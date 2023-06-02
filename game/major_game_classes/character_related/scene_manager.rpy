init -2 python:

    def hide_ui(): # Hides the UI
        renpy.hide_screen("main_ui")
        renpy.hide_screen("phone_hud_ui")
        renpy.hide_screen("business_ui")
        renpy.hide_screen("goal_hud_ui")
        return

    def show_ui(): # Show the UI
        renpy.show_screen("main_ui")
        renpy.show_screen("phone_hud_ui")
        renpy.show_screen("business_ui")
        renpy.show_screen("goal_hud_ui")
        return

    class Scene():
        def __init__(self):
            self.actors = []

        def add_group(self, people, position = None, emotion = None, special_modifier = None, lighting = None, z_order = None):
            xoffset = 0.1
            for person in people:
                self.add_actor(person, position, emotion, special_modifier, lighting, character_center(xoffset), z_order)
                xoffset -= .1
            self.draw_scene()

        def add_actor(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None, visible = True):
            if not isinstance(person, Person):
                print("Actor requires a Person object.")
                return

            actor = next((x for x in self.actors if x.person == person), None)
            if actor:   # we have an existing actor object, so use that
                self.show_actor(actor.person, position, emotion, special_modifier, lighting, display_transform, z_order)
            else:       # add person as actor
                if display_transform is None:
                    display_transform = self.get_random_free_position()
                actor = Actor(person, position, emotion, special_modifier, lighting, display_transform, z_order, visible)
                self.actors.append(actor)
                self.draw_scene()
            return actor

        # Removes all actors from the scene
        def clear_scene(self, reset_actor = True):
            for person in [actor.person for actor in self.actors]:
                person.hide_person()
                self.remove_actor(person, reset_actor = reset_actor)
            clear_scene()

        def review_outfits(self, dialogue = True, draw_person = True):
            for person in [actor.person for actor in self.actors]:
                person.review_outfit(dialogue = dialogue, draw_person = draw_person)

        def apply_outfits(self, draw_person = True):
            for actor in self.actors:
                actor.person.apply_planned_outfit()
                if draw_person:
                    actor.draw_actor()

        def update_actor(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None):
            actor = next((x for x in self.actors if x.person == person), None)
            if not actor:
                self.add_actor(person, position, emotion, special_modifier, lighting, display_transform, z_order)
                return

            if position:
                actor.position = position
            if emotion:
                actor.emotion = emotion
            actor.special_modifier = special_modifier   # always set special modifier
            if lighting:
                actor.lighting = lighting
            if display_transform:
                actor.display_transform = display_transform
            if not z_order is None:
                actor.z_order = z_order

            # print("Update actor:" + actor.person.name + " (position: " + actor.position + ", z-order: " + str(actor.z_order) + ")")
            self.draw_scene()

        def strip_actor_outfit_to_max_sluttiness(self, person, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, narrator_messages = None, temp_sluttiness_boost = 0):
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                #mc.log_event("Strip " + actor.person.title, "gray_float_text")
                return actor.person.strip_outfit_to_max_sluttiness(top_layer_first = top_layer_first, exclude_upper = exclude_upper, exclude_lower = exclude_lower, exclude_feet = exclude_feet, narrator_messages = narrator_messages, display_transform = actor.display_transform, lighting = actor.lighting, temp_sluttiness_boost = temp_sluttiness_boost, position = actor.position, emotion = actor.emotion, scene_manager = self)
            return False

        def strip_full_outfit(self, person = None, strip_feet = False, strip_accessories = False, lighting = None, delay = 1):
            strip_matrix = []
            if person is None:
                actors = [x for x in self.actors if x.visible]
            else:
                actors = [next((x for x in self.actors if x.person == person), self.add_actor(person))]

            for actor in actors:
                strip_list = actor.person.outfit.get_full_strip_list(strip_feet = strip_feet, strip_accessories = strip_accessories)
                strip_matrix.append([actor, strip_list, False])

            self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)
            return

        def strip_to_underwear(self, person = None, visible_enough = True, avoid_nudity = False, lighting = None, delay = 1):
            strip_matrix = []
            if person is None:
                actors = [x for x in self.actors if x.visible]
            else:
                actors = [next((x for x in self.actors if x.person == person), self.add_actor(person))]

            for actor in actors:
                strip_list = actor.person.outfit.get_underwear_strip_list(visible_enough = visible_enough, avoid_nudity = avoid_nudity)
                strip_matrix.append([actor, strip_list, False])

            self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)
            return

        def strip_to_tits(self, person = None, visible_enough = True, prefer_half_off = False, lighting = None, delay = 1):
            strip_matrix = []
            if person is None:
                actors = [x for x in self.actors if x.visible]
            else:
                actors = [next((x for x in self.actors if x.person == person), self.add_actor(person))]

            for actor in actors:
                half_off_instead = False
                if prefer_half_off and actor.person.outfit.can_half_off_to_tits(visible_enough = visible_enough):
                    strip_list = actor.person.outfit.get_half_off_to_tits_list(visible_enough = visible_enough)
                    half_off_instead = True
                else:
                    strip_list = actor.person.outfit.get_tit_strip_list(visible_enough = visible_enough)

                strip_matrix.append([actor, strip_list, half_off_instead])

            self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)
            return

        def strip_to_vagina(self, person = None, visible_enough = False, prefer_half_off = False, lighting = None, delay = 1):
            strip_matrix = []
            if person is None:
                actors = [x for x in self.actors if x.visible]
            else:
                actors = [next((x for x in self.actors if x.person == person), self.add_actor(person))]

            for actor in actors:
                half_off_instead = False
                if prefer_half_off and actor.person.outfit.can_half_off_to_vagina():
                    strip_list = actor.person.outfit.get_half_off_to_vagina_list(visible_enough = visible_enough)
                    half_off_instead = True
                else:
                    strip_list = actor.person.outfit.get_vagina_strip_list(visible_enough = visible_enough)

                strip_matrix.append([actor, strip_list, half_off_instead])

            self.strip_actor_strip_matrix(strip_matrix, lighting = lighting, delay = delay)
            return

        def strip_actor_strip_matrix(self, strip_matrix, lighting = None, delay = 1):
            keep_stripping = True
            while keep_stripping:
                keep_stripping = False
                for am in strip_matrix:
                    actor = am[0]
                    if am[1]:
                        the_clothing = am[1].pop(0)
                        if delay > 0:
                            actor.person.draw_animated_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = am[2]) #Draw the strip choice being removed from our current outfit
                        else:
                            actor.person.outfit.remove_clothing(the_clothing)
                        keep_stripping = True
                        renpy.pause(delay)
            return

        def strip_actor_strip_list(self, person, strip_list, lighting = None, half_off_instead = False):
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                for item in strip_list:
                    actor.person.draw_animated_removal(item, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

        def draw_animated_removal(self, person, the_clothing, lighting = None, half_off_instead = False): #A special version of draw_person, removes the_clothing and animates it floating away. Otherwise draws as normal.
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                #mc.log_event("Remove clothing " + actor.person.title, "gray_float_text")
                actor.person.draw_animated_removal(the_clothing, position = actor.position, emotion = actor.emotion, special_modifier = actor.special_modifier, lighting = lighting, display_transform = actor.display_transform, scene_manager = self, half_off_instead = half_off_instead)

        def get_random_free_position(self):
            if not any(x for x in self.actors if x.display_transform in [character_right, character_right_flipped]):
                return renpy.random.choice([character_right, character_right_flipped])
            if not any(x for x in self.actors if x.display_transform in [character_center, character_center_flipped]):
                return renpy.random.choice([character_center, character_center_flipped])
            if not any(x for x in self.actors if x.display_transform in [character_left, character_left_flipped]):
                return renpy.random.choice([character_left, character_left_flipped])
            return None

        # removes specific actor from scene
        def remove_actor(self, person, reset_actor = True):
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                if reset_actor:
                    # reset actor clothing
                    actor.person.apply_planned_outfit()
                actor.person.hide_person()
                self.actors.remove(actor)
                self.draw_scene()

        def hide_actor(self, person):
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                actor.visible = False
                actor.person.hide_person()
                self.draw_scene()

        def show_actor(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None):
            actor = next((x for x in self.actors if x.person == person), None)
            if actor:
                actor.visible = True
                self.update_actor(actor.person, position, emotion, special_modifier, lighting, display_transform, z_order)
            else:
                self.add_actor(person, position, emotion, special_modifier, lighting, display_transform, z_order)

        def draw_info_ui(self):
            clear_scene()
            visible_actors = [x for x in self.actors if x.visible]
            if __builtin__.len(visible_actors) > 3:
                return  # we cannot display more info than 3

            if __builtin__.len(visible_actors) > 1:
                renpy.show_screen("multi_person_info_ui", visible_actors)
            elif __builtin__.len(visible_actors) == 1:
                renpy.show_screen("person_info_ui", visible_actors[0].person)

        def draw_scene(self, exclude_list = []):
            self.draw_info_ui()
            for actor in sorted([x for x in self.actors if x.visible and x not in exclude_list], key = lambda x: x.z_order):
                #print("Draw: " + actor.person.name + " at: " + str(actor.z_order))
                actor.draw_actor()

        # update each actor and draw scene
        def update_scene(self, position = None, emotion = None, special_modifier = None, lighting = None):
            for actor in sorted(self.actors, key = lambda x: x.z_order):
                if position:
                    actor.position = position
                if emotion:
                    actor.emotion = emotion
                actor.special_modifier = special_modifier   # always set special modifier
                if lighting:
                    actor.lighting = lighting
            self.draw_scene()

    # z_order determines the order in which the actors are drawn, low number first, high number later
    class Actor():
        def __init__(self, person, position = None, emotion = None, special_modifier = None, lighting = None, display_transform = None, z_order = None, visible = True):
            self.person = person
            self.position = position
            self.emotion = emotion
            self.special_modifier = special_modifier
            self.lighting = lighting
            self.display_transform = display_transform
            self.sort_order = 2
            self.z_order = 0
            self.visible = visible

            if position is None:
                self.position = person.idle_pose

            if emotion is None:
                self.emotion = person.get_emotion()

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_transform is None:
                self.display_transform = character_right

            if z_order:
                self.z_order = z_order

            if display_transform == character_center or display_transform == character_center_flipped:
                self.sort_order = 1
            if display_transform == character_left or display_transform == character_left_flipped:
                self.sort_order = 0

        @property
        def person(self):
            if not hasattr(self, "_person"):
                self._person = None
            return Person.get_person_by_identifier(self._person)

        @person.setter
        def person(self, value):
            if isinstance(value, Person):
                self._person = value.identifier
            else:
                self._person = None

        def draw_actor(self):
            self.person.draw_person(position = self.position, emotion = self.emotion, special_modifier = self.special_modifier, lighting = self.lighting, display_transform = self.display_transform, display_zorder = self.z_order, wipe_scene = False, show_person_info = False)


##########################################
# Transformation for display_transform   #
##########################################
init 1:
    python:
        def calculate_scale(height_factor):
            return 0.7 - ((1 - height_factor) / 3)   # for now render at 70% size

    transform character_portrait_say():
        pos (360,-40)
        zoom .5

    transform zoom(factor):
        zoom factor

    transform character_right(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (1.0 + xoffset)
        xanchor 1.0
        zoom zoom


    transform character_right_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (1.0 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_center(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.75 + xoffset)
        xanchor 1.0
        zoom zoom

    transform character_center_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.75 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_left(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.5 + xoffset)
        xanchor 1.0
        zoom zoom

    transform character_left_flipped(xoffset = 0, yoffset = 0, zoom = 1):
        yalign (0.85 + yoffset)
        yanchor 1.0
        xalign (0.5 + xoffset)
        xanchor 1.0
        xzoom -(zoom)
        yzoom zoom

    transform character_69_bottom():
        yalign 0.62
        yanchor 0.5
        xalign 1.0
        xanchor 0.95
        zoom 0.8

    transform character_69_on_top():
        yalign 0.38
        yanchor 0.5
        xalign 1.0
        xanchor 1.02
        zoom 0.75
