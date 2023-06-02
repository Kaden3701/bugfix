init 5 python:
    sixty_nine.double_orgasm = "sixty_nine_double_orgasm"

label sixty_nine_double_orgasm(the_girl, the_location, the_object):
    #$ sixty_nine.current_modifier = "sixty_nine"
    "Licking and probing all around [the_girl.possessive_title]'s clit, you can feel her start to quiver."
    "She is getting close to cumming, and the excitement of getting her off is bringing you to the edge too."
    $ play_moan_sound()
    the_girl "Mmmm... MMMMMMmmmmm..."
    "The vibrations and moans coming from her mouth around your cock are driving you over the edge. You smack her ass and pause licking her for a second."
    mc.name "Ah, I'm going to cum too!"
    if the_girl.facial_or_swallow() == "facial":
        "[the_girl.possessive_title] pulls you out of her mouth, and begins stroking you eagerly."
        the_girl "That's it, [the_girl.mc_title], cum with me! OH YES!!!"
        $ the_girl.cum_on_face()
        $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_girl)
        $ the_girl.have_orgasm()
        if the_girl.has_cum_fetish:
            "[the_girl.possessive_title] begins moaning uncontrollably as she receives the cum her addiction has been craving."
        else:
            "[the_girl.possessive_title] is cumming with you, moaning loudly as you blow your load all over her face."
        $ sixty_nine.redraw_scene(the_girl)
        "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She is panting for breath as you finish"
        $ the_girl.call_dialogue("cum_face")
    else:
        if the_girl.has_cum_fetish:
            the_girl "Mmmmm... YESSSHHHHHH!"
            "[the_girl.possessive_title] pulls off until just the tip of your cock is in her mouth and she strokes you off eagerly."
            "Her body is quivering as she cums, but her focus remains on your cock as it gets ready to burst."
            "You erupt in orgasm into her greedy mouth. Her expert mouth milks you with every spurt."
            $ the_girl.cum_in_mouth()
            $ the_girl.have_orgasm()
            $ sixty_nine.redraw_scene(the_girl)
            "[the_girl.possessive_title] begins moaning uncontrollably around your twitching cock when her cum addicted brain registers her cum dosage and her orgasm."
        elif the_girl.sex_skills["Oral"] > 5:
            "You feel [the_girl.possessive_title] take you all the way in her mouth as you start to orgasm."
            $ the_girl.have_orgasm()
            "You grunt and twitch as you start to empty your balls right into her stomach. She is moaning with every wave of her own orgasm as she cums with you."
            $ play_gag_sound()
            "She tightens and relaxes her throat, swallowing your erection over and over as it spurts every last drop of cum straight down her throat."
            $ the_girl.cum_in_mouth()
            $ sixty_nine.redraw_scene(the_girl)
            $ play_swallow_sound()
            "When you're completely finished she pulls off slowly, panting and catching her breath."
        else:
            "You feel [the_girl.possessive_title] leave just the tip of you in her mouth. She strokes you with her hand as you start to orgasm."
            $ play_moan_sound()
            "She moans as you fill up her mouth with your sperm."
            $ the_girl.have_orgasm()
            "Her body is twitching as she orgasms with you in unison."
            $ the_girl.cum_in_mouth()
            $ sixty_nine.redraw_scene(the_girl)
            $ play_swallow_sound()
            "When you're completely finished, you can feel her swallow the contents of her mouth, before slowly pulling off, panting as she catches her breath."
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
        $ the_girl.call_dialogue("cum_mouth")
        "You give [the_girl.possessive_title]'s slit a few more appreciative licks."

    $ post_double_orgasm(the_girl)
    return
