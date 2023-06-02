init 5 python:
    breeding_missionary.double_orgasm = "breeding_missionary_double_orgasm"

label breeding_missionary_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is scratching her fingernails down your back. She is moaning with every thrust."
    the_girl "It's so good... I'm gonna cum!"
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "Me too!"
    if the_girl.knows_pregnant:
        the_girl "Cum deep! I want you to soak my unborn baby with your cum!"
    else:
        the_girl "Do it! I want you to cum with me! Cum deep and knock me up!"
    "[the_girl.possessive_title] wraps her legs around your waist. Even if you wanted to pull out, you couldn't, as she uses her legs to pull you into her."
    "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax. She gasps and claws at your back as you pump your seed into her."
    $ the_girl.call_dialogue("cum_vagina")
    $ the_girl.cum_in_vagina()
    $ breeding_missionary.redraw_scene(the_girl)
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
    if the_girl.has_breeding_fetish:
        $ play_moan_sound()
        "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
        if the_girl.knows_pregnant:
            the_girl "Yes! Paint my pregnant womb white with your cum!"
        else:
            the_girl "Yes! Paint my fertile womb white with your cum!"
        $ the_girl.have_orgasm()
        "Her body convulses as she begins to cum at the same time. She clings to you as her orgasm hits."
        if the_girl.knows_pregnant:
            "[the_girl.title] revels having her breeding fetish fulfilled as you pump her already pregnant body full of cum."
        else:
            "[the_girl.title] revels having her breeding fetish fulfilled as you pump her full of a risky creampie."
    elif the_girl.has_cum_fetish:
        $ play_moan_sound()
        "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
        the_girl "Oh fuck oh yes!!!"
        $ the_girl.have_orgasm()
        "Her body convulses as she begins to cum at the same time. She wraps her legs around you and clings to you as orgasm hits her as you cum inside of her."
        "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
    else:
        $ play_moan_sound()
        "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
        $ the_girl.have_orgasm()
        "Her body convulses as she begins to cum at the same time. She clings to you as her orgasm hits."
    "When you finish, you wait a few minutes while [the_girl.title] has a few aftershocks. Her pussy grasps your cock with each one."
    "You roll off of [the_girl.possessive_title] and lie beside her."
    "She lifts her legs up a bit, tilting her vagina so that your cum will naturally slide deeper inside. She sighs happily."
    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
