init 5 python:
    add_label_hijack("normal_start", "activate_sarah_mod_core")
    add_label_hijack("after_load", "update_sarah_mod_core")

label activate_sarah_mod_core(stack):
    python:
        hr_director_prog_scene_init()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_sarah_mod_core(stack):
    python:
        # assign correct weight to relative recruitment status
        if get_HR_director_tag("business_HR_relative_recruitment", 0) == 2:
            update_hire_daughter_crisis(10)
            update_hire_mother_crisis(10)
        else:
            # when Sarah did not put the sign up, disable the event completely.
            # also prevents the event from occurring at start of game.
            update_hire_daughter_crisis(0)
            update_hire_mother_crisis(0)

        if "hr_director_prog_scene" not in globals():
            hr_director_prog_scene_init()
        else:
            hr_director_prog_scene.compile_scenes(hr_director_prog_scene)
        execute_hijack_call(stack)
    return
