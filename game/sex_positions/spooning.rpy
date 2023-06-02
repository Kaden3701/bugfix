init python:
    spooning_sex = Position(name = "Spooning", slut_requirement = 60, slut_cap = 85, requires_hard = True, requires_large_tits = False,
        position_tag = "back_peek", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
        girl_arousal = 12, girl_energy = 7,
        guy_arousal = 12, guy_energy = 10,  #A relaxed, low energy position
        connections = [],
        intro = "intro_spooning",
        scenes = ["scene_spooning_1","scene_spooning_2"],
        outro = "outro_spooning",
        transition_default = "transition_default_spooning",
        strip_description = "strip_spooning", strip_ask_description = "strip_ask_spooning",
        orgasm_description = "orgasm_spooning",
        taboo_break_description = "taboo_break_spooning",
        opinion_tags = ["doggy style sex","vaginal sex", "being submissive"], record_class = "Vaginal Sex",
        default_animation = missionary_bob,
        associated_taboo = "vaginal_sex")
    # not available as normal position
    # list_of_positions.append(spooning) #I can't list this until I come up with a taboo break.

init 5 python:
    spooning_sex.double_orgasm = "spooning_double_orgasm"

# init 1:
#     python:
#         missionary.link_positions(piledriver,"transition_missionary_piledriver")

label intro_spooning(the_girl, the_location, the_object):
    "You turn lay down with [the_girl.title] so her back is to you, laying beside her on the [the_object.name]."
    mc.name "Just lay down. I'm going to lay behind you."
    "Your cock is hard. You rub it up against [the_girl.title]'s ass, grinding a bit."
    "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
    "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
    the_girl "Oh [the_girl.mc_title]. Mmmmmm..."
    "You give her a few tentative strokes, and soon you are established in a nice, easy rhythm."
    return

label taboo_break_spooning(the_girl, the_location, the_object):
    pass
    return

label scene_spooning_1(the_girl, the_location, the_object):

    "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body responds to the stimulation."
    "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
    "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
    if the_girl.has_large_tits :
        if the_girl.tits_available:
            the_girl "Oh god, handle with care [the_girl.mc_title]..."
            "[the_girl.possessive_title]'s hot and ample tit flesh feels great in your hand."
            "You enjoy the squishy weight of her breasts for a few moments, then shift your focus back to fucking her."
        else:
            "[the_girl.possessive_title]'s tits feel amazing, even through her [the_girl.outfit.get_upper_top_layer.display_name]."
            the_girl "Mmm, you should just pull that out of the way. I want you to be able to grab them and squeeze them."
    else:
        if the_girl.tits_available:
            "[the_girl.possessive_title]'s cute [the_girl.tits_description] feel firm and hot in your hand."
            the_girl "Oh! Mmm, gentle with me [the_girl.mc_title]."
            "You rub her nipple for a moment and feel it get hard, then move to her other breast and do the same."
        else:
            "[the_girl.possessive_title]'s tits feel perky, even through her [the_girl.outfit.get_upper_top_layer.display_name]."
            the_girl "Mmm, you should just pull that out of the way. I want you to be able to grab them and squeeze them."
    return

label scene_spooning_2(the_girl, the_location, the_object):
    the_girl "God [the_girl.mc_title], you feel so big like this! Fuck me good!"
    "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
    "You pick up the pace and begin to fuck her earnestly for a bit."
    "[the_girl.possessive_title] reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
    "Her ass is making smacking noises every time your hips drive your cock deep inside of her."
    return


label outro_spooning(the_girl, the_location, the_object):
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside of her", "pussy"],["Cum on her ass","body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        $ play_moan_sound()
        "You push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She gasps and moans."

        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You take a moment to catch your breath, then on your back next to [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."

            call post_orgasm_condom_routine(the_girl, spooning) from _call_post_orgasm_condom_routine_spooning

        else:
            $ climax_controller.do_clarity_release(the_girl)
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ spooning_sex.redraw_scene(the_girl)
            if the_girl.has_cum_fetish or the_girl.has_breeding_fetish:
                "[the_girl.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
                the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
                "[the_girl.possessive_title] revels in having her fetish fulfilled."
            if the_girl.knows_pregnant:
                the_girl "Oh god... no wonder I got knocked up..."
            elif the_girl.sluttiness > 90:
                the_girl "Oh god it's so deep."
            elif the_girl.on_birth_control:
                the_girl "Oh fuck...  Good thing I'm on the pill..."
            else:
                the_girl "Oh fuck... I could get pregnant you know.."
        "You take a moment to catch your breath, then roll on your back next to [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum on her ass":
        $ the_girl.cum_on_ass()
        $ spooning_sex.redraw_scene(the_girl)
        if mc.condom:
            "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s ass."
        else:
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s ass."
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            "She truly is addicted to your cum."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."
    return

label transition_default_spooning(the_girl, the_location, the_object):
    mc.name "Just lay down. I'm going to lay behind you."
    $ spooning_sex.redraw_scene(the_girl)
    "You turn lay down with [the_girl.title] so her back is to you, laying beside her on the [the_object.name]."
    "Your cock is hard. You rub it up against [the_girl.title]'s ass, grinding a bit."
    "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
    "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
    the_girl "Oh [the_girl.mc_title]. Mmmmmm..."
    "You give her a few tentative strokes, and soon you are established in a nice, easy rhythm."
    return

label strip_spooning(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = spooning_sex.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She sighs happily when you slip back inside of her."
    return

label strip_ask_spooning(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.title] pants as you fuck her."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = spooning_sex.position_tag)
            "You move back kneel for a moment while [the_girl.title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She sighs happily when you slide your cock back inside."

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
    return

label orgasm_spooning(the_girl, the_location, the_object):
    the_girl "Oh fuck, yes! YES!"
    "[the_girl.possessive_title] shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "Her [the_girl.pubes_description] pussy is dripping wet as you fuck through her climax. She paws at the [the_object.name], trying to find something to hold onto."
    return

label spooning_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. Her breathing is getting ragged as she nears her orgasm also."
    the_girl "[the_girl.mc_title], your cock is so good! Pin me to the [the_object.name] and make me cum!"
    "You speed up with her words of encouragement, passing the point of no return."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if the_girl.wants_creampie:
            the_girl "Oh god yes, cum with me [the_girl.mc_title]!"
        "You quickly shift you weight from being beside her to on top of her, pinning her to the [the_object.name], prone."
        if mc.condom:
            $ play_moan_sound()
            "You push your weight down on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans as you dump your load into her, barely contained by your condom."
            the_girl "Oh god!"
            $ climax_controller.do_clarity_release(the_girl)
            "You can feel her [the_girl.pubes_description] pussy quivering all around you as you cum in unison. Her body is milking your cum, with only a thin layer of latex keeping it from spilling deep inside her."
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock."
            "You pull out and sit back. The condom is ballooned and sagging with the weight of your seed."
            if the_girl.get_opinion_score("drinking cum") > 1 and the_girl.sluttiness > 50:
                $ the_girl.discover_opinion("drinking cum")
                "[the_girl.possessive_title] points to your crotch, but can't get out the words she wants to say."
                mc.name "You want my cum, slut?"
                "She nods. You take the condom off. Instead of handing it to her though, you put the end of it up to her lips and try to feed it to her."
                "It drops down her chin but she managed to drink some of it."
                $ the_girl.cum_in_mouth()
                $ the_girl.change_slut(the_girl.get_opinion_score("drinking cum"), 70)
            else:
                "You take off the condom, tie the end in a knot and throw it away."
            "You sigh contentedly and enjoy the post-orgasm feeling of relaxation. [the_girl.possessive_title] can barely move, still face down on the [the_object.name]."
        else:
            $ play_moan_sound()
            "You push your weight down on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans in time with each new shot of hot semen inside of her."
            the_girl "Oh fuck..."
            "You can feel her [the_girl.pubes_description] pussy quivering all around you as you cum in unison. Her body is milking your cum, you swear it feels like she's pulling it deep into her womb."
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ spooning_sex.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "You slowly pull out of [the_girl.possessive_title], then roll over next to her."

    elif the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
        else:
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass."
        $ the_girl.cum_on_ass()
        $ spooning_sex.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        "She reaches down between her legs and starts to play with herself, bringing herself to orgasm in unison with you."
        the_girl "Oh god I'm cumming!"
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.title] covered in your semen."
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid and goosebumps erupt all over her body as her brain registers your cum on her."
            "[the_girl.possessive_title] revels in bliss as she mindlessly rubs in your cum and licks of her fingers to heighten her orgasm."
            "She truly is addicted to your cum."
        elif the_girl.sluttiness > 90:
            the_girl "What a waste, you should have put that inside of me."
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh wow, there's so much of it..."

    $ post_double_orgasm(the_girl)
    return
