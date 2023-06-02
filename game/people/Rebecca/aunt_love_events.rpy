init 2 python:
    def aunt_first_date_tips_requirement(the_person):
        return False

    def add_aunt_first_date_tips_action():
        aunt_first_date_tips_action = Action("Rebecca's dating problems", aunt_first_date_tips_requirement, "aunt_first_date_tips_label")
        aunt.add_unique_on_room_enter_event(aunt_first_date_tips_action)
        return

label aunt_first_date_tips_label(the_person):
    "In this label, we help [the_person.title] with tips on getting first and second dates on dating apps."
    return
