init 10 python:
    def stephanie_story_character_description():
        return "After starting your new pharmaceutical company, you hired your friend [stephanie.fname], to run the research and development division."

    def stephanie_story_love_list():
        love_story_list = {}

        if stephanie.progress.love_step == 0:
            if stephanie.love < 20:
                love_story_list[0] = "Increase [stephanie.fname]'s love to 20."
            else:
                love_story_list[0] = "Get to work early on Saturday, and you might catch [stephanie.fname] as she comes and goes."
        elif stephanie.progress.love_step >= 1:
            love_story_list[0] = "[stephanie.fname] spends Saturday mornings playing tennis.."
            love_story_list[1] = "This story step has not yet been written."

        return love_story_list

    def stephanie_story_lust_list():
        lust_story_list = {}
        lust_story_list[0] = "This story step has not yet been written."
        return lust_story_list

    def stephanie_story_obedience_list():
        obedience_story_list = {}
        if stephanie != mc.business.head_researcher:
            obedience_story_list[0] = "[stephanie.fname] is no longer your head researcher. You cannot progress this story arc any more."
            return obedience_story_list
        if stephanie.progress.obedience_step == 0:
            obedience_story_list[0] = "Advance your business serum trait R&D to tier 1, then [stephanie.fname] will approach you about serum testing."
        elif stephanie.progress.obedience_step == 1:
            obedience_story_list[0] = "[stephanie.fname] has asked you to create a special testing room for serum traits."
        else:
            obedience_story_list[0] = "You have created a room for special serum testing. Talk to [stephanie.fname] to run a test."
        if stephanie.progress.obedience_step == 2:
            if stephanie.obedience < 140:
                obedience_story_list[1] = "Increase her obedience to atleast 140 to continue this story."
            else:
                obedience_story_list[1] = "Work in R&D with [stephanie.fname] to continue this story."
        elif stephanie.progress.obedience_step > 2:
            obedience_story_list[1] = "You ordered [stephanie.fname] to give you a special show. You can now command any employee with atleast 140 obedience for a lap dance."
            obedience_story_list[2] = "The next story step is not yet written"
        return obedience_story_list

    def stephanie_story_teamup_list():
        teamups = {
            0: [nora, "[nora.fname] and [stephanie.fname]. Could you get your old lab mates together again?"],
            1: [ashley, "Her sister, [ashley.fname], would be awfully fun to get together with, but right now that seems impossible."],
            2: [ellie, "You wonder how [stephanie.fname] and [ellie.fname] enjoy working together."]    #this should have conditions on it
        }
        return teamups

    def stephanie_story_other_list():
        other_story_list = {}
        #stephanies other story index:
        # 0 - Her current head researcher status
        # 1 - Her tennis status
        # 2 - Sister storyline status
        if stephanie == mc.business.head_researcher:
            other_story_list[0] = "[stephanie.fname] is your head researcher. Talk to her to advance your business research capabilities."
        else:
            other_story_list[0] = "[stephanie.fname] is no longer your head researcher."
        if stephanie.progress.love_step >= 1:
            other_story_list[1] = "She plays tennis at the gym on Saturday mornings."
        if ashley.is_employee:
            other_story_list[2] = "You hired her sister, [ashley.fname], as a favor to her."

        return other_story_list
