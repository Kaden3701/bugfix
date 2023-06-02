init 5 python:
    deepthroat.double_orgasm = "deepthroat_double_orgasm"

label deepthroat_double_orgasm(the_girl, the_location, the_object):
    $ deepthroat.current_modifier = "blowjob"
    $ deepthroat.redraw_scene(the_girl)
    "[the_girl.title] pulls back on your cock, almost letting it fall out of her mouth. She closes her eyes and quivers slightly."
    "But the warm, tight feeling of [the_girl.title]'s throat sliding back from your shaft pulls you closer to orgasm. You feel yourself pass the point of no return and let out a soft moan."

    $ climax_controller = ClimaxController(["Cum on her face", "face"],["Cum in her mouth", "mouth"],["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ deepthroat.current_modifier = None
        $ the_girl.draw_person("kneeling1")
        "You take a step back, pulling your cock out of [the_girl.possessive_title]'s throat with a satisfyingly wet pop, and take aim at her face."
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.sluttiness > 80:
            "[the_girl.title] sticks out her tongue and rubs her [the_girl.pubes_description] pussy while waiting for your hot load."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.title]'s face and into her open mouth, all the while rubbing her wet clit."
        elif the_girl.sluttiness > 60:
            "[the_girl.title] closes her eyes riding out her orgasm."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as keep pumping out cum over [the_girl.title]'s face."
        else:
            "[the_girl.title] closes her eyes, presenting her cheek while she enjoys her orgasm."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.title]'s face. She is a little distracted as the warm liquid lands on her cheek, but keeps enjoying her own bliss."
        $ the_girl.have_orgasm()
        "You hear her whimper and a final shiver runs through her body."
        "You take a deep breath to steady yourself once you've finished cumming."
        "[the_girl.possessive_title] looks up at you from her knees, face covered in your semen, still recovering from her own orgasm."
        $ the_girl.call_dialogue("cum_face")

    elif the_choice == "Cum in her mouth":
        mc.name "Fuck, I'm about to cum! I'm going to fill that cute mouth of yours up!"
        "You keep your hand on the back of [the_girl.title]'s head to make it clear you want her to keep sucking. She keeps throating you, increasing the sensation with the moaning of her approaching orgasm."
        $ the_girl.have_orgasm()
        if the_girl.sluttiness > 70:
            "[the_girl.title] doesn't even flinch as you shoot your hot cum across the back of her throat."
            "She keeps bobbing her head up and down while moaning and rubbing her labia, savoring a mouth full of sperm."
        else:
            "[the_girl.title] temporarily stops when you shoot your first blast of hot cum across the back of her throat."
            "She pulls back a little, leaving just the tip of your cock in her mouth, squeezing her thighs, while savoring a mouth full of sperm."

        $ the_girl.cum_in_mouth()
        $ deepthroat.current_modifier = None
        $ deepthroat.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.sluttiness > 80:
            $ play_swallow_sound()
            "When [the_girl.title]'s orgasm subsides, she closes her mouth and swallows loudly, smiling at you."
        else:
            if the_girl.tits_visible:
                $ the_girl.cum_on_tits()
                $ deepthroat.redraw_scene(the_girl)
                if the_girl.has_large_tits:
                    "After her orgasm subsides, she lets the cum dribble down her chin on to her nice [the_girl.tits_description], giving you a wink."
                else:
                    "After her orgasm subsides, she lets the cum dribble down her chin on to her [the_girl.tits_description], giving you a wink."
            else:
                "After her orgasm subsides, she moves her head to the side, letting the cum on dribble on the floor."

        "She straightens up and wipes her lips with the back of her hand."
        $ the_girl.call_dialogue("cum_mouth")

    elif the_choice == "Cum down her throat":
        "You put your hands on the back of [the_girl.title]'s head and pull her back down onto your shaft, hard."
        mc.name "Cum for me you dirty little slut!"
        if the_girl.sex_skills["Oral"] > 3:
            "[the_girl.possessive_title] keeps her mouth wide open for you, moaning hard as she is close to her orgasm."
        else:
            "[the_girl.possessive_title] gags on your cock as you push her down onto it."
            "Her body tightens up and you make sure to take advantage of her moaning, contracting throat by fucking it hard."

        "You grunt and twitch as you start to empty your balls down her esophagus."
        if the_girl.get_opinion_score("being submissive") > 0:
            if the_girl.sluttiness > the_girl.sluttiness and the_girl.sluttiness < blowjob.slut_cap:
                $ the_girl.change_slut(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.
                $ the_girl.change_slut(-the_girl.get_opinion_score("being submissive"))
            $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
            $ the_girl.have_orgasm()
            if the_girl.vagina_visible:
                "You can see that [the_girl.title]'s pussy is dripping wet as she starts shaking and enjoying her own orgasm."
            else:
                $ the_item = the_girl.outfit.get_lower_top_layer
                if the_item.underwear:
                    "[the_girl.title]'s trembling wet pussy has soaked her [the_item.display_name], and it drips fluid as she cums."
                else:
                    "[the_girl.title] clenches her thighs together and rides out her orgasm."
                $ the_item = None
            $ deepthroat.current_modifier = None
            $ the_girl.cum_in_mouth()
            $ deepthroat.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "You keep on sliding your dick down her tight throat, preventing her from breathing, until she finishes twitching."
            "When she's finished cumming you let [the_girl.title] pull back off your shaft. She gasps loudly for air."
            the_girl "That was... oh my god [the_girl.mc_title], I want you to do that again!"

        else:
            $ the_girl.have_orgasm()
            "When she's finished cumming you let [the_girl.title] pull back off your shaft. She gasps loudly for air, unable to speak."
            $ deepthroat.current_modifier = None
            $ the_girl.cum_in_mouth()
            $ deepthroat.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.change_stats(happiness = -2, obedience = 1)
            the_girl "Ah... fuck. This was nice, but go a little easier on me next time, okay?"
            "She clears her throat, then kisses the side of your dick."
        $ the_girl.call_dialogue("cum_mouth")

    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
