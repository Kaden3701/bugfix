init 1 python: #Original code is at -1, so make sure we are higher than that for custom code
    #This is the requirement for the punishment itself
    def punishment_service_mc_requirement(the_person, the_infraction):
        if the_infraction.severity < 3:
            return "Severity 3"
        elif not corporal_punishment.is_active:
            return "Requires Policy: Corporal Punishment"
        else:
            return True

    def employee_cocksucking_practice_remove_requirement(the_person, trigger_day):
        if day >= trigger_day:
            return True
        return False

    def employee_cocksucking_practice_report_requirement(the_person):
        if not mc.business.is_open_for_business:
            return False
        elif not mc.is_at_work:
            return False
        return True

    # Practice adding a time gated work discipline.
    def add_practice_cocksucking_work_action(person):
        if not person.has_role(employee_practice_cocksucking_work_role): # prevent adding it twice
            person.add_role(employee_practice_cocksucking_work_role)
            clear_action = Action("Clear employee cocksucking practice", employee_cocksucking_practice_remove_requirement, "employee_cocksucking_practice_remove_label", args = person, requirement_args = [person, day + 7])
            mc.business.add_mandatory_crisis(clear_action)
        return

    def add_practice_cocksucking_report_action(person):
        if person.has_role(employee_practice_cocksucking_work_role):
            person.remove_role(employee_practice_cocksucking_work_role, remove_linked = False)

        if person.has_role(employee_role): #She may have quit/been fired since then.
            person.sex_skills["Oral"] = min(4, person.sex_skills["Oral"] + 1)

            if person.get_opinion_score("giving blowjobs") <= -2:
                person.update_opinion_with_score("giving blowjobs", -1, add_to_log = False)  #Set this to -1 if it was -2 so that she at least tries to give MC a blowjob.

            practice_cocksucking_report_action = Action("Cocksucking practice report crisis", employee_cocksucking_practice_report_requirement, "employee_cocksucking_practice_report_label", args = person, requirement_args = person)
            mc.business.add_mandatory_crisis(practice_cocksucking_report_action)
        return

    employee_practice_cocksucking_work_role = Role("Practicing Cocksucking", [], hidden = True)

    punishment_service_mc_action = Action("Service Me", punishment_service_mc_requirement, "punishment_service_mc_label") #Let's follow previous naming conventions and add label to labe names
    list_of_punishments.append(punishment_service_mc_action)

label punishment_service_mc_label(the_person, the_infraction):
    mc.name "It's time for your punishment [the_person.title]."
    the_person "What are you going to do?"
    mc.name "When you break company rules, you are being selfish. You're only serving yourself."
    mc.name "I think it's time you learned a lesson by servicing someone else. Namely, me."
    if the_person.effective_sluttiness() < 40:
        the_person "What do you mean?"
        "You step closer to her and put your hands on her shoulders."
        mc.name "Get down on your knees. It will be obvious momentarily."
        the_person "Wha... What? You can't be serious... You can't do that!"
        mc.name "Of course I can, punishments are all listed in the employee manual. Of course, if you'd prefer to quit I can walk you to the door."
        the_person "Fine... Just warn me when you get close [the_person.mc_title]... I don't want you finishing in my mouth."
        mc.name "I'll warn you if I please. Now get on your knees."
    elif the_person.effective_sluttiness() < 80:
        the_person "Okay [the_person.mc_title], I'll take my punishment."
        "You step closer to her and put your hands on her shoulders."
        mc.name "Good girl. Now get on your knees."
    else:
        the_person "Come on, wouldn't it be better if we both enjoyed ourselves?"
        mc.name "I fully intend to enjoy myself with you, but you aren't going to get anything in return."
        "[the_person.possessive_title] pouts while you step closer to her. You put your hands on her shoulders."
        mc.name "So be a good girl and get on your knees."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] sinks down to her knees while you reach down and pull out your cock. She tentatively sticks her tongue out and runs it over the tip."
    mc.name "It's going to take a bit more than that. Now open up."
    $ the_person.break_taboo("sucking_cock")
    "Finally relenting, [the_person.possessive_title] opens her mouth and takes you. While her technique isn't amazing, the soft confines of her mouth feels great."
    $ the_person.add_situational_obedience("punishment", 40, "I'm being punished, I don't have any right to refuse.")
    call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = True, affair_ask_after = False, condition = make_condition_blowjob_training()) from _call_custom_bj_punishment_01
    $ the_report = _return
    $ the_person.clear_situational_obedience("punishment")

    if the_report.get("guy orgasms", 0) == 0: #She didn't finish you off. Berate her verbally.
        mc.name "I'm sorry, but that was not an acceptable performance. It seems you can't even get something as basic as sucking my cock done right."
        the_person "I'm... I'm sorry sir... I tried my best..."
        mc.name "I have a new punishment for you. I want you to practice sucking cock for the next week. Then come back to me and try again."
        the_person "That's... that's crazy!"
        mc.name "What's crazy is how bad at giving head you are. You heard me, now get back to work."
        $ the_person.change_stats(happiness = -5, obedience = 2)
        $ add_practice_cocksucking_work_action(the_person)
    else:
        "You give a sigh, satisfied after [the_person.possessive_title] drained your balls."
        mc.name "You look good like that. Next time this happens, I'll have you wear my cum on your face for the rest of the day."
        the_person "Yes sir..."
        $ the_person.change_stats(happiness = -5, obedience = 3)
        mc.name "Alright, I hope you learned something. Now get back to work."
    $ clear_scene()
    return

label employee_cocksucking_practice_remove_label(the_person):
    $ add_practice_cocksucking_report_action(the_person)
    return

label employee_cocksucking_practice_report_label(the_person):
    if not the_person.has_role(employee_role): #She doesn't work here, bail out!
        return

    $ the_person.draw_person()
    "[the_person.title] catches your attention while you are working."
    the_person "Do you have a moment [the_person.mc_title]?"
    mc.name "Sure, what do you need?"
    the_person "I wanted to let you know that I've finished my week of punishment."
    mc.name "Good. Show me."
    the_person "Like... right here?"
    "You put your hands on her shoulders."
    mc.name "There's no time like the present. Now get on your knees and give this another shot."
    the_person "Ahh... okay..."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] sinks down to her knees while you reach down and pull out your cock. She tentatively sticks her tongue out and runs it over the tip."
    mc.name "It's going to take a bit more than that. Now open up."
    $ the_person.break_taboo("sucking_cock")
    "Finally relenting, [the_person.possessive_title] opens her mouth and takes you. While her technique isn't great, the soft confines of her mouth feel great."
    $ the_person.add_situational_obedience("punishment", 40, "I'm being punished, I don't have any right to refuse.")
    call fuck_person(the_person, private = False, start_position = blowjob, skip_intro = True, affair_ask_after = False, condition = make_condition_blowjob_training()) from _call_custom_bj_punishment_02
    $ the_report = _return
    $ the_person.clear_situational_obedience("punishment")
    if the_report.get("guy orgasms", 0) == 0: #She didn't finish you off. Berate her verbally.
        mc.name "God, that was awful. Are you sure you've been practicing?"
        the_person "I'm... I'm sorry sir... I tried my best..."
        mc.name "Fine... next time I'll just have you service me with a different hole."
        the_person "Yes sir."
        mc.name "It's crazy how bad at giving head you are. Now get back to work."
        $ the_person.change_stats(happiness = -5, obedience = 3)
    else:
        "You give a sigh, satisfied after [the_person.possessive_title] drained your balls."
        mc.name "Much better performance."
        mc.name "You look good like that. Next time this happens, I'll have you wear my cum on your face for the rest of the day."
        the_person "Yes sir..."
        $ the_person.change_stats(happiness = -5, obedience = 4)
    mc.name "Alright, I hope you learned something. Now get back to work."
    $ clear_scene()
    return
