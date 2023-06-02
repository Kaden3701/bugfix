# Massive Pregnancy Decelerator (Original by Kaden)
init -1 python:
    def massive_pregnancy_decelerator_on_turn(the_person, the_serum, add_to_log):
        if not the_person.is_pregnant:
            return

        if the_person.event_triggers_dict.get("preg_announce_day", day) > day:
            the_person.event_triggers_dict["preg_announce_day"] = the_person.event_triggers_dict.get("preg_announce_day", day) + 1
        if the_person.event_triggers_dict.get("preg_tits_date", day) > day:
            the_person.event_triggers_dict["preg_tits_date"] = the_person.event_triggers_dict.get("preg_tits_date", day) + 1
        if the_person.event_triggers_dict.get("preg_transform_day", day) > day:
            the_person.event_triggers_dict["preg_transform_day"] = the_person.event_triggers_dict.get("preg_transform_day", day) + 1
        if the_person.event_triggers_dict.get("preg_finish_announce_day", day) > day:
            the_person.event_triggers_dict["preg_finish_announce_day"] = the_person.event_triggers_dict.get("preg_finish_announce_day", day) + 1
        return

    def add_massive_pregnancy_decelerator():
        massive_pregnancy_decelerator_serum_trait = SerumTraitMod(name = "Pregnancy Hormone Inhibitors",
            desc = "Clamps down on natural pregnancy hormone production. Massively decreases the pace at which a pregnancy will progress.",
            positive_slug = "-1 Pregnancy Progress per Turn",
            negative_slug = "",
            research_added = 300,
            base_side_effect_chance = 80,
            on_turn = massive_pregnancy_decelerator_on_turn,
            requires = [pregnancy_decelerator_trait],
            tier = 3,
            research_needed = 1400,
            exclude_tags = "Pregnancy",
            clarity_cost = 1800,
            mental_aspect = 0, physical_aspect = 9, sexual_aspect = 0, medical_aspect = 3, flaws_aspect = 0, attention = 4)
        return

# any label that starts with serum_mod is added to the serum mod list
label serum_mod_massive_pregnancy_decelerator_trait(stack):
    python:
        add_massive_pregnancy_decelerator()
        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return
