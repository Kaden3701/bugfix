


init 2 python:
    def emily_university_lunch_requirement(the_person):
        return False


# Story progression actions
    def add_emily_university_lunch_action():
        emily_university_lunch_action = Action("Lunch Date with Emily", emily_university_lunch_requirement, "emily_university_lunch_label")
        emily.add_unique_on_room_enter_event(emily_university_lunch_action)
        return



label emily_university_lunch_label(the_person):
    $ the_person = emily

    pass
    return
