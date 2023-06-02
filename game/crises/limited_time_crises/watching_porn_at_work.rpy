# This could be expanded in future version where you catch someone watching porn
# with many choices like punishment, taking them to your office, service here etc.

init -1 python:
    def watching_porn_at_work_requirement(person):
        if not person.is_at_work:
            return False
        # special case for college inters
        if person.is_intern and not person.location == university:
            return True
        return person.is_employee or person.is_strip_club_employee

    def watching_porn_at_work_raise_arousal(person):
        if person.arousal_perc < 50:
            person.change_arousal((person.max_arousal * .5) - person.arousal, add_to_log = False)
        return

    limited_time_event_pool.append([
        Action("Employee watches porn at work", watching_porn_at_work_requirement, "watching_porn_at_work", event_duration = 2),
        4, "on_enter"])

label watching_porn_at_work(the_person):
    # this is an action without feedback to player (for now)
    # it only raises her arousal and will allow for triggering 'work_spank_opportunity'
    # having an arousal aura or vibe policy will also increase their arousal

    $ watching_porn_at_work_raise_arousal(the_person)
    return
