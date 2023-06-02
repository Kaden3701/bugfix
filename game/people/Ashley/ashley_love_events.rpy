
#Ashley Love Path
init 2 python:
    def ashley_after_hours_requirement():
        if mc.is_at_work and time_of_day == 3:
            if ashley.love >= 20 and ashley.story_event_ready("love"):
                return True
        return False

    def ashley_asks_about_lily_requirement():
        return mc.is_at_work and mc.business.is_open_for_business

    def ashley_lily_hangout_requirement():
        return time_of_day == 4

    def ashley_lily_shopping_selfies_requirement():
        return False
        if ashley.love >= 60 and ashley.story_event_ready("love"):
            if time_of_day != 0 and day%7 == 5: #Saturday
                return True
        return False

    def ashley_lily_shopping_aftermath_requirement():
        return time_of_day == 4

    def ashley_lily_truth_or_dare_requirement():
        if ashley.love >= 80 and ashley.story_event_ready("love"):
            if time_of_day == 4 and day%7 != 5 and day%7 != 6: #not weekend
                return True
        return False

    def ashley_steph_harem_entry_requirement():
        return False


    def add_ashley_afterhours_action():
        ashley_after_hours_action = Action("Ashley approach you", ashley_after_hours_requirement, "ashley_after_hours_label")
        mc.business.add_mandatory_crisis(ashley_after_hours_action)
        return

    def add_ashley_asks_about_lily_action():
        ashley_asks_about_lily = Action("Ashley asks about Lily", ashley_asks_about_lily_requirement, "ashley_asks_about_lily_label")
        mc.business.add_mandatory_crisis(ashley_asks_about_lily)
        ashley.progress.love_step = 2
        return

    def add_ashley_lily_hangout_action():
        ashley_lily_hangout = Action("Ashley and Lily makeup", ashley_lily_hangout_requirement, "ashley_lily_hangout_label")
        mc.business.add_mandatory_crisis(ashley_lily_hangout)
        return

    def add_ashley_lily_shopping_selfies_action():
        ashley_lily_shopping_selfies = Action("Ashley sends you pics", ashley_lily_shopping_selfies_requirement, "ashley_lily_shopping_selfies_label")
        mc.business.add_mandatory_crisis(ashley_lily_shopping_selfies)
        town_relationships.update_relationship(lily, ashley, "Friend")
        ashley.progress.love_step = 3

    def add_ashley_lily_shopping_aftermath_action():
        ashley_lily_shopping_aftermath = Action("Ashley sneaks into your room", ashley_lily_shopping_aftermath_requirement, "ashley_lily_shopping_aftermath_label")
        mc.business.add_mandatory_crisis(ashley_lily_shopping_aftermath)
        return

    def add_ashley_lily_truth_or_dare_action():
        ashley_lily_truth_or_dare = Action("Ashley and Lily Truth or Dare", ashley_lily_truth_or_dare_requirement, "ashley_lily_truth_or_dare_label")
        mc.business.add_mandatory_crisis(ashley_lily_truth_or_dare)
        return

    def add_ashley_steph_harem_entry_action():
        ashley_steph_harem_entry = Action("Ashley and Steph join your harem", ashley_steph_harem_entry_requirement, "ashley_steph_harem_entry_label")
        mc.business.add_mandatory_crisis(ashley_steph_harem_entry)
        town_relationships.update_relationship(lily, ashley, "Best Friend")
        return

label ashley_after_hours_label():   #Ashley looks for an opportunity to get MC alone, waits until after closing when Steph is for sure gone to approach him.
    $ scene_manager = Scene()
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "It is the end of the day, so you swing by your office to pick up your daily serum dose."
    $ mc.change_location(ceo_office)
    $ scene_manager.add_actor(the_person, emotion = "happy")
    "As you open the door, you see [the_person.possessive_title] standing there, waiting for you."
    mc.name "Ah, hello [the_person.title]."
    the_person "Hello [the_person.mc_title]."
    mc.name "Is there something you needed?"
    "She gives you a sly smile."
    the_person "Oh, I wouldn't say I necessarily NEED something."
    the_person "I guess... I was just thinking about how much of a favor you did for me, hiring me here."
    the_person "I know that things with Steph are a little bit... complicated."
    the_person "But I feel like I don't get to just... spend time with you very much."
    mc.name "Oh?"
    the_person "So umm, I was just wondering... can I walk you home?"
    mc.name "Oh. Umm, sure. I guess that would be alright."
    the_person "Great!"
    mc.name "Just give me a moment to finish up."
    the_person "Sure."
    "You finish closing up the business, then step out into the evening."
    $ mc.change_location(downtown)
    "As you start to make your way home, you chat a bit with [the_person.possessive_title]."
    the_person "So... I never really understood something. How DID you meet Steph, anyway?"
    mc.name "Well, the summer before my senior year, I got to do this internship at the university."
    mc.name "She was already a lab assistant, so we met while I was doing that."
    mc.name "That internship actually led to a LOT of what we are doing now."
    the_person "Huh... interesting."
    the_person "I think I remember her saying something about that, but I was pretty busy with my own thing at the time."
    "You walk a little more while [the_person.title] reflects on some things."
    the_person "Actually... I was umm... not the nicest person in university, if I'm being honest."
    the_person "I kind of ignored my sister a lot... And to be honest I kind of had a bit of a drinking problem."
    the_person "It umm... wasn't uncommon for me to wake up at a frat house with no idea how I got there. I had more than one girl get pissed at me for screwing around with their boyfriends..."
    the_person "I've never been one for exclusive relationships myself, but for some reason, I find guys who are in relationships with other girls to be very attractive."
    "You had a suspicion of such, with how [stephanie.title] warned you about her."
    the_person "I actually quit drinking this summer though! I got fired from my other job and I could feel things almost spiraling out of control."
    mc.name "That is an admirable thing, to feel yourself at the edge of the abyss and to pull yourself back. Not everyone manages to."
    the_person "Yeah... I suppose..."
    "You continue walking, eventually you get to your house."
    $ mc.change_location(her_hallway)
    "You step up into your front door."
    mc.name "Well, this is my house. I live here with my sister and my mother."
    the_person "Oh? I figured you for a bachelor type, out living alone."
    mc.name "Not yet. Maybe someday, but to be honest, I'm really hoping for the business to do well so I can take care of my family."
    $ the_person.change_love(3)
    the_person "That sounds very nice..."
    lily "I SAID FUCK OFF, ASSHOLE!"
    $ scene_manager.add_actor(lily, emotion = "angry", display_transform = character_left_flipped)
    "Suddenly, the front door swings open and a very angry [lily.title] appears."
    lily "I'M SO SICK OF... Oh."
    $ scene_manager.update_actor(lily, emotion = "happy")
    lily "Hey bro, I'm sorry, I thought... there was this guy at the mall being super creepy and who started following me home..."
    "[lily.title] smiles at you, then looks at [ashley.fname] and suddenly gets angry again."
    lily "I... hey, what the hell? What is SHE doing here?"
    $ scene_manager.add_actor(lily, emotion = "angry", display_transform = character_left_flipped)
    the_person "AGH, oh boy..."
    mc.name "What do you mean? [lily.fname], this is..."
    lily "[the_person.fname], yes, believe me, I'm familiar!!!"
    lily "Remember the boyfriend I had last year? And things were starting to get serious but I caught him cheating on me?"
    the_person "Well, it's probably a good time for me to go..."
    mc.name "[lily.title], she is an employee of mine."
    if lily.is_employee:
        mc.name "I'm surprised you haven't seen her around by now."
    mc.name "She was just walking me home. Thank you for that, [the_person.title], I appreciate it."
    the_person "Umm... right... I'm gonna go ahead and bail out now."
    "[lily.possessive_title] lets out an exasperated sigh and turns around, going up te stairs."
    $ scene_manager.remove_actor(lily)
    mc.name "Right. Well, I'll see you at work."
    the_person "Bye!"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "Suddenly, [the_person.title] puts her arms around you and gives you a hug, then plants a quick kiss on your cheek."
    "As quickly as it started, she backs away."
    $ scene_manager.update_actor(the_person,position = "walking_away")
    "[the_person.title] turns and starts to walk away. You watch her for a bit, admiring her figure, before go into the livingroom."
    $ scene_manager.clear_scene()
    $ mc.change_location(hall)
    "So it turns out, your sister and [the_person.possessive_title] already know each other... but definitely not in a good way."
    "If you want to get close to [the_person.title], you might have to work on repairing their relationship."
    $ add_ashley_asks_about_lily_action()
    return

label ashley_asks_about_lily_label():   #Ashley talks to MC about Lily and how she is doing. Expresses remorse for cheating issue. 40 love
    $ the_person = ashley
    "You are deep in thought as your work on some algorithms related to the latest set of research results. Suddenly, a throat clearing alerts you to someone standing next to you."
    $ the_person.draw_person()
    "It is [the_person.possessive_title]."
    mc.name "Ah, hello [the_person.title]."
    the_person "[the_person.mc_title]... have a sec?"
    mc.name "Sure."
    "She steps around the desk and sits down on the other side of it."
    $ the_person.draw_person(position = "sitting")
    the_person "So. I've been thinking about the other day, when I walked you back to your house, and then the thing... with your sister?"
    the_person "I feel really bad about it. I... was wondering if maybe we could like... try something."
    mc.name "Like what?"
    the_person "I really enjoyed just spending the time with you, walking back to your place... I was kind of hoping... maybe we could hang out at your place more often."
    the_person "It would be away from Steph, so she wouldn't know about it."
    the_person "But it won't work unless I get the chance to talk to your sister and apologize."
    mc.name "Yeah, having you come by once in a while would be problematic if she's pissed at you."
    "You think about it for a bit."
    mc.name "You know what she loves? Old comedy movies. And all the feel good vibes that go with them."
    mc.name "I'll text her and see if she wants to hang out sometime and watch one. You can come over and hang out with us, and I won't tell her you're coming."
    mc.name "It would be a good chance for you two to maybe make up a little."
    the_person "Yeah... I mean, I kind of have my doubts, but that might actually work."
    the_person "I think it'll help that you're her brother, and not her boyfriend!"
    #TODO after integration check lilys love path
    mc.name "Oh yeah, totally. Alright I'll text her. Tonight okay?"
    the_person "Yeah, should be..."
    "You pull out your phone and look up [lily.possessive_title]."
    $ mc.start_text_convo(lily)
    mc.name "Hey, what are you up to tonight?"
    lily "Hey bro! Not much, probably just studying for an exam I have next week."
    mc.name "Put it off. I want to watch Three Amigos tonight."
    "Several seconds go by."
    lily "Hey! You know I love that movie. Just come get me when you get ready to start it."
    mc.name "Will do."
    $ mc.end_text_convo()
    "You put your phone away."
    mc.name "Alright, we're on for tonight. Be there about 9, okay?"
    the_person "Okay. I'll be there."
    mc.name "I hope this plan of yours works..."
    the_person "Don't worry, I got this."
    $ clear_scene()
    "[the_person.possessive_title] turns and steps away, leaving you at your work station."
    "You are a little nervous about this plan, but maybe she can pull off redemption with your sister?"
    $ add_ashley_lily_hangout_action()
    return

label ashley_lily_hangout_label():
    $ the_person = ashley
    $ the_person.arousal = 20
    $ the_person.story_event_log("love")
    "It is late, and you have a date with [the_person.title] and your sister for a movie tonight. You get the TV ready when your phone goes off."
    $ mc.start_text_convo(the_person)
    the_person "Hey, I'm here. Let me in?"
    mc.name "OMW"
    $ mc.end_text_convo()
    "You step to the front door and open it."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    the_person "Hey. Ready to rock and roll?"
    mc.name "I guess. Make yourself comfortable in the living room, and I'll go get [lily.fname]."
    the_person "Okay."
    $ scene_manager.remove_actor(the_person)
    $ mc.change_location(lily.home)
    "You knock on [lily.possessive_title]'s door."
    $ scene_manager.add_actor(lily)
    mc.name "Hey, I'm starting the movie up."
    lily "Great! I could really use a break."
    mc.name "Hey, as a heads up, I have a friend over to watch it with us."
    lily "Oh? Who is it?"
    mc.name "You'll see..."
    $ mc.change_location(hall)
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "sitting")
    "[lily.title] stops when she walks into the living room."
    lily "... Seriously?"
    mc.name "Hey, she likes comedy movies too."
    the_person "Hey! Don't worry you won't even know I'm here. I love this movie!"
    $ scene_manager.update_actor(lily, emotion = "angry")
    lily "[lily.mc_title], are you kidding me!?!"
    mc.name "It's just a movie. Okay?"
    "[lily.possessive_title] gives you a long glare. For a moment, it seems she may turn around and walk back to her room, but eventually she relents."
    lily "You're lucky I love this movie."
    the_person "Me too!"
    lily "I wasn't talking to you."
    $ scene_manager.update_actor(lily, position = "sitting")
    "[lily.title] walks over and sits down in a chair across the room. You sit down next to [the_person.title]."
    "You give her a nervous smile, but she looks at you with unnerving determination."
    "You pick up the remote and start the movie. There is some definite tension as it starts."
    "Thankfully, the comedic stylings of Steve Martin, Chevy Chase, and Martin Short let some air into the room."
    $ scene_manager.update_actor(lily, emotion = "happy")
    "When it gets to the scene in the bar where the three amigos perform a musical number, [lily.title] is openly laughing."
    "Near the end of the musical scene, [the_person.title] quotes the bartender in time with the movie."
    the_person "My little buttercup!"
    "[lily.possessive_title] looks over and laughs. It definitely feels like some of the tension is leaving the room."
    "As you are watching the movie, you feel [the_person.title] take your hand. She guides your hand to her stomach and starts to slide your hand down her panties."
    "You glance over at [lily.possessive_title]. She seems to be unaware, so you let [the_person.title] guide your hand between her legs."
    "[the_person.possessive_title] shifts in her seat a little, hiding under the blanket, opening her legs up to give your fingers easy access."
    "She sighs when your finger slides between her labia. You can feel that she is already a little aroused as you slide your fingers along her slit."
    "Thankfully, her hand moves over into your lap as well. Through your pants you feel her start to stroke your rapidly hardening cock."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "You easily slide your middle finger into [the_person.title]'s vagina as you watch the movie together with [lily.possessive_title]."
    "[the_person.title] looks over at your sister, then you feel her unzip your pants. Her hand carefully reaches in, and after several seconds she manages to pull out your dick."
    "Her soft hand starts to stroke you, skin to skin. It feels pretty good as you continue to finger her."
    $ the_person.change_arousal(20)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "The movie keeps going, but you start to zone out. [the_person.possessive_title]'s soft hand stroking you is turning you on, and your sister being in the same room makes it even more exciting."
    "You push a second finger into [the_person.title]. With the angle of your hand, you are able to use the palm of your hand to put pressure on her clit while you stroke her g-spot."
    "She is starting to get a little bit restless in her seat, shifting back and forth. She stifles a moan, trying to keep quiet."
    "Double checking to make sure [lily.title] is still transfixed on the movie, she brings her hand up to her mouth and lets a large amount of saliva dribble out and onto her hand."
    "When she resumes stroking you, the extra lubrication makes her soft hand feel even better."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.possessive_title]'s hips are starting to move on their own. She is still stroking you with her hand, but her rhythm is off as she approaches climax."
    "You look over at her face. She bites her lip and closes her eyes as you push her over the edge."
    $ the_person.change_arousal(30)
    $ mc.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[the_person.title]'s body trembles slightly as she starts to cum. You stroke her g-spot relentlessly as her body clenches in orgasm."
    "Somehow, she manages to hold her breath and stifles any noises while she cums. After several seconds, you worry she might pass out."
    $ the_person.have_orgasm(half_arousal = False)
    "Eventually she starts to breathe again though, beginning with a large exhale."
    "Damn. Watching her orgasm like that has got you right on the edge. You move your hips, encouraging [the_person.title] to keep stroking and finish you off."
    "She gives you a half smile, then keeps stroking you."
    "The excitement of getting a handjob with your sister in the same room and watching [the_person.title] orgasm is too much."
    $ mc.change_arousal(30)
    $ mc.change_locked_clarity(30)
    "As you start to cum, [the_person.possessive_title] uses her hand to keep your cum contained and off the blanket."
    "You can feel yourself making a mess of her hand and your pants but you don't care."
    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = ashley)
    $ mc.reset_arousal()
    "You finish climaxing. Damn that felt good."
    $ scene_manager.update_actor(lily, position = "stand2")
    "Suddenly, [lily.title] jumps up. You startle, thinking she might have noticed what was going on."
    lily "I'm gonna make some popcorn."
    "[the_person.possessive_title] quickly wipes her hand on your shirt, thankfully hidden underneath the blanket."
    the_person "Oh! I could use a drink. I'll come too!"
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[lily.title] rolls her eyes for a second, then looks at you. She seems to notice something is off."
    lily "Hey, what's with the dopey look, [lily.mc_title]?"
    "[the_person.title] looks at you."
    the_person "Does he not usually look dopey like that? That's how he always looks, I think..."
    lily "Ha! Maybe so..."
    $ scene_manager.update_actor(lily, position = "walking_away")
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "The two girls turn and leave the living room to go get some snacks and drinks."
    $ scene_manager.clear_scene()
    "You are just considering making your escape to your room to clean up for a bit, when [mom.title] walks in."
    $ scene_manager.add_actor(mom)
    mom "Oh hey [mom.mc_title]. Watching a movie?"
    mc.name "Oh... yeah... with [lily.fname] and a friend..."
    mom "Oh! I love this one. That blanket looks comfy. Scoot over!"
    mc.name "Oh, umm my friend was actually sitting..."
    mom "There's plenty of seats in this house for her to sit in. Now scoot!"
    "You shift the end of the couch and lift up the blanket just enough for [mom.possessive_title] to sit down next to you."
    $ scene_manager.update_actor(mom, display_transform = character_left_flipped, position = "sitting")
    "Thankfully, she doesn't appear to notice your current state..."
    mom "Huh... this couch is smelling kind of musty. Maybe I should do some cleaning this weekend."
    mc.name "Yeah... good idea..."
    "[mom.title] settles into the couch, sitting right next to you as she watches the movie."
    "After a few minutes, you can hear two girls chatting as they re-enter the room, carrying snacks and drinks."
    $ scene_manager.add_actor(the_person, display_transform = character_center)
    $ scene_manager.add_actor(lily, display_transform = character_right)
    lily "Oh hey mom."
    "[the_person.title] stops when she sees your mother sitting next to you. She gives you a mischievous smile when she realizes what state you are in."
    mom "Ah! Hello there, you must be the friend that [mc.name] was telling me about..."
    the_person "Hi, I'm [the_person.fname]. It is an absolute PLEASURE to meet you!"
    $ scene_manager.update_actor(lily, position = "sitting")
    $ scene_manager.update_actor(the_person, position = "sitting")
    "The two girls sit down next to each other on the other end of the couch, sharing popcorn and watching the movie."
    "You sit there, your mother right next to you, your shirt and pants covered in cum. You manage to put your dick away at least without your family noticing..."
    "[lily.possessive_title] and [the_person.title] are chatting constantly now. You can't really hear what they are talking about, but you are glad they seem to be getting along."
    if mom.love > 40:
        "[mom.title] scoots over a bit closer to you now, putting her head on your shoulder."
        "Normally you would enjoy this sign of affection from her, but you are just one wrong move away from her finding out and that could lead to a really awkward situation..."
    "You settle in and just try and enjoy what is left of the movie. Thankfully, the movie ends and [mom.possessive_title] never discoveres the source of the odd smell."
    mom "Oh wow, what a fun movie! I need to get to bed though. Goodnight everyone!"
    $ scene_manager.update_actor(mom, position = "walking_away")
    "[mom.title] gets up and leaves the room. You are relieved."
    "[lily.possessive_title] and [the_person.title] are still chatting, seemingly unaware that the movie is over."
    $ scene_manager.remove_actor(mom)
    lily "No, it isn't like that. I just take pictures and upload them. I never meet with anyone."
    lily "The most annoying part is shopping for new outfits. It isn't like I can just call up my friends and be like... Hey! I need to shop for a new thirst trap outfit!"
    the_person "Why not? I mean, I would go. That sounds like a lot of fun actually."
    lily "Ha... I... I don't know. I guess I'm just not open like that with most of my friends."
    "There is a moment of silence. Then [the_person.title] speaks up."
    the_person "Look... I know we aren't like... close... but... why don't you take my number? Insta doesn't really sound like my thing, but shopping for outfits for it sounds like fun."
    "[lily.title] thinks about it for a moment."
    lily "Okay... I don't know... we'll see, okay?"
    "Your sister and [the_person.possessive_title] exchange numbers, and [lily.title] promises to think about it."
    "They might go shopping together? Sounds interesting for sure. You had no idea [the_person.title] was into shopping..."
    lily "Alright... I really need to get to bed."
    $ scene_manager.update_actor(lily, position = lily.idle_pose)
    "She stands up."
    if lily.sluttiness > 40:
        lily "And bro... you should really wash that blanket after this! Your cum is smelling up the whole living room!"
        "[the_person.title] about chokes on a bite of popcorn."
        the_person "Ha! Oh man, when I saw your mom had sat next to him, I almost died. So funny!"
        "Damn, [lily.title] must have known the whole time! At least she doesn't seem to be mad about it..."
    lily "Goodnight!"
    $ scene_manager.remove_actor(lily)
    $ scene_manager.update_actor(the_person, display_transform = character_left_flipped, position = "sitting")
    "[the_person.possessive_title] scoots over next to you."
    the_person "Well. THAT was hilarious!"
    mc.name "Speak for yourself!"
    the_person "I am!"
    mc.name "So... It seems like you managed to patch things up a bit with my sister..."
    the_person "Yep! I told you this would work."
    "She lays her head on your shoulder for a bit."
    mc.name "I... I still can't believe what we did... in my living room."
    the_person "Mmm, yeah. That was exciting."
    "She turns and looks you in the eye."
    the_person "You know, you really were a good sport about it. I'm just glad I was able to make you feel good."
    the_person "You deserve to have someone make you feel good once in a while like that."
    "She sighs."
    the_person "I mean... obviously Steph does... but it is nice for me to be able to..."
    mc.name "Yeah..."
    "Things with [the_person.possessive_title] sure are getting complicated. It is clear that she is starting to get feelings for you, but isn't ready to admit it yet."
    "After a little longer, she gets up."
    $ scene_manager.update_actor(ashley, position = lily.idle_pose)
    the_person "Well, I need to get going. Don't worry about me, I know the way home."
    the_person "Besides... you stink like cum. Go clean yourself up!"
    $ scene_manager.clear_scene()
    "You get up as [the_person.possessive_title] leaves."
    "Wow. What a night. The way that [the_person.title] is able to manipulate people... it is a little bit scary."
    "After one night, she appears to be well on the way to befriending your sister. You wonder... is it possible she used some kind of serum on her in the kitchen?"
    "You are glad they agreed to hang out and go shopping once in a while. Wait... maybe this is a bad idea... is [the_person.title] going to be a good influence on [lily.possessive_title]?"
    "You clean yourself up in the bathroom, then head to bed."
    $ add_ashley_lily_shopping_selfies_action()
    return

label ashley_lily_shopping_selfies_label(): #60
    $ the_person = ashley
    "In this label, Ashley starts sending MC some selfies of both her and Lily at the clothing store trying on outfits. Asks his opinion on a bunch."
    "At the end, sends one of both them in lingerie. Says Lily needs a special outfit for some kind of photo shoot."
    "Asks which girl looks better. Regardles of how MC answers, Ashley teases MC about it."
    $ add_ashley_lily_shopping_aftermath_action()
    return

label ashley_lily_shopping_aftermath_label():
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "MC goes to bed the same day after receiving the text messages from Ashley. As he is falling asleep, Ashley sneaks into his room."
    "Says she can't stay long, but strips down to the lingerie she sent selfie of earlier."
    "She teases MC, winds up riding him cowgirl before leaving."
    "Begins weekly Ashley and Lily teamup at the clothing store. If MC goes they let him rate their outfits. If MC doesn't, Ashley sends some pics of the highlights."
    $ add_ashley_lily_truth_or_dare_action()
    return

label ashley_lily_truth_or_dare_label():    #80
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "In this scene, MC comes home after work and Ashley and Lily are in the living room hanging out."
    "You wind up playing truth or dare. At some point Ashley selects truth and Lily asks her if shes in love with MC."
    "She tries to refuse to answer, but eventually she admits to being in love with him, but that things are complicated."
    "Lily apologizes for prying. Says you two should really try to work things out, she thinks you are perfect for each other."
    "Adds truth or dare as available for after shopping events."
    $ add_ashley_steph_harem_entry_action()
    return

label ashley_steph_harem_entry_label(): #100 Love AND requires both girls to be your girlfriend from bonus scenes.
    $ the_person = ashley
    $ the_person.story_event_log("love")
    "In this scene, you convince Stephanie AND Ashley to join your harem officially."
    return
