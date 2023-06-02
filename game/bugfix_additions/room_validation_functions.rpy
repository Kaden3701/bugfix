init 10 python:
    add_label_hijack("normal_start", "validate_custom_rooms")
    add_label_hijack("after_load", "update_custom_rooms")

    def fix_duplicate_objects_in_rooms():
        for room in list_of_places:
            unique = list(set(room.objects))
            if len(unique) != len(room.objects):    # mismatch update
                room.objects = unique
        return

    def fix_duplicate_bedroom_objects():
        if not lily.bedroom is lily_bedroom:
            lily.bedroom = lily_bedroom
        if not mom.bedroom is mom_bedroom:
            mom.bedroom = mom_bedroom
        if not aunt.bedroom is aunt_bedroom:
            aunt.bedroom = aunt_bedroom
        if not cousin.bedroom is cousin_bedroom:
            cousin.bedroom = cousin_bedroom
        return

    def update_room_visibility():
        remove_list = []
        for i in range(0, len(list_of_places) - 1):
            for j in range(i + 1, len(list_of_places)):
                if not list_of_places[j] in remove_list:
                    if i == j:
                        remove_list.append(list_of_places[j])

        if len(remove_list) > 0:
            for room in remove_list:
                renpy.say("Warning", "Duplicate room " + room.name + ", game is corrupt, you are advised to start a new game.")

        return

    def link_unique_character_bedrooms():
        lily.bedroom = lily_bedroom
        mom.bedroom = mom_bedroom
        aunt.bedroom = aunt_bedroom
        cousin.bedroom = cousin_bedroom
        return

    def update_rd_div_with_genetics_unlocked():
        if not genetic_modification_policy.is_owned:
            return

        found = find_in_list(lambda x: x.name == "R&D division", list_of_places)
        if found:
            found.background_image = biotech_background
        return

label update_custom_rooms(stack):
    python:
        update_room_visibility()
        fix_duplicate_objects_in_rooms()
        fix_duplicate_bedroom_objects()
        update_rd_div_with_genetics_unlocked()

        execute_hijack_call(stack)
    return

label validate_custom_rooms(stack):
    # extra code run after creation of all rooms
    python:
        # initialize dungeon room creation action
        fix_duplicate_objects_in_rooms()
        link_unique_character_bedrooms()

        execute_hijack_call(stack)
    return
