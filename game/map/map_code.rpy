init 5 python:
    GRID_MAP_POS = [[1,1], [0,1], [2,1], [1,0], [1,2], [0,2], [2,2]]

    def mall_is_open():
        if time_of_day == 0 or time_of_day == 4:
            return False
        return True

    def gym_is_open():
        if time_of_day == 0 or time_of_day == 4:
            return False
        return True

    def sex_shop_is_open():
        if (time_of_day == 4 and day % 7 in [0,1,2,3,4]) \
            or day % 7 == 6 or time_of_day == 0:
            return False
        return True

    def university_is_open():
        if (time_of_day == 4 or time_of_day == 0 or day % 7 in [6]):
            return False
        return True

    def coffee_shop_is_open():
        if time_of_day == 0 or time_of_day == 4:
            return False
        return True

    def hair_salon_is_open():
        if day%7 in [6]:
            return False
        return True

    def downtown_bar_is_open():
        if time_of_day < 2 or day % 7 in [0]:
            return False
        return True

    def strip_club_is_open():
        if time_of_day < 2:
            return False
        return True

    def mom_office_is_open():
        if time_of_day == 0 or time_of_day > 2 or day % 7 in [5, 6]:
            return False
        return True

    def gaming_cafe_is_open():
        if not myra.event_triggers_dict.get("gaming_cafe_open", False):
            return False
        if day%7 in [2,3,4] and time_of_day in [2,3]:
            return True
        if day%7 in [5,6] and time_of_day in [1,2,3]:
            return True
        return False

    def create_tooltip_dictionary(locations):
        # start_time = time.time()
        # only create this once for each buildup
        active_progression_scene_names = [y.progression_scene_action.name for y in list_of_progression_scenes if y.progression_available()]

        result = {}
        for place in locations:
            result[place.name] = [get_location_tooltip(place)]
            result[place.name].extend(get_location_on_enter_events(place, active_progression_scene_names))

        # if debug_log_enabled: # disable log for now
        #    add_to_debug_log("Map Buildup Time: {total_time:.3f}", start_time)
        return result

    def get_location_tooltip(location):
        known_people = sorted(known_people_at_location(location), key = lambda x: x.name)
        if __builtin__.len(known_people) == 0:
            return ""
        tooltip = "You know {} {} here:\n".format(__builtin__.len(known_people), ("person" if __builtin__.len(known_people) == 1 else "people"))
        for person in known_people:
            info = []
            #added girlfriend statuses to beginning
            if person.is_favourite:
                info.append(" {image=full_star_token_small}")
            if person.has_exact_role(affair_role):
                info.append(" {image=paramour_token_small}")
            if person.has_exact_role(harem_role):
                info.append(" {image=harem_token_small}")
            if person.has_exact_role(girlfriend_role):
                info.append(" {image=gf_token_small}")
            #dialog in front of name to catch eye faster
            if any(not isinstance(x, Limited_Time_Action) for x in person.on_talk_event_list.enabled_actions(person)):
                info.append("{image=speech_bubble_exclamation_token_small}")
            elif any(not x.effect in hidden_talk_events for x in person.on_talk_event_list.enabled_actions(person)):
                info.append("{image=speech_bubble_token_small}")
            info.append(person.name)
            info.append(person.last_name)
            if person.has_role(clone_role):
                info.append("{image=dna_token_small}")
            if person.knows_pregnant:
                info.append("{image=feeding_bottle_token_small}")
            if person.serum_effects:
                info.append("{image=vial_token_small}")
            if person.infractions:
                info.append("{image=infraction_token_small}")
            if person.trance_training_availabe:
                info.append("{image=lust_eye_token_small}")
            if person.arousal_perc >= 60:
                info.append("{image=arousal_token_small}")
            info.append("\n")
            tooltip += " ".join(info)
        return tooltip

    def get_location_on_enter_events(location, scene_names):
        room_event_list = [y for x in location.people for y in x.on_room_enter_event_list.enabled_actions(x)]
        on_enter_event = any(x for x in room_event_list if not x.effect in ["work_spank_opportunity", "watching_porn_at_work"]) \
            or any(x for x in location.on_room_enter_event_list.enabled_actions())
        progression_event = any(x for x in room_event_list if x.name in scene_names)
        return (on_enter_event, progression_event)

    def get_location_tile_text(location, tt_dict):
        #added to show icons in tile text to bring attention that there is something there worth checking out etc
        known_people = known_people_at_location(location)
        return build_tile_information(known_people, location.person_count, location.formal_name, tt_dict[location.name][1], tt_dict[location.name][2])

    def get_hub_tile_text(hub):
        active_progression_scene_names = [y.progression_scene_action.name for y in list_of_progression_scenes if y.progression_available()]
        known_people = []
        total_people = 0
        has_event = False
        has_progress = False
        for location in [x for x in hub.visible_locations if x.is_accessible]:
            known_people.extend(known_people_at_location(location))
            total_people += location.person_count
            (loc_event, loc_progress) = get_location_on_enter_events(location, active_progression_scene_names)
            if loc_event:
                has_event = True
            if loc_progress:
                has_progress = True

        return build_tile_information(known_people, total_people, hub.formal_name, has_event, has_progress)

    def build_tile_information(known_people, total_people, location_name, has_event, has_progress):
        #setting the catches
        extra_info = []
        if any(x for x in known_people if x.is_favourite):
            extra_info.append("{image=full_star_token_small}")
        if any(x for x in known_people if x.has_exact_role(harem_role)):
            extra_info.append("{image=harem_token_small}")
        if any(x for x in known_people if x.has_exact_role(affair_role)):
            extra_info.append("{image=paramour_token_small}")
        if any(x for x in known_people if x.has_exact_role(girlfriend_role)):
            extra_info.append("{image=gf_token_small}")
        if any(x for x in known_people if x.knows_pregnant):
            extra_info.append("{image=feeding_bottle_token_small}")
        if any(x for x in known_people if x.trance_training_availabe):
            extra_info.append("{image=lust_eye_token_small}")
        if any(y for y in known_people if any(not isinstance(x, Limited_Time_Action) for x in y.on_talk_event_list.enabled_actions(y))):
            extra_info.append("{image=speech_bubble_exclamation_token_small}")
        if any(y for y in known_people if any(not x.effect in hidden_talk_events for x in y.on_talk_event_list.enabled_actions(y))):
            extra_info.append("{image=speech_bubble_token_small}")
        if any(x for x in known_people if x.arousal >= 60):
            extra_info.append("{image=arousal_token_small}")

        info = []
        if extra_info:
            info.append(" ".join(extra_info) + "\n")
        info.append(location_name.replace(" ", "\n", 2))
        info.append("\n({}/{})".format(len(known_people), total_people))
        if has_event:
            info.append("\n{color=#FFFF00}Event!{/color}")
        if has_progress:
            info.append("\n{image=progress_token_small}")
        return "".join(info)

    def get_current_location_hub():
        return next((x for x in list_of_hubs if mc.location in x), None)

    def change_page(page, distance, max_page):
        page += distance
        if page > max_page:
            page = 1
        if page < 1:
            page = max_page
        return page

    def calculate_hub_offsets(hub, idx, location):
        hex_offset = (75 if isinstance(hub, HomeHub) and hub.visible_count > 7 and hub.position.Y < 540 else 0)

        if not hub.is_expandable:    # location hub with 1 POI
            offset_x, offset_y = (0, 0)
        elif not isinstance(hub, HomeHub) and hub.visible_count < 8:
            # fully controlled position by location map_pos
            offset_x = (132 * location.map_pos[0])
            offset_y = (150 * location.map_pos[1]) - 75
            if location.map_pos[0] % 2 == 1:
                offset_y += 75
        elif isinstance(hub, HomeHub) and hub.visible_count < 8:
            offset_x = (132 * GRID_MAP_POS[(idx % 7)][0])
            offset_y = (150 * GRID_MAP_POS[(idx % 7)][1]) - 75
            if GRID_MAP_POS[(idx % 7)][0] % 2 == 1:
                offset_y += 75
        else:
            if hub.position.Y < 540:
                row_idx = idx // 3
                offset_x = (132 * GRID_MAP_POS[(idx % 3)][0])
                offset_y = ((150 * GRID_MAP_POS[(idx % 3)][1]) + (row_idx * 150)) - 75
                if GRID_MAP_POS[(idx % 3)][0] % 2 != 1:
                    offset_y += 75
            else:
                row_idx = 3 - (idx // 3) # inverted fill
                offset_x = (132 * GRID_MAP_POS[(idx % 3)][0])
                offset_y = ((150 * GRID_MAP_POS[(idx % 3)][1]) + (row_idx * 150)) - 75
                if GRID_MAP_POS[(idx % 3)][0] % 2 == 1:
                    offset_y += 75
        return (offset_x, offset_y - hex_offset)
