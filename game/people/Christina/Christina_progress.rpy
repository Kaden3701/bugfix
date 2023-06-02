init 10 python:
    def christina_story_character_description():
        return "Neglected wife and mother of [emily.fname], a student who you are helping with her lessons."

    def christina_story_love_list():
        love_story_list = {}

        love_story_list[0] = "This story step has not yet been written."

        return love_story_list

    def christina_story_lust_list():
        lust_story_list = {}

        lust_story_list[0] = "This story step has not yet been written."

        return lust_story_list

    def christina_story_obedience_list():
        obedience_story_list = {}
        obedience_story_list[0] = "This story step has not yet been written."
        return obedience_story_list

    def christina_story_teamup_list():
        teamups = {
            0: [emily, "[emily.fname] and [christina.fname], a mother daughter pair that seems made for fucking."],
            1: [city_rep, "You wonder if she runs in the same social circles as [city_rep.fname]..."],
        }
        return teamups

    def christina_story_other_list():
        other_story_list = {}
        #christinas other story index:
        # 0 - Her current affair status
        # 1 - Her current involvement with training of Emily
        # 2 - Her council influence

        if christina.is_affair:
            other_story_list[0] = "You are currently in an affair with [christina.title]."
        elif christina.is_girlfriend:
            other_story_list[0] = "You broke up her marriage and are now dating [christina.fname]."
        elif christina.is_single:
            other_story_list[0] = "You broke up her marriage and [christina.fname] is now single."
        else:
            other_story_list[0] = "[christina.fname] is married to a city council member."

        other_story_list[1] = "[christina.fname] is paying the bills for you to tutor her daughter."

        other_story_list[2] = "[christina.fname] has no influence over her husband and his job at the city council."

        return other_story_list
