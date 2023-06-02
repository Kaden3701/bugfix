init -1 python:
    biotech_body_modifications = []

init 3 python:
    def build_cloning_facility_requirement():
        if clone_facility.visible:
            return False
        if not genetic_modification_policy.is_owned:
            return False
        if not mc.business.has_funds(100000):
            return "Requires: $100,000"
        return True

    biotech_build_cloning_facility = Action("Build Cloning Facility", build_cloning_facility_requirement, "biotech_build_cloning_facility")

    def biotech_clone_person_requirement():
        if time_of_day == 4:
            return "Too late"
        elif not clone_facility.visible:
            return "Cloning facility required"
        return True

    biotech_clone_person = Action("{image=dna_sequence} Clone a person {image=gui/heart/Time_Advance.png}", biotech_clone_person_requirement, "biotech_clone_person",
        menu_tooltip = "Create a near identical clone of the targeted person")

    def biotech_modify_person_requirement():
        return True

    biotech_modify_person = Action("Modify a person", biotech_modify_person_requirement, "biotech_modify_person",
        menu_tooltip = "Modify the appearance of a person through magic, not science")

    def biotech_change_body_requirement():
        if mc.business.is_trait_researched(weight_gain) and mc.business.is_trait_researched(weight_loss):
            return True
        return "Requires: Weight Promoter traits researched"

    biotech_change_body = Action("Change body: [the_person.body_type]", biotech_change_body_requirement, "biotech_change_body",
        menu_tooltip = "Modify [the_person.title]'s body type.")
    biotech_body_modifications.append(biotech_change_body)

    def biotech_change_skin_requirement():
        if mc.business.is_trait_researched("Pigment"):
            return True
        return "Requires: Pigment Trait researched"

    biotech_change_skin = Action("Change skin: [the_person.skin]", biotech_change_skin_requirement, "biotech_change_skin",
        menu_tooltip = "Modify [the_person.title]'s skin tone.")
    biotech_body_modifications.append(biotech_change_skin)

    def biotech_change_face_requirement():
        return True

    biotech_change_face = Action("Change face: [the_person.face_style]", biotech_change_face_requirement, "biotech_change_face",
        menu_tooltip = "Modify [the_person.title]'s face style.")
    biotech_body_modifications.append(biotech_change_face)

    def biotech_change_breasts_requirement():
        if mc.business.is_trait_researched(breast_enhancement) and mc.business.is_trait_researched(breast_reduction):
            return True
        return "Requires: Breast modification traits"

    biotech_change_breasts = Action("Change breasts: [the_person.tits]", biotech_change_breasts_requirement, "biotech_change_breasts",
        menu_tooltip = "Modify [the_person.title]'s cup size.")
    biotech_body_modifications.append(biotech_change_breasts)

    def create_clone(person, clone_name, clone_last_name, clone_age):
        if clone_name is None:
            clone_name = Person.get_random_name()
        if clone_last_name is None:
            clone_last_name = Person.get_random_last_name()
        if clone_age is None:
            clone_age = person.age

        clone = make_person(name = clone_name, last_name = clone_last_name, age = clone_age, body_type = person.body_type, face_style = person.face_style, tits = person.tits, height = person.height, hair_colour = person.hair_colour, hair_style = person.hair_style, skin = person.skin, eyes = person.eyes,
            personality = person.personality, starting_wardrobe = person.wardrobe, stat_array = [person.charisma, person.int, person.focus], skill_array = [person.hr_skill, person.market_skill, person.research_skill, person.production_skill, person.supply_skill], sex_skill_array = [person.sex_skills["Foreplay"], person.sex_skills["Oral"], person.sex_skills["Vaginal"], person.sex_skills["Anal"]],
            sluttiness = person.sluttiness, obedience = person.obedience, happiness = person.happiness, love = person.love, job = unemployed_job, suggestibility = 25, work_experience = person.work_experience, start_home = clone_facility, title = "Clone", possessive_title = "Your creation", mc_title = "Creator", relationship = "Single", kids = 0, forced_sexy_opinions = [["being submissive", 2 , True]] , force_random = True)

        clone.set_schedule(clone_facility, the_times = [0,1,2,3,4])
        clone.add_role(clone_role)

        clone_facility.add_person(clone)
        return

    def build_body_type_choice_menu():
        body_types = []
        for n in Person._list_of_body_types:
            body_types.append(n)
        body_types.append("Back")
        return renpy.display_menu(simple_list_format(body_types, n, string = "Body Type: ", ignore = "Back"), True, "Choice")

    def build_skin_style_choice_menu():
        skin_styles = [x[0] for x in Person._list_of_skins]
        skin_styles.append("Back")
        return renpy.display_menu(simple_list_format(skin_styles, x[0], string = "Skin Type: ", ignore = "Back"), True, "Choice")

    def build_face_style_choice_menu():
        face_styles = []
        for face in Person._list_of_faces:
            face_styles.append(face)
        face_styles.append("Back")
        return renpy.display_menu(simple_list_format(face_styles, face, string = "Face Type: ", ignore = "Back"), True, "Choice")

    def build_cup_size_choice_menu():
        cup_sizes = [x[0] for x in Person._list_of_tits]
        cup_sizes.append("Back")
        return renpy.display_menu(simple_list_format(cup_sizes, x[0], string = "Cup Size: ", ignore = "Back"), True, "Choice")

    def build_gene_modification_menu():
        gene_modification_options = []
        for act in biotech_gene_modifications:
            gene_modification_options.append(act)
        gene_modification_options.append("Back")
        return gene_modification_options

    def build_body_modification_options_menu():
        body_modification_options = []
        for act in biotech_body_modifications:
            body_modification_options.append(act)
        body_modification_options.append("Back")
        return body_modification_options


    def cloning_facility_complete_requirement():
        return mc.business.is_open_for_business and day >= mc.business.get_event_day("cloning_facility_complete")

    def add_cloning_facility_completed_action():
        finish_day = (day + TIER_3_TIME_DELAY + renpy.random.randint(0, 5))
        mc.business.set_event_day("cloning_facility_complete", set_day = finish_day)
        cloning_facility_complete_action = Action("Cloning Facility Completed", cloning_facility_complete_requirement, "biotech_cloning_facility_completed")
        mc.business.add_mandatory_crisis(cloning_facility_complete_action)

label biotech_build_cloning_facility():
    "You decide to build the cloning facility and give a call to your contractor."
    mc.name "Good day, this is [mc.name] [mc.last_name] from [mc.business.name], I want to extend my company with a high-tech facility."
    "You go over the details with your contractor."
    python:
        mc.business.change_funds(-100000)
        ceo_office.remove_action("biotech_build_cloning_facility")
        add_cloning_facility_completed_action()
    return

label biotech_cloning_facility_completed():
    $ man_name = Person.get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The cloning facility has been completed and is now ready for inspection."
    python:
        clone_facility.visible = True
    return

label biotech_gene_modifications():
    $ act_choice = call_formated_action_choice(build_gene_modification_menu())
    if act_choice == "Back":
        return
    else:
        $ act_choice.call_action()
        $ del act_choice
    jump biotech_gene_modifications

label biotech_clone_person():
    # only known people who are not unique character or clone herself (genetic degradation too high)
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list([x for x in known_people_in_the_game(unique_character_list) if x.can_clone], "Clone Person", "Back")]
        ))
    if isinstance(_return, Person):
        $ the_person = _return
        call cloning_process() from _call_cloning_process
    return

label cloning_process(): # default to the_person when not passed as parameter
    $ the_person.draw_person()
    $ clone_name = the_person.name
    $ clone_last_name = the_person.last_name
    $ clone_age = the_person.age

label .continue_cloning_process:
    menu:
        "Give the clone a name":
            $ clone_name = str(renpy.input("Name: ", clone_name))
            $ clone_last_name = str(renpy.input("Last name: ", clone_last_name))
        "Age":
            $ clone_age = __builtin__.int(renpy.input("Age: ", clone_age))
            if clone_age < 18:
                $ clone_age = 18
        "Begin production: {image=gui/heart/Time_Advance.png}\n{color=#ff0000}{size=18}Name: [clone_name] [clone_last_name], Age: [clone_age]{/size}{/color}":
            $ create_clone(the_person, clone_name, clone_last_name, clone_age)
            "The clone has been created and is now awaiting you in the [clone_facility.formal_name]."
            call advance_time from _call_advance_time_cloning_process
            return
        "Back":
            return
    jump cloning_process.continue_cloning_process

label biotech_modify_person():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_in_the_game(), "Modify Person", "Back")]
        ))
    if isinstance(_return, Person):
        $ the_person = _return
        call modification_process() from _call_modification_process
    return

label modification_process(): # when called without specific person use the_person variable
    $ the_person.draw_person()
    $ act_choice = call_formated_action_choice(build_body_modification_options_menu())
    if act_choice == "Back":
        $ clear_scene()
        return
    else:
        $ act_choice.call_action()
        $ del act_choice
    jump modification_process

label biotech_change_body():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    $ body_choice = build_body_type_choice_menu()

    if body_choice == "Back":
        return
    else:
        $ the_person.body_type = body_choice
        $ the_person.draw_person()
        $ del body_choice
    jump biotech_change_body

label biotech_change_skin():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    $ skin_choice = build_skin_style_choice_menu()

    if skin_choice == "Back":
        return
    else:
        $ the_person.skin = skin_choice
        $ the_person.match_skin(skin_choice)
        $ the_person.draw_person()
        $ del skin_choice
    jump biotech_change_skin

label biotech_change_face():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    $ face_choice = build_face_style_choice_menu()

    if face_choice == "Back":
        return
    else:
        $ the_person.face_style = face_choice
        $ the_person.match_skin(the_person.skin)
        $ the_person.draw_person()
        $ del face_choice
    jump biotech_change_face

label biotech_change_breasts():
    #Generate a list of options from the actions that have their requirement met, plus a back button in case the player wants to take none of them.
    $ cup_choice = build_cup_size_choice_menu()

    if cup_choice == "Back":
        return
    else:
        $ the_person.tits = cup_choice
        $ the_person.draw_person()
        $ del cup_choice
    jump biotech_change_breasts
