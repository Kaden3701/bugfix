init 2 python:
    def myra_distracted_gaming_requirement(the_person):
        if the_person.sluttiness >= 20 and myra_at_cafe():
            return True
        return False

    def myra_lewd_gaming_requirement(the_person):
        if the_person.sluttiness >= 40 and myra_at_cafe() and time_of_day == 3 and myra.days_since_event("myra_distracted_day") > TIER_1_TIME_DELAY:
            return True
        return False

    def myra_lewd_game_fuck_intro_requirement(the_person):
        if the_person.has_taboo("vaginal_sex"):
            return False
        if the_person.sluttiness >= 60 and myra_at_cafe() and time_of_day == 3 and myra.days_since_event("myra_lewd_game_day") > TIER_1_TIME_DELAY:
            return True
        return False

    def myra_lewd_game_fuck_requirement(the_person):
        if not myra_lewd_game_fuck_avail():
            return False
        if myra_at_cafe() and time_of_day == 3:
            if mc.energy < 40:
                return "You are too tired"
            elif the_person.energy < 40:
                return "She looks too tired"
            return True
        return False

    def myra_adult_gaming_intro_requirement(the_person):
        return False # current writing spot, event is disabled
        if the_person.sluttiness >= 80 and myra.days_since_event("myra_lewd_game_fuck") >= TIER_2_TIME_DELAY:
            if myra_is_expanding_business() and myra_at_cafe():
                return True
        return False

    def myra_adult_gaming_opening_requirement():
        if myra_at_cafe() and myra.days_since_event("adult_cafe_opening_day") >= TIER_3_TIME_DELAY:
            return True
        return False

    def myra_harem_entry_requirement(the_person):
        return False

    def add_myra_distracted_gaming_action():
        myra_distracted_gaming = Action("Myra Distracts Her Opponents", myra_distracted_gaming_requirement, "myra_distracted_gaming_label")
        myra.add_unique_on_room_enter_event(myra_distracted_gaming)
        return

    def add_myra_lewd_gaming_action():
        myra_lewd_gaming = Action("Myra Plays Lewd Games", myra_lewd_gaming_requirement, "myra_lewd_gaming_label")
        myra.add_unique_on_room_enter_event(myra_lewd_gaming)
        myra.set_event_day("myra_distracted_day")
        myra.event_triggers_dict["distracts_gamers"] = True
        return

    def add_myra_lewd_game_fuck_intro_action():
        myra_lewd_game_fuck_intro = Action("Myra Game Reenactment", myra_lewd_game_fuck_intro_requirement, "myra_lewd_game_fuck_intro_label")
        myra.add_unique_on_room_enter_event(myra_lewd_game_fuck_intro)
        myra.set_event_day("myra_lewd_game_day")
        return

    def add_myra_lewd_game_fuck_action():
        myra_lewd_game_fuck = Action("Lewd Game Reenactment", myra_lewd_game_fuck_requirement, "myra_lewd_game_fuck_label")
        myra.get_role_reference("myrabelle").add_action(myra_lewd_game_fuck)
        myra.event_triggers_dict["lewd_game_fuck"] = True
        myra.set_event_day("myra_lewd_game_fuck")
        return

    def add_myra_adult_gaming_intro_action():
        myra_adult_gaming_intro = Action("Myra Wants Lewd Cafe", myra_adult_gaming_intro_requirement, "myra_adult_gaming_intro_label")
        myra.add_unique_on_room_enter_event(myra_adult_gaming_intro)
        return

    def add_myra_adult_gaming_opening_action():
        myra_adult_gaming_opening = Action("Myra Opens Lewd Cafe", myra_adult_gaming_opening_requirement, "myra_adult_gaming_opening_label")
        mc.business.add_mandatory_crisis(myra_adult_gaming_opening)
        myra.set_event_day("adult_cafe_opening_day")
        return

    def add_myra_harem_entry_action():
        myra_harem_entry = Action("Harem: Myra", myra_harem_entry_requirement, "myra_harem_entry_label")
        myra.add_unique_on_room_enter_event(myra_harem_entry)
        myra.event_triggers_dict["lewd_cafe_open"] = True
        return

label myra_distracted_gaming_label(the_person):       #20 sluttiness event. MC can suggest she should distract her opponents by dressing slutty. second chance to suggest bigger tits
    # $ myra.event_triggers_dict["suggested_bigger_tits"] = True
    "You step into the gaming cafe. [the_person.title] isn't at the desk, where she usually is."
    "Looking around, you see her playing a game with several guys. It looks like some kind of first person shooter game they are all playing together."
    $ the_person.draw_person(position = "sitting")
    "You walk over and watch from behind her."
    the_person "That's it! Suck on THIS shaft, boy!"
    "[the_person.possessive_title] kills an enemy player with a long green link gun. You can't help but chuckle at the tone of her voice."
    the_person "Ha! Kiss my ass. Or eat it! Your choice bitch!"
    "Her trash talking is top notch, with obvious sexual tones. You look at some of the guys sitting close to her."
    "They keep peeking over at her as she continues her sexual trash talk."
    the_person "God damn bitch. Are you worried? Are you scared? Don't worry baby what's the worst thing that could happen."
    "You realize that her trash talking is incredibly effective. Several of the guys she is playing against are either getting upset or clearly distracted by her."
    "The match finishes up. This is an area of her game you hadn't really considered before. Has she ever though of dressing suggestively for matches?"
    the_person "Alright, I better get back to the desk. I'll destroy your asses again some other time boys."
    "The guys are muttering to themselves, but seem to agree it is a break time and start to disperse for now."
    $ the_person.draw_person()
    "[the_person.possessive_title] stretches, and then stands up. She turns and notices you."
    the_person "Oh hey [the_person.mc_title]. Good to see you! Something I can help you with?"
    mc.name "Not at the moment, but I was watching that last match. That was quite the show!"
    the_person "Ah, thank you 'coach'."
    mc.name "Hey, I have a question. You were doing a lot of trash talking, and I noticed that it was really distracting to some of them."
    mc.name "Have you ever thought about like, you know, dressing in a more provocative way for a match? Within rules obviously, but it might be an effective distraction."
    the_person "Wow. Well, I guess I'd prefer to have a more neutral match. I don't want to win just because the other team is drooling all over me."
    if not the_person.has_large_tits:
        the_person "But, it doesn't really matter anyway. For that strategy to be effective, you gotta have a little more... up top... if you know what I mean."
        "You take a moment to check out [the_person.possessive_title]. It might be effective if she were to level up a bit, in the chest."
        menu:
            "Encourage her to get bigger tits":
                mc.name "Have you ever though about having bigger tits?"
                the_person "Wow, straight to the point eh? I've thought about it, but honestly, surgery terrifies me. So I guess we'll never know?"
                $ add_myra_bigger_tits_intro_action()
                "Hmmm, you wonder if you brought her a serum that would increase her chest size if she would agree to it."
                "You decide for now to just move the conversation along."
            "Move the conversation along":
                "You decide not to encourage any body modification for now."
    mc.name "I think if you dressed a little more provocatively, it might even help your business. You know, sex sells, and your target demographic here is a little on the nerdy side."
    $ mc.change_locked_clarity(20)
    if the_person.opinion_score_skimpy_outfits() < 2:
        $ the_person.increase_opinion_score("skimpy outfits")
        the_person "You know, you might actually be on to something. That isn't a bad idea."
    else:
        the_person "You're preaching to the choir. I don't mind showing some skin, but I have to keep it legal, you know?"
    the_person "Anyway, I need to get back to the desk. If you need anything, give me a holler!"
    $ the_person.draw_person(position = "walking_away")
    "You watch as [the_person.possessive_title] walks away. There is a bit of a swagger in her step..."
    $ clear_scene()
    $ add_myra_lewd_gaming_action()
    call advance_time from _call_advance_myra_lewd_games_05
    return

label myra_lewd_gaming_label(the_person):           #40 sluttiness event. Catch Myra playing lewd games.
    "You step into the gaming cafe. It is pretty late in the day, and it appears to be mostly empty."
    "You look towards the main desk, but you don't see anyone. You look around a bit, eventually finding [the_person.possessive_title] in a secluded corner, playing a game."
    $ the_person.draw_person(position = "sitting")
    $ the_person.arousal = 70
    the_person "Mmm... fuck..."
    "As you walk up behind her, you notice she is making some gasping and soft moaning noises. She has a headset on and doesn't notice you approach."
    "You see on her screen, she is playing The Sims. However, it is clear from the scene that is being shown on her screen that she has installed some sexual mods for it."
    "You quickly walk up behind her now. On her screen is a blue haired sim, getting fucked from behind by another sim that looks surprisingly similar to you..."
    "You notice as you get close that [the_person.title] is touching herself and seems really into it."
    the_person "Yeah... oh..."
    "This opportunity seems too good to pass up. You decide to see if she wants a little help."
    mc.name "That looks like a fun game [the_person.title]."
    $ the_person.draw_person()
    the_person "Ah!"
    "[the_person.possessive_title] jumps up. She pushes her chair back and stands up, turning her body so it is between you and the computer screen."
    the_person "I wasn't... Ah!"
    "She pulls at her headset, taking it off. However, in her urgency, it pulls the headphone jack out of the computer."
    "Fucking noises and sounds start coming from her computer speakers."
    the_person "That's not... ugh fuck."
    "[the_person.title]'s arms drop to her sides. She gives up pretending she isn't playing a lewd version of The Sims."
    mc.name "Seriously though, that looks like a really fun game. You don't have to stop just because I'm here."
    mc.name "In fact, maybe you could use some help?"
    "Her face looks conflicted for a few seconds, but as she realizes what you are saying, she quickly accepts."
    the_person "We can't like, fuck back here, but if we could be discreet..."
    mc.name "Don't worry, I know just want to do. Sit back down."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] sits down. You decide to get down below desk level and eat her out until she finishes."
    mc.name "Here, turn this way, so I can have better access."
    "[the_person.title] turns and spreads her legs, and you start to pull aside the clothes in your way."
    $ the_person.strip_to_vagina(prefer_half_off = True, position = "missionary")
    "You hear as [the_person.possessive_title] plugs her headphones back in and looks at the computer screen again."
    "You bring your face up to her cunt. She is soaked, her puffy pink lips showing clear signs of arousal. This should be quick!"
    $ the_person.break_taboo("licking_pussy")
    "You stick your tongue out and run it up and down her cunt a few times. You feel her hand running through your hair."
    "You easily find her clit and start to circle your tongue around it. She gives a couple muffled moans as you get to work."
    $ the_person.change_arousal(20)
    "[the_person.title]'s hips start to move as you eat her out. Her hand is grabbing the back of your head now, encouraging you as you lick her clit."
    the_person "Oh fuck... [the_person.mc_title] I'm already so close..."
    $ the_person.change_arousal(30)
    "[the_person.possessive_title]'s groans get urgent, and her legs are twitching noticeably on either side of you."
    "You speed up your efforts, doing your best to drive her towards her orgasm. She moans and begins to writhe under your skilled tongue."
    the_person "That's it!... Oh fuck!..."
    "All at once the tension in her body is unleashed in a series of violent tremors. Her hand urgently holds your face in place as she grinds against it."
    $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "She definitely just orgasmed, but the hand on the back of your head remains."
    "Sensing she isn't done yet, you bring up two fingers and easily slide them into her sloppy cunt."
    $ the_person.change_arousal(20)
    the_person "Oh fuck! That's so good... keep going I'm going to cum again..."
    "[the_person.possessive_title]'s voice is wavering as she pleads with you to keep going."
    "You pump your fingers inside of her as you lick her clit. You gently suck on it, and her moans are growing even more urgent."
    $ the_person.change_arousal(40)
    the_person "Yes... YES! Oh..."
    "The hand on the back of your head is starting to shake. Her legs are quivering too as she begins to orgasm again."
    $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "Her body shudders for several seconds, and her breathing is ragged between muffled moans of pleasure."
    the_person "So good... that feels so good [the_person.mc_title]."
    "Her voice is getting husky. She almost growls at you. Her hips haven't stopped moving with you though."
    "Can you make her cum again? She seems really turned on. You decide to double down and see if you can make it happen."
    "You push your two fingers deep inside of her, turn them so that they can curl up, then find her g-spot."
    "You start to stroke her g-spot firmly with your fingers, and with your mouth you suck her clit into your mouth and start to suck on it aggressively."
    $ the_person.change_arousal(30)
    the_person "Ah! Oh fuck [the_person.mc_title] that's so good you're gonna make me cum again!"
    "Her voice is urgent and getting louder. Thankfully the place is basically empty or you are sure someone would have noticed."
    "[the_person.possessive_title]'s hips are still moving, but the movements are disjointed, and she is having trouble getting a rhythm going."
    "Her hand in your hair is just holding on as you eat her out. Her juices are running down her cunt and have started collecting on the chair below her."
    the_person "I'm cumming... I'm cumming again!"
    $ the_person.change_arousal(30)
    "[the_person.title]'s whole body spasms as she starts to cum again."
    $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 60)
    $ mc.change_locked_clarity(50)
    $ the_person.change_energy(-40)
    "When she finishes, her body goes limp. She is completely spent."
    $ the_person.draw_person(position="sitting")
    "You slowly stand up. Looking around, it appears that no one else was here to have noticed your oral session."
    the_person "That... holy fuck..."
    "[the_person.possessive_title] is in a post orgasm stupor. It seems like she would be receptive to some training."
    call do_training(the_person) from _call_do_training_myra_post_oral_01
    the_person "I don't think I can get up."
    mc.name "Sure you can. Here, let me help you."
    "You take [the_person.title]'s hand and help her up."
    $ the_person.draw_person()
    the_person "I need to close up now... I'm sorry, I'll have to owe you one... okay?"
    mc.name "Sounds good. I'm going to go clean up."
    the_person "Fuck, I'm gonna sleep good tonight..."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You say goodbye to [the_person.possessive_title] and leave the cafe. You quickly use the restroom to clean your face off before continuing on your way."
    $ add_myra_lewd_game_fuck_intro_action()
    $ add_myra_blowjob_training_intro_action()
    call advance_time from _call_advance_myra_lewd_games_01
    return

label myra_lewd_game_fuck_intro_label(the_person):
    $ the_person.draw_person()
    the_person "Oh hey [the_person.mc_title]!"
    "As you step into the gaming cafe, you almost walk into [the_person.possessive_title]."
    mc.name "Oh hey, I was just coming to play some games."
    the_person "Ah, sorry. Things were really slow this evening so I was just about to close up."
    "She looks at your thoughtfully."
    the_person "Actually, we could hang out for a bit if you want to?"
    the_person "I haven't forgotten that I umm... sort of owe you for the other day when you caught me playing The Sims..."
    $ mc.change_locked_clarity(20)
    "Hmmm, sounds like maybe she might be thinking about something sexy..."
    mc.name "Sure, I'll hang out for a bit."
    $ the_person.change_happiness(2)
    the_person "Great! Head to the back and let me lock up. I have a fun idea..."
    "[the_person.possessive_title] gives you a wink."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns to go lock the doors. You look at her desk, and see she has an energy drink out. If you are quick, you could slip a serum into it..."
    call give_serum(the_person) from _call_give_myra_lewd_game_fuck_01
    $ the_person.draw_person()
    the_person "Alright, let's go back here. I have a couple couches set up."
    "You follow her to the back."
    the_person "So, I like to play this game where you play as little avatars... you can hook up with other people and I installed this mod where you can even fuck each other."
    the_person "It has an option to cycle through random positions. I thought it would be fun to start it up and let it run and we could try and act out each scene as it goes."
    mc.name "Sounds hot. Let's give it a shot!"
    the_person "Okay! We should probably get comfortable..."
    $ the_person.strip_full_outfit(position = "stand3")
    "[the_person.possessive_title] gets naked, so you do the same."
    call myra_sex_roullette_session_label(the_person) from _myra_lewd_game_fuck_intro_01
    if _return:
        "Wow. Who knew that following a computer game could be so much fun. You feel great after your orgasm."
    else:
        "Damn. You just couldn't finish."
    the_person "Okay... that was hot."
    mc.name "Yeah, it was."
    the_person "We should, like... do that again sometime..."
    mc.name "Yeah?"
    the_person "How about, if you ever want to do that again, just swing by in the evening, and when I close up we can do it again?"
    mc.name "Sounds hot to me."
    the_person "Alright, well, I'm gonna go clean up and head home... can you let yourself out?"
    mc.name "Yeah, I can do that."
    the_person "Alright [the_person.mc_title], I'll see you next time."
    mc.name "See ya."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You let yourself out of the gaming cafe after getting dressed."
    "You can now visit [the_person.possessive_title] at the gaming cafe in the evening and she will let you fuck her in random positions, even letting you finish wherever it shows on the game!"
    $ clear_scene()
    # unlock role action lewd game fuck
    $ add_myra_lewd_game_fuck_action()
    call advance_time from _call_advance_myra_lewd_fuck_01
    return

label myra_lewd_game_fuck_label(the_person):    #Repeatable game reenactment scene.
    mc.name "Hey, I was wondering. You up for some Sims tonight?"
    if the_person.energy < 80:
        the_person "I'm a little tired, but I'd be down to give it a shot."
    else:
        the_person "Mmm, sound fun."
    the_person "There aren't many people here. Let me close up and we can meet in the back."
    mc.name "Sounds good."
    $ clear_scene()
    "[the_person.possessive_title] walks off to clear out the store and lock up. She leaves her drink open on the counter..."
    "Maybe you could drop a serum in really quick..."
    call give_serum(the_person) from _call_give_myra_lewd_game_fuck_02
    "It takes her a while, but eventually [the_person.title] joins you in the back of the cafe."
    $ the_person.draw_person()
    the_person "Alright. I was kind of hoping you'd swing by tonight. Let's get comfortable first."
    "She gives you a wink as she starts to strip down."
    $ the_person.strip_full_outfit(position = "stand3")
    "[the_person.possessive_title] gets naked, so you do the same."
    call myra_sex_roullette_session_label(the_person) from _myra_lewd_game_fuck_intro_02
    "Finished for now, you decide it is time to head out."
    mc.name "That was as amazing as always. I'm going to head out."
    the_person "Yeah... I'm going to get cleaned up. See you [the_person.mc_title]!"
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    $ add_myra_adult_gaming_intro_action()
    "You leave the gaming cafe."
    call advance_time from _call_advance_myra_lewd_fuck_02
    return

label myra_adult_gaming_intro_label(the_person):    #80 sluttiness event. requires finishing her love story, Myra wabts to open adults only section of the cafe.
    "Starbuck" "Hey you! This event is for outline purposes, and is not yet written"
    "[the_person.title] asks MC for some feedback on an idea. Want's to know his opinion because he is sponsor and scared she will lose money."
    "She wants to open an adults only lewd section to the gaming cafe. Want's to know what MC thinks about it."
    "MC thinks it is a great idea. She says check back at a later time."
    $ add_myra_adult_gaming_opening_action()
    return

label myra_adult_gaming_opening_label():
    "Starbuck" "Hey you! This event is for outline purposes, and is not yet written"
    $ the_person = myra
    "[the_person.title] is excited, opens new adults only section of the gaming cafe. Texts MC to meet her there."
    "It has restricted entry via ID card scanner. Clothing is optional and anything goes there. PCs are loaded with pornographic games."
    "When MC walks back, there are already a few girls back there. MC spots a woman playing an adult game and with [the_person.title]'s encouragement, approaches her."
    "Without any introductions, she agrees to suck MC's cock while she plays."
    "This unlocks a new gaming cafe action. Entering the adults only section. The game will grab a random girl sluttiness >40 there for MC to play with."
    $ add_myra_harem_entry_action()
    return

label myra_harem_entry_label(): #100 sluttiness event. If MC already has a harem started, you initiate Myra into it
    "This label is referring to a harem mechanic that does not yet exist."
    return

label myra_sex_roullette_session_label(the_person, breeding_fetish_intro = False): #In this scene, MC and Myra are acting out a randomized sex scene from the Sims. They alternate through sex positions until MC finishes.
    $ current_position = None
    $ report_log = defaultdict(int) #Holds information about the encounter: what positions were tried, how many rounds it went, who came and how many times, etc. Defaultdict sets values to 0 if they don't exist when accessed
    $ report_log["positions_used"] = [] #This is a list, not an int.
    if mc.arousal_perc > 60:
        $ mc.change_arousal(60 - mc.arousal)
    the_person "Alright, give me one second to get the game setup."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] bends over a computer desk and starts to load up the game, her ass pointing back at you."
    $ mc.change_locked_clarity(40)
    "It would be a shame to let this opportunity go by..."
    $ play_spank_sound()
    "*SMACK*"
    the_person "Ah!"
    $ the_person.change_arousal(20)
    "You give her ass a solid spank, then grope it gingerly."
    "You slide your fingers down her crack to her slit. You give it some attention as she pulls the game up."
    "When she finishes pulling up the game, you see a couple of people in a bedroom together."
    the_person "Alright, get ready..."
    if persistent.always_ask_condom or the_person.effective_sluttiness("condomless_sex") < the_person.get_no_condom_threshold() + 50 or the_person.has_taboo("condomless_sex"):
        $ condom_threshold = the_person.get_no_condom_threshold()
        if the_person.has_breeding_fetish or breeding_fetish_intro:
            the_person "Don't even think about wearing a condom. Hopefully the game has you finish deep inside of me..."
            $ the_person.change_arousal(10)
            $ mc.change_locked_clarity(20)
            if the_person.knows_pregnant:
                the_person "Besides, I'm already pregnant anyways. Isn't it just better without those stupid things?"
            else:
                the_person "Oh god what if you knocked me up like that... that would be so hot!"
            "[the_person.possessive_title] rubs her belly absent mindedly."
        elif the_person.effective_sluttiness() < condom_threshold:
            the_person "Do you need a condom? I have some extra if you don't have any."
            the_person "And yes. You NEED to have one."
            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_01
        elif the_person.get_opinion_score("bareback sex") < 0 or the_person.effective_sluttiness("condomless_sex") < condom_threshold + 20 or the_person.has_taboo("condomless_sex"):
            the_person "You... you need to wear a condom."
            the_person "I mean, who knows how the game will have you finish... it'll be safer if the finale has you finish inside me..."
            call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_02
        elif the_person.is_dominant and the_person.get_opinion_score("bareback sex") > 0:
            the_person "Don't even think about wearing a rubber. It feels way too fucking good when your hot cock is inside me bare..."
            if the_person.get_opinion_score("creampies"):
                the_person "Besides, what if the game has you cum inside me? Wouldn't it feel good to dump a hot load inside of me?"
        else:
            if the_person.knows_pregnant:
                the_person "I'm already pregnant, but I guess if you REALLY want to you could put a condom on..."
            else:
                the_person "Do you want to put a condom on? I have one if you need one."
                the_person "It doesn't matter to me though, you can go bare if you really want to."
            menu:
                "Put on condom":
                    mc.name "I think a condom is a good idea."
                    call put_on_condom_routine(the_person) from _call_put_on_condom_routine_myra_gaming_session_03

                "Fuck her raw":
                    mc.name "No arguments here."
    else:
        "[the_person.possessive_title] doesn't bring up anything about a condom, so you don't even bother."
    the_person "Alright! Here we go. Remember to tell me when you are getting ready to finish, and however they finish in game is what we'll do, okay?"
    "[the_person.title] holds up a small wireless mouse."
    the_person "All I have to do is click this and it will make them finish, with a random cumshot. Ready?"
    mc.name "Let's do it."

    while mc.arousal_perc < 100 and mc.energy > 20 and the_person.energy > 20:
        $ current_position = get_random_from_list(myra_random_positions)
        "The sims start a new position."
        $ renpy.say(None, myra_random_positions_desc[current_position.name])
        "You look at [the_person.possessive_title]."

        $ current_position.redraw_scene(the_person)
        $ renpy.say(None, myra_random_positions_intro[current_position.name])
        $ current_position.call_scene(the_person, gaming_cafe, myra_random_positions_obj[current_position.name])
        $ the_person.change_arousal(current_position.girl_arousal * (1.0 + 0.1 * mc.sex_skills[current_position.skill_tag]))
        $ mc.change_arousal(current_position.guy_arousal * (1.0 + 0.1 * the_person.sex_skills[current_position.skill_tag]))
        $ mc.change_locked_clarity(100)
        $ the_person.change_energy(-current_position.girl_energy, add_to_log = False)
        $ mc.change_energy(-current_position.guy_energy, add_to_log = False)
        if the_person.arousal_perc >= 100:
            if report_log.get("girl orgasms", 0) == 0:
                the_person "Oh fuck, [the_person.mc_title], I'm cumming!"
            else:
                the_person "Fuck me [the_person.mc_title], I'm cumming again!"
            $ the_person.have_orgasm(half_arousal = False, force_trance = True, sluttiness_increase_limit = current_position.slut_requirement, reset_arousal = False)
        if mc.arousal_perc < 100:
            "The sims start to change positions, so you pull your cock out of [the_person.possessive_title] and get ready for the next round."
    if mc.arousal_perc < 100 and the_person.energy > 20:    #Too tired
        "You try to follow the next round, but you are just too tired."
        mc.name "I'm sorry, I just can't keep going..."
        "[the_person.possessive_title] looks disappointed but understands."
        the_person "I wanted you to cum, but I understand, it IS getting pretty late."
        return False
    elif mc.arousal_perc < 100:  #SHE wore out. Give the option to prone bone her.
        "[the_person.possessive_title] puts her hands out and stops you before you can continue the next position."
        the_person "I'm sorry, I'm completely worn out. Can we stop?"
        call prone_decision_label(the_girl = the_person, the_location = gaming_cafe, the_object = make_couch(), the_position = current_position) from _prone_sex_myra_takeover_01
        if _return:
            call fuck_person(the_person, private= True, start_position = prone_bone, start_object = make_couch(), skip_intro = True, position_locked = True, report_log = None, affair_ask_after = False, skip_condom = True) from _myra_submissive_finish_01
            "You slowly stand up, the exhausted [the_person.possessive_title] laying face down on the couch."
            return True
        else:
            mc.name "That's fine, I'm a little worn out as well."
            return False
    else:   #MC is cumming
        $ cum_target = None
        mc.name "Fuck. I'm gonna cum!"
        $ cum_target = get_random_from_list(["cum_inside", "face", "tits", "ass", "swallow"])
        if breeding_fetish_intro or (the_person.has_breeding_fetish and renpy.random.randint(0,100) < 60): #60 chance she makes you cum inside if she has a breeding fetish.
            "Suddenly, the wireless mouse she was holding clatters across the floor."
            the_person "Ohhhh noooooo. I dropped the mouse. Guess you'd better just cum inside me then!"
            "Her voice is thick with lust and need. She obviously dropped it on purpose."
            "That's fine with you though, time to breed this slut!"
            $ cum_target = "cum_inside_breeding"
        else:
            "You hear [the_person.possessive_title] click the mouse. You look over at the screen to see how the sims finish."
        if cum_target == "cum_inside":
            "You watch as the sims keep going at it. The male sim moans and it is clear that he is finishing inside the female sim."
            if the_person.has_breeding_fetish or breeding_fetish_intro:
                the_person "Oh fuck yes cum inside me [the_person.mc_title]!!!"
                if the_person.knows_pregnant:
                    the_person "Flood my womb with your seed! Over and over!"
                else:
                    the_person "Knock me up and make me your cow! Cum inside me over and over until we make a baby!"
            elif the_person.wants_creampie:
                the_person "Oh my god, cum inside me [the_person.mc_title]!"
            elif mc.condom:
                the_person "That's it, cum inside me [the_person.mc_title]!"
            else:
                the_person "Oh fuck... is this really happening?"
            mc.name "Oh fuck, get ready!"
            $ renpy.say(None, myra_random_positions_cum_inside_desc[current_position.name])
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            if mc.condom:
                $ the_person.call_dialogue("cum_condom")
                "You cum. Wave after wave captured by the condom."
            else:
                $ the_person.call_dialogue("cum_vagina")
                $ the_person.cum_in_vagina()
                $ current_position.redraw_scene(the_person)
                "You fire wave after wave of cum into [the_person.possessive_title]'s unprotected cunt."
            "Neither of you move for several seconds. Eventually though, your cock starts to get too soft to stay inside her, so you slowly pull apart."
            if the_person.has_breeding_fetish or breeding_fetish_intro:
                if current_position == missionary:
                    "As you pull off her, [the_person.title] lifts her legs up a bit, angling her hips up to keep your cum inside."
                else:
                    the_person "Hang on!..."
                    $ the_person.draw_person(position = "missionary")
                    "[the_person.possessive_title] lays down on the couch, then lifts her legs, angling her hips up to keep as much cum inside as possible."
                "You stand up and look down at your cum drunk breeding stock."
                $ the_person.change_happiness(20)
                if breeding_fetish_intro:
                    return
                else:
                    the_person "Fuck, another load of your fertile cum..."
            else:
                $ the_person.draw_person()
                "You both stand up."
                if mc.condom:
                    the_person "Wow, that thing looks full... that's just impressive."
                    $ the_person.change_obedience(2)
                    $ mc.condom = False
                else:
                    "Your cum is slowly dripping down the inside of her legs."

                    if the_person.wants_creampie:
                        the_person "Wow... that was so good..."
                    else:
                        the_person "Oh my god... I can't believe I let that go so far..."
                        "She looks a little concerned, but there isn't much she can do about it now."
        elif cum_target == "cum_inside_breeding":
            "You growl at [the_person.possessive_title]."
            mc.name "Get ready slut! I'm about to fill you up like a bitch in heat!"
            the_person "Oh fuck yes cum inside me [the_person.mc_title]!!!"
            if the_person.knows_pregnant:
                the_person "Flood my womb with your seed! Over and over!"
            else:
                the_person "Knock me up and make me your cow! Cum inside me over and over until we make a baby!"
            $ renpy.say(None, myra_random_positions_cum_inside_desc[current_position.name])
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            $ the_person.call_dialogue("cum_vagina")
            $ the_person.cum_in_vagina()
            $ current_position.redraw_scene(the_person)
            "You fire wave after wave of cum into [the_person.possessive_title]'s unprotected cunt."
            "Neither of you move for several seconds. Eventually though, your cock starts to get too soft to stay inside her, so you slowly pull apart."
            if current_position == missionary:
                "As you pull off her, [the_person.title] lifts her legs up a bit, angling her hips up to keep your cum inside."
            else:
                the_person "Hang on!..."
                $ the_person.draw_person(position = "missionary")
                "[the_person.possessive_title] lays down on the couch, then lifts her legs, angling her hips up to keep as much cum inside as possible."
            "You stand up and look down at your cum drunk breeding stock."
            $ the_person.change_happiness(20)
            if breeding_fetish_intro:
                return
            else:
                the_person "Fuck, another load of your fertile cum..."

        elif cum_target == "face":
            "You watch as the female sim suddenly gets on her knees. The screen zooms in a bit as the male sim starts spraying her face down with cum."
            if the_person.opinion_score_cum_facials() < 0:
                the_person "Oh god... I didn't think it would go this way..."
            elif the_person.opinion_score_cum_facials() > 0:
                the_person "Oh fuck that looks hot!"
            else:
                the_person "Oh fuck on my face? Okay..."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] gets on her knees as you stand up."
            if mc.condom:
                "She quickly pulls your condom off and starts to stroke you, pointing it at her face."
                $ mc.condom = False
            else:
                "She grabs your cock and starts to stroke it eagerly, pointing it at her face."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
            if the_person.opinion_score_cum_facials() > 0:
                "[the_person.title] sticks out her tongue for you and holds still, eager to take your hot load."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            else:
                "[the_person.title] closes her eyes and waits patiently for you to cum."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
            "You take a deep breath to steady yourself once you've finished cumming. [the_person.title] looks up at you from her knees, face covered in your semen."
            $ the_person.call_dialogue("cum_face")
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "tits":
            "You watch on the screen as the male pulls out of the female. She lays down on the bed on her back and he sprays down her tits with cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. On my tits? Typical..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "Oh fuck, cover my tits in your hot cum [the_person.mc_title]!"
            else:
                the_person "Mmm, time to cum on my tits, [the_person.mc_title]!"
            if current_position == missionary:
                "You pull out of [the_person.title] and move up the couch. She grabs your cock and starts to stroke you."
            else:
                $ the_person.draw_person(position = "missionary")
                "[the_person.title] throws herself down on the couch on her back and looks up at you."
                "You quickly get on top of her waist and she strokes you eagerly."
            if mc.condom:
                "[the_person.possessive_title] pulls your condom off just in time."
                $ mc.condom = False
            $ the_person.cum_on_tits()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            $ the_person.draw_person(position = "missionary")
            "You watch as your cum coats [the_person.title]'s tits with spurt after spurt of cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. It feels so sticky..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "God, your seed feels so fucking hot..."
                "[the_person.title] licks her fingers clean."
            else:
                the_person "Mmm, that's it [the_person.mc_title], let it all out..."
            "After several seconds, you look down at [the_person.possessive_title]. Her tits are coated in your spunk."
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "ass":
            "You watch on the screen as the male pulls out of the female. The screen zooms in as he bends her over the bed and starts to cum all over her ass"
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. On my ass? Fine..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "Oh fuck, cover my ass in your hot cum [the_person.mc_title]!"
            else:
                the_person "Mmm, time to cum on my ass, [the_person.mc_title]!"
            if current_position == standing_doggy or current_position == doggy:
                "You pull out of [the_person.title]."
            else:
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.title] bends over the couch and you get behind her."
            if mc.condom:
                "You pull your condom off and start to stroke yourself."
                $ mc.condom = False
            "[the_person.possessive_title] wiggles her ass back at you as you start to cum."
            $ the_person.cum_on_ass()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            $ the_person.draw_person(position = "standing_doggy")
            "You watch as you coat [the_person.title]'s ass with spurt after spurt of cum."
            if the_person.opinion_score_being_covered_in_cum() < 0:
                the_person "Ugh. It feels so sticky..."
            elif the_person.opinion_score_being_covered_in_cum() > 0:
                the_person "God, your seed feels so fucking hot..."
            else:
                the_person "Mmm, that's it [the_person.mc_title], let it all out..."
            "After several seconds, you look down at [the_person.possessive_title]. Her ass is coated in your spunk."
            $ the_person.draw_person()
            "You both stand up."
        elif cum_target == "swallow":
            "You look at the screen. The female sim gets on her knees and takes the male in her mouth as he cums. The virtual character makes loud slurping and gulping noises as she swallows it down."
            if the_person.opinion_score_drinking_cum() < 0:
                the_person "Shit, why did I say I would do this!..."
            elif the_person.opinion_score_drinking_cum() > 0:
                the_person "Oh fuck, I'm ready for it, let me drink your cum!"
            else:
                the_person "Ah, I guess it is time to swallow it for you [the_person.mc_title]..."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] gets on her knees as you stand up."
            if mc.condom:
                "She quickly pulls your condom off. She opens her mouth and takes the tip while stroking the shaft with her hand."
                $ mc.condom = False
            else:
                "She opens her mouth and takes the tip, while she strokes your shaft with her hand rapidly..."
            "After a couple strokes, you explode, dumping your cum into [the_person.possessive_title]'s mouth. Some of it drips down her chin."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
            $ the_person.draw_person(position = "blowjob")
            if the_person.opinion_score_drinking_cum() < 0:
                "When you finish, [the_person.possessive_title] looks up at you. Her face isn't pleasant."
                mc.name "Come on now. You saw the screen. Swallow like a good girl."
                $ the_person.change_obedience(5)
                $ play_swallow_sound()
                "She gives you a middle finger, but eventually swallows, then gags a little and makes a face."
                the_person "Fuck, I hate doing that. You're a lucky son of a bitch, you know that?"
            elif the_person.opinion_score_drinking_cum() > 0:
                $ play_swallow_sound()
                "As you cum [the_person.possessive_title] eagerly drinks every drop."
                mc.name "Damn. What a good girl, swallowing my cum like that."
                $ the_person.change_obedience(5)
                the_person "Mmm, it helps that you taste so good sir..."
            else:
                "You look down when you are finished. [the_person.possessive_title] still has the tip in her mouth."
                mc.name "Good girl. Now swallow."
                $ the_person.change_obedience(5)
                $ play_swallow_sound()
                "[the_person.title] grimaces a bit, but dutifully swallows your cum."
                the_person "Mmm, that wasn't so bad."
            "You take a deep breath to steady yourself. [the_person.title] looks up at you from her knees, a bit of your cum still on her chin."
            $ the_person.draw_person()
            "You both stand up."
    $ mc.condom = False
    $ del cum_target
    $ del current_position
    return True
