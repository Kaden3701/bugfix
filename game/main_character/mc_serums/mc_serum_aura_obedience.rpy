#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_aura_obedience = MC_Serum_Trait("Serum: Aura of Compliance",
        "Low Concentration Sedatives",
        "aura",
        [perk_aura_obedience_small, perk_aura_obedience_med, perk_aura_obedience_large],
        [perk_aura_obedience_advance_req_01],
        "perk_aura_obedience_upg_label",
        upg_string = "Master the Obedience Enhancer trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_aura_obedience)

init 1 python:  #Associated Perks
    def perk_aura_obedience_small_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_med_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(2, add_to_log = True)
            elif person.obedience < 200:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_large_update():
        for person in get_nearby_people():
            if person.obedience < 150:
                person.change_obedience(3, add_to_log = True)
            elif person.obedience < 200:
                person.change_obedience(2, add_to_log = True)
            elif person.obedience < 250:
                person.change_obedience(1, add_to_log = True)
        return

    def perk_aura_obedience_small():
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 150 and never refuse small favors.", usable = False, update_func = perk_aura_obedience_small_update)

    def perk_aura_obedience_med():
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 200 and never refuse small or medium favors, and have +10 obedience during sex.", usable = False, update_func = perk_aura_obedience_med_update)

    def perk_aura_obedience_large():
        return Ability_Perk(description = "Girls near you slowly gain obedience up to 250 and never refuse any favors, have +20 obedience during sex, and never refuse a sex position based on her opinions.", usable = False, update_func = perk_aura_obedience_large_update)

    def perk_aura_obedience_advance_req_01():
        the_serum = find_serum_trait_by_name("Obedience Enhancer")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_aura_obedience_upg_label(the_person):
    the_person "Research with the Obedience Enhancer serum trait has yielded some interesting results that I was able to apply to the Aura of Compliance serum."
    the_person "I updated the serum formula accordingly, and if you take it now you might find girls nearby fall in line a lot faster and are more compliant during sexual activity."
    mc.name "Sounds great. I'll give a try when I have the chance."
    return
