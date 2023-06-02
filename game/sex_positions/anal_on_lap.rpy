init python:
    anal_on_lap = Position(name = "Sit on Lap", slut_requirement = 75, slut_cap = 95, requires_hard = True, requires_large_tits = False,
        position_tag = "sitting", requires_location = "Sit", requires_clothing = "Vagina", skill_tag = "Anal",
        girl_arousal = 22, girl_energy = 20,
        guy_arousal = 16, guy_energy = 14,
        connections = [],
        intro = "intro_anal_on_lap",
        scenes = ["scene_anal_on_lap_1","scene_anal_on_lap_2"],
        outro = "outro_anal_on_lap",
        transition_default = "transition_default_anal_on_lap",
        strip_description = "strip_anal_on_lap",  strip_ask_description = "strip_ask_anal_on_lap",
        taboo_break_description = "taboo_break_anal_on_lap",
        orgasm_description = "orgasm_anal_on_lap",
        verb = "ass fuck",
        opinion_tags = ["anal sex"], record_class = "Anal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "anal_sex")

    list_of_positions.append(anal_on_lap)
    list_of_girl_positions.append(anal_on_lap)
    anal_on_lap.girl_outro = "GIC_outro_anal_on_lap"

#init 1:
    #python:
        #anal_on_lap.link_positions_two_way(doggy, "transition_anal_on_lap_doggy", "transition_doggy_anal_on_lap")

label intro_anal_on_lap(the_girl, the_location, the_object):
    "You sit down on the [the_object.name] and motion [the_person.possessive_title] over to you. You turn her around so her ass is facing you."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = "back_peek", visible_enough = True, prefer_half_off = True)

    $ the_girl.draw_person(position = "back_peek")
    "You give her ass cheeks a lengthy grope. You slide your fingers up and down her slit a few times, getting them nice and wet."
    mc.name "I want you to sit on my lap, but I'm going to put it here..."
    "You push your lubed up fingers against her asshole, slowly working them inside her."
    if the_girl.has_anal_fetish:
        the_girl "Ohhhh that's a great idea [the_girl.mc_title]!"
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Ahh, that feels really nice. You know I like it like that..."
    elif the_girl.effective_sluttiness() > 95:
        the_girl "Mmm, sounds kinky! Let's do it!"
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl "I don't know, I guess I can do that."

    "You work your fingers in and out of her ass a few times, getting it good and lubed up. You finger her pussy again, and this time use her arousal to rub on your cock, getting it ready."
    $ the_girl.draw_person(position = anal_on_lap.position_tag)
    "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
    "[the_girl.possessive_title] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god, I can't wait to ride this thing. Mmmm, I feel so full."
        $ the_girl.discover_opinion("anal sex")
    else:
        the_girl "Wow! Okay... I think I'm ready... let's do this!"
    return

label scene_anal_on_lap_1(the_girl, the_location, the_object):
    #She rides you hard
    "[the_girl.possessive_title] reaches back and holds on to your thighs, steadying herself as she starts to bounce her ass on your lap."
    if the_girl.body_is_thin:
        "[the_girl.possessive_title]'s gloriously fit ass bounces up and down on your cock."
        "It feels amazing to plunder her tight little body."
    elif the_girl.body_is_average:
        "[the_girl.possessive_title]'s delicious ass bounces up and down on your cock. Her ass quakes slightly with each bounce."
        "It feels amazing to plunder her incredible body."
    elif the_girl.body_is_thick:
        "[the_girl.possessive_title]'s thick ass bounces up and down on your cock. Her ass quakes with each bounce, mesmerizing you with the motions."
        "It feels amazing to plunder her generous body."
    elif the_girl.body_is_pregnant:
        "[the_girl.possessive_title]'s wide ass bounces up and down on your cock. Her ass quakes slightly with each bounce."
        "Pregnancy has made her body ripe with curves that are enticingly pleasuring you now."
    else:
        "[the_girl.possessive_title]'s ass bounces up and down on your cock."
        "It feels amazing to plunder her booty."
    $ the_girl.call_dialogue("sex_responses_anal")

    if the_girl.has_anal_fetish:           #Anal fetish
        the_girl "Yes! Oh fuck it's so good!"
        "[the_girl.possessive_title] is impaling her back door on your erection over and over with wild abandon."
        "Her back is arched as she revels in the sensations of fulfilling her anal fetish."
    if the_girl.get_opinion_score("taking control") > 0:
        the_girl "I bet I can make you cum..."
        "You can feel it as she begins to tighten her muscles around your cock rhythmically. You stop and just let yourself enjoy her efforts for a bit."

    "[the_girl.title] bounces on top of you until her breathing gets ragged. Eventually, she has to stop and catch her breath."
    the_girl "God [the_girl.mc_title]... making me ruin my own ass..."
    "[the_girl.title] is no longer bouncing, but slowly gyrating her hips in circles around yours. The stirring motion feels great."
    "You enjoy stirring her bowels until she catches her breath."

    return


label scene_anal_on_lap_2(the_girl, the_location, the_object):
    #Use your arms to bounce her
    mc.name "Here, let me take over for a minute."
    "You reach down and grab [the_girl.possessive_title]'s hips. You lift her up slightly, then let her down, slowly setting the pace you want."
    "Soon, you are bouncing her up and down, impaling her forbidden hole. You speed up, intent on fucking her raw."
    if the_girl.sex_skills["Anal"] > 3 : #She begs you to fuck her good.
        the_girl "Yes! Fuck me good [the_girl.mc_title]!"
        "Empowered by her encouragement, you speed up, pounding her hole with wild abandon. The sound of her ass clapping against you crescendos, filling you with primal lust."
        menu:
            "Talk dirty":
                mc.name "Take it bitch! I'm gonna destroy your tight little asshole."
                if the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.discover_opinion("being submissive")
                    $ play_moan_sound()
                    "[the_girl.title] just moans, leaning back against you. You seize the opportunity."
                    "Pulling her back against you, you reach under her legs and force them up and open, so she is spread wide."
                    "She whimpers helplessly as you fuck her backdoor without mercy."
                    $ the_girl.change_arousal(5)
                elif the_girl.effective_sluttiness() > 95:
                    the_girl "Mmm, do it! Fuck me hard and make me cum!"
                elif the_girl.effective_sluttiness() > 80:
                    the_girl "Fuck [the_girl.mc_title], it's so intense I might need you to slow down..."
                else:
                    the_girl "Oh god I can't take it!"

            "Finger her too":
                "You reach forward and wrap your arms around her. With one arm you lift her entire body up and down, with the other you reach between her legs and shove two fingers into her cunt."
                if the_girl.get_opinion_score("being fingered") > 0 or the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.discover_opinion("being fingered")
                    "You use your fingers inside of her as extra leverage to push her up and down. She gasps at the intense sensations."
                    the_girl "Fucking hell! That's so intense... oh yes [the_girl.mc_title]!"
                    $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being fingered", "anal sex"]))
                else:
                    $ play_moan_sound()
                    "[the_girl.title] moans as your fingers push inside of her."
                    if the_girl.arousal_perc > 70:
                        "Her cunt is soaked. You time your strokes with each thrust as you fuck her ass and finger her at the same time."
                        the_girl "Fucking hell... I'm so close!"
                        $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being fingered", "anal sex"]))
                    else:
                        "You stroke her cunt with two fingers as you fuck her ass. She really enjoys the attention."
                        $ the_girl.change_arousal(the_girl.get_opinion_score(["being fingered", "anal sex"]))
        "You keep up the pace for a while, but eventually your arms start to wear out."

    else:   #She begs you to slow down
        the_girl "Too much [the_girl.mc_title]! I'm sorry... I can't take it!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your cock and she sighs as you bottom out."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you knead her ass cheeks with both hands."
        "Going nice and slow, you get her more and more used to her anal intruder."
    return


label outro_anal_on_lap(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, bouncing her as hard as you can manage."
    $ the_girl.call_dialogue("sex_responses_anal")
    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her ass", "body"])
    mc.name "Ah, I'm going to cum!"

    if the_girl.get_opinion_score("anal creampies") > 0 or mc.condom:
            the_girl "Yes! Shove it in deep [the_girl.mc_title]!"
    elif mc.condom:
        the_girl "That's it [the_girl.mc_title], cum for me! Show me how much you love my ass!"
    elif the_girl.sluttiness < 80:
        the_girl "Oh my god I can't believe I'm letting you do this..."
    else:
        the_girl "That's it [the_girl.mc_title], cum for me! Show me how much you love my ass!"
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        "[the_girl.possessive_title]'s ass is just too good. You decide to cum inside it."
        "You grab her hips and force her down all the way, burying your cock deep inside her bowel as you start to spurt."
        if mc.condom:
            "Your cock erupts and begins filling the condom. She sighs when she feels the heat from it."
            "She waits until your orgasm has passed completely, then pulls off. Her asshole gapes slightly."
            $ climax_controller.do_clarity_release(the_girl)
            the_girl "Wow... that was intense..."
            return
        if the_girl.get_opinion_score("anal creampies") > 0:
            the_girl  "Yes! Fill your slut's ass with your cum! It's so hot!"
        if the_girl.has_anal_fetish:
            the_girl "Fuck... it's so good! Oh yes!"
            "[the_girl.possessive_title] squeals as you dump your load in her ass. Her anal fetish causes her to orgasm as you cum inside her."
            $ the_girl.have_orgasm()
        $ the_girl.cum_in_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ anal_on_lap.redraw_scene(the_girl)
        if the_girl.get_opinion_score("anal creampies") > 0:
            $ the_girl.discover_opinion("anal creampies")
            the_girl "Yes!... Thank you so much [the_girl.mc_title]. It's inside me... you know I love that so much..."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god it's so good. It makes me so happy to be pumped full like this."
        else:
            the_girl "Oh fuck, I can't believe I let you cum in my ass..."

        "She waits until your orgasm has passed completely, then pulls off. Her asshole gapes and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel."

    if the_choice == "Cum on her ass":
        mc.name "Pull off, I want to cum on your ass!"
        if mc.condom:
            "[the_girl.possessive_title] pulls off you at the last moment. You pull the condom off and blow your load all over her heart shaped ass cheeks."
        else:
            "[the_girl.possessive_title] pulls off you at the last moment. You start stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        if the_girl.get_opinion_score("being covered in cum") > 0:
            the_girl "Yes! Paint me with your sticky cum!"
        if the_girl.has_cum_fetish:
            the_girl "Fuck... it's so good! Oh yes!"
            "[the_girl.possessive_title] squeals as you paint her ass with your cum. Her cum fetish causes her to orgasm as you cum all over her."
            $ the_girl.have_orgasm()
        $ the_girl.cum_on_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ anal_on_lap.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            $ play_moan_sound()
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the streams of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
    return


label transition_default_anal_on_lap(the_girl, the_location, the_object):
    $ anal_on_lap.redraw_scene(the_girl)
    "You sit down on the [the_object.name]. She follows and starts to sit on your lap."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = "back_peek", visible_enough = True, prefer_half_off = True)
    "When she's ready, she grabs your cock and points it at her rear, then slowly lowers herself down on it. She lets out a gasp under her breath."
    return

label strip_anal_on_lap(the_girl, the_clothing, the_location, the_object):
    #"[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = anal_on_lap.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_anal_on_lap(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as she sits on your lap."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = anal_on_lap.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "She groans happily when you resume fucking her tight rear."
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
                the_girl "Does it make me look like the cum hungry slut that I am? Or is it your cock in my ass that makes me look that way?"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_anal_on_lap(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s having trouble staying on top of you, so you grab her hips and fuck her hard."
    if the_girl.get_opinion_score("masturbating") > 0:
        "She reaches down with one hand and pushes two fingers into her pussy."
    $ the_girl.call_dialogue("climax_responses_anal")
    "You bury your cock deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.possessive_title] sighs as she regains her senses."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl "I can't believe I just came like that... oh god you want to keep going, don't you?"
    else:
        the_girl "Let's keep going, it still feels so good!"
    "Still holding her, you give her a few thrusts, testing if she is ready to continue."
    return

label taboo_break_anal_on_lap(the_girl, the_location, the_object):
    "You sit down on the [the_object.name] and motion [the_person.possessive_title] over to you. You turn her around so her ass is facing you."
    $ the_girl.draw_person(position = "back_peek")
    "You give her ass cheeks a lengthy grope. You slide your fingers up and down her slit a few times, getting them nice and wet."
    mc.name "I want you to sit on my lap, but I'm going to put it here..."
    $ the_girl.call_dialogue(anal_on_lap.associated_taboo+"_taboo_break")
    "You push your lubed up fingers against her asshole, slowly working them inside her."

    the_girl "Ok, just be careful [the_girl.mc_title]..."

    "You work your fingers in and out of her ass a few times, getting it good and lubed up. You finger her pussy again, and this time use her arousal to rub on your cock, getting it ready."
    $ anal_on_lap.redraw_scene(the_girl)
    "She slowly sits down in your lap. You hold your cock in your hand, pointed at her puckered hole as she backs up onto it."
    "[the_girl.possessive_title] uses her weight to provide the pressure required to squeeze your cock past her sphincter. She gasps when her body finally relents and lets you in."
    the_girl "Wow! Okay... I think I'm ready... let's do this!"
    return

label GIC_outro_anal_on_lap(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal == "hate fuck" or the_goal == "waste cum":
        if mc.condom:
            $ anal_on_lap.call_default_outro(the_girl, the_location, the_object)
        "With each stroke of her hips [the_girl.possessive_title]'s impossibly tight ass brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        the_person "Thank god, I was about to hop off and just leave you hanging."
        "She stops moving her hips."
        the_person "Maybe I should do that anyway..."
        "She starts to pull up off of you."
        menu:
            "Grab her hips":
                mc.name "You'll get up when I tell you to."
                "You grab [the_girl.possessive_title]'s hips and force her back down."
                the_person "Hey, what the fuck!"
                $ the_person.change_stats(obedience = 5, love = -3)
                "You hold her in place as you cum into her tight ass. She squirms a little bit but she also gasps a bit."
                $ the_girl.cum_in_ass()
                $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
                $ anal_on_lap.redraw_scene(the_girl)
                "As soon as you let go of her she immediately pops off and stands over you. Her ass gives a little squelch as your cum leaks from it onto your lap."
                the_person "God dammit, that's now how that was supposed to go. Next time I'm putting handcuffs on you first..."
            "Beg her to finish inside":
                mc.name "No! Stop! Please! I want to cum inside you so bad!"
                "[the_person.title] smiles and stops, leaving just the tip of your cock in her puckered hole."
                the_person "Oh, is that so? Is my ass so good, you want to defile it with your awful sperm?"
                "You try to thrust your hips, but she backs off even further, leaving you too close to popping out."
                mc.name "Oh fuck, just finish me off please!"
                if the_goal == "hate fuck":
                    the_person "Oh fuck it."
                    "[the_person.possessive_title] drops her hips back down onto you, sheathing your cock in her tight asshole completely."
                    "There's a hint of devilish mischief in her eyes as she rocks her hips back and forth, coaxing your cum from your body."
                    "You finally erupt. She gasps as she feels the heat of it in her body."
                    $ the_girl.cum_in_ass()
                    $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
                    $ anal_on_lap.redraw_scene(the_girl)
                    "As soon as you finish she immediately pops off and stands over you. Her ass gives a little squelch as your cum leaks from it onto your lap."
                else:
                    the_person "I love to hear you beg, but not a chance."
                    "She pulls of you completely and starts to stroke you with her hand. You groan but are immediately firing off your sperm into the air. It lands on your stomach, making a mess."
                    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
                    "When you finish, she wipes her hand on your leg."
                    the_person "All that wasted seed... oh well! Better luck next time!"


    elif the_goal == "anal creampie":
        if mc.condom:
            the_person "Oh my god... hang on! I need to feel this!"
            "She suddenly pops off you. You look down confused, but then see her pulling desperately at the condom, ripping it off."
            "She quickly lines you up and sits back down on your cock, burying it deep in her ass."
            $ mc.condom = False
        "Instead of going up and down, she starts rocking her hips forward and back, milking your cock while keeping it buried deep."
        the_person "Do it... I want to feel it deep!"
        $ play_moan_sound()
        "Her words push you over the edge. Your cock explodes deep inside her bowel. She moans as she feels her body filling up."
        $ the_girl.change_obedience(3)
        $ the_girl.cum_in_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
        $ anal_on_lap.redraw_scene(the_girl)
        "You give a few half-hearted pumps when you're done, then tap [the_girl.possessive_title] on the ass. She slowly slides off of your dick."
    elif the_goal == "body shot":
        "[the_person.possessive_title] pulls off."
        if mc.condom:
            "She quickly reaches down and pulls off  your condom, throwing it to the side."
        "She grinds her hips against your shaft as you climax. You fire your hot load over her ass."
        the_girl "Cum for me [the_girl.mc_title], I want you to cum on me!"
        "You tense up and cum, shooting your thick load up and onto [the_girl.possessive_title]'s ass. She keeps grinding against your cock until you are completely spent."
        $ the_girl.cum_on_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ anal_on_lap.redraw_scene(the_girl)
        "After a while she sits next to you on the [the_object.name]."
    else:
        $ anal_on_lap.call_default_outro(the_girl, the_location, the_object)
