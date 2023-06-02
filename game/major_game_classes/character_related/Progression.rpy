init -1 python:
    class Progression():
        def __init__(self, person):
            self.person_identifier = person.identifier
            return

        @property
        def person(self):
            return Person.get_person_by_identifier(self.person_identifier)

        @property
        def love_step(self):
            return self.person.event_triggers_dict.get("love_step", 0)

        @love_step.setter
        def love_step(self, value):
            self.person.event_triggers_dict["love_step"] = value

        @property
        def lust_step(self):
            return self.person.event_triggers_dict.get("lust_step", 0)

        @lust_step.setter
        def lust_step(self, value):
            self.person.event_triggers_dict["lust_step"] = value

        @property
        def obedience_step(self):
            return self.person.event_triggers_dict.get("obedience_step", 0)

        @obedience_step.setter
        def obedience_step(self, value):
            self.person.event_triggers_dict["obedience_step"] = value

        @property
        def story_character_description(self):
            func_name = "{}_story_character_description".format(self.person.name.lower())
            return self.__call_global_func(func_name, "")

        @property
        def has_love_story(self):
            func_name = "{}_story_love_list".format(self.person.name.lower())
            return self.__has_global_func(func_name)

        @property
        def story_love_list(self):
            func_name = "{}_story_love_list".format(self.person.name.lower())
            return self.__call_global_func(func_name, {
                0: "This character's love progress has not yet been created."
            })

        @property
        def has_lust_story(self):
            func_name = "{}_story_lust_list".format(self.person.name.lower())
            return self.__has_global_func(func_name)

        @property
        def story_lust_list(self):
            func_name = "{}_story_lust_list".format(self.person.name.lower())
            return self.__call_global_func(func_name, {
                0: "This character's lust progress has not yet been created."
            })

        @property
        def has_obedience_story(self):
            func_name = "{}_story_obedience_list".format(self.person.name.lower())
            return self.__has_global_func(func_name)

        @property
        def story_obedience_list(self):
            func_name = "{}_story_obedience_list".format(self.person.name.lower())
            return self.__call_global_func(func_name, {
                0: "This character's obedience progress has not yet been created."
            })

        @property
        def story_other_list(self):
            func_name = "{}_story_other_list".format(self.person.name.lower())
            return self.__call_global_func(func_name, {})

        @property
        def has_teamup(self):
            func_name = "{}_story_teamup_list".format(self.person.name.lower())
            return self.__has_global_func(func_name)

        @property
        def story_teamup_list(self):
            func_name = "{}_story_teamup_list".format(self.person.name.lower())
            return self.__call_global_func(func_name, {
                0: [None, "No teamups have been written for this character yet!"]
            })

        def __has_global_func(self, func_name):
            return func_name in globals()

        def __call_global_func(self, func_name, default_message):
            if func_name in globals():
                return globals()[func_name]()
            return default_message
