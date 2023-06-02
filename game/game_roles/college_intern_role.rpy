init 1 python:
    def college_intern_days(the_person):
        if not the_person.has_role(college_intern_role):
            return -1
        return (day - person.event_triggers_dict.get("intern_since", 9999))

    def college_intern_on_turn(the_person):
        for duty in the_person.duties:
            if the_person.is_at_work or not duty.only_at_work:
                duty.on_turn(the_person)

        if the_person.is_at_work:
            the_person.event_triggers_dict["worked_today"] = True
        return

    def college_intern_on_day(the_person):  #Use this to figure out when to end the internship
        for duty in the_person.duties:
            if the_person.event_triggers_dict.get("worked_today", False) or not duty.only_at_work: #Only perform on_day functions if they had work that day.
                duty.on_day(the_person)

        the_person.event_triggers_dict["worked_today"] = False #Reset this for the next day.
        return

    def college_intern_on_move(the_person):
        pass
        return

    def college_intern_happiness_score(the_person):
        happiness_score = the_person.happiness - 100
        happiness_score += the_person.sluttiness
        happiness_score += (the_person.obedience - 95)
        happiness_score += the_person.calculate_base_salary()   #She is happier if you actively developed her skills
        return happiness_score

    def hire_new_college_intern_requirement(the_person):
        if not mc.business.has_funds(15000):
            return "$15000 scholarship fund"
        if len(mc.business.get_intern_depts_with_openings()) > 0:
            return True
        else:
            return "No internship openings"
        return False

    def college_intern_training_requirement(the_person):
        return False # disabled until written
        #return the_person.is_at_work and not the_person.location == university

    def college_intern_set_duties_requirement(the_person):
        if not the_person.is_at_work or the_person.location == university:
            return "Only in the office"

        if the_person.event_triggers_dict.get("work_duties_last_set", -1) < day:
            return True
        return "Duties already changed today"

    def get_intern_candidates(count, stat_array, skill_array, required_opinions):
        candidates = []

        for x in range(0,count):
            candidates.append(make_person(age = renpy.random.randint(19, 22), stat_array = stat_array, skill_array = skill_array, job = student_job, force_random = True))

        for candidate in candidates:
            for opinion in required_opinions:
                candidate.set_opinion(opinion[0], opinion[1], opinion[2])

            for x in __builtin__.range(0,2): #Reveal all of their opinions based on our policies.
                candidate.discover_opinion(candidate.get_random_opinion(include_known = False, include_sexy = False),add_to_log = False) #Get a random opinion and reveal it.
        return candidates

    def college_intern_quit(person):
        mc.business.undesignate_person(person)
        person.remove_role(college_intern_role)
        person.change_job(student_job)
        person.set_override_schedule(None, the_days = [5,6], the_times = [1,2])
        return

    def college_intern_hire(person):
        if person.event_triggers_dict.get("intern_since", -1) == -1:
            person.event_triggers_dict["intern_since"] = day
            mc.business.listener_system.fire_event("new_intern", the_person = person)
        return

    def college_intern_unlock_recruit_supply_requirement(the_person):
        if not mc.business.college_interns_unlocked:
            return False
        return day > erica.event_triggers_dict.get("team_reinstate_day", 9999) + 14

    def setup_college_intern_supply_unlock():
        college_intern_recruit_supply_unlock = Action("Unlock recruit Supply Interns", college_intern_unlock_recruit_supply_requirement, "college_intern_unlock_recruit_supply_label")
        nora.add_unique_on_room_enter_event(college_intern_recruit_supply_unlock)
        return

init 2 python:
    college_intern_training = Action("Train your intern", college_intern_training_requirement, "college_intern_training_label")   #TODO tooltip
    college_intern_duty_set_action = Action("Set her work duties", college_intern_set_duties_requirement, "employee_set_duties_label", menu_tooltip = "Review and set her work duties.")

label unlock_college_interns():
    python:
        mc.business.college_interns_unlocked = True
        hire_new_college_intern = Action("Hire new intern {image=gui/heart/Time_Advance.png}", hire_new_college_intern_requirement, "hire_new_college_intern_label")
        nora.get_role_reference(nora_role).add_action(hire_new_college_intern)
    return

label hire_new_college_intern_label(the_person):
    $ the_person = nora
    $ the_dept = ""
    $ skill_array = []
    $ stat_array = []
    "You walk around the university campus a bit. You decide to look into hiring a new college intern for your business."
    "You track down [the_person.title]."
    $ the_person.draw_person()
    the_person "Hello [the_person.mc_title]. What can I do for you today?"
    mc.name "I'm interested in providing a scholarship for another intern."
    the_person "Oh? Are you able to write a check for the full amount today?"
    the_person "Okay. What major are you looking for an intern from?"
    menu:
        "Biology (Research)" if len(mc.business.college_interns_research) < mc.business.max_interns_by_division:
            $ the_dept = "Research"
            $ stat_array = [1,3,2]  #Interns start with extremely basic stats, but can be trained.
            $ skill_array = [1,1,2,1,1]
            $ required_opinions = [["research work", renpy.random.randint(1, 2), True]]
        "Biology \n{color=#ff0000}{size=18}Research Team Full!{/size}{/color} (disabled)" if len(mc.business.college_interns_research) >= mc.business.max_interns_by_division:
            pass
        "Chemistry (Production)" if len(mc.business.college_interns_production) < mc.business.max_interns_by_division:
            $ the_dept = "Production"
            $ stat_array = [1,3,3]
            $ skill_array = [1,1,1,2,1]
            $ required_opinions = [["production work", renpy.random.randint(1, 2), True]]
        "Chemistry \n{color=#ff0000}{size=18}Production Team Full!{/size}{/color} (disabled)" if len(mc.business.college_interns_production) >= mc.business.max_interns_by_division:
            pass
        "Graphic Design (Marketing)" if len(mc.business.college_interns_market) < mc.business.max_interns_by_division and mc.business.college_market_interns_unlocked:
            $ the_dept = "Marketing"
            $ stat_array = [3,1,2]
            $ skill_array = [1,2,1,1,1]
            $ required_opinions = [["marketing work", renpy.random.randint(1, 2), True]]
        "Graphic Design (Marketing) (disabled)":    #In the future we may have opportunities to recruit interns for these programs.
            pass
        "Psychology (HR)" if len(mc.business.college_interns_HR) < mc.business.max_interns_by_division and mc.business.college_hr_interns_unlocked:
            $ the_dept = "HR"
            $ stat_array = [3,2,1]
            $ skill_array = [2,1,1,1,1]
            $ required_opinions = [["HR work", renpy.random.randint(1, 2), True]]
        "Psychology (HR) (disabled)":
            pass
        "Business (Supply)" if len(mc.business.college_interns_supply) < mc.business.max_interns_by_division and mc.business.college_supply_interns_unlocked:
            $ the_dept = "Supply"
            $ stat_array = [2,1,3]
            $ skill_array = [1,1,1,1,2]
            $ required_opinions = [["supply work", renpy.random.randint(1, 2), True]]
        "Business (Supply) (disabled)":
            pass
        "Never mind":
            mc.name "Actually, I just realized I can't bring on someone right now."
            the_person "I see, well let me know if you change your mind."
            return
    the_person "OK. Here's my list of candidates from that program."
    the_person "These are all girls who are doing good academically, are starting their final semester, and have applied for the scholarship."

    $ clear_scene()
    $ candidates = get_intern_candidates(3, stat_array, skill_array, required_opinions)

    # pad with extra element to make sure we can reach all candidates
    call hire_select_process(candidates + [1]) from _call_intern_select_process_01
    $ candidates = [] #Prevent it from using up extra memory
    $ required_opinions = None
    $ clean_memory() #Try and force a clean up of unused memory.

    if isinstance(_return, Person):
        $ new_person = _return
        $ new_person.generate_home() #Generate them a home location so they have somewhere to go at night.
        $ mc.business.hire_college_intern(new_person, the_dept, add_to_location = True)
        $ new_person.set_title(new_person.get_random_title())
        $ new_person.set_possessive_title(new_person.get_random_possessive_title())
        $ new_person.set_mc_title(new_person.get_random_player_title())
        $ new_person = None
        the_person "I'll pass this along to her. I'm sure she will be excited! Expect to see her on Saturday."
        mc.name "Thank you [the_person.title]."
        $ mc.business.change_funds(-15000)
    else:
        "You decide against hiring any new interns for now."
    call advance_time from _call_advance_time_after_intern_screen_01
    return


label college_intern_complete_internship(the_person):
    "As you are going about your day, you get a phone call. It's from [the_person.title], one of your college interns."
    the_person "Hey [the_person.mc_title]. Guess what! I graduated today!"
    mc.name "Congratulations! I suppose that means you won't be participating in the scholarship internship anymore."
    the_person "Yeah... that's true..."
    if college_intern_happiness_score(the_person) > 200:    #She begs to keep working for you.
        the_person "Listen... I know that I graduated, but, I was wondering something. I've learned so much working for you."
        if the_person.sluttiness > 40:
            the_person "And working for you has provided so many other, shall we say, benefits?"
        else:
            the_person "And you've been so good to me."
        the_person "Would you be willing to hire me? I've honestly been dreading this day a little bit."
        the_person "I'll be the ideal employee for you, I promise! I'll do anything... you don't even have to put me in the same department if you don't have room there..."
        "Sounds like she really wants you to keep her around."
        # CHeck to see if we have any employee spots.
        "You think about her progress and decide..."
        call hire_select_process([the_person, 1]) from _call_hire_intern_work_select_process_01
        if _return == the_person:
            mc.name "Alright [the_person.title]. I can't give you any preferential treatment, but we will give it a shot."
            $ the_person.change_stats(happiness = 5, love = 2)
            the_person "Oh my! Thank you so much! I'll see you at work sir!"
            "You use your phone and text HR to get her paperwork started to change her from intern to full employee status. You should probably decide what department she goes to."
            call hire_someone(the_person) from _call_hire_intern_work__01
        else:
            mc.name "I'm sorry, but I can't do that right now, the logistics aren't good for a new full time employee."
            $ the_person.change_stats(happiness = -5, love = -2)
            the_person "Ah... I understand. Well, if you change your mind, please let me know, okay?"
            "She hangs up before you can respond. It's unfortunate, but not every intern can transition to a full employee."
    elif college_intern_happiness_score(the_person) > 100:  #She wants to keep working for you
        the_person "I have to admit, I really enjoyed working for you. I was wondering, would you consider hiring me full time?"
        the_person "I know I'm young, and not very experienced, but I can make up for it with enthusiasm, and I learn quick!"
        "Sounds like she wants you to keep her around."
        # CHeck to see if we have any employee spots.
        "You think about her progress and decide..."
        call hire_select_process([the_person, 1]) from _call_hire_intern_work_select_process_02
        if _return == the_person:
            mc.name "Alright [the_person.title]. I can't give you any preferential treatment, but we will give it a shot."
            $ the_person.change_stats(happiness = 5, love = 2)
            the_person "Ah, I was hoping you would say that! I appreciate it sir!"
            "You use your phone and text HR to get her paperwork started to change her from intern to full employee status. You should probably decide what department she goes to."
            call hire_someone(the_person) from _call_hire_intern_work__02
        else:
            mc.name "I'm sorry, but I can't do that right now, the logistics aren't good for a new full time employee."
            $ the_person.change_stats(happiness = -5, love = -2)
            the_person "Ah... I understand. Well, if you change your mind, please let me know, okay?"
            "She hangs up before you can respond. It's unfortunate, but not every intern can transition to a full employee."
    elif college_intern_happiness_score(the_person) > renpy.random.randint(1,100):  #She might ask to stay on
        the_person "I've been thinking about this a lot, and I keep going back and forth on it. But before I start putting in applications elsewhere, I was wondering something."
        the_person "Would you consider hiring me on full time? I know it's a lot to ask, and if the answer is no that's okay."
        the_person "But the scholarship really helped me out, and I know my way around the business already."
        "Sounds like she wants you to keep her around."
        # CHeck to see if we have any employee spots.
        "You think about her progress and decide..."
        call hire_select_process([the_person, 1]) from _call_hire_intern_work_select_process_03
        if _return == the_person:
            mc.name "Alright [the_person.title]. I can't give you any preferential treatment, but I'll hire you full time."
            $ the_person.change_happiness(5)
            the_person "Okay, that certainly makes things simpler for me! I'll see you at the office then."
            "You use your phone and text HR to get her paperwork started to change her from intern to full employee status. You should probably decide what department she goes to."
            call hire_someone(the_person) from _call_hire_intern_work__03
        else:
            mc.name "I'm sorry, but I can't do that right now, the logistics aren't good for a new full time employee."
            the_person "That's okay. I appreciate the experience I got while I was there. Take care, [the_person.mc_title]."
            "You say goodbye to her. You aren't sure if you'll see her around again or not."    #TODO delete person?
    else:#She doesn't want to work for you
        the_person "I don't think I could work there full time, but I appreciate the opportunity to come and learn from you."
        the_person "The scholarship really helped me get through my final round of classes also."
        mc.name "That's good to hear. Take care now."
        the_person "Take care [the_person.mc_title]."
        "You say goodbye to her. You aren't sure if you'll see her around again or not."    #TODO delete person?
    $ mc.business.remove_college_intern(the_person)


    return

label college_intern_training_label(the_person):
    "This is going to be a menu where you can train your intern, but it has not yet been created."
    return

label college_intern_unlock_recruit_supply_label(the_person):
    if mc.business.college_supply_interns_unlocked:
        return False
    $ the_person.draw_person()
    the_person "Oh! [the_person.possessive_title], I was hoping to see you soon."
    mc.name "That's nice to hear."
    the_person "Yeah, it is about your internship program."
    the_person "I was talking with the new track coach a couple of days ago, and he was lamenting the lack of scholarships being offered to female student athletes."
    the_person "He said that a lot of the girls are here to just play their sport, and just getting basic degrees in business."
    the_person "I didn't think much of it at the time, but then I realized they might be interested in something like your scholarship program."
    mc.name "Hmm, business degrees? I'm not sure I could find something for them to do."
    the_person "It doesn't have to be anything advanced, even just menial logistics work, but that would give them some experience in day to day business operations."
    "Hmm... maybe you could start hiring interns to work in your supply department?"
    mc.name "Actually, I have something I could probably have them do."
    the_person "Excellent! I'll let the coach know and have him forward me information on anyone who might qualify. Just let me know when you want to set it up!"
    "You can now recruit Business major interns for your supply department!"
    $ mc.business.college_supply_interns_unlocked = True
    return
