# TODO: Encourage players to unlock the "Follow Me" command to bring people to the Dungeon for situational bonuses from the objects in the Room.
#       Balance how much of a bonus the objects give. Right now it's a sluttiness_modifier = 10, obedience_modifier = 20 for the lowest tier, "the_bdsmbed" which is +10 obedience from a normal bed.
# NOTE: Strip action is now in generic_people_role
init 10 python:
    def dungeon_room_appoint_slave_requirement():
        if mc.location.people:
            return True
        return "Requires: Person in Room"

    dungeon_room_appoint_slave_action = Action("Appoint a slave", dungeon_room_appoint_slave_requirement, "dungeon_room_appoint_slave_label", menu_tooltip = "Assigns the person a role as a slave. Use the \"Follow Me\" Action on a person to bring them to the Dungeon.")

label dungeon_room_appoint_slave_label():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_at_location(mc.location), "Turn into slave", "Back")]
        ))

    if isinstance(_return, Person):
        $ the_person = _return
        if the_person.personality == alpha_personality:
            "This girl has an Alpha personality and will never submit into becoming your slave. You could turn her into a bimbo, that would remove her Alpha personality."
        else:
            call dungeon_room_appoint_slave_label_2(the_person) from dungeon_room_appoint_slave_label_1
    return # Where to go if you hit "Back"

label dungeon_room_appoint_slave_label_2(the_person):
    if not the_person.has_role(slave_role): # What happens when you try to appoint them
        if the_person.obedience >= 130 and the_person.get_opinion_score("being submissive") > 0:
            "[the_person.possessive_title] seems to be into the idea of serving you."
            $ the_person.call_dialogue("sex_obedience_accept")
        elif the_person.get_opinion_score("being submissive") <= 0 and the_person.obedience >= 160:
            "[the_person.possessive_title] is willing to serve you as her master."
            $ the_person.call_dialogue("sex_obedience_accept")
        else:
            "[the_person.possessive_title] needs to be more obedient before being willing to commit to being your slave."
            return

        $ the_person.unlock_spanking()
        $ the_person.add_role(slave_role)

        "[the_person.title] is now a willing slave of yours."


    else: # What happens when they are already appointed
        "Releasing has a high impact on the girls stats, are you sure?"
        menu:
            "Release her":
                $ slave_release_slave(the_person)
                $ del the_person.event_triggers_dict["unique_sex_positions"]
                "You release [the_person.possessive_title] from their duties as a slave."
            "Never mind":
                pass

    return
