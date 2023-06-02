init:
    python:
        skull_fuck = Position(name = "Skull Fuck", slut_requirement = 65, slut_cap = 100, requires_hard = True, requires_large_tits = False,
            position_tag = "blowjob", requires_location = "Kneel", requires_clothing = "None", skill_tag = "Oral",
            girl_arousal = 5, girl_energy = 10,
            guy_arousal = 25, guy_energy = 12,
            connections = [],
            intro = "intro_skull_fuck",
            scenes = ["scene_skull_fuck_1","scene_skull_fuck_2","scene_skull_fuck_3", "scene_skull_fuck_4"],
            outro = "outro_skull_fuck",
            transition_default = "transition_default_skull_fuck",
            strip_description = "strip_skull_fuck", strip_ask_description = "strip_ask_skull_fuck",
            orgasm_description = "orgasm_skull_fuck",
            taboo_break_description = "taboo_break_skull_fuck",
            verb = "throat fuck",
            opinion_tags = ["giving blowjobs", "being submissive"], record_class = "Blowjobs",
            default_animation = idle_wiggle_animation, modifier_animations = {"blowjob":blowjob_bob},
            associated_taboo = "sucking_cock")


init 1:
    python:
        skull_fuck.link_positions(deepthroat,"transition_skull_fuck_deepthroat_blowjob")


label intro_skull_fuck(the_girl, the_location, the_object):
    # In theory this event is only reachable while deepthroating someone, but who knows...

    "You unzip your pants and pull your hard cock out."
    mc.name "[the_girl.title], I want you on your knees. I want to fuck that pretty little mouth."
    $ the_girl.draw_person(position = "kneeling1")
    "[the_girl.possessive_title] nods and obediently kneels down in front of you."
    "You rub your dick along her cheek a few times, then slide it back and line it up with her lips."
    $ skull_fuck.current_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "You grab her head firmly and pull it towards you. Her eyes go wide as you ram yourself balls deep."
    return

label taboo_break_skull_fuck(the_girl, the_location, the_object): #In theory you can only reach this from a transition that would have already broken the taboo, so this shouldn't come up.
    $ the_girl.call_dialogue(skull_fuck.associated_taboo+"_taboo_break") #Convince dialogue is handled here.
    if the_girl.effective_sluttiness(skull_fuck.associated_taboo) > skull_fuck.slut_cap:
        #She's eager to try this
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)
        "[the_girl.possessive_title] kneels down in front of you, eyes locked on your hard cock."

        $ skull_fuck.current_modifier = "blowjob"
        $ skull_fuck.redraw_scene(the_girl)
        "She leans in, turning her head to the side to run her tongue down the bottom of your shaft."
        "She licks your balls briefly, then works back up to the tip and slides it past her lips."
        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She wastes no time picking up speed, happily bobbing her head up and down over your sensitive tip."

    else:
        $ skull_fuck.current_modifier = None
        $ skull_fuck.redraw_scene(the_girl)
        "[the_girl.possessive_title] hesitantly gets onto her knees, eyes locked on your hard cock."
        "She gently holds onto your shaft with one hand and brings the tip closer to her lips."
        "She looks up at you just before the moment of truth, locking eyes as she opens her lips and slides the tip of your cock past them."

        $ skull_fuck.current_modifier = "blowjob"
        $ skull_fuck.redraw_scene(the_girl)
        "You sigh happily as you feel [the_girl.title]'s warm mouth envelop your cock."
        "She moves slowly at first, gently working her head up and down over your sensitive tip."
    mc.name "I think we can do better than that. Come here!"
    $ play_gag_sound()
    "You grab onto [the_girl.title]'s head with both hands and slam it forward onto your cock. She gags loudly, blowing spit around your base as you bottom out."
    "For a few seconds you just enjoy the feeling of her throat as it struggles to adjust to your size. Then you pull back and slam your cock home again."
    return

label scene_skull_fuck_1(the_girl, the_location, the_object):
    # Mantle her and pin her down.
    $ skull_fuck.current_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "[the_girl.title]'s throat is warm and tight around your shaft as you slide yourself in and out."
    "She closes her eyes, struggling to keep herself under control."
    mc.name "Fuck your throat feels good!"
    "You take a half step forward, putting her between your legs with her head tilted upwards."
    "You pull her face against your crotch, flexing your cock."
    mc.name "Can you feel that? Do you like choking on a big, hard cock?"
    $ play_gag_sound()
    "Her only response is to gag softly, spit running down her chin."
    "You hold the position for a second before moving your hips and fucking her face."
    return

label scene_skull_fuck_2(the_girl, the_location, the_object):
    # Standard "You hold her head in place and fuck her throat raw"
    "You hold tight onto [the_girl.possessive_title]'s head, keeping it in place as you move your hips and fuck her face."
    $ play_gag_sound()
    "She gags and gurgles as you bottom your cock out with each stroke, but manages to keep her arms down at her sides."
    mc.name "Look up at me [the_girl.title]."
    "She struggles to turn her eyes up to meet yours. When she manages it you hold yourself deep and grind your hips against her face."
    mc.name "You're such a perfect cock socket, you know that? Fuck, this feels good."
    "You grab onto her hair at the roots and piston her head back and forth. Each thrust comes with a fresh gurgle from her ravaged throat."
    return

label scene_skull_fuck_3(the_girl, the_location, the_object):
    # Push extra deep and get her gagging on it.

    "You slow down and enjoy every inch of [the_girl.possessive_title]'s tight throat."
    "You keep one hand firm on the back of her head and move the other down to her throat, wrapping your fingers around it."
    "You can feel it bulge as you slide your full length inside of her."
    $ play_gag_sound()
    "She sputters as you throat her. Her spit bubbles around your shaft and drips down her chin, dropping onto her tits below."
    mc.name "That's it, gag on it you cock slut!"
    "You massage her throat with your hand and can feel the pressure on your own cock."
    "When you're satisfied she's had it down long enough you pull back, freeing her windpipe and letting her pull in a deep breath through her nose."
    "You don't wait long before sliding back into her, holding her head in place and fucking it like a toy."
    return

label scene_skull_fuck_4(the_girl, the_location, the_object):
    if the_girl.sex_skills["Oral"] < 4:
        "[the_girl.title] is struggling to take the full length of your dick down her throat. She pulls off and pants for air."
        the_girl "Ah... I haven't got it quite right yet..."
        "Once she's caught her breath you slide your cock back into her mouth. Slowly sliding it deeper down her throat."
        "[the_girl.possessive_title] looks up to you, tears welling up in her eyes."
        if the_girl.sex_skills["Oral"] < 2:
            $ play_gag_sound()
            "She gags and gurgles as you bottom your cock out with each stroke, but manages to keep her arms down at her sides."
            mc.name "You're such a perfect flesh light, you know that? Fuck, this feels good."
            "Her inexperience stops her from making any progress. She lurches backwards, gagging and gasping for air."
            the_girl "Maybe I... Ah... Just need more practice..."
            "She shrugs, wipes some spit from her lips, and slips you back into her mouth."
        else:
            $ play_gag_sound()
            "She sputters as you throat her. Her spit bubbles around your shaft and drips down her chin, dropping onto her tits below."
            mc.name "That's it, gag on it you cock slut!"
            "You massage her throat with your hand and can feel the pressure on your own cock."
    else:
        "You stop fucking [the_girl.title]'s face for a second."
        mc.name "I wonder how long I could keep deep fucking your face, want to find out?"
        "She nods and you push your cock back into [the_girl.possessive_title]'s throat. Your balls tap against her chin."
        if the_girl.get_opinion_score("being submissive") > 0 and the_girl.get_opinion_score("giving blowjobs") > 0:
            "After a while, she pulls back, gagging and gasping for air."
            mc.name "That wasn't bad, but I think you could do better..."
            the_girl "I want to try again. [the_girl.mc_title], could you... hold me down so I can't pull off?"
            "You place a steady hand on the back of her head and pull her closer to you in response."
            mc.name "I'll help you do the best you could possibly do."
            $ the_girl.change_happiness(4+the_girl.get_opinion_score("giving blowjobs"))
            "She looks up to you, takes a few deep breaths through her nose and slides you all the way to the back of her throat."
            $ play_gag_sound()
            "[the_girl.possessive_title]'s throat spasms around your shaft as she starts to reach her limit. She closes her eyes and focuses hard on her task."
            menu:
                "Keep fucking her throat" if the_girl.obedience >= 110:
                    mc.name "Not yet, you can do better than that."
                    "You keep fucking [the_girl.title]'s throat deeply. She doesn't resist."
                    "After a few more seconds [the_girl.title] tries to pull off again, forcing you to pull her back in."
                    menu:
                        "Keep fucking her throat" if the_girl.obedience >= 120:
                            "A little more force and [the_girl.title] stays where she is. Her eyes are closed tight as she struggles to stay in control."
                            $ play_gag_sound()
                            "More time passes. [the_girl.title] starts to squirm on her knees."
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                            menu:
                                "Keep fucking her throat" if the_girl.obedience >= 130:
                                    mc.name "Don't give up now [the_girl.title], you're doing great."
                                    if the_girl.is_bald:
                                        "You grab her head, locking your fingers behind her head to give you a better grip and control over her movements."
                                    else:
                                        "You grab a handful of her hair to give you a better grip and don't let her go anywhere."
                                    $ play_gag_sound()
                                    "[the_girl.title]'s throat starts to rhythmically clench down on the shaft of your dick."
                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                    $ mc.change_arousal(1)
                                    "[the_girl.possessive_title]'s grabs at your legs, looking for support."
                                    menu:
                                        "Keep fucking her throat" if the_girl.obedience >= 150:
                                            mc.name "You're going to choke on this dick until I'm satisfied. Don't you dare pull off."
                                            $ play_moan_sound()
                                            "[the_girl.title] moans, her throat rumbling around your cock. Her eyes roll up as she tries to make eye contact with you."
                                            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                            "Several more long seconds pass. Pushed to her limit, [the_girl.title] pulls back harder and starts to tap on your leg."
                                            menu:
                                                "Choke her out" if the_girl.obedience >= 170:
                                                    mc.name "I said hold still. Not until I'm done with you."
                                                    "[the_girl.title] squirms and fidgets on her knees, but obeys your commands like a good girl."
                                                    "Little by little her movements slow down, her eyelids start to droop down over her rolled up eyes, and she slips into a half-conscious state."
                                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                                    $ play_moan_sound()
                                                    "[the_girl.possessive_title]'s body doesn't stop reacting to you and your cock. Her throat rhythmically milking your shaft and she keeps moaning softly."
                                                    "Satisfied, you keep fucking [the_girl.title]'s face. She keeps sucking on you in her oxygen deprived stupor."
                                                    mc.name "That's enough [the_girl.title], you've done enough."
                                                    "You pull back entirely. She leaves your cock with a satisfying, wet pop followed by a huge gasp for air."
                                                    "It takes a few long moments until [the_girl.title] shakes her head and comes to her senses."
                                                    $ the_girl.increase_trance(show_dialogue = False)
                                                    the_girl "I... Oh my god... How long was I... Ah... Ah..."
                                                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                                                    "The thought of passing out on your cock seems to turn her on."
                                                    mc.name "Long enough, I think you've got a new personal best."
                                                    $ play_moan_sound()
                                                    "[the_girl.possessive_title] bites her lip and moans to herself for a second."
                                                    the_girl "Thank you [the_girl.mc_title], you really pushed me there. Now... I can't make this all about me."
                                                    "She takes a deep breath, opens wide, waiting for you enter into her mouth. She holds her head still while you fuck her face and when you pull back, she takes a quick breath through her nose."
                                                    return #Don't do the rest of the scene because we have our special case here.

                                                "Choke her out\n{color=#ff0000}{size=18}Requires: 170 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 170:
                                                    pass

                                                "Let her up":
                                                    pass
                                        "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 150 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 150:
                                            pass

                                        "Let her up":
                                            pass
                                "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 130:
                                    pass

                                "Let her up":
                                    pass

                        "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 120 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 120:
                            pass

                        "Let her up":
                            pass

                "Keep fucking her throat\n{color=#ff0000}{size=18}Requires: 110 Obedience{/size}{/color} (disabled)" if the_girl.obedience < 110:
                    pass

                "Let her up":
                    pass

            "[the_girl.title] yanks her head back and off of your hard cock. She gasps for breath as soon as you're clear."
            the_girl "That... was... intense... Ah..."
            if the_girl.is_bald:
                "It takes her a moment to catch her breath. You run hand over her smooth head while you let her recover."
            else:
                "It takes her a moment to catch her breath. You run your fingers through her hair while you let her recover."
            the_girl "That was a long time, but I think I could do better next time... Don't go so easy on me, okay?"
            "With that she leans forward and you start fucking her pretty face again."
        else:
            mc.name "Wow... that was pretty good, right?"
            $ the_girl.change_happiness(1+the_girl.get_opinion_score("giving blowjobs"))
            mc.name "Ah... Right, where was I..."
            $ play_gag_sound()
            "She only gurgles an answer while you push your cock back into her throat."
    return

label outro_skull_fuck(the_girl, the_location, the_object):
    $ play_gag_sound()
    "[the_girl.title]'s warm, wet throat wrapped around your cock sends shivers up your spine and the sound of her gagging on your dick pushes you past your limits."
    "You have a brief moment to consider how you want to finish as you jackhammer yourself in and out of her mouth."

    $ climax_controller = ClimaxController(["Cum on her face", "face"],["Cum down her throat", "throat"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum on her face":
        mc.name "Fuck, here I come!"
        $ deepthroat.current_modifier = None
        $ deepthroat.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_face_cum(the_girl) from _call_blowjob_enhanced_kneel_face_cum_outro_skull_fuck
    elif the_choice == "Cum down her throat":
        mc.name "Fuck, here I come!"
        $ blowjob.current_modifier = "blowjob"
        $ blowjob.redraw_scene(the_girl)
        call blowjob_enhanced_kneel_throat_cum(the_girl) from _call_blowjob_enhanced_kneel_throat_cum_outro_skull_fuck
    return

label transition_skull_fuck_deepthroat_blowjob(the_girl, the_location, the_object):
    $ play_gag_sound()
    "You give [the_girl.possessive_title]'s mouth a few more fast, powerful thrusts. She gags, spit dripping down her chin, as you bottom out each time."
    $ skull_fuck.special_modifier = None
    $ skull_fuck.redraw_scene(the_girl)
    "With one final thrust you let go of her, letting her pull back and away from your hard shaft. She sputters and coughs, desperate for a full breath of air."
    "You give her a moment to catch her breath, then place a hand on her cheek and guide her back towards your throbbing shaft."
    $ skull_fuck.special_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "She takes a deep breath, then slides it back into her mouth. You keep your hand light on her head and let her set her own pace and depth as she works your cock."
    return

label transition_default_skull_fuck(the_girl, the_location, the_object):
    $ skull_fuck.redraw_scene(the_girl)
    "You place your hands on either side of [the_girl.title]'s head and level your hard cock with her mouth."
    "You rest the tip on her lower lip and feel her warm breath on the sensitive skin each time she exhales."
    menu:
        "Ask her":
            mc.name "Ready?"
            if the_girl.is_dominant:
                the_girl "Just take it slow."
                "You pull her head towards your belly while thrusting your hips forwards, slowly penetrating her throat."
            else:
                if the_girl.is_submissive:
                    the_girl "Take me however you want."
                else:
                    the_girl "I'm ready, if you are."
                "She kisses the tip. You pull her head hard towards you and push your hips forward, slamming your cock to its base in a single stroke."
            $ skull_fuck.special_modifier = "blowjob"
            $ skull_fuck.redraw_scene(the_girl)
            $ play_gag_sound()
            the_girl "Guaah...gock...gargh..."
            "Although she is not comfortable, she let's you abuse her throat."
        "Push her down":
            if the_girl.has_cum_fetish:
                "She doesn't resist and lets you push her all the way down, while looking lovingly into your eyes."
                $ play_gag_sound()
                the_girl "Guaah...gock...gargh..."
                "Her eyes betray the pleasure she is feeling, towards the reward that is looming when you finish."
            elif the_girl.is_dominant:
                if the_girl.sex_skills["Oral"] >= 4:
                    "Her eyes go wide and she gags loudly."
                    $ play_gag_sound()
                    the_girl "Guaaah!"
                    "Her arms come up instinctively, but she struggles against the urge to push you away. She balls her fists and holds them close against her body."
                elif the_girl.sex_skills["Oral"] >= 2:
                    "She is resisting your push, slowly sliding your cock all the way down, squeezing your balls just a little too hard."
                    $ play_gag_sound()
                    the_girl "Guaaah!"
                else:
                    "She resists your push, spitting out your cock."
                    the_girl "Hey, I'm not your fleshlight! Let me do this on my own."
                    $ the_girl.change_stats(arousal = -10, happiness = -2)
            elif the_girl.is_submissive:
                if the_girl.sex_skills["Oral"] >= 4:
                    "She doesn't resist and lets you push her down, while looking into your eyes."
                    $ play_gag_sound()
                    the_girl "Guaah...gock...gargh..."
                    "She keeps on making guttural noises while you fuck her throat."
                else:
                    "She slightly resists your push, but lets you shove your dick down her throat."
                    $ play_gag_sound()
                    the_girl "Guaah...gock..."
                    "She keeps on gagging noises while you fuck her throat, but soldiers through."
            else:
                "She resists your push, coming back up."
                the_girl "Fuck me, could you do that a little slower!"
                $ the_girl.change_stats(arousal = -5, happiness = -1)
    return

label strip_skull_fuck(the_girl, the_clothing, the_location, the_object):
    "[the_girl.title] taps on your thigh and tries to move her head back."
    menu:
        "Ignore her": #You're really in control here.
            mc.name "I can't stop now, this feels too good!"

        "Let her up":
            $ skull_fuck.current_modifier = None
            $ skull_fuck.redraw_scene(the_girl)
            "You give her throat one last thrust, then let her slide back until the tip of your cock clears her lips."
            the_girl "Ah... One... Sec..."
            $ the_girl.call_dialogue("sex_strip")
            $ the_girl.draw_animated_removal(the_clothing, position = deepthroat.position_tag)
            "She gasps for air while pulling off her [the_clothing.name]. She drops it to the ground, then nods up at you."
            the_girl "Much better. Well, what are you waiting for?"
            "She opens her mouth and you slam your dick back down her throat."
            $ skull_fuck.current_modifier = "blowjob"
            $ skull_fuck.redraw_scene(the_girl)
    return

label strip_ask_skull_fuck(the_girl, the_clothing, the_location, the_object):
    $ return_value = True
    "[the_girl.title] taps on your thigh and tries to move her head back."
    menu:
        "Ignore her": #You're really in control here.
            mc.name "I can't stop now, this feels too good!"

        "Let her up":
            $ skull_fuck.current_modifier = None
            $ skull_fuck.redraw_scene(the_girl)
            "You give her throat one last thrust, then let her slide back until the tip of your cock just barely clears her lips."
            the_girl "I'm going to take off my [the_clothing.name], if that's okay with you."
            menu:
                "Let her strip":
                    mc.name "Take it off."
                    $ the_girl.draw_animated_removal(the_clothing, position = blowjob.position_tag)
                    "[the_girl.possessive_title] strips out of her [the_clothing.name], your hard shaft hovering inches from her face."
                    "When she drops it to the side you press yourself forward, parting her lips and sliding your cock back down her throat."

                "Leave it on":
                    mc.name "No, I like how you look with it on."
                    the_girl "Well then, what are you waiting for?"
                    "She opens her mouth wide and you slam your dick back down her throat."
                    $ return_value = False
            $ skull_fuck.current_modifier = "blowjob"
            $ skull_fuck.redraw_scene(the_girl)
    return return_value

label orgasm_skull_fuck(the_girl, the_location, the_object):
    $ skull_fuck.current_modifier = "blowjob"
    $ skull_fuck.redraw_scene(the_girl)
    "You're happily fucking [the_girl.possessive_title]'s warm, wet throat when you notice her closing her eyes."
    "Her thighs quiver and her hands drop instinctively to her crotch. She begins to rub her pussy furiously, driving herself to orgasm."
    mc.name "Cum for me you dirty slut!"
    if the_girl.sex_skills["Oral"] > 3:
        $ play_moan_sound()
        "[the_girl.possessive_title] keeps her mouth wide open for you, even as she twitches and writhes through her climax."
        "You fuck her tight throat until she finishes twitching."
    else:
        $ play_gag_sound()
        "[the_girl.possessive_title] gags on your cock as you push her down onto it."
        $ play_moan_sound()
        "Her body tightens up as she climaxes, and you make sure to take advantage of her tight throat by fucking it hard."

    if the_girl.get_opinion_score("being submissive") > 0:
        if the_girl.sluttiness > the_girl.sluttiness and the_girl.sluttiness < skull_fuck.slut_cap:
            $ the_girl.change_slut(the_girl.get_opinion_score("being submissive")) #If she likes being submissive this makes her cum and become sluttier super hard.

        $ the_girl.change_obedience(2*the_girl.get_opinion_score("being submissive"))
        if the_girl.vagina_visible:
            "You can see that [the_girl.title]'s [the_girl.pubes_description] pussy is dripping wet as she cums."
        else:
            $ the_item = the_girl.outfit.get_lower_top_layer
            if the_item.underwear:
                "[the_girl.title]'s dripping wet pussy has managed to soak through her underwear, leaving a wet mark on her [the_item.display_name]."
            else:
                "[the_girl.title] clenches her thighs together and rides out her orgasm."
            $ the_item = None
    else:
        $ the_girl.change_stats(happiness = -2, obedience = 1)

    $ skull_fuck.current_modifier = None
    $ skull_fuck.redraw_scene(the_girl)

    "Watching [the_girl.title]'s body writhe as she climaxes from your cock encourages you to go faster."
    "You clamp down on her head and slam yourself in and out of her throat."
    return
