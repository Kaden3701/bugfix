#Extra Serum trait side effects. (Original by Computant)

init 5 python:
    list_of_instantiation_labels.append("instantiate_more_side_effect_traits")

init 2 python:
    ## uncontrollable_arousal_side_effect_functions ##
    def uncontrollable_arousal_side_effect_on_apply(person, the_serum, add_to_log):
        change_amount = person.change_slut(20, add_to_log = add_to_log)
        the_serum.effects_dict["uncontrollable_arousal_effect"] = change_amount

    def uncontrollable_arousal_side_effect_on_remove(person, the_serum, add_to_log):
        change_amount = the_serum.effects_dict.get("uncontrollable_arousal_effect", 20)
        person.change_slut(-(20 if change_amount is None else change_amount), add_to_log = add_to_log)

    ## tryptamine_side_effect_functions ##
    def tryptamine_side_effect_on_apply(person, the_serum, add_to_log):
        change_amount = person.change_obedience(10, add_to_log = add_to_log)
        the_serum.effects_dict["tryptamine_effect"] = change_amount

    def tryptamine_side_effect_on_remove(person, the_serum, add_to_log):
        change_amount = the_serum.effects_dict.get("tryptamine_effect", 10)
        person.change_obedience(-(10 if change_amount is None else change_amount), add_to_log = add_to_log)

    ## oxytocin_side_effect_functions ##
    def oxytocin_side_effect_on_turn(person, the_serum, add_to_log):
        person.change_love(1, max_modified_to = 40, add_to_log = False)

    def skin_sensitivity_side_effect_on_turn(person, the_serum, add_to_log):
        person.change_arousal(5, add_to_log = add_to_log)

    uncontrollable_arousal_side_effect = SerumTrait(name = "Uncontrollable Arousal",
        desc = "An unintended interaction produces a sudden and noticeable spike in the recipient's promiscuity, making them more agreeable to lewd interactions.",
        positive_slug = "+20 Sluttiness for duration",
        negative_slug = "",
        on_apply = uncontrollable_arousal_side_effect_on_apply,
        on_remove = uncontrollable_arousal_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 5, physical_aspect = 0, sexual_aspect = 7, medical_aspect = 0, flaws_aspect = 1, attention = 2)

    tryptamine_side_effect = SerumTrait(name = "Tryptamine Induction",
        desc = "An unintended interaction produces a sudden and noticeable degradation of the subject's free will, making them suspectable to suggestion for the duration.",
        positive_slug = "+10 Obedience for duration",
        negative_slug = "",
        on_apply = tryptamine_side_effect_on_apply,
        on_remove = tryptamine_side_effect_on_remove,
        is_side_effect = True,
        mental_aspect = 7, physical_aspect = 0, sexual_aspect = 0, medical_aspect = 0, flaws_aspect = 1, attention = 2)

    oxytocin_side_effect = SerumTrait(name = "Oxytocin Increment",
        desc = "An unintended interaction produces a sudden and lasting emotional connection to a person, but only when they have no deep connection already.",
        positive_slug = "Permanent +1 Love/Turn when Love < 40",
        negative_slug = "",
        on_turn = oxytocin_side_effect_on_turn,
        is_side_effect = True,
        mental_aspect = 3, physical_aspect = 0, sexual_aspect = 1, medical_aspect = 0, flaws_aspect = 1, attention = 1)

label instantiate_more_side_effect_traits(): #Creates all of the default LR2 serum trait objects.
    python:
        list_of_side_effects.append(uncontrollable_arousal_side_effect)
        list_of_side_effects.append(tryptamine_side_effect)
        list_of_side_effects.append(oxytocin_side_effect)
    return
