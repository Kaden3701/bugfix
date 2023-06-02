init python:
    anal_cowgirl = Position("Anal Cowgirl", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
        position_tag = "cowgirl", requires_location = "Lay",  requires_clothing = "Vagina", skill_tag = "Anal",
        girl_arousal = 22, girl_energy = 20,
        guy_arousal = 16, guy_energy = 14,
        connections = [],
        intro = "intro_anal_cowgirl",
        scenes = ["scene_anal_cowgirl_1","scene_anal_cowgirl_2","scene_anal_cowgirl_3","scene_anal_cowgirl_4"],
        outro = "outro_anal_cowgirl",
        transition_default = "transition_default_anal_cowgirl",
        strip_description = "strip_anal_cowgirl", strip_ask_description = "strip_ask_anal_cowgirl",
        taboo_break_description = "taboo_break_anal_cowgirl",
        orgasm_description = "orgasm_anal_cowgirl",
        verb = "ass fuck",
        opinion_tags = ["taking control", "anal sex", "anal creampie"], record_class = "Anal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "anal_sex")

    list_of_girl_positions.append(anal_cowgirl)
    anal_cowgirl.girl_outro = "GIC_outro_anal_cowgirl"

#init 1:
#    python:
#        ##Here is where you would put connections if they existed.

label intro_anal_cowgirl(the_girl, the_location, the_object):
    the_girl "Lie down for me, I want to be on top."
    "You lie down on the [the_object.name] and undo your pants."
    "[the_girl.possessive_title] swings a leg over your body and straddles you."
    the_girl "I'm gonna put it in my ass. Let's get you lubed up first though..."
    if the_girl.vagina_visible:
        "She leans back and grinds herself against you. The shaft of your cock rubs against the lips of her pussy."
    else:
        "She leans back and grinds herself against you. Underneath her [the_girl.outfit.get_lower_top_layer.display_name] you can feel the lips of her pussy sliding along the length of your shaft."
    "She grinds up against you for several seconds, until your cock glides pleasingly along her wet slit."
    if not the_girl.vagina_available:
        "She quickly moves some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_cowgirl.position_tag, visible_enough = True, prefer_half_off = True)
    the_girl "Ready?"
    if the_girl.sex_skills["Anal"] > 3:
        "You nod. She grinds forward one last time, then lifts herself up. She reaches back behind her and guides your cock to the entrance of her puckered hole."
        "With a grunt, she slowly lets her body weight sink down on top of you. Her sphincter finally gives way with a pleasing pop, and she slowly sinks down on top of you."
    else:
        "You nod and she lifts herself up. She reaches down with one hand and holds onto your cock to hold it steady."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight ass."
    if the_girl.has_anal_fetish:
        the_girl "OH! Thank god. I needed this so bad."
        "[the_girl.possessive_title] settles in with the familiar feeling of your dick in her ass."
    else:
        the_girl "Ah..."
    "After pausing for a second to adjust [the_girl.possessive_title] starts to ride your dick."
    return

label scene_anal_cowgirl_1(the_girl, the_location, the_object):
    if the_girl.arousal_perc > 50:
        "[the_girl.possessive_title] leans back, putting her hands in line with your feet."
        "In her reclined position you have a perfect view of her drooling pussy. Just below it you can see your cock stretching her nice little asshole."
        if the_girl is mom:
            the_girl "Oh god [the_girl.mc_title], you make [the_girl.title] feel so good... You grew up into such a good man!"
            mc.name "Mmm, [the_girl.title] your ass is amazing. It's so tight!"
        elif the_girl.has_anal_fetish:
            the_girl "God, do you see how good it makes me feel? Having your cock in my ass feels so fucking good!"
            mc.name "It's so tight too, your ass is amazing."
        else:
            the_girl "Does that feel good? It feels even bigger when it's in my ass like this."
            mc.name "Mmm, [the_girl.title] your ass is amazing. It's so tight!"

    else:
        "[the_girl.possessive_title] leans back, putting her hands in line with your feet, and slows down her rhythm."
        the_girl "I need to take it a little slow. I need to get warmed up before I can really take it hard when it's in my ass."
        "You have a perfect view of her pussy. It is just starting to show some early signs of arousal. Just below it you can see your cock stretching her nice little asshole."
        mc.name "Take all the time you need. Your ass is so tight, even completely still it feels amazing."
    "[the_girl.possessive_title] rocks her hips back and forth. Each movement feels like her tight back passage is milking you, begging for you to cum in it."
    return

label scene_anal_cowgirl_2(the_girl, the_location, the_object):
    "[the_girl.possessive_title] speeds up, working her thighs to pump herself up and down your cock."
    "Her ass makes a few lewd squelching noises from her aggressive fucking. Her buttery smooth puckered hole strokes your erection with every pump."
    if the_girl.has_large_tits:
        if the_girl.tits_visible:
            "Her large, unconstrained [the_girl.tits_description] bounce up and down with each stroke."
            the_girl "Fuck, hold onto these!"
            "[the_girl.possessive_title] reaches down and grabs your hands. She brings them up to her tits and plants them there."
            $ play_moan_sound()
            "She moans and grinds your hands into her breasts, then puts her hands on your chest and focuses on fucking you."
        else:
            $ the_clothing = the_girl.outfit.get_upper_top_layer
            "Her [the_girl.tits_description] are barely contained by her [the_clothing.display_name]. You watch them bounce around as she fucks you vigorously."
            menu:
                "Pull her [the_clothing.display_name] off":
                    "You reach up and start to pull at her [the_clothing.display_name]. She stops fucking you for a moment as she moves her arms to give you better access."
                    mc.name "I want a better look at your tits while you fuck me."
                    $ the_girl.draw_animated_removal(the_clothing, position = anal_cowgirl.position_tag) #Hopefully this copy paste works.
                    "Now free of her [the_clothing.display_name], [the_girl.possessive_title] resumes fucking you."
                "Play with her pussy":
                    "You quickly stick your thumb in your mouth to get it wet, then reach down and start to rub her clit with your thumb as she rides you."
                    if the_girl.get_opinion_score("being fingered") > 0:
                        $ play_moan_sound()
                        "[the_girl.possessive_title] moans as you start to play with her."
                        the_girl "Oh! That feels good. Makes it easier to handle buttsex when you touch me like that."
                        $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being fingered", "anal sex"]))
                    else:
                        the_girl "That feels good... Keep going that makes this easier."
                    "You push a finger up inside her while you continue to use your thumb to rub her love button. As she bounces up and down on your cock you can feel your cock deep inside her ass through the thin vaginal wall."
                    "You stroke yourself a bit through her vagina while she fucks you. It's a very unique feeling, and very pleasurable!"
            $ the_clothing = None
            return

    else:
        if the_girl.tits_visible:
            "She reaches up and grabs onto one of her own [the_girl.tits_description], squeezing it while she rides you."
            the_girl "Ah!"
            "You decide to get in on the action. You reach up and grab her other breast."
            $ play_moan_sound()
            "She moans as you rub and tweak her breasts. She puts her hands on your chest and focuses on fucking you."
        else:
            $ the_clothing = the_girl.outfit.get_upper_top_layer
            "She reaches up and grabs onto one of her [the_girl.tits_description] through her [the_clothing.display_name]. She kneads it through the fabric and moans loudly while she rides you."
            the_girl "Ah!"
            menu:
                "Pull her [the_clothing.display_name] off":
                    "You reach up and start to pull at her [the_clothing.display_name]. She stops fucking you for a moment as she moves her arms to give you better access."
                    mc.name "I want a better look at your tits while you fuck me."
                    $ the_girl.draw_animated_removal(the_clothing, position = anal_cowgirl.position_tag) #Hopefully this copy paste works.
                    "Now free of her [the_clothing.display_name], [the_girl.possessive_title] resumes fucking you."
                "Play with her pussy":
                    "You quickly stick your thumb in your mouth to get it wet, then reach down and start to rub her clit with your thumb as she rides you."
                    if the_girl.get_opinion_score("being fingered") > 0:
                        $ play_moan_sound()
                        "[the_girl.possessive_title] moans as you start to play with her."
                        the_girl "Oh! That feels good. Makes it easier to handle buttsex when you touch me like that."
                        $ the_girl.change_arousal(2 * the_girl.get_opinion_score(["being fingered", "anal sex"]))
                    else:
                        the_girl "That feels good... Keep going that makes this easier."
                    "You push a finger up inside her while you continue to use your thumb to rub her love button. As she bounces up and down on your cock you can feel your cock deep inside her ass through the thin vaginal wall."
                    "You stroke yourself a bit through her vagina while she fucks you. It's a very unique feeling, and very pleasurable!"
            $ the_clothing = None
            return
    "You give her nipple a pinch. You roll it between your finger and thumb."
    if the_girl is mom:
        the_girl "[the_girl.mc_title]! [the_girl.title] loves it when you play with her nipples."
    else:
        the_girl "Mmm, I love it when you play with my tits!"
    if the_girl.has_large_tits:
        "You give her epic tits another squeeze. They are so full and soft and feel heavy in your hands."
    else:
        "You give her modest tits another squeeze. They are supple yet firm in your hands."
    return

label scene_anal_cowgirl_3(the_girl, the_location, the_object):
    "You put your hands on [the_girl.possessive_title]'s hips and guide her up and down at a steady pace."
    if the_girl.arousal_perc > 75:
        "Your cock glides in and out of her tight, supple ass. [the_girl.possessive_title] is so excited her pussy is dripping her juices onto you."
    else:
        "Her ass is warm and tight. You glide in and out of her at her pace."
    if the_girl.has_anal_fetish:
        "[the_girl.possessive_title] leans forward. She runs one hand through your hair and the other she puts on your chest."
        the_girl "Mmmm, your cock feels so good [the_girl.mc_title]. I crave it, stuffing my tight little asshole constantly." #NOTE: mc_title can be the_girl.mc_title
        "[the_girl.possessive_title] stops rocking her hips for a few minutes. Pausing just to enjoy the exquisite fullness your erection gives her."
    else:
        "With [the_girl.possessive_title] in control you're able to relax and focus entirely on enjoying the feeling."
    return

label scene_anal_cowgirl_4(the_girl, the_location, the_object):
    "[the_girl.possessive_title] slows her strokes down, eventually stopping as she sits on top of you, your cock buried deep in her ass."
    if the_girl.has_anal_fetish:
        if the_girl.arousal_perc > 85:
            "Even though she stopped, you can still feel her body twitching and pulsing around you."
            "It seems like she's trying to edge herself a bit, but her breathing is getting more ragged despite her lack of movement."
            the_girl "Oh fuck... I just want a second... I'm not ready to cum yet...!"
            "She tries to keep herself from getting off too soon, but her hips are starting to twitch a bit on their own."
            "[the_girl.title] gives one small stroke of her hips and gasps. There is no way she can stop herself from cumming now."
            $ the_girl.change_arousal(5)
            "Suddenly, [the_girl.possessive_title] is fucking you with incredible need."
            the_girl "Oh fuck! Oh!"
        else:
            "Even though she stopped, you can still feel movement as [the_girl.title] starts to clench and unclench her ass around you."
            the_girl "Fuck you are so big... it feels so good to just have you deep for a bit."
            "[the_girl.possessive_title]'s subtle strokes and heavy breathing is really turning you on. It's clear she is savoring having your cock deep in her ass."
            $ mc.change_arousal(5)
    elif the_girl.sex_skills["Anal"] > 3 and the_girl.get_opinion_score("anal sex") > 0:
        if the_girl.arousal_perc > 90:   #She tries to edge herself.
            "Even though she stopped, you can still feel her body twitching and pulsing around you."
            "It seems like she's trying to edge herself a bit, but she is still slowly getting herself off from the pleasure of having her ass filled."
            if the_girl.tits_available:
                "Not content to let her off easy, you reach up and grab her tits. When you pinch her nipples you feel her ass clench your cock."
                the_girl "Ah! Hey! I need a second... I'm... I'm not ready to cum yet...!"
                "[the_girl.title] protests, but doesn't move to stop you, so you pinch her nipples again."
            else:
                "Not content to let her off easy, you reach down and grab her hips. You move her body side to side a bit, stirring your cock inside her."
                the_girl "Ah! Hey! I need a second... I'm... I'm not ready to cum yet...!"
                "[the_girl.title] protests, but doesn't move to stop you, so you keep going."
            "[the_girl.title] gives one small stroke of her hips and gasps. There is no way she can stop herself from cumming now."
            $ the_girl.change_arousal(5)
            "Suddenly, [the_girl.possessive_title] is fucking you with incredible need."
            the_girl "Oh fuck! Oh!"
        else:
            the_girl "Your cock is so big... it feels good even when I'm not moving."
            "[the_girl.title]'s ass clenches and unclenches around your cock slowly. You can tell she is doing it on purpose."
            $ mc.change_arousal(5)
            "It feels amazing to have her stroking you without even moving. You lay back and enjoy it."

    else:   #A chance to train her
        the_girl "Sorry, I... I just need a second... this is so intense!"
        if the_girl.arousal_perc > 90 and the_girl.get_opinion_score("anal sex") < 1:
            "You can tell that even though she doesn't particularly enjoy it, [the_girl.title] is getting off on this. You decide to push it a bit."
            mc.name "Wow, you are dripping. You are really getting off on this aren't you?"
            the_girl "No! I... I mean... your cock in inside me... of course it's going to feel a little bit good..."
            mc.name "It's not just a little bit good though, is it? You are starting to like it like this, are you, you little butt slut?"
            if ((the_girl.suggestibility + the_girl.arousal) / 2) > renpy.random.randint(0,100):    #Odds of improvement are average of suggestability and arousal. Because of conditions base chance of 45%
                the_girl "I... oh god... I think you're right..."
                $ the_girl.increase_opinion_score("anal sex")
                $ the_girl.change_arousal(2 * the_girl.get_opinion_score("anal sex"))
                "[the_girl.title] gives one small stroke of her hips and gasps."
                the_girl "It's you! You make it so good... oh fuck!"
                "Suddenly, [the_girl.possessive_title] is fucking you with need."
            else:
                the_girl "I... no... I'm not a butt slut!"
                "Despite your urging, [the_girl.possessive_title] resists your training."
        elif the_girl.arousal_perc > 90 and the_girl.sex_skills["Anal"] < 3:
            "You can tell that [the_girl.title] is really enjoying herself, but is struggling with being on top during anal."
            mc.name "Wow, you are dripping. Are you going to get off soon?"
            the_girl "I want to... It's just so big! I... I'm not sure I can do this..."
            mc.name "Shhh, it's okay. Don't focus on me, just focus on yourself. Think about your body, how good it feels, then force your ass to relax."
            the_girl "I... I'm trying... it just hurts a little, but it feels so good too."
            mc.name "Close your eyes, take a deep breath. Remember this isn't a race."
            "[the_girl.title] closes her eyes and sighs. You can feel it as her ass slightly unclenches around you."
            $ the_girl.increase_sex_skill("Anal")
            $ play_moan_sound()
            "She gives you a slow stroke and moans."
            mc.name "That's it. You're doing great. I'll make you my little butt slut soon enough. You want to be my butt slut, don't you?"
            the_girl "Oh fuck... I do!"
            $ the_girl.change_arousal(2 * the_girl.get_opinion_score("anal sex"))
            "[the_girl.title] gives another small stroke of her hips and gasps."
            "[the_girl.possessive_title] is speeding up now, her body leading her to her orgasm."
        else:
            mc.name "It's okay. Take your time."
            if the_girl.tits_available:
                "You reach up and grab her tits. When you pinch her nipples you feel her ass clench your cock."
                the_girl "Ah! Mmm, that feels good, do that again..."
                $ play_moan_sound()
                "You pinch her nipples again. She moans in response."
            else:
                "To help her relax, you decide to her off a little. You reach down with your hand and stroke her a slit."
                the_girl "Ahhh... that feels nice."
                "[the_girl.title] closes her eyes as you touch her pussy. When you flick her clit with your thumb, you feel her ass clench around you."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
            the_girl "Mmm... okay, I'm going to keep going..."
            "Slowly, [the_girl.possessive_title] starts to move her hips again, her backdoor accepting you more and more."





    return

label outro_anal_cowgirl(the_girl, the_location, the_object):
    "With each stroke of her hips [the_girl.possessive_title]'s impossibly tight ass brings you closer and closer to cumming. You're finally driven past the point of no return."
    mc.name "Fuck, I'm going to cum!"

    if mc.condom:
        the_girl "Yes! Ah!"
        "[the_girl.possessive_title] drops herself down, grinding her hips against yours and pushing your cock as deep into her ass as possible."
        "Your cock erupts and begins filling the condom. She sighs when she feels the heat from it."
        $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
        the_girl "Ah... I hope the condom didn't break!"
        "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
        "The condom is full of your potent seed."
        call post_orgasm_condom_routine(the_girl, anal_cowgirl) from _call_post_orgasm_condom_routine_anal_cowgirl

    elif the_girl.sluttiness > 70 and the_girl.get_opinion_score("anal creampies") > 0 and the_girl.get_opinion_score("anal sex") > 0:
        #She drops down on you as you cum.
        if the_girl.has_anal_fetish:
            the_girl "Yes! Finish in my ass... I need it in my ass!"
        else:
            the_girl "Yes! Ah!"
        "[the_girl.possessive_title] drops herself down, grinding her hips against yours and pushing your cock as deep into her ass as possible."
        "Her breath catches in her throat when you pulse out your hot load of cum deep inside of her."
        if the_girl is mom:
            the_girl "That's it baby! Give your cum to [the_girl.title]!"
        else:
            the_girl "Oh my god... Give it all to me [the_girl.mc_title]... Fill my ass up!"
        $ the_girl.cum_in_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
        $ anal_cowgirl.redraw_scene(the_girl)
        if the_girl.has_cum_fetish:
            the_girl "Yes, I can feel it, give me more, I need more..."
        else:
            the_girl "Oh yes... so full..."
        "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
        "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    elif the_girl.sluttiness < 30 or the_girl.get_opinion_score("anal creampies") < 0:
        #She always pull off and you cum on her stomach.
        the_girl "Oh shit, don't cum in my ass!"
        "[the_girl.possessive_title] jerks up, pulls off your cock, and lowers herself back down."
        "She leans back and uses one hand to push your shaft against the lips of her pussy, grinding against it until you climax."
        the_girl "Cum for me [the_girl.mc_title], I want you to cum on me!"
        "You tense up and cum, shooting your thick load up and onto [the_girl.possessive_title]'s stomach. She keeps grinding against your cock until you are completely spent."
        $ the_girl.cum_on_stomach()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ anal_cowgirl.redraw_scene(the_girl)

    else:
        #She hesitates and you can decide to pull her down or not.
        "[the_girl.possessive_title] starts to pull up and off of you. She hesitates with the tip of your cock just inside of her ass."
        the_girl "I... I really shouldn't let you..."
        $ play_moan_sound()
        "She bites her lip and moans, unsure of what to do."
        menu:
            "Pull her down and cum inside her":
                "You reach up and grab [the_girl.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
                "The feeling of her tight, warm ass sliding down and engulfing your cock again pushes you over the edge. You pull [the_girl.possessive_title] tight against you and unload inside of her."
                if the_girl.has_cum_fetish:
                    the_girl "Yes, I can feel it, give me more, I need more..."
                else:
                    the_girl "Ah! Fuck... so full..."
                $ the_girl.change_obedience(3)
                $ the_girl.cum_in_ass()
                $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
                $ anal_cowgirl.redraw_scene(the_girl)
                "You give a few half-hearted pumps when you're done, then tap [the_girl.possessive_title] on the ass. She slides off of your dick and collapses beside you."

            "Let her pull off and cum on her stomach":
                "You stay silent. [the_girl.possessive_title] waits another second, as if waiting to be convinced, then pulls off of your cock."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_girl.cum_on_stomach()
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
                $ anal_cowgirl.redraw_scene(the_girl)
                the_girl "Whew, that was close..."

        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    return

label transition_default_anal_cowgirl(the_girl, the_location, the_object):
    $ anal_cowgirl.redraw_scene(the_girl)
    "You lie down on [the_object.name]. [the_girl.possessive_title] swings a leg over your waist and straddles you."
    if not the_girl.vagina_available:
        "She moves some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = anal_cowgirl.position_tag, visible_enough = True, prefer_half_off = True)
    if the_girl.sex_skills["Anal"] > 3:
        "You nod. She grinds forward one last time, then lifts herself up. She reaches back behind her and guides your cock to the entrance of her puckered hole."
        "With a grunt, she slowly lets her body weight sink down on top of you. Her sphincter finally gives way with a pleasing pop, and she slow sinks down on top of you."
    else:
        "You nod and she lifts herself up. She reaches down with one hand and holds onto your cock to hold it steady."
        "When she has you in place she lowers herself down slowly, sliding you inch by inch into her tight ass."
    the_girl "Ah..."
    "After pausing for a second to adjust [the_girl.possessive_title] starts to ride your dick."
    return

label strip_anal_cowgirl(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = anal_cowgirl.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.display_name] and throws it to the side."
    return

label strip_ask_anal_cowgirl(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.display_name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = anal_cowgirl.position_tag)
            "[the_girl.possessive_title] slows down her pace while she strips out of her [the_clothing.display_name]. When she's free of it she puts her hands on your chest and fucks you faster again."

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 70:
                the_girl "Yeah? Do I look sexy in it?"
                "She sighs happily while she rides you."
            else:
                the_girl "Yeah? Do I look like a good little slut in it? Because that's what I feel like right now!"
                "She sighs happily while she rides your cock hard and fast."
    return

label orgasm_anal_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title] works her hips faster and her breathing grows heavier."
    $ the_girl.call_dialogue("climax_responses_anal")
    "With one last gasp she collapses down against you. Her thighs quiver as she climaxes. Her velvet smooth ass quivers around your erection as she cums."
    "After a second [the_girl.possessive_title] regains control of herself. Her breath is warm against your ear as she whispers to you."
    if the_girl.has_anal_fetish:
        the_girl "Every time you're in my ass, it's like I just can't stop cumming..."
    else:
        the_girl "I can't stop now, I want you to make me cum again!"
    "She leans back and starts to ride you faster than ever."
    return

label taboo_break_anal_cowgirl(the_girl, the_location, the_object):
    # TODO: initial dialog needs a little more substance.
    "You slap [the_girl.possessive_title]'s ass and give it a squeeze."
    if the_girl.effective_sluttiness(anal_standing.associated_taboo) > anal_standing.slut_cap or the_girl.get_opinion_score("showing her ass") > 0:
        mc.name "Now sit on my cock and shove it into your cute little butt."
        $ anal_cowgirl.redraw_scene(the_girl)
        "You lay down on the [the_object.name] and she straddles your body getting herself into position to ride your cock."
    else:
        "You lay down on the [the_object.name] and tell her to crouch down on your dick."
        $ anal_cowgirl.redraw_scene(the_girl)
        mc.name "Now sit down and push it into your cute little ass."

    $ the_girl.call_dialogue(anal_standing.associated_taboo+"_taboo_break")

    "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you press it against her tight hole."
    if the_girl.sex_skills["Anal"] > 3:
        "She gasps as your tip starts to spread her open, but continues to lower herself down on your throbbing cock."
        the_girl "Oh god... Mfphhhh!"
    else:
        "She gasps as your tip tries to spread open her impossibly tight asshole."
        mc.name "Come on, you'll get there."
        "She spits on your cock and tries again. This time making better progress, sliding the tip of your dick into her ass."
        the_girl "Oh god... Fuck!"
    return

label GIC_outro_anal_cowgirl(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal == "hate fuck" or the_goal == "waste cum":
        if mc.condom:
            $ anal_cowgirl.call_default_outro(the_girl, the_location, the_object)
        "With each stroke of her hips [the_girl.possessive_title]'s impossibly tight ass brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        the_person "Thank god, I was about to hop off and just leave you hanging."
        "She stops moving her hips."
        the_person "Maybe I should do that anyway..."
        "She starts to pull up off of you."
        menu:
            "Grab her hips":
                mc.name "You'll get up when I tell you to."
                "You grab [the_girl.possessive_title]'s hips and force her back down."
                the_person "Hey, what the fuck!"
                $ the_person.change_stats(obedience = 5, love = -3)
                "You hold her in place as you cum into her tight ass. She squirms a little bit but she also gasps a bit."
                $ the_girl.cum_in_ass()
                $ anal_cowgirl.redraw_scene(the_girl)
                $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
                "As soon as you let go of her she immediately pops off and stands over you. Her ass gives a little squelch as your cum leaks from it onto you chest."
                the_person "God dammit, that's now how that was supposed to go. Next time I'm putting handcuffs on you first..."
            "Beg her to finish inside":
                mc.name "No! Stop! Please! I want to cum inside you so bad!"
                "[the_person.title] smiles and stops, leaving just the tip of your cock in her puckered hole."
                the_person "Oh, is that so? Is my ass so good, you want to defile it with your awful sperm?"
                "You try to thrust your hips, but she backs off even further, leaving you too close to popping out."
                mc.name "Oh fuck, just finish me off please!"
                if the_goal == "hate fuck":
                    the_person "Oh fuck it."
                    "[the_person.possessive_title] drops her hips back down onto you, sheathing your cock in her tight asshole completely."
                    "There's a hint of devilish mischief in her eyes as she rocks her hips back and forth, coaxing your cum from your body."
                    "You finally erupt. She gasps as she feels the heat of it in her body."
                    $ the_girl.cum_in_ass()
                    $ anal_cowgirl.redraw_scene(the_girl)
                    $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
                    "As soon as you finish she immediately pops off and stands over you. Her ass gives a little squelch as your cum leaks from it onto you chest."
                else:
                    the_person "I love to hear you beg, but not a chance."
                    "She pulls of you completely and starts to stroke you with her hand. You groan but are immediately firing off your sperm into the air. It lands on your stomach, making a mess."
                    "When you finish, she wipes her hand on your leg."
                    the_person "All that wasted seed... oh well! Better luck next time!"


    elif the_goal == "anal creampie":
        if mc.condom:
            the_person "Oh my god... hang on! I need to feel this!"
            "She suddenly pops off you. You look down confused, but then see her pulling desperately at the condom, ripping it off."
            "She quickly lines you up and sits back down on your cock, burying it deep in her ass."
            $ mc.condom = False
        "Instead of going up and down, she starts rocking her hips forward and back, milking your cock while keeping it buried deep."
        the_person "Do it... I want to feel it deep!"
        "Her words push you over the edge. Your cock explodes deep inside her bowel. She moans as she feels her body filling up."
        $ the_girl.change_obedience(3)
        $ the_girl.cum_in_ass()
        $ anal_cowgirl.redraw_scene(the_girl)
        $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_girl)
        "You give a few half-hearted pumps when you're done, then tap [the_girl.possessive_title] on the ass. She slides off of your dick and collapses beside you."
    elif the_goal == "body shot":
        "[the_person.possessive_title] pulls off."
        if mc.condom:
            "She quickly reaches down and pulls off  your condom, throwing it to the side."
        "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
        the_girl "Cum for me [the_girl.mc_title], I want you to cum on me!"
        "You tense up and cum, shooting your thick load up and onto [the_girl.possessive_title]'s stomach. She keeps grinding against your cock until you are completely spent."
        $ the_girl.cum_on_stomach()
        $ anal_cowgirl.redraw_scene(the_girl)
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    else:
        $ anal_cowgirl.call_default_outro(the_girl, the_location, the_object)
