init -1 python:
    def skin_improvement_trait_on_apply(the_person, the_serum, add_to_log):
        the_person.change_happiness(5, add_to_log = add_to_log)

    def add_skin_improvement_serum():
        skin_improvement_trait = SerumTraitMod(name = "Skin Improvement",
                desc = "Normal medical serum that improves skin condition (prevent acne / reduces pigment spots).",
                positive_slug = "Permanent +5 Happiness",
                negative_slug = "",
                research_added = 50,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 5,
                on_apply = skin_improvement_trait_on_apply,
        #     on_remove =trait_function_on_remove,
        #     on_turn = trait_function_on_turn,
        #     on_day = a_function,
                requires = [clinical_testing],
                tier = 2,
                start_researched =  False,
                research_needed = 250,
                clarity_cost = 250,
                mental_aspect = 1, physical_aspect = 6, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_skin_improvement_serum_trait(stack):
    python:
        add_skin_improvement_serum()
        execute_hijack_call(stack)
    return
