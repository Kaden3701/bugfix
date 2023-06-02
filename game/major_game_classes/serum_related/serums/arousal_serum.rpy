init python:
    def arousal_serum_function_on_turn(the_person, the_serum, add_to_log):
        if the_person.arousal < the_person.suggestibility:
            the_person.change_arousal(__builtin__.min(15, the_person.suggestibility - the_person.arousal),add_to_log = False)
        return

    arousal_serum_trait = SerumTrait(name = "Female Viagra",
        desc = "Reverse engineered from the pills you ordered. Increases arousal over time, maxing out based on suggestibility.",
        positive_slug = "+15 Arousal over time",
        negative_slug = "",
        research_added = 20,
    #     slots_added = a_number,
    #     production_added = a_number,
    #     duration_added = a_number,
        base_side_effect_chance = 30,
    #        on_apply = essential_oil_function_on_apply,
    #        on_remove = essential_oil_function_on_remove,
        on_turn = arousal_serum_function_on_turn,
    #     on_day = a_function,
    #     requires = [list_of_other_traits],
        tier = 2,
        start_researched =  True,
        research_needed = 800,
        clarity_cost = 1000,
        mental_aspect = 4, physical_aspect = 5, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2
    #     exclude_tags = [list_of_other_tags],
    #     is_side_effect = a_bool)
        )
