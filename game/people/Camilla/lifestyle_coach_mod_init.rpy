init 5 python:
    add_label_hijack("normal_start", "activate_lifestyle_coach_mod_core")
    add_label_hijack("after_load", "update_lifestyle_coach_mod_core")


label activate_lifestyle_coach_mod_core(stack):
    python:
        # lifestyle_coach_init()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_lifestyle_coach_mod_core(stack):
    pass
    $ execute_hijack_call(stack)
    return
