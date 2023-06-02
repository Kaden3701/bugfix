## Stripclub storyline Mod by Corrado
#  BDSM performers role definition.
#  The role is appended to BDSM performers after they start to work for you.

init 5 python:

    def get_bdsm_exhibitions(person):
        return person.event_triggers_dict.get("exhibitions", 0)

    def increase_bdsm_exhibitions(person):
        person.event_triggers_dict["exhibitions"] = get_bdsm_exhibitions(person) + 1
        return

    def strip_club_bdsm_dildochair_MC_requirements(the_person):
        if the_person.has_role(stripclub_bdsm_performer_role):
            if mc.location is bdsm_room:
                return True
        return False

    def strip_club_bdsm_dildochair_Mistress_requirements(the_person):
        if the_person.has_role(stripclub_bdsm_performer_role):
            if mc.location is bdsm_room:
                if strip_club_get_mistress() in mc.location.people:
                    return True
        return False

    def strip_club_hire_bdsm_performer(person):
        stripclub_bdsm_performers.append(person)

    def strip_club_fire_bdsm_performer(person):
        if person in stripclub_bdsm_performers:
            stripclub_bdsm_performers.remove(person)

    strip_club_dildochair_MC_action = Action("Use the dildo chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_MC_requirements, "strip_club_bdsm_dildochair_MC_label", menu_tooltip = "Use the dildo chair with your BDSM performer.")
    strip_club_dildochair_Mistress_action = Action("Mistress use the chair {image=gui/heart/Time_Advance.png}", strip_club_bdsm_dildochair_Mistress_requirements, "strip_club_bdsm_dildochair_Mistress_label", menu_tooltip = "Have the Mistress use the dildo chair with your BDSM performer.")

    stripclub_bdsm_performer_role = Role("BDSM performer", [promote_to_manager_action, strip_club_stripper_move_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action, strip_club_dildochair_MC_action, strip_club_dildochair_Mistress_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

    def strip_club_get_caged():
        caged = people_in_role(caged_role)
        if __builtin__.len(caged) > 0:
            return caged[0]
        return None

    def strip_club_cage_her_requirements(the_person):
        if the_person.has_role(caged_role):
            return False
        if mc.location is bdsm_room:
            caged = people_in_role(caged_role)
            if __builtin__.len(caged) < 2:
                return True
        return False

    def strip_club_caged_strip_requirements(the_person):
        if the_person.has_role(caged_role):
            if the_person.tits_available and the_person.vagina_available:
                return False
            return True
        return False

    def strip_club_caged_actions_milk_her_requirements(the_person):
        if the_person.has_role(caged_role):
            if the_person.tits_available:
                return True
            else:
                return "Obstructed by Clothing"
        return False

    def strip_club_caged_actions_blowjob_requirements(the_person):
        return the_person.has_role(caged_role)

    def strip_club_caged_actions_release_requirements(the_person):
        return the_person.has_role(caged_role)

    def strip_club_caged_actions_sex_requirements(the_person):
        if the_person.has_role(caged_role):
            if the_person.vagina_available:
                return True
            else:
                return "Obstructed by Clothing"
        return False

    def add_strip_club_cage_her_action_to_mc_actions():
        strip_club_cage_her_action = Action("Cage her", strip_club_cage_her_requirements, "cage_her_label", menu_tooltip = "Put her in the cage.")
        mc.main_character_actions.append(strip_club_cage_her_action)

    def strip_club_cage_role_on_turn(person):
        amount = __builtin__.min((210 - person.obedience)/10, 5) # slowly decaying increase of obedience.
        if amount > 0:
            person.change_obedience(5)

    def strip_club_cage_role_on_move(person):
        person.change_location(bdsm_room)

    def strip_club_cage_role_on_day(person):
        person.clear_situational_slut("being_caged")
        person.clear_situational_obedience("being_caged")
        person.remove_role(caged_role)
        person.apply_planned_outfit()

    caged_strip_action = Action("Strip her", strip_club_caged_strip_requirements, "caged_strip_label", menu_tooltip = "Strip the caged girl.")
    caged_get_milked_action = Action("Milk her", strip_club_caged_actions_milk_her_requirements, "caged_get_milked_label", menu_tooltip = "Milk the caged girl.")
    caged_BJ_action = Action("Get a BJ from her", strip_club_caged_actions_blowjob_requirements, "caged_BJ_label", menu_tooltip = "Get a BJ from the caged girl.")
    caged_doggy_action = Action("Fuck her Doggy style", strip_club_caged_actions_sex_requirements, "caged_doggy_label", menu_tooltip = "Fuck the caged girl Doggy style.")
    caged_anal_doggy_action = Action("Fuck her anally", strip_club_caged_actions_sex_requirements, "caged_anal_doggy_label", menu_tooltip = "Anal fuck the caged girl Doggy style.")
    caged_release_action = Action("Release her from the cage", strip_club_caged_actions_release_requirements, "caged_release_label", menu_tooltip = "Release girl from the cage.")

    caged_role = Role("CAGED !", [caged_strip_action, caged_BJ_action, caged_doggy_action, caged_anal_doggy_action, caged_release_action], \
        on_turn = strip_club_cage_role_on_turn, on_move = strip_club_cage_role_on_move, on_day = strip_club_cage_role_on_day, hidden = True)

init -1 python:
    def strip_club_bdsm_strip_description(the_person, the_item, the_group):
        test_outfit = the_person.outfit.get_copy()
        test_outfit.remove_clothing(the_item)
        if test_outfit.tits_visible and not the_person.tits_visible:
            if person.has_taboo("bare_tits"):
                renpy.say(None, the_person.title + " glances around nervously.")
                renpy.say(the_person.char, "Maybe I can keep my bra on?")
                renpy.say(mc.name, "Relax " + person.title + ", it's your job! Come on, get those tits out for us.")
                renpy.say(the_person.char, "Okay, okay...")

            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            if the_person.has_large_tits:
                renpy.say(None, the_person.title + " pulls off her " + the_item.display_name + ". Her [the_person.tits_description] jiggle briefly as they're released.")
            else: #Peepers
                renpy.say(None, the_person.title + " pulls off her " + the_item.display_name + ", setting her [the_person.tits_description] free.")

            if person.has_taboo("bare_tits"):
                renpy.say(None, the_person.title + " tries to keep her breasts covered with her hands, cheeks red.")
                the_person.break_taboo("bare_tits")

        elif test_outfit.vagina_visible and not the_person.vagina_visible:
            if the_person.has_taboo("bare_pussy"):
                renpy.say(None, the_person.title + " starts to move her " + the_item.display_name + ", but hesitates.")
                renpy.say(the_person.char, "Should I really remove my "+ the_item.display_name + "?")
                renpy.say(mc.name, "Come on " + the_person.title + ", it's your job and the reason we're here.")
                renpy.say(None, "She takes a deep breath and gathers up her courage.")
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say(None, the_person.title + " pulls her " + the_item.display_name + " down, peeling them away from her pussy.")

            if the_person.has_taboo("bare_pussy"):
                renpy.say(None, the_item.display_name + " off, " + the_person.title + " cover herself as she can, blushing a fierce red.")
                the_person.break_taboo("bare_pussy")

        elif the_person.has_taboo("underwear_nudity") and test_outfit.underwear_visible and not the_person.underwear_visible:
            renpy.say(None, the_person.title + " glances around nervously.")
            renpy.say(the_person.char, "You don't really want me to take off my " + the_item.display_name + ", do you? I'll just have my underwear on...")
            renpy.say(mc.name, "Come on " + the_person.title + ", that's the whole point of this place! Nobody cares about you just wearing your underwear.")
            renpy.say(None,"She bites her lip as she considers it, then takes a deep breath.")
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say(None, the_person.title + " pulls off her " + the_item.display_name + " and drops it on the floor.")
            renpy.say(the_person.char, "There, I did it.")
            the_person.break_taboo("underwear_nudity")

        else:
            the_group.draw_animated_removal(the_person, make_primary = True, the_clothing = the_item)
            renpy.say(None, the_person.title + " takes her " + the_item.display_name + " off and drops it on the floor.")
            pass

        the_person.update_outfit_taboos()
        return

    def dildochair_pleasure_loop_allow_orgasm(person, is_punishment = False):
        if is_punishment:
            if person.arousal_perc > 70:
                renpy.say(the_person.char, "Please " + the_person.mc_title + ", I promise I will be the best slave you ever had, please... let me cum!")
        elif person.arousal_perc >= 100:
            scene_manager.update_actor(person, emotion = "orgasm")
            renpy.say(person.char, "Oh my god, I'm cumming... Ahhh... YES!... please " + person.mc_title + ", increase the speed!")
            scene_manager.update_actor(person, emotion = "happy")
            person.have_orgasm(sluttiness_increase_limit = 80)
        return

    def dildochair_pleasure_loop_intensity(person, arousal = 0, energy = 0):
        for count in __builtin__.range(5):
            renpy.say(person.char, "Bzzz !... " + (renpy.random.choice(["Ahh!", "Yes!", "Fuck!", "Oh!"]) if count%2 == 0 else ""), interact = False)
            person.change_stats(arousal = arousal, energy = energy, add_to_log = False)
            renpy.pause(1)
        return

label strip_club_advance_time_label():
    if time_of_day == 4:
        "Tired after you spent the night at the club, you go back home, to have a good night's rest."
        $ mc.change_location(bedroom)
    call advance_time from _call_advance_time_strip_club_end_of_day
    return

label strip_club_bdsm_dildochair_MC_label(the_person): # MC use the dildo chair with her
    $ scene_manager = Scene()
    "You decide it's time for [the_person.title] to have some fun, so you approach the chair and set up..."
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 2:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mc.name "Ok, [the_person.title]... Come here and take off your clothes!"
    $ scene_manager.add_actor(the_person, position = "stand4", emotion = "happy")
    the_person "Okay, whatever you want [the_person.mc_title]."
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_chaired", 8, "Everyone can see the slut I am...")
    "She starts to strip down for you."
    $ scene_manager.strip_full_outfit(person = the_person)
    the_person "Are you planning something naughty for me, [the_person.mc_title]?"
    menu:
        "Reward her (tooltip)Let her orgasm":
            mc.name "Since you've been a good girl [the_person.title], I will let you have as many orgasm as your body can take."
            if mc.location.person_count > 1 and get_bdsm_exhibitions(the_person) <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person "I'm your slave [the_person.mc_title], I'll do as you command."
            mc.name "Sit on this chair [the_person.title], I'm going to restrain you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 2:
                the_person "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mc.name "I think your pussy will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mc.name "I think your lil' asshole will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                "She obeys your command and takes a seat."
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
            else:
                "She obeys your command and takes a seat."
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Her eyes are glued to yours while you slowly slips the big dildos inside both her holes."
            "You lock the belts on her legs, arms, neck and stomach, she is unable to move her body away from the device."
            the_person "Oh my god! I feel..."
            mc.name "That your master owns you? You're my good slave, and good slaves should be rewarded."
            $ the_person.change_obedience (5)
            call strip_club_bdsm_dildochair_pleasure_loop(the_person, is_punishment = False) from _call_strip_club_bdsm_dildochair_MC_label_reward
        "Punish her (tooltip)Deny her orgasm":
            mc.name "Since you've not been a good slave [the_person.title], you will be pleasured, but you're not allowed to orgasm."
            $ scene_manager.update_actor(the_person, emotion = "sad", position = "stand4")
            if get_bdsm_exhibitions(the_person) <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person "I'm your slave [the_person.mc_title], I'll do as you command."
            mc.name "Sit on this chair [the_person.title], I'm going to restrain you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 2:
                the_person "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mc.name "I think your pussy is the right place for this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mc.name "I think your lil' asshole is the right place for this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                "She obeys your command and takes a seat."
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
            else:
                "She obeys your command and takes a seat."
                $ scene_manager.update_actor(the_person, position = "sitting")
                "Her eyes are glued to yours while she slowly slips the big dildos inside both her holes."
            "You lock the belts on her legs, arms, neck and stomach, she is unable to move her body away from the device."
            the_person "Oh my god! I feel..."
            mc.name "That your master owns you? That's the right feeling, even if you're not yet a good slave."
            $ the_person.change_obedience (5)
            call strip_club_bdsm_dildochair_pleasure_loop(the_person, is_punishment = True) from _call_strip_club_bdsm_dildochair_MC_label_punishment
    python:
        increase_bdsm_exhibitions(the_person)
        the_person.reset_arousal()
        the_person.clear_situational_slut("being_chaired")
        scene_manager.clear_scene()
        clear_scene()

    call strip_club_advance_time_label from _call_strip_club_advance_time_label_1
    return


label strip_club_bdsm_dildochair_pleasure_loop(the_person, mistress = None, is_punishment = False):
    "You turn on the chair and set the vibrations at:"
    menu dildochair_reward_menu:
        "Speed 1 (tooltip)Slowly increase her arousal" if the_person.energy >= 5: # Each action use 10 energy and give 10 arousal and 1 obedience
            "A feeble buzz can be heard in the room, [the_person.title] bites her lip."
            $ dildochair_pleasure_loop_intensity(the_person, arousal = 3, energy = -1)
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                the_person "It's such a pleasant feeling, this thing tickles my pussy very nicely!"
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                the_person "It's such a pleasant feeling, having both my holes filled so good!"
            else: # One dildo in the ass
                the_person "It's such a good feeling, having my ass stimulated like this!"
            $ the_person.change_obedience (1, add_to_log = False)
            $ dildochair_pleasure_loop_allow_orgasm(the_person, is_punishment)
            "You decide what to do next."
            jump dildochair_reward_menu
        "Speed 1\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 5:
            pass
        "Speed 2 (tooltip)Moderately increase her arousal" if the_person.energy >= 10: # Each action use 10 energy and give 20 arousal and 2 obedience
            "A soft buzz can be heard in the room, [the_person.title] bite her lips moaning."
            $ dildochair_pleasure_loop_intensity(the_person, arousal = 5, energy = -2)
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                the_person "It's such a pleasant feeling, this thing tickles my pussy very nicely!"
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                the_person "It's such a pleasant feeling, having both my holes filled so good!"
            else: # One dildo in the ass
                the_person "It's such a good feeling, having my ass stimulated like this!"
            $ the_person.change_obedience (2, add_to_log = False)
            $ dildochair_pleasure_loop_allow_orgasm(the_person, is_punishment)
            "You decide what to do next."
            jump dildochair_reward_menu
        "Speed 2\n{color=#ff0000}{size=18}Requires at least 10 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 10:
            pass
        "Speed 3 (tooltip)Strongly increase her arousal" if the_person.energy >= 15: # Each action use 10 energy and give 30 arousal and 3 obedience
            "A buzz can be heard in the room, [the_person.title] bites her lips moaning loudly."
            $ dildochair_pleasure_loop_intensity(the_person, arousal = 7, energy = -3)
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                the_person "Ahh! This feeling is amazing, this cock fills my pussy so good!"
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                the_person "Ahh! This feeling is amazing, both my holes are stuffed so good!"
            else: # One dildo in the ass
                the_person "Ahh! This feeling is amazing, this cock fills my ass so good!"
            $ the_person.change_obedience (3, add_to_log = False)
            $ dildochair_pleasure_loop_allow_orgasm(the_person, is_punishment)
            "You decide what to do next."
            jump dildochair_reward_menu
        "Speed 3\n{color=#ff0000}{size=18}Requires at least 15 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 15:
            pass
        "Max speed (tooltip)Extraordinarily increase her arousal" if the_person.energy >= 25: # Each action use 10 energy and give 40 arousal and 4 obedience
            "A loud buzz can be heard in the room, [the_person.title]'s tongue is out and begs to lick something!"
            $ dildochair_pleasure_loop_intensity(the_person, arousal = 10, energy = -5)
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                the_person "Oh YES! YES! Tear my pussy apart with that dong, more, give me more!"
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                the_person "Oh! YES! YES! Keep pumping my holes, more, give me more!"
            else: # One dildo in the ass
                the_person "Oh! YES! YES! Wreck my ass with this monster, more, give me more!"
            $ the_person.change_obedience (4, add_to_log = False)
            $ dildochair_pleasure_loop_allow_orgasm(the_person, is_punishment)
            "You decide what to do next."
            jump dildochair_reward_menu
        "Max speed\n{color=#ff0000}{size=18}Requires at least 25 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if the_person.energy < 25:
            pass
        "Change your mind (tooltip)Change your mind and let her cum." if is_punishment and the_person.energy >=25 and the_person.arousal_perc >= 80:
            "You decide to let her finally cum, and you set the chair to its maximum speed."
            "A loud buzz can be heard in the room, [the_person.title]'s tongue is out crying out in pleasure!"
            $ dildochair_pleasure_loop_intensity(the_person, arousal = 10, energy = -5)
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1: # One dildo in the pussy
                the_person "Oh YES! YES! Tear my pussy apart with that dong, more, give me more!"
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 2: # Two dildos
                the_person "Oh! YES! YES! Keep pumping my holes, more, give me more!"
            else: # One dildo in the ass
                the_person "Oh! YES! YES! Wreck my ass with this monster, more, give me more!"
            $ scene_manager.update_actor(the_person, emotion = "orgasm")
            "She finally reaches her coveted orgasm, the chair is now wet with her flowing juices."
            $ the_person.change_stats(obedience = 5, happiness = 10, love = 2)
            $ scene_manager.update_actor(the_person, emotion = "happy")
            $ the_person.have_orgasm()
            the_person "Thank you [the_person.mc_title], make me cum like this and I'll be your devoted slave!"
            "You release her from the chair and let her dress."
            $ the_person.apply_planned_outfit()
            $ scene_manager.update_actor(the_person, position = "stand3")
            "She still can't properly stand on her trembling legs."
        "Release her":
            if mistress:
                if is_punishment:
                    "While you stop the chair she begs you."
                    the_person "Please [the_person.mc_title]... Master! Yes, Master... Please, let me cum at least one time!"
                    mc.name "[mistress.title], untie [the_person.title]... I think she had enough fun."
                else:
                    mc.name "Please [mistress.title], untie [the_person.title]... I think she can't resist anymore."
                $ scene_manager.update_actor(mistress, position = "standing_doggy")
                mistress "Sure thing, Master!"
                $ scene_manager.update_actor(mistress, position = "stand4")
                $ scene_manager.update_actor(the_person, position = "stand5")
                "She still can't properly stand on her trembling legs."
                if is_punishment:
                    the_person "I'm exhausted, but I got your lesson [the_person.mc_title], I promise I'll be your devoted slave."
                    mc.name "Very well, now get dressed, my little pet."
                else:
                    the_person "I'm exhausted, but it was worth every second, thank you Master for granting your slave this much pleasure!"
                    mc.name "Please me and you'll be pleased. Now you can get dressed."
                $ the_person.apply_planned_outfit()
                $ scene_manager.draw_scene()
                $ the_person.change_stats(obedience = 5, happiness = 10, love = 2)
                $ mistress.change_stats(obedience = 3)
                "Her eyes are full of love for her Master."
            elif the_person.energy < 15:
                the_person "I'm exhausted, but I got your lesson [the_person.mc_title], I promise I'll be your devoted slave."
                mc.name "Please me and you'll be pleased, now put on your clothes."
                "You release her from the chair's restraints."
                $ the_person.apply_planned_outfit()
                $ scene_manager.update_actor(the_person, position = "stand3", emotion = "sad")
                $ the_person.change_stats(obedience = 5)
                "Her eyes are full of love for her Master."
            elif the_person.arousal_perc >= 90:
                "While you stop the chair and start to release the restraints she looks at you with hopeful eyes."
                the_person "Please [the_person.mc_title]... Master! Yes, Master... Please, let me cum at least one time!"
                mc.name "I will consider your request for the next time, Slave. Now you can get dressed."
                $ the_person.apply_planned_outfit()
                $ scene_manager.update_actor(the_person, position = "stand3", emotion = "sad")
                $ the_person.change_stats(obedience = 5, happiness = -5)
                the_person "I promise I'll do my best to please my Master!"
            else:
                "After a while you turn off the chair and remove her restraints."
                the_person "Already, please Master can I please you a little longer next time?"
                mc.name "Perhaps, continue to serve me and I might grant your request, now put on your clothes"
                $ the_person.apply_planned_outfit()
                $ scene_manager.update_actor(the_person, position = "stand3", emotion = "sad")
                $ the_person.change_stats(obedience = 5, happiness = -5)
                the_person "As you wish, my Master!"
    return

label strip_club_bdsm_dildochair_Mistress_label(the_person): # The Mistress use the dildo chair with her
    $ scene_manager = Scene()
    $ mistress = strip_club_get_mistress()
    "You ask [mistress.possessive_title] to set up the dildo chair so you can have some fun with [the_person.possessive_title]."
    $ scene_manager.add_actor(mistress, position = "stand4", emotion = "happy")
    mistress "Sure [mistress.mc_title], how many dildos do you want me to install on the chair?"
    menu:
        "One dildo":
            $ the_person.event_triggers_dict["dildochair_dildos"] = 1
        "Two dildos" if the_person.get_opinion_score("anal sex") >= 2:
            $ the_person.event_triggers_dict["dildochair_dildos"] = 2
    mistress "Ok, [the_person.fname]... Come here and take off your clothes!"
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "stand3", emotion = "happy")
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_chaired", 8, "Everyone can see the slut I am...")
    the_person "Okay Mistress, whatever [the_person.mc_title] wants."
    "She starts to strip down while she looks at you."
    $ scene_manager.strip_full_outfit(person = the_person)
    the_person "Are you guys planning something naughty for me?"
    menu:
        "Reward her (tooltip)Let her orgasm":
            mc.name "[the_person.title], since you've been a good girl I'll let [mistress.title] give you as many orgasm as your body can take."
            if mc.location.person_count > 2 and get_bdsm_exhibitions(the_person) <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person "Really [mistress.title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person "Really [mistress.title]? I don't know if I..."
            else:
                the_person "I'm [the_person.mc_title]'s slave [mistress.title], and a slave obeys."
            $ scene_manager.update_actor(mistress, position = "stand5")
            mistress "Sit on this chair [the_person.fname], I'm going to restrain you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 2:
                the_person "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mistress "I think your pussy will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mistress "I think your lil' asshole will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                $ scene_manager.update_actor(the_person, position = "sitting")
                "She obeys the Mistress's command and sits down."
                "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
            else:
                $ scene_manager.update_actor(the_person, position = "sitting")
                "She obeys the Mistress's command and sits down."
                "Her eyes are glued to yours while she slowly slips the big dildos inside both her holes."
            $ scene_manager.update_actor(mistress, position = "standing_doggy")
            "[mistress.possessive_title] locks the belts on her legs, arms, neck and stomach, she is unable to move her body away from the device."
            $ scene_manager.update_actor(the_person, emotion = "default")
            the_person "Oh my god! I feel..."
            mistress "That your master owns you? You're a good slave, and good slaves should be rewarded."
            $ scene_manager.update_actor(mistress, position = "stand4")
            $ scene_manager.update_actor(the_person, emotion = "happy")
            call strip_club_bdsm_dildochair_pleasure_loop(the_person, mistress = mistress, is_punishment = False) from _call_strip_club_bdsm_dildochair_Mistress_reward
        "Punish her (tooltip)Deny her orgasm":
            mc.name "Since you've not been a good slave [the_person.title], you will be pleasured but you're not allowed to orgasm."
            $ scene_manager.update_actor(the_person, emotion = "sad", position = "stand4")
            if get_bdsm_exhibitions(the_person) <= 3 and the_person.get_opinion_score("public sex") <= 0: # She's still a bit shy
                the_person "Really [the_person.mc_title]? Here in front of everyone? I don't know if I..."
            elif the_person.obedience <= 200:
                the_person "Really [the_person.mc_title]? I don't know if I..."
            else:
                the_person "I'm [the_person.mc_title]'s slave [mistress.title], and a slave obeys."
            $ scene_manager.update_actor(mistress, position = "stand5")
            mistress "Sit on this chair [the_person.fname], I'm going to restrain you."
            if the_person.event_triggers_dict.get("dildochair_dildos") == 1 and the_person.get_opinion_score("anal sex") >= 2:
                the_person "Where should I put the dildo?"
                menu:
                    "Vaginal fun":
                        mistress "I think your pussy will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
                    "Anal fun":
                        $ the_person.event_triggers_dict["dildochair_dildos"] = 3
                        mistress "I think your lil' asshole will be pleased by this toy!"
                        $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
                        "Her eyes are glued to yours while she slowly slips the big dildo inside her asshole."
            elif the_person.event_triggers_dict.get("dildochair_dildos") == 1:
                $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
                "She obeys the Mistress's command and sits down."
                "Her eyes are glued to yours while she slowly slips the big dildo inside her pussy."
            else:
                $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
                "She obeys the Mistress's command and sits down."
                "Her eyes are glued to yours while she slowly slips the big dildos inside both her holes."
            $ scene_manager.update_actor(mistress, position = "standing_doggy")
            "[mistress.possessive_title] locks the belts on her legs, arms, neck and stomach, she is unable to move her body away from the device."
            $ scene_manager.update_actor(the_person, emotion = "default")
            the_person "Oh my god! I feel..."
            mistress "That your master owns you? You're a bad slave, and bad slaves should be punished."
            $ scene_manager.update_actor(mistress, position = "stand4")
            $ the_person.change_obedience (5)
            call strip_club_bdsm_dildochair_pleasure_loop(the_person, mistress = mistress, is_punishment = True) from _call_strip_club_bdsm_dildochair_Mistress_punishment

    python:
        increase_bdsm_exhibitions(the_person)
        the_person.reset_arousal()
        the_person.clear_situational_slut("being_chaired")
        scene_manager.clear_scene()
        clear_scene()
        del mistress

    call strip_club_advance_time_label from _call_strip_club_advance_time_label_2
    return

label cage_her_label(the_person):
    mc.name "I think some time in the cage will improve your attitude."
    if the_person.obedience < 100:
        $ the_person.draw_person(position = "stand3", emotion = "angry")
        the_person "What? Are you crazy?"
        mc.name "Oh, don't worry [the_person.title], you'll enjoy it!"
        if the_person.sluttiness < 60:
            the_person "There's absolutely no way I'll do it... Never in my life!"
            "Maybe I need to work a bit on her obedience or her sluttiness before she'll agree to this..."
            mc.name "Ok [the_person.title], but never say never!"
            return
        else:
            $ the_person.draw_person(position = "stand3", emotion = "sad")
            the_person "It's so degrading... Do you promise me it'll be worth it?"
            mc.name "Have you ever been disappointed by your master?"
            "She looks deeply in your eyes, you can see her deepest dirty fantasies invade her mind."
            "Then, without a word, she kneels and enters the cage."
    elif the_person.obedience < 200:
        $ the_person.draw_person(position = "stand3", emotion = "default")
        the_person "Are you sure it's really necessary?"
        mc.name "That's what I want from you right now, do you want to disappoint your master?"
        "She knows there's no return from this; if she accepts this she will forever be in your power."
        "Then, without a word, she kneels and enters the cage."
    else:
        $ the_person.draw_person(position = "stand3", emotion = "happy")
        the_person "As you wish, [the_person.mc_title]."
        "Then she kneels and enters the cage."
    $ the_person.add_role(caged_role)
    $ ran_num = renpy.random.randint(1,3)
    if ran_num == 1:
        $ the_person.draw_person(position = "kneeling1")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "kneeling1"
    elif ran_num == 2:
        $ the_person.draw_person(position = "blowjob")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "blowjob"
    else:
        $ the_person.draw_person(position = "cowgirl")
        $ the_person.event_triggers_dict["bdsm_room_pose"] = "cowgirl"
    if not "caged_actions" in the_person.event_triggers_dict:
        $ the_person.event_triggers_dict["caged_actions"] = 0
    if the_person.follow_mc:
        $ the_person.follow_mc = False
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    $ the_person.add_situational_obedience("being_caged", 10, "I am completely at his mercy.")
    "She now awaits your next move."
    return

label caged_strip_label(the_person):
    mc.name "I want you to be naked, remove your clothes."
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    $ naked_strip_description(the_person)
    the_person "Is my master pleased?"
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_get_milked_label(the_person):
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    # TODO
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_BJ_label(the_person):
    "You unzip your pants and pull out your dick in front of the cage."
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    if the_person.has_cum_fetish or the_person.get_opinion_score("giving blowjobs") > 0:
        $ the_person.draw_person(position = "cowgirl", emotion = "happy")
        the_person "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "cowgirl", emotion = "default")
        the_person "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person "If it's the only way to please my master..."
        else:
            the_person "Don't you think it's degrading enough for me to being inside... 'this'?"
            "Your gaze fixed in her eyes, you start a willingness fight: you know the first one who looks down loses..."
            "After a few seconds [the_person.title] realize where she is and, aware, looks down at the tip of your shoes."
            mc.name "My dear slave... Open your mouth, would you?"
    call fuck_person(the_person, private = False, start_position = blowjob, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_BJ
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_doggy_label(the_person):
    "The sight of [the_person.title] being so powerless intrigues you."
    "With your hand between the bars you start to caress [the_person.title]'s buttocks."
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    "Meanwhile your finger plays with [the_person.title]'s wet pussy, with the other hand you unzip your pants and set your hard dick free."
    if the_person.has_breeding_fetish or the_person.get_opinion_score("doggy style sex") > 0:
        $ the_person.draw_person(position = "doggy", emotion = "happy")
        the_person "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "doggy", emotion = "default")
        the_person "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person "If it's the only way to please my master..."
        else:
            the_person "Don't you think it's degrading enough for me to being inside... 'this'?"
            "Disappointed by her behaviour you slap her pussy and [the_person.title] moans loudly: she can't deny anymore what her body desperately wants."
            mc.name "My dear slave... Push your ass closer, would you?"
    call fuck_person(the_person, private = False, start_position = doggy, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_doggy
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_anal_doggy_label(the_person):
    "Everyone can now see that [the_person.title] belongs to you... But there is a little something more you can do."
    "With your hand between the bars you start to caress [the_person.title]'s buttocks."
    if mc.location.person_count > 1: # There's other people around
        $ the_person.add_situational_slut("being_caged", 8, "Everyone can see the slut I am...")
    if the_person.get_opinion_score("public sex") >= 0:
        $ the_person.add_situational_slut("being_used_in_the_cage", (the_person.get_opinion_score("public sex")*5 +5), "Everyone can see the slut I am...")
    "Meanwhile your finger circles [the_person.title]'s asshole, with the other hand you unzip your pants and set your hard dick free."
    if the_person.has_role(anal_fetish_role) or the_person.get_opinion_score("anal sex") >= 2:
        $ the_person.draw_person(position = "doggy", emotion = "happy")
        the_person "Oh! I like where this is going!"
    else:
        $ the_person.draw_person(position = "doggy", emotion = "default")
        the_person "Oh! I think I know what you want..."
        if the_person.obedience >= 150:
            the_person "If it's the only way to please my master..."
        else:
            the_person "Don't you think it's degrading enough for me, being inside... 'this'?"
            "Disappointed by her behaviour, you finger her asshole and [the_person.title] moans loudly, she can't deny anymore what her body disparately wants."
            mc.name "My dear slave... Spread your cheeks, would you?"
    call fuck_person(the_person, private = False, start_position = doggy_anal, start_object = bdsm_room.get_object_with_name("Cage"), skip_intro = True, girl_in_charge = False, position_locked = True, ignore_taboo = True, affair_ask_after = False) from _call_caged_doggy_anal
    $ the_person.clear_situational_slut("being_used_in_the_cage")
    $ the_person.event_triggers_dict["caged_actions"] += 1
    return

label caged_release_label(the_person):
    mc.name "You can leave the cage now."
    $ the_person.clear_situational_slut("being_caged")
    $ the_person.clear_situational_obedience("being_caged")
    $ the_person.remove_role(caged_role)
    $ the_person.draw_person(position = "stand3", emotion = "happy")
    if the_person.event_triggers_dict.get("caged_actions") <= 2:
        if the_person.obedience <= 150:
            the_person "I hope you got me out just to have some more fun with me!"
        else:
            the_person "I hope my performance has pleased my master."
    else:
        if the_person.obedience <= 150:
            the_person "Actually I was starting to enjoy the place!"
        else:
            the_person "I'm happy my master played with me!"
    $ the_person.apply_planned_outfit()
    return
