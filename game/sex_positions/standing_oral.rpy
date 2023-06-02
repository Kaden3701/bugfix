#Original file by Badrabbit
init:
    python:
        standing_oral = Position(name = "Kneeling oral", slut_requirement = 40, slut_cap = 70, requires_hard = False, requires_large_tits = False,
            position_tag = "stand3", requires_location = "Stand", requires_clothing = "Vagina", skill_tag = "Oral",
            girl_arousal = 15, girl_energy = 3,
            guy_arousal = 3, guy_energy = 10,
            connections = [],
            intro = "intro_standing_oral",
            scenes = ["scene_standing_oral_1","scene_standing_oral_2"],
            outro = "outro_standing_oral",
            transition_default = "transition_default_standing_oral",
            strip_description = "strip_standing_oral",
            strip_ask_description = "strip_ask_standing_oral",
            orgasm_description = "orgasm_standing_oral",
            taboo_break_description = "taboo_break_standing_oral",
            verb = "lick",
            opinion_tags = ["sex standing up", "getting head"],
            record_class = "Cunnilingus",
            default_animation = blowjob_bob,
            associated_taboo = "licking_pussy")
        # don't add to list of positions, you need to unlock it ;)
        list_of_positions.append(standing_oral)


label intro_standing_oral(the_girl, the_location, the_object):
    if girl_in_charge:
        "[the_girl.title] pulls you close against her."
        if blowjob in report_log.get("positions_used",[]) or deepthroat in report_log.get("positions_used",[]):
            the_girl "It's your turn. On your knees."
        else:
            the_girl "I have something I want you to do."
            mc.name "Oh? What might that be?"
        if (the_girl.get_opinion_score("getting head") > 0 and the_girl.get_known_opinion_score("getting head")):
            the_girl "You know what I like."
            "[the_girl.title] winks at you as she gently but firmly pushes your shoulders down until you are kneeling before her."
        else:
            "[the_girl.title] gently but firmly pushes your shoulders down until you are kneeling before her."

        $ standing_oral.redraw_scene(the_girl)

        if not the_girl.vagina_available:
            $ the_girl.strip_to_vagina(position = standing_oral.position_tag, visible_enough = True, prefer_half_off = True)
            "She quickly moves her clothes out of the way."

        if the_girl.sex_record.get("Cunnilingus", 0) > 1 and mc.sex_skills["Oral"] > 5:
            if the_girl.love < 0:
                the_girl "Well? Get to it!"
            else:
                the_girl "Don't be shy. We both know you're good at this."
                "She shivers slightly in anticipation."
                $ the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
        "She runs the fingers of one hand through your hair as she pulls your face to her [the_girl.pubes_description] pussy."
        the_girl "Now start licking."
        "You do as you are told."
    else:
        if not the_girl.vagina_available:
            "You quickly move her clothes out of the way."
            $ the_girl.strip_to_vagina(position = standing_oral.position_tag, visible_enough = True, prefer_half_off = True)

        $ standing_oral.redraw_scene(the_girl)
        "You kneel before [the_girl.title] and gently start to lick her pussy."
        if the_girl.get_opinion_score("taking control")> 0:
            if the_girl.love < 0:
                the_girl "At least you know your proper place."
            else:
                the_girl "My, my. What did I do to deserve this?"
            $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))
        elif the_girl.get_opinion_score("getting head") < 0 or (the_girl.get_opinion_score("getting head") == 0 and mc.sex_skills["Oral"] < 2) or (the_girl.get_opinion_score("getting head") == 1 and mc.sex_skills["Oral"] == 0):
            the_girl "You know you don't have to do that."
            "[the_girl.possessive_title] pushes your head away."
            $ the_girl.change_arousal(-10)
            if the_girl.get_opinion_score("giving blowjobs") > 0:
                the_girl "How about we swap and I do something for you instead?"
        elif the_girl.get_opinion_score("getting head") == 2 or (the_girl.get_opinion_score("getting head") == 0 and mc.sex_skills["Oral"] > 7) or (the_girl.get_opinion_score("getting head") == 1 and mc.sex_skills["Oral"] > 5):
            the_girl "I could get used to this."
            the_girl "That feels GOOD."
        else:
            the_girl "Mmm."
    return

label taboo_break_standing_oral(the_girl, the_location, the_object):
    if girl_in_charge:
        the_girl "We haven't done this before but I want to do it."
        "[the_girl.title] pulls you close against her."
        the_girl "I have something I want you to do."
        mc.name "Oh? What might that be?"
        if not the_girl.has_taboo("sucking_cock"):
            the_girl "It's your turn on your knees."
        "[the_girl.title] gently but firmly pushes your shoulders down until you are kneeling before her."
        if not the_girl.vagina_available:
            $ the_girl.strip_to_vagina(standing_oral.position_tag, visible_enough = True, prefer_half_off = True)
            "She quickly moves her clothes out of the way."
        "She runs the fingers of one hand through your hair as she pulls your face to her pussy."
        the_girl "Now start licking."
        "You do as you are told."
    else:
        "You kneel before [the_girl.title]."
        if not the_girl.vagina_available:
            "You quickly move her clothes out of the way."
            $ the_girl.strip_to_vagina(standing_oral.position_tag, visible_enough = True, prefer_half_off = True)
        $ the_girl.call_dialogue("licking_pussy_taboo_break")
        "You gently lick her [the_girl.pubes_description] pussy."
        if the_girl.get_opinion_score("getting head") < 0:
            the_girl "You know you don't have to do that."
    $ the_girl.break_taboo("licking_pussy")
    return

label scene_standing_oral_1(the_girl, the_location, the_object):
    if the_girl.arousal_perc > 70:
        "[the_girl.possessive_title]'s pussy is dripping wet, filling your mouth with the taste of her juices."
    $ the_girl.call_dialogue("sex_responses_oral")
    if girl_in_charge or the_girl.get_opinion_score("taking control") > 0:
        "[the_girl.possessive_title] holds your head in place with one hand."
        "You use your tongue on [the_girl.possessive_title]."
    else:
        "You use your tongue on [the_girl.possessive_title]. On your knees in front of her, you look up and admire her shapely body and chest."
        "[the_girl.possessive_title] rests one hand on your shoulder."
    if the_girl.tits_available:# TODO: put in not heart pasties? How do I do that?
        if the_girl.get_opinion_score("being submissive") > 0:
            "[the_girl.possessive_title] reaches up and pinches one of her nipples hard, wincing from excitement and pain. She then proceeds to tweak and roll it between her fingers."
            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
        if the_girl.has_large_tits:
            "With one hand she softly squeezes her [the_girl.tits_description], gently playing with her nipple."
        else:
            "With one hand she squeezes her [the_girl.tits_description], gently playing with her nipple."
    else:
        if the_girl.has_large_tits:
            "With one hand she softly squeezes her [the_girl.tits_description]."
        else:
            "With one hand she squeezes her [the_girl.tits_description]."
    return


label scene_standing_oral_2(the_girl, the_location, the_object):
    if the_girl.arousal_perc > 75:
        "Her pussy is dripping wet now, her juices are running down your face and chin."
        "You can tell she is getting close, so you double down on your efforts to get [the_girl.title] off."
        the_girl "Oh god, that feels so good..."
        "She closes her eyes and tilts her head back. She grips your head tightly."
        $the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
    else:
        if girl_in_charge or the_girl.get_opinion_score("taking control") > 0:
            "[the_girl.possessive_title] grabs your hair and holds your head in place as you continue to lick."
            the_girl "Look me in the eyes."
            "You look up at her as you continue. She smiles down at you, clearly enjoying the experience."
            the_girl "Keep going, [the_girl.mc_title]."
            $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))
        else:
            if the_girl.love > 0:
                "[the_girl.possessive_title] strokes your head affectionately, as you continue to lick."
            else:
                "[the_girl.possessive_title] holds your head in place, as you continue to lick."

        menu:
            "Lick firmly and steadily":
                "You lick at [the_girl.possessive_title]'s pussy."
                $ the_girl.call_dialogue("sex_responses_oral")
                $ the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
                "You continue to lick until your tongue starts to tire."

            "Do what you think best":
                $ the_girl.call_dialogue("sex_responses_oral")
                $ the_girl.change_arousal(mc.sex_skills["Oral"])
                if (mc.sex_skills["Oral"]) > 4:
                    the_girl "Oh yes! Do that!"
                if the_girl.get_opinion_score("taking control") > 0:
                    "[the_girl.possessive_title] grabs your hair and hold your head in place as you continue to lick."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))
                "You continue to play with [the_girl.possessive_title]'s pussy with your mouth until you start to tire."
    return


label outro_standing_oral(the_girl, the_location, the_object):
    $ the_goal = the_girl.get_sex_goal()

    $ play_moan_sound()
    "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
    "You touch yourself, stroking your hard cock between your legs while you pleasure her."
    "[the_girl.possessive_title] can tell that you are on the verge of climax."
    "Finally you've gone too far, pushing yourself to climax."
    if not girl_in_charge:
        "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto the floor in front of [the_girl.title]."
        if the_girl.get_opinion_score("taking control") > 0:
            the_girl "Well look at that."
            the_girl "You got a secret sub side I should know about?"
            the_girl "Cumming buckets on your knees with your face in my pussy?"
        if the_girl.get_opinion_score("getting head") < 0:
            the_girl "That's maybe a good time to stop. Do you think?"
    if girl_in_charge:
        if the_girl.love < 0:
            the_girl "You gonna cum? Are you?"
            "[the_girl.possessive_title] pulls your head close into her as she grinds your face into her pussy as you cum."
            "You jerk your cock and blast out a load of cum onto the floor in front of [the_girl.title]."
        else:
            "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto the floor in front of [the_girl.title]."
        the_girl "Well look at that."
        "She watches as your cock twitches and finishes."
        the_girl "You got a secret sub side I should know about?"
        the_girl "Cumming buckets with your face ground in my pussy?"
        if the_girl == cousin:
            the_girl "Doesn't exactly scream Macho Man does it, cuz?"
            the_girl "Maybe screaming is the right word."
        if the_goal == "get off" or the_goal == "hate fuck":
            the_girl "Don't forget why you're there."
        elif the_goal == "waste cum":
            the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
            "She gives a slight smile."
        elif the_goal == "get mc off":
            the_girl "There we go."
            the_girl "Feeling better now?"
        else: #wasted opportunity
            the_girl "What a waste. Next time tell me when you're close."
    return

label transition_default_standing_oral(the_girl, the_location, the_object):
    if girl_in_charge:
        "[the_girl.title] pulls you close against her."
        if blowjob in report_log.get("positions_used",[]) or deepthroat in report_log.get("positions_used",[]):
            the_girl "It's your turn. On your knees."
        else:
            the_girl "I have something I want you to do."
            mc.name "Oh? What might that be?"
        if (the_girl.get_opinion_score("getting head") > 0 and the_girl.get_known_opinion_score("getting head")):
            the_girl "You know what I like."
            "[the_girl.title] winks at you as she gently but firmly pushes your shoulders down until you are kneeling before her."
        else:
            "[the_girl.title] gently but firmly pushes your shoulders down until you are kneeling before her."
        $ standing_oral.redraw_scene(the_girl)
        if the_girl.sex_record.get("Cunnilingus", 0) > 1 and mc.sex_skills["Oral"] > 5:
            if the_girl.love < 0:
                the_girl "Well? Get to it!"
            else:
                the_girl "Don't be shy. We both know you're good at this."
                "She shivers slightly in anticipation."
                $ the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
        "She runs the fingers of one hand through your hair as she pulls your face to her [the_girl.pubes_description] pussy."
        the_girl "Now start licking."
        "You do as you are told."
    else:
        $ standing_oral.redraw_scene(the_girl)
        "You kneel before [the_girl.title] and gently start to lick her [the_girl.pubes_description] pussy."
        if the_girl.get_opinion_score("taking control")> 0:
            if the_girl.love < 0:
                the_girl "At least you know your proper place."
            else:
                the_girl "My, my. What did I do to deserve this?"
            $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))
        elif the_girl.get_opinion_score("getting head") < 0 or (the_girl.get_opinion_score("getting head") == 0 and mc.sex_skills["Oral"] < 2) or (the_girl.get_opinion_score("getting head") == 1 and mc.sex_skills["Oral"] < 3):
            the_girl "You know you don't have to do that."
            "[the_girl.possessive_title] pushes your head away."
            $ the_girl.change_arousal(-10)
            if the_girl.get_opinion_score("giving blowjobs") > 0:
                the_girl "How about we swap and I do something for you instead?"
        elif the_girl.get_opinion_score("getting head") >= 2 or (the_girl.get_opinion_score("getting head") == 0 and mc.sex_skills["Oral"] > 7) or (the_girl.get_opinion_score("getting head") == 1 and mc.sex_skills["Oral"] > 5):
            the_girl "I could get used to this."
            the_girl "That feels GOOD."
        else:
            the_girl "Mmm."
    return


label strip_standing_oral(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = standing_oral.position_tag)
    "[the_girl.possessive_title] strips off her [the_clothing.name] while you're eating her out, throwing it to the side."
    $ standing_oral.redraw_scene(the_girl)
    return

label strip_ask_standing_oral(the_girl, the_clothing, the_location, the_object):
    if girl_in_charge:
        $ the_girl.call_dialogue("sex_strip")
        $ the_girl.draw_animated_removal(the_clothing, position = standing_oral.position_tag)
        "[the_girl.possessive_title] strips off her [the_clothing.name] while you're eating her out, throwing it to the side."
        return True
    else:
        the_girl "[the_girl.mc_title], I'm like to take off my [the_clothing.name] if you don't mind."
        menu:
            "Let her strip":
                "You look up from between her legs and nod."
                mc.name "Take it off for me."
                $ the_girl.draw_animated_removal(the_clothing, position = standing_oral.position_tag)
                "She strips out of her [the_clothing.name] and throws it to the side while you move back in and lick at her cunt."
                return True
            "Leave it on":
                "You look up from between her legs and shake your head."
                mc.name "No, I like how you look with it on."
                the_girl "Yeah? Do I look sexy in it? Mmmm..."
                if the_girl.sluttiness < 80:
                    the_girl "Do you think I look sexy in it?"
                else:
                    the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
                return False

label orgasm_standing_oral(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You notice [the_girl.possessive_title]'s moans becoming louder, and her legs twitching more noticeably on either side of you."
    $ the_girl.call_dialogue("climax_responses_oral")
    "Her whole body tenses up and she grabs you by the hair. A shiver runs through her body as she climaxes."
    "The moment passes and she relaxes. For a moment all she can do is look down at you and pant."
    if the_girl.get_opinion_score("getting head") < 0:
        if the_girl.love > 0:
            the_girl "That was great - your turn now."
        else:
            the_girl "OK. Now let's do something else."
    if girl_in_charge:
        pass
    else:
        the_girl "Ah... Keep going... I bet you can make me cum again."
    return
