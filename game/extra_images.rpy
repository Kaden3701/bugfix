init -100 python:
    def get_file_handle(file_name):
        found = None
        for file in renpy.list_files():
            if file_name in file:
                found = file
                break

        return found

init -20 python:
    mod_image = Image(get_file_handle("LR2Mod_idle.png"))
    mod_hover_image = Image(get_file_handle("LR2Mod_hover.png"))

    info_frame_image = Image(get_file_handle("Info_Frame_1.png"))
    goal_frame_image = Image(get_file_handle("Goal_Frame_1.png"))

    phone_background = Image(get_file_handle("LR2_Phone_Text_Dark.png"))
    text_bubble_blue = Image(get_file_handle("LR2_Text_Bubble_Blue.png"))
    text_bubble_gray = Image(get_file_handle("LR2_Text_Bubble_Gray.png"))
    text_bubble_yellow = Image(get_file_handle("LR2_Text_Bubble_Yellow.png"))

    portrait_mask_image = Image(get_file_handle("portrait_mask.png"))
    empty_image = Image(get_file_handle("empty_holder.png"))

    paper_background_image = Image(get_file_handle("Paper_Background.png"))
    science_menu_background_image = Image(get_file_handle("Science_Menu_Background.png"))
    map_background_image = Image(get_file_handle("map_background_sketch.png"))
    IT_background_image = Image(get_file_handle("IT_Background.png"))

    serum_slot_full_image = Image(get_file_handle("Serum_Slot_Full.png"))
    serum_slot_empty_image = Image(get_file_handle("Serum_Slot_Empty.png"))
    serum_slot_incorrect_image = Image(get_file_handle("Serum_Slot_Incorrect.png"))

    #Harem/girlfriend/affair
    gf_token_small_image = im.Scale(Image(get_file_handle("girlfriend.png")), 18, 18)
    renpy.image("gf_token_small", gf_token_small_image)

    paramour_token_small_image = im.Scale(Image(get_file_handle("paramour.png")), 18, 18)
    renpy.image("paramour_token_small", paramour_token_small_image)

    full_star_token_small_image = im.Scale(Image(get_file_handle("favourite_star_filled.png")), 18, 18)
    renpy.image("full_star_token_small", full_star_token_small_image)

    empty_star_token_small_image = im.Scale(Image(get_file_handle("favourite_star_empty.png")), 18, 18)
    renpy.image("empty_star_token_small", empty_star_token_small_image)

    harem_token_small_image = im.Scale(Image(get_file_handle("harem.png")), 18, 18)
    renpy.image("harem_token_small", harem_token_small_image)

    # scaled images
    taboo_break_image = im.Scale(Image(get_file_handle("taboo_lock_alt.png")), 16, 22)
    renpy.image("taboo_break", taboo_break_image)
    thumbs_up_image = im.Scale(Image(get_file_handle("thumbs_up_small.png")), 16, 22)
    renpy.image("thumbs_up", thumbs_up_image)
    thumbs_down_image = im.Scale(Image(get_file_handle("thumbs_down_small.png")), 16, 22)
    renpy.image("thumbs_down", thumbs_down_image)

    energy_token_small_image = im.Scale(Image(get_file_handle("energy_token.png")), 18, 18)
    renpy.image("energy_token_small", energy_token_small_image)

    arousal_token_small_image = im.Scale(Image(get_file_handle("arousal_token.png")), 18, 18)
    renpy.image("arousal_token_small", arousal_token_small_image)

    red_heart_token_small_image = im.Scale(Image(get_file_handle("heart/red_heart.png")), 18, 18)
    renpy.image("red_heart_token_small", red_heart_token_small_image)

    gold_heart_token_small_image = im.Scale(Image(get_file_handle("heart/gold_heart.png")), 18, 18)
    renpy.image("gold_heart_token_small", gold_heart_token_small_image)

    lust_eye_token_small_image = im.Scale(Image(get_file_handle("lust_eye.png")), 18, 18)
    renpy.image("lust_eye_token_small", lust_eye_token_small_image)

    feeding_bottle_token_small_image = im.Scale(Image(get_file_handle("feeding_bottle.png")), 18, 18)
    renpy.image("feeding_bottle_token_small", feeding_bottle_token_small_image)

    happy_small_image = im.Scale(Image(get_file_handle("happy.png")), 18, 18)
    renpy.image("happy_token_small", happy_small_image)

    underwear_small_image = im.Scale(Image(get_file_handle("underwear_token.png")), 18, 18)
    renpy.image("underwear_token_small", underwear_small_image)

    padlock_small_image = im.Scale(Image(get_file_handle("padlock.png")), 18, 18)
    renpy.image("padlock_token_small", padlock_small_image)

    triskelion_small_image = im.Scale(Image(get_file_handle("triskelion.png")), 18, 18)
    renpy.image("triskelion_token_small", triskelion_small_image)

    question_mark_small_image = im.Scale(Image(get_file_handle("question.png")), 18, 18)
    renpy.image("question_mark_small", question_mark_small_image)

    infraction_token_small_image = im.Scale(Image(get_file_handle("infraction_token.png")), 18, 18)
    renpy.image("infraction_token_small", infraction_token_small_image)

    speech_bubble_small_image = im.Scale(Image(get_file_handle("speech_bubble.png")), 18, 18)
    renpy.image("speech_bubble_token_small", speech_bubble_small_image)

    speech_bubble_exclamation_small_image = im.Scale(Image(get_file_handle("speech_bubble_exclamation.png")), 18, 18)
    renpy.image("speech_bubble_exclamation_token_small", speech_bubble_exclamation_small_image)

    vial_token_small_image = im.Scale(Image(get_file_handle("vial.png")), 18, 18)
    renpy.image("vial_token_small", vial_token_small_image)

    dna_token_small_image = im.Scale(Image(get_file_handle("dna.png")), 18, 18)
    renpy.image("dna_token_small", dna_token_small_image)

    progress_token_small_image = im.Scale(Image(get_file_handle("Progress32.png")), 18, 18)
    renpy.image("progress_token_small", progress_token_small_image)

    vial_image = Image(get_file_handle("vial.png"))
    dna_image = Image(get_file_handle("dna.png"))
    question_image = Image(get_file_handle("question.png"))
    home_image = Image(get_file_handle("home_marker.png"))


init -1:
    define mannequin_average = Image(get_file_handle("mannequin_average.png"))

    define house_background = Image(get_file_handle("Home_Background.png"))
    define apartment_background = Image(get_file_handle("Apartment_Lobby.png"))
    define bedroom_background = Image(get_file_handle("Bedroom_1.png"))
    define home_bathroom_background = Image(get_file_handle("Home_Bathroom_Background.png"))
    define old_home_shower_background = Image(get_file_handle("Home_Shower_Background_Old.jpg"))
    define home_shower_background = Image(get_file_handle("Home_Shower_Background.jpg"))
    define kitchen_background = Image(get_file_handle("Kitchen_1.png"))
    define laundry_room_background = Image(get_file_handle("Laundry_Room_Background.jpg"))
    define her_hallway_background = Image(get_file_handle("her_hallway_background.jpg"))
    define dungeon_background = Image(get_file_handle("Dungeon_Background.jpg"))
    define harem_mansion_background = Image(get_file_handle("harem_mansion.jpg"))
    define lily_bedroom_background = Image(get_file_handle("Lily_Bedroom_Background.jpg"))
    define cousin_bedroom_background = Image(get_file_handle("Cousin_Bedroom_Background.jpg"))


    define mall_background = Image(get_file_handle("Mall_Background.png"))
    define electronics_store_background = Image(get_file_handle("Electronics_Store_Background.jpg"))
    define home_improvement_store_background = Image(get_file_handle("Home_Improvement_Store_Background.jpg"))
    define bathroom_background = Image(get_file_handle("Bathroom_Background.png"))
    define sex_store_background = Image(get_file_handle("Sex_Shop_Background.jpg"))
    define gym_background = Image(get_file_handle("Gym_Background.jpg"))
    define gym_shower_background = Image(get_file_handle("Gym_Shower_Background.jpg"))
    define clothing_store_background =  Image(get_file_handle("Clothing_Store_Background.jpg"))
    define changing_room_background = Image(get_file_handle("Changing_Room_Background.jpg"))
    define office_store_background = Image(get_file_handle("Office_Store_Background.jpg"))
    define salon_background = Image(get_file_handle("Salon_Background.jpg"))
    define coffee_shop_background = Image(get_file_handle("Coffee_Shop_Background.jpg"))
    define gaming_cafe_background = Image(get_file_handle("Internet_Cafe_Background.jpg"))

    define ceo_office_background = Image(get_file_handle("CEO_Office_Background.jpg"))
    define lab_background = Image(get_file_handle("Lab_Background.png"))
    define office_background = Image(get_file_handle("Main_Office_Background.jpg"))
    define marketing_background = Image(get_file_handle("Marketing_Background.jpg"))
    define production_background = Image(get_file_handle("Production_Background.jpg"))
    define research_background = Image(get_file_handle("RandD_Background.jpg"))
    define lobby_background = Image(get_file_handle("Office_Lobby_Background.jpg"))
    define biotech_background = Image(get_file_handle("Biotech_Background.jpg"))
    define testing_room_background = Image(get_file_handle("Testing_Room_Background.jpg"))
    define clone_facility_background = Image(get_file_handle("Cloning_Facility_Background.jpg"))

    define luxury_apartment_background = Image(get_file_handle("Luxury_Apartment_Background.jpg"))
    define outside_background = Image(get_file_handle("Outside_Background.png"))

    define police_station_background = Image(get_file_handle("Police_Station_Background.jpg"))
    define police_jail_background = Image(get_file_handle("Police_Jail_Background.jpg"))

    define bar_background = Image(get_file_handle("Bar_Background.png"))
    define stripclub_background = Image(get_file_handle("Club_Background.png"))
    define bdsm_room_background = Image(get_file_handle("BDSM_Room_Background.jpg"))
    define hotel_background = Image(get_file_handle("Hotel_Lobby_Background.jpg"))
    define hotel_room_background = Image(get_file_handle("Hotel_Room_Background.jpg"))

    define campus_background = Image(get_file_handle("Campus.png"))
    define university_library_background = Image(get_file_handle("University_Library_Background.jpg"))
    define university_study_room_background = Image(get_file_handle("Study_Room_Background.jpg"))
    define student_apartment_background = Image(get_file_handle("student_apartment_background.jpg"))

    define restaraunt_background = Image(get_file_handle("Restaraunt_Background.png"))
    define fancy_restaurant_background = Image(get_file_handle("Fancy_Restaurant_Background.jpg"))
    define theater_background = Image(get_file_handle("Theater_Background.png"))
    define concert_hall_background = Image(get_file_handle("Concert_Hall_Background.jpg"))

    define standard_bedroom1_background = Image(get_file_handle("Generic_Bedroom1_Background.jpg"))
    define standard_bedroom2_background = Image(get_file_handle("Generic_Bedroom2_Background.jpg"))
    define standard_bedroom3_background = Image(get_file_handle("Generic_Bedroom3_Background.jpg"))
    define standard_bedroom4_background = Image(get_file_handle("Generic_Bedroom4_Background.jpg"))
    define prostitute_bedroom_background = Image(get_file_handle("Prostitute_Bedroom_Background.jpg"))



    image bg science_menu_background = science_menu_background_image
    image bg paper_menu_background = paper_background_image

    image serum_vial = "[vial_image.filename]"
    image question_mark = "[question_image.filename]"
    image dna_sequence = "[dna_image.filename]"
    image home_marker = "[home_image.filename]"

    python: #Some standard background progressions we can use throughout the game. Generally should be copied (use the [:] slice operator to copy the list)
        #lighting_format = [[r,g,b],[r,g,b],[r,g,b],[r,g,b],[r,g,b]]
        standard_indoor_lighting = [[0.91,0.91,0.95],[0.98,0.98,0.98],[0.98,0.98,0.98],[0.98,0.98,0.98],[0.91,0.91,0.95]]
        standard_outdoor_lighting = [[0.7,0.7,0.8],[1,1,1],[1,1,1],[1,1,1],[0.7,0.7,0.8]]
        standard_club_lighting = [[0.8,0.8,0.9], [0.8,0.8,0.9], [0.8,0.8,0.9], [0.8,0.8,0.9], [0.8,0.8,0.9]]

        dark_lighting = [[0.4,0.4,0.55],[0.4,0.4,0.55],[0.4,0.4,0.55],[0.4,0.4,0.55],[0.4,0.4,0.55]]
