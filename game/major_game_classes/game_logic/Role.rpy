init -2 python:
    class Role(): #Roles are assigned to special people. They have a list of actions that can be taken when you talk to the person and acts as a flag for special dialogue options.
        def __init__(self, role_name, actions = None, hidden = False, on_turn = None, on_move = None, on_day = None, role_dates = None, looks_like = None, role_trainables = None, internet_actions = None):
            self.role_name = role_name
            self.actions = ActionList(actions)
            self.internet_actions = ActionList(internet_actions)

            # At some point we may want a seperate list of role actions that are available when you text someone.
            self.hidden = hidden #A hidden role is not shown on the "Roles" list
            self.on_turn = on_turn #A function that is run each turn on every person with this Role.
            self.on_move = on_move #A function that is run each move phase on every person with this Role.
            self.on_day = on_day

            if role_dates is None:
                self.role_dates = [] # A role date is an action that should be added to the list of date triggers.
            elif isinstance(role_dates, list):
                self.role_dates = role_dates
            else:
                self.role_dates = [role_dates]

            self.linked_roles = [] #A list of other roles. If this role is removed, all linked roles are removed as well.
            self.looks_like = None
            if isinstance(looks_like, Role):
                self.looks_like = looks_like

            if role_trainables is None: #Trainable entries added when a girl is in a trance.
                self.role_trainables = []
            elif isinstance(role_trainables, list):
                self.role_trainables = role_trainables
            else:
                self.role_trainables = [role_trainables]

        def __cmp__(self,other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.role_name == other.role_name:
                    return 0

            if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.role_name)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.role_name == other.role_name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.role_name != other.role_name
            return True

        @property
        def parent_role(self):
            return self.looks_like

        def check_parent_role(self, the_role):
            if not self.parent_role:
                return False
            if isinstance(the_role, basestring):
                return self.parent_role.role_name == the_role.name or self.parent_role.check_parent_role(the_role)
            if isinstance(the_role, Role):
                return self.parent_role == the_role or self.parent_role.check_parent_role(the_role)
            return False

        def run_turn(self, the_person):
            if self.on_turn is not None:
                self.on_turn(the_person)

        def run_move(self, the_person):
            if self.on_move is not None:
                self.on_move(the_person)

        def run_day(self, the_person):
            if self.on_day is not None:
                self.on_day(the_person)

        def link_role(self, the_role):
            if the_role not in self.linked_roles:
                self.linked_roles.append(the_role)

        def add_action(self, action):
            self.actions.add_action(action)

        def remove_action(self, action):
            self.actions.remove_action(action)

        def has_action(self, action):
            return self.actions.has_action(action)

        def add_internet_action(self, action):
            self.internet_actions.add_action(action)

        def remove_internet_action(self, action):
            self.internet_actions.remove_action(action)
