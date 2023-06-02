# This file contains the details of Myra's focus training scenes.
# This scene will be callable on demand via Myra's role.
# Starts off with basic back massage while she is playing games. Progression:
# Back rub > Grope > Sit on lap with fingering > Assjob > Anal
# Each scene progresses based on sluttiness AND on Myra's focus level.
# Focus has increased chance of increasing based on suggestability.
# If Myra is in trance, give MC a chance to raise Focus at the end of the scene if it is below MC's value for free.
#7/13



init 1 python:
    def myra_train_focus_requirement(the_person):
        if myra_at_cafe() and myra_can_train_focus():
            if myra_last_focus_train_day() + 1 < day:
                return True
            else:
                return "Trained focus too recently."
        return False

    def myra_focus_progression_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
        return True

    def myra_focus_progression_scene_1_req():    #Requirements for grope scene
        if myra.sluttiness > 20 and myra.focus >= 3:
            return True
        return False

    def myra_focus_progression_scene_2_req():    #Requirements for fingering
        if myra.sluttiness > 40 and myra.focus >= 4:
            return True
        return False

    def myra_focus_progression_scene_3_req():    #Requirements for assjob scene
        if myra.sluttiness > 60:
            return True
        return False

    def myra_focus_progression_scene_4_req():    #Requirements for anal
        return False
        if myra.sluttiness > 80 and myra_lewd_cafe_open():
            return True
        return False

    def myra_focus_progression_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        return True
        if the_person.location == gaming_cafe and myra_last_focus_train_day() < day:
            return True
        return False

    def myra_focus_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(10)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def myra_focus_progression_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["myra_focus_progression_scene_intro_0", "myra_focus_progression_scene_intro_1", "myra_focus_progression_scene_intro_2", "myra_focus_progression_scene_intro_3", "myra_focus_progression_scene_intro_4"]
        the_progression_scene.req_list = [myra_focus_progression_scene_0_req, myra_focus_progression_scene_1_req, myra_focus_progression_scene_2_req, myra_focus_progression_scene_3_req, myra_focus_progression_scene_4_req]
        the_progression_scene.trans_list = ["myra_focus_trans_scene_0", "myra_focus_trans_scene_1", "myra_focus_trans_scene_2", "myra_focus_trans_scene_3", "myra_focus_trans_scene_4"]
        the_progression_scene.final_scene_list = ["myra_focus_progression_scene_0", "myra_focus_progression_scene_1", "myra_focus_progression_scene_2", "myra_focus_progression_scene_3", "myra_focus_progression_scene_4"]
        # the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    myra_focus_progression_scene_action = Action("Train her Focus", myra_focus_progression_scene_action_req, "myra_focus_progression_scene_action_label")
    myra_train_focus = Action("Help Myra Train Focus", myra_train_focus_requirement, "myra_train_focus_label")

    def myra_focus_progression_scene_init():  #Run this during init only
        global myra_focus_progression_scene
        myra_focus_progression_scene = Progression_Scene(
            compile_scenes = myra_focus_progression_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "myra_focus_progression_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "myra_focus_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = myra_train_focus,      #The action used to call for this progression scene
            choice_scene = "myra_focus_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = False,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occurring crisis event
            unit_test_func = myra_focus_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        myra_focus_progression_scene.compile_scenes(myra_focus_progression_scene)   #This will populate the scenes that are blank above.


label myra_train_focus_label(the_person):   #Her standard corruption event. Slowly devolves from groping to anal. role action
    $ myra_focus_progression_scene.call_scene([the_person])
    return

label myra_focus_progression_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: myra_focus_progression_scene_action_label():

    call progression_scene_label(myra_focus_progression_scene, [the_person]) from _myra_focus_progression_scene_call_test_01  #[the_person] parameter should be a list of people in the scene itself, IE [mom], [mom,lily], [sarah,erica,mom], etc
    return

label myra_focus_progression_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person(emotion = "sad")
    $ myra.event_triggers_dict["can_train_focus"] = True
    the_person "Hey [the_person.mc_title]."
    mc.name "Hey. How are you doing?"
    "[the_person.possessive_title] sighs."
    the_person "Oh, not so good. I just can't get that tournament out of my head."
    the_person "I can't believe I choked! It was just the whole atmosphere of it. There was so much pressure... I felt like I couldn't focus!"
    mc.name "That is understandable. It was your first public tournament, right?"
    the_person "I know, I just feel like I let my whole team down."
    "You shrug your shoulders."
    mc.name "I'm sure that as you gain more experience, you'll learn to ignore the noise and focus on the game better."
    the_person "I know, I just wish there was some way to fast track that, you know?"
    the_person "I've tried putting on loud music or youtube, but it just isn't the same as having real human interaction."
    mc.name "Hmmm..."
    "You think about it for a minute."
    mc.name "What if I helped distract you?"
    the_person "Huh? What do you mean?"
    mc.name "I mean, I have nothing going on right now. You play some, and I'll sit beside you and watch and talk to you. Ask you questions. That sort of thing."
    mc.name "You'll have to divide your attention between the two. It will be good focus training for you."
    the_person "I don't know... I guess we could try and see though?"
    the_person "Let me just grab an energy drink. I'll meet you at the PC's over there."
    "[the_person.title] points to a group of PCs."
    $ clear_scene()
    "You head over and sit down."
    "Your job now is to distract [the_person.possessive_title] as she plays the game. You wonder if you can make conversation enough to distract her?"
    "You wonder if there is anything else you could do to distract her also."
    the_person "Alright, let's get this started."
    $ the_person.draw_person(position = "sitting")
    "[the_person.title] sits down at the desk, logs in and loads up the game."
    "Soon she is in a solo queue for some capture the point style pvp matches."
    "It's a 5v5 format with 3 king of the hill style points. Holding points and scoring kills grants your team points, and the first to 500 wins."
    "She starts playing and you watch as she starts out. She joins a team fight at the center point, fighting 4 on 4. She's doing great!"
    the_person "Hey, aren't you supposed to like... distract me or something?"
    mc.name "Right! So... umm.... did you hear about the new pirate movie?"
    the_person "I... are you telling me shitty jokes..."
    mc.name "Yes, it IS rated R!"
    "You drag out the letter, and she just rolls her eyes and keeps playing."
    "She easily pushes her team to control the center point, wiping the four enemy players in the process."
    the_person "This isn't working. Is that the best you can do?"
    "You desperately try to come up with something to talk about."
    mc.name "So, where do you and [alexia.fname] know each other from?"
    the_person "Ah, we used to live in the same neighborhood growing up. Our moms were friends and we used to hang out a lot, even though I was older than her."
    the_person "Sometimes I would even babysit... SHIT."
    "[the_person.title] pushed for the far point, but her team held back, and she now finds herself in a 2v1 on the far point."
    "Now is the time to push for answers and distract her."
    mc.name "That's neat. Do you two still hang out?"
    the_person "Hang out? I... I don't..."
    "[the_person.possessive_title] is trying to focus on the fight, but you keep pushing."
    mc.name "I mean, I know I see her around here on weekends, but do you two still get together?"
    the_person "Not really... I mean... we kinda went separate ways... I... YES!"
    "[the_person.possessive_title] manages to score a kill, then promptly disengages from the remaining enemy. They wasted valuable time defending their close point from her."
    mc.name "Why not? I mean, games are better played together, and if you got together to play I'm sure you would enjoy it."
    "[the_person.title] appears to be thoughtful about it as she moves to her next fight."
    the_person "You know, that's not a bad idea. She's a sweet girl, and it's not like having friends is such a bad thing."
    "[the_person.possessive_title] moves in to another group fight at the center point. Her team is getting beaten there badly, it looks like it is down to 3v2, and the two on her side are low on health."
    "[the_person.title] moves in to attack, when you notice her shoulders scrunching and she gets tense."
    mc.name "You get really tense when you play this game. Maybe it would be distracting if I tried helping you relax. May I?"
    the_person "I... I don't know what you have in mind, but go ahead..."
    "You stand up and move behind [the_person.possessive_title]. You put your hands on her shoulders and start to rub her back."
    the_person "Hey that's... ahhhh that feels nice..."
    "Her shoulders start to relax as your strong hands explore her shoulder blades. They seem very tense, so you use strong pressure to try and relax some of it away."
    mc.name "Damn, you are tense, girl! Let me try to work on some of this."
    the_person "That's... That is kind of distracting... wow..."
    "[the_person.title] tries to attack an enemy, but doesn't notice when another enemy joins the fight, making it 4v3."
    "Suddenly, the group stun locks her and easily spikes her down."
    the_person "Fuck! I can't play when you do that... its so..."
    mc.name "Distracting? Sounds like you just need to focus."
    the_person "Hmm... yeah you're right..."
    "You get to work on the tension in [the_person.possessive_title]'s neck and shoulders. A couple times when you find particularly tense muscles you hear a gasp as you massage them."
    $ the_person.change_slut(1, 40)
    $ the_person.change_happiness(2)
    $ the_person.change_love(1, 40)
    $ the_person.change_obedience(2)
    "You continue as [the_person.title] plays through a series of matches. Sometimes during particularly difficult fights, you feel her tense up, and you fight the tension away with your hands."
    "Overall, she does pretty good, but definitely not as dominating as she normally is. You feel like at the end of it she might have actually made some progress."
    "At the end of her last match, she logs off the game and stands up."
    $ the_person.draw_person()
    mc.name "So... have you thought about it?"
    the_person "You know, I think that might actually have worked..."
    mc.name "Yeah, but I mean about the other thing we talked about."
    the_person "What other thing?"
    mc.name "Why don't you invite [alexia.fname] to hang out sometime?"
    the_person "You know what? I'm going to. I'm going to call her right now."
    "[the_person.possessive_title] pulls out her phone. She dials her friend from her contacts."
    the_person "Hey girl! Yeah it's me. Hey, I was just wondering something..."
    the_person "Do you have any time free soon? I was thinking maybe we could get together. Maybe you could come out to the cafe and just hang out after I close up?"
    if day%7 == 4:
        the_person "Oh!... tonight? Yeah! That would be great! Yeah we could stay up late and play anything, that would be fun!"
        "Wow, so tonight [the_person.title] and [alexia.title] are going to get together..."
    else:
        the_person "Oh! Yeah I could do Friday night! We could stay up late and play anything! That would be fun!"
        "Hmm, so friday [the_person.title] and [alexia.title] are going to get together..."
    "Maybe you should swing by? Just to say hello?"
    the_person "Okay girl. Yeah I'll text you. Sounds good! Bye!"
    "[the_person.title] hangs up the phone then looks at you."
    the_person "You know what? I'm glad you swung by. Do you think, if you ever have some spare time, we could do more focus training?"
    the_person "I could pay you, if you need, I don't expect you to do it for free."
    the_person "You could be like my coach! Even though you don't play much yourself, you still have an idea of how it works and seem to have a knack for helping me improve."
    mc.name "I don't want to make any promises, but I think I can do that."
    the_person "Okay! Just swing by and let me know whenever you have time."
    "You say goodbye to [the_person.title] and head out."
    $ clear_scene()
    "Training [the_person.possessive_title]'s focus will be beneficial to her career in esports. You wonder if any of your serums could help out."
    "You bet that you could probably offer to get her an energy drink when you train her and dose it..."
    "Would increasing her suggestibility make it easier to train her focus? You imagine so."
    "You can now train [the_person.title]'s focus once per day."
    "[the_person.title] and [alexia.title] are getting together on Friday night. You make a note to swing by and see what they are up to..."
    $ myra.add_unique_on_room_enter_event(myra_alexia_teamup_scene_action)
    $ alexia.set_override_schedule(gaming_cafe, the_days = [4], the_times = [4])
    $ myra.set_override_schedule(gaming_cafe, the_days = [4], the_times = [4])
    call advance_time from _call_advance_myra_focus_progression_scene_adv_01
    return

label myra_focus_progression_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person()
    the_person "Hey, want to help me with my training today?"
    the_person "I really feel like we are making progress with my focus, but I know it takes up a big chunk of your time."
    return

label myra_focus_progression_scene_intro_1(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my training?"
    "[the_person.title] looks around the cafe. She spots an area near the back that is dark with no one around. She nods towards it."
    the_person "There's no one in the back corner... It felt really nice last time..."
    $ mc.change_locked_clarity(10)
    if the_person.tits_available:
        the_person "Plus I think you'll find that you'll have easy access to the girls..."
    return

label myra_focus_progression_scene_intro_2(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my training?"
    "[the_person.title] looks around the cafe. She spots an area near the back that is dark with no one around. She nods towards it."
    the_person "There's no one in the back corner... I'll sit on your lap again and... you know..."
    $ mc.change_locked_clarity(20)
    if the_person.vagina_available:
        "She lowers her voice to a whisper."
        the_person "Plus, I'm not wearing any panties..."
    return

label myra_focus_progression_scene_intro_3(the_group):
    $ the_person = the_group[0]
    the_person "Hey, want to help me with my *training*?"
    "The inflection in her voice shifts when she says training, making it clear she is really more interested in just having your cock against her bare ass..."
    "[the_person.title] looks towards the back of the cafe and nods towards it."
    the_person "I've started closing that section when I think you might swing by. We won't be disturbed if you want to..."
    $ mc.change_locked_clarity(30)
    return

label myra_focus_progression_scene_intro_4(the_group):
    $ the_person = the_group[0]
    the_person "Hey, is it time to fuck my ass again?"
    mc.name "Don't you mean focus training?"
    the_person "Of course! I mean, if I can win a game while your big dick is in my ass, nothing could possibly get in my way!"
    "[the_person.title] looks towards the back of the cafe and nods towards it."
    if myra_lewd_cafe_open():
        the_person "This is why I made the adult's only section. Come on, you know you want to!"
    else:
        the_person "The section in the back is closed. Come on... you know you want to!"
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title] is eager to drag you to the back of the gaming cafe and stuff her ass with your cock while she plays a game."
    return

label myra_focus_progression_scene_choice(the_group):
    $ the_person = the_group[0]
    $ the_person.draw_person()
    "Do you want to stick around and help [the_person.title] train her focus?"
    menu:
        "Training" if mc.energy >= 60:
            pass
        "Training\n{color=#ff0000}{size=18}Not enough Energy{/size}{/color} (disabled)" if mc.energy < 60:
            pass
        "Not right now":
            return False
    mc.name "Sure, I have time to do that. How about you go get logged in and I'll grab you an energy drink?"
    the_person "Okay! That sounds perfect. I'll see you over there."
    $ the_person.event_triggers_dict["focus_train_day"] = day
    $ clear_scene()
    call myra_focus_train_get_energy_drink(the_person) from _myra_energy_drink_focus_scene_01
    return True

label myra_focus_progression_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    mc.name "Unfortunately, I don't have time to do that right now."
    the_person "Ah, that is too bad."
    if myra_focus_progression_scene.get_stage() >= 2:
        the_person "The sessions have been so... productive... I've been looking forward to them more and more!"
    the_person "But anyway, was there something else you needed?"
    $ clear_scene()
    return



label myra_focus_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label myra_focus_trans_scene_1(the_group):  #Use event triggers to determine if this is from a transition or normal.
    $ the_person = the_group[0]
    "You walk over to the PC where [the_person.title] is sitting."
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard. She is just getting logged in."
    "You have made quiet a bit of progress with her. You feel like now is the time to push her boundaries some."
    mc.name "Hey, I think we need to change up your training some."
    the_person "Oh?"
    mc.name "I'm concerned that back rubs, while relaxing, aren't as distracting as a crowd of rowdy fans, cheering you on at a match."
    mc.name "We don't really have the ability to recreate that atmosphere, but we CAN push things with a massage that would be a little more distracting."
    "[the_person.title] bites her lip while she considers what you are saying."
    the_person "Okay... what did you have in mind?"
    mc.name "How about, instead of a just a back massage, what if it was a full, upper body massage?"
    the_person "Umm... you mean..."
    mc.name "I'll keep my hands above the waist, but the thrill of doing something a little naughty would definitely be more distracting."
    the_person "You... you just want to cop a feel of my tits, don't you?"
    mc.name "I mean, that is a definite perk, but I do feel like we would BOTH get something out of it this way."
    "[the_person.title] laughs."
    the_person "You know what? Fuck it. It's my cafe. But let's go back there..."
    "[the_person.possessive_title] points to the back corner."
    the_person "People don't go back there much, so even if we are in the cafe itself, it'll be less likely that we put a show on for anyone..."
    mc.name "Sounds good."
    $ the_person.draw_person("walking_away")
    "You follow [the_person.title] to the back corner of the cafe."
    $ the_person.draw_person(position = "sitting")
    "She sits down and gets logged in, taking a long sip from her energy drink."
    return

label myra_focus_trans_scene_2(the_group):
    $ the_person = the_group[0]
    "You walk over to the PC where [the_person.title] is sitting."
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard."
    "She has been getting more open to different experiences. You feel like it is time to push her boundaries a bit more."
    mc.name "Hey, I think we need to change up your training some more."
    the_person "Oh?"
    "She raises an eyebrow with a suspicious look."
    mc.name "I'm concerned that, even when I play with your tits, it still isn't as distracting as a rowdy crowd of esports fans."
    mc.name "I thought maybe we should push distractions to the next level."
    "[the_person.title] bites her lip while she considers what you are saying."
    the_person "What did you have in mind this time?"
    mc.name "How about, you sit on my lap, and while you are playing, I can touch you anywhere."
    the_person "I... anywhere?"
    mc.name "Anywhere."
    the_person "I... what if I like... you know..."
    mc.name "You'll just have to play through it. It'll be hard, I'm sure, but just think. If you can play through that..."
    the_person "Fuck, I don't know. I get what you are saying though..."
    "She seems right on the edge."
    mc.name "It just makes sense, right?"
    the_person "In a weird, perverted kind of way. Yeah. It makes sense."
    $ the_person.change_obedience(5)
    the_person "Fuck. You are going to get me in trouble one of these days, you know that? Let's try it."
    mc.name "Yeah! Let's start with your top off too."
    "[the_person.possessive_title] gives you a cold stare."
    mc.name "What? You've had your tits out before. Nobody ever looks back here, no one will notice."
    the_person "You're impossible. You know that right?"
    mc.name "No. I'm your COACH. And I just want what is best for you."
    "[the_person.title] laughs."
    the_person "I'm pretty sure coaches that do these kind of things with their athletes get prison time. But I'll play along, for now."
    $ the_person.strip_to_tits(position = "sitting")
    if the_person.has_large_tits:
        "[the_person.possessive_title] takes off her top. Her generous tits spill free, wobbling enticingly."
    else:
        "[the_person.possessive_title]'s perky tits drop as she takes her top off. They look firm and pleasing to the eye."

    "She takes a long sip from her energy drink as she gets logged in to the game. She smacks your hand when you try to pre-emptively cop a feel."
    return

label myra_focus_trans_scene_3(the_group):
    $ the_person = the_group[0]
    "You walk over to the PC where [the_person.title] is sitting. She is already topless."
    $ the_person.outfit.remove_all_upper_clothing()
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard."
    "You've been enjoying her training so far, but you feel like you could enjoy it even more. You decide it is time to try and push her further."
    mc.name "Hey, I think we need to change up your training some more."
    the_person "Oh?"
    "She raises an eyebrow with a suspicious look."
    mc.name "I'm concerned that no matter what I do, it just isn't as distracting as a crowd of people, cheering your name."
    mc.name "Then I realized the solution. If you can multi-task while you are playing, you can play during anything."

    "[the_person.title] rolls her eyes, but is listening to you so far."
    the_person "What did you have in mind this time?"
    mc.name "I want you to try giving me a lap dance while you play. Having to split your attention between two things will be a major challenge."
    "[the_person.possessive_title] just laughs."
    the_person "And let me guess. We should both be naked."
    mc.name "Of course. How distracting do you think a pair of trousers are?"
    "[the_person.title] shakes her head. At first, you think the jig is probably up, but then she surprises you."
    the_person "You know what? There's something about you. Ever since you showed up, things have progressed in ways I never would have imagined."
    $ the_person.change_obedience(10)
    the_person "If you think that will do the trick, let's give it a shot. I'm in."
    "You are surprised. You assumed you would have to do a lot more convincing. She gets up and takes off her bottoms."
    $ the_person.strip_full_outfit(position = "stand3")
    "You stare in aww at [the_person.possessive_title], standing naked in front of you."
    the_person "Well? You gonna stare all day? Or are you gonna sit down?"
    "You quickly sit down in the chair and pull your cock out. She sits on your lap."
    $ the_person.draw_person(position = "sitting")
    "She takes a long sip from her energy drink as she gets logged in to the game. She sighs and wiggles her hips a bit as you reach up and grope one of her tits."
    return

label myra_focus_trans_scene_4(the_group):
    $ the_person = the_group[0]
    $ the_person.strip_full_outfit(delay = 0)
    $ the_person.draw_person(position = "sitting")
    "You walk over to the PC where [the_person.title] is sitting. She is already naked."
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard."
    "You've finally pushed her to giving you lap dances while she plays games. You are thoroughly enjoying each and every training session."
    the_person "Hey coach, I got an idea."
    mc.name "Oh?"
    the_person "I've been thinking about it, you know, how I can take my focus to the next level."
    the_person "I think I know how to do it."
    mc.name "And how would that be?"
    the_person "I was thinking that, if I could win a match while you are fucking my ass, I think I could win a match no matter how many people are watching."
    if the_person.has_taboo("anal_sex"):
        "Wow. You were not expecting this."
        mc.name "I mean, it wouldn't necessarily have to be in your ass..."
        the_person "Yeah, but I think that would be more challenging..."
        the_person "Besides, I kind of like it that way..."
        "[the_person.title] gives you a wink."
        # TODO discover anal opinion?
    else:
        "Wow. You were not expecting this. She wants you to fuck her in the ass while she plays?"
        "You knew she liked it that way, but to have her suggest it is a huge win."
    mc.name "That does sound like a pretty incredible challenge. Are you sure you are up for it?"
    the_person "We won't know unless we try it, will we?"
    "Thankfully, as part of the expansion of the gaming cafe, in the adult only section you can do something like this without worrying about getting caught."
    the_person "And if I can't do it the first time, we'll just have to keep trying until I manage it!"
    "You aren't sure if she is trying to convince you, or herself, but you decide to jump on the opportunity before it passes you by."
    mc.name "Alright. If you think you are ready, let's give it a try."
    "[the_person.title] stands up."
    $ the_person.strip_full_outfit(position = "standing_doggy")
    "You stare in aww at [the_person.possessive_title]'s ass as she bends over the desk."
    the_person "Well? You gonna stare all day? Or are you gonna sit down?"
    "You quickly lose your clothes and sit down."
    "She takes a long sip from her energy drink as she gets logged in to the game, her ass still bare in front of your face. You give it a solid spank."
    return


label myra_focus_progression_scene_0(the_group, scene_transition = False):  #Innocent back massage
    $ the_person = the_group[0]
    $ myra_score = 0
    $ enemy_score = 0
    $ myra_wins = False
    "You walk over to the PC where [the_person.title] is sitting."
    $ the_person.draw_person(position = "sitting")
    "You set her energy drink down next to her keyboard. She is just getting logged in."
    the_person "Alright, ready to do this?"
    mc.name "I am. Start a match."
    "You set your hands on [the_person.possessive_title]'s shoulders as she loads into a match. There is a countdown and then the match begins."
    while myra_score < 100 and enemy_score < 100:
        $ score_str = "The score is " + str(myra_score) + " to " + str(enemy_score) + "."
        "[score_str]"
        call myra_focus_training_encounter(the_person) from _myra_focus_train_loop_01
        if _return:
            $ myra_score += renpy.random.randint(15,25)
            $ enemy_score += renpy.random.randint(0,10)
        else:
            $ myra_score += renpy.random.randint(1,10)
            $ enemy_score += renpy.random.randint(15,25)
    if myra_score > enemy_score:
        $ myra_wins = True
    if myra_wins:
        the_person "Yes! I won!"
        $ the_person.change_happiness(3)
    else:
        the_person "Wow, I lost?"
        $ the_person.change_obedience(3)
    $ the_person.draw_person()
    "[the_person.possessive_title] stands up and turns to you."
    if myra_wins:
        mc.name "I knew you could ignore the distractions and focus. Good job."
        the_person "Thanks!"
        if the_person.focus < 4:
            $ the_person.change_focus(1)
            the_person "I think... I really do feel like this has helped me train my focus better. You know?"
            mc.name "You're right. You are doing great."
        else:
            the_person "I don't know... I feel like I've almost gotten used to it, the way you rub my back, you know?"
            mc.name "Maybe we should try something that is a little more... distracting?"
            $ the_person.change_slut(1, 40)
            "[the_person.possessive_title] blushes a bit at your obvious innuendo."
            the_person "Ah... maybe..."
    else:
        the_person "Ugh, I suck at this. I don't think I'm ever going to get better."
        mc.name "Nonsense, you just need to stick with it."
        "You may have distracted her a bit too much. To help her make progress, you should probably try and make sure she wins the match."
        "Some of her problem is just a lack of confidence. Winning while you are rubbing her back might help some."
    the_person "I think I need a break... I really appreciate you helping me out with this though!"
    mc.name "Of course. I'll see you around."
    $ clear_scene()
    "Getting your hands on [the_person.possessive_title] is nice, but you can't help but feel like you could push things farther."
    $ the_person.apply_outfit(the_person.planned_outfit)
    if the_person.sluttiness < 20:
        "For now though, she is just too uptight. You should look for opportunities to loosen her up some."
    elif the_person.focus <= 2:
        "She clearly has trouble focusing right now. You should try and get her focus higher before you try and take things further with her."
    return

label myra_focus_progression_scene_1(the_group, scene_transition = False):  #groping
    $ the_person = the_group[0]
    $ myra_score = 0
    $ enemy_score = 0
    $ myra_wins = False
    if not scene_transition:
        "You walk over to the PC where [the_person.title] is sitting."
        $ the_person.draw_person(position = "sitting")
        "You set her energy drink down next to her keyboard. She is just getting logged in."
    the_person "Alright, ready to do this?"
    "[the_person.title] nervously looks around the room a little. She has picked a computer in the back corner, away from anyone else."
    mc.name "I am. Start a match."
    "You set your hands on [the_person.possessive_title]'s shoulders as she loads into a match. There is a countdown and then the match begins."
    while myra_score < 100 and enemy_score < 100:
        $ score_str = "The score is " + str(myra_score) + " to " + str(enemy_score) + "."
        "[score_str]"
        call myra_focus_training_encounter(the_person) from _myra_focus_train_loop_02
        if _return:
            $ myra_score += renpy.random.randint(15,25)
            $ enemy_score += renpy.random.randint(0,10)
        else:
            $ myra_score += renpy.random.randint(1,10)
            $ enemy_score += renpy.random.randint(15,25)
    if myra_score > enemy_score:
        $ myra_wins = True
    if myra_wins:
        the_person "Yes! I won!"
        $ the_person.change_happiness(3)
    else:
        the_person "Wow, I lost?"
        $ the_person.change_obedience(3)
    $ the_person.draw_person()
    "[the_person.possessive_title] stands up and turns to you."
    if myra_wins:
        mc.name "I knew you could ignore the distractions and focus. Good job."
        the_person "Thanks! Your hands ARE really distracting..."
        if the_person.focus < 5:
            $ the_person.change_focus(1)
            the_person "I think... I really do feel like this has helped me train my focus better. You know?"
            mc.name "You're right. You are doing great."
        else:
            the_person "I don't know... I feel like I've almost gotten used to it, the way you grab my tits, you know?"
            mc.name "Maybe we should try something that is a little more... distracting?"
            $ the_person.change_slut(1, 60)
            "[the_person.possessive_title] blushes a bit at your obvious innuendo."
            the_person "Ah... maybe..."
    else:
        the_person "Ugh, I suck at this. Are you sure grabbing my tits while I play is going to help me get better?"
        mc.name "Absolutely, you just need to stick with it."
        "You may have distracted her a bit too much. To help her make progress, you should probably try and make sure she wins the match."
    the_person "I think I need a break... I really appreciate you helping me out with this though!"
    mc.name "Of course. I'll see you around."
    $ clear_scene()
    $ the_person.apply_outfit(the_person.planned_outfit)
    "Getting your hands on [the_person.possessive_title]'s tits is great, but you can't help but feel like you could push things farther."
    if the_person.sluttiness < 40:
        "For now though, she is just too uptight. You should look for opportunities to loosen her up some."
    elif the_person.focus <= 3:
        "She clearly has trouble focusing right now. You should try and get her focus higher before you try and take things further with her."
    return

label myra_focus_progression_scene_2(the_group, scene_transition = False):  #sit on lap and fingering
    $ the_person = the_group[0]
    $ myra_score = 0
    $ enemy_score = 0
    $ myra_wins = False
    if not scene_transition:
        $ the_person.outfit.remove_all_upper_clothing()
        "You walk over to the PC where [the_person.title] is sitting."
        $ the_person.draw_person(position = "sitting")
        "You set her energy drink down next to her keyboard. She is just getting logged in and is already topless."
    the_person "Alright, ready to do this?"
    "[the_person.title] nervously looks around the room a little. She has picked a computer in the back corner, away from anyone else."
    mc.name "I am. let me sit down."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] gets up out her chair, leaving you just enough room to sit down. You give her ass a quick little spank before she can sit on your lap."
    the_person "Stop it fucker! I haven't even loaded in yet..."
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] sits down on your lap and loads into a match. The countdown timer starts, and soon the fight is beginning."
    while myra_score < 100 and enemy_score < 100:
        $ score_str = "The score is " + str(myra_score) + " to " + str(enemy_score) + "."
        "[score_str]"
        call myra_focus_training_encounter(the_person) from _myra_focus_train_loop_03
        if _return:
            $ myra_score += renpy.random.randint(15,25)
            $ enemy_score += renpy.random.randint(0,10)
        else:
            $ myra_score += renpy.random.randint(1,10)
            $ enemy_score += renpy.random.randint(15,25)
    if myra_score > enemy_score:
        $ myra_wins = True
    if myra_wins:
        the_person "Yes! I won!"
        $ the_person.change_happiness(3)
    else:
        the_person "Wow, I lost?"
        $ the_person.change_obedience(3)
    "[the_person.possessive_title] turns her head, but remains sitting on your lap."
    if myra_wins:
        mc.name "I knew you could ignore the distractions and focus. Good job."
        "When you say 'distractions', you give her tits one last squeeze."
        the_person "Mmm, that felt amazing."
        mc.name "Winning? or..."
        the_person "Yes to both."
        if the_person.focus < 6:
            $ the_person.change_focus(1)
            the_person "I think... I really do feel like this has helped me train my focus better. You know?"
            mc.name "You're right. You are getting better and better."
        else:
            the_person "I don't know... I feel like I've almost gotten used to it, the way you touch me, you know?"
            mc.name "Maybe we should try something that is a little more... distracting?"
            $ the_person.change_slut(1, 80)
            "[the_person.possessive_title] blushes a bit at your obvious innuendo."
            the_person "Ah... maybe..."
    else:
        the_person "To be honest... I don't even care that I lost. That felt amazing."
        mc.name "Yeah, but you need to focus better. You can have an orgasm, AND win a match. I'm sure of it!"
        "You may have distracted her a bit too much. To help her make progress, you should probably try and make sure she wins the match."
    if the_person.is_willing(blowjob):
        "[the_person.possessive_title] wiggles her hips a bit against your erection. She looks around the room."
        the_person "Hey... want a little help with that before we finish?"
        $ mc.change_locked_clarity(30)
        mc.name "Fuck yeah."
        the_person "Mmm, I know just what to do..."
        "[the_person.title] quietly slides down the chair, below the computer desk and gets on her knees."
        $ the_person.draw_person(position = "blowjob")
        "You pull out your dick and she doesn't waste any time, licking up and down the shaft."
        the_person "This is my way of saying thanks for the help."
        "[the_person.possessive_title] opens up her mouth and slides your cock into her hot mouth."
        call fuck_person(the_person, start_position = blowjob, skip_intro = True, position_locked = True, private = True) from _call_sex_description_myra_post_focus_bj_01
        "When you finish, you both quietly stand up."
    the_person "I think I need a break."
    mc.name "Of course. I'll see you around."
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    $ the_person.arousal = 20
    "Running your hands all over [the_person.possessive_title] is great, but you can't stop now. You have to push things further."
    if the_person.sluttiness < 60:
        "For now though, she is probably about at the limit of what she will do. You should use your serums to try and make her sluttier."
    elif the_person.focus <= 4:
        "She clearly has trouble focusing right now. You should try and get her focus higher before you try and take things further with her."
    return

label myra_focus_progression_scene_3(the_group, scene_transition = False):  #assjob / lap dance
    $ the_person = the_group[0]
    $ myra_score = 0
    $ enemy_score = 0
    $ myra_wins = False
    if not scene_transition:
        $ the_person.strip_full_outfit(delay = 0)
        "You walk over to the PC where [the_person.title] is sitting."
        $ the_person.draw_person(position = "sitting")
        "You set her energy drink down next to her keyboard. She is just getting logged in and is already naked."
        the_person "Alright, ready to do this?"
        "[the_person.title] looks around the room a little. She has picked a computer in the back corner, away from anyone else."
        mc.name "I am. let me sit down."
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title] gets up out of her chair, leaving you just enough room to sit down. You give her ass a quick little spank before she can sit on your lap."
        the_person "Mmm! Harder..."
        "You give [the_person.title]'s ass another spank. The sound echoes around the room. Her ass wobbles enticingly."
        $ mc.change_locked_clarity(30)
        "She sits down on your lap."
        $ the_person.draw_person(position = "sitting")
        "She takes a long sip from her energy drink as she gets logged in to the game. She sighs and wiggles her hips a bit as you reach up and grope one of her tits."
    "The countdown timer starts, and soon the fight is beginning."
    while myra_score < 100 and enemy_score < 100:
        $ score_str = "The score is " + str(myra_score) + " to " + str(enemy_score) + "."
        "[score_str]"
        call myra_focus_training_encounter(the_person) from _myra_focus_train_loop_04
        if _return:
            $ myra_score += renpy.random.randint(15,25)
            $ enemy_score += renpy.random.randint(0,10)
        else:
            $ myra_score += renpy.random.randint(1,10)
            $ enemy_score += renpy.random.randint(15,25)
    if myra_score > enemy_score:
        $ myra_wins = True
    if myra_wins:
        the_person "Yes! I won!"
        $ the_person.change_happiness(3)
    else:
        the_person "Wow, I lost?"
        $ the_person.change_obedience(3)
    "[the_person.possessive_title] turns her head, but remains sitting on your lap."
    if myra_wins:
        mc.name "I knew you could ignore the distractions and focus. Good job."
        "When you say 'distractions', you give her tits one last squeeze."
        the_person "Mmm, that felt amazing."
        mc.name "Winning? or..."
        the_person "Yes to both."
        if the_person.focus < 7:
            $ the_person.change_focus(1)
            the_person "I think... I really do feel like this has helped me train my focus better. You know?"
            mc.name "You're right. You are getting better and better."
        else:
            the_person "I don't know... I feel like I've almost gotten used to it, the way you touch me, you know?"
            "Her voice trails off a bit, but she doesn't present any alternative distraction means."
            $ the_person.change_slut(1, 90)
    else:
        the_person "To be honest... I don't even care that I lost. That felt amazing."
        mc.name "Yeah, but you need to focus better. You can have an orgasm, AND win a match. I'm sure of it!"
        "You may have distracted her a bit too much. To help her make progress, you should probably try and make sure she wins the match."

    the_person "I think I need a break."
    mc.name "Of course. I'll see you around."
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    $ the_person.arousal = 20
    "Having [the_person.possessive_title]'s ass cheeks wrapped around your cock is amazing. You wonder if she'll be willing to take the final step soon."
    if the_person.sluttiness < 80:
        "For now though, she is probably about at the limit of what she will do. You should use your serums to try and make her sluttier."
    elif the_person.focus <= 5:
        "She clearly has trouble focusing right now. You should try and get her focus higher before you try and take things further with her."
    return

label myra_focus_progression_scene_4(the_group, scene_transition = False):  #anal
    $ the_person = the_group[0]
    $ myra_score = 0
    $ enemy_score = 0
    $ myra_wins = False
    if not scene_transition:
        $ the_person.strip_full_outfit(delay = 0)
        "You walk back to the adult section and over to the PC where [the_person.title] is sitting."
        $ the_person.draw_person(position = "sitting")
        "You set her energy drink down next to her keyboard. She is just getting logged in and is already naked."
        the_person "Alright, ready to do this?"
        mc.name "I am. let me sit down."
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.possessive_title] gets up out of her chair, leaving you just enough room to sit down. You give her ass a quick little spank before she can sit on your lap."
        the_person "Mmm! Harder..."
        "You give [the_person.title]'s ass another spank. The sound echoes around the room. Her ass wobbles enticingly."
        $ mc.change_locked_clarity(30)
        "She takes a long sip from her energy drink as she gets logged in to the game. She sighs and wiggles her hips a bit as you continue to grope her rear."
    the_person "Ok... here we go..."
    $ the_person.draw_person(position = "sitting")
    "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
    "[the_person.possessive_title] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
    if scene_transition:
        $ the_person.break_taboo("anal_sex")
        the_person "Oh fuck... maybe I'm not ready for this..."
        mc.name "Too late now. Let's just give it a go and see what happens."
    else:
        the_person "Oh fuck... I keep forgetting how intense this is... I don't know if this is going to work..."
        mc.name "Too late now, the game is starting!"
    "The countdown timer starts, and soon the fight is beginning."
    while myra_score < 100 and enemy_score < 100:
        $ score_str = "The score is " + str(myra_score) + " to " + str(enemy_score) + "."
        "[score_str]"
        call myra_focus_training_encounter(the_person) from _myra_focus_train_loop_05
        if _return:
            $ myra_score += renpy.random.randint(15,25)
            $ enemy_score += renpy.random.randint(0,10)
        else:
            $ myra_score += renpy.random.randint(1,10)
            $ enemy_score += renpy.random.randint(15,25)
    if myra_score > enemy_score:
        $ myra_wins = True
    if myra_wins:
        the_person "Yes! I won!"
        $ the_person.change_happiness(3)
    else:
        the_person "Wow, I lost?"
        $ the_person.change_obedience(3)
    "[the_person.possessive_title] turns her head, but remains sitting on your lap."
    if myra_wins:
        mc.name "That was incredible."
        the_person "I know! That felt amazing."
        "She leaves it ambiguous whether she is talking about winning or your cock that is still deep in her ass..."
        if the_person.focus < 8:
            $ the_person.change_focus(1)
            the_person "I feel like I'm getting better and better. Thank you for your help."
            mc.name "Of course. It is an honor to be your coach."
        else:
            mc.name "I have to say... I don't think there is anything more I can teach you."
            mc.name "The fact that you can focus... through this..."
            "You give your hips a thrust as you say it."
            mc.name "I dare say your focus is near perfect."
            the_person "Maybe... I think I might need to keep training though, to keep sharp!"
            mc.name "Of course."
        if mc.arousal_perc > 50 or the_person.arousal_perc > 70:
            if the_person.arousal_perc > 70:
                "[the_person.title] slowly starts to move her hips again..."
                the_person "God... it still feels so good... can... can we go for just a little bit longer?"
            else:
                "You run your hands along her sides, making her shiver. Her ass twitches around your cock."
                the_person "Fuck... you are still so hard... do you want to go for just a little longer?"
            mc.name "Yeah, but stand up. I want to fuck your ass properly."
            the_person "Oh fuck..."
            $ the_person.draw_person(position = "standing_doggy")
            "You push the chair back as you stand up with [the_person.possessive_title], bending her over the computer desk."
            "Still inside of her, you grab her hips and start to fuck her ass some more."
            call fuck_person(the_person, start_position = anal_standing, start_object = make_desk(), skip_intro = True, skip_condom = True) from _call_sex_description_myra_anal_post_focus_train_01
    else:
        the_person "To be honest... I don't even care that I lost. That felt amazing."
        mc.name "Yeah, but I think you can do better."
        "You may have distracted her a bit too much, but for now, you are just happy you got to fuck her in the ass."
    $ the_person.draw_person()
    #TODO trance training
    "[the_person.title] slowly stands up, her legs a bit wobbly."
    the_person "I think I need a break."
    mc.name "Of course. I'll see you around."
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    $ the_person.arousal = 20
    "Having [the_person.possessive_title]'s ass bouncing up and down on your cock as she plays games is amazing."
    "You don't think you can take this any farther, but you look forward to your next training session."
    return



#Progression scene specific labels

label myra_focus_train_get_energy_drink(the_person):
    "You head to the refreshments and find an energy drink for [the_person.title]."
    "You look around... you could easily slip a serum into the drink before taking it back to her."
    call give_serum(the_person) from _call_give_myra_serum_focus_train_01
    if _return:
        "You slip the serum into her drink."
    else:
        "You decide not to add a serum to it."
    return

label myra_focus_training_encounter(the_person):
    $ encounter_num = renpy.random.randint(0,9) #In approximate degree of difficulty
    $ encounter_won = False
    $ base_difficulty = myra_focus_progression_scene.get_stage() * 15
    if encounter_num == 0:
        "[the_person.title] is pushing the middle. The other team seem distracted, presenting her team with a 2v4."
        "This should be an easy encounter for someone as skilled as [the_person.possessive_title]."
    elif encounter_num == 1:
        "[the_person.title] defends her home point with two teammates. The other team has sent 2 attackers, for a 2v3."
        "The two enemies are already injured, [the_person.possessive_title] should be able to handle this encounter, under normal circumstances anyway..."
    elif encounter_num == 2:
        "A 3v3 battle is occurring on the center point, which [the_person.title] quickly joins."
        "Her allies were struggling, but with [the_person.possessive_title] they should be able to turn the tide."
    elif encounter_num == 3:
        "[the_person.title] joins in during a 1v2 battle her home point, evening up the battle."
        "[the_person.possessive_title] looks at the map sees an ally also just resurrected, if she can hold off the two attackers for a bit, a teammate will be there soon to assist."
    elif encounter_num == 4:
        "[the_person.title] finds herself in a team battle at the center point. This appears to be an even 3v3 battle."
        "This should be a moderately challenging scenario for someone as skilled as [the_person.possessive_title]."
    elif encounter_num == 5:
        "[the_person.title] joins a team battle at the center point that is already in progress."
        "Her teammates have taken some damage, but with some skill and luck, [the_person.possessive_title] can turn the tide there."
    elif encounter_num == 6:
        "[the_person.title] pushes the far point, engaging one on one with an enemy player."
        "As she is about to strike down the enemy player, another enemy joins the battle, tipping the odds slightly against her."
    elif encounter_num == 7:
        "[the_person.title] is holding valiantly at the center point in a 2v2 battle, when an enemy player joins the attack."
        "It will take skill and precision from [the_person.possessive_title] to hold onto the point, outnumbered by the enemy team."
    elif encounter_num == 8:
        "[the_person.title] arrives at her home point just as a teammate there is defeated by two attackers."
        "This will be a difficult encounter, as [the_person.possessive_title] needs to hold out until her ally can resurrect and rejoin the fight."
    elif encounter_num == 9:
        "After her team splits between home and far, the enemy team looks to take the center point from [the_person.title]."
        "The odds are against her as she finds herself in a 3v1, she needs to survive long enough for teammates to clear their points and help."
    "As [the_person.title] engages, you consider her odds. How much do you want to distract her?"

    $ distraction_percentages = myra_calculate_success_percentages(the_person, encounter_num, base_difficulty)
    menu:
        "Light Distraction\n{color=ff0000}{size=18}[distraction_percentages[0]]%% Chance{/size}{/color}":
            call myra_focus_light_distraction(the_person) from _myra_focus_train_light_distr_01
        "Moderate Distraction\n{color=ff0000}{size=18}[distraction_percentages[1]]%% Chance{/size}{/color}":
            $ base_difficulty += 20
            call myra_focus_med_distraction(the_person) from _myra_focus_train_med_distr_01
        "Large Distraction\n{color=ff0000}{size=18}[distraction_percentages[2]]%% Chance{/size}{/color}":
            $ base_difficulty += 40
            call myra_focus_heavy_distraction(the_person) from _myra_focus_train_heavy_distr_01

    $ encounter_won = myra_calc_encounter_outcome(the_person, (encounter_num + 1) * 10, base_difficulty)
    if the_person.arousal_perc > 100:
        call myra_focus_training_orgasm(the_person) from _myra_focus_training_orgasms_03
        $ encounter_won = False
    if mc.arousal_perc > 100 and myra_focus_progression_scene.get_stage() >= 3:
        call myra_focus_training_mc_orgasm(the_person) from _myra_focus_train_mc_cums_01
        if myra_focus_progression_scene.get_stage() >= 3:
            $ encounter_won = True
    if encounter_won:
        #Wins encounter
        if encounter_num == 0:
            "[the_person.title] pushes through the distraction, easily cutting through the opponents, taking the center point and downing both enemies."
        elif encounter_num == 1:
            "[the_person.title] skillfully plays against the two attackers. When it becomes obvious they are about to fall, she teleports behind them."
            "When they turn to flee, she snares them both, allowing her teammates to cut them down."
        elif encounter_num == 2:
            "Despite the distraction, when a teammate gets downed, [the_person.title] quickly resurrects them and helps turn the tide."
            "Her team manages to down two enemies, while the third one stealths and retreats away."
        elif encounter_num == 3:
            "[the_person.title] manages the 2v2 fight despite your distractions. She has almost downed one enemy when her teammate joins."
            "Together, they snare the final enemy long enough to down them."
        elif encounter_num == 4:
            "While your distraction increases the challenge level, [the_person.title] pulls through."
            "Playing tactically, she holds back from a full onslaught until one of the enemy players pushes too far into her group."
            "When it happens, she pounces, downing the enemy player. After finishing them off, her team chases off the remaining two enemy players and secures the center point."
        elif encounter_num == 5:
            "[the_person.title] plays defensively, disrupting enemy attacks as they battle on the center point."
            "At one point, one of her teammates manages to snare one of the squishier enemy players. Despite your distraction, [the_person.possessive_title] notices and pounces on the enemy."
        elif encounter_num == 6:
            "[the_person.title] manages to finish off the downed enemy, and then fights the other enemy."
            "Despite your distractions, she manages to stall the far point for an extended period, until another enemy joins the defense."
            "Once outnumbered, she skillfully disengages and roams back toward the center of the map."
        elif encounter_num == 7:
            "[the_person.title] knows a long battle favors the enemy team while she is outnumbered, so she fights quickly through her distractions."
            "She gets snared by the team and gets focused. However, she quickly pops her stun break and drops her hardest hitting AoEs, significantly damaging all three attackers."
            "Her teammate capitalizes and downs one of the enemy players. [the_person.possessive_title] snares another attacker and finishes them off while the third one successfully retreats."
        elif encounter_num == 8:
            "[the_person.title] plays defensively while waiting for the teammate to come back. She skillfully dodges the enemy's hardest hitting attacks, watching for specific skill animations despite your distractions."
            "As her teammate gets back to the fight, she even manages to snare and damage an enemy as her teammate joins. They down one opponent and the other one retreats."
        elif encounter_num == 9:
            "Somehow, despite your distractions, [the_person.title] plays defensively and survives on the center point against three enemies."
            "For what seems like several minutes, she weaves between attacks, frustrating her attackers, until two of her teammates join her from her home point."
            "Once back on even footing, they push the attackers off the center point and down one."
    #Loses encounter
    else:
        if encounter_num == 0:
            "[the_person.title]'s mind is wandering from the fight and it shows."
            "Your distractions work as she doesn't even realize until it is too late that two attackers approached from behind, quickly downing her and two other teammates before capturing the center point."
        elif encounter_num == 1:
            "[the_person.title] plays recklessly as you distract her. Overconfidence catches up to her though, as she loses positioning and gets pushed off the map."
            "She sighs in frustration from the OHKO as she waits for the countdown time to respawn."
        elif encounter_num == 2:
            "[the_person.title] pushes to turn the tide at the center point, believing her team now outnumbers them."
            "However, due to your distractions, she doesn't see the enemy player that also enters late."
            "Not seeing the player until too late, she gets stunned by them and the enemy focuses her down, then kills off one other teammate as she gets ready to respawn."
        elif encounter_num == 3:
            "[the_person.title] tries to play for time, so her teammate can run back and help in the fight."
            "However, your distractions prove to be too much. She misses the tell for a heavy attack and gets downed, right as her ally returns to the fight."
        elif encounter_num == 4:
            "[the_person.title] can normally handle an even team fight like this. However, your distractions prove too much for her."
            "[the_person.possessive_title] makes several small mistakes, setting her team back with each one. Eventually, they are overcome by the enemy team and wipe."
        elif encounter_num == 5:
            "[the_person.title] fights to bring her team back, but your distractions make it impossible."
            "One by one, her teammates fall, until eventually [the_person.possessive_title] falls back, conceding the center point."
        elif encounter_num == 6:
            "[the_person.title] tries to finish off the enemy player, but gets stunned by the extra attacker before she is able to finish them."
            "The enemy manages to get their teammate back up, resulting in a 2v1. [the_person.possessive_title] tries to disengage, but gets snared and killed."
        elif encounter_num == 7:
            "[the_person.title] tries to play defensively while outnumbered at the center. However, because of your distractions, she misses it when one of the enemy player's stealths."
            "The enemy player un-stealths right next to her, knocking her down. Before she can react, the enemy team focuses and downs her, driving away her teammate."
        elif encounter_num == 8:
            "[the_person.title] plays defensively at her home point, but it is of little use."
            "Between your distractions and being outnumbered, the enemy team quickly downs her and takes the home point."
        elif encounter_num == 9:
            "[the_person.title] plays defensively on the center point, and for a while it seems she might actually pull through."
            "However, her focus falters, and eventually the enemy group manages a hard snare and KO, before her allies are able to join her."

    return encounter_won


label myra_focus_light_distraction(the_person):
    if myra_focus_progression_scene.get_stage() == 0:   #backrub
        "It seems like a good chance to go easy on [the_person.title], so you make lighter movement with your hands."
        "With light, easy strokes, using your fingertips, you rub the tensions out down her neck, shoulders, and arms."
    elif myra_focus_progression_scene.get_stage() == 1: #grope
        if the_person.arousal_perc < 30:
            "For now, you keep a light touch with [the_person.title]. You run your hands up and down her sides."
            "She shivers a bit from your touch, but otherwise continues to play undisturbed."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(10)
        else:
            "You run your fingers lightly across [the_person.title]'s sides."
            if the_person.tits_available:
                "Your hands run up along her belly to the underside of her tits, teasing them a bit, but otherwise leaving her mostly undisturbed."
                $ the_person.change_arousal(15)
            else:
                "Your hands run up her front. You trace a few circles around her tits through her clothes, but otherwise leaving her mostly undisturbed."
                $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(20)
    elif myra_focus_progression_scene.get_stage() == 2: #finger while on lap
        if the_person.arousal_perc < 30:
            "You run your hands along [the_person.title]'s soft skin on her sides. You let your hands travel up her body and play with her tits."
            "You don't want to be too much of a distraction, you just want to slowly build her arousal for now."
            if the_person.vagina_available:
                "With one hand still on her chest, you let the other slide down between her legs."
                "You run your fingers along her slit, being careful not to push your fingers inside her for now."
            else:
                "With one hand still on her chest, you slide the other down between her legs."
                "Your run your hand up and down her mound, touching her privates through her clothes."
            the_person "Mmm, that's nice..."
            "[the_person.possessive_title] murmurs. She wiggles her hips a bit against your groin as you touch her."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(20)
        elif the_person.arousal_perc < 70:
            "You can feel [the_person.title] leaning back against you some as she begins her next encounter. She is getting excited."
            "For now, you want to just keep building her arousal without pushing things too fast."
            if the_person.vagina_available:
                "You grope her chest with one hand, while the other goes between her legs."
                "You run your middle finger along her slit, then slowly push it inside of her. You give her cunt easy, slow strokes, trying not to distract her too much from her current fight."
            else:
                "You grope her chest with one hand, while the other goes between her legs."
                "Your push your fingers gently against her crotch, near the top of her slit, trying to stimulate her clit."
                "The mumbles something as you do your best to stimulate her gently through her clothes."
            the_person "That's it... mmm..."
            "[the_person.possessive_title] sighs. She is absent mindedly wiggling her hips against you now.."
            $ the_person.change_arousal(25)
            $ mc.change_locked_clarity(25)
        else:
            if not the_person.vagina_available:
                the_person "Fuck this is so hot... give me one second..."
                "Without even having to ask, [the_person.possessive_title] quickly strips out of her bottoms."
                $ the_person.strip_to_vagina()
            "[the_person.title] takes your hand and brings it down between her legs. She starts to eagerly grind against your hand now."
            the_person "That's it... oh [the_person.mc_title] I'm so close..."
            "[the_person.possessive_title] is whimpering, but still trying to concentrate on her fight. It seems impossible though, and it is clear that she is getting ready to cum!"
            $ the_person.change_arousal(35)
            $ mc.change_locked_clarity(30)
    elif myra_focus_progression_scene.get_stage() == 3: #assjob
        if mc.arousal_perc < 30:
            "For now, you are content to let [the_person.title] gently rock her hips against you as she plays."
            "You run your hands along her sides and up to her tits. She gives a soft moan when you play with her nipples."
            the_person "Mmm, that feels good..."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(20)
            $ mc.change_arousal(10)
        elif mc.arousal_perc < 80:
            "[the_person.title] continues her steady grinding motions as she gives you a lap dance while she plays."
            "The heat of her body against yours is really turning you on, but you don't want to distract her too much."
            "You run one hand between her legs, stroking along her slit a few times, while you grope her tits with the other."
            mc.name "God you are fucking hot. Keep working that ass girl..."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you."
            $ the_person.change_arousal(15)
            $ mc.change_locked_clarity(20)
            $ mc.change_arousal(10)
        else:
            "[the_person.title]'s ass feels so good as she grinds up against you. Your balls are starting to churn a bit with urgency."
            "You try not to distract her too much, but you slide a hand down between her legs."
            "You slip two fingers inside her easily. Her soft moans are like music to your ears as you finger her a bit."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(30)
            $ mc.change_arousal(10)
    elif myra_focus_progression_scene.get_stage() == 4: #anal
        if the_person.arousal_perc < 30:
            pass
        elif the_person.arousal_perc < 70:
            pass
        else:
            pass
    return

label myra_focus_med_distraction(the_person):
    if myra_focus_progression_scene.get_stage() == 0:   #backrub
        "[the_person.title] seems to be doing okay, so you decide to just give a normal back massage."
        "You use some force, without going too heavy with it, on her neck and shoulders, paying specific attention to tight feeling areas."
    elif myra_focus_progression_scene.get_stage() == 1: #grope
        if the_person.arousal_perc < 30:
            "You run your hands down along her sides, then back up her front, making sure to give her tits a gentle squeeze as your hands make large circles."
            "[the_person.title] gives a little sigh as you touch her body eagerly."
            $ the_person.change_arousal(15)
        else:
            if not the_person.tits_available:
                "Not content to touch her over her clothes, you quietly start to pull at her top."
                "[the_person.title] glances around to see if anyone is watching, but you feel safe in your secluded corner."
                $ the_person.strip_to_tits(position = "sitting")
                "Finally topless, you bring your hands up to her amazing tits."
            else:
                "You can tell that [the_person.title] is getting excited, so you push her focus, bringing your hands up to her amazing tits."
            if the_person.has_large_tits:
                "You grope [the_person.possessive_title]'s big tits in your hands. They feel so soft, and she moans when your fingers graze her nipples."
            else:
                "You grope [the_person.possessive_title]'s perky tits. They are small but soft in your hands, and she moans at every touch."
            "She yelps a bit when you pinch the nipples, wiggling a bit in her seat."
            $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
    elif myra_focus_progression_scene.get_stage() == 2: #finger while on lap
        if the_person.arousal_perc < 30:
            "While things are just getting started, you want to get [the_person.possessive_title] worked up to really push her focus."
            "You reach up with both hands and grab her tits. You give her nipples a little pinch."
            the_person "Mmm... easy now..."
            "Eventually, you drop your hand down between her legs."
            if the_person.vagina_available:
                "You run your middle finger along her slit several times. She is just started to get wet, so you take your time."
                "When you feel a bit of moisture starting to form around her entrance, you gently push your finger up inside of her."
                the_person "Ahhh... mmmm..."
                "As you finger her, [the_person.possessive_title] tries to focus on her encounter, but it is difficult."
                "As you move your finger slowly, her hips start to move with each thrust."
                $ the_person.change_arousal(30)
            else:
                "Although her bottoms are in your way, you use three fingers to gently massage her crotch."
                "You make slow circles, but use a decent amount of pressure. She sighs and enjoys your touch."
                "As you touch her, [the_person.possessive_title] tries to focus on her encounter, but it is difficult."
                $ the_person.change_arousal(25)

        elif the_person.arousal_perc < 70:
            if not the_person.vagina_available:
                "[the_person.possessive_title] is starting to get worked up. You decide the time is right to push a little harder."
                "However, to do that, you need easy access to her cunt. You reach down and start to pull off her bottoms."
                "[the_person.title] looks around briefly, but quickly submits and allows you to expose her privates."
                $ the_person.strip_to_vagina()
            "[the_person.possessive_title] is showing obvious signs of arousal as you continue to touch her."
            "You aren't trying to push her too hard, but you want to keep arousing her more and more to really test her focus."
            "With one hand you alternate, pinching a bit between each nipple, while with the other you push two fingers inside of her."
            the_person "Ah fuck... that feels so nice..."
            "[the_person.title] is trying to be quiet, but she is getting really into it. A couple times she falters, but she is really trying to concentrate on her match as you finger her."
            $ the_person.change_arousal(30)
        else:
            if not the_person.vagina_available:
                the_person "Fuck this is so hot... give me one second..."
                "Without even having to ask, [the_person.possessive_title] quickly strips out of her bottoms."
                $ the_person.strip_to_vagina()
            "You can tell that [the_person.title] is really getting into it. Her cunt is flooded with her juices and starting to run down the inside of her legs."
            "You pinch her nipple with one hand, and with the other you push your middle and ring fingers inside of her."
            "Using slow but deep strokes, you massage her g-spot with your fingers, while applying pressure to her clit with your palm."
            the_person "That's so good... oh god [the_person.mc_title]..."
            "She is desperately trying to concentrate on her match, but there is no way she doesn't cum soon."
            $ the_person.change_arousal(35)
        $ mc.change_locked_clarity(30)
    elif myra_focus_progression_scene.get_stage() == 3: #assjob
        if mc.arousal_perc < 30:
            "You put your hands on her hips as [the_person.title] grinds up against you, guiding her at the pace you want."
            "Her ass feels warm and soft as she gives you a lap dance while playing."
            "You don't want to make things too easy for her to focus, so you let go of her hips with one hand and reach up and grope her tits."
            the_person "Mmm, that feels good..."
            "[the_person.possessive_title] squeals a bit when you give it a pinch. She loses her focus for just a moment from the surprise."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(20)
            $ mc.change_arousal(10)
        elif mc.arousal_perc < 80:
            "[the_person.title] continues her steady grinding motions as she gives you a lap dance while she plays."
            "The heat of her body against yours is really turning you on. You can't help but run your hands all along her hot body."
            "You run one hand between her legs. You stick a finger inside of her to get it wet, then run it in circles around her clit a few times."
            the_person "Gah... fuck that feels good..."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(20)
            $ mc.change_arousal(15)
        else:
            "[the_person.title]'s ass feels so good as she grinds up against you. Your balls are starting to churn a bit with urgency."
            "You can tell you aren't going to last much longer, so you decide to make her feel good too."
            "You slip two fingers inside her easily. Her soft moans are like music to your ears as you finger her."
            mc.name "Damn you are so hot. If you keep going you are going to make me cum..."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you. If anything she picks up her pace a little..."
            $ the_person.change_arousal(20)
            $ mc.change_locked_clarity(40)
            $ mc.change_arousal(20)
    elif myra_focus_progression_scene.get_stage() == 4: #anal
        if the_person.arousal_perc < 30:
            pass
        elif the_person.arousal_perc < 70:
            pass
        else:
            pass
    return

label myra_focus_heavy_distraction(the_person):
    if myra_focus_progression_scene.get_stage() == 0:   #backrub
        "[the_person.title] asked you to test her focus, so you decide to oblige. Using firm strokes, you force her tense shoulders loose."
        the_person "Wow, that's intense..."
        "[the_person.possessive_title] is having trouble concentrating from the force of your touch."
    elif myra_focus_progression_scene.get_stage() == 1: #grope
        if not the_person.tits_available:
            "You really want to push [the_person.title]'s focus, but to do that, you need to get her top off. You start to strip her down."
            "[the_person.title] glances around to see if anyone is watching, but you feel safe in your secluded corner."
            $ the_person.strip_to_tits(position = "sitting")
            $ mc.change_locked_clarity(20)
        if the_person.arousal_perc < 30:
            "You bring your hands up her belly and to her tits. It's time to see if she has really made progress or not."
            "She protests a bit, but you shush her, as you pinch and pull at her nipples."
            "[the_person.possessive_title] just wiggles in her seat as you eagerly grope her body."
            $ the_person.change_arousal(20)
        else:
            if the_person.has_large_tits:
                "You bring your hands up to her generous tits. Her nipples are hard from the combination of your touching and her arousal."
                "[the_person.possessive_title] just moans when you pinch them and twist a little, the pleasure and the pain testing her focus to the utmost."
            else:
                "You bring your hands up to her perky tits. Her hard nipples are just begging to be played with."
                "[the_person.possessive_title] just moans when you pinch them, the pleasure mixed with pain testing her focus to the utmost."
            $ the_person.change_arousal(25)
        $ mc.change_locked_clarity(30)
    elif myra_focus_progression_scene.get_stage() == 2: #finger while on lap
        if the_person.arousal_perc < 70:
            if not the_person.vagina_available:
                "[the_person.possessive_title] needs focus training, so you are going to deliver."
                "However, to do that, you need easy access to her cunt. You reach down and start to pull off her bottoms."
                "[the_person.title] looks around briefly, but quickly submits and allows you to expose her privates."
                $ the_person.strip_to_vagina()
        else:
            if not the_person.vagina_available:
                the_person "Fuck this is so hot... give me one second..."
                "Without even having to ask, [the_person.possessive_title] quickly strips out of her bottoms."
                $ the_person.strip_to_vagina()
        if the_person.arousal_perc < 30:
            "[the_person.title] groans as you start to touch her with eager, rough hands."
            the_person "Hey take it easy..."
            "You ignore her request though. You grab her nipples and give them pretty rough twists, making her yelp."
            $ the_person.change_happiness(-1)
            $ the_person.change_obedience(2)
            "You drop one hand to her cunt. She is just starting to get excited, so she isn't very wet yet."
            "You bring your fingers up to her mouth, pushing two into her mouth after she opens up, getting them wet, then bring them back down between her legs."
            "You circle her cunt a few times, then slowly but firmly push them up inside of her."
            "[the_person.possessive_title] moans and arches her back at the intrusion. It is a mixture of pain and pleasure and is really testing her ability to concentrate."
            $ the_person.change_arousal(35)
        elif the_person.arousal_perc < 70:
            "[the_person.title] is starting to get turned on, so you decide to push her to her limit."
            "Pushing two fingers as deep as you can inside her, you start to fingerbang her earnestly."
            the_person "Oh fuck... do you have to be so rough?"
            $ the_person.change_happiness(-1)
            $ the_person.change_obedience(2)
            "[the_person.possessive_title] is really struggling with her match, as you finger fuck her relentlessly."
            $ the_person.change_arousal(35)
        else:
            "[the_person.possessive_title] is panting and moaning. You know there is no way she makes it through another encounter without cumming, so you push her to her limit."
            the_person "Oh fuck [the_person.mc_title], I'm... I'm gonna..."
            "You bang her relentlessly with your fingers, making obvious sexual noises to anyone who might be listening."
            the_person "That's so good... oh god [the_person.mc_title]..."
            "She is desperately trying to concentrate on her match, but there is no way she doesn't cum soon."
            $ the_person.change_arousal(45)
        $ mc.change_locked_clarity(30)
    elif myra_focus_progression_scene.get_stage() == 3: #assjob
        if mc.arousal_perc < 30:
            "You put your hands on her hips as [the_person.title] grinds up against you, guiding her at the pace you want."
            "You grind yourself against her as she wiggles against you. Her hot little body feels amazing as she gives you a lap dance."
            "You let yourself have your way with her body. You reach up with both her and grab tits with both hands, pinching and pulling at her nipples."
            the_person "Gah! Fuck take it easy..."
            mc.name "Not a chance, slut."
            "[the_person.possessive_title] squeals a bit when you give them another pinch. She loses her focus for just a moment from the sensations, but keeps playing."
            $ the_person.change_arousal(25)
            $ mc.change_locked_clarity(20)
            $ mc.change_arousal(15)
        elif mc.arousal_perc < 80:
            "[the_person.title] continues her steady grinding motions as she gives you a lap dance while she plays."
            "The heat of her body against yours is really turning you on. You grope her roughly as she moves."
            "You run one hand between her legs. Right as you stick two fingers inside of her, you lean forward and bite her shoulder."
            the_person "Ahh! Fuck..."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you. You finger her roughly as she moves against you."
            $ the_person.change_arousal(25)
            $ mc.change_locked_clarity(40)
            $ mc.change_arousal(20)
        else:
            "[the_person.title]'s ass feels so good as she grinds up against you. Your balls are starting to churn a bit with urgency."
            mc.name "Damn, you are going to make me cum. You want to make me cum?"
            the_person "Yeah! Please cum for me, [the_person.mc_title]!"
            "You slip two fingers inside her easily. She moans with you as you finger her roughly."
            "[the_person.possessive_title] just moans as she keeps playing, grinding her ass against you. She starts to pick up the pace as you finger her."
            $ the_person.change_arousal(30)
            $ mc.change_locked_clarity(50)
            $ mc.change_arousal(30)
    elif myra_focus_progression_scene.get_stage() == 4: #anal
        if the_person.arousal_perc < 30:
            pass
        elif the_person.arousal_perc < 70:
            pass
        else:
            pass
    return

label myra_focus_training_orgasm(the_person):
    if myra_focus_progression_scene.get_stage() <= 1:   #grope
        "[the_person.title] suddenly starts to shudder. She gasps and moans under her breath."
        "Is... is she cumming?"
        "She has stopped moving, and the other team is taking advantage of her."
        $ the_person.have_orgasm()
        $ mc.change_locked_clarity(50)
        "Wow, she definitely just orgasmed. Your hands really are magic?"
        "For several seconds, she rides her orgasm until she finally opens her eyes."
    elif myra_focus_progression_scene.get_stage() == 2: #finger while on lap
        "[the_person.title] is barely holding it together and has stopped playing as you finger her urgently."
        the_person "Oh god... oh... OH!"
        "Her pussy clenches down on your fingers as she begins to orgasm. She closes her eyes and her hips are bucking slightly."
        $ the_person.have_orgasm()
        $ the_person.arousal = 35
        $ mc.change_locked_clarity(50)
        "For several seconds, she rides her orgasm until she finally opens her eyes."
    elif myra_focus_progression_scene.get_stage() == 3: #assjob
        "You had no idea this was even possible, but something about your hands on her body and your cock against her ass has got [the_person.possessive_title] ready to cum."
        the_person "Fuck... Oh fuck!"
        "[the_person.title] is shuddering as an orgasm starts to run through her body."
        $ the_person.have_orgasm()
        $ the_person.arousal = 35
        $ mc.change_locked_clarity(50)
        "For several seconds, she rides her orgasm until she finally opens her eyes."
    elif myra_focus_progression_scene.get_stage() == 4: #anal
        $ mc.change_locked_clarity(50)
        if mc.arousal_perc > 100:    #dual orgasm
            "[the_person.possessive_title] is getting ready to cum, and you aren't far behind her."
            the_person "Fuck... Oh fuck!"
            "You whisper in her ear."
            mc.name "Get ready for it, I'm gonna cum too!"
            "[the_person.possessive_title] stops playing and rides you as you start to cum together."
            "As you start to shoot your load inside of her, she suddenly falls back against you, bottoming out on top of you as she orgasms also."
            the_person "Oh fuck! Fill my slutty ass with your cum [the_person.mc_title]!"
            $ the_person.have_orgasm()
            $ ClimaxController.manual_clarity_release(climax_type = "ass", the_person = the_person)
            $ the_person.cum_in_ass()
            $ the_person.draw_person(position = "sitting")
            "You pulse wave after wave of cum inside of her tight ass as she rides out her own orgasm."
            "When you are finished, she opens her eyes and looks at the encounter."
        else:
            "[the_person.possessive_title]'s having trouble staying on top of you, so you grab her hips and fuck her hard."
            if the_person.opinion_score_masturbating("masturbating") > 0:
                "She reaches down with one hand and pushes two fingers into her pussy."
            $ the_person.call_dialogue("climax_responses_anal")
            $ the_person.have_orgasm()
            "You bury your cock deep in [the_person.possessive_title]'s ass while she cums. Her bowel grips you tightly."
            "After a couple of seconds [the_person.possessive_title] sighs as she regains her senses."
            "She looks up and surveys the situation on her screen."
    return

label myra_focus_training_mc_orgasm(the_person):
    if myra_focus_progression_scene.get_stage() == 3:   #assjob
        "[the_person.possessive_title]'s hot ass grinding against your cock has got you ready burst."
        mc.name "God damn keep going, I'm about to cum."
        "[the_person.title] moves her hips up and down against you aggressively. You grab her hips as you start to cum."
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
        $ the_person.cum_on_ass()
        $ mc.reset_arousal()
        $ the_person.draw_person(position = "sitting")
        the_person "Oh my god it's so warm..."
        "[the_person.possessive_title] keeps playing, focusing on her encounter."
        "You take a minute to recover. While you do that, [the_person.title] is able to focus completely on her current encounter."
        mc.name "Get up for a second, let me see what a good little slut you are."
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.title] stands up, but bends over at the waist as she keeps playing, pointing her cum coated ass at you."
        $ mc.change_arousal(10)
        "You feel your erection returning as you check her out."
        mc.name "Alright, sit back down and keep going."
        $ the_person.draw_person(position = "sitting")
        $ the_person.change_obedience(2)
        "[the_person.title] is completely focused on her match, but obediently sits back down on your lap."
        "When she starts to move her hips a bit again, your cum acts as sticky lube, quickly bringing you back up to full hardness."
        $ mc.change_locked_clarity(50)
    elif myra_focus_progression_scene.get_stage() == 4: #anal
        "[the_person.possessive_title] tight ass has you ready to cum."
        mc.name "Get ready for it, I'm gonna cum!"
        "[the_person.possessive_title] keeps playing as she rides you to your orgasm."
        "Your grab her hips and pull her down as you start to shoot your load inside of her.."
        the_person "That's it, fill my slutty ass with your cum [the_person.mc_title]!"
        $ ClimaxController.manual_clarity_release(climax_type = "ass", the_person = the_person)
        $ the_person.cum_in_ass()
        "You pulse wave after wave of cum inside of her tight ass."
        $ mc.reset_arousal()
        $ the_person.draw_person(position = "sitting")
        the_person "Oh my god it's so warm..."
        "[the_person.possessive_title] keeps playing, focusing on her encounter."
        "You take a minute to recover. While you do that, [the_person.title] is able to focus completely on her current encounter."
        mc.name "Get up for a second, let me see what a good little slut you are."
        $ the_person.draw_person(position = "standing_doggy")
        "[the_person.title] stands up, but bends over at the waist as she keeps playing."
        "A small bit of cum is dripping down her crack and between legs, but most of it remains buried inside of her."
        $ play_spank_sound()
        "You give her ass a hard spank. It wobbles enticingly."
        $ mc.change_arousal(10)
        "You feel your erection returning as you check her out."
        mc.name "Alright, sit back down and keep going."
        $ the_person.draw_person(position = "sitting")
        $ the_person.change_obedience(2)
        "[the_person.title] is completely focused on her match, but obediently sits back down on your lap."
        "As your cock slips into her ass, your cum acts as sticky lube, quickly bringing you back up to full hardness."
        $ mc.change_locked_clarity(50)
    return

init 4 python:
    def myra_calculate_stat_and_difficulty(the_person, difficulty, dif_modifier = 0):
        encounter_dif = __builtin__.int(difficulty + dif_modifier + __builtin__.min(the_person.arousal, 100))
        skill_stat = __builtin__.int((the_person.focus + the_person.sex_skills["Foreplay"]) * 10) #Max 140, min 20

        #print("Skill stat: " + str(skill_stat) + " Difficulty: " + str(difficulty) + " Modifier: " + str(dif_modifier) + " Final Difficulty: " + str(encounter_dif))
        return (skill_stat, encounter_dif)

    def myra_calc_encounter_outcome(the_person, difficulty, dif_modifier = 0):
        (skill_stat, encounter_dif) = myra_calculate_stat_and_difficulty(the_person, difficulty, dif_modifier)
        if skill_stat > renpy.random.randint(0, encounter_dif):
            return True
        return False

    #Return odds for the purpose of creating a menu string
    def myra_calc_encounter_odds(the_person, difficulty, dif_modifier = 0):
        (skill_stat, encounter_dif) = myra_calculate_stat_and_difficulty(the_person, difficulty, dif_modifier)
        chance = __builtin__.int(((encounter_dif - skill_stat) * 1.0 / encounter_dif) * 100)

        if chance < 0:
            chance = 0
        return chance

    def myra_calculate_success_percentages(person, encounter, difficulty):
        return [myra_calc_encounter_odds(person, (encounter + 1) * 10, difficulty),
            myra_calc_encounter_odds(person, (encounter + 1) * 10, difficulty + 20),
            myra_calc_encounter_odds(person, (encounter + 1) * 10, difficulty + 40)]
