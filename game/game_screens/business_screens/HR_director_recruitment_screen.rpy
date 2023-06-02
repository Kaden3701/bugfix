init 2:

    screen HR_director_recruitment_screen(hr_director):
        $ slut_modifier = 0 if recruitment_slut_improvement_policy.is_owned else -20

        add paper_background_image
        vbox:
            frame:
                background "#000080"
                xfill True
                text "Department" style "serum_text_style_header"

            hbox:
                xalign 0.5
                textbutton "HR Dept":
                    style "textbutton_no_padding_highlight"
                    text_style "cheat_text_style"
                    xsize 250
                    if get_HR_director_tag("recruit_dept", None) == "HR":
                        background "#4f7ad6"
                        hover_background "#4f7ad6"
                    action [Function(set_HR_director_tag, "recruit_dept", "HR")]
                textbutton "Supply Dept":
                    style "textbutton_no_padding_highlight"
                    text_style "cheat_text_style"
                    xsize 250
                    if get_HR_director_tag("recruit_dept", None) == "supply":
                        background "#4f7ad6"
                        hover_background "#4f7ad6"
                    action [Function(set_HR_director_tag, "recruit_dept", "supply")]
                textbutton "Marketing Dept":
                    style "textbutton_no_padding_highlight"
                    text_style "cheat_text_style"
                    xsize 250
                    if get_HR_director_tag("recruit_dept", None) == "market":
                        background "#4f7ad6"
                        hover_background "#4f7ad6"
                    action [Function(set_HR_director_tag, "recruit_dept", "market")]
                textbutton "Research Dept":
                    style "textbutton_no_padding_highlight"
                    text_style "cheat_text_style"
                    xsize 250
                    if get_HR_director_tag("recruit_dept", None) == "research":
                        background "#4f7ad6"
                        hover_background "#4f7ad6"
                    action [Function(set_HR_director_tag, "recruit_dept", "research")]
                textbutton "Production Dept":
                    style "textbutton_no_padding_highlight"
                    text_style "cheat_text_style"
                    xsize 250
                    if get_HR_director_tag("recruit_dept", None) == "production":
                        background "#4f7ad6"
                        hover_background "#4f7ad6"
                    action [Function(set_HR_director_tag, "recruit_dept", "production")]

            frame:
                background "#000080"
                xfill True
                text "Character" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_obedience", False):
                hbox:
                    xalign 0.5
                    textbutton "Free spirited":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_obedience") and get_HR_director_tag("recruit_obedience", 0) < 90:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_obedience", 100-renpy.random.randint(11,30))]
                    textbutton "Obedient":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_obedience") and get_HR_director_tag("recruit_obedience", 0) > 110:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_obedience", 100 + renpy.random.randint(11,30))]
                    textbutton "InBetween":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_obedience") and get_HR_director_tag("recruit_obedience", 0) >= 90 and get_HR_director_tag("recruit_obedience", 0) <= 110:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_obedience", 100 + renpy.random.randint(-10,10))]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_obedience", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_obedience", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"


            frame:
                background "#000080"
                xfill True
                text "Job Focus" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_focused", False):
                hbox:
                    xalign 0.5
                    textbutton "Department Focus":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_focused") and get_HR_director_tag("recruit_focused", False):
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_focused", True)]
                    textbutton "Balanced":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_focused", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_focused", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Marital Status" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_marital", False):
                hbox:
                    xalign 0.5
                    textbutton "Married":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_marital") and get_HR_director_tag("recruit_marital", None) == "Married":
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_marital", "Married")]
                    textbutton "In a relationship":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_marital") and get_HR_director_tag("recruit_marital", None) in ["Girlfriend", "Fiancée"]:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_marital", get_random_from_list(["Girlfriend", "Fiancée"]))]
                    textbutton "Single":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_marital") and get_HR_director_tag("recruit_marital", None) == "Single":
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_marital", "Single")]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_marital", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_marital", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Sluttiness" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_slut", False):
                hbox:
                    xalign 0.5
                    textbutton "Slutty":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_slut") and get_HR_director_tag("recruit_slut", 0) >= 30 + slut_modifier:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_slut", 30 + renpy.random.randint(0, 10) + slut_modifier)]
                    textbutton "Normal":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_slut") and get_HR_director_tag("recruit_slut", 0) >= 15 + slut_modifier and get_HR_director_tag("recruit_slut", 0) < 30 + slut_modifier:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_slut", 15 + renpy.random.randint(0, 10) + slut_modifier)]
                    textbutton "Prude":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_slut") and get_HR_director_tag("recruit_slut", 0) >= slut_modifier and get_HR_director_tag("recruit_slut", 0) < 15 + slut_modifier:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_slut", renpy.random.randint(0, 10) + slut_modifier)]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_slut", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_slut", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Children" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_kids", False):
                hbox:
                    xalign 0.5
                    textbutton "Mother":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if not get_HR_director_tag("recruit_kids", None) is None and get_HR_director_tag("recruit_kids", 0) != 0:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_kids", renpy.random.randint(1,3)),
                                Function(set_HR_director_tag, "recruit_age", renpy.random.randint(25, 48))]
                    textbutton "No Children":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if not get_HR_director_tag("recruit_kids", None) is None and get_HR_director_tag("recruit_kids", 0) == 0:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_kids", 0),
                                Function(set_HR_director_tag, "recruit_age", renpy.random.randint(18, 30))]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_kids", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_kids", None),
                                Function(set_HR_director_tag, "recruit_age", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Height" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_physical", False):
                hbox:
                    xalign 0.5
                    textbutton "Tall":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_height") and get_HR_director_tag("recruit_height", 0) >= 1.05:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_height", renpy.random.randint(105, 125) / 100.0)]
                    textbutton "Short":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_height") and get_HR_director_tag("recruit_height", 0) <= 0.90:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_height", renpy.random.randint(75, 90) / 100.0)]
                    textbutton "Normal":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_height") and get_HR_director_tag("recruit_height", 0) >= 0.91 and get_HR_director_tag("recruit_height", 0) <= 1.04:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_height", renpy.random.randint(91, 104) / 100.0)]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_height", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_height", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Body" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_physical", False):
                hbox:
                    xalign 0.5
                    textbutton "Thick":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_body") and get_HR_director_tag("recruit_body", None) == "curvy_body":
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_body", "curvy_body")]
                    textbutton "Skinny":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_body") and get_HR_director_tag("recruit_body", None) == "thin_body":
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_body", "thin_body")]
                    textbutton "Normal":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_body") and get_HR_director_tag("recruit_body", None) == "standard_body":
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_body", "standard_body")]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_body", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_body", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

            frame:
                background "#000080"
                xfill True
                text "Bust" style "serum_text_style_header"

            if get_HR_director_tag("headhunter_physical", False):
                hbox:
                    xalign 0.5
                    textbutton "Busty":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_bust") and get_HR_director_tag("recruit_bust", None) in ["DDD", "E", "F","FF"]:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_bust", get_random_from_list(["DDD", "E", "F","FF"]))]
                    textbutton "Flat":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_bust") and get_HR_director_tag("recruit_bust", None) in ["AA", "A", "B"]:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_bust", get_random_from_list(["AA", "A", "B"]))]
                    textbutton "Normal":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_bust") and get_HR_director_tag("recruit_bust", None) in ["C", "D", "DD"]:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_bust", get_random_from_list(["C", "D", "DD"]))]
                    textbutton "Not Relevant":
                        style "textbutton_no_padding_highlight"
                        text_style "cheat_text_style"
                        xsize 250
                        if get_HR_director_tag("recruit_bust", None) is None:
                            background "#4f7ad6"
                            hover_background "#4f7ad6"
                        action [Function(set_HR_director_tag, "recruit_bust", None)]
            else:
                hbox:
                    xalign 0.5
                    frame:
                        xsize 500
                        text "Software Upgrade Locked" style "serum_text_style_header"

        frame:
            background None
            anchor [0.5,0.5]
            align [0.3,0.88]
            xysize [300,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action [Return(False), Hide("serum_tooltip")]
            textbutton "Cancel" align [0.5,0.5] style "return_button_style"

        if get_HR_director_tag("recruit_dept", None) is not None:
            frame:
                background None
                anchor [0.5,0.5]
                align [0.7,0.88]
                xysize [300,125]
                imagebutton:
                    align [0.5,0.5]
                    auto "gui/button/choice_%s_background.png"
                    focus_mask "gui/button/choice_idle_background.png"
                    action [Return(True), Hide("serum_tooltip")]
                textbutton "Start Recruitment" align [0.5,0.5] style "return_button_style"
