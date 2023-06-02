#This scene replaces the HR supervisor scene where she services MC at the start of their monday morning meeting.
#Starts out with a blowjob and continues, via the rough order of:
#blowjob    [0]
# titfuck   [1]
# missionary on desk    [2]
# bent over desk    [3]
# anal lapdance [4]
# cum fetish session    [5]
# breeding fetish session   [6]
# anal fetish session   [7]

init 1 python:  #Requirements
    def hr_director_prog_scene_0_req():
        return True

    def hr_director_prog_scene_1_req():
        if mc.business.hr_director != sarah:
            if mc.business.hr_director.has_large_tits and mc.business.hr_director.opinion_score_giving_tit_fucks() > -2:
                return True
        else:
            if sarah_epic_tits_progress() > 1:
                return True
        return False

    def hr_director_prog_scene_2_req():
        if mc.business.hr_director.opinion_score_vaginal_sex() == -2 or mc.business.hr_director.opinion_score_missionary_style() == -2:
            return False
        if mc.business.hr_director.sluttiness >= 60 and (mc.business.hr_director != sarah or sarah_get_sex_unlocked()):
            return True
        return False

    def hr_director_prog_scene_3_req():
        if mc.business.hr_director.opinion_score_vaginal_sex() == -2 or mc.business.hr_director.opinion_score_doggy_style() == -2:
            return False
        if mc.business.hr_director.sluttiness >= 70 and (mc.business.hr_director != sarah or sarah_get_sex_unlocked()):
            if mc.business.hr_director.obedience > 140:
                return True
        return False

    def hr_director_prog_scene_4_req(): #This is actually Sarah's 80 love event
        if mc.business.hr_director is sarah and sarah.love >= 80 and sarah.sluttiness >= 60 and sarah.event_triggers_dict.get("stripclub_progress", 0) >= 1:
            return True
        return False

    def hr_director_prog_scene_5_req():
        return False

    def hr_director_prog_scene_6_req():
        if the_person.has_breeding_fetish and the_person.is_highly_fertile:
            return True
        return False

    def hr_director_prog_scene_7_req():
        return False

    def hr_director_prog_scene_action_req():
        return True


init 2 python:
    def hr_director_prog_scene_compile_scenes(the_progression_scene):
        #TODO
        the_progression_scene.start_scene_list = ["hr_director_prog_scene_intro_0"]
        the_progression_scene.req_list = [hr_director_prog_scene_0_req, hr_director_prog_scene_1_req, hr_director_prog_scene_2_req, hr_director_prog_scene_3_req, hr_director_prog_scene_4_req, hr_director_prog_scene_5_req, hr_director_prog_scene_6_req, hr_director_prog_scene_7_req]
        the_progression_scene.trans_list = ["hr_director_prog_trans_scene_0", "hr_director_prog_trans_scene_1", "hr_director_prog_trans_scene_2", "hr_director_prog_trans_scene_3", "hr_director_prog_trans_scene_4", "hr_director_prog_trans_scene_5", "hr_director_prog_trans_scene_6", "hr_director_prog_trans_scene_7"]
        the_progression_scene.final_scene_list = ["hr_director_prog_scene_scene_0", "hr_director_prog_scene_scene_1", "hr_director_prog_scene_scene_2", "hr_director_prog_scene_scene_3", "hr_director_prog_scene_scene_4", "hr_director_prog_scene_scene_5", "hr_director_prog_scene_scene_6", "hr_director_prog_scene_scene_7"]
        the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    hr_director_prog_scene_action = Action("Hr Director Quality Time", hr_director_prog_scene_action_req, "hr_director_prog_scene_action_label")

    def hr_director_prog_scene_init():
        global hr_director_prog_scene
        hr_director_prog_scene = Progression_Scene(
            compile_scenes = hr_director_prog_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "hr_director_prog_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "hr_director_prog_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = hr_director_prog_scene_action,      #The action used to call for this progression scene.
            choice_scene = "hr_director_prog_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = False,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = None,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = False,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = True, #If MC can choose what final scene he wants
            multiple_choice_scene = "hr_director_prog_scene_multiple_choice_scene",   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        hr_director_prog_scene.compile_scenes(hr_director_prog_scene)   #This will populate the scenes that are blank above.
        return

label hr_director_prog_scene_action_label():  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: hr_director_prog_scene_action_label():

    #"Test, is this working"
    $ hr_director_prog_scene.call_scene([mc.business.hr_director])

    return

label hr_director_prog_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    "For some reason, she doesn't begin with her usual efficiency talk. Instead, she seems to be keenly interested in watching you eat..."
    the_person "So, before we get started today, I was wondering if umm..."
    mc.name "Yes?"
    "Her cheeks a little flushed, she's obviously embarrassed about what she is about to ask."
    the_person "Well... I've noticed that, we only employ women here, and it must be hard on you to be around so many women all day long..."
    "You don't really see where she is going with this."
    the_person "It would cause the company a lot of trouble if some sort of sexual harassment suit were to come up."
    mc.name "I suppose."
    the_person "So anyway, I thought maybe, to start the meeting, we could fool around a little."
    $ mc.change_locked_clarity(20)
    the_person "It would help clear your mind when we talk about the staff as well as give you an outlet for all the tension you have being around women all day..."
    mc.name "That's very generous of you. All in the name of efficiency?"
    the_person "Yeah! Well, plus it would be fun..."
    "You consider her offer."
    mc.name "That would be acceptable, and I can see how it would be helpful to start the meeting with a clear mind."
    "She smiles widely when you accept her explanation. You can tell she really just wants to fuck around..."
    $ set_HR_director_tag("business_HR_sexy_meeting", True)
    the_person "So... can we start today?"
    mc.name "Certainly, that seems like a great idea."
    the_person "So... I have no idea the best way to do this..."
    mc.name "Why don't you just come over here and give me a blowjob."
    the_person "Okay! That should be fun!"
    $ scene_manager.update_actor(the_person, position = "blowjob")
    "[the_person.possessive_title] comes around to your side of the desk and gets down on her knees. She pulls down your zipper and pulls your cock out."
    the_person "Mmm, it smells so manly. Let's get this taken care of!"
    $ mc.change_locked_clarity(30)
    "She runs her tongue up and down your length a few times, then parts her lips and begins to suck you off."
    $ mc.change_arousal(40)
    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_hr_prog_01
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        mc.name "Mmm, this is a great way to start Monday. This was a great idea [the_person.title]."
        $ scene_manager.update_actor(the_person, emotion = "happy")
        "[the_person.possessive_title] stops licking the cum off her lips for a second and smiles."
        the_person "Thank you sir! I am willing to do this next week again if you decide to."
    else:
        mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
        $ scene_manager.update_actor(the_person, emotion = "sad")
        the_person "Of course sir, I am willing to do this anytime you want me to."
    $ the_person.apply_planned_outfit()
    $ scene_manager.update_actor(the_person, position = "stand3")
    "She cleans herself up and makes herself presentable again."
    return

label hr_director_prog_scene_choice_label(the_group):
    $ the_person = the_group[0]
    if the_person.energy < 60:
        "She looks at you before she begins."
        the_person "So, normally I would offer to help with your... you know... needs..."
        the_person "But honestly I'm pretty worn out from earlier. If you are still feeling needy later, let me know, okay?"
        mc.name "Okay."
        return False

    else:
        $ prog_avail = hr_director_prog_scene.progression_available()
        "She looks at you intently."
        the_person "So, need some relief before we get started today? I'd be glad to help!"
        menu:
            "Let's go {image=gui/extra_images/Progress24.png}" if prog_avail:
                "Something about the look in her eyes tells you it is a good day to accept."
                mc.name "I could definitely use some relief today."
                return True
            # "Let's go" if not hr_director_prog_scene.progression_available():
            #     mc.name "I could definitely use some relief today."
            #     return True
            "Let's go" if not prog_avail:
                mc.name "I could definitely use some relief today."
                return True
            "Not Today":
                the_person "Ahh, damn. Okay, give me a second and we can get started here."

                return False
    return False

label hr_director_prog_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    "She reaches down to her backpack and begins to pull out her notes from the previous week."
    return

label hr_director_prog_scene_multiple_choice_scene(the_group):
    $ the_person = the_group[0]
    the_person "Okay! How do you want me to take care of you this week, [the_person.mc_title]?"

    menu:
        "Blowjob" if 0 in hr_director_prog_scene.scene_unlock_list:
            return 0
        "Tit Fuck" if 1 in hr_director_prog_scene.scene_unlock_list:
            return 1
        "Missionary on Desk" if 2 in hr_director_prog_scene.scene_unlock_list:
            return 2
        "Bent over Desk" if 3 in hr_director_prog_scene.scene_unlock_list:
            return 3
        "Anal Lapdance" if 4 in hr_director_prog_scene.scene_unlock_list:
            return 4
        "Cum Fetish Scene" if 5 in hr_director_prog_scene.scene_unlock_list:
            return 5
        "Breed Her" if 6 in hr_director_prog_scene.scene_unlock_list:
            return 6
        "Anal Fetish Scene" if 7 in hr_director_prog_scene.scene_unlock_list:
            return 7
        "Surprise me" if len(hr_director_prog_scene.scene_unlock_list) > 1:
            the_person "Mmmm, I can do that!"
            $ mc.change_arousal(20)
            $ the_person.change_stats(happiness = 5, obedience = 3)
            return renpy.random.choice(hr_director_prog_scene.scene_unlock_list)
    return


#Transition scenes
label hr_director_prog_scene_intro_0(the_group):
    $ the_person = the_group[0]
    "[the_person.possessive_title] sits across from you and eats her lunch. You make some small chat together."
    "Soon you are finishing up. She looks at you with a glimmer in her eye."
    return

label hr_director_prog_trans_scene_0(the_group):
    #This should never get called since BJs are opened from the start
    $ the_person = the_group[0]
    return

label hr_director_prog_trans_scene_1(the_group):
    $ the_person = the_group[0]
    if the_person is sarah and sarah_epic_tits_progress() > 1:
        the_person "So... I was thinking this week maybe I could do that thing again. You know, where I put your cock between my tits?"
        the_person "It felt soooo good last time. I've been thinking about it a lot."
        mc.name "That sounds great, I'll admit it, seeing my cock between your tits is hot."
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
        $ mc.change_arousal(20)
        $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
        "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
        $ mc.change_locked_clarity(30)
        "She gets on her knees and gives you a couple strokes with her hand."
        $ mc.change_arousal(20)
        the_person "Mmmm, I love the feeling of a cock buried between my big tits... this is gonna be great!"
        "With her hands on each side of her chest, she wraps her sizeable boobs around you and begins to bounce them up and down."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_hr_prog_02
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "After you finish, [the_person.possessive_title] runs her hands along her tits, rubbing your cum into her skin."
            the_person "Mmm, god that was hot. Let me just enjoy this a minute before we move on with the meeting..."
            if the_person.is_bald:
                "You run your hands over her shiny scalp for a bit while she enjoys the warmth of your cum on her skin."
            else:
                "You run your hands through her hair for a bit while she enjoys the warmth of your cum on her skin."
        else:
            mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "Of course sir, I am willing to do this anytime you want me to."
    else:
        mc.name "You know, you have some pretty generous cleavage. I've been wondering... what would it feel like to have those tits wrapped around my cock."
        the_person "Ah, you mean these?"
        $ scene_manager.update_actor(the_person, position = "stand3")
        if the_person.tits_available:
            "[the_person.title] stands up, then gropes herself with both hands, shifting her tits back and forth in a pleasing wobble motion."
        else:
            if the_person.outfit.can_half_off_to_tits():
                "[the_person.possessive_title] moves her top out of the way."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
            else:
                "[the_person.possessive_title] takes off her top."
                $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_tit_strip_list(), half_off_instead = False)
            "With her tits out and ready to be used, she gives you a big smile."
        $ mc.change_arousal(20)
        $ scene_manager.update_actor(the_person, position = "blowjob", emotion = "happy")
        "She gets up and starts walking around the desk. By the time she gets to you, you already have your rock hard dick out."
        $ mc.change_locked_clarity(30)
        "She gets on her knees and gives you a couple strokes with her hand."
        $ mc.change_arousal(20)
        the_person "Mmmm, I love the feeling of a cock buried between my big tits... this is gonna be great!"
        "With her hands on each side of her chest, she wraps her sizeable boobs around you and begins to bounce them up and down."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_hr_prog_02b
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "After you finish, [the_person.possessive_title] runs her hands along her tits, rubbing your cum into her skin."
            the_person "Mmm, god that was hot. Let me just enjoy this a minute before we move on with the meeting..."
            if the_person.is_bald:
                "You run your hands over her shiny scalp for a bit while she enjoys the warmth of your cum on her skin."
            else:
                "You run your hands through her hair for a bit while she enjoys the warmth of your cum on her skin."
        else:
            mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
            $ scene_manager.update_actor(the_person, emotion = "sad")
            the_person "Of course sir, I am willing to do this anytime you want me to."
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_01
    return

label hr_director_prog_trans_scene_2(the_group):
    $ the_person = the_group[0]
    the_person "Hey... you know what would be really hot?"
    "You feel yourself raise your eyebrow in response. This should be good!"
    the_person "What if I just lay down on your desk and you have your way with me, right here in your office?"
    the_person "Having my boss pin me to his desk and ravage me..."
    $ mc.change_arousal(20)
    mc.name "I think that's a good idea, but why don't you get your ass over here and we'll find out for sure!"
    the_person "Oh! Yes sir!"
    "[the_person.possessive_title] gets on your desk and lays on her back."
    $ scene_manager.update_actor(the_person, position = "missionary", emotion = "happy")
    if the_person.vagina_visible:
        "She spreads her legs, her pussy on display in front of you."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            "You move [the_person.possessive_title]'s clothes out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
        else:
            "You start to strip [the_person.possessive_title] down."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
        "Soon her pussy is on full display in front of you, on your desk."
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You have your cock out in a flash. You position it at her slick entrance."
    "You push yourself inside of her nice and slow, since she hasn't had much time to warm up yet."
    the_person "Mmmm, [the_person.mc_title]. Use me boss! I'm here to serve you!"
    "You start to piston your cock in and out of her."
    call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_hr_prog_03
    "[the_person.possessive_title] lays on your desk, recovering."
    mc.name "You were right, [the_person.title]. It IS really hot to fuck you on my desk!"
    the_person "Ah, yes, I suspected it would be, sir!"
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_02
    return

label hr_director_prog_trans_scene_3(the_group):
    $ the_person = the_group[0]
    mc.name "Come here, I'm going to use you the way I see fit today."
    if the_person.get_opinion_score("being submissive"):
        the_person "Oh! Yes sir!"
        $ the_person.change_obedience(3)
    else:
        the_person "Ok..."
    "You stand up as she walks around to your side of the desk. You roughly turn her around and bend her over your desk."
    $ scene_manager.update_actor(the_person, position="standing_doggy")
    $ mc.change_arousal(20)
    the_person "Oh my!"

    if the_person.vagina_visible:
        "She wiggles her hips back at you a bit. Her pussy lips glisten with a bit of moisture."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            "You move [the_person.possessive_title]'s clothes out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
        else:
            "You start to strip [the_person.possessive_title] down."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
        "Soon her ass is on full display in front of you, bent over your desk."
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You push yourself inside of her nice and slow, since she hasn't had much time to warm up yet."
    the_person "Oh God! It's going so deep."
    "You give her ass a solid spank, then begin to fuck her roughly."
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_hr_prog_04
    $ the_report = _return
    if the_report.get("girl_orgasms",0)>0:
        "[the_person.possessive_title] is still bent over your desk, recovering from her orgasm."
        the_person "That's... yeah you can do that to me any time."
    else:
        "[the_person.possessive_title] slowly recovers from using her body for your pleasure."
        the_person "Mmm, happy to be of service, sir. We can do that again next time... if you want!"
    $ scene_manager.update_actor(the_person, position = "stand3")
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_03
    return

label hr_director_prog_trans_scene_4(the_group):
    $ the_person = the_group[0]
    if the_person.is_girlfriend:
        the_person "[the_person.mc_title]... you know I love you, right?"
        "She seems very serious about what she's going to say."
        mc.name "Of course."
        the_person "Good."
    else:
        the_person "[the_person.mc_title]... you know I care about you, right?"
        mc.name "Of course."
        the_person "Good"
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[the_person.possessive_title] stands up."
    mc.name "Is there something wrong?"
    the_person "No. You know, I love these Monday meetings. Do you know why?"
    $ scene_manager.strip_to_tits(person = the_person)
    $ mc.change_locked_clarity(30)
    "[the_person.title] starts taking some of her clothes off."
    mc.name "No, why?"
    the_person "It just feels like we are starting the week off right."
    "[the_person.title] bends over and keeps stripping."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = False)
    $ mc.change_locked_clarity(50)
    the_person "Especially when it starts with us messing around in your office!"
    "[the_person.possessive_title] gives her ass a little shake before standing back up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    if the_person.has_taboo("anal_sex"):
        the_person "I kind of want to try something... we've never really done before..."
        mc.name "Oh?"
        if the_person.is_girlfriend:
            the_person "I want to be a good girlfriend, who meets all your needs, no matter what they are."
            the_person "So far you've claimed my mouth... and my pussy..."
            the_person "I want you to claim me in one more hole... I think you know what I mean!"
        else:
            the_person "I just want you to feel good, and I think I might like it as well, if you let me sit on your lap."
            the_person "I wouldn't normally do this, but your cock is so amazing... I just have to know what it would feel like in my ass!"
        the_person "Don't worry, I want to do it for you. Just sit back in your chair and let me!"
    else:
        the_person "This morning, I just want to make you feel good, and judging by last time, I think it will make me feel good too."
        mc.name "Oh yeah? What do you have in mind?"
        the_person "Why don't you just sit back in your chair and find out."
    mc.name "Sounds good, do your thing."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    "[the_person.possessive_title] turns away from you, her ass now right at eye level. She pulls her cheeks apart slightly, giving you an amazing view of her puckered hole."
    $ mc.change_locked_clarity(50)
    "She brings up one hand to her mouth and spits in it, then runs it back along her crack, giving you a show as she lubes up her ass a bit. You pull your cock out and give it a couple strokes."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "[the_person.title] bends over your desk, reaching for her purse she left on the far side. She wiggles her hips a bit as she pulls some lube out of her purse."
    the_person "Would you mind?"
    "[the_person.possessive_title] hands you the lube. You squirt a generous amount onto your fingers and work them around her sphincter and then slowly push a finger inside her."
    $ the_person.change_arousal (20)
    the_person "Ahhhhh..."
    $ mc.change_locked_clarity(50)
    "Her hips push back against you a bit as you work your finger in and out of her a bit, getting her good and lubed up. She moans at the penetration."
    the_person "Ok, let's do this."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
    "[the_person.possessive_title] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
    $ the_person.break_taboo("anal_sex")
    the_person "Oh god! It's in!"
    call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = anal_on_lap, skip_intro = True, allow_continue = False) from _call_get_fucked_sarah_gives_anal_lapdance_monday_01b
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "[the_person.possessive_title] stands up. Some of your cum has managed to escape, running down her leg."
    else:
        mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
        the_person "Of course..."
        "[the_person.possessive_title] stands up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "You make a mental note that from now on you can ask your HR director for some anal on Mondays."
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_04
    return

label hr_director_prog_trans_scene_5(the_group):
    $ the_person = the_group[0]
    #Not yet written
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_06
    return

label hr_director_prog_trans_scene_6(the_group):
    $ the_person = the_group[0]
    the_person "So, I know this is usually about you, and making sure your needs are met before the start of the week..."
    mc.name "... but?"
    the_person "But... I swear to god I feel like I'm in heat right now. It is all I can do to keep myself from jumping you everytime I see you in the hall!"
    the_person "I know this is out of line... but would you mind? It's a good time for it too..."
    mc.name "Hmmm, I don't know..."
    the_person "Please? I'm not sure I can concentrate on my work until you give me a big fertile load!"
    mc.name "Okay. Get over here and bend over."
    the_person "Yes!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.title] turns around. You quickly get her ready to fuck."
    $ the_person.strip_to_vagina(visible_enough = True, prefer_half_off = True, position = "standing_doggy")
    call fuck_person(the_person, start_position = bent_over_breeding, private = True) from _call_sex_description_hr_prog_05
    if the_person.has_creampie_cum:
        the_person "Oh fuck... every time you finish inside me is just so good..."
        "She rubs her belly and sighs."
        $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    the_person "Mmm, that was nice..."
    $ scene_manager.update_actor(the_person, position = "stand3")
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_05
    return

label hr_director_prog_trans_scene_7(the_group):
    $ the_person = the_group[0]
    # not yet written
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_07
    return


#Final Scenes
label hr_director_prog_scene_scene_0(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    the_person "Get your cock out, I want to taste it!"
    "[the_person.possessive_title] stands up and starts to walk around the desk while you pull out your erection."
    $ scene_manager.update_actor(the_person, position = "blowjob")
    "She gets down on her knees in front of you and takes a moment to admire your hardness."
    $ mc.change_locked_clarity(30)
    "She opens her mouth and runs her tongue along it a few times, and then parts her lips and begins to suck you off."
    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_hr_prog_00c
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_00b
    return

label hr_director_prog_scene_scene_1(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    if not the_person.tits_available:
        if the_person.outfit.can_half_off_to_tits():
            "[the_person.possessive_title] moves her top out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
        else:
            "[the_person.possessive_title] begins to take off her top."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_tit_strip_list(), half_off_instead = False)
        "With her tits out and ready to be used, she gives you a big smile."
    the_person "Get your cock out, I want to feel it slide between my boobs!"
    $ mc.change_locked_clarity(30)
    "You pull your cock out as she gets up and walks around your desk. She drops down on her knees in front of you."
    $ scene_manager.update_actor(the_person, position = "blowjob")
    "[the_person.possessive_title] smiles at you as she uses her hands to wrap her tits around your cock, and then starts to move them up and down."
    if the_person == sarah and sarah_get_special_titfuck_unlocked():
        call fuck_person(the_person, start_position = sarah_tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_special_titfuck_1b
    else:
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_meeting_mid_twob
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_01b
    return

label hr_director_prog_scene_scene_2(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    if not the_person.vagina_visible:
        if the_person.outfit.can_half_off_to_vagina():
            "[the_person.possessive_title] moves her clothes out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
        else:
            "[the_person.possessive_title] begins to take off her clothes."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
        "When she finishes getting naked, she gives you a big smile."
    the_person "Oh my, fucking me on your desk? You are so naughty, [the_person.mc_title]!"
    $ scene_manager.update_actor(the_person, position = "missionary")
    mc.name "Oh, I'm the naughty one? I seem to remember this was your idea in the first place..."
    "You pull your cock out and line it up with [the_person.title]'s pussy. You ease yourself inside of her with one slow, smooth push."
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    the_person "I never said I wasn't naughty too... Oh god, [the_person.mc_title], that feels good. Have your way with me!"
    call fuck_person(the_person, start_position = missionary, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_hr_prog_02c
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_02b
    return

label hr_director_prog_scene_scene_3(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    mc.name "Get over here, I'm going to bend you over my desk again."
    if the_person.get_opinion_score("being submissive"):
        the_person "Oh! Yes sir!"
        $ the_person.change_obedience(2)
    else:
        the_person "OK."
    "You stand up as she walks around to your side of the desk. You roughly pull her closer and give her ass a tight squeeze."
    $ scene_manager.update_actor(the_person, position="stand3")
    the_person "Oh my!"
    if the_person.vagina_visible:
        "You give her pussy a little rub and show her your fingers glistening with a bit of moisture. You quickly turn her around and bend her over your desk."
    else:
        if the_person.outfit.can_half_off_to_vagina():
            "You move [the_person.possessive_title]'s clothes out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
        else:
            "You start to strip [the_person.possessive_title] down."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
        "As soon as her pussy is on full display in front of you, you bend her over your desk, exposing her round ass."
    $ scene_manager.update_actor(the_person, position="standing_doggy")

    "You don't waste any time. You pull your cock out and point it at her slit. You pull her hips back as you push inside of her with one smooth push."
    the_person "Mmm, fuck me good [the_person.mc_title]!"
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("condomless_sex")
    $ the_person.break_taboo("vaginal_sex")
    "You eagerly begin to pump your hips and fuck your HR director over your desk."
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True, girl_in_charge = False, position_locked = True, private = True) from _call_sex_description_hr_prog_03c
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_03b
    return

label hr_director_prog_scene_scene_4(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    the_person "Oh god, you want your HR director's ass, do you? What a naughty CEO!"
    $ the_person.change_arousal(20)
    if not the_person.vagina_visible:
        if the_person.outfit.can_half_off_to_vagina():
            "[the_person.possessive_title] moves her clothes out of the way."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
        else:
            "[the_person.possessive_title] begins to take off her clothes."
            $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_vagina_strip_list(), half_off_instead = False)
        "When she finishes getting naked, she gives you a big smile."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "In here was it? Where you wanted to stick that incredible dick you've got?"
    "[the_person.possessive_title] spreads her cheeks, revealing her puckered hole."
    $ mc.change_locked_clarity(50)
    mc.name "You know it."
    the_person "Hmm... I'm not sure it'll go in easily..."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    "She bends over your desk and grabs her purse, looking through it."
    "Her ass is on full display for you, so you make sure to give it a couple of spanks and a firm grope."
    "[the_person.title] hands back to you a bottle of lube she pulled from her bag."
    the_person "Here, can you lube me up?"
    mc.name "With pleasure."
    "You squirt a generous amount onto [the_person.title]'s ass. You work it all along her crack and then push a finger inside."
    $ the_person.change_arousal (20)
    the_person "Ahhhhh..."
    $ mc.change_locked_clarity(50)
    "It isn't long until you've got two fingers working her backdoor good."
    the_person "Ok, let's do this."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
    "[the_person.possessive_title] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
    $ the_person.break_taboo("anal_sex")
    the_person "Oh god! It's in!"
    call get_fucked(the_person, the_goal = "anal creampie", private= True, start_position = anal_on_lap, skip_intro = True, allow_continue = False) from _call_get_fucked_sarah_gives_anal_lapdance_monday_02c
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "[the_person.possessive_title] stands up. Some of your cum has managed to escape, running down her leg."
    else:
        mc.name "That was great, but we have a long day ahead, could we finish this up another time?"
        the_person "Of course..."
        "[the_person.possessive_title] stands up."
    $ scene_manager.update_actor(the_person, position = "stand3")
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_04b
    return

label hr_director_prog_scene_scene_5(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return

    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_06b
    return

label hr_director_prog_scene_scene_6(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return
    mc.name "Get over here, I'm going to bend you over my desk and creampie you."
    the_person "Fuck I love Mondays. Let's do it!"
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ mc.change_locked_clarity(50)
    "[the_person.title] turns around. You quickly get her ready to fuck."
    $ the_person.strip_to_vagina(visible_enough = True, prefer_half_off = True, position = "standing_doggy")
    call fuck_person(the_person, start_position = bent_over_breeding, private = True) from _call_hr_breeding_02c
    if the_person.has_creampie_cum:
        the_person "Oh fuck... every time you finish inside me is just so good..."
        "She rubs her belly and sighs."
        $ the_person.event_triggers_dict["LastBreedingFetish"] = day
    the_person "Mmm, that was nice..."
    $ scene_manager.update_actor(the_person, position = "stand3")
    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_05b
    return

label hr_director_prog_scene_scene_7(the_group, scene_transition = False):
    $ the_person = the_group[0]
    if scene_transition:
        return

    call hr_director_post_scene(the_group) from _hr_director_cleanup_time_07b
    return


label hr_director_post_scene(the_group):
    $ the_person = the_group[0]
    if the_person.is_in_trance:
        "[the_person.title] is in a trance. Before you continue, you can take a moment to train her."
        call do_training(the_person) from _call_do_training_post_hr_sex_time_01
    if the_person.has_cum_fetish or the_person.has_exhibition_fetish:
        the_person "Alright, I'm ready to continue the meeting."
        "[the_person.title] doesn't appear to be concerned with her appearance whatsoever."
    elif ((the_person.obedience - 100) + the_person.sluttiness) > 100: #If she is either very obedient, slutty, or a mixture
        menu:
            "Tell her to stay like that for the meeting":
                mc.name "I'm very busy, let's just continue the meeting. Don't bother to clean up."
                "[the_person.title] opens her mouth for a second, ready to protest, but quickly reconsiders."
                the_person "Of course, [the_person.mc_title]. Let's see what is next."
                $ mc.change_locked_clarity(20)
            "Let her clean herself up":
                $ the_person.apply_planned_outfit()
                "[the_person.possessive_title] quickly cleans herself up, ready to continue the meeting."
    else:
        $ the_person.apply_planned_outfit()
        "She quickly starts to get dressed to continue your meeting."

    $ the_person.draw_person(position = "sitting")
    return
