init 10 python:
    #Prototypes for an easier way of managing story progress screens. Add an init function to attempt to retain global functionaliy
    def camilla_story_character_description():
        return "A married lifestyle coach who frequents the bar in the evening."

    def camilla_story_love_list():
        love_story_list = {}

        if not camilla.event_triggers_dict.get("met", False):
            love_story_list[0] = "Look for [camilla.name] at the bar in the evening"
            return love_story_list

        if camilla.love < 20:
            love_story_list[0] = "Increase [camilla.name]'s love to 20"
        if not camilla.story_event_ready("love"):
            love_story_list[0] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != mall:
            love_story_list[0] = "Meet [camilla.name] when she is working at the mall"


        if not camilla.event_triggers_dict.get("help_with_outfit", False):
            return love_story_list

        love_story_list[0] = "[camilla.name] asked your opinion on date night outfits."

        if camilla.love < 40:
            love_story_list[1] = "Increase [camilla.name]'s love to 40"
        if not camilla.story_event_ready("love"):
            love_story_list[1] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != mall:
            love_story_list[1] = "Meet [camilla.name] when she is working at the mall"

        if not camilla.event_triggers_dict.get("help_with_lingerie", False):
            return love_story_list

        love_story_list[1] = "[camilla.name] tried on lingerie for you and you had fun in the dressing room with her."

        if camilla.love < 60:
            love_story_list[2] = "Increase [camilla.name]'s love to 60"
        else:
            love_story_list[2] = "[camilla.name] will contact you and continue this story when the time is right"

        if not camilla.event_triggers_dict.get("formal_date", False):
            return love_story_list

        love_story_list[2] = "You went on a formal date with [camilla.name] and had a one night stand."

        love_story_list[3] = "This next story step is not yet written"

        # camilla.love_messages[3] = "As an act of retribution to her husband, [camilla.name] gave you her anal virginity."


        return love_story_list

    def camilla_story_lust_list():
        lust_story_list = {}

        if camilla.sluttiness < 20:
            lust_story_list[0] = "Raise her sluttiness to 20"

        if not camilla.event_triggers_dict.get("go_dancing", False):
            lust_story_list[0] = "Go dancing with [camilla.name] on Wednesday"
            return lust_story_list

        lust_story_list[0] = "You can now go salsa dancing with [camilla.name] at the bar"

        if camilla.sluttiness < 40:
            lust_story_list[1] = "Raise her sluttiness to 40"
        if not camilla.story_event_ready("slut"):
            lust_story_list[1] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != downtown_bar:
            lust_story_list[1] = "Talk to [camilla.name] at the bar in the evening"

        if not camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 0) == 0:
            return lust_story_list

        lust_story_list[1] = "[camilla.name] sucked you off in the bar restroom while you took pictures for her husband"

        if camilla.sluttiness < 60:
            lust_story_list[2] = "Raise her sluttiness to 60"
        if mc_dancing_skill() <= 6:
            lust_story_list[2] = "Increase you dancing skill to continue this story"
        if not camilla.story_event_ready("slut"):
            lust_story_list[2] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != downtown_bar:
            lust_story_list[2] = "Talk to [camilla.name] at the bar in the evening"

        if not camilla.event_triggers_dict.get("bathroom_sex", False):
            return lust_story_list

        lust_story_list[2] = "You fucked [camilla.name] after a night of dancing"

        if camilla.sluttiness < 80:
            lust_story_list[3] = "Raise her sluttiness to 80"
        if not camilla.story_event_ready("slut"):
            lust_story_list[3] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != downtown_bar:
            lust_story_list[3] = "Talk to [camilla.name] at the bar in the evening"

        if not camilla.event_triggers_dict.get("home_sex", False):
            return lust_story_list

        lust_story_list[3] = "You fucked [camilla.name] in her own bedroom while her husband watched"
        lust_story_list[4] = "This story step is not yet written"

        return lust_story_list

    def camilla_story_obedience_list():
        obedience_story_list = {}

        if camilla.obedience < 120:
            obedience_story_list[0] = "Increase [camilla.name]'s obedience to 120"
        if not camilla.story_event_ready("obedience"):
            obedience_story_list[0] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != mall:
            obedience_story_list[0] = "Talk to [camilla.name] when she is at the mall"

        if not camilla.event_triggers_dict.get("goal_coach", False):
            return obedience_story_list

        obedience_story_list[0] = "You got [camilla.name] to help you make new business goals"

        if camilla.obedience < 140:
            obedience_story_list[1] = "Increase [camilla.name]'s obedience to 140"
        if not camilla.story_event_ready("obedience"):
            obedience_story_list[1] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != mall:
            obedience_story_list[1] = "Talk to [camilla.name] when she is at the mall"

        if not camilla.event_triggers_dict.get("sex_goal_coach", False):
            return obedience_story_list

        obedience_story_list[1] = "You got [camilla.name] to help you make new sexual goals"

        if camilla.obedience < 160:
            obedience_story_list[2] = "Increase [camilla.name]'s obedience to 160"
        if not camilla.story_event_ready("obedience"):
            obedience_story_list[2] = "[camilla.name] needs time before she is ready to progress this story"
        if camilla.location != mall:
            obedience_story_list[2] = "Talk to [camilla.name] when she is at the mall"

        if not camilla.event_triggers_dict.get("obedience_titfuck", False):
            return obedience_story_list

        obedience_story_list[2] = "[camilla.name] helped you realize your love for tits, when you finished all over hers."

        if camilla.obedience < 180:
            obedience_story_list[3] = "Increase [camilla.name]'s obedience to 180"
            return False
        if not camilla.story_event_ready("obedience"):
            obedience_story_list[3] = "[camilla.name] needs time before she is ready to progress this story"
            return False
        if camilla.location != mall:
            obedience_story_list[3] = "Talk to [camilla.name] when she is at the mall"


        obedience_story_list[4] = "The next story step has not yet been written."

        return obedience_story_list

    def camilla_story_teamup_list():
        return {
            0: [alexia, "This teamup is not yet written"],
            1: [nora, "This teamup is not yet written"]
        }

    def camilla_story_other_list():
        #camilla's other story indices:
        # 0 - Her relationship with her husband
        # 1 - Your salsa dancing skill level
        # 2 - Her fertility progress (if any)
        other_story_list = {}

        if camilla.event_triggers_dict.get("bar_met", False):
            other_story_list[0] = "[camilla.name] is happily married but in an open marriage"
            other_story_list[1] = "[camilla.name] doesn't have any children"

        dancing_skill = str(mc_dancing_skill())
        other_story_list[2] = "Your skill level at salsa dancing is "+ dancing_skill + " / 20"
        if camilla.event_triggers_dict.get("bathroom_sex", False):
            other_story_list[3] = "[camilla.name] is infertile"

        return other_story_list
