screen mc_perk_sheet():
    add paper_background_image
    modal True
    zorder 100
    vbox:
        xanchor 0.5
        xalign 0.5
        yalign 0.1
        frame:
            background "#1a45a1aa"
            vbox:
                xsize 770
                text mc.name + " " + mc.last_name style "menu_text_style" size 40 xanchor 0.9 xalign 0.5
                text "Perk Sheet" style "menu_text_title_style" size 30 xanchor 0.9 xalign 0.5
        null height 60
        hbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.4
            spacing 40
            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Stat Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for stat_perk in perk_system.get_stat_perk_list():
                        hbox:
                            xalign 0.5
                            textbutton stat_perk:
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                                hovered [
                                Show("perk_tooltip",None,stat_perk)
                                ]

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:
                    xsize 500
                    text "Item Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for item_perk in perk_system.get_item_perk_list():
                        hbox:
                            xalign 0.5
                            textbutton item_perk:
                                xalign 0.5
                                yalign 0.5
                                style "textbutton_style"
                                text_style "textbutton_text_style"
                                sensitive True
                                action NullAction()
                                hovered [
                                Show("perk_tooltip",None,item_perk)
                                ]



            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:
                    xsize 500
                    text "Ability Perks" style "menu_text_title_style" size 32 xalign 0.5
                    for ability_perk in perk_system.get_ability_perk_list():
                        hbox:
                            xalign 0.5
                            if perk_system.get_ability_clickable(ability_perk):
                                textbutton perk_system.get_ability_perk_text_desc(ability_perk):
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    action Function(perk_system.click_ability, ability_perk)
                                    sensitive perk_system.get_ability_clickable(ability_perk)
                                    background "#43B197"
                                    insensitive_background "#222222"
                                    xalign 0.5
                                    yalign 0.5
                                    hovered [
                                    Show("perk_tooltip",None,ability_perk)
                                    ]
                            else:
                                textbutton perk_system.get_ability_perk_text_desc(ability_perk):
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    action Function(perk_system.click_ability, ability_perk)
                                    sensitive True
                                    xalign 0.5
                                    yalign 0.5
                                    hovered [
                                    Show("perk_tooltip",None,ability_perk)
                                    ]


    # frame:
    #     background None
    #     anchor [0.5,0.5]
    #     align [0.2,0.88]
    #     xysize [500,125]
    #     imagebutton:
    #         align [0.5,0.5]
    #         auto "gui/button/choice_%s_background.png"
    #         focus_mask "gui/button/choice_idle_background.png"
    #         action Show("mc_character_sheet")
    #     textbutton "Character Sheet" align [0.5,0.5] text_style "return_button_style"

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Hide("mc_perk_sheet"),
                    Hide("perk_tooltip")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

    if mc.business.event_triggers_dict.get("perk_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("perk_tutorial", 1)  <= 4: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle Image(get_file_handle("perk_tutorial_{}.png".format(mc.business.event_triggers_dict.get("perk_tutorial",1))))
            hover Image(get_file_handle("perk_tutorial_{}.png".format(mc.business.event_triggers_dict.get("perk_tutorial",1))))
            action Function(mc.business.advance_tutorial,"perk_tutorial")

screen perk_tooltip(the_perk):
    $ hint_height = 120
    $ window_height = hint_height
    $ perk_desc = perk_system.get_perk_desc(the_perk)

    zorder 105
    frame:
        background "#1a45a1aa"
        xpos 1000
        #xalign 0.1
        yalign 0.065
        xsize 760
        ysize window_height

        vbox:
            spacing 5
            frame:
                background "#33333388"
                xsize 750
                ysize hint_height - 10
                padding (0,0)
                vbox:
                    spacing 0
                    text "{size=24}[the_perk]{/size}" style "serum_text_style_header" xalign 0 text_align 0 xpos 2
                    text "{size=18}[perk_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
