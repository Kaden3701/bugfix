init 3 python:
    def lust_booty_call_intro_requirement():
        if mc.is_in_bed and mc.energy > 80 and schedule_sleepover_available():
            return len(lust_get_booty_call_list()) >= 3
        return False

    def lust_booty_call_requirement():
        if time_of_day == 4 and mc.energy > 80:
            if not schedule_sleepover_available():
                return "Sleepover scheduled"
            if mc.lust_tier <= 2:
                return "Not enough lust"
            return True
        return False

    def lust_get_booty_call_list():
        booty_call_list = []
        for person in known_people_in_the_game(excluded_people = [mom, lily, aunt, cousin]):
            if (person.is_girlfriend or person.sluttiness > 70) and person.energy > 80:
                booty_call_list.append(person)
        return booty_call_list

    def lust_booty_call_init(action_mod):
        lust_booty_call_enabled(action_mod.enabled)
        return

    def lust_booty_call_enabled(enabled):
        if enabled:
            if not mc.business.event_triggers_dict.get("lust_booty_call_unlocked", False):
                mc.business.add_mandatory_crisis(lust_booty_call_intro_action)
        else:
            mc.business.remove_mandatory_crisis("lust_booty_call_intro_label")
        return

    # extend the default build phone menu function with renovations
    def build_phone_menu_booty_call_extended(org_func):
        def phone_menu_wrapper():
            # run original function
            phone_menu = org_func()
            # run extension code
            if mc.business.event_triggers_dict.get("lust_booty_call_unlocked", False):
                lust_booty_call_action = Action("Make booty call {image=gui/heart/Time_Advance.png}", lust_booty_call_requirement, "lust_booty_call_label", menu_tooltip = "Call someone for a one time late night sexual encounter.", priority = 10)
                phone_menu[2].insert(1, lust_booty_call_action)

            return phone_menu

        return phone_menu_wrapper

    build_phone_menu = build_phone_menu_booty_call_extended(build_phone_menu)

    lust_booty_call_intro_action = ActionMod("Lust Booty Call", lust_booty_call_intro_requirement, "lust_booty_call_intro_label",
        initialization = lust_booty_call_init, on_enabled_changed = lust_booty_call_enabled,
        menu_tooltip = "You make a booty call to get laid.", category="Misc")

label lust_booty_call_intro_label():
    $ mc.change_location(bedroom)   # make sure we are in the bedroom
    "You lay down in your bed and try to go to sleep."
    "You toss and turn for a while. This is impossible! You feel like you have so much energy."
    "What you wouldn't give for a bedwarmer to play with right about now..."
    "You grab your phone. You start to open the web browser to look up some porn, but you stop yourself."
    "Instead, you open up your contacts."
    "You wonder... surely you could convince someone to come over?"
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(lust_get_booty_call_list(), "Text who?", "No one" )],
        draw_hearts_for_people = True))

    if not isinstance(_return, Person):
        "After looking at your phone contacts, you change your mind. Maybe another opportunity will present itself later."
        $ mc.business.add_mandatory_crisis(lust_booty_call_intro)
        return

    $ the_person = _return
    "You decide to text [the_person.possessive_title]."
    show screen person_info_ui(the_person)
    $ mc.start_text_convo(the_person)
    mc.name "Hey, you up?"
    the_person "Actually yeah. WYD?"
    mc.name "Thinking about you. Wanna come over?"
    if the_person.is_girlfriend:
        "You snap a quick dick pick and attach it."
        the_person "Mmmmmm. I'm always hot for you babe. I'll be right there."
    else:
        the_person "Maybe. You got something in mind?"
        "You snap a quick dick pick and attach it."
        the_person "Damn, why didn't you say you were DTF. I'll be right over."
        "You make sure she has your address."
    "You use the time to make sure your bedroom is cleaned up and ready for your booty call."
    "Soon, your phone is going off."
    the_person "I'm here."
    $ mc.end_text_convo()
    "You quickly let her in and sneak back to your room."
    $ the_person.draw_person()
    mc.name "Let's get down to business."
    "You don't waste anytime. You pick her up and throw her on your bed."
    $ the_person.draw_person(position = "missionary")
    the_person "Ah!"
    "She gives a little yelp as you jump on top of her. You start to make out, pushing yourself up against her."
    $ the_person.change_arousal(15)
    $ mc.change_arousal(15)
    "Pretty soon, you start moving her clothes out of the way."
    $ the_person.strip_to_vagina(position = "missionary", visible_enough = True, prefer_half_off = True)
    the_person "Wow, you are really into it tonight! How do you want to start?"
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True, ignore_taboo = True, private = True) from _lust_booty_call_fuck_01
    $ the_report = _return
    if the_report.get("guy orgasms", 0) == 0:
        "Frustrated, you finish up but still haven't cum."
        the_person "Sorry... I guess I'm just not feeling it tonight."
        $ the_person.change_happiness(-3)
    elif the_report.get("girl orgasms", 0) == 0:
        "Fully spent, you let yourself relax in your bed. [the_person.possessive_title] seems a little disgruntled."
        the_person "Wow, I come all the way over here, and you can't even reciprocate?"
        $ the_person.change_stats(happiness = -3, obedience = -3)
    else:
        "You and [the_person.possessive_title] take a few moments to recover, satisfied from your orgasms."
        $ the_person.change_stats(happiness = 3, obedience = 3)
    mc.name "Let me call you a cab. It's the least I can do for coming over late like this."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits on the edge of your bed."
    the_person "Okay, let's chat a little while we wait."
    "As you order a Lyft, she gets herself presentable."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "sitting")
    "You make small talk for a bit, but soon her ride is here, so you walk her to the door."
    $ hall.show_background()
    $ the_person.draw_person()
    mc.name "Thanks, [the_person.title], you were amazing."
    the_person "Anytime [the_person.mc_title], goodnight."
    $ the_person.draw_person(position = "walking_away")
    "She turns around, and hurries to her ride."
    $ clear_scene()
    $ mc.location.show_background()
    "After she leaves, you lay down on your bed."
    "The options that your business and the serums have opened up for sexual encounters is increasing what seems like daily."
    "You change the background of your phone to a picture you took during a recent sexual encounter."
    "You decide to embrace your new life of constant sexual encounters."
    $ add_lust_drip_perk()
    "You have gained a new perk! Your Clarity now slowly converts to Lust while active, maximum 200 per time slot."
    $ mc.business.event_triggers_dict["lust_booty_call_unlocked"] = True
    "You also have learned the art of the booty call. You can now select this option on your phone at night if your lust is high enough!"
    return

label lust_booty_call_label():
    if mc.is_home:
        "As you get yourself ready for bed, you can tell you have way too much sexual tension to fall asleep, so you decide to make a booty call."
    else:
        "Before you head home for the day, you can feel all the sexual tension you've built up throughout the day, so you decide to make a booty call."

    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(lust_get_booty_call_list(), "Text who?", "No one" )],
        draw_hearts_for_people = True))

    if not isinstance(_return, Person):
        "After looking at your contact list, you change your mind. Maybe another opportunity will present itself later."
        return

    $ the_person = _return
    "You decide to text [the_person.possessive_title]."
    show screen person_info_ui(the_person)
    $ mc.start_text_convo(the_person)
    mc.name "Hey, I'm bored. You DTF tonight?"
    the_person "Actually yeah. Your place?"
    mc.name "Hell yeah!"
    if the_person.is_girlfriend:
        mc.name "Can't wait to see you babe."
    else:
        "You make sure she has your address."
    if mc.is_home:
        if mc.location != bedroom:
            "You quickly go to your bedroom"
            $ mc.change_location(bedroom)
        "You use the time to make sure your bedroom is cleaned up and ready for your booty call."
        "Soon, your phone is going off."
        the_person "I'm here."
        $ mc.end_text_convo()
        "You quickly let her in and sneak back to your room."
    else:
        $ mc.end_text_convo()
        "You head home. Thankfully, the timing works out that you get home the same time [the_person.title] gets there."
        $ mc.change_location(bedroom) #Make sure we're in our bedroom.
        "You sneak into your room with her."
    $ the_person.draw_person()
    mc.name "Let's get down to business."
    "You don't waste anytime. You pick her up and throw her on your bed."
    $ the_person.draw_person(position = "missionary")
    the_person "Ah!"
    "She gives a little yelp as you jump on top of her. You start to make out, pushing yourself up against her."
    $ the_person.change_arousal(15)
    $ mc.change_arousal(15)
    "Pretty soon, you start moving her clothes out of the way."
    $ the_person.strip_to_vagina(position = "missionary", visible_enough = True, prefer_half_off = True)
    the_person "Wow, you are really into it tonight! How do you want to start?"
    call fuck_person(the_person, start_position = missionary, start_object = make_bed(), skip_intro = True, ignore_taboo = True, private = True) from _lust_booty_call_fuck_02
    $ the_report = _return
    if the_report.get("guy orgasms", 0) == 0:
        "Frustrated, you finish up but still haven't cum."
        the_person "Sorry... I guess I'm just not feeling it tonight."
        $ the_person.change_happiness(-3)

    elif the_report.get("girl orgasms", 0) == 0:
        "Fully spent, you let yourself relax in your bed. [the_person.possessive_title] seems a little disgruntled."
        the_person "Wow, I come all the way over here, and you can't even reciprocate?"
        $ the_person.change_stats(happiness = -3, obedience = -3)
    else:
        "You and [the_person.possessive_title] take a few moments to recover, satisfied from your orgasms."
        $ the_person.change_stats(happiness = 3, obedience = 3)
    mc.name "Let me call you a cab. It's the least I can do for coming over late like this."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits on the edge of your bed."
    the_person "Okay, let's chat a little while we wait."
    "As you order a Lyft, she gets herself presentable."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "sitting")
    "You make small talk for a bit, but soon her ride is here, so you walk her to the door."
    $ hall.show_background()
    $ the_person.draw_person()
    mc.name "Thanks, [the_person.title], you were amazing."
    the_person "Anytime [the_person.mc_title], goodnight."
    $ the_person.draw_person(position = "walking_away")
    "She turns around, and hurries to her ride."
    $ clear_scene()
    $ mc.location.show_background()
    "After she leaves, you lay down on your bed. It's nice having girls to come over anytime you ask like this. You quickly fall asleep."
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_booty_call_aftermath_01
    return


label lust_booty_call_unit_test():
    $ mc.free_clarity = 0
    $ mc.change_locked_clarity(1000)
    if not lust_booty_call_intro_requirement():
        "Intro requirements not met! This test may fail."
    call lust_booty_call_intro_label() from _lust_booty_unit_test_1
    $ mc.energy = mc.max_energy
    $ mc.change_locked_clarity(mc.free_clarity * 3)
    $ time_of_day = 4
    if not lust_booty_call_requirement():
        "Booty Call requirements not met! This test may fail."
    call lust_booty_call_label() from _lust_booty_unit_test_2
    "Unit test successful completion."
    return
