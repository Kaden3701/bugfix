## Stripclub storyline Mod by Corrado
#  Strippers role definition.
#  The role is appended to strippers after they start to work for you.
init 3 python:
    def calculate_stripper_salary(person):
        shifts = person.event_triggers_dict.get("strip_club_shifts", 2)
        tit_modifier = 10 - (__builtin__.abs(5 - Person.rank_tits(person.tits)))   # optimal size is DD-Cup
        age_modifier = 8 - (__builtin__.abs(25 - person.age) / 3.0)            # optimal age is 25
        slut_modifier = person.sluttiness / 20.0
        obed_modifier = 0
        if person.has_role(stripclub_bdsm_performer_role):
            obed_modifier = person.obedience / 20.0

        return __builtin__.round((person.charisma + tit_modifier + age_modifier + slut_modifier + obed_modifier) * shifts, 1)

    def calculate_stripper_profit(person):
        shifts = person.event_triggers_dict.get("strip_club_shifts", 2)
        profit_base = calculate_stripper_salary(person) * (renpy.random.random() + .8) # stripper income is variable
        if person.has_role(stripclub_waitress_role):
            profit_base = calculate_stripper_salary(person) * (renpy.random.random() + .6) # waitress income is variable

        tit_modifier = person.get_opinion_score("showing her tits") * 2
        ass_modifier = person.get_opinion_score("showing her ass") * 2

        return (profit_base + tit_modifier + ass_modifier + person.charisma) * shifts

    def is_strip_club_stripper_requirement(person):
        if person.is_strip_club_employee:
            return False
        if get_strip_club_foreclosed_stage() >= 5:
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            if person.has_role([stripper_role, stripclub_bdsm_performer_role, stripclub_waitress_role]):
                return True
        return False

    def strip_club_hire_employee_requirement(person):
        if person.is_strip_club_employee:
            return False
        if person in list(set(unique_character_list)-set([cousin, aunt, mom, lily, nora])): # disqualified from action
            return False
        if person in [mom, aunt]:   # special work around for mom and aunt (will block the wednesday night event)
            if not person.has_job([unemployed_job, aunt_unemployed_job]):
                return "Only when unemployed"
            return True
        if person.has_job_role(critical_job_role): # critical jobs require very high sluttiness
            if person.sluttiness < 80:
                return False
            if person.sluttiness < 100:
                return "Try at max sluttiness"
        if __builtin__.len(stripclub_strippers) >= 7 and (not strip_club_get_manager() or __builtin__.len(stripclub_waitresses) >= 2) and (not bdsm_room_available() or __builtin__.len(stripclub_bdsm_performers) >= 5):
            return "At maximum Strip Club employees"
        if day < person.event_triggers_dict.get("stripper_ask_hire", 0) + 3:
            return "Asked too recently"
        return True

    def strip_club_review_requirement(person):
        if not person.is_strip_club_employee:
            return False
        if get_strip_club_foreclosed_stage() >= 5 and person.has_role([stripper_role, stripclub_bdsm_performer_role, stripclub_waitress_role]):
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            if day - person.event_triggers_dict.get("stripclub_last_promotion_day", -7) < 7:
                return "Too recently promoted"
            if day - person.event_triggers_dict.get("day_last_performance_review", -7) < 7:
                return "Too recently reviewed"
            return True
        return False

    def add_strip_club_hire_employee_action_to_mc_actions():
        strip_club_hire_employee_action = Action("Employ at [strip_club.formal_name]", strip_club_hire_employee_requirement, "strip_club_hire_employee_label", menu_tooltip = "Hire [the_person.title] to work for you in your strip club.")
        mc.main_character_actions.append(strip_club_hire_employee_action)
        # change strippers jobs role
        for stripper in stripclub_strippers[:]: # use copy of existing array
            stripper.job.quit_function = stripper_quit # replace base game stripper job quit_function
            stripper.quit_job() # use quit job because the role names match
            stripper.change_job(stripclub_stripper_job, job_known = True)

    def allow_promote_to_manager_requirement(person):
        if get_strip_club_foreclosed_stage() < 5:
            return False
        if person.is_employee or person in [mom, lily, aunt, nora]:
            return False
        if not person.is_at_work:
            return False
        if person.has_role([stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role]) and not strip_club_get_manager():
            # if person.age < 25: # As requested from a lot of people to hire Gabrielle as manager
                # return "Requires: age >= 25"
            if person.int < 4 or person.charisma < 5:
                return "Requires: intelligence >= 4 and charisma >= 5"
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            if day - person.event_triggers_dict.get("stripclub_hire_day", -7) < 7:
                return "Too recently hired"
            return True
        return False

    def build_strip_club_hire_role_menu(person):
        available_roles = []
        if __builtin__.len(stripclub_strippers) < 7:
            available_roles.append(["Stripper", stripper_role])
        if strip_club_get_manager() and __builtin__.len(stripclub_waitresses) < 2:
            available_roles.append(["Waitress", stripclub_waitress_role])
        if bdsm_room_available() and __builtin__.len(stripclub_bdsm_performers) < 5:
            available_roles.append(["BDSM Performer", stripclub_bdsm_performer_role])

        available_roles.append(["Forget It", "None"])

        available_roles.insert(0, "Strip Club Role")
        return [available_roles]

    def hire_stripper(person, job):
        if not person in unique_character_list:
            person.set_override_schedule(None, the_times = [4]) # clear party schedule
        if person.is_employee or person in [lily, nora]:    # moonlighting
            person.event_triggers_dict["strip_club_shifts"] = 1
            person.set_schedule(job.job_location, the_times = [4])
            for role in job.job_roles:
                person.add_role(role)
                if role == stripclub_stripper_role:
                    stripclub_strippers.append(person)
                elif role == stripclub_waitress_role:
                    stripclub_waitresses.append(person)
                elif role == stripclub_bdsm_performer_role:
                    stripclub_bdsm_performers.append(person)
        else:
            person.event_triggers_dict["strip_club_shifts"] = 2
            person.change_job(job, job_known = True)

        salary = calculate_stripper_salary(person)
        if person.has_role(stripclub_waitress_role):
            salary *= .5
        if person.has_role(stripclub_bdsm_performer_role):
            salary *= 1.1
        person.stripper_salary = __builtin__.round(salary, 1)
        return

    def move_stripper(person, job):
        old_salary = person.stripper_salary
        if person.has_role(stripclub_waitress_role):
            old_salary *= 2

        if person.is_employee or person in [lily, aunt, mom, nora]:   # moonlighting
            for role in [stripclub_stripper_role, stripclub_bdsm_performer_role, stripclub_waitress_role]:
                person.remove_role(role)
            if person in stripclub_strippers:
                stripclub_strippers.remove(person)
            if person in stripclub_bdsm_performers:
                stripclub_bdsm_performers.remove(person)
            if person in stripclub_waitresses:
                stripclub_waitresses.remove(person)

            for role in job.job_roles:
                person.add_role(role)
                if role == stripclub_stripper_role:
                    stripclub_strippers.append(person)
                elif role == stripclub_waitress_role:
                    stripclub_waitresses.append(person)
                elif role == stripclub_bdsm_performer_role:
                    stripclub_bdsm_performers.append(person)
        else:
            person.change_job(job)

        if person.has_role(stripclub_bdsm_performer_role):
            old_salary *= 1.1
        person.stripper_salary = __builtin__.round(old_salary, 1)

    def fire_stripper(person):
        if person.is_employee or person in [lily, nora]:   # moonlighting
            person.set_schedule(person.home, the_times = [4])
            for role in [stripclub_stripper_role, stripclub_bdsm_performer_role, stripclub_waitress_role]:
                person.remove_role(role)
            if person in stripclub_strippers:
                stripclub_strippers.remove(person)
            if person in stripclub_bdsm_performers:
                stripclub_bdsm_performers.remove(person)
            if person in stripclub_waitresses:
                stripclub_waitresses.remove(person)
        else:
            person.quit_job()
        return

    def stripper_quit(person): # on_quit function called for strippers to make sure there's always someone working at the club. Also removes them from the list of dancers
        if person in stripclub_strippers:
            stripclub_strippers.remove(person)
        if person.has_role(stripper_role):  # extra check for removal of old stripper role
            person.remove_role(stripper_role)
        return

    promote_to_manager_action = Action("Appoint as Manager", allow_promote_to_manager_requirement, "promote_to_manager_label", menu_tooltip = "Appoint [the_person.title] as strip club manager.")
    strip_club_stripper_move_action = Action("Move to new role", is_strip_club_stripper_requirement, "strip_club_move_employee_label", menu_tooltip = "Move [the_person.title] to a different role within the strip club.")
    strip_club_stripper_fire_action = Action("Fire her", is_strip_club_stripper_requirement, "strip_club_fire_employee_label", menu_tooltip = "Fire [the_person.title] from her stripper job in your strip club.")
    strip_club_stripper_performance_review_action = Action("Review her performance", strip_club_review_requirement, "stripper_performance_review_label", menu_tooltip = "Review [the_person.title]'s performances on stage.")

    stripclub_stripper_role = Role("Stripper", get_stripper_role_actions() + [promote_to_manager_action, strip_club_stripper_move_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

label strip_club_hire_employee_label(the_person):
    mc.name "So [the_person.title], are you looking for a job?"
    $ ran_num = renpy.random.randint(0,100)
    if the_person is lily:
        the_person "Hey [the_person.mc_title], you know I'm always looking for ways to boost my pocket money, a student always has a shortage of money."
        mc.name "Then you might like the proposal I have for you."
    elif the_person is mom:
        the_person "Hi [the_person.mc_title], you know I have a lot of bills to pay, but I also have my job, so I'm not really looking for something else."
        mc.name "I think you are going to like this offer."
    elif the_person is aunt:
        the_person "Hello [the_person.mc_title], I'm so tired of sitting around at home all day, I wouldn't mind a little diversion."
        mc.name "Well, it's not exactly a daytime job, but the hours and pay are very good."
    elif the_person is cousin:
        the_person "After you fired me from the strip club I didn't find anything interesting... Do you have something in mind?"

        call screen main_choice_display(build_menu_items(build_strip_club_hire_role_menu(the_person)))
        if _return == "None":
            mc.name "I've changed my mind, we will talk about this another time."
            the_person "Ok, that's fine."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return

        $ ran_num = calculate_stripper_salary(the_person)

        if _return is stripper_role:
            mc.name "Actually I had a change of heart, how do you feel about coming back to work for me at the strip club?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person "Ok, but after what you did last time, the pay should be magnificent!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person "Really you will pay me that much? Ok, then my answer is yes, I'll work as a stripper again."
            $ hire_stripper(the_person, stripclub_stripper_job)

        elif _return is stripclub_bdsm_performer_role:
            mc.name "I did it just because I already knew I had a better offer for a girl like you. How do you feel about coming back to the strip club to work as a BDSM performer?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person "Maybe, but as a stripper I was getting good money, so if I do this, the pay should be a lot better!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that is 'a lot better' for you?"
            the_person "Really you will pay me that much? Ok, then my answer is yes, I'll do some kinky stuff for you."
            $ hire_stripper(the_person, stripclub_bdsm_performer_job)

        else:
            mc.name "I don't like the idea of you working as a stripper, but how do you feel about coming back to the strip club to work as a waitress?"
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            the_person "Ok, but as a stripper I was getting good money, so the pay should be as good!"
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person "Really you will pay me that much just to give people drinks and clean some tables? Ok, then my answer is yes."
            $ hire_stripper(the_person, stripclub_waitress_job)

        mc.name "See you at the club."
        return
    elif the_person.is_employee:
        if mc.business.is_open_for_business:
            the_person "What do you mean? I already have a job, right here, right now."
            mc.name "Don't worry, it won't interfere with this job, I just thought you might like to make something extra on the side."
        else:
            the_person "I don't understand, I already work for you. Or are you terminating my position?"
            mc.name "Of course not, you are a valuable employee, but I thought you might like to make some extra cash for just a few hours work, after hours."
    elif the_person.has_job(unemployed_job):
        the_person "I'm currently unemployed, so I'm open to any suggestions..."
    elif ran_num < 33: # Any other 33% chance Yes
        the_person "Actually yes, I would like to take a break from being a [the_person.job.job_title]... Do you have something available for me?"
    elif ran_num > 67: # Any other 33% chance No
        the_person "No [the_person.mc_title], I'm quite happy with my job as [the_person.job.job_title]."
        mc.name "Oh, that's good for you! If one day you change your mind, let me know."
        the_person "Sure, thank you!"
        $ the_person.event_triggers_dict["stripper_ask_hire"] = day
        return
    else: #  Any other (34% chance) Maybe
        the_person "Maybe, but not right now, I'm really busy at the moment, so there's not too many jobs I can do..."
        mc.name "Then my proposal will be perfect for you!"

    if mc.location == strip_club:
        mc.name "I own this strip club and I could see you working here..."
    else:
        mc.name "I own the [strip_club.formal_name] downtown, and I need some workers for the place..."

    the_person "Oh my God, really? You're proposing a job in your strip club? I don't know..."

    $ ran_num = calculate_stripper_salary(the_person)

    call screen main_choice_display(build_menu_items(build_strip_club_hire_role_menu(the_person)))
    if _return == "None":
        mc.name "I've changed my mind, we will talk about this another time."
        the_person "Ok, that's fine."
        $ the_person.event_triggers_dict["stripper_ask_hire"] = day
        return

    if _return is stripper_role:
        if the_person.has_role(prostitute_role):
            the_person "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person "Great, then I'll be a stripper for you."
        elif the_person.effective_sluttiness() > 70:
            the_person "I admit, I love turning men on, just making them horny while they ogle my body, mmm... Where should I sign?"
        elif the_person.effective_sluttiness() > 40 and the_person.get_opinion_score(["showing her ass","showing her tits"]) > 1:
            the_person "I admit, I always wanted to do something like that. Seducing men, with my body on full display, mmm... Where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score(["showing her ass", "showing her tits"]) > 3:
            the_person "Maybe, if the money is good enough, I could give it a try..."
            mc.name "Your pay will be $[ran_num] a day. Do you think that will be good enough for you?"
            the_person "Really you will pay me that much? Ok, then my answer is yes, I'll work as a stripper for you."
        else:
            the_person "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, showing so much skin..."
            "Maybe I can work on her sluttiness a bit, or change her attitude to 'showing some skin' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return
        $ hire_stripper(the_person, stripclub_stripper_job)

    elif _return is stripclub_bdsm_performer_role:
        mc.name "I was thinking you might like to perform in the BDSM room..."
        if the_person.has_role(prostitute_role):
            the_person "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person "Great, then I'll be your naughty girl on stage."
        elif the_person.effective_sluttiness() > 70:
            the_person "That sounds like something interesting... What do you think I should do?"
            mc.name "You're a beautiful, sexy and attractive girl, you'll be amazing on stage!"
            the_person "You are absolutely right, where should I sign?"
        elif the_person.effective_sluttiness() > 40 and the_person.get_opinion_score("being submissive") + the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 1:
            the_person "I don't know... I really don't know... What do you think I should do?"
            mc.name "You're a beautiful, sexy and attractive girl, you'll be amazing on stage!"
            the_person "Ok, your offer is really tempting, where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score("being submissive") + the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 4:
            the_person "Maybe, if the money is good enough, I could give it a try..."
            mc.name "Your pay will be $[ran_num] a day, is that good enough for you?"
            the_person "Oh! Your offer was tempting, and for that money I don't care about being a bit submissive and showing some skin. Ok then, my answer is yes."
        else:
            the_person "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, letting everyone know how slutty I am..."
            "Maybe I can work on her sluttiness a bit, or change her attitude to 'showing some skin' or 'being submissive' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return
        $ hire_stripper(the_person, stripclub_bdsm_performer_job)

    else:
        mc.name "I was thinking you might like to become a waitress..."
        if the_person.has_role(prostitute_role):
            the_person "Could I still turn tricks, when I like the guy?"
            mc.name "As long as you don't do it inside the club, you can do what ever you like."
            the_person "Great, then I'll be one of the best waitresses you will ever see."
        elif the_person.effective_sluttiness() > 50:
            the_person "I would love being a waitress, showing some skin, having them groping my ass... Ok, where should I sign?"
        elif the_person.effective_sluttiness() > 20 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 0:
            the_person "If it's just to be a waitress there, I don't mind showing some skin... Ok, where should I sign?"
        elif the_person.effective_sluttiness() > 10 and the_person.get_opinion_score("showing her ass") + the_person.get_opinion_score("showing her tits") > 2:
            the_person "Maybe, if the money is good enough, I could give it a try..."
            $ ran_num = calculate_stripper_salary(the_person) * .5
            mc.name "Your pay will be $[ran_num] a day, not bad for waiting some tables, right?"
            the_person "Oh! Ok, then my answer is yes, for that kind of money I don't mind running around in a short skirt waiting tables."
        else:
            the_person "I'm sorry [the_person.mc_title], I'm flattered you think I'm pretty enough for the job, but I don't think I would fit in there, showing so much skin..."
            "Maybe I can work on her sluttiness a bit, or I change her attribute to 'showing some skin' and try again."
            mc.name "Don't worry [the_person.title], if you change your mind, just let me know."
            $ the_person.event_triggers_dict["stripper_ask_hire"] = day
            return
        $ hire_stripper(the_person,stripclub_waitress_job)

    "You ask her to sign the standard contract and [the_person.title] now works for you in the [strip_club.formal_name]."

    the_person "Thank you for the opportunity [the_person.mc_title], I'll try my best!"
    return

label strip_club_move_employee_label(the_person):
    mc.name "[the_person.title], I want you to work in a different position."
    $ the_person.draw_person(emotion = "happy")
    if the_person.has_role(stripclub_bdsm_performer_role):
        the_person "Like this?"
        $ the_person.draw_person(position = "missionary", emotion = "happy")
        "[the_person.title] sits on the stage and spreads her legs wide"
        $ mc.change_locked_clarity(5)
        mc.name "Not quite. A different job position."
    else:
        the_person "What did you have in mind?"

    call screen main_choice_display(build_menu_items(build_strip_club_hire_role_menu(the_person)))

    if _return is stripper_role:
        mc.name "I want you to work on our main stage, stripping for all of customers."
        if the_person.has_role(stripper_role):
            the_person "Don't I already do that?"
            mc.name "Oh, you do? My mistake."
            $ the_person.change_stats(love = -1)
            return
        if the_person.has_role(stripclub_waitress_role):
            mc.name "It comes with a major pay bump."
        else:
            mc.name "Don't worry, there's no pay decrease."
        the_person "Alright. I'll be on the stage next shift."
        $ move_stripper(the_person, stripclub_stripper_job)
    elif _return is stripclub_waitress_role:
        mc.name "I want you to work on the floor, serving drinks to the customers."
        if the_person.has_role(stripclub_waitress_role):
            the_person "Don't I already do that?"
            mc.name "Oh, you do? My mistake."
            $ the_person.change_stats(love = -1)
            return
        mc.name "Don't worry, there's no pay decrease."
        the_person "Alright. I'll report to the bar next shift."
        $ move_stripper(the_person, stripclub_waitress_job)
    elif _return is stripclub_bdsm_performer_role:
        mc.name "I want you in the back, performing BDSM shows"
        if the_person.has_role(stripclub_bdsm_performer_role):
            the_person "Don't I already do that?"
            mc.name "Oh, you do? My mistake."
            $ the_person.change_stats(love = -1)
            return
        if the_person.has_role(stripclub_waitress_role):
            mc.name "It comes with a major pay bump."
        else:
            mc.name "It comes with a minor pay bump."
        the_person "Alright. Next shift, I'll be back there."
        $ move_stripper(the_person, stripclub_bdsm_performer_job)
    else:
        mc.name "On second thought, I like you exactly where you are."
    return

label strip_club_fire_employee_label(the_person):
    if the_person.has_role(stripper_role) or the_person.has_role(stripclub_waitress_role):
        mc.name "[the_person.title], I've checked your performance on stage and it is absolutely unsatisfactory."
        mc.name "There's no a nice way to say this, but you're fired, you can finish your shift tonight and collect your severance pay."
        $ the_person.draw_person(emotion = "happy", position = "stand3")
        the_person "Are you sure [the_person.mc_title]? There's nothing I can do to make you change your mind?"
        "She place a hand on your crotch and start to move it gently, with a clear innuendo."
    else: # bdsm performer
        mc.name "[the_person.title], I've checked your performances here, your Master is really disappointed."
        mc.name "There's not a nice way to say this, but you're fired, you can finish your shift tonight and collect your severance pay."
        $ the_person.draw_person(position = "kneeling1", emotion = "sad")
        the_person "Are you sure Master? There's nothing your pet here can do to make you change your mind?"
        "She places her cheek on your leg as a good pet, waiting for a caress from her Master."

    menu:
        "Accept the advances":
            mc.name "Alright [the_person.title], you've got me interested, try to convince me."
            $ the_person.add_situational_slut("seduction_approach", -5, "I'm just a toy for him.")
            $ the_person.add_situational_obedience("seduction_approach", 25, "I'll do what I need to keep my job!")
            call fuck_person(the_person, private = True) from _call_fuck_person_strip_club_fire_employee_label
            $ the_person.clear_situational_slut("seduction_approach")
            $ the_person.clear_situational_obedience("seduction_approach")
            $ the_person.apply_planned_outfit()
            $ the_person.change_stats(happiness = -5, obedience = 5, slut = 1, max_slut = 60)
            mc.name "Okay [the_person.title], I'll keep you around for a little while longer, but you really need to work on your act, I'm not running a charity."
            if the_person.effective_sluttiness() < 50:
                the_person "I'll do my best [the_person.mc_title], I promise."
            else:
                the_person "It's tempting just to be fucked like this again..."
            return
        "Refuse":
            mc.name "I'm sorry [the_person.title], but sex won't make me change my mind..."
            $ the_person.draw_person(emotion = "sad", position = "stand3")
            the_person "Damn... Ok, I will clear out my locker at the end of my shift."
            $ the_person.change_stats(happiness = -10, obedience = -5, love = -5)
            $ fire_stripper(the_person)
    return

label stripper_performance_review_label(the_person):
    $ the_person.event_triggers_dict["day_last_performance_review"] = day
    mc.name "[the_person.title], I'd like to have a talk with you about your recent performance here at the club. Can you follow me to my office?"
    if the_person.obedience > 100:
        the_person "Oh, of course [the_person.mc_title]."
    else:
        the_person "Uh, I guess. so."

    "You lead [the_person.title] to your office at the strip club and close the door behind her, asking her to sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "So [the_person.title], tell me what you think about your job."
    if the_person.job_happiness_score > 0: # She's happy enough with the job to stay here
        if the_person.stripper_salary > the_person.calculate_base_salary() + 20: # She get a lot of money as stripper in comparison with a 'regular' job
            the_person "It's a fantastic job and I'm lucky to have it! There aren't very many places that would be able to pay me as well as I am here."
        elif the_person.stripper_salary > the_person.calculate_base_salary() + 5: # She get some money more as stripper in comparison with a 'regular' job
            the_person "It's a great job. The pay is great and the work is 'stimulating'."
        elif the_person.stripper_salary > the_person.calculate_base_salary() - 5: # She get the same money as stripper in comparison with a 'regular' job
            the_person "I really like my job, every day I feel like I can come in and do an honest day's work."
        else: # She get less money as stripper in comparison with a 'regular' job
            the_person "The pay isn't the greatest, but I really enjoy working here."
    else: #She's thinking about quitting.
        if the_person.stripper_salary > the_person.calculate_base_salary() + 20: #She's very overpaid# She get a lot of money as stripper in comparison with a 'regular' job
            the_person "The pay is amazing, but the work environment here is just terrible. I honestly don't know how much longer I can take it."
        elif the_person.stripper_salary > the_person.calculate_base_salary() + 5: # She get some money more as stripper in comparison with a 'regular' job
            the_person "I know you're paying me very well, but the work here is terrible. I hope you have some plans to make things better."
        elif the_person.stripper_salary > the_person.calculate_base_salary() - 5: # She get the same money as stripper in comparison with a 'regular' job
            the_person "Things could be better. I'd like it if my conditions to work here were improved a little, or I could be paid a little bit more."
        else: # She get less money as stripper in comparison with a 'regular' job
            the_person "I don't really have anything positive to say. The pay isn't great and it isn't exactly the most pleasant work environment."
    "You nod and take some notes while you think of how you want to respond."
    $ ran_num = calculate_stripper_salary(the_person)
    if ran_num > the_person.stripper_salary:
        "Her actual salary is $[the_person.stripper_salary], but for her current performance level it should be $[ran_num], what will you do?"
    else:
        "Her current performance level does not warrant a raise of her salary, what will you do?"

    menu:
        "Reward her for work well done":
            $ raise_amount = __builtin__.round(the_person.stripper_salary * 0.1)
            menu:
                "Give her a 10%% raise\n{color=#ff0000}{size=18}Costs: $[raise_amount] / day{/size}{/color}": #Pay her more money. Large happiness and obedience raise.
                    mc.name "I've been very impressed by your work lately, and I'd like to make sure you stay happy with your decision to work here."
                    mc.name "I'm going to put you down for a 10%% raise. How does that sound?"
                    $ the_person.stripper_salary += raise_amount
                    $ the_person.change_stats(happiness = 1 + mc.charisma, obedience = 1 + mc.charisma)
                    $ the_person.draw_person(position = "sitting", emotion = "happy")
                    the_person "That sounds amazing! Thank you sir, I promise I won't let you down!"
                    mc.name "Good to hear it."
                "Reward her sexually" if the_person.effective_sluttiness() >= 40: #At high sluttiness you can make her cum to make her even happier with her job.
                    mc.name "You do a lot of work here in the club, and I know how stressful your job can be at times."
                    "You get up, step behind [the_person.title] and place your hands on her shoulders, rubbing them gently."
                    mc.name "I'd like to do something for you to help you relax. How does that sound for a bonus?"
                    $ the_person.add_situational_slut("seduction_approach", 15, "It's all about me!")
                    $ the_person.add_situational_obedience("seduction_approach", -10, "It's all about me!")
                    the_person "Oh [the_person.mc_title], that sounds like a great idea..."
                    call fuck_person(the_person, private = True) from _call_fuck_stripper_performance_review_1
                    $ the_report = _return
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    if the_report.get("girl orgasms", 0) > 1: #We made her cum multiple times! Congratulations!
                        $ the_person.change_stats(happiness = 10, slut = 1, max_slut = 60)
                        the_person "Oh [the_person.mc_title], that was wonderful! I couldn't have asked for a better performance bonus!"
                    elif the_report.get("girl orgasms", 0) == 1:
                        $ the_person.change_stats(happiness = 5, slut = 1, max_slut = 50)
                        the_person "Well, that was a good time [the_person.mc_title]. It's a lot more fun than a normal performance bonus, that's for sure!"
                    else:
                        $ the_person.change_stats(happiness = -5, obedience = -2)
                        the_person "It's not much of a bonus if you're the only one who gets to cum. Maybe next time a cash bonus would be better, okay?"
                    $ the_person.apply_planned_outfit()

        "Punish her for poor performance":
            $ cut_amount = __builtin__.round(the_person.salary * 0.1)
            menu:
                "Cut her pay by 10%%\n{color=#00ff00}{size=18}Profit: $[cut_amount] / day{/size}{/color}": #Pay her less. Large happiness and obedience drop.
                    mc.name "I'm really sorry to do this [the_person.title], but your performance lately just doesn't justify what I'm paying you."
                    mc.name "I'm going to have to cut your pay by 10%%."
                    $ the_person.change_salary(-cut_amount)
                    $ the_person.change_stats(happiness = -10 - mc.charisma, obedience = -5 - mc.charisma)
                    if the_person.job_happiness_score > 0:
                        $ the_person.draw_person(position = "sitting", emotion = "sad")
                        the_person "I... I understand."
                    elif the_person.job_happiness_score > -25:
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person "What? I... I don't know what to say!"
                        mc.name "Like I said, I'm sorry, but it has to be done."
                    else: #She's so unhappy with her job she quits.
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person "What? I... I can't believe that [the_person.mc_title], why would you ever think I would stay here for less money?"
                        mc.name "Like I said, I'm sorry, but it has to be done."
                        the_person "Well you know what, I think I'm just going to find somewhere else to work. I quit."
                        $ clear_scene()
                        "[the_person.title] stands up and storms out of the room."
                        $ the_person.change_stats(happiness = -25, obedience = -15, love = -30)
                        $ fire_stripper(the_person)
                        $ the_person.change_location(the_person.home)
                        return
                "Threaten to fire her": #She may ask to stay in exchange for some sort of favour, or get fired on the spot.
                    mc.name "I'll be honest with you [the_person.title], your performance here at the club leaves a lot to be desired."
                    mc.name "I've been running the numbers and I think, unless you can convince me otherwise, we'd be better off without you."
                    if the_person.job_happiness_score > -10:
                        if the_person.effective_sluttiness() < 30:
                            the_person "No sir, I really need this job. What if I took a pay cut? Would that be enough?"
                            menu:
                                "Cut her pay\n{color=#00ff00}{size=18}Profit: $[cut_amount] / day{/size}{/color}":
                                    mc.name "If you're willing to take a pay cut I think I can keep you around and see if your performance improves."
                                    $ the_person.stripper_salary += -cut_amount
                                    $ the_person.change_stats(happiness = 10, obedience = 5)
                                    the_person "Thank you sir! Thank you so much!"
                                "Fire her":
                                    mc.name "I'm sorry, but that wouldn't be enough."
                                    the_person "I understand. I'll clear out my locker at the end of my shift."
                                    $ the_person.change_stats(happiness = -10, obedience = -5)
                                    $ fire_stripper(the_person)
                        else:
                            the_person "Wait, I really need this job... What if I... let you use me. Just so you'll keep me around."
                            menu:
                                "Fuck her":
                                    $ the_person.add_situational_slut("seduction_approach", -5, "I'm just a toy to him.")
                                    $ the_person.add_situational_obedience("seduction_approach", 25, "I'll do what I need to keep my job!")
                                    mc.name "Alright, you've got me interested. Let's see what you can do."
                                    call fuck_person(the_person,private = True) from _call_fuck_stripper_performance_review_2
                                    $ the_person.clear_situational_slut("seduction_approach")
                                    $ the_person.clear_situational_obedience("seduction_approach")
                                    $ the_person.apply_planned_outfit()
                                    $ the_person.change_stats(happiness = -5, obedience = 5, slut = 1, max_slut = 50)
                                    mc.name "Okay [the_person.title], I'll keep you around for a little while longer, but you're going to need to work on your act, or else I might change my mind about keeping you here."
                                    if the_person.effective_sluttiness() < 50:
                                        the_person "I'll do my best [the_person.mc_title], I promise."
                                    else:
                                        the_person "It's tempting just to be fucked like this again..."
                                "Fire her":
                                    mc.name "I'm sorry, but that wouldn't be enough."
                                    the_person "I understand. I'll clear out my locker at the end of the shift."
                                    $ the_person.change_stats(happiness = -15, obedience = -10, love = -10)
                                    $ fire_stripper(the_person)
                                    return
                    else:
                        $ the_person.draw_person(position = "sitting", emotion = "angry")
                        the_person "What? You want me to beg to stay at this shitty job? If you don't want me here I think it's best I just move on. I quit!"
                        $ clear_scene()
                        "[the_person.title] stands up and storms out."
                        $ the_person.change_stats(happiness = -15, obedience = -10, love = -10)
                        $ fire_stripper(the_person)
                        return
                "Punish her sexually" if the_person.effective_sluttiness() >= 40 and the_person.obedience >= 120: #Orgasm denial and/or make her service you.
                    "You sigh dramatically, stand up and walk over to [the_person.title]."
                    mc.name "Your performance has really let me down, but I think what you need is a little motivation."
                    mc.name "I want to have some fun with you, but you're not allowed to climax, is that understood?"
                    $ opinion_modifier = the_person.get_opinion_score("being submissive") * 5
                    $ the_person.add_situational_slut("seduction_approach", -5+opinion_modifier, "I'm just being used...")
                    $ the_person.add_situational_obedience("seduction_approach", 15+opinion_modifier, "I'm being punished")
                    the_person "I... if you think this is what I need, sir."
                    call fuck_person(the_person, private = True) from _call_fuck_person_stripper_performance_review_3
                    $ the_report = _return
                    $ the_person.clear_situational_slut("seduction_approach")
                    $ the_person.clear_situational_obedience("seduction_approach")
                    if the_report.get("girl orgasms", 0) > 0: #We made her cum! Congratulations!
                        $ the_person.change_stats(happiness = 5, slut = 1, max_slut = 50)
                        the_person "You just can't resist pleasing me, can you [the_person.mc_title]? I thought I wasn't supposed to cum?"
                        "[the_person.title] seems smug about her orgasmic victory."
                    elif the_report.get("end arousal", 0) >= 80:
                        $ the_person.change_stats(happiness = 5, slut = 1, max_slut = 60)
                        the_person "Oh my god [the_person.mc_title], you got me so close... Can't you just finish me off, real quick?"
                        mc.name "Do a better job and I'll let you cum next time, understood?"
                        "[the_person.title] nods meekly."
                    else:
                        $ the_person.change_stats(happiness = -5, obedience = 3)
                        mc.name "That felt great [the_person.title], I suppose if your performance doesn't improve you'll still be useful as a toy."
                        the_person "I... Yes sir, I suppose I would be."
                    $ the_person.apply_planned_outfit()
        "Finish the performance review":
            mc.name "Well, I think you're doing a perfectly adequate job around here [the_person.title]. If you keep up the good work I don't think we will have any issues."
            $ the_person.change_stats(happiness = 2, obedience = 1)
            the_person "Thank you, I'll do my best."
    "You stand up and open the door for [the_person.title] at the end of her performance review."
    $ clear_scene()
    return
