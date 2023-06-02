init -2 python:
    class SerumDesign(): #A class that represents a design for a serum built up from serum traits.
        @staticmethod
        def build_test_serum(serumtraits, duration = 1):
            serum = SerumDesign("Test Serum")
            if isinstance(serumtraits, SerumTrait):
                serumtraits = [serumtraits]

            for x in serumtraits:
                if isinstance(x, SerumTrait):
                    serum.add_trait(x)

            serum.duration = duration
            return serum

        def __init__(self, name = ""):
            self.name = name
            self.traits = []
            self.side_effects = []

            self.researched = False
            self.unlocked = False
            self.obsolete = False
            self.current_research = 0

            self.research_needed = 0
            self.clarity_needed = 0
            self.slots = 0
            self.production_cost = 0

            self.duration = 0
            self.duration_counter = 0

            self.expires = True #If set to false the serum does not tick up the duration_counter, meaning it will never expire.

            self.effects_dict = {} # A dict that can be used to store information about this serum when appied to people. For example, tracking how much Sluttiness was added so the same amount can be removed at the end of the duration.

            self.mental_aspect = 0
            self.physical_aspect = 0
            self.sexual_aspect = 0
            self.medical_aspect = 0
            self._flaws_aspect = 0
            self.attention_modifier = 0  # is modified by change_attention

        def is_same_design(self, other): #Checks if two serums are the same design (but not necessarily the same _dose_ of that design).
            same = False
            if self.name == other.name:
                if len(self.traits) != len(other.traits):
                    return False
                elif len(self.side_effects) != len(other.side_effects):
                    return False

                same = True #At this point assume this is true unless something else is wrong.
                for trait in self.traits:
                    trait_matched = False
                    for other_trait in other.traits:
                        if trait.is_similar(other_trait):
                            trait_matched = True
                    if not trait_matched:
                        same = False
                        break

                for trait in other.traits:
                    trait_matched = False
                    for other_trait in self.traits:
                        if trait.is_similar(other_trait):
                            trait_matched = True
                            break

                    if not trait_matched:
                        same = False
                        break

                for side_effect in self.side_effects:
                    trait_matched = False
                    for other_side_effect in other.side_effects:
                        if side_effect.is_similar(other_side_effect):
                            trait_matched = True
                            break

                    if not trait_matched:
                        same = False
                        break

                for side_effect in other.side_effects:
                    trait_matched = False
                    for other_side_effect in self.side_effects:
                        if side_effect.is_similar(other_side_effect):
                            trait_matched = True
                            break

                    if not trait_matched:
                        same = False
                        break

            return same

        def reset(self): #Resets the serum to the default serum values.
            self.__init__()

        @property
        def trait_count(self):
            return __builtin__.len(self.traits)

        @property
        def slots_used(self):
            return len([x for x in self.traits if not x.has_tag("Production")])

        @property
        def tier(self):
            return max([x.tier for x in self.traits + self.side_effects] or [0])

        @property
        def attention(self):
            # base attention from traits
            attention = max([x.attention for x in self.traits + self.side_effects] or [0])
            if clinical_testing in self.traits:
                attention -= 1
            attention += self.attention_modifier
            if attention < 0:
                return 0
            return attention

        @property
        def flaws_aspect(self):
            if self._flaws_aspect < 0:
                return 0
            return self._flaws_aspect

        @flaws_aspect.setter
        def flaws_aspect(self, value):
            self._flaws_aspect = value

        @property
        def is_expired(self):
            return self.duration_counter >= self.duration

        @property
        def positive_slug(self):
            return "\n".join([x.positive_slug for x in self.traits + self.side_effects if x.positive_slug])

        @property
        def negative_slug(self):
            return "\n".join([x.negative_slug for x in self.traits + self.side_effect if x.negative_slug])

        @property
        def has_production_trait(self):
            return any(x for x in self.traits if x.has_tag("Production"))

        def can_add_trait(self, trait):
            if trait in self.traits:
                return False
            return not self.__is_tag_excluded(trait)

        def add_trait(self, trait):
            if self.can_add_trait(trait):
                self.traits.append(trait)
                self.__apply_trait_side_effects(trait)

        def can_add_side_effect(self, side_effect):
            if side_effect in self.side_effects:
                return False

            return not self.__is_tag_excluded(side_effect)

        def add_side_effect(self, side_effect):
            if self.can_add_side_effect(side_effect):
                self.side_effects.append(side_effect)
                self.__apply_trait_side_effects(side_effect)

        def remove_trait(self, trait):
            if trait in self.traits:
                self.traits.remove(trait)
                self.__remove_trait_side_effects(trait)

            if trait in self.side_effects:
                self.side_effects.remove(trait)
                self.__remove_trait_side_effects(trait)

        def has_trait(self, trait):
            return any(x for x in self.traits + self.side_effects if x == trait)

        def has_tag(self, the_tag): #Returns true if at least one of the traits has the tag "the_tag". Used to confirm a production trait is included.
            return any(x for x in self.traits if x.has_tag(the_tag))

        def change_attention(self, amount): # can be used to increase or decrease attention of design
            self.attention_modifier += amount

        def run_on_turn(self, the_person, add_to_log = False): #Increases the counter, applies serum effect if there is still some duration left
            if self.duration_counter < self.duration:
                for trait in [x for x in self.traits + self.side_effects if x.on_turn]:
                    trait.run_on_turn(the_person, self, add_to_log)
            if self.expires:
                self.duration_counter += 1

        def run_on_move(self, the_person, add_to_log = False):
            for trait in [x for x in self.traits + self.side_effects if x.on_move]:
                trait.run_on_move(the_person, self, add_to_log)

        def run_on_apply(self, the_person, add_to_log = True):
            self.effects_dict = {} #Ensure this is clear and it isn't a reference to the main dict.
            for trait in [x for x in self.traits + self.side_effects if x.on_apply]:
                trait.run_on_apply(the_person, self, add_to_log)

        def run_on_remove(self, the_person, add_to_log = False):
            for trait in [x for x in self.traits + self.side_effects if x.on_remove]:
                trait.run_on_remove(the_person, self, add_to_log)

        def run_on_day(self, the_person, add_to_log = False):
            for trait in [x for x in self.traits + self.side_effects if x.on_day]:
                trait.run_on_day(the_person, self, add_to_log)

        def add_research(self, amount): #Returns true if "amount" research completes the research
            amount = __builtin__.int(__builtin__.round(amount))
            self.current_research += amount
            if self.current_research >= self.research_needed:
                self.researched = True
                return True
            return False

        def unlock_design(self, pay_clarity = True):
            if pay_clarity:
                mc.spend_clarity(self.clarity_needed)
            self.unlocked = True

        # Called when a serum is finished development.
        # Tests all traits against their side effect chance and adds an effect for any that fail.
        def generate_side_effects(self, add_to_log = True):
            for trait in self.traits:
                if renpy.random.randint(0,100) < trait.side_effect_chance:
                    self.create_side_effect(trait.name, add_to_log)

        # Add random side effect to a serum
        def create_side_effect(self, cause, add_to_log = True):
            side_effect = get_random_from_list([x for x in list_of_side_effects if self.can_add_side_effect(x)])
            if side_effect:
                self.add_side_effect(side_effect)
                if add_to_log:
                    mc.log_event("{} developed side effect {} due to {}".format(self.name, side_effect.name, cause), "float_text_blue")


        def __is_tag_excluded(self, trait):
            disallowed_tags = []
            map(disallowed_tags.extend, [x.exclude_tags for x in self.traits + self.side_effects])
            return any(x for x in trait.exclude_tags if x in disallowed_tags)

        def __apply_trait_side_effects(self, trait):
            self.research_needed += trait.research_added
            self.clarity_needed += trait.clarity_added
            self.slots += trait.slots
            self.production_cost += trait.production_cost
            self.duration += trait.duration

            self.mental_aspect += trait.mental_aspect
            self.physical_aspect += trait.physical_aspect
            self.sexual_aspect += trait.sexual_aspect
            self.medical_aspect += trait.medical_aspect
            self._flaws_aspect += trait.flaws_aspect

        def __remove_trait_side_effects(self, trait):
            self.research_needed -= trait.research_added
            self.clarity_needed -= trait.clarity_added
            self.slots -= trait.slots
            self.production_cost -= trait.production_cost
            self.duration -= trait.duration

            self.mental_aspect -= trait.mental_aspect
            self.physical_aspect -= trait.physical_aspect
            self.sexual_aspect -= trait.sexual_aspect
            self.medical_aspect -= trait.medical_aspect
            self._flaws_aspect -= trait.flaws_aspect
