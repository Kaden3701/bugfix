init -2 python:
    class Goal():
        def __init__(self, goal_name, goal_description, event_name, listener_type, valid_goal_function, on_trigger_function, arg_dict = None, difficulty_scale_function = None, report_function = None, progress_fraction_function = None, mandatory = False, enabled = True):
            self.name = goal_name #Short form name to be displayed to the player, generally on a progress bar of some sort.
            self.description = goal_description #A long form fluff description of the goal purpose.
            self.event_name = event_name #The event (aka a string to give to a listener manager) that this goal listens to.
            self.listener_type = listener_type #Either "MC" or "Business", decides which object the goal will grab as their listener manager when you ask it to enroll.
            self.valid_goal_function = valid_goal_function #A function called to check to see if the goal is a valid/reasonable one to give to the player. Also is used to make sure goals aren't completed when they are assigned.
            self.on_trigger_function = on_trigger_function #A function called by an event listener that that this goal is hooked up to.
            if arg_dict: #A dict to hold arguments you want to be used by the on_trigger function without having to get specific about what they are here.
                self.arg_dict = arg_dict
            else:
                self.arg_dict = {}

            self.completed = False #A flag set to true when the goal is finished, so the player can complete the objective and claim their bonus point.

            self.difficulty_scale_function = difficulty_scale_function #A function called when the goal is activated (aka when it is copied from the default goal) to scale the parameters to the current difficulty.
            self.report_function = report_function
            self.progress_fraction_function = progress_fraction_function
            self.mandatory = mandatory
            self.enabled = enabled

        def __cmp__(self,other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.name == other.name:
                    return 0

            if self.__hash__() > other.__hash__():
                return 1
            else:
                return -1

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.name == other.name
            return False

        def __neq__(self, other):
            if isinstance(self, other.__class__):
                return self.name != other.name
            return True

        def check_valid(self, difficulty):
            if self.valid_goal_function is not None:
                return self.valid_goal_function(self, difficulty)
            else:
                return True #If a goal does not have a valid goal function it is always valid.

        def activate_goal(self, difficulty):
            if self.listener_type == "MC": #Figure out what listener we should be listening to
                listener = mc.listener_system
            else: #== "Business"
                listener = mc.business.listener_system

            if self.difficulty_scale_function:
                self.difficulty_scale_function(self, difficulty) #If we have a function for changing difficulty hand it ourselves and the difficulty we were activated at.

            listener.enroll_goal(self.event_name, self) #Enroll us to the proper listener and hand it us so it will call our trigger when we need it to.

        @property
        def progress_string(self): #Returns a string corresponding to the current progress of the goal. Generally something like "5 of 10" or "3/20".
            if self.completed:
                return "Completed"
            if self.report_function:
                return self.report_function(self)
            return "In Progress"

        @property
        def progress_fraction(self):
            if self.progress_fraction_function:
                return self.progress_fraction_function(self)
            return 0.0

        def call_trigger(self, **kwargs):
            return self.on_trigger_function(self, **kwargs)

        def complete_goal(self):
            self.completed = True

        def toggle_enabled(self):
            def enable_in_list(the_goal, the_list):
                found = next((x for x in the_list if x == the_goal), None)
                if not found:
                    the_list.append(the_goal)
                    the_goal.enabled = True

            def disable_in_list(the_goal, the_list):
                if __builtin__.len(the_list) < 3: # minimum of two active items
                    return
                found = next((x for x in the_list if x == the_goal), None)
                if found:
                    the_list.remove(found)
                    the_goal.enabled = False

            #renpy.notify(self.name + " is now [" + str(hex(id(self))) + "] :" + str(self.enabled))
            if not self.enabled:
                if self in stat_goals_options_list:
                    enable_in_list(self, stat_goals)
                if self in work_goals_options_list:
                    enable_in_list(self, work_goals)
                if self in sex_goals_options_list:
                    enable_in_list(self, sex_goals)
            else:
                if self in stat_goals_options_list:
                    disable_in_list(self, stat_goals)
                if self in work_goals_options_list:
                    disable_in_list(self, work_goals)
                if self in sex_goals_options_list:
                    disable_in_list(self, sex_goals)
            return
