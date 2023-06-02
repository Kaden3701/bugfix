init python:
    anal_swing = Position(name = "Swinging Anal", slut_requirement = 80, slut_cap = 100, requires_hard = True, requires_large_tits = False,
        position_tag = "sitting", requires_location = "Swing", requires_clothing = "Vagina", skill_tag = "Anal",
        girl_arousal = 20, girl_energy = 12,
        guy_arousal = 22, guy_energy = 16,
        connections = [],
        intro = "intro_anal_swing",
        scenes = ["scene_anal_swing_1","scene_anal_swing_2"],
        outro = "outro_anal_swing",
        transition_default = "transition_default_anal_swing",
        strip_description = "strip_anal_swing",  strip_ask_description = "strip_ask_anal_swing",
        taboo_break_description = "taboo_break_anal_swing",
        orgasm_description = "orgasm_anal_swing",
        verb = "ass fuck",
        opinion_tags = ["doggy style sex", "anal sex"], record_class = "Anal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "anal_sex")

    list_of_positions.append(anal_swing)

#init 1:
    #python:
        #anal_swing.link_positions_two_way(doggy, "transition_anal_swing_doggy", "transition_doggy_anal_swing")

label intro_anal_swing(the_girl, the_location, the_object):
    "[the_girl.possessive_title] sits down in the [the_object.name]. Her ass is hanging off the back end."
    "You run your hands along her supple hips."
    if the_girl.has_role(anal_fetish_role):
        the_girl "Oh my god. This is so kinky... fuck me good [the_girl.mc_title]!"
    elif the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "I can't wait! It's so intense when you fuck me back there..."
    elif the_girl.effective_sluttiness() > 95:
        the_girl "Oh god I love it when you do this to me..."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "Ok, just be careful [the_girl.mc_title]..."
    else:
        the_girl "I don't know, are you sure this thing is safe?"

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_swing.position_tag, visible_enough = True, prefer_half_off = True)

    if the_girl.has_role(anal_fetish_role):
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
        elif the_girl is starbuck:
            "You work your cock up and down [the_girl.possessive_title]'s slit a few times, her wetness lubricating it."
            "You lean forward and whisper into her ear."
            mc.name "Baby... I'm going to fuck your ass now... just the way you like it!"
            "You can see goosebumps break out all over her body."
            the_girl "Oh god, I touch myself every time I think about the first time you fucked in one of these at the shop."
            the_girl "Fuck me good, [the_girl.mc_title]! I want it so bad!"
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
        else:
            "You slowly pull out the pink jeweled butt plug from [the_girl.possessive_title]'s rectum. She quivers in anticipation of what you are about to do to her."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            "You work a couple fingers into her bottom. It is clear she loves anal sex so much, she keeps herself lubed up with the plug in throughout the day hoping for you to come fuck it."
            "You decide to tease her before you put it in."
            mc.name "You're such a buttslut, [the_girl.title]. Are you sure you want it back there? Your pussy looks like it could use a proper fucking too..."
            "[the_girl.possessive_title] begs you not to stick it in her pussy."
            the_girl "No! I need you in my ass right now... I need the heat and intensity of you fucking my ass please!"
            "When you're ready you push forward. Her back passage greedily accepts your erection, eliciting a satisfied sigh from [the_girl.possessive_title]."
    elif the_girl.arousal_perc > 60:
        "You rub the tip of your penis against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. You rub your lubricated penis against her ass to help prepare her for your initial penetration."
        "You rub your dick against her pussy again and gather more of her juices. She is already so wet you are soon slick with her secretions."
    else:
        "You line yourself up with her ass, but the lack of lubricant makes it impossible to push it in. You pull on her [the_girl.hair_description] to bring her head back around to face you."
        "You put your other hand in front of her face and she quickly opens her mouth and sucks on them. [the_girl.possessive_title] slobbers all over your fingers for a few a seconds before you pull them out with a loud pop"
        "You use your fingers to crudely work in and out of her ass a few times to help get it lubricated."
        "Deciding against making her suck on your fingers again after they've been in her ass, you spit a couple times down on her ass to get a bit more lubrication so you can penetrate her"
    "When you're ready you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
    if the_girl.get_opinion_score("anal sex") > 0 :
        the_girl "Oh my god it's so dirty... but it is so good too..."
        $ the_girl.discover_opinion("anal sex")
    return

label scene_anal_swing_1(the_girl, the_location, the_object):
    "Your hips slap against [the_girl.possessive_title]'s as you plunder her rectum. You keep a slow but steady pace."
    "With each bounce in the swing, [the_girl.possessive_title]'s ass pulls off you almost completely, but you grab the ropes of the swing and forcefully slam her ass back into you."
    $ the_girl.call_dialogue("sex_responses_anal")

    if the_girl.has_role(anal_fetish_role):           #Anal fetish
        $ play_moan_sound()
        "After a particularly hard bounce, [the_girl.possessive_title] moans ecstatically."
        if the_girl is mom:
            the_girl "That's it honey, fuck [the_girl.title] harder! Tie me up and hang me from a swing and pound [the_girl.title]'s ass any way you want! It feels so good!"
        elif the_girl is lily:
            the_girl "That's it [the_girl.mc_title]! Fuck me harder! I'm [the_girl.possessive_title], hanging from a swing just to please you!"
        elif the_girl is starbuck:
            the_girl "Yes! Don't let up! I think about you stringing me up like this every time I see the swing in the store."
        else:
            the_girl "That's it, fuck me harder! Make me walk funny for a week!"
        "With your hands wrapped around the straps, you control the pace of your fucking."
        "[the_girl.possessive_title] clenches each time you pull back, and relaxes each time your push forward. The sensation is exquisite."
        "You grab the swing and pull her into you hard, slamming yourself into her."
    else:
        $ play_moan_sound()
        "Fucking her hard, [the_girl.possessive_title] moans. She clutches onto the swing, holding on while you have your way with her ass."
        the_girl "Oh god, you fuck me so good."

    #menu:
    #    "Knead her ass":


    #    "Play with her clit":

    return


label scene_anal_swing_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] quivers as you slowly up the pace a bit. You pull the straps on the swing towards you and thrust your hips forward, burying your cock as deep in her ass as you can."
    if the_girl.tits_available:
        "You reach around her body with both hands and grab her tits. You pinch and pull at her nipples roughly being careful to keep your cock deep inside her."
    else:
        "You reach around her body with both hands and grab as her tits. The fabric covering them is maddening. You decide to strip her down."
        mc.name "[the_girl.title]... I need to feel your skin!"
        $ the_person.strip_to_tits(position = anal_swing.position_tag, visible_enough = True, prefer_half_off = True)

        mc.name "Mmm, you tits are amazing."
        if the_girl.get_opinion_score("showing her tits") > 0:
            "You can see a blush in [the_girl.possessive_title]'s cheeks. She likes to show off her [the_girl.tits] tits!"
            $ the_girl.discover_opinion("showing her tits")
            $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["showing her tits", "anal sex"]))

    $ play_moan_sound()
    "You roll each of nipples between your thumb and index fingers. [the_girl.possessive_title] arches her back and moans."
    "You grasp her tits with both hands and hold her in place and start to give her rapid thrusts with your hips."
    the_girl "Oh fuck! Yes! [the_girl.mc_title]!"
    "She is writhing in the swing back against you, but she has no leverage. You have all the control."

    if the_girl.arousal_perc > 120:
        the_girl "Ohhh my god, it's so good..."
        "[the_girl.possessive_title]'s ass is quivering non stop."
        if the_girl.has_role(anal_fetish_role):
            the_girl "I just can't stop cumming! It feels so good [the_girl.mc_title]! Fuck my ass and make it yours!"
    elif the_girl.arousal_perc > 80:
        the_girl "Ohhh, it feels so good. You're gonna make me cum like this... aren't you?"
        "You can feel a slight quiver in [the_girl.possessive_title]'s body as you fuck her. She's probably going to cum soon!"
    else:
        "[the_girl.possessive_title] groans in response to one particularly deep thrust."
        the_girl "It's so big... How does it even fit back there?"

    $ play_moan_sound()
    "You push yourself in as deep as you can go. [the_girl.possessive_title] moans as you fill her completely."
    menu:
        "Kiss her neck":
            "You lean down and start to kiss [the_girl.possessive_title]'s neck. She tilts her head to the side to let you."
            if mc.sex_skills["Foreplay"] > 2:

                if the_girl.get_opinion_score("kissing") > 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("kissing") * 2)
                the_girl "[the_girl.mc_title]! I don't know if I can take this!"
                $ play_moan_sound()
                "She moans erotically. Her senses are in overdrive."
                "Your lips on her neck, your fingers pinching her nipples, and your dick in her ass. You are giving her an incredible amount of stimulation."
                $ the_girl.change_arousal(mc.sex_skills["Foreplay"])
            else:
                "You do your best to split your focus between kissing [the_girl.possessive_title] and pumping your hips, but you find yourself slipping out of the steady rhythm you had established."
                "[the_girl.possessive_title] sighs happily."
                the_girl "That feels nice, but it feels better when you focus on fucking me."
            "You kiss her neck one more time, then move your hands back to the swing straps and continue fucking her. She gives a little yelp when you pinch one of her nipples."
        "Talk Dirty":
            mc.name "I love to fuck your ass. It's so tight! You make such a great butt slut."
            if the_girl.has_role(anal_fetish_role):
                $ play_moan_sound()
                "[the_girl.possessive_title] moans enthusiastically. She reaches back with one hand and grabs your hip, urging you to fuck her harder."
                the_girl "[the_girl.mc_title]! I love being your butt slut. Now give it to your slut hard!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                the_girl "Oh fuck [the_girl.mc_title]! Yes!"
                $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                "[the_girl.possessive_title] is moaning your name over and over. Her whole body bounces and sways as you fuck her on the swing."

            elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.obedience > 180:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans enthusiastically."
                the_girl "[the_girl.mc_title]... use me... fuck me! Make me your little slut!"
                "You give her what she wants. You grab her hips and start thrusting into her hard and fast."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 3 + 3)
                "You give her the anal reaming she is begging for."
            else:
                "[the_girl.possessive_title] looks back at you and manages to smile through the intense sensation of having her ass fucked."
                the_girl "You are stretching me out so much... Be careful back there, I'm not sure how much of this I can take!"
                "You reassure her, and then slowly begin to fuck her tightest hole again."

    return


label outro_anal_swing(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s tight ass draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_anal")
    mc.name "Ah, I'm going to cum!"
    if the_girl.get_opinion_score("anal creampies") > 0 or mc.condom:
        the_girl "Yes! Shove it in deep [the_girl.mc_title]!"
    elif mc.condom:
        the_girl "That's it [the_girl.mc_title], cum for me! Show me how much you love my ass!"
    elif the_girl.sluttiness < 80:
        the_girl "Oh my god I can't believe I'm letting you do this..."
    else:
        the_girl "That's it [the_girl.mc_title], cum for me! Show me how much you love my ass!"
    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her ass", "body"], ["Cum on her tits", "tits"])
    $ the_choice = climax_controller.show_climax_menu()
    if the_choice == "Cum inside of her":
        "[the_girl.possessive_title]'s ass is just too good. You decide to cum inside it."
        if mc.condom:
            "You pull back on the swing straps and drive your cock deep inside of her as you cum. You hope the condom can handle your load."
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.arousal_perc > 110:
                "You feel her bowel contracting around your dick as she also starts to orgasm."
                $ the_girl.change_happiness(5)
                $ the_girl.have_orgasm()
            "You wait until your orgasm has passed completely, then pull out. Her asshole gapes slightly."
            the_girl "Wow... that was intense..."
            return
        else:
            "You pull back on the swing straps and drive your cock deep inside of her as you cum. She moans as you body dumps your load deep into her bowel."
        if the_girl.get_opinion_score("anal creampies") > 0:
            the_girl  "Yes! Fill your slut's ass with your cum! It's so hot!"
        if the_girl.arousal_perc > 110:
            "You feel her bowel contracting around your dick as she also starts to orgasm."
            $ the_girl.change_happiness(5)
            $ the_girl.have_orgasm()
        $ the_girl.cum_in_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ anal_swing.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum pours into her ass. Goosebumps erupt all over her body as her brain registers her creampie."
            the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
            "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
        elif the_girl.get_opinion_score("anal creampies") > 0:
            the_girl "Yes!... Thank you so much [the_girl.mc_title]. It's inside me... you know I love that so much..."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god it's so good. It makes me so happy to be pumped full like this."
        else:
            the_girl "Oh fuck, I can't believe I let you cum in my ass..."

        "You wait until your orgasm has passed completely, then pull out. Her asshole gapes and you can see a hint of your cum start to dribble out, but most of it stays buried with her bowel"

    if the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.possessive_title] at the last moment. You pull the condom off and blow your load all over her heart shaped ass cheeks."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        if the_girl.get_opinion_score("being covered in cum") > 0:
            the_girl "Yes! Paint me with your sticky cum!"
        $ the_girl.cum_on_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ anal_swing.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the streams of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
    if the_choice == "Cum on her tits":
        mc.name "Fuck, get ready [the_girl.title], I wanna cum on your tits!"
        if mc.condom:
            "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. You spin the swing around quickly so she faces you, pulling your condom off at the same time."
        else:
            "You pull your cock out of [the_girl.possessive_title]'s ass with a satisfying pop. You spin the swing around quickly so she faces you."
        if the_girl.get_opinion_score("being covered in cum") > 0:
            "[the_girl.possessive_title] reaches up and immediately begins stroking you off for you final few seconds."
            "Your orgasm hits hard. Your first jet sprays across her tits."
            $ the_girl.cum_on_tits()
            $ the_girl.draw_person(position = "sitting")
            if the_girl.has_cum_fetish:
                "You can see [the_girl.possessive_title]'s pupils dilate as you fulfil her cum fetish."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her body. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                "[the_girl.possessive_title] moans as your dick sprays jet after jet of seed across her body."
        elif the_girl.sluttiness > 80:
            "[the_girl.possessive_title] presses her tits together with her hands, eager to take your hot load."
            $ the_girl.cum_on_tits()
            $ the_girl.draw_person(position = "sitting")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s chest. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title] looks up at you and waits patiently for you to cum."
            $ the_girl.cum_on_tits()
            $ the_girl.draw_person(position = "sitting")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s chest. She waits until she's sure you're finished."
        else:
            "[the_girl.possessive_title] closes her eyes and turns away."
            $ the_girl.cum_on_tits()
            $ the_girl.draw_person(position = "sitting")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s chest. She flinches as the first splash of warm liquid lands on her body, but doesn't pull away entirely."
        $ climax_controller.do_clarity_release(the_girl)
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from the swing, her tits covered in your seed."
        the_girl "Wow, that was really intense..."


    return


label transition_default_anal_swing(the_girl, the_location, the_object):
    $ anal_swing.redraw_scene(the_girl)
    "[the_girl.possessive_title] sits down in the [the_object.name]. Her ass is hanging off the back end."
    "You run your hands along her supple hips."
    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_swing.position_tag, visible_enough = True, prefer_half_off = True)
    "You bounce your hard shaft on her ass a couple of times before lining yourself up with her sphincter."
    "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_anal_swing(the_girl, the_clothing, the_location, the_object):
    #"[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position =  anal_swing.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_anal_swing(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = anal_swing.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "She groans happily when you resume fucking her tight rear."
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

label orgasm_anal_swing(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s whole body starts to tremble, and then suddenly she tenses up."
    $ the_girl.call_dialogue("climax_responses_anal")
    "You bury your cock deep in [the_girl.possessive_title]'s ass while she cums. Her bowel grips you tightly."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    if the_girl.get_opinion_score("anal sex") < 0:
        the_girl "I can't believe that just happened... oh god now you're going to keep going, aren't you?"
    else:
        the_girl "Don't stop... it still feels so good!"
    return

label taboo_break_anal_swing(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return
