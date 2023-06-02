init:
    python:
        missionary = Position(name = "Missionary", slut_requirement = 50, slut_cap = 70, requires_hard = True, requires_large_tits = False,
            position_tag = "missionary", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
            girl_arousal = 16, girl_energy = 12,
            guy_arousal = 15, guy_energy = 14,
            connections = [],
            intro = "intro_missionary",
            scenes = ["scene_missionary_1","scene_missionary_2", "scene_missionary_3"],
            outro = "outro_missionary",
            transition_default = "transition_default_missionary",
            strip_description = "strip_missionary", strip_ask_description = "strip_ask_missionary",
            orgasm_description = "orgasm_missionary",
            taboo_break_description = "taboo_break_missionary",
            opinion_tags = ["missionary style sex","vaginal sex"], record_class = "Vaginal Sex",
            default_animation = missionary_bob,
            associated_taboo = "vaginal_sex")
        list_of_positions.append(missionary)

init 1:
    python:
        missionary.link_positions(piledriver,"transition_missionary_piledriver")

label intro_missionary(the_girl, the_location, the_object):
    "You run your hands along [the_girl.title]'s hips, feeling the shape of her body."
    mc.name "I want you to lie down for me."
    $ missionary.redraw_scene(the_girl)
    "She nods and lies down on the [the_object.name], waiting while you climb on top of her."
    "[the_girl.possessive_title] wraps her arms around you and holds you close as you line your cock up with her pussy. She sighs happily into your ear as you slide into her."
    return

label taboo_break_missionary(the_girl, the_location, the_object):
    "You take [the_girl.title]'s hands in yours and guide her down onto the [the_object.name]. She follows your lead, lying down for you."
    $ missionary.redraw_scene(the_girl)
    "You place your hands on her knees and spread her legs, kneeling down between them."
    "You sit your hard cock on her stomach, teasingly close to her warm pussy. [the_girl.possessive_title] reaches down and gently pets your shaft."
    $ the_girl.call_dialogue(missionary.associated_taboo+"_taboo_break")
    if the_girl.effective_sluttiness(missionary.associated_taboo) > missionary.slut_cap:
        "She takes your cock and moves it down, sliding the tip into her pussy for you."

    else:
        "You grab your cock and move it down. [the_girl.title] gasps as your tip flicks over her clit and spreads her pussy lips open."
    "You lie down on top of her and thrust forward. After a moment of resistance you slide easily into her slippery, warm tunnel."
    the_girl "Ah..."
    "You hold yourself deep inside of her for a few seconds, then pull back and begin slowly thrust in and out."
    return

label scene_missionary_1(the_girl, the_location, the_object):
    # CHOICE CONCEPT: Kiss her neck // Talk dirty to her
    # Intro concept. Short difference depending on if she's wet or not.
    if the_girl.arousal_perc > 50:
        "[the_girl.title]'s pussy is nice and wet as you pump your hips and fuck her."
    else:
        "[the_girl.title]'s pussy is still getting wet. You take it slow, giving her time to warm up."

    menu:
        "Kiss her neck":
            "You lean down and start to kiss at [the_girl.possessive_title]'s neck. She tilts her head to the side to let you."
            if mc.sex_skills["Foreplay"] > 2:

                if the_girl.get_opinion_score("kissing") > 0:
                    $ the_girl.discover_opinion("kissing")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("kissing"))
                the_girl "[the_girl.mc_title]... Oh [the_girl.mc_title] that feels so good."
                $ play_moan_sound()
                "She moans into your ear and pulls you closer to her."
                "You kiss her neck a few more times, then lean back and look into her eyes. She sighs happily and returns your gaze, locking eyes with you while you fuck her."
            else:
                "You do your best to split your focus between kissing [the_girl.title] and pumping your hips, but you find yourself slipping out of the steady rhythm you had established."
                "[the_girl.possessive_title] sighs happily and whispers in your ear."
                the_girl "That feels nice, but I want you to keep fucking me."
                "You kiss her one last time, then divert all of your attention to making love."

        "Talk dirty to her":
            mc.name "You feel amazing [the_girl.title], I wish I could fuck you like this all day."
            if the_girl.sluttiness > 60 or the_girl.get_opinion_score("being submissive" > 0):
                the_girl "Then do it. Pin me against the [the_object.name] and fuck me all you want."
                "She wraps her legs around your waist and pulls you deep inside of her. The tight, warm feeling of her cunt makes your cock twitch."
                if the_girl.wants_creampie:
                    the_girl "You can cum anywhere you want. You can pump your load right into me if that's what you want. If that's what would make you happy..."
                else:
                    the_girl "You can use me however you want [the_girl.mc_title], I'll be your obedient fuck toy, if that's what you want me to be..."
                $ play_moan_sound()
                "She moans into your ear and trembles beneath you."
            else:
                the_girl "Ah... I'm glad you're having a good time."
                mc.name "I bet you are too."
                the_girl "I... oh god, I am."
                "She blushes and turns away from you, panting for breath while you fuck her."

    # $ the_girl.call_dialogue("sex_responses_vaginal")
    # "[the_girl.title] digs her fingers into your back as you pump in and out of her tight slit. She moans into your ear, letting you hear her soft gasps and yelps."
    # if the_girl.arousal_perc > 50:
    #     "Her pussy is dripping wet now, practically begging you to fuck it more. You kiss her and keep going."
    # else:
    #     "Her pussy is starting to get nice and wet as you fuck it. You kiss her and keep going."
    return

label scene_missionary_2(the_girl, the_location, the_object):
    # CHOICE CONCEPT: Pin her down // Kiss her
    if the_girl.sex_skills["Vaginal"] < 3 and the_girl.arousal < 50:
        # INTRO: She's inexperienced and needs some help.
        "[the_girl.title]'s slit is tight and warm, but you can tell she's still getting wet."
        the_girl.name "Could you... take it a little slower for me? Sorry, I'm just not very good at this."
        menu:
            "Go easy on her":
                mc.name "Of course."
                $ play_moan_sound()
                "You slow your thrusts and hold [the_girl.possessive_title] close to you. You can feel her warm breath against your ear and hear her soft moans."
                mc.name "Is that better?"
                the_girl "Yeah. Ah..."
                "Little by little [the_girl.title] gets wetter and you're able to speed up. Her panting in your ear becomes louder and more passionate."


            "Fuck her hard anyways":
                mc.name "Don't worry, just relax and it'll all come naturally to you."
                "You speed up and fuck [the_girl.title]s tight little cunt. She lets out a surprised gasp."
                if the_girl.get_opinion_score("being submissive") > 0:
                    "[the_girl.possessive_title] grabs at your back and moans right into your ear."
                    the_girl "Wait... I don't think I can... handle your big cock!"
                    $ the_girl.discover_opinion("being submissive")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    "You feel her body tremble beneath you and her pussy get suddenly wetter."
                    mc.name "It doesn't matter what you think. I'm going to fuck you until I'm done."
                    if the_girl.get_opinion_score("bareback sex") > 0:
                        the_girl "Oh my god, you're fucking me raw and going to get me pregnant... I'm such a worthless, dirty slut that you don't even care if you get me pregnant..."
                        $ the_girl.discover_opinion("bareback sex")
                    else:
                        the_girl "Oh my god... I'm just a worthless, dirty slut to you..."
                    "She shivers again, apparently turned on by the thought."
                    "You fuck [the_girl.possessive_title] hard and fast for as long as you can manage, but eventually you need to slow down to a more maintainable pace."

                else:
                    the_girl "Ow! Ow, please slow down..."
                    mc.name "You can manage."
                    $ the_girl.change_stats(obedience = -1 + the_girl.get_opinion_score("being submissive"), arousal = -1 + the_girl.get_opinion_score("being submissive"))
                    "[the_girl.title] pushes against you and forces you to slide out of her pussy."
                    the_girl "No, really, I need you to go slower or I can't do this"
                    "You finally nod and she lets you slide back inside of her. This time you move more slowly, and after a few moments you've moved past the incident."

    else:
        # INTRO: She takes you easily and wraps her arms around you.
        "[the_girl.title]'s slit is tight and wet as you fuck her. She moans into your ear."
        the_girl "Take me, [the_girl.mc_title], I'm all yours..."
        menu:
            "Fondle her tits":
                if the_girl.has_large_tits :
                    if the_girl.tits_available:
                        "You plant a hand on one of [the_girl.possessive_title]'s nice, soft tits and squeeze it. You use your thumb to rub her already hard nipple."
                        the_girl "Oh god, go easy on them. They're sensitive!"
                        "You enjoy the squishy weight of her breasts for a few moments, then shift your focus back to fucking her."

                    else:
                        "You plant a hand on [the_girl.possessive_title]'s big tits and fondle them through her [the_girl.outfit.get_upper_top_layer.display_name]."
                        the_girl "Mmm, you should just pull that out of the way. I want you to be able to grab them and squeeze them."

                else:
                    if the_girl.tits_available:
                        "You run a hand over [the_girl.possessive_title]'s cute little tits, pausing to pinch one of her nipples."
                        the_girl "Oh! Easy there, it's sensitive."
                        "You rub her nipple for a moment and feel it get hard, then move to her other breast and do the same."
                    else:
                        "You try and feel up [the_girl.possessive_title]'s little tits, but her [the_girl.outfit.get_upper_top_layer.display_name] stops you from getting much more than a handful of fabric."
                        "You give up and focus on fucking her instead."

            "Pin her down":
                "You grab [the_girl.title]'s hands and lift them above her head. You push them against the [the_object.name] and pin [the_girl.title] underneath you."
                if the_girl.get_opinion_score("being submissive") > 0:
                    the_girl "Oh my god [the_girl.mc_title], what are you going to do to me?"
                    "She bites her lip and looks up at you."
                    mc.name "Whatever I want. Keep your legs spread for me."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    $ the_girl.discover_opinion("being submissive")
                    $ play_moan_sound()
                    "You fuck her hard and fast. [the_girl.possessive_title] gasps and moans, her hips bucking with pleasure."
                    the_girl "Ah! You've got me held down and there's nothing I can do..."
                    "She tests your grip on her hands and shivers with pleasure when you force them back down and keep her in place. You can hear her talking softly to herself."
                    the_girl "I'm just a fuck toy to you right now... Just a soft wet hole for you to fuck with that big cock... Ah!"
                    if the_girl.get_opinion_score("bareback sex") > 0:
                        the_girl "You could fuck me until you cum inside. You might get me pregnant and all I can do is sit here and get fucked like a slut... Oh my god..."
                    elif the_girl.wants_creampie:
                        the_girl "You could cum right inside me and there's nothing I could do to stop you... You would just fuck me full of your cum!"
                    "[the_girl.title]'s pussy feels great to fuck, but you can't keep this pace up forever. You let go of her hands and slow down."
                    "You're both silent for a few seconds, panting for breath."
                    the_girl "Don't stop..."

                elif the_girl.get_opinion_score("being submissive") < 0:
                    the_girl "Whoah, easy there..."
                    mc.name "Keep those legs spread for me."
                    "She rolls her eyes and spreads her legs. You start to fuck her hard and fast."
                    the_girl "Let my hands go, I want to be able to feel you. I want to touch you."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    $ the_girl.discover_opinion("being submissive")
                    "It's clear [the_girl.title] isn't enjoying being dominated as much as you were expecting. You let her hands go and she pulls you close against her."
                    the_girl "Much better."

                else:
                    the_girl "Oh! Hello there..."
                    mc.name "Spread your legs for me, I want to get nice and deep."
                    "She does what you want and spreads her legs. You start to fuck her hard and fast."
                    the_girl "Fuck me... Oh fuck me harder!"
                    $ play_moan_sound()
                    "She pants and moans underneath you. You keep the pace up as long as you can manage, fucking [the_girl.title]'s tight, wet cunt while she's pinned underneath you."
                    "You keep up the pace as long as you can manage, but eventually you have to slow down and catch your breath."
                    the_girl "That was... that felt great, it was so intense."
                    "She licks at your ear, then whispers into it."
                    the_girl "Don't stop..."
    return

label scene_missionary_3(the_girl, the_location, the_object):
    #Girl asks you to indulge her fetishes if she has any. Otherwise generally encourages you.
    "[the_girl.possessive_title] leans forward a bit and begins to kiss your neck. Her lips peck up your neck and then she whispers in your ear."
    if the_girl.has_breeding_fetish:
        the_girl "I want you to cum inside me... push as deep as you can and unload!"
    elif the_girl.has_cum_fetish:
        the_girl "I can't wait to feel your cum... cum deep, or pull out and cum all over me... I just want your cum!"
    elif mc.condom:
        the_girl "You feel so good... I can feel you so deep. I love it!"
    elif the_girl.wants_creampie:
        the_girl "You feel so good inside me bare like this. It's okay if you want to cum inside me... I kind of want it too!"
    else:
        the_girl "Your cock feels so good... I can't wait until you pull out and cum all over me!"
    "Encouraged by her words, you speed up, fucking her faster. She runs her hand through your hair and starts to moan at your increased pace."
    menu:
        "Give her everything you've got":
            if the_girl.is_girlfriend:
                mc.name "That's it, you little minx. God I love fucking your tight cunt..."
            elif the_girl.is_affair:
                mc.name "Take it, slut. No man in your life fucks you the way I do."
            elif the_girl.is_single:
                mc.name "You are such a good little slut. God your cunt is so tight and slick."
            else:
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                mc.name "Take it bitch. God your cunt is so tight, so slick. I bet your [so_title] doesn't fuck you as good as I do."
            "[the_girl.possessive_title] clings to you as you fuck her, harder, faster, stronger."
            "You continue at what seems like an impossible pace for as long as you can."
            the_girl "Oh god [the_girl.mc_title]! OH fuck yes!"
            "She is moaning your name right in your ear, and it's really turning you on."
            $ the_girl.change_arousal(10)
            $ mc.change_arousal(10)
        "Tease her":
            the_girl "That's it... oh god [the_girl.mc_title]!"
            "Her body is clinging to you as you start to speed up, but you change up, pushing deep inside her and holding it there."
            the_girl "Oh my god... keep... keep going!"
            "She tries to buck her hips against you, but your weight is pinning her against the [the_object.name]."
            mc.name "You didn't say the magic word."
            if the_girl.arousal_perc > 80:
                the_girl "Please... I'm so close... just a little more!"
            else:
                the_girl "It feels good... just... keep going! Please!"
            mc.name "I'm not sure if you really mean it."
            the_girl "Fuck me please! Fuck me hard and don't stop until I'm cumming my brains out!"
            $ play_moan_sound()
            "Instead of answering, you ease up the pressure and begin to fuck her earnestly again. Her eyes close and she moans as you continue."
            $ the_girl.change_obedience(2)

    return

label outro_missionary(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum outside", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax."
        "She gasps and claws lightly at your back as you pump your seed into her."
        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."

            call post_orgasm_condom_routine(the_girl, missionary) from _call_post_orgasm_condom_routine_missionary

        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ missionary.redraw_scene(the_girl)
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            "You take a moment to catch your breath, then roll off of [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum outside":
        if mc.condom == False and (the_girl.has_cum_fetish or the_girl.wants_creampie):
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God,", "Oh yes", "Oh... OH! Yes "])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.sex_skills["Vaginal"] > 3:
                "[the_girl.possessive_title] pulls your body close to hers, burying your cock as deep as she can and milks it with the muscles inside her pussy."
                "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
            $ missionary.redraw_scene(the_girl)
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! You were meant to cum inside me!"
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            $ wordchoice = renpy.random.choice(['Relax', "Don't panic", 'Stay calm', 'Chill', "It's okay"])
            $ wordchoice2 = renpy.random.choice(['the pill', 'birth control'])
            if the_girl.knows_pregnant:# The personality reactions but should it not be True instead of False?
                the_girl "[wordchoice], [the_girl.mc_title]. I'm already pregnant remember?"
            elif the_girl.on_birth_control:
                the_girl "[wordchoice], [the_girl.mc_title]. I'm on [wordchoice2]."
            elif the_girl.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_girl.relationship)
                the_girl "[wordchoice], [the_girl.mc_title]. If anything happens I'll tell my [so_title] it's his."
            else:
                if the_girl.love >59:
                    the_girl "I love you, [the_girl.mc_title]. We should make a baby together."
                elif the_girl.love >0:
                    pass
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."
        else:
            $ mid_sentence = "You kneel and stroke yourself off"
            $ target = "taking aim at [the_girl.title]'s stomach"
            if mc.condom:
                $ mid_sentence = "You whip off your condom and stroke yourself off"
            if the_girl.is_pregnant and the_girl.pregnancy_is_visible:
                $ target = "taking aim at [the_girl.title]'s pregnancy bump"

            "You pull out at the last moment and grab your cock. [mid_sentence], [target]."
            $ mid_sentence = None
            $ target = None

            $ the_girl.cum_on_stomach()
            $ missionary.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title]'s body goes rigid as your cum splashes onto her skin. Goosebumps erupt all over her body as her brain registers your cum on her."
                $ play_moan_sound()
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her. She moans lewdly."
                "She truly is addicted to your cum."
            else:
                the_girl "Ah... Good job... Ah..."
                "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."
    return

label transition_missionary_piledriver(the_girl, the_location, the_object):
    "[the_girl.title]'s pussy feels so warm and inviting, you can't help but want to get deeper inside of her. You pause for a moment and reach down for her legs."
    the_girl "Hey, what's... Whoa!"
    "You pull her legs up and bend them over her shoulders. You hold onto her ankles as you start to fuck her again, pushing your hard cock nice and deep."
    return

label transition_default_missionary(the_girl, the_location, the_object):
    $ missionary.redraw_scene(the_girl)
    "You put [the_girl.title] on her back and lie down on top of her, lining your hard cock up with her tight cunt."
    "After running the tip of your penis along her slit a few times you press forward, sliding inside of her. She gasps softly and closes her eyes."
    return

label strip_missionary(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = missionary.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She sighs happily when you slip back inside of her."
    return

label strip_ask_missionary(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you fuck her."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = missionary.position_tag)
            "You move back to your knees for a moment while [the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She sighs happily when you get on top of her and slide your cock back inside."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips against yours and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her hips against you and moans ecstatically."
            return False
    return

label orgasm_missionary(the_girl, the_location, the_object):
    "[the_girl.title] turns her head and pants loudly. Suddenly she bucks her hips up against yours and gasps."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "Her pussy is dripping wet as you fuck through her climax. She paws at the [the_object.name], trying to find something to hold onto."
    "After a few seconds she lets out a long sigh and all the tension drains out of her body. You slow down your thrusts to catch your own breath."
    the_girl "Don't stop [the_girl.mc_title], I might be able to get there again..."
    return
