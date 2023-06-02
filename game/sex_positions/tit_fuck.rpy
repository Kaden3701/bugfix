init:
    python:
        tit_fuck = Position(name = "Tit Fuck", slut_requirement = 30, slut_cap = 55, requires_hard = True, requires_large_tits = True,
            position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "Tits", skill_tag = "Foreplay",
            girl_arousal = 5, girl_energy = 20,
            guy_arousal = 15, guy_energy = 5,
            connections = [],
            intro = "intro_tit_fuck",
            scenes = ["scene_tit_fuck_1","scene_tit_fuck_2", "scene_tit_fuck_3", "scene_SB_Titfuck_Kneeling_1", "scene_SB_Titfuck_Kneeling_2"],
            outro = "outro_tit_fuck",
            transition_default = "transition_default_tit_fuck",
            strip_description = "strip_tit_fuck", strip_ask_description = "strip_ask_tit_fuck",
            orgasm_description = "orgasm_tit_fuck",
            taboo_break_description = "taboo_break_tit_fuck",
            verb = "tit fuck",
            opinion_tags = ["giving tit fucks"], record_class = "Tit Fucks",
            default_animation = tit_bob,
            associated_taboo = "touching_body")

        list_of_positions.append(tit_fuck) #TODO: Decide if this should be a girl_position too.

#init 1:
    #python:
        #Here is where you would put connections if they existed.
        #TODO: Transition to a tit-blowjob.

label intro_tit_fuck(the_girl, the_location, the_object):
    #This position requires free (and big) tits, so we can assume they're available for everything.
    "You place a hand on [the_girl.possessive_title]'s shoulder and rub it gently, then move down to her sizeable [the_girl.tits] cup tits and squeeze them."
    the_girl "Ah... Do you like them?"
    mc.name "Of course I like them. I'd like them even more if they were wrapped around my cock."
    if not the_girl.tits_visible:
        the_girl "Well then let's get these puppies out."
        $ the_girl.strip_to_tits(position = tit_fuck.position_tag)

    "She smiles and nods, reaching down to your waist and undoing your pants zipper."
    $ tit_fuck.redraw_scene(the_girl)
    "When your cock springs out, already hard, she drops to her knees in front of you."
    "She takes her tits up in her hands and lifts them up, pressing them on either size of your shaft."
    if the_girl.has_large_tits: #E sized or larger
        "They're warm, soft, and feel like they melt around your sensitive dick. Her breasts are so large the tip of your cock doesn't even make it to the top of her cleavage."
    else:
        "They're warm, soft, and feel like they melt around your sensitive dick. The tip of your cock just barely pops out of the top of her cleavage."
    return

label taboo_break_tit_fuck(the_girl, the_location, the_object):
    "You place a hands on [the_girl.possessive_title]'s shoulders and rub them gently for a few seconds."
    "Then you move them lower, towards her sizeable [the_girl.tits] cup tits."
    "You're just about to grab them when she reaches up and holds your hands, stopping you from moving them any closer."
    $ the_girl.call_dialogue(tit_fuck.associated_taboo+"_taboo_break")
    "She lets go of your hands and you slide them over her breasts. They're soft and heavy with a pleasant jiggle to them."
    mc.name "These feel amazing. Could you use them to take care of this?"
    if not mc.recently_orgasmed:
        "You grind your erection against [the_girl.title]'s thigh while you squeeze her tits."
    #TODO: Maybe also a taboo break for touching your penis
    if the_girl.effective_sluttiness(tit_fuck.associated_taboo) > tit_fuck.slut_cap:
        the_girl "Of course I can. You're going to have to let go of these first though."
        "She places her hands over yours and presses them against her breasts."
        the_girl "I promise I'll put them to good use."
        if not the_girl.tits_visible:
            the_girl "Well then let's set them free."
            $ the_girl.strip_to_tits(position = tit_fuck.position_tag)

        "She lets go of your hands and kneels down, taking her tits into her own hands."
    else:
        the_girl "I can try. You're going to have to let go of me first though."
        if not the_girl.tits_visible:
            the_girl "Well, let me get them ready for you."
            $ the_girl.strip_to_tits(position = tit_fuck.position_tag)
        "She lifts your hands off of her chest and kneels down, taking her tits up into her own hands"
    $ the_girl.draw_person(position = "blowjob")
    "She hefts her breasts up and presses them on either side of your shaft."
    if the_girl.has_large_tits: #E sized or larger
        "They're warm, soft, and feel like they melt around your sensitive dick. Her breasts are so large the tip of your cock doesn't even make it to the top of her cleavage."
    else:
        "They're warm, soft, and feel like they melt around your sensitive dick. The tip of your cock just barely pops out of the top of her cleavage."
    $ tit_fuck.redraw_scene(the_girl)
    "She starts to heft them up and down, working your cock with them."
    return

label scene_tit_fuck_1(the_girl, the_location, the_object):
    "[the_girl.possessive_title] works her tits up and down your cock, alternating between slow and fast strokes."
    $ the_girl.change_arousal(the_girl.get_opinion_score("giving tit fucks"))
    the_girl "Mmm, do my tits feel good? Your cock feels so good between them."
    "She jiggles her tits in opposite directions to each other, then presses down hard on them and gives you a few powerful strokes."
    return

label scene_tit_fuck_2(the_girl, the_location, the_object):
    "You reach down and grab [the_girl.title]'s tits yourself. She places her hands over yours and holds them in place."
    $ the_girl.change_arousal(the_girl.get_opinion_score("giving tit fucks"))
    the_girl "Mmm, fuck my tits [the_girl.mc_title], they're all yours."
    $ play_moan_sound()
    "You squeeze down hard on her breasts and work your hips, fucking her soft cleavage. [the_girl.title] moans in response."
    "When you're satisfied you let go and let her take over again."
    return

label scene_tit_fuck_3(the_girl, the_location, the_object):
    "[the_girl.possessive_title] gives you a few fast strokes with her tits, then stops and tilts her head down."
    "She lets a long line of saliva drip down between her tits and onto the tip of your cock."
    "She gives your shaft a few strokes, spreading her spit and lubricating her cleavage. She looks up at you from her knees and smiles."
    $ the_girl.change_arousal(the_girl.get_opinion_score("giving tit fucks"))
    the_girl "There, much better."
    "She starts servicing you with her tits again, now gliding quickly and easily over your hard dick."
    return

label scene_SB_Titfuck_Kneeling_1(the_girl, the_location, the_object):

    "[the_girl.possessive_title] sticks her tongue out and licks at the tip of your dick each time she moves her body down."
    $ play_moan_sound()
    "She moans slightly as she pauses to stroke you with her soft, velvet lips. She gets your shaft nice and wet and then continues heaving her chest up and down."
    $ play_moan_sound()
    "The extra lubrication feels great, causing you to let out an appreciative moan."
    if the_girl.sex_skills["Foreplay"] < 2: #Inexperienced.
        "[the_girl.title] is trying her best to pleasure you with her chest, but her inexperience is starting to show."
        "She is pushing her tits together, but she is doing it too hard. It doesn't hurt, but the sensation isn't particularly pleasurable."
        mc.name "Mmm, easy, you aren't trying to strangle it. Tits are soft, your grip should be soft too."
        "[the_girl.title] mutters a quick apology, but lightens up her grip. It feels much better when she resumes stroking you."
    else: #Is experienced
        "[the_girl.title]'s creamy pillows feel amazing wrapped around your erection."
        $ play_moan_sound()
        "[the_girl.possessive_title] lets out a moan. She pinches her nipples while you pound her pillows."

        "She grabs your cock with her hand and then pulls her chest back from around you. She takes the tip of your cock and uses it to tease her nipples."
        the_person "Mmm, my nipples are so sensitive."
        "[the_girl.title] raps her chest a few times now with your cock, sending ripples out from the point of impact."

    return

label scene_SB_Titfuck_Kneeling_2(the_girl, the_location, the_object):
    if the_girl.is_bald:
        "You run your hand over [the_girl.title]'s smooth scalp while she bounces her [the_girl.tits_description] up and down."
    else:
        "You run your hand through [the_girl.title]'s hair while she bounces her [the_girl.tits_description] up and down."
    "You move your hand down to her shoulder and grasp it firmly, stopping her motion. You begin to buck your hips, giving her a break from her motions."
    "Her hands move to your ass, and you can feel her gently urging you as you thrust up against her."
    if the_girl.has_large_tits:   #Must have a certain cup size
        "You look down and can barely see the tip of your cock poking up from between [the_girl.title]'s generous chest."
        mc.name "Your tits feel so good. You should play with them while I thrust."
        "She takes her hands and runs them along the sides of her breasts. Her abundance of tit flesh feels amazing wrapped around you."
        "[the_girl.title] starts to pinch and pull at her nipples."
        if the_girl.has_cum_fetish:
            the_person "Mmm, your cock is so hot, I can't wait to feel your cum bursting out, all over me."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(5 + the_girl.get_opinion_score("giving tit fucks"))
        else:
            the_person "Your cock is so hot, it feels so right up against my body like this."
            "She pinches her nipples hard and pulls on them, causing her to cry out."
            $ the_girl.change_arousal(3 + the_girl.get_opinion_score("giving tit fucks"))
    else:                           #She has smaller tits
        "Her hands leave your ass and she brings her hands to the sides of her chest, squishing her tits together to try and stimulate you better."
        mc.name "Mmm, that's it, push them together like that."
        "You keep thrusting. [the_girl.title] gathers some saliva in her mouth and then spits on the head of your cock."
        the_person "Gotta keep things lubricated..."
        "She spits again. You can feel her spit coating your cock and it slides a little smoother between her tits now."
    "You let go of her shoulders. She looks up at you, smiles, and then resumes fucking you with her tits."
    return

label outro_tit_fuck(the_girl, the_location, the_object):
    "Her warm, soft tits wrapped around your sensitive cock drive you closer and closer to climax with each stroke up and down."
    the_girl "You're so tense, are you going to cum?"
    "You nod and she speeds up."
    the_girl "Cum for me [the_girl.mc_title], cum for me!"
    $ climax_controller = ClimaxController(["Cum between her tits", "air"],["Cum on her face","face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum between her tits":
        "You close your eyes and focus on the sensation of [the_girl.possessive_title]'s warm, soft breasts massaging your cock."
        $ climax_controller.do_clarity_release(the_girl)
        "Your orgasm builds to a peak and you grunt, blasting your load up between [the_girl.title]'s tits and out the top of her cleavage."
        $ the_girl.draw_person(position = "kneeling1")
        $ the_item = the_girl.outfit.get_upper_top_layer
        if the_item: #There's something on her top
            "Your cum splatters down over [the_girl.title]'s [the_item.display_name]. She gasps as the warm liquid covers her and drips back down between her tits."
        else:
            "Your cum splatters down over the top of [the_girl.title]'s tits. She gasps as the warm liquid covers her and drips back down between her tits."
        $ the_item = None

        $ the_girl.cum_on_tits()
        $ the_girl.draw_person(position = "kneeling1")

    elif the_choice == "Cum on her face":
        "You close your eyes and focus on the sensation of [the_girl.possessive_title]'s warm, soft breasts massaging your cock."
        "As your orgasm builds to its peak you step back, sliding your cock out from her cleavage and take it up in your own hand."
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.effective_sluttiness() > 40 or the_girl.get_opinion_score("cum facials") > 0:
            "[the_girl.title] understands immediately what is about to happen and tilts her head up, giving you a clear target."
            $ climax_controller.do_clarity_release(the_girl)
            "You stroke yourself to completion and blast your load over her face, throwing thick ropes of cum her lips and nose and eyes."
        else:
            the_girl "What's wrong? I...!"
            $ climax_controller.do_clarity_release(the_girl)
            "You grunt and climax, blasting thick ropes of cum over [the_girl.title]'s surprised face. She jerks back, then waits until you're finished."
        $ the_girl.cum_on_face()
        $ the_girl.draw_person(position = "kneeling1")

    the_girl "Ah... Wow..."
    return

label transition_default_tit_fuck(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You grab a hold of sizeable tits and give them a gentle squeeze, bringing a little moan from her lips."
    mc.name "I want to feel my cock between these lovely tits."
    if not the_girl.tits_visible:
        the_girl "Let's get them ready for you."
        $ the_girl.strip_to_tits(position = tit_fuck.position_tag)
    $ tit_fuck.redraw_scene(the_girl)
    "She smiles and nods, dropping to her knees in front of you. She gathers her tits up in her hands and presses them to the side of your shaft."
    return

label strip_tit_fuck(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    "[the_girl.title] leans back, letting your cock slide out of her cleavage, and pulls off her [the_clothing.name]."
    $ the_girl.draw_animated_removal(the_clothing, position = tit_fuck.position_tag)
    "She pulls it off and drops it at her side, then leans back and engulfs your hard cock in her breasts again."
    return

label strip_ask_tit_fuck(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], would you like me to take off my [the_clothing.name]?"
    "She works her tits up and down while she waits for you to respond."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = tit_fuck.position_tag)
            "[the_girl.title] leans back, letting your cock slide out of her cleavage, and pulls off her [the_clothing.name]."
            the_girl "Ah, so much better. Now, where were we..."
            "She leans back and engulfs your hard cock in her breasts again."
            return True

        "Leave it on":
            mc.name "I think you look cute in it, leave it on."
            "She nods and keeps working her tits up and down."
            return False
    return

label orgasm_tit_fuck(the_girl, the_location, the_object):
    "[the_girl.title] speeds up her tit fuck, servicing your cock as fast as she can manage."
    "Suddenly she squeezes down on her tits and through them your cock, gasping softly."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She holds her breath as her body is wracked with an orgasm, then lets it out as a loud sigh when she recovers."
    the_girl "I... Wow... Feeling your cock between my tits like this just made me..."
    $ play_moan_sound()
    "She moans and starts tit fucking you again, going at it with renewed vigor."
    return
