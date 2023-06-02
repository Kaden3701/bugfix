init -1 python:
    def get_mod_category_list():
        cat_list = []
        for mod in action_mod_list:
            if not mod.category in cat_list:
                cat_list.append(mod.category)
        cat_list.sort()
        return cat_list

init 2:
    screen mod_configuration_ui(): #How you select serum and trait research
        $ categories = get_mod_category_list()

        add science_menu_background_image
        modal True
        frame:
            background "#0a1426dd"
            xalign 0.5
            xsize 1000
            yalign 0.5
            ysize 900
            hbox:
                spacing 20
                vbox:
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 480
                        text "Mod Modules" style "menu_text_header_style"

                    viewport:
                        xsize 480
                        ysize 780
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 470
                            for category in categories:
                                frame:
                                    background "#000080"
                                    xsize 460
                                    text category style "serum_text_style_header"

                                for mod in sorted(action_mod_list, key = lambda x: x.name):
                                    if mod.category == category and mod.allow_disable == True:
                                        $ name = mod.name.replace("[the_person.possessive_title]", "the person").replace("[the_person.title]", "the person").split('{')[0].split('\n')[0]
                                        textbutton "[name] {size=16}" + ("{color=#007000}Enabled" if mod.enabled else "{color=#930000}Disabled"):
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            tooltip mod.menu_tooltip
                                            action [Function(mod.toggle_enabled)]
                                            xsize 460

                vbox:
                    spacing 5
                    frame:
                        background "#000080"
                        xsize 480
                        text "Serum Traits" style "menu_text_header_style"

                    viewport:
                        xsize 480
                        ysize 780
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 470
                            for i in __builtin__.range(1, 4):
                                frame:
                                    background "#000080"
                                    xsize 460
                                    text "Research Tier: [i]" style "serum_text_style_header"

                                for mod in sorted(serum_mod_list, key = lambda x: x.name):
                                    if mod.tier == i:
                                        textbutton "[mod.name] {size=16}" + ("{color=#007000}Enabled" if mod.enabled else "{color=#930000}Disabled"):
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            tooltip mod.desc
                                            if mod.allow_toggle:
                                                action [Function(mod.toggle_enabled)]
                                            xsize 460
                # vbox:
                #     spacing 5
                #     frame:
                #         background "#000080"
                #         xsize 380
                #         text "Generic People Role" style "serum_text_style"

                #     viewport:
                #         xsize 380
                #         ysize 780
                #         scrollbars "vertical"
                #         mousewheel True
                #         vbox:
                #             xsize 370
                #             for role_action in generic_people_role.actions:
                #                 if role_action.allow_disable == True:
                #                     $ name = role_action.name.replace("[the_person.possessive_title]", "the person").replace("[the_person.title]", "the person").split('\n')[0]
                #                     textbutton "[name] {size=16}" + ("{color=#007000}Enabled" if role_action.enabled else "{color=#930000}Disabled"):
                #                         style "textbutton_style"
                #                         text_style "serum_text_style_traits"
                #                         tooltip role_action.menu_tooltip
                #                         action [Function(role_action.toggle_enabled)]
                #                         xsize 360

        textbutton "Close" action [Return()] style "textbutton_style" text_style "serum_text_style" yalign 0.91 xanchor 0.5 xalign 0.5
