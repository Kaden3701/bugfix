# Added gag her with your fingers (original idea by BadRabbit)

init python:
    anal_standing = Position(name = "Standing Anal", slut_requirement = 70, slut_cap = 95, requires_hard = True, requires_large_tits = False,
        position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "Vagina", skill_tag = "Anal",
        girl_arousal = 20, girl_energy = 16,
        guy_arousal = 18, guy_energy = 16,
        connections = [],
        intro = "intro_anal_standing",
        scenes = ["scene_anal_standing_1","scene_anal_standing_2"],
        outro = "outro_anal_standing",
        transition_default = "transition_default_anal_standing",
        strip_description = "strip_anal_standing",  strip_ask_description = "strip_ask_anal_standing",
        taboo_break_description = "taboo_break_anal_standing",
        orgasm_description = "orgasm_anal_standing",
        verb = "ass fuck",
        opinion_tags = ["doggy style sex", "anal sex", "sex standing up"], record_class = "Anal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "anal_sex")

    list_of_positions.append(anal_standing)

init 1 python:
    anal_standing.link_positions(standing_doggy, "transition_anal_standing_standing_doggy")
    anal_standing.link_positions(doggy_anal, "transition_anal_standing_doggy_anal")

label intro_anal_standing(the_girl, the_location, the_object):
    "With your arms wrapped around [the_girl.possessive_title], you make out for a bit with her back to the [the_object.name]."
    "You turn her around, and she leans over [the_object.name], presenting her ass to you."
    $ the_girl.draw_person(position = anal_standing.position_tag)
    mc.name "That's it, [the_girl.title], I'm going to fuck your ass today."
    if the_girl.has_anal_fetish:
        the_girl "Oh thank god, I've been daydreaming about this all day long."
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "I can't wait! It's so intense when you fuck me back there..."
    elif the_girl.effective_sluttiness() > 95:
        the_girl "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl "I don't know, are you sure that thing is gonna fit in me back there?"

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_standing.position_tag, visible_enough = True, prefer_half_off = True)

    if the_girl.has_anal_fetish:
        if the_girl is mom:
            "You work your cock up and down [the_girl.possessive_title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "[the_girl.title]... your [the_girl.mc_title] is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl "Do it honey. [the_girl.title] is ready for you!"
        elif the_girl is lily:
            "You work your cock up and down [the_girl.possessive_title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Hey [the_girl.title], your [the_girl.mc_title] is about to fuck your ass now, just the way you like."
            "Her body shudders from your dirty talk. She wiggles her ass back up against you."
            the_girl "Do it! Stick it in me, you know I can take it!"
        else:
            "You slowly pull out the pink jeweled butt plug from [the_girl.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_girl.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_girl.possessive_title] tries to push back against you and begins to beg."
            the_girl "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass right now!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_girl.possessive_title]."
    elif the_girl.arousal_perc > 60:
        "You rub the tip of your penis against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions."
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her [the_girl.hair_description] to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_girl.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop."
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her."
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god it's so dirty... but it is so good too..."
        $ the_girl.discover_opinion("anal sex")
    return

label scene_anal_standing_1(the_girl, the_location, the_object):
    "Your hips slap against [the_girl.possessive_title]'s as you plunder her rectum."
    $ the_girl.call_dialogue("sex_responses_anal")
    if the_girl.sex_skills["Anal"] < 2: #Inexperienced
        "After a particularly hard thrust, [the_girl.possessive_title] reflexively starts to pull away. You grab her hips to keep her from pulling off completely."
        the_girl "I'm sorry [the_girl.mc_title], it hurts. Can you go a little slower?"
        "You pull her hips back toward you slowly. Her inexperienced ass yields to your penis and she sighs as you bottom out."
        "You pull yourself out a bit, then spit on her asshole and work it around a bit to provide a bit of extra lubrication."
        "Next time you push yourself in it goes in a bit easier, but you can tell she is having a hard time taking you in her back passage."
    elif the_girl.has_role(anal_fetish_role):           #Anal fetish
        $ play_moan_sound()
        "After a particularly hard thrust, [the_girl.possessive_title] moans lewdly."
        if the_girl is mom:
            the_girl "That's it honey, fuck me harder! God I wish I could walk around with you inside me all day..."
        elif the_girl is lily:
            the_girl "That's it [the_girl.mc_title]! Fuck me harder! God I wish I could walk around with you inside me all day..."
        else:
            the_girl "That's it, fuck me harder! This is so much better than that plug, I wish I could walk around with you inside me all day..."
        "With one hand on her hip to control the pace, you grope and worship her ass cheeks with the other hand."
        "[the_girl.possessive_title] clenches each time you pull back, and relaxes each time your push forward. The sensation is exquisite."
        "You use both hands to grab her hips and slam yourself into her."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers and caresses you in response."
    else:
        $ play_moan_sound()
        "Fucking her hard, [the_girl.possessive_title] moans, matching each hip movement of yours with a movement of her own."
        the_girl "Oh god, you fuck me so good, I can barely keep up!"
        "[the_girl.possessive_title] reaches back with one hand and pulls her ass cheek back, giving you a great view of her booty hole stretched wide to accommodate you."
        "Buried deep inside, you stir your hips in a circular motion. Her rectum quivers in response."

    menu:
        "Knead her ass":
            "With your erection buried deep in her rump, you take both hands and knead her ass cheeks."
            mc.name "[the_girl.title], your ass is so tight, I can't believe you let me sodomize you like this."
            if the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 180:
                "[the_girl.possessive_title] trembles at your words and touch."
                "You pull her ass cheeks apart and revel in her ultimate submission, your cock in her forbidden hole."
                the_girl "I couldn't stop you from fucking me... any way you want... even if I wanted to..."
                if the_girl.is_bald:
                    "You reach forward and run a hand over her shoulder. You knead them for a few seconds, then grasp on firmly and pull her towards you."
                else:
                    "You reach forward and run a hand through her hair. You knead her scalp for a few seconds, then grasp her hair and pull it towards you."
                mc.name "That's right bitch, you're here to pleasure me, when, how, and wherever I want."
                $ the_girl.discover_opinion("being submissive")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3)
            elif the_girl.is_dominant or the_girl.obedience < 80:
                "[the_girl.possessive_title] looks back at you and smiles."
                the_girl "It's definitely a... unique feeling [the_girl.mc_title]. Maybe you should let me peg you sometime?"
                "You give [the_girl.possessive_title] a good, hard thrust in response."
                $ the_girl.discover_opinion("taking control")
            else:
                the_girl "I don't know what is about you, [the_girl.mc_title]... I just want to make you feel good!"
                "You pull her ass cheeks apart. You give her a couple long, slow thrusts and enjoy the sight of your erection disappearing inside her bowel."
                if mc.arousal_perc > 70:
                    "You moan at the sensations."
                    mc.name "You feel amazing. You're gonna make me cum soon."
                    if the_girl.get_opinion_score("anal creampies") > 0:
                        "[the_girl.possessive_title] looks back at you and smiles."
                        the_girl "Oh [the_girl.mc_title], I can't wait to feel you fill me up. I hope you finish deep!"
                        "[the_girl.possessive_title]'s ass quivers a bit, as she imagines you cumming deep inside her."
                        $ the_girl.discover_opinion("anal creampies")
                        $ the_girl.change_arousal(the_girl.get_opinion_score("anal creampies") * 3)
                        if the_girl.get_opinion_score("being covered in cum") > 0:
                            the_girl "You could always pull out too... your cum feels so good when is splashes all over my skin..."
                            $ the_girl.discover_opinion("being covered in cum")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being covered in cum") * 3)
                            if the_girl.get_opinion_score("cum facials") > 0:
                                the_girl "Or my face! You haven't cum on my face in a while either..."
                                $ the_girl.discover_opinion("cum facials")
                                $ the_girl.change_arousal(the_girl.get_opinion_score("cum facials") * 3)
                                "[the_girl.possessive_title] starts muttering to herself, fantasizing about all the different ways you could cum on, or in her."
            "You put your hands on her hips and resume your anal coupling."

        "Play with her clit":
            "You lean forward a bit and reach down with one hand and begin to move it in circles around her clit."
            if the_girl.get_opinion_score("being fingered") > 0:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans loudly in response."
                the_girl "Oh [the_girl.mc_title], I love your hands on me... especially down there..."
                "You slide your middle finger along her slit a few times and then push up inside her pussy."
                "You give your hips a few long, slow strokes and you move your finger in time, penetrating both her holes at once."
                $ the_girl.discover_opinion("being fingered")
                $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") * 2 + mc.sex_skills["Foreplay"])
                "She really enjoys the extra stimulation."
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans in response."
                "After a few moments of stimulation, she starts to move her hips back and forth, stirring your dick inside her bowel."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
                if the_girl.arousal_perc > 80:
                    "You can feel her juices dripping down from her slit in response to your touch."
                    if the_girl.arousal_perc >= 100:
                        $ play_moan_sound()
                        "She moans loudly. She grinds herself up against your fingers while your cock is buried deep inside her ass. The stirring motion feels great."
                        the_girl "Oh fuck, here I go again!"
                        "[the_girl.possessive_title]'s legs start to give out as she cums yet again. You hold her body in place as she cums, your hips in the back and your hand in her crotch."
                        $ the_girl.change_happiness(5)
                        $ the_girl.have_orgasm()
                        the_girl "Oh Jesus... you made me cum again... I... god keep going, I'm going to cum again!"
                        return
            "After a bit longer of touching her, you straighten your back and begin to rock your hips again, continuing to fuck her ass."

        "Gag her with your fingers" if the_girl.get_opinion_score("being submissive") > 0:
            if the_girl.is_bald:
                "You grab a hold of the [the_girl.possessive_title]'s throat with one hand. You pull back causing her back to arch and constricting her breathing, her mouth opening slightly."
            else:
                "You grab a hold of the [the_girl.possessive_title]'s hair with one hand. You pull back causing her back to arch and she exclaims in surprise, her mouth opening slightly."
            "You reach around and grab her shoulders, while forcing two fingers of your other hand into her mouth and down her throat as far as you can."
            if the_girl.sex_skills["Oral"] > 4:#expert
                $ play_moan_sound()
                "[the_girl.possessive_title] moans in response."
                "She is so practiced at throating dick that this exercise is not creating the desired response."
                "She reaches behind her with both her hands and spreads her butt cheeks as you fuck her ass."
                $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being submissive", "anal sex"]))
            else:
                $ play_gag_sound()
                "[the_girl.possessive_title] starts to gag and choke and splutter."
                "This makes her whole body clench and unclench, including her ass, giving you the sensation you were looking for."
                $ mc.change_arousal(5)
                if the_girl.get_opinion_score("being submissive") < 2:# she is not submissive enough
                    "[the_girl.possessive_title] reaches up and tries to pull your fingers out of her mouth."
                    menu:
                        "Let her":
                            "[the_girl.possessive_title] pulls your hand and fingers out of her mouth though she is still choking and spluttering."
                            "You hold her hips as you continue to fuck her ass."
                            $ the_girl.change_stats(arousal = -2, happiness = -3)
                        "Keep your fingers there":
                            mc.name "Oh no you don't."
                            if the_girl.get_opinion_score("taking control") > 1:
                                "[the_girl.possessive_title] holds onto your arm with her other hand and bites your fingers hard."
                                mc.name "Fuck!"
                                "You reflexively pull your hand back out."
                                $ the_girl.change_stats(arousal = -10, happiness = -5, love = -5)
                                the_girl "Don't do that."
                            elif the_girl.get_opinion_score("taking control") > 0:
                                "[the_girl.possessive_title] holds on to your arm with her other hand."
                                "She is finding it hard to do much of anything as she coughs, splutters and retches with your fingers down her throat."
                                $ the_girl.change_stats(arousal = -5, happiness = -3, love = -3)
                                "Once you're satisfied you withdraw your fingers."
                            else:
                                "[the_girl.possessive_title] drops her hand in resignation."
                                $ play_gag_sound()
                                "She coughs, splutters and retches with your fingers down her throat, clenching and unclenching her rectum with each gag."
                                $ the_girl.change_stats(arousal = -2, happiness = -3, love = -1)
                                "Once you're satisfied you withdraw your fingers."
                else:#girl is submissive
                    $ play_gag_sound()
                    "[the_girl.possessive_title] pushes her head onto your hand causing her to gag."
                    "She reaches behind her with both her hands and uses them to hold on to your butt cheeks as you fuck her ass."
                    "She pulls you into her ass, while at the same time trying to push your fingers further down her throat, causing her whole body to clench and unclench."
                    $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being submissive", "anal sex"]))
                    "Once you're satisfied you withdraw your fingers."
        "Gag her with your fingers\n{color=#ff0000}{size=18}Must be submissive{/size}{/color} (disabled)" if the_girl.get_opinion_score("being submissive") <= 0:
            pass
    return


label scene_anal_standing_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] quivers as you slowly up the pace a bit. The sensation of burying yourself in her tight chute over and over is amazing."
    if the_girl.tits_available:
        "You reach around her body with one hand and grasp her tit. You pinch and pull at her nipple roughly as you plow her behind."
    else:
        $ play_spank_sound()
        "You run your hands along her hips. You grab her hips and smack her ass roughly as you plow her behind."

    if the_girl.arousal_perc > 120:
        the_girl "Ohhh my god, it's so good... I can't believe I came already..."
        "[the_girl.possessive_title]'s legs are shaking. She is thoroughly enjoying her anal plundering."
        if the_girl.has_role(anal_fetish_role):
            the_girl "This is it, this is why I love anal so much... I just can't stop cumming! It feels so good."
    elif the_girl.arousal_perc > 80:
        the_girl "Ohhh, it feels so good. You're gonna make me cum like this... aren't you?"
        "You can feel a slight quiver in [the_girl.possessive_title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.possessive_title] groans in response to one particularly deep thrust."
        the_girl "It's so big... How does it even fit back there?"
    $ play_moan_sound()
    "You push yourself in as deep as you can go. [the_girl.possessive_title] moans as you fill her completely."
    menu:
        "Admire her":
            "You moan in appreciation."
            mc.name "[the_girl.title], your ass is so good. Your booty feels amazing."
            if the_girl.has_role(anal_fetish_role):
                the_girl "I love being your anal slut. Fuck me good [the_girl.mc_title]!"
            elif the_girl.sluttiness > 80:
                the_girl "You are so big... it's so full when you push it in me like this."
            else:
                the_girl "It better... I can't believe I let you talk me into this..."
        "Talk Dirty":
            mc.name "I love how your ass gets so stretched out with my cock fucking it."
            if the_girl.has_role(anal_fetish_role):
                $ play_moan_sound()
                "[the_girl.possessive_title] moans enthusiastically. She wiggles her hips back and forth, caressing your dick with her forbidden hole."
                the_girl "[the_girl.mc_title]... fuck my ass... fuck me hard!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                the_girl "Oh [the_girl.mc_title]... [the_girl.mc_title]!"
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "[the_girl.possessive_title] is moaning your name over and over. You continue to give her the anal reaming she is begging for."

            elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 180:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans enthusiastically."
                the_girl "[the_girl.mc_title]... use me... fuck me! Make me your little slut!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 2)
                "You give her the anal reaming she is begging for."
            elif the_girl.get_opinion_score("anal sex") < 0 :
                "[the_girl.possessive_title] looks back at you with a scowl."
                the_girl "Don't get used to it, [the_girl.mc_title]... I'm not sure how I let you talk me into this..."
                $ the_girl.discover_opinion("anal sex")
                "You decide for now to keep your pace nice and slow."
            else:
                "[the_girl.possessive_title] looks back at you and manages to smile through the intense sensation of having her ass fucked."
                the_girl "You are stretching me out so much... Be careful back there, I'm not sure how much of this I can take!"
                "You reassure her, and then slowly begin to fuck her tightest hole again."
        "Choke Her" if the_girl.get_opinion_score("being submissive") > 0:
            if the_girl.is_bald:
                "You take your hands off her hips and run them up her back. With one hand you grab her throat and pull her head back."
            else:
                "You take your hands off her hips and run them up her back. With one hand you grab the back of her hair and pull her head back."
            the_girl "Mmm, that's it, you can be rough with me if you want..."
            "You pull her [the_girl.hair_description] back hard enough to hurt a little, she arches her back in pleasure as you start to fuck her ass more roughly."
            mc.name "Of course I can, I can do anything I want to you, my little slut."
            "You run your other hand along the side of her neck. She begins to say something but you squeeze her neck and she stops."
            mc.name "Sshhh, there's no need for words right now."
            "You tighten your hold around her neck, constricting her airway. [the_girl.title] shoves her ass back hard against you."
            $ play_moan_sound()
            "You loosen your grip for a second and she moans loudly and takes a couple deep breaths. You cut the third one off and begin to really pound her ass."
            "Her ass cheeks quake from your relentless fucking. [the_girl.possessive_title] begins to squirm against you, fighting for air."
            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 5)
            "You hold on for a few more seconds, until you feel her knees start to buckle before letting go. [the_girl.possessive_title] gasps for air."
            the_girl "Oh my god, that was so hot..."
            "You spank her ass hard and continue to fuck her tightest hole."
        "Choke Her\n{color=#ff0000}{size=18}Must be submissive{/size}{/color} (disabled)" if the_girl.get_opinion_score("being submissive") <= 0:
            pass
    return


label outro_anal_standing(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_anal")
    mc.name "Ah, I'm going to cum!"
    if mc.condom:
        the_girl "Oh god do it! Show me how much you love my ass!"
    elif the_girl.get_opinion_score("anal creampies") > 0:
        the_girl "Yes! Shove it in deep [the_girl.mc_title]!"
    elif the_girl.sluttiness < 80:
        the_girl "Oh my god I can't believe I'm letting you do this..."
    else:
        the_girl "That's it [the_girl.mc_title], cum for me! Show me how much you love my ass!"
    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her ass", "body"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        if mc.condom:
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum."
            "She gasps with every final thrust as you fill your condom, which is slowly expanding inside her to accommodate your seed."
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.get_opinion_score("bareback sex") > 0:
                the_girl "Oh god, imagine if you weren't wearing that fucking rubber! I could feel you filling me up..."
            else:
                the_girl "That's it, cum deep!"
            "You wait until your orgasm has passed completely, then pull out and sit back. Her asshole gapes slightly. You condom is full of your potent seed."

            call post_orgasm_condom_routine(the_girl, anal_standing) from _call_post_orgasm_condom_routine_anal_standing
            return
        "[the_girl.possessive_title]'s ass is just too good. You decide to cum inside it."
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."
        if the_girl.get_opinion_score("anal creampies") > 0:
            the_girl  "Yes! Fill my ass with your cum!"
        if the_girl.arousal_perc >= 100:
            "You feel her bowel contracting around your dick as she also starts to orgasm."
            $ the_girl.change_happiness(5)
            $ the_girl.have_orgasm()
        $ the_girl.cum_in_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ anal_standing.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum pours into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
            the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
            "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
        elif the_girl.get_opinion_score("anal creampies") > 0:
            the_girl "Oh god... it's inside me... right where it belongs. Thank you so much, [the_girl.mc_title]!"
        elif the_girl.sluttiness > 90:
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
        $ anal_standing.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        elif the_girl.sluttiness > 90:
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
        if the_girl.get_opinion_score("being covered in cum") > 0 or the_girl.get_opinion_score("cum facials") > 0:
            "[the_girl.possessive_title] reaches up and immediately begins stroking you off for you final few seconds."
            "Your orgasm hits hard. Your first jet sprays across her face."
            $ the_girl.cum_on_face()
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            if the_girl.has_cum_fetish:
                "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her face. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans as your dick sprays jet after jet of seed across her face."
        elif the_girl.sluttiness > 80:
            "[the_girl.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from her knees, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")


    return


label transition_default_anal_standing(the_girl, the_location, the_object):
    if the_girl.obedience > 120:
        mc.name "Stand here."
        "[the_girl.possessive_title] obeys then leans forward and puts her hands on [the_object.name]."
    else:
        mc.name "Come stand over here."

    $ anal_standing.redraw_scene(the_girl)

    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_standing.position_tag, visible_enough = True, prefer_half_off = True)

    "You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    call transition_default_anal_penetration_dialog(the_girl, the_location, the_object) from _call_transition_default_anal_penetration_dialog_1
    return

label transition_standing_anal_to_standing_doggy_taboo_break_label(the_girl, the_location, the_object):
    "You pull your cock out of [the_girl.title]'s ass."
    "You continue your back and forth motion, rubbing your cock along her pussy lips."
    if the_girl.get_opinion_score("vaginal sex") > 0:
        the_girl "Oh... Please..."
    "You continue to move your cock forwards and backwards teasing her pussy."
    mc.name "Ready."
    "The word is a command not a question."
    $ the_girl.call_dialogue(standing_doggy.associated_taboo+"_taboo_break")
    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
    "After a moment of resistance your cock spreads her pussy open and you slide smoothly inside of her."
    the_girl "Oh god... Ah..."
    "You start with short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
    return

label transition_anal_standing_doggy_anal(the_girl, the_location, the_object):
    mc.name "Get down on your knees [the_girl.title], I'm going to fuck you like the little bitch you are."
    $ doggy_anal.redraw_scene(the_girl)
    the_girl "Oh yes, [the_girl.mc_title], make me your little bitch."
    return

label transition_default_anal_penetration_dialog(the_girl, the_location, the_object):
    if the_girl.sex_skills["Anal"] > 3 or the_girl.get_opinion_score("anal sex") > 1:
        the_girl "Oh god, yes. Fuck my ass [the_girl.mc_title]!"
        menu:
            "Slide it all in":
                "You keep a firm grip on her hips as you push forward, sliding it into her ass in one smooth motion."
                if the_girl.get_opinion_score("being submissive") > 0:
                    the_girl "Ah! Yes! Now we are getting somewhere!"
                else:
                    the_girl "Mmmhph... Fuck..."
            "Ram it home!":
                "You get a firm grip on her hips, make sure you're lined up, and push yourself in with all your might."
                if the_girl.get_opinion_score("being submissive") > 1 or the_girl.get_opinion_score("anal sex") >= 2:
                    the_girl "Ah! Yes! Tear that ass up!"
                    $ the_girl.change_arousal(3 * the_girl.get_opinion_score(["being submissive", "anal sex"]))
                    "Using her pussy juice as lube you lay into her tight ass, wasting no time in fucking her hard."
                else:
                    the_girl "Oh fuck! FUCK! YES!"
                    "She yells out in surprise and pain. You bottom out and hold still, giving her a second to get used to your size."
    else:
        the_girl "Uh... Oh fuck, you'd tear me apart [the_girl.mc_title]..."
        menu:
            "Ram it home!":
                "You get a firm grip on her hips, make sure you're lined up, and push yourself in with all your might."
                if the_girl.get_opinion_score("being submissive") > 1 or the_girl.get_opinion_score("anal sex") >= 2:
                    the_girl "Ah! Yes! Tear that ass up!"
                    $ the_girl.change_arousal(5* the_girl.get_opinion_score(["being submissive", "anal sex"]))
                    "Using her pussy juice as lube you lay into her tight ass, wasting no time in fucking her hard."
                else:
                    the_girl "Oh fuck! FUCK!"
                    "She yells out in surprise and pain. You bottom out and hold still, giving her a second to get used to your size."
                    the_girl "Fuck... I hate that part..."
                    mc.name "It's just like ripping off a bandage. You'll get used to it."
                    "You wait a moment, then start to move again. Using her pussy juices as lube you've soon got a good rhythm going."

            "Take it slow":
                if the_girl.get_opinion_score("being submissive") > 0 or the_girl.get_opinion_score("anal sex") >= 2:
                    the_girl "Mmmm."
                    "[the_girl.possessive_title] reaches behind her and grabs one of your butt cheeks. She pulls on you to get your cock as deep in her ass as she can."
                else:
                    "You keep a firm grip on her hips as you push forward, sliding into her one painful inch at a time."
                    "Using her pussy juice as lube, you manage to slip your full cock into her ass. You pause there, giving her a moment to adjust."
                    the_girl "Mmmhph... Fuck..."
                    "When she's finally ready you start to move, fucking her cute little ass."
    return

label transition_anal_standing_standing_doggy(the_girl, the_location, the_object):
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

    "You grab her by the hips and thrust yourself deep inside her tight, pulsating pussy."
    return

label strip_anal_standing(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  anal_standing.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_anal_standing(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = anal_standing.position_tag)
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
                the_girl "Does it make me look like the cum hungry slut that I am? Or is it your cock in my ass that makes me look that way?"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False


label orgasm_anal_standing(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s legs start to quiver, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses_anal")
    "You bury your cock deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl "Don't stop... it still feels so good!"
    return

label taboo_break_anal_standing(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You grab [the_girl.possessive_title]'s ass and give it a squeeze, then a hard slap."
    if the_girl.effective_sluttiness(anal_standing.associated_taboo) > anal_standing.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
        mc.name "Stand over here, I want to get a look at this ass."
        $ the_girl.draw_person(position = "back_peek", the_animation = ass_bob)
        "She turns around and jiggles her butt playfully for you."
        the_girl "This big fat ass? You finally want to take a closer look?"
        mc.name "I said stand here, come on."
        $ the_girl.draw_person(position = "standing_doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "She leans into the [the_object.name] and points her butt in your direction. She lowers her shoulders and works her hips for you."

    else:
        mc.name "Stand over here."
        $ the_girl.draw_person(position = "stand2")
        "She slowly walks to the indicated position in front of you."
        mc.name "Good girl, now spin around and show me that ass."
        "She nods and turns around."
        $ the_girl.draw_person(position = "walking_away")
        mc.name "Nice. Now shake it for me."
        the_girl "Like... this?"
        $ the_girl.draw_person(position = "standing_doggy", the_animation = ass_bob, animation_effect_strength = 0.4)
        "[the_girl.title] works her hips and jiggles her ass for you."
        mc.name "Getting there, a little faster now."
        $ the_girl.draw_person(position = "standing_doggy", the_animation = ass_bob, animation_effect_strength = 0.7)
        "She speeds up."
    the_girl "Is that what you wanted?"
    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_standing.position_tag, visible_enough = True, prefer_half_off = True)
    "You slap your cock down on her ass and grab her tight cheeks, spreading them apart to get a look at her asshole."
    mc.name "Almost. I think it's time we stretched you open."
    $ the_girl.call_dialogue(anal_standing.associated_taboo+"_taboo_break")
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
