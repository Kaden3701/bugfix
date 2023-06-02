#Saturday morning coffee with the sisters.
#This label stays pretty tame until we unlock public sex options.
#Order goes:
# - Buy coffees
# - Stephanie Dialogue
# - Ashley Dialogue
# - Progression Dialogue


init 5 python:
    add_label_hijack("normal_start", "activate_ashley_stephanie_mod_core")
    add_label_hijack("after_load", "update_ashley_stephanie_mod_core")

    def ashley_stephanie_scene_mod_initialization():
        ashley_stephanie_progression_scene_init()
        return

label activate_ashley_stephanie_mod_core(stack):
    python:
        ashley_stephanie_scene_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_ashley_stephanie_mod_core(stack):
    python:
        if "ashley_stephanie_progression_scene" not in globals():
            ashley_stephanie_progression_scene_init()
        else:
            ashley_stephanie_progression_scene.compile_scenes(ashley_stephanie_progression_scene)
        execute_hijack_call(stack)
    return



init 1 python:
    def ashley_stephanie_progression_scene_0_req(the_group):    #Requirements for the basic scene. Should almost always be true.
        return True

    def ashley_stephanie_progression_scene_1_req(the_group):    #Requirements fo the second stage.
        if the_group[1].sluttiness > 20:
            return True
        return False

    def ashley_stephanie_progression_scene_2_req(the_group):
        if the_group[1].sluttiness > 40 and the_group[0].sluttiness > 20:
            return True
        return False

    def ashley_stephanie_progression_scene_action_req(the_person):  #Use this function to determine the requirement for when to actually run the scene itself.
        if the_person.location == stephanie.location and day%7 == 6 and time_of_day == 0:
            return True
        return False

    def ashley_stephanie_unit_test_func(the_group):
        for person in the_group:
            person.change_slut(30)
            person.change_energy(200)
        mc.change_energy(200)
        return

init 2 python:
    def ashley_stephanie_progression_scene_compile_scenes(the_progression_scene):
        #WARNING: The order of the following lists is critical! They are referenced based on their indexes!!!
        the_progression_scene.start_scene_list = ["ashley_stephanie_progression_scene_intro_0"]
        the_progression_scene.req_list = [ashley_stephanie_progression_scene_0_req, ashley_stephanie_progression_scene_1_req, ashley_stephanie_progression_scene_1_req]
        the_progression_scene.trans_list = ["ashley_stephanie_trans_scene_0", "ashley_stephanie_trans_scene_1", "ashley_stephanie_trans_scene_2"]
        the_progression_scene.final_scene_list = ["ashley_stephanie_progression_scene_0", "ashley_stephanie_progression_scene_1", "ashley_stephanie_progression_scene_2"]
        the_progression_scene.regress_scene_list = []   #Add labels for regression here if desired.
        return

    ashley_stephanie_progression_scene_action = Action("Coffee with Ashley and Stephanie", ashley_stephanie_progression_scene_action_req, "ashley_stephanie_progression_scene_action_label")

    def ashley_stephanie_progression_scene_init():  #Run this during init only
        global ashley_stephanie_progression_scene
        ashley_stephanie_progression_scene = Progression_Scene(
            compile_scenes = ashley_stephanie_progression_scene_compile_scenes,
            start_scene_list = [],  #Set via the compile action
            req_list = [],  #Set via the compile action
            trans_list = [],    #Set via the compile action
            final_scene_list = [],  #Set via the compile action
            intro_scene = "ashley_stephanie_progression_scene_intro_scene", #Scene that plays the first time this scene is run
            exit_scene = "ashley_stephanie_progression_scene_exit_scene",   #Scene for if the player chooses to exit the scene
            progression_scene_action = ashley_stephanie_progression_scene_action,      #The action used to call for this progression scene.
            choice_scene = "ashley_stephanie_progression_scene_choice",   #The action used to let player decide if they want to continue the scene or leave
            stage = -1,     #-1 will play the intro
            person_action = True,   #If this progression scene should run when encountering a person
            business_action = False,    #If this progression scene is a mandatory business event
            is_random = False,  #If this progression scene is a randomly occuring crisis event
            unit_test_func = ashley_stephanie_unit_test_func,  #Set a custom unit test function to test this progression event. Runs between every cycle
            advance_time = True,    #Currently this is broke. Advance time in the scenes themselves for now...
            is_multiple_choice = False, #If MC can choose what final scene he wants
            multiple_choice_scene = None,   #The scene that lets MC choose which final scene he wants.
            regress_scene_list = [])    #If the scene can regress, fill this with appropriate regression scenes to play between intro and final scenes.
        ashley_stephanie_progression_scene.compile_scenes(ashley_stephanie_progression_scene)   #This will populate the scenes that are blank above.


label ashley_stephanie_progression_scene_action_label(the_person):  #Use (the_person) if this event is attached to a person, otherwise leave params blank, EG: ashley_stephanie_progression_scene_action_label():
    "You can use this section to setup anything that is universal to the whole scene, EG location, etc."
    call progression_scene_label(ashley_stephanie_progression_scene, [the_person, stephanie]) from _ashley_stephanie_progression_scene_call_test_01  #[the_person] parameter should be a list of people in the scene itself, IE [mom], [mom,lily], [sarah,erica,mom], etc
    return

label ashley_stephanie_progression_scene_intro_scene(the_group):
    $ the_person = ashley
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(stephanie, position = "sitting")
    $ mc.business.add_mandatory_crisis(ashley_blows_during_meeting)
    "As you are walking downtown, you pass by the coffee shop. Looking inside, you are surprised to see [ashley.fname] and [stephanie.fname] sitting inside."
    "You decide to step inside and say hello."
    mc.name "Hey girls, good to see you."
    "They are surprised to see you. [ashley.fname] blushes and looks down at her coffee as [stephanie.fname] responds."
    stephanie "Hey boss! Me and Ash are just having a cup of coffee before we go our separate ways. It's kind of become our little tradition every Sunday morning, since she moved in with me."
    "She looks over at her sister and starts to tease her."
    stephanie "I think she said something about hitting up the gym today... I think there's a guy she's trying to impress!"
    the_person "Oh my gosh Steph, stop it!"
    "[the_person.title] is blushing, and once in a while sneaks a peek up at you. Even though you've already discussed with her how you want things to be with her, it is cute to see her squirm a little."
    mc.name "Is that true [the_person.title]? Who might this lucky guy be?"
    the_person "Ah. Errm... Well..."
    "She's sputtering out unintelligible mumbles."
    stephanie "Don't worry Ash. I'm sure whoever it is will appreciate you putting in the time to keep your body fit!"
    "[the_person.possessive_title] is relieved when her sister intervenes and changes the subject."
    stephanie "Hey, why don't you grab a coffee and join us? It's kind of nice to hang out in a non-work environment."
    mc.name "Oh, I wouldn't want to interrupt you two having some family time together..."
    "Surprisingly, it's [the_person.title] that interrupts you."
    the_person "It's fine! We live together, remember?"
    "You raise an eyebrow. It's not often that she speaks up, but clearly [the_person.title] wants you to hang out too. Suddenly, she realizes she is speaking up and quiets down."
    the_person "I mean... It would be okay, right? We don't mind at all..."
    mc.name "Okay. Just give me a moment and I'll get something. Either of you two want something while I'm in line?"
    "The sisters look at each other. [the_person.title] shakes her head and [stephanie.possessive_title] responds."
    stephanie "No thanks! We're good for now, but maybe another time we'll let you buy us coffees!"
    "You excuse yourself and head up to the counter. You glance back at the two sisters as you wait in line."
    "It's amazing how similar the girls are, but still so different. [the_person.title] is so quiet and shy, but sometimes when you talk with her you can see glimpses of the fiery passions that drive [stephanie.title]."
    "You order your coffee, and soon the hot brew is in your hand. As you walk back to the table, you decide to use the opportunity to try and get to know them both a little better."
    "The sisters are sitting opposite to each other at the booth... Who should you sit next to?"
    menu:
        "[the_person.fname]" if not ashley_is_secret_path():    #Depending on previous choices, MC may have to sit next to a particular girl.
            "[the_person.possessive_title] scoots over to give you room to sit next to her. She sneaks a peek at you and you see a slight smile on her lips."
            $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = .1, zoom = 1.1))
            $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = -.1, zoom = 0.9))
            $ the_person.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(the_person)
        "[stephanie.fname]" if not ashley_is_normal_path():
            "[stephanie.possessive_title] scoots over so you have room to sit next to her."
            stephanie "Have a seat, [stephanie.mc_title]."
            $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.1, zoom = 0.9))
            $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .1, zoom = 1.1))
            "She pats the seat next to her. You sit down and see her smirking at you before she keeps talking to her sister."
            $ stephanie.change_stats(love = 3, happiness = 5)
            $ ashley_set_coffee_partner(stephanie)
    "You listen to the two sisters chat for a bit as you enjoy your coffee. [the_person.title] seems to almost forget you are at the table, and you get a glimpse into her personality as she talks with her older sibling."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "... but yeah, I have to say I [text_one] [text_two]"
    if the_person.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person.title] felt that way."
    "The sisters discuss it for a bit. You kind of zone out for a little bit as the conversation changes to clothing. The girls are discussing some different brands..."
    "Suddenly the girls stop talking. You look up and notice they are both looking out the window. A woman is walking by the coffee shop window out in the street."
    call coffee_time_woman_walks_by_label() from _coffee_time_prog_scene_intro_outfit_01
    stephanie "Well, I'd better get going. I've got some errands to run!"
    "You stand up and both girls also get up."
    mc.name "Thank you for the pleasant morning. You two have a good day."
    stephanie "You bet boss! We do this pretty much every Sunday. Feel free to join us!"
    "[stephanie.possessive_title]'s invitation is tempting. [the_person.title] is smiling at you, clearly mirroring her sister's invitation to join again."
    stephanie "Next week you're buying the coffees though!"
    mc.name "That's acceptable. With us all being employees, I'll just put it down as a company expense."
    "You say your goodbyes and go separate ways. This could be an interesting opportunity in the future to learn more about the sisters."

    $ ashley_reset_coffee_partner()
    $ scene_manager.clear_scene()
    return
    #You probably want to to advance time after this
    # call advance_time from _call_advance_ashley_stephanie_progression_scene_adv_01

label ashley_stephanie_progression_scene_intro_0(the_group):
    $ the_person = the_group[0]
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped, position = "sitting")
    $ scene_manager.add_actor(stephanie, position = "sitting")
    "You swing by the coffee shop. Right on time, you see [the_person.title] and [stephanie.title] in a booth. You walk over to the table."
    mc.name "Good morning!"
    stephanie "Good morning [stephanie.mc_title]! Are you here to join us?"
    the_person "Yeah, you should buy us coffees. We worked hard this week!"
    "[the_person.possessive_title] gives you a little wink."

    # if not the_person.event_triggers_dict.get("second_date", False) and the_person.sluttiness > 60 and stephanie.sluttiness > 40 and ashley_is_secret_path():
    #     call ashley_second_concert_intro_label(the_person) from _start_ashley_second_date_path_01

    return

#For more progression, add more scenes.

label ashley_stephanie_progression_scene_0(the_group):
    $ the_person = the_group[0]
    call coffee_time_banter_label(the_group) from _coffee_time_banter_prog_scene_00
    "The conversation is starting to die down a bit, and your coffee cup is dry. You decide to head out."
    mc.name "Thank you for the company. I think it's about time for me to go."
    stephanie "Hey, you know where to find us next week!"
    the_person "Bye [the_person.mc_title]..."
    $ scene_manager.clear_scene()
    return

label ashley_stephanie_progression_scene_1(the_group):
    $ the_person = the_group[0]
    call coffee_time_banter_label(the_group) from _coffee_time_banter_prog_scene_01
    $ cum_on_hand = False
    "Without any provocation, you feel [stephanie.possessive_title]'s hand on your thigh. She is rubbing back and forth, but is slowly drifting higher."
    "[stephanie.title] is keeping a completely inconspicuous attitude."
    stephanie "So Ash, any good concerts coming up soon?"
    "As she asks her sister, her hand drifts up to your crotch. It rapidly hardens as she begins to stroke it carefully."
    $ mc.change_locked_clarity(20)
    the_person "No... Not that I'm aware of anyway... The Chicago symphony is doing a charity live-stream later though, so I might watch that..."
    "You decide two can play at this game. In the same way, you carefully run your hand along her thigh until it's resting on her mound. She gives a small sigh when you start to apply pressure on it."
    $ stephanie.change_arousal(15)

    "You and [stephanie.title] pet each other for a few minutes, but stroking each other through you clothes can only take things so far."
    if stephanie.get_opinion_score("public sex") > 0:
        "She decides to push things further. You feel her hand clumsily reach into your pants, eventually pulling your cock out. The soft skin of her hand feels great."
        "Not to be outdone, you bring your hand up [stephanie.fname]'s body, then slowly slide it under her clothes. When you get to her slit, you push you middle finger inside of her, while pressing your palm against her clit."
        "She sighs, but doesn't seem particularly concerned about other people around."
        $ mc.change_locked_clarity(20)
    else:
        "Not content to leave things where they are, you take the next step. You bring your hand up [stephanie.possessive_title]'s body, then slowly slide it under her clothes."
        "She squirms a bit and glances around nervously as your hand reaches her slit. She sighs when your middle finger pushes inside of her, but is on alert for anyone who might be watching."
        "Not to be outdone, [stephanie.title] starts to undo your zipper. She clumsily reaches into your pants and pulls your cock out. The soft skin of her hand feels great as she starts to stroke you."
        $ mc.change_locked_clarity(20)
    $ stephanie.change_arousal(30)

    "You and [stephanie.title] continue to pet each other at the booth, sipping your coffees once in a while with your free hands."
    "Across the table, [the_person.title] appears to be completely oblivious. [stephanie.possessive_title] is beginning to squirm as you stroke her g-spot with your finger."
    $ stephanie.change_arousal(30)
    the_person "So... I'm thinking about going to the spa later to treat myself to something... Do you want to go Steph?"
    stephanie "Oh!!! Uhh... Yesssss..."
    "[stephanie.title] practically growls. She's getting close and having trouble hanging on. You use the palm of your hand to grip her pussy harder, while your finger runs circles around her g spot."
    $ stephanie.change_arousal(30)
    $ mc.change_locked_clarity(20)
    "She stops stroking you as she finishes. She leans forward a bit, closing her eyes as her pussy begins quivering around your finger."
    "You wish your cock was inside her instead of your finger, but in a public place like a coffee shop booth, you can't justify risking it."
    $ stephanie.have_orgasm(half_arousal = False)
    if stephanie.get_opinion_score("public sex") > 0: #[If Steph likes public sex, she finishes you no matter what.]
        "[stephanie.possessive_title] eventually opens her eyes, taking a quick peek around, then begins stroking you again."
        "Seems she is intent on giving you a similar treatment. You slowly pull your hand out of her clothes."
        stephanie "Are you going to look at those tops we were looking at the other day Ash?"
        "[stephanie.title] picks up the conversation with her sister."
        stephanie "I really liked the way that crop top look on you."
        "Some of your precum is starting to leak out. [stephanie.possessive_title] uses her thumb to spread it around the tip then keeps stroking."
        $ mc.change_locked_clarity(20)
        the_person "I don't know... I like the shirt but I don't know if I like how much skin it shows..."
        stephanie "Aww, you should try it anyway! Guys like seeing a little midriff. Don't you agree [stephanie.mc_title]?"
        "This time it's you who is barely able to get a reply out."
        mc.name "Ah yes. Yes it's very nice."
        "[the_person.title] raises an eyebrow. You think she is probably finally beginning to sense something is up..."
        mc.name "I mean, only if you feel comfortable with it..."
        "You manage to get out. She seems to buy it for now."
        the_person "I guess..."
        "The conversation continues, but you stop listening. The soft hand of [stephanie.title] drives you over the edge and you start to cum in her hand."
        "Your cum spurts up and hits the bottom of the table before falling back down onto [stephanie.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = stephanie)
        $ cum_on_hand = True
    else: #[Steph neutral or doesn't like public sex, give player the option]
        "As [stephanie.title] regains her senses, she looks around for a moment. She looks at you and gives you a couple tentative strokes, clearly unsure of what to do."
        menu:
            "Keep going":
                "You slowly pull your hand away from [stephanie.possessive_title]'s crotch. You put your hand on hers and encourage her to stroke you, making it clear that you expect her to continue."
                "She looks around nervously but begins jacking you off again on her own."
                $ mc.change_locked_clarity(20)
                mc.name "So what are you thinking about getting done at the Spa? I hear they have really good service there."
                "You keep the conversation going so Steph can concentrate on her work. You are starting to leak precum, making her handjob feel even better."
                the_person "Oh, ahh, well I want to get my nails done for sure..."
                "[the_person.possessive_title] starts to explain. However, [stephanie.title] is looking around nervously and she is starting to notice."
                the_person "You okay Steph? You seem preoccupied..."
                "She startles and looks back at her sister."
                stephanie "Oh! Yeah I just thought I saw someone..."
                "Under the table you are reaching your limit. The soft hand of [stephanie.title] drives you over the edge and you start to cum in her hand."
                "Your cum spurts up and hits the bottom of the table before falling back down onto [stephanie.possessive_title]'s hand and your pants. Oh fuck you are making a mess..."
                $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = stephanie)
                $ cum_on_hand = True
            "Stop":
                "While [the_person.possessive_title] is looking something up on her phone, you whisper into [stephanie.title]'s ear."
                mc.name "Sorry, I don't want to make a mess here..."
                if stephanie.is_girlfriend:
                    "[stephanie.title] leans over and whispers in your ear."
                    stephanie "That's okay... maybe I can come over tonight and make it up to you?"
                    $ mc.change_locked_clarity(20)
                    menu:
                        "Have her come over" if schedule_sleepover_available():
                            "You give her a nod. She takes that as her cue to stop."
                            stephanie "I'll see you tonight then..."
                            $ schedule_sleepover_in_story(stephanie)
                        "Have her come over (disabled)" if not schedule_sleepover_available():
                            pass
                        "Not tonight":
                            mc.name "I can't tonight, maybe another night..."
                "[stephanie.possessive_title] releases your erection, leaving it aching with need. You quickly put yourself away and zip up as [the_person.title] finishes pulling up a picture on her phone."
                the_person "So I was thinking about getting my haircut to something like this... What do you think?"
                "You continue your coffee date with the sisters, with [the_person.title] unaware of you getting her sister off right in front of her."
    if cum_on_hand:
        "[stephanie.title] checks her hand while it's still under the table. It is absolutely coated in your cum."
        if stephanie.get_opinion_score("public sex") >= 0 and (stephanie.get_opinion_score("drinking cum") >= 0 or stephanie.get_opinion_score("drinking cum") > 0):
            if the_person.sluttiness < 40:
                "[stephanie.possessive_title] beings her hand up from underneath the table and begins to lick your cum off of it. [the_person.title] notices and looks puzzled for a second, then realizes what she is doing."
                the_person "Jesus Steph... Can you two seriously not keep your hands off each other for two seconds? You are nuts!"
                "[the_person.title] looks at you, jealousy clear on her face."
                $ the_person.change_obedience(-3)
                # TODO Ash gains sluttiness, loses obedience and love
            else:
                "[the_person.title] just watches as [stephanie.title] brings her hand up from underneath the table and begins to lick your cum off of it."
                "She looks at you with jealousy clear on her face."
                $ the_person.change_obedience(-3)
        else:
            "You pick up a napkin and bring it under the table. You hold it in place as [stephanie.title] wipes her hand off on it. You grab another napkin and use it to clean yourself off as best you can, hoping no one will notice."
    "The conversation is starting to die down a bit, and your coffee cup is dry. You decide to head out."
    mc.name "Thank you for the company. I think it's about time for me to go."
    stephanie "Hey, you know where to find us next week!"
    the_person "Bye [the_person.mc_title]..."
    $ scene_manager.clear_scene()
    return

label ashley_stephanie_progression_scene_2(the_group):
    $ the_person = the_group[0]
    call coffee_time_banter_label(the_group) from _coffee_time_banter_prog_scene_02
    $ cum_on_hand = False
    "Without any provocation, you feel [stephanie.possessive_title]'s hand on your thigh. She is rubbing back and forth, but is slowly drifting higher."
    "[stephanie.title] is keeping a completely inconspicuous attitude."
    stephanie "So Ash, any good concerts coming up soon?"
    "As she asks her sister, her hand drifts up to your crotch. It rapidly hardens as she begins to stroke it carefully."
    $ mc.change_locked_clarity(20)
    the_person "No... Not that I'm aware of anyway... The Chicago symphony is doing a charity live-stream later though, so I might watch that..."
    "You decide two can play at this game. In the same way, you carefully run your hand along her thigh until it's resting on her mound. She gives a small sigh when you start to apply pressure on it."
    $ stephanie.change_arousal(15)

    "You and [stephanie.title] pet each other for a few minutes, but stroking each other through you clothes can only take things so far."
    if stephanie.get_opinion_score("public sex") > 0:
        "She decides to push things further. You feel her hand clumsily reach into your pants, eventually pulling your cock out. The soft skin of her hand feels great."
        "Not to be outdone, you bring your hand up [stephanie.fname]'s body, then slowly slide it under her clothes. When you get to her slit, you push you middle finger inside of her, while pressing your palm against her clit."
        "She sighs, but doesn't seem particularly concerned about other people around."
        $ mc.change_locked_clarity(20)
    else:
        "Not content to leave things where they are, you take the next step. You bring your hand up [stephanie.possessive_title]'s body, then slowly slide it under her clothes."
        "She squirms a bit and glances around nervously as your hand reaches her slit. She sighs when your middle finger pushes inside of her, but is on alert for anyone who might be watching."
        "Not to be outdone, [stephanie.title] starts to undo your zipper. She clumsily reaches into your pants and pulls your cock out. The soft skin of her hand feels great as she starts to stroke you."
        $ mc.change_locked_clarity(20)
    $ stephanie.change_arousal(30)

    "You and [stephanie.title] continue to pet each other at the booth, sipping your coffees once in a while with your free hands."
    "Across the table, [the_person.title] appears to be completely oblivious. [stephanie.possessive_title] is beginning to squirm as you stroke her g-spot with your finger."
    $ stephanie.change_arousal(30)
    the_person "So I was thinking about going to the spa... Do you think I should..."
    "[the_person.title] stops mid question and is looking at her sister. She quickly realizes what is going on."
    the_person "Wow... I guess I should have expected you two wouldn't be able to keep your hands off each other. I'll just play on my phone while you two do your thing..."
    "[the_person.title] gives you a look of what you can only call pure jealousy, before she pulls out her phone and starts looking at it."
    "You feel [the_person.title]'s foot beneath the table begin to rub along your leg."
    $ mc.change_locked_clarity(30)
    "You push the palm of your hand rigidly against [stephanie.possessive_title]'s clit, while your middle finger strokes her g-spot. Your attention to her sensitive spots soon has her gasping."
    "Only a whimper escapes her lips when you feel her pussy begin to quiver around your finger. She stops stroking you as she focuses on the pleasure of orgasming in the palm of your hands."
    $ stephanie.have_orgasm(half_arousal = False)
    "After several seconds, [stephanie.title] slowly opens her eyes and glances around as you withdraw your hand."

    stephanie "Hey Ash... Can you act natural for a minute and cover me? I need to take care of something..."
    "[stephanie.title] gives her sister a wink, and [the_person.title] gives her a nod."
    "[stephanie.possessive_title] looks around to make sure no one is watching, but then slowly sinks in her seat and then slips under the table."
    $ scene_manager.update_actor(stephanie, position = "blowjob")
    "She gets between your legs and immediately goes to work, sucking you off. [the_person.possessive_title] hears the slurping noises start and looks at you."
    $ mc.change_locked_clarity(40)
    the_person "Wow. I bet that feels good."
    "[the_person.title] doesn't say a word, but she puts two fingers in the shape of a V, the brings it to her face and sticks her tongue out between them, then points to herself."
    "She is making it clear she is expecting you to get her off later."
    $ mc.change_locked_clarity(20)
    "The wet tongue of [stephanie.title] is driving you quickly to orgasm. Between the public setting, her partial handjob, and talented mouth, you are sure you can't take any more."
    "You relax and enjoy the blowjob. Soon your orgasm approaches. There's no easy way to warn [stephanie.title], so you just let it go, firing your load into her mouth."
    $ stephanie.cum_in_mouth()
    $ scene_manager.update_actor(stephanie)
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = stephanie)
    "Her talented mouth takes your load easily. When you finish, her mouth slowly releases your cock and you hear a loud gulp."
    "You look around to make sure you are still anonymous before putting your hand on her shoulder and then helping her back up and into her seat."
    $ scene_manager.update_actor(stephanie, position = "sitting")
    "Once back up, she wipes what little cum managed to get on her face with a napkin and sets it aside. [ashley.title] shakes her head."
    $ stephanie.outfit.remove_all_cum()
    $ scene_manager.draw_scene()

    "Your balls are empty and your coffee cup is dry. You decide to head out."
    mc.name "Thank you for the company. I think it's about time for me to go."
    stephanie "Hey, you know where to find us next week!"
    the_person "Bye [the_person.mc_title]..."
    $ scene_manager.clear_scene()
    return

label ashley_stephanie_trans_scene_0(the_group):
    pass
    #This label should probably never be called.
    return

label ashley_stephanie_trans_scene_1(the_group):
    pass
    return

label ashley_stephanie_trans_scene_2(the_group):
    pass
    return



label ashley_stephanie_progression_scene_choice(the_group):
    $ the_person = the_group[0]
    "You consider it. If you stick around, you could probably sneak a serum into their coffees."
    "Buy the girls' coffee?"
    menu:
        "Stay and Buy Coffee":
            pass
        "Say goodbye and Leave":
            return False
    stephanie "Yay! Can I get an Americano with two creams?"
    the_person "I like mine black..."
    if stephanie.sluttiness > 20:
        stephanie "That's what she said!"
        "The girls are laughing at [stephanie.possessive_title]'s joke as you head up to the counter and order the coffees."
    else:
        "You head up to the counter and order the coffees."
    "When you get your orders, you look back and see the two sisters talking. You could slip a serum into their coffees pretending to add creamer..."
    "You look at [the_person.possessive_title]'s drink."
    call give_serum(the_person) from _call_give_ashley_serum_teamup_03
    "You look at [stephanie.possessive_title]'s drink."
    call give_serum(alexia) from _call_give_stephanie_serum_teamup_04
    $ mc.business.change_funds(-15)
    if stephanie.is_girlfriend:
        "As you wait for your coffees to get made, you spot a yummy looking blueberry muffin. You decide to get it to share with [stephanie.title]."
        $ mc.business.change_funds(-5)
    "You walk back to the table and give the girls their coffee."
    if stephanie.is_girlfriend:
        stephanie "Ohh! Yum, that looks tasty [stephanie.mc_title]."
        "[stephanie.possessive_title] spots your muffin. You slide into the booth next to her."
        $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.1, zoom = 0.9))
        $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .1, zoom = 1.1))
        mc.name "Got it for us to share."
        "You glance over at [the_person.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ ashley_set_coffee_partner(stephanie)
    else:
        "[stephanie.possessive_title] scoots over so you have room to sit next to her."
        stephanie "Have a seat, [stephanie.mc_title]."
        $ scene_manager.update_actor(stephanie, display_transform = character_right(yoffset = -.1, zoom = 0.9))
        $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(yoffset = .1, zoom = 1.1))
        "She pats the seat next to her. You sit down and see her smirking at you as she keeps talking to her sister."
        "You glance over at [the_person.title]. A hint of jealousy crosses her face, but she quickly hides it."
        $ stephanie.change_stats(love = 3, happiness = 5)
        $ ashley_set_coffee_partner(stephanie)
    "As you sit down, the girls are sharing their plans for the weekend. You take a few sips of your coffee enjoying the flavor."
    return True

label ashley_stephanie_progression_scene_exit_scene(the_group):
    $ the_person = the_group[0]
    mc.name "Unfortunately, I am just grabbing a coffee to go. I have other errands to run."
    the_person "That's too bad."
    stephanie "I understand. I'll see you later then."
    "You leave the sisters to their coffee and gossip time."
    $ clear_scene()
    return







#This is for reusable scenes and functions required for the scene.
#If there are any special functions or scenes you want to add, do it here.
#For example, for the above scene, you could write a script where the girl strips her bottoms and presents her ass to MC.

label coffee_time_banter_label(the_group):
    if the_group[0].sluttiness < 30 or the_group[1].sluttiness < 0:
        call coffee_time_innocent_chat_label from _coffee_time_banter_01
    else:
        call coffee_time_sexy_chat_label from _coffee_time_banter_02
    call coffee_time_woman_walks_by_label from _coffee_time_banter_03



label coffee_time_innocent_chat_label():
    $ the_person = ashley
    "The two sisters are chatting about different kinds of things."
    "It's fun to be in a situation where [the_person.title] opens up and actually... talks..."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "... but yeah, I'm not sure he realizes I [text_one] [text_two]."
    if the_person.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [the_person.title] felt that way."
    "The girls keep talking. They keep bouncing back and forth between multiple topics. You just listen as you sip your coffee."
    $ overhear_topic = stephanie.get_random_opinion(include_sexy = False)
    $ text_one = person_opinion_to_string(stephanie, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    stephanie "... But I [text_one] [text_two], so I'm not sure what to do."
    if stephanie.discover_opinion(overhear_topic):
        "Wow, you knew they were sisters, but they really do talk about basically everything!"

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_sexy_chat_label():
    $ the_person = ashley
    "The two sisters are chatting about all kinds of different things."
    "Not surprisingly, the subject of the chatting turns sexual, as the two sisters talk about different sexual encounters."
    $ overhear_topic = stephanie.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(stephanie, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    stephanie "... but yeah, I have to say I [text_one] [text_two]"
    if stephanie.discover_opinion(overhear_topic):
        "Oh! You didn't realize that [stephanie.title] felt that way."
    $ mc.change_locked_clarity(10)
    "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
    $ overhear_topic = the_person.get_random_opinion(include_sexy = True, include_normal = False)
    $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
    $ text_two = get_topic_text(overhear_topic)
    the_person "... But I [text_one] [text_two], so I'm not sure what to do."
    if the_person.discover_opinion(overhear_topic):
        "Wow, you didn't realize they talked about sex in such detail with each other."
    $ mc.change_locked_clarity(10)

    python:
        del overhear_topic
        del text_one
        del text_two
    return

label coffee_time_woman_walks_by_label(): #Whoever's turn it is should be the person one in this label.
    $ the_person = ashley
    $ preferences = WardrobePreference(the_person)
    $ bystander = get_random_from_list(known_people_in_the_game(excluded_people = [ashley, stephanie]))

    if not bystander:
        return  # exit loop if we have no bystander

    "Enjoying your coffee, you zone out for a minute while the two sisters are chatting, when suddenly the talking stops. You look up and see them both looking out the restaurant window."
    "Outside is a woman who has stopped and is checking her phone for something. The girls are checking her out."

    $ scene_manager.add_actor(bystander, display_transform = character_left_flipped, position = "stand3")
    "She takes a moment to look at something on her phone."
    "Then she walks away."
    $ scene_manager.add_actor(bystander, display_transform = character_left_flipped, position = "walking_away")
    "The girls watch as she walks away."
    $ scene_manager.remove_actor(bystander)
    the_person "Wow, did you see that?"
    $ temp_string = bystander.outfit.build_outfit_name()
    stephanie "The [temp_string]?"
    if preferences.evaluate_outfit(bystander.outfit, the_person.sluttiness + 10) == True:
        the_person "Yeah. I really liked it! I could totally see myself wearing something like that."
    else:
        $ temp_string = "I know that the outfit " + preferences.evaluate_outfit_get_return(bystander.outfit, the_person.sluttiness + 10) + ", but what if I did something similar?"
        the_person "[temp_string]"
    "[stephanie.title] considers it for a moment."
    if the_person.approves_outfit_color(bystander.outfit):
        stephanie "I suppose so. I mean the colour was nice."
    else:
        stephanie "I don't know, I don't usually see you wear that colour."
        the_person "I could do something like that but in [the_person.favourite_colour]."
        stephanie "That would be interesting."
    "[the_person.possessive_title] sips her coffee and thinks about it for a bit."
    stephanie "What do you think [stephanie.mc_title]? Sometimes it's easy to fall into the trap of just wearing what is comfortable. Do you think she would look good in that?"
    if stephanie.is_girlfriend:
        "[the_person.possessive_title] glances at you. She tries not to show it, but you can tell she is interested in your opinion."
    else:
        "[the_person.possessive_title] listens to your response intently. You can tell she is interested in your opinion."
    menu:
        "Yes":
            the_person "I think I'm gonna go over to the mall this afternoon and try some stuff on. I could use a new outfit!"
            "Hmm, maybe you should swing by the mall later and help [the_person.title] go clothes shopping?"
            $ ashley_set_observed_outfit(bystander.outfit)
        "No":
            the_person "Ahh..."
            "[the_person.possessive_title] sinks down in her seat a bit. You can tell she is a little embarrassed."

    python:
        del bystander
        del preferences
    return
