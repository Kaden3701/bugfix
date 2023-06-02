#The very first Mc serum trait. Regenerates extra energy for the MC every turn.



init 2 python:
    mc_serum_aura_arousal = MC_Serum_Trait("Serum: Aura of Arousal",
        "Distilled Aphrodisiac",
        "aura",
        [perk_aura_arousal_small, perk_aura_arousal_med, perk_aura_arousal_large],
        [perk_aura_arousal_advance_req_01],
        "perk_aura_arousal_upg_label",
        upg_string = "Master the Pleasure Center Stimulator trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_aura_arousal)

init 1 python:  #Associated Perks
    def perk_aura_arousal_small_update():
        for person in get_nearby_people():
            if person.arousal_perc < 25:
                person.change_arousal(1, add_to_log = False)
        return

    def perk_aura_arousal_med_update():
        for person in get_nearby_people():
            if person.arousal_perc < 25:
                person.change_arousal(2, add_to_log = False)
            elif person.arousal_perc < 50:
                person.change_arousal(1, add_to_log = False)
        return

    def perk_aura_arousal_large_update():
        for person in get_nearby_people():
            if person.arousal_perc < 25:
                person.change_arousal(3, add_to_log = False)
            elif person.arousal_perc < 75:
                person.change_arousal(2, add_to_log = False)
        return

    def perk_aura_arousal_small():
        return Ability_Perk(description = "Girls near you slowly gain up to 25 arousal.", usable = False, update_func = perk_aura_arousal_small_update)

    def perk_aura_arousal_med():
        return Ability_Perk(description = "Girls near you slowly gain up to 50 arousal, and never find vaginal and anal positions boring.", usable = False, update_func = perk_aura_arousal_med_update)

    def perk_aura_arousal_large():
        return Ability_Perk(description = "Girls near you slowly gain up to 75 arousal, and never find any sexual positions boring.", usable = False, update_func = perk_aura_arousal_large_update)

    def perk_aura_arousal_advance_req_01():
        the_serum = find_serum_trait_by_name("Pleasure Center Stimulator")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_aura_arousal_upg_label(the_person):
    the_person "Research with the Pleasure Center Enhancer serum trait has yielded some interesting results that I was able to apply to the Aura of Arousal serum."
    the_person "By adding elements of the Pleasure Center Enhancer, women you are having sex with find even mundane positions more exciting."
    mc.name "Sounds great. I'll give a try when I have the chance."
    return
