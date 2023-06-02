# ****Sarah profile****
# Personality type: Outgoing, extrovert.
# Background: Childhood friend. Moved away when you were kids but recently moved back to pursue a job that didn't work out. Now selling solar panels door to door, knocks on your door randomly.
#   Has a great HR resume.
#   After first chance meeting, unlocks the HR Supervisor organization policy that unlocks the role and increases maximum company size by 1.
#   After unlocking the policy, the player calls Sarah and hires her.
#   First level corruption:
#   Second level corruption: You catch her stealing breast enhancing serums. Option to forbid her, allow her, or encourage her.
#
#
# Required labels:
# INTRO
# Hire
# Story arc part one: She catches you in the office on Saturday, invites you to bar where she is meeting a friend. Close the bar down with her
# Story arc part two: She comes looking for you at the office on Saturday. Invites you out to drinks with jut her. She winds up at your place.
# Story arc part three: Catch her swiping breast enhancement serums on friday  NOTE: Part three has separate requirements from one and two and could happen before or after either part.
# Following monday, observe the results
# Story part four: Date night, starts with drinks, ends at a strip club
#
# Intro: mandatory event, in the AM knocks on MC home selling solar panels.
# Hiring: mandatory event. Call up Sarah and hire her for the HR position.

init 2 python:
    list_of_instantiation_functions.append("create_sarah_character")
    list_of_instantiation_functions.append("create_naomi_character")

    sarah_strip_pose_list = ["walking_away","back_peek","standing_doggy","stand2","stand3","stand4","stand5", "doggy","kneeling1"]

    def alternative_hire_sarah_requirement(the_person):
        return not mc.business.hr_director and HR_director_creation_policy.is_owned and the_person.event_triggers_dict.get("alt_hire", False)

    def create_sarah_character():
        sarah_wardrobe = wardrobe_from_xml("Sarah_Wardrobe")

        sarah_base_outfit = Outfit("Sarah's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_eyeshadow = light_eye_shadow.get_copy()
        the_eyeshadow.colour = [.45,.31,.59,1.0]
        sarah_base_outfit.add_accessory(the_glasses)
        sarah_base_outfit.add_accessory(the_eyeshadow)

        # give player one more chance to hire her as HR director
        alt_hire_action = Action("Hire her as HR Director", alternative_hire_sarah_requirement, "Sarah_alternative_hire_label")

        # init Sarah role
        global sarah_role
        sarah_role = Role(role_name ="Childhood Friend", actions =[alt_hire_action], role_dates = [sarah_bar_date_ask_action], hidden = True)
        # initial representative job
        sarah_initial_job = Job("Representative", critical_job_role, work_days = [], work_times = [])

        global sarah
        sarah = make_person(name = "Sarah", last_name ="Cooper", age = 21, body_type = "thin_body", face_style = "Face_3", tits = "A", height = 0.90, hair_colour = ["chocolate", [.247, .0, .058, 1]], hair_style = windswept_hair, skin="white",\
            eyes = "dark blue", personality = Sarah_personality, name_color = "#dda0dd", starting_wardrobe = sarah_wardrobe, \
            stat_array = [5,3,3], skill_array = [5,3,2,1,1], sex_skill_array = [1,2,3,1], sluttiness = 3, happiness = 102, love = 3, \
            title = "Sarah", possessive_title = "Your childhood friend",mc_title = mc.name, relationship = "Single", kids = 0, base_outfit = sarah_base_outfit, type = 'story', \
            force_random = True, forced_opinions = [
                ["HR work", 2, True],        # she loves HR work
                ["work uniforms", 1, False], # she likes uniforms
                ["Mondays", 1, False],       # she likes mondays, and monday meetings!
                ["working", 1, False],       # a bit of a workaholic
                ["the colour purple", 2, False], #She loves purple!
                ["skirts", 1, False],        #And Skirts
                ["the colour red", -2, False], #She hates red
                ["yoga", 2, False]          #She helps us establish the yoga class
            ], forced_sexy_opinions = [
                ["taking control", 1, False], # she likes taking control, type A
                ["giving handjobs", 2, False], # Not afraid to get her hands dirty ;)
                ["giving blowjobs", 1, False], # make sure she likes blowjobs (HR meeting)
                ["showing her tits", -2, False], # She hates showing her small tits
            ])

        sarah.generate_home()
        sarah.add_role(sarah_role)
        sarah.change_job(sarah_initial_job, job_known = True)
        sarah.set_override_schedule(sarah.home)
        sarah.home.add_person(sarah)

        # Sarah_mod_initialization(): #Add actionmod as argument#
        # sarah.event_triggers_dict["yoga_voyeur"] = False
        # sarah.event_triggers_dict["gym_tshirt"] = False
        # sarah.event_triggers_dict["epic_tits_progress"] = 0    # 0 = not started, 1 = mandatory event triggered, 2 = tits epic, -1 = convinced her not to do it
        # sarah.event_triggers_dict["drinks_out_progress"] = 0   # 0 = not started, 1 = third wheel event complete, 2 = grab drinks complete
        # sarah.event_triggers_dict["dating_path"] = False       # False = not started, or doing FWB during story, True = dating her.
        # sarah.event_triggers_dict["stripclub_progress"] = 0    # 0 = not complete, 1 = strip club even complete
        # sarah.event_triggers_dict["initial_threesome_target"] = None    #this will hold who sarah decides she wants to have a threesome with.
        # sarah.event_triggers_dict["threesome_unlock"] = False     #\\
        # sarah.event_triggers_dict["try_for_baby"] = 0         # 0 = not trying, 1 = trying for baby, 2 = knocked up
        # sarah.event_triggers_dict["fertile_start_day"] = -1    #-1 means not fertile, otherwise is the day that she tells MC she is fertile. Using math we can determine if she is fertile in the future.
        # sarah.event_triggers_dict["fertile_start_creampie_count"] = -1  #Set this to the total number of creampies she has had at the beginning of her fertile period.
        # sarah.event_triggers_dict["special_tit_fuck"] = False

        # add appoint
        office.add_action(HR_director_appointment_action)

        Sarah_intro = Action("Sarah_intro",Sarah_intro_requirement,"Sarah_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        mc.business.add_mandatory_morning_crisis(Sarah_intro) #Add the event here so that it pops when the requirements are met.
        return

    def create_naomi_character():     # initializes her and returns person
        global naomi
        naomi = make_person(name = "Naomi", last_name = "Walters", age = 23, body_type = "thin_body", face_style = "Face_3", height = 0.94, hair_colour = ["alt blond", [.882, .733, .580, 1]], hair_style = braided_bun, \
            skin="white", relationship = "Fiancée", kids = 0, tits = "DD", sluttiness = renpy.random.randint(25, 40), job = unemployed_job, type = 'story', force_random = True, forced_opinions = [
                ["skirts", 1, False],
                ["other girls", 1, False],
                ["boots", 1, False],
                ["the colour yellow", 2, False],
                ["the colour blue", 2, False],
                ["the colour green", -2, False],
                ["pants", -2, False],
                ["high heels", 2, False]
            ], forced_sexy_opinions = [
                ["taking control", 1, False],
                ["threesomes", 2, False],
                ["giving handjobs", -2, False],
                ["skimpy outfits", 1, False],
                ["showing her tits", 2, False],
                ["not wearing underwear", 2, False],
                ["anal sex", -2, False]
            ])
        naomi.generate_home()
        naomi.home.add_person(naomi)
        naomi.set_title(naomi.name)
        naomi.set_mc_title(mc.name)
        naomi.set_possessive_title("Sarah's slutty friend")
        # hide her from player until she is reintroduced into the story
        naomi.set_override_schedule(naomi.home)
        town_relationships.update_relationship(sarah, naomi, "Best Friend")
        return

    def Sarah_reset_vars():
        if sarah.has_large_tits:
            sarah.event_triggers_dict["epic_tits_progress"] = 2
        sarah.event_triggers_dict["drinks_out_progress"] = 0
        sarah.event_triggers_dict["dating_path"] = False
        return

    def get_Sarah_willing_threesome_list():
        target_list = []
        if willing_to_threesome(sarah, mom):
            target_list.append(mom)
        if willing_to_threesome(sarah, lily):
            target_list.append(lily)
        if willing_to_threesome(sarah, starbuck):
            target_list.append(starbuck)
        if willing_to_threesome(sarah, cousin):
            target_list.append(cousin)
        if willing_to_threesome(sarah, aunt):
            target_list.append(aunt)
        if willing_to_threesome(sarah, nora):
            target_list.append(nora)
        for person in [x for x in mc.business.employee_list if not x == sarah and willing_to_threesome(sarah, x)]:
            if not person in target_list:
                target_list.append(person)

        return target_list

    def sarah_foreplay_position_filter(foreplay_positions):
        if sarah_get_special_titfuck_unlocked():
            filter_out = [tit_fuck]
            return not foreplay_positions[1] in filter_out
        return True

    def sarah_oral_position_filter(oral_positions):
        return True

    def sarah_vaginal_position_filter(vaginal_positions):
        return sarah_get_sex_unlocked()

    def sarah_anal_position_filter(anal_positions):
        return sarah_get_sex_unlocked() \
            and sarah.sex_record.get("Vaginal Creampies", 0) > 3

    def sarah_unique_sex_positions(person, prohibit_tags = []):
        positions = []
        if sarah_get_special_titfuck_unlocked() and "Foreplay" not in prohibit_tags:
            positions.append([sarah_tit_fuck, 1])
        return positions

    def sarah_epic_tits_progress():
        return sarah.event_triggers_dict.get("epic_tits_progress", 0)

    def sarah_threesomes_unlocked():
        return sarah.event_triggers_dict.get("threesome_unlock", False)

    def sarah_get_special_titfuck_unlocked():
        return sarah.event_triggers_dict.get("special_tit_fuck", False)

    def sarah_get_sex_unlocked():
        return sarah.event_triggers_dict.get("drinks_out_progress", 0) >= 2

    def Sarah_intro_requirement():
        return day >= TIER_1_TIME_DELAY and mc.is_home

    def Sarah_hire_requirement(day_trigger):
        if day > day_trigger and HR_director_creation_policy.is_owned:
            return True
        return False

    def Sarah_catch_stealing_requirement():
        if strip_club_is_closed(): #Don't run while the strip club is closed
            return False
        return day%7 == 4 and time_of_day == 3 and sarah.is_available and mc.is_at_work

    def Sarah_new_tits_requirement():
        if time_of_day == 0:    # triggers right when she comes into office
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_epic_tits_requirement():
        if time_of_day == 0:    # triggers right when she comes into office
            if day%7 == 0:  #Monday
                return True
        return False

    def Sarah_third_wheel_requirement():
        if sarah_epic_tits_progress() == 1: #Don't run this if epic tits is in progress
            return False
        if day%7 == 5 and time_of_day > 2 and sarah.sluttiness >= 20 and sarah.love >= 20:
            return sarah.is_available and mc.is_at_work
        return False

    def Sarah_get_drinks_requirement():
        if sarah_epic_tits_progress() == 1: #Don't run this if epic tits is in progress
            return False
        if time_of_day > 2 and day%7 == 5 and sarah.sluttiness > 40 and sarah.love > 40:
            return sarah.is_available and mc.is_at_work and get_HR_director_tag("business_HR_sexy_meeting", False)
        return False

    def Sarah_watch_yoga_at_gym_requirement(the_person):
        return sarah.sluttiness > 20 and sarah.location == gym

    def Sarah_stripclub_story_requirement():
        if sarah_epic_tits_progress() < 2 and not sarah_epic_tits_progress() == -1:  #Don't run until after she has bigger tits of you convinced her not to do it
            return False
        if strip_club_is_closed(): # Don't run while strip club is closed
            return False
        #Only in the evening when the strippers are at the club
        if time_of_day > 2 and day%7 == 5 and sarah.sluttiness > 50 and sarah.love >= 60:  #Saturday
            return sarah.is_available and mc.is_at_work
        return False

    def Sarah_workout_in_tshirt_requirement(the_person):
        return sarah.sluttiness > 60 and sarah.location == gym

    def Sarah_threesome_request_requirement():
        if time_of_day > 2 and day%7 == 5 and sarah.sluttiness >= 80:
            if sarah.is_available and mc.is_at_work:
                # at least three choices for who to hook up with
                return __builtin__.len(get_Sarah_willing_threesome_list()) >= 3
        return False

    def Sarah_arrange_threesome_requirement(the_person):
        return True

    def Sarah_initial_threesome_requirement():
        return time_of_day > 2 and day%7 == 5 and sarah.is_available

    def Sarah_ask_for_baby_requirement():
        return False    #Disabling this event since it is covered by breeding fetish intro.
        if mc.is_in_bed and sarah.has_role(girlfriend_role) and not sarah.is_pregnant:
            if sarah_threesomes_unlocked() and sarah.sex_record["Vaginal Creampies"] >= 10:
                return True
        return False

    def Sarah_fertile_period_start_requirement():  #When this returns true, start the fertile period
        if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
            return sarah.is_highly_fertile
        return False

    def Sarah_fertile_period_end_requirement():     #When this returns true, end the fertile period
        if sarah.event_triggers_dict.get("try_for_baby", 0) == 1:
            return not sarah.is_highly_fertile
        return False

    def Sarah_try_for_baby_dialogue():  #Just a wrapper to make it easier to make if statements for baby making related dialogue
        return sarah.event_triggers_dict.get("try_for_baby", 0) == 1

    def Sarah_has_bigger_tits():
        return sarah_epic_tits_progress() > 1 or sarah.has_large_tits

    def Sarah_remove_bra_from_wardrobe(wardrobe):  #Test this function
        for outfit in [x for x in wardrobe.outfit_sets if x.wearing_bra]:
            outfit.remove_clothing(outfit.get_bra())
        for outfit in [x for x in wardrobe.underwear_sets if x.wearing_bra]:
            outfit.remove_clothing(outfit.get_bra())

    def Sarah_weekend_surprise_crisis_requirement():
        return False    #Disable event for now
        if time_of_day > 1 and day%7 == 5:  #Saturday
            if mc.is_at_work and sarah_get_sex_unlocked():   #You've gotten drinks out with Sarah before.
                return True
        return False

    def Sarah_unlock_special_tit_fuck_requirement():  #Not an action, but make a requirement to make it easy to test anyway.
        return sarah.sex_record.get("Tit Fucks", 0) > 3 and not sarah_get_special_titfuck_unlocked()

    def naomi_reconciliation_requirement(the_person):
        return time_of_day > 0 and time_of_day < 4 and the_person.location in mall_hub

    def talk_to_sarah_about_naomi_requirement(the_person):
        return mc.is_at_work and mc.business.is_open_for_business

    def naomi_visits_to_apologize_requirement(the_day):
        if day <= the_day:
            return False
        if day % 7 != 2 or time_of_day != 2:
            return False
        return True

    def roll_dart_odds(target = 50, focus_score = 0):
        dart_roll = 0
        ran_num = renpy.random.randint(0,100)
        if target == 50:
            if ran_num < (20 + (focus_score * 4)): #Bullseye!
                dart_roll = 50
            elif ran_num < (50 + (focus_score * 5)): #HIT
                dart_roll = 25
            else:
                dart_roll = renpy.random.randint(1,20)
            pass
        elif target == 25:
            if ran_num < (40 + (focus_score * 4)): #HIT
                dart_roll = 25
            elif ran_num < (50 + (focus_score * 4)): #Bullseye!
                dart_roll = 50
            else:
                dart_roll = renpy.random.randint(1,20)
        else:
            if ran_num < (50 + (focus_score * 4)):
                dart_roll = target
            else:
                dart_roll = renpy.random.randint(1,20)

        renpy.say(None, "The dart hits " + str(dart_roll) + "!")
        return dart_roll

    def get_sarah_spend_night_threesome_possibility():
        threesome_wakeup = False
        threesome_partner = None
        if sarah_threesomes_unlocked() and renpy.random.randint(0,100) < 50:
            if renpy.random.randint(0,100) < 10: #Try lily first
                if willing_to_threesome(the_person, lily):
                    threesome_partner = lily
                    threesome_wakeup = True
                elif willing_to_threesome(the_person, mom):
                    threesome_partner = mom
                    threesome_wakeup = True
            else:
                if willing_to_threesome(the_person, mom):
                    threesome_partner = mom
                    threesome_wakeup = True
                elif willing_to_threesome(the_person, lily):
                    threesome_partner = lily
                    threesome_wakeup = True
        return (threesome_wakeup, threesome_partner)

    def test_bra_function(the_person):
        Sarah_remove_bra_from_wardrobe(the_person.wardrobe)

    def add_sarah_watch_yoga_at_gym_action():
        Sarah_watch_yoga_at_gym_action = Action("Sarah does yoga", Sarah_watch_yoga_at_gym_requirement, "Sarah_watch_yoga_at_gym_label")
        sarah.add_unique_on_room_enter_event(Sarah_watch_yoga_at_gym_action)

    def add_sarah_epic_tits_action():
        Sarah_epic_tits_action = Action("Sarah Epic Tits Action", Sarah_epic_tits_requirement, "Sarah_epic_tits_label")
        mc.business.add_mandatory_crisis(Sarah_epic_tits_action)

    def add_sarah_get_drinks_action():
        Sarah_get_drinks_action = Action("Sarah get drinks",Sarah_get_drinks_requirement,"Sarah_get_drinks_label")
        mc.business.add_mandatory_crisis(Sarah_get_drinks_action)

    def add_sarah_stripclub_story_action():
        Sarah_stripclub_story_action = Action("Sarah Strip Club",Sarah_stripclub_story_requirement,"Sarah_stripclub_story_label")
        mc.business.add_mandatory_crisis(Sarah_stripclub_story_action)

    def add_sarah_hire_action():
        Sarah_hire_action = Action("Sarah hire",Sarah_hire_requirement,"Sarah_hire_label", requirement_args = day)
        mc.business.add_mandatory_crisis(Sarah_hire_action)

    def add_sarah_new_tits_action():
        Sarah_new_tits_action = Action("Sarah new tits",Sarah_new_tits_requirement,"Sarah_new_tits_label")
        mc.business.add_mandatory_crisis(Sarah_new_tits_action)

    def add_sarah_workout_in_tshirt_action():
        Sarah_workout_in_tshirt_action = Action("Sarah works out",Sarah_workout_in_tshirt_requirement,"Sarah_workout_in_tshirt_label")
        sarah.add_unique_on_room_enter_event(Sarah_workout_in_tshirt_action)

    def add_sarah_threesome_request_action():
        Sarah_threesome_request_action = Action("Sarah Threesome Request",Sarah_threesome_request_requirement,"Sarah_threesome_request_label")
        mc.business.add_mandatory_crisis(Sarah_threesome_request_action)

    def add_sarah_arrange_threesome_action(person):
        Sarah_arrange_threesome_action = Action("Sarah_threesome_arrange",Sarah_arrange_threesome_requirement,"Sarah_arrange_threesome_label")
        person.add_unique_on_talk_event(Sarah_arrange_threesome_action)

    def add_sarah_initial_threesome_action():
        Sarah_initial_threesome_action = Action("Sarah initial threesome",Sarah_initial_threesome_requirement,"Sarah_initial_threesome_label")
        mc.business.add_mandatory_crisis(Sarah_initial_threesome_action)

    def add_sarah_ask_for_baby_action():
        Sarah_ask_for_baby = Action("Sarah asks for a baby", Sarah_ask_for_baby_requirement, "Sarah_ask_for_baby_label")
        mc.business.add_mandatory_crisis(Sarah_ask_for_baby)

    def add_sarah_fertile_period_start_action():
        Sarah_fertile_period_start = Action("Sarah starts a fertile period", Sarah_fertile_period_start_requirement, "Sarah_fertile_period_start_label")
        mc.business.add_mandatory_crisis(Sarah_fertile_period_start)

    def add_sarah_fertile_period_end_action():
        Sarah_fertile_period_end = Action("Sarah ends a fertile period", Sarah_fertile_period_end_requirement, "Sarah_fertile_period_end_label")
        mc.business.add_mandatory_crisis(Sarah_fertile_period_end)

    def add_hr_director_initial_hire_action(person):
        HR_director_initial_hire_action = Action("Hire HR Director",HR_director_initial_hire_requirement,"HR_director_initial_hire_label", args = person, requirement_args = day)
        mc.business.add_mandatory_crisis(HR_director_initial_hire_action)

    def add_naomi_reconciliation_action():
        naomi_reconciliation_action = Action("Naomi reconciliation", naomi_reconciliation_requirement, "Sarah_naomi_reconciliation_label")
        naomi.add_unique_on_room_enter_event(naomi_reconciliation_action)

    def add_talk_to_sarah_about_naomi_action():
        talk_to_sarah_about_naomi_action = Action("Sarah talk about Naomi", talk_to_sarah_about_naomi_requirement, "Sarah_talk_about_naomi_label")
        sarah.add_unique_on_talk_event(talk_to_sarah_about_naomi_action)

    def add_naomi_visits_to_apologize_action():
        naomi_visits_to_apologize_action = Action("Naomi visits to apologize", naomi_visits_to_apologize_requirement, "Sarah_naomi_visits_to_apologize_label", requirement_args = day)
        mc.business.add_mandatory_crisis(naomi_visits_to_apologize_action)

    def get_sarah_date_outfit_one():
        outfit = Outfit("Sarah Date Outfit One")
        outfit.add_upper(summer_dress.get_copy(), [.95, .7, .87, .95])
        outfit.add_lower(tiny_lace_panties.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(heels.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(thigh_highs.get_copy(), [.95, .7, .87, .95])
        outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        return outfit

    def get_sarah_date_outfit_two():
        outfit = Outfit("Sarah Date Outfit Two")
        outfit.add_upper(two_part_dress.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(fishnets.get_copy(), [.95, .7, .87, .95])
        outfit.add_feet(pumps.get_copy(), [.95, .7, .87, .95])
        outfit.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        outfit.add_accessory(lipstick.get_copy(), [.745, .117, .235, .8])
        return outfit

    def get_sarah_workout_event_outfit():
        outfit = Outfit("Sarah Workout Outfit")
        outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, 1.0])
        outfit.add_lower(booty_shorts.get_copy(), [.15, .15, .15, .95])
        outfit.add_feet(short_socks.get_copy(), [1.0, 1.0, 1.0, 1.0])
        outfit.add_feet(sneakers.get_copy(), [.71, .4, .85, 1.0], "Pattern_1", [1.0, 1.0, 1.0, 1.0])
        return outfit


label Sarah_intro_label():
    $ the_person = sarah
    "*DING DONG*"
    "You hear the doorbell ring. You look at the clock. It's early."
    "It rings again... isn't anyone going to get that?"
    "You get up and stumble out of your room. Your sister and mom are nowhere to be scene."
    "You make your way to your front door and open it."
    $ renpy.show("Apartment Entrance", what = her_hallway_background, layer = "master")
    $ the_person.draw_person()
    "Standing at your door is a cute brunette, fairly short, and strikingly familiar..."
    "She appears to be holding some kind of clipboard. A door to door saleswoman? Do those still exist?"
    the_person "Hello sir, I am [the_person.title], with Metropolis Power and Light, I was just wondering if you had ever thought about installing solar panels..."
    "She begins talking about the benefits and tax credits associated with solar panels, but you have a hard time listening."
    "This girl... she look so familiar! Where do you know her from!?!"
    the_person "... with even 50%% coverage of the roof you can expect a considerable reduction in your electric bill..."
    "What did she say her name was again? [the_person.title]? Suddenly you get a flash of a memory from a long time again. You quickly interrupt her."
    mc.name "I'm sorry, you said your name was [the_person.title]? Is your name [the_person.title] [the_person.last_name]?"
    "She immediately stops her sales pitch."
    the_person "That's right... do... do I know you from somewhere?"
    "Faint memories come flooding back to you. When you were growing up, your dad and his best friend got married around the same time and had kids!"
    "You used to spend a lot of time with your dad and his friend, and his friend's daughter, who was just a few years younger than you!"
    "You aren't sure what happened, but one day the other family moved away, to another city, and you never saw them again."
    mc.name "Your dad, he was friends with my dad! I remember when our dad's used to hang out, we spent a lot of time together!"
    "She looks shocked, but you can see she is also starting to remember..."
    the_person "Wait, I think I remember... Mr. [mc.last_name]? So you must be... is it really [mc.name]???"
    "You quickly nod!"
    $ the_person.draw_person(emotion = "happy")
    the_person "Oh my god! I don't believe it! You and your dad used to come over every week! And even though I was a few years younger than you, you would be so nice to me!"
    "You don't really remember going out of your way to be nice, but it was also a long time ago."
    $ the_person.draw_person(position = "kissing")
    "Without warning, [the_person.fname] throws herself at you and gives you a big hug."
    the_person "I never would have thought in a million years I would run into you again!"
    $ the_person.draw_person(position = "stand2", emotion = "happy")
    mc.name "Dad told me your family had to move away for work. What brings you back to town?"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    the_person "Ahh... well, I had just finished my degree and landed an internship at a company in town here. It was a great company, or so I thought..."
    "She clears her throat and continues."
    the_person "The director there told me if the internship went well it could become a full time position. I worked my ASS off at that place, for 6 months! And I was bartending in the evenings to make ends meet..."
    the_person "... well, when my six months was up, he said, sorry, that wasn't good enough. We are terminating you."
    $ the_person.draw_person(position = "stand2", emotion = "angry")
    the_person "I found out later, they hired some dumb bimbo for my position. I made some friends at the company, they are pretty sure the director is banging her in the office every day!"
    $ the_person.draw_person(position = "stand2", emotion = "sad")
    "[the_person.possessive_title] looks down at the ground. It looks like she is about to cry."
    mc.name "That really sucks. I'm sorry to hear that. What were you interning for, anyway?"
    $ the_person.draw_person(position = "stand3")
    "The change of topic helps her keep her composure."
    the_person "Well, I just finished up my degree in Sociology, and I was interning for a Human Resources position..."
    "Human Resources? That might actually be fairly useful."
    the_person "... I was really hoping to eventually move up to HR director there. I love working with other people, and the small business atmosphere was great!"
    "HR director? You've never heard of such a position."
    mc.name "So, what kind of work would you do as an HR director that is different from a regular HR position?"
    the_person "Well, I would be in charge of the direction of the company in general, as far as work values, help with company morale..."
    "She goes on to list multiple duties, aspects of running a small business that you had honestly never considered before."
    "When she finishes, you consider things for a moment. It would be REALLY handy to have someone around like this. She already has some work experience, and is young and ready to prove herself."
    "But, before you hire her, you would need to set up the HR director position at the company. Alternatively, you could still set up the new position, but hire someone else to fill the position."
    menu:
        "Offer to hire her":
            mc.name "So, as it turns out, I just recently started a new business making small run pharmaceuticals. You seem pretty knowledgeable, would you consider running the HR department?"
            "[the_person.title] is caught completely off guard by your offer."
            the_person "Wait, so, you run a small business? I mean, I would love to, but I can't afford to do another unpaid internship right now."
            mc.name "I didn't say it was unpaid, this would definitely be a paid position."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            $ the_person.change_stats(happiness = 5, love = 2)
            the_person "That would be... incredible! I don't know what to say! I can't wait to get started!"
            mc.name "I'll have to get your phone number. I'll need to set up the position before I can officially hire you, and that might take a few days."
            the_person "Oh! Of course, here..."
            $ mc.phone.register_number(the_person)
            "You quickly exchange phone numbers with [the_person.title]."
            mc.name "I'll be in touch with you soon I think."
            the_person "This is great, [the_person.mc_title], you won't regret this, I promise!"
            "You say goodbye to her, and she goes to keep selling solar panels until you get back to her after creating the HR director position."
            "In order to hire [the_person.title], you will need to create a new HR Director position via the policy menu."

            $ add_sarah_hire_action()

        "Don't offer to hire her":
            "You decide maybe down the line you could make a new HR director position, but you decide the [the_person.title] is probably not the best fit for it."
            mc.name "I'm sorry it didn't work out, I hope you are able to find something in your field."
            the_person "Thanks... well, it was good seeing you. I'd better keep at it."
            "You say goodbye to [the_person.title]. If you want to hire an HR director, you will need to create the position via the policy menu."
            $ sarah.event_triggers_dict["rejected"] = True
            $ sarah.set_schedule(None, the_times = [1,2,3])   # make her a free roaming character
            $ sarah.event_triggers_dict["alt_hire"] = True

    # make her a free roaming character
    $ sarah.set_override_schedule(None)
    $ sarah.set_schedule(gym, the_days = [5,6], the_times = [1])    #She tries to stay in shape
    $ sarah.event_triggers_dict["first_meeting"] = True
    $ add_sarah_watch_yoga_at_gym_action()
    $ mc.change_location(hall)
    return

label Sarah_hire_label():
    $ the_person = sarah
    "After creating the new HR Director position, you call up [the_person.title]. She answers and says hello."
    mc.name "Hey, I just wanted to let you know, I have the details finalized for an HR Director position."
    the_person "That sounds great! When can I get started?"
    $ day_name = "Tomorrow"
    if day%7 == 4 or day%7 == 5: # it's friday or saturday so next workday is monday
        $ day_name = "Monday"

    mc.name "[day_name] morning. I'll text the address after this call. We will go over your role and responsibilities when you get there."
    if day%7 == 4 or day%7 == 5:
        the_person "Yes! I'm so glad to finally be done selling solar panels. I'll see you on [day_name]!"
    else:
        the_person "Yes! I'm so glad to finally be done selling solar panels. I'll see you in the morning!"
    "You hang up the phone. You quickly text [the_person.title] the address of your business."

    $ add_hr_director_initial_hire_action(the_person)
    return

label Sarah_alternative_hire_label(the_person):
    $ the_person.draw_person()
    mc.name "Hey, are you still selling those solar panels?"
    the_person "Yeah, still haven't found a better job."
    mc.name "Interested in becoming my new HR Director?"
    $ the_person.draw_person(position = "stand3", emotion = "happy")
    $ the_person.change_stats(happiness = 5, love = 2)
    the_person "That would be... incredible! I don't know what to say! I can't wait to get started!"
    $ day_name = "tomorrow"
    if day%7 == 4 or day%7 == 5: # it's friday or saturday so next workday is monday
        $ day_name = "Monday"
    mc.name "Great, here is my card with the address, drop by [day_name] morning so we can go over the details."
    the_person "Great, thank you again, I will."
    $ add_hr_director_initial_hire_action(the_person)
    $ sarah.event_triggers_dict["alt_hire"] = False
    return

label Sarah_third_wheel_label():
    $ the_person = sarah
    $ the_person.apply_outfit(get_sarah_date_outfit_one())

    "By yourself on the weekend at work, you get up for a minute and decide to stretch your legs and walk the hallways for a bit."
    $ mc.change_location(office)
    "As you pass by the HR offices, you notice the HR Director's office door is open and the light is on. You decide to investigate."
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You see [the_person.possessive_title] sitting at her desk, rummaging through her drawers looking for something."
    "She notices you step in her door and looks surprised."
    the_person "Oh! Hey [the_person.mc_title]. I was just looking for something I left in my desk. What are you doing here? Isn't this place closed down for the weekend?"
    mc.name "Yeah, well, I had a few things I wanted to get done over the weekend. Is it something I can help you find?"
    the_person "I actually just found it! One second..."
    "You see her pull a small, silver package out of her desk and shove it in her bag quickly... was that a condom?"
    $ mc.change_locked_clarity(5)
    the_person "... sorry I just... you know, like to be prepared. You never know!"
    mc.name "You look nice, you have a date tonight?"
    "[the_person.title] blushes and looks down at her desk."
    the_person "Errrmm... not really. I'm meeting a friend at the bar for a few drinks. I thought it was just going to be me and her, but she just texted me she is bringing her boyfriend."
    mc.name "Ah... your friend... is she like, your wing-woman or something? Helping you pick up guys at the bar?"
    the_person "Well, not exactly. I don't really want to talk about it right now."
    "She glances up and looks at you for a moment. Suddenly you realize she is checking you out."
    the_person "Say, what are you up to tonight, [the_person.mc_title]?"
    mc.name "Well, I was gonna get a few more things done around here. But to be honest, I wouldn't be against grabbing a few drinks with an old friend, if that were to be suggested."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    the_person "Aww, you wouldn't mind coming along? I hate being the third wheel. If you get bored you can leave at any time, I promise!"
    mc.name "Nonsense, let me just wrap up what I was doing, lockup and we'll go."
    "You head downtown with [the_person.char]. You decide to walk since it isn't very far, and enjoy talking with her as you go."

    $ mc.change_location(downtown)

    $ scene_manager.update_actor(the_person, position = "stand2")
    "Getting curious, you decide to ask her why she needed the condom at the office."
    mc.name "So... when I first stepped into your office you were looking for something in your desk... was that a condom?"
    "[the_person.title] doesn't stop walking, but you can see her get a little tense."
    the_person "Yeah, it was."
    mc.name "So, why did you need to come back and grab that?"
    the_person "Well my friend has been dating this guy for a while and keeps complaining, he wants them to open up their relationship some, maybe bring a lucky guy or girl back to their place sometime..."
    the_person "I've been out with them a couple of times now, hoping maybe they would show interest in me, but so far nothing."
    $ mc.change_locked_clarity(10)
    if sarah_epic_tits_progress() < 2:
        the_person "Her boyfriend... it's like he just looks right through me. I've seen them leave the bar with a girl before, and it's always some dumb looking, busty girl."
        mc.name "Don't be silly, you are so sexy. There is more to look for in a woman than chest size."
        "She laughs at you sarcastically."
        the_person "Ha! Very funny. No, I'm afraid the guys I meet tend to friend zone me pretty quick. The flat chested third wheel! I suspect that is how things will go tonight."
    else:
        the_person "I thought that, you know, after taking those serums that her boyfriend might actually notice me now."
        the_person "Really though, I'm about ready to move on. They still think of me as that flat chested third wheel I used to be!"
    "[the_person.title] considers things for a bit."
    the_person "However tonight goes... it's pretty amazing you are willing to come out here with me like this."
    $ mc.change_locked_clarity(10)
    mc.name "Of course, I can't remember the last time I said no to drinks with a single lady as beautiful as you."
    the_person "There you go again! You know, it was a long time ago that we grew up together. But I still have so many fond memories of you. You always used to be so nice to me."
    the_person "I remember one time, we were playing in the living room at my house, and suddenly a bug landed on my head. I started screaming! I was so scared."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    "She stops walking for a moment and turns to you, a serious, but happy look on her face."
    the_person "Suddenly, you grabbed me. HOLD STILL! you yelled, and you knocked the bug off me and on the floor and stomped on it."
    the_person "When my family moved away and the memories got old... I kept telling myself, we were just kids. He was sweet because we were just kids."
    the_person "But meeting you again, now that we are adults... and getting to know you all over again. You are still that sweet boy."
    the_person "You didn't even think twice about it tonight, when I asked you to go. That means a lot to me, you know?"
    $ scene_manager.update_actor(the_person, position = "stand2")
    "[the_person.possessive_title] turns and continues walking. You walk beside her the rest of the way to the bar in silence."

    $ mc.change_location(downtown_bar)
    $ naomi.change_location(downtown_bar)

    "When you get to the bar, [the_person.title] quickly spots her friend and leads you over to the table."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(naomi, position = "sitting", display_transform = character_left_flipped)
    the_person "Hey [naomi.title]! Good to see you."
    naomi "Hey girl! Is he with you?"
    "She nods towards you."
    the_person "Yup! This is my bo... I mean, an old friend of mine. [mc.name] this is [naomi.title]!"
    "You make acquaintance and sit down. [naomi.title] also introduces you to her boyfriend."
    "You chat for a bit, but notice that [naomi.title] keeps checking you out. Normally you would be testing the waters with her, but with [the_person.title] here, you are a little leery."
    mc.name "Hey, how about I get us a couple drinks, [the_person.title]?"
    the_person "Oh! That sounds great! Can you get me an appletini?"
    "As you start to get up, [naomi.title]'s boyfriend also excuses himself to the restroom, leaving the girls alone."
    "It takes a few minutes to get the attention of the bartender. You order the drink for [the_person.title] and get yourself a nice bourbon, straight."
    $ mc.business.change_funds(-20)
    $ scene_manager.update_actor(the_person, position = "sitting", emotion = "sad")
    "When you come back to the table, you notice that [the_person.possessive_title] is looking down at the table and looks upset about something."
    mc.name "Hey! Here's your drink... are you okay?"
    the_person "Yeah... yeah I'm fine I just umm, I need to go use the lady's room."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She gets up in a hurry and walks quickly away. You look at [naomi.title]."
    $ scene_manager.hide_actor(the_person)
    mc.name "Umm... any idea what that is about?"
    naomi "No idea... we were just talking about, well you actually."
    "Something about the way she says it makes you uncomfortable."
    naomi "[the_person.fname] says you are a great guy, a good friend of hers."
    mc.name "Yeah, something like that I guess..."
    naomi "What do you say we get out of here? Like back to my place?"
    mc.name "That sounds pretty good actually. [the_person.fname] will be excited to hear that I think."
    naomi "Ha! No no, I mean, just you. [the_person.fname] is a good friend but..."
    mc.name "But?"
    if sarah_epic_tits_progress() < 2:
        naomi "My boyfriend... he just isn't attracted to her. I mean, have you seen her chest? Like, neither have we!"
    elif sarah_epic_tits_progress() == 2:
        naomi "My boyfriend can't stop staring at her tits. It's pissing me off! I can't believe she got implants, she is such a whore."
    else:
        naomi "Like, one day she's got nothing, next thing I know, her tits are fucking huge!?! She's such a bimbo."
    "You feel yourself getting angry at her crude remarks."
    "You are able to restrain yourself, but only just barely."
    mc.name "[the_person.fname] has an amazing body, and a great personality to go with it. If you and your boyfriend don't see that, I don't think anything with me can work out."
    naomi "Pfft, whatever. There's a dozen other dicks at the bar. Why don't you go find your date, she's probably sulking in the bathroom again!"
    "You decide not to stoop to her level and to end your conversation there. You grab your and [the_person.title]'s drinks and get up, not bothering to say goodbye."
    $ scene_manager.remove_actor(naomi)
    "You walk over to where the restrooms are and wait for [the_person.title]. You stand there for several minutes but start to get worried about her."
    "You don't see anyone come in or out of the women's restroom so you decide to risk it. You walk to the door and slowly open it."
    $ scene_manager.show_actor(the_person, position = "stand2", emotion = "sad")
    "Inside you see [the_person.title] looking at herself in the mirror. She is forlorn and from the look of her makeup has obviously been crying."
    mc.name "Hey, are you okay? I don't mean to invade your privacy, but I was starting to get worried about you."
    "She quickly looks up and is surprised to see you. She briefly pulls herself together."
    the_person "Is that you, [the_person.mc_title]? You're still here? I thought you would be gone by now..."
    mc.name "What are you talking about?"
    the_person "Well, [naomi.title] said... she was asking me about you, asked if we were involved, and when I said no said she was going to make a pass at you tonight..."
    the_person "I just assumed, when I left the table that, I mean, why didn't you go with her?"
    "She assumed when her friend made a pass at you that you would bail on her! You quickly reassure her."
    mc.name "[the_person.title], I came here to support you, and to spend time with my long-lost friend having some fun and a few drinks."
    mc.name "If you think I'm going to miss out on that for a silly one night stand, you are mistaken."
    $ scene_manager.update_actor(the_person, position = "stand2", emotion = "happy")
    the_person "I'm sorry! I didn't mean that I think you're shallow or anything I just... Look, give me one more minute and I'll be right out, okay?"
    mc.name "Sounds good!"
    "You step out of the lady's room and shortly after [the_person.title] steps out and joins you. You hand her the appletini."
    the_person "Thanks for waiting! I'm so sorry, I honestly thought you were going to go with them."
    the_person "Thank you for... I mean, everything you've done for me. You gave me a job, you let me drag you out to a bar with strangers, and then stuck with me even when you probably shouldn't have..."
    mc.name "You're crazy, it's not everyday a long-lost childhood friend literally knocks on your front door."
    the_person "You've always been amazing to me. I should have known better."
    $ the_person.change_stats(happiness = 10, obedience = 5, love = 5)
    "She takes a long sip of her drink. You begin to chat and catch up a bit."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ mc.business.change_funds(-100)
    "You spend several hours with [the_person.title] sitting in a secluded booth catching up. After multiple appletinis and whiskeys, you are both feeling pretty good."
    the_person "Well, I suppose it is getting pretty late. You have no idea how great this was. I don't want to say goodbye yet..."
    "[the_person.title] thinks for a moment."
    the_person "Hey... do you want to walk me home?"
    $ mc.change_locked_clarity(10)
    mc.name "That sounds like a perfect way to end the evening. Let's go."

    $ mc.change_location(downtown)

    $ scene_manager.update_actor(the_person, position = "stand3")
    "You walk together with [the_person.title] through the streets as she slowly leads the way. You converse a bit, but things are mostly quiet as you walk."
    "Soon you are standing in front of the door to her apartment building."
    # you now know were Sarah lives
    $ the_person.learn_home()
    the_person "Thanks for today! It really means a lot to me that you spent the whole evening with me."
    mc.name "Consider it making up for lost time."
    "[the_person.possessive_title] blushes and looks down."
    mc.name "Goodnight."
    "You step close and put your arms around her."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "She quickly wraps her arms around you and embraces you. You move your head to kiss her on the cheek, but at the last second she moves her head and you find your lips pressing into hers."
    $ the_person.break_taboo("kissing") # break her kissing taboo
    the_person "Ohhh! Mmmmm..."
    "At first she opens her eyes in surprise, but quickly closes them and begins to kiss you back."
    "Her lips part and your tongue quickly takes advantage and begins to explore her soft lips. They taste sweet, with just a hint of appletini."
    $ mc.change_locked_clarity(15)
    "You stand there in front of [the_person.title]'s building, holding each other and making out for several minutes until the kiss stops and you step back. Her eyes are still closed."
    mc.name "I'll see you on Monday?"
    $ scene_manager.update_actor(the_person, position = "stand4")
    "She suddenly snaps back to reality. Her cheeks are flushed."
    the_person "Right! Yes of course. Goodnight!"
    $ time_of_day = 3
    "She turns and heads into her building. You check your watch and realize how late it is."
    $ scene_manager.remove_actor(the_person, reset_actor = False)
    $ add_sarah_get_drinks_action()
    $ sarah.event_triggers_dict["drinks_out_progress"] = 1
    return

label Sarah_watch_yoga_at_gym_label(the_person):    #20 sluttiness event
    "You decide to hit up the gym. You go to the locker room and change into workout clothes."
    "When you step out, you look at the different workout equipment. Since it's the weekend, maybe you should focus on some cardio?"
    "You notice to the side of the gym are some bike machines that happen to be facing a glass wall, peeking into a yoga class."
    "You sit down on the bike and look inside at the women doing their exercises. You realize you recognize someone!"
    $ the_person.draw_person(position = "stand3")
    "Inside the room is [the_person.possessive_title]. She is doing the stretches and moves with the other women."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(10)
    "You watch, enjoying the chance to see her bending over and stretching her fit young body..."
    $ the_person.draw_person(position = "blowjob")
    "On her knees, just before leaning forward into a stretch, she looks out the window and sees you, recognizing you instantly."
    "You make eye contact. She immediately realizes you are watching her do her yoga."
    $ the_person.draw_person(position = "blowjob", emotion = "happy")
    "She smiles at you, her eyes drifting down your body as well as you workout on the bike machine."
    $ the_person.draw_person(position = "back_peek")
    "As she continues following instructions, she watches you carefully. She seems to like that you are watching her!"
    $ the_person.draw_person(position = "doggy")
    "At one point, in between leg stretches while she is on her hands and knees, you swear you can see her wiggle her ass at you..."
    $ mc.change_locked_clarity(15)
    "It looks nice and tight... she must make an effort to stay in shape. When she shows it off you can't help but let your mind wander a bit..."
    "You watch for a little longer, but unfortunately the class is almost over."
    $ clear_scene()
    "Soon the girls leave the room. You are a little disappointed, but it is probably better for you to finish your workout without anymore distractions."
    "It would be awkward to stand up from the equipment with a boner..."
    the_person "Hey [the_person.mc_title]."
    $ the_person.draw_person()
    "Aaaand of course, she comes to say hello."
    mc.name "Hey."
    the_person "Getting a good workout I see?"
    mc.name "I sure am. You?"
    the_person "Yes, I'd say you saw me get a good workout in also."
    "She gives you a quick wink, clearly flirting with you."
    $ the_person.change_slut(2)
    mc.name "What can I say, it makes it easier to push the limits of my endurance when I get my testosterone flowing."
    if the_person.love < 40:
        the_person "Ahh, is that the secret? Perhaps I should hit up the elliptical facing the pool the next time they are doing the morning men's swimming..."
    else:
        the_person "Ahh, I must say, being watched helped motivate me to work hard and have good form as well."
    the_person "Well, I have other commitments for today, have a good workout!"
    mc.name "Take care."
    $ clear_scene()
    $ sarah.event_triggers_dict["yoga_voyeur"] = True
    return

label Sarah_get_drinks_label():
    $ scene_manager = Scene() # make sure we have a clean scene manager
    $ the_person = sarah
    $ the_person.planned_outfit = get_sarah_date_outfit_one()
    $ the_person.apply_outfit(the_person.planned_outfit)

    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person "[the_person.mc_title]! I figured I'd find you around here on a Saturday again!"
    "You look up to see the now familiar face of [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "It's crazy to think that just a short time ago, she was out of your life completely, but after your chance encounter, you feel like you've been friends forever."
    mc.name "Hey [the_person.title]. You look great! Are you going out tonight?"
    the_person "Actually, I'm not sure yet. I hope so! But I'm not sure if the guy I want to go out with is going to be able to go yet or not..."
    mc.name "Is that so? I hope he can make it and that he treats you well!"
    the_person "Hahaha, yeah me too. And don't worry, he's always treated me right."
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] looks down at the floor for a minute and mumbles something. It's obvious she is trying to work up the courage to ask you out, but it is cute watching her fumble a bit."
    the_person "So... you uhh, have any big plans for the evening, [the_person.mc_title]?"
    mc.name "Oh, well, certainly nothing as big as what you have planned! I'm just trying to get a little ahead of work for next week."
    the_person "Ah! That's good. It is pretty amazing how much work you put into this place. It's something I admire a lot..."
    the_person "Anyway, I've seen how hard you work and I was thinking that, maybe we could go out and get a few drinks?"
    "You decide to tease her a bit."
    mc.name "Ahh, I see. You meeting another friend tonight? I'm not sure I want..."
    "She quickly interrupts you."
    the_person "No! God no, that was awful. I thought we could just go out, you know? Me and you?"
    mc.name "You mean like a date?"
    "She stutters a moment before she replies."
    the_person "Well, ermm, I mean, uhh..."
    the_person "Yeah. Pretty much that is exactly what I'm trying to ask..."
    $ mc.change_locked_clarity(10)
    "You admire her courage. She must be really interested in you to have the guts to ask you out like this! If you accept, she might assume you are interested in a relationship..."
    menu:
        "Sounds great!": #Begin the dating path with Sarah
            mc.name "A date sounds great! I'd love to spend some more time with you, catching up and learning about what you've been up to."
            "Her face shows visible signs of relief."
            the_person "Okay! This will be fun! Do you want to get out of here now, or do you need some time to finish up?"
            $ sarah.event_triggers_dict["dating_path"] = True
            $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness since she really likes you.

            $ the_person.change_stats(happiness = 10, love = 5)
        "Just as friends":
            mc.name "I wouldn't mind going out for a few drinks, with a friend of course."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            "Her face shows visible signs of disappointment."
            the_person "Oh, right. Friends! That's us! I don't want to interrupt you, there, buddy. Need a few minutes to finish up?"
            $ the_person.change_stats(happiness = -10, love = -5, obedience = 5)
            $ sarah.event_triggers_dict["dating_path"] = False
            $ the_person.add_situational_slut("Date", 10, "There's no reason to hold back, he's here to fuck me!") # Bonus to sluttiness not so high since we go as friends.

    mc.name "I'm actually at a great stopping point now. Let's go!"
    the_person "Great! Do you want to walk again tonight? It was kind of nice when we walked together last time."
    mc.name "Sounds good to me, it's good to get out and stretch the legs once in a while."
    "You lock up on your way out and head toward downtown."

    $ mc.change_location(downtown)


    "You enjoy pleasant conversation with [the_person.possessive_title] as you walk downtown."
    if the_person.event_triggers_dict.get("dating_path", False):
        "As you walk along, you feel her hand slip into yours. You twiddle your thumb with hers as you walk downtown."
        $ mc.change_locked_clarity(10)
    #TODO the convo




    $ mc.change_location(downtown_bar)

    "You walk into the bar. [the_person.title] spots an empty booth."
    the_person "Hey, there's an empty table over there!"
    mc.name "Go grab it. Appletini?"
    the_person "Sounds great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She walks off to the booth while you head up to the bar."
    "You order your drinks with the bartender. If you wanted to, now would be a good time to slip a serum into her drink..."
    $ mc.business.change_funds(-20)
    menu:
        "Slip in a serum":
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_001
        "Leave alone":
            "You decide to leave her drink alone."
    "You grab your drinks and then head to the table. You sit down across from [the_person.title]."
    $ scene_manager.update_actor(the_person, position = "sitting")
    the_person "Thanks! I love these things..."
    "She takes a long sip from her glass. You take a sip of yours. [the_person.possessive_title] sets down her glass and looks at you."
    the_person "I have to say, I feel like I'm settling in pretty well. The girls at the office have been really nice to me so far."
    mc.name "That's good to hear. I'm very selective about who I hire."
    the_person "Yeah. You choice is very, shall we say, interesting? Hiring only women to work for you. Not that I'm complaining or anything!"
    mc.name "I know it may seem a bit odd, but so far it has been advantageous to keep the staff all female. Perhaps in the future that could change, but for now it is working."
    the_person "It's quite alright with me. To be honest, I umm, enjoy the surroundings..."
    "She takes a long sip of her drink."
    mc.name "Sorry, I feel like you've hinted at this a few times before but, I just want to clarify. Are you a lesbian? I'm totally fine with that, I'm just curious."
    "[the_person.title] laughs and puts her hand on yours."
    the_person "Oh, I'm not dedicated to it or anything, but I've always been curious about what it would be like to be with another woman."
    "She sighs."
    the_person "Don't get me wrong, I don't think I could ever date another woman, I prefer men, but I've always wanted to try a Ménage à trois..."
    $ the_person.increase_opinion_score("other girls")
    $ the_person.increase_opinion_score("threesomes")
    "You have discovered that [the_person.title] is bi-curious and into threesomes!"
    $ mc.change_locked_clarity(20)
    mc.name "That's very open minded of you. I can certainly respect that!"
    "[the_person.title] tips her glass back and finishes her first drink. You make it a point to do the same."
    mc.name "Let me grab the next round."
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "That sounds great. Say, want to play some darts? I'll grab us a board while you grab the drinks!"
        mc.name "That sounds great, I'll meet you over there."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and walks over to the dart boards while you grab a couple more drinks."
        $ mc.business.change_funds(-20)
        "You feel like, so far at least, this date is going pretty well!"
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You walk over to [the_person.title], drinks in hand. You hand her a drink."
        mc.name "How about a toast? To tonight! May we love as long as we live, and live as long as we love."
        $ the_person.change_stats(happiness = 5, love = 2)
        "You surprise yourself with your sappy toast. It seems to have the desired effect though, as she smiles wide with your toast."
    else:
        the_person "Hey, let me grab the next round. I want to play a game though! Can you go get us a dart game set up?"
        mc.name "Yeah, that actually sounds pretty fun. I'll do that."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.possessive_title] gets up and walks over to the bar while you head over to reserve a dart board."
        "You are having a lot of fun hanging out with [the_person.title]. Even though you rejected her earlier, you are wondering how she might feel about a friends with benefits setup..."
        $ scene_manager.update_actor(the_person, position = "stand4")
        "[the_person.title] joins you and hands you another whiskey."
        the_person "How about a toast? To he who has seen me at my best and has seen me at my worst and can't tell the difference!"
        "You grin at her cheesy toast, she smiles wide at you."
    "You clink your glasses together and take a deep sip."
    the_person "Alright! I'm going first."
    $ scene_manager.hide_actor(the_person)
    call play_darts_301(the_person, focus_mod = 2) from play_darts_301_call_1
    if _return:
        $ scene_manager.show_actor(the_person, emotion = "sad")
        "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
    else:
        $ scene_manager.show_actor(the_person, emotion = "happy")
        "[the_person.title] gives you a huge smile after winning your game of darts!"
    "You notice the drinks are empty."
    mc.name "That was a good game. Want another round and another game?"
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person "Oh! That sounds great! I'll get it set up!"
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20)
    the_person "Thanksh! I love these things..."
    "You notice her speech is starting to get a little slurred... You bet as you feed her drinks, she may have trouble focusing on the game."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] starts to line herself up on the line to throw. You decide to see if you can distract her a little further."
    "You walk up behind her and put your hand on her back."
    mc.name "Hang on, I just noticed something about the way you are throwing the darts."
    "You get in close behind her until you are right behind her, your body up against hers."
    $ mc.change_locked_clarity(20)
    the_person "Oh? I thought I did okay, but if you have some... tips... for me that would be nice!"
    "The feminine smell of her perfume enters your nostrils and you take a deep breath, enjoying your proximity with [the_person.title]."
    "You run your fingertips along her arm, until you are holding her hand as she holds her dart."
    mc.name "That's right, there was something about your posture that caught my eye."
    "You are now pushing yourself lightly up against [the_person.title]. She catches her breath when she feels your erection beginning to grow against her backside."
    $ the_person.change_slut(2, 60)
    the_person "Ah, something caught your eye then?"
    "You quickly release her and then walk back to the table."
    mc.name "Yeah, something like that. I'm not sure what it was, but I'll let you know if I can put my finger on it..."
    # "[the_person.title] is trying to focus on the dart board, but she keeps stealing glances back at you. Your flirting is having the desired effect on her!"
    # "She readies herself for the next round of darts."
    # $ scene_manager.hide_actor(the_person)
    # call play_darts_301(the_person, focus_mod = -2) from play_darts_301_call_2
    # if _return:
    #     $ scene_manager.show_actor(the_person, emotion = "sad")
    #     "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
    # else:
    #     $ scene_manager.show_actor(the_person, emotion = "happy")
    #     "[the_person.title] gives you a huge smile after winning your game of darts!"
    "Drinks are empty again. You look at [the_person.title]. She is definitely tipsy, but you think she should be able to handle one more round."
    mc.name "How about one more game? I'll grab us another round."
    $ scene_manager.update_actor(the_person, position = "stand4", emotion = "happy")
    the_person "Another drink! I loooooveeeee going out with you, [the_person.mc_title]! You know how to keep the drinksh flowing!"
    mc.name "Haha, okay, let me go grab us another round."
    "You walk over to the bartender and order another round. You walk back to the dart board and give [the_person.possessive_title] her drink."
    $ mc.business.change_funds(-20)
    the_person "Okay, so, I've had a great warm up now, but I think for this next round, we should make it a littler more... intereshting."
    mc.name "Oh? What did you have in mind?"
    the_person "I think, whoever loses... hah, that's a funny word... anyway, whoever is the loser, should hafta walk the winner home!"
    "You raise an eyebrow involuntarily. For some reason you expected something a little... crazier than that."
    mc.name "Hah, okay, we can do that. You're up first!"
    "[the_person.possessive_title] turns and looks at the table where she set the darts earlier. She bends over and slowly starts picking them up, one by one."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She's completely bent over the table, and is obviously wiggling her hips at you. You realize when she talked earlier about the loser walking the winner home, she was probably proposing your place or hers..."
    $ mc.change_locked_clarity(25)
    "You step behind her and get close to her again. You push your hips against hers, and pretend to reach past her towards your darts that are also on the table."
    mc.name "Excuse me... just grabbing my darts here real quick..."
    "You slowly grab your darts, one by one. She pushes herself back against you."
    the_person "Of course, be careful though! The tipsh are sharp."
    mc.name "Of course, you needn't worry, I'll handle them gently..."
    $ the_person.change_slut(2, 60)
    "As you finish your sentence, you run your free hand down along her back. You slowly stand up and move away from her. You don't want to be too lewd in a public setting like this... not yet anyway..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] walks over to the line and looks at the dart board, then back at you. She is so distracted, she can barely focus on the board."
    "You should be able to win this game handily, unless you decide to throw the game on purpose!"
    $ scene_manager.hide_actor(the_person)
    $ sarah.event_triggers_dict["drinks_out_progress"] = 2
    call play_darts_301(the_person, focus_mod = -6) from play_darts_301_call_3
    if _return:
        $ scene_manager.show_actor(the_person, emotion = "happy")
        "[the_person.title] can't even pretend to be sad when you win the game."
        the_person "You won!"
    else:
        $ scene_manager.show_actor(the_person, emotion = "happy")
        "[the_person.title] gives you a huge smile after winning your game of darts!"
        the_person "You are such a gentleman. I'm pretty sure you were just letting me win! That totally doesn't count!"
    "She takes the last sip of her drink before setting it down."
    the_person "I'll walk you home! Besides, it's only fair, you walked me home last time."
    "You start to protest, but she quickly silences you."
    the_person "Don't be silly! I can see myself home whenever we get done... err... when you say goodbye I mean..."
    "Her intentions are pretty clear at this point. You take the last sip of your whiskey and set it down."
    mc.name "I can see there's no talking you out of it. And to be honest, I would appreciate the company."
    "She smiles at you. You leave the bar with her and start walking home."
    $ mc.change_location(downtown)
    #TODO set to night time
    $ time_of_day = 3 #Hopefully this works

    "You enjoy the fresh air as you begin your walk. Thinking about your time with [the_person.title] tonight, you decide now it would probably be a good idea to talk about things."
    if the_person.event_triggers_dict.get("dating_path", False):
        "You take the initiative and take [the_person.title]'s hand. You can see her smile out of the corner of your eye."
        mc.name "So, I had a lot of fun on our date tonight."
        the_person "Me too!"
        mc.name "I think it is great that you are so open in your sexuality, and wanting to try new things."
        "You can feel her grip tighten on your hand for a second."
        mc.name "I know it is kind of weird to talk about, but I want you to know that if you want to mess around with another girl... let's just say I'm not the jealous type."
        "She laughs at you before replying."
        the_person "That's good to know. Honestly, I wasn't sure how you would feel about it, but I figure most guys like the idea of being with two women..."
        mc.name "Yeah, I suppose that much is obvious. But I think I could probably help set something up..."
        "She stops and turns to you."
    else:
        mc.name "So, I had a lot of fun tonight."
        the_person "Me too!"
        mc.name "I think it is great that you are open in your sexuality, and wanting to try new things."
        "You see a brief frown on her face start to form."
        mc.name "I know it is kind of weird to talk about, but I want you to know that, even though I'm not looking for anything serious right now, I'd love to help you explore that side of things... sexually."
        "She stops and turns to you."
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person "You mean... you would be willing to try and set something up?"
    mc.name "Well... yeah! I'm pretty sure that is something I could pull off."
    "[the_person.title] looks bewildered."
    the_person "That would be something. Huh! I'll have to think about it... okay?"
    "As you are standing there looking at each other, you feel a cold breeze begin, followed quickly by rain drops beginning to fall."
    the_person "Ah! I didn't know it was going to rain!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.possessive_title] turns and starts to walk quickly. You hurry to catch up to her."
    "You are only a few blocks from your house, but by the time you get there, the rain is pouring down in sheets."
    "You quickly open the door and let [the_person.title] in."

    $ mc.change_location(hall)

    # make sure we don't alter the outfit in her wardrobe
    $ test_outfit = the_person.outfit.get_copy()
    if test_outfit.get_upper_top_layer:
        $ test_outfit.get_upper_top_layer.colour[3] *= .75 #make top transparent
    if test_outfit.get_lower_top_layer:
        $ test_outfit.get_lower_top_layer.colour[3] *= .75 #make bottom transparent

    $ the_person.apply_outfit(test_outfit)
    $ del test_outfit

    $ scene_manager.update_actor(the_person, position = "stand4")
    if (len(the_person.outfit.get_upper_ordered()) > 0 or __builtin__.len(the_person.outfit.get_lower_ordered()) > 0):
        "You look at [the_person.title]. Her clothing is soaked and you can practically see through it. She looks cold."
    else:  #She's... naked?
        "Barely clothed, [the_person.title] is shivering from the cold."
    $ mc.change_locked_clarity(30)
    mc.name "I'm sorry, I didn't realize it was going to rain like that!"
    "You made quite a bit of noise when you came in the door, and [mom.title] pokes her head out from the kitchen to see what is going on."
    $ scene_manager.add_actor(mom, position = "stand2", display_transform = character_left_flipped)
    mom "Oh! You two look absolutely soaked! Are you okay?"
    mc.name "Thanks, [mom.title]! This is [the_person.title]! We got caught out in the rain walking back. Do you think you could grab us a few towels, and maybe have some dry clothes for her to wear for a bit?"
    if sarah_epic_tits_progress() == 0: #Small tits
        mom "Yes of course! She looks about [lily.fname]'s size, I'm sure I can find something..."
    elif sarah_epic_tits_progress() == 2: #Big tits
        "[mom.title] looks her over for a moment, checking out her curves."
        mom "Yes! I'm not sure [lily.fname]'s clothes would work... I bet I have something I could give her, just give me a minute."
    elif sarah_epic_tits_progress() == 3: #Huge tits
        "[mom.possessive_title] eyes travel all over [the_person.title]'s body. Her eyes go wide when she see how big her tits are."
        mom "I'm not sure I have... actually, I think [cousin.fname] might have left something that would fit her..."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.title] leaves to go find something. [the_person.title] is shivering cold."
    $ scene_manager.hide_actor(mom)
    mc.name "I'm sorry, you look so cold. Why don't you come here for a minute..."
    "You step toward her. You put your hands around her back and draw her close to you. She wraps her arms around your neck."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "Her body feels cold, but it feels great running your hands along her body. After a minute, she stops shivering."
    $ mc.change_locked_clarity(20)
    the_person "Thank you... that feels... much better."
    "Her face is nearing yours, and you are just getting ready to kiss her."
    $ scene_manager.show_actor(mom, position = "stand2")
    mom "Here we go! I got you some... OH!"
    "ABORT! You quickly let go of [the_person.title] when your mother interrupts you."
    mom "Sorry! I didn't... here you go!"
    "She quickly hands [the_person.title] a large towel and a set of clothes."
    mom "There you are dear. I'm sorry, but [lily.fname] is in the bathroom right now, taking one of her ridiculously long showers..."
    mc.name "That's okay, she can change in my room! I can wait out here."
    the_person "Thank you! I'll be quick!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] takes the clothes and the towel. You quickly point her to your room."
    "She disappears behind your bedroom door with the clothes. You mother turns to you."
    $ scene_manager.hide_actor(the_person)
    mom "She seems nice!"
    mc.name "Yeah! Believe it or not, she is the daughter of one of dad's old friends. We used to play together as kids!"
    if mom.sluttiness < 40:
        if sarah_epic_tits_progress() == 0: #Small tits
            mom "Aww! That's cute! And she is so cute too. You be nice to her, okay?"
        elif sarah_epic_tits_progress() == 2: #Big tits
            mom "Aww! That's great! She certainly has blossomed into a beautiful young lady. You be nice to her, okay?"
        elif sarah_epic_tits_progress() == 3: #Huge tits
            mom "Wow! That's great! And she has... I mean... her figure is incredible! You be nice to her, okay?"
        mc.name "Don't worry, [mom.title]."
    elif mom.sluttiness < 70:
        if sarah_epic_tits_progress() == 0: #Small tits
            mom "That's cute... but... what about me? The woman who brought you into this world needs your attention too..."
        elif sarah_epic_tits_progress() == 2: #Big tits
            mom "That's nice dear... but don't forget about me, okay? I have needs too!"
        elif sarah_epic_tits_progress() == 3: #Huge tits
            mom "That's nice I guess..."
            mom "But... look I know she is absolutely stacked, but don't forget about me, okay? I have needs too!"
        $ mc.change_locked_clarity(20)
        mc.name "Don't worry, [mom.title]. No one could ever replace you."
    else:
        mom "Wow! She is so pretty."
        mom "So... when do I get a chance to get my hands on her?"
        $ mc.change_locked_clarity(30)
        mc.name "Don't worry, it'll be soon [mom.title]."
    mom "Okay! I'll umm, just be in my room for the night..."
    $ scene_manager.remove_actor(mom, reset_actor = False)
    "[mom.possessive_title] quickly steps into her room and closes the door. You look at the door to your own bedroom, imagining the woman inside it slowly peeling off her soaking wet garments..."
    "As you look at your door, you realize that it isn't closed all the way. [the_person.title] left it open a crack!"
    "You creep slowly up to your door and listen. You don't hear much coming from within, so you slowly inch the door open and then peek inside."

    $ mc.change_location(bedroom)

    $ scene_manager.show_actor(the_person, position = "walking_away")
    "You see that [the_person.title] is just starting to peel off her clothes."
    $ scene_manager.strip_full_outfit(person = the_person)
    $ mc.change_locked_clarity(50)
    "She stands there, looking at herself in the mirror for a moment, when she spots you looking at her from the door. Busted!"
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "Hey! You gonna come in and close the door or just stand there?"
    "Nice! She must have left the door cracked on purpose, hoping you would peek."
    "You quickly step into your room, close your door and lock it behind you. [the_person.title] giggles."
    "You walk over to her and embrace her again."
    $ scene_manager.update_actor(the_person, position = "kissing")
    the_person "I was hoping you would come..."
    "Her mouth opens, her eyes close, and your faces move together as you begin to kiss. Her mouth immediately opens and you begin to twirl your tongues around each other."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(10)
    the_person "That feels good... but I'm freezing!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You quickly pick her up. You carry her over to your bed and then throw her down on it."
    mc.name "Don't worry, I'll get you warmed up in a hurry!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You start to climb on top of [the_person.possessive_title]. She opens her legs and the wraps them around you."
    "You are still wearing your wet clothes, but you don't care. You slowly start to grind your hardness into her groin through your pants."
    $ the_person.change_arousal(10)
    the_person "Mmmm, that feels good, but you're cold too! Let's get these off..."
    "[the_person.title] is pulling at your shirt. You quickly help her take it off, then reach down, unbutton your pants, and take them and your underwear off in one smooth motion."
    "Your cock springs free. [the_person.title] gasps as she takes it in her hand."
    the_person "Ohhhh. It's so warm! This is exactly what I need to warm me up!"
    "You look down at [the_person.title]. She is stroking your cock now, and you can feel her legs start to wrap around your back again, urging you to push yourself into her."
    "For a moment you consider grabbing a condom, but that thought evaporates when she runs the nails of her free hand roughly down your back."
    "You let go of yourself, and move your hips into position just above hers. Her hand stops stroking you and guides your cock to her pussy as it gets close."
    "You can feel the moist heat coming from between [the_person.title]'s legs as you get close. You feel the head begin to poke against her slit."
    "Her legs wrap tighter behind you, begging you to push into her. You happily give in, parting her labia and sinking slowly into her cunt."
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "OH god... that's so good!"
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_description_sarah_grabbing_drinks_1
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "Oh my god... ever since you came back into my life, I'd been hoping... maybe this was all happening for a reason."
        $ scene_manager.draw_scene()
        "You lay down on your side next to her. She scoots next to you and lays her head on your arm."
        the_person "Can we... can I just be close to you for a while? I'm not ready for this day to end!"
        $ the_person.change_stats(happiness = 5, love = 2)
        mc.name "Of course! Your skin feels so good."
        "You cuddle up with [the_person.possessive_title] for a while, just enjoying the afterglow of your lovemaking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    else:
        the_person "Mmm, that was nice. It's been a while since I was able to do that."
        $ scene_manager.draw_scene()
        "She rolls on her side and looks at you."
        the_person "So... friends with benefits then? I think that is an arrangement that I could live with."
        mc.name "Great! Yeah if you get the urge, I'm up for a hookup now and then."
        the_person "Okay. You'd better satisfy me though!"
        "You give her a wink and a nod."
        $ the_person.change_stats(happiness = 5, slut = 1, max_slut = 60)
        the_person "Alright... I'm just gonna lay here for a moment. It's been a long day, I need to take a few minutes before I get up."
        "She rolls over, facing away from you and relaxes for a bit, enjoying coming down from the high of fucking."
        "She is starting to doze off, when suddenly she wakes up and gets up."
    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Sorry... I just realized how late it is getting. I'd better get home!"
    $ the_person.apply_outfit(get_sarah_date_outfit_one())
    $ scene_manager.draw_scene()
    "You watch her intently from your bed. Her body looks amazing, as she begins to hide it behind her clothes that have dried up by now."
    $ mc.change_locked_clarity(10)
    the_person "Don't worry, I can see myself out. I had a great time tonight! I'll see you on Monday, okay?"
    mc.name "Goodbye!"
    $ scene_manager.remove_actor(the_person)
    $ the_person.clear_situational_slut("Date")

    "[the_person.possessive_title] lets herself out of your room and leaves. Wow, what an evening!"

    $ add_sarah_stripclub_story_action()
    $ scene_manager.clear_scene()
    return

label Sarah_catch_stealing_label():
    $ the_person = sarah
    $ sarah.event_triggers_dict["epic_tits_progress"] = 1
    "As you walk the halls of your company, getting ready to pack things up for the weekend, you notice [the_person.title] sneaking out of the research division."
    $ mc.change_location(rd_division)
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]... what brings you to research on a late Friday evening?"
    "She looks down at the ground and mutters for a second, trying to think of something. It is clear she is hiding something."
    the_person "Hey [the_person.mc_title]! I was just, well, [mc.business.head_researcher.name] had something for me that umm, I asked her for help with and so I was just grabbing it before I left for the weekend!"
    "With one hand behind her back, it doesn't appear she wants you to know what it is that she has."
    mc.name "Is that so? That's awfully nice of her. What is she helping with? Can I see it?"
    if the_person.obedience > 120:
        "Realizing that you need to know what she was doing in there, she lowers her head and brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person "I'm sorry... I know I shouldn't... distract the research staff but, when you told me on Monday that we had come up with a breast enhancement serum, I immediately knew I had to get some I just..."
    else:
        the_person "Oh, don't worry about it, it is just between me and her!"
        "You furrow your brow. Hopefully you can convince her to come clean with whatever it is that she is doing."
        mc.name "I'm sure it is fine, but you ARE coming out of Research on a Friday, after everyone has left for the weekend. Let me see what you have."
        "Realizing that you aren't going to back down, she slowly brings her hand forward. In it are several glass vials with some prototype serum labeled 'T+'"
        the_person "Don't be mad! When you told me on Monday that we had come up with a breast enhancement serum, I knew I had to get my hands on one of the prototypes..."
    mc.name "It's okay. I didn't realize that was something you would be interested in. If you had asked me, I would have seen it arranged without you having to sneak around!"
    $ the_person.change_stats(happiness = 5, love = 2)
    $ the_person.draw_person(emotion = "happy")
    $ mc.change_locked_clarity(10)
    "She is very relieved to hear that."
    the_person "Oh! Thank you [the_person.mc_title]! I'm sorry, I won't be sneaky like that again. I just... you know I've always had such a small chest and been really self-conscious about it."
    the_person "I've thought about getting implants before but... surgery seems so extreme for a cosmetic issue."
    mc.name "So, how many are you planning to take?"
    the_person "Oh, well, research says we don't know for sure how effective they are... I figure I'll just take one each day until I go up a few cup sizes."
    the_person "I've already ordered new bras and everything. I'm going to keep a careful record of how many I take and when, and then take measurements over the weekend."
    the_person "[stephanie.fname] is going to stop by this weekend to help document everything, she said it would be good for research..."
    "You think about it for a moment. You picture [the_person.title] for a moment with some nice 'C' cup tits... but then you can't help but imagine if she went crazy with it and took more."
    $ try_to_convince = True
    menu epic_tits_choice_menu:
        "Sounds like a good plan":
            mc.name "You should definitely take it slow. I mean, worst case scenario, you can just take more later if you need to."
        "You should take them all":
            "[the_person.title] looks up at you, a bit surprised."
            the_person "Wh... what? I mean, I've always dreamed of having huge tits but... I mean I can always take more later, right?"
            mc.name "Fortune favors the bold, [the_person.title]. I don't think you will regret it if you do it."
            the_person "But... I've already bought all new bras and lingerie... I don't have the money right now to do that all over again!"
            menu:
                "Buy her new bras ($300)":
                    $ mc.business.change_funds(-300)
                    mc.name "I'll consider it an investment, from the business. It is the least we can do if you are willing to test the new serum prototypes."
                    the_person "Oh... that's very generous! I mean, I suppose if you're willing to do that. I can probably return a bunch of the other ones too."
                    "She stands there for a few moments, considering her options."
                    the_person "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                    mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                    "She blushes and nods."
                    the_person "Alright, see you Monday!"
                    $ mc.change_locked_clarity(10)
                    $ add_sarah_epic_tits_action()
                    return
                "Stop wearing bras":
                    if the_person.sluttiness > 40:
                        $ the_person.draw_person(position = "stand4", emotion = "happy")
                        the_person "Oh! Well that's an idea. Funny, why hadn't I thought of that?"
                        if the_person.should_wear_uniform:
                            the_person "If I do that... Are you going to relax the dress code a bit? That's fine as long as I don't have to wear bras to work anymore..."
                            if not commando_uniform_policy.is_active:
                                mc.name "I will definitely look into it, if it helps you make up your mind."
                            else:
                                mc.name "Have you been wearing bras? Our uniform policy strictly bans them already."
                        "She stands there for a few moments, considering her options."
                        the_person "Ok! I'll do it! Oh god I'm so excited. I'm going to go straight home and take a few before bedtime."
                        mc.name "Sounds good. I'll look forward to seeing... all of you... on Monday."
                        "She blushes and nods."
                        the_person "Alright, see you Monday!"
                        $ mc.change_locked_clarity(15)
                        $ Sarah_remove_bra_from_wardrobe(the_person.wardrobe)
                        $ add_sarah_epic_tits_action()
                        $ bra_removal(the_person)
                        return
                    else:
                        the_person "I just... I don't think I can do that right now. I'm sorry [the_person.mc_title]!"
                        mc.name "It's fine, I just want you to be happy with your body."
                        the_person "Right. I mean, I can always take more later if I need to."
                        $ mc.change_locked_clarity(10)

                "You're right":
                    mc.name "I just want you to be happy with your body."
                    "[the_person.title] looks a bit relieved."
                    the_person "Thanks, [the_person.mc_title]."

        "Don't take them at all" if try_to_convince:
            "[the_person.title] looks up at you, a bit surprised."
            the_person "Wh... what? I mean, I've always dreamed of having huge tits... this is my opportunity to make that dream come true."
            mc.name "[the_person.title], you are a beautiful intelligent woman, with or without huge tits, you are still a woman I would love to date."
            the_person "Do you really mean that [the_person.mc_title], would you like dating me as I am now?"
            mc.name "Of course I would, now give me those vials."
            the_person "I don't know, I really want to give this a shot."
            menu:
                "Insist":
                    pass
                "Relent":
                    mc.name "Ok, have it your way, but I still think it's a mistake."
                    $ try_to_convince = False
                    jump epic_tits_choice_menu
            mc.name "I have to insist [the_person.title] and be happy I don't give you a good spanking for being so dumb as to think men only judge woman by their breast size."
            "She looks at you shocked for the harshness of your words, but slowly stretches out her hand, giving you the serum."
            mc.name "Good, and if [mc.business.head_researcher.name] gives you any troubles, let her come see me. Now get out of here and go home."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] gives a short nod and quickly scoots out of the building."
            # don't let her take them end epic tits story line
            $ sarah.event_triggers_dict["epic_tits_progress"] = -1
            return

    mc.name "Alright, you be careful this weekend. I'll look forward to seeing... all of you... on Monday."
    "She blushes and nods."
    the_person "Alright, see you Monday!"

    $ add_sarah_new_tits_action()
    return

label Sarah_epic_tits_label():
    python:
        the_person = sarah
        the_person.tits = "F"
        the_person.event_triggers_dict["epic_tits_progress"] = 3
        the_person.change_stats(happiness = 5, slut = 1, max_slut = 40)
    call Sarah_tits_reveal_label() from Sarah_epic_tits_call_1
    return

label Sarah_new_tits_label():
    python:
        the_person = sarah
        the_person.tits = "D"
        the_person.event_triggers_dict["epic_tits_progress"] = 2
        the_person.change_stats(happiness = 3, slut = 1, max_slut = 40)
    call Sarah_tits_reveal_label() from Sarah_new_tits_call_1
    return

label Sarah_tits_reveal_label():
    $ the_person = sarah
    "Your phone rings. It's [the_person.possessive_title]. You answer it."
    the_person "Hello [the_person.mc_title], could you meet me in your office? It's urgent."
    "You put your phone in your pocket and head to your office."
    $ mc.change_location(ceo_office)

    $ the_person.draw_person()
    "[the_person.title] steps confidently into your office."
    the_person "Good morning [the_person.mc_title]! Ready for our Monday meeting?"
    "Your jaw drops when you look up."
    $ mc.change_locked_clarity(15)
    mc.name "Wow, [the_person.title], you are awfully perky this morning!"
    "She laughs at you and smiles."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "Thank you [the_person.mc_title]. I'm sorry again about being sneaky about the whole thing. I really appreciate you letting me do this!"
    "You notice she turns and closes your office door... and then locks it."
    if the_person.tits_available:
        "[the_person.title] takes a breast in her hand, enjoying the weight of it."
        the_person "It is incredible. So much better than a implant, and they've gotten more sensitive too."
        "Her hand begins to idly pinch one of her nipples."
        $ the_person.change_arousal(15)
        the_person "Mmm. Go ahead and touch them. I want to feel your hands one me!"

    else:
        the_person "Do you want to give them a closer look? I mean, you are the man who made this all possible..."
        "You quickly agree."
        $ the_person.strip_to_tits(prefer_half_off = False)

        "Her chest now bare before you, [the_person.title] takes a breast in her hand, enjoying the weight."
        the_person "Go ahead and touch them. These are so much better than implants, I can't believe how good they feel. And they are so sensitive too..."
    $ mc.change_locked_clarity(30)
    "With both hands your reach and cup her considerable chest. The skin is soft and pliable in your hands."
    $ the_person.change_arousal(15)
    the_person "Mmmmmm. Don't be shy! Play with them a bit. It feels so goooood..."
    "You begin to knead her chest a bit rougher now. She gasps as you struggle to get all of her pleasant titflesh in your hands."
    $ the_person.change_arousal(15)
    the_person "Oh god, you are getting me so hot..."
    "Her knees buckle for a second when you start to play with her nipples. You pinch and roll them in your fingers."
    $ the_person.change_arousal(15)
    the_person "Ah! Stop! God that feels amazing. But there's something else I want to try..."
    mc.name "Oh? What is that?"
    the_person "Well, I've tried this a couple times before but to be honest my chest was so small I don't think it was very good for the guy but... I want your cock between my tits!"
    mc.name "That sounds hot. Let's do it!"
    "You turn your chair to the side and [the_person.title] gets on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] eagerly begins opening your pants. She pulls out your cock and gives it a few gentle strokes."
    $ mc.change_locked_clarity(50)
    the_person "I can't believe I'm finally doing this. This all feels like a dream!"
    "She looks up at you from her knees. She looks you right in the eyes as she leans forward and slides your cock between her pillowy tits."
    "With both hands holding her breasts together, she slowly starts to move her pillowy flesh up and down your erection."

    # boost sluttiness to prevent tit fuck aborting due to low sluttiness
    if tit_fuck.slut_requirement > the_person.effective_sluttiness(tit_fuck.associated_taboo):
        $ the_person.add_situational_slut("first_time", 10 + (5 * (tit_fuck.slut_requirement - the_person.effective_sluttiness(tit_fuck.associated_taboo))), "I can finally do it, no way I'm chickening out!" )
    else:
        $ the_person.add_situational_slut("first_time", 10, "I can finally do it, no way I'm chickening out!" )

    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_sarah_tits_reveal_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Oh my god, I came so hard... I can't believe it. That felt so good! I need to do that again soon!"
        if the_person.get_opinion_score("showing her tits") < 2:
            $ the_person.update_opinion_with_score("showing her tits", 2)
    else:
        the_person "Mmm, that was so hot. I can't wait to try that again..."
        if the_person.get_opinion_score("showing her tits") < 1:
            $ the_person.update_opinion_with_score("showing her tits", 1)
    $ the_person.clear_situational_slut("first_time")

    the_person "Okay... let me go get cleaned up... then I'll come back and we can start our regular Monday meeting!"
    $ the_person.draw_person(position = "walking_away")
    "She gets up and leaves the room. You smile to yourself, thinking about how good her new tits felt around your cock."
    $ the_person.apply_planned_outfit()
    $ add_sarah_workout_in_tshirt_action()
    return

label Sarah_workout_in_tshirt_label(the_person):    #60 sluttiness event
    $ the_person = sarah
    $ the_person.apply_outfit(get_sarah_workout_event_outfit())
    $ the_clothing = the_person.outfit.get_upper_top_layer
    "You step into the gym. You change in the locker room and get ready for a good workout."
    "You step out and look around, trying to decide how you want to warm up. As you look around, you notice [the_person.possessive_title] stepping out from the women's lockers."
    $ the_person.draw_person()
    "She has on a pair of tight workout shorts and a white camisole, and you are pretty sure she isn't wearing a bra underneath it..."
    "You walk over to her to say hello."
    mc.name "Hello [the_person.title]. Here for some yoga?"
    the_person "Oh hi [the_person.mc_title]! Actually yoga was cancelled today, so I decided to come and get a good workout instead!"
    mc.name "I see... are you sure your outfit is appropriate?"
    the_person "Of course... I've got everything covered! Although the shorts might be a little short."
    "[the_person.title] gives you a wink. It appears she knows exactly what is going to happen when she works up a good sweat."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks off and finds an elliptical machine. She starts it up and starts working out."
    "You decide this is too good of an opportunity to pass up, so you find a treadmill near her machine where you can watch."
    "At first, you just kind of zone out. You hit a good pace and are enjoying your workout, almost forgetting about [the_person.title]."
    "However, after a couple of miles, you remember her and look over to see how she is doing."
    $ the_clothing.colour[3] *= .8
    $ the_person.draw_person(position = "walking_away")
    "It appears that she has started sweating, and the moisture has begun to soak into her shirt, making it a little transparent."
    "So far, it appears that no one has really taken notice, so you continue to watch."
    $ the_clothing.colour[3] *= .8
    $ the_person.draw_person(position = "walking_away")
    "After a couple more miles, the effect of her sweat on her shirt has gotten very noticeable. As she works out, guys walking by have started to stop and gawk at her."
    "You slow your treadmill down to a walk as you start to cool down, and eventually [the_person.possessive_title] stops her elliptical and gets off."
    $ the_person.draw_person()
    "?????" "Holy shit those tits are... AH!"
    "When she turns around, you hear the guy on a treadmill a couple down from you trip and fall off."
    "[the_person.title] walks over to you."
    the_person "Hey! Wow, looks like you got a good workout in too!"
    $ mc.change_locked_clarity(30)
    "You can barely formulate a response with her sweat drenched titties heaving up and down as she breathes heavily."
    mc.name "Yeah, I've certainly got my heart rate up."
    the_person "Well, I'm gonna go shower, see you around!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks off, towards the locker room."
    "She walks by a guy and girl who are working out together. The guy stares at her tits as she walks by, and the girl he is working out with notices and smacks him."
    $ sarah.event_triggers_dict["gym_tshirt"] = True
    return

label Sarah_stripclub_story_label():
    $ the_person = sarah
    $ the_person.planned_outfit = get_sarah_date_outfit_two()
    $ the_person.apply_outfit(the_person.planned_outfit)

    $ scene_manager = Scene()
    #TODO going out outfit
    "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
    the_person "[the_person.mc_title]! You crazy workaholic, let's go blow off some steam!"
    "You look up and see [the_person.title] standing in the doorway."
    $ scene_manager.add_actor(the_person, emotion = "happy")
    if sarah_epic_tits_progress() != -1:
        "You still aren't quite used to her enhanced chest size. You realize you are blatantly checking her out as she stands in the door."
        the_person "Mmm, I've been getting exactly that look from a ton of guys lately... and a few girls too."
        the_person "It's been great! I can't thank you enough for helping this happen. I think I might know a way to repay you a little bit though..."
    else:
        "She is a quite a stunner and you realize you are blatantly checking her out as she stands in the door."
        the_person "Mmm, I like the way you look at me and just the other day I saw some girls checking me out too."
        the_person "Thank you for convincing me to stay true to myself. I think I might know a way to repay you a little bit though..."
    $ mc.change_locked_clarity(20)

    mc.name "It's okay, you don't have to do anything, I was just happy to help!"
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "Hah! [the_person.mc_title], that's one of the things I love about you. You are so giving of yourself and your resources."
        $ the_person.change_love(5)
    else:
        the_person "Hey now, friends with benefits means we both get benefits, but lately it feels like I've been getting most of the benefits!"
        the_person "This arrangement has been great, I don't want it to end just because I'm the only one getting anything out of it."
    the_person "This time though, you are going to have to let me do something for you. Don't worry, we're both gonna like it."
    mc.name "Ok, what did you have in mind?"
    the_person "You'll just have to see! Let's go!"

    $ mc.change_location(downtown)
    if the_person.event_triggers_dict.get("dating_path", False):
        "[the_person.possessive_title] holds your hand as you leave the lab and head downtown."
        "You pass the bar you usually go to. Where is this girl taking you?"
    else:
        "[the_person.possessive_title] leads the way as you leave the lab and head downtown."
        "You pass the bar you usually go to. You wonder what this crazy girl has in mind for tonight."
    "Soon you walk up to a building and [the_person.title] comes to a stop. The sign out from says [strip_club.formal_name]."
    "Wow, a strip club? This could be interesting. You decide to tease her."

    # if MC has not yet discovered this place, make it visible on the map
    if not strip_club.visible:
        $ strip_club.visible = True

    mc.name "You know, it's against company policy to be moonlighting at a place like this. Even with a body like yours."
    the_person "Ha! No I haven't been working here, I just thought it would be fun to watch a couple shows."
    $ mc.change_locked_clarity(10)
    mc.name "Sounds great!"

    $ mc.change_location(strip_club)

    "You head inside. Your senses are assaulted by everything going on. The loud bass music thumps in your ears. On stage you see a girl shaking her ass for a group of guys."
    "You check around quickly... looks like [the_person.title] is one of the few women in the crowd with you."
    the_person "Come on, let's grab a table to the side before we decide what to do first!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You sit down across from [the_person.possessive_title] in a booth."
    the_person "Alright, let's just watch the girls from here for a little bit. I'm going to buy you a private dance before we go."
    mc.name "That's... very generous of you. You know you don't have to do that, right?"
    the_person "Sure but, it's not like I'm not going to have fun while we're here too. I've heard the girls here are hot!"
    "It's been clear for a while now that [the_person.title] has an interest in both men and women. It's cute to see her coming out of her shell a bit and enjoying her sexuality."
    the_person "Oh look! Here comes a girl now!"
    "Your eyes are drawn to the stage."
    call watch_strip_show(the_person) from Sarah_strip_show_call_1
    $ mc.change_locked_clarity(50)
    the_person "Wow! That was impressive! I've never been to a place like this before, but I can see why guys like it so much..."
    "As she finishes her sentence, one of the guys who had been around the stage gets a little too close to your table. You can see him checking out [the_person.title]."
    "???" "Hey there, aren't you a doll! Whaddya say to a private dance in the back? Not sure how much this guy is paying, but I could make it worth your while..."
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "Not likely! I'm reserved for my boyfriend here."
    else:
        the_person "Not likely!"
        "???" "Come on baby, I bet I can pay you better than what this guy is payin' you to be here with him!"
        the_person "Yeah right! This guy owns his own pharmaceutical business. Move along now."
    "You get ready to add in to the conversation, but the guy gets the point."
    if sarah_epic_tits_progress() >= 2: # only when she got the big boobs
        "???" "Damn, alright. Enjoy those tits mister, they look fantastic."
    else:
        "???" "Damn, alright. Have a nice time mister, she's gorgeous."
    $ the_person.change_happiness(5)
    "The guy wanders off. [the_person.possessive_title] has a smug look on her face."
    the_person "Damn right they're fantastic. What do you think, [the_person.mc_title]. Are you gonna enjoy these tits later?"
    $ mc.change_locked_clarity(20)
    "Before you can respond, the music starts up again and another girl comes out on the stage."
    the_person "Oh! Here we go again!"
    call watch_strip_show(the_person) from Sarah_strip_show_call_2
    $ mc.change_locked_clarity(50)
    $ showgirl = _return
    if showgirl.has_large_tits:
        the_person "Damn! That girl had a nice chest. Wish I could get my hands on her..."
    else:
        the_person "That was impressive! Even though her chest was small, she certainly knows how to work her body. Wish I could get my hands on her..."
    if showgirl is cousin:
        "While it was true, you aren't sure you have the guts to tell her that the girl on stage was your cousin, [cousin.title]."
        "Either way, she seemed to really enjoy her performance."
    else:
        "She seems to have really enjoyed this particular performance."
    "You enjoy your time with [the_person.title]. As girls come and go off the stage you both remark on what you like or didn't like about each performance."
    the_person "Mmm, I think I've seen enough. So, want to go back to the private room for a lap dance? Any girls in particular stand out to you?"
    "You think about it for a second. Then decide to change it up a little."
    mc.name "I've got a better idea. Why don't we both get a private dance?"
    "[the_person.title] raises an eyebrow."
    the_person "You mean... I figured that they only did private dances for guys..."
    mc.name "Nah, if you give me a minute, I bet I can get it set up."
    the_person "But I don't have the money for two..."
    mc.name "Ah! Forget about it. I'll put it on the company card. This is a team building exercise, right?"
    the_person "Team building... right! I can get behind that!"
    mc.name "Ok, I'll be right back."
    $ scene_manager.hide_actor(the_person)
    if get_strip_club_foreclosed_stage() < 5:
        "You get up and head over to the counter where the owner is."
    else:
        "You get up and head over to the counter and talk with the manager."
    if cousin.event_triggers_dict.get("blackmail_level", -1) >= 2 and cousin.has_role(stripper_role):
        if showgirl is cousin:
            "You arrange two private lap dances: for [the_person.title] you get [cousin.possessive_title] since she enjoyed her so much, and you pick a random girl for yours."
        else:
            "You arrange two private lap dances: for [the_person.title] you ask for the girl that did the second dance on stage since she enjoyed her so much."
            "You smile when you look at the list of stage names for the available strippers: you see the one that must be referring to [cousin.title] and pick her for yours."
    else:
        "You arrange two private lap dances: for [the_person.title] you ask for the girl that did the second dance on stage, and you pick a random girl for yours."
    $ mc.business.change_funds(-200)
    "You go to the back, and find a room with two chairs facing each other. [the_person.title] sits across from you."
    $ scene_manager.show_actor(the_person, position = "sitting", emotion = "happy", display_transform = character_left_flipped)
    the_person "Mmm, I'm so nervous..."
    #TODO make a variant on character left that is a close to Sarah so it looks more like an actual lap dance.
    $ showgirl.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl, display_transform = character_center_flipped)
    if cousin.event_triggers_dict.get("blackmail_level", -1) >= 2 and cousin.has_role(stripper_role):  #We have blackmailed Gabrielle about stripping already#
        if showgirl is cousin:
            $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x != showgirl])
        else:
            $ showgirl_2 = cousin
    else:
        $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x != showgirl])
    $ showgirl_2.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_2)
    showgirl_2 "Alright! We got a couple in here tonight, this should be fun!"
    if showgirl_2 is cousin:
        "Suddenly, [showgirl_2.title] realizes it's you she is getting ready to dance for."
        "[showgirl_2.possessive_title] lowers her face to your ear and whispers in it."
        showgirl_2 "What the fuck? You want me to give you a lap dance? Here??? In front of your little bimbo? You're a sick fuck..."
        mc.name "Don't worry, I'll make it worth it."
        showgirl_2 "You better..."
        "She stands back up and acts as if nothing happened."
        $ mc.change_locked_clarity(30)
    if showgirl is cousin:
        "You see [showgirl.title] looking over to you, realizing that you are gonna be in the room as she performs for [the_person.title]."
        "She gives you a quick wink."
        $ mc.change_locked_clarity(10)
    showgirl "Alright, let's get the fun started!"
    $ scene_manager.update_actor(showgirl_2, position = "kneeling1")
    "Your stripper gets on your lap. She starts to take off her top."
    $ scene_manager.strip_to_tits(person = showgirl_2)
    "With her tits free, she begins to gyrate them back and forth, right in front of your face. They wobble appealingly."
    $ mc.change_locked_clarity(30)
    $ scene_manager.update_actor(showgirl, position = "blowjob")
    "You glance over and notice the girl in front of [the_person.title] is doing something similar."
    $ mc.change_locked_clarity(10)
    $ scene_manager.strip_to_tits(person = showgirl)
    showgirl_2 "For $100, you two can play with our tits for a bit."
    if showgirl_2 is cousin:
        "[showgirl_2.title] lowers her lips to your ear again."
        showgirl_2 "Don't you wanna grab your cousin's tits, pervert?"
    "You see [the_person.title] look over at you. You can see her mouth the word 'please'."
    mc.name "That sounds fair."
    "You grab $100 and put it in the tip jar."
    $ mc.business.change_funds(-100)
    "Before you finish putting the money in the jar, you notice that [the_person.title] has her hands all over her stripper's chest."
    "She seems to be really enjoying the show so far!"
    $ mc.change_arousal(10)
    $ the_person.change_arousal(12)
    if showgirl_2 is cousin:
        "You reach up and grope [showgirl_2.possessive_title]'s tits. You're mesmerized by how soft and warm they are."
        $ mc.change_locked_clarity(40)
    else:
        "You reach up and begin to fondle your stripper's tits. They are so soft and warm. They feel amazing."
        $ mc.change_locked_clarity(30)
    "After a while, it's time to change things up. Both strippers get up and turn to so their backs are facing you and [the_person.title]."
    $ scene_manager.update_actor(showgirl_2, position = "standing_doggy")
    $ scene_manager.update_actor(showgirl, position = "standing_doggy")
    "Your girl puts her ass against your chest and starts to wiggle her hips back and forth as she slowly works herself down your body."
    "Soon she is working your erection with her hips, through both of your clothes."
    $ mc.change_locked_clarity(30)
    "She starts to strip down her remaining clothing."
    $ scene_manager.strip_to_vagina(person = showgirl_2)
    "You notice that [the_person.title] and her stripper are in a similar state."
    $ scene_manager.strip_to_vagina(person = showgirl)
    "Her ass bare now, you find it difficult to restrain your hands from molesting the girl in front of you."
    $ mc.change_arousal(15)
    $ the_person.change_arousal(20)
    showgirl_2 "For $200, you two can touch anywhere you want, other than pussies, while we dance for you."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 50:
        "[showgirl_2.title] looks bank and whispers at you."
        showgirl_2 "Maybe later you can touch me there..."
    "You don't hesitate. You grab $200 and put it in the tip jar."
    $ mc.business.change_funds(-200)
    "[the_person.title] sees you do it and immediately starts to run her hands along her girl's hips."
    "You do the same. The girl in front of you continues to work her hips back and forth across your erection as you run your hands along her hips."
    "You cup and grab her ass a few times when you have the opportunity. Her hips sway enticingly."
    $ mc.change_locked_clarity(50)
    "You look up and see [the_person.title] hands roaming all over her stripper's body. She plays with her tits for a while, then runs her hands along her sides and down her legs."
    $ mc.change_arousal(40)
    $ the_person.change_arousal(45)
    "It's beginning to get hard to control yourself, you are getting close to cumming, when it is time for the lap dance to end."
    $ scene_manager.update_actor(showgirl, position = "stand4")
    $ scene_manager.update_actor(showgirl_2, position = "stand5")
    showgirl "Mmm, that was fun! It's been forever since I had a female client. They always give such loving touches..."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 70:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2 "That was fun... how soon until I get to play with your girlfriend too? Soon I hope?"
    elif showgirl_2 is cousin:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2 "I hope your little slut doesn't realize we're related. That would be an unfortunate event, for sure..."
    "The strippers leave, leaving you and [the_person.title] alone and highly aroused."
    $ scene_manager.remove_actor(showgirl)
    $ scene_manager.remove_actor(showgirl_2)
    $ del showgirl
    $ del showgirl_2
    the_person "Good lord... we need to get out here! Can we go back to your place?"
    mc.name "Absolutely."
    "You both head out and are soon walking through your front door."
    $ mc.change_location(hall)
    $ scene_manager.update_actor(the_person, position = "stand2", display_transform = character_right)
    the_person "Oh god I can't wait to get to your bedroom and..."
    $ scene_manager.add_actor(mom, display_transform = character_left_flipped)
    "[mom.title] pops around the corner when she hears you walking down the hall and unknowingly interrupts."
    mom "Hey [mom.mc_title]. You missed dinner! Leftovers are in the fridge. Oh! Hello again!"
    mc.name "Thanks, we're just going to go to my room for a bit to discuss some... work related matters."
    "You see [mom.title] quickly appraises the situation."
    mom "Right. Have fun talking about work stuff! HAH! Nice to see you again!"
    the_person "Nice to see you again too."
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.possessive_title] walks away, chuckling to herself."
    $ scene_manager.remove_actor(mom)

    $ mc.change_location(bedroom)

    "Finally, you reach your bedroom and quickly close and lock the door."
    mc.name "God I'm sorry, if you aren't in the mood anymore..."
    the_person "Sorry for what? It's your mom, I think it's sweet."
    mc.name "So... do you wanna..."
    the_person "Oh fuck yeah, I'm so worked up. But first I want to try something! Why don't you sit down on the bed there."
    "You quickly sit down."
    mc.name "What do you have in mind, [the_person.title]?"
    the_person "I'm gonna give you a lap dance. Just like that girl at the strip club."
    if the_person.event_triggers_dict.get("dating_path", False):
        the_person "But the difference is, you can touch me all you want to!"
        mc.name "Mmm, don't mind if I do."
    else:
        the_person "But remember, no touching!"
        mc.name "No promises."
    $ scene_manager.update_actor(the_person, position = "kneeling1")
    "[the_person.title] climbs up on your lap."

    if the_person.tits_available:
        "She runs her hands through your hair and brings your face up to her naked, heaving chest."
    else:
        "She begins to undress her top half right in front of you, letting you watch as she exposes her soft skin."
        $ scene_manager.strip_to_tits(person = the_person)
        "As she pulls off her last piece of clothing, she runs her hands through your hair and brings your face to her naked, heaving chest."
    $ mc.change_locked_clarity(30)

    if the_person.event_triggers_dict.get("dating_path", False):
        "Your hands naturally reach up and begin to fondle [the_person.possessive_title]'s breasts."
        the_person "Mmmm, that's it baby. It feels so good when you touch me there."
        $ the_person.change_arousal(10)
    else:
        "Your hands begin to move towards [the_person.possessive_title]'s breasts, but she slaps your hands away."
        the_person "Hey! You know the rules, no touching!"
        "You quickly lower your hands to your sides."
    "[the_person.title] is slowly grinding herself in circles against your lap. The heat of her body against yours is really getting you worked up."
    "With the excitement from the strip club earlier, you are starting to ache for some relief."
    $ mc.change_arousal(10)
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "[the_person.possessive_title] stands up and turns away from you."
    if the_person.vagina_available:
        "Her hips sway back forth. Her shapely ass inches from your face makes a tantalizing target."
        $ scene_manager.strip_full_outfit(person = the_person)
    else:
        "She begins to slowly strip her bottom half down in front of you, swaying her hips tantalizingly as she does so."
        $ scene_manager.strip_full_outfit(person = the_person)
        "Now naked in front of you, you can't tear your eyes away from her bare ass, mere inches from your face."
    "Her pussy is dripping with excitement. It looks like you could probably make her cum in seconds, she is so turned on."
    the_person "Oh god I'm so hot... I can't take it!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She bends over and pushes her ass back against your face. You immediately begin to lick and probe her slit with your tongue."
    the_person "It was so hot having those girls strip for us earlier... I need to cum, make me cum!"
    $ mc.change_locked_clarity(50)
    $ play_spank_sound()
    "You reach up and grab her hips with your hands. You give one cheek a hard spank while your tongue snakes its way inside of her."
    $ the_person.change_arousal(30)
    the_person "Yes! Oh fuck I'm gonna cum!!!"
    $ the_person.have_orgasm()
    $ the_person.change_stats(obedience = 5)
    "You grip her hips roughly to hold her still as you bring her to a climax. Her knees start to buckle but you hold her ass firmly in place."
    "She gives a low, steady moan when she finally finishes climaxing."
    $ the_person.change_arousal(-(the_person.arousal / 3))
    the_person "Oh god I needed that so bad... I think... you're gonna have to take over, [the_person.mc_title]."
    "The excitement of the evening has you on edge, so you grab [the_person.title] and throw her down on the bed."
    $ scene_manager.update_actor(the_person, position = "doggy")
    "You quickly strip out of your clothes and get behind her, lining yourself up with her slit."
    if mc.energy < 30:
        $ mc.energy = 30
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_stripclub_aftermath_1
    "When you finish with her, [the_person.title] collapses in the bed."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You cuddle up next to her as you both catch your breath."
    #complex decision tree here.
    # If dating path, have her ask to be your girlfriend officially.
    # If she is already dating someone else, have her break up with them
    # If she is already married, turn it into an affaire
    # if she is engaged, have her break it off.
    # If not dating path, she recovers, then heads out
    if the_person.has_role(girlfriend_role):  #You are already dating her via other means. She just cuddles up with you.
        "As you both recover, [the_person.possessive_title] starts kissing you along your neck, then whispers in your ear."
        the_person "Thank you for the good time tonight. I love you."
        mc.name "I love you too."

    elif the_person.event_triggers_dict.get("dating_path", False):
        "After you both recover, you continue to lie together, enjoying your flesh being against one another. She seems deep in thought, but eventually asks you a question."
        if the_person.relationship == "Single":
            the_person "So... we've done this a couple times now and... I know this is usually where the man kind of takes the lead but umm..."
            the_person "Every time I think about you, and being with you, I get so happy, and I start smiling."
            the_person "Is it... can we just make it official? I want to be with you. I want to be your girlfriend!"
            menu:
                "Make it official":
                    the_person "Yes! Oh my god you have no idea how happy that makes me to hear, that you feel the same way!"
                    $ the_person.change_stats(happiness = 10, love = 3)
                    "She kisses you, and you kiss her back."
                    $ the_person.add_role(girlfriend_role)

                "Let's just be friends":
                    the_person "Ah... okay wow, I guess I was just... totally misinterpreting things between us..."
                    $ the_person.change_stats(happiness = -10, love = -5)
                    $ the_person.event_triggers_dict["dating_path"] = False
                    the_person "I didn't realize you just wanted things to be strictly physical between us. Is that what you want? Friends with benefits?"
                    mc.name "Yes that is what I am looking for right now."
                    the_person "Okay... I'm sorry I didn't realize. But I think I can manage that."

        elif the_person.relationship == "Married":
            the_person "So... we've done this a couple of times. I know, I'm a married woman, but I can't stop thinking about you."
            the_person "Every time I think about you, I get a little bit wet thinking about what you do to me."
            the_person "Is this something you want to continue? I can't leave my husband but you can fuck me anytime you want!"
            menu:
                "Have an affair":
                    the_person "Okay. Wow, I never thought I would do this..."
                    "She reaches down and gives your softened cock a few strokes."
                    the_person "But the things you do to me... my husband doesn't even come close!"
                    $ the_person.add_role(affair_role)
                    $ the_person.change_slut(2)
                "Let's keep it casual":
                    the_person "Ah, okay. So like, friends with benefits? Is that what we are talking about here?"
                    mc.name "Exactly."
                    the_person "Okay. That actually makes things a little easier for me. I can manage that!"
                    the_person "And if my husband ever asks, I'm just with friends!"
                    $ the_person.event_triggers_dict["dating_path"] = False
        else:       #She is a girlfriend or a fiancee
            the_person "So... we've done this a couple of times. I know, I'm seeing someone else right now, but I can't stop thinking about you."
            the_person "Honestly, if you gave the word, I would call him up and dump him right now so that we could be together!"
            the_person "So... should I do that? I just want to be your girlfriend!"
            menu:
                "Dump him for me":
                    "[the_person.title] takes a deep breath, then slowly gets up."
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    the_person "Okay. For you, I'll do it. Here we go."
                    "You watch as she dials her man. She talks quietly into her phone, so you can't make out everything she is saying."
                    "It takes her several minutes, and you hear her apologize a few times, but eventually she finishes and hangs up her phone."
                    "She crawls back into bed beside you."
                    $ scene_manager.update_actor(the_person, position = "missionary")
                    "Well, it's official. I'm all yours now!"
                    python:
                        the_person.add_role(girlfriend_role)
                        the_person.change_stats(love = 10, obedience = 5)
                "Let's keep it casual":
                    the_person "Ah, okay. So like, friends with benefits? Is that what we are talking about here?"
                    mc.name "Exactly."
                    the_person "Okay. That actually makes things a little easier for me. I can manage that!"
                    $ the_person.event_triggers_dict["dating_path"] = False

    else:
        "As you both recover, [the_person.possessive_title] just lays back and enjoys the warmth of your skin."
        the_person "Mmmm, that was such a fun night, [the_person.mc_title]. I don't want to get up..."
    $ the_person.event_triggers_dict["stripclub_progress"] = 1
    $ staying_over = False
    if the_person.has_role(girlfriend_role):
        the_person "It feels so good to be next to you, I could lay like this all night."
        mc.name "Why don't you? Just spend the night here."
        the_person "Oh! That's a great idea!"
        $ staying_over = True
    elif the_person.has_role(affair_role):
        the_person "It feels so good to be next to you, but I need to get home."
        mc.name "You don't have to. Just spend the night here."
        the_person "I'm sorry I can't. Thanks for the offer though!"
    else:
        the_person "I need to get going... I guess. Thanks for the evening though. It was great!"
        mc.name "You don't have to. Just spend the night here."
        the_person "That's tempting, believe me, but I need to get home. Thanks for the offer!"
    if staying_over:
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "Worn out from your date with [the_person.possessive_title], you cuddle up with her and quickly fall asleep."
        $ mc.change_locked_clarity(50)
        call Sarah_spend_the_night() from sarah_stripclub_spend_the_night_sequence
    else:
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
        $ scene_manager.remove_actor(the_person)

    $ add_sarah_threesome_request_action()
    $ scene_manager.clear_scene()
    return "Advance Time"

label Sarah_threesome_request_label():
    $ scene_manager = Scene()
    $ the_person = sarah
    $ gossip_target = get_random_employees(1, exclude_list = [sarah], slut_required = 50)
    if gossip_target is None:
        return

    "Another Saturday, another extra workday for you. You are hardly surprised when you hear [the_person.title]'s familiar voice."
    the_person "Hey [the_person.mc_title]. I figured you'd be around here."
    $ scene_manager.add_actor(the_person)
    mc.name "Hello [the_person.title]."
    if the_person.has_role(girlfriend_role):
        "You admire your girlfriend as she stands in the door. God she is sexy."
    elif the_person.has_role(affair_role):
        "You admire your mistress as she stands in the door. It's so hot fucking a taken woman."
    else:
        "You admire [the_person.title] as she stands in the door."
    "You notice she is carrying a bottle of something."
    mc.name "Is that... Scotch?"
    the_person "Yup! I'm like... totally not suggesting we just get wasted right here or anything..."
    "You feel yourself raise an eyebrow."
    the_person "But uhh, you know, if we DID happen to get wasted and banged in every room in the business, I'm pretty sure I would be okay with that."
    $ mc.change_locked_clarity(10)
    "Jesus, this girl is insatiable. It's amazing!"
    the_person "You got any shot glasses?"
    mc.name "No... I actually don't have any around."
    "You think about a possible solution."
    if not mc.location == mc.business.r_div:
        mc.name "Why don't we start down in research? I'm sure we have some extra beakers we could use."
        the_person "Let's go!"
        $ mc.change_location(rd_division)
    mc.name "Pull up a seat."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You grab a couple vials from one of the desks. [the_person.possessive_title] hands you the bottle and you pour the first round."
    mc.name "Cheers!"
    the_person "Cheers!"
    "You tap your vials together and take your shots together. It burns on the way down, but the aftertaste is smooth."
    mc.name "Mmm, that's a good scotch."
    the_person "Thanks! I had to look for recommendations. I usually drink more girly drinks, but a good scotch is good to drink neat."
    "You pour the next round."
    the_person "Oh, in a hurry to get me tipsy, are we? You wouldn't be looking to take advantage of little ol' me, are you sir?"
    "She cracks a smile as she plays innocent."
    mc.name "You see right through me miss. Suppose I'll have to find some other unsuspecting lass."
    "She takes the vial from your hand with round two."
    the_person "Oh, that won't be necessary sir."
    "You clink your vials together again and drain them both."
    "As you sit there drinking you both start to gossip about drama around the office."
    "Being in HR, [the_person.title] knows a surprising amount of details of the other girls and their private lives."
    "You drink, gossip, and laugh with [the_person.possessive_title] for a while."
    "You aren't sure how many shots you've both done. You look at the bottle. There's only about a third of it left! That feels like a lot, but you're not sure, maybe that's a normal amount."
    "[the_person.title] is talking about a meeting she had recently with an employee."
    the_person "So then I said... what exactly am I supposed to do with these pictures of [gossip_target.name] getting fucked in the backseat of a Jeep Wrangler?"
    the_person "And she said... nothing! She just thought the pictures were hot and so she was showing all the girls in the office."
    the_person "So I said, that is pretty hot... can you text me those? Hahahahaha."
    mc.name "That's great... so do you have them?"
    the_person "Oh hell yeah, one sec..."
    "[the_person.title] fumbles around on her phone for a second. She is pretty drunk, so it takes her a while to find them."
    $ scene_manager.hide_actor(sarah)
    $ gossip_target.strip_outfit(delay = 0)
    $ scene_manager.show_actor(sarah)
    $ scene_manager.add_actor(gossip_target, position = "cowgirl", emotion = "orgasm", display_transform = character_center)
    "She shows you her phone with a picture of [gossip_target.title] riding some guy you don't recognize, in the backseat of a Jeep."
    $ mc.change_locked_clarity(25)
    mc.name "Damn! She looks like she is enjoying herself there!"
    "You enjoy the picture for a few more moments before [the_person.title] takes her phone back."
    $ scene_manager.remove_actor(gossip_target)
    $ del gossip_target
    the_person "God, I know. She is so hot, wish I could get my hands on her..."
    "So, at this point, [the_person.possessive_title] has brought it up multiple times that she would like to have some action with another girl sometime."
    "As you think through your business and all the people you have interacted with, you are pretty sure you have some girls who would love to join a threesome with you and [the_person.title]."
    mc.name "So, I know we've talked about this before, but, is a threesome still something that you would be interested in doing sometime?"
    the_person "Oh god I would do anything, just to try it once. I know it may not turn out to be as good as I hope, but, I just want to TRY, you know!?!"
    "You don't remember pouring this shot, but you grab the drink in front of you and drain it."
    mc.name "Alright, how about this. This time, next week, I'll have something set up."
    the_person "What? You mean it?"
    mc.name "Absolutely."
    the_person "That would be incredible... but... I mean, I feel like I have a right to know... who do you have in mind?"
    # use new menu layout for selecting people
    call screen main_choice_display(build_menu_items([["Request Threesome From"] + get_Sarah_willing_threesome_list()], draw_hearts_for_people = False))
    $ person_choice = _return
    $ scene_manager.update_actor(the_person, position = "sitting")
    if person_choice is mom:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person "Who did you have in mind?"
        mc.name "It's actually my mom."
        the_person "Oh! Well, I mean, she DOES have a really nice body..."
    elif person_choice is lily:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person "Who did you have in mind?"
        mc.name "It's actually my sister, [lily.fname]."
        the_person "Oh! Well, I mean, she DOES have a really nice body..."
    elif person_choice is cousin:
        "You consider carefully whether or not you should reveal that [cousin.fname] is your cousin, but you decide not to."
        mc.name "Actually, one of the strippers at the club we went to the other night is a good friend of mine."
        the_person "Ah. Are you friends with a lot of... strippers?"
        mc.name "Ha! Not really, but she and I go back a ways. And she actually owes me a favor or two."
    elif person_choice is aunt:
        mc.name "So, uh, this might sound kind of weird, but, I actually have a family member in mind."
        "[the_person.title] stays quiet for a moment before she responds."
        the_person "I mean... that's a little weird, sure. But, I mean, we're already pushing boundaries having a threesome in the first place."
        the_person "Who did you have in mind?"
        mc.name "It's actually my aunt. She's been going through a rough patch after her divorce. I think it would really help pick her up."
        the_person "Oh! Well, I mean, an aunt is fairly distant relation. And it sounds like she could use a good opportunity to cut loose..."
    elif person_choice is starbuck:
        if sex_shop_stage() >= 1:
            mc.name "I actually have a joint venture in another business. There's a woman who owns the mall sex shop, and I invested a decent sum of money in it recently."
            the_person "Ah, so, she's a business partner?"
        else:
            mc.name "I actually have a friend who owns the sex shop, over in the mall."
            the_person "Ah, so, she's another small business owner?"
        mc.name "Yeah. Her husband died a while ago, and she opened the shop in memory of him. It's a little weird, but also kinda sweet."
        mc.name "Anyway, she is very open to experimentation. I think a threesome would be right up her alley, so to speak."
        the_person "Aww, you are a sweetheart."
    elif person_choice is nora:
        mc.name "I have an old college professor, who helped develop some of the original formulas that we make here."
        mc.name "She works full time over at the university, and is overworked a bit. I'm sure she would appreciate the chance to blow off some steam with us."
    elif person_choice.is_employee:
        mc.name "I was thinking about [person_choice.name]. She seems like she would be down for just about anything, to be honest."
        the_person "Oh! She's cute! Damn, that would be great!"
    "A few moments go by as she thinks about it."
    the_person "Okay! Let's do it!"

    # Make threesome request even on talk event and add it here.
    $ sarah.event_triggers_dict["initial_threesome_target"] = person_choice.identifier
    $ sarah.event_triggers_dict["initial_threesome_arranged"] = False

    $ add_sarah_arrange_threesome_action(person_choice)

    $ add_sarah_initial_threesome_action()

    $ scene_manager.update_actor(the_person, position = "stand2")
    the_person "Oh man, all this talk about sex is starting to get me all hot. Or is it just warm in here?"
    "Without prompting, [the_person.possessive_title] stands up and starts stripping down."
    $ scene_manager.strip_full_outfit(person = the_person)
    $ mc.change_locked_clarity(30)
    the_person "Aaahhhh, that's better."
    "Your cock is getting hard, looking at [the_person.title], completely naked in front of you."
    call fuck_person(the_person) from _sarah_threesome_request_aftermath_1
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        "[the_person.title] takes it easy for a moment, enjoying the afterglow of her orgasm."
    the_person "Mmm, that was hot as always."
    $ the_person.apply_planned_outfit()
    $ scene_manager.update_actor(the_person, position = "stand3")
    if the_person.has_role(girlfriend_role):
        pass
    elif the_person.has_role(affair_role):
        the_person "I don't want to go... but I know I probably should. I'm sure someone will be waiting for me to get home..."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person "Don't forget to talk to [person_choice.name]! I'll be looking forward to next Saturday!"
        "You both say goodbye, and [the_person.title] leaves you alone in the research lab."
        $ scene_manager.clear_scene()
        $ del person_choice
        return
    else:
        the_person "God, you wore me out. I know I promised every room, but I don't think I can go on. I think I'd better catch a cab home..."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person "Don't forget to talk to [person_choice.name]! I'll be looking forward to next Saturday!"
        "You both say goodbye, and [the_person.title] leaves you alone in the research lab."
        $ scene_manager.clear_scene()
        $ del person_choice
        return
    #Assume everything from her on, sarah is girlfriend status.
    the_person "God babe, you wore me out. I know I promised every room, but I don't think I can go on. I think I'd better catch a cab home..."
    mc.name "Why don't I just get us a cab back to my place? I'm in no condition to walk home either. You can stay over."
    the_person "Ah, charming, AND economical! That's my man."
    "You call the cab and soon it arrives. You give each other little gropes and quick kisses in the back of the cab, but manage to keep things from getting too heated."
    "You get home and walk through the front door."

    $ mc.change_location(hall)

    if person_choice is aunt:
        $ scene_manager.add_actor(mom, display_transform = character_left_flipped, position = "sitting")
        $ scene_manager.add_actor(aunt, display_transform = character_center, position = "sitting")
        "As you walk down the hall, you see that [aunt.possessive_title] is sitting with [mom.possessive_title], having coffee."
        "They notice you as you enter."
        aunt "Oh hey! Good to see you [aunt.mc_title]. And who is this?"
        mc.name "Hey [mom.title], [aunt.title]. This is my girlfriend, [the_person.title]."
        mc.name "[the_person.title], you've met my mom, and THIS is my AUNT, [aunt.title]."
        the_person "Nice to meet you... OH!"
        "It suddenly dawns on her that this is who you are planning to hook up with next week..."
        the_person "Wow, you are beautiful. It's a pleasure!"
        $ mc.change_locked_clarity(10)
        "[the_person.title] is blatantly checking out [aunt.possessive_title]. Being drunk, she's lost her subtlety..."
        aunt "It's nice to meet you too!"
        "She actually seems to be appreciating the attention."
        $ aunt.change_happiness(5)
        mc.name "Ah, well, we've been drinking so uh, I think we're gonna go sleep it off now."
        mom "Okay! Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        "As you turn to leave the room, you overhear [mom.possessive_title] whispering to your aunt."
        mom "She's been over a few times... I think they are great together..."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.remove_actor(aunt)
    elif person_choice is mom:
        $ scene_manager.add_actor(mom, display_transform = character_left, position = "sitting")
        "As you walk down the hall past the kitchen, you see [mom.possessive_title] sitting at the table, having a cup of coffee. She notices you in the hall."
        mom "Oh, hey [mom.mc_title]."
        "She notices [the_person.possessive_title] walking beside you."
        mom "Oh! Hello again dear! It's great to see you!"
        "You both step into the kitchen for a moment."
        mc.name "Hey [mom.title]. I told my girlfriend, [the_person.title] she could spend the night, is that okay?"
        mom "Girlfriend? Oh that's great! Yes of course she's welcome to stay here anytime!"
        the_person "Thank you! Might I say you are looking sexy tonight."
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title] is blatantly checking out [mom.possessive_title]. Suggesting her for the threesome has changed the way she looks at her now."
        "However, being drunk, [the_person.title] has lost her subtlety."
        mom "Ha! That's sweet of you to say."
        mc.name "We've had a few drinks. I think we're gonna go sleep it off. Goodnight!"
        mom "Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        $ scene_manager.remove_actor(mom)
    elif person_choice is lily:
        $ scene_manager.add_actor(mom, display_transform = character_left_flipped, position = "sitting")
        $ scene_manager.add_actor(lily, display_transform = character_center, position = "sitting")
        "As you walk down the hall and past the living room, you see [mom.possessive_title] and [lily.possessive_title] sitting at the couch, watching a movie."
        "They notice you walking by."
        lily "Hey Bro, we're watching a movie if you wanna join us... Wow! Who's the girl?"
        mc.name "Hey [lily.title], this is my girlfriend [the_person.title]."
        lily "Wow, you didn't tell me you had a girlfriend!"
        "[lily.title] is checking out [the_person.title]. You look at her and see she is doing the same."
        lily "Nice to meet you! Damn you did good bro!"
        $ mc.change_locked_clarity(10)
        the_person "Ah, nice to meet you! [the_person.mc_title] you didn't tell me your sister was so hot."
        "[mom.possessive_title] clears her throat, trying to clear some of the sexual tension in the air."
        mc.name "Right. Anyway, we've been doing some drinking, I think we're gonna go try and sleep it off. Goodnight!"
        mom "Make sure you drink a glass of water so you aren't hungover in the morning. Goodnight you two!"
        "As you and [the_person.possessive_title] walk away, you can feel [lily.possessive_title]'s eyes lingering on the two of you."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.remove_actor(lily)
    $ mc.change_location(bedroom)
    "You get to your room. When you walk in, [the_person.possessive_title] starts to strip down."
    the_person "Hope you don't mind if I sleep naked!"
    mc.name "That would actually be ideal, if I'm being honest."
    $ scene_manager.strip_full_outfit(person = the_person, strip_feet = True)
    $ scene_manager.update_actor(the_person, position = "missionary")
    "She flops down on your bed. You hop in bed next to her."
    "You run your hands along her body as you snuggle up next to her. Her skin is so soft."
    "Her breathing is getting deep... soon you hear... is that snoring?"
    "You look at her face. She passed out."
    "Worn out, you cuddle up with her and quickly fall asleep as well."
    $ scene_manager.clear_scene()
    $ del person_choice

    call Sarah_spend_the_night() from sarah_threesome_request_spend_the_night_sequence

    return

label Sarah_arrange_threesome_label(the_person):
    if the_person.is_employee:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person "Hello! What can I help you with?"
        mc.name "Well, you know [sarah.fname], right? From HR?"
        the_person "Oh yeah, I was just talking to her this morning about the best way to get a guy to go down on you."
        mc.name "You were... what?"
        mc.name "Never mind. Anyway, she's never been in a threesome before, and she really wants to try one sometime."
        mc.name "She keeps hinting, so I promised her I'd try to arrange something for Saturday. Would you be interested in coming over Saturday night?"
        the_person "That sounds really fun! You better believe I'll go! Just let me know what time to be there."
        mc.name "Thanks!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is mom:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person "Hey Honey. What can I help you with?"
        mc.name "Well, you know how I've been seeing that girl, [sarah.fname]."
        the_person "I know! It's so great that you're seeing someone. I'm so proud of you."
        mc.name "Well, as it turns out, she's a little curious about the fairer sex. She's never been in a threesome before."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I was wondering if you would be willing to join us?"
        the_person "That sounds really fun! But umm, I mean, how would she respond to you and I... being intimate?"
        mc.name "I've actually already talked to her about it, and she's okay with it. Are you in?"
        "She thinks for a moment."
        the_person "Okay... I'll do it! I'll see you two on Saturday!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is lily:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person "Hey Bro. What do you need?"
        mc.name "Well, you know how I've been seeing that girl, [sarah.fname]."
        the_person "I know! Damn when you brought her in here the other night, that was impressive!"
        the_person "You know you guys woke me up the next morning? I know you we're trying to be quiet, but the bed banging against the wall is really loud in the rest of the house..."
        mc.name "Sorry about that."
        mc.name "Well, as it turns out, she's a little curious about the fairer sex. She's never been in a threesome before."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I was wondering if you would be willing to join us?"
        the_person "That sounds really fun! But umm, I mean, how would she respond to you being intimate with your sister?"
        mc.name "I've actually already talked to her about it, and she's okay with it. Are you in?"
        the_person "Oh! She's kinky? That sounds like fun. Okay, I'll clear my schedule for Saturday night."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is cousin:
        mc.name "Hello [the_person.title]. I need a favor I was hoping to talk to you about."
        the_person "Seriously?"
        mc.name "Yeah seriously. Don't worry you'll like it."
        mc.name "There's this girl I've been seeing lately. She is pretty bi-curious, and has never had a threesome before."
        the_person "Oh Jesus, I can tell where this is going already."
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. I need you to come over to my place Saturday night."
        if cousin.event_triggers_dict.get("blackmail_level", -1) >= 2 and cousin.has_role([stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role]):
            the_person "That's ridiculous. I'm gonna make a ton of money in tips on a Saturday night. You're gonna have to convince me..."
            mc.name "How about I promise not to tell your mom where you make all those tips at? Does that sound good?"
            the_person "Look, I need that money. I'm sorry, but I can't just give up the most lucrative night of the week."
            mc.name "Fine, I'll give you $500, right now."
            the_person "Deal!"
            $ mc.business.change_funds(-500)
            "You give her the cash. She counts it twice to make sure it's all there."
            the_person "Alright, I'll call in sick on Saturday. It's been a pleasure doing business with you."
        else:
            the_person "Can't. I have other plans for Saturday night."
            mc.name "You're always doing something late at night. What have you been up to anyway?"
            the_person "Nothing! It's none of your business, even if I was doing something."
            mc.name "Can't you just give up one Saturday night?"
            the_person "What's it worth to you?"
            mc.name "What?"
            the_person "Give me $500, right now, and I'll be there."
            mc.name "You're crazy."
            "She looks at you, unwavering."
            mc.name "Fine, I'll give you $500, right now."
            $ mc.business.change_funds(-500)
            "You give her the cash. She counts it twice to make sure it's all there."
            the_person "Alright, I'll see you on Saturday. It's been a pleasure doing business with you."
        "You give her the details. maybe picking [the_person.possessive_title] was a bad idea..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is aunt:
        "Note, this dialogue is not yet written. I'm waiting until [aunt.fname] gets further developed as a character."  #TODO
        "At the end of the dialogue, she agrees to be the threesome partner..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is starbuck:
        mc.name "Hello [the_person.title]. I've got something I need help with I was hoping to talk to you about."
        the_person "Hello! What can I help you with?"
        mc.name "Well, there's this girl I've been seeing lately. She is pretty bi-curious, and has never had a threesome before."
        the_person "Oh! I think I like her already!"
        mc.name "Anyway, she's been asking, so I promised her I'd try to arrange something for Saturday. Would you be interested in coming over Saturday night?"
        the_person "That sounds really fun! You better believe I'll come! Just let me know what time to be there."
        mc.name "Thanks!"
        "You give her the details. This is going to be a fun night!"
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    elif the_person is nora:
        # TODO: Write Nora part
        "Note, this dialogue is not yet written. I'm waiting until Nora gets further developed as a character."  #TODO
        "At the end of the dialogue, she agrees to be the threesome partner... for science..."
        $ sarah.event_triggers_dict["initial_threesome_arranged"] = True
    return

label Sarah_initial_threesome_label():
    if not sarah.event_triggers_dict.get("initial_threesome_arranged", False):
        $ mc.start_text_convo(sarah)
        sarah "Hey, are we still on for tonight?"
        mc.name "Actually, I haven't been able to talk to her yet. I'm sorry, it'll be ready next week."
        sarah "Okay..."
        $ mc.end_text_convo()
        $ sarah.change_stats(happiness = -10, love = -3)
        $ add_sarah_initial_threesome_action()
        return

    $ the_person = Person.get_person_by_identifier(sarah.event_triggers_dict.get("initial_threesome_target", None))
    if the_person is None:
        return

    "It's Saturday night. You quickly head home, you have an exciting night ahead of you."
    $ mc.change_location(bedroom)
    "You make sure your bedroom is nice and tidy."
    $ mc.start_text_convo(sarah)
    sarah "Hey, I'm here."
    $ mc.end_text_convo()
    "You head to the front door and invite her in."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(sarah)
    "You head back to your bedroom and she sits on your bed."
    $ scene_manager.update_actor(sarah, position = "sitting", display_transform = character_center_flipped)
    sarah "Oh god, I've got butterflies in my stomach. I cant believe this is finally happening. Do I look okay?"
    mc.name "You look incredible, as always."
    if the_person is lily or the_person is mom:
        "Okay, let me go get [the_person.title], I'll be right back."
        "You walk into her room. She follows you back to your room."
    else:
        $ mc.start_text_convo(the_person)
        the_person "I'm here now. Come let me in?"
        $ mc.end_text_convo()
        mc.name "She's here, give me one second."
        "You go to the front door and let in [the_person.title]. She follows you quietly to your room."
    # make the second person wear a more sexy outfit (50% sluttiness boost)
    $ the_person.apply_outfit(the_person.decide_on_outfit(sluttiness_modifier = .5))
    $ scene_manager.add_actor(the_person)
    "Alright, here you are, in your room, with [sarah.title] and [the_person.possessive_title]."
    sarah "Hi..."
    "She's getting shy. The atmosphere in the room is getting awkward. You'd better do something to break the ice!"
    mc.name "Hey, why don't you sit on the bed, [the_person.title]. I'm gonna turn on some music."
    the_person "Okay! Sounds good."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You turn some music on. A soft instrumental that should help set the mood. The girls are starting to chat."
    the_person "I'll be honest, after [the_person.mc_title] asked me to do this, I was pretty surprised, but I've really been looking forward to it."
    sarah "Oh... really?"
    the_person "Yeah. Don't worry. It might be awkward at first, but once we get going, this is going to be a LOT of fun."
    sarah "That's what I keep hoping!"
    "[the_person.possessive_title] stands up and motions towards [sarah.title]."

    the_person "Come here. This will help..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.update_actor(sarah, position = "kissing", display_transform = character_right)
    "The two girls embrace. They begin to run their hands along each others bodies. Then they begin to kiss."
    $ mc.change_locked_clarity(30)
    sarah "Mmm... your skin is so soft..."
    "Damn! They are starting to get into it. [the_person.title] has her hands around her back, while [sarah.possessive_title] is grabbing her ass."
    $ sarah.change_arousal(10)
    $ the_person.change_arousal(10)
    "The girls are starting to moan into each other's mouths. Things are heating up quickly!"
    "You decide it's time for you to make your presence known. You step directly behind [sarah.title] and hug her from behind."
    $ mc.change_locked_clarity(20)
    $ scene_manager.update_actor(sarah, position = "back_peek")
    sarah "Oh... oh my god..."
    "You wrap your left hand around and begin to fondle her tits. With your other hand you reach all the way to [the_person.possessive_title]'s back, pulling you all close together."
    "With her head to one side, you and [the_person.title] begin kissing both sides of [sarah.possessive_title]'s neck."
    $ sarah.change_arousal(25)
    $ the_person.change_arousal(10)
    "You grind your erection into her backside. She is beginning to pant heavily."
    sarah "Oh god... I need to stop... Give me a second!"
    "You both pause while you wait for her. She looks [the_person.title] in the eyes..."
    sarah "I want to taste you. I've never kissed another woman down there... I want to try it!"
    the_person "Mmm, that sounds nice. Let's do it!"
    "[sarah.possessive_title] looks back at you."
    sarah "I want you to fuck me... fuck me while I eat out another woman!"
    mc.name "Gladly! But I think everyone here is still wearing way too many clothes..."
    "The girls chuckle and then quickly agree."
    $ scene_manager.update_actor(the_person, position = "stand2", display_transform = character_center_flipped)
    $ scene_manager.update_actor(sarah, position = "stand3")
    $ scene_manager.strip_full_outfit() # strip both simultaneously
    $ mc.change_locked_clarity(50)
    "After everyone is naked, the action moves to the bed."
    call start_threesome(sarah, the_person, start_position = Threesome_doggy_deluxe, swapped = True) from sarah_initial_threesome_1
    $ scene_manager.update_actor(sarah, position = "missionary", display_transform = character_center)
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
    "As the activity winds down, you all lay down next to each other. You have [sarah.possessive_title] on one side and [the_person.possessive_title] on the other."
    sarah "Oh my god... that was so good. I never knew it could be so good, to be with another woman like that..."
    $ sarah.event_triggers_dict["threesome_unlock"] = True
    "You hear a murmur of approval from [the_person.title]."
    "You enjoy the pair of bedwarmers, and are just getting ready to fall asleep when you feel movement."
    $ scene_manager.update_actor(the_person, position = "stand4")
    the_person "Well, I had a lot of fun, but I should be going. Goodnight you two."
    "You both say goodbye. [the_person.title] grabs her stuff and leaves the room."
    $ scene_manager.remove_actor(the_person)
    if not sarah.has_role(girlfriend_role):
        sarah "Ohh, I'm not sure I can walk... but I should get going too..."
        "[sarah.title] slowly gets out of bed."
        $ scene_manager.update_actor(sarah, position = "stand4")
        sarah "That was more than I could have hoped for. Thank you so much for this!"
        $ scene_manager.remove_actor(sarah)
        "You say goodbye, and slowly drift off to sleep."
        call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_initial_threesome_no_overnight
        return
    mc.name "You're staying tonight... right?"
    sarah "Oh god, I don't think I could get up, even if I wanted to. Which I don't."
    "Worn out, you cuddle up with her and quickly fall asleep as well."
    $ scene_manager.clear_scene()

    call Sarah_spend_the_night() from sarah_threesome_spend_the_night

    python: # only add this if she is not already pregnant
        add_naomi_reconciliation_action()
    return

label Sarah_ask_for_baby_label():
    $ the_person = sarah
    $ mc.change_location(bedroom)
    $ scene_manager = Scene()
    $ mc.start_text_convo(the_person)
    the_person "Hey, can I come over tonight? I had something I wanted to talk to you about."
    mc.name "Sure. Want to spend the night?"
    the_person "Hell yeah! I'll bring some stuff over."
    "About 20 minutes later..."
    the_person "Hey, I'm here! Come let me in!"
    $ mc.end_text_convo()
    "You head to your front door and open it."
    "For once, you manage to get her back to your room while avoiding [mom.possessive_title] and [lily.title]."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She walks over and sits on your bed."
    mc.name "So... what did you want to talk about?"
    "She clears her throat. You can tell she is a little nervous."
    the_person "Well, this is kind of hard to talk about. But... we've been having a lot of unprotected sex lately..."
    mc.name "Oh my god, are you pregnant?"
    the_person "No! No, not yet anyway..."
    mc.name "Not... yet?"
    the_person "Well, [the_person.mc_title], it's been like a dream, having you back in my life like this. Things are amazing, being with you."
    the_person "I've been, well, tracking my cycles recently and, well, basically, I'm fertile right now."
    $ mc.change_locked_clarity(30)
    "You can feel your cock twitch in your pants. You imagine [the_person.possessive_title], knocked up, her tits swelling with milk and her belly growing..."
    the_person "Every time you finish inside me, I find myself thinking about it, more and more, what it would be like to get pregnant and have a baby with you."
    the_person "Look, you don't have to answer me right now, but, I thought maybe we could try and have a baby. Together?"
    "This is quite a twist! You weren't expecting this so soon, but you have to admit that the thought is exciting..."
    menu:
        "Try for a baby":
            mc.name "Honestly, I didn't realize this was something you were thinking about. But I would love to make a baby with you!"
            $ the_person.change_stats(happiness = 15, obedience = 10)
            the_person "Oh! Wow, I honestly... I thought you we're gonna say no! This is... I can't believe it."
            "She looks up at you, and you can see the changes in her facial expression. She goes from surprised, to happy, to sultry."
            the_person "So umm, like I was saying, I'm pretty sure I'm actually fertile right now..."
            mc.name "I think we should get naked now."
            the_person "Yes sir!"
            $ scene_manager.strip_full_outfit(person = the_person)
            "You get naked with [the_person.possessive_title]. She rolls onto her back and spreads her legs."
            $ mc.change_locked_clarity(50)
            the_person "Come fill me up, [the_person.mc_title]!"
            if the_person.get_opinion_score("creampies") < 2:   #From now on, she loves getting creamed, and has relevant dialogue
                $ the_person.update_opinion_with_score("creampies", 2)
            if the_person.get_opinion_score("bareback sex") < 2:
                $ the_person.update_opinion_with_score("bareback sex", 2)
            $ the_person.event_triggers_dict["try_for_baby"] = 1
            #$ the_person.event_triggers_dict["fertile_start_day"] = day  #Her 5 day fertility period starts today.
            call Sarah_fertile_period_start_label() from sarah_initial_fertile_period_start_01
            #TODO create mandatory event for starting fertility period. Stores creampies before fertility period. Then second mandatory event at the end of the fertility period determines if pregnant based on # of creampies and RNG
            call fuck_person(the_person, start_position = missionary, start_object = bedroom.get_object_with_name("bed"), skip_intro = False, skip_condom = True, girl_in_charge = False, position_locked = True) from _sarah_ask_for_baby_01
            if the_person.has_creampie_cum:
                the_person "Oh my god... we actually did it..."
                "She grabs an extra pillow and puts it under her butt so her hips are elevated."
                the_person "I'm just going to lay her like this for a bit, you know. Keep that seed nice and deep."
            else:
                mc.name "I'm sorry, I really want to, I'm just really tired."
                "You can tell she is a little disappointed."
                the_person "That's okay. Maybe in the morning?"
            "You snuggle up with [the_person.possessive_title]. You both quickly fall asleep."

        "Think about it":
            mc.name "This is a really big decision. Give me some time to think about it, okay?"
            "You can tell she is a little disappointed, but she understands your answer."
            the_person "Of course! I understand."
            #TODO add ability to revisit this decision later.
            the_person "I guess, umm, just be careful then. Wouldn't want to knock me up while you are still considering it, right?"
            "You walk up to [the_person.possessive_title] as she stands up. You put your hands on her hips and draw her close."
            $ scene_manager.update_actor(the_person, position = "kissing")
            "Your tongues meet and you begin to make out. The kissing starts innocent, but quickly grows in urgency."
            the_person "Mmm."
            call fuck_person(the_person, start_position = kissing, skip_intro = True, girl_in_charge = False) from _sarah_ask_for_baby_reject_01
            $ scene_manager.update_actor(the_person, position = "missionary")
            "When you finish, you lay down next to [the_person.title] in your bed. You both quickly fall asleep together."

    call Sarah_spend_the_night() from sarah_ask_for_baby_overnight

    return

label Sarah_spend_the_night():      #She spends the night with you. Have a random chance of a threesome with mom or lily
    python: # she stays the night so she will have to wear the same outfit again the next day
        the_person = sarah
        the_person.next_day_outfit = the_person.planned_outfit

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sarah_spend_the_night

    python: # init morning
        the_person.apply_outfit(special_fetish_nude_outfit)
        the_person.change_energy(200)
        (threesome_wakeup, threesome_partner) = get_sarah_spend_night_threesome_possibility()
        scene_manager = Scene()

    if not threesome_wakeup:
        $ scene_manager.add_actor(the_person, position = "walking_away")
        "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
        $ mc.change_locked_clarity(50)
        "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
        "Your hands cup and squeeze one of her breasts. It's so full and hot, they feel so good in your hands."
        the_person "Mmmmmmmm......"
        "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
        if the_person.is_highly_fertile:
            "You're sure she wouldn't mind an extra creampie to start the day. The more cum in her the better during her fertile period!"
        menu:
            "Try to slide yourself in":
                pass
            "Get ready for the day":
                "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
                "You get up and head for bathroom to take a leak."
                "When you come back, [the_person.title] is awake."
                $ scene_manager.update_actor(the_person, position = "missionary")
                the_person "Good morning! I slept great."
                $ the_person.apply_planned_outfit()
                $ scene_manager.update_actor(the_person, position = "stand3")
                "You both get ready for the day before heading out."
                $ scene_manager.clear_scene()
                return
        "Your cock is already hard, being up against [the_person.title], but she may not be fully wet yet."
        "You spit into your hand and rub it on your dick a few times, getting it lubed up."
        "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
        "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
        the_person "Oh [the_person.mc_title]. Mmmmmm..."
        "She's still asleep, but is still responding to your touch. She must be a heavy sleeper! Or maybe she is just really worn out from last night..."
        "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body begins to respond to the stimulation."
        $ the_person.change_arousal(20)
        "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
        $ mc.change_locked_clarity(50)
        "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(15)
        the_person "Mmm, that feels so... wait... [the_person.mc_title]?"
        $ scene_manager.update_actor(the_person, position = "back_peek", emotion = "happy")
        "[the_person.possessive_title] wakes up and looks back at you smiling."
        the_person "Oh my god that feels so good... Baby you know how to give a wakeup call, holy fuck!"
        "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
        "You pick up the pace and begin to fuck her earnestly."
        $ the_person.change_arousal(30) #70
        $ mc.change_locked_clarity(50)
        the_person "Oh yes that feels so good, fuck me good!"
        "She reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
        "Her ass is making smacking noises now, every time your hips drive your cock deep inside of her."
        $ the_person.change_arousal(40) #110
        $ mc.change_arousal(35) #90
        the_person "Oh fuck, yes! YES!"
        $ the_person.have_orgasm()
        "She shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you to fuck her even harder."
        $ mc.change_locked_clarity(50)
        mc.name "I'm gonna cum!"
        if the_person.is_highly_fertile:
            the_person "Cum deep! Knock me up with your hot cum, [the_person.mc_title]!"
        else:
            the_person "Shove it in deep! I want to feel your seed inside me all day long!"
        $ the_person.cum_in_vagina()
        $ scene_manager.update_actor(the_person) # paint cum
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
        #TODO internal fetish specific dialogue
        "You grab her hip and shove your cock deep and hold it there, cumming deep inside her. She moans and gasps with every spurt."
        "Satisfied, you slowly pull out of her."
        the_person "That's certainly one way to start the day... holy hell."
        $ the_person.reset_arousal()
        $ mc.reset_arousal()
        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person "Alright, I need to get some things done today. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)
        $ scene_manager.clear_scene()
        return

    #sexy morning wakeup starts here
    if threesome_wakeup:
        $ threesome_partner.apply_outfit(special_fetish_nude_outfit)
        "You are slow to wake up. You had several sexy dreams the night before, and you aren't ready to leave them yet."
        "It feels good, in your dream, as you slowly push your cock into [the_person.title]'s hot pussy."
        "Something stirs you though. You hear a hushed whisper. But that wasn't to you? Then a little giggle."
        threesome_partner "Mmmm, he's so big..."
        $ threesome_partner.change_arousal(30)
        "You must still be dreaming, that sounded like [threesome_partner.title]. Your cock feels amazing, wrapped in a warm, wet vice."
        the_person "I know. He was grinding against me all night last night. It was making me so horny!"
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(30)
        "Wait... what?"
        "You slowly open your eyes."
        $ scene_manager.add_actor(threesome_partner, position = "cowgirl")
        "[threesome_partner.possessive_title] is on top of you, your cock inside of her. Holy fuck!"
        "You open your eyes completely."
        $ scene_manager.add_actor(the_person, position = "kneeling1", display_transform = character_center_flipped)
        "[the_person.title] is beside her, touching herself while [threesome_partner.title] fucks you. She notices you wakeup."
        the_person "Good morning! [threesome_partner.name] came in this morning looking for you, so I invited her to hop on for a bit."
        threesome_partner "I'm sorry, I didn't realize your girlfriend was spending the night, and I was feeling needy this morning..."
        $ mc.change_locked_clarity(50)
        "As she talks, [threesome_partner.title] starts to rock her hips back and forth, enjoying the fullness of being penetrated by you."
        mc.name "Wow, what a wakeup... a guy could get used to this..."
        the_person "Mmm, I don't mind sharing you. I need a little more stimulation than my fingers though..."
        "[the_person.title] turns around, facing away from you and lifts one leg over your body, backing her pussy up to your face."
        the_person "Do me a favor and kiss me for a bit?"
        mc.name "Mmm, definitely."
        "You waste no time and dive right into [the_person.possessive_title]'s delicious cunt."
        # TODO change this scene if the girls both like anal? Need to figure out how to handle starting in a specific threesome action
        call start_threesome(threesome_partner, the_person, start_position = Threesome_double_down, skip_intro = True, private = True, position_locked = False, affair_ask_after = False, hide_leave = False) from sarah_overnight_threesome_wakeup
        $ the_report = _return
        $ scene_manager.update_actor(the_person, position = "missionary", display_transform = character_center_flipped)
        $ scene_manager.update_actor(threesome_partner, position = "missionary", display_transform = character_right)
        "All finished, the girls flop onto their backs, one on each side of you."
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0:  #They both finished.
            $ the_person.increase_opinion_score("incest", max_value = 1)
            the_person "Oh wow, that was so hot..."
            $ threesome_partner.increase_opinion_score("incest")
            if threesome_partner is mom:
                threesome_partner "I know... I just had a threesome with my son and his girlfriend... and I loved it!"
            else:
                threesome_partner "I know! A threesome with my bro and his girl... and I loved it!"
            threesome_partner "It was amazing... [the_person.fname] don't be a stranger now..."
        else:
            "You lay together for a few moments, enjoying each other's proximity."
        $ scene_manager.update_actor(threesome_partner, position = "stand3")
        "[threesome_partner.title] gets up, and remarks before leaving."
        threesome_partner "That was fun! I'm gonna head back to my room. Thanks for sharing [the_person.fname]!"
        $ scene_manager.remove_actor(threesome_partner)
        "She walks out, leaving you alone with [the_person.possessive_title]."
        the_person "That's certainly one way to start the day... holy hell."
        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person "Alright, I need to get some things done. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)
        $ threesome_partner = None

    else:
        "You are slow to wake up. You had several sexy dreams the night before, and you aren't ready to leave them yet."
        "It feels good, in your dream, as you slowly push your cock into [the_person.title]'s hot pussy."
        "It's so wet and tight, it feels almost real..."
        the_person "... [the_person.mc_title]... mmm... I can't take it anymore..."
        $ scene_manager.add_actor(the_person, position = "cowgirl")
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(50)
        "You slowly open your eyes and discover [the_person.possessive_title] is on top of you, riding your cock."
        the_person "Oh thank god you're awake. I swear you were poking me all night long! I kept hoping you would just stick it in, but I think you were sleeping."
        the_person "I couldn't take it anymore. I hope you don't mind!"
        "[the_person.title]'s epic tits are bouncing up and down right in front of you as she rides you."
        mc.name "Definitely. Ride me good!"
        # call fuck_person(the_person, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, girl_in_charge = True) from _sarah_cowgirl_wakeup_overnight_1
        call get_fucked(the_person, the_goal = "vaginal creampie", private= True, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, allow_continue = True) from _call_get_fucked_sarah_cowgirl_wakeup_overnight_1
        $ the_report = _return
        if the_report.get("girl orgasms", 0) > 0:
            $ the_person.change_love(5)
            the_person "Oh wow I came so hard [the_person.mc_title]."
            "She rolls over and kisses you, then rests her head on your chest."
            $ mc.change_locked_clarity(10)

        "You lay in bed together for a little longer, but soon it is time to start the day."
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand4")
        "You both get ready for the day."
        the_person "Alright, I need to get some things done today. Thanks for letting me spend the night!"
        $ scene_manager.remove_actor(the_person)

    $ scene_manager.clear_scene()
    return "Advance Time"

label watch_strip_show(the_person):  #This scene assumes scene manager is running and the_person is with you, so she won't strip for you.
    $ showgirl = get_random_from_list(stripclub_strippers)
    $ showgirl.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    "You watch as a girl gets on stage and starts to do her routine."
    $ scene_manager.add_actor(showgirl, display_transform = character_left_flipped)
    if showgirl is cousin:
        if showgirl.event_triggers_dict.get("blackmail_level",-1) < 2 and cousin.has_role(stripper_role) and not showgirl.event_triggers_dict.get("seen_cousin_stripping",False):
            $ add_cousin_blackmail_2_confront_action()
            "It takes you a moment to recognize your cousin, [showgirl.title], as she struts out onto the stage."
            if not showgirl.event_triggers_dict.get("found_stripping_clue", False):
                "[showgirl.possessive_title]'s late nights and secret keeping suddenly make a lot more sense."

            "With the glare of the stage lights it's likely she won't be able to see who you are, but you can talk to her later and use this as leverage to blackmail her."
    $ finished = True
    $ finished_chance = 0
    python:
        for x in __builtin__.range(6):
            scene_manager.update_actor(showgirl, position = get_random_from_list(sarah_strip_pose_list))
            if renpy.random.randint(0,100) <76: #Take something off
                showgirl.outfit.remove_random_any(top_layer_first = True)
            if renpy.random.randint(0,100) < finished_chance:
                finished = False
            else:
                finished_chance += 5
                renpy.pause(1)
    if showgirl.vagina_visible:
        "As she finishes, the showgirl gives one more pose, showing off her exposed ass to the crowd."
        $ scene_manager.update_actor(showgirl, position = "standing_doggy")
    elif showgirl.tits_visible:
        "As she finishes, the showgirl gives one more pose, showing off her exposed tits to the crowd."
        $ scene_manager.update_actor(showgirl, position = "kneeling1")
    else:
        "As she finishes, the showgirl gives one more pose, to the enjoyment of everyone in the crowd."
        $ scene_manager.update_actor(showgirl, position = get_random_from_list(sarah_strip_pose_list))
    $ scene_manager.update_actor(showgirl, position = "walking_away")
    "After finishing, the showgirl grabs her tips then exits the stage."
    $ scene_manager.remove_actor(showgirl)
    return showgirl

label play_darts_301(the_person, focus_mod = 0): #Label returns true if mc wins, false if the_person wins
    $ mc_score = 301
    $ p2_score = 301
    $ scene_manager.show_actor(the_person, position = "walking_away")
    "[the_person.title] steps to the line and prepares to throw her first set of darts."
    while (mc_score != 0) and (p2_score != 0):
        "It's [the_person.title]'s turn."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] begins to throw her darts."

        #First Dart
        if p2_score > 49:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        elif p2_score > 19:
            $ p2_score -= roll_dart_odds(target = 20, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

            #Second Dart
        if p2_score > 50:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score < 0:
            pass
            #TODO BUST
        elif p2_score == 0:
            pass
            #TODO SHE WINS
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

            #Third Dart
        if p2_score > 50:
            $ p2_score -= roll_dart_odds(target = 50, focus_score = (the_person.focus + focus_mod))
        elif p2_score < 0:
            pass
            #TODO BUST
        elif p2_score == 0:
            pass
            #TODO SHE WINS
        elif p2_score > 24:
            $ p2_score -= roll_dart_odds(target = 25, focus_score = (the_person.focus + focus_mod))
        else:
            $ p2_score -= roll_dart_odds(target = p2_score, focus_score = (the_person.focus + focus_mod))

        "[the_person.title] score: [p2_score]"
        if p2_score == 0:
            "[the_person.title] wins the game!"
            $ scene_manager.hide_actor(the_person)
            return False
        elif p2_score < 0:
            "[the_person.title] busts! Her score is reset to 101!"
            $ p2_score = 101
        $ scene_manager.update_actor(the_person)
        the_person "Okay, [the_person.mc_title]. Your turn!"
        "Your score: [mc_score], what would you like to target?"
        menu:
            "Bullseye (50)" if mc_score > 49:
                $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                pass
            "Bullseye (50)" if mc_score < 50:
                "You decide to try and bust on purpose."
                $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
            "Outer Ring (25)" if mc_score > 24:
                $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                pass
            "Outer Ring (25)" if mc_score < 25:
                "You decide to try and bust on purpose."
                $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
            "20" if mc_score > 20:
                $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                pass
            "[mc_score]" if mc_score < 21:
                "This is it, you're going for the win!"
                $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)

        if mc_score > 0:
            "Now for your second dart. Your score: [mc_score], what would you like to target?"
            menu:
                "Bullseye (50)" if mc_score > 49:
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                    pass
                "Bullseye (50)" if mc_score < 50:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                "Outer Ring (25)" if mc_score > 24:
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                    pass
                "Outer Ring (25)" if mc_score < 25:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                "20" if mc_score > 20:
                    $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                    pass
                "[mc_score]" if mc_score < 21:
                    "This is it, you're going for the win!"
                    $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)

        if mc_score > 0:
            "Now for your third dart. Your score: [mc_score], what would you like to target?"
            menu:
                "Bullseye (50)" if mc_score > 49:
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                    pass
                "Bullseye (50)" if mc_score < 50:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 50, focus_score = mc.focus)
                "Outer Ring (25)" if mc_score > 24:
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                    pass
                "Outer Ring (25)" if mc_score < 25:
                    "You decide to try and bust on purpose."
                    $ mc_score -= roll_dart_odds(target = 25, focus_score = mc.focus)
                "20" if mc_score > 20:
                    $ mc_score -= roll_dart_odds(target = 20, focus_score = mc.focus)
                    pass
                "[mc_score]" if mc_score < 21:
                    "This is it, you're going for the win!"
                    $ mc_score -= roll_dart_odds(target = mc_score, focus_score = mc.focus)
        if mc_score == 0: #MC wins!
            "You win the game of darts!"
            $ scene_manager.hide_actor(the_person)
            return True
        elif mc_score < 0:
            "You bust! Your score is reset to 101."
            $ mc_score = 101
    $ scene_manager.hide_actor(the_person)
    return False

label Sarah_weekend_date_grab_drinks_label():
    $ the_person = sarah
    $ scene_manager = Scene()
    $ mc.change_location(downtown_bar)
    $ scene_manager.add_actor(the_person, emotion = "happy")
    $ intoxication_level = 0 #Start at 0, options may open up depending on how drunk you get her.
    "After a short walk, you arrive at the bar that you and [the_person.title] have been to a few times recently."
    the_person "Oh! I think I see a booth over there."
    mc.name "Perfect, go grab it while I get the first round."
    "You wander over to the bar and buy drinks for you and [the_person.possessive_title]. You make sure to get her favorite, the appletini."
    $ mc.business.change_funds(-20)
    "If you wanted to, now would be a good time to slip a serum into her drink..."
    menu:
        "Slip in a serum":
            "After you get the drinks, you carefully add a serum to it."
            call give_serum(the_person) from _call_give_sarah_serum_005
        "Leave alone":
            "You decide to leave her drink alone."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You join [the_person.title] at the booth and begin to enjoy your drinks together."
    "You spend some time, shooting the breeze and enjoying each other's company."
    "After a while the drinks are empty. You consider what to do next."
    $ intoxication_level += 1
    $ loop_count = 0
    while loop_count < 5: #Limited number of rounds available
        $ chance_service_him = the_person.sluttiness + ((the_person.obedience - 100) / 4 ) + (mc.charisma * 4) + (intoxication_level * 4)
        if chance_service_him > 100:
            $ chance_service_him = 100
        elif chance_service_him < 0:
            $ chance_service_him = 0
        menu:
            "Have another round" if intoxication_level < 7:
                mc.name "Wow, drinks are empty already. Another round?"
                the_person "Hell yeah!"
                if renpy.random.randint(0,100) < 35:  #She offers to buy a round once in a while
                    the_person "Tell you what, let me pick up this round. It's only fair!"
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    "[the_person.possessive_title] jumps up and walks away. You admire her figure as she makes her way over to the bartender."
                    "After a short time, she returns with the drinks and sits down."
                    $ scene_manager.update_actor(the_person, position = "sitting")
                else:
                    "You wander over to the bar and buy drinks for you and [the_person.possessive_title]. You make sure to get her favorite, the appletini."
                    $ mc.business.change_funds(-20)
                    "You come back to the booth with the drinks."
                    the_person "Yum! Thank you!"
                "You sit with [the_person.title], enjoying your drinks while chatting."
                call Sarah_get_drunk_dialogue(the_person, intoxication_level) from sarah_drunk_dialogue_01 #found in personality file
                $ intoxication_level += 2
                "After a while the drinks are empty. You consider what to do next."
            "Play some darts":
                mc.name "How about a round of darts?"
                the_person "Hell yeah!"
                "You walk over to the dart boards and get ready to have a game."
                call play_darts_301(the_person, focus_mod = -intoxication_level) from play_darts_301_call_date_night_1
                if _return:
                    $ scene_manager.show_actor(the_person, emotion = "sad")
                    "[the_person.title] gives you a pathetically fake pout after you win your game of darts."
                    the_person "Damn you're good at that!"
                    $ the_person.change_obedience(5)
                else:
                    $ scene_manager.show_actor(the_person, emotion = "happy")
                    "[the_person.title] gives you a huge smile after winning your game of darts!"
                    the_person "Ha! In your face!"
                    $ the_person.change_happiness(5)
                $ intoxication_level += -1

            "Propose sex in the bathroom\n{color=#ff0000}{size=18}Success Chance: [chance_service_him]%%{/size}{/color}" if intoxication_level > 10: #TODO this option currently disabled while it is being written (10 is impossible)
                "You lean in close and whisper to her."
                mc.name "Why don't we take a break from the drinking and sneak back to the restroom and do something a little more... physical."
                the_person "Oh my..."
                if renpy.random.randint(0,100) < chance_service_him: #Success
                    the_person "That sounds hot... okay! Let's do it!"
                    call Sarah_sex_in_the_bar_restroom_label(the_person) from sarah_seduction_public_restroom_1
                else:
                    the_person "I'm sorry... the restrooms are always so dirty... why don't we just get out of here?"
                $ loop_count += 5
            "Get outta here":
                $ loop_count += 5


        $ loop_count += 1
    "You step out of the bar with [the_person.title]. You can tell she is hesitant to part ways with you already."
    if intoxication_level < 5:
        the_person "So... how about I walk you back to your place?"
    else:
        the_person "Sooooo, listen here. I had such a great time tonight. Why don't we go back to your place and mess around a bit?"
        "Her slurred speech makes you chuckle."
    menu:
        "Back to your place":
            pass
        "Part ways for tonight":
            mc.name "I had a great time tonight, but I'm afraid we need to part ways for now."
            if intoxication_level < 5:
                the_person "Ah, okay. Well have a good night. I think I'm gonna grab a taxi home tonight!"
            else:
                the_person "Damn, that's cold! Fine... but do you think you could call me a taxi? I'm not sure I'm good to walk home..."
                "You call up a local taxi company, soon one is on the way."
            "You stay out front of the bar with [the_person.title] until her cab arrives. You say goodnight and soon the cab is driving off."
            return "Advance Time"

    mc.name "My place sounds great. Let's go!"
    "A short walk later, and you are walking through your front door."
    call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_01
    $ scene_manager.clear_scene()
    return

label Sarah_sex_in_the_bar_restroom_label(the_person):
    #TODO this function
    "This option currently being written."

    return

label Sarah_weekend_date_strip_club_label():
    $ the_person = sarah
    $ scene_manager = Scene()
    $ mc.change_location(strip_club)
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "After a short walk, you and [the_person.possessive_title] enter the front door of the now familiar strip club."
    "Your senses are assaulted by everything going on. The loud bass music thumps in your ears. On stage you see a girl shaking her ass for a group of guys."
    "You notice several guys checking out [the_person.title] as you find a secluded booth and sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "You sit down across from [the_person.possessive_title]."
    "The sights, sounds, and smells of a strip club. There's really nothing quite like it."
    "You consider what you would like to do first."
    $ loop_count = 0
    while loop_count < 5: #Limited number of rounds available
        menu:
            "Watch a dance":
                "You and [the_person.title] chat for a bit until the lights in the room dim in preparation for the next girl's show."
                call watch_strip_show(the_person) from weekend_date_strip_club_strip_call_01
                $ mc.change_locked_clarity(50)
                the_person "Ugh, the girls they have working here are so hot."
                $ the_person.change_arousal(renpy.random.randint(5,15))
                $ mc.change_arousal(renpy.random.randint(5,15))
                $ showgirl = None
            "Get a private dance\n{color=#ff0000}{size=18}Costs: $200{/size}{/color}" if mc.business.has_funds(200):
                mc.name "Want to get a private dance? I'll get it set up."
                the_person "Ohh, now we're talking! Sounds great!"
                $ scene_manager.hide_actor(the_person)
                call Sarah_date_strip_club_private_dance_label(the_person) from weekend_date_strip_club_strip_dance_01
                pass
            "Get outta here":
                $ loop_count += 5
        if the_person.arousal_perc >= 70:
            the_person "Hey, so... don't you think it's about time for us to get outta here? I'm not sure I can take much more teasing!"
            $ loop_count += 5
            mc.name "Good idea..."

    "You step out of the strip club with [the_person.title]. You can tell she is hesitant to part ways with you already."
    if the_person.arousal_perc < 70:
        the_person "That was fun! Can we go back to your place now?"
    else:
        the_person "That was hot. I'm am SO worked up. Can we please go back to your place now?"
    menu:
        "Back to your place":
            mc.name "My place sounds great. Let's go!"
            "A short walk later, and you are walking through your front door."
            call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_03
        "Part ways for tonight":
            mc.name "I had a great time tonight, but I'm afraid we need to part ways for now."
            the_person "Damn, that's cold! Fine... I'll grab a taxi. Your loss!"
            "You stay out front of the strip club with [the_person.title] until her cab arrives. You say goodnight and soon the cab is driving off."
        "Wait for [cousin.title]" if willing_to_threesome(sarah, cousin):
            "Sorry! This isn't written yet. You decide to not wait for her and just head back to your place."
            call Sarah_date_ends_at_your_place_label(the_person) from sarah_date_happy_ending_03b
    $ scene_manager.clear_scene()
    return

label Sarah_naomi_reconciliation_label(the_person):
    if not sarah.is_employee: # quick exit if she no longer works here
        return

    python:
        so_title = SO_relationship_to_title(the_person.relationship)
        so_name = the_person.SO_name
        the_person.SO_name = None
        the_person.relationship = "Single"
        # bring her back into the game
        the_person.set_override_schedule(None) # make Naomi free-roam

    "As you are walking around, you suddenly hear a familiar voice calling you."
    the_person "Hey [the_person.mc_title], is that you?"
    $ the_person.draw_person()
    mc.name "Hello [the_person.title], long time no see. How are you these days?"
    $ the_person.draw_person(emotion = "sad")
    if so_title == "Married":
        the_person "To be honest, not so good. I recently divorced [so_name]."
    else:
        the_person "To be honest, not so good. I recently broke up with my [so_title] [so_name]."
    the_person "It seems we weren't as compatible as I thought."
    the_person "If you don't mind me asking, are you still seeing [sarah.fname]?"
    mc.name "Of course, she's one of my best employees."
    the_person "I would like to apologize to her, she's always been a good friend and we didn't part on the best terms last time..."
    mc.name "I remember, you were a real bitch the last time."
    the_person "I know and I'm really sorry about that. I shouldn't have said what I did, I guess I let [so_name] influence me too much."
    mc.name "You know what, I will see what I can do for you, but first I need to talk this over with [sarah.fname]."
    $ the_person.draw_person(emotion = "happy")
    the_person "That would be awesome, I don't know how I could ever repay you."
    "You got a few ideas for that and you doubt she is going to like them."
    if mc.phone.has_number(the_person):
        mc.name "Don't worry about it, I'll give you a call soon."
        the_person "Thanks again, talk to you soon."
    else:
        mc.name "Don't worry about it, just give me your phone number and I'll give you a call soon."
        $ mc.phone.register_number(the_person)
        the_person "Here you are, thanks again and talk to you soon."
    $ the_person.draw_person(position = "walking_away")
    "You should talk to [sarah.possessive_title] to give her a heads-up and discuss what just happened."
    $ clear_scene()
    $ add_talk_to_sarah_about_naomi_action()
    return

label Sarah_talk_about_naomi_label(the_person):
    $ the_person.draw_person()
    mc.name "Hey [the_person.title], can we have a talk in my office?"
    the_person "I'm not in trouble, am I?"
    mc.name "Don't worry, it's personal."
    the_person "Ok, let's go then."
    $ mc.change_location(ceo_office)
    "You gesture [the_person.possessive_title] to sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "Guess who I bumped into the other day..."
    the_person "No clue, come on tell me..."
    mc.name "Your old friend [naomi.name]."
    "[sarah.fname] looks at you for a few seconds..."
    the_person "Okay, why should I care?"
    mc.name "Well, she wants to get back in touch with you, she's sorry about what happened last time."
    "She is still skeptical, what do you want to propose to her?"
    menu:
        "Get some revenge":
            mc.name "I think she deserves a little punishment for how she treated you last time."
            $ the_person.draw_person(position = "sitting", emotion = "happy")
            the_person "Yeah, I agree, she needs to be put in her place."
            mc.name "And since she's single again, we could make this a little more interesting for you."
            the_person "Oh, you little devil, what are you planning?"
            mc.name "Don't worry about that, do you trust me? I promise you will love it."
            the_person "Darn, now you made me really curious, but I will let you surprise me."
            mc.name "Perfect, now get back to work, you little slacker."
            $ the_person.draw_person(position = "back_peek")
            "With that she stands up and leaves your office, looking back to give you a wink."
            $ clear_scene()
            "Now let's invite [naomi.name] over to give her the 'good' news."
            $ mc.start_text_convo(naomi)
            mc.name "Good news, I talked it over with [the_person.fname]."
            mc.name "Can you come to my business next Wednesday afternoon?"
            naomi "That's just wonderful, I'll be there."
            $ mc.end_text_convo()
            $ add_naomi_visits_to_apologize_action()
            "The stage is set and you can execute your plan next Wednesday."
        "Be friends again\n{color=ff0000}{size=18}Not written yet{/size}{/color} (disabled)":
            pass
        "Nothing":
            mc.name "Looking at how she treated you, I would keep away from her."
            the_person "Yeah, I agree, I don't need her in my life. Things are just fine. Thanks for telling me though."
            mc.name "No problem, now back to work."
            $ the_person.draw_person(position = "walking_away")
            "With that she stands up and leaves your office."
            $ clear_scene()
    return

label Sarah_naomi_visits_to_apologize_label():
    if not sarah.is_employee: # quick exit if she no longer works here
        return

    "It's Wednesday afternoon and Naomi is visiting, so you go down to the lobby to pick her up."
    python:
        the_person = naomi
        scene_manager = Scene()
        mc.change_location(lobby)
        scene_manager.add_actor(the_person)
    the_person "Hello [the_person.mc_title], thank you again for doing this for me."
    mc.name "Hi [the_person.fname], good to see you, let's go to my office."
    $ mc.change_location(ceo_office)
    $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_center_flipped)
    "You motion her to take a seat."
    mc.name "Would you like some coffee?"
    the_person "Yes, [the_person.coffee_style], please."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        "You pour some of your serum enhanced coffee, to make her a little more open to suggestion."
    else:
        "Your pour some coffee and place the cup before her on the desk."
    mc.name "Right, since we are all set, shall I call in [sarah.fname]?"
    the_person "Perfect, I have been thinking about what to say for a few days now."
    "You make a quick call to [sarah.possessive_title] and wait until she knocks on your door, all the while [the_person.fname] is sipping on her coffee."
    $ scene_manager.add_actor(sarah, display_transform = character_right)
    sarah "Good afternoon, [sarah.mc_title]."
    if sarah_epic_tits_progress() > 1:
        the_person "Oh my god, [sarah.fname] you look absolutely stunning, your breasts... they are... amazing."
        $ the_person.change_arousal(10)
        $ scene_manager.update_actor(sarah, emotion = "happy")
    else:
        the_person "Hello [sarah.fname], it's good to see you, you look great."
    "Before you have any chance to say anything, [the_person.fname], starts apologizing to [sarah.possessive_title]."
    the_person "I'm so sorry, for the last time, you are my best friend, you were always there for me, I shouldn't have listened to that shit bag..."
    "During her rambling, [sarah.possessive_title] sits down, without saying a word."
    $ scene_manager.update_actor(sarah, position = "sitting", emotion = "default")
    mc.name "SILENCE !!"
    "[the_person.fname] stops rambling and both girls look at you."
    mc.name "We are not here to listen to you babbling, [sarah.fname] is here for an apology."
    mc.name "So it's time we get to it, I think [the_person.fname] deserves a good spanking, don't you agree [sarah.title]?"
    $ scene_manager.update_actor(sarah, emotion = "happy")
    "For a second [the_person.fname] looks dumbfounded, but [sarah.title] starts to smile and nods to you."
    mc.name "Good, I thought you both would agree, [the_person.fname] please stand and lean over my desk."
    the_person "I... but... well..."
    $ scene_manager.update_actor(the_person, position = "standing_doggy", display_transform = character_center)
    mc.name "Right, [sarah.title], I think it would be only fair if you did the spanking."
    "[sarah.possessive_title] finally seems to figure out where you are going and leans into the role."
    $ scene_manager.update_actor(sarah, position = "stand4", emotion = "default")
    if not the_person.vagina_visible:
        sarah "Right, this won't do at all [the_person.fname], a good spanking is done on a bare butt, show it to me."
        "[the_person.fname] looks at you and only sees you nodding, reluctantly she moves her clothes out of the way."
        $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = False)
    $ the_person.change_arousal(15)
    $ sarah.change_arousal(15)
    sarah "Good, I see you are committed to apologizing."
    $ scene_manager.update_actor(sarah, position = "stand5")
    "And with that [sarah.possessive_title] starts slapping away at [the_person.fname]'s naked ass cheeks."
    $ spank_factor_increment(the_person)
    the_person "Oh shit!... Fuck!... Aaarg!"
    sarah "Now you little bitch, tell me how sorry you are!"
    the_person "Aaah... I'm... shit... really... Ouch... SORRY!!"
    $ spank_factor_increment(the_person)
    mc.name "I don't think she's really sorry yet [sarah.fname]."
    sarah "I agree, [sarah.mc_title]."
    while the_person.event_triggers_dict.get("spank_level", 0) < 6:
        $ spank_factor_increment(the_person)
        $ ran_num = renpy.random.randint(0,2)
        if ran_num == 0:
            the_person "Oh... I'm sorry [sarah.fname]! Oh god..."
            "She keeps her ass still, taking [sarah.possessive_title]'s punishment with pride."
        elif ran_num == 1:
            the_person "Please... ah... fuck... [sarah.fname], please... ouch..."
        else:
            "[sarah.possessive_title] keeps slapping her old friends ass like there is no tomorrow."

        if the_person.event_triggers_dict.get("spank_level", 0) % 2 == 1:
            $ ass_desc = spanking_get_ass_description(the_person)
            "You look down at [the_person.fname]'s ass. It is [ass_desc]"

        if the_person.event_triggers_dict.get("spank_level", 0) < 6:
            mc.name "Just keep going, there is some room for improvement"
            if the_person.event_triggers_dict.get("spank_level", 0) > 4:
                "As you are watching this scene you see [the_person.fname]'s [the_person.pubes_description] pussy seems to get wet also."
        else:
            mc.name "I think that should be enough."

    "How to continue?"
    menu:
        "Degrade [the_person.title]":
            mc.name "Hey [sarah.title], I think she is ready to make some further amends."
            sarah "What did you have in mind, Sir?"
            mc.name "Why don't you take a seat."
            $ scene_manager.update_actor(sarah, position = "sitting")
            mc.name "Well [the_person.fname], did you know that [sarah.fname] had a girl crush on you since you met?"
            $ scene_manager.update_actor(the_person, position = "stand2")
            the_person "Oh... I didn't know that, is that why you were so angry with me after that night? Because my ex didn't let you join us?"
            $ the_person.change_arousal(10)
            "[sarah.possessive_title] looks at her and quietly nods."
            mc.name "[sarah.title], why don't you show her how wet your little snatch is..."
            $ scene_manager.update_actor(sarah, position = "missionary", display_transform = Threesome_doggy_deluxe_girl_one_transform, z_order = 0)
            if not sarah.vagina_visible:
                $ scene_manager.strip_to_vagina(sarah, visible_enough = True, prefer_half_off = True)
            $ sarah.change_arousal(10)
            "As [sarah.possessive_title] lays back in her chair she reveals her already slick snatch to her friend."
            mc.name "[the_person.fname], why don't you show her how much you value her friendship, by making her cum with your tongue."
            if not sarah.tits_visible and sarah_epic_tits_progress() > 1:
                the_person "Could I also see your magnificent breasts, they just look amazing as far as I can tell."
                "[sarah.possessive_title] smiles and reveals her new boobs."
                $ scene_manager.strip_to_tits(sarah, visible_enough = True, prefer_half_off = True)
                $ the_person.change_arousal(15)
                the_person "Oh my, they look truly amazing, you have to give me the number of your doctor."
                $ scene_manager.update_actor(sarah, emotion = "happy")
                "[sarah.possessive_title] looks up at you and gives you a big smile and a wink."
                mc.name "Well, get down to business [the_person.title]."
            $ scene_manager.update_actor(the_person, position = "doggy" , display_transform = Threesome_doggy_deluxe_girl_two_transform, z_order = 1)
            $ sarah.change_arousal(20)
            "[the_person.fname] moves between her friend's legs, and slowly starts licking her [sarah.pubes_description] fold."
            sarah "Oh yes, right there, sweety."
            "While [the_person.fname] is doing her best to satisfy [sarah.possessive_title], you position yourself right behind her."
            mc.name "I think she needs some extra motivation, don't you agree [sarah.title]?"
            "[sarah.possessive_title] is only able to nod while enjoying the tongue of her friend. And with that you continue the spanking of [the_person.fname]."
            the_person "*SLAP*... Aargh... *SLAP*... hmm... *SLAP*... MMM..."
            $ the_person.change_arousal(20)
            $ sarah.change_arousal(20)
            "Occasionally, you move your hands between her legs to check how wet she is, and she's getting wetter by the minute."
            $ the_person.change_arousal(20)
            $ sarah.change_arousal(20)
            "[sarah.possessive_title] is close to orgasm, judging by her groans getting louder and louder."
            $ the_person.change_arousal(30)
            $ sarah.change_arousal(30)
            sarah "Oh yes, right there [the_person.fname], make me cum... Oh God, YES, I'm CUMMING!!!"
            $ sarah.have_orgasm()
            "As [sarah.possessive_title] starts squirting, her friend starts to shudder indicating that she's having an orgasm as well."
            $ the_person.have_orgasm()
            the_person "MMMM!!!... Oh my, this is so good, I never thought you could taste this good."
            $ sarah.increase_opinion_score("getting head", 2)
            sarah "You really know you way around down there, I came like a freight train."
            "After [the_person.fname] gives [sarah.possessive_title] a few more licks along her dripping slit, she stands up."
            $ the_person.increase_opinion_score("being submissive", 1)
            $ scene_manager.update_actor(sarah, position = "sitting", display_transform = character_right)
            $ scene_manager.update_actor(the_person, position = "stand4", display_transform = character_center_flipped)
            the_person "I'm really happy I was able to do this for you [sarah.fname], friends?"

        "End the punishment":
            mc.name "Right, that will be enough for now."
            sarah "Ah, well, if you think so [sarah.mc_title]."
            $ the_person.increase_opinion_score("being submissive", 1)
            $ scene_manager.update_actor(sarah, position = "sitting")
            $ scene_manager.update_actor(the_person, position = "stand4")
            the_person "Do you think we could be friends again, [sarah.fname]?"

    "You look at [sarah.possessive_title], so she knows it's her decision."
    sarah "Very well, let's consider this a friendship on trial basis and see where it goes from here."
    the_person "Thats all I ever wanted."
    if sarah.vagina_visible:
        "The girls rearrange their outfits."
    else:
        "[the_person.fname] puts her clothes in order."
    $ scene_manager.apply_outfits()
    the_person "Why don't you give me a tour of this place [sarah.fname]?"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She grabs [sarah.possessive_title] by the hand and drags her out of your office."
    $ scene_manager.update_actor(sarah, position = "walking_away")
    "It seems they are off to a good start, let's see where this relationship goes in the future."
    $ scene_manager.clear_scene()

    # TODO: add bar date with Sarah and Naomi, where you end up at Sarah's place for a night of fun
    return

label Sarah_date_ends_at_your_place_label(the_person):
    $ mc.change_location(hall)
    $ scene_manager.update_actor(the_person, position = "stand2", display_transform = character_right)
    if the_person.is_highly_fertile:
        the_person "Oh god, I can't wait to feel you fill me up again..."
    else:
        the_person "Oh god, I can't wait to feel your hands all over me again..."
    $ scene_manager.add_actor(mom, display_transform = character_left_flipped)
    "[mom.title] pops around the corner when she hears you walking down the hall and unknowingly interrupts."
    mom "Ah! It's [the_person.fname] again!"
    "[mom.possessive_title] raises her arms and gives [the_person.title] a hug."
    $ scene_manager.update_actor(the_person, position = "kissing")
    $ scene_manager.update_actor(mom, position = "walking_away", display_transform = character_right)
    if mom.sluttiness > 40:
        "[mom.possessive_title] embraces her warmly. In fact it seems to be going on for quite some time..."
        if mom.sluttiness > 80 and the_person.sluttiness > 80:
            the_person "Mmmmm..."
            "You hear the soft sound of lips smacking each other... wait are they kissing?"
            $ mc.change_locked_clarity(30)
            "... yep... they are definitely kissing. Damn this is hot."
        elif the_person.sluttiness < 40:
            the_person "Awww. Hello [mom.fname]. I was just coming over to spend some quality time with [the_person.mc_title]."
    "Eventually they back away from each other."
    $ scene_manager.update_actor(mom, position = "stand4", display_transform = character_left_flipped)
    $ scene_manager.update_actor(the_person, position = "stand2")
    mom "Alright, well don't let me keep you. You two have fun!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.possessive_title] walks away, chuckling to herself."
    $ scene_manager.remove_actor(mom)

    $ mc.change_location(bedroom)

    "You reach your bedroom and quickly close and lock the door."
    "[the_person.possessive_title] looks at you."
    the_person "Well, I think we both know where this is going!"
    $ scene_manager.strip_full_outfit(person = the_person)
    $ skip_condom = False
    if the_person.is_highly_fertile:
        the_person "Let's go! Ovulation is driving me crazy, I've been daydreaming about your cock filling me with seed all night long!"
        $ skip_condom = True
    else:
        the_person "What are you staring at? Let's go! I've been looking forward to this all night!"
    call fuck_person(the_person, skip_intro = False, skip_condom = skip_condom, girl_in_charge = False) from _call_sex_description_date_happy_ending_1
    "When you finish with her, [the_person.title] collapses in the bed."
    $ scene_manager.update_actor(the_person, position = "missionary")
    "You cuddle up next to her as you both catch your breath."
    if the_person.has_role(girlfriend_role):  #You are already dating her via other means. She just cuddles up with you.
        "As you both recover, [the_person.possessive_title] starts kissing you along your neck, then whispers in your ear."
        the_person "Thank you for the good time tonight. I love you."
        mc.name "I love you too."
        the_person "Do you care if I just stay here tonight? I umm... actually brought my toothbrush..."
        mc.name "Of course! I wouldn't have it any other way!"
        $ the_person.change_love(5)
        $ scene_manager.strip_full_outfit(person = the_person, strip_feet = True)
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "Worn out from your romp with [the_person.possessive_title], you cuddle up with her and quickly fall asleep."
        call Sarah_spend_the_night() from sarah_date_night_happy_ending_gf_path
    elif the_person.has_role(affair_role):
        the_person "It feels so good to be next to you, but I need to get home."
        mc.name "You don't have to. Just spend the night here."
        the_person "I'm sorry I can't. You know I can't. Thanks for the offer though!"
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
        return "Advance Time"
    else:
        the_person "I need to get going... I guess. Thanks for the evening though. It was great!"
        mc.name "You don't have to. Just spend the night here."
        the_person "That's tempting, believe me, but I need to get home. Thanks for the offer!"
        $ the_person.apply_planned_outfit()
        $ scene_manager.update_actor(the_person, position = "stand3")
        "You lay on your bed and watch as [the_person.possessive_title] slowly gets her clothes on. She says goodbye then lets herself out."
        return "Advance Time"
    return

label Sarah_date_strip_club_private_dance_label(the_person):
    $ showgirl_1 = get_random_from_list([x for x in stripclub_strippers if x not in [cousin]])
    $ showgirl_2 = get_random_from_list([x for x in stripclub_strippers if x not in [showgirl_1, cousin]])
    if get_strip_club_foreclosed_stage() < 5:
        "You get up and head over to the counter where the owner is."
    else:
        "You get up and head over to the counter and talk with the manager."
    "You look through the list of girls available for private dances."
    if cousin.event_triggers_dict.get("blackmail_level", -1) >= 2 and cousin.has_role(stripper_role):
        "You spot your cousin on the list. You could ask for her to dance for either you or [the_person.possessive_title]..."
        menu:
            "Dance for [the_person.title]":
                $ showgirl_1 = cousin
                "You just can't pass up an opportunity to have [cousin.possessive_title] dance for [the_person.title]. You arrange for her to be her private dancer."
            "Dance for you":
                $ showgirl_2 = cousin
                "You just can't pass up an opportunity to have [cousin.possessive_title]'s huge tits in your face. You arrange for her to be your private dancer."
            "Don't ask for her":
                "You decide not to bring [cousin.possessive_title] into the private dance this time."
    else:
        "You don't really care too much about who does the dance, so you pick a couple random girls."

    $ mc.business.change_funds(-200)
    "You go to the back, and find a room with two chairs facing each other. [the_person.title] sits across from you."
    $ scene_manager.show_actor(the_person, position = "sitting", emotion = "happy", display_transform = character_left_flipped)
    the_person "Mmm, I'm so nervous..."
    #TODO make a variant on character left that is a close to Sarah so it looks more like an actual lap dance.
    $ showgirl_1.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_1, display_transform = character_center_flipped)

    $ showgirl_2.apply_outfit(stripclub_wardrobe.pick_random_outfit())
    $ scene_manager.add_actor(showgirl_2)
    showgirl_2 "Alright! We got a couple in here tonight, this should be fun!"
    if showgirl_2 is cousin:
        "Suddenly, [showgirl_2.title] realizes she is getting ready to dance for you."
        "[showgirl_2.possessive_title] lowers her face to your ear and whispers in it."
        showgirl_2 "Wow, you have your slut here, with you, but you want MY tits in your face? You're a sick fuck."
        $ mc.change_locked_clarity(30)
        "She stands back up and winks at you, then acts as if nothing happened."
    if showgirl_1 is cousin:
        "You see [showgirl_1.title] looking over to you, realizing that you are gonna be in the room as she performs for [the_person.title]."
        "She gives you a quick wink."
        $ mc.change_locked_clarity(10)
    showgirl_1 "Alright, let's get the fun started!"
    $ scene_manager.update_actor(showgirl_2, position = "kneeling1")
    "Your stripper gets on your lap. She starts to take off her top."
    $ scene_manager.strip_to_tits(person = showgirl_2)
    "With her tits free, she begins to gyrate them back and forth, right in front of your face. They wobble appealingly."
    $ mc.change_locked_clarity(30)
    $ scene_manager.update_actor(showgirl_1, position = "blowjob")
    "You glance over and notice the girl in front of [the_person.title] is doing something similar."
    $ scene_manager.strip_to_tits(person = showgirl_1)
    showgirl_2 "For $100, you two can play with our tits for a bit."
    if showgirl_2 is cousin:
        "[showgirl_2.title] lowers her lips to your ear again."
        showgirl_2 "Don't you wanna grab your cousin's tits?"
    "You see [the_person.title] look over at you. You can see her mouth the word 'please'"
    menu:
        "Pay\n{color=ff0000}{size=18}Costs: $100{/size}{/color}" if mc.business.has_funds(100):
            mc.name "That sounds fair."
            "You grab $100 and put it in the tip jar."
            $ mc.business.change_funds(-100)
            "Before you finish putting the money in the jar, you notice that [the_person.title] has her hands all over her stripper's chest."
            "She seems to be really enjoying the show so far!"
            $ mc.change_arousal(10)
            if showgirl_2 is cousin:
                "You reach up and grope [showgirl_2.possessive_title]'s tits. You're mesmerized by how soft and warm they are."
                $ mc.change_locked_clarity(40)
            else:
                "You reach up and begin to fondle your stripper's tits. They are so soft and warm. They feel amazing."
                $ mc.change_locked_clarity(30)
            $ the_person.change_arousal(15)
        "Pay\n{color=ff0000}{size=18}Requires: $100{/size}{/color} (disabled)" if not mc.business.has_funds(100):
            pass
        "Not today":
            mc.name "We're just here to watch."
            "Glancing at [the_person.title], you can tell she is a little disappointed, but she quickly returns her attention to the girl in front of her."

    "After a while, it's time to change things up. Both strippers get up and turn to so their backs are facing you and [the_person.title]."
    $ scene_manager.update_actor(showgirl_2, position = "standing_doggy")
    $ scene_manager.update_actor(showgirl_1, position = "standing_doggy")
    "Your girl puts her ass against your chest and starts to wiggle her hips back and forth as she slowly works herself down your body."
    "Soon she is working your erection with her hips, through both of your clothes."
    "She starts to strip down her remaining clothing."
    $ scene_manager.strip_full_outfit(person = showgirl_2)
    "You notice that [the_person.title] and her stripper are in a similar state."
    $ scene_manager.strip_full_outfit(person = showgirl_1)
    "Her ass bare now, you find it difficult to restrain your hands from molesting the girl in front of you."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(10)
    showgirl_2 "For $200, you two can grope and spank it!"
    menu:
        "Pay\n{color=ff0000}{size=18}Costs: $200{/size}{/color}" if mc.business.has_funds(200):
            "You don't hesitate. You grab $200 and put it in the tip jar."
            $ mc.business.change_funds(-200)
            "[the_person.title] sees you do it and immediately starts to run her hands along her girl's hips."
            if showgirl_2 is cousin:
                "You reach up and grope [showgirl_2.possessive_title]'s ass. It is firm and supple."
                $ play_spank_sound()
                "You give her cheeks a few firm spanks."
                $ mc.change_locked_clarity(50)
                if showgirl_2.sluttiness > 60:
                    "You glance over and notice that [the_person.title] is thoroughly distracted. You run your hand down [showgirl_2.possessive_title]'s ass crack and start to play with her labia."
                    "She stifles a moan. You can feel the humidity radiating from her. She is really worked up!"
                    "You push a finger in and give her cunt a few strokes. She wiggles her hips for you as you finger her briefly."
                    $ showgirl_2.change_arousal(35)
                    "[showgirl_2.title] looks back and whispers at you."
                    showgirl_2 "Maybe later you can finish this..."

            else:
                $ mc.change_locked_clarity(30)
                "You reach up and begin to fondle your stripper's ass. It is firm and supple."
                $ play_spank_sound()
                "You give her cheeks a few firm spanks."
            $ the_person.change_arousal(15)
            $ mc.change_arousal(15)
        "Pay\n{color=ff0000}{size=18}Requires: $200{/size}{/color} (disabled)" if not mc.business.has_funds(200):
            pass
        "Not today":
            mc.name "We're just here to watch."
            "Glancing at [the_person.title], you can tell she is a little disappointed, but she quickly returns her attention to the girl in front of her."

    "Soon it is time for the private dance to end."
    $ scene_manager.update_actor(showgirl_1, position = "stand4")
    $ scene_manager.update_actor(showgirl_2, position = "stand5")
    showgirl_1 "Mmm, that was fun! It's been forever since I had a female client. They always give such soft touches..."
    if showgirl_2 is cousin and showgirl_2.sluttiness > 80:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2 "That was fun... if you wait for me to get off work, we could head back to your place for some fun?"
    elif showgirl_2 is cousin:
        "[showgirl_2.possessive_title] whispers in your ear before she leaves."
        showgirl_2 "I hope your little slut doesn't realize we're related. That would be an unfortunate event, for sure..."
    "The strippers leave, leaving you and [the_person.title] alone and highly aroused."

    $ scene_manager.remove_actor(showgirl_1)
    $ scene_manager.remove_actor(showgirl_2)
    $ del showgirl_1
    $ del showgirl_2
    "You head back out to the main room and sit down at a booth."
    $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_right)
    return

label Sarah_unlock_special_tit_fuck(the_person):
    the_person "So, umm... I have a little confession to make."
    "You raise an eyebrow."
    mc.name "Oh? Go ahead then."
    the_person "Last night... I was playing with one of my special toys... pretending it was you... obviously."
    the_person "It was nice... but I just couldn't get off. I don't know why, it just wasn't feeling right."
    the_person "So I took it out, then put it, you know, between my tits..."
    "Interesting."
    the_person "I kept imagining you, fucking my tits, cumming all over me."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "Her cheeks are starting to get a little flushed."
    the_person "I actually came, without even touching myself, you know, down there."
    mc.name "Those serums have made your tits very sensitive. I think it is normal to want to explore all these new sensations you have been having."
    the_person "Yeah, of course..."
    "Absent mindedly, she reaches up with one hand and starts to play with one of her breasts."
    $ the_person.change_arousal(20)
    the_person "I can't stop thinking about it. Can I... Can I service you with them? Please?"
    mc.name "Go ahead. I want to see if your practice has been paying off."
    if the_person.tits_available:
        "With her tits already out and ready to be used, she just gives you a big smile."
    else:
        if the_person.outfit.can_half_off_to_tits():
            "[the_person.possessive_title] moves her top out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
        else:
            "[the_person.possessive_title] begins to take off her top."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_tit_strip_list(), half_off_instead = False)
        "With her tits out and ready to be used, she gives you a big smile."
    $ mc.change_locked_clarity(50)
    "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
    "She gets on her knees and gives you a couple strokes with her hand."
    $ mc.change_arousal(10)
    $ the_person.change_arousal(10)
    the_person "Oh god, here we go! Don't hold back, use me like I'm your big titted cum slut!"
    "With her hands on each side of her chest, she wraps her sizable boobs around you and begins to bounce them up and down."
    "Your cock disappears inside of her ample cleavage."
    $ sarah.update_sex_skill("Foreplay", 6)
    $ sarah.max_opinion_score("giving tit fucks")
    call fuck_person(the_person, start_position = sarah_tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _unlock_special_tit_fuck_actual_1
    "Finished, she takes a few moments to recover. You have to admit, she has refined her technique and is very good."
    $ the_person.event_triggers_dict["special_tit_fuck"] = True
    $ the_person.apply_planned_outfit()
    return

label Sarah_fertile_period_start_label():
    $ the_person = sarah
    $ the_person.event_triggers_dict["fertile_start_creampie_count"] = the_person.sex_record["Vaginal Creampies"]
    #TODO add slutty crisis events where Sarah tries to get creampies from MC
    $ add_sarah_fertile_period_end_action()
    return

label Sarah_fertile_period_end_label():
    $ the_person = sarah
    $ success_chance = the_person.sex_record["Vaginal Creampies"] - the_person.event_triggers_dict.get("fertile_start_creampie_count", the_person.sex_record["Vaginal Creampies"])
    if (success_chance * 3) >=  renpy.random.randint(0,100): #She is pregnant!
        $ add_sarah_fertile_period_end_action() #Until we write this segment, just let us have fun trying to make babies without ever actually getting pregnant.
        #TODO make her pregnant!
    else:
        $ add_sarah_fertile_period_start_action()
    return

label Sarah_titfuck_mentor_label():
    return
