# Behavior Adjustment Serum by Starbuck

init -1 python:
    def behavior_adjustment_on_turn(the_person, the_serum, add_to_log):
        if the_person.obedience_tier < 5:
            suggestion_bonus = (1 + the_person.suggest_tier - the_person.obedience_tier) * 10
            if renpy.random.randint(0, 100) < 20 + suggestion_bonus - (the_person.get_opinion_score("taking control") * 5):
                the_person.change_stats(obedience = 1, add_to_log = add_to_log)

    behavior_adjustment_ther = SerumTraitMod(name = "Behavior Adjustment",
            desc = "Slowly increases obedience. Strong wills can resist it, but it increases effect based on suggestibility.",
            positive_slug = "Slowly increases obedience based on suggestibility",
            negative_slug = "",
            research_added = 100,
            base_side_effect_chance = 20,
            on_turn = behavior_adjustment_on_turn,
            tier = 1,
            start_researched =  False,
            research_needed = 500,
            clarity_cost = 500,
            mental_aspect = 2, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 0, attention = 2
        )
