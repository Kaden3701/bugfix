

init 2 python:
    def alexia_first_stream_requirement(the_person):
        return False


# Story progression actions
    def add_alexia_first_stream_action():
        alexia_first_stream_action = Action("Alexia wants to stream", alexia_first_stream_requirement, "alexia_first_stream_label")
        alexia.add_unique_on_room_enter_event(alexia_first_stream_action)
        return



label alexia_first_stream_label(the_person):

    pass
    return
