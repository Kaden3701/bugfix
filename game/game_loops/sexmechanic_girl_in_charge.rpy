#GLOBAL TODO before releasing this mechanic into the wild
#Need at least three positions that qualify for each sex goal for variety.
#Add new personality dialogue.
#Add dialogue based on sex goals
#Control where MC finishes based on sex goals to have a better chance of meeting the goal.



init -2:
    python:
        list_of_selfish_dom_sex_goals = []
        list_of_selfish_dom_sex_goals.append("get off")
        list_of_selfish_dom_sex_goals.append("waste cum")  #Unrealistic until we can control where MC finishes. Thru new sex options?
        #list_of_selfish_dom_sex_goals.append("hate fuck")  #We can't yet reliably path to this. Not enough pathing options

        list_of_unselfish_dom_sex_goals = []
        list_of_unselfish_dom_sex_goals.append("vaginal creampie")
        list_of_unselfish_dom_sex_goals.append("anal creampie")
        list_of_unselfish_dom_sex_goals.append("facial")
        list_of_unselfish_dom_sex_goals.append("body shot")
        list_of_unselfish_dom_sex_goals.append("get mc off") #Generally this will be foreplay tags
        list_of_unselfish_dom_sex_goals.append("oral creampie")

        list_of_all_dom_sex_goals = list_of_selfish_dom_sex_goals + list_of_unselfish_dom_sex_goals

        class dom_sex_path_node():
            def __init__(self, position, completion_requirement = True):
                self.position = position
                self.completion_requirement =  completion_requirement

init 3 python: #Add appropriate opinion tags to all vanilla positions
    blowjob.opinion_tags.append("get mc off")
    blowjob.opinion_tags.append("oral creampie")
    blowjob.opinion_tags.append("facial")
    blowjob.opinion_tags.append("body shot")
    cowgirl.opinion_tags.append("vaginal creampie")
    cowgirl.opinion_tags.append("get off")
    cowgirl.opinion_tags.append("hate fuck")
    cowgirl.opinion_tags.append("body shot")
    deepthroat.opinion_tags.append("oral creampie")
    handjob.opinion_tags.append("get mc off")
    handjob.opinion_tags.append("waste cum")
    handjob.opinion_tags.append("body shot")  #Change this later if we come up with a better position
    skull_fuck.opinion_tags.append("oral creampie")
    tit_fuck.opinion_tags.append("body shot")


init -1:
    python:
        #List of completion requirements for different possible dom sex positions.
        def dom_requirement_creampie(person, the_report):
            if the_report["guy orgasms"] >= 1 and person.has_creampie_cum:
                return True
            return False

        def dom_requirement_anal_creampie(person, the_report):
            if the_report["guy orgasms"] >= 1 and person.has_creampie_cum:
                return True
            return False

        def dom_requirement_oral_creampie(person, the_report):
            if the_report["guy orgasms"] >= 1 and person.has_mouth_cum:
                return True
            return False

        def dom_requirement_facial(person, the_report):
            if the_report["guy orgasms"] >= 1 and person.has_face_cum:
                return True
            return False

        def dom_requirement_body_shot(person, the_report):
            if the_report["guy orgasms"] >= 1:
                if person.has_ass_cum or person.has_tits_cum or person.has_stomach_cum or person.has_face_cum:
                    return True
            return False

        def dom_requirement_get_mc_off(person, the_report):
            if the_report["guy orgasms"] >= 1:
                return True
            return False

        def dom_requirement_get_off(person, the_report):
            if the_report["girl orgasms"] >= 1:
                return True
            return False

        def dom_requirement_hate_fuck(person, the_report):
            if the_report["girl orgasms"] >= 2:
                return True
            return False

        def dom_requirement_waste_cum(person, the_report):
            if the_report["guy orgasms"] >= 1:
                return True
            return False

        def dom_requirement_mc_hard(person, the_report):
            return mc.arousal_perc > 20

        def dom_requirement_mc_aroused(person, the_report):
            return mc.arousal_perc > 40

        def dom_requirement_mc_highly_aroused(person, the_report):
            return mc.arousal_perc > 70

        def dom_requirement_girl_aroused(person, the_report):
            return person.arousal_perc > 40

        def dom_requirement_girl_highly_aroused(person, the_report):
            return person.arousal_perc > 70

        def dom_requirement_girl_vagina_avail(person, the_report):
            return person.vagina_available

        def dom_requirement_tits_avail(person, the_report):
            return person.tits_available

        def construct_mc_turn_on_weighted_list(person, prohibit_tags = []):
            position_option_list = []
            position_option_list.append([kissing, 30 + person.get_opinion_score("kissing")])
            position_option_list.append([handjob, 30 + person.get_opinion_score("giving handjobs")])
            position_option_list.append([drysex_cowgirl, 30 + person.get_opinion_score("taking control")])
            return get_random_from_weighted_list(position_option_list)

        def set_sex_goal(person, the_goal):
            person.event_triggers_dict["sex_goal"] = the_goal
            return

        def reset_sex_goal(person):
            person.event_triggers_dict["sex_goal"] = None
            return



init 2:
    python:
        #Use this function to make a "random" sex goal. Weights outcome based on the person and how far things have already gone.
        #weight is scale 0-100
        def create_sex_goal(person, report_log = None):
            if report_log is not None: #First, check if we are here
                if report_log.get("guy orgasms", 0) > 0 and report_log.get("girl orgasms", 0) == 0:   #We are here because Mc finished too fast.
                    pass #TODO do this here or in the original call?

            dom_sex_goal_weighted_list = []

            if person.fetish_count > 0: #She has fetishes, so use those to set a goal.
                if person.has_anal_fetish:
                    dom_sex_goal_weighted_list.append(["anal creampie", 100])
                if person.has_cum_fetish:
                    dom_sex_goal_weighted_list.append(["oral creampie", 50])
                    dom_sex_goal_weighted_list.append(["body shot", 50])
                    dom_sex_goal_weighted_list.append(["facial", 50])
                if person.has_breeding_fetish:
                    dom_sex_goal_weighted_list.append(["vaginal creampie", 100])
                return get_random_from_weighted_list(dom_sex_goal_weighted_list)  #Hopefully this works if list only has one entry

            # If love is less than 0, we consider selfish sex goals
            if person.love < 0:
                for goal in list_of_selfish_dom_sex_goals:
                    dom_sex_goal_weighted_list.append ([goal,-person.love])
            else: #Always have at least one option in the list
                dom_sex_goal_weighted_list.append(["get mc off", 30])

            #Next, we add individual goals based on her sluttiness. #TODO consider a list of constants declared at the top that can be changed for setting sluttiness threshholds for these.
            #body shot
            if person.sluttiness > 30:
                body_shot_weight = 40 + (person.get_opinion_score("being covered in cum") * 10)
                dom_sex_goal_weighted_list.append(["body shot", body_shot_weight])

            #Facial
            if person.sluttiness > 40:
                facial_weight = 40 + (person.get_opinion_score("being covered in cum") * 10) + (person.get_opinion_score("cum facials") * 10)
                dom_sex_goal_weighted_list.append(["facial", facial_weight])

            #oral creampie
            if person.sluttiness > 50:
                oral_creampie_weight = 40 + (person.get_opinion_score("drinking cum") * 20)
                dom_sex_goal_weighted_list.append(["oral creampie", oral_creampie_weight])

            #vaginal creampie
            if person.sluttiness > 60:
                vaginal_creampie_weight = 40 + (person.get_opinion_score("creampies") * 20)
                dom_sex_goal_weighted_list.append(["vaginal creampie", vaginal_creampie_weight])

            #anal creampie
            if person.sluttiness > 70:
                anal_creampie_weight = 40 + (person.get_opinion_score("anal creampies") * 20)
                dom_sex_goal_weighted_list.append(["anal creampie", anal_creampie_weight])

            return get_random_from_weighted_list(dom_sex_goal_weighted_list)

        def build_blowjob_path(person):
            path = [] # start off with normal blowjob
            path.append(dom_sex_path_node(blowjob, dom_requirement_mc_aroused))

            transition = deepthroat
            if person.sex_skills["Oral"] >= 5 and person.get_opinion_score("giving blowjobs") > 1 and person.get_opinion_score("being submissive") > 1:
                transition = skull_fuck
            if person.has_cum_fetish:
                transition = cum_fetish_blowjob
            if person == salon_manager:
                transition = Ophelia_blowjob

            path.append(dom_sex_path_node(transition, dom_requirement_get_mc_off))
            return path

        def build_titfuck_path(person):
            path = [] # use handjob as intro
            path.append(dom_sex_path_node(handjob, dom_requirement_mc_hard))

            transition = tit_fuck
            if person == sarah:
                transition = sarah_tit_fuck

            if person.has_cum_fetish: # when she has a cum fetish she will finish you off with her mouth
                path.append(dom_sex_path_node(transition, dom_requirement_mc_highly_aroused))
                path.append(dom_sex_path_node(cum_fetish_blowjob, dom_requirement_get_mc_off))
            else: # complete titfuck
                path.append(dom_sex_path_node(transition, dom_requirement_get_mc_off))
            return path

        def create_sex_path(person, the_goal, prohibit_tags = []):
            position_option_list = []
            second_position_option_list = []
            extra_positions = []
            ### Create list of possible positions###
            # when she enjoys blow jobs, add one to her choices (to prevent always going to blowjob variant)
            if person.has_cum_fetish:
                extra_positions.append(cum_fetish_blowjob)
            elif person.sex_skills["Oral"] >= 5 and person.get_opinion_score("giving blowjobs") > 1 and person.get_opinion_score("being submissive") > 1:
                extra_positions.append(skull_fuck)
            elif person.sex_skills["Oral"] > 3 and person.get_opinion_score("giving blowjobs") > 1:
                extra_positions.append(deepthroat)
            elif person.sex_skills["Oral"] > 2 and person.get_opinion_score("giving blowjobs") > 0:
                extra_positions.append(blowjob)
            elif the_goal == "oral creampie" or the_goal == "facial":
                extra_positions.append(blowjob)

            # when she enjoys tit fucks, add it to her position choices
            if person.sex_skills["Foreplay"] > 2 and person.get_opinion_score("giving tit fucks") >= 1 and person.has_large_tits:
                extra_positions.append(tit_fuck)

            #TODO we also need to check and make sure an object exists for each possible sex position. Figure out how to do this
            #TODO Add in per character position filters so make sure ALL positions are included
            for position in list_of_girl_positions + extra_positions:
                if the_goal in position.opinion_tags:
                    if person.sluttiness >= position.slut_requirement:
                        if not position.skill_tag in prohibit_tags:
                            position_option_list.append([position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))])  #every qualifying position has at least weight 20, with higher weights if actual sluttiness is close to requirement

            if len(position_option_list) == 0: #Somehow no positions available for this requirement.
                return None

            #Construct final node by choosing appropriately tagged final position
            final_node = dom_sex_path_node(get_random_from_weighted_list(position_option_list))
            if the_goal == "get off":
                final_node.completion_requirement = dom_requirement_get_off
            if the_goal =="waste cum":
                final_node.completion_requirement = dom_requirement_waste_cum
            if the_goal =="hate fuck":
                final_node.completion_requirement = dom_requirement_hate_fuck
            if the_goal =="vaginal creampie":
                final_node.completion_requirement = dom_requirement_creampie
            if the_goal =="anal creampie":
                final_node.completion_requirement = dom_requirement_anal_creampie
            if the_goal =="facial":
                final_node.completion_requirement = dom_requirement_facial
            if the_goal =="body shot":
                final_node.completion_requirement = dom_requirement_body_shot
            if the_goal =="get mc off":
                final_node.completion_requirement = dom_requirement_get_mc_off
            if the_goal =="oral creampie":
                final_node.completion_requirement = dom_requirement_oral_creampie

            ###Construct path to final node
            #First, we explore cases where we MUST have an earlier node
            req_func = None
            first_position = None

            #She isn't naked enough to go straight to final node
            if not final_node.position.check_clothing(person):  #She isn't naked enough to go straight to the end node
                for position in list_of_girl_positions + extra_positions:
                    if person.allow_position(position) and mc.location.has_object_with_trait(position.requires_location) and (person.has_large_tits or not position.requires_large_tits):
                        if position.check_clothing(person):
                            if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                                if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))])
                            else:
                                if position.skill_tag == "Foreplay":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))])
                if len(second_position_option_list) == 0: #No workable options.
                    return None
                first_position = get_random_from_weighted_list(second_position_option_list)
                if final_node.position.requires_clothing == "Vagina":
                    req_func = dom_requirement_girl_vagina_avail
                else:
                    req_func = dom_requirement_tits_avail

            #MC isn't hard enough for final node
            elif mc.recently_orgasmed and final_node.position.requires_hard:
                first_position = construct_mc_turn_on_weighted_list(person, prohibit_tags)
                req_func = dom_requirement_mc_aroused

            #If we don't have a first node, 50/50 chance we create a first node, or sex begins with final node
            elif renpy.random.randint(0,100) < 50:
                for position in list_of_girl_positions + extra_positions:
                    if person.allow_position(position) and mc.location.has_object_with_trait(position.requires_location) and (person.has_large_tits or not position.requires_large_tits):
                        if position.check_clothing(person):
                            if final_node.position.skill_tag == "Vaginal" or final_node.position.skill_tag == "Anal":
                                if position.skill_tag == "Foreplay" or position.skill_tag == "Oral":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))])
                            else:
                                if position.skill_tag == "Foreplay":
                                    if not position.skill_tag in prohibit_tags:
                                        second_position_option_list.append([position, max(20, 100 - abs(person.sluttiness - position.slut_requirement))])
                first_position  = get_random_from_weighted_list(second_position_option_list)

                if first_position.girl_arousal > first_position.guy_arousal: #Choose our exit function based on who the position arouses more
                    req_func = dom_requirement_girl_aroused
                else:
                    req_func = dom_requirement_mc_aroused

            ###Now we construct our path.
            sex_path = []
            if first_position is None:  #We are going straight to our final position
                sex_path.append(final_node)
                return sex_path
            else:
                first_node = dom_sex_path_node(first_position, completion_requirement = req_func)
                sex_path.append(first_node)
                sex_path.append(final_node)
                return sex_path

        def get_sex_finish_req(the_goal):
            if the_goal == "get off":
                return dom_requirement_get_off
            if the_goal =="waste cum":
                return dom_requirement_waste_cum
            if the_goal =="hate fuck":
                return dom_requirement_hate_fuck
            if the_goal =="vaginal creampie":
                return dom_requirement_creampie
            if the_goal =="anal creampie":
                return dom_requirement_anal_creampie
            if the_goal =="facial":
                return dom_requirement_facial
            if the_goal =="body shot":
                return dom_requirement_body_shot
            if the_goal =="get mc off":
                return dom_requirement_get_mc_off
            if the_goal =="oral creampie":
                return dom_requirement_oral_creampie
            return dom_requirement_get_mc_off

        def sex_can_continue(person, the_position = None, the_node = None): #Use this to check and see if girl would be up to continue the current position
            if the_node is not None:
                the_position = the_node.position

            if the_position is not None:
                if not the_position.check_clothing(person):
                    return False
                if person.energy < the_position.girl_energy * 2:  #Enough for at least 2 more rounds
                    return False

                if mc.energy < the_position.guy_energy * 2:
                    return False
            elif person.energy < 30 or mc.energy < 30:
                return False
            return True

        def requires_condom(person):
            if person == kaya and persistent.pregnancy_pref != 0:
                return False
            if person.effective_sluttiness("condomless_sex") < person.get_no_condom_threshold(situational_modifier = 10):  #
                return True
            return False

        def go_raw_mid_sex(person):
            if person.effective_sluttiness("condomless_sex") > person.get_no_condom_threshold(situational_modifier = 25):
                if renpy.random.randint(0,100) < 10:  #10% chance per round over sluttiness threshold
                    return True
            return False


label get_fucked(the_person, the_goal = None, sex_path = None, private= True, start_position = None, start_object = None, skip_intro = False, report_log = None, ignore_taboo = False, prohibit_tags = [], unit_test = False, allow_continue = True, condition = Condition_Type("Empty")):
    $ apply_sex_modifiers(the_person, private) #Apply sex modifiers before choosing goals and positions to avoid choosing positions girl shouldn't accept
    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ ask_for_threesome = False
    $ object_choice = start_object
    $ start_mc_orgasm = 0
    $ start_girl_orgasm = 0
    $ used_mc_energy_serum = False
    if report_log:  #We set orgasms in the report to zero for now so that requirement functions can check for them easier.
        $ start_mc_orgasm = report_log.get("guy orgasms", 0)
        $ start_girl_orgasm = report_log.get("girl orgasms", 0)
        $ report_log["guy orgasms"] = 0
        $ report_log["girl orgasms"] = 0
    else:
        $ report_log = create_report_log({ "was_public": not private })
        $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
        $ report_log["positions_used"] = []
        $ report_log["was_public"] = not private

    if skip_intro:  #If we are already having sex, using whatever condom status presently is
        $ using_condom = mc.condom
    else:
        $ using_condom = requires_condom(the_person)

    # generate a sex path for locked requests
    if not sex_path and not allow_continue and (not the_goal or the_goal == "get mc off"):
        if start_position == blowjob:
            $ sex_path = build_blowjob_path(the_person)
            # $ write_log("Build blowjob path: {}".format(len(sex_path)))
        if start_position == tit_fuck:
            $ sex_path = build_titfuck_path(the_person)
            # $ write_log("Build titfuck path: {}".format(len(sex_path)))

    # break taboos automatically, so the caller doesn't need to remember to do it
    if not ignore_taboo and isinstance(start_position, Position):
        # since we skip intro, it's assumed we are already in the position and use the loop to continue
        if skip_intro:
            $ the_person.break_taboo(start_position.associated_taboo)
        # we don't ask for condom and the mc is not wearing it and we are having intercourse
        if not mc.condom and start_position.skill_tag in ["Vaginal", "Anal"]:
            $ the_person.break_taboo("condomless_sex")

    if start_position and not sex_path:
        if not the_goal:
            $ the_goal = "get mc off"
        $ sex_path = [dom_sex_path_node(start_position, get_sex_finish_req(the_goal))]  #If we have a start position only, we set the path to be the start position with MC getting off as the goal

    if not the_goal:
        $ the_goal = create_sex_goal(the_person, report_log)
        if unit_test: #unit_test is for debug dialogue
            "The goal for this session is [the_goal]."

    if the_goal and not sex_path:
        $ sex_path = create_sex_path(the_person, the_goal, prohibit_tags)
        if unit_test:
            "The first position for this session is [sex_path[0].position.name]."

    if not sex_path:  #We couldn't find a sex path, so abort the session, or possibly rerun it relaxing conditions? #TODO
        "[the_person.title] can't think of anything more to do with you."
        $ finished = True
        if unit_test: #unit_test is for debug dialogue
            "No viable path."

    if not object_choice and sex_path:
        $ object_choice = girl_choose_object(the_person, sex_path[0].position)
    if not object_choice:
        "[the_person.title] can't find a good place to have fun with you."
        $ finished = True
        if unit_test:
            "No suitable object"

    if sex_path:
        $ current_node = sex_path.pop(0)  #Pop the first node in the list of sex path nodes.
    #Next we mimic fuck_person() but only with applicable girl in charge parameters.
    #Privacy modifiers
    if mc.location.person_count == 1 and not private and mc.location.privacy_level != 3 and mc.location.privacy_level != 1:
        $ private = True #If we're alone in the space we're always Private, even if we had left the possibility for people being around.
    #Next, check for generic conditions that keep us from continuing

    if not finished:
        if current_node.position is None: #There's no position we can take
            "[the_person.title] can't think of anything more to do with you."
            $ finished = True
        elif object_choice is None:
            "[the_person.title] looks around, but can't see anywhere to have fun with you."
            $ finished = True
        elif the_person.energy < 15 :
            the_person "I'm tired. Maybe we will continue this another time."
            $ finished = True

    if sex_path and len(sex_path) > 1 and not finished:
        the_person "Let's get warmed up a little bit first..."
    #TODO determine condom usage. Can probably just call a method from the sex bugfix file

    if the_goal:
        $ set_sex_goal(the_person, the_goal)
    #We should be able to initiate sex. If we need to, call initial intros and taboo breaks.
    if not skip_intro and not finished:
        $ the_person.draw_person()
        if (current_node.position.skill_tag == "Vaginal" or current_node.position.skill_tag == "Anal") and using_condom:
            the_person "Hang on a second. I need to wrap this thing up first."
            "[the_person.title] gets a condom out of their own bag and opens it."
            "She holds it at the top of your cock with one hand as she strokes further and further with the other hand, rolling the condom down onto it."
            $ mc.condom = True
        if not ignore_taboo and the_person.has_taboo(current_node.position.associated_taboo):
            # call mod taboo break
            $ current_node.position.call_transition_taboo_break(None, the_person, mc.location, object_choice)
            $ the_person.break_taboo(current_node.position.associated_taboo)
        else:
            $ current_node.position.call_intro(the_person, mc.location, object_choice)
    elif not skip_intro and not finished and start_position is None:
        # show dialog since there is probably no intro for the position
        $ current_node.position.call_transition(start_position, the_person, mc.location, object_choice)

    #Now begin the sex loop
    while not finished:
        if mc.condom and go_raw_mid_sex(the_person):
            call remove_condom_go_raw(the_person, current_node.position) from _go_raw__girl_in_charge_01
            $ mc.condom = False
            $ using_condom = False
        if mc.recently_orgasmed and not used_mc_energy_serum and allow_continue:
            if perk_system.has_ability_perk("Serum: Energy Regeneration") and mc_serum_energy_regen.trait_tier >= 2 and mc.energy > 30:
                $ mc.recently_orgasmed = False
                $ used_mc_energy_serum = True   # prevent too long looping if she has a lot of energy
                "Despite your orgasm, because of your Energy Regeneration Serum, your cock quickly gets hard again, allowing [the_person.possessive_title] to continue."
        if current_node.position.requires_hard and mc.recently_orgasmed:
            "Your post-orgasm cock softens, stopping [the_person.possessive_title] for now."
            #TODO if this keeps us from accomplishing sex goal, consider rerunning this method from the beginning, or just ending the scene. Or creating a new path?
            $ finished = True
        else:
            $ condition.call_pre_label(the_person, current_node.position, object_choice, report_log)
            $ scene_private = private
            if not private and mc.location.person_count == 1:
                $ scene_private = False #Only pass private to sex desc. if there is actually a witness

            call sex_description(the_person, current_node.position, object_choice, private = scene_private, report_log = report_log) from _call_sex_description_girl_in_charge_override_1

            $ condition.call_post_label(the_person, current_node.position, object_choice, report_log)

            $ report_log["last_position"] = current_node.position
            if not private and not mc.recently_orgasmed:
                call public_sex_post_round(the_person, current_node.position, report_log) from _public_sex_post_round_02
                if not _return:
                    $ finished = True
        if mc.condom and mc.recently_orgasmed: # you orgasmed so you used your condom.
            $ mc.condom = False

        #TODO figure out what to do in the following three cases


        if current_node.position.calculate_energy_cost(mc) > mc.energy - 5:
            "You're too exhausted to let [the_person.possessive_title] keep [current_node.position.verbing] you."
            $ finished = True

        elif current_node.position.calculate_energy_cost(the_person) > the_person.energy - 5:
            the_person "I'm exhausted [the_person.mc_title], I can't keep this up..."
            $ finished = True

        #Determine if the current node has completed it's finished requirement.
        if not finished:
            if current_node.completion_requirement(the_person, report_log):
                if len(sex_path) > 0:
                    $ current_node = sex_path.pop(0)
                    $ object_choice = girl_choose_object(the_person, current_node.position)
                    if object_choice is None:
                        if current_node.position.requires_location == "kneel" or current_node.position.requires_location == "lay":
                            $ object_choice = make_floor()
                        elif current_node.position.requires_location == "lean":
                            $ object_choice = make_wall()
                        else:
                            $ object_choice = make_chair()
                    the_person "Mmm, I think we're ready. Let's move on now!"
                    if (current_node.position.skill_tag == "Vaginal" or current_node.position.skill_tag == "Anal") and using_condom and not mc.condom:
                        the_person "Hang on a second. I need to wrap this thing up first."
                        "[the_person.title] gets a condom out of their own bag and opens it."
                        "She holds it at the top of your cock with one hand as she strokes further and further with the other hand, rolling the condom down onto it."
                        $ mc.condom = True
                    if not ignore_taboo and the_person.has_taboo(current_node.position.associated_taboo):
                        # call mod taboo break
                        $ current_node.position.call_transition_taboo_break(current_node.position, the_person, mc.location, object_choice)
                        $ the_person.break_taboo(current_node.position.associated_taboo)
                    else:
                        $ current_node.position.call_transition(current_node.position, the_person, mc.location, object_choice)

                else:
                    $ finished = True    #Sex goal has been accomplished
                    $ the_person.call_dialogue("GIC_finish_response", the_goal = the_goal)
            elif len(sex_path) > 0:
                if not sex_path[0].position.check_clothing(the_person): #We don't meet the clothing requirements for the next position, so we strip some
                    $ the_clothing = the_person.choose_strip_clothing_item()
                    $ current_node.position.call_strip(the_person, the_clothing, mc.location, object_choice)
                else:
                    call girl_strip_event(the_person, current_node.position, object_choice) from _call_girl_strip_event_girl_in_charge_01


    #TODO create positive feedback here for accomplishing sex goal
    #First condition, she is obedient. offers to keep going or to let MC take over.

    if not finished and allow_continue: #Allows sex to keep going after girl finishes objectives
        if sex_can_continue(the_person, the_node = current_node) and the_person.obedience > 100 and mc.arousal_perc > 50:
            "As she finishes up, [the_person.title] gives your erection a couple strokes."
            the_person "Actually, do you want me to keep going? Or maybe you should take over..."
            menu:
                "Keep going":
                    mc.name 'Keep going, this is hot.'
                    the_person "Yes sir!"
                    call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_01
                "Take over":
                    mc.name "Come here, I'm not done with you yet."
                    call fuck_person(the_person, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_01
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."
        #Second condition, she isn't obedient but at least likes MC a little bit. She offers to continue
        elif sex_can_continue(the_person, the_node = current_node) and the_person.love > 0 and mc.arousal_perc > 50:
            "As she finishes up, [the_person.title] gives your erection a couple strokes."
            the_person "Wow, you are still rock hard. Do you want me to keep going?"
            menu:
                "Keep going":
                    mc.name 'Yes, please keep going.'
                    the_person "Okay, I can do that!"
                    call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_02
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."

        #Third condition, she doesn't care for MC. She forces him to beg. She may or may not comply (think Gabrielle)
        elif sex_can_continue(the_person, the_node = current_node) and mc.arousal_perc > 50:
            "As she finishes up, [the_person.title] looks at your rock hard cock."
            the_person "Still hard? I bet you want me to keep going, don't you..."
            "She takes a pause before she continues."
            the_person "If you want me to keep going, you're going to have to beg for it. Want me to?"
            menu:
                "Beg her to continue":
                    mc.name "Oh god, please keep going. I'm so close, just a little bit farther!"
                    "She laughs at your plight while she considers what to do."
                    if renpy.random.randint(-150,0) < the_person.love:  #Even at -100 love, she has a 1/3 chance of continuing
                        the_person "Hmm, I guess it's only fair. Maybe I'll even finish again!"
                        $ the_person.change_stats(obedience = -5)
                        call get_fucked(the_person, private= private, start_position = current_node.position, start_object = object_choice, skip_intro = True, report_log = report_log, ignore_taboo = ignore_taboo, prohibit_tags = prohibit_tags, unit_test = unit_test, condition = condition) from GIC_keeps_going_03
                    else:
                        the_person "Ha! It was worth letting you defile me just to hear you beg. Not a chance!"
                        "[the_person.possessive_title] gets up, leaving you hanging."
                        $ the_person.change_stats(obedience = -5, slut = -1)
                "Finish":
                    mc.name "There's nothing special about you. Let's be done, I can always get a more willing cunt."
                    the_person "Whatever [the_person.mc_title], your loss!"
                    $ the_person.change_stats(obedience = 2, love = -5)
        elif sex_can_continue(the_person) and the_person.love > 50: #She loves you, so she leaves it up to you if you want to keep going.
            "As she finishes up, [the_person.title] cuddles up beside you."
            the_person "Mmm, thank you. I needed that really bad."
            "She pauses for a moment."
            the_person "Are you good? Or do you want to keep going?"
            menu:
                "Take over":
                    mc.name "Come here, I'm not done with you yet."
                    call fuck_person(the_person, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_03
                "Finish":
                    mc.name "Let's be done for now."
                    the_person "Okay."
        elif the_person.energy < 50 and mc.arousal_perc > 70 and the_person.energy > 20 and mc.energy > 30: #She's exhausted and can't defend herself briefly from your advances.
            "You get up, but notice that [the_person.title] is a bit slower. She is breathing heavily and appears to be really worn out."
            the_person "Oh god... just give me a minute, okay?"
            $ the_person.draw_person(position = "doggy")
            "She gets on her hands and knees and is obviously worn out. Her current position leaves her ass obviously exposed. You give your rock hard cock a couple strokes and consider taking advantage."
            "She doesn't have the energy to stop you, but if she doesn't like you she might get pretty upset..."
            menu:
                "Fuck her":
                    "You get behind her. You line yourself up with her cunt."
                    the_person "Hey... [the_person.mc_title]... what are you doing?"
                    mc.name "Shhh, quiet."
                    "With one smooth motion you push yourself inside of her."
                    if the_person.effective_sluttiness() > 90:
                        the_person "Ohhh god. Go ahead and take what you want, I'll just be along for the ride."
                    elif the_person.effective_sluttiness() > 60:
                        the_person "Ohhhhhh. I'm not sure how long I can do this but if you need to finish that bad go ahead..."
                    else:
                        the_person "What the fuck? Are you kidding me?"
                        "You give her ass a sharp spank."
                        mc.name "Quiet. I'm close to cumming, this will only take a minute."
                        $ the_person.add_situational_obedience("finish_him",40,"Whatever, just hurry up and finish.")
                        $ the_person.change_stats(happiness = -5, love = -5)
                    call fuck_person(the_person,start_position = doggy, private = private, ignore_taboo = ignore_taboo, report_log = report_log, prohibit_tags = prohibit_tags, condition = condition) from GIC_guy_takes_over_05
                    $ the_person.clear_situational_obedience("finish_him")
                "Finish":
                    "You decide to leave her be."

    python:
        condition.run_rewards(the_person, report_log)
        clear_sex_modifiers(the_person)

        report_log["end arousal"] = the_person.arousal
        report_log["girl orgasms"] = report_log.get("girl orgasms",0) + start_girl_orgasm

        the_person.change_arousal(-__builtin__.max((the_person.arousal/(report_log.get("girl orgasms", 0)+2))+20, the_person.arousal - the_person.max_arousal - 1))

        report_log["guy orgasms"] = report_log.get("guy orgasms",0) + start_mc_orgasm
        mc.condom = False
        mc.recently_orgasmed = False

        #TODO determine if we want to offer an affair from this
    # if affair_ask_after and private and ask_girlfriend_requirement(the_person) is True and not the_person.relationship == "Single":
    #     if the_person.love >= 60 and the_person.sluttiness >= 30 - (the_person.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
    #         call affair_check(the_person, report_log) from _call_affair_check_bugfix

        update_person_sex_record(the_person, report_log)
        the_goal = None
        sex_path = None
        current_node = None
        reset_sex_goal(the_person)
    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

# use as wrapper for get_fucked to satisfy mc requests, by building a custom sex path to fullfill request
# for now only supports 'blowjob' and 'titfuck'
label mc_sex_request(the_person, the_request = "blowjob", private = True):
    python:
        if the_request == "titfuck":
            path = build_titfuck_path(the_person)
            start_object = mc.location.get_object_with_trait("Kneel")
        else:   # default blowjob
            path = build_blowjob_path(the_person)
            start_object = mc.location.get_object_with_trait("Kneel")

    call get_fucked(the_person, sex_path = path, private = private, start_object = start_object, skip_intro = True, ignore_taboo = True, allow_continue = False) from _call_get_fucked_mc_request
    $ the_report = _return
    python:
        path = None
        start_object = None
    return the_report

label remove_condom_go_raw(the_person, the_position):
    the_person "Hang on a second..."
    "[the_person.title] slowly pulls off your cock. You feel her give you a couple strokes with her hand."
    "She slowly pulls the condom off your cock."
    mc.name "[the_person.title]?"
    the_person "Sssshhh... I need to feel it... inside me..."
    "[the_person.possessive_title] slowly sinks back down onto your shaft, raw this time."
    $ the_person.change_arousal(5)
    $ mc.change_arousal(5)
    "The heat from her body translates perfectly now that you have that piece of latex between you removed. It feels wonderful."
    return

init 100 python:
    def GIC_unit_test(count = 1):#Count is the number of times we repeat the unit test.
        unit_test_count = 0
        while unit_test_count < count:
            mc.change_location(bedroom)
            the_person = renpy.random.choice(known_people_in_the_game())
            the_person.love = renpy.random.randint(-50,50)
            the_person.sluttiness = renpy.random.randint(60,120)
            mc.energy = mc.max_energy
            the_person.energy = the_person.max_energy
            renpy.call("get_fucked", the_person, unit_test = True, the_goal = renpy.random.choice(list_of_all_dom_sex_goals))
            unit_test_count += 1

    def GIC_unit_test_2(count = 1):#Count is the number of times we repeat the unit test.
        unit_test_count = 0
        while unit_test_count < count:
            mc.change_location(bedroom)
            the_person = renpy.random.choice(known_people_in_the_game())
            the_person.love = -50
            the_person.sluttiness = renpy.random.randint(60,120)
            mc.energy = mc.max_energy
            the_person.energy = the_person.max_energy
            renpy.call("get_fucked", the_person, unit_test = True)
            unit_test_count += 1

#############################################################
# Generic Outro GIC statement
# Copy past this into a new sex position outro to give easy access to all possible goals.

# if the_goal == "get off":
#     pass
# elif the_goal == "waste cum":
#     pass
# elif the_goal == "hate fuck":
#     pass
# elif the_goal == "vaginal creampie":
#     pass
# elif the_goal == "anal creampie":
#     pass
# elif the_goal == "facial":
#     pass
# elif the_goal == "body shot":
#     pass
# elif the_goal == "get mc off":
#     pass
# elif the_goal == "oral creampie":
#     pass
# else:
#     pass
############################################
