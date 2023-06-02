# This file contains the provisions for the lifetstyle coach screen for setting personal goal lists.
init -2 style textbutton_green_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
    padding (5,5)
    margin (5,5)
    background "#43B197"
    insensitive_background "#222222"
    hover_background "#aaaaaa"

screen lifestyle_goal_sheet():
    add paper_background_image
    modal True
    zorder 100

    default tt = Tooltip("")

    vbox:
        xanchor 0.5
        xalign 0.5
        yalign 0.1
        frame:
            background "#1a45a1aa"
            xanchor 0.5
            xalign 0.5
            hbox:
                xsize 1600
                ysize 110
                vbox:
                    xsize 600
                    text "Goal Lists" + " " + mc.name + " " + mc.last_name style "menu_text_style" size 36
                    text "Each category requires a minimum of 2 selections" size 20
                vbox:
                    xsize 1000
                    text tt.value size 20
        null height 40
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
                    text "Stat Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(__builtin__.len(stat_goals)) style "menu_text_style" size 24 xalign 0.5
                    for goal in sorted(stat_goals_options_list, key = lambda x: x.name):
                        hbox:
                            xalign 0.5

                            if goal in stat_goals:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]
                            else:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]
            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Work Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(__builtin__.len(work_goals)) style "menu_text_style" size 24 xalign 0.5
                    for goal in sorted(work_goals_options_list, key = lambda x: x.name):
                        hbox:
                            xalign 0.5
                            if goal in work_goals:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]
                            else:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]

            frame:
                background "#1a45a1aa"
                xalign 0.5
                xanchor 0.5
                vbox:

                    xsize 500
                    text "Sex Goals" style "menu_text_style" size 32 xalign 0.5
                    text "Current Total: " + str(__builtin__.len(sex_goals)) style "menu_text_style" size 24 xalign 0.5
                    for goal in sorted(sex_goals_options_list, key = lambda x: x.name):
                        hbox:
                            xalign 0.5

                            if goal in sex_goals:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_green_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]
                            else:
                                textbutton goal.name:
                                    xalign 0.5
                                    yalign 0.5
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    sensitive True
                                    action [
                                        Function(goal.toggle_enabled)
                                    ]
                                    hovered [
                                        tt.Action(goal.name + "\n" + goal.description)
                                    ]

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [Return(True), Hide("serum_tooltip")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
