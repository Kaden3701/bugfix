## Production Failure Crisis Mod by Tristimdorion
init 2 python:
    def production_failure_requirement():
        if not mc.business.is_weekend:
            if mc.is_at_work:
                if time_of_day > 0 and time_of_day < 4: # only during morning afternoon or evening
                    if __builtin__.len(rd_division.people + p_division.people) > 0: # Must have RD or Prod employee
                        return True
        return False

    def production_failure_increase_sluttiness(person):
        for team_member in person.job.job_location.people:
            team_member.add_situational_slut("Gassed",25,"The girls become extremely slutty.")
            team_member.change_stats(slut = 1 + person.get_opinion_score("not wearing anything"), max_slut = 30, arousal = 50, add_to_log = False)

        mc.log_event("All " + person.job.job_location.formal_name + " staff affected","float_text_pink")
        return

    def production_failure_clear_situational_sluttiness(person):
        for team_member in person.job.job_location.people:
            team_member.clear_situational_slut("Gassed")

        person.apply_planned_outfit()
        return

    def production_failure_change_obedience(person, amount):
        for team_member in person.job.job_location.people:
            team_member.change_obedience(amount, add_to_log = False)

        mc.log_event("All " + person.job.job_location.formal_name + " staff: " + str(amount) + " obedience","float_text_pink")
        return

    def production_failure_fix_the_problem(person):
        for team_member in person.job.job_location.people:
            team_member.change_stats(happiness = -2, love = 2, add_to_log = False)

        mc.log_event("All " + person.job.job_location.formal_name + " staff: +2 love, -2 happiness","float_text_pink")
        return

    production_failure_action = ActionMod("Production Failure", production_failure_requirement, "production_failure_action_label",
        menu_tooltip = "An accident during research / production causes some issues.", category = "Business", is_crisis = True)


label production_failure_action_label():
    $ the_person = get_random_from_list(rd_division.people + p_division.people)
    if the_person is None or not the_person.is_employee:
        return

    "While monitoring the equipment you notice a problem in the [the_person.job.job_location.formal_name], it seems a gas mixture is building up."
    "Without halting work and alerting everyone to the problem there is no way to fix it. You also can't be sure what the effects of this will be on your employees."
    menu:
        "Halt work and fix the problem":
            "The girls are clearly unhappy about breathing in a foreign substance. But are extremely grateful you alerted them so soon."
            $ production_failure_fix_the_problem(the_person)
            "The repair man shows up early and fixes the problem. The loss of production was negligible."

        "Call in an overnight repair man":
            "You call the repair man and tell him to come in that night, and warn him not to alert anyone and to wear a gas mask."
            if mc.location != the_person.job.job_location:
                "You decide to monitor the situation first hand and move to the [the_person.job.job_location.formal_name]."
                $ mc.change_location(the_person.job.job_location)
            else:
                "You decide to monitor the situation first hand and stay in the [the_person.job.job_location.formal_name]."

            $ ran_num = renpy.random.randint(0,100)
            if ran_num > 45: # 55% chance it's a mixture that alters behavior (slutty)
                "For the first half hour everything seems fine, but then you notice a sudden shift in behavior."
                if mc.location.person_count > 1:
                    "The girls are clearly hot and bothered. They barely keep their focus on their work, spending much of their time eyeing you and each other."
                    "[the_person.fname] appears to have been particularly affected."
                else:
                    "[the_person.fname] is clearly hot and bothered. She can barely keep her focus on her work, spending much of her time eyeing you."
                $ production_failure_increase_sluttiness(the_person)
                $ the_person.draw_person(position = "stand2", emotion = "happy")
                $ the_person.change_slut(2)

                "[the_person.fname] looks around desperately trying to figure out the source of her sudden arousal. When she sees you she immediately loses control."
                the_person "Please [the_person.mc_title], I need you... please help me..."
                $ the_person.break_taboo("touching_penis")
                $ mc.change_locked_clarity(20)
                "[the_person.possessive_title] shoves her hand down your pants and begs for your cock."

                call fuck_person(the_person, private = False, skip_intro = True) from _call_fuck_person_production_failure_action_label

                the_person "*Panting* Oh god, [the_person.mc_title]. Thank you... thank you so much."

                $ production_failure_clear_situational_sluttiness(the_person)

                "You leave [the_person.possessive_title] to get cleaned up and get back to work."
            elif ran_num > 30: # 15% chance
                $ production_failure_change_obedience(the_person, 3)
                "The girls seem slightly more respectful."
            elif ran_num > 15: # 15% chance
                "Everyone appears fine, there doesn't seem to be an effect."
            else: # 15% chance it's a foul mixture
                $ production_failure_change_obedience(the_person, -5)
                "The mood of all the girls turn sour. They spend the next few hours bickering about petty nonsense."
    return
