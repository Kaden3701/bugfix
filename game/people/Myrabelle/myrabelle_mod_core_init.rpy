init 5 python:
    add_label_hijack("normal_start", "activate_myrabelle_mod_core")
    add_label_hijack("after_load", "update_myrabelle_mod_core")


label activate_myrabelle_mod_core(stack):
    python:
        #This function only runs on initial new game start
        myra_focus_progression_scene_init()
        myra_alexia_teamup_scene_init()
        # continue on the hijack stack if needed
        if myra_alexia_teamup_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_alexia_teamup_scene)
        if myra_focus_progression_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_focus_progression_scene)
        execute_hijack_call(stack)
    return

label update_myrabelle_mod_core(stack):
    python:
        if "myra_focus_progression_scene" not in globals():
            myra_focus_progression_scene_init()
        else:
            myra_focus_progression_scene.compile_scenes(myra_focus_progression_scene)

        if "myra_alexia_teamup_scene" not in globals():
            myra_alexia_teamup_scene_init()
        else:
            myra_alexia_teamup_scene.compile_scenes(myra_alexia_teamup_scene)

        if myra_alexia_teamup_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_alexia_teamup_scene)
        if myra_focus_progression_scene not in list_of_progression_scenes:
            list_of_progression_scenes.append(myra_focus_progression_scene)

        execute_hijack_call(stack)
    return
