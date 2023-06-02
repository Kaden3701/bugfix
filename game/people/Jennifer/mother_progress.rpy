init 10 python:
    def jennifer_story_character_description():
        return "[mom.fname] is your mother, and you live together with her and your sister, [lily.fname]. Your father is out of the picture."

    def jennifer_story_love_list():
        love_story_list = {}

        return love_story_list

    def jennifer_story_lust_list():
        lust_story_list = {}
        if mom.is_employee: #First, check and see if we have hired her.
            #If we have hired Jennifer, we drop all the entries for her previous job, and pick up new entries for being MC's employee
            lust_story_list[0] = "[mom.title] works for you now! The next set of events has not yet been written."
            return lust_story_list

        if mom.has_job(unemployed_job):
            lust_story_list[0] = "[mom.title] is currently unemployed. Maybe you could hire her?"
            return lust_story_list


        if mom.progress.lust_step == 0:
            if mom.sluttiness < 20:
                lust_story_list[0] = "Increase [mom.title]'s sluttiness to trigger this event"
            else:
                lust_story_list[0] = "[mom.title] will approach you soon."
        elif mom.progress.lust_step == 1:
            if mom.event_triggers_dict.get("mom_work_promotion_outfit_slutty", False):
                lust_story_list[0] = "[mom.title] is up for a promotion at her job, and you suggested she use her womanly charms to get it."
            else:
                lust_story_list[0] = "[mom.title] is up for a promotion at her job, and you suggested she use her professionalism to get it."
        elif mom.progress.lust_step == 2:
            if mom.event_triggers_dict.get("mom_work_promotion_two_prep_enabled", False):
                lust_story_list[0] = "[mom.title] needs help preparing for a round two interview for her promotion. You should help her prepare for it."
            elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "slutty":
                lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she act slutty."
            elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "friendly":
                lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she be extra friendly."
            elif mom.event_triggers_dict.get("mom_work_promotion_two_tactic", "professional") == "professional":
                lust_story_list[0] = "You helped [mom.title] prepare for her next interview by suggesting she be strictly professional."
        elif mom.progress.lust_step >= 3:
            if mom.has_job(mom_secretary_job):
                lust_story_list[0] = "You helped [mom.title] get promoted to being a personal secretary."
                if mom.sluttiness < 40:
                    lust_story_list[1] = "Increase [mom.title]'s sluttiness to trigger her next event"
                else:
                    lust_story_list[1] = "[mom.title] will approach you soon for her next event."
            else:
                lust_story_list[0] = "Your help wasn't enough, and [mom.title] didn't get a promotion."
                lust_story_list[1] = "To continue this arc, you should convince her to quit and to come work for you."
        if mom.progress.lust_step == 4:
            if mom.event_triggers_dict.get("mom_promotion_boss_phase_one", False):
                lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You should talk to her boss about the situation, then report back to her."
            elif mom.event_triggers_dict.get("mom_replacement_approach", "tits") == "seduce":
                lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You suggested that she perform sexual favors for her boss."
            elif mom.event_triggers_dict.get("mom_replacement_approach", "tits") == "tits":
                lust_story_list[1] = "[mom.fname] is worried about being replaced at her work. You suggested that she get bigger tits."
        elif mom.progress.lust_step >= 5:
            if the_person.event_triggers_dict.get("mom_replacement_approach", "seduce") == "seduce":
                lust_story_list[1] = "[mom.fname] kept her boss from hiring a replacement by performing sexual favors for him."
            else:
                lust_story_list[1] = "[mom.fname] kept her boss from hiring a replacement by getting bigger tits."
            if mom.progress.lust_step == 5:
                lust_story_list[2] = "Give [mom.title] some time to settle in to her new work duties."
        if mom.progress.lust_step == 6:
            lust_story_list[2] = "[mom.fname] is regularly giving her boss sexual favors."
            lust_story_list[3] = "The rest of this story is a work in progress."


        return lust_story_list

    def jennifer_story_obedience_list():
        obedience_story_list = {}


        return obedience_story_list

    def jennifer_story_teamup_list():
        teamups = {
            0: [aunt, "[aunt.fname] and your mom... Two hot milfs, could something like this be possible?"],
            1: [lily, "[mom.fname] and your sister... The ultimate fantasy? There is probably no way this could ever happen."],
            2: [sarah, "Maybe someday you could get [mom.fname] together with [sarah.fname]..."]    #this should have conditions on it
        }
        return teamups

    def jennifer_story_other_list():
        other_story_list = {}
        #Jennifers other story index:
        # 0 - Her current employment status
        # 1 - Her current taboo status
        # 2 - Her current Insta status
        # 3 - Her current girlfriend status
        if mom.has_job(mom_secretary_job):
            other_story_list[0] = "[mom.fname] is a personal assistant at the company she works for."
        elif mom.has_job(mom_associate_job):
            other_story_list[0] = "[mom.fname] is a business associate at the company she works for."
        elif mom.has_job(unemployed_job):
            other_story_list[0] = "[mom.fname] is currently unemployed."
        elif mom.is_employee:
            other_story_list[0] = "[mom.fname] works for you."
        else:
            other_story_list[0] = "[mom.fname] has some other job? Please report this error on Discord."

        if mom.event_triggers_dict.get("vaginal_revisit_complete", False):
            other_story_list[1] = "[mom.possessive_title] is completely open to your sexual requests."
        elif mom.event_triggers_dict.get("anal_revisit_complete", False):
            other_story_list[1] = "[mom.possessive_title] is willing to let you take her anally, but is refusing to go all the way."
        elif mom.event_triggers_dict.get("oral_revisit_complete", False):
            other_story_list[1] = "[mom.possessive_title] is willing to exchange oral favors, but refuses to go any farther."
        elif mom.event_triggers_dict.get("kissing_revisit_complete", False):
            other_story_list[1] = "[mom.possessive_title] is willing to exchange minor sexual favors, but refuses to go any farther."
        else:
            other_story_list[1] = "[mom.possessive_title] is unwilling to let you touch her sexually."

        if mom.has_role(onlyfans_role):
            other_story_list[2] = "[mom.title] has an OnlyFanatics that she regularly posts nudes to."
        elif mom.has_role(instapic_role):
            other_story_list[2] = "[mom.title] has an InstaPic account that she regularly posts pics to."
        else:
            other_story_list[2] = "[mom.title] doesn't post pictures online anywhere that you are aware of."

        other_story_list[3] = "[mom.fname] isn't dating anyone seriously that you know of."

        return other_story_list
