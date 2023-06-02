init -3 python:


    SB_MOD_MC_AROUSAL_MULT = 1.0     #Default arousal multiplier for the MC
    SB_MOD_MC_AROUSAL_1ST_MULT = 0.9     #Arousal multiplier after the first upgrade
    SB_MOD_MC_AROUSAL_2ND_MULT = 0.8     #Arousal multiplier after second upgrade

    FETISH_VAGINAL_EVENT_LABEL_LIST = [
        "SB_fetish_mom_vaginal_label",
        "SB_fetish_lily_vaginal_label",
        "SB_fetish_vaginal_label",
        "SB_fetish_vaginal_event_label",
    ]

    FETISH_ANAL_EVENT_LABEL_LIST = [
        "SB_lily_anal_dp_fetish_label",
        "SB_mom_anal_pay_label",
        "SB_fetish_anal_label",
        "SB_fetish_anal_label_non_employee",
        "SB_fetish_anal_staylate_event_label",
        "SB_starbuck_anal_intro",
        "SB_stephanie_anal_fetish_label",
    ]

    FETISH_CUM_EVENT_LABEL_LIST = [
        "SB_fetish_mom_cum_label",
        "SB_fetish_lily_cum_label",
        "SB_fetish_cum_label",
        "SB_fetish_cum_non_employee_label",
        "SB_fetish_stephanie_cum_label",
    ]

    FETISH_BREEDING_EVENT_LABEL_LIST = [
        "breeding_fetish_employee_intro_label",
        "breeding_fetish_non_employee_intro_label",
        "breeding_fetish_mom_intro_label",
        "breeding_fetish_lily_intro_label",
        "breeding_fetish_rebecca_intro_label",
        "breeding_fetish_gabrielle_intro_label",
        "breeding_fetish_stephanie_intro_label",
        "breeding_fetish_emily_intro_label",
        "breeding_fetish_christina_intro_label",
        "breeding_fetish_starbuck_intro_label",
        "breeding_fetish_sarah_intro_label",
        "breeding_fetish_ophelia_intro_label",
        "breeding_fetish_erica_intro_label",
        "breeding_fetish_candace_intro_label",
        "breeding_fetish_ashley_intro_label",
    ]

    def SB_FETISH_EVENT_ACTIVE():
        for effect in FETISH_VAGINAL_EVENT_LABEL_LIST + FETISH_ANAL_EVENT_LABEL_LIST + FETISH_CUM_EVENT_LABEL_LIST + FETISH_BREEDING_EVENT_LABEL_LIST:
            if exists_in_mandatory_crisis_list(effect) or exists_in_mandatory_morning_crisis_list(effect):
                return True
        return False
