init 10 python:
    def alexia_story_character_description():
        return "After no contact for over a year, you have a chance encounter with [alexia.fname], a former schoolmate from your time at the university."

    def alexia_story_love_list():
        love_story_list = {}

        if alexia.progress.love_step == 0:
            love_story_list[0] = "Increase [alexia.fname]'s love to 10, then hire her to your marketing department."
        elif alexia.progress.love_step == 1:
            love_story_list[0] = "[alexia.fname] seems interested in gaming. Wait for the gaming cafe to open up at the mall."
        else:
            love_story_list[0] = "You've hired [alexia.fname] to be in your marketing department."
            love_story_list[1] = "This story step has not yet been written."

        return love_story_list

    def alexia_story_lust_list():
        lust_story_list = {}
        if alexia.progress.love_step == 0:
            lust_story_list[0] = "Hire [alexia.fname] to start this story."
            return lust_story_list
        if alexia.progress.lust_step == 0:
            if alexia.event_triggers_dict.get("camera_reintro_enabled", False):
                lust_story_list[0] = "Talk to [alexia.fname] to purchase the camera equipment."
            else:
                lust_story_list[0] = "Wait for [alexia.fname] to talk to you about camera equipment, then purchase it."
        else:
            lust_story_list[0] = "You can talk to [alexia.fname] to do a photoshoot for company advertising."
            lust_story_list[1] = "This story step has not yet been written."


        return lust_story_list

    def alexia_story_obedience_list():
        obedience_story_list = {}
        obedience_story_list[0] = "This story step has not yet been written."
        return obedience_story_list

    def alexia_story_teamup_list():
        teamups = {
            0: [myra, "[myra.fname] and [alexia.fname], a match made in gamer heaven?"],
            1: [camilla, "[camilla.fname] also has a significant other, maybe you could get them together?"],
            2: [kaya, "You wonder if [alexia.fname] and [kaya.fname] would be up for grabbing coffee together sometime."]    #this should have conditions on it
        }
        return teamups

    def alexia_story_other_list():
        other_story_list = {}
        #alexias other story index:
        # 0 - Her current employment status
        # 1 - Her current girlfriend status
        # 2 - Is she the company model, if so, how far have photo shoots gone?
        if alexia.is_employee:
            other_story_list[0] = "You have hired [alexia.fname] to work for you."
        else:
            other_story_list[0] = "[alexia.fname] does not work for you."
        if alexia.relationship != "Single":
            if alexia.is_affair:
                other_story_list[1] = "She is currently dating someone else, but having an affair with you!"
            else:
                other_story_list[1] = "She is currently dating someone else."
        elif alexia.is_girlfriend:
            other_story_list[1] = "She is your girlfriend."
        elif alexia.is_single:
            other_story_list[1] = "She is currently single."
        if alexia == mc.business.company_model:
            if alexia.event_triggers_dict.get("camera_fuck", False):
                other_story_list[2] = "[alexia.fname] is your company model, and even lets you fuck her for ad campaigns!"
            elif alexia.event_triggers_dict.get("camera_suck", False):
                other_story_list[2] = "[alexia.fname] is your company model, and even sucks your cock for ad campaigns."
            elif alexia.event_triggers_dict.get("camera_touch", False):
                other_story_list[2] = "[alexia.fname] is your company model and lets you touch her for ad campaigns."
            elif alexia.event_triggers_dict.get("camera_naked", False):
                other_story_list[2] = "[alexia.fname] is your company model and is willing to get naked for photo shoots."
            elif alexia.event_triggers_dict.get("camera_flash", False):
                other_story_list[2] = "[alexia.fname] is your company model and is willing to flash to camera for photo shoots."
            elif alexia.event_triggers_dict.get("camera_flirt", False):
                other_story_list[2] = "[alexia.fname] is your company model and flirts like a pro for photo shoots."
            else:
                other_story_list[2] = "[alexia.fname] is your company model, but the photo shoots are a bit boring."

        return other_story_list
