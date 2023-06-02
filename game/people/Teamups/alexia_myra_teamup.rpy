#Myra and Alexia teamup scene! Myra invites Alexia over for a game night.
#Happens on Friday nights because that's the only night that makes actual logical sense to have an all night gaming session
#Unfortunately this conflicts with dates so probably lots of QQ
#Oh well. Progression is similar to Myra's focus practice.
#Mc shows up to game night, but girls are playing a two player only game.
#Girls wager that winner gets a back rub. MC agrees. Myra wins, but they agree to make it a weekly thing and invite MC back anytime
#During recurrent, reward progression goes to...
#Back rub - fingering - oral servicing - Full service - Free Use
#

# 16/25
init 1 python:
    def myra_alexia_teamup_scene_0_req():    #Requirements for the basic scene. Should almost always be true.
        return True

    def myra_alexia_teamup_scene_1_req():    #Requirements for the second stage.
        if myra.has_taboo("touching_vagina") or alexia.has_taboo("touching_vagina"):
            return False
        if myra.opinion_score_being_fingered() >-2 and alexia.opinion_score_being_fingered() >-2:
            if myra.sluttiness >= 40 and alexia.sluttiness >= 40:
                return True
        return False

    def myra_alexia_teamup_scene_2_req():
        if myra.has_taboo("licking_pussy") or alexia.has_taboo("licking_pussy"):
            return False
        if myra.opinion_score_getting_head() >-2 and alexia.opinion_score_getting_head() >-2:
            if myra.sluttiness >= 60 and alexia.sluttiness >= 60:
                return True
        return False

    def myra_alexia_teamup_scene_3_req():
        if myra.has_taboo("vaginal_sex") or alexia.has_taboo("vaginal_sex"):
            return False
        if myra.opinion_score_vaginal_sex() >-2 and alexia.opinion_score_vaginal_sex() >-2:
            if myra.sluttiness >= 80 and alexia.sluttiness >= 80 and willing_to_threesome(myra, alexia):
                return True
        return False

    def myra_alexia_teamup_scene_4_req():    #Not yet full implemented, leave false for now.
        if myra.is_free_use and alexia.is_free_use:
            return True
        return False


    def myra_alexia_teamup_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        if day%7 == 4 and time_of_day == 4:
            return True
        return False

    def myra_alexia_teamup_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(20)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def myra_alexia_teamup_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["myra_alexia_teamup_scene_intro_0", "myra_alexia_teamup_scene_intro_1", "myra_alexia_teamup_scene_intro_2", "myra_alexia_teamup_scene_intro_3", "myra_alexia_teamup_scene_intro_4"]
        the_progression_scene.req_list = [myra_alexia_teamup_scene_0_req, myra_alexia_teamup_scene_1_req, myra_alexia_teamup_scene_2_req, myra_alexia_teamup_scene_3_req, myra_alexia_teamup_scene_4_req]
        the_progression_scene.trans_list = ["myra_alexia_teamup_trans_scene_0", "myra_alexia_teamup_trans_scene_1", "myra_alexia_teamup_trans_scene_2", "myra_alexia_teamup_trans_scene_3", "myra_alexia_teamup_trans_scene_4"]
        the_progression_scene.final_scene_list = ["myra_alexia_teamup_scene_scene_0", "myra_alexia_teamup_scene_scene_1", "myra_alexia_teamup_scene_scene_2", "myra_alexia_teamup_scene_scene_3", "myra_alexia_teamup_scene_scene_4"]
        the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    myra_alexia_teamup_scene_action = Action("Myra and Alexia's Game Night", myra_alexia_teamup_scene_action_req, "myra_alexia_teamup_scene_action_label")

    def myra_alexia_teamup_scene_init():  #Run this during init only
        global myra_alexia_teamup_scene
        myra_alexia_teamup_scene = Progression_Scene(
            compile_scenes = myra_alexia_teamup_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "myra_alexia_teamup_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "myra_alexia_teamup_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = myra_alexia_teamup_scene_action,      #The action used to call for this progression scene.
            choice_scene = "myra_alexia_teamup_scene_choice_label",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = True,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = myra_alexia_teamup_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        myra_alexia_teamup_scene.compile_scenes(myra_alexia_teamup_scene)   #This will populate the scenes that are blank above.

        return

label myra_alexia_teamup_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: myra_alexia_teamup_scene_action_label():
    $ mc.change_location(gaming_cafe)
    #"Test, is this working"
    call progression_scene_label(myra_alexia_teamup_scene, [the_person, alexia]) from _myra_alexia_teamup_scene_call_test_01
    return

label myra_alexia_teamup_scene_intro_scene(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "Walking through the mall, nearly everything is closing down. It is a bit of a ghost town as you make your way to the gaming cafe."
    "You step inside, and hear a familiar voice calling out to you."
    the_person "Hey, sorry we are just closing up, you'll have to come another time..."
    $ scene_manager.add_actor(the_person)
    "[the_person.possessive_title] suddenly appears from around a group of desks."
    the_person "Oh hey [the_person.mc_title]. Did you need something?"
    alexia "[alexia.mc_title] is here?"
    "You hear [alexia.possessive_title] call out from the back of the cafe. [the_person.title] has a couple couches and some retro consoles set up back there."
    mc.name "I knew you two were gonna hang out tonight, just thought maybe I'd swing by for a bit."
    the_person "Oh... I suppose we could all hang out for a bit. Hey [alexia.fname]! Do you care if he hangs out with us some?"
    alexia "Sure! Let's put him to work though. The food court is probably almost closed, can you go get me a milkshake?"
    the_person "Ooooh! That sounds good! Get me one too!"
    mc.name "Ummm, sure... what flavors?"
    alexia "Strawberry!"
    the_person "Chocolate for me..."
    mc.name "Okay, I'll be right back with those."
    the_person "Sounds good. Do me a favor, I'll leave the door unlocked but closed behind you. When you get back can you lock up behind you?"
    mc.name "Yeah I can do that."
    the_person "Great!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns and walks back towards the couches. "
    $ scene_manager.clear_scene()
    "You walk down to the food court. Most places are closing up, but a few are still open."
    "Luckily, the stand that sells milkshakes is still open. You purchase a strawberry and a chocolate and head back towards the gaming cafe."
    $ mc.business.change_funds(-10)
    "As you walk back to the cafe, you look around. The mall is deserted... maybe you should slip a couple serums in the milkshakes?"
    "You look at [the_person.possessive_title]'s drink."
    call give_serum(the_person) from _call_give_myra_serum_teamup_01
    "You look at [alexia.possessive_title]'s drink."
    call give_serum(alexia) from _call_give_alexia_serum_teamup_02
    "When you get back to the cafe, you step inside and lock the door behind you."
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing an old game together."
    mc.name "I've got milkshakes!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "The girls seem thankful for their drinks. You sit down on the couch next to [the_person.title] and watch as the girls play."
    "They are playing a fighting game where the character's look like they are made of clay. A match is just getting ready to start."
    the_person "Are you okay just watching? This game is only two player... maybe we play it where winner stays on?"
    mc.name "That's okay, I'm fine with just watching and hanging out with you two."
    $ alexia.change_love(1, 50)
    $ the_person.change_love(1,50)
    alexia "Aww, that's sweet of you. Alright [the_person.fname], you're mine!"
    "Round one starts, but it is clear that [the_person.possessive_title] is the better gamer. After two quick rounds, the game declares her as the winner."
    the_person "Yes!"
    alexia "Geeze! You just going to sit there and watch this slaughter [alexia.mc_title]? Or are you going to help me?"
    mc.name "Help? By doing what?"
    alexia "I don't know... distract her or something!"
    the_person "Oh! That's a good idea! Do that thing we did the other day, [the_person.mc_title]."
    alexia "Thing?"
    the_person "Yeah, he is helping me train my focus while playing games by giving me backrubs. It makes it hard to play when you are feeling relaxed."
    the_person "His hands are amazing though, so it helps me learn to focus, and at the same time it feels great..."
    "You glance at [alexia.title] and see a hint of jealousy in her face..."
    alexia "Ahh... yeah... I just didn't realize you two were getting to be so friendly I guess..."
    "[the_person.possessive_title] blushes a little but tries to deflect."
    the_person "It's not like that! He's just like... being my coach or something..."
    "The room is getting awkward."
    mc.name "Hey, I've got an idea, just to make this fair. How about whoever wins a match, during the next I'll give the winner a back rub."
    alexia "Yeah! That's a great idea!"
    the_person "Yeah! Can't wait to have your hands on me all night!"
    $ mc.change_locked_clarity(10)
    "[the_person.title] sticks her tongue out at [alexia.possessive_title], teasing her."
    alexia "Ha! As if! It's time to bring out my secret weapon... Frosty!"
    "[alexia.title] selects the snowman clay fighter on the screen. You scoot over close to [the_person.title] as she selects the scarecrow themed fighter."
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = .2, zoom = 1.2))
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
    "[the_person.possessive_title] sighs when you put your hands on her shoulders. You can already feel her relaxing as [alexia.title] selects an arena."
    "TV" "Round one. Fight!"
    "You are only half paying attention to the game as you massage [the_person.possessive_title]'s neck and shoulders."
    "She gets tense for a second as she tries to pull off a combo, but your hands dig in and she sighs."
    the_person "Mmnnff..."
    "A small moan escapes her lips. [alexia.possessive_title] glances over and notices she is distracted."
    "She quickly strings together a combo before [the_person.title] can react, and soon the round is over."
    the_person "Ah! Hey!"
    alexia "Yes! Lookout girl, I need a backrub too!"
    the_person "I don't think so!"
    "TV" "Round two. Fight!"
    "[the_person.possessive_title] jumps out aggressively. She gets in a few good hits, so you double down and press hard under her shoulder blades."
    the_person "Oh! Mmmm..."
    $ the_person.change_arousal(10)
    "There is a definite pleasurable tone to her gasp as you work on her back. [alexia.possessive_title] looks over and flashes you a big smile."
    "[alexia.title] runs another combo, dropping [the_person.possessive_title]'s health by over half."
    the_person "No! [the_person.mc_title] stop for just a second I'm not ready for you to be done yet!"
    "Unwilling to play fairly, you keep kneading her back."
    "[the_person.title] tries holding the block button, just trying to prolong the match as long as she can."
    "[alexia.possessive_title] quickly catches on, jumps over her character and uses a grab move."
    "TV" "Player two wins!"
    $ scene_manager.update_actor(alexia, position = "stand3")
    "[alexia.title] jumps up."
    alexia "YES!!!"
    the_person "No!"
    alexia "Get your ass over here [alexia.mc_title]! From the noises she was making, those hands must be magical!"
    "You move over next to [alexia.title]."
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
    $ scene_manager.update_actor(alexia, position = "sitting", display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
    "You start to rub [alexia.possessive_title]'s back as the girls get ready to play another round. She let's out an exaggerated moan."
    alexia "MMMM that feels AMAZING [alexia.mc_title]!"
    $ mc.change_locked_clarity(10)
    if alexia.is_single or alexia.is_girlfriend:    #
        $ the_person.event_triggers_dict["knows_alexia_single"] = True
        the_person "Wow, should I give you two some privacy?"
        if alexia.sluttiness > 20:
            alexia "Wow, you would do that? You're such a good friend [the_person.fname]!"
        else:
            alexia "Just teasing, geesh! No need to take it so far."
        "[the_person.title] rolls her eyes."
    else:
        # $ so_title = SO_relationship_to_title(alexia.relationship)
        $ the_person.event_triggers_dict["knows_alexia_single"] = False
        the_person "Wow, does your boyfriend know you're out getting backrubs from strange men tonight [alexia.fname]?"
        "[alexia.title] rolls her eyes."
        alexia "What he doesn't know won't hurt him..."
        $ alexia.change_slut(1, 50)
        "You are a little surprised by her words. You wonder how far you'll be able to take things in the future at these gaming sessions with [alexia.title]..."
    "The match starts, but [alexia.possessive_title] doesn't even bother trying to win."
    "She guards, counters and plays defensively, just trying to prolong the match."
    the_person "Seriously? This is how its gonna be huh?"
    alexia "Mmmff... Hey you started it..."
    $ alexia.change_arousal(10)
    "[alexia.title] groans as you work on her shoulders. You think hear a gasp even."
    "[alexia.possessive_title] successfully drags the match out for several minutes, but eventually it's over."
    "TV" "Player one wins!"
    the_person "Yes!"
    alexia "Arg... five more minutes?"
    the_person "Not a chance! Get over here magic hands!"
    $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = .2, zoom = 1.2))
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
    "You scoot back over next to [the_person.title]."
    "For a while, you massage the backs of the two girls as they play games. Once in a while [alexia.possessive_title] wins, but you spend most of your time with [the_person.title]."
    alexia "Damn! I hate this game! I need a break."
    the_person "Me too. I have snacks, let me go grab some."
    mc.name "I think it is time for me to head out. You two have fun tonight."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose, display_transform = character_right(yoffset = 0, zoom = 1))
    $ scene_manager.update_actor(alexia, position = alexia.idle_pose, display_transform = character_center_flipped(yoffset = 0, zoom = 1))
    "When you stand up, so do both girls."
    alexia "Okay, I lied. That was super fun. I just need to get better."
    the_person "Yeah, honestly it is really nice playing a different game for a change too. We should do this more often!"
    alexia "How about next week? [alexia.mc_title] could come by if he wants too!"
    the_person "Oh! That's a great idea! Friday night, game night!"
    mc.name "That sounds great! I can't promise I'll be here every Friday, but I'll try to swing by when I can."
    the_person "Neat! Can you let yourself out? The door should lock itself."
    mc.name "Certainly. Goodnight girls, have a good night!"
    alexia "Bye!"
    $ scene_manager.clear_scene()
    "You let yourself out and head home."
    $ mc.change_location(bedroom)
    "The friendship between [the_person.title] and [alexia.possessive_title] seems to be in good health. And this Friday night appointment seems to be a great opportunity."
    "You are pretty sure that if you offer to grab milkshakes for the girls, you can probably continue to test serums on them... you wonder how far you can push things at Friday Night game night!"
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] is getting ready to close up."
    $ scene_manager.add_actor(the_person)
    the_person "Oh hey [the_person.mc_title]. We are having another game night!"
    mc.name "We?"
    alexia "Hey!"
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.possessive_title] suddenly stands up from a couch and walks over."
    alexia "[alexia.mc_title]! Couldn't stay away from gamer girl's night could you?"
    the_person "Here to rub my back all night?"
    alexia "Hey now, he only rubs the WINNER's back!"
    "[the_person.title] sticks out her tongue, then retorts."
    the_person "I know."
    alexia "Hey, I've been practicing!"
    the_person "Sure, sure."
    "You can feel some friendly competition in the air."
    return

label myra_alexia_teamup_scene_intro_1(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.title] notices you first."
    alexia "Oh hey! Excuse me sir we are closing up for the night!"
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_2(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up. They don't notice you right away..."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    # if alexia.is_employee:
    alexia "Yeah, well... let's just say working there has been... interesting."
    "[the_person.title] looks up an notices you. She quickly elbows [alexia.title]."
    the_person "Hey! You're here! We were wondering if you would be swinging by."
    alexia "Hoping, even."
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_3(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You step into the gaming cafe. It looks like [the_person.title] and [alexia.possessive_title] are chatting as they close up."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    "[alexia.title] notices you right away. It's almost like they were waiting for you?"
    alexia "Yes! You're here!"
    the_person "Told you he couldn't stay away. A couple hot bitches like us, who could?"
    "She gives you a big wink."
    return

label myra_alexia_teamup_scene_intro_4(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    "You go to the gaming cafe. As you try to enter the door though, it is already locked. Are you late?"
    "You knock on the door. Suddenly a figure appears in the doorway."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.strip_full_outfit(the_person, delay = 0)
    $ mc.change_locked_clarity(40)
    "She quickly opens the door and you step inside."
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped)
    $ scene_manager.strip_full_outfit(alexia, delay = 0)
    "[alexia.title] is also inside. The state of the girls dress leaves you speechless."
    $ mc.change_locked_clarity(40)
    alexia "Hey [alexia.mc_title]! I've been looking forward to game night all week!"
    the_person "Yeah, me too!"
    "The girls both give you big smiles."
    return

#For more progression, add more scenes.

label myra_alexia_teamup_scene_scene_0(the_group, scene_transition = False):  #Massages
    $ the_person = the_group[0]
    $ current_round = 1
    $ round_count = 1
    $ myra_wins = 0
    $ alexia_wins = 0
    $ the_target = None
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
    mc.name "Milkshake time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "The girls seem thankful for their drinks."
    "As the girls get ready to play, you check your watch. It is already pretty late, but you want to watch enough matches to at least declare a winner."
    "How many wins will it take to win tonight?"
    "NOTE: the larger the number, the longer the event."
    menu:
        "1":
            pass
        "2":
            $ round_count = 2
        "3":
            $ round_count = 3

    alexia "Same rules as last time, right? Winner gets a back massage during the next round?"
    the_person "Sure, but I think we should put him to work right away. Why don't you sit down next to me and start that massage now? It'll be like a handicap."
    alexia "Hey, that's not fair! You should start with me, [alexia.mc_title]!"
    "Which girl do you want to sit next to first?"
    menu:
        "[myra.title]":
            $ the_target = myra
        "[alexia.title]":
            $ the_target = alexia

    "You sit down next to [the_target.possessive_title]. You think you see a hint of jealousy in the other girl's eyes, but it quickly vanishes as the game starts up."
    while myra_wins < round_count and alexia_wins < round_count:
        #Get close to the target
        if the_target == myra:
            $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
        else:
            $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "The character select screen comes up, and you get close to [the_target.title], ready to begin your back massage."
        call myra_alexia_teamup_fight_round_label(the_group, (the_target == myra)) from _myra_alexia_back_massage_round_call_01
        if _return == myra:
            $ myra_wins += 1
            $ the_target = myra
            if the_target.arousal_perc >= 30:
                myra "Yes! I win again! This is the best night ever! Your hands feel amazing [myra.mc_title]!"
                $ mc.change_locked_clarity(10)
            else:
                myra "Yes! I could use a good back massage."
        else:
            $ alexia_wins += 1
            $ the_target = alexia
            if the_target.arousal_perc >= 30:
                alexia "Oh my god... I won again? This is great!"
                $ mc.change_locked_clarity(10)
            else:
                alexia "Yay! You give great massages, [alexia.mc_title]!"

    if alexia_wins >= round_count:
        "It's over. [alexia.possessive_title] is the winner for the night."
        $ the_target = alexia
    else:
        "It's over. [myra.possessive_title] is the winner for the night."
        $ the_target = myra
    mc.name "Alright girls, I need to get going soon, but I also don't want to go without giving the final winner her reward."
    if the_target == myra:
        mc.name "[alexia.title], why don't you grab some snacks for you two while I work on [myra.title] for a bit?"
        alexia "Fine. I need to use the ladies room anyway... just don't do anything too crazy while I'm gone you two!"
        myra "No promises!"
        # if alexia.is_employee:
        alexia "[alexia.mc_title], I'll see you at work next week, okay?"
        mc.name "Bye [alexia.title]."
        "The girls laugh, but [alexia.possessive_title] gets up and heads towards the restroom."
        $ scene_manager.remove_actor(alexia)
    else:
        mc.name "[myra.title], why don't you grab some snacks for you two while I work on [alexia.title] for a bit?"
        myra "Damn. Beat at games in my own gaming cafe. Fine! I think I'm going to heat up a frozen pizza I got in the back."
        "[myra.possessive_title] starts to get up, but then stops and looks at you."
        myra "Don't do anything too crazy while I'm gone... or I'll send you the cleaning bill!"
        alexia "[myra.name]!"
        "You and [myra.title] share a good laugh at [alexia.possessive_title]'s expense."
        myra "See ya around [myra.mc_title]."
        mc.name "Bye [alexia.title]."
        "[myra.possessive_title] gets up and heads towards the kitchen area."
        $ scene_manager.remove_actor(myra)
    "You scoot back over next to [the_target.title]."
    the_target "Hey, I got an idea. I'm going to lay on my stomach and just relax, okay?"
    mc.name "Sure, sounds good."
    $ scene_manager.update_actor(the_target, position = "walking_away")
    "You gently sit on [the_target.title]'s back, leaning forward as you begin your work on her back." # not sure we are sitting on her back. Straddling her legs?
    the_target "Ahhh, sweet victory."
    "You spend a while just rubbing and caressing her back. She sighs and coos as your massage her."
    $ the_target.change_love(2, 60)
    if the_target.opinion_score_being_fingered() == -2:
        the_target "God your hands are amazing... I wonder if they would actually feel good... if you..."
        "She is mumbling a bit under her breath."
        mc.name "Sorry... feel good doing what?"
        "[the_target.possessive_title] startles for a second."
        the_target "Ah! I mean ummm... Just like... you should do this more often..."
        $ the_target.increase_opinion_score("being fingered")
        "You have a feeling she meant something else..."
        $ mc.change_locked_clarity(10)
    "After a bit, it is definitely time to go."
    mc.name "Alright, well I need to get home. You have a good night, okay?"
    the_target "God that was so good. Is it okay if I don't get up?"
    mc.name "That is fine. I'll see myself out."
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    "There was a lot of tension in the air tonight between you and the two girls. You know you can push things between you and them farther with a little more time..."
    if myra.has_taboo("touching_vagina") or alexia.has_taboo("touching_vagina"):
        "You aren't sure that you will be able to convince the girls to do anything lewd when you haven't done much one on one yet."
        "You should make sure you've fingered each girl at least once before you try to make things go any farther..."
    elif myra.opinion_score_being_fingered() == -2:
        "You aren't sure that you will be able to manage it while [myra.title] hates getting fingered though..."
    elif alexia.opinion_score_being_fingered() == -2:
        "You aren't sure that you will be able to manage it while [alexia.title] hates getting fingered though..."
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_scene_1(the_group, scene_transition = False):  #Fingering
    $ the_person = the_group[0]
    $ current_round = 1
    $ round_count = 1
    $ myra_wins = 0
    $ alexia_wins = 0
    $ the_target = None
    if scene_transition != True:
        $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(the_person, position = "sitting")
        "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
        mc.name "Milkshake time!"
        alexia "Yay!"
        the_person "Hey, thanks [the_person.mc_title]!"
        $ the_person.change_happiness(5)
        $ alexia.change_happiness(5)
        "The girls seem thankful for their drinks."


        alexia "Same rules as last time, right? [alexia.mc_title] feels up the winner of each round during the next round?"
        the_person "Yeah! And don't forget the most important part. Winner gets off while the loser has to jack him off!"
        "Your cock twitches in your pants. You can't wait to get one of these girls' hands on your dick."
    "As the girls get ready to play, you check your watch. It is already pretty late, but you want to watch enough matches to fairly declare a winner."
    "How many wins will it take to win tonight?"
    "NOTE: the larger the number, the longer the event."
    menu:
        "1":
            pass
        "2":
            $ round_count = 2
        "3":
            $ round_count = 3
    "The girls look at you. Which girl do you want to sit next to first?"
    menu:
        "[myra.title]":
            $ the_target = myra
        "[alexia.title]":
            $ the_target = alexia

    "You sit down next to [the_target.possessive_title]. You think you see a hint of jealousy in the other girl's eyes, but it quickly vanishes as the game starts up."
    while myra_wins < round_count and alexia_wins < round_count:
        #Get close to the target
        if the_target == myra:
            $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
        else:
            $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "The character select screen comes up, and you get close to [the_target.title], your hands already running along her sides."
        call myra_alexia_teamup_fight_round_label(the_group, (the_target == myra)) from _myra_alexia_back_massage_round_call_02
        if _return == myra:
            $ myra_wins += 1
            $ the_target = myra
            if the_target.arousal_perc >= 60:
                "[myra.title] gazes at you, her face a little flushed."
                $ mc.change_locked_clarity(25)
                if myra.tits_available:
                    "Her nipples are hard, your hands have been on them a lot tonight."
                myra "I win again? God you are getting me so worked up..."
            elif the_target.arousal_perc >= 30:
                myra "Yes! I win again! Your hands feel amazing [myra.mc_title]!"
                $ mc.change_locked_clarity(15)
            else:
                myra "Yes! Get to work [myra.mc_title]!"
        else:
            $ alexia_wins += 1
            $ the_target = alexia
            if the_target.arousal_perc >= 60:
                "[alexia.title] gazes at you, she bites her lip."
                $ mc.change_locked_clarity(25)
                if myra.tits_available:
                    "Her nipples are hard, your hands have been on them a lot tonight."
                alexia "Oh god, I'm getting so hot... this feels amazing..."
            elif the_target.arousal_perc >= 30:
                alexia "Oh my god... I won again? This is great!"
                $ mc.change_locked_clarity(15)
            else:
                alexia "Yay! You give great massages, [alexia.mc_title]!"

    $ the_loser = None

    if alexia_wins >= round_count:
        "It's over. [alexia.possessive_title] is the winner for the night."
        $ the_target = alexia
        $ the_loser = myra
    else:
        "It's over. [myra.possessive_title] is the winner for the night."
        $ the_target = myra
        $ the_loser = alexia
    mc.name "Alright girls, time for the winner to get her reward!"
    if scene_transition:
        if the_target == myra:
            mc.name "[alexia.title], why don't you grab some snacks for you two while I work on [myra.title] for a bit?"
        else:
            mc.name "[myra.title], why don't you grab some snacks for you two while I work on [alexia.title] for a bit?"
        "[the_target.possessive_title] looks at you, noticing your sizable bulge..."
        the_target "Wait... I feel kind of bad."
        "[the_target.title] turns to the other girl."
        the_target "Look at him! He is turned on too. Is it really fair to leave him hanging?"
        "Suddenly, [the_target.title] gets a big smile."
        if the_target == myra:
            the_target "[alexia.fname], why don't you jack him off while he is touching me? Fitting end for the loser!"
            mc.name "That's okay, we didn't agree on that at the beginning..."
            alexia "I'll do it."
            mc.name "I... what?"
            alexia "She's right. That looks painful! It's only fair we let you touch us, and she DID win fair and square..."
            "Holy shit, you were not expecting this when the night started!"
        else:
            the_target "How about... I'll touch you too? We can touch each other, and get each other off..."
            mc.name "That's okay, we didn't agree on that at the beginning..."
            myra "I'll do it."
            mc.name "I... what?"
            the_target "Huh?"
            myra "I lost. Fair and square. It makes sense that the loser has to service him."
            mc.name "You don't have to..."
            myra "I know. But don't worry. You'll come back next week, right? All the more reason for me to focus and win next time!"
            "Holy shit, you were not expecting this when the night started!"
    "There's no easy way to do this, so you get positioned as best you can."
    $ scene_manager.update_actor(the_target, position = "missionary", display_transform = character_right(yoffset = .2, zoom = 1.2))
    "You sit down next to [the_target.possessive_title]. She spreads her legs a bit to give you access as your run your hand up and down the inside of her legs."
    $ scene_manager.update_actor(the_loser, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.4))
    "[the_loser.possessive_title] gets down on her knees between your legs. She pulls your pants and underwear off, and your cock springs out."
    the_target "Wow... you look so hard..."
    if the_target.vagina_available:
        "You run your fingers up and down [the_target.title]'s pussy. She is already excited."
    else:
        "You run your hand under [the_target.title]'s clothes, your fingers running along her pussy. She is already excited."
    if the_loser.opinion_score_giving_handjobs() == -2:
        the_loser "God your cock is so hot."
        "[the_loser.possessive_title] spits into her hands to help make some extra lube."
        the_loser "I never realized it would be so hard..."
        "She is mumbling a bit under her breath."
        $ the_loser.increase_opinion_score("giving handjobs")
        "You wonder if [the_loser.title] might be coming around to the idea of jacking you off..."
        $ mc.change_locked_clarity(20)
    else:
        "[the_loser.title] spits in her hand then strokes your cock, alternating a few times until you are lubed up."
        the_loser "God your cock is so hot..."
        "She looks up at you from her knees."
        the_loser "I almost don't mind losing, except I don't get off..."
        $ mc.change_locked_clarity(20)
    $ mc.change_arousal(20)
    $ the_loser.break_taboo("touching_penis")
    "You slide two fingers up into [the_target.title]'s cunt. She moans and bucks her hips, already worked up from your groping earlier."
    "Seeing that things have started, [the_loser.title] also gets to work. Her soft hands work their way up and down your cock."
    "You slide your fingers in and out of her pussy, stroking the inside of that soft tunnel."
    "Each movement draws moans of pleasure from [the_target.possessive_title], who looks over at you."
    the_target "Can... can we kiss too?"
    "Not seeing any harm in it, you move your neck forward. You lips meet with [the_target.title] as your fingers work her love tunnel."
    $ the_target.change_love(2, 80)
    $ the_target.break_taboo("kissing")
    "As you make out, [the_target.possessive_title] let's out little moans, which are really turning you on."
    "[the_loser.possessive_title] takes a moment to spit on her hand again, then keeps working your cock."
    if the_loser == myra:
        # $ so_title = SO_relationship_to_title(alexia.relationship)
        the_loser "Holy fuck you two... [alexia.fname] are you sure you have a boyfriend?"
        the_target "Quiet. I don't want to think about him right now..."
        $ mc.change_locked_clarity(20)
        "[the_target.title] is putty in your hands. It really doesn't matter who she gets with, does it? She seems to always come back to you."
    else:
        the_loser "God, you two are so hot together..."
        $ mc.change_locked_clarity(20)
        "[the_loser.title] is starting to touch herself, but you are pretty sure she knows better than to get herself off now."
    "[the_target.possessive_title]'s moans are getting urgent. She's going to cum soon!"
    the_target "Yes! Oh [the_target.mc_title]!"
    "Her whole body tenses up and a shiver runs through her body as she climaxes."
    $ the_target.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    $ the_target.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(50)
    "Getting [the_target.title] off has you hugely turned on. Each stroke of [the_loser.possessive_title]'s hand is bringing you closer to orgasm."
    "Partially recovered, [the_target.title] looks over at you."
    the_target "Getting close? You should cum all over her face! I want to watch you cover her face in cum!"
    "Hearing her encouragement is pushing you over the edge."
    mc.name "Oh fuck, I'm gonna cum!"
    "[the_loser.title] just looks up at you and speeds up, ready to accept the consequences of her poor gaming performance."
    "You moan as you finish. Spurt after spurt of your cum covers [the_loser.possessive_title]'s face."
    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_loser)
    $ the_loser.cum_on_face()
    $ scene_manager.update_actor(the_loser)
    "When you are finished, [the_loser.title] slowly opens her eyes and looks up at you and [the_target.title]."
    "You enjoy your post orgasm bliss with [the_target.possessive_title] for a bit."
    if the_target.opinion_score_cum_facials() <= 0 or the_target.opinion_score_being_covered_in_cum() <= 0:
        the_target "Oh my god... that looks so hot... is this why guys love cumming all over you?"
        mc.name "It looks hot, yeah, but part of it is also a masculine sense of... marking your territory I guess."
        the_target "Yeah... that makes sense..."
        "While normally not something she enjoys, you wonder if [the_target.title] might be more open to getting covered in your cum in the future..."
        $ the_target.increase_opinion_score("cum facials", max_value = 1)
        $ the_target.increase_opinion_score("being covered in cum", max_value = 1)
    else:
        the_target "Damn that's hot... maybe next time I should lose on purpose..."
        "[the_target.title] reaches down and wipes a finger through your cum, then brings it back to her mouth. She quietly sucks it off."
        the_target "Mmm..."
    $ mc.change_locked_clarity(50)
    $ the_target.change_slut(2, 65)
    $ the_loser.change_slut(2, 70)
    "Sadly, things seem to be winding down, and you aren't ready to push things with these two girls further yet."
    the_loser "Hey... can you get some snacks [the_target.name]? While I umm... go clean up..."
    the_target "Sure! [the_target.mc_title] do you want to have some?"
    mc.name "No, I need to get going. Thanks though."
    if scene_transition:
        the_loser "We are doing it this way from now on though... right?"
        the_target "Oh, want to get covered in cum again next week?"
        the_loser "Errr, no way! Of course not! But I wouldn't mind watching him cover you when I kick your ass!"

    else:
        the_loser "I can't wait until next week."
        the_target "Oh, want to get covered in cum again next week?"
        the_loser "No way! I mean... yeah but... I won't be! I'll be watching him cover you when I kick your ass!"
    "The girls start to play fight a little bit. It's cute, but you get up to leave."
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    "Things are progressing nicely with the two gamer girls. Obviously, you want to keep pushing things with them."
    "The next logical step is to move to oral sex..."
    if myra.has_taboo("licking_pussy") or alexia.has_taboo("licking_pussy"):
        "You aren't sure that you will be able to convince the girls to do anything lewd when you haven't done much one on one yet."
        "You should make sure you've eaten out each girl at least once before you try to make things go any farther..."
    if myra.opinion_score_getting_head() == -2:
        "You aren't sure that you will be able to manage it while [myra.title] hates getting head though..."
    elif alexia.opinion_score_getting_head() == -2:
        "You aren't sure that you will be able to manage it while [alexia.title] hates getting head though..."
    $ the_loser = None
    $ the_target = None
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_scene_2(the_group, scene_transition = False):  #Oral
    $ the_person = the_group[0]
    $ current_round = 1
    $ round_count = 1
    $ myra_wins = 0
    $ alexia_wins = 0
    $ the_target = None
    if scene_transition != True:
        $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(the_person, position = "sitting")
        "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
        mc.name "Milkshake time!"
        alexia "Yay!"
        mc.name "Hey, you two know the rules. Before you get your shakes, I want to see some tits!"
        the_person "Ha! Fine!"
        "The girls make a small show of shedding their tops."
        $ scene_manager.strip_to_tits()
        "When they finish, you hand them their milkshakes."
        the_person "Hey, thanks [the_person.mc_title]!"
        $ the_person.change_happiness(5)
        $ alexia.change_happiness(5)
        "The girls seem thankful for their drinks."
        alexia "Same rules as last time, right? [alexia.mc_title] eats out the winner?"
        the_person "Yeah! And don't forget the most important part. The loser has to suck him off!"
        "Your cock twitches in your pants. You can't wait to get one of these girls' mouths on your dick."
    "As the girls get ready to play, you check your watch. It is already pretty late, but you want to watch enough matches to fairly declare a winner."
    "How many wins will it take to win tonight?"
    "NOTE: the larger the number, the longer the event."
    menu:
        "1":
            pass
        "2":
            $ round_count = 2
        "3":
            $ round_count = 3
    "The girls look at you. Which girl do you want to sit next to first?"
    menu:
        "[myra.title]":
            $ the_target = myra
        "[alexia.title]":
            $ the_target = alexia

    "You sit down next to [the_target.possessive_title]. You think you see a hint of jealousy in the other girl's eyes, but it quickly vanishes as the game starts up."
    while myra_wins < round_count and alexia_wins < round_count:
        #Get close to the target
        if the_target == myra:
            $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
        else:
            $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "The character select screen comes up, and you get close to [the_target.title], your hands already running along the soft skin on her sides."
        call myra_alexia_teamup_fight_round_label(the_group, (the_target == myra)) from _myra_alexia_back_massage_round_call_03
        if _return == myra:
            $ myra_wins += 1
            $ the_target = myra
            if the_target.arousal_perc >= 65:
                "[myra.title] gazes at you, her face is flush with excitement."
                $ mc.change_locked_clarity(35)
                "There is no way she gets through another round without cumming."
            elif the_target.arousal_perc >= 30:
                myra "Yes! I win again! Your hands feel amazing [myra.mc_title]!"
                $ mc.change_locked_clarity(25)
            else:
                myra "Yes! Get to work [myra.mc_title]!"
        else:
            $ alexia_wins += 1
            $ the_target = alexia
            if the_target.arousal_perc >= 65:
                "[alexia.title] gazes at you, she bites her lip. Her face is flushed with arousal."
                $ mc.change_locked_clarity(35)
                "There is no way she gets through another round without cumming, and she knows it."
            elif the_target.arousal_perc >= 30:
                alexia "Oh my god... I won again? This is great!"
                $ mc.change_locked_clarity(25)
            else:
                alexia "Yay! You give great massages, [alexia.mc_title]!"

    $ the_loser = None

    if alexia_wins >= round_count:
        "It's over. [alexia.possessive_title] is the winner for the night."
        $ the_target = alexia
        $ the_loser = myra

    else:
        "It's over. [myra.possessive_title] is the winner for the night."
        $ the_target = myra
        $ the_loser = alexia
    mc.name "Alright girls, time for the winner to get her reward!"
    if scene_transition:
        the_target "This is amazing. How do you want to do this?"
        mc.name "What if, why don't you lay on the table, and then I can sit down and [the_loser.title] can service me beneath the table."
        the_target "Hmm, but I want to watch! What if like... YOU lay on the couch, and I can sit on your face while [the_loser.fname] sucks you off?"
        mc.name "I suppose that would be okay."
    else:
        mc.name "Alright, [the_target.title], we'll do it like last time again. You can sit on my face, okay?"
        the_target "Okay!"
    $ scene_manager.strip_full_outfit(the_target)
    "[the_target.title] gets herself ready to be serviced."
    "You lay down on the couch. [the_loser.possessive_title] gets between your legs and pulls your pants and underwear off, freeing your erection."
    $ scene_manager.update_actor(the_loser, position = "blowjob", display_transform = character_center(yoffset = .2, zoom = 1.1))
    if the_loser.opinion_score_giving_blowjobs() == -2:
        the_loser "Fuck. I can't believe I am about to do this. I HATE giving blowjobs!"
        the_target "Guess you should have won then!"
    "[the_target.possessive_title] slowly swings a leg over your body, getting herself into position "
    $ scene_manager.update_actor(the_target, position = "doggy", display_transform = character_right(yoffset = .2, zoom = 1.4))
    "[the_target.title]'s sexy ass is now right in your face. You waste no time diving in and begin to lick up and down her slit."
    $ face_fuck = False
    if the_loser == myra and the_loser.opinion_score_giving_blowjobs() == -2:   #Special scene where Alexia trains Myra a bit on blowjobs
        "Above you, you can hear [the_target.title] give some encouragement."
        the_target "Come on [the_loser.fname]! Don't worry, it won't bite!"
        the_loser "I know, I just... Ugh I don't know why I just can't stand giving blowjobs."
        the_target "Why? It is SO much fun! They are so hot and you can make him squirm like a little... AH!"
        "Your tongue hits a particularly sensitive spot, interrupting [the_target.title] for a second."
        the_loser "I guess, I've just had a few bad experiences before where guys... got a little rough I guess."
        the_target "Oh... I'm sorry. Well don't worry, if [the_target.mc_title] tries anything I'll just drown him for you."
        the_loser "Ha! Yeah I mean... I guess it is kind of nice that he is so... preoccupied..."
        "Your cock is aching, and after a few quiet moments, you finally feel [the_loser.title]'s soft tongue slide up and down it a few times."
        "You make sure to moan appreciatively into [the_target.title]'s cunt as you eat her out. She moans in response too."
        the_target "Ahhh... there see? It's no big deal."
        the_loser "Yeah... I think so..."
        if the_loser.love >40:
            the_loser "I think something is different too... about [the_loser.mc_title]."
            the_loser "Like... I would normally never do this but... I just want him to feel good. It makes me feel good to get him off!"
        else:
            the_loser "I don't know why I was so scared to do this. I don't know what has been up with me lately."
            the_loser "Normally, I would never do this. But lately, I feel like I'm really starting to find myself, sexually, you know?"
        "Another moment of silence, but this time instead of licks, you feel lips close around then sink down over the tip of your cock."
        the_target "Don't worry, I get it. Mmm, I bet that feels good, doesn't it [the_target.mc_title]?"
        "You moan appreciatively into [the_target.possessive_title]'s cunt."
        "You feel a small moan around your cock as [the_loser.title] starts to get into sucking you off. She isn't the most talented, but the whole situation has you really turned on."
        $ myra.increase_opinion_score("giving blowjobs")
    elif myra_finish_blowjob_training() and the_loser == myra and not myra.event_triggers_dict.get("shown_off_blowjob_skills", False):
        $ myra.event_triggers_dict["shown_off_blowjob_skills"] = True
        "As you begin licking, [the_loser.possessive_title] also gets to work, hungrily."
        "You feel her lips wrap around your tip, then descend down your cock slowly, all the way to the base. Your head is hitting the back of her throat."
        the_target "Wow... [the_loser.fname] you've really been practicing that, haven't you?"
        "A moaning affirmative is the only thing that escapes [the_loser.title]'s mouth as her tongue licks all around your balls."
        "You realize that you are going to cum fast. You'd better get to work!"
        "You eagerly lick up and down [the_target.title]'s slit, running circles around her clit for a few seconds in between strokes."
        "[the_loser.possessive_title] pulls off your cock for a second."
        the_loser "Hey, can you help me out? He normally does this for me, but he is a little busy right now."
        the_target "Mmmm... yeah? What do you need?"
        the_loser "Would you grab my head and like, you know, force me down on him?"
        the_target "Myr... you want me to... make you face fuck him?"
        the_loser "Yes please!"
        the_target "Fuck that's hot... Okay..."
        "While you can't see past the amazing ass in front of you, you have a pretty good idea of what is happening."
        "Suddenly, [the_loser.possessive_title]'s mouth forcefully descends your cock, her nose buried in your skin."
        "Her mouth is licking at you as it goes up and down a few times rapidly. After a few seconds, you can feel her gag."
        the_target "Oh my god, I'm sorry!"
        the_loser "What? Why? Keep going this is so hot!"
        the_target "Oh my god, oh fuck..."
        $ face_fuck = True
    elif the_target.opinion_score_giving_blowjobs() == 2 and the_target.opinion_score_being_submissive() > 0:
        "As you begin licking, [the_loser.possessive_title] also gets to work, hungrily."
        "You feel her lips wrap around your tip, then descend down your cock slowly, all the way to the base. Your head is hitting the back of her throat."
        the_target "Wow, you like that don't you, you little whore? You love gagging yourself on [the_target.mc_title]'s cock?"
        "A moaning affirmative is all that escapes [the_loser.possessive_title]'s mouth."
        "Suddenly, you feel her head bouncing up and down on your cock forcefully."
        the_target "Do you like that too? When I pull your hair and force you down on it? That's it bitch, take it!"
        "[the_target.title] rams [the_loser.possessive_title]'s face down on your cock and holds it there. You can feel her nose buried in your skin and she licks your balls a bit."
        "After a few seconds, suddenly she pulls off, gasping for air."
        the_loser "Holy fuck that was hot... keep going!"
        "Fuck, [the_target.possessive_title] is about to fuck you with [the_loser.title]'s face!"
        "You realize that you are going to cum fast. You'd better get to work!"
        "You eagerly lick up and down [the_target.title]'s slit, running circles around her clit for a few seconds in between strokes."
        $ face_fuck = True
    else:
        "As you begin licking, [the_loser.possessive_title] also gets to work."
        "You feel her soft hand around the base of your cock, as she licks at the tip a few times, tasting your pre-cum."
        if the_target.opinion_score_drinking_cum() > 0:
            the_target "Mmmm, I bet that tastes good, doesn't it? Can I have some?"
            "You feel [the_loser.title]'s soft hand give you a few strokes, while some weight shifts on the couch. Soon you hear the two girls making out."
            the_target "Mmm, it DOES taste good!"
            "The soft mouth of [the_loser.possessive_title] returns to your erection."
        "Slowly, methodically, you feel her lips descend your cock and then hold it about halfway in for a few seconds, her tongue swirling around it."
        "You moan appreciatively into the soaking wet cunt of [the_target.title]."
    "You put both hands on [the_target.title]'s ass cheeks, pulling them apart to give you better access."
    the_target "Ohhh god, that's it [the_target.mc_title]. Your tongue feels so good!"
    if face_fuck:
        $ play_gag_sound()
        "[the_target.possessive_title] mercilessly fucks her gaming buddy's face with your cock. Once in a while you feel her gag around you, and the twitching feels amazing."
        the_target "Look up at me [the_loser.fname]. I want you to look at me this time."
        "[the_loser.title] pulls off for a second, sputtering and catching her breath. After a second to catch her breath, her hot mouth slowly works its way down your cock again."
        "You feel your hips buck a little, her tight throat feels incredible."
    else:
        the_target "Fuck, it is so hot to watch you suck him off..."
        "[the_loser.possessive_title] moans a little bit as her mouth begins to stroke you."
    "You lay on your back, just enjoy the amazing sensations of having your two gamer girls fucking around with you."
    "You lick at [the_target.possessive_title]'s delicate pussy, spreading her lips and sending your tongue inside."
    "She shivers with each touch, obviously enjoying the feeling."
    "Her pussy is dripping wet, filling your mouth with the taste of her juices."
    $ the_target.call_dialogue("sex_responses_oral")
    if face_fuck:
        "[the_target.title] is really getting off on her position controlling [the_loser.possessive_title]."
        the_target "That's it. Taking it deep you little cum slut! If you can't play games, the least you can do is service [the_target.mc_title]'s cock!"
        "The sensations are amazing as she gags and throats you. There is no way you are going to last much longer."
    elif the_loser.sex_skills["Oral"] <= 2 and the_loser == myra:
        "[the_loser.possessive_title] is trying her best to suck you off, but clearly does not have much experience. At one point she rakes her teeth up the underside, causing you to flinch."
        mc.name "Mff! Hey!"
        "You cry out, but it is muffled by [the_target.possessive_title]'s cunt."
        the_target "Whoa, easy there [the_loser.fname]! No teeth!"
        the_loser "What?"
        the_target "The poor guy is sensitive down there, don't use teeth!"
        the_loser "Ah... right..."
        "[the_loser.possessive_title] keeps trying, and [the_target.title] gives her a couple tips as she goes."
        "Her technique is getting better, and it is starting to feel much better."
        "Soon you feel the familiar urge growing in your body."
    else:
        "[the_loser.possessive_title] keeps working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
        "You can feel her hand stroking you as she gently sucks on your testicles, as if urging them to release your cum to her."
    the_target "Oh fuck that feels so good... Oh god I'm gonna cum!"
    "Licking and probing all around [the_target.possessive_title]'s clit, you can feel her start to quiver."
    $ the_target.call_dialogue("climax_responses_oral")
    "All at once the tension in her body is unleashed in a series of violent tremors. Her body collapses for a second, momentarily keeping you from breathing."
    "You give her ass a slap, and she lifts up on her knees enough to get you some air."
    $ the_target.have_orgasm(half_arousal = False)
    "Having [the_target.title] cum all over your face has really gotten you turned on, you feel yourself getting ready to cum too."
    mc.name "Oh god... [the_loser.title] I'm gonna cum!"
    if face_fuck:
        "You feel [the_loser.possessive_title]'s mouth being shoved forcefully down on your cock and it stays there. Her tongue is lapping all around your testicles."
        the_target "That's it! Take it down your throat you little cum slut!"
        "You can't take it anymore. You buck your hips as you start to cum down [the_loser.title]'s throat."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_loser)
        $ the_loser.cum_in_mouth()
        $ scene_manager.update_actor(the_loser)
        "[the_loser.title] struggles to drink it all down, but doesn't try and pull off."
        "When you finish, she suddenly pulls off when [the_target.title] lets go of her [the_loser.hair_description]."
        the_loser "Oh my god, I thought I was drowning..."
        if the_loser.opinion_score_drinking_cum() > 0:
            the_loser "It was amazing!"
    else:
        "You feel [the_loser.possessive_title]'s hand stroking you rapidly while she sucks on the tip, milking your cock."
        the_target "That's it! Swallow it like a good little cum slut!"
        "You can't take it anymore, and you start to cum in [the_loser.title]'s mouth."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_loser)
        $ the_loser.cum_in_mouth()
        $ scene_manager.update_actor(the_loser)
        $ play_swallow_sound()
        "[the_loser.title] struggles to drink it all down, but doesn't pull off."
        "A few seconds after your last spurt, she stops stroking you and pulls off."
        if the_loser.opinion_score_drinking_cum() > 0:
            the_loser "Mmmm, you came so much for me!"
        else:
            the_target "Mmmm, why the face? You know you like it! Now be a good girl and swallow."
            $ play_swallow_sound()
            "A few seconds later, [the_loser.possessive_title] must have complied as she starts to talk."
            the_loser "Yeah... call me crazy, but I think I'm getting used to that... For some reason it wasn't as bad as I remembered."
            $ the_loser.increase_opinion_score("drinking cum")
        if the_target.opinion_score_drinking_cum() > 0:
            the_target "Oh hey, you got a little on your... mmm just come here..."
            "You can't see anything around her ass, but you can hear [the_target.title] and [the_loser.possessive_title] start to kiss each other."
            "They go at it for several seconds."
            $ the_target.cum_in_mouth()
            $ scene_manager.update_actor(the_target)
            the_loser "Oh! Now you've got some... ahh..."

    the_target "Well... should we let him up?"
    the_loser "Yeah we probably should... although..."
    the_target "Nope! You'll just have to get off on your own time!"
    $ the_loser.change_obedience(10)
    "The girls slowly get up, leaving you in a bit of a daze."
    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped, position = "stand3")
    $ scene_manager.update_actor(myra, display_transform = character_right, position = "stand2")
    alexia "Oh god, did we break him?"
    myra "Hopefully not, we need him to come back next week!"
    "[alexia.title] laughs a bit, but she still appears to be a bit concerned about you."
    mc.name "Don't worry, I'm good. That was amazing, wow. You two are absolutely incredible."
    $ the_target.change_stats(happiness = 10, slut = 2, max_slut = 80)
    $ the_loser.change_stats(obedience = 10, slut = 2, max_slut = 80)
    "The girls clearly appreciate your kind words."
    "Sadly, things seem to be drawing to a natural conclusion for tonight."
    the_loser "Hey... want to help me with the snacks [the_target.name]? I know I already had one, but I'm still kinda hungry."
    the_target "Sure! [the_target.mc_title] do you want to have some?"
    mc.name "No, I need to get going. Thanks though."
    if scene_transition:
        the_loser "We are doing it this way from now on though... right?"
        the_target "Oh, want to swallow cum every week?"
        the_loser "Errr, I mean a little bit... but it was so hot how you were on top of him like that, watching you get off..."
    else:
        the_loser "I can't wait until next week."
        the_target "Oh, want to swallow another load next week?"
        the_loser "No way! I mean... yeah but... I won't be! It was so hot watching you ride his face... I want a turn!"
    "The girls start to play fight a little bit. It's cute, but you get up to leave."
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    "Things are progressing amazingly with the two gamer girls. Obviously, you want to keep pushing things with them."
    "You feel like you are getting them ready for your end game, a full on threesome."
    if myra.has_taboo("vaginal_sex") or alexia.has_taboo("vaginal_sex"):
        "You aren't sure that you will be able to convince the girls to go that far together yet though."
        "You should make sure you've fucked each girl at least once before you try to make things go any farther..."
    if myra.opinion_score_vaginal_sex() == -2:
        "You aren't sure that you will be able to manage it while [myra.title] hates vaginal sex though..."
    elif alexia.opinion_score_vaginal_sex() == -2:
        "You aren't sure that you will be able to manage it while [alexia.title] hates vaginal sex though..."

    $ the_loser = None
    $ the_target = None
    # call advance_time from _call_advance_myra_alexia_teamup_scene_adv_01
    return

label myra_alexia_teamup_scene_scene_3(the_group, scene_transition = False):  #Sex
    $ the_person = the_group[0]
    $ current_round = 1
    $ round_count = 1
    $ myra_wins = 0
    $ alexia_wins = 0
    $ the_target = None
    if scene_transition != True:
        $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(the_person, position = "sitting")
        "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
        mc.name "Milkshake time!"
        alexia "Yay!"
        mc.name "Hey, you two know the rules. Before you get your shakes, lose the clothes!"
        the_person "Ha! Fine!"
        "The girls make a small show of shedding their clothing."
        $ scene_manager.strip_full_outfit()
        "When they finish, you hand them their milkshakes."
        the_person "Hey, thanks [the_person.mc_title]!"
        $ the_person.change_happiness(5)
        $ alexia.change_happiness(5)
        "The girls seem thankful for their drinks."
        alexia "Same rules as last time, right? [alexia.mc_title] fucks the winner?"
        the_person "Yeah! And don't forget the most important part. The loser has to help!"
        "Your cock twitches in your pants. You can't wait to fuck these beautiful girls."
    "As the girls get ready to play, you check your watch. It is already pretty late, but you want to watch enough matches to fairly declare a winner."
    "How many wins will it take to win tonight?"
    "NOTE: the larger the number, the longer the event."
    menu:
        "1":
            pass
        "2":
            $ round_count = 2
        "3":
            $ round_count = 3
        "4":
            $ round_count = 4
    "The girls look at you. Which girl do you want to sit next to first?"
    menu:
        "[myra.title]":
            $ the_target = myra
        "[alexia.title]":
            $ the_target = alexia

    "You sit down next to [the_target.possessive_title]. You think you see a hint of jealousy in the other girl's eyes, but it quickly vanishes as the game starts up."
    while myra_wins < round_count and alexia_wins < round_count:
        #Get close to the target
        if the_target == myra:
            $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
        else:
            $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
            $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "The character select screen comes up, and you get close to [the_target.title], your hands already running along the soft skin on her sides."
        call myra_alexia_teamup_fight_round_label(the_group, (the_target == myra)) from _myra_alexia_back_massage_round_call_04
        if _return == myra:
            $ myra_wins += 1
            $ the_target = myra
            if the_target.arousal_perc >= 65:
                "[myra.title] gazes at you, her face is flush with excitement."
                $ mc.change_locked_clarity(35)
                "There is no way she gets through another round without cumming."
            elif the_target.arousal_perc >= 30:
                myra "Yes! I win again! This is amazing [myra.mc_title]!"
                $ mc.change_locked_clarity(25)
            else:
                myra "Yes! Get to work [myra.mc_title]!"
        else:
            $ alexia_wins += 1
            $ the_target = alexia
            if the_target.arousal_perc >= 65:
                "[alexia.title] gazes at you, she bites her lip. Her face is flushed with arousal."
                $ mc.change_locked_clarity(35)
                "There is no way she gets through another round without cumming, and she knows it."
            elif the_target.arousal_perc >= 30:
                alexia "Oh my god... I won again? This is great!"
                $ mc.change_locked_clarity(25)
            else:
                alexia "Yay! You give great massages, [alexia.mc_title]!"

    $ the_loser = None

    if alexia_wins >= round_count:
        "It's over. [alexia.possessive_title] is the winner for the night."
        $ the_target = alexia
        $ the_loser = myra
    else:
        "It's over. [myra.possessive_title] is the winner for the night."
        $ the_target = myra
        $ the_loser = alexia
    mc.name "Alright girls, time for the winner to get her reward!"
    if scene_transition:
        the_loser "No! I can't believe I lost!"
        "She shakes her head in disbelief."
        the_loser "Well, how are we going to do this?"
        the_target "[the_target.mc_title], what if like... we don't HAVE to leave [the_loser.fname] hanging?"
        mc.name "Have something in mind?"
        the_target "I mean, we could like, sixty nine, and then you could fuck me right in front of her!"
        the_loser "Ohhh, wow that sounds nice..."
        the_target "I know it was a competition but it can be so frustrating to be left out, and I want her to feel good too... just as much as I want you to!"
        "You consider it for a second."
        mc.name "Is that what you both want?"
        the_loser "Yeah! And next week if I win I'll do the same!"
        mc.name "Alright."
    else:
        mc.name "Alright, [the_target.title], we'll do it like last time again. Lay down and [the_loser.title] get on top of her."
        the_target "Okay!"
    call start_threesome(the_target, the_loser, start_position = Threesome_sixty_nine, position_locked = True) from _myra_alexia_postgame_threesome_01
    $ the_report = _return
    if the_report.get("trifecta", False) and scene_transition:
        "When you finish, you can't believe how well it went. Everyone orgasmed and seems satisfied."
        the_target "God that dick is amazing..."
        the_loser "Your tongue was pretty good too..."
        "There's no doubt in your mind that this has set a new precedent with the two girls."
    elif the_report.get("trifecta", False):
        "You lay with the two gamer girls for a bit. Everyone is enjoying their post orgasmic bliss."


    "After a while, [alexia.title] breaks the silence."
    alexia "I hate to do this but... my stomach is rumbling. Is it snack time?"
    myra "Yeah we probably should..."

    $ scene_manager.update_actor(alexia, display_transform = character_center_flipped, position = "stand3")
    $ scene_manager.update_actor(myra, display_transform = character_right, position = "stand2")
    "You get up with the two girls."
    myra "I know the answer is probably no, but... are you sticking around for snacks [myra.mc_title]?"
    mc.name "No, but this has been a night to remember, for sure."
    $ the_target.change_stats(happiness = 10, slut = 2, max_slut = 100)
    $ the_loser.change_stats(obedience = 10, slut = 2, max_slut = 100)
    "The girls clearly appreciate your kind words."
    if scene_transition:
        the_loser "We are doing it this way from now on though... right?"
        the_target "Yeah, definitely."
    else:
        the_loser "I can't wait until next week."
        the_target "Me too!"
    "The girls start to chat as they walk towards the kitchen area."
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    "Things are amazing with the two gamer girls. Could it possibly even get any better?"

    $ the_loser = None
    $ the_target = None
    return

label myra_alexia_teamup_scene_scene_4(the_group, scene_transition = False):    #Free use - Not yet written.
    $ the_person = the_group[0]
    $ finished = False
    $ myra_ass_warmed_up = False
    $ alexia_ass_warmed_up = False
    $ myra_warmed_up = False
    $ alexia_warmed_up = False
    if scene_transition != True:
        $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "walking_away")
        $ scene_manager.add_actor(the_person, position = "walking_away")
        $ myra.increase_opinion_score("threesomes")
        $ alexia.increase_opinion_score("threesomes")
        "You walk to the back where the couches are and see the two girls playing a cooperative older game featuring a puffy pink protagonist that eats anything."
        mc.name "Milkshake time!"
        alexia "Yay!"
        the_person "Yum!"
        "You set the milkshakes down on a small table between the two couches. Both girls grab theirs and take a big sip."
    else:
        $ scene_manager.update_actor(alexia, display_transform = character_center_flipped, position = "walking_away")
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "The girls lay down on the couches and grab their controllers, after taking a big sip from their milkshakes."
    "As they start their game, both girls idly sway their hips a bit... as if trying to entice you to take them first..."
    "They are in a relaxed position, so they will be able to go for as long as you want to."
    while not finished:
        "You look at the two girls. Four holes, ready and willing to receive you."
        menu:
            "[myra.title]'s ass":
                $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
                $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
                call myra_alexia_teamup_anal_prone(myra, myra_ass_warmed_up) from _myra_alexia_teamup_anal_myra_01
                $ myra_ass_warmed_up = True
            "[myra.title]'s pussy":
                $ scene_manager.update_actor(myra, display_transform = character_right(yoffset = .2, zoom = 1.2))
                $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = 0, zoom = 0.8))
                call myra_alexia_teamup_vaginal_prone(myra, myra_warmed_up) from _myra_alexia_teamup_prone_myra_01
                $ myra_warmed_up = True
            "[alexia.title]'s ass":
                $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
                $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
                call myra_alexia_teamup_anal_prone(alexia, alexia_ass_warmed_up) from _myra_alexia_teamup_anal_alexia_01
                $ alexia_ass_warmed_up = True
            "[alexia.title]'s pussy":
                $ scene_manager.update_actor(the_person, display_transform = character_right(yoffset = 0, zoom = 0.8))
                $ scene_manager.update_actor(alexia, display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
                call myra_alexia_teamup_vaginal_prone(alexia, alexia_warmed_up) from _myra_alexia_teamup_prone_alexia_01
                $ alexia_warmed_up = True
            "Finish up":
                "You decide you want to be done for the evening."
                $ finished = True
        if mc.arousal == 0:
            "You take a few moments to catch your breath. That orgasm felt amazing."
            "Your dick starts to go soft... do you want to take a breather? Or just be done for the night?"
            menu:
                "Take a breather" if mc.energy > 10:
                    "You stand up for a moment. You look down, first checking out [myra.title]..."
                    if myra.has_creampie_cum and myra.has_ass_cum:
                        $ mc.change_locked_clarity(50)
                        "You admire [myra.possessive_title]'s well used backside. Your cum covers her ass from one load, while another load dribbles down between her legs from when you finished inside her."
                    elif myra.has_creampie_cum:
                        $ mc.change_locked_clarity(40)
                        "Your cum is dripping down [myra.possessive_title]'s legs, what small amount has escaped from when you came inside her."
                    elif myra.has_ass_cum:
                        $ mc.change_locked_clarity(40)
                        "You admire [myra.possessive_title]'s cum covered ass, your sticky seed coating her tight buttocks."
                    else:
                        $ mc.change_locked_clarity(30)
                        "You admire [myra.possessive_title]'s pristine back side. It could use a load or two of your cum before the night is over..."
                    "You look over at [alexia.title]'s tight, willing holes."
                    if alexia.has_creampie_cum and alexia.has_ass_cum:
                        $ mc.change_locked_clarity(50)
                        if alexia_ass_warmed_up:
                            "[alexia.possessive_title]'s asshole gapes a bit from your your previous fucking, and your cum is covering her ass."
                        else:
                            "[alexia.possessive_title]'s asshole looks tight and begging to be fucked, and your cum is covering her ass."
                        "Another load of your cum is slowly dripping down between her legs from when you finished inside her."
                    elif alexia.has_creampie_cum:
                        $ mc.change_locked_clarity(40)
                        if alexia_warmed_up and alexia_ass_warmed_up:
                            "Both of [alexia.possessive_title]'s well fucked holes look like they could handle another round, while a bit of your cum has started to leak out of her."
                        else:
                            "Your cum is starting to leak from inside her."
                    elif alexia.has_ass_cum:
                        $ mc.change_locked_clarity(40)
                        "[alexia.possessive_title]'s ass is covered in your spunk. You couldn't help but mark your territory all over her backside."
                    else:
                        $ mc.change_locked_clarity(30)
                        "[alexia.possessive_title]'s pristine ass looks ready for you to defile. You reach over and give it a quick spank."
                    $ mc.change_energy(20)
                    "Something about having the two gamer girls being free for your personal pleasure helps you regain some energy."
                    "You stroke yourself a couple of times. You are getting hard again."
                "Finish":
                    "You decide you've had enough for tonight. You sit back and catch your breath for a moment."
                    $ finished = True
        elif mc.energy < 20:
            "You are too tired to continue anymore. You sit back and catch your breath."
            $ finished = True

    mc.name "I think I'm done for tonight."
    #Best dialogue if you came for each girl atleast once.
    if (ask_harem_requirement(myra) and (ask_harem_requirement(alexia) or alexia.has_role(harem_role))):
        myra "You know, setting up gaming night with you and [alexia.fname] is probably the best thing I've done since I opened this cafe."
        alexia "Yeah, it has been great."
        myra "I know we're both dating [myra.mc_title]... but honestly, I don't even mind it."
        myra "I actually... kind of like it, to be honest."
        alexia "I like it too..."
        myra "[myra.mc_title]... you have this relationship going... with other girls too... don't you?"
        mc.name "I do. But I think that is okay."
        mc.name "You two, and me. We have a lot of love to share. There's no reason we can't all be a part of something bigger."
        mc.name "I want us to be part of a strong and healthy polyamorous relationship. The three of us. And more."
        myra "I honestly never thought I would be in a relationship like this... but somehow, it just feels so right."
        myra "I'll do it. As long as [alexia.fname] does too!"
        $ myra.add_role(harem_role)
        if alexia.has_role(harem_role):
            alexia "I umm... well I already decided to do that, so yeah, I'm in!"
        else:
            alexia "I know exactly what you are saying. I'll do it to!"
            $ alexia.add_role(harem_role)
        myra "Oh god. Come here..."
        $ scene_manager.update_actor(alexia, position = "missionary", display_transform = character_center(yoffset = .2, zoom = 1.2))
        $ scene_manager.update_actor(myra, position = "walking_away", display_transform = character_center_flipped(yoffset = .2, zoom = 1.2))
        "[alexia.title] turns over on her back, and [myra.possessive_title] jumps on top of her. They embrace and start to make out..."
        $ mc.change_locked_clarity(500)
        "You've done it. Both girls are completely fine with sharing you in a romantic relationship. It is so hot to watch them make out..."
        "You clear your throat."
        $ scene_manager.update_actor(myra, position = "back_peek")
        myra "Oh god. [myra.mc_title], I don't think I can get up. You don't mind letting yourself out, do you?"
        mc.name "Of course. Goodnight girls, I'll be seeing you both soon I'm sure."

    elif (myra.has_creampie_cum or myra.has_ass_cum and (alexia.has_creampie_cum or alexia.has_ass_cum)):
        $ scene_manager.update_actor(alexia, display_transform = character_center_flipped, position = "back_peek")
        $ scene_manager.update_actor(the_person, position = "back_peek")
        "The girls both look back at you. They both look happy. [alexia.possessive_title] wiggles her ass at your for a moment."
        alexia "Are you sure you can't give me just one more load of your cum?"
        myra "Or me!"
        mc.name "Sorry, I need to be done. But that was amazing."
        $ myra.change_stats(obedience = 5, happiness = 10, love = 5)
        $ alexia.change_stats(obedience = 5, happiness = 10, love = 5)
        myra "Okay. Next week?"
        mc.name "I'll do my best."
        alexia "You better!"
    else:
        $ scene_manager.update_actor(alexia, display_transform = character_center_flipped, position = "back_peek")
        $ scene_manager.update_actor(the_person, position = "back_peek")
        "The girls both look back at you."
        myra "Okay. Next week?"
        mc.name "I'll do my best."
        alexia "You better!"
    $ scene_manager.clear_scene()
    "You get up and head home."
    $ mc.change_location(bedroom)
    "Things are amazing with the two gamer girls. You can't wait to stuff their holes again next week."
    python:
        del alexia_ass_warmed_up
        del myra_ass_warmed_up
        del alexia_warmed_up
        del myra_warmed_up
        del finished
        #del the_target
    return

label myra_alexia_teamup_trans_scene_0(the_group):
    pass
    #This label should probably never be called because this event can't regress.
    return

label myra_alexia_teamup_trans_scene_1(the_group):
    $ the_person = the_group[0]
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
    mc.name "Milkshake time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "As the girls start to sip their milkshakes, you feel like it is time for you to up the stakes of the game."
    "As fun as it rubbing the girls backs, you feel like you could probably push them a bit farther."
    alexia "Same rules as last time, right? Winner get's a back massage during the next round?"
    "Before [the_person.title] can answer, you reply."
    mc.name "Actually, I have an idea for how we can make game night a bit more exciting. For everyone."
    "Both girls look at you with eyebrows raised."
    mc.name "As much as I enjoy rubbing your backs for an entire evening, I'd like to expand it some, to a full upper body massage."
    "[the_person.title] starts to roll her eyes."
    alexia "Sounds good to me!"
    the_person "[alexia.fname]... he just wants to feel us up!"
    alexia "Yeah... so?"
    the_person "So? You... you're okay with that?"
    alexia "Yeah, why not?"
    #TODO figure out if she has a boyfriend or not?
    # if alexia.is_single or alexia.is_girlfriend:
    # $ so_title = SO_relationship_to_title(the_person.relationship)
    the_person "What would your boyfriend think about that?"
    alexia "I mean, like earlier, what he doesn't know won't hurt him..."
    the_person "But like, we'll just get all worked up from him touching us? And then what?"
    mc.name "Well, that will be better incentive to win enough matches."
    mc.name "Whoever the winner is, I'll get her off while the loser goes to make snacks."
    "[the_person.title] looks exasperated."
    alexia "Yeah! Let's do it!"
    the_person "You know what? Fuck it. Let's do it. No mercy though [alexia.fname]!"
    alexia "Bring it bitch!"
    return

label myra_alexia_teamup_trans_scene_2(the_group):
    $ the_person = the_group[0]
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
    mc.name "Milkshake time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "As the girls start to sip their milkshakes, you feel like you are ready to move game time to the next step."
    "You admit that running your hands all over the girls is nice, but you want more."
    alexia "Same rules as last time, right? Winner get's an upper body massage during the next round?"
    "Before [the_person.title] can answer, you reply."
    mc.name "Actually, I have an idea for how we can make game night a bit more exciting. For everyone."
    "Both girls look at you with eyebrows raised."
    the_person "Oh boy, here we go."
    mc.name "First of all, don't misunderstand me, I love running my hands all over you two. You are very sexy."
    the_person "But?"
    mc.name "But... handjobs are great and all, but they aren't really anything special."
    mc.name "I think to make it more fun, we should all start with no shirts on, and my hands are allowed to go anywhere during the rounds."
    mc.name "I also think we should increase the stakes. I'll eat out the winner, but the loser has to give me a blowjob."
    the_person "There it is."
    "[the_person.title] starts to roll her eyes."
    alexia "That sounds reasonable to me."
    the_person "[alexia.fname]... what!?!"
    alexia "I mean, guys jack off all the time, right? I'm sure he can use his own hand with more skill than we have."
    the_person "That's not the point..."
    alexia "Besides, his tongue is even better than his fingers..."
    "[the_person.title] stops her protest."
    the_person "[alexia.fname]... how would you even know..."
    "Suddenly, [alexia.possessive_title] realizes what she said."
    alexia "I mean, he probably does... that's how sex is, right? It gets better like..."
    "[alexia.title] is rambling, trying to come up with a good excuse for why she knows what your tongue feels like."
    the_person "Hey. It's okay. If you're fine with sucking off [the_person.mc_title] while he eats me out, that's fine by me."
    alexia "If you WIN, you mean!"
    the_person "WHEN I win!"
    alexia "Not a chance!"
    the_person "You know what? Fuck it. Let's do it. No mercy though [alexia.fname]!"
    alexia "Bring it bitch!"
    "Oh my god, you did it. You can't wait to blow your load into one of these two girl's mouths."
    return

label myra_alexia_teamup_trans_scene_3(the_group):
    $ the_person = the_group[0]
    $ alexia.outfit.remove_all_upper_clothing()
    $ the_person.outfit.remove_all_upper_clothing()
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    "You walk to the back where the couches are and see the two girls playing the claymation fighting game again."
    "They've already taken their tops off. You take a moment to enjoy their nice tits before you announce your presence."
    mc.name "Milkshake time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "As the girls start to sip their milkshakes, you feel like you are ready to move game time to the final step."
    "Your endgame all along has been to fuck the winner, and you feel like you've gotten them both ready for it."
    alexia "Same rules as last time, right? Winner gets a happy ending with [alexia.mc_title]'s tongue?"
    "Before [the_person.title] can answer, you reply."
    mc.name "Actually, I have a proposal for you two."
    "Both girls look at you, but it is clear that they were expecting this."
    the_person "Go ahead, what are you thinking?"
    mc.name "Well, I feel like there's no need to ignore the obvious sexual tension between the three of us anymore."
    mc.name "But it is also clear that you two enjoy your little competition, so I think it is time that we raise the stakes again."
    mc.name "I think we should all just start naked, and between rounds, I get full access to the previous round winner to do... whatever."
    mc.name "Then at the end, the loser services the winner while I fuck her."
    "The girls look at each other, then back at you."
    alexia "That sounds like fun to me!"
    the_person "Me too. I can't wait to win! That cock is MINE!"
    alexia "No way! I'm going to win!"
    "The girls are surprisingly willing. As they start to strip their remaining clothes, you can't wait to fuck them both..."
    $ scene_manager.strip_full_outfit(alexia)
    $ scene_manager.strip_full_outfit(the_person)
    return

label myra_alexia_teamup_trans_scene_4(the_group):
    $ the_person = the_group[0]
    $ scene_manager.add_actor(alexia, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.strip_full_outfit(alexia, delay = 0)
    $ scene_manager.strip_full_outfit(the_person, delay = 0)
    "You walk to the back where the couches are and see the two girls playing a game."
    "This time though, they are playing an older game with a puffy pink protagonist and a sidekick, instead of the usual fighting game. It looks like more of a cooperative game than competitive."
    "They've already gotten naked. Damn you are one lucky bastard. You take a moment to enjoy their nice tits before you announce your presence."
    mc.name "Milkshake time!"
    alexia "Yay!"
    the_person "Hey, thanks [the_person.mc_title]!"
    $ the_person.change_happiness(5)
    $ alexia.change_happiness(5)
    "The girls happily take their milkshakes."
    mc.name "Alright, remember the rules?"
    alexia "Actually, we wanted to talk to you about that."
    mc.name "Oh?"
    the_person "[the_person.mc_title]... we don't want this to be a competition anymore."
    alexia "We just want this to be a fun night, where we play some games, relax, and get fucked senseless."
    the_person "We were wondering... While we are playing rounds, could you just fuck us both? Then whenever you are almost done with us, we could all just get off together?"
    alexia "You can use us however you want! We just want to make you happy!"
    "This is a surprising turn of events. However, this could be a lot of fun. Your two gamer girls, free for you to use while they just play casually."
    mc.name "Okay, that sounds great to me."
    alexia "Yay!"
    the_person "Here's what we were thinking. We could pull these two couches together and just lay on them on our stomachs while we play, and you can do... well anything."
    alexia "Just promise you'll try to get us both off!"
    mc.name "Of course!"
    return

label myra_alexia_teamup_scene_choice_label(the_group):
    $ the_person = the_group[0]
    the_person "So, are you going to stick around? Or just stopping by?"
    "[alexia.possessive_title] looks at you, you can tell she wants you to hang out."
    if myra_alexia_teamup_scene.stage < 2:
        alexia "Please [alexia.mc_title]? It's not the same without your magic hands to play for!"
        the_person "Ha! Yeah having something to play for definitely makes it more fun!"
    elif myra_alexia_teamup_scene.stage == 2:
        alexia "I honestly don't even care if I win or lose... but you should stick around!"
        "[alexia.title] glances down at your crotch and licks her lips. She's clearly thinking about what would happen if she loses..."
        the_person "Not me! I want to win for sure!"
        $ mc.change_locked_clarity(25)
        "Thought's of eating out [the_person.title] while [alexia.possessive_title] sucks your cock are certainly tantalizing..."
    elif myra_alexia_teamup_scene.stage == 3:
        alexia "You can warm me up while we play the first few rounds! You should stick around!"
        "[alexia.title] appears ready to start getting naked already."
    else:
        "You look at the two girls, ready and eager to let you fuck them as they play games together."
        "Their naked bodies already on display for you."
        alexia "It is so nice now, just playing for fun and relaxing while you fuck us good!"
        the_person "Yeah! You're totally going to stick around... right [the_person.mc_title]?"

    "Are you going to stay while the girls play?"
    menu:
        "Stay {image=gui/heart/Time_Advance.png}":
            pass
        "Leave":
            return False
    mc.name "Of course, I'd be crazy not to stick around. Do you two want milkshakes?"
    the_person "Fuck yeah!"
    alexia "One for me too please!"
    mc.name "Okay, I'll be right back."
    $ scene_manager.clear_scene(reset_actor = False)
    call myra_alexia_teamup_serum_label(the_group) from _myra_alexia_milkshake_serums_02
    return True

label myra_alexia_teamup_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    mc.name "Sorry, it has been a really long week and I need to head home."
    alexia "What? Damn..."
    the_person "That's okay. Maybe next week then?"
    mc.name "I'll try."
    $ clear_scene()
    "You leave the gaming cafe, leaving the girls to their game night"
    return

label myra_alexia_teamup_serum_label(the_group):
    "You walk down to the food court. Most places are closing up, but a few are still open."
    "Luckily, the stand that sells milkshakes is still open. You purchase a strawberry and a chocolate and head back towards the gaming cafe."
    $ mc.business.change_funds(-10)
    "As you walk back to the cafe, you look around. The mall is deserted... time to decide if you want to drop a serum in."
    if myra_alexia_teamup_scene.stage != 4:
        "If you wanted a particular girl to win, you could probably influence it with a serum you put in."
        "To be good at games, someone needs to have focus, and be good with their hands... (foreplay)"
    else:
        "The girls are already basically putty in your hands."
    "You look at [the_person.possessive_title]'s drink."
    call give_serum(the_person) from _call_give_myra_serum_teamup_03
    "You look at [alexia.possessive_title]'s drink."
    call give_serum(alexia) from _call_give_alexia_serum_teamup_04
    "When you get back to the cafe, you step inside and lock the door behind you."
    return

label myra_alexia_teamup_fight_round_label(the_group, myra_is_target):
    #Use skill score to determine the likely winner. Foreplay and focus score, with arousal being a distraction.
    $ skill_score = int(((myra.focus + myra.sex_skills["Foreplay"]) - (myra.arousal / 10) ) - ((alexia.focus + alexia.sex_skills["Foreplay"]) - (alexia.arousal / 10) ))
    if myra_is_target:
        $ the_target = myra
    else:
        $ the_target = alexia
        $ skill_score = (-skill_score)

    if myra_alexia_teamup_scene.stage < 3:
        "[the_target.title] leans back against you as the girls pick their characters. The heat of her body feels good against your chest."
    elif myra_alexia_teamup_scene.stage == 3:
        "[the_target.title] sits on your lap and leans back against you, your cock nestled in the crack of her ass."
        "She gives a sigh and a little giggle as she picks up her controller and the girls pick their characters."
    else:
        "You get on top of [the_target.title] as she lays on the couch. Her whole backside is open for you to do what you want with."
        "She gives a sigh and a little giggle when she feels your weight on her. She picks up her controller and the girls pick their characters."
    # if myra_alexia_teamup_scene.stage != 4: else: no longer competing
    if skill_score > 2:
        "[the_target.possessive_title] has an excellent chance of winning the matchup..."
        "That is, of course, depending on if your magic hands happen to be a distraction."
        "Maybe you should even up the match a little?"
    if skill_score < -2:
        "[the_target.possessive_title] has a low chance of winning the matchup from what you have seen so far."
        "Maybe you should take the opportunity to have some fun with [the_target.title]..."
    else:
        "The matchup seems to be pretty even. You feel like this round could go either way."
        "You could go easy on [the_target.possessive_title] to keep the matchup fair... or..."

    "How much should you distract [the_target.title]?"
    menu:
        "Light Distraction":
            call myra_alexia_teamup_light_distraction(the_target) from _myra_alexia_teamup_light_dist_0101
            $ skill_score -= 1
        "Moderate Distraction":
            call myra_alexia_teamup_med_distraction(the_target) from _myra_alexia_teamup_med_dist_0101
            $ skill_score -= 3
        "Major Distraction":
            call myra_alexia_teamup_large_distraction(the_target) from _myra_alexia_teamup_large_dist_0101
            $ skill_score -= 5
    if _return:
        $ the_target.change_arousal(_return)
    if the_target.arousal_perc >= 100:   #You drive her to orgasm and she loses her match
        call myra_alexia_teamup_orgasm_finish(the_target) from _call_myra_alexia_teamup_orgasm_finish
        if myra_is_target:
            return alexia
        else:
            return myra

    if renpy.random.randint(-10,10) <= skill_score:
        if myra_is_target:
            "TV" "Player one wins!"
            return myra
        else:
            "TV" "Player two wins!"
            return alexia
    else:
        if myra_is_target:
            "TV" "Player two wins!"
            return alexia
        else:
            "TV" "Player one wins!"
            return myra
    return

label myra_alexia_teamup_light_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a soft massage."
        "You keep your hands light to make sure not to distract her too much."
        "At a couple points in time, the fight gets tense, so you take a second and let [the_person.title] fight before resuming your back rub."
        the_person "Mmm..."
        "[the_person.title] sighs as you hit a particularly sensitive area. She feels good and relaxed."
        return 10
    if myra_alexia_teamup_scene.stage == 1:
        if the_person.arousal_perc < 40:
            "You let your hands roam up an down [the_person.possessive_title]'s back for a bit as the match gets started."
            "She wiggles a bit when you put your hands on her sides and pull her back against you a little bit more."
            "Your wrap your hands around her front, rubbing her stomach."
            "The fighting suddenly gets tense. Since she is distracted, you softly bring your hands up to her tits."
            the_person "Mmmm! Ahhh..."
            "[the_person.title] suddently realizes what you are doing when your thumb grazes against her nipple."
            if the_person.tits_available:
                "The heat and weight of her soft skin feels amazing in you hand. You softly knead her titflesh for the remainder of the match."
                return 20
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You softly knead her tits through her clothes for the remainder of the match."
                return 15
        else:
            "[the_person.possessive_title] is breathing a little heavy in front of you. She seems to be pretty excited."
            "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            "Encouraged by her, you run your thumb over her nipples. They are erect with excitement."
            if the_person.tits_available:
                "The heat and weight of her soft skin feels amazing in you hand. You eagerly caress her as she plays her match."
                return 20
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You softly knead her tits through her clothes for the remainder of the match."
                return 15
    if myra_alexia_teamup_scene.stage == 2:
        if the_person.arousal_perc < 30:
            "You softly run hands up and down [the_person.possessive_title]'s soft skin on her sides and belly as the match gets started."
            "You don't want to be too much of a distraction, you just want to get her slowly turned on as the match progresses."
            "Slowly, you reach up with your right hand and run your finger tips along her breast."
            "With your left hand, you reach down and cup her mound between her legs, applying gentle pressure."
            if the_person.vagina_available:
                "Some warmth is emanating from her exposed pussy as she slowly starts to get aroused."
            else:
                "[the_person.title] squirms a bit as you touch her pussy over her clothes."
            "The match has its ebbs and lulls, but you just keep slow steady pressure on [the_person.title] as you touch her."
            the_person "Mmm... ah..."
            "She gives a small moan as the matches are just about finished."
            if the_person.vagina_available:
                return 30
            return 25

        elif the_person.arousal_perc < 65:
            "[the_person.possessive_title] leans back against you. She sighs when your hands start to move along her skin."
            the_person "Mmm, that's nice..."
            "You bring both hands up to her tits for a bit. Her nipples are hard with arousal, so you give them a few light pinches as the game begins."
            "You keep cupping her breast with one hand, then let the other work its way south."
            if the_person.vagina_available:
                "Your hand slowly slides down her mound, then reaches her cunt."
                "Her arousal is just barely starting to leak out, moistening your fingers as you run them along her soft lips."
                "You are careful not to push your fingers inside, as much as you want to, trying to keep her arousal building but not providing too big of a distraction."
            else:
                "You run your hand along her mound on the outside of her clothes. You consider for a moment pulling them down."
                "You decide against it. You aren't trying to distract her too much, just keep her arousal building."
                "You cup her between her legs, applying moderately heavy pressure, and moving your fingers in a circular motion to stimulate her."
            the_person "That feels good... Mmm..."
            "You can tell that her arousal is starting to distract her from the match, but [the_person.title] is still doing pretty good."
            "Sometimes when there is a lull in the match, you feel her move her hips a bit, grinding against your hand as she plays."
            if the_person.vagina_available:
                return 35
            else:
                return 30
        else:
            if not the_person.vagina_available:
                "[the_person.possessive_title] is pretty clearly aroused, and you feel like you are about at your limit of how far you can drive her while she has clothes on."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway."
                $ scene_manager.strip_to_vagina(the_person)
                "Finally exposed, you drop one hand to her soaking wet pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal. You drop one hand down to her exposed soaking wet pussy."
            "You try to go easy on her, trying to prolong her pleasure as long as possible."
            "A couple times you feel her body start to tense up, not from the game, but from pleasure, so you back off each time."
            the_person "[the_person.mc_title]... I'm so close... just... just..."
            "You try to back off again, but [the_person.title] has other ideas. She grabs your hand with hers, shifts forward a bit, then sits on your hand, pinning it to the couch."
            "Completely ignoring the game, [the_person.possessive_title] starts rocking her hips, grinding herself on your hand."
            return 40
    if myra_alexia_teamup_scene.stage == 3:
        "For now, you are content to let the girls have a mostly fair match. You decide to enjoy the hot young body of [the_person.possessive_title] on your lap without going overboard."
        if the_person.arousal_perc < 40:
            "Her sides, her stomach, her thighs, her chest, her crotch... you let your hands roam her body."
            "Her skin is hot and soft, and feels amazing against yours. Your cock twitches between her ass cheeks when she adjusts her weight slightly"
            the_person "Mmm. God you feel so hard..."
            "[the_person.title] wiggles her hips against you a bit, but mostly just concentrates on the game."
            "You keep sliding one hand around her skin, and with the other you reach down between her legs. She spreads her legs to give you easy access."
            "You run your fingers along her slit a few times. She is just starting to get warmed up, so you take your time."
            "Her hips move a bit when you apply some pressure. It feels amazing having your cock nestled between her cheeks."
            "When you feel a bit of moisture, you slowly push your middle finger inside of her."
            the_person "Mmm... yes [the_person.mc_title]..."
            "The match is already almost over, so you spend the rest of it gently fingering her pussy, and getting her warmed up."
            $ mc.change_arousal(10)
            return 30
        elif the_person.arousal_perc < 65:
            "[the_person.possessive_title] whispers back to you."
            the_person "Do... do you want to put it in?"
            mc.name "Not yet."
            the_person "Hmm... okay..."
            "[the_person.title] is starting to get turned on, but you decide to keep teasing her for now."
            if the_person.has_large_tits:
                "You reach around her body, cupping her generous tits in your hands. You jiggle and squeeze them pleasingly in your hands."
            else:
                "You reach around her body, cupping her perky tits in your hands. She gasps when your thumbs graze her sensitive nipples."
            "[the_person.possessive_title] wiggles her hips a bit. Your cock twitches between her cheeks."
            "You slide one hand down between her legs. She opens her legs giving you easy access."
            "Her cunt is wet and ready for penetration, so you push two fingers up inside of her."
            "You move your fingers slowly, but each stroke elicits a small gasp of pleasure from [the_person.possessive_title]."
            "You go nice and slow for the duration of the match. Once in a while she squirms, the movement of her body feels great on your cock."
            $ mc.change_arousal(10)
            return 30

        elif the_person.arousal_perc < 90:
            the_person "Do you... want to put it in?"
            mc.name "No, I don't want to scew the game matchup."
            the_person "Ah... okay..."
            "She sound slightly disappointed, but then moans softly as you start to run your hands along her body."
            "You take your hands and tweak both of her nipples for a bit. You give them a pinch, then roll them between your fingers."
            the_person "Ah! Mmm....."
            "You run one hand down to her cunt. [the_person.possessive_title] is soaked and you easily slide two fingers in."
            the_person "Are you sure you don't want to put it in?"
            mc.name "Hush."
            "As you start to finger her, [the_person.title] begins to move her hips with you. She is trying to grind against your hand to get off."
            "However, you don't want to let her get off yet. You are content to edge her throughout the match, leaving her barely able to focus."
            "As the match is getting close to the end, she is trying to finish herself off with your hand, but you grab her hip with your free hand and steady her, driving her crazy."
            the_person "Fuck! So close... just... come on!"
            mc.name "Shhh, patience."
            $ mc.change_arousal(10)
            $ the_person.change_obedience(2)
            return 25
        else:
            "As you start to run your hands along [the_person.possessive_title]'s sides, she wiggles her ass against you."
            the_person "I'm sorry... I just... I really need this..."
            "She pushes herself up for a second off your lap, reaches back and grabs your cock, pointing it up, then slowly sits back down."
            "Your cock slides easily into her cunt. She is so turned on, she starts to move her hips, almost ignoring the game."
            the_person "Oh god... I don't even care if I lose... this feels so good!"
            "[the_person.title] sets down her controller and just starts riding you. Her ass is just bouncing up and down on your cock."
            "You grab her hips and help her. She is obviously on the final stretch."
            "The game sounds off with a declaration of the winner, but you barely hear over her ass smacking against your lap with each thrust."
            $ mc.change_arousal(20)
            return 40
    return

label myra_alexia_teamup_med_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a massage."
        "She has several tense areas, so you alternate between a light and more forceful massage, trying to get her tensest areas loosened up."
        "At a couple points in time, the fight gets tense, so you keep your touch light on [the_person.title] for a few seconds so you aren't TOO much of a distraction."
        the_person "Mmm... that's nice..."
        "[the_person.title] sighs as you hit a particularly sensitive area. She feels good and relaxed."
        return 15
    if myra_alexia_teamup_scene.stage == 1:
        if the_person.arousal_perc < 40:
            "You let your hands roam up an down [the_person.possessive_title]'s back for a bit as the match gets started."
            "She wiggles a bit when you put your hands on her sides and pull her back against you a little bit more."
            "Your wrap your hands around her front, rubbing her stomach and working your way upward."
            "The fighting suddenly gets tense. Since she is distracted, you bring your hands up to her tits."
            the_person "Mmmm! Ahhh..."
            "[the_person.title] gasps when you run your thumbs over her nipples. Her body wiggles back against you a bit as you grope her breasts."
            if the_person.tits_available:
                "The heat and weight of her soft skin feels amazing in your hands. You eagerly knead her titflesh for the remainder of the match, much to her enjoyment."
                return 30
            else:
                "You wish you could put your hand under her clothes, but you don't want to distract her too much."
                "You eagerly knead her tits through her clothes for the remainder of the match, much to her enjoyment."
                return 20
        else:
            "[the_person.possessive_title] is breathing a little heavy in front of you. She seems to be pretty excited."
            if not the_person.tits_available:
                "Not content to touch her over her clothes, you quietly start to pull at her top."
                "[the_person.title] glances over at the other girl, but with the match already starting she quickly decides to let you."
                $ scene_manager.strip_to_tits(the_person)
                "Finally topless, you bring your hands up to her amazing tits."
            else:
                "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            "You grope and massage [the_person.possessive_title]'s tits. You keep a steady pace, not slowing down even when the matchup gets tense."
            "[the_person.title] gasps and squirms under your touch. She's trying to hide her pleasure, but she is barely keeping it together."
            return 30
    if myra_alexia_teamup_scene.stage == 2:
        if the_person.arousal_perc < 30:
            "You softly run hands up and down [the_person.possessive_title]'s soft skin on her sides and belly."
            "Your goal isn't necessarily to throw the match, but you want to get her aroused and needy as the match progresses."
            "You reach up with your right hand and grab her breast, kneading it and once in a while you give her nipple a light pinch."
            "With your left hand, you reach down and cup her mound between her legs, applying pressure."
            if the_person.vagina_available:
                "Some warmth is emanating from her exposed pussy as she slowly starts to get aroused."
            else:
                "[the_person.title] squirms a bit as you touch her pussy over her clothes."
            "The match has its ebbs and lulls, but you just keep steady pressure on [the_person.title] as you touch her."
            "It is slight, but as the match goes on, her body is responding to your touches more and more. Her hips are moving slightly and her back arches when you pinch her nipple."
            the_person "Mmm... ah..!"
            "She gives a moan as the matches are just about finished."
            if the_person.vagina_available:
                return 35
            return 30

        elif the_person.arousal_perc < 60:
            if not the_person.vagina_available:
                "[the_person.possessive_title] is starting to get aroused, and you want to drive her arousal even further, but that is hard to do while she is still covered up."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway."
                $ scene_manager.strip_to_vagina(the_person)
                "Finally exposed, you drop one hand to her moist pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal in the air faintly. You drop one hand down to her exposed pussy."
            "[the_person.possessive_title] leans back against you. She sighs when your other hand gropes her tit."
            the_person "Mmm, that feels so good."
            "Her body is melting into yours. She is trying to concentrate on the match, but is thoroughly enjoying your touch too."
            "Her pussy is getting very wet, and her hips are rocking a bit as you touch her."
            "She is still in the match, but it is clear she is really enjoying the way you are touching her."
            return 40
        else:
            if not the_person.vagina_available:
                "[the_person.possessive_title] is pretty clearly aroused, and you feel like you are about at your limit of how far you can drive her while she has clothes on."
                "You reach down and start to take her bottoms off."
                the_person "Hey, that's no fair, I can't concen..."
                "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway."
                $ scene_manager.strip_to_vagina(the_person)
                "As you finish pulling her clothes off, you can smell her arousal. You drop one hand to her soaking wet pussy."
            else:
                "You can smell [the_person.possessive_title]'s arousal. You drop one hand down to her exposed soaking wet pussy."
            "You push two fingers into her, trying to prolong her pleasure."
            "A couple times you feel her body start to tense up, not from the game, but from pleasure, so you back off each time."
            the_person "[the_person.mc_title]... I'm so close... just... just..."
            "This time, you don't back off of [the_person.title]. She gasps when you start to finger her rapidly."
            "Completely ignoring the game, [the_person.possessive_title] starts rocking her hips, grinding herself on your hand."
            return 40
    if myra_alexia_teamup_scene.stage == 3:
        if the_person.arousal_perc >= 50:
            "You can tell that [the_person.title] is getting really turned on. You decide to fuck her for a bit as the match starts."
            "With one hand you urge her hips back up. She gets off your lap just enough for you to reach down and take your cock in your hand."
            "You point it up and then gently urge her back down."
        if the_person.arousal_perc < 40:
            "Her sides, her stomach, her thighs, her chest, her crotch... you let your hands roam her body."
            "Her skin is hot and soft, and feels amazing against yours. Your cock twitches between her ass cheeks when she adjusts her weight slightly"
            the_person "Mmm. God you feel so hard..."
            mc.name "Don't worry, I'm sure it'll be inside you soon."
            "Goosebumps go up all over [the_person.title]'s skin."
            "[the_person.title] wiggles her hips against you a bit, but mostly just tries to concentrate on the game."
            "You keep sliding one hand around her skin, and with the other you reach down between her legs. She spreads her legs to give you easy access."
            "You run your fingers along her slit a few times. You give her a bit to warm up."
            "Her hips move a bit when you apply some pressure. It feels amazing having your cock nestled between her cheeks."
            "When you feel a bit of moisture, you slowly push your middle finger inside of her. When you can easily push that one in, you slowly slide in a second finger."
            the_person "Mmm...  fuck yes [the_person.mc_title]..."
            "The match is already almost over, so you speed up, intent on getting her warmed up."
            "[the_person.title] squirms a bit under your touch, but clearly enjoys having your hands all over her as she finishes her match."
            $ mc.change_arousal(10)
            return 40
        elif the_person.arousal_perc < 65:
            "[the_person.possessive_title] whispers back to you."
            the_person "Do... do you want to put it in?"
            mc.name "Not yet."
            the_person "Hmm... okay..."
            "[the_person.title] is starting to get turned on, but you decide to just use your hands for now."
            if the_person.has_large_tits:
                "You reach around her body, cupping her generous tits in your hands. You jiggle and squeeze them pleasingly in your hands."
            else:
                "You reach around her body, cupping her perky tits in your hands. She gasps when your thumbs graze her sensitive nipples."
            "You give her nipples a hard pinch. She yelps and shoves her hips back against you. The friction of her soft cheeks against your cock feels great."
            "[the_person.possessive_title] wiggles her hips a bit. Your cock twitches between her cheeks."
            "You slide one hand down between her legs. She opens her legs giving you easy access."
            "Her cunt is wet and ready for penetration, so you push two fingers up inside of her."
            "You move your fingers slowly, but each stroke elicits a small gasp of pleasure from [the_person.possessive_title]."
            "You keep a nice steady pace for the duration of the match. She squirms often, the movement of her body feels great on your cock."
            $ mc.change_arousal(15)
            return 30

        elif the_person.arousal_perc < 90:
            "[the_person.title]'s cunt slides down easily over your cock. She gasps when her ass is finally resting against your hips, your cock deep inside her."
            the_person "Oh fuck... that feels so good..."
            "[the_person.possessive_title] is trying to concentrate on playing her match, but her hips are moving up and down."
            "You grab her hips with both hands, helping her move her hips easier."
            "Your cock plunges over and over into her needy cunt."
            the_person "Yes! Oh... fuck me... YES."
            "[the_person.title] is trying to play the game, but your cock is proving to be a huge distraction. Her juices are starting to run down your legs and onto the couch."
            $ mc.change_arousal(20)
            if the_person.arousal_perc >= 80:
                the_person "Oh god.. I can't... Fuck!"
                "Even though the match is almost over, [the_person.title] is getting ready to cum."
                "She drops her controller and just goes for it."
            else:
                "The match is almost over, and although she is really into it, [the_person.title] just isn't quite there."
            return 40
        else:
            "[the_person.possessive_title]'s cunt slides easily down onto your cock. She gasps when you bottom out inside her."
            the_person "Oh fuck... that's... that's so good..."
            "You feel her pussy twitch a couple times. She is ready to cum."
            "You grab her hips in your hands and pick her up slightly, then slam her back down."
            the_person "Oh! Jesus oh!"
            "[the_person.title] drops her controller."
            the_person "Oh god... I don't even care if I lose... this feels so good!"
            "[the_person.possessive_title] starts to move her hips up and down, your hands on her hips guiding her."
            "[the_person.title]'s ass is bouncing up and down now. Her tight, steamy cunt feels amazing sliding up and down you."
            "The game sounds off with a declaration of the winner, but you barely hear over her ass smacking against your lap with each thrust."
            $ mc.change_arousal(20)
            return 40
    return

label myra_alexia_teamup_large_distraction(the_person):
    if myra_alexia_teamup_scene.stage == 0:
        "You put your hands on [the_person.possessive_title]'s shoulders and start a massage."
        "She has several tense areas, so you press your hands into her muscles with urgency."
        "[the_person.title] gasps, trying to concentrate on the fight, but your hands are relentless."
        "At a couple points in time, the fight gets tense. You use the opportunity to find her tensest muscles and ."
        the_person "God... that feels amazing [the_person.mc_title]..."
        "[the_person.title] sighs as you hit a particularly sensitive area. She feels good but you have definitely distracted her."
        return 20
    if myra_alexia_teamup_scene.stage == 1:
        if not the_person.tits_available:
            "You are immediately annoyed by her top. You decide to take it off, whether she likes it or not."
            "[the_person.title] starts to protest, but you quickly pull her clothes off her upper body anyway."
            $ scene_manager.strip_to_tits(the_person)
            "Finally topless, you bring your hands up to her amazing skin, running both hands down her sides."
        if the_person.arousal_perc < 40:
            "You let your hands roam up and down [the_person.possessive_title]'s soft skin on her back and sides."
            "You don't even bother pretending to be gentle. With one hand you work on a knot you find on her back, with the other hand you reach around and grab one of her tits."
            the_person "Mmm! God... take it easy..."
            "[the_person.title] is trying to concentrate as the match gets suddenly tense, but instead of letting up, you double down."
            "You reach both hands around now and give her nipples a little pinch."
            "She curses under her breath and squirms a bit as you are now shamelessly groping her."
            return 40
        else:
            "[the_person.possessive_title] is breathing heavy in front of you. She seems to be pretty excited."
            "[the_person.title] steals a quick glance at the other girl, then quietly takes your hand and guides it from her side up to her chest."
            the_person "Mmmm..."
            if the_person.has_large_tits:
                "You grope and massage [the_person.possessive_title]'s amazing tits. They feel heavy and full in your hands, her titflesh spilling between your fingers as you grab her."
            else:
                "You grope and massage [the_person.possessive_title]'s perky tits. She gasps with each pull and tug on her sensitive nipples."
            "When the matchup gets intense, you double down, pinching her nipples."
            the_person "Mmm! God... take it easy..."
            "[the_person.title] gasps and squirms under your touch. She's trying to hide her pleasure, but she is barely keeping it together."
            return 40
    if myra_alexia_teamup_scene.stage == 2:
        if not the_person.vagina_available:
            "[the_person.possessive_title] needs to be taught a lesson in humility. You need to get her bottoms off for the best effect."
            "You reach down and start to take her bottoms off."
            the_person "Hey, that's no fair, I can't concen..."
            "[the_person.title] starts to protest, but you quickly pull her clothes off her lower body anyway."
            $ scene_manager.strip_to_vagina(the_person)
        if the_person.arousal_perc < 30:
            "You softly run your hands up and down [the_person.possessive_title]'s soft skin on her sides and belly."
            "You couldn't care less about the match, to be honest, you just want to get her as needy as possible in the time you have."
            "You reach up with your right hand and grab her breast, kneading it and once in a while you give her nipple a pinch."
            "With your left hand, you reach down and cup her mound between her legs, applying pressure."
            "Your ring finger and middle finger dip into her labia, eliciting a moan from [the_person.title]"
            the_person "Ah! Oh god... getting off to a fast start don't you think?"
            "You grind the palm of your hand against her clit as your two fingers dip slightly into her vagina. She is rapidly getting wet."
            the_person "Fuck! [the_person.mc_title], at least just let me play a little first..."
            "[the_person.possessive_title] whimpers and squirms under your touch. She is protesting, but it is obvious she is getting turned on."
            "She gives a moan, but the match is unfortunately almost over."
            return 45
        elif the_person.arousal_perc < 60:
            "[the_person.possessive_title] leans back against you. She sighs when you grope her tit."
            "You reach down with your other hand and easily slide two fingers into her cunt. Her arousal is clear from her smell and her gasps."
            the_person "Mmm, that feels so good."
            "Her body is melting into yours. She is trying to concentrate on the match, but is thoroughly enjoying your touch too."
            "Her pussy is extremely wet, and her hips are rocking a bit as you touch her."
            "You don't hold anything back. You grope her tit, pinching her nipple roughly as you finger fuck her."
            "Suddenly though, the match is over. She is close to orgasm, but not quite there..."
            return 40
        else:
            "You push two fingers into her. [the_person.title]'s cunt is soaked and she immediately moans."
            mc.name "Get ready to cum for me."
            the_person "Oh fuck I'm ready..."
            "[the_person.title] puts the controller down, not even bothering to play. Your grab her tits with your free hand and roughly pinch her nipple."
            "You push your fingers deep inside of her, stroking her g-spot."
            the_person "[the_person.mc_title]... I'm so close... just... just..."
            "Completely ignoring the game, [the_person.possessive_title] starts rocking her hips, grinding herself on your hand."
            return 45
    if myra_alexia_teamup_scene.stage == 3:
        "With one hand you urge her hips back up. She gets off your lap just enough for you to reach down and take your cock in your hand."
        "You point it up and then gently urge her back down."
        if the_person.arousal_perc < 40:
            "Since she is just getting warmed up, it takes her a few moments to sink down on your cock."
            the_person "Mmm... just getting right to it tonight then?"
            mc.name "That's right. Good luck with your game."
            "[the_person.title] finally bottoms out. Her pussy feels amazing wrapped around you."
            "[the_person.possessive_title] is concentrating on the match, so you reach around with your hands and pinch her nipples."
            the_person "Ah! Fuck..."
            "Her cunt twitches when you do that, so you do it again."
            the_person "[the_person.mc_title], will you just let me play one match!?!"
            "She asks in exasperation. Instead of answering, you put both hands on her hips. You lift her up until your cock is almost out, then slide her back down again."
            "Her pussy has gotten wetter, and you slide back in much easier."
            the_person "Oh fuck..."
            "She doesn't help you at all, but you are able to lift her hips with your hands and then bring them back down a few more times."
            "With each stroke you slide back in a little easier as her cunt gets wet with arousal."
            "She is trying to concentrate as much as possible on the match, but you are able to set a steady, albeit slow pace."
            "[the_person.title] is starting to gasp and her breathing is getting deeper when the match is almost over."
            $ mc.change_arousal(25)
            return 50
        elif the_person.arousal_perc < 65:
            "[the_person.possessive_title] is fairly aroused, so you are able to slide in easily."
            the_person "Oh fuck... I'm not sure this is fair... how am I supposed to play with your cock inside me?"
            mc.name "I have no idea. And to be honest I don't really care."
            "[the_person.title] squirms a bit. You reach up with both hands and roughly pinch her nipples."
            the_person "Ah! Fuck, this is crazy..."
            "You feel her pussy twitch when you pinch her nipples, so you do it again. Then again."
            "Feeling her cunt grasping you feels good, but you need more."
            "You grab her hips now with your hands. You lift her up until your cock is almost all the way out, then roughly back down."
            "Her ass makes a loud slap when you bottom out again."
            the_person "This isn't fair!"
            mc.name "That you get to sit on this dick but she doesn't? You're right, so enjoy it while it lasts."
            the_person "Mmm... okay..."
            "[the_person.possessive_title] tries to juggle concentrating on the game while moving her hips as you start to fuck her."
            "While you are doing most of the work, she is able to use her knees a bit to help so you don't have to lift her entire weight with each stroke."
            "[the_person.title] is trying desperately to win her match again, if for no other reason than to let you keep fucking her."
            "You set an eager pace, and her tight cunt feels amazing with each thrust, but unfortunately the length of the match doesn't leave you with enough time to finish her off."
            "The sound of her ass slapping against your hips echoes in the room as the match finishes up."
            $ mc.change_arousal(25)
            return 50

        elif the_person.arousal_perc < 90:
            "[the_person.title]'s cunt slides down easily over your cock. She gasps when her ass is finally resting against your hips, your cock deep inside her."
            the_person "Oh fuck... that feels so good..."
            "[the_person.possessive_title] is trying to concentrate on playing her match, but her hips are moving up and down."
            "You grab her hips with both hands, helping her move her hips easier."
            "Your cock plunges over and over into her needy cunt."
            the_person "Yes! Oh... fuck me... YES."
            "[the_person.title] is trying to play the game, but your cock is proving to be a huge distraction. Her juices are starting to run down your legs and onto the couch."
            "At this point, she is doing most of the work, so you just guide her with one hand while you reach up with the other and fondle her tits."
            the_person "[the_person.mc_title], your cock feels so good... oh fuck me... Fuck me!"
            "The match is almost over, but she isn't going to make it. She drops her controller and moans loudly. She is getting ready to cum."
            $ mc.change_arousal(20)
            return 50
        else:
            "[the_person.possessive_title]'s cunt slides easily down onto your cock. She gasps when you bottom out inside her."
            the_person "Oh fuck... that's... that's so good..."
            "You feel her pussy twitch a couple times. She is ready to cum."
            "You grab her hips in your hands and pick her up slightly, then slam her back down."
            the_person "Oh! Jesus oh!"
            "[the_person.title] drops her controller."
            the_person "Oh god... I don't even care if I lose... this feels so good!"
            "[the_person.possessive_title] starts to move her hips up and down, your hands on her hips guiding her."
            "[the_person.title]'s ass is bouncing up and down now. Her tight, steamy cunt feels amazing sliding up and down you."
            "The game sounds off with a declaration of the winner, but you barely hear over her ass smacking against your lap with each thrust."
            $ mc.change_arousal(20)
            return 50

    return

label myra_alexia_teamup_orgasm_finish(the_person):
    if myra_alexia_teamup_scene.stage <= 1:
        "[the_person.title] suddenly starts to shudder. She gasps and moans under her breath."
        "Is... is she cumming?"
        "Her character has stopped moving in the game. The other girl easily finishes her off."
        $ the_person.have_orgasm()
        "Wow, she definitely just orgasmed. You hands really are magic?"
        "For several seconds, she rides her orgasm until she finally opens her eyes, discovering she has lost the match."
    elif myra_alexia_teamup_scene.stage == 2:
        "[the_person.title] is still holding her controller, but has stopped playing as you finger her urgently."
        the_person "Oh god... oh... OH!"
        "Her pussy clenches down on your fingers as she begins to orgasm. She closes her eyes and her hips are bucking slightly."
        $ the_person.have_orgasm()
        "For several seconds, she rides her orgasm until she finally opens her eyes, discovering she has lost the match."
    elif myra_alexia_teamup_scene.stage == 3:
        "Her controller on the floor, [the_person.title] is riding your cock with abandon."
        if mc.arousal_perc >= 100:   #Cum together.
            "Her hot pussy and urgent moans are too much. You are going to cum too."
            mc.name "I'm gonna cum!"
            the_person "Oh fuck me too!"
            if the_person.wants_creampie:
                "[the_person.possessive_title] just keeps riding you as you orgasm."
                "As you start to shoot your load inside of her, she suddenly falls back against you, bottoming out on top of you as she orgasms also."
                the_person "Oh fuck! Oh yes fill me up [the_person.mc_title], OH!"
                $ the_person.have_orgasm()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
                $ the_person.cum_in_vagina()
                $ scene_manager.update_actor(the_person)
                "You pulse wave after wave of cum inside of her as she rides out her own orgasm."
                "When you are finished, your combined juices have started to run down your legs and onto the couch."
                myra "I guess I'm going to have to clean that up... aren't I..."
                if the_person == myra:
                    "You chuckle."
                    alexia "Jesus, you two are fucking hot..."
                    $ alexia.change_arousal(5)
                    "[alexia.title] won the match already, and she just watches as you and [the_person.title] finish up."
                else:
                    "[myra.title] won the match already, and just watches as you and [the_person.title] finish up."
                    alexia "I... I can help..."
                    myra "You better! That was really hot though..."
                    $ myra.change_arousal(5)
            else:
                "[the_person.possessive_title] suddenly pulls off you, then backs her ass up against your cock."
                "You ache to be back inside her, but it is too late to protest. You start to cum all over her ass."
                $ the_person.cum_on_ass()
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
                $ scene_manager.update_actor(the_person)
                the_person "Oh fuck... cum all over me!"
                "[the_person.title] reaches down and rubs circles around her slit like crazy as she finishes herself off."
                "Your cock twitches as the couple waves erupt out of your cock and onto her ass." # not sure how to fix this line
                $ the_person.have_orgasm()
                if the_person == myra:
                    alexia "Wow! You two are so hot..."
                    $ alexia.change_arousal(5)
                    "[alexia.title] won the match already, and she just watches as you and [the_person.title] finish up."
                else:
                    "[myra.title] won the match already, and just watches as you and [the_person.title] finish up."
                    myra "Wow. I'm not jealous or anything but that was... wow."
                    $ myra.change_arousal(5)
                the_person "Let me just... clean up real quick..."
                "[the_person.title] grabs a few wipes off a table and quickly cleans herself up before returning to the couch. You do the same."
                $ the_person.outfit.remove_all_cum()
                $ scene_manager.update(the_person)

        else:
            the_person "Yes... oh yes!"
            "You slam her hips down one last time as [the_person.possessive_title] starts to cum."
            "You can feel her cunt gripping you as she has a strong orgasm. It feels amazing."
            "When she finishes, she looks up, seeing that the match is over."
            $ the_person.have_orgasm()
            the_person "Ahh... that... was worth it."
    else:
        pass
    return

label myra_alexia_teamup_anal_prone(the_person, warmed_up = True):
    "You get on top of [the_person.possessive_title]. Her puckered back door beckons you."
    if warmed_up:
        "It still gapes a little bit from earlier. She moans a bit when you lean forward and slowly push your cock inside her."
    else:
        "Her asshole is, as of yet, undefiled, for tonight anyway. You should probably warm her up a bit before proceeding."
        if renpy.random.randint(0,1) == 0:
            "You spit a copious amount onto your middle and index fingers, then work them around her sphincter."
            "[the_person.title] moans a bit and arches her back."
            $ the_person.change_arousal(10)
            "You give her ass two more rounds of spit, then a little more on your cock. You're ready to go."
        else:
            "You reach down and push two fingers into her cunt. She is wet and ready, and you quickly have lots of her juices on your fingers."
            "You pull your fingers out, then push them steadily into her sphincter. She moans and arches her back."
            $ the_person.change_arousal(10)
            "Her backdoor seems lubed up now, but your cock is a little dry. You lean forward and stick your cock in her cunt this time."
            the_person "Oh! Mmmmmm..."
            $ the_person.change_arousal(10)
            "You give her a several strokes, then pull out. Your erection is slick with her arousal."
        "You work slowly, but with steady pressure, you push yourself into [the_person.possessive_title]'s tight anal passage."
    "Buried inside her, you let your weight pin her to the couch as you start to fuck her."
    if the_person.arousal_perc < 40: #Spank her to warm her up
        "You push yourself up a bit. [the_person.title] is still getting warmed up, and you have an idea of how to help."
        $ play_spank_sound()
        "*SMACK*"
        "You give her ass a solid spank. She yelps, but arches her back, pushing your cock deeper."
        mc.name "Sorry. Your ass is just so spankable. You love it when I treat you this way, don't you?"
        the_person "I do, I love it when you do anything you want to me..."
        $ play_spank_sound()
        "*SMACK*"
        mc.name "Sounds about right. Let's get this started off right then."
        "You push your weight down again, leaving her helplessly pinned to the couch as you start fucking her puckered hole earnestly."
    elif the_person.arousal_perc < 65:   #Pull her hair
        if the_person.is_bald:
            "Your reach up and pull back by her neck."
        else:
            "Your reach up and run your hand though her hair, then grab a bunch at the base and pull back."
        $ play_moan_sound()
        the_person "Oh my god... ooohhhhh..."
        "She is moaning as you thrust yourself in hard and deep. [the_person.possessive_title] is taking your cock like a slut."
        mc.name "That's it. Be a good little cum dump and take it."
        $ play_moan_sound()
        "She can only moan as you continue to have your way with her."
    elif the_person.arousal_perc < 90:   #dominate her
        mc.name "That's it. Your ass is nothing more than my personal cocksleeve, here to use as I wish."
        mc.name "You like being used, don't you? Every hole is an opportunity to pleasure a man and make him cum."
        mc.name "Don't worry. You're doing great."
        the_person "Oh god, thank you, I..."
        "Her words get caught in her throat as you fuck her forbidden hole mercilessly."
    else:                           #Tell her how you're gonna cum
        mc.name "You're getting close, aren't you? You little butt slut. I bet you're gonna love it when I pull out and cum all over your slutty ass."
        the_person "Yeah! Oh..."
        mc.name "Or maybe I shouldn't. Maybe I should just let go with my arms and pin you to the couch while I cum inside your hungry back door. Do you want that?"
        the_person "Oh fuck... I want both!"
        mc.name "Well you can't have both, bitch!"
        the_person "Oh fuck, I'm... I'm gonna..."
        "You pound her puckered hole mercilessly. She is obviously going to cum soon."
    $ the_person.call_dialogue("sex_responses_anal")
    $ the_person.change_arousal(18 * (1.0 + 0.1 * mc.sex_skills["Anal"]))
    $ mc.change_arousal(15 * (1.0 + 0.1 * the_person.sex_skills["Anal"]))
    $ mc.change_locked_clarity(200)
    $ mc.change_energy(-12, add_to_log = False)
    if the_person.arousal_perc > 100 and mc.arousal_perc < 100:
        call orgasm_prone_anal(the_person, gaming_cafe, make_couch()) from _myra_alexia_anal_teamup_orgasm_01
        $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 100, reset_arousal = False)
        $ the_person.change_arousal(-70)
    elif mc.arousal_perc > 100:
        $ her_orgasm = False
        if the_person.arousal_perc > 100:
            $ her_orgasm = True
        "You get to hear every little gasp and moan from [the_person.title] as you're pressed up against her. Combined with the feeling of fucking her ass it's not long before you're pushed past the point of no return."
        mc.name "I'm going to cum!"
        if her_orgasm:
            the_person "Oh fuck, me too [the_person.mc_title]!!!"
            "[the_person.title] is pushing her ass back against you desperately."
        $ the_person.call_dialogue("cum_anal")
        $ climax_controller = ClimaxController(["Cum inside of her", "anal"],["Cum on her ass","body"])
        $ the_choice = climax_controller.show_climax_menu()

        if the_choice == "Cum inside of her":
            "You use your full weight to push your cock deep inside of [the_person.possessive_title]'s ass as you climax. She gasps and moans as you pin her to the couch."

            $ climax_controller.do_clarity_release(the_person)
            #$ the_person.call_dialogue("cum_anal")
            $ the_person.cum_in_ass()
            $ scene_manager.update_actor(the_person)
            if her_orgasm:
                "[the_person.title]'s ass begins to spasm around you, as she joins you in orgasm. It feels incredible."
            if the_person.has_cum_fetish or the_person.has_anal_fetish:
                "[the_person.possessive_title]'s body goes rigid as your cum pours into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
                the_person "Oh... OH! Yes [the_person.mc_title]! Pump it deep! I was made to take your cum inside me!"
                "[the_person.possessive_title] revels in having her fetish fulfilled."
                if not her_orgasm:
                    $ her_orgasm = True
                    "[the_person.title]'s ass starts to spasm around you. It seems her anal creampie has triggered her own orgasm."
                    "She moans like a whore as you finish filling her up."
            else:
                the_person "Oh god it's so deep."

        elif the_choice == "Cum on her ass":
            $ the_person.cum_on_ass()
            $ scene_manager.update_actor(the_person)
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_person.title]'s ass."
            $ climax_controller.do_clarity_release(the_person)
            if the_person.has_cum_fetish:
                "[the_person.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_person.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            if the_person.is_submissive:
                "[the_person.title] lays there, whimpering. It seems you nearly fucked her senseless, and she loved it."
                $ the_person.change_happiness(10)
            elif the_person.is_dominant:
                "[the_person.title] lays there, whimpering. It seems you nearly fucked her senseless, and it scared her."
                $ the_person.change_stats(happiness = -5, obedience = 2)
            "You sit back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s exhausted body covered in your semen."
            if her_orgasm:
                "She slowly recovers from her own orgasm."
        if her_orgasm:
            $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 100, reset_arousal = False)
            $ the_person.change_arousal(-50)
        $ mc.reset_arousal()
    else:
        "After a while of fucking her ass, you pull out from [the_person.possessive_title]. It might be time to move on to another needy hole."
    return

label myra_alexia_teamup_vaginal_prone(the_person, warmed_up = True):
    "You get on top of [the_person.title]. You can't wait to use her cunt for your pleasure."
    if warmed_up:
        "[the_person.possessive_title]'s pussy is engorged with arousal from your previous fucking."
        "You line yourself up, then slowly push into her quivering pussy."
    else:
        "[the_person.possessive_title]'s pristine pussy looks inviting, but you know she probably needs to get warmed up a bit."
        "You push forward, your cock right at her entrance. But instead of pushing it inside of her, you thrust along the length of her labia."
        $ the_person.change_arousal(10)
        the_person "Mmm... you feel so hard..."
        "You let yourself grind against her cunt for a few seconds, getting your cock lubed up with her arousal."
        "When you feel ready, you line yourself up, then slowly push into her pussy."
    if the_person.arousal_perc < 40: #Grab her shoulders
        "You put your hands on [the_person.title]'s shoulders. The leverage helps you pound her harder."
        $ play_moan_sound()
        the_person "Oh my god... ooohhhhh..."
        "She is moaning as you thrust yourself in hard and deep. [the_person.possessive_title] is taking your cock like a slut."
        mc.name "That's it. Be a good little cum dump and take it."
        $ play_moan_sound()
        "She can only moan as you continue to have your way with her."
        "You push your weight down again, leaving her helplessly pinned to the couch as you fuck her."
    elif the_person.arousal_perc < 65:   #Pull her hair
        if the_person.is_bald:
            "Your reach up and pull back by her neck."
        else:
            "Your reach up and run your hand though her hair, then grab a bunch at the base and pull back."
        $ play_moan_sound()
        the_person "Oh my god... ooohhhhh..."
        "She is moaning as you thrust yourself in hard and deep. [the_person.possessive_title] is taking your cock like a slut."
        mc.name "That's it. Be a good little cum dump and take it."
        $ play_moan_sound()
        "She can only moan as you continue to have your way with her."
    elif the_person.arousal_perc < 90:   #dominate her
        "Being completely in control of [the_person.possessive_title] as you pound her prone is such a turn on."
        "She is arching her back and moaning loudly as you fuck her."
        the_person "Fuck me [the_person.mc_title], your cock feels so good!"
        mc.name "Damn right it's good. You are such a cock hungry slut, your holes are just begging to be stuffed."
        mc.name "Don't worry, I'm gonna fuck all your slutty holes until you can barely walk!"
        "You grab her by the hair and pull a little bit as you fuck her harder for a bit."
    else:                           #Tell her how you're gonna cum
        mc.name "You're getting close, aren't you? You such a good slut. Do you want my cum too?"
        the_person "Yeah! Oh... yes please!"
        if mc.arousal_perc < 80:
            mc.name "I might even give it to you. I don't cum as easy as a whore like you though."
        else:
            mc.name "That's right. You act like you just want to play games, but really you are just here for a chance at my cum, aren't you?"
        "You speed up. [the_person.possessive_title] is going to cum soon."
    $ the_person.call_dialogue("sex_responses_anal")
    $ the_person.change_arousal(18 * (1.0 + 0.1 * mc.sex_skills["Vaginal"]))
    $ mc.change_arousal(15 * (1.0 + 0.1 * the_person.sex_skills["Vaginal"]))
    $ mc.change_locked_clarity(200)
    $ mc.change_energy(-12, add_to_log = False)
    if the_person.arousal_perc > 100 and mc.arousal_perc < 100:
        call orgasm_prone_bone(the_person, gaming_cafe, make_couch()) from _myra_alexia_vaginal_teamup_orgasm_01
        $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 100, reset_arousal = False)
        $ the_person.change_arousal(-70)
    elif mc.arousal_perc > 100:
        $ her_orgasm = False
        if the_person.arousal_perc > 100:
            $ her_orgasm = True
        "You get to hear every little gasp and moan from [the_person.title] as you're pressed up against her. Her quivering pussy soon pushes you past the point of no return."
        mc.name "I'm going to cum!"
        if her_orgasm:
            the_person "Oh fuck, me too [the_person.mc_title]!!!"
            "[the_person.title] is pushing her ass back against you desperately."
        $ the_person.call_dialogue("cum_pullout")
        $ climax_controller = ClimaxController(["Cum inside of her", "pussy"],["Cum on her ass","body"])
        $ the_choice = climax_controller.show_climax_menu()
        if the_choice == "Cum inside of her":
            "You use your full weight to push your cock deep inside of [the_person.possessive_title]'s cunt as you climax. She gasps and moans as you pin her to the couch."
            $ climax_controller.do_clarity_release(the_person)
            #$ the_person.call_dialogue("cum_anal")
            $ the_person.cum_in_vagina()
            $ scene_manager.update_actor(the_person)
            if her_orgasm:
                "[the_person.title]'s cunt begins to spasm around you, as she joins you in orgasm. It feels incredible."
            if the_person.has_cum_fetish or the_person.has_breeding_fetish:
                "[the_person.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                the_person "Oh... OH! Yes [the_person.mc_title]! Pump it deep! I was made to take your cum inside me!"
                "[the_person.possessive_title] revels in having her fetish fulfilled."
                if not her_orgasm:
                    $ her_orgasm = True
                    "[the_person.title]'s cunt starts to spasm around you. It seems her anal creampie has triggered her own orgasm."
                    "She moans like a whore as you finish filling her up."
            else:
                the_person "Oh god it's so deep."
        elif the_choice == "Cum on her ass":
            $ the_person.cum_on_ass()
            $ scene_manager.update_actor(the_person)
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_person.title]'s ass."
            $ climax_controller.do_clarity_release(the_person)
            if the_person.has_cum_fetish:
                "[the_person.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
                "[the_person.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
                "She truly is addicted to your cum."
            if the_person.is_submissive:
                "[the_person.title] lays there, whimpering. It seems you nearly fucked her senseless, and she loved it."
                $ the_person.change_happiness(10)
            elif the_person.is_dominant:
                "[the_person.title] lays there, whimpering. It seems you nearly fucked her senseless, and it scared her."
                $ the_person.change_stats(happiness = -5, obedience = 2)
            "You sit back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s exhausted body covered in your semen."
            if her_orgasm:
                "She slowly recovers from her own orgasm."
        if her_orgasm:
            $ the_person.have_orgasm(force_trance = True, sluttiness_increase_limit = 100, reset_arousal = False)
            $ the_person.change_arousal(-50)
        $ mc.reset_arousal()
    else:
        "After a while of fucking her, you pull out from [the_person.possessive_title]. It might be time to move on to another needy hole."
    return
