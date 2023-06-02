init 2 python:
    def change_crisis_chance_requirement():
        return True

    change_crisis_chance_action = Action("Change Event Occurrence", change_crisis_chance_requirement, "show_crisis_chance_ui", menu_tooltip = "Change how often events will occur in the game.")

init 5 python:
    add_label_hijack("normal_start", "activate_change_crisis_chance")
    add_label_hijack("after_load", "update_change_crisis_chance")

    def action_mod_disabled_count():
        disabled = 0
        for action_mod in action_mod_list:
            if hasattr(action_mod, "is_crisis") and action_mod.is_crisis and not action_mod.enabled:
                if not hasattr(action_mod, "is_morning_crisis") or not action_mod.is_morning_crisis:
                    disabled += 1
        return disabled

    def action_mod_morning_disabled_count():
        morning_disabled = 0
        for action_mod in action_mod_list:
            if hasattr(action_mod, "is_crisis") and action_mod.is_crisis and not action_mod.enabled:
                if hasattr(action_mod, "is_morning_crisis") and action_mod.is_morning_crisis:
                    morning_disabled += 1
        return morning_disabled

label activate_change_crisis_chance(stack):
    python:
        bedroom.add_action(change_crisis_chance_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_change_crisis_chance(stack):
    python:
        if not change_crisis_chance_action in bedroom.actions:
            bedroom.add_action(change_crisis_chance_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_crisis_chance_ui():
    $ renpy.call_screen("crisis_chance_setting", action_mod_disabled_count(), action_mod_morning_disabled_count())
    $ crisis_chance = crisis_base_chance
    $ morning_crisis_chance = morning_crisis_base_chance
    return
