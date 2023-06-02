init 3 python:
    def downtown_bar_drink_requirement(): # Leave this in
        return True

    # actions available from entry point action
    downtown_bar_drink_action = Action("Order a drink for... {image=gui/heart/Time_Advance.png}", downtown_bar_drink_requirement, "downtown_bar_drink_label", menu_tooltip = "Treat someone with a drink...")

label downtown_bar_drink_label():
    $ new_person = make_person(force_random = True)

    "[downtown_bar.formal_name] is Under Construction - Placeholder Action (Probably will be removed)" # A way to generate new people.

    if not mc.location.people: # No one is in the bar so we create a person.
        "The [downtown_bar.formal_name] is a desolate place to be..."

        $ new_person.draw_person()
        "Having seated yourself by the counter with no bartender in sight you hear the entry door open up as a woman walks in."


        $ new_person.draw_person(position = "sitting")
        "She seats herself in the lounge area, seemingly puzzled by the lack of attendance at the only bar in town."
        "She sits quietly minding her own business..."

        "Do you wish to introduce yourself, perhaps grace her with a free- of charge drink?"

    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_at_location(mc.location) + unknown_people_at_location(mc.location) + [new_person], "Drink with", "Back")]
        ))

    if not isinstance(_return, Person):
        if new_person.mc_title == "Stranger": # If the player had no interest in interacting with the character we remove it from the game. Assuming a proper "Back" button gets added during first time introduction we can do more with this.
            "Not seeing any reason to stick around she promptly leaves, never to be seen again."

        python: # release variables
            new_person.remove_person_from_game()
            clear_scene()
            del new_person

        return # Where to go if you hit "Back".
    else:
        $ the_person = _return
        $ del new_person

    # add person to game
    python:
        if not the_person in mc.location.people:
            the_person.generate_home()
            mc.location.add_person(the_person)

    $ the_person.draw_person()

    if the_person.is_stranger: # First time introduction that does not return to talk_person
        call person_introduction(the_person) from _call_person_introduction_downtown_bar_drink

    "Since there's no bartender in town you grab a glass of the finest tap water and treat [the_person.title] to a once- in a lifetime experience."
    $ the_person.change_stats(love = 2, happiness = 2)

    the_person.title "Oh, wow. I literally cannot live without water, this is great. Thanks, [the_person.mc_title]!"

    mc.name "Stay healthy and hydrated, [the_person.title]."


    if time_of_day == 4:
        "After a night of drinks you decide to head back home to bed."
        $ mc.change_location(bedroom)

    call advance_time from downtown_bar_drink_1

    $ clear_scene()
    return
