# Role based around obedience that can be appended to people in the Dungeon.
init 2 python:

    Person.stay_wet = False
    Person.slave_collar = False

init 10 python:

    def stay_wet_requirement(the_person):
        return not the_person.stay_wet

    def calm_down_requirement(the_person):
        return the_person.stay_wet

    def collar_slave_requirement(the_person):
        return not the_person.slave_collar

    def slave_trim_pubes_requirement(the_person):
        if the_person.has_role(girlfriend_role) or the_person.has_role(affair_role):
            return False
        return True

    def slave_shave_head_requirement(the_person):
        if the_person.has_role(affair_role):
            return False    # she still has a SO who would notice
        if not the_person.location == dungeon:
            return False    # only allow in dungeon
        return not the_person.is_bald

    def uncollar_slave_requirement(the_person):
        return the_person.slave_collar

    def wakeup_duty_requirement(the_person):
        if wakeup_duty_action.enabled and wakeup_duty_crisis not in mc.business.mandatory_morning_crises_list:
            return True
        elif wakeup_duty_action.enabled is False:
            return False
        elif day%7 == 5:    # not on saturday mornings
            return False
        else:
            return  "Alarm duty already set."

    def wakeup_duty_crisis_requirement():
        if day%7 == 5:    # not on saturday mornings
            return False
        return True

    def slave_assign_new_collar(person, collar):
        person.outfit.remove_all_collars()

        if collar == "Simple Collar":
            new_collar = breed_collar.get_copy()
            new_collar.colour = [.1,.1,.1,.8]
            new_collar.colour_pattern = [.1,.1,.1,.8]
        else:
            new_collar = collar.get_copy()
            new_collar.colour = [.1,.1,.1,.8]

            if new_collar.supported_patterns.has_key("Two Tone"):
                new_collar.pattern = new_collar.supported_patterns["Two Tone"]
                new_collar.colour_pattern = [.95,.95,.95,.9]

        person.base_outfit.add_accessory(new_collar)

        person.slave_collar = True
        person.apply_planned_outfit()
        person.draw_person()
        return

    def slave_remove_collar(person):
        person.slave_collar = False
        person.outfit.remove_all_collars()
        person.base_outfit.remove_all_collars()
        person.draw_person()
        return

    def slave_release_slave(person):
        slave_remove_collar(person)
        person.remove_role(slave_role)
        person.stay_wet = False
        # she is not happy and will reset her obedience to 100
        person.change_stats(love = -20, happiness = -20, obedience = 100 - person.obedience)
        # she loses her submissive trait
        person.update_opinion_with_score("being submissive", 0)
        return

    def slave_add_wakeup_duty_action(person):
        mc.business.remove_mandatory_crisis("slave_alarm_clock_label")
        wakeup_duty_crisis.args = [person]
        mc.business.add_mandatory_morning_crisis(wakeup_duty_crisis)
        return

    def slave_role_on_turn(person):
        if person.stay_wet and person.arousal_perc < 50:
            person.arousal = person.max_arousal * .5
        if person.slave_collar and person.obedience < 150:
            person.obedience = 150

    stay_wet_action = ActionMod("Stay wet", stay_wet_requirement, "stay_wet_label", menu_tooltip = "Order your slave to stay aroused at all times.", category = "Slave Role")
    calm_down_action = ActionMod("Calm down", calm_down_requirement, "calm_down_label", menu_tooltip = "Let your slave calm down.", category = "Slave Role", allow_disable = False)
    slave_trim_pubes_action = ActionMod("Trim pubes", slave_trim_pubes_requirement, "slave_trim_pubes_label", menu_tooltip = "Order her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.", category = "Slave Role")
    slave_shave_head_action = ActionMod("Shave her head", slave_shave_head_requirement, "slave_shave_head_label", menu_tooltip = "Make her submission complete by shaving her head.", category = "Slave Role")

    collar_slave_action = ActionMod("Place collar on [the_person.title]", collar_slave_requirement, "slave_collar_person_label", menu_tooltip = "Put a collar of ownership on the target, ensure that their obedience stays high.", category = "Slave Role")
    uncollar_slave_action = ActionMod("Remove collar from [the_person.title]", uncollar_slave_requirement, "slave_collar_person_label", menu_tooltip = "Remove the collar, declaring them a free spirit.", category = "Dungeon Actions", allow_disable = False)

    wakeup_duty_action = ActionMod("Wake me up in the morning", wakeup_duty_requirement, "wakeup_duty_label", menu_tooltip = "Have your slave wake you up in the morning", category = "Slave Role")
    wakeup_duty_crisis = Action("Slave Alarm Clock", wakeup_duty_crisis_requirement, "slave_alarm_clock_label")

    slave_role = Role("Slave", [stay_wet_action, calm_down_action, collar_slave_action, uncollar_slave_action, slave_trim_pubes_action, slave_shave_head_action, wakeup_duty_action], \
        on_turn = slave_role_on_turn, hidden = False)

label stay_wet_label(the_person): # Can expand with dialogue options and degrees of arousal, but just setting up basic actions for now.
    "You order [the_person.possessive_title] to keep herself wet and ready at all times for you."
    if the_person.arousal_perc < 50:
        $ the_person.arousal = person.max_arousal * .5
    $ the_person.stay_wet = True
    return

label calm_down_label(the_person):
    "You tell [the_person.possessive_title] to calm their tits."
    $ the_person.stay_wet = False
    $ the_person.reset_arousal()
    return

label slave_collar_person_label(the_person):
    if the_person.slave_collar:
        $ slave_remove_collar(the_person)
        "You remove the collar from [the_person.possessive_title]'s neck"
    else:
        call screen main_choice_display(build_menu_items([["Select Collar"] + [["Simple Collar", "Simple Collar"], ["Breed Me", breed_collar], ["Cum Slut", cum_slut_collar], ["Fuck Doll", fuck_doll_collar], ["Spiked Choker", spiked_choker], ["Back", "Back"]]]))
        $ collar_choice = _return
        if collar_choice == "Back":
            return

        $ slave_assign_new_collar(the_person, collar_choice)
        $ del collar_choice
        "You put one of the collars you bought around [the_person.possessive_title]'s neck."

    return

label slave_trim_pubes_label(the_person):
    mc.name "You're going to trim your pubes for me."
    "[the_person.possessive_title] nods obediently."
    the_person "Yes, Master. How do you prefer them?"
    if the_person.event_triggers_dict.get("trimming_pubes", None) is not None:
        # She was already planning on a different style, so we can have some change your mind dialogue here
        $ mc.business.mandatory_crises_list.remove(the_person.event_triggers_dict.get("trimming_pubes",None)) #If she already had an event for this make sure to remove it.
        $ the_person.event_triggers_dict["trimming_pubes"] = None

    $ pubes_choice = renpy.display_menu(girlfriend_build_pubes_choice_menu(the_person),True,"Choice")

    if pubes_choice == "Never mind":
        mc.name "On second thought, just leave them the way they are."
        the_person "As you wish."
    else:
        "You show her a picture of the style you want on your phone..."
        if pubes_choice.ordering_variable > the_person.pubes_style.ordering_variable:
            the_person "Yes Sir, I'll need to grow out a bit, but as soon as I can I'll trim them the way you prefer [the_person.mc_title]."
            #It will take some time for them to grow out.
            $ add_girlfriend_do_trim_pubes_action(the_person, pubes_choice, renpy.random.randint(2,5))
        else:
            the_person "Yes Sir, it will be ready for your inspection tomorrow, [the_person.mc_title]."
            $ add_girlfriend_do_trim_pubes_action(the_person, pubes_choice, 0)
    $ del pubes_choice
    return

label slave_shave_head_label(the_person):
    mc.name "Would you like to please me, slave?"
    the_person "Yes, Master."
    mc.name "Don't you want to know how?"
    the_person "Anything I can do for you, Maser."
    mc.name "Good...I have decided that you hairstyle is not to my liking."
    the_person "How would you like me to style it, Master."
    mc.name "You don't need to do anything, I will style it for you."
    the_person "Master?"
    mc.name "I've decided that taking care of your hair is diminishing the time you can spend serving me."
    mc.name "So, I will shave your pretty head, so you don't have to worry about that anymore."
    if the_person.obedience < 240:
        the_person "Oh, Master, please, don't remove my hair."
        mc.name "That's not you decision slave, or did you want to disobey me?"
        the_person "{size=16}...no master...{/size}"
    else:
        the_person "If that is your wish, Master."

    mc.name "Come, sit here."
    $ the_person.draw_person(position = "sitting")

    "You take out your clippers and get to work."

    $ the_person.clean_cache() # force rebuild of displayable
    $ the_person.hair_style = bald_hair.get_copy()
    $ the_person.draw_person(position = "sitting")

    "After about 10 minutes, most of her hair is gone and you continue with a razor."

    "You slide you hand over her smooth head."
    mc.name "There, all done."
    "She turns and looks into the mirror."

    $ the_person.change_obedience(20)
    the_person "Thank you, Master. I live to serve."
    return

label wakeup_duty_label(the_person):
    "You tell [the_person.possessive_title] to make sure you wake up in the morning."
    $ slave_add_wakeup_duty_action(the_person)
    return

label slave_training_label(the_person): # TODO: Add variations to these. They are supposed to be rather short interactions that do not take up time. Both "rewards" and punishments should be available. Some characters might see certain "punishments" as rewards too.
    menu:

        "Give her a head pat":
            "You give [the_person.possessive_title] a quick head pat as to signal approval of her actions." #Or something like that. I don't do writing.
            $ the_person.change_stats(obedience = 2, happiness = 2, arousal = 10, love = 2)

        "Give her a quick kiss":
            $ the_person.draw_person("kissing")
            "You give [the_person.possessive_title] a quick kiss"
            $ the_person.change_stats(happiness = 2, arousal = 10, love = 3)

        "Give her a serum":
            $ the_person.change_stats(obedience = 2)
            call give_serum(the_person) from _call_give_serum_slave_training

        "Increase submission" if the_person.get_opinion_score("being submissive") < 2:
            call increase_slave_submission_label(the_person) from _call_increase_slave_submission_slave_training

        #"Anal Training" if the_person.obedience > 250 and the_person.effective_sluttiness() > 60 and (the_person.get_opinion_score("anal sex") < 2 or the_person.sex_skills["Anal"] < 5):
        #    call slave_anal_training(the_person) from _call_slave_anal_training

        "Send her away":
            pass

    return

label slave_alarm_clock_label(the_person):
    # start with some MC arousal to shorten the sex loops.
    $ mc.change_arousal(40)
    #TODO: Finish all of the side functionality this event requires to be implemented.
    if the_person.sluttiness < 50:
        the_person "[the_person.mc_title], it's time to wake up."
        "You're woken up by the voice of [the_person.possessive_title]. You struggle to open your eyes and find her sitting on the edge of your bed."
        $ the_person.draw_person(position="sitting")
        mc.name "Uh... Huh?"
        "You roll over and check your phone. It's a couple of minutes before your alarm clock usually rings."
        $ the_person.draw_person(position = "back_peek")
        "She smiles and stands up, unsure of what to do next."
        $ the_person.draw_person()
        "You sit up on the side of the bed and stretch, letting out a long yawn."
        if the_person.sluttiness < 20:
            the_person "Oh... I should... Uh..."
            "[the_person.possessive_title] blushes and turns around suddenly. It takes you a moment to realize why: your morning wood is pitching an impressive tent with your underwear."
            the_person "No, it's perfectly natural. I'll give you some privacy."
            $ the_person.change_slut(2)
            $ the_person.draw_person(position = "back_peek")
            "She can't help but take some quick glances at you, but seems to be trying her best to respect your privacy."

        else:
            the_person "Oh, and you might want to take care of that before you go out [the_person.mc_title]."
            "She nods towards your crotch and you realize you're pitching an impressive tent."
            mc.name "Oh, sorry about that."
            the_person "No, it's perfectly natural and nothing to be embarrassed about."
            $ the_person.change_slut(2)
            "She stares at it for a short moment before pulling her eyes back up to meet yours."
            #TODO: She offers to pick out an outfit for you while you jerk off "To avoid bothering anyone at work".
            the_person "Certainly nothing to be embarrassed about, but I think you should take care of it before you leave."
            "[the_person.possessive_title] turns around and starts rifling through your closet."
            $ the_person.draw_person(position = "walking_away")
            the_person "I'll find you a nice outfit to wear to save you some time. Go ahead [the_person.mc_title], pretend I'm not even here. It's nothing I haven't seen before."
            menu:
                "Masturbate":
                    "You pull your underwear down, grab your hard cock, and start to stroke it."
                    mc.name "Thanks, [the_person.title], you're really helping me out this morning."
                    the_person "Anything to help you succeed."
                    $ the_person.draw_person(position = "back_peek")
                    "She wiggles her butt a bit as if to tease you, then turns her attention back to putting together an outfit for you."
                    $ the_person.call_dialogue("sex_strip")
                    "You keep jerking yourself off, pulling yourself closer and closer to orgasm."
                    "You're getting close when [the_person.possessive_title] turns around and walks back towards your bed with a handful of clothes."
                    the_person "I think you'll look really cute in this. Are you almost done [the_person.mc_title]?"
                    menu:
                        "Order [the_person.possessive_title] to get on her knees" if the_person.obedience >= 130:
                            mc.name "I'm so close. Get on your knees [the_person.title]."
                            $ the_person.call_dialogue("sex_obedience_accept")
                            $ the_person.draw_person(position = "blowjob")
                            menu:
                                "Order her to open her mouth" if the_person.obedience >= 140:
                                    mc.name "Open your mouth [the_person.title]."
                                    "She hesitates for a split second, then closes her eyes and opens her mouth."
                                    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                    "Seeing [the_person.possessive_title] presenting herself for you pushes you past the point of no return."
                                    $ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                    $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
                                    "You slide forward a little, place the tip of your cock on her bottom lip, and start to fire your load into her mouth."
                                    "[the_person.possessive_title] stays perfectly still while you cum. When you're done you sit back and sigh."
                                    $ the_person.call_dialogue("cum_mouth")
                                    $ the_person.change_stats(obedience = 5)
                                    $ the_person.draw_person()
                                    "She stands up and heads for the door."

                                "Order her to open her mouth\n{color=#ff0000}{size=18}Requires: 140 Obedience{/size}{/color} (disabled)" if the_person.obedience < 140:
                                    pass

                                "Order her to hold up her tits" if the_person.has_large_tits:
                                    mc.name "Hold up your tits, I'm going to cum!"
                                    "[the_person.possessive_title] mumbles something but does as she's told. She cups her large breasts in her hands and presents them in front of you."
                                    "You grunt and climax, firing your load out and right onto [the_person.possessive_title]'s chest."
                                    $ the_person.cum_on_tits()
                                    #TODO: have more clothing aware stuff here
                                    $ the_person.call_dialogue("cum_face")
                                    $ the_person.draw_person()
                                    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                                    $ the_person.change_stats(obedience = 3)

                                    # TODO: She should seem a little shocked, but otherwise okay with how things turned out
                                "Continue": # An escape if you get locked since obedience is less than 140 and has_large_tits() is false. #NOTE: Can write other alternatives
                                    pass

                        "Order her to get on her knees\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_person.obedience < 130:
                            pass

                        "Climax":
                            "Knowing that [the_person.possessive_title] is just a step away watching you stroke your cock and waiting for you to cum pushes you over the edge."
                            "You grunt and climax, firing your load out in an arc. [the_person.title] gasps softly and watches it fly, then looks away."
                            the_person "Well done [the_person.mc_title]. I'll make sure to clean that up while you're out today."
                            "She leans over and kisses you on the forehead."
                            the_person "Now get dressed or you'll be late for work."
                            $ clear_scene()

                "Ask her to leave":
                    mc.name "I think it will take care of itself [the_person.title]. Thanks for the offer but I can pick out my own outfit."
                    the_person "Oh, okay [the_person.mc_title]. Just make sure you don't give any of those nice girls you work with a shock when you walk in."
                    $ the_person.draw_person()
                    "She turns back to you and gives you a hug and a kiss. Her eyes continue to linger on your crotch."

    elif the_person.sluttiness < 70:
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realize you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob") #TODO: We need a handjob pose.
        "[the_person.possessive_title] is sitting on the side of your bed. The covers have been pulled down and she has your morning wood in her hand. She strokes it slowly as she speaks."
        the_person "Good morning [the_person.mc_title]. You didn't really specify how you would like to be woke up so I thought I'd improvise... You see; I came in to wake you up and saw this..."
        "She speeds up her strokes."
        the_person "I thought that this would be a much nicer way to wake up."
        mc.name "Right, of course... Good thinking, [the_person.title]."
        "You lie back, relax, and enjoy the feeling of [the_person.possessive_title] hand caressing your hard shaft."
        the_person "Anything for you [the_person.mc_title], I just want to make sure you're happy and successful."
        "After a few minutes you can feel your orgasm starting to build. [the_person.title] rubs your precum over your shaft and keeps stroking."
        menu:
            "Order her to take your cum in her mouth" if the_person.obedience >= 130:
                mc.name "I'm almost there [the_person.title], I need to cum in your mouth."
                $ the_person.change_obedience(5)
                $ the_person.call_dialogue("sex_obedience_accept")
                "She nods and leans over, stroking your cock faster and faster as she places the tip just inside her mouth."
                "The soft touch of her lips pushes you over the edge. You gasp and climax, shooting your hot load into [the_person.possessive_title]'s waiting mouth."
                $ the_person.cum_in_mouth()
                $ the_person.draw_person(position = "blowjob")
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
                "[the_person.title] pulls back off your cock slowly. She spits your cum out into her hand and straightens up."
                $ the_person.call_dialogue("cum_mouth")

            "Order her to take your cum in her mouth\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_person.obedience<130:
                pass
            "Climax":
                mc.name "I'm almost there [the_person.title], keep going!"
                "She nods and strokes your dick as fast as she can manage, pushing you over the edge."
                "You grunt and fire your hot load up into the air. It falls back down onto your stomach and [the_person.possessive_title]'s hand."
                "[the_person.possessive_title] strokes you slowly for a few seconds, then lets go and places her hand on her lap while you take a second to recover."

        the_person "Whew, that was a lot. I hope that leaves you feeling relaxed for the rest of the day."
        $ the_person.change_stats(love = 2, happiness = 5)
        $ the_person.draw_person(position = "back_peek")
        "She smiles and gets up. She pauses before she leaves your room."
        the_person "You better get ready now or you're going to be late!"

    elif the_person.sluttiness < 90:
        #TODO: image a lying down blowjob pose
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realize you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.possessive_title] is lying face down between your legs, gently sucking off your morning wood."
        "She notices you waking up and pulls off of your cock to speak."
        the_person "Good morning [the_person.mc_title]. I noticed your alarm hadn't gone off and came in to wake you up..."
        "She licks your shaft absentmindedly."
        the_person "And saw this. I thought this would be a much nicer way of waking you up."
        mc.name "That feels great [the_person.title]."
        $ the_person.change_happiness(5)
        "She smiles up at you, then lifts her head and slides your hard dick back into her mouth."
        "You lie back and enjoy the feeling of [the_person.possessive_title] sucking you off."
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
        "For several minutes the room is quiet save for a soft slurping sound each time [the_person.title] slides herself down your shaft."
        "You rest a hand on the back of her head as you feel your orgasm start to build, encouraging her to go faster and deeper."
        mc.name "I'm almost there [the_person.title], keep going!"
        "She mumbles out an unintelligible response and keeps sucking your cock."
        "You arch your back and grunt as you climax, firing a shot of cum into [the_person.possessive_title]'s mouth."
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob")
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
        "She pulls back until the tip of your cock is just inside her lips and holds there, collecting each new spurt of semen until you're completely spent."
        "When you're done she pulls up and off, keeping her lips tight to avoid spilling any onto you."
        menu:
            "Order her to swallow" if the_person.obedience >= 130:
                mc.name "That was great [the_person.title], now I want you to swallow."
                $ play_swallow_sound()
                "She looks at you and hesitates for a split second, then you see her throat bob as she sucks down your cum."
                $ the_person.change_obedience(5)
                $ play_swallow_sound()
                "[the_person.possessive_title] takes a second gulp to make sure it's all gone, then opens her mouth and takes a deep breath."
                $ the_person.call_dialogue("cum_mouth")

            "Order her to swallow\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_person.obedience < 130:
                pass

            "Let her spit it out":
                $ the_person.draw_person(position = "sitting")
                "You watch as she slides her legs off the side of your bed, holds out a hand, and spits your cum out into it."

        the_person "Whew, I'm glad I was able to help with that [the_person.mc_title]. That was a lot more than I was expecting."
        mc.name "Thanks, [the_person.title], you're the best."
        $ the_person.change_stats(love = 2)
        the_person "My pleasure, now you should be getting up or you'll be late for work!"

    else:
        # First we need to take her and remove enough clothing that we can get to her vagina, otherwise none of this stuff makes sense.
        # This makes sure skirts are kept on (because this is suppose to be a quickly).
        $ the_person.strip_outfit(exclude_upper = True, position = "cowgirl", emotion = "happy")
        "You're woken up by your bed shifting under you and a sudden weight around your waist."
        $ the_person.draw_person(position = "cowgirl", emotion = "happy")
        "[the_person.possessive_title] has pulled down your sheets and underwear and is straddling you. The tip of your morning wood is brushing against her pussy."
        the_person "Good morning [the_person.mc_title]. I came to wake you up, but then I noticed this..."
        "She grinds her hips back and forth, rubbing your shaft along the lips of her cunt."
        the_person "Would you like me to take care of this for you?"
        menu:
            "Let [the_person.possessive_title] fuck you":
                mc.name "That would be great [the_person.title]."
                $ the_person.change_stats(happiness = 5, love = 2)
                "You lie back and relax as [the_person.possessive_title] lowers herself down onto your hard cock."
                # call fuck_person(the_person, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, girl_in_charge = True, position_locked = True) from _slave_alarm_clock_label_2
                call get_fucked(the_person, the_goal = "vaginal creampie", private= True, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, allow_continue = False) from _call_get_fucked_slave_alarm_clock_label_2
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    $ the_person.change_love(5)
                    the_person "That was amazing [the_person.mc_title]..."
                    "She rolls over and kisses you, then rests her head on your chest."
                    "After a minute she sighs and starts to get up."
                    the_person "I shouldn't be keeping you from your work, I don't want to make you any more late!"
                    "She reaches down to help you up. She smiles at you longingly, eyes lingering on your crotch, patiently waiting for your next move."
                else:
                    the_person "I'm glad I could help [the_person.mc_title]. Now you should hurry up before you're late!"
                    "[the_person.possessive_title] kisses you on the forehead and stands up arms behind her back."
                $ the_person.review_outfit()

            "Ask her to get off":
                mc.name "Sorry [the_person.title], but I need to save my energy for later today."
                $ the_person.change_stats(obedience = 5, happiness = -3)
                "She frowns but nods. She swings her leg back over you and stands up."
                $ the_person.draw_person()
                the_person "Of course [the_person.mc_title], if you need me for anything just let me know. I hope you aren't running too late!"
                if removed_something:
                    "[the_person.possessive_title] collects some of her discarded clothing from the floor and starts to dress herself."
                else:
                    "[the_person.possessive_title] gives you a kiss on the forehead and stands patiently by your side."

    $ the_person.draw_person(position = "stand3", emotion = "happy")
    "You finally get out of bed and prepare yourself for the day ahead."

    call slave_training_label(the_person) from _call_slave_training_slave_alarm_clock_label

    # At the end we would want the "Slave" to be in the room and intractable after the crisis event. Moving them during the event causes issues with scheduled destinations on run_move
    $ clear_scene()
    return

label increase_slave_submission_label(the_person):
    mc.name "[the_person.title] get on your knees."
    "[the_person.possessive_title] looks at you, meekly nods and drops to her knees."
    $ the_person.draw_person(position = "kneeling1")

    mc.name "[the_person.title], I sense you have not yet completely accepted me as your master."
    "[the_person.possessive_title] starts to shake her head, but you simply hold up your hand to stop her before she starts."
    mc.name "Do you want to be my devoted and loyal slave?"
    if the_person.obedience < 200 or the_person.get_opinion_score("being submissive") < 1:
        "She looks at you intently..."
        the_person "No Master, I've got other duties that prevent that."
        mc.name "It seems you need a punishment for this insolence."
        if not the_person.vagina_visible:
            mc.name "Take off your clothes and bend over against the desk."
            $ the_person.strip_outfit(exclude_upper = True, position = "stand3", emotion = "sad")
        else:
            mc.name "Bend over against the desk."
        $ the_person.draw_person(position = "standing_doggy", emotion = "sad")
        "You slowly walk over to her and start to rub her ass cheeks."
        $ the_person.change_stats(arousal = 10)
        "Suddenly you pull you hand back and start giving her the spanking she deserves."
        $ play_spank_sound()
        "SMACK! SMACK! SMACK!"
        the_person "Please Master... OUCH, I'll try to obey... AH... your wishes... OW, please let me... OUCH... prove it to you..."
        $ play_spank_sound()
        mc.name "Be quiet, slave and take your punishment with pride."
        "You keep on punishing her for another minute, while she tries to stifle her cries."
        mc.name "Very well, slave, I will be demanding your complete submission next time."
        $ the_person.draw_person(position = "stand2", emotion = "angry")
        if the_person.obedience < 200:
            $ the_person.change_obedience(10)
            "She turns around with a slight defiant stare..."
        else:
            "She turns around, with a faint smile and devotion in her eyes."
            $ the_person.increase_opinion_score("being submissive")
            $ the_person.change_stats(obedience = 10, arousal = 20)

        the_person "Yes Master, I will try to please you better next time."
    else:
        "She looks at you with tears in her eyes."
        the_person "Yes Master, I want to serve you as a good slave should, unconditionally and loyal."
        $ the_person.change_stats(happiness = 10, love = 10, arousal = 30)
        "You smile and pat her on the head."
        $ the_person.max_opinion_score("being submissive")
        if not the_person.outfit.has_full_access:
            mc.name "Now stand up and take off your clothes."
            $ the_person.strip_outfit(position = "stand3", emotion = "happy")
            $ the_person.change_stats(obedience = 2, arousal = 10)
        mc.name "I think you deserve a reward, get on your hands and knees, like a good little pet."
        $ the_person.change_stats(obedience = 3, arousal = 10)
        the_person "Yes Master, as you command."
        $ the_person.draw_person(position = "doggy")
        $ mc.change_arousal(40) # make the fuck loop a little shorter
        $ the_person.break_taboo("anal_sex")
        "You pull out your hard cock and shove it right into her ass."
        call fuck_person(the_person, start_position = doggy_anal, start_object = make_floor(), skip_intro = True, skip_condom = True, position_locked = True, affair_ask_after = False) from _call_fuck_person_increase_slave_submission
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Thank you Master, for giving me such satisfaction."
        else:
            the_person "Thank you Master, for allowing me to satisfy you."
        $ the_person.apply_planned_outfit()
    return

label slave_anal_training(the_person):
    $ ran_num = the_person.event_triggers_dict.get("anal_training", 0)
    if ran_num == 0:
        pass
    elif ran_num == 1:
        pass
    elif ran_num > 1:
        pass

    $ the_person.increase_opinion_score("anal sex")
    $ the_person.increase_sex_skill("Anal")
    $ the_person.event_triggers_dict["anal_training"] = ran_num + 1
    return
