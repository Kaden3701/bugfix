screen serum_design_menu_item(the_design, given_x_size = 500, given_y_size = 64, name_addition = ""):
    python:
        serum_name = "{name}{addition}".format(name = the_design.name, addition = name_addition)
    frame:
        background None

        xsize given_x_size
        ysize given_y_size
        padding (0,0)
        margin (0,0)
        button:
            style "textbutton_style"
            xfill True
            yfill True
            action SetScreenVariable("selected_serum", the_design)
            sensitive True
            hovered [SetScreenVariable("selected_serum", None), Show("serum_tooltip", None, the_design, given_anchor = (1.0,0.0), given_align = (0.95,0.05))]
            unhovered Hide("serum_tooltip")

        vbox:
            yanchor 0.5
            yalign 0.5
            xalign 1.0
            xfill True
            yfill True
            text "[serum_name]" style "textbutton_text_style" xoffset 16 yoffset 10
            use aspect_grid(the_design, given_xalign = 0.03, given_xanchor = 0.0)
