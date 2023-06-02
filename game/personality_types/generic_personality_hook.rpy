# Generic Personality Hook by Tristimdorion
# overrides the default make person function in the game
# so we can add / change person characteristics based on custom personalities.
# if you need person customizations, extend the hijacked labels
init 2:
    default persistent.low_memory_wardrobes = True

init 10 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_generic_personality")
    add_label_hijack("after_load", "update_generic_personality")

init 2 python:
    # change the random person based other characteristics of personality
    def update_special_personalities(person):
        # turn cougars on or off
        update_cougar_personality(person)
        # turn alpha personality on or off
        update_alpha_personality(person)
        return

    def change_personality(person, personality):
        if not person.personality == personality:
            person.event_triggers_dict["original_personality"] = person.personality.personality_type_prefix
            person.personality = personality
        return

    def restore_original_personality(person):
        original_personality = None
        if person.event_triggers_dict.has_key("original_personality"):
            original_personality = find_in_list(lambda x: x.personality_type_prefix == person.event_triggers_dict["original_personality"], list_of_personalities)
        if not original_personality:
            original_personality = get_random_from_list(list_of_personalities)
        if original_personality:
            person.personality = original_personality
        return


    def update_cougar_personality(person):
        # change personality to cougar if we meet age requirement
        if action_mod_list is None or find_in_list(lambda x: x.effect == "cougar_personality_dummy_label", action_mod_list).enabled:
            if  person.age > 45 and person not in unique_character_list:
                change_personality(person, cougar_personality)
                # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        else:
            if person.personality == cougar_personality:
                if person not in unique_character_list:
                    restore_original_personality(person)
                    # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return

    def update_alpha_personality(person):
        # change personality to alpha if we meet requirements
        if action_mod_list is None or find_in_list(lambda x: x.effect == "alpha_personality_dummy_label", action_mod_list).enabled:
            if person.age > 25 and person.charisma >= 5 and person.int >= 4 and person.get_opinion_score("taking control") > 0 and person not in unique_character_list:
                if not person.personality == alpha_personality:
                    change_personality(person, alpha_personality)
                    # mc.log_event((person.title or person.name) + "  A:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        else:
            if person.personality == alpha_personality:
                if person not in unique_character_list:
                    restore_original_personality(person)
                    # mc.log_event((person.title or person.name) + " D:" + str(person.age) + ": " + person.personality.personality_type_prefix, "float_text_grey")
        return



    def get_party_destinations():
        party_destinations = []

        def add_party_destination_by_room(room):    # add correct room object from list_of_places (prevents people disappearing)
            found = find_in_list(lambda x: x.name == room.name, list_of_places)
            if found:
                party_destinations.append(found)

        for room in [downtown_bar, downtown_hotel, downtown]:
            add_party_destination_by_room(room)

        if not strip_club_is_closed():
            add_party_destination_by_room(strip_club)
            if bdsm_room_available():
                add_party_destination_by_room(bdsm_room)

        return party_destinations


    def create_party_schedule(person):
        if person in unique_character_list:
            return  # don't touch unique characters
        if person.is_strip_club_employee or person in stripclub_strippers:
            return  # no party for the working girls
        if person.pregnancy_is_visible:
            return  # no party for girls who already show the baby bump

        # clear old party schedule (clear after stripper check as to not clear her override schedule during foreclosed phase)
        person.set_override_schedule(None, the_times = [4])

        count = 0
        party_destinations = get_party_destinations()
        if person.get_opinion_score("Mondays") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [0], the_times=[4])
            count += 1
        if person.get_opinion_score("Fridays") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [4], the_times=[4])
            count += 1
        if person.get_opinion_score("the weekend") > 0:
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [5], the_times=[4])
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [6], the_times=[4])
            count += 2

        while count < 2:
            rnd_day = renpy.random.randint(0, 6)
            person.set_override_schedule(renpy.random.choice(party_destinations), the_days = [rnd_day], the_times=[4])
            count += 1
        return

    def create_bimbo():
        # add one bimbo to the game (on start of game)
        person = make_person(age=renpy.random.randint(21, 35), tits="DD", face_style = "Face_4", skin = "tan", stat_array = [4, 1, 2],
            hair_colour = ["platinum blonde", [.789, .746, .691, 1]], hair_style = messy_hair, eyes = ["light blue", [0.60, 0.75, 0.98, 1.0]], personality = bimbo_personality, force_random = True,
            forced_opinions = [["high heels", 2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False]])
        person.generate_home()
        person.home.add_person(person)
        return

    def create_alpha_personality():
        person = make_person(age = renpy.random.randint(25,35), personality = alpha_personality, relationship = "Single", stat_array = [5, 4, 3], force_random = True,
            forced_opinions = [["high heels", 2, False], ["the colour black", 2, False], ["the colour pink", -2, False], ["the colour green", -2, False]],
            forced_sexy_opinions = [["skimpy outfits", 2, False], ["being submissive", -1, False], ["taking control", 2, False]])
        person.generate_home()
        person.home.add_person(person)
        return

    def update_characters():
        for person in all_people_in_the_game(unique_character_list):
            update_special_personalities(person)
            create_party_schedule(person)
        return

    unique_character_list = []  # global not stored variable (since not defined in label function)
    progress_list = []

    def create_unique_character_list():
        # use extend when adding a list to another list
        unique_character_list.extend([mom, lily, aunt, cousin, stephanie, alexia, nora, emily, christina, city_rep, iris])

        # mod unique characters at game start
        unique_character_list.extend([salon_manager, starbuck, sarah, naomi, candace, ashley, erica, camilla, kaya, ellie, sakari, myra])
        return

    def setup_progression_scenes():
        base_name = "{}_story_character_description"

        for person in unique_character_list:
            func_name = base_name.format(person.name.lower())
            if func_name in globals():
                progress_list.append(Progression(person))
        return

    def update_main_character_actions():
        if "main_character_actions_list" in globals():
            for action in main_character_actions_list:
                if action not in mc.main_character_actions:
                    mc.main_character_actions.append(action)
        return

    def generate_random_mothers_and_daughters():
        for person in [x for x in all_people_in_the_game(excluded_people = unique_character_list) if x.age > 35 or x.age < 25]:
            if renpy.random.randint(0, 1) == 1:
                if person.age > 35:
                    for count in range(0, renpy.random.randint(1, 3)):
                        person.generate_daughter(True)
                else:
                    person.generate_mother(True)

    def generate_random_sisters_cousins_nieces():
        mothers = [x for x in all_people_in_the_game(excluded_people = unique_character_list) if town_relationships.get_existing_child_count(x) > 0]
        linked_mothers = []

        def get_new_mother_from_list():
            available_mothers = [x for x in mothers if x not in linked_mothers]
            if not available_mothers:
                return None
            mother = renpy.random.choice(available_mothers)
            linked_mothers.append(mother)
            return mother

        for i in range(4):
            mother = get_new_mother_from_list()
            other_mother = get_new_mother_from_list()

            if not mother or not other_mother:
                break

            town_relationships.update_relationship(mother, other_mother, "Sister")
            for cousin in town_relationships.get_existing_children(mother):
                town_relationships.update_relationship(other_mother, cousin, "Niece", "Aunt")
                for other_cousin in town_relationships.get_existing_children(other_mother):
                    town_relationships.update_relationship(cousin, other_cousin, "Cousin")
                    town_relationships.update_relationship(mother, other_cousin, "Niece", "Aunt")
        return

    def generate_random_sisters():
        linked_sisters = []

        def get_new_sister_from_list():
            no_family = [x for x in all_people_in_the_game(excluded_people = unique_character_list) if x.age < 30 and len(town_relationships.get_relationship_type_list(x, types = ["Mother", "Daughter", "Sister", "Cousin", "Niece", "Aunt", "Grandmother", "Granddaughter"])) == 0]
            available_sisters = [x for x in no_family if x not in linked_sisters]
            if not available_sisters:
                return None
            sister = renpy.random.choice(no_family)
            linked_sisters.append(sister)
            return sister

        def update_sister_relationship(sister, other_sister):
            town_relationships.update_relationship(sister, other_sister, "Sister")
            # when not married, their last names should be identical
            if other_sister.relationship != "Married" and sister.relationship != "Married":
                other_sister.last_name = sister.last_name

        for i in range(4):
            sister = get_new_sister_from_list()
            other_sister = get_new_sister_from_list()

            if not sister or not other_sister:
                break

            update_sister_relationship(sister, other_sister)

        return

label activate_generic_personality(stack):
    python:
        create_unique_character_list()

        for i in __builtin__.range(2):
            create_bimbo()

        # create two random people with the alpha personality (they have a very low chance of being created at random)
        for i in __builtin__.range(3):
            create_alpha_personality()

        # add two random hookers to the game (on start of game)
        for i in __builtin__.range(3):
            create_hooker()

        update_main_character_actions()

        update_characters()

        generate_random_mothers_and_daughters()

        generate_random_sisters_cousins_nieces()

        generate_random_sisters()

        setup_progression_scenes()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_generic_personality(stack):
    python:
        create_unique_character_list()

        update_main_character_actions()

        setup_progression_scenes()

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
