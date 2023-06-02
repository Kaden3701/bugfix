init 2 python:
    def restore_hair_style(person, hair_style, pubes_style):
        person.hair_style = hair_style
        person.hair_colour = hair_style.colour
        person.pubes_style = pubes_style
        return

    def set_hair_style(person, new_clothing):
        cs = renpy.current_screen()
        person.hair_style = new_clothing.get_copy()

        if cs:
            person.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]

    # SET PUBIC STYLE Clothing ITEM

    def set_pubic_style(person, new_clothing):
        cs = renpy.current_screen()
        person.pubes_style = new_clothing.get_copy()

        if cs:
            person.hair_colour = [cs.scope["selected_hair_colour_name"], [cs.scope["current_r"], cs.scope["current_g"], cs.scope["current_b"], cs.scope["current_a"]]]


screen hair_creator(person, old_hair_style, old_pubes_style): ##Pass the person and the variables holding the current hair style
    modal True
    default category_selected = "Hair Style"
    default selected_style = person.hair_style

    default use_current_outfit = person.outfit
    default use_nude = Outfit("Nude")

    #default valid_categories = ["Hair Style", "Pubic Style"] #Holds the valid list of categories strings to be shown at the top.
    default categories_mapping = { # list of clothing | Apply method | Valid / sensitive check | nudity switch | tooltip string
        "Hair Style": [[x for x in hair_styles if not x in [bald_hair]] , set_hair_style, True, use_current_outfit],
        "Pubic Style": [pube_styles, set_pubic_style, ophelia_person_wants_pubic_hair_included(person), use_nude] #Set the False bool to either true or a custom requirement function
    }

    default bar_select = 0 # 0 is nothing selected, 1 is red, 2 is green, 3 is blue, and 4 is alpha

    default selected_colour = "colour" #If secondary we are alternating the pattern colour. When changed it updates the colour of the clothing item. Current values are "colour" and "colour_pattern"
    default current_r = selected_style.colour[0]
    default current_g = selected_style.colour[1]
    default current_b = selected_style.colour[2]
    default current_a = selected_style.colour[3]

    default selected_hair_colour_name = person.hair_colour[0]
    default selected_hair_colour = selected_style.colour
    # default selected_style = person.hair_style
    #
    # default selected_pube_style = person.pubes_style

    hbox: #The main divider between the new item adder and the current outfit view.
        xpos 15
        yalign 0.5
        yanchor 0.5
        spacing 15
        frame:
            background "#0a142688"
            padding (20,20)
            xysize (880, 1015)
            hbox:
                spacing 15
                vbox: #Categories select on far left
                    spacing 15
                    for category in [x for x in categories_mapping if categories_mapping[x][2]]:
                        textbutton "[category]":
                            style "textbutton_style"
                            text_style "textbutton_text_style"
                            if category == category_selected:
                                background "#4f7ad6"
                                hover_background "#4f7ad6"
                            else:
                                background "#1a45a1"
                                hover_background "#3a65c1"
                            text_align(0.5,0.5)
                            text_anchor(0.5,0.5)
                            if __builtin__.len(categories_mapping[category]) > 4 and categories_mapping[category][2] is False:
                                tooltip categories_mapping[category][4]
                            xysize (220, 60)
                            action [
                                SetScreenVariable("category_selected", category),
                                SetScreenVariable("selected_style", None),
                                SetScreenVariable("selected_colour", "colour"),
                                SetField(person, "outfit", categories_mapping[category][3]),
                                Function(person.clean_cache),
                                Function(person.draw_person, show_person_info = False)
                            ]
                    # textbutton old_hair_colour:
                    #     style "textbutton_style"
                    #     text_style "textbutton_text_style"
                    #     xysize (220, 60)
                    # textbutton old_hair_style.name:
                    #     style "textbutton_style"
                    #     text_style "textbutton_text_style"
                    #     xysize (220, 60)

                vbox:
                    spacing 15
                    viewport:
                        ysize 480
                        xminimum 605
                        scrollbars "vertical"
                        mousewheel True
                        frame:
                            xsize 620
                            yminimum 480
                            background "#0a142688"
                            vbox:
                                if category_selected in categories_mapping:
                                    #    $ valid_check = categories_mapping[category_selected][1]
                                    #    $ apply_method = categories_mapping[category_selected][2]
                                    #    $ cloth_list_length = __builtin__.len(categories_mapping[category_selected][0])
                                    for style_item in sorted(categories_mapping[category_selected][0], key = lambda x: x.name):
                                        textbutton "[style_item.name]":
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                            tooltip ""
                                            xfill True
                                            sensitive True

                                            action [
                                                SetField(style_item, "colour", [current_r, current_g, current_b, current_a]),
                                                SetScreenVariable("selected_colour", "colour"),
                                                SetScreenVariable("selected_style", style_item.get_copy()),
                                                Function(categories_mapping[category_selected][1], person, style_item),
                                                Function(person.clean_cache),
                                                Function(person.draw_person, show_person_info = False)
                                            ]

                    frame:
                        #THIS IS WHERE SELECTED ITEM OPTIONS ARE SHOWN
                        xysize (605, 480)
                        background "#0a142688"
                        vbox:
                            spacing 10
                            if selected_style:
                                text "[selected_style.name]" style "textbutton_text_style"

                                hbox:
                                    spacing -5 #We will manually handle spacing so we can have our colour predictor frames
                                    textbutton "Primary Colour":
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        if selected_colour == "colour":
                                            background "#4f7ad6"
                                            hover_background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                            hover_background "#3a65c1"
                                        sensitive True
                                        tooltip ""
                                        action NullAction()

                                    frame:
                                        background Color(rgb=(current_r, current_g, current_b, current_a))
                                        xysize (45,45)
                                        yanchor 0.5
                                        yalign 0.5

                                    textbutton "Dye Hair":
                                        style "textbutton_style"
                                        text_style "textbutton_text_style"
                                        background "#1a45a1"
                                        hover_background "#3a65c1"
                                        sensitive True
                                        tooltip ""
                                        xoffset 20
                                        action [
                                            SetField(selected_style, "colour", [current_r, current_g, current_b, current_a]),
                                            SetScreenVariable("selected_hair_colour", [current_r, current_g, current_b, current_a]),
                                            SetField(person, "hair_colour", [selected_hair_colour_name, [current_r, current_g, current_b, current_a]]),
                                            Function(categories_mapping[category_selected][1], person, selected_style),
                                            Function(person.clean_cache),
                                            Function(person.draw_person, show_person_info = False)
                                        ]

                                hbox:
                                    spacing 10
                                    vbox:
                                        text "Red" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 1:
                                                frame:
                                                    input default current_r length 4 changed colour_changed_r allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",1)
                                                    text "%.2f" % current_r style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_r", 1.0)  xsize 120 ysize 45 style style.slider #unhovered #SetScreenVariable("current_r",__builtin__.round(current_r,2))
                                    vbox:
                                        text "Green" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 2:
                                                frame:
                                                    input default current_g length 4 changed colour_changed_g allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",2)
                                                    text "%.2f" % current_g style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_g", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_g",__builtin__.round(current_g,2))
                                    vbox:
                                        text "Blue" style "textbutton_text_style"
                                        hbox:
                                            if bar_select == 3:
                                                frame:
                                                    input default current_b length 4 changed colour_changed_b allow ".0123456789" style "menu_text_style"
                                                    xsize 70
                                                    ysize 50
                                            else:
                                                button:
                                                    background "#888888"
                                                    action SetScreenVariable("bar_select",3)
                                                    text "%.2f" % current_b style "menu_text_style"
                                                    xsize 70
                                                    ysize 50

                                            bar value ScreenVariableValue("current_b", 1.0) xsize 120 ysize 45 style style.slider #unhovered SetScreenVariable("current_b",__builtin__.round(current_b,2))

                                text "Transparency: " style "menu_text_style"
                                hbox:
                                    spacing 20
                                    button:
                                        if current_a == 1.0:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        hover_background "#3a65c1"
                                        text "Normal" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 1.0)

                                    button:
                                        if current_a == 0.95:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        hover_background "#3a65c1"
                                        text "Sheer" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.95)

                                    button:
                                        if current_a == 0.8:
                                            background "#4f7ad6"
                                        else:
                                            background "#1a45a1"
                                        hover_background "#3a65c1"
                                        text "Translucent" style "menu_text_style" xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5
                                        xysize (120, 40)
                                        action SetScreenVariable("current_a", 0.8)
                                for block_count, hair_colour_list in __builtin__.enumerate(split_list_in_blocks(Person._list_of_hairs, 10)):
                                    hbox:
                                        spacing 5
                                        xalign 0.5
                                        xanchor 0.5
                                        yanchor (block_count * .1)
                                        for count, hair_colour in __builtin__.enumerate(hair_colour_list):
                                            frame:
                                                background "#aaaaaa"
                                                button:
                                                    background Color(rgb=(hair_colour[1][0], hair_colour[1][1], hair_colour[1][2]))
                                                    xysize (40,40)
                                                    sensitive True
                                                    tooltip ""
                                                    action [
                                                        SetScreenVariable("selected_hair_colour_name", hair_colour[0]),
                                                        SetScreenVariable("selected_hair_colour", hair_colour[1]),
                                                        SetField(selected_style, "colour", [hair_colour[1][0], hair_colour[1][1], hair_colour[1][2], hair_colour[1][3]]),
                                                        SetScreenVariable("current_r", hair_colour[1][0]),
                                                        SetScreenVariable("current_g", hair_colour[1][1]),
                                                        SetScreenVariable("current_b", hair_colour[1][2]),
                                                        SetScreenVariable("current_a", hair_colour[1][3]),
                                                        SetField(person, "hair_colour", hair_colour),
                                                        Function(categories_mapping[category_selected][1], person, selected_style),
                                                        Function(person.clean_cache),
                                                        Function(person.draw_person, show_person_info = False)
                                                    ]
                                                    # We use a fixed pallette of hair colours
        vbox:
            spacing 15
            xalign 0.5
            frame:
                xysize (440, 500)
                background "#0a142688"
                padding (20,20)
                vbox:
                    frame:
                        background "#000080"
                        xsize 400
                        text "Current Hair Style" xalign 0.5 style "textbutton_text_style"
                    frame:
                        xfill True
                        yfill True
                        background None
                        vbox:
                            spacing 5 #TODO: Add a viewport here too.
                            frame:
                                background Color(rgb = (selected_hair_colour[0], selected_hair_colour[1], selected_hair_colour[2]))
                                xysize (390, 40)
                                xalign 0.5
                                yalign 0.0
                                if selected_style:
                                    text selected_style.name xalign 0.5 xanchor 0.5 yalign 0.5 yanchor 0.5 style "outfit_style"

            frame:
                background "#0a142688"
                xysize (440, 500)
                padding (20,20)
                vbox:
                    yalign 0.0
                    hbox:
                        yalign 1.0
                        xalign 0.5
                        xanchor 0.5
                        spacing 50
                        textbutton "Save Haircut" action [Return, Function(person.clean_cache), SetField(person, "outfit", use_current_outfit), Hide("hair_creator")] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,80) background "#222222" hover_background "#1a45a1"

                        textbutton "Abandon Design" action [Function(restore_hair_style, person, old_hair_style, old_pubes_style), Function(person.clean_cache), SetField(person, "outfit", use_current_outfit), Return, Hide("hair_creator")] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (185,80) background "#222222" hover_background "#1a45a1"
