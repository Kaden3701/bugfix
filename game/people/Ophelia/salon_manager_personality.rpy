init 720 python:
    def salon_manager_possessive_titles(person):
        valid_possessive_titles = []
        valid_possessive_titles.append(person.name)
        valid_possessive_titles.append("Your stylist")
        if person.sluttiness > 40:
            valid_possessive_titles.append("Crazy Bitch")
        if person.sluttiness > 50:
            valid_possessive_titles.append("Your intimate stylist")
        if ophelia_get_special_bj_unlocked():
            valid_possessive_titles.append("Your blowjob prodigy")
        return valid_possessive_titles

    def build_salon_manger_title_choice_menu(person):
        title_tuple = []
        title_choice = None
        for title in person.get_player_titles():
            title_tuple.append([title,title])
        return renpy.display_menu(title_tuple, True, "Choice")

    salon_manager_personality = Personality("salon_manager", default_prefix = wild_personality.default_prefix, #Based on relaxed style personality
        common_likes = ["skirts", "small talk", "the weekend", "the colour purple", "makeup", "hiking", "flirting", "high heels"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal creampies", "showing her tits", "showing her ass", "being submissive", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "supply work", "conservative outfits", "work uniforms", "pants", "boots"],
        common_sexy_dislikes = ["taking control", "bareback sex"],
        titles_function = wild_titles, possessive_titles_function = salon_manager_possessive_titles, player_titles_function = wild_player_titles)

label salon_manager_greetings(the_person):
    $ the_person.draw_person(emotion = "happy")

    if the_person.event_triggers_dict.get("introduced", 0) == 0:
        "You enter the hair salon. A beautiful young woman walks up to you and introduces herself."
        $ the_person.draw_person(position = "stand2", emotion = "happy")
        the_person "Hello there sir! Welcome to the Sweet Pixie Salon!"

        # uses parts of the in-game introduction sequence tailored to SB
        if the_person.title is None:
            mc.name "Hey, there."
            $ title_choice = the_person.get_random_title()
            $ formatted_title = the_person.create_formatted_title(title_choice)
            the_person "I am [formatted_title], top stylist and owner."
            $ the_person.set_title(title_choice)
            $ the_person.set_possessive_title(the_person.get_random_possessive_title())
            "She holds her hand out to shake yours."
            the_person "And how may I call you?"
            $ title_choice = build_salon_manger_title_choice_menu(the_person)
            mc.name "[title_choice], nice to meet you."
            $ the_person.set_mc_title(title_choice)

        the_person "I've just opened, so what can I do for you today? A wash or a trim? A shave perhaps?"
        mc.name "Nothing like that today, I own a company downtown."
        mc.name "My employees need to look perfect and I want to pay for their expenses, is that possible?"
        the_person "No problem, just give me your credit card details and I will charge it whenever you send someone by."
        "You smile at [the_person.fname] and hand over your company credit card."
        the_person "Perfect! All done."
        $ the_person.event_triggers_dict["introduced"] = 1
        $ the_person.event_triggers_dict["day_met"] = day
        $ the_person.add_unique_on_room_enter_event(ophelia_gets_dumped)
    else:
        if the_person.love < 0:
            the_person "Hi, what can I do for you?"
        elif the_person.happiness < 90:
            the_person "Hey. I hope you're having a better day than I am."
        else:
            the_person "Hey there, [the_person.mc_title]! It's good to see you!"
            if the_person.sluttiness > 60:
                "[the_person.possessive_title] smiles playfully."
                the_person "I was just thinking about you. Anything I can do for you today?"
            else:
                the_person "Is there anything I can help you with?"

    $ clear_scene()
    return
