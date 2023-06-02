init 0 python:
    #### UNIFORM POLICY SECTION ####
    uniform_policies_list = []

    def reset_invalid_uniforms(uniform_disobedience_priority): #Called by all uniform policies to clear newly inappropriate planned uniforms.
        slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        for employee in [x for x in mc.business.employee_list if x.planned_uniform and x.planned_uniform.outfit_slut_score > slut_limit and x.planned_uniform.outfit_slut_score > x.effective_sluttiness()]:
            employee.planned_uniform = None
            employee.apply_planned_outfit()
        return

    strict_uniform_policy = Policy(name = "Strict Corporate Uniforms",
        desc = "Requiring certain styles of attire in the business world is nothing new.\nAllows you to designate overwear sets of sluttiness 10 or less as part of your business uniform.",
        cost = 500,
        toggleable = True,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        extra_arguments = {"uniform_disobedience_priority":0}) #Uniform disobedience is only run once, regardless of how many policies are running. The highest priority uniform function is run.
    uniform_policies_list.append(strict_uniform_policy)

    relaxed_uniform_policy = Policy(name = "Relaxed Corporate Uniforms",
        desc = "Corporate dress code is broadened to include more casual apparel.\nYou can designate overwear sets up to sluttiness 20 as part of your business uniform.",
        cost = 1000,
        toggleable = True,
        own_requirement = strict_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = strict_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":1})
    uniform_policies_list.append(relaxed_uniform_policy)

    casual_uniform_policy = Policy(name = "Casual Corporate Uniforms",
        desc = "Corporate dress code is broadened even further.\nOverwear sets up to 30 sluttiness are now valid uniforms.",
        cost = 2000,
        toggleable = True,
        own_requirement = relaxed_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = relaxed_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":2})
    uniform_policies_list.append(casual_uniform_policy)

    reduced_coverage_uniform_policy = Policy(name = "Reduced Coverage Corporate Uniforms",
        desc = "The term \"appropriate coverage\" in the employee manual is redefined and subject to employer approval.\nYou can now use full outfits or underwear sets as part of your corporate uniform.\nUnderwear sets must have a sluttiness score of 15 or less, outfits to 40 or less.",
        cost = 5000,
        toggleable = True,
        own_requirement = casual_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = casual_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":3})
    uniform_policies_list.append(reduced_coverage_uniform_policy)

    minimal_coverage_uniform_policy = Policy(name = "Minimal Coverage Corporate Uniforms",
        desc = "Corporate dress code is broadened further.\nUniforms must now only meet a \"minimum coverage\" requirement, generally nothing more than a set of bra and panties.\nFull uniforms can have a sluttiness score of 60, underwear sets can go up to 30.",
        cost = 10000,
        toggleable = True,
        own_requirement = reduced_coverage_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = reduced_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":4})
    uniform_policies_list.append(minimal_coverage_uniform_policy)

    corporate_enforced_nudity_policy = Policy(name = "Corporate Enforced Nudity",
        desc = "Corporate dress code is removed in favour of a \"need to wear\" system.\nAll clothing items that are deemed non-essential are subject to employer approval.\nConveniently, all clothing is deemed non-essential.\nFull outfit sluttiness is limited to 80 or less, underwear sets have no limit.",
        cost = 25000,
        toggleable = True,
        own_requirement = minimal_coverage_uniform_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = minimal_coverage_uniform_policy,
        extra_arguments = {"uniform_disobedience_priority":5})
    uniform_policies_list.append(corporate_enforced_nudity_policy)

    maximal_arousal_uniform_policy = Policy(name = "Maximal Arousal Uniform Policy",
        desc = "Visually stimulating uniforms are deemed essential to the workplace.\nAny and all clothing items and accessories are allowed, uniform sluttiness is uncapped.",
        cost = 50000,
        toggleable = True,
        own_requirement = corporate_enforced_nudity_policy,
        on_remove_function = reset_invalid_uniforms,
        on_move_function = uniform_disobedience_on_move,
        dependant_policies = corporate_enforced_nudity_policy,
        extra_arguments = {"uniform_disobedience_priority":6})
    uniform_policies_list.append(maximal_arousal_uniform_policy)

    male_focused_marketing_policy = Policy(name = "Male Focused Modeling",
        desc = "The adage \"Sex Sells\" is especially true when selling your serum to men.\nMarket reach is increased by an additional 1% per point of outfit Sluttiness worn by your marketing staff, and several new duties are unlocked for Marketing and Supply staff.",
        cost = 500,
        toggleable = True,
        own_requirement = strict_uniform_policy,
        dependant_policies = strict_uniform_policy)
    uniform_policies_list.append(male_focused_marketing_policy)

    creative_colored_uniform_policy = Policy(
        name = "Relaxed Uniform Color Policy",
        cost = 1000,
        desc = "Employees are given some leeway with the colors of their outfits. While active, employees wear your uniform pieces but can select their own colors.\nReduces happiness penalties for girls who hate work uniforms.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(creative_colored_uniform_policy)

    personal_bottoms_uniform_policy = Policy(
        name = "Relaxed Uniform Bottoms Policy",
        cost = 2000,
        desc = "Employees are given some leeway on uniforms.\nWhile active, employees may choose to swap pants for a skirt and vice versa.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(personal_bottoms_uniform_policy)

    casual_friday_uniform_policy = Policy(
        name = "Casual Friday Uniform Policy",
        cost = 2000,
        desc = "Employees are free to choose their own uniform on Fridays.\nThis adds some variety on Fridays and prevents uniform infractions.",
        toggleable = True,
        own_requirement = casual_uniform_policy,
        dependant_policies = casual_uniform_policy
    )
    uniform_policies_list.append(casual_friday_uniform_policy)

    creative_skimpy_uniform_policy = Policy(
        name = "Uniform Self Expression Policy",
        cost = 10000,
        desc = "Employees are given some leeway on uniforms.\nWhile active, employees may choose not to wear a piece or two of the uniform as a form of self expression.",
        toggleable = True,
        own_requirement = [corporate_enforced_nudity_policy, creative_colored_uniform_policy],
        dependant_policies = [corporate_enforced_nudity_policy, creative_colored_uniform_policy]
    )
    uniform_policies_list.append(creative_skimpy_uniform_policy)

    dress_code_policy = Policy(
        name = "Dress Code",
        cost = 500,
        desc = "Employees are required to abide by a dress code.\nPersonal outfits worn to work may not exceed uniform policy sluttiness limits.",
        toggleable = True,
        own_requirement = casual_uniform_policy
    )
    uniform_policies_list.append(dress_code_policy)

    easier_access_policy = Policy(
        name = "Easier Access Policy",
        cost = 2000,
        desc = "Employees are required to wear skirts while working, unless given a specific uniform or the Relaxed Uniform Bottoms Policy is active.",
        toggleable = True,
        own_requirement = dress_code_policy,
        dependant_policies = dress_code_policy
    )
    uniform_policies_list.append(easier_access_policy)

    commando_uniform_policy = Policy(
        name = "Commando Dress Code Policy",
        cost = 10000,
        desc = "Employees are forbidden from wearing bras or panties as part of their dress code or uniform.",
        toggleable = True,
        own_requirement = [corporate_enforced_nudity_policy, dress_code_policy],
        dependant_policies = dress_code_policy
    )
    uniform_policies_list.append(commando_uniform_policy)

    def mandatory_toys_policy_on_turn():
        if not mc.business.is_open_for_business:
            return

        modifier_percent = 0
        if mandatory_vibe_policy.is_active:
            modifier_percent += 0.15
        if mandatory_bullet_policy.is_active:
            modifier_percent += 0.2
        if mandatory_plug_policy.is_active:
            modifier_percent += 0.25

        for person in [x for x in mc.business.employee_list if x.is_at_work and x.arousal < (x.max_arousal * modifier_percent)]:
            person.arousal = modifier_percent * person.max_arousal
        return

    def mandatory_toys_policy_on_day():
        def change_toy_based_stats(person, happiness, effectiveness):
            #print("Toy change: {} -> {} {}".format(person.name, happiness, effectiveness))
            person.change_happiness(happiness, add_to_log = False)
            mc.business.change_team_effectiveness(effectiveness, instant = True)
            return

        if mc.business.is_weekend:
            return

        for person in [x for x in mc.business.employee_list]:
            if mandatory_plug_policy.is_active and not person.has_anal_fetish:
                if person.sluttiness < 30:
                    change_toy_based_stats(person, -10, -3)
                elif person.sluttiness < 50:
                    change_toy_based_stats(person, -5, -2)
                elif person.sluttiness < 70:
                    change_toy_based_stats(person, -2, -1)
            elif mandatory_bullet_policy.is_active and not person.has_breeding_fetish:
                if person.sluttiness < 30:
                    change_toy_based_stats(person, -5, -2)
                elif person.sluttiness < 50:
                    change_toy_based_stats(person, -2, -1)
            elif mandatory_vibe_policy.is_active and person.sluttiness < 30:
                change_toy_based_stats(person, -2, -1)
        return

    mandatory_vibe_policy = Policy(
        name = "Mandatory Vibrator Policy",
        cost = 30000,
        desc = "All employees are required to wear a butterfly vibrator that stimulates their vaginas during work hours, ensuring they are aroused at work all the time.\nRaises minimum arousal during work hours by 15%.\nAffects person happiness and team efficiency when sluttiness is less than 30.",
        toggleable = True,
        own_requirement = maximal_arousal_uniform_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )
    uniform_policies_list.append(mandatory_vibe_policy)

    mandatory_bullet_policy = Policy(
        name = "Mandatory Bullet Policy",
        cost = 50000,
        desc = "All employees are required to have a bullet vibrator inserted into their vaginas during work hours, ensuring they are aroused at work all the time.\nRaises minimum arousal during work hours by 20%.\nAffects person happiness and team efficiency when sluttiness is less than 50.",
        toggleable = True,
        own_requirement = mandatory_vibe_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )
    uniform_policies_list.append(mandatory_bullet_policy)

    mandatory_plug_policy = Policy(
        name = "Mandatory Plug Policy",
        cost = 100000,
        desc = "All employees are required to have a butt plug inserted during work hours, ensuring they are aroused at work all the time.\nRaises minimum arousal during work hours by 25%.\nAffects person happiness and team efficiency when sluttiness is less than 70.",
        toggleable = True,
        own_requirement = mandatory_bullet_policy,
        on_turn_function = mandatory_toys_policy_on_turn,
        on_day_function = mandatory_toys_policy_on_day
    )
    uniform_policies_list.append(mandatory_plug_policy)
