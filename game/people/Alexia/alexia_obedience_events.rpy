


init 2 python:
    def alexia_company_propaganda_intro_requirement():
        return False


# Story progression actions
    def add_alexia_company_propaganda_intro_action():
        alexia_company_propaganda_intro_action = Action("Alexia tries viral marketing", alexia_company_propaganda_intro_requirement, "alexia_company_propaganda_intro_label")
        mc.business.add_mandatory_crisis(alexia_company_propaganda_intro_action)
        return



label alexia_company_propaganda_intro_label():
    $ the_person = alexia

    pass
    return
