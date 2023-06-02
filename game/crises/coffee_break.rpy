## Coffee Break Crisis Mod by Tristimdorion
init 2 python:
    def coffee_break_requirement():
        if mc.is_at_work: # only during morning afternoon or evening
            if mc.business.is_open_for_business:
                return __builtin__.len([x for x in mc.business.employee_list if x.effective_sluttiness() > 20]) >= 3
            if mc.business.is_open_for_internship:
                return __builtin__.len([x for x in mc.business.intern_list if x.effective_sluttiness() > 20]) >= 3
        return False

    coffee_break_action = ActionMod("Coffee Break", coffee_break_requirement, "coffee_break_action_label",
        menu_tooltip = "A group of employees is having a coffee break.", category = "Business", is_crisis = True)

label coffee_break_action_label():
    if mc.business.is_open_for_business:
        $ word = "employee"
        if __builtin__.len([x for x in mc.business.employee_list if x.effective_sluttiness() > 60]) >= 2:
            $ (person_two, person_three) = get_random_employees(2, slut_required = 61)
        elif __builtin__.len([x for x in mc.business.employee_list if x.effective_sluttiness() > 40]) >= 2:
            $ (person_two, person_three) = get_random_employees(2, slut_required = 41)
        else:
            $ (person_two, person_three) = get_random_employees(2, slut_required = 20)
        $ person_one = get_random_employees(1, exclude_list = [person_two, person_three], slut_required = 20)
    else:
        $ word = "intern"
        if __builtin__.len([x for x in mc.business.intern_list if x.effective_sluttiness() > 60]) >= 2:
            $ (person_two, person_three) = get_random_interns(2, slut_required = 61)
        elif __builtin__.len([x for x in mc.business.intern_list if x.effective_sluttiness() > 40]) >= 2:
            $ (person_two, person_three) = get_random_interns(2, slut_required = 41)
        else:
            $ (person_two, person_three) = get_random_interns(2, slut_required = 20)
        $ person_one = get_random_interns(1, exclude_list = [person_two, person_three], slut_required = 20)
    if not (isinstance(person_one, Person) and isinstance(person_two, Person) and isinstance(person_three, Person)):
        return


    $ mc.change_location(lobby)
    "As you are walking around the office, you see several [word]s at the coffee machine. They haven't noticed you, but you can hear what they are saying."
    call coffee_break_chit_chat_label(person_one, person_two, person_three) from _call_coffee_break_chit_chat_label_1
    python:     # Release variables
        del person_one
        del person_two
        del person_three
        del word
    return

label coffee_break_chit_chat_label(person_one, person_two, person_three):
    python:
        scene_manager = Scene()
        scene_manager.add_actor(person_one, emotion="default", display_transform = character_left_flipped)
        scene_manager.add_actor(person_two, emotion="default", display_transform = character_center_flipped)
        scene_manager.add_actor(person_three, emotion="default")

    if person_two.sluttiness > 70 and person_three.sluttiness > 70:
        person_one "Last night, I was dreaming of sucking [person_one.mc_title]'s big cock."
        person_two "I wouldn't mind giving that meat stick some affection myself."
        person_three "That would be perfect, when you two are done, I can tame and ride that monster."
    elif person_two.sluttiness > 40 and person_three.sluttiness > 40:
        person_one "Don't you think [person_one.mc_title] has a nice bulge in his pants."
        person_two "I bet that he is hung like a horse."
        person_three "I've always wanted to take some horse riding lessons."
    else:
        person_one "Don't you think [person_one.mc_title] is really good looking."
        person_two "I like how his butt flexes in his pants."
        person_three "To be honest, I much more prefer the other side."

    python:
        scene_manager.update_actor(person_one, emotion="happy")
        scene_manager.update_actor(person_two, emotion="happy")
        scene_manager.update_actor(person_three, emotion="happy")

    "The girls start laughing at [person_three.title]'s last remark."

    if not perk_system.has_ability_perk("Situational Awareness"):
        "You quickly check out the three girls as they chit chat. You suddenly realize how hot all three of them are."
        "You're building your own company, staffing it with beautiful women you hand select. You realize how unaware you are sometimes of how lucky you are."
        "You make a quick mental note to take better notice of the girls around you, and to enjoy their physical attractiveness."
        $ situational_awareness_perk_unlock()
        "You have unlocked the Situational Awareness perk! You now gain lust every turn based on the outfits of girls in the same room."
        "The girls resume their banter."

    person_one "That was very funny [person_three.name], but I have to get back to work."

    $ scene_manager.update_actor(person_one, position = "walking_away")

    "[person_one.title] walks off to her workstation."
    # remove person 1 from scene
    $ scene_manager.remove_actor(person_one)

    if person_two.sluttiness > 40 and person_three.sluttiness > 40:
        person_two "Oh, she's such a stickler for rules."
        person_three "Why don't we go break some rules together in the supply closet?"

        if person_two.sluttiness > 60 and person_three.sluttiness > 60:
            $ scene_manager.update_actor(person_two, position = "walking_away")
            $ scene_manager.update_actor(person_three, position = "walking_away")

            "You decide to follow them at a discrete distance."
            "As soon as they enter the supply closet you peek through the side window where [person_two.possessive_title] starts kissing [person_three.possessive_title]."

            $ scene_manager.update_actor(person_two, position = "kissing")
            $ scene_manager.update_actor(person_three, position = "kissing")
            $ mc.change_locked_clarity(20)

            "What's your next move?"
            menu:
                "Walk away":
                    pass

                "Join them\n{color=#ff0000}{size=18}Requires: Both girls open to threesomes{/size}{/color} (disabled)" if not willing_to_threesome(person_two, person_three):
                    pass

                "Join them" if willing_to_threesome(person_two, person_three):
                    mc.name "Hello girls... mind if I join your little party?"
                    $ scene_manager.update_actor(person_two, position = "stand3")
                    $ scene_manager.update_actor(person_three, position = "stand4")
                    person_three "Oh my, hello [person_three.mc_title], we didn't see you there."
                    "You tell the girls to take off their clothes."

                    $ scene_manager.strip_full_outfit()

                    call start_threesome(person_two, person_three) from _call_coffee_break_threesome_test_3

                    person_two "Wow... this was... really good actually... You can join us anytime you want boss..."
                    $ scene_manager.update_actor(person_two, position = "walking_away", display_transform = character_center_flipped)
                    $ scene_manager.update_actor(person_three, position = "walking_away", display_transform = character_right)
                    "They pick up their clothes and leave you feeling very proud of yourself."

                    # cleanup scene
                    $ scene_manager.clear_scene()
                    $ person_two.increase_opinion_score("threesomes")
                    $ person_two.reset_arousal()
                    $ person_two.apply_planned_outfit()

                    $ person_three.increase_opinion_score("threesomes")
                    $ person_three.reset_arousal()
                    $ person_three.apply_planned_outfit()

                    $ town_relationships.improve_relationship(person_two, person_three)

                    "Amazing you just fucked two of your [word]s, and are left wondering if other girls in your company might also be up for this."

                "Punish them for inappropriate behaviour" if office_punishment.is_active and mc.business.is_open_for_business:
                    mc.name "[person_three.title], [person_two.title], this is completely inappropriate, even if you're on your break."
                    mc.name "I don't have any choice but to record this for disciplinary action later."
                    $ person_three.add_infraction(Infraction.inappropriate_behaviour_factory())
                    $ person_two.add_infraction(Infraction.inappropriate_behaviour_factory())
                    $ scene_manager.update_actor(person_three, emotion = "sad")
                    person_three "Really? I..."
                    $ scene_manager.update_actor(person_two, emotion = "sad")
                    person_two "Don't get us in any more trouble [person_three.title]. Sorry [person_two.mc_title], we'll get back to work right away."
                    person_three "Ugh, whatever. Come on [person_two.title], let's go."
                    $ scene_manager.update_actor(person_three, position = "walking_away")
                    $ scene_manager.update_actor(person_two, position = "walking_away")

                    "They quickly leave the supply closet together."

        else:
            person_two "Another time, [person_three.name], let's get back to work."

            $ scene_manager.update_actor(person_two, position = "walking_away")
            $ scene_manager.update_actor(person_three, position = "walking_away")

            $ town_relationships.improve_relationship(person_two, person_three)

            "[person_two.title] grabs [person_three.title] by her arm and they walk down the corridor."
    else:
        person_two "Yeah, we better get going too."
        $ scene_manager.update_actor(person_two, position = "walking_away")
        $ scene_manager.update_actor(person_three, position = "walking_away")

        $ town_relationships.improve_relationship(person_two, person_three)

        "You watch [person_two.title] and [person_three.title] walk away together."

    # clear scene
    $ scene_manager.clear_scene()
    return
