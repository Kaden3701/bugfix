# Since a lot of players complain about a new game restart is due almost at every game
# update, I made this cheat screen for serums to be quickly researched and mastered.

init python:
    # Define function to open the screen
    def toggle_serum_cheat_menu():
        if renpy.get_screen("serum_cheat_menu"):
            renpy.hide_screen("serum_cheat_menu")
        else:
            renpy.show_screen("serum_cheat_menu")

        renpy.restart_interaction()

    config.keymap["toggle_serum_cheat_menu"] = ["t", "T"]
    config.underlay.append(renpy.Keymap(toggle_serum_cheat_menu=toggle_serum_cheat_menu))


screen serum_cheat_menu():
    add science_menu_background_image
    zorder 10
    use quick_menu

    default decorated = sorted([(trait.exclude_tags or "zzz", trait.name, i, trait) for i, trait in enumerate(list_of_traits + mc.business.blueprinted_traits)])
    default sorted_traits = [trait for exclude_tags, name, i, trait in decorated]

    vbox:
        xalign 0.04
        yalign 0.3
        frame:
            background "#0a142688"
            xsize 1200
            ysize 1000
            hbox:
                spacing 5
                vbox:
                    frame:
                        background "#000080"
                        xsize 380
                        vbox:
                            text "Available New Traits" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Trait to have it researched{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 380
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370
                            for dt in range(mc.business.research_tier, -1, -1):
                                if any([x for x in list_of_traits + mc.business.blueprinted_traits if x.tier == dt and not x.researched and x.is_unlocked]):
                                    frame:
                                        background "#000000"
                                        xsize 365
                                        text "Tier [dt]" style "serum_text_style_header"

                                    for trait in sorted_traits:
                                        if trait.tier == dt and not trait.researched and trait.is_unlocked:
                                            $ trait_title = get_trait_display_title(trait)
                                            textbutton "[trait_title]":
                                                style "textbutton_style"
                                                text_style "serum_text_style_traits"
                                                sensitive not isinstance(trait, SerumTraitBlueprint)
                                                action [Hide("trait_tooltip"), SetField(trait, "researched", True), SetField(trait, "unlocked", True)]
                                                hovered Show("trait_tooltip",None,trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                                unhovered Hide("trait_tooltip")
                                                xsize 365
                vbox:
                    frame:
                        background "#000080"
                        xsize 410
                        vbox:
                            text "Master Existing Traits" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Trait to add mastery levels{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 410
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 400

                            for dt in range(mc.business.research_tier, -1, -1):
                                if any([x for x in list_of_traits + mc.business.blueprinted_traits if x.tier == dt and x.researched]):
                                    frame:
                                        background "#000000"
                                        xsize 395
                                        text "Tier [dt]" style "serum_text_style_header"

                                for trait in sorted_traits:
                                    if trait.tier == dt and trait.researched:
                                        $ trait_title = get_trait_display_title(trait)
                                        $ trait_side_effects_text = get_trait_side_effect_text(trait)
                                        $ trait_mastery_text = get_trait_mastery_text(trait)

                                        textbutton "[trait_title]\n{size=14}Mastery Level: [trait_mastery_text] | Side Effect Chance: [trait_side_effects_text]{/size}":
                                            text_xalign 0.5
                                            text_text_align 0.5
                                            action [
                                                Hide("trait_tooltip"),
                                                SetField(trait, "mastery_level", trait.mastery_level + 1)
                                            ]
                                            alternate [
                                                Hide("trait_tooltip"),
                                                SetField(trait, "mastery_level", (trait.mastery_level - 1) if trait.mastery_level > 2 else 1.0),
                                            ]
                                            style "textbutton_style"
                                            text_style "serum_text_style_traits"
                                            hovered Show("trait_tooltip",None,trait, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                            unhovered Hide("trait_tooltip")
                                            xsize 395

                vbox:
                    frame:
                        background "#000080"
                        xsize 390
                        vbox:
                            text "Research New Designs" style "menu_text_title_style"
                            text "{color=#B14365}{size=14}Click the Design to have it researched{/size}{/color}" style "serum_text_style"

                    viewport:
                        xsize 390
                        ysize 980
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            xsize 370

                            for serum in mc.business.serum_designs:
                                if not serum.researched:
                                    textbutton "[serum.name] ([serum.current_research]/[serum.research_needed])":
                                        text_xalign 0.5
                                        text_text_align 0.5
                                        action [Hide("serum_tooltip"), SetField(serum, "researched", True)]
                                        style "textbutton_style"
                                        text_style "serum_text_style_traits"
                                        hovered Show("serum_tooltip",None,serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                        unhovered Hide("serum_tooltip")
                                        xsize 370
                                        xalign 0.5
