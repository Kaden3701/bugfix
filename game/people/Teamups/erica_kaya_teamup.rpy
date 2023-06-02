#This scene is for Kaya and Erica tuesday night study sessions at the university.
#Currently this scene should roughly mimic study session progress of the study sessions with the tutor
#STAGES:
#0: Just help them study
#1: but only if they strip for each wrong answer
#2: they get spanked for each wrong answer
#3: they suck you off for each wrong answer
#4: girl with most right answer gets fucked, while the loser gets eaten out.

#All stages should present opportunity to build sluttiness a bit.

init 1 python:
    def kaya_erica_teamup_0_req():
        return True

    def kaya_erica_teamup_1_req():
        if kaya.sluttiness > 20 and erica.sluttiness > 20:
            return True
        return False

    def kaya_erica_teamup_2_req():
        if kaya.sluttiness >= 40 and erica.sluttiness >= 40:
            return True
        return False

    def kaya_erica_teamup_3_req():
        if kaya.sluttiness >= 60 and erica.sluttiness >= 60:
            return True
        return False

    def kaya_erica_teamup_4_req():
        if willing_to_threesome(kaya, erica):
            return True
        return False

    def kaya_erica_teamup_action_req(the_person):
        if day%7 == 1 and time_of_day == 4 and the_person.location == university:    #TODO double check and make sure this actually works...
            return True
        return False

init 2 python:
    def kaya_erica_teamup_compile_scenes(the_teamup):
        the_teamup.start_scene_list = ["kaya_erica_teamup_intro_0", "kaya_erica_teamup_intro_1", "kaya_erica_teamup_intro_2", "kaya_erica_teamup_intro_3", "kaya_erica_teamup_intro_4"]
        the_teamup.req_list = [kaya_erica_teamup_0_req, kaya_erica_teamup_1_req, kaya_erica_teamup_2_req, kaya_erica_teamup_3_req, kaya_erica_teamup_4_req]
        the_teamup.trans_list = ["kaya_erica_trans_scene_0", "kaya_erica_trans_scene_1", "kaya_erica_trans_scene_2", "kaya_erica_trans_scene_3", "kaya_erica_trans_scene_4"]
        the_teamup.final_scene_list = ["kaya_erica_teamup_scene_0", "kaya_erica_teamup_scene_1", "kaya_erica_teamup_scene_2", "kaya_erica_teamup_scene_3", "kaya_erica_teamup_scene_4"]
        return

    kaya_erica_teamup_action = Action("Kaya and Erica Study Night", kaya_erica_teamup_action_req, "kaya_erica_teamup_action_label")

    def kaya_erica_teamup_init():
        global kaya_erica_teamup
        kaya_erica_teamup = Progression_Scene(compile_scenes = kaya_erica_teamup_compile_scenes,
            start_scene_list = [],
            req_list = [],
            trans_list = [],
            final_scene_list = [],
            intro_scene = "kaya_erica_teamup_intro_scene",
            exit_scene = "kaya_erica_teamup_exit_scene",
            progression_scene_action = kaya_erica_teamup_action,
            choice_scene = "kaya_erica_teamup_study_choice",
            person_action = True,
            stage = -1)

        kaya_erica_teamup.compile_scenes(kaya_erica_teamup)

label kaya_erica_teamup_action_label(the_person):
    $ mc.change_location(university_study_room)
    call progression_scene_label(kaya_erica_teamup, [kaya, erica]) from _erica_kaya_teamup_scene_call_test_02
    return

label kaya_erica_teamup_intro_scene(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night there."
    "You quickly text [kaya.title], letting her know you are here and asking where they are studying at."
    "Soon you step into a study room and see the two girls sitting at a small table with their books out."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey!"
    erica "Hey [erica.mc_title], glad you could make it!"
    mc.name "Of course."
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, before we get started, want me to fill up those bottles at the drinking fountain for you?"
    erica "Oh! That would be great! I had a long workout today and really need to stay hydrated..."
    kaya "Yes please."
    mc.name "Okay, one sec."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_01
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "You step inside the room and sit down next to the two girls."
    kaya "So, we have a quiz tomorrow, we were wondering if you could quiz us on some of the material."
    erica "It would be great for figuring out what we need to be studying!"
    mc.name "Sure, let me take a look at the material."
    "[kaya.possessive_title] hands you a study guide for the class they are taking together."
    "You look over it for a moment. Yes, you remember this material, and quickly come up with a few questions to gauge their progress."
    mc.name "Okay [kaya.title]."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_question_01
    "Now you turn to [erica.possessive_title]."
    mc.name "Alright [erica.title], how about this."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_question_02
    "You spend some time going over a couple more questions, and soon you have a pretty good idea of what to direct their study time towards."
    $ kaya.change_stats(happiness = 2, love = 2, max_love = 40)
    $ erica.change_stats(happiness = 2, love = 2, max_love = 40)
    erica "Wow, that was really helpful. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help."
    mc.name "Alright, you girls can take it from here?"
    erica "Sure can."
    mc.name "Alright, I'll see myself out then."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    $ kaya.add_unique_on_talk_event(kaya_uni_scholarship_intro)
    $ kaya.event_triggers_dict["studies_with_erica"] = True
    "It is late, and you start your walk home."
    $ downtown.show_background()
    "This arrangement between the two college girls could work to your advantage. The study rooms at the university seem fairly private..."
    "This could be an opportunity for you to make progress with the two girls, with opportunities to give them your serums."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_01
    return

label kaya_erica_teamup_intro_0(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night there."
    "The girls have a room they usually use for their study sessions, so you swing by and find them."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey!"
    erica "Hey [erica.mc_title], we are just doing some more studying."
    mc.name "Sounds like you girls are working hard."
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, want me to fill up those bottles at the drinking fountain for you?"
    erica "Oh! That would be great! I had a long workout today and really need to stay hydrated..."
    kaya "Yes please."
    mc.name "Okay, one sec."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_02
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "You step inside the room and sit down next to the two girls."
    return

label kaya_erica_teamup_intro_1(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night there."
    "Recently, the sessions have included the girls stripping when they get questions wrong. It has been a wonderful diversion."
    "The girls have a room they usually use for their study sessions, so you swing by and find them."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey!"
    erica "Hey [erica.mc_title], we are just doing some more studying."
    mc.name "Sounds like you girls are working hard."
    kaya "Yeah, we were just talking about how we were kind of hoping you would swing by tonight..."
    mc.name "Is that so?"
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, want me to fill up those bottles at the drinking fountain for you?"
    erica "Oh! That would be great! I did 10k on the treadmill earlier so I'm drinking my water FAST!"
    kaya "Yes please."
    mc.name "Okay, one sec."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_03
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "You step inside the room and sit down next to the two girls."
    return

label kaya_erica_teamup_intro_2(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night there."
    "Recently, you managed to convince them it would be good for the study session to get spanked when they get a question wrong."
    "Thoughts of their tight, reddened asses get you a little excited as you head towards the building they are in."
    "The girls have a room they usually use for their study sessions, so you swing by and find them."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey! [erica.fname] he's here!"
    erica "Hey! I figured you would come!"
    mc.name "Sounds like you girls are working hard."
    kaya "Yeah, we were just talking about how we were kind of hoping you would swing by tonight..."
    mc.name "Is that so?"
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, want me to fill up those bottles at the drinking fountain for you?"
    erica "You know it! I pushed myself hard today at the gym!"
    kaya "Yes please."
    mc.name "Okay, one minute."
    kaya "Take your time."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_04
    $ kaya.strip_to_underwear(delay = 0)
    $ kaya.outfit.remove_all_upper_clothing()
    $ erica.strip_to_underwear(delay = 0)
    $ erica.outfit.remove_all_upper_clothing()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "When you get back to the room, you notice the girls have already stripped down to their panties while you were gone."
    $ mc.change_locked_clarity(50)
    "You step inside the room and sit down next to the two girls."
    return

label kaya_erica_teamup_intro_3(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night there."
    "Recently, you managed to convince them it would be good for the study session to go down on you when they get a question wrong."
    "Thoughts of their soft lips wrapped around your cock get you excited just thinking about it."
    "The girls have a room they usually use for their study sessions, so you swing by and find them."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey! [erica.fname] he's here!"
    erica "Hey! I was really hoping you would make it out tonight..."
    mc.name "Sounds like you girls are working hard."
    kaya "Yeah! Having you here helps us study nice and hard..."
    mc.name "Is that so?"
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, want me to fill up those bottles at the drinking fountain for you?"
    erica "You know it! I pushed myself hard today at the gym!"
    kaya "Yes please."
    mc.name "Okay, one minute."
    kaya "Take your time."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_05
    $ kaya.strip_to_underwear(delay = 0)
    $ kaya.outfit.remove_all_upper_clothing()
    $ erica.strip_to_underwear(delay = 0)
    $ erica.outfit.remove_all_upper_clothing()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "When you get back to the room, you notice the girls have already stripped down to their panties while you were gone."
    $ mc.change_locked_clarity(50)
    "You step inside the room and sit down next to the two girls."
    return

label kaya_erica_teamup_intro_4(the_group):
    "You head to the university. It is Tuesday night, and [erica.title] and [kaya.possessive_title] are planning a study night here."
    "Study sessions with the two college girls are incredible. When you finish studying, the threesome afterwords makes the whole session worth it."
    "[erica.title] and her fit young body and [kaya.title]'s deliciously dark skin have you fantasizing about it as you walk into the building."
    "The girls have a room they usually use for their study sessions, so you swing by and find them."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    kaya "Hey! Just can't stop coming to the study sessions can you?"
    erica "He sure can't!"
    mc.name "Sounds like you girls are ready to put in some hard work tonight."
    kaya "Oh yeah, hopefully it's as hard as last time..."
    "You start to sit down at the table with the two girls, but notice they both have water bottles that are almost empty."
    mc.name "Hey, want me to fill up those bottles at the drinking fountain for you?"
    erica "You know it! I pushed myself hard today at the gym!"
    kaya "Yes please."
    mc.name "Okay, one minute."
    kaya "Take your time."
    $ scene_manager.clear_scene()
    "You step out of the room."
    call kaya_erica_teamup_get_drinks_label() from _kaya_erica_teamup_intro_drinks_06
    $ kaya.strip_outfit(delay = 0)
    $ erica.strip_outfit(delay = 0)
    $ scene_manager.add_actor(kaya, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(erica, position = "sitting")
    "When you get back to the room, you notice the girls have already stripped naked."
    $ mc.change_locked_clarity(100)
    "You step inside the room and sit down next to the two girls."
    return

label kaya_erica_teamup_scene_0(the_group, scene_transition = False):
    mc.name "Of course I'll help, that's why I swung by."
    kaya "Great! We have a quiz tomorrow, we were wondering if you could quiz us on some of the material."
    erica "It would be great for figuring out what we need to be studying!"
    mc.name "Sure, let me take a look at the material."
    "[kaya.possessive_title] hands you a study guide for the class they are taking together."
    "You look over it for a moment. Yes, you remember this material, and quickly come up with a few questions to gauge their progress."
    mc.name "Okay [kaya.title]."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_question_03
    "Now you turn to [erica.possessive_title]."
    mc.name "Alright [erica.title], how about this."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_question_04
    "You spend some time going over a couple more questions, and soon you have a pretty good idea of what to direct their study time towards."
    $ kaya.change_stats(happiness = 2, love = 2, max_love = 40)
    $ erica.change_stats(happiness = 2, love = 2, max_love = 40)
    erica "Wow, that was really helpful. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help."
    mc.name "Alright, you girls can take it from here?"
    erica "Sure can."
    mc.name "Alright, I'll see myself out then."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    "It is late, and you start your walk home."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_02
    return

label kaya_erica_teamup_scene_1(the_group, scene_transition = False):
    mc.name "Let's get to studying. Let's go over the rules."
    mc.name "Three questions each. For each wrong answer, you have to remove an INTERESTING piece of clothing. No shoes or bracelets."
    kaya "Got it."
    erica "Alright, let's do this!"
    "Always competitive, [erica.possessive_title] seems excited by the challenge, while [kaya.title] seems calm but determined."
    mc.name "Okay, [kaya.title], here we go."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_strip_question_01
    if not _return:
        kaya "Oh no! Alright... here goes..."
        $ the_item = kaya.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(kaya, the_item)
            "[kaya.title] quietly peels off her [the_item.display_name]."
            $ kaya.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ erica.change_arousal(3)
            $ kaya.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            kaya "I don't have anything to take off though."
            mc.name "Hmm... maybe we need to come up with something more punishing if you are showing up to study time already naked?"
            $ kaya.change_slut(2, 40)
    mc.name "Alright, [erica.title], your first question."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_strip_question_02
    if not _return:
        erica "Damn! Okay..."
        $ the_item = erica.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(erica, the_item)
            "[erica.title] quickly takes off her [the_item.display_name]."
            $ erica.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ kaya.change_arousal(3)
            $ erica.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            erica "I don't have anything to take off."
            mc.name "Hmm... maybe we need to come up with something more punishing if you are showing up to study time already naked?"
            $ erica.change_slut(2, 40)
    mc.name "Alright, on to the second round of questions."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_strip_question_03
    if not _return:
        kaya "Ugh! I thought I had it for sure."
        $ the_item = kaya.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(kaya, the_item)
            "[kaya.title] quietly peels off her [the_item.display_name]."
            $ kaya.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ erica.change_arousal(3)
            $ kaya.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            kaya "I don't have anything to take off though."
            mc.name "Hmm... maybe we need to come up with something more punishing if you are already naked?"
            $ kaya.change_slut(2, 40)
    mc.name "Alright, [erica.title], next question."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_strip_question_04
    if not _return:
        erica "Fuck! I thought for sure I had that one."
        $ the_item = erica.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(erica, the_item)
            "[erica.title] quickly takes off her [the_item.display_name]."
            $ erica.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ kaya.change_arousal(3)
            $ erica.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            erica "I don't have anything to take off."
            mc.name "Hmm... maybe we need to come up with something more punishing if you are already naked?"
            $ erica.change_slut(2, 40)
    mc.name "Alright, on to the final round of questions."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_strip_question_05
    if not _return:
        kaya "What? That can't be right..."
        $ the_item = kaya.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(kaya, the_item)
            "[kaya.title] peels off her [the_item.display_name] while muttering about her incorrect answer."
            $ kaya.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ erica.change_arousal(3)
            $ kaya.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            kaya "I don't have anything to take off though."
            mc.name "Hmm... maybe we need to come up with something more punishing if you are already naked?"
            $ kaya.change_slut(2, 40)
    mc.name "Alright, [erica.title], last question."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_strip_question_06
    if not _return:
        erica "No! I swear I had it right!"
        $ the_item = erica.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if the_item:
            $ scene_manager.draw_animated_removal(erica, the_item)
            "[erica.title] takes off her [the_item.display_name] even though she is protesting."
            $ erica.change_arousal(5)    #Everyone liked that
            $ mc.change_arousal(3)
            $ kaya.change_arousal(3)
            $ erica.change_slut(1, 40)
            $ mc.change_locked_clarity(10)
            $ the_item = None
        else:
            erica "I don't have anything left to take off!"
            mc.name "Hmm... maybe we need to come up with something more punishing if you are already naked?"
            $ erica.change_slut(2, 40)
    "Finished with your questions, you have a pretty good idea of where to direct their study time."
    $ kaya.change_stats(happiness = 2, love = 2, max_love = 40)
    $ erica.change_stats(happiness = 2, love = 2, max_love = 40)
    erica "Wow, that was really helpful. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help, and it was fun too!"
    mc.name "Alright, you girls can take it from here?"
    erica "Sure can."
    mc.name "Alright, I'll see myself out then."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    "It is late, and you start your walk home."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_03
    return

label kaya_erica_teamup_scene_2(the_group, scene_transition = False):
    mc.name "Let's get to studying. Let's go over the rules."
    mc.name "Three questions each. For each wrong answer, you have bend over and get spanked while I ask your study partner their question."
    kaya "Got it."
    erica "Alright, let's do this!"
    "Always competitive, [erica.possessive_title] seems excited by the challenge, while [kaya.title] seems calm but determined."
    mc.name "Okay, [kaya.title], here we go."
    $ previous_punished = False
    $ erica_spank_count = 0
    $ kaya_spank_count = 0
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_spank_question_01
    if not _return:
        $ kaya_spank_count += 1
        kaya "Oh no! Okay, I guess I'm first up..."
        $ scene_manager.update_actor(kaya, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ kaya.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ erica.change_arousal(5)
        $ kaya.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "As you spank her, you turn to [erica.possessive_title]."
    mc.name "Alright, [erica.title], your first question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_spank_question_02
    if not _return:
        $ erica_spank_count += 1
        erica "Damn! Okay..."
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_01
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "[kaya.title] takes her seat."
        $ scene_manager.update_actor(erica, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ erica.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ kaya.change_arousal(5)
        $ erica.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "As you spank her, you turn to [kaya.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, it's your turn again."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_02
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "[kaya.title] takes her seat."
        $ previous_punished = False
    mc.name "Alright, on to the second round of questions."
    call kaya_erica_teamup_question_label(kaya, active_punishment = previous_punished, punished_person = erica) from _kaya_erica_teamup_spank_question_03
    if not _return:
        $ kaya_spank_count += 1
        kaya "No! Ugh... okay okay..."
        if previous_punished:
            mc.name "Alright [erica.title], it's your study partner's turn."
            call kaya_erica_teamup_spank_ass_condition(erica, erica_spank_count) from _kaya_erica_teamup_spank_debrief_03
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "She takes her seat."
        $ scene_manager.update_actor(kaya, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ kaya.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ erica.change_arousal(5)
        $ kaya.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "As you spank her, you turn to [erica.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [erica.title]. Your partner got her question right, it's your turn again."
            call kaya_erica_teamup_spank_ass_condition(erica, erica_spank_count) from _kaya_erica_teamup_spank_debrief_04
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "She takes her seat."
        $ previous_punished = False
    mc.name "Alright, [erica.title], next question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_spank_question_04
    if not _return:
        $ erica_spank_count += 1
        erica "Damn! These questions are hard!"
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_05
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "She takes her seat."
        $ scene_manager.update_actor(erica, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ erica.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ kaya.change_arousal(5)
        $ erica.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "As you spank her, you turn to [kaya.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, it's your turn again."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_06
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "She takes her seat."
        $ previous_punished = False
    mc.name "Alright, on to the final round of questions."
    call kaya_erica_teamup_question_label(kaya, active_punishment = previous_punished, punished_person = erica) from _kaya_erica_teamup_spank_question_05
    if not _return:
        $ kaya_spank_count += 1
        kaya "No! I was so close!"
        mc.name "Not close enough. You know what to do."
        if previous_punished:
            mc.name "Alright [erica.title], it's your study partner's turn."
            call kaya_erica_teamup_spank_ass_condition(erica, erica_spank_count) from _kaya_erica_teamup_spank_debrief_07
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "She takes her seat."
        $ scene_manager.update_actor(kaya, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ kaya.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ erica.change_arousal(5)
        $ kaya.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "As you spank her, you turn to [erica.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [erica.title]. Your partner got her question right, it's your turn again."
            call kaya_erica_teamup_spank_ass_condition(erica, erica_spank_count) from _kaya_erica_teamup_spank_debrief_08
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "She takes her seat."
        $ previous_punished = False
    mc.name "Alright, [erica.title], last question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_spank_question_06
    if not _return:
        $ erica_spank_count += 1
        erica "Damn! I thought I had that!"
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_09
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "She takes her seat."
        $ scene_manager.update_actor(erica, position = "standing_doggy", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] bends over, presenting her ass to you."
        $ previous_punished = True
        $ play_spank_sound()
        "You give her ass a firm spank. First on one cheek, then the other. She gives a little yelp with the first one."
        $ erica.change_arousal(7)    #Everyone liked that
        $ mc.change_arousal(5)
        $ kaya.change_arousal(5)
        $ erica.change_slut(1, 60)
        $ mc.change_locked_clarity(20)
        "Since that was the last question, there is only silence in the room this time, except for the loud slapping as you deliver [erica.possessive_title]'s punishment."
        "When you are done, you grope her ass a moment."
        call kaya_erica_teamup_spank_ass_condition(erica, erica_spank_count) from _kaya_erica_teamup_spank_debrief_10
        $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
        "She takes her seat."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, so I think we are finished."
            call kaya_erica_teamup_spank_ass_condition(kaya, kaya_spank_count) from _kaya_erica_teamup_spank_debrief_11
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "She takes her seat."
        $ previous_punished = False
    "Finished with your questions, you have a pretty good idea of where to direct their study time."
    $ kaya.change_stats(happiness = 2, love = 2, max_love = 40)
    $ erica.change_stats(happiness = 2, love = 2, max_love = 40)
    erica "Wow, that was really helpful. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help, and it was fun too!"
    mc.name "Alright, you girls can take it from here?"
    erica "Sure can."
    mc.name "Alright, I'll see myself out then."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    "It is late, and you start your walk home."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_04
    return

label kaya_erica_teamup_scene_3(the_group, scene_transition = False):
    mc.name "Let's get to studying. Let's go over the rules."
    mc.name "Three questions each. For each wrong answer, you get on your knees and service me for at least one minute while I ask your partner their question."
    kaya "Got it."
    erica "Alright, let's do this!"
    "Always competitive, [erica.possessive_title] seems excited by the challenge, while [kaya.title] seems calm but determined."
    "You unzip your pants and pull out your cock, already hard from the anticipation."
    mc.name "Okay, [kaya.title], here we go."
    $ previous_punished = False
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_oral_question_01
    if not _return:
        kaya "Oh no! Okay, I guess I'm first up..."
        $ scene_manager.update_actor(kaya, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] gets on her knees. She hesitates for a moment, but then opens up and takes your cock into her heavenly mouth."
        $ previous_punished = True
        "You give a little grunt as she gets to work, putting one hand on the back of her head to guide her bobbing."
        $ kaya.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ erica.change_arousal(10)
        $ kaya.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ kaya.increase_opinion_score("giving blowjobs", weighted = True)
        "You turn to [erica.possessive_title]."
    mc.name "Alright, [erica.title], your first question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_oral_question_02
    if not _return:
        erica "Damn! Okay..."
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = True) from _kaya_erica_teamup_oral_debrief_01
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "[kaya.title] gets up and takes her seat."
        $ scene_manager.update_actor(erica, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] gets on her knees at your feet. She wastes no time opening up and getting to work on your cock."
        $ previous_punished = True
        if erica.is_bald:
            "You run your hand over her smooth scalp as you start to enjoy [erica.possessive_title]'s oral ministrations."
        else:
            "You run your hand through her hair as you start to enjoy [erica.possessive_title]'s oral ministrations."
        $ erica.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ kaya.change_arousal(10)
        $ erica.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ erica.increase_opinion_score("giving blowjobs", weighted = True)
        "As she services you, you turn back to [kaya.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, it's your turn again."
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "Your cock escapes her lips with a pop and she gets up and takes her seat."
            call kaya_erica_teamup_blowjob_condition() from _kaya_erica_teamup_oral_debrief_02
        $ previous_punished = False
    mc.name "Alright, on to the second round of questions."
    call kaya_erica_teamup_question_label(kaya, active_punishment = previous_punished, punished_person = erica) from _kaya_erica_teamup_oral_question_03
    if not _return:
        kaya "No! Ugh... okay okay..."
        if previous_punished:
            mc.name "Alright [erica.title], don't hog all the fun, it's your partner's turn."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = True) from _kaya_erica_teamup_oral_debrief_03
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "[erica.title] gets up and takes her seat with a little pout."
        $ scene_manager.update_actor(kaya, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] gets on her knees. She hesitates for a moment, but then opens up and takes your cock into her heavenly mouth."
        $ previous_punished = True
        "You give a little grunt as she gets to work, putting one hand on the back of her head to guide her bobbing."
        $ kaya.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ erica.change_arousal(10)
        $ kaya.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ kaya.increase_opinion_score("giving blowjobs", weighted = True)
        "You turn to [erica.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [erica.title]. Your partner got her question right, it's your turn again."
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "Your cock escapes her lips with a pop and she gets up and takes her seat."
            call kaya_erica_teamup_blowjob_condition() from _kaya_erica_teamup_oral_debrief_04
        $ previous_punished = False
    mc.name "Alright, [erica.title], next question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_oral_question_04
    if not _return:
        erica "What? Are you sure?"
        mc.name "Definitely. On your knees."
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = True) from _kaya_erica_teamup_oral_debrief_05
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "[kaya.title] gets up and takes her seat."
        $ scene_manager.update_actor(erica, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] gets on her knees at your feet. She hungrily takes you in her mouth and gets to work."
        $ previous_punished = True
        "There's nothing quite like the feeling of a eager young coed's mouth."
        $ erica.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ kaya.change_arousal(10)
        $ erica.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ erica.increase_opinion_score("giving blowjobs", weighted = True)
        "As she services you, you turn back to [kaya.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, it's your turn again."
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "Your cock escapes her lips with a pop and she gets up and takes her seat."
            call kaya_erica_teamup_blowjob_condition() from _kaya_erica_teamup_oral_debrief_06
        $ previous_punished = False
    mc.name "Alright, on to the final round of questions."
    call kaya_erica_teamup_question_label(kaya, active_punishment = previous_punished, punished_person = erica) from _kaya_erica_teamup_oral_question_05
    if not _return:
        kaya "No! That's impossible!"
        mc.name "Search your feelings, you know I'm right. On your knees."
        if previous_punished:
            mc.name "Alright [erica.title], fun time is over, it's your partner's turn."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = True) from _kaya_erica_teamup_oral_debrief_07
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "[erica.title] gets up and takes her seat with a little pout."
        $ scene_manager.update_actor(kaya, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.title] gets on her knees. She cautiously runs her tongue up and down the shaft a couple times before opening up and taking you in her mouth."
        $ previous_punished = True
        "You rest your hand on her head, guiding her as she sucks you off."
        $ kaya.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ erica.change_arousal(10)
        $ kaya.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ kaya.increase_opinion_score("giving blowjobs", weighted = True)
        "You turn to [erica.possessive_title]."
    else:
        if previous_punished:
            mc.name "Alright [erica.title]. Your partner got her question right, it's your turn again."
            $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
            "Your cock escapes her lips with a pop and she gets up and takes her seat."
            call kaya_erica_teamup_blowjob_condition() from _kaya_erica_teamup_oral_debrief_08
        $ previous_punished = False
    mc.name "Alright, [erica.title], last question."
    call kaya_erica_teamup_question_label(erica, active_punishment = previous_punished, punished_person = kaya) from _kaya_erica_teamup_oral_question_06
    if not _return:
        erica "Damn! I thought I had that!"
        if previous_punished:
            mc.name "Alright [kaya.title], it's your study partner's turn."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = True) from _kaya_erica_teamup_oral_debrief_09
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "[kaya.title] takes her seat."
        $ scene_manager.update_actor(erica, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[erica.title] gets on her knees at your feet. She hungrily takes you in her mouth and gets to work."
        $ previous_punished = True
        "[erica.title] keeps up a steady pace, bobbing her head back and forth and running your cock in and out of her soft mouth."
        $ erica.change_arousal(5)    #Everyone liked that
        $ mc.change_arousal(25)
        $ kaya.change_arousal(10)
        $ erica.change_slut(1, 80)
        $ mc.change_locked_clarity(40)
        $ erica.increase_opinion_score("giving blowjobs", weighted = True)
        "Since that was the last question, there is only silence in the room this time, except for lewd slurping noises as you deliver [erica.possessive_title]'s punishment."
        if mc.arousal_perc >= 100:
            "Thankfully, you feel your orgasm approaching. You were starting to get worried you might not get off tonight, but the final wrong answer of the night is going to finish you off."
            mc.name "Atta girl. Get ready [erica.title], I'm about to cum!"
            "She just moans as you start to cum."
            $ erica.cum_in_mouth()
            $ erica.increase_opinion_score("drinking cum", weighted = True)
            $ scene_manager.update_actor(erica, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
            "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [erica.hair_description]."
            "[kaya.title] just watches quietly, a hint of jealousy on her face."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = erica)
            $ mc.reset_arousal()
            "When you finish, [erica.title] slides off and gasps for air. You give her a few moments."
            mc.name "I suppose that is enough punishment then."
        else:
            "As much as you want her to just keep going until you finish, you can tell it wouldn't really be fair."
            mc.name "Alright, that's enough."
            $ scene_manager.update_actor(erica, erica.idle_pose, display_transform = character_right)
            "Your cock escapes her lips with a pop and she gets up."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = False, final = True) from _kaya_erica_teamup_oral_debrief_10
        $ scene_manager.update_actor(erica, position = "sitting", display_transform = character_right)
        "She takes her seat."
    else:
        if previous_punished:
            mc.name "Alright [kaya.title]. Your partner got her question right, so I think we are finished."
            call kaya_erica_teamup_blowjob_condition(inc_mouth = False, final = True) from _kaya_erica_teamup_oral_debrief_11
            $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
            "She takes her seat."
        $ previous_punished = False
    if mc.arousal_perc > 70 and kaya.love > 40:    #She loves MC enough to take care of him.
        kaya "[kaya.mc_title]... are you okay? That looks... Painful!"
        mc.name "It actually does hurt a little."
        kaya "That's... I can't let you go home like that!"
        $ scene_manager.update_actor(kaya, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "[kaya.possessive_title] drops to her knees and grabs your cock. She quickly takes it in her mouth and starts bobbing her head up and down."
        mc.name "Oh! Fuck [kaya.title] thank you I'm so close..."
        "[kaya.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
        $ erica.change_arousal(10)    #Everyone liked that
        $ mc.change_arousal(35)
        $ kaya.change_arousal(10)
        $ kaya.change_slut(2, 90)
        $ mc.change_locked_clarity(50)
        $ kaya.increase_opinion_score("giving blowjobs")
        erica "Damn, she's really thirsty for it, isn't she?"
        kaya "Mmmmhmmmmffff!!!"
        "[kaya.possessive_title] gives out a moaning, muffled affirmative. The vibrations and the eagerness of her mouth are going to make you cum!"
        mc.name "Oh fuck that's it, here it comes!"
        $ kaya.cum_in_mouth()
        $ kaya.increase_opinion_score("drinking cum", weighted = True)
        $ scene_manager.update_actor(kaya, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
        "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [kaya.hair_description]."
        "[erica.title] just watches quietly, a hint of jealousy on her face."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = kaya)
        $ mc.reset_arousal()
        "When you finish, [kaya.title] slides off and gasps for air. You give her a few moments."
        mc.name "[kaya.title], that was incredible. You didn't have to do that..."
        kaya "I know, I just couldn't let you go home like that! It looked so painful!"
        $ scene_manager.update_actor(kaya, position = "sitting", display_transform = character_left_flipped)
        "[kaya.possessive_title] slides back in her seat."
    "Finished with your questions, you have a pretty good idea of where to direct their study time."
    $ kaya.change_stats(happiness = 2, love = 2, max_love = 40)
    $ erica.change_stats(happiness = 2, love = 2, max_love = 40)
    erica "Wow, that was really helpful. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help, and it was fun too!"
    mc.name "Alright, you girls can take it from here?"
    erica "Sure can."
    mc.name "Alright, I'll see myself out then."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    "It is late, and you start your walk home."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_05
    return

label kaya_erica_teamup_scene_4(the_group, scene_transition = False):
    mc.name "Let's get to studying. Let's go over the rules."
    mc.name "Two questions each. After all the questions, if you girls got more right than wrong, you get to do whatever you want with me."
    mc.name "If it is two and two or if you got more wrong than right, you are both mine. Ready?"
    kaya "Got it."
    erica "Alright, let's do this!"
    "Always competitive, [erica.possessive_title] seems excited by the challenge, while [kaya.title] seems calm but determined."
    mc.name "Okay, [kaya.title], here we go."
    $ correct_count = 0
    $ kaya_count = 0
    $ erica_count = 0

    mc.name "[kaya.title], you're up first."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_final_question_01
    if _return:
        $ correct_count += 1
        $ kaya_count += 1
        erica "Yes! Good one [kaya.fname]!"
    else:
        kaya "Noooo! I swear I had it..."
        mc.name "Definitely not."

    mc.name "Alright [erica.title], your turn."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_final_question_02
    if _return:
        $ correct_count += 1
        $ erica_count += 1
        kaya "I knew you had that one!"
    else:
        erica "What!?! Are you sure?"
        mc.name "Yes, I am certain."

    mc.name "[kaya.title], your second question."
    call kaya_erica_teamup_question_label(kaya) from _kaya_erica_teamup_final_question_03
    if _return:
        $ correct_count += 1
        $ kaya_count += 1
        erica "Yes! Way to go [kaya.fname]!"
    else:
        kaya "Noooo! I swear I had it..."
        mc.name "Definitely not."

    mc.name "Alright [erica.title], last question of the night."
    call kaya_erica_teamup_question_label(erica) from _kaya_erica_teamup_final_question_04
    if _return:
        $ correct_count += 1
        $ erica_count += 1
        kaya "Hooray!"
    else:
        erica "What!?! Are you sure?"
        mc.name "Yes, I am certain."
    "Alright, quiz time is over, now it's time for fun."
    if correct_count == 0:
        "You shake your head. They didn't get a single question right."
        mc.name "I'm disappointed. I thought I had trained you girls better than that."
        "They look at you in dismay."
        mc.name "I guess I'll see if I trained you any better in the act of servicing a man. Get on your knees, both of you."
        kaya "Yes sir..."
        "You stand up and get your cock out as the girls get down on their knees."
        call start_threesome(kaya, erica, start_position = threesome_double_blowjob, position_locked = True) from _kaya_erica_punishment_threesome_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            "You enjoy your post-orgasm bliss for a few moments while [erica.possessive_title] and [kaya.possessive_title] get up."
        else:
            "Finished for now, you decide to put your cock away while [erica.possessive_title] and [kaya.possessive_title] get up."
        $ scene_manager.update_actor(kaya, position="stand3", display_transform = character_center_flipped)
        $ scene_manager.update_actor(erica, position = "stand4", display_transform = character_right)
    elif correct_count == 1:
        "You shake your head."
        mc.name "Well, at least one of you got a question right."
        if kaya_count > 0:
            mc.name "[kaya.title], since you got one right, you get my cock. Get on your hands and knees, you can eat out [erica.title] while I fuck you."
            kaya "Oh! Yes I love it when you rough me up from behind..."
            call start_threesome(erica, kaya, start_position = Threesome_doggy_deluxe, position_locked = True) from _kaya_erica_punishment_threesome_02
            $ the_report = _return
        else:
            mc.name "[erica.title], since you got one right, you get my cock. Get on your hands and knees, you can eat out [kaya.title] while I fuck you."
            kaya "Oh, this is gonna be fun!"
            call start_threesome(kaya, erica, start_position = Threesome_doggy_deluxe, position_locked = True) from _kaya_erica_punishment_threesome_03
            $ the_report = _return
        if the_report.get("trifecta", False):
            "You slowly recover with the girls. They both had orgasms, and you are recovering from yours also."
        "Finished for tonight, you decide to put your cock away while [erica.possessive_title] and [kaya.possessive_title] get up."
        $ scene_manager.update_actor(kaya, position="stand3", display_transform = character_center_flipped)
        $ scene_manager.update_actor(erica, position = "stand4", display_transform = character_right)
    elif correct_count == 2:
        mc.name "Not bad. You got half of them right. But by the rules, you are both still mine for the night."
        erica "Oh boy!"
        kaya "Hush, this is supposed to be a punishment, remember?"
        "[erica.title] chuckles."
        erica "Right. I meant, oh no! He's going to have his way with us!"
        call start_threesome(kaya, erica) from _kaya_erica_punishment_threesome_04
        $ the_report = _return
        if the_report.get("trifecta", False):
            "You slowly recover with the girls. They both had orgasms, and you are recovering from yours also."
        "Finished for tonight, you decide to put your cock away while [erica.possessive_title] and [kaya.possessive_title] get up."
        $ scene_manager.update_actor(kaya, position="stand3", display_transform = character_center_flipped)
        $ scene_manager.update_actor(erica, position = "stand4", display_transform = character_right)
    elif correct_count == 3:
        mc.name "Alright, you got three out of four. How do you girls want to do this?"
        if kaya_count == 2:
            erica "Well, [kaya.fname] got both of hers right... I say we should just focus on her!"
            kaya "That's okay, you really don't have..."
            "You stand up."
            mc.name "Excellent plan, let's reward [kaya.title] for doing such a good job!"
            call start_threesome(erica, kaya, start_position = Threesome_standing_embrace, position_locked = True) from _kaya_erica_punishment_threesome_05
            $ the_report = _return
            if the_report.get("girl two orgasms", 0) >= 2:
                $ scene_manager.update_actor(kaya, position = "doggy", display_transform = character_center_flipped)
                "When you finish holding her up, [kaya.possessive_title] collapses to the floor."
                "Her multiple orgasms have left her completely drained. Her breathing is ragged as she tries to recover from the pleasure."
                kaya "That was... fucking amazing... holy..."
                $ kaya.change_stats(happiness = 5, love = 5, obedience = 5)
                "Eventually, she starts to recover."
        else:
            kaya "Well, [erica.fname] got both of hers right... we should make her cum like crazy!"
            erica "That's okay, you really don't have..."
            "You stand up."
            mc.name "Excellent plan, let's reward [erica.title] for doing such a good job!"
            call start_threesome(kaya, erica, start_position = Threesome_standing_embrace, position_locked = True) from _kaya_erica_punishment_threesome_06
            $ the_report = _return
            if the_report.get("girl two orgasms", 0) >= 2:
                $ scene_manager.update_actor(erica, position = "doggy", display_transform = character_right)
                "When you finish holding her up, [erica.possessive_title] collapses to the floor."
                "Her multiple orgasms have left her completely drained. Her breathing is ragged as she tries to recover from the pleasure."
                erica "That was... fucking amazing... holy..."
                $ erica.change_stats(happiness = 5, love = 5, obedience = 5)
                "Eventually, she starts to recover."
        "Finished for tonight, you decide to put your cock away while [erica.possessive_title] and [kaya.possessive_title] get up."
        $ scene_manager.update_actor(kaya, position="stand3", display_transform = character_center_flipped)
        $ scene_manager.update_actor(erica, position = "stand4", display_transform = character_right)
    else:
        mc.name "Wow, you got them all right..."
        kaya "Yes!"
        erica "We've been studying hard!"
        kaya "Now you're all ours..."
        "The girls look at each other for a second."
        kaya "Who gets the uummm... you know..."
        erica "Go for it. I want to sit on his face anyway."
        "Oh fuck."
        kaya "Ha! Alright [kaya.mc_title], get your dick out and get on the table!"
        "You quickly comply and lay down on the table. [kaya.title] climbs on your lap while [erica.possessive_title] approaches your head."
        call start_threesome(kaya, erica, start_position = Threesome_double_down, position_locked = True) from _kaya_erica_punishment_threesome_07
        $ the_report = _return
        if the_report.get("trifecta", False):
            "You slowly recover with the girls. They both had orgasms, and you are recovering from yours also."
            $ kaya.change_stats(happiness = 5, obedience = 5)
            $ erica.change_stats(happiness = 5, obedience = 5)
        "Finished for tonight, you decide to put your cock away while [erica.possessive_title] and [kaya.possessive_title] get up."
        $ scene_manager.update_actor(kaya, position="stand3", display_transform = character_center_flipped)
        $ scene_manager.update_actor(erica, position = "stand4", display_transform = character_right)
    erica "Wow, that was a great session. Thanks, [erica.mc_title]!"
    kaya "Yes! Thank you so much, I feel like this has been a big help, and it was fun too!"
    mc.name "You're talking about the study session... right?"
    erica "Study?"
    kaya "Yes! Yes of course, a fantastic study session."
    "You stand up and leave the study room, waving goodbye to the girls."
    $ scene_manager.clear_scene()
    "It is late, and you start your walk home."
    $ mc.change_location(bedroom)
    call advance_time from _call_advance_kaya_erica_teamup_adv_06
    return

label kaya_erica_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label kaya_erica_trans_scene_1(the_group):
    "You are just getting ready to tell the girls you are going to help when [kaya.title] speaks up."
    kaya "You know, it is really nice of you to do this, but I kind of feel bad."
    erica "About what?"
    kaya "Like... he runs a business, and he is taking time out of his day to help us study, for free too, you know?"
    erica "Yeah..."
    "The girls seem to feel bad about taking up your time. You wonder if you could push their boundaries a bit..."
    mc.name "You know, there might be a way to make our study time more interesting for me, that would also help you two study a bit more."
    kaya "Oh?"
    "[erica.title] looks at you with a slight smirk. She seems to have an inkling of what you are about to suggest."
    mc.name "How about if we make it a type of competition? I'll ask you both three questions each. For each wrong answer, you'll have to take off a piece of clothing."
    kaya "Oh my..."
    "[erica.title]'s face turns to a wide smile."
    mc.name "With three questions each, I'll be able to make more personal recommendations on what to study, and if you get the questions wrong, I get to look at something nice for a bit."
    kaya "That's pretty... oh my..."
    erica "Sounds good to me!"
    kaya "It... it does?"
    erica "Sure! It's not like he's going to get us completely naked, and I think it's only fair for him."
    kaya "That's true."
    "[kaya.possessive_title] thinks about it for a few more moments."
    kaya "Okay. I'm willing to study like that from now on."
    "Nice! These study sessions just got a lot more interesting!"
    return

label kaya_erica_trans_scene_2(the_group):
    "The two girls look at you with expectant faces. It seems they are excited to get started. Maybe it is time to push things to the next level?"
    "It's worth a try anyway."
    mc.name "Yes. The rules. I'm not sure they are still effective."
    kaya "What do you mean?"
    mc.name "I mean... both of you seem to be excited to start study time... is it really a punishment if I ask you to take off clothes if you LIKE it?"
    erica "Ha! I suppose not."
    kaya "That... no I guess it isn't."
    mc.name "I think we've all gotten pretty comfortable with each other. I think it is about time to step things up a little bit. Make the punishment more punishing."
    erica "What do you have in mind?"
    mc.name "I propose we keep the same three questions each, but start with you girls in just your panties."
    mc.name "Then, for every wrong answer, you have to bend over and get a spanking from me."
    kaya "Wow..."
    "The girls look at each other for a few moments, processing your request. Neither wants to be the first to blink."
    "It seems that while they have become good friends, there is a bit of a competition beginning to form between them. Neither wants to be the first to back down."
    erica "I'll do it."
    kaya "I... I'll do it too."
    "FUCK YES. You can't wait to manhandle their tight little asses..."
    mc.name "Alright, well... the start conditions are for you both to be in just your panties."
    "The two hot college coeds start to strip down."
    $ scene_manager.strip_to_underwear(visible_enough = False)
    $ scene_manager.strip_to_tits(visible_enough = False)
    $ mc.change_locked_clarity(50)
    "Wow. This is going to be a fantastic study session."
    return

label kaya_erica_trans_scene_3(the_group):
    "The two girls look at you with obvious desire in their eyes as they await your answer."
    "So far, the girls have been getting all the attention, and it is clear that even with spanking, they are starting to like it a little too much to be an effective punishment."
    mc.name "You are both far too eager for this. I think it is time to change things up again."
    kaya "Yes? What do you have in mind?"
    mc.name "This time, I think that if you get a question wrong, you should service me orally while I ask the other person their question."
    "The girls look at you in surprise. Neither of them seems necessarily disgusted by the idea, but they both seem to be shocked that you would be so forward with them."
    if kaya.get_opinion_score("giving blowjobs") < 0:
        kaya "But... I don't even like giving blowjobs..."
        if erica.get_opinion_score("giving blowjobs") < 0:
            erica "Yeah, me neither..."
    elif erica.get_opinion_score("giving blowjobs") < 0:
        erica "What? I don't even like giving blowjobs!"
    else:
        kaya "What? That would be like... so embarrassing!"
    mc.name "Which is why it would be an effective punishment for getting a question wrong."
    mc.name "Plus, all this teasing and spanking is taking a toll on me. It's about time I start getting something out of these sessions, isn't it?"
    kaya "But like, what if we get several wrong and you... you know... finish..."
    mc.name "Then I guess whoever got the last question wrong will get a mouthful."
    "[kaya.title] looks at [erica.possessive_title] with skepticism. When you look at [erica.title] though... did she just lick her lips?"
    "[kaya.possessive_title] seems almost ready to say no, but appears to get a sudden burst of courage."
    kaya "Screw it. My grade has gone way up in this class since we started this, and if [kaya.mc_title] actually gets off, then I should have just studied harder."
    erica "You know I'm up for it!"
    kaya "Of course you are, you little cocksucker!"
    "[kaya.title] teases her friend. You can't believe it, they are actually going to do it!"
    $ mc.change_locked_clarity(50)
    return

label kaya_erica_trans_scene_4(the_group):
    "[erica.title] licks her lips. The girls are anxiously awaiting your response."
    "They both seem eager to suck your cock. Are they even here to study anymore? Is ANY sexual punishment going to actually work on them anymore?"
    "Suddenly you realize something. You are going about this all wrong. You shouldn't be punishing them for getting questions wrong..."
    mc.name "I think it is time for another rule change."
    kaya "Oh?"
    erica "OH! Good idea! Maybe when we get one wrong you could stick your..."
    mc.name "No. It is clear to me that I have been going about this all wrong."
    erica "Wrong?"
    mc.name "I've been using negative reinforcement for wrong answers, when I should have been doing the opposite."
    mc.name "This time, whoever gets the most right answers gets a reward."
    kaya "Is that so? And what is the reward?"
    mc.name "I'll fuck whoever gets the most right."
    erica "Oh! Damn that IS a good rule change!"
    kaya "Hang on... what if we both get them all correct?"
    mc.name "Oh... umm... I guess I'll just have to fuck you both."
    kaya "Ha! Yeah right. Can you even keep up with two college girls at the same time?"
    erica "Ummm, yeah... yeah he probably can..."
    erica "We've been working out a lot together. He has some pretty serious stamina [kaya.fname]..."
    "[erica.possessive_title]'s inflection makes it clear that by working out, she means having sex."
    kaya "Oh! Ah... I see."
    "The girls look at each other, but it is clear from their facial expressions that they both want to say yes, but are afraid to."
    "Finally, the silence breaks."
    kaya "I have another idea."
    "You are surprised, but she quickly continues."
    kaya "[erica.fname]... I don't want either of us to get left out. How about we work together... as a team?"
    kaya "You still have to fuck both of us no matter what."
    kaya "But if between the two of us, we got more right than we got wrong, WE get to pick the postion? If we don't, you get to use us both however you want."
    if not kaya.vagina_visible:
        $ scene_manager.strip_to_vagina(kaya)
        "As she finishes talking, you notice [kaya.title] is already stripping off her panties."
    "You can't believe it... [kaya.possessive_title] just suggested a mandatory threesome!"
    $ mc.change_locked_clarity(100)
    erica "Ohhh... [kaya.fname]. You are so sweet."
    erica "I'm down for that! What do you think [erica.mc_title]? I feel like no matter what happens it'll be a happy ending for you!"
    mc.name "Yes, I think those terms are acceptable. Let's get started!"
    if not erica.vagina_visible:
        $ scene_manager.strip_to_vagina(erica)
        "Noticing her study partner is already naked, [erica.title] slips off her panties."
    return

label kaya_erica_teamup_study_choice(the_group):
    kaya "Are you going to stick around and help us study tonight?"
    if kaya_erica_teamup.get_stage() > 0:
        erica "Don't worry, we haven't forgotten the rules..."
        if kaya_erica_teamup.get_stage() == 2:
            "The girls' bodies on display in front of you makes it obvious they are ready for your firm punishments."
        elif kaya_erica_teamup.get_stage() == 3:
            "[erica.title] licks her lips, obviously already thinking about her 'punishments'."
        elif kaya_erica_teamup.get_stage() == 4:
            "The sexual tension in the room is intense. It is obvious the girls are here for what happens after the study session primarily..."
    "Do you want to stick around and help the girls study?"
    menu:
        "Help them study {image=gui/heart/Time_Advance.png}":
            "You slide closer to the table, ready to help the girls with their study session."
            $ scene_manager.update_actor(kaya, display_transform = character_left_flipped)
            return True
        "Leave":
            return False
    return True

label kaya_erica_teamup_exit_scene(the_group):
    mc.name "Unfortunately, I don't have time to help study tonight, but wanted to swing by and just say hello."
    kaya "Ah, okay. Well thanks for stopping in!"
    "You stand up and leave the room, leaving the girls to their study session."
    $ scene_manager.clear_scene()
    return

#This is for reusable scenes and functions required for the teamup.

label kaya_erica_teamup_get_drinks_label():
    "You take the two girls water bottles and find a drinking fountain."
    "You fill up their water bottles, then take a look around. No one would notice if you added some serum to their waters."
    menu:
        "Add serum to [kaya.title]'s drink":
            call give_serum(kaya) from _call_give_serum_kaya_study_night_111
            if _return:
                "You mix the serum into [kaya.possessive_title]'s water."
            else:
                "You decide not to give her any for now."
        "Leave her drink alone":
            "You decide not to give her any for now."
    menu:
        "Add serum to [erica.title]'s drink":
            call give_serum(erica) from _call_give_serum_erica_study_night_111
            if _return:
                "You mix the serum into [erica.possessive_title]'s water."
            else:
                "You decide not to give her any for now."
        "Leave her drink alone":
            "You decide not to give her any for now."
    "You return to the study room with the water bottles."
    return

label kaya_erica_teamup_question_label(the_person, active_punishment = False, punished_person = None):
    "You look at [the_person.title]. It is their turn for a question."
    menu:
        "Try to stump her":
            if active_punishment and mc.arousal_perc >= 100 and kaya_erica_teamup.get_stage() == 3:
                "You try to come up with an impossible question, but the soft lips of [punished_person.possessive_title] are too hard to ignore any longer."
                mc.name "One second..."
                "You grab [punished_person.title]'s head with both hands as you feel yourself getting ready to cum."
                mc.name "Oh fuck... that's it, here it comes..."
                $ punished_person.cum_in_mouth()
                $ scene_manager.update_actor(punished_person, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
                $ punished_person.increase_opinion_score("drinking cum", weighted = True)
                "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [punished_person.hair_description]."
                "[the_person.title] just watches quietly, a hint of jealousy on her face."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = punished_person)
                $ mc.reset_arousal()
                "When you finish, [punished_person.title] slides off and gasps for air. You give her a few moments."
                mc.name "Alright, back to work, I haven't asked [the_person.title] her question yet."
                "She almost protests, but [punished_person.title] relents and start to suck on your rapidly softening cock."
            if the_person.int > mc.int:
                "You try to come up with a nearly impossible question."
                mc.name "Alright, how about this."
                if active_punishment and kaya_erica_teamup.get_stage() == 3:
                    "After you finish with the question, you look down at [punished_person.title]. You use your hand on her head to guide her hot little mouth up and down your cock."
                elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                    "When you finish the question, you give [punished_person.title]'s ass another spank. The slapping noise echoes in the small room."
                "When you finish stating the question, [the_person.title] gives you a smirk and easily comes up with the correct answer."
                mc.name "That's correct."
                return True
            else:
                if renpy.random.randint(0,100) < (mc.int - the_person.int) * 25:    #- 25% chance of answering correctly per int greater than person
                    "You try to come up with a nearly impossible question."
                    mc.name "Alright, how about this."
                    if active_punishment and kaya_erica_teamup.get_stage() == 3:
                        "After you finish with the question, you look down at [punished_person.title]. You use your hand on her head to guide her hot little mouth up and down your cock."
                    elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                        "When you finish the question, you give [punished_person.title]'s ass another spank. The slapping noise echoes in the small room."
                    "[the_person.title] mumbles for a few minutes, trying to remember a prior lecture or book passage."
                    "Eventually she mumbles out an answer that is obviously incorrect."
                    mc.name "That's incorrect."
                    return False
                else:
                    "You try to come up with a nearly impossible question."
                    mc.name "Alright, how about this."
                    if active_punishment and kaya_erica_teamup.get_stage() == 3:
                        "After you finish with the question, you look down at [punished_person.title]. You use your hand on her head to guide her hot little mouth up and down your cock."
                    elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                        "When you finish the question, you give [punished_person.title]'s ass another spank. The slapping noise echoes in the small room."
                    "When you finish stating the question, [the_person.title] gives you a smirk and easily comes up with the correct answer."
                    mc.name "That's correct."
                    return True
        "Give her a tough question":
            if active_punishment and mc.arousal_perc >= 100 and kaya_erica_teamup.get_stage() == 3:
                "You try to come up with a fair question, but the soft lips of [punished_person.possessive_title] are too hard to ignore any longer."
                mc.name "One second..."
                "You grab [punished_person.title]'s head with both hands as you feel yourself getting ready to cum."
                mc.name "Oh fuck... that's it, here it comes..."
                $ punished_person.cum_in_mouth()
                $ punished_person.increase_opinion_score("drinking cum", weighted = True)
                $ scene_manager.update_actor(punished_person, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
                "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [punished_person.hair_description]."
                "[the_person.title] just watches quietly, a hint of jealousy on her face."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = punished_person)
                $ mc.reset_arousal()
                "When you finish, [punished_person.title] slides off and gasps for air. You give her a few moments."
                mc.name "Alright, back to work, I haven't asked [the_person.title] her question yet."
                "She almost protests, but [punished_person.title] relents and start to suck on your rapidly softening cock."
            "You give [the_person.title] a firm but fair question."
            if renpy.random.randint(0,100) < the_person.int * 10:   #10% chance of answering correctly per intelligence
                mc.name "Alright, how about this."
                if active_punishment and kaya_erica_teamup.get_stage() == 3:
                    "After you finish with the question, you look down at [punished_person.title]. You use your hand on her head to guide her hot little mouth up and down your cock."
                elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                    "When you finish the question, you give [punished_person.title]'s ass another spank. The slapping noise echoes in the small room."
                "[the_person.title] struggles for a few moments, but suddenly remembers from a prior lecture or book reading and answers correctly."
                mc.name "That's correct."
                return True
            else:
                mc.name "Alright, how about this."
                if active_punishment and kaya_erica_teamup.get_stage() == 3:
                    "After you finish with the question, you look down at [punished_person.title]. You use your hand on her head to guide her hot little mouth up and down your cock."
                elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                    "When you finish the question, you give [punished_person.title]'s ass another spank. The slapping noise echoes in the small room."
                "[the_person.title] mumbles for a few minutes, trying to remember a prior lecture or book passage."
                "Eventually she mumbles out an answer that is obviously incorrect."
                mc.name "That's incorrect."
                return False
            pass
        "Give her an easy question":
            if active_punishment and mc.arousal_perc >= 100 and kaya_erica_teamup.get_stage() == 3:
                "You try to come up with an easy question, but the soft lips of [punished_person.possessive_title] are too hard to ignore any longer."
                mc.name "One second..."
                "You grab [punished_person.title]'s head with both hands as you feel yourself getting ready to cum."
                mc.name "Oh fuck... that's it, here it comes..."
                $ punished_person.cum_in_mouth()
                $ punished_person.increase_opinion_score("drinking cum", weighted = True)
                $ scene_manager.update_actor(punished_person, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.2))
                "You deliver spurt after spurt of your cum down her throat before finally relaxing your grip on her [punished_person.hair_description]."
                "[the_person.title] just watches quietly, a hint of jealousy on her face."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = punished_person)
                $ mc.reset_arousal()
                "When you finish, [punished_person.title] slides off and gasps for air. You give her a few moments."
                mc.name "Alright, back to work, I haven't asked [the_person.title] her question yet."
                "She almost protests, but [punished_person.title] relents and start to suck on your rapidly softening cock."
            "You decide for now to give her an easy question."
            mc.name "Alright, how about this."
            if active_punishment and kaya_erica_teamup.get_stage() == 3:
                "[punished_person.title] pulls off for a second to protest."
                punished_person "Seriously? You're gonna give her an easy one? That is so..."
                "You grab [punished_person.possessive_title] by the hair and force her back down on your cock, cutting off her complaint."
                $ punished_person.change_stats(happiness = -2, obedience = 3)
                $ play_gag_sound()
                "She gags for a second, but soon resumes her punishment, pleasuring you with her mouth."
            elif active_punishment and kaya_erica_teamup.get_stage() == 2:
                punished_person "Seriously? You're gonna give her an easy one? That is so..."
                $ play_spank_sound()
                "You deliver a smack to her ass, using more force than usual this time. She yelps and quickly shuts up."
                $ punished_person.change_stats(happiness = -2, obedience = 3)
            "[the_person.title] immediately gives you the correct answer."
            mc.name "That's correct."
            return True
    return true

label kaya_erica_teamup_spank_ass_condition(the_person, spank_count):
    if the_person == kaya:
        if spank_count == 1:
            "[the_person.possessive_title]'s ass shows just the lightest hint of pink on her dark skin."
            "She trembles a moment when her spanking is complete."
        elif spank_count == 2:
            "[the_person.possessive_title]'s ass shows a bit red as the result of your spanking."
            "She whimpers a moment, trembling when her spanking is complete."
        else:
            "[the_person.possessive_title]'s ass glows bright red, despite her dark skin."
            "She whimpers and trembles when her spanking is complete."
            mc.name "Maybe next week you'll actually study, unless you like getting your ass whipped like this?"
    elif the_person.skin == "black": #TODO three variants all base on the_person.skin for serum alterations
        if spank_count == 1:
            "[the_person.possessive_title]'s ass shows just the lightest hint of pink on her dark skin."
            "She trembles a moment when her spanking is complete."
        elif spank_count == 2:
            "[the_person.possessive_title]'s ass shows a bit red as the result of your spanking."
            "She whimpers a moment, trembling when her spanking is complete."
        else:
            "[the_person.possessive_title]'s ass glows bright red, despite her dark skin."
            "She whimpers and trembles when her spanking is complete."
            mc.name "Maybe next week you'll actually study, unless you like getting your ass whipped like this?"
    else:
        if spank_count == 1:
            "[the_person.possessive_title]'s tight ass shows just the lightest hint of pink."
            "She mutters under her breath when her spanking is complete."
        elif spank_count == 2:
            "[the_person.possessive_title]'s fit ass shows a bit red as the result of your spanking."
            "She whimpers a moment, trembling when her spanking is complete."
        else:
            "[the_person.possessive_title]'s ass glows bright red as a result of your firm punishment."
            "She whimpers and trembles when her spanking is complete."
            mc.name "Maybe next week you'll actually study, unless you like getting your ass whipped like this?"
    $ the_person.increase_opinion_score("being submissive", weighted = True)
    $ the_person.increase_opinion_score("showing her ass", weighted = True)
    return

label kaya_erica_teamup_blowjob_condition(inc_mouth = False, final = False):
    if mc.arousal_perc < 10: #post orgasm?
        "Your cock has gotten a little bit soft after cumming."
        if inc_mouth and not final:
            "You give it a couple strokes. It is already getting hard as the the other girl gets on her knees."
        elif final:
            "You are glad you got to get off before the end of the study session!"
        else:
            "You give a couple strokes, content that it'll get hard again if you get another wrong answer."
    elif mc.arousal_perc < 30:
        "Your cock is hard and aches a little bit when the cool air of the room hits it."
        if inc_mouth and not final:
            "Thankfully there is already another wrong answer, as you eagerly await the other girl's mouth to take over."
        elif final:
            "Your cock stands at attention, but thankfully you aren't TOO turned on, now that the questions are over."
        else:
            "Hopefully you can get another wrong answer soon."
    elif mc.arousal_perc < 75:
        "Your rock hard cock stands proudly, with the girls' slobber running down the sides of it."
        if inc_mouth and not final:
            "Thankfully there is already another wrong answer, and you look forward to having the other girl's mouth take over."
        elif final:
            "The cold air in the room hurts a little. You are really turned on, but unfortunately the night appears to be over."
        else:
            "You ache for another mouth to take over. You carefully consider upping the difficulty of the questions..."
    else:
        "Your painfully engorged cock twitches when the air hits it."
        if inc_mouth and not final:
            "As one girl starts to get up, the other girl approaches, getting ready to service you."
            "There is no way you'll make it through the next question without cumming. You can't wait to unload in her mouth soon!"
        elif final:
            "Both girls look at your cock in awe as it twitches, ready to burst. But unfortunately, the study session is over..."
            "You long for another mouth to take over and finish you off... Maybe you can..."
        else:
            "You long for another mouth to take over and finish you off."
            "It is obvious just by looking at it that whoever gets the next question wrong is probably going to get a mouthful of your cum."
    return
