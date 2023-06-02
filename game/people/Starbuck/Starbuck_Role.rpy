init 2 python:
    list_of_instantiation_functions.append("create_starbuck_character")

    #starbuck ACTIONS#
    starbuck_vaginal_skillup = Action("Ask about temporarily improving vaginal skill", starbuck_vaginal_skillup_requirement, "starbuck_vaginal_skillup_label")
    starbuck_anal_skillup = Action("Ask about temporarily improving anal skill", starbuck_anal_skillup_requirement, "starbuck_anal_skillup_label")
    starbuck_oral_skillup = Action("Ask about temporarily improving oral skill", starbuck_oral_skillup_requirement, "starbuck_oral_skillup_label")
    starbuck_foreplay_skillup = Action("Ask about temporarily improving foreplay", starbuck_foreplay_skillup_requirement, "starbuck_foreplay_skillup_label")
    starbuck_arousal_reduction_one = Action("Ask about lasting longer", starbuck_arousal_reduction_one_requirement, "starbuck_arousal_reduction_one_label")
    starbuck_arousal_reduction_two = Action("Ask about lasting even longer", starbuck_arousal_reduction_two_requirement, "starbuck_arousal_reduction_two_label")
    starbuck_sex_store_investment_one = Action("Ask about investing in her store", starbuck_sex_store_investment_one_requirement, "starbuck_sex_store_investment_one_label")
    starbuck_sex_store_investment_two = Action("Ask about stock levels", starbuck_sex_store_investment_two_requirement, "starbuck_sex_store_investment_two_label")
    starbuck_sex_store_investment_three = Action("Ask about further investment", starbuck_sex_store_investment_three_requirement, "starbuck_sex_store_investment_three_label")
    starbuck_sex_store_promo_one = Action("Ask how business is going", starbuck_sex_store_promo_one_requirement, "starbuck_sex_store_promo_one_label")
    starbuck_sex_store_promo_two = Action("Ask if advertising is working", starbuck_sex_store_promo_two_requirement, "starbuck_sex_store_promo_two_label")
    starbuck_sex_store_promo_three = Action("Ask if women are coming in", starbuck_sex_store_promo_three_requirement, "starbuck_sex_store_promo_three_label")
    starbuck_sex_store_promo_four = Action("Ask if couples are coming in", starbuck_sex_store_promo_four_requirement, "starbuck_sex_store_promo_four_label")
    starbuck_sex_store_promo_five = Action("Ask if couples are coming in", starbuck_sex_store_promo_five_requirement, "starbuck_sex_store_promo_five_label")
    starbuck_spend_the_night = Action("Spend the night with her", starbuck_spend_the_night_requirement, "starbuck_spend_the_night_label")
    starbuck_close_up = Action("Help close the store", starbuck_close_up_requirement, "starbuck_close_up_label")
    starbuck_anal_fetish_swing_demo = Action("Anal Sex Swing Demo", starbuck_anal_fetish_swing_demo_requirement, "starbuck_anal_fetish_swing_demo_label")

    def create_starbuck_character():
        starbuck_wardrobe = wardrobe_from_xml("Starbuck_Wardrobe")

        starbuck_personality = Personality("starbuck", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["skirts", "small talk", "the colour blue", "makeup"],
        common_sexy_likes = ["lingerie","taking control",  "doggy style sex", "creampies"],
        common_dislikes = ["working", "conservative outfits", "Mondays", "pants", "dresses"],
        common_sexy_dislikes = [ "masturbating", "giving handjobs"],
        titles_function = starbuck_titles, possessive_titles_function = starbuck_possessive_titles, player_titles_function = starbuck_player_titles)

        # init starbuck role
        global starbuck_role
        starbuck_role = Role(role_name ="Sex Shop Owner", actions =[starbuck_vaginal_skillup, starbuck_anal_skillup, starbuck_oral_skillup, starbuck_foreplay_skillup, starbuck_sex_store_investment_one,
            starbuck_sex_store_investment_two, starbuck_sex_store_investment_three, starbuck_sex_store_promo_one, starbuck_sex_store_promo_two, starbuck_sex_store_promo_three, starbuck_sex_store_promo_four,
            starbuck_sex_store_promo_five, starbuck_spend_the_night, starbuck_close_up, starbuck_anal_fetish_swing_demo], hidden = True)

        starbuck_job = Job("Sex Shop Owner", starbuck_role, sex_store, work_times = [2, 3])
        starbuck_job.schedule.set_schedule(sex_store, the_days = [5,6], the_times=[1,2])

        #global starbuck_role
        global starbuck
        starbuck_base = Outfit("Starbuck's accessories")
        starbuck_lipstick = lipstick.get_copy()
        starbuck_lipstick.colour = [.80, .26, .04, .90]
        starbuck_base.add_accessory(starbuck_lipstick)

        starbuck = make_person(name = "Cara", last_name = "Thrace", age = 32, body_type = "curvy_body", face_style = "Face_4", tits="E", height = 0.89, hair_colour= ["golden blonde", [0.895, 0.781, 0.656,1]], hair_style = messy_short_hair, skin = "white",
            eyes = ["green",[0.245, 0.734, 0.269, 1.0]], pubes_style = landing_strip_pubes, personality = starbuck_personality, name_color = "#cd5c5c", starting_wardrobe = starbuck_wardrobe, job = starbuck_job,  \
            stat_array = [3,4,3], skill_array = [1,1,4,2,1], sex_skill_array = [3,3,4,4], sluttiness = 27, obedience_range = [70, 85], happiness = 119, love = 0, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = starbuck_base, type = 'story')

        starbuck.generate_home()
        starbuck.home.add_person(starbuck)
        make_sex_shop_owner(starbuck)
        return

    def SB_mod_initialization(action_mod):
        # Add StarBuck introduction event to sex store
        starbuck.add_unique_on_room_enter_event(starbuck_introduction_event_action)
        return

    # create mod event to trigger creation
    starbuck_introduction_event_action = ActionMod("Starbuck's Sex Shop", starbuck_introduction_requirement, "starbuck_greetings", initialization = SB_mod_initialization, menu_tooltip = "Starbuck's Sex Shop", category = "Misc", allow_disable = False)

init -1 python:
    def get_shop_investment_rate():
        return starbuck.event_triggers_dict.get("shop_investment_rate", 1)

    def starbuck_introduction_requirement(the_person):
        if starbuck.location == sex_store:    # only trigger event when starbuck is there
            return True
        return False

    def starbuck_vaginal_skillup_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() >= 2:
            if perk_system.has_stat_perk("Vibrating Cock Ring"):
                return "Already Active"
            if mc.business.has_funds(500):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $500"
        return False


    def starbuck_anal_skillup_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() >= 3:
            if perk_system.has_stat_perk("Perfect Anal Lube"):
                return "Already Active"
            if mc.business.has_funds(800):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $800"
        return False

    def starbuck_foreplay_skillup_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() >= 1:
            if perk_system.has_stat_perk("Small Finger Vibrator"):
                return "Already Active"
            if mc.business.has_funds(100):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $100"
        return False

    def starbuck_oral_skillup_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() >= 2:
            if perk_system.has_stat_perk("Stimulating Lip Balm"):
                return "Already Active"
            if mc.business.has_funds(250):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $250"
        return False

    def starbuck_arousal_reduction_one_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if SB_MOD_MC_AROUSAL_MULT == 1.0:
            if mc.business.has_funds(500):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $500"
        return False

    def starbuck_arousal_reduction_two_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if SB_MOD_MC_AROUSAL_MULT == SB_MOD_MC_AROUSAL_1ST_MULT:
            if mc.business.has_funds(5000):
                if mc.location == sex_store:
                    return True
            else:
                return "Requires: $5000"
        return False

    def starbuck_sex_store_investment_one_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() == 0:
            if mc.business.has_funds(1000):
                return True
            else:
                return "Requires: $1000"

    def starbuck_sex_store_investment_two_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() == 1:
            if (the_person.event_triggers_dict.get("shop_stage_one_day", 9999) + 7) < day:
                if mc.business.has_funds(5000):
                    return True
                else:
                    return "Requires: $5000"
            else:
                return "Wait for her stock to balance out"

    def starbuck_sex_store_investment_three_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() == 2:
            if (the_person.event_triggers_dict.get("shop_stage_two_day", 9999) + 7) < day:
                if mc.business.has_funds(15000):
                    return True
                else:
                    return "Requires: $15000"
            else:
                return "Wait for her stock to balance out"

    def starbuck_sex_store_promo_one_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() > 0:
            if get_shop_investment_rate() == 1.0:
                return True
        return False

    def starbuck_sex_store_promo_two_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() > 0:
            if get_shop_investment_rate() == 2.0:
                return True
        return False

    def starbuck_sex_store_promo_three_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() > 1:
            if get_shop_investment_rate() == 3.0:
                if starbuck.sluttiness >= 60:
                    if starbuck.love >= 50:
                        return True
                    else:
                        return "Requires: 50+ Love"
                else:
                    return "Requires: 60+ sluttiness"
        return False

    def starbuck_sex_store_promo_four_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() > 1:
            if get_shop_investment_rate() == 4.0:
                if starbuck.sluttiness >= 70:
                    if starbuck.love >= 60:
                        return True
                    else:
                        return "Requires: 60+ Love"
                else:
                    return "Requires: 70+ sluttiness"
        return False

    def starbuck_sex_store_promo_five_requirement(the_person):
        if not the_person.is_at_work:
            return False
        if sex_shop_stage() > 2:
            if get_shop_investment_rate() == 5.0:
                if starbuck.sluttiness >= 90:
                    if starbuck.love >= 70:
                        return True
                    else:
                        return "Requires: 70+ Love"
                else:
                    return "Requires: 90+ sluttiness"
        return False

    def starbuck_spend_the_night_requirement(the_person):
        if get_shop_investment_rate() == 6.0:
            if time_of_day < 4:
                return "Only at night"
            else:
                return True

    def starbuck_close_up_requirement(the_person):
        if sex_shop_stage() > 0:
            if mc.location == sex_store:
                if time_of_day == 3:
                    return True
                else:
                    return "She closes in the evening"

    def starbuck_anal_fetish_swing_demo_requirement(person):
        if person is starbuck and starbuck.has_anal_fetish:
            if mc.location == sex_store:
                return True
            else:
                return "Must be at the Sex Shop"
        else:
            return False

    def starbuck_is_business_partner():
        if sex_shop_stage() >= 1:
            return True
        return False



#SBS10
label starbuck_vaginal_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at vaginal sex. You ask if she has any tips or products for further improvement, even if it's temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of cock rings."
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title] picks one off the shelf, it looks like it has a number of features, like vibration and heat."
    "It looks like a good buy, but unfortunately it has a built in battery that cannot be recharged. Once it's done, it's done!"
    menu:
        "Purchase ($500)":
            $ mc.business.change_funds(-500)
            $ perk_system.add_stat_perk(Stat_Perk(description = "Cock ring that increases pleasure during vaginal sex. Lasts one week. +2 Vaginal skill", vaginal_bonus = 2, bonus_is_temp =True, duration = 7), "Vibrating Cock Ring")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 70:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her":
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair you be the first to feel it."
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(50)
                        "She quickly takes off some clothes to give you easy access and hops on the counter."
                        if the_person.outfit.can_half_off_to_vagina():
                            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "stand3")
                        else:
                            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "stand3")
                        call fuck_person(the_person, start_position = missionary, start_object = make_counter(), skip_intro = True) from _call_fuck_person_SBS10
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh wow... I've never... I came so many times..."
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 60)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 60)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS20
label starbuck_anal_skillup_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    "You explain to [the_person.possessive_title] that you feel like you need something to help take anal sex to the next level. You ask if she has any tips or products for further improvement, even if the benefits are temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of lubrications."
    the_person "You see [the_person.mc_title], the key to great anal sex, is using the perfect lube!"
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title] picks one off the shelf."
    the_person "This company has made a ton of advances in lube technology recently."
    the_person "This one has full effectiveness with just a small application, and is designed to both lubricate, AND increases blood flow to the nerve endings, making anal more pleasurable for the receiver!"
    menu:
        "Purchase ($800)":
            $ mc.business.change_funds(-800)
            $ perk_system.add_stat_perk(Stat_Perk(description = "Sensitizing and highly effective anal lubricant. Lasts one week. +2 Anal Skill", anal_bonus = 2, bonus_is_temp =True, duration = 7), "Perfect Anal Lube")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 90:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Fuck her ass":
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners from now on..."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair I use it on you first!"
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(50)
                        "She quickly takes off some clothes to give you easy access, turns around and bends over the counter."
                        if the_person.outfit.can_half_off_to_vagina():
                            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "stand3")
                        else:
                            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "stand3")
                        call fuck_person(the_person, start_position = anal_standing, start_object = mc.location.get_object_with_name("counter"), skip_intro = True) from _call_fuck_person_SBS20
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh wow... I've never... I came so many times!"
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 70)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... I came so hard!"
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 70)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS30
label starbuck_oral_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at oral sex. You ask if she has any tips or products for further improvement, even if the effects are temporary."
    the_person "Oh [the_person.mc_title]... I think I can probably help you with that!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of balms and oils."
    "She picks a balm up off the shelf. It looks like it's some kind of lip balm, but it's designed to increase blood flow and pleasure to female partners genitals it comes into contact with."
    the_person "Personally, I recommend this one."
    menu:
        "Purchase ($250)":
            $ mc.business.change_funds(-250)
            $ perk_system.add_stat_perk(Stat_Perk(description = "Lip balm that feels good when you go down on women. Lasts one week. +2 Oral Skill", oral_bonus = 2, bonus_is_temp =True, duration = 7), "Stimulating Lip Balm")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 45:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Eat her pussy":
                        mc.name "Sounds good, [the_person.title]."
                        the_person "Ah yes!"
                        "She quickly takes off some clothes to give you easy access and leans against her counter."
                        $ mc.change_locked_clarity(25)
                        if the_person.outfit.can_half_off_to_vagina():
                            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "stand3")
                        else:
                            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "stand3")
                        call fuck_person(the_person, start_position = cunnilingus, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_SBS30
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 1:
                            the_person "Oh my god, I came so many times... did you make me squirt?"
                            $ the_person.change_stats(obedience = 5, slut = 1, max_slut = 30)
                            the_person "Let's do that again soon!"
                        elif the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... That felt so good!"
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."
                        "You head back to your house and watch the video. You pick up several new tips and tricks to try next to eat a girl out!"

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS40
label starbuck_foreplay_skillup_label(the_person):
    "You explain to [the_person.possessive_title] that you feel like you've stopped improving your skill at foreplay. You ask if she has any tips or products for further improvement, even if it's only temporary."
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of sex toys."
    the_person "Personally, I recommend this one."
    "[the_person.possessive_title] picks a small vibrator off the shelf. It looks like it has a number of features, like vibration and heat."
    menu:
        "Purchase ($100)":
            $ mc.business.change_funds(-100)
            $ perk_system.add_stat_perk(Stat_Perk(description = "Small, finger mounted vibrator. Increases foreplay skill. Lasts one week. +2 Foreplay Skill", foreplay_bonus = 2, bonus_is_temp =True, duration = 7), "Small Finger Vibrator")
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            if the_person.sluttiness > 30:
                "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
                the_person "Now... did you maybe want some help... trying this out?"
                menu:
                    "Grope her":
                        "You take a quick look at the instructions. Looks like it should be fairly easy to keep with you and use with your partners."
                        mc.name "Sounds good, [the_person.title]. Since you recommended it, it's only fair you be the first to feel it."
                        the_person "Ah... I can't wait! Let's go!"
                        $ mc.change_locked_clarity(15)
                        "She quickly takes off some clothes to give you easy access."
                        if the_person.outfit.can_half_off_to_vagina():
                            $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True, position = "stand3")
                        else:
                            $ generalised_strip_description(the_person, the_person.outfit.get_vagina_strip_list(), position = "stand3")
                        call fuck_person(the_person, start_position = standing_grope, skip_intro = True) from _call_fuck_person_SBS40
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 0:
                            the_person "Oh wow... The orgasms that thing gives..."
                            $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 20)
                            the_person "Let's do that again soon!"
                        else:
                            the_person "Thanks for the fuck!"

                        "You leave [the_person.possessive_title] to get cleaned up and get back to work."
                        $ the_person.apply_planned_outfit()

                    "No thanks":
                        "You thank her for the offer, but decide against it for now."

        "Not right now":
            "You thank her for the help, but decide against it for now."
    return


#SBS50
label starbuck_arousal_reduction_one_label(the_person):
    $ global SB_MOD_MC_AROUSAL_MULT
    "You explain to [the_person.possessive_title] that you feel like you're having trouble pleasing the women you've been with lately. You ask if she has anything that can help you last longer during sex"
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of numbing creams and similar products."
    the_person "While there are a ton of products on the market to help with you are talking about, the one I've gotten the best feedback from is this one."
    "[the_person.possessive_title] picks a cream off the shelf. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person "I have gotten a lot of good reviews from men... and their women! It's made so you only have to apply it once a day, and just gives a slight numbing effect."
    the_person "Perfect to last just a bit longer, no matter when you have sex that day!"
    menu:
        "Purchase ($500)":
            $ mc.business.change_funds(-500)
            $ SB_MOD_MC_AROUSAL_MULT = SB_MOD_MC_AROUSAL_1ST_MULT
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
            "Before you leave, you take a look at the instructions. Hopefully this will help let you last longer! You head to the bathroom and apply a little bit of it."
            "NOTE: You now gain arousal at 90 percent of the normal rate"
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

#SBS60
label starbuck_arousal_reduction_two_label(the_person):
    #TODO you offer to make dinner. It takes up time, but you can slip serum to your mom and sister.
    $ global SB_MOD_MC_AROUSAL_MULT
    "You explain to [the_person.possessive_title] that you feel like you're still having trouble pleasing the women you've been with lately, even with the numbing cream. You ask if she has anything that can help you last longer during sex"
    the_person "Oh [the_person.mc_title], I have just the thing to help!"
    "[the_person.possessive_title] leads you over to an area of the store where she sells a number of pharmaceutical products."
    the_person "While there are a ton of products on the market to help with you are talking about, the one I've gotten the best feedback from is this one."
    "[the_person.possessive_title] picks a pill off the shelf. You eye the price tag warily"
    mc.name "I dunno... is it really worth that much?"
    the_person "This company has made a ton of advances in this area recently!"
    the_person "They've done numerous double blind studies. Almost all men who took it daily found they lasted longer in bed!"
    menu:
        "Purchase ($5000)":
            $ mc.business.change_funds(-5000)
            $ SB_MOD_MC_AROUSAL_MULT = SB_MOD_MC_AROUSAL_2ND_MULT
            the_person "Oh! I'll ring this right up. You won't regret it, [the_person.mc_title]!"
            "[the_person.possessive_title] hands you your purchase after she rings you up. She smiles at you and blushes a bit."
            "Before you leave, you take a look at the instructions. You take a pill out and swallow it with a quick gulp of water."
            "NOTE: You now gain arousal at 75 Percent of the normal rate"
        "Not right now":
            "You thank her for the help, but decide against it for now."
    return

label starbuck_sex_store_investment_one_label(the_person):
    mc.name "So, I'm seriously considering investing in your shop. What kind of stock can you get if I invest $1000?"
    the_person "Oh! That would be amazing! Well, with that money, I could get basic toys, creams, and lubricants. There are some pretty good creams for male endurance enhancement you can get..."
    the_person "As well as some toys for better foreplay and masturbation. Some dildos, male masturbation sleeves, vibrating rings..."
    "That sounds like a pretty good list of stuff that you would be interested in buying if you were to go to a sex shop."
    "Do you want to invest?"
    menu:
        "Invest ($1000)":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.change_funds(-1000)
            $ the_person.change_stats(obedience = 5, happiness = 20)
            the_person "Don't worry, [the_person.mc_title]! You won't regret this!"
            "Even if the business winds up flopping, in your heart you know you are doing the right thing, helping this widow achieve her dream of owning a sex shop."
            $ starbuck.event_triggers_dict["shop_investment_total"] += 1000
            $ starbuck.event_triggers_dict["shop_investment_basic_total"] += 1000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 1
            $ starbuck.event_triggers_dict["shop_investment_rate"] = 1.0
            $ starbuck.event_triggers_dict["shop_stage_one_day"] = day
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

label starbuck_sex_store_investment_two_label(the_person):
    "While things at [the_person.possessive_title]'s sex shop have definitely picked up, you can't help but notice there are several sections of the store that lack variety."
    "There are some dildos, but only a couple varieties. Same with condoms, lubricants, and other items."
    "You decide to bring it up with [the_person.possessive_title]."
    mc.name "Hey [the_person.title]. I see things are going good around here, but I'm curious. You've got basic items around the store, but why don't you have more variety?"
    "She frowns and responds."
    the_person "Well, I'd love to have more variety, but unfortunately I'm not bringing in very much profit. I'm in the black now, thanks to your investment, but I'm not really making enough to expand inventory significantly."
    "You watch as a customer comes in the store. He looks around for a bit, then leaves. You wonder how much business you are missing out on due to the lack of stock."
    mc.name "Have you done any research on what it would take to get more variety in?"
    "She nods."
    the_person "I have. And it's too much for me to ask from you. You've already done so much for me and shop..."
    "You interrupt her."
    mc.name "How much?"
    "[the_person.possessive_title] clears her throat."
    the_person "Well, the way I added it up, to expand beyond just basic stock, and include a variety of novelty items, edibles, and accessories would be about $5000."
    "You consider the amount. It is steep, to be sure, but it also might be a good investment."
    if get_shop_investment_rate() == 3.0:
        "It might also open up new opportunities with [the_person.possessive_title]. You wouldn't mind a few more excuses to get intimate with her..."
    "Do you want to invest?"
    menu:
        "Invest ($5000)":
            "You discuss with [the_person.possessive_title] for a while what the terms of your investment are. Once you are both happy, you write her a check from your business account."
            $ mc.business.change_funds(-5000)
            $ the_person.change_stats(obedience = 5, happiness = 20, love = 5)
            the_person "Wow... are you really doing this? I can hardly believe it. Don't worry, I won't let you down!"
            "Even as you write your check, she is already going on about the stock she'll be able to get."
            the_person "... hmmm... OH! And edible underwear! And nipple clamps! Maybe some handcuffs..."
            $ mc.change_locked_clarity(20)
            $ starbuck.event_triggers_dict["shop_investment_total"] += 5000
            $ starbuck.event_triggers_dict["shop_investment_advanced_total"] += 5000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 2
            "She is so excited, you can tell already, this is an investment that is going to pay off for you... one way or another!"
            $ starbuck.event_triggers_dict["shop_stage_two_day"] = day
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

label starbuck_sex_store_investment_three_label(the_person):
    "You take a look around at the sex shop. You see a sexy looking redhead checking out some lingerie. In the back corner is a guy looking at strapons. In an aisle you see a couple looking at edibles."
    "Everyone seems to be shopping and finding what they are looking for... but you can't help but have a nagging in you head that you could make the store even better."
    mc.name "Hey [the_person.title]. Looks like things are going great here, how is business?"
    the_person "Oh, it's been great! I've been meeting so many new people, and I'm actually making a decent income now!"
    "She gives you a warm smile. It nice seeing her so happy with her work."
    mc.name "Are you pretty happy with all the stuff you are able to keep in stock now? Seems like you've got just about anything you could ever need."
    the_person "Well, I don't know about EVERY thing, but we definitely have a great selection now."
    mc.name "What do you mean?"
    the_person "Well, goodness, there is so much stuff out there, there's no way we could fit it all in this little store. That's why I'm saving up."
    the_person "The store next to us recently went out of business, once I save up enough money, I'm gonna buy it out and expand my store. Turn this place into [the_person.fname]'s MEGA sex shop!"
    "You consider what she is saying."
    mc.name "What kind of stuff could you carry with the extra space that you aren't carrying now?"
    the_person "Oh, well in here we sell mostly accessories, lingerie, that kind of thing, but with more room we could get in all kinds of kinky stuff. Sex furniture, like chairs and swings, massage tables..."
    "Wow, you had no idea there was so much stuff out there..."
    the_person "... could even get into bondage gear, fetish items like furry tail butt plugs... I mean, the sky is the limit, you know?"
    "So far, all of your investments in the shop have paid off... plus, you start to imagine what it would be like to try some of these items with [the_person.possessive_title]..."
    mc.name "Let's say I was interested in investing again... How much would you need to make all that happen?"
    "[the_person.possessive_title]'s mouth drops in surprise."
    the_person "Well... my estimates put it at about $15000. But please, don't think you have to do that! I'm making decent money, I'll be able to afford it eventually..."
    "You consider the investment."
    menu:
        "Invest ($15000)":
            mc.name "How about this. You've done an incredible job managing this place. How about if I front the money, and from now on we're partners?"
            the_person "Wow... partners?... I mean... you're talking business partners, right?"
            if get_shop_investment_rate() > 3.0:
                mc.name "[the_person.title], I'd be lying if I said I don't thoroughly enjoy the time we've spent together. So yeah, we would be business partners, but I'd also love the excuse to spend more time with you."
                $ the_person.draw_person(emotion = "happy")
                if starbuck.love > 60:
                    the_person "Oh, [the_person.mc_title]... I'm so glad to hear that. I feel the same way."
                else:
                    the_person "Wow... that's nice to hear! I'm interesting in spending more time with you in the future too."
            else:
                mc.name "Of course, we'll keep things perfectly professional..."
            $ mc.business.change_funds(-15000)
            $ the_person.change_stats(obedience = 10, happiness = 20, love = 10)
            the_person "Wow... this is it! The opportunity of a lifetime. I'm speechless [the_person.mc_title]. Thank you so much!"
            "Even as you write your check, she is beginning to plan the expansion to the shop."
            $ starbuck.event_triggers_dict["shop_investment_total"] += 15000
            $ starbuck.event_triggers_dict["shop_investment_fetish_total"] += 15000
            $ starbuck.event_triggers_dict["shop_progress_stage"] = 3
        "Reconsider":
            "You decide you need more time to consider the investment."
            mc.name "Sorry, [the_person.title], I haven't made up my mind yet. Thanks for the info though, I'll be back when I've reconsidered."
            "[the_person.possessive_title] frowns, but she nods in understanding."
            the_person "Of course, [the_person.mc_title]. It is a lot of money we are talking about, you should be careful with your hard earned money!"
    return

init 2 python:
    def starbuck_promo_classic_black_lingerie():
        outfit = Outfit("Lingerie Set Classic Black")
        outfit.add_upper(lace_bra.get_copy(),colour_black)
        outfit.add_lower(lace_panties.get_copy(), colour_black)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_black)
        outfit.add_feet(high_heels.get_copy(), colour_black)
        return outfit

    def starbuck_promo_blue_nightgown_lingerie():
        outfit = Outfit("Lingerie Set Blue Nightgown")
        outfit.add_upper(nightgown_dress.get_copy(), colour_sky_blue)
        outfit.add_lower(cute_panties.get_copy(), colour_sky_blue)
        outfit.add_feet(thigh_highs.get_copy(),colour_sky_blue)
        outfit.add_feet(sandle_heels.get_copy(), colour_sky_blue)
        return outfit

    def starbuck_promo_pink_onepiece_lingerie():
        outfit = Outfit("Lingerie Set Pink Onepiece")
        outfit.add_upper(lacy_one_piece_underwear.get_copy(),colour_pink)
        outfit.add_feet(fishnets.get_copy(), colour_pink)
        outfit.add_feet(pumps.get_copy(), colour_pink)
        return outfit

#SBS70
label starbuck_sex_store_promo_one_label(the_person):
    the_person "Well, it is going okay. Thanks to your investment, I'm finally turning a profit at least!"
    the_person "But, I feel like I'm just not getting the foot traffic I need. I need to find a way to attract more customers."
    "You consider what she is saying. Given the nature of the store, what you really need is some seriously sexy advertising."
    "You check out [the_person.possessive_title]. She has an amazing body. Maybe you should get her to pose with some of her product, take some pictures and turn it into an ad!"
    "[the_person.possessive_title] sees you checking her out, and the wheels turning in your head as you think about it."
    $ mc.change_locked_clarity(5)
    the_person "[the_person.mc_title]? Are you still with me here? Or are you too busy checking me out?"
    "You give her a smile as a plan comes together."
    mc.name "I know just what you need to do [the_person.title], that will help drive traffic here. You need to do some advertising!"
    "[the_person.possessive_title] shakes her head."
    the_person "I do, but it doesn't seem to be very effective."
    mc.name "That's right, because your advertising is so plain! What you need to do is get a sexy woman in your advertising, in some lingerie, showing off some of the products you have for sale!"
    "She thinks about your proposal."
    the_person "That sounds great, [the_person.mc_title], but... where am I going to find a model for something like that? Let alone pay her?"
    "You pretend to think hard about it."
    mc.name "Well, [the_person.title], I think YOU are pretty fucking sexy..."
    "[the_person.possessive_title] quickly realizes you are suggesting that she dresses up in lingerie for some advertising."

    if the_person.sluttiness > 50 : #We easily pass the sluttiness check.
        the_person "Oh! I mean, that would be fun for sure... but... do you really think I'm sexy enough for that?"
        "You give her another once over."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        $ mc.change_locked_clarity(10)
        the_person "Hmm... okay! If nothing else, I'll have some nice pictures I can send to guys who hit me up on my dating app..."
    elif the_person.sluttiness > 20 :  #Barely passes the sluttiness check.
        the_person "Oh... I don't know [the_person.mc_title]. I mean, believe me, I love sex, I even opened a shop... But to put myself out there in public like that? Are you sure I'm sexy enough for that?"
        "You make a show of checking her out."
        mc.name "Absolutely. If I was a guy and I saw you in some lingerie on an advertisement, I'd be sure to come check the store out!"
        $ mc.change_locked_clarity(10)
        the_person "Hmm... okay, I mean, we can give a shot anyway. What's the worst that could happen?"
    else: #She fails the sluttiness check. Give dialogue to come back when shes sluttier.
        the_person "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there in public like that?"
        "[the_person.possessive_title] considers for a bit."
        the_person "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready for something like that. Maybe at some point in the future she'd be willing to do something like that."
        return

    $ the_person.wardrobe.add_underwear_set(starbuck_promo_classic_black_lingerie())
    $ the_person.wardrobe.add_underwear_set(starbuck_promo_blue_nightgown_lingerie())
    $ the_person.wardrobe.add_underwear_set(starbuck_promo_pink_onepiece_lingerie())

    "Yes! [the_person.possessive_title] is gonna show off her amazing body of hers while you take pictures!"
    $ mc.change_locked_clarity(20)
    "You coordinate with her on the items you want to advertise and some outfits that would be suitable to show them off."
    #Pose walking away#
    "You collect the items, while [the_person.possessive_title] grabs a few sets of lingerie. You meet her in the back room."
    #pose standing#
    "Once in the backroom, you can see that [the_person.possessive_title] has three outfits picked out. Some classic black lingerie with fishnet and garter belt, a light blue nightgown, and a pink lacy one piece."
    "The first item to model is a bottle of some good quality, oil based lube. You figure a regular standing pose should work for this."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie())
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie())
            $ the_person.draw_person()
        "The pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie())
            $ the_person.draw_person()
    $ the_person.break_taboo("underwear_nudity")
    "Now dressed in her outfit, [the_person.possessive_title] hands you her phone. She grabs the first item, the bottle of lubricant."
    $ mc.change_locked_clarity(20)
    mc.name "Wow... you look great..."
    "You murmur. She smiles at your compliment."
    mc.name "Okay, why don't you just stand and put your hand on your hip."
    $ starbuck.draw_person(position = "stand4", emotion = "happy")
    "[the_person.possessive_title] strikes a pose for you. You take several pictures, trying to find the best angles to show off her body... and the product."
    "You can tell that [the_person.possessive_title] is actually enjoying herself and your attention. Her cheeks are starting to get a little flushed."
    $ the_person.change_arousal(15)
    "The next item for her to model will be a male masturbation sleeve."
    "It is designed to look like a famous porn actress' asshole, so you figure to model this product, [the_person.possessive_title] should have her back to you."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie())
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie())
            $ the_person.draw_person()
        "The pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie())
            $ the_person.draw_person()
    "Now dressed in her outfit, [the_person.possessive_title] looks to you for direction."
    $ mc.change_locked_clarity(25)
    mc.name "[the_person.title]. You look incredible..."
    "She clears her throat to get your attention."
    mc.name "Right! Why don't you turn around and peek back at me and hold this to the side, right next to your hip."
    $ starbuck.draw_person(position = "back_peek", emotion = "happy")
    "[the_person.possessive_title] turns around and looks back at you. You get a bunch of pictures of her amazing ass. You almost forget to get pictures of the product!"
    mc.name "Perfect! These pictures are perfect, you are going to get a flood of guys in here looking for this!"
    "Once you are done [the_person.possessive_title] turns back to face you."
    $ starbuck.draw_person(position = "stand2", emotion = "happy")
    $ the_person.change_arousal(30)
    "The attention you are giving her is really starting to excite [the_person.possessive_title]. You can see her nipples sticking out proudly in her outfit."
    "The last item for her to model is a dildo. You figure since you are mainly targeting a male audience with this advertisement, a good pose for her would be on her knees, like she's getting ready to put it in her mouth."
    "Which lingerie should you have her use for this?"
    menu:
        "The classic black set":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_classic_black_lingerie())
            $ the_person.draw_person()
        "The blue nightgown":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_blue_nightgown_lingerie())
            $ the_person.draw_person()
        "The pink one piece":
            "[the_person.possessive_title] starts to strip down."
            $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
            "Once she finishes stripping, she grabs the lingerie set and puts it on."
            $ the_person.apply_outfit(starbuck_promo_pink_onepiece_lingerie())
            $ the_person.draw_person()
    "As she changes you stand and gawk at her amazing body."
    $ mc.change_locked_clarity(30)
    the_person "Don't worry [the_person.mc_title], we're almost done. What should I do for this one?"
    mc.name "I think you should get down on your knees, you know, like you are getting ready to suck on it."
    the_person "Oh! That sounds like fun... sucking on a... a dildo, right!"
    $ starbuck.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets down on her knees. She looks at the dildo longingly. You take multiple pictures of her."
    $ the_person.change_arousal(45)
    the_person "Mmm... it looks so tasty..."
    $ mc.change_arousal(15)
    "[the_person.possessive_title] opens her mouth, and slowly starting to run her tongue along the dildo. You see one of her hands slowly drift down between her legs and she begins to touch herself."
    "She has her eyes closed, so you snap a few more pictures of her sucking on the dildo. She suddenly realizes what she is doing and pulls off."
    the_person "Right! So, I thought maybe a picture like that... I mean maybe we could include a picture like that free with every purchase... or something?"
    "You can tell she is fumbling with her words, trying to cover up that she lost her awareness and started sucking on the dildo."
    "You are all done with the pictures... maybe you should offer her something else to suck on?"
    menu:
        "Want a real dick?":
            "[the_person.possessive_title] looks up at you, still on her knees."
            the_person "Oh [the_person.mc_title], getting all dressed up has me all turned on. If you'd let me do that, I would really appreciate it."
            $ the_person.add_situational_slut("Excited", 20, "I want to suck your cock")
            mc.name "Go ahead, you look amazing. I can't wait to feel your mouth."
            $ mc.change_locked_clarity(50)
            "You walk up to [the_person.possessive_title]. She unzips your pants and pulls your cock out from your pants."
            "She runs her tongue up and down the sides a few times, then opens her mouth and sucks you into her hot mouth."
            $ the_person.break_taboo("sucking_cock")
            call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBS70
            $ the_report = _return
            if the_report.get("girl orgasms", 0) > 0:
                "[the_person.possessive_title] takes a few minutes to recover from her orgasm. Eventually she gets up."
                "Giving [the_person.title] an orgasm makes you feel more confident in your foreplay skills."
            else:
                "After you finish, [the_person.possessive_title] takes a second, then gets up."
            $ the_person.clear_situational_slut("Excited")
            $ perk_system.add_stat_perk(Stat_Perk(description = "Increase foreplay skill after helping Starbuck with her advertisement photos. +1 Foreplay Skill", foreplay_bonus = 1, bonus_is_temp =False), "Starbuck Foreplay Bonus")
            $ starbuck.draw_person(position = "stand2", emotion = "happy")
            the_person "Mmm... That was nice. It's been a while since I sucked on a hard cock. It was kinda nice!"
            if the_person.get_opinion_score("giving blowjobs") < 1:
                $ the_person.update_opinion_with_score("giving blowjobs", 1)
            "You are still recovering from your orgasm. You take a look at her phone and start looking at the pictures you got."
            the_person "If this advertisement works, we'll have to make more right?"
            mc.name "Definitely. Alright, I'll go ahead and get some advertisements done, and we'll see if we can't get better foot traffic in here."
            if perk_system.has_item_perk("Dildo"):
                pass
            else:
                "[the_person.possessive_title] looks at the dildo she was modeling for a few minutes ago."
                the_person "Hey... I probably shouldn't sell this in the store anymore. Do you want it?"
                "You consider... what would you need a dildo for?"
                the_person "I know you may not use it on yourself, but, you never know when a toy like this can spice up an encounter."
                mc.name "That's true. Sure, I'm sure I could find a use for it."
                $ dildo_unlock()
                "You are now the proud owner of a dildo."
                the_person "Maybe even use it on me sometime..."
            "You say goodbye to [the_person.possessive_title] and head out. You look through the pictures again."
            "With pictures like these, you are sure the business here will increase."
        "Give her some privacy":
            "You decide to give her some time to yourself. You use her phone to forward all the pictures you took to your account."
            mc.name "Okay, those should be good. I'll go ahead and get some advertisements done, and we'll see if we can't get better traffic in here."
            "You say goodbye to [the_person.possessive_title] and head out. With pictures like these, you are sure the business here will increase."

    python:
        the_person.event_triggers_dict["shop_investment_rate"] = 2.0
        the_person.apply_planned_outfit()
        mc.location.show_background()
        clear_scene()
    return #Toy modeling, ends in blowjob

#SBS80
label starbuck_sex_store_promo_two_label(the_person):
    the_person "Oh, business is going pretty good! I have definitely been getting more traffic ever since... you know... helped me with some advertising flyers."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person "And it's been nice, all the attention I've been getting from the guys that come in here."
    the_person "But, it's only guys coming in! I feel like I'm really missing market share, but I can't figure out a way to get more women in here!"
    "You consider her problem for a bit. Then you come up with an idea."
    mc.name "Have you ever considered doing reviews of the products you carry?"
    "She pauses and looks at you."
    the_person "I'm not sure what you mean."
    mc.name "Well, for example, that dildo over there. If I'm a girl, how do I know how well it's going to hold up? Is it going to hit all the right places? Is it easy to clean?"
    "[the_person.possessive_title] thinks about what you are saying."
    mc.name "What we could do is, take a video of yourself trying out the product. We post it online, and make sure people know, come get it here!"
    the_person "So... you're basically saying, I should take a video of myself... using dildos? And post it online?"
    #Sluttiness Check!
    if the_person.sluttiness > 70 : #We easily pass the sluttiness check.
        $the_person.draw_person(emotion = "happy")
        the_person "Oh! That's an amazing idea! I could put QR labels next to the tags too, so people can scan it with their phone and check it out!"
        "[the_person.possessive_title] seems to really like the idea."
        mc.name "Hey, that's a good idea too! Let's do it!"
    elif the_person.sluttiness > 40 :  #Barely passes the sluttiness check.
        the_person "Oh... I don't know [the_person.mc_title]. I mean, it sounds like it would work... but videos of me, on the internet? Using sex toys?"
        "You do your best to reassure her."
        mc.name "Absolutely. I mean, when have I steered you wrong? The last idea worked too, didn't it?"
        the_person "Hmm... okay. Let's do it!"
    else: #She fails the sluttiness check. Give dialogue to come back when shes sluttier.
        the_person "Wow, [the_person.mc_title]. I'm sorry I just... I don't think I could do that. To put myself out there on the internet like that?"
        "[the_person.possessive_title] considers for a bit."
        the_person "No, I'm sorry [the_person.mc_title]. It's a great idea, I just don't think I'm ready to do something like that. I'm sorry!"
        "You understand she's just not ready. Maybe at some point in the future she'd be willing to do something like that."
        return
    "[the_person.possessive_title] looks at you for a moment."
    the_person "So... You're going to help me... right? I mean, I'm sure I could figure it out eventually, but it would be really nice to have someone help me make the first couple..."
    "You consider her request. It sounds pretty reasonable, plus maybe you'll get to watch her masturbate!"
    $ mc.change_locked_clarity(10)
    mc.name "Sure, I'd be glad to help! Any idea which products you would like to review first?"
    the_person "Yeah, I've got a pretty good idea. Meet me in the back in a few minutes while I get everything together!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks away. You see her going around and grabbing a few things from around the store. You decide to head to the back room and wait for her there."
    $ SB_advert_four_outfit = Outfit("Lingerie Set Dark Blue Corset")
    $ SB_advert_four_outfit.add_upper(corset.get_copy(),[0.15, 0.2, 0.45, 1])
    #$ SB_advert_four_outfit.add_lower(lace_panties.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(garter_with_fishnets.get_copy(), [0.15, 0.2, 0.45, 1])
    $ SB_advert_four_outfit.add_feet(heels.get_copy(), colour_black)
    $ the_person.draw_person(position = "stand2")
    "She joins in the backroom carrying a couple of dildos and a set of lingerie."
    the_person "Okay, let me just get changed really quick."
    $ the_person.strip_outfit(position = "stand2", exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Once she finishes stripping, she grabs the lingerie set and puts it on."
    $ the_person.apply_outfit(SB_advert_four_outfit)
    $ the_person.draw_person()
    $ the_person.wardrobe.add_outfit(SB_advert_four_outfit)
    $ del SB_advert_four_outfit
    $ mc.change_locked_clarity(20)
    "You check out [the_person.possessive_title] in her outfit. Damn she looks hot!"
    the_person "Okay, so here's what I'm thinking..."
    "[the_person.possessive_title] starts going over the details of how she wants to do it. You take mental notes. Soon you are ready to begin."
    "You get the camera recording as [the_person.possessive_title] begins her reviews."
    $ the_person.draw_person(position = "stand4")
    the_person "Hello! This is [the_person.fname]! Owner of [the_person.fname]'s sex shop, and welcome to my review of the Ramboner dildo by..."
    "You check to make sure she is in frame. She talks for a few minutes about the quality of the toy."
    the_person "Okay! Time to try it out!"
    $ the_person.draw_person(position = "missionary")
    "[the_person.possessive_title] lays down on the floor. She begins by stroking herself with the dildo a few times up and down her slit."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(20)
    the_person "Mmm, that texturing feels great sliding up and down, let's see how it feels going in..."
    "She slowly takes the head of the dildo and begins pushing it into her pussy."
    the_person "Oh! Wow the curve on the tip feels great sliding in..."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title] begins working the dildo in and out of her."
    the_person "Yes! And with the flared base, it's easy to hold... so I can control the depth... oh fuck!"
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "She is working the dildo in and out of herself now at a steady pace. Each time she pulls it out, you can see her juices glistening on the toy."
    the_person "The texturing on the outside... it really... stimulates the nerve endings as it... oh god."
    $ the_person.change_arousal(15)
    "[the_person.possessive_title] is now fucking herself earnestly with the dildo. The sights and sounds are starting to turn you on. You absentmindedly begin to stroke yourself through your pants."
    the_person "Okay... now seems like a good time to test the curve, and see how well it stimulates the g-spot."
    "She pulls the dildo mostly out, then changes the angle of penetration. She gives herself short, shallow thrusts, focusing on her g-spot."
    the_person "YES! Okay this toy stimulates the g-spot... SO GOOD."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] looks up and notices you stroking yourself. Her mouth goes wide in a moan as her orgasm approaches."
    "She looks directly at you and cries out."
    the_person "YES! OH god, fuck me... YES! FUCK ME!!!"
    $ the_person.change_arousal(25)
    $ mc.change_locked_clarity(50)
    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
    $ the_person.have_orgasm()
    "[the_person.possessive_title]'s body begins to spasm as she orgasms. She shoves the toy in deep inside her. Her juices are trickling down beneath her out of her cunt."
    "Her body relaxes after she finishes. She slowly pulls the toy from her sopping wet cunt."
    the_person "So... overall... I rate this toy... a solid 9 out of 10... thanks for watching!"
    $ the_person.event_triggers_dict["shop_investment_rate"] = 3.0
    "You step out from behind the camera. Her sultry eyes look up at you as you walk over to her."
    if (the_person.love > 50):
        the_person "Oh [the_person.mc_title]. That toy was so good... but honestly the whole time I was imagining it was you fucking me..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person "Don't get me wrong, toys are great, but I want you! Seeing you touching yourself... looking at me... Please fuck me [the_person.mc_title]!"
    else:
        the_person "Damn [the_person.mc_title]. I'm glad you were enjoying the show..."
        "She pushes herself up on her elbows, but makes no motion to stand up."
        the_person "Toys are great... but nothing beats a real cock inside me. Would you please fuck me [the_person.mc_title]?"
    $ mc.change_locked_clarity(30)
    menu:
        "Fuck Her":
            mc.name "[the_person.title], that was so hot! I can't wait to bury myself into your amazing cunt."
            "She smiles at your response."
            the_person "Then come get some! I just came, no need to warm me up!"
            "You quickly strip out of your clothes and lay down on top of her."
            $ mc.change_locked_clarity(20)
            if (the_person.love > 50):
                "[the_person.possessive_title] wraps her arms around you and holds you close. You move your face in for a kiss and she greedily accepts your tongue in your mouth."
                "While you make out with her, you use one hand to get yourself lined up with her soaked slit. You slide in easily with no resistance, bottoming out inside her."
            else:
                "[the_person.possessive_title] runs her hands along your sides as you get into position."
                "She grabs your cock with your hand and points it at her soaked slit. With one smooth motion you thrust into her. She's so wet you glide in with no resistance."
            $ the_person.break_taboo("condomless_sex")
            $ the_person.break_taboo("vaginal_sex")
            "Wasting no time, you begin thrusting into her. Her pussy feels amazing wrapped around you."
            call fuck_person(the_person, start_position = missionary, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_fuck_person_SBS80
            "[the_person.possessive_title] lays there in a daze. Between the toy and your cock, she had multiple orgasms."
            if (the_person.love > 50):
                "As your start getting dressed again, out of the corner of your eye you see [the_person.possessive_title] begin to shudder."
                "You see a tear roll down one of her eyes."
                the_person "Thank you [the_person.mc_title]... It means so much to me, everything you've done for me... and for the shop."
            else:
                "You get up and start getting dressed. [the_person.possessive_title] calls out to you."
                the_person "Thank you [the_person.mc_title], for all your help. I wouldn't have made it this far without you."
            mc.name "Thanks, [the_person.title]. It has been a pleasure helping you out. Please let me know if you'd like... help... again in the future with your reviews!"
            $ the_person.change_stats(love = 5, happiness = 10, slut = 1, max_slut = 50)
            $ perk_system.add_stat_perk(Stat_Perk(description = "Increase vaginal skill after helping Starbuck with her demonstration video. +1 Vaginal Skill", vaginal_bonus = 1, bonus_is_temp =False), "Starbuck Vaginal Bonus")
            "Fucking and pleasing an experienced woman like [the_person.title] makes you feel more confident in your vaginal skills."
            "You go back and take a look at the camera. You accidentally left it recording! It has a recording of you and [the_person.possessive_title] fucking!"
            "You decide you should probably just be honest and tell her."
            mc.name "So... I accidentally forgot to stop the camera... it caught the whole scene of us having sex."
            the_person "Oh! Let me see!"
            $ the_person.draw_person(position = "stand2")
            "[the_person.possessive_title] hops up and takes a look at the camera."
            the_person "Oh my... this is hot... I didn't think I would like this but... it's kinda hot watching yourself on video get fucked..."
            "You raise an eyebrow. Is she starting to like showing off a bit?"
            if the_person.get_opinion_score("public sex") < 1:
                $ the_person.update_opinion_with_score("public sex", 1)
            "You chat with her for a few minutes about the details of setting up a review site, but eventually it's time to say goodbye."
            the_person "Thanks again for everything [the_person.mc_title]. Don't be a stranger now!"
        "Refuse":  #Lol really? I guess some people may not have the energy.
            mc.name "Sorry, I've had a long day, and I should probably get to work on editing this video."
            "She seems surprised by your answer."
            the_person "Oh... right, I'm sure that's going to be a lot of hard work..."
            "You chat with her for a few minutes about the details of setting up a review site, but eventually it's time to say goodbye."
            the_person "Thanks for the help [the_person.mc_title], if you find yourself needing anything later... just ask okay?"
            $ the_person.change_stats(love = -5, happiness = -5, slut = -1)

    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    return #Masturbation, ends in sex

#SBS90
label starbuck_sex_store_promo_three_label(the_person): #Cunnilingus, ends in rough sex
    the_person "Oh, business is great! I'm definitely getting more women in here now."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person "The interest has been booming now for masturbation tools, but one thing I've noticed as I've had customers come in, as well as my sales..."
    the_person "A huge percentage of my sales are to singles. I get almost no couples in here shopping together."
    "You consider her problem for a bit, but it is actually her that comes up with an idea first."
    the_person "So, I was thinking, maybe for my next video review you could umm,  you know, help me demonstrate something?"
    "She looks at you hopefully. This is an easy decision."
    mc.name "Absolutely. It's only fair. You've already put yourself out there, I'm ready to do my part."
    "[the_person.possessive_title] gives you a bright, beaming smile."
    the_person "Yes! Okay! Give me minute I'll meet you in the back! Get the camera ready!"
    "You make your way to the back. You get the camera set up and ready to go."
    $ SB_advert_five_outfit = Outfit("Lingerie Just Red Panties")
    $ SB_advert_five_outfit.add_lower(panties.get_copy(), colour_red)
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title] enters the room."
    the_person "Ok, I figure we can get through a couple things... I have a pair of edible panties, and a nice set of fuzzy handcuffs..."
    "Wow... so at her suggestion, you are about to eat panties off of [the_person.possessive_title]... and then hand cuff her... all on camera."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title] starts to strip down."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she grabs the panties and puts them on."
    $ the_person.apply_outfit(SB_advert_five_outfit)
    $ the_person.draw_person()
    $ the_person.wardrobe.add_underwear_set(SB_advert_five_outfit)
    $ del SB_advert_five_outfit
    "[the_person.possessive_title] stands before you almost completely exposed, her incredible body is on full display."
    $ mc.change_locked_clarity(30)
    if starbuck.love > 50:
        the_person "Do you think that before we get started, maybe you could just hold me for a little bit?"
        "You step up to her. Your hands go to her waist and she wraps her arms around you."
        $ the_person.draw_person(position = "kissing")
        the_person "Mmm... it feels so good when you hold me."
        "She looks up into your eyes. Your bring your face down to hers and begin to kiss. Her lips open submissively to allow your tongue to invade her mouth."
        "You embrace each other for a while, just enjoying the heat and softness of her skin."
        the_person "Okay, are you ready to get this started?"
    else:
        the_person "You just gonna watch? Or are you ready to get started?"
    "You walk over and start up the camera. You give her a nod to show her that it's running."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review another couple of products."
    the_person "Today, we are going to review a couple of products meant for couples! So today I've asked a friend to be here to help me review them..."
    "You step into frame next to [the_person.possessive_title]."
    the_person "This is [the_person.mc_title], and we are going to review some edible underwear by Skinworks, and some neat fuzzy handcuffs by PowerTrips Inc..."
    "[the_person.possessive_title] gives some of the details on the products."
    the_person "Ok, I guess we're ready to get started! Are you ready [the_person.mc_title]?"
    "You nod. [the_person.possessive_title] lays down in the table and spreads her legs, angled in such a way that the camera can get a good view of her barely hidden pussy."
    $ the_person.draw_person(position = "missionary")
    "You get down on your knees between her legs. You kiss and lick up along her leg, working your way up to her pussy."
    "When you reach her mound, you stop and breath deeply in through your nose, savoring the musky scent of her sex."
    "[the_person.possessive_title] runs her hands through your hair, gently urging your face down into her edible panty clad cunt."
    $ mc.change_locked_clarity(20)
    "You push your face into her mound, and begin to nibble at the gummy panties that are between your tongue and [the_person.possessive_title]'s sweet cunt."
    $ the_person.change_arousal(10)#10
    the_person "Mmm, how do they taste, [the_person.mc_title]?"
    "You give her a loud MMMmmm of approval."
    "You are starting to make good size holes in the cherry flavored covering. One is close enough to her slit, you are able to snake your tongue through it and along her moist fuckhole."
    $ the_person.change_arousal(10)#20
    $ mc.change_locked_clarity(20)
    the_person "Oh! Mmm, that felt good. These panties would be good if you had a significant other who... maybe doesn't usually like to go down on you..."
    "You chew the hole a little wider. You can now access her clit easily through the hole. You take the opportunity to roll her clit between your lips for a few seconds before resuming your panty eating."
    $ the_person.change_arousal(15)#35
    the_person "Oooohhhhh, he just go through to my clit... Mmmm, that feels so good."
    "[the_person.possessive_title] reaches down and tears a piece off her panties, now giving you almost free reign to eat her pussy."
    the_person "Okay, let's see how they taste..."
    $ play_swallow_sound()
    "She takes a bite of the panties, chews and swallows. While she does that you push your tongue deep into her cunt."
    $ the_person.change_arousal(15)#50
    $ mc.change_locked_clarity(30)
    the_person "Yes! Mmm, they actually taste pretty good, I can see why [the_person.mc_title] here is so eager..."
    $ strip_choice = the_person.choose_strip_clothing_item()
    $ the_person.draw_animated_removal(strip_choice)
    $ the_person.draw_person(position = "missionary")
    "Her panties now in shreds, [the_person.possessive_title] gathers what is left of them and pulls them off."
    $ the_person.change_arousal(20)#70
    "[the_person.possessive_title]'s juices are beginning to flow freely from her slit. You lap them up before circling your tongue around her clit a few times."
    "After licking at her clit, you move your tongue down to her entrance. You push your tongue up inside her as far as it will go."
    $ the_person.change_arousal(10)#80
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] has stopped providing commentary and is now just moaning and encouraging you."
    the_person "Oh [the_person.mc_title]! That feels so good..."
    "She starts to rock her hips, grinding herself against your face."
    $ the_person.change_arousal(10)#90
    "[the_person.possessive_title] is bucking her hips wildly as you lick her. Suddenly, she grabs the back of your head and gasps."
    $ the_person.change_arousal(20)#110
    $ the_person.call_dialogue("climax_responses_oral")
    $ the_person.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(30)
    "Her pussy is drooling wet as she climaxes. She paws at the table, trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down a bit and lap up her sweet, creamy juices."
    the_person "Oh fuck [the_person.mc_title], your tongue feels so good. Wow!"
    "You slowly push yourself back from her pussy. [the_person.possessive_title]'s juices are dripping down your chin. You lick up as much as you can."
    the_person "Ok... wow... so, moving on... you know... to the handcuffs..."
    "You step over and grab the handcuffs. They having linings on them so they are nice and soft, but you can tell that underneath the cloth lining is strong steel. They feel very sturdy."
    the_person "That was great for when you want to get your pussy eaten... as my incredibly able assistant just showed, but these, they are good for when you want your man to take control."
    $ the_person.draw_person(position = "sitting")
    "You approach [the_person.possessive_title] with the handcuffs. She sits up and puts her hands behind her back. As you put the handcuffs on her hands, she whispers in your ear."
    the_person "[the_person.mc_title] that was amazing. I want you to be rough with me now. Don't worry, I can take it, and I want to show off how sturdy the cuffs are for the camera..."
    $ mc.change_locked_clarity(30)
    "You nod in acknowledgement. Even though the camera is running, you know that the real reason [the_person.possessive_title] has you here isn't for the video, but because she wants you to dominate her."
    "She could have chosen any other toy, and she could have chosen any other guy, but she chose you. You snap the second hand cuff in place."
    the_person "So, these handcuffs are soft enough they don't hurt or dig into the skin, but they are very sturdy. [the_person.mc_title] can do whatever he wants to me now, there's no way I'll be able to break free."
    "You take that as your cue. You grab her shoulders and turn her away from you, then push her down onto the table. Soon, she has her face down and her ass up."
    $ the_person.draw_person(position = "doggy")
    "Her pussy lips are wildly engorged, slick from the juices of her previous orgasm."
    "You rub your dick back and forth across her slit, getting it nice and slick. Then you grab her hips, and in one smooth motion you thrust yourself deep inside her."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "You thrust yourself deep into her steamy sex. Her moans begin immediately, her arousal still high from her previous orgasm."
    "You hold onto [the_person.possessive_title]'s hips and settle into a steady rhythm, pumping your cock in and out of her tight pussy."
    $ play_spank_sound()
    "You take a hand off of [the_person.possessive_title]'s hips and squeeze her ass cheeks with it. She moans happily in response you give her a hard slap."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title] struggles a bit against her handcuffs, but she is helpless to defend herself from your spanking."
    $ play_moan_sound()
    "[the_person.possessive_title]'s moaning intensifies rapidly, until finally she takes a sharp breath and tenses up."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.have_orgasm(half_arousal = False)
    $ the_person.change_stats(happiness = 4, slut = 1, max_slut = 50)
    "You keep up your pace while [the_person.possessive_title] cums. With each pulse of her pussy around your cock you spank her ass."
    the_person "Ah!"
    "You enjoy the way her tight ass jiggles and spank it again."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(50)
    "You take your hands off of her hips and lean forward to put them on her shoulders. With her hands in cuffs she is powerless to resist when you pull her shoulder back towards you, forcing her to arch her back."
    "With the leverage of your hands on her shoulders, holding her body weight up off the table. Your hips make heavy slapping noises as the slam into her ass with each thrust."
    the_person "OHHH! Fuck me [the_person.mc_title]! HOLY FUCK!"
    "[the_person.possessive_title]'s entire body begins to tremble as another orgasm hits her. Her pussy spasms wildly all around you and you can see her hips quaking."
    $ the_person.call_dialogue("climax_responses_vaginal")
    $ the_person.change_stats(happiness = 4, arousal = 20, slut = 1, max_slut = 50)
    $ mc.change_locked_clarity(30)
    $ the_person.have_orgasm()
    "[the_person.possessive_title]'s orgasm is milking your cock. It is rapidly pushing you past the point of no return."
    "You can't help but grunt with each thrust as you fuck her roughly. [the_person.possessive_title] is having trouble speaking intelligible words."
    the_person "[the_person.mc_title]! Oh cum for me baby... please cum! I want it so bad!"
    $ the_person.change_arousal(20)
    $ mc.change_arousal(25)#105
    "You can't take anymore. You let go of her shoulders and her upper body crashes roughly to the table. You grab her hips and plow deep into her pussy."
    $ the_person.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    "You bottom out and explode deep inside of [the_person.possessive_title]. The heat of your semen painting her vaginal walls sends her into another orgasm."
    the_person "OH! I'M CUMMING AGAIN! YES [the_person.mc_title]!"
    $ the_person.have_orgasm()
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "doggy")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
    "You are completely spent. [the_person.possessive_title] is a sweaty, handcuffed mess beneath you. She takes a few seconds to recover."
    $ mc.reset_arousal()
    the_person "So... as you can see... the handcuffs... fuck... they can hold up to... some pretty intense... amazing... mind-blowing... fucking..."
    "You move of the side to exit the frame. You can see in the camera your seed slowly dripping out of [the_person.possessive_title], when you press the stop button."
    mc.name "Wow, that was amazing. I'd be surprised if we don't get at least a little bit of traffic from couples out of that!"
    "[the_person.possessive_title] turns her head to look at you. You laugh when you realize you forgot to un-cuff her."
    mc.name "Sorry, I forgot you still had those on."
    "You grab the key and undo the cuffs. She slowly sits up, but is hesitant to stand."
    $ the_person.draw_person(position = "sitting")
    the_person "[the_person.mc_title]... it's been so long... since I've been fucked like that..."
    if the_person.love > 50:
        the_person "I've missed that, having someone take control of me and just fuck my brains out..."
        "While she is normally a very independent woman, you think maybe [the_person.possessive_title] is starting to get a bit of a submissive streak when you are around."
        if the_person.get_opinion_score("being submissive") < 1:
            $ the_person.update_opinion_with_score("being submissive", 1)
    the_person "So... I'm just gonna throw this out there. I have at least 4 other sets of fuzzy cuffs... we could totally try them out anytime you want..."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] slowly stands up. She walks over toward you."
    $ the_person.reset_arousal()
    the_person "Except right now... I'm going to need some time to recover from that."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] wraps her arms around you. She kisses you twice on the neck, then whispers in your ear."
    the_person "I can feel you running down my leg... and I love it..."
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "walking_away")
    the_person "I'm gonna go get cleaned up now... Get to work on that video!"
    $ the_person.event_triggers_dict["shop_investment_rate"] = 4.0
    $ the_person.apply_planned_outfit()
    "You grab the camera, and start looking at the footage. The first thing you do is copy it on a thumb drive, for you to enjoy at a later date."
    "You head out to start work on the advertisement video."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Increase oral skill after helping Starbuck demonstrate edible panties. + 1 Oral Skill", oral_bonus = 1, bonus_is_temp =False), "Starbuck Oral Bonus")
    "Giving [the_person.title] an orgasm with your tongue gives you more confidence in your oral skills."
    $ mc.location.show_background()
    $ clear_scene()
    $ strip_choice = None
    return


#SBS100
label starbuck_sex_store_promo_four_label(the_person): #DP, ends in ???
    the_person "Oh, yeah! It's great to see couples coming in now..."
    "[the_person.possessive_title]'s voice trails off for a second before she continues."
    the_person "You know, I've been tracking the stock of stuff we have been selling though. It's all very... vanilla? I guess you could say."
    mc.name "I'm not sure I understand what you mean?"
    "[the_person.possessive_title] stutters as she tries to figure out the best way to explain what she means."
    the_person "I guess I just mean that, the sales we are getting, it's for just generic sex items. Lingerie, condoms, handcuffs... but the more... shall we say, kinky items aren't really selling."
    mc.name "Like what kind of things aren't selling?"
    the_person "Well, some of the kinkier items... like whips, ropes, strap-ons... that kind of thing."
    "You consider some of the items she has in mind. The list she's said makes you a little nervous."
    mc.name "Well, I mean, I'm definitely willing to help you make another video showcasing an item or two... did you have anything specific in mind?"
    the_person "Well... I'm going to be honest here, you definitely seem like more of a dominant type... why don't we make a video where I play the submissive? See if we can get more business that way?"
    "Wow... she wants you to play the dom! You definitely like where this is going..."
    $ mc.change_locked_clarity(20)
    the_person "Tell you what... set up the camera and meet me in back in a few minutes... I've got a couple things in mind I wouldn't mind..."
    mc.name "Sounds great!"
    "You make your way to the back. You get the camera set up and ready to go."
    $ SB_advert_six_outfit = Outfit("Starbuck's Pink Lingerie")
    $ SB_advert_six_outfit.add_upper(corset.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(garter_with_fishnets.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_feet(high_heels.get_copy(), colour_pink)
    $ SB_advert_six_outfit.add_accessory(wide_choker.get_copy(),colour_pink)
    $ SB_advert_six_outfit.add_accessory(lipstick.get_copy(), [1.0,0.44,0.43,0.7])

    "[the_person.possessive_title] enters the room. When you see what she is carrying you start to get excited."
    the_person "Ok, I figure we can start with the whip... I also have a bottle of premium anal lube, and a strap-on for guys designed for double penetration..."
    "Wow... you wonder which hole you are gonna get to fuck while the strap-on fucks the other..."
    $ mc.change_locked_clarity(20)
    "[the_person.possessive_title] starts to strip down in front of you."
    $ the_person.strip_outfit(position = "stand4", exclude_feet = False)
    "Once she finishes stripping, she puts on some incredibly sexy pink lingerie."
    $ the_person.apply_outfit(SB_advert_six_outfit)
    $ the_person.draw_person()
    $ the_person.wardrobe.add_outfit(SB_advert_six_outfit)
    $ del SB_advert_six_outfit
    mc.name "[the_person.title]... that's... you look amazing."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] gives you a wide smile."
    the_person "Thank you! You know I can't give ALL my investors special views like this..."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns around and wiggles her hips a bit. She peeks back at you and teases."
    the_person "But you've done so much for me... I figure this is the least I can do for you!"
    $ the_person.draw_person(position = "stand4")
    $ mc.change_locked_clarity(20)
    the_person "Okay! Let's start with the whip, go ahead and get the camera rolling, and I'll do the introduction."
    "You step over to the camera. When [the_person.possessive_title] is in frame you hit the record button."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review another couple of products."
    the_person "Today, we are going to review a couple of products meant for those who are look to get things a little... kinkier in the bedroom..."
    "[the_person.possessive_title] talks about the whip she has in her hand. After explaining tips and tricks to proper usage, she cues you."
    the_person "And now, to demonstrate proper usage, I'm going to invite [the_person.mc_title] back to help me demonstrate it..."
    "You move in frame, and she hands you the whip."
    the_person "Okay! Now, it is important, anytime you get something like a whip involved, that you are very careful with where you strike the other person."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] bends over a chair nearby."
    the_person "While really, you could use it on any fatty part of the body, the obvious place to utilize a whip during sex play is on the ass..."
    "You are partially mesmerized by [the_person.possessive_title]'s ass when she bends over. In her pink lingerie, you can't wait to fuck her... you are startled when she prompts you."
    $ mc.change_locked_clarity(30)
    the_person "... [the_person.mc_title]? I said I'm ready now. Show the viewers how to use that thing!"
    "You move behind her, but at an angle so that the camera can still see what is going on."
    "For your first strike, you spank her modestly. You aren't sure how much pain tolerance she has."
    $ play_spank_sound()
    "SMACK"
    the_person "OH! As you can see, another important thing when you are using a tool like this is... start slow! As you can see, my partner here is starting easy..."
    "[the_person.possessive_title] wiggles her hips back and forth a couple times."
    the_person "Don't worry [the_person.mc_title], you can give it to me harder than that."
    "You swing the whip with a little more force this time."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)
    the_person "AHH! Mmmm, that's nice... Now remember, an important part of spicing up the bedroom is communication! Tell your partner how you like it!"
    "[the_person.possessive_title] wiggles her hips again."
    $ mc.change_locked_clarity(30)
    the_person "Okay [the_person.mc_title], that was about a 5 out of 10 for how hard you can spank... I want you give me a 7 this time..."
    "You'd never thought about rating how hard you swing the whip, but it makes total sense after [the_person.possessive_title] says that. It's pretty sexy the way she tells you the way she wants to get spanked..."
    "You put more force into the next one, but not too much."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)#20
    the_person "Fuck! Oh that was good... That was just about perfect... now try and..."
    "SMACK"
    "You catch her off guard as you give her other ass cheek a whipping."
    the_person "AHH! Oh that hurt so good... that's it baby, I've been a bad girl... spank me!"
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(10)#30
    $ mc.change_locked_clarity(30)
    "You give her a couple more spanks with the whip."
    $ play_spank_sound()
    "SMACK"
    "You can see her ass cheeks beginning to turn red. She wiggles her hips as you spank her."
    $ play_spank_sound()
    "SMACK"
    $ the_person.change_arousal(15)#45
    the_person "YES! Oh [the_person.mc_title]... okay... I think the viewers get the idea now..."
    $ play_spank_sound()
    "SMACK"
    "You give her one last spank, just for good measure... You can see her pussy is starting to glisten with excitement."
    $ the_person.draw_person(position = "stand2")
    $ mc.change_locked_clarity(30)
    the_person "Okay... time to move on. The other thing we have to demonstrate today is... mmm, that felt good..."
    "[the_person.possessive_title] takes a second to gather her thoughts."
    the_person "We are going to demonstrate proper usage of a special type of strap-on. This strap-on goes around a man and sits just below the penis..."
    "[the_person.possessive_title] explains the basics of the strap-on in her hand. When she gets done talking about it, she gets down on her knees."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    the_person "Okay, here is how we put it on..."
    "She grabs your dick and gives it a couple strokes. She puts the straps in place and secures the strap-on to you. You now have a second, rubber cock, sitting just below your fleshy one."
    "[the_person.possessive_title] gazes intently at your meat. She licks her lips and then runs her tongue along the side of it a couple times before she stands up."
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "stand4")
    the_person "Now, before we get to the good part, it is important, anytime you are getting ready to put anything in your ass, that you get it good and lubed up..."
    "She grabs the bottle of premium anal lube and squirts some in her hand. She lists the pro's of buying the higher quality lubes."
    "[the_person.possessive_title] takes your cock in her hand and started to lube it up. She takes the bottle and squirts some more into her hand, getting you nice and slick."
    $ mc.change_arousal(5)#10
    "She squirts some more in her hand, and you see her reach back and start to lube up her backside."
    the_person "Okay, I think we are all set..."
    $ the_person.draw_person(position = "doggy")
    "[the_person.possessive_title] gets down on her hands and knees and sticks her ass up in the air. Her puckered hole glistens from the lube she put on it, and her lips are puffy with arousal."
    $ mc.change_locked_clarity(30)
    the_person "[the_person.mc_title]... I want you to go slow when you put your cock in my ass... I'll guide the strap-on into my vagina..."
    "Her ass looks supple and firm. You are about to fuck [the_person.possessive_title]'s ass, while a dildo penetrates her pussy. You can't believe how lucky you are to able to do this with her."
    "You get down on your knees behind her. With one hand on her hip and the other on your cock, you line yourself up with tight back passage."
    "[the_person.possessive_title] reaches one hand between her legs and grabs the dildo. She lines it up with her other hole."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    $ mc.change_locked_clarity(30)
    the_person "Oh my god! I'm so full... It's so good [the_person.mc_title]! This thing is amazing..."
    "With your hands on her hips, you slowly start to fuck her."
    call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_sex_description_SBS100
    "[the_person.possessive_title] is in a sex induced daze after you finish. She struggles to make a coherent end to the video."
    the_person "So that's... when you use a strap-on... holy fuck people just get one."
    "You get up and head over to the camera and stop the recording."
    mc.name "Well... that was incredible. [the_person.title] if that doesn't bring in customers, I don't know what would."
    if the_person.love > 60:
        the_person "[the_person.mc_title]... you are amazing. Look... I'm going to be honest here. I couldn't care less about bringing in more business... I just wanted you to fuck me with that thing."
        $ the_person.draw_person(position = "stand2")
        "[the_person.possessive_title] slowly stands up. Her feet are a bit wobbly."
        the_person "It has been amazing having you around [the_person.mc_title]. It just feels so right every time we have sex. It almost feels wrong... recording it just to bring in more business..."
        "You decide to interrupt her."
        mc.name "[the_person.title], it has been great being your business partner. I know what you are saying, but don't worry. I'd be doing this with you even if we weren't recording it."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "She smiles at you happily."
        mc.name "But don't worry. If it helps the business grow, there's no reason not to record it. It doesn't make the sex any less meaningful to me. I mean really, you could ask any guy in here to do this stuff..."
        the_person "I can't imagine it though... doing this whole venture with anyone else as my partner. Thank you, [the_person.mc_title]."
    else:
        the_person "Thanks, [the_person.mc_title]. That was amazing... UGH I can barely get up."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        "[the_person.possessive_title] slowly stands up. Her feet are a bit wobbly."
    "[the_person.possessive_title] rubs her ass a bit where you spanked her earlier."
    the_person "I remember when... my husband used to use me like that... bending me over, spanking me like the naughty girl that I am."
    the_person "We should do this again. It felt so good when your cock started pushing into my ass..."
    if not perk_system.has_item_perk("Male Strapon"):
        "She looks at the strapon, then looks back at you."
        the_person "Actually... do you want this strapon? I'm sure I probably can't sell it now. I could give it to you if you want it..."
        $the_person.draw_person(position = "stand4")
        "She gets closer and whispers in your ear."
        the_person "Just promise me you'll use it on me again..."
        mc.name "I promise!"
        # $ item_perk_male_strapon = Item_Perk("A strap on designed to be worn by men. Useful for dual penetration!")
        # $ perk_system.add_item_perk(item_perk_male_strapon, "Male Strapon")
        $ male_strapon_unlock() #TODO test this
    if the_person.get_opinion_score("being submissive") < 2:
        $ the_person.update_opinion_with_score("being submissive", 2)
    if the_person.get_opinion_score("anal sex") < 1:
        $ the_person.update_opinion_with_score("anal sex", 1)
    "You grab the camera, and start looking at the footage."
    mc.name "Okay, you take it easy for a bit, I'm gonna go work on that advertisement video!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] starts to walk away. She is walking a little funny."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Increase anal skill after helping Starbuck demonstrate double penetration with a dildo. +1 Anal Skill", anal_bonus = 1, bonus_is_temp = False), "Starbuck Anal Bonus")
    "Fucking [the_person.title] anally makes you more confident in your anal skills."
    $ the_person.event_triggers_dict["shop_investment_rate"] = 5.0
    $ the_person.apply_planned_outfit()
    "You head out to start work on the advertisement video."

    return

#SBS110
label starbuck_sex_store_promo_five_label(the_person): #Swingset anal, ends in ???
    the_person "Oh, yeah! Business is great! It has been amazing having all different types of people coming in here to try out all kinda of new things."
    "[the_person.possessive_title] gives you a big smile."
    the_person "I tell you what. I have a product I've been wanting to try out ever since we expanded and got it in..."
    "You like where this conversation is going!"
    the_person "If you are willing to try it out with me... I'd be willing to give you an extra that you can take home with you!"
    mc.name "Are we going to do another video of it? For advertising purposes?"
    the_person "Of course! I mean, as long as you are okay with it... honestly... I want to try it out either way, but if we're gonna try a new product, might as well take a video anyway, right?"
    "You nod in agreement."
    mc.name "Okay, I'm in. What exactly are we going to test out?"
    the_person "Well... I got in a special... ermm... swing set... with straps that I can get up in, so you can fuck me in while I'm suspended up in the air..."
    mc.name "Wow... do you need help setting it up?"
    the_person "Yes, actually. That would be really helpful!"
    "You and [the_person.possessive_title] head to the back room. To the side of the room you can see a box that has the swing in it."
    "You pull it out and start going through the directions. It seems pretty straightforward to set up!"
    $ the_person.draw_person(position = "back_peek")
    "While working on the set up, you look over and see [the_person.possessive_title] working on something with her back to you. You walk up behind her."
    "You run your hands along her hips, admiring their shape and form."
    if the_person.love > 70:
        the_person "Mmm... I love it when you run your hands all over me [the_person.mc_title]."
        "You work your hands along her belly and then slowly up to her wonderful tits."
        if the_person.tits_available:
            "They are so soft and warm in your hands. You give them a good squeeze and then punch lightly at her nipples."
        else:
            "They feel so soft, even through her clothes. You give them a good squeeze, and you can feel her nipples start to poke through the fabric."
        "[the_person.possessive_title] pushes her ass back against you. She starts to grind her hips against your hardening erection."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(30)
        the_person "[the_person.mc_title] it is so nice having you close... let's get done with this swing. I want you!"
    else:
        the_person "That feels good... Let's focus on the swing though. I need a good fucking!"
        $ mc.change_locked_clarity(15)
    "You get back to work. It isn't long until the whole thing is finished. You stand with [the_person.possessive_title] and admire your handiwork."
    $ the_person.draw_person(position = "stand3")
    the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
    "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."
    $ the_person.strip_outfit(position = "stand3")
    $ mc.change_locked_clarity(30)
    "Now that she is naked, [the_person.possessive_title] grabs some of her anal lube of a shelf. You raise an eyebrow as she squirts some onto her hand."
    mc.name "Anal lube? Wow... going all out are we?"
    "[the_person.possessive_title] chuckles as she reaches back and starts to spread the lube around her backside."
    the_person "Of course! I mean, it feels so good when you push it into me back there..."
    the_person "Besides, I'm sure that the viewers would probably like it better anyway!"
    "[the_person.possessive_title] walks over to you and starts lubing up your cock. It feels great when she gives you a couple of strokes."
    $ mc.change_locked_clarity(30)
    the_person "Okay! I'm ready to do this! Go ahead and start up the camera, this is gonna be great!"
    "You step behind the camera. You make sure everything is in frame, then hit record. You give [the_person.possessive_title] a thumbs up."
    the_person "Hello! This is [the_person.fname], from [the_person.fname]'s Sex Shop! Here to review a new product we've just gotten in to the store!"
    the_person "Today, I am going to be reviewing the FEMco Sex Swing 3000..."
    "[the_person.possessive_title] starts talking about the swing set. As she talks, she is using hand gestures to illustrate some of the set up methods."
    "Every time she moves her hands back and forth, her amazing tits quiver a bit."
    "After she is done introducing the swing, she sits down in it."
    $ the_person.draw_person(position = "sitting")
    the_person "And now to help me demonstrate one of the ways you could use it, the always amazing [the_person.mc_title]!"
    "You step into frame and start to walk up behind her."
    the_person "Today, he is going to show us how it could be used for a relaxed sodomy session. I'll be able to relax here in the swing, while my ass is at just the right height for him to fuck it..."
    "As you get close behind her, you put your hands on her hips. She reaches back and grasps your cock, and begins to guide it toward her bottom."
    "When your cock begins poking up against her puckered hole, you can feel a bit of resistance. With your hands firmly on her hips, you pull her ass towards you."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] forces herself to relax her sphincter, and you penetrate her with a wonderful pop. With more gentle pressure you are soon deep inside her bowel."
    the_person "Mmm... as you can see... I'm able to completely relax with my ass off the back of the swing, so I can just sit and enjoy the sensations."
    "You give her a modest thrust. The swing bounces forward for a second, but gravity soon causes her ass to pendulum back and smack against your hip."
    "The feeling is exquisite. You grab her hips and get ready to fuck [the_person.possessive_title]'s brains out."
    #Call sex scene#
    call fuck_person(the_person, start_position = anal_swing, start_object = make_swing(), skip_intro = True) from _call_sex_description_SBS110

    "Turning off the video camera, you turn to [the_person.possessive_title]."
    $ the_person.event_triggers_dict["shop_investment_rate"] = 6.0
    mc.name "Wow, that was good. You are so sexy."
    the_person "Aww, thanks, [the_person.mc_title]. Now, I promised that if you helped me make the video, I'd give you a swing for you to have."
    mc.name "Thanks, but you don't need to do that."
    the_person "No no, it's okay, I want you to have one... I was thinking... you helped me set up this one, why don't you let me come over and I'll help you set up one?"
    "Hmm, she is offering to come over to your place!"
    mc.name "Well, it would be rude to say no."
    "[the_person.possessive_title] gives you a big hug."
    the_person "Great! Let's get it done. It won't take us long!"
    $ the_person.apply_outfit(the_person.decide_on_outfit(.4))

    #TODO move the scene to the player's bedroom. and get dressed
    $ mc.change_location(bedroom)
    $ the_person.draw_person(position = "stand4")
    "You and [the_person.possessive_title] head back to your place. Having already put one together, you and her quick have it all set up."

    the_person "Great! Now you have one of your own... you know... for when you have girls over..."
    "She gets a little shy."
    the_person "I think that I'm going to leave up the one I have in the back room at the shop, in case you ever want to try it out again..."
    if the_person.love > 70:
        "She looks at you. Her face is a little forlorn, clearly remembering something from her past."
        the_person "[the_person.mc_title], getting this shop up and running... and everything you've done for me. You really don't have any idea how much it all means to me. Thank you so much!"
        $the_person.draw_person(position = "kissing")
        "She wraps her arms around you and hugs you close."
        the_person "Look... I don't know any other way of saying this, so I'm just gonna say it. I'm falling for you, [the_person.mc_title]. And I know you have a busy job and there's other girls and I'm not saying..."
        "She stutters for a minute."
        the_person "I understand that you aren't looking to be tied down to one girl, and I just want you to know that I understand that. I just want to know if you, maybe have feelings for me too..."
        menu:
            "It's mutual":
                mc.name "Don't worry, [the_person.title]. The feeling is mutual. I love spending time with you."
                $ the_person.draw_person(position = "stand2", emotion = "happy")
                the_person "Oh! That is such a relief to hear."
                "You see her digging around in her pocket."
                the_person "Here... I want you to have this. It's a key to my apartment. You don't have to come over if you don't want to, but I just want you to know, you're always welcome in my bed."
                $ the_person.learn_home()
                mc.name "Thanks, [the_person.title]. It will be nice to be able to share a warm bed with a beautiful woman like you once in a while."
                $the_person.draw_person(position = "kissing")
                "She hugs you again and begins kissing you on your neck."
                the_person "You make me feel so good, [the_person.mc_title]... come visit me soon okay?"
            #TODO it's not mutual
    else:
        # alternative to learning her home location (needed for 'spend the night' event)
        the_person "Anyway, if you are ever in my neighborhood make sure to drop by for a beer."
        $ the_person.learn_home()
        "She tells you her home address, so make sure you go visit her sometime."

    $the_person.draw_person(position = "stand2")
    the_person "Okay, it's time for me to get to the shop. See you soon [the_person.mc_title]!"
    "You walk her to the door and say goodbye. Wow, you are now the proud owner of a sex swing! And with everything going on with [the_person.possessive_title], you brain is swimming a bit."
    $ perk_system.add_stat_perk(Stat_Perk(description = "Increase sexual skill cap from repeated sexual activity with Starbuck. +1 Sex Skill Cap", sex_cap = 1, bonus_is_temp =False), "Starbuck Sex Bonus")
    "After having multiple sexual encounters with a woman like [the_person.title], you feel like if you put in the effort, you could become an even more skilled lover."
    $ sex_store.add_object(make_swing())
    $ bedroom.add_object(make_swing())
    return

#SBS120
label starbuck_spend_the_night_label(the_person): #You spend the night at her place. You'll probably get busy
    mc.name "I was thinking I could spend the night here tonight."
    "[the_person.title] looks delighted."
    the_person "Oh! That would be great! I'd love the company!"
    $ ran_num = renpy.random.randint(0,100)
    if ran_num < 10 or mc.energy < 30: #No event, just cuddle up and go to bed.
        mc.name "Thanks. It's been a long day and I'm exhausted."
        $ the_person.change_to_bedroom()
        "You strip off your work clothes, down to your boxers. You head to [the_person.title]'s bedroom and hop in her bed."
        the_person "I'll be in in a minute!"
        "You see [the_person.title] step into the bathroom. In a few minutes she emerges, ready for bed."
        $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(sluttiness_min = 10, guarantee_output = True))
        $ the_person.draw_person()
        "She crawls into bed beside you. You cuddle up behind her and enjoy the warmth of her body as you drift off to a restful night's sleep."
    elif ran_num < 40: #She seduces you
        mc.name "Thanks. I just have a little bit of work stuff to finish up. I brought my laptop, mind if I take over your desk for a few?"
        the_person "Help yourself! I'll tell you what, I'm going to hop in the shower."
        "You sit down at the desk and pull out your laptop. You review some of the days research notes and begin emailing instructions for tomorrow."
        "You make note of a couple issues serum production, so write yourself a reminder to talk with an employee tomorrow about it..."
        "You delve into your work emails for a while longer, totally forgetting you are at [the_person.title]'s house. You are vaguely aware when you feel her coming up behind you."
        "Your mind is brought immediately back to the present when you feel the heavenly sensation of [the_person.title]'s warm, soft tit flesh on the back of your neck as she wraps her arms around you from behind."
        mc.name "Mmm, that feels great..."
        $ mc.change_locked_clarity(20)
        "She runs her hands up and down your chest, slowly unbuttoning your shirt. You lean your head back, your neck nestled between her amazing tits."
        "[the_person.title] begins to move her chest up and down slightly, rubbing her breasts along your neck and shoulders."
        the_person "Are you about at a stopping point?"
        mc.name "Yes, definitely."
        "You close your eyes and enjoy the sensations. [the_person.title]'s hands move lower down your belly and begins to stroke you through your pants."
        "She expertly begins to unbuckle your belt, and undoes your pants. You sigh when she puts one hand down your underwear and begins to jack you off slowly. She whispers into your ear."
        the_person "Come on... let's go to bed."
        $ the_person.apply_outfit(Outfit("Nude"))
        $ the_person.draw_person(position = "back_peek")
        "She backs away from you and walks into her bedroom. You turn and watch her, seeing she is completely naked."
        $ the_person.change_to_bedroom()
        "You quickly follow her."
        $ the_person.draw_person(position = "stand4")
        "[the_person.title] stops when she gets to the bed and turns to you."
        the_person "Lay down... there's something I want to do..."
        $ the_person.draw_person(position = "standing_doggy")
        "You nod. You take off what is left of your clothes and lay down. You watch [the_person.title] rummage through her nightstand. Her ass wiggles back and forth, right in front of you."
        $ mc.change_locked_clarity(30)
        $ play_spank_sound()
        "*SMACK*"
        "You reach up and give her ass a firm spank. She gives a sigh."
        the_person "Ah! Here it is..."
        $ mc.change_arousal(10)
        $ the_person.draw_person(position = "stand4")
        "She stands up and you see that she is holding a bottle of anal lubricant. You feel your dick twitch when you realize what she has in mind."
        "She squirts some of it out onto your cock and works her hand up and down you a few times. Then she squirts a bit more into her hand and then reaches back to her ass."
        "[the_person.title] gives another gasp as you imagine she works a bit of the lube into her tight hole."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title] climbs up on top of you. She takes you in her hand and points it towards her back passage."
        the_person "Oh god, [the_person.mc_title], it's so big! Okay, here we go..."
        $ mc.change_arousal(10)
        "[the_person.possessive_title] goes slow, but steadily slides down, impaling her sphincter on your throbbing erection. She bottoms out and moans loudly."
        #Fuck her#
        call fuck_person(the_person, start_position = anal_cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_SBS120
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh god, I came so hard..."
            "[the_person.possessive_title] collapses onto the bed next to you, exhausted from her anal cowgirl ride."
        else:
            the_person "Mmm, that was so good, thank you [the_person.mc_title]..."
            "[the_person.possessive_title] rolls off you and lays down on the bed next to you."
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person "Thanks, [the_person.mc_title], I needed that so bad."
        "She stretches her arms out and yawns."
        the_person "I'm worn out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."
    elif ran_num < 70 or mc.energy < 60: #You seduce her
        $ the_person.draw_person(position = "kissing")
        "[the_person.possessive_title] wraps her arms around you to give you a hug. You use the opportunity."
        "You grab her ass and pick her up easily. She yelps for a second but quickly wraps her legs around you in an embrace."
        "Your lips meet and you begin to kiss her hungrily. She returns your kiss. You pull her tight against you and begin to grind your needy cock up against her."
        $ the_person.change_arousal(5)
        $ mc.change_locked_clarity(20)
        "She breaks the kiss for a second."
        the_person "Oh [the_person.mc_title], I missed you too."
        "[the_person.possessive_title] clings to you and begins to kiss your neck eagerly. You carefully carry her towards her bedroom."
        $ the_person.change_to_bedroom()
        $ the_person.draw_person(position = "missionary")
        "When you get to her bed, you roughly throw her down on it."
        if the_person.vagina_available and the_person.tits_available:
            "You stop for a second and admire [the_person.title], her body on display in front of you. You guess she walks around the house like this?"
        else:
            "Your mind hazy with lust, you begin to pull [the_person.title]'s clothes off."
            $ the_person.strip_outfit(position = "missionary")
            "Now naked, you stop for a second and admire [the_person.title]'s incredible body."
        $ mc.change_locked_clarity(30)
        "Before you go any further, you decide to make sure that [the_person.title] is wet and ready for you. You pull her over so her legs are hanging off the edge of the bed and get down on your knees in front of her."
        "She spread's her legs instinctively as you begin to kiss along her knee. You trail wet kisses along the inside of her thigh, working your way further up."
        "When you reach her cunt, you waste no time, pushing your tongue between her lips and running it up and down her delicious slit."
        "[the_person.title] moans and begins to run her hands through your hair. When you push your tongue up inside her he gently urges you deeper."
        $ the_person.change_arousal(10)
        "You reach forward with your hands and grasp her tits. You roll her nipples in your fingers for a second causing her moans to grow louder."
        "You lick circles around her clit, then close your mouth over and gently suck on it."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Oh! Baby I'm ready, come fuck me!"
        call fuck_person(the_person) from _call_fuck_person_SBS121
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh god, I came so hard..."
        else:
            the_person "Mmm, that was so good, thank you [the_person.mc_title]..."
        "You lay down on the bed, hopping in the covers."
        "[the_person.title] doesn't bother to get up, she just cuddles up next to you."
        the_person "Thanks, [the_person.mc_title], I didn't know I needed that until you got here."
        "She stretches her arms out and yawns."
        the_person "You wore me out! Goodnight!"
        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."

    else: # You both want it, and MC has stamina for a wild ride
        "She gives you a flirty smile."
        the_person "I'm kinda sweaty from a long day at the shop, so I was just getting ready to hop in the shower. Why don't you get comfortable? I won't be long."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] turns and walks into her bathroom. She closes the door... mostly... leaving it open a crack. You're sure she left it open on purpose, but you decide for now to let her get started solo."
        $ clear_scene()
        "You head into her kitchen and notice her coffee pot is on and full. Was she expecting you? You pour yourself a cup and take a few sips."
        "You sit down and enjoy your coffee. It has been about 5 minutes now. The crack in the door is calling you. Should you join her in the shower? Or let her finish?"
        menu:
            "Shower with her":
                $ the_person.apply_outfit(Outfit("Nude"))
                $ mc.change_location(home_shower)
                "You decide you've waited long enough and make your way into the bathroom. Inside you smell the scent of lavender body wash and quickly spy [the_person.title]'s soapy body through the hazy steam."
                $ the_person.draw_person(position = "back_peek")
                $ mc.change_locked_clarity(30)
                mc.name "Have room for me in there?"
                the_person "Of course! I was hoping you would join me..."
                "You strip down and enter the shower. [the_person.fname] gives you a turn under the hot running water."
                the_person "Great timing... can you wash my back?"
                $ mc.change_arousal(10)
                "She hands you her loofah and you begin to work circles up and down her back. The soap bubbles make her already smooth skin slick and soft."
                "When her back is all soapy, you reach over her shoulder and hand the loofah back to her. You put your other hand against her hip and slowly pull her back against you."
                "You now wrap your arms around her from behind, and she melts back into you. Your hands roam her body but quickly begin to grope her generous bosom, while she wiggles her ass back against you."
                $ mc.change_locked_clarity(20)
                the_person "Mmm, I'm glad we're thinking the same thing. I'm really hungry for you tonight, [the_person.mc_title]!"
                "You whisper into her ear."
                mc.name "Is that so? I don't believe you... Why don't you show me."
                $ mc.change_arousal(10)
                if the_person.obedience > 110:  #She gets on her knees#
                    "[the_person.title] chuckles."
                    the_person "Mmm, for you, [the_person.mc_title]? I'll do just about anything..."
                    $ the_person.draw_person(position = "blowjob")
                    "[the_person.possessive_title] turns to you and gets down on her knees. She looks up at you. Her eyes certainly look a bit hungry..."
                    "She puts her hands on her breasts. She leans forward and nestles your cock between her bountiful tits."
                    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_fuck_person_SBS122
                    "You spend a moment recovering while [the_person.title] rinses your cum off her body."

                else:                           #She gets Feisty
                    "[the_person.title] chuckles and pushes her ass back against you."
                    the_person "Mmm, I have a better idea..."
                    "[the_person.possessive_title] leans forward a bit, against the shower wall. She reaches back and grabs your hardness, pointing it down towards her slit."
                    the_person "Why don't you just push it in... I'm ready for it, I promise..."
                    "You decide to go for it. She has you lined up, so you slowly push yourself forward inside of her."
                    the_person "Oh my god..."
                    "[the_person.possessive_title] sighs as you bottom out."
                    "She wiggles her ass back and forth a few times, enjoying the familiar feel of fullness you give her when you fuck her."
                    call fuck_person(the_person, start_position = standing_doggy, start_object = make_wall(), skip_intro = True, position_locked = True) from _call_sex_description_SBS123
                    "You spend a moment recovering while [the_person.title] rinses herself off."
                #TODO set outfit to regular nude again. She washed the cum off!
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.arousal = 50   #A hard setting of arousal... Did this to avoid an entry in the log. Not ideal code#
                $ the_person.draw_person(position = "stand2")
                "You both quickly finish showering. As you hop out, you quickly dry off and [the_person.title] takes your hand."
                the_person "Let's go to bed! I'm so charged tonight, I think I can go all night!"
                mc.name "Sounds good. I'm gonna fuck your brains out tonight."
                $ the_person.draw_person(position = "walking_away")
            #"Wait for her":  #TODO
        $ the_person.change_to_bedroom()
        "You follow [the_person.title] to her bedroom."
        "Her amazing ass sways back and forth as she walks. Your cock twitches thinking about the night ahead of you."
        "She gets to her bed and immediately opens her nightstand and begins looking for something."
        "She pulls out the strap-on dildo you helped her demonstrate for her advertisement and some anal lube and turns to you."
        $ the_person.draw_person(position = "stand4")
        $ mc.change_arousal(20)
        the_person "How about we give this another run? Last time we used it, the results were very good..."
        menu:
            "Agree":
                mc.name "Let's do it. I love fucking your tight little ass."
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title] gets down on her knees in front of you and starts securing the strap-on."
                mc.name "Hey... while you're down there..."
                "[the_person.possessive_title] looks up at you and smiles. She sticks out her tongue and slithers it along your aching shaft, teasing you."
                $ mc.change_locked_clarity(20)
                the_person "Mmm... you taste so good. But I have other plans for this."
                "She squirts some lube into her hand and then gives you a couple strokes."
                the_person "Okay, you're ready, now it's my turn!"
                $ the_person.draw_person(position = "doggy")
                "[the_person.title] stands up and hands you the lube, then crawls up on the bed on all fours, presenting her ass to you. She gives her hips a little shake."
                the_person "Lube me up, [the_person.mc_title]. Don't be stingy!"
                "You squirt a generous amount of lube onto your fingers. You run your fingers along her ass crack, coating it in a glaze of lube."
                "You take a finger and begin to push it up against her sphincter. You can feel her physically force herself to relax and then your finger eases right in."
                $ mc.change_locked_clarity(50)
                the_person "Mmm... that feels good already. I think I'm getting better at this!"
                "You apply some more lube, then slowly push two fingers into her smooth back passage. You feel like she is ready for you."
                "You get into position behind her. She arches her back and presents her ass."
                "[the_person.possessive_title]'s pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
                $ mc.change_arousal(10)
                "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                the_person "Oh my god! I'm so full... It's so good [the_person.mc_title]! Fuck me like you paid for this! Like I'm just a whore!"
                call fuck_person(the_person, start_position = doggy_anal_dildo_dp, start_object = make_bed(), skip_intro = True) from _call_sex_description_SBS124
                "Finished with your anal plundering, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

            "Fuck her your way":
                mc.name "Not tonight. I have something different in mind."
                "[the_person.title] looks a little disappointed, but waits to see what you DO have in mind."
                call fuck_person(the_person) from _call_fuck_person_SBS125
                "Finished for the night, you let yourself collapse onto [the_person.title]'s bed."
                "She cuddles up next to you."
                $ the_person.draw_person(position = "missionary", emotion = "happy")

        "[the_person.title] nuzzles up against you and slowly drifts off to sleep. In your sex induced haze, you quickly drift off to sleep with her."

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_SBS129
    #Good morning!
    $ perk_system.add_stat_perk(Stat_Perk(description = "Temporary increase max energy after sleeping with a lover. +20 Energy Cap", energy_bonus = 20, bonus_is_temp = True, duration = 2,  energy_cap = 20), "Overnight Lover")
    $ mc.change_location(the_person.home)

    $ clear_scene()
    if renpy.random.randint(0,100) < 50:        #Roll for morning sex is successful
        "[the_person.title]'s naked body against yours makes for a very pleasant night of sleep. A couple times throughout the night you stirred for a bit and gave her a grope, but quickly fell back asleep."
        "Pleasant sensations and the feeling of weight around your torso slowly wakes you up."
        $ mc.change_arousal(10)
        $ the_person.change_arousal(30)
        $ the_person.draw_person(position = "cowgirl")
        "When you awaken, you discover that [the_person.title] is on top of you, with your morning wood already hilted inside her pussy."
        "You moan in appreciation at the wonderful wake up call."
        $ mc.change_locked_clarity(50)
        the_person "Mmm... Good morning [the_person.mc_title]... When I woke up this morning you were poking me pretty good... I figured you wouldn't mind if I took it for a quick ride."
        "You murmur your acceptance. Her mesmerizing tits are bouncing up and down right in front of you. You take them both in your palms and give them a good squeeze."
        # call fuck_person(the_person, start_position = cowgirl, start_object = make_bed(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_SBS125
        call get_fucked(the_person, the_goal = "vaginal creampie", private= True, start_position = cowgirl, start_object = make_bed(), skip_intro = True, allow_continue = False) from _call_get_fucked_starbuck_spend_the_night_01
        the_person "Mmmff. So good... I wish I could call in sick and we could fuck all day... but I need to get to the shop."
        $ the_person.draw_person(position = "stand3")
        the_person "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title] slowly gets up and heads to the bathroom. You grab your stuff and head out."
    else:                                    #No morning sex
        "You wake up in the next morning after sleeping soundly the night before. As your stir it wakes up your bedwarmer, [the_person.title]. She yawns and stretches."
        "Slowly, [the_person.title] yawns and sits up at the side of the bed."
        $ the_person.draw_person(position = "sitting")
        the_person "Good morning, sleepyhead! Wow, I slept so good last night... you really wore me out!"
        "You chat for a few minutes, enjoying the warmth of her bed, until she gets up."
        $ the_person.draw_person(position = "stand3")
        the_person "I'm gonna go hop in the shower. Feel free to let yourself out! Thanks for spending the night [the_person.mc_title]!"
        "[the_person.title] heads to the bathroom. You grab your stuff and head out."
    $ mc.change_location(downtown)
    $ the_person.apply_outfit(the_person.decide_on_outfit(.4))
    $ clear_scene()
    return "Advance Time"

#SBS130
label starbuck_close_up_label(the_person): #You offer to help her close up. Mainly a chance to give her serum, also can screw around at higher sluttiness settings.
    mc.name "Can I help you close up tonight?"
    the_person "Oh! That would be great! I really appreciate it [the_person.mc_title]. I suppose it is about closing time..."
    "You continue to chat with her for a while, until it reaches the regular closing time. [the_person.title] locks the front door."
    the_person "I noticed earlier we had some pretty good lube sales. I think I'm going to bring out some boxes from the back. Want to help me restock?"
    mc.name "Sure! I can do that. Got anything to drink around here?"
    the_person "I have a mini fridge behind the counter. I have beer, some bottled water, maybe a soda or two in there."
    mc.name "Nice. Want anything?"
    the_person "A beer sounds great!"
    $ the_person.draw_person(position = "walking_away")
    "You grab two beers from the fridge and pop the caps on both with a bottle open magnet you find stuck to the front of the fridge."
    "[the_person.possessive_title] is in the back, you could probably drop some serum into her beer if you want to."
    menu:
        "Add some serum to her beer" if mc.inventory.total_serum_count > 0:
            call give_serum(the_person) from _call_give_serum_SBS130
            if _return:
                "You double check to make sure she is still in the back, then add the serum to [the_person.title]'s food."
            else:
                "You think about adding a dose of serum to [the_person.title]'s beer, but decide against it."

        "Add some serum to her beer\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
            pass

        "Leave her beer alone":
            "You take a long sip of your drink, waiting until [the_person.title] returns."
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title] returns with several boxes and sets them down, the grabs the beer and takes a sip."
    "You help her with the boxes and start to unpack as you both enjoy your drinks and each other's company."
    "When the boxes are unpacked, you help her take the empty ones to the back and put them in the recycling."
    the_person "Thanks for your help."
    if the_person.sluttiness > 40 and the_person.energy > 50:
        the_person "Is there something... ANYTHING I can do to return the favor?"
        "She bats her eyelashes as she looks at you. She licks her lips as you notice she steals a glance between your legs..."
    else:
        mc.name "It's no problem. Take care!"
        "You say goodbye to [the_person.title] and head out."
        call advance_time from _call_advance_time_starbuck_close_up_label_1
        return

    menu: #This menu is just to weed out if we don't want to have fun
        "Have some fun with her":
            pass
        "Some other time":
            mc.name "Honestly, I'm pretty tired out. Can I have a rain check?"
            "You can tell she is a little disappointed, but soon she is stretching and yawning."
            the_person "You know what?... I'm pretty tired too. Good night [the_person.mc_title]."
            "She walks you to the door of the business and you walk out together, before going your separate ways."
            call advance_time from _call_advance_time_starbuck_close_up_label_2
            return
    mc.name "I can definitely think of something."
    the_person "Oh yeah? I hope it's the same thing I'm thinking..."
    $ mc.change_locked_clarity(10)
    menu:
        "Just mess around some":
            "You grab [the_person.possessive_title]. She wraps her arms around you."
            $ mc.change_arousal(20)
            call fuck_person(the_person, skip_intro = False, private = True) from _call_fuck_person_SBS131
            the_person "So... you'll help me close up every night, right?"
            mc.name "I'm sorry, I can't promise something like that, my business keeps me busy."
            the_person "Damn. A girl can dream though."
            $ the_person.change_love(amount = 3, max_modified_to = 30)
        "Dress up for you" if get_shop_investment_rate() >= 2.0:
            call starbuck_replay_dressup_label(the_person) from _call_starbuck_replay_SBS132
        # "Play with a dildo for you" if get_shop_investment_rate() >= 3.0:   #TODO these options.
        #     pass
        # "Try more edible underwear" if get_shop_investment_rate() >= 4.0:
        #     pass
        # "Use whip and strap on" if get_shop_investment_rate() >= 5.0:
        #     pass
        # "Anal on the swingset" if get_shop_investment_rate() >= 6.0:

    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    "[the_person.title] lets out a big yawn, while rearranging her clothes."

    if the_person.is_in_trance:
        "[the_person.title] is tired and in a suggestible state, you can take a moment to train her."
        call do_training(the_person) from _call_do_training_starbuck_close_up_01

    the_person "You really wore me out! Good night [the_person.mc_title]."
    "She walks you to the door of the business and you walk out together, before going your separate ways."

    # time goes forward and exit the talk menu by jumping to game loop
    call advance_time from _call_advance_time_starbuck_close_up_label_3
    return

#SBS140
label starbuck_replay_dressup_label(the_person):
    mc.name "Remember that one time, you got dressed up in a bunch of different lingerie and I took pictures for that ad?"
    the_person "Of course! The last picture I was sucking on a dildo and it got me all hot and bothered and..."
    mc.name "Right... right... well, have any new lingerie sets that need modeled? Maybe before we head out I could umm, you know, take some pictures for another ad..."
    the_person "Oh! I supposed I would be up for that. I don't really have any new sets though, but I do have a pretty wide selection!"
    the_person "You know what would be fun? Why don't you go pick something out? I'll put it on and you can snap some pics."
    "Oh god, she wants you to dress her up... in lingerie."
    the_person "You're a guy, so I'm sure you probably have a better idea of what would be good for a new advertisement anyway, right?"
    mc.name "Yes. I absolutely am the best person I know of to dress you up in lingerie."
    "She laughs at your reply."
    the_person "I guess when you put it that way. Anyway, go pick out something!"
    "You head out into the store and look at the lingerie. You try to come up with a racy outfit to put [the_person.possessive_title] in."

    call screen outfit_creator(Outfit("New Outfit"), outfit_type="under", slut_limit = the_person.effective_sluttiness())
    $ the_person.draw_person()
    if isinstance(_return, Outfit):
        $ the_outfit = _return
        "You pull out a few pieces of clothing and take them to [the_person.possessive_title]."
        "She looks at the outfit you've picked out for her and seems to think for a second."
        if the_outfit.outfit_slut_score <= the_person.effective_sluttiness() * .2: #She likes it enough to try it on.
            the_person "Are you sure? This seems kinda tame..."
            mc.name "I know. I just want to see what it looks like on you."
        elif the_outfit.outfit_slut_score >= the_person.effective_sluttiness() * .8:
            the_person "Wow! I can honestly say I was not expecting you to go all in like this!"
            mc.name "If you don't feel comfortable..."
            "She interrupts you."
            the_person "Ha! No way, I can't wait to see you start drooling after I get this on..."
        else:
            the_person "Ah, this look great! I bet this generates a lot of interest..."
            "She gives you a quick wink."
            the_person "And I bet if we put it on an ad it would get some interest too!"
    else:
        mc.name "It seems I've lost my touch, why don't you surprise me?"
        the_person "Oh hotshot, give me a minute."
        $ the_outfit = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under", allow_skimpy = True)
        "After a few minutes she is back, holding an outfit in her hand."

    "[the_person.possessive_title] starts to get undressed in front of you."
    $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
    while strip_choice is not None:
        $ the_person.draw_animated_removal(strip_choice)
        "You watch as [the_person.possessive_title] takes off her [strip_choice.name]."
        $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

    $ strip_choice = None
    "Once she's stripped out of her clothing, [the_person.possessive_title] puts on the outfit you've made for her."
    $ the_person.apply_outfit(the_outfit, update_taboo = True)
    $ the_person.draw_person()

    $ mc.change_locked_clarity(30)
    the_person "Mmm, I like it! Alright, let's take some pictures!"
    $ the_person.wardrobe.add_outfit(the_outfit)
    "[the_person.title] hands you her phone with the photo app already up."
    $ the_person.draw_person(position = "back_peek")
    "In the first photo, you get some great shots of her backside. She sways her ass slowly, being careful not to go too fast in a way that would make the photos blurry."
    $ the_person.draw_person(position = "against_wall")
    "Next, she props up her leg on a stool and adopts a really sultry pose, with her legs open. She runs her hands down her sides and then back up between her legs..."
    $ the_person.change_arousal(10)
    $ the_person.draw_person(position = "cowgirl")
    "Finally, she gets down on her knees and slowly starts crawling over to you in a sultry display of her femininity."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    mc.name "Jesus girl, you are stunning..."
    the_person "Showing off for you is getting me all worked up again. Will you ummm... lay down for me?"
    "Thank god, things are about to get steamy."
    mc.name "For you? Anything."
    "You lay down on your back."
    if not the_person.vagina_available:
        "As you lay down, you notice [the_person.possessive_title] is stripping her bottoms off."
        $the_person.strip_outfit(top_layer_first = True, exclude_upper = True, exclude_lower = False, exclude_feet = True)
    $ the_person.draw_person(position = "stand4")
    "From the floor, you look up at the stunning sex shop owner. You notice a hint of moisture starting to form on her labia."
    the_person "When we made the first ad, I sucked you off. But this time, I want a little action too..."
    "[the_person.title] gets down beside you, then swings her leg over your body, her pussy right in your face. She adjusts her body into the classic sixty nine positions."
    $ the_person.draw_person(position = "doggy")
    mc.name "I suppose that is only fair."
    "You put your hands on her heavenly ass cheeks and get her to adjust her body a bit until she is in the perfect position for you to dive in."
    "You push your nose into her slit and begin to lick and suck on her clit. She exhales forcefully and you feel her hot breath on your dick."
    the_person "Mmmm, that's it. Oh god you are so hard, I have to taste it..."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(30)
    "You feel her tongue circling around the tip. She gives the head a couple of quick kisses and then parts her lips."
    "Her lips slowly descend your length, entering her blissfully hot mouth. You refrain from bucking your hips to keep from gagging her."
    call fuck_person(the_person, start_position = sixty_nine, start_object = mc.location.get_object_with_name("floor"), skip_intro = True) from _call_fuck_person_SBS141
    "When you finish, you slowly get up off the floor. You help [the_person.title] up as well."
    $ the_person.draw_person()
    the_person "So... you'll help me close up every night, right?"
    mc.name "I'm sorry, I can't promise something like that, my business keeps me busy."
    the_person "Damn. A girl can dream though."
    $ the_person.change_love(amount = 3, max_modified_to = 40)
    $ the_outfit = None
    return

#SBS150
label starbuck_replay_dildo_demo_label(the_person):




    return

#SBS160
label starbuck_replay_edible_undies_label(the_person):




    return

label starbuck_replay_anal_DP_label(the_person):



    return

label starbuck_replay_anal_on_swing_label(the_person):




    return

init 2 python:
    def starbuck_intro_choose_title(person):
        title_tuple = []
        for title in person.get_player_titles():
            title_tuple.append([title,title])

        return renpy.display_menu(title_tuple, True, "Choice")

    def starbuck_anal_fetish_prepare_demo_audience(the_person):
        count = 0
        for girl in [x for x in mc.location.people if not x is the_person]:
            if girl.sluttiness > 60:
                count += 1
            else:
                girl.change_location(mall)
        return count

label starbuck_intro():
    $ the_person = starbuck

    $ the_person.draw_person(emotion = "happy")
    if not the_person.event_triggers_dict.get("starbuck_intro_complete", False):
        "You enter the sex shop. A beautiful woman comes up to you and begins to introduce herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        $ the_person.event_triggers_dict["starbuck_intro_complete"] = True
        the_person "Hello there sir! Welcome to Starbuck's Sex Shop!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.title is None:
            mc.name "Hello."
            $ title_choice = the_person.get_random_title()
            $ formatted_title = the_person.create_formatted_title(title_choice)
            the_person "Let me introduce myself, I am [formatted_title]."
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(the_person.get_random_possessive_title())
            "She holds her hand out to shake yours."
            the_person "And how may I address you?"
            $ title_choice = starbuck_intro_choose_title(the_person)
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person "We've just opened, so stock is still fairly limited, but feel free to browse and I'm here to answer any questions you might have!"
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person "Sounds great!"
        $ clear_scene()
        "After [the_person.possessive_title] goes back to the counter, you walk around the shop a bit. Unfortunately, things are pretty bare. There are several shelves with just labels on them."
        "You walk by one labeled as anal toys, but there aren't any on the shelf available for purchase."
        "You walk over to the counter."
        $ the_person.draw_person(position = "stand3", emotion = "happy")
        mc.name "This is pretty interesting, to open a sex shop like this, but the shelves seem pretty empty? Are you going to get more stock soon?"
        $ the_person.draw_person(position = "stand3", emotion = "sad")
        the_person "Yes, I'm sorry they are fairly empty, I didn't have much money to invest in the store. I'm hoping I'll be able to attract some customers, and reinvest the money back into the shop..."
        "You can see she is struggling a bit to open up."
        the_person "You see, it was always my husband and I's dream to open a shop like this, to help people be more adventurous and have fun in the bedroom..."
        the_person "When he died... it was hard. It has been a struggle to make ends meet, but I feel like I'm finally ready to move on with my life, and decided to chase my dreams!"
        "You glance around the shop for a bit. You can tell she is very... optimistic."
        mc.name "That's great that you are moving on... but surely you should get a bit more stock? Have you tried finding any investors?"
        "[the_person.possessive_title] mumbles for a second before answering."
        the_person "Well, you would be surprised how hard it is to find investors for a sex shop..."
        "You can tell that she is a hard worker, and is dedicated to making her shop work. Maybe you should consider investing in her shop?"
        mc.name "How much money would you need, say if someone were interested in investing in your shop, to get some basic stock on the shelves?"
        "[the_person.possessive_title] considers for a moment."
        the_person "Well, I really want the stock to be good, quality product. I'd say I could probably get everything set up for a basic shop for... say $1000?"
        "That seems pretty reasonable. You decide to consider investing. You should talk to [the_person.title] again if you decide to invest in the shop!"
    elif sex_shop_stage() == 0:
        the_person "Hello there sir! Welcome back to Starbuck's Sex Shop! Feel free to look around."
        "You smile at [the_person.possessive_title] and promise to take a look."
        the_person "Sounds great, [the_person.mc_title]! I'll be here if you have any questions!"
    elif sex_shop_stage() == 1:
        the_person "Hey there, [the_person.mc_title]! It's good to see you!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person "I was just thinking about you. Anything I can help you with?"
        else:
            the_person "Is there anything I can help you with?"
    elif sex_shop_stage() >= 2 and get_shop_investment_rate() >= 3.0 and candace_get_has_gone_clothes_shopping() and candace.personality == bimbo_personality and not the_person.event_triggers_dict.get("Candi_event_start", False):
        if candace.sluttiness >= 60: #Separate candace slut check since I never check to make sure she exists in globals
            call starbuck_cargo_shipment_label(the_person) from _begin_candi_duo_event_intro_01
        else:
            "[the_person.possessive_title] smiles playfully."
            the_person "I don't think I could ever repay you, is there anything I can help you with?"
    elif sex_shop_stage() == 2:
        the_person "[the_person.mc_title]! I'm so glad to see you! This place is starting to do really well, thanks to you!"
        "[the_person.possessive_title] smiles playfully."
        the_person "Is there anything I can help you with?"
    elif sex_shop_stage() == 3:
        the_person "[the_person.mc_title]! Thanks for checking in! Thing are going amazing here, all thanks to you and your generous investments!"
        if the_person.sluttiness > 60:
            "[the_person.possessive_title] smiles playfully."
            the_person "I'll be forever in your debt. Is there anything I can help you with?"
        else:
            the_person "Is there anything I can help you with?"
    $ clear_scene()
    return

label starbuck_anal_fetish_masturbate(alert = False):
    $ the_person = starbuck

    if alert == True:
        "You feel your phone vibrate with a notification."
        "You pull it out and take a look. Looks like [the_person.title] is masturbating with her plug!"
    else:
        "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
        "You are mildly surprised to see that she is masturbating with her plug!"
    "Do you want to have some fun with the plug?"
    menu:
        "Leave her to her fun":
            #TODO this section
            return
        "Vibrate the plug":
            $ mc.change_locked_clarity(10)
            "You decide to have a little fun with the plug vibration. You push and the hold the vibration function for a solid three seconds."
            "The app registers a heart rate spike with the vibration. [the_person.possessive_title] knows you are watching the monitor as she masturbates!"
    #WE can assume we decided to vibrate the plug
    "You imagine [the_person.title], somewhere in her shop, pushing the plug in and out of herself."
    "You push and hold the vibrate button again, release it, then pulse again. You make it pulse with vibration every second or two."
    "You watch as her heart rate slowly climbs. It's 100 beats per minute now and still climbing."
    "You pulse the plug a bit faster now. Her heart rate keeps climbing."
    "You can imagine her, bent over, fucking herself with her plug as it vibrates deep inside her needy bowel."
    "After a minute, you see her heart rate peak. You give her 10-15 seconds of strong pulsing vibrations."
    $ mc.change_locked_clarity(10)
    $ the_person.change_stats(happiness = 5, obedience = 3)
    "You see the obvious spike on the chart now as her heart rate subsides. The plug registers that it is now back in place and not being used for masturbation."
    "After a few seconds you get a text message from [the_person.possessive_title]."
    #TODO picture of her bent over
    $ mc.start_text_convo(the_person)
    the_person "That felt good! You should come visit me soon though... get yourself some of this!"
    "She attached a picture of herself, bent over and showing her ass to you."
    $ mc.end_text_convo()
    return

label starbuck_anal_fetish_request(alert = False):
    $ the_person = starbuck
    "You feel your phone vibrate with a notification."
    "[the_person.title] sent you a text and a picture!"
    $ the_person.draw_person(position = SB_get_random_ass_position())
    the_person "Hey! You need to get over here and fuck this! I'm about to go crazy! I might jump the next guy that walks through my door!"
    "Sounds like she is desperate for a dick in her ass!"
    $ mc.change_locked_clarity(10)
    return

label starbuck_anal_fetish_checkup(alert = False):
    $ the_person = starbuck
    "You decide to check up on [the_person.title]. You pull out your phone and check up on her."
    "You see she has been good. She's had the plug in, just the way she said she would!"
    if the_person.arousal_perc > 40:
        "You can also see her temperature is a little elevated, consistent with what you would expect from someone in a consistent arousal state."
    "You decide to let her know you're thinking about her and her delicious ass."
    "You set the vibration setting to high, then press and hold the vibration button for several seconds. You can see her heart rate spike as her plug quakes inside her ass."
    "You wait for a few seconds, then send her another round of vibrations."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(10)
    "You decide that is enough for now and go back to what you were doing."
    return


label starbuck_anal_fetish_swing_demo_label(the_person):
    $ the_person = starbuck
    $ the_person.event_triggers_dict["LastAnalFetish"] = day
    mc.name "Hey, I was just wondering, you wanna go for a swing in the back?"
    "[the_person.possessive_title] gives you a big smile."
    the_person "That sounds great!"
    $ in_private = True
    #TODO determine if there are people here
    if mc.location.person_count > 1 and starbuck.has_exhibition_fetish: #If Starbuck is not the only girl
        the_person "I've got an idea! I've got a few customers in here... want to do a demonstration for anyone who wants to attend?"
        "You consider her proposition carefully."
        menu:
            "Do a demo!":
                mc.name "That would be hot! Let's do it!"
                the_person "Yes! Okay, you head back there, I'll get ready, make an announcement, then meet you back there, okay?"
                "You head to the back room. You make sure the swing is in a good position for people to be watch you... demonstrate it."
                $ mc.change_locked_clarity(30)
                "Soon you hear [the_person.title] making her announcement."
                the_person "Attention everyone! In five minutes, myself and a partner will be demonstrating one of the sex swingsets that we have for sale! Feel free to come watch and ask questions!"
                $ the_person.apply_outfit(special_fetish_nude_outfit)
                $ the_person.draw_person(position = "stand4")
                "Soon, [the_person.title] appears in the doorway, completely naked."
                #TODO: Determine if anyone wants to watch
                $ count = starbuck_anal_fetish_prepare_demo_audience(the_person)
                if count == 0:  #No one wants to watch
                    the_person "Well, I made my announcement, but it doesn't look like anyone is interested in watching..."
                    "You can hear the disappointment in her voice."
                    mc.name "Hey, their loss. Don't worry, it'll still feel just as good when I slide into that amazing ass of yours..."
                    "Her nipple stiffen slightly when she hears what you say."
                    the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
                    $ the_person.draw_person(position = "back_peek")
                    "[the_person.possessive_title] turns away from you. You see her plug nestled between her cheeks."
                    $ mc.change_locked_clarity(20)
                    "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
                    mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                    the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
                else:   #People watch
                    the_person "Here they come! This is gonna be great!"
                    "[the_person.possessive_title] looks genuinely excited! She walks over next to swing and nonchalantly takes out her plug and sets it to the side."
                    $ get_random_from_list(known_people_at_location(mc.location, [the_person])).draw_person(position = "stand4")
                    "You watch as people begin to walk into the room..."
                    "You are about to fuck [the_person.title], in the ass, in front of customers..."
                    $ mc.change_locked_clarity(30)
                    "You can't believe this is actually happening!"
                    $ the_person.draw_person(position = "sitting")
                    "[the_person.title] makes begin to speak. When you turn to her she is already seated in the swing. You quickly move around behind her."
                    the_person "So, today, my wonderful partner and I are going to demonstrate proper technique on this swing..."
                    "You zone out for a bit as she begins explaining the basics, how to set it up, etc."
                    "You can't wait to feel yourself slide into her tight rear end. You start to day dream a bit."
                    the_person "Alright, [the_person.mc_title], go ahead, I think we are ready for the demonstration."
                    "Hearing her mention you grabs your attention. You slide up behind her, your hands squeezing her pliant cheeks."
                    "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                    "She whimpers back at you."
                    the_person "Alright, let's give 'em a good show."
                    $ in_private = False

            "Keep it private":
                mc.name "I think I'd like to keep it between me and you, if that's okay."
                "You can tell she is a little disappointed, but she quickly smiles again when she remembers that you are about to fuck her in the ass..."
                the_person "Okay! Let's go!"
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title] walks to the back room. You quickly follow her."
                "You get to the back room and [the_person.title] turns to you."
                the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
                $ the_person.draw_person( position = "stand2")
                "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."

                $ the_person.strip_outfit(position = "stand2")

                "When you finish stripping, she turns her back to you."
                $ the_person.draw_person(position = "back_peek")
                mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
                "She gives her ass a little wiggle."
                the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
                "[the_person.possessive_title] pulls her cheeks apart. You can see her plug nestled between her cheeks."
                "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
                mc.name "Alright, let's replace that with something a little... meatier... shall we?"
                $ the_person.draw_person(position = "sitting")
                "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
                "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
                the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"
    else:
        the_person "Okay! Let's go!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] walks to the back room. You quickly follow her."
        "You get to the back room and [the_person.title] turns to you."
        the_person "Alright. Before we get started, let me get ready. You should probably get naked too!"
        $ the_person.draw_person(position = "stand2")
        "You start to strip down, but watch intently while [the_person.possessive_title] strips down along side you."

        $ the_person.strip_outfit(position = "stand2")

        "When you finish stripping, she turns her back to you."
        $ the_person.draw_person(position = "back_peek")
        mc.name "It's going to feel so good when I slide into that amazing ass of yours..."
        "She gives her ass a little wiggle."
        $ mc.change_locked_clarity(20)
        the_person "Mmm... I can feel it already... Probably because I still have this thing in!"
        "[the_person.possessive_title] pulls her cheeks apart. You can see her plug nestled between her cheeks."
        "You slide up behind her, your hands squeezing her pliant cheeks. You slowly pull the plug out of her. She whimpers when it's fully removed."
        mc.name "Alright, let's replace that with something a little... meatier... shall we?"
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] sits down on the swing. You get behind her and grab the ropes. Her ass already well lubed from her plug, she is ready for you."
        "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_person.possessive_title]."
        the_person "Oh fuck! Every time I think about the first time you fucked me on this thing I touch myself... fuck me good [the_person.mc_title]!"

    call fuck_person(the_person, private = in_private, start_position = anal_swing, start_object = make_swing(), skip_intro = True) from _call_sex_description_SBA080

    #TODO the rest of this scene.
    if in_private:
        the_person "Oooh, fuck that was just what I needed."
        $ the_person.draw_person(position = "stand3")
        "[the_person.possessive_title] slowly stands up. Her knees are a little wobbly."
        "She grabs her plug. She reaches back and slowly re-inserts it with a moan."
        the_person "Mmm, that feels nice. Alright, you run a long now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself as [the_person.title] heads to the bathroom."
    else:
        $ person_one = get_random_from_list(known_people_at_location(mc.location, [the_person]))
        "You look around the room. All eyes are on you and [the_person.title]."
        $ person_one.draw_person (position = "stand4")
        "To one side you see [person_one.title], clearly touching herself, after watching you and [the_person.title] fuck."
        person_one "Oh wow... maybe I should... I wonder if..."
        "She is muttering things under her breath as she touches herself. She closes her eyes and you see her body tense as she orgasms."
        $ person_one.have_orgasm()
        $ the_person.draw_person(position = "sitting")
        "[the_person.title] has noticed and is smiling wide."
        the_person "So... as you can see... the swing makes a wide variety of sexual maneuvers possible... For anyone who attended, I'd like to offer a discount!"
        "You hear a few murmurs of approval. [the_person.title] looks up at you and winks."
        the_person "Thanks, [the_person.mc_title], that was amazing. Alright, you run a long now! Don't worry about me, I'll get cleaned up and back out front in a quick minute."
        "You excuse yourself. You wonder if this will help sell the swing any!"
        $ del person_one

    call advance_time from _call_advance_SB_Anal_call_time_SBA081

    return
