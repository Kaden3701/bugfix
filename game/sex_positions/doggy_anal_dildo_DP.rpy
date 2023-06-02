init python:
    doggy_anal_dildo_dp = Position(name = "Doggy Anal DP", slut_requirement = 80, slut_cap = 100, requires_hard = True, requires_large_tits = False,
        position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
        girl_arousal = 26, girl_energy = 14,
        guy_arousal = 22, guy_energy = 20,
        connections = [],
        intro = "intro_doggy_anal_dildo_dp",
        scenes = ["scene_doggy_anal_dildo_dp_1","scene_doggy_anal_dildo_dp_2"],
        outro = "outro_doggy_anal_dildo_dp",
        transition_default = "transition_default_doggy_anal_dildo_dp",
        strip_description = "strip_doggy_anal_dildo_dp", strip_ask_description = "strip_ask_doggy_anal_dildo_dp",
        taboo_break_description = "taboo_break_doggy_anal_dildo_dp",
        orgasm_description = "orgasm_doggy_anal_dildo_dp",
        verb = "dp", verbing = "dp-ing",
        opinion_tags = ["doggy style sex", "anal sex", "vaginal sex"], record_class = "Anal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "anal_sex")

    # only one associated taboo is allowed in code ["anal_sex", "vaginal_sex"]


    #list_of_positions.append(doggy_anal_dildo_dp)

#init 1:
#    python:
#        doggy_anal_dildo_dp.link_positions_two_way(doggy, "transition_doggy_anal_dildo_dp_doggy", "transition_doggy_doggy_anal_dildo_dp")

label intro_doggy_anal_dildo_dp(the_girl, the_location, the_object):
    mc.name "[the_girl.title], I want you to get on your hands and knees for me. I want to fuck your ass and your pussy."
    "You secure the strap-on dildo to your cock. A quick lube application later, you get behind [the_girl.possessive_title]."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = doggy_anal_dildo_dp.position_tag, visible_enough = True, prefer_half_off = True)

    $ the_girl.draw_person(position = doggy_anal_dildo_dp.position_tag)

    if the_girl.effective_sluttiness() > 95:
        the_girl "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl "I don't know, are you sure that thing is gonna fit in me back there?"
    "[the_girl.possessive_title] gets onto all fours in front of you on the [the_object.name]. She arches her back and presents her ass."
    if the_girl.arousal_perc > 60:
        "Her [the_girl.pubes_description] pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
    else:
        "You line yourself up with her ass while [the_girl.possessive_title] reaches down and lines the dildo up with her pussy."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god! I'm so full... It's so good [the_girl.mc_title]!"
        $ the_girl.discover_opinion("anal sex")
    else:
        the_girl "Holy fuck! Go slow [the_girl.mc_title]. This is really intense..."
    return

label scene_doggy_anal_dildo_dp_1(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You give [the_girl.possessive_title]'s ass a good hard spank. She lets out a loud yelp"
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "[the_girl.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_girl "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out."
        $ play_moan_sound()
        "Pushing deep, the vibrating function on the dildo is in direct contact with her clit. She squirms and moans, being stuffed completely full."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you knead her ass cheeks with both hands."
        the_girl "Mmmm, that feels good [the_girl.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                "Encouraged by your response, [the_girl.possessive_title] reaches down with one hand and begins to rub her clit."
                "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. With each thrust the vibrator brushes against her fingers on her clit."
                "[the_girl.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit"
                if the_girl.get_opinion_score("masturbating") > 0:
                    "[the_girl.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                    $ the_girl.discover_opinion("masturbating")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating") * 2)
                if the_girl.sluttiness > 90:
                    the_girl "I'm sorry [the_girl.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                    the_girl "and then the dildo with it? I've never felt so full..."
                else:
                    "[the_girl.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself"
            "Fuck me with your ass":
                if the_girl.obedience > 180 or the_girl.get_opinion_score("being submissive") > 0:
                    the_girl "Yes [the_girl.mc_title]. I'll do my best."
                else:
                    the_girl "I'll give it my best, but this better be worth it..."
                "[the_girl.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you"
                "The next time she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier"
                the_girl "Mmm, that's a bit better..."
                "With the extra lube, [the_girl.possessive_title] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        $ play_moan_sound()
        "In response to your spanking, [the_girl.possessive_title] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass cheek a hard swat. She buries her face in the [the_object.name] and moans as she pushes herself back onto you again."
        the_girl "Oh fuck [the_girl.mc_title], I needed this so bad. Make me cum all over that dildo!"
        "[the_girl.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                "You decide to see what [the_girl.possessive_title] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass" ###FINISH
                the_girl "Mmm, does it feel good when I work it like this?"
                "[the_girl.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                if mc.arousal_perc > 70:
                    mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                    if the_girl.get_opinion_score("anal creampies") > 0:
                        the_girl "You should just shove it in as deep as you can and cum inside me."
                    elif the_girl.get_opinion_score("being covered in cum") > 0:
                        the_girl "You should pull out and cum all over my ass. That would be so hot..."
                    elif the_girl.get_opinion_score("cum facials") > 0:
                        the_girl "Tell me when you are about to cum and I'll let you cum all over my face..."
                    elif the_girl.obedience > 180:
                        the_girl "Cum wherever you want to... I just want to please you [the_girl.mc_title]."
                    else:
                        the_girl "I don't know... wherever you want I guess?"
                else:
                    mc.name "Wow, your ass is amazing. I love watching my dick disappear in your ass and the dildo into your pussy."
                    if the_girl.get_opinion_score("anal sex") > 0:
                        "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you. The grinding motion stimulates her clit against the vibrator."
                        the_girl "It's so good... I can't think... it's so good!"
                        "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                        mc.name "Wow, the things you do with this ass. You are amazing [the_girl.title]."
                        "[the_girl.possessive_title] sighs. You can tell the double penetration is very fulfilling for her."
                    else:
                        "[the_girl.possessive_title] looks back at you."
                        the_girl "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                        the_girl "And the dildo makes this so much better than just anal... it's AMAZING."
                "[the_girl.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                if the_girl.is_bald:
                    "Sensing that your slut is getting out of hand, you quickly take charge. You grab grab her by the troat an pull her head back until her hands are no longer on the ground, taking away all her leverage."
                else:
                    "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                $ the_girl.call_dialogue("surprised_exclaim")
                "You lean forward and whisper into [the_girl.possessive_title]'s ear."
                mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                if the_girl.has_role(anal_fetish_role):
                    "[the_girl.possessive_title] whimpers in total submission to you."
                    the_girl "I dream about it... I beg for it... It completes me! I'm not me unless your dick is deep in my ass [the_girl.mc_title]!"
                    $ play_moan_sound()
                    "You give her a couple slow, heavy thrusts before releasing her [the_girl.hair_description]. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                elif the_girl.obedience > 180 or the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.discover_opinion("being submissive")
                    if the_girl.get_opinion_score("being submissive") > 0:
                        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 2)
                        "For once, [the_girl.possessive_title] is speechless. She can only whimper softly in total submission to you."
                    else:
                        the_girl "I'm sorry [the_girl.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                    $ play_moan_sound()
                    "You give her a couple slow, heavy thrusts before releasing her [the_girl.hair_description]. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                else :
                    if the_girl.is_bald:
                        the_girl "Ah fuck! I can't breathe, take it a little easier, please!"
                    else:
                        the_girl "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return


label scene_doggy_anal_dildo_dp_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_girl "Ah... I feel so full!"
    "The dildo is clearly making the experience much more intense for her."
    "You reach forward and place your hands on [the_girl.possessive_title]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $the_girl.call_dialogue("sex_responses_anal")
    if the_girl.arousal_perc > 120:
        "[the_girl.possessive_title]'s pussy is now constantly convulsing in orgasm. Her juices are running out from around the dildo and down the inside of her legs."
        "With every quiver and every spasm, her buttery butthole contracts and squeezes your cock, begging you to cum for her."
    if the_girl.arousal_perc > 80:
        "[the_girl.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her pussy as a result of your rutting."
        the_girl "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_girl.possessive_title] seems to be enjoying the double penetration you are giving her. She yelps in response to one particularly eager thrust."
        the_girl "God dammit, you're so fucking big. You feel huge... I'm so full."
    if the_girl.get_opinion_score("masturbating") > 0:
        "You notice that [the_girl.possessive_title] now has one hand on her pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating") * 2)
    else:
        "[the_girl.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
        "You decide with her cheeks spread wide to see how deep you can get yourself into [the_girl.possessive_title]."
        "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]."
        "[the_girl.possessive_title] whimpers, her body now pinned between your body and [the_object.name]. The vibrating dildo stimulates her pussy mercilessly."
        if the_girl.has_role(anal_fetish_role):
            "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to try to milk your cock"
            "You enjoy her efforts before you speak clearly to her."
            mc.name "You are such a slut. Is it nice to finally have a real cock, stuffed deep in your tight little asshole?"
            "[the_girl.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled. The extra stimulation from the dildo just makes it even better."
            the_girl "Oh god it is. Every time I play with my ass and all I can think about is your big meaty dick buried inside me."
            "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
            mc.name "Don't worry, slut. This won't be the last time I stuff your holes. This one especially."
            "You give her prone body a forceful thrust."
            $ play_moan_sound()
            "You can see goosebumps all over [the_girl.possessive_title]'s skin. She moans and then begs you to keep fucking her."
            the_girl "I was made to be your little cock sleeve. Fuck me [the_girl.mc_title]!"
        elif the_girl.get_opinion_score("anal creampies") > 0:
            the_girl "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
            $mc.change_arousal(5)
            "In your mind, you play out the fantasy of cumming so deep in [the_girl.possessive_title]'s ass, even when you pull out not a drop of your seed leaks out."
            "You give the idea serious consideration. You can tell she would love it if you did."
        elif the_girl.get_opinion_score("anal sex") > 0:
            "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to milk your cock"
            "You lower your face down behind her head and whisper into her ear."
            mc.name "Mmm, so rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
            "You can see goosebumps all over [the_girl.possessive_title]'s skin. You wonder how many times you can make her cum before you blow your load."
            $ the_girl.change_slut(2)
        elif the_girl.sluttiness > 90:
            the_girl "Oh fuck, bury it in me [the_girl.mc_title]! I don't think I've ever felt so full..."
        else:
            "[the_girl.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best she can."
            the_girl "God [the_girl.mc_title] that is so intense... please just try to be gentle okay?"
        "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
        "After a minute or two of slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_girl.possessive_title]'s back, and she follows, getting on all fours again to resume your fucking."

    return


label scene_doggy_anal_dildo_dp_3(the_girl, the_location, the_object):
    "third scene here"





    return

label outro_doggy_anal_dildo_dp(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_anal")
    mc.name "Ah, I'm going to cum!"
    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her ass", "body"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        if mc.condom:
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum."
            "She gasps with every final thrust as you fill your condom, which is slowly expanding inside her to accommodate your seed."
            if the_girl.get_opinion_score("bareback sex") > 0:
                the_girl "Oh god, imagine if you weren't wearing that rubber thing... I could feel you filling me up!"
            else:
                the_girl "That's it, cum deep!"
            $ climax_controller.do_clarity_release(the_girl)
            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly. You condom is full of your potent seed."

            call post_orgasm_condom_routine(the_girl, doggy_anal_dildo_dp) from _call_post_orgasm_condom_routine_doggy_anal_dildo_dp
            return
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
        if the_girl.get_opinion_score("anal creampies") > 0:
            the_girl "Yes! Fill my ass with your cum!"
        $ the_girl.cum_in_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ doggy_anal_dildo_dp.redraw_scene(the_girl)
        if the_girl.sluttiness > 90:
            the_girl "Oh god it's so good. It doesn't matter which hole you do it in, I love it when you cum inside me."
        else:
            the_girl "Oh fuck, I can't believe I let you cum in my ass..."

        "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

    if the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as your blow your load all over her ass."
            "She holds still for you as you cover her with your sperm."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        if the_girl.get_opinion_score("being covered in cum") > 0:
            the_girl "Yes! Paint me with your sticky cum!"
        $ the_girl.cum_on_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ doggy_anal_dildo_dp.redraw_scene(the_girl)
        if the_girl.sluttiness > 90:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
    if the_choice == "Cum on her face":
        mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
        if mc.condom:
            "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. You pull your condom off as she turns around on gets on her knees in front of you."
        else:
            "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. She immediately turns around on gets on her knees in front of you."
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.sluttiness > 80:
            "[the_girl.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        $ climax_controller.do_clarity_release(the_girl)
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from her knees, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")
    return

label transition_doggy_to_doggy_anal_dp_taboo_break_label(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight pussy feels amazing, but you decide it is time to take things up another notch."
    "She groans as you pull out and reach for you backpack. She looks back, and her eyes go wide when you pull out your strap-on."
    the_girl "What... what is that for?"
    call transition_doggy_doggy_anal_dp(the_girl, the_location, the_object) from _call_transition_doggy_anal_doggy_anal_dp_taboo_break
    return

label transition_anal_doggy_to_doggy_anal_dp_taboo_break_label(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight asshole feels great, but you decide it is time to take things up a notch."
    "She groans as you pull out and reach for you backpack. She looks back, and her eyes go wide when you pull out your strap-on."
    the_girl "What... what is that for?"
    call transition_doggy_doggy_anal_dp(the_girl, the_location, the_object) from _call_transition_doggy_doggy_anal_dp_taboo_break
    return

label transition_anal_doggy_doggy_anal_dp(the_girl, the_location, the_object):
    call transition_doggy_doggy_anal_dp (the_girl, the_location, the_object) from _call_transition_doggy_doggy_anal_dp
    return

label transition_doggy_doggy_anal_dp(the_girl, the_location, the_object):
    mc.name "I'm gonna fuck both your holes at the same time."
    if the_girl.effective_sluttiness() > 95:
        the_girl "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl "Oh Jesus! I don't know..."
        mc.name "Hush. Don't worry, it'll fit."
    "[the_girl.possessive_title] waits patiently on all fours as you secure the strap-on. She arches her back and presents her ass."
    if the_girl.arousal_perc > 60:
        "Her pussy is already dripping with arousal. You line yourself up with her ass, while she reaches down and lines the dildo up with her pussy."
    else:
        "You line yourself up with her ass while [the_girl.possessive_title] reaches down and lines the dildo up with her pussy."
    if the_girl.has_anal_fetish:
        "Since she's craving anal sex so much, you give a firm push, filling up both her holes."
    else:
        "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 1 or the_girl.sex_skills["Anal"] > 2:
        the_girl "Oh my god! I'm so full... It's so good [the_girl.mc_title]!"
        $ the_girl.discover_opinion("anal sex")
    else:
        the_girl "Holy fuck! Go slow [the_girl.mc_title]. This is really intense..."
    return

label transition_default_doggy_anal_dildo_dp(the_girl, the_location, the_object):
    $ doggy_anal_dildo_dp.redraw_scene(the_girl)
    "[the_girl.possessive_title] gets on her hands and knees as you kneel behind her."
    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = doggy_anal_dildo_dp.position_tag, visible_enough = True, prefer_half_off = True)
    "You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_doggy_anal_dildo_dp(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = doggy_anal_dildo_dp.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_doggy_anal_dildo_dp(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = doggy.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside of her."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips back into you and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_doggy_anal_dildo_dp(the_girl, the_location, the_object):
    if the_girl.arousal_perc > 120:
        $ play_moan_sound()
        "[the_girl.possessive_title] has stopped being able to put together coherent sentences. She moans and gasps as yet another orgasm wracks her body."
        "You bury your cock deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly. The vibrations from the dildo intensify her orgasm."
        $ the_girl.have_orgasm()
        "Her body is now in a near constant state of orgasm. The constant quivering and her sexy moans are almost too much to bear."
        $ mc.change_arousal(10)
        the_girl "Oh fuck... fuck... yes!"
        return
    "[the_girl.possessive_title]'s tight back passage start to quiver, and suddenly tenses up."
    $ the_girl.call_dialogue("climax_responses_anal")
    "You bury your cock deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly. The vibrations from the dildo intensify her orgasm."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl "Don't stop... it still feels so good!"
    return

label taboo_break_doggy_anal_dildo_dp(the_girl, the_location, the_object):
    "She groans as you pull out and reach for you backpack. She looks back, and her eyes go wide when you pull out your strap-on."
    the_girl "What... what is that for?"
    call transition_doggy_doggy_anal_dp(the_girl, the_location, the_object) from _call_transition_doggy_doggy_anal_dp_default_taboo_break
    return
