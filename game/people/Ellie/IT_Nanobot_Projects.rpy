init -10 python:
    ## Nano IT Projects

    nanobot_IT_project_list = []

    ### Project related functions ###

    def basic_clarity_reduction_on_apply():
        get_fetish_basic_serum().research_added = 100
        return

    def basic_clarity_reduction_on_remove():
        get_fetish_basic_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def basic_attention_reduction_on_apply():
        get_fetish_basic_serum().attention = 0
        return

    def basic_attention_reduction_on_remove():
        get_fetish_basic_serum().attention = FETISH_SERUM_ATTENTION
        return

    def anal_clarity_reduction_on_apply():
        get_fetish_anal_serum().research_added = 100
        return

    def anal_clarity_reduction_on_remove():
        get_fetish_anal_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def anal_attention_reduction_on_apply():
        get_fetish_anal_serum().attention = 0
        return

    def anal_attention_reduction_on_remove():
        get_fetish_anal_serum().attention = FETISH_SERUM_ATTENTION
        return

    def breeder_clarity_reduction_on_apply():
        get_fetish_breeding_serum().research_added = 100
        return

    def breeder_clarity_reduction_on_remove():
        get_fetish_breeding_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def breeder_attention_reduction_on_apply():
        get_fetish_breeding_serum().attention = 0
        return

    def breeder_attention_reduction_on_remove():
        get_fetish_breeding_serum().attention = FETISH_SERUM_ATTENTION
        return

    def cum_clarity_reduction_on_apply():
        get_fetish_cum_serum().research_added = 100
        return

    def cum_clarity_reduction_on_remove():
        get_fetish_cum_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def cum_attention_reduction_on_apply():
        get_fetish_cum_serum().attention = 0
        return

    def cum_attention_reduction_on_remove():
        get_fetish_cum_serum().attention = FETISH_SERUM_ATTENTION
        return

    def exhibition_clarity_reduction_on_apply():
        get_fetish_exhibition_serum().research_added = 100
        return

    def exhibition_clarity_reduction_on_remove():
        get_fetish_exhibition_serum().research_added = FETISH_RESEARCH_ADDED
        return

    def exhibition_attention_reduction_on_apply():
        get_fetish_exhibition_serum().attention = 0
        return

    def exhibition_attention_reduction_on_remove():
        get_fetish_exhibition_serum().attention = FETISH_SERUM_ATTENTION
        return

    def anal_incest_project_on_apply():
        if "incest" not in FETISH_ANAL_OPINION_LIST:
            FETISH_ANAL_OPINION_LIST.append("incest")
        return

    def anal_incest_project_on_remove():
        if "incest" in FETISH_ANAL_OPINION_LIST:
            FETISH_ANAL_OPINION_LIST.remove("incest")
        return

    def breeder_submission_project_on_apply():
        if "being submissive" not in FETISH_BREEDING_OPINION_LIST:
            FETISH_BREEDING_OPINION_LIST.append("being submissive")
        return

    def breeder_submission_project_on_remove():
        if "being submissive" in FETISH_BREEDING_OPINION_LIST:
            FETISH_BREEDING_OPINION_LIST.remove("being submissive")
        return

    def cum_thirst_project_on_apply():
        if "taking control" not in FETISH_CUM_OPINION_LIST:
            FETISH_CUM_OPINION_LIST.append("taking control")
        return

    def cum_thirst_project_on_remove():
        if "taking control" in FETISH_CUM_OPINION_LIST:
            FETISH_CUM_OPINION_LIST.remove("taking control")
        return

    def exhibition_cheating_project_on_apply():
        if "cheating on men" not in FETISH_EXHIBITION_OPINION_LIST:
            FETISH_EXHIBITION_OPINION_LIST.append("cheating on men")
        return

    def exhibition_cheating_project_on_remove():
        if "cheating on men" in FETISH_EXHIBITION_OPINION_LIST:
            FETISH_EXHIBITION_OPINION_LIST.remove("cheating on men")
        return

    def anal_program_unlock_project_on_apply():
        fetish_unlock_anal_serum()
        return

    def breeder_program_unlock_project_on_apply():
        fetish_unlock_breeding_serum()
        return

    def cum_program_unlock_project_on_apply():
        fetish_unlock_cum_serum()
        return

    def exhibition_program_unlock_project_on_apply():
        fetish_unlock_exhibition_serum()
        return


    def basic_attention_reduction_project_requirement():
        if get_fetish_basic_serum().mastery_level >= 5.0:
            return True
        return "Low Trait Mastery (> 5)"

    def anal_incest_project_requirement():
        if get_fetish_anal_serum().mastery_level >= 3.0:
            return True
        return "Low Trait Mastery (> 3)"

    def anal_attention_reduction_project_requirment():
        if get_fetish_anal_serum().mastery_level >= 5.0:
            return True
        return "Low Trait Mastery (> 5)"

    def anal_fetish_increase_project_requirment():
        if ellie_has_anal_fetish():
            return True
        return "IT Girl Anal Fetish"

    def breeder_submission_project_requirement():
        if get_fetish_breeding_serum().mastery_level >= 3.0:
            return True
        return "Low Trait Mastery (> 3)"

    def breeder_attention_reduction_project_requirement():
        if get_fetish_breeding_serum().mastery_level >= 5.0:
            return True
        return "Low Trait Mastery (> 5)"

    def breeder_fetish_increase_project_requirment():
        if ellie_has_breeding_fetish():
            return True
        return "IT Girl Breeding Fetish"

    def cum_thirst_project_requirement():
        if get_fetish_cum_serum().mastery_level >= 3.0:
            return True
        return "Low Trait Mastery (> 3)"

    def cum_attention_reduction_project_requirement():
        if get_fetish_cum_serum().mastery_level >= 5.0:
            return True
        return "Low Trait Master (> 5)"

    def cum_fetish_increase_project_requirment():
        if ellie_has_cum_fetish():
            return True
        return "IT Girl Cum Fetish"

    def exhibition_cheating_project_requirement():
        if get_fetish_exhibition_serum().mastery_level >= 3.0:
            return True
        return "Low Trait Mastery (> 3)"

    def exhibition_attention_reduction_project_requirement():
        if get_fetish_exhibition_serum().mastery_level >= 5.0:
            return True
        return "Low Trait Mastery (> 5)"

    def exhibition_fetish_increase_project_requirment():
        if ellie_has_exhibition_fetish():
            return True
        return "IT Girl Exhibition Fetish"

init -5 python:
    basic_clarity_reduction_project = IT_Project(name = "Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = basic_clarity_reduction_on_apply,   #Heckin typos. too lazy to fix, this is research_added, not clarity
        on_remove_function = basic_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "basic",
        tier = 10)

    basic_attention_reduction_project = IT_Project(name = "Deceptive Programming",
        desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
        cost = 0,
        requirement = basic_attention_reduction_project_requirement,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = basic_attention_reduction_on_apply,
        on_remove_function = basic_attention_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 200,
        category = "basic",
        tier = 30)

    anal_clarity_reduction_project = IT_Project(name = "Anal Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_clarity_reduction_on_apply,
        on_remove_function = anal_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "anal",
        tier = 10)

    anal_incest_project = IT_Project(name = "Familial Anal Adaptation",
        desc = "Members of family may be more willing to accept acts of anal sex. Adds Incest to opinions increased by the Anal Proclivity Nanobots.",
        cost = 0,
        requirement = anal_incest_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_incest_project_on_apply,
        on_remove_function = anal_incest_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "anal",
        tier = 20)

    anal_attention_reduction_project = IT_Project(name = "Evasive Programming",
        desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
        cost = 0,
        requirement = anal_attention_reduction_project_requirment,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_attention_reduction_on_apply,
        on_remove_function = anal_attention_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 200,
        category = "anal",
        tier = 30)

    anal_fetish_increase_project = IT_Project(name = "Anal Fetish Prioritization",
        desc = "Greatly increases the chances of causing an anal fetish after exposure.",
        cost = 0,
        requirement = anal_fetish_increase_project_requirment,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 250,
        category = "anal",
        tier = 40)

    breeder_clarity_reduction_project = IT_Project(name = "Breeding Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_clarity_reduction_on_apply,
        on_remove_function = breeder_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "breeder",
        tier = 10)

    breeder_submission_project = IT_Project(name = "Submissive Breeder Adaptation",
        desc = "Encourages breeding as an active form of submission. Adds being submissive to the list of opinions increased by Reproduction Proclivity Nanobots.",
        cost = 0,
        requirement = breeder_submission_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_submission_project_on_apply,
        on_remove_function = breeder_submission_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "breeder",
        tier = 20)

    breeder_attention_reduction_project = IT_Project(name = "Evasive Programming",
        desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
        cost = 0,
        requirement = breeder_attention_reduction_project_requirement,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_attention_reduction_on_apply,
        on_remove_function = breeder_attention_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 200,
        category = "breeder",
        tier = 30)


    breeder_fetish_increase_project = IT_Project(name = "Breeding Fetish Prioritization",
        desc = "Greatly increases the chances of causing a breeding fetish after exposure.",
        cost = 0,
        requirement = breeder_fetish_increase_project_requirment,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 250,
        category = "breeder",
        tier = 40)

    cum_clarity_reduction_project = IT_Project(name = "Cum Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_clarity_reduction_on_apply,
        on_remove_function = cum_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "cum",
        tier = 10)

    cum_thirst_project = IT_Project(name = "Cum Thirst Adaptation",
        desc = "Sexual fixation on cum can inspire a powerful thirst, motivating girls to take a more active role in getting their fix. Adds taking control to the list of opinions increased by Semen Proclivity Nanobots.",
        cost = 0,
        requirement = cum_thirst_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_thirst_project_on_apply,
        on_remove_function = cum_thirst_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "cum",
        tier = 20)

    cum_attention_reduction_project = IT_Project(name = "Evasive Programming",
        desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
        cost = 0,
        requirement = cum_attention_reduction_project_requirement,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_attention_reduction_on_apply,
        on_remove_function = cum_attention_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 200,
        category = "cum",
        tier = 30)

    cum_fetish_increase_project = IT_Project(name = "Cum Fetish Prioritization",
        desc = "Greatly increases the chances of causing a cum fetish after exposure.",
        cost = 0,
        requirement = cum_fetish_increase_project_requirment,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 250,
        category = "cum",
        tier = 40)

    exhibition_clarity_reduction_project = IT_Project(name = "Exhibition Chemical Adaptation",
        desc = "Changes nanobot adjustment strategy. Instead of adjusting serum composition for nanobots, adjust nanobot programming to handle different chemicals. Reduces research requirement.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_clarity_reduction_on_apply,
        on_remove_function = exhibition_clarity_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "exhibition",
        tier = 10)

    exhibition_cheating_project = IT_Project(name = "Risky Behavior Adaptation",
        desc = "Exhibitionism often encourages risky behavior. Adds cheating on men to the list of opinions increased by Social Sexual Proclivity Nanobots.",
        cost = 0,
        requirement = exhibition_cheating_project_requirement,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_cheating_project_on_apply,
        on_remove_function = exhibition_cheating_project_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 150,
        category = "exhibition",
        tier = 20)

    exhibition_attention_reduction_project = IT_Project(name = "Evasive Programming",
        desc = "Updates nanobot programming to automatically hide themselves from all known interception and detection strategies. Reduces attention.",
        cost = 0,
        requirement = exhibition_attention_reduction_project_requirement,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_attention_reduction_on_apply,
        on_remove_function = exhibition_attention_reduction_on_remove,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 200,
        category = "exhibition",
        tier = 30)

    exhibition_fetish_increase_project = IT_Project(name = "Exhibitionism Fetish Prioritization",
        desc = "Greatly increases the chances of causing an exhibitionist fetish after exposure.",
        cost = 0,
        requirement = exhibition_fetish_increase_project_requirment,
        toggleable = True,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = None,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 250,
        category = "exhibition",
        tier = 40)


    nanobot_IT_project_list.append(basic_clarity_reduction_project)
    nanobot_IT_project_list.append(basic_attention_reduction_project)
    nanobot_IT_project_list.append(anal_clarity_reduction_project)
    nanobot_IT_project_list.append(anal_incest_project)
    nanobot_IT_project_list.append(anal_attention_reduction_project)
    nanobot_IT_project_list.append(anal_fetish_increase_project)
    nanobot_IT_project_list.append(breeder_clarity_reduction_project)
    nanobot_IT_project_list.append(breeder_submission_project)
    nanobot_IT_project_list.append(breeder_attention_reduction_project)
    nanobot_IT_project_list.append(breeder_fetish_increase_project)
    nanobot_IT_project_list.append(cum_clarity_reduction_project)
    nanobot_IT_project_list.append(cum_thirst_project)
    nanobot_IT_project_list.append(cum_attention_reduction_project)
    nanobot_IT_project_list.append(cum_fetish_increase_project)
    nanobot_IT_project_list.append(exhibition_clarity_reduction_project)
    nanobot_IT_project_list.append(exhibition_cheating_project)
    nanobot_IT_project_list.append(exhibition_attention_reduction_project)
    nanobot_IT_project_list.append(exhibition_fetish_increase_project)

    anal_unlock_project = IT_Project(name = "Anal Program",
        desc = "A new nanobot program that encourages anal stimulation.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = anal_program_unlock_project_on_apply,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "anal",
        tier = 0)

    breeder_unlock_project = IT_Project(name = "Breeding Program",
        desc = "A new nanobot program that encourages breeding behaviors.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = breeder_program_unlock_project_on_apply,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "breeder",
        tier = 0)

    cum_unlock_project = IT_Project(name = "Cum Program",
        desc = "A new nanobot program that encourages cum exposure.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = cum_program_unlock_project_on_apply,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "cum",
        tier = 0)

    exhibition_unlock_project = IT_Project(name = "Exhibitionism Program",
        desc = "A new nanobot program that encourages exhibitionism.",
        cost = 0,
        requirement = None,
        toggleable = False,
        on_buy_function = None,
        extra_arguments = None,
        on_apply_function = exhibition_program_unlock_project_on_apply,
        on_remove_function = None,
        on_turn_function = None,
        on_move_function = None,
        on_day_function = None,
        dependant_policies = None,
        project_progress = 0,
        project_cost = 100,
        category = "exhibition",
        tier = 0)

    def IT_get_basic_bot_projects():
        return sorted(list(filter(lambda x: x.category == "basic", nanobot_IT_project_list)), key = lambda x: (x.tier, x.name))

    def IT_get_breeder_bot_projects():
        return sorted(list(filter(lambda x: x.category == "breeder", nanobot_IT_project_list)), key = lambda x: (x.tier, x.name))

    def IT_get_anal_bot_projects():
        return sorted(list(filter(lambda x: x.category == "anal", nanobot_IT_project_list)), key = lambda x: (x.tier, x.name))

    def IT_get_cum_bot_projects():
        return sorted(list(filter(lambda x: x.category == "cum", nanobot_IT_project_list)), key = lambda x: (x.tier, x.name))

    def IT_get_exhibition_bot_projects():
        return sorted(list(filter(lambda x: x.category == "exhibition", nanobot_IT_project_list)), key = lambda x: (x.tier, x.name))
