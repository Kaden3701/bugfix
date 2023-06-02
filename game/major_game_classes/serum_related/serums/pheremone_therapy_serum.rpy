# Pheremone Therapy Serum by Starbuck

init -1 python:
    def pheremone_therapy_on_apply(the_person, the_serum, add_to_log):
        change_amount = the_person.change_slut(15, add_to_log = add_to_log)
        the_serum.effects_dict["pheromone_therapy_change"] = change_amount

    def pheremone_therapy_on_remove(the_person, the_serum, add_to_log):
        change_amount = the_serum.effects_dict.get("pheromone_therapy_change", 15)
        the_person.change_slut(-(15 if change_amount is None else change_amount), add_to_log = add_to_log)

    pher_ther = SerumTraitMod(name = "Pheromone Therapy",
        desc = "By mimicking pheromones found in closely related animals, this serum can recreate feelings of going into heat in women. No effect when girl at maximum sluttiness.",
        positive_slug = "+15 Sluttiness",
        negative_slug = "",
        research_added = 200,
    #     slots_added = a_number,
    #     production_added = a_number,
    #     duration_added = a_number,
        base_side_effect_chance = 20,
        on_apply = pheremone_therapy_on_apply,
        on_remove = pheremone_therapy_on_remove,
    #     on_turn = a_function,
    #     on_day = a_function,
    #     requires = [list_of_other_traits],
        tier = 2,
        start_researched =  False,
        research_needed = 800,
        clarity_cost = 1500,
        mental_aspect = 5, physical_aspect = 0, sexual_aspect = 5, medical_aspect = 0, flaws_aspect = 0, attention = 2,
        start_enabled = False
    #     exclude_tags = [list_of_other_tags],
    #     is_side_effect = a_bool)
        )
