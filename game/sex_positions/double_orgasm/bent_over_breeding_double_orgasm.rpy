init 5 python:
    bent_over_breeding.double_orgasm = "bent_over_breeding_double_orgasm"

label bent_over_breeding_double_orgasm(the_girl, the_location, the_object):
    "[the_girl.title]'s back is arched and she is moaning non stop. Her ass quakes with every rapid thrust."
    the_girl "Oh god it's so good! Oh [the_girl.mc_title] I'm gonna cum!"
    "Hearing her call out your name is pushing you over the edge. You are about to cum too."
    mc.name "I'm cumming too!"
    $ the_girl.call_dialogue("cum_pullout")
    "[the_girl.possessive_title]'s drenched cunt is just too good. You decide to cum inside it."
    if mc.condom:
        $ play_moan_sound()
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans when she feels you filling the condom deep inside of her."
        $ the_girl.have_orgasm()
        "Her cunt quivers as she joins you in orgasm. Her body goes rigid but you can feel the delicious pulsing as it feels like her body is trying to suck the condom off."
        the_girl "Oh god, I can feel you twitching... but something is missing?"
        "You wait until both of your orgasms have passed completely, then pull out and sit back. Your condom is bulged on the end where it is filled with your seed."
        "She looks at your condom and frowns."
        the_girl "You were... seriously? You had a condom on? Why would you do that?"
        $ the_girl.change_happiness(-5)
        "You sigh contentedly and enjoy the post-orgasm feeling of relaxation."
    else:
        $ play_moan_sound()
        "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She moans in time with each new shot of hot semen inside of her."
        "You feel her pussy convulsing around your dick as she also starts to orgasm."

        if the_girl.wants_creampie:
            the_girl  "Yes! Fill me with your cum!"
        $ the_girl.have_orgasm()
        $ the_girl.cum_in_vagina()
        $ bent_over_breeding.redraw_scene(the_girl)
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        if the_girl.has_breeding_fetish:
            "[the_girl.possessive_title] pushes herself back tightly against you, forcing your cum as deep as she can."
            the_girl "Yes! Yes I needed this so bad! Fill me up! Oh god it's so good..."
            "[the_girl.possessive_title] revels in having her breeding fetish fulfilled."
        elif the_girl.has_cum_fetish:
            "[the_girl.possessive_title]'s body goes rigid as your cum pours into her [the_girl.pubes_description] pussy. Goosebumps erupt all over her body as her brain registers her creampie."
            the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I was made to take your cum inside me!"
            "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
        if the_girl.get_opinion_score("bareback sex") > 0:
            the_girl "Oh god... I can feel it so deep. I mean... it could... hopefully..."
            "[the_girl.possessive_title]'s voice starts to trail off."
        elif the_girl.wants_creampie:
            the_girl "Oh god it's so deep."
        elif the_girl.knows_pregnant:
            the_girl "Its nice, already being pregnant, I can take a load like that anytime..."
        elif the_girl.on_birth_control:
            the_girl "Oh fuck...  Good thing I'm on the pill..."
        else:
            the_girl "Oh fuck... I could get pregnant you know.."

        "When you finish, you wait for a bit, reveling in the sensations as [the_girl.title]'s slick cunt has aftershocks."
        "You wait until her orgasm has passed completely, then pull out and stand back."
        if the_girl.has_breeding_fetish:
            "As your cum starts to leak out, [the_girl.possessive_title] reaches back and tries to keep it inside with her hand."
        else:
            "Your cum leaks out of her dripping wet [the_girl.pubes_description] pussy."
        $ post_double_orgasm(the_girl) #We have to put this at the end of each double orgasm scene because return doesn't return to where you think it will.
    return
