init 2 python:
    def mall_flirt_requirement():
        if mc.location in mall_hub:
            return __builtin__.len(known_people_at_location(mc.location, unique_character_list)) > 0
        return False

    def mall_flirt_get_known_person():
        return get_random_from_list(known_people_at_location(mc.location, unique_character_list))

    mall_flirt_action = ActionMod("Mall Flirt", mall_flirt_requirement, "mall_flirt_event",
        menu_tooltip = "You have a short flirt with someone in the mall.", category = "Mall", is_crisis = True, is_fast = True)

label mall_flirt_event():
    $ the_person = mall_flirt_get_known_person()
    if the_person is None:
        return

    $ the_person.draw_person()
    the_person "Oh, hey [the_person.mc_title]!"
    mc.name "Hello, [the_person.title]. How are you doing today?"
    "[the_person.possessive_title] smiles and bats her eyelashes a few times."
    the_person "Well, to be honest, it is much better now that you are here!"
    menu:
        "Looking good girl!":
            the_person "Aww, thanks! You're looking pretty sexy yourself..."
            "[the_person.possessive_title] looks you up and down a few times. Her eyes tend to linger on your crotch each time they pass."
            $ the_person.change_slut(2)
            "You flirt back and forth with [the_person.possessive_title], but soon it is time to part ways."
            the_person "It was great seeing you! Take care [the_person.mc_title]!"
        "Thank you":
            "You make some small talk with [the_person.possessive_title]. You catch up on a few various things, but soon it is time to part ways."
            the_person "It was great seeing you! Take care [the_person.mc_title]!"
            $ the_person.change_happiness(5)

    $ clear_scene()
    return
