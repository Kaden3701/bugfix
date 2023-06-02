init 5 python:
    piledriver_anal.double_orgasm = "piledriver_anal_double_orgasm"

label piledriver_anal_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is moaning with every thrust into her tight little asshole."
    the_girl "It's so good... I'm gonna cum!"
    "Pinning [the_girl.title] down to the [the_object.name] as you fuck her puckered hole is really turning you on. You feel yourself approaching the point of no return."
    mc.name "Me too!"
    the_girl "Do it! I want you to cum with me!"

    $ climax_controller = ClimaxController(["Cum inside of her","anal"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        $ play_moan_sound()
        "You push yourself balls deep into [the_girl.title]'s ass and dump your load. Her moans grow desperate as she cums with you in unison."
        $ climax_controller.do_clarity_release(the_girl)
        $ the_girl.have_orgasm()
        if the_girl.get_opinion_score("anal creampies") > 0:
            the_girl "Oh god yes fill me up! Fill up my poor little ass with your cum!"
        else:
            the_girl "Oh god I can't believe it, I'm cumming!"
        "You hold yourself inside of her until your climax has passed. You start to pull out but [the_girl.title] begs you to wait."
        the_girl "Wait! Oh god leave it just a little longer..."
        "You can feel her tight back passage quivering around you as she has little aftershocks from her orgasm. When they stop, you slowly pull out."
        if mc.condom:
            "Your condom is filled and bulging on one side. [the_girl.title] is too worn out to do anything with it."
            "You tie the end in a knot and pull it off, throwing it away while she recovers."
        else:
            "She is left on her back, holding her own ankles up by her head, trying to catch her breath, as your cum drips out of her gaping asshole."
            $ the_girl.cum_in_ass()
            $ piledriver_anal.redraw_scene(the_girl)
            if the_girl.get_opinion_score("anal creampies") > 0:
                # If she's into both...
                $ the_girl.discover_opinion("anal creampies")
                the_girl "Oh fuck... I'm so full of cum. I don't want to move..."
            else:
                the_girl "Wow, that was intense. I hope you didn't stretch me out too badly."
            "Her puckered hole is raw and gaping. You watch as her asshole slowly starts to close, sealing your load inside of it."
            "She slowly lowers her legs until she is laying flat on the [the_object.name]."

    elif the_choice == "Cum on her face":
        $ the_girl.cum_on_face()
        $ missionary.redraw_scene(the_girl)
        $ climax_controller.do_clarity_release(the_girl)
        if mc.condom:
            "You pull out at the last moment and grab your cock. You whip off your condom and stroke yourself off, blowing your load over [the_girl.title]'s face."
        else:
            "You pull out at the last moment and grab your cock. You kneel and stroke yourself off, blowing your load over [the_girl.title]'s face."
        "[the_girl.title] reaches down and starts rubbing circles around her clit as you start to blow your load. She is cumming at the same time."
        $ the_girl.have_orgasm()
        the_girl "Ohhhh yes! Shower me with your hot cum!"
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum splashes onto her skin. Goosebumps erupt all over her body as her brain registers your cum on her."
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her. Your cum on her skin heightens her orgasm."
            "She truly is addicted to your cum."
        else:
            the_girl "Ah... Good job... Ah..."
            "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."

    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
