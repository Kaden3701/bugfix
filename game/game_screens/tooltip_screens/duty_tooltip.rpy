screen duty_tooltip(the_duty):
    frame:
        background None
        vbox:
            spacing 20
            text the_duty.duty_name style "serum_text_style_header"
            text the_duty.duty_description style "menu_text_style" size 20 text_align 0.0

            transclude
