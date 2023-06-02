init:
    python:
        piledriver_anal = Position(name = "Anal Piledriver", slut_requirement = 80, slut_cap = 95, requires_hard = True, requires_large_tits = False,
            position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
            girl_arousal = 18, girl_energy = 12,
            guy_arousal = 24, guy_energy = 20,
            connections = [],
            intro = "intro_piledriver_anal",
            scenes = ["scene_piledriver_anal_1","scene_piledriver_anal_2"],
            outro = "outro_piledriver_anal",
            transition_default = "transition_default_piledriver_anal",
            strip_description = "strip_piledriver_anal", strip_ask_description = "strip_ask_piledriver_anal",
            orgasm_description = "orgasm_piledriver_anal",
            taboo_break_description = "taboo_break_piledriver_anal",
            verb = "ass fuck",
            opinion_tags = ["missionary style sex","anal sex","being submissive"], record_class = "Anal Sex",
            default_animation = blowjob_bob,
            associated_taboo = "anal_sex")

        list_of_positions.append(piledriver_anal)

init 1:
    python:
        piledriver.link_positions(piledriver_anal,"transition_piledriver_piledriver_anal")
        #Here is where you would put connections if they existed.



label intro_piledriver_anal(the_girl, the_location, the_object):
    mc.name "[the_girl.title], I want you to lie down for me."
    "[the_girl.possessive_title] nods, glancing briefly at the bulge in your pants. She gets onto the [the_object.name] and waits for you."
    $ the_girl.draw_person(position = piledriver_anal.position_tag)
    the_girl "How's this?"

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = piledriver_anal.position_tag, visible_enough = True, prefer_half_off = True)

    "You get your hard cock out and kneel down in front of her. She yelps in surprise when you grab her ankles and bring them up and over her waist."
    the_girl "Oh god, it's crazy when you fuck my pussy like this."
    mc.name "I'm not fucking your pussy."
    "Your run your cock along her slit a few times, getting it lubricated. She understands what you mean after a few seconds."
    if the_girl.sex_skills["Anal"] > 3 or the_girl.get_opinion_score("anal sex") > 1:
        if the_girl.effective_sluttiness() > 90:
            the_girl "Oh god, you're gonna pin me to the [the_object.name] and fuck my ass, aren't you?"
        else:
            the_girl "Oh god, you're gonna fuck my ass aren't you?"
    else: #She's inexperienced and doesn't quite know what to do.
        if the_girl.effective_sluttiness() > 90:
            the_girl "Oh fuck, you want to put it in my ass don't you?"
        else:
            "[the_girl.possessive_title] looks worried."
            the_girl "You... you want to put it in my ass don't you?"

    "When your cock is all lubed up, you pull back slightly, then line it up with her pretty little asshole."
    mc.name "Ready?"
    if the_girl.sex_skills["Anal"] > 3 or the_girl.get_opinion_score("anal sex") > 1:
        the_girl "Yes!"
    else:
        the_girl "No, but I don't know if I ever will be."
    "You hold onto her ankles and push yourself in. She gasps as the tip of your cock slips into her ass."
    "[the_girl.title] grunts and gasps as you slowly fit your whole dick inside of her. When you bottom out you hold still, giving her time to adjust to your size."
    "After a long moment it seems like she's ready and you start to move, slowly at first then picking up speed."
    return

label taboo_break_piledriver_anal(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You grab [the_girl.possessive_title]'s ass and give it a squeeze, then a hard slap."
    mc.name "[the_girl.title], I want you to lie down for me."
    "[the_girl.possessive_title] nods, glancing briefly at the bulge in your pants. She gets onto the [the_object.name] and waits for you."
    $ piledriver_anal.redraw_scene(the_girl)
    the_girl "How's this?"
    mc.name "You look amazing."
    "You lay down on top of her and kiss her neck a few times, then whisper in her ear."
    mc.name "I think it's time we stretched your ass open."
    $ the_girl.call_dialogue(piledriver_anal.associated_taboo+"_taboo_break")
    "You grab onto [the_girl.title]'s ankles and lift them up, bringing her knees up to your shoulders."
    "You rub your cock along her slit, getting yourself good and wet."
    if the_girl.effective_sluttiness(piledriver_anal.associated_taboo) > piledriver_anal.slut_cap:
        the_girl "Ooh... I can't believe I'm saying this, but I want it!"
        "She reaches down between her legs and holds onto your cock, lining it up with her ass for you."
    else:
        the_girl "Ah! What are you doing?"
        mc.name "Trust me, this will feel great."
        "You reach down between your legs and hold onto your cock, lining it up with her tight puckered hole."
    "You hold onto her ankles and push yourself in. She gasps as the tip of your cock slips into her ass."
    "[the_girl.title] grunts and gasps as you slowly fit your whole dick inside of her. When you bottom out you hold still, giving her time to adjust to your size."
    "After a long moment it seems like she's ready and you start to move, slowly at first then picking up speed."
    return

label scene_piledriver_anal_1(the_girl, the_location, the_object):

    "You hold onto [the_girl.title]'s ankles and settle into a steady rhythm, sliding your cock in and out out of her tight ass."
    $ the_girl.call_dialogue("sex_responses_anal")
    "You bring her legs together, pushing her knees to her chest and pinning her to the [the_object.name]."
    if the_girl.arousal_perc > 70:
        "[the_girl.title]'s labia are swollen with arousal. A bit of her juices is leaking out, down toward her puckered hole that you are eagerly plundering."
    else:
        "[the_girl.title]'s labia look soft and inviting, as you plunder the puckered hole just below it."
    "Soft whimpers escape her throat as you have your way with her forbidden passage."


    return

label scene_piledriver_anal_2(the_girl, the_location, the_object):
    "You take [the_girl.possessive_title]'s legs and spread them wide. Her whole body lays open and surrendered to you."
    "She reaches down with her hand and starts to play with her [the_girl.pubes_description] pussy as you fuck her buttery back door."
    if the_girl.tits_available:
        "[the_girl.title]'s tits are swaying attractively with each thrust. You give her a couple of rough thrusts and enjoy the change in their movement."
    else:
        "Suddenly, you realize that [the_girl.title] still hasn't taken her tits out. You decide to change that. You quickly move her clothes out of the way before she has a chance to protest."
        $ the_girl.strip_to_tits(position = piledriver_anal.position_tag, visible_enough = True, prefer_half_off = True)
        "With her tits now out, you resume fucking her ass and enjoy the way they shake as you pound her."
    $ the_girl.call_dialogue("sex_responses_anal")
    menu:
        "Grope her tits":
            "With her legs spread wide, you can't resist groping [the_girl.possessive_title]'s tits."
            mc.name "Hold your ankles wide open for me."
            "She bites her lip and does what she is told, freeing your hands to use as you please."
            if the_girl.has_large_tits:
                "With both hands, you take hold of [the_girl.title]'s generous tit flesh."
                $ play_moan_sound()
                "She moans as you pinch and pull her nipples as you slowly fuck her ass."
            else:
                "With both hands, you grab [the_girl.title]'s [the_girl.tits_description], holding them entirely in your hands."
                $ play_moan_sound()
                "She moans as you rub her nipples with your thumbs as you slowly fuck her ass."
        "Pin her down hard":
            "It's time to see how flexible she is. With her ankles in your hands, you push your body down as far as you can, pinning her ankles to the [the_object.name]."
            if the_girl.get_opinion_score("being submissive") > 0:
                the_girl "Oh god... I think you're going to tear me in half!"
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 2)
                "[the_girl.title] closes her eyes, but the look on her face is pleasure, not pain. Her puckered hole is quivering around your cock which is buried to the hilt."
                mc.name "Good thing you like it. You love it when I fold you over and pin you down, don't you? You love being my little butt slut, free to use any time I wish."
                the_girl "[the_girl.mc_title], I do! Use me any way you want, you can do anything!"
                "In her helpless state, all she can do is moan as you fuck her roughly, using her forbidden hole for your satisfaction."
            else:
                the_girl "Oh fuck! That hurts a little... slow down!"
                "[the_girl.title] struggles a little underneath you, but her position doesn't give her any chance of moving."
                "You pull out almost completely until just your tip is inside her sphincter. You spit a large chunk of saliva, most of it missing, but some of it lands on your cock."
                "You push in slowly again, letting it lubricate her hole and easing your passage a bit before you begin fucking her again."

    return

label outro_piledriver_anal(the_girl, the_location, the_object):

    "Fucking [the_girl.possessive_title]'s tight asshole feels amazing, and you come closer and closer to your climax."
    "You pass the point of no return and speed up, slamming your cock into her with each thrust."
    $ the_girl.call_dialogue("sex_responses_anal")
    mc.name "Fuck, here I cum!"
    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        "You push yourself balls deep into [the_girl.title]'s ass and dump your load."
        #This is where the "cum in me" section would go instead
        #the_girl "Ah! Ah!"
        $ climax_controller.do_clarity_release(the_girl)
        if mc.condom:
            "You hold yourself inside of her until your climax has passed, then pull out slowly and sit back."

            "Your condom is filled and bulging on one side. [the_girl.title] is too worn out to do anything with it."
            "You tie the end in a knot and pull it off, throwing it away while she recovers."
        else:
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title]'s body goes rigid as your cum pours into her ass. Her eyes go blank and she gets a blissful expression on her face."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! Fill this slutty ass up!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."

            "She is left on her back, holding her own ankles up by her head, trying to catch her breath, as your cum drips out of her gaping asshole."
            $ the_girl.cum_in_ass()
            $ piledriver_anal.redraw_scene(the_girl)
            if the_girl.get_opinion_score("anal creampies") > 0:
                # If she's into both...
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Oh fuck... I'm so full of cum. I don't want to move..."
            else:
                the_girl "Wow, that was intense. I hope you didn't stretch me out too badly."
            "Her puckered hole is raw and gaping. You watch as her asshole slowly starts to close, sealing your load inside of it."
            "She slowly lowers her legs until she is laying flat on the [the_object.name]."


    if the_choice == "Cum on her face":
        if mc.condom:
            "You pull your cock out at the last minute, whipping the condom off with one hand as you aim it towards [the_girl.possessive_title]'s face."
        else:
            "You pull your cock out at the last minute, stroking it off with one hand as you point it towards [the_girl.possessive_title]'s face."
        $ the_girl.cum_on_face()
        $ climax_controller.do_clarity_release(the_girl)
        $ piledriver.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.title] sticks out her tongue and stares into your eyes as you climax. You spray your load onto her face, splattering some over her tongue and sending some right into her mouth."
            $ play_moan_sound()
            "[the_girl.possessive_title] begins moaning uncontrollably as she receives the cum her addicted brain has been begging her for."
        elif the_girl.sluttiness > 80:
            "[the_girl.title] sticks out her tongue and stares into your eyes as you climax. You spray your load onto her face, splattering some over her tongue and sending some right into her mouth."
            $ play_swallow_sound()
            "She closes her mouth and swallows quickly, then bites her lip and smiles at you."
        else:
            "[the_girl.title] closes her eyes and waits for you to climax. You spray your load over her face and dribble a few drops of sperm onto her chest."
        "You sit back and let [the_girl.possessive_title]'s legs down. You enjoy the sight of her covered in your semen when she looks at you."
    return

label transition_piledriver_piledriver_anal(the_girl, the_location, the_object):
#     #transition from anal to normal doggy style.
    "You pull out of [the_girl.title]'s pussy, then move your tip a couple inches lower."
    "You put your cock against her puckered asshole and begin to push."
    if the_girl.has_taboo("anal_sex"):
        the_girl "Whoa! What do you think you're doing?"
        mc.name "I think it's time we stretched your ass open."
        $ the_girl.call_dialogue(piledriver_anal.associated_taboo+"_taboo_break")
        $ the_girl.break_taboo("anal_sex")
    "You hold onto her ankles and push yourself in. She gasps as the tip of your cock slips into her ass."
    "[the_girl.title] grunts and gasps as you slowly fit your whole dick inside of her. When you bottom out you hold still, giving her time to adjust to your size."
    "After a long moment it seems like she's ready and you start to move, slowly at first then picking up speed."
    return

label transition_default_piledriver_anal(the_girl, the_location, the_object):
    $ piledriver_anal.redraw_scene(the_girl)
    "You push [the_girl.title] onto her back onto the [the_object.name]. You grab her ankles and push them up by her head."
    the_girl "Whoa! Oh god be gentle with me..."
    mc.name "Ready?"
    the_girl "I... I think so."
    "You hold onto her hips and push forward, spreading her ass with your large cock. She gasps and closes her eyes, until finally you've buried your shaft in her."
    "After giving her a second to acclimatize you start to thrust in and out, slowly at first but picking up speed."
    return

label strip_piledriver_anal(the_girl, the_clothing, the_location, the_object):

    "[the_girl.title] gasps between thrusts."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = piledriver_anal.position_tag)
    "You stop fucking as [the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    "Once she's done, you resume reaming her puckered hole."
    return

label strip_ask_piledriver_anal(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], what do you think of me taking off my [the_clothing.name]?"
    "[the_girl.title] pants as you fuck her ass."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = piledriver_anal.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "Once she's done, you resume reaming her puckered hole."
            return True

        "Leave it on":
            mc.name "No, I want you to keep it on."
            if the_girl.sluttiness < 60:
                the_girl "Do I look sexy in it? Does it turn you on?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                "You speed up, fucking her faster in response to her question."
            else:
                the_girl "Does it look good on me, when you're fucking my ass? When you're stirring up my insides with your big cock?"
                "You speed up, fucking her faster in response to her question."
            return False

label orgasm_piledriver_anal(the_girl, the_location, the_object):
    $ play_moan_sound()
    "[the_girl.title]'s grunts and pants turn to moans of pleasure."
    $ the_girl.call_dialogue("climax_responses_anal")
    "Her ass squeezes down on your dick, so tight it's almost difficult to move."
    "She throws her head back and tenses up, her whole body quivering as she cums."
    "You fuck her ass through her climax, making her moan and pant with each thrust. After a few seconds it passes and she relaxes."
    the_girl "Oh god, keep fucking me [the_girl.mc_title]!"
    mc.name "Like you could stop me if you didn't want me to."
    return
