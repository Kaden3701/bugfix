init 2 python:
    DEALBREAKER_HIGH_ENERGY = 80

    def train_dealbreaker_blowjob_requirement(the_person):
        if not the_person.get_opinion_score("giving blowjobs") == -2:
            return False
        if the_person.sluttiness < 50:
            return ">50 sluttiness"
        if mc.inventory.has_serum_with_trait(oral_enhancer):
            return True
        if the_person.has_broken_taboo(["touching_penis","sucking_cock", "licking_pussy"]):
            return True
        return "Break similar taboo or have oral increasing serum in inventory"

    # def increase_dealbreaker_blowjob(person):
    #     if renpy.random.randint(0,100) < 25: # only chance to increase skill
    #         person.increase_sex_skill("Anal", 5, add_to_log = True)
    #
    #     person.change_slut(2, 90, add_to_log = True)
    #
    #     if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, 2, person):
    #         mc.log_event((person.title or person.name) + " anal fetish training is less effective, but she hasn't got a fetish yet.", "float_text_blue")
    #     return

    def dealbreaker_blowjob_factor(the_person):
        base_factor = -2    #We start with the person's base opinion level
        if mc.inventory.has_serum_with_trait(oral_enhancer):
            base_factor += 1
        if the_person.has_broken_taboo(["touching_penis","sucking_cock", "licking_pussy"]):
            base_factor += 1
        if the_person.energy >= DEALBREAKER_HIGH_ENERGY:
            base_factor += 1
        return base_factor

    def orgasm_location_formatted_menu(the_person, locations):
        formatted_opinion_list = []
        for item in locations:
            score = the_person.get_known_opinion_score(item[1])    # only colorize when opinion is known
            item_string = item[0]
            if score > 0:
                item_string = "{color=00e000}" + item[0] + "{/color}"
            elif score < 0:
                item_string = "{color=e00000}" + item[0] + "{/color}"

            formatted_opinion_list.append([item_string, item])
        return formatted_opinion_list

    dealbreaker_blowjob_trainable = Trainable("dealbreaker_blowjob_train", "train_dealbreaker_blowjob_label", "Ease Hated Opinion: Blowjob", base_cost = 400, unlocked_function = train_dealbreaker_blowjob_requirement)
    special_trainables.append(dealbreaker_blowjob_trainable)


label train_dealbreaker_blowjob_label(the_person):
    python:
        after_training_opinion_score = dealbreaker_blowjob_factor(the_person)
        has_effective_serum = mc.inventory.has_serum_with_trait(oral_enhancer)
        has_broken_similar_taboo = the_person.has_broken_taboo(["touching_penis","sucking_cock", "licking_pussy"])
        person_is_tired = the_person.energy <= DEALBREAKER_HIGH_ENERGY
        mc.reset_arousal()
        orgasm_options = [["On her face", "cum facials"],["In her mouth", "drinking cum"],["On her tits", "being covered in cum"], ["On the floor", "None"]]

    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you won't go down on me. This is a dealbreaker for me."
    mc.name "I want you to reconsider. I think if you try it again, with an open mind, you might be pleasantly surprised."
    the_person "You want me to what!?!"
    "For a second, it almost appears that her hatred of giving blowjobs has snapped her out of her trance, but your soothing words soon have her back to her trance state."
    mc.name "It's okay that you may not necessarily like it, but I think with the right partner and some patience, you could actually enjoy it some."
    the_person "Hmmm... I don't know..."
    if has_effective_serum: #First, use a serum to loosen her up if possible
        "You grab an oral enhancing serum from your pack."
        mc.name "Here, drink this really quick. It will help."
        the_person "Hmmm, okay..."
        $ the_serum = get_random_from_list(mc.inventory.get_serums_with_trait(oral_enhancer))
        if the_serum:
            $ mc.inventory.change_serum(the_serum,-1)
            $ the_person.give_serum(copy.copy(the_serum), add_to_log = True)
        else:
            "Actually, you don't have an oral enhancing serum? This is a bug, tell starbuck about this on Discord!"
        "In her trance like state, [the_person.possessive_title] drinks the serum obediently. This will help with the process."
    else:
        mc.name "Don't worry, you can go slow."
        "You wish you had a serum with you that you could give her that would help ease her into this."

    #Next up, if we have done similar acts, we bring up that they were good and she enjoyed them.
    if has_broken_similar_taboo:
        if the_person.has_broken_taboo("sucking_cock"):    # Somehow she now hates the position though.
            mc.name "You've done this before actually... remember?"
            the_person "Yes, of course."
            mc.name "I know you probably don't like the taste, but you can get used to it with a little practice."
            the_person "I guess..."
            mc.name "It felt amazing, when your lips wrapped around my cock. Don't you like making me feel good?"
            "[the_person.possessive_title] closes her eyes for a moment, remembering that moment. Her voice wavers."
            the_person "Well yeah but..."
            mc.name "Shhhh, it's okay. Remember that feeling, the empowering moment you take a man's cock and service it in a way he can't do for himself."
        elif the_person.has_broken_taboo("licking_pussy"):
            mc.name "You seem to like it when I kiss you. On your neck, your breasts, your pussy."
            the_person "Mmm, yeah. That can feel nice."
            mc.name "Wouldn't it make sense to return the favor? To make me feel as good as I make you feel when I get down between your legs and service you?"
            "[the_person.possessive_title] closes her eyes for a moment. Her voice wavers."
            the_person "I... I know I should, but it just..."
            mc.name "Shhh, it's okay. Things between a man and woman are give and take, and when you get down on your knees and service him, it shows you are willing to give and not just take."
        elif the_person.has_broken_taboo("touching_penis"):
            mc.name "You are okay with using your hand. Don't you like it when you wrap your hand around it and start to jerk me off?"
            the_person "Mmm, yeah. It feels nice in my hand..."
            mc.name "You made me feel good. Wouldn't it just be a natural progression then to get down on your knees and kiss it a little?"
            "[the_person.possessive_title] closes her eyes for a moment. Her voice wavers."
            the_person "But... but you don't want just a kiss..."
            mc.name "Shhh, and then what happens after a kiss? It would make me feel so good to just keep kissing and licking and going..."
        else:
            "We should not end up here. This is a bug, tell starbuck about this on Discord!"
        the_person "I... do love making your feel good..."
    else:
        mc.name "You are so sexy. It would make me feel amazing if you just let your inhibitions go and gave it a few kisses."
        the_person "I... I don't know. I think you want me to give it more than just kisses."
        mc.name "The real question is, what is so bad about it that you DON'T want to give it more than just kisses?"
        "You wish you had a similar experience to pull a memory from to help convince her, she still seems on the fence."
        the_person "I mean... I do like to make you feel good once in a while."
    mc.name "Why don't we just give it a try? If it is really that bad we can stop."
    "She is slow to respond."
    if person_is_tired:
        "[the_person.possessive_title] is too tired to resist from your earlier sexual activity, but she doesn't seem to have much enthusiasm either."
        the_person "Ok... I'll try it again."
        "You wonder how this would have gone if she had more energy before you tried to convince her to go down on you."
    else:
        the_person "I do want to make you feel good. I think you talked me into trying it at least."
        "[the_person.possessive_title] is energetic. She actually seems a little eager to give it a try now that you've talked her into it."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] gets down on her knees in front of you. She waits patiently as you pull your dick out."
    mc.name "Good girl. Now, just go nice and slow. Focus on how you are making me feel, and let yourself enjoy it too."
    the_person "Okay..."

    #Copy blowjob position's taboo break scene.
    "She reaches out and gently holds onto your shaft with one hand and brings the tip closer to her lips."
    "She looks up at you just before the moment of truth, locking eyes as she opens her lips and slides the tip of your cock past them."
    "You sigh happily as you feel [the_person.title]'s warm mouth envelop your cock."
    "She moves slowly at first, gently working her head up and down over your sensitive tip."

    $ mc.change_locked_clarity(20)

    #Next, run BJ dialogue. Based on how she feels about it when MC cums we can get the final progress point..
    "You rest your hand on [the_person.title]'s head as she bobs her head back and forth. She struggles to take you very deep, and focuses on licking and sucking your tip instead."
    mc.name "It's okay if you can't get the whole thing. Use your hand a little so you don't gag."
    "[the_person.possessive_title] wraps her right hand around the base of your cock and starts to slide it back and forth in time with her blowjob."

    $ mc.change_locked_clarity(20)

    "You relax for a little while while [the_person.possessive_title] services your cock, stroking your shaft and sucking gently on your tip."
    if the_person.is_bald:
        "You're pleasantly surprised when she reaches her other hand up and starts to gently play with your balls. You run your hand over her bald head and sigh contentedly."
    else:
        "You're pleasantly surprised when she reaches her other hand up and starts to gently play with your balls. You run your fingers through her hair and sigh contentedly."

    $ mc.change_locked_clarity(20)

    "[the_person.title] pulls your cock out of her mouth and leans in even closer. She runs her tongue along the bottom of your shaft, pausing at the top to kiss the tip a few times."
    the_person "Does that feel good?"
    "[the_person.possessive_title] seems to actually be getting into this. You make sure to encourage her."
    mc.name "It feels amazing."

    $ mc.change_locked_clarity(20)

    "[the_person.possessive_title] smiles and keeps working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
    if the_person.get_opinion_score("taking control") > 0:
        the_person "Mmm, this is actually really fun... being in control of your pleasure almost makes it worth it..."
        "She runs her tongue along the underside of your cock, licking the sensitive spot just below the tip. You moan in response."
        "She giggles a second, then opens her mouth wide and starts to blow you again."
    else:
        the_person "Just relax and enjoy, I'll take care of you as best I can."
        if the_person.sex_skills["Oral"] < 2:
            "[the_person.title] keeps on licking your cock. You enjoy the feeling for a while, but you're glad when she finally opens her mouth and starts to blow you again."
        else:
            "[the_person.title] keeps on licking your cock. Her tongue hits all the right places and sends shivers up your spine."
            "You're almost disappointed when she opens her mouth wide and starts to blow you again."

    $ mc.change_locked_clarity(20)
    "The sweet, pouty lips of [the_person.possessive_title] are getting you off. You are going to cum soon."
    mc.name "I'm gonna cum!"
    $ mc.change_arousal(20)
    "Suddenly, a look of panic is in her eyes. She doesn't know what to do! She looks at you for direction."
    $ orgasm_choice = renpy.display_menu(orgasm_location_formatted_menu(the_person, orgasm_options),True,"Choice")
    if orgasm_choice[0] == "On her face":
        "You take a step back, pulling your cock out of [the_person.possessive_title]'s mouth with a satisfyingly wet pop, and take aim at her face."
        "[the_person.title] closes her eyes and waits patiently for you to cum."
        $ the_person.cum_on_face()
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
        $ the_person.draw_person(position = "kneeling1")
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_person.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
    elif orgasm_choice[0] == "On her tits":
        "You pull back from [the_person.possessive_title]'s mouth, pointing yourself down at her tits."
        "Your orgasm builds to a peak and you grunt, blasting your load at [the_person.title]'s tits."
        $ the_person.cum_on_tits()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
        $ the_person.draw_person(position = "kneeling1")
    elif orgasm_choice[0] == "In her mouth":
        "You keep a hand on the back of [the_person.title]'s head to make it clear you want her to keep sucking. She keeps blowing you until you tense up and start to pump your load out into her mouth."
        "[the_person.possessive_title] stops when you shoot your first blast of hot cum across the back of her throat. She pulls back, leaving just the tip of your cock in her mouth as you fill it up with semen."
        "Once you've finished she slides off and looks up to show you a mouth full of sperm."
        $ the_person.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
        $ the_person.draw_person(position = "kneeling1")
        "Once you've had a good long look at your work [the_person.title] leans over to the side and lets your cum dribble out slowly onto the ground."
        "She straightens up and wipes her lips with the back of her hand."
    elif orgasm_choice[0] == "On the floor":
        "At the last second, you pull out of [the_person.possessive_title]'s mouth and start to stroke yourself off, pointing away from her."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_person)
        "You don't want to ruin the training you've achieved so far by grossing her out with your cum. Cum training can happen later..."
    if the_person.get_opinion_score(orgasm_choice) > 0:
        $ after_training_opinion_score += 1
        "[the_person.title] seems to have enjoyed the grand finale."
    elif the_person.get_opinion_score(orgasm_choice) < 0 and after_training_opinion_score >= 0:   #MAke sure we at least increase by 1
        "[the_person.title] seems to be put off by the way you finished. Unfortunately this will probably impact the effectiveness of the training..."
        $ after_training_opinion_score += (-1)
    else:
        "[the_person.title] seems to be indifferent to the way the blowjob ended."

    "After taking a moment to recover, [the_person.possessive_title] stands up and looks at you."
    $ the_person.update_opinion_with_score("giving blowjobs", after_training_opinion_score, add_to_log = True)
    $ the_person.draw_person()
    mc.name "So, what do you think?"
    if after_training_opinion_score == -1:
        the_person "I guess it wasn't as bad as I was thinking it would be."
        mc.name "So you would be up for it again sometime?"
        the_person "... maybe... but be careful about how you finish, okay?"
    elif after_training_opinion_score == 0:
        the_person "That was nice. I think you're right, it was nice making you cum."
        mc.name "Do you think you would be up for it again sometime?"
        the_person "Yeah, I could be up for that once in a while, or as a good warmup!"
    elif after_training_opinion_score == 1:
        the_person "You are right. I think I still prefer other things, but it got me really hot..."
    elif after_training_opinion_score >= 2:
        the_person "I... I can't believe I made you cum with my mouth! Can we do it again soon?"
        mc.name "Soon, don't worry."
    else:
        "This is an error, you shouldn't be here. Please let know Starbuck know on discord this event is bugged!"
    "You feel like you made excellent headway with [the_person.possessive_title]. She no longer hates giving blowjobs!"
    python:
        del after_training_opinion_score
        del has_effective_serum
        del has_broken_similar_taboo
        del person_is_tired
        del orgasm_choice
        del orgasm_options
    return True
