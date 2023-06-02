init -2 python:
    class Business():
        # main jobs to start with:
        # 1) buying raw supplies.
        # 2) researching new serums.
        # 2a) The player (only) designs new serums to be researched.
        # 3) working in the lab to produce serums.
        # 4) Working in marketing. Increases volume you can sell, and max price you can sell for.
        # 5) Packaging and selling serums that have been produced.
        # 6) General secretary work. Starts at none needed, grows as your company does (requires an "HR", eventually). Maybe a general % effectivness rating.
        def __init__(self, name, m_div, p_div, r_div, s_div, h_div):
            self.name = name
            self.funds = 1000 #Your starting wealth.

            self.bankrupt_days = 0 #How many days you've been bankrupt. If it hits the max value you lose.
            self.max_bankrupt_days = 3 #How many days you can be negative without loosing the game. Can be increased through research.

            self._m_div = m_div.identifier #The physical locations of all of the teams, so you can move to different offices in the future.
            self._p_div = p_div.identifier
            self._r_div = r_div.identifier
            self._s_div = s_div.identifier
            self._h_div = h_div.identifier

            # These wardrobes handle the department specific uniform stuff. A list of UniformOutfits is used to populate the uniform manager screen.
            self.m_uniform = Wardrobe(self.name + " Marketing Wardrobe")
            self.p_uniform = Wardrobe(self.name + " Production Wardrobe")
            self.r_uniform = Wardrobe(self.name + " Research Wardrobe")
            self.s_uniform = Wardrobe(self.name + " Supply Wardrobe")
            self.h_uniform = Wardrobe(self.name + " HR Wardrobe")

            self.business_uniforms = [] #A list of UniformOutfits

            #These are the serums given to the different departments if the daily serum dosage policy is researched.
            self.m_serum = None
            self.p_serum = None
            self.r_serum = None
            self.s_serum = None
            self.h_serum = None

            self.head_researcher = None #A reference to the head researcher is stored here, for use in important events.
            self.company_model = None #A reference to the current company model. May be used for some events.

            self.max_employee_count = 5

            self.supply_count = 0
            self.supply_goal = 250
            self.auto_sell_threshold = None
            self.marketability = 0
            #self.production_points = 0 Use to be used to store partial progress on serum. is now stored in the assembly line array
            self.team_effectiveness_temp = 100 #Used as a temporary store to flip-flop the value at the start of the turn for HR puprposes.
            self.team_effectiveness = 100 #Ranges from 50 (Chaotic, everyone functions at 50% speed) to 200 (masterfully organized). Normal levels are 100, special traits needed to raise it higher.
            self.effectiveness_cap = 100 #Max cap, can be raised.

            self.research_tier = 0 #The tier of research the main character has unlocked with storyline events. 0 is starting, 3 is max.
            self.max_serum_tier = 0 #The tier of serum you can produce in your lab. Mirrors research tiers.

            self.blueprinted_traits = [] #List of traits that we have built from trait blueprints.

            self.serum_designs = [] #Holds serum designs that you have researched.
            self.active_research_design = None #The current research (serum design or serum trait) the business is working on

            self.batch_size = 5 #How many serums are produced in each production batch

            self.recruitment_cost = 50

            self.inventory = SerumInventory()
            # Production lines now have their own class.
            self.production_lines = [] #Holds instances of Production Line. Default is 2, buying more production lines let's you produce serum designs in parallel (but no more than your default amount).
            self.production_lines.append(ProductionLine(self.inventory))
            self.production_lines.append(ProductionLine(self.inventory))

            self.max_active_contracts = 2
            self.active_contracts = []

            self.max_offered_contracts = 2
            self.offered_contracts = []

            # self.policy_list = [] #This is a list of Policy objects.
            # self.active_policy_list = [] #This is a list of currently active policies (vs just owned ones)

            self.message_list = [] #This list of strings is shown at the end of each day on the business update screen. Cleared each day.
            self.counted_message_list = {} #This is a dict holding the count of each message stored in it. Used when you want to have a message that is counted and the total shown at the end of the day.
            self.production_potential = 0 #How many production points the team was capable of
            self.supplies_purchased = 0
            self.production_used = 0 #How many production points were actually used to make something.
            self.research_produced = 0 #How much research the team produced today.
            self.sales_made = 0
            self.serums_sold = 0

            self.partial_clarity = 0.0 #Float used to store partial clarity produced by research until it can be given out as a full integer.

            self.sales_multipliers = [] #This list holds ["Source_type",multiplier_as_float]. The multiplier is applied to the value of serums when they are sold.
            # Only the most positive modifier of any source type is used. (This means a 1.0 modifier can be used to replace a negative modifier).


            self.mandatory_crises_list = ActionList() #A list of crises to be resolved at the end of the turn, generally generated by events that have taken place.
            self.mandatory_morning_crises_list = ActionList() #A list of specifically morning crises that need to be resolved.

            self.event_triggers_dict = {} #This dictionary will be used to hold flags for story events and triggers. In general a string is the key and a bool is the value stored.
            self.event_triggers_dict["policy_tutorial"] = 1 #We have a policy tutorial.
            self.event_triggers_dict["research_tutorial"] = 1 #We have a research tutorial.
            self.event_triggers_dict["design_tutorial"] = 1 #We have a serum design tutorial.
            self.event_triggers_dict["production_tutorial"] = 1 #We have a production tutorial.
            self.event_triggers_dict["outfit_tutorial"] = 1 #We have an outfit design tutorial.
            self.event_triggers_dict["hiring_tutorial"] = 1 #We have an outfit design tutorial.

            self.market_reach = 100 #"market_reach" can be thought of as your total customer base.
            self.mental_aspect_sold = 0 #Customers only have so much need for serum, so as you sell aspects the price per aspect goes down. You need to increase your market reach to get that price back up.
            self.physical_aspect_sold = 0
            self.sexual_aspect_sold = 0
            self.medical_aspect_sold = 0

            self.default_aspect_price = 10 # THis is the starting price that most aspects are "worth".
            self.aspect_price_max_variance = 8 # This is the total amount each aspect can be worth (ie no aspect is ever worth base more than 18 or less than 2).
            self.aspect_price_daily_variance = 2 #This is the +- amount the price of each aspect can fluctuate.

            self.mental_aspect_price = self.default_aspect_price #These are the actual current values of each aspect, which will vary from day to day
            self.physical_aspect_price = self.default_aspect_price
            self.sexual_aspect_price = self.default_aspect_price
            self.medical_aspect_price = self.default_aspect_price

            self.flaws_aspect_cost = -10 #NOTE: Flaws are a flat -10 each, _not_ reduced by amount sold.

            self.attention = 0 #Current attention.
            self.max_attention = 100 #If you end the day over this much attention you trigger a high attention event.
            self.attention_bleed = 10 #How much attention is burned each day,

            self.operating_costs = 0 #How much money is spent every work day just owning your lab.
            self.standard_efficiency_drop = 1 #How much efficiency drops per employee per turn at work.

            self.listener_system = ListenerManagementSystem()

            self._active_policy_list = MappedList(Policy, all_policies_in_the_game)
            self._policy_list = MappedList(Policy, all_policies_in_the_game)
            self._active_IT_project_map = MappedList(IT_Project, all_IT_projects)
            self._IT_project_map = MappedList(IT_Project, all_IT_projects)
            self._partial_IT_projects = {}
            self._current_IT_project = None
            self._head_researcher = None
            self._hr_director = None
            self._it_director = None
            self._prod_assistant = None
            self._company_model = None
            self._research_team = MappedList(Person, all_people_in_the_game)
            self._market_team = MappedList(Person, all_people_in_the_game)
            self._supply_team = MappedList(Person, all_people_in_the_game)
            self._production_team = MappedList(Person, all_people_in_the_game)
            self._hr_team = MappedList(Person, all_people_in_the_game)
            self._funds_yesterday = self.funds
            self._unisex_restroom_unlocks = {}
            self._stripper_wardrobe = stripclub_wardrobe
            self._waitress_wardrobe = waitress_wardrobe
            self._bdsm_wardrobe = BDSM_performer_wardrobe
            self._manager_wardrobe = manager_wardrobe
            self._mistress_wardrobe = mistress_wardrobe
            self._college_interns_research = MappedList(Person, all_people_in_the_game)
            self._college_interns_production = MappedList(Person, all_people_in_the_game)
            self._college_interns_market = MappedList(Person, all_people_in_the_game)
            self._college_interns_supply = MappedList(Person, all_people_in_the_game)
            self._college_interns_HR = MappedList(Person, all_people_in_the_game)
            self._college_interns_unlocked = False
            self._max_interns_by_division = 3


        @property
        def active_policy_list(self):
            return self._active_policy_list

        @property
        def policy_list(self):
            return self._policy_list

        @property
        def active_IT_projects(self):
            return self._active_IT_project_map

        @property
        def IT_projects(self):
            return self._IT_project_map

        @property
        def IT_partial_projects(self):
            return self._partial_IT_projects

        @property
        def current_IT_project(self):
            return self._current_IT_project

        @current_IT_project.setter
        def current_IT_project(self, value):
            self._current_IT_project = value

        def IT_increase_project_progress(self, amount = 0, add_to_log = False):
            if not self.current_IT_project:
                return
            self.current_IT_project[1] += amount
            if add_to_log:
                mc.log_event( "+" + str(amount) + " IT Project Progress", "float_text_green")
            if self.current_IT_project[1] >= self.current_IT_project[0].project_cost:
                self.IT_unlock_project(self.current_IT_project[0])
                self.current_IT_project = None
                self.add_mandatory_crisis(IT_project_complete_action)
            return

        def IT_unlock_project(self, project = None, add_to_log = True):
            if project and project not in self.IT_projects:
                self.IT_projects.append(project)
                project.apply_policy()  # enable project at completion

                if add_to_log:
                    mc.log_event(project.name + " IT Project Complete!", "float_text_green")
            return

        def IT_project_is_active(self, project):
            return project in self.active_IT_projects

        @property
        def m_div(self):
            return next((x for x in list_of_places if x.identifier == self._m_div), None)

        @property
        def p_div(self):
            return next((x for x in list_of_places if x.identifier == self._p_div), None)

        @property
        def r_div(self):
            return next((x for x in list_of_places if x.identifier == self._r_div), None)

        @property
        def s_div(self):
            return next((x for x in list_of_places if x.identifier == self._s_div), None)

        @property
        def h_div(self):
            return next((x for x in list_of_places if x.identifier == self._h_div), None)

        @property
        def head_researcher(self):
            return Person.get_person_by_identifier(self._head_researcher)

        @head_researcher.setter
        def head_researcher(self, value):
            self._head_researcher = None
            if isinstance(value, Person):
                self._head_researcher = value.identifier

        @property
        def hr_director(self):
            return Person.get_person_by_identifier(self._hr_director)

        @hr_director.setter
        def hr_director(self, value):
            self._hr_director = None
            if isinstance(value, Person):
                self._hr_director = value.identifier

        @property
        def it_director(self):
            return Person.get_person_by_identifier(self._it_director)

        @it_director.setter
        def it_director(self, value):
            self._it_director = None
            if isinstance(value, Person):
                self._it_director = value.identifier

        @property
        def prod_assistant(self):
            return Person.get_person_by_identifier(self._prod_assistant)

        @prod_assistant.setter
        def prod_assistant(self, value):
            self._prod_assistant = None
            if isinstance(value, Person):
                self._prod_assistant = value.identifier

        @property
        def company_model(self):
            return Person.get_person_by_identifier(self._company_model)

        @company_model.setter
        def company_model(self, value):
            if isinstance(value, Person):
                self._company_model = value.identifier
            else:
                self._company_model = None

        @property
        def research_team(self):
            return self._research_team

        @property
        def market_team(self):
            return self._market_team

        @property
        def supply_team(self):
            return self._supply_team

        @property
        def production_team(self):
            return self._production_team

        @property
        def hr_team(self):
            return self._hr_team

        @property
        def funds_yesterday(self):
            return self._funds_yesterday

        @funds_yesterday.setter
        def funds_yesterday(self, value):
            self._funds_yesterday = value

        @property
        def unisex_restroom_unlocks(self):
            return self._unisex_restroom_unlocks


        def run_turn(self): #Run each time the time segment changes. Most changes are done here.
            for a_person in self.employee_list:
                if a_person.is_at_work and not a_person.has_duty(extra_paperwork_duty):
                    self.change_team_effectiveness(-self.standard_efficiency_drop) #Last thing we do is figur out what our effectivness drop should be before truncating our temp_value and applying it.
            self.update_team_effectiveness()

            if self.is_open_for_business and self.active_research_design is None:
                self.event_triggers_dict["no_research"] = self.event_triggers_dict.get("no_research", 0) + 1
            else:
                self.event_triggers_dict["no_research"] = 0

            self.do_autosale() #Mark extra serums to be sold by marketing.

            for policy in self.active_policy_list:
                policy.on_turn()

        def run_move(self):
            for policy in self.active_policy_list:
                policy.on_move()

        def run_day(self): #Run at the end of the day.
            self.attention += -self.attention_bleed
            if self.attention < 0:
                self.attention = 0

            #Pay everyone for the day
            if self.is_work_day:
                cost = self.calculate_salary_cost() + self.operating_costs
                self.change_funds(-cost)

                if self.attention >= self.max_attention and not self.event_triggers_dict.get("attention_event_pending", False):
                    self.event_triggers_dict["attention_event_pending"] = True
                    self.mandatory_crises_list.append(Action("attention_event", attention_event_requirement, "attention_event"))

                for policy in self.active_policy_list:
                    policy.on_day()

                remove_list = []
                for contract in self.active_contracts:
                    if contract.run_day():
                        remove_list.append(contract)
                        if contract.can_finish_contract:
                            contract.finish_contract()
                            self.add_normal_message("Contract " + contract.name + " was going to expire with product in inventory, completed automatically.")
                        else:
                            contract.abandon_contract()
                            self.add_normal_message("Contract " + contract.name + " has expired unfilled.")

                for removal in remove_list:
                    self.active_contracts.remove(removal)

            strip_club_income = self.calculate_strip_club_income()
            if strip_club_income != 0:
                self.change_funds(strip_club_income, add_to_log = False)
                self.add_normal_message("The [strip_club.formal_name] has made a net profit of $" + str(strip_club_income) + " today!")

            # reset some events
            self.event_triggers_dict["coffee_shop_buy_coffee_day"] = 0

            if day%7 == 6: #ie is Monday
                self.renew_contracts()
            return

        @property
        def is_open_for_business(self): #Checks to see if employees are currently working
            if not self.is_work_day: #It is the weekend, people have the day off.
                return False
            if time_of_day == 1 or time_of_day == 2 or time_of_day == 3: #It is the work period of the day
                return True
            return False #If all else fails, give them some time off.

        @property
        def is_work_day(self):
            return not self.is_weekend        #TODO: add support for expanding workdays

        @property
        def is_weekend(self):                   #TODO: add support for expanding/changing the weekend
            return day%7 == 5 or day%7 == 6     #Checks to see if it is saturday or sunday. Note that days might eventually be both neither weekend or workday, or both weekend AND workday!

        @property
        def stripper_wardrobe(self):
            return self._stripper_wardrobe

        @property
        def waitress_wardrobe(self):
            return self._waitress_wardrobe

        @property
        def bdsm_wardrobe(self):
            return self._bdsm_wardrobe

        @property
        def manager_wardrobe(self):
            return self._manager_wardrobe

        @property
        def mistress_wardrobe(self):
            return self._mistress_wardrobe

        @property
        def stripclub_uniforms(self):
            def parse_wardrobe_to_uniform(wardrobe, flag_func):
                for outfit in wardrobe.outfit_sets:
                    uniform = StripClubOutfit(outfit)
                    uniform.set_full_outfit_flag(True)
                    getattr(uniform, flag_func)(True)
                    self._stripclub_uniforms.append(uniform)

                for outfit in wardrobe.overwear_sets:
                    uniform = StripClubOutfit(outfit)
                    uniform.set_overwear_flag(True)
                    getattr(uniform, flag_func)(True)
                    self._stripclub_uniforms.append(uniform)

                for outfit in wardrobe.underwear_sets:
                    uniform.set_underwear_flag(True)
                    getattr(uniform, flag_func)(True)
                    self._stripclub_uniforms.append(uniform)
                return

            if not hasattr(self, "_stripclub_uniforms"):
                self._stripclub_uniforms = []

                parse_wardrobe_to_uniform(stripclub_wardrobe, "set_stripper_flag")
                parse_wardrobe_to_uniform(waitress_wardrobe, "set_waitress_flag")
                parse_wardrobe_to_uniform(BDSM_performer_wardrobe, "set_bdsm_flag")
                parse_wardrobe_to_uniform(manager_wardrobe, "set_manager_flag")
                parse_wardrobe_to_uniform(mistress_wardrobe, "set_mistress_flag")

            return self._stripclub_uniforms

        def get_uniform_wardrobe_for_person(self, person):
            if not person.job:
                return Wardrobe("Empty Wardrobe")

            if person.is_at_office:
                if person.job == market_job:
                    return self.m_uniform
                if person.job == rd_job or person.job == head_researcher_job:
                    return self.r_uniform
                if person.job == production_job:
                    return self.p_uniform
                if person.job == supply_job:
                    return self.s_uniform
                if person.job == hr_job:
                    return self.h_uniform

                if "college_intern_role" in globals():
                    # only use this part after the college interns unlocked
                    if person.job == student_intern_market_job:
                        return self.m_uniform
                    if person.job == student_intern_rd_job:
                        return self.r_uniform
                    if person.job == student_intern_production_job:
                        return self.p_uniform
                    if person.job == student_intern_supply_job:
                        return self.s_uniform
                    if person.job == student_intern_hr_job:
                        return self.h_uniform

            if person == police_chief:
                return police_chief_uniform_wardrobe
            if person.job == stripper_job: # base game stripper
                return stripclub_wardrobe
            if person.job == stripclub_stripper_job or person.has_role(stripclub_stripper_role): # stripclub bought stripper
                return self.stripper_wardrobe
            if person.job == stripclub_waitress_job or person.has_role(stripclub_waitress_role):
                return self.waitress_wardrobe
            if person.job == stripclub_bdsm_performer_job or person.has_role(stripclub_bdsm_performer_role):
                return self.bdsm_wardrobe
            if person.job == stripclub_mistress_job or person.has_role(stripclub_mistress_role):
                return self.mistress_wardrobe
            if person.job == stripclub_manager_job or person.has_role(stripclub_manager_role):
                return self.manager_wardrobe
            if person.has_role(maid_role) or person.job in [hotel_maid_job, hotel_maid_job2]:
                return maid_wardrobe
            if person.job == prostitute_job:
                return prostitute_wardrobe
            if person.job in [doctor_job, nurse_job, night_nurse_job]:
                return nurse_wardrobe
            if person.job.job_title == "Barista":
                return barista_wardrobe

            return Wardrobe("Empty Wardrobe")

        def update_stripclub_wardrobes(self):
            def update_stripclub_uniform(wardrobe, uniform):
                if uniform.full_outfit_flag:
                    wardrobe.add_outfit(uniform.outfit)
                if uniform.overwear_flag:
                    wardrobe.add_overwear_set(uniform.outfit)
                if uniform.underwear_flag:
                    wardrobe.add_underwear_set(uniform.outfit)
                return

            self.stripper_wardrobe.clear_wardrobe()
            self.waitress_wardrobe.clear_wardrobe()
            self.bdsm_wardrobe.clear_wardrobe()
            self.manager_wardrobe.clear_wardrobe()
            self.mistress_wardrobe.clear_wardrobe()

            for uniform in self.stripclub_uniforms:
                if uniform.stripper_flag:
                    update_stripclub_uniform(self.stripper_wardrobe, uniform)
                if uniform.waitress_flag:
                    update_stripclub_uniform(self.waitress_wardrobe, uniform)
                if uniform.bdsm_flag:
                    update_stripclub_uniform(self.bdsm_wardrobe, uniform)
                if uniform.manager_flag:
                    update_stripclub_uniform(self.manager_wardrobe, uniform)
                if uniform.mistress_flag:
                    update_stripclub_uniform(self.mistress_wardrobe, uniform)
            return

        def get_uniform_limits(self): #Returns three values: the max sluttiness of a full outfit, max sluttiness of an underwear set, and if only overwear sets are allowed or notself.
            slut_limit = 0
            underwear_limit = 0
            limited_to_top = True
            if maximal_arousal_uniform_policy.is_active:
                slut_limit = 999 #ie. no limit at all.
                underwear_limit = 999
                limited_to_top = False
            elif corporate_enforced_nudity_policy.is_active:
                slut_limit = 80
                underwear_limit = 999
                limited_to_top = False
            elif minimal_coverage_uniform_policy.is_active:
                slut_limit = 60
                underwear_limit = 30
                limited_to_top = False
            elif reduced_coverage_uniform_policy.is_active:
                slut_limit = 40
                underwear_limit = 15
                limited_to_top = False
            elif casual_uniform_policy.is_active:
                slut_limit = 30
                underwear_limit = 0
                limited_to_top = True
            elif relaxed_uniform_policy.is_active:
                slut_limit = 20
                underwear_limit = 0
                limited_to_top = True
            elif strict_uniform_policy.is_active:
                slut_limit = 10
                underwear_limit = 0
                limited_to_top = True
            return slut_limit, underwear_limit, limited_to_top

        def add_uniform_to_company(self, outfit, full_outfit_flag = False, overwear_flag = False, underwear_flag = False, research = True, production = True, supply = True, marketing = True, hr = True):
            uniform = UniformOutfit(outfit)
            if uniform.can_toggle_full_outfit_state():
                uniform.set_full_outfit_flag(full_outfit_flag)
            if uniform.can_toggle_overwear_state():
                uniform.set_overwear_flag(overwear_flag)
            if uniform.can_toggle_underwear_state():
                uniform.set_underwear_flag(underwear_flag)

            uniform.set_research_flag(research)
            uniform.set_production_flag(production)
            uniform.set_supply_flag(supply)
            uniform.set_marketing_flag(marketing)
            uniform.set_hr_flag(hr)

            self.business_uniforms.append(uniform)
            self.update_uniform_wardrobes()
            return

        def update_uniform_wardrobes(self): #Rebuilds all uniforms in the wardrobe based on current uniform settings.
            def update_department_uniform(the_wardrobe, the_uniform):
                if the_uniform.full_outfit_flag:
                    the_wardrobe.add_outfit(the_uniform.outfit.get_copy())
                if the_uniform.overwear_flag:
                    the_wardrobe.add_overwear_set(the_uniform.outfit.get_copy())
                if the_uniform.underwear_flag:
                    the_wardrobe.add_underwear_set(the_uniform.outfit.get_copy())

            self.m_uniform.clear_wardrobe()
            self.p_uniform.clear_wardrobe()
            self.r_uniform.clear_wardrobe()
            self.s_uniform.clear_wardrobe()
            self.h_uniform.clear_wardrobe()

            for a_uniform in self.business_uniforms:
                if a_uniform.hr_flag:
                    update_department_uniform(self.h_uniform, a_uniform)
                if a_uniform.research_flag:
                    update_department_uniform(self.r_uniform, a_uniform)
                if a_uniform.production_flag:
                    update_department_uniform(self.p_uniform, a_uniform)
                if a_uniform.supply_flag:
                    update_department_uniform(self.s_uniform, a_uniform)
                if a_uniform.marketing_flag:
                    update_department_uniform(self.m_uniform, a_uniform)

        def clear_messages(self): #clear all messages for the day.
            self.message_list = []
            self.counted_message_list = {}
            self.production_potential = 0
            self.supplies_purchased = 0
            self.production_used = 0
            self.research_produced = 0
            self.sales_made = 0
            self.serums_sold = 0

        def add_counted_message(self,message,new_count = 1):
            if message in self.counted_message_list:
                self.counted_message_list[message] += new_count
            else:
                self.counted_message_list[message] = new_count

        def add_normal_message(self,message): #Adds an uncounted message, only ever listed once per day
            if message not in self.message_list:
                self.message_list.append(message)

        def calculate_salary_cost(self):
            daily_cost = 0
            for person in self.supply_team + self.research_team + self.production_team + self.market_team + self.hr_team:
                daily_cost += person.salary
            return daily_cost

        def calculate_strip_club_income(self):
            income = 0
            if "get_strip_club_foreclosed_stage" in globals():
                if get_strip_club_foreclosed_stage() >= 5: # The player owns the club
                    multiplier = 1
                    if any(x for x in list_of_people if x.is_at_work and x.has_job([stripclub_manager_job, stripclub_mistress_job])):
                        multiplier = 1.1 # +10% income

                    for person in [x for x in known_people_in_the_game() if x.is_at_work and x.is_strip_club_employee]:
                        income += (calculate_stripper_profit(person) * multiplier)  # profit
                        income -= person.stripper_salary    # costs

            return __builtin__.int(income)  # round to whole dollars

        def add_serum_design(self,the_serum):
            self.serum_designs.append(the_serum)

        def remove_serum_design(self,the_serum):
            self.serum_designs.remove(the_serum)
            if the_serum is self.active_research_design:
                self.active_research_design = None

            for line in self.production_lines:
                if line.selected_design == the_serum:
                    line.set_product(None)

        def remove_trait(self, trait):
            self.blueprinted_traits.remove(trait)
            if trait is self.active_research_design:
                self.active_research_design = None

        def is_trait_researched(self, trait):
            if isinstance(trait, basestring):
                research_trait = find_in_list(lambda x: x.name.startswith(trait), list_of_traits) # As long as the naming convention of the serums are consistent then this should be a lazy workaround for not having them accessible in the global scope anymore
            else:
                research_trait = find_in_list(lambda x: x.name == trait.name, list_of_traits)
            if research_trait:
                return research_trait.researched
            return False

        def set_serum_research(self,new_research):
            if callable(new_research):
                new_research = new_research() #Used by serumtrait.unlock_function's, particularly SerumTraitBlueprints to properly set the new trait.
            self.active_research_design = new_research

        def research_progress(self, intel, focus, skill, production_modifier = 1.0):
            research_amount = ((3 * intel) + focus + (2 * skill) + 10) * (self.team_effectiveness / 100.0) * production_modifier

            if self.head_researcher:
                bonus_percent = (self.head_researcher.int - 2)*0.05
                research_amount = __builtin__.round(research_amount * (1.0 + bonus_percent), 1) #Every point above int 2 gives a 5% bonus.
                if bonus_percent > 0:
                    self.add_normal_message("Head researcher " + self.head_researcher.title + "'s intelligence resulted in a " + str(bonus_percent*100) + "% increase in research produced!")
                else:
                    self.add_normal_message("Head researcher " + self.head_researcher.title + "'s intelligence resulted in a " + str(bonus_percent*100) + "% change in research produced.")
            else:
                research_amount = __builtin__.round(research_amount * 0.9, 1) #No head researcher is treated like int 0.
                self.add_normal_message("No head researcher resulted in a 10% reduction in research produced! Assign a head researcher at R&D!")

            if self.active_research_design is not None:
                the_research = self.active_research_design
                is_researched = the_research.researched # If it was researched before we added any research then we are increasing the mastery level of a trait (does nothing to serum designs)
                self.research_produced += research_amount
                if the_research.add_research(research_amount): #Returns true if the research is completed by this amount'
                    if isinstance(the_research, SerumDesign):
                        the_research.generate_side_effects() #The serum will generate any side effects that are needed.
                        self.mandatory_crises_list.append(Action("Research Finished Crisis",serum_creation_crisis_requirement,"serum_creation_crisis_label",the_research,priority=100)) #Create a serum finished crisis, it will trigger at the end of the round
                        self.add_normal_message("New serum design researched: " + the_research.name)
                        self.active_research_design = None
                    elif isinstance(the_research, SerumTrait):
                        if is_researched: #We've researched it already, increase mastery level instead.
                            self.add_normal_message("Serum trait mastery improved: " + the_research.name + ", Now " + str(the_research.mastery_level))
                        else:
                            self.add_normal_message("New serum trait researched: " + the_research.name)
                            self.active_research_design = None #If it's a newly discovered trait clear it so we don't start mastering it without player input.


                #research_amount = 0 #We didn't actually research anything because there is nothing to research!

            return research_amount

        def player_research(self):
            amount_researched = self.research_progress(mc.int,mc.focus,mc.research_skill)
            self.listener_system.fire_event("general_work")
            self.listener_system.fire_event("player_research", amount = amount_researched)
            renpy.say(None, "You spend time in the lab, experimenting with different chemicals and techniques and producing " + str(amount_researched) + " research points.")
            return amount_researched

        def player_buy_supplies(self):
            amount_bought = self.supply_purchase(mc.focus, mc.charisma, mc.supply_skill)
            self.listener_system.fire_event("general_work")
            self.listener_system.fire_event("player_supply_purchase", amount = amount_bought)
            renpy.say(None, "You spend time securing new supplies for the lab, purchasing " + str(amount_bought) + " units of serum supplies.")
            return amount_bought

        def supply_purchase(self, focus, cha, skill, production_modifier = 1.0, cost_modifier = 1.0):
            max_supply = __builtin__.int(((5 * focus) + (3 * cha) + (3 * skill) + 20) * (self.team_effectiveness / 100.0))
            if (self.supply_count / (self.supply_goal or 1)) < 20 and self.supply_count < 250 and self.IT_project_is_active(supply_inventory_project):
                max_supply *= 1.25
            if max_supply + self.supply_count > self.supply_goal:
                max_supply = self.supply_goal - self.supply_count
                if max_supply <= 0:
                    return 0

            max_supply = __builtin__.int(max_supply)

            self.change_funds(-(max_supply * candace_calculate_discount()), add_to_log = False)

            self.supply_count += max_supply
            self.supplies_purchased += max_supply #Used for end of day reporting
            return max_supply

        def accept_contract(self, the_contract):
            self.active_contracts.append(the_contract)
            if the_contract in self.offered_contracts:
                self.offered_contracts.remove(the_contract)

            the_contract.start_contract()

        def abandon_contract(self, the_contract):
            if the_contract in self.active_contracts:
                self.active_contracts.remove(the_contract)

            the_contract.abandon_contract()

        def complete_contract(self, the_contract):
            if the_contract in self.active_contracts:
                self.active_contracts.remove(the_contract)

            the_contract.finish_contract()

        def renew_contracts(self):
            self.offered_contracts = []
            for x in range(0, self.max_offered_contracts):
                self.offered_contracts.append(generate_contract(self.max_serum_tier))

        def player_market(self):
            amount_sold = self.sale_progress(mc.charisma,mc.focus,mc.market_skill)
            #  #TODO: Replace the old goal here with the new one.
            self.listener_system.fire_event("general_work")
            renpy.say(None, "You spend time making phone calls to acquire new potential clients and advertising your business. You expand your market reach by " + str(amount_sold) + " people.")
            return amount_sold

        def sale_progress(self,cha,focus,skill, slut_modifier = 0, production_modifier = 1.0): #TODO: Decide what effects should directly affect price, and which ones should increase market reach gain.
            amount_increased = __builtin__.int((3*cha) + (focus) + (2*skill)) * (1.0+(slut_modifier)) * 5.0 * ((self.team_effectiveness*0.01) * production_modifier)
            self.market_reach += amount_increased
            return amount_increased

        def sell_serum(self, the_serum, serum_count = 1, slut_modifier = 0, fixed_price = -1, external_serum_source = False): #TODO: Set this up. Takes each serum, check's it's value on todays' market, and sells it.
            #NOTE: Each serum immediately decreases the value of the one sold after it. (ie selling one serum at a time is no more or less efficient than bulk selling to the open market.
            sales_value = 0

            if self.inventory.get_serum_count(the_serum) < serum_count and not external_serum_source:
                serum_count = self.inventory.get_serum_count(the_serum)

            for x in range(0, serum_count):
                if fixed_price >= 0:
                    serum_base_value = fixed_price
                else:
                    serum_base_value = self.get_serum_base_value(the_serum)

                # apply sales multipliers to serum base value
                serum_value = serum_base_value
                for modifier_tuple in self.sales_multipliers:
                    serum_value = serum_value * modifier_tuple[1]

                sales_value += serum_value

                self.mental_aspect_sold += the_serum.mental_aspect
                self.physical_aspect_sold += the_serum.physical_aspect
                self.sexual_aspect_sold += the_serum.sexual_aspect
                self.medical_aspect_sold += the_serum.medical_aspect

                attention_gain = the_serum.attention
                if attention_floor_increase_1_policy.is_active:
                    attention_gain -= 1
                if attention_floor_increase_2_policy.is_active:
                    attention_gain -= 1
                if attention_gain < 0:
                    attention_gain = 0
                self.attention += attention_gain

            sales_value = __builtin__.int(sales_value)

            if not external_serum_source:
                self.inventory.change_serum(the_serum, -serum_count)
            self.change_funds(sales_value)
            self.sales_made += sales_value
            self.listener_system.fire_event("player_serums_sold_count", amount = serum_count)
            self.listener_system.fire_event("serums_sold_value", amount = sales_value)

        def get_serum_base_value(self, the_serum, round_value = False):
            serum_value = 0
            serum_value += the_serum.mental_aspect * self.get_aspect_price("mental")
            serum_value += the_serum.physical_aspect * self.get_aspect_price("physical")
            serum_value += the_serum.sexual_aspect * self.get_aspect_price("sexual")
            serum_value += the_serum.medical_aspect * self.get_aspect_price("medical")

            if round_value:
                serum_value = __builtin__.int(serum_value)

            return serum_value

        def get_aspect_price(self, the_aspect): #If we want to be really proper we could have this check _per aspect_, but I think that's excessive.
            the_aspect = the_aspect.lower()
            if the_aspect == "mental":
                return self.mental_aspect_price * self.get_aspect_percent("mental")

            elif the_aspect == "physical":
                return self.physical_aspect_price * self.get_aspect_percent("physical")

            elif the_aspect == "sexual":
                return self.sexual_aspect_price * self.get_aspect_percent("sexual")

            elif the_aspect == "medical":
                return self.medical_aspect_price * self.get_aspect_percent("medical")

            elif the_aspect == "flaw":
                return self.flaws_aspect_cost * self.get_aspect_percent("flaw")

        def get_aspect_percent(self, the_aspect):
            the_aspect = the_aspect.lower()
            if the_aspect == "mental":
                return 1.0/(1+((self.mental_aspect_sold*1.0)/(self.market_reach*1.0)))

            elif the_aspect == "physical":
                return 1.0/(1+((self.physical_aspect_sold*1.0)/(self.market_reach*1.0)))

            elif the_aspect == "sexual":
                return 1.0/(1+((self.sexual_aspect_sold*1.0)/(self.market_reach*1.0)))

            elif the_aspect == "medical":
                return 1.0/(1+((self.medical_aspect_sold*1.0)/(self.market_reach*1.0)))

            elif the_aspect == "flaw":
                return 1.0

        def has_funds(self, money_amount):
            return self.funds >= money_amount

        def change_funds(self, amount, add_to_log = True):
            amount = __builtin__.int(amount)
            self.funds += amount

            if amount != 0 and add_to_log:
                if amount > 0:
                    mc.log_event(self.name + " received: " + "$" + str(__builtin__.abs(amount)), "float_text_green")
                else:
                    mc.log_event(self.name + " paid: " + "$" + str(__builtin__.abs(amount)), "float_text_green")
            return

        def production_progress(self, focus, intel, skill, production_modifier = 1.0):
            #First, figure out how many production points we can produce total. Subtract that much supply and mark that much production down for the end of day report.
            production_amount = __builtin__.int(((3*focus) + intel + (2*skill) + 10) * (self.team_effectiveness / 100.0) * production_modifier)
            self.production_potential += production_amount

            if production_amount > self.supply_count:
                production_amount = self.supply_count #Figure out our total available production, before we split it up between tasks (which might not have 100% usage!)

            for line in self.production_lines:
                supply_used = line.add_production(production_amount) #NOTE: this is modified by the weighted use of the Line in particular. This allows for greater than 100% efficency.
                self.supply_count += - supply_used
                self.production_used += supply_used

            return production_amount

        # Use to be def clear_production(self)
        def clear_all_production(self): #Clears all current production lines.
            for line in self.production_lines:
                line.set_product(None)

        @property
        def used_line_weight(self):
            used_production = 0
            for line in self.production_lines:
                used_production += line.production_weight #Tally how much weight we are using so far.
            return used_production

        def do_autosale(self):
            for line in self.production_lines:
                if line.autosell and line.selected_design:
                    extra_doses = self.inventory.get_serum_count(line.selected_design) - line.autosell_amount
                    if extra_doses > 0:
                        self.sell_serum(line.selected_design, extra_doses)

        def get_random_weighed_production_serum(self): #Return the serum design of one of our actively produced serums, relative probability by weight.
            used_production = self.used_line_weight
            random_serum_number = renpy.random.randint(0,used_production)

            for line in self.production_lines:
                if random_serum_number < line.production_weight and line.selected_design:
                    return line.selected_design
                else:
                    random_serum_number -= line.production_weight #Subtract the probability of this one from our number to make progress in our search.

            return None


        def player_production(self):
            production_amount = self.production_progress(mc.focus,mc.int,mc.production_skill)
            self.listener_system.fire_event("player_production", amount = production_amount)
            self.listener_system.fire_event("general_work")
            renpy.say(None, "You spend time in the lab synthesizing serum from the raw chemical precursors. You generate " + str(production_amount) + " production points.")
            return production_amount

        def player_hr(self):
            eff_amount = self.hr_progress(mc.charisma,mc.int,mc.hr_skill, instant_effect = True) #Player effect is instant so that it can be reflected on the UI right away.
            self.listener_system.fire_event("player_efficiency_restore", amount = eff_amount)
            self.listener_system.fire_event("general_work")
            renpy.say(None, "You settle in and spend a few hours filling out paperwork, raising company efficiency by " + str(eff_amount )+ "%%.")
            return eff_amount

        def hr_progress(self, cha, intel, skill, production_modifier = 1.0, instant_effect = False): #Don't compute efficiency cap here so that player HR effort will be applied against any efficiency drop even though it's run before the rest of the end of the turn.
            restore_amount = __builtin__.round(((3*cha) + (intel) + (2*skill)) * production_modifier)
            self.change_team_effectiveness(restore_amount, instant = instant_effect)
            return restore_amount

        def change_team_effectiveness(self, the_amount, instant = False):
            self.team_effectiveness_temp += the_amount #temp_effectiveness is changed to team_effectiveness on_turn so that all HR effects are frozen.

            if instant:
                self.team_effectiveness += the_amount
                if self.team_effectiveness > self.effectiveness_cap:
                    self.team_effectiveness = self.effectiveness_cap
                elif self.team_effectiveness < 50:
                    self.team_effectiveness = 50

        def update_team_effectiveness(self):
            self.team_effectiveness = self.team_effectiveness_temp

            if self.team_effectiveness > self.effectiveness_cap:
                self.team_effectiveness = self.effectiveness_cap
            elif self.team_effectiveness < 50:
                self.team_effectiveness = 50
            self.team_effectiveness_temp = self.team_effectiveness #Gets rid of overflow/underflow for the next round

        def undesignate_person(self, person): #Removes person from all of the work lists so they can be moved around without them working in two departments.
            if person in self.research_team:
                self.research_team.remove(person)
            if person in self.production_team:
                self.production_team.remove(person)
            if person in self.supply_team:
                self.supply_team.remove(person)
            if person in self.market_team:
                self.market_team.remove(person)
            if person in self.hr_team:
                self.hr_team.remove(person)
            if person in self.college_interns_research:
                self.college_interns_research.remove(person)
            if person in self.college_interns_production:
                self.college_interns_production.remove(person)
            if person in self.college_interns_supply:
                self.college_interns_production.remove(person)
            if person in self.college_interns_market:
                self.college_interns_market.remove(person)
            if person in self.college_interns_HR:
                self.college_interns_HR.remove(person)

        def add_employee_research(self, new_person):
            self.undesignate_person(new_person)
            new_person.change_job(rd_job, job_known = True)
            self.research_team.append(new_person)

        def add_employee_production(self, new_person):
            self.undesignate_person(new_person)
            new_person.change_job(production_job, job_known = True)
            self.production_team.append(new_person)

        def add_employee_supply(self, new_person):
            self.undesignate_person(new_person)
            new_person.change_job(supply_job, job_known = True)
            self.supply_team.append(new_person)

        def add_employee_marketing(self, new_person):
            self.undesignate_person(new_person)
            new_person.change_job(market_job, job_known = True)
            self.market_team.append(new_person)

        def add_employee_hr(self, new_person):
            self.undesignate_person(new_person)
            new_person.change_job(hr_job, job_known = True)
            self.hr_team.append(new_person)

        def remove_employee(self, person): #As of v0.49 this should be used exclusively for firing people. When changing jobs you can just assign them a new one, they should keep the correct roles.
            self.undesignate_person(person)
            person.change_location(person.home) # remove from premisis

            person.change_job(unemployed_job, job_known = True)

            #Roles can have an on_remove function, but these have special events that we want to make sure are triggered properly.
            if person == self.head_researcher:
                renpy.call("fire_head_researcher", person) #Call the label we use for firing the person as a role action. This should trigger it any time you fire or move your head researcher.

            if person == self.company_model:
                renpy.call("fire_model_label", person)

            if person == self.hr_director:
                self.fire_HR_director()

            if person == self.it_director:
                self.fire_IT_director()

            if person == self.prod_assistant:
                self.fire_production_assistant()

            if person == cousin and get_strip_club_foreclosed_stage() == 0: # she goes back to stripping
                stripclub_strippers.append(person)
                person.set_schedule(strip_club, the_times = [3, 4])
                person.event_triggers_dict["stripping"] = True #Used to flag the blackmail event

        @property
        def employee_list(self):
            return [x for x in self.research_team + self.production_team + self.supply_team + self.market_team + self.hr_team if x.is_available]

        @property
        def employee_count(self):
            return len(self.employee_list)

        def get_employee_title(self, person):
            if person in self.research_team:
                return "Researcher"

            elif person in self.market_team:
                return "Marketing"

            elif person in self.supply_team:
                return "Supply"

            elif person in self.production_team:
                return "Production"

            elif person in self.hr_team:
                return "Human Resources"

            return "None"

        def get_employee_workstation(self, person): #Returns the location a girl should be working at, or "None" if the girl does not work for you
            if person in self.research_team:
                return self.r_div

            elif person in self.market_team:
                return self.m_div

            elif person in self.supply_team:
                return self.s_div

            elif person in self.production_team:
                return self.p_div

            elif person in self.hr_team:
                return self.h_div

            return None

        def get_requirement_employee_list(self, exclude_list = [], **kargs): #Get a list of employees who pass the validrequirements. Pass the same arguments as person_meets_requirements expects as named args.
            return [x for x in self.employee_list if x not in exclude_list and x.person_meets_requirements(**kargs)]

        def advance_tutorial(self, tutorial_name):
            self.event_triggers_dict[tutorial_name] += 1 #advance our tutorial slot.

        def reset_tutorial(self, tutorial_name):
            self.event_triggers_dict[tutorial_name] = 1 #Reset it when the reset tutorial button is used.

        def add_sales_multiplier(self, multiplier_class, multiplier):
            mc.log_event("Serum sale value increased by " + str((multiplier - 1) * 100) + "% due to " + multiplier_class + ".", "float_text_grey")
            self.sales_multipliers.append([multiplier_class, multiplier])

        def update_sales_multiplier(self, multiplier_class, multiplier):
            found = next((x for x in self.sales_multipliers if x[0] == multiplier_class), None)
            if found:
                found[1] = multiplier
                mc.log_event("Serum sale value increased by " + str((multiplier - 1) * 100) + "% due to " + multiplier_class + ".", "float_text_grey")

        def remove_sales_multiplier(self, multiplier_class, multiplier):
            if [multiplier_class, multiplier] in self.sales_multipliers:
                mc.log_event("No longer receiving " + str((multiplier - 1) * 100) + "% serum value increase from " + multiplier_class + ".", "float_text_grey")
                self.sales_multipliers.remove([multiplier_class, multiplier])

        def generate_candidate_requirements(self): #Checks current business policies and generates a dict of keywords for create_random_person to set the correct values to company requirements.
            # In cases where a range is allowed it generates a random value in that range, so call this one per person being created.
            candidate_dict = {} # This will hold keywords and arguments for create_random_person to create a person with specific modifies

            candidate_dict["age_range"] = [Person.get_age_floor(),Person.get_age_ceiling()]
            candidate_dict["height_range"] = [Person.get_height_floor(),Person.get_height_ceiling()]
            candidate_dict["stat_range_array"] = [[Person.get_stat_floor(),Person.get_stat_ceiling()] for x in range(0,3)]
            candidate_dict["skill_range_array"]= [[Person.get_skill_floor(),Person.get_skill_ceiling()] for x in range(0,5)]
            candidate_dict["sex_skill_range_array"]= [[Person.get_sex_skill_floor(),Person.get_sex_skill_ceiling()] for x in range(0,4)]

            candidate_dict["happiness_range"] = [Person.get_happiness_floor(),Person.get_happiness_ceiling()]
            candidate_dict["suggestibility_range"] = [Person.get_suggestibility_floor(),Person.get_suggestibility_ceiling()]
            candidate_dict["sluttiness_range"] = [Person.get_sluttiness_floor(),Person.get_sluttiness_ceiling()]
            candidate_dict["love_range"] = [Person.get_love_floor(),Person.get_love_ceiling()]
            candidate_dict["obedience_range"] = [Person.get_obedience_floor(),Person.get_obedience_ceiling()]

            candidate_dict["tits_range"] = Person.get_tit_weighted_list()

            candidate_dict["relationship_list"] = Person.get_potential_relationships_list()

            #First Pass / Independent & Relative Policies
            for recruitment_policy in recruitment_policies_list:
                if recruitment_policy.is_active:
                    candidate_dict["age_range"][0] += recruitment_policy.extra_data.get("age_floor_adjust",0)
                    candidate_dict["age_range"][1] += recruitment_policy.extra_data.get("age_ceiling_adjust",0)

                    for stat_range in candidate_dict["stat_range_array"]:
                        stat_range[0] += recruitment_policy.extra_data.get("stat_floor_adjust",0)
                        stat_range[1] += recruitment_policy.extra_data.get("stat_ceiling_adjust",0)

                    for skill_range in candidate_dict["skill_range_array"]:
                        skill_range[0] += recruitment_policy.extra_data.get("skill_floor_adjust",0)
                        skill_range[1] += recruitment_policy.extra_data.get("skill_ceiling_adjust",0)

                    for sex_skill_range in candidate_dict["sex_skill_range_array"]:
                        sex_skill_range[0] += recruitment_policy.extra_data.get("sex_skill_floor_adjust",0)
                        sex_skill_range[1] += recruitment_policy.extra_data.get("sex_skill_ceiling_adjust",0)


                    candidate_dict["happiness_range"][0] += recruitment_policy.extra_data.get("happiness_floor_adjust",0)
                    candidate_dict["happiness_range"][1] += recruitment_policy.extra_data.get("happiness_ceiling_adjust",0)

                    candidate_dict["suggestibility_range"][0] += recruitment_policy.extra_data.get("suggestibility_floor_adjust",0)
                    candidate_dict["suggestibility_range"][1] += recruitment_policy.extra_data.get("suggestibility_ceiling_adjust",0)

                    candidate_dict["sluttiness_range"][0] += recruitment_policy.extra_data.get("sluttiness_floor_adjust",0)
                    candidate_dict["sluttiness_range"][1] += recruitment_policy.extra_data.get("sluttiness_ceiling_adjust",0)

                    candidate_dict["love_range"][0] += recruitment_policy.extra_data.get("love_floor_adjust",0)
                    candidate_dict["love_range"][1] += recruitment_policy.extra_data.get("love_ceiling_adjust",0)

                    candidate_dict["obedience_range"][0] += recruitment_policy.extra_data.get("obedience_floor_adjust",0)
                    candidate_dict["obedience_range"][1] += recruitment_policy.extra_data.get("obedience_ceiling_adjust",0)

                    relationships_allowed = recruitment_policy.extra_data.get("relationships_allowed")
                    if relationships_allowed:
                        candidate_dict["relationship_list"] = [relationship for relationship in candidate_dict["relationship_list"] if relationship[0] in relationships_allowed]

            #Make sure ranges are not reversed (only done for ranges where that is currently possible)
            if candidate_dict["age_range"][0] > candidate_dict["age_range"][1]:
                candidate_dict["age_range"].reverse()

            #2nd Pass / Absolute Policies
            for recruitment_policy in recruitment_policies_list:
                if recruitment_policy.is_active:
                    candidate_dict["tits_range"] = recruitment_policy.extra_data.get("tits_range", candidate_dict["tits_range"])

                    #Because these are absolute they should also ensure that the range is valid (so an absolute floor also needs to raise the ceiling if it's below the floor)
                    candidate_dict["height_range"][0] = __builtin__.max(candidate_dict["height_range"][0],recruitment_policy.extra_data.get("height_floor", candidate_dict["height_range"][0]))
                    candidate_dict["height_range"][1] = __builtin__.max(candidate_dict["height_range"][1],recruitment_policy.extra_data.get("height_floor", candidate_dict["height_range"][1]))

                    candidate_dict["height_range"][1] = __builtin__.min(candidate_dict["height_range"][1],recruitment_policy.extra_data.get("height_ceiling", candidate_dict["height_range"][1]))
                    candidate_dict["height_range"][0] = __builtin__.min(candidate_dict["height_range"][0],recruitment_policy.extra_data.get("height_ceiling", candidate_dict["height_range"][0]))

                    candidate_dict["age_range"][0] = __builtin__.max(candidate_dict["age_range"][0],recruitment_policy.extra_data.get("age_floor", candidate_dict["age_range"][0]))
                    candidate_dict["age_range"][1] = __builtin__.max(candidate_dict["age_range"][1],recruitment_policy.extra_data.get("age_floor", candidate_dict["age_range"][1]))

                    candidate_dict["age_range"][1] = __builtin__.min(candidate_dict["age_range"][1],recruitment_policy.extra_data.get("age_ceiling", candidate_dict["age_range"][1]))
                    candidate_dict["age_range"][0] = __builtin__.min(candidate_dict["age_range"][0],recruitment_policy.extra_data.get("age_ceiling", candidate_dict["age_range"][0]))

            #Enforce limits (only done where it's currently possible for it to be violated)
            candidate_dict["age_range"][0] = __builtin__.max(candidate_dict["age_range"][0],Person.get_age_floor(initial=False))
            candidate_dict["age_range"][1] = __builtin__.min(candidate_dict["age_range"][1],Person.get_age_ceiling(initial=False))

            #3rd Pass / Dependent limits
            candidate_dict["kids_range"] = Person.get_initial_kids_range(candidate_dict["age_range"],candidate_dict["relationship_list"])

            for recruitment_policy in recruitment_policies_list:
                if recruitment_policy.is_active:
                    #These are special restrictions that should be enforced *after* final age / relationships adjustments (which can only be done when the age and relationships are known) so they can't be calculated in at this point
                    candidate_dict["kids_floor"] = recruitment_policy.extra_data.get("kids_floor")
                    candidate_dict["kids_ceiling"] = recruitment_policy.extra_data.get("kids_ceiling")

            return candidate_dict

        def hire_company_model(self, person):
            if self.company_model:
                self.fire_company_model()
            self.company_model = person
            person.add_role(company_model_role)

        def fire_company_model(self):
            if self.company_model:
                self.company_model.remove_role(company_model_role)
                self.company_model = None

        def hire_head_researcher(self, person):
            if self.head_researcher:
                self.fire_head_researcher()
            self.head_researcher = person
            person.change_job(head_researcher_job)

        def fire_head_researcher(self):
            if self.head_researcher:
                self.head_researcher.change_job(rd_job)
                self.head_researcher = None

        def fire_HR_director(self):
            if self.hr_director:
                self.hr_director.remove_role(HR_director_role)
                self.hr_director = None
                cleanup_HR_director_meetings()

        def fire_IT_director(self):
            if self.it_director:
                self.set_override_schedule(None, the_days = [0, 1, 2, 3, 4], the_times = [1,2,3])
                self.it_director.remove_role(IT_director_role)
                self.it_director = None

        def fire_production_assistant(self):
            if self.prod_assistant:
                self.prod_assistant.remove_role(prod_assistant_role)
                self.prod_assistant = None

        def add_mandatory_crisis(self, crisis_event):
            self.mandatory_crises_list.append(crisis_event)

        def add_mandatory_morning_crisis(self, crisis_event):
            self.mandatory_morning_crises_list.append(crisis_event)

        def remove_mandatory_crisis(self, crisis_event):
            self.mandatory_crises_list.remove(crisis_event)
            self.mandatory_morning_crises_list.remove(crisis_event)

        def mc_offspring_count(self):
            return sum(x.number_of_children_with_mc for x in self.employee_list)

        def employees_with_children_with_mc(self):
            return [x for x in self.employee_list if x.has_child_with_mc]

        def employees_knocked_up_by_mc(self):
            return [x for x in self.employee_list if (x.is_pregnant and x.is_mc_father)]

        def date_scheduled_today(self):
            return (self.event_triggers_dict.get("movie_date_scheduled", False) and day%7 == 1) \
                or (self.event_triggers_dict.get("fuck_date_scheduled", False) and day%7 == 3) \
                or (self.event_triggers_dict.get("dinner_date_scheduled", False) and day%7 == 4)

        def set_event_day(self, dict_key, override = True, set_day = None):
            if not override and not dict_key in self.event_triggers_dict:
                return False
            self.event_triggers_dict[dict_key] = day if set_day is None else set_day
            return True

        def get_event_day(self, dict_key, set_if_none = True):
            if not dict_key in self.event_triggers_dict and set_if_none:
                self.set_event_day(dict_key)

            return self.event_triggers_dict.get(dict_key, 0)

        def days_since_event(self, dict_key, set_if_none = False):
            if not dict_key in self.event_triggers_dict and set_if_none:
                self.set_event_day(dict_key)

            return day - self.event_triggers_dict.get(dict_key, day)

        def string_since_event(self, dict_key): #Returns a string describing how long it has been since an event
            since = self.days_since_event(dict_key)

            if since < 1:
                return "earlier"
            elif since == 1:
                return "yesterday"
            elif since <= 4:
                return "a few days ago"
            elif since <= 10:
                return "a week ago"
            elif since <= 19:
                return "a couple weeks ago"
            elif since <= 28:
                return "a few weeks ago"
            elif since <= 45:
                return "a month ago"
            elif since <= 75:
                return "a couple months ago"
            elif since <= 145:
                return "a few months ago"
            return "quite some time ago"

        # College intern related functions
        @property
        def college_interns_research(self):
            return self._college_interns_research

        @property
        def college_interns_production(self):
            return self._college_interns_production

        @property
        def college_interns_market(self):
            return self._college_interns_market

        @property
        def college_interns_supply(self):
            return self._college_interns_supply

        @property
        def college_interns_HR(self):
            return self._college_interns_HR

        @property
        def college_interns_unlocked(self):
            return self._college_interns_unlocked

        @college_interns_unlocked.setter
        def college_interns_unlocked(self, value):
            self._college_interns_unlocked = value

        @property
        def college_supply_interns_unlocked(self):
            return self.event_triggers_dict.get("supply_interns_unlocked", False)

        @college_supply_interns_unlocked.setter
        def college_supply_interns_unlocked(self, value):
            self.event_triggers_dict["supply_interns_unlocked"] = value

        @property
        def college_market_interns_unlocked(self):
            return self.event_triggers_dict.get("market_interns_unlocked", False)

        @college_market_interns_unlocked.setter
        def college_market_interns_unlocked(self, value):
            self.event_triggers_dict["market_interns_unlocked"] = value

        @property
        def college_hr_interns_unlocked(self):
            return self.event_triggers_dict.get("hr_interns_unlocked", False)

        @college_hr_interns_unlocked.setter
        def college_hr_interns_unlocked(self, value):
            self.event_triggers_dict["hr_interns_unlocked"] = value

        @property
        def max_interns_by_division(self):
            return self._max_interns_by_division

        @college_interns_unlocked.setter
        def max_interns_by_division(self, value):
            self._max_interns_by_division = value

        def hire_college_intern(self, person, target_division, add_to_location = False):
            div_func = {
                "Research" : [ self.college_interns_research, self.r_div, student_intern_rd_job],
                "Production" : [ self.college_interns_production, self.p_div, student_intern_production_job],
                "Supply" : [ self.college_interns_supply, self.s_div, student_intern_supply_job],
                "Marketing" : [ self.college_interns_market, self.m_div, student_intern_market_job],
                "HR" : [ self.college_interns_HR, self.h_div, student_intern_hr_job]
            }
            if not person in div_func[target_division][0]:
                div_func[target_division][0].append(person)
            person.add_role(college_intern_role)
            person.change_job(div_func[target_division][2])
            person.set_override_schedule(div_func[target_division][1], the_days = [5,6], the_times = [1,2])
            if add_to_location:
                university.add_person(person)
            return

        def remove_college_intern(self, person):
            if person in self.college_interns_research:
                self.college_interns_research.remove(person)
            elif person in self.college_interns_production:
                self.college_interns_production.remove(person)
            elif person in self.college_interns_supply:
                self.college_interns_supply.remove(person)
            elif person in self.college_interns_market:
                self.college_interns_market.remove(person)
            elif person in self.college_interns_HR:
                self.college_interns_HR.remove(person)

            person.set_override_schedule(None, the_days = [5,6], the_times = [1,2])
            person.remove_role(college_intern_role)
            return

        def get_intern_depts_with_openings(self):
            dept_list = []
            if len(self.college_interns_research) < self.max_interns_by_division:
                dept_list.append("Research")
            if len(self.college_interns_production) < self.max_interns_by_division:
                dept_list.append("Production")
            if len(self.college_interns_market) < self.max_interns_by_division and self.college_market_interns_unlocked:
                dept_list.append("Marketing")
            if len(self.college_interns_supply) < self.max_interns_by_division and self.college_supply_interns_unlocked:
                dept_list.append("Supply")
            if len(self.college_interns_HR) < self.max_interns_by_division and self.college_hr_interns_unlocked:
                dept_list.append("HR")
            return dept_list

        @property
        def intern_list(self):
            return [x for x in self.college_interns_research + self.college_interns_production + self.college_interns_supply + self.college_interns_market + self.college_interns_HR if x.is_available]

        @property
        def intern_count(self):
            return __builtin__.len(self.intern_list)

        @property
        def is_open_for_internship(self):
            if self.is_weekend and time_of_day == 1 or time_of_day == 2:
                if self.intern_list:
                    return True
            return False

        def get_requirement_intern_list(self, exclude_list = [], **kargs): #Get a list of interns who pass the validrequirements. Pass the same arguments as person_meets_requirements expects as named args.
            return [x for x in self.intern_list if x not in exclude_list and x.person_meets_requirements(**kargs)]

        @property
        def topless_is_legal(self):
            return False

        @property
        def nudity_is_legal(self):
            return False

        @property
        def public_sex_act_is_legal(self):  #If minor sexual acts are legal
            return False

        @property
        def public_sex_is_legal(self):  #If full sex in public is legal
            return False

        @property
        def incestual_sex_is_legal(self):  #If incest is legal
            return False
