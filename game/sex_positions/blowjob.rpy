﻿init:
    python:
        blowjob = Position(name = "Blowjob", slut_requirement = 40, slut_cap = 60, requires_hard = False, requires_large_tits = False,
            position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
            girl_arousal = 3, girl_energy = 13,
            guy_arousal = 16, guy_energy = 5,
            connections = [],
            intro = "intro_blowjob",
            scenes = ["scene_blowjob_1","scene_blowjob_2", "scene_blowjob_3"],
            outro = "outro_blowjob",
            transition_default = "transition_default_blowjob",
            strip_description = "strip_blowjob", strip_ask_description = "strip_ask_blowjob",
            orgasm_description = "orgasm_blowjob",
            taboo_break_description = "taboo_break_blowjob",
            verb = "mouth fuck",
            opinion_tags = ["giving blowjobs"], record_class = "Blowjobs",
            default_animation = idle_wiggle_animation, modifier_animations = {"blowjob":blowjob_bob},
            associated_taboo = "sucking_cock")

        list_of_positions.append(blowjob)

init 1:
    python:
        blowjob.link_positions(deepthroat,"transition_blowjob_deepthroat")

label intro_blowjob(the_girl, the_location, the_object):
    "You unzip your pants and pull your underwear down far enough to let your hard cock out."
    mc.name "How about you take care of this for me?"
    if the_girl.has_cum_fetish or the_girl.get_opinion_score("giving blowjobs") > 1:
        $ blowjob.redraw_scene(the_girl)
        "Without hesitation, [the_girl.possessive_title] drops to her knees in front of you. She runs her hands along your hips, then leans forward and slides her lips over the tip of your dick."
    else:
        "[the_girl.possessive_title] grabs your cock with one hand."
        the_girl "Sure thing but what do you want?"
        mc.name "How about a blowjob?"
        if the_girl.effective_sluttiness() > 35 or the_girl.get_opinion_score("giving blowjobs") > 0:
            "[the_girl.possessive_title] looks down at your shaft, thinks about it for a moment, then drops to her knees in front of you. She leans forward and slides her lips over the tip of your dick."
        else:
            "[the_girl.possessive_title] looks down at your shaft for a moment, thinks about it for a moment, then drops to her knees in front of you. She leans forward and kisses the tip of your dick gingerly."
        $ blowjob.redraw_scene(the_girl)

    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    return

label taboo_break_blowjob(the_girl, the_location, the_object):
    $ the_girl.call_dialogue(blowjob.associated_taboo+"_taboo_break") #Personality dialogue includes all associated "convince me" dialogue
    if the_girl.effective_sluttiness(blowjob.associated_taboo) > blowjob.slut_cap:
        #She's eager to try this
        $ the_girl.draw_person(position = "kneeling1")
        "[the_girl.possessive_title] kneels down in front of you, eyes locked on your hard cock."
        $ blowjob.current_modifier = None
        $ blowjob.redraw_scene(the_girl)
        "She leans in, turning her head to the side to run her tongue down the bottom of your shaft."
        "She licks your balls briefly, then works back up to the tip and slides it past her lips."
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She wastes no time picking up speed, happily bobbing her head up and down over your sensitive tip."

    else:
        $ the_girl.draw_person(position = "kneeling1")
        "[the_girl.possessive_title] hesitantly gets onto her knees, eyes locked on your hard cock."
        "She gently holds onto your shaft with one hand and brings the tip closer to her lips."
        "She looks up at you just before the moment of truth, locking eyes as she opens her lips and slides the tip of your cock past them."
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)

        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She moves slowly at first, gently working her head up and down over your sensitive tip."
    return

label scene_blowjob_1(the_girl, the_location, the_object):
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    if the_girl.sex_skills["Oral"] < 2: #Inexperienced.
        "You rest your hand on [the_girl.title]'s head as she bobs her head back and forth. She struggles to take you very deep, and focuses on licking and sucking your tip instead."
        call blowjob_comment(the_girl, the_location, the_object) from call_blowjob_comment_scene_blowjob_1_1
        menu:
            "Encourage her to go deeper":
                mc.name "Come on, you'll never get better if you don't try and take it deeper."
                $ play_gag_sound()
                "[the_girl.possessive_title] hesitates for a moment, then tries to slide you to the back of her throat. She manages to get half your shaft into her mouth before she pauses, then gags and pulls off."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                if the_girl.get_opinion_score("giving blowjobs") < 0:
                    $ the_girl.discover_opinion("giving blowjobs")
                    the_girl "Ugh... I hate that feeling."
                    mc.name "Give it time, you'll get used to it."
                else:
                    the_girl "Ah... Ah..."
                    mc.name "Better. Now keep it up."

                $ blowjob.current_modifier = "blowjob"
                $ blowjob.redraw_scene(the_girl)
                "You put a little pressure on the back of her head. She takes the hint and slips you back into her soft mouth."

            "Tell her to use her hand too":
                mc.name "There's plenty of shaft still left. Stroke me off a little."
                if the_girl.sex_skills["Foreplay"] < 2:
                    "[the_girl.possessive_title] wraps her right hand around the base of your cock. She tries jerk off the base of your cock while licking at the tip, but can't quite coordinate the movements."
                    "After trying for a few seconds she takes a break and sighs."
                    the_girl "Ugh, I'm just so bad at this..."
                    mc.name "Keep trying, you'll get better. Don't worry, I promise I'm having a good time."
                    "You press the tip of your cock against her lips and she lets you slide it back in. She resumes sucking and licking the tip, without trying to stroke you off at the same time."
                else:
                    "[the_girl.possessive_title] wraps her right hand around the base of your cock and starts to slide it back and forth in time with her blowjob."
                    if (the_girl.get_opinion_score("cum facials") > 0 or the_girl.get_opinion_score("being covered in cum") > 0 ) and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and looks up at you."
                        the_girl "Mmm, look at this. Don't you just want to cum all over my face?"
                        "She strokes you off faster and holds your cock right against her face."
                        the_girl "I want you to cum on me. I want you to pump your load right onto my face!"
                        $ the_girl.discover_opinion("cum facials")
                        $ the_girl.discover_opinion("being covered in cum")
                        "[the_girl.title] trembles slightly and slides your cock back into her mouth, sucking at it with renewed vigor."
                    elif the_girl.get_opinion_score("drinking cum") > 0 and the_girl.sluttiness > 40:
                        "After a moment she takes her lips off your dick and looks up at you."
                        the_girl "Come on, I want you to unload right in my mouth [the_girl.mc_title]."
                        "She pops back onto your cock, sucking at the tip eagerly before letting it slip out again."
                        the_girl "I want you to fire it right down my throat. Ugh, I want it so badly!"
                        "[the_girl.title] slides you back into her mouth and sucks your dick with renewed vigor."
                    else:
                        "You relax for a little while while [the_girl.possessive_title] services your cock, stroking your shaft and sucking gently on your tip."
                        "You're pleasantly surprised when she reaches her other hand up and starts to gently play with your balls. You run your fingers through her hair and sigh contentedly."


    else: #competent at blowjobs.
        "[the_girl.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
        call blowjob_comment(the_girl, the_location, the_object) from call_blowjob_comment_scene_blowjob_1_2
        menu:
            "Talk dirty to her":
                mc.name "That feels great [the_girl.title]. You look good on your knees, sucking my cock."
                if the_girl.get_opinion_score("giving blowjobs") > 0:
                    "She slides your cock out of her mouth to speak."
                    the_girl "Mmm, and you feel so good in my mouth. You're so big I can barely manage."
                    $ the_girl.discover_opinion("giving blowjobs")
                    "She rubs her cheek against your wet shaft."
                    if the_girl.get_opinion_score("drinking cum") > 0:
                        the_girl "Now just relax and enjoy. I want you to cum right into my mouth, okay?"
                        $ the_girl.discover_opinion("drinking cum")
                    else:
                        the_girl "Now just relax and enjoy, I'll take care of everything."
                    "She slips you back into her mouth and resumes blowing you."

                elif the_girl.get_opinion_score("giving blowjobs") < 0:
                    "She pulls off of your cock to speak."
                    the_girl "How about we try some other position? My knees are killing me, and I keep feeling like I'm going to gag on this."
                    $ the_girl.discover_opinion("giving blowjobs")
                    mc.name "Maybe in a little bit. Come on, back to work."
                    "[the_girl.possessive_title] sighs and slides your dick back into her mouth, settling back into the steady rhythm of her blowjob."

                else:
                    "[the_girl.possessive_title] stays focused on the task at hand. You run a hand through her hair, then settle the hand on the back of her head to encourage her to keep up the pace."

            "Stay quiet":
                "You rest your hand on her head, guiding her as she sucks you off."
                if the_girl.get_opinion_score("masturbating") > 0:
                    if the_girl.vagina_available:
                        "[the_girl.title] puts a hand between her legs and starts to touch herself while she blows you."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
                        $ the_girl.discover_opinion("masturbating")
                        if the_girl.arousal_perc > 60:
                            "Her moans are muffled by your cock when she slides a finger into her pussy and starts to finger herself."

                        else:
                            "She rubs her clit with her middle finger, making little circles around the sensitive nub."


                    else:
                        if the_girl.arousal_perc > 60:
                            "[the_girl.title] puts a hand between her legs and eagerly rubs at her crotch through her clothing."
                        else:
                            "[the_girl.title] puts a hand between her legs and rubs at her crotch absentmindedly."

                else:
                    "[the_girl.title] keeps up a steady pace, bobbing her head back and forth and running your cock in and out of her soft mouth."
                    if the_girl.get_opinion_score("giving blowjobs") < 0:
                        "After a minute she pulls off and wipes at her lips."
                        the_girl "Are you almost done? My jaw is getting sore."
                        $ the_girl.discover_opinion("giving blowjobs")
                        mc.name "Keep going, I'll finish soon."
                        "She sighs and slips you back into her mouth."

    return

label scene_blowjob_2(the_girl, the_location, the_object):
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)

    "[the_girl.title] pulls your cock out of her mouth and leans in even closer. She runs her tongue along the bottom of your shaft, pausing at the top to kiss the tip a few times."
    call blowjob_comment(the_girl, the_location, the_object) from call_blowjob_comment_scene_blowjob_2_1
    the_girl "Does that feel good?"
    menu:
        "Encourage her":
            mc.name "Yeah, it does. Keep licking it for me."
            "[the_girl.possessive_title] smiles and keeps working her tongue over your cock. She licks it bottom to top, then sucks on the tip, then licks it from the top back to the bottom."
            if the_girl.get_opinion_score("taking control") > 0:
                the_girl "Mmm, I love this so much. I love being in control of your pleasure. Being able to..."
                "She runs her tongue along the underside of your cock, licking the sensitive spot just below the tip. You moan in response."
                $ the_girl.discover_opinion("taking control")
                $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))
                the_girl "Make you moan, just like that."
            else:
                the_girl "Just relax and enjoy, I'll take care of you as best I can."
                if the_girl.sex_skills["Oral"] < 2:
                    "[the_girl.title] keeps on licking your cock. You enjoy the feeling for a while, but you're glad when she finally opens her mouth and starts to blow you again."
                else:
                    "[the_girl.title] keeps on licking your cock. Her tongue hits all the right places and sends shivers up your spine."
                    "You're almost disappointed when she opens her mouth wide and starts to blow you again."
            $ blowjob.current_modifier = "blowjob"
            $ blowjob.redraw_scene(the_girl)


        "Insult her":
            mc.name "Of course it does, you filthy little cocksucker."
            if the_girl.get_opinion_score("being submissive") > 0:
                "You grab hold of your dick with one hand and bounce it against [the_girl.possessive_title]'s face. She gasps loudly when you do."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                mc.name "Do you like having a wet cock slapped against your face? I bet you're a total slut for it, right?"
                $ play_moan_sound()
                "You do it again. Your cock makes a wet thwack against her face. This time she moans."
                the_girl "Yes..."
                "She responds softly, as if she's suddenly distracted."
                mc.name "I didn't hear you."
                $ play_moan_sound()
                "Thwack. You flop your cock over her face again. She moans again."
                the_girl "Yes... Yes I like having your cock all over my face!"
                "She opens her mouth wide and sticks her tongue out. You bounce your cock against her soft tongue, then against her cheeks and onto her forehead. She moans with each hit."
                $ the_girl.change_obedience(the_girl.get_opinion_score("being submissive"))
                mc.name "Good girl. Now be a good slut for me and keep sucking me off."
                "You present your cock to [the_girl.possessive_title]. She nods and slips her lips around it."

            elif the_girl.get_opinion_score("being submissive") < 0:
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                "[the_girl.title] leans away from you."
                the_girl "Ugh, could you not say stuff like that, please? It really kills the mood."
                "She sighs and slips your cock back into her mouth."

            else:
                "You grab hold of your dick with one hand and bounce it against [the_girl.title]'s face. She gasps in surprise."
                if the_girl.sex_skills["Foreplay"] > 3:
                    the_girl "Filthy cocksucker, huh? Is that what you want me to be?"
                    "She leans forward and rubs her cheek against your wet cock, nuzzling it like a cat."
                    the_girl "Okay then, I'll be your filthy little cocksucker [the_girl.mc_title]. I'll take this monster cock nice and deep..."
                    "She kisses the side of it, then sticks her tongue out and runs it along the entire length of your shaft."
                    the_girl "I'll gag on it until you're ready to cum, if that's what you want me to do."
                    the_girl "Because deep down I'm just a cock hungry slut, begging to be used."
                    "Hearing [the_girl.title] gets you even more aroused. Your dick flexes in response and bumps against her face."
                    the_girl "Mmm, I thought so. Everyone likes a bit of dirty talk..."
                    "She opens her mouth and slides you inside."
                else:
                    the_girl "Hey, I'm..."
                    "You interrupt her and flop your cock onto her face again."
                    the_girl "Ugh, fine. Go to town."
                    "She closes her eyes and points her face up. You enjoy a few moments rubbing your cock all over [the_girl.possessive_title]'s face."
                    the_girl "Happy now?"
                    mc.name "Very."
                    "She opens her mouth back up and slides you inside."

    return

label scene_blowjob_3(the_girl, the_location, the_object):
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    # Outline: If she likes blowjobs, is neutral, or doesn't like them. Give her a chance to show it.

    if the_girl.opinion_score_giving_blowjobs() > 0:    #She enjoys it
        "[the_girl.possessive_title] is bobbing her mouth up and down on your cock. With each stroke you can feel little moans and hums."
        "She appears to be really enjoying sucking you off."
        $ blowjob.current_modifier = None
        $ blowjob.redraw_scene(the_girl)
        "She pulls off for a moment, then licks your erection from base to tip, then goes down and even sucks each of your balls in her mouth, one at a time."
        mc.name "Damn, I don't think you missed a spot. That feels amazing."
        "[the_girl.title] looks up at you, making eye contact as she leans forward again, running her tongue along from base to tip slowly, savoring the taste."
        "When she reaches the tip, she opens her mouth and her lips begin to descend, surrounding your dick with her soft lips."
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        "She varies the suction with each stroke, leaving you to just watch and enjoy."
    else:
        "[the_girl.possessive_title] is bobbing her mouth up and down on your cock."
        "You give her an appreciative moan, but she just looks up at you, then rolls her eyes."
        $ blowjob.current_modifier = None
        $ blowjob.redraw_scene(the_girl)
        the_girl "Are you almost done? This is starting to hurt my jaw..."
        if mc.arousal > 80:
            mc.name "Fuck yeah I'm almost done, now get back to it."
            "You put your hand on the back of her head, encouraging her to get back to work."
            "Knowing you are almost done, she easily complies."
        if mc.arousal > 50:
            mc.name "It feels good, I admit, but you still have your work cut out for you. Now get back to it."
            "You put your hand on the back of her head, encouraging her to get back to work."
            the_girl "Ugh... seriously? I guess..."
            "She resists for a moment, but then relents."
        else:
            mc.name "Your mouth is good, but it isn't THAT good. Now get back to it."
            "You put your hand on the back of her head, encouraging her to get back to work."
            the_girl "Ugh... seriously? Maybe this wasn't such a good idea."
            "She looks at your cock for several seconds, but so steadily increase the pressure on the back of her head until she sighs and gives in."
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        "[the_girl.title] opens her mouth and resumes sucking you off, her soft pouty lips feel great as her head begins to bob up and down again."
        $ the_person.change_obedience(2)
    return

label outro_blowjob(the_girl, the_location, the_object):
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    "Little by little the soft, warm mouth of [the_girl.title] brings you closer to orgasm. One last pass across her velvet tongue is enough to push you past the point of no return."
    $ climax_controller = ClimaxController(["Cum on her face","face"],["Cum in her mouth","mouth"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        call blowjob_enhanced_kneel_face_cum(the_girl) from _call_blowjob_enhanced_kneel_face_cum_outro_blowjob
    elif the_choice == "Cum in her mouth":
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        mc.name "Fuck, I'm about to cum!"
        "You keep a hand on the back of [the_girl.title]'s head to make it clear you want her to keep sucking."
        call blowjob_enhanced_kneel_mouth_cum(the_girl) from _call_blowjob_enhanced_kneel_mouth_cum_outro_blowjob
    return

label transition_blowjob_deepthroat(the_girl, the_location, the_object):
    mc.name "Fuck that feels great [the_girl.title]. Think you can take it any deeper?"
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] slides off your dick with a wet pop and takes a few breaths."
    if the_girl.body_type == "curvy_body" and the_girl.get_opinion_score("giving blowjobs") > 0 and the_girl.sex_skills["Oral"] > 3 and renpy.random.randint(0,2) == 0:
        the_girl "Well you know what they say."
        mc.name "What?"
        the_girl "Big girls give better head."
        "With that she opens her mouth wide and slides you back down her throat. She doesn't stop until her nose taps your stomach and she has your entire cock in her mouth. [the_girl.possessive_title] look up at you and winks as she starts to very slightly bob her head."
    else:
        if the_girl.effective_sluttiness() > 60 or the_girl.sex_skills["Oral"] > 3 :
            if the_girl.get_opinion_score("giving blowjobs") < 0:
                the_girl "Okay [the_girl.mc_title], I'll see what I can do."
            else:
                the_girl "Okay [the_girl.mc_title], I'll see what I can do, but I'm not very good at it."
        else:
            the_girl "I'll... I'll do my best."

        if the_girl.sex_skills["Oral"] < 3:
            $ play_gag_sound()
            "She kisses the tip of your cock, then slides it into her mouth. Gets your length halfway down, then gags softly on it and pauses."
            $ deepthroat.current_modifier = "blowjob"
            $ deepthroat.redraw_scene(the_girl)
            "[the_girl.possessive_title] collects herself then keeps going, fighting her gag reflex until she manages to fit three quarters of your shaft down her throat."
        else:
            $ deepthroat.current_modifier = "blowjob"
            $ deepthroat.redraw_scene(the_girl)
            "She kisses the tip of your cock, then slides it into her mouth. Bit by bit she takes it deeper, until you have your entire shaft down her throat."
            "She pauses there for a moment, then starts to bob her head up and down slowly."
    return

label transition_blowjob_to_deepthroat_taboo_break_label(the_girl, the_location, the_object):
    mc.name "Fuck that feels great [the_girl.title]. Could you do something for me?"
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)
    "[the_girl.possessive_title] slides off your dick with a wet pop and takes a few breaths."
    the_girl "Alright, what dirty thought crossed your mind?"
    mc.name "Could you slide my dick as deep as possible down your throat?"
    the_girl "Oh, you want me to deepthroat this monster..."
    if the_girl.effective_sluttiness() > 60 or the_girl.sex_skills["Oral"] > 3 :
        if the_girl.get_opinion_score("giving blowjobs") < 0:
            the_girl "Okay [the_girl.mc_title], I'll see what I can do."
        else:
            the_girl "Okay [the_girl.mc_title], I'll see what I can do, but I'm not very good at it."
    else:
        the_girl "I'll... I'll give it a try..."

    if the_girl.sex_skills["Oral"] < 3:
        $ play_gag_sound()
        "She kisses the tip of your cock, then slides it into her mouth. Gets your length halfway down, then gags softly on it and pauses."
        $ deepthroat.current_modifier = "blowjob"
        $ deepthroat.redraw_scene(the_girl)
        "[the_girl.possessive_title] collects herself then keeps going, fighting her gag reflex until she manages to fit three quarters of your shaft down her throat."
    else:
        $ deepthroat.current_modifier = "blowjob"
        $ deepthroat.redraw_scene(the_girl)
        "She kisses the tip of your cock, then slides it into her mouth. Bit by bit she takes it deeper, until you have your entire shaft down her throat."
        "She pauses there for a moment, then starts to bob her head up and down slowly."
    return

label transition_default_blowjob(the_girl, the_location, the_object):
    if mc.condom:
        the_girl "I don't think we need this anymore."
        "[the_girl.possessive_title] pulls the condom off your dick."
        $ mc.condom = False

    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    if the_girl.has_cum_fetish or the_girl.get_opinion_score("giving blowjobs") > 1:
        "Without hesitation, [the_girl.possessive_title] drops to her knees in front of you. She runs her hands along your hips, then leans forward and slides her lips over the tip of your dick."
    else:
        if the_girl.effective_sluttiness() > 35 or the_girl.get_opinion_score("giving blowjobs") > 0:
            "[the_girl.possessive_title] looks at your shaft then drops to her knees in front of you. She leans forward and slides her lips over the tip of your dick."
        else:
            "[the_girl.possessive_title] looks at your shaft for a moment then drops to her knees in front of you. She leans forward and kisses the tip of your dick gingerly."
    mc.name "That's it, that's a good girl."
    return

label strip_blowjob(the_girl, the_clothing, the_location, the_object):
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)

    "[the_girl.title] pops off your cock and looks up at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing)
    "[the_girl.possessive_title] stands and strips off her [the_clothing.name]. She drops it to the ground, then gets back on her knees and slides your cock inside her mouth."
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    return

label strip_ask_blowjob(the_girl, the_clothing, the_location, the_object):
    $ blowjob.current_modifier = None
    $ blowjob.redraw_scene(the_girl)

    "[the_girl.title] pops off your cock and looks up at you from her knees."
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = blowjob.position_tag)
            "[the_girl.possessive_title] strips out of her [the_clothing.name]. Then she gets back to work and slides your cock all the way to the back of her mouth."
            $ blowjob.current_modifier = "blowjob"
            $ blowjob.redraw_scene(the_girl)
            return True


        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Yeah? Do I look sexy in it?"
                $ blowjob.current_modifier = "blowjob"
                "She licks the length of your shaft, then slides your tip into her mouth and starts to blow you again."
            else:
                the_girl "Does it make me look like a good little slut? Or is your cock in my mouth enough for that?"
                $ blowjob.current_modifier = "blowjob"
                $ blowjob.redraw_scene(the_girl)
                "She slides you back into her mouth and presses you all the way to the back, rubbing your tip against the back of her throat for a second before she goes back to blowing you."
            return False
    return

label orgasm_blowjob(the_girl, the_location, the_object):
    $ blowjob.current_modifier = "blowjob"
    $ blowjob.redraw_scene(the_girl)
    "[the_girl.title] pauses suddenly. You hear her whimper softly - the noise party muffled by your cock."
    menu:
        "Be rough as she cums":
            "[the_girl.possessive_title] starts to pull back off of your cock. You place a firm hand on the back of her head."
            mc.name "Did I tell you to stop sucking, you dirty little slut?"
            if the_girl.sex_skills["Oral"] > 2:
                "You push her back down, hard. [the_girl.title] keeps her mouth open wide and fits you all the way in, quivering as she climaxes."
            else:
                $ play_gag_sound()
                "You push her back down, hard. [the_girl.title] gags and coughs, but you make sure she gets your cock back into her mouth. She quivers as she climaxes"

            mc.name "A cock sleeve like you deserves to have her throat stuffed when she cums."
            if the_girl.get_opinion_score("being submissive") > 0:
                if the_girl.sluttiness < blowjob.slut_cap:
                    $ the_girl.change_slut(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.
                $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
                $ play_gag_sound()
                "[the_girl.possessive_title] closes her eyes tight. You can feel her throat spasm around your shaft in time with her orgasmic contractions."
                $ the_girl.have_orgasm()
                if the_girl.vagina_visible:
                    "You can see that [the_girl.title]'s pussy is dripping wet as she cums."
                else:
                    $ the_item = the_girl.outfit.get_lower_top_layer
                    if the_item.underwear:
                        "[the_girl.possessive_title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.display_name]."
                    else:
                        "[the_girl.possessive_title] clenches her thighs together and rides out her orgasm."
                    $ the_item = None
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                "When she's stopped twitching and moaning you let [the_girl.title] slide back. She pants loudly, then licks along the length of your cock."
                the_girl "That was... incredible... I want more!"
            else:
                "[the_girl.possessive_title] closes her eyes as her orgasm peaks. She holds almost perfectly still, your dick still sitting in her mouth, until she's finished."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                "She pulls off and takes a long, deep breath."
                $ the_girl.change_stats(happiness = -2, obedience = 1)
                the_girl "Just... Let me handle things next time, okay?"

        "Be gentle as she cums":
            $ blowjob.current_modifier = None
            $ blowjob.redraw_scene(the_girl)
            mc.name "That's it, cum for me [the_girl.title]."
            $ the_girl.have_orgasm()
            "[the_girl.possessive_title] pulls off your cock as she climaxes. She nuzzles up against your hot, wet shaft as her body shivers uncontrollably."
            "You stroke her hair and wait until she's over the worst of it."
            $ the_girl.change_happiness(2)
            the_girl.name "Wow... Thanks for waiting, that was really intense."
            "She licks your shaft and looks up at you."
            the_girl.name "Should I get going again?"
            "She doesn't wait for an answer and starts sucking your cock again."
    return

label blowjob_comment(the_girl, the_location, the_object):
    $ last_position = last_position_used()
    if not last_position or not last_position.skill_tag in ["Anal", "Vaginal"]:
        $ last_position = None
        return

    if the_girl.effective_sluttiness() > 70 or (the_girl.effective_sluttiness(50) and the_girl.get_opinion_score("being submissive") > 0):
        if last_position.skill_tag == "Anal":
            the_girl "I love the taste of my ass on your lovely cock."
            $ the_girl.change_arousal(2)
        elif last_position.skill_tag == "Vaginal":
            the_girl "I love tasting my pussy juice on your amazing cock."
            $ the_girl.change_arousal(2)
    elif the_girl.effective_sluttiness() > 40:
        if last_position.skill_tag == "Anal":
            the_girl "I'm still getting used to tasting my ass on your cock."
            $ the_girl.change_arousal(1)
        elif last_position.skill_tag == "Vaginal":
            the_girl "I'm still getting used to tasting my juices on your cock."
            $ the_girl.change_arousal(1)
    else:
        if last_position.skill_tag == "Anal":
            the_girl "I don't care for tasting my ass on your dick."
            $ the_girl.change_stats(happiness = -2, arousal = -2)
        elif last_position.skill_tag == "Vaginal":
            the_girl "I don't like tasting my juices on your dick."
            $ the_girl.change_stats(happiness = -2, arousal = -2)

    $ last_position = None
    return

label blowjob_enhanced_kneel_throat_cum(the_girl):
    if the_girl.obedience >= 180 or the_girl.get_opinion_score("drinking cum") > 0: #She takes it like a champ
        "With both hands firmly on [the_girl.possessive_title]'s head you pull her as far down your cock as she'll go."
        "You grunt and release your load, firing pulse after pulse of hot cum down her throat and directly into her stomach."
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)
        "[the_girl.title] struggles to drink it all down, but doesn't try and pull off."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ skull_fuck.redraw_scene(the_girl)
        "When the last moments of your climax have passed you pull back, cock trailing spit and cum as you leave her mouth."
        if the_girl.get_opinion_score("drinking cum") > 0:
            the_girl "I thought you were going to drown me with your cum for a moment... Mmmm."
            $ the_girl.change_stats(happiness = 1, slut = 1)
            "She shivers with pleasure at the thought."
        else:
            "She runs the back of her hand along her lips, removing the cum trails and sits back to catch her breath."
            $ the_girl.call_dialogue("cum_mouth")

    elif the_girl.effective_sluttiness() > 90 or (the_girl.get_opinion_score("giving blowjobs") > 1 and the_girl.sex_skills["Oral"] > 2) or the_girl.sex_skills["Oral"] > 5:
        "[the_girl.possessive_title] looks up at you and stares into your eyes as you climax."
        if the_girl.sex_skills["Oral"] > 3:
            "She tightens and relaxes her throat, as if to draw out every last drop of semen from you."
        "She gently licks your balls with her tongue."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ deepthroat.redraw_scene(the_girl)
        "When you're completely finished she pulls off slowly, kissing the tip before leaning back."
        $ the_girl.call_dialogue("cum_mouth")
    elif the_girl.effective_sluttiness() > 70 or the_girl.get_opinion_score("giving blowjobs") > 1 or the_girl.sex_skills["Oral"] > 4:
        $ play_gag_sound()
        "[the_girl.possessive_title] closes her eyes and holds still as you climax. You feel her throat spasm a few times as she struggles to keep your cock in place."
        $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
        $ the_girl.cum_in_mouth()
        $ deepthroat.redraw_scene(the_girl)
        "When you're finished she pulls off quickly, gasping for air. It takes a few seconds for her to regain her composure."
        $ the_girl.call_dialogue("cum_mouth")
    else:
        $ play_gag_sound()
        "[the_girl.possessive_title] closes her eyes and tries to hold still as you climax. Her throat spasms as soon as the first blast of sperm splashes across the back, and she goes to pull back."
        menu:
            "Let her pull back":
                "With no other choice, you stroke yourself off onto her face as she coughs and gasps for breath."
                $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                $ the_girl.cum_on_face()
                $ the_girl.draw_person(position = "kneeling1")
                $ the_girl.call_dialogue("cum_face")
            "Stop her":
                "You grab [the_girl.possessive_title]'s head with both hands and pull her as far down your cock as she'll go."
                "[the_girl.title]'s eyes go wide as she realizes you don't intend to let her off your cock as you cum."
                "She tries to pull her head back, but you hold it in place as you begin to unload your hot, sticky load directly into her throat."
                "For a brief second she manages to keep up with the torrent of cum, then it overwhelms her."
                $ the_girl.cum_in_mouth()
                $ skull_fuck.redraw_scene(the_girl)
                $ play_gag_sound()
                "She spasms and gags. A mix of her spit and your semen bubble around the base of your cock, collecting in drops that roll down her chin and onto her tits."
                $ the_girl.cum_on_tits(add_to_record = False)
                $ skull_fuck.redraw_scene(the_girl)
                $ play_gag_sound()
                "She gags and coughs again, this time blowing little cum bubbles out of her nose as her body struggles to find somewhere to put more and more of your sperm."
                $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
                "Finally you're spent and you finally let [the_girl.title] pull off of your cock."
                $ play_gag_sound()
                the_girl "Guahh... Guahh... Ah... Ah..."
                $ play_swallow_sound()
                mc.name "Fuck that felt good."
                the_girl "There was so much... Ah... I thought I was going to drown in it..."
                "Still gasping for air, she wipes your sperm away from her nose and chin, then swallows loudly to get rid of the rest of it."
                $ the_girl.call_dialogue("cum_mouth")
                $ the_girl.change_arousal(the_girl.get_opinion_score(["drinking cum", "being submissive"]))
    return

label blowjob_enhanced_kneel_mouth_cum(the_girl):
    if the_girl.get_opinion_score("drinking cum") < 0:
        "[the_girl.title] clearly has other ideas as she brings one hand up to your cock and goes to pull her mouth off of your cock."
        menu:
            "Let her off":
                "You let her pull back."
                $ the_girl.change_stats(love = -the_girl.get_opinion_score("drinking cum"), happiness = -the_girl.get_opinion_score("drinking cum"))
                if the_girl.has_cum_fetish:
                    "[the_girl.title] takes a hold of your cock with one hand and starts to pump it."
                    "She sticks out her tongue for you and holds still, eager to take your hot load."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She shivers herself as your cum splashes over her."
                    $ the_girl.change_arousal(10)
                elif the_girl.get_opinion_score("cum facials") < 0:
                    "[the_girl.title] moves her head so that your cum will miss her face."
                    if the_girl.get_opinion_score("being covered in cum") > 0:
                        "[the_girl.possessive_title] moves your cock to point at her chest."
                        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
                        $ the_girl.cum_on_tits()
                        $ the_girl.draw_person(position = "kneeling1")
                        $ the_girl.change_stats(love = the_girl.get_opinion_score("being covered in cum"))
                        if the_girl.tits_available:
                            "You let out a shuddering moan as you cum, pumping your sperm over [the_girl.possessive_title]'s bare tits. She shivers herself as your cum splashes over her."
                        else:
                            "You let out a shuddering moan as you cum, pumping your sperm over [the_girl.possessive_title]'s chest. She smiles as your cum splashes over her."
                    else:
                        "You cum onto the floor, missing [the_girl.possessive_title] completely."
                        $ the_girl.change_stats(love = -the_girl.get_opinion_score("cum facials"), happiness = -the_girl.get_opinion_score("cum facials"))
                elif (the_girl.effective_sluttiness() > 90 or the_girl.get_opinion_score("cum facials") > 1):
                    "[the_girl.title] sticks out her tongue for you, holds still and looks you in the eye, eager to take your hot load."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished as she maintains eye contact."
                elif the_girl.effective_sluttiness() > 70:
                    "[the_girl.title] closes her eyes and waits patiently for you to cum."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
                else:
                    "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."

                if the_girl.has_face_cum:
                    "You take a deep breath to steady yourself once you've finished cumming. [the_girl.title] looks up at you from her knees, face covered in your semen."
                    $ the_girl.call_dialogue("cum_face")
                    if the_girl.has_cum_fetish:
                        "She closes her eyes and starts to gently massage your cum all over her face."

            "Hold her in place":
                "You grab her head with both your hands and thrust roughly into her mouth as you cum."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
                if the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                else:
                    $ the_girl.change_stats(arousal = the_girl.get_opinion_score("being submissive"), love = the_girl.get_opinion_score("drinking cum"))
    else:
        if the_girl.has_cum_fetish:
            if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
                "[the_girl.possessive_title] goes as deep as she can on your dick, trying to get as much of it in her mouth as possible."
                "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
                "You grunt and twitch as you start to empty your balls right into her throat."
                $ play_gag_sound()
                "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
                $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                $ play_swallow_sound()
                "When you're completely finished she pulls back slightly so that she can breathe more easily."
                $ the_girl.call_dialogue("cum_mouth")
            else:
                "She keeps blowing you until you tense up and start to pump your load out into her mouth."
                "[the_girl.possessive_title] pulls her head back until just the tip of your cock is in her mouth and she begins to stroke you."
                $ play_swallow_sound()
                "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
                $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
                $ the_girl.cum_in_mouth()
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.change_arousal(10)
                $ the_girl.call_dialogue("cum_mouth")
                $ play_moan_sound()
                "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
        elif the_girl.effective_sluttiness() > 80 or the_girl.get_opinion_score("giving blowjobs") > 1:
            "[the_girl.possessive_title] doesn't even flinch as you shoot your hot cum across the back of her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "She keeps bobbing her head up and down until you've let out every last drop, then slides back carefully. She looks up at you and opens her mouth to shows it full of sperm."
        else:
            "[the_girl.possessive_title] stops when you shoot your first blast of hot cum across the back of her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            "She pulls back, leaving just the tip of your cock in her mouth as you fill it up with semen. Once you've finished she slides off, looks up at you and opens her mouth to shows it full of sperm."


        if not the_girl.has_cum_fetish:
            if the_girl.get_opinion_score("being covered in cum") > 0 and the_girl.tits_available:
                "[the_girl.possessive_title] tilts her head forward and let your cum dribble out of her mouth onto her bare tits."
                $ the_girl.call_dialogue("cum_mouth")
                $ the_girl.cum_on_tits(add_to_record = False)
                $ the_girl.draw_person(position = "kneeling1")
                "She starts to rub your cum on her breasts."
            elif the_girl.effective_sluttiness() > 80 or the_girl.get_opinion_score("drinking cum") > 1:
                $ play_swallow_sound()
                "Once you've had a good long look at your work [the_girl.title] closes her mouth and swallows loudly."
                $ play_swallow_sound()
                "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
            else:
                "Once you've had a good long look at your work [the_girl.title] leans over to the side and lets your cum dribble out slowly onto the ground."
                "She straightens up and wipes her lips with the back of her hand."
                $ blowjob.current_modifier = None
                $ blowjob.redraw_scene(the_girl)
                $ the_girl.call_dialogue("cum_mouth")
    return

label blowjob_enhanced_kneel_face_cum(the_girl):
    if the_girl.has_cum_fetish:
        if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
            "You go to step back but [the_girl.possessive_title]'s grabs your butt-cheeks with her hands, holding you in place and pushing her face forward."
            "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
            $ play_gag_sound()
            "You grunt and twitch as you start to empty your balls right into her throat."
            $ play_gag_sound()
            "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
            $ ClimaxController.manual_clarity_release(climax_type = "throat", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            $ play_swallow_sound()
            "When you're completely finished she pulls back slightly so that she can breathe more easily."
        else:
            "You go to step back but [the_girl.possessive_title]'s grabs you by the cock with her hand."
            "[the_girl.possessive_title] lets you pull back until just the tip of your cock is in her mouth and she begins to stroke you."
            $ play_swallow_sound()
            "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
            $ the_girl.cum_in_mouth()
            $ blowjob.redraw_scene(the_girl)
            $ play_moan_sound()
            "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage."
        $ the_girl.change_arousal(10)
        $ the_girl.call_dialogue("cum_mouth")
    else:
        "You take a step back, pulling your cock out of [the_girl.possessive_title]'s mouth with a satisfyingly wet pop, and take aim at her face."
        if (the_girl.get_opinion_score("drinking cum")) > (the_girl.get_opinion_score("cum facials")):
            "[the_girl.possessive_title] looks slightly disappointed."
        $ blowjob.current_modifier = None
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.has_cum_fetish:
            "[the_girl.title] takes a hold of your cock with one hand and starts to pump it."
            "She sticks out her tongue for you and holds still, eager to take your hot load."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She shivers herself as your cum splashes over her."
            $ the_girl.change_arousal(10)

        elif the_girl.get_opinion_score("cum facials") < 0:
            "[the_girl.title] moves her head to the side so that your cum will miss her."
            menu:
                "Let her off":
                    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
                    "You cum onto the floor, missing [the_girl.possessive_title]."
                    $ the_girl.change_stats(love = -the_girl.get_opinion_score("cum facials"))
                "Pull her back":
                    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
                    $ the_girl.cum_on_face()
                    $ the_girl.draw_person(position = "kneeling1")
                    $ the_girl.change_stats(love = the_girl.get_opinion_score("cum facials"))
                    "You grab your cock with one hand and her head with the other. You hold her head in place as you use your other hand to pump your cum over [the_girl.possessive_title]'s face."
        elif (the_girl.effective_sluttiness() > 90 or the_girl.get_opinion_score("cum facials") > 1):
            "[the_girl.title] sticks out her tongue for you, holds still and looks you in the eye, eager to take your hot load."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished as she maintains eye contact."
        elif the_girl.effective_sluttiness() > 70:
            "[the_girl.title] closes her eyes and waits patiently for you to cum."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        if the_girl.has_face_cum:
            "You take a deep breath to steady yourself once you've finished cumming. [the_girl.title] looks up at you from her knees, face covered in your semen."
            $ the_girl.call_dialogue("cum_face")
            if the_girl.has_cum_fetish:
                "She closes her eyes and starts to gently massage your cum all over her face."
    return
