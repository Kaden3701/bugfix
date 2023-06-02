# Camilla's standard storyline is her lust series. It involves her hotwifing at the request of her husband.
# At first, she is hesistant, but with encouragement she engages in multiple sex acts with MC

init -1 python:
    def camilla_get_a_drink_requirement(the_person):
        if the_person.location == downtown_bar:
            if mc.business.change_funds > 20:
                return True
            else:
                return "Not enough money!"
        return False

    def camilla_dance_lessons_requirement():
        if day%7 == 2 and time_of_day == 3:
            return True
        return False

    def camilla_bathroom_blowjob_requirement(person):
        if person.sluttiness < 40:
            return False
        if not person.story_event_ready("slut"):
            return False
        if person.location != downtown_bar:
            return False
        return True

    def camilla_blowjob_text_requirement(the_person):
        if day >= camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 9999):
            return True
        return False

    def camilla_dancing_sex_requirement(person):
        if person.sluttiness < 60:
            return False
        if mc_dancing_skill() <= 6:
            return False
        if not person.story_event_ready("slut"):
            return False
        if person.location != downtown_bar:
            return False
        return True

    def camilla_sex_invite_requirement(person):
        if person.sluttiness < 80:
            return False
        if not person.story_event_ready("slut"):
            return False
        if person.location != downtown_bar:
            return False
        return True

    def camilla_her_place_requirement():
        if time_of_day == 4:
            return True
        return False

    def camilla_go_dancing_requirement(the_person):
        return False
        if the_person.location == downtown_bar and camilla.event_triggers_dict.get("bathroom_sex", False):
            return True
        return False

    def camilla_take_pics_requirement(the_person):
        if the_person.location == downtown_bar and not camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 0) == 0:
            return True
        return False

    def camilla_home_sex_requirement(the_person):
        if time_of_day == 4 and camilla.event_triggers_dict.get("home_sex", False):
            if the_person.is_home():
                return True
        return False

init 2 python:
    camilla_get_a_drink = Action("Get a drink {image=gui/heart/Time_Advance.png}", camilla_get_a_drink_requirement, "camilla_get_a_drink_label", is_fast = False)
    camilla_go_dancing = Action("Salsa Dancing", camilla_go_dancing_requirement, "camilla_go_dancing_label")
    camilla_take_pics = Action("Take Sexy Pics {image=gui/heart/Time_Advance.png}", camilla_take_pics_requirement, "camilla_take_pics_label", is_fast = False)
    camilla_dance_lessons = Action("Dancing Lessons", camilla_dance_lessons_requirement, "camilla_dance_lessons_label")
    camilla_bathroom_blowjob = Action("Bathroom Blowjob", camilla_bathroom_blowjob_requirement, "camilla_bathroom_blowjob_label")
    camilla_blowjob_text = Action("Blowjob Discussion", camilla_blowjob_text_requirement, "camilla_blowjob_text_label")
    camilla_dancing_sex = Action("First Sex", camilla_dancing_sex_requirement, "camilla_dancing_sex_label")
    camilla_sex_invite = Action("House Call", camilla_sex_invite_requirement, "camilla_sex_invite_label")
    camilla_her_place = Action("Cuckold Visit", camilla_her_place_requirement, "camilla_her_place_label")
    camilla_home_sex = Action("Cuckold Visit {image=gui/heart/Time_Advance.png}", camilla_home_sex_requirement, "camilla_home_sex_label", is_fast = False)


label camilla_get_a_drink_label(the_person):
    mc.name "Care to get a drink, [the_person.title]?"
    "You consider for a moment. If you offer to buy her a drink, you'll have a chance to slip a serum into it."
    $ ran_num = (mc.charisma + (the_person.effective_sluttiness() / 10)) * 10  #More willing to let you buy a drink for her as she gets sluttier
    #$ bartender_name = Person.get_random_male_name()
    if camilla.event_triggers_dict.get("bathroom_sex", False):
        $ ran_num = 100
    menu:
        "Offer to Buy\n{color=#ff0000}{size=18}Success Chance: [ran_num]%%{/size}{/color}":
            mc.name "Hey, let me buy you a drink."
            if renpy.random.randint(0,100) < ran_num:  #Success
                the_person "Hmm... Okay! That sounds great! I'll go find us a table!"
                "You head over to the bar and order yourself a beer, and a cocktail for [the_person.title]."
                the_person.SO_name "Here you go, one beer, and a cocktail for the beautiful [the_person.fname]."
                "Sounds like the bartender knows [the_person.title] pretty well. She must be in here often!"
                "The place is busy, so it's easy to slip some serum into her drink."
                call give_serum(the_person) from _call_give_serum_camilla_01
            else:                                 #Fail

                the_person "That's okay! I prefer to go dutch anyway."
                "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
                the_person "Hey there, [the_person.SO_name]! I'll have a flora dora tonight. You know how I like it!"
                "It sounds like she knows the bartender. She must be in here pretty often!"
        "Grab Drinks Separately":
            the_person "That's okay! I prefer to go dutch anyway."
            "You head over to the bar and order yourself a beer, [the_person.title] orders herself a fruity sounding cocktail."
            the_person "Hey there, [the_person.SO_name]! I'll have a flora dora tonight. You know how I like it!"
            "It sounds like she knows the bartender. She must be in here pretty often!"
    $ the_person.draw_person(position = "sitting")
    "You sit down at a table with [the_person.title]."

    #***Event State 0 ####
    if not camilla.event_triggers_dict.get("go_dancing", False):
        mc.name "Glad to see you here again. How have you been?"
        the_person "Pretty good. You?"
        mc.name "I'm doing well. Especially now that I have a chance to have a drink with a beautiful woman such as yourself."
        "She looks a little embarrassed, but doesn't respond negatively to your comment."
        mc.name "So, your hubby is okay with you going out to the bar all by yourself?"
        the_person "Si, he doesn't mind. In fact, he kind of encourages it."
        mc.name "Really? That's interesting."
        "[the_person.possessive_title] takes a sip of her drink and takes a moment."
        the_person "Truth be told, hubby has been encouraging me recently to umm... get out and meet new people... men specifically."
        "Her statement catches you a little bit by surprise."
        the_person "To be honest... I'm not sure I'm going to... but hubby has this fantasy thing where I... get with other guys..."
        "Ah her husband is some kind of cuckold."
        mc.name "That's interesting. Manage to snag any yet?"
        the_person "No. I'm... I just want to be a good wife... and honestly I never thought my hubby would ask me to do something like this."
        the_person "I'm still too nervous, but I like to come to the bar and have a couple drinks. Maybe someday I'll actually go through with it."
        "[the_person.possessive_title] takes another long sip of her drink."
        the_person "I don't know why but, it's nice being able to talk to you. Something about you puts me at ease."
        mc.name "Ah, I understand what you mean."
        mc.name "So, how's it going? Any luck with picking up guys?"
        if the_person.effective_sluttiness() >= 20:
            "[the_person.possessive_title] ignores your question and looks at you."
            the_person "Do you like salsa dancing?"
            mc.name "Ah, I'll admit, I've never really tried it."
            "[the_person.title] takes a sip of her drink."
            the_person "Did you know they do salsa dancing here sometimes? Even if you are new at it, it would be fun to try it sometime."
            the_person "On Wednesday nights they have a salsa dancing for beginners class. You should come and I'll go with you."
            "That sounds suspiciously like a date. With this smoking hot señorita in an open relationship, the implications are impossible to ignore."
            mc.name "Sure, I'll do it next Wednesday."
            the_person "Great!"
            "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
            $ mc.business.add_mandatory_crisis(camilla_dance_lessons)
            mc.name "Take care, I'll see you on Wednesday!"
        else:
            "[the_person.possessive_title] sighs."
            the_person "No, not yet. I'm just having a hard time getting myself to open up to that kind of thing."
            mc.name "Well, it is definitely not something you want to rush into."
            the_person "Yeah... he keeps telling me... he wants me to seduce a guy, and get pictures, to send him you know?"
            "Yep! He definitely sounds like a cuckold."
            the_person "But I don't know, I think maybe I just need a little more time."
            "Sounds like she might benefit from a few more doses of your serum, too..."
            "You chat with [the_person.title] for a bit longer, but soon it is time to leave."
            mc.name "Take care, I'm sure I'll see you here again sometime!"

    elif camilla.event_triggers_dict.get("camilla_blowjob_pic_day", 0) == 0:
        the_person "No dancing tonight?"
        mc.name "No, sometimes it is nice to just relax and have a drink."
        the_person "Yeah, I agree."
        "You chat with [the_person.possessive_title] for a bit."
        "There is definitely some sexual tension in the air between you two, but she knows she can talk to you about it when she is ready."
        $ mc.change_locked_clarity(10)

    elif not camilla.event_triggers_dict.get("bathroom_sex", False):
        mc.name "How are things going? Still going well with the husband?"
        the_person "Oh yes... I haven't had the guts to do anything with any other guys yet, but, those blowjob pictures definitely changed our sex life."
        mc.name "Good, glad to hear it's working out for you."
        the_person "Yeah... he umm... he's started asking me if, you know, I'm almost ready to take things to the next level..."
        mc.name "Oh yeah? Meaning what?"
        the_person "Well, you know, not just blowing a guy but, letting him fuck me..." #TODO Finish this
        "You just about choke on your drink."
        mc.name "Hey, I'd be glad to help out. But obviously, don't rush into it if you aren't ready yet."
        "[the_person.title] takes a long sip from her cocktail."
        the_person "Ay, caramba, [the_person.mc_title], I just don't think I'm ready."
        "You nod in understanding."
        the_person "But I'd be glad to, you know, get you off in the usual way..."
        mc.name "Sounds good. I'll try to look for you next time I'm around."
        $ mc.change_locked_clarity(20)

    elif not camilla.event_triggers_dict.get("home_sex", False):
        mc.name "How are things going? You husband happy with the pics we've been sending him?"
        the_person "Oh si... he loves the photos. And I love what he does to me after he gets them!"
        mc.name "Hah, that's good! I'm glad, it sounds like it has really spiced things up for you two."
        "[the_person.possessive_title] takes a long sip of her drink."
        "[the_person.title] clearly has something on her mind, but she doesn't seem to have the courage to speak up."
        "As far as things have gone with her, is her husband pushing her to go even farther?"
        the_person "Yeah, it has certainly worked wonders..."
        "You make small talk with [the_person.possessive_title] for a while. Eventually you finish your drinks and part ways."

    else:
        the_person "Thanks for the drink, [the_person.mc_title]. This whole adventure has really supercharged my sex life, it's nice to have a break from fucking and just enjoy a stiff drink."
        mc.name "Yeah, so is [the_person.SO_name] still enjoying your new lifestyle?"
        the_person "Oh god, we both are. I've started fucking around with a couple other guys too. Last time I came home, he tied me up and umm... reclaimed me in every hole he could fit it in..."
        mc.name "Damn! That sounds hot!"
        the_person "Yeah! I came so many times... you didn't forget my address did you? You should stop by sometime and we could fuck around again."
        mc.name "Don't worry, I haven't forgotten."
        "You and [the_person.title] finish your drinks and then you say goodbye."

    call advance_time from _call_advance_camilla_drink
    return

label camilla_dance_lessons_label():
    $ the_person = camilla
    $ camilla_wear_salsa_dress()
    $ scene_manager = Scene()
    $ the_person.story_event_log("lust")
    "It's Wednesday night, and you have a date with [the_person.possessive_title] at the bar to learn salsa dancing."
    $ mc.change_location(downtown_bar)
    "When you get there, you step inside. You see [the_person.title] at the bar, in a very nice dress."
    $ scene_manager.add_actor(the_person)
    "You walk over to her. When she sees you she smiles."
    the_person "Ah, señor! I wasn't sure that you would actually come!"
    mc.name "Of course. Sometimes we need to be adventurous and get out of our comfort zone to try something new."
    "When you finish your statement, you give her a wink. She immediately realizes you are commenting about her situation with her husband..."
    $ the_person.change_slut(2)
    the_person "You are right about that, but tonight, it is all about you!"
    "You make some idle chatter at the bar as you wait for the lessons to begin. You admit you are pretty nervous, but as people filter in, you see a lot of people around who also look new at this."
    "?????" "Alright, everyone here for salsa lessons, we are forming up over here! Come with your partner!"
    "You and [the_person.possessive_title] head over."
    "?????" "Alright, my name is Alvero, and I'll be your instructor tonight! First let's start off with a little..."
    "You listen intently as the instructor begins initial warm up instructions."
    "Finally, it's time to start dancing."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "You get close to [the_person.title] as the music starts. You listen as the instructor begins to issue commands."
    "Alvero" "Alright fellas, remember, your sole purpose while salsa dancing is to display the beautiful flower you are partners with."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
    "You try one of the moves as instructed, moving [the_person.possessive_title] away from you a bit and allowing her to make a graceful spin back to you."
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
    "She spins beautifully and stops with her back to you. She looks back and gives you a sly smile."
    if mc_dancing_skill() < 4:
        "Unfortunately you fumble a bit as she spins back out. You don't trip but you definitely feel awkward compared to the grace your partner is exhibiting."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Don't worry, we were all new at one time. You are doing great."
        $ the_person.change_stats(happiness = 2, love = 2)
    elif mc_dancing_skill() < 10:
        "You spin her back out the other side. She gracefully finishes her spin before returning to you."
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "You're doing great! I think you are a natural."
        $ the_person.change_stats(happiness = 2, love = 2, obedience = 2)
    else:
        "You easily lead her into a reverse spin out the other side the way the instructor led. Her skirt flares up as she spins gracefully and then returns to your side."
        $ mc.change_locked_clarity(10)
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] whispers in your ear."
        the_person "Are you sure this is your first time doing this? You have the manner of someone experienced sir..."
        $ the_person.change_stats(obedience = 5, love = 3)
    "As you continue your first salsa dancing lesson, that trend continues."
    if mc_dancing_skill() < 4:
        "You are bumbling and awkward, but you enjoy the chance to get close with this sexy señora."
        $ mc.change_locked_clarity(10)

    elif mc_dancing_skill() < 10:
        "While you don't have nearly the skill of your partner, you feel like you are learning fairly quick."
        "By the end of the night, you are spinning and dancing with [the_person.possessive_title]. While you still make a few mistakes, you are getting better."
        "It is nice to get so close and personal with this señora."
        $ mc.change_locked_clarity(20)
    else:
        "You take to salsa dancing like a natural. Throughout the night you have her spinning and moving to the music."
        "After a short time, you stop listening to the instructor and start doing things your own way. You lead [the_person.possessive_title] around the dance floor with authority."
        "At the end of the lesson, she is close to you again, breathless. A light sheen of sweat makes her skin shine."
        "Your hands on her body throughout the dancing has definitely put sexual tension in the air."
        $ mc.change_locked_clarity(30)
        $ the_person.change_slut(2, 50)
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "Tired from your evening, you chat with [the_person.possessive_title] before you leave."
    the_person "So, they do this most evenings here. If you ever want a dance partner, I love to dance!"
    mc.name "I'll remember that. It might be a good way to unwind a bit after a long day at work."
    "You can now take [the_person.title] dancing any evening she is at the bar."
    "To increase your skill at salsa dancing, increase your charisma and energy. You can check your salsa dancing skill from [the_person.fname]'s story progress screen!"
    $ camilla.event_triggers_dict["go_dancing"] = True
    $ scene_manager.clear_scene()
    $ camilla.add_unique_on_room_enter_event(camilla_bathroom_blowjob)
    call advance_time from _call_advance_camilla_post_dance_lesson_01

    return

label camilla_bathroom_blowjob_label(the_person):
    $ the_person.draw_person(position = "sitting")
    $ the_person.story_event_log("lust")
    "You walk into the bar. You immediately notice [the_person.possessive_title] sitting down, sipping on a cocktail."
    "You walk over and sit down beside her."
    mc.name "Good evening, señorita!"
    the_person "Buenas noches sir!"
    "You sit down and chat idly with her for a few minutes. Eventually the subject of her husband comes up."
    mc.name "So, any progress with the husband? And his request for... extracurricular activies?"
    the_person "Not yet... but I think I'm ready to. I'm just waiting for the right opportunity to come along."
    mc.name "Oh? What kind of opportunity are you waiting for?"
    the_person "I guess... I'm just waiting on the right guy to offer to umm... take some pics with me."
    "She lowers her voice to a whisper."
    the_person "You know I'm on a first name basis with the bartender? I'm pretty sure he would help cover for me with... whoever that guy happens to be."
    "This seems like an invitation."
    mc.name "Hey, so uhh... want me to take some pictures for you?"
    "You see a bright red flush in her cheeks, but she quickly nods."
    the_person "Si! I would like that... a lot!"
    "She takes a quick look around."
    the_person "Let me just go talk to the bartender... head to the lady's room and wait outside... I'll be over in a second."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks away to talk to the bartender. You make your way over to the lady's room."
    $ the_person.draw_person(position = "stand4")
    "Soon, [the_person.title] comes over, holding a sign that says 'Bathroom closed for renovations: Please use men's room"
    $ mc.change_location(work_bathroom)
    "You both take a quick look around, and when the coast is clear, you both walk into the bathroom and lock the door behind you."
    "You waste no time, you quickly wrap your arms around [the_person.title] and start making out with her."
    $ the_person.draw_person(position = "kissing")
    $ mc.change_locked_clarity(20)
    the_person "Mm... mmm... mmmmmmmmmff..."
    "She is moaning in your mouth. You can tell the naughtiness of finally getting intimate with someone other than her husband is really turning her on."
    $ the_person.change_arousal(10)
    the_person "Ok... wow this is hot. This is my first time ever doing something like this... so... I want you to just let me do my thing, ok?"
    "You quickly agree."
    the_person "Also, could you take my phone? And take some pictures for me? Papi asked me to..."
    "She is very awkwardly asking. You quickly answer like this is a completely normal request to put her at ease."
    mc.name "Of course! How else is daddy gonna know what his slutty girl has been up to?"
    "She smiles."
    the_person "Exactly!"
    "She hands you her phone with the camera app up."
    $ the_person.draw_person(position = "stand3")
    if not the_person.tits_available:    #If covered up, have her take her top off
        the_person "Here I go... don't forget to take pictures!"
        "[the_person.possessive_title] takes off her [the_person.outfit.get_upper_top_layer.display_name]."
        $ the_person.draw_animated_removal(the_person.outfit.get_upper_top_layer)
    else:
        "[the_person.possessive_title] strikes a pose, her tits on display."
        the_person "Don't forget to take pictures!"
    "With her phone in hand, you snap a few pictures as she slowly walks over to you."
    "She runs her hands across your chest. She slowly gets down on her knees in front of you."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(40)
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] tugs at your belt, then slowly lowers your pants."
    "One more tug on your underwear, and your erection springs free."
    the_person "Wow! I haven't seen anything other than hubby for... years..."
    "She begins to stroke you softly with her hand."
    the_person "Mmmmm... it's so hard... and hot!"
    "You moan as she strokes you. You make sure to snap a couple pictures."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(40)
    the_person "Does that feel good? I bet it does... I just wanna make you feel good..."
    "She closes her eyes, then opens her mouth. She slowly rubs the tip back and forth along her slithery tongue."
    the_person "Mmm, you taste good too."
    "She starts to take you into her mouth. You snap a few more pictures of this beautiful señora, on her knees servicing you."
    "[the_person.possessive_title]'s head is now bouncing up and down on your cock. Her pouty lips feel amazing sliding up and down your length."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(40)
    "You forget you are supposed to take pictures and begin to just enjoy the wonderful sensations."
    # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH010
    call get_fucked(the_person, start_position = blowjob, start_object = make_sink(), private = True, skip_intro = True, ignore_taboo = True,  allow_continue = False) from _call_get_fucked_camilla_sex_description_CSH010
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Wow... I can't believe I came... while I was blowing you! That was fucking hot!"
    else:
        the_person "Wow... that was hot!"

    if the_person.has_mouth_cum:
        "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
        the_person "Hey! Don't forget to take pictures!"
        "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
    elif the_person.has_face_cum:
        "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
        the_person "Hey! Don't forget to take pictures!"
        "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
    $ the_person.draw_person (position = "stand2")
    "[the_person.title] stands up. You hand her back her phone."
    the_person "Wow... well... I guess there's no going back now? I guess I'll go ahead and send him some of these..."
    "She gets closer to you."
    the_person "Well, no matter what happens tonight, thanks for your help! If all goes well... maybe we can do this again."
    mc.name "Yeah I mean... if it makes your hubby happy for you to give me blowjobs... I GUESS I can help out..."
    "She laughs and punches you in the arm."
    the_person "Alright, I'm going to clean up. I'll see you."
    $ clear_scene()
    $ mc.change_location(downtown_bar)
    "You sneak your way out of the bathroom while [the_person.possessive_title] cleans herself up. You hope everything goes well with her tonight!"
    $ the_person.event_triggers_dict["camilla_blowjob_pic_day"] = day + 1
    $ the_person.apply_planned_outfit()
    $ the_person.add_unique_on_room_enter_event(camilla_blowjob_text)
    call advance_time from _call_advance_camilla_post_first_bj_01
    return

label camilla_blowjob_text_label(the_person):
    $ the_person.draw_person()
    "You walk up to [the_person.possessive_title]."

    mc.name "So... how did it go with the pictures?"
    "[the_person.possessive_title] gives you a quick smile."
    the_person "Well, I sent them off to him as he was getting off work, and I got an almost immediate response. 'Come home now'. No explanation or anything..."
    the_person "At first I got really scared. Did I just completely fuck up? So I went straight home..."
    the_person "When I got home, he was waiting for me... He umm... he handcuffed me with my hands behind my back... I didn't even know he had handcuffs!"
    "Her voice is starting to get excited as she recounts some of the details."
    the_person "He forced me down on my knees and then said... he said that I was a dirty little slut, and that after using my mouth on another man he would have to... reclaim it."
    the_person "So I opened up and I let him use my mouth... god I never could have imagined my husband doing that to me could be so hot!"
    the_person "Now... I'm a good wife... I've always, you know, swallowed for him. But this time..."
    "Her voice trails off a bit as she recalls the details. A smile on her face."
    the_person "I've never, ever had to swallow soooooo much. It was so hot, like a firehose it just kept cumming..."
    "You shift uncomfortably. This story is starting to turn you on!"
    $ mc.change_locked_clarity(20)
    the_person "Haaa... sorry! I probably should have just said that it went well."
    mc.name "No it's alright. I was a little concerned with how things would go for you, but I'm glad that it turned out well."
    $ the_person.draw_person(position = "stand4", emotion = "happy")
    the_person "It really did! So uhh, if you wanna go again, just ask. I'd be happy to be of service, BUT, we need to set some ground rules first!"
    mc.name "Okay, I'm down for that."
    the_person "Okay, well, like I said. I'm a good wife! I love my husband. He always comes first."
    "You nod in understanding."
    the_person "If you try to make me choose between you two, I'll choose him, every time. So let's just keep this casual, okay?"
    mc.name "Sounds good. Purely physical. I'm okay with that."
    the_person "Right... here, let's exchange numbers. I'll text you and if we're both free, we can screw around, no strings attached!"
    "You agree. You and [the_person.title] exchange numbers."
    $ mc.phone.register_number(the_person)
    the_person "Okay, well, I need to get going. I'm sure I'll see you around soon..."
    "You say goodbye and head out. Hot damn! You are now friends with benefits with a hot wife. You bet the sex is going to be amazing..."
    $ camilla.add_unique_on_room_enter_event(camilla_dancing_sex)
    call advance_time from _call_advance_camilla_sex_discussion
    return

label camilla_dancing_sex_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ the_person.arousal = 35
    $ the_person.story_event_log("lust")
    "You walk into the bar. You immediately notice [the_person.possessive_title] sitting down, sipping on a cocktail."
    "You walk over and sit down beside her."
    mc.name "Good evening, señorita!"
    the_person "Buenas noches sir!"
    "[the_person.title] is looking at you. There is something in her eyes that you've never seen before. Something firey."
    the_person "[the_person.mc_title]... I want to dance. Let's go dance."
    mc.name "Oh. Okay! Let's do it."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She gets up and starts walking out to the dance floor. You follow her."
    "You waste no time and grab [the_person.possessive_title]. You sync your movements to hers and begin to move your bodies to the beat."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "You bring her close, letting your body be close to hers. Heat begins to build as you get into the dance."
    $ scene_manager.update_actor(the_person, position = "kissing", display_transform = character_left_flipped)
    "When things start to get too heated, [the_person.possessive_title] moves away from you a bit."
    "You hold out your opposite hand, spinning her around gracefully back to you, finishing her spin with her back facing you."
    $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_right)
    "With [the_person.title] facing away from you, you put a hand on her hips and bring her close to you."
    "She slightly grinds her ass back against you as you keep moving to the beat. Her ass feels great moving back and forth against your rapidly rising erection."
    mc.name "Mmm, that feels good. I can't wait to get you alone..."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(20)
    "She gives a sigh and melts back into you. You let your hands roam all along the sides of her body, once in a while moving across the sides of her breasts."
    "Being careful not to push things too fast, you spin her out again, and then back to you."

    $ scene_manager.update_actor(the_person, position = "kissing")
    "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. Your hands start on her hips, but soon drift down to her ass."
    the_person "I love this song. Let's dance to this and then..."
    "You notice her glance over to the bar. You follow her eyes and notice the bartender, [the_person.SO_name] is watching you dance."
    "You look back at [the_person.title]. You squeeze her supple ass and grind up against her slightly."
    the_person "Mmm... fuck that feels good."
    "[the_person.title] begins moving her hips against yours. Your cock, constrained in your clothing, is nestled against her crotch, aching to be let free."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "The song ends, and [the_person.title] looks at you."
    the_person "Ok... you know what to do... I'll meet you in the Lady's room in just a minute..."
    $ clear_scene()
    $ mc.change_location(work_bathroom)
    "You head to the women's restroom and [the_person.title] soon meets you there."
    $ the_person.draw_person (position = "against_wall")
    "You grab her and pick her up. Her legs wrap around you."
    the_person "Oh god... I can't believe I'm doing this... but I need it so bad!"
    "You take her over to the bathroom sinks and set her on the edge of it. You start to strip her clothes off."
    if the_person.vagina_visible:
        "You stop for a second and admire [the_person.title]'s [the_person.pubes_description] little slit glistening in the florescent lights."
    else:
        "You quickly remove [the_person.title]'s clothes blocking the way to your prize."

        $ the_person.strip_to_vagina(position = "against_wall", prefer_half_off = True, visible_enough = True)
        $ the_person.change_arousal(20)

        "Once finished, You stop for a second and admire [the_person.title]'s [the_person.pubes_description] little slit glistening in the florescent lights."
    the_person "Oh! Shit I almost forgot!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] grabs her purse. She rummages through it for a moment then pulls out her phone."
    the_person "Can't forget this!"
    $ the_person.draw_person(position = "stand3")
    "She hands you her phone and you quickly pull up her camera app. While you are doing that [the_person.possessive_title] turns around and leans over the bathroom sink."
    $ the_person.draw_person (position = "standing_doggy")
    "You snap a couple pictures of her amazing ass while she is bent over."
    the_person "Okay, you better get your pants off, we don't have much time!"
    "You quickly drop your pants, letting your aching hard on spring free. You step behind [the_person.title], letting your cock nestle between her pliant ass cheeks."
    "You snap a few more pictures as you dry hump her ass crack a bit. Then you pull back a bit and get yourself pointed at her juicy slit."
    mc.name "Should I umm... wrap it up?"
    the_person "Don't bother, unless you REALLY want to. I'm actually infertile..."
    mc.name "Ah... I see..."
    "You make a mental note of her infertility."
    "You change the camera app to take a video. You figure since this is her first time getting fucked by a man other than her husband it might come in handy..."
    "With one hand firmly on [the_person.possessive_title]'s hip, you steadily push yourself into her. She moans loudly and you capture the whole thing on glorious video."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    the_person "Oh fuck that feels good. Fuck me good [the_person.mc_title]!"
    "You stop the video, you figure this is as good of a place as any to stop it. You take a few nice and slow strokes, snapping pictures of your cock penetrating her at various depths."
    "You look up and get one last picture of [the_person.title] in the mirror. Her mouth is open and she has one hand groping one of her own tits while her other hand is reaching back and grabbing your hip."
    "You set the phone down and begin to fuck her."
    $ mc.condom = False
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_sink(), private = True, skip_intro = True, skip_condom = True, ignore_taboo = True) from _call_camilla_sex_description_CSH020
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        #TODO description for all possible cum locations
        if the_person.has_mouth_cum:
            "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            "You grab her phone and snap a couple pictures of her face with your traces of cum on it."
        elif the_person.has_face_cum:
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            "You grab her phone and snap a couple pictures of her face with your cum covering it."
        elif the_person.has_tits_cum:
            "[the_person.possessive_title] looks up at you. Her tits are plastered with your sticky seed."
            "You grab her phone and snap a couple pictures of her tits with your cum covering it."
        elif the_person.has_ass_cum:
            "[the_person.possessive_title] looks back at you. Her ass is plastered with your sticky seed."
            "You grab her phone and snap a couple pictures of her ass with your cum covering it."
        elif the_person.has_creampie_cum:       #We assume we finished inside her#
            "[the_person.possessive_title]'s pussy is dripping cum from your creampie."
            "You grab her phone and snap a couple pictures of her well used pussy with your cum dripping out of it."
        else:   #We have no idea where the cum is. It got wasted?
            "You grab her phone and snap a couple pictures of her well used pussy."
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Oh my god... that was amazing. That felt so good."
    $ the_person.draw_person("stand3")
    the_person "Wow, I never knew cheating could feel so good. God, I can't wait until my husband reclaims me later... oh fuck."
    "[the_person.possessive_title] starts to touch herself a bit, getting herself excited thinking about what is in store for her later tonight. She quickly realizes she needs to stop though."
    $ the_person.event_triggers_dict["will_fuck"] = True
    "She takes her phone from you and starts going through the pictures you took."
    the_person "You'd better get going, [the_person.mc_title]. I'm going to send these to my husband..."

    $ the_person.event_triggers_dict["booty_call"] = True # unlock casual encounters. Am I still using this? I should probably get rid of this...

    $ clear_scene()
    $ the_person.apply_planned_outfit()
    $ mc.change_location(downtown_bar)
    "After straightening up, you step out of the restroom and into the bar."
    "You just fucked [the_person.possessive_title], a married woman, in the bar bathroom! And you know this is probably not just going to be a one time thing."
    $ camilla.event_triggers_dict["bathroom_sex"] = True
    $ camilla.add_unique_on_room_enter_event(camilla_sex_invite)


    # else:   #We've done this before
    #     mc.name "Hey, [the_person.title]. You up for some dancing?"
    #     "[the_person.possessive_title] smiles."
    #     the_person "You know it! Let's go!"
    #     "You follow [the_person.title] out on to the dance floor. The bar is playing some pretty upbeat, fun music."
    #     "You waste no time and grab [the_person.possessive_title]. You sync your movements to the beat and begin to move your bodies to the beat."
    #     $ the_person.draw_person (position = "back_peek")
    #     "At some point, [the_person.title] turns away from you. You put your hand on her hips and bring her close to you."
    #     "You can feel her grinding her ass back against you as you keep moving to the beat. Her ass feels great moving back and forth against your rapidly rising erection."
    #     mc.name "Mmm, that feels good. I can't wait to fuck you again."
    #     $ the_person.change_arousal(20)
    #     $ mc.arousal.change_arousal(10)
    #     "She gives a sigh and melts back into you. You let your hands roam all along the sides of her body, once in a while moving across the sides of her breasts."
    #     "The song ends and a slower song begins to play."
    #     $ the_person.draw_person (position = "kissing")
    #     "[the_person.possessive_title] turns back to you and puts her arms around your shoulders. Your hands start on her hips, but soon drift down to her ass."
    #     the_person "I love this song. Let's dance to this! Then we can head to the back and you can have your way with me..."
    #     "You squeeze her supple ass and grind up against her slightly."
    #     the_person "Mmm... fuck that feels good. You better make sure I cum all over that amazing cock of yours."
    #     "[the_person.title] begins moving her hips against yours. Your cock, constrained in your clothing, is nestled against her crotch, aching to be let free."
    #     $ the_person.change_arousal(20)
    #     $ mc.arousal += 10
    #     "The song ends, and [the_person.title] looks at you."
    #     the_person "Ok! I didn't think that song was ever going to end. I'll meet you in the Lady's room in just a minute."
    #     $ clear_scene()
    #     $ mc.change_location(work_bathroom)
    #     "You head to the women's restroom and [the_person.title] soon meets you there."
    #     $ the_person.draw_person (position = "stand4")
    #     the_person "Okay, I want you to sit on the bathroom sink. I'm gonna get naked for you."
    #     "She hands you her phone."
    #     the_person "Here we go! Get lots of good pics!"
    #     call strip_tease(the_person, for_pay = False, skip_intro = True) from _CS_free_strip_scene_camilla_021
    #     "You got lots of pics of her strip tease. You take a few more as she saunters over to you."
    #     the_person "Come on, let's fuck!"
    #     call fuck_person(the_person, start_object = make_sink(), private = True) from _call_casual_sex_mod_camilla_022
    #     "As you finish up, you make sure to take some pictures of the aftermath. You notice [the_person.possessive_title] is touching herself."
    #     the_person "Oh god, daddy is gonna fuck me so rough when he reclaims me tonight... I'm gonna be so sore. I can't wait!"
    #     "You almost think she is going to make herself cum again until she stops."
    #     $ the_person.draw_person("stand3")
    #     the_person "Thanks again [the_person.mc_title]. You know where to look for me next time you need some... action."
    #     "She takes her phone from you and starts going through the pictures you took."
    #     the_person "You'd better get going. I'm going to send these to my husband..."
    #     $ the_person.apply_planned_outfit()
    #     $ clear_scene()
    call advance_time from _call_advance_camilla_dancing
    return

label camilla_sex_invite_label(the_person):
    $ the_person.draw_person(position = "sitting")
    $ the_person.story_event_log("lust")
    "You walk into the bar. You immediately notice [the_person.possessive_title] sitting down, sipping on a cocktail."
    "You walk over and sit down beside her."
    mc.name "Good evening, señorita!"
    the_person "Buenas noches sir!"
    "You sit down and chat idly with her for a few minutes. Eventually the subject of her husband comes up."
    mc.name "So how is it going on the homefront? Hubby enjoying all the smut we've been sending him?"
    the_person "Yes, he has been. But you know men... they always want more."
    the_person "He's started asking, when am I gonna bring you back to our place..."
    mc.name "Oh? He wants pictures of us in his own house huh?"
    the_person "Well, not exactly."
    mc.name "What do you mean?"
    the_person "Well, he wants to be there. He wants to watch."
    "Wow, her husband is really getting into the cuckolding thing!"
    mc.name "And how do you feel about it? Do you feel like you're ready for that?"
    the_person "Honestly? I'm getting a little turned on just thinking about it."
    mc.name "I'll admit, I'm' a little hesitant to do something like that in front of your husband... but if you're sure about it."
    the_person "Yeah... I'm certain! Let me know when would be a good time to come over, and I'll get the details sorted."
    "Wow, she wants you to come to her house and fuck her in front of her husband! You should probably get on that before the opportunity passes!"
    mc.name "What about tonight?"
    the_person "I... you want to come over tonight?"
    mc.name "Sure. I'm not doing anything."
    "[the_person.possessive_title] gives you her address."
    the_person "Come over tonight, around 10pm. You won't regret it! I'm going to go now and get... set up..."
    $ mc.business.add_mandatory_crisis(camilla_her_place)
    $ the_person.learn_home()
    #call advance_time from _call_advance_camilla_sex_invite
    return

label camilla_her_place_label():
    $ the_person = camilla
    "You head over to [the_person.title]'s place. You can't believe you're gonna fuck her in front of her husband!"
    "You ring the doorbell. Soon [the_person.title] answers the door."

    $ the_person.change_to_hallway()
    $ the_person.apply_outfit(get_camilla_lingerie_set_white(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    the_person "Señor! I wasn't sure you would actually come!"
    mc.name "Of course!"
    $ mc.change_location(the_person.home)
    "You check her out. She definitely looks ready for some action! She takes your hand and slowly walks you back to the bedroom."
    the_person "[the_person.SO_name] and I were just getting started... you came at the perfect time..."
    "[the_person.SO_name]? Why does that sound so familiar?"
    $ the_person.change_to_bedroom()
    "As you walk into the bedroom, you see [the_person.SO_name], the bartender sitting in a chair, completely naked."
    "Holy shit! It's the bartender! He had a front row ticket every time you fucked [the_person.title] at the bar! No wonder he went along with all of it!"
    "He nods to you, but you are shocked at the revelation."
    the_person "Don't worry about him, get over here and fuck me [the_person.mc_title]!"
    $ the_person.draw_person(position = "doggy")
    "You watch as [the_person.possessive_title] crawls on to the bed, pointing her ass back at you. She wiggles it back and forth, enticingly."
    "You walk up behind her and run your hands over her pliant cheeks. [the_person.SO_name]'s chair is at the end of the bed, so he will have an excellent profile view while you fuck his wife."
    "With one hand you start to undo your trousers. With your other hand, you run you fingers along her slit. She is wet and ready for you."
    "Your cock now free, you line yourself up with [the_person.possessive_title]'s pussy. You put her husband out of your mind as you slowly push into her."
    "[the_person.possessive_title] gasps as you begin to slide in and out of her."
    call fuck_person(the_person, start_position = doggy, start_object = make_bed(), private = True, skip_intro = True, skip_condom = True) from _call_camilla_sex_description_CSH040
    $ the_report = _return

    #Finishing dialogue based on sexual performance
    if the_report.get("girl orgasms", 0) > 1:   #She had more than one orgasm
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You've finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0: #She had one orgasm
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dressed and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dressed and quietly excuse yourself from the bedroom."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You make your way back home. You can hardly believe your luck, fucking [the_person.title] in her house, in front of her husband, who is also the bartender!"
    $ perk_system.add_stat_perk(Stat_Perk(description = "Fucking Camilla in front of her husband has made you feel more charismatic.", cha_bonus = 1, bonus_is_temp = False), "Camilla Charisma Bonus")
    $ mc.change_location(bedroom)
    $ camilla.event_triggers_dict.get("home_sex", True)
    # $ camilla.add_unique_on_room_enter_event(camilla_sex_invite)
    #$ the_person.event_triggers_dict["camilla_progress"] = 5
    return

# Repeatable scenes
label camilla_go_dancing_label(the_person):
    pass
    return

label camilla_take_pics_label(the_person):  #Not the first time.
    mc.name "Hey, you wanna sneak off for a bit and take some pictures?"
    "[the_person.possessive_title] flashes you her beautiful smile."
    the_person "Si! You know what to do!"
    $ mc.change_location(work_bathroom)
    "You head to the lady's room. [the_person.title] soon follows behind you. She locks the door as she closes it."
    $ the_person.draw_person (position = "kissing")
    "You waste no time. She throws her arms around you and you begin to make out."
    if camilla.event_triggers_dict.get("home_sex", False): #If we've had sex before, open up to that.
        "Knowing you don't have much time, you start getting her naked right away."
        "Piece by piece, you take [the_person.title]'s clothes off."

        $ the_person.strip_outfit(position = "kissing")
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        the_person "Here, take this. You know what to do!"
        "[the_person.possessive_title] hands you her phone. You pull up her photo app."
        $ the_person.draw_person(position = "missionary")
        "She hops up on the bathroom sink and spreads her legs, showing you everything."
        "Moisture glistens between her legs, her pussy looks great and ready for you to fuck. You snap several pictures."
        the_person "Here, let me see it now..."
        "She takes her phone back. You see her attach a couple to a text message and send it."
        the_person "Alright, I'm going to set this up to take a picture every few seconds... now get over here and fuck me!"
        call fuck_person(the_person, start_object = make_sink(), private = True) from _call_camilla_sex_photo_shoot_01
        $ the_report = _return
        if the_report.get("guy orgasms", 0) > 0:
            #description for all possible cum locations
            if the_person.has_mouth_cum:
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth. You snap a couple pictures."
            elif the_person.has_face_cum:
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "Her face is plastered with your sticky seed. You snap a couple pictures of her sperm covered smile."
            elif the_person.has_tits_cum:
                $ the_person.draw_person()
                "[the_person.possessive_title] stands up as you grab her phone."
                "Her tits are plastered with your sticky seed. You snap a couple pictures of her snow capped mountains."
            elif the_person.has_ass_cum:
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] bends over the bathroom sink. Her ass is plastered with your sticky seed."
                "You grab her phone and snap a couple pictures of her ass with your cum covering it."
            elif the_person.has_creampie_cum:       #We assume we finished inside her#
                $ the_person.draw_person(position = "missionary")
                "[the_person.possessive_title] sits on the edge of the bathroom sink, mirroring her pose before you started fucking."
                "This time though, her cunt is a little gaped and your seed is clearly leaking out and down her legs."
                "You grab her phone and snap a couple pictures of her well used pussy with your cum dripping out of it."
            else:   #We have no idea where the cum is. It got wasted?
                "You grab her phone and snap a couple pictures of her well used pussy."
        if the_report.get("girl orgasms", 0) > 0:
            the_person "Oh my god... that was amazing. You always make me feel so good."

    else:
        if the_person.effective_sluttiness() > 30 and not the_person.tits_available:
            "[the_person.possessive_title] steps back suddenly."
            the_person "Let me just get this off... Papi loves it when I have my tits out for this..."
            "She hands you her phone with the camera app out. You snap some pictures as she starts to strip."
            if the_person.outfit.can_half_off_to_tits():
                $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True)
            else:
                $ generalised_strip_description(the_person, the_person.outfit.get_tit_strip_list())

            "With her tits completely exposed, she saunters back over to you then starts to get down on her knees."
        else:
            "[the_person.possessive_title] slowly starts to get down on her knees in front of you."
        $ the_person.draw_person(position = "blowjob")
        "You can tell that [the_person.title] is hungry. She wastes no time pulling your pants down, followed quickly by your underwear."
        "Your hardened cock springs out. Her agile hands grasp it and begin to stroke."
        if the_person.is_willing(deepthroat):
            the_person "Mmm, I've been working on a new skill lately... since we started doing this. Mind if I practice on you?"
            mc.name "Sure I guess, but what is..."
            "She doesn't wait for you to finish your response. In one, smooth motion, she opens her mouth and swallows your cock whole."
            $ the_person.break_taboo("sucking_cock")
            "Past her lips, to the back of her tongue, and down her throat the tip of your dick goes."
            mc.name "Oh fuck!"
            "You make sure to snap more pictures of her. She's getting good at this!"
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH011
            call get_fucked(the_person, start_position = deepthroat, start_object = make_sink(), private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_camilla_sex_description_CSH011
        else:
            the_person "Mmmm, I can't wait any longer... I have to taste it!"
            $ the_person.break_taboo("sucking_cock")
            "She opens up her mouth and wraps her lips around your meat."
            "You snap some pictures as she pulls off and begins to run her tongue up and down along the sides of your cock."
            mc.name "Mmm, that feels great [the_person.title]."
            "You decide to just enjoy her skilled mouth going down on you."
            # call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_camilla_sex_description_CSH012
            call get_fucked(the_person, start_position = blowjob, start_object = make_sink(), private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_camilla_sex_description_CSH012

        if the_person.has_mouth_cum:
            "[the_person.possessive_title] looks up at you. She couldn't quite swallow all your cum, some of it is slowly dripping down the sides of her mouth."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your traces of cum on it."
        elif the_person.has_face_cum:
            "[the_person.possessive_title] looks up at you. Her face is plastered with your sticky seed."
            the_person "Hey! Don't forget to take pictures!"
            "You suddenly remember the phone. You snap a couple pictures of her face with your cum covering it."
    $ the_person.draw_person (position = "stand2")
    the_person "Mmm, that was great [the_person.mc_title]! I can't wait until I get home tonight... I hope daddy gets the handcuffs out again..."
    $ clear_scene()
    $ mc.change_location(downtown_bar)
    "You say goodbye and excuse yourself while she gets herself cleaned up. This arrangement is working out to be very beneficial!"
    $ the_person.apply_planned_outfit()
    call advance_time from _call_advance_camilla_bathroom_blowjob
    return


label camilla_home_sex_label(the_person):
    $ mc.change_location(the_person.home)
    mc.name "So, want to have some fun tonight?"
    the_person "Sounds great! Just give me a minute to get ready..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] walks into her bedroom and closes the door. You hang out in her living room for a few minutes while she gets ready."
    $ the_person.apply_outfit(get_camilla_lingerie_set_pink(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "She opens up the bedroom door and motions for you to follow her. As you step into her bedroom you see [the_person.SO_name] sitting at the edge of the bed again."
    $ the_person.change_to_bedroom()
    "You nod at him, and he gives a brief nod back. You turn your attention back to [the_person.title]."
    the_person "Mmm, I can't wait. Let's go!"
    call fuck_person(the_person, private = True) from _call_casual_sex_mod_camilla_505
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 1:
        the_person "Oh my god... I came so many times..."
        "[the_person.possessive_title] collapses onto the bed after your performance. You get up and start to get dressed."
        "You nod at [the_person.SO_name], and he nods back. He goes over to a bedside table and gets out a set of handcuffs."
        "After you fucked her brains out, [the_person.title] lays helpless on the bed as he starts to cuff her hands behind her back."
        "You've finished getting dressed and decide to leave them to it, so you quietly excuse yourself from the bedroom."
    elif the_report.get("girl orgasms", 0) > 0:
        the_person "Oh god, I came so hard... That was good [the_person.mc_title]."
        $ the_person.draw_person (position = "missionary")
        "[the_person.possessive_title] rolls over on her back and spreads her legs wide."
        the_person "[the_person.SO_name]... I've been a bad girl..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        "[the_person.SO_name] begins cuffing [the_person.title]'s hands to the bedpost. You finish getting dressed and quietly excuse yourself from the bedroom."
    else:                           #You left her hanging
        "Surprised you are finished so soon, [the_person.title] gets up and sits at the edge of the bed."
        $ the_person.draw_person( position = "sitting")
        the_person "Thanks for getting me warmed up..."
        "[the_person.SO_name] gets up from his chair and gets some handcuffs from a bedside table. You get yourself dressed."
        the_person "Oh... [the_person.SO_name], I've been a bad girl... what are you gonna do with those handcuffs?"
        "[the_person.SO_name] begins cuffing [the_person.title]'s behind her back. You finish getting dressed and quietly excuse yourself from the bedroom."
    $ clear_scene()
    $ mc.change_location(bedroom)
    "You make your way back home after a sexy evening with [the_person.possessive_title]."

    call advance_time from _call_advance_camilla_home_sex
    return
