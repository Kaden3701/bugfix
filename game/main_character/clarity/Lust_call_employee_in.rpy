init 4 python:
    def lust_blowjob_intro_requirement():
        if mc.business.is_open_for_business: #Only trigger if people are in the office.
            if mc.is_at_work: #Check to see if the main character is at work
                if len(get_willing_lust_blowjob_girl_list()) > 2:
                    return True
        return False

    def lust_blowjob_office_requirement():
        if mc.business.is_open_for_business: #Only trigger if people are in the office.
            if mc.lust_tier > 2:
                return True
            return "Not enough Lust"
        else:
            return "Only during business hours"

    def get_willing_lust_blowjob_girl_list():
        return [x for x in mc.business.employee_list if x.is_willing(blowjob)]

    def lust_blowjob_office_init(action_mod):
        lust_blowjob_office_enabled(action_mod.enabled)
        return

    def lust_blowjob_office_enabled(enabled):
        if enabled:
            if not mc.business.event_triggers_dict.get("lust_office_blowjob_unlocked", False):
                mc.business.add_mandatory_crisis(lust_blowjob_office_intro_action)
        else:
            mc.business.remove_mandatory_crisis("lust_blowjob_intro_label")
        return

    # extend the default build phone menu function with renovations
    def build_phone_menu_office_blowjob_extended(org_func):
        def phone_menu_wrapper():
            # run original function
            phone_menu = org_func()
            # run extension code
            if mc.business.event_triggers_dict.get("lust_office_blowjob_unlocked", False):
                lust_blowjob_call_action = Action("Office Blowjob {image=gui/heart/Time_Advance.png}", lust_blowjob_office_requirement, "lust_blowjob_office_label", menu_tooltip = "Order an employee to give you a blowjob in your office.", priority = 10)
                phone_menu[2].insert(1, lust_blowjob_call_action)

            return phone_menu

        return phone_menu_wrapper

    build_phone_menu = build_phone_menu_office_blowjob_extended(build_phone_menu)

    lust_blowjob_office_intro_action = ActionMod("Office Blowjob", lust_blowjob_intro_requirement, "lust_blowjob_intro_label",
        initialization = lust_blowjob_office_init, on_enabled_changed = lust_blowjob_office_enabled,
        menu_tooltip = "Order an employee to give you a blowjob", category="Business")

label lust_blowjob_intro_label():
    $ the_person = None
    "In between shifts, you make your way around the office. You stop once in a while to admire some of the women you have employed."
    "Someone stops and asks you about something... it takes several seconds of staring at their tits before you realize they are talking to you."
    "Your sexual tension is starting to distract you from your work. You decide to hide in your office. You lock the door behind you."
    $ mc.change_location(ceo_office)
    "You sit down at your computer and lookup some porn. You browse for a bit, looking for something good to watch."
    "As you are looking around though, you start to rethink this decision."
    "You own this business. You employ all these women. With the progress you've made with the serums, surely you could convince someone to help you out?"
    "You pull up your employee list on your computer... who should you call down?"
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(get_willing_lust_blowjob_girl_list(), "Call in")]
        , draw_hearts_for_people = False))

    if not isinstance(_return, Person):
        return  # this should not happen

    $ the_person = _return
    "You walk over to your door and unlock it as you call [the_person.possessive_title]. You tell her to come to your office ASAP."
    "You walk back to your desk and sit down. Soon, there's a knock on your door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I did. Step inside and close the door... and lock it."
    the_person "Oh... okay..."
    "She does as you instruct before walking over to your desk and sitting down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "Okay, I'm going to get straight to the point. I can't focus on work because of all the distractions around here. I need you to get me off so I can get back to work."
    the_person "Oh! Wow I didn't realize... god you scared me calling me in here like this!"
    if the_person.has_taboo("sucking_cock"):
        "[the_person.title] gets a shy smile on her face."
        the_person "So... you want like... a blowjob?"
        mc.name "It doesn't have to be your mouth, if you don't feel comfortable you could just use your hand."
        the_person "That's okay. To be honest I kinda want to find out how you taste."
    else:
        "[the_person.title] smiles at you."
        the_person "How about a blowjob? Would that help you get back to work?"
        if the_person.sluttiness > 70:
            the_person "Or do you need a different hole?"
        mc.name "A blowjob sounds perfect."
    "[the_person.possessive_title] walks around your desk, then gets on her knees next your chair. You turn to her."
    $ the_person.draw_person(position = "blowjob")
    "She fumbles with your zipper for a second, but soon has your cock out. She looks up at you while she gives it a couple strokes."
    the_person "Mmm, you're right, it's so hard! I bet you've got a big load saved up for me..."
    "[the_person.title] runs her tongue along the tip, tasting your pre-cum. She moans quietly before opening her mouth and slowly sliding the tip in her mouth."
    $ the_person.break_taboo("sucking_cock")
    call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_lust_blowjob_intro
    $ the_report = _return

    if the_report.get("guy orgasms", 0) == 0:
        $ the_person.draw_person(position = "blowjob")
        "Frustrated with her service, you take control of the situation and finish yourself off by hand."
        $ the_person.cum_on_face()
        $ the_person.draw_person(position = "kneeling1")
        "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
        $ ClimaxController.manual_clarity_release()
    else:
        "Fully spent, you let yourself relax in your chair."
    $ the_person.draw_person(position = "stand3")
    "[the_person.title] stands up."
    the_person "Wow, I hope that helps you focus again [the_person.mc_title]. If you need this again, just let me know..."
    mc.name "Don't worry, I will."
    $ the_person.change_stats(obedience = 5, happiness = 5, slut = 1, max_slut = 50)
    $ the_person.review_outfit()
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and walks out of your office. That went great!"
    "You can now order an employee to give you a blowjob in the privacy of your office using your phone."
    $ mc.business.event_triggers_dict["lust_office_blowjob_unlocked"] = True
    "Realizing you have employees willing to suck your cock anytime you ask, you think about the mental gymnastics you've always put yourself through."
    "Lust has always been a taboo thing, to be shoved down and repressed, until you have the rare opportunity to utilize it."
    "But now... why bother repressing it? You make a mental note to stop repressing it. Now whenever you would normally gain lust, you gain extra."
    $ add_lust_gain_perk()
    "You have gained a new perk! Every time you normally gain lust, you gain 5 extra."
    return

label lust_blowjob_office_label():
    "All the skin and sexy outfits you've been exposed to at work has got you hard as a rock and you need some relief."
    "You decide to call an employee in for a blowjob and pull up your employee list on your phone."
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(mc.business.employee_list, "Call in", "Change your mind")]
        draw_hearts_for_people = True))

    if not isinstance(_return, Person):
        "After looking at your employee list, you change your mind. Maybe another opportunity will present itself later."
        return

    $ the_person = _return
    "You call [the_person.possessive_title] and tell her to come to your office ASAP."
    $ mc.change_location(ceo_office)
    "Soon, there's a knock on your door."
    mc.name "Come in."
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I did. Step inside and close the door... and lock it."
    the_person "Oh... okay..."
    "She does as you instruct before walking over to your desk and sitting down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "Okay, I'm going to get straight to the point. I can't focus on work because of all the distractions around here."
    mc.name "I need you to give me a blowjob."
    $ slut_base = the_person.effective_sluttiness("sucking_cock")
    $ final_slut_requirement, final_slut_cap  = blowjob.calculate_position_requirements(the_person, False)
    if slut_base > (final_slut_requirement * 1.5) and not the_person.has_taboo("sucking_cock"):  #She's very slutty. Gets excited and strips first.
        the_person "Wow! Of all the employees here, you picked me for this? Thank you!"
        $ the_person.draw_person(position = "stand3")
        "[the_person.possessive_title] stands up and walks excitedly around your desk."
        the_person "Here, I bet this will help."
        $ the_person.strip_outfit(position = "stand3")
        "[the_person.title] sheds her clothes, giving you a good look at her naked body before getting down on her knees."
        $ the_person.draw_person(position = "blowjob")
        "She unzips your pants and pulls your cock out, giving it a couple strokes."
        if the_person.has_cum_fetish:
            "With her other hand she cups your balls, feeling their weight."
            the_person "Oh god... I can feel how full you are. You've saved up a big load for me, haven't you?"
            "[the_person.possessive_title] leans forward and licks all around the tip, savoring the taste of your cum."
            $ the_person.change_arousal(20)
            the_person "Oh fuck it's so warm... I can't wait to feel it explode!"
            if the_person.is_bald:
                "[the_person.title] opens her mouth and takes you easily inside and down her throat. You run put your hand on the back of her head as she starts to blow you."
            else:
                "[the_person.title] opens her mouth and takes you easily inside and down her throat. You run a hand through her [the_person.hair_description] as she starts to blow you."
            call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_cum_fetish_lust_blowjob_01
            $ the_report = _return
            if the_report.get("guy orgasms", 0) == 0:
                $ the_person.draw_person(position = "blowjob")
                "You decide to take control of the situation and finish yourself off by hand."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "kneeling1")
                "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
                $ ClimaxController.manual_clarity_release()
            else:
                "Fully spent, you let yourself relax in your chair."
            $ the_person.draw_person(position = "stand3")
            "[the_person.title] stands up."
            the_person "Wow, I needed that too. Thank you so much for calling me [the_person.mc_title]."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title] turns and walks out of your office. She doesn't even bother to clean up."
        else:
            the_person "God you are so hard today. I bet you've got a big load saved up in there for me, don't you?"
            call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _lust_blowjob_at_work_02
            $ the_report = _return
            if the_report.get("guy orgasms", 0) == 0:
                $ the_person.draw_person(position = "blowjob")
                "Frustrated with her service, you take control of the situation and finish yourself off by hand."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "kneeling1")
                "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
                $ ClimaxController.manual_clarity_release()
            else:
                "Fully spent, you let yourself relax in your chair."
            $ the_person.draw_person(position = "stand3")
            "[the_person.title] stands up."
            the_person "Wow, I hope that helps you focus again [the_person.mc_title]. I'm always happy to suck you off when you need it."
            mc.name "Thanks."
            $ the_person.change_stats(obedience = 5, happiness = 5)
            $ the_person.review_outfit()
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title] turns and walks out of your office."

    elif slut_base > final_slut_requirement:   #She accepts
        the_person "Oh! Wow I didn't realize... god you scared me calling me in here like this!"
        if the_person.has_taboo("sucking_cock"):
            "[the_person.title] gets a shy smile on her face."
            the_person "So... you want a blowjob?"
            mc.name "Yes. I've always wanted to feel your lips wrapped around me."
            the_person "Mmm... okay. To be honest I kinda want to find out how you taste."
        else:
            "[the_person.title] smiles at you."
            the_person "Mmm, a blowjob. Okay I'll do it."
        "[the_person.possessive_title] walks around your desk, then gets on her knees next your chair. You turn to her."
        $ the_person.draw_person(position = "blowjob")
        "She fumbles with your zipper for a second, but soon has your cock out. She looks up at you while she gives it a couple strokes."
        the_person "Mmm, you're right, it's so hard! I bet you've got a big load saved up for me..."
        "[the_person.title] runs her tongue along the tip, tasting your pre-cum. She moans quietly before opening her mouth and slowly sliding the tip in her mouth."
        $ the_person.break_taboo("sucking_cock")
        call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_lust_blowjob_office_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) == 0:
            $ the_person.draw_person(position = "blowjob")
            "Frustrated with her service, you take control of the situation and finish yourself off by hand."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "kneeling1")
            "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
            $ ClimaxController.manual_clarity_release()
        else:
            "Fully spent, you let yourself relax in your chair."
        $ the_person.draw_person(position = "stand3")
        "[the_person.title] stands up."
        the_person "Wow, I hope that helps you focus again [the_person.mc_title]. If you need this again, just let me know..."
        mc.name "Don't worry, I will."
        $ the_person.change_stats(obedience = 5, happiness = 5, slut = 1, max_slut = 50)
        $ the_person.review_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] turns and walks out of your office."
    elif slut_base + (the_person.obedience-100) >= final_slut_requirement:  #You can order her to do it
        "[the_person.possessive_title] gasps."
        the_person "Wh... What??? You want me to..."
        "She lowers her voice to a whisper."
        the_person "Suck on it?"
        "You can see a troubled look in her eyes. You can tell she wants to, but her propriety is holding her back."
        mc.name "That is exactly what I want. Is there a problem?"
        the_person "I... sir are you sure that would be... proper?"
        mc.name "[the_person.title], is it proper for you to do the work that is assigned to you? Tasks that are assigned to you by me?"
        the_person "Of course..."
        mc.name "Then just think of this as an extra task that I am assigning. You can say no, if you choose, but it would really be helping me out if you would do it."
        if the_person.has_taboo("sucking_cock"):
            the_person "I suppose, but we... we just haven't done anything like this before!"
            mc.name "I know, but it would really help me out. And it would help the company, if I can finally concentrate on my work."
            "[the_person.title] takes several seconds to consider what you are saying."
            the_person "I suppose... I could try it."
        else:
            "[the_person.title] takes several seconds to consider what you are saying."
            the_person "I suppose... I mean... we've done this before..."
        the_person "What do you want me to do?"
        mc.name "Just come around here, and get on your knees."
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] obediently gets down, you pull your cock out. She gasps when she sees it."
        the_person "Wow... it looks so hard! It's okay... I'll take care of it!"
        $ the_person.add_situational_slut("situation",10, "I'm doing my work duties.")
        "[the_person.title] opens her mouth and begins to suck you off. She starts off tentatively, but soon has a good rhythm going."
        call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_lust_blowjob_office_02
        $ the_report = _return
        $ the_person.clear_situational_slut("situation")
        if the_report.get("guy orgasms", 0) == 0:
            $ the_person.draw_person(position = "blowjob")
            "Frustrated with her service, you take control of the situation and finish yourself off by hand."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "kneeling1")
            "As you finish, you point your cock at [the_person.possessive_title]'s face, covering it in your seed."
            $ ClimaxController.manual_clarity_release()
        else:
            "Fully spent, you let yourself relax in your chair."
        $ the_person.draw_person(position = "stand3")
        "[the_person.title] stands up."
        mc.name "See? That was exactly what I needed. Thank you [the_person.title]."
        $ the_person.change_stats(obedience = 5, happiness = -5, slut = 1, max_slut = 50)
        the_person "I suppose that was okay... let's not make a habit of this... okay?"
        mc.name "Don't worry, I won't."
        $ the_person.review_outfit()
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] turns and walks out of your office."
    else:   #She refuses
        $ the_person.draw_person(emotion="angry")
        the_person "Wha... what the fuck? You scare me half to death, calling me in here ASAP, thinking I'm in trouble for something..."
        "Her face grows red in anger."
        the_person "You're a sick man. I'm not some floozy for you to get your rocks off with!"
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_stats(happiness = -5, obedience = -1, love = -2)
        "[the_person.possessive_title] quickly stands up and storms out of your office. Maybe you should be more careful who you pick for this?"
    call advance_time from _call_advance_time_lusty_blowjob_01
    return


label lust_blowjob_unit_test():
    $ mc.free_clarity = 0
    $ mc.change_locked_clarity(500)
    if not lust_blowjob_intro_requirement():
        "Intro requirements not met! Aborting unit test"
        return
    call lust_blowjob_intro_label() from _lust_unit_test_1
    $ mc.energy = mc.max_energy
    $ mc.change_locked_clarity(mc.free_clarity * 3)
    if not lust_blowjob_office_requirement():
        "Office blowjob requirements not met! aborting unit test"
        return
    call lust_blowjob_office_label() from _lust_unit_test_2
    "Unit test successful completion."
    return
