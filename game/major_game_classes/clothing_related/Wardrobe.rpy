init -5 python:
    class Wardrobe(): #A bunch of outfits!
        @staticmethod
        def build_assembled_outfit(outfit_under, outfit_over):
            # print("Assemble outfit: {}".format(outfit_over.name))
            assembled_outfit = outfit_over.get_copy()

            # print("Overwear has {} items".format(outfit_over.item_count))
            # print("Underwear has {} items".format(outfit_under.item_count))

            for upper in [x for x in outfit_under.upper_body if not x.is_extension]:
                assembled_outfit.add_upper(upper.get_copy())

            for lower in [x for x in outfit_under.lower_body if not x.is_extension]:
                assembled_outfit.add_lower(lower.get_copy())

            for feet_wear in [x for x in outfit_under.feet if not x.is_extension]:
                assembled_outfit.add_feet(feet_wear.get_copy())

            for acc in [x for x in outfit_under.accessories if not x.is_extension]:
                assembled_outfit.add_accessory(acc.get_copy())

            assembled_outfit.build_outfit_name()

            # print("Assembled Outfit: {}".format(assembled_outfit.name))
            return assembled_outfit

        @staticmethod
        def generate_random_appropriate_outfit(person, outfit_type = "full", sluttiness_limit = None, opinion_color = None, coloured_underwear = False, swap_bottoms = False, allow_skimpy = False):
            wardrobe_builder = WardrobeBuilder(person)
            (min_slut, max_slut) = WardrobeBuilder.get_clothing_min_max_slut_value(sluttiness_limit or person.sluttiness)
            outfit = wardrobe_builder.build_outfit(outfit_type, max_slut, min_slut)
            return wardrobe_builder.personalize_outfit(outfit, opinion_color = opinion_color, coloured_underwear = coloured_underwear, swap_bottoms = swap_bottoms, allow_skimpy = allow_skimpy)

        def __init__(self,name,outfits = None, underwear_sets = None, overwear_sets = None): #Outfits is a list of Outfit objects, or empty if the wardrobe starts empty
            self.name = name
            self.outfit_sets = outfits #Outfits is now used to hold full outfits.
            self.underwear_sets = underwear_sets #Limited to layer 1 clothing items.
            self.overwear_sets = overwear_sets #Limited to layer 2 and 3 clothing items.
            if outfits is None:
                self.outfit_sets = []
            if underwear_sets is None:
                self.underwear_sets = []
            if overwear_sets is None:
                self.overwear_sets = []

            for outfit in self:
                outfit.restore_all_clothing() #Make sure none of them are stored half off.

        def __copy__(self):
            #TODO: see if adding a .copy() here has A) Fixed any potential bugs and B) not had a major performance impact.
            outfit_copy_list = []
            for outfit in self.outfit_sets:
                outfit_copy_list.append(outfit.get_copy())

            under_copy_list = []
            for underwear in self.underwear_sets:
                under_copy_list.append(underwear.get_copy())

            over_copy_list = []
            for overwear in self.overwear_sets:
                over_copy_list.append(overwear.get_copy())


            return Wardrobe(self.name, outfit_copy_list, under_copy_list, over_copy_list)

        def __iter__(self):
            return iter(self.outfit_sets + self.underwear_sets + self.overwear_sets)

        @property
        def outfit_count(self):
            return sum(1 for _ in self)

        def clear_wardrobe(self):
            for outfit in self:
                outfit.clear()
            self.outfit_sets.clear()
            self.underwear_sets.clear()
            self.overwear_sets.clear()

        def merge_wardrobes(self, other_wardrobe, keep_primary_name = False): #Returns a copy of this wardrobe merged with the other one, with this taking priority for base outfits.
            base_wardrobe = self.__copy__() #This already redefines it's copy method, so we should be fine.
            if isinstance(other_wardrobe, Wardrobe):
                for outfit in other_wardrobe.outfit_sets:
                    base_wardrobe.add_outfit(outfit.get_copy())

                for underwear in other_wardrobe.underwear_sets:
                    base_wardrobe.add_underwear_set(underwear.get_copy())

                for overwear in other_wardrobe.overwear_sets:
                    base_wardrobe.add_overwear_set(overwear.get_copy())

                if not keep_primary_name:
                    base_wardrobe.name = base_wardrobe.name + " + " + other_wardrobe.name
            return base_wardrobe

        def add_outfit(self, the_outfit):
            the_outfit.restore_all_clothing() #Ensure none of the outfits have half-off clothing.
            found = next((x for x in self.outfit_sets if x.name == the_outfit.name), None)
            if found:   # if we already have an outfit with that name, replace it (outfit name must be unique)
                self.outfit_sets.remove(found)
            self.outfit_sets.append(the_outfit)

        def add_underwear_set(self, the_outfit):
            the_outfit.restore_all_clothing()
            found = next((x for x in self.underwear_sets if x.name == the_outfit.name), None)
            if found:   # if we already have an outfit with that name, replace it (outfit name must be unique)
                self.underwear_sets.remove(found)
            self.underwear_sets.append(the_outfit)

        def add_overwear_set(self, the_outfit):
            the_outfit.restore_all_clothing()
            found = next((x for x in self.overwear_sets if x.name == the_outfit.name), None)
            if found:   # if we already have an outfit with that name, replace it (outfit name must be unique)
                self.overwear_sets.remove(found)
            self.overwear_sets.append(the_outfit)

        def remove_outfit(self, outfit):
            for outfit_set in [self.outfit_sets, self.underwear_sets, self.overwear_sets]:
                if isinstance(outfit, basestring):
                    found = next((x for x in outfit_set if x.name == outfit), None)
                    if found:
                        outfit_set.remove(found)
                elif outfit in outfit_set:
                    outfit_set.remove(outfit)

        def pick_random_outfit(self): #TODO: We might be able to pass a reference instead of a copy here now that apply_outfit always takes a copy.
            return get_random_from_list(self.outfit_sets).get_copy() # Get a copy of _any_ full outfit in this character's wardrobe.

        def pick_random_overwear(self):
            return get_random_from_list(self.overwear_sets).get_copy()

        def pick_random_underwear(self):
            return get_random_from_list(self.underwear_sets).get_copy()

        def get_random_appropriate_underwear(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0): #Get an underwear outfit that is considered appropriate (based on underwear sluttiness, not full outfit sluttiness)
            if preferences is None:
                preferences = WardrobePreference()

            if sluttiness_min < 0:
                sluttiness_min = 0

            valid_underwear = [x for x in self.underwear_sets if preferences.evaluate_underwear(x, sluttiness_limit, sluttiness_min)]

            if not valid_underwear: # when we find no valid items, only validate sluttiness score
                valid_underwear = [x for x in self.underwear_sets if x.underwear_slut_score <= sluttiness_limit and x.underwear_slut_score >= sluttiness_min]

            if valid_underwear:
                return renpy.random.choice(valid_underwear).get_copy()
            elif guarantee_output: # If an output is guaranteed we always return an Outfit object (even if it is empty). Otherwise we return None to indicate failure to find something.
                if depth < 2: #Sets an effective recursion limit.
                    return self.get_random_appropriate_underwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

                return self.__pick_underwear_with_lowest_sluttiness() or Outfit("Nothing")
            return None

        def get_random_appropriate_overwear(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0):
            if preferences is None:
                preferences = WardrobePreference()

            if sluttiness_min < 0:
                sluttiness_min = 0

            valid_overwear = [x for x in self.overwear_sets if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]
            if not valid_overwear:  # when we find no valid items, only validate sluttiness score
                valid_overwear = [x for x in self.overwear_sets if x.overwear_slut_score <= sluttiness_limit and x.overwear_slut_score >= sluttiness_min]

            if valid_overwear:
                return renpy.random.choice(valid_overwear).get_copy()
            elif guarantee_output:
                if depth < 2:
                    return self.get_random_appropriate_overwear(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

                return self.__pick_overwear_with_lowest_sluttiness() or Outfit("Nothing")
            return None

        def get_random_appropriate_outfit(self, sluttiness_limit, sluttiness_min = 0, guarantee_output = False, preferences = None, depth = 0):
            if preferences is None:
                preferences = WardrobePreference()

            if sluttiness_min < 0:
                sluttiness_min = 0

            valid_outfits = [x for x in self.outfit_sets if preferences.evaluate_outfit(x, sluttiness_limit, sluttiness_min)]

            # print("Valid outfits: {}".format(len(valid_outfits)))
            if not valid_outfits: # when we find no valid items, only validate sluttiness score
                valid_outfits = [x for x in self.outfit_sets if x.outfit_slut_score <= sluttiness_limit and x.outfit_slut_score >= sluttiness_min]

            if valid_outfits:
                return renpy.random.choice(valid_outfits).get_copy()
            elif guarantee_output:
                if depth < 2:
                    return self.get_random_appropriate_outfit(sluttiness_limit+5, sluttiness_min-5, guarantee_output, preferences, depth + 1)

                #print("Unable to get outfit from wardrobe, pick outfit with lowest sluttiness.")
                return self.__pick_outfit_with_lowest_sluttiness() or Outfit("Nothing")
            return None

        def decide_on_outfit(self, person, sluttiness_modifier = 0.0, slut_limit = 999):
            conservative_score = person.get_opinion_score("conservative outfits") / 20.0
            skimpy_outfit_score = person.get_opinion_score("skimpy outfits") / 20.0
            marketing_score = 0
            # girls working in marketing know they make more sales when wearing a sluttier outfit, so this affects their uniform choice
            if mc.business.is_work_day and male_focused_marketing_policy.is_active and person in mc.business.market_team:
                marketing_score = .05

            target_sluttiness = __builtin__.int(person.sluttiness * (1.0 + skimpy_outfit_score + marketing_score + sluttiness_modifier - conservative_score))
            target_sluttiness = __builtin__.min(target_sluttiness, slut_limit)

            minimum_sluttiness = __builtin__.int(target_sluttiness * .3)

            #print("{} - Decide on outfit -> Target slut {}, min slut {}".format(person.name, target_sluttiness, minimum_sluttiness))

            if not self.outfit_sets and not self.underwear_sets and not self.overwear_sets:
                #print("{} - No available outfits in wardrobe {}, generate random.".format(person.name, self.name))
                #We have nothing to make a outfit out of. Use default builder function.
                return Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = target_sluttiness, swap_bottoms = True, allow_skimpy = person.sluttiness > 50)

            preferences = WardrobePreference(person)

            if self.outfit_sets:
                #We have some full body outfits we might use. 50/50 to use that or a constructed outfit.
                outfit_choice = renpy.random.randint(0,100)
                chance_to_use_full = (50 / 12.0) * __builtin__.len(self.outfit_sets)   # when 12 outfits chance is 50%.
                if chance_to_use_full > 60: # cap at 60%
                    chance_to_use_full = 60

                #If we roll use full or we don't have the parts to make an assembled outfit.
                if outfit_choice < chance_to_use_full or not (self.underwear_sets or self.overwear_sets):

                    full_outfit = self.get_random_appropriate_outfit(target_sluttiness, minimum_sluttiness, preferences = preferences)

                    if not full_outfit: # fallback if we cannot find anything for our sluttiness or preferences
                        # print("{} - Unable to find full outfit in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                        full_outfit = self.__pick_outfit_with_lowest_sluttiness()

                    if not full_outfit and not self == person.wardrobe: # try personal wardrobe if available
                        full_outfit = person.wardrobe.get_random_appropriate_outfit(target_sluttiness, minimum_sluttiness, preferences = preferences)

                    if full_outfit:
                        # print("{} - full outfit: {}".format(self.name, full_outfit.name))
                        return full_outfit.get_copy()

            #If we get to here we are assembling an outfit out of underwear or overwear.
            outfit_over = self.get_random_appropriate_overwear(target_sluttiness, minimum_sluttiness, preferences = preferences)
            outfit_under = None

            if outfit_over:
                slut_limit_remaining = target_sluttiness - outfit_over.overwear_slut_score
                if slut_limit_remaining < 10:
                    slut_limit_remaining = 10  # don't expect 0 sluttiness underwear to be in wardrobe.

                outfit_under = self.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

                if not outfit_under:
                    # print("{} - Unable to find underwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                    outfit_under = self.__pick_underwear_with_lowest_sluttiness()

                if not outfit_under and not self == person.wardrobe: # try personal wardrobe if available
                    # print("{} - Unable to find underwear in wardrobe, pick underwear from person wardrobe.".format(self.name))
                    outfit_under = person.wardrobe.get_random_appropriate_underwear(slut_limit_remaining, preferences = preferences)

                if not outfit_under:
                    # print("{} - Unable to find underwear in wardrobe {}, generate random underwear set.".format(person.name, self.name))
                    outfit_under = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under", sluttiness_limit = slut_limit_remaining)

            else:
                #There are no tops, so we're going to try and get a bottom and use one of the persons tops.
                outfit_under = self.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

                if not outfit_under:
                    # print("{} - Unable to find underwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                    outfit_under = self.__pick_underwear_with_lowest_sluttiness()

                if not outfit_under and not self == person.wardrobe: # try personal wardrobe if available
                    # print("{} - Unable to find underwear in wardrobe, pick underwear from person wardrobe.".format(self.name))
                    outfit_under = person.wardrobe.get_random_appropriate_underwear(target_sluttiness, preferences = preferences)

                if not outfit_under:
                    # print("{} - Unable to find underwear in wardrobe {}, generate random underwear.".format(person.name, self.name))
                    outfit_under = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under", sluttiness_limit = target_sluttiness)

                if outfit_under:
                    slut_limit_remaining = target_sluttiness - outfit_under.underwear_slut_score
                    if slut_limit_remaining < 10:
                        slut_limit_remaining = 10 # don't expect 0 sluttiness overwear to be in personal wardrobe.

                    outfit_over = self.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

                    if not outfit_over:
                        # print("{} - Unable to find overwear in wardrobe {}, pick lowest sluttiness.".format(person.name, self.name))
                        outfit_over = self.__pick_overwear_with_lowest_sluttiness()

                    if not outfit_over and not self == person.wardrobe: # try personal wardrobe if available
                        # print("{} - Unable to find overwear in wardrobe, pick overwear from person wardrobe.".format(self.name))
                        outfit_over = person.wardrobe.get_random_appropriate_overwear(slut_limit_remaining, preferences = preferences)

                    if not outfit_over:
                        # print("{} - Unable to find overwear in wardrobe {}, generate random underwear set.".format(person.name, self.name))
                        outfit_over = Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "over", sluttiness_limit = slut_limit_remaining)

            #At this point we have our under and over, if at all possible.
            if not outfit_over or not outfit_under:
                # print("{} - Unable to find anything in wardrobe {}, generate a complete outfit.".format(person.name, self.name))
                # Something's gone wrong and we don't have one of our sets. Last attempt on getting a full outfit from any wardrobe.
                return Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = target_sluttiness, swap_bottoms = True, allow_skimpy = person.sluttiness > 50)

            full_outfit = Wardrobe.build_assembled_outfit(outfit_under, outfit_over)
            # print("{} - full outfit: {}".format(self.name, full_outfit.name))
            return full_outfit

        def decide_on_uniform(self, person):
            slut_limit = 999
            valid_wardrobe = None
            if (person.is_employee or person.is_intern) and dress_code_policy.is_active:
                slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
                valid_wardrobe = self.__build_uniform_wardrobe(slut_limit, underwear_limit, limited_to_top)
            else:
                valid_wardrobe = self.__build_uniform_wardrobe()

            sluttiness_modifier = person.get_opinion_score("work uniforms") / 40.0 # low impact on sluttiness
            sluttiness_modifier += person.get_opinion_score("skimpy uniforms") / 20.0 #larger impact

            uniform = valid_wardrobe.decide_on_outfit(person, sluttiness_modifier = sluttiness_modifier, slut_limit = slut_limit)

            if not uniform: # generate an outfit since we have nothing in our wardrobe that is compliant
                uniform = Wardrobe.generate_random_appropriate_outfit(person, sluttiness_limit = slut_limit)

            if uniform and (person.is_employee or person.is_intern):  # only apply policies for employees
                if creative_colored_uniform_policy.is_active:
                    uniform = WardrobeBuilder(person).personalize_outfit(uniform,
                        swap_bottoms = personal_bottoms_uniform_policy.is_active,
                        allow_skimpy = creative_skimpy_uniform_policy.is_active)
                elif personal_bottoms_uniform_policy.is_active:
                    (uniform, _swapped) = WardrobeBuilder(person).apply_bottom_preference(person, uniform)
                elif easier_access_policy.is_active: # only when creative and relaxed are not active
                    uniform.make_easier_access()

                if commando_uniform_policy.is_active: # always applied, overrides uniform
                    if person.has_large_tits:
                        uniform.remove_panties()    # they still need the support ;)
                        if not uniform.wearing_bra: # probably a body suit, she will show a real bra to wear
                            uniform.add_upper(sports_bra.get_copy(), neutral_palette[renpy.random.choice(neutral_color_map["Underwear"])])
                            WardrobeBuilder.set_sexier_bra(person, uniform, allow_remove_bra = False) # update for sexier version if slutty enough
                    else:
                        uniform.remove_bra_and_panties()

            # special handling for doctors -> she wears a labcoat over her uniform
            if uniform and person.job in [doctor_job]:
                overcoat = next((x for x in uniform.upper_body if x.layer == 4), None)
                if overcoat:
                    uniform.remove_clothing(overcoat)
                uniform.add_upper(lab_coat.get_copy(), [.95, .95, .95, .95])

            uniform.build_outfit_name()

            # print("Picked uniform: {} ({})".format(uniform.name, uniform.outfit_slut_score))

            return uniform

        def has_outfit_with_name(self, the_name):
            return any(x for x in self if x.name == the_name)

        def get_outfit_with_name(self, the_name):
            found = next((x for x in self if x.name == the_name), None)
            if found:
                return found.get_copy()
            return None

        def __build_uniform_wardrobe(self, slut_limit = 999, underwear_limit = 999, limited_to_top = False):
            def _filter_outfit_sets(outfit_sets, slut_limit = 999):
                return [x for x in outfit_sets if x.outfit_slut_score <= slut_limit]

            def _filter_underwear_sets(underwear_sets, underwear_limit = 999):
                return [x for x in underwear_sets if x.underwear_slut_score <= underwear_limit]

            def _filter_overwear_sets(overwear_sets, slut_limit = 999):
                return [x for x in overwear_sets if x.overwear_slut_score <= slut_limit]

            outfit_sets = []
            underwear_sets = []
            overwear_sets = []

            if self.overwear_sets:
                overwear_sets = _filter_overwear_sets(self.overwear_sets, slut_limit)

            if limited_to_top:
                return Wardrobe("Valid Uniform Wardrobe", outfit_sets, underwear_sets, overwear_sets)

            if self.outfit_sets:
                outfit_sets = _filter_outfit_sets(self.outfit_sets, slut_limit)

            if self.underwear_sets:
                underwear_sets = _filter_underwear_sets(self.underwear_sets, underwear_limit)

            return Wardrobe("Valid Uniform Wardrobe", outfit_sets, underwear_sets, overwear_sets)

        def __pick_outfit_with_lowest_sluttiness(self):
            if not self.outfit_sets:
                return None
            return min(self.outfit_sets, key=lambda x: x.outfit_slut_score).get_copy()

        def __pick_overwear_with_lowest_sluttiness(self):
            if not self.overwear_sets:
                return None
            return min(self.overwear_sets, key=lambda x: x.overwear_slut_score).get_copy()

        def __pick_underwear_with_lowest_sluttiness(self):
            if not self.underwear_sets:
                return None
            return min(self.underwear_sets, key=lambda x: x.underwear_slut_score).get_copy()
