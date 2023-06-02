init 10 python:
    #Prototypes for an easier way of managing story progress screens. Add an init function to attempt to retain global functionality
    def ashley_story_character_description():
        return "[ashley.name] is [stephanie.name]'s sister and you gave her job in your production department to help her out."

    def ashley_story_love_list():
        love_story_list = {}
        if mc.business.p_div.person_count <= 1:
            love_story_list[0] = "Hire more production staff."
        elif ashley.days_employed < TIER_2_TIME_DELAY:
            love_story_list[0] = "Give [ashley.fname] time to settle into her new job."
        else:
            love_story_list[0] = "Talk to her about going to the classical concert."

        if ashley.progress.love_step == 0:
            if ashley.event_triggers_dict.get("concert_date", 0) == 0:
                return love_story_list
            if ashley.event_triggers_dict.get("concert_date", 0) == 1:
                love_story_list[0] = "Go with [ashley.fname] to the concert on Thursday night."
                return love_story_list

        love_story_list[0] = "You went with [ashley.fname] to a classical music concert."

        if ashley.progress.love_step == 1:
            if ashley.love < 20:
                love_story_list[1] = "Increase your love score with her to progress."
            elif not ashley.story_event_ready("love"):
                love_story_list[1] = "[ashley.fname] needs time before she is ready to progress this story."
            else:
                love_story_list[1] = "[ashley.fname] may approach you at work soon."
            return love_story_list

        love_story_list[1] = "She walked you home, and it seems she already knows your sister."

        if ashley.progress.love_step == 2:
            if ashley.love < 40:
                love_story_list[2] = "Increase [ashley.fname]'s love to at least 40."
            elif not ashley.story_event_ready("love"):
                love_story_list[2] = "[ashley.fname] needs some time to progress this story."
            else:
                love_story_list[2] = "[ashley.fname] will come over this evening."
            return love_story_list

        love_story_list[2] = "[ashley.fname] patched things up with your sister during movie night and they exchanged phone numbers."

        if ashley.progress.love_step == 3:
            if ashley.love < 60:
                love_story_list[3] = "Increase [ashley.fname]'s love to at least 60."
            elif not ashley.story_event_ready("love"):
                love_story_list[3] = "[ashley.fname] needs some time to progress this story."
            else:
                love_story_list[3] = "The next scene has not been written yet."
                #love_story_list[3] = "[ashley.fname] will come over this evening."

            return love_story_list

        love_story_list[3] = "The next scene has not been written yet."
        return love_story_list

    def ashley_story_lust_list():
        lust_story_list = {}

        if ashley.progress.lust_step == 0:
            if ashley.sluttiness < 20:
                lust_story_list[0] = "Increase [ashley.fname]'s sluttiness to progress"
            elif not ashley.story_event_ready("slut"):
                lust_story_list[0] = "[ashley.fname] needs a few days to adjust before progressing."
            else:
                lust_story_list[0] = "You think there will be progress with [ashley.fname] soon."
            return lust_story_list

        if not ashley.event_triggers_dict.get("porn_discovered", False):
            return lust_story_list

        lust_story_list[0] = "You should talk to [ashley.fname]'s sister about the video you found."

        if not ashley.event_triggers_dict.get("porn_discussed", False):
            return lust_story_list

        lust_story_list[0] = "You should talk to [ashley.fname] about the video you found."
        if not ashley.event_triggers_dict.get("porn_convo_avail", False):
            return lust_story_list

        lust_story_list[0] = "[ashley.fname] gave you a handjob after asking her about her porn video."

        if ashley.progress.lust_step == 1:
            if ashley.sluttiness < 40:
                lust_story_list[1] = "Increase [ashley.fname]'s sluttiness to progress"
            elif not ashley.story_event_ready("slut"):
                lust_story_list[1] = "[ashley.fname] needs a few days to adjust before progressing."
            elif not ashley.is_willing(blowjob):
                lust_story_list[1] = "[ashley.fname] needs to be willing to give blowjobs to progress."
            else:
                lust_story_list[1] = "You think there will be progress with [ashley.fname] soon."
            return lust_story_list

        lust_story_list[1] = "She gave you a blowjob while her sister was asking for advice!"

        if ashley.progress.lust_step == 2:
            lust_story_list[2] = "The rest of the story has not yet been written."


        #lust_story_list[1] = "You should talk to [ashley.fname] ASAP about the handjob."
        #lust_story_list[1] = "You should talk to [ashley.fname]'s sister about your relationships."

        return lust_story_list

    def ashley_story_obedience_list():
        obedience_story_list = {}

        if ashley.progress.obedience_step == 0:
            if ashley.obedience < 120:
                return {
                    0: "Increase [ashley.fname]'s obedience to progress."
                }
            elif ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
                return {
                    0: "Wait a few days to progress."
                }

            obedience_story_list[0] = "Use obedience to convince [ashley.fname] to let you use her tits again."
            return obedience_story_list

        obedience_story_list[0] = "You've convinced [ashley.fname] to let you fuck her tits anytime you want."

        if ashley.progress.obedience_step == 1:
            if ashley.obedience < 150:
                obedience_story_list[1] = "Increase [ashley.fname]'s obedience to progress."
                return obedience_story_list
            elif ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
                obedience_story_list[1] = "Wait a few days to progress."
                return obedience_story_list

            obedience_story_list[1] = "Use obedience to convince [ashley.fname] to blow you again."
            return obedience_story_list

        obedience_story_list[1] = "[ashley.fname]'s mouth is available for your use whenever you want."

        if ashley.progress.obedience_step == 2:
            if ashley.obedience < 180:
                obedience_story_list[2] = "Increase [ashley.fname]'s obedience to progress."
                return obedience_story_list
            elif ashley.days_since_event("obedience_event") < TIER_1_TIME_DELAY:
                obedience_story_list[2] = "Wait a few days to progress."
                return obedience_story_list


            obedience_story_list[2] = "The next scene has not been written yet!"
            return obedience_story_list


        return obedience_story_list

    def ashley_story_teamup_list():
        teamup_story_list = {}

        teamup_story_list[0] = [stephanie, "[ashley.fname] and her sister would make an interesting pair to get together, but right now that seems impossible."]
        if ashley.progress.love_step >= 2:
            teamup_story_list[1] = [lily, "[ashley.fname] and your sister already seem to know eachother. What might happen if you work on repairing their relationship?"]

        return teamup_story_list

    def ashley_story_other_list():
        other_story_list = {}
        if ashley.is_employee:
            other_story_list[0] = "You hired her as your production assistant"
        else:
            other_story_list[0] = "You did not hire her, locking you out of her stories."

        if ashley.event_triggers_dict.get("story_path", None) == "secret":
            other_story_list[1] = "You are keeping your relationship with [ashley.fname] a secret for now."
        elif ashley.event_triggers_dict.get("story_path", None) == "fwb":
            other_story_list[1] = "You are keeping your relationship with [ashley.fname] casual for now."

        if ashley_mc_submission_story_complete():
            other_story_list[2] = "[ashley.fname] had a plan to dominate you, but abandoned it."
        else:
            if ashley.event_triggers_dict.get("dom_fingers", False):
                other_story_list[2] = "[ashley.fname] sometimes requires you to finger her after work."

            if ashley.event_triggers_dict.get("dom_oral", False):
                other_story_list[3] = "[ashley.fname] sometimes requires you to go down on her after work."

            if ashley.event_triggers_dict.get("dom_fuck", False):
                other_story_list[4] = "[ashley.fname] fucks you after work whenever she wants."

        if False: # need to set flags for this
            other_story_list[5] = "[ashley.fname] has given you a serum for personal use."
            other_story_list[5] = "[ashley.fname] can give you serums for personal use."


        if False: # not yet written
            other_story_list[5] = "She has found a serum candidate that causes intense female libido that may be worth studying."

        #Ashley's other story indices:
        # 0 - Her attempting to get MC obedient
        # 1 - Your arrangement with Stephanie
        # 2 - arousal serum quest
        return other_story_list
