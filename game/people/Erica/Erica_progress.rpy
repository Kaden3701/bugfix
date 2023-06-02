init 10 python:
    def erica_story_character_description():
        return "A collegiate track and field athlete."

    def erica_story_love_list():
        love_story_list = {}
        if erica_get_is_doing_yoga_sessions() and erica_get_is_doing_insta_sessions():
            love_story_list[0] = "You helped [erica.name] earn some extra money doing InstaPic and Yoga."
        elif erica_get_is_doing_yoga_sessions():
            love_story_list[0] = "You helped [erica.name] earn some extra money doing Yoga."
            love_story_list[1] = "Try working with [lily.title] to help [erica.name] earn some extra money."
            return love_story_list
        elif erica_get_is_doing_insta_sessions():
            love_story_list[0] = "You helped [erica.name] earn some extra money doing InstaPic with [lily.title]."
            love_story_list[1] = "Try working with your HR Director to help [erica.name] earn some extra money."
            return love_story_list
        elif erica_is_looking_for_work():
            love_story_list[0] = "[erica.name] is looking for some part time work."
            love_story_list[1] = "Try working with your HR director or [lily.title] to help her find some extra work!"
            return love_story_list
        elif erica.love <20:
            love_story_list[0] = "Try increasing [erica.name]'s love score."
            return love_story_list
        else:
            love_story_list[0] = "Try getting to know [erica.name] better."
            return love_story_list

        if erica_pre_insta_blowjob_complete():
            love_story_list[1] = "[erica.name] showed her appreciation by giving you a blowjob before an InstaPic session!"
        elif erica.love <= 40:
            love_story_list[1] = "Try increasing her love to continue this story."
            return love_story_list
        elif not erica.is_willing(blowjob):
            love_story_list[1] = "[erica.name] needs to be willing to give you a blowjob. Make sure her sluttiness is high enough and she doesn't hate that act!"
            return love_story_list
        else:
            love_story_list[1] = "Make sure to be there to take pics for [erica.name] and [lily.title]'s next InstaPic session."
            return love_story_list

        if erica_post_yoga_fuck_complete():
            love_story_list[2] = "You couldn't stop watching [erica.name] during your company yoga. She loved it and you fucked her after against your office wall."
        elif erica.love <= 60:
            love_story_list[2] = "Try increasing her love to continue this story."
            return love_story_list
        elif not erica.is_willing(against_wall):
            love_story_list[2] = "[erica.name] needs to be willing to fuck you against the wall. Make sure her sluttiness is high enough and she doesn't hate that act!"
            return love_story_list
        else:
            love_story_list[2] = "Make sure to attend company yoga on Tuesday morning to continue this story."
            return love_story_list

        love_story_list[3] = "There is nothing more in this story line at this time."
        return love_story_list

    def erica_story_lust_list():
        lust_story_list = {}

        if erica_has_given_morning_handjob():
            lust_story_list[0] = "[erica.name] woke you up with a handjob after spending the night with [lily.fname]."
            lust_story_list[1] = "Talk to her if you want her to wake you up more or less often."
        elif not erica.is_willing(cowgirl_handjob):
            lust_story_list[0] = "[erica.name] needs to be willing to give a handjob to continue this story. Try raising her sluttiness and check her opinions."
            return lust_story_list
        elif not erica_get_is_doing_insta_sessions():
            lust_story_list[0] = "Try advancing [erica.name]'s love story to unlock this."
            return lust_story_list
        else:
            lust_story_list[0] = "[erica.name] may try sneaking into your room some morning..."
            return lust_story_list

        if erica_get_progress() > 1:
            lust_story_list[1] = "You worked out with [erica.name] and had some fun in the gym locker room afterwords."
        elif erica_get_progress() == 1:
            lust_story_list[1] = "Try working out with [erica.name] sometime."
            return lust_story_list
        elif mc.max_energy < 120:
            lust_story_list[1] = "[erica.name] prefers athletic guys. Try raising your maximum energy."
            return lust_story_list
        elif erica.sluttiness < 40:
            lust_story_list[1] = "Try raising [erica.name]'s sluttiness to continue this story."
            return lust_story_list

        if erica_get_progress() >= 4:
            lust_story_list[2] = "You won a bet with [erica.name] in a race, then fucked her at her place."
        elif erica_get_progress() == 3:
            lust_story_list[2] = "You've challenged [erica.name] to a race. To the victor go the spoils!"
            return lust_story_list
        elif erica.sluttiness < 60:
            lust_story_list[2] = "Try raising [erica.name]'s sluttiness to continue this story."
            return lust_story_list
        elif mc.max_energy < 140:
            lust_story_list[2] = "[erica.name] prefers athletic guys. Try raising your maximum energy."
            return lust_story_list
        else:
            lust_story_list[2] = "Try challenging [erica.name] to a race."
            return lust_story_list

        lust_story_list[3] = "There is nothing more in this story line at this time."

        return lust_story_list

    def erica_story_teamup_list():
        teamup_story_list = {}
        #Yoga
        if erica_get_is_doing_yoga_sessions():
            teamup_story_list[0] = [sarah,"Watch [erica.name] do yoga with [sarah.fname] every Tuesday morning at the office!"]
        elif not erica.event_triggers_dict.get("yoga_quest_started", False):
            teamup_story_list[0] = [sarah,"Try progressing [erica.name]'s story."]
        elif len(erica_get_yoga_class_list()) < 4:
            teamup_story_list[0] = [sarah,"Help [sarah.fname] convince employees to like or love yoga."]
        else:
            teamup_story_list[0] = [sarah,"Talk to [erica.name] about hosting a company yoga class."]

        #Insta
        if erica_get_is_doing_insta_sessions():
            teamup_story_list[1] = [lily,"Help [erica.name] take InstaPics with [lily.fname] every Saturday night in [lily.fname]'s bedroom!"]
        elif not erica_is_looking_for_work():
            teamup_story_list[1] = [lily, "Try progressing [erica.name]'s story."]
        elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
            teamup_story_list[1] = [lily, "Try advancing [lily.fname]'s storyline."]
        else:
            teamup_story_list[1] = [lily, "Try talking to [lily.fname] and [erica.name] about money issues."]

        #Study
        if kaya_studies_with_erica():
            if kaya_erica_teamup.get_stage() == 0:
                teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] study together on Tuesday nights."]
            elif kaya_erica_teamup.get_stage() == 1:
                teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] study together on Tuesday nights, sometimes getting naked for you."]
            elif kaya_erica_teamup.get_stage() == 2:
                teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] study together on Tuesday nights, sometimes letting you spank them."]
            elif kaya_erica_teamup.get_stage() == 3:
                teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] study together on Tuesday nights, sometimes sucking you off."]
            elif kaya_erica_teamup.get_stage() == 4:
                teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] study together on Tuesday nights, and are down for a threesome after!"]
        elif kaya_has_finished_intro():
            teamup_story_list[2] = [kaya,"[erica.name] and [kaya.fname] are both college students..."]
        return teamup_story_list

    def erica_story_other_list():
        other_info_list = {}
        if erica_get_progress() > 1:
            other_info_list[0] = "[erica.name] likes to workout with you at the gym, especially what happens after..."
        if erica_get_progress() >= 4:
            other_info_list[1] = "You are always welcome at [erica.name]'s house at night."
        if erica_fetish_is_kicked_off_team() and not erica_fetish_rejoin_team():
            other_info_list[2] = "[erica.name] got kicked off the track team for getting pregnant! Try talking to [nora.fname]."
        if erica_fetish_rejoin_team():
            other_info_list[3] = "You helped [erica.name] rejoin the track team after knocking her up."

        return other_info_list
