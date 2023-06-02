init 5 python:
    anal_standing.double_orgasm = "anal_standing_double_orgasm"

label anal_standing_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is moaning with every thrust into her tight little asshole."
    the_girl "It's so good... I'm gonna cum!"
    mc.name "Me too!"
    the_girl "Do it! I want you to cum with me!"

    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her ass", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if mc.condom:
            $ play_moan_sound()
            "You push yourself balls deep into [the_girl.title]'s ass and dump your load. Her moans grow desperate as she cums with you in unison."
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.get_opinion_score("anal creampies") > 0:
                the_girl "Oh god yes cum for me! Shoot your load while you fuck my little ass!"
            else:
                the_girl "Oh god I can't believe it, I'm cumming!"
            $ the_girl.have_orgasm()
            "You can feel her ass pulsating all around you as you cum in unison. Her bowels are milking your cum, with only a thin layer of latex keeping it from spilling deep inside her."
            "After you finish, you leave your cock deep inside her, enjoying her hole quivering with each aftershock."
            "You pull out and sit back. The condom is ballooned and sagging with the weight of your seed."

            call post_orgasm_condom_routine(the_girl, anal_standing) from _call_post_orgasm_condom_routine_anal_standing_double_orgasm
        else:
            $ play_moan_sound()
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans in time with each new shot of hot semen inside of her."
            if the_girl.get_opinion_score("anal creampies") > 0:
                the_girl "Oh god yes fill me up! Fill up my poor little ass with your cum!"
            else:
                the_girl "Oh god cum with me!"
            $ the_girl.cum_in_ass()
            $ anal_standing.redraw_scene(the_girl)
            $ the_girl.have_orgasm()
            "You can feel her bowels quivering all around you as you cum in unison. Her body is milking your cum, you swear it feels like she's sucking your cock with her intestines."
            "After you finish, you leave your cock deep inside her, enjoying her hole pulsating with each aftershock."
            $ climax_controller.do_clarity_release(the_girl)
            "You slowly pull out of [the_girl.possessive_title] asshole, then roll over next to her."
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title] reaches back and starts fingering her ass, occasionally putting her fingers in her mouth to taste you cum."
                the_girl "Hmmm, just delicious!"

    elif the_choice == "Cum on her ass":
        if mc.condom:
            "You pull out of [the_girl.title] at the last moment. You whip your condom off and stroke your cock as you blow your load over her ass."
        else:
            "You pull out of [the_girl.title] at the last moment, stroking your shaft as you blow your load over her ass."
        $ the_girl.cum_on_ass()
        $ anal_standing.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        "She reaches down between her legs and starts to play with herself, bringing herself to orgasm in unison with you."
        $ the_girl.have_orgasm()
        the_girl "Oh god I'm cumming!"
        "You sit back and sigh contentedly, enjoying the sight of [the_girl.title] covered in your semen."
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid and goosebumps erupt all over her body as her brain registers your cum on her."
            "[the_girl.possessive_title] mindlessly scoops your cum out of her puckered hole and licks of her fingers to heighten her orgasm."
            "She truly is addicted to your cum."
        elif the_girl.sluttiness > 90:
            the_girl "What a waste, you should have put that inside of me."
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh wow, there's so much of it..."

    $ post_double_orgasm(the_girl)
    return
