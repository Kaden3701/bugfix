init 1 python:
    def daily_serum_dosage_duty_on_move_enhanced(the_person):
        if the_person.event_triggers_dict.get("daily_serum_distributed", False):
            return #Give it to them first thing in the morning, but only once

        elif not the_person.is_at_work:
            return #Don't give it to them if they aren't at work.

        the_serum = None
        if the_person in mc.business.research_team:
            the_serum = mc.business.r_serum
        elif the_person in mc.business.market_team:
            the_serum = mc.business.m_serum
        elif the_person in mc.business.production_team:
            the_serum = mc.business.p_serum
        elif the_person in mc.business.supply_team:
            the_serum = mc.business.s_serum
        elif the_person in mc.business.hr_team:
            the_serum = mc.business.h_serum
        elif get_strip_club_foreclosed_stage() >= 5:
            if the_person in stripclub_strippers and hasattr(mc.business, "strippers_serum"):
                the_serum = mc.business.strippers_serum
            elif the_person in stripclub_waitresses and hasattr(mc.business, "waitresses_serum"):
                the_serum = mc.business.waitresses_serum
            elif the_person in stripclub_bdsm_performers and hasattr(mc.business, "bdsm_performers_serum"):
                the_serum = mc.business.bdsm_performers_serum
            elif hasattr(mc.business, "manager_serum") and (the_person.has_job(stripclub_manager_job) or the_person.has_job(stripclub_mistress_job)):
                the_serum = mc.business.manager_serum

        if the_serum is not None:
            the_person.event_triggers_dict["daily_serum_distributed"] = True
            should_give_serum = True
            for active_serum in the_person.serum_effects:
                if the_serum.is_same_design(active_serum):
                    if active_serum.duration - active_serum.duration_counter >= 3:
                        should_give_serum = False #Don't double-dose girls if they have the serum running and it will last the work day already
                        break

            if should_give_serum:
                if mc.business.inventory.get_serum_count(the_serum) > 0:
                    mc.business.inventory.change_serum(the_serum,-1)
                    the_person.give_serum(the_serum, add_to_log = False)
                else:
                    the_message = "Stockpile out of " + the_serum.name + " to give to staff."
                    mc.business.add_counted_message(the_message)

    daily_serum_dosage_duty.on_move = daily_serum_dosage_duty_on_move_enhanced

    def stripclub_employee_on_turn(the_person):
        #Each turn check to see if the person wants to quit.
        for duty in the_person.duties:
            if the_person.is_at_work or not duty.only_at_work:
                duty.on_turn(the_person)

        if the_person.is_at_work:
            the_person.event_triggers_dict["worked_today"] = True
        return

    def stripclub_employee_on_move(the_person):
        for duty in the_person.duties:
            if the_person.is_at_work or not duty.only_at_work:
                duty.on_move(the_person)
        return

    def stripclub_employee_on_day(the_person):
        for duty in the_person.duties:
            if the_person.event_triggers_dict.get("worked_today", False) or not duty.only_at_work: #Only perform on_day functions if they had work that day.
                duty.on_day(the_person)

        the_person.event_triggers_dict["worked_today"] = False #Reset this for the next day
        return
