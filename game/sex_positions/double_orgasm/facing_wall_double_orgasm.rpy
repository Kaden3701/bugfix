init 5 python:
    facing_wall.double_orgasm = "facing_wall_double_orgasm"

label facing_wall_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s tight cunt draws you closer to your orgasm with each thrust. Her breathing is getting ragged as she nears her orgasm also."
    the_girl "[the_girl.mc_title], your cock is so good! Pin me to the wall and make me cum all over it!"
    "You speed up with her words of encouragement, passing the point of no return. You push her up against the [the_object.name] and lay into her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Fuck, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if the_girl.wants_creampie:
            the_girl "Oh god yes, cum with me [the_girl.mc_title]!"
        if mc.condom:
            "You push forward as you climax, thrusting your cock as deep inside of [the_girl.possessive_title] as you can manage."
            $ the_girl.have_orgasm()
            "She wraps her legs around you as she cums in unison."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "Once your climax has passed you keep [the_girl.title] pinned to the [the_object.name] for a little longer. When her aftershocks wind down, she slowly unwraps her legs."
            "You step back and pull out of [the_girl.possessive_title]. Your condom is ballooned out, filled with your seed."

            call post_orgasm_condom_routine(the_girl, facing_wall) from _call_post_orgasm_condom_routine_facing_wall_double_orgasm

        else:
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans in ecstasy as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                $ the_girl.have_orgasm()
                "Her body goes rigid as your cum pumps into her. Goosebumps erupt all over her body and her pupils dilate as her brain registers her creampie."
                "Having your cum inside of her heightens her orgasm as her fetish for your cum is fulfilled."
            else:
                "You push forward as you finally climax, thrusting your cock as deep inside of [the_girl.possessive_title] as you can manage."
                $ the_girl.have_orgasm()
                "She clings to you helplessly as she cums with you in unison."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ facing_wall.redraw_scene(the_girl)
            "You wait until your orgasm has passed, then step back and sigh happily. [the_girl.title] stays leaning against the [the_object.name] for a few seconds as your semen drips down her leg."

    elif the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as your blow your load all over her ass."
            "She holds still for you as you cover her with your sperm."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        "She reaches down and you see she is rapidly rubbing her clit as she begins to orgasm at the same time."
        if the_girl.get_opinion_score("being covered in cum") > 0:
                the_girl "Yes! Paint me with your sticky cum!"
        $ the_girl.have_orgasm()
        $ the_girl.cum_on_ass()
        $ facing_wall.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            $ play_moan_sound()
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly as her orgasm is enhanced by your bodyshot."
            "She truly is addicted to your cum."
        "After you finish, you watch as she slowly stops rubbing herself. Her body twitches once in a while from an aftershock."
        if the_girl.sluttiness > 90 or the_girl.get_opinion_score("being covered in cum") > 0:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."

    $ post_double_orgasm(the_girl)
    return
