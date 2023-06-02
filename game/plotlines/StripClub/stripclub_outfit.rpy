init -2 python:
    class StripClubOutfit():
        def __init__(self, the_outfit):
            self.outfit = the_outfit.get_copy()

            self.full_outfit_flag = False #True if this uniform should belong in the overwear set of the appropriate wardrobes
            self.overwear_flag = False
            self.underwear_flag = False

            self.stripper_flag = False #True if this uniform should belong to this departments wardrobe.
            self.waitress_flag = False
            self.bdsm_flag = False
            self.manager_flag = False
            self.mistress_flag = False

        def set_full_outfit_flag(self, state):
            self.full_outfit_flag = state

        def set_overwear_flag(self, state):
            self.overwear_flag = state

        def set_underwear_flag(self, state):
            self.underwear_flag = state


        def set_stripper_flag(self, state):
            self.stripper_flag = state

        def set_waitress_flag(self, state):
            self.waitress_flag = state

        def set_bdsm_flag(self, state):
            self.bdsm_flag = state

        def set_manager_flag(self, state):
            self.manager_flag = state

        def set_mistress_flag(self, state):
            self.mistress_flag = state


        def can_toggle_full_outfit_state(self):
            return True

        def can_toggle_overwear_state(self):
            return True

        def can_toggle_underwear_state(self):
            return True
