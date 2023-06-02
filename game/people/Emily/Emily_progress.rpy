init 10 python:
    def emily_story_character_description():
        return "A university student that asked you to help her with her studies."

    def emily_story_love_list():
        love_story_list = {}

        if not emily.event_triggers_dict.get("tutor_enabled", False):
            love_story_list[0] = "You haven't offered to tutor her yet."
            return love_story_list

        love_story_list[0] = "You have accepted to tutor [emily.fname]."

        return love_story_list

    def emily_story_lust_list():
        lust_story_list = {}

        if not emily.event_triggers_dict.get("tutor_enabled", False):
            lust_story_list[0] = "You haven't offered to tutor her yet."
            return lust_story_list

        lust_story_list[0] = "You have accepted to tutor [emily.fname]."

        return lust_story_list

    def emily_story_obedience_list():
        obedience_story_list = {}
        obedience_story_list[0] = "This story step has not yet been written."
        return obedience_story_list

    def emily_story_teamup_list():
        teamups = {
            0: [christina, "[emily.fname] and [christina.fname], a mother daughter pair that seems made for fucking."]
        }
        return teamups

    def emily_story_other_list():
        other_story_list = {}
        #emilys other story index:
        # 0 - Her current tutor status
        # 1 - Her current involvement with training of Emily
        # 2 - Her council influence

        if not emily.event_triggers_dict.get("tutor_enabled", False):
            other_story_list[0] = "You haven't offered to tutor her yet."
        else:
            other_story_list[0] = "You are tutoring [emily.fname]."


        return other_story_list
