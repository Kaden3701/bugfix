init -50 python:
    FETISH_BASIC_OPINION_LIST = ["giving handjobs", "giving tit fucks", "being fingered", "kissing", "masturbating", "big dicks", "getting head", "lingerie"]
    FETISH_ANAL_OPINION_LIST = ["anal sex", "doggy style sex", "anal creampies", "showing her ass"]
    FETISH_CUM_OPINION_LIST = ["being covered in cum","drinking cum", "cum facials", "giving blowjobs", "anal creampies", "creampies"]
    FETISH_BREEDING_OPINION_LIST = ["bareback sex","vaginal sex", "creampies", "missionary style sex"]
    FETISH_EXHIBITION_OPINION_LIST = ["public sex", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "skimpy outfits", "skimpy uniforms", "sex standing up" ]
    FETISH_RESEARCH_ADDED = 300     #Research Difficulty
    FETISH_PRODUCTION_COST = 30    #Production Difficulty
    FETISH_SERUM_ATTENTION = 3      #Attention stat. Can be reduced via IT procedures
    #relation fetishes (impact relationship with people) still need to workout how to make this happen
    FETISH_RELATION_OPTION_LIST = ["cheating on men", "incest"]
    # these fetishes could be used for 'slave' / 'dominatrix'
    FETISH_BDSM_OPTION_LIST = ["being submissive", "taking control"]

    FETISH_SERUM_TRIGGER_VALUE = 20


    def fetish_serum_unlock_count():
        return mc.business.event_triggers_dict.get("fetish_serum_count", 0)

    def start_anal_fetish_quest(person):
        if not is_anal_fetish_unlocked():
            return False
        if person.has_started_anal_fetish:
            return False
        if person.has_taboo("anal_sex"):
            return False

        if person.get_opinion_score("anal sex") < 2 \
            or person.sex_skills["Anal"] < 4 \
            or person.sluttiness < 70:
                return False

        # chance to start the anal fetish quest
        if not mc.business.IT_project_is_active(anal_fetish_increase_project):
            if renpy.random.randint(0,100) > fetish_serum_roll_fetish_chance(FETISH_ANAL_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
                return False

        if person is lily:
            mc.business.mandatory_crises_list.append(anal_fetish_lily_intro)
            return True
        elif person is mom:
            mc.business.mandatory_crises_list.append(anal_fetish_mom_intro)
            return True
        # elif person is aunt and False:
        #     pass
        # elif person is cousin and False:
        #     pass
        elif person is starbuck and get_shop_investment_rate() >= 6.0:
            mc.business.mandatory_crises_list.append(anal_fetish_starbuck_intro)
            return True
        elif person is stephanie:
            mc.business.mandatory_crises_list.append(anal_fetish_stephanie_intro)
            return True
        # elif person is emily and False:
        #     pass
        # elif person is christina and False:
        #     pass
        # elif person is sarah and False:
        #     pass
        # elif person is salon_manager and False:
        #     pass
        elif person is erica and erica_has_given_morning_handjob():
            mc.business.add_mandatory_morning_crisis(anal_fetish_erica_intro)
            return True
        elif "candace" in globals() and person is candace and False:
            pass
        # elif person is ashley and False:
        #     pass
        # elif person is alexia and False:
        #     pass
        # elif person is kaya and False:
        #     pass
        # elif person is ellie and False:
        #     pass
        # elif person is camilla and False:
        #     pass
        # elif person is sakari and False:
        #     pass
        elif person.is_employee:
            anal_fetish_employee_intro = Fetish_Action("Employee Anal Fetish Intro", anal_fetish_employee_intro_requirement, "anal_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "anal")
            mc.business.add_mandatory_crisis(anal_fetish_employee_intro)
            return True
        elif person.is_family:
            person.add_unique_on_room_enter_event(anal_fetish_family_intro)
            return True
        else:
            person.add_unique_on_talk_event(anal_fetish_generic_intro)
            return True
        return False

    def start_breeding_fetish_quest(person):
        #Determine who it is, then add the appropriate quest.
        if persistent.pregnancy_pref == 0:
            return False

        if not is_breeding_fetish_unlocked():
            return False
        if person.has_started_breeding_fetish:
            return False
        if person.has_taboo(["condomless_sex", "vaginal_sex"]):
            return False

        if person.get_opinion_score("bareback sex") < 2 \
            or person.sex_skills["Vaginal"] < 4 \
            or person.sluttiness < 70: \
                return False

        # chance to start the anal fetish quest
        if not mc.business.IT_project_is_active(breeder_fetish_increase_project):
            if renpy.random.randint(0,100) > fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
                return False

        if person is mom:
            mc.business.mandatory_morning_crises_list.append(breeding_fetish_mom_intro)
            return True
        elif person is lily:
            lily.add_unique_on_room_enter_event(breeding_fetish_lily_intro)
            return True
        # elif person is aunt and False:
        #     pass
        # elif person is cousin and False:
        #     pass
        elif person is stephanie:
            mc.business.mandatory_crises_list.append(breeding_fetish_stephanie_intro)
            return True
        # elif person is emily and False:
        #     pass
        # elif person is christina and False:
        #     pass
        elif person is starbuck:
            mc.business.mandatory_crises_list.append(breeding_fetish_starbuck_intro)
            return True
        elif person is sarah:
            mc.business.mandatory_crises_list.append(breeding_fetish_sarah_intro)
            return True
        # elif person is salon_manager and False:
        #     pass
        elif person is erica and erica_get_progress() >= 4:
            mc.business.mandatory_crises_list.append(breeding_fetish_erica_intro)
            return True
        elif "candace" in globals() and person is candace:
            candace.add_unique_on_room_enter_event(breeding_fetish_candace_intro)
            return True
        # elif person is ashley and False:
        #     pass
        # elif person is alexia and False:
        #     pass
        # elif person is kaya and False:
        #     pass
        # elif person is ellie and False:
        #     pass
        # elif person is camilla and False:
        #     pass
        # elif person is sakari and False:
        #     pass
        elif person is myra and myra_lewd_game_fuck_avail():
            mc.business.add_mandatory_crisis(breeding_fetish_myra_intro)
        elif person.is_employee:
            breeding_fetish_employee_intro = Fetish_Action("Employee breeding fetish intro", breeding_fetish_employee_intro_requirement, "breeding_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "breeding")
            mc.business.mandatory_crises_list.append(breeding_fetish_employee_intro)
            return True
        elif person.is_family:
            person.add_unique_on_room_enter_event(breeding_fetish_family_intro)
            return True
        else:
            person.add_unique_on_talk_event(breeding_fetish_non_employee_intro)
            return True
        return False

    def start_cum_fetish_quest(person):
        if not is_cum_fetish_unlocked():
            return False
        if person.has_started_cum_fetish:
            return False
        if person.has_taboo(["sucking_cock", "condomless_sex"]):
            return False

        if person.get_opinion_score("being covered in cum") < 2 \
            or person.sex_skills["Oral"] < 4 \
            or person.sluttiness < 70:
                return False

        # chance to start the cum fetish quest
        if not mc.business.IT_project_is_active(cum_fetish_increase_project):
            if renpy.random.randint(0,100) > fetish_serum_roll_fetish_chance(FETISH_CUM_OPINION_LIST, person) and not person.is_in_very_heavy_trance:
                return False

        if person is lily:
            mc.business.mandatory_morning_crises_list.append(cum_fetish_lily_intro)
            return True
        elif person is mom:
            mc.business.mandatory_crises_list.append(cum_fetish_mom_intro)
            return True
        elif person is aunt:
            person.add_unique_on_room_enter_event(cum_fetish_rebecca_intro)
            return True
        elif person is stephanie and person.has_role(head_researcher) and person.personality != bimbo_personality and False:
            pass
        elif person is sarah:
            mc.business.mandatory_crises_list.append(cum_fetish_sarah_intro)
            return True
        elif person is erica and erica_get_progress() >= 4:
            erica.add_unique_on_room_enter_event(cum_fetish_erica_intro)
            return True
        # elif person is kaya and False:
        #     pass
        # elif person is ellie and False:
        #     pass
        # elif person is camilla and False:
        #     pass
        # elif person is sakari and False:
        #     pass
        elif person.is_employee:
            cum_fetish_employee_intro = Fetish_Action("Employee cum fetish intro", cum_fetish_employee_intro_requirement, "cum_fetish_employee_intro_label", args = person, priority = 10, fetish_type = "cum")
            mc.business.mandatory_crises_list.append(cum_fetish_employee_intro)
            return True
        elif person.is_family:
            person.add_unique_on_room_enter_event(cum_fetish_family_intro)
            return True
        else:
            cum_fetish_generic_intro = Fetish_Action("Someone needs cum", cum_fetish_generic_intro_requirement, "cum_fetish_generic_intro_label", args = person, priority = 10, fetish_type = "cum")
            mc.business.add_mandatory_crisis(cum_fetish_generic_intro)
            return True
        return False

    def start_exhibition_fetish_quest(person):
        if not is_breeding_fetish_unlocked():
            return False
        if person.has_started_exhibition_fetish:
            return False
        if person.has_taboo(["sucking_cock", "vaginal_sex"]):
            return False

        if person.get_opinion_score("public sex") < 2 \
            or person.sex_skills["Oral"] < 4 \
            or person.sex_skills["Vaginal"] < 4 \
            or person.sex_skills["Anal"] < 4 \
            or person.sluttiness < 70:
            return False

        if not mc.business.IT_project_is_active(exhibition_fetish_increase_project):
            if renpy.random.randint(0,100) > fetish_serum_roll_fetish_chance(FETISH_EXHIBITION_OPINION_LIST, person) and not person.is_in_very_heavy_trance():
                return False

        return False #None of them are written yet

    def fetish_serum_increase_opinion(opinion_list, max_value, person): #WE purposefully increase a score EVERY time this function is used instead of RNG
        avail_opinions = [x for x in opinion_list if person.get_opinion_score(x) < max_value]
        if person.is_dominant and "being submissive" in avail_opinions:   # prevent dominant person from becoming submissive
            avail_opinions.remove("being submissive")
        if avail_opinions:
            person.increase_opinion_score(get_random_from_list(avail_opinions), max_value, True)
            return True #Return true if we increased an opinion
        return False

    def fetish_serum_calculate_completion(person, serum_tag):
        counter = person.event_triggers_dict.get(serum_tag, 0)
        return __builtin__.round((counter / float(FETISH_SERUM_TRIGGER_VALUE)) * 100, 1)

    def fetish_serum_increase_counter(person, serum_tag):
        person.event_triggers_dict[serum_tag] = person.event_triggers_dict.get(serum_tag, 0) + person.suggest_tier + 1
        return

    def fetish_serum_roll_fetish_chance(opinion_list, person):
        fetish_odds = (person.suggest_tier * 20) #Up to 60 points based on suggestibility
        opinion_modifier = sum((person.get_opinion_score(x) * 20) for x in opinion_list) / __builtin__.len(opinion_list)
        return fetish_odds + int(opinion_modifier)

    def fetish_basic_function_on_apply(person, the_serum, add_to_log):
        person.event_triggers_dict["nano_bots_f"] = False
        return

    def fetish_basic_function_on_remove(person, the_serum, add_to_log):
        if not person.event_triggers_dict.get("nano_bots_f", False): # no trigger, report progress
            mc.log_event((person.title or person.name) + " sexual proclivity bots: " + str(fetish_serum_calculate_completion(person, "nano_bots_fc")) + "%", "float_text_blue")
        return

    def fetish_basic_function_on_turn(person, the_serum, add_to_log):
        if person.event_triggers_dict.get("nano_bots_f", False):
            return # this fetish already triggered (prevents stacking multiple basic fetish serums)

        fetish_serum_increase_counter(person, "nano_bots_fc")

        # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
        if person.event_triggers_dict.get("nano_bots_fc", 0) < FETISH_SERUM_TRIGGER_VALUE:
            return

        person.event_triggers_dict["nano_bots_fc"] = 0 # reset counter
        person.event_triggers_dict["nano_bots_f"] = True # block any effect for this dose

        tier = person.suggest_tier
        if renpy.random.randint(0,100) < 10 + (tier * 5): # only chance to increase skill
            person.increase_sex_skill("Foreplay", 2 + tier, add_to_log = True)

        if not fetish_serum_increase_opinion(FETISH_BASIC_OPINION_LIST, tier - 1, person):
            mc.log_event((person.title or person.name) + " sexual proclivity bots no longer effective at " + str(person.suggestibility) + "% suggestibility.", "float_text_blue")
        return

    def fetish_anal_function_on_apply(person, the_serum, add_to_log):
        person.event_triggers_dict["nano_bots_a"] = False
        return

    def fetish_anal_function_on_remove(person, the_serum, add_to_log):
        if not person.event_triggers_dict.get("nano_bots_a", False): # no trigger, report progress
            mc.log_event((person.title or person.name) + " anal proclivity Bots: " + str(fetish_serum_calculate_completion(person, "nano_bots_ac")) + "%", "float_text_blue")
        return

    def fetish_anal_function_on_turn(person, the_serum, add_to_log):
        if person.event_triggers_dict.get("nano_bots_a", False):
            return # this fetish already triggered (prevents stacking multiple basic fetish serums)

        fetish_serum_increase_counter(person, "nano_bots_ac")

        # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
        if person.event_triggers_dict.get("nano_bots_ac", 0) < FETISH_SERUM_TRIGGER_VALUE:
            return

        person.event_triggers_dict["nano_bots_ac"] = 0 # reset counter
        person.event_triggers_dict["nano_bots_a"] = True # block any effect for this dose

        tier = person.suggest_tier
        if renpy.random.randint(0,100) < 10 + (tier * 5): # only chance to increase skill
            person.increase_sex_skill("Anal", 2 + tier, add_to_log = True)
        if renpy.random.randint(0,100) < (person.suggestibility - (person.obedience - 90)) * 3:
            person.change_obedience(1, add_to_log = True)

        if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, tier - 1, person):
            if person.sex_skills["Anal"] < 2 + tier:
                person.increase_sex_skill("Anal", 2 + tier, add_to_log = True)
            else:
                mc.log_event((person.title or person.name) + " anal proclivity bots reduced effectiveness at " + str(person.suggestibility) + "% suggestibility.", "float_text_blue")

        if start_anal_fetish_quest(person):
            person.event_triggers_dict["anal_fetish_start"] = True
            #TODO some kind of test here to indicate to the player that their anal quest has started
        else:
            #TODO throw some kind of error here to indicate that I haven't created this scenario yet
            pass
        return

    def fetish_breeding_function_on_apply(person, the_serum, add_to_log):
        person.event_triggers_dict["nano_bots_b"] = False
        return

    def fetish_breeding_function_on_remove(person, the_serum, add_to_log):
        if not person.event_triggers_dict.get("nano_bots_b", False): # no trigger, report progress
            mc.log_event((person.title or person.name) + " reproduction proclivity bots: " + str(fetish_serum_calculate_completion(person, "nano_bots_bc")) + "%", "float_text_blue")
        return

    def fetish_breeding_function_on_turn(person, the_serum, add_to_log):
        if person.event_triggers_dict.get("nano_bots_b", False):
            return # this fetish already triggered (prevents stacking multiple basic fetish serums)

        fetish_serum_increase_counter(person, "nano_bots_bc")
        person.change_baby_desire(5)

        # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
        if person.event_triggers_dict.get("nano_bots_bc", 0) < FETISH_SERUM_TRIGGER_VALUE:
            return

        person.event_triggers_dict["nano_bots_bc"] = 0 # reset counter
        person.event_triggers_dict["nano_bots_b"] = True # block any effect for this dose

        tier = person.suggest_tier
        if renpy.random.randint(0,100) < 10 + (tier * 5):
            person.increase_sex_skill("Vaginal", 2 + tier, add_to_log = True)
        if renpy.random.randint(0,100) < (person.suggestibility - (person.happiness - 100)) * 3:
            person.change_happiness(1, add_to_log = True)

        if not fetish_serum_increase_opinion(FETISH_BREEDING_OPINION_LIST, tier - 1, person):
            if person.sex_skills["Vaginal"] < 2 + tier:
                person.increase_sex_skill("Vaginal", 2 + tier, add_to_log = True)
            else:
                mc.log_event((person.title or person.name) + " reproduction proclivity bots reduced effectiveness at " + str(person.suggestibility) + "% suggestibility.", "float_text_blue")

        if persistent.pregnancy_pref == 0:  # pregnancy is disabled, so don't run rest of function
            return

        # going off birth-control
        if fetish_serum_roll_fetish_chance(FETISH_BREEDING_OPINION_LIST, person) >= 50 and person.on_birth_control:
            person.add_unique_on_talk_event(breeding_fetish_going_off_BC)

        if start_breeding_fetish_quest(person):
            person.event_triggers_dict["breeding_fetish_start"] = True
            person.on_birth_control = False
            #TODO some kind of test here to indicate to the player that their breeding quest has started
        else:
            #TODO throw some kind of error here to indicate that I haven't created this scenario yet
            pass
        return

    def fetish_cum_function_on_apply(person, the_serum, add_to_log):
        person.event_triggers_dict["nano_bots_c"] = False
        return

    def fetish_cum_function_on_remove(person, the_serum, add_to_log):
        if not person.event_triggers_dict.get("nano_bots_c", False): # no trigger, report progress
            mc.log_event((person.title or person.name) + " semen proclivity bots: " + str(fetish_serum_calculate_completion(person, "nano_bots_cc")) + "%", "float_text_blue")
        return

    def fetish_cum_function_on_turn(person, the_serum, add_to_log):
        if person.event_triggers_dict.get("nano_bots_c", False):
            return # this fetish already triggered (prevents stacking multiple basic fetish serums)

        fetish_serum_increase_counter(person, "nano_bots_cc")

        # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
        if person.event_triggers_dict.get("nano_bots_cc", 0) < FETISH_SERUM_TRIGGER_VALUE:
            return

        person.event_triggers_dict["nano_bots_cc"] = 0 # reset counter
        person.event_triggers_dict["nano_bots_c"] = True # block any effect for this dose

        tier = person.suggest_tier
        if renpy.random.randint(0,100) < 10 + (tier * 5): # only chance to increase skill
            person.increase_sex_skill("Oral", 2 + tier, add_to_log = True)
        if person.sluttiness < person.suggestibility:
            if renpy.random.randint(0,100) < (30 - (person.suggestibility - person.sluttiness)):
                person.change_slut(1, add_to_log = add_to_log)

        if not fetish_serum_increase_opinion(FETISH_CUM_OPINION_LIST, tier - 1, person):
            if person.sex_skills["Oral"] < 2 + tier:
                person.increase_sex_skill("Oral", 2 + tier, add_to_log = True)
            else:
                mc.log_event((person.title or person.name) + " semen proclivity bots reduced effectiveness at " + str(person.suggestibility) + "% suggestibility.", "float_text_blue")

        if start_cum_fetish_quest(person):
            person.event_triggers_dict["cum_fetish_start"] = True
            #TODO some kind of test here to indicate to the player that their cum quest has started
        else:
            #TODO throw some kind of error here to indicate that I haven't created this scenario yet
            pass
        return

    def fetish_exhibition_function_on_apply(person, the_serum, add_to_log):
        person.event_triggers_dict["nano_bots_e"] = False
        return

    def fetish_exhibition_function_on_remove(person, the_serum, add_to_log):
        if not person.event_triggers_dict.get("nano_bots_e", False):   # no trigger, report progress
            mc.log_event((person.title or person.name) + " social sexual proclivity bots: " + str(fetish_serum_calculate_completion(person, "nano_bots_ec")) + "%", "float_text_blue")
        return

    def fetish_exhibition_on_turn(person, the_serum, add_to_log):
        if person.event_triggers_dict.get("nano_bots_e", False):
            return # this fetish already triggered (prevents stacking multiple basic fetish serums)

        fetish_serum_increase_counter(person, "nano_bots_ec")

        # determine if we trigger on this turn (long running serums with high suggestibility have a higher chance of working)
        if person.event_triggers_dict.get("nano_bots_ec", 0) < FETISH_SERUM_TRIGGER_VALUE:
            return

        person.event_triggers_dict["nano_bots_ec"] = 0 # reset counter
        person.event_triggers_dict["nano_bots_e"] = True # block any effect for this dose

        tier = person.suggest_tier
        if person.sluttiness < person.suggestibility:
            if renpy.random.randint(0,100) < (30 - (person.suggestibility - person.sluttiness)):
                person.change_slut(1, add_to_log = True)
        if renpy.random.randint(0,100) < (person.suggestibility - (person.obedience - 90)) * 3:
            person.change_obedience(1, add_to_log = True)

        if not fetish_serum_increase_opinion(FETISH_EXHIBITION_OPINION_LIST, tier - 1, person):
            if person.sex_skills["Foreplay"] < 2 + tier:
                person.increase_sex_skill("Foreplay", 2 + tier, add_to_log = True)
            else:
                mc.log_event((person.title or person.name) + " social sexual proclivity bots reduced effectiveness at " + str(person.suggestibility) + "% suggestibility.", "float_text_blue")

        if start_exhibition_fetish_quest(person):
            person.event_triggers_dict["exhibition_fetish_start"] = True
            #TODO some kind of test here to indicate to the player that their exhibitionism quest has started
        else:
            #TODO throw some kind of error here to indicate that I haven't created this scenario yet
            pass
        return

    def unlock_fetish_serum(serum):
        if not serum or serum.researched: # prevent duplicate unlock calls
            return
        serum.tier = 1
        serum.researched = True
        mc.business.event_triggers_dict["fetish_serum_count"] = fetish_serum_unlock_count() + 1
        return

    def fetish_unlock_basic_serum():
        unlock_fetish_serum(get_fetish_basic_serum())
        return

    def get_fetish_basic_serum():
        return find_in_list(lambda x: x.name == "Sexual Proclivity Nanobots", list_of_traits)

    def fetish_unlock_anal_serum():
        unlock_fetish_serum(get_fetish_anal_serum())
        return

    def get_fetish_anal_serum():
        return find_in_list(lambda x: x.name == "Anal Proclivity Nanobots", list_of_traits)

    def fetish_unlock_exhibition_serum():
        unlock_fetish_serum(get_fetish_exhibition_serum())
        return

    def get_fetish_exhibition_serum():
        return find_in_list(lambda x: x.name == "Social Sexual Proclivity Nanobots", list_of_traits)

    def fetish_unlock_cum_serum():
        unlock_fetish_serum(get_fetish_cum_serum())
        return

    def get_fetish_cum_serum():
        return find_in_list(lambda x: x.name == "Semen Proclivity Nanobots", list_of_traits)

    def fetish_unlock_breeding_serum():
        unlock_fetish_serum(get_fetish_breeding_serum())
        return

    def get_fetish_breeding_serum():
        return find_in_list(lambda x: x.name == "Reproduction Proclivity Nanobots", list_of_traits)

    def add_fetish_serum_traits():
        fetish_basic_serum = SerumTraitMod(name = "Sexual Proclivity Nanobots",
            desc = "Targeted endorphin emitters increase general positive sexual responses based on suggestibility.",
            positive_slug = "Increases sexual opinions, slowly increases Foreplay skill",
            negative_slug = "+" + str(FETISH_PRODUCTION_COST) + " Production/Batch",
            research_added = FETISH_RESEARCH_ADDED,
            slots_added = 1,
            production_added = FETISH_PRODUCTION_COST,
            base_side_effect_chance = 0,
            on_apply = fetish_basic_function_on_apply,
            on_remove = fetish_basic_function_on_remove,
            on_turn = fetish_basic_function_on_turn,
            tier = 99,
            start_researched = False,
            research_needed = 1000,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1000,
            mental_aspect = 3, physical_aspect = 3, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
            allow_toggle = False
        )

        fetish_exhibition_serum = SerumTraitMod(name = "Social Sexual Proclivity Nanobots",
            desc = "Targeted endorphin emitters increase general positive opinions of public sexual encounters based on suggestibility.",
            positive_slug = "Increases exhibitionistic behavior, slow increases sluttiness",
            negative_slug = "+" + str(FETISH_PRODUCTION_COST) + " Production/Batch",
            research_added = FETISH_RESEARCH_ADDED,
            slots_added = 1,
            production_added = FETISH_PRODUCTION_COST,
            base_side_effect_chance = 0, #0 on purpose or typo?
            on_apply = fetish_exhibition_function_on_apply,
            on_remove = fetish_exhibition_function_on_remove,
            on_turn = fetish_exhibition_on_turn,
            tier = 99,
            start_researched =  False,
            research_needed = 1200,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1000,
            mental_aspect = 5, physical_aspect = 2, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
            allow_toggle = False
        )

        fetish_anal_serum = SerumTraitMod(name = "Anal Proclivity Nanobots",
            desc = "Targeted endorphin emitters increase pleasure received from anal stimulation based on suggestibility.",
            positive_slug = "Increases Anal sexual opinions, slowly increases Anal skill, Slowly increases obedience",
            negative_slug = "+" + str(FETISH_PRODUCTION_COST) + " Production/Batch",
            research_added = FETISH_RESEARCH_ADDED,
            slots_added = 1,
            production_added = FETISH_PRODUCTION_COST,
            base_side_effect_chance = 0,
            on_apply = fetish_anal_function_on_apply,
            on_remove = fetish_anal_function_on_remove,
            on_turn = fetish_anal_function_on_turn,
            tier = 99,
            start_researched =  False,
            research_needed = 2000,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1500,
            mental_aspect = 4, physical_aspect = 6, sexual_aspect = 6, medical_aspect = 1, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
            allow_toggle = False
        )

        fetish_cum_serum = SerumTraitMod(name = "Semen Proclivity Nanobots",
            desc = "Targeted endorphin emitters increase pleasure received when in contact with semen based on suggestibility.",
            positive_slug = "Increases Cum related sexual opinions, slowly increases sluttiness, slowly increases Oral skill",
            negative_slug = "+" + str(FETISH_PRODUCTION_COST) + " Production/Batch",
            research_added = FETISH_RESEARCH_ADDED,
            slots_added = 1,
            production_added = FETISH_PRODUCTION_COST,
            base_side_effect_chance = 0,
            on_apply = fetish_cum_function_on_apply,
            on_remove = fetish_cum_function_on_remove,
            on_turn = fetish_cum_function_on_turn,
            tier = 99,
            start_researched =  False,
            research_needed = 2000,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1500,
            mental_aspect = 5, physical_aspect = 3, sexual_aspect = 6, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
            allow_toggle = False
        )

        fetish_breeding_serum = SerumTraitMod(name = "Reproduction Proclivity Nanobots",
            desc = "Targeted endorphin emitters increase reproduction drive and associated opinions based on suggestibility.",
            positive_slug = "Increases reproduction sexual opinions, slowly increases Vaginal skill",
            negative_slug = "+" + str(FETISH_PRODUCTION_COST) + " Production/Batch",
            research_added = FETISH_RESEARCH_ADDED,
            slots_added = 1,
            production_added = FETISH_PRODUCTION_COST,
            base_side_effect_chance = 0,
            on_apply = fetish_breeding_function_on_apply,
            on_remove = fetish_breeding_function_on_remove,
            on_turn = fetish_breeding_function_on_turn,
            tier = 99,
            start_researched =  False,
            research_needed = 2000,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1500,
            mental_aspect = 5, physical_aspect = 5, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = FETISH_SERUM_ATTENTION,
            allow_toggle = False
        )
        return

    def fetish_anal_serum_is_unlocked():
        return get_fetish_anal_serum().researched

    def fetish_breeding_serum_is_unlocked():
        return get_fetish_breeding_serum().researched

    def fetish_cum_serum_is_unlocked():
        return get_fetish_cum_serum().researched

    def fetish_exhibition_serum_is_unlocked():
        return get_fetish_exhibition_serum().researched

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_fetish_serum_trait(stack):
    python:
        add_fetish_serum_traits()
        execute_hijack_call(stack)
return
