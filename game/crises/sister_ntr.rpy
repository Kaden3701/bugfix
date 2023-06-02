## Sister NTR Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
init 3 python:
    def sister_ntr_crisis_requirement():
        if not lily.is_available or lily.has_queued_event("sleeping_walk_in_label"):
            return False
        if mc.is_in_bed:
            if not (day % 7 == 4 or day % 7 == 5):  # not on friday or saturday night, conflicts with story
                if lily.effective_sluttiness() >= 30:
                    return True
        return False

    def select_position(person):
        positions = ["bj"]
        if person.vagina_available:
            positions.append("missionary")
            positions.append("wall")
            if person.get_opinion_score("anal sex") > 0 or person.sluttiness > 70:
                positions.append("anal")
        return get_random_from_list(positions)

    def sister_ntr_select_finish(person):
        finishes = []
        if person.get_opinion_score("being covered in cum") > 0 or person.get_opinion_score("cum facials") > 0:
            finishes.append ("facial")
        if person.wants_creampie:
            finishes.append ("inside")
        if person.get_opinion_score("giving blowjobs") > 0 or person.get_opinion_score("drinking cum") > 0:
            finishes.append ("drink")
        finishes.append ("usual")
        return get_random_from_list(finishes)

    sister_ntr_mod_action = ActionMod("Sister NTR",sister_ntr_crisis_requirement,"sister_ntr_crisis_action_label",
        menu_tooltip = "At night you hear strange sounds out of [lily.possessive_title]'s bedroom", category = "NTR",
        initialization = init_action_mod_disabled,
        is_crisis = True)

label sister_ntr_crisis_action_label():
    ## Lily studying with her friends
    $ the_person = lily
    "While trying to fall asleep, you're disturbed by some noise down the hallway."
    menu:
        "Investigate?":
            pass
        "Ignore it":
            return
    "Unable to fall asleep, you decide to investigate."
    "You drag yourself out of bed and down the hallway. There is a trace of light under the door to [the_person.possessive_title]'s bedroom and it is slightly cracked."

    ## Determine what type of encounter it is
    if the_person.sluttiness >= 60:
        $ ran_num = renpy.random.randint(1,2)
    else:
        $ ran_num = 1

    $ mc.change_location(lily_bedroom)
    $ man_name = Person.get_random_male_name()

    if ran_num == 1: ## a scene with one man
        if the_person.sluttiness < 40:
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "You see [the_person.possessive_title] kissing a young man. On the table there are some college books lying around. Seems they decided to take a break from studying."
            the_person "Oh, [man_name]. You are so sweet, agreeing to help me with homework. I could not have done this myself!"
            "Now you recognize the man. It is [man_name], [the_person.possessive_title]'s friend."
            man_name "No a problem at all!"
            "They go back to kissing. [man_name] moves his hands to [the_person.possessive_title] butt and starts caressing it."
            the_person "Mmmmm... Your hands are so gentle..."
            "You see [man_name] starts to undress [the_person.possessive_title]."
            $ the_person.strip_outfit_to_max_sluttiness(narrator_messages = "He takes off [the_person.possessive_title]'s [strip_choice.display_name] and throws it on a chair.")
            the_person "Hold it there, [man_name]. I'm not ready for this. Hope you understand."
            "You see a glimpse of disappointment on man's face, but he regains himself."
            man_name "Sorry, [the_person.fname]. I understand."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            "He gets away from [the_person.possessive_title] and starts picking up his books from the table."
            "Once done, he moves to the door."
            man_name "Thanks for the evening, [the_person.fname]. Say, how about we have a lunch at the cafe next to college tomorrow?"
            the_person "Oh, I like that, [man_name]. I'll give you a call after the class, ok?"
            man_name "Great. See you tomorrow then!"
            $ the_person.change_slut(2, 40)
            "You get back to your room and don't even hear the front door closing. You fall asleep quickly."
        else:
            $ the_person.strip_outfit_to_max_sluttiness()
            $ target_position = select_position(the_person)
            $ the_person.change_arousal (75)
            if target_position == "missionary":
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "You take a look inside the room and you see [the_person.possessive_title] lying on the table with wide spread legs. And some young man is between them with his pants down."
                the_person "Oh, [man_name]! You are so good! Keep going!"
                "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, they've been fucking for a while now."
                if the_person.get_opinion_score("being submissive") > 0:
                    "[man_name] grabs [the_person.possessive_title]'s legs and thrusts himself into her with some force."
                    the_person "Yes, [man_name]. Fuck me harder! Be rough with me!"
                $ the_person.change_arousal (26)
                "After a few more moves, [the_person.possessive_title] seems to have reached an orgasm."
                $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                $ the_person.have_orgasm()
                the_person "Keep fucking me, [man_name]! I'm... cumming!..."
                "Her body shrugs and you see happy smile on her face."
                the_person "You made me cum, [man_name]! I needed that so much!"
                man_name "Don't think I can go on for long, [the_person.fname]."
                $ finish = sister_ntr_select_finish(the_person)
                if finish == "facial":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "Remember the link I sent you, with a girl getting a cum shot? Do that to me, okay?"
                    man_name "With pleasure!"
                    "He strokes his dick for few moments and starts to cover [the_person.possessive_title]'s face with hot semen."
                    $ cum_on_face_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    the_person "Yes! That's it! Cover my face!"
                    "After [man_name] finishes, she looks him in the eyes."
                    the_person "Do I look cute this way?"
                    man_name "You look marvelous, [the_person.fname]. I really liked that."
                    the_person "I loved that too. Now I go wash my face and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Do me again, [man_name]. Fuck me harder! Please cum on my face again!"
                        man_name "On your knees, [the_person.fname]! I'm cumming again!"
                        the_person "Here, take a photo on my phone. I wanna see it too!"
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "inside":
                    the_person "Yes! Do it, [man_name]! I want you to fill me."
                    if the_person.on_birth_control:
                        the_person "Don't worry, I'm on the pill."
                    $ cum_in_vagina_ntr(the_person)
                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                    the_person "Yes, [man_name]! I want it in me!"
                    "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from her pussy."
                    man_name "What a nice view! [the_person.fname] [the_person.last_name] fucked and creampied."
                    "She spreads her legs even more to show her cum drenched pussy."
                    the_person "Hope you like the view. Now I go wash myself and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Take me again, [man_name]. Fuck me hard! I need you to fill me once more!"
                        man_name "On your knees, [the_person.fname]! I want you from behind this time!"
                        the_person "Slap my ass harder! I like it rough!"
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "drink":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls."
                    man_name "I'm gonna cum, [the_person.fname]!"
                    "She just keep on going at steady pace."
                    the_person "Mmmmmm... Mmmm... Uh."
                    $ cum_in_mouth_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "[man_name] moans and starts filling her mouth with his load."
                    man_name "Take it all, [the_person.fname]!"
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    $ play_swallow_sound()
                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows most of it, but you still see traces around her mouth."
                    the_person "Such a wonderful taste, [man_name]! Let me get a glass of water and then we have to finish studying. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Mmmmmm... Brhkhmmm..."
                        man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "usual":
                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                    "[the_person.possessive_title] grabs the tip of his cock to catch all the sperm."
                    man_name "Ow, fuck! That was great!"
                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                    the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                    the_person "Now I go wash my hands and then we go back to our books. I don't want to fail this test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Please, take me once more. I want to feel your hard dick inside again!"
                        man_name "Sure, [the_person.fname]. Get your little pussy ready!"
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif target_position == "wall":
                $ the_person.draw_person(position = "against_wall", emotion = "happy")
                "You take a look inside the room and you see [the_person.possessive_title] pushed against the wall. And some young man is doing her with his pants down."
                the_person "Oh, [man_name]! You are so good! Keep going!"
                "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
                if the_person.get_opinion_score("being submissive") > 0:
                    "[man_name] grabs [the_person.possessive_title]'s buttocks and squeezes them with some force."
                    the_person "Oh, yes, [man_name]. Be rough with me! I love being owned by a man."
                $ the_person.change_arousal (26)
                "After a few more thrusts, [the_person.possessive_title] seems to have reached an orgasm."
                $ the_person.draw_person(position = "against_wall", emotion = "orgasm")
                $ the_person.have_orgasm()
                the_person "Keep fucking me, [man_name]! I'm... cumming!..."
                "Her body shrugs and you see happy smile on her face."
                the_person "You made me cum, [man_name]! I needed that so much!"
                man_name "Don't think I can go on for long, [the_person.fname]."
                $ finish = sister_ntr_select_finish(the_person)
                if finish == "facial":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "Remember the link I sent you, with a girl getting a cum shot? Do this to me, will you?"
                    man_name "And how can I deny that?"
                    "He strokes his dick for few moments and starts to cover [the_person.possessive_title] face with hot semen."
                    $ cum_on_face_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    the_person "Yes! That's it! Cover my face!"
                    "After [man_name] finishes, she looks him in the eyes."
                    the_person "Do I look cute this way?"
                    man_name "You look marvelous, [the_person.fname]. I really liked that."
                    the_person "I loved that too. Now I go wash my face and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Do me again, [man_name]. Fuck me harder! Please cum on my face again!"
                        man_name "On your knees, [the_person.fname]! I'm cumming again!"
                        the_person "Here, take a photo on my phone. I wanna see it too!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "inside":
                    the_person "Yes! Do it, [man_name]! I want you to fill me."
                    if the_person.on_birth_control:
                        the_person "Don't worry, I'm on the pill."
                    $ cum_in_vagina_ntr(the_person)
                    $ the_person.draw_person(position = "against_wall", emotion = "happy")
                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                    the_person "Yes, [man_name]! I want it in me!"
                    "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from her pussy."
                    man_name "What a nice view! [the_person.fname] [the_person.last_name] fucked and creampied."
                    "She spreads her legs even more to show her cum drenched pussy."
                    the_person "Hope you like the view. Now I go wash myself and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Take me again, [man_name]. Fuck me hard! I need you to fill me once more!"
                        man_name "On your knees, [the_person.fname]! I want you from behind this time!"
                        the_person "Slap my ass harder! I like it rough!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "drink":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls."
                    man_name "I'm gonna cum, [the_person.fname]!"
                    "She just keep on going at steady pace."
                    the_person "Mmmmmm... Mmmm... Uh."
                    $ cum_in_mouth_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "[man_name] shrugs and starts filling her mouth with his load."
                    man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    $ play_swallow_sound()
                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                    the_person "Such a wonderful taste, [man_name]! Now I go for a glass of cola and then we go back to our books. I don't want to fail this test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Mmmmmm... Brhkhmmm..."
                        man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "usual":
                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                    "[the_person.possessive_title] grabs the head of his cock as not to spill any sperm."
                    man_name "Ow, fuck! That was great!"
                    $ the_person.draw_person(position = "against_wall", emotion = "happy")
                    the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                    the_person "Now I go wash my hands and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Please, take me once more. I want to feel your hard dick inside again!"
                        man_name "Sure, [the_person.fname]. Get your little pussy ready!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif target_position == "anal":
                $ the_person.draw_person(position = "standing_doggy")
                "You take a look inside the room and you see [the_person.possessive_title] bend over the chair. And some young man thrusts his dick into [the_person.possessive_title] little ass."
                the_person "Oh, [man_name]! You are so good! I like it in my ass."
                "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
                if the_person.get_opinion_score("being submissive") > 0:
                    "[man_name] slaps [the_person.possessive_title]'s buttocks. You see some red there. He must done so before."
                    the_person "Oh, [man_name]. Slap me more! I like that!"
                $ the_person.change_arousal (26)
                "After a few more moves, [the_person.possessive_title] seems to have reached an orgasm."
                the_person "Fuck my ass, [man_name]! I'm... cumming!..."
                "Her body shrugs and you hear a moan of pleasure."
                the_person "You made me cum, [man_name]! I needed that so much!"
                man_name "Don't think I can go on for long, [the_person.fname]."
                $ finish = sister_ntr_select_finish(the_person)
                if finish == "facial":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "Remember the link I sent you, with a girl getting a cum shot? Do this to me, will you?"
                    man_name "And how can I deny that?"
                    "He strokes his dick for few moments and starts to cover [the_person.possessive_title] face with hot semen."
                    $ cum_on_face_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    the_person "Yes! That's it! Cover my face!"
                    "After [man_name] finishes, she looks him in the eyes."
                    the_person "Do I look cute this way?"
                    man_name "You look marvelous, [the_person.fname]. I really liked that."
                    the_person "I loved that too. Now I go wash my face and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Take my ass again, [man_name]. Fuck me harder! And don't forget to cum on my face!"
                        man_name "On your knees, [the_person.fname]! I'm cumming again!"
                        the_person "Here, take a photo on my phone. I wanna see it too!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "inside":
                    the_person "Wait, [man_name]. Please cum in my pussy. I want you to fill me."
                    if the_person.on_birth_control:
                        the_person "Don't worry, I'm on the pill."
                    $ cum_in_vagina_ntr(the_person)
                    $ the_person.draw_person(position = "standing_doggy")
                    "The man take his cock from [the_person.possessive_title] ass and sticks it into her vagina."
                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                    the_person "Yes, [man_name]! I want it in me!"
                    "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from her pussy."
                    man_name "What a nice view! [the_person.fname] [the_person.last_name] fucked and creampied."
                    "She spreads her legs even more to show her cum drenched pussy."
                    the_person "Hope you like the view. Now I go wash myself and then we go back to our books. I don't want to fail this test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Take me again, [man_name]. Fuck me hard! I need you to fill me once more!"
                        man_name "On your knees, [the_person.fname]! I want you from behind this time!"
                        the_person "Slap my ass harder! I like it rough!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "drink":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                    the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls."
                    man_name "I'm gonna cum, [the_person.fname]!"
                    "She just keep on going at steady pace."
                    the_person "Mmmmmm... Mmmm... Uh."
                    $ cum_in_mouth_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "[man_name] shrugs and starts filling her mouth with his load."
                    man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    $ play_swallow_sound()
                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                    the_person "Such a wonderful taste, [man_name]! Now I go for a glass of cola and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Mmmmmm... Brhkhmmm..."
                        man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "usual":
                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                    "[the_person.possessive_title] grabs the tip with her hand so that no sperm would spill."
                    man_name "Ow, fuck! That was great!"
                    the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                    the_person "Now I go wash my hands and then we go back to our books. I don't want to fail this test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Please, take me once more. I want to feel your hard dick in my little ass!"
                        man_name "Sure, [the_person.fname]. Get your little hole ready!"
                        "Screams go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif target_position == "bj":
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "You take a look inside the room and you see [the_person.possessive_title] on her knees. And some young man thrusts his dick into [the_person.possessive_title] mouth."
                man_name "You mouth feels great, [the_person.fname]. Keep going."
                "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
                "The man grabs [the_person.possessive_title]'s head and tries to force her to take his member all way long."
                if the_person.get_opinion_score("being submissive") > 0:
                    "[the_person.possessive_title] obediently takes it all in her mouth. You see some tears in her eyes but she does not object."
                    man_name "That's it, dear. Take it deep. I like the way you do it."
                else:
                    "[the_person.possessive_title] shakes her head, clearly showing that she does not like this. [man_name] takes his hands away."
                $ the_person.change_arousal (26)
                "You notice that with one hand [the_person.possessive_title] is rubbing between her legs."
                "After a few more moves there her body shrugs and you hear a moan of pleasure."
                man_name "Don't think I can go on for long, [the_person.fname]."
                $ finish = sister_ntr_select_finish(the_person)
                if finish == "facial":
                    the_person "Hold it, [man_name]! I have a better idea."
                    $ the_person.draw_person(position = "blowjob")
                    "She pushes him backwards. With a wet sound his dick leaves her mouth. [the_person.possessive_title] is sitting on her knees in front of [man_name] cock."
                    the_person "Remember the link I sent you, with a girl getting a cum shot? Do this to me, will you?"
                    man_name "And how can I deny that?"
                    "He strokes his dick for few moments and starts to cover [the_person.possessive_title] face with hot semen."
                    $ cum_on_face_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    the_person "Yes! That's it! Cover my face!"
                    "After [man_name] finishes, she looks him in the eyes."
                    the_person "Do I look cute this way?"
                    man_name "You look marvelous, [the_person.fname]. I really liked that."
                    the_person "I loved that too. Now I go wash my face and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Let me take care of you so that you could cum on my face!"
                        man_name "Don't mind if you do, [the_person.fname]!"
                        the_person "Here, take a photo on my phone. I wanna see it too!"
                        "Noises go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "drink":
                    "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls."
                    man_name "I'm gonna cum, [the_person.fname]!"
                    "She just keep on going at steady pace."
                    the_person "Mmmmmm... Mmmm... Uh."
                    $ cum_in_mouth_ntr(the_person)
                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                    "[man_name] shrugs and starts filling her mouth with his load."
                    man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    $ play_swallow_sound()
                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                    the_person "Such a wonderful taste, [man_name]! Now I go for a glass of cola and then we have to finish the tasks. Don't wanna get bad grade on that test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        the_person "Mmmmmm... Brhkhmmm..."
                        man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                elif finish == "usual":
                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                    "[the_person.possessive_title] grabs the tip with her hand collecting all his cum."
                    man_name "Ow, fuck! That was great!"
                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                    the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                    the_person "Now I go wash my hands and then we go back to our books. I don't want to fail this test."
                    "You go back to you room to finally have some sleep."
                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                        "While trying to sleep, you hear some loud noises from outside the bedroom."
                        man_name "Suck me again, [the_person.fname]. I really loved it."
                        the_person "Let's finish this one first and then I will reward you."
                        "Moans go on long into the night..."
                    else:
                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
    if ran_num == 2: ## a scene with two men
        $ the_person.strip_outfit_to_max_sluttiness()
        $ target_position = select_position(the_person)
        $ man_name2 = Person.get_random_male_name()
        while man_name == man_name2: ## Just to make sure that names don't match or it will look stupid
            $ man_name2 = Person.get_random_male_name()
        $ the_person.change_arousal (75)

        if target_position == "missionary":
            $ the_person.draw_person(position = "missionary", emotion = "happy")
            "You take a look inside the room and you see [the_person.possessive_title] lying on the table with wide spread legs. And some young man is between them with his pants down."
            "There is another man, sitting on the bed. Stroking his cock. It seems that he is waiting for his turn."
            the_person "Oh, [man_name]! You are so good! Keep going!"
            man_name "It seems that [the_person.fname] likes my dick more than yours, [man_name2]."
            "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
            if the_person.get_opinion_score("being submissive") > 0:
                "[man_name] grabs [the_person.possessive_title]'s legs and thrusts himself to her with some force."
                the_person "Yes, [man_name]. Fuck me harder! Be rough with your [the_person.fname]!"
                man_name2 "Yeah, man, fuck our little classmate real hard."
            "[man_name2] stands up and comes to the table. He starts playing with [the_person.possessive_title] clit while [man_name] keeps doing her."
            $ the_person.change_arousal (26)
            "After a few more moves, [the_person.possessive_title] seems to have reached an orgasm."
            $ the_person.draw_person(position = "missionary", emotion = "orgasm")
            $ the_person.have_orgasm()
            the_person "Keep fucking me, [man_name]! I'm... cumming!..."
            "Her body shrugs and you see happy smile on her face."
            the_person "You made me cum, guys! I really love being fucked by both of you."
            man_name "Don't think I can go on for long, [the_person.fname]."
            $ finish = sister_ntr_select_finish(the_person)
            if finish == "facial":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "Do you like porn with a lot of cum shots? Do this to me, will you?"
                man_name "And how can I deny that?"
                man_name2 "Yeah, such stuff really turns me on!"
                "They stroke their dicks for few moments and start to cover [the_person.possessive_title] face with hot semen."
                $ cum_on_face_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                the_person "Yes! That's it! Cover my face!"
                $ cum_on_tits_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "Their load is so huge that it starts do drip on [the_person.possessive_title] breast."
                "After both men finishes, she looks up to them."
                the_person "Do I look cute this way?"
                man_name "You look like a real porn actress, [the_person.fname]."
                man_name2 "Our little coed just got her sperm bath. What a view!"
                the_person "I loved that too. Now I go wash my face and then we have to study. I need a straight A on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Do me again, [man_name]. Fuck me harder! Please cum on my face again!"
                    man_name "On your knees, [the_person.fname]! I'm cumming again!"
                    man_name2 "Take my load too, you little cum-loving slut!"
                    the_person "Here, take a photo on my phone. I wanna see it too!"
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "inside":
                the_person "Yes! Do it, [man_name]! I want you to fill me"
                if the_person.on_birth_control:
                    the_person "Don't worry, I'm on the pill."
                $ cum_in_vagina_ntr(the_person)
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                the_person "Yes, [man_name]! I want it in me!"
                "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from her pussy."
                man_name "What a nice view! [the_person.fname] [the_person.last_name] fucked and creampied."
                "She spreads her legs even more to show her cum drenched pussy."
                the_person "Now you, [man_name2]. I want your stuff in me too!"
                "The man comes up to her and enters [the_person.possessive_title] cum filled pussy. Since he is pretty aroused, it doesn't take him long to cum."
                man_name2 "Take it all in, [the_person.fname]!"
                the_person "Yes! Fill me more!"
                "After both men shot their loads into [the_person.possessive_title], she is lying on the table and sperm is flowing out of her vagina."
                the_person "Hope you like the view. Now I go wash myself and then we have to finish the tasks. Don't wanna get bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Take me again, [man_name]. Fuck me hard! I need you to fill me once more!"
                    man_name "On your knees, [the_person.fname]! I want you from behind this time!"
                    the_person "Slap my ass harder! I like it rough!"
                    man_name2 "Take it in your mouth, [the_person.fname]! Work on it before I get my turn for your pussy."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "drink":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls and the other is stroking [man_name2]."
                man_name "I'm gonna cum, [the_person.fname]!"
                "She just keep on going at steady pace."
                the_person "Mmmmmm... Mmmm... Uh."
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "[man_name] shrugs and starts filling her mouth with his load."
                man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                $ play_swallow_sound()
                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "After finishing with [man_name], [the_person.possessive_title] starts sucking [man_name2]'s cock."
                man_name2 "Shit, your mouth is so good! I'm gonna explode right now!"
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "You see [man_name2] body shrugs as he starts to shoot his load into [the_person.possessive_title] mouth."
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "She gulps and looks up to men with a broad smile."
                the_person "Such a wonderful taste, [man_name]! Now I go for a glass of water and then we have to study. I need a straight A on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Mmmmmm... Brhkhmmm..."
                    man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                    man_name2 "Yeah, and get ready for one more."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "usual":
                "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                "[the_person.possessive_title] grabs the tip with her hand so that no sperm would spill."
                man_name "Ow, fuck! That was great!"
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                man_name2 "Help me too, [the_person.fname]."
                "She grabs his dick and strokes it for a while. Once he reaches an orgasm, [the_person.possessive_title] closes the tip with a hand so that the semen won't stain anything."
                the_person "You really fucked me good, guys! Now I go wash my hands and then we have to get back to studying. I don't want a bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Please, take me once more, guys. I want to feel your hard dicks inside again!"
                    man_name "Sure, [the_person.fname]. Get your little pussy ready!"
                    man_name2 "Suck me, [the_person.fname], while I wait."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
        elif target_position == "wall":
            $ the_person.draw_person(position = "standing_doggy")
            "You take a look inside the room and you see [the_person.possessive_title] bent over the bed. And some young man is doing her with his pants down."
            "There is another man, sitting on the bed in front of [the_person.possessive_title]. She is playing with his dick."
            the_person "Oh, [man_name]! You are so good! Keep going!"
            man_name "Wow, [man_name2], you really turned our little classmate on!"
            "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
            if the_person.get_opinion_score("being submissive") > 0:
                "[man_name] slaps [the_person.possessive_title]'s buttocks with a loud sound."
                the_person "Oh, yes, [man_name]. Be rough with your [the_person.fname]! I like being owned by a man."
                man_name2 "Like being owned, eh? How about this?"
                "He grabs her head and impales with his erected penis. [the_person.possessive_title] does not object."
            $ the_person.change_arousal (26)
            "After a few more moves, [the_person.possessive_title] seems to have reached an orgasm."
            the_person "Keep fucking me, [man_name]! I'm... gonna cum..."
            man_name2 "Yeah, man, keep doing this little slut. She is hungry for a cock!"
            "Her body shrugs and you hear a moan of pleasure."
            the_person "You made me cum, [man_name]! You guys have amazing cocks."
            man_name "Don't think I can go on for long, [the_person.fname]."
            $ finish = sister_ntr_select_finish(the_person)
            if finish == "facial":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "Do you like porn with a lot of cum shots? Do this to me, will you?"
                man_name "And how can I deny that?"
                man_name2 "Yeah, such stuff really turns me on!"
                "They stroke their dicks for few moments and start to cover [the_person.possessive_title] face with hot semen."
                $ cum_on_face_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                the_person "Yes! That's it! Cover my face!"
                $ cum_on_tits_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "Their load is so huge that it starts do drip on [the_person.possessive_title] breast."
                "After both men finishes, she looks up to them."
                the_person "Do I look cute this way?"
                man_name "You look like a real porn actress, [the_person.fname]."
                man_name2 "Our little coed just got her sperm bath. What a view!"
                the_person "I loved that too. Now I go wash my face and then we have to finish the tasks. Don't wanna get bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Do me again, [man_name]. Fuck me harder! Please cum on my face again!"
                    man_name "On your knees, [the_person.fname]! I'm cumming again!"
                    man_name2 "Take my load too, you little cum-loving slut!"
                    the_person "Here, take a photo on my phone. I wanna see it too!"
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "inside":
                the_person "Yes! Do it, [man_name]! I want you to fill me up."
                if the_person.on_birth_control:
                    the_person "Don't worry, I'm on the pill."
                $ cum_in_vagina_ntr(the_person)
                $ the_person.draw_person(position = "standing_doggy")
                "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                the_person "Yes, [man_name]! I want it in me!"
                "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from her pussy."
                man_name "What a nice view! [the_person.fname] [the_person.last_name] fucked and creampied."
                "She spreads her legs even more to show her cum drenched pussy."
                the_person "Now you, [man_name2]. I want your stuff in me too!"
                "The man comes up to her and enters [the_person.possessive_title] cum filled pussy. Since he is pretty aroused, it doesn't take him long to cum."
                man_name2 "Take it all in, [the_person.fname]!"
                the_person "Yes! Fill me more!"
                $ cum_in_vagina_ntr(the_person)
                $ the_person.draw_person(position = "standing_doggy")
                "After both men shot their loads into [the_person.possessive_title], you see sperm flowing out of her vagina and down on her legs."
                the_person "Hope you like the view. Now I go wash myself and then we have to get back to studying. I don't want a bad grade on that test.."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Take me again, [man_name]. Fuck me hard! I need you to fill me once more!"
                    man_name "On your knees, [the_person.fname]! I want you from behind this time!"
                    the_person "Slap my ass harder! I like it rough!"
                    man_name2 "Take it in your mouth, [the_person.fname]! Work on it before I get my turn for your pussy."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "drink":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls and the other is stroking [man_name2]."
                man_name "I'm gonna cum, [the_person.fname]!"
                "She just keep on going at steady pace."
                the_person "Mmmmmm... Mmmm... Uh."
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "[man_name] shrugs and starts filling her mouth with his load."
                man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                $ play_swallow_sound()
                "He pull his dick out of [the_person.possessive_title]'s mouth. She looks up, swallows and smiles."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "After finishing with [man_name], [the_person.possessive_title] starts sucking [man_name2]'s cock."
                man_name2 "Shit, your mouth is so good! I'm gonna explode right now!"
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "You see [man_name2] body convulse as he shoots his load into [the_person.possessive_title] mouth."
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "She gulps and looks up to the men with a broad smile."
                the_person "Such a wonderful taste, [man_name]! Now I go for a glass of water and then we have to study. I need a straight A on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Mmmmmm... Brhkhmmm..."
                    man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                    man_name2 "Yeah, and get ready for one more."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "usual":
                "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                "[the_person.possessive_title] encloses the tip of his cock with her hand, [mom.title] should not find any sperm stains."
                man_name "Ow, fuck! That was great!"
                the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                man_name2 "Help me too, [the_person.fname]."
                "She grabs his dick and strokes it for a while. Once he reaches an orgasm, [the_person.possessive_title] closes the tip with a hand so that the semen won't stain anything."
                the_person "You really fucked me good, guys! Now I go wash my hands and then we have to finish the tasks. Don't wanna get bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Please, take me once more, guys. I want to feel your hard dicks inside again!"
                    man_name "Sure, [the_person.fname]. Get your little pussy ready!"
                    man_name2 "Suck me, [the_person.fname], while I wait."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
        elif target_position == "anal":
            $ the_person.draw_person(position = "doggy")
            "You take a look inside the room and you see [the_person.possessive_title] squeezed between two men. One is fucking her pussy while the other is working on her ass."
            the_person "Oh, [man_name]! You are so good! I like it in my ass."
            man_name "Never imagined I would fuck our classmate, sweet [the_person.fname] [the_person.last_name] in the ass. How fo you like her pussy, [man_name2]."
            man_name2 "Fresh and tight, just as I like it!"
            "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
            if the_person.get_opinion_score("being submissive") > 0:
                "[man_name] slaps [the_person.possessive_title]'s buttocks. It's red from spanking."
                the_person "Oh, [man_name]. Slap me more! I like that!"
                man_name2 "Oh, like it rough? Then you gonna like this."
                "He speeds up in [the_person.possessive_title] pussy"
                the_person "Yes! God, I love that! Fuck me real hard, guys!"
            $ the_person.change_arousal (26)
            "After a few more moves, [the_person.possessive_title] seems to have reached an orgasm."
            the_person "Fuck my ass, [man_name]! I'm... cumming!..."
            "Her body shrugs and you hear a moan of pleasure."
            the_person "You made me cum, guys! I guess I like being fucked by two men at once!"
            man_name "Don't think I can go on for long, [the_person.fname]."
            $ finish = sister_ntr_select_finish(the_person)
            if finish == "facial":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes them backwards. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "Do you like porn with a lot of cum shots? I want you both to cum all over me?"
                man_name "How could I deny that?"
                man_name2 "Yeah, that really turns me on!"
                "They stroke their dicks for few moments and start to cover [the_person.possessive_title]'s face with hot semen."
                $ cum_on_face_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                the_person "Yes! That's it! Cover my face!"
                $ cum_on_tits_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "Their loads are so huge that it slowly drips down on [the_person.possessive_title]'s breasts."
                "After both men finish, she looks up to them."
                the_person "Do you think I look cute this way?"
                man_name "You look like a real porn actress, [the_person.fname]."
                man_name2 "Our little coed just got her sperm bath. What a view!"
                the_person "I loved that too. I'll go and clean up a little and then we need to study. I don't wanna get a bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from [the_person.possessive_title]'s bedroom."
                    the_person "Do me again, guys. Fuck my both holes! Please cum on my face again!"
                    man_name "On your knees, [the_person.fname]! I'm cumming again!"
                    man_name2 "Take my load too, you little cum-loving slut!"
                    the_person "Here, take a photo on my phone. I wanna see it too!"
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "inside":
                the_person "Yes! Do it, guys! I want you to fill me up."
                if the_person.on_birth_control:
                    the_person "Don't worry, I'm on the pill."
                $ cum_in_vagina_ntr(the_person)
                $ the_person.draw_person(position = "doggy")
                "After a few hard thrusts, both men start spilling his semen into [the_person.possessive_title] holes."
                the_person "Yes! I want it in me! Fill me with cum!"
                "After few seconds they both get off inside [the_person.possessive_title]. You see a trace of their love juice dripping from her pussy and anus."
                man_name "What a nice view! Our school slut got fucked in both holes and creampied."
                man_name2 "It felt so good to fill you up, [the_person.fname]!"
                the_person "Hope you like the view. Now I will clean up so we can get back to studying. I don't want a bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Take me again. Fuck my ass hard! I need you to fill me once more!"
                    man_name "Sit on me, [the_person.fname]! I want your pussy this time!"
                    the_person "Oh, your dick is so good! [man_name2], stick it into my ass! I want both of you in me!"
                    man_name2 "Take it in your ass, [the_person.fname]! You are just crazy sex maniac, you know that?"
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "drink":
                the_person "Hold it, [man_name]! I have a better idea."
                $ the_person.draw_person(position = "blowjob")
                "She pushes them backwards. [the_person.possessive_title] gets on her knees in front of [man_name] cock. [man_name2] also comes up to her."
                the_person "I want to taste your hot cum. I won't forgive myself if I don't taste it."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls and the other is stroking [man_name2]."
                man_name "I'm gonna cum, [the_person.fname]!"
                "She just keep on going at steady pace."
                the_person "Mmmmmm... Mmmm... ahh."
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "[man_name] shrugs and starts filling her mouth with his load."
                man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                $ play_swallow_sound()
                "He pulls his cock out of [the_person.possessive_title]'s mouth. She looks up, and swallows his load."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "After finishing with [man_name], [the_person.possessive_title] starts sucking [man_name2]'s cock."
                man_name2 "Shit, your mouth is so good! I'm gonna explode right now!"
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "You see [man_name2] body shiver as he starts to shoot his load into [the_person.possessive_title] mouth."
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "She also gulps his load down and looks up to men with a broad smile."
                the_person "Such a wonderful taste, [man_name2]! Now I'll get a glass of water and then we go back to our books. I don't want to fail this test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from [the_person.possessive_title]'s bedroom."
                    the_person "Mmmmmm... Brhkhmmm..."
                    man_name "Liked my dick all the way down your throat, [the_person.fname]? Oh, here it comes..."
                    man_name2 "Yeah, and get ready for one more."
                    "It's going to be a long night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "usual":
                "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                "[the_person.possessive_title] closes the tip with her hand so she catches all his cum."
                man_name "Ow, fuck! That was great!"
                the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                man_name2 "I'm gonna cum too, [the_person.fname]."
                "She gets off from him, grabs his dick and strokes it for a while. Once he reaches an orgasm, [the_person.possessive_title] also catches all his semen so it won't stain anything."
                the_person "You did well, boys! Now I go and wash my hands and get back to our studies. I need a straight A on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Please, guys. Cum for me once more!"
                    man_name "Sure, [the_person.fname]. Stroke my cock slowly..."
                    man_name2 "Do us both simultaneously, [the_person.fname], You're gonna love it."
                    "You don't catch a lot of sleep tonight..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
        elif target_position == "bj":
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "You take a look inside the room and you see [the_person.possessive_title] on her knees. She sits in front of two men and sucks their dicks."
            man_name "You mouth feels great, [the_person.fname]. Keep going. A blowjob from a coed is a college classic, isn't it, [man_name2]?"
            man_name2 "Absolutely, [man_name]. College is there for little girls like [the_person.fname] could learn to suck cocks."
            "You see some books lying on the table. Seems they were studying and got little bored. Judging by the sweat on their bodies and loud moans, the seem to be relaxing for some time now."
            "The man grabs [the_person.possessive_title]'s head and tries to force her to take his member all way long."
            if the_person.get_opinion_score("being submissive") > 0:
                "[the_person.possessive_title] obediently takes it all in her mouth. You see some tears in her eyes but she does not object."
                man_name "That's it, dear. Take it deep. I like the way you do it."
                man_name2 "Like being face-fucked, don't you , [the_person.fname]?"
            else:
                "[the_person.possessive_title] shakes her head, clearly showing that she does not like this. [man_name] takes his hands away."
            $ the_person.change_arousal (26)
            "You notice that with one hand [the_person.possessive_title] is rubbing between her legs."
            "After a few more moves there her body shrugs and you hear a moan of pleasure."
            man_name "Don't think I can go on for long, [the_person.fname]."
            $ finish = sister_ntr_select_finish(the_person)
            if finish == "facial":
                "She takes his cock out of her mouth."
                the_person "Hold it, [man_name]! I have a better idea."
                the_person "Do you like porn with a lot of cum shots? Do this to me, will you?"
                man_name "And how can I deny that?"
                man_name2 "Yeah, such stuff really turns me on!"
                "They stroke their dicks for few moments and start to cover [the_person.possessive_title] face with hot semen."
                $ cum_on_face_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                the_person "Yes! That's it! Cover my face!"
                $ cum_on_tits_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "Their load is so huge that it starts do drip on [the_person.possessive_title] breasts."
                "After both men finishes, she looks up to them."
                the_person "Do I look cute this way?"
                man_name "You look like a real porn actress, [the_person.fname]."
                man_name2 "Our little coed just got her sperm bath. What a view!"
                the_person "I loved that too. Now I go wash my face and then we go back to our books. I don't want to fail this test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Let me take care of you so that you could cum on my face!"
                    man_name "Don't mind if you do, [the_person.fname]!"
                    man_name2 "No objections here either."
                    the_person "Here, take a photo on my phone. I wanna see it too!"
                    "Noises go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "drink":
                the_person "Hold it, [man_name]! I have a better idea."
                "She looks into [man_name]'s eyes while sucking him off. One of her hands is playing with his balls and the other is stroking [man_name2]."
                man_name "I'm gonna cum, [the_person.fname]!"
                "She just keep on going at steady pace."
                the_person "Mmmmmm... Mmmm... Uh."
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "[man_name] shrugs and starts filling her mouth with his load."
                man_name "Take it all, [the_person.fname]. Get you protein cocktail of the day!"
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                $ play_swallow_sound()
                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "After finishing with [man_name], [the_person.possessive_title] starts sucking [man_name2]'s cock."
                man_name2 "Shit, your mouth is so good! I'm gonna explode right now!"
                $ cum_in_mouth_ntr(the_person)
                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                "You see [man_name2] body shrugs as he starts to shoot his load into [the_person.possessive_title] mouth."
                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                "She gulps and looks up to men with a broad smile."
                the_person "Such a wonderful taste, [man_name]! Now I go for a glass of water and then we have to finish the tasks. Don't wanna get bad grade on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from outside the bedroom."
                    the_person "Mmmmmm... Brhkhmmm..."
                    man_name "Liked that, [the_person.fname]? Now drink my hot stuff!"
                    man_name2 "Yeah, and get ready for one more."
                    "Screams go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            elif finish == "usual":
                "[man_name] pulls out his cock from [the_person.possessive_title]'s mouth, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                "[the_person.possessive_title] quickly grabs his cock to prevent his cum from staining anything."
                man_name "Ow, fuck! That was great!"
                the_person "Yeah, [man_name]! It was great! We really should have done this sooner!"
                man_name2 "I'm gonna cum too, [the_person.fname]."
                "She grabs his dick and strokes it for a while. Once he reaches an orgasm, [the_person.possessive_title] closes the tip with a hand so that the semen won't stain anything."
                the_person "You have such sweet and tasty cocks, guys! Now I go wash my hands and then we have to study. I need a straight A on that test."
                "You go back to you room to finally have some sleep."
                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                    "While trying to sleep, you hear some loud noises from [the_person.possessive_title]'s bedroom."
                    man_name "Suck me again, [the_person.fname]. I really loved it."
                    the_person "Let me finish this one first and then I will reward you."
                    man_name2 "You really love our dicks, don't you, [the_person.fname]?"
                    "Moans go on long into the night..."
                else:
                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
        $ del man_name2
    $ finish = None
    $ target_position = None
    $ del man_name
    $ the_person.reset_arousal()
    $ the_person.apply_planned_outfit()
    $ mc.change_location(bedroom)
    $ clear_scene()
    return
