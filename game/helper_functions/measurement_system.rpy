init -1 python:
    global use_imperial_system

    use_imperial_system = True

init 2 python:
    def metric_system_requirement():
        return use_imperial_system

    def imperial_system_requirement():
        return not use_imperial_system

    metric_system_action = Action("Use metric system", metric_system_requirement, "change_to_metric_system_label", menu_tooltip = "Switch to the metric system of meters and kilograms")
    imperial_system_action = Action("Use imperial system", imperial_system_requirement, "change_to_imperial_system_label", menu_tooltip = "Switch to the imperial system of feet and pounds")

init 5 python:
    add_label_hijack("normal_start", "activate_measurement_system")
    add_label_hijack("after_load", "update_measurement_system")

label activate_measurement_system(stack):
    python:
        bedroom.add_action(metric_system_action)
        bedroom.add_action(imperial_system_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_measurement_system(stack):
    python:
        bedroom.add_action(metric_system_action)
        bedroom.add_action(imperial_system_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label change_to_metric_system_label():
    $ use_imperial_system = False
    return

label change_to_imperial_system_label():
    $ use_imperial_system = True
    return
