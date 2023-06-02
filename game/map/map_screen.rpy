transform pop_in_frame:
    zoom 0.0
    pause 0.001
    zoom 1.0
    # linear .2 zoom 1.0

screen map_manager():
    imagemap:
        ground map_background_image
        hotspot (0, 0, 1920, 1080) clicked SetScreenVariable("active_hub", None)

    default active_hub = get_current_location_hub()
    default page = 1
    default max_page = 1
    default tt = Tooltip(None)
    default extra_info = None
    default day_info = "{size=16}" + get_formatted_date_string() + " (day "+ str(day) + "){/size}"

    text "[day_info]" style "menu_text_style" size 18

    # if active_hub and persistent.map_auto_open_current_hub:
    #     on "show" action [
    #         MouseMove(x=active_hub.position.X, y=active_hub.position.Y, duration=0)
    #     ]

    # button:
    #     #Invisible button covers entire screen, closes the context menu when mouse leaves the menu
    #     anchor (0, 0)
    #     xysize (1920, 1080)

    #     sensitive active_hub
    #     hovered [SetScreenVariable("active_hub",None),SetScreenVariable("page",1),]
    #     action [SetScreenVariable("active_hub",None),SetScreenVariable("page",1),]


    for hub in [x for x in list_of_hubs if x.is_visible]:
        frame:
            background None
            xysize (100, 87)
            anchor (0.5, 0.5)
            pos (hub.position.X, hub.position.Y)
            imagebutton:
                anchor (0.5, 0.5)
                align (0.5, 0.5)
                focus_mask True
                if hub.is_accessible:
                    auto "map/images/icons/Map_{}_%s.png".format(hub.icon)
                    if renpy.variant("touch"):
                        action [SetScreenVariable("active_hub", hub), SetScreenVariable("page",1)]
                    else:
                        hovered [SetScreenVariable("active_hub", hub), SetScreenVariable("page",1)]
                        action NullAction()

                    if mc.location in hub:
                        idle "map/images/icons/Map_%s_alt_idle.png" % hub.icon
                    elif active_hub == hub:
                        idle "map/images/icons/Map_%s_hover.png" % hub.icon

                else:
                    idle "map/images/icons/Map_%s_insensitive.png" % hub.icon
                    hover "map/images/icons/Map_%s_idle.png" % hub.icon
                    hovered [CaptureFocus("hub"), SetScreenVariable("extra_info", "{} is closed".format(hub.formal_name))]
                    unhovered [ClearFocus("hub"), SetScreenVariable("extra_info", None)]
                    action [SetScreenVariable("active_hub", None)]

            #Label and icons drawn below icon
            vbox:
                anchor (0.5, 0)
                align (0.5, 1.0)
                yoffset 10
                if hub.is_accessible:
                    text get_hub_tile_text(hub):
                        text_align 0.5
                        style "map_text_style"
                else:
                    text "[hub.formal_name]":
                        text_align 0.5
                        style "map_text_style"

    if active_hub:
        python:
            tt_dict = create_tooltip_dictionary(active_hub.visible_locations)
            max_page = ((active_hub.visible_count -1) // 12) + 1
            current_locations = active_hub.visible_locations[
                (page-1) * 12 : (page * 12)
            ]

        #Pagination Controls / Label
        if isinstance(active_hub, HomeHub) and active_hub.visible_count > 7:
            frame at pop_in_frame anchor (0.5,0.5) modal True xysize (450,85) pos (active_hub.position.X,active_hub.position.Y) background None:
                frame:
                    xysize (86,75)
                    align (0.5,0.5)
                    background "map/images/icons/Map_POI_blank_hover.png"
                    text "[page]/[max_page]":
                        align (0.5,0.5)
                        size 28
                        style "menu_text_title_style"
                if max_page > 1:
                    fixed:
                        xysize (171,75)
                        align (0.0,0.5)
                        imagebutton:
                            auto "map/images/LR2_LeftArrow_Button_%s_B.png"
                            action SetScreenVariable("page",change_page(page, -1, max_page))
                            align (0.5,0.5)
                        text "Back" align (0.5,0.5) style "textbutton_text_style"
                    fixed:
                        xysize (171,75)
                        align (1.0,0.5)
                        imagebutton:
                            auto "map/images//LR2_RightArrow_Button_%s_B.png"
                            action [SetScreenVariable("page",change_page(page,1,max_page))]
                            align (0.5,0.5)
                        text "Next" align (0.5,0.5) style "textbutton_text_style"

        frame at pop_in_frame:
            background None # "#aaaa00aa"
            align (0, 0)
            padding (0, 0)
            xanchor .5
            if active_hub.visible_count > 7:
                #District Icons / Long Maps appear above/below their icons instead of on top
                #Combined with pagination, should keep maps from going above/below screen line
                if active_hub.position.Y < 540:
                    yanchor 0.0
                    offset (0,42)
                else:
                    yanchor 1.0
                    offset (0,-44)
                xysize (440, 750)
            else:
                yanchor 0.5
                if active_hub.is_expandable:
                    xysize (440, 450)
                else:
                    xysize (170, 150)
            pos (active_hub.position.X, active_hub.position.Y)

            #Draw each location hex
            frame:
                background None # "#1a45a1aa"
                align (0, 0)
                padding (0, 0)
                anchor (0, 0)
                yfill True

                #Invisible button that covers, the navigation controls and partial hexes to prevent closing of menu
                # if isinstance(active_hub, HomeHub) and active_hub.visible_count > 7:
                #     button:
                #         background None # "#aaaaaaaa"
                #         align (0.5, (0.0 if active_hub.position.Y < 540 else 1.0))
                #         yoffset (-30 if active_hub.position.Y < 540 else 30)
                #         xysize (350, 150)
                #         sensitive True
                #         action NullAction()

                for idx, location in enumerate(current_locations):
                    frame:
                        background None
                        anchor (0, 0)
                        xysize (170, 150)
                        offset calculate_hub_offsets(active_hub, idx, location)
                        imagebutton:
                            anchor (0.5, 0.5)
                            align (0.5, 0.5)
                            if location.is_accessible:
                                action [Return(location)]
                                #tooltip tooltips[place.name][0]
                                #hovered SetScreenVariable("tooltip",tile_tip)
                                #unhovered SetScreenVariable("tooltip",None)
                                if location != mc.location:
                                    auto "map/images/hexes/hex_%s.png"
                                else:
                                    auto "map/images/hexes/hex_%s_alt.png"
                                hovered tt.Action(tt_dict[location.name][0])
                            else:
                                auto "map/images/hexes/hex_%s_inactive.png"
                                hovered [CaptureFocus("hub"), SetScreenVariable("extra_info", "{} is closed".format(location.formal_name))]
                                unhovered [ClearFocus("hub"), SetScreenVariable("extra_info", None)]
                                action NullAction()
                            focus_mask "map/images/hexes/hex_focus_mask.png"
                        if location.is_accessible:
                            text get_location_tile_text(location, tt_dict) anchor (0.5, 0.5) align (0.5, 0.5) style "map_text_style"
                        else:
                            text "[location.formal_name]" anchor (0.5, 0.5) align (0.5, 0.5) style "map_text_style"

    frame id "return_frame":
        background None
        anchor (0.5, 0.5)
        align (0.5, 0.92)
        imagebutton:
            align (0.5, 0.5)
            auto "gui/button/choice_%s_background.png"
            focus_mask True
            action Return(mc.location)
        textbutton "Return" align (0.5, 0.5) text_style "return_button_style"

    if tt.value:
        frame:
            background "#09090990"
            align (0.95, 0.95)
            text "[tt.value]" style "textbutton_text_style" text_align 0.0 size 18 xalign 0.5 yalign 0.0

    if extra_info:
        nearrect:
            focus "hub"

            frame:
                align (0.5, 0)
                background "#09090990"
                text "[extra_info]" style "serum_text_style"
