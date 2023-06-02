#Candace, AKA Candi. Office bimbo. First met via Ophelia's story line. Can eventually corrupt, hire, and seduce her as revenge. Has default bimbo personality
# After hiring her, get discount on supplies purchased based on her sluttiness (she offers to seduce suppliers)
#Later, can develop anti bimbo serum to restore her. Transforms into Candace. Still slutty, but incredibly smart.
#Uses smarts to further seduce suppliers for a bigger discount
#TODO figure out max discounts. Probably 10-20%? Late game, supply discount is mostly flavor players are probably already profitable. Make available earlier via policy? "Logistics Coordinator?"
#Enjoys supply work, skirts, showing her ass.

init 3 python:
    list_of_instantiation_functions.append("create_candace_character")

    #Requirement functions
    def candace_meet_at_office_store_requirement(person):
        return person.location == office_store and mc.business.is_work_day

    def candace_get_to_know_requirement(person):
        if person.location == office_store:
            if not candace_get_has_quit_job():
                if not candace_can_talk():
                    return "Already talked today"
                return True
        return False

    def candace_convince_to_quit_requirement(person):
        if candace_get_can_convince_to_quit() and ophelia_get_will_help_candace():
            if mc.business.employee_count >= mc.business.max_employee_count:
                return "At employee limit"
            if not candace_get_has_quit_job():
                return True
        return False

    # def candace_goes_clothes_shopping_requirement(person):
    #     if candace.employed_since == -1 or candace.event_triggers_dict.get("clothes_shopping", 0) != 0:
    #         return False
    #     if candace.days_employed > 7:  #She's been working at least a week.
    #         return mc.business.has_funds(500) and candace.is_at_work
    #     return False
    #
    # def candace_overhear_supply_order_requirement(person):
    #     return time_of_day > 1 and person.sluttiness > 40 and day > candace.employed_since + 14 and person.is_at_work
    #
    # def candace_supply_order_discount_requirement():
    #     return time_of_day == 1 and mc.is_at_work and mc.business.is_open_for_business
    #
    # def candace_topless_at_mall_requirement(the_person):
    #     return the_person.love >= 40 and the_person.location in get_mall_locations()
    #
    # def candace_midnight_wakeup_requirement():
    #     if time_of_day == 4 and mc.business.research_tier >= 3 and candace.love >= 60:
    #         return day >= candace_starbuck_are_friends_day() + 7
    #     return False
    #
    # def candace_begin_cure_research_requirement(the_person):
    #     return the_person.is_at_work
    #
    # def candace_anti_bimbo_serum_requirement():
    #     if mc.business.is_open_for_business and mc.is_at_work:
    #         # lock for at least 2 weeks
    #         return day >= candace_get_living_with_stephanie_day() + 14
    #     return False
    #
    # def candace_cure_bimbo_requirement():
    #     if mc.business.is_open_for_business and mc.is_at_work:
    #         return mc.business.is_trait_researched(anti_bimbo_serum_trait)
    #     return False
    #
    # def candace_meet_doctor_candace_requirement():
    #     if mc.business.is_open_for_business and mc.is_at_work:
    #         return time_of_day == 2 and day >= candace_get_cure_day() + 7
    #     return False

    def candace_check_police_chief_met():
        if police_chief.title is None:  # haven't met, set title
            police_chief.set_possessive_title("The police chief")
            police_chief.set_mc_title("Mr. " + mc.last_name)
            police_chief.set_title("Officer " + police_chief.last_name)
        return

    #Candace Actions (define actions in init)
    candace_meet_at_office_store = Action("Meet Candi", candace_meet_at_office_store_requirement, "candace_meet_at_office_store_label")
    candace_get_to_know = Action("Get to know her {image=gui/heart/Time_Advance.png}", candace_get_to_know_requirement, "candace_get_to_know_label", menu_tooltip = "Find out more about Candi")
    candace_convince_to_quit = Action("Convince her to quit", candace_convince_to_quit_requirement, "candace_convince_to_quit_label", menu_tooltip = "Quit her current job and join your company.")
    # candace_goes_clothes_shopping = Action("Clothes shopping", candace_goes_clothes_shopping_requirement, "candace_goes_clothes_shopping_label")
    # candace_overhear_supply_order = Action("Overhear supply call", candace_overhear_supply_order_requirement, "candace_overhear_supply_order_label")
    # candace_supply_order_discount = Action("Candi reports success", candace_supply_order_discount_requirement, "candace_supply_order_discount_label")
    # candace_topless_at_mall = Action("Candi going topless", candace_topless_at_mall_requirement, "candace_topless_at_mall_label")
    # candace_midnight_wakeup = Action("Candi gets arrested", candace_midnight_wakeup_requirement, "candace_midnight_wakeup_label")
    # candace_begin_cure_research = Action("Candi moves", candace_begin_cure_research_requirement, "candace_begin_cure_research_label")
    # candace_anti_bimbo_serum = Action("Head Researcher makes a plan", candace_anti_bimbo_serum_requirement, "candace_anti_bimbo_serum_label")
    # candace_cure_bimbo = Action("Candi gets cured", candace_cure_bimbo_requirement, "candace_cure_bimbo_label")
    # candace_meet_doctor_candace = Action("Meet Doctor Candace", candace_meet_doctor_candace_requirement, "candace_meet_doctor_candace_label")

    def create_candace_character():
        #TODO candance wardrobe and base outfit
        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe")

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        global candace_role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "standard_body", face_style = "Face_12", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = candace_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job,  \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_skill_array = [2,3,4,1], sluttiness = 30, obedience_range = [50, 70], happiness = 76, love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Girlfriend", kids = 0, base_outfit = candace_base_outfit, type = 'story',
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves HR work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        candace.home.add_person(candace)
        candace.set_override_schedule(candace.home)
        return


    def make_candace_free_roam_and_set_intro_event():
        candace.SO_name = ophelia_get_ex_name()
        # candace.event_triggers_dict["met_at_store"] = 0
        # candace.event_triggers_dict["day_met"] = -1 #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        # candace.event_triggers_dict["learned_about_unhappy"] = 0
        # candace.event_triggers_dict["learned_about_bf_control"] = 0
        # candace.event_triggers_dict["learned_about_previous_work"] = 0
        # candace.event_triggers_dict["learned_about_uniform"] = 0
        # candace.event_triggers_dict["learned_about_pay"] = 0
        # candace.event_triggers_dict["relationship_doubt_score"] = 0  #Everytime you plant a seed of doubt, increment this.
        # candace.event_triggers_dict["quit_job"] = 0
        # candace.event_triggers_dict["last_talk_day"] = 0
        # candace.event_triggers_dict["clothes_shopping"] = 0
        # candace.event_triggers_dict["supply_discount_active"] = False
        # candace.event_triggers_dict["is_bimbo"] = True

        candace.set_override_schedule(office_store, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)
        return

    def create_debug_candace(): #Use this function to make a version of Candace for debug purposes.
        if "candace" in globals():
            renpy.say(None, "Candace already exists! Overwriting")

        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe") # This name will allow the rebuild_wardrobe function to generate a new one

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = candace_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job, \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_skill_array = [2,3,4,1], sluttiness = 35, obedience_range = [50, 70], happiness = 76, love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Girlfriend", SO_name = ophelia_get_ex_name(), kids = 0, base_outfit = candace_base_outfit, type = 'story',
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves supply work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        candace.set_schedule(purgatory, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.home.add_person(candace)
        # candace.event_triggers_dict["met_at_store"] = 0
        # candace.event_triggers_dict["day_met"] = day #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        # candace.event_triggers_dict["learned_about_unhappy"] = 0
        # candace.event_triggers_dict["learned_about_bf_control"] = 0
        # candace.event_triggers_dict["learned_about_previous_work"] = 0
        # candace.event_triggers_dict["learned_about_uniform"] = 0
        # candace.event_triggers_dict["learned_about_pay"] = 0
        # candace.event_triggers_dict["relationship_doubt_score"] = 0  #Everytime you plant a seed of doubt, increment this.
        # candace.event_triggers_dict["quit_job"] = 0
        # candace.event_triggers_dict["last_talk_day"] = 0
        # candace.event_triggers_dict["clothes_shopping"] = 0
        # candace.event_triggers_dict["supply_discount_active"] = False
        # candace.event_triggers_dict["is_bimbo"] = True

        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)

        return


    def create_debug_genius_candace():  #Use this function to make a version of genius Candace for debug purposes.
        if "candace" in globals():
            renpy.say(None, "Candace already exists! Overwriting")

        candace_base_outfit = Outfit("Candace's base accessories")
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.15, .15, .15, 0.95]
        candace_base_outfit.add_accessory(the_eyeshadow)

        candace_wardrobe = Wardrobe("Candace's Wardrobe") # This name will allow the rebuild_wardrobe function to generate a new one

        # her boyfriend only allows her to wear this 'company wardrobe'
        outfit = Outfit("Pink Lace Top And Leggings")
        outfit.add_upper(strappy_bra.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_upper(lace_crop_top.get_copy(),[.87, .44, .63, .95])
        outfit.add_lower(strappy_panties.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_lower(leggings.get_copy(),[.87, .44, .63, .95])
        outfit.add_feet(thigh_highs.get_copy(),[.15, .15, .15, 0.95])
        outfit.add_feet(high_heels.get_copy(),[.87, .44, .63, .95])
        outfit.add_accessory(lipstick.get_copy(),[.41, .16, .38, 0.5])
        outfit.add_accessory(heavy_eye_shadow.get_copy(),[.87, .44, .63, .6])
        candace_wardrobe.add_outfit(outfit)

        # init candace role
        candace_role = Role(role_name ="It\'s Complicated", actions =[candace_get_to_know, candace_convince_to_quit], hidden = True)
        candace_job = Job("Assistant", candace_role, purgatory, work_times = [1, 2])

        global candace
        candace = make_person(name = "Candace", last_name = "Hooper", age = 29, body_type = "thin_body", face_style = "Face_3", tits = "F", height = 0.94, hair_colour = ["black",[0.09,0.07,0.09,1]], hair_style = curly_bun, skin="black",\
            eyes = "light blue", personality = genius_personality, name_color = "#D2691E", starting_wardrobe = candace_wardrobe, job = candace_job, \
            stat_array = [3,1,5], skill_array = [2,1,2,1,5], sex_skill_array = [2,3,4,1], sluttiness = 35, obedience_range = [50, 70], happiness = 76, love = 0, \
            title = "Candi", possessive_title = "Your acquaintance",mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = candace_base_outfit, type = 'story',
            force_random = True, forced_opinions = [
                ["supply work", 2, True],        # she loves supply work
                ["skirts", 1, False],        #And Skirts
                ["the colour pink", 2, False], #She loves pink
                ["the colour yellow", 1, False],
                ["the colour purple", -2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],        #She hates pants!
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["being submissive", 1, False], # likes when others have their way with her
                ["giving handjobs", -2, False], # prefers to use other body parts...
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["cheating on men", 1, False]
            ])

        candace.generate_home()
        #candace.set_schedule(candace.home, the_times = [1,2])
        #candace.set_schedule(office_store, the_times = [3], the_days = [0, 1, 2, 3, 4]) #Buying office supplies for her employer.
        candace.home.add_person(candace)
        # candace.event_triggers_dict["met_at_store"] = 1
        # candace.event_triggers_dict["day_met"] = day #Might eventually change the code where candi gets INIT other than when you meet her, so leave this -1 for now
        # candace.event_triggers_dict["learned_about_unhappy"] = 1
        # candace.event_triggers_dict["learned_about_bf_control"] = 1
        # candace.event_triggers_dict["learned_about_previous_work"] = 1
        # candace.event_triggers_dict["learned_about_uniform"] = 1
        # candace.event_triggers_dict["learned_about_pay"] = 1
        # candace.event_triggers_dict["relationship_doubt_score"] = 8  #Everytime you plant a seed of doubt, increment this.
        # candace.event_triggers_dict["quit_job"] = 1
        # candace.event_triggers_dict["last_talk_day"] = day
        # candace.event_triggers_dict["clothes_shopping"] = 1
        # candace.event_triggers_dict["supply_discount_active"] = True
        # candace.event_triggers_dict["is_bimbo"] = False

        candace.add_unique_on_room_enter_event(candace_meet_at_office_store)
        mc.business.add_employee_supply(candace, False)

        return

label candace_meet_at_office_store_label(the_person):
    "As you browse some office furniture for your business, out of the corner of your eye you spot a vaguely familiar figure."
    $ the_person.draw_person()
    "Hmm... isn't that the bimbo that [salon_manager.title]'s ex is dating?"
    mc.name "Hey there... [the_person.title], right?"
    "She looks at you. She seems to recognize you."
    the_person "Ah! You must be the new guy. I'm here to pick up the umm... supplies... that we talked about on the phone."
    "Or not."
    mc.name "Sorry, you must have me confused with someone else. We met the other night, at a restaurant."
    "She squints at you for several seconds."
    the_person "Wait... you're the host? Right? I had a great time that night, at your restaurant!"
    mc.name "Actually, I was there as a customer. Just like you."
    the_person "Oh! I see. Sorry! I don't know what my problem is lately, I feel like I'm just so easily confused by things. I used to have a great memory!"
    "Sure you did..."
    mc.name "I understand. Anyway, are you meeting someone here?"
    the_person "Oh yes! I buy a lot of office supplies for my boyfriend's business here. I have an arrangement where they give me, well, a pretty good discount..."
    mc.name "Oh! That must be nice. I run a business myself, and a discount in supplies would be a wonderful thing to have."
    the_person "Oh yeah! It's easy! Do you want to know my secret?"
    mc.name "Certainly."
    "She comes close to you and whispers in your ear."
    the_person "When I pick up the supplies, I go to the backroom with the guy and suck his dick!"
    $ mc.change_locked_clarity(10)
    "You probably should have known that was coming."
    mc.name "Interesting. And your boyfriend... he is okay with this?"
    the_person "Oh yes! He says as long as they don't fuck me it's fine."
    "Hmm, so he isn't a cuck. He is just fine with using his bimbo girlfriend to further his business..."
    "?????""Ms. [the_person.fname]? I have your order ready for you in the back now."
    the_person "Oh! How exciting!"
    the_person "Nice to meet you again mister. I've got some work to do!"
    $ the_person.draw_person(position = "walking_away")
    "You watch as [the_person.title] walks to the back room to pick up her supplies."
    "There is something that just doesn't seem right here. You aren't sure what it is exactly, but you feel like you should really get to know [the_person.title] better."
    "If nothing else, maybe you could convince her to have a little fun sometime..."
    $ the_person.event_triggers_dict["met_at_store"] = 1
    return "Advance Time"

label candace_get_to_know_label(the_person):
    if the_person.happiness > 80: #Cap her happiness until we set her free.
        $ the_person.happiness = 80
    if candace_get_learned_about_unhappy():  #We have already learned she is unhappy, so learn more about why.
        "You consider what to talk to her about."
        menu:
            "Her Boyfriend":
                call candace_talk_about_bf_control(the_person) from _candace_chit_chat_choice_BF1
            "Her Previous Job":
                call candace_talk_about_previous_work(the_person) from _candace_chit_chat_choice_work1
            "Her Pay":
                call candace_talk_about_pay(the_person) from _candace_chit_chat_choice_pay1
            "Her Clothes":
                call candace_talk_about_uniforms(the_person) from _candace_chit_chat_choice_uniform1
        "You consider trying to push more on the subject, when you are interrupted."
        "?????""Ms. [the_person.fname]? I have your order ready for you in the back now."
        the_person "Yay! See you around [the_person.mc_title]!"
        $ the_person.draw_person(position = "walking_away")
        "You watch as [the_person.title] walks back to the storeroom."
        if candace_get_ready_to_quit():
            if candace_get_can_convince_to_quit():
                if ophelia_get_will_help_candace():
                    "You already talked to [salon_manager.title]. Next time you see [the_person.title], you should put the pressure on and see if you can convince her to quit and come work for you."
                elif the_person.love < 20:
                    "You can tell that [the_person.title] is wavering, but you sense hesitation. The conditions aren't quite right to get her to convince her to split with her boyfriend."
                    "Maybe if you got closer with her? If she had more affection for you, she might be more willing to break up with her asshole boyfriend."
                else:
                    "You feel like with one more push, you could probably get [the_person.title] to quit. But what will happen when you do?"
                    "You consider if for a few moments. You should probably ask for help. This guy sounds like a narcissist, and he could be trouble if you aren't careful."
                    "[salon_manager.title] used to date him... and she seems pretty knowledgeable about this kind of stuff. Maybe you should ask her for some help?"
                    $ salon_manager.event_triggers_dict["talk_about_candace"] = 1
            else:
                "You feel like you've just about convinced her that she could quit, but you need to learn more about her."
        else:
            "So far, she still seems pretty resolute on not quitting. Just keep chipping away, and you'll be able to convince her eventually!"
    else:
        mc.name "How are you doing today, [the_person.title]?"
        the_person "Oh... I'm doing okay I guess."
        mc.name "You guess?"
        the_person "Yeah... I guess, I just don't understand my boyfriend sometimes."
        mc.name "Guys can be confusing sometimes."
        the_person "I know! It's like, he's okay with me blowing the supply guys here for discounts on his work supplies."
        the_person "Then last night, I ordered a pizza and invited him over, and when he got there I was blowing the pizza guy to save some money on the tip..."
        $ mc.change_locked_clarity(10)
        "Does she ever stop sucking cock?"
        the_person "When he walked in, he got all pissed off! Like, why is it okay to do it to save money on one thing, but not something else?"
        mc.name "That does seem inconsistent."
        "She sighs."
        the_person "I know! The worst part is, he spanked me, which he knows I love, but then didn't do anything else!"
        $ mc.change_locked_clarity(10)
        the_person "I have needs! You can't just spank a girl and then not fuck her rough! It's just not right."
        mc.name "Exactly what I was thinking."
        the_person "I don't know what it is, I just feel like, something isn't right, you know? Like, I'm just in the wrong place."
        "Hmmm... very interesting."
        mc.name "You know... you don't have to work where you are now."
        the_person "Yeah... I guess... but then my boyfriend would dump me!"
        mc.name "I'm sure he would understand..."
        the_person "No no no, he already told me as much. He said, \'don't you think about quitting, or I'll dump you! and no one wants to date a dumb bimbo like you but me!\'"
        "Jesus, this guy sounds like a major narcissist. The more you learn about him, the more happy you are that [salon_manager.title] got away from him, even if involuntarily."
        the_person "And if he dumps me, who's going to fuck me every night? No, I think I'd better just stay where I'm at for now."
        $ mc.change_locked_clarity(10)
        $ the_person.event_triggers_dict["learned_about_unhappy"] = 1
        "?????""Ms. [the_person.fname]? I have your order ready for you in the back now."
        the_person "Oh! Finally! Some action! See you around [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "You watch as [the_person.title] rushes to the back of the store. There is absolutely something not right with what is going on."
        "She may not be the brightest, but [the_person.title] doesn't deserve to be treated this way. You think about it for a while, but make up your mind."
        "It is going to take some convincing. You might have to plant a few seeds of doubt here and there, but surely you can get her to quit her job and dump this guy."
        "Maybe you could convince her to work for you? She seems to have quite the knack for maintaining office supplies... maybe she would have a similar skill for medical and chemical supplies?"

    $ candace.event_triggers_dict["last_talk_day"] = day # prevent talk spamming (at least two days need to pass before you can plant the next seed)
    call advance_time from _call_advance_time_candace_get_to_know_label
    return

label candace_talk_about_bf_control(the_person):
    if candace_get_learned_about_bf_control():
        mc.name "How are things going with the boyfriend? Any better?"
        the_person "No! God no. Last night, I made him dinner. I was in the kitchen, wearing only an apron, hoping he would do something while I was cooking..."
        the_person "When I was almost done, I looked over, and he was asleep on the couch!"
        mc.name "Did you wake him up?"
        the_person "I umm... he doesn't let me wake him up... says his rest is very important..."
        mc.name "Aren't your needs important too?"
        the_person "Yeah... I guess? I don't know! I just don't like it when he gets mad at me."
        menu:
            "I would help meet your needs" if candace_get_mc_is_sexually_skilled():
                $ candace_increase_doubt()
                mc.name "You know, at my job, I always reward my employees, with a multitude of different types of rewards, or bonuses."
                mc.name "You work so hard, you deserve to have someone who meets your needs."
                the_person "Ha, it's hard to imagine having a man who could actually meet my needs."
                mc.name "Who says it has to be just one man? You have wonderfully free spirit, you should be free to share that spirit with anyone you want."
                $ mc.change_locked_clarity(5)
                if candace_get_ready_to_quit():
                    the_person "You know... I think you are right. But it's scary, you know? To leave what you know for something new."
                else:
                    the_person "You might be right... but I don't think I'm ready. It's scary, you know? To leave what you know."
            "I would help meet your needs\n{color=#ff0000}{size=18}Requires: high sex skills{/size}{/color} (disabled)" if not candace_get_mc_is_sexually_skilled():
                pass
            "Sorry to hear that":
                mc.name "I'm sorry to hear about your problems."
                the_person "That's okay. I'm sure it's just me, he was probably just tired after a long day at work... right?"

    else:
        mc.name "So, how are things going with your boyfriend?"
        the_person "Oh, as good as it can be, I guess."
        mc.name "I'm not sure. Is there something in particular that is bothering you?"
        the_person "Well, I don't mean to complain, but, it just feels like everyday there are more and more rules!"
        mc.name "He gives you... rules?"
        the_person "I mean, at first it was okay, and kinda made sense. No fucking other guys, stop spending all your pay-check at the strip club."
        the_person "But it feels like everyday he's adding some kind of new rule! I can hardly keep track of them all!"
        the_person "No going to the bar without him. No talking with the other men at his business. Leave my location setting shared with him on my phone."
        "It really does seem to be what you feared it might be. Her boyfriend is an overbearing psychopath."
        mc.name "[the_person.title]... that doesn't sounds like a healthy relationship."
        the_person "That's what I thought at first, but then he told me I'm not allowed to watch daytime talk shows anymore... I don't remember why I thought it was weird to be honest."
        $ candace.event_triggers_dict["learned_about_bf_control"] = 1
        $ candace_increase_doubt()
        "Yeah, you definitely need to help her get out of this."
        mc.name "You know, I've had a few girlfriends throughout the years. Part of the relationship is being open with each other, and trusting each other."
        the_person "Oh, don't worry! I trust him completely!"
        mc.name "But do you feel that he trusts you too?"
        the_person "Of course! I just feel bad. No one ever taught me relationships are supposed to have all these rules! Thankfully he is really patient with me though."
        "Hmm... you aren't sure that this approach is going to convince her."
        mc.name "So how long have you two been together?"
        if day < 180:
            the_person "Oh, we've been together now for a little over six months! Pretty crazy to think about!"
        elif day < 365:
            the_person "Oh we've been together for just over a year now! Pretty crazy to think about!"
        else:
            $ rel_length = str((day / 365) + 1)
            the_person "Oh, we've been together for a little over [rel_length] now! Pretty crazy to think about!"
            $ del rel_length
        "Wait a minute... you do the math in your head. You were there when [the_person.title]'s boyfriend broke up with with [salon_manager.title]. That means he had been cheating on her!"
        "Not just a narcissist, but a cheater as well. Yet another reason you really need to get her out of this situation."
    return

label candace_talk_about_previous_work(the_person):
    if candace_get_learned_about_previous_work():
        mc.name "Hey, remember what you told me about your previous job?"
        the_person "Yeah! I really liked that place. I wish I still worked there."
        mc.name "I did some research on that place. Guess what? It did research and production on small run pharmaceuticals, just like the business I run now!"
        the_person "Small run... what now?"
        mc.name "Drugs, basically. Like pills."
        the_person "Oh! Yeah I remember that! Checking boxes, taking notes, talking to people."
        $ candace_increase_doubt()
        mc.name "Yeah, my business does the same thing? You know, if you quit, I would totally hire you to work for me."
        if candace_get_ready_to_quit():
            the_person "That sounds amazing. Are you sure? I mean, I feel like there's something wrong with me sometimes. Are you sure you would take me?"
        else:
            the_person "That sounds too good to be true... so it must be! My boyfriend keeps telling me he's the only one who would put up with me. Are you sure you would take me?"
        mc.name "You would be great, I would love have someone like you on board."
    else:
        mc.name "I've heard you mention your previous job a couple of times. What did you do before?"
        the_person "Oh... well, to be honest, I don't actually remember much about it. It was at a place over on the east side of town, near the old car factory."
        the_person "I remember taking these vials of stuff... liquids I think! Mixing things together, shaking them up, taking a bunch of notes."
        mc.name "You were a researcher?"
        the_person "Yeah, a scientist or something like that! I don't remember how I did it, to be honest. Now it sounds so dull, but I remember really enjoying it at the time."
        mc.name "Do you know the name of the place? It sounds like somewhere I'd like to visit sometime."
        the_person "Oh... no actually I don't, but I remember the company logo! It was a neat science beaker with 4 hearts all around it."
        "Hmm. On the east side of town? You should look it up and see if you can find out more about it."
        $ candace.event_triggers_dict["learned_about_previous_work"] = 1
        #TODO new mandatory event where you look up the old business
    return

label candace_talk_about_uniforms(the_person):
    if candace_get_learned_about_uniform():
        mc.name "Any luck talking to your boyfriend about relaxing your dress code some?"
        the_person "No... no I haven't..."
        mc.name "Haven't talked to him?"
        the_person "No, I've tried to talk to him, but he shut it down and just said it was non negotiable."
        if candace_get_employees_have_lax_uniforms():
            mc.name "You know, the girls at my company have a much more... relaxed... dress code."
            the_person "Oh? Those girls sure are lucky!"
            mc.name "Yup! I have multiple uniforms available to choose from, from conservative business suits, to topless with a set of yoga pants."
            the_person "You... you let girls go topless? That sounds... SO COMFY!!!"
            $ mc.change_locked_clarity(10)
            $ candace_increase_doubt()
            mc.name "It is! You would like it there. You know if you quit, I would hire you to work there, right?"
            if candace_get_ready_to_quit():
                the_person "I bet I would like it there! Maybe it's about time to make a change in my life."
            else:
                the_person "I think you might be right, but I don't think I'm ready. It's scary, you know? To leave what you know."
            mc.name "You would fit in wonderfully at my company."
    else:
        mc.name "I can't help but notice, every time I see you here, you have the same outfit on."
        the_person "Oh god, don't get me started. I fucking hate pants!"
        #TODO learn she hates pants
        mc.name "Ah, then why do you wear them?"
        the_person "I just got off work. My boyfriend made uniforms for everyone at work to wear pants."
        the_person "I used to wear skirts. It was great! Such easy access... and if you don't wear panties it's so easy to just, sit on someone's lap or face or whatever."
        $ mc.change_locked_clarity(20)
        mc.name "That does sound handy. Why did your boyfriend change the dress code?"
        the_person "Ah, it was my fault really. One time I was wearing this short skirt and no panties, and I was bending over to get something out from under my desk I had dropped..."
        the_person "Suddenly I felt someone's hands on my ass, feeling me up. I thought it was my boyfriend! I asked him for a quickie and soon he was fucking me."
        the_person "Imagine my surprise when my boyfriend comes around the corner! I looked back and realized it wasn't him!"
        mc.name "He didn't care for that?"
        the_person "No, he fired the guy right then and there. Then he told me I'm not allowed to wear skirts to work anymore!"
        $ candace.event_triggers_dict["learned_about_uniform"] = 1
        mc.name "That sounds awfully restrictive. Don't you think you should be able to wear what you want to work?"
        the_person "Oh, I mean, it would be nice, but I kind of understand. It keeps accidents like getting fucked by random guys from happening!"
        "She says the last bit of that sentence with as much resolve as she can muster, but you can tell from the tone her voice, she wishes it would happen once in a while anyway..."
        mc.name "You should talk to your boyfriend about it. Maybe he would let you wear a skirt if you promise to make it a certain length? Or to wear panties?"
        the_person "Hmm... that's not a bad idea! I'll have to try that sometime!"
        $ candace_increase_doubt()
    return

label candace_talk_about_pay(the_person):
    if candace_get_learned_about_pay():
        mc.name "You know, the girls who work for me, make about as much money as you do per week in a day working for me."
        the_person "Aww, you pay so well! You must really take care of your employees."
        mc.name "I'm always on the lookout for talented employees. I think you would make a good employee. You interested? I promise you'll make a lot more than you are now!"
        $ candace_increase_doubt()
        if candace_get_ready_to_quit():
            the_person "You know, I can't believe I'm saying this, but I've been seriously considering it!"
        else:
            the_person "Oh, I'm okay, I don't need the money. But I suppose it would be nice to have."
    else:
        mc.name "So, as a business owner, with several employees of my own, I have a question for you."
        the_person "Sure! Go ahead."
        mc.name "How much does your job pay, to have talent like yours?"
        the_person "Oh! I work on commission! I keep half of the money I save the company on office supplies!"
        mc.name "Ah... but what about your base rate?"
        the_person "Base rate?"
        mc.name "Yeah, like, how much do you get paid per hour, or per day? Or do you have a salary?"
        the_person "Oh, no, it's commission only! My boyfriend says working on commission will help keep me motivated to work hard!"
        mc.name "I see... and how much commission do you usually make?"
        the_person "Oh, well, I average about $20, but sometimes when I let the stock boy play with my ass I can make as much as $25!"
        mc.name "Per day?"
        the_person "Oh no, not that much. Per week!"
        mc.name "I see... and how much do you work?"
        the_person "Oh, I'm out there pretty much 9am to 5pm on weekdays..."
        "That is criminally low pay. Yet another reason you really need to get her out of this situation."
        mc.name "You know, I'm pretty sure literally ANY job would pay you more."
        the_person "Yeah, but you know the economy these days. It would be hard for someone like me to find work!"
        mc.name "Yeah, but you should probably really talk to your boyfriend about paying you more. It might be illegal how little you are making."
        the_person "Ah, I suppose, but I'm okay with it. My boyfriend puts the money back into the business anyway!"
        mc.name "But how do you afford, say, rent?"
        the_person "Oh! That's easy! I have another little agreement with my landlord. Instead of rent..."
        mc.name "That's okay. I think I get the picture."
        $ candace.event_triggers_dict["learned_about_pay"] = 1
    return

label candace_convince_to_quit_label(the_person):
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person)
    $ ex_name = ophelia_get_ex_name()
    "Alright. This is it. It's now or never."
    mc.name "[the_person.title]... can I talk to you about something? Something important?"
    the_person "Oh, of course! What is it?"
    mc.name "This isn't easy to say, but, I want you to quit your job and come work for me."
    the_person "Ha, I know, I know, you keep saying that, but..."
    mc.name "I'll pay you $40 a day. Effective immediately."
    the_person "Oh! That's more than I make in a week! But I don't know..."
    mc.name "I know you used to work at a pharmaceuticals company. You told me you used to love that place! You could work at one again!"
    the_person "[the_person.mc_title], I really do have fond memories... from what I can remember... but I don't think I can do that kind of work again..."
    mc.name "You don't have to do research. My company is constantly sourcing chemicals and reagents for different products. It wouldn't be any different than what you are doing now, helping keep supplies up!"
    the_person "I just don't know. God, is it getting hot in here?"
    mc.name "Probably. Are you overheating? Wouldn't it be nicer if you could go back to wearing skirts again?"
    the_person "It really would be, to feel the breeze between my legs again."
    mc.name "Just do it. Just say yes, it will be worth it, I promise."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    the_person "I want to... I really do..."
    mc.name "Then why don't you?"
    the_person "I'm... I'm so scared! [ex_name]... I think he knows I've been thinking about leaving! Last night he told me if I quit, he's going to expose that I've been trading sexual favors for discounts..."
    the_person "He says it's illegal! That I'll go to jail for being a prostitute!"
    mc.name "Don't worry, I know someone who can help. I have a friend who has dealt with a similar situation... let's say she can handle herself."
    mc.name "She can help you. Take a leap of faith. You can trust me."
    "She thinks about it for a bit."
    "?????""Ms. [the_person.fname]? I have your order ready for you in the back now."
    "She looks over at the clerk. She seems to make up her mind."
    the_person "Actually... I'm really sorry. I can't take the delivery tonight."
    "?????""Oh? Okay Ms. [the_person.fname]. Have a good night!"
    the_person "I think I will."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "Alright mister. I'm going to trust you. What do we do?"
    mc.name "Let's go to my friend's. She'll help us get set up."
    the_person "Lead the way!"
    "Thankfully, the office supply store is right next to the mall, so it is a quick walk over to the salon."
    $ mc.change_location(mall_salon)
    "As you walk into the salon, you notice that [salon_manager.title] is working with a customer."
    mc.name "Okay, she's over there, but she's with a customer right now. While we wait for her, why don't we do the paperwork for your new employment?"
    the_person "Okay... let's do it!"
    "There is a small table to the side of the room. You sit down and start to go through it with [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")

    $ mc.business.add_employee_supply(the_person)
    $ town_relationships.update_relationship(salon_manager, the_person, "Friend")

    "You complete the necessary paperwork and hire [the_person.title], assigning her to the supply department."
    "As you finish up, you notice [salon_manager.possessive_title] is walking over to the table."
    $ scene_manager.add_actor(salon_manager, position = "sitting", display_transform = character_left_flipped)
    salon_manager "Hello! I'm [salon_manager.name]. I don't think we've been properly introduced."
    the_person "Hi! You can call me [the_person.fname]."
    salon_manager "You know, I used to date [ex_name] too!"
    the_person "Right... used to... kind of weird to think about, this is all happening so fast!"
    salon_manager "Don't worry. First thing's first! Do you have your phone handy? Let's take a picture together!"
    the_person "Okay! I love selfies."
    "[the_person.title] and [salon_manager.possessive_title] lean together and take a picture."
    salon_manager "There we go! That will be a great picture to send with your break up text..."
    "Oh boy. Things are about to get juicy."
    salon_manager "Let me see your phone now. Okay here we go."
    salon_manager "Guess who I met today, [ex_name]! Turns out we having something in common!..."
    "You spend the next hour or so getting [the_person.title] all set up. [salon_manager.title] really does think of everything."
    $ the_person.relationship = "Single"
    $ the_person.SO_name = None
    $ the_person.remove_role(affair_role)   # people can get her to this role before she quits
    $ the_person.change_happiness(30)
    "She's got new passwords on everything from bank accounts, to social media. A locksmith is already en route to change her locks, and she's blocked her ex from her phone completely."
    "After a while, you notice they seem to be done, and now they are just trading stories and gossip. They actually seem to be getting along okay."
    "You stand up and stretch."
    mc.name "Well... I don't know about you two, but I'm pretty worn out. Take care. And [the_person.title], I'll see you at the office!"
    the_person "Sure thing boss! Oh! Should I call you boss now? Oh that sounds nice!"
    menu:
        "Boss\n{color=#00ff00}{size=18}+10 Obedience{/size}{/color}":
            $ the_person.set_mc_title("Boss")
            $ the_person.change_obedience(10)
        "[mc.name]\n{color=#00FF00}{size=18}+10 Love{/size}{/color}":
            $ the_person.set_mc_title(mc.name)
            $ the_person.change_love(10)
    the_person "Whatever you say [the_person.mc_title]!"
    $ the_person.change_happiness(10)
    "Well, you now have your very own office bimbo. While before you were just looking to get her out of a bad situation, you are now considering some of the possibilities open to you..."
    $ the_person.set_possessive_title("Your Office Bimbo")
    mc.name "Alright, well have a good night."
    salon_manager "Goodnight!"
    the_person "Bye!"
    $ candace.event_triggers_dict["quit_job"] = 1
    # she has quit her job, give her a new wardrobe
    $ rebuild_wardrobe(candace, force = True)
    $ candace.set_override_schedule(None)
    $ candace.add_unique_on_talk_event(candace_goes_clothes_shopping)
    $ candace.add_unique_on_talk_event(candace_overhear_supply_order)
    $ candace.add_unique_on_talk_event(candace_goes_clothes_shopping)
    $ candace.set_event_day("obedience_event")
    $ candace.set_event_day("love_event")
    $ candace.set_event_day("slut_event")
    $ candace.set_event_day("story_event")

    call advance_time from _call_advance_time_candace_convince_to_quit_label
    return


#Character variable wrappers
init 3 python:
    def candace_get_day_met():
        return candace.event_triggers_dict.get("day_met", -1)

    def candace_get_met_at_store():
        return candace.event_triggers_dict.get("met_at_store", 0)

    def candace_get_learned_about_unhappy():
        return candace.event_triggers_dict.get("learned_about_unhappy", 0)

    def candace_get_learned_about_bf_control():
        return candace.event_triggers_dict.get("learned_about_bf_control", 0)

    def candace_get_learned_about_previous_work():
        return candace.event_triggers_dict.get("learned_about_previous_work", 0)

    def candace_get_learned_about_uniform():
        return candace.event_triggers_dict.get("learned_about_uniform", 0)

    def candace_get_learned_about_pay():
        return candace.event_triggers_dict.get("learned_about_pay", 0)

    def candace_get_employees_have_lax_uniforms():
        return reduced_coverage_uniform_policy.is_active

    def candace_get_mc_is_sexually_skilled():
        if (mc.sex_skills["Foreplay"] + mc.sex_skills["Oral"] + mc.sex_skills["Vaginal"] + mc.sex_skills["Anal"]) > 16 : #Average of 4 or better across sex skills.
            return True
        return False

    def candace_get_ready_to_quit():
        if candace.event_triggers_dict.get("relationship_doubt_score", 0) >= 5:
            return True
        return False

    def candace_get_can_convince_to_quit():
        if candace_get_ready_to_quit():
            if candace_get_learned_about_pay() and candace_get_learned_about_previous_work() and candace_get_learned_about_uniform() and candace_get_learned_about_bf_control():
                if candace_get_employees_have_lax_uniforms() or candace_get_mc_is_sexually_skilled():
                    return True
        return False

    def candace_get_has_quit_job():
        if "candace" in globals():
            return candace.event_triggers_dict.get("quit_job", 0) != 0
        return False

    def candace_can_talk():
        if "candace" in globals():
            return candace.event_triggers_dict.get("last_talk_day", 0) < day
        return False

    def candace_increase_doubt():
        score = candace.event_triggers_dict.get("relationship_doubt_score", 0)
        candace.event_triggers_dict["relationship_doubt_score"] = score + 1
        return

    def candace_get_has_gone_clothes_shopping():
        if "candace" in globals():
            return candace.event_triggers_dict.get("clothes_shopping", 0) != 0
        return False

    def candace_update_action_lists():  #This function is designed to try and bring action lists up to date, from update to update, so we don't have to start a new game every time.
        if candace_get_has_quit_job():
            if not candace_get_has_gone_clothes_shopping():
                candace.add_unique_on_talk_event(candace_goes_clothes_shopping)
        return

    def candace_is_giving_supply_discount():
        if candace.is_employee:
            return candace.event_triggers_dict.get("supply_discount_active", False)
        return False

    def candace_calculate_discount():
        disc_mult = 1.0
        if "candace" in globals():
            if candace.is_employee:
                if candace_is_giving_supply_discount():
                    if candace.personality == bimbo_personality:
                        disc_mult = 0.90
                    else:
                        disc_mult = 0.80
        if mc.business.IT_project_is_active(supply_storage_project):
            disc_mult -= 0.05
        return disc_mult

    def candace_starbuck_are_friends_day():
        if "candace" in globals():
            return candace.event_triggers_dict.get("friends_with_starbuck", 9999)
        return 9999

    def candace_get_cure_day():
        if "candace" in globals():
            return candace.event_triggers_dict.get("cure_day", 9999)
        return 9999

    def candace_get_living_with_stephanie_day():
        if "candace" in globals():
            return candace.event_triggers_dict.get("living_with_stephanie", 9999)
        return 9999

    def candace_get_sex_record_difference_tier(): #Use this to determine what dialogue to run after curing her bimboism. Made a function because messy
        old_dict = candace.event_triggers_dict.get("sex_record_snapshot", None)
        if old_dict is None:
            return 0
        if old_dict["Vaginal Sex"] < candace.sex_record["Vaginal Sex"] or old_dict["Anal Sex"] < candace.sex_record["Anal Sex"]: #You fucked her at least once
            if old_dict["Vaginal Sex"] + old_dict["Anal Sex"] + 2 <= candace.sex_record["Vaginal Sex"] + candace.sex_record["Anal Sex"]: #Sex at least twice
                if old_dict["Vaginal Creampies"] + old_dict["Anal Creampies"] + 2 <= candace.sex_record["Vaginal Creampies"] + candace.sex_record["Anal Creampies"]:
                    return 4
                else:
                    return 3
            else:
                return 2
        if old_dict["Handjobs"] < candace.sex_record["Handjobs"] or old_dict["Blowjobs"] < candace.sex_record["Cunnilingus"] or old_dict["Cunnilingus"] < candace.sex_record["Blowjobs"]or old_dict["Fingered"] < candace.sex_record["Fingered"]:
            return 1
        return 0
