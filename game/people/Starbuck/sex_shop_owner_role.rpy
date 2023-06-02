#This role is a replacement for Starbuck's Sex Shop Owner inherited class file.
#All functions associated with running the sex shop can now be done via Roles, so lets simplify the code and do it that way.
init -1 python:
    def sex_shop_invest_basic_requirement(person):
        if sex_shop_stage() > 0:
            if person.location != sex_store:
                return False
            if person.event_triggers_dict.get("shop_investment_basic_total", 0) > 5000:
                return "No more investment opportunity."
            elif mc.business.funds >= 1000:
                return True
            else:
                return "Requires: $1000"
        return False

    def sex_shop_invest_advanced_requirement(person):
        if sex_shop_stage() > 1:
            if person.location != sex_store:
                return False
            if person.event_triggers_dict.get("shop_investment_advanced_total", 0) > 20000:
                return "No more investment opportunity."
            elif mc.business.funds >= 5000:
                return True
            else:
                return "Requires: $5000"
        return False

    def sex_shop_invest_fetish_requirement(person):
        if sex_shop_stage() > 2:
            if person.location != sex_store:
                return False
            if person.event_triggers_dict.get("shop_investment_fetish_total", 0) > 45000:
                return "No more investment opportunity."
            elif mc.business.funds >= 15000:
                return True
            else:
                return "Requires: $15000"
        return False


init 1 python:
    sex_shop_invest_basic = Action("Invest in more basic inventory", sex_shop_invest_basic_requirement, "sex_shop_invest_basic_label")
    sex_shop_invest_advanced = Action("Invest in more advanced inventory", sex_shop_invest_advanced_requirement, "sex_shop_invest_advanced_label")
    sex_shop_invest_fetish = Action("Invest in more fetish inventory", sex_shop_invest_fetish_requirement, "sex_shop_invest_fetish_label")

    def sex_shop_owner_on_turn(person):
        pass
        return

    def sex_shop_owner_on_day(person): #Use this function to determine if she is going to act on jealous score. also can check for date events here.
        if sex_shop_stage() > 0:
            investment_return = sex_shop_investment_return(person)
            if (investment_return > 0) :
                mc.business.change_funds(investment_return, add_to_log = False)
                mc.business.add_normal_message("Sex shop has returned $" + str(investment_return) + " on your investment!")
            return

    def make_sex_shop_owner(the_person):
        the_person.event_triggers_dict["shop_progress_stage"] = 0   #For story purposes
        the_person.event_triggers_dict["shop_investment_total"] = 0 #For calculation purposes
        the_person.event_triggers_dict["shop_investment_rate"] = 0  #For balance purposes
        the_person.event_triggers_dict["shop_investment_basic_total"] = 0
        the_person.event_triggers_dict["shop_investment_advanced_total"] = 0
        the_person.event_triggers_dict["shop_investment_fetish_total"] = 0
        the_person.event_triggers_dict["shop_market_production_count"] = 0  #For extra income if we've spent a lot of time on promo videos etc.
        sex_shop_invest_role = Role(role_name ="Sex Shop Invest Role", actions =[sex_shop_invest_basic, sex_shop_invest_advanced, sex_shop_invest_fetish], on_turn = sex_shop_owner_on_turn, on_move = None, on_day = sex_shop_owner_on_day, hidden = True)
        the_person.add_role(sex_shop_invest_role)
        return

    def sex_shop_investment_return(person):
        investment_return = 30
        investment_return += int (person.event_triggers_dict.get("shop_investment_basic_total", 0) * get_shop_investment_rate() * 0.01)
        investment_return += int (person.event_triggers_dict.get("shop_investment_advanced_total", 0) * get_shop_investment_rate() * 0.004)
        investment_return += int (person.event_triggers_dict.get("shop_investment_fetish_total", 0) * get_shop_investment_rate() * 0.004)
        return __builtin__.int(investment_return * (renpy.random.random() + .5))    # make it variable rounded to whole dollars

    def sex_shop_stage():
        return starbuck.event_triggers_dict.get("shop_progress_stage", 0)


label sex_shop_invest_basic_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh?"
    mc.name "I'd like for you to expand more of your basic inventory."
    the_person "Those do tend to be high margin, profitable items. I supposed I could look around and see if I can expand my inventory some."
    mc.name "Sounds great. Here's a check for $1000."
    $ the_person.change_love(1)
    $ the_person.change_obedience(2)
    $ mc.business.change_funds(-1000)
    $ the_person.event_triggers_dict["shop_investment_basic_total"] += 1000
    $ the_person.event_triggers_dict["shop_investment_total"] += 1000
    the_person "Wow! I really appreciate this. Is there anything else you need [the_person.mc_title]?"
    the_person "Maybe you could swing by sometime in the evening and help me put up stock?"
    return

label sex_shop_invest_advanced_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh?"
    mc.name "I'd like for you to expand more of your advanced inventory."
    the_person "Yeah, having intricate toys and the like can be great for driving foot traffic, even if they don't sell very fast."
    mc.name "Sounds great. Here's a check for $5000."
    $ the_person.change_love(2)
    $ the_person.change_obedience(5)
    $ mc.business.change_funds(-5000)
    $ the_person.event_triggers_dict["shop_investment_advanced_total"] += 5000
    $ the_person.event_triggers_dict["shop_investment_total"] += 5000
    the_person "Wow! I can't believe you are investing even more! This is really incredible. Is there anything else you need while you're here, [the_person.mc_title]?"
    return

label sex_shop_invest_fetish_label(the_person):
    mc.name "I'd like to invest more in your shop, [the_person.title]."
    the_person "Oh? You've already done so much."
    mc.name "I'd like for you to expand more of your fetish inventory."
    the_person "Fetish inventory moves slowly, but it definitely drives interest and foot traffic."
    mc.name "Sounds great. Here's a check for $15000."
    $ the_person.change_love(3)
    $ the_person.change_obedience(10)
    $ mc.business.change_funds(-15000)
    $ the_person.event_triggers_dict["shop_investment_fetish_total"] += 15000
    $ the_person.event_triggers_dict["shop_investment_total"] += 15000
    the_person "Holy fuck! You're amazing [the_person.mc_title]! Anything else you need while you are here?"
    return
