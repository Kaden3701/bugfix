init:
    python:
        cowgirl_handjob = Position(name = "Cowgirl Handjob", slut_requirement = 20, slut_cap = 50, requires_hard = False, requires_large_tits = False,
            position_tag = "kneeling1", requires_location = "Lay", requires_clothing = "None", skill_tag = "Foreplay",
            girl_arousal = 3, girl_energy = 10,
            guy_arousal = 14, guy_energy = 5,
            connections = [],
            intro = "intro_cowgirl_handjob",
            scenes = ["scene_cowgirl_handjob_1","scene_cowgirl_handjob_2", "scene_cowgirl_handjob_3"],
            outro = "outro_cowgirl_handjob",
            transition_default = "transition_default_cowgirl_handjob",
            strip_description = "strip_cowgirl_handjob", strip_ask_description = "strip_ask_cowgirl_handjob",
            orgasm_description = "orgasm_cowgirl_handjob",
            taboo_break_description = "taboo_break_cowgirl_handjob",
            verb = "stroke", verbing = "stroking",
            opinion_tags = ["giving handjobs", "facial", "get mc off"], record_class = "Handjobs",
            default_animation = blowjob_bob,
            associated_taboo = "touching_penis")

        list_of_girl_positions.append(cowgirl_handjob)
        cowgirl_handjob.girl_outro = "GIC_outro_cowgirl_handjob"


label intro_cowgirl_handjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_handjob.redraw_scene(the_girl)
    the_girl "I want to want to feel how hot that thing is in my hand."
    "She kisses you on the neck while her hands drift down to your pants.."
    "She slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes."
    "She brings her hand back to her mouth, spitting a generous portion of saliva on it, before returning it to your cock."
    "It feels great as she starts to stroke you off."
    return

label taboo_break_cowgirl_handjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_handjob.redraw_scene(the_girl)
    the_person "I'm sorry, I know I'm not usually this forward, but I just have to see what you're packing..."
    "She kisses you on the neck while her hands drift down to your pants.."
    "She slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes."
    "She brings her hand back to her mouth, spitting a generous portion of saliva on it, before returning it to your cock."
    "It feels great as she starts to stroke you off."
    return

label scene_cowgirl_handjob_1(the_girl, the_location, the_object):
    if not mc.recently_orgasmed:
        "[the_girl.possessive_title]'s hand is warm and soft as it slides up and down your dick."
        if mc.arousal_perc > 40:
            "She rubs her thumb over your tip, spreading your precum over it and then working it back to the shaft."
        else:
            "She rubs her thumb over your tip, then moves to the sensitive underside."
        the_girl "You're so big in my hand... Mmm."
    else:
        "[the_girl.possessive_title] fondles your soft cock, rubbing the tip with her thumb."
        the_girl "Mmm, even soft you're so big..."
        "Pretty soon you can feel your member returning to life from the attention [the_girl.title] is giving it."
    return


label scene_cowgirl_handjob_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] leans forward, and kisses at your neck as she strokes you."
    "[the_girl.title] moves her hand down and cups your balls, massaging them gently. Her lips move to your ears and she whispers softly."
    the_girl "I want you to let all of your cum out of here for me..."
    "She kisses your neck a few more times as her hand returns to stroking your erection."
    return

label scene_cowgirl_handjob_3(the_girl, the_location, the_object):
    "[the_girl.possessive_title] gives you a few fast strokes, then lets go."
    the_girl "One second..."
    "She brings her hand up to her mouth and sticks her tongue out, running it from her palm to the tips of her fingers."
    "She reaches back down and wraps her slippery hand around your cock again. She starts to gently stroke it."
    return

label outro_cowgirl_handjob(the_girl, the_location, the_object):
    "Little by little the soft hand of [the_girl.title] brings you closer to orgasm."
    "She can sense you are getting close and has started to speed up her stroking."
    if the_girl.facial_or_swallow() == "facial" or the_girl.sluttiness > 50:
        mc.name "Fuck, here I come!"
        the_girl "Oh god, cover my face in it!"
        "[the_girl.possessive_title] moves down your body, still stroking your cock while she aims it at her face."

        if the_girl.effective_sluttiness() > 80:
            "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
        elif the_girl.effective_sluttiness() > 60:
            "[the_girl.title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
        "You take a deep breath and lay back, enjoying your post-orgasm bliss. [the_girl.title] looks up at you, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")
    else:
        mc.name "Fuck, I'm about to cum!"
        "[the_girl.title]'s keeps stroking, pushing you over the edge."
        "Your cum erupts, shooting up and over your stomach. It feels great even though you are just making a mess of yourself.."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
        $ cowgirl_handjob.redraw_scene(the_girl)
        if the_girl.effective_sluttiness() > 90 or the_girl.has_cum_fetish:
            "Once you've finished, she brings her hand to her lips and starts to lick your cum off it."
            $ the_girl.draw_person(position = "blowjob")
            "Not someone to let good cum go to waste, she lowers her face to your stomach and starts to lick your cum off of it."
            $ play_moan_sound()
            "She moans happily as she finishes slurping up the last of your cum from your body."
            $ cowgirl_handjob.redraw_scene(the_girl)
        else:
            "She gives you a few more strokes until you're completely spent, then lets go and gives you a kiss."

    return


label transition_default_cowgirl_handjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_handjob.redraw_scene(the_girl)
    the_girl "I want to want to feel how hot that thing is in my hand."
    "She kisses you on the neck while her hands drift down to your pants.."
    "She slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes."
    "She brings her hand back to her mouth, spitting a generous portion of saliva on it, before returning it to your cock."
    "It feels great as she starts to stroke you off."
    return

label strip_cowgirl_handjob(the_girl, the_clothing, the_location, the_object):

    "[the_girl.title] stops stroking your for a second and looks at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on top of you and starts stroking you again."
    return

label strip_ask_cowgirl_handjob(the_girl, the_clothing, the_location, the_object):
    $ return_value = True

    "[the_girl.title] stops stroking your for a second and looks at you."
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cowgirl_handjob.position_tag)
            "[the_girl.possessive_title] strips out of her [the_clothing.name]. Then she gets back to work and starts stroking you again."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                "She whispers in your ear as she starts to stroke you again."
                the_girl "Yeah? Do I look sexy in it?"
            else:
                "She whispers in your ear as she starts to stroke you again."
                the_girl "Does it make me look like a good little slut? Or is your giant cock in my hand enough fro that?"
            $ return_value = False

    return return_value

label orgasm_cowgirl_handjob(the_girl, the_location, the_object):
    "[the_girl.title] pauses suddenly. You hear her whimper softly."
    "You notice she has one hand between her legs, getting herself off while she strokes you with the other hand."
    $ play_moan_sound()
    "She stops moving her hand and moans. She is cumming!"
    "When she finishes she looks at you and smiles before resuming stroking your cock."
    return

label GIC_outro_cowgirl_handjob(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    if the_goal == "get off" or the_goal == "hate fuck" or the_goal == "vaginal creampie" or the_goal == "anal creampie" or the_goal is None or the_goal == "get mc off":
        $ cowgirl_handjob.call_default_outro(the_girl, the_location, the_object)
    elif the_goal == "waste cum":
        "Little by little the soft hand of [the_girl.title] brings you closer to orgasm."
        mc.name "Fuck, here I come!"
        "[the_girl.possessive_title] keeps stroking you. She points your cock... up at you?"
        the_girl "I'm not letting your spunk touch me!"
        "You groan but you don't have time to take over, so you just lay back and let your orgasm overtake you."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
        "Thick strands of cum erupt as you orgasm. It ropes up and out over your belly."
        "When you finish you lay back and [the_girl.title] stops stroking you. She has a naughty smile on her face."
        $ the_girl.change_stats(happiness = 2, obedience = -3)
        "She wipes her hand on your leg and starts to get up."
    elif the_goal == "facial" or the_goal == "body shot":
        "Little by little the soft hand of [the_girl.title] brings you closer to orgasm."
        mc.name "Fuck, here I come!"
        the_girl "Oh god, cover my face in it!"
        "[the_girl.possessive_title] moves down your body, still stroking your cock while she aims it at her face."

        if the_girl.effective_sluttiness() > 80:
            "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
        elif the_girl.effective_sluttiness() > 60:
            "[the_girl.title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ cowgirl_handjob.redraw_scene(the_girl)
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
        "You take a deep breath and lay back, enjoying your post-orgasm bliss. [the_girl.title] looks up at you, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")


    elif the_goal == "oral creampie":
        "Little by little the soft hand of [the_girl.title] brings you closer to orgasm."
        mc.name "Fuck, here I come!"
        the_girl "Oh god, I want to taste it!"

        $ the_girl.draw_person(position = "blowjob")
        "Just hearing her say that would have pushed you over the edge - her soft, wet hand working your cock is just a bonus."
        "She opens up her mouth and sticks out her tongue, presenting you with a clear target."
        $ the_girl.cum_in_mouth()
        $ cowgirl_handjob.redraw_scene(the_girl)
        "You spasm and shoot out a pulse of hot sperm, splashing it over her tongue and down the back of her throat."
        $ the_girl.cum_on_face()
        $ cowgirl_handjob.redraw_scene(the_girl)
        $ play_swallow_sound()
        "She maintains eye contact as you fire off the rest of your load over her face, she closes her mouth and swallows quietly."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
        $ the_girl.call_dialogue("cum_mouth")
    else:
        $ cowgirl_handjob.call_default_outro(the_girl, the_location, the_object)
    return
