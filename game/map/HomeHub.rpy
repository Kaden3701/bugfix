init -5 python:
    class HomeHub(MapHub):
        def __init__(self, name, formal_name, locations = [], position = None, icon = None, accessible_func = None,
                people = None, jobs = None):

            super(HomeHub, self).__init__(name, formal_name, locations, position, icon, accessible_func)
            self.people = MappedList(Person, all_people_in_the_game)
            self.jobs = MappedList(Job, all_jobs)

            for person in people:
                self.people.append(person)
            for job in jobs:
                self.jobs.append(job)

        def __iter__(self):
            return iter(set(self.locations + [x.home for x in self.people] + [x.home for x in list_of_people if x not in unique_character_list and x.job in self.jobs]))

        @property
        def visible_locations(self):
            return [x for x in self if not x.hide_in_known_house_map and x in mc.known_home_locations]
