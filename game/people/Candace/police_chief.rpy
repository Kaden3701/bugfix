init 5 python:
    add_label_hijack("normal_start", "create_police_chief")

    def police_chief_titles(person):
        valid_titles = ["Officer " + person.last_name]
        if person.love > 30:
            valid_titles.append("Officer " + person.name)
        if person.sluttiness > 40:
            valid_titles.append("Officer Cumslut")
        if person.sluttiness > 70:
            valid_titles.append("Officer Cornhole")
        return valid_titles

    def police_chief_possessive_titles(person):
        valid_possessive_titles = ["The police chief"]
        if person.love > 30:
            valid_possessive_titles.append("Your police chief")
        if person.sluttiness > 40:
            valid_possessive_titles.append("Your police bitch")
        if person.sluttiness > 70:
            valid_possessive_titles.append("Your anal cop")
        return valid_possessive_titles

    def add_police_chief_character():
        police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")
        cop_outfit = police_chief_wardrobe.get_outfit_with_name("Cop")

        global police_chief_uniform_wardrobe
        police_chief_uniform_wardrobe = Wardrobe("Cop Uniform")
        police_chief_uniform_wardrobe.add_outfit(cop_outfit)
        police_chief_wardrobe.remove_outfit(cop_outfit)

        police_chief_personality = Personality("police_chief", default_prefix = reserved_personality.default_prefix,
            common_likes = ["pants", "small talk", "working", "the colour blue", "the colour black", "boots", "sports", "working", "work uniforms"],
            common_sexy_likes = ["taking control", "anal sex", "sex standing up", "anal creampies", "getting head"],
            common_dislikes = ["Mondays", "the colour yellow", "the colour pink", "skirts", "dresses", "high heels", "flirting"],
            common_sexy_dislikes = ["being submissive", "bareback sex", "skimpy outfit", "showing her tits", "showing her ass", "not wearing underwear", "cum facials", "incest"],
            titles_function = police_chief_titles, possessive_titles_function = police_chief_possessive_titles, player_titles_function = reserved_player_titles)

        police_job = Job("Police Chief", critical_job_role, police_station, work_times = [1, 2])
        police_job.schedule.set_schedule(mall, the_days = [0,2,4], the_times = [1]) #patrol mall
        police_job.schedule.set_schedule(downtown, the_days=[1,3], the_times=[2]) # patrol downtown
        police_job.schedule.set_schedule(downtown_bar, the_days=[5,6], the_times=[3]) # patrol bar
        police_job.schedule.set_schedule(strip_club, the_days=[5,6], the_times=[4]) # patrol strip club (Does she have a kinky side?)

        global police_chief
        police_chief = make_person(name = "Christine", last_name = "Lavardin", age = 34, body_type = "thin_body", face_style = "Face_4", tits = "C", height = 0.91, \
            hair_colour = ["knight red", [.745, .117, .235, 1]], hair_style = short_hair, skin="white", eyes = "emerald", name_color = "#fcf7de",  \
            stat_array = [4,6,2], skill_array = [2,1,4,1,2], sex_skill_array = [0,1,1,4], sluttiness = -20, obedience_range = [50, 70], happiness = 89, love = 0, \
            generate_insta = False, generate_dikdok = False, generate_onlyfans = False, relationship = "Single", job = police_job, \
            kids = 0, force_random = True, starting_wardrobe = police_chief_wardrobe, personality = police_chief_personality, type = 'story',
            forced_opinions = [
                ["pants", 2, False],
                ["the colour blue", 2, True],
                ["the colour black", 1, False],
                ["boots", 2, False],
                ["sports", 1, True],
                ["working", 2, False],
                ["work uniforms", 2, True],
            ], forced_sexy_opinions = [
                ["taking control", 2, False],
                ["anal sex", 2, False],
                ["sex standing up", 1, False],
                ["being submissive", -2, False],
                ["skimpy outfits", -2, False],
                ["showing her tits", -1, False],
                ["showing her ass", -1, False],
                ["not wearing underwear", -2, False],
            ])
        police_chief.idle_pose = "stand3"   # forced idle pose
        police_chief.generate_home()
        police_chief.home.add_person(police_chief)
        police_chief.event_triggers_dict["times_arrested"] = 0
        return

label create_police_chief(stack):
    python:
        add_police_chief_character()
        execute_hijack_call(stack)
    return

label police_chief_introduction(the_person):
    mc.name "Excuse me, officer?"
    "She looks up and measures you with a methodical glance."
    $ the_person.set_title("???")
    the_person "Yes citizen, how can I be of service?"
    mc.name "Ah yes, how may I address you?"
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Well then, you can address me as [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    "[the_person.possessive_title] looks you straight in the eyes."
    the_person "What's your name, citizen?"
    return

label police_chief_greetings(the_person):
    if the_person.love < 0:
        the_person "Yes, citizen, how can I help you?"
    elif the_person.happiness < 90:
        the_person "Hello citizen, what's your problem?"
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], how can I be of assistance?"
            else:
                the_person "Hello [the_person.mc_title], what can I do for you today?"
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], is there something I can help you with?"
            else:
                the_person "Hello [the_person.mc_title], how can I help you today?"
    return

label police_chief_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "[the_person.possessive_title] steps back and moves her hand to her weapon."
        the_person "Stand back, Sir. Or else I could charge you with assaulting an officer."
        mc.name "I'm sorry, my mistake."
        "She seems more guarded, but you both try and move past the awkward moment."
    else: #Fail point for touching waist
        "[the_person.possessive_title] suddenly shifts, steps back and moves her hand to her weapon."
        the_person "Stand back, Sir. You need to keep your hands away from my weapon."
        "You pull your hands back and lift them half up in the air apologetically."
        mc.name "Of course, I'm sorry."
        the_person "Thank you, you should know it's very dangerous to reach for an officer's weapon."
        "She seems unconvinced, but decides not to say anything else."
    return

label police_chief_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] speaks quietly as you start to move her [the_clothing.display_name]."
    if the_person.obedience > 180:
        the_person "I... I'm sorry, but I can't take that part of my uniform off [the_person.mc_title]..."
    else:
        the_person "I really can't take that part of my uniform off [the_person.mc_title]..."
    return

label police_chief_flirt_response_low(the_person):
    "[the_person.possessive_title] seems caught off guard by the compliment."
    the_person "Oh, thank you! I'm just wearing my daily uniform."
    mc.name "Well, you make it look good."
    $ mc.change_locked_clarity(5)
    "She smiles and laughs self-consciously."
    the_person "Charmer!"
    return

label police_chief_flirt_response_mid(the_person):
    if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
        "[the_person.possessive_title] smiles, then glances around self-consciously."
        the_person "Keep your voice down [the_person.mc_title], there are other citizens around."
        mc.name "I'm sure they're all thinking the same thing."
        "She rolls her eyes and laughs softly."
        the_person "Maybe they are, but they are smart enough not to say it out loud."
        $ mc.change_locked_clarity(10)
        the_person "You'll have better luck if you save your flattery for when we're alone."
        mc.name "I'll keep that in mind."
    else:
        "[the_person.possessive_title] gives a subtle smile and nods her head."
        the_person "Thank you [the_person.mc_title]. I'm happy you like to see me in uniform."
        the_person "How does it look when I'm walking away?"
        $ the_person.draw_person(position = "walking_away")
        $ mc.change_locked_clarity(10)
        "She just keeps on walking, did you go too far?"
        mc.name "You have an amazing swag in your step, I wouldn't mind walking behind you."
        $ the_person.draw_person()
        "She turns around and smiles warmly."
    return

label police_chief_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "[the_person.mc_title], there are other citizens around."
        "She bites her lip and leans close to you, whispering in your ear."
        $ mc.change_locked_clarity(15)
        the_person "But if we were alone, I'm sure we could figure something out..."
        menu:
            "Find someplace quiet":
                mc.name "Follow me."
                "[the_person.possessive_title] nods and follows a step behind you."
                "After searching for a couple of minutes you find a quiet, private space."
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person "Well? You better plan you next move carefully..."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She closes her eyes and leans her body against yours."
                else:
                    "You answer with a kiss. She closes her eyes and leans her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_police_chief_response_high
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person "You're a smart man, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.person_count == 1: #She's shy but you're alone
            "[the_person.title] blushes and stammers out a response."
            the_person "I... I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide how you feel. I feel the same way."
            "She nods and takes a deep breath, steadying herself."
            the_person "Okay. You're right. What... do you want to do then?"

        else:  #You're not alone, but she doesn't care.
            the_person "Well I wouldn't want you to run amok. You'll just have to convince me to get me out of this uniform..."
            $ mc.change_locked_clarity(15)
            if the_person.has_large_tits: #Bounces her tits for you
                $ the_person.draw_person(the_animation = tit_bob)
                "[the_person.possessive_title] bites her lip sensually and grabs her [the_person.tits_description], jiggling them for you."

            else: #No big tits, so she can't bounce them (as much
                "[the_person.possessive_title] bites her lip sensually and looks you up and down, as if mentally undressing you."

            $ the_person.draw_person()
            the_person "Well? You better plan you next move carefully..."

        menu:
            "Kiss her":
                "You step close to [the_person.title] and put an arm around her waist."
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She presses her body up against yours."
                else:
                    "When you lean in and kiss her she responds by pressing her body tight against you."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_person_police_chief_response_high2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "Not here, not right now, but I've got a few ideas I would like to run by you..."
                "If [the_person.title] has any feelings toward you, she does a good job hiding it, while staring in your eyes."
                the_person "Well maybe if you entertain me when I'm off-duty, you can enlighten me."
    return

label police_chief_public_sex_intervention(the_person):
    police_chief "Hey! What are you doing? You can't do that at the [mc.location.formal_name]!"
    $ police_chief.draw_person()
    "Suddenly, a police officer arrives. You stop what you are doing with [the_person.possessive_title]."
    police_chief "God, get decent. I'm taking you two downtown!"
    $ the_person.apply_planned_outfit()
    $ mc.change_location(police_station)
    $ scene_manager = Scene()
    $ scene_manager.add_actor(police_chief)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left_flipped)
    "You and [the_person.title] are escorted to the police station by the police officer. You spend a couple hours doing paperwork."
    call mc_arrested_penalties from _arrested_public_sex_01
    "You and [the_person.possessive_title] go your separate ways for now. She doesn't seem eager to chat about getting arrested."
    call advance_time from _call_advance_time_after_arrested_1
    jump game_loop
    return

label mc_arrested_penalties():
    if mc_times_arrested() == 0:
        $ mc.business.change_funds(-100)
        "Since this is your first offense, you get off with a light fine."
        $ police_chief.event_triggers_dict["times_arrested"] = 0
    elif mc_times_arrested() == 1:
        $ mc.business.change_funds(-500)
        "Since this is your second offense, you get fined."
        police_chief "Seriously, don't do that again. You can't be doing that stuff in public!"
    elif mc_times_arrested() == 2:
        $ mc.business.change_funds(-5000)
        "Since this is your third offense, you receive a heavy fine."
        police_chief "I guess you still haven't learned your lesson. I'm fining you the maximum amount under the law."
        police_chief "If this happens again, I'll have to let the city know you got problems with authority. Catch my drift?"
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Damn, you just can't keep your hands to yourself, can you?"
        police_chief "Guess I'll have to call this in to the city. Where did you say you work again?"
        $ mc.business.attention += 20
    elif mc_times_arrested() == 3:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Still screwing around with whores in public are you?"
        police_chief "Guess last time I didn't word my request with the city strongly enough."
        $ mc.business.attention += 50
    else:
        $ mc.business.change_funds(-5000)
        "You once again receive a heavy fine."
        police_chief "Again. You're here AGAIN. "
        police_chief "Enough is enough. Get out of here, I'm sure the city will be checking out your business now soon enough."
        $ mc.business.attention += 100
    $ police_chief.event_triggers_dict["times_arrested"] += 1
    return
init 2 python:
    def mc_times_arrested():
        return police_chief.event_triggers_dict.get("times_arrested", 0)
