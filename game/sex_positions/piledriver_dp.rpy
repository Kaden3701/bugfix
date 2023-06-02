init:
    python:
        piledriver_dp = Position(name = "Piledriver DP", slut_requirement = 90, slut_cap = 100, requires_hard = True, requires_large_tits = False,
            position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
            girl_arousal = 18, girl_energy = 14,
            guy_arousal = 24, guy_energy = 22,
            connections = [],
            intro = "intro_piledriver_dp",
            scenes = ["scene_piledriver_dp_1","scene_piledriver_dp_2"],
            outro ="outro_piledriver_dp",
            transition_default = "transition_default_piledriver_dp",
            strip_description = "strip_piledriver_dp", strip_ask_description = "strip_ask_piledriver_dp",
            orgasm_description = "orgasm_piledriver_dp",
            taboo_break_description = "taboo_break_piledriver_dp",
            verb = "piledrive", verbing = "piledriving",
            opinion_tags = ["missionary style sex","vaginal sex","being submissive", "anal sex"], record_class = "Vaginal Sex",
            default_animation = missionary_bob,
            associated_taboo = "vaginal_sex")
        # list_of_positions.append(piledriver_dp)

#init 1:
    #python:
        # piledriver_dp.link_positions(missionary,"transition_piledriver_dp_missionary")

label intro_piledriver_dp(the_girl, the_location, the_object):
    "You grab your strap-on from your bag, then turn to [the_girl.title]."
    mc.name "[the_girl.title], I want you to lie down for me. I'm going to fuck your pussy and your ass."
    $ piledriver_dp.redraw_scene(the_girl)

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = piledriver_dp.position_tag, visible_enough = True, prefer_half_off = True)

    "You secure the strap-on dildo to your cock. A quick lube application later, you get on top of [the_girl.possessive_title]."
    the_girl "I'm not sure the angle is gonna work for..."
    "She lets out a startled yelp as you grab her ankles and bring them up over her head."
    if the_girl.get_opinion_score("being submissive") > 0:
        the_girl "Oh god, you're gonna dominate me with that thing aren't you?"
        "She sounds more excited than scared."
        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
    elif the_girl.sluttiness > 90:
        the_girl "Oh! That'll work! My holes are for you to use [the_girl.mc_title]!"
    else:
        the_girl "Oh god! I don't know... are you sure about this?"
        mc.name "Don't worry, I'll go slow."
    "[the_girl.possessive_title] reaches down and grabs the dildo. You position yourself at the entrance to her slit and she guides the dildo to her rear entrance."
    if the_girl.arousal_perc > 60:
        "You slip into her soaked cunt easily. However, you go nice and slow, giving her body a chance to adjust to having her other hole filled at the same time."
    else:
        "You slide in nice and slow, giving her plenty of time to adjust to being filled in both holes."

    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god! I'm so full... It's so good [the_girl.mc_title]!"
        $ the_girl.discover_opinion("anal sex")
    else:
        the_girl "Holy fuck! Go slow [the_girl.mc_title]. This is really intense..."
    return

label taboo_break_piledriver_dp(the_girl, the_location, the_object): #This should only be filler, since piledriver can only be transitioned to for now
    $ piledriver_dp.redraw_scene(the_girl)
    "You take [the_girl.title]'s hands in yours and guide her down onto the [the_object.name]. She follows your lead, lying down for you."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = piledriver_dp.position_tag, visible_enough = True, prefer_half_off = True)
    "You place your hands on her knees and spread her legs, kneeling down between them."
    "You sit your hard cock on her stomach, teasingly close to her warm pussy. [the_girl.possessive_title] reaches down and gently pets your shaft."
    $ the_girl.call_dialogue(piledriver_dp.associated_taboo+"_taboo_break")
    "You grab onto [the_girl.title]'s ankles and lift them up, bringing her knees up to your shoulders."
    if the_girl.effective_sluttiness(piledriver_dp.associated_taboo) > piledriver_dp.slut_cap:
        the_girl "Ooh, I like it!"
        "With one hand she reaches down between her legs positioning your cock, while her other hand lines up the dildo for her sphincter."
        "She rubs your tip against her clit a few times before moving it down and slightly pushing the dildo inside her ass."
    else:
        the_girl "Ah! What are you doing?"
        mc.name "Trust me, this will feel great."
        "You reach down between your legs and hold onto your cock, lining it up with [the_girl.possessive_title]'s pussy."
        "At the same time you place the dildo against her sphincter, slightly opening it up."

    "You hold onto [the_girl.title]'s legs and push forward. After a moment of resistance you slide smoothly into both her holes."
    the_girl "Ohhhh...."
    "You hold yourself deep inside of her for a few seconds, then pull back and begin slowly thrust in and out."
    return

label scene_piledriver_dp_1(the_girl, the_location, the_object):
    #CHOICE CONCEPT: Talk dirty to her // Fuck her in silence
    "You hold onto [the_girl.title]'s ankles and lean into her. Her cunt feels even tighter than usual, thanks to the girth of the strap-on in her ass."
    if the_girl.sex_skills["Vaginal"] < 3 or the_girl.sex_skills["Anal"] < 3: #She struggles with the position
        the_girl "Ah! Oh fuck me, I don't know if I can handle this!"

    else:
        $ the_girl.call_dialogue("sex_responses_vaginal")
        "[the_girl.title] holds her legs out wide for you, spreading herself so you can fuck her hard and fast against the [the_object.name]."
    $ play_moan_sound()
    "[the_girl.title] moans loudly. You do your best to drive your cock all the way to its base, fitting every last inch into [the_girl.title]'s cunt."
    the_girl "So full... holy hell."
    "You hold yourself in deep. Her holes are completely stuffed. She reaches up and grabs her ankles, helping to hold them apart."
    menu:
        "Talk dirty to her":
            mc.name "You take cock like a champ. I bet you would love it if there were another cock to stuff your throat too, wouldn't you?"
            if the_girl.get_opinion_score("threesomes") >= 0:
                "She looks up at you and bites her lip."
                if the_girl.obedience > 170:  #Basically a slave
                    the_girl "If that's what you want. Get a whole room full of guys and gangbang me! I'll do anything you want me to!"
                elif the_girl.love > 80: #she loves you
                    the_girl "I just can't refuse you. If you wanted to do it with another guy, or girl, I'll do it. But just for you!"
                else:
                    the_girl "Mmm, that sounds great. I'm not sure I can take any more, but I wouldn't mind trying!"
                $ the_girl.change_arousal(5)
            else:
                "She gives a small frown."
                the_girl "I would rather we keep things personal... just between me and you."

        "Pinch her nipples" if the_girl.tits_available:
            "While she holds her own ankles, you decide to take advantage and play with her tits."
            "You grab both her nipples and pinch and twist them."
            the_girl "Gah! God you know just how to mix pleasure with pain, don't you?"
            "You respond with another pinch."
            the_girl "Oh! Fuck that hurts so good..."
            $ the_girl.change_arousal(5)

        "Kiss her neck":
            "You lean all the forward and kiss the side of her neck. Your cock is buried as deep as it will go, with the strap-on equally deep."
            if the_girl.get_opinion_score("kissing") > 0:
                $ the_girl.discover_opinion("kissing")
                $ the_girl.change_arousal(the_girl.get_opinion_score("kissing") * 2)
                the_girl "[the_girl.mc_title]... Oh [the_girl.mc_title] fuck that feels amazing..."
                "You bare your teeth and scrape them against her skin gently. She gasps and her body jumps at the sensation."
                the_girl "Fuuuuuuck that's nice..."
            else:
                "She squirms beneath you as you kiss and suckle lightly on the side of her neck."

    return

label scene_piledriver_dp_2(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You pound [the_girl.possessive_title]'s holes hard. She moans and her toes curl from the overwhelming sensations."
    "She lifts her head up from the [the_object.name] and looks you in the eyes."
    the_girl "Don't hold back... Give it to me good!"
    "She reaches down and starts to run circles with her fingertips around her clit."
    menu:
        "Pound her hard":
            "You pull yourself out almost completely, until just the tip of your cock and the strap-on are left inside her."
            "She almost has time to protest, but then you slam them both deep with one forceful thrust."
            the_girl "AH! Oh fuck me!"
            "You give her slow but forceful thrusts."
            if the_girl.tits_available:
                "[the_girl.possessive_title]'s tits jiggle enticingly with every thrust. Shock waves erupting from her crotch arc through her entire body."
            else:
                "Shock waves erupting from her crotch arc through her entire body."
            "The slapping noise echoes throughout the room. It is occasionally punctuated by a moan or a gasp from [the_girl.title]."

        "Pound her fast":
            "You decide to give her all you've got. Holding her ankles open wide, you move your hips now as fast as you can."
            "[the_girl.possessive_title] wraps her arms around you, just trying to hold on. Her fingernails start to scratch at your back."
            the_girl "I'm so full. [the_girl.mc_title]... [the_girl.mc_title]! It's so good!"
            "She clings to you as you fuck her. Her eyes start to roll up in the back of her head from the intense sensations."
    return

label outro_piledriver_dp(the_girl, the_location, the_object):
    "[the_girl.title]'s pussy is warm, tight and wet as you pump in and out of it, pulling you closer and closer to climaxing with each thrust."
    "You reach your limit and feel your orgasm approaching quickly."
    mc.name "Fuck me, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        if the_girl.wants_creampie or mc.condom:
            the_girl "Come on, dump it right inside of me!"
            if mc.condom:
                "You had no intention of stopping, but hearing her ask for it makes you cum even harder."
                "You push yourself as deep as you can manage and pump your load out into her cunt, hopefully contained by your condom."
                $ climax_controller.do_clarity_release(the_girl)
                "You take a moment to catch your breath, then you pull your cock out of [the_girl.title] and sit back down. Her ass gapes slightly where the strap-on was previously buried."
                "The condom tip is ballooned out, hanging to one side and filled with your cum."

                call post_orgasm_condom_routine(the_girl, piledriver_dp) from _call_post_orgasm_condom_routine_piledriver_dp
            else:
                "You had no intention of stopping either way, but hearing her ask for it makes you cum even harder. You gasp and push yourself as deep as you can, draining your balls into [the_girl.title]'s cunt."
                $ the_girl.cum_in_vagina()
                $ climax_controller.do_clarity_release(the_girl)
                $ piledriver_dp.redraw_scene(the_girl)
                if the_girl.wants_creampie:
                    the_girl "Yes! Fill me with your cum!"
                if the_girl.has_cum_fetish:
                    "[the_girl.possessive_title]'s body goes rigid as your cum pours into her [the_girl.pubes_description] pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                    the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
                    "[the_girl.possessive_title] revels in having her cum fetish fulfilled."

                if the_girl.knows_pregnant:
                    the_girl "Oh yes, fill me up with your hot semen!"
                elif the_girl.get_opinion_score("bareback sex") > 0:
                    the_girl "Oh god... I can feel it so deep. I mean... it could... hopefully..."
                    "[the_girl.possessive_title]'s voice starts to trail off."
                elif the_girl.sluttiness > 90:
                    the_girl "Oh god it's so deep."
                elif the_girl.on_birth_control:
                    the_girl "Oh fuck...  Good thing I'm on the pill..."
                else:
                    the_girl "Oh fuck... god I could get pregnant... what was I thinking?"
                "You take a moment to catch your breath, then sit back and pull your cock out of [the_girl.title]. Her ass gapes slightly where the strap-on was previously buried."
                "You keep her on her back for a few more seconds, enjoying the way the position keeps your semen inside of her."

        else:
            the_girl "Wait, make sure to pull out!"
            "It's a little late for that now. You gasp and push yourself as deep as you can, draining your balls into [the_girl.possessive_title]'s cunt."
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ piledriver_dp.redraw_scene(the_girl)
            if the_girl.knows_pregnant:
                the_girl "Oh fuck... that's a lot, next time spray it all over me."
            elif not the_girl.on_birth_control:
                the_girl "Oh fuck... what if I get pregnant [the_girl.mc_title]?"
            "You take a moment to catch your breath, then sit back and pull your cock out of [the_girl.title]. Her ass gapes slightly where the strap-on was previously buried."
            "You keep her on her back for a few more seconds, enjoying the way the position keeps your semen inside of her."

    if the_choice == "Cum on her face":
        if mc.condom:
            "You pull your cock out at the last minute, whipping the condom off with one hand as you aim it towards [the_girl.possessive_title]'s face."
        else:
            "You pull your cock out at the last minute, stroking it off with one hand as you point it towards [the_girl.possessive_title]'s face."
        "The strap-on hangs below your cock as you stroke it."
        $ the_girl.cum_on_face()
        $ climax_controller.do_clarity_release(the_girl)
        $ piledriver_dp.redraw_scene(the_girl)
        if the_girl.sluttiness > 80:
            "[the_girl.title] sticks out her tongue and stares into your eyes as you climax. You spray your load onto her face, splattering some over her tongue and sending some right into her mouth."
            $ play_swallow_sound()
            "She closes her mouth and swallows quickly, then bites her lip and smiles at you."
        else:
            "[the_girl.title] closes her eyes and waits for you to climax. You spray your load over her face and dribble a few drops of sperm onto her chest."
        "You sit back and let [the_girl.possessive_title]'s legs down. You enjoy the sight of her covered in your semen when she looks at you."
    return

label transition_piledriver_piledriver_dp(the_girl, the_location, the_object):
    "You slide back and let [the_girl.title] lower her legs. You reach for your backpack and pull out the strap-on."
    mc.name "[the_girl.title], I'm going to fuck your pussy and your ass now."
    "You secure the strap-on dildo to your cock. A quick lube application later, you get on top of [the_girl.possessive_title]."
    "You grab her ankles and bring them up over her head."
    if the_girl.get_opinion_score("being submissive") > 0:
        the_girl "Oh god, you're gonna dominate me with that thing aren't you?"
        "She sounds more excited than scared."
        $ the_girl.change_arousal(5)
    elif the_girl.sluttiness > 90:
        the_girl "Oh god here we go. My holes are for you to use [the_girl.mc_title]!"
    else:
        the_girl "Oh god! I don't know... are you sure about this?"
        mc.name "Don't worry, I'll go slow."
    "[the_girl.possessive_title] reaches down and grabs the dildo. You position yourself at the entrance to her slit and she guides the dildo to her rear entrance."
    if the_girl.arousal_perc > 60:
        "You slip into her soaked cunt easily. However, you go nice and slow, giving her body a chance to adjust to having her other hole filled at the same time."
    else:
        "You slide in nice and slow, giving her plenty of time to adjust to being filled in both holes."

    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god! I'm so full... It's so good [the_girl.mc_title]!"
        $ the_girl.discover_opinion("anal sex")
    else:
        the_girl "Holy fuck! Go slow [the_girl.mc_title]. This is really intense..."
    return

label transition_default_piledriver_dp(the_girl, the_location, the_object):
    $ piledriver_dp.redraw_scene(the_girl)
    "You put [the_girl.title] on her back."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = piledriver_dp.position_tag, visible_enough = True, prefer_half_off = True)
    "Then lift her legs up and bend her over at the waist. You kneel over her, lining your hard cock up with her tight pussy."
    mc.name "Ready?"
    "[the_girl.possessive_title] nods, and you slip yourself deep, deep inside of her."
    return

label strip_piledriver_dp(the_girl, the_clothing, the_location, the_object):
    the_girl "Wait, wait a second."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = piledriver_dp.position_tag)
    "You let your cock pop out of [the_girl.title]'s pussy and watch as she struggles out of her [the_clothing.name] and throws it to the side."
    the_girl "Okay, keep going!"
    "You throw her legs over your shoulders and slide yourself as deep into her cunt as you can get it. She guides the strap-on into her puckered hole simultaneously."
    return

label strip_ask_piledriver_dp(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to ah... take off my... my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you fuck her hard."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = piledriver_dp.position_tag)
            "You let your cock pop out of [the_girl.possessive_title]'s pussy and watch as she struggles out of her [the_clothing.name] and throws it to the side."
            the_girl "Okay, keep going now [the_girl.mc_title]!"
            "You throw her legs over your shoulders and slide yourself as deep into her cunt as you can get it. She guides the strap-on into her puckered hole simultaneously."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips back into you and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_piledriver_dp(the_girl, the_location, the_object):
    "[the_girl.title] takes a sharp breath in and you feel her legs try and clench together. Her toes curl as you bring her to the brink."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    $ play_moan_sound()
    "You keep fucking [the_girl.possessive_title] through her climax, enjoying her sopping wet cunt while she twitches and moans underneath you."
    "A few seconds later she relaxes and all the tension drains from her body."
    the_girl "God that is so intense. Keep going, I bet you can make me cum again!"
    return
