# GENERIC LIST OF ROLES AND ACTIONS ASSOCIATED WITH THAT ROLE
init -1 python:
    def always_true(the_person):
        return True

    def get_employee_role_actions():
        #EMPLOYEE ACTIONS#
        employee_duty_set_action = Action("Set her work duties", employee_set_duties_requirement, "employee_set_duties_label",
            menu_tooltip = "Review and set her work duties.")
        move_employee_action = Action("Move her to a new division", move_employee_requirement, "move_employee_label",
            menu_tooltip = "Move her to a new division, where her skills might be put to better use.")
        employee_complement_action = Action("Compliment her work", employee_complement_requirement, "employee_complement_work",
            menu_tooltip = "Offer a few kind words about her performance at work. Increases happiness and love, dependent on your charisma.")
        employee_insult_action = Action("Insult her work", employee_insult_requirement, "insult_recent_work",
            menu_tooltip = "Offer a few choice words about her performance at work. Lowers love and happiness, but is good for instilling obedience.")
        employee_pay_cash_action = Action("Pay her a cash bonus", employee_pay_cash_requirement, "employee_pay_cash_bonus",
            menu_tooltip = "A bonus in cold hard cash is good for obedience and happiness. The larger the reward the greater the effect.")
        employee_performance_review = Action("Start a performance review {image=gui/heart/Time_Advance.png}", employee_performance_review_requirement , "employee_performance_review",
            menu_tooltip = "Bring her to your office for a performance review. Get her opinion about her job, reward, punish, or fire her as you see fit. Can only be done once every seven days.")
        employee_punishment = Action("Punish her", employee_punishment_hub_requirement, "employee_punishment_hub",
            menu_tooltip = "Punish her for any violations of company policy.", priority = 5)
        employee_find_out_home_location_action = Action("{image=home_marker} Have a personal chat", employee_find_out_home_location_requirement, "employee_find_out_home_location_label",
            menu_tooltip = "Have a chat with an employee and find our more about her, including her home address.")

        return [employee_duty_set_action, employee_complement_action, employee_insult_action, employee_pay_cash_action, employee_performance_review, move_employee_action, employee_punishment, employee_find_out_home_location_action]

    def get_head_researcher_actions():
        #HEAD RESEARCHER ACTIONS#
        improved_serum_unlock = Action("Ask about advancing your research", improved_serum_unlock_requirement, "improved_serum_unlock_label",
            menu_tooltip = "Your basic initial research can only take you so far. You will need a breakthrough to discover new serum traits.", priority = 10)

        visit_nora_intro = Action("Visit Nora to try and advance your research", visit_nora_intro_requirement, "nora_intro_label",
            menu_tooltip = "Have your head researcher reach out to your old mentor to see if she can help advance your research.", priority = 10)

        advanced_serum_unlock_stage_1 = Action("Ask about advancing your research", advanced_serum_stage_1_requirement, "advanced_serum_stage_1_label",
            menu_tooltip = "Another breakthrough will unlock new serum traits.", priority = 10)

        advanced_serum_unlock_stage_3 = Action("Present with recording of prototype serum test", advanced_serum_stage_3_requirement, "advanced_serum_stage_3_label",
            menu_tooltip = "Your new head researcher will have to take over now, and this recording should help them.", priority = 10)

        futuristic_serum_unlock_stage_1 = Action("Ask about advancing your research", futuristic_serum_stage_1_requirement, "futuristic_serum_stage_1_label",
            menu_tooltip = "You will need another breakthrough to unlock new serum traits.", priority = 10) #First time you ask about it

        futuristic_serum_unlock_stage_2 = Action("Talk about the test subjects", futuristic_serum_stage_2_requirement, "futuristic_serum_stage_2_label",
            menu_tooltip = "Your head researcher needs willing, dedicated test subjects to advance your research any further.", priority = 10) #Talk to her to either select test subjects or get a refresher on what you need.

        fire_head_researcher_action = Action("Remove her as head researcher", fire_head_researcher_requirement, "fire_head_researcher",
            menu_tooltip = "Remove her as your head researcher so you can select another. Without a head researcher your R&D department will be less efficient.")

        head_researcher_serum_trait_test_action = Action("Test a Serum Trait {image=gui/heart/Time_Advance.png}", head_researcher_serum_trait_test_requirement, "head_researcher_serum_trait_test_label",
            menu_tooltip = "Perform intensive serum trait test with the help of your head researcher on an employee.", priority = 5)

        fetish_serum_discuss_action = Action("Discuss Nanobot Program", fetish_serum_discuss_requirement, "fetish_serum_discuss_label",
            menu_tooltip = "Discuss creation / status of the Nanobot program.", priority = 5)

        return [fire_head_researcher_action,improved_serum_unlock,advanced_serum_unlock_stage_1, visit_nora_intro, advanced_serum_unlock_stage_3,futuristic_serum_unlock_stage_1, futuristic_serum_unlock_stage_2, head_researcher_serum_trait_test_action, fetish_serum_discuss_action]

    def get_company_model_role_actions():
        #MODEL ACTIONS#
        model_ad_photo_list = Action("Shoot pictures for an advertisement {image=gui/heart/Time_Advance.png}", model_photography_list_requirement, "model_photography_list_label", priority = 5)

        fire_model_action = Action("Remove her as your company model", fire_model_requirment, "fire_model_label",
            menu_tooltip = "Remove her as your company model so you can give the position to someone else. Effects from existing ad campaigns will continue until they expire.")

        return [model_ad_photo_list, fire_model_action]

    def get_girlfriend_role_actions():
        ask_break_up_action = Action("Break up with her", ask_break_up_requirement, "ask_break_up_label", menu_tooltip = "Breaking up may break her heart, but it'll be easier on her than catching you with another woman.")
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        girlfriend_sleepover_action = Action("Arrange a sleepover", girlfriend_myplace_yourplace_requirement, "girlfriend_myplace_yourplace_label", menu_tooltip = "Ask your girlfriend if she wants to sleep together tonight.")
        girlfriend_underwear_shopping_action = Action("Shop for new lingerie {image=gui/heart/Time_Advance.png}", girlfriend_underwear_shopping_requirement , "girlfriend_underwear_shopping_label", menu_tooltip = "Take your girlfriend out to shop for some exciting underwear to wear for you.")
        girlfriend_quit_dikdok_action = Action("Quit DikDok", girlfriend_quit_dikdok_requirement, "girlfriend_quit_dikdok_label", menu_tooltip = "Ask your girlfriend to stop showing herself off on DikDok.")

        return [ask_break_up_action, ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, girlfriend_sleepover_action, girlfriend_underwear_shopping_action, girlfriend_quit_dikdok_action]

    def get_girlfriend_role_dates():
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        return [plan_fuck_date_action, girlfriend_shopping_date]

    def get_paramour_role_actions():
        ask_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", girlfriend_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        ask_leave_SO_action = Action("Ask her to leave her significant other for you", ask_leave_SO_requirement, "ask_leave_SO_label", menu_tooltip = "This affair has been secret long enough! Ask her to leave her significant other and make your relationship official.")

        return [ask_get_boobjob_action, girlfriend_ask_trim_pubes_action, ask_leave_SO_action]

    def get_paramour_role_dates():
        plan_fuck_date_action = Action("Plan a fuck date at her place", fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        return [plan_fuck_date_action]

    def get_unemployed_role_actions():
        unemployed_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "unemployed_offer_hire")
        return [unemployed_hire_action]

    def get_unimportant_job_role_actions():
        unimportant_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "unimportant_job_offer_hire")
        return [unimportant_hire_action]

    def get_stripper_role_actions():
        stripper_dance_action = Action("Ask for a private dance\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}", stripper_private_dance_requirement, "stripper_private_dance_label",
            menu_tooltip = "Ask her to a back room for a private dance.")
        stripper_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "stripper_offer_hire")

        return [stripper_dance_action, stripper_hire_action]

    def get_prostitute_role_actions():
        prostitute_action = Action("Pay her for sex\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}", prostitute_requirement, "prostitute_label",
            menu_tooltip = "You know she's a prostitute, pay her to have sex with you.")
        prostitute_hire_action = Action("Offer to hire her", offer_to_hire_requirement, "prostitute_hire_offer")
        return [prostitute_action, prostitute_hire_action]

    def get_freeuse_actions():
        #EMPLOYEE FREEUSE ACTIONS#
        freeuse_fuck = Action("Fuck her", freeuse_fuck_requirement, "employee_freeuse_fuck", menu_tooltip = "Grab your free use slut and have some fun with her.")
        return [freeuse_fuck]

    def get_trance_role_actions():
        trance_training_action = Action("Take advantage of her trance", trance_train_requirement, "trance_train_label", menu_tooltip = "Take advantage of her orgasm-induced trance and make some changes while she is highly suggestible.")
        return [trance_training_action]

    def get_lactating_serum_role_actions():
        milk_for_serum_action = Action("Milk her for serum\n{color=#ff0000}{size=18}Costs: 15 {image=gui/extra_images/energy_token.png}{/size}{/color}", milk_for_serum_requirement, "milk_for_serum_label", menu_tooltip = "Those tits contain company property!")
        return [milk_for_serum_action]

    def get_hypno_orgasm_role_orgasm_actions():
        hypno_trigger_orgasm_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_orgasm", menu_tooltip = "You've implanted a trigger word. You can make her cum whenever you want.")
        return [hypno_trigger_orgasm_action]

    def get_hypno_orgasm_role_online_actions():
        hypno_trigger_online_action = Action("Trigger an orgasm", hypno_trigger_orgasm_requirement, "hypno_trigger_online", menu_tooltip = "You've implanted a trigger word, it should work over a text message.")
        return [hypno_trigger_online_action]

    def get_harem_role_actions():
        ask_harem_move_to_mansion_action = Action("Move into Harem Mansion", harem_move_to_mansion_requirement, "harem_move_to_mansion_label", menu_tooltip = "Ask her to leave her current residence and move into your Harem Mansion.", priority = 10)
        ask_harem_break_up_action = Action("Break up with her", harem_break_up_requirement, "leave_harem_label", menu_tooltip = "Rip out her heart and stomp on it, will remove her from the Polyamory.")
        ask_harem_get_boobjob_action = Action("Ask her to get a boob job\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}", harem_ask_get_boobjob_requirement, "ask_get_boobjob_label", menu_tooltip = "A little silicone goes a long way. Ask her to get breast enhancement surgery for you.")
        girlfriend_ask_trim_pubes_action = Action("Ask her to trim her pubes", harem_ask_trim_pubes_requirement, "girlfriend_ask_trim_pubes_label", menu_tooltip = "Ask her to do a little personal landscaping. Tell her to wax it off, grow it out, or shape it into anything in between.")
        return [ask_harem_move_to_mansion_action, ask_harem_get_boobjob_action, girlfriend_ask_trim_pubes_action, ask_harem_break_up_action]

    def get_harem_role_dates():
        plan_fuck_date_action = Action("Plan a fuck date at her place", harem_fuck_date_requirement, "plan_fuck_date_label", menu_tooltip = "Pick a night to go over there and spend nothing but \"quality time\" with each other.")
        girlfriend_shopping_date = Action("Go shopping together {image=gui/heart/Time_Advance.png}", shopping_date_requirement, "shopping_date_intro", menu_tooltip = "Take her to the mall and do some shopping together.")
        return [plan_fuck_date_action, girlfriend_shopping_date]


label instantiate_roles(): #This section instantiates all of the key roles in the game. It is placed here to ensure it is properly created, saved, ect. by Renpy.
    #All of the role labels and requirements are defined in their own file, but their Action representations are stored here for saving purposes.
    python:

        employee_role = Role("Employee", get_employee_role_actions(),
            on_turn = employee_on_turn, on_move = employee_on_move, on_day = employee_on_day, hidden = True)

        #EMPLOYEE BUSYWORK ACTIONS#
        employee_busywork_role = Role("Office Busywork", [], hidden = True) #TODO: Add some other actions to this role
        employee_role.link_role(employee_busywork_role) #Link this role to the employee_role, so they are removed at the same time.

        #EMPLOYEE HUMILIATING WORK ACTIONS#
        employee_humiliating_work_role = Role("Humiliating Office Work", [], hidden = True) #TODO: Add some other actions to this role.
        employee_role.link_role(employee_humiliating_work_role)

        employee_freeuse_role = Role("Freeuse Slut", get_freeuse_actions(), hidden = True)
        employee_role.link_role(employee_freeuse_role)

        head_researcher = Role("Head Researcher", get_head_researcher_actions())

        company_model_role = Role("Model", get_company_model_role_actions())

        #GENERIC STUDENT
        generic_student_role = Role("Student", [], hidden = True)
        college_intern_role = Role("College Intern", actions = [college_intern_training, college_intern_duty_set_action], hidden = True, on_turn = college_intern_on_turn, on_move = college_intern_on_move, on_day = college_intern_on_day, looks_like = generic_student_role)

        ################
        #INTERNET ROLES#
        ################
        #These roles are given to any girl who has an account on the particular site, even if you don't know about it.

        instapic_role = Role("On InstaPic", [], hidden = True, on_turn = insta_on_turn, on_day = insta_on_day)

        dikdok_role = Role("On Dikdok", [], hidden = True, on_turn = dikdok_on_turn, on_day = dikdok_on_day)

        onlyfans_role = Role("On OnlyFanatics", [], hidden = True, on_turn = onlyfans_on_turn, on_day = onlyfans_on_day)

        ####################
        #RELATIONSHIP ROLES#
        ####################

        #GIRLFRIEND ACTIONS#
        # Give her gifts (bonus happiness + Love)
        # She tests serum for you for free.
        # Go on dates (Remove this option from the normal chat menu?)
        # If she has (of age) kids, meet them (and, amazingly, they're hot young women!)

        #Other things to add#
        # Enables new girlfriend specific crises.
        # Adds more love to seduction attempts (reduce love from other sources)
        # Fallout if your girlfriend catches you with someone else.


        girlfriend_role = Role("Girlfriend", get_girlfriend_role_actions(), role_dates = get_girlfriend_role_dates()) #Your girlfriend, and she's not in a relationship with anyone else
        #Getting married is some kind of victory for the game?


        #affair ACTIONS
        # Sneaky versions of all of the normal girlfriend stuff
        # Have her get money from her (b/f/h) and give it to you.
        # Convince her to leave her (boyfriend/fiance/husband) for you. Changes to her being your girlfriend.
        # Start to blackmail her for money or sex.

        affair_role = Role("Paramour", get_paramour_role_actions(), role_dates = get_paramour_role_dates()) #A woman who is in a relationship but also wants to fuck you because of love (rather than pure sluttiness, where she thinks that's normal)


        ###################
        ### TRANCE ROLE ###
        ###################

        trance_role = Role("In a Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day)
        heavy_trance_role = Role("In a Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = trance_role)
        very_heavy_trance_role = Role("In a Very Deep Trance", actions = get_trance_role_actions(), on_turn = trance_on_turn, on_day = trance_on_day, looks_like = heavy_trance_role)

        #######################
        ### TRAINABLE ROLES ###
        #######################

        hypno_orgasm_role = Role("Hypno Orgasm", actions = get_hypno_orgasm_role_orgasm_actions(), hidden = True, on_turn = hypno_orgasm_on_turn, internet_actions = get_hypno_orgasm_role_online_actions())

        ###################
        ### OTHER ROLES ###
        ###################
        unemployed_role = Role("Unemployed", get_unemployed_role_actions(), hidden = True)
        unimportant_job_role = Role("Unimportant Job", get_unimportant_job_role_actions(), hidden = True) # Used for roles where it is relatively simple to get the character to quit their job.
        critical_job_role = Role("Critical Job", [], hidden = True) # Used for role where it is impossible to get the character to quit their job, but they don't have anything else going on.
        stripper_role = Role("Stripper", get_stripper_role_actions(), hidden = True)

        prostitute_role = Role("Prostitute", get_prostitute_role_actions(), hidden = True)
        pregnant_role = Role("Pregnant", [], hidden = True)
        lactating_serum_role = Role("Lactating Serum", get_lactating_serum_role_actions(), hidden = True, on_turn = lactating_serum_on_turn, on_day = lactating_serum_on_day)

        harem_role = Role("Girlfriend in Polyamory", get_harem_role_actions(), role_dates = get_harem_role_dates(), looks_like = girlfriend_role)
    return
