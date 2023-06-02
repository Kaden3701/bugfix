## Business Meeting Crisis Mod by Tristimdorion
init 2 python:
    def business_meeting_requirement():
        if time_of_day == 0 or time_of_day== 4 or mc.business.is_weekend:
            return False
        if not mc.is_at_work or mc.business.employee_count < 3:
            return False
        return True

    def remove_person_shoes(person):
        feet = person.outfit.remove_random_feet(top_layer_first = True, do_not_remove = True)
        if feet:
            person.draw_animated_removal(feet, position="sitting", emotion="default")
        return

    business_meeting_action = ActionMod("Business Meeting", business_meeting_requirement, "business_meeting_action_label",
        menu_tooltip = "An employee wants to discuss some business with you.", category = "Business", is_crisis = True)

label business_meeting_action_label():
    $ the_person = get_random_employees(1)
    if the_person is None:
        return

    $ the_place = mc.business.get_employee_workstation(the_person)
    $ day_part = time_of_day_string(time_of_day)

    if (mc.location ==  the_place):
        "You're hard at work in the [day_part], when [the_person.possessive_title] asks you over to discuss some plans."
    else:
        "You're hard at work in the [day_part], when [the_person.possessive_title] calls you on your phone to discuss some plans."

    "You meet up in an empty office of the [the_place.formal_name] department."

    $ the_place.show_background()
    $ the_place = None
    $ done = False
    $ the_person.draw_person(position="sitting", emotion="happy")

    call business_meeting_introduction(the_person) from _call_business_meeting_introduction_1
    call business_meeting_flirtation(the_person) from _call_business_meeting_flirtation_1
    if the_person.effective_sluttiness() > 25:
        call business_meeting_arousal(the_person) from _call_business_meeting_arousal_1
        if (the_person.effective_sluttiness() > 40):
            call business_meeting_seduction(the_person) from _call_business_meeting_seduction_1
            $ done = _return
        else:
            $ the_person.change_happiness(5)
            "After a while [the_person.title] wraps up her story."
    else:
        $ the_person.change_happiness(5)
        "[the_person.title] finishes up her proposal."

    $ the_person.apply_planned_outfit()

    call business_meeting_end(the_person, done) from _call_business_meeting_end_1

    $ ran_num = renpy.random.randint(1, 3)
    $ hr_employee = mc.business.hr_director or get_random_from_list(mc.business.hr_team)
    if hr_employee == the_person:
        "You give [the_person.title] a call and tell her that she can implement the changes you discussed."
    elif hr_employee is None:
        "You decide to implement the changes you discussed with [the_person.title]."
    else:
        "You make a call to [hr_employee.title] from HR to implement some of the changes you discussed with [the_person.title]."
    $ mc.business.effectiveness_cap += ran_num
    if get_HR_director_tag("business_HR_eff_bonus"):
        $ set_HR_director_tag("business_HR_eff_bonus", get_HR_director_tag("business_HR_eff_bonus") + ran_num)
    #$ mc.log_event("Company Efficiency: " + str(mc.business.effectiveness_cap) + "%", "float_text_grey")
    "The changes increased your business efficiency by [ran_num]%%."

    $ hr_employee = None
    $ mc.location.show_background()
    $ clear_scene()
    return

label business_meeting_introduction(the_person):
    the_person "Hello [the_person.mc_title], thank you for meeting me on such short notice."
    the_person "I have been thinking about some ways to improve the streamlining of the company."
    return

label business_meeting_flirtation(the_person):
    if the_person.effective_sluttiness() > 15:
        $ remove_person_shoes(the_person)
        $ mc.change_locked_clarity(10)
        if the_person.outfit.feet_available:
            "While talking about her proposal, you suddenly feel her bare foot moving up and down your leg."
        else:
            "While talking about her proposal, you suddenly feel her stockinged foot moving up and down your leg."
    else:
        "You mind wanders off while she is talking..."
    return

label business_meeting_arousal(the_person):
    if the_person.effective_sluttiness() > 30:
        "She moves up to your crotch and unzips your pants with her feet, sliding her foot over your growing bulge."
        $ mc.change_locked_clarity(20)
        the_person "Oh my, [the_person.mc_title] it seems my proposal got you all excited."
    else:
        the_person "She keeps stroking your legs while she talks, making sure you are focused on her."
    return

label business_meeting_seduction(the_person):
    if the_person.effective_sluttiness() > 40:
        $ strip_choice = the_person.choose_strip_clothing_item()
        if strip_choice:
            "After talking for a while she takes off her [strip_choice.display_name]."
            $ the_person.draw_animated_removal(strip_choice, position="sitting", emotion="default")
            if the_person.tits_visible:
                if the_person.has_taboo("bare_tits"):
                    $ mc.change_locked_clarity(10)
                    "She hesitates for a second, it seems she forgot she didn't put on a bra today, but after a second she continues without hesitation."
                    $ the_person.break_taboo("bare_tits")
            elif not the_person.bra_covered:
                $ mc.change_locked_clarity(5)
                if the_person.has_taboo("underwear_nudity"):
                    "She seems nervous at first, but quickly gets used to being in her underwear in front of you."
                    $ the_person.break_taboo("underwear_nudity")

            the_person "This should help you focus, [the_person.mc_title]."
            $ strip_choice = None
            $ mc.change_arousal(20)

        if the_person.has_cum_fetish:
            the_person "I'll tell you what. I'll give you the rest of the proposal if you let me have a taste of that cum of yours..."
            "[the_person.possessive_title]'s cum fetish has driven her to bargain with you. It seems you have the opportunity for an expert cock sucker to get you off."
            menu:
                "Continue":
                    $ the_person.draw_person(position = "blowjob")
                    "[the_person.title] drops to her knees in front of you, and soon you feel her expert tongue running up and down your length."
                    $ mc.change_locked_clarity(20)
                    "You sigh and let yourself enjoy the sensations as your employee gets to work."
                    call get_fucked(the_person, private= True, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = False, allow_continue = False) from _call_get_sucked_during_meeting_01
                    $ the_person.event_triggers_dict["LastCumFetish"] = day
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    return True
                "Not Now":
                    mc.name "I'm sorry [the_person.title], I've got another meeting to attend."
                    $ the_person.draw_person(position = "stand4", emotion="sad")
                    "[the_person.possessive_title] stands up with a disappointed look on her face."
                    $ the_person.change_happiness(-5)
                    return False
        elif the_person.effective_sluttiness() > 60:
            "After spending a few more minutes talking she suddenly perks up."
            the_person "I'm sorry [the_person.mc_title], it seems I've dropped something..."

            $ the_person.draw_person(position = "blowjob")
            $ mc.change_locked_clarity(20)

            if the_person.has_taboo("touching_penis"):
                the_person "Oh my god, that is a big one!"
                mc.name "You can touch it for real, if you want."
                "She wraps her hand around your shaft and rubs it gently."
                the_person "Sure thing [the_person.mc_title], it feels nice and warm."
                $ the_person.break_taboo("touching_penis")
            else:
                "[the_person.possessive_title] slides under the table grabbing your now exposed cock looking up at you with a smile."

            $ the_person.change_arousal(25)
            menu:
                "Continue":
                    if the_person.has_taboo("sucking_cock"):
                        if the_person.is_bald:
                            "You move your hand to her face, slowly moving your hand behind her head pulling her closer to your throbbing cock."
                        else:
                            "You move your hand to her face, pushing back a hair, slowly moving your hand behind her head pulling her closer to your throbbing cock."
                        "She looks at you with confusion when the tip of your cock moves over her cheek and lips."
                        mc.name "Why don't you give it a lick, you might like the taste."
                        the_person "What? I don't know... it looks quite tasty though."
                        $ mc.change_locked_clarity(20)
                        "She kisses the tip slowly at first, but soon after she starts moving her tongue along the base of the head."
                        mc.name "Now try sliding it into your mouth and sucking on it, like eating a popsicle."
                        $ mc.change_locked_clarity(30)
                        "[the_person.possessive_title] only nods slightly and starts to move your member into her mouth."
                        $ the_person.break_taboo("sucking_cock")

                    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_business_meeting
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    return True
                "Not now":
                    mc.name "I'm sorry [the_person.title], I've got another meeting to attend."
                    $ the_person.draw_person(position = "stand4", emotion="sad")
                    "[the_person.possessive_title] stands up with a disappointed look on her face."
                    $ the_person.change_happiness(-5)
        else:
            "You can't help but admire [the_person.possessive_title] boldness, while she keeps on talking."
    else:
        "After a while [the_person.title] stops rubbing your exposed member."
        the_person "I will leave you now, it seems you have some other business to take care of."
    return False

label business_meeting_end(the_person, done):
    if the_person.effective_sluttiness() < 20:
        the_person "Thank you for listening to my ideas, [the_person.mc_title]."
    elif done:
        the_person "Thank you, [the_person.mc_title], I hope you 'come' to see things my way."
    else:
        the_person "Thank you, [the_person.mc_title], I hope you liked my contribution."

    if not done:
        "You thank [the_person.title] for her time and assure her that you will look into the matter."
    else:
        mc.name "You did well [the_person.title], this was very productive and relaxing."

    $ the_person.draw_person(position="walking_away")

    if not done:
        "You watch her walking away, deciding what to do next."
    else:
        $ the_person.apply_planned_outfit()
        "[the_person.possessive_title] puts on her clothes and walks away."

    "After contemplating what just happened, you decide what to do next."
    return
