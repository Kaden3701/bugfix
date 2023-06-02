## Strip club storyline Mod by Corrado
# You have some strippers but the business could improve: you need a manager.
# When the strip club has a BDSM room, the role will be improved as Mistress.
# The role is incompatible with: low Charisma, slave_role, having collar.

init 5 python:

    def manager_role_status_acquisition(person):
        if person.has_role(slave_role):
            slave_release_slave(person)
            # restore partial stat loss from removing slave
            person.change_stats(happiness = 10, love = 10, obedience = 20, add_to_log = False)

        person.update_opinion_with_score("taking control", 2, add_to_log = False)
        if not person in unique_character_list and not person.personality == alpha_personality:
            change_personality(alpha_personality)
        return

    def has_manager_role_requirement(person):
        if person.has_role(stripclub_manager_role):
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            return True
        return False

    def allow_promote_to_mistress_requirement(person):
        if person.has_role(stripclub_manager_role) and bdsm_room_available() and not strip_club_get_mistress():
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            if day - the_person.event_triggers_dict.get("stripclub_last_promotion_day", -7) < 7:
                return "Too recently promoted"
            return True
        return False

    def has_mistress_role_requirement(person):
        if person.has_role(stripclub_mistress_role):
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            return True
        return False

    def mistress_hunt_for_me_requirement(person):
        if person.has_role(stripclub_mistress_role):
            if not person.is_at_work:
                return False
            if not mc.location in [strip_club, bdsm_room]:
                return "Only in [strip_club.formal_name]"
            if person.has_taboo("condomless_sex"):
                return "Requires: had sex with " + person.name
            if person.has_taboo("sucking_cock"):
                return "Requires: blowjob from " + person.name
            if person.get_opinion_score("threesomes") <= -2:
                return "Requires: threesome experience " + person.name
            minimum_sluttiness = THREESOME_BASE_SLUT_REQ + (person.get_opinion_score("threesomes") * -5)
            if person.effective_sluttiness() < minimum_sluttiness:
                return "Requires: " + str(minimum_sluttiness) + " Sluttiness"
            return True
        return False

    def mistress_hunt_for_me_prey(person):
        # first find a non-employee target
        target = get_random_from_list([x for x in known_people_at_location(mc.location, [person]) if not x.is_strip_club_employee])
        if target:
            return target

        # alternative find an employee target
        return get_random_from_list([x for x in known_people_at_location(mc.location, [person]) if willing_to_threesome(person, x)])

    def promote_strip_club_stripper_to_manager(person):
        if person.love <= 0:
            person.love = 5
        person.change_stats(happiness = 10, obedience = 5, love = 5)
        person.change_job(stripclub_manager_job, job_known = True)
        person.stripper_salary = __builtin__.round(person.stripper_salary * 1.1, 1)

        manager_role_status_acquisition(person)

        add_strip_club_manager_hire_more_stripper_reminder_action()
        add_strip_club_manager_waitresses_suggestion_action()
        add_strip_club_manager_bdsm_room_suggestion_action()
        return

    def promote_strip_club_manager_to_mistress(person):
        person.change_job(stripclub_mistress_job, job_known = True)
        person.stripper_salary = __builtin__.round(person.stripper_salary * 1.1, 1)
        return

    manager_role_remove_action = Action("Remove as Manager", has_manager_role_requirement, "manager_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club manager.")
    promote_to_mistress_action = Action("Promote to Mistress", allow_promote_to_mistress_requirement, "promote_to_mistress_label", menu_tooltip = "Promote [the_person.title] as strip club mistress.")
    mistress_role_remove_action = Action("Remove as Mistress", has_mistress_role_requirement, "mistress_role_remove_label", menu_tooltip = "Remove [the_person.title] as strip club mistress.")
    mistress_hunt_for_me_action = Action("Hunt for me", mistress_hunt_for_me_requirement, "mistress_hunt_for_me_label", menu_tooltip = "Ask [the_person.title] to find you a girl for a threesome.")

    stripclub_manager_role = Role("Manager", [manager_role_remove_action, promote_to_mistress_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)
    stripclub_mistress_role = Role("Mistress", [mistress_role_remove_action, mistress_hunt_for_me_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)

label promote_to_manager_label(the_person):
    $ the_person.event_triggers_dict["stripclub_last_promotion_day"] = day
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "Maybe. Since I bought this place, I've been turning a profit, but I think business could be better."
    mc.name "Managing the girls' shifts, dealing with suppliers, and keeping an eye on everything here is going to take time, and I'm already pretty busy with other things."
    mc.name "So I wanna ask you, do you think you can manage this place? Are you the girl I'm looking for?"
    the_person "[mc.name], with the previous owner this place was a real mess, and I've seen the changes and the improvement you made."
    the_person "The place is clean, the girls are happy, and I don't see those shady figures hanging around here anymore."
    the_person "I get what you're doing here, and I think I see what you are trying to do."
    mc.name "Okay, [the_person.title], I will let you run the place. Prove to me that I made the right choice."
    "She looks intensely into your eyes. You see in her own eyes the glimmer of excitement for being chosen."
    the_person "I will."
    $ promote_strip_club_stripper_to_manager(the_person)
    return

label manager_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I'm still keeping you with me here, just as a stripper."
    $ the_person.change_stats(happiness = -10, obedience = 2)
    # this might increase the number of active strippers to 6
    $ the_person.change_job(stripclub_stripper_job, job_known = True)
    return

label promote_to_mistress_label(the_person):
    $ the_person.event_triggers_dict["stripclub_last_promotion_day"] = day
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I think someone should manage the BDSM room..."
    the_person "Wow, it would be a kinky job that one! Wait, are you planning to get some other man instead of you to do it?"
    $ the_person.draw_person(emotion = "sad")
    the_person "Because I don't know if I can accept someone else instead of you giving me orders, even if it is you asking me that..."
    the_person "You have been my 'first'... Well, not in the physical way, but you know what I mean, and I think you're the only one I can accept."
    mc.name "Actually, I was planning to have a woman doing the job."
    $ the_person.draw_person(emotion = "angry")
    the_person "What? No way! I will never agree to allow another woman to command me. If you do that, I will be forced to resign!"
    mc.name "And what if that commanding woman is you?"
    $ the_person.draw_person(emotion = "happy")
    the_person "Really? Are you asking me to be, after you, the ultimate authority here?"
    mc.name "I know it's a dirty job, but someone needs to do it."
    "A malicious smile creeps over her face, while she glances over to the other girls."
    the_person "I will do my best... or worst, depending on my mood."
    $ promote_strip_club_manager_to_mistress(the_person)
    return

label mistress_role_remove_label(the_person):
    mc.name "[the_person.title], I need to talk with you."
    the_person "Sure [the_person.mc_title], something I can help you with?"
    mc.name "I checked your management results and I can't say I'm happy, so I have decided to remove you from your management position."
    $ the_person.draw_person(emotion = "sad")
    the_person "I understand [the_person.mc_title], I can assure you I did my best..."
    mc.name "I know, that's why I'll keep you with me here, just as a stripper."
    $ the_person.change_job(stripclub_stripper_job, job_known = True)
    return

label mistress_hunt_for_me_label(the_person):
    $ scene_manager = Scene()
    mc.name "Do you think you can find a girl here to have some fun with?"
    the_person "Oh, 'that' kind of fun, [the_person.mc_title]? Sure, let me see..."
    $ scene_manager.add_actor(the_person, position = "walking_away")
    "She starts scanning the room, looking for a new victim."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "I think I've found what we're looking for, let me work my magic."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "She arranges her clothes and starts moving closer to her prey..."
    $ the_person_two = mistress_hunt_for_me_prey(the_person)
    $ scene_manager.hide_actor(the_person)
    if the_person_two is None:
        $ scene_manager.show_actor(the_person, position = "stand3", emotion = "sad")
        the_person "Amazing, she's not interested and I cannot find anyone else... Am I losing my touch?"
        return
    "After a couple of minutes the girls are back."
    $ scene_manager.show_actor(the_person, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(the_person_two, display_transform = character_center_flipped, position = "stand2", emotion = "happy")
    the_person "I told her we have something nice planned for her, [the_person.mc_title]..."
    mc.name "Good choice [the_person.title]! So [the_person_two.title], would you like to join us?"
    the_person_two "It would be my pleasure [the_person.mc_title]!" # Only known people answer this tnx to the high obedience required
    mc.name "Ok, let's find a more appropriate place, follow me girls!"
    $ mc.change_location(downtown_hotel)
    $ clear_scene()
    "A couple of minutes later, you are in the hotel. You walk up to the reception desk to get a hotel room for one night."
    $ mc.business.change_funds(-80)
    $ downtown_hotel_room.show_background()

    $ scene_manager.update_actor(the_person, position = "back_peek")
    $ scene_manager.update_actor(the_person_two, position = "walking_away")
    "You open the door of the room and motion the girls to come in. You notice [the_person.title] already grabbing [the_person_two.title]'s ass."
    if not the_person.vagina_available:
        "[the_person_two.possessive_title] starts moving some of your mistress's clothing to get access to her [the_person.pubes_description] pussy."
        $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "back_peek")
    if not the_person_two.vagina_available:
        "Your mistress is eager to get access to [the_person_two.possessive_title]'s pussy."
        $ the_person_two.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "walking_away")
    call start_threesome(the_person, the_person_two, girl_in_charge = the_person, start_object = make_bed(), affair_ask_after = False) from _call_start_threesome_mistress_hunt_for_me_label
    "Once you've all had your fun, you and the girls go back to the Strip Club."
    $ scene_manager.clear_scene()
    $ mc.change_location(strip_club)
    return
