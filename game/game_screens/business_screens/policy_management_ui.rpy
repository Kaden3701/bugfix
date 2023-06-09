init -2 python:
    def purchase_policy(the_policy, ignore_cost = False):
        the_policy.buy_policy(ignore_cost)
        if not the_policy.toggleable or the_policy.is_toggleable: #Note: is_toggleable() checks to see if a toggleable policy has pre-reqs met to toggle, while toggleable flags a policy to turn on when bought then stay on.
            if the_policy.exclusive_tag is not None:
                for other_policy in mc.business.active_policy_list:
                    if other_policy.is_toggleable and the_policy.exclusive_tag == other_policy.exclusive_tag:
                        toggle_policy(other_policy)

            the_policy.apply_policy()

    def toggle_policy(the_policy):
        if the_policy in mc.business.active_policy_list:
            the_policy.remove_policy()
        else:
            if the_policy.exclusive_tag is not None:
                for other_policy in mc.business.active_policy_list:
                    if other_policy.is_toggleable and the_policy.exclusive_tag == other_policy.exclusive_tag:
                        toggle_policy(other_policy)

            the_policy.apply_policy()

    def get_policy_categories():
        org_pol = organisation_policies_list + [x for x in mc.business.policy_list if x not in uniform_policies_list + recruitment_policies_list + serum_policies_list + organisation_policies_list]

        return [["Uniform Policies",uniform_policies_list], ["Recruitment Policies",recruitment_policies_list], ["Serum Policies",serum_policies_list], ["Organisation Policies", org_pol]]


screen policy_selection_screen():
    add paper_background_image
    modal True
    zorder 100
    default categories = get_policy_categories()
    default selected_category = categories[0] #Default to the first in our categories list
    default selected_policy = None #If not None this will have it's info displayed on the right section of the bottom pane
    #TODO: Side bar showing current and max Complience, once the Complience system is added.

    vbox:
        xalign 0.5
        xanchor 0.5
        yanchor 0.0
        yalign 0.05
        spacing 20
        frame: #Top frame holding the policy categories that we have.
            xsize 1320
            ysize 140
            background "#0a142688"
            text "Funds: ${funds:,}".format(funds = __builtin__.int(mc.business.funds)):
                xalign 1.0
                xanchor 1.0
                yanchor 0.0
                style "serum_text_style"
            vbox:
                text "Policy Categories" style "menu_text_title_style" size 28 xalign 0.5
                hbox:
                    yoffset 10
                    spacing 25
                    for category in categories:
                        textbutton category[0]:
                            xysize (300, 50)
                            padding (0, 10)
                            action SetScreenVariable("selected_category", category)
                            sensitive selected_category != category
                            style "textbutton_style"
                            text_style "serum_text_style"
                            text_size 22
                            background "#000080"
                            hover_background "#1a45a1"
                            insensitive_background "#222222"

        frame:
            xsize 1320
            ysize 650
            background "#0a142688"
            xpadding 20
            ypadding 20
            hbox: #Container for the policy select and policy info screens.
                xanchor 0.5
                xalign 0.5
                yanchor 0.5
                yalign 0.5
                xsize 1300
                ysize 600
                spacing 20
                xfill True
                frame: #Container for policy select
                    xsize 500
                    background "#1a45a1aa"
                    viewport:
                        mousewheel True
                        scrollbars "vertical"
                        vbox: # Contains list for policy select
                            spacing 0
                            for policy in selected_category[1]:
                                $ policy_name = policy.name + " - "
                                if policy.is_active: #Display owned and active policies
                                    $ policy_name += "Active"
                                elif policy.is_owned:
                                    $ policy_name += "Disabled"
                                else:
                                    if policy.cost <= mc.business.funds:
                                        $ policy_name += "{color=20a020}$" + str(policy.cost) + "{/color}"
                                    else:
                                        $ policy_name += "{color=B14365}$" + str(policy.cost) + "{/color}"

                                    if not (policy.requirement_met and (policy.cost <= mc.business.funds)):
                                        $ policy_name = "{color=999999}" + policy_name + "{/color}"
                                textbutton policy_name:
                                    xalign 0.5
                                    xanchor 0.5
                                    #xsize 500
                                    xfill True
                                    action SetScreenVariable("selected_policy", policy)
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    text_size 16
                                    if policy.is_owned:
                                        if policy.is_active:
                                            background "#59853f"
                                            hover_background "#a9d59f"
                                        else:
                                            background "#85593f"
                                            hover_background "#d5a99f"
                                        #insensitive_background "#305012"
                                        insensitive_background "#222222"
                                    else:
                                        if policy.requirement_met and (policy.cost <= mc.business.funds):
                                            background "#000080"
                                        else:
                                            background "#000040"
                                        hover_background "#1a45a1"
                                        insensitive_background "#222222"
                                    sensitive selected_policy != policy

                frame: #Container for the seleected policy info.
                    background "#00000080"
                    xsize 780
                    xpadding 40
                    ypadding 10
                    if selected_policy is not None:
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            xalign 0.5
                            xanchor 0.5
                            ysize 500

                            vbox: # Contains title, description, and buy/toggle button for policy
                                xalign 0.5
                                xanchor 0.5
                                xfill True

                                text selected_policy.name:
                                    xalign 0.5
                                    xanchor 0.5
                                    yanchor 0.0
                                    text_align 0.5
                                    size 32
                                    style "serum_text_style"

                                $ toggleable_text = ""
                                if selected_policy.toggleable:
                                    $ toggleable_text = "- Toggleable"
                                else:
                                    $ toggleable_text = "- Permanent Upgrade"

                                text toggleable_text:
                                    xalign 0.5
                                    xanchor 0.5
                                    yanchor 0.0
                                    text_align 0.0
                                    size 18
                                    style "serum_text_style"

                                if not selected_policy.requirement_met and selected_policy.requirement_string != "":
                                    text selected_policy.requirement_string:
                                        xalign 0.5
                                        xanchor 0.5
                                        yanchor 0.0
                                        text_align 0.0
                                        size 18
                                        style "serum_text_style"
                                        color "#B14365"

                                null height 30

                                text selected_policy.desc:
                                    xalign 0.5
                                    xanchor 0.5
                                    yanchor 0.0
                                    text_align 0.5
                                    size 16
                                    style "serum_text_style"
                                    justify True

                        if selected_policy.is_owned:
                            $ the_button_name = ""
                            if selected_policy.toggleable:
                                if selected_policy.is_active:
                                    $ the_button_name = "Disable Policy"
                                else:
                                    $ the_button_name = "Enable Policy"

                                if not selected_policy.is_toggleable:
                                    if selected_policy.is_active:
                                        $ the_button_name += "\n{size=12}{color=B14365}Cannot be disabled, needed for:\n"
                                        $ blocking_policies = [a_policy for a_policy in selected_policy.depender_policies if a_policy.is_active]
                                        for requirement in blocking_policies:
                                            $ the_button_name += requirement.name
                                            if requirement is not blocking_policies[-1]:
                                                $ the_button_name += "\n" #Format the list with a comma if not at the end of the list.
                                        $ the_button_name += "{/color}{/size}"


                                    else:
                                        $ the_button_name += "\n{size=12}{color=B14365}Requires Active:\n"
                                        $ blocking_policies = [a_policy for a_policy in selected_policy.dependant_policies if not a_policy.is_active]
                                        for requirement in blocking_policies:
                                            $ the_button_name += requirement.name
                                            if requirement is not blocking_policies[-1]:
                                                $ the_botton_name += "\n" #Format the list with a comma if not at the end of the list.
                                        $ the_button_name += "{/color}{/size}"
                            else: #Note: Non-toggleable policies that are owned should _always_ be active.
                                $ the_button_name = "Policy Active"

                            textbutton the_button_name:
                                padding (0, 10)
                                align (.5, 1.0)
                                yanchor 1.0
                                xsize 300
                                action Function(toggle_policy, selected_policy)
                                style "textbutton_style"
                                text_style "serum_text_style"
                                background "#000080"
                                hover_background "#1a45a1"
                                insensitive_background "#222222"
                                sensitive selected_policy.is_toggleable
                        else: #We want to purchase it
                            textbutton "Purchase: $[selected_policy.cost]":
                                padding (0, 10)
                                align (.5, 1.0)
                                yanchor 1.0
                                xsize 300
                                action Function(purchase_policy, selected_policy)
                                style "textbutton_style"
                                text_style "serum_text_style"
                                background "#000080"
                                hover_background "#1a45a1"
                                insensitive_background "#222222"
                                sensitive selected_policy.requirement_met and (selected_policy.cost <= mc.business.funds)

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action Return()
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"

    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xsize 54
        ysize 54
        yanchor 1.0
        xalign 0.0
        yalign 1.0
        action Function(mc.business.reset_tutorial,"policy_tutorial")

    $ policy_tutorial_length = 4 #The number of  tutorial screens we have.
    if mc.business.event_triggers_dict["policy_tutorial"] > 0 and mc.business.event_triggers_dict["policy_tutorial"] <= policy_tutorial_length: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle "/tutorial_images/policy_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["policy_tutorial"])+".png"
            hover "/tutorial_images/policy_tutorial_"+__builtin__.str(mc.business.event_triggers_dict["policy_tutorial"])+".png"
            action Function(mc.business.advance_tutorial,"policy_tutorial")
