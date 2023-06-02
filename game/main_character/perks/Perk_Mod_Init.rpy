default perk_system = None

init 5 python:
    add_label_hijack("normal_start", "activate_perk_mod_core")
    add_label_hijack("after_load", "update_perk_mod_core")

    Perk_Tutorial_Crisis = Action("Perk Tutorial",Perk_Tutorial_Crisis_requirement,"Perk_Tutorial_Crisis_label")


    def Perk_mod_initialization():
        global perk_system
        perk_system = Perks()
        mc.business.event_triggers_dict["perk_tutorial"] = 1
        mc.business.add_mandatory_crisis(Perk_Tutorial_Crisis)
        return

label activate_perk_mod_core(stack):
    python:
        Perk_mod_initialization()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label update_perk_mod_core(stack):
    python:
        if perk_system is None:
            Perk_mod_initialization()

        if mc.business.event_triggers_dict.get("perk_tutorial", 1) < 2:
            mc.business.event_triggers_dict["perk_tutorial"] = 1
        if not perk_system.has_ability_perk("Time of Need"):
            mc.business.add_mandatory_crisis(Perk_Tutorial_Crisis)

        perk_system.save_load()

        execute_hijack_call(stack)
    return
