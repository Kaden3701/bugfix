label do_training(the_person):
    call screen training_select(the_person)
    if _return:
        call training_manager(the_person, _return) from _call_training_manager_do_training
        if _return:
            $ the_person.event_triggers_dict["trance_training_available"] = False
    return

label training_manager(the_person, the_trainable):
    $ renpy.call(the_trainable.on_train_label, the_person, *the_trainable.extra_args) #The on_train label should make any actual changes needed
    if _return: #Note that this does NOT include None, which is the default return
        $ mc.spend_clarity(the_trainable.get_cost(the_person))
        $ the_person.training_log[the_trainable.training_tag] += 1
        return True
    return False

init 2 python:
    def build_other_trainables(person):
        other_list = special_trainables[:]
        for role in person.special_role:
            for trainable in role.role_trainables:
                if trainable not in other_list:
                    other_list.append(trainable)
        return other_list

screen training_select(the_person):
    add paper_background_image
    modal True
    zorder 100
    $ trance_string = ""
    if the_person.has_exact_role(trance_role):
        $ trance_string = "Normal Trance: 100% Clarity Cost"
    elif the_person.has_exact_role(heavy_trance_role):
        $ trance_string = "Heavy Trance: 50% Clarity Cost"
    elif the_person.has_exact_role(very_heavy_trance_role):
        $ trance_string = "Very Heavy Trance: 25% Clarity Cost"

    default other_list = build_other_trainables(the_person)

    vbox:
        spacing 25
        xalign 0.5
        xanchor 0.5
        yalign 0.2
        use girl_title_header(the_person, 1750, 120, include_details_button = True)

        hbox:
            xsize 1750
            xalign 0.5
            xanchor 0.5
            spacing 30

            for trainable_list in [("Stat Training", stat_trainables),("Skill Training", skill_trainables),("Opinion Training", opinion_trainables), ("Other Training", other_list)]:
                frame:
                    background "#1a45a1aa"
                    xsize 410
                    ysize 450
                    viewport:
                        xsize 410
                        yfill True
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            text trainable_list[0] style "menu_text_style" size 22
                            for trainable in [x for x in trainable_list[1] if x.can_be_trained(the_person)]:
                                use trainable_select_button(trainable, the_person)
    vbox:
        xalign 0.1
        yalign 0.15
        xanchor 0.1
        yanchor 0.5
        text "Free Clarity: " + str(mc.free_clarity):
            style "menu_text_style"
            size 22

        text trance_string:
            style "menu_text_style"
            size 22

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action Return(False)
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
