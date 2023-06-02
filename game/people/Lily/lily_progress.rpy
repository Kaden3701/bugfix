init 10 python:
    def lily_story_character_description():
        return "Your younger sister. Attends classes at the local university and often hard up for cash."

    def lily_story_love_list():
        love_story_list = {}
        if not lily_can_give_serum():
            love_story_list[0] = "[lily.name] may talk to you about earning some money soon!"
            return love_story_list
        else:
            love_story_list[0] = "[lily.name] agreed to help you test your serums."

        if lily.is_girlfriend:
            love_story_list[1] = "[lily.name] has agreed to be your girlfriend!"
        elif lily.love < 60:
            love_story_list[1] = "[lily.name] minimum love of 60 to consider being your girlfriend."
            return love_story_list
        elif not mom.event_triggers_dict.get("sister_girlfriend_ask_blessing", False):
            love_story_list[1] = "Work on getting [mom.name] to accept your relationship."
            return love_story_list
        else:
            love_story_list[1] = "You might be able to convince [lily.name] to be your girlfriend if you try."
            return love_story_list

        love_story_list[2] = "There is nothing more in this story line at this time."
        return love_story_list

    def lily_story_lust_list():
        if not lily_can_give_serum():
            return {
                0: "Work on [lily.name]'s love story first."
            }

        #Insta start
        lust_story_list = {}
        if lily.sluttiness < 20:
            return {
                0: "Get [lily.name] to 20 sluttiness."
            }
        elif lily_started_insta_story():
            lust_story_list[0] = "You helped [lily.name] take pictures for InstaPic."
        else:
            return {
                0: "Try entering [lily.name]'s room when she is alone there."
            }

        #Stripping
        if lily_will_strip():
            lust_story_list[1] = "[lily.name] offered to strip for you for extra cash!"
        elif lily.sluttiness < 30:
            lust_story_list[1] = "Raise [lily.name]'s sluttiness to at least 30 to continue this story."
            return lust_story_list
        elif lily_get_serums_tested() < 4:
            lust_story_list[1] = "Have [lily.name] test " + str(4 - lily_get_serums_tested()) + " more serums."
            return lust_story_list

        lust_story_list[2] = "There is nothing more in this story line at this time."

        return lust_story_list

    def lily_story_teamup_list():
        teamup_story_list = {}
        if erica_get_is_doing_insta_sessions():
            teamup_story_list[0] = [erica,"Help [erica.name] take InstaPics with [lily.name] every Saturday night in [lily.name]'s room!"]
        elif not erica_is_looking_for_work():
            teamup_story_list[0] = [erica,"Try progressing [erica.name]'s story."]
        elif lily.event_triggers_dict.get("sister_instathot_pic_count", 0) == 0:
            teamup_story_list[0] = [erica,"Try advancing [lily.name]'s storyline."]
        else:
            teamup_story_list[0] = [erica,"Try talking to [lily.name] and [erica.name] about money issues."]

        if mc.business.event_triggers_dict.get("family_threesome", False):
            teamup_story_list[1] = [mom,"You've slept with [lily.name] and [mom.name] at the same time!"]
        elif lily_mom_topless_pics_complete():
            teamup_story_list[1] = [mom,"You've convinced [lily.name] and [mom.name] to take topless InstaPics!"]
        elif lily_mom_insta_started():
            teamup_story_list[1] = [mom,"You've convinced [lily.name] and [mom.name] to take InstaPics together."]
        else:
            teamup_story_list[1] = [mom,"Getting [lily.name] and [mom.name] together seems impossible... but is it?"]

        if ashley.progress.love_step >= 2:
            teamup_story_list[2] = [ashley, "Your sister and [ashley.fname] already seem to know eachother. What might happen if you work on repairing their relationship?"]

        # This is currently not available
        #if kaya_has_finished_intro():
        #    teamup_story_list[3] = [kaya,"The [lily.name] and [kaya.name] teamup is in progress but not yet written."]

        return teamup_story_list

    def lily_story_other_list():
        story_other_list = {}
        if lily_can_give_serum():
            story_other_list[0] = "[lily.name] will test your serums for $50"
        if lily_will_strip():
            story_other_list[1] = "[lily.name] will strip for you for $100"
        if lily_started_insta_story():
            story_other_list[2] = "You can help [lily.name] take pictures for her InstaPic account."
        return story_other_list




#Use this for lily based wrappers to make coding above stuff easier.
init 9 python:
    def lily_can_give_serum():
        return mc.business.event_triggers_dict.get("sister_serum_test", False)

    def lily_get_serums_tested():
        return mc.business.event_triggers_dict.get("sister_serum_test_count", 0)

    def lily_will_strip():
        return mc.business.event_triggers_dict.get("sister_strip", False)   #Why vren uses mc.business for this?

    def lily_started_insta_story():
        return lily.event_triggers_dict.get("insta_intro_finished", False)

    def lily_mom_insta_started():
        return mom.event_triggers_dict.get("mom_instathot_pic_count", 0) > 0

    def lily_mom_topless_pics_complete():
        return lily.event_triggers_dict.get("sister_instathot_mom_shirtless_covered_count", 0) > 0
