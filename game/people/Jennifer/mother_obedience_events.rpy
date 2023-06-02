# In Jennifer's obedience arc, we slowly make MC the man of the house, by making Jennifer into a subservient housewife.
# In the intro event, we have Jennifer serve MC breakfast in bed, kickstarting the notion of her maid like services
# In the second event, we introduce the idea of "House Rules". Most of these are from Vren's outline, but new ideas are welcome.
# Things like daily breakfast, nude breakfast, breakfast with a service, on demand bed warmer, Arm Candy.

init 2 python:
    def mother_obedience_breakfast_requirement():
        return False


# Story progression actions
    def add_mother_obedience_breakfast_action():
        mother_obedience_breakfast_action = Action("Mom serves Breakfast in Bed", mother_obedience_breakfast_requirement, "mother_obedience_breakfast_label")
        mc.business.add_mandatory_crisis(mother_obedience_breakfast_action)
        return



label mother_obedience_breakfast_label():
    $ the_person = mom

    pass
    return
