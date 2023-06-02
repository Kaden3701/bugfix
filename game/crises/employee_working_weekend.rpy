###Scene Idea: Working Weekend
#
#   In this scene, MC is working on the weekend when the business is otherwise closed.
#   Girl comes in to grab something from their locker or workspace and finds player working.
#   If not slutty, girl is just impressed by the MC work ethic.
#   If girl is a little slutty, she may offer to tease MC or give a blowjob
#   If girl is very slutty, girl may take the opportunity to striptease
#
#
###
init 2 python:
    def SB_working_weekend_requirement():
        if mc.business.is_weekend and mc.is_at_work and mc.location.person_count < 1:
            return mc.business.employee_count > 2
        return False

    def person_opinion_to_string(person, topic):
        score = person.get_opinion_score(topic)
        if score <= -2:
            return (score, "actually hate")
        if score == -1:
            return (score, "don't like")
        if score == 0:
            return (score, "have no opinion about")
        if score == 1:
            return (score, "like")
        if score >= 2:
            return (score, "actually love")

    def get_topic_text(topic):
        if topic == "getting head":
            return "when guys lick my pussy"
        if topic == "creampies":
            return "when guys cum inside me"
        if topic == "being covered in cum":
            return "when guys cum all over me"
        if topic == "cum facials":
            return "when guys cum all over my face"
        if topic == "drinking cum":
            return "swallowing cum"
        if topic == "bareback sex":
            return "having sex without a condom."
        if topic == "showing her tits":
            return "showing my tits"
        if topic == "showing her ass":
            return "showing my ass"
        if topic == "lingerie":
            return "wearing lingerie"
        return topic

    def count_topic_opinions(person, topics):
        counter = 0
        for topic in topics:
            (score, opinion) = person_opinion_to_string(person, topic)
            if score != 0:
                counter += 1
        return counter

    def display_topic_opinions(person, topics):
        counter = 0
        for topic in topics:
            (score, opinion) = person_opinion_to_string(person, topic)
            if score != 0:
                display_text = get_topic_text(topic)
                renpy.say(person.char, "I " + opinion + " " + display_text + ".")
                counter += 1
                person.discover_opinion(topic)
        return counter

    working_weekend_topics = {
        "general" : ["flirting", "sports", "hiking", "Mondays", "Fridays", "the weekend"],
        "work": ["working", "work uniforms", "research work", "marketing work", "HR work", "supply work", "production work"],
        "style": ["skirts", "pants", "dresses", "boots", "high heels", "makeup", "conservative outfits", "the colour blue", "the colour yellow", "the colour red", "the colour pink", "the colour green", "the colour purple", "the colour white", "the colour black"],
        "positions": ["missionary style sex", "doggy style sex", "sex standing up"],
        "sex_types": ["vaginal sex", "anal sex", "giving blowjobs", "getting head"],
        "cum": ["creampies", "being covered in cum", "cum facials", "drinking cum", "bareback sex"],
        "sexy_clothing" : ["skimpy outfits", "skimpy uniforms", "not wearing underwear", "not wearing anything", "showing her tits", "showing her ass", "lingerie", "high heels", "dresses"],
        "kinks" : ["masturbating", "giving handjobs", "being fingered", "being submissive", "taking control"]
    }

    SB_working_weekend_crisis = ActionMod("Working Weekend",SB_working_weekend_requirement,"SB_working_weekend_crisis_label",
        menu_tooltip = "While working weekends an employee comes into the office.", category = "Business", is_crisis = True)

label SB_working_weekend_crisis_label():
    $ person_one = get_random_employees(1, exclude_list = [] if not sarah_epic_tits_progress() == 1 else [sarah])
    if person_one is None:
        return
    $ scene_manager = Scene()
    "Even though it is the weekend, you find yourself working."
    if mc.business.is_open_for_internship:
        "Deep in thought, and with the [mc.location.name] normally deserted, it takes you by surprise when you see movement out of the corner of your eye."
    else:
        "Deep in thought, and with the company normally deserted, it takes you by surprise when you see movement out of the corner of your eye."
    "Looking aside, you see [person_one.possessive_title]."
    $ scene_manager.add_actor(person_one, emotion="default")
    $ scene_manager.draw_scene()
    "You can tell by the look on her face that [person_one.possessive_title] is also surprised to see you."
    if person_one.effective_sluttiness() > 70 and not person_one.has_taboo("vaginal_sex"):
        call SB_working_weekend_crisis_label_high(person_one) from _call_SB_working_weekend_crisis_label_high
    elif person_one.effective_sluttiness() > 40 and not person_one.has_taboo("sucking_cock"):
        call SB_working_weekend_crisis_label_medium(person_one) from _call_SB_working_weekend_crisis_label_medium
    else:
        call SB_working_weekend_crisis_label_low(person_one) from _call_SB_working_weekend_crisis_label_low
    $ scene_manager.clear_scene()
    $ person_one.apply_planned_outfit()
    $ del person_one
    $ mc.location.show_background()
    return

label SB_working_weekend_crisis_label_high(person_one):
    person_one "Oh hey [person_one.mc_title]! Are you here all by yourself?"
    if mc.business.is_open_for_internship:
        mc.name "Well there is an intern working somewhere, but I'm alone here."
        "You explain as you finish up what you were doing."
    else:
        "You give her a quick nod as your finish up what you were doing."
    "Seeing that you are here all by yourself, [person_one.possessive_title] grabs a chair and sits close to you."
    $ scene_manager.update_actor(person_one, position = "sitting")
    person_one "Wow, your dedication to this place is pretty sexy... would you like to maybe... blow off a little steam?"
    $ mc.change_locked_clarity(20)
    "[person_one.possessive_title] begins to rub your crotch through your pants. You are almost done with your previous task, maybe you could get her to do something while you finish up..."
    menu:
        "Strip for me":
            mc.name "Hey, I'm almost done with this, but I tell you what. Why don't you give me a show while I finish and then maybe when I'm done I'll take you up on that."
            "[person_one.possessive_title] smiles mischievously at you, before nodding."
            person_one "I can do that, [person_one.mc_title]... I hope you like the show!"
            $ person_one.change_slut(2)
            call strip_tease(person_one, for_pay = False) from _free_strip_scene_3
            $ mc.change_locked_clarity(50)
            if mc.business.is_open_for_internship:
                $ person_two = get_random_interns(1)
            else:
                $ person_two = get_random_employees(1, exclude_list = [person_one] if not sarah_epic_tits_progress() == 1 else [sarah, person_one])
            if not willing_to_threesome(person_one, person_two):
                "You're pretty sure she's ready for next step if you are."
                menu:
                    "Fuck her on your desk" if person_one.is_willing(missionary): # only show sex option if she's willing
                        "You walk over to [person_one.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
                        "When her ass runs up against the desk, she reaches down and begins unzipping your pants."
                        $ mc.change_locked_clarity(30)
                        $ person_one.break_taboo("condomless_sex")
                        "She pulls your your dick out and lays back. She lines you up with her pussy and you push yourself into her."
                        call fuck_person(person_one, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_sex_description_SB15
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 0:
                            "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a while, recovering from her orgasm."
                            $ person_one.change_stats(slut = 3, love = 5)
                        else:   #She didn't cum
                            "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a bit, clearly disappointed she didn't orgasm."
                            $ person_one.change_stats(slut = 1, happiness = -5)
                        $ person_one.apply_planned_outfit()
                        $ person_one.draw_person()
                        "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
                    "Explore her body":
                        "You walk over to [person_one.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
                        "When her ass runs up against the desk you set her down and take a half step back."
                        $ mc.change_locked_clarity(30)
                        "Judging by the moisture glistening on her pussy, the show got her almost as excited as you."
                        call fuck_person(person_one, start_position = standing_finger, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_sex_description_SB15_2
                        $ the_report = _return
                        if the_report.get("girl orgasms", 0) > 0:
                            "[person_one.possessive_title] lays there for a while, recovering from her orgasm."
                            $ person_one.change_stats(slut = 3, love = 5)
                        else:   #She didn't cum
                            "[person_one.possessive_title] lays there for a bit, clearly disappointed she didn't orgasm."
                            $ person_one.change_stats(slut = 1, happiness = -5)
                        $ person_one.apply_planned_outfit()
                        $ person_one.draw_person()
                        "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
                    "Thank her for the show":
                        mc.name "Thanks for that very pleasant distraction, [person_one.title], but I need to get back to work now."
                        "[person_one.possessive_title] can barely hide their disappointment. There's a hint of anger in their voice when they reply."
                        person_one "Wow, really? After I stripped for you? Okay then, I hope your day goes better than mine..."
                        $ person_one.change_stats(slut = 2, happiness = -5, love = -5)
            else:  #Someone walks in, threesome opportunity#
                "You walk over to [person_one.possessive_title]. She wraps her arms around you as you roughly grab her ass and pick her up. She's grinding herself against you as you carry her over to your desk."
                $ scene_manager.update_actor(person_one, position = "kissing")
                $ mc.change_locked_clarity(30)
                "[person_one.possessive_title] is just pulling your cock out when you hear a cough from the doorway."
                $ person_one.break_taboo("touching_penis")
                person_two "Wow, looks like you guys are getting ready for some fun!"
                $ scene_manager.add_actor(person_two, position = "stand3", display_transform = character_left, emotion = "happy")
                "You turn and see [person_two.possessive_title] standing in the doorway. You aren't sure how long she has been standing there."
                person_two "This is so sexy... [person_two.mc_title], can I join? Please!?! You won't regret it!"
                $ mc.change_locked_clarity(50)
                "Dumbfounded, you can only nod."
                person_two "Yes! Oh just give me one second!!!"
                "She starts to strip down."
                $ scene_manager.strip_full_outfit(person = person_two)
                $ person_two.break_taboo("bare_tits")
                $ person_two.break_taboo("bare_pussy")
                $ mc.change_arousal(10)
                "Now naked, she walks over to you and [person_one.possessive_title]."
                person_two "Okay, how do you want to do this?"
                call start_threesome(person_one, person_two) from _call_start_threesome_SB_working_weekend_crisis
                $ the_report = _return
                "Wow, you just had sex with [person_one.title] and [person_two.title]! You can't believe how lucky you are."
                "Eventually, [person_two.possessive_title] gets up."
                $ scene_manager.update_actor(person_two, position = "stand3", display_transform = character_center)
                person_two "Mmm... wow... I guess I should stop by on the weekend more often..."
                $ scene_manager.update_actor(person_one, position = "missionary", display_transform = character_right)
                $ person_two.apply_planned_outfit()
                $ scene_manager.update_actor(person_two, position = "walking_away")
                "[person_two.possessive_title] puts on her clothes and heads for the door."
                $ scene_manager.remove_actor(person_two)
                if the_report.get("girl one orgasms", 0) > 0:
                    "You get up and make yourself presentable again. [person_one.possessive_title] lays there for a while, recovering from her orgasm."
                    $ person_one.change_stats(happiness = 5, slut = 3, love = 3)
                person_one "Holy fuck [person_one.mc_title], that was so hot."
                $ person_one.apply_planned_outfit()
                $ scene_manager.update_actor(person_one, position = "stand3")
                "She eventually gets up and gets herself dressed again. You say goodbye as she leaves the office."
            $ del person_two
        "Just Talk":
            "While her offer is tempting, you decide to take the opportunity to learn a little more about [person_one.possessive_title]."
            mc.name "Sorry, I can't while I'm in the middle of this, but maybe you could stay and talk to me for a little while."
            "[person_one.possessive_title] is clearly disappointed, so you decide to keep the topic of conversation sexual to keep her interested."
            "What do you ask about?"
            menu:
                "Positions" if count_topic_opinions(person_one, working_weekend_topics["positions"]) > 0:
                    mc.name "So, how do you feel about different sexual positions, [person_one.title]?"
                    "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                    person_one "Well..."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["positions"])
                "Sex types" if count_topic_opinions(person_one, working_weekend_topics["sex_types"]) > 0:
                    mc.name "So, how do you feel about different types of sex, [person_one.title]?"
                    "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["sex_types"])
                "Cum" if count_topic_opinions(person_one, working_weekend_topics["cum"]) > 0:
                    mc.name "So, how do you feel about cum, [person_one.title]?"
                    "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["cum"])
                "Sexy Clothing" if count_topic_opinions(person_one, working_weekend_topics["sexy_clothing"]) > 0:
                    mc.name "So, how do you feel about sexy clothing and outfits, [person_one.title]?"
                    "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["sexy_clothing"])
                "Other Kinks" if count_topic_opinions(person_one, working_weekend_topics["kinks"]) > 0:
                    mc.name "So, do you have any kinks, [person_one.title]? Something that might be more fun for me to know about?"
                    "[person_one.possessive_title] smiles when she realizes you are going to keep the topic interesting."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["kinks"])
            $ mc.change_locked_clarity(20)
            if SB_discover_opinion_count == 0:
                person_one "I guess you could say I don't care too much about that."
            elif SB_discover_opinion_count < 2:
                person_one "So I guess you could say I don't have a lot of strong feelings about that."
            else:
                person_one "So I guess you could say I have a lot of opinions on that."
            "You chat with [person_one.possessive_title] for a little longer. Eventually she says goodbye and heads out."
    return

label SB_working_weekend_crisis_label_medium(person_one):
    "Before you can respond, [person_one.possessive_title] pulls up a chair and sits beside you."
    $ scene_manager.update_actor(person_one, position = "sitting")
    person_one "Wow, your dedication to this place is pretty incredible... Don't you ever do something... you know, to blow off steam?"
    "[person_one.possessive_title]'s voice takes a bit of a sultry tone at the end of that statement. Is she flirting with you?"
    $ mc.change_locked_clarity(10)
    mc.name "Yes, [person_one.title], of course I do... but... it IS rather boring around here. I'd be grateful for a bit of company while I'm working"
    "[person_one.possessive_title] smiles at you. And was that a wink?"
    person_one "Oh! [person_one.mc_title], I was about to go out, but seeing you here still working on the weekend, I'd be glad to stay here with you a bit and give you a bit of a... distraction."
    "The suggestion in her voice is apparent with the last statement. You briefly consider her offer before making a request..."
    menu:
        "How about a blowjob?" if person_one.is_willing(blowjob):
            "[person_one.possessive_title] smiles."
            person_one "Oh [person_one.mc_title], you work so hard. Don't worry, I'll take care of you."
            if not person_one.tits_available:    #If covered up, have her take her top off
                person_one "Here... let me take this off. I bet that will help ease some of your stress."
                $ the_clothing = person_one.outfit.get_upper_top_layer
                $ mc.change_arousal(10)
                "[person_one.possessive_title] takes off her [the_clothing.name]."
                $ scene_manager.draw_animated_removal(person_one, the_clothing)
                $ the_clothing = None
            $ mc.change_arousal(10)
            "Your eyes wander down to [person_one.possessive_title]'s tits."
            $ mc.change_locked_clarity(30)
            if person_one.tits_available:
                if person_one.get_opinion_score("showing her tits") > 0:
                    "You can see a blush in [person_one.possessive_title]'s cheeks. She likes to show off her [person_one.tits] tits!"
                    $ person_one.discover_opinion("showing her tits")
                    $ person_one.change_slut(1)
                    $ person_one.change_slut(2)
            $ mc.change_arousal(10)
            "You back your chair up and move it to the side while [person_one.possessive_title] gets down on her knees in front of you."
            $ person_one.break_taboo("sucking_cock")
            $ scene_manager.update_actor(person_one, position = "blowjob")
            $ person_one.add_situational_slut("seduction_approach",20, "Your dedication turns me on.")
            $ person_one.add_situational_obedience("seduction_approach", 5, "I will do this for you.")
            call fuck_person(person_one, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_SB1
            $ person_one.clear_situational_slut("seduction_approach")
            $ person_one.clear_situational_obedience("seduction_approach")
            $ person_one.draw_person()
            "Eventually, [person_one.possessive_title] gets up. She says goodbye after giving you a quick kiss."
        "Just Talk":
            "You decide to take the opportunity to learn a little more about [person_one.possessive_title]."
            "You chit chat about various things. You decide to probe a little further about her interests."
            $ SB_discover_opinion_count = 0
            menu:
                "Ask about general opinions" if count_topic_opinions(person_one, working_weekend_topics["general"]) > 0:
                    "You decide to ask about her general opinions."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["general"])
                "Ask about work opinions" if count_topic_opinions(person_one, working_weekend_topics["work"]) > 0:
                    "You decide to ask about her opinions about work."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["work"])
                "Ask about style opinions" if count_topic_opinions(person_one, working_weekend_topics["style"]) > 0:
                    "You decide to ask about her opinions about her personal style."
                    $ SB_discover_opinion_count = display_topic_opinions(person_one, working_weekend_topics["style"])
            "You chat with [person_one.possessive_title] for a bit longer, but eventually she says goodbye and leaves."
    return

label SB_working_weekend_crisis_label_low(person_one):
    #if she is not slutty at all
    person_one "Oh hey there [person_one.mc_title], I didn't expect to see you here! I just stopped by because I forgot something in my desk. Are you... working? You know it's the weekend right?"
    "You can tell by the look on her face that she is impressed by your work ethic. You consider the chance to impress on her the values of the company in this one on one situation."
    menu:
        "Stress the importance of obedience":
            mc.name "It is no accident that this place is accomplishing great things. The work I am trying to do requires many long hours, but also organization and commitment to procedures."
            mc.name "A highly organized workplace is important, especially in a lab setting. I need employees who are able to listen to my instructions and follow them."
            "[person_one.possessive_title] nods in agreement."
            mc.name "You are doing a great job so far, [person_one.title], can I count on you to listen and obey the tasks I set out for you?"
            $ person_one.change_obedience(10)
            person_one "Yes, absolutely. I'll do everything I can to make sure this business is successful."
        "Stress the importance of satisfaction":
            mc.name "I've worked hard to build this place into what it is. Even though it is the weekend, I can't help but come out here and work on improving the business in any way I can..."
            mc.name "But it can be easy to burn yourself out in this line of business. Pay might not always be great and the hours might be long, but a good attitude is key."
            "[person_one.possessive_title] nods in agreement."
            mc.name "You are doing a great job for me so far, [person_one.title], but take care of yourself, and don't let yourself get burned out."
            $ person_one.change_happiness(10)
            person_one "Yes sir, I do enjoy being here."
        "Stress the importance of work hard, play hard":
            mc.name "Yes, it is true that I work late into the days and even on the weekends, but that doesn't mean that I'm all business."
            mc.name "It is important though, that when you work hard, you can also play hard."
            "[person_one.possessive_title] nods in agreement."
            mc.name "You are doing a great job for me so far, [person_one.title]. Maybe some time we should play hard together?"
            $ person_one.change_slut(1, 30)
            person_one "Oh! I suppose I might be up for something like that, sometime anyway."
    "After a minute of chit chat, [person_one.possessive_title] eventually says goodbye and walks out of the room."
    return
