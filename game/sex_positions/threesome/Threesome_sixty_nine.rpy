#Girls 69, can get oral from girl 2 or vaginal with girl 1 who is in missionary

init 2 python:
    Threesome_sixty_nine_fuck_girl_one = Threesome_MC_position(name = "fuck_girl_1",
        action_description = "Fuck [the_person_{0}.title]",
        default_action_person = "one",
        skill_tag_p1 = "Vaginal",
        skill_tag_p2 = "Oral",
        girl_one_arousal = 22,
        girl_two_arousal = 20,
        girl_one_source = 0,
        girl_two_source = 1,
        girl_one_energy = 12,
        girl_two_energy = 10,
        guy_arousal = 20,
        guy_source = 1,
        guy_energy = 10,
        skill_tag_guy = "Vaginal",
        intro = "intro_threesome_sixty_nine_fuck_girl_one",
        scenes = ["scene_threesome_sixty_nine_fuck_girl_one_1", "scene_threesome_sixty_nine_fuck_girl_one_2"],
        outro = "outro_threesome_sixty_nine_fuck_girl_one",
        strip_description = "strip_threesome_sixty_nine_fuck_girl_one",
        strip_ask_description = "strip_ask_threesome_sixty_nine_fuck_girl_one",
        orgasm_description = "orgasm_threesome_sixty_nine_fuck_girl_one",
        swap_description = "swap_threesome_sixty_nine_fuck_girl_one",
        requirement = requirement_hard_both_vagina_available)

    Threesome_sixty_nine_oral_girl_two = Threesome_MC_position(name = "oral_girl_2",
        action_description = "Get Blowjob from [the_person_{0}.title]",
        default_action_person = "two",
        skill_tag_p1 = "Foreplay",
        skill_tag_p2 = "Oral",
        girl_one_arousal = 16,
        girl_two_arousal = 20,
        girl_one_source = 0,
        girl_two_source = 1,
        girl_one_energy = 9,
        girl_two_energy = 13,
        guy_arousal = 18,
        guy_source = 2,
        guy_energy = 10,
        skill_tag_guy = "Oral",
        intro = "intro_threesome_sixty_nine_oral_girl_two",
        scenes = ["scene_threesome_sixty_nine_oral_girl_two_1", "scene_threesome_sixty_nine_oral_girl_two_2"],
        outro = "outro_threesome_sixty_nine_oral_girl_two",
        strip_description = "strip_threesome_sixty_nine_oral_girl_two",
        strip_ask_description = "strip_ask_threesome_sixty_nine_oral_girl_two",
        orgasm_description = "orgasm_threesome_sixty_nine_oral_girl_two",
        swap_description = "swap_threesome_sixty_nine_oral_girl_two",
        requirement = requirement_hard_both_vagina_available)

    Threesome_sixty_nine_watch_girls = Threesome_MC_position(name = "watch_girls",
        description = "Watch the Girls",
        skill_tag_p1 = "Oral",
        skill_tag_p2 = "Oral",
        girl_one_arousal = 15,
        girl_two_arousal = 15,
        girl_one_source = 2,
        girl_two_source = 1,
        girl_one_energy = 10,
        girl_two_energy = 10,
        guy_arousal = 6,
        guy_source = 0,
        guy_energy = 5,
        skill_tag_guy = "Foreplay",
        intro = "intro_threesome_sixty_nine_watch_girls",
        scenes = ["scene_threesome_sixty_nine_watch_girls"],
        outro = "outro_threesome_sixty_nine_watch_girls",
        strip_description = "strip_threesome_sixty_nine_watch_girls",
        strip_ask_description = "strip_ask_threesome_sixty_nine_watch_girls",
        orgasm_description = "orgasm_threesome_sixty_nine_watch_girls",
        swap_description = "swap_threesome_sixty_nine_watch_girls",
        requirement = requirement_test)

    Threesome_sixty_nine = Threesome_Position(name = "Sixty Nine Plus One",
        slut_requirement = 60,
        position_one_tag = "missionary",
        position_two_tag = "cowgirl",
        girl_one_final_description = "On your back and eat her out",
        girl_two_final_description = "Face me and ride her face",
        requires_location = "Lay",
        requirements = requirement_test,
        verb = "fuck",
        p1_transform = character_69_bottom,
        p2_transform = character_69_on_top,
        p1_z_order = 0,
        p2_z_order = 1,
        can_swap = True)

    Threesome_sixty_nine.mc_position = [Threesome_sixty_nine_fuck_girl_one,Threesome_sixty_nine_oral_girl_two, Threesome_sixty_nine_watch_girls]
    list_of_threesomes.append(Threesome_sixty_nine)

label intro_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_1.title] smiles and agrees."
    if not the_girl_1.vagina_visible:
        "[the_girl_1.title] quickly moves some clothing out of the way..."
        $ the_girl_1.strip_to_vagina(position = Threesome_sixty_nine.position_one_tag, display_transform = Threesome_sixty_nine.p1_transform, visible_enough = True, prefer_half_off = True)

    if the_girl_1.has_breeding_fetish:
        the_girl_1 "Mmm, I can't wait to feel your raw cock sliding into me..."
    elif the_girl_1.has_cum_fetish:
        the_girl_1 "Mmm, I can't wait to taste that sweet pussy..."
    elif the_girl_1.has_anal_fetish:
        the_girl_1 "Mmm, that sounds good... maybe you could stick a finger in my ass once in a while too..."
    else:
        the_girl_1 "Sounds good! I can't wait, I bet this is going to be amazing..."
    "[the_girl_1.title] starts to lay down. [the_girl_2.title] turns to you."
    if the_girl_2.has_cum_fetish:
        the_girl_2 "This should be good, I've heard [the_girl_1.fname] has a pretty good tongue..."
    elif the_girl_2.has_breeding_fetish:
        the_girl_2 "This should be a good warmup... but don't forget, [the_girl_2.mc_title], I need you to fuck me sometime too..."
    elif the_girl_2.has_anal_fetish:
        the_girl_2 "Sounds good! [the_girl_1.fname] could you move your tongue into my little sphincter too, that would drive me wild..."
    else:
        the_girl_2 "Sounds good! Don't forget to change it up once in a while... I'd be glad to take a turn sucking you off..."

    if not the_girl_2.vagina_visible:
        "[the_girl_2.title] quickly moves some clothing out of the way..."
        $ the_girl_2.strip_to_vagina(position = Threesome_sixty_nine.position_two_tag, display_transform = Threesome_sixty_nine.p2_transform, visible_enough = True, prefer_half_off = True)

    "[the_girl_2.title] climbs on top of [the_girl_1.title] and slowly lowers her pussy down onto her face. She moans as [the_girl_1.title] starts to lick between her legs."
    "You get down on your knees and spread [the_girl_1.title]'s legs. You position your hips in line with hers and move your cock along her slit."
    if the_girl_2.arousal_perc > 60:
        "Her pussy is soaking wet. As you run your length along her hole you are soon slick with her juices."
    else:
        "Her pussy looks absolutely perfect. As you run your length along her hole she starts to squirm."
    $ the_girl_1.break_taboo("vaginal_sex")
    $ the_girl_1.break_taboo("condomless_sex")
    "You push yourself into [the_girl_1.title]'s steamy cunt and start to fuck her while [the_girl_2.title] rides on her face."
    return

label intro_threesome_sixty_nine_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    mc.name "I want you to warm me up before I fuck [the_girl_1.title]."
    if the_girl_2.has_cum_fetish:
        the_girl_2 "Oh my god, a mouth on my pussy and my lips on your cock... this is going to be incredible!"
    else:
        the_girl_2 "Mmmm, you may not even make it to her pussy!"
    "The girls start to get into position. [the_girl_2.title] sits on [the_girl_1.title]'s face and immediately opens wide and takes you in her mouth."
    "She moans as she begins to grind her pussy against the other girls face."
    return

label scene_threesome_sixty_nine_fuck_girl_one_1(the_girl_1, the_girl_2, the_location, the_object):
    "You run your hands along [the_girl_1.title]'s hips as you fuck her. You can see her hands groping [the_girl_2.title]'s ass cheeks as she pleasures her with her tongue."
    if the_girl_2.has_large_tits :
        if the_girl_2.tits_available:
            "In front of you, you can see [the_girl_2.title]'s [the_girl_2.tits_description] heaving up and down as she slowly rocks her hips back and forth across [the_girl_1.title]'s tongue."
        else:
            "In front of you, you can see [the_girl_2.title]'s huge tits heaving up and down, barely contained in her [the_girl_2.outfit.get_upper_top_layer.display_name] as she slowly rocks her hips back and forth across [the_girl_1.title]'s tongue."
            "You decide they've been contained for too long."
            $ scene_manager.strip_to_tits(the_girl_2, visible_enough = True, prefer_half_off = True)
    else:
        if the_girl_2.tits_available:
            "In front of you, you can see [the_girl_2.title]'s [the_girl_2.tits_description] swaying up and down as she slowly rocks her hips back and forth across [the_girl_1.title]'s tongue."
        else:
            "In front of you, you can see [the_girl_2.title]'s perky tits swaying up and down as she slowly rocks her hips back and forth across [the_girl_1.title]'s tongue."
            "They look great in her [the_girl_2.outfit.get_upper_top_layer.display_name], but you decide they've been contained for too long."
            $ scene_manager.strip_to_tits(the_girl_2, visible_enough = True, prefer_half_off = True)
    menu:
        "Squeeze her tits":
            "You grab [the_girl_2.title]'s tits. They feel warm and soft in your hands. You pinch and tug at her nipples."
            the_girl_2 "Mmmm, [the_girl_2.mc_title]. I love your hands on me."
            $the_girl_2.change_arousal(mc.sex_skills["Foreplay"])
        "Suck her nipples" if the_girl_2.tits_available:
            "You lean forward and run your tongue all around one of [the_girl_2.title]'s nipples."
            the_girl_2 "Oh! [the_girl_2.mc_title]! That feels good!"
            "You suck one of [the_girl_2.possessive_title]'s nipples into your mouth. You flip it up and down with your tongue a few times."
            $the_girl_2.change_arousal(mc.sex_skills["Oral"])
        "Suck her nipples\n{color=#ff0000}{size=18}Obstructed by Clothing{/size}{/color} (disabled)" if not the_girl_2.tits_available:
            pass
    "While you give attention to [the_girl_2.possessive_title]'s tits, you never stop pistoning your cock in and out of [the_girl_1.title]'s slick pussy."
    return

label scene_threesome_sixty_nine_oral_girl_two_1(the_girl_1, the_girl_2, the_location, the_object):
    "You rest one hand on [the_girl_2.title]'s head, guiding her as she sucks you off. With your other hand you continue to finger fuck [the_girl_1.title]."
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        "You can see that [the_girl_2.title] is really moving her hips back and forth roughly on [the_girl_1.title]'s face. She gets off on having a dick in her mouth!"
        $the_girl_2.change_arousal(the_girl_2.get_opinion_score("giving blowjobs") * 3)
    else:
        "You can see that [the_girl_2.title] is bobbing her head on your cock in time with her hip movement as she grinds against [the_girl_1.title]'s face"
    mc.name "Mmm, that feels great. When I blow my load, do you want it in your mouth or all over your face, [the_girl_2.fname]?"
    if the_girl_2.facial_or_swallow() == "facial":
        "[the_girl_2.possessive_title] pops off your cock for a second."
        the_girl_2 "I want you to just blow all over my face..."
        if the_girl_1.has_cum_fetish:
            "You hear a muffled voice speak up."
            the_girl_1 "Hey! [the_girl_1.mc_title], make sure I get some too!"
    else:
        "[the_girl_2.possessive_title] pops off your cock for a second."
        the_girl_2 "You should just cum in my mouth! I'll swallow it all for you..."
        if the_girl_1.has_cum_fetish:
            "You hear a muffled voice speak up."
            the_girl_1 "Hey! That's no fair! [the_girl_1.mc_title], make sure I get some too!"
    return

label scene_threesome_sixty_nine_fuck_girl_one_2(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_1.title]'s whole body is jostling forward and backward as you fuck her roughly. Her tight pussy feels silky smooth around your dick."
    "You lean forward and grab the back of [the_girl_2.title]'s head, bringing her in for a kiss. Your tongues meet together and you start to make out on top of [the_girl_1.title]."
    "You decide it's time for [the_girl_2.possessive_title] to put her mouth to better use."
    "You pull back from making out with [the_girl_2.title]."
    mc.name "I think [the_girl_1.fname] needs a little more attention..."
    "You grab [the_girl_2.possessive_title]'s head by her [the_girl_2.hair_description] and start to pull her head downwards. You pull out of [the_girl_1.title]'s pussy partially to give her room to work."
    "She starts to lap at [the_girl_1.title]'s cunt. You can feel her tongue brushing up against your cock."
    "You give [the_girl_1.title] a few slow thrusts, making sure to give [the_girl_2.title] room to work."
    the_girl_1 "Mmmm..."
    "Muffled moans come from [the_girl_1.title]. Your cock is buried deep inside her while [the_girl_2.possessive_title] licks and sucks at her clit."
    $ the_girl_1.change_arousal(the_girl_2.sex_skills["Oral"] * 2)
    return

label scene_threesome_sixty_nine_oral_girl_two_2(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_2.title]'s mouth pops off you for a second. She starts to run her tongue up and down the length of your shaft."
    "The view is incredible. [the_girl_2.possessive_title] is servicing you while she rides [the_girl_1.title]'s face."
    "You can't believe how lucky you are."
    "You push your fingers deep into [the_girl_1.title]. She moans into [the_girl_2.title]'s pussy, who in turn moans around your cock."
    "The vibrations from the moaning set off an incredible wave of pleasure in your amazing love triangle."
    "[the_girl_2.title] opens her mouth wide and takes your cock back into her mouth again, wrapping her velvet tongue and lips around your erection."
    return

label outro_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "Between [the_girl_1.title]'s steamy pussy and [the_girl_2.title]'s heaving tits in front of you, you find yourself going past the point of no return."
    mc.name "Oh fuck I'm gonna cum!"
    menu:
        "Cum inside [the_girl_1.title]":
            "You thrust yourself deep inside of [the_girl_1.title]'s cunt as you climax."
            if the_girl_1.arousal_perc > 100:
                "Your cock bursting deep inside her triggers another orgasm for [the_girl_1.title]. She is moaning non stop."
                $ the_girl_1.change_happiness(5)
                $ the_girl_1.have_orgasm()
            $ the_girl_1.cum_in_vagina()
            $ scene_manager.draw_scene()
            if the_girl_2.has_cum_fetish:
                the_girl_2 "Hey! No fair! I want some of that!"
                "As you slowly pull out of [the_girl_1.title], a trickle of your cum starts to escape her."
                "[the_girl_2.title] immediately moves her head down to [the_girl_1.title]'s pussy and starts to lick up the cum leaking out."
                "Desperate for more of your cum, she sticks her tongue deep into [the_girl_1.title]."
                $ the_girl_2.cum_in_mouth()
                $ scene_manager.draw_scene()
                if the_girl_2.arousal_perc > 100:
                    "Getting a dose of your cum triggers another orgasm in [the_girl_2.possessive_title]. Her body twitches as an orgasm goes through it."
                    $ the_girl_2.have_orgasm()
                "When she finally sits up, you can see traces of your cum on the corners of [the_girl_2.title]'s mouth."
            else:
                "As you slowly pull out of [the_girl_1.title], a trickle of your cum starts to escape her."
            "You give a sigh, deeply contented with having dumped your load inside of [the_girl_1.title]."

        "Cum on [the_girl_2.title]'s face":
            "You pull out of [the_girl_1.title] and grab the back of [the_girl_2.title]'s head, bringing it toward your cock."
            "She instinctively reaches out and starts to stroke you, pointing your cock right at her face."
            "Your orgasm erupts and you begin spraying cum across her face."
            $ the_girl_2.cum_on_face()
            $ scene_manager.draw_scene()
            if the_girl_2.has_cum_fetish:
                "You can see [the_girl_2.title]'s pupils dilate as you fulfil her cum fetish."
                "[the_girl_2.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            "Some of your cum runs down off [the_girl_2.title]'s face and onto [the_girl_1.title]'s belly."
            $ the_girl_1.cum_on_stomach()
            $ scene_manager.draw_scene()
            if the_girl_1.has_cum_fetish:
                "[the_girl_1.possessive_title]'s body quivers as your cum splashes down onto her. She runs her hands through your cum and rubs it into her belly."
            "You give a sigh. Two girls covered in your cum is an amazing sight to behold."
    return

label outro_threesome_sixty_nine_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_2.possessive_title]'s talented mouth suddenly pushes you past the point of no return. Her tongue slithers and swirls relentlessly around your cock."
    mc.name "Oh fuck I'm gonna cum!"
    menu:
        "Cum inside [the_girl_2.title]'s mouth":
            "You put your hand on the back of [the_girl_2.possessive_title]'s head."
            mc.name "That's it [the_girl_2.fname]. I want you to swallow it all!"
            "[the_girl_2.title] moans and looks you in the eyes. She pulls off until just the tip of your cock is in her mouth and she begins to stroke you off eagerly."
            "Your cock explodes in orgasm into her greedy mouth."
            if the_girl_2.has_cum_fetish:
                "Her pupils dilate as her cum addicted brain registers the presence of your cum in her mouth."
                "[the_girl_2.possessive_title] is moaning uncontrollably around your twitching cock."
            $ the_girl_2.cum_in_mouth()
            $ scene_manager.draw_scene()
            "After you finish cumming, [the_girl_2.possessive_title] slowly pulls away from your cock."
            "You give a sigh, deeply contented with having dumped your load inside of [the_girl_2.possessive_title]'s mouth."

        "Cum on [the_girl_2.title]'s face":
            "You pull out of [the_girl_2.title]'s mouth."
            "She instinctively reaches out and starts to stroke you, pointing your cock right at her face."
            "Your orgasm erupts and you begin spraying cum across her face."
            $ the_girl_2.cum_on_face()
            $ scene_manager.draw_scene()
            if the_girl_2.has_cum_fetish:
                "You can see [the_girl_2.title]'s pupils dilate as you fulfil her cum fetish."
                "[the_girl_2.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            "Some of your cum runs down off [the_girl_2.title]'s face and onto [the_girl_1.title]'s belly."
            $ the_girl_1.cum_on_stomach()
            $ scene_manager.draw_scene()
            if the_girl_1.has_cum_fetish:
                "[the_girl_1.possessive_title]'s body quivers as your cum splashes down onto her. She runs her hands through your cum and rubs it into her belly."
            "You give a sigh. Two girls covered in your cum is an amazing sight to behold."
    return

label strip_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the ask to strip Scene!"
    return

label orgasm_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        "You can feel [the_girl_1.title] trembling beneath you. [the_girl_2.title] opens her mouth and moans as [the_girl_1.title] licks her in just the right spot."
        $ the_girl_2.call_dialogue("climax_responses_oral")
        "[the_girl_1.title] is moaning loudly but it all gets muffled as [the_girl_2.title] grinds against her face roughly."
        $ the_girl_1.have_orgasm()
        $ the_girl_2.have_orgasm()
        "They both orgasm. [the_girl_1.title]'s cunt pulses around your cock as she cums, while [the_girl_2.title] moans and closes her eyes."
        "As they start to wind down, you continue fucking [the_girl_1.title]'s now considerably slicker pussy."
        return

    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        "You can feel [the_girl_1.title] trembling beneath you. She moans loudly but it's muffled by [the_girl_2.title] grinding her pussy in her face."
        $ the_girl_1.have_orgasm()
        "She orgasms, her pussy quivering around your cock. You grab her hips and give a few extra rough thrusts."
        "You don't even bother to slow down. As [the_girl_1.title] comes down from her orgasm you continue your relentless fucking."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        "[the_girl_2.title] opens her mouth and moans as [the_girl_1.title] licks her in just the right spot."
        $ the_girl_2.call_dialogue("climax_responses_oral")
        $ the_girl_2.have_orgasm()
        "[the_girl_2.title] grinds her pussy against the other girl's face as she orgasms."
    return

label orgasm_threesome_sixty_nine_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        "You can feel [the_girl_1.title] trembling as you finger her. [the_girl_2.title] moans around your cock as [the_girl_1.title] licks her in just the right spot."
        $ the_girl_2.call_dialogue("climax_responses_oral")
        "[the_girl_1.title] is moaning loudly but it all gets muffled as [the_girl_2.title] grinds against her face roughly."
        $ the_girl_1.have_orgasm()
        $ the_girl_2.have_orgasm()
        "They both orgasm. [the_girl_1.title]'s cunt quivers around your fingers as she cums, while [the_girl_2.title] moans and closes her eyes."
        "As they start to wind down, you put your hand on the back of [the_girl_2.title]'s head and remind her to keep sucking."
        return
    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        "You can feel [the_girl_1.title] trembling at your touch. She moans loudly but it's muffled by [the_girl_2.title] grinding her pussy in her face."
        $ the_girl_1.have_orgasm()
        "She orgasms, her pussy quivering around your fingers. You thrust them into her roughly."
        "As [the_girl_1.title] comes down from her orgasm you continue stimulating her with your hand."
        return
    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        "[the_girl_2.title] moans around your cock as [the_girl_1.title] licks her in just the right spot."
        $ the_girl_2.have_orgasm()
        "She grinds her pussy against the other girl's face as she orgasms."
    return

label swap_threesome_sixty_nine_fuck_girl_one(the_girl_1, the_girl_2, the_location, the_object):
    "Stepping back for a moment, you decide you want to fuck [the_girl_1.possessive_title]."
    mc.name "Mmm, here it comes [the_girl_1.fname]..."
    $ the_girl_1.break_taboo("vaginal_sex")
    $ the_girl_1.break_taboo("condomless_sex")
    "You lower yourself down until you are lined up with [the_girl_1.title]'s pussy. She moans as you slide yourself back into her, but it is muffled by [the_girl_2.title]'s hips as she rides her face."
    "You slide yourself into her slick cunt a few times, filling her eager hole with your dick."
    return

label swap_threesome_sixty_nine_oral_girl_two(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_2.is_bald:
        "Stepping back for a moment, you begin to run your hands over [the_girl_2.title]'s smooth head, then slowly pull her mouth down towards your cock."
    else:
        "Stepping back for a moment, you begin to run your hands through [the_girl_2.title]'s hair, then slowly pull her mouth down towards your cock."
    mc.name "Lick me clean, [the_girl_2.fname]."
    "[the_girl_2.title] opens her mouth and begins to greedily slurp at your cock. Her mouth feels great sliding up and down your erection."
    "You reach down holding [the_girl_2.title]'s bobbing head, while your other hand you start to play with [the_girl_1.title]'s [the_girl_1.pubes_description] pussy."
    return

label intro_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "You watch as [the_girl_1.title] and [the_girl_2.title] get into position."
    if mc.recently_orgasmed:
        "You put your hand on your softening cock and start to stroke it."
    else:
        "You can't help but stroke yourself as you watch the girls begin to eat each other out."
    "The sound of muffled moans and slick licking motions fill the air."
    return

label scene_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_1.title] and [the_girl_2.title] seem to be really enjoying themselves."
    "When one girl moans, the vibrations stimulate the other and she often lets out a moan herself."
    "You slowly stroke yourself as you watch. The smell in the air carries a distinctly feminine musk."
    return

label outro_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "You watch, completely enthralled by the girls as they pleasure each other."
    "Suddenly, you realize you stroked yourself too far and you are already past the point of no return."
    mc.name "Oh fuck I'm gonna cum!"
    "[the_girl_2.title] suddenly looks up and sees the look on your face. She smiles wide."
    the_girl_2 "Damn, couldn't handle watching? Why don't you..."
    "She doesn't have time to finish that sentence as you explode. You point your cock at her face, covering it in your cum."
    "She instinctively reaches out and starts to stroke you."
    $ the_girl_2.cum_on_face()
    $ scene_manager.draw_scene()
    if the_girl_2.has_cum_fetish:
        "You can see [the_girl_2.title]'s pupils dilate as you fulfil her cum fetish."
        "[the_girl_2.title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
        "She truly is addicted to your cum."
    "Some of your cum runs down off [the_girl_2.title]'s face and onto [the_girl_1.title]'s belly."
    $ the_girl_1.cum_on_stomach()
    $ scene_manager.draw_scene()
    if the_girl_1.has_cum_fetish:
        "[the_girl_1.possessive_title]'s body quivers as your cum splashes down onto her. She runs her hands through your cum and rubs it into her belly."
    "You give a sigh. Two girls covered in your cum is an amazing sight to behold."
    return

label strip_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label strip_ask_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "This is just a test to see if this position is working."
    "This is the Strip Scene!"
    return

label orgasm_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        $ play_moan_sound()
        "Both girls are moaning wildly into each other's crotches."
        $ the_girl_1.have_orgasm()
        "You can see [the_girl_1.possessive_title]'s legs shaking as an orgasm hits her."
        $ the_girl_2.have_orgasm()
        "[the_girl_2.title] is right behind her, her hips pushing back against [the_girl_1.title]'s face as she cums too."
        return
    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        $ the_girl_1.have_orgasm()
        "You can see [the_girl_1.possessive_title]'s legs shaking as an orgasm hits her."
        "Her moans are muffled by [the_girl_2.title]'s pussy."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        "[the_girl_2.title] stops eating out [the_girl_1.title] for a moment as she is starting to climax."
        the_girl_2 "Oh god... that's the spot. Fuck!"
        $ the_girl_2.have_orgasm()
        "She grinds her pussy against the other girl's face as she orgasms."
    return

label swap_threesome_sixty_nine_watch_girls(the_girl_1, the_girl_2, the_location, the_object):
    "You step back for a second and just watch [the_girl_1.title] and [the_girl_2.title] as they eat each other out."
    if mc.recently_orgasmed:
        "You put your hand on your softening cock and start to stroke it."
    "The sound of muffled moans and slick licking motions fill the air."
    return
