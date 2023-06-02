init -2 python:
    darken_matrix = im.matrix.saturation(0.9)*im.matrix.tint(.9,.9,.9)*im.matrix.brightness(-0.15)

    class Room(): #Contains objects.
        def __init__(self, name = None, formal_name = None, background_image= None, objects = None, actions = None, public = False, map_pos = None,
            tutorial_label = None, visible = True, hide_in_known_house_map = True, lighting_conditions = None, privacy_level = 0, darken = True, accessible_func = None):

            if name is None:
                self.name = "Unnamed Room"
            else:
                self.name = name

            if formal_name is None:
                self.formal_name = name
            else:
                self.formal_name = formal_name

            if background_image is None:
                raise AttributeError("Room '%s' has no background image defined." % (formal_name))

            self.background_image = background_image #If a string this is used at all points in the day. If it is a list each entry corrisponds to the background for a different part of the day

            self.objects = []
            if isinstance(objects, list):
                for x in objects:
                    self.add_object(x)
            elif isinstance(objects, RoomObject):
                self.add_object(objects)
            self.objects.append(RoomObject("stand",["Stand"], sluttiness_modifier = 0, obedience_modifier = 0)) #Add a standing position that you can always use.

            self.actions = ActionList(actions)

            self.on_room_enter_event_list = ActionList() #A list of Actions that are triggered when you enter a location. People events take priority.

            self.public = public #If True, random people can wander here.

            if map_pos is None:
                self.map_pos = [-1,-1] #off screen
            else:
                self.map_pos = map_pos #A tuple of two int values giving the hex coords, starting in the top left. Using this guarantees locations will always tessalate.

            self.visible = visible #If true this location is shown on the map. If false it is not on the main map and will need some other way to access it.
            self.hide_in_known_house_map = hide_in_known_house_map #If true this location is hidden in the house map, usually because their house is shown on the main map.

            self.tutorial_label = tutorial_label #When the MC first enters the room the tutorial will trigger.
            self.trigger_tutorial = True #Flipped to false once the tutorial has been done once
            self.accessable = True #If true you can move to this room. If false it is disabled

            if lighting_conditions is None: #Default is 100% lit all of the time.
                self.lighting_conditions = [[1,1,1], [1,1,1], [1,1,1], [1,1,1], [1,1,1]] #A colour array that tints characters in this location. Perfect default light is 1,1,1
            else:
                self.lighting_conditions = lighting_conditions

            self.privacy_level = privacy_level
            self.darken = darken
            self.accessible_func = accessible_func
            self.identifier = hash((name, formal_name))

            #TODO: add an "appropriateness" or something trait that decides how appropriate it would be to have sex, be seduced, etc. in this location.

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.name == other.name and self.formal_name == other.formal_name:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return self.identifier

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.name == other.name and self.formal_name == other.formal_name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.name != other.name or self.formal_name != other.formal_name
            return True

        def show_background(self):
            if (time_of_day == 0 or time_of_day == 4) and self.darken:
                the_background_image = im.MatrixColor(self.background_image, darken_matrix)
            else:
                the_background_image = self.background_image

            renpy.scene("master")
            renpy.show(name = self.name, what = the_background_image, layer = "master")

        def add_object(self,the_object):
            if isinstance(the_object, RoomObject):
                if not the_object in self.objects:
                    self.objects.append(the_object)

        def remove_object(self, object_or_name):
            found = next((x for x in self.objects if x == object_or_name), None)
            if not found and isinstance(object_or_name, basestring):
                found = next((x for x in self.objects if x.name == object_or_name), None)

            if found:
                self.objects.remove(found)

        def add_person(self,the_person):
            if not isinstance(the_person, Person):
                return
            if the_person not in list_of_people:
                list_of_people.append(the_person)
            the_person.change_location(self)

        @property
        def people(self):
            return people_at_location(self)

        @property
        def person_count(self):
            return len(self.people)

        def objects_with_trait(self,the_trait):
            return_list = []
            for object in self.objects:
                if object.has_trait(the_trait):
                    return_list.append(object)
            return return_list

        def has_object_with_trait(self,the_trait):
            if the_trait == "None":
                return True
            for object in self.objects:
                if object.has_trait(the_trait):
                    return True
            return False

        def get_object_with_trait(self, the_trait):
            if self.has_object_with_trait(the_trait):
                return get_random_from_list(self.objects_with_trait(the_trait))
            return None

        def get_object_with_name(self,name): #Use this to get objects from a room when you know what they should be named but don't have an object reference yet (ik
            for obj in self.objects:
                if obj.name == name:
                    return obj
            return None

        def get_lighting_conditions(self):
            return self.lighting_conditions[time_of_day]

        def add_action(self, action):
            self.actions.add_action(action)

        def remove_action(self, action):
            self.actions.remove_action(action)

        @property
        def is_accessible(self):
            if self.accessible_func and callable(self.accessible_func):
                return self.accessible_func()
            return True

        @property
        def valid_actions(self):
            actions = [x for x in self.actions if x.is_action_enabled() or x.is_disabled_slug_shown()]
            actions.sort(key = lambda x: x.priority if x.is_action_enabled() else -1000, reverse = True)
            return actions

        @property
        def has_cum_slut(self):
            return not self.get_cum_slut() is None

        def get_cum_slut(self):
            return get_random_from_list([x for x in self.people if x.has_cum_fetish])

        @property
        def has_anal_slut(self):
            return not self.get_anal_slut() is None

        def get_anal_slut(self):
            return get_random_from_list([x for x in self.people if x.has_anal_fetish])

        @property
        def has_breeder(self):
            return not self.get_breeder() is None

        def get_breeder(self):
            return get_random_from_list([x for x in self.people if x.has_breeding_fetish])

        @property
        def has_exhibitionist(self):
            return not self.get_exhibitionist() is None

        def get_exhibitionist(self):
            return get_random_from_list([x for x in self.people if x.has_exhibition_fetish])

        @property
        def is_private(self):
            return self.privacy_level == 0

        @property
        def room_average_slut(self):
            if __builtin__.len(self.people) == 0:
                return 0
            sum = 0
            for person in self.people:
                sum += person.sluttiness
            return __builtin__.int(sum / __builtin__.len(self.people))

        @property
        def room_max_slut(self):
            sum = 0
            for person in self.people:
                sum = __builtin__.max(person.sluttiness, sum)
            return __builtin__.int(sum)

        @property
        def room_outfit_average_sluttiness(self):
            if __builtin__.len(self.people) == 0:
                return 0
            sum = 0
            for person in self.people:
                sum += person.outfit.outfit_slut_score
            return __builtin__.int(sum / __builtin__.len(self.people))

        @property
        def room_outfit_max_sluttiness(self):
            sum = 0
            for person in self.people:
                sum = __builtin__.max(person.outfit.outfit_slut_score, sum)
            return __builtin__.int(sum)

        @property
        def room_outfit_eye_candy_score(self):
            if __builtin__.len(self.people) == 0:
                return 0
            sum = 0
            for person in self.people:
                sum += __builtin__.int(person.outfit.outfit_slut_score / 5)
                sum += 5 if person.outfit.cum_covered else 0

            return __builtin__.int(sum)
