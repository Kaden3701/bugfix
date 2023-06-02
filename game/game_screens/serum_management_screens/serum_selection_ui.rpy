screen serum_inventory_select_ui(the_inventory, the_person = None, batch_size = 1, select_requirement = None): #Used to let the player select a serum from an inventory.
    add science_menu_background_image
    frame:
        background "#888888"
        xsize 400
        ysize 1000
        xalign 0.05
        yalign 0.05
        anchor (0.0,0.0)
        vbox:
            frame:
                background "#000080"
                xsize 380
                text "Serum Available" style "serum_text_style_header"

            for serum in sorted(the_inventory.serums_held, key = lambda x: x[0].name):
                textbutton "[serum[0].name] - [serum[1]] Doses":
                    style "textbutton_style"
                    text_style "serum_text_style"
                    xsize 380

                    xalign 0.5
                    xanchor 0.5
                    yalign 0.5
                    yanchor 0.5

                    action [Hide("serum_tooltip"),Return(serum[0])]
                    hovered Show("serum_tooltip",None,serum[0], given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                    sensitive serum[1] >= batch_size and (not callable(select_requirement) or select_requirement(serum[0]))

    if the_person:
        frame:
            background None
            anchor [0.5, 0.5]
            align [0.5,0.2]
            use serum_tolerance_indicator(the_person)

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Hide("serum_tooltip"), Return(None)]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
