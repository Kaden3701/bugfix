#Use this for recording a onlyfans session.

init -1 python:
    def condition_onlyfans_recording_reward_req(self, the_person, report_log):
        if report_log.get("guy orgasms", 0) > 0:   #She finished off MC
            return True
        return False


    def make_condition_onlyfans_recording():
        onlyfans_recording_blacklist = [anal_swing, missionary, breeding_missionary, doggy_anal_dildo_dp, piledriver_anal, piledriver_dp, spanking, standing_dildo, against_wall, kissing, piledriver, standing_grope]  #We should blacklist any position that would require both of MC's hands
        onlyfans_recording_condition = Condition_Type("Blowjob Training", pre_label = "condition_onlyfans_recording_pre_label", post_label = "condition_onlyfans_recording_post_label", position_blacklist = onlyfans_recording_blacklist,
            reward_cond = condition_onlyfans_recording_reward_req, reward_label = "condition_onlyfans_recording_reward_label")
        onlyfans_recording_condition.condition_vars.append(False) #Initialize this to false so in the first pre label we can mention getting the phone camera ready
        onlyfans_recording_condition.condition_vars.append(0)     #Female orgasms
        onlyfans_recording_condition.condition_vars.append(0)     #Male orgasms
        return onlyfans_recording_condition


label condition_onlyfans_recording_pre_label(the_person, the_position, the_object, report_log, the_condition):
    if the_condition.condition_vars[0]:
        "You check the phone, trying to make sure you are keeping the action in view while you [the_position.verb] [the_person.title]."
    else:
        mc.name "Here, let me see your phone. I'll take an OnlyFans video while I'm [the_position.verbing] you."
        the_person "Okay."
        "[the_person.title] gets out her phone, unlocks it, and loads up the OnlyFans app before handing it to you."
        mc.name "Alright, recording! Let's do this."
        $ the_condition.condition_vars[0] = True
    return

label condition_onlyfans_recording_post_label(the_person, the_position, the_object, report_log, the_condition):
    if report_log.get("girl orgasms", 0) > the_condition.condition_vars[1] and report_log.get("guy orgasms", 0) > the_condition.condition_vars[2]:  #you finished together
        "You aren't sure if you managed to keep the finale in focus, but you're sure the sounds of [the_person.title] cumming with you were hot."
        "You stop [the_position.verbing] her for a moment to make sure you capture the aftermath of your orgasm."
    elif report_log.get("girl orgasms", 0) > the_condition.condition_vars[1]: #she orgasmed
        "You keep [the_position.verbing] her, keeping her in frame as she cums for the video."
    elif report_log.get("guy orgasms", 0) > the_condition.condition_vars[2]:
        "You stop [the_position.verbing] her for a moment to make sure you capture the aftermath of your orgasm."
    $ the_condition.condition_vars[1] = report_log.get("girl orgasms", 0)
    $ the_condition.condition_vars[2] = report_log.get("guy orgasms", 0)
    return

label condition_onlyfans_recording_reward_label(the_person, report_log, the_condition):
    $ the_person.change_stats(slut = 2, max_slut = 80, obedience = 3)
    "[the_person.possessive_title] seems pleased she managed to get you off during the video."
    return
