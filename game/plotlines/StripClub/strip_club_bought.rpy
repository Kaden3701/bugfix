## Stripclub storyline Mod by Corrado
# You actually buy the stripclub and hire the strippers.

init 5 python:
    # imported from bugfix
    cousin_strip_pose_list = ["walking_away","back_peek","standing_doggy","stand2","stand3","stand4","stand5"] #A list to let us randomly get some poses so each dance is a little different.

    def strip_club_call_in_all_strippers():
        for stripper in stripclub_strippers:
            stripper.change_location(strip_club)
        return

    # for testing purposes, convert strip club to player owned.
    def test_strip_club():
        mc.business.event_triggers_dict["old_strip_club_owner"] = strip_club_owner
        mc.business.event_triggers_dict["foreclosed_day"] = day
        mc.business.event_triggers_dict["old_strip_club_name"] = strip_club.formal_name
        strip_club.formal_name = "Starlight Club"
        strip_club.visible = True
        set_strip_club_foreclosed_stage(5)
        add_strip_club_hire_employee_action_to_mc_actions()
        for stripper in stripclub_strippers:
            stripper.set_title(get_random_from_list(stripper.get_titles()))
            stripper.set_mc_title("Boss")
            stripper.set_possessive_title("The stripper")
            stripper.change_stats(happiness = 10, obedience = 5, love = 5)
        return

label strip_club_bought_strippers_selection_label(the_person): # Talk event
    python:
        cousin.set_override_schedule(None, the_times = [3, 4])  # reset alternative schedule
        for person in strip_club.people:
            if person is not cousin:
                person.change_location(downtown) # Failsafe to remove anyone improperly scheduled to be at the strip club
    $ the_person.draw_person()
    mc.name "Hey [the_person.title], good, you came."
    the_person "Yeah, I'm here, now tell me why I'm here."
    mc.name "Not yet, can you call all your old coworkers from the strip club and get them here as soon as possible?"
    the_person "You are a weird pervert, you know. But fine, I'll humor you."
    "She talks on the phone for a while."
    the_person "Right, I was able to contact them all, they will be here as soon as they can."
    mc.name "Good, come, let's go inside."
    the_person "You have keys for this place? You must have been a very good customer for that cheap fuck to give you some keys."
    $ strip_club.background_image = Image(get_file_handle("Club_Background.png")) # Set up the original background
    $ mc.location.show_background()
    "You just smile and take her inside. About 30 minutes later, they're all there, eager to get their jobs back."
    $ strip_club_call_in_all_strippers()
    $ the_person.draw_person()
    the_person "Okay [mc.name], we're all here... Actually, what are we doing here? You wanted a private party?"
    mc.name "Calm your tits [the_person.title], I'm here because I bought this place and now it belongs to me."
    "The girls all stare at you in surprise."
    mc.name "If you all are still looking to get your old jobs back, I think we need to discuss it a bit, don't you agree?"
    $ the_person.draw_person(emotion = "angry")
    the_person "You bought this place, [mc.name]? Really? What does that mean for us? We can get our old jobs back? What about our back pay?"
    $ name_string = mc.business.event_triggers_dict.get("old_strip_club_owner", "that cheap fuck")
    mc.name "For your back pay, I can't do anything about that. The money [name_string] owed you is gone."
    mc.name "I'm not stupid, so I recognize that hiring skilled and experienced workers has its advantages."
    mc.name "Here's my offer: you girls show me your skills on the stage, and I will decide if I'm going to give you your old job back..."
    mc.name "If my evaluation is positive, you sign the new contract, and I'll pay you a $500 signing bonus."
    $ the_person.draw_person(emotion = "default")
    the_person "And what will be our daily salary?"
    mc.name "I'll calculate it based on your skills on the stage. Sexy girls attract more customers; more customers, more profit, so you get a better salary."

    # one stripper does not apply
    $ the_person = get_random_from_list([x for x in stripclub_strippers if x not in [cousin]])
    $ mc.location.show_background()
    $ the_person.draw_person(emotion = "happy")
    the_person "[mc.name], I'm sorry to interrupt, but in the meantime I found another job, it doesn't pay as much as stripping, but it gives me enough to live, so..."
    mc.name "Well, I can't force anyone to stay, if one day you decide that you need more cash to get by, I'll give you your chance, but let me wish you the best with your new job."
    the_person "Now I'm a little sad, [mc.name]... Finally this could become a real 'Gentleman's Club', with you here..."
    the_person "I hope to see you again someday, thank you for your understanding."
    $ the_person.draw_person(emotion = "happy", position = "kissing")
    "She leans on you, placing a hand on your chest and giving you a soft kiss on your cheek."
    the_person "Goodbye, [mc.name]!"
    $ the_person.draw_person(position = "walking_away")
    if the_person.title is None:
        mc.name "Goodbye!"
    else:
        mc.name "Goodbye, [the_person.title]!"
    $ the_person.change_stats(happiness = 5, obedience = 3, love = 3)
    if not the_person in unique_character_list:
        $ the_person.set_override_schedule(None, the_days=[0,1,2,3,4,5,6], the_times=[3,4])
    $ the_person.job.quit_function = stripper_quit
    $ the_person.quit_job()
    $ the_person.change_location(the_person.home)

    # resume dialog with
    $ the_person = cousin
    $ the_person.draw_person()
    the_person "I still don't know if I want my old job back... I mean, of course I want it, I just don't know if I will enjoy working for you."
    mc.name "Your choice, [the_person.title], but only after MY choice to hire you or not. Don't forget who's the boss here now."
    $ the_person.change_obedience(10)
    $ the_person.draw_person(emotion = "happy")
    the_person "I like the job, and most importantly, I like the money... I can manage a working relationship with you."
    mc.name "Okay girls, if we haven't met before, do a quick introduction and then start stripping. Let's get the music started, and show me your best! Who wants to go first?"

    # loop remaining strippers and hire
    while mc.location.person_count > 0:
        $ the_person = get_random_from_list(mc.location.people)
        $ the_person.stripper_salary = calculate_stripper_salary(the_person)
        call strip_club_evaluate_stripper(the_person) from _call_strip_club_evaluate_stripper_selection

    $ strip_club_call_in_all_strippers()
    $ clear_scene()

    if __builtin__.len(stripclub_strippers) > 1:
        $ the_person = get_random_from_list([x for x in stripclub_strippers if x not in [cousin]])
        $ the_person.draw_person(emotion = "happy", position = "stand5")
        mc.name "Okay girls, the team is built. Enjoy the rest of your day, we will reopen the club tomorrow evening."
        "Excited to have got back their jobs and the unexpected pay raises, the girls get dressed and walk out of the club."
    elif __builtin__.len(stripclub_strippers) > 0:
        mc.name "Okay [stripclub_strippers[0].name], I will count on you. Enjoy the rest of the day, we will re-open the club tomorrow evening."
        "Excited to have got back her job and the unexpected pay raise, the girl puts her clothes back on and walks out."
    else:
        mc.name "Damn, I bought a stripclub and now I don't have any strippers..."
        mc.name "I'd better hurry and find someone to work here fast, if I want to reopen this place."

    $ set_strip_club_foreclosed_stage(5)
    $ strip_club.add_action(strip_club_show_action)
    $ add_strip_club_hire_employee_action_to_mc_actions()

    "As the last one left in the club, you turn off the lights, close the doors, and return home eager for a good night's rest."
    $ mc.change_location(bedroom)
    $ add_strip_club_manager_reminder_action()
    call advance_time from _call_advance_time_club_bought_strippers_selection
    # since we are in a talk event with Gabrielle, we need to exit using a jump.
    return

label strip_club_evaluate_stripper(the_person):
    python:
        mc.location.show_background()
        the_person.outfit = stripclub_wardrobe.pick_random_outfit()
        the_person.draw_person(emotion = "happy", position = "stand4")
        if the_person not in unique_character_list:
            the_person.set_override_schedule(None, the_days=[0,1,2,3,4,5,6], the_times=[3,4])
        if the_person.is_employee:
            # switch her back to strippers without changing her location (should only apply to Cousin, since other strippers can't work for you while stripping)
            mc.business.undesignate_person(the_person)
            the_person.change_job(unemployed_job, job_known = True)
            if the_person not in stripclub_strippers:
                stripclub_strippers.append(the_person)

    "A new song starts playing over the speakers and a stripper moves elegantly up on the stage."

    if the_person.title is None:
        $ the_person.set_title(get_random_from_list(the_person.get_titles()))
        $ the_person.set_mc_title("Boss")
        $ the_person.set_possessive_title("The stripper")
        the_person "Hi [the_person.mc_title], my name is [the_person.title] and I'm [the_person.age] years old."

    "She shows off a few poses, then she starts to strut down the walkway and stops at the end of the stage."
    "[the_person.title] starts to dance to the music, swinging her hips and turning slowly to show herself off."
    $ the_person.draw_person(position = "back_peek")
    "She spins and poses for you, and you can easily imagine a crowd responding with whoops and cheers."
    if the_person.has_large_tits:
        if the_person.tits_available:
            "As the music builds, [the_person.title]'s dance becomes more energetic. Her [the_person.tits_description] bounce and jiggle in rhythm with her movements."
        else:
            "As the music builds, [the_person.title]'s dance becomes more energetic. Her big tits bounce and jiggle, looking almost desperate to escape her clothing."
    else:
        "As the music builds, [the_person.title]'s dance becomes more energetic. She runs her hands over her tight body, accentuating her curves."
    $ the_person.draw_person(position = get_random_from_list(cousin_strip_pose_list), the_animation = blowjob_bob, animation_effect_strength = 1.5)
    "Her music hits its crescendo and her dancing does the same. [the_person.title] holds onto the pole in the middle of the stage and spins herself around it."
    $ the_person.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 1.5)
    if the_person.vagina_visible:
        "As the song comes to an end, the dancer lowers herself to all fours, showing off her ass and pussy."
    else:
        "As the song comes to an end, the dancer lowers herself to all fours. She spreads her legs and works her hips, jiggling her ass for your amusement."
    $ the_person.draw_person()
    "She stands up and gives you a coy smile, hoping for your final approval."
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.title]'s body as she walks offstage to rejoin you and the other girls."
    $ the_person.draw_person(emotion = "happy")
    the_person "So [mc.name] what do you think, am I good enough to be one of your girls?"
    "She puts a hand on your shoulder pressing her bosom against your body..."
    menu:
        "Yes" if mc.business.has_funds(500):
            $ the_person.change_job(stripclub_stripper_job, job_known = True)
            mc.name "Yes, you impressed me! Your salary will be $[the_person.stripper_salary] per day excluding tips, if you agree?"
            $ name_string = mc.business.event_triggers_dict.get("old_strip_club_owner", "that cheap fuck")
            $ ran_num = __builtin__.int(((the_person.stripper_salary / 20) - 1) * 100)
            if ran_num < 5: # make sure we are >= 5%
                $ ran_num = 5
            the_person "If I agree? Of course, that's [ran_num]%% more than what [name_string] paid me before!"
            $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
            "Without any forewarning she pushes her tongue into your mouth showing you her happiness and gratitude."
            $ mc.business.change_funds(-500)
            $ the_person.set_possessive_title("Your stripper")
            $ the_person.draw_person(emotion = "happy")
            "After a few seconds, when she stops, you give her the promised signing bonus."
            $ the_person.change_stats(happiness = 5, obedience = 3, love = 3)
            $ the_person.change_location(the_person.home) # Avoid to process the person again
        "Yes\n{color=#ff0000}{size=18}Insufficient funds{/size}{/color} (disabled)" if not mc.business.has_funds(500):
            pass
        "Maybe later": # Don't need to reschedule
            $ the_person.draw_person(emotion = "sad", position = "stand2")
            "[the_person.title] was so sure she would get back her job she can't utter a single word."
            "She can't believe your decision, and in a few seconds her face is striped by copious tears."
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person(emotion = "sad", position = "walking_away")
            if the_person == cousin:
                "Humiliated like never before, [the_person.title] quickly dresses back up and walks out of the club."
                $ the_person.change_stats(happiness = -10, obedience = 3, love = -5)
            else:
                "Unable to argue with you, [the_person.title] quickly dresses back up and leaves the club, still in tears."
            $ the_person.job.quit_function = stripper_quit
            $ the_person.quit_job()
            $ the_person.change_location(the_person.home)
            $ mc.location.show_background()
    return
