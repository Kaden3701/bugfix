init 20 python:  # load quest tracker last on stack (higher init number is later on stack)
    add_label_hijack("normal_start", "activate_side_character_mod_core")

    def side_character_init():
        mc.business.event_triggers_dict["side_character_unavail_list"] = MappedList(Person, all_people_in_the_game)
        #print("Adding {} unique charaters to side char list".format(len(unique_character_list)))
        for person in unique_character_list:
            mc.business.event_triggers_dict["side_character_unavail_list"].append(person)

        # init side char quests
        mc.business.add_mandatory_crisis(cuckold_employee_init)
        mc.business.add_mandatory_crisis(chemist_daughter_init)
        return

    def side_character_set_unavail(person):
        mc.business.event_triggers_dict["side_character_unavail_list"].append(person)
        return

    def side_character_is_unavail(person):
        return person in mc.business.event_triggers_dict.get("side_character_unavail_list", [])

    def side_character_unavail_list():
        return [x for x in mc.business.event_triggers_dict.get("side_character_unavail_list", [])]

label activate_side_character_mod_core(stack):
    python:
        side_character_init()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
