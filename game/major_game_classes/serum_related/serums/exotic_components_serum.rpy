# Exotic Ingredients Serum by RogueKnightUK
init -1 python:
    def add_exotic_components_serum():
        exotic_components = SerumTraitMod(name = "Exotic Ingredients",
            desc = "Exotic sounding ingredients from unlikely sources ranging from unheard tree saps to rare flower products give the customers the idea that this serum must be very special indeed, and increase its sale value accordingly. There is no change to the effects of the serum.",
            positive_slug = "",
            negative_slug = "",
            research_added = 100,
            base_side_effect_chance = 1,
            requires = [basic_med_app, improved_serum_prod],
            tier = 1,
            research_needed = 300,
            clarity_cost = 300,
            mental_aspect = 4, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = -1, attention = 0)


# any label that starts with serum_mod is added to the serum mod list
label serum_mod_exotic_components_serum_trait(stack):
    python:
        add_exotic_components_serum()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
