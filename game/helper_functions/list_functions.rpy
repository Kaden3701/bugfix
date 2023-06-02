init -20 python:
    from lru import lru_cache_function
    from lru import LRUCacheDict

    def all_people_in_the_game(excluded_people = [], excluded_locations = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        return [x for x in list_of_people if x not in excluded_people and not x.location in excluded_locations]

    def all_locations_in_the_game(excluded_locations = []):
        return [x for x in list_of_places if not x in excluded_locations]

    def all_policies_in_the_game(excluded_policies = []):
        return [x for x in uniform_policies_list + recruitment_policies_list + serum_policies_list + organisation_policies_list + unmapped_policies_list if x not in excluded_policies]

    def all_IT_projects():
        return [x for x in business_IT_project_list + nanobot_IT_project_list]

    def all_jobs(excluded_jobs = []):
        return [x for x in list_of_jobs if x not in excluded_jobs]

    @lru_cache_function(max_size=1, expiration=3)
    def unique_characters_not_known(): # TODO The check should be standardized, but some people are vanilla, some are different modders or different 'style'.
        not_met_yet_list = []
        if alexia.get_destination(specified_time = 1) == alexia.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(alexia)
        if "ashley" in globals() and ashley.employed_since == -1:
            not_met_yet_list.append(ashley)
        if "candace" in globals() and candace.event_triggers_dict.get("met_at_store", 0) == 0: # She exist but not met yet.
            not_met_yet_list.append(candace)
        if christina.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(christina)
        if emily.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(emily)
        if "erica" in globals() and erica_get_progress() == 0:
            not_met_yet_list.append(erica)
        if cousin.get_destination(specified_time = 1) == cousin.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(cousin)
        if nora.get_destination(specified_time = 1) == nora.home: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(nora)
        if "salon_manager" in globals() and salon_manager.mc_title == 'Stranger': #She'll call MC differently when met.
            not_met_yet_list.append(salon_manager)
        if aunt.get_destination(specified_time = 2) == aunt_bedroom: # She'll be scheduled otherwise when met.
            not_met_yet_list.append(aunt)
        if "sarah" in globals() and not sarah.event_triggers_dict.get("first_meeting", False): # She'll be scheduled otherwise when met.
            not_met_yet_list.append(sarah)
        if "starbuck" in globals() and not starbuck.event_triggers_dict.get("starbuck_intro_complete", False):
            not_met_yet_list.append(starbuck)
        if "camilla" in globals() and camilla.mc_title == 'Stranger':
            not_met_yet_list.append(camilla)
        if "kaya" in globals() and kaya.mc_title == 'Stranger':
            not_met_yet_list.append(kaya)
        if "sakari" in globals() and sakari.mc_title == 'Stranger':
            not_met_yet_list.append(sakari)
        if "ellie" in globals() and ellie.mc_title == 'Stranger':
            not_met_yet_list.append(ellie)
        if "myra" in globals() and myra.mc_title == 'Stranger':
            not_met_yet_list.append(myra)
        return not_met_yet_list

    @lru_cache_function(max_size=1, expiration=3)
    def known_people_in_the_game(excluded_people = [], excluded_locations = []): # Pass excluded_people as array of people [mc, lily, aunt, cousin, alexia]
        return [x for x in list_of_people if x not in excluded_people and not x.location in excluded_locations and x not in unique_characters_not_known() and not x.is_stranger]

    def people_at_location(location, excluded_people = []):
        return [x for x in list_of_people if x not in excluded_people and x.location == location]

    @lru_cache_function(max_size=3, expiration=3)
    def known_people_at_location(location, excluded_people = []):
        return [x for x in location.people if x.is_available and not x in excluded_people + unique_characters_not_known() and not x.is_stranger]

    @lru_cache_function(max_size=1, expiration=3)
    def unknown_people_in_the_game(excluded_people = [], excluded_locations = []):
        return [x for x in list_of_people if x not in excluded_people and not x.location in excluded_locations and (x in unique_characters_not_known() or x.is_stranger)]

    @lru_cache_function(max_size=3, expiration=3)
    def unknown_people_at_location(location, excluded_people = []):
        return [x for x in location.people if x.is_available and not x in excluded_people and (x in unique_characters_not_known() or x.is_stranger)]

    def people_in_mc_home(excluded_people = []):
        return [x for x in list_of_people if x.is_available and not x in excluded_people and x.location in home_hub]

    def people_in_role(role):
        return [x for x in list_of_people if x.has_role(role)]

    def people_with_job(job):
        return [x for x in list_of_people if x.job == job]

    # returns a single employee when number of employees == 1
    # returns a tuple of employees when number of employees > 1
    # only returns employees available for events
    def get_random_employees(number_of_employees, exclude_list = [], **employee_args):
        list_of_possible_people = [x for x in mc.business.get_requirement_employee_list(exclude_list = exclude_list, **employee_args) if x.is_available]
        if len(list_of_possible_people) < number_of_employees:
            # build up tuple with correct number of items
            return tuple(None for _ in range(number_of_employees))

        result = []
        for i in range(number_of_employees):
            person = get_random_from_list(list_of_possible_people)
            result.append(person)
            list_of_possible_people.remove(person)

        if number_of_employees == 1:
            return result[0]

        return tuple(result)

    def get_random_interns(number_of_interns, exclude_list = [], **intern_args):
        list_of_possible_people = [x for x in mc.business.get_requirement_intern_list(exclude_list = exclude_list, **intern_args) if x.is_available]
        if len(list_of_possible_people) < number_of_interns:
            # build up tuple with correct number of items
            return tuple(None for _ in range(number_of_employees))

        result = []
        for i in __builtin__.range(number_of_interns):
            person = get_random_from_list(list_of_possible_people)
            result.append(person)
            list_of_possible_people.remove(person)

        if number_of_interns == 1:
            return result[0]

        return tuple(result)

    #Return a list of people in the same room as MC. If MC is home, return everyone at MC's home.
    def get_nearby_people():
        if mc.is_home:
            return [x for x in list_of_people if x.location in home_hub]
        if mc.is_at_work:
            return [x for x in list_of_people if x.location in office_hub]
        return mc.location.people

    # splits a item_array in even chunks of blok_size
    @renpy.pure
    def split_list_in_blocks(split_list, blok_size):
        for i in __builtin__.range(0, __builtin__.len(split_list), blok_size):
            yield split_list[i:i + blok_size]

    # splits an item_array in a number of blocks about equal in size (remainders are added to last block)
    @renpy.pure
    def split_list_in_even_blocks(split_list, blok_count):
        avg = __builtin__.len(split_list) / float(blok_count)
        result = []
        last = 0.0

        while last < __builtin__.len(split_list):
            result.append(split_list[__builtin__.int(last):__builtin__.int(last + avg)])
            last += avg

        return result

    # finds an item in a list, where search(item) == True
    # search as lambda could be a lambda ==> x: x.name == 'searchname'
    @renpy.pure
    def find_in_list(search, in_list):
        return next((x for x in in_list if search(x)), None)

    def find_serum_trait_by_name(name):
        return find_in_list(lambda x: x.name == name, list_of_traits)

    @renpy.pure
    def find_in_set(obj, in_set):
        return next((x for x in in_set if x == obj), None)

    def simple_list_format(list_to_format, what_to_format, string = "", ignore = "", attrib = ""): # Returns a simple list for use in generic menus. Extensive use in the Biotech Actions.
        tuple_list = []                                                    # NOTE: Needed a generic list setup, this seems to cover most usecases I came across.
        for what_to_format in list_to_format:
            if what_to_format is not ignore:

                if attrib is not "":
                    tuple_string = str(string) + str(vars(what_to_format)[attrib]) # e.g attrib = "name" for SerumTrait.name to be displayed
                    tuple_list.append([tuple_string, what_to_format])

                else:
                    tuple_string = str(string) + str(what_to_format)
                    tuple_list.append([tuple_string, what_to_format])
            else:
                tuple_string = str(what_to_format)
                tuple_list.append([tuple_string, what_to_format])
        return tuple_list

    # get a sorted list of people to use with main_choice_display
    @renpy.pure
    def get_sorted_people_list(people, title, back_extension = None, reverse = False):
        people.sort(key = lambda x: x.name, reverse = reverse)
        people.insert(0, title)
        if not back_extension is None:
            people.extend([back_extension])
        return people

    @renpy.pure
    def get_random_from_list(choices):
        if choices and hasattr(choices, '__iter__'):
            return renpy.random.choice(choices)
        return None
