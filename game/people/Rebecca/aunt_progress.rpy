init 10 python:
    def rebecca_story_character_description():
        return "Your aunt on your mom's side. She is recently divorced, and has a daughter, your cousin [cousin.fname]."

    def rebecca_story_love_list():
        love_story_list = {}
        love_story_list[0] = "The next step in this story has not yet been written."

        return love_story_list

    def rebecca_story_lust_list():
        lust_story_list = {}
        if aunt.progress.lust_step == 0:
            if aunt.sluttiness < 20:
                lust_story_list[0] = "Increase [aunt.fname]'s sluttiness to progress this story."
            else:
                lust_story_list[0] = "[aunt.fname] like to drink with your mother once in a while. Wait until next time this happens."
        else:
            lust_story_list[0] = "[aunt.fname] let you dry hump her ass after getting drunk one evening."
        if aunt.progress.lust_step == 1:
            if aunt.sluttiness < 40:
                lust_story_list[1] = "Increase [aunt.fname]'s sluttiness to progress this story."
            elif not aunt.event_triggers_dict.get("moved_out", False):
                lust_story_list[1] = "Wait for [aunt.fname] to move into her own apartment."
            else:
                lust_story_list[1] = "Visit [aunt.fname] at her apartment sometime."
        if aunt.progress.lust_step > 1:
            lust_story_list[1] = "[aunt.fname] gave you a blowjob after you accidentally walked in on her in her underwear."
            lust_story_list[2] = "The next step in this story has not yet been written."


        return lust_story_list

    def rebecca_story_obedience_list():
        obedience_story_list = {}

        obedience_story_list[0] = "The next step in this story has not yet been written."

        return obedience_story_list

    def rebecca_story_teamup_list():
        teamup_story_list = {
            0: [mom, "[aunt.fname] and your mom... Two hot milfs, could something like this be possible?"]
        }

        if sakari.has_story:
            teamup_story_list[1] = [sakari, "[sakari.fname] and seemed to take a liking to your aunt when you took her shopping."]

        if cousin.has_story:
            teamup_story_list[2] = [cousin, "Maybe someday you could get [aunt.fname] together with [cousin.fname], but right now that seems impossible."]

        return teamup_story_list

    def rebecca_story_other_list():
        story_other_list = {}

        # Rebecca's other stories
        # 0 - How far she takes wine night with MC
        # 1 - How far she goes with family card night
        # 2 - Her status with her Ex

        if not aunt.event_triggers_dict.get("moved_out", False):
            story_other_list[0] = "[aunt.fname] is still living with your family."
        elif not aunt.event_triggers_dict.get("invited_for_drinks", False):
            story_other_list[0] = "Visit [aunt.fname] in her new apartment."
        else:
            story_other_list[0] = "Have some drinks with [aunt.fname] in the evenings at her apartment."

        if mc.business.event_triggers_dict.get("family_games_strip", 0) > 0:
            story_other_list[1] = "[aunt.fname] and the rest of your family are willing to play strip euchre on Wednesday nights."
        elif mc.business.event_triggers_dict.get("family_games_cards",0) > 0:
            story_other_list[1] = "You have a family game night on Wednesday nights."
        else:
            story_other_list[1] = "Progress things with [aunt.fname] to begin having family game nights."

        story_other_list[2] = "[aunt.fname] went through a messy divorce after discovering her ex husband was cheating on her."

        return story_other_list
