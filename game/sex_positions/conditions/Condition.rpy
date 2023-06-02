#This is the class for the condition
#Condition is used for non standard sex.
#Pretty much all params are optional. If they exist, they get called during sex at the appropriate times.


init -2 python:
    class Condition_Type():
        def __init__(self, name, pre_label = None, post_label = None, position_whitelist = None, position_blacklist = None, reward_cond = None, reward_label = None, fail_label = None):
            self.name = name #A descriptive name of the contract.
            self.pre_label = pre_label  #Run this label before each sex round
            self.post_label = post_label    #Run this label after each sex round
            self.position_whitelist = position_whitelist    #Only positions on this list will be available
            self.position_blacklist = position_blacklist    #Positions on this list will NOT be available
            self.reward_cond = reward_cond          #Conditions to check for a reward
            self.reward_label = reward_label        #label to call for rewarded sequence.
            self.fail_label = fail_label
            self.condition_vars = []

            return

        def call_pre_label(self, the_person, the_position, the_object, report_log):
            if self.pre_label:
                renpy.call(self.pre_label, the_person, the_position, the_object, report_log, self)
            return

        def call_post_label(self, the_person, the_position, the_object, report_log):
            if self.post_label:
                renpy.call(self.post_label, the_person, the_position, the_object, report_log, self)
            return

        def filter_condition_positions(self, the_position):
            if self.position_whitelist:
                return the_position in self.position_whitelist
            if self.position_blacklist:
                return the_position not in self.position_blacklist
            return True

        def run_rewards(self, the_person, report_log):
            if self.reward_cond:
                if self.reward_cond(self, the_person, report_log):
                    renpy.call(self.reward_label, the_person, report_log, self)
                elif self.fail_label:
                    renpy.call(self.fail_label, the_person, report_log, self)
            return
