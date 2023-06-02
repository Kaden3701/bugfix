init python:
    def essential_oil_function_on_apply(the_person, the_serum, add_to_log):
        the_person.change_happiness(5, add_to_log = add_to_log)
        return

    def essential_oil_function_on_remove(the_person, the_serum, add_to_log):
        the_person.change_happiness(-5, add_to_log = add_to_log)
        return


    essential_oil_trait = SerumTrait(name = "Essential Oils",
            desc = "Pleasant smell and texture adds greatly to the value of the serum. High chance of negative side effect.",
            positive_slug = "+5 Happiness",
            negative_slug = "",
            research_added = 20,
    #     slots_added = a_number,
    #     production_added = a_number,
    #     duration_added = a_number,
            base_side_effect_chance = 150,
            on_apply = essential_oil_function_on_apply,
            on_remove = essential_oil_function_on_remove,
    #     on_turn = ovulation_function_on_turn,
    #     on_day = a_function,
    #     requires = [list_of_other_traits],
            tier = 0,
            start_researched =  True,
            research_needed = 1500,
            clarity_cost = 1000,
            mental_aspect = 6, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 2, flaws_aspect = 0, attention = 0
    #     exclude_tags = [list_of_other_tags],
    #     is_side_effect = a_bool)
        )
