init 10 python:  # load quest tracker last on stack (higher init number is later on stack)
    add_label_hijack("normal_start", "activate_side_quest_mod_core")
    add_label_hijack("after_load", "update_side_quest_mod_core")


label activate_side_quest_mod_core(stack):
    python:
        Quest_tracker_init()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_side_quest_mod_core(stack):
    python:
        try:
            quest_director  #Hopefully triggers for existing save games to create the quest director.
            Quest_tracker_update()
        except NameError:
            Quest_tracker_init()

        execute_hijack_call(stack)
    return
