#Cousin Role Action Requirements
init 4 python:
    list_of_instantiation_functions.append("create_gabrielle_character")

    def get_cousin_role_actions():
        #COUSIN ACTIONS#
        cousin_blackmail_action = Action("Blackmail her", cousin_blackmail_requirement, "cousin_blackmail_label",
            menu_tooltip = "Threaten to tell her mother about what she's been doing and see what you can get out of her.", priority = 10)
        return [cousin_blackmail_action]

    def create_gabrielle_character():
        ### COUSIN ###
        cousin_wardrobe = wardrobe_from_xml("Cousin_Wardrobe")

        global cousin
        cousin = create_random_person(name = "Gabrielle", last_name = aunt.last_name, age = 18, body_type = "curvy_body", face_style = "Face_3", tits = "DDD", height = 0.98, hair_colour = "black", hair_style = messy_short_hair, skin="white",\
            eyes = "brown", personality = cousin_personality, name_color = "#9c4dea", dial_color = "#9c4dea", starting_wardrobe = cousin_wardrobe, start_home = cousin_bedroom, \
            stat_array = [0,4,2], skill_array = [0,0,2,1,0], sex_skill_array = [3,0,0,0], sluttiness = 8, obedience = 70, happiness = 70, love = -20, \
            title = "Gabrielle", possessive_title = "Your cousin", mc_title = mc.name, relationship = "Single", kids = 0,type="story")

        global cousin_role
        cousin_role = Role("Cousin", get_cousin_role_actions())

        cousin.add_role(cousin_role)
        cousin.change_job(unemployed_job)
        cousin.set_schedule(cousin_bedroom) #Hide them in their bedroom off the map until they're ready
        cousin.home.add_person(cousin)

        # kissing an groping are the only actions open for Gabrielle, it's too difficult when they are 'hated'
        cousin.set_opinion("kissing", 1, False)
        cousin.set_opinion("being fingered", 2, False)
        # Goth so must love black
        cousin.set_opinion("the colour black", 2, True)

        town_relationships.update_relationship(mom, cousin, "Niece", "Aunt")
        town_relationships.update_relationship(aunt, cousin, "Daughter", "Mother")
        town_relationships.update_relationship(lily, cousin, "Cousin")

init -2 python:
    cousin_strip_pose_list = ["walking_away","back_peek","standing_doggy","stand2","stand3","stand4","stand5"] #A list to let us randomly get some poses so each dance is a little different.

    def cousin_intro_phase_one_requirement(day_trigger):
        return day >= day_trigger and time_of_day == 4

    def cousin_house_phase_one_requirement(day_trigger):
        return day >= day_trigger

    def cousin_house_phase_two_requirement(the_person):
        return the_person.location == hall

    def cousin_house_phase_three_requirement(day_trigger):
        return day>= day_trigger

    def cousin_blackmail_intro_requirement(the_person):
        #Only triggers when she's in there alone (and after the event has been added to the trigger list)
        return the_person.location == lily_bedroom and lily_bedroom.person_count == 1 and the_person.event_triggers_dict.get("blackmail_level", -1) < 0

    def cousin_blackmail_requirement(the_person):
        if the_person.event_triggers_dict.get("blackmail_level", -1) < 1:
            return False
        elif day < the_person.event_triggers_dict.get("last_blackmailed",-5) + 5:
            return "Blackmailed too recently"
        elif mc.location.person_count > 1:
            return "Must be in private"
        return True

    def stripclub_show_requirement():
        # check available strippers in club (not possible strippers)
        if __builtin__.len([x for x in stripclub_strippers if x in mc.location.people]) == 0:
            return False
        if time_of_day in [0,1,2]:
            return "Too early for performances"
        if get_strip_club_foreclosed_stage() < 5 and not mc.business.has_funds(20):
            return "Not enough cash"
        return True

    def blackmail_hint_requirement(the_person, min_day):
        if day < min_day or time_of_day != 4:
            return False
        elif the_person.sluttiness < 25:
            return False
        elif the_person.event_triggers_dict.get("blackmail_level",-1) != 1:
            return False
        return True

    def cousin_room_search_requirement(the_person):
        if the_person.event_triggers_dict.get("blackmail_level",-1) != 1:
            return False
        elif the_person.event_triggers_dict.get("found_stripping_clue", False):
            return False
        elif time_of_day == 4:
            return "Too late to search room"
        elif the_person.location == mc.location:
            return the_person.title + " is in the room."
        return True

    def blackmail_2_confront_requirement(the_person):
        if the_person.event_triggers_dict.get("blackmail_level", -1) != 1:
            return False
        elif mc.location.person_count > 1:
            return "Not with other people around"
        elif the_person.get_destination() == strip_club:
            return "Not in the strip club"
        return True

    def cousin_boobjob_ask_requirement(the_person, start_day):
        if day < start_day or the_person.sluttiness < 40:
            return False
        elif the_person.event_triggers_dict.get("getting boobjob", False):
            return False
        elif Person.rank_tits(the_person.tits) >= Person.rank_tits("F"):
            return False #She already has F sized tits, which she thinks is good enough.
        elif aunt.location == mc.location:
            return False
        return True

    def cousin_talk_boobjob_again_requirement(the_person):
        if the_person.sluttiness < 40:
            return False
        elif the_person.event_triggers_dict.get("getting boobjob", False):
            return False
        elif aunt.location == mc.location:
            return "Not while [aunt.title] is around"
        else:
            return True

    def cousin_new_boobs_brag_requirement(the_person):
        return not aunt.location == mc.location

    def cousin_boobjob_get_requirement(the_person, start_day):
        return day >= start_day

    def cousin_tits_payback_requirement(the_day):
        return day >= the_day

    def cousin_serum_boobjob_check_requirement(the_person, the_tits, the_day):
        return day >= the_day

    def add_cousin_blackmail_hint_action(the_person):
        the_person.set_schedule(hall, the_days = [0, 1, 2, 3, 4], the_times = [2])
        the_person.event_triggers_dict["blackmail_level"] = 1

        blackmail_2_event = Action("Blackmail hint", blackmail_hint_requirement, "aunt_cousin_hint_label", args = [aunt, the_person], requirement_args = [the_person, day + renpy.random.randint(2,4)])
        mc.business.mandatory_crises_list.append(blackmail_2_event)
        return

    def add_cousin_serum_boobjob_check_action(the_person):
        cousin_serum_boobjob_check_action = Action("Cousin serum boobjob check", cousin_serum_boobjob_check_requirement, "cousin_serum_boobjob_label", args = [the_person, the_person.tits], requirement_args = [the_person, the_person.tits, day + 3])
        mc.business.mandatory_crises_list.append(cousin_serum_boobjob_check_action)
        return

    def add_cousin_boobjob_get_action(the_person):
        #Sets up an event that will trigger after a set number of days when she has gotten her boob job. This event, in turns, adds in an event when you talk to her.
        the_person.event_triggers_dict["getting boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
        cousin_boobjob_get_action = Action("Cousin boob job get", cousin_boobjob_get_requirement, "cousin_boobjob_get_label", args = the_person, requirement_args = [the_person, day + renpy.random.randint(4,6)])
        mc.business.mandatory_crises_list.append(cousin_boobjob_get_action)
        return

    def add_cousin_tits_payback_action(the_person, amount):
        cousin_tits_payback_action = Action("cousin tits payback", cousin_tits_payback_requirement, "cousin_tits_payback_label", args = [the_person, amount], requirement_args = day + 7)
        mc.business.mandatory_crises_list.append(cousin_tits_payback_action) #An event where she sends you some cash in a week, which if it has not finished then re-adds itself with the new amount
        return

    def add_cousin_blackmail_2_confront_action():
        blackmail_2_confront_action = Action("Confront her about her stripping", blackmail_2_confront_requirement, "cousin_blackmail_level_2_confront_label",
            menu_tooltip = "Tell her that you know about her job as a stripper and use it as further leverage.")
        cousin.get_role_reference(cousin_role).add_action(blackmail_2_confront_action)
        cousin.event_triggers_dict["seen_cousin_stripping"] = True
        return

    def add_cousin_at_house_phase_two_action(the_person):
        #Changes her schedule to be at your house
        found = next((x for x in the_person.on_room_enter_event_list if x.effect == "cousin_house_phase_two_label"), None)
        if not found:
            the_person.set_schedule(hall, the_days = [0, 1, 2, 3, 4], the_times = [2])
            cousin_at_house_phase_two_action = Action("Cousin visits house", cousin_house_phase_two_requirement, "cousin_house_phase_two_label")
            the_person.on_room_enter_event_list.append(cousin_at_house_phase_two_action) #When you see her next in your house this event triggers and she explains why she's there.
        return

    def add_cousin_at_house_phase_three_action():
        cousin_at_house_phase_three_action = Action("Cousin changes schedule", cousin_house_phase_three_requirement, "cousin_house_phase_three_label", args = cousin, requirement_args = day+renpy.random.randint(2,5))
        mc.business.mandatory_crises_list.append(cousin_at_house_phase_three_action) #In a couple of days change her schedule so she starts stealing from Lily.
        return

    def add_cousin_blackmail_intro_action(the_person):
        found = next((x for x in the_person.on_room_enter_event_list if x.effect == "cousin_blackmail_intro_label"), None)
        if not found:
            the_person.set_schedule(lily_bedroom, the_days = [0, 1, 2, 3, 4], the_times = [2])
            cousin_blackmail_intro_action = Action("Cousin caught stealing", cousin_blackmail_intro_requirement, "cousin_blackmail_intro_label")
            the_person.on_room_enter_event_list.append(cousin_blackmail_intro_action)
        return

    def add_cousin_stripping_and_setup_search_room_action(the_aunt, the_cousin):
        stripclub_strippers.append(the_cousin)
        the_cousin.set_schedule(strip_club, the_times = [3, 4])

        the_cousin.event_triggers_dict["stripping"] = True #Used to flag the blackmail event.
        cousin_room_search_action = Action("Search her room {image=gui/heart/Time_Advance.png}", cousin_room_search_requirement, "cousin_search_room_label",requirement_args = [the_cousin], args = [the_cousin, the_aunt])
        cousin_bedroom.add_action(cousin_room_search_action) #Lets you search her room for a clue about where to go to find her.
        return

    def add_cousin_boobjob_ask_action(the_person):
        cousin_boobjob_ask_action = Action("Cousin Boobjob Ask", cousin_boobjob_ask_requirement, "cousin_boobjob_ask_label", requirement_args = day + renpy.random.randint(3,6))
        the_person.on_talk_event_list.append(cousin_boobjob_ask_action)
        return

    def add_cousin_boobjob_brag_action(the_person):
        cousin_new_boobs_brag_action = Action("Cousin new boobs brag", cousin_new_boobs_brag_requirement, "cousin_new_boobs_brag_label")
        the_person.on_talk_event_list.append(cousin_new_boobs_brag_action) #Next time you talk to her she brags about her new boobs, offers to show them to you, and tells you that she'll pay you back eventually.
        return

    def add_cousin_talk_boobjob_again_action():
        cousin_talk_boobjob_again_action = Action("Talk about getting a boobjob\nCosts: $5000", cousin_talk_boobjob_again_requirement, "cousin_talk_boobjob_again_label")
        cousin.get_role_reference(cousin_role).add_action(cousin_talk_boobjob_again_action)
        return

    def remove_cousin_talk_boobjob_again_action():
        for role in cousin.special_role:
            role.remove_action("cousin_talk_boobjob_again_label")
        return

###COUSIN ACTION LABELS###
label cousin_intro_phase_one_label():
    #Your cousin bursts into your room at the end of the day frustrated with Lily and how little personal space she has.
    $ mc.change_location(bedroom)
    $ cousin.draw_person(emotion = "angry")
    "Without warning your bedroom door is opened and [cousin.possessive_title] walks in. She closes the door behind her and looks awkwardly at you."
    mc.name "Hey..."
    cousin "Hey. I'm just going to be here for a few minutes. You don't need to say anything."
    mc.name "Is everything okay?"
    cousin "Your sister just keeps talking. She won't shut up. I just need some silence."
    menu:
        "Offer to talk to [lily.title]":
            pass

        "Let [cousin.title] stay as long as she wants":
            pass

        "Tell [cousin.title] to leave you alone":
            pass

    mc.name "Right. How about..."
    "[cousin.possessive_title] glares at you."
    cousin "I want silence, [cousin.mc_title]. It means not talking."
    $ cousin.draw_person()
    "She sits down and leans back against your door, staring at her phone."
    menu:
        "Say nothing":
            "You decide to just stay quiet and go back to what you were doing. [cousin.title] reads on her phone for half an hour before standing back up."
            $ cousin.change_happiness(5)
            $ cousin.change_love(1)
            cousin "Thanks."
            "With that she opens your door and leaves."

        "Kick her out":
            mc.name "Listen [cousin.title], this is my room and I want some privacy. Get out."
            "[cousin.possessive_title] rolls her eyes and sighs dramatically."
            cousin "If you're just going to keep talking at me, gladly."
            $ cousin.change_love(-2)
            "She stands back up and leaves your room. She slams your door on the way out."

    $ clear_scene()
    return

label cousin_house_phase_one_label(the_person):
    $ add_cousin_at_house_phase_two_action(the_person)
    return

label cousin_house_phase_two_label(the_person):
    "When you come in the front door you see [the_person.title] sitting on your couch watching TV."
    $ the_person.draw_person(position = "sitting")
    mc.name "Uh... Hey."
    the_person "Hey."
    "She glances up from the TV for the briefest moment, then goes back to ignoring you."
    mc.name "What's up? Why are you over here?"
    the_person "Your mom said I could come over whenever I wanted. My mom won't stop bothering me and our crappy apartment is tiny."
    "[the_person.possessive_title] shrugs and turns her full attention back to her TV show."
    $ add_cousin_at_house_phase_three_action()
    return

label cousin_house_phase_three_label(the_person):
    $ add_cousin_blackmail_intro_action(the_person)
    return

label cousin_blackmail_intro_label(the_person):
    #You find your cousin in Lily's room, looking for cash. Event triggers as soon as you come in. Begins blackmailing storyline.
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] is standing in front of [lily.possessive_title]'s nightstand. She turns suddenly when you open the door."
    $ the_person.draw_person()
    the_person "Uh... Hey."
    mc.name "What are you doing in here?"
    "[the_person.title] crosses her arms and looks away from you."
    the_person "Nothing. I was just... looking around."
    mc.name "Uh huh. So I can tell [lily.fname] about this and you won't mind?"
    "She glares at you."
    the_person "Sure. It's not even a big deal."
    "You shrug and get your phone out. You pull up [lily.possessive_title]'s contact information."
    the_person "Wait! It's really not a big deal [the_person.mc_title]. You don't need to tell her."
    mc.name "What were you doing in here [the_person.title]?"
    "[the_person.possessive_title] groans before breaking."
    $ the_person.change_happiness(-10)
    the_person "Fine. I was... I was looking for some money. My dad cut me off and my mom doesn't have any."
    the_person "[lily.possessive_title] is so scatterbrained she would never notice anything was missing."
    "[the_person.title] takes a few panicked steps towards you."
    the_person "You can't tell my mom. She would never let me leave the house."
    menu:
        "Blackmail her":
            mc.name "Fine, I'll stay quiet. If you do something for me."
            $ the_person.change_happiness(5)
            $ the_person.change_obedience(5)
            $ the_person.change_love(-1)
            "[the_person.title] seems relieved. She nods."
            the_person "Fine. What do you want?"
            call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list
            $ add_cousin_blackmail_hint_action(the_person)


        "Promise to stay quiet":
            mc.name "I'll keep this between you and me."
            "[the_person.title] gives you a suspicious look."
            the_person "Just like that?"
            "You shrug."
            mc.name "You're right, [lily.fname] wouldn't notice anything missing and you need it more."
            $ the_person.change_happiness(8)
            $ the_person.change_love(2)
            the_person "Okay. I better not find out you told someone."
            mc.name "Your secret's safe with me."

    $ clear_scene()
    return

label cousin_blackmail_label(the_person):
    #The dialogue intro for the blackmail list when you talk to her again.
    #TODO: Have this refer to the different blackmail stuff once it's been written
    #TODO: Write a variant for when you promised to "keep quiet' then come back to blackmail her.
    mc.name "So, I was thinking about going to your mom and having a talk. About you."
    "[the_person.title] lets out a resigned sigh."
    the_person "Fine. What do you want?"
    call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_1

    return

label cousin_blackmail_list(the_person):
    menu:
        "Demand to know where she has been going at night" if the_person.event_triggers_dict.get("stripping", False) and the_person.event_triggers_dict.get("blackmail_level",-1) == 1:
            call cousin_blackmail_ask_label(the_person) from _call_cousin_blackmail_ask_label
            if not _return: #If she didn't tell you anything she tells you to pick something else.
                call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_4
            else:
                $ the_person.event_triggers_dict["last_blackmailed"] = day
                $ the_person.change_love(-1)

        "Cash":
            call cousin_blackmail_cash(the_person) from _call_cousin_blackmail_cash

        "Test this serum":
            call cousin_blackmail_test_this_serum(the_person) from _call_cousin_blackmail_test_this_serum

        "Strip for me":
            call cousin_blackmail_strip_for_me(the_person) from _call_cousin_blackmail_strip_for_me

        "Kiss me" if the_person.event_triggers_dict.get("blackmail_level", -1) >= 2:
            call cousin_blackmail_kiss_me(the_person) from _call_cousin_blackmail_kiss_me

        "Fuck me" if the_person.event_triggers_dict.get("blackmail_level", -1) >= 2:
            call cousin_blackmail_fuck_me(the_person) from _call_cousin_blackmail_fuck_me

        "Work for me" if the_person.event_triggers_dict.get("blackmail_level", -1) >= 2 and not the_person.has_role(employee_role) and mc.business.employee_count < mc.business.max_employee_count:
            call cousin_blackmail_work_for_me(the_person) from _call_cousin_blackmail_work_for_me

        "Nothing":
            mc.name "Nothing right now, but I'll come up with something."
            the_person "Ugh."

    return

label cousin_blackmail_cash(the_person):
    #Always succeeds. Get some extra cash from her.
    if the_person.event_triggers_dict.get("blackmail_level",-1) >= 2:
        mc.name "I assume your little stripping gig has still been paying well. I want my cut."
        the_person "Fine."
        if not the_person.tits_visible:
            "[the_person.title] reaches into her shirt and pulls out a roll of cash."
        else:
            "[the_person.title] pulls out a roll of cash."
            "She leafs out a bunch of $100 bills and hands them over to you. You take the money and slip it into your wallet."

    else:
        mc.name "If you're taking cash from my sister, I want half."
        $ the_person.change_obedience(1)
        if not the_person.tits_visible:
            "[the_person.title] reaches into her shirt and pulls out a small wad of bills."
        else:
            "[the_person.title] pulls out a small wad of bills."
        the_person "Fine."
        "She pulls out a $100 bill and hands it over to you. You take the money and slip it into your wallet."
    $ mc.business.change_funds(100)
    $ the_person.change_love(-1)
    $ the_person.change_obedience(3)
    $ the_person.event_triggers_dict["last_blackmailed"] = day
    return

label cousin_blackmail_test_this_serum(the_person):
    #Always succeeds. She takes a dose of serum for you.
    mc.name "I've got stuff from work that needs testing. If you test it, I'll stay quiet."
    the_person "Fine."
    "She rolls her eyes and waits for you to give her a vial of serum."
    call give_serum(the_person) from _call_give_serum_12
    if _return:
        "You hand over the vial. [the_person.possessive_title] drinks it down without any comment or complaint."
        the_person "There. Now just keep up your end of the bargain and keep quiet."
        $ the_person.event_triggers_dict["last_blackmailed"] = day
        $ the_person.change_love(-1)
        $ the_person.change_obedience(3)

    else:
        mc.name "Actually, I don't have anything with me right now."
        "[the_person.title] rolls her eyes."
        the_person "Whatever. What else do I need to do to keep you quiet?"
        call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_2
    return

label cousin_blackmail_strip_for_me(the_person):
    #Requires min sluttiness. She'll strip down her outfit until a certain point for you.
    mc.name "I want to see you strip for me."
    if the_person.effective_sluttiness() >= 15:
        "[the_person.possessive_title] doesn't say anything for a second."
        the_person "Fine. Sit down and pay attention. I'm not doing this for fun."
        if the_person.effective_sluttiness("underwear_nudity") <= 20:
            #She only wants to show you her underwear.
            "She starts to move, then pauses to glare at you."
            the_person "And I'm not taking off my underwear. Got it?"
            mc.name "Whatever, just make sure you put on a good show for me."
            if the_person.outfit.wearing_bra: #If she's wearing a bra strip down to it.
                while the_person.outfit.bra_covered:
                    $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item) #Strip down to her underwear.
                    "[the_person.possessive_title] takes off her [the_item.name]."
                $ the_item = None
            else: #She's not wearing a bra and doesn't want you to see her tits.
                "[the_person.title] seems nervous and plays with her shirt." #TODO: Check that she is wearing a shirt
                mc.name "What's wrong?"
                "She scoffs and looks away."
                the_person "Nothing. I just... don't have a bra on... I can't take this off."
                mc.name "Come on, you know the deal."
                the_person "Nope. Not doing it. Be happy with what you're getting."

            if the_person.outfit.wearing_panties:
                while the_person.outfit.panties_covered:
                    $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item)
                    "[the_person.possessive_title] takes off her [the_item.name]."
                $ the_item = None
            else: #TODO: make sure she's actually wearing a dress or skirt or something
                the_person "So, I'm not wearing any panties right now. That means I can't take this off."
                mc.name "Come on, that's not what the deal is."
                the_person "Sad you don't get to see my tight, wet pussy [the_person.mc_title]?"
                "She laughs and shakes her head."
                the_person "Deal with it. Go cry to mommy if it matters that much to you."

            if the_person.outfit.wearing_panties and the_person.outfit.wearing_bra:
                "Once [the_person.possessive_title] has stripped down to her underwear, she turns around to let you look at her ass."
            else:
                "Once [the_person.possessive_title] has stripped down as far as she's willing, she turns around to let you look at her ass."
            $ mc.change_locked_clarity(20)
            $ the_person.draw_person(position = "back_peek")
            $ the_person.update_outfit_taboos()
            the_person "Finished yet? I bet you're about to cream your fucking pants looking at this."
            #TODO: Add a strip-show-and-masturbate event that we can pass people into.
            "You take a second to enjoy the view."
            mc.name "Alright, that'll do."
            the_person "Finally..."
            "[the_person.possessive_title] gets dressed again."
            $ the_person.update_outfit_taboos()
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person()
            $ the_person.change_slut(2, 20)

        elif the_person.effective_sluttiness("bare_tits") <= 40:
            #She'll show you her tits.
            while not the_person.tits_visible:
                $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                $ the_person.draw_animated_removal(the_item) #Strip down to her underwear.
                if the_person.tits_visible:
                    if the_person.has_taboo("bare_tits"):
                        the_person "God, I can't believe you're going to see my tits. You're a fucking dick of a cousin, you know that?"
                        mc.name "Whatever. Pull those girls out so I can have a look."
                        the_person "I don't know why my Mom likes you... Fine."
                        $ the_person.break_taboo("bare_tits")

                    "[the_person.possessive_title] takes off her [the_item.display_name] slowly, teasing you as she frees her tits."
                else:
                    "[the_person.possessive_title] takes off her [the_item.display_name]."

            $ the_item = None

            if the_person.outfit.wearing_panties:
                while the_person.outfit.panties_covered:
                    $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                    $ the_person.draw_animated_removal(the_item)
                    "[the_person.possessive_title] takes off her [the_item.display_name]."
                $ the_item = None
            else: #TODO: make sure she's actually wearing a dress or skirt or something
                the_person "So, I'm not wearing any panties right now. That means I can't take this off."
                mc.name "Come on, that's not what the deal is."
                the_person "Sad you don't get to see my tight, wet pussy [the_person.mc_title]?"
                the_person "Deal with it. Go cry to mommy if it matters that much to you."

            $ mc.change_locked_clarity(20)
            "Once [the_person.possessive_title] has stripped down, she turns around to let you get a look at her ass."
            $ the_person.draw_person(position  = "back_peek")
            the_person "Look all you want... I bet you're creaming your pants thinking about touching me."
            $ mc.change_locked_clarity(10)
            "She wiggles her butt in your direction. Her tits swing back and forth with the same movement."
            the_person "Well keep dreaming. I'm not that fucking desperate."
            "Once you've gotten your fill, [the_person.title] gets dressed again."
            $ the_person.update_outfit_taboos()
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person()
            $ the_person.change_slut(2, 40)

        else:
            #She'll get completely naked.
            while not the_person.tits_visible:
                $ the_item = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                $ the_person.draw_animated_removal(the_item) #Strip down to her underwear.
                if the_person.tits_visible:
                    if the_person.has_taboo("bare_tits"):
                        the_person "God, I can't believe you're going to see my tits. You're a fucking dick of a cousin, you know that?"
                        mc.name "Whatever. Pull those girls out so I can have a look."
                        the_person "I don't know why my Mom likes you... Fine."
                        $ the_person.break_taboo("bare_tits")
                    "[the_person.possessive_title] takes off her [the_item.name] slowly, teasing you as she frees her tits."
                else:
                    "[the_person.possessive_title] takes off her [the_item.name]."

            while not the_person.vagina_visible:
                $ the_item = the_person.outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                $ test_outfit = the_person.outfit.get_copy() #Use a copy so we can check for the effects before actually removing and drawing it.
                $ test_outfit.remove_clothing(the_item)
                if test_outfit.vagina_visible:
                    if the_person.has_taboo("bare_pussy"):
                        "[the_person.title] pauses and takes a deep breath."
                        mc.name "What's the hold up?"
                        the_person "Nothing! I though you would have chickened out by now, but whatever."
                        $ the_person.break_taboo("bare_pussy")
                    $ the_person.draw_animated_removal(the_item)
                    "[the_person.possessive_title] peels off her [the_item.name], slowly revealing her cute little pussy."
                else:
                    $ the_person.draw_animated_removal(the_item)
                    "[the_person.possessive_title] takes off her [the_item.name]."

            $ the_item = None
            the_person "There, are you satisfied?"
            $ the_person.draw_person(position = "back_peek")
            $ mc.change_locked_clarity(20)
            "She spins on the spot, letting you get a look at her ass."
            mc.name "I'm not sure this is enough [the_person.title]. I think you need to convince me."
            "[the_person.possessive_title] sighs dramatically."
            $ the_person.draw_person()
            the_person "Please [the_person.mc_title], please don't tell my mom what a bad girl I've been."
            $ mc.change_locked_clarity(20)
            the_person "I'm here, with my big fucking tits and my tight fucking cunt out just for you. Please don't say anything."
            "She gives you an overly dramatic pout."
            mc.name "Fine, that'll do."
            the_person "Fucking finally..."
            $ the_person.update_outfit_taboos()
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person()
            $ the_person.change_slut(2, 60)

        $ the_person.event_triggers_dict["last_blackmailed"] = day
        $ the_person.change_love(-1)
        $ the_person.change_obedience(3)
        $ the_person.review_outfit()

    else:
        "[the_person.title] stares at you for a moment."
        the_person "Really? You want me to strip? For you?"
        the_person "You want me to get naked. To show you my nice... big... tits?"
        "She squeezes her breasts together and leans forward."
        the_person "Keep dreaming. Seriously, what do you want?"
        call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_3
    return

label cousin_blackmail_kiss_me(the_person):
    #Requires min sluttiness and more blackmail (Or high sluttiness). Either is a special kissing scene OR we add functionality to lock people into a sex position.
    mc.name "I want you to kiss me."
    "She sneers."
    the_person "Ugh. Disgusting."
    "She leans forward and gives you a brief kiss on the cheek."
    the_person "There, are we done now?"
    mc.name "You know we aren't. Come here."
    $ the_person.add_situational_obedience("blackmail", 30, "This will keep him quiet.")

    call fuck_person(the_person, start_position = kissing, start_object = make_floor(), position_locked = True) from _call_fuck_person_24
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.title] is left flush and panting when you're finished making out."
        mc.name "Did you enjoy yourself? You're pretty good at that."
        $ the_person.change_slut(2, 60)
        $ the_person.change_obedience(4)
        the_person "Shut up, I'm just glad that's over..."
    else:
        the_person "Finally. I'm glad that's over."
        $ the_person.change_obedience(3)

    $ the_person.clear_situational_obedience("blackmail")
    $ the_person.review_outfit()
    $ the_person.event_triggers_dict["last_blackmailed"] = day
    return

label cousin_blackmail_fuck_me(the_person):
    #Requires min sluttiness and more blackmail (Or high sluttiness). Generic fuck_person call with a large obedience boost so she'll do things you tell her to do.
    mc.name "I want your body. All of it."
    if the_person.effective_sluttiness("vaginal_sex") >= 20:
        the_person "Ugh, really?"
        "She sighs and rolls her eyes dramatically."
        the_person "Fine. Just make it quick, and I swear to god you better never tell anyone about this."
        $ the_person.add_situational_obedience("blackmail", 30, "This will keep him quiet.")

        call fuck_person(the_person) from _call_fuck_person_25
        $ the_report = _return
        $ the_person.draw_person()
        if the_report.get("girl orgasms", 0) > 0:
            "[the_person.possessive_title] closes her eyes and tries to catch her breath."
            the_person "Fuck... God fucking damn it..."
            mc.name "Something wrong?"
            the_person "God damn it, you shouldn't be able to do that to me. Fuck."

        else:
            the_person "Are we done here? I feel like I need a shower after that."
            mc.name "Cheer up, you'll be enjoying it soon enough."
            the_person "God I hope not. Even if I was, you'll never get the satisfaction of knowing about it."

        $ the_person.clear_situational_obedience("blackmail")
        $ the_person.review_outfit()
        $ the_person.event_triggers_dict["last_blackmailed"] = day

    else:
        the_person "Really? You want to touch me?"
        "She bites her lip and runs her hands over her hips."
        the_person "Grab my tits? Fuck my tight pussy? Make me cum with your huge cock?"
        the_person "Ha! Dream on you fucking perv. I'm a stripper not a whore."
        call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_5
    return

label cousin_blackmail_work_for_me(the_person):
    mc.name "I want you to come at my company."
    the_person "What? I already have a job, I don't need to work at your stupid fucking company."
    mc.name "You don't have a job, you have a hobby."
    the_person "I make more money each night than you could pay me in a week."
    mc.name "I wouldn't be so sure about that, but we can talk about your salary later."
    "She scoffs and rolls her eyes."
    the_person "Why would you want me to work for you anyways?"
    mc.name "Because I need people I can trust."
    the_person "You trust me? You're dumber than you look."
    the_person "... And you look like a fucking idiot, by the way."
    "You ignore her and continue."
    mc.name "I trust you because I have leverage on you."
    mc.name "If you fucked me over I'll tell your Mom what you've been doing for cash."
    the_person "And if I quit to work for you? What will you tell her then?"
    mc.name "The same thing. Do you think she's going to be proud because you {i}use{/i} to be a stripper?"
    mc.name "No, she'd rip you apart if she ever heard about this. I'm sure I could find plenty of evidence..."
    "[the_person.possessive_title] sighs and shakes her head, admitting defeat."
    the_person "Shut up, I'll do it. But I'm not going to be cheap, alright?"
    the_person "I'm not one of those cheap skanks you keep around."
    $ the_person.salary_modifier = 2.0
    $ stripper_replace(the_person) #Decrement the stripper target pool, and remove Gabriel, so that an extra replacement isn't generated
    call stranger_hire_result(the_person) from _call_stranger_hire_result_cousin_blackmail_list
    if _return:
        mc.name "Congratulations, you have a real job now."
        the_person "Pfh, whatever."
        menu:
            "Keep stripping on the weekend":
                mc.name "I feel bad though. Getting naked was about the only skill you were kind of good at."
                the_person "Ugh, what are you talking about now?"
                mc.name "You've got the weekends off, so if you wanted to keep working at the club..."
                the_person "I don't need your permission! I was going to keep working there anyways."
                $ the_person.set_schedule(strip_club, the_days = [5,6], the_times = [3,4])
                $ the_person.add_role(stripper_role) #Add the role back specifically for her so when she's in the club she can give dances
                $ stripper_hire(the_person) #Add her to stripclub list and increase Stripclub target strippers to account for her presence
                "You shrug, content that either way she'll have her tits on display during the weekend."

            "Demand she stop stripping":
                mc.name "Now that I'm your boss I don't want to see you at that filthy strip club again, alright?"
                the_person "You can't tell me what to do!"
                mc.name "As long as you want to keep your stint there secret you will."
                mc.name "If you really want to show your tits to men you can come to me."
                the_person "Ugh... Whatever."

    else:
        $ stripper_hire(the_person) #Readd her
        mc.name "Man, I thought you might have been useful for something, but this is just dreadful."
        the_person "Fuck you, you came to me!"
        mc.name "Yeah, that was a mistake. Never mind, stripping is probably the best you can do with your life."
        "She scowls angrily at you."
        call cousin_blackmail_list(the_person) from _call_cousin_blackmail_list_6
    return

label aunt_cousin_hint_label(the_aunt, the_cousin):
    # prevent event from triggering twice
    python:
        if any(x.effect == "cousin_search_room_label" for x in cousin.home.actions):
            renpy.return_statement()

    #Your aunt calls at night to ask if you know where Gabrielle is. Hints that she's up to something late at night.
    "You get a call on your phone. It's [the_aunt.possessive_title]."
    mc.name "Hey [the_aunt.title], is everything alright?"
    the_aunt "Hi [the_aunt.mc_title]. Do you have a moment?"
    mc.name "Sure, what's up?"
    the_aunt "It's about [the_cousin.name]. For the last few nights she's been staying out late and she won't tell me where she is."
    the_aunt "I'm worried that she's getting up to trouble. Do you have any clue what she's doing?"
    menu:
        "Offer to find out":
            mc.name "No, but I can try and find out if you'd like."
            $ the_aunt.change_happiness(3)
            $ the_aunt.change_love(1)
            the_aunt "That would be great, thank you. I'm sure I'm just overreacting, but it would help me sleep better at night knowing she's okay."
            mc.name "I'll let you know if I learn anything."

        "No clue":
            mc.name "Nope, no idea. Sorry."
            the_aunt "That's okay, she's always been very private, so I'm not surprised."
            the_aunt "Well, if you hear anything, just let me know, okay? I'm sure I'm overreacting, but it would help me sleep if I knew she was okay."
            mc.name "Okay [the_aunt.title], if I hear anything I'll let you know."

    the_aunt.title "Thank you. I won't keep you any longer then, I'm sure you're busy!"

    $ add_cousin_stripping_and_setup_search_room_action(the_aunt, the_cousin)
    return

label cousin_blackmail_ask_label(the_person):
    #This is an option made available when blackmailing her
    #With a high enough love or obedience she tells you what she's been doing, otherwise she just tells you to fuck off.
    $ talked_before = the_person.event_triggers_dict.get("blackmail_2_asked", False)
    $ the_person.event_triggers_dict["blackmail_2_asked"] = True # For future events we have slightly different dialogue.

    $ told = False
    if not talked_before:
        mc.name "Your mom told me you've been staying out late, but you won't tell her why. I'm want to know what you're up to."
    else:
        mc.name "So [the_person.title], are you ready to tell me what you've been staying out late for?"

    if the_person.love >= 60:
        if not talked_before:
            the_person "You heard about that? Ugh, of course she's been asking everyone."
        else:
            the_person "Are you still thinking about that? Ugh..."
        mc.name "You know you can trust me. What have you been doing?"
        "She hesitates, torn between her love for you and her desire for privacy. She finally breaks down."
        the_person "I have a new job."
        the_person "..."
        $ mc.change_locked_clarity(5)
        the_person "At a strip club."
        mc.name "What?"
        the_person "I got a job at a strip club. I didn't tell my mom because she would flip out."
        the_person "I didn't tell you because you're my cousin, and I didn't want you to think I was a freak."
        the_person "Can you please just not tell her? I make a lot of money. I'll give you a cut to stay quiet."
        mc.name "I would really hate to let your mom down though..."
        "She sighs and nods her head."
        $ mc.change_locked_clarity(5)
        the_person "Yeah, yeah, I know what else you want. I'll let you touch me sometimes, if you promise to keep your mouth shut."
        mc.name "I think that might be enough."
        $ the_person.event_triggers_dict["blackmail_level"] = 2
        call begin_boobjob_story(the_person) from _call_begin_boobjob_story
        $ told = True

    elif the_person.obedience >= 130:
        "She rolls her eyes."
        if not talked_before:
            the_person "Ugh, of course she's been asking everyone. I'm not telling her for a reason."
        else:
            the_person "Ugh, are you still thinking about that. I haven't told my mom for a reason, you know."
        mc.name "Well, I want to know. What have you been doing?"
        "She hesitates, fighting against her own obedience to you, then breaks down."
        the_person "I have a new job."
        the_person "..."
        $ mc.change_locked_clarity(5)
        the_person "At a strip club."
        mc.name "What?"
        the_person "I got a job at a strip club, and I don't want my mom to know, okay?"
        the_person "She would freak out, and I make a lot of money doing it. Just don't tell her."
        mc.name "Why not? What do I get out of it?"
        "She sighs dramatically."
        the_person "Yeah, yeah. I see where this is going. I'll give you a cut."
        mc.name "And?"
        $ mc.change_locked_clarity(5)
        the_person "And... I'll let you touch me sometimes, if you promise to stay quiet."
        mc.name "I think that might be enough."
        $ the_person.event_triggers_dict["blackmail_level"] = 2
        call begin_boobjob_story(the_person) from _call_begin_boobjob_story_1
        $ told = True

    else:
        "She rolls her eyes."
        if not talked_before:
            the_person "And you think I'd tell you instead? Dream on."
            mc.name "But you {i}are{/i} doing something?"
            the_person "Wouldn't you like to know. Come one, what do you really want?"
        else:
            the_person "Why would I tell you anything? If you're so curious, you should figure it out yourself."
            the_person "Come on, tell me what you really want so I can get this over with."

        "[the_person.possessive_title] doesn't seem like she's about to crack."
        "Maybe if she liked you more or was more obedient she would tell you, or maybe there's another way to figure out what she's been doing."

    return told

label cousin_search_room_label(the_cousin, the_aunt):
    # You start to search her room to find anything you can. If her mom is home she'll ask you to stop, but with enough obedience you can tell her to let you do it.
    "You start to search through [the_cousin.title]'s room for any hints you can find about where she's been going at night."
    if the_aunt in aunt_apartment.people or the_aunt in aunt_bedroom.people:
        #Your aunt is around and asks you to stop.
        "You start with the most obvious places, digging through the papers on her desk and checking her closet."
        "While you're searching, the bedroom door opens."
        $ the_aunt.draw_person()
        if the_aunt.love < 30:
            the_aunt "[the_aunt.mc_title], what the hell are you doing?"
            mc.name "Uh... I'm looking for information about your daughter."
            $ the_aunt.draw_person(emotion = "angry")
            $ the_aunt.change_love(-3)
            the_aunt "And you think you can just come in here and dig through her stuff? Get out! I'll be telling your mother about this!"
            "She glares at you and ushers you out of the apartment and out of the building."
            $ the_aunt.change_happiness(-5)
            $ the_aunt.change_love(-1)
            $ mc.change_location(downtown)
            "You'll need [the_aunt.possessive_title] to like you more if you want to search [the_cousin.title]'s room undisturbed."
            return
        else:
            the_aunt "[the_aunt.mc_title], are you looking for something?"
            mc.name "I'm looking for clues about what your daughter has been up to."
            the_aunt "Oh. I'm not sure she would appreciate you searching through all of her things though."
            mc.name "I doubt she would, but we both want information, right?"
            if the_aunt.obedience < 130:
                the_aunt "I do, but not like this. You're going to have to stop."
                $ the_aunt.change_love(-1)
                "You're forced to abandon your search. [the_aunt.possessive_title] escorts you to the living room."
                $ mc.change_location(aunt_apartment)
                "If she was more obedient she might let you continue the search, or you could wait until she isn't in the apartment."
                return

            else:
                "She sighs and nods."
                the_aunt "You're right. If [the_cousin.title] asks, I don't know anything about this, okay?"
                mc.name "I won't tell a soul."
                $ clear_scene()
                "[the_aunt.possessive_title] leaves you alone in her daughter's room to continue your search."



    else:
        "With nobody else around you're able to thoroughly search the room. You start with the most obvious places, digging through her desk and checking her closet."

    "Your initial sweep doesn't turn up anything interesting, so you start looking in more hidden places."
    "Under her mattress you discover a piece of paper hidden as deep as possible. You pull it out and read it."
    $ strip_club.visible = True
    "It's a pay stub from [strip_club.formal_name], covering the last two weeks for an impressive amount of pay."
    "It's possible that [the_cousin.title] is working there as a waitress, but you have your doubts."
    "If you can catch [the_cousin.title] while she's working there she won't be able to make any excuses and you'll have her in the palm of your hand."

    $ the_cousin.event_triggers_dict["found_stripping_clue"] = True
    call advance_time() from _call_advance_time_25
    return

label cousin_blackmail_level_2_confront_label(the_person, in_club = False):
    # A talk action added once you have seen her stripping that results in higher blackmailing levels.
    mc.name "So I was at [strip_club.formal_name] and I saw something really interesting."
    "Her eyes go wide and lock with yours."
    the_person "Uh... What were you doing there? That's a weird place for you to be."
    mc.name "I was enjoying the talent. Imagine my surprise when I see you walk out."
    $ the_person.change_happiness(-5)
    the_person "... Fuck."
    mc.name "So this was what you were hiding, huh? I'm sure your mom is going to be thrilled when she hears about this."
    the_person "I swear to god I'll kill you if you do. You can't say a word about this to her."
    mc.name "Why not? What do I get out of it?"
    "She holds her forehead for a moment and sighs."
    $ the_person.change_love(-5)
    the_person "Yeah, yeah. I see where this is going. Listen, I make really good money doing this."
    the_person "I'll give you a cut if you stay quiet."
    mc.name "And?"
    the_person "And? What \"and\"? could you want?"
    mc.name "That whole strip show is just a massive tease. I'm feeling a little unsatisfied."
    $ mc.change_locked_clarity(5)
    the_person "God, you fucking perv. Fine, if you can keep quiet I might also let you... touch me. Deal?"
    mc.name "I think that might be enough."
    $ the_person.set_schedule(None, the_times = [3, 4]) # clear old scheduled stripping
    $ stripper_hire(the_person)
    $ the_person.change_job(stripper_job) #She's a stripper now, officially.
    $ the_person.event_triggers_dict["blackmail_level"] = 2
    call begin_boobjob_story(the_person) from _call_begin_boobjob_story_2
    return


label begin_boobjob_story(the_person):
    #Creates and adds the boobjob quest. Broken out here to make it easier to run in multiple places once you know about her job.
    $ add_cousin_boobjob_ask_action(the_person)
    return

label cousin_boobjob_ask_label(the_person):
    # TODO: Also add a specific event for Lily after you discover her new "career", maybe if she has a minimum sluttiness we can suggest it to her in that event.
    #Add event to on_talk_event_list at some point, probably using a random event timed after you find out what her new job is.
    $ the_person.draw_person()
    if the_person.love < 10: #Check to make sure she still hates your guts, otherwise you get a toned down version of the dialogue since you've made friends with her.
        the_person "Hey, I'm glad you're here."
        $ the_person.draw_person(emotion = "happy")
        "She gives you a wide, fake smile."
        mc.name "That's not a good sign. What do you want?"
        the_person "Want? Why would I want anything?"
        the_person "Maybe I just want to spend time with my pervy blackmailing cousin. Is that so weird?"
        mc.name "Come on, spit it out."
        $ the_person.draw_person()

    else:
        the_person "Hey, I'm glad you're here, I wanted to ask you about something."

    $ mc.change_locked_clarity(5)
    the_person "I need money for a boob job."
    mc.name "Why do you need a boob job, and why should I be paying for it?"
    the_person "Come on, you know where I work. Girls with bigger tits get tipped more."
    if the_person.has_large_tits and the_person.love < 10: #Just in case you shrink them with serum so this doesn't make sense any more:
        "You gesture to her already sizeable tits."
        mc.name "Those udders aren't enough? Maybe it's more of a personality thing."
        the_person "Oh, thank you for the input. I'll let all my customers know my cousin thinks my tits are already big enough."
        mc.name "Whatever, fine. That doesn't explain why I should be paying for it though."
    else:
        mc.name "That doesn't explain why I should be paying for it though."
    the_person "Because I don't have all the money I need right now, and if I get this done, I can earn it back quicker."
    the_person "If you spot me the cash now, I can pay you back as soon as I earn it."
    mc.name "How much would you need?"
    the_person "I've got some money, but I'd need another five grand from you."
    the_person "Please [the_person.mc_title], it's a rock solid investment."
    $ has_boob_enhancement_serum = len(mc.inventory.get_serums_with_trait(breast_enhancement)) != 0
    menu:
        "Pay for it\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}" if mc.business.has_funds(5000):
            mc.name "Fine. Send me over the bill and I'll pay it."
            the_person "Really? Just like that?"
            if the_person.love < 10:
                mc.name "Just like that. Your tits are the only interesting thing about you, so you might as well have the best money can buy."
                the_person "Ugh. You're the worst."

            else:
                mc.name "Just like that. I think you'll look good with bigger tits."
                the_person "Thanks, I guess."

            $ the_person.change_obedience(5)
            $ the_person.change_slut(2, 60)
            $ mc.business.change_funds(-5000)

        "Pay for it\n{color=#ff0000}{size=18}Requires: $5000{/size}{/color} (disabled)" if not mc.business.has_funds(5000):
            pass

        "Offer breast enhancing serum instead" if has_boob_enhancement_serum:
            mc.name "Why go through all that trouble when I have a serum that could do this for you right now."
            the_person "Wait, you do?"
            mc.name "Of course I do. It's what my business does. I have a dose right here, if you'd like to try it out."
            the_person "And this stuff really works? I always thought you were running a scam."
            mc.name "Yes, it really works. Do you want it or not?"
            "She eyes you cautiously, then nods."
            the_person "Fine, give it here."
            call give_serum(the_person) from _call_give_serum_15
            if _return == False:
                mc.name "Actually, I don't think this particular serum would be good for you."
                $ the_person.change_love(-1)
                the_person "I knew you were running a scam. If you didn't want to pay, you could have just said so instead of lying."
                call talk_person(the_person) from _call_talk_person_2

                $ add_cousin_talk_boobjob_again_action()
                return

            else:
                "She drinks the serum down, hands the vial back to you, and then looks down at her chest."
                the_person "So... Should they be doing something?"
                mc.name "I'm a chemical engineer, not a wizard. It will take some time for the effects to be apparent, and the effectiveness varies from person to person."
                the_person "Right, of course. I guess I'll let you know if it actually works then. I'm going to be pissed if this is all a scam though."
                call talk_person(the_person) from _call_talk_person_3

                $ add_cousin_serum_boobjob_check_action(the_person)
                return

        "Offer breast enhancing serum instead\n{color=#ff0000}{size=18}Requires: Serum with Breast Enhancement trait{/size}{/color} (disabled)" if not has_boob_enhancement_serum and mc.business.research_tier >= 2:
            pass #Shows as a disabled when you could get the research, until then does not show up at all (unless you somehow have something with the trait, from a random event for example)

        "Refuse to pay":
            mc.name "Five thousand dollars? That's ridiculous. I can't pay that just to get you a set of bigger tits."
            the_person "Come on, please? What can I do to convince you?"
            if not mc.business.has_funds(5000):
                mc.name "Nothing, because I don't have that kind of money."
                $ the_person.change_happiness(-5)
                the_person "Really? Ugh, you're useless."
                call talk_person(the_person) from _call_talk_person_4
                #Note: we add the boobjob talk option after so that the player has to come back and talk to her again.
                $ add_cousin_talk_boobjob_again_action()
                return
            else:
                mc.name "What can you do? I've got the money, I just don't see a reason to give it to you."
                the_person "You don't see a reason to get me some big, juicy tits?"
                "She leans close to you, standing on the tips of her toes to whisper sensually into your ear."
                $ mc.change_locked_clarity(10)
                the_person "Maybe I can show you why... Would that be enough? If your slutty, stripper cousin helped get you off, would that be enough to convince you?"
                menu:
                    "Pay for it and fuck her\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}":
                        $ play_spank_sound()
                        "You wrap a hand around her waist and slap her ass."
                        mc.name "Alright then, you've got yourself a deal."
                        $ the_person.add_situational_obedience("event", 20, "My new tits will make this all worth it!")
                        call fuck_person(the_person) from _call_fuck_person_42
                        $ the_person.clear_situational_obedience("event")
                        $ the_person.change_slut(2, 80)
                        $ mc.business.change_funds(-5000)

                    "Refuse to pay":
                        mc.name "I don't need to pay you if I want to use you. Sorry, but you'll have to find a way to buy your own tits."
                        "She backs up and sulks."
                        the_person "Ugh. Fine. Whatever."
                        call talk_person(the_person) from _call_talk_person_5
                        $ add_cousin_talk_boobjob_again_action()
                        return


    $ add_cousin_boobjob_get_action(the_person)

    call talk_person(the_person) from _call_talk_person_7
    return

label cousin_talk_boobjob_again_label(the_person):
    mc.name "Do you still want to get a boob job?"
    if the_person.has_large_tits:
        the_person "Yeah. Why, have you come around? Do you want to get your cousin some big..."
        "She leans forward, accentuating her already sizeable breasts."
        the_person "Juicy tits? You know if you come down to the club, you'd be able to see them, right?"
    else:
        the_person "Yeah, obviously."

    $ has_boob_enhancement_serum = len(mc.inventory.get_serums_with_trait(breast_enhancement)) != 0

    menu:
        "Pay for it\n{color=#ff0000}{size=18}Costs: $5000{/size}{/color}" if mc.business.has_funds(5000):
            mc.name "Fine. Send me the bill and I'll pay it."
            the_person "Really? Just like that?"
            if the_person.love < 10:
                mc.name "Just like that. Your tits are the only interesting thing about you, so you might as well have the best money can buy."
                the_person "Ugh. You're the worst."

            else:
                mc.name "Just like that. I think you'll look good with bigger tits."
                the_person "Thanks, I guess."

            python:
                the_person.change_obedience(5)
                the_person.change_slut(2, 50)
                mc.business.change_funds(-5000)
                add_cousin_boobjob_get_action(the_person)
                remove_cousin_talk_boobjob_again_action()

        "Pay for it\n{color=#ff0000}{size=18}Requires: $5000{/size}{/color} (disabled)" if not mc.business.has_funds(5000):
            pass

        "Offer breast enhancing serum instead" if has_boob_enhancement_serum:
            mc.name "Why go through all that trouble when I have a serum that could do this for you right now."
            the_person "Wait, you do?"
            mc.name "Of course I do. It's what my business does. I have a dose right here, if you'd like to try it out."
            the_person "And this stuff really works? I always thought you were running a scam."
            mc.name "Yes, it really works. Do you want it or not?"
            "She eyes you cautiously, then nods."
            the_person "Fine, give it here."
            call give_serum(the_person) from _call_give_serum_16
            if _return == False:
                mc.name "Actually, I don't think this particular serum would be good for you."
                the_person "I knew you were running a scam. If you didn't want to pay you could have just said so instead of lying."
                $ the_person.change_love(-1)
                return

            else:
                "She drinks the serum down, hands the vial back to you, and then looks down at her chest."
                the_person "So... Should they be doing something?"
                mc.name "I'm a chemical engineer, not a wizard. It will take some time for the effects to be apparent, and the effectiveness varies from person to person."
                the_person "Right, of course. I guess I'll let you know if it actually works then. I'm going to be pissed if this is all a scam though."

                $ add_cousin_serum_boobjob_check_action(the_person)
                $ remove_cousin_talk_boobjob_again_action()
                return

        "Offer breast enhancing serum instead\n{color=#ff0000}{size=18}Requires: Serum with Breast Enhancement trait{/size}{/color} (disabled)" if not has_boob_enhancement_serum and mc.business.research_tier >= 2:
            pass

        "Refuse to pay":
            mc.name "Well, you can keep on wanting them, because I'm still not paying."
            the_person "Wait, did you seriously bring that up just to say no again."
            $ the_person.change_love(-3)
            the_person "Your pettiness never ceases to amaze me."

    return

label cousin_boobjob_get_label(the_person):
    call got_boobjob(the_person) from _call_got_boobjob
    # Now set the cousin specific stuff so she'll talk about it with you after
    $ add_cousin_boobjob_brag_action(the_person)
    return

label cousin_new_boobs_brag_label(the_person):
    #She brags about her new boobs and offers to let you see/touch them if she's slutty enough.
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Do you notice anything different?"
    $ mc.change_locked_clarity(10)
    if the_person.love < 10:
        "[the_person.possessive_title] seems unusually happy to see you. She puts her arms behind her back and sways her shoulders."
    else:
        "She puts her arms behind her back and sways her shoulders, emphasizing her chest."

    the_person "I got my new tits! Come on, what do you think?"
    menu:
        "They look good":
            mc.name "They look good. They better after what I paid!"
            $ the_person.change_love(1)
            $ the_person.change_obedience(3)

        "You look like a bimbo":
            mc.name "They make you look like a bimbo. Big tits, no brain."
            if the_person.personality is bimbo_personality:
                the_person "Thank you! I really like them, too!"
            else:
                the_person "Whatever. Who even asked you anyway?"
                mc.name "You did."
                the_person "Shut up."
            $ the_person.change_slut(1, 60)
            $ the_person.change_love(-2)

    mc.name "So, when can I expect to be paid back for your new sweater puppies?"
    the_person "As soon as I actually have a chance to make some money with them, okay?"
    the_person "You don't have to worry. I'm going to have to pay or you'll tell my Mom everything, right?"
    mc.name "You've got the idea."

    if the_person.tits_visible: #They're already out, she can't exactly charge you to see them.
        $ mc.change_locked_clarity(10)
        "She looks down at her chest and shakes her tits a little, obviously for her own enjoyment and not yours."
        "After a moment watching them jiggle she looks at you."
        the_person "Did you need anything else?"

    else:
        $ mc.change_locked_clarity(5)
        if mc.location.person_count > 1: #More than just her here.
            the_person "So... Do you want to see them? We can go find somewhere quiet."
        else:
            the_person "So... Do you want to see them?"
        menu:
            "Show them to me":
                mc.name "Alright, I want to see my investment."
                $ the_person.change_slut(1, 60)
                if mc.location.person_count > 1:
                    "You and [the_person.possessive_title] find a quiet spot away from anyone else, and she strips down in front of you."
                else:
                    "[the_person.possessive_title] starts to strip down in front of you."

                if the_person.outfit.can_half_off_to_tits():
                    $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
                else:
                    $ generalised_strip_description(the_person, the_person.outfit.get_tit_strip_list())

                $ mc.change_locked_clarity(10)
                if the_person.has_taboo("bare_tits"):
                    mc.name "I can't believe I had to pay for you to get bigger tits before I even got to see them."
                    $ the_person.break_taboo("bare_tits")
                    the_person "You should have come to the club, you could have seen them there."

                if the_person.effective_sluttiness("touching_body") > 50:
                    the_person "There you go. Go on, give them a feel. They feel almost exactly like the real thing."
                    $ mc.change_locked_clarity(10)
                    "You hold [the_person.title]'s new, larger breasts in your hands. They feel a little firmer than natural tits, but they're pleasant nonetheless."
                    "After you've had a chance to fondle them, she reaches for her top."
                    $ the_person.break_taboo("touching_body")
                else:
                    the_person "There you go. Good, right? These girls are going to bring in so much more at the club."
                    $ mc.change_locked_clarity(10)
                    "She looks down at her own chest and gives it a shake, setting her tits jiggling. When they settle down, she reaches for her top again."

                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()

            "Not right now":
                $ the_person.change_obedience(1)
                mc.name "I'm sure I'll get a chance to see them some other time. Maybe I'll stop by the club and watch you put them to work."
                the_person "Oh god, could you please not? I hate knowing you might be out in the crowd watching..."

    $ add_cousin_tits_payback_action(the_person, 5000)
    call talk_person(the_person) from _call_talk_person_8
    return

label cousin_tits_payback_label(the_person, amount_remaining):
    "You receive a notification on your phone from your bank."
    $ mc.business.change_funds(1000)
    if amount_remaining > 1000:
        "[the_person.title] has transferred you $1000 with a note saying \"You know why\"."
        $ add_cousin_tits_payback_action(the_person, amount_remaining - 1000)
    else:
        "[the_person.title] has transferred the last of the $5000 you loaned her for her surgery. You get a text shortly afterwards."
        the_person "There, I'm finally done with your tits payment plan."
        mc.name "For now. Maybe you'll want them even bigger someday."
        the_person "You wish, perv."
    return

label cousin_serum_boobjob_label(the_person, starting_tits):
    if the_person.rank_tits(the_person.tits) == the_person.rank_tits(starting_tits) and the_person.rank_tits(the_person.tits) < 8:
        #No change.
        "You get a text from [the_person.title]."
        $ the_person.change_love(-1)
        $ the_person.change_obedience(-3)
        the_person "Hey [the_person.mc_title], your serum thing didn't do anything for me."
        the_person "I'm going to need some cash so I can go to an actual doctor to do this for me. Come talk to me."

    elif the_person.rank_tits(the_person.tits) < the_person.rank_tits(starting_tits):
        "You get an angry text from [the_person.title]."
        $ the_person.change_happiness(-10)
        $ the_person.change_love(-5)
        $ the_person.change_obedience(-5)
        the_person "What the fuck, your serum thing made my tits smaller, not bigger!"
        the_person "I'm going to need to see an actual doctor now, these things aren't going to make me any money!"
        the_person "Come talk to me, I need cash for my boob job."
        #You actually made her tits smaller

    elif the_person.rank_tits(the_person.tits) - the_person.rank_tits(starting_tits) == 1 and the_person.rank_tits(the_person.tits) < 8:
        # One level bigger which she's kind of happy with but wanted more.
        "You get a text from [the_person.title]."
        $ the_person.change_obedience(2)
        the_person "Hey, I think your serum thing stopped working. My boobs seem a little bigger, but I was hoping for more."
        the_person "I still want to get my tits done properly. Come see me when I'm not doing anything important."

    else:
        # At least two levels, which is what she was aiming for.
        "You get a text from [the_person.title]."
        $ the_person.change_obedience(3)
        $ the_person.change_love(1)
        the_person "I can't believe it, but your freaky serum stuff actually worked! My tits are way bigger now!"
        "There's a pause, then she sends you a picture."
        $ the_person.outfit.strip_to_tits()

        $ the_person.draw_person(emotion = "happy")
        $ the_person.break_taboo("bare_tits")
        "It's a selfie of her in the bathroom, tits on display for you."
        the_person "You've saved me a ton of cash, so I thought you might enjoy that."
        $ the_person.apply_planned_outfit()
        $ clear_scene()
        return #NOTE: we're returning without adding the boobjob ask again event, which means we can consider this "done" at this point.

    $ add_cousin_talk_boobjob_again_action()
    return
