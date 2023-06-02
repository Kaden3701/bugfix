init python:
    bent_over_breeding = Position(name = "Breeding Doggy", slut_requirement = 60, slut_cap = 100, requires_hard = True, requires_large_tits = False,
        position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "Vagina", skill_tag = "Vaginal",
        girl_arousal = 18, girl_energy = 14,
        guy_arousal = 20, guy_energy = 16,
        connections = [],
        intro = "intro_bent_over_breeding",
        scenes = ["scene_bent_over_breeding_1","scene_bent_over_breeding_2", "scene_bent_over_breeding_3"],
        outro = "outro_bent_over_breeding",
        transition_default = "transition_default_bent_over_breeding",
        strip_description = "strip_bent_over_breeding",  strip_ask_description = "strip_ask_bent_over_breeding",
        orgasm_description = "orgasm_bent_over_breeding",
        taboo_break_description = "taboo_break_bent_over_breeding",
        verb = "fuck",
        opinion_tags = ["doggy style sex", "vaginal sex", "sex standing up", "bareback sex"], record_class = "Vaginal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "condomless_sex")



label intro_bent_over_breeding(the_girl, the_location, the_object):
    $ the_girl.draw_person(position = bent_over_breeding.position_tag)
    "You turn [the_girl.possessive_title] around, and she leans over [the_object.name], presenting her ass to you."
    if mc.condom:
        "She notices you are wearing a condom."
        the_girl "Hey, get that dumb rubber off! If you're gonna breed me you need to go in bare!"
        "You quickly pull the condom off and throw it to the side."
        $ mc.condom = False
    mc.name "Good girl, [the_girl.title], I'm going to fuck you hard and fill you up with my seed."
    if the_girl.get_opinion_score("doggy style sex") > 2 :
        the_girl "Oh thank god, I've been daydreaming about you bending me over all day long."
    elif the_girl.get_opinion_score("sex standing up") > 2 :
        the_girl "Oh thank god, I've been daydreaming about this all day long."
    else:
        the_girl "Oh thank god, I've been daydreaming about getting filled up all day long."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = bent_over_breeding.position_tag, visible_enough = True, prefer_half_off = True)

    if the_girl.arousal_perc > 60:
        $ play_moan_sound()
        "You rub the tip of your cock against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. She moans, anticipating your penetration."
        "You continue to rub your dick against her [the_girl.pubes_description] pussy and gather more of her juices. She is already so wet you are soon slick with her secretions."
    else:
        "You rub the tip of your cock against [the_girl.possessive_title]'s cunt."
    "When you're ready you push forward. Her pussy feels amazing wrapped around your erection."
    if the_girl.get_opinion_score("doggy style sex") > 0 :
        the_girl "Oh my god..."
        $ the_girl.discover_opinion("doggy style sex")
    if the_girl.get_opinion_score("sex standing up") > 0 :
        "Her legs shake a bit as she gets used to the depth of your penetration."
        $ the_girl.change_arousal(the_girl.get_opinion_score("sex standing up"))
        $ the_girl.discover_opinion("sex standing up")
    return

label scene_bent_over_breeding_1(the_girl, the_location, the_object):
    "Your hips slap against [the_girl.possessive_title]'s ass as you fuck her vigorously."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    if the_girl.sex_skills["Vaginal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl.possessive_title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl "I'm sorry [the_girl.mc_title], that's a little too rough. Can you go a little slower?"
        "You pull her hips back toward you slowly. She sighs, still trying to get accustomed to your girth, penetrating her at such a deep angle."
        "The next time you push yourself in you push a little faster. She seems to be adapting to your fucking."
    elif the_girl.has_role(breeding_fetish_role):          #breeding fetish
        $ play_moan_sound()
        "After a particularly hard thrust, [the_girl.possessive_title] moans lewdly."
        the_girl "That's it, fuck me harder! Fill me up so full your seed is spilling out, then fill me up again!"
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.possessive_title] rocks her hips side to side each time you slam into her. Each time you pull back you can see her labia clinging to you."
        "You use both hands to grab her hips and slam yourself into her as deep as you can go."
        $ play_spank_sound()
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    else:
        $ play_moan_sound()
        "Fucking her hard, [the_girl.possessive_title] moans, matching each hip movement of yours with a movement of her own."
        the_girl "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.possessive_title] reaches back with one hand and pulls her ass cheek back, giving you a great view of her pussy stretched wide to accommodate you."
        $ play_spank_sound()
        "Buried deep inside, you give her ass a smack. Her pussy trembles and caresses you in response."
    menu:
        "Spank her":
            $ ass_desc = spanking_get_ass_description(the_girl)
            "You look down at [the_girl.possessive_title]'s ass. It is [ass_desc]"
            $ play_spank_sound()
            "With your erection buried deep inside her, you give her ass a firm spank. Her sexy cheeks quake in response."
            $ spank_factor_increment(the_girl)
            mc.name "[the_girl.title], your ass looks amazing when I spank it. You are such a slut. I bet you love it don't you?"
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 180:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans at your words."
                $ play_spank_sound()
                "You pull her ass cheeks apart. You give her a hard spank with your other hand and enjoy the feeling of her silky cunt."
                mc.name "Do you let any guy with a hard cock fuck you and spank you like this? Or just me?"
                "[the_girl.possessive_title] responds quietly."
                if the_girl.get_opinion_score("being submissive") > 0 and not the_girl.can_be_spanked:
                    the_girl "Just you! I love it when you get rough with me, and spank me when I've been naughty!"
                    "She really seemed to enjoy her spanking. Maybe you should work it into your normal foreplay..."
                    $ the_girl.unlock_spanking()
                else:
                    the_girl "Just you, [the_girl.mc_title]. I don't know why but it just feels so good... so right when you dominate me..."
                if the_girl is mom:
                    the_girl "It makes [the_girl.title] so happy to serve you like this... To be [the_girl.possessive_title]!"
                "You give her pussy a few rough thrusts before bottoming out again."
                mc.name "That's right bitch, you're my little fuckhole. I'll bend you over and fuck you anytime I please."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 2)
            else:
                the_girl "Mmm, it feels good but kinda hurts... could you hit a little more softly?"
                "You give her plaint ass another swat, this time not quite as hard."
                "Her ass quivers slightly as you spank her. Her pussy clenches around you each time you spank her."
            if mc.arousal_perc > 70:
                "[the_girl.possessive_title]'s tight pussy feels so good. You are getting close to cumming."
                mc.name "You feel amazing. You're gonna make me cum soon."
                "[the_girl.title] throws her ass back against you hard, forcing you deep."
                the_girl "You better put it in deep! I need your seed planted as deep as it will go!"
                "You grab her hips and take control back, resuming fucking her."
                mc.name "Don't worry bitch, you'll get it when it's time."
            "You put your hands on her hips and continue fucking her."

        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.get_opinion_score("being fingered"):
                $ play_moan_sound()
                "[the_girl.possessive_title] moans loudly in response."
                the_girl "Oh [the_girl.mc_title], I love when you touch me there."
                "You slide your fingers around her slit a few times."
                "You give your hips a few long, slow strokes as your circle her clit with your fingers."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                "She really enjoys the extra stimulation."
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            elif mc.sex_skills["Foreplay"] > 4:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."

            else:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
            if the_girl.arousal_perc > 90:
                the_girl "Oh fuck! Don't stop! Don't you dare stop!"
                $ play_moan_sound()
                "Her moans clearly indicate an impending orgasm. As best you can, you fuck her while you roughly rub her clit."
            else:
                "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her."
    return


label scene_bent_over_breeding_2(the_girl, the_location, the_object):
    "You take a breather, and then slowly start bringing the pace back up a bit."
    if the_girl.tits_available:
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you fuck her saturated slit."
    else:
        $ play_spank_sound()
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you fuck her saturated slit."

    if the_girl.arousal_perc > 80:
        the_girl "Ohhh, [the_girl.mc_title]... You are gonna make me cum so hard..."
        "You can feel a slight quiver in [the_girl.possessive_title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.possessive_title] groans in response to one particularly deep thrust."
        the_girl "It's so big... it feels so good buried inside me. I can't wait to feel it pulse and twitch when you cum!"
    "You push yourself in as deep as you can go. [the_girl.possessive_title] moans as you fill her completely."
    menu:
        "Gentle Sex":
            "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
            mc.name "[the_girl.title], your pussy is so good. I love how eager you are to be my cum dumpster."
            if the_girl.has_role(breeding_fetish_role):
                the_girl "I love being your mare! Fuck me good [the_girl.mc_title]!"
            elif the_girl.sluttiness > 80:
                the_girl "Of course I'm eager. Your cock fills me just right. Fuck me good [the_girl.mc_title]!"
            else:
                the_girl "Mmm, I can't help it, you make me feel so good."
        "Rough Sex":
            if the_girl.is_bald:
                "You take one hand and start to knead the back of her scalp. You grab her throat and pull."
            else:
                "You take one hand and start to knead the back of her scalp. You grab a fistful of hair and pull."
            "[the_girl.possessive_title] arches her back in response."
            mc.name "That's a good slut. Take it nice and deep."
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 180:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans enthusiastically."
                the_girl "[the_girl.mc_title]! I love it deep. Fuck me good!"
                "[the_girl.possessive_title] begs you for more."
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(2 * the_girl.get_opinion_score("being submissive"))
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans."
                the_girl "You are so deep... It feels good having you so deep inside me."
                "You stir the depths of her pussy with your erection by moving your hips side to side."

    return

label scene_bent_over_breeding_3(the_girl, the_location, the_object):
    if the_girl.body_is_thin:
        "Your hips begin to slap up against [the_girl.possessive_title]'s gloriously fit ass."
        "Her cheeks are tight from the exercise and care she puts into her body."
    elif the_girl.body_is_average:
        "Your hips begin to slap up against [the_girl.possessive_title]'s delicious ass."
        "Her cheeks are round but firm with just a hint of quaking with each impact."
    elif the_girl.body_is_thick:
        "Your hips begin to slap up against [the_girl.possessive_title]'s thick ass."
        "Her cheeks are full and generous, and they quake back and forth enticingly as you pound her."
    elif the_girl.body_is_pregnant:
        "Your hips begin to slap up against [the_girl.possessive_title]'s wide ass."
        "Her cheeks make a pleasing heart shape since her body has been changing with the baby growing in her belly."
    else:
        "Your hips begin to slap up against [the_girl.possessive_title]'s ass."
        "Her cheeks respond delightfully with each thrust."
    "[the_girl.title] is thrusting back against you, using the [the_object.name] as leverage to push herself back. Her ass is mesmerising."
    menu:
        "Finger her ass":
            "You decide to give her ass a little extra attention. You work up some saliva in your mouth then pause fucking her for a second."
            the_person "Hey... why did you stop?"
            "Instead of answering, you let the saliva drop from your mouth onto her crack. She feels it and realizes what you are about to do when you start to work it into her crack with your finger."
            if the_girl.get_opinion_score("anal sex") > 1:
                "[the_girl.possessive_title] bucks her hips slightly as you start to push your finger into her tight back passage. Her back arches in pleasure."
                the_girl "Mmm! [the_girl.mc_title] that feels so good."
                $ the_girl.discover_opinion("anal sex")
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") + mc.sex_skills["Anal"])
                "You slowly give her a long, deliberate stroke, pushing your cock and finger into her at the same time."
                "With your shaft buried inside her, you start to stroke yourself with your finger in her ass. An odd but very pleasurable feeling."
                "[the_girl.title] starts to get impatient and begins to move her hips forward and back. It feels so good, soon you are matching her."
                "You speed up and start to really pound her, her moans increasing in pitch from the double penetration."
                "Soon though, you feel the urge to really give it to her, so you pull your finger out so you can grab both her hips and fuck her rough."

            elif the_girl.get_opinion_score("anal sex") < 0:
                the_girl "WHOA! Hey I'm not really into that..."
                "She starts to pull away from you."
                "It seems that [the_girl.possessive_title] doesn't like having her ass played with."
                $ the_girl.discover_opinion("anal sex")
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "You quickly mumble an apology. Instead of fingering her, you grab her hips with both hands and start to pound her."
            else:
                "[the_girl.possessive_title] tenses slightly as you start to push your finger into her back passage, but otherwise doesn't resist."
                the_girl "Go slow... I don't let just anyone touch me like this..."
                "She forces herself to relax. You can feel her rectum physically unclench, and you begin to slowly move your finger in and out of her."
                the_girl "That feels good [the_girl.mc_title]... just be careful with me back there!"
                "As you finger her ass, her hips remain stationary. She wills herself to relax, and manages to enjoy the stimulation."
                $ the_girl.change_arousal(mc.sex_skills["Anal"])
                "Soon though, you feel the urge in your hips to start fucking her again, so you pull your finger out so you can grab both her hips."
        "Grope her ass":
            "Your hands are drawn to her cheeks. With a soft touch you trace your finger down around their delicious curve."
            "You grab a handful, her ass flesh feels tight and full in your hand. She moans and you give her a couple vigorous thrusts."
            mc.name "Your ass is amazing. Maybe I'll fuck you back there next..."
            $ play_moan_sound()
            "She moans and pushes back against you as you fuck."
            the_girl "You can fuck me anywhere, just promise you'll cum in my pussy!"
    return


label outro_bent_over_breeding(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    "[the_girl.possessive_title]'s drenched cunt is just too good. You decide to cum inside it."
    if mc.condom:
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps when she feels you filling the condom deep inside of her."
        the_girl "Oh god, I can feel you twitching... but something is missing?"
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        "You wait until your orgasm has passed completely, then pull out and sit back. Your condom is bulged on the end where it is filled with your seed."
        "She looks at your condom and frowns."
        the_girl "You were... seriously? You had a condom on? Why would you do that?"
        "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
    else:
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."

        if the_girl.wants_creampie:
            the_girl  "Yes! Fill me with your cum!"
        $ the_girl.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        $ bent_over_breeding.redraw_scene(the_girl)
        if the_girl.has_breeding_fetish:
            "[the_girl.possessive_title] pushes herself back tightly against you, forcing your cum as deep as she can."
            the_girl "Yes! Yes I needed this so bad! Fill me up! Oh god it's so good..."
            "[the_girl.possessive_title] revels in having her breeding fetish fulfilled."
        elif the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
            the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
            "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
        if the_girl.knows_pregnant:
            the_girl "It's nice, already being pregnant, I can take a load like that anytime..."
        elif the_girl.wants_creampie:
            the_girl "Oh god... I can feel it so deep. I mean... it could... hopefully..."
            "[the_girl.possessive_title]'s voice starts to trail off."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god it's so deep."
        elif the_girl.on_birth_control:
            the_girl "Oh fuck...  Good thing I'm on the pill..."
        else:
            the_girl "Oh fuck... I could get pregnant you know.."

        "You wait until your orgasm has passed completely, then pull out and stand back."
        "Your cum leaks out of her dripping wet [the_girl.pubes_description] pussy."


    return

label transition_default_bent_over_breeding(the_girl, the_location, the_object):
    mc.name "Stand here."
    $ bent_over_breeding.draw_scene(the_girl)
    "[the_girl.possessive_title] obeys then leans forward and puts her hands on [the_object.name]."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = bent_over_breeding.position_tag, visible_enough = True, prefer_half_off = True)
    "You bounce your hard shaft on her ass a couple of times before sliding your cock between her thighs."
    "You continue your back and forth motion, rubbing your cock along her pussy lips."
    if mc.condom:
        "You quickly pull the condom off and throw it to the side."
        $ mc.condom = False
    mc.name "Get ready, I'm going to breed you, bent over this [the_object.name], right now."
    if the_girl.knows_pregnant:
        the_girl "That sounds hot, but I'm already pregnant?"
        mc.name "I know, but that doesn't mean we can't practice. A good mare is always full of cum."
        the_girl "Oh god, okay! I'm ready for it!"
    else:
        the_girl "Oh god, okay! I'm ready for it!"
    if the_girl.has_taboo("vaginal_sex"):
        $ the_girl.call_dialogue(doggy.associated_taboo+"_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
        "After a moment of resistance your cock spreads her pussy open and you slide smoothly inside of her."
        the_girl "Oh god... Ah..."
        "You start with short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
        $ the_girl.break_taboo("vaginal_sex")
    else:
        "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_bent_over_breeding(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  bent_over_breeding.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_bent_over_breeding(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = bent_over_breeding.position_tag)
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
                the_girl "Does it make me look like the cum hungry slut that I am? Or is it your cock inside me that makes me look that way?"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_bent_over_breeding(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "You bury your cock deep in [the_girl.possessive_title]'s cunt while she cums. Her pussy spasms around you."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("doggy style sex") > 0:
        the_girl "Oh god, you've got me bent over and it feels so good I'm just cumming all over you..."
    the_girl "Don't stop... it still feels so good!"
    return

label taboo_break_bent_over_breeding(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return
