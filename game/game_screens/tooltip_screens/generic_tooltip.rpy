screen tooltip_screen():
    zorder 500

    default hovered_enough_time = False
    $ tooltip = GetTooltip()

    if tooltip and __builtin__.len(tooltip) > 0:
        timer 0.3 action SetScreenVariable("hovered_enough_time",True)
        if hovered_enough_time:
            $ mouse_xy = renpy.get_mouse_pos()
            frame:
                xanchor (0 if mouse_xy[0] < 1920 - 500 else 1.0)
                yanchor (1.0 if mouse_xy[1] > 1080/2 else 0.0)
                xsize 450
                pos (mouse_xy[0], mouse_xy[1])
                text "[tooltip]":
                    style "serum_text_style"
                    xalign 0.5
    else:
        timer 0.1 action SetScreenVariable("hovered_enough_time", False)
