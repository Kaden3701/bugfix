


init 2 python:
    def christina_free_time_requirement(the_person):
        return False


# Story progression actions
    def add_christina_free_time_action():
        christina_free_time_action = Action("christina tries viral marketing", christina_free_time_requirement, "christina_free_time_label")
        christina.add_unique_on_room_enter_event(christina_free_time_action)
        return



label christina_free_time_label(the_person):
    $ the_person = christina

    pass
    return
