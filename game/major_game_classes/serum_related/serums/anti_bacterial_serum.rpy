init -1 python:
    def anti_biotics_trait_on_apply(the_person, the_serum, add_to_log):
        the_person.change_happiness(2, add_to_log = add_to_log)
        return

    def add_anti_biotics_serum():
        anti_biotics_trait = SerumTraitMod(name = "Anti-Biotics",
                desc = "Normal medical serum that combats bacterial infections.",
                positive_slug = "Permanent +2 Happiness",
                negative_slug = "",
                research_added = 20,
        #     slots_added = a_number,
        #     production_added = a_number,
        #     duration_added = a_number,
                base_side_effect_chance = 5,
                on_apply = anti_biotics_trait_on_apply,
        #     on_remove =trait_function_on_remove,
        #     on_turn = trait_function_on_turn,
        #     on_day = a_function,
                requires = [basic_med_app],
                tier = 1,
                start_researched =  False,
                research_needed = 50,
                clarity_cost = 50,
                mental_aspect = 0, physical_aspect = 2, sexual_aspect = 0, medical_aspect = 4, flaws_aspect = 0, attention = 0
        #     exclude_tags = [list_of_other_tags],
        #     is_side_effect = a_bool)
            )

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_anti_biotics_serum_trait(stack):
    python:
        add_anti_biotics_serum()
        execute_hijack_call(stack)
    return
