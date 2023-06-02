init 2 python: # Declare variables to use
    list_of_instantiation_functions.append("create_salon_manager_character")

    # Note that the class Room have a bunch of useful variables already for restricting access, adding objects etc.
    def salon_requirement():
        if day%7 == 6: # Can be removed
            return "Closed on Sundays"

        elif time_of_day == 0:
            return "Opens in the morning"

        elif time_of_day == 4: # Can be removed
            return "Closed for the night"

        elif not mc.business.has_funds(salon_total_cost): # $60 for hair cut, $30 for dye. You wont be spending your last money on haircuts.
            return "Requires $[salon_total_cost]"
        else:
            return True

    def create_salon_manager_character():
        salon_wardrobe = wardrobe_from_xml("Salon_Wardrobe")
        # Place the stylist character so it is in a room in the world.
        ophelia_base_outfit = Outfit("Ophelia's base accessories")
        the_eye_shadow = light_eye_shadow.get_copy()
        the_eye_shadow.colour = [.15, .15, .15, 0.95]
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15,.15,.15,1.0]
        the_lipstck = lipstick.get_copy()
        the_lipstck.colour = [.5, .28, .37, 0.95]
        ophelia_base_outfit.add_accessory(the_eye_shadow)
        ophelia_base_outfit.add_accessory(the_glasses)
        ophelia_base_outfit.add_accessory(the_lipstck)

        global salon_manager_role
        salon_manager_role = Role("Salon Manager", [cut_hair_action, ophelia_ex_bf_plan_pics, ophelia_talk_about_candace], hidden = True)
        salon_job = Job("Hair Stylist", salon_manager_role, mall_salon, work_times = [1,2,3])
        salon_job.schedule.set_schedule(mall_salon, the_days = 5, the_times = [1,2])

        global salon_manager
        salon_manager = make_person(name = "Ophelia", last_name = "von Friseur", age = renpy.random.randint(26,35), body_type = "thin_body", skin="tan", face_style = "Face_11", hair_colour = ["barn red", [.486, .039, .007, 1]], hair_style = messy_hair,
            personality = salon_manager_personality, starting_wardrobe = salon_wardrobe, eyes="green", sex_skill_array = [1,5,3,1], sluttiness = 10,
            possessive_title = "Your Stylist", relationship = "Single", force_random = True, base_outfit = ophelia_base_outfit, type = 'story',
                forced_opinions = [
                ["dark chocolate", 2, False],
                ["hiking", 2, False],
                ["the colour red", 2, False],
                ["the colour yellow", 1, False]],
                forced_sexy_opinions = [
                ["cum facials", 2, False], # it's good for the skin
                ["giving blowjobs", 2, False],
                ["skimpy outfits", 1, False], # Fashion forward
            ])

        # create home for salon manager
        salon_manager.change_job(salon_job, job_known = True)
        salon_manager.generate_home()
        salon_manager.home.add_person(salon_manager)
        return

    def ophelia_foreplay_position_filter(foreplay_positions):
        return True

    def ophelia_oral_position_filter(oral_positions):
        if ophelia_get_special_bj_unlocked():
            filter_out = [blowjob, deepthroat, skull_fuck]
            return not oral_positions[1] in filter_out
        return False

    def ophelia_vaginal_position_filter(vaginal_positions):
        return ophelia_get_first_date_finished()

    def ophelia_anal_position_filter(anal_positions):
        return ophelia_is_over_her_ex_day() > 0

    def ophelia_unique_sex_positions(person, prohibit_tags = []):
        positions = []
        if ophelia_get_special_bj_unlocked() and "Oral" not in prohibit_tags:
            positions.append([Ophelia_blowjob, 1])
        return positions

    def hair_salon_mod_initialization(self):
        # salon_manager.event_triggers_dict["introduced"] = 0
        # salon_manager.event_triggers_dict["day_met"] = -1
        # salon_manager.event_triggers_dict["coworker_overhear"] = 0
        # salon_manager.event_triggers_dict["chocolates_received"] = 0
        # salon_manager.event_triggers_dict["chocolate_gift_unlocked"] = 0
        # salon_manager.event_triggers_dict["day_of_last_chocolate"] = -1
        # salon_manager.event_triggers_dict["secret_admirer_known"] = 0
        # salon_manager.event_triggers_dict["ex_phone_overhear"] = 0
        # salon_manager.event_triggers_dict["pics_to_ex_plan_made"] = 0    #0 = not started. 1 = talked to her, but without resolution. 2 = pics planned. 3 = pics made
        # salon_manager.event_triggers_dict["pics_to_ex_sent"] = 0  #0 =incomplete, 1 = complete, not followed up with. 2 = complete and followed up with
        # salon_manager.event_triggers_dict["special_bj_unlock"] = 0
        # salon_manager.event_triggers_dict["first_date_planned"] = 0 #Misnomer... oh well...
        # salon_manager.event_triggers_dict["first_date_finished"] = 0
        # salon_manager.event_triggers_dict["salon_and_spa_planned"] = 0
        # salon_manager.event_triggers_dict["salon_and_spa_finished"] = 0
        # salon_manager.event_triggers_dict["talk_about_candace"] = 0
        # salon_manager.event_triggers_dict["help_candace"] = 0
        # salon_manager.event_triggers_dict["full_style_state"] = 0
        # salon_manager.event_triggers_dict["offers_full_style"] = False
        salon_manager.event_triggers_dict["ex_name"] = Person.get_random_male_name()

        # add haircut action to mall salon
        mall_salon.add_action(self)
        salon_manager.add_unique_on_room_enter_event(salon_introduction_action)
        return

    def salon_introduction_action_requirement(the_person):
        if not "mall_salon" in globals():
            return False
        if the_person.is_at_work:    # only trigger event when ophelia is there
            return True
        return False

    salon_action = ActionMod("Schedule a haircut {image=gui/heart/Time_Advance.png}", salon_requirement, "salon_label", initialization = hair_salon_mod_initialization,
        menu_tooltip = "Change a person's hair style and color.", category="Mall")

    salon_introduction_action = Action("Ophelia's Hair Salon", salon_introduction_action_requirement, "salon_manager_greetings", menu_tooltip = "Ophelia's Hair Salon")
