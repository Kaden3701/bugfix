init -1 python:
    def tits_man_perk_unlock():
        if perk_system.has_ability_perk("Tits Man"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Gain increased clarity when cumming on tits.", active = True, usable = False), "Tits Man")
        if ClimaxController.climax_type_dict["tits"] < 2.0:
            ClimaxController.climax_type_dict["tits"] = 2.0
        return

    def tits_man_perk_save_loat():
        if ClimaxController.climax_type_dict["tits"] < 2.0:
            ClimaxController.climax_type_dict["tits"] = 2.0

    def ass_man_perk_unlock():
        if perk_system.has_ability_perk("Ass Man"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Gain increased clarity when cumming on ass.", active = True, usable = False), "Ass Man")
        if ClimaxController.climax_type_dict["body"] < 2.0:  #Apparently ass is not a separate area to the climax controller
            ClimaxController.climax_type_dict["body"] = 2.0
        return

    def ass_man_perk_save_loat():
        if ClimaxController.climax_type_dict["body"] < 2.0:
            ClimaxController.climax_type_dict["body"] = 2.0

    def lustful_vigor_perk_update_func():
        lust_factor = __builtin__.abs(mc.lust_tier - 4)
        mc.change_locked_clarity(lust_factor * 20, add_to_log = False)
        return

    def lustful_vigor_perk_unlock():
        if perk_system.has_ability_perk("Lustful Vigor"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Gain lust quickly when it is low.", active = True, togglable = True, usable = False, update_func = lustful_vigor_perk_update_func), "Lustful Vigor")
        return

    def lustful_youth_perk_update_func():
        if mc.energy < mc.max_energy:
            mc.change_energy((mc.lust_tier * 20), add_to_log = False)
        return True

    def lustful_youth_perk_unlock():
        if perk_system.has_ability_perk("Lustful Youth"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Gain energy back more rapidly with high lust.", active = True, togglable = True, usable = False, update_func = lustful_youth_perk_update_func), "Lustful Youth")
        return

    def situational_awareness_perk_update_func():
        if len(mc.location.people) > 0:
            mc.change_locked_clarity(int(mc.location.room_outfit_eye_candy_score), add_to_log = False)
            if persistent.clarity_messages:
                log_string = "You gain " + str(int(mc.location.room_outfit_eye_candy_score)) + " Lust from eye candy in this room."
                mc.log_event(log_string, "float_text_blue")
        return

    def situational_awareness_perk_unlock():
        if perk_system.has_ability_perk("Situational Awareness"):
            return
        perk_system.add_ability_perk(Ability_Perk(description = "Gain lust based on sluttiness of girl's outfits in the area.", active = True, togglable = True, usable = False, update_func = situational_awareness_perk_update_func), "Situational Awareness")
        return
