init:
    python:
        cowgirl_blowjob = Position(name = "Cowgirl Blowjob", slut_requirement = 40, slut_cap = 60, requires_hard = True, requires_large_tits = False,
            position_tag = "blowjob", requires_location = "Lay", requires_clothing = "None", skill_tag = "Oral",
            girl_arousal = 3, girl_energy = 13,
            guy_arousal = 16, guy_energy = 5,
            connections = [],
            intro = "intro_cowgirl_blowjob",
            scenes = ["scene_cowgirl_blowjob_1","scene_cowgirl_blowjob_2", "scene_cowgirl_blowjob_3"],
            outro = "outro_cowgirl_blowjob",
            transition_default = "transition_default_cowgirl_blowjob",
            strip_description = "strip_cowgirl_blowjob", strip_ask_description = "strip_ask_cowgirl_blowjob",
            orgasm_description = "orgasm_cowgirl_blowjob",
            taboo_break_description = "taboo_break_cowgirl_blowjob",
            verb = "mouth fuck",
            opinion_tags = ["giving blowjobs", "facial", "oral creampie", "get mc off"], record_class = "Blowjobs",
            default_animation = idle_wiggle_animation, modifier_animations = {"blowjob":blowjob_bob},
            associated_taboo = "sucking_cock")

        list_of_girl_positions.append(cowgirl_blowjob)
        cowgirl_blowjob.girl_outro = "GIC_outro_cowgirl_blowjob"


label intro_cowgirl_blowjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_blowjob.redraw_scene(the_girl)
    the_girl "I want to taste you..."
    "She kisses you on the neck, then starts slowly working her way down your neck."
    "When she reaches your waist, she slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes. She leans forward and kisses the tip of your dick gingerly."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "Her mouth opens and you feel the warm wetness of her gullet envelope your cock. It feels great as she starts to bob her head up and down on it."
    return

label taboo_break_cowgirl_blowjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_blowjob.redraw_scene(the_girl)
    the_person "I know we've never done this before, but I really want to taste you..."
    "She kisses you on the neck, then starts slowly working her way down your neck."
    "When she reaches your waist, she slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes. She leans forward and kisses the tip of your dick gingerly."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "Her mouth opens and you feel the warm wetness of her gullet envelope your cock. It feels great as she starts to bob her head up and down on it."
    return

label scene_cowgirl_blowjob_1(the_girl, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] is stroking you with her mouth at an easy pace. She has her eyes closed and is just enjoying the taste."
    "She pauses for a second while she licks the tip."
    the_person "Mmm, it's so musky. It tastes good... mmmm..."
    "Her mouth opens and her silky lips descend your cock again. You try to keep yourself from bucking your hips while she controls the pace."
    return

label scene_cowgirl_blowjob_2(the_girl, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = None
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] grips your shaft and strokes while she plants small kisses all over your pelvic area. Each touch is a spark of electricity."
    "Her tongue slides across the tip for second before her mouth gently closes around your cock."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.title]'s head rocks up and down, slobbering all over your erection as she sucks on it."
    "You close your eyes and enjoy the sensation of her mouth working you over. She dances her tongue all around it until she pulls away."
    $ cowgirl_blowjob.current_modifier = None
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "You open your eyes to see her smiling at you."
    the_person "Does that feel good?"
    mc.name "It feels amazing... keep going."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] goes back down on you, stroking you quickly, using her hand to guide her lips up and down."

    return

label scene_cowgirl_blowjob_3(the_girl, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] is looking up at you, smiling with the corner of her lips and her eyes as she services you."
    mc.name "Mmm, [the_girl.title], that feels so good."
    "Moaning her name only makes her work faster. Her smile and her eye contact is enchanting."
    "She starts swirling her tongue around the tip, driving you crazy."
    "Her lips close around the tip and she suckles it a bit, her tongue still circling it."
    "She closes her eyes, clearly just enjoying the taste as she suckles a bit of pre-cum from the tip."
    return

label outro_cowgirl_blowjob(the_girl, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    if the_girl.facial_or_swallow() == "facial" or the_girl.sluttiness < 50:
        mc.name "Fuck, here I come!"
        "[the_girl.possessive_title]'s mouth pulls back with a satisfyingly wet pop. She aims it at her face."
        $ cowgirl_blowjob.current_modifier = None
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.effective_sluttiness() > 80:
            "[the_girl.title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
        elif the_girl.effective_sluttiness() > 60:
            "[the_girl.title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
        "You take a deep breath and lay back, enjoying your post-orgasm bliss. [the_girl.title] looks up at you, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")
    else:
        $ cowgirl_blowjob.current_modifier = "blowjob"
        $ cowgirl_blowjob.redraw_scene(the_girl)
        mc.name "Fuck, I'm about to cum!"
        "[the_girl.title]'s head keeps bobbing up and down, making it clear where she wants you to cum. She keeps blowing you until you tense up and start to pump your load out into her mouth."
        if the_girl.effective_sluttiness() > 70:
            "[the_girl.possessive_title] doesn't even flinch as you shoot your hot cum across the back of her throat."
            "She keeps bobbing her head up and down until you've let out every last drop, then slides back carefully and looks up with a mouth full of sperm."
        else:
            "[the_girl.possessive_title] stops when you shoot your first blast of hot cum across the back of her throat."
            "She pulls back, leaving just the tip of your cock in her mouth as you fill it up with semen. Once you've finished she slides off and looks up to show you a mouth full of sperm."

        $ the_girl.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
        $ cowgirl_blowjob.redraw_scene(the_girl)
        if the_girl.effective_sluttiness() > 80:
            $ play_swallow_sound()
            "Once you've had a good long look at your work [the_girl.title] closes her mouth and swallows loudly."
            "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        else:
            "Once you've had a good long look at your work [the_girl.title] leans over to the side and lets your cum dribble out slowly onto the ground."
            "She straightens up and wipes her lips with the back of her hand."

        $ cowgirl_blowjob.current_modifier = None
        $ cowgirl_blowjob.redraw_scene(the_girl)
        $ the_girl.call_dialogue("cum_mouth")
    return


label transition_default_cowgirl_blowjob(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_blowjob.redraw_scene(the_girl)
    the_person "I want to taste you..."
    "She kisses you on the neck, then starts slowly working her way down your neck."
    "When she reaches your waist, she slowly undoes your pants, then pulls them down and off, revealing your erection."
    the_girl "Oh [the_girl.mc_title]..."

    "[the_girl.possessive_title] looks down at your shaft for a moment, giving it a couple strokes. She leans forward and kisses the tip of your dick gingerly."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "Her mouth opens and you feel the warm wetness of her gullet envelope your cock. It feels great as she starts to bob her head up and down on it."
    return

label strip_cowgirl_blowjob(the_girl, the_clothing, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = None
    $ cowgirl_blowjob.redraw_scene(the_girl)

    "[the_girl.title] pops off your cock and looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on top of you and slides your cock inside her mouth."
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    return

label strip_ask_cowgirl_blowjob(the_girl, the_clothing, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = None
    $ cowgirl_blowjob.redraw_scene(the_girl)
    $ return_value = True

    "[the_girl.title] pops off your cock and looks up at you."
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cowgirl_blowjob.position_tag)
            "[the_girl.possessive_title] strips out of her [the_clothing.name]. Then she gets back to work sliding your cock all the way to the back of her mouth."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Yeah? Do I look sexy in it?"
                $ cowgirl_blowjob.current_modifier = "blowjob"
                "She licks the length of your shaft, then slides your tip into her mouth and starts to blow you again."
            else:
                the_girl "Does it make me look like a good little slut? Or is your cock in my mouth enough for that?"
                $ cowgirl_blowjob.current_modifier = "blowjob"
                $ cowgirl_blowjob.redraw_scene(the_girl)
                "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
            $ return_value = False

    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    return return_value

label orgasm_cowgirl_blowjob(the_girl, the_location, the_object):
    $ cowgirl_blowjob.current_modifier = "blowjob"
    $ cowgirl_blowjob.redraw_scene(the_girl)
    "[the_girl.title] pauses suddenly. You hear her whimper softly - the noise party muffled by your cock."
    "You notice she has one hand between her legs, getting herself off while she blows you."
    $ play_moan_sound()
    "She stops moving her head and a long moans vibrates around your cock. She is cumming!"
    "When she finishes she looks at you and smiles before resuming stroking your cock with her plush lips."
    return

label GIC_outro_cowgirl_blowjob(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    if the_goal == "get off" or the_goal == "hate fuck" or the_goal == "vaginal creampie" or the_goal == "anal creampie" or the_goal is None or the_goal == "get mc off":
        $ cowgirl_blowjob.call_default_outro(the_girl, the_location, the_object)
    elif the_goal == "waste cum":
        "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
        mc.name "Fuck, here I come!"
        "[the_girl.possessive_title]'s mouth suddenly pops of your cock and she strokes you with her hand. She points your cock... up at you?"
        the_girl "I'm not letting your spunk touch me!"
        "You groan but you don't have time to take over, so you just lay back and let your orgasm overtake you."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
        "Thick strands of cum erupt as you orgasm. It ropes up and out over your belly."
        "When you finish you lay back and [the_girl.title] stops stroking you. She has a naughty smile on her face."
        $ the_girl.change_stats(happiness = 2, obedience = -3)
        "She wipes her hand on your leg and starts to get up."
    elif the_goal == "facial" or the_goal == "body shot":
        "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
        mc.name "Fuck, here I come!"
        "[the_girl.possessive_title]'s mouth pulls back with a satisfyingly wet pop. She aims it at her face."
        $ cowgirl_blowjob.current_modifier = None
        $ the_girl.draw_person(position = "kneeling1")
        the_girl "Do it... I want it all over me!"
        "Her encouraging words push you over the edge. She sticks out her tongue to try and catch some as your cock erupts."
        $ the_girl.cum_on_face()
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
        $ the_girl.draw_person(position = "kneeling1")
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."


    elif the_goal == "oral creampie":
        "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
        mc.name "Fuck, here I come!"
        "[the_girl.title]'s head keeps bobbing up and down, making it clear where she wants you to cum. She keeps blowing you until you tense up and start to pump your load out into her mouth."
        if the_girl.effective_sluttiness() > 70:
            "[the_girl.possessive_title] doesn't even flinch as you shoot your hot cum across the back of her throat."
            "She keeps bobbing her head up and down until you've let out every last drop, then slides back carefully and looks up with a mouth full of sperm."
        else:
            "[the_girl.possessive_title] stops when you shoot your first blast of hot cum across the back of her throat."
            "She pulls back, leaving just the tip of your cock in her mouth as you fill it up with semen. Once you've finished she slides off and looks up to show you a mouth full of sperm."

        $ the_girl.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
        $ cowgirl_blowjob.redraw_scene(the_girl)
        if the_girl.effective_sluttiness() > 80 or the_girl == erica:
            $ play_swallow_sound()
            "Once you've had a good long look at your work [the_girl.title] closes her mouth and swallows loudly."
            "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
        else:
            "Once you've had a good long look at your work [the_girl.title] leans over to the side and lets your cum dribble out slowly onto the ground."
            "She straightens up and wipes her lips with the back of her hand."
    else:
        $ cowgirl_blowjob.call_default_outro(the_girl, the_location, the_object)
    return
