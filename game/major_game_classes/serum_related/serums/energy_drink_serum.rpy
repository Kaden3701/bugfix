init -1 python:
    def energy_drink_serum_on_apply(the_person, the_serum, add_to_log):
        the_person.change_energy(20, add_to_log = add_to_log)
        return

    def energy_drink_serum_on_remove(the_person, the_serum, add_to_log):
        the_person.change_energy(-20, add_to_log = add_to_log)
        return

    def energy_drink_serum_on_turn(the_person, the_serum, add_to_log):
        the_person.change_energy(20, add_to_log = add_to_log)
        return

    def energy_drink_serum_on_day(the_person, the_serum, add_to_log):
        the_person.change_energy(100, add_to_log = add_to_log)
        return

init 1 python:
    energy_drink_serum_trait = SerumTraitMod(name = "Energy Drink",        # The name of the serum
        desc = "B vitamins, caffeine, and blue raspberry flavoring combine to back a basic energy drink",                                          # Make up something about how it works.
        positive_slug = "+20 energy per turn",                              # The green section in the serum design screen
        negative_slug = "-1 serum duration",                                         # The red section in the serum design screen
        research_added = 30,                                         # Extra research required to develop the protoype
        slots_added = 0,                                            # IF it adds any additional serum trait slots. Usually No
        production_added = 0,                                       # If it adds production time
        duration_added = -1,                                         # IF it makes the final serum last longer or shorter.
        base_side_effect_chance = 0,                                # %Chance of side effects without any mastery
        clarity_added = 0,                                          # Clarity requirement added to develop serum using this trait
        on_apply = energy_drink_serum_on_apply,                               # Function to run when this trait applies
        on_remove = energy_drink_serum_on_remove,                             # Function to run when this trait wears off
        on_turn = energy_drink_serum_on_turn,                                 # Function to run every turn this trait is active
        on_day = energy_drink_serum_on_day,                                   # Function to run if person sleeps while under the effects
        requires = None,                                            # If it requires another serum to be researched first
        tier = 99,                                                   # Use 0-3
        start_researched = False,                                   # If trait is already researched
        research_needed=50,                                         # Research required to unlock trait
        exclude_tags="Energy",                                          # Traits with similar  tags cannot combine. Currently "Production", "Suggest", "Energy", "Nanobots"
        is_side_effect = False,                                     # IF this trait is actually a side effect and not researchable
        clarity_cost = 50,                                          # Cost in clarity to begin researching this trait
        start_unlocked = False,                                     # IF this trait does not require clarity to unlock
        start_enabled = True,                                       # MOD function. if False, players MUST enable the serum in the mod options menu from MC bedroom.
        mental_aspect = 1,                                          # The following 5 aspects govern serum value for contracts
        physical_aspect = 1,
        sexual_aspect = 0,
        medical_aspect = 0,
        flaws_aspect = 0,
        attention = 0)                                              # How much attention this serum trait generates for story purposes.


# # any label that starts with serum_mod is added to the serum mod list
# label serum_mod_energy_drink_serum_trait(stack):
#     python:
#         add_energy_drink_serum()
#         execute_hijack_call(stack)
#     return
