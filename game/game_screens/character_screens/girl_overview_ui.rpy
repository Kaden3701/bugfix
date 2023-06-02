screen person_info_detailed(person):
    add paper_background_image
    modal True
    zorder 100

    default hr_base = human_resource_potential_stat(person)
    default market_base = marketing_potential_stat(person)
    default research_base = research_potential_stat(person)
    default prod_base = production_potential_stat(person)
    default supply_base = supply_potential_stat(person)
    default master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
    default relationship_list = sorted(town_relationships.get_relationship_type_list(person, visible = True), key = lambda x: x[0].name)
    default visible_roles = ", ".join([x.role_name for x in person.special_role if not x.hidden])
    default person_portrait = person.build_person_portrait()
    default person_job_info = person_info_ui_get_job_title(person)
    default fertility_info = "{}%".format(__builtin__.round(person.effective_fertility, 1))
    if person.fertility_percent <= -100: # infertile
        $ fertility_info = "Infertile"
    default fertility_peak_day = str(person.ideal_fertile_day + 1)
    default pregnancy_chance = str(__builtin__.round(person.pregnancy_chance, 1))
    default known_days = str(day - person.event_triggers_dict.get("birth_control_known_day", 0))
    default obedience_info = get_obedience_string(person.obedience)
    default personality_info = person.personality.base_personality_prefix.capitalize()
    default novelty_info = str(person.novelty)
    default height_info = height_to_string(person.height)
    if isinstance(person.hair_colour, list) and isinstance(person.hair_colour[0], basestring):
        default hair_info = person.hair_colour[0].title()
    else:
        default hair_info = ""
    if isinstance(person.eyes, list) and isinstance(person.eyes[0], basestring):
        default eyes_info = person.eyes[0].title()
    else:
        default eyes_info = ""
    default desired_salary = person.calculate_base_salary()
    default desired_stripper_salary = calculate_stripper_salary(person)

    vbox:
        spacing 25
        xalign 0.5
        xanchor 0.5
        yalign 0.2
        frame:
            xsize 1750
            ysize 120
            padding (0, 10)
            align (.5, .5)
            background "#1a45a1aa"
            hbox:
                spacing 60
                imagebutton:
                    offset (0, -20)
                    idle person_portrait at zoom(.65)
                    xysize (465, 120)
                fixed:
                    xsize (670 if persistent.pregnancy_pref > 0 else 1270)
                    vbox:
                        hbox:
                            text format_titles(person) style "menu_text_style" size 30 xalign 0.5 yalign 0.5 yanchor 0.5 color person.char.who_args["color"] font person.char.what_args["font"]
                            use favourite_toggle_button(person)
                        text "Job: [person_job_info]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5
                        if visible_roles:
                            text "Special Roles: [visible_roles]" style "menu_text_style" xalign 0.5 yalign 0.5 yanchor 0.5

                if isinstance(person, Person) and persistent.pregnancy_pref > 0:
                    vbox:
                        xsize 350
                        if person.knows_pregnant:
                            text "Pregnant: Yes" style "menu_text_style"
                            if day < person.pregnancy_show_day:
                                text "- Visible Day: " + str(person.pregnancy_show_day) style "menu_text_style"
                            elif day < person.pregnancy_due_day:
                                text "- Delivery Day: " + str(person.pregnancy_due_day) style "menu_text_style"
                        elif person.has_role(clone_role):
                            text "Fertility: Sterile" style "menu_text_style"
                        elif person.fertility_percent <= -100:
                            text "Fertility: Infertile" style "menu_text_style"
                        else:
                            if persistent.pregnancy_pref > 0:
                                text "Fertility: [fertility_info]" style "menu_text_style"
                            if not person.event_triggers_dict.get("birth_control_status", None) is None and person.on_birth_control:
                                text "BirthControl: [person.birthcontrol_efficiency]%" style "menu_text_style"
                            if persistent.pregnancy_pref >= 2:
                                text "Monthly Peak Day: [fertility_peak_day]" style "menu_text_style"
                            if persistent.pregnancy_pref > 0 and not person.event_triggers_dict.get("birth_control_status", None) is None:
                                text "Pregnancy chance: [pregnancy_chance]%" style "menu_text_style"

                    vbox:
                        xsize 350
                        if person.has_role(clone_role) or person.fertility_percent <= -100:
                            pass
                        elif person.knows_pregnant:
                            text "Birth Control: No" style "menu_text_style"
                        elif person.event_triggers_dict.get("birth_control_status", None) is None:
                            text "Birth Control: Unknown" style "menu_text_style"
                        else:
                            hbox:
                                text "Birth Control:" style "menu_text_style"
                                vbox:
                                    text ("Yes" if person.on_birth_control else "No") style "menu_text_style"
                                    text "Known [known_days] days ago" size 12 style "menu_text_style"
                        use serum_tolerance_indicator(person)

        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Status and Info" style "serum_text_style_header"
                    text "Happiness: [person.happiness]" style "menu_text_style"
                    text "Sluttiness: [person.sluttiness]%" style "menu_text_style"
                    text "Obedience: [person.obedience] {image=triskelion_token_small} [obedience_info]" style "menu_text_style"
                    text "Love: [person.love]" style "menu_text_style"
                    text "Personality: [personality_info]" style "menu_text_style"
                    if person.has_role(girlfriend_role):
                        text "Relationship: Girlfriend" style "menu_text_style"
                    else:
                        text "Relationship: [person.relationship]" style "menu_text_style"
                    if person.relationship != "Single":
                        text "Significant Other: [person.SO_name]" style "menu_text_style"
                    elif person.has_role(girlfriend_role):
                        text "Significant Other: [mc.name]" style "menu_text_style"
                    if person.kids > 0:
                        text "Kids: [person.kids]" style "menu_text_style"
                    if person.is_employee:
                        text "Salary: $[person.salary]/day" style "menu_text_style"
                    if  person.is_strip_club_employee:
                        text "Club Salary: $[person.stripper_salary]/day" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Characteristics" style "serum_text_style_header"
                    text "Intelligence: [person.int]" style "menu_text_style"
                    text "Focus: [person.focus]" style "menu_text_style"
                    text "Charisma: [person.charisma]" style "menu_text_style"
                    text "Age: [person.age]" style "menu_text_style"
                    text "Cup size: [person.tits]" style "menu_text_style"
                    text "Height: [height_info]" style "menu_text_style"
                    text "Hair: [hair_info]" style "menu_text_style"
                    text "Eyes: [eyes_info]" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Work Skills" style "serum_text_style_header"
                    text "Human Resources: [person.hr_skill]" style "menu_text_style"
                    text "Marketing: [person.market_skill]" style "menu_text_style"
                    text "Research & Development: [person.research_skill]" style "menu_text_style"
                    text "Production: [person.production_skill]" style "menu_text_style"
                    text "Supply Procurement: [person.supply_skill]" style "menu_text_style"
                    text "Work Experience Level: [person.work_experience]" style "menu_text_style"
                    if person.is_employee or person.is_intern:
                        textbutton "Review Duties: " + str(len(person.duties)) + "/" + str(person.work_experience):
                            style "textbutton_style"
                            text_style "menu_text_style"
                            action Show("set_duties_screen", None, person, allow_changing_duties = False, show_available_duties = True, hide_on_exit = True)

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Sex Skills" style "serum_text_style_header"
                    text "Foreplay Skill: {}".format(person.sex_skills["Foreplay"]) style "menu_text_style"
                    text "Oral Skill: {}".format(person.sex_skills["Oral"]) style "menu_text_style"
                    text "Vaginal Skill: {}".format(person.sex_skills["Vaginal"]) style "menu_text_style"
                    text "Anal Skill: {}".format(person.sex_skills["Anal"]) style "menu_text_style"
                    text "Novelty: [novelty_info]%" style "menu_text_style"

            frame:
                background "#1a45a1aa"
                xysize (325, 264)
                vbox xfill True:
                    text "Sex Record" style "serum_text_style_header"
                    viewport:
                        scrollbars "vertical"
                        draggable False
                        mousewheel True
                        vbox:
                            for record in sorted(person.sex_record.keys()):
                                text "[record]: " + str(person.sex_record[record]) style "menu_text_style"

        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Loves" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, 2)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Likes" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, 1)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Dislikes" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, -1)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Hates" style "serum_text_style_header"
                    use opinion_list(master_opinion_dict, -2)

            frame:
                background "#1a45a1aa"
                xysize (325, 400)
                vbox xfill True:
                    text "Other Relations" style "serum_text_style_header"
                    if len(relationship_list) > 10:
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                for relationship in relationship_list:
                                    text "[relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"
                    else:
                        for relationship in relationship_list:
                            text "[relationship[0].name] [relationship[0].last_name] [[[relationship[1]]]" size 14 style "menu_text_style"

        hbox:
            xsize 1750
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (325, 185)
                vbox xfill True:
                    text "Job Statistics" style "serum_text_style_header"
                    text "HR: [hr_base]% Company Efficiency" style "menu_text_style"
                    text "Marketing: [market_base] Market Reach" style "menu_text_style"
                    text "Research: [research_base] Research Points" style "menu_text_style"
                    text "Production: [prod_base] Production Points" style "menu_text_style"
                    text "Supply: [supply_base] Supply Units" style "menu_text_style"
                    if person.is_employee:
                        text "Desired Salary: $[desired_salary]/day" style "menu_text_style"
                    if person.is_strip_club_employee:
                        text "Desired Salary: $[desired_stripper_salary]/day" style "menu_text_style" size 16

            frame:
                background None
                anchor [0.5,1]
                align [0.5,0]
                xysize [1000,125]
                xoffset 10
                yoffset 30
                imagebutton:
                    align [0.0,0.5]
                    auto "gui/button/choice_%s_background.png"
                    focus_mask "gui/button/choice_idle_background.png"
                    action Hide("person_info_detailed")
                textbutton "Return" align [0.17,0.5] style "return_button_style"

                if person.has_story:
                    imagebutton:
                        align [1.0,0.5]
                        auto "gui/button/choice_%s_background.png"
                        focus_mask "gui/button/choice_idle_background.png"
                        action [
                            Show("story_progress", None, person),
                            Function(draw_mannequin, person, person.outfit)
                        ]
                    textbutton "Story Progress" align [0.87,0.5] style "return_button_style"
            frame:
                background "#1a45a1aa"
                xysize (325, 185)
                xoffset 30
                vbox xfill True:
                    text "Currently Affected By" style "serum_text_style_header"
                    viewport:
                        scrollbars "vertical"
                        draggable False
                        mousewheel True
                        vbox:
                            text "Suggestibility: [person.suggestibility]%" style "menu_text_style"
                            if not person.serum_effects:
                                text "No active serums" style "menu_text_style"
                            else:
                                for serum in person.serum_effects:
                                    text "[serum.name]: " + str(serum.duration - serum.duration_counter) + " Turns Left" style "menu_text_style"

screen opinion_list(opinion_dict, preference):
    if len([x for x in opinion_dict if opinion_dict[x][0] == preference]) > 10:
        viewport:
            scrollbars "vertical"
            draggable False
            mousewheel True
            vbox:
                use opinion_list_values(opinion_dict, preference)

    else:
        use opinion_list_values(opinion_dict, preference)

screen opinion_list_values(opinion_dict, preference):
    for opinion in sorted(opinion_dict):
        if opinion_dict[opinion][0] == preference:
            if opinion_dict[opinion][1]:
                text opinion.title() style "menu_text_style"
            else:
                text "???" style "menu_text_style"
