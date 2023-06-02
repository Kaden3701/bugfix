# This file holds all of the goal objects that the player might be given over the course of the game.

## LIST OF CURRENT EVENTS ##

## STAT GOALS ##
# "general_work"
# "new_hire", the_person
# "new_serum", the_serum
# "serums_sold_value", amount
# "time_advance"
# "daily_profit", amount

## WORK GOALS ##
# "player_research",amount
# "player_serums_sold_count", amount
# "player_efficiency_restore", amount
# "player_production", amount
# "player_supply_purchase", amount
# "add_uniform", the_outfit
# "HR_opinion_improvement", the_person
# "give_random_serum", the_person

## SEX GOALS ##
# "player_flirt", the_person
# "sex_event", the_person, the_position, the_object
# "sex_cum_mouth", the_person
# "sex_cum_vagina", the_person
# "girl_climax", the_person
# "girl_pregnant", the_person
# "girl_trance", the_person
# "sex_cum_on_face", the_person
# "sex_cum_on_tits", the_person
# "sex_cum_ass", the_person
# "threesome", persone_one, person_two

#GOALS TO MAKE#
# "Dress up" - Assign an outfit with X sluttiness to a person.
# Reach research tier X.

init 1 python: #TODO: Prevent you from getting the game goal type twice in a row.
    def create_new_stat_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(stat_goals) - set([mc.stat_goal])))
        else:
            potential_goal = get_random_from_list(stat_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_stat_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.

    def create_new_work_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(work_goals) - set([mc.work_goal])))
        else:
            potential_goal = get_random_from_list(work_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_work_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.

    def create_new_sex_goal(goal_difficulty, recursion = 0):
        if recursion < 5:
            potential_goal = get_random_from_list(list(set(sex_goals) - set([mc.sex_goal])))
        else:
            potential_goal = get_random_from_list(sex_goals)

        if potential_goal.check_valid(goal_difficulty) or recursion > 10: # forced exit add random goal even if not valid.
            goal_template = copy.deepcopy(potential_goal)
            goal_template.activate_goal(goal_difficulty)
            return goal_template
        else:
            return create_new_sex_goal(goal_difficulty, recursion + 1) #Quick and dirty recursion to cycle through and get a goal. Note: Explodes if we don't have a goal.


    def create_initial_stat_goal(goal_difficulty):
        goal_template = copy.deepcopy(work_time_goal)
        goal_template.activate_goal(goal_difficulty)
        return goal_template

    def create_initial_work_goal(goal_difficulty):
        goal_template = copy.deepcopy(generate_supply_goal)
        goal_template.activate_goal(goal_difficulty)
        return goal_template

    def create_initial_sex_goal(goal_difficulty):
        goal_template= copy.deepcopy(flirt_count_goal)
        goal_template.activate_goal(goal_difficulty)
        return goal_template

    ## STAT GOAL FUNCTIONS ##

    def work_time_function(the_goal):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def work_time_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += (the_difficulty * 2)
        return

    def hire_someone_function(the_goal, the_person):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def serum_design_function(the_goal, the_serum):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def make_money_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def make_money_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += the_difficulty * 200
        return

    def make_money_report(the_goal):
        return "$" + str(the_goal.arg_dict["count"]) + "/$" + str(the_goal.arg_dict["required"])

    def business_size_valid_function(the_goal, the_difficulty):
        return mc.business.employee_count >= __builtin__.int(the_difficulty/2)

    def business_size_function(the_goal):
        the_goal.arg_dict["count"] = mc.business.employee_count
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def business_size_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/2)
        return

    def business_size_report_function(the_goal):
        return str(mc.business.employee_count) + "/" + str(the_goal.arg_dict["required"])

    def business_size_fraction_function(the_goal):
        return mc.business.employee_count/the_goal.arg_dict["required"]

    def bank_account_size_valid_function(the_goal, the_difficulty):
        return mc.business.has_funds(500 + 500*the_difficulty)

    def bank_account_size_function(the_goal):
        #Checks to see if the player has made enough money yet.
        return mc.business.funds >= the_goal.arg_dict["required"]

    def bank_account_size_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"]  += (500 * the_difficulty)
        return

    def bank_account_size_report_function(the_goal):
        return "$" + str(mc.business.funds) + "/$" + str(the_goal.arg_dict["required"])

    def bank_account_size_fraction_function(the_goal):
        return mc.business.funds/the_goal.arg_dict["required"]

    def daily_profit_count_function(the_goal, profit):
        the_goal.arg_dict["count"] = profit # To make "progress" show
        return profit >= the_goal.arg_dict["required"]

    def daily_profit_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"]  = 100
        the_goal.arg_dict["required"]  += (50 * the_difficulty)
        if the_difficulty > 4:
            the_goal.arg_dict["required"]  += (100 * the_difficulty)
        if the_difficulty > 8:
            the_goal.arg_dict["required"]  += (150 * the_difficulty)
        if the_goal.arg_dict["required"] > 5000:
            the_goal.arg_dict["required"]  = 5000
        return

    ## WORK GOAL FUNCTIONS ##
    def generate_research_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def generate_research_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += (the_difficulty * 50)
        return

    def player_sell_serums_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def player_sell_serums_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += 5*the_difficulty
        return

    def player_hr_efficiency_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def player_hr_efficiency_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += 5*the_difficulty
        return

    def player_production_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def player_production_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += (the_difficulty * 50)
        return

    def player_supply_function(the_goal, amount):
        the_goal.arg_dict["count"] += amount
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def player_supply_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += (the_difficulty * 50)
        return

    def uniform_designer_function(the_goal, the_outfit):
        if the_outfit not in the_goal.arg_dict["outfits"]:
            the_goal.arg_dict["count"] += 1
            the_goal.arg_dict["outfits"].append(the_outfit)
            return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def uniform_designer_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += renpy.random.randint(0,4) #Difficulty doesn't matter, but we want them to have to add a random number of outfits.
        return

    def HR_interview_count_function(the_goal, the_person):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def HR_interview_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] = __builtin__.int(1 + (the_difficulty / 5))
        if the_goal.arg_dict["required"] > 5:
            the_goal.arg_dict["required"]  = 5

    def give_serum_count_function(the_goal, the_person):
        if the_person in mc.business.employee_list + [mom, lily, aunt, cousin]:
            return False

        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def give_serum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/3)
        return


    ## SEX GOAL FUNCTIONS ##
    def flirt_count_function(the_goal, the_person):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def flirt_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += the_difficulty
        return


    def makeout_count_function(the_goal, the_person, the_position, **kwargs):
        if the_position == kissing:
            if not the_person in the_goal.arg_dict["people"]:
                the_goal.arg_dict["people"].append(the_person)
                the_goal.arg_dict["count"] += 1
                return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def makeout_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] +=  __builtin__.int(the_difficulty/(2*1.0))
        return


    def mouth_cum_count_function(the_goal, the_person):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def mouth_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += the_difficulty
        return


    def orgasm_count_function(the_goal, **kwargs):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def knockup_count_function(the_goal, **kwargs):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def trance_count_function(the_goal, **kwargs):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def orgasm_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += the_difficulty
        return

    def vagina_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def vagina_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/3)
        return

    def chain_orgasm_count_function(the_goal, the_person, **kwargs):
        if the_goal.arg_dict["day"] == day and the_goal.arg_dict["time"] == time_of_day and the_goal.arg_dict.get("last person") == the_person:
            the_goal.arg_dict["count"] += 1

        else:
            the_goal.arg_dict["day"] = day
            the_goal.arg_dict["time"] = time_of_day
            the_goal.arg_dict["last person"] = the_person
            the_goal.arg_dict["count"] = 1 #We've made her orgasm at this point.

        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def chain_orgasm_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/5)
        return

    def taboo_break_function(the_goal, **kwargs):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def taboo_break_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/3)
        return

    def standard_count_report(the_goal):
        return str(the_goal.arg_dict["count"]) + "/" + str(the_goal.arg_dict["required"]) #Returns a string representation of the progress (generally to put over a progress bar). Default assumes count and required exist

    def standard_progress_fraction(the_goal): #Returns a float from 0.0 to 1.0 used to display progress bars. Default assumes float and required exist
        return (the_goal.arg_dict["count"]*1.0)/the_goal.arg_dict["required"]

    def always_valid_goal_function(the_goal, the_difficulty): #Always a valid goal to give to the player. TODO: Impliment support for non-valid goals.
        return True

    def pregnancy_valid_goal_function(the_goal, the_difficulty):
        return persistent.pregnancy_pref > 0 and the_difficulty >= 5

    def flat_difficulty_function(the_goal, the_difficulty): #Does not become more difficult with time.
        return

    def face_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def face_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/4)
        return

    def tits_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def tits_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/6)  #Unlocked goal, so we make it slightly easier than other similar ones.
        return

    def ass_cum_count_function(the_goal, the_person):
        if not the_person in the_goal.arg_dict["people"]:
            the_goal.arg_dict["people"].append(the_person)
            the_goal.arg_dict["count"] += 1
            return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]
        return False

    def ass_cum_count_difficulty_function(the_goal, the_difficulty):
        the_goal.arg_dict["required"] += __builtin__.int(the_difficulty/4)
        return

    def threesome_count_function(the_goal, the_person_one, the_person_two):
        the_goal.arg_dict["count"] += 1
        return the_goal.arg_dict["count"] >= the_goal.arg_dict["required"]

    def threesome_difficulty_function(the_goal, the_difficulty): #For now this difficulty does not scale
        the_goal.arg_dict["required"] = 1
        return

    stat_goals = [] #This list will hold all of the stat goals that the player can be given. Goals are described by frameworks, esntially a list of parameters to hand to the Goal object when the goal is live.
    work_goals = [] #Holds goals related to the work category of variables
    sex_goals = [] #Same as above but for sex category goals


    ## STAT GOALS ##
    work_time_goal = Goal("Work-A-Day", "It may not be groundbreaking, but you learn a little something every day. Personally perform any work task.", "general_work", "Business",always_valid_goal_function, work_time_function,
    {"count": 0, "required": 5},
    difficulty_scale_function = work_time_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    hire_someone_goal = Goal("Fresh Blood", "New talent is the lifeblood of your business. Comb through the resumes and see who catches your eye.", "new_hire", "Business", always_valid_goal_function, hire_someone_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    serum_design_goal = Goal("Research and Development", "Theoretical research is all well and good, but you need products to put to market. Create a new serum design.", "new_serum", "Business", always_valid_goal_function, serum_design_function,
    {"count": 0 , "required": 1},
    difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    make_money_goal = Goal("Stable Income", "Any successful business needs income to match expenses. Have your business earn money.", "serums_sold_value", "Business", always_valid_goal_function, make_money_function,
    {"count": 0, "required": 300},
    difficulty_scale_function = make_money_difficulty_function, report_function = make_money_report, progress_fraction_function = standard_progress_fraction)

    business_size_goal = Goal("Sizable Workforce", "Sometimes quantity is more important than quality. Ensure your business has the required number of employees.", "time_advance", "MC", business_size_valid_function, business_size_function,
    {"required": 1},
    difficulty_scale_function = business_size_difficulty_function, report_function = business_size_report_function, progress_fraction_function = business_size_fraction_function)

    bank_account_size_goal = Goal("Liquidity", "A depth of liquid cash gives you the ability to react quickly to the changing whims of the free market. Amass a small fortune (Checked at the end of the day).", "time_advance", "MC", bank_account_size_valid_function, bank_account_size_function,
    {"required": 500},
    difficulty_scale_function = bank_account_size_difficulty_function, report_function = bank_account_size_report_function, progress_fraction_function = bank_account_size_fraction_function)

    daily_profit_goal = Goal("Daily Profit", "Profitability is always a concern when running a business. Have your business make at least a certain amount in one day.", "daily_profit", "Business", always_valid_goal_function, daily_profit_count_function,
    {"count": 0, "required": 50},
    difficulty_scale_function = daily_profit_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)



    ## WORK GOALS ##
    generate_research_goal = Goal("Brave New World", "The future is knocking, it's time to answer. Generate research points.", "player_research", "Business", always_valid_goal_function, generate_research_function,
    {"count": 0, "required": 100},
    difficulty_scale_function = generate_research_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    sell_serums_goal = Goal("Face of the Business", "Exercise your personal skills, pick up a phone, and make some sales! Sell some doses of serum.", "player_serums_sold_count", "Business", always_valid_goal_function, player_sell_serums_function,
    {"count": 0, "required": 5},
    difficulty_scale_function = player_sell_serums_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    hr_efficiency_goal = Goal("Paper Pusher", "Payroll, scheduling, tax structure, the internal demands of employment are always present. Perform HR work to improve efficiency", "player_efficiency_restore", "Business", always_valid_goal_function, player_hr_efficiency_function,
    {"count": 0, "required": 10},
    difficulty_scale_function = player_hr_efficiency_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    generate_production_goal = Goal("Practical Chemistry", "Get busy in the production lab and turn out some product. Produce production points.", "player_production", "Business", always_valid_goal_function, player_production_function,
    {"count": 0, "required": 100},
    difficulty_scale_function = player_production_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    generate_supply_goal = Goal("Master of Logistics", "You need to handle the \"supply\" side of supply and demand. Get on the phone and secure basic supplies for your serum.", "player_supply_purchase", "Business", always_valid_goal_function, player_supply_function,
    {"count": 0, "required": 100},
    difficulty_scale_function = player_supply_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    set_uniform_goal = Goal("Corporate Dress", "Public appearance can be just as important as the product you are selling. Pay your corporate wardrobe a visit and assign a few new uniform pieces.", "add_uniform", "Business", always_valid_goal_function, uniform_designer_function,
    {"count": 0, "required": 1, "outfits": []},
    difficulty_scale_function = uniform_designer_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    HR_interview_goal = Goal("HR meetings", "Use the HR director to conduct meetings with employees.", "HR_opinion_improvement", "MC", always_valid_goal_function, HR_interview_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = HR_interview_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    give_serum_goal = Goal("Try This Serum", "Successfully give a serum to a person who is not an employee or family member.", "give_random_serum", "MC", always_valid_goal_function, give_serum_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = give_serum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)



    ## SEX GOALS ##
    flirt_count_goal = Goal("Plenty of Fish", "The first step is putting yourself out there. Flirt a few times.", "player_flirt", "MC", always_valid_goal_function, flirt_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = flirt_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    makeout_count_goal = Goal("Tongue Twister", "Practice makes perfect, and kissing is a good thing to be perfect at. Make out with different women.", "sex_event", "MC", always_valid_goal_function, makeout_count_function,
    {"count": 0, "required": 2, "people": []},
    difficulty_scale_function = makeout_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    mouth_cum_goal = Goal("Good Girls Swallow", "There's nothing better than seeing the look in a girl's eyes when you shoot your hot cum across her tongue. Do that a few times.", "sex_cum_mouth", "MC", always_valid_goal_function, mouth_cum_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = mouth_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    orgasm_count_goal = Goal("Shiver", "Send shivers down her spine with a kiss; make her spasm while you fuck her; do what you have to do to make her orgasm. Cause a few orgasms, all at once or split up.", "girl_climax", "MC", always_valid_goal_function, orgasm_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = orgasm_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    vagina_cum_goal = Goal("Spread your Seed", "They may be on the pill, they may be playing it risky, maybe they just aren't thinking straight. Regardless, when a girl asks for you to cum inside you should be happy to oblige. Cum inside a few different girls.", "sex_cum_vagina", "MC", always_valid_goal_function, vagina_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = vagina_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    chain_orgasm_goal = Goal("Ahegao", "Sure she's orgasmed, but what about second orgasms? Melt a girl's brain by making her cum repeatedly in the same session.", "girl_climax", "MC", always_valid_goal_function, chain_orgasm_count_function,
    {"count": 0, "required": 2, "day":0, "time":0, "last person":None},
    difficulty_scale_function = chain_orgasm_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    taboo_break_goal = Goal("New Frontiers", "There's nothing like a new experience, so go give someone else one. Break some taboos and show her what she's missing!", "girl_taboo_break", "MC", always_valid_goal_function, taboo_break_function,
    {"count": 0, "required": 2},
    difficulty_scale_function = taboo_break_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    knockup_goal = Goal("Beautiful Burdening", "They might say they don't want kids, but in the heat of the moment simple biology can not be denied. Bang 'em and breed 'em!", "girl_pregnant", "MC", pregnancy_valid_goal_function, knockup_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    trance_goal = Goal("Mind Break", "Those soft-spoken words, her shallow breathing, that cum-clouded look in her eye - all of them mean she's ready to hear a few choice suggestions from you. Put a girl into a trance.", "girl_trance", "MC", always_valid_goal_function, trance_count_function,
    {"count":0, "required": 1},
    difficulty_scale_function = flat_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction)

    face_cum_goal = Goal("Paint the Town White", "Show the world that various girls belong to you, by cumming all over their faces.", "sex_cum_on_face", "MC", always_valid_goal_function, face_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = face_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    tits_cum_goal = Goal("Frosted Cupcakes", "Mark you territory. Cum on multiple girl's tits.", "sex_cum_on_tits", "MC", always_valid_goal_function, tits_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = tits_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    ass_cum_goal = Goal("Anal Seeding", "There's nothing like dumping a load in a tight asshole. Cum inside a few different asses.", "sex_cum_ass", "MC", always_valid_goal_function, ass_cum_count_function,
    {"count": 0, "required": 1, "people": []},
    difficulty_scale_function = ass_cum_count_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)

    threesome_goal = Goal("Have a Threesome", "You don't need a million dollars to do two girls at the same time.", "threesome", "MC", always_valid_goal_function, threesome_count_function,
    {"count": 0, "required": 1},
    difficulty_scale_function = threesome_difficulty_function, report_function = standard_count_report, progress_fraction_function = standard_progress_fraction, enabled = False)


    stat_goals.append(work_time_goal)
    stat_goals.append(hire_someone_goal)
    stat_goals.append(serum_design_goal)
    stat_goals.append(make_money_goal)
    stat_goals.append(business_size_goal)
    stat_goals.append(bank_account_size_goal)
    stat_goals.append(daily_profit_goal)


    work_goals.append(generate_research_goal)
    work_goals.append(sell_serums_goal)
    work_goals.append(hr_efficiency_goal)
    work_goals.append(generate_production_goal)
    work_goals.append(generate_supply_goal)
    work_goals.append(set_uniform_goal)
    work_goals.append(give_serum_goal)
    work_goals.append(HR_interview_goal)


    sex_goals.append(flirt_count_goal)
    sex_goals.append(makeout_count_goal)
    sex_goals.append(mouth_cum_goal)
    sex_goals.append(orgasm_count_goal)
    sex_goals.append(vagina_cum_goal)
    sex_goals.append(chain_orgasm_goal)
    sex_goals.append(taboo_break_goal)
    sex_goals.append(knockup_goal)
    sex_goals.append(trance_goal)
    sex_goals.append(face_cum_goal)
    sex_goals.append(tits_cum_goal)
    sex_goals.append(ass_cum_goal)
    sex_goals.append(threesome_goal)


## CODE REQUIRED FOR ENABLING AND DISABLING GOALS (USE BY LIFESTYLE COACH)

init 5 python:
    add_label_hijack("normal_start", "activate_goal_storage")
    add_label_hijack("after_load", "update_goal_storage")

    def update_goal_enabled_states_for_list(option_list, goal_list):
        for goal in goal_list: # add new goals to existing games
            if goal not in option_list:
                option_list.add(goal)

        for goal in option_list:
            if not goal.enabled: # remove disabled, when in list
                found = find_in_list(lambda x: x == goal, goal_list)
                if found:
                    goal_list.remove(found)
            else: # add enabled, when not in list
                found = find_in_list(lambda x: x == goal, goal_list)
                if not found:
                    goal_list.append(goal)


    def update_goal_enabled_states():
        update_goal_enabled_states_for_list(stat_goals_options_list, stat_goals)
        update_goal_enabled_states_for_list(work_goals_options_list, work_goals)
        update_goal_enabled_states_for_list(sex_goals_options_list, sex_goals)
        return


label activate_goal_storage(stack):
    python:
        # secondary lists for storing all goals so we can enabled / disabled goals
        stat_goals_options_list = set(stat_goals)
        work_goals_options_list = set(work_goals)
        sex_goals_options_list = set(sex_goals)

        update_goal_enabled_states()
        # execute after stack has run
        execute_hijack_call(stack)
    return

label update_goal_storage(stack):
    python:
        update_goal_enabled_states()
        # execute after stack has run
        execute_hijack_call(stack)
    return
