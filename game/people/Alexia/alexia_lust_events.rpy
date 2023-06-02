


init 2 python:
    def alexia_viral_marketing_requirement(the_person):
        return False


# Story progression actions
    def add_alexia_viral_marketing_action():
        alexia_viral_marketing_action = Action("Alexia tries viral marketing", alexia_viral_marketing_requirement, "alexia_viral_marketing_label")
        alexia.add_unique_on_room_enter_event(alexia_viral_marketing_action)
        return



label alexia_viral_marketing_label(the_person):
    $ the_person = mom

    pass
    return
