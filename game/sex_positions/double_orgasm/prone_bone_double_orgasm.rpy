init 5 python:
    prone_bone.double_orgasm = "prone_bone_double_orgasm"

label prone_bone_double_orgasm(the_girl, the_location, the_object):
    $ play_spank_sound()
    "You smack [the_girl.title]'s ass and moan, in the final stretch before your orgasm."
    the_girl "[the_girl.mc_title]... [the_girl.mc_title]... I'm gonna cum!"
    "She weakly manages to call out your name as she gets ready to cum."
    mc.name "I'm cumming too!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if mc.condom:
            $ play_moan_sound()
            "You push your weight down on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans as you dump your load into her, barely contained by your condom."
            $ the_girl.have_orgasm()
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
            $ the_girl.have_orgasm()
            the_girl "Oh fuck..."
            "You can feel her [the_girl.pubes_description] pussy quivering all around you as you cum in unison. Her body is milking your cum, you swear it feels like she's pulling it deep into her womb."
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ prone_bone.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            "You slowly pull out of [the_girl.possessive_title], then roll over next to her."

    elif the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
        else:
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass."
        $ the_girl.cum_on_ass()
        $ prone_bone.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        "She reaches down between her legs and starts to play with herself, bringing herself to orgasm in unison with you."
        $ the_girl.have_orgasm()
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
