init 2 python:
    def clone_recall_requirement(person):
        return person not in clone_facility.people

    def clone_rent_apartment_requirement(person):
        if not person.home is clone_facility:
            return False
        if not mc.business.has_funds(25000):
            return "Requires: $25,000"
        return person.home == clone_facility

    # Clone Recall - Brings the clone back to base
    clone_recall_action = Action("Recall clone", clone_recall_requirement, "clone_recall_label", menu_tooltip = "Bring the clone back to the facility for modifications")

    # Clone Rent House - Rent a house for your clone
    clone_rent_apartment_action = Action("Rent Apartment\n{color=#ff0000}{size=18}Costs: $25000{/size}{/color}", clone_rent_apartment_requirement, "clone_rent_apartment_label", menu_tooltip = "Rent a apartment for your clone.")

    clone_role = Role("Clone", [clone_recall_action, clone_rent_apartment_action])



# Labels
label clone_recall_label(the_person):
    "You order [the_person.title] back to [clone_facility.formal_name]."

    $ the_person.change_location(clone_facility)

    the_person "Okay, [the_person.mc_title]. I'll head there next."
    return

label clone_rent_apartment_label(the_person):
    $ the_person.draw_person()
    mc.name "Listen, [the_person.fname], you are very dear to me and I have decided that you are mature enough to live on your own."
    mc.name "So I am willing to rent you a place where you can live by yourself."
    the_person "Please [the_person.mc_title], I love being with you, do I really have to go?"
    menu:
        "Let her stay":
            mc.name "Do you really want to live here, in this facility?"
            the_person "Yes, [the_person.mc_title], please let me stay..."
            mc.name "Ok, if that is what you want."
            return
        "Rent the apartment":
            mc.name "I think it's better for your development if you have your own place. Trust me."
            the_person "Ok [the_person.mc_title], if you think that is best, I will honor your wish."

            python:
                the_person.home = None
                the_person.generate_home()
                mc.business.change_funds(-25000)
                the_person.set_schedule(None, the_times = [1,2,3])

            "You make all the necessary arrangements, your clone [the_person.fname] will now stay at the new apartment and start living her own life."

    $ clear_scene()
    return
