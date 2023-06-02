init -1 python:
    def color_indicator(variable, max_value = 100): # Gives color indication to a value range split into 5.
        if variable >= max_value / 1.25: # 80%
            return "{color=#24ed27}" + str(variable) +"{/color}"
        if variable >= max_value / 1.67: # 60%
            return "{color=#8edb21}" + str(variable) +"{/color}"
        if variable >= max_value / 2.5: # 40%
            return "{color=#ffec6e}" + str(variable) +"{/color}"
        if variable >= max_value / 5: # 20%
            return "{color=#ed9d4c}" + str(variable) +"{/color}"
        else: # less than 20%
            return "{color=#ff6347}" + str(variable) +"{/color}"

screen serum_production_select_ui():
    add science_menu_background_image
    modal True
    default line_selected = None
    default production_line_weight_tooltip = "Work done by production employees will be split between active lines based on production weight."
    default production_line_autosell_tooltip = "Doses of serum above the auto-sell threshold will automatically be flagged for sale and moved to the marketing department."
    $ production_remaining = 100 - mc.business.used_line_weight
    hbox:
        xalign 0.04
        yalign 0.4
        ysize 900
        spacing 20
        frame:
            background "#0a142688"
            xsize 600
            ysize 900
            vbox:
                spacing 5
                xalign 0.5
                frame:
                    background "#000080"
                    xfill True

                    text "Production Lines" style "menu_text_title_style" xalign 0.5

                frame:
                    background "#000080"
                    xfill True

                    text "Capacity Remaining: " + str(color_indicator(production_remaining)) + "%" style "serum_text_style"

                frame:
                    background "#000080"
                    xfill True
                    textbutton "Max Serum Tier: [mc.business.max_serum_tier]" action VrenNullAction style "serum_text_style" text_style "serum_text_style" tooltip "The highest tier of serum you can produce is limited by your production facilities. Upgrade them to produce higher tier designs."

                viewport:
                    draggable True
                    if mc.business.production_lines > 3: # Have the scrollbar only exist if it is nescessary
                        scrollbars "vertical"
                    mousewheel True
                    xfill True

                    vbox:
                        spacing 20
                        xsize 600

                        $ line_number = 0
                        for line in mc.business.production_lines: #For the non-programmers we index our lines to 1 through production_lines.
                            $ line_number += 1
                            vbox:
                                xsize 580
                                frame:
                                    background "#0a142688"

                                    vbox:
                                        xfill True
                                        spacing 0

                                        textbutton "Production Line [line_number]":
                                            action [
                                                SetScreenVariable("line_selected", line),
                                                Hide("serum_tooltip")
                                            ]
                                            style "serum_textbutton_style_header"
                                            text_style "menu_text_title_style"
                                            margin (0,0)
                                            if line.selected_design:
                                                hovered Show("serum_tooltip",None, line.selected_design, given_anchor = (1.0,0.0), given_align = (0.97,0.07))
                                                unhovered Hide("serum_tooltip")
                                            background ("#000080" if line_selected == line else "#0a142688")
                                            xfill True
                                            xalign 0.5 xanchor 0.5

                                        textbutton "Currently Producing: " + (line.selected_design.name if line.selected_design else "Nothing"):
                                            action [
                                                SetScreenVariable("line_selected", line),
                                                Hide("serum_tooltip")
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            margin (0,0)
                                            if line.selected_design:
                                                hovered Show("serum_tooltip",None, line.selected_design, given_anchor = (1.0,0.0), given_align = (0.97,0.07))
                                                unhovered Hide("serum_tooltip")
                                            background ("#000080" if line_selected == line else "#0a142688")
                                            xfill True
                                            xalign 0.5 xanchor 0.5

                                    #null height 20
                                        frame:
                                            background "#000080"
                                            xfill True
                                            grid 1 2:
                                                hbox:
                                                    frame:
                                                        background None

                                                        text "Production Weight:   " style "serum_text_style"

                                                    if line.selected_design:
                                                        textbutton "-10%":
                                                            action Function(line.change_line_weight, -10)
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            sensitive line.production_weight >= 10
                                                            xsize 60
                                                            tooltip production_line_weight_tooltip

                                                        frame:
                                                            xsize 140
                                                            background None

                                                            text str(color_indicator(line.production_weight)) + "%" style "serum_text_style"

                                                        textbutton "+10%":
                                                            action Function(line.change_line_weight, 10)
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            sensitive production_remaining >= 10
                                                            xsize 60
                                                            tooltip production_line_weight_tooltip

                                                        textbutton "X":
                                                            style "textbutton_style"
                                                            text_style "serum_text_style"
                                                            xsize 40
                                                            action Function(line.clear_product)
                                                            tooltip "Cancel production on this line."

                                                    else:
                                                        frame:
                                                            background None
                                                            xsize 60
                                                            text "-10%" style "serum_text_style"
                                                            tooltip production_line_weight_tooltip

                                                        frame:
                                                            background None
                                                            xsize 140
                                                            text "0%" style "serum_text_style"

                                                        frame:
                                                            background None
                                                            xsize 60
                                                            text "+10%" style "serum_text_style"
                                                            tooltip production_line_weight_tooltip

                                                hbox:

                                                    frame:
                                                        background None
                                                        text "Auto-sell: " style "serum_text_style"

                                                    if line.autosell:
                                                        button action Function(line.toggle_line_autosell) background "#44aa44" xsize 35 ysize 35 yalign 0.5 yanchor 0.5 xalign 0.0 xanchor 0.0 tooltip production_line_autosell_tooltip
                                                    else:
                                                        button action Function(line.toggle_line_autosell) background "#444444" xsize 35 ysize 35 yalign 0.5 yanchor 0.5 xalign 0.0 xanchor 0.0 tooltip production_line_autosell_tooltip

                                                    frame:
                                                        background None
                                                        xsize 60
                                                        ysize 20

                                                    if line.selected_design:
                                                        if line.autosell:
                                                            hbox:
                                                                xsize 60
                                                                yoffset 4
                                                                textbutton "<<" action Function(line.change_line_autosell, -10) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5  text_style "serum_text_style" tooltip production_line_autosell_tooltip
                                                                textbutton "<" action Function(line.change_line_autosell, -1) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5  text_style "serum_text_style" tooltip production_line_autosell_tooltip

                                                            frame:
                                                                xsize 180
                                                                text "When > [line.autosell_amount] doses" style "menu_text_style" ysize 30 yalign 0.5 yanchor 0.5

                                                            hbox:
                                                                xsize 60
                                                                yoffset 4
                                                                textbutton ">" action Function(line.change_line_autosell, 1) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5 text_style "serum_text_style" tooltip production_line_autosell_tooltip
                                                                textbutton ">>" action Function(line.change_line_autosell, 10) style "textbutton_no_padding_highlight" yalign 0.5 yanchor 0.5 text_style "serum_text_style" tooltip production_line_autosell_tooltip

        if line_selected:
            frame:
                background "#0a142688"
                xsize 400
                ysize 650
                xalign 0.5
                vbox:
                    textbutton "Choose Production":
                        style "serum_textbutton_style_header"
                        text_style "menu_text_title_style"
                        xsize 375
                        action SetScreenVariable("line_selected",None)

                    if __builtin__.len(mc.business.serum_designs) == 0:
                        textbutton "No designs researched! Create and research a design in the R&D department first!":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            action NullAction()
                    else:
                        viewport:
                            draggable True
                            scrollbars "vertical"
                            mousewheel True
                            xsize 400
                            vbox:
                                for a_serum in sorted(mc.business.serum_designs, key = lambda x: x.name):
                                    if a_serum.researched:
                                        $ serum_title = a_serum.name if a_serum.tier <= mc.business.max_serum_tier else "{}\n{{color=#ff0000}}{{size=18}}Requires Policy: Tier {} Serum Production{{/size}}{{/color}}".format(a_serum.name, a_serum.tier)
                                        textbutton "[serum_title]":
                                            action [
                                            Hide("serum_tooltip"),
                                            Function(line_selected.set_product, a_serum, production_remaining),
                                            SetScreenVariable("line_selected",None)
                                            ]
                                            hovered [
                                            Show("serum_tooltip",None,a_serum,given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            sensitive a_serum.tier <= mc.business.max_serum_tier
                                            xsize 400
                                            xalign 0.5

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Return(), Hide("serum_tooltip")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xsize 54
        ysize 54
        yanchor 1.0
        xalign 0.0
        yalign 1.0
        action Function(mc.business.reset_tutorial,"production_tutorial")

    if mc.business.event_triggers_dict.get("production_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("production_tutorial", 1) <= 5: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle "/tutorial_images/production_tutorial_{}.png".format(mc.business.event_triggers_dict.get("production_tutorial", 1))
            hover "/tutorial_images/production_tutorial_{}.png".format(mc.business.event_triggers_dict.get("production_tutorial", 1))
            action Function(mc.business.advance_tutorial,"production_tutorial")
