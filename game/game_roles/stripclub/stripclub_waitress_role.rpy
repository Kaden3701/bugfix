## Stripclub storyline Mod by Corrado
#  Waitresses role definition.
#  The role is appended to waitresses after they start to work for you.

init 5 python:
    def strip_club_hire_waitress(person):
        stripclub_waitresses.append(person)

    def strip_club_fire_waitress(person):
        if person in stripclub_waitresses:
            stripclub_waitresses.remove(person)

    stripclub_waitress_role = Role("Waitress", [promote_to_manager_action, strip_club_stripper_move_action, strip_club_stripper_fire_action, strip_club_stripper_performance_review_action],
        on_turn = stripclub_employee_on_turn, on_move = stripclub_employee_on_move, on_day = stripclub_employee_on_day, hidden = True)
