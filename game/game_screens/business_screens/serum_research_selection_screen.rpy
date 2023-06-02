screen select_trait_research(the_traits): #You can now pass extra inventories, as well as names for all of the inventories you are passing. Returns nothing, but is used to view inventories.
    default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
    default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]

    add science_menu_background_image
    hbox:
        xalign 0.52
        yalign 0.05
        spacing 40
        frame:
            background "#000080"
            ysize 48
            xsize 600
            text "Select a trait to research" style "menu_text_title_style" xalign 0.5:
                size 24
    hbox:
        $ count = 0
        xalign 0.05
        yalign 0.12
        yanchor 0.07
        spacing 40
        frame:
            background "#0a142688"
            xsize 600
            vbox:
                xalign 0.02
                yalign 0.02
                frame:
                    background "#000080"
                    xsize 590
                    text "Serums Traits" style "menu_text_title_style" xalign 0.5

                viewport:
                    xsize 600
                    ysize 900
                    scrollbars "vertical"
                    mousewheel True
                    spacing 1
                    xalign 0

                    vbox:
                        for dt in range(mc.business.research_tier, -1, -1):
                            if any([x for x in sorted_traits if x.tier == dt and not isinstance(x, SerumTraitBlueprint) and x.researched]):
                                frame:
                                    background "#000000"
                                    xsize 365
                                    text "Tier [dt]" style "serum_text_style_header"

                                for trait in sorted_traits:
                                    if trait.tier == dt and not isinstance(trait, SerumTraitBlueprint) and trait.researched:
                                        $ trait_title = get_trait_display_title(trait)
                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\nMastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]":
                                            text_xalign 0.5
                                            text_text_align 0.5
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            xsize 580
                                            action [Hide("select_trait_research"),Hide("trait_tooltip"),Return(trait)]
                                            hovered Show("trait_tooltip",None, trait, given_align = (0.97,0.06), given_anchor = (1.0,0.0), show_unlocks = False)
