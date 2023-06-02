init 2 python:
    #Pose list. [0] is lily's pose, [1] is ericas, [2] is playful text, [3] is sexy text.
    # erica_insta_pose_pairs = [
    #     ["back_peek", "standing_doggy", "The girls wiggle their asses a bit as you snap their pictures.", lily.title + " is twerking her hips while " + erica.possessive_title + " gives herself a couple playful spanks."],
    #     ["missionary","missionary", "The girl cross their inside legs across each other, getting close for the camera.", "The girls both put one hand between their legs, another on their chests, pretending they are masturbating."],
    #     ["doggy","stand4", erica.title + " puts a hand on "+ lily.possessive_title + "'s lower back.", erica.title + " gives a playful spank on " + lily.possessive_title + "'s ass."],
    #     ["kneeling1","kneeling1", "The girls run their hands along their sides sensually for the camera.", "The girls put a hand between their legs, pretending to masturbate for the camera."],
    #     ["blowjob","back_peek", lily.title + " licks her lips while " + erica.possessive_title + " leans forward a bit, angling her ass toward the camera.",lily.title + " gets on her knees next to " + erica.possessive_title + ", licking her lips and pretending to kiss her ass."]
    # ]

    def erica_make_insta_pose_pairs():
        insta_pose_list = [
            ["back_peek", "standing_doggy", "The girls wiggle their asses a bit as you snap their pictures.", lily.title + " is twerking her hips while " + erica.possessive_title + " gives herself a couple playful spanks."],
            ["missionary","missionary", "The girl cross their inside legs across each other, getting close for the camera.", "The girls both put one hand between their legs, another on their chests, pretending they are masturbating."],
            ["doggy","stand4", erica.title + " puts a hand on "+ lily.possessive_title + "'s lower back.", erica.title + " gives a playful spank on " + lily.possessive_title + "'s ass."],
            ["kneeling1","kneeling1", "The girls run their hands along their sides sensually for the camera.", "The girls put a hand between their legs, pretending to masturbate for the camera."],
            ["blowjob","back_peek", lily.title + " licks her lips while " + erica.possessive_title + " leans forward a bit, angling her ass toward the camera.",lily.title + " gets on her knees next to " + erica.possessive_title + ", licking her lips and pretending to kiss her ass."]
        ]
        return insta_pose_list

init -2 python:
    def erica_lily_instapic_setup_requirement(person):
        return person.location == lily_bedroom

    def erica_lily_instapic_proposal_requirement(person):
        return person.location == gym

    def erica_lily_instapic_intro_requirement():
        return time_of_day == 4 and day%7 == 5

    def erica_lily_post_photoshoot_requirement(person):
        return time_of_day > 0 and day%7 < 5

    def erica_post_photoshoot_requirement(person):
        return person.location == gym

    def erica_lily_weekly_photoshoot_requirement(person):
        return person.location == lily.location and time_of_day == 4 and day%7 == 5

    def erica_lily_post_insta_handjob_requirement():
        if erica.is_willing(cowgirl_handjob) and day%7 == 6:
            return True
        return False

    def erica_post_insta_handjob_followup_requirement(the_person):
        return the_person.location == gym

    def erica_lily_post_insta_morning_requirement():
        if day%7 == 6 and erica_has_given_morning_handjob():
            if erica_get_morning_wakeup_pref() != 0:
                if erica.sex_record.get("Last Sex Day", 9999) != day: #If mandatory and random crisis happen to fire on the same day, suppress the second event.
                    return True
        return False

init -1 python:
    erica_lily_instapic_setup = Action("Talk to Lily about Erica", erica_lily_instapic_setup_requirement, "erica_lily_instapic_setup_label")
    erica_lily_instapic_proposal = Action("Propose InstaPic session to Erica", erica_lily_instapic_proposal_requirement, "erica_lily_instapic_proposal_label")
    erica_lily_instapic_intro = Action("InstaPic session with Lily and Erica", erica_lily_instapic_intro_requirement, "erica_lily_instapic_intro_label")
    erica_lily_post_photoshoot = Action("Ask Lily about InstaPic results", erica_lily_post_photoshoot_requirement, "erica_lily_post_photoshoot_label")
    erica_post_photoshoot = Action("Convince Erica to continue Insta", erica_post_photoshoot_requirement, "erica_post_photoshoot_label")
    erica_lily_weekly_photoshoot = Action("Weekly instapic session with Lily", erica_lily_weekly_photoshoot_requirement, "erica_lily_weekly_photoshoot_label")
    erica_lily_post_insta_handjob = Action("Erica wakes you up", erica_lily_post_insta_handjob_requirement, "erica_lily_post_insta_handjob_label")
    erica_post_insta_handjob_followup = Action("Talk about Handjob", erica_post_insta_handjob_followup_requirement, "erica_post_insta_handjob_followup_label")
    erica_lily_post_insta_morning_mand = Action("Erica wakes you up", erica_lily_post_insta_morning_requirement, "erica_lily_post_insta_morning_label")
    erica_pre_insta_love = Action("Erica blows you", erica_pre_insta_love_requirement, "erica_pre_insta_love_label")

init 2 python:
    erica_lily_post_insta_morning_action = ActionMod("Erica wakes you up", erica_lily_post_insta_morning_requirement, "erica_lily_post_insta_morning_label",
        menu_tooltip = "Erica wakes you up after spending the night with Lily.", category = "Home", is_crisis = True, is_morning_crisis = True)


label erica_lily_instapic_setup_label(the_person):#This should be an event assigned to Lily
    mc.name "Hey sis. I have an idea for your InstaPic channel."
    the_person "Oh? Having a male perspective on the channel is always good!"
    mc.name "I have a friend I recently made at the gym. You might actually know her, she goes to your university too."
    mc.name "She's on the track and field team, but is having some cash flow problems. I was wondering if you would be willing to guest host her on your channel."
    if mom.event_triggers_dict.get("mom_instathot_pic_count",0) > 0:
        mc.name "Something similar to what we've done with mom. You know how things took off with her, right?"
    the_person "What's her name?"
    mc.name "Her name is [erica.fname]."
    "[the_person.title] thinks about it for a minute."
    the_person "I think I know her... We might have had a general class together a year ago?"
    "She's considering it, but you can tell she isn't a big fan of the idea. You might have to sweeten the deal a little bit to get her to agree to it."
    the_person "I think I'm okay with it. But what if it doesn't pull in any extra money? I don't want to have to split the profit if it turns out to be a dud."
    mc.name "Tell you what... For the first session, I'll donate the $100 you normally pay me to run the camera. I'll tell [erica.fname] for the first session it's a straight $100 fee, and if it is successful there may be more opportunities in the future?"
    the_person "Aww, you're gonna let her have your share? You must like this girl!"
    "[the_person.title] starts to tease you, but you also detect a hint of jealousy in her voice."
    the_person "You have a crush on this girl, don't you? Does mom know you're *in love*?"
    mc.name "Hey, she's a good person, just trying to make ends meet. Do we have a deal?"
    the_person "Yeah, we have a deal. You think this will really help my channel?"
    mc.name "Speaking as a guy... Yes... Having two hot college girls dressing up for pics will be perfect!"
    the_person "Good point! Okay, Did you need anything else?"
    $ erica.add_unique_on_room_enter_event(erica_lily_instapic_proposal)

    return

label erica_lily_instapic_proposal_label(the_person): #This should be assigned to Erica
    $ the_person.draw_person()
    "You spot [the_person.possessive_title]. She appears to be in between workout equipment."
    mc.name "I have an idea for something you could do to bring in a little extra money."
    the_person "Oh? What is it?"
    mc.name "My sister, who you may actually know from your classes, runs an InstaPic channel where she makes some extra money modeling clothes."
    the_person "You're not suggesting I make my own InstaPic channel, are you? You know how much work those are?"
    mc.name "No, actually I talked it over with her and thought maybe you could appear as a guest on her channel once in a while."
    the_person "Oh! You mean like, we get together and take pictures of both of us?"
    mc.name "Exactly. She makes pretty good money doing it. I'll be the one taking pictures, and we agreed for your first session she'd pay you a $100 fee, with more opportunities in the future if it goes well."
    the_person "You're taking the pictures? Do you... Always do that for your sister?"
    mc.name "Yeah it's usually me."
    if the_person.get_opinion_score("incest") < 0:
        the_person "I don't know... that's kinda creepy..."
        $ the_person.change_love(-3)
    elif the_person.get_opinion_score("incest") > 0:
        the_person "That's awful nice of you! You sound like a good big brother!"
        $ the_person.change_love(3)
    the_person "What was your sister's name?"
    mc.name "It's [lily.fname]. She said she thinks you might have had a class together once."
    "She wrinkles her nose as she tries to remember. It's kind of a cute look for her."
    the_person "I think I remember her... She seemed pretty nice. Kinda chatty?"
    mc.name "That's her."
    the_person "Okay... But you can't use my name or anything! I'm not sure I'm supposed to do stuff like that while I'm on a college sports team."
    mc.name "Yeah, [lily.fname] doesn't use any personally identifying info in the channel."
    the_person "Oh god... Okay! I'll try it! My schedule is pretty busy right now... Maybe this weekend? Saturday night?"
    mc.name "Okay. I'll text you my address. I'll give [lily.fname] your contact info also. She might need your clothes sizes."
    the_person "Alright. I'll see you on Saturday!"
    "You let [the_person.possessive_title] get back to her workout. You text [lily.title] about [the_person.title]'s info. You can't wait to snap some sexy pics of the duo!"
    $ mc.business.add_mandatory_crisis(erica_lily_instapic_intro)
    return

label erica_lily_instapic_intro_label():
    if not lily.is_available or not erica.is_available:
        return
    $ erica.event_triggers_dict["insta_pic_intro_complete"] = True
    $ scene_manager = Scene() #Clean Scene

    "It's Saturday evening, which means it's time for a sexy photo shoot with [lily.title] and [erica.title]! You head home and knock on [lily.possessive_title]'s door. She swings it open."
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(lily)
    lily "Hey, any word from your friend?"
    mc.name "Not yet."
    lily "Are you sure she's gonna make it? I teased on my channel that I have a surprise for them tonight. It's gonna be hard to come up with something if she doesn't show up!"
    mc.name "She'll be here."
    "You chat with [lily.possessive_title] for a bit. Soon you feel a vibration in your pocket as your phone goes off."
    erica "I'm here! Come let me in!"
    $ scene_manager.clear_scene()
    $ hall.show_background()
    "You go to your front door and open it. [erica.title] gives you a nervous smile as she steps inside."
    $ scene_manager.add_actor(erica)
    erica "Sorry I'm late. I almost didn't come... This whole thing is just a little... crazier than anything I would normally do."
    mc.name "Don't worry, [lily.title] is great at this. I was pretty skeptical about it at first too, but she's been pretty successful with this."
    "You lead her to [lily.possessive_title]'s room. As she steps in, you see the two girls make eye contact. Recognition dawns on both of their faces."
    $ lily_bedroom.show_background()
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    lily "Oh my gosh... [erica.fname]? I totally remember you! You were in my psych class! You sat next to that girl that kept flirting with the professor!"
    erica "Ah! Yes I remember you now! You were at the study group for the midterm!"
    lily "I never realized you were on the track team! But God, I can tell now! You look amazing! No wonder my brother is crushing on you."
    erica "Aww, thank you!... Wait, your brother what?"
    mc.name "[lily.title], let's not..."
    lily "He's totally into you. Did he tell how much the fee was for today?"
    erica "He just said $100..."
    mc.name "[lily.title], could you not do this right now..."
    lily "Yeah! That's totally his normal cameraman fee. He offered to donate it to you to help you out!"
    "[erica.possessive_title] looks at you, surprise on her face."
    erica "[erica.mc_title]... Is that true?"
    mc.name "Well... yeah... I mean, about where the fee is coming from. I just want everyone here to be successful. This is gonna be great for both of you, and there's no strings attached to the money."
    $ erica.change_love(3)
    "[erica.title] smirks at you."
    erica "I see. Well, I'm here now! We should get started."
    lily "Right! Let me show you what I got for us for tonight!"
    "The girls start to chat as [lily.title] pulls out a few outfits. You are glad that they seem to be hitting it off so well... But also a little fearful. [lily.possessive_title] seems to be enjoying this a little TOO much."
    "After a bit, [lily.title] moves to get things started."
    lily "Alright, let's go with these!"
    # todo start stripping
    $ scene_manager.strip_full_outfit(person = lily, strip_feet = True)
    "[lily.title] starts to take her clothes off, surprising [erica.title]."
    erica "Whoa, like, right here? In front of him?"
    "[erica.possessive_title] seems a little unsure."
    lily "It's okay, he doesn't mind!"
    "She starts to protest again, but [lily.title] continues to strip down. Soon she decides to just follow her and starts to strip also."
    $ scene_manager.strip_full_outfit(person = erica, strip_feet = True)
    if erica.has_taboo(["bare_pussy", "bare_tits"]):
        "[erica.title] uses her hands to try and cover herself up after she finishes stripping down. She looks at you and blushes."
        $ erica.break_taboo("bare_pussy")
        $ erica.break_taboo("bare_tits")

    "When they finish, [lily.title] hands her the outfit. They both quickly get dressed. The outfits look great."
    $ lily.apply_outfit(insta_wardrobe.pick_random_outfit(), update_taboo = True)
    $ erica.apply_outfit(erica.personalize_outfit(insta_wardrobe.pick_random_outfit(), coloured_underwear = True, allow_skimpy = False), update_taboo = True)
    $ scene_manager.update_actor(lily)
    $ scene_manager.update_actor(erica)
    $ mc.change_locked_clarity(25)
    erica "It's... A little skimpy, don't you think?"
    lily "That's the point! A little showy, but leave the guys thirsty and they'll come back again and again!"
    "[erica.possessive_title] looks at you. At first, you see uncertainty in her eyes, but then your eyes meet. You can almost see her confidence return when she observes your reaction."
    erica "What do you think, [erica.mc_title]? Will this bring in lots of views?"
    $ scene_manager.update_actor(erica, position = "back_peek")
    "[erica.title] turns and gives you a good look at her back side. There's a large lump in your throat as you try to reply."
    mc.name "I mean... I can only speak for myself, and I would check it out..."
    $ erica.change_stats(happiness = 3, love = 2, slut = 1, max_slut = 30)
    lily "Oh god, look at him! His brain cells can barely respond! You gonna be able to take these pictures [lily.mc_title]?"
    $ scene_manager.update_actor(erica, position = "stand3")
    mc.name "Yeah, of course, I got this."
    erica "Ok... how do we start?"
    lily "It's easy! Just follow my lead."
    "[lily.possessive_title] hops up on her bed and gets down on her knees in a seductive pose."
    $ scene_manager.update_actor(lily, position = "kneeling1", emotion = "happy")
    "She pats the bed next to her, and soon [erica.title] is awkwardly climbing up next to her."
    $ scene_manager.update_actor(erica, position = "kneeling1", emotion = "happy")
    $ mc.change_locked_clarity(25)
    lily "That's it. Just relax! You're so tense."
    erica "Sorry... I've just never done anything like this before."
    lily "I know, just look over at the dumb goofy face my brother is giving us right now."
    "[erica.possessive_title] looks over at you, and her smile goes from obviously forced to much more genuine."
    lily "Heyyyyy, that's it! Just pretend like we're not even taking pictures... you're just posing for [lily.mc_title]!"
    "[lily.title] turns to you and you start taking pictures. It isn't long until [erica.title] gets the hang of it."
    $ scene_manager.update_actor(lily, position = "back_peek", emotion = "happy")
    $ scene_manager.update_actor(erica, position = "stand4", emotion = "happy")
    $ mc.change_locked_clarity(25)
    "You fit in a couple different poses, but all throughout [erica.possessive_title] watches your reactions closely."
    $ scene_manager.update_actor(lily, position = "missionary", emotion = "happy")
    $ scene_manager.update_actor(erica, position = "missionary", emotion = "happy")
    "For the final set of pics you capture them laying in bed next to each other. It is undeniably sexy."
    mc.name "Alright, I think we've got all the shots we need."
    $ scene_manager.update_actor(erica, position = "stand2", emotion = "happy")
    "[erica.title] stands up."
    erica "That was actually really fun... Do you think the pictures will make any money?"
    mc.name "Definitely."
    $ scene_manager.update_actor(lily, position = "stand3", emotion = "happy")
    "[lily.title] gives [erica.title] money as payment for the session."
    lily "Now, the question is, are you up for doing this again?"
    erica "I'm not sure... I had fun tonight, but I need to think about it."
    "[erica.possessive_title] quickly changes back into her regular clothes. You do your best not to make it obvious you are watching..."
    $ scene_manager.strip_full_outfit(person = erica, strip_feet = True)
    "She looks over and gives you a little smirk."
    $ mc.change_locked_clarity(15)
    $ erica.apply_planned_outfit()
    $ scene_manager.update_actor(erica, position = "stand2", emotion = "happy")
    erica "Alright, well I have to get up early tomorrow for track practice, so I'd better get going."
    lily "See you soon!"
    $ scene_manager.remove_actor(lily)
    $ hall.show_background()
    "You walk with [erica.possessive_title] to the front door. When you get there, she turns to you and gives you a big hug."
    $ scene_manager.update_actor(erica, position = "kissing")
    "She gives you a quick kiss, then turns and leaves."
    $ scene_manager.remove_actor(erica)
    $ mc.change_location(bedroom)
    "You turn around and walk to your room. Damn... what a hot photo session!"
    "You should wait a couple days, then talk to [lily.title] and see how the pics did..."
    $ lily.add_unique_on_talk_event(erica_lily_post_photoshoot)
    return

label erica_lily_post_photoshoot_label(the_person):
    the_person "[the_person.mc_title]! You won't believe it."
    mc.name "Yeah?"
    the_person "My follower count went up almost FORTY PERCENT from the pics we did with [erica.fname] the other night!"
    mc.name "Wow, that's great!"
    the_person "I know! I'm already getting all kinds of requests from people. You HAVE to convince her to do it again, okay?"
    the_person "Do you think we could make this a regular thing? Every Saturday night?"
    mc.name "I mean, that is kind of up to her, but I'll do what I can..."
    the_person "Don't take no for an answer! I know you can do it bro! Tell her I'll double her fee!"
    "Sounds like you should probably talk to [erica.possessive_title] about doing more InstaPics..."
    $ erica.add_unique_on_room_enter_event(erica_post_photoshoot)
    return

label erica_post_photoshoot_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "[erica.possessive_title] is pushing herself hard on the treadmill as you walk up to her."
    mc.name "Hey, I've got good news."
    the_person "Oh hey [the_person.mc_title]! What's the good news?"
    mc.name "It's my sister. She said the photos were a huge success and she wants to know if you can take more photos."
    the_person "Oh! Were they really? I wasn't sure that whole thing was going to work out."
    mc.name "Apparently they turned out great. She wants to know if you want to meet up every Saturday night from here on out, and offered to double your fee."
    the_person "Holy shit... one second..."
    "[the_person.title] turns off the treadmill and hops off so she can talk to you better."
    $ the_person.draw_person(position = "stand2")
    the_person "That's $200 per session? That would be amazing!"
    mc.name "So I'll tell her you'll be there?"
    the_person "Are you going to be the one taking all the pictures?"
    mc.name "I'll do my best, but I won't necessarily be able to do it every week. Don't worry, [lily.title] has a pretty good tripod she invested in recently."
    the_person "Okay. I'll do it! But just so you know, it would really mean a lot to me if you were the one there taking pictures. I don't know why, but having you there made it a lot easier."
    mc.name "If I'm not busy, I'll be there."
    the_person "Wow! Okay. This is going to be a huge change for me."
    $ the_person.change_stats(happiness = 3, love = 3)
    the_person "[the_person.mc_title]... I really appreciate this. I owe you so many favors at this point."
    mc.name "Nonsense. I'm just glad to see you reach your potential. Plus... the pics ARE really hot."
    "[the_person.title] gives you a playful punch on the shoulder."
    the_person "Was there anything else you needed?"
    $ the_person.set_override_schedule(lily_bedroom, the_days = [5], the_times = [4])
    $ lily.set_override_schedule(lily_bedroom, the_days = [5], the_times = [4]) #This should already be set, but just in case, make sure she is there.
    $ erica.add_unique_on_room_enter_event(erica_pre_insta_love)
    $ erica.add_unique_on_room_enter_event(erica_lily_weekly_photoshoot)
    $ erica.event_triggers_dict["insta_pic_intro_complete"] = True
    return

label erica_lily_weekly_photoshoot_label(the_person):
    if not lily.is_available or not erica.is_available:
        return
    $ scene_manager = Scene()
    $ lily_insta_outfit = insta_wardrobe.pick_random_outfit()
    $ mc.change_location(lily_bedroom)
    "You walk down the hall toward [lily.possessive_title]'s room. As you approach her door, you can hear laughter and giggling from the other side."
    "Sounds like [erica.title] is already here! You knock on the door."
    lily "Come in!"
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped, position = "back_peek")
    $ scene_manager.add_actor(erica, position = "back_peek")
    "As you open the door, the two girls are standing in front of [lily.title]'s closet, looking back at you."
    lily "Oh hey [lily.mc_title]. Good timing! We were just picking out what to wear for tonights photos!"
    erica "[lily.fname] thinks we should match, but I was thinking about just wearing something else. What do you think?"
    "It's clear the your opinion is important to her. You think about it for a moment."
    menu:
        "You should match":
            $ erica_insta_outfit = lily_insta_outfit.get_copy()
        "You should wear something similar, but not matching":
            $ erica_insta_outfit = erica.personalize_outfit(lily_insta_outfit.get_copy(), allow_skimpy = False)
        "You should wear your own thing":
            $ erica_insta_outfit = erica.personalize_outfit(insta_wardrobe.pick_random_outfit(), allow_skimpy = False)
    erica "Thanks! I'm still pretty new at this, so it's nice to have your opinion on it."
    $ erica.change_stats(happiness = 1, obedience = 1)
    lily "Alright, before we get going, I need to grab a soda or something. I'm parched!"
    erica "Yeah, me too. Do you have any flavored seltzers?"
    "You think for a second. You could offer to go get them their drinks, and that would give you an opportunity to give them a serum..."
    "If you do, you will probably miss the chance to watch them change..."
    menu:
        "Grab the drinks":
            mc.name "Yeah we have seltzer. Let me go grab drinks for everyone while you two get changed."
            erica "Thanks! Lots of ice with mine please!"
            lily "Me too. You're gonna like the outfits we got for this week bro!"
            $ scene_manager.clear_scene()
            "You step out of [lily.possessive_title]'s room and head to the kitchen."
            $ mc.change_location(kitchen)
            "First, you make a glass with lots of ice for [erica.title]..."
            menu:
                "Add serum to [erica.title]'s drink" if mc.inventory.total_serum_count > 0:
                    call give_serum(erica) from _call_give_serum_erica_insta_20
                    if _return:
                        "You add a dose to her drink, then top it off with seltzer."
                    else:
                        "You think about adding a dose of serum to her drink, but decide against it."

                "Add serum to [erica.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                    pass

                "Leave her drink alone":
                    "You top it off with seltzer."
            "Next, you grab another glass for [lily.title] and a soda."
            menu:
                "Add serum to [lily.title]'s drink" if mc.inventory.total_serum_count > 0:
                    call give_serum(lily) from _call_give_serum_lily_insta_20
                    if _return:
                        "You add a dose to her drink, then top it off with soda."
                    else:
                        "You think about adding a dose of serum to her drink, but decide against it."

                "Add serum to [lily.title]'s drink\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                    pass

                "Leave her drink alone":
                    "You top it off with soda."
            "You pick up both drinks and walk back down the hall to [lily.title]'s room. You open the door and step inside."
            $ mc.change_location(lily_bedroom)
            $ lily.apply_outfit(lily_insta_outfit, update_taboo = True)
            $ erica.apply_outfit(erica_insta_outfit, update_taboo = True)
            $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
            $ scene_manager.add_actor(erica)
            $ mc.change_locked_clarity(25)
            "When you step into the room, you see the girls are both dressed and ready for their photoshoot."
        "Watch them strip":
            lily "Yeah, we have seltzer I think. Let me go grab drinks."
            $ scene_manager.remove_actor(lily)
            "[lily.possessive_title] leaves the room, leaving you for a minute with [erica.title]."
            #TODO small talk?
            "You make a little bit of awkward small talk until she gets back."
            $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
            lily "Alright, let's get ready!"
            "The girls start to strip down."
            $ scene_manager.strip_full_outfit(strip_feet = True) # strip both simultaneously
            $ mc.change_locked_clarity(40)
            "[erica.possessive_title] gives you a sly smile before she starts putting on her outfit."
            $ erica.change_stats(happiness = 2, slut = 2, max_slut = 30)
            $ lily.apply_outfit(lily_insta_outfit, update_taboo = True)
            $ erica.apply_outfit(erica_insta_outfit, update_taboo = True)
            $ scene_manager.update_actor(lily)
            $ scene_manager.update_actor(erica)
            $ mc.change_locked_clarity(20)
            "Once they get dressed, the girls are ready for their photoshoot."
    $ erica_insta_pose_pairs = erica_make_insta_pose_pairs()
    $ current_pos = get_random_from_list(erica_insta_pose_pairs)
    $ erica_insta_pose_pairs.remove(current_pos)
    $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
    $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
    "You snap the first round of pictures."
    if (erica.sluttiness > 20 and lily.sluttiness > 20):
        "The girls seem relaxed. The pictures are coming out natural and they look great together."
        $ mc.change_locked_clarity(10)
        mc.name "Alright, let's do another set, these are great."
        $ current_pos = get_random_from_list(erica_insta_pose_pairs)
        $ erica_insta_pose_pairs.remove(current_pos)
        $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
        $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
        "You snap the second round of pictures"
        if (erica.sluttiness > 40 and lily.sluttiness > 40):
            mc.name "That looks great. Remember, be playful!"
            "[current_pos[2]!i]"
            $ mc.change_locked_clarity(30)
            mc.name "Nice, these are great. How about one more set?"
            "The girls agree and get into a new position."
            $ current_pos = get_random_from_list(erica_insta_pose_pairs)
            $ erica_insta_pose_pairs.remove(current_pos)
            $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
            $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
            if (erica.sluttiness > 60 and lily.sluttiness > 60):
                mc.name "Remember, these are for the thirsty InstaPic boys. Work it for the camera!"
                "[current_pos[3]!i]"
                $ mc.change_locked_clarity(50)
            else:
                "You snap the final set of pictures. This should be good!"
        else:
            "You snap a second set of pictures. This should be good!"
    else:
        "As you snap the first set of pictures, it is clear that girls are faking the smiles and the pictures are looking unnatural."
        mc.name "I'm not sure this is going to do it. Maybe we should try a different pose?"
        $ current_pos = get_random_from_list(erica_insta_pose_pairs)
        $ scene_manager.update_actor(lily, position = current_pos[0], emotion = "happy")
        $ scene_manager.update_actor(erica, position = current_pos[1], emotion = "happy")
        "The girls get into a second pose, but the pictures still feel a little mechanical."
        "They look okay, but you wonder if they could do even better if you could loosen them up a bit more."
    $ scene_manager.update_actor(lily, position = lily.idle_pose)
    $ scene_manager.update_actor(erica, position = erica.idle_pose)
    #TODO special requests. IE topless, kissing, etc.
    #TODO add outfits to wardrobes if they like them.
    #TODO add new outfits?
    "With the pictures done, you give the camera back to [lily.possessive_title]."
    lily "Thanks, [lily.mc_title]! You're the best!"
    erica "Yeah, thanks, [erica.mc_title]. [lily.fname] is it still okay if I spend the night?"
    lily "Of course! I could really use your help studying for my exam coming up."
    "You wish you could come up with a good excuse to stick around, but can't think of anything, so you say goodnight."
    $ scene_manager.clear_scene()
    if erica.sluttiness > 20 and not erica.event_triggers_dict.get("post_insta_handy", False):
        $ mc.business.add_mandatory_morning_crisis(erica_lily_post_insta_handjob)
    elif erica_get_morning_wakeup_pref() == 2 or (erica_get_morning_wakeup_pref() == 1 and renpy.random.randint(0,2) == 1):
        # make sure we add this if it's not already present
        $ mc.business.add_mandatory_morning_crisis(erica_lily_post_insta_morning_mand)

    $ erica.add_unique_on_room_enter_event(erica_lily_weekly_photoshoot)
    $ mc.change_location(bedroom)
    $ del lily_insta_outfit
    $ del erica_insta_outfit
    $ del current_pos
    $ del erica_insta_pose_pairs
    call advance_time() from _call_advance_time_erica_insta_night_01
    return

label erica_lily_post_insta_handjob_label():
    $ the_person = erica
    $ mc.change_location(bedroom) # switch to mc bedroom
    $ mc.location.lighting_conditions = dark_lighting
    $ erica.event_triggers_dict["post_insta_handy"] = True
    "You hear the door to your room slowly open, slowly waking you up."
    $ the_person.draw_person()
    "A figure appears in your door. Is that [the_person.possessive_title]? She slowly makes her way over to your bed, then sits on the side of it."
    $ the_person.draw_person(position = "sitting")
    mc.name "[the_person.title]? Is that you? What time is it?"
    the_person "Yeah, it's me. I am just getting ready to head out for an early morning run. It's 5 am."
    mc.name "Wow. Your commitment to fitness is amazing, you know that?"
    "She chuckles before responding."
    the_person "Thank you. I was just going to head out, but I wanted to come in and say thank you, for setting me up with [lily.fname] and the InstaPic stuff..."
    mc.name "It's fine, you don't have to come in at 5am to tell me that though."
    the_person "I know, but I wanted to make sure I had you alone for what I want to do to show you how thankful I am..."
    "Over your blankets, [the_person.title] reaches over and puts her hand on your chest, then starts to slide it down your body."
    "When she gets to your morning wood, she starts to stroke it."
    $ mc.change_locked_clarity(20)
    "Your sleep addled brain only lets you moan as she starts to work it."
    the_person "Can you pull your blanket down?"
    "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
    "Her hands feel soft and warm."
    if the_person.has_taboo("touching_penis"):
        the_person "I know I've never really been this forward with you before..."
        the_person "But when I was trying to come up with a way to say thanks, this was the best way I could think of."
        mc.name "This is great, but I'm a little tired to reciprocate..."
        the_person "That's okay! Just lay back and let me take care of it."
        $ the_person.break_taboo("touching_penis")
    else:
        mc.name "This is great, but I'm pretty tired. I'm not sure I'll be able to reciprocate."
        the_person "Don't worry, I just want to take care of this for you!"
    "You lay back in your bed and just enjoy it as [the_person.possessive_title] starts to give you a handjob."
    call get_fucked(the_person, start_position = cowgirl_handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_first_handjob_01
    "[the_person.possessive_title] slowly gets up after you finish."
    the_person "Take care [the_person.mc_title]. I'll see you soon!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] quietly leaves your room and you quickly fall back asleep."
    $ clear_scene()
    "You wake up a few hours later. Did [the_person.possessive_title] really come in your room in the middle of the night? Or was that just a dream?"
    $ the_person.add_unique_on_talk_event(erica_post_insta_handjob_followup)
    $ mc.location.lighting_conditions = standard_indoor_lighting
    return

label erica_lily_post_insta_morning_label():
    $ the_person = erica
    if the_person.sex_record.get("Last Sex Day", 9999) == day: #If mandatory and random crisis happen to fire on the same day, suppress the second event.
        return

    $ mc.change_location(bedroom) # switch to mc bedroom
    $ mc.location.lighting_conditions = dark_lighting
    $ option_list = erica_get_wakeup_options()
    "You hear the door to your room slowly open, waking you up."
    $ the_person.draw_person()
    "A figure appears in your door. It's [the_person.possessive_title] again. She tip toes over to your bed, then sits on the side of it."
    $ the_person.draw_person(position = "sitting")
    "Hearing you stir, she leans down and whispers in your ear."
    the_person "Good morning."
    mc.name "Mmm, it's just regular morning right now, but I have a feeling it is about to get good."
    "She chuckles as she reaches down your body and grabs your morning wood through your blankets. She starts to stroke it."
    if the_person.is_willing(drysex_cowgirl) and "drysex" not in option_list:
        the_person "Mmm, it's so hard..."
        "Her voice trails off as she strokes you a few more times."
        the_person "I kind of just want to feel it up against me... do you mind?"
        mc.name "Go ahead."
        "You pull down your blanket, but she leaves your underwear on you as she climbs up on top of you."
        $ the_person.draw_person(position = "cowgirl")
        "As she settles into place, she starts to rub her crotch up against yours."
        "The friction of your clothes and her body rubbing against you feels good, and soon there is a significant amount of heat coming from her crotch that makes it feel even better."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(20)
        $ the_person.break_taboo("touching_body")
        call get_fucked(the_person, start_position = drysex_cowgirl, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_morning_drysex_01
        $ add_erica_wakeup_option("drysex")
        $ the_person.apply_planned_outfit()
        $ the_person.change_slut(1, 40)
        "When she finishes, [the_person.possessive_title] gets up and straightens up her outfit."
        the_person "Thanks, that was nice. I'll see you soon [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] quietly leaves your room and you quickly fall back asleep."
        $ clear_scene()
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return

    if the_person.is_willing(cowgirl_blowjob) and "blowjob" not in option_list:
        the_person "Mmm, it's so hard..."
        "Her voice trails off as she strokes you a few more times."
        the_person "You know, I usually take a protein supplement before I workout, but I don't have any with me..."
        the_person "Do you think you could donate some?"
        mc.name "Hmm, well I suppose if it's for a good cause..."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] lowers herself down your body until you feel her warm breath on your crotch. She opens her mouth and licks your pre-cum from the tip."
        the_person "Mmm, you taste better than those protein powders too..."
        "Opening her mouth, she slides her wet lips down over the tip and runs her tongue all up and down it a few times."
        if the_person.is_bald:
            "You run your hand over her smooth head as she begins to suck you off."
        else:
            "You run your hand thru her [the_person.hair_description] as she begins to suck you off."
        $ the_person.break_taboo("sucking_cock")
        $ mc.change_arousal(20)
        call get_fucked(the_person, start_position = cowgirl_blowjob, the_goal = "oral creampie", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_morning_blowjob_01
        $ add_erica_wakeup_option("blowjob")
        $ the_person.apply_planned_outfit()
        $ the_person.change_slut(1, 60)
        $ play_swallow_sound()
        "When she finishes swallowing, [the_person.possessive_title] gets up and straightens up her outfit."
        the_person "Thanks for the protein... I'll see you later [the_person.mc_title]."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] quietly leaves your room and you quickly fall back asleep."
        $ clear_scene()
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return

    if willing_to_threesome(the_person, lily) and "threesome" not in option_list:
        the_person "God, you are so hard this morning. I need to feel it in me... can I put it in me?"
        mc.name "Of course."
        "As you pull down your blankets and shorts, [the_person.title] gets naked."
        $ the_person.strip_outfit(position = "stand4")
        the_person "Mmm, I can't wait!"
        mc.name "Shhh, you'll wake..."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.possessive_title] jumps on top of you. She grabs your cock, points it towards her hungry cunt, then sits down on it."
        the_person "Mmmm, oh fuck..."
        $ the_person.change_arousal(20)
        $ mc.change_arousal(10)
        the_person "Sorry, I couldn't help it. Taking all those sexy photos last night for all the thirsty guys out there, when the only one I want to fuck was just in the next bedroom over..."
        "[the_person.title] starts to ride you pretty aggressively. You lay back and enjoy it."
        #Swap to scene manager because I was too lazy to do it earlier.
        $ scene_manager = Scene()
        "You close your eyes, just enjoying the sensations. However, an out of place gasp causes you to open your eyes."
        $ scene_manager.add_actor(the_person, position = "cowgirl")
        $ scene_manager.add_actor(lily, display_transform = character_left_flipped(zoom = 0.7))
        "When you open your eyes, you see another figure in your doorway. Is that [lily.possessive_title]?"
        $ scene_manager.update_actor(lily,display_transform = character_left_flipped(zoom = 1.0))
        "She steps into your room."
        lily "Ah, here you are [erica.fname]. I guess I should have known you would sneak in here."
        "[the_person.title] suddenly stops rocking her hips."
        the_person "[lily.fname]? Oh my..."
        lily "You guys are going to wake up mom if you aren't careful, but now that I'm up, can I join you?"
        the_person "You want to join... us?"
        lily "Sure, you just keep doing what you are doing, I'm sure I can put [lily.mc_title]'s tongue to good use."
        "[the_person.title] looks at you, unsure."
        mc.name "Sounds good to me, but like you said, keep it down, we don't want to wake mom up..."
        if mc.business.event_triggers_dict.get("family_threesome", False):
            mc.name "I'm not sure I have the stamina to satisfy all three of you..."
            "[the_person.possessive_title] gasps at your joke."
            the_person "Ha... that's... funny... right?"
            lily "Yeah, he's totally just joking."
        "[lily.title] starts to strip as [the_person.possessive_title] starts moving her hips again."
        $ scene_manager.strip_full_outfit(person = lily)
        "When she finishes, [lily.possessive_title] swings her legs up over your head and brings her pussy to your face."
        call start_threesome(the_person,lily, start_position = Threesome_double_down) from _erica_wakeup_threesome_01
        $ add_erica_wakeup_option("threesome")
        $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_center_flipped)
        $ scene_manager.update_actor(lily, position = "missionary", display_transform = character_right)
        $ the_report = _return
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #Happy family
            $ the_person.change_slut(2, 100)
            $ lily.change_slut(2, 100)
            "[the_person.possessive_title] falls into your bed on one side of you on her side, while [lily.title] lays on her back next to you."
            "You actually start to fall asleep, enjoying the afterglow of your collective orgasms, until you feel [the_person.title] stir."
        else:
            $ the_person.change_slut(1, 100)
            $ lily.change_slut(1, 100)
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        the_person "I think I'm going to take it easy during my workout this morning... you two about wore me out."
        lily "God I know, I think I'm gonna go back to bed..."
        the_person "Next Saturday then [lily.fname]?"
        lily "Of course, and if you're gonna sneak into my brother's room let me know next time okay?"
        the_person "Mmm, maybe. I might want him all to myself though..."
        $ scene_manager.clear_scene()
        "The two girls get up. You fall asleep as they slip out of your room."
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return


    the_person "So, up for anything in particular today?"
    $ position_choice = erica_wakeup_choose_position()
    if position_choice == "Surprise me":
        the_person "Mmmm, okay."
        $ mc.change_arousal(20)
        $ the_person.change_stats(happiness = 5, obedience = -5)
        $ position_choice = get_random_from_list(erica_get_wakeup_options())

    if position_choice == "handjob":
        the_person "I don't know why, I just love the feeling of your thick cock in my hand..."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        the_person "God it's so warm..."
        "[the_person.possessive_title] doesn't waste any time and starts stroking you off."
        call get_fucked(the_person, start_position = cowgirl_handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_wakeup_handjob_02
        $ the_person.change_slut(1, 40)
    elif position_choice == "drysex":
        the_person "It's so big, I want to feel it against me."
        "You pull your blanket down as [the_person.possessive_title] climbs on top of you."
        $ the_person.draw_person(position = "cowgirl")
        "She gets into position and starts to grind up against you. The friction of your clothes and her body feels great."
        call get_fucked(the_person, start_position = drysex_cowgirl, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_morning_drysex_02
    elif position_choice == "blowjob":
        the_person "Let me have a dose of your protein before I go work out."
        "You pull your blanket down and your shorts. When your cock springs free, she takes it in her hand and starts stroking it again."
        $ the_person.draw_person(position = "blowjob")
        "She moves her head down to your crotch and licks your pre-cum from the tip."
        the_person "Mmm, I should do this every time I need some extra protein... you taste so good."
        "[the_person.possessive_title] opens her mouth and begins to bob her head up and down on your morning wood."
        call get_fucked(the_person, start_position = cowgirl_blowjob, the_goal = "oral creampie", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_erica_morning_blowjob_02
        $ the_person.change_slut(1, 60)
    elif position_choice == "anal cowgirl":
        the_person "Mmm, that sounds amazing. But try to be gentle, okay? I still want to go for a run today."
        mc.name "Hey, you're the one who will need to be gentle then, you're the one on top!"
        "[the_person.possessive_title] stands up and starts to strip down."
        $ the_person.strip_outfit(position = "stand4")
        "While she strips, you pull the blanket down and take your shorts off."
        "When she finishes stripping, she gets on top of you, takes your cock in her hand and brings her face down to it."
        $ the_person.draw_person(position = "blowjob")
        "[the_person.title] opens her mouth and licks your morning wood up and down several times, slathering it in her saliva."
        the_person "Mmm, you taste so good..."
        "[the_person.possessive_title] opens her mouth and gives you a couple strokes with her mouth before stopping."
        the_person "God, I could keep going, but it's time to put this someplace a little more fun..."
        $ the_person.draw_person(position = "cowgirl")
        "She climbs on top of you, and with one hand she points your erection up at her puckered hole."
        "She lowers herself gently, but easily takes your hardness into her well trained back passage."
        the_person "Ahhh! Oh fuck it's so big..."
        "It takes her a moment, but soon [the_person.possessive_title] starts to rock her hips. Time to fuck her silly."
        call get_fucked(the_person, the_goal = "anal creampie", start_position = anal_cowgirl, start_object = make_bed(), allow_continue = False) from _call_get_fucked_anal_fetish_erica_morning_wakeup_01
        $ the_person.change_slut(2, 100)
    elif position_choice == "threesome":
        the_person "I'll go get [lily.fname]. She DID say to let her know when I sneak back in anyway..."
        $ clear_scene
        "[the_person.possessive_title] leaves the room. A minute later, she returns with [lily.title] following her."
        $ scene_manager = Scene()
        $ scene_manager.add_actor(the_person)
        $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
        lily "*Yawn* Mmm, I should have known you two would be up to shenanigans again."
        "You pull your blanket down as the two girls get naked."
        $ scene_manager.strip_full_outfit()
        "You can only stare in awe at the two sexy college coeds who are naked, in your room, and ready for a threesome."
        lily "Mmm, I'm too tired to think. [lily.mc_title], how do you want us?"
        call start_threesome(lily, the_person) from _threesome_erica_wakeup_02
        $ scene_manager.update_actor(lily, position = "back_peek", display_transform = character_center_flipped)
        $ scene_manager.update_actor(the_person, position = "missionary", display_transform = character_right)
        $ the_report = _return
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #Happy family
            $ the_person.change_slut(2, 100)
            $ lily.change_slut(2, 100)
            "[lily.possessive_title] falls into your bed on one side of you on her side, while [the_person.title] lays on her back next to you."
            mc.name "God you two are so hot. I must be the luckiest man alive."
            the_person "Mmm, and don't you forget it."
            if the_person.is_girlfriend:
                the_person "Not many girls would be okay with their boyfriend banging their sister..."
                $ the_person.change_love(2)
        else:
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        the_person "I better get up, or I'm going to miss my workout..."
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] gets up and grabs her clothes. She carries them with her, probably going to change in the bathroom on her way out."
        lily "Goodnight [the_person.fname]! I'd better get back to my room too, as fun as it would be to sleep in here..."
        $ scene_manager.remove_actor(the_person)
        $ scene_manager.update_actor(lily, position = "walking_away", display_transform = character_right)
        "You watch as [lily.possessive_title] gets up and excuses herself, her ass swaying back and forth as she walks away."
        $ scene_manager.remove_actor(lily)
        "You fall back asleep. What an incredible midnight rendezvous..."
        $ mc.location.lighting_conditions = standard_indoor_lighting
        return


    $ the_person.apply_planned_outfit()
    "[the_person.possessive_title] slowly gets up after you finish, straightening up her outfit."
    the_person "Take care [the_person.mc_title]. I'll see you soon!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] quietly leaves your room and you quickly fall back asleep."
    $ clear_scene()
    $ mc.location.lighting_conditions = standard_indoor_lighting
    return

label erica_post_insta_handjob_followup_label(the_person):
    the_person "Hey [the_person.mc_title]."
    mc.name "Hey [the_person.title]. You know, I had the craziest dream the other day."
    the_person "Oh?"
    mc.name "Yeah, I had this dream that you came into my room in the middle of the night..."
    the_person "Ah... did this dream have a happy ending?"
    mc.name "Mostly, except it ended with you leaving instead of hopping in bed with me and falling back asleep."
    $ the_person.change_slut(1, 60)
    the_person "Ah, well, that actually wasn't a dream."
    mc.name "Really? I was so tired, I wasn't sure..."
    the_person "Did you... you know... like it?"
    mc.name "Yeah, it was REALLY nice!"
    the_person "Mmm, okay. Maybe I'll do that again next time I come over and spend the night with your sister!"
    mc.name "That would be nice."
    the_person "Did you need something?"
    # continue talk event
    call talk_person(the_person) from _call_talk_person_handjob_followup
    return

label erica_pre_insta_love_label(the_person):
    "You walk down the hall to [lily.possessive_title]'s room, ready to help out with InstaPic."
    "You knock on the door, but are surprised when it is answered by [the_person.possessive_title]."
    $ the_person.draw_person()
    mc.name "Oh! Hey [the_person.title]."
    the_person "Hey! [lily.fname] just left, she is going to pick us up some sushi tonight!"
    mc.name "Oh, that's great. Have her come get me when she gets back and we can start."
    the_person "Ok... why don't you just come in now? Actually I've been meaning to talk to you about something."
    mc.name "Oh, okay. Sure."
    "You step into [lily.title]'s room and close the door behind you. You and [the_person.possessive_title] walk over and sit on the bed."
    $ the_person.draw_person(position = "sitting")
    mc.name "Is something wrong?"
    the_person "No, not at all. The opposite actually."
    the_person "I just wanted to tell you, I really appreciate all the help you have been giving me."
    the_person "I feel like the more I get to know you, the more I like you. You workout with me, helped me pay for classes, even welcomed me into your home."
    if erica_get_is_doing_yoga_sessions():
        the_person "You even welcomed me into your business, teaching yoga to a bunch of really neat ladies."
    the_person "I'm not really sure where everything is going, but I see all the hard work you put into things, and I guess I just want you to know that I notice and appreciate it."
    the_person "Just understand... I'm really busy, right? With school, and track, and everything. I don't have much more time for extracurricular stuff!"
    mc.name "That is very kind of you to say, and don't worry, I understand we can't spend every waking moment together, and I'm okay with that."
    the_person "So... I was thinking, since [lily.fname] is gonna be gone for a bit, maybe I could SHOW you how much I appreciate you!"
    "[the_person.possessive_title] slides down onto the floor on her knees in front of you."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(20)
    mc.name "I think I'm supposed to say that you don't have to do this, but I can tell you want to, so I'll say what I'm really thinking."
    mc.name "I can't wait to feel your mouth on me."
    the_person "Mmm, glad to hear it!"
    "[the_person.title] pulls at your zipper then reaches in, fishing out your dick. She gives it a few strokes and smiles up at you."
    if the_person.has_taboo("sucking_cock"):
        the_person "I've been wanting to do this for a while. Mmm, you smell so manly."
        "[the_person.possessive_title] gives the tip a few exploring licks."
        the_person "I guess I'd better get to work... I'm not sure how long [lily.fname] is going to be gone."
        "[the_person.title] opens her mouth. She slides her wet, velvet lips down your erection."
        $ the_person.break_taboo("sucking_cock")
        $ mc.change_locked_clarity(50)
    else:
        the_person "Mmm, you smell so manly. I love the way you taste and the way you feel so hot in my mouth."
        "[the_person.possessive_title] gives the tip a few exploring licks."
        the_person "I guess I'd better get to work... I'm not sure how long [lily.fname] is going to be gone."
        "[the_person.title] opens her mouth. She slides her wet, velvet lips down your erection"
        $ mc.change_locked_clarity(50)
    "[the_person.title] starts to bob her head up and down, eager to satisfy you with her mouth."
    $ mc.change_arousal(10)
    "It's so hot, getting a blowjob from [the_person.possessive_title] while sitting on your sister's bed!"
    call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_erica_pre_insta_oral_01
    "When you finish, [the_person.possessive_title] quickly starts to straighten up her clothes and wipes the cum from her face."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    mc.name "[the_person.title]... that was awesome."
    the_person "Mmm, thanks! But you should probably get out before [lily.fname] gets back!"
    the_person "Just go back to your room and pretend like nothing happened."
    mc.name "Should I come back to take pics?"
    the_person "Up to you! Now go!"
    $ clear_scene()
    $ mc.change_location(bedroom)
    "You clear out of [lily.possessive_title]'s room and head back to yours. Damn, now you feel so tired."
    "Should you go back and take pics? You have a bit to think about it."
    $ erica.event_triggers_dict["pre_insta_blowjob"] = True
    return

init 2 python:
    def erica_get_wakeup_options():
        return erica.event_triggers_dict.get("wake_up_options", ["handjob"])

    def add_erica_wakeup_option(option):
        if not "wake_up_options" in erica.event_triggers_dict:
            erica.event_triggers_dict["wake_up_options"] = erica_get_wakeup_options()
        if not option in erica_get_wakeup_options():
            erica.event_triggers_dict["wake_up_options"].append(option)
        return

    def erica_wakeup_choose_position():
        tuple_list = []
        for position in erica_get_wakeup_options():
            tuple_list.append([position.title(), position])
        tuple_list.append(["Surprise me", "Surprise me"])

        return renpy.display_menu(tuple_list,True,"Choice")

    def erica_get_morning_wakeup_pref():
        return erica.event_triggers_dict.get("morning_wakeup_pref", 0)

    def erica_pre_insta_blowjob_complete():
        return erica.event_triggers_dict.get("pre_insta_blowjob", False)
