#Elements_list is a list of lists, with each internal list receiving an individual column
#The first element in a column should be the title, either text or a displayable. After that it should be a tuple of (displayable/text, return_value).
screen main_choice_display(menu_items):
    hbox:
        spacing 10
        align (0.518, 0.2)
        anchor (0.5, 0.0)
        for count in __builtin__.range(len(menu_items)):
            if __builtin__.len(menu_items[count]) > 1:
                frame:
                    background "gui/LR2_Main_Choice_Box.png"
                    xysize (380, 700)
                    $ title_element = menu_items[count][0]
                    if isinstance(title_element, basestring):
                        text "[title_element]" xalign 0.5 ypos 45 anchor (0.5,0.5) size 22 style "menu_text_title_style" xsize 240
                    else:
                        add title_element xalign 0.5 ypos 45 anchor (0.5,0.5)

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        xalign 0.5
                        xanchor 0.5
                        yanchor 0.0

                        ypos 99
                        xsize 360
                        ysize 588
                        vbox:
                            for item in [x for x in menu_items[count][1:] if x.display]:
                                textbutton "[item.title!i]":
                                    xysize (360, 80)
                                    align (0.5, 0.5)
                                    style "textbutton_style"
                                    text_style "textbutton_text_style"
                                    text_align (0.5,0.5)
                                    if not (renpy.mobile or renpy.android) and item.display_key:
                                        hovered [Function(item.show_person)]
                                        unhovered [Function(item.hide_person)]
                                    action [
                                        Function(item.hide_person),
                                        Return(item.return_value)
                                    ]
                                    tooltip item.the_tooltip
                                    sensitive item.is_sensitive
