init:
    python:
        spanking = Position(name = "Spanking", slut_requirement = 30, slut_cap = 50, requires_hard = False, requires_large_tits = False,
            position_tag = "standing_doggy", requires_location = "Low", requires_clothing = "None", skill_tag = "Foreplay",
            girl_arousal = 0, girl_energy = 5,  #We use person specific variables to determine arousal
            guy_arousal = 0, guy_energy = 5,
            connections = [],
            intro = "intro_spanking",
            scenes = ["scene_spanking_1", "scene_spanking_2"],
            outro = "outro_spanking",
            transition_default = "transition_default_spanking",
            strip_description = "strip_spanking", strip_ask_description = "strip_ask_spanking",
            orgasm_description = "orgasm_spanking",
            taboo_break_description = "taboo_break_spanking",
            verb = "spank",
            opinion_tags = ["being submissive"], record_class = "Spankings",
            default_animation = blowjob_bob,
            associated_taboo = "touching_body")

init 1 python:
    spanking.link_positions(standing_doggy, "transition_spanking_standing_doggy")

            #TODO transitions to standing anal

    def calc_spank_factor(person):  #Returns an int that is representative of how much someone likes this round of spanking.
        factor = 3 + (person.get_opinion_score("being submissive") * 3)
        factor += (- (person.event_triggers_dict.get("spank_level", 0)))
        return factor

    def update_ass_condition(person): #update ass condition everytime spanking is initiated to make sure we describe it correctly.
        if person.event_triggers_dict.get("last_day_spanked", 0) <= day:
            heal_factor = (day - person.event_triggers_dict.get("last_day_spanked", 0)) * 2 #Heal 2 stages per day since last spanking
            person.event_triggers_dict["spank_level"] = __builtin__.max((person.event_triggers_dict.get("spank_level", 0) - heal_factor), 0) #heal by 1 per day, minimum of zero
        person.event_triggers_dict["last_day_spanked"] = day
        return

    def spank_factor_increment(person):
        if person.event_triggers_dict.get("spank_level", 0) == 0:
            person.event_triggers_dict["spank_level"] = 1
        else:
            person.event_triggers_dict["spank_level"] += 1
        return

    #Returns a string based on the physical appears of the girl's ass
    #Assume previous sentence flows something like, "The girls ass is [this return value]"
    def spanking_get_ass_description(person):
        if person.event_triggers_dict.get("spank_level", 0) < 2:
            return "flawless. It is perky and ready for you to discipline."
        elif person.event_triggers_dict.get("spank_level", 0) < 4:
            return "slightly red. There are a few marks, but it still looks ripe for further discipline."
        elif person.event_triggers_dict.get("spank_level", 0) < 6:
            return "red. It looks like she has been disciplined properly."
        elif person.event_triggers_dict.get("spank_level", 0) < 8:
            return "bright red. There are a few small bruises. She has been thoroughly punished."
        else:
            return "bruised. She has been punished nearly to her limit. You might want to stop soon."




label intro_spanking(the_girl, the_location, the_object):
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over the [the_object.name]."
    mc.name "Someone has been a bad girl. It's time for your punishment, [the_girl.title]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, visible_enough = True, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    $ update_ass_condition(the_girl)

    return

label taboo_break_spanking(the_girl, the_location, the_object):
    mc.name "Someone has been a bad girl. It's time for you punishment, [the_girl.title]."
    the_girl "What... what are you gonna do to me?"
    mc.name "You need a spanking. It's only natural for a bad girl like you to get a spanking once in a while."
    the_girl "Oh god... I... Okay [the_girl.mc_title]..."
    $ spanking.redraw_scene(the_girl)
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over [the_object.name]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, visible_enough = True, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    $ update_ass_condition(the_girl)

    return

label scene_spanking_1(the_girl, the_location, the_object):
    $ spank_factor = calc_spank_factor(the_girl)
    $ ass_desc = spanking_get_ass_description(the_girl)
    "You look down at [the_girl.possessive_title]'s ass. It is [ass_desc]"
    $ play_spank_sound()
    "*SMACK*"
    "You give her a solid spank. She lets out a little yelp."
    $ play_spank_sound()
    "*SMACK* *SMACK* SMACK*"
    "You don't let up, giving her a solid spanking."
    if spank_factor > 5: #She loves it.
        the_girl "Oh god [the_girl.mc_title]! Give it to me good! Oh god!"
        "She is really getting into this. With each spank she wiggles her ass, giving you an enticing target."
        $ the_girl.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
        $ the_girl.change_slut(spank_factor - 5, 30)
    elif spank_factor > 0:
        the_girl "Oh... I'm sorry [the_girl.mc_title]! Oh god..."
        "She keeps her ass still, taking your blows. Her ass makes an enticing target."
        $ the_girl.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
        $ the_girl.change_obedience(spank_factor)
    elif spank_factor > -5:
        the_girl "Ouch! I'm sorry [the_girl.mc_title]! That really hurts..."
        "With each spank, she flinches a bit."
        $ the_girl.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
        $ the_girl.change_obedience(-(spank_factor-3))
    else:
        the_girl "Fuck! That hurts! Why are you doing this? Please stop!"
        "She is trembling. With each spank she flinches and quakes."
        $ the_girl.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))
        $ the_girl.change_obedience(-spank_factor)
        $ the_girl.change_love(spank_factor)
    $ spank_factor_increment(the_girl)
    if mc.arousal_perc < 20:
        $ mc.change_arousal(5)
    return

label scene_spanking_2(the_girl, the_location, the_object):
    $ spank_factor = calc_spank_factor(the_girl)
    $ ass_desc = spanking_get_ass_description(the_girl)

    $ play_spank_sound()
    "*SMACK*"
    "You look at her bottom, deciding what to do next..."
    menu:
        "Continue spanking":
            call scene_spanking_1(the_girl, the_location, the_object) from _call_scene_spanking_1_from_scene_2
        "Rub her ass":
            "Instead of smacking her ass again, you start rubbing, it's [ass_desc]"
            if spank_factor > 5:
                the_girl "Oh, that feels very nice, [the_girl.mc_title]."
                "She starts to move her ass, moving along with your rubbing motions."
            elif spank_factor > 0:
                the_girl "Oh... I didn't expect that [the_girl.mc_title]! Oh god..."
                "She keeps her ass motionless in order to minimize the discomfort."
            elif spank_factor > -5:
                the_girl "Ouch! I'm sorry [the_girl.mc_title]! I'm a little tender, could your rub a little softer..."
                "You soften your touch and softly rub her apple red buttocks."
            else:
                the_girl "Jesus! That hurts! Please stop, even a feathers touch would be to painful!"
                "She is trembling. With each touch of a finger her legs start shaking."

            $ the_girl.change_arousal(spank_factor * ((mc.sex_skills["Foreplay"] / 10) + 1))

        "Finger her pussy" if the_girl.get_opinion_score("being fingered") > 0:
            "You slide your fingers in and out of her pussy, stroking the inside of that soft tunnel."
            $ play_moan_sound()
            "Each movement draws moans of pleasure from [the_girl.possessive_title], who presses herself against you."
            "She places one of her own hands over yours, encouraging you to speed up."
            the_girl "Just like that... Ah..."
            $ the_girl.change_arousal((the_girl.get_opinion_score("being fingered") + 1) * 5)

        "Finger Her pussy\n{color=#ff0000}{size=18}Must like being fingered{/size}{/color} (disabled)" if the_girl.get_opinion_score("being fingered") <= 0:
            pass

        "Finger her ass" if the_girl.get_opinion_score("anal sex") > 0:
            "You slide your finger through her wet slit and move it up to her sphincter slightly lubricating it."
            the_girl "Oh god I love it when you do this..."
            "[the_girl.possessive_title] is pushing her ass against your finger, her breathing heavy, enticing you to keep going. You push your finger deep into her bowel."
            the_girl "Oh!!! [the_girl.mc_title] YES!"
            "You continue for a while. [the_girl.title] clearly enjoys the anal penetration. Eventually you pull your finger out and continue the punishment."
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") * 10)

        "Finger her ass\n{color=#ff0000}{size=18}Must like anal sex{/size}{/color} (disabled)" if the_girl.get_opinion_score("anal sex") <= 0:
            pass
    if mc.arousal_perc < 20:
        $ mc.change_arousal(5)
    return


label outro_spanking(the_girl, the_location, the_object):
    pass #arousal is zero for MC. this shouldn't be possible
    return


label transition_default_spanking(the_girl, the_location, the_object):
    $ spanking.redraw_scene(the_girl)
    "You stand behind [the_girl.title] and put your arms around her waist, pushing her so she is bending over [the_object.name]."
    mc.name "Someone has been a bad girl. It's time for your punishment, [the_girl.title]."
    if the_girl.vagina_visible:
        "You don't waste any time and put your hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    else:
        mc.name "Let's get these out of the way first."
        $ the_girl.strip_to_vagina(position = spanking.position_tag, visible_enough = True, prefer_half_off = True)
        "You put both hands on her ass, groping her cheeks."
        $ play_spank_sound()
        "You raise one hand and bring it down hard, give her ass a firm spank."
    $ update_ass_condition(the_girl)

    return

label strip_spanking(the_girl, the_clothing, the_location, the_object):
    the_girl "Oh my god... I'm so hot... I need to get this off!"
    $ the_girl.draw_animated_removal(the_clothing, position = spanking.position_tag)
    "She strips off her [the_clothing.name] while you're spanking her, moaning the whole time."
    return

label strip_ask_spanking(the_girl, the_clothing, the_location, the_object):
    the_girl "Everything feels so tight, I want to take it all off... Please can I?"
    "[the_girl.possessive_title] grabs onto her [the_clothing.name], waiting for you to tell her what to do."
    menu:
        "Let her strip":
            mc.name "Take it off.."
            $ the_girl.draw_animated_removal(the_clothing, position = spanking.position_tag)
            "[the_girl.possessive_title] takes off her [the_clothing.name] and drops it to the side while you grope her ass."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 80:
                the_girl "Do you think I look sexy in it?"
            else:
                the_girl "Don't you think I would look better wearing your cum? That would be so fitting for your dirty little slut, wouldn't it?"
            return False

label orgasm_spanking(the_girl, the_location, the_object):
    the_girl "Oh god, oh god, oh... OH... OHHHH!"
    "Her whole body tenses up. You give her a few more spanks as she cums, just from the sensations of being spanked."
    $ the_girl.call_dialogue("climax_responses_foreplay")
    "She quivers with pleasure for a few seconds before her whole body relaxes."
    the_girl "Ah... I'm sorry."
    mc.name "There you go, being bad again!"
    $ play_spank_sound()
    "You give her another hard spank."
    return

label transition_spanking_standing_doggy(the_girl, the_location, the_object):
    "You are done spanking her. You run your fingers along her slit a bit, getting a feel for how ready she is."
    mc.name "That's enough spanking [the_girl.title]. Now I'll make it feel all better.."
    the_girl "Oh yes, [the_girl.mc_title], make me feel good."
    "You bounce your hard shaft on her ass a couple of times before sliding your cock between her thighs."
    "You continue your back and forth motion, rubbing your cock along her already wet pussy lips."
    if the_girl.get_opinion_score("vaginal sex") > 0:
        the_girl "Oh... Please..."
    "You continue to move your cock forwards and backwards teasing her [the_girl.pubes_description] pussy."
    if the_girl.has_taboo("vaginal_sex"):
        $ the_girl.call_dialogue(doggy.associated_taboo+"_taboo_break")
        "You hold onto [the_girl.title]'s hips with one hand and your cock with the other, guiding it as you push forward."
        "After a moment of resistance your cock spreads her pussy open and you slide smoothly inside of her."
        the_girl "Oh god... Ah..."
        "You start with short thrusts, each time going a little bit deeper. Soon you're working your full length in and out of her wet hole."
        $ the_girl.break_taboo("vaginal_sex")
    else:
        "Once you're both ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

# when breaking the taboo we don't go into the default transition, so we use this custom label to trigger the transition dialog
label transition_spanking_to_standing_doggy_taboo_break_label(the_girl, the_location, the_object):
    call transition_spanking_standing_doggy(the_girl, the_location, the_object) from _call_transition_spanking_to_standing_doggy_taboo_break_label
    return
