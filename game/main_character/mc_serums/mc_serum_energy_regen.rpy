#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_energy_regen = MC_Serum_Trait("Serum: Energy Regeneration",
    "Caffeine Infusion",
    "energy",
    [perk_energy_regen_small, perk_energy_regen_med, perk_energy_regen_large],
    [perk_energy_regen_advance_req_01],
    "perk_energy_regen_upg_label",
    upg_string = "Master the Refined Stimulants trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_energy_regen)

init 1 python:  #Associated Perks
    def perk_energy_regen_small_update():
        mc.change_energy(20)
        return

    def perk_energy_regen_med_update():
        mc.change_energy(50)
        return

    def perk_energy_regen_large_update():
        mc.change_energy(mc.max_energy)
        return

    def perk_energy_regen_small():
        return Ability_Perk(description = "You naturally regenerate a small amount of energy throughout the day.", usable = False, update_func = perk_energy_regen_small_update)

    def perk_energy_regen_med():
        return Ability_Perk(description = "You naturally regenerate a moderate amount of energy throughout the day. ", usable = False, update_func = perk_energy_regen_med_update)

    def perk_energy_regen_large():
        return Ability_Perk(description = "You naturally regenerate a large amount of energy throughout the day. During sex, only lose erection when low on Energy.", usable = False, update_func = perk_energy_regen_large_update)

    def perk_energy_regen_advance_req_01():
        the_serum = find_serum_trait_by_name("Refined Stimulants")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_energy_regen_upg_label(the_person):
    the_person "Research with the Refined Stimulants serum trait has yielded some interesting results that I was able to apply to the Energy Regeneration serum."
    the_person "Taking purer stimulants should reduce the side effects and allow for better dosing. You may find yourelf with increased energy in all sorts of situations now."
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return
