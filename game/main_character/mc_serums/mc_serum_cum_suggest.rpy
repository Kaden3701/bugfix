#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_cum_suggest = MC_Serum_Trait("Serum: Cum of Change",
    "Off Label Pharmaceuticals",
    "cum",
    [perk_cum_suggest_small, perk_cum_suggest_med, perk_cum_suggest_large],
    [perk_cum_suggest_advance_req_01],
    "perk_cum_suggest_upg_label",
    upg_string = "Master the Mind Control Agent trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_cum_suggest)

init 1 python:  #Associated Perks
    def perk_cum_suggest_small_on_cum(the_person, the_place, add_to_log = True):
        the_person.change_modded_suggestibility(1, max_amt = 10, add_to_log = add_to_log)
        return

    def perk_cum_suggest_med_on_cum(the_person, the_place, add_to_log = True):
        the_person.change_modded_suggestibility(2, max_amt = 20, add_to_log = add_to_log)
        return

    def perk_cum_suggest_large_on_cum(the_person, the_place, add_to_log = True):
        the_person.change_modded_suggestibility(2, max_amt = 30, add_to_log = add_to_log)
        return

    def perk_cum_suggest_small():
        return Ability_Perk(description = "When exposed to your cum, increases her suggestibility by 1% to a maximum of 10%.", usable = False, cum_func = perk_cum_suggest_small_on_cum)

    def perk_cum_suggest_med():
        return Ability_Perk(description = "When exposed to your cum, increases her suggestibility by 2% to a maximum of 20%.", usable = False, cum_func = perk_cum_suggest_med_on_cum)

    def perk_cum_suggest_large():
        return Ability_Perk(description = "When exposed to your cum, increases her suggestibility by 2% to a maximum of 30%.", usable = False, cum_func = perk_cum_suggest_large_on_cum)



    def perk_cum_suggest_advance_req_01():
        the_serum = find_serum_trait_by_name("Mind Control Agent")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_cum_suggest_upg_label(the_person):
    the_person "Research with the Mind Control Agent serum trait has yielded some interesting results that I was able to apply to the Cum of Change serum."
    the_person "Do... do I really need to explain how adding elements of mind control makes the serum more effective?"
    mc.name "I suppose not. Thank you, [the_person.title], I'll give it a try sometime."
    return
