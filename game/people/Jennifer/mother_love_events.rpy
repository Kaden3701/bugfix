# In Jennifer's love arc, we build up to the girlfriend request that is already in the vanilla code.
# In the first event, Jennifer calls on a whim, asking MC to meet her for a lunch date. If she is already employed by MC, she swings by his office to ask.
# In the second event, MC offers to cook for Jennifer. They wind up having wine and possibly sexual encounter depending on sluttiness progress.
# In the third event, MC begins to push the idea of romantic relationship. Jennifer initially pushes back.
# In the fourth event, we use the MC and Jennifer dating event.
# In all follow up events, we deal with the aftermath of what would happen if a romantic involvement were to occur. Lily, Rebecca, and possibly others give input.

init 2 python:
    def mother_love_lunch_date_requirement():
        return False


# Story progression actions
    def add_mother_love_lunch_date_action():
        mother_love_lunch_date_action = Action("Lunch Date With Mom", mother_love_lunch_date_requirement, "mother_love_lunch_date_label")
        mc.business.add_mandatory_crisis(mother_love_lunch_date_action)
        return



label mother_love_lunch_date_label():
    $ the_person = mom

    pass
    return
