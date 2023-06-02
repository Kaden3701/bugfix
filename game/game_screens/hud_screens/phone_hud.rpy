transform phone_slide(start_yalign, goal_yalign, duration = 0.4):
    yalign start_yalign
    linear duration yalign goal_yalign

transform background_fade(max_time, time_used):
    alpha (max_time-time_used)/max_time
    linear max_time - time_used alpha 0

screen phone_hud_ui():
    default phone_up = False
    default start_phone_pos = 1.45
    default end_phone_pos = 1.45
    default ui_xsize = 360
    default fade_time = 5
    modal False

    frame:
        background Transform("#0a142688", alpha=persistent.hud_alpha)
        xsize ui_xsize + 20
        ysize 440
        xanchor 1.0
        xalign 1.0
        at phone_slide(start_phone_pos, end_phone_pos)

        frame:
            background None

            null height 5
            viewport:
                mousewheel True
                draggable True
                if __builtin__.len(mc.log_items) > 4:
                    scrollbars "vertical"
                vbox:
                    for log_item in [x for x in mc.log_items if x and x[0] and x[1]]:
                        $ time_diff = time.time() - log_item[2]
                        if time_diff > fade_time:
                            $ time_diff = fade_time

                        frame:
                            background Transform("#11334488", alpha=persistent.hud_alpha)
                            xsize ui_xsize
                            padding (2, 2)
                            text "[log_item[0]]" style log_item[1] size 18 xsize ui_xsize - 20 first_indent 10 rest_indent 10 yoffset 2
                        frame:
                            background "#ff000088"
                            xsize ui_xsize
                            ysize 2
                            yanchor 1.0
                            yalign 0.95
                            xpadding 0
                            ypadding 0
                            at background_fade(5, time_diff)
                        null height 2
            button:
                style "transparent_style"
                focus_mask None
                margin (-20, -20)
                ysize 440
                action [
                    ToggleScreenVariable("phone_up"),
                    ToggleScreenVariable("end_phone_pos",1.0, 1.45),
                    ToggleScreenVariable("start_phone_pos",1.45, 1.0),
                    ]
