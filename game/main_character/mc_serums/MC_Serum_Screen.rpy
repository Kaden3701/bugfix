init 5:
    screen mc_personal_serum_screen():
        add IT_background_image
        modal True
        zorder 100
        use screen_mc_serum_return_button()
        use screen_mc_serum_basic_stats()
        vbox:

            xcenter 960
            yalign 0.1
            # background "#1a45a1aa"
            text "Select Personal Serum(s)" style "menu_text_title_style" size 48 xanchor 0.5 xalign 0.5
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
                        xsize 300
                        text "Performance" style "menu_text_title_style" size 32 xalign 0.5
                        for trait in mc_serum_get_energy_list():
                            use screen_personal_serum_button(trait)

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:
                        xsize 300
                        if mc_aura_serum_unlocked():
                            text "Aura" style "menu_text_title_style" size 32 xalign 0.5
                            for trait in mc_serum_get_aura_list():
                                use screen_personal_serum_button(trait)
                        else:
                            text "??????" style "menu_text_title_style" size 32 xalign 0.5

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:
                        xsize 300
                        if mc_cum_serum_unlocked():
                            text "Cum" style "menu_text_title_style" size 32 xalign 0.5
                            for trait in mc_serum_get_cum_list():
                                use screen_personal_serum_button(trait)
                        else:
                            text "??????" style "menu_text_title_style" size 32 xalign 0.5

                frame:
                    background "#1a45a1aa"
                    xalign 0.5
                    xanchor 0.5
                    vbox:

                        xsize 300
                        if mc_physical_serum_unlocked():
                            text "Physical" style "menu_text_title_style" size 32 xalign 0.5
                            for trait in mc_serum_get_physical_list():
                                use screen_personal_serum_button(trait)
                        else:
                            text "??????" style "menu_text_title_style" size 32 xalign 0.5

screen screen_mc_serum_return_button():
    frame:
        background None
        anchor [0.5,0.5]
        align [0.88,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [
                Hide("mc_personal_serum_screen"),
                Hide("mc_serum_tooltip"),
                Hide("nanobot_project_screen"),
                Hide("business_project_screen"),
                Hide("screen_IT_active_project"),
                Hide("mc_serum_unknown_tooltip"),
                Return()
            ]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

screen screen_mc_serum_basic_stats():
        zorder 100
        # $ length_desc = "Trait duration: " + str(get_mc_serum_duration()) + " days"
        $ quant_desc = "Maximum quantity: " + str(mc_serum_max_quantity()) + " serums"
        frame:
            background "#1a45a1aa"
            xcenter 1100
            #xalign 0.1
            ycenter 900
            xsize 510
            ysize 150

            vbox:
                spacing 5
                frame:
                    background Frame("gui/frame.png", 5,5)
                    xsize 500
                    ysize 140
                    ypadding 15
                    xpadding 30
                    vbox:
                        spacing 0
                        text "{size=24}Serum Stats{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                        # text "{size=18}[length_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                        text "{size=18}[quant_desc]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                        text "{size=18}Select serums will take effect tomorrow morning with their first dose.{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2

screen screen_personal_serum_button(trait):
    $ box_text = "??????"
    hbox:
        xalign 0.5
        #First, determine if the trait has not yet been unlocked. If so, obscure it.
        if not trait.is_unlocked:
            imagebutton:
                idle "gui/button/IT_button_a_inactive.png"
                hover "gui/button/IT_button_a_hover.png"
                sensitive True
                action NullAction()
                hovered [
                    Hide("mc_serum_tooltip"),
                    Show("mc_serum_unknown_tooltip",None,trait)
                    ]
        else:
            $ box_text = trait.menu_name()
            if trait.is_selected:    #The trait is currently active. Show a green box.
                imagebutton:
                    auto "gui/button/IT_button_a_%s.png"
                    sensitive True
                    selected True
                    action Function (trait.toggle_selected)
                    hovered [
                        Hide("mc_serum_unknown_tooltip"),
                        Show("mc_serum_tooltip",None,trait)
                        ]
            elif trait.is_available:  #IF the trait is available, make it clickable
                imagebutton:
                    auto "gui/button/IT_button_a_%s.png"
                    # action screen confirm(message="Take this serum?", Function (trait.apply_trait), no_action=return)
                    action Function (trait.toggle_selected)
                    sensitive True # (proj.identifier == mc.business.current_IT_project[0])
                    hovered [
                        Hide("mc_serum_unknown_tooltip"),
                        Show("mc_serum_tooltip",None,trait)
                        ]
            else:   #The trait is known, not active, but not available for use. Grey box
                imagebutton:
                    auto "gui/button/IT_button_a_%s.png"
                    sensitive False
                    action NullAction()
                    hovered [
                        Hide("mc_serum_unknown_tooltip"),
                        Show("mc_serum_tooltip",None,trait)
                        ]
    text box_text size 28 xanchor 0.5 xalign 0.5 style "textbutton_text_style" ypos -80


screen mc_serum_tooltip(the_trait):
    default hint_height = 150

    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 440
        #xalign 0.1
        ycenter 900
        xsize 760
        ysize hint_height

        vbox:
            spacing 5
            frame:
                background Frame("gui/frame.png", 5,5)
                xsize 750
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}[the_trait.name]{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=14}Upgrade Requirement: [the_trait.upgrade_info]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                    text "{size=18}[the_trait.trait_description]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                    text "{size=18}Tier: [the_trait.trait_tier]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2

screen mc_serum_unknown_tooltip(the_trait):
    default hint_height = 150

    zorder 100
    frame:
        background "#1a45a1aa"
        xcenter 440
        #xalign 0.1
        ycenter 900
        xsize 760
        ysize hint_height

        vbox:
            spacing 5
            frame:
                background Frame("gui/frame.png", 5,5)
                xsize 750
                ysize hint_height - 10
                ypadding 15
                xpadding 30
                vbox:
                    spacing 0
                    text "{size=24}???{/size}" style "menu_text_title_style" xalign 0 text_align 0 xpos 2
                    text "{size=18}You have not discovered the associated serum trait yet.{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
                    text "{size=14}Linked Serum Trait: [the_trait.linked_trait]{/size}" style "serum_text_style_traits" xalign 0 text_align 0 xpos 2
