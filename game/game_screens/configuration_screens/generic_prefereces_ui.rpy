init 2 python:
    generic_preference = {}
    generic_preference["Body Type"] = {
        "Thin Body": ["thin_body", 33, 0],
        "Normal Body": ["standard_body", 33, 1],
        "Curvy Body": ["curvy_body", 33, 2]
    }
    generic_preference["Cup Size"] = {
        "AA": ["AA", 4, 0],
        "A": ["A", 8 , 1],
        "B": ["B", 15, 2],
        "C": ["C", 20, 3],
        "D": ["D", 20 , 4],
        "DD": ["DD", 15, 5],
        "DDD": ["DDD", 10, 6],
        "E": ["E", 5, 7],
        "F": ["F", 2, 8],
        "FF": ["FF", 1, 9]
    }
    generic_preference["Skin Color"] = {
        "White": ["white", 33, 0],
        "Tan": ["tan", 33, 1],
        "Dark": ["black", 33, 2]
    }
    generic_preference["Hair Style"] = {
        "Bobbed Hair": ["Bobbed Hair", 8, 0],
        "Braided Hair": ["Braided Hair", 8, 1],
        "Coco Hair": ["Coco Hair", 8 , 2],
        "Curly Bun Hair": ["Curly Bun Hair", 8, 3],
        "Long Hair": ["Long Hair", 8, 4],
        "Messy Hair": ["Messy Hair", 8 , 5],
        "Messy Ponytail": ["Messy Ponytail", 8, 6],
        "Messy Short Hair": ["Messy Short Hair", 8, 7],
        "Ponytail": ["Ponytail", 8, 8],
        "Shaved Side Hair": ["Shaved Side Hair", 8, 9],
        "Short Hair": ["Short Hair", 8, 10],
        "Twin Tails": ["Twintails", 8, 11],
        "Windswept Short Hair": ["Windswept Short Hair", 8, 12]
    }
    generic_preference["Pubes Style"] = {
        "Shaved Pubic Hair": ["Shaved Pubic Hair", 20, 0],
        "Landing Strip Pubic Hair": ["Landing Strip Pubic Hair", 20, 1],
        "Diamond Shaped Pubic Hair": ["Diamond Shaped Pubic Hair", 20, 2],
        "Neatly Trimmed Pubic Hair": ["Neatly Trimmed Pubic Hair", 20, 3],
        "Untrimmed Pubic Hair": ["Untrimmed Pubic Hair", 20, 4]
    }

    # update defaults when not exist
    for pref in generic_preference:
        for x in generic_preference[pref]:
            if not (getattr(persistent, generic_preference[pref][x][0]) or isinstance(getattr(persistent, generic_preference[pref][x][0]), int)):
                setattr(persistent, generic_preference[pref][x][0], generic_preference[pref][x][1])


    @classmethod
    def get_random_skin(cls):
        return get_random_from_weighted_list(build_generic_weighted_list("Skin Color"))

    Person.get_random_skin = get_random_skin

    @classmethod
    def get_random_body_type(cls):
        return get_random_from_weighted_list(build_generic_weighted_list("Body Type"))

    Person.get_random_body_type = get_random_body_type

    @classmethod
    def get_random_tit(cls, min = None, max = None):
        if not min:
            start = 0
        else:
            start = cls.get_tit_index(min)
        if not max:
            end = len(cls._list_of_tits)
        else:
            end =  cls.get_tit_index(max)+1
        return get_random_from_weighted_list(build_generic_weighted_list("Cup Size", start, end))

    Person.get_random_tit = get_random_tit

    @classmethod
    def get_random_pubes_style(cls):
        return get_random_copy_from_named_list(build_generic_weighted_list("Pubes Style"), pube_styles)

    Person.get_random_pubes_style = get_random_pubes_style

    @classmethod
    def get_random_hair_style(cls):
        return get_random_copy_from_named_list(build_generic_weighted_list("Hair Style"), hair_styles)

    Person.get_random_hair_style = get_random_hair_style

    def get_random_copy_from_named_list(weighted_list, item_list):
        name = get_random_from_weighted_list(weighted_list)
        found = next((x for x in item_list if x.name.lower() == name.lower()), None)
        if found:
            return found.get_copy()
        return None

    def build_generic_weighted_list(pref, start = None, end = None):
        weighted_list = []
        if start is None:
            start = 0
        if end is None:
            end = len(generic_preference[pref])

        pref_dict = OrderedDict(generic_preference[pref])
        for x in pref_dict:
            idx = pref_dict.keys().index(x)
            if idx < start or idx > end:
                continue
            if getattr(persistent, generic_preference[pref][x][0], generic_preference[pref][x][1]) > 0:
                weighted_list.append([generic_preference[pref][x][0], getattr(persistent, generic_preference[pref][x][0], generic_preference[pref][x][1])])
        return weighted_list

    def change_generic_preferences_requirement():
        return True

    change_generic_preferences_action = Action("Change Preferences", change_generic_preferences_requirement, "show_generic_preference_ui", menu_tooltip = "Change the chance of a certain body type / cup size / skin tone will be generated for a random person.")

init 5 python:
    add_label_hijack("normal_start", "activate_generic_preference")
    add_label_hijack("after_load", "activate_generic_preference")

label activate_generic_preference(stack):
    python:
        bedroom.remove_action("show_body_type_preference_ui")
        bedroom.remove_action("show_cup_preference_ui")
        bedroom.remove_action("show_skin_preference_ui")
        bedroom.add_action(change_generic_preferences_action)
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_generic_preference_ui():
    $ renpy.call_screen("generic_preference_ui")
    return

init 10 python:
    def switch_preference(pref):
        cs = renpy.current_screen()
        cs.scope["pref_selected"] = pref
        preference_value_changed(pref)
        return

    def preference_value_changed(pref):
        cs = renpy.current_screen()

        total = 0
        for x in generic_preference[pref]:
            total += getattr(persistent, generic_preference[pref][x][0])

        cs.scope["current_total"] = total
        return

screen generic_preference_ui():
    modal True
    zorder 49

    default pref_selected = "Body Type"
    default current_total = 100

    frame: # top frame
        background "#0a1426dd"
        xsize 1200
        yalign 0.4
        xalign 0.5
        xanchor 0.5

        vbox:
            xanchor 0.5
            xalign 0.5
            yalign 0.3
            spacing 10

            hbox:
                for pref in sorted(generic_preference):
                    textbutton pref:
                        style "textbutton_style"
                        text_style "menu_text_title_style"
                        xsize 220
                        sensitive pref != pref_selected
                        action [
                            Function(switch_preference, pref) # If a clothing item is selected and currently being previewed then remove it from preview.
                        ]

            for pref in sorted(generic_preference):
                if pref == pref_selected:
                    vbox:
                        for x in [x[0] for x in sorted(generic_preference[pref].items(), key = lambda x: x[1][2])]:
                            hbox:
                                spacing 5
                                vbox:
                                    xsize 340
                                    ysize 50
                                    yoffset 5
                                    text x style "textbutton_text_style"
                                vbox:
                                    xsize 600
                                    ysize 50
                                    bar value FieldValue(persistent, generic_preference[pref][x][0], 100, step = 1, style = "slider", action = [ Function(preference_value_changed, pref_selected) ]) xsize 600 ysize 45
                                vbox:
                                    xsize 60
                                    ysize 50
                                    yoffset 5
                                    text (str(getattr(persistent, generic_preference[pref][x][0])) + "%" if getattr(persistent, generic_preference[pref][x][0]) > 0 else "None") style "menu_text_style" xsize 100

            hbox:
                text "Total: {current}%".format(current = current_total):
                    xalign 1.0
                    style "menu_text_style"

            hbox:
                xsize 800
                text "{size=16}Warning: setting all values to the same value will result in even chance, for correct percentage make sure they sum close to 100. If you want all random characters to adhere to these value, start a new game after you changed these values." style "warning_text"

            hbox:
                xalign 0.5
                textbutton "Close" action [Return] style "textbutton_style" text_style "textbutton_text_style" tooltip "" text_text_align 0.5 text_xalign 0.5 xysize (155,60)

style warning_text:
    color "B22222"
    size 16
    xalign 0.5
