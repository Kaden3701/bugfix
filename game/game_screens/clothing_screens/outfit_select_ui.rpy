screen outfit_select_manager(slut_limit = 999, show_outfits = True, show_overwear = True, show_underwear = True, main_selectable = True, show_make_new = True, show_export = True, show_modify = True, show_duplicate = True, show_delete = True):
    #If sluttiness_limit is passed, you cannot exit the creator until the proposed outfit has a sluttiness below it (or you create nothing).
    add paper_background_image
    modal True
    zorder 100
    default demo_outfit = None
    default hide_underwear = False
    default hide_shoes = False
    default hide_base = False
    default hide_overwear = False
    default hide_list = []
    default mannequin = "mannequin"

    $ outfit_info_array = []
    ## ["Category name", is_category_enabled, "return value when new is made", slut score calculation field/function, "export field type", add_outfit_to_wardrobe_function] ##
    $ outfit_info_array.append([show_outfits, "Outfit", "new_full", "outfit_slut_score" , "FullSets", Wardrobe.add_outfit, "outfit_sets"])
    $ outfit_info_array.append([show_overwear, "Overwear", "new_over", "overwear_slut_score", "OverwearSets",  Wardrobe.add_overwear_set, "overwear_sets"])
    $ outfit_info_array.append([show_underwear, "Underwear", "new_under", "underwear_slut_score", "UnderwearSets", Wardrobe.add_underwear_set, "underwear_sets"])

    hbox:
        spacing 20
        xalign 0.1
        yalign 0.1
        for category_info in outfit_info_array:
            if category_info[0]:
                frame:
                    background "#1a45a1aa"
                    xsize 450
                    ysize 850
                    viewport:
                        scrollbars "vertical"
                        xsize 450
                        ysize 850
                        mousewheel True
                        vbox:
                            spacing -10
                            text "[category_info[1]]s" style "menu_text_title_style" size 30 xalign 0.5 #Add an s to make it plural so we can reuse the field in the new button. Yep, I'm that clever-lazy.
                            null height 20
                            if show_make_new:
                                textbutton "Create New [category_info[1]]":
                                    action Return(category_info[2])
                                    sensitive True
                                    style "textbutton_style"
                                    text_style "outfit_description_style"
                                    xsize 450

                                null height 20

                            for outfit in getattr(mc.designed_wardrobe, category_info[6]):
                                textbutton "{}\n{} {{image=gold_heart_token_small}}".format(outfit.name, getattr(outfit, category_info[3])):
                                    action [
                                        Function(hide_mannequin),
                                        Return(["select",outfit.get_copy()])
                                    ]
                                    sensitive (getattr(outfit, category_info[3]) <= slut_limit) and main_selectable
                                    hovered [
                                        SetScreenVariable("demo_outfit", outfit.get_copy()),
                                        Function(preview_outfit)
                                    ]
                                    unhovered [
                                        SetScreenVariable("demo_outfit", None),
                                        Function(hide_mannequin)
                                    ]
                                    style "textbutton_style"
                                    text_style "outfit_description_style"
                                    tooltip "Pick this outfit."
                                    xsize 450

                                if show_export or show_modify or show_duplicate or show_delete:
                                    hbox:
                                        yoffset 6
                                        spacing 0
                                        xsize 450
                                        if show_export:
                                            default exported = []
                                            textbutton "Export":
                                                action [Function(exported.append,outfit), Function(log_outfit, outfit, outfit_class = category_info[4], wardrobe_name = "Exported_Wardrobe"), Function(renpy.notify, "Outfit exported to Exported_Wardrobe.xml")]
                                                sensitive outfit not in exported
                                                hovered [
                                                    SetScreenVariable("demo_outfit", outfit.get_copy()),
                                                    Function(preview_outfit)
                                                ]
                                                unhovered [
                                                    SetScreenVariable("demo_outfit", None),
                                                    Function(hide_mannequin)
                                                ]
                                                style "textbutton_style"
                                                text_style "outfit_description_style"
                                                tooltip "Export this outfit. The export will be added as an xml section in game/wardrobes/Exported_Wardrobe.xml."
                                                xsize 100

                                        if show_modify:
                                            textbutton "Modify":
                                                action Return(["modify",outfit]) #If we are modifying an outfit just return it. outfit management loop will find which category it is in.
                                                sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                hovered [
                                                    SetScreenVariable("demo_outfit", outfit.get_copy()),
                                                    Function(preview_outfit)
                                                ]
                                                unhovered [
                                                    SetScreenVariable("demo_outfit", None),
                                                    Function(hide_mannequin)
                                                ]
                                                style "textbutton_style"
                                                text_style "outfit_description_style"
                                                tooltip "Modify this outfit."
                                                xsize 100

                                        if show_duplicate:
                                            $ the_copied_outfit = outfit.get_copy() #We make a copy to add to the wardrobe if this is selected. Otherwise continues same as "Modify"
                                            textbutton "Duplicate":
                                                action [Function(category_info[5], mc.designed_wardrobe, the_copied_outfit), Return(["duplicate",the_copied_outfit])]
                                                #sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                hovered [
                                                    SetScreenVariable("demo_outfit", outfit.get_copy()),
                                                    Function(preview_outfit)
                                                ]
                                                unhovered [
                                                    SetScreenVariable("demo_outfit", None),
                                                    Function(hide_mannequin)
                                                ]
                                                style "textbutton_style"
                                                text_style "outfit_description_style"
                                                tooltip "Duplicate this outfit and edit the copy, leaving the original as it is."
                                                xsize 100

                                        if show_delete:
                                            textbutton "Delete":
                                                action Function(mc.designed_wardrobe.remove_outfit, outfit)
                                                #sensitive (getattr(outfit, category_info[3]) <= slut_limit)
                                                hovered [
                                                    SetScreenVariable("demo_outfit", outfit.get_copy()),
                                                    Function(preview_outfit)
                                                ]
                                                unhovered [
                                                    SetScreenVariable("demo_outfit", None),
                                                    Function(hide_mannequin)
                                                ]
                                                style "textbutton_style"
                                                text_style "outfit_description_style"
                                                tooltip "Remove this outfit from your wardrobe. This cannot be undone!"
                                                xsize 100

                                    null height 20

                                null height 25

        if slut_limit != 999:
            frame:
                background "#888888"
                text "Slut Limit: [slut_limit]{image=gui/heart/red_heart.png}" style "textbutton_text_style" text_align 0.0
    frame:
        background None
        anchor [0.5,0.5]
        align [0.39,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [
                Function(hide_mannequin),
                Function(renpy.free_memory),
                Return("No Return")
            ]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
