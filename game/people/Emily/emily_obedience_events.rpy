


init 2 python:
    def emily_ask_about_serum_requirement():
        return False


# Story progression actions
    def add_emily_ask_about_serum_action():
        emily_ask_about_serum_action = Action("Emily gets curious about your serums", emily_ask_about_serum_requirement, "emily_ask_about_serum_label")
        mc.business.add_mandatory_crisis(emily_ask_about_serum_action)
        return



label emily_ask_about_serum_label():
    $ the_person = emily

    pass
    return
