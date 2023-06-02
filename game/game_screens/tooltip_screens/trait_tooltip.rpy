init 2:
    python:
        def get_unlockable_trait_names(trait):
            return [x.name for x in list_of_traits if trait in x.requires]


screen trait_tooltip(the_trait, given_align = (0.0,0.0), given_anchor = (0.0,0.0), show_unlocks = True):
    frame:
        background "#0a142688"

        xsize 525
        align given_align
        anchor given_anchor

        vbox:
            spacing 5
            xalign 0.5
            frame xfill True:
                background "#000080"
                text "[the_trait.name]" + (" (C)" if isinstance(the_trait, SerumTraitBlueprint) else ""):
                    style "menu_text_title_style"
                    xalign 0.5

            use aspect_grid(the_trait)

            grid 2 1 xfill True:
                spacing 5
                frame xfill True:
                    yminimum 80
                    background "#43B197"
                    text "[the_trait.positive_slug]" style "serum_text_style_traits"

                frame xfill True:
                    background "#B14365"
                    yminimum 80
                    text "[the_trait.negative_slug]" style "serum_text_style_traits"

            frame xfill True:
                background "#000080"
                text "[the_trait.desc]" style "serum_text_style"

            $ unlockable_traits = get_unlockable_trait_names(the_trait)
            if show_unlocks and len(unlockable_traits) > 0:
                frame xfill True:
                    background "#000000"
                    text "Required for Traits" style "menu_text_title_style" xalign 0.5

                frame xfill True:
                    background "#000080"
                    viewport xfill True:
                        ysize min(len(unlockable_traits) * 24, 580)
                        scrollbars "vertical"
                        mousewheel True
                        vbox:
                            for ut in get_unlockable_trait_names(the_trait):
                                text "■ [ut]" style "serum_text_style" xalign 0.0


            transclude


screen trait_list_tooltip(the_traits, given_align = (0.0,0.0), given_anchor = (0.0,0.0), show_unlocks = False):
    vbox:
        align given_align
        anchor given_anchor
        for trait in the_traits:
            frame:
                background "#0a142688"
                use trait_tooltip(trait, show_unlocks = show_unlocks)

        transclude
        #If you hand the serum tooltip a child it's added to the vBox

screen trait_details(the_trait, given_xanchor = 0.5, given_xalign = 0.5):
    frame:
        background "#444444"
        xfill True
        yfill False
        vbox:
            text the_trait.name style "menu_text_style"
            use aspect_grid(the_trait, given_xanchor, given_xalign)
            if the_trait.positive_slug:
                text "    "  + the_trait.positive_slug style "menu_text_style" color "#98fb98"
            if the_trait.negative_slug:
                text "    "  + the_trait.negative_slug style "menu_text_style" color "#ff0000"

screen aspect_grid(aspect_object, given_xanchor = 0.5, given_xalign = 0.5): #Note: This can be given either a trait or a serum, since both have aspect info.
    default tsize = 16
    frame:
        background None
        xanchor given_xanchor
        xalign given_xalign
        margin 0,0,0,0
        padding 10,0,10,0

        grid 7 1 xfill True:
            if aspect_object.tier > mc.business.max_serum_tier:
                text "Tier: {color=#fb6868}[aspect_object.tier]{/color}" style "menu_text_style" size tsize
            else:
                text "Tier: [aspect_object.tier]" style "menu_text_style" size tsize
            text "Men: [aspect_object.mental_aspect]" style "menu_text_style" size tsize color "#387aff"
            text "Phy: [aspect_object.physical_aspect]" style "menu_text_style" size tsize color "#00AA00"
            text "Sex: [aspect_object.sexual_aspect]" style "menu_text_style" size tsize color "#FFC0CB"
            text "Med: [aspect_object.medical_aspect]" style "menu_text_style" size tsize color "#FFFFFF"
            text "Flaw: [aspect_object.flaws_aspect]" style "menu_text_style" size tsize color "#AAAAAA"
            text "Attn: [aspect_object.attention]" style "menu_text_style" size tsize color "#FF6249"

screen contract_aspect_grid(contract):
    python:
        non_zero_aspects = 0
        if contract.mental_aspect > 0:
            non_zero_aspects += 1
        if contract.physical_aspect > 0:
            non_zero_aspects += 1
        if contract.sexual_aspect > 0:
            non_zero_aspects += 1
        if contract.medical_aspect > 0:
            non_zero_aspects += 1
        time_left = contract.contract_length
        if contract.contract_started:
            time_left = contract.contract_length - contract.time_elapsed

    hbox:
        spacing 10
        if contract.contract_started:
            text "Doses: [contract.serum_count]/[contract.amount_desired]" style "menu_text_style" size 16 color "#fbff00"
        else:
            text "Doses Required: [contract.amount_desired]" style "menu_text_style" size 16 color "#fbff00"
        text "Payout: ${payout:,}".format(payout = __builtin__.int(contract.price_per_dose * contract.amount_desired)) style "menu_text_style" size 16 color "#85bb65"
        text "Deliver in: [time_left] days" style "menu_text_style" size 16 color "#BBBBBB"

    grid non_zero_aspects+2 1 xfill True:
        if contract.mental_aspect > 0:
            text "Men: >=[contract.mental_aspect]" style "menu_text_style" size 16 color "#387aff"
        if contract.physical_aspect > 0:
            text "Phy: >=[contract.physical_aspect]" style "menu_text_style" size 16 color "#00AA00"
        if contract.sexual_aspect > 0:
            text "Sex: >=[contract.sexual_aspect]" style "menu_text_style" size 16 color "#FFC0CB"
        if contract.medical_aspect > 0:
            text "Med: >=[contract.medical_aspect]" style "menu_text_style" size 16 color "#FFFFFF"
        text "Flaw: <=[contract.flaws_aspect]" style "menu_text_style" size 16 color "#AAAAAA"
        text "Attn: <=[contract.attention]" style "menu_text_style" size 16 color "#FF6249"
