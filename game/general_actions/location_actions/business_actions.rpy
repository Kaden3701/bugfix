init 0 python:
    def cheat_requirement():
        return debugMode

    def sleep_action_requirement():
        if time_of_day != 4:
            return "Too early to sleep"
        else:
            return True

    def faq_action_requirement():
        return True

    def hr_work_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def research_work_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.active_research_design is None:
            return "No research project set"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def supplies_work_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def market_work_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def production_work_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.used_line_weight == 0:
            return "No serum design set"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def interview_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.employee_count >= mc.business.max_employee_count:
            return "At employee limit"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def serum_design_action_requirement():
        if time_of_day >= 4:
            return "Too late to work"
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        else:
            return True

    def research_select_action_requirement():
        return True

    def production_select_action_requirement():
        return True

    def trade_serum_action_requirement():
        return True

    def sell_serum_action_requirement():
        return True

    def pick_supply_goal_action_requirement():
        return True

    def policy_purchase_requirement():
        return True

    def head_researcher_select_requirement():
        if mc.business.head_researcher is not None:
            return False
        elif __builtin__.len(mc.business.research_team) == 0:
            return "Nobody to pick"
        else:
            return True

    def pick_company_model_requirement():
        if mc.business.company_model is not None:
            return False
        elif not public_advertising_license_policy.is_active:
            return False
        elif mc.business.employee_count == 0:
            return "Nobody to pick"
        else:
            return True

    def set_uniform_requirement():
        return strict_uniform_policy.is_active

    def set_serum_requirement():
        if daily_serum_dosage_policy.is_owned and not daily_serum_dosage_policy.is_active:
            return "Policy not active"
        else:
            return daily_serum_dosage_policy.is_active

    def review_designs_action_requirement():
        return True

    def mc_breakthrough_requirement(new_level, clarity_cost):
        if mc.business.research_tier+1 != new_level:
            return False
        elif clarity_cost > mc.free_clarity:
            return "Not enough Clarity."
        elif mc.business.event_triggers_dict.get("Tutorial_Section", False):
            return "Finish tutorial first"
        elif time_of_day >= 4:
            return "Too late to work."
        else:
            return True

    def get_candidate_count_costs():
        interview_cost = mc.business.recruitment_cost
        count = 3 #Num of people to generate, by default is 3. Changed with some policies
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                count += recruitment_policy.extra_data.get("recruitment_batch_adjust",0)
                interview_cost +=  recruitment_policy.extra_data.get("interview_cost_adjust",0)

        return count, interview_cost

    def interview_build_candidates_list(count):
        start_time = time.time()
        candidates = []
        for x in __builtin__.range(0, count): #NOTE: count is given +1 because the screen tries to pre-calculate the result of button presses. This leads to index out-of-bounds, unless we pad it with an extra character (who will not be reached).
            candidates.append(make_person(**(mc.business.generate_candidate_requirements())))

        reveal_count = 0
        reveal_sex = False

        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_count += recruitment_policy.extra_data.get("reveal_count_adjust",0)
                reveal_sex = reveal_sex or recruitment_policy.extra_data.get("reveal_sex_opinion",False)

        for a_candidate in candidates:
            for x in __builtin__.range(0,reveal_count): #Reveal all of their opinions based on our policies.
                a_candidate.discover_opinion(a_candidate.get_random_opinion(include_known = False, include_sexy = reveal_sex),add_to_log = False) #Get a random opinion and reveal it.

            # new candidate could be pregnant
            if persistent.pregnancy_pref > 0:
                if a_candidate.age > 21 and renpy.random.randint(0,100) < (58 - a_candidate.age) // 5: # chance she is already pregnant decreases with age
                    #Can hire her up to 10 days from due date. Probably not hiring anyone a week from due!
                    become_pregnant(a_candidate, mc_father = False, progress_days = renpy.random.randint(5,80))
                    #renpy.say("Pregnant", "Candidate: " + a_candidate.name + " " + a_candidate.last_name + " is pregnant.")

        add_to_debug_log("Candidates (" + str(count) + "): {total_time:.3f}", start_time)
        return candidates


label sleep_action_description:
    if mc.business.is_weekend:
        "You go to bed after a nice day."
    else:
        "You go to bed after a hard days work."
    call advance_time() from _call_advance_time
    return

label faq_action_description:
    call faq_loop() from _call_faq_loop_1
    return

label hr_work_action_description:
    $ mc.business.player_hr()
    call advance_time() from _call_advance_time_1
    return

label research_work_action_description:
    $ mc.business.player_research()
    call advance_time() from _call_advance_time_2
    return

label supplies_work_action_description:
    $ mc.business.player_buy_supplies()
    call advance_time() from _call_advance_time_3
    return

label market_work_action_description:
    $ mc.business.player_market()
    call advance_time() from _call_advance_time_4
    return

label production_work_action_description:
    $ mc.business.player_production()
    call advance_time() from _call_advance_time_5
    return

label interview_action_description:
    $ count, interview_cost = get_candidate_count_costs()

    "Bringing in [count] people for an interview will cost $[interview_cost]. Do you want to spend time interviewing potential employees?"
    menu:
        "Yes, I'll pay the cost\n{color=#ff0000}{size=18}Costs: $[interview_cost]{/size}{/color}":
            $ mc.business.change_funds(-interview_cost)
            $ clear_scene()

            $ candidates = interview_build_candidates_list(count)

            # pad with one extra element, to make sure we can see all candidates
            call hire_select_process(candidates + [1]) from _call_hire_select_process_interview_action_enhanced

            if not _return == "None":
                $ new_person = _return
                $ new_person.generate_home() #Generate them a home location so they have somewhere to go at night.
                $ candidates.remove(new_person)

                call hire_someone(new_person, add_to_location = True) from _call_hire_someone_interview_action_enhanced
                $ new_person.set_title(new_person.get_random_title())
                $ new_person.set_possessive_title(new_person.get_random_possessive_title())
                $ new_person.set_mc_title(new_person.get_random_player_title())
                $ del new_person
            else:
                "You decide against hiring anyone new for now."

            # cleanup not used candidates
            python:
                if persistent.keep_patreon_characters:
                    for person in candidates:
                        if person.type == "unique": # preserve Patreon unique characters.
                            person.generate_home()
                            person.home.add_person(person)
                        else:
                            person.remove_person_from_game()

                candidates.clear() #Prevent it from using up extra memory
                person = None
                clean_memory() # extra memory cleanup after interview screen

            call advance_time from _call_advance_time_interview_action_enhanced
        "Never mind":
            pass
    return

label hire_select_process(candidates):
    hide screen main_ui #NOTE: We have to hide all of these screens because we are using a fake (aka. non-screen) background for this. We're doing that so we can use the normal draw_person call for them.
    hide screen phone_hud_ui
    hide screen business_ui
    hide screen goal_hud_ui
    $ show_candidate(candidates[0]) #Show the first candidate, updates are taken care of by actions within the screen.
    show bg paper_menu_background #Show a paper background for this scene.
    $ count = __builtin__.len(candidates)-1
    call screen interview_ui(candidates,count)
    $ renpy.scene()
    show screen phone_hud_ui
    show screen business_ui
    show screen goal_hud_ui
    show screen main_ui
    $ clear_scene()
    $ mc.location.show_background()

    return _return


label hire_someone(new_person, add_to_location = False, research_allowed = True, production_allowed = True, supply_allowed = True, marketing_allowed = True, hr_allowed = True): # Breaks out some of the functionality of hiring someone into an independent lable.
    "You complete the necessary paperwork and hire [new_person.name]. What division do you assign them to?"
    menu:
        "Research and Development" if research_allowed:
            $ mc.business.add_employee_research(new_person)
            if add_to_location:
                $ mc.business.r_div.add_person(new_person)

        "Production" if production_allowed:
            $ mc.business.add_employee_production(new_person)
            if add_to_location:
                $ mc.business.p_div.add_person(new_person)

        "Supply Procurement" if supply_allowed:
            $ mc.business.add_employee_supply(new_person)
            if add_to_location:
                $ mc.business.s_div.add_person(new_person)

        "Marketing" if marketing_allowed:
            $ mc.business.add_employee_marketing(new_person)
            if add_to_location:
                $ mc.business.m_div.add_person(new_person)

        "Human Resources" if hr_allowed:
            $ mc.business.add_employee_hr(new_person)
            if add_to_location:
                $ mc.business.h_div.add_person(new_person)

    call set_duties_controller(new_person) from _call_set_duties_controller_hire_someone
    if _return:
        $ new_person.event_triggers_dict["work_duties_last_set"] = day
    return

label serum_design_action_description:
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    call screen serum_design_ui(SerumDesign(),[]) #This will return the final serum design, or None if the player backs out.
    $ the_serum = _return

    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    if not the_serum == "None":
        $ name = renpy.input("Please give this serum design a name.")
        $ the_serum.name = name.replace("[", "[[")
        $ mc.business.add_serum_design(the_serum)
        $ mc.business.listener_system.fire_event("new_serum", the_serum = the_serum)
        $ the_serum = None
        call advance_time() from _call_advance_time_7
    else:
        "You decide not to spend any time designing a new serum type."
    return

label research_select_action_description:
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    call screen research_select_ui
    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return

label cheat:
    $ mc.free_stat_points += 4 + 7 + 7
    $ mc.free_work_points += 8 *5
    $ mc.free_sex_points += 8 *4 -2 + 5
    $ mc.business.change_funds(100000)
    return

label production_select_action_description: #TODO: Change this to allow you to select which line of serum you are changing!
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    call screen serum_production_select_ui
    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return

label trade_serum_action_description:
    "You step into the stock room to check what you currently have produced."
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    $ renpy.block_rollback()
    call screen serum_trade_ui(mc.inventory,mc.business.inventory)
    $ renpy.block_rollback()
    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return

label sell_serum_action_description:
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    $ renpy.block_rollback()
    # call screen serum_trade_ui(mc.business.inventory,mc.business.sale_inventory,"Production Stockpile","Sales Stockpile")
    call screen serum_sell_ui()
    $ renpy.block_rollback()

    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return

label review_designs_action_description:
    hide screen main_ui
    hide screen phone_hud_ui
    hide screen business_ui
    $ renpy.block_rollback() #Block rollback to prevent any strange issues with references being lost.
    call screen review_designs_screen()
    $ renpy.block_rollback()

    show screen phone_hud_ui
    show screen business_ui
    show screen main_ui
    return


label pick_supply_goal_action_description:
    $ amount = renpy.input("How many units of serum supply would you like your supply procurement team to keep stocked?")
    $ amount = amount.strip()

    while not amount.isdigit():
        $ amount = renpy.input("Please put in an integer value.")

    $ amount = __builtin__.int(amount)
    $ mc.business.supply_goal = amount
    if amount <= 0:
        "You tell your team to keep [amount] units of serum supply stocked. They question your sanity, but otherwise continue with their work. Perhaps you should use a positive number."
    else:
        "You tell your team to keep [amount] units of serum supply stocked."

    return

label policy_purchase_description:
    call screen policy_selection_screen()
    return

label head_researcher_select_description:
    call screen employee_overview(white_list = mc.business.research_team, person_select = True)
    $ new_head = _return
    $ mc.business.head_researcher = new_head
    $ new_head.change_job(head_researcher_job)
    $ del new_head
    return

label pick_company_model_description:
    call screen employee_overview(white_list = mc.business.market_team,person_select = True)
    $ new_model = _return
    if new_model is not None:
        $ mc.business.hire_company_model(_return)
    return

label uniform_manager_loop():
    call screen uniform_manager()
    if _return == "Add":
        call outfit_master_manager() from _call_outfit_master_manager_uniform_manager_loop #TODO: Decide if we need to pass this the uniform peramiters, of if we do that purely in what's selectable.
        if isinstance(_return, Outfit):
            $ mc.business.business_uniforms.append(UniformOutfit(_return))
            $ mc.business.listener_system.fire_event("add_uniform", the_outfit = _return)
        jump uniform_manager_loop
    return

label set_serum_description:
    call screen assign_division_serum()
    return

label mc_research_breakthrough(new_level, clarity_cost):
    "You feel an idea in the back of your head. You realise it's been there this whole time, but you've been too distracted to see it."
    "You snatch up the nearest notebook and get to work right away."
    "Within minutes your thoughts are flowing fast and clear. Everything makes sense, and your path forward is made crystal clear."
    $ mc.spend_clarity(clarity_cost)
    $ mc.business.research_tier = new_level
    if new_level == 1:
        $ mc.log_event("Tier 1 Research Unlocked", "float_text_grey")
    elif new_level == 2:
        $ mc.log_event("Tier 2 Research Unlocked", "float_text_grey")
    else:
        $ mc.log_event("Max Research Tier Unlocked", "float_text_grey")
    "You throw your pen down when you're finished. Your new theory is awash in possibilities!"
    "Now you just need to research them in the lab!"
    return
