# Rebecca's obedience story.
# At first, we convincer her to help out with the business accounting.
# Later, we find out she used to help her ex with his business finances, and that he used to launder money
# She helps us with MC's business, laundering money
# Later, we gain the ability to blackmail her ex

init 2 python:
    def aunt_employement_problems_requirement(person):
        return False

    def aunt_employment_offer_requirement(person):
        return False

    def aunt_cpa_first_day_requirement():
        return False

    def aunt_money_launder_offer_requirement():
        return False

    def add_aunt_employement_problems_action():
        aunt_employement_problems_action = Action("Rebecca's Employment Issues", aunt_employement_problems_requirement, "aunt_employement_problems_label")
        aunt.add_unique_on_room_enter_event(aunt_employement_problems_action)
        aunt.progress.obedience_step = 0
        return

    def add_aunt_employment_offer_action():
        aunt_employment_offer_action = Action("Rebecca's Employment Issues", aunt_employment_offer_requirement, "aunt_employment_offer_label")
        aunt.add_unique_on_room_enter_event(aunt_employment_offer_action)
        aunt.progress.obedience_step = 1
        return

    def add_aunt_cpa_first_day_action():
        aunt_cpa_first_day_action = Action("Rebecca's Employment Issues", cpa_first_day_requirement, "cpa_first_day_label")
        mc.business.add_mandatory_crisis(cpa_first_day_action)
        aunt.progress.obedience_step = 2
        return

    def add_aunt_money_launder_offer_action():
        aunt_employement_problems_action = Action("Rebecca's Employment Issues", aunt_money_launder_offer_requirement, "aunt_money_launder_offer_label")
        mc.business.add_mandatory_crisis(aunt_money_launder_offer_action)
        aunt.progress.obedience_step = 3
        return




label aunt_employement_problems_label(the_person):  #120
    "In this label, we discover that [the_person.title] is having trouble getting employement."
    "We offer to help her out but she turns us down."
    return

label aunt_employment_offer_label(the_person):  #140
    "In this label, we discover that [the_person.title]'s ex is sabotaging her employment prospects."
    "We offer to help her out but she turns us down."
    "We offer again but this time as part time work that she can accomplish on her own time, just coming in once a week, and she accepts."
    return

label aunt_cpa_first_day_label():
    $ the_person = aunt
    "In this label, we show [the_person.title] around the office for her first day. She discovers what the business is actually about."
    "Due to her obedience, we convince her to keep it quiet. She mentions how difficult it can be to hide sources of income in a business like this."
    "She offers to help manage MC's accounts, providing for investment opportunities for the business and employees both."
    return

label aunt_money_launder_offer_label(): #160
    $ the_person = aunt
    "In this label, [the_person.title] presents MC with options for laundering money. MC can accept or refuse."
    "IF MC accepts, we gain improved attention drain, but possibly at some other consequence."
    return
