init 2 python:
    # maid knows her work locations by using add_work_location / remove_work_location
    # then set her schedule (preferably using maid_job) to be in one of these locations
    # she will automatically wear a maid outfit when she moves to the location and unlock actions.

    # assign new maid job to person (with empty work schedule)
    # can also be used as 'cleaning lady' or whatever work you want to assign the maid role
    def assign_maid_job(person, job_title = "Maid"):
        person.change_job(Job(job_title, maid_role, work_days = [], work_times = []))
        return

    # remove maid job from person (defacto make her unemployed)
    def remove_maid_job(person):
        person.change_job(unemployed_job)
        return

    # in effect assign her as many work locations as you see fit
    def add_maid_work_location(person, location, the_days = None, the_times = None):
        if not person.has_role(maid_role):
            return False
        person.job.schedule.set_schedule(location, the_days, the_times)
        return True

    def remove_maid_work_location(person, location = None):
        if not person.has_role(maid_role) or location is None:
            return False

        person.job.schedule.remove_location(location)
        return True

    def get_maid_work_locations(person):
        locations = []
        if not person.has_role(maid_role):
            return locations

        for day_number in range(0, 7):
            for time_number in range(0,5):
                destination = person.job.schedule.get_destination(specified_day = day_number, specified_time = time_number)
                if destination and not destination in locations:
                    locations.append(destination)

        return locations

    def clear_maid_work_locations(person):
        for location in get_maid_work_locations(person):
            remove_maid_work_location(person, location)
        return

    def maid_on_move(person):
        return

    def maid_on_turn(person):
        return

    def maid_on_day(person):
        return

    def maid_slap_ass_requirement(person):
        return person.obedience > 120 and person.is_at_work

    def maid_grope_requirement(person):
        return person.love > 20 and person.is_at_work

    def maid_service_requirement(person):
        return person.sluttiness > 40 and person.is_at_work

    maid_slap_ass_action = Action("Slap Her", maid_slap_ass_requirement, "maid_slap_ass_label")
    maid_grope_action = Action("Grope Her", maid_grope_requirement, "maid_grope_label")
    maid_service_action = Action("Bend Over", maid_service_requirement, "maid_service_label")

    maid_role = Role("Maid", actions = [
            maid_slap_ass_action,
            maid_grope_action,
            maid_service_action
        ],
        hidden = True, on_turn = maid_on_turn, on_move = maid_on_move, on_day = maid_on_day)

label maid_slap_ass_label(the_person):
    return

label maid_grope_label(the_person):
    return

label maid_service_label(the_person):
    return
