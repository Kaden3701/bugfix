init -2 python:
    hidden_talk_events = [
        "so_relationship_quarrel_label",
        "ask_new_title_label",

    ]

    def build_menu_items(elements_list, draw_hearts_for_people = True, draw_person_previews = True, show_location = False, person_preview_args = None):
        result = []
        for count in __builtin__.range(__builtin__.len(elements_list)):
            if __builtin__.len(elements_list[count]) > 1:
                if not isinstance(elements_list[count][1], MenuItem):
                    result.append(build_menu_item_list(elements_list[count], draw_person_previews, draw_hearts_for_people, show_location, person_preview_args))
                else:
                    result.append(elements_list[count])
        return result

    def build_menu_item_list(element_list, draw_hearts_for_people = True, draw_person_previews = True, show_location = False, person_preview_args = None):
        def find_and_replace_tooltip_property(item, extra_args):
            groups = re.search("\[[^]]*\]", item.menu_tooltip)
            if groups and isinstance(extra_args, Person):
                if ".title" in groups.group(0):
                    return re.sub("\[[^]]*\]", extra_args.title, item.menu_tooltip)
                if ".name" in groups.group(0):
                    return re.sub("\[[^]]*\]", extra_args.name, item.menu_tooltip)
            return item.menu_tooltip

        result = []
        result.append(element_list[0])

        column_elements = element_list[1:]
        for item in column_elements:
            mi = MenuItem()

            if isinstance(item, list): #It's a title/return value pair. Show the title, return the value.
                if isinstance(item[0], Action): #It's an action with extra arguments.
                    mi.extra_args = item[1]
                    item = item[0] #Rename item so that this is caught by the action section below.

                else: #It's (probably) a title/return string pair. Show the title, return the value
                    mi.title = item[0]
                    mi.return_value = item[1]

            if isinstance(item,Person): #It's a person. Format it for a person list.
                # Pre-load early
                if not (renpy.mobile or renpy.android): # don't load person on mobile
                    renpy.invoke_in_thread(mi.preload)

                info = []
                if item.is_favourite:
                    info.append("{image=full_star_token_small}")
                if item.has_exact_role(harem_role):
                    info.append("{image=harem_token_small}")
                if item.has_exact_role(girlfriend_role):
                    info.append("{image=gf_token_small}")
                if item.has_exact_role(affair_role):
                    info.append("{image=paramour_token_small}")
                if any(not isinstance(x, Limited_Time_Action) for x in item.on_talk_event_list.enabled_actions(item)):
                    info.append("{image=speech_bubble_exclamation_token_small}")
                elif any(not x.effect in hidden_talk_events for x in item.on_talk_event_list.enabled_actions(item)):
                    info.append("{image=speech_bubble_token_small}")

                info.append(format_titles(item))

                if item.has_role(clone_role):
                    info.append("{image=dna_token_small}")
                if item.knows_pregnant:
                    info.append("{image=feeding_bottle_token_small}")
                if item.serum_effects:
                    info.append("{image=vial_token_small}")
                if item.infractions:
                    info.append("{image=infraction_token_small}")
                if item.trance_training_availabe:
                    info.append("{image=lust_eye_token_small}")
                if item.arousal_perc >= 60:
                    info.append("{image=arousal_token_small}")
                if show_location:
                    info.append("\n{size=15}<" + item.location.formal_name + ">{/size}")
                if draw_hearts_for_people:
                    info.append("\n" + get_heart_image_list(item.sluttiness, item.effective_sluttiness()))
                if person_preview_args is None:
                    person_preview_args = {}

                mi.title = " ".join(info)
                mi.return_value = item
                mi.person_preview_args = person_preview_args
                mi.display_key = str(item.identifier)
                mi.display_scale = scale_person(item.height)
                if draw_person_previews:
                    mi.display_func = item.build_person_displayable

            if isinstance(item, Action):
                mi.title = ""
                mi.return_value = item
                mi.display = False #Default display state for an action is to hide it unless it is enabled or has a disabled slug
                if item.is_action_enabled(mi.extra_args):
                    mi.title = item.name
                    mi.display = True

                elif item.is_disabled_slug_shown(mi.extra_args):
                    mi.title = item.get_disabled_slug_name(mi.extra_args)
                    mi.display = True

                if item.menu_tooltip:
                    mi.the_tooltip = find_and_replace_tooltip_property(item, mi.extra_args)

            if isinstance(item, basestring): #It's just text. Display the text and return the text.
                mi.title = item
                mi.return_value = item

            if " (tooltip)" in mi.title:
                mi.the_tooltip = mi.title.split(" (tooltip)",1)[1]
                mi.title = mi.title.replace(" (tooltip)" + mi.the_tooltip,"")

            if " (disabled)" in mi.title:
                mi.title = mi.title.replace(" (disabled)", "")
                parts = mi.title.split("\n")
                if __builtin__.len(parts) > 1: # color and size disable reason
                    parts[-1] = "{color=#ff0000}{size=16}" + parts[-1] + "{/color}{/size}"
                    mi.title = "\n".join(parts)
                mi.is_sensitive = False

            if mi.display:
                if isinstance(item,Person) and isinstance(item.title, basestring) and isinstance(mi.the_tooltip, basestring):
                    mi.the_tooltip = mi.the_tooltip.replace("[the_person.title]", item.title)
                result.append(mi)
        return result


    class MenuItem():
        def __init__(self, title = "", return_value = None, the_tooltip = None, extra_args = None, display = True, is_sensitive = True, display_key = None, display_func = None, person_preview_args = None):
            self.title = title
            self.display_func = display_func
            self.the_tooltip = the_tooltip
            self.extra_args = extra_args
            self.display = display
            self.is_sensitive = is_sensitive
            self.display_key = display_key
            self.display_scale = None
            self.person_preview_args = person_preview_args
            self.return_value = return_value

        def __del__(self):
            self.return_value = None
            self.display_func = None
            return

        def show_person(self):
            if not self.display_func:
                return

            # check if we are not running out of memory
            validate_texture_memory()

            renpy.show(self.display_key, at_list=[character_right, self.display_scale], layer = "extra", what= self.display_func(lighting = mc.location.get_lighting_conditions(), **self.person_preview_args), tag = self.display_key)
            return

        def hide_person(self):
            if self.display_key:
                renpy.hide(self.display_key, layer = "extra")
            return

        def preload(self):
            def load_image(file):
                if file and not "empty_holder.png" in file.filename:
                    file.load()
                return

            def actual_body_type(person, cloth):
                if not cloth.body_dependant:
                    body_type = "standard_body"
                return person.body_type

            def actual_tit_size(person, cloth):
                if cloth.draws_breasts:
                    return person.tits
                return "AA"

            if not self.display_func:
                return

            # pre-load clothing items
            person = self.return_value
            for cloth in person.outfit:
                if isinstance(cloth, Facial_Accessory):
                    load_image(cloth.position_sets[person.idle_pose].get_image(person.face_style, person.get_emotion()))
                else:
                    load_image(cloth.position_sets[person.idle_pose].get_image(actual_body_type(person, cloth), actual_tit_size(person, cloth)))
            return
