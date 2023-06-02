


init 2 python:
    def christina_council_influence_intro_requirement(the_person):
        return False


# Story progression actions
    def add_christina_council_influence_intro_action():
        christina_council_influence_intro_action = Action("christina tries viral marketing", christina_council_influence_intro_requirement, "christina_council_influence_intro_label")
        christina.add_unique_on_room_enter_event(christina_council_influence_intro_action)
        return



label christina_council_influence_intro_label(the_person):
    $ the_person = mom

    pass
    return
