# Allows you to preview and select singular items from an XML file before importing.
init 2:
    screen import_outfit_manager(target_wardrobe, xml_filename = None, outfit_type = None):
        default outfit_categories = {
            "Full": ["FullSets", "full", "outfit_sets", "outfit_slut_score"],
            "Overwear": ["OverwearSets", "over", "overwear_sets", "overwear_slut_score"],
            "Underwear": ["UnderwearSets", "under", "underwear_sets", "underwear_slut_score"]
        }
        add paper_background_image
        modal True
        zorder 100

        python:
            if xml_filename:
                wardrobe = wardrobe_from_xml(xml_filename)

        grid __builtin__.len(outfit_categories) 1:
            for category in sorted(outfit_categories):
                vbox:
                    xsize 480
                    frame:
                        background "#0a142688"
                        text "[category]" style "menu_text_title_style" xalign 0.5
                        xfill True
                    if not outfit_type or outfit_categories[category][1] == outfit_type:
                        viewport:
                            ysize 880
                            if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])) > 7:
                                scrollbars "vertical"
                            mousewheel True
                            vbox:
                                if __builtin__.len(getattr(wardrobe, outfit_categories[category][2])) > 0: #Don't show a frame if it is empty
                                    frame:
                                        background None
                                        vbox:
                                            for outfit in sorted(getattr(wardrobe, outfit_categories[category][2]), key = lambda outfit: (outfit.outfit_slut_score, outfit.name)):  # Not sure if there's any good reason to sort XML lists since the default way it works is to place the newest outfit at the bottom which is predictable.
                                                frame:
                                                    background "#0a142688"
                                                    vbox:
                                                        id str(outfit)
                                                        xfill True
                                                        textbutton "{}\n{}".format(outfit.name.replace("_", " ").title(), get_hearts(getattr(outfit, outfit_categories[category][3]), color = "gold")):
                                                            xfill True
                                                            style "textbutton_no_padding_highlight"
                                                            text_style "serum_text_style"

                                                            action [
                                                                Show("outfit_creator", None, outfit.get_copy(), outfit_categories[category][1], None, target_wardrobe), # Bring the outfit into the outfit_creator for editing when left clicked
                                                                Hide(renpy.current_screen().screen_name)
                                                                ]

                                                            hovered Function(draw_average_mannequin, outfit)

        frame:
            background None
            anchor [0.5,0.5]
            align [0.5,0.92]
            xysize [500,125]
            imagebutton:
                align [0.5,0.5]
                auto "gui/button/choice_%s_background.png"
                focus_mask "gui/button/choice_idle_background.png"
                action Hide("import_outfit_manager")
            textbutton "Return" align [0.5,0.5] text_style "return_button_style"
