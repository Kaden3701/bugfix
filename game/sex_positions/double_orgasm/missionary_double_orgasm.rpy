init 5 python:
    missionary.double_orgasm = "missionary_double_orgasm"

label missionary_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title] is scratching her fingernails down your back. She is moaning with every thrust."
    the_girl "It's so good... I'm gonna cum!"
    "You get to hear every little gasp and moan from [the_girl.title] as you're pressed up against her. Combined with the feeling of fucking her pussy it's not long before you're pushed past the point of no return."
    mc.name "Me too!"
    $ the_girl.call_dialogue("cum_pullout")
    if the_girl.wants_creampie:
        the_girl "Do it! I want you to cum with me!"

    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum outside", "body"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        "You use your full weight to push your cock deep inside of [the_girl.possessive_title]'s cunt as you climax"
        $ the_girl.have_orgasm()
        "She is moaning loudly as she cums together with you at the same time."
        if mc.condom:
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "When you finish, you leave yourself deep inside her for a few moments while she has a few aftershocks."
            "You roll off of [the_girl.possessive_title] and lie beside her."
            "Your condom is ballooned with your seed, hanging off your cock to one side."

            call post_orgasm_condom_routine(the_girl, missionary) from _call_post_orgasm_condom_routine_missionary_double_orgasm

        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ missionary.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish:
                $ play_moan_sound()
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                the_girl "Oh fuck oh yes!!!"
                "Her body convulses as she begins to cum at the same time. She wraps her legs around you and clings to you as orgasm hits her as you cum inside of her."
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            "When you finish, you wait a few minutes while [the_girl.title] has a few aftershocks. Her pussy grasps your cock with each one."
            "You roll off of [the_girl.possessive_title] and lie beside her."

    elif the_choice == "Cum outside":
        if mc.condom == False and (the_girl.has_cum_fetish or the_girl.wants_creampie):
            "Before you get the chance to pull back and out, [the_girl.title] lifts both her feet up and wraps her legs around you, locking her ankles together."
            $ wordchoice = renpy.random.choice(["Oh God,", "Oh yes", "Oh... OH! Yes "])
            $ wordchoice2 = renpy.random.choice(["Cum for me!", "Cum inside!", "Cum for me!", "Cum in me!", "Pump it deep!", ""])
            if the_girl.love < 0:
                the_girl "Where do think you're going, [the_girl.mc_title]?"
            else:
                the_girl "[wordchoice], [the_girl.mc_title]! [wordchoice2]"
            the_girl "I'm cumming... you can't pull out now!"
            "The strength of her legs prevents you from pulling out."
            $ ran_num = renpy.random.randint(0,1)
            if ran_num == 0:
                mc.name "What the fuck!"
            if the_girl.sex_skills["Vaginal"] > 3:
                "[the_girl.possessive_title] pulls your body close to hers, burying your cock as deep as she can. She orgasms with you in unison, her cunt milks you with the muscles inside her."
                "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            else:
                "She humps against you a few times to make sure that you cum deep inside her. She orgasms with you in unison, her cunt milks you with the muscles inside her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ the_girl.have_orgasm()
            $ missionary.redraw_scene(the_girl)
            $ climax_controller.do_clarity_release(the_girl)
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy."
                $ play_moan_sound()
                the_girl "Oh fuck oh yes!!!"
                "Her body convulses as she begins to cum at the same time. She wraps her legs around you and clings to you as orgasm hits her as you cum inside of her."
                "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            "When you finish, [the_girl.title] leaves her legs wrapped around you as she has a couple aftershocks. Her pussy twitches with each one."
            "She slowly opens her eyes and looks up at you."
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
                    the_girl "I'm sorry... I don't know what came over me... I just couldn't let you pull out!"
                else:
                    the_girl "I hope you enjoy paying child support, [the_girl.mc_title]."
            "You roll off of [the_girl.possessive_title] and lie beside her."

            $ del wordchoice
            $ del wordchoice2
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
            "[the_girl.title] reaches down and starts rubbing circles around her clit as you start to blow your load. She is cumming at the same time."
            the_girl "Ohhhh yes! Shower me with your hot cum!"
            $ the_girl.have_orgasm()
            if the_girl.has_cum_fetish:
                "[the_girl.possessive_title]'s body goes rigid as your cum splashes onto her skin. Goosebumps erupt all over her body as her brain registers your cum on her."
                "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her. Your cum on her skin heightens her orgasm."
                "She truly is addicted to your cum."
            else:
                the_girl "Ah... Good job... Ah..."
                "You sit back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s body covered in your semen."

    $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
