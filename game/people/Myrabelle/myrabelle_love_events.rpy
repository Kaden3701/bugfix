
init 2 python:
    def myra_esports_practice_requirement(the_person):
        if the_person.love >= 20 and gaming_cafe_is_open() and day%7 < 5 and myra.days_since_event("gaming_cafe_open_day") > TIER_2_TIME_DELAY:
            return True
        return False

    def myra_esports_first_tournament_requirement():
        if gaming_cafe_is_open() and day%7 == 6 and myra.love >= 40:
            return True
        return False

    def myra_train_focus_intro_requirement(the_person):
        if gaming_cafe_is_open() and myra.days_since_event("myra_fails_tournament") > TIER_1_TIME_DELAY and myra_at_cafe():
            return True
        return False

    def myra_loses_sponsor_requirement(the_person):
        if the_person.love >= 60 and gaming_cafe_is_open() and myra_at_cafe() and time_of_day == 3 and myra.days_since_event("myra_fails_tournament") > TIER_3_TIME_DELAY:
            return True
        return False

    def myra_gains_sponsor_requirement(the_person):
        if myra_at_cafe() and time_of_day < 3 and mc.business.has_funds(25000):
            return True
        return False

    def myra_esports_second_tournament_intro_requirement(the_person):
        if the_person.love >= 80 and mc.business.days_since_event("energy_drink_start_research") > TIER_2_TIME_DELAY:
            if myra_focus_progression_scene.get_stage() >= 2 and gaming_cafe_is_open() and myra_at_cafe() and day%7 < 4:
                return True
        return False

    def myra_esports_second_tournament_requirement():
        if gaming_cafe_is_open() and day%7 == 6:
            return True
        return False

    def myra_gaming_cafe_expansion_intro_requirement(the_person):
        if the_person.love >= 95 and myra.days_since_event("myra_tourn_win_day") > TIER_2_TIME_DELAY:
            if gaming_cafe_is_open() and myra_at_cafe() and day%7 != 6:
                return True
        return False

    def add_myra_esports_practice_action():
        myra_esports_practice = Action("Myra's Esports Aspirations", myra_esports_practice_requirement, "myra_esports_practice_label")
        myra.add_unique_on_room_enter_event(myra_esports_practice)
        mc.event_triggers_dict["guild_quest_level"] = 6
        mc.event_triggers_dict["guild_quest_name"] = "Bud Lightyear"
        mc.event_triggers_dict["gaming_cafe_grind_day"] = day
        myra.set_event_day("gaming_cafe_open_day")
        return

    def add_myra_esports_first_tournament_action():
        myra_esports_first_tournament = Action("Esports Tournament", myra_esports_first_tournament_requirement, "myra_esports_first_tournament_label")
        gaming_cafe.on_room_enter_event_list.append(myra_esports_first_tournament)
        myra.event_triggers_dict["knows_plays_esports"] = True
        add_myra_distracted_gaming_action()
        return

    def add_myra_train_focus_intro_action():
        myra_train_focus_intro = Action("Myra needs help", myra_train_focus_intro_requirement, "myra_train_focus_intro_label")
        myra.add_unique_on_room_enter_event(myra_train_focus_intro)
        myra.event_triggers_dict["has_failed_tournament"] = True
        myra.set_event_day("myra_fails_tournament")
        return

    def add_myra_train_focus_action():
        myra.get_role_reference("myrabelle").add_action(myra_train_focus)
        myra.event_triggers_dict["can_train_focus"] = True
        myra.event_triggers_dict["focus_train_day"] = day
        return

    def add_myra_loses_sponsor_action():
        myra_loses_sponsor = Action("Myra Loses a Sponsor", myra_loses_sponsor_requirement, "myra_loses_sponsor_label")
        myra.add_unique_on_room_enter_event(myra_loses_sponsor)
        return

    def add_myra_gains_sponsor_action():
        myra_gains_sponsor = Action("Myra Gains a Sponsor", myra_gains_sponsor_requirement, "myra_gains_sponsor_label")
        myra.add_unique_on_room_enter_event(myra_gains_sponsor)
        myra.event_triggers_dict["bar_arcade_avail"] = True
        myra.event_triggers_dict["can_sponsor"] = True
        return

    def add_myra_esports_second_tournament_intro_action():
        myra_esports_second_tournament_intro = Action("Myra Sets Up New Tournament", myra_esports_second_tournament_intro_requirement, "myra_esports_second_tournament_intro_label")
        myra.add_unique_on_room_enter_event(myra_esports_second_tournament_intro)
        myra.event_triggers_dict["has_been_sponsored"] = True
        myra.set_event_day("myra_sponsor_day")
        return

    def add_myra_esports_second_tournament_action():
        myra_esports_second_tournament = Action("Myra's Redemption", myra_esports_second_tournament_requirement, "myra_esports_second_tournament_label")
        mc.business.add_mandatory_crisis(myra_esports_second_tournament)
        return

    def add_myra_gaming_cafe_expansion_intro():
        myra_gaming_cafe_expansion_intro = Action("Myra Wants to Expand", myra_gaming_cafe_expansion_intro_requirement, "myra_gaming_cafe_expansion_intro_label")
        myra.add_unique_on_room_enter_event(myra_gaming_cafe_expansion_intro)
        myra.event_triggers_dict["has_won_tournement"] = True
        myra.set_event_day("myra_tourn_win_day")
        return

label myra_esports_practice_label(the_person):  #20 love event, on room enter event on myra
    "You step into the gaming cafe. As you start to walk over to the main counter, however, you realize that there isn't anyone there."
    "You wonder where [the_person.possessive_title] might be? You scan the room."
    "Near one side, you see a small group of about 8 people watching a computer. You can't tell who is playing, so you walk over."
    "When you get there, you see [the_person.title] playing."
    $ the_person.draw_person(position = "sitting")
    "She appears to be in a pretty tight match. You ask one of the other people watching."
    mc.name "Hey, why is everyone watching her play?"
    "?????" "She's at the end of a tournament. If her team wins, they automatically qualify for the esports tournament Battle of the Bay."
    "Ahhh, so it is like a qualifying round."
    "You watch as she plays. [the_person.possessive_title] is manhandling her competition."
    "In a climactic battle, she manages to stall two attackers at home point while her team finishes off the other team at mid, securing the victory."
    the_person "Yes! We did it!"
    $ the_person.draw_person()
    "[the_person.title] jumps to her feet. All the people watching her cheer and start to give each other high fives."
    "?????" "Way to go!"
    "?????" "Nice going!"
    "The small group congratulate her on the win. Eventually she gets to you."
    the_person "Oh hey [the_person.mc_title]! Did you see?"
    mc.name "I did! Congratulations! When is the tournament?"
    the_person "I'm actually not sure. I know it is usually on a Sunday, but I'm not sure how close it is."
    mc.name "Neat. I can't wait to watch!"
    the_person "Yeah! I'll have to set up something for it. It is an online thing, so I'll be able to play from the cafe here. Maybe I could put it up on the main projection screen."
    mc.name "That is an excellent idea."
    the_person "Thanks! Oh my god, I gotta go text [alexia.fname], she is going to be so excited. I'll see you around, okay?"
    mc.name "Sounds good."
    $ add_myra_esports_first_tournament_action()
    $ the_person.draw_person(position = "walking_away")
    "Wow, so [the_person.possessive_title]'s esports team has managed to qualify for a big tournament! You'll have to see if you can attend."
    return

label myra_esports_first_tournament_label():    #Mandatory event. Preluded to during the first love event
    $ the_person = myra
    "You feel your phone go off when you get a notification. It's a message from [alexia.possessive_title]"
    $ mc.start_text_convo(alexia)
    alexia "Hey! I don't know what you are doing right now, but get over to the gaming cafe!"
    alexia "[the_person.fname] is hosting a watch party for her esports tournament! She asked me to text you because she doesn't have your number I guess."
    alexia "It's going to start soon!"
    mc.name "Thanks! I'm on my way. Save me a seat?"
    alexia "Sure!"
    $ mc.end_text_convo()

    "Alright, this should be interesting. You head over to the gaming cafe."
    $ mc.change_location(gaming_cafe)
    $ scene_manager = Scene()
    "When you get there, you look around. A bunch of seats have been set up to watch a projector screen. There is actually a fairly large crowd here... you estimate about 100 people."
    "You look around. Eventually you spot [alexia.title] with an open seat next to her. You walk over and sit next to her."
    $ scene_manager.add_actor(alexia, position = "sitting", display_transform = character_right)
    mc.name "Hey! Thanks for saving me a seat."
    alexia "Hey [alexia.mc_title]! I had to shoo away several cute guys, so I hope you can manage to keep me good company for this!"
    if alexia.is_single:
        mc.name "I'll do my best. Is [the_person.title] here?"
    else:
        mc.name "Ah, I didn't realize you were in the market for cute guys?"
        alexia "I, ermm... I mean I'm not..."
        mc.name "I'm just teasing. Is [the_person.title] here?"
    alexia "Yeah. She's over there."
    "You follow [alexia.possessive_title]'s finger pointing to a computer desk set up to the side of the projector. [the_person.possessive_title] is there, getting set up."
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_left(yoffset = 0, zoom = 0.5))
    alexia "You are just in time, it is just getting started!"
    mc.name "Nice. Can you fill me in on the details?"
    alexia "Sure. This first match should be just a warm up for them. Technically it is an elimination match, but her team should win pretty easily."
    mc.name "Nice."
    "You chit chat with [alexia.title] for a bit, but soon the match starts up."
    "You look over at [the_person.possessive_title]. Her hands are on the keyboard, but she is shaking a little bit. It appears her nerves might be getting to her a bit?"
    mc.name "Has she ever played in something like this before?"
    alexia "No, this is her first time in a big tournament like this."
    "Oh boy. Nerves can be a powerful thing. You hope she is able to do well."
    "The match begins. You watch on the projector as [the_person.possessive_title] starts out. She plays conservatively, sticking with her team as they attack the center point."
    "The battle for the center point looks hard fought. You watch as [the_person.title]'s team manages to down an enemy, but when trying to finish them off, the enemy team successfully revives them."
    "As her team pulls back, [the_person.title]'s team has a player get downed. She quickly stealths and is able to revive them quickly."
    alexia "Wooo! You go girl!"
    "Several people in the crowd cheer for her. However, the spike in noise almost seems to startle her. She looks up from her computer and sees how many people are watching."
    "She turns back to the computer, but you note that her playstyle suddenly gets a bit rougher. She isn't capitalizing on as many opportunities and is playing too conservatively."
    "When another teammate gets downed, she attempts to stealth again to revive them. This time, however, the enemy team uses a stealth removal skill and stun her. They manage to down her and kill off her teammate."
    "A few seconds later, the enemy finishes her off, taking the center point. You hear some mumbles in the crowd as her respawn timer comes up."
    mc.name "[alexia.title]... she is completely off her game. Her nerves are really getting to her."
    alexia "Yeah... she'll pull through though! I'm sure she'll come back..."
    "The match continues, but unfortunately, [the_person.possessive_title] is unable to shake off her first time tournament jitters."
    "In an unfortunate encounter, she and a teammate engage the enemy two on two at her home point. Normally she is able to carry in these situations easily, but this time she fumbles."
    "Pushing to far against a low health enemy, suddenly they counter her attack and stun her. Before she can react, the enemy pair down her. Caught far from her teammate, she can only watch as they finish her off."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    "The match itself stays fairly close as [the_person.title] pushes back and forth at a couple points. However, she just isn't able to tip the balance in their favor."
    "When the match is over, the score is close, but [the_person.possessive_title] is the worst performer on her team. If she had been able to focus better, they would have won."
    "The crowd is stunned. You turn to [alexia.title]."
    alexia "Oh... oh no... Myra..."
    "The people who were watching the match start to get up. There are several murmurs but nobody really says much."
    "You watch as [the_person.title] gets up and quietly leaves the room. She looks pretty disappointed."
    $ scene_manager.remove_actor(the_person)
    $ scene_manager.update_actor(alexia, position = "stand3", emotion = "sad")
    mc.name "That was too bad. She looked really off her normal game there."
    alexia "I know! Gosh I don't know what to do... should I text her?"
    mc.name "I don't know. She might just want some space after that."
    alexia "You're right... I'll text her later."
    mc.name "Yeah... anyway, [alexia.title], thanks for letting me know about this. I appreciate it."
    alexia "Ah, of course."
    mc.name "I'm going to get going. Take care."
    alexia "See ya."
    $ scene_manager.clear_scene()
    "You stand up and walk out of the gaming cafe."
    "That was hard to watch. You are sure that [the_person.possessive_title] is devastated at the result."
    "You wonder to yourself. Could helping her with her focus be something that you could help with?"
    "Surely there are ways that you could help her out. Maybe you should wait a few days and talk to her about it?"
    $ add_myra_train_focus_intro_action()
    call advance_time() from _call_advance_time_myra_esports_first_tournament
    return

label myra_train_focus_intro_label(the_person): #40 love, room entry event, allows for a recurring event after.
    $ add_myra_loses_sponsor_action()
    $ add_myra_train_focus_action()
    $ myra_focus_progression_scene.call_scene([the_person])
    return

label myra_loses_sponsor_label(the_person):   #mandatory 60 love event. Has a date at the bar, unlock street fighter, option to sponsor her, spend the night at her place.
    $ the_person.draw_person(position = "walking_away")
    $ the_person.change_happiness(-50)
    "You walk up to the gaming cafe. [the_person.possessive_title] is at the front door, locking up."
    mc.name "Hey [the_person.title]. Headed out early today?"
    "She turns around after she finishes locking up."
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Yeah you could say that."
    the_person "I just got some bad news, so I decided to close up early tonight and hit the bar."
    the_person "Want to come with me? I could use a drinking buddy. As a warning, I'm probably going to get fucking wasted tonight."
    mc.name "I suppose I could go for a couple of drinks. I know a good place too."
    the_person "Great! Let's get out of here."
    $ mc.change_location(downtown)
    "You step out of the mall and start walking toward downtown."
    mc.name "So... if you don't want to talk about it that's fine..."
    the_person "Nah, it's fine. I got a call today from one of the team's sponsors, letting me know that they are pulling out."
    the_person "Apparently my performance in the last tournament was not up to their standards."
    mc.name "Ah. that is unfortunate."
    the_person "Yeah. They make like, my favorite energy drinks too. That's okay though, who needs them!"
    mc.name "Exactly."
    $ mc.change_location(downtown_bar)
    "You step inside the bar. After a quick ID check, you walk with [the_person.title] up to the bar."
    "Bartender" "Hey, what'll it be for you two?"
    mc.name "I'll just have a bourbon. Neat."
    the_person "Can I get a zombie?"
    "Bartender" "Sure thing. You paying?"
    mc.name "Yeah, let me open up a tab."
    the_person "I can get my own..."
    mc.name "Nonsense. You just take it easy tonight and cut loose a little."
    the_person "Thanks..."
    $ the_person.change_love(1)
    $ the_person.change_obedience(1)
    $ mc.change_locked_clarity(10)
    "You walk with [the_person.title] over to a table and sit down."
    $ the_person.draw_person(position = "sitting")
    mc.name "So, a zombie huh? I probably should have had you pegged as a rum drinker."
    the_person "Yeah, I like fruity. Passion fruit especially."
    "You chit chat with [the_person.possessive_title] about some things while you both have your drinks."
    "You think about [the_person.title]'s financial situation as you make some small talk."
    call small_talk_person(the_person, apply_energy_cost = False) from _call_small_talk_person_myra_bar_date_01
    "The drinks are empty."
    mc.name "Hey, another round?"
    the_person "Sounds great! I'm gonna hit up the lady's room real quick."
    mc.name "Hoping to find a lady?"
    the_person "Nah, but after an energy drink and some booze I've gotta piss!"
    $ clear_scene()
    "You chuckle to yourself a bit as you get up and head back to the bar. [the_person.title] is definitely a wild, outspoken person."
    "You get two more drinks. You sit back down at the table and look at them. If you are careful, you can probably sneak a serum into hers..."
    call give_serum(the_person) from _call_give_myra_serum_bar_date_01
    "After another minute, [the_person.title] returns to the table."
    $ the_person.draw_person(position = "sitting")
    the_person "Yum, this looks good."
    "She takes a big sip of her drink."
    mc.name "So, I'm curious. Let's say a local business was interested in sponsoring your esports team."
    mc.name "How much would you be looking for, money wise?"
    "[the_person.possessive_title] rolls her eyes a bit."
    if the_person.has_large_tits:
        the_person "I don't know. Maybe it's time for me to open one of those slutty picture accounts."
        the_person "I bet a lot of nerds out there would pay for pics of a big titty blue haired girl playing games!"
        mc.name "That's not what I was asking."
        "[the_person.title] sticks her tongue out at you instead of replying."
    else:
        the_person "Probably not much, to be honest. It seems to get a sponsorship gaming as a woman these days you gotta have milkers out to HERE."
        "[the_person.possessive_title] motions her hands over her chest, suggesting incredible endowment would be required."
        the_person "Not that I have anything against big tits anyway. I'm just not what you would call blessed in the chest."
        mc.name "Do you want to be?"
        the_person "Ha! You make it sounds like it is a choice I can just make."
        menu:
            "Encourage her to get bigger tits":
                mc.name "I mean, there are multiple ways of achieving that, if it is something you want to do."
                the_person "I... I'm sorry, are you suggesting I get implants?"
                mc.name "Not necessarily. It just seemed like you were interested in the possibility?"
                the_person "Well, I'm not. Not through surgery anyway."
                mc.name "There are ways of achieving a larger bust without surgery"
                the_person "Wow, well, that is a subject for another time... What were we talking about again?"
                $ the_person.change_love(-1)
                $ the_person.change_obedience(1)
                $ mc.change_locked_clarity(10)
                $ add_myra_bigger_tits_intro_action()
            "Change the subject":
                mc.name "Hey, you're the one who brought up tits."
                the_person "Right. Well, I would never get surgery for it. What were we talking about again?"
    mc.name "Let me get straight to the point. How much money are you going to lose from the sponsorship you lost today?"
    "[the_person.title] quietly takes a long sip from her drink before responding."
    the_person "Well... the one I lost today was for ten grand."
    mc.name "I see. What if I sponsored you? My pharmaceutical company could use a bit more press."
    the_person "Ugh, can we talk about it another time? I wanted to go out tonight to get AWAY from fucking finances."
    $ the_person.change_happiness(-2)
    "[the_person.possessive_title] takes a long sip from her drink, finishing it."
    the_person "I just wanted to go out tonight, get wasted, and who knows? Maybe wind up in someone else's bed for once."
    mc.name "You know what? That's fair. Actually, I think I can help you out with both of those."
    the_person "Is that so?"
    "[the_person.title] leans her head back and opens her mouth. The last couple drops of her drink fall onto her tongue, as she makes a show out of her drink being empty."
    $ mc.change_locked_clarity(10)
    the_person "I'm not sure about that [the_person.mc_title], my glass seems awfully dry..."
    mc.name "I'll be right back, let me go fix that."
    "You start to get up."
    the_person "Hey, meet me over there, I think I see some old arcade games."
    "[the_person.title] points to the back corner where some older arcade cabinets are set up."
    mc.name "Sounds good, I'll meet you over there."
    $ clear_scene()
    "You head over to the bartender, ordering a couple more drinks for you and her."
    "It takes a couple minutes, but you find them, then head over to where she is standing."
    $ the_person.change_happiness(10)
    $ the_person.draw_person(emotion = "happy")
    the_person "Hey! It's about time. Get your ass over here!"
    "You walk up to the cabinet she is standing next to."
    the_person "That's right! I can't believe it, they have a legit Super Street Kombat 2 Turbo machine here!"
    the_person "I already got quarters from the change machine. Prepare your ass! I am coming for you!"
    mc.name "That is pretty much word for word what I'll be saying to you in a couple hours."
    "She laughs."
    the_person "Yeah right! More like, by the gods, that ass! I'm coming already!"
    mc.name "Poe-Tay-Toe, Poe-Tah-Toe"
    $ the_person.change_happiness(10)
    "It feels good to see her smile. However, as she puts in two quarters, you brace yourself for the ass whooping you are likely about to receive from [the_person.possessive_title]."
    call bar_date_arcade_round_label(the_person, skill_modifier = 50) from _myra_bar_date_round_1_fight_01
    if _return:
        "You can't believe it. You actually won."
        "It makes no sense whatsoever, but you actually did it."
        the_person "What? I... you must be cheating!"
        mc.name "Me? Never!"
        the_person "Yeah right..."
    else:
        "[the_person.possessive_title] gloats a bit. You got absolutely dismantled."
        the_person "Fuck yeah! I still got it! I used to dominate at this game."
        mc.name "I'm pretty sure you still do."
    "?????" "Hey, that game is great. Can I get the next match?"
    "You turn around. A group of three guys is behind you, and seem interested in the game."
    the_person "Sure. I want to stay on though."
    "The guys seem skeptical."
    "?????" "No offense, but we don't want to play against a girl, we want some REAL competition."
    "Oh shit."
    the_person "Oh my. Is that so? Well I'll tell you guys what. First one of you guys to win against me gets to take me home, and I'll do anything you want."
    $ mc.change_locked_clarity(20)
    "Oh shit. These guys have no idea who they are up against."
    "?????" "Damn, I'm first!"
    mc.name "Want another drink?"
    the_person "Absolutely. Alright guys, if you want a shot, you gotta front the quarters!"
    "She could probably hustle a lot of guys this way..."
    $ clear_scene()
    "You head over to the bar. You order another round for her, and just get a water for yourself. You are a little buzzed, but you don't want to get too drunk. You have a good feeling about the rest of the night."
    "You take your time, even watch a little bit from the bar. Several guys have wandered over and have started watching her play."
    "When you get her drink, you head back over. She is just finishing up her sixth win."
    "?????" "Fuck! This bitch is good!"
    the_person "Damn right!"
    $ the_person.draw_person(emotion = "happy")
    $ the_person.change_happiness(10)
    "She looks to be having a great time, dismantling every challenger that faces her."
    the_person "Ah! [the_person.mc_title]. It's your turn!"
    "She takes the drink from you. She brings it to her lips and drinks half of it in one go."
    the_person "Don't forget the rules! If you win, I'm going home with you tonight."
    "She gives you an almost imperceptible wink. You put in a quarter and the game starts up for another round."
    call bar_date_arcade_round_label(the_person, skill_modifier = -500) from _myra_bar_date_round_1_fight_02
    "There are groans from the guys watching after you win. There was no way she was trying her hardest that match!"
    "?????" "Gah, that must be her boyfriend or something. Shoulda known..."
    if the_person.is_girlfriend:
        the_person "Yeah, sorry guys, you never REALLY had a chance."
    else:
        "[the_person.possessive_title] blushes a little at the comment."
        the_person "He isn't my boyfriend... err..."
        $ the_person.change_love(1, 80)
        "It is clear from the way she said that, she wouldn't mind if it were true..."
    "[the_person.title] takes her drink and finishes it off."
    mc.name "Let me go settle up with the bartender and let's get out of here."
    the_person "Yessir!"
    "[the_person.possessive_title] is starting to slur her words a bit."
    $ mc.business.change_funds(-100)
    "You settle up with the bartender. You've run up quite the tab, but it was worth it for a fun night with [the_person.possessive_title]."
    $ mc.change_location(downtown)
    "You step outside with [the_person.title]."
    the_person "Hey... so... we are going to your place... right?"
    $ mc.change_locked_clarity(10)
    "[the_person.possessive_title] looks at you. You can tell she is a little apprehensive of your answer."
    mc.name "If you have had too much to drink and can't, that is okay..."
    "You lean forward and whisper into her ear."
    mc.name "... but otherwise I plan to take you home and fuck your brains out."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(20)
    the_person "Mmm... that sounds nice..."
    the_person "Lead on then!"
    "You start walking towards your house."
    mc.name "So, I should probably warn you about something..."
    the_person "Oh god... you have a wife?"
    mc.name "What? No... no."
    mc.name "My umm... My dad isn't around anymore. I live with my sister and my mother."
    the_person "Oh thank god. I totally thought you were about to say you have a wife!"
    "She laughs a bit longer than is normal. But she is rather intoxicated."
    the_person "I mean, you're still a loser for living with your mom, but at least you aren't married!"
    mc.name "Hey, you better watch your mouth."
    the_person "Or what?"
    mc.name "I might have to find better uses for that mouth of yours."
    $ the_person.change_arousal(10)
    the_person "Yeah right. I don't give blowjobs on a first date, mister. Or ever."
    the_person "You can use my other holes however you want though..."
    "Hmmm, this is interesting. Does [the_person.possessive_title] have a bit of a submissive streak?"
    $ mc.change_location(bedroom)
    "You step into your house, and make it un-accosted to your bedroom."
    $ the_person.draw_person(position = "back_peek")
    "When the door is closed and locked, you grab her from behind."
    $ the_person.add_situational_slut("Date", 20, "There's no reason to hold back, he's here to fuck me!")
    the_person "Oh god, you can do anything you want to me."
    mc.name "Mmm, is that so? Let's get this off you first..."
    $ the_person.strip_outfit(position = "back_peek")
    "You get her naked. You run your hands all up and down her sides, her tits, her thighs..."
    $ the_person.draw_person(position = "standing_doggy")
    "You bend her over your bed. She sighs when you run your hand across her ass, groping at her cheeks."
    mc.name "You love to put up such a tough front. But it's all an act, isn't it?"
    the_person "I... I don't know what you mean..."
    $ play_spank_sound()
    "You give her ass a hard spank."
    $ the_person.change_arousal(5)
    $ mc.change_locked_clarity(30)
    the_person "Ah!"
    mc.name "You want someone to do that to you, don't you? To treat you like the fuck doll you want to be so bad."
    $ play_spank_sound()
    "*SPANK*"
    the_person "OH FUCK."
    $ the_person.change_arousal(5)
    $ play_moan_sound()
    "[the_person.possessive_title] moans when you spank her again. She has to be a closet sub, despite her normally wild attitude."
    $ the_person.discover_opinion("being submissive")
    the_person "I, I just like it when you use me... when I make you feel good..."
    $ play_spank_sound()
    "You give her another spank."
    $ the_person.change_arousal(5)
    $ play_moan_sound()
    the_person "AH!"
    mc.name "You liar. You don't like it. You love it. I can tell. Look at how wet you are getting."
    "You run your fingers along her slit. She loves the way you are getting rough with her. You make a note to spank her more in the future."
    $ the_person.unlock_spanking()
    $ mc.change_locked_clarity(30)
    mc.name "You are such a good little slut. What hole do you want it in?"
    the_person "Umm, whichever one you want. I like it in either one..."
    mc.name "Is that so? You want it in your tight little asshole?"
    the_person "Ah, if you want... I'm okay with that."
    mc.name "Maybe I will, but for now I'm going to fuck your pussy. Are you ready?"
    the_person "Oh fuck yeah I'm ready..."
    "You quickly pull off your clothes. You grab her by the hips and get behind her."
    "[the_person.possessive_title] wiggles her ass back and forth when she feels you get close. You can feel the heat and humidity coming off her cunt as you line yourself up."
    "She sighs when she feels the tip begin pushing into her."
    the_person "Oh fuck that feels so good..."
    "You slide yourself in inch by inch. [the_person.title]'s slippery cunt feels amazing as you push yourself in."
    the_person "Fuck your cock feels so good..."
    $ the_person.break_taboo("vaginal_sex")
    $ the_person.break_taboo("condomless_sex")
    $ mc.change_locked_clarity(50)
    "Fully sheathed, you enjoy the heat coming off of [the_person.possessive_title]'s ass for a moment. You give her another spank."
    $ play_spank_sound()
    "*SPANK*"
    $ the_person.change_arousal(10)
    the_person "Ah! Oh fuck me [the_person.mc_title]..."
    "You pull back and start to give it to her."
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_sex_description_myra_post_drinks_01
    $ the_person.draw_person(position = "missionary")
    "[the_person.title] falls onto your bed when you finish. You lay down next to her."
    the_person "That was just what I needed, god damn."
    if not the_person.is_girlfriend:
        the_person "You know what was funny? When one of the guys at the bar was like, oh damn, she's got a boyfriend. Wasn't that funny?"
        mc.name "Funny? I suppose."
        the_person "I mean, can you imagine? Us dating? Hah, I mean... I could imagine it..."
        "[the_person.possessive_title] seems to be dropping pretty big hints that she is interested in making your relationship more official."
        menu:
            "Ask her to be your girlfriend":
                mc.name "I don't know, I think that would be pretty nice."
                the_person "Ah, I mean... I think it would be nice too..."
                mc.name "Do you want to? Be my girlfriend?"
                $ the_person.change_happiness(30)
                $ the_person.change_love(5, 90)
                the_person "Ah! Fuck, I didn't think you were ever gonna ask. I'm down for it if you are!"
                if myra_alexia_teamup_scene.stage >= 2:
                    "One thing bothers you a bit about it though."
                    mc.name "What about when I come to game nights? You know, with you and [alexia.title]."
                    the_person "Oh, I mean, she is such a good friend of mine, I wouldn't be too upset if we um... kept doing that."
                $ the_person.add_role(girlfriend_role)
            "Just be friends":
                mc.name "I definitely enjoy spending time with you, especially doing stuff like this. But I'm not ready for anything serious."
                the_person "Right, that's totally what I was thinking too. That's why it was funny... right?"
                $ the_person.change_happiness(-3)
                $ the_person.change_obedience(5)
                "While her words are optimistic, you note a hint of sadness in her voice when she says that."
    else:
        the_person "God, it feels so good to be with you. That was so funny, at the bar! That guy was like, aww fuck she's got a boyfriend!"
        the_person "Damn right! And his dick is AMAZING!"
        mc.name "Poor guys thought they actually had a chance beating you at that game."
        the_person "Yeah, I suppose that was kind of mean."
    "You lay with [the_person.possessive_title] a little longer."
    mc.name "Do you want to stay over?"
    the_person "Ah, I can't. I actually have something I need to get done in the morning."
    $ the_person.draw_person()
    "[the_person.title] slowly gets up. You just watch her as she gets herself dressed again."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "I think I can see myself out. Goodnight [the_person.mc_title]."
    mc.name "Goodnight."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    $ the_person.clear_situational_slut("Date")
    $ add_myra_gains_sponsor_action()
    "You think about the fun night you had at the bar with [the_person.possessive_title]."
    "Her business at the gaming cafe... You feel like there are some real opportunities there, if you can convince her to accept you as a sponsor."
    "You resolve yourself to save up some funds to invest in her sports team. You make a mental note: save at least $25000 and talk to her about it."
    call advance_time from _call_advance_myra_post_bar_day_advance_01
    return

label myra_gains_sponsor_label(the_person):
    $ the_person.draw_person()
    mc.name "Hey, we need to talk."
    the_person "Oh? What is it, [the_person.mc_title]?"
    mc.name "I want in. I want to sponsor your esports team."
    the_person "Seriously, you don't have to do that..."
    mc.name "I have $15000 I want to invest. I want the opportunity to invest further in the business in the future also, as well as a small cut when you start dominating esports tournaments."
    the_person "Fuck, that's a lot of money. Are you sure? That's more than double what I was getting from my last sponsor."
    mc.name "I am absolutely certain. Take it. Invest in your cafe. I believe in you, and I believe in your business."
    $ the_person.change_obedience(10)
    $ the_person.change_love(5, 90)
    "You hand her a check, made out for the full amount."
    the_person "Wow... okay... You are now a sponsor of the Predators esports gaming team!"
    "[the_person.possessive_title] smiles at you. You really do feel like this is going to be a worthwhile business venture."
    the_person "I'm gonna go put this in the safe for the day, if you need anything else, come find me, okay?"
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] throws her arms around you and gives you a big hug, before letting go and walking off."
    $ clear_scene()
    $ mc.business.change_funds(-15000)
    $ add_myra_esports_second_tournament_intro_action()
    $ add_myra_develop_energy_drink_intro_action()
    return

label myra_esports_second_tournament_intro_label(the_person):   #Sets up for the second tournament. on room enter event. 80 love
    "Starbuck" "Hey you! This event is for outline purposes, and is not yet written"
    "Requires significant progress in the focus training. [the_person.title] announces there is another tournament this weekend."
    "The gaming cafe has actually won the contract for the tournament to be held in person. She is excited but scared how it will go with all the people there."
    #Just use this event to set up anticipation for the tournament itself.
    $ add_myra_esports_second_tournament_action()
    return

label myra_esports_second_tournament_label(): #Mandatory event. Myra wins her second tournament
    "Starbuck" "Hey you! This event is for outline purposes, and is not yet written"
    $ the_person = myra
    "The tournament itself occurs. [the_person.title] plays a key role on her team, and thanks to her focus training, they place 3rd overall at the tournament."
    "While this isn't first, it is a huge improvement over the last tournament's early exit. Thanks to your sponsorship, you gain a 5%% market boost."
    $ add_myra_gaming_cafe_expansion_intro()
    return

label myra_gaming_cafe_expansion_intro_label(the_person):   #100 love event. Myra approaches MC about further expander her business. offers to move in.
    "Starbuck" "Hey you! This event is for outline purposes, and is not yet written"
    "With winnings from tournaments, [the_person.title] has bought two adjacent shops and is planning to expand her gaming cafe."
    "The gaming cafe expands their hours to open 7 days a week now. She remarks she feels like she barely goes home anymore."
    "She makes a remark that maybe she should just move in with MC because she can barely keep up around her apartment as a joke."
    "MC can either jump on it and tell her to move in with him, or just move on."
    $ myra.event_triggers_dict["is_expanding_business"] = True
    return
