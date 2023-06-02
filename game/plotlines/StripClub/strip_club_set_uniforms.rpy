init 5 python:
    add_label_hijack("normal_start", "activate_strip_club_set_uniforms_label")
    add_label_hijack("after_load", "activate_strip_club_set_uniforms_label")

    def strip_club_set_uniforms_requirement():
        if get_strip_club_foreclosed_stage() >= 5:
            return True
        return False

    strip_club_set_uniforms_action = Action("Manage Stripclub Uniforms",strip_club_set_uniforms_requirement,"strip_club_set_uniforms_label")

label activate_strip_club_set_uniforms_label(stack):
    python:
        strip_club.add_action(strip_club_set_uniforms_action)
        execute_hijack_call(stack)
    return

label strip_club_set_uniforms_label():
    call screen stripclub_uniform_manager()
    if _return == "Add":
        call outfit_master_manager() from _call_outfit_master_manager_strip_club_set_uniforms #TODO: Decide if we need to pass this the uniform peramiters, of if we do that purely in what's selectable.
        if isinstance(_return, Outfit):
            $ mc.business.stripclub_uniforms.append(StripClubOutfit(_return))
        jump strip_club_set_uniforms_label
    return    
