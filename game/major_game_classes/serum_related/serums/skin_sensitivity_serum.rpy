# Skin sensitivity serum original by Kaden

init 2 python:
    def skin_sensitivity_on_apply(person, the_serum, add_to_log = True):
        test_outfit = person.planned_outfit.get_copy()
        cloth = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
        if not cloth:
            return # nothing to strip
        test_outfit.remove_clothing(cloth)
        if not person.judge_outfit(test_outfit):
            return # too slutty
        if cloth in person.outfit.upper_body and test_outfit.tits_visible and person.has_taboo("bare_tits"):
            return # won't strip to tits
        if cloth in person.outfit.lower_body and test_outfit.vagina_visible and person.has_taboo("bare_pussy"):
            return # won't strip to vagina
        if test_outfit.underwear_visible and person.has_taboo("underwear_nudity"):
            return # won't strip to underwear

        person.planned_outfit = test_outfit
        person.apply_outfit(person.planned_outfit)

        if add_to_log:
            # she is wearing it and we can see her
            if mc.location == person.location and person.outfit.has_clothing(cloth):
                person.draw_animated_removal(cloth)
                "It seems [person.possessive_title] is affected by the skin sensitivity serum."
            mc.log_event((person.title or person.create_formatted_title("???")) + ": Removed her " + cloth.display_name, "float_text_grey")
        return

    def skin_sensitivity_on_turn(person, the_serum, add_to_log = True):
        if person.location.public:
            person.change_happiness(-2, add_to_log = add_to_log)
        if person.arousal_perc < 50:
            person.change_arousal(5, add_to_log = add_to_log)
        return

    skin_sensitivity_serum_trait = SerumTraitMod(name = "Skin Sensitivity",
        desc = "Heighten the subjects sense of touch. This can lead to increased arousal, but in public it might be frustrating if their clothes are too restrictive.",
        positive_slug = "+5 Arousal/turn, may cause stripping when administered",
        negative_slug = "-2 Happiness/turn in public",
        research_added = 20,
        base_side_effect_chance = 30,
        on_apply = skin_sensitivity_on_apply,
        on_turn = skin_sensitivity_on_turn,
        requires = [clinical_testing],
        tier = 1,
        research_needed = 800,
        clarity_cost = 1000,
        mental_aspect = 3, physical_aspect = 1, sexual_aspect = 4, medical_aspect = 0, flaws_aspect = 0, attention = 2)
