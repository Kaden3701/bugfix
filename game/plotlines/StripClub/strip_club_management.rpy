## Stripclub storyline Mod by Corrado
# You have some strippers but the business could improve.
init 3 python:
    def bdsm_room_available():
        return mc.business.event_triggers_dict.get("strip_club_has_bdsm_room", False)

    def strip_club_manager_bdsm_room_build_requirement():
        if not mc.business.has_funds(10000):
            return False
        if bdsm_room_available():
            return False
        if not mc.business.is_open_for_business:
            return "Only during business hours"
        if strip_club_get_manager():
            return True
        return False

    # extend the default build phone menu function with renovations
    def build_phone_menu_build_bdsm_room_extended(org_func):
        def phone_menu_wrapper():
            # run original function
            phone_menu = org_func()
            if mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", None) == 0: # only show option when we haven't started construction
                strip_club_manager_bdsm_room_build_action = Action("Build a BDSM room\n{color=#ff0000}{size=18}Costs: $10,000{/size}{/color}", strip_club_manager_bdsm_room_build_requirement, "strip_club_manager_bdsm_room_build_label")
                phone_menu[2].insert(1, strip_club_manager_bdsm_room_build_action)

            return phone_menu

        return phone_menu_wrapper

    build_phone_menu = build_phone_menu_build_bdsm_room_extended(build_phone_menu)


init 3 python:
    def strip_club_get_manager():
        managers = people_in_role(stripclub_manager_role)
        if __builtin__.len(managers) > 0:
            return managers[0]
        return None

    def strip_club_get_mistress():
        mistresses = people_in_role(stripclub_mistress_role)
        if __builtin__.len(mistresses) > 0:
            return mistresses[0]
        return None

    def strip_club_manager_reminder_requirement():
        if day >= (get_strip_club_foreclosed_last_action_day() + 7): # the event start to trigger after 7 days MC bought the club.
            if get_strip_club_foreclosed_stage() == 5 and not strip_club_get_manager(): # the event only trigger if there's no Manager yet
                if day % 5 == 0 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (toughts)
                    return True
        return False

    def add_strip_club_manager_reminder_action():
        if not strip_club_get_manager():
            strip_club_manager_reminder_action = Action("A simple reminder to appoint someone as strip club manager", strip_club_manager_reminder_requirement, "strip_club_manager_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_reminder_action)

    def strip_club_manager_hire_more_stripper_reminder_requirement():
        if __builtin__.len(stripclub_strippers) < 7: # the event only trigger if there's not the max nr. of strippers (5 + 1 manager)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 0 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_hire_more_stripper_reminder_action():
        if __builtin__.len(stripclub_strippers) < 7:
            strip_club_manager_hire_more_stripper_reminder_action = Action("A simple reminder from the strip club manager to hire more stripper", strip_club_manager_hire_more_stripper_reminder_requirement, "strip_club_manager_hire_more_stripper_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_hire_more_stripper_reminder_action)

    def strip_club_manager_waitresses_suggestion_requirement():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_waitresses_suggestion_action():
        if __builtin__.len(stripclub_waitresses) < 2:
            strip_club_manager_waitresses_suggestion_action = Action("Your strip club manager suggests you hire a couple of waitresses.", strip_club_manager_waitresses_suggestion_requirement, "strip_club_manager_waitresses_suggestion_label")
            mc.business.add_mandatory_crisis(strip_club_manager_waitresses_suggestion_action)

    def strip_club_manager_hire_more_waitresses_reminder_requirement():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_hire_more_waitresses_reminder_action():
        if __builtin__.len(stripclub_waitresses) < 2: # the event only trigger if there's not the max nr. of waitresses (2)
            strip_club_manager_hire_more_waitresses_reminder_action = Action("A simple reminder from the strip club manager to hire more waitresses", strip_club_manager_hire_more_waitresses_reminder_requirement, "strip_club_manager_hire_more_waitresses_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_hire_more_waitresses_reminder_action)

    def strip_club_manager_bdsm_room_suggestion_requirement():
        if not bdsm_room_available():
            if day >= (get_strip_club_foreclosed_last_action_day() + 15): # the event trigger after 15 days you have a manager
                if not mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day", None): # Not suggested yet
                    if __builtin__.len(stripclub_waitresses) > 0 and strip_club_get_manager():
                        if not mc.location is strip_club and time_of_day == 3:
                            return True
        return False

    def add_strip_club_manager_bdsm_room_suggestion_action():
        if not bdsm_room_available():
            strip_club_manager_bdsm_room_suggestion_action = Action("Your strip club manager suggests you build a new BDSM room.", strip_club_manager_bdsm_room_suggestion_requirement, "strip_club_manager_bdsm_room_suggestion_label")
            mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_suggestion_action)

    def strip_club_manager_bdsm_room_reminder_requirement():
        if not bdsm_room_available() and mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day") == 0: # the event only trigger if the bdsm_room isn't started yet
            if strip_club_get_manager(): # the event only trigger if there's a Manager
                if day % 5 == 2 and time_of_day == 2: # the event trigger every 5 days in the afternoon. (phone call)
                    return True
        return False

    def add_strip_club_manager_bdsm_room_reminder_action():
        if not bdsm_room_available():
            strip_club_manager_bdsm_room_reminder_action = Action("A simple reminder from the strip club manager to build a BDSM room.", strip_club_manager_bdsm_room_reminder_requirement, "strip_club_manager_bdsm_room_reminder_label")
            mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_reminder_action)


    def strip_club_manager_bdsm_room_built_requirement():
        if day >= (mc.business.event_triggers_dict.get("strip_club_bdsm_decision_day") + 5):
            if mc.business.is_open_for_business: # only during work hours
                return True
        return False

    def add_strip_club_manager_bdsm_room_built_event():
        strip_club_manager_bdsm_room_built_event = Action("Your new BDSM room has been built.", strip_club_manager_bdsm_room_built_requirement, "strip_club_manager_bdsm_room_built_label")
        mc.business.add_mandatory_crisis(strip_club_manager_bdsm_room_built_event)

    def strip_club_switch_rooms_requirement():
        return bdsm_room_available()

    strip_club_switch_rooms_action = Action("Switch rooms", strip_club_switch_rooms_requirement, "strip_club_switch_rooms_label", menu_tooltip = "Switch between Stripclub and BDSM rooms.")


label strip_club_manager_reminder_label():
    "A few days have passed since you bought the strip club, and after running the numbers, you realize that business could be better."
    "But you can't spend all your time there micro-managing everything, you need to find someone to do it for you."
    "Someone obedient to you, but also strong enough to manage the other girls, the customers and the suppliers... Perhaps one of the strippers?"
    return

label strip_club_manager_hire_more_stripper_reminder_label(): # phone call
    if __builtin__.len(stripclub_strippers) >= 7:
        return
    $ the_person = strip_club_get_manager()
    if mc.location == strip_club and the_person.location == strip_club:
        $ the_person.draw_person()
    else:
        "Suddenly your phone rings, it's your strip club manager."
    the_person "Hello [the_person.mc_title], I just wanted to remind you that we can have seven girls here, performing on the stage."
    the_person "A full roster would make setting up the shifts easier and, of course, it would be more profitable for you."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person "Okay [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_hire_more_waitresses_reminder_label(): # phone call
    if __builtin__.len(stripclub_waitresses) >= 2:
        return
    $ the_person = strip_club_get_manager()
    if mc.location == strip_club and the_person.location == strip_club:
        $ the_person.draw_person()
    else:
        "Your phone rings. It's your strip club manager."
    the_person "Hello [the_person.mc_title], I just wanted to remind you that we need two waitresses, we can't have our strippers do that."
    mc.name "Thank you [the_person.title]... I know, I'll find someone, I promise!"
    the_person "Okay [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_waitresses_suggestion_label(): # (personal contact)
    "Your smartphone rings. It's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person "Hi [the_person.mc_title]! Can you join me here at the Club ? I need to talk with you."
    mc.name "Sure [the_person.title], I'm coming."
    $ mc.change_location(strip_club)
    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Here I am [the_person.title], how are things going here?"
    the_person "That's exactly what I wanna talk to you about: you spent a lot of money to buy this place, don't you wanna make it more profitable?"
    mc.name "Of course I do: what do you have in mind?"
    the_person "A lot of customers here get a drink at the bar, then sit by the stage to watch the girls stripping, right?"
    mc.name "Yes, that's how the business here works."
    the_person "Exactly! After they get their drink, most customers don't want to leave the stage. Only a few come back to the bar to get another drink."
    mc.name "I think I get where you're going with this..."
    the_person "Yeah! What if we had a couple of waitresses serving the drinks directly at the customer's seat, and maybe some peanuts or some chips..."
    the_person "With the salty snacks keeping them thirsty and the waitresses letting them stay in their seats, we'd sell a lot more drinks by the end of the day."
    mc.name "Thank you [the_person.title], that's really a good idea! I'll look into hiring some waitresses as soon as possible."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "[the_person.title] smiles back to you, proud to have proven herself worthy."
    $ add_strip_club_manager_hire_more_waitresses_reminder_action()
    return

label strip_club_manager_bdsm_room_suggestion_label(): # (personal contact)
    "Your smartphone rings. It's your strip club manager."
    $ the_person = strip_club_get_manager()
    the_person "Hi [the_person.mc_title]! Can you join me here at the club? I need to talk with you."
    mc.name "Sure [the_person.title], I'll be right over."
    $ mc.change_location(strip_club)
    $ the_person.draw_person(emotion = "happy", position = "stand3")
    mc.name "Okay, here I am [the_person.title], how things are going here?"
    the_person "That's exactly what I wanna talk to you about, I have an idea to make the business here more profitable."
    mc.name "You have my attention, what do you have in mind?"
    the_person "This place has a lot of unused space around the back... What if we make another room there for a different kind of shows?"
    mc.name "'Different shows'? You know that this is a strip club, right, and not a brothel?"
    the_person "No no no, [the_person.mc_title], nothing like that! I did some research, and I found that in other cities you can find places that offer BDSM shows."
    the_person "But here, in our city, there's nothing like it... yet!"
    mc.name "What do you mean by 'BDSM shows'?"
    the_person "Well, you know there are girls who like to submit themselves completely to their partners during sex, right?"
    "Your mind wanders off for a bit, of course you know, you know very well!"
    the_person "And you know that almost every girl, more or less, likes to show herself off, right?"
    "You don't even try to hide your smile, you know that too..."
    the_person "So, in a BDSM show girls submit themselves completely to their partners in a public place like this, showing off their obedience and devotion to their Master."
    mc.name "But you know [the_person.title], we can't have guys on the stage, fucking around with girls... we would get into some serious trouble!"
    the_person "Whoever said anything about men performing on stage?"
    "She winks mischievously at you, now it's clear what kind of picture is floating in her vicious mind..."
    mc.name "I get the picture. I admit it could be a very good idea, but I need to double-check with my lawyer to see if it is feasible."
    the_person "I made a business prospect for you with costs and revenues, I will send it to your phone."
    mc.name "Thank you, [the_person.title], I'll look at it."
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    "As you glance over the documents, you quickly realize that the $10,000 investment could be very, very profitable."

    $ add_strip_club_manager_bdsm_room_reminder_action()
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = 0
    return

label strip_club_manager_bdsm_room_build_label(): # (action button)
    "You pick up the phone and call your usual contractor."
    mc.name "Hello, this is [mc.name] [mc.last_name] from [strip_club.formal_name], I need some construction work done here at my club."
    "You go over the details and agree on a price of $10,000 for converting some unused space into a fully equipped and soundproofed BDSM room."
    $ mc.business.change_funds(-10000)
    $ add_strip_club_manager_bdsm_room_built_event()
    $ mc.business.event_triggers_dict["strip_club_bdsm_decision_day"] = day
    return

label strip_club_manager_bdsm_room_reminder_label(): # phone call
    $ the_person = strip_club_get_manager()
    if mc.location == strip_club and the_person.location == strip_club:
        $ the_person.draw_person()
    else:
        "Your phone rings, it's your strip club manager."
    the_person "Hello [the_person.mc_title], did you check the business prospect I sent you for having a special room for BDSM shows?"
    the_person "I'm sure it would make the business here a lot more profitable, we would be the only club in the city having that kind of entertainment."
    mc.name "Thank you [the_person.title]... I know, I'll get back to you, I promise!"
    the_person "Ok [the_person.mc_title], thank you!"
    $ clear_scene()
    return

label strip_club_manager_bdsm_room_built_label(): # (time event)
    $ man_name = Person.get_random_male_name()
    "Going about your day, you get a call from your contractor."
    man_name "Hello Sir, this is [man_name] from Turner Construction. I just wanted you to know that we have finished our work."
    mc.name "Thank you [man_name], much appreciated."
    "The BDSM room at the strip club is now ready for use."
    $ strip_club.add_action(strip_club_switch_rooms_action)
    $ bdsm_room.add_action(strip_club_switch_rooms_action)
    $ add_strip_club_cage_her_action_to_mc_actions()
    $ mc.business.event_triggers_dict["strip_club_has_bdsm_room"] = True
    return

label strip_club_switch_rooms_label():
    if mc.location is strip_club:
        $ mc.change_location(bdsm_room)
    elif mc.location is bdsm_room:
        $ mc.change_location(strip_club)
    return
