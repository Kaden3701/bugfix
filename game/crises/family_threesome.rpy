# Before the family threesome flag is set, the crisis chance is high (it unlocks other parts of the game)
# After first occurrence the chance is lowered, since we don't want it to happen too often.

init 2 python:
    def SB_fetish_vaginal_family_threesome_requirement():
        if mc.is_in_bed and mc.energy > 50:
            if lily.is_available and mom.is_available:
                return willing_to_threesome(lily, mom)
        return False

    crisis_list.append([
        Action("Family Threesome",SB_fetish_vaginal_family_threesome_requirement,"SB_fetish_vaginal_family_threesome_label")
        , 3])

label SB_fetish_vaginal_family_threesome_label():
    $ the_person = lily
    $ scene_manager = Scene()

    $ mc.change_location(bedroom) #Make sure we're in our bedroom.

    #Make sure everyone is up for this because sex is fun and getting tired after one round of sex isn't
    if the_person.energy < the_person.max_energy:
        $ the_person.energy = the_person.max_energy
    if mom.energy < mom.max_energy:
        $ mom.energy = mom.max_energy

    "Laying in your bed, you hear a knock on your door. You hear [the_person.possessive_title] from the other side of the door."
    the_person "Hey [the_person.mc_title], you still up? I was just wondering if I could come in for a bit?"
    "You invite [the_person.possessive_title] in. You immediately start to get aroused when you see what she is wearing."
    $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))
    $ mom.apply_outfit(mom.get_random_appropriate_underwear(guarantee_output = True))
    $ scene_manager.add_actor(the_person)
    $ mc.change_locked_clarity(10)
    the_person "So... I was wondering... is it okay if I sleep in here with you tonight?"
    menu:
        "Not tonight":
            mc.name "Sorry [the_person.title]... I had a long day and I'm pretty worn out... maybe tomorrow?"
            "She is clearly disappointed."
            the_person "Whatever [the_person.mc_title]... see you in the morning I guess?"
            "You head for bed, looking forward to a restful night's sleep."
            $ the_person.change_stats(happiness = -5, obedience = -2)
            return
        "Strip first" if not the_person.outfit.has_full_access:
            mc.name "That sounds good [the_person.title], I could use a bed warmer. Why don't you get naked first?"
            "[the_person.possessive_title] smiles at you."
            the_person "Aww, does my [the_person.mc_title] wanna see his [the_person.title] get naked for him? What a pervert!"
            "[the_person.possessive_title] winks at you before stripping down."
            $ scene_manager.strip_full_outfit(person = the_person)
            $ mc.change_locked_clarity(20)
            mc.name "Damn [the_person.title], you are really getting good at that..."
            $ scene_manager.update_actor(the_person, position="kneeling1", display_transform = character_center_flipped)
            "She begins to crawl up your bed towards you."
        "Hop in!" if the_person.outfit.has_full_access:
            mc.name "I was just thinking my bed felt cold."
            the_person "Mmmm, I can think of a few ways to keep you warm."
            $ scene_manager.update_actor(the_person, position="kneeling1", display_transform = character_center_flipped)
            "[the_person.possessive_title] gives you a wink and then begins to crawl up the bed towards you."

    "You are so busy checking out [the_person.possessive_title], your brain barely registers a knock on your door. [the_person.possessive_title] is just sitting down in your lap when you hear a gasp from your door."
    if mc.business.event_triggers_dict.get("family_threesome", False):
        $ scene_manager.add_actor(mom, emotion = "happy")
        mom "Is that [the_person.fname]? Ah good, I thought I heard you come in here."
        the_person "Mom! Going to join us again tonight?"
        mom "If that's okay with you two... I don't want to be a bother."
        mc.name "[mom.title]. Having you here can only make things even better."
        $ scene_manager.strip_full_outfit(person = mom)
        $ scene_manager.update_actor(mom, position = "sitting")
        $ mc.change_locked_clarity(20)
        "[mom.title] sits on the edge of your bed."
        the_person "So... how are we doing it tonight?"
        "They both look to you."
        mom "[mom.mc_title], you're the man here. What do you want to do?"
        call start_threesome(lily, mom) from _threesome_family_evening_event_1
        $ scene_manager.update_actor(the_person, position = "back_peek", display_transform = character_center_flipped)
        $ scene_manager.update_actor(mom, position = "missionary", display_transform = character_right)
        $ the_report = _return
        if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0:  #Happy family
            "[the_person.possessive_title] falls into your bed on one side of you on her side, while [mom.title] lays on her back next to you."
            mom "Oh my god... you two... that was amazing!"
            $ mom.change_happiness(10)
            the_person "I know... I swear [the_person.mc_title] makes me cum my brains out."
            $ the_person.change_obedience(10)
            "You all lay together for a while in your sex induced afterglow. You enjoy the two girls warming you from each side."
        else:
            "The girls fall into your bed beside you. You relax for a little bit, enjoying the warmth of their bodies."
        mom "Well. I should get up before I fall asleep. Goodnight you two!"
        $ scene_manager.update_actor(mom, position = "walking_away")
        the_person "Goodnight mom! Actually, I should probably get to bed as well, I just remembered I have to get up early..."
        $ scene_manager.remove_actor(mom)
        $ scene_manager.update_actor(the_person, position = "walking_away", display_transform = character_right)
        "You watch as [the_person.possessive_title] gets up and excuses herself, her ass swaying back and forth as she walks away."
        "God damn you love this family!"
        $ scene_manager.remove_actor(the_person)

    else:
        $ scene_manager.add_actor(mom, emotion = "angry")
        mom "Is that... [the_person.fname]!?! What are you... why are you naked in [mom.mc_title]'s room?" #NOTE: the_person doesn't necessarily know mom's title for the MC, but still somewhat makes sense.
        "[mom.possessive_title] is shocked to discover that you and [the_person.possessive_title] are in your room, clearly about to get busy."
        the_person "Mom! Nothing was... wait... what are you wearing?"
        "[mom.possessive_title] quickly realizes that [the_person.possessive_title] is here... doing exactly what she was coming here to do. Her cheeks turn red with embarrassment."
        "You think quickly. Maybe you can salvage this situation?"
        mc.name "Hey [mom.title]... you look amazing! Want to come in for a little bit? [the_person.title] and I are just getting started."
        "You can see a clear look of conflict in [mom.possessive_title]'s eyes. Up until now, your antics have been isolated to you and her, in her mind anyway. She's slowly processing that you have a similar relationship with [the_person.possessive_title]."
        mom "I mean... I suppose I could... for a bit..."
        "Still in a bit of a daze, [mom.possessive_title] comes into your room, closing the door behind her. She sits over at your desk and looks over at you and [the_person.possessive_title]."
        $ scene_manager.update_actor(mom, position = "sitting")
        "[the_person.possessive_title] looks back at you, still a little unsure of herself. You hold up your hands and beckon her."
        $ scene_manager.update_actor(the_person, position = "cowgirl")
        "You draw her into your arms. She melts into you giving you a kiss."
        $ mc.change_locked_clarity(10)
        "Your lips lock together in a passionate kiss. [the_person.possessive_title]'s body melts into yours in surrender, even as [mom.possessive_title] looks on."
        mom "Oh my... [mom.mc_title]... [the_person.fname]..."
        "You move your hands down [the_person.possessive_title]'s waist and around to her butt. You give both cheeks a squeeze."
        "She presses her body against yours and sighs."
        the_person "Mmm... I can't wait for you to fuck me..."
        $ the_person.change_arousal(10)
        if mom.vagina_available:
            "You glance over at [mom.possessive_title]. She is watching you and [the_person.possessive_title] intently and has one hand between her legs, stroking the outer lips of her pussy."
        else:
            "You glance over and see that [mom.possessive_title] has her hand in her [mom.outfit.get_lower_top_layer.display_name], playing with herself as she watches."
        $ mc.change_locked_clarity(10)
        $ mom.change_arousal(10)
        "This is going better than you expected! You get a little braver."
        mc.name "Hey [mom.title]... why don't you join us? There's no reason we can't all have a little family fun together..."
        "[mom.possessive_title] sighs. She gives in to her arousal and need."
        mom "Okay... What do you want me to do?"
        mc.name "Come here. I'll please you with my mouth while [the_person.title] rides my cock."
        "[mom.title] hesitates for a second, but then relents."
        mom "That sounds like fun... Okay! I'll do it!"
        $ scene_manager.strip_full_outfit(person = mom)
        $ mc.change_locked_clarity(10)
        call start_threesome(lily, mom, start_position = Threesome_double_down) from threesome_event_test_call_2
        $ mc.business.event_triggers_dict["family_threesome"] = True
        "Wow, you just had sex with [the_person.possessive_title] and [mom.possessive_title]! You can't believe how lucky you are."
        "Maybe this is the event that will finally set things in motion for your family. All three of you are in this sexually together."
        "Eventually, the girls get up."
        $ scene_manager.update_actor(the_person, position = "stand2", display_transform = character_center_flipped)
        $ scene_manager.update_actor(mom, position = "stand4", display_transform = character_right)
        $ mom.increase_opinion_score("incest")
        mom "Mmm... wow... I guess... that was really good actually... Maybe we should do this more often..."
        $ scene_manager.update_actor(mom, position = "walking_away")
        "[mom.possessive_title] turns and starts to walk out."
        $ scene_manager.remove_actor(mom)
        $ the_person.increase_opinion_score("incest")
        the_person "Holy fuck [the_person.mc_title], that was so hot, I can't believe you got mom to join us..."
        mc.name "I know! This might not be the last time that happens."
        the_person "Oh god, I can't wait. See you in the morning bro!"
        "[the_person.possessive_title] says goodnight and then turns to leave."
        $ scene_manager.remove_actor(the_person)

    python:
        scene_manager.clear_scene()
        the_person.reset_arousal()
        the_person.apply_planned_outfit()

        mom.reset_arousal()
        mom.apply_planned_outfit()

        mc.location.show_background()
        clear_scene()
    return
