# This file is used to define the functions and actions needed for a new clarity based character menu
# Screen is in a different file

init -2 python:
    def persuade_person_requirement(the_person):
        if the_person == city_rep and city_rep.event_triggers_dict.get("currently_interrogating", False):
            return "Not during official visit"
        if mc.free_clarity < 500:
            return "Requires: 500+ Clarity"
        return True

    def clarity_train_int_requirement(the_person):
        if the_person.int >= mc.int:
            return "Requires: Higher MC Intelligence"
        elif the_person.int >= 7:
            return "Intelligence maximum reached"
        elif mc.free_clarity < (the_person.int * 500):
            return "Requires: {} Clarity".format(the_person.int * 500)
        return True

    def clarity_train_cha_requirement(the_person):
        if the_person.charisma >= mc.charisma:
            return "Requires: Higher MC Charisma"
        elif the_person.charisma >= 7:
            return "Charisma maximum reached"
        elif mc.free_clarity < (the_person.charisma * 500):
            return "Requires: {} Clarity".format(the_person.charisma * 500)
        return True

    def clarity_train_focus_requirement(the_person):
        if the_person.focus >= mc.focus:
            return "Requires: Higher MC Focus"
        elif the_person.focus >= 7:
            return "Focus maximum reached"
        elif mc.free_clarity < (the_person.focus * 500):
            return "Requires: {} Clarity".format(the_person.charisma * 500)
        return True

    def clarity_train_obedience_requirement(the_person):
        if (the_person.obedience - 100) / 5 >= mc.charisma:
            return "Requires: Higher MC Charisma"
        elif the_person.obedience > 150:
            return "Obedience maximum reached"
        elif mc.free_clarity < max(500, ((the_person.obedience - 100) * 100)):
            return "Requires: {} Clarity".format(max(500, ((the_person.obedience - 100) * 100)))
        return True

    def clarity_serum_dose_requirement(the_person):
        if mc.inventory.total_serum_count <= 0:
            return "Requires: Serum in inventory"
        if len(the_person.serum_effects) >= the_person.serum_tolerance:
            return "Already at Serum Limit"
        if mc.free_clarity < 500:
            return "Requires: 500 Clarity"
        return True

    def build_clarity_person_actions_menu(the_person):
        clarity_train_int_action = Action("Train her Intelligence", requirement = clarity_train_int_requirement, effect = "clarity_train_int", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her intelligence score.", priority = -5)
        clarity_train_cha_action = Action("Train her Charisma", requirement = clarity_train_cha_requirement, effect = "clarity_train_cha", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her charisma score.", priority = -5)
        clarity_train_focus_action = Action("Train her Focus", requirement = clarity_train_focus_requirement, effect = "clarity_train_focus", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her focus score.", priority = -5)
        clarity_train_obedience_action = Action("Train her Obedience", requirement = clarity_train_obedience_requirement, effect = "clarity_train_obedience", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to increase her obedience.", priority = -5)
        clarity_serum_dose_action = Action("Give her a serum", requirement = clarity_serum_dose_requirement, effect = "clarity_serum_dose", args = the_person, requirement_args = the_person,
            menu_tooltip = "Utilize your clarity to give her a serum.", priority = -5)

        return ["Persuade", clarity_train_int_action, clarity_train_cha_action, clarity_train_focus_action , clarity_train_obedience_action, clarity_serum_dose_action, ["Never mind", "Return"]]


label persuade_person(the_person):
    mc.name "[the_person.title], I was hoping you would do something for me."
    the_person "Yes [the_person.mc_title]?"

    call screen main_choice_display(build_menu_items([build_clarity_person_actions_menu(the_person)]))

    if isinstance(_return, Action):
        $ _return.call_action()
    return

label clarity_train_int(the_person):
    mc.name "I was hoping we could have some one-on-one time. I came across a few things I thought you might appreciate."
    the_person "I suppose we could do that."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours chatting about recent advances in science and the scientific method."
    $ mc.spend_clarity(the_person.int * 500)
    $ the_person.change_int(1)
    the_person "Thank you [the_person.mc_title], that was very educational!"

    call advance_time from _call_advance_clarity_int_01
    return "Advance Time"

label clarity_train_cha(the_person):
    mc.name "Hey, have you heard the latest rumours?"
    the_person "No, I haven't."
    mc.name "Ah, have some time for me to fill you in?"
    the_person "I suppose we could do that."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours chatting about the latest rumours and gossip."
    $ mc.spend_clarity(the_person.charisma * 500)
    $ the_person.change_cha(1)
    the_person "Thank you [the_person.mc_title], that was very educational!"
    call advance_time from _call_advance_clarity_cha_01
    return "Advance Time"

label clarity_train_focus(the_person):
    mc.name "Hey, are you busy? I was thinking about doing some meditation, and I thought you might want to join me."
    the_person "I didn't realize you did that. Sure I'd love to join you."
    $ the_person.draw_person(position = "sitting")
    "You sit down with [the_person.possessive_title]. You spend a few hours in still, silent communion, merely breathing while the world passes by around you."
    $ mc.spend_clarity(the_person.focus * 500)
    $ the_person.change_focus(1)
    the_person "Thank you [the_person.mc_title]. I feel like I can really focus on the rest of my day now!"
    call advance_time from _call_advance_clarity_focus_01
    return "Advance Time"

label clarity_train_obedience(the_person):
    if the_person.is_employee:
        mc.name "Hey, have a minute?"
        the_person "Sure."
        mc.name "I wanted to go over some work tasks. I want to make sure we are on the same page, organizationally."
        the_person "Okay."
        "You spend some time with [the_person.possessive_title], making sure they are performing their job the way you expect."
        the_person "I understand. Okay, I'm going to get back to work now."
    else:
        mc.name "Hey, have a minute?"
        the_person "Sure."
        "You spend some time with [the_person.possessive_title]."
        "You are careful not to say anything too overt, but use subtle language to encourage her to be more obedient and trust you more."
        the_person "Sorry [the_person.mc_title]. This is nice, but I need to get going."
    $ the_person.change_obedience(10)
    $ mc.spend_clarity(max(500, ((the_person.obedience - 100) * 100)))
    call advance_time from _call_advance_clarity_obedience_01
    return "Advance Time"

label clarity_serum_dose(the_person):
    $ mc.spend_clarity(500)
    call serum_give_label(the_person) from _call_clarity_serum_dose_01
    return
