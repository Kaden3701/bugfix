init -2 python:
    def offer_to_hire_requirement(the_person):
        if the_person.love < 10:
            return False
        elif the_person.has_role(employee_role):
            return False
        elif the_person == cousin and not cousin in stripclub_strippers:
            return False    # don't hire cousin until she goes stripping (schedule changes mess up logic)
        elif the_person == lily and the_person.has_role(generic_student_role):
            return False    # lily has her own offer to hire her when she's a student
        elif the_person == aunt and the_person.has_job(aunt_unemployed_job):
            return False    # aunt has her own offer to hire her when she's unemployed
        elif the_person.love < 20:
            return "Requires: 20 Love"
        elif mc.business.employee_count >= mc.business.max_employee_count:
            return "At employee limit"
        return True

    def setup_employee_stats(person): #Centralized function for setting up employee stuff when you hire them
        if person.employed_since == -1: # prevent fire / hire loop event triggering
            person.employed_since = day
            for other_employee in mc.business.employee_list:
                town_relationships.begin_relationship(person, other_employee) #They are introduced to everyone at work, with a starting value of "Acquaintance"
            mc.phone.register_number(person)        # you know the phone numbers of your employees

        # special case, she is a stripper but has no stripper_job so if you hire her before you confronted her, the schedule will be wrong
        if person == cousin and person in stripclub_strippers:
            person.set_schedule(cousin.home, the_times = [4])
            person.event_triggers_dict["stripping"] = False # un-flag blackmail event
            if person in stripclub_strippers:
                stripclub_strippers.remove(person)

        # set names when hiring (if not set)
        if not person.title:
            person.set_title(person.get_random_title())
        if not person.possessive_title:
            person.set_possessive_title(person.get_random_possessive_title())
        if not person.mc_title or person.mc_title == "Stranger":
            person.set_mc_title(person.get_random_player_title())

        # make sure she is dressed appropriately
        person.apply_planned_outfit()
        mc.business.listener_system.fire_event("new_hire", the_person = person)
        return

    def stripper_hire(the_person):
        if the_person not in stripclub_strippers:
            stripclub_strippers.append(the_person)
        return

    def stripper_replace(the_person): # on_quit function called for strippers to make sure there's always someone working at the club. Also removes them from the list of dancers
        #Note: Gabrielle is a special case and is manually added back into the list after she quits.
        if the_person in stripclub_strippers:
            stripclub_strippers.remove(the_person)

        if len(stripclub_strippers) < 4:
            create_random_stripper()
        return

label stranger_hire_result(the_person): #Check to see if you want to hire someone.
    $ the_person.salary = the_person.calculate_base_salary()
    call hire_select_process([the_person, 1]) from _call_hire_select_process_stranger_hire_result
    if isinstance(_return, Person):
        call hire_someone(the_person) from _call_hire_someone_process_stranger_hire_result
        $ the_person.draw_person()
        return True
    else:
        $ the_person.draw_person()
        return False

    return False
