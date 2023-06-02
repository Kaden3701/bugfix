# override standard strip club dance to remove randomness of performer on stage

init 5 python:
    def get_next_stripper():
        def update_strip_club_rotation():
            rotation = [x.identifier for x in stripclub_strippers]
            renpy.random.shuffle(rotation)
            mc.business.event_triggers_dict["stripper_rotation_changed"] = day
            mc.business.event_triggers_dict["stripper_rotation"] = rotation
            mc.business.event_triggers_dict["stripper_number"] = 0
            return rotation

        if mc.business.event_triggers_dict.get("stripper_rotation_changed", 0) != day:
            update_strip_club_rotation()    # rotation changes daily

        rotation = mc.business.event_triggers_dict.get("stripper_rotation", None)
        if not rotation:
            rotation = update_strip_club_rotation()

        stripper = None
        while not stripper:
            current = mc.business.event_triggers_dict.get("stripper_number", 0) + 1
            if current > len(stripclub_strippers):
                current = 1

            mc.business.event_triggers_dict["stripper_number"] = current
            # select stripper from girls working right now
            stripper = find_in_list(lambda x: x.identifier == rotation[current-1], [x for x in stripclub_strippers if x in mc.location.people])

        return stripper


label stripclub_dance():
    #Watch a dance at the strip club.
    #-> You sit down and watch. A girl (generate a list of girls at the club) comes out wearing one of several special outfits.
    #-> She poses a few times. Each time you can tip her or just watch.
    #-> If you tip enough she strips off her bra and/or panties.
    #-> When she ends her dance, if you've paid enough she may ask if you want to come back for a private lap dance.
    #-> Lap dance scene may just turn into sex.

    "You decide to stay a while and enjoy a show. You stop by the bar to satisfy the drink minimum, then find a seat near the edge of the stage."
    if get_strip_club_foreclosed_stage() < 5:
        $ mc.business.change_funds(-20)
    "You nurse your beer while you wait for the next performer."

    $ the_person = get_next_stripper()

    $ the_person.apply_outfit(stripclub_wardrobe.pick_random_outfit()) #TODO: Add more stripper outfits
    $ title = the_person.title
    $ the_person.draw_person(position = "walking_away", the_animation = ass_bob)
    "A new song starts playing over the speakers and a girl steps out onto the stage."
    $ the_person.draw_person(the_animation = idle_wiggle_animation)
    if title is not None:
        if the_person.has_role(cousin_role):
            if the_person.event_triggers_dict.get("blackmail_level", 999) < 2 and not the_person.event_triggers_dict.get("seen_cousin_stripping",False):
                $ add_cousin_blackmail_2_confront_action()

                "It takes you a moment to recognize your cousin, [the_person.title], as she struts out onto the stage."
                if not the_person.event_triggers_dict.get("found_stripping_clue", False):
                    "[the_person.possessive_title]'s late nights and secret keeping suddenly make a lot more sense."

                "With the glare of the stage lights it's likely she won't be able to see who you are, but you can talk to her later and use this as leverage to blackmail her."

            else:
                "You recognize your cousin almost as soon as she steps onto the stage."

        elif the_person.has_role(sister_role):
            "You recognize your little sister almost as soon as she steps onto the stage."

        elif the_person.has_role(aunt_role):
            "You recognize your aunt as she steps into the stage spotlights."

        elif the_person.has_role(mother_role):
            "You recognize your mother as soon as she steps into the stage spotlight."

        elif the_person.has_role(employee_role):
            "You recognize [title] as one of your employees."

        else:
            "You recognize her as [title]."

        $ title = the_person.possessive_title #Change to their possessive title, because that sounds better in the following dialogue

    else:
        $ title = the_person.create_formatted_title("The stripper")

    # you seen her on stage, so you know she's a stripper...although you might not know her name
    if not the_person.event_triggers_dict.get("job_known", True):
        $ the_person.event_triggers_dict["job_known"] = True

    "She poses for a moment, and the crowd cheers around you. Then she starts to strut down the walkway."
    "She stops at the end of the stage, surrounded on three sides by eagerly watching men."
    "[title] starts to dance to the music, swinging her hips and turning slowly to show herself off to all members of the crowd."
    call stripshow_strip(the_person) from _call_stripshow_strip_dance
    $ the_person.draw_person(position = "back_peek", the_animation = ass_bob, animation_effect_strength = 0.7)
    "She spins and poses for her audience, who respond with whoops and cheers."
    $ the_person.change_arousal(2)
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_1
    if the_person.has_large_tits:
        if the_person.tits_available:
            $ mc.change_locked_clarity(15)
            "As the music builds, [title]'s dance becomes more energetic. Her [the_person.tits_description] bounce and jiggle in rhythm with her movements."
        else:
            $ mc.change_locked_clarity(10)
            "As the music builds, [title]'s dance becomes more energetic. Her big tits bounce and jiggle, looking almost desperate to escape."
    else:
        $ mc.change_locked_clarity(5)
        "As the music builds, [title]'s dance becomes more energetic. She runs her hands over her tight body, accentuating her curves."
    $ the_person.change_arousal(3)
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_2
    $ the_person.draw_person(position = get_random_from_list(cousin_strip_pose_list), the_animation = blowjob_bob, animation_effect_strength = 0.7)
    $ mc.change_locked_clarity(5)
    "Her music hits its crescendo and her dancing does the same. [title] holds onto the pole in the middle of the stage and spins herself around it."
    $ the_person.change_arousal(4)
    call stripshow_strip(the_person) from _call_stripshow_strip_dance_3
    $ the_person.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.8)
    if the_person.vagina_visible:
        $ the_person.change_arousal(8)
        $ mc.change_locked_clarity(15)
        "As the song comes to an end, the dancer lowers herself to all fours, showing off her ass and pussy to the crowd."
    else:
        $ the_person.change_arousal(5)
        $ mc.change_locked_clarity(10)
        "As the song comes to an end, the dancer lowers herself to all fours. She spreads her legs and works her hips, jiggling her ass for the crowd's amusement."

    $ the_person.draw_person()
    "She stands up and waves to her audience."
    the_person "Thank you everyone, you've been wonderful!"
    $ the_person.draw_person(position = "walking_away")
    "[title] blows a kiss and struts off stage."

    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return

label stripshow_strip(the_person):
    menu:
        "Throw some cash\n{color=#ff0000}{size=18}Costs: $20{/size}{/color}" if mc.business.has_funds(20):
            $ mc.business.change_funds(-20)
            "You reach into your wallet and pull out a $20 bill. You wait until the dancer is looking in your direction, then throw it onto the stage."

            $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_lower = True,  exclude_feet = True, do_not_remove = True) #Try and get a bra/top first if you can
            if the_clothing is None:
                $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_lower = False,  exclude_feet = True, do_not_remove = True) #When that fails get her bottom/panties.

            if the_clothing:
                $ the_person.draw_animated_removal(the_clothing)
                $ mc.change_locked_clarity(10)
                "She smiles at you and starts to peel off her [the_clothing.display_name]."
            else:
                $ mc.change_locked_clarity(5)
                "She smiles and wiggles her hips for you."
            $ del the_clothing

        "Throw some cash\n{color=#ff0000}{size=18}Requires: $20{/size}{/color} (disabled)" if not mc.business.has_funds(20):
            pass

        "Just enjoy the show":
            "You lean back in your seat and enjoy the dance."
            if renpy.random.randint(0,100) < 30:
                #Someone else throws cash onto the stage.
                "On the other side of the stage, someone waves a bill at the dancer."
                $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_lower = True,  exclude_feet = True, do_not_remove = True) #Try and get a bra/top first if you can
                if the_clothing is None:
                    $ the_clothing = the_person.outfit.remove_random_any(top_layer_first = True, exclude_lower = False,  exclude_feet = True, do_not_remove = True) #When that fails get her bottom/panties.

                if the_clothing:
                    "She takes the money and starts to slowly strip off her [the_clothing.display_name]."
                    $ mc.change_locked_clarity(5)
                    $ the_person.draw_animated_removal(the_clothing)
                else:
                    "She takes the money and holds onto it while she continues to move her body to the music."
                $ del the_clothing
    return
