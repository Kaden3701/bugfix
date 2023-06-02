label GIC_outro_cowgirl(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal is None or the_goal == "get mc off" or the_goal == "anal creampie":
        $ cowgirl.call_default_outro(the_girl, the_location, the_object)

    else:
        "With each stroke of her hips [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        if the_goal == "get off":
            the_girl "Seriously? I haven't finished yet..."
            if mc.condom:
                "She keeps riding you. With one final stroke you start to cum into the condom."
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."
            else:
                "You stay silent. [the_girl.possessive_title] waits another second, as if waiting for a response, then pulls off of your cock."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_girl.cum_on_stomach()
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "waste cum":
            the_girl "You wanna cum inside me? Do you?"
            "She starts to speed up. You moan as you get ready to fire your load up inside her."
            if mc.condom:
                "At the last second she pulls off and pulls your condom off. You groan as your start to cum, spraying all over your stomach."
            else:
                "At the last second she pulls off, you groan as your start to cum, spraying all over your stomach."
            the_girl "Ha! Not a chance."
            "She watches as your cock twitches and finishes."
            $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
            the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "hate fuck":
            if the_girl.on_birth_control or mc.condom:
                the_girl "Already? I guess I was just too much for you to handle."
                if mc.condom:
                    the_girl "Whatever, I'm sure the condom can handle your pathetic load."
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."
                else:
                    the_girl "I don't feel like getting off. Go ahead and cum inside me [the_girl.mc_title], I'm on birth control anyway."
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ the_girl.cum_in_vagina()
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                    $ cowgirl.redraw_scene(the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
            else:
                the_girl "Already? Is my cunt to just too much for you to handle?"
                if the_girl.wants_creampie:
                    the_girl "Whatever. I want to feel you cum inside me. Not like your swimmers are strong enough to knock me up anyway."
                    "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                    $ the_girl.cum_in_vagina()
                    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                    $ cowgirl.redraw_scene(the_girl)
                    "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                    "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
                else:
                    the_girl "Whatever. Hurry up and cum."
                    "She starts to speed up. You moan as you get ready to fire your load up inside her."
                    "At the last second she pulls off, you groan as your start to cum, spraying all over your stomach."
                    "She watches as your cock twitches and finishes."
                    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
                    the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "vaginal creampie":
            the_girl "Yes! Ah!"
            "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
            "Her breath catches in her throat when you pulse out your hot load of cum deep inside of her."
            #the_girl "Oh my god... Give it all to me [the_girl.mc_title]... Fill me up..."
            if mc.condom:
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."

                call post_orgasm_condom_routine(the_girl, cowgirl) from _call_post_orgasm_condom_routine_GIC_cowgirl

            else:
                $ the_girl.call_dialogue("cum_vagina")
                $ the_girl.cum_in_vagina()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                $ cowgirl.redraw_scene(the_girl)
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "facial":
            if mc.condom:
                "[the_girl.possessive_title] pulls off you, but quickly moves down your body. She pulls off the condom and begins stroking you while pointing it at her face."
            else:
                "[the_girl.possessive_title] pulls off you, but quickly moves down your body and begins stroking your cock. She points it at her face."
            $ the_girl.draw_person(position = "kneeling1")
            the_girl "That's it. I want it on my face!"
            "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            "[the_girl.title] looks up at you, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")
        elif the_goal == "body shot":
            the_girl "Ohhh, I can't wait to feel it on my skin."
            if mc.condom:
                "[the_girl.possessive_title] pulls off you, reaches down and pulls your condom off and begins stroking you."
            else:
                "[the_girl.possessive_title] pulls off you, reaches down and begins to stroke you."
            "She grinds the lips of her [the_girl.pubes_description] pussy against your shaft as you climax. You fire your hot load over her stomach."
            $ the_girl.cum_on_stomach()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
            $ the_girl.draw_person(position = "missionary")
            "She rolls off and lies next to you on the [the_object.name]."
        elif the_goal == "oral creampie":
            the_girl "Wait! I want it in my mouth!"
            if mc.condom:
                "[the_girl.possessive_title] pulls off you, but quickly moves down your body. She pulls off the condom and takes you into her mouth."
            else:
                "[the_girl.possessive_title] pulls off you, but quickly moves down your body and takes you into her mouth."
            $ the_girl.draw_person(position = "kneeling1")
            $ play_moan_sound()
            "She moans as your cum begins to spill into her mouth"
            $ the_girl.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm into [the_girl.possessive_title]'s eager mouth. She makes sure to wait until you're completely finished."
            $ play_swallow_sound()
            "[the_girl.title] closes her mouth and swallows loudly."
            "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        else:
            "DEBUG tell starbuck she fucked up you shouldn't be here"
            pass
    return

label GIC_outro_handjob(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()
    # describe wanting to cum
    #TODO
    $ handjob.call_default_outro(the_girl, the_location, the_object)
    return

label GIC_outro_tit_fuck(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()
    if the_goal == "body shot": #Code for cum on tits
        "With each stroke of her tits [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        the_girl "Yes! Ah! Cover my tits with it!"
        "You watch closely as [the_girl.possessive_title]'s warm tits bring you to your orgasm."
        $ the_girl.cum_on_tits()
        $ ClimaxController.manual_clarity_release(climax_type = "tits", the_person = the_girl)
        "Your orgasm builds to a peak and you grunt, blasting your load up between [the_girl.title]'s tits and out the top of her cleavage."
        $ the_girl.draw_person(position = "kneeling1")
        $ the_item = the_girl.outfit.get_upper_top_layer
        if the_item: #There's something on her top
            "Your cum splatters down over [the_girl.title]'s [the_item.display_name]. She gasps as the warm liquid covers her and drips back down between her tits."
        else:
            "Your cum splatters down over the top of [the_girl.title]'s tits. She gasps as the warm liquid covers her and drips back down between her tits."
        $ the_item = None
        the_girl "Oh my god, it's so warm..."
    else:
        $ tit_fuck.call_default_outro(the_girl, the_location, the_object)
    return

init 7 python:
    tit_fuck.girl_outro = "GIC_outro_tit_fuck"
    handjob.girl_outro = "GIC_outro_handjob"
    cowgirl.girl_outro = "GIC_outro_cowgirl"
