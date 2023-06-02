init -8 python:
    def IT_proj_generic_req_True():
        return True

    def IT_proj_test_req_text():
        return "Text Test"

    def IT_proj_test_req_False():
        return False

    class IT_Project(Policy):
        def __init__(self, name, desc, requirement, cost, toggleable = False,
            on_buy_function = None, extra_arguments = None, on_apply_function = None, on_remove_function = None, on_turn_function = None, on_move_function = None, on_day_function = None, dependant_policies = None,
            project_progress = 0, project_cost = 100, category = "",  tier = 0):

            if requirement is None:
                requirement = IT_proj_generic_req_True
            super(IT_Project, self).__init__(name, desc, cost, requirement = requirement, toggleable = toggleable,
                on_buy_function = on_buy_function, extra_arguments = extra_arguments, on_apply_function = on_apply_function, on_remove_function = on_remove_function,
                on_turn_function = on_turn_function, on_move_function = on_move_function, on_day_function = on_day_function, dependant_policies = dependant_policies)
            self.project_progress = project_progress
            self.project_cost = project_cost
            self.category = category
            self.tier = tier
            self.identifier = hash((category, name))

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.category == other.category and self.name == other.name:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return self.identifier

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.category == other.category and self.name == other.name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.category != other.category or self.name != other.name
            return True

        def apply_policy(self):
            mc.business.active_IT_projects.append(self)
            if self.on_apply_function is not None:
                self.on_apply_function(**self.extra_arguments)
            return

        def remove_policy(self):
            if self in mc.business.active_IT_projects:
                mc.business.active_IT_projects.remove(self)
                if self.on_remove_function is not None:
                    self.on_remove_function(**self.extra_arguments)
            return

        def buy_policy(self, ignore_cost = False):  #Only use this function if an IT Project can be outright bought.
            mc.business.IT_projects.append(self)
            if not ignore_cost:
                mc.business.funds -= self.cost
            if self.on_buy_function is not None:
                self.on_buy_function(**self.extra_arguments)
