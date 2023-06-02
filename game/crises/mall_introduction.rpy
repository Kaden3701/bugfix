## Mall Introduction Crisis Mod by Tristimdorion
init 2 python:
    def mall_introduction_get_people_with_status():
        strangers = []
        known_people = []
        for loc in get_current_location_hub():
            strangers += unknown_people_at_location(loc, unique_character_list) # don't introduce unique characters
            known_people += known_people_at_location(loc)
        return strangers, known_people

    def mall_introduction_requirement():
        if not time_of_day in [1,2,3]: # only during morning afternoon or evening
            return False
        if mc.business.days_since_event("mall_introduction", set_if_none = True) < TIER_0_TIME_DELAY:
            return False
        if not get_current_location_hub() in [mall_hub, downtown_hub, gym_hub]:
            return False
        strangers, known_people = mall_introduction_get_people_with_status()
        if __builtin__.len(strangers) > 0 and __builtin__.len(known_people) > 0:
            return True
        return False

    def mall_introduction_get_actors():
        strangers, known_people = mall_introduction_get_people_with_status()
        # pick a person from each
        known_person = get_random_from_list(known_people)
        stranger = get_random_from_list(strangers)
        return (known_person, stranger)

    mall_introduction_action = ActionMod("Mall Introduction", mall_introduction_requirement, "mall_introduction_action_label",
        menu_tooltip = "You meet a stranger and a friend introduces you.", category = "Mall", is_crisis = True)

label mall_introduction_action_label():
    $ (known_person, stranger) = mall_introduction_get_actors()

    if known_person is None or stranger is None:
        return

    python:
        scene_manager = Scene()
        # make sure they don't wear location outfits that don't match current location
        known_person.change_location(mc.location)
        stranger.change_location(mc.location)

        scene_manager.add_actor(known_person, position = "stand4", emotion = "happy", display_transform = character_center_flipped)
        scene_manager.add_actor(stranger, position = "stand3")

    known_person "Oh, hello [known_person.mc_title], how nice to see you here."
    mc.name "Hello [known_person.title], nice to see you too."

    # set titles for unknown person
    python:
        formatted_title = stranger.create_formatted_title(stranger.name + " " + stranger.last_name)
        title_choice = stranger.get_random_title()
        stranger.set_title(title_choice)
        stranger.set_possessive_title(stranger.get_random_possessive_title())

    known_person "Let me introduce my friend [formatted_title]."
    "[formatted_title] holds her hand out to shake yours."

    # sets your title for unknown person
    python:
        title_choice = get_random_from_list(stranger.get_player_titles())
        stranger.set_mc_title(title_choice)
        # set to player full name for intro
        title_choice = mc.name + " " + mc.last_name

    if known_person.is_employee:
        known_person "And this is my boss, [title_choice]."
    elif known_person is lily:
        known_person "And this is my brother, [title_choice]."
    elif known_person is mom:
        known_person "And this is my son, [title_choice]."
    elif known_person is aunt:
        known_person "And this is my nephew, [title_choice]."
    elif known_person is cousin:
        known_person "And this is my cousin, [title_choice]."
    else:
        known_person "And this is my friend, [title_choice]."

    mc.name "It's a pleasure to meet you, [formatted_title]."
    $ scene_manager.update_actor(stranger, emotion = "happy")
    $ stranger.change_love(5)
    stranger "The pleasure is all mine, [stranger.mc_title]."
    if formatted_title != stranger.title:
        stranger "But please, call me [stranger.title]."

    # bonus stats when the person knows you more intimately
    if known_person.sluttiness > 20 or known_person.love > 20:
        if known_person.is_employee:
            if known_person.sluttiness > 40:
                known_person "You should get to know him more intimately [stranger.fname], you should apply for a position in the company."
            else:
                known_person "I promise you [stranger.fname], he is a great boss. You should go out with him sometime."
        else:
            if known_person.sluttiness > 40:
                known_person "He can show you a really good time [stranger.fname], if you know what I mean."
            else:
                known_person "I have to tell you [stranger.fname], he is a great person to hang out with."

        $ stranger.change_stats(happiness = 10, love = 5)

        if stranger.sluttiness > 30:
            stranger "Well, he's very handsome [known_person.fname], I wouldn't mind going on a date with him."
        elif stranger.sluttiness > 10:
            stranger "He is very cute [known_person.fname], I might just do that."
        else:
            stranger "I trust your judgement [known_person.fname], perhaps we could go out sometime."

    mc.name "It was great meeting you both here. I'll see you around [stranger.title]."
    if stranger.has_role(prostitute_role):
        stranger "If you ever want some company, give me a call, I'm sure we can come to some kind of arrangement."
        "She hands you a business card with her phone number."
        $ mc.phone.register_number(stranger)

    $ scene_manager.update_actor(stranger, position = "back_peek")
    $ scene_manager.update_actor(known_person, position = "walking_away")

    "While walking away [stranger.title] looks back at you smiling."

    python: # Release variables
        mc.business.set_event_day("mall_introduction")
        scene_manager.clear_scene()
        title_choice = None
        formatted_title = None
        del stranger
        del known_person
    return
