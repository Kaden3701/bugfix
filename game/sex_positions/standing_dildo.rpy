init:
    python:
        standing_dildo = Position(name = "Dildo Fuck", slut_requirement = 40, slut_cap = 70, requires_hard = False, requires_large_tits = False,
            position_tag = "against_wall", requires_location = "Stand", requires_clothing = "Vagina", skill_tag = "Foreplay",
            girl_arousal = 15, girl_energy = 7,
            guy_arousal = 5, guy_energy = 20,
            connections = [],
            intro = "intro_standing_dildo",
            scenes = ["scene_standing_dildo_1","scene_standing_dildo_2"],
            outro = "outro_standing_dildo",
            transition_default = "transition_default_standing_dildo",
            strip_description = "strip_standing_dildo", strip_ask_description = "strip_ask_standing_dildo",
            orgasm_description = "orgasm_standing_dildo",
            taboo_break_description = "taboo_break_standing_dildo",
            verb = "dildo",
            opinion_tags = ["being fingered", "sex standing up"], record_class = "Insertions",
            default_animation = blowjob_bob,
            associated_taboo = "touching_vagina")
        # don't add to list of positions, you need to unlock it ;)
        #list_of_positions.append(standing_dildo)


label intro_standing_dildo(the_girl, the_location, the_object):
    "You pull [the_girl.title] close against you."

    if the_girl.event_triggers_dict.get("has_used_dildo", False):
        mc.name "I have brought your favorite toy."
        if the_girl.arousal_perc > 50:
            the_girl "Oh God yes, give it to me [the_girl.mc_title]!"
        else:
            the_girl "Oh really, show me what you got."
        $ standing_dildo.redraw_scene(the_girl)
        "While you get on your knees she spreads her legs while leaning onto the [the_object.name]."
        the_girl "Ok, slide that bad boy right in there!"
    else:
        mc.name "I have something I think you might enjoy."
        the_girl "Oh? What might that be?"
        "You pull the dildo out of your backpack. Her eyes fix on it and she realizes what you want to do."
        if the_girl.sluttiness > 40: #She is excited.
            the_girl "Oh! That looks like fun..."
        else:
            the_girl "Oh my god, it's so big! I don't know about this..."
            mc.name "Don't worry, I'll go slow."

        $ standing_dildo.redraw_scene(the_girl)
        "You get down on your knees in front of her. You bring the dildo up to her [the_girl.pubes_description] pussy, and she spreads her legs to give you easier access."
        the_girl "Ok. Ready when you are I guess!"
        "You bring the dildo up to her slit and begin to apply light pressure."
        if the_girl.arousal_perc > 50:
            "It slides into [the_girl.possessive_title]'s sopping cunt easily. Her excitement provides more than enough lube to push it deep."
        else:
            "It takes several seconds of gentle pressure to push it up inside of [the_girl.possessive_title]'s cunt. She takes a moment to adjust to the pressure."
        the_girl "You can start moving it."

        $ the_girl.event_triggers_dict["has_used_dildo"] = True
    return

label taboo_break_standing_dildo(the_girl, the_location, the_object):

    return

label scene_standing_dildo_1(the_girl, the_location, the_object):
    "You pump the dildo in and out of [the_girl.possessive_title]. On your knees in front of her, you look up and admire her shapely body and chest."
    if the_girl.has_large_tits:
        if the_girl.tits_available:
            "You reach your free hand up to [the_girl.title]'s bare [the_girl.tits_description] and cup one. Her skin is flushed and it feels hot in your hand."

        else:
            "You reach your free hand up to [the_girl.title]'s tits and squeeze one through her clothing, enjoying its size and weight."
    else:
        if the_girl.tits_available:
            "You paw at [the_girl.possessive_title]'s [the_girl.tits_description] with your free hand, running your thumb over one of her nipples."
            "Her body responds, the nipple hardening as you play with it."
        else:
            "You paw at [the_girl.possessive_title]'s [the_girl.tits_description] through her clothing with your free hand."
            "You can feel her body respond, her nipple hardening enough that you can feel it through the fabric."
    return


label scene_standing_dildo_2(the_girl, the_location, the_object):
    "You slide the dildo in and out of her pussy, stroking the inside of that soft tunnel."
    $ play_moan_sound()
    "Each movement draws moans of pleasure from [the_girl.possessive_title]. She runs a hand through your hair."
    if the_girl.arousal_perc > 75:
        "Her pussy is dripping wet now, her juices are running down the dildo and onto your hand.."
        menu:
            "Make her lick her juices off":
                if the_girl.event_triggers_dict.get("has_sucked_dildo", False):
                    "You pull the dildo out. She immediately starts to protest."
                    the_girl "Hey! What are you doing! I'm getting so close..."
                    "Her words stop when you shove your fingers from your free hand into her cunt. You raise the dildo up to her face."
                mc.name "Look at how wet you are! I want you to taste it."
                if the_girl.get_opinion_score("being submissive") >= 0:
                    "[the_girl.title] submissively opens her mouth. You push the dildo into her mouth, making her clean her own juices from it."
                    "As she strokes the dildo with her mouth, you reciprocate, pushing your fingers into her at the same time."
                    "Soon she is eagerly sucking the dildo, your fingers stroking her silky insides in turn."
                    $ the_girl.change_stats(arousal = the_girl.get_opinion_score("being submissive"), obedience = 1)
                    "Suddenly, you pull the dildo out of her mouth. You bring it back down to her cunt and push it back inside her."
                    $ the_girl.event_triggers_dict["has_sucked_dildo"] = True
                else:
                    the_girl "Fuck that. Why don't you do it?"
                    "She doesn't seem particularly interested in tasting herself, so you back off."
                    "You bring the dildo back down to her cunt and push it inside her."
            "Finish her off":
                "You can tell she is getting close, so you double down on your efforts to get [the_girl.title] off."
                "With one hand you piston the dildo in and out of her, and with the other you flick your thumb over her clit."
                the_girl "Oh god, that feels so good..."
                $the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
    else:

        "She places one of her own hands over yours, encouraging you to speed up."
        the_girl "Just like that... Ah..."

    return

label outro_standing_dildo(the_girl, the_location, the_object):
    "The view of [the_girl.title]'s hot, tight pussy squeezing your dildo is enough to push you that little bit further, past the point of no return."
    "You grasp her tightly with your free hand as you cum, shoving your dildo deep into her cunt and making her gasp in surprise."
    "When you've recovered you slide it out."
    $ ClimaxController.manual_clarity_release(climax_type = "air")
    the_girl "Did you just... Cum?"
    mc.name "Yeah."
    "She gives a slight smile."
    the_girl "Wow, I didn't realize you were enjoying this as much as I was."
    return


label transition_standing_finger_standing_dildo(the_girl, the_location, the_object):
    "You pull your fingers out of [the_girl.title] and turn her to face you."
    call intro_standing_dildo(the_girl, the_location, the_object) from _call_transition_standing_finger_standing_dildo
    return

label transition_default_standing_dildo(the_girl, the_location, the_object):
    call intro_standing_dildo(the_girl, the_location, the_object) from _call_transition_default_standing_dildo
    return

label strip_standing_dildo(the_girl, the_clothing, the_location, the_object):
    the_girl "That thing feels amazing, oh my god..."
    $ the_girl.draw_animated_removal(the_clothing, position = standing_dildo.position_tag)
    "She strips off her [the_clothing.name] while you fuck her with the dildo, moaning the whole time."
    return

label strip_ask_standing_dildo(the_girl, the_clothing, the_location, the_object):
    the_girl "Everything feels so tight, I need to get this off! Do you mind?"
    "[the_girl.possessive_title] grabs onto her [the_clothing.name], waiting for you to tell her what to do."
    menu:
        "Let her strip":
            mc.name "Take it off. Strip for me."
            $ the_girl.draw_animated_removal(the_clothing, position = standing_dildo.position_tag)
            "[the_girl.possessive_title] takes off her [the_clothing.name] and drops it to the side while you pump the dildo in and out of her cunt."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
            else:
                the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
            return False

label orgasm_standing_dildo(the_girl, the_location, the_object):
    the_girl "Oh god... Right there! Right there! Ahhhhh!"
    "Her whole body tenses up and she grabs you by the hair. A shiver runs through her body as she climaxes."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    the_girl "Ah... Keep going... I bet that thing will make me cum again."
    return
