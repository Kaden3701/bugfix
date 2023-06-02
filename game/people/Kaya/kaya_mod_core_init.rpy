init 5 python:
    add_label_hijack("normal_start", "activate_kaya_mod_core")
    add_label_hijack("after_load", "update_kaya_mod_core")


label activate_kaya_mod_core(stack):
    python:
        kaya_erica_teamup_init()
        if kaya_erica_teamup not in list_of_progression_scenes:
            list_of_progression_scenes.append(kaya_erica_teamup)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_kaya_mod_core(stack):
    python:
        if "kaya_erica_teamup" not in globals():
            kaya_erica_teamup_init()
        if not isinstance(kaya_erica_teamup, Progression_Scene):
            kaya_erica_teamup_init()
        kaya_erica_teamup.compile_scenes(kaya_erica_teamup)
        if kaya_erica_teamup not in list_of_progression_scenes:
            list_of_progression_scenes.append(kaya_erica_teamup)
        execute_hijack_call(stack)
    return
