init 3 python:
    def get_clarity_multiplier():
        multiplier = 1.0
        if "perk_system" in globals() and perk_system is not None:
            if perk_system.has_ability_perk("Intelligent Clarity"):
                multiplier += (mc.int * .05) #5% increase per intelligence point
            if perk_system.has_ability_perk("Charismatic Clarity"):
                multiplier += (mc.charisma * .05) #5% increase per charisma point
            if perk_system.has_ability_perk("Focused Clarity"):
                multiplier += (mc.focus * .05) #5% increase per charisma point
        return multiplier

    def lust_drip_perk_update_func():
        change_amount = __builtin__.int(max(5, (min(20, mc.free_clarity * .001))))
        mc.locked_clarity += change_amount
        mc.free_clarity -=  change_amount
        return

    def add_lust_drip_perk():
        if perk_system.has_ability_perk("Lust Drip"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Clarity slowly converts into lust.", active = True, togglable = True, usable = False, update_func = lust_drip_perk_update_func), "Lust Drip")
        return

    def add_intelligence_clarity_perk():
        if perk_system.has_ability_perk("Intelligent Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your intelligence.", active = False, usable = False), "Intelligent Clarity")
        return

    def add_charismatic_clarity_perk():
        if perk_system.has_ability_perk("Charismatic Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your charisma.", active = False, usable = False), "Charismatic Clarity")
        return

    def add_focus_clarity_perk():
        if perk_system.has_ability_perk("Focused Clarity"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "You gain increase clarity based on your focus.", active  = False, usable = False), "Focused Clarity")
        return

    def add_lust_gain_perk():
        if perk_system.has_ability_perk("Lustful Priorities"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Every time you normally gain lust, you gain 5 extra.", active = True, togglable = True, usable = False), "Lustful Priorities")
        return

    persuade_action = ActionMod("Use Persuasion", requirement = persuade_person_requirement, effect = "persuade_person",
        menu_tooltip = "Leverage your clarity to persuade her to do something.", category = "Generic People Actions")

    def build_specific_action_list_extended(org_func):
        def build_specific_action_list_wrapper(person, keep_talking = True):
            # run original function
            result = org_func(person, keep_talking)
            # run extension code (append new action to base game menu)
            if persuade_action.enabled:
                result.append([persuade_action, person])
            return result

        return build_specific_action_list_wrapper

    # wrap up the build_specific_action_list function
    if "build_specific_action_list" in globals():
        build_specific_action_list = build_specific_action_list_extended(build_specific_action_list)
