#Morning crisis
#You wake and move out into the hall. You overhear your mom and Lily talking in Lily's room
#At low sluttiness they are just talking. If one has considerably more than the other, the sluttier is encouraging the other to "loosen up"
#At mid sluttiness you overhear them talking about guys/sex (learn new sexy opinions)
#At mid-high sluttiness they are comparing assets
#At high sluttiness you discover them fucking, option to join or observe
init 2 python:
    def mom_sister_snooping_requirement():
        if not day%7 == 5 and mc.is_home and not lily.is_employee and lily.is_available and mom.is_available: # not on saturday mornings
            if mom.has_queued_event("sleeping_walk_in_label") or lily.has_queued_event("sleeping_walk_in_label"):
                return False
            return True
        return False

    def mom_sister_snooping_initialization(self):
        # No Init code for this yet.
        return

    mom_sister_snooping_action = ActionMod("Snooping on Mom and Lily", mom_sister_snooping_requirement,"mom_sister_snooping_action_label", initialization = mom_sister_snooping_initialization,
        menu_tooltip = "You overhear something from the hallway.", category="Home", is_crisis = True, is_morning_crisis = True)


label mom_sister_snooping_action_label():
    "You wake up. You're a little groggy, but you manage to get out of bed."
    "You grab yourself some clothes and quietly leave your room. You aren't sure if you are the first one awake or not."
    "However, as you walk by [lily.possessive_title]'s room, you hear her talking to [mom.title] inside. Her door is cracked so you take a quick peek."
    # show lily her bedroom
    $ lily_bedroom.show_background()
    $ scene_manager = Scene()
    if mom.sluttiness < 20 and lily.sluttiness < 20:
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped)
        $ scene_manager.add_actor(lily, position = "sitting")
        "[lily.title] is sitting on her bed while [mom.possessive_title] talks with her."
        "It seems like they are having a pretty lively conversation."
        $ overhear_topic = lily.get_random_opinion(include_sexy = False)
        $ text_one = person_opinion_to_string(lily, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        lily "... but yeah, I'm not sure he realizes I [text_one] [text_two]."
        if lily.discover_opinion(overhear_topic):
            "Oh! You didn't realize that [lily.title] felt that way."
        "The girls keep talking. They keep bouncing back and forth between multiple topics."
        $ overhear_topic = mom.get_random_opinion(include_sexy = False)
        $ text_one = person_opinion_to_string(mom, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        mom "... But I [text_one] [text_two], so I'm not sure what to do."
        if mom.discover_opinion(overhear_topic):
            "Wow, you didn't realize they talked about basically everything."
        "They keep talking, but you decide to keep heading to the bathroom. You wouldn't want to get caught snooping around, anyway!"
    elif mom.sluttiness < 50 and lily.sluttiness < 50 and mom.sluttiness >=20 and lily.sluttiness >= 20: #Both mid range sluttiness
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(lily, position = "sitting")
        "[lily.title] and [mom.title] are sitting on her bed while chatting."
        "It seems like they are having a pretty lively conversation."
        $ overhear_topic = mom.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(mom, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        mom "... but yeah, I'm not sure he realizes I [text_one] [text_two]."
        $ mc.change_locked_clarity(10)
        if mom.discover_opinion(overhear_topic):
            "Oh! You didn't realize that [mom.title] felt that way."
        "The girls keep talking. They keep bouncing back and forth between multiple sexual topics."
        $ overhear_topic = lily.get_random_opinion(include_sexy = True, include_normal = False)
        $ text_one = person_opinion_to_string(lily, overhear_topic)[1]
        $ text_two = get_topic_text(overhear_topic)
        lily "... But I [text_one] [text_two], so I'm not sure what to do."
        $ mc.change_locked_clarity(10)
        if lily.discover_opinion(overhear_topic):
            "Wow, you didn't realize they talked about sex in such detail with each other."
        "They keep talking, but you decide to keep heading to the bathroom. You wouldn't want to get caught snooping around, anyway!"
    elif mom.sluttiness >= 50 and lily.sluttiness >= 50 and not mc.business.event_triggers_dict.get("family_threesome", False): #Both high slut but no threesome yet
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(lily, position = "sitting")
        "[lily.title] and [mom.title] are sitting on her bed while chatting."
        mom "Nonsense honey, they look great. They're young and perky, just like you!"
        lily "You keep saying that, but I wish they were more like yours..."
        "[lily.title] reaches over and puts one of her hands on [mom.possessive_title]'s tits."
        lily "They're so full and soft."
        "Damn. What are they doing in there? Comparing assets?"
        mom "Honey, you just have to work with what you've been given. Let mama help. Show me what you're working with."
        lily "Okay mom..."
        $ scene_manager.strip_to_tits(person = lily)
        $ mc.change_locked_clarity(30)
        "Oh my... [lily.title] is topless!"
        mom "See? Any man would love to get their hands on you. You just have to learn to work with what you have."
        mom "I have to actively cover up, to keep from getting too much attention..."
        lily "Why would you do that!?! I'd kill to have your figure..."
        $ scene_manager.strip_to_tits(person = mom)
        "Now [mom.possessive_title] is taking her top off?"
        $ mc.change_locked_clarity(30)
        mom "I don't know, I just feel like they are such a distraction sometimes..."
        "[mom.title] is holding her own tits, a bit self-consciously."
        lily "Don't say that, they are so beautiful..."
        "[lily.title] reaches over and replaces [mom.possessive_title]'s hands. She hefts her tits in her hands and starts to tweak them a bit."
        lily "See? They're so heavy and soft..."
        $ mom.change_arousal(15)
        "[mom.title] reaches over and puts her hands on [lily.possessive_title] now."
        mom "Look at you though, so perky and firm..."
        "She pinches her nipples, prompting a squeal from [lily.title]."
        mom "And sensitive too!"
        $ lily.change_arousal(15)
        "You feel yourself getting hard watching [mom.title] and [lily.title] comparing their assets..."
        $ mc.change_locked_clarity(30)
        $ lily.change_slut(2)
        $ mom.change_slut(2)
        "Eventually you tear your eyes away. You don't want to get caught snooping."
    elif mc.business.event_triggers_dict.get("family_threesome", False): #You've already had a threesome
        "As you peek around her door, your cock starts to get hard at what you see."
        $ mom.arousal = 55
        $ lily.arousal = 40
        $ girl_swap_pos = False
        $ mom.apply_outfit(Outfit("Nude"), update_taboo = True)
        $ lily.apply_outfit(Outfit("Nude"), update_taboo = True)
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(lily, position = "sitting")
        $ Threesome_sixty_nine.update_scene(lily, mom)
        "When you peek around the corner, you see [mom.title] on top of [lily.title]. They are eating each other out."
        $ mc.change_locked_clarity(50)
        mom "Mmmm, that's it dear, lick right there!"
        $ mom.change_arousal(12)
        menu:
            "Keep watching":
                pass
            "Go on with your day":
                "You decided to let them have some fun and continue with your day."
                $ scene_manager.clear_scene()
                return

        "You accidentally let out a little gasp. It must have been audible, because [mom.possessive_title] looks up and notices you at the door."
        mom "Oh! [mom.mc_title]! Come in here honey."
        "You slowly walk in to your sister's room."
        mom "Ohh... Your sister is doing such a good job, I can hardly concentrate. Would you help me take care of her?"
        "You hear [lily.possessive_title] moan her approval of the offer while she has her face buried in [mom.title]'s cunt."
        mc.name "Sure. I'd be glad to help."
        $ mom.change_stats(obedience = 3, happiness = 5)
        mom "Oh thank you honey. I really appreciate this."
        "You quickly get undressed, your cock springing free of its confines, and step toward [lily.title] and [mom.title]."
        call start_threesome(lily, mom, start_position = Threesome_sixty_nine, position_locked = False) from _mom_sister_snooping_threesome_01
        $ scene_manager.update_actor(mom, display_transform = character_center_flipped, position = "missionary")
        $ scene_manager.update_actor(lily, display_transform = character_right, position = "missionary")
        "When you finish, [mom.possessive_title] and your sister flop down on her bed next to each other."
        lily "Thanks, [lily.mc_title]. I think I'm just gonna... go back to sleep for a little bit..."
        "As fun as it would be to join them, you decide to excuse yourself to get ready for the day."
        mc.name "No problem. You two take it easy, I'm gonna go shower."
    elif mom.sluttiness >= 20:
        $ lily.apply_university_outfit()
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(lily)
        "You peek in. You see [mom.title] sitting on [lily.possessive_title]'s bed, talking to her while she gets ready for the day."
        mom "I know, I know there's a uniform at the university, but that doesn't mean you can't express yourself a little!"
        lily "What do you mean?"
        mom "A beautiful young woman like you, maybe you could fold the top of your skirt? Show those beautiful legs of yours!"
        lily "Mom!"
        mom "Or leave a couple buttons open on your blouse?"
        lily "Stop! I don't want guys to think I'm a slut."
        "[mom.title] gives a laugh."
        mom "Honey, they won't think you're a slut. A body as young and firm as yours needs to be shown off a little!"
        mom "Sure you might get a little extra attention, but there's nothing wrong with that!"
        "[lily.title] laughs this time."
        lily "I guess it couldn't hurt to try..."
        $ lily.change_slut(2)
        $ mc.change_locked_clarity(10)
        "They keep talking, but you decide to keep heading to the bathroom. You wouldn't want to get caught snooping around, anyway!"
    elif lily.sluttiness >= 20:
        $ lily.apply_university_outfit()
        $ scene_manager.add_actor(mom, display_transform = character_center_flipped, position = "sitting")
        $ scene_manager.add_actor(lily)
        "You peek in. You see [mom.title] sitting on [lily.possessive_title]'s bed, talking to her while she gets ready for the day."
        mom "Isn't there a uniform at the university? That skirt seems a little short..."
        lily "It's fine mom. I just roll it up a little at the top, no one even notices. Well, except for this one professor... I like to sit in the front and..."
        mom "That's enough... I don't need to hear about this! Young lady unroll that skirt right now."
        lily "Mom! It's fine! There's nothing wrong with a little fun. Besides, he really enjoys it. Especially if I leave the top couple buttons open on the blouse..."
        mom "Oh my. [lily.fname], what am I gonna do with you."
        "[lily.title] gives a little laugh."
        lily "It's okay mom. Say, you should try something like this sometime!"
        mom "Why I would never..."
        lily "Didn't you say it felt like your boss was checking you out? It wouldn't hurt to get on his good side..."
        mom "I'm not gonna dress like a slut to get my boss to like me!"
        lily "I'm not saying to go to work naked! Besides, a body like yours needs to be shown off once in a while!"
        lily "Sure, you might get a little extra attention, but there's nothing wrong with that!"
        "[mom.title] gives a laugh."
        mom "I guess it couldn't hurt to try..."
        $ mom.change_slut(2)
        $ mc.change_locked_clarity(10)
        "They keep talking, but you decide to keep heading to the bathroom. You wouldn't want to get caught snooping around, anyway!"
    $ scene_manager.clear_scene()
    return
