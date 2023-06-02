#Use this for fucking an employee while working.

init -1 python:
    def condition_computer_work_reward_req(self, the_person, report_log):
        if report_log.get("girl orgasms", 0) > 0 and self.condition_vars[0]:   #She orgasmed AND concentrated on her work
            return True
        return False


    def make_condition_computer_work():
        computer_work_whitelist = [anal_standing, standing_doggy, spanking]
        computer_work_condition = Condition_Type("Computer Work", pre_label = "condition_computer_work_pre_label", post_label = "condition_computer_work_post_label", position_whitelist = computer_work_whitelist,
            reward_cond = condition_computer_work_reward_req, reward_label = "condition_computer_work_reward_label", fail_label = "condition_computer_work_fail_label")
        computer_work_condition.condition_vars.append(True)   #Leave true if she is concentrating on her work.
        computer_work_condition.condition_vars.append(0)       #Distraction level
        return computer_work_condition


label condition_computer_work_pre_label(the_person, the_position, the_object, report_log, the_condition):
    if the_person.arousal_perc < 50 or the_condition.condition_vars[1] < 50:
        "[the_person.possessive_title] continues working on her computer while you take advantage of her."
    elif the_condition.condition_vars[0]:
        if the_condition.condition_vars[1] < 100:   #She's not very distracted
            $ play_moan_sound()
            "[the_person.possessive_title] moans, but continues to work on her computer despite your distraction."
        elif the_condition.condition_vars[1] < 200: #She's distracted
            "[the_person.possessive_title] is moaning. Her work has slowed considerably from your distraction but she is still trying."
        elif the_condition.condition_vars[1] < 300: #She's very distracted
            "[the_person.possessive_title] is moaning and arching her back. Her work has almost stopped, but she is trying to keep going despite your distraction."
        else:
            $ play_moan_sound()
            "[the_person.possessive_title] has given up trying to work. She moans and arches her back, pushing her ass back against you."
            $ the_condition.condition_vars[0] = False
    else:
        "[the_person.possessive_title] is moaning and arching her back, pushing her ass back against you. She isn't even looking at her computer screen anymore."
    if not the_condition.condition_vars[0] or the_condition.condition_vars[1] > 100:    #If she's atleast a little bit distracted
        menu:
            "Get back to work" if not the_condition.condition_vars[0]:
                "You give her ass a solid spank."
                mc.name "Did I say you could stop? Get back to it!"
                $ the_condition.condition_vars[1] += (-100)
                if the_condition.condition_vars[1] < 300:
                    "[the_person.possessive_title] snaps her head up and starts typing again."
                else:
                    $ play_moan_sound()
                    "[the_person.possessive_title] just moans. The pleasure is so intense she can't even pretend to work anymore."
            "Tell her to concentrate" if the_condition.condition_vars[0]:
                mc.name "You better keep at it. I didn't say you could take a break!"
                $ the_condition.condition_vars[1] += (-50)
                the_person "Yes [the_person.mc_title]!"
            "Let her be":
                pass
    return

label condition_computer_work_post_label(the_person, the_position, the_object, report_log, the_condition):
    $ the_condition.condition_vars[1] += (report_log.get("girl orgasms", 0) * 40) + 25
    return

label condition_computer_work_reward_label(the_person, report_log, the_condition):
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.title] is still working on her computer, despite her orgasm."
    mc.name "Good work."
    the_person "Wow, if that is how you reward good employees..."
    $ the_person.change_obedience(20)
    "[the_person.possessive_title] seems much more obedient now."
    return

label condition_computer_work_fail_label(the_person, report_log, the_condition):
    if not the_condition.condition_vars[0]:
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.title] has stopped working completely."
        if office_punishment.is_active:
            mc.name "Did I tell you to stop working? I'll have to record this as performance infraction."
            $ the_person.add_infraction(Infraction.underperformance_factory())
        else:
            mc.name "Did I tell you to stop working?"
        "[the_person.possessive_title] doesn't respond."
        if the_person.is_in_trance:
            "In fact, she appears to be in a trance. Maybe you should take advantage of it?"
            call do_training(the_person) from _call_do_training_condition_comp_work_01
        else:
            "She seems happy though. You gave her a pretty thorough dicking."
            $ the_person.change_happiness(10)
    else:
        "You finish with [the_person.possessive_title] for now. She seems disappointed but obediently gets back to work."

    return
