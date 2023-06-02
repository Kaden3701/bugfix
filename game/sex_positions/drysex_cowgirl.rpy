#Foreplay position where girl grinds MC on top of him. Designed specifically for girl in charge sex scenes

init:
    python:
        drysex_cowgirl = Position(name = "Dry Cowgirl", slut_requirement = 20, slut_cap = 40, requires_hard = False, requires_large_tits = False,
            position_tag = "cowgirl", requires_location = "Lay", requires_clothing = "None", skill_tag = "Foreplay",
            girl_arousal = 12, girl_energy = 9,
            guy_arousal = 10, guy_energy = 11,
            connections = [],
            intro = "intro_drysex_cowgirl",
            scenes = ["scene_drysex_cowgirl_1","scene_drysex_cowgirl_2"],
            outro = "outro_drysex_cowgirl",
            transition_default = "transition_default_drysex_cowgirl",
            strip_description = "strip_drysex_cowgirl", strip_ask_description = "strip_ask_drysex_cowgirl",
            orgasm_description = "orgasm_drysex_cowgirl",
            taboo_break_description = "taboo_break_drysex_cowgirl",
            verb = "be ridden by", verbing = "being ridden by",
            opinion_tags = ["taking control", "get mc off", "get off", "waste cum"],
            default_animation = blowjob_bob,
            associated_taboo = "touching_body")

        list_of_girl_positions.append(drysex_cowgirl)

        drysex_cowgirl.girl_outro = "GIC_outro_drysex_cowgirl"

#init 1:
#    python:
#        ##Here is where you would put connections if they existed.

label intro_drysex_cowgirl(the_girl, the_location, the_object):
    the_girl "Lie down for me, I want to feel you against me."
    $ drysex_cowgirl.redraw_scene(the_girl)
    "You lie down on the [the_object.name]. [the_girl.title] swings a leg over your body and straddles you."
    if the_girl.vagina_available:
        "She leans back and grinds herself against you. She rubs her pussy along your cock, your pants the only thing separating the two."
    else:
        "She leans back and grinds herself against you. It feels good, even with your clothes on."
    the_girl "Ah..."
    if mc.recently_orgasmed:
        "[the_person.possessive_title]'s body rubbing against yours feels great. You feel yourself getting hard in response."
        $ mc.recently_orgasmed = False
    the_girl "Your body feels so good..."
    $ play_moan_sound()
    "She closes her eyes and moans, rubbing her crotch against yours."
    return

label taboo_break_drysex_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title] leads you to the [the_object.name]."
    the_girl "Lie down for me [the_girl.mc_title]..."
    $ drysex_cowgirl.redraw_scene(the_girl)
    "You nod and follow her instructions. She steps over you and kneels down, straddling your hips."
    if the_girl.effective_sluttiness(drysex_cowgirl.associated_taboo) > drysex_cowgirl.slut_cap:
        "She reaches between her legs and grabs your cock, bringing it towards her and running the tip against her clit."
        "You feel her thighs tremble with pleasure."
    else:
        "She reaches between her legs and grabs your cock, rubbing it against her stomach and stroking it gently."
    the_girl "To feel your body against mine... I've been wanting this."
    $ play_moan_sound()
    "She closes her eyes and moans, rubbing her crotch against yours."
    return

label scene_drysex_cowgirl_1(the_girl, the_location, the_object):
    # Scene 1. Grab her hips or grab her neck. Bonus to neck if hate fuck
    "[the_girl.possessive_title] is slowly working her hips against yours. It feels great, but you wish she would speed up a little."
    menu:
        "Grab her hips":
            "You put your hands on her hips. You push and pull her against you, trying to speed up the pace a little."
            if the_girl.get_opinion_score("being submissive") > 0:
                "[the_girl.title] follows your lead and starts to speed up a bit. You tighten your grip on her hips."
                mc.name "That's it."
                "The increase in pace feels great for both of you."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                $ mc.change_arousal(5)
            else:
                "She senses what you are doing and intentionally slows down."
                the_girl "Easy there [the_girl.mc_title]. I'm in charge right now, you just let me set the pace."
                "You stop urging her to go faster, but keep your hands on her hips. The slow pace is torture but feels good."
        "Grab her neck":
            "You reach up with your hand and go around the side of her neck. You try to start moving your hips a little faster against her."
            if the_girl.get_sex_goal() == "hate fuck":
                "At first, she tries to resist you, so you begin to squeeze her neck."
                the_girl "Hey now, I'm in..."
                "You tighten your hand, silencing her words. You growl back at her."
                mc.name "You're boring me to death here bitch. Let's pick up the pace a little."
                "She stares daggers at you, but does what you say and speeds up to meet your pace."
                "She runs her hands down your chest. As she passes your nipples, you feel her fingertips transition to fingernails and she starts to scratch you."
                "The pain enhances the pleasure, causing you to buck your hips for a moment. You loosen your grip on her neck for a moment eliciting a gasp and then a moan."
                $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                $ mc.change_arousal(5)
                $ the_girl.change_love(-1)
            else:
                "She speeds up a little, but still not as much as you would like, so you begin to squeeze her neck."
                if the_girl.get_opinion_score("being submissive") > 0:
                    $ play_moan_sound()
                    "[the_girl.title] moans for a second, but is soon silenced as you squeeze her neck. She starts to move her hips much faster now in response."
                    "Her mouth is hanging open and her eyes a closed tight as she submissively dry humps you."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                else:
                    "[the_girl.title] starts to protest, but is soon silenced as you squeeze her neck. She stops dry humping you and reaches up, trying to pull your hand away."
                    "You release her neck and she begins to gasp."
                    the_girl "Fuck, take it easy, okay? No need to do that!"
                    $ the_girl.change_love(-1)
                "Her body so close to yours is torture. It feels good, but your pants are insufferably tight..."

    return

label scene_drysex_cowgirl_2(the_girl, the_location, the_object):
    #Scene 2. If she is exposed, rub her clit. If not, grab her tits.
    if the_girl.vagina_available:
        "[the_girl.possessive_title] continues to ride you, with just that thin cloth of your pants in the way between your cock and her steamy cunt."
        "You reach down and start to rub along her clit."
        if the_girl.get_opinion_score("being fingered") < 0:
            $ play_moan_sound()
            "She moans as you touch her, but doesn't really seem to pick up the pace."
        else:
            the_girl "Oh! Mmm..."
            $ play_moan_sound()
            "She moans as your fingers circle her clit. Her body responds, bucking her hips harder against you."
            "The pressure of her body against yours feels good."
            $ the_girl.change_arousal(5)
            $ mc.change_arousal(3)
    else:
        if the_girl.tits_available:
            "[the_girl.possessive_title] continues to ride you. Her tits heaving up and down above you present an irresistible target."
            "You reach up with both hands and begin to fondle them."
            if the_girl.get_sex_goal() == "waste cum" or the_girl.get_sex_goal() == "hate fuck":
                $ play_moan_sound()
                "You grab her tits roughly. She moans as you play with them."
                the_person "You like my tits [the_girl.mc_title]? I bet you're going to cum in your pants just touching them."
                "You pinch her nipples roughly in response. She gasps in a mix a pleasure and pain."
                $ the_girl.change_arousal(5)
            else:
                "Her skin is hot and soft to the touch. They jiggle pleasantly in your hands as she grinds you."
                the_person "Mmm, they're really sensitive..."
                "She sighs happily as you play with her tits."
                $ the_girl.change_arousal(3)
        else:
            "[the_girl.possessive_title] continues to ride you. Her tits jiggle enticingly, even through her clothing."
            "You reach up with both hands and begin to fondle them."
            the_girl "Mmm, your hands feel great."

    return


label outro_drysex_cowgirl(the_girl, the_location, the_object, the_goal = None):
    "With each stroke of her hips [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
    mc.name "Fuck, I'm going to cum!"

    "She acts surprised, but quickly speeds up, dry humping you at a rapid pace."
    mc.name "Oh... Fuck!"
    $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
    "You dump your load in your pants. It makes a mess but it feels great."
    the_girl "Wow..."
    return

label transition_default_drysex_cowgirl(the_girl, the_location, the_object):
    $ drysex_cowgirl.redraw_scene(the_girl)
    "You lie down on the [the_object.name]. [the_girl.title] swings a leg over your body and straddles you."
    if the_girl.vagina_available:
        "She leans back and grinds herself against you. She rubs her pussy along your cock, your pants the only thing separating the two."
    else:
        "She leans back and grinds herself against you. It feels good, even with your clothes on."
    return

label strip_drysex_cowgirl(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = drysex_cowgirl.position_tag)
    "[the_girl.title] struggles out of her [the_clothing.name] and throws it to the side."
    return

label strip_ask_drysex_cowgirl(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name]. Would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = drysex_cowgirl.position_tag)
            "[the_girl.title] slows down her pace while she strips out of her [the_clothing.name]. When she's free of it she puts her hands on your chest and fucks you faster again."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 70:
                the_girl "Yeah? Do I look sexy in it?"
                "She sighs happily while she rides you."
            else:
                the_girl "Yeah? Do I look like a good little slut in it? Because that's what I feel like right now!"
                "She sighs happily while she rides your cock hard and fast."
            return False

label orgasm_drysex_cowgirl(the_girl, the_location, the_object):
    "[the_girl.title] works her hips faster and her breathing grows heavier."
    the_girl "Oh god!"
    $ the_girl.have_orgasm()
    "With one last gasp she collapses down against you. Her thighs quiver as she climaxes."
    "After a second [the_girl.title] regains control of herself."
    "She leans back and starts to grind against you again, but much slower now."
    return

label GIC_outro_drysex_cowgirl(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal == "hate fuck" or the_goal == "waste cum":
        "With each stroke of her hips [the_girl.title] brings you closer and closer to cumming. You're finally driven past the point of no return."
        mc.name "Fuck, I'm going to cum!"
        the_person "Wow, already?"
        "It feels too good. You feel yourself begin to dump your load in your pants."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
        the_person "Hah! What a waste of cum."
        "It makes a mess, but you finish cumming."
    else:
        $ drysex_cowgirl.call_default_outro(the_girl, the_location, the_object)
