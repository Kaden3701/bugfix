# Special titfuck for Sarah. After a few rounds with MC, she gains some foreplay skill and gains this position.
# Because tit fucks are foreplay, low slut cap, so we make several opportunities to arouse Sarah during, to make her more likely to orgasm from this.

init:
    python:
        sarah_tit_fuck = Position(name = "Special Tit Fuck", slut_requirement = 30, slut_cap = 55, requires_hard = True, requires_large_tits = True,
            position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "Tits", skill_tag = "Foreplay",
            girl_arousal = 7, girl_energy = 20,
            guy_arousal = 15, guy_energy = 5,
            connections = [],
            intro = "intro_sarah_tit_fuck",
            scenes = ["scene_sarah_tit_fuck_1","scene_sarah_tit_fuck_2", "scene_sarah_tit_fuck_3"],
            outro = "outro_sarah_tit_fuck",
            transition_default = "transition_default_sarah_tit_fuck",
            strip_description = "strip_sarah_tit_fuck", strip_ask_description = "strip_ask_sarah_tit_fuck",
            orgasm_description = "orgasm_sarah_tit_fuck",
            taboo_break_description = "taboo_break_sarah_tit_fuck",
            verb = "tit fuck",
            opinion_tags = ["giving tit fucks"], record_class = "Tit Fucks",
            default_animation = tit_bob,
            associated_taboo = "touching_body")

        #list_of_positions.append(sarah_tit_fuck) #TODO: Decide if this should be a girl_position too.

label intro_sarah_tit_fuck(the_girl, the_location, the_object):
    #This position requires free (and big) tits, so we can assume they're available for everything.
    "You place a hand on [the_girl.possessive_title]'s shoulder and rub it gently, then move down to her sizeable [the_girl.tits] cup tits and squeeze them."
    the_girl "Mmm, I love when you touch me like this. They are so sensitive ever since they got bigger."
    "She reaches down and rubs your cock."
    the_girl "Want to put your cock between them again? It feels so good, I think I'm getting addicted to that feeling."
    mc.name "Mmm, do it [the_girl.title]."
    "[the_girl.possessive_title] gets down on her knees. She starts to open up your pants."
    if not the_girl.tits_visible:
        the_girl "Well, let me get them ready for you."
        $ the_girl.strip_to_tits(position = sarah_tit_fuck.position_tag, visible_enough = True, prefer_half_off = False)

    $ sarah_tit_fuck.redraw_scene(the_girl)
    "She takes her tits up in her hands and lifts them up, pressing them on either size of your shaft."
    "They're warm, soft, and feel like they melt around your sensitive dick. Her breasts are so large the tip of your cock doesn't even make it to the top of her cleavage."
    return

label taboo_break_sarah_tit_fuck(the_girl, the_location, the_object):
    "You place a hands on [the_girl.possessive_title]'s shoulders and rub them gently for a few seconds."
    "Then you move them lower, towards her sizeable [the_girl.tits] cup tits."
    "You're just about to grab them when she reaches up and holds your hands, stopping you from moving them any closer."
    $ the_girl.call_dialogue(sarah_tit_fuck.associated_taboo+"_taboo_break")
    "She lets go of your hands and you slide them over her breasts. They're soft and heavy with a pleasant jiggle to them."
    mc.name "These feel amazing. Could you use them to take care of this?"
    if not mc.recently_orgasmed:
        "You grind your erection against [the_girl.title]'s thigh while you squeeze her tits."
    #TODO: Maybe also a taboo break for touching your penis
    if the_girl.effective_sluttiness(sarah_tit_fuck.associated_taboo) > sarah_tit_fuck.slut_cap:
        the_girl "Of course I can. You're going to have to let go of these first though."
        "She places her hands over yours and presses them against her breasts."
        the_girl "I promise I'll put them to good use."
        $ the_girl.draw_person(position = "kneeling1")
        "She lets go of your hands and kneels down."
    else:
        the_girl "I can try. You're going to have to let go of me first though."
        $ the_girl.draw_person(position = "kneeling1")
        "She lifts your hands off of her chest and kneels down."

    if not the_girl.tits_visible:
        the_girl "Well, let me get them ready for you."
        $ the_girl.strip_to_tits(position = sarah_tit_fuck.position_tag, visible_enough = True, prefer_half_off = False)

    $ sarah_tit_fuck.redraw_scene(the_girl)
    "She hefts her breasts up and presses them on either side of your shaft."
    if Person.rank_tits(the_girl.tits) >= 7: #E sized or larger
        "They're warm, soft, and feel like they melt around your sensitive dick. Her breasts are so large the tip of your cock doesn't even make it to the top of her cleavage."
    else:
        "They're warm, soft, and feel like they melt around your sensitive dick. The tip of your cock just barely pops out of the top of her cleavage."
    $ sarah_tit_fuck.redraw_scene(the_girl)
    "She starts to heft them up and down, working your cock with them."
    return

label scene_sarah_tit_fuck_1(the_girl, the_location, the_object):
    "[the_girl.possessive_title] works her tits up and down your cock, alternating between slow and fast strokes."
    "Your erection is lost between her enormous mounds. You are both well endowed, you thrust your hips, eager to feel every square inch of her soft tit-flesh."
    the_girl "Your cock feels so good... I can't help it..."
    "You look down. She has one arm below her chest, holding her tits together, and with her other hand she is pinching and pulling one of her nipples."
    $ the_girl.change_arousal(5)
    the_girl "Oh fuck. Yes! Oh god it feels so good."
    "She closes her eyes but keeps playing with herself."
    return

label scene_sarah_tit_fuck_2(the_girl, the_location, the_object):
    "You reach down and grab [the_girl.title]'s tits yourself. She looks up at you and smiles."
    mc.name "I'll hold them for a bit. That way you can have your hands free."
    the_girl "Mmm, fuck my tits [the_girl.mc_title], they're all yours!"
    "You squeeze down hard on her breasts and work your hips, fucking her soft cleavage. [the_girl.title] moans in response."
    "She reaches down with her free hand and starts to play with her [the_girl.pubes_description] pussy. Her eyes glaze over for a bit as the sensations start to overwhelm her."
    $ the_girl.change_arousal(10 + (3 * the_girl.get_opinion_score("masturbating")))
    $ play_spank_sound()
    "With her other hand she smacks your ass, then grabs it, urging you to fuck her tits harder."
    the_girl "That's it! My tits are yours to use... Make me cum, then cover me in yours!"
    "You pinch her nipples and she squeals. God this girl loves getting her titties played with."
    "When you're satisfied you let go and let her take over again."
    return

label scene_sarah_tit_fuck_3(the_girl, the_location, the_object):
    "[the_girl.possessive_title] gives you a few fast strokes with her tits, then stops and tilts her head down."
    "She lets a long line of saliva drip down between her tits. Your cock is lost between them, but you feel the lubrication trickle down onto it."
    "She gives your shaft a few strokes, spreading her spit and lubricating her cleavage. She looks up at you from her knees and smiles."
    the_girl "Hmm... that's a little bit better."
    "She looks down, then pushes her tits down all the way to your base. The tip of your cock is just poking up between them. A bit of precum leaks out."
    the_girl "Mmm! It looks so yummy..."
    "She strains her neck down a bit and licks the precum from the tip. She moans when she tastes it."
    "She opens her mouth and takes the tip of your erection into her velvet lips. Her tongue begins to swirl all around it."
    "[the_girl.possessive_title] takes her hands and squeezes her tits together rhythmically. She isn't stroking you with them, but the variations in pressure of her tit-flesh feels great."
    "Slowly, she lets your cock free from her mouth. A large string of drool connects her lips to the tip for several seconds until it breaks."
    "[the_girl.title] starts to slowly tit fuck you again. When she had you in her mouth, she must have been slobbering all over you, because your cock is slick with lubrication."
    "Her cleavage shines with saliva as your cock disappears between them again. Her breasts somehow feel even better now that there is considerable lubrication between them."
    return


label outro_sarah_tit_fuck(the_girl, the_location, the_object):

    "Her warm, soft tits wrapped around your sensitive cock and expert technique are driving you to an imminent orgasm."
    the_girl "Oh my god, it's twitching. Cum for me [the_girl.mc_title]! I want you to cum!!!"
    "She speeds up."
    menu:
        "Cum between her tits":
            "You close your eyes. The sensation of [the_girl.possessive_title]'s warm, soft breasts massaging your cock is too intense to cum anywhere else."
            "Your orgasm builds to a peak and you grunt, blasting your load up between [the_girl.title]'s tits and out the top of her cleavage."
            $ the_item = the_girl.outfit.get_upper_top_layer
            if the_item: #There's something on her top
                "Your cum splatters down over [the_girl.title]'s [the_item.display_name]. She gasps as the warm liquid covers her and drips back down between her tits."
            else:
                "Your cum splatters down over the top of [the_girl.title]'s tits. She gasps as the warm liquid covers her and drips back down between her tits."
            $ the_item = None
            $ the_girl.cum_on_tits()
            $ sarah_tit_fuck.redraw_scene(the_girl)
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)

        "Cum on her face":
            "You close your eyes and focus on the sensation of [the_girl.possessive_title]'s warm, soft breasts massaging your cock."
            "As your orgasm builds to its peak, you step back, slide your cock out from her cleavage and take it up in your own hand."
            $ the_girl.draw_person(position = "kneeling1")
            if the_girl.effective_sluttiness() > 40 or the_girl.get_opinion_score("cum facials") > 0:
                "[the_girl.title] understands immediately what is about to happen and tilts her head up, giving you a clear target."
                "You stroke yourself to completion and blast your load over her face, throwing thick ropes of cum on her lips, nose, and eyes."
            else:
                the_girl "What's wrong? I...!"
                "You grunt and climax, blasting thick ropes of cum over [the_girl.title]'s surprised face. She jerks back, then waits until you're finished."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)

    the_girl "Ah... Wow..."
    return

label transition_default_sarah_tit_fuck(the_girl, the_location, the_object):
    if not the_girl.tits_visible:
        the_girl "Well, let's get the puppies out to play."
        $ the_girl.strip_to_tits(position = sarah_tit_fuck.position_tag, visible_enough = True, prefer_half_off = False)
    $ sarah_tit_fuck.redraw_scene(the_girl)
    "You grab a hold of her sizeable tits and give them a gentle squeeze, bringing a little moan from her lips."
    mc.name "I want to feel my cock between these lovely tits again."
    "She smiles and nods, dropping to her knees in front of you. She gathers her tits up in her hands and presses them to the side of your shaft."
    return

label strip_sarah_tit_fuck(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    "[the_girl.title] leans back, letting your cock slide out of her cleavage, and pulls off her [the_clothing.name]."
    $ the_girl.draw_animated_removal(the_clothing, position = sarah_tit_fuck.position_tag)
    "She pulls it off and drops it at her side, then leans back and engulfs your hard cock in her breasts again."
    return

label strip_ask_sarah_tit_fuck(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], would you like me to take off my [the_clothing.name]?"
    "She works her tits up and down while she waits for you to respond."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = sarah_tit_fuck.position_tag)
            "[the_girl.title] leans back, letting your cock slide out of her cleavage, and pulls off her [the_clothing.name]."
            the_girl "Ah, so much better. Now, where were we..."
            "She leans back and engulfs your hard cock in her breasts again."
            return True

        "Leave it on":
            mc.name "I think you look cute in it, leave it on."
            "She nods and keeps working her tits up and down."
            return False

label orgasm_sarah_tit_fuck(the_girl, the_location, the_object):
    "[the_girl.title] speeds up her tit fuck, servicing your cock as fast as she can manage."
    "Suddenly she squeezes down on her tits and through them your cock, gasping softly."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She holds her breath as her body is wracked with an orgasm, then lets it out as a loud sigh when she recovers."
    the_girl "I can't help it, it feels so good between my tits..."
    "She moans and starts tit fucking you again, going at it with renewed vigor."
    return
