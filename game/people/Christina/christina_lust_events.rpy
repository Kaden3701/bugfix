


init 2 python:
    def christina_daughter_training_requirement(the_person):
        return False


# Story progression actions
    def add_christina_daughter_training_action():
        christina_daughter_training_action = Action("Christina wants to help", christina_daughter_training_requirement, "christina_daughter_training_label")
        christina.add_unique_on_room_enter_event(christina_daughter_training_action)
        return



label christina_daughter_training_label(the_person):
    $ the_person = christina

    pass
    return
