init 2 python:
    erica_yoga_poses = ["walking_away", "against_wall", "cowgirl", "doggy", "kissing", "missionary", "standing_doggy"]
    erica_yoga_pose_descriptions = {
        "walking_away" : "The girls are stretching one foot out in front of them, trying to maintain balance.",
        "against_wall" : "The girls are holding their arms out while balancing on one leg.",
        "cowgirl" : "The girls are on their knees, stretching out their backs.",
        "doggy" : "The girls are doing the downward facing dog.",
        "kissing" : "The girls are holding their arms out while doing breathing exercises.",
        "missionary" : "The girls are on their backs, stretching their legs out.",
        "standing_doggy" : "The girls are in a line, stretching their backs while they lean over."
    }

    erica_yoga_sexy_pose_descriptions = {
        "walking_away" : "The pose gives you a great view of their backsides.",
        "against_wall" : "Your eyes are drawn between their legs as they stretch.",
        "cowgirl" : "You can't help but imagine the girls mounting you in a similar pose...",
        "doggy" : "You watch intently at the room of asses pointed back at you. You think you see a couple wiggle...",
        "kissing" : "You wonder if the girls would be breathing so evenly if you were on your knees, eating them out.",
        "missionary" : "You can't help but fantasize about walking out, pinning one of the girls down, and having your way with her in this pose.",
        "standing_doggy" : "The sight of the class all bent over in front of you is breathtaking."
    }

    erica_yoga_nude_pose_descriptions = {
        "walking_away" : "Rows of ample backsides are available for your viewing pleasure.",
        "against_wall" : "Several of the girls' pussy lips are puffy, showing clear signs of arousal.",
        "cowgirl" : "You make eye contact with several of them. You can tell from the way they look at you they are thinking similar thoughts.",
        "doggy" : "Rows of fuckable cunts and asses are on display, ripe for the taking.",
        "kissing" : "You breathe deeply with them. The musk of feminine arousal is heavy in the air.",
        "missionary" : "You notice a couple girls' hands stray between their legs, their arousal on obvious display.",
        "standing_doggy" : "You wonder how many asses you could fill with cum before your cock refused to get hard again. You bet several."
    }

    def display_yoga_dialog(pose):
        renpy.say(None, erica_yoga_pose_descriptions[pose])
        if slutty_class:
            renpy.say(None, erica_yoga_sexy_pose_descriptions[pose])
            mc.change_arousal(20)
            if nude_class:
                renpy.say(None, erica_yoga_nude_pose_descriptions[pose])
                mc.change_locked_clarity(30)
            else:
                mc.change_locked_clarity(20)
        else:
            mc.change_locked_clarity(10)
        return

init -2 python:
    def erica_money_problems_sarah_talk_requirement(person):
        return mc.business.hr_director and person.is_at_work

    def erica_money_problems_sarah_update_requirement():
        if mc.business.is_open_for_business:
            if mc.business.hr_director and mc.is_at_work:
                if day >= erica.event_triggers_dict.get("yoga_quest_hr_talk_day", 0) + TIER_1_TIME_DELAY:
                    return True
        return False

    def erica_money_problem_sarah_convincing_employee_requirement():
        if mc.business.is_open_for_business:
            if mc.business.hr_director and mc.is_at_work:
                return day > sarah.event_triggers_dict.get("last_talk_day", 0) + 2
        return False

    def erica_money_problems_sarah_final_update_requirement():
        if mc.business.is_open_for_business:
            if mc.business.hr_director and mc.is_at_work:
                if day >= erica.event_triggers_dict.get("yoga_quest_hr_talk_day", 0) + TIER_1_TIME_DELAY:
                    return True
        return False

    def erica_money_problems_yoga_start_requirement(person):
        return mc.business.hr_director and person.location == gym

    def erica_yoga_event_intro_requirement():
        return mc.business.hr_director and day%7 == 1

    def erica_weekly_yoga_requirement(person):
        return mc.business.hr_director and person.location == lobby and day%7 == 1

init -1 python:
    erica_money_problems_sarah_talk = Action("Talk to HR Director", erica_money_problems_sarah_talk_requirement, "erica_money_problems_sarah_talk_label")
    erica_money_problems_sarah_update = Action("Sarah reports back about yoga", erica_money_problems_sarah_update_requirement, "erica_money_problems_sarah_update_label")
    erica_money_problem_sarah_convincing_employee = Action("Sarah doses another employee", erica_money_problem_sarah_convincing_employee_requirement, "erica_money_problem_sarah_convincing_employee_label")
    erica_money_problems_sarah_final_update = Action("Sarah has enough attendants", erica_money_problems_sarah_final_update_requirement, "erica_money_problems_sarah_final_update_label")
    erica_money_problems_yoga_start = Action("Talk to Erica about yoga", erica_money_problems_yoga_start_requirement, "erica_money_problems_yoga_start_label")
    erica_yoga_event_intro = Action("First yoga class", erica_yoga_event_intro_requirement, "erica_yoga_event_intro_label")
    erica_weekly_yoga = Action("Weekly yoga class", erica_weekly_yoga_requirement, "erica_weekly_yoga_label")

label erica_money_problems_sarah_talk_label(the_person):
    mc.name "Hey, I have a question for you."
    the_person "Okay, shoot..."
    mc.name "My sister has a friend at the local university who is struggling to make ends meet while taking her classes."
    mc.name "She's looking for a part-time job. Would you happen to know of anything around here I could hire her to do? It has to be on a fairly flexible schedule, she needs to be able to focus on her education."
    "[the_person.possessive_title] pauses as she considers your inquiry."
    the_person "Well... Things are running fairly smoothly here to be honest... I'm not sure what we could have her do. What are her qualifications?"
    "You share what you know about her and what she is studying. Nothing really seems to pique her interest until you mention her doing track and field."
    the_person "Oh! She's an athlete?"
    mc.name "Yeah. Very accomplished in fact. Sometimes we work out together at the gym."
    "The wheels in her head are turning. She seems to have the beginning of an idea in her head."
    if get_HR_director_tag("business_HR_gym_tier", 0) > 0:
        the_person "Some of the girls here are really enjoying the gym membership you've offered... But I've gotten some complaints that after a long day here they are just too tired to make it to the gym."
    else:
        the_person "Some of the girls go to the gym after work, but it is very taxing to go into the gym after work."
    "You consider what she is saying, but you aren't sure how [erica.title] could help. After a pause though, [the_person.title] continues, clearly brainstorming out loud."
    the_person "What if we like... Hired her... To come in, like once a week, and run a personal fitness class?"
    mc.name "Here at the office?"
    the_person "Sure! It could be company sanctioned, and optional, but I think if it were supported, we would get good attendance. You could even start it like an hour before normal start time so it doesn't affect productivity."
    mc.name "Wouldn't having people work out in the morning like that affect their energy for the rest of the day?"
    the_person "You could make it something low impact? And focus on general well-being... Maybe like a yoga class?"
    "Hmm. Having [erica.title] come in and teach a yoga class once a week is actually a pretty good idea. But having it start before normal business hours, you wonder if there would be enough participation to make it worth it."
    mc.name "Can you do something for me? Take an informal poll with the employees... See how many would be interested in something like that. I don't want to arrange it just to have nobody show up."
    the_person "Well I can tell you straight away I'll come. I love yoga! How many do you think we need to make it happen?"
    $ the_person.update_opinion_with_score("yoga", 2, add_to_log = True) #If she doesn't already love yoga, she does now. TODO Maybe make different dialogue and let her not like it, but go along with it?
    mc.name "I think at least 5 total, so with you hopefully we can get 4 more."
    the_person "What about you? Can I count you to come also?"
    "Hmm... A bunch of your employees... In gym gear... Doing a bunch of crazy poses... That would be a pleasant use of the morning. But you don't want to effect the numbers too much."
    mc.name "I think I'd prefer not to be counted in that."
    if mc.business.employee_count < 5:
        the_person "But we don't even have that many employees?"
        mc.name "That's true. It might have to wait until we have enough employees."
    the_person "Ah okay..."
    "She looks a bit disappointed. Your company is pretty small, so you may not have the numbers. She seems to have another idea though."
    the_person "What if, umm... You know... When we do our employee meetings... We could add counseling about... errm... Yoga?"
    "You sigh. It seems [the_person.char] really likes this idea and is looking for ways to make it happen."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        mc.name "Tell you what. We don't need to push it officially, but if you happen to take some of the serum and use it for that purpose... I would be willing to look the other way."
    else:
        mc.name "I don't think that is a good idea. But if you really want to make it happen, you could always use the power of persuasion to see if you can get people to come."
    "[sarah.fname] gets a mischievous smile."
    the_person "Okay! I'll let you know in a couple days if we have the people to make it happen... And if we don't... We'll see."
    "You part ways with [the_person.title] for now. You feel pretty confident at this point that, even if you don't have the numbers now, you'll have enough people to make it happen soon."

    $ erica.event_triggers_dict["yoga_quest_hr_talk_day"] = day
    if len(erica_get_yoga_class_list()) < 4:
        $ mc.business.add_mandatory_crisis(erica_money_problems_sarah_update)
    else:
        $ mc.business.add_mandatory_crisis(erica_money_problems_sarah_final_update)
    return

label erica_money_problems_sarah_update_label():
    # If we have enough people, we finish the quest
    if __builtin__.len(erica_get_yoga_class_list()) >= 4:
        jump erica_money_problems_sarah_final_update_label

    $ the_person = mc.business.hr_director
    $ the_person.draw_person(emotion = "sad")
    "[the_person.title] seeks you out as you work. She seems a bit disappointed."
    $ count = __builtin__.len(erica_get_yoga_class_list())
    if count > 0:
        the_person "Hey... So I was asking around with the girls... unfortunately, I could only get [count] interested in joining the morning yoga class... for now..."
    else:
        the_person "Hey... So I was asking around with the girls... unfortunately, I couldn't find anybody interested in joining the morning yoga class... for now..."

    "You admit you are a bit disappointed as well."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        the_person "So... Do you think that... you know, it would be okay if I, umm... used some of the serum we have for the one-on-ones...?"
        "You had forgotten about her using the serum, and you are glad she reminded you."
        mc.name "Yeah, that sounds fine. Let me know if you manage to convince enough employees and I'll speak with [erica.fname] about starting that morning yoga class."
    else:
        the_person "So, do you think it would be okay if I tried to talk people into coming? I think over time I might be able to convince enough people to come."
        mc.name "That sounds fine. Let me know if you manage to convince enough people and I'll speak with [erica.fname] about starting that program."
    $ the_person.draw_person(emotion = "happy")
    "[the_person.possessive_title] smiles wide. She seems to really be into this..."
    the_person "Yes sir! Don't worry, I'm sure we'll be able to get this going soon!"
    $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
    return

label erica_money_problem_sarah_convincing_employee_label():
    # If we have enough people, we finish the quest
    if __builtin__.len(erica_get_yoga_class_list()) >= 4:
        jump erica_money_problems_sarah_final_update_label

    python:
        scene_manager = Scene()
        the_person = mc.business.hr_director
        the_target = get_yoga_convince_employee_target()

    if the_target is None:
        $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        #For now we add the crisis back so that when we finally have enough employees we can still finish this scenario.
        return

    # change location to lobby, since break room is located here
    $ mc.change_location(lobby)

    "Passing by the break room, you can hear [the_person.possessive_title] talking to someone else inside."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(the_target, position = "sitting", display_transform = character_center_flipped)
    the_person "Yeah, it has lots of health benefits too!"
    the_target "I've heard that, but I don't know, I'm just really busy right now."
    if get_HR_director_tag("business_HR_coffee_tier", 0) > 0:
        the_person "I'm sure you are... more coffee? I just brewed some!"
        $ scene_manager.update_actor(the_person, position = "back_peek")
        the_target "Yeah! That would be great."
        "Sounds like she is using some of the serum you produced for HR meetings to help her persuade [the_target.possessive_title] to come to the yoga class."
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person "Here you go... now, I know we're all busy, but trust me, the benefits of doing yoga really are worth the time!"
        $ scene_manager.update_actor(the_person, position = "sitting")
        the_target "Yeah... maybe you're right..."
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "Sounds like [the_person.possessive_title] is hard at work, convincing some of your employees to give the yoga session a shot!"
        $ the_target.update_opinion_with_score("yoga", 1)
    else:
        if (the_person.charisma * 10 + the_target.suggestibility) > renpy.random.randint(0,100):
            the_person "The science is behind it! People who do yoga live longer, happier lives. Not to mention the general benefits of the extra flexibility."
            the_target "Yeah... maybe you're right..."
            $ scene_manager.update_actor(the_target, emotion = "sad")
            "Sounds like [the_person.possessive_title] is hard at work, convincing some of your employees to give the yoga session a shot!"
            $ the_target.update_opinion_with_score("yoga", 1)
        else:
            the_person "It's good for you! I'm sure of it!"
            the_target "There's a lot of things that are good for you. I'm sorry, I just don't think I'm interested."
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "... I understand."
            "Sounds like [the_person.possessive_title] is still trying to convince employees to give the yoga class a try. You appreciate her dedication to it."

    python:
        scene_manager.clear_scene()
        clear_scene()
        sarah.event_triggers_dict["last_talk_day"] = day
        if __builtin__.len(erica_get_yoga_class_list()) < 4:
            mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        else:
            mc.business.add_mandatory_crisis(erica_money_problems_sarah_final_update)
        the_target = None
    return

label erica_money_problems_sarah_final_update_label():
    if __builtin__.len(erica_get_yoga_class_list()) < 4:
        $ mc.business.add_mandatory_crisis(erica_money_problem_sarah_convincing_employee)
        return

    $ the_person = mc.business.hr_director
    $ the_person.draw_person()
    "[the_person.title] comes and finds you as you work. She seems excited."
    the_person "Hey! Guess what! As of this morning, I have enough girls willing to attend a morning yoga class once a week! As soon as you give me the day, I'll put out a notice."
    mc.name "Great! Let me talk to [erica.fname] about it. I'm not sure what day it will be yet, it will probably depend on her class schedule, but I will let you know."
    the_person "Alright. I'm going to get back to work. Looking forward to it though!"
    $ erica.add_unique_on_talk_event(erica_money_problems_yoga_start)
    return

label erica_money_problems_yoga_start_label(the_person):
    mc.name "I have an idea I wanted to share with you, an opportunity to make some money to help with tuition."
    "[the_person.title] smiles, but you can tell she is also a little apprehensive."
    $ the_person.draw_person()
    the_person "That's great!... Something I can fit into my schedule? I need to be flexible you know..."
    "You can't help but make the obvious joke."
    mc.name "Oh, don't worry. You HAVE to be flexible for this!"
    the_person "I'm not sure what you mean..."
    mc.name "Dumb joke. But how about this: How would you like to teach a yoga class?"
    "She looks at you a bit skeptically."
    the_person "A yoga class? They already offer those here... And the instructor has been doing it for years..."
    mc.name "Not here. It would be once a week, in the morning, on a day of your choosing... At the business I run."
    the_person "At... your company?"
    mc.name "Yeah. We've recently been running some promotions for employees, encouraging them to stay fit, and eat right. What better way to encourage them to do that than with a personal yoga instructor?"
    the_person "That would be... incredible! I didn't realize that you took fitness so seriously! I mean... I know YOU do..."
    "She glances down at your fit chest before she continues."
    the_person "But to make it a company policy... That's a great program!"
    mc.name "I've been working with my HR director. I asked her for help coming up with something you could do at the company, and she helped me come up with the whole thing."
    mc.name "She's already got a list of the people interested, all they need to know is what day works for you to come in. We want to do it in the morning, you know, before your classes."
    "[the_person.title] looks at you, stunned."
    the_person "Wow... It's like you thought of everything!"
    $ the_person.draw_person(position = "kissing")
    $ mc.change_locked_clarity(10)
    "[erica.fname] gives you a big hug. When she steps back, she ponders a moment."
    the_person "How about Tuesday mornings? I could go straight from there to class."
    mc.name "I'll make it happen. For compensation, I'll start you at $100 per session. Are you good to start next week?"
    the_person "That's great! I'll be ready!"
    mc.name "Okay. I'm going to give your number to my HR director. She'll contact you to set up the final details. Her name is [mc.business.hr_director.name]."
    the_person "I'll look for it. I'm going to get back to my workout, thank you so much!"
    "After you finish up your conversation, you text [mc.business.hr_director.title], your HR director. You give her [the_person.possessive_title]'s contact info."
    $ the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
    $ mc.business.hr_director.set_override_schedule(lobby, the_days = [1], the_times =[0])
    $ mc.business.add_mandatory_morning_crisis(erica_yoga_event_intro)
    return

label erica_yoga_event_intro_label():
    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event

        the_person = erica
        yoga_assistant = mc.business.hr_director
        yoga_list = erica_get_yoga_class_list()

        erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)
        erica.event_triggers_dict["yoga_assistant"] = yoga_assistant.identifier

    "It's Tuesday morning, it is weekly morning yoga day! While you don't think you'll need to go every time, since this is the inaugural session, it might be good for you to oversee it, just in case there are any issues."
    if mc.is_at_work:
        "You go down to the lobby to see how things are working out."
        $ mc.change_location(lobby)
        "As you walk into the main lobby, you see some of your employees just getting ready to set up."
    else:
        "You head to the office early, to see how things are working out."
        $ mc.change_location(lobby)
        "When you walk into the main lobby, you see some of your employees just getting ready to set up."

    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    "At the front, you see [the_person.possessive_title] doing some light stretching. She brought a portable Bluetooth speaker, playing some upbeat music."
    "Next to her you see [yoga_assistant.title]. She has been the biggest supporter of this event from the get-go, and it doesn't surprise you to see her at the front of the group. As you walk up, you can hear the two chatting. They seem to be hitting it off..."
    yoga_assistant "Oh! Wow that's a really good time! I could never do something like that, I just don't have the endurance..."
    the_person "Yeah, I've been running since I was little. I don't know why, I've just always loved it! But I know it's not for everyone."
    if yoga_assistant.has_large_tits:
        if yoga_assistant is sarah:
            yoga_assistant "Yeah... I recently, umm... filled out a bit... Running long distances isn't really practical with these!"
            "[yoga_assistant.title] gives her pleasantly [yoga_assistant.tits_description] a shake."
        else:
            yoga_assistant "I've been keeping in shape by doing some exercises, but I'm not there yet."
            the_person "Hey, I'm glad you're still taking steps to stay fit though. You gotta work with the assets you've been given!"
        "The girls share a laugh."
    else:
        yoga_assistant "Yeah. Everyone is different. This class is going to be great though! I think with time and some training, just about everyone can get something out of yoga!"
        the_person "I agree! No one can do everything... Sometimes you just have to work with the assets you've been given!"
        "The girls share a laugh."

    "Okay ... [yoga_assistant.title] and [the_person.possessive_title] seem to REALLY be hitting it off. You make a mental note. You walk up to the front and greet them."
    mc.name "Hello [the_person.title] and [yoga_assistant.title]. Looks like this is going to be a good training class!"
    the_person "Oh hey [the_person.mc_title]!"
    the_person "I'm glad to see you. I wasn't sure if you were going to be here or not."
    yoga_assistant "Hello [yoga_assistant.mc_title]! The man of the hour! Here to make sure company funds are being spent wisely?"
    "[the_person.title] chuckles."
    mc.name "I have no doubt that you two will make this class a success. I'm just here to make sure all the first session jitters get worked out and to lend a hand if any problems arise."
    the_person "Thanks, [the_person.mc_title]. I really appreciate your support with this. It's just a yoga class, but having you here definitely helps me feel more confident trying to tackle this!"
    yoga_assistant "Yeah, don't worry [the_person.fname], [mc.name] is a great guy to work for! He really knows how to treat his employees!"
    mc.name "Alright, I'll be over there, getting some of the morning paperwork started. Let me know if you need anything."
    "You head to the side of the room and sit down at a computer terminal. You pull up some serum designs and get to work, analyzing them. After a bit, you glance up when you hear [the_person.possessive_title] starting things up."
    the_person "Good morning everyone! Thanks for coming out. Since today is our first session, we are going to start out with just some basic poses and breathing techniques! Does anyone have any questions before we get started?"
    "You watch as your employees start out doing some light stretching. Everyone seems to be paying attention and trying their best."
    "This really does seem like it could be a good benefit for your employees who are willing to come out a bit early. You turn back to the computer and get to work."
    call erica_yoga_loop_label(the_person, yoga_assistant) from _erica_yoga_loop_call_01
    "As you finish up with your work, you hear [the_person.title] calling out instructions for the cool down. Sounds like the yoga session is wrapping up as well. The girls finish and start rolling up their mats."
    $ scene_manager.add_actor(the_person)
    "You walk up to [the_person.possessive_title]."
    mc.name "Congratulations, that seemed like a very successful first meeting!"
    the_person "Thank you!"
    call erica_getting_watched_reaction_label(the_person, _return) from _erica_gets_watched_during_yoga_intro_01
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    yoga_assistant "Alright, I know everyone is thirsty. Anyone who needs water, head for the break room."
    "You can hear [yoga_assistant.possessive_title] calling out. The room starts to clear. She walks over to you and [the_person.possessive_title]."
    yoga_assistant "That went great!"
    "[yoga_assistant.title] seems pretty enthusiastic."
    the_person "You think so? I honestly wasn't sure... But it seemed like everyone did well."
    "[the_person.possessive_title] seems a little apprehensive, but you think she probably just needs to build some confidence."
    mc.name "Well, is there anything I can do to help for next time?"
    "[the_person.title] thinks about it for a bit, but [yoga_assistant.possessive_title] quickly speaks up."
    yoga_assistant "It's actually kind of a pain, having to go all the way to the break room to get water. Maybe we could get one of those 5 gallon water dispensers?"
    "It's not THAT hard to just walk to the break room... But at the same time, if you had a water source that all the girls at the yoga session used, you could dose it with serum and every girl attending would get some..."
    mc.name "Can you get that ordered and just put it on the company account?"
    yoga_assistant "Yes sir!"
    mc.name "Also, could you make sure [the_person.title] gets paid? For now her standard fee is $100 per session."
    yoga_assistant "Sure thing!"
    mc.name "One last thing... I think I'd like to follow your previous request, and add yoga as a topic to discuss with employees at our HR meetings."
    mc.name "With a little work, I think we could really make something special here."
    "You say goodbye to [the_person.title] and [yoga_assistant.title]. They turn and walk off, with [the_person.possessive_title] following so they can work out payment details. You can hear them chattering as they start to walk off."
    the_person "You did great! I was overall really impressed with all the girls who came. Seems like most of the girls here take care of themselves..."
    yoga_assistant "Yeah, but not all of them were here today... Hopefully I can drag more of them out here next week..."
    "It seems the two girls have struck up a friendship. You wonder how things will develop between them."
    $ town_relationships.update_relationship(the_person, yoga_assistant, "Best Friend")

    python:
        # setup yoga events
        erica.event_triggers_dict["yoga_sessions_started"] = True
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)

        # cleanup yoga class
        yoga_list.append(yoga_assistant) #Add assistant to yoga list to make sure she gets appropriate energy increase and outfit cleanup.
        erica_after_class_outfit_cleanup(yoga_list) #NOTE we rely on Erica moving to gym next to make sure her outfit gets cleaned up.
        erica_class_energy_increase(yoga_list)

        # make sure we set the schedule right (fixes room change)
        the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
        yoga_assistant.set_override_schedule(lobby, the_days = [1], the_times =[0])

        scene_manager.clear_scene()
        yoga_list = None
        yoga_assistant = None


    call advance_time(no_events = True) from _call_advance_time_erica_yoga_intro
    return

label erica_yoga_loop_label(the_person, yoga_assistant):
    python: # init loop
        scene_manager.clear_scene(reset_actor = False)
        slutty_class = erica_get_class_average_sluttiness(yoga_list) > 50
        nude_class = erica_get_is_yoga_nude()
        back_row = erica_get_back_of_class(yoga_list)
        erica_num_watched = 0
        erica_only_watch = False

    "As you start your morning paperwork, you come across a personnel list of possible personality conflicts from the HR department."
    "If you focus on this, you could probably improve company efficiency by quite a bit."
    "As you listen, you hear [the_person.possessive_title] begin the warmups. Maybe you should just sit back and watch the girls do their yoga, too?"
    "[back_row[0].title], [back_row[1].title], and [back_row[2].title] are the three girls in the back, closest to where you are."
    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall):
        "However, something about [erica.possessive_title] really grabs your attention."
        "You've been getting closer and closer to her lately. Despite the women in the room, you feel like you can barely take your eyes off of her."
        $ erica_only_watch = True
    elif nude_class:
        "However, with the class being nude... surely work can get done at another time, right?"
    elif slutty_class:
        "The outfits that you've seen around the room... a lot of them really draw your attention. The class has been getting sluttier and sluttier each week..."
    $ the_pose = get_random_from_list(erica_yoga_poses)
    menu:
        #"Work on efficiency (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
        #    pass
        "Watch [the_person.title]":
            "You look up and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
            $ switch_to_class_front(the_person, yoga_assistant, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."
            $ erica_num_watched += 1
        "Watch the class" if not erica_only_watch:
            "You decide to watch the girls in their class instead. How often do you get the chance to watch a show like this?"
            $ switch_to_back_of_class(back_row, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."

    $ scene_manager.clear_scene(reset_actor = False)
    "You decide to pull up one of the recent medical journals that you usually read."
    "You stumble across an article that has some interesting implications with one of the serums you recently began testing."
    "If you read the article, it might help reduce the number of side effects that serum usually has."
    "Before you start reading, you can hear [the_person.title] calling out more instructions. The girls are starting to get into the yoga session!"
    "Maybe you should watch it..."
    if erica_only_watch:
        "Once again, your eyes are drawn to [the_person.possessive_title]. Her sexy form looks so good doing the different poses, you can't look away."
    elif nude_class:
        "Sweat is beginning to form a sheen on the stunning nude bodies that are presented to you in incredible poses."
        "You note that several of the girls are occasionally touching themselves between poses, pulling at hard nipples and stroking increasingly wet cunts."
    elif slutty_class:
        "Some of the girls are starting to work up a good sweat, giving a nice shine to their nubile bodies."
    $ the_pose = get_random_from_list(erica_yoga_poses)
    menu:
        #"Work on research (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
        #    pass
        "Watch [the_person.title]":
            "You look up and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
            $ switch_to_class_front(the_person, yoga_assistant, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."
            $ erica_num_watched += 1
        "Watch the class" if not erica_only_watch:
            "You decide to watch the girls in their class instead. Your eyes are treated to the girls in the back of the class."
            $ switch_to_back_of_class(back_row, the_pose)
            $ display_yoga_dialog(the_pose)
            "You watch for a while, but soon turn your attention back to the computer."

    # SHORTENED LOOP BY ONE SCENE, it gets tedious watching it over and over.
    # $ scene_manager.clear_scene(reset_actor = False)
    # "You decide to pull up a list of suppliers for some of your chemical components."
    # "As you look at a few of their websites, you discover that one of them is dumping stock of a component they accidentally over produced!"
    # "If you order it right now, you could get a bunch of supplies at a steeply discounted rate."
    # "Before you make the order, you can hear [the_person.title] encouraging the class to keep with it. The yoga session is getting intense!"
    # "Maybe you should watch it..."
    # if nude_class:
    #     "When you glance up, sexual tension in the room is really ramping up."
    #     "A couple girls are now actively making out, and another pair are doing their poses so close together their bodies are rubbing against each other."
    # elif slutty_class:
    #     "The sound of heavy breathing and gasps coming from the class makes it hard to pay attention to the computer terminal."
    # $ the_pose = get_random_from_list(erica_yoga_poses)
    # menu:
    #     "Work on supply (disabled)": #We aren't here to get work done! Probably actually make this possible in the future though.
    #         pass
    #     "Watch [the_person.title]":
    #         "You look up at and see [the_person.possessive_title] and [yoga_assistant.title] near the front of the class."
    #         $ switch_to_class_front(the_person, yoga_assistant, the_pose)
    #         $ display_yoga_dialog(the_pose)
    #         $ erica_num_watched += 1
    #     "Watch the class":
    #         "You can't help it, this might be your last chance for today to watch the girls posing. You look up at the class and watch intently"
    #         $ switch_to_back_of_class(back_row, the_pose)
    #         $ display_yoga_dialog(the_pose)

    # if mc.arousal_perc <= 10:
    #     "The class is wrapping up now, and you feel pretty good about the amount of work you were able to get done."
    # elif mc.arousal_perc <= 30:
    #     "The class is wrapping up now. You didn't get as much done as you would have liked, but the views from where you were sitting were worth it!"
    # elif mc.arousal_perc <= 60:
    #     "The class is wrapping up now. Your erection is hard to ignore after watching the girls do all kinds of sexy poses."
    # else:
    #     "The class is wrapping up now. It appears to be degenerating into an outright orgy. You consider joining the fray."

    python:
        # cleanup loop
        scene_manager.clear_scene(reset_actor = False)
        back_row = None

    return erica_num_watched

label erica_weekly_yoga_label(the_person):
    if not erica.is_available:
        call erica_no_yoga_session_this_week() from _call_erica_no_yoga_session_this_week_1
        return

    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event

        the_person = erica
        yoga_assistant = erica_get_yoga_assistant()
        yoga_list = erica_get_yoga_class_list()
        schedule_assistant = True

        erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)

    "As you walk into the lobby, you see the now-familiar sight of some of your employees gathering for their weekly yoga session."
    if erica_get_is_yoga_nude():
        "The girls are all naked, as has been previously decided. Nude yoga is probably your favorite spectator sport right now."

    $ scene_manager.add_actor(the_person)
    if not yoga_assistant.available:
        mc.name "Hey [the_person.title], I see [yoga_assistant.name] is not here today?"
        the_person "Yeah, [yoga_assistant.name] couldn't make it this week."
        $ yoga_assistant = erica_get_alternative_assistant(yoga_list)
        $ erica_apply_yoga_outfit_to_class([yoga_assistant])
        the_person "But [yoga_assistant.name] is filling in for her."
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
        $ schedule_assistant = False
    else:
        $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
        "At the front, you see [the_person.possessive_title] doing some light stretching. She has a speaker out, playing some upbeat music."
        "Next to her you see [yoga_assistant.title]. They have become good friends and are chatting idly as you walk up."
        the_person "Oh hey [the_person.mc_title]!"

    if not erica_get_is_yoga_nude() and erica_get_class_average_sluttiness(yoga_list) > 80: #Average class sluttiness is super slutty. They want to do it nude from now on
        the_person "I'm glad you're here. Several of the girls have approached me about something, but I wanted to run it by you before it became an official policy."
        the_person "The class and I both agree, this is a great, safe place to celebrate the feminine form and what we are capable of."
        the_person "It has been requested by multiple people here that our yoga sessions adopt an au naturel dress code."
        yoga_assistant "Because the office is currently closed, this technically falls outside of the employee uniform requirements..."
        yoga_assistant "But we decided that it would probably be better to run it by you before me make it official. It IS your office building, after all!"
        $ mc.change_locked_clarity(20)
        "Holy fuck, they want to do yoga in the nude. You rack your brain, trying to think of a logical reason to say no. Only one thing comes to mind."
        mc.name "Umm... I think I'm okay with that... except... Everyone still needs to wear shoes."
        the_person "Shoes?"
        mc.name "If there is a nail or something that happens to be on the floor, I don't want to be held liable in case someone gets injured."
        yoga_assistant "Oh! That makes total sense."
        the_person "This is great! I'll make an announcement."
        "[the_person.possessive_title] raises her voice extra loud so everyone in the room can hear it."
        the_person "Hey everyone! Good news! We just got the okay, from now on - in celebration of the female body - this will be a nude yoga class!"
        "You hear several cheers go up from the group."
        "You notice that [yoga_assistant.possessive_title] has already started to strip down..."
        $ scene_manager.strip_full_outfit(person = yoga_assistant)
        $ mc.change_locked_clarity(20)
        the_person "We only ask, please leave your shoes on! This is a safety issue, in case a piece of glass or other object is left on the floor!"
        "When she finishes the announcement, [the_person.title] starts to strip down also."
        $ scene_manager.strip_full_outfit(person = the_person)
        $ mc.change_locked_clarity(20)
        "You look around and watch as the all the girls are also stripping. It is a surreal moment."
        # "You walk over to the computer terminal in a daze. You sit down, and let the girls get started in their official, company sponsored, all nude yoga class."
        $ the_person.event_triggers_dict["nude_yoga"] = True
        $ erica_apply_yoga_outfit_to_class([the_person, yoga_assistant] + yoga_list)

    else:
        $ class_size = __builtin__.len([the_person, yoga_assistant] + yoga_list)
        the_person "Glad you could make it! We are just getting ready to get started."
        yoga_assistant "Hello [yoga_assistant.mc_title]! I was just getting ready to fill up the water jug for the attendants."
        "You consider offering to fill it for her. It would give you a chance to distribute a dose of serum to all [class_size] of the girls gathered."
        menu:
            "Fill it for her\n{color=#00FF00}{size=18}Give class serum{/size}{/color}":
                call screen serum_inventory_select_ui(mc.inventory)
                if isinstance(_return, SerumDesign):
                    $ the_serum = _return
                    if mc.inventory.get_serum_count(the_serum) > __builtin__.len([the_person, yoga_assistant] + yoga_list):
                        "You decide to add [class_size] doses of [the_serum.name] to the water jug. You quickly return and place it on the counter."
                        $ dose_yoga_class_with_serum([the_person, yoga_assistant] + yoga_list, the_serum)
                    else:
                        "You have insufficient doses to make the serum effective in that much water."
                        "You quickly return with the water jug with absolutely no serum in it and place it on the counter."
                    $ the_serum = None
                else:
                    "You quickly return with the water jug with absolutely no serum in it and place it on the counter."
            "Chat with [the_person.title]":
                mc.name "Don't let me keep you."
                yoga_assistant "Right..."
                "[yoga_assistant.title] grabs the jug and leaves the room."
                $ scene_manager.hide_actor(yoga_assistant)
                "You turn to [the_person.title]."
                mc.name "Thank you again for doing this. I really feel like this is a huge benefit for the company."
                the_person "Of course! Glad to do it. I get the feeling from talking to the girls here that you are a great boss to work for, too!"
                mc.name "Alright, I'll let you get to it. I'm going to try and get some work done, let me know if you need anything."

    "You head to the side of the room and sit down at a computer terminal. You pull up some serum designs and get to work, analyzing them. After a bit, you glance up when you hear [the_person.possessive_title] starting things up."
    the_person "Good morning everyone! Thanks for coming out. We are going to start things out slowly this morning with some stretching!"
    "You watch as your employees start out doing some light stretching. Everyone seems to be paying attention and trying their best."
    "You turn back to the computer and get to work."
    call erica_yoga_loop_label(the_person, yoga_assistant) from _erica_yoga_loop_call_02
    if erica_get_is_yoga_nude():
        "As the all-nude yoga session finishes, several girls are REALLY celebrating the feminine form."
        "As you walk over to [the_person.possessive_title], you pass a pair of girls in a sixty-nine, moaning as they eat each other out."
        "Another couple are on their hands and knees, ass to ass... with a double-sided dildo? Where the hell did that come from?"
    else:
        "As you finish up with your work, you hear [the_person.title] calling out instructions for the cool down. Sounds like the yoga session is wrapping up as well. The girls finish and start rolling up their mats."
    $ scene_manager.add_actor(the_person)
    "You walk up to [the_person.title]."
    mc.name "Looks like another highly successful yoga class."
    the_person "Thank you!"
    "She has a definite hint of pride in her voice."
    call erica_getting_watched_reaction_label(the_person, _return) from _erica_gets_watched_during_yoga_recurrent_01
    $ scene_manager.add_actor(yoga_assistant, display_transform = character_center_flipped)
    "As you are talking, [yoga_assistant.title] walks up to you."
    yoga_assistant "Great class!"
    $ remaining_person = None
    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall): #Love scene
        mc.name "[the_person.title], could you come to my office for a minute? I have some ideas for additional things you could do during the session."
        the_person "Oh, sure! I have some time before my first class."
        yoga_assistant "Ah, guess I'll get to work then."
        $ scene_manager.remove_actor(yoga_assistant)
        call erica_post_yoga_love_label() from _erica_60_love_post_yoga_scene_01
    elif mc.arousal_perc >= 30: #Use 30 so that this is possible from the start
        "Unfortunately, there is no hiding your erection from the duo. Watching the class has you way too excited."
        if willing_to_threesome(the_person, yoga_assistant) and renpy.random.randint(0,2) == 0: #Give a chance, if possible, to get a double blowjob after the show
            "[yoga_assistant.title] is blatantly gawking at your tent, when [the_person.title] speaks up."
            the_person "Yup, there's only one thing left to do!"
            mc.name "Oh? What's that?"
            the_person "The best way to make gains after a workout is with a shot of protein!"
            "[the_person.possessive_title] is clearly referencing your cum."
            yoga_assistant "Oh! That sounds good! Can I get some too?"
            mc.name "I think there's enough for both of you. Let's step into my office really quick."
            "The duo quickly follow you to your office. As you walk in, you turn and lock the door."
            $ mc.change_location(ceo_office)
            "Before you can say anything, the girls are already getting down on their knees, ready to earn their protein."
            "You take out your cock and let them get to work."
            call start_threesome(the_person, yoga_assistant, start_position = threesome_double_blowjob, position_locked = True) from _after_yoga_protein_yum_1
            $ the_report = _return
            if the_report.get("guy orgasms", 0) > 0:
                "You enjoy your post-orgasm bliss for a few moments while [the_person.possessive_title] and [yoga_assistant.possessive_title] swap your cum back and forth for a bit."
                "When you look back down, they seem to have swallowed most of it, but [yoga_assistant.title] is licking the last few remnants of your cum off of [the_person.possessive_title]'s face."
            $ scene_manager.update_actor(the_person, position="stand3", display_transform = character_center_flipped)
            $ scene_manager.update_actor(yoga_assistant, position = "stand4", display_transform = character_right)
            "The girls stand back up."
            mc.name "God, what a way to start the day."
            yoga_assistant "I know! Starting the day off right."
            the_person "Yeah. Sorry, but I need to get going. [yoga_assistant.name], did you want to hang out later this week?"
            yoga_assistant "I'll have to text you later, I'm not sure yet."
            the_person "Ok! " #Make a small chance, if possible, to have a threesome.
        elif renpy.random.randint(0,1) == 0:
            if the_person.sluttiness > 40:
                "[the_person.title] looks at you longingly, but you can tell she has to get going."
            the_person "Sorry, I really need to get going."
            "As she starts to walk by you, she whispers in your ear."
            the_person "If you need help with that later, swing by the gym..."
            $ mc.change_locked_clarity(10)
            "She walks off leaving you with [yoga_assistant.title]."
            $ scene_manager.remove_actor(the_person)
            $ remaining_person = yoga_assistant
            # call erica_after_yoga_office_session_label(yoga_assistant) from _sarah_after_yoga_fun_01
        else:
            if yoga_assistant.sluttiness > 40:
                "[yoga_assistant.title] looks at you longingly, but you can tell she has to get going."
            yoga_assistant "Sorry, I really need to get going."
            "As she starts to walk by you, she whispers in your ear."
            yoga_assistant "If you need help with that, I'm sure we can find a private place after the workday starts..."
            $ mc.change_locked_clarity(10)
            "She walks off leaving you with [the_person.title]."
            $ scene_manager.remove_actor(yoga_assistant)
            $ remaining_person = the_person
            # call erica_after_yoga_office_session_label(the_person) from _erica_after_yoga_fun_01

        if remaining_person:
            if remaining_person.effective_sluttiness() > 40:
                "[remaining_person.title] looks at you, smiling."
                remaining_person "Guess it's just you and me. Why don't we find somewhere... private?"
                $ threesome_partner = get_random_from_list(yoga_list)
                menu:
                    "Head to your office":
                        mc.name "I know just the place."
                        call erica_after_yoga_office_session_label(remaining_person) from _erica_after_yoga_fun_01
                    "Ask [threesome_partner.title] to join" if erica_get_is_yoga_nude() and willing_to_threesome(remaining_person, threesome_partner):
                        mc.name "Private? Look around... why would we have to go somewhere private?"
                        remaining_person "Ah, okay."
                        "Off to one side, you see [threesome_partner.possessive_title], apparently taking a break by herself."
                        mc.name "Let's go over there and have some fun with [threesome_partner.title]."
                        remaining_person "Sounds good! I'll follow your lead!"
                        "You and [remaining_person.title] walk over to [threesome_partner.title]. Her eyes light up when she sees the two of you approaching her."
                        $ scene_manager.add_actor(threesome_partner, display_transform = character_left)
                        threesome_partner "Hello! I was just getting ready to get to work, sir..."
                        mc.name "No need for that yet. Let's have a little fun first."
                        threesome_partner "Yay! I was hoping you would say that!"
                        call start_threesome(remaining_person, threesome_partner) from _nude_yoga_aftermath_threesome_01
                        "Satisfied for now, you decide to get cleaned up and ready for work."
                        call erica_nude_yoga_office_aftermath_label() from _nude_yoga_lobby_survey_01
                    "Decline":
                        mc.name "Sorry, but the workday is approaching quickly. I have a lot to get done today."
                        $ remaining_person.change_happiness(-3)
                        remaining_person "Wow... okay, I guess..."
                        "Rejected, [remaining_person.possessive_title] quickly walks off."
            else:
                "[remaining_person.title] gives you a shy smile."
                remaining_person "Well... I, umm... I'm glad you enjoyed the class. I should probably get going as well..."

    elif erica_get_is_yoga_nude(): #You didn't really watch, but the girls having sex all around you is distracting.
        "You try to make conversation with the duo, but the sounds of sex building in the room is getting to be distracting."
        yoga_assistant "It's amazing, isn't it? A group of women, getting together, getting empowered, taking their pleasure into their own hands."
        mc.name "Yes, it's amazing for sure."
        if willing_to_threesome(the_person, yoga_assistant):
            the_person "I have some time before I have to get to class... want to mess around some?"
            yoga_assistant "Oh! Yeah, me too, me too!"
            "The girls look at you, hungrily. It is clear they want to have some fun with you before they clean up."
            menu:
                "Have a threesome":
                    "The girls watch you hungrily as you get undressed. When you take your underwear off, your cock springs free."
                    call start_threesome(the_person, yoga_assistant) from _nude_yoga_aftermath_threesome_02
                    "Satisfied for now, you decide to get cleaned up and ready for work."
                    the_person "Mmm, that was great!"
                    yoga_assistant "Hey [the_person.fname], did you want to get together this weekend?"
                    the_person "I'm not sure yet, I'll have to see how much homework I get! I'll text you."
                    "It's been amazing witnessing the two girls develop such a deep friendship."
                    call erica_nude_yoga_office_aftermath_label() from _nude_yoga_lobby_survey_02
                "Decline":
                    mc.name "Sorry, but the workday is approaching quickly. I have a lot to get done today."
                    $ the_person.change_happiness(-3)
                    $ yoga_assistant.change_happiness(-3)
                    yoga_assistant "Wow... okay, I guess..."
                    the_person "Your loss!"
                    "Rejected, [remaining_person.possessive_title] quickly walks off."
                    yoga_assistant "Guess we'll just have some fun without you..."
                    $ scene_manager.update_actor(the_person, position = "kissing")
                    $ scene_manager.update_actor(yoga_assistant, position = "walking_away", display_transform = character_right)
                    "The two girls embrace each other and start to kiss as you walk away."
        elif the_person.sluttiness > 40 and yoga_assistant.sluttiness > 40:
            "The two girls look at you a bit awkwardly, as if waiting for you to do something."
            the_person "So... umm... you want to do anything, [the_person.mc_title]?"
            yoga_assistant "Yeah... I mean... didn't you want to talk to me, in your office or something?"
            "The girls seem to want you to pick one of them."
            menu:
                "Private time with [the_person.title]":
                    "You're right [the_person.title]. Do you have a minute? I need to discuss something with you in my office."
                    $ the_person.change_stats(happiness = 5, love = 3)
                    $ yoga_assistant.change_stats(happiness = -5, love = -3)
                    the_person "Oh! Yeah I definitely have some time."
                    "[yoga_assistant.possessive_title] clearly looks a little rejected."
                    yoga_assistant "I guess I'll get to work..."
                    call erica_after_yoga_office_session_label(the_person) from _erica_after_yoga_fun_02
                "Private time with [yoga_assistant.title]":
                    "You're right [yoga_assistant.title]. I have a problem with some time sheets. I printed them in my office, can you follow me?"
                    $ the_person.change_stats(happiness = -5, love = -3)
                    $ yoga_assistant.change_stats(happiness = 5, love = 3)
                    yoga_assistant "Oh! Yeah, I remember now! Let's go."
                    "[the_person.possessive_title] clearly looks a little rejected."
                    the_person "I guess I'll get to the university..."
                    call erica_after_yoga_office_session_label(yoga_assistant) from _erica_after_yoga_fun_03
                "Get to work":
                    mc.name "I'm sorry, I have some work that I need to accomplish. The session today was great though. Keep up the good work you two!"
                    "They both look at you disappointed, but nothing more comes of it. You say your goodbyes and soon you are starting your workday."
        else:
            "Awkwardly, you decide it would be best to get to work."
            mc.name "I'm sorry, I have some work that I need to accomplish. The session today was great though. Keep up the good work, you two!"
            "They are both watching the orgy unfolding. You say your goodbyes and soon you are starting your workday."
        $ the_person.change_stats(slut = 1, max_slut = 70)
        $ yoga_assistant.change_stats(slut = 1, max_slut = 70)
    else:
        the_person "Yeah, that was great!"
        yoga_assistant "Hey [the_person.fname], did you want to get together this weekend?"
        the_person "I'm not sure yet, I'll have to see how much homework I get! I'll text you."
        "It's been amazing witnessing the two girls develop such a deep friendship. You decide it is time for you to start your workday proper now also."
    python:
        # setup next event
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)
        remaining_person = None
        threesome_partner = None
        # cleanup yoga class
        yoga_list.append(yoga_assistant) #Add assistant to yoga list to make sure she gets appropriate energy increase and outfit cleanup.
        erica_after_class_outfit_cleanup(yoga_list)
        erica_class_energy_increase(yoga_list)

        # make sure we set the schedule right (fixes room change)
        the_person.set_override_schedule(lobby, the_days = [1], the_times = [0])
        if schedule_assistant:
            yoga_assistant.set_override_schedule(lobby, the_days = [1], the_times =[0])

        scene_manager.clear_scene()
        yoga_list = None
        yoga_assistant = None

    call advance_time(no_events = True) from _call_advance_time_erica_yoga_weekly_recurring
    return

label erica_no_yoga_session_this_week():
    python: # setup yoga class
        scene_manager = Scene() # only use one scene manager per event
        yoga_assistant = erica_get_yoga_assistant()

    if not yoga_assistant.is_available:
        "As you walk into the lobby, you expected to see the yoga class, but nobody is here."
        "You suddenly remember that [erica.possessive_title] is not available and they probably rescheduled the class."
    else:
        $ scene_manager.add_actor(yoga_assistant)
        mc.name "Hey [yoga_assistant.title], no class today?"
        yoga_assistant "Hey [yoga_assistant.mc_title], nah, [erica.fname], couldn't make it today, we rescheduled to next week."
        mc.name "Ok, thanks."

    python:
        # setup next event
        erica.add_unique_on_room_enter_event(erica_weekly_yoga)
        scene_manager.clear_scene()
        yoga_assistant = None
    return


label erica_getting_watched_reaction_label(the_person, watched_count = 0): #A short label to describe how Erica feels when you watch her doing yoga.
    if watched_count == 0:
        return # we didn't look at her

    if erica.love >= 60 and not erica_post_yoga_fuck_complete() and erica.is_willing(against_wall):
        the_person "So... enjoy the class? Or did you even notice there were other girls in the room?"
        "She is blushing heavily and looking down."
        mc.name "What can I say, I really enjoyed watching the class, but watching the instructor in particular. Her form is fantastic."
        "She gives you a genuine smile, but otherwise doesn't say anything."
        $ the_person.change_stats(love = 3, slut = 2, max_slut = 40)
    elif (watched_count * 20) + 10 > the_person.effective_sluttiness(): #She is embarrassed how much you watched her. sluttiness gain.
        if watched_count == 1:
            the_person "I couldn't help but notice you sneaking glances at me... during the session."
            "She is blushing slightly."
            mc.name "Sorry, being in the same room as you doing yoga is a little bit distracting."
            the_person "It's okay! I actually don't mind. That's totally normal, right?"
            mc.name "Of course."
            $ the_person.change_stats(love = -1, slut = 1, max_slut = 30)
        # elif watched_count == 2:
        #     the_person "I couldn't help but notice you looking at me during the session."
        #     "She is blushing."
        #     mc.name "You're a beautiful woman, [the_person.title]. I'm sorry, I'll try not to stare so much next time."
        #     the_person "It's okay! I mean, I guess that's pretty normal, considering the circumstances."
        #     $ the_person.change_stats(happiness = 2)
        else:
            the_person "I couldn't help but notice you staring at me the entire session. I could feel your eyes every time I posed..."
            "She is blushing heavily and looking down."
            mc.name "I'm sorry. You're a sexy woman, and having you in the same room doing yoga is very distracting."
            "She smiles at you, but you can tell she is a little uncomfortable."
            the_person "It's okay I guess... considering the circumstances."
            $ the_person.change_stats(love = -3, slut = 2, max_slut = 40)
    else:
        if watched_count == 1:
            the_person "I couldn't help but notice you sneaking glances at me during the session."
            "She is smiling at you."
            the_person "It's kind of nice, having you here to watch. Did you like what you saw?"
            mc.name "Of course. You're very flexible, and a great yoga instructor."
            the_person "Aww, thank you."
            $ the_person.change_stats(love = 1, happiness = 1, slut = 1, max_slut = 20, add_to_log = False)
        # elif watched_count == 2:
        #     the_person "I couldn't help but notice you looking at me during the session."
        #     "She is smiling wide."
        #     the_person "I can't say I blame you. Should I assume from the drool that was coming out of the side of your mouth that you liked what you saw?"
        #     mc.name "Definitely. You have a great figure, and being in the same room during yoga, I couldn't help but watch."
        #     the_person "Aww, you're sweet."
        #     $ the_person.change_stats(love = 2, happiness = 2)
        else:
            the_person "I couldn't help but notice you staring at me the entire session. I could feel your eyes every time I posed..."
            "She is giving you a mischievous smile."
            if erica_get_is_yoga_nude():
                the_person "I love the atmosphere in here, with everyone naked. But I love it even more that your eyes were glued to me the entire time."
                mc.name "I can't help it, your figure is absolutely stunning."
                the_person "Thank you... do you think we have time to help you take care of... this?"
                $ mc.change_locked_clarity(20)
                "She puts her hand on your erection and gives it a few strokes."
            else:
                the_person "I could feel you undressing me with your eyes every time I posed."
                "She lowers her voice to a soft growl."
                the_person "Maybe later you can undress me with your hands."
                mc.name "Don't worry, I intend to."
            $ the_person.change_stats(happiness = 3, love = 3, slut = 2, max_slut = 50,add_to_log = False)
    return

label erica_post_yoga_love_label():
    "You head to your office, bringing [the_person.possessive_title] with you. You open the door, walk in, then close and lock it behind you."
    $ mc.change_location(ceo_office)
    the_person "So... what was it you wanted to talk abo... AH!"
    "You quickly grab her and pin her to the wall."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_right)
    $ mc.change_locked_clarity(20)
    "She wraps her arms around you and you start to make out, your mouths meeting and exploring each other."
    "[the_person.title] moans when she feels your erection pressing against her."
    $ the_person.change_arousal(20)
    # $ initial_outfit = the_person.outfit.get_copy() # store outfit
    mc.name "I'm sorry I couldn't stop staring at you. Watching your sexy body all morning has me so worked up... I need you right now!"
    the_person "Oh god, me too!"
    "You don't have the patience to wait any longer, you are going to fuck her right here against the wall."
    if the_person.vagina_available:
        "You quickly pull your cock out and put it in between her legs, getting it into position."
    else:
        "You quickly move away every piece of cloth between you and [the_person.possessive_title]'s cunt."
        $ scene_manager.strip_to_vagina(person = the_person, prefer_half_off = True)
        "You pull your cock out and put it in between her legs, getting it into position."
    $ scene_manager.update_actor(the_person, position = "against_wall")
    $ mc.change_locked_clarity(30)
    "She lifts one leg to give you better access. Your grab her ass with both hands, lifting her up slightly."
    "She looks you right in the eyes as you slowly lower her, your cock sliding inside her. She gasps as you bottom out inside of her."
    the_person "Oh fuck... we forgot... we forgot a condom!"
    mc.name "Want me to stop?"
    the_person "No! Oh god, just promise me you'll pull out, okay?"
    mc.name "I'll try."
    the_person "You'll try? Oh my god..."
    $ the_person.change_arousal(20)
    "All she can do is cling to you as you start to fuck her."
    call fuck_person(the_person, start_position = against_wall, private = True, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_fuck_erica_after_yoga_01
    $ the_person.draw_person(position = "stand4")
    if the_person.has_creampie_cum:
        the_person "Oh god, you were supposed to pull out!"
        $ the_person.change_love(-2)
        "Your cum is dribbling down between her legs."
        if the_person.on_birth_control:
            the_person "You have got to be more careful... thankfully I'm on birth control..."
        else:
            the_person "I'm not on birth control! I'll have to get a plan B before class..."
        mc.name "I'm sorry, I just couldn't help it, you are so amazing."
        the_person "I'm a little mad... but it's okay. You just really need to do a better job controlling yourself if this is gonna work!"
    else:   #Check and make sure MC finished before this
        the_person "Wow, I don't know what came over you, but then YOU came over ME, and it was amazing."
        $ the_person.change_love(2)
        the_person "I know that was really sudden, but thanks for not cumming inside me. I really can't get pregnant right now."
        the_person "I need you to have some self control if this is gonna work!"
    mc.name "If what is going to work?"
    the_person "I ummm... errmm... I mean..."
    "She stutters, suddenly realizing what she said. Then she sighs."
    the_person "I guess I mean us? Like, we've gotten really close lately... tell me it isn't just me feeling this way?"
    menu:
        "I feel the same way":
            the_person "Yes! Oh god, you have no idea how happy I am to hear that."
            $ the_person.change_stats(happiness = 15, love = 5)
            "She kisses you, and you kiss her back."
            the_person "So like... are we official now? I can call you my boyfriend?"
            mc.name "Yes that would be appropriate."
            $ the_person.add_role(girlfriend_role)
            the_person "Yay! Oh my god, this is great!"

        "Let's just be friends":
            the_person "Ah... okay wow, I guess I was just... totally misinterpreting things between us..."
            $ the_person.change_stats(happiness = -15, love = -20)
            the_person "I didn't realize you just wanted things to be strictly physical between us. Is that what you want? Friends with benefits?"
            mc.name "Yes that is what I am looking for right now."
            the_person "Okay... I'm sorry I didn't realize. But I think I can manage that."
    "Suddenly, [the_person.possessive_title] checks the time."
    the_person "Oh fuck! I have to get to class!"
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    if the_person.is_girlfriend:
        the_person "I'll see you around, I'm sure! If you get busy I'll still be over on Saturday night!"
    else:
        the_person "Well, I'll see you around."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns around and opens the door to your office, leaving you to begin your work day properly."
    $ erica.event_triggers_dict["post_yoga_fuck"] = True
    return

label erica_after_yoga_office_session_label(the_person): #Theoretically this could be anyone, don't use any specific reference to a person.
    "You head to your office, bringing [the_person.possessive_title] with you. You open the door, walk in, then close and lock it behind you."
    $ mc.change_location(ceo_office)
    "You quickly grab her and pin her to the wall."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_right)
    $ mc.change_locked_clarity(20)
    "She wraps her arms around you and you start to make out, your mouths meeting and exploring each other."
    "[the_person.title] moans when she feels your erection pressing against her."
    $ the_person.change_arousal(20)
    $ initial_outfit = the_person.outfit.get_copy() # store outfit
    menu:
        "Fuck her against the wall" if the_person.is_willing(against_wall):
            "You don't have the patience to wait any longer, you are going to fuck her right here against the wall."
            if the_person.vagina_available:
                "You quickly pull your cock out and put it in between her legs, getting it into position."
            else:
                "You quickly move away every piece of cloth between you and [the_person.possessive_title]'s cunt."
                $ scene_manager.strip_to_vagina(person = the_person, prefer_half_off = True)
                "You pull your cock out and put it in between her legs, getting it into position."
            $ scene_manager.update_actor(the_person, position = "against_wall")
            $ mc.change_locked_clarity(30)
            "She lifts one leg to give you better access. Your grab her ass with both hands, lifting her up slightly."
            "She looks you right in the eyes as you slowly lower her, your cock sliding inside her. She gasps as you bottom out inside of her."
            #TODO relevant you better pull out / cum inside / knock me up / other appropriate dialogue here.
            $ the_person.change_arousal(20)
            "All she can do is cling to you as you start to fuck her."
            call fuck_person(the_person, start_position = against_wall, private = True, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_fuck_after_yoga_01
            $ the_person.call_dialogue("sex_review", the_report = _return)

        "Fuck her against the wall (disabled) " if not the_person.is_willing(against_wall):
            pass
        "Make her service you" if the_person.obedience >= 150:
            "As things are starting to get heated, you slowly back off. You walk over to your desk and sit down at the edge of it, leaving her confused."
            the_person "Sir?"
            "You unzip your pants and take your cock out."
            mc.name "I want you to come take care of this for me."
            if the_person.love < 0:
                the_person "You? What about what I want? I didn't come in here so you could have all the fun."
                mc.name "Shut up, slut. You came in here because you love cock and you know it. If you want to have some fun, then use your pussy. Either way, service me."
                $ the_person.change_stats(obedience = 5, love = -3, slut = 1, max_slut = 50)
                $ mc.change_locked_clarity(20)
                "She looks upset, but you can tell her obedience and her sluttiness are overcoming her reservations."
                the_person "Fine, since you asked so nicely."
                "She spits her last sentence out sarcastically. But it doesn't matter, she starts walking over to you."
                the_person "I'll be damned before I let your cum touch me though."
                call get_fucked(the_person, the_goal = "waste cum", skip_intro = True) from _call_get_fucked_after_yoga_hate_fuck_01
            else:
                the_person "Yes [the_person.mc_title]... with my mouth? or?"
                mc.name "You can use your imagination."
                "She smiles as she starts to walk over to you."
                $ mc.change_locked_clarity(20)
                the_person "Okay! I think I can think of a good way to do this..."
                call get_fucked(the_person, the_goal = "get mc off", skip_intro = True) from _call_get_fucked_after_yoga_get_serviced
        "Make her service you (disabled) " if the_person.obedience < 150:
            pass
        "Have some fun":  # most simple form, she decides how far she is willing to go (she takes control)
            "You reach down and grab her ass, pulling her close to you. Through your pants, you grind your erection against her mound."
            call get_fucked(the_person, allow_continue = False) from _call_get_fucked_after_yoga_get_serviced_02
    "Finished, you get yourself cleaned up and walk over to your desk."
    $ the_person.apply_outfit(initial_outfit)
    $ initial_outfit = None
    $ the_person.draw_person()
    if the_person == erica:
        the_person "Mmm, that was fun! I guess I'll head to class now..."
    else:
        the_person "I suppose I'll get back to work now..."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] puts on her clothes, turns around and opens the door to your office, leaving you to begin your work day properly."
    return

label erica_nude_yoga_office_aftermath_label(): #We use this to describe the state of the lobby after the nude yoga orgy.
    "As the orgy that resulted from the nude yoga class is winding down, you do a quick survey of the lobby."
    "The girls are all winding down. A couple of them are cuddling but most have gotten up and either cleared out or are getting cleaned up."
    "You notice the absolutely undeniable scent of feminine musk in the room. It smells of pussy and sex in the best way possible."
    "You are pretty sure that any employees who weren't at the class this morning will know exactly what happened when they walk in the door."
    "And even if they don't, you're sure that word will get around quick about it."
    return

init 2 python:
    def switch_to_class_front(person_one, person_two, pose):
        # we assume we have a scene manager
        scene_manager.clear_scene(reset_actor = False)
        scene_manager.add_actor(the_person, position = pose)
        scene_manager.add_actor(yoga_assistant, position = pose, display_transform = character_left_flipped)
        return

    def switch_to_back_of_class(back_row, pose):
        transforms = [ character_right, character_center_flipped, character_left ]

        scene_manager.clear_scene(reset_actor = False)
        for idx in range(0, 3):
            # renpy.say(None, "Add actor: " + back_row[idx].name)
            scene_manager.add_actor(back_row[idx], position = pose, display_transform = transforms[idx])

        scene_manager.draw_scene()
        return

    def dose_yoga_class_with_serum(people, serum):
        for person in people:
            mc.inventory.change_serum(serum, -1)
            person.give_serum(copy.copy(serum))
        return
    def erica_get_yoga_class_list():
        yoga_list = []
        for person in [x for x in mc.business.employee_list if x.get_opinion_score("yoga") > 0]:
            if not person is mc.business.hr_director:
                yoga_list.append(person)
        return yoga_list

    def erica_get_alternative_assistant(yoga_class):
        alt = next((x for x in mc.business.employee_list if x not in yoga_class and x.get_opinion_score("yoga") > 0), None)
        if not alt:
            alt = renpy.random.choice(yoga_class)
            yoga_class.remove(alt)
        return alt

    def erica_get_yoga_assistant():
        return Person.get_person_by_identifier(erica.event_triggers_dict.get("yoga_assistant", None))

    def erica_apply_yoga_outfit_to_class(yoga_list):
        for person in yoga_list:
            if erica_get_is_yoga_nude():
                person.apply_yoga_shoes_only()
            else:
                person.apply_yoga_outfit()
        return

    def erica_after_class_outfit_cleanup(yoga_list):
        for person in yoga_list:
            person.apply_planned_outfit()
        return

    def erica_get_class_average_sluttiness(yoga_list):
        if __builtin__.len(yoga_list) == 0:
            return 0

        total_slut = 0
        for person in yoga_list:
            total_slut += person.sluttiness
        return int(total_slut / __builtin__.len(yoga_list))

    def erica_get_back_of_class(yoga_list):
        back_of_class = []
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        back_of_class.append(get_random_from_list([x for x in yoga_list if x not in back_of_class]))
        return back_of_class

    def erica_class_energy_increase(yoga_list):
        for person in yoga_list:
            if person.max_energy < 150:
                person.change_max_energy(3)
        return

    def get_yoga_convince_employee_target():
        eligible_list = [x for x in mc.business.employee_list if x not in erica_get_yoga_class_list() + [mc.business.hr_director]]
        return get_random_from_list(eligible_list)

    def erica_get_is_yoga_nude():
        return erica.event_triggers_dict.get("nude_yoga", False)

    def erica_post_yoga_fuck_complete():
        return erica.event_triggers_dict.get("post_yoga_fuck", False)

    # def erica_check_class_size_and_add_event():
    #     if len(erica_get_yoga_class_list()) < 4:
    #
    #     else:
    #
    #     return
