# Use this condition for taking someone's virginity

init -1 python:
    def condition_taking_virginity_reward_req(self, the_person, report_log):
        if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) > 0:   #both finished
            return True
        return False


    def make_condition_taking_virginity():
        taking_virginity_whitelist = [missionary, doggy, standing_doggy, cowgirl]    #Mostly vanilla positions
        taking_virginity_condition = Condition_Type("Taking Virginity", pre_label = "condition_taking_virginity_pre_label", post_label = "condition_taking_virginity_post_label", position_whitelist = taking_virginity_whitelist,
            reward_cond = condition_taking_virginity_reward_req, reward_label = "condition_taking_virginity_reward_label")
        taking_virginity_condition.condition_vars.append(False) #Initialize this to false so in the first pre label we can mention getting the phone camera ready
        taking_virginity_condition.condition_vars.append(0)     #Female orgasms
        taking_virginity_condition.condition_vars.append(0)     #Male orgasms
        return taking_virginity_condition


label condition_taking_virginity_pre_label(the_person, the_position, the_object, report_log, the_condition):
    if the_condition.condition_vars[0]:
        $ the_person.change_arousal(-5)
        if the_person.arousal_perc < 50:
            "[the_person.possessive_title] whimpers in a mixture of pain and pleasure as you continue to fuck her for the first time."
        elif the_person.arousal_perc < 85 and the_condition.condition_vars[1] == 0:
            "[the_person.possessive_title] is starting to moan in pleasure from the incredible sensations your cock is giving her."
        else:
            "[the_person.possessive_title] is moaning constantly, in awe of the pleasure she is experiencing for the first time."
    else:
        $ the_person.change_arousal(-50)
        "You've finally done it. You've taken [the_person.possessive_title]'s virginity."
        "It was painful for her, and she whimpers a bit once you are fully inside of her."
        "You give her several moments to adjust."
        the_person "Okay... I think I'm ready... you can start moving..."
        "You take it nice and slow at first, savoring [the_person.title]'s first time."
        $ the_condition.condition_vars[0] = True
    return

label condition_taking_virginity_post_label(the_person, the_position, the_object, report_log, the_condition):
    pass
    return

label condition_taking_virginity_reward_label(the_person, report_log, the_condition):
    $ the_person.change_stats(slut = 2, max_slut = 80, obedience = 15)
    "[the_person.possessive_title] is amazed. She seems to be in disbelief how pleasurable it was."
    the_person "[the_person.mc_title], that was so good! I can't believe I've been missing out on that for so long..."
    the_person "You can do that to me any time... okay?"
    return
