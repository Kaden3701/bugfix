init 0 python:
    strip_lap_dance = StripteasePosition(name = "Lap Dancing",
        slut_requirement = 30,
        is_close = True,
        allows_touching = True, allows_jerking = False, allows_turning = True,
        position_towards_pose = "cowgirl", position_away_pose = "sitting",
        girl_energy_cost = 6, guy_arousal_gain = 6,
        girl_arousal_gain = 2,
        intro_label = "strip_lap_dance_intro",
        transition_label = "strip_lap_dance_transition",
        turn_towards_label = "strip_lap_dance_turn_towards",
        turn_away_label = "strip_lap_dance_turn_away",
        towards_labels = ["strip_lap_dance_towards_1", "strip_lap_dance_towards_2"],
        away_labels = ["strip_lap_dance_away_1"],
        climax_label = "strip_lap_dance_climax")

    list_of_strip_positions.append(strip_lap_dance)

init 1 python:
    close_strip_dancing.leads_to.append([strip_lap_dance, "Pull her on your lap"])

label strip_lap_dance_intro(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title] stands right in front of you, slowing moving closer."
    "She places her legs besides your hips and starts moving back and forth sensually, keeping time to imagined music."
    if guy_state == "touching":
        "You reach out and place your hands on her tits, squeezing her [the_person.tits_description] as she moves."
    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_transition(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title] dances her way closer to you, positioning herself right above your crotch."
    if guy_state == "touching":
        "You immediately put your hands on her ass."
    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_turn_towards(the_person, guy_state, for_pay = False):
    "[the_person.title] turns around to face you, making sure her ass keeps bouncing on your lap."
    if guy_state == "touching":
        if the_person.tits_available:
            if the_person.has_large_tits:
                "You reach up her torso and fondle her tits as she presents them. Their soft, warm weight feels satisfying in your hands."
            else:
                "You reach up her torso and fondle her chest as she presents it to you."
        else:
            "You reach up her torso and grope at her tits underneath her [the_person.outfit.get_upper_top_layer.display_name]."
    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_turn_away(the_person, guy_state, for_pay = False):
    "[the_person.title] spins herself around and sits right back on your crotch."
    if the_person.vagina_visible:
        "She wiggles her hips, as you feel the wetness of her vagina on you."
    else:
        "She shakes her hips, rubbing her [the_person.outfit.get_lower_top_layer.display_name] on the bulge in your pants."

    if guy_state == "touching":
        if the_person.vagina_available:
            "You feel the shapely curves of her ass and hips, caressing her as she dances."
        else:
            "You feel the shapely curves of her ass and hips underneath her [the_person.outfit.get_lower_top_layer.display_name]."

    elif guy_state == "jerking":
        pass #No special dialogue
    return

label strip_lap_dance_towards_1(the_person, guy_state, for_pay = False):
    if the_person.tits_visible:
        "[the_person.title] presses her [the_person.tits_description] in your face while she wiggles rhythmically over your body."
    else:
        "[the_person.title] moves her body over you body while looking you deeply in the eyes."

    if guy_state == "touching":
        if the_person.vagina_visible:
            "You grab her ass moving along with her motions."
        else:
            "You grab her ass through her [the_person.outfit.get_lower_top_layer.display_name] moving along with her motions."
    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_towards_2(the_person, guy_state, for_pay = False):
    if the_person.has_large_tits:
        "[the_person.possessive_title] cups her tits and squeezes your face between them."
    else:
        "[the_person.possessive_title] slowly pushes a nipple between your lips."

    if guy_state == "touching":
        "You feel up her hips while she slowly keeps grinding on you."
    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_away_1(the_person, guy_state, for_pay = False):
    "[the_person.title] pushes her butt into your lap, slowly moving to either side."
    if the_person.vagina_visible:
        "You can feel the dampness between her legs."
    else:
        "You wonder how it would feel without her [the_person.outfit.get_lower_top_layer.display_name] in the way."

    if guy_state == "touching":
        if the_person.tits_available:
            if the_person.has_large_tits:
                "You grab around her frame to hold her tits and juggle them in your hands."
            else:
                "You grab around her chest to fondle her tits."
        else:
            "You feel up her chest, grabbing at her [the_person.tits_description] through her [the_person.outfit.get_lower_top_layer.display_name]."

    elif guy_state == "jerking":
        pass
    return

label strip_lap_dance_climax(the_person, guy_state, for_pay = False):
    "[the_person.possessive_title] is breathing heavily and presses herself harder into your lap."
    the_person "Oh my... Ah...!"
    if guy_state == "touching":
        "She screams and presses her self up to your body, climaxing from the sensation of riding on your cock while you squeeze her tits."
    elif guy_state == "jerking":
        pass
    else:
        "She screams and presses her self up to your body, riding herself to a much needed orgasm."
    $ the_person.have_orgasm(trance_chance_modifier = the_person.get_opinion_score(["public sex", "masturbating"]))
    "You feel a shiver run through her body where she lets herself fall onto your chest."
    "After a while she takes a few deep breaths and slowly starts moving her hips again."
    return
