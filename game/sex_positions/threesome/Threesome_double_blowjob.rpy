#Both girls on their knees

transform threesome_double_blowjob_one_transform():
    yalign 0.6
    yanchor 0.5
    xalign 0.85
    xanchor 1.0

transform threesome_double_blowjob_two_transform():
    yalign 0.6
    yanchor 0.5
    xalign 1.0
    xanchor 1.0
    xzoom -1

init:
    python:
        threesome_double_blowjob_focus_oral= Threesome_MC_position(name = "focus_oral",
            description = "Focus on You",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 5,
            girl_two_arousal = 5,
            girl_one_source = 0,
            girl_two_source = 0,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_focus_oral",
            scenes = ["scene_threesome_double_blowjob_focus_oral_1", "scene_threesome_double_blowjob_focus_oral_2"],
            outro = "outro_threesome_double_blowjob_focus_oral",
            strip_description = "strip_threesome_double_blowjob_focus_oral",
            strip_ask_description = "strip_ask_threesome_double_blowjob_focus_oral",
            orgasm_description = "orgasm_threesome_double_blowjob_focus_oral",
            swap_description = "swap_threesome_double_blowjob_focus_oral",
            requirement = requirement_hard)

        threesome_double_blowjob_makeout = Threesome_MC_position(name = "Makeout",
            description = "Watch Girls Makeout",
            skill_tag_p1 = "Oral",
            skill_tag_p2 = "Oral",
            girl_one_arousal = 12,
            girl_two_arousal = 12,
            girl_one_source = 2,
            girl_two_source = 1,
            girl_one_energy = 15,
            girl_two_energy = 15,
            guy_arousal = 20,
            guy_source = 1,
            guy_energy = 5,
            skill_tag_guy = "Oral",
            intro = "intro_threesome_double_blowjob_makeout",
            scenes = ["scene_threesome_double_blowjob_makeout_1", "scene_threesome_double_blowjob_makeout_2"],
            outro = "outro_threesome_double_blowjob_makeout",
            strip_description = "strip_threesome_double_blowjob_makeout",
            strip_ask_description = "strip_ask_threesome_double_blowjob_makeout",
            orgasm_description = "orgasm_threesome_double_blowjob_makeout",
            swap_description = "swap_threesome_double_blowjob_makeout",
            requirement = requirement_always_true)

        threesome_double_blowjob = Threesome_Position(name = "Double Blowjob",
            slut_requirement = 60,
            position_one_tag = "blowjob",
            position_two_tag = "blowjob",
            girl_one_final_description = "On your knees too",
            girl_two_final_description = "On your knees too",
            requires_location = "Kneel",
            requirements = requirement_always_true,
            verb = "throat",
            p1_transform = threesome_double_blowjob_one_transform,
            p2_transform = threesome_double_blowjob_two_transform,
            can_swap = True,)

        threesome_double_blowjob.mc_position = [threesome_double_blowjob_focus_oral,threesome_double_blowjob_makeout]
        list_of_threesomes.append(threesome_double_blowjob)

label intro_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    "As the girls get on their knees, you run your hands through along their faces."
    mc.name "I want you two to focus on me for a bit."
    if the_girl_1.get_opinion_score("giving blowjobs") > 0:
        the_girl_1 "Mmm, you want to feel us slobbering all over your cock, [the_girl_1.mc_title]?"
    else:
        the_girl_1 "I don't usually give blowjobs, but with [the_girl_2.fname] here it should be fun!"
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        the_girl_1 "This is gonna be great, I can lick your balls while she's blowing you, [the_girl_2.mc_title]!"
    else:
        the_girl_2 "I wonder how long you can last with two girls on their knees for you, [the_girl_2.mc_title]."
    $ the_girl_1.break_taboo("sucking_cock")
    $ the_girl_2.break_taboo("sucking_cock")
    "[the_girl_1.possessive_title] and [the_girl_2.possessive_title] get to work servicing your cock."
    return

label scene_threesome_double_blowjob_focus_oral_1(the_girl_1, the_girl_2, the_location, the_object):
    #Girl 1 services you
    #TODO scene modifier for blowing
    "[the_girl_1.title] opens up and begins to blow you. Her tongue works circles around your head as she gives you shallow strokes."
    "[the_girl_2.title] moves her head lower and gently suckles on your ballsack. She gently sucks one into her mouth, then moves over to the other."
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        "You feel a pleasurable vibration in your testicles as [the_girl_2.possessive_title] starts to hum a bit."
    "The sensations of having two mouths pleasuring you is intense."
    mc.name "Damn girls, that feels amazing!"
    "[the_girl_1.title] comes up for air, then runs her mouth along the side of your cock. [the_girl_2.title] notices and moves her mouth to the opposite side of your cock."
    "They slowly stroke your cock together, mouths on opposite sides of your aching hard on."
    return

label scene_threesome_double_blowjob_focus_oral_2(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_2.title] opens up and takes a turn focusing on your hard on. She takes the base in her hand and gives you long, deep strokes."
    $ scene_manager.update_actor(the_girl_1, position = "kissing")
    "[the_girl_1.title] takes a moment and stands up, wrapping her hands around you. She begins kissing your neck and along your jawline."
    "[the_girl_1.possessive_title]'s lips on your neck, her body against yours, and [the_girl_2.possessive_title]'s mouth on your cock. This must be heaven."
    "[the_girl_1.title] slowly kisses lower on your neck, moving down your collarbone. She continues to descend, licking and nipping at your chest and nipples."
    $ scene_manager.update_actor(the_girl_1, position = "blowjob")
    "She continues descending, kissing down your belly until she is back on her knees. When [the_girl_2.title] comes off she takes you in her hand and gives you a few strokes."
    return

label outro_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    #Since the girls are pretty much in control, they determine where you cum.
    "Soon, the mouths of the beautiful girls on their knees in front of you drive you past the point of no return. Your orgasm is swiftly approaching."
    mc.name "Oh god, I'm gonna cum!"
    if the_girl_1.get_opinion_score("drinking cum") > 1:
        call threesome_double_blowjob_girls_cum_drink(the_girl_1, the_girl_2, the_location, the_object) from _call_threesome_double_blowjob_girls_cum_drink_1
        return
    elif the_girl_2.get_opinion_score("drinking cum") > 0:
        call threesome_double_blowjob_girls_cum_drink(the_girl_2, the_girl_1, the_location, the_object) from _call_threesome_double_blowjob_girls_cum_drink_2
        return
    "You take your cock and begin to stroke it. Both girls look up at you as you get ready to finish."
    "Your orgasm hits and you begin spraying down their beautiful faces with your seed."
    $ the_girl_1.cum_on_face()
    $ scene_manager.draw_scene()
    "Your first couple of spurts hit [the_girl_1.title] in the face. She gives a sigh when she feels your warm seed."
    "You point your cock at [the_girl_2.title] and fire another couple of rounds."
    $ the_girl_2.cum_on_face()
    $ scene_manager.draw_scene()
    "When you finish, both of the girl's faces are covered in your sticky cum."
    return

label strip_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    "This scene in progress"

label orgasm_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        $ play_moan_sound()
        "You can feel the pace of the double blowjob pick up a bit as both girls begin moaning at each other."
        "When you look down, you can see that each girl has a hand along the other's crotch... have they been doing that the whole time?"
        $ the_girl_1.have_orgasm()
        $ the_girl_2.have_orgasm()
        "They both orgasm, almost in unison. As they do they kiss and grope each other, momentarily ignoring your erection."
        "As they start to wind down, you turn their attention back to you."
        mc.name "That was hot, but don't forget about me."
        return

    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        "You can feel [the_girl_1.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_2.title]'s hand petting her crotch."
        $ the_girl_1.have_orgasm()
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_1 "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_2.title] takes over for her while she recovers."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        "You can feel [the_girl_2.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_1.title]'s hand petting her crotch."
        $ the_girl_2.have_orgasm()
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_2 "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_1.title] takes over for her while she recovers."
        return
    return

label swap_threesome_double_blowjob_focus_oral(the_girl_1, the_girl_2, the_location, the_object):
    "You decide to change things up a bit. You run your hands behind their heads, pulling them toward your cock."
    mc.name "I want you two to focus on me for a bit."
    if the_girl_1.get_opinion_score("giving blowjobs") > 0:
        the_girl_1 "Mmm, you want to feel us slobbering all over your cock, [the_girl_1.mc_title]?"
    else:
        the_girl_1 "I don't usually give blowjobs, but with [the_girl_2.name] here it should be fun!"
    if the_girl_2.get_opinion_score("giving blowjobs") > 0:
        the_girl_2 "This is gonna be great, I can lick your balls while she's blowing you, [the_girl_2.mc_title]!"
    else:
        the_girl_2 "I wonder how long you can last with two girls on their knees for you, [the_girl_2.mc_title]."
    "[the_girl_1.possessive_title] and [the_girl_2.possessive_title] get to work servicing your cock."
    return

#Makeout. In this scene 1, the girls makeout while on their knees in front of you, touching and caressing each other.
#In scene 2, girls make out around MC's cock

label intro_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    "As the girls get on their knees, you run your hands over their faces, pushing them closer to each other."
    mc.name "Why don't you two makeout for a bit. I want to watch."
    "[the_girl_1.title] and [the_girl_2.title] turn to each other and begin to kiss. Their hands begin to explore each other's breasts."
    the_girl_1 "Mmmm, I love your tits, [the_girl_2.name]!"
    the_girl_2 "Yours are nice too... I kinda want to suck on them..."
    "The girls are heating up as they start to make out with each other."
    return

label scene_threesome_double_blowjob_makeout_1(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_2.vagina_visible:
        "As they are making out, you notice [the_girl_1.possessive_title] has her hand between [the_girl_2.title]'s legs, petting her pussy."
    else:
        the_girl_1 "Mmm... I want to touch you. Let's get these out of the way!"
        $ scene_manager.strip_to_vagina(person = the_girl_2, prefer_half_off = True)
        "Now [the_girl_1.title] immediately begins to fondle [the_girl_2.possessive_title]'s pussy."
    if the_girl_1.vagina_visible:
        "As she gets fingered, you notice that [the_girl_2.title] reaches down and begins to return the favor, fondling [the_girl_1.title]."
    else:
        the_girl_2 "Mmm, I want to touch you too! Let's get these off of you..."
        $ scene_manager.strip_to_vagina(person = the_girl_1, prefer_half_off = True)
        "Once her pussy is bare, the girls waste no time and begin to pet each other."
    "[the_girl_1.title] and [the_girl_2.title] begin moaning into each others mouths as they make out, while simultaneously fingering each other."
    "You start to stroke yourself, watching the impressive show in front of you, but soon feel another hand on yours."
    if mc.recently_orgasmed:
        "[the_girl_1.title]'s hand bumps yours away, and she begins to stroke your semi-erect cock."
    else:
        "[the_girl_1.title]'s hand bumps yours away, and she begins to stroke your hard cock."
    "The girls make out for a while, enjoying the taste of each other's lips."
    return

label scene_threesome_double_blowjob_makeout_2(the_girl_1, the_girl_2, the_location, the_object):
    "You decide to give the girls something additional to kiss as they make out with each other."
    "You move forward and move your hips right next to their faces, your cock resting on [the_girl_1.title]'s cheek."
    if mc.recently_orgasmed:
        "She gets the hint. The girls shift over, so they are making out, but the tip of your cock is also in the side of each of their mouths."
        "Watching the girls make out around your cock is extremely arousing, causing you to get hard even though you just came a few moments ago."
        $ mc.change_arousal(5)
        $ mc.recently_orgasmed = False
    else:
        "The girls get the hint. They shift over, so they are making out, but the tip of your cock is also in the side of each of their mouths."
    "Two tongues duel around the tip of your cock. The pleasure is exquisite, their lovely lips smacking and slurping at each other and you."
    "You grab the back of their heads for a moment, then thrust your hips forward. Their tongues and lips caress the side of your dick as it slides between them."
    "When you pull back, you step back. The girls pout for a second when your cock is no longer in reach but quickly resume touching and kissing each other."
    return

label outro_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    "Watching the girls, on their knees in front of you, kiss and please each other has you hot and bothered. You find yourself stroking yourself past the point of no return."
    mc.name "Oh god, I'm gonna cum!"
    if the_girl_1.get_opinion_score("drinking cum") > 1:
        call threesome_double_blowjob_girls_cum_drink(the_girl_1, the_girl_2, the_location, the_object) from _call_threesome_double_blowjob_girls_cum_drink_3
        return
    elif the_girl_2.get_opinion_score("drinking cum") > 0:
        call threesome_double_blowjob_girls_cum_drink(the_girl_2, the_girl_1, the_location, the_object) from _call_threesome_double_blowjob_girls_cum_drink_4
        return
    "You take your cock and begin to stroke it. Both girls look up at you as you get ready to finish."
    "Your orgasm hits and you begin spraying down their beautiful faces with your seed."
    $ the_girl_1.cum_on_face()
    $ scene_manager.draw_scene()
    "Your first couple of spurts hit [the_girl_1.title] in the face. She gives a sigh when she feels your warm seed."
    "You point your cock at [the_girl_2.title] and fire another couple of rounds."
    $ the_girl_2.cum_on_face()
    $ scene_manager.draw_scene()
    "When you finish, both of the girl's faces are covered in your sticky cum."
    return

label strip_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    "This scene in progress"

label strip_ask_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    "This scene in progress"

label orgasm_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    if the_girl_1.arousal_perc > 100 and the_girl_2.arousal_perc > 100:  #Both girls orgasm#
        $ play_moan_sound()
        "You can feel the pace and urgency of the girls moaning increase as they kiss each other."
        "When you look down, you can see that each girl has a hand along the other's crotch."
        $ the_girl_1.have_orgasm()
        $ the_girl_2.have_orgasm()
        "They both orgasm, almost in unison."
        "As they start to wind down, they continue kissing and caressing each other."
        return

    elif the_girl_1.arousal_perc > 100:   #Just girl 1 orgasms
        $ play_moan_sound()
        "You can feel [the_girl_1.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_2.title]'s hand petting her crotch."
        $ the_girl_1.have_orgasm()
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_1 "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_2.title] takes over for her while she recovers."
        return

    elif the_girl_2.arousal_perc > 100:   #Just girl 2 orgasms
        $ play_moan_sound()
        "You can feel [the_girl_2.title] moaning around your cock with increasing intensity. When you look down, you notice [the_girl_1.title]'s hand petting her crotch."
        $ the_girl_2.have_orgasm()
        "An orgasm hits her. She takes your cock into her mouth and moans around it loudly. The vibrations feel amazing."
        "When she finishes, she briefly comes up for air."
        the_girl_2 "Oh fuck that was good. I need a second."
        "She sits back and [the_girl_1.title] takes over for her while she recovers."
        return
    return

label swap_threesome_double_blowjob_makeout(the_girl_1, the_girl_2, the_location, the_object):
    mc.name "Why don't you two makeout for a bit. I want to watch."
    "[the_girl_1.title] and [the_girl_2.title] turn to each other and begin to kiss. Their hands begin to explore each other's breasts."
    the_girl_1 "Mmmm, I love your tits, [the_girl_2.fname]!"
    the_girl_2 "Yours are nice too... I kinda want to suck on them..."
    "The girls are heating up as they start to make out with each other."
    return

label threesome_double_blowjob_girls_cum_drink(the_girl_1, the_girl_2, the_location, the_object):
    "[the_girl_1.possessive_title] immediately grabs your cock, opens up and takes your tip in her mouth."
    "[the_girl_2.title] moves down and strokes the side of your cock as you begin to ejaculate into [the_girl_1.title]'s eager mouth."
    $ the_girl_1.cum_in_mouth()
    $ scene_manager.draw_scene()
    $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl_1)
    "You dump wave after wave of cum into [the_girl_1.title]'s mouth."
    if the_girl_2.get_opinion_score("drinking cum") > 0:
        "As you finish, you slowly pull back. Some of your cum slowly dribbles out of her mouth."
        the_girl_2 "Hey girl, save some for me!"
        "[the_girl_2.title] leans towards her blowjob partner and begins kissing and licking your cum off her face."
        "Soon, they are full on making out, swapping your cum between their mouths."
        $ the_girl_2.cum_in_mouth()
        $ scene_manager.draw_scene()
        "When they finish, they look up at you, remnants of your cum still visible at the corner of their mouths."
    else:
        "You slowly pull back. Some of your cum slowly dribbles out of her mouth."
    return
