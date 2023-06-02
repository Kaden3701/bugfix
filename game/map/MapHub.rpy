init -10 python:
    class MapHub():
        def __init__(self, name, formal_name, locations = [], position = None, icon = None, accessible_func = None):
            self.name = name
            self.formal_name = formal_name
            # internal property don't use in code -> user iterator of hub to get its locations
            self.locations = MappedList(Room, all_locations_in_the_game)
            self.position = position
            self.icon = icon
            self.accessible_func = accessible_func

            for loc in locations:
                self.add_location(loc)

            self.identifier = hash((name, formal_name))

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

        def __iter__(self):
            return iter(self.locations)

        def add_location(self, location):
            self.locations.append(location)

        def remove_location(self, location):
            self.locations.remove(location)

        @property
        def is_accessible(self):
            if self.accessible_func and callable(self.accessible_func):
                return self.accessible_func()
            return True

        @property
        def is_visible(self):
            return self.visible_count > 0

        @property
        def is_expandable(self):
            return self.visible_count > 1

        @property
        def visible_count(self):
            return len(self.visible_locations)

        @property
        def visible_locations(self):
            return [x for x in self if x.visible]



    class Point():
        def __init__(self, x, y):
            self.X = x
            self.Y = y

        def __str__(self):
            return "Point({},{}})".format(self.X, self.Y)

        def distance(self, other):
            if isinstance(self, other.__class__):
                dx = self.X - other.X
                dy = self.Y - other.Y
                return math.sqrt(dx**2 + dy**2)
            raise TypeError
