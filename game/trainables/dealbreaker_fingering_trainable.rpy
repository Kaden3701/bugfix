init 2 python:
    DEALBREAKER_HIGH_SEX_SKILL = 4
    DEALBREAKER_LOW_ENERGY = 30

    def train_dealbreaker_fingering_requirement(the_person):
        if not the_person.get_opinion_score("being fingered") == -2:
            return False
        if the_person.sluttiness < 30:
            return ">30 sluttiness"
        if mc.inventory.has_serum_with_trait(foreplay_enhancer):
            return True
        if the_person.has_broken_taboo(["touching_penis","touching_body", "touching_vagina"]):
            return True
        return "Break similar taboo or have foreplay increasing serum in inventory"

    # def increase_dealbreaker_fingering(person):
    #     if renpy.random.randint(0,100) < 25: # only chance to increase skill
    #         person.increase_sex_skill("Anal", 5, add_to_log = True)
    #
    #     person.change_slut(2, 90, add_to_log = True)
    #
    #     if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, 2, person):
    #         mc.log_event((person.title or person.name) + " anal fetish training is less effective, but she hasn't got a fetish yet.", "float_text_blue")
    #     return

    def dealbreaker_fingering_factor(the_person):
        base_factor = -2    #We start with the person's base opinion level
        if mc.inventory.has_serum_with_trait(foreplay_enhancer):
            base_factor += 1
        if the_person.has_broken_taboo(["touching_penis","touching_body", "touching_vagina"]):
            base_factor += 1
        if mc.sex_skills["Foreplay"] > DEALBREAKER_HIGH_SEX_SKILL:
            base_factor += 1
        if the_person.energy <= DEALBREAKER_LOW_ENERGY:
            base_factor += 1
        return base_factor

    dealbreaker_fingering_trainable = Trainable("dealbreaker_fingering_train", "train_dealbreaker_fingering_label", "Ease Hated Opinion: Fingering", base_cost = 200, unlocked_function = train_dealbreaker_fingering_requirement)
    special_trainables.append(dealbreaker_fingering_trainable)


label train_dealbreaker_fingering_label(the_person):
    python:
        after_training_opinion_score = dealbreaker_fingering_factor(the_person)
        has_effective_serum = mc.inventory.has_serum_with_trait(foreplay_enhancer)
        has_broken_similar_taboo = the_person.has_broken_taboo(["touching_penis","touching_body", "touching_vagina"])
        person_is_tired = the_person.energy <= DEALBREAKER_LOW_ENERGY
        mc_has_high_skill = mc.sex_skills["Foreplay"] > DEALBREAKER_HIGH_SEX_SKILL

    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you won't let me touch you intimately with my hands. This is a dealbreaker for me."
    mc.name "I want you to reconsider. I think if you try it again, with an open mind, you might be pleasantly surprised."
    the_person "You want to what!?!"
    "For a second, it almost appears that her hatred of being fingered has snapped her out of her trance, but your soothing words soon have her back to her trance state."
    mc.name "It's okay that you may not necessarily like it, but I think with the right partner and some patience, you could actually enjoy it some."
    the_person "Hmmm... I don't know..."
    if has_effective_serum: #First, use a serum to loosen her up if possible
        "You grab a foreplay enhancing serum from your pack."
        mc.name "Here, drink this really quick. It will help."
        the_person "Hmmm, okay..."
        $ the_serum = get_random_from_list(mc.inventory.get_serums_with_trait(foreplay_enhancer))
        if the_serum:
            $ mc.inventory.change_serum(the_serum,-1)
            $ the_person.give_serum(copy.copy(the_serum), add_to_log = True)
        else:
            "Actually, you don't have a foreplay enhancing serum? This is a bug, tell starbuck about this on Discord!"
        "In her trance like state, [the_person.possessive_title] drinks the serum obediently. This will help with the process."
    else:
        mc.name "Don't worry, we can go slow."
        "You wish you had a serum with you that you could give her that would help ease her into this."
    #Next up, if we have done similar acts, we bring up that they were good and she enjoyed them.
    if has_broken_similar_taboo:
        if the_person.has_broken_taboo("touching_vagina"):    #We've touched her before? Somehow she now hates the position though.
            mc.name "We've done this before actually... remember?"
            the_person "Yes, of course."
            mc.name "Didn't it feel good? When my fingers first pushed up inside you..."
            "[the_person.possessive_title] closes her eyes for a moment, remembering that moment. Her voice wavers."
            the_person "I... I guess it felt good... but I just..."
            mc.name "Shhhh, it's okay. Remember that feeling, the sweet sensation of being touched intimately. Was it so bad?"
        elif the_person.has_broken_taboo("touching_body"):
            mc.name "You seem to like it when I touch you in other places. Your neck. Your legs. Your breasts."
            the_person "Mmm, yeah. That can feel nice."
            mc.name "Wouldn't it make sense that it would also feel good if I touched you somewhere more intimate?"
            "[the_person.possessive_title] closes her eyes for a moment. Her voice wavers."
            the_person "I... I guess it would feel good, but I just..."
            mc.name "Shhh, it's okay. It's a natural progression of being touched in more and more intimate areas. Would that be so bad?"
        elif the_person.has_broken_taboo("touching_penis"):
            mc.name "You are okay with touching me, aren't you?"
            mc.name "Remember how good you made me feel, when you wrapped your hand around my cock and stroked it."
            the_person "Mmm, yeah. It feels nice in my hand..."
            mc.name "You made me feel so good. Would it be so bad if I touched you the same way?"
            "[the_person.possessive_title] closes her eyes for a moment. Her voice wavers."
            the_person "I... I know it would feel good, but I just..."
            mc.name "Shhh, I just want to do for you, what you've already done for me. Would that be so bad?"
        else:
            "We should not end up here. This is a bug, tell starbuck about this on Discord!"
        the_person "I... I guess we could try it..."
    else:
        mc.name "You are so sexy. I just want to make you feel good, and using my fingers I could make you feel so good."
        the_person "I... I don't know. It is kind of hard to imagine..."
        "You wish you had a similar experience to pull a memory from to help convince her."
    mc.name "Alright. Let's give it a try. I want you to turn around and close your eyes."
    if person_is_tired:
        "[the_person.possessive_title] is too tired to resist from your earlier sexual activity."
        "She obediently turns around and awaits your touch."
    else:
        the_person "I don't know... I'm not sure I want to do this right now."
        "[the_person.possessive_title] is energetic, more capable of withstanding your training. You wish she was a bit more worn out."
        mc.name "Don't worry, no one is going to see. It's just you and me, and I just want what is best for you, I promise."
        "[the_person.title] thinks about it a few more seconds. She seems just about ready to refuse, but eventually turns away and complies with your instructions."
    $ the_person.draw_person(position = "walking_away")
    mc.name "Good girl. Now I want you to just stand with your hands at your sides. I'm going to make you feel good, okay?"
    the_person "... Okay..."

    #Copy fingering position's taboo break scene.
    "You kiss [the_person.title]'s neck from behind, distracting her from your hand sliding along her inner thigh and towards her crotch."
    if the_person.vagina_available:
        "She starts as you brush her sensitive pussy. She grabs your wrist and stops you from moving any further."
    else:
        $ the_item = the_person.outfit.get_lower_top_layer
        if the_item:
            "She starts as you slide your hand under her [the_item.display_name]. She grabs your wrist and stops you from moving any further."
            $ the_item = None
        else:
            "She starts as you brush her sensitive pussy. She grabs your wrist and stops you from moving any further."
    mc.name "Shh, it's okay. It's going to feel good, I promise."
    "She lets go of your hand, and you slide it down to your prize. She moans softly as you touch her, and shivers when you first touch her clit."
    "After teasing her for a moment you press two fingers between her slit, sliding them into the wet passage beyond her pussy lips."

    #Next, if MC has a high sex skill, he wows her with a performance.
    if mc_has_high_skill:
        "You start slow, caressing her and slowly building up her arousal."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(10)
        "As her passage gets wetter, you reach up with your other hand and caress her chest, linking the good feelings from your fingers with her breasts being touched."
        $ play_moan_sound()
        "She gives a little moan, but you can tell she is still trying to hold back."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(10)
        "You move your fingers a little more urgently now, pushing a little deeper and with more pressure."
        $ play_moan_sound()
        the_person "Oooohhh..."
        "A long drawn out moan tells you she is starting to let go and enjoy it finally."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(15)
        "You slide your fingers in and out of her pussy, stroking the inside of that soft tunnel."
        "Each movement draws moans of pleasure from [the_person.possessive_title], who presses herself against you."
        if the_person.vagina_available:
            "Her pussy is dripping wet now, dripping juices down her thighs."
        else:
            $ the_item = the_person.outfit.get_lower_top_layer
            if the_item:
                "Her pussy is dripping wet now, her juices leaving a faint wet spot on her [the_item.display_name]."
                $ the_item = None
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(15)
        the_person "Oh my god... I'm... I'm!!!"
        "Her knees start to buckle for a moment. You stop groping her breast with your free hand and catch her."
        $ the_person.change_arousal(30)
        $ mc.change_locked_clarity(25)
        "Her whole body tenses up and she leans back into you. A shiver runs through her body as she climaxes."
        $ the_person.call_dialogue("climax_responses_foreplay")
        "She quivers with pleasure for a few seconds before her whole body relaxes."
        $ the_person.have_orgasm()
        "You hold her a bit longer before letting go. You feel confident that getting her off has made an impression on her opinion."
    else:   #If MC is low sex skill, run a couple rounds as if he was fingering, and if girl cums, give credit. (needs prior arousal)
        "You start slow, pushing your fingers into her and moving them in and out carefully."
        $ the_person.change_arousal(10 + mc.sex_skills["Foreplay"])
        $ mc.change_locked_clarity(10)
        if the_person.has_large_tits:
            if the_person.tits_available:
                "You reach your free hand up to [the_person.title]'s bare [the_person.tits_description] and cup one, massaging it while you finger her."
            else:
                "You reach your free hand up to [the_person.title]'s large breasts and squeeze one through her clothing, enjoying its size and weight."
        else:
            if the_person.tits_available:
                "You paw at [the_person.possessive_title]'s [the_person.tits_description] with your free hand, running your thumb over one of her nipples as you continue to finger her."
                "Her body responds, the nipple hardening as you play with it."
            else:
                "You paw at [the_person.possessive_title]'s small tits through her clothing with your free hand."
                "You can feel her body respond, her nipple hardening enough that you can feel it through the fabric."
        $ the_person.change_arousal(10 + mc.sex_skills["Foreplay"])
        $ mc.change_locked_clarity(10)
        "You can feel [the_person.possessive_title]'s pussy get a little wetter from your touch. She shivers as you continue to finger her."
        $ play_moan_sound()
        the_person "Mmmmmmmm..."
        "[the_person.title] lets out a soft moan, encouraging you to keep going. Her body is melting into yours."
        $ the_person.change_arousal(10 + mc.sex_skills["Foreplay"])
        $ mc.change_locked_clarity(10)
        if the_person.arousal_perc >= 90:
            the_person "Oh my god... I'm... I'm!!!"
            "Her knees start to buckle for a moment. You stop groping her breast with your free hand and catch her."
            $ the_person.change_arousal(30)
            $ mc.change_locked_clarity(25)
            "Her whole body tenses up and she leans back into you. A shiver runs through her body as she climaxes."
            $ the_person.call_dialogue("climax_responses_foreplay")
            $ the_person.have_orgasm()
            "She quivers with pleasure for a few seconds before her whole body relaxes."
            "You hold her a bit longer before letting go. You feel confident that getting her off has made an impression on her opinion."
            $ after_training_opinion_score += 1 #Credit for getting her to orgasm anyway despite low skill. Requires prior arousal.
            $ mc_has_high_skill = True
        else:
            "You continue to finger her for a bit, but you can tell her arousal has plateaued."
            mc.name "Feels good, doesn't it?"
            "She gives a little shudder."
            the_person "Yeah... it does..."
            "Unfortunately, you aren't skilled enough to get her to cum, but she does at least enjoy the sensations."

    "You slowly let go of [the_person.title]. She turns around to face you."
    $ the_person.update_opinion_with_score("being fingered", after_training_opinion_score, add_to_log = True)
    $ the_person.draw_person()
    mc.name "So, what do you think?"
    if after_training_opinion_score == -1:
        the_person "I guess it wasn't as bad as I was thinking it would be."
        mc.name "So you would be up for it again sometime?"
        the_person "... as a warm up maybe?"
    elif after_training_opinion_score == 0:
        the_person "That was nice. I think you're right."
        mc.name "So you would be up for it again sometime?"
        the_person "Yeah, I could be up for that once in a while, or as a good warmup!"
    elif after_training_opinion_score == 1:
        the_person "You are right. I think I still prefer other things, but it felt really good..."
    elif after_training_opinion_score >= 2:
        the_person "I... I can't believe you made me cum! Yeah, I umm... when can we do it again?"
        mc.name "Soon, don't worry."
    else:
        "This is an error, you shouldn't be here. Please let Starbuck know on discord this event is bugged!"
    "You feel like you made excellent headway with [the_person.possessive_title]."
    python:
        del after_training_opinion_score
        del has_effective_serum
        del has_broken_similar_taboo
        del person_is_tired
        del mc_has_high_skill
    return True
