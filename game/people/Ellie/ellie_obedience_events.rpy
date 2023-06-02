# Obedience Events
init -1 python: #Requirement functions
    def ellie_tit_fuck_requirement():
        if not mc.business.is_open_for_business:
            return False
        if not ellie.story_event_ready("obedience"):
            return False
        if mc.location == mc.business.r_div and ellie.obedience >= 120:
            return True
        return False

    def ellie_start_search_requirement():
        if not (mc.is_at_work and mc.business.is_open_for_business):
            return False
        if ellie.days_since_event("obedience_event") <= TIER_2_TIME_DELAY:
            return False
        if mc.business.get_event_day("IT_dir_nanobot_takeover_day") < TIER_3_TIME_DELAY:
            return False
        if ellie.obedience >= 140 and nanobot_program_is_IT():  #Need to make sure we know contact has ghosted head researcher.
            return True
        return False

    def ellie_search_update_requirement(the_person):
        if not (mc.is_at_work and mc.business.is_open_for_business):
            return False
        if not ellie.story_event_ready("obedience"):
            return False
        if not ellie_has_given_blowjob():
            return False
        return True

    def ellie_search_finish_requirement():
        if not (mc.is_at_work and mc.business.is_open_for_business):
            return False
        if not ellie.story_event_ready("obedience"):
            return False
        if time_of_day == 3:
            return True
        return False

    def ellie_submission_requirement():
        if not (mc.is_at_work and mc.business.is_open_for_business):
            return False
        if not ellie.story_event_ready("obedience"):
            return False
        if ellie.obedience > 160 and time_of_day == 3:
            return True
        return False

    def ellie_nanobot_fetish_testing_requirement(the_person):
        return False

    def ellie_nanobot_fetish_requirement(the_person):
        return False

init 1 python:
    ellie_start_search = Action("Ellie was framed", ellie_start_search_requirement, "ellie_start_search_label")
    ellie_search_update = Action("Finding the Culprit", ellie_search_update_requirement, "ellie_search_update_label")
    ellie_search_finish = Action("Ellie's Revenge", ellie_search_finish_requirement, "ellie_search_finish_label")
    ellie_submission = Action("Ellie's submission", ellie_submission_requirement, "ellie_submission_label")
    ellie_nanobot_fetish_testing = Action("Ellie's first fetish", ellie_nanobot_fetish_testing_requirement, "ellie_nanobot_fetish_testing_label")
    ellie_nanobot_fetish = Action("Give Ellie another fetish", ellie_nanobot_fetish_requirement, "ellie_nanobot_fetish_label")

    def add_ellie_tit_fuck_action():
        ellie_tit_fuck = Action("Use Ellie's Tits", ellie_tit_fuck_requirement, "ellie_tit_fuck_label")
        mc.business.add_mandatory_crisis(ellie_tit_fuck)
        ellie.story_event_log("obedience")
        return

label ellie_tit_fuck_label(): #120 obedience. Unlocks Ellie's tit fucks
    $ the_person = ellie
    $ mc.change_arousal(30)
    $ the_person.event_triggers_dict["tit_fuck"] = True
    $ mc.change_location(mc.business.r_div)
    "You sit at a desk, working in the research department."
    "However, you are having an incredibly hard time concentrating. You look across the room at [the_person.possessive_title]."
    $ the_person.draw_person(position = "sitting")
    $ desc_string = mc.business.string_since_event("hired_ellie_IT")
    "You hired her [desc_string]."
    "Since then you've found yourself getting closer with the buxom redhead. You gaze at her from across the lab."
    "Her chest heaves slightly with every breath. You can't help but fantasize about sliding your cock between her generous tits."
    $ mc.change_locked_clarity(30)
    "You imagine in your mind, pinching and rolling her nipples between your fingers as fuck her soft, pillowy tit flesh..."
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title] looks up, and realizes you are staring at her."
    the_person "You okay over there, [the_person.mc_title]?"
    "You see some color in her cheeks. She knows you were checking her out."
    "Instead of answering you, you stand up and walk over to her desk. You see her bite her lip as you approach."
    the_person "Sir?"
    "Something shifts in your mind. Why just fantasize? [the_person.title] is your employee."
    "She's been opening up to you recently, and you've been more than generous with her with her work. You deserve a kickback."
    mc.name "I need your help with something, can you come with me?"
    the_person "Of course..."
    $ the_person.draw_person(position = "stand2")
    "You walk quietly to your office with [the_person.possessive_title] following you."
    $ mc.change_location(ceo_office)
    "You step into your office. After she follows you in, you close and lock the door."
    the_person "[the_person.mc_title], you're scaring me..."
    mc.name "[the_person.title], you've been doing great work for me ever since I hired you. Your work on the company IT programs has been examplary."
    mc.name "However, if I'm being honest, sometimes working with you is a bit of a struggle for me."
    the_person "I'm sorry sir. I don't want to be a problem, what is wrong with my work?"
    mc.name "There's nothing wrong with your work. The problem is your body."
    the_person "My... body?"
    mc.name "You have incredible curves. After working with you for extended periods, it becomes impossible for me to concentrate."
    $ the_person.change_stats(slut = 2, max_slut = 40)
    "[the_person.possessive_title] gasps as you start to pull out your cock. It is rock hard from your previous fantasizing."
    mc.name "I need you to take care of this for me. On your knees."
    if the_person.sluttiness >= 40: #Gladly
        the_person "Of course [the_person.mc_title]. Sorry I'm still kinda new to this, I didn't realize you need me so bad."
    else:
        "[the_person.title] hesitates for a second, but then slowly, obediently, gets down on her knees."
    $ the_person.draw_person(position = "blowjob")
    if the_person.tits_available:
        "You look down at [the_person.possessive_title]. Her tits are out and she looks ready to service you."
    else:
        mc.name "Let's get this off..."
        "You quickly pull at her top before she has a chance to resist."
        $ the_person.strip_to_tits(position = "blowjob")
        $ the_person.break_taboo("bare_tits")
        "She looks up at you, waiting for you to take the lead."
    $ mc.change_locked_clarity(30)
    mc.name "I want you to do something different for me. I want you to put my cock between your tits."
    the_person "You want to put your thing between my... my boobies?"
    mc.name "Tits. When we are having sex, they're called tits. And yes, I want to fuck your tits."
    $ the_person.change_stats(obedience = 2)
    the_person "Ah ok... you can... fuck my titties..."
    "[the_person.title] hesitates a bit, but soon obediently complies, moving close to you."
    "[the_person.possessive_title] lifts up her knees a little. She looks up at you, obviously still a little unsure, but you nod your encouragement."
    "You help press forward a bit when her soft tit-flesh finally makes contact with your groin. You take her hands in yours and show her how to wrap her tits around you."
    $ the_person.break_taboo("touching_penis")
    mc.name "There, now just... bounce them a little."
    the_person "Ah, okay."
    "[the_person.title] uses her hands to move her big tits up and down your cock. The soft flesh feels amazing sliding up and down."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20) #50
    "You let out a low, growling moan. It feels so good to finally have your cock buried between the buxom redheads tits."
    "Your pre-cum is starting to leak out, but you could definitely use some lube. You stop her for a moment."
    the_person "[the_person.mc_title]?... ahhhh."
    "You let a large amount of saliva out of the bottom of your mouth. It splatters onto her chest and into her cleavage."
    mc.name "There, add some of your own too. IT feels better."
    the_person "Ah, yes sir..."
    "[the_person.possessive_title] adds some of her own spit to yours, working it down into her cleavage by jiggling her tits with her hands."
    mc.name "Mmm, that's better. Keep going now."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20) #70
    "[the_person.title] is clumsily jiggling her tits around your cock. Thankfully her flesh is so soft it feels pretty good anyway."
    "You reach down and grab [the_person.title]'s tits yourself. She places her hands over yours and holds them in place."
    the_person "Stars... your thing is so warm..."
    "You squeeze down hard on her breasts and work your hips, fucking her soft cleavage. [the_person.title] moans in response."
    $ the_person.change_arousal(30)
    mc.name "Cock. Its called my cock. It feels good, doesn't it? To get down on your knees and service my cock like this."
    the_person "Yes..."
    mc.name "Say it. I want you to tell me how much you love getting your tits fucked like this."
    "[the_person.title] stutters for a moment."
    mc.name "Its okay. Just say it."
    the_person "I... it feels so right. I love it! Please fuck my tits [the_person.mc_title]!"
    $ mc.change_arousal(20) #90
    "Your pre-cum is leaking pretty heavily now. It adds to the pleasure of [the_person.possessive_title] fucking you with her tits."
    "She stops moving her tits for a second to spit down into her cleavage. She moves her breasts up and down, slathering you up before continuing."
    $ mc.change_locked_clarity(50)
    $ mc.change_arousal(20) #110
    mc.name "Oh god. [the_person.title], I'm almost there. Keep going!"
    the_person "Okay [the_person.mc_title]!"
    "This southern redhead's big titties are amazing, bouncing up and down around your cock. It's getting ready to burst."
    $ mc.change_locked_clarity(50)
    $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_person)

    "Your orgasm builds to a peak and you grunt, blasting your load up between [the_person.title]'s tits and out the top of her cleavage."
    $ the_person.cum_on_tits()
    $ the_person.draw_person(position = "kneeling1")
    "Your cum splatters down over the top of [the_person.title]'s tits. She gasps as the warm liquid covers her and drips back down between them."
    "She looks up at you. She has no idea what to do."
    mc.name "Hang on, let me get you some tissues and wet wipes."
    "You quickly walk back to your desk and pull some out and hand them to her."
    $ the_person.draw_person()
    the_person "There's so much! And so warm..."
    $ the_person.change_arousal(20)
    "You help her get cleaned up, then back into her outfit."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    mc.name "That was amazing. Exactly what I needed."
    the_person "Ah, yeah that was nice. Do you want to do it again sometime?"
    mc.name "I do. But for now I need to recover a bit before I go back to work."
    $ the_person.change_stats(obedience = 3)
    the_person "Okay. I'm going to get back to work then."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] awkwardly turns and leaves your office. You can't help but smile."
    "She'll get used to servicing your needs in your office with more than just her tits soon enough. For now you are content with the leap of progress you have made with her."
    $ mc.business.add_mandatory_crisis(ellie_start_search)
    $ ellie.story_event_log("obedience")
    $ clear_scene()
    return

label ellie_start_search_label(): #140 obedience. Scene where you talk to ellie and Steph about the contact
    $ the_person = ellie
    $ scene_manager = Scene()
    $ the_researcher = mc.business.head_researcher
    $ mc.change_location(mc.business.r_div)
    "You walk into the Research department. As you step in, you see [the_researcher.title] look up from her work and walk over to you."
    $ scene_manager.add_actor(the_researcher)
    the_researcher "Hey [the_researcher.mc_title]. You'll never believe what just happened to me."
    mc.name "What's that?"
    the_researcher "Remember my nanobot contact? The guy that ghosted us?"
    mc.name "Of course."
    the_researcher "Well, I was posting some selfies to my DikDok, and I got a bunch of comments from him!"
    mc.name "Wow... how do you know it was him?... And you are on DikDok?"
    the_researcher "Yes, and I know because he has a very unique last name, and his username was basically just his first initial and last name..."
    mc.name "Huh. You know who might be interested in that?"
    the_researcher "Who?"
    "You look over to the other side of the lab."
    mc.name "Hey [the_person.title]! Come her for a second!"
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped)
    the_person "Hey, what's the fuss?"
    mc.name "Remember the guy from your last employer that set you up and got you fired?"
    the_person "Stars, how could I forget that jerk!"
    mc.name "He is hitting on [the_researcher.title] on DikDok."
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "He... He what!?!"
    the_researcher "Yeah. He keeps asking for nudes, but doesn't want to pay for em'. I keep blowing him off."
    the_researcher "His last message, he said he lives in the same area as me and was willing to pay $100 for a blowjob."
    the_person "UGH. Typical. What I wouldn't do to get my hands on that good for nothin'..."
    "As [the_person.possessive_title] goes off about the guy, a plan slowly begins to form in your head..."
    "He sounds like a total creep... but you would score major bonus points with [the_person.title] if you could help her get back at him."
    "You wonder... could you lure the guy in? Then capture him offering to pay for sex on video and blackmail him... or even get him arrested?"
    "You probably shouldn't turn him over to the authorities... but blackmail could work..."
    mc.name "Hey [the_researcher.title]. On DikDok, it isn't uncommon to do shoutouts, right? Especially to new accounts?"
    the_researcher "Yeah I think I've seen a few of those."
    mc.name "[the_person.title]... I have an idea."
    the_person "Yeah?"
    $ scene_manager.update_actor(the_person, emotion = "happy")
    mc.name "We're going to set you up with a DikDok account and have [the_researcher.title] do a shoutout for you."
    mc.name "He is sure to see it. We already know he's willing to pay for sexual favors. We'll use the account to lure him in and get dirt on him."
    the_researcher "Damn, a classic honeypot."
    the_person "I ahm, I don't know. Isn't that thing for like, women who send out pictures of themselves naked?"
    mc.name "That is precisely what it is. And for making money off them."
    the_person "I don't know if I can do something like that..."
    mc.name "Non sense. Of course you can. It isn't like you are just doing it for fun, we could use them to get back at him."
    "[the_person.possessive_title] seems to be wavering a bit, so you decide to push her a bit..."
    mc.name "Here, let me see your phone, I'll help you set up an account."
    the_person "Ah, okay, I guess we can try."
    $ the_person.add_role(dikdok_role)
    $ the_person.event_triggers_dict["dikdok_known"] = True
    "You walk her through getting her account set up."
    "Of course you make note of the name so you can check up on it."
    $ the_person.change_stats(obedience = 3)
    mc.name "Alright, once in a while make a new posting with a pic of you doing something naughty, but first let's get you a promo."
    mc.name "Let's go back to the testing room."
    #TODO make a testing room background and transition to it here.
    "You walk with the girls back to the serum testing room for privacy."
    mc.name "Alright, [the_researcher.title], you make a video. Say something like, hey guys, just found out my super hot coworker has an account too and everyone should check it out."
    if the_person.tits_available:
        mc.name "Then you can zoom in on [the_person.title]'s tits and she'll shake em' around or something. Then plug her username and we'll see if we can get a hit. Sound good?"
    else:
        mc.name "Then you can zoom in on [the_person.title] and she'll take her top off. Then plug her username and we'll see if we can get hit. Sound good?"
    the_researcher "Sounds great to me!"
    the_person "You... you wanna take a video of mah tits?"
    mc.name "That's the idea, yeah."
    the_person "I... I dunno, I'm not sure I want a video like that going around on the internet..."
    mc.name "Don't worry. We're just doing this to help you get even, remember?"
    the_researcher "Don't worry, it is fun too!"
    the_person "Okay... I guess..."
    "You make a mental note to thank [the_researcher.possessive_title] for helping convince [the_person.title] to take some topless pics later..."
    mc.name "Alright, well, this should be straight forward. [the_researcher.title]... whenever you are ready?"
    the_researcher "Okay."
    "[the_researcher.possessive_title] pulls out her phone and takes a few seconds to boot up the app."
    if the_person.is_bald:
        "She checks her make-up and then starts the video."
    else:
        "She takes a few seconds to straighten her hair, then starts the video."
    the_researcher "Hey guys! Guess what!?!"
    "Her mock enthusiasm is amusing, but you keep yourself from laughing and ruining the video."
    the_researcher "I just found out... the new girl at work... has a DikDok account too! And she JUST STARTED!"
    the_researcher "She is smoking hot too... I just wanted to give her a quick shoutout!"
    "[the_researcher.title] takes her phone and moves the camera around to get [the_person.title] in frame."
    the_researcher "Here she is! Show my viewers what they're missing!"
    if the_person.tits_available:
        $ scene_manager.update_actor(the_person, position = "kneeling1")
        "[the_person.title] smiles, then takes her tits in her hands and pushes them together, giving them a squeeze."
    else:
        $ scene_manager.strip_to_tits(the_person)
        "[the_person.title] smiles, then takes her top off, revealing her big tits."
    $ mc.change_locked_clarity(30)
    "[the_researcher.possessive_title] brings the camera back to her."
    the_researcher "Damn, right? Anyway, here's her username..."
    "[the_researcher.title] finishes up the promo video."
    $ scene_manager.update_actor(the_person, position = "stand3")
    mc.name "There, that wasn't so bad, was it?"
    the_person "No... actually it was kinda fun... do you think people will like it?"
    the_researcher "I mean, I'm mostly straight, but I loved it. Your tits are fantastic."
    the_person "Aww, thanks [the_researcher.name]."
    $ the_person.increase_opinion_score("showing her tits", max_value = 1)
    mc.name "Alright, [the_person.title], once or twice a day, take a video or a couple pics and drop them on there."
    mc.name "[the_researcher.title] will give you the guy's username. If you get any DMs from him, start talking to him and see if you can get anything going, okay?"
    the_person "Yessir."
    "The two girls get together and start to talk about the mysterious contact. You decide to leave them to it."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.remove_actor(the_researcher)
    "You step out of the examination room. You have no idea if this plan will work or not, but you know it will take time to find out."
    "Even if the guy never bites, at least you convinced [the_person.title] to start a DikDok account..."
    $ del the_researcher
    $ ellie.story_event_log("obedience")
    $ the_person.add_unique_on_room_enter_event(ellie_search_update)
    return

label ellie_search_update_label(the_person):    #You locate the contact
    $ mc.change_location(mc.business.r_div)
    "You step into the Research and Development department. When you do, [the_person.title] notices you, gets up, and walks over to you."
    $ the_person.draw_person()
    the_person "Hey! Have a second? I have something I need to talk to you about... you know... in private."
    mc.name "Sure. Let's head for my office."
    $ mc.change_location(ceo_office)
    "You walk into your office with [the_person.possessive_title] and sit down."
    $ the_person.draw_person(position = "sitting")
    the_person "Well, Alan, you know that guy we've been trying to find, messaged me on DikDok and I've been messaging back and forth with him."
    mc.name "That is excellent news."
    the_person "I keep trying to get him to meet up, you know, like you told me to do, but so far he hasn't taken any interest."
    the_person "I sent him some pretty umm... interesting... pics, but I can't convince him I'm being legitimate."
    mc.name "Ahhh, he is wary. Have you offered to exchange sexual favors with him?"
    the_person "Umm, yeah I did that, but he doesn't believe me."
    "You think about it for a moment, but you are able to come up with a solution."
    mc.name "What if we get some pictures to send him of you actually doing some of those sexual favors?"
    the_person "Whaddya mean?"
    mc.name "He doesn't believe that you'll actually do anything with him... what if we take a picture of you sucking on my dick and send it to him."
    mc.name "If he truly doesn't believe you would be willing to, it would convince him otherwise."
    if ellie_has_given_blowjob():
        the_person "I dunno... taking pictures while I suck your dick seems like it might be taking things a little too far..."
    else:
        the_person "I... I don't know... that feels like we are taking this whole thing a little too far..."
    mc.name "I know it feels that way, but don't worry, this is just an act to try and expose him."
    "[the_person.possessive_title] mutters something under her breath. She seems unconvinced."
    "You decide to push the issue before she has the chance to think it through."
    mc.name "Come here. It will take just a few minutes, and if it doesn't work, it'll be no big deal."
    the_person "I... okay..."
    $ the_person.draw_person(position = the_person.idle_pose)
    "After hesitating, [the_person.title] obediently gets up and walks around your desk."
    mc.name "Here, let me have your phone. I'll take the pictures. Go ahead and get on your knees."
    $ the_person.draw_person(position = "blowjob")
    "Slowly but obediently, [the_person.possessive_title] hands you her phone and then gets on her knees in front of your chair."
    if the_person.tits_available:
        "You feel your cock twitch in your pants as you look down at the busty redhead, on her knees at your desk, her tits already on display."
    else:
        mc.name "Get your tits out, we want to make this look good."
        the_person "Yes sir."
        $ the_person.strip_to_tits(position = "blowjob")
    "You pull out your dick, now rock hard, and take a picture of [the_person.title] with her face right next to it."
    $ mc.change_locked_clarity(30)
    if ellie_has_given_blowjob():
        mc.name "Alright, you know what to do. Just pretend like I'm not even taking pictures."
    else:
        mc.name "Alright. I know you don't have a lot of experience with this, but don't worry, it's easy."
        the_person "I... I'll try..."
    "You put your free hand on the back of [the_person.possessive_title]'s head. She opens her mouth and lets you guide her lips down to the tip."
    "[the_person.title]'s lips part, and you feel the tip of your cock slide into her soft, wet mouth."
    $ mc.change_locked_clarity(30)
    if ellie_has_given_blowjob():
        "[the_person.possessive_title] has been working on her oral technique, you can tell as she swirls her tongue around the tip."
    else:
        "You've finally gotten [the_person.possessive_title] to give you a blowjob, and victory feels amazing."
    mc.name "Look up at me while you do that."
    "[the_person.title] looks up at you as her tongue plays with the tip. You snap a couple quick pictures."
    mc.name "Damn that's hot. Now make me feel good, the quicker you work the sooner we can get the pictures we need."
    if ellie_has_given_blowjob():
        "[the_person.title] just nods and then starts to bob her head up and down, stroking you with her lips and tongue."
    else:
        "[the_person.title] pops off your cock."
        the_person "Can't you just like... you know... do it yourself? Then get pics when you finish?"
        mc.name "No. You can tell when people take fake pictures like that. Sucking on dick smears lipstick, makes things messy..."
        "[the_person.possessive_title] reluctantly gives in and starts her blowjob in earnest."
        "You pull her head back down on your cock, and her head starts to bob up and down."
    $ mc.change_locked_clarity(50)
    "You hands on her head guide her inexperienced mouth as she gets to work, sucking you off."
    "You make sure to snap a couple pictures here and there, her face getting progressively messier as things continue."
    mc.name "Let's get a picture of you taking it deep, okay?"
    "[the_person.title] looks up, a hint of fear in her eyes, but she nods."
    mc.name "Alright, just relax, and let me guide you down."
    "Slowly, you pull her head down your cock further and further, until at last her nose is touching your skin."
    "You snap a couple quick pictures, when she suddenly gags hard and backs off."
    $ mc.change_locked_clarity(50)
    the_person "Stars! You are so big..."
    "She takes a moment to recover, then with your encouragement gets back to work."
    "The soft slurping noises of [the_person.possessive_title] as she blows you are really turning you on."
    "Her steamy mouth milking your cock is getting to you. You are going to cum soon."
    mc.name "I'm gonna cum. Let me cum on your face, it'll make the most convincing pictures."
    $ the_person.draw_person(position = "kneeling1")
    "[the_person.title] pops off your cock and looks up at you as you point it at her face and give it the final few strokes."
    $ the_person.cum_on_face()
    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
    "You do your best to snap pictures as you finish all over [the_person.title]'s face. One spurt hits her in the eye and she flinches."
    the_person "Ah! Careful where you point that thing!"
    $ the_person.event_triggers_dict["given_blowjob"] = True
    "You finish cumming with one last drip that lands on [the_person.possessive_title]'s chin."
    "Satisfied with your work, you quickly snap a few pictures."
    mc.name "Go ahead and get cleaned up, I'll DM him the pictures."
    the_person "Umm... right..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] stands up and turns around, looking for something to wipe her face off with."
    "You open up her DikDok account and find the messages with the contact. You quickly read through the more recent ones, and discover she really has been trying to bait this guy."
    "You quickly upload a few from your blowjob session. The last one is with [the_person.title]'s face plastered with your cum."
    "This could have been you ;)"
    "You send him a message with it. Let's see if he takes the bait or not."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    "You are starting to come up with a plan for what to do if this guy responds when [the_person.title] comes back."
    the_person "Alright, did I get it all?"
    mc.name "Yeah, I think you did. Alright, here is the plan. I want you to see if you can seduce this guy. Make it clear that you want to meet up and go back to his place, okay?"
    the_person "Umm... okay?"
    mc.name "When you do, me and [mc.business.head_researcher.fname] will be there. We'll get some blackmail material on him and then decide our next move."
    the_person "Okay... but like... I won't have to actually do anything with him... right?"
    mc.name "Of course not. We'll be there to put a stop to anything."
    the_person "Hmm... okay... I guess I can try."
    mc.name "Alright. I'm going to coordinate this with the head researcher. Go ahead and get back to work."
    the_person "Yes sir."
    $ the_person.draw_person(position = "walking_away")
    "As [the_person.possessive_title] turns and leaves the office, you call your head researcher to your office."
    $ clear_scene()
    $ the_person = mc.business.head_researcher
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I do. I need you to procure some equipment for me."
    the_person "Oh?"
    mc.name "I need some remote monitoring equipment. It needs to be extremely discreet, and capable of 2 way communication."
    the_person "Like... an ear piece? Like from a spy movie?"
    mc.name "Yes, exactly. I also want you to procure a spare set of portable hard drives and computer imaging software."
    the_person "Okay... what for?"
    mc.name "I have [ellie.fname] working on seducing our nanobot contact. If she is successful, I want to go through his home for blackmail material while he is... occupied..."
    the_person "Oh wow! That's pretty ballsy. Are you sure she's up for it?"
    mc.name "Yes, I think so. Are you?"
    the_person "Hell yeah, nothing like some breaking and entering to get the blood flowing."
    mc.name "Good. Acquire is as soon as possible. Charge it to the company account, I'm not sure when we will have our opportunity, but hopefully soon."
    the_person "Yes sir."
    "You share a few more details of your plan with [the_person.possessive_title], then she returns to work."
    $ the_person.draw_person(position = "walking_away")
    "You aren't sure what kind material you will find, going into this guy's apartment, but you are sure you will be able to find something."
    $ clear_scene()
    "There is just one more piece to the puzzle you need..."
    if starbuck_is_business_partner():
        "You place a phone call to your business partner at the mall."
        starbuck "Hello?"
        mc.name "Hey, it's me. I need you to get a few... shall we say... roleplaying outfits for me..."
        starbuck "Oh! Sounds fun! What do you need?"
    else:
        "You look up a listing of businesses at the mall, and one catches your eye."
        "You dial up the listing for the Sex Shop."
        starbuck "Hello?"
        mc.name "Hello. I was hoping to place a special order for some... roleplaying outfits..."
        starbuck "Oh! What are you looking for?"
    "..."
    $ ellie.story_event_log("obedience")
    $ mc.business.add_mandatory_crisis(ellie_search_finish)
    return

label ellie_search_finish_label():    #You and Ellie sabotage the contact
    $ police_chief_wardrobe = wardrobe_from_xml("Cop_Wardrobe")
    $ cop_outfit = police_chief_wardrobe.get_outfit_with_name("Cop")
    $ prost_outfit = prostitute_wardrobe.get_outfit_with_name("Body Suit")
    $ ellie.add_outfit(prost_outfit)    # she might want to surprise you by wearing it
    $ the_person = ellie
    $ the_researcher = mc.business.head_researcher
    $ scene_manager = Scene()
    "You feel your phone vibrate in your pocket."
    $ mc.start_text_convo(the_person)
    the_person "Hey! I got a hit with the contact! Let's meet in your office!"
    mc.name "I'll be right there."
    $ mc.end_text_convo()
    "Before you go to your office, you text [the_researcher.possessive_title]."
    $ mc.start_text_convo(the_researcher)
    mc.name "Hey. Tonight is the night, meet me in my office ASAP, and bring the equipment."
    the_researcher "OMW"
    $ mc.end_text_convo()
    $ mc.change_location(ceo_office)
    "You hurry to your office. [the_person.title] is right behind you."
    $ scene_manager.add_actor(the_person, position = "sitting")
    "She sits down at your desk and starts to talk hurriedly, clearly nervous."
    the_person "I got him to agree to meet up tonight! He wants to meet for a quick bite, then back to his place to 'see what happens'."
    "She cringes a bit with the last part of the sentence."
    mc.name "Excellent job."
    $ scene_manager.add_actor(the_researcher, display_transform = character_center_flipped)
    "[the_researcher.possessive_title] walks into your office, carrying some electronics."
    mc.name "[the_researcher.title], thanks for coming. Did you get the equipment?"
    the_researcher "I sure did. Here's the hard drives, they have software installed to immediately begin imaging and copying any systems they get plugged into..."
    the_researcher "And here is the wire. It should fit nicely into her ear, and with her long hair it will be basically imperceptible unless someone goes looking for it."
    the_person "The wire?"
    mc.name "We are going to give you a recoding and 2 way communication device, that way we can monitor your situation and hopefully get some blackmail material that way as well."
    the_person "I see."
    the_researcher "So like... what are we going to do if his neighbor or something catches us?"
    mc.name "Leave that to me. We have on more stop before dinner time."
    mc.name "Let's go."
    $ mc.change_location(mall)
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "You go with the two girls to the mall, then walk into the sex shop."
    $ mc.change_location(sex_store)
    "You step into the sex store with [the_person.title] and [the_researcher.possessive_title], looking for someone..."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    if starbuck_is_business_partner():
        starbuck "Hello there, can I help... Oh hey there [starbuck.mc_title]."
        mc.name "Hello [starbuck.title]. I'm here to pick up those outfits I called about the other day."
        starbuck "Oh! The two police uniforms and one 'lady of night' costumes?"
        mc.name "That is them."
        starbuck "Ah! I don't know what you have planned for those, but I wish I could join! You umm... have room for one more?"
        mc.name "Not this time."
        starbuck "What a shame. Give me a moment I'll find them."
    else:
        starbuck "Hello there, can I help you?"
        mc.name "Ah yes, I called in a few days to order a few outfits, two police officers and..."
        starbuck "Ah! And the lady of the night, of course. Give me just a moment, they just came in!"
    $ scene_manager.remove_actor(starbuck)
    the_person "Did she say lady of the night? What... What's that supposed to mean?"
    "[the_researcher.possessive_title] just looks at you with a smirk."
    "After a few moments, [starbuck.possessive_title] returns with the outfits."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    starbuck "Here they are. Did you want to try them on before you buy them?"
    mc.name "Yes. Actually I was hoping we could leave wearing them."
    starbuck "Oh my. What an adventurous group. Yes that would be fine! The dressing room is back there."
    $ scene_manager.remove_actor(starbuck)
    "You walk back to the dressing room with [the_person.possessive_title] and [the_researcher.title]. You each strip down."
    $ scene_manager.strip_full_outfit(strip_feet = True)
    $ mc.change_locked_clarity(50)
    "You quickly check out the two girls before they start getting dressed..."
    $ the_person.apply_outfit(prost_outfit)
    $ the_researcher.apply_outfit(cop_outfit)
    $ scene_manager.update_scene()
    "You check out the two girls and their outfits. Your police officer uniform seems to fit perfectly."
    the_researcher "Wow, this looks just like a real uniform!"
    the_person "I umm... this is pretty umm..."
    the_researcher "Wow [the_person.fname]! You look so hot. Alan is gonna fall into this for sure!"
    the_person "Ahh, yah think so?"
    mc.name "Definitely. This is going to work."
    "You step out of the dressing room with the two girls. A couple is shopping nearby, and the guy notices you, then gives you a wink and thumbs up."
    "You walk over to the checkout counter."
    $ scene_manager.add_actor(starbuck, display_transform = character_left_flipped)
    starbuck "Oh! Those turned out so good!"
    mc.name "They really did. How much do we owe you for the outfits?"
    starbuck "They were about $100 each... OH one second, I almost forgot!"
    "[starbuck.possessive_title] quickly reaches down to a shelf behind the counter, then drops some handcuffs on the counter."
    starbuck "The cop suits came with these. They aren't real, so there is a quick escape button on the side!"
    mc.name "Thanks [starbuck.title]."
    $ mc.business.change_funds(-300)
    "You pay for the outfits before setting out from the sex shop."
    starbuck "Have fun everyone!"
    $ scene_manager.remove_actor(starbuck)
    "You step out into the mall with [the_person.title] and [the_researcher.possessive_title]."
    $ mc.change_location(mall)
    the_researcher "Alright, here's the earpiece. Me and [the_researcher.mc_title] will be listening to everything."
    mc.name "When you get back to his place, see if you can leave the front door unlocked so we can get in easier."
    the_researcher "I'm also recording, so try to get him to say something incriminating."
    mc.name "If you can get him to offer money for sex that would be a big one, obviously."
    the_person "Stars, I never thought I'd be a honeypot. This feels like one of those Jim Bond movies..."
    mc.name "[the_researcher.fname] and I will stay nearby and follow you to his place."
    the_researcher "Don't worry... you'll do great!"
    the_person "Alright... here goes..."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and walks way, off to meet with Alan for dinner."
    $ scene_manager.hide_actor(the_person)
    the_researcher "Here is a receiver, push this button to talk into it, otherwise it will just receive and record."
    mc.name "Alright, let's find somewhere discreet to be, before someone realizes we aren't really cops..."

    # TODO write rest of scene
    "This part is outlined. Have a scene with the head researcher in discreet while listening to Ellie have dinner."
    "Pick back up following Ellie to Alan's."

    $ mc.change_location(the_person.home)
    "You quietly slip into the contact's apartment with [the_researcher.title] while [the_person.possessive_title] is keeping him occupied."
    "The place is an absolute mess. Dishes are piled up on the small kitchen counter, and there are dirty clothes on the floor."
    "There are three doors, and one is closed with light coming out from underneath it. That must be the bedroom."
    "You take a quick peak into the next and discover a small office. Along one wall, is some heavy duty looking electronic equipment."
    "[the_researcher.title] follows you in, then whispers."
    the_researcher "Huh... I'm not sure what this stuff is..."
    "She takes one of the hard drives over and plugs it into a computer while you start to go through some of the notes."
    "You find something that looks like a journal... it appears to contain a short timeline."
    mc.name "Look here..."
    "At the beginning, it shows his initial contact with [the_researcher.possessive_title], and some notes on the program he wrote."
    "Then it has notes on how he noticed her insta getting more lewd?"
    "Next it notes... production equipment procured? What kind of production equipment?"
    "You show it to [the_researcher.title]."
    the_researcher "Huh... it is like he was stalking me... he makes notes about how my social media got increasingly sexual..."
    the_researcher "What kind of production equipment? Is that what this heavy duty stuff is?"
    "As you look through the office, you are reminded on the monitor that [the_person.title] is in the next room with him..."
    the_person "Mmm, remember the deal though, right? $100 and..."
    "Alan" "Yeah yeah... I was wondering about..."
    "For now, it seems he is still trying to talk her out of charging... you aren't sure if he is suspicious, or just cheap."
    the_researcher "Oh my god... I know what this is..."
    mc.name "What?"
    the_researcher "This is a production rig for the nanobots! He stole the equipment to make them himself!..."
    "She is excited, but is trying to keep her voice down."
    mc.name "Are you sure?"
    the_researcher "I'm positive. He was trying to recreate what we are doing? He even has some test notes.... oh my god..."
    mc.name "What is it?"
    the_researcher "The sick fuck... he was testing them on his SISTER."
    mc.name "Oh my god. What a sick fuck."
    the_researcher "I know... thankfully he had basically zero success. He didn't realize we were combining them with the suggestibility serums..."
    mc.name "Do you have copies of his research data?"
    the_researcher "Almost... it is still copying..."
    $ mc.change_location(the_person.bedroom)
    $ scene_manager.hide_actor(the_researcher)
    $ scene_manager.show_actor(the_person, position = "stand3")
    "Alan" "Okay, okay. $100 it is. I have the cash right here."
    the_person "Oh! That's... perfect... let me just count it real quick..."
    "Alan" "It's all there. Now get on your knees whore, I need this."
    $ ellie_ntr = False
    if persistent.show_ntr:
        "Oh no, it sounds like [the_person.title] is about out of time. You should probably step in now..."
        "Or should you? You need a few more minutes to finish copying the files... Should you stall a little longer? Or step in before [the_person.title] gets taken advantage of?"
        menu:
            "Step in right away":
                "You quietly push the button to talk to [the_person.title]."
                mc.name "Don't worry, we'll be there in a few seconds, help is on the way [the_person.title]."
                $ the_person.change_love(3, 80)
                $ the_person.change_happiness(5)
                $ mc.change_location(the_person.home)
                $ scene_manager.hide_actor(the_person)
                $ scene_manager.show_actor(the_researcher)
                "You look at [the_researcher.title]."
                mc.name "We need to get in there. Let these things keep copying... we might have to improvise a little."
                the_researcher "Ok, I'm sure we can still get the information we need..."
                mc.name "Get your handcuffs ready."
                the_researcher "They aren't real?"
                mc.name "Yeah, but HE doesn't know that."

            "Stall for a few more minutes" if persistent.show_ntr:
                $ ellie_ntr = True
                "You quietly push the button to talk to [the_person.title]."
                mc.name "We found some good stuff, but we need a few more minutes to copy files. You're doing great, do what you have to do, [the_person.title]."
                the_person "Oh stars..."
                $ the_person.change_obedience(2)
                $ the_person.change_love(-2)
                $ the_person.change_happiness(-10)
                "Alan" "Yeah, it IS big, ain't it?"
                the_person "Oh uhh, yeah. So big..."
                "Alan" "That's right. Now choke on it whore."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "Through the receiver, you listen as blowjob noises begin."
                "You can hear [the_person.title] lips smack and the soft sounds of sucking start coming through the received."
                "Alan" "Ohh, that's it. Swallow it all bitch."
                $ mc.change_location(the_person.home)
                $ scene_manager.hide_actor(the_person)
                $ scene_manager.show_actor(the_researcher)
                mc.name "Alright, she's buying us some extra time, let's make sure we get everything we need."
                the_researcher "Poor [the_person.fname]... she's taking one for the team, so to speak..."
                "You continue going through the research notes, while you hear the blowjob noises continue on the other side of the receiver..."
                the_person "Ulg.... ULGGG"
                "[the_person.possessive_title] gags a couple times, follow by some coughing."
                "Alan" "I guess you need more practice, whore. Take a breath. Now get back to work."
                "The sounds of gagging and slobbering continue."
                mc.name "Do you think we can get this production equipment out of here?"
                the_researcher "Umm... I mean we probably could, but he would probably hear it..."
                mc.name "Maybe it's time for us to intervene... We might have to freestyle a bit."
                mc.name "Get your handcuffs ready."
                the_researcher "They aren't real?"
                mc.name "Yeah, but HE doesn't know that."
                "Alan" "Oh fuck, that's it bitch! Get ready I'm going to cum all over that pouty little face of yours!"
                "You hear a loud pop in the receiver you assume is the contact pulling out of [the_person.title]'s mouth..."
                "Alan" "Fuck! OH FUCK YEAH!"
                $ cum_on_face_ntr(the_person)

            "Stall for a few more minutes (disabled)" if not persistent.show_ntr:
                pass
    else:
        "You didn't allow things to go this far so that another man could get sucked off by [ellie.possessive_title]. It's time to end this."
        "You quietly push the button to talk to [the_person.title]."
        mc.name "Don't worry, we'll be there in a few seconds, help is on the way [the_person.title]."
        $ the_person.change_love(3, 80)
        $ the_person.change_happiness(5)
        "You look at [the_researcher.title]."
        mc.name "We need to get in there. Let these things keep copying... we might have to improvise a little."
        the_researcher "Ok, I'm sure we can still get the information we need..."
        mc.name "Get your handcuffs ready."
        the_researcher "But they aren't real?"
        mc.name "Yeah, but HE doesn't know that."
    "You step out of the office and next to the bedroom door."
    "You count down from 3, then kick the door open as loudly as possible."
    $ mc.change_location(the_person.bedroom)
    $ scene_manager.show_actor(the_person, display_transform = character_left_flipped, position = "standing_doggy")
    mc.name "POLICE! Stop right there!!!"
    "[the_person.possessive_title] is bent over the contact, his cock in her hand."
    "Alan" "Wha... what!?!"
    mc.name "Deputy! Cuff him to the chair."
    the_researcher "Yes sir."
    $ scene_manager.update_actor(the_person, position = "sitting")
    "[the_person.title] sits on the floor as [the_researcher.possessive_title] walks over and grabs the contact and drag him to a nearby chair."
    $ scene_manager.update_actor(the_researcher, position = "standing_doggy")
    mc.name "Nice work, officer [the_person.fname], we got him paying for sex loud and clear on the wire."
    "Alan" "The wire? Wha... I didn't... you don't work for the cops..."
    "[the_researcher.title] has one hand cuffed down now... she's working on the other hand. Your distraction only has to work for a few more moments..."
    mc.name "Of course she does. Where else was she going to work after she got fired from her job after YOU SET HER UP?"
    "Alan" "Wha? Why I would never... you have no proof!... Wait..."
    "You hear the second set of handcuffs click into place."
    "Alan" "That's... [the_researcher.fname]? But... Oh shit."
    mc.name "That's right. Thank you [the_researcher.title]."
    $ scene_manager.update_actor(the_researcher, position = "stand3")
    the_researcher "My pleasure."
    "Alan" "That... that makes you..."
    mc.name "Yeah yeah. Thought you could ghost us, did you?"
    "Alan" "I..."
    mc.name "We found all kinds of equipment in your office. Oh, and evidence, too."
    mc.name "Your sister though? Really?"
    "Alan" "It isn't what you think!"
    mc.name "Isn't it? No matter. We'll be taking that with us. Along with the production equipment."
    "Alan" "Hey! You can't steal that!"
    mc.name "Can't we? Are you telling me you acquired it legitimately? What exactly are you going to do about it?"
    "The contact turns red in the face as he realizes just how much shit he is in. Stolen equipment, unethical research, you've got him by the balls."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "That's right! And making it look like I was the one who did it!"
    "Alan" "Ellie... it wasn't anything personal..."
    the_person "Nothing personal... stars... No Alan, when you go after a person's integrity, you MAKE it personal."
    the_person "If things were different, I would have you arrested for what you've done."
    the_person "But you are lucky... that I was able to find another job, doing work more exciting and cutting edge than anything I did before."
    "Alan" "You... you aren't going to release any of that data... are you?"
    mc.name "Maybe. Maybe not. We'll see. But secrets carry a price. Be ready for it."
    "The contact just looks down. You look at the two girls and motion for them to follow you out of the room."
    $ mc.change_location(the_person.home)
    "You leave him there, cuffed to a chair, going back to his office."
    if ellie_ntr:
        the_person "Let me just... wash up really quick..."
        $ scene_manager.hide_actor(the_person)
        $ the_person.apply_outfit(prost_outfit)
        $ scene_manager.update_scene()
    $ scene_manager.update_actor(the_researcher, position = "standing_doggy")
    "[the_researcher.possessive_title] checks the computer."
    the_researcher "Looks like the drives are done copying. We should have everything we need."
    "She unplugs the drives and collects them. You look at the production equipment."
    if ellie_ntr:
        $ scene_manager.show_actor(the_person, emotion = "happy")
        "Your [the_person.possessive_title] walks back in, with a smile."
    mc.name "Let's take this with us."
    the_person "If you ever get caught with it, there could be serious legal implications."
    mc.name "Then let's not get caught."
    "[the_person.possessive_title] helps you break down the equipment enough to move it. You put the pieces into your backpacks."
    $ scene_manager.update_actor(the_researcher, position = the_researcher.idle_pose)
    mc.name "Alright, let's get out of here."
    "You walk out of the contact's apartment. You can hear him yelling after you."
    "Alan" "Hey! You aren't... you can't leave me like this!?!"
    # TODO if you have beta male obedience serum for ashley, give the option to use it here.
    $ mc.change_location(downtown)
    "[the_person.title] chuckles as you step outside the apartment."
    mc.name "I'm sure he'll figure out those cuffs have an easy release button sooner or later..."
    $ mc.change_location(mc.business.r_div)
    "You and the two girls take your loot back to the research department. You start to unload your new equipment."
    the_researcher "We'll have to keep this somewhere secure."
    "You look at the nanobot production equipment."
    mc.name "Honestly, it looks like just about any other research equipment. I don't think anyone would know what it is unless they were looking for it specifically."
    mc.name "And if someone comes along looking for it... well I think we will already have other problems."
    the_person "True... I can probably get it set up... but it is going to take me some time I think."
    mc.name "Sounds good. You don't have to make it a high priority, we aren't going to run out of nanobots anytime soon, but it would still be useful to have running."
    mc.name "Good work today girls. We have all the blackmail material we need on the contact, if we ever need anything from him."
    the_person "If we just want to make him sweat a little."
    the_researcher "Or if we ever need a male test subject."
    $ scene_manager.remove_actor(the_researcher)
    "[the_researcher.possessive_title] unpacks, then says goodbye and leaves, but [the_person.title] sticks around..."
    the_person "Hey, before I go... I need to say something."
    mc.name "Sure."
    if ellie_ntr:
        the_person "I know it is important that we got all the stuff that we did but... I really wish you hadn't let things go so far with me and Alan."
        the_person "It was awful... the whole time I just kept telling myself... just pretend it's [the_person.mc_title]..."
        the_person "I don't know if I can ever do that again... please don't make me do that again, okay?"
    else:
        the_person "Thank you for stepping in when you did. I... I really thought I was going to have to suck that man's dick."
        the_person "I'm not sure I could have done it... I was freaking out so bad!"
        the_person "Please tell me you'll never make me do anything like that?"
    menu:
        "Be strict":
            mc.name "[the_person.title]... I can't make that promise. There may be times that I need you to accomplish things that might get messy."
            mc.name "But I want you to understand something. Just because I allow something like that to happen, doesn't make you any less mine."
            mc.name "Do you understand?"
            "[the_person.possessive_title] sighs."
            the_person "Yes sir."
            $ the_person.change_slut(3, 80)
        "Be Reassuring":
            mc.name "[the_person.title]... I appreciate you being flexible like that. But don't worry, I won't put you in that position again."
            the_person "Thank you! I really needed to hear that..."
            $ the_person.change_love(3, 80)
    $ the_person.change_obedience(5)
    "You give her ass a quick swat."
    mc.name "Now let's get going. We have a lot of work to do, but let's get some rest now."
    the_person "Yes [the_person.mc_title]!"
    python:
        mc.business.add_mandatory_crisis(ellie_submission)
        ellie.story_event_log("obedience")
        the_researcher = None
        cop_outfit = None
        prost_outfit = None
    return

label ellie_submission_label():   #Ellie submits herself to be used by MC
    $ the_person = ellie
    $ mc.change_location(lobby)
    "Closing time. You make your rounds through the business, making sure the lights are off and the rooms are empty."
    $ mc.change_location(mc.business.r_div)
    $ the_person.draw_person(position = "walking_away")
    "You enter the research department. You notice [the_person.possessive_title] standing at her desk, and barely hear her muttering to herself."
    the_person "I said work... there's no reason in on god's name that you shouldn't be working you piece of..."
    "You walk behind her and put your hands on her shoulders."
    $ the_person.draw_person(position = "back_peek")
    the_person "Stars! Oh hi [the_person.mc_title]."
    mc.name "Everything going okay over here?"
    the_person "Yes... but actually no. I'm trying to get this blasted nanobot tool to work, but the data protocols just don't seem to be working right!"
    mc.name "Sounds complicated."
    the_person "Everything about nanotech is complicated, and this certainly isn't my specialty."
    "She sighs."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.title] bends over and starts typing on her terminal... her ass pointing back, straight at you."
    "It makes an incredibly tantalizing target..."
    "*SLAP*"
    the_person "Aghhhnnnhhh!"
    $ the_person.change_arousal(3)
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] let's out a... did that turn into a moan?"
    $ mc.change_locked_clarity(10)
    the_person "[the_person.mc_title]!... Wha... what was that for...?"
    mc.name "All my employees know what happens when they bend over like that in front of me."
    the_person "Oh... is that so?..."
    "[the_person.title] bites her lip for a second. She looks around the room, realizing that you are alone together."
    $ the_person.draw_person(position = "standing_doggy")
    "Then bends over and returns to typing, her ass pointing back at you. A switch flips in your brain as you realize what is happening."
    "[the_person.possessive_title] is actively seeking your attention and approval now, of her work AND her body."
    "You decide it is time to see how she reacts if you rough things up a bit."
    "You put your hand on her hip and run it across her back, then down her ass, stopping to grope one of her cheeks."
    mc.name "Still working on the production equipment then? It sure does seem to be taking you a long time."
    "*SLAP*"
    the_person "Ahh!"
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    $ play_spank_sound()
    "You give her ass a hard spank, she gasps out a mixture of pleasure and pain."
    the_person "Sir? I..."
    "Her voice has a hint of fear in it."
    mc.name "Shhh... Let's just roleplay a little. I know you're working hard, but let's have a little fun with it."
    the_person "Ah... yes sir..."
    "You softly rub her ass where you just spanked a moment earlier. The you pull back and swing at the other cheek."
    $ play_spank_sound()
    "*SLAP*"
    the_person "Mmmf..."
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    mc.name "Yes, you've been slacking haven't you? Waiting for me to notice? Waiting for me to come over here and bend you over like the bad little girl you are?"
    the_person "Of course not! I don't..."
    $ play_spank_sound()
    "*SLAP*"
    $ mc.change_locked_clarity(10)
    $ the_person.change_arousal(5)
    the_person "Oh stars, yes sir! I've been hoping you would notice me..."
    mc.name "I know. Come here you little slut. I'm going to have to teach you a lesson."
    "You sit down in her chair, then grab her by the hips. You pull her onto your lap while she is still leaning over. You stick out one leg, bending her over your knee while she hangs onto the edge of the desk."
    $ the_person.draw_person(position = "doggy")
    if the_person.vagina_available:
        "You softly rub her bare ass, bent over your knee. There are couple red circles starting to form, one on each ass cheek."
    else:
        mc.name "Of course, if we are going to do this properly, we're going to have to get these out of the way..."
        "[the_person.possessive_title] ass shakes pleasantly as you pull her bottoms down..."
        $ the_person.strip_to_vagina(prefer_half_off = False, position = "doggy")
        "Once her ass is bare, you gently rub the two red circles starting to form, one on each cheek."
    $ play_spank_sound()
    $ play_spank_sound()
    "*SLAP*, *SLAP*"
    "You give each rosey cheek another spank. Her voice trembles with a moan."
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10)
    the_person "Ahhh, I'm sorry sir, I'll have the equipment working soon I..."
    $ play_spank_sound()
    "*SLAP*"
    $ play_moan_sound()
    the_person "AHH!"
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10)
    $ play_spank_sound()
    "You give her ass a harder spank this time."
    mc.name "Shhh, I didn't tell you to speak. I understand exactly what is going on, and right now, it is time to take your punishment without excuses."
    $ the_person.change_obedience(2)
    "You run your hand between her cheeks now, down and between her legs, along her slit."
    "Your attention is starting to get her wet. Having the busty red head bent over your knee is starting to get you really turned on too."
    $ mc.change_arousal(10)
    $ play_spank_sound()
    "You give her rosey cheeks another thorough round of spanking. She gasps or moans with each strike."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    $ play_moan_sound()
    the_person "Ahhh!"
    "You decide to give her a break from the spanking for a few moments. You run your fingers along her slit again, finding her to be even more aroused."
    $ play_moan_sound()
    "You push a finger inside her and she moans loudly. Her body shakes a little bit with your intrusion."
    the_person "Ohhh that feels so good... oh stars [the_person.mc_title]..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(20)
    $ mc.change_arousal(10)
    mc.name "You like it, don't you? Having my finger inside your needy cunt?"
    if ellie_has_given_virginity():
        "Note from the author. You have already had sex with [the_person.title]."
        "However, you can reset her virginity status now to experience this part of the story as if it were her first time."
        "Would you like to experience this event as if she is still a virgin?"
        menu:
            "Yes. Take her virginity (again)":
                $ restore_virginity(the_person)
            "No.":
                pass
    if ellie_has_given_virginity():
        mc.name "Don't worry. I'll replace it with my cock soon. Once your punishment is complete anyway."
        $ play_moan_sound()
        "You pull your finger out then give her ass cheeks another series of spanks. She is starting to wince with each one."
        $ mc.change_locked_clarity(50)
        $ the_person.change_arousal(20)
        $ mc.change_arousal(10)
        the_person "Stars... [the_person.mc_title]... please..."
        mc.name "Please what? I want you beg for what you want."
        the_person "Sir! Please... please fuck me now! I want you to fill me up again!"
        $ mc.change_locked_clarity(50)
        "The busty redhead is begging you to fuck her. It has been a long road to get her here, but having her beg you now, to put your cock inside her, makes it all worth it."
        mc.name "Mmm... okay slut. Bend over your desk and get ready for me."
        "You let her off your knee and she quickly bends over her desk, her ass still pointed at you."
        $ the_person.draw_person(position = "standing_doggy")
        "Her sorry little cheeks are red like her [the_person.hair_description]. You pull of your pants and get behind her, run your dick along her slit a few times."
        if the_person.is_bald:
            "You put one hand on her hip, and with the other you grab her shoulders. You line yourself up then push yourself deep inside her in one quick thrust."
        else:
            "You put one hand on her hip, and with the other you grab the back of her hair. You line yourself up then push yourself deep inside her in one quick thrust."
        the_person "Yes! Oh stars yes fuck me [the_person.mc_title]!"
        if the_person.is_bald:
            "You pull a little at her shoulders to remind her you are in control, but you begin to do exactly as she asks."
        else:
            "You pull her hair a bit to remind her you are in control, but you begin to do exactly as she asks."
        call fuck_person(the_person, private=True, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_fuck_person_ellie_obedience_60_02
    else:
        the_person "Yes, yes sir. It feels so good."
        "[the_person.title]'s hips move back and forth with your hand as you finger her. The busty redhead is putty in your hands now."
        "You decide it is time to take the next step, to gain carnal knowledge of the submissive minx."
        mc.name "[the_person.fname]..."
        "She pauses when she hears you use her first name."
        the_person "Y... yes?"
        mc.name "It's time."
        "You feel her body quiver for a second when she hears your words."
        the_person "For what...?"
        mc.name "Don't play coy. You know what it is time for."
        "You push a second finger into her incredibly tight little breeding hole."
        the_person "I know... I'm scared, [the_person.mc_title]..."
        mc.name "I know. But it'll be okay. You enjoyed your spanking, didn't you? This will be just as good."
        the_person "Are you sure?"
        mc.name "Yes. Now bend over my desk. I'm going to fuck you now."
        $ the_person.change_arousal(25)
        the_person "Oh stars... yes sir."
        "You let her off your knee, and she slowly bends over her desk for you."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "I'm ready sir... do whatever you want with me... I'm yours to do what you want with..."
        "Her soft words convey her total submission to you. It is time to take her virginity."
        "You stand up and take off your pants, ready for the deed. She seems ready for anything that is about to happen, but stop for a moment."
        "Should you wear a condom? You have no idea if she is on birth control..."
        menu:
            "Put on a condom":
                $ mc.condom = True
                mc.name "I'm going to put on a condom, that way I don't have to worry about pulling out."
                the_person "Okay, if that is what you want."
                "You reach over to your pants, grab your wallet and quickly pull out a condom. You quickly slide it on."
            "Go bareback":
                mc.name "I'm going to fuck you raw. If you want me to pull out, I can try, but I'm not going to promise I'll be able to."
                the_person "That's okay. I kind of want to know, what it feels like... to take your seed..."
                the_person "But if you want to pull out, you can do that too. Do what you want with me."
                "[the_person.possessive_title] blushes with the last of her words."
                $ the_person.increase_opinion_score("bareback sex")
                $ the_person.increase_opinion_score("creampies")
        "You step directly behind her. You run the length of your erection up and down her slit a few times. She is ready for you."
        mc.name "Alright. Here we go."
        "With your hands on both her hips, you slowly push your cock into her virin entrance. It yields slowly for a bit, then stops."
        "With one smooth motion, you pull her hips back with your hands and push forward, your cock pushing through her hymen, deep inside of her."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "standing_doggy")
        "Another small push, and you bottom out inside of her. You are finally balls deep inside of [the_person.possessive_title]."
        call fuck_person(the_person, private=True, start_position = standing_doggy, start_object = make_desk(), skip_intro = True, skip_condom = True, position_locked = True, condition = make_condition_taking_virginity()) from _call_fuck_person_ellie_obedience_60_01
        $ the_person.change_obedience(5)
    "When you finish with her, [the_person.title] slumps over her desk. Her well used ass is still bare and pointing back at you."
    $ the_person.draw_person(position = "standing_doggy")
    $ the_person.unlock_spanking()
    $ the_person.increase_opinion_score("being submissive")
    "You can now spank her whenever you please."
    mc.name "Fuck, you are a such a hot lay. I'm going to finish closing up, you should clean up and head home."
    the_person "Yes sir... I just need a moment."
    $ clear_scene()
    "You leave the research department to finish closing up your business. You swing back by research before you leave to verify she left."
    "[the_person.possessive_title] is getting more and more submissive. You feel like you are so close to breaking her completely to your will."
    "You should try to keep increasing her obedience and see what happens."
    $ ellie.event_triggers_dict["has_submit"] = True
    $ ellie.story_event_log("obedience")
    $ ellie.add_unique_on_room_enter_event(ellie_nanobot_fetish_testing)
    return

label ellie_nanobot_fetish_testing_label(the_person):   #MC has ellie test fetish impact of nanobots
    $ ellie.event_triggers_dict["fetish_avail"] = True
    $ ellie.story_event_log("obedience")
    return

label ellie_nanobot_fetish_label(the_person):   #After first test, MC can give ellie additional fetishes at will.
    pass
    $ ellie.story_event_log("obedience")
    return
