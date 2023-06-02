#Used to display stats for multi people while you're talking to them, takes an array of Actor objects.
init 2 python:
    def multi_person_info_ui_get_formatted_tooltip(person):
        (role_list, fetish_list) = person_info_ui_get_special_role_information(person)

        tooltip = ""
        if mc.business.get_employee_title(person) != "None":
            tooltip += "Job: " + mc.business.get_employee_title(person) + "\n"
        tooltip += "Love: " + get_love_hearts(person.love, 5) + "\n"
        tooltip += "Suggestibility: " + str(person.suggestibility) + "%\n"
        tooltip += "Age: " + str(person.age) + "\n"
        tooltip += "Height: " + height_to_string(person.height) + "\n"
        tooltip += "Cup size: " + str(person.tits) + "\n"
        tooltip += "Weight: " + get_person_weight_string(person) + "\n"
        if fetish_list:
            tooltip += "Fetishes: " + ", ".join(fetish_list) + "\n"
        if role_list:
            tooltip += ", ".join(role_list) + "\n"
        return tooltip

screen multi_person_info_ui(actors):
    layer "solo"
    frame:
        background Transform("gui/topbox.png", alpha=persistent.hud_alpha)
        xsize 1100
        ysize 200
        yalign 0.0
        xalign 0.5
        xanchor 0.5

        hbox:
            xanchor 0.5
            xalign 0.5
            spacing 10
            xsize 1000
            xoffset 50

            for actor in sorted(actors, key=lambda a: a.sort_order):
                python:
                    arousal_info = get_arousal_with_token_string(actor.person.arousal, actor.person.max_arousal)
                    arousal_tooltip_info = get_arousal_number_string(actor.person.arousal, actor.person.max_arousal)
                    energy_info = get_energy_string(actor.person.energy, actor.person.max_energy)
                    energy_tooltip_info = get_energy_number_string(actor.person.energy, actor.person.max_energy)
                    sluttiness_info = get_heart_image_list(actor.person.sluttiness, actor.person.effective_sluttiness())

                vbox:
                    hbox:
                        textbutton "{image=question_mark_small}":
                            yoffset 4
                            style "transparent_style"
                            tooltip multi_person_info_ui_get_formatted_tooltip(actor.person)
                            action NullAction()

                        text format_titles_short(actor.person) style "menu_text_style" size 30 ysize 30

                        if actor.person.serum_effects:
                            textbutton "{image=serum_vial} +[actor.person.suggestibility]%":
                                style "transparent_style"
                                text_style "menu_text_style"
                                tooltip person_info_ui_get_serum_info_tooltip(actor.person)
                                action NullAction()

                    textbutton "Arousal: [arousal_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "When a girl is brought to 100% arousal she will start to climax. Climaxing will increase sluttiness, as well as make the girl happy. The more aroused you make a girl the more sex positions she is willing to consider.\nCurrently: {}".format(arousal_tooltip_info)
                        action NullAction()

                    textbutton "Energy: [energy_info]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "Energy is spent while having sex, with more energy spent on positions that give the man more pleasure. Some energy comes back each turn, and a lot of energy comes back over night.\nCurrently {}".format(energy_tooltip_info)
                        action NullAction()

                    textbutton "Happiness: [actor.person.happiness]":
                        style "transparent_style"
                        text_style "menu_text_style"
                        tooltip "The happier a girl the more tolerant she will be of low pay and unpleasant interactions. High or low happiness will return to it's default value over time."
                        action NullAction()

                    hbox:
                        textbutton "Obedience: [actor.person.obedience] {image=triskelion_token_small} " + get_obedience_string(actor.person.obedience):
                            style "transparent_style"
                            text_style "menu_text_style"
                            tooltip "Girls with high obedience will listen to commands even when they would prefer not to and are willing to work for less pay. Girls who are told to do things they do not like will lose happiness, and low obedience girls are likely to refuse altogether."
                            action NullAction()

                        if any(x[0] > 0 or x[0] < 0 for x in actor.person.situational_obedience.itervalues()):
                            textbutton "{image=question_mark_small}":
                                style "transparent_style"
                                tooltip person_info_ui_get_formatted_obedience_tooltip(actor.person)
                                action NullAction()

                    hbox:
                        textbutton "Sluttiness: [sluttiness_info]":
                            style "transparent_style"
                            text_style "menu_text_style"
                            tooltip "The higher a girls sluttiness the more slutty actions she will consider acceptable and normal. Temporary sluttiness ({image=red_heart_token_small}) is easier to raise but drops slowly over time. Core sluttiness ({image=gold_heart_token_small}) is permanent, but only increases slowly unless a girl is suggestible."
                            action NullAction()

                        if any(x[0] > 0 or x[0] < 0 for x in actor.person.situational_sluttiness.itervalues()):
                            textbutton "{image=question_mark_small}":
                                style "transparent_style"
                                tooltip person_info_ui_get_formatted_tooltip(actor.person)
                                action NullAction()
