## Employee Review Mod by Mattt
# Compliment/Insult all employees based on their happiness
init 3 python:
    def daily_talk_requirement():
        if mc.business.is_open_for_business and mc.business.employee_count > 0:
            if mc.business.event_triggers_dict.get("daily_talk_employees", 0) < day:
                return True
            return "Only once per day"
        return False

    def daily_talk_initialization(self):
        lobby.add_action(self)
        return

    def daily_talk_update_employee_stats():
        for person in [x for x in mc.business.employee_list if x.event_triggers_dict.get("day_last_employee_interaction", 0) < day]:
            person.event_triggers_dict["day_last_employee_interaction"] = day
            if person.obedience > 150 and person.love * 2 + 89 < person.obedience:
                person.change_stats(love = 1, happiness = mc.charisma)
            elif person.happiness > 120 and person.love >= 12:
                person.change_stats(happiness = -5, love = -2, obedience = mc.charisma)
            else:
                person.change_stats(happiness = mc.charisma, love = 1)

        mc.business.event_triggers_dict["daily_talk_employees"] = day
        return

    daily_talk_action = ActionMod("Talk with Employees {image=gui/heart/Time_Advance.png}", daily_talk_requirement, "daily_talk_employees", initialization = daily_talk_initialization,
        menu_tooltip = "Compliment Work (Happiness <= 120 or Love < 12) / Insult Work (Happiness > 120)", category = "Business")

label daily_talk_employees():

    "You tell all of your employees to meet you in the [lobby.formal_name] for a daily chat."
    $ daily_talk_update_employee_stats()

    call advance_time from daily_talk_employees_1

    return
