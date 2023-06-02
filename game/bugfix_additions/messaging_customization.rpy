####################################################
# Allows for suppressing of log message categories #
####################################################

init -2:
    # categories
    default persistent.serum_messages = True
    default persistent.stat_change_messages = True
    default persistent.skill_change_messages = True
    default persistent.clarity_messages = True
    default persistent.energy_messages = True

init 2 python:
    import inspect

    # generic extension function for suppressing messages
    def generic_messages_extended(org_func, message_flag, default_value):
        func_args = inspect.getargspec(org_func)
        if not "add_to_log" in func_args[0]:    # fix when argument not found
            write_log("Unable to wrap: {}".format(org_func.__name__))
            return org_func
        idx = func_args[0].index("add_to_log")

        def generic_messages_wrapper(*args, **kwargs):
            if len(args) > idx:  # replace add_to_log argument if passed
                list_args = list(args)
                list_args[idx] = getattr(persistent, message_flag)
                args = tuple(list_args)
            elif kwargs.get("add_to_log", default_value): # append or replace the keyword argument for suppressing the message
                kwargs["add_to_log"] = getattr(persistent, message_flag)

            # run original function
            return org_func(*args, **kwargs)

        return generic_messages_wrapper

    # serum messages
    Person.apply_serum_study = generic_messages_extended(Person.apply_serum_study, "serum_messages", True)
    Person.add_suggest_effect = generic_messages_extended(Person.add_suggest_effect, "serum_messages", True)
    Person.change_suggest = generic_messages_extended(Person.change_suggest, "serum_messages", True)

    SerumDesign.run_on_turn = generic_messages_extended(SerumDesign.run_on_turn, "serum_messages", False)
    SerumDesign.run_on_apply = generic_messages_extended(SerumDesign.run_on_apply, "serum_messages", True)
    SerumDesign.run_on_remove = generic_messages_extended(SerumDesign.run_on_remove, "serum_messages", False)
    SerumDesign.run_on_day = generic_messages_extended(SerumDesign.run_on_day, "serum_messages", False)

    SerumTrait.run_on_turn = generic_messages_extended(SerumTrait.run_on_turn, "serum_messages", False)
    SerumTrait.run_on_apply = generic_messages_extended(SerumTrait.run_on_apply, "serum_messages", True)
    SerumTrait.run_on_remove = generic_messages_extended(SerumTrait.run_on_remove, "serum_messages", False)
    SerumTrait.run_on_day = generic_messages_extended(SerumTrait.run_on_day, "serum_messages", True)

    #SerumTraitMod.run_on_turn = generic_messages_extended(SerumTraitMod.run_on_turn, persistent.serum_messages, False)
    #SerumTraitMod.run_on_apply = generic_messages_extended(SerumTraitMod.run_on_apply, persistent.serum_messages, True)
    #SerumTraitMod.run_on_remove = generic_messages_extended(SerumTraitMod.run_on_remove, persistent.serum_messages, False)
    #SerumTraitMod.run_on_day = generic_messages_extended(SerumTraitMod.run_on_day, persistent.serum_messages, True)

    # clarity messages
    MainCharacter.change_masturbation_novelty = generic_messages_extended(MainCharacter.change_masturbation_novelty, "clarity_messages", True)
    MainCharacter.change_locked_clarity = generic_messages_extended(MainCharacter.change_locked_clarity, "clarity_messages", True)
    MainCharacter.convert_locked_clarity = generic_messages_extended(MainCharacter.convert_locked_clarity, "clarity_messages", True)
    MainCharacter.spend_clarity = generic_messages_extended(MainCharacter.spend_clarity, "clarity_messages", False)
    MainCharacter.add_clarity = generic_messages_extended(MainCharacter.add_clarity, "clarity_messages", True)

    # stat changes
    Person.change_happiness = generic_messages_extended(Person.change_happiness, "stat_change_messages", True)
    Person.change_love = generic_messages_extended(Person.change_love, "stat_change_messages", True)
    Person.change_slut = generic_messages_extended(Person.change_slut, "stat_change_messages", True)
    Person.change_obedience = generic_messages_extended(Person.change_obedience, "stat_change_messages", True)
    Person.change_arousal = generic_messages_extended(Person.change_arousal, "stat_change_messages", True)
    Person.change_max_arousal = generic_messages_extended(Person.change_max_arousal, "stat_change_messages", True)
    Person.change_novelty = generic_messages_extended(Person.change_novelty, "stat_change_messages", True)
    Person.change_stats = generic_messages_extended(Person.change_stats, "stat_change_messages", True)

    # energy changes
    Person.change_energy = generic_messages_extended(Person.change_energy, "energy_messages", True)
    Person.change_max_energy = generic_messages_extended(Person.change_max_energy, "energy_messages", True)
    MainCharacter.change_energy = generic_messages_extended(MainCharacter.change_energy, "energy_messages", True)
    MainCharacter.change_max_energy = generic_messages_extended(MainCharacter.change_max_energy, "energy_messages", True)

    # skill changes
    Person.change_hr_skill = generic_messages_extended(Person.change_hr_skill, "skill_change_messages", True)
    Person.change_market_skill = generic_messages_extended(Person.change_market_skill, "skill_change_messages", True)
    Person.change_research_skill = generic_messages_extended(Person.change_research_skill, "skill_change_messages", True)
    Person.change_production_skill = generic_messages_extended(Person.change_production_skill, "skill_change_messages", True)
    Person.change_supply_skill = generic_messages_extended(Person.change_supply_skill, "skill_change_messages", True)
    Person.change_cha = generic_messages_extended(Person.change_cha, "skill_change_messages", True)
    Person.change_int = generic_messages_extended(Person.change_int, "skill_change_messages", True)
    Person.change_focus = generic_messages_extended(Person.change_focus, "skill_change_messages", True)
    Person.change_sex_skill = generic_messages_extended(Person.change_sex_skill, "skill_change_messages", True)
    Person.update_work_skill = generic_messages_extended(Person.update_work_skill, "skill_change_messages", True)
