init 2 python:
    def get_exclude_tags(trait):
        tags = ""
        if trait.exclude_tags:
            tags = " - "
            for a_tag in trait.exclude_tags:
                tags += "{color=#d38c19}[" + a_tag + "]{/color}"
        return tags

    def get_trait_allowed(starting_serum, trait):
        for a_trait in starting_serum.traits:
            if any(t in a_trait.exclude_tags for t in trait.exclude_tags):
                return False
        return True

    def get_trait_aspect_tags(trait):
        aspect_tags = "\n{size=15}"
        if trait.tier > mc.business.max_serum_tier:
            aspect_tags += "Tier: {color=#98fb98}" + str(trait.tier) + "{/color}"
        else:
            aspect_tags += "Tier:" + str(trait.tier)

        aspect_tags += "{color=#387aff}   Ment: " + str(trait.mental_aspect) + "{/color}"
        aspect_tags += "{color=#00AA00}   Phys: " + str(trait.physical_aspect) + "{/color}"
        aspect_tags += "{color=#FFC0CB}   Sex: " + str(trait.sexual_aspect) + "{/color}"
        aspect_tags += "{color=#FFFFFF}   Med: " + str(trait.medical_aspect) + "{/color}"
        aspect_tags += "{color=#AAAAAA}   Flaw: " + str(trait.flaws_aspect) + "{/color}"
        aspect_tags += "{color=#FF6249}   Attn: " + str(trait.attention) + "{/color}"
        aspect_tags += "{/size}"
        return aspect_tags

    def get_filtered_traits(traits):
        cs = renpy.current_screen()
        show_mental = cs.scope["show_mental"]
        show_sexual = cs.scope["show_sexual"]
        show_physical = cs.scope["show_physical"]
        show_medical = cs.scope["show_medical"]

        return [x for x in traits if (show_mental or x.mental_aspect != 0) and (show_sexual or x.sexual_aspect != 0) and (show_physical or x.physical_aspect != 0) and (show_medical or x.medical_aspect != 0)]


screen serum_design_ui(starting_serum,current_traits):
    $ renpy.block_rollback()

    default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
    default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]
    default show_mental = True
    default show_sexual = True
    default show_physical = True
    default show_medical = True

    add science_menu_background_image
    default trait_tooltip = primitive_serum_prod
    hbox:
        yalign 0.15
        xanchor 0.5
        xalign 0.5
        xsize 1180
        spacing 10
        frame:
            background "#0a142688"
            ysize 850

            vbox:
                xsize 530
                if not starting_serum.has_production_trait:
                    frame:
                        background "#000080"
                        xsize 530
                        text "Pick Production Type" style "menu_text_title_style" xalign .5
                    frame:
                        background "#0a142688"
                        xalign 0.5
                        xsize 530
                        ysize 175

                        viewport:
                            xsize 530
                            scrollbars "vertical"
                            mousewheel True
                            vbox:
                                for trait in sorted([x for x in list_of_traits + mc.business.blueprinted_traits if x.researched and x not in starting_serum.traits and "Production" in x.exclude_tags], key = lambda trait: trait.tier, reverse = True):
                                    $ trait_tags = get_exclude_tags(trait)
                                    $ trait_allowed = get_trait_allowed(starting_serum, trait)

                                    #$ trait_side_effects_text = get_trait_side_effect_text(trait)
                                    #$ trait_mastery_text = get_trait_mastery_text(trait)
                                                #+ "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                    textbutton "[trait.name][trait_tags]":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 530
                                        sensitive trait_allowed
                                        action [
                                            Function(starting_serum.add_trait,trait)
                                        ]
                                        hovered [
                                            SetScreenVariable("trait_tooltip", trait)
                                        ]

                                        #unhovered [
                                        #Hide("trait_tooltip")
                                        #]

                frame:
                    background "#000080"
                    xsize 530
                    text "Add Serum Traits" style "menu_text_title_style" xalign .5

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 530
                    ysize ((490 + 216) if starting_serum.has_production_trait else 490)

                    viewport:
                        xsize 530
                        scrollbars "vertical"
                        mousewheel True

                        vbox:
                            for dt in range(mc.business.research_tier + 1, -1, -1):
                                if any([x for x in get_filtered_traits(list_of_traits + mc.business.blueprinted_traits) if x.tier == dt and x not in starting_serum.traits and x.researched and "Production" not in x.exclude_tags]):

                                    frame:
                                        background "#000000"
                                        xsize 530
                                        text "Tier [dt]" style "serum_text_style_header"

                                    for trait in [x for x in get_filtered_traits(sorted_traits) if x.tier == dt and x.researched and x not in starting_serum.traits and "Production" not in x.exclude_tags]:
                                        $ trait_tags = get_exclude_tags(trait)
                                        $ trait_allowed = get_trait_allowed(starting_serum, trait)

                                        #$ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        #$ trait_mastery_text = get_trait_mastery_text(trait)
                                                        #+ "\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text] %":
                                        textbutton "[trait.name][trait_tags]":
                                            style "textbutton_style"
                                            text_style "serum_text_style"
                                            xsize 530
                                            sensitive trait_allowed
                                            action [
                                                Function(starting_serum.add_trait,trait)
                                            ]
                                            hovered [
                                                SetScreenVariable("trait_tooltip", trait)
                                            ]

                                            #unhovered [
                                            #Hide("trait_tooltip")
                                            #]

                frame:
                    background "#000080"
                    xsize 530
                    text "Aspect Filter" style "menu_text_title_style" xalign .5

                frame:
                    background "#0a142688"
                    xalign 0.5
                    xsize 530
                    grid 4 1 xanchor 0.5 xalign 0.5 xfill True:
                        textbutton "{color=#387aff}Mental{/color}":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            hover_background "#143869"
                            background ("#171717" if show_mental else "#14386988")
                            action [ToggleScreenVariable("show_mental")]
                        textbutton "{color=#00AA00}Physical{/color}":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            hover_background "#143869"
                            background ("#171717" if show_physical else "#14386988")
                            action [ToggleScreenVariable("show_physical")]
                        textbutton "{color=#FFC0CB}Sexual{/color}":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            hover_background "#143869"
                            background ("#171717" if show_sexual else "#14386988")
                            action [ToggleScreenVariable("show_sexual")]
                        textbutton "{color=#FFFFFF}Medical{/color}":
                            style "textbutton_style"
                            text_style "serum_text_style"
                            hover_background "#143869"
                            background ("#171717" if show_medical else "#14386988")
                            action [ToggleScreenVariable("show_medical")]

        frame:
            background "#0a142688"
            xysize (530, 850)
            vbox xfill True:
                frame xfill True:
                    background "#000080"


                    text "Remove a trait" style "menu_text_title_style" xalign .5

                frame:
                    background "#0a142688"
                    xalign 0.5
                    ysize 450
                    viewport:

                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            for trait in starting_serum.traits:
                                $ trait_tags = get_exclude_tags(trait)
                                $ trait_aspect_tags = get_trait_aspect_tags(trait)
                                $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                $ trait_mastery_text = get_trait_mastery_text(trait)

                                textbutton "[trait.name][trait_tags][trait_aspect_tags]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
                                    style "textbutton_style"
                                    text_style "serum_text_style"
                                    xsize 520
                                    action[
                                        Function(starting_serum.remove_trait,trait)
                                    ]
                                    hovered [
                                        SetScreenVariable("trait_tooltip", trait)
                                    ]
                                    #unhovered Hide("trait_tooltip")

                $ trait_side_effects_text = get_trait_side_effect_text(trait_tooltip)
                $ trait_mastery_text = get_trait_mastery_text(trait_tooltip)
                frame xfill True:
                    background "#000080"
                    text "[trait_tooltip.name]" style "menu_text_title_style" xalign .5
                frame:
                    background None
                    text "{size=14}Mastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]{/size}" style "serum_text_style" xalign .5

                use aspect_grid(trait_tooltip)

                frame xfill True:
                    background "#0a142688"
                    xalign 0.5
                    viewport:
                        draggable True
                        xfill True
                        mousewheel "vertical"
                        vbox:
                            spacing 5
                            grid 2 1 xfill True:
                                spacing 5
                                frame xfill True:
                                    background "#43B197"
                                    yminimum 66
                                    text trait_tooltip.positive_slug style "serum_text_style" size 16
                                frame xfill True:
                                    background "#B14365"
                                    yminimum 66
                                    text trait_tooltip.negative_slug style "serum_text_style" size 16
                            frame xfill True:
                                background "#000080"
                                text trait_tooltip.desc style "serum_text_style"

        frame:
            background "#0a142688"
            ysize 850
            vbox:
                xsize 550
                spacing 5
                frame:
                    background "#000080"
                    xsize 550
                    text "Current Serum Statistics:" style "menu_text_title_style" xalign .5

                frame:
                    if starting_serum.slots_used > starting_serum.slots:
                        background "#B14365"
                    else:
                        background "#000080"
                    xsize 550
                    text "Trait Slots: [starting_serum.slots_used]/[starting_serum.slots]" style "serum_text_style"

                viewport:
                    draggable True
                    xsize 550
                    ysize 50
                    mousewheel "horizontal"
                    hbox:
                        xanchor 0.5
                        xalign 0.5
                        spacing 5
                        xsize 550
                        for num in __builtin__.range(__builtin__.max(starting_serum.slots,starting_serum.slots_used)):
                            if num < starting_serum.slots_used and num < starting_serum.slots:
                                add serum_slot_full_image xanchor 0.5 xalign 0.5
                            elif num < starting_serum.slots_used and num >= starting_serum.slots:
                                add serum_slot_incorrect_image xanchor 0.5 xalign 0.5
                            else:
                                add serum_slot_empty_image xanchor 0.5 xalign 0.5

                use aspect_grid(starting_serum)

                hbox:
                    spacing 5
                    vbox:
                        spacing 5
                        frame:
                            background "#000080"
                            xsize 270
                            text "Research Required: {color=#ff0000}[starting_serum.research_needed]{/color}" style "serum_text_style"
                        frame:
                            background "#000080"
                            xsize 270
                            text "Production Cost: {color=#ff0000}[starting_serum.production_cost]{/color}" style "serum_text_style"
                        frame:
                            background "#000080"
                            xsize 270
                            if starting_serum.tier <= mc.business.max_serum_tier:
                                text "Serum Tier: [starting_serum.tier]" style "serum_text_style"
                            else:
                                text "Serum Tier: {color=#fb6868}[starting_serum.tier]{/color}" style "serum_text_style"
                    vbox:
                        spacing 5
                        frame:
                            background "#000080"
                            xsize 270

                            $ calculated_profit = __builtin__.round(mc.business.get_serum_base_value(starting_serum)-(starting_serum.production_cost/mc.business.batch_size))
                            if calculated_profit >= 0:
                                text "Expected Profit:{color=#98fb98} $[calculated_profit]{/color}" style "serum_text_style"
                            else:
                                $ calculated_profit = 0 - calculated_profit
                                text "Expected Profit:{color=#ff0000} -$[calculated_profit]{/color}" style "serum_text_style"

                        frame:
                            background "#000080"
                            xsize 270
                            text "Duration: [starting_serum.duration] Turns" style "serum_text_style"

                        frame:
                            background "#000080"
                            xsize 270
                            text "Unlock Cost: [starting_serum.clarity_needed] Clarity" style "serum_text_style"

                frame:
                    background "#000080"
                    xsize 550
                    text "Serum Effects:" style "menu_text_title_style" xalign .5

                viewport:
                    xsize 550
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    vbox:
                        for trait in starting_serum.traits:
                            textbutton "[trait.name]":
                                style "textbutton_style"
                                text_style "serum_text_style"
                                xsize 540
                                action  NullAction()
                                hovered SetScreenVariable("trait_tooltip", trait)

                            hbox:
                                frame:
                                    background "#43B197"
                                    xsize 270
                                    margin (5, 0, 5, 0)
                                    text "[trait.positive_slug]" style "serum_text_style" size 16
                                frame:
                                    xsize 270
                                    background "#B14365"
                                    text trait.negative_slug style "serum_text_style" size 16

    frame:
        background "#0a142688"
        xsize 250
        xanchor 0.5
        xalign 0.5
        yalign 0.93
        hbox:
            xanchor 0.5
            xalign 0.5
            spacing 40
            textbutton "Create Design":
                action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return(starting_serum)]
                sensitive (starting_serum.slots >= starting_serum.slots_used and __builtin__.len(starting_serum.traits) > 0 and starting_serum.has_tag("Production"))

                style "textbutton_style"
                text_style "serum_text_style"
                xanchor 0.5
                xalign 0.5
                xsize 230

            textbutton "Reject Design":
                action [Hide("trait_tooltip"), Hide("serum_design_ui"), Hide("serum_tooltip"), Return("None")]

                style "textbutton_style"
                text_style "serum_text_style"
                xanchor 0.5
                xalign 0.5
                xsize 230

            textbutton "View Contracts":
                action Show("contract_select")
                style "textbutton_style"
                text_style "serum_text_style"
                xanchor 0.5
                xalign 0.5
                xsize 230

    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xsize 54
        ysize 54
        yanchor 1.0
        xalign 0.0
        yalign 1.0
        action Function(mc.business.reset_tutorial,"design_tutorial")

    if mc.business.event_triggers_dict.get("design_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("design_tutorial", 1) <= 5: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle "/tutorial_images/design_tutorial_{}.png".format(mc.business.event_triggers_dict.get("design_tutorial", 1))
            hover "/tutorial_images/design_tutorial_{}.png".format(mc.business.event_triggers_dict.get("design_tutorial", 1))
            action Function(mc.business.advance_tutorial,"design_tutorial")
