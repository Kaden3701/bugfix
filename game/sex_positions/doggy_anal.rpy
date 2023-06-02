init:
    python:
        doggy_anal = Position(name = "Anal Doggy", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
            position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Anal",
            girl_arousal = 16, girl_energy = 14,
            guy_arousal = 22, guy_energy = 20,
            connections = [],
            intro = "intro_doggy_anal",
            scenes = ["scene_doggy_anal_1","scene_doggy_anal_2", "scene_SB_doggy_anal_1", "scene_SB_doggy_anal_2"],
            outro = "outro_doggy_anal",
            transition_default = "transition_default_doggy_anal",
            strip_description = "strip_doggy_anal", strip_ask_description = "strip_ask_doggy_anal",
            orgasm_description = "orgasm_doggy_anal",
            taboo_break_description = "taboo_break_doggy_anal",
            verb = "ass fuck",
            opinion_tags = ["doggy style sex","anal sex"], record_class = "Anal Sex",
            default_animation = blowjob_bob,
            associated_taboo = "anal_sex")

        list_of_positions.append(doggy_anal)

init 1:
    python:
        #Here is where you would put connections if they existed.
        doggy_anal.link_positions(doggy,"transition_stealth_doggy_anal_doggy")



label intro_doggy_anal(the_girl, the_location, the_object):
    mc.name "Get down on all fours, I want to fuck your tight ass."
    if the_girl.sex_skills["Anal"] > 3 or the_girl.get_opinion_score("anal sex") > 1:
        if the_girl.effective_sluttiness() > 90:
            if mc.condom:
                the_girl "Get inside of me and fuck my ass hard and deep!"
            else:
                the_girl "Get inside of me and fuck my ass raw!"
        else:
            the_girl "Okay, but take it slowly. I need some time to adjust..."
    else: #She's inexperienced and doesn't quite know what to do.
        if the_girl.effective_sluttiness() > 90:
            the_girl "Oh fuck, I want you inside me but I need you to go slowly."
        else:
            "[the_girl.possessive_title] looks worried for a moment."
            the_girl "I'll let you try, but I don't know if you'll be able to fit. I haven't done this much..."

    $ doggy_anal.redraw_scene(the_girl)
    "[the_girl.title] gets onto her hands and knees on the [the_object.name]. You spit into your hand and use it to lube up your cock, then line it up with her pretty little asshole."
    mc.name "Ready?"
    if the_girl.sex_skills["Anal"] > 3 or the_girl.get_opinion_score("anal sex") > 1:
        the_girl "Yes!"
    else:
        the_girl "No, but I don't know if I ever will be. Let's try it."
    "You hold onto her hips and push yourself in. She gasps as the tip of your cock slips into her ass."
    "[the_girl.title] grunts and gasps as you slowly fit your whole dick inside of her. When you bottom out you hold still, giving her time to adjust to your size."
    "After a long moment it seems like she's ready and you start to move, slowly at first then picking up speed."
    return

label taboo_break_doggy_anal(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You grab [the_girl.possessive_title]'s ass and give it a squeeze, then a hard slap."
    if the_girl.effective_sluttiness(doggy_anal.associated_taboo) > doggy_anal.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
        mc.name "Get on your knees, I want to get a look at this ass."
        $ the_girl.draw_person(position = "back_peek", the_animation = ass_bob)
        "She turns around and jiggles her butt playfully for you."
        the_girl "This big fat ass? You finally want to take a closer look?"
        mc.name "I said on your knees, come on."
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "She gets onto the [the_object.name] and points her butt in your direction. She lowers her shoulders and works her hips for you."

    else:
        mc.name "Get on your knees."
        $ the_girl.draw_person(position = "kneeling1")
        "She gets onto her knees in front of you."
        mc.name "Good girl, now spin around and show me that ass."
        "She nods and turns around."
        $ the_girl.draw_person(position = "doggy")
        mc.name "Nice. Now shake it for me."
        the_girl "Like... this?"
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.4)
        "[the_girl.title] works her hips and jiggles her ass for you."
        mc.name "Getting there, a little faster now."
        $ the_girl.draw_person(position = "doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "She speeds up."
    the_girl "Is that what you wanted?"
    "You slap your cock down on her ass and grab her tight cheeks, spreading them apart to get a look at her asshole."
    mc.name "Almost. I think it's time we stretched you open."
    $ the_girl.call_dialogue(doggy_anal.associated_taboo+"_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you press it against her tight hole."
    if the_girl.sex_skills["Anal"] > 3:
        "She gasps as your tip starts to spread her open. She lowers her shoulders and pushes her hips against you, helping the process."
        the_girl "Oh god... Mfphhhh!"

    else:
        "She gasps as your tip tries to spread open her impossibly tight asshole. She tries to pull away, but you pull on her waist and bring her closer."
        mc.name "Come on, you'll get there."
        "You spit onto your cock and try again. This time making better progress, sliding the tip of your dick into [the_girl.title]'s ass."
        the_girl "Oh god... Fuck!"
    "Inch by inch you slide your entire length into [the_girl.possessive_title]. She grunts and gasps the whole way down."
    "You stop when you've bottomed out, to give your cock time to properly stretch her out."
    the_girl "I think... I'm ready for you to move some more..."
    "You pull back a little bit and give her a few testing strokes. When she can handle those you speed up, until you're thrusting your entire length."
    return

label scene_doggy_anal_1(the_girl, the_location, the_object):

    "You hold onto [the_girl.title]'s hips and settle into a steady rhythm, sliding your cock in and out out of her tight ass."
    $ the_girl.call_dialogue("sex_responses_anal")

    if the_girl.has_large_tits and the_girl.tits_visible:
        "With each thrust [the_girl.title]'s large tits pendulum underneath her. You reach a hand around and grab one of them, squeezing it hard."
    else:
        $ play_spank_sound()
        "With each thrust [the_girl.title]'s ass shakes and jiggles. You give it a hard slap, making her yelp."

    return

label scene_doggy_anal_2(the_girl, the_location, the_object):
    $ play_moan_sound()
    if the_girl.sex_skills["Anal"] > 3:
        "[the_girl.title] works her hips back against you with each thrust, moaning happily to herself as your cock stretches out her asshole."
    else:
        "[the_girl.title] grunts and pants as your cock stretches out her asshole. Her hands ball into fists as she tries to adjust."

    "You reach forward and place your hands on her shoulders, pulling her against you with each stroke."
    $ the_girl.call_dialogue("sex_responses_anal")
    "Her ass squeezes down on your dick, so tight it's almost difficult to move."
    return

label scene_SB_doggy_anal_1(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You give [the_girl.possessive_title]'s ass a good hard spank. She lets out a loud yelp."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "[the_girl.possessive_title] reflexively starts to pull away after you spank her. You grab her hips to keep her from pulling off completely."
        the_girl "Sorry, I just... I don't do this very often... please just be gentle with me!"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out."
        "You decide to give her a little break in the intensity of your fucking. Leaving yourself deep inside her, you knead her ass cheeks with both hands."
        the_girl "Mmmm, that feels good [the_girl.mc_title]. Can I touch myself while you do that?"
        menu:
            "Masturbate for me":
                "Encouraged by your response, [the_girl.possessive_title] reaches down with one hand and begins to rub her clit."
                "You take it slow, and you revel in the delicious pleasure of each penetration as you thrust. [the_girl.possessive_title] struggles to hold herself up with one hand while the other works circles around her clit."
                if the_girl.get_opinion_score("masturbating") > 0:
                    "[the_girl.possessive_title] moves her fingers masterfully across her pussy. You can tell she masturbates often."
                    $ the_girl.discover_opinion("masturbating")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
                if the_girl.sluttiness > 90:
                    the_girl "I'm sorry [the_girl.mc_title], I'll try to get better at this. Having you in my ass is so intense..."
                else:
                    "[the_girl.possessive_title] seems to be enjoying the anal penetration a bit more now that she is touching herself."
            "Fuck me with your ass":
                if the_girl.obedience > 180 or the_girl.get_opinion_score("being submissive") > 0:
                    the_girl "Yes [the_girl.mc_title]. I'll do my best."
                else:
                    the_girl "I'll give it my best, but this better be worth it..."
                "[the_girl.possessive_title] slowly eases forward until just the tip remains inside, then slowly backs her ass back onto you. She is trying to obey but you can tell she is struggling to take you."
                "The next she starts to ease forward, you put your hand on her hips for a second to stop her. You spit into your hand then rub it along your shaft a bit, hoping it will make the penetration easier."
                the_girl "Mmm, that's a bit better..."
                "With the extra lube, [the_girl.possessive_title] resumes fucking you. She still has a fairy slow pace, but is a bit quicker than before."

    else:
        "In response to your spanking, [the_girl.possessive_title] thrusts herself back against you. Your penis is completely consumed by her bowel and she moans lewdly."
        "When she starts to pull off you give her other ass cheek a hard swat. She buries her face in [the_object.name] and moans as she pushes herself back onto you again."
        the_girl "Oh fuck [the_girl.mc_title], I needed this so bad. Don't stop, it feels so good when you go deep!"
        "[the_girl.possessive_title]'s ass feels so tight you are tempted to let her continue setting the pace, but you worry she might get the wrong idea if you let this little slut take charge."
        menu:
            "Fuck me with your ass":
                "You decide to see what [the_girl.possessive_title] can do if you let her take control of the pace. Encouraged by your words, she eagerly works your cock with her ass." ###FINISH
                the_girl "Mmm, does it feel good when I work it like this?"
                "[the_girl.possessive_title] begins to twerk up and down your shaft with quick, shallow movements."
                if mc.arousal_perc > 70:
                    mc.name "Damn that feels good. You're gonna make me cum if you keep that up. Where do you want my load?"
                    if mc.condom:
                        the_girl "Just shove it in deep and dump it right in my ass. You still have that condom on, right?"
                    elif the_girl.has_cum_fetish:
                        the_girl "Anywhere on my skin! My ass, my face, I don't care, just spray me down with it! With you know I need it like that!"
                    elif the_girl.get_opinion_score("anal creampies") > 0:
                        the_girl "You should just shove it in as deep as you can and cum inside me."
                    elif the_girl.get_opinion_score("being covered in cum") > 0:
                        the_girl "You should pull out and cum all over my ass. That would be so hot..."
                    elif the_girl.get_opinion_score("cum facials") > 0:
                        the_girl "Tell me when you are about to cum and I'll let you cum all over my face..."
                    elif the_girl.obedience > 180:
                        the_girl "Cum wherever you want to... I just want to please you, [the_girl.mc_title]."
                    else:
                        the_girl "I don't know... wherever you want I guess?"
                else:
                    mc.name "Wow, your ass is amazing. Where'd you learn to work it like that girl? Have you been practicing?"
                    if the_girl.has_role(anal_fetish_role):
                        "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                        the_girl "Practicing, dreaming, begging for your cock in my ass! Every moment my rear is empty I'm craving your dick deep inside it."
                        "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                        mc.name "Fuck [the_girl.title], I don't know how you do that, but it's amazing."
                        "[the_girl.possessive_title] sighs. She is truly addicted to getting her tight back passage fucked"
                    elif the_girl.get_opinion_score("anal sex") > 0:
                        "In response, she slams her ass all the way back on your dick. She grinds her hips left and right up against you."
                        "You can feel her tense and relax her muscles in her ass rhythmically, messaging your shaft while you remain totally engulfed inside her."
                        mc.name "Wow, I guess so! That feels amazing. Feel free to practice anytime you want on me, [the_girl.title]!"
                        "[the_girl.possessive_title] sighs. You can tell having your dick in her ass is very fulfilling for her."
                    else:
                        "[the_girl.possessive_title] looks back at you."
                        the_girl "Honestly, I'm not usually into butt stuff... but I just want to make you feel so good..."
                "[the_girl.possessive_title] continues to twerk her ass up and down on your penis. How does she make it look so easy?"
            "I'm in charge here":
                if the_girl.is_bald:
                    "Sensing that your slut is getting out of hand, you quickly take charge. You grab grab her by the troat an pull her head back until her hands are no longer on the ground, taking away all her leverage."
                else:
                    "Sensing that your slut is getting out of hand, you quickly take charge. You grab her by the hair and pull her head back until her hands are no longer on the ground, taking away all her leverage."
                $ the_girl.call_dialogue("surprised_exclaim")
                "You lean forward and whisper into [the_girl.possessive_title]'s ear."
                mc.name "I know you dream about my dick in your ass constantly and it feels good to finally have that dream come true, but don't forget who is in charge around here."
                if the_girl.obedience > 180 or the_girl.get_opinion_score("being submissive") > 0:
                    $ the_girl.discover_opinion("being submissive")
                    if the_girl.get_opinion_score("being submissive") > 0:
                        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                        "For once, [the_girl.possessive_title] is speechless. She can only whimper softly in total submission to you."
                    else:
                        the_girl "I'm sorry [the_girl.mc_title], I couldn't help myself. Please use me however you want, I'll be good I promise!"
                    if the_girl.is_bald:
                        "You give her a couple slow, heavy thrusts before releasing your grip. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                    else:
                        "You give her a couple slow, heavy thrusts before releasing her hair. She returns her hands to the ground and moans when you resume your slow, methodical fucking."
                        $ play_moan_sound()
                else:
                    if the_girl.is_bald:
                        the_girl "Ah fuck! I can't breathe, take it a little easier, please!"
                    else:
                        the_girl "Okay! Geesh! Be careful with my hair, that hurts!"
                #TODO this option is kinda boring... expand some?

    return

label scene_SB_doggy_anal_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] lowers her shoulders against the [the_object.name] and groans as you fuck her from behind."
    the_girl "Ah... I feel so full!"
    "You reach forward and place your hands on [the_girl.possessive_title]'s shoulders. With each thrust you pull her back onto you forcefully, your hips smacking her ass cheeks loudly. She arches her back and lets out a series of satisfied yelps."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.arousal_perc > 80:
        "[the_girl.possessive_title]'s pussy is dripping wet. A damp spot has begun to accumulate below her [the_girl.pubes_description] pussy as a result of your rutting."
        the_girl "Ohhh, you feel so fucking good in my ass."
    else:
        "[the_girl.possessive_title] seems to be enjoying the fucking you are giving her. She yelps in response to one particularly eager thrust."
        the_girl "God dammit, you're so fucking big. You feel huge in my ass."
    if the_girl.get_opinion_score("giving handjobs") > 0:
        "[the_girl.possessive_title] reaches down and begins to stroke and rub your scrotum with one hand, while with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("giving handjobs"))
    elif the_girl.get_opinion_score("masturbating") > 0:
        "You notice that [the_girl.possessive_title] now has one hand on her [the_girl.pubes_description] pussy, rubbing her clit, and with the other hand she reaches back and pulls her ass cheeks apart."
        $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
    else:
        "[the_girl.possessive_title] reaches back with both hands and spreads her ass cheeks apart."
    "With her ass cheeks spread, you consider for a moment, should you pull back and admire the view, or shove yourself down deep?"
    menu:
        "Admire her ass":
            "You pull yourself out of [the_girl.possessive_title]'s ass for moment and admire the soft, round cheeks of carnal pleasure in front of you."
            "Her asshole gapes a bit from your sudden pullout, and she quickly turns her head to see why she suddenly feels so empty."
            "[the_girl.possessive_title] realizes you are taking a moment to check out her backside."
            if the_girl.get_opinion_score("showing her ass") > 0:
                the_girl "Do you like my ass, [the_girl.mc_title]? I've caught you checking it out before. It gets me so hot when I feel your eyes checking out my backside..."
                $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))###
                $ the_girl.discover_opinion("showing her ass")
                "[the_girl.possessive_title] moves her ass side to side, gyrating her hips for you while keeping her ass cheeks spread wide."
            elif the_girl.get_opinion_score("being covered in cum") > 0:
                the_girl "Do you like what you see, [the_girl.mc_title]? I bet it is going to look even more amazing covered in your hot cum."
                $mc.change_arousal(5)
                "The thought of painting [the_girl.possessive_title]'s ass with your semen makes your cock twitch in anticipation."
            elif the_girl.sluttiness > 80:
                the_girl "Hey, you can check my ass out later, right now you're supposed to be fucking it, [the_girl.mc_title]!"
                "[the_girl.possessive_title] tries to push herself back on to you, but from her angle she is unable to get you to penetrate her again unless you help."
                "She quickly gives up an resorts to rubbing her ass up and down along the length of your penis."
            elif the_girl.obedience > 180:
                "[the_girl.possessive_title] blushes. The conflict of the dirtiness of the act of anal sex and her obedience to you are clear in her face."
                the_girl "[the_girl.mc_title]... don't you find my ass pleasing? Why did you pull out?"
                mc.name "Don't worry, [the_girl.title], I'll fuck your ass some more in a second, I just needed to take a moment and how loose your backdoor has gotten so far."
                $ the_girl.change_slut(2)
                "[the_girl.possessive_title]'s cheeks turn even redder with your dirty talk. She puts her head down again, but leaves her cheeks spread, ready for you to resume fucking her whenever you are ready."
            else:
                the_girl "Hey, why'd you pull out? I was just getting used to how thick you are..."
            "After taking a moment appraising [the_girl.possessive_title]'s buttocks, you decide to get back to the act."
            "With gentle pressure, you slowly fill her ass with your erection again. [the_girl.possessive_title] groans as you resume your thrusting."
        "Shove it in deep":
            "You decide with her cheeks spread wide to see how deep you can get yourself into [the_girl.possessive_title]."
            "With her hands busy, she has no way of holding up your weight as you push yourself forward and then down on top of her, your full body weight pushing her prone down onto the [the_object.name]."
            "[the_girl.possessive_title] whimpers, her body now pinned between your body and [the_object.name]."
            if the_girl.has_role(anal_fetish_role):
                "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to try to milk your cock."
                "You enjoy her efforts before you speak clearly to her."
                mc.name "Does this feel better than that plug? Is this what you're imagining every time you push that plug up your ass?"
                "[the_girl.possessive_title] is writhing in pleasure, having her fetish of anal sex fulfilled."
                the_girl "Oh god it is. Every time I play with my ass and all I can think about is your big meaty dick buried inside me."
                if the_girl.is_bald:
                    "You lock her throat in your elbow and pull her head back before whispering into her ear."
                else:
                    "You grab her hair at the base of her scalp and pull her head back before whispering into her ear."
                mc.name "Don't worry, slut. This won't be the last time I fill your ass with my cock."
                $ play_moan_sound()
                "You can see goosebumps all over [the_girl.possessive_title]'s skin. She moans and then begs you to keep fucking her."
            elif the_girl.get_opinion_score("anal creampies") > 0:
                the_girl "Holy hell that is deep... tell me... tell me you'll push it this deep again when you cum... that would be so hot!"
                $mc.change_arousal(5)
                "In your mind, you play out the fantasy of cumming so deep in [the_girl.possessive_title]'s ass, even when you pull out not a drop of your seed leaks out."
                "You give the idea serious consideration. You can tell she would love it if you did."
            elif the_girl.get_opinion_score("anal sex") > 0:
                "Despite having no leverage, [the_girl.possessive_title] wriggles her ass against you as best she can. Even with no room to move, her love for anal sex drives her to milk your cock."
                "You lower your face down behind her head and whisper into her ear."
                mc.name "Mmm, so rear entry is how you like it, slut? Don't worry, this won't be the last time you feel my cock ravage your back door."
                "You can see goosebumps all over [the_girl.possessive_title]'s skin. You wonder how many times you can make her cum before you blow your load."
                $ the_girl.change_slut(2)
            elif the_girl.sluttiness > 80:
                the_girl "Oh fuck, bury it in me [the_girl.mc_title]! I don't think I've ever felt so full..."
            else:
                "[the_girl.possessive_title] lets out a loud groan. You can tell she isn't used to being penetrated like this, but she is taking it as best she can."
                the_girl "God [the_girl.mc_title] that is so intense... please just try to be a little more gentle okay?"
            "You take a few seconds to enjoy being engulfed by her back passage, then give her a few slow, probing thrusts."
            "After a minute or two of slow, deep thrusts you decide to move back to doggy. You push yourself up off of [the_girl.possessive_title]'s back, and she follows, getting on all fours again to resume your fucking."

    return

label outro_doggy_anal(the_girl, the_location, the_object):
    "Fucking [the_girl.possessive_title]'s tight asshole feels amazing, and you come closer and closer to your climax."
    "You pass the point of no return and speed up, slamming your cock into her with each thrust."
    $ the_girl.call_dialogue("sex_responses_anal")
    mc.name "Fuck, here I cum!"
    $ climax_controller = ClimaxController(["Cum inside of her", "anal"],["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        if stealth_orgasm:  #You sly dog
            "You know you should probably pull out after pulling the condom off, but you can't. You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside her bowels as you cum."
            the_girl "Oh god, you are cumming so hard, I swear I can feel your cum inside of me!"
            $ the_girl.cum_in_ass()
            $ doggy_anal.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "After you finish, you leave your cock deep inside her, while her contractions start pushing your dick and cum out of her."
            "[the_girl.title] reaches between her butt cheeks, realizing you just finished inside her ass."
            if the_girl.has_role(prostitute_role):
                the_girl "What the FUCK? You took the condom off? And then came inside me!?! I know I'm just a working girl, but you can't treat me like this."
                $ the_girl.change_stats(happiness = -5, obedience = 3, love = -5) #She loses trust
            elif the_girl.get_opinion_score("anal creampies") > 0:         #She likes anal creampies...
                the_girl "Wait... that's... you took the condom off, didn't you? Oh fuck that's why it felt so good!"
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Oh god, that's so hot! I love feeling cum deep inside me."
                $ the_girl.change_stats(happiness = 2, obedience = 3)
                # she liked it, so skip condom in next loops
                $ use_condom = False
            elif the_girl.sluttiness > 80:                          #She is slutty enough she doesn't mind the cream filling
                the_girl "Oh my god you took the condom off? You know you can cum inside me anytime you want, no need to be stealthy about it!"
                menu:
                    "Agree":
                        mc.name "I like the sound of that."
                        $ use_condom = False
                    "Don't":
                        mc.name "I was just checking how far you were willing to go."
                $ the_girl.change_obedience(3)
            else:                                                   #She gets pissed
                the_girl "What the FUCK? You took the condom off? And then came inside me!?! You asshole!"
                $ the_girl.change_stats(happiness = -5, obedience = 3, love = -5) #She loses trust
                "You came inside [the_girl.possessive_title]'s ass, but it is clear she isn't happy about it."
            "You slowly pull out of [the_girl.title]'s bowels while your cum drips down her butt and legs."
        else:
            "You push yourself balls deep into [the_girl.title]'s ass and dump your load."
            $ climax_controller.do_clarity_release(the_girl)
            "You hold yourself inside of her until your climax has passed, then pull out slowly and sit back."
            if mc.condom:
                "She is left on her hands and knees, trying to catch her breath, giving you a perfect view of her gaping ashole."
            else:
                "She is left on her hands and knees, trying to catch her breath, as your cum drips out of her gaping asshole."
            $ the_girl.cum_in_ass()
            $ doggy_anal.redraw_scene(the_girl)
            if not mc.condom and the_girl.get_opinion_score("anal creampies") > 0:
                # If she's into both...
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Oh fuck... I'm so full of cum. Put it back in me."
                mc.name "What?"
                the_girl "Your cock, put it back in me... Just a little bit more, please!"
                "She lowers her shoulders to the [the_object.name] and wiggles her ass at you. You slide the tip of your still-hard dick into her asshole."
                the_girl "Ah..."
                "Your semen gives you the lubrication you need to slide into her smoothly and easily. She shivers with pleasure as you push yourself in balls deep."
                the_girl "Just... hold it there. Mphfhhh."
                $ play_moan_sound()
                "She bites her lip, closes her eyes, and moans."
                "Eventually your dick starts to soften and you pull out."


            else:
                the_girl "Wow, that was intense. I hope you didn't stretch me out too badly."

    elif the_choice == "Cum on her ass":
        "You pull out of [the_girl.possessive_title]'s asshole, leaving it gaping while you stroke yourself to completion."
        if the_girl.sex_skills["Anal"] <= 2:
            "She sighs in relief as you pull out."
            the_girl "Oh thank god..."

        "You grunt and climax, shooting your hot cum out onto [the_girl.title]'s back and ass."
        $ the_girl.cum_on_ass()
        $ doggy_anal.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.effective_sluttiness() > 90:
            the_girl "Aw, I feel so empty now. You should have filled my ass with your cum instead."
        else:
            the_girl "Mmm, it's so warm."

    $ stealth_orgasm = False
    return

label transition_stealth_doggy_anal_doggy(the_girl, the_location, the_object):
    #transition from anal to normal doggy style.
    $ stealth_orgasm = False

    "You pull out of [the_girl.title]'s asshole, leaving it gaping and her sighing in relief."
    "You shift your cock downwards and rub the tip of it along the slit of her vagina."

    if the_girl.effective_sluttiness() < the_girl.get_no_condom_threshold():
        the_girl "Mmm, fuck me [the_girl.mc_title]. Use all of my holes for your pleasure!"
    elif not mc.condom:
        if the_girl.on_birth_control:
            the_girl "Wait, please put on a condom, I feel safer that way."
        else:
            the_girl "Wait, wait... I can't risk getting pregnant, I need you to put on a condom."
        menu:
            "Put on a condom":
                "You pull your dick back and quickly put on a condom. Then you line up your dick with her dripping wet pussy."
                $ mc.condom = True
            "Ram it home!":
                mc.name "Don't worry, I'll pull out."
                $ the_girl.change_happiness(-5)
        the_girl "Mmm, fuck me [the_girl.mc_title]. Use all of my holes for your pleasure!"

    "You pull on her hips and thrust yourself inside her tight, wet pussy."
    return

label transition_anal_doggy_to_doggy_taboo_break_label(the_girl, the_location, the_object):
    the_girl "Are you enjoying pounding my tight asshole?"
    "You slide your cock out of her ass and drag it down between her legs, ending with your tip resting against her pussy."
    mc.name "No, this is what I really want."
    $ the_girl.call_dialogue(doggy.associated_taboo+"_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
    "After a moment of resistance your cock spreads her [the_girl.pubes_description] pussy open and you slide smoothly inside of her."
    if the_girl.sex_skills["Vaginal"] > 2:
        the_girl "Oh god yes... keep sliding that monster into me..."
        "You ram your whole length into her wet pussy and start pounding her."
    else:
        the_girl "Oh god... take it slow..."
        "You give her short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
    return

label transition_default_doggy_anal(the_girl, the_location, the_object):
    $ doggy_anal.redraw_scene(the_girl)
    "[the_girl.title] gets on her hands and knees as you kneel behind her. You bounce your hard shaft on her ass a couple of times before lining yourself up with tight asshole."
    mc.name "Ready?"
    the_girl "I... I think so."
    "You hold onto her hips and push forward, spreading her ass with your large cock. She gasps and balls her fists, until finally you've buried your shaft in her."
    "After giving her a second to acclimatize you start to thrust in and out, slowly at first but picking up speed."
    return

label strip_doggy_anal(the_girl, the_clothing, the_location, the_object):
    "[the_girl.title] leans forward, pulling your cock out of her."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = doggy.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    "You line your cock back up with her ass and slide back in, a little easier than the first time now that it's been stretched out."
    return

label strip_ask_doggy_anal(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], what do you think of me taking off my [the_clothing.name]?"
    "[the_girl.title] pants as you fuck her ass from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = doggy.position_tag)
            "She leans forward and pops off your dick. [the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "When she's ready you line your cock back up with her asshole and slide back in, a little easier than the first time now that it's been stretched out."
            return True

        "Leave it on":
            mc.name "No, I want you to keep it on."
            if the_girl.sluttiness < 60:
                the_girl "Do I look sexy in it? Does it turn you on?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                "She pushes her hips back into you and grinds against you."
            else:
                the_girl "Does it look good on me, when you're fucking my ass? When you're stirring up my insides with your big cock?"
                "She pushes her hips back into you and grinds against you."
            return False
    return

label orgasm_doggy_anal(the_girl, the_location, the_object):
    $ play_moan_sound()
    "[the_girl.title]'s grunts and pants turn to moans of pleasure."
    $ the_girl.call_dialogue("climax_responses_anal")
    "She balls her fists and tenses up, her whole body quivering as she cums."
    "You fuck her ass through her climax, making her moan and pant with each thrust. After a few seconds it passes and she relaxes."
    the_girl "Oh god, keep fucking me [the_girl.mc_title]!"
    return
