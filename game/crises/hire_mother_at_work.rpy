## Hire Mother Crisis Mod by Tristimdorion
# Original idea by Corrado

init 2 python:
    def hire_mother_work_crisis_requirement():
        # Requires you to have an employee under a certain age, with a mother, who hasn't been introduced to the game yet.
        # Requires you and her to be at work.
        # Requires you to have a free slot in the company
        if mc.is_at_work and mc.business.employee_count < mc.business.max_employee_count:
            return not hire_mother_work_crisis_get_daughter() is None
        return False

    def hire_mother_work_crisis_get_daughter():
        valid_people_list = []
        if mc.business.is_open_for_business:
            for person in [x for x in mc.business.employee_list if x.age < 34 and not x.has_role(clone_role) and not side_character_is_unavail(x) and x not in unique_character_list]:
                if town_relationships.get_existing_parent_count(person) == 0: #The mother for this character is not yet in the game
                    valid_people_list.append(person)
        if mc.business.is_open_for_internship:
            for person in [x for x in mc.business.intern_list if x.age < 34 and not x.has_role(clone_role) and not side_character_is_unavail(x) and x not in unique_character_list]:
                if town_relationships.get_existing_parent_count(person) == 0: #The mother for this character is not yet in the game
                    valid_people_list.append(person)
        return get_random_from_list(valid_people_list) #Pick someone appropriate from the company.

    hire_mother_work_crisis = ActionMod("Mother Work Crisis", hire_mother_work_crisis_requirement,"hire_mother_work_crisis_label",
        menu_tooltip = "Allow you to hire the mothers of girls working for you.", category = "Business", is_crisis = True)

label hire_mother_work_crisis_label():
    if mc.business.employee_count >= mc.business.max_employee_count:
        return #The business is full due to some other crisis triggering this time chunk.

    $ the_person = hire_mother_work_crisis_get_daughter()
    if the_person is None:
        return #We couldn't find anyone to be a daughter, so the event fails.

    $ in_private = False
    $ the_person.draw_person()
    the_person "[the_person.mc_title], could I talk to you for a moment in your office?"
    mc.name "Of course. What's up?"
    $ mc.change_location(ceo_office)
    "You and [the_person.possessive_title] step into your office. You sit down at your desk while she closes the door."
    $ ran_num = renpy.random.randint(0,2)
    if ran_num == 0:
        the_person "I wanted to ask you... My mother is bored from sitting home all day and asked me to help her find a job."
        the_person "I promise she would be a very hard worker, and I'd keep a close eye on her."
    elif ran_num == 1:
        the_person "This is embarrassing to ask, but... my mother was let go from her job last week."
        the_person "It would mean the world to me if you would look at this and at least consider it."
    else: # ran_num == 2
        the_person "I wanted to ask you... Well, my mother just got divorced and moved in with me, she badly needs a job to get her life back on track."
        the_person "I was thinking that she might be a good fit for the company. I can tell you she's very smart."
        $ in_private = True # she will be living with the daughter

    $ promised_sex = False
    if the_person.sluttiness > 70:
        "[the_person.title] hands over a printed out resume and leans forward onto your desk, bringing her breasts closer to you."
        the_person "If you did hire her, I would be so very thankful. I'm sure we could find some way for me to show you how thankful."
        $ promised_sex = True

    else:
        "[the_person.title] hands over a printed out resume and waits nervously for you to look it over."

    menu:
        "Look at the resume for [the_person.fname]'s mother":
            pass

        "Tell her you aren't hiring":
            "You hand the resume back."
            mc.name "I'm sorry, but I'm not looking to hire anyone right now."
            if the_person.effective_sluttiness() > 50 and not promised_sex:
                the_person "Wait, please [the_person.mc_title], at least take a look. Maybe I could... convince you to consider her?"
                the_person "She means the world to me, and I would do anything for her. Anything at all."
                "She puts her arms behind her back and puffs out her chest in a clear attempt to show off her tits."
                $ mc.change_locked_clarity(5)
                menu:
                    "Look at the resume for [the_person.fname]'s mother":
                        "Convinced, you start to read through the resume."
                        $ promised_sex = True

                    "Tell her you aren't hiring":
                        if the_person.love < 10:
                            mc.name "If I wanted to fuck you I wouldn't need to hire your mother to do it. Give it up, you look desperate."
                            $ the_person.change_obedience(3)
                            "She steps back and looks away."
                            $ the_person.draw_person(emotion = "sad")
                            the_person "Uh, right. Sorry for taking up your time."
                            "[the_person.possessive_title] hurries out of your office."
                        else:
                            mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                            $ the_person.change_obedience(1)
                            "She takes the resume back and steps away from your desk, defeated."
                            $ the_person.draw_person(emotion = "sad")
                            the_person "Right, of course. Sorry for wasting your time."
                        $ clear_scene()
                        return
            elif promised_sex:
                the_person "There's nothing I could do? Nothing at all?"
                "She moves to run a hand down your shirt, but you shove the resume back into her hand."
                if the_person.love < 10:
                    mc.name "If I wanted to fuck you I wouldn't need to hire your mother to do it. Give it up, you look desperate."
                    $ the_person.change_obedience(3)
                    "She steps back and looks away."
                    $ the_person.draw_person(emotion = "sad")
                    the_person "Uh, right. Sorry for taking up your time."
                    "[the_person.possessive_title] hurries out of your office."
                else:
                    mc.name "I'm not hiring right now, and that's final. Now I'm sure you have work to do."
                    $ the_person.change_obedience(1)
                    "She takes the resume back and steps away from your desk, defeated."
                    $ the_person.draw_person(emotion = "sad")
                    the_person "Right, of course. Sorry for wasting your time."
                $ clear_scene()
                return

            else:
                $ the_person.draw_person(emotion = "sad")
                $ the_person.change_happiness(-3)
                the_person "I understand. Sorry for taking up your time."
                "She collects the resume and leaves your office."
                $ clear_scene()
                return

    $ the_mother = the_person.generate_mother(lives_with_daughter = in_private) #Produces a person who has a high chance to share characteristics with her mother.

    call hire_select_process([the_mother, 1]) from _call_hire_mother_work_select_process #Hire her or reject her. Padded with an extra item in the array or we crash due to trying to pre-calculate forward/backwards buttons

    $ the_person.draw_person()
    if _return == the_mother: #You've chosen to hire her.
        if in_private:
            # divorced so make sure she's single and the SO is cleared
            $ the_mother.relationship = "Single"
            $ the_mother.SO_name = None

        $ hire_day = "tomorrow"
        if day%7 == 4 or day%7 == 5: #If it's Friday or Saturday, don't start tomorrow
            $ hire_day = "Monday"

        if promised_sex:
            mc.name "Alright, I'll admit this looks promising, but I need some convincing."
            the_person "Of course, [the_person.mc_title]."
            "She steps around your desk and comes closer to you."
            $ the_person.add_situational_obedience("bribe", 30, "It's for my mother and her future!")
            call fuck_person(the_person) from _call_fuck_person_hire_mother_work_1
            $ the_person.draw_person()
            $ the_person.clear_situational_obedience("bribe")
            $ the_person.change_obedience(2)
            $ the_person.review_outfit()
            the_person "Are we all done then?"
            mc.name "For now. You can call your mother and tell her she can start [hire_day]. I won't give her any preferential treatment from here on out though."
            the_person "Of course. Thank you."
            call hire_someone(the_mother) from _call_hire_mother_work_1
        else:
            mc.name "Alright [the_person.title], this looks promising, she can start [hire_day]. I can't give her any preferential treatment, but I'll give her a try."
            $ the_person.draw_person(emotion = "happy")
            $ the_person.change_stats(happiness = 5, love = 2)
            the_person "Thank you so much!"
            call hire_someone(the_mother) from _call_hire_mother_work_2
        # make sure to set titles for the mother (prevent introduction dialogs)
        $ the_mother.set_mc_title(get_random_from_list(the_mother.get_player_titles()))
        $ the_mother.set_title(the_mother.get_random_title())
        $ the_mother.set_possessive_title(the_mother.get_random_possessive_title())
    else: #is "None
        if promised_sex: #You promised to do it for sex but don't want to hire her, mom is disappointed.
            mc.name "I'm sorry, but her credentials just aren't what they need to be. I could never justify hiring your mother."
            $ the_person.change_stats(happiness = -5, love = -2)
            $ the_person.draw_person(emotion = "sad")
            "[the_person.possessive_title] seems to deflate. She nods sadly."
            the_person "I understand. Thank you for the time."
        else:
            mc.name "I'm sorry, but I don't think her skills are where I would need them to be."
            $ the_person.change_obedience(1)
            the_person "I understand, thank you for at least taking a look for me."

    $ del the_mother
    $ clear_scene()
    return
