## Coffee Break 2 Crisis Mod by Tristimdorion
init 2 python:
    def coffee_break2_requirement():
        if mc.is_at_work: # only during morning afternoon or evening
            if mc.business.is_open_for_business:
                return __builtin__.len([x for x in mc.business.employee_list if x.effective_sluttiness() > 20]) >= 3
            if mc.business.is_open_for_internship:
                return __builtin__.len([x for x in mc.business.intern_list if x.effective_sluttiness() > 20]) >= 3
        return False

    coffee_break2_action = ActionMod("Coffee Break 2", coffee_break2_requirement, "coffee_break2_action_label",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business", is_crisis = True)

label coffee_break2_action_label():
    if mc.business.is_open_for_business:
        $ (person_one, person_two, person_three) = get_random_employees(3, slut_required = 20)
    else:
        $ (person_one, person_two, person_three) = get_random_interns(3, slut_required = 20)
    if not (isinstance(person_one, Person) and isinstance(person_two, Person) and isinstance(person_three, Person)):
        return

    $ mc.change_location(lobby)
    if mc.business.is_open_for_business:
        "As you are walking around the office, you see several employees at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    else:
        "As you are walking around the office, you see several interns at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    call coffee_break2_food_delivery_label(person_one, person_two, person_three) from _call_coffee_break2_food_delivery_label_1

    python:
        # Release variables
        del person_one
        del person_two
        del person_three
    return

label coffee_break2_food_delivery_label(person_one, person_two, person_three):
    python:
        scene_manager = Scene()
        scene_manager.add_actor(person_one, emotion="default", display_transform = character_left_flipped)
        scene_manager.add_actor(person_two, emotion="default", display_transform = character_center_flipped)
        scene_manager.add_actor(person_three, emotion="default")

        loser_index = renpy.random.randint(0, 2)
        if loser_index == 0:
            loser = person_one
            winner_one = person_two
            winner_two = person_three
        elif loser_index == 1:
            loser = person_two
            winner_one = person_one
            winner_two = person_three
        else:
            loser = person_three
            winner_one = person_one
            winner_two = person_two

    winner_one "Ok, listen up girls, whoever gets the shortest straw will pick up the food from the delivery guy in the lobby."
    $ scene_manager.update_actor(winner_two, emotion = "happy")
    "[winner_two.possessive_title] draws a long straw."
    winner_one "Right, [loser.fname], it's between you and me now, pick one."
    $ scene_manager.update_actor(winner_one, emotion = "happy")
    $ scene_manager.update_actor(loser, emotion = "sad")
    "[loser.possessive_title] draws the short straw."
    winner_two "Don't forget [loser.fname], you have to take off some clothes before you pick up the food."
    if loser.effective_sluttiness() >= 40:
        $ scene_manager.update_actor(loser, emotion = "happy")
        loser "Great, let's give this guy a show!"
        $ loser.change_slut(1, 40)

        if loser.effective_sluttiness() >= 60:
            $ scene_manager.update_actor(winner_one, position = "walking_away")
            $ scene_manager.update_actor(winner_two, position = "walking_away")
            "As [loser.possessive_title] turns around, she walks right into you."
            loser "Hey [mc.name] do you mind helping me out real quick?"
            $ scene_manager.remove_actor(winner_one)
            $ scene_manager.remove_actor(winner_two)

            menu:
                "Help her":
                    loser "Awesome! Cum on my face real quick. The delivery guy just pulled into the parking lot."
                    $ scene_manager.update_actor(loser, position = "blowjob")
                    if loser.is_bald:
                        "[loser.possessive_title] gives you a quick blowjob and you splatter your cum all over her face, she smears it around and over her bald head for added effect."
                    else:
                        "[loser.possessive_title] gives you a quick blowjob and you splatter your cum all over her face, she smears it around and into [loser.hair_description] for added effect."
                    $ loser.cum_on_face()
                    $ scene_manager.update_actor(loser, position = "stand3")
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = loser)
                    loser "Thanks, these delivery boys love it when I do this."
                "Refuse":
                    loser "Aww you're no fun, [loser.mc_title]. If he makes me pay this time it's your fault."

            "You watch as [loser.possessive_title] strips down."
            $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, temp_sluttiness_boost = 40)

            "She gives you a wink and turns around to pick up the food."
            $ scene_manager.update_actor(loser, position = "walking_away")

            if loser.effective_sluttiness() >= 90 and loser.vagina_visible:
                if persistent.show_ntr:
                    "When [loser.possessive_title] reaches the lobby she pulls the sweaty guy into an empty office."
                    loser "I left my purse at my desk. I can go get it... or maybe I could pay another way."
                    $ scene_manager.update_actor(loser, position = "standing_doggy")
                    $ mc.change_locked_clarity(30)
                    "[loser.possessive_title] turns around and presents herself, the sweaty guy quickly drops his pants and pushes his cock against her pussy."
                    loser "Oh, hard already. We must be getting so predictable."
                    "The delivery man begins thrusting as hard and fast as he can. He seems to be in a hurry to finish and get back to work."
                    loser "Ah yes, fill me up. Fuck me you sweaty pig."
                    "His face turns bright red as he pushes [loser.possessive_title]'s face into the desk."
                    loser "Oh yes. I'm cumming!"
                    $ loser.have_orgasm()
                    $ loser.change_stats(slut = 1, max_slut = 100)
                    $ mc.change_locked_clarity(20)
                    $ loser.cum_on_ass(add_to_record = False)
                    $ scene_manager.update_actor(loser)
                    "He finishes leaving her quivering against the desk. As he walks away he says: 'Enjoy your food, slut!'"
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "She gathers her clothes and takes the food back to her colleagues."
                else:
                    "When [loser.possessive_title] reaches the lobby, where the delivery guy is standing with a big grin on his face."
                    loser "I left my purse at my desk. I can go get it... or maybe I could pay another way."
                    $ scene_manager.update_actor(loser, position = "stand3")
                    $ mc.change_locked_clarity(20)
                    "[loser.possessive_title] indicates the guy to come forward, she spreads her legs a little to give him a nice view."
                    $ loser.change_stats(slut = 1, max_slut = 100)
                    $ scene_manager.update_actor(loser, position = "walking_away")
                    "After a while she tells him the food is getting cold. He nods, turns around and as he walks away he says: 'Enjoy your food, slut!'"

                if winner_one.effective_sluttiness() > 60 and winner_two.effective_sluttiness() > 60:
                    "You follow [loser.possessive_title] as she takes the delivery to the break room."
                    $ scene_manager.update_actor(loser, display_transform = character_center_flipped)
                    "She steps into the break room and sets the food on the table."
                    loser "Lunch is here!"
                    $ scene_manager.add_actor(winner_one, emotion="happy", display_transform = character_left_flipped)
                    $ scene_manager.add_actor(winner_two, emotion="happy")
                    if persistent.show_ntr:
                        "You enter the room and see [winner_one.title] and [winner_two.title] waiting. They see you enter the room and fall silent."
                        "You start to walk up behind [loser.title] and quietly start to take your dick out of your pants."
                        $ mc.change_locked_clarity(20)
                        loser "Hey, I see the food is here, why are you two acting so funny?"
                        mc.name "That was quite the show [loser.title]."
                        $ scene_manager.update_actor(loser, position = "back_peek")
                        $ mc.change_locked_clarity(20)
                        "You put your hands on her hips, her ass still slick with the delivery guy's cum."
                        if loser.has_face_cum:
                            mc.name "I only got to cum on your face, it doesn't seem right the delivery guy got more than me."
                        else:
                            mc.name "It doesn't seem right the delivery guy got something I didn't."
                    else:
                        "You enter the room and see [winner_one.title] and [winner_two.title] waiting for the food, you motion them to be quiet."
                        "You slowly walk up behind [loser.title] and quietly start to take your dick out of your pants."
                        $ mc.change_locked_clarity(20)
                        loser "Hey girls, the food is here, why are you two acting so funny?"
                        mc.name "That was quite the show [loser.title]."
                        $ scene_manager.update_actor(loser, position = "back_peek")
                        $ mc.change_locked_clarity(20)
                        "You put your hands on her hips, her pussy still wet from the excitement a few minutes earlier."
                        if loser.has_face_cum:
                            mc.name "I only got to cum on your face, but after this display I definitely need more."
                        else:
                            mc.name "After that show, I definitely deserve something too."

                    loser "Hey now, it's not like that, you know you can claim me anytime you want, we were just looking for some free... FUCK"
                    $ mc.change_locked_clarity(20)
                    "You grab her hips and ram yourself forward into [loser.possessive_title]'s sopping wet pussy."
                    if winner_one.effective_sluttiness() > 80 and winner_one.vagina_visible:
                        winner_one "Holy shit he's gonna fuck her right here!"
                        $ scene_manager.update_actor(winner_one, position = "kneeling1")
                        "While watching you, [winner_one.title] begins to touch herself and masturbate."
                        $ mc.change_locked_clarity(10)
                        $ winner_one.change_stats(happiness = 3, slut = 1, max_slut = 100)
                    else:
                        winner_one "Holy!... Wow, I was not expecting this!"
                        "[winner_one.title] watches you closely."
                    "You pound [loser.title] hard. She's so wet that you easily slide in and out of her."
                    $ mc.change_locked_clarity(20)
                    "You look down and see the soft wet lips of her labia gripping and pulling at you every time you start to slide out. It feels amazing."
                    if winner_two.effective_sluttiness() > 80 and winner_two.get_opinion_score("public sex") > 0:
                        winner_two "Fuck yeah! Give it to her good [winner_two.mc_title]!"
                        $ mc.change_locked_clarity(10)
                        "[winner_two.title] is watching intently, cheering you on as you give it to [loser.possessive_title]."
                        $ winner_two.change_stats(happiness = 3, slut = 1, max_slut = 100)
                    else:
                        winner_two "Wow, that looks like it feels good..."
                        "[winner_two.title] is watching intently."
                    loser "Oh god... I'm gonna... It's so good!"
                    $ scene_manager.update_actor(loser, position = "standing_doggy")
                    "[loser.title] bends over the lunch table and pushes herself back against you as she orgasms."
                    loser "Yes... YES!!!"
                    $ loser.have_orgasm()
                    "Her pussy clenching you drives you over the edge as well. You ram yourself deep and dump your cum inside of her."
                    $ loser.cum_in_vagina()
                    $ scene_manager.draw_scene()
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = loser)
                    if loser.has_face_cum:
                        "You pull out and look at [loser.possessive_title]. She has your old cum on her face and now also running down the inside of her legs as your seed spills out of her."
                    else:
                        "You pull out and look at [loser.possessive_title]. Your cum is running down the inside of her legs as your seed spills out of her."

                    $ loser.change_stats(obedience = 5, love = 3)
                    if winner_one.effective_sluttiness() > 90 and winner_one.vagina_visible:
                        winner_one "Oh god, so hot..."
                        "[winner_one.title] can't help herself. She is so turned on watching, she makes herself cum."
                        winner_one "Oh Fuck!"
                        $ mc.change_locked_clarity(20)
                        $ winner_one.have_orgasm()
                        $ winner_one.change_stats(obedience = 5)
                    if winner_two.effective_sluttiness() > 90 and winner_two.get_opinion_score("public sex") > 0:
                        winner_two "God... Damn... maybe next time I can set it up so I get the short straw."
                    "You pull up your pants, turn around and walk out of the room without saying a word. You can feel the three girls looking at you as you leave the room."
                else:
                    "While enjoying the view you decide to go back to work."
            else:
                $ scene_manager.update_actor(loser, position = "back_peek")
                "Seems he has seen this before since he doesn't move a muscle when she looks back in your direction."
                $ mc.change_locked_clarity(20)
                $ scene_manager.update_actor(loser, position = "walking_away")
                "While enjoying the view you decide to go back to work."
        else:
            "You watch as [loser.possessive_title] strips down."
            $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, temp_sluttiness_boost = 40)
            $ mc.change_locked_clarity(20)
            "[loser.possessive_title] turns around walking down to the lobby to pick up the food."
            $ scene_manager.update_actor(loser, position = "walking_away")
            "You decide to go back to work and let the girls sort this out."
    else:
        loser "This is not fair [winner_one.fname], you wanted me to lose."
        winner_one "No I didn't. And you know the rules!"

        $ scene_manager.update_actor(loser, emotion = "angry")
        # the loser feels betrayed by winner_one who is holding the straws
        $ town_relationships.worsen_relationship(winner_one, loser)

        loser "Fine, I'll do it but only my top and if I get it a third time in a row I swear..."
        # strip at least one item
        $ the_clothing = loser.outfit.get_upper_top_layer
        if the_clothing:
            $ scene_manager.draw_animated_removal(loser, the_clothing)
            $ the_clothing = None
        # do we strip more?
        $ scene_manager.strip_actor_outfit_to_max_sluttiness(loser, exclude_lower = True, temp_sluttiness_boost = 10)
        $ mc.change_locked_clarity(10)
        if loser.tits_visible:
            "[loser.possessive_title] sheepishly walks down the lobby trying to cover her breasts."
        else:
            "[loser.possessive_title] sheepishly walks down the lobby."
        $ scene_manager.update_actor(loser, position = "walking_away")
        "The other girls stand back and watch, giggling amongst themselves."
        $ loser.change_slut(1)
        $ scene_manager.remove_actor(loser)
        "You walk up to [winner_one.possessive_title] and [winner_two.possessive_title]."
        mc.name "Ok, girls you had your fun, now back to work."
        winner_two "Yes [winner_two.mc_title], right away."
        $ scene_manager.update_actor(winner_one, position = "walking_away")
        $ scene_manager.update_actor(winner_two, position = "walking_away")
        $ winner_one.change_happiness(2)
        $ winner_two.change_happiness(2)
        "Although not professional, you can't help but smile and enjoy the situation."

    python: # Release variables
        del winner_one
        del winner_two
        del loser
        scene_manager.clear_scene()
    return
