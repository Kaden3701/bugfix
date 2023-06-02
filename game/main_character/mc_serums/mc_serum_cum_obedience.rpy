#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_cum_obedience = MC_Serum_Trait("Serum: Seed of Submission",
    "Obedience Enhancer",
    "cum",
    [perk_cum_obedience_small, perk_cum_obedience_med, perk_cum_obedience_large],
    [perk_cum_obedience_advance_req_01],
    "perk_cum_obedience_upg_label",
    upg_string = "Master the Stress Inhibitors trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_cum_obedience)

init 1 python:  #Associated Perks
    def perk_cum_obedience_small_on_cum(the_person, the_place, add_to_log = True):
        if the_person.obedience < 150:
            the_person.change_obedience(2, add_to_log = add_to_log)
            if the_person.obedience > 150:
                the_person.obedience = 150
        return

    def perk_cum_obedience_med_on_cum(the_person, the_place, add_to_log = True):
        if the_person.obedience < 200:
            the_person.change_obedience(4, add_to_log = add_to_log)
            if the_person.obedience > 200:
                the_person.obedience = 200
        the_person.increase_opinion_score(the_place, max_value = 0, add_to_log = add_to_log)
        return

    def perk_cum_obedience_large_on_cum(the_person, the_place, add_to_log = True):
        if the_person.obedience < 250:
            the_person.change_obedience(6, add_to_log = add_to_log)
            if the_person.obedience > 250:
                the_person.obedience = 250
        the_person.increase_opinion_score(the_place, max_value = 2, add_to_log = add_to_log)
        if not the_person.is_in_trance:
            the_person.increase_trance(show_dialogue = True, reset_arousal = False, add_to_log = add_to_log)
        return

    def perk_cum_obedience_small():
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 2 obedience, to a maximum of 150.", usable = False, cum_func = perk_cum_obedience_small_on_cum)

    def perk_cum_obedience_med():
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 4 obedience, to a maximum of 200 and if disliked, her opinion of the cumshot is shifted positively.", usable = False, cum_func = perk_cum_obedience_med_on_cum)

    def perk_cum_obedience_large():
        return Ability_Perk(description = "When exposed to your cum, girls gain up to 6 obedience, to a maximum of 250 and her opinion of the cumshot is shifted positively. If she isn't already in a trance, she is put in one.", usable = False, cum_func = perk_cum_obedience_large_on_cum)



    def perk_cum_obedience_advance_req_01():
        the_serum = find_serum_trait_by_name("Stress Inhibitors")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_cum_obedience_upg_label(the_person):
    the_person "Research with the Stress Inhibitors serum trait has yielded some interesting results that I was able to apply to the Seed of Submission serum."
    the_person "Adding Stress Inhibitors to your semen should provide for a more immediate and stronger reaction to contact with your semen."
    the_person "Women who are exposed to it will become more compliant and even view more favorably the act that led to the exposure, providing easier repeat exposures."
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return
