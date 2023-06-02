screen girl_outfit_select_manager(target_wardrobe, show_sets = False, slut_limit = the_person.sluttiness): ##Brings up a list of outfits currently in a girls wardrobe.
    #add paper_background_image
    modal True
    zorder 99 #Allow it to be hidden below outfit_creator
    default preview_outfit = None
    default import_selection = False
    default mannequin = the_person

    hbox:
        xalign 0.1
        yalign 0.1
        spacing 20
        frame:
            background "#0a142688"
            xsize 450
            ysize 750


            vbox:
                frame:
                    background "#000080"
                    xfill True
                    text "Full Outfit Selection" style "menu_text_title_style" xalign 0.5

                viewport:

                    if __builtin__.len(target_wardrobe.outfit_sets) > 11:
                        scrollbars "vertical"
                    xfill True
                    yfill True
                    mousewheel True
                    vbox:
                        for outfit in sorted(target_wardrobe.outfit_sets, key = lambda outfit: outfit.outfit_slut_score):
                            use outfit_select_button(outfit, "full", the_person, slut_limit)

        if show_sets:
            frame:
                background "#0a142688"
                xsize 450
                ysize 750
                vbox:
                    frame:
                        background "#000080"
                        xfill True
                        text "Overwear Selection" style "menu_text_title_style" xalign 0.5

                    viewport:
                        if __builtin__.len(target_wardrobe.overwear_sets) > 11:
                            scrollbars "vertical"
                        xfill True
                        yfill True
                        mousewheel True
                        vbox:
                            for outfit in sorted(target_wardrobe.overwear_sets, key = lambda outfit: outfit.outfit_slut_score):
                                use outfit_select_button(outfit, "over", the_person, slut_limit)


            frame:
                background "#0a142688"
                xsize 450
                ysize 750
                vbox:
                    frame:
                        background "#000080"
                        xfill True
                        text "Underwear Selection" style "menu_text_title_style" xalign 0.5

                    viewport:
                        if __builtin__.len(target_wardrobe.underwear_sets) > 11:
                            scrollbars "vertical"
                        xfill True
                        yfill True
                        mousewheel True
                        vbox:
                            for outfit in sorted(target_wardrobe.underwear_sets, key = lambda outfit: outfit.outfit_slut_score):
                                use outfit_select_button(outfit, "under", the_person, slut_limit)

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Function(hide_mannequin), Return("None")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

screen outfit_select_button(outfit, outfit_type, the_person, slut_limit):
    textbutton outfit.name.replace("_", " ").title() + "\n" + get_hearts(outfit.outfit_slut_score, color = "gold"):
        style "textbutton_no_padding_highlight"
        text_style "serum_text_style"

        xfill True

        sensitive (outfit.outfit_slut_score <= slut_limit)

        action [Function(hide_mannequin), Return(outfit)]
        hovered [Function(draw_mannequin, the_person, outfit)]
        alternate Show("outfit_creator", None, outfit.get_copy(), outfit_type, slut_limit, the_person.wardrobe)
