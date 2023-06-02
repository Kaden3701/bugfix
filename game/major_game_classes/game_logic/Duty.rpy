## A duty is similar to a Role, but it's mechanics are controlled by the business.
# -> Duties are given to employees of the MC's business, capped at that employees seniority level.
# -> Seniority levels are 1(intern, green employee), 2 (standard employee), 3(senior employee, department head).
# -> Duties are checked to add role actions/dates/interactions in the same way as roles.
init -2 python:
    class Duty():
        def __init__(self, duty_name, duty_description, requirement_function = None,
            actions = None, internet_actions = None,
            on_turn_function = None, on_move_function = None, on_day_function = None,
            on_apply_function = None, on_remove_function = None,
            duty_trainables = None, only_at_work = True):

            #TODO: Have a "smalltalk" label that can be called whenever you talk to a girl, she'll talk to you about her recent duties and what that entails.
            #TODO: Have an "on entrance" label that can be called instead of the generic greetings when you enter the room so it can tie into their active duties.

            self.duty_name = duty_name  #A short slug that can be shown in a menu, UI, etc.
            self.duty_description = duty_description # A paragraph to describe what this duty is, both flavour and effect
            self.actions = ActionList(actions)
            self.internet_actions = ActionList(internet_actions)

            self.requirement_function = requirement_function

            self.on_turn_function = on_turn_function
            self.on_move_function = on_move_function
            self.on_day_function = on_day_function

            self.on_apply_function = on_apply_function
            self.on_remove_function = on_remove_function

            self.only_at_work = only_at_work # Only run on_turn, on_move only when the employee is at work. Only run on_day when the employee went to work that day.

            if duty_trainables is None:
                self.duty_trainables = []
            elif isinstance(duty_trainables, list):
                self.duty_trainables = duty_trainables
            else:
                self.duty_trainables = [duty_trainables]

            if duty_trainables is None:
                self.duty_trainables = []
            elif isinstance(duty_trainables, list):
                self.duty_trainables = duty_trainables
            else:
                self.duty_trainables = [duty_trainables]

        def __cmp__(self,other): ##This and __hash__ are defined so that I can use "if Action in List" and have it find identical actions that are different instances.
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.duty_name == other.duty_name and self.requirement_function == other.requirement_function \
                    and self.on_turn_function == other.on_turn_function and self.on_move_function == other.on_move_function \
                    and self.on_day_function == other.on_day_function and self.on_apply_function == other.on_apply_function \
                    and self.on_remove_function == other.on_remove_function and self.only_at_work == other.only_at_work:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(tuple([self.duty_name,
                self.requirement_function,
                self.on_turn_function,
                self.on_move_function,
                self.on_day_function,
                self.on_apply_function,
                self.on_remove_function,
                self.only_at_work
                ]))

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.duty_name == other.duty_name and self.requirement_function == other.requirement_function \
                    and self.on_turn_function == other.on_turn_function and self.on_move_function == other.on_move_function \
                    and self.on_day_function == other.on_day_function and self.on_apply_function == other.on_apply_function \
                    and self.on_remove_function == other.on_remove_function and self.only_at_work == other.only_at_work
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.duty_name != other.duty_name or self.requirement_function != other.requirement_function \
                    or self.on_turn_function != other.on_turn_function or self.on_move_function != other.on_move_function \
                    or self.on_day_function != other.on_day_function or self.on_apply_function != other.on_apply_function \
                    or self.on_remove_function != other.on_remove_function or self.only_at_work != other.only_at_work
            return True

        def check_requirement(self, the_person):
            if callable(self.requirement_function):
                return self.requirement_function(the_person)
            return True

        def on_turn(self, the_person):
            if callable(self.on_turn_function):
                self.on_turn_function(the_person)

        def on_move(self, the_person):
            if callable(self.on_move_function):
                self.on_move_function(the_person)

        def on_day(self, the_person):
            if callable(self.on_day_function):
                self.on_day_function(the_person)

        def on_apply(self, the_person):
            if callable(self.on_apply_function):
                self.on_apply_function(the_person)

        def on_remove(self, the_person):
            if callable(self.on_remove_function):
                self.on_remove_function(the_person)

        def add_action(self, action):
            self.actions.add_action(action)

        def remove_action(self, action):
            self.actions.remove_action(action)

        def add_internet_action(self, action):
            self.internet_actions.add_action(action)

        def remove_internet_action(self, action):
            self.internet_actions.remove_action(action)
