#This serum is designed to enhance MC's performance at work. Note, some employees may find MCs increased performance sexy, particularly if they also like working and their departments.

init 2 python:
    mc_serum_workaholic = MC_Serum_Trait("Serum: Workaholic",
    "Clinical Testing Procedures",
    "energy",
    [perk_workaholic_small, perk_workaholic_med, perk_workaholic_large],
    [perk_workaholic_advance_req_01],
    "perk_workaholic_upg_label",
    upg_string = "Master the Quick Release Nootropics trait to upgrade this serum formula.",
    on_apply = perk_serum_workaholic_on_apply,
    on_remove = perk_serum_workaholic_on_remove)

    list_of_mc_traits.append(mc_serum_workaholic)

init 1 python:  #Associated Perks
    def perk_workaholic_small_update():
        pass
        return

    def perk_workaholic_med_update():
        if mc.is_at_work:
            mc.change_energy(20)
        return

    def perk_workaholic_large_update():
        if mc.is_at_work:
            mc.change_energy(50)
        return

    def perk_serum_workaholic_on_apply():
        bonus = mc_serum_workaholic.trait_tier
        if not day% 7 >= 5:
            bonus *= 2
        perk_system.add_stat_perk(Stat_Perk(description = "Your workaholic serum has increased all your work related stats.", hr_bonus = bonus, market_bonus = bonus, research_bonus = bonus, production_bonus = bonus, supply_bonus = bonus, skill_cap = bonus, bonus_is_temp = True, duration = 2), "Workaholic Stats")
        return

    def perk_serum_workaholic_on_remove():
        perk_system.remove_perk("Workaholic Stats")
        return

    def perk_workaholic_small():
        return Ability_Perk(description = "You have slightly increased work stats. Bonus doubles on the weekend.", usable = False, update_func = perk_workaholic_small_update)

    def perk_workaholic_med():
        return Ability_Perk(description = "You have moderately increased work stats and some gain energy while working. Bonus doubles on the weekend.", usable = False, update_func = perk_workaholic_med_update)

    def perk_workaholic_large():
        return Ability_Perk(description = "You have increased work stats and gain energy while working. Bonus doubles on the weekend.", usable = False, update_func = perk_workaholic_large_update)

    def perk_workaholic_advance_req_01():
        the_serum = find_serum_trait_by_name("Quick Release Nootropics")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_workaholic_upg_label(the_person):
    the_person "Research with the Quick Release Nootropics serum trait has yielded some interesting results that I was able to apply to the Workaholic serum."
    the_person "Ever hear the saying, work smarter, not harder? Turns out there is truth to that. "
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return
