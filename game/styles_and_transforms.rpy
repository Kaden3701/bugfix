#Contains LR2 specific styles and transforms that are used elsewhere, rather inconsistently.
init -10:
    python:
        def calculate_scale(height_factor):
            return 0.7 - ((1 - height_factor) / 2)   # for now render at 70% size

    transform scale_person(height_factor = 1):
        zoom calculate_scale(height_factor)

    transform character_right():
        yalign 0.85
        yanchor 1.0
        xalign 1.0
        xanchor 1.0

    transform position_shift(character_xalign = 1.0, scale_mod = 1.0, character_alpha = 1.0):
        yalign 0.85
        yanchor 1.0
        xanchor 1.0
        xalign character_xalign
        zoom scale_mod
        alpha character_alpha

    transform clothing_fade():
        linear 1.0 alpha 0.0

    style textbutton_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
        padding (5,5)
        margin (2,2)
        background "#0a142688"
        insensitive_background "#171717"
        hover_background "#143869"

    style textbutton_text_style: ##The generic style used for text button backgrounds. TODO: Replace this with a pretty background image instead of a flat colour.
        size 22
        italic False
        bold False
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        text_align 0.5
        yoffset 2

    style textbutton_no_padding: # Textbutton without padding
        margin (2,2)
        background "#0a142688"
        insensitive_background "#171717"
        hover_background "#143869"

    style textbutton_no_padding_highlight: # Textbutton without padding
        margin (2,2)
        background "#0a142688"
        insensitive_background "#171717"
        hover_background "#143869"

    style outfit_description_style is textbutton_text_style:
        size 18

    style menu_text_style:
        size 18
        italic False
        bold False
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        text_align 0.0
        line_spacing 2

    style menu_text_title_style is menu_text_style:
        font "fonts/ethnocentric rg.ttf"
        text_align 0.5
        xalign 0.5
        xanchor 0.5

    style menu_text_header_style is menu_text_title_style:
        size 32
        line_spacing 4

    style outfit_style: ##The text style used for text inside of the outfit manager.
        size 16
        italic True
        color "#dddddd"
        outlines [(1,"#666666",0,0)]
        insensitive_color "#222222"
        hover_color "#ffffff"

    style return_button_style:
        text_align 0.5
        size 30
        italic True
        bold True
        color "#dddddd"
        outlines [(2,"#222222",0,0)]

    style map_text_style:
        text_align 0.5
        size 14
        italic True
        bold True
        color "#dddddd"
        outlines [(2,"#222222",0,0)]

    style map_frame_style:
        background "#094691"

    style map_frame_blue_style:
        background "#5fa7ff"

    style map_frame_grey_style:
        background "#222222"

    style digital_text is text:
        font "fonts/Autobusbold-1ynL.ttf"
        color "#19e9f7"
        outlines [(2,"#222222",0,0)]
        yanchor 0.5
        yalign 0.5

    style text_message_style is say_dialogue:
        font "fonts/Autobusbold-1ynL.ttf"
        color "#19e9f7"
        outlines [(2,"#222222",0,0)]
        #TODO: MIght need to decide on Size too

    style general_dialogue_style is say_dialogue:
        outlines [(2,"#222222",0,0)]

    style float_text:
        size 24
        italic False
        bold False
        outlines [(2,"#222222",0,0)]
        yalign 0.5

    style float_text_pink is float_text:
        color "#d0759e"

    style float_text_red is float_text:
        color "#b14343"

    style float_text_grey is float_text:
        color "#696969"

    style float_text_green is float_text:
        color "#43B197"

    style float_text_yellow is float_text:
        color "#d0d010"

    style float_text_blue is float_text:
        color "#6394ED"

    style transparent_style:
        background None
        padding (5, 0)


    style serum_text_style: # General text style used in the serum screens.
        text_align 0.5
        size 20
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        xalign 0.5

    style serum_background_style: # General text style used in the serum screens.
        padding (5,5)
        margin (5,5)
        background "#0a142688"
        insensitive_background "#171717"
        hover_background "#143869"

    style serum_textbutton_style_positive: # Used for positive trait / serum slugs
        margin (2,2)
        background "#43B197"
        insensitive_background "#171717"
        hover_background "#143869"

    style serum_textbutton_style_negative: # Used for negative trait / serum slugs
        margin (2,2)
        background "#B14365"
        insensitive_background "#171717"
        hover_background "#143869"

    style serum_textbutton_style_header: # Used for header / title boxes NOTE: Make this different later to easier distinguish
        padding (5,5)
        margin (5,5)
        background "#0a142688"
        insensitive_background "#171717"
        hover_background "#143869"

    style serum_text_style_header: # Increased text size for headers
        size 22
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        bold True
        xalign 0.5
        xanchor 0.5
        text_align 0.5
        line_spacing 2

    style serum_text_style_traits: # Unaligned text style for traits in the serum_tooltip screen
        size 18
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        text_align 0.5
        xalign 0.5
        line_spacing 2
        yoffset 2

    style custom_outfit_style: ##The text style used for text inside of the outfit manager.
        size 20
        color "#dddddd"
        outlines [(2,"#222222",0,0)]
        insensitive_color "#dddddd"
        hover_color "#ffffff"
        bold False
        italic False
