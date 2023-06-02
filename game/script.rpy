init -50 python: #Init -10 is used for all project wide imports of external resources
    import os
    import copy
    import math
    import __builtin__
    import xml.etree.ElementTree as ET
    import time
    import zipfile
    import hashlib
    import io
    from collections import defaultdict
    from collections import OrderedDict
    import unicodedata
    import sys
    from functools import partial
    import re
    import string
    from operator import attrgetter


    # all image sets available
    global supported_positions
    supported_positions = ["stand2","stand3","stand4","stand5","walking_away","kissing","doggy","missionary","blowjob","against_wall","back_peek","sitting","kneeling1","standing_doggy","cowgirl"]

    # zipfile cachingF
    global mobile_zip_dict
    mobile_zip_dict = {}
    for position in supported_positions:
        file_path = "images/character_images/" + position + ".zip"
        renpy_file = renpy.file(file_path)
        mobile_zip_dict[position] = zipfile.ZipFile(renpy_file, "r") #Cache all of the zip files so we have a single static pointer to them.

    # add zip dictionary for MOD character images
    mobile_zip_dict["character_images"] = zipfile.ZipFile(renpy.file(get_file_handle("character_images.zip")), "r") #Cache all of the zip files so we have a single static pointer to them.


    renpy.music.register_channel("sex", "sfx", loop=False, stop_on_mute=True, tight=False, file_prefix="", file_suffix="", buffer_queue=True, movie=False, framedrop=True)


    # non stored list arrays
    list_of_instantiation_labels = [] #Strings added to this list will be called at the start of the game. Use to initialize things which need their game state saved.
    list_of_instantiation_functions = [] #String added to this list will be callled as python functions at start of the game
    list_of_positions = [] # These are sex positions that the PC can make happen while having sex.
    list_of_girl_positions = [] # These are sex positions that the girl can make happen while having sex.
    list_of_strip_positions = [] # These are positions a girl can take while putting on a stirp tease for you.


#Init -5 establishes all game classes
#Init -2 is then used by all game content that will use those game classes (ie. instantiates different Crises that could be generated)
#Init 0 establishes Renpy settings, including callbacks for display code.

init -2: # Establish some platform specific stuff.
    # if renpy.macintosh:
    #     #default persistent.vren_animation = True
    #     $ persistent.vren_mac_scale = 1.0 #2.0 # Changes to the way the surface size is calculated has made a mac specific setting like this oboslete. This section is only here until I can confirm everything is working properly.
    #
    # else:
    #     default persistent.vren_animation = True
    #     $ persistent.vren_mac_scale = 1.0

    default persistent.vren_animation = True #By default animation is enabled if possible. If it's not possible because it's on mobile toggling it just does nothing for now.
    default persistent.pregnancy_pref = 0 # 0 = no content, 1 = predictable, 2 = realistic
    default persistent.vren_display_pref = "Float" # "Float" = no BG, "Frame" = Frame with coloured BG for most interactions.
    default persistent.text_effects = True
    default persistent.nearby_locations_enabled = True

    # initialize with defaults (standard)
    default GAME_SPEED = 1
    default TIER_0_TIME_DELAY = 1
    default TIER_1_TIME_DELAY = 3
    default TIER_2_TIME_DELAY = 7
    default TIER_3_TIME_DELAY = 14

init -4 python:
    default_wardrobe = wardrobe_from_xml("Master_Default_Wardrobe")
    lingerie_wardrobe = wardrobe_from_xml("Lingerie_Wardrobe")
    insta_wardrobe = wardrobe_from_xml("Insta_Wardrobe")
    business_wardrobe = wardrobe_from_xml("Business_Wardrobe") #Used in some of Mom's events when we need a business-ish outfit
    stripclub_wardrobe = wardrobe_from_xml("Stripper_Wardrobe")
    waitress_wardrobe = wardrobe_from_xml("Waitresses_Wardrobe")
    BDSM_performer_wardrobe = wardrobe_from_xml("BDSM_Wardrobe")
    nurse_wardrobe = wardrobe_from_xml("Nurse_Wardrobe")
    barista_wardrobe = wardrobe_from_xml("Barista_Wardrobe")
    manager_wardrobe = wardrobe_from_xml("Manager_Wardrobe")
    mistress_wardrobe = wardrobe_from_xml("Mistress_Wardrobe")
    prostitute_wardrobe = wardrobe_from_xml("Prostitute_Wardrobe")
    university_wardrobe = wardrobe_from_xml("University_Wardrobe")
    workout_wardrobe = wardrobe_from_xml("Workout_Wardrobe")
    maid_wardrobe = wardrobe_from_xml("Maid_Wardrobe")

init -2 python:

    day_names = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"] #Arrays that hold the names of the days of the week and times of day. Arrays start at 0.
    time_names = ["Early Morning","Morning","Afternoon","Evening","Night"]
    time_food_names = ["Breakfast", "Breakfast", "Lunch", "Dinner", "Midnight Snack"]

    global emotion_images_dict
    emotion_images_dict = {}
    for skin in ["white", "tan", "black"]:
        emotion_images_dict[skin] = {}
        for face in Person._list_of_faces:
            emotion_images_dict[skin][face] = Expression(skin + "_" + face, skin, face)

    def update_game_speed(speed):
        global GAME_SPEED, TIER_0_TIME_DELAY, TIER_1_TIME_DELAY, TIER_2_TIME_DELAY, TIER_3_TIME_DELAY

        GAME_SPEED = speed
        if speed == 0:
            TIER_0_TIME_DELAY = -1
            TIER_1_TIME_DELAY = 1
            TIER_2_TIME_DELAY = 3
            TIER_3_TIME_DELAY = 7
        elif speed == 1:
            TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 3
            TIER_2_TIME_DELAY = 7
            TIER_3_TIME_DELAY = 14
        elif speed == 2:
            TIER_0_TIME_DELAY = 1
            TIER_1_TIME_DELAY = 5
            TIER_2_TIME_DELAY = 12
            TIER_3_TIME_DELAY = 20
        else:
            TIER_0_TIME_DELAY = 2
            TIER_1_TIME_DELAY = 7
            TIER_2_TIME_DELAY = 15
            TIER_3_TIME_DELAY = 30
        return



init 0 python:
    #config.use_cpickle = False #Set to True for more useful save failure info

    #config.interact_callbacks.append(take_animation_screenshot)
    config.history_callbacks.append(text_message_history_callback) #Ensures conversations had via text are recorded properly
    # config.say_arguments_callback = text_message_say_callback #Recolours and re-fonts say statements made while having a text conversation #NOTE: NOt needed now that we properly store messages into the phone and display them from a custom screen.

    config.gl2 = True  #Required to enable the model based renderer and use shaders.
    config.scene_clears_layer_at_list = True # Restore old (renpy 7.4.3) at layer clear

    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 32
    config.cache_surfaces = False   # prevent render surfaces from being cached

    # Don't predict screens, it eats resources since every screen reloaded on a screen action (like hover)
    config.predict_screen_statements = False
    config.predict_screens = False

    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if renpy.variant("pc"):
        config.image_cache_size_mb = 768
    else:
        config.image_cache_size_mb = 384

    config.autosave_frequency = None
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.autosave_on_input = False
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_slots = 6

    config.rollback_enabled = True  # allows for smoother dialogs while skipping
    config.rollback_length = 32
    config.autoreload = False

    config.debug_text_overflow = False #If enabled finds locations with text overflow. Turns out I have a lot, kind of blows up when enabled and generates a large text file. A problem for another day.
    config.debug_image_cache = False
    config.debug = False

    # THIS IS WHAT PREVENTS IT FROM INDEXING IMAGES
    # SEE 00images.rpy for where this is created
    config.images_directory = None
    preferences.gl_tearing = True ## Prevents jittery animation with text while using advanced shaders to display images #TODO: Double check if this actually does anything anymore.

    _preferences.show_empty_window = False #Prevents Ren'py from incorrectly showing the text window in complex menu situations (which was a new bug/behaviour in Ren'py v7.2)

    global draw_layers
    draw_layers = []

    add_draw_layer("solo") # Add the main default draw layer, used for all single character displays
    add_draw_layer("extra", "solo") # Used for menu choice draw operation (person selection)
    add_draw_layer("mannequin", "screens")  # draw above screens

    config.layer_clipping["mannequin"] = [1380, 0, 540, 1080] # for outfit mannequin


label start:
    scene bg paper_menu_background with fade
    "Lab Rats 2 contains adult content. If you are not over 18 or your country's equivalent age you should not view this content."
    menu:
        "I am over 18":
            "Excellent, let's continue then."

        "I am not over 18":
            $renpy.full_restart()

    "[config.version] represents an early iteration of Lab Rats 2. Expect to run into limited content, unexplained features, and unbalanced game mechanics."
    "Would you like to view the FAQ?"
    menu:
        "View the FAQ":
            call faq_loop from _call_faq_loop_alternative_start
        "Get on with the game!":
            "You can access the FAQ from your bedroom at any time."

    "Lab Rats 2 contains content related to impregnation and pregnancy. These settings may be changed in the menu at any time."
    menu:
        "No pregnancy content\n{size=16}Girls never become pregnant. Most pregnancy content hidden.{/size}":
            $ persistent.pregnancy_pref = 0

        "Predictable pregnancy content\n{size=16}Birth control is 100%% effective. Girls always default to taking birth control.{/size}":
            $ persistent.pregnancy_pref = 1

        "Semi-Realistic pregnancy content\n{size=16}Birth control is not 100%% effective. Girls may not be taking birth control.{/size}":
            $ persistent.pregnancy_pref = 2

        "Realistic pregnancy content\n{size=16}Realistic cycles. Girls know their fertile times. Pulling out not 100%% effective. Girls don't want to get pregnant.{/size}":
            $ persistent.pregnancy_pref = 3

    "How quickly would you like stories from the game to play out? This will affect spacing between story events."
    menu:
        "Quick":
            $ update_game_speed(0)
        "Standard":
            $ update_game_speed(1)
        "Epic":
            $ update_game_speed(2)
        "Marathon":
            $ update_game_speed(3)

    $ easy_mode = False
    "Do you want to play with default game difficulty or make the game easier?"
    menu:
        "Default Game Play":
            pass
        "Easier Game Play":
            "All options for making the game easier will be applied after character creation."
            $ easy_mode = True

    "Finally, the game uses random generated characters, the mod offers you the ability to control the random generation."
    "We will now open that screen for you, so you can set it to your preferences."

    call screen generic_preference_ui()

    "That's all, the game will now initialize, this might take a moment."

    $ renpy.block_rollback()
    if persistent.stats:
        $ name = persistent.stats['name']
        $ l_name = persistent.stats['l_name']
        $ b_name = persistent.stats['b_name']
    call screen character_create_screen()
    $ return_arrays = _return #These are the stat, skill, and sex arrays returned from the character creator.
    $ setattr(persistent, "stats", {})
    $ [[persistent.stats["cha"],persistent.stats["int"],persistent.stats["foc"]], [persistent.stats["h_skill"],persistent.stats["m_skill"],persistent.stats["r_skill"],persistent.stats["p_skill"],persistent.stats["s_skill"]], [persistent.stats["F_skill"],persistent.stats["O_skill"],persistent.stats["V_skill"],persistent.stats["A_skill"]]] = _return
    $ [persistent.stats["name"],persistent.stats["l_name"],persistent.stats["b_name"]] = [store.name,store.l_name,store.b_name]


    python:
        renpy.show("Loading", layer = "solo", at_list = [truecenter], what = Image(get_file_handle("creating_world.png")))
        renpy.pause(0.5)
        renpy.game.interface.timeout(30)
        if easy_mode:
            for array in range(0, len(return_arrays)):
                for val in range(0, len(return_arrays[array])):
                    return_arrays[array][val] += 2

    call initialize_game_state(store.name,store.b_name,store.l_name,return_arrays[0],return_arrays[1],return_arrays[2], max_num_of_random = 2) from _call_initialize_game_state

    python:
        if easy_mode:
            # increased business stats
            mc.business.funds = 10000
            mc.business.supply_count = 1000
            mc.business.supply_goal = 1000
            mc.business.effectiveness_cap = 110
            mc.business.marketability = 100
            # increased player stats
            mc.max_energy = 120
            mc.free_clarity += 500
            # default unlock policies
            purchase_policy(mandatory_paid_serum_testing_policy, ignore_cost = True)
            purchase_policy(serum_size_1_policy, ignore_cost = True)
            purchase_policy(recruitment_batch_one_policy, ignore_cost = True)
            purchase_policy(recruitment_knowledge_one_policy, ignore_cost = True)
            purchase_policy(recruitment_skill_improvement_policy, ignore_cost = True)
            purchase_policy(business_size_1_policy, ignore_cost = True)
            purchase_policy(theoretical_research, ignore_cost = True)
            purchase_policy(max_attention_increase_1_policy, ignore_cost = True)
        renpy.hide("Loading", layer = "solo")

    $ renpy.block_rollback()
    menu:
        "Play introduction and tutorial":
            call tutorial_start from _call_tutorial_start

        "Skip introduction and tutorial":
            $ mc.business.event_triggers_dict["Tutorial_Section"] = False
    jump normal_start

init 0 python:
    def initialize_stephanie_in_our_business():
        mc.business.add_employee_research(stephanie)
        mc.business.hire_head_researcher(stephanie)
        stephanie.change_location(lobby)

        # setup Nano bot quest line
        fetish_serum_quest_intro = Action("Nanobot Discovery", fetish_serum_quest_intro_requirement, "fetish_serum_quest_intro_label")
        mc.business.mandatory_crises_list.append(fetish_serum_quest_intro)
        return

label normal_start:
    ## For now, this ensures reloading the game doesn't reset any of the variables.
    show screen tooltip_screen
    show screen phone_hud_ui
    show screen business_ui
    show screen goal_hud_ui
    show screen main_ui
    $ renpy.scene()
    $ bedroom.show_background()
    "It's Monday, and the first day of operation for your new business!"
    "[stephanie.title] said she would meet you at your new office for a tour."
    #TODO: Have an on_enter event for Steph if you see her the first day. Minor interaction stuff.

    #Add Stephanie to our business and flag her with a special role.

    $ initialize_stephanie_in_our_business()

    #TODO: movement overlay tutorial thing.
    jump game_loop

init 0 python:
    def build_actions_list():
        actions_list = []
        if time_of_day == 4:
            if sleep_action not in mc.location.actions: #If they're in a location they can sleep we shouldn't show this because they can just sleep here.
                location_word = "home" if not get_current_location_hub() == home_hub else "to bedroom"
                actions_list.append(["Go " + location_word + " and sleep {image=gui/heart/Time_Advance.png}{image=gui/heart/Time_Advance.png} (tooltip)It's late. Go " + location_word + " and sleep.", "Wait"])
        else:
            actions_list.append(["Wait here {image=gui/heart/Time_Advance.png}\n{color=#FFFF00}10% Extra{/color} {image=gui/extra_images/energy_token.png} (tooltip)Kill some time and wait around. Recovers more energy than working.", "Wait"])
        actions_list.append(["Go somewhere else", "Travel"])
        actions_list.append(["Check your phone", "Phone"])
        actions_list.extend(mc.location.valid_actions)
        actions_list.insert(0, "Do Something")
        return actions_list

    def build_people_list():
        people_list = []
        people_list.extend(mc.location.people)
        people_list.sort(key = sort_display_list, reverse = True)
        people_list.insert(0, "Talk to Someone")
        return people_list

    def build_nearby_location_list():
        location_list = []
        active_hub = get_current_location_hub()
        if not active_hub or not persistent.nearby_locations_enabled:
            return location_list
        nearby = [x for x in active_hub.visible_locations if x != mc.location and x.is_accessible]
        if not nearby:
            return location_list

        tt_dict = create_tooltip_dictionary(nearby)
        for loc in sorted(nearby, key = lambda x: x.formal_name):
            tooltip = get_location_tile_text(loc, tt_dict)
            location_list.append(["{} (tooltip){}".format(loc.formal_name, tooltip), loc])
        location_list.insert(0, "Go to nearby location")
        return location_list

    def main_loop_pick_talk_event(person):
        enabled_actions = person.on_talk_event_list.enabled_actions(person)

        # out of uniform takes precedence for other talk events
        out_of_uniform = next((x for x in enabled_actions if x.name == "Uniform Disobedience LTE"), None)
        if out_of_uniform:
            person.on_talk_event_list.remove(out_of_uniform)
            return out_of_uniform

        # non LTE events take priority over LTE events
        chosen = get_random_from_list([x for x in enabled_actions if not isinstance(x, Limited_Time_Action)])
        if chosen:
            person.on_talk_event_list.remove(chosen)
            return chosen

        chosen = get_random_from_list(enabled_actions)
        if chosen:
            person.on_talk_event_list.remove(chosen)
            return chosen
        return None

    def main_loop_pick_room_event(location):
        enabled_room_events = []
        for person in location.people:
            enabled_room_events.extend([[person, x] for x in person.on_room_enter_event_list.enabled_actions(person)])

        if enabled_room_events:
            chosen = get_random_from_list(enabled_room_events)
            chosen[0].on_room_enter_event_list.remove(chosen[1]) #Remove the event from their list since we will be running it.
            return chosen
        return None

    def main_loop_pick_location_event(location):
        chosen = get_random_from_list(location.on_room_enter_event_list.enabled_actions())
        if chosen:
            location.on_room_enter_event_list.remove(chosen)
            return chosen
        return None

    def main_loop_select_greeter(location):
        possible_greetings = [x for x in location.people if mc.business.get_employee_title(x) != "None"]
        return get_random_from_list(possible_greetings)

    common_variable_list = ["talk_action", "picked_option", "picked_event", "outfit", "insta_outfit", \
        "the_outfit", "new_outfit", "old_outfit", "the_uniform", "the_underwear", "person_one", "person_two", "the_person_one", \
        "the_person_two", "the_item", "the_clothing", "clothing", "the_group", "the_report", "the_trait", "the_mom", "the_action", \
        "the_aunt", "the_sister", "the_student", "the_place", "the_girl", "test_outfit", "object", "the_object", "the_start_object", \
        "the_location", "next_item", "file_path", "title_choice", "title_one", "title_two", "placeholder", \
        "formatted_title_one", "formatted_title_two", "new_title", "the_type", "the_person", "player_choice", \
        "strip_list", "first_item", "feet_ordered", "top_feet", "crisis", "the_morning_crisis", \
        "report_log", "position_choice", "object_choice", "round_choice", "start_position", "the_group", \
        "report", "the_relationship", "partner", "the_subject", "stripper", "potential_people",\
        "not_stripper", "the_student", "strip_choice", "new_pose", "picked_object", "picked_position", "picked_pose", "picked_serum", "pose_choice", "new_person" \
        "clothing", "formatted_name", "formatted_title", "hair_style_check", "pubic_style_check", "the_cause", "a_duty", \
        "text_one", "text_two", "the_goal", "the_serum", "title", "opinion_tag", "overhear_topic", "the_choice", "the_position", \
        "opinion_string", "mc_opinion_string", "talk_opinion_text", "opinion_learned", "place", "the_place", "the_taboo",
        "climax_controller", "the_watcher", "person_choice", "t", "x", "y", "z", "so_title", "a_person", "person_1", "person_2", "test_person",
        "grope_tits_slut_token", "grope_pussy_slut_token", "jerk_off_slut_token", "titfuck_slut_token", "facefuck_slut_token", "sex_token",
        "cum_tits_slut_token", "cum_face_slut_token", "cum_throat_slut_token", "cum_inside_slut_token", "sluttines_token", "slut_token",
        "jerk_token", "blowjob_token", "fuck_token", "tease_token", "red_heart_token", "blowjob_slut_token", "sex_slut_token", "anal_token",
        "scene_manager", "HR_employee_list", "the_target"]

    def main_loop_cleanup():
        clear_scene()
        # generic cleanup routine for common variable names
        for name in common_variable_list:
            if name in globals():
                del globals()[name]

    def main_loop_auto_save():
        last_save_day = mc.business.event_triggers_dict.get("last_save_day", 0)
        if day > last_save_day and time_of_day == 0:
            #renpy.notify("Saving game: " + str(day))
            renpy.force_autosave(take_screenshot = True, block = True)
            mc.business.event_triggers_dict["last_save_day"] = day


label game_loop(): ##THIS IS THE IMPORTANT SECTION WHERE YOU DECIDE WHAT ACTIONS YOU TAKE
    $ main_loop_cleanup()
    $ main_loop_auto_save()
    $ renpy.block_rollback()
    $ renpy.checkpoint()

    call screen main_choice_display(build_menu_items([build_people_list(), build_actions_list(), build_nearby_location_list()]))
    $ picked_option = _return

    if isinstance(picked_option, Person):
        $ talk_action = main_loop_pick_talk_event(picked_option)
        if talk_action:
            $ picked_option.draw_person()
            $ talk_action.call_action(picked_option)
        else:
            if picked_option.title is None:
                "You decide to approach the stranger and introduce yourself."
                $ picked_option.draw_person()
            else:
                "You approach [picked_option.title] and chat for a little bit."
                $ picked_option.draw_person()
                $ picked_option.call_dialogue("greetings")

            if picked_option.has_taboo(["underwear_nudity","bare_tits", "bare_pussy"]) and picked_option.judge_outfit(picked_option.outfit, -30): #If she's in anything close to slutty she's self-conscious enough to comment on it.
                if picked_option.vagina_visible and picked_option.has_taboo("bare_pussy") and picked_option.tits_visible and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but seems uncomfortable being naked in front of you."
                    "As you talk she seems to become more comfortable with her own nudity, even if she isn't thrilled by it."

                if picked_option.vagina_visible and picked_option.has_taboo("bare_pussy"):
                    "[picked_option.title] doesn't say anything about it, but angles her body to try and conceal her bare pussy from you."
                    "As you talk she seems to become more comfortable, even if she isn't thrilled about it."

                elif picked_option.tits_visible and picked_option.has_taboo("bare_tits"):
                    "[picked_option.title] doesn't say anything about it, but brings her arms up to try and conceal her tits."
                    if picked_option.has_large_tits:
                        "Her large chest isn't easy to hide, and she quickly realizes it's hopeless."
                    else:
                        "As you talk she seems to become more comfortable, and eventually lets her arms drop again."

                elif (picked_option.outfit.are_panties_visible or picked_option.outfit.is_bra_visible) and picked_option.has_taboo("underwear_nudity"):
                    "[picked_option.title] doesn't say anything about it, but she tries to cover up her underwear with her hands."
                    "As you talk she seems to become more comfortable, and eventually she lets her arms drop to her sides."

                $ picked_option.update_outfit_taboos()
            call talk_person(picked_option) from _call_talk_person

    elif isinstance(picked_option, Action):
        $ picked_option.call_action()

    elif isinstance(picked_option, Room):

        call change_location(picked_option) from _call_change_location_nearby #_return is the location returned from the map manager.

    elif picked_option == "Travel":
        call screen map_manager()
        if isinstance(_return, Room):
            call change_location(_return) from _call_change_location #_return is the location returned from the map manager.

    elif picked_option == "Phone":
        call browse_internet() from _call_browse_internet

    elif picked_option == "Wait":
        if time_of_day == 4:
            $ mc.change_location(bedroom)
        else:
            $ mc.change_energy(10) #Extra 10 energy gain if you spend your time waiting around
        call advance_time() from _call_advance_time_15

    jump game_loop

label change_location(the_place):
    $ renpy.scene()
    $ mc.change_location(the_place)

    if the_place.trigger_tutorial and the_place.tutorial_label is not None and mc.business.event_triggers_dict.get("Tutorial_Section",False):
        $ the_place.trigger_tutorial = False
        $ renpy.call(the_place.tutorial_label)

    $ picked_room_event = main_loop_pick_location_event(the_place)
    if picked_room_event:   # the location enter event has higher priority
        $ picked_room_event.call_action()
        $ picked_room_event = None
    elif the_place.people: #There are people in the room, let's see if there are any room events
        $ picked_event = main_loop_pick_room_event(the_place)
        if picked_event: #If there are room events to take care of run those right now.
            $ picked_event[1].call_action(picked_event[0]) #Run the action with the person as an extra argument.
        elif renpy.random.randint(0,2) == 0 and the_place in [mc.business.m_div, mc.business.p_div, mc.business.r_div, mc.business.s_div, mc.business.h_div]: #There are no room events, so generate a quick room greeting from an employee if one is around.
            $ the_greeter = main_loop_select_greeter(the_place)
            if the_greeter:
                $ the_greeter.draw_person()
                $ the_greeter.call_dialogue("work_enter_greeting")
                $ clear_scene()
                $ the_greeter = None
        $ picked_event = None
    return

init 0 python:
    def build_chat_action_list(the_person, keep_talking = True):
        chat_list = []
        for act in chat_actions:
            if keep_talking or act.is_fast:
                chat_list.append([act, the_person])

        chat_list.sort(key = sort_display_list, reverse = True)
        chat_list.insert(0,"Chat with her")
        return chat_list

    def build_specific_action_list(the_person, keep_talking = True):
        specific_actions_list = ["Say goodbye"]
        for act in specific_actions:
            if keep_talking or act.is_fast:
                specific_actions_list.append([act, the_person])

        specific_actions_list.sort(key = sort_display_list, reverse = True)
        specific_actions_list.insert(0,"Do something specific")
        return specific_actions_list

    def build_special_role_actions_list(the_person, keep_talking = True):
        special_role_actions = []
        for role in the_person.special_role:
            if the_person.job and role in the_person.job.job_roles and not the_person.event_triggers_dict.get("job_known", False):
                continue    # we don't know the job, so don't add it's specific actions
            for act in role.actions:
                if keep_talking or act.is_fast:
                    special_role_actions.append([act,the_person])

        for act in the_person.get_duty_actions():
            if keep_talking or act.is_fast:
                special_role_actions.append([act, the_person])

        for act in mc.main_character_actions: #The main character has a "role" that lets us add special actions as well.
            if keep_talking or act.is_fast:
                special_role_actions.append([act, the_person])

        special_role_actions.sort(key = sort_display_list, reverse = True)
        special_role_actions.insert(0,"Special Actions")
        return special_role_actions

label talk_person(the_person, keep_talking = True):
    $ mc.having_text_conversation = None #Just in case some event hasn't properly reset this.
    if the_person.title is None:
        $ the_person.draw_person()
        call person_introduction(the_person) from _call_person_introduction #If their title is none we assume it is because we have never met them before. We have a special introduction scene for new people.

label .continue_talk:
    $ renpy.restart_interaction()
    $ the_person.draw_person()
    call screen main_choice_display(build_menu_items([build_chat_action_list(the_person, keep_talking), build_specific_action_list(the_person, keep_talking), build_special_role_actions_list(the_person, keep_talking)]))

    $ explicit_exit = True # Use to check if the player selected an explicit "stop talking" option
    if isinstance(_return, Action):
        $ starting_time_of_day = time_of_day
        $ _return.call_action(the_person)

        if the_person in mc.location.people and time_of_day == starting_time_of_day and keep_talking:
            jump talk_person.continue_talk #If we're in the same place and time hasn't advanced keep talking to them until we stop talking on purpose.

        $ explicit_exit = False
    $ clear_scene()
    return explicit_exit

init 0 python:
    ##Work Actions##
    hr_work_action = Action("Organize your business {image=gui/heart/Time_Advance.png}",hr_work_action_requirement,"hr_work_action_description",
        menu_tooltip = "Raise business efficiency, which drops over time based on how many employees the business has.\n+3*Charisma + 2*Skill + 1*Intelligence + 5 Efficiency.")
    research_work_action = Action("Research in the lab {image=gui/heart/Time_Advance.png}",research_work_action_requirement,"research_work_action_description",
        menu_tooltip = "Contribute research points towards the currently selected project.\n+3*Intelligence + 2*Skill + 1*Focus + 10 Research Points.")
    supplies_work_action = Action("Order Supplies {image=gui/heart/Time_Advance.png}",supplies_work_action_requirement,"supplies_work_action_description",
        menu_tooltip = "Purchase serum supply at the cost of $1 per unit of supplies. When producing serum every production point requires one unit of serum.\n+3*Focus + 2*Skill + 1*Charisma + 10 Serum Supply.")
    market_work_action = Action("Find new clients {image=gui/heart/Time_Advance.png}",market_work_action_requirement,"market_work_action_description",
        menu_tooltip = "Find new clients who may be interested in buying serum from you, increasing your Market reach. Important for maintaining good Aspect prices.\n+(3*Charisma + 2*Skill +1*Focus)*5 Market Reach.")
    production_work_action = Action("Produce serum {image=gui/heart/Time_Advance.png}",production_work_action_requirement,"production_work_action_description",
        menu_tooltip = "Produce serum from raw materials. Each production point of serum requires one unit if supply, which can be purchased from your office.\n+3*Focus + 2*Skill + 1*Intelligence + 10 Production Points.")

    ##Breakthrough Actions##
    mc_breakthrough_1 = Action("Have a Breakthrough {image=gui/heart/Time_Advance.png}\n{color=#ff0000}{size=18}Requires: 500 Clarity{/size}{/color}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [1, 500], requirement_args = [1, 500],
        menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)
    mc_breakthrough_2 = Action("Have a Breakthrough {image=gui/heart/Time_Advance.png}\n{color=#ff0000}{size=18}Requires: 5000 Clarity{/size}{/color}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [2, 5000], requirement_args = [2, 5000],
        menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)
    mc_breakthrough_3 = Action("Have a Breakthrough {image=gui/heart/Time_Advance.png}\n{color=#ff0000}{size=18}Requires: 25000 Clarity{/size}{/color}", mc_breakthrough_requirement, "mc_research_breakthrough", args = [3, 25000], requirement_args = [3, 25000],
        menu_tooltip = "Put your intellect to work and unlock a new tier of research! There may be other ways to achieve this breakthrough as well", priority = 100)

    ##Complex Work Actions##
    interview_action = Action("Hire someone new {image=gui/heart/Time_Advance.png}", interview_action_requirement,"interview_action_description",
        menu_tooltip = "Look through the resumes of several candidates. More information about a candidate can be revealed by purchasing new business policies.")
    design_serum_action = Action("Design new serum {image=gui/heart/Time_Advance.png}", serum_design_action_requirement,"serum_design_action_description",
        menu_tooltip = "Combine serum traits to create a new design. Once a design has been created it must be researched before it can be put into production.")
    pick_research_action = Action("Assign Research Project", research_select_action_requirement,"research_select_action_description",
        menu_tooltip = "Pick the next research topic for your R&D division. Serum designs must be researched before they can be put into production.")
    pick_production_action = Action("Set production settings", production_select_action_requirement,"production_select_action_description",
        menu_tooltip = "Decide what serum designs are being produced. Production is divided between multiple factory lines, and automatic sell thresholds can be set to automatically flag serum for sale.")
    pick_supply_goal_action = Action("Set the amount of supply you would like to maintain", pick_supply_goal_action_requirement,"pick_supply_goal_action_description",
        menu_tooltip = "Set a maximum amount of serum you and your staff will attempt to purchase.")
    policy_purchase_action = Action("Manage business policies", policy_purchase_requirement,"policy_purchase_description",
        menu_tooltip = "New business policies changes the way your company runs and expands your control over it. Once purchased business policies are always active.")
    set_head_researcher_action = Action("Select a Head Researcher", head_researcher_select_requirement, "head_researcher_select_description",
        menu_tooltip = "Pick a member of your R&D staff to be your head researcher. A head researcher with a high intelligence score will increase the amount of research produced by the entire division.")

    trade_serum_action = Action("Access production stockpile", trade_serum_action_requirement, "trade_serum_action_description",
        menu_tooltip = "Move serum to and from your personal inventory. You can only use serum you are carrying with you.")
    sell_serum_action = Action("Sell Serum", sell_serum_action_requirement, "sell_serum_action_description",
        menu_tooltip = "Review your current stock of serum, accept and complete contracts, and check the current market prices.")
    review_designs_action = Action("Review serum designs", review_designs_action_requirement, "review_designs_action_description",
        menu_tooltip = "Shows all existing serum designs and allows you to delete any you no longer desire.")

    set_company_model_action = Action("Pick a company model", pick_company_model_requirement, "pick_company_model_description",
        menu_tooltip = "Pick one your employees to be your company model. You can run ad campaigns with your model, increasing the value of every dose of serum sold.")

    #PC Bedroom actions#
    sleep_action = Action("Sleep for the night {image=gui/heart/Time_Advance.png}{image=gui/heart/Time_Advance.png}",sleep_action_requirement,"sleep_action_description",
        menu_tooltip = "Go to sleep and advance time to the next day. Night time counts as three time chunks when calculating serum durations.", priority = 20)
    bedroom_masturbate_action = Action("Masturbate {image=gui/heart/Time_Advance.png}", bedroom_masturbate_requirement, "bedroom_masturbation",
        menu_tooltip = "Jerk off. A useful way to release Clarity, but you'll grow bored of this eventually.")

    ##Mom Bedroom Actions##
    mom_room_search_action = Action("Search [mom.title]'s room -15{image=gui/extra_images/energy_token.png}", mom_room_search_requirement, "mom_room_search_description",
        menu_tooltip = "Take a look around and see what you can find.")

    faq_action = Action("Check the FAQ",faq_action_requirement,"faq_action_description",
        menu_tooltip = "Answers to frequently asked questions about Lab Rats 2.")

    downtown_search_action = Action("Wander the streets {image=gui/heart/Time_Advance.png}", downtown_search_requirement, "downtown_search_label",
        menu_tooltip = "Spend time exploring the city and seeing what interesting locations it has to offer.")

    strip_club_show_action = Action("Watch a show", stripclub_show_requirement, "stripclub_dance",
        menu_tooltip = "Take a seat and wait for the next girl to come out on stage.")
    mom_office_person_request_action = Action("Approach the receptionist", mom_office_person_request_requirement, "mom_office_person_request",
        menu_tooltip = "The receptionist might be able to help you, if you're looking for someone.")
    import_wardrobe_action = Action("Import a wardrobe file", faq_action_requirement, "wardrobe_import",
        menu_tooltip = "Select and import a wardrobe file, adding all outfits to your current wardrobe.")

    ## Temp and Test Actions
    # test_action = Action("This is a test", faq_action_requirement, "debug_label")
    # integration_test_action = Action("Run Integration Tests", integration_test_dev_requirement, "run_integration_tests")


    ##Actions unlocked by policies##
    set_uniform_action = Action("Manage Employee Uniforms",set_uniform_requirement,"uniform_manager_loop")
    set_serum_action = Action("Set Daily Serum Doses",set_serum_requirement,"set_serum_description")

label initialize_game_state(character_name,business_name,last_name,stat_array,skill_array,_sex_array,max_num_of_random=2): #Gets all of the variables ready. TODO: Move some of this stuff to an init block?

    ##Global Variable Initialization##
    python:
        renpy.not_infinite_loop(10)
        day = 0 ## Game starts on day 0.
        time_of_day = 0 ## 0 = Early morning, 1 = Morning, 2 = Afternoon, 3 = Evening, 4 = Night

        list_of_traits = [] #List of serum traits that can be used. Established here so they play nice with rollback, saving, etc.
        list_of_nora_traits = []
        list_of_places = [] #By having this in an init block it may be set to null each time the game is reloaded, because the initialization stuff below is only called once.
        list_of_side_effects = []
        list_of_people = []
        list_of_jobs = []
        list_of_hubs = []
        stripclub_strippers = MappedList(Person, all_people_in_the_game)
        stripclub_bdsm_performers = MappedList(Person, all_people_in_the_game)
        stripclub_waitresses = MappedList(Person, all_people_in_the_game)

    #NOTE: These need to be established in a separate label to ensure they are loaded/saved correctly
    call instantiate_serum_traits() from _call_instantiate_serum_traits #Creates all of the default LR2 serum traits. TODO: Create a mod loading list that has labels that can be externally added and called here.
    call instantiate_roles() from _call_instantiate_roles
    call instantiate_side_effect_traits() from _call_instantiate_side_effect_traits
    call instantiate_business_policies() from _call_instantiate_business_policies

    python:
        ##PC's Home##
        hall = Room("home_hall", "Living Room", house_background, [make_floor(), make_wall(), make_front_door()],
            map_pos = [1,1], lighting_conditions = standard_indoor_lighting)
        bedroom = Room("mc_bedroom", "Your Bedroom", bedroom_background,
            actions = [sleep_action,bedroom_masturbate_action,faq_action],
            map_pos = [1,0], lighting_conditions = standard_indoor_lighting)
        lily_bedroom = Room("lily_bedroom", "Lily's Bedroom", bedroom_background,
            map_pos = [0,1], lighting_conditions = standard_indoor_lighting)
        mom_bedroom = Room("mom_bedroom", "Mom's Bedroom", bedroom_background,
            actions = [mom_room_search_action],
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting)
        kitchen = Room("kitchen", "Kitchen", kitchen_background, [make_wall, make_floor(), make_chair(), make_table()],
            map_pos = [1,2], lighting_conditions = standard_indoor_lighting)
        home_bathroom = Room("bathroom", "Bathroom", home_bathroom_background, home_shower_objects,
            map_pos = [2, 2], visible = False, darken = False)
        home_shower = Room("home_shower", "Home Shower", old_home_shower_background, home_shower_objects,
            public = False, visible = False, lighting_conditions = standard_indoor_lighting)
        her_hallway = Room("her_hallway", "Front hall", her_hallway_background, [make_floor(), make_wall(), make_front_door(), make_hall_carpet(), make_stairs()],
            map_pos = [1,1], public = False, visible = False, lighting_conditions = standard_indoor_lighting)
        laundry_room = Room("laundry_room", "Laundry Room", laundry_room_background, laundry_room_objects,
            public = False, visible = False, lighting_conditions = standard_indoor_lighting)
        dungeon = Room("dungeon", "Dungeon", dungeon_background, dungeon_objects, [dungeon_room_appoint_slave_action],
            map_pos = [2,1], public = False, visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        harem_mansion = Room("harem_mansion", "Harem Mansion", harem_mansion_background, harem_objects,
            public = False, map_pos =[1, 1], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC's Work##
        ceo_office = Room("ceo_office", "CEO Office", ceo_office_background, ceo_office_objects,
            actions = [policy_purchase_action, set_uniform_action, set_serum_action],
            map_pos = [1,0], public = False, visible = True, lighting_conditions = standard_indoor_lighting)
        lobby = Room("lobby", "Lobby", lobby_background, [make_floor(), make_wall(), make_reception(), make_chair(), make_front_door(), make_window()],
            map_pos = [1,1], tutorial_label = "lobby_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        office = Room("main_office", "Main Offices", office_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [hr_work_action,supplies_work_action,interview_action,pick_supply_goal_action],
            map_pos = [0,1], tutorial_label = "office_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        m_division = Room("market_div", "Marketing Division", marketing_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [sell_serum_action, market_work_action,set_company_model_action],
            map_pos = [2,1], tutorial_label = "marketing_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        rd_division = Room("rd_div", "R&D Division", research_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall(), make_examtable()],
            actions = [research_work_action,design_serum_action,pick_research_action,review_designs_action,set_head_researcher_action, mc_breakthrough_1, mc_breakthrough_2, mc_breakthrough_3],
            map_pos = [2,2], tutorial_label = "research_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        p_division = Room("prod_div", "Production Division", production_background, [make_floor(), make_desk(), make_window(), make_chair(), make_wall()],
            actions = [production_work_action,pick_production_action,trade_serum_action],
            map_pos = [0,2], tutorial_label = "production_tutorial_intro", lighting_conditions = standard_indoor_lighting, privacy_level = 2)
        clone_facility = Room("clone_facility", "Cloning Facility", clone_facility_background, [make_floor(), make_desk(), make_chair(), make_wall()],
            map_pos = [1,2], public = False, visible = False, lighting_conditions = standard_indoor_lighting, darken = False)
        work_bathroom = Room("work_bathroom", "Work Bathroom", bathroom_background, [make_wall(), make_floor(), make_toilet(), make_sink()],
            public = False, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 2, darken = False)
        testing_room = Room("testing_room", "Test Room", testing_room_background, [make_floor(), make_wall(), make_medical_table(), make_mirror()],
            map_pos = [1,2], public = False, visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        ## Downtown ##
        downtown = Room("downtown", "Downtown Streets", outside_background, [make_floor(), make_bench(), make_alley()],
            actions = [downtown_search_action], public = True,
            map_pos = [1,1], lighting_conditions = standard_outdoor_lighting, privacy_level = 3)
        downtown_bar = Room("bar", "The Downtown Distillery", bar_background, downtown_bar_objects, [downtown_bar_drink_action],
            map_pos = [2,1], public = True, visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False, accessible_func = downtown_bar_is_open)
        downtown_hotel = Room("hotel_lobby", "The Hotel", hotel_background, downtown_hotel_lobby_objects,
            map_pos = [0,1], public = True, visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        downtown_hotel_room = Room("hotel_room", "The Hotel Room", hotel_room_background, downtown_hotel_room_objects,
            map_pos = [0,2], public = False, visible = False, lighting_conditions = standard_indoor_lighting, darken = False)
        fancy_restaurant = Room("fancy_restaurant", "Restaurant", fancy_restaurant_background, [make_floor(), make_chair(), make_table()],
            map_pos = [2,2], public = False, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        coffee_shop = Room("coffee_shop", "Coffee Shop", coffee_shop_background, coffee_shop_objects, [coffee_shop_get_coffee_action],
            map_pos = [1,0], public = True, visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = coffee_shop_is_open)
        mom_office_lobby = Room("mom_office_lobby", "Vandenberg\u00A0Ltd. Lobby", lobby_background, [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            actions = [mom_office_person_request_action],
            map_pos = [0,2], lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = mom_office_is_open)
        mom_offices = Room("mom_office", "Vandenberg\u00A0Ltd. Offices", marketing_background, [make_wall(), make_floor(), make_chair(), make_desk(), make_window()],
            map_pos = [1,2], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1)

        ## MALL ##
        mall = Room("mall", "Atrium", mall_background, [make_wall(), make_floor(), make_bench()],
            map_pos = [1,1], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3)
        home_store = Room("home_store", "Home Improvement Store", home_improvement_store_background, generic_store_objects,
            map_pos = [1,0], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3)
        clothing_store = Room("clothing_store", "Sak's Clothing Store", clothing_store_background, clothing_store_objects,
            actions = [import_wardrobe_action], public = True,
            map_pos = [2,2], lighting_conditions = standard_indoor_lighting, privacy_level = 3)
        office_store = Room("supply_store", "Office Supply Store", office_store_background, generic_store_objects,
            map_pos = [2,1], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3)
        electronics_store = Room("electronics_store", "Electronics Store", electronics_store_background, generic_store_objects,
            map_pos = [0,1], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3)
        mall_salon = Room("salon", "Hair Salon", salon_background, hair_salon_objects,
            map_pos = [0,2], public = True, visible = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = hair_salon_is_open)
        gaming_cafe = Room("gaming_cafe", "Gaming Cafe", gaming_cafe_background, gaming_cafe_objects,
            actions = [gaming_cafe_grind_character_action, gaming_cafe_buy_max_level_token_action, gaming_cafe_adult_swim],
            map_pos = [1,2], public = True, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, accessible_func = gaming_cafe_is_open)

        gym = Room("gym", "Gym", gym_background, [make_wall(), make_floor(), make_bench(), make_mirror()],
            map_pos = [1,1], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        gym_shower = Room("gym_shower", "Gym Shower", gym_shower_background, gym_shower_objects,
            map_pos = [1,0], public = True, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1)

        sex_store = Room("sex_store", "Sex Store", sex_store_background, generic_store_objects,
            map_pos = [1,1], public = True, lighting_conditions = standard_indoor_lighting, privacy_level = 1)

        ## Mall supporting locations
        changing_room = Room("changing_room", "Changing Room", changing_room_background, changing_room_objects,
            public = True, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1)

        ##Other Locations##
        aunt_apartment = Room("aunt_apartment", "Living Room", house_background, [make_floor(), make_wall(), make_couch(), make_table(), make_chair(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting)
        aunt_bedroom = Room("aunt_bedroom", "Rebecca's Bedroom", standard_bedroom4_background,
            map_pos = [2,1],visible = False, lighting_conditions = standard_indoor_lighting)
        cousin_bedroom = Room("cousin_bedroom", "Gabrielle's Bedroom", cousin_bedroom_background,
            map_pos = [2,2], visible = False, lighting_conditions = standard_indoor_lighting, darken = False)

        university = Room("campus", "University Campus", campus_background, [make_grass(), make_bench()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_outdoor_lighting, privacy_level = 3)
        university_library = Room("uni_library", "Library", university_library_background, [make_floor(), make_wall(), make_table(), make_chair(), make_couch()],
            map_pos = [1,0], public = True, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1)
        university_study_room = Room("study_room", "Study Room", university_study_room_background, [make_floor(), make_wall(), make_chair(), make_table(), make_window()],
            map_pos = [1,2], public = True, visible = False, lighting_conditions = standard_indoor_lighting)

        strip_club_owner = Person.get_random_male_name()

        strip_club = Room("strip_club", strip_club_owner + "'s Gentlemen's Club", stripclub_background, [make_wall(), make_floor(), make_table(), make_chair(), make_stage(), make_pole()],
            actions = [strip_club_show_action], public = True,
            map_pos = [2,2], visible = False, lighting_conditions = standard_club_lighting, privacy_level = 1, darken = False, accessible_func = strip_club_is_open)
        bdsm_room = Room("bdsm_room", "[strip_club.formal_name] - BDSM\u00a0room", bdsm_room_background, bdsm_room_objects, [dungeon_room_appoint_slave_action],
            map_pos = [1,2], public = False, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 1, darken = False)


        police_station = Room("police_station", "Police Station", police_station_background, ceo_office_objects,
            map_pos = [0,1], public = False, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)
        police_jail = Room("police_jail", "Police Jail", police_jail_background, police_jail_objects,
            map_pos = [0,0], public = False, visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3, darken = False)

        city_hall = Room("city_hall", "City Hall", outside_background, [make_wall(), make_floor(), make_chair(), make_reception(), make_window()],
            map_pos = [1,1], visible = False, lighting_conditions = standard_indoor_lighting, privacy_level = 3)

        purgatory = Room("purgatory", "Hospital", outside_background, purgatory_objects,
            public = False, visible = False, lighting_conditions = standard_indoor_lighting)

        prostitute_bedroom = Room("Prostitute Bedroom", "Prostitute Bedroom", prostitute_bedroom_background,[make_bed(), make_wall(), make_window(), make_love_rug()],[],False,[-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_1 = Room("Generic Bedroom 1", "Bedroom", standard_bedroom1_background,[make_bed(), make_wall(), make_window(), make_floor()],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_2 = Room("Generic Bedroom 2", "Bedroom", standard_bedroom2_background,[make_bed(), make_wall(), make_window(), make_floor()],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_3 = Room("Generic Bedroom 3", "Bedroom", standard_bedroom3_background,[make_bed(), make_wall(), make_window(), make_floor()],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)
        generic_bedroom_4 = Room("Generic Bedroom 4", "Bedroom", standard_bedroom4_background,[make_bed(), make_wall(), make_window(), make_floor()],[],False, [-5,-5], visible = False, lighting_conditions = standard_indoor_lighting)

        ##PC starts in his bedroom##
        mc = MainCharacter(bedroom,character_name,last_name, Business(business_name, m_division, p_division, rd_division, office, office),stat_array,skill_array,_sex_array)

        town_relationships = RelationshipArray() #Singleton class used to track relationships. Removes need for recursive character references (which messes with Ren'py's saving methods)
        mc.generate_goals()

        ##Keep a list of all the places##
        list_of_places.append(bedroom)
        list_of_places.append(lily_bedroom)
        list_of_places.append(mom_bedroom)
        list_of_places.append(kitchen)
        list_of_places.append(hall)
        list_of_places.append(her_hallway)
        list_of_places.append(laundry_room)
        list_of_places.append(home_bathroom)
        list_of_places.append(home_shower)
        list_of_places.append(dungeon)
        list_of_places.append(harem_mansion)

        list_of_places.append(ceo_office)
        list_of_places.append(lobby)
        list_of_places.append(office)
        list_of_places.append(rd_division)
        list_of_places.append(testing_room)
        list_of_places.append(p_division)
        list_of_places.append(m_division)
        list_of_places.append(work_bathroom)

        list_of_places.append(downtown)
        list_of_places.append(downtown_bar)
        list_of_places.append(downtown_hotel)
        list_of_places.append(downtown_hotel_room)
        list_of_places.append(fancy_restaurant)

        list_of_places.append(mall)
        list_of_places.append(office_store)
        list_of_places.append(clothing_store)
        list_of_places.append(changing_room)
        list_of_places.append(sex_store)
        list_of_places.append(home_store)
        list_of_places.append(gym)
        list_of_places.append(gym_shower)
        list_of_places.append(electronics_store)
        list_of_places.append(mall_salon)
        list_of_places.append(coffee_shop)
        list_of_places.append(gaming_cafe)

        list_of_places.append(aunt_apartment)
        list_of_places.append(aunt_bedroom)
        list_of_places.append(cousin_bedroom)

        list_of_places.append(university)
        list_of_places.append(university_library)
        list_of_places.append(university_study_room)

        list_of_places.append(strip_club)
        list_of_places.append(bdsm_room)

        list_of_places.append(mom_office_lobby)
        list_of_places.append(mom_offices)

        list_of_places.append(city_hall)
        list_of_places.append(police_station)
        list_of_places.append(police_jail)
        list_of_places.append(purgatory)

        list_of_places.append(prostitute_bedroom)
        list_of_places.append(generic_bedroom_1)
        list_of_places.append(generic_bedroom_2)
        list_of_places.append(generic_bedroom_3)
        list_of_places.append(generic_bedroom_4)


        for room in [bedroom, lily_bedroom, mom_bedroom, aunt_bedroom, cousin_bedroom]:
            room.add_object(make_wall())
            room.add_object(make_floor())
            room.add_object(make_bed())
            room.add_object(make_window())

        room = None

    call instantiate_duties() from _call_instantiate_duties #Duties need to be instantiated by jobs, so do that here.
    call instantiate_jobs() from _call_instantiate_jobs #We need locations to exist before we can set up jobs, so we do that here.

    python:
        generate_patreon_character_list()
        c = 0
        while c < len(list_of_instantiation_functions):
            globals()[list_of_instantiation_functions[c]]()
            c += 1

    $ c = 0
    while c < len(list_of_instantiation_labels):
        $ renpy.not_infinite_loop(5)
        $ renpy.call(list_of_instantiation_labels[c])
        $ c += 1
    python:

        renpy.not_infinite_loop(30)
        generate_premade_list() # Creates the list with all the premade characters for the game in it. Without this we both break the policies call in create_random_person, and regenerate the premade list on each restart.
        generate_random_characters(max_num_of_random)
        add_stripclub_strippers()

        # Map Hubs for grouped map locations
        home_hub = MapHub("home", "Home", icon = "POI_House", position = Point(250, 475), locations = [hall, bedroom, lily_bedroom, mom_bedroom, kitchen, home_bathroom, dungeon, home_shower])
        aunt_home_hub = MapHub("aunt_home", "Rebecca's Apartment", icon = "POI_House", position = Point(150, 255), locations = [aunt_apartment,aunt_bedroom, cousin_bedroom])
        office_hub = MapHub("office", business_name, icon = "POI_Business", position = Point(1295, 365), locations = [lobby, m_division, p_division, rd_division, office, ceo_office, clone_facility, testing_room, work_bathroom])
        mall_hub = MapHub("mall", "Shopping Mall", icon = "POI_Mall", position = Point(640, 360), locations = [mall, home_store, clothing_store, electronics_store, office_store, mall_salon, gaming_cafe], accessible_func = mall_is_open)
        sex_shop_hub = MapHub("sex_shop", "Starbuck's Sex\u00A0Shop", icon = "POI_Sexshop", position = Point(770, 120), locations = [sex_store], accessible_func = sex_shop_is_open)
        downtown_hub = MapHub("downtown", "Downtown", icon = "POI_Downtown", position = Point(560, 800), locations = [mom_office_lobby, mom_offices, downtown_bar, coffee_shop, downtown, downtown_hotel, downtown_hotel_room, fancy_restaurant, strip_club, bdsm_room])
        plaza_hub = MapHub("plaza", "City Plaza", icon = "POI_Police", position = Point(590, 650), locations = [city_hall, police_station, police_jail])
        gym_hub = MapHub("gym", "Gym", icon = "POI_Gym", position = Point(890, 615), locations = [gym, gym_shower], accessible_func = gym_is_open)
        university_hub = MapHub("university", "University", icon = "POI_Uni", position = Point(1165, 770), locations = [university, university_library, university_study_room], accessible_func = university_is_open)
        harem_hub = MapHub("mansion", "Harem Mansion", icon = "POI_Brothel", position = Point(210, 595), locations = [harem_mansion])

        residential_home_hub = HomeHub("residential", "Residential District", icon = "District_Residential", position = Point(380, 190),
            people = [camilla, salon_manager, starbuck, emily, sakari, city_rep],
            jobs = [doctor_job, lawyer_job, architect_job, interior_decorator_job, fashion_designer_job, prostitute_job,
                pro_gamer_job, stripper_job, secretary_job, nurse_job, night_nurse_job])

        industrial_home_hub = HomeHub("industrial", "Industrial District", icon = "District_Industrial", position = Point(1050, 210),
            people = [ellie, ashley, sarah, alexia],
            jobs = [hr_job, market_job, rd_job, supply_job, production_job, head_researcher_job, office_worker_job,
                home_improvement_support_job, electronics_support_job])

        downtown_home_hub = HomeHub("downtown_home", "Downtown Apartments", icon = "District_Downtown", position = Point(300, 765),
            people = [city_rep, myra, iris],
            jobs = [unemployed_job, barista_job, bartender_job, waitress_job, hotel_receptionist_job, hotel_maid_job,
                hotel_maid_job2, hotel_chef_job, clothing_cashier_job, sex_cashier_job, electronics_cashier_job, supply_cashier_job,
                home_improvement_cashier_job, salon_hairdresser_job, store_assistant_job, store_clerk_job,
                gym_instructor_job, yoga_teacher_job, unemployed_job])

        university_home_hub = HomeHub("uni_home", "University Housing", icon = "District_ResidentialB", position = Point(1440, 820),
            people = [kaya, nora, erica],
            jobs = [university_professor_job, student_job, student_intern_market_job, student_intern_hr_job,
                student_intern_production_job, student_intern_rd_job, student_intern_supply_job])

        list_of_hubs = [home_hub, aunt_home_hub, office_hub, mall_hub, sex_shop_hub, downtown_hub, plaza_hub,
            gym_hub, university_hub, harem_hub, residential_home_hub, industrial_home_hub, downtown_home_hub, university_home_hub]

    return
