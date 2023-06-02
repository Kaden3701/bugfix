init 2:
    screen story_progress(person):
        # show_candidate(person)
        add paper_background_image
        modal True
        zorder 100

        default mannequin = person

        vbox:
            yalign 0.2
            xalign 0.4
            xanchor 0.5
            spacing 30
            frame:
                background "#1a45a1aa"
                xysize (1320, 110)
                vbox xfill True:
                    spacing 10
                    text "[person.name] [person.last_name]" xalign 0.5 style "menu_text_style" size 50 color person.char.who_args["color"] font person.char.what_args["font"]
                    text "[person.progress.story_character_description!i]" xalign 0.5 style "serum_text_style"

            hbox:
                xsize 1320
                spacing 30
                frame:
                    background "#1a45a1aa"
                    xysize (420, 420)
                    vbox xfill True:
                        text "Obedience Story Progress" style "serum_text_style_header" #Info about the persons raw stats, work skills, and sex skills
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                spacing 10
                                for _, obedience_text in sorted(person.progress.story_obedience_list.items(), key=lambda x:x[0]):
                                    text "[obedience_text!i]" style "menu_text_style"
                frame:
                    background "#1a45a1aa"
                    xysize (420, 420)
                    vbox xfill True:
                        text "Love Story Progress" style "serum_text_style_header" #Info about the persons raw stats, work skills, and sex skills
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                spacing 10
                                for _, love_text in sorted(person.progress.story_love_list.items(), key=lambda x: x[0]):
                                    text "[love_text!i]" style "menu_text_style"

                frame:
                    #$ master_opinion_dict = dict(person.opinions, **person.sexy_opinions)
                    background "#1a45a1aa"
                    xysize (420, 420)
                    vbox xfill True:
                        text "Lust Story Progress" style "serum_text_style_header" #Info about the persons loves, likes, dislikes, and hates
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                spacing 10
                                for _, lust_text in sorted(person.progress.story_lust_list.items(), key=lambda x:x[0]):
                                    text "[lust_text!i]" style "menu_text_style"
            hbox:
                xsize 1320
                spacing 60
                frame:
                    background "#1a45a1aa"
                    xysize (630, 300)
                    vbox xfill True:
                        text "Other information" style "serum_text_style_header"
                        viewport:
                            scrollbars "vertical"
                            draggable False
                            mousewheel True
                            vbox:
                                spacing 10
                                for _, other_info in sorted(person.progress.story_other_list.items(), key=lambda x: x[0]):
                                    text "[other_info!i]" style "menu_text_style"
                                if person.fetish_count == 0:
                                    text "No known fetishes" style "menu_text_style"
                                if person.has_breeding_fetish:
                                    text "Has breeding fetish" style "menu_text_style"
                                if person.has_anal_fetish:
                                    text "Has anal fetish" style "menu_text_style"
                                if person.has_cum_fetish:
                                    text "Has cum fetish" style "menu_text_style"
                                if person.has_exhibition_fetish:
                                    text "Is an exhibitionist" style "menu_text_style"
                                if person.is_girlfriend and not person.is_jealous:
                                    text "Is polyamory" style "menu_text_style"
                                elif person.is_girlfriend:
                                    text "Is monogamous" style "menu_text_style"

                if person.progress.has_teamup:
                    frame:
                        background "#1a45a1aa"
                        xysize (630, 300)
                        vbox xfill True:
                            text "Teamups" style "serum_text_style_header"
                            viewport:
                                scrollbars "vertical"
                                draggable False
                                mousewheel True
                                vbox:
                                    spacing 10
                                    xalign 0.0
                                    for teamup_info in [x for key, x in sorted(person.progress.story_teamup_list.items(), key=lambda x:x[0]) if isinstance(x, list) and len(x) == 2]:
                                        if isinstance(teamup_info[0], Person) and teamup_info[0] in known_people_in_the_game() and teamup_info[0].has_story:
                                            hbox:
                                                spacing 10
                                                textbutton "[teamup_info[0].fname]":
                                                    xsize 120
                                                    action [
                                                        Function(person.hide_person, draw_layer = "mannequin"),
                                                        Function(teamup_info[0].draw_person, draw_layer = "mannequin", show_person_info = False, wipe_scene = False),
                                                        Show("story_progress", None, teamup_info[0])
                                                    ]
                                                    style "textbutton_style"
                                                    text_style "serum_text_style"
                                                text "[teamup_info[1]!i]" style "menu_text_style"
            frame:
                background None
                anchor (0.5, 1.0)
                align (0.5, 1.0)
                xysize (500, 125)
                imagebutton:
                    align (0.5, 0.5)
                    auto "gui/button/choice_%s_background.png"
                    focus_mask "gui/button/choice_idle_background.png"
                    action [
                        Function(hide_mannequin),
                        (Hide("story_progress"))
                    ]
                textbutton "Return" align (0.5, 0.5) style "return_button_style"
