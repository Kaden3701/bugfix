init:
    python:
        cowgirl_cunnilingus = Position(name = "Cowgirl Cunnilingus", slut_requirement = 40, slut_cap = 80, requires_hard = False, requires_large_tits = False,
            position_tag = "kneeling1", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Oral",
            girl_arousal = 15, girl_energy = 3,
            guy_arousal = 3, guy_energy = 15,
            connections = [],
            intro = "intro_cowgirl_cunnilingus",
            scenes = ["scene_cowgirl_cunnilingus_1","scene_cowgirl_cunnilingus_2", "scene_cowgirl_cunnilingus_3"],
            outro = "outro_cowgirl_cunnilingus",
            transition_default = "transition_default_cowgirl_cunnilingus",
            strip_description = "strip_cowgirl_cunnilingus", strip_ask_description = "strip_ask_cowgirl_cunnilingus",
            orgasm_description = "orgasm_cowgirl_cunnilingus",
            taboo_break_description = "taboo_break_cowgirl_cunnilingus",
            verb = "lick",
            opinion_tags = ["getting head", "taking control", "get off"], record_class = "Cunnilingus",
            default_animation = missionary_bob,
            associated_taboo = "licking_pussy")

        list_of_girl_positions.append(cowgirl_cunnilingus)

        cowgirl_cunnilingus.girl_outro = "GIC_outro_cowgirl_cunnilingus"

# init 1:
#     python:
#         cunnilingus.link_positions(other, "transition_label") #If there are transitions they go here

label intro_cowgirl_cunnilingus(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_cunnilingus.redraw_scene(the_girl) #Draw her sitting down.
    the_girl "I want you to kiss me for a little bit..."
    "She slowly climbs up your body until her cunt is inches from your face."
    $ play_moan_sound()
    "You lean forward and run your tongue along her slit. She moans softly as soon as you make contact."
    the_girl "Oh [the_girl.mc_title]..."
    return

label taboo_break_cowgirl_cunnilingus(the_girl, the_location, the_object):  #because this is a girl in charge position only it makes sense to bypass normal taboo break dialogue which usually assumes MC is in charge
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_cunnilingus.redraw_scene(the_girl)
    mc.name "What are you doing?"
    the_girl "I know we've never done this but... I want you to kiss me."
    mc.name "That hardly seems like a big deal..."
    the_girl "Not on my lips..."
    "She slowly climbs up your body until her cunt is inches from your face."
    "You slide forward and bring your head even closer. [the_girl.possessive_title] takes a sharp breath and turns her head to the side."
    "You bring one hand up to her [the_girl.pubes_description] pussy and spread it open to reveal the tender pink inside."
    "With her thighs pressed against your shoulders you can feel every tremble and shiver of anticipation in her body."
    the_girl "Come on, do it!"
    "You run your tongue along the length of her slit, tasting her sweet juices."
    the_girl "Oh my god!"
    return

label scene_cowgirl_cunnilingus_1(the_girl, the_location, the_object):
    if the_girl.get_sex_goal() == "hate fuck":
        "[the_girl.title] is pushing herself down against your face, riding you roughly."
        "You can feel her hands run through your hair a bit. Then she grabs your hair and pulls. Pain shoots down your head."
        the_girl "That's it, lick my cunt [the_girl.mc_title]."
        "You swing your hand around hard and spank her ass. Her hips involuntarily thrust against you when you strike her."
        $ the_girl.call_dialogue("sex_responses_oral")
        $ the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
    else:
        "You lick at [the_girl.possessive_title]'s delicate pussy, spreading her lips and sending your tongue inside."
        "She shivers with each touch, obviously enjoying the feeling."
        if the_girl.arousal_perc > 40:
            "Her pussy is dripping wet, filling your mouth with the taste of her juices."
        $ the_girl.call_dialogue("sex_responses_oral")
    return

label scene_cowgirl_cunnilingus_2(the_girl, the_location, the_object):
    "You flick your tongue over [the_girl.possessive_title]'s clit. She gasps and grabs at your shoulders."
    $ the_girl.call_dialogue("sex_responses_oral")
    "You tease the sensitive nub with your tongue, then suck on it gently."
    if the_girl.arousal_perc > 80:
        $ play_moan_sound()
        "Her moans are getting desperate and her hips are bucking against you as you stimulate her."
    "She runs her fingers through your hair and sighs, reclining on the [the_object.name]."
    return

label scene_cowgirl_cunnilingus_3(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()

    the_girl "Just keep licking... licking... licking..."
    if the_girl.arousal_perc > 70:
        "[the_girl.possessive_title]'s juices are flowing freely from her slit. You lap them up before circling your tongue around her clit a few times."
    elif the_girl.arousal_perc > 50:
        "[the_girl.possessive_title]'s pussy is wet. You lick it carefully."
    else:
        "[the_girl.possessive_title]'s pussy is still getting wet. You lick it slowly, giving her time to warm up."

    if the_goal == "hate fuck" or the_goal == "waste cum":
        "[the_girl.title] shifts her legs slightly, making sure that your arms are pinned down by her shins."
        if mc.arousal_perc >= 10:
            "She looks behind her and sees your erect cock."
            the_girl "This isn't for your benefit, [the_girl.mc_title]."
            "She reaches behind her and starts to manhandle your balls, pulling and flicking them. Your erection soon subsides."
            $ mc.reset_arousal()
            the_girl "That's better. Now focus!"
            "She gently slaps one of your cheeks."
    else:
        if mc.recently_orgasmed:
            "[the_girl.title] looks back at your softened cock. She reaches back and gives it a couple strokes."
            the_girl "Mmm, sex is more fun when you're turned on..."
            $ mc.arousal += 5
        else:
            "[the_girl.title] looks back at your cock. She reaches back and gives it a couple strokes."
            the_girl "Mmm, I love how hard it is for me!"

    return

label outro_cowgirl_cunnilingus(the_girl, the_location, the_object): #With low arousal gain this is unlikely to come up much
    "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
    "You touch yourself, stroking your hard cock between your legs while you pleasure her."
    "Finally you've gone too far, pushing yourself to climax."
    $ ClimaxController.manual_clarity_release(climax_type = "masturbation", the_person = the_girl)
    "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto your stomach behind [the_girl.title]."
    the_girl "Oh my god... That's so hot!"
    return


label transition_default_cowgirl_cunnilingus(the_girl, the_location, the_object):
    "[the_girl.title] motions to the [the_object.name]. When you sit down she pushes you onto your back."
    $ cowgirl_cunnilingus.redraw_scene(the_girl) #Draw her sitting down.
    the_girl "I want you to kiss me for a little bit..."
    "She slowly climbs up your body until her cunt is inches from your face."
    $ play_moan_sound()
    "You lean forward and run your tongue along her slit. She moans softly as soon as you make contact."
    the_girl "Oh [the_girl.mc_title]!"
    return

label strip_cowgirl_cunnilingus(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = cowgirl_cunnilingus.position_tag)
    "[the_girl.possessive_title] strips off her [the_clothing.name] while you're eating her out, throwing it to the side."
    return

label strip_ask_cowgirl_cunnilingus(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'm like to take off my [the_clothing.name] if you don't mind."
    menu:
        "Let her strip":
            "You look up from between her legs and nod."
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = cowgirl_cunnilingus.position_tag)
            "She strips out of her [the_clothing.name] and throws it to the side while you move back in and lick at her cunt."
            return True

        "Leave it on":
            "You look up from between her legs and shake your head."
            mc.name "No, I like how you look with it on."
            the_girl "Yeah? Do I look sexy in it? Mmmm..."
            return False

label orgasm_cowgirl_cunnilingus(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You notice [the_girl.possessive_title]'s moans becoming louder, and her legs twitching more noticeably on either side of you."
    "You speed up your efforts, doing your best to drive her towards her orgasm. She moans and begins to writhe under your skilled tongue."
    $ the_girl.call_dialogue("climax_responses_oral")
    "All at once the tension in her body is unleashed in a series of violent tremors. Her legs wrap around you for a moment, pulling you against her."
    "The moment passes and she relaxes. For a moment all she can do is look down at you and pant."
    return

label GIC_outro_cowgirl_cunnilingus(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal == "hate fuck" or the_goal == "waste cum":
        $ play_moan_sound()
        "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
        "You touch yourself, stroking your hard cock between your legs while you pleasure her."
        "Finally you've gone too far, pushing yourself to climax."
        $ ClimaxController.manual_clarity_release(climax_type = "masturbation", the_person = the_girl)
        "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto your stomach behind [the_girl.title]."
        the_girl "Wow. Just from licking me? What a pathetic waste of cum."
        "It makes a mess, but you finish cumming."
    else:
        $ cowgirl_cunnilingus.call_default_outro(the_girl, the_location, the_object)
    return
