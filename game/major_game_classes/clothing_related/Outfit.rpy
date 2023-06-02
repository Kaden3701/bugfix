init -7 python:
    class Outfit(): #A bunch of clothing added together, without slot conflicts.
        @staticmethod
        def _cloth_sort_key(cloth):
            key = cloth.layer
            if cloth == leotard:
                key = 1.2 # for sorting to layer 1.2 (over underwear but under layer 2)
            if cloth == garter_with_fishnets:
                key = 1.3 # also draw above leotard
            if cloth in shirts_list + bracelet_list: # draw shirts over pants
                key += .1
            if cloth in neckwear_list: # move from layer 2 to 3.5 (between clothing and overwear)
                key += 1.5
            if cloth.tucked: # tucked is always a between layer value
                key += .5
            return key

        @staticmethod
        def classification(slut_score):
            classifications = ["Conservative", "Timid", "Modest", "Casual", "Trendy", "Stylish", "Enticing", "Provocative", "Sensual", "Sexy", "Seductive", "Sultry", "Slutty"]
            ci = __builtin__.int(slut_score * .14)
            if ci >= __builtin__.len(classifications):
                return classifications[-1]
            return classifications[ci]

        def __init__(self,name):
            self.name = name
            self.upper_body = []
            self.lower_body = []
            self.feet = []
            self.accessories = [] #Extra stuff that doesn't fit anywhere else. Hats, glasses, ect.

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.name == other.name:
                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def __hash__(self):
            return hash((self.name, tuple(x for x in map(hash, self.upper_body)),
                tuple(x for x in map(hash, self.lower_body)),
                tuple(x for x in map(hash, self.feet)),
                tuple(x for x in map(hash, self.accessories))))

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.name == other.name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.name != other.name
            return True

        def matches(self, other):
            if not isinstance(self, other.__class__):
                return False

            current_clothing = self.upper_body + self.lower_body + self.feet
            other_clothing = other.upper_body + other.lower_body + other.feet

            if len(current_clothing) != len(other_clothing):
                return False

            return sorted(current_clothing) == sorted(other_clothing)

        def __iter__(self):
            return iter(self.upper_body + self.lower_body + self.feet + self.accessories)

        @property
        def item_count(self):
            return sum(1 for _ in self)

        def clear(self):
            self.upper_body.clear()
            self.lower_body.clear()
            self.feet.clear()
            self.accessories.clear()

        def get_copy(self):
            copy_outfit = Outfit(self.name)

            for feet in self.feet:
                copy_outfit.feet.append(feet.get_copy())

            for lower in self.lower_body:
                if not lower.is_extension:
                    copy_outfit.lower_body.append(lower.get_copy())

            for upper in self.upper_body:
                upper_copy = upper.get_copy()
                copy_outfit.upper_body.append(upper_copy)
                if upper.has_extension:
                    copy_outfit.lower_body.append(upper_copy.has_extension)

            for accessory in self.accessories:
                copy_outfit.accessories.append(accessory.get_copy())
            return copy_outfit

        def generate_draw_list(self, the_person, position, emotion = "default", special_modifiers = None, lighting = None, hide_layers = None): #Generates a sorted list of displayables that when drawn display the outfit correctly.
            nipple_wetness = 0.0 # Used to simulate a girl lactating through clothing. Ranges from 0 (none) to 1 (Maximum Effect)
            if the_person is None:
                body_type = "standard_body"
                tit_size = "D"
                face_style = "Face_1"

            else:
                body_type = the_person.body_type
                tit_size = the_person.tits
                face_style = the_person.face_style
                if the_person.lactation_sources > 0:
                    nipple_wetness = (0.1*(float(Person.rank_tits(the_person.tits)+the_person.lactation_sources))) * (the_person.arousal_perc / 100)
                    if nipple_wetness > 1.0:
                        nipple_wetness = 1.0

            if hide_layers is None:
                hide_layers = []

            all_items = self.__generate_clothing_list() #First generate a list of the clothing objects

            currently_constrained_regions = []
            ordered_displayables = []
            for item in reversed(all_items): #To properly constrain items we need to figure out how they look from the outside in, even though we eventually draw from the inside out
                if isinstance(item, Facial_Accessory):
                    if item.layer not in hide_layers:
                        ordered_displayables.append(item.generate_item_displayable(position, face_style, emotion, special_modifiers, lighting = lighting))
                elif not item.is_extension:
                    if item.layer not in hide_layers:
                        ordered_displayables.append(item.generate_item_displayable(body_type, tit_size, position, lighting = lighting, regions_constrained = currently_constrained_regions, nipple_wetness = nipple_wetness))
                        for region in item.constrain_regions:
                            if item.half_off and region in item.half_off_regions:
                                pass # If an item is half off the regions that are hidden while half off are also not constrained by the clothing.
                            elif item.has_extension and item.has_extension.half_off and region in item.has_extension.half_off_regions:
                                pass # If the extension for an item (a dress bottom, for example) is half off and hiding something that section is not contrained.
                            else:
                                currently_constrained_regions.append(region)

            return reversed(ordered_displayables) #We iterated over all_items backwards, so our return list needs to be inverted

        def generate_split_draw_list(self, split_on_clothing, the_person, position, emotion = "default", special_modifiers = None, lighting = None): #Mirrors generate draw list but returns only the clothing above and below the given item as two lists with the item in between (in a tuple)
            if the_person is None:
                body_type = "standard_body"
                tit_size = "D"
                face_style = "Face_1"

            else:
                body_type = the_person.body_type
                tit_size = the_person.tits
                face_style = the_person.face_style

            on_bottom = True #Checks to see if we are adding things to the top or bottom list, flips when it sees the split_on_clothing item
            bottom_items = [] #Things drawn below the middle item
            middle_item = None #The displayable for the middle item
            top_items = [] #Things drawn on top of the middle item
            all_items = self.__generate_clothing_list()


            for item in all_items:
                currently_constrained_regions = []
                if isinstance(item, Facial_Accessory):
                    item_check = item.generate_item_displayable(position, face_style, emotion, special_modifiers, lighting = lighting)
                elif not item.is_extension:
                    item_check = item.generate_item_displayable(body_type, tit_size, position, lighting = lighting, regions_constrained = currently_constrained_regions)
                    for region in item.constrain_regions:
                        if item.half_off and region in item.constrain_regions:
                            pass # If an item is half off the regions that are hidden while half off are also not constrained by the clothing.
                        elif item.has_extension and item.has_extension.half_off and region in item.has_extension.half_off_regions:
                            pass # If the extension for an item (a dress bottom, for example) is half off and hiding something that section is not contrained.
                        else:
                            currently_constrained_regions.append(region)

                if not item.is_extension:
                    if item == split_on_clothing:
                        middle_item = item_check
                        on_bottom = False
                    else:
                        if on_bottom:
                            bottom_items.append(item_check)
                        else:
                            top_items.append(item_check)
            return (bottom_items,middle_item,top_items)

        def get_forced_modifier(self): #Returns, if one exists, a forced modifier caused by one of the facial accessories (Currently used to support ball gags)
            forced_special_modifier = None
            for item in self.accessories:
                if isinstance(item, Facial_Accessory) and item.modifier_lock is not None:
                    forced_special_modifier = item.modifier_lock #TODO: Decide what to do if multiple accessories add a forced modifier. Probably limit outfits so only 1 can contribute a modifier
            return forced_special_modifier

        def merge_outfit(self, other_outfit, underwear_only = False):
            if not isinstance(other_outfit, Outfit):
                return self
            # Takes other_outfit
            for cloth in [x for x in other_outfit.upper_body if not underwear_only or x.layer <= 2]:
                self.add_upper(cloth.get_copy())
            for cloth in [x for x in other_outfit.lower_body if not underwear_only or x.layer <= 2]:
                self.add_lower(cloth.get_copy())
            for cloth in [x for x in other_outfit.feet if not underwear_only or x.layer <= 2]:
                self.add_feet(cloth.get_copy())
            for cloth in [x for x in other_outfit.accessories if not underwear_only or x.layer <= 2]:
                self.add_accessory(cloth.get_copy())
            return self

        def can_add_dress(self, new_clothing):
            return self.can_add_upper(new_clothing)

        def add_dress(self, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
            self.add_upper(new_clothing, re_colour = re_colour, pattern = pattern, colour_pattern = colour_pattern)

        def can_add_upper(self, new_clothing):
            allowed = not any(x for x in self.upper_body if x.name == new_clothing.name or (x.layer > 0 and x.layer == new_clothing.layer))
            if allowed and new_clothing.has_extension:
                return not any(x for x in self.lower_body if x.layer == new_clothing.has_extension.layer) \
                    and not any(x for x in self.upper_body if x.has_extension and x.layer == new_clothing.has_extension.layer and x.has_extension.layer == new_clothing.layer)
            return allowed

        def add_upper(self, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
            if re_colour is not None:
                new_clothing.colour = re_colour

            if pattern is not None:
                new_clothing.pattern = pattern
                if colour_pattern is not None:
                    new_clothing.colour_pattern = colour_pattern
                else:
                    new_clothing.colour_pattern = new_clothing.colour

            if self.can_add_upper(new_clothing): ##Always check to make sure the clothing is valid before you add it.
                self.upper_body.append(new_clothing)
                if new_clothing.has_extension:
                    self.lower_body.append(new_clothing.has_extension)

        def can_add_lower(self,new_clothing):
            return not any(x for x in self.lower_body if x.layer == new_clothing.layer)

        def add_lower(self, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
            if re_colour is not None:
                new_clothing.colour = re_colour
            if pattern is not None:
                new_clothing.pattern = pattern
                if colour_pattern is not None:
                    new_clothing.colour_pattern = colour_pattern
                else:
                    new_clothing.colour_pattern = new_clothing.colour

            if self.can_add_lower(new_clothing):
                self.lower_body.append(new_clothing)

        def can_add_feet(self, new_clothing):
            return not any(x for x in self.feet if x.layer == new_clothing.layer)

        def add_feet(self, new_clothing, re_colour = None, pattern = None, colour_pattern = None):
            if re_colour is not None:
                new_clothing.colour = re_colour

            if pattern is not None:
                new_clothing.pattern = pattern
                if colour_pattern is not None:
                    new_clothing.colour_pattern = colour_pattern
                else:
                    new_clothing.colour_pattern = new_clothing.colour

            if self.can_add_feet(new_clothing):
                self.feet.append(new_clothing)

        def can_add_accessory(self, new_clothing):
            allowed = True #For now all we do not filter what accessories we let people apply. All we require is that this exact type of accessory is not already part of the outfit.
            for accessory in self.accessories:
                if accessory.is_similar(new_clothing):
                    allowed = False
            return allowed

        def add_accessory(self,new_clothing, re_colour = None, pattern = None, colour_pattern = None):
            if re_colour is not None:
                new_clothing.colour = re_colour
            if pattern is not None:
                new_clothing.pattern = None
                if colour_pattern is not None:
                    new_clothing.colour_pattern = colour_pattern
                else:
                    new_clothing.colour_pattern = new_clothing.colour

            if self.can_add_accessory(new_clothing):
                self.accessories.append(new_clothing)

        def has_clothing(self, the_clothing): #Returns True if this outfit includes the given clothing item, false otherwise. Checks for exact parameter match (colour, name, ect), but not reference match.
            return any(x for x in self.upper_body + self.lower_body + self.feet + self.accessories if x == the_clothing)

        def remove_clothing(self, old_clothing):
            #TODO: make sure this works with dresses when you remove the bottom (ie. extension) first.
            if old_clothing.has_extension:
                self.remove_clothing(old_clothing.has_extension)

            if old_clothing in self.upper_body:
                self.upper_body.remove(old_clothing)
            elif old_clothing in self.lower_body:
                self.lower_body.remove(old_clothing)
            elif old_clothing in self.feet:
                self.feet.remove(old_clothing)
            elif old_clothing in self.accessories:
                self.accessories.remove(old_clothing)

        def half_off_clothing(self, the_clothing):
            found = next((x for x in self if x == the_clothing), None)
            if found:
                found.half_off = True

        def remove_clothing_list(self, the_list, half_off_instead = False):
            if not (the_list and isinstance(the_list, list)):
                return

            for item in the_list:
                if half_off_instead:
                    self.half_off_clothing(item)
                else:
                    self.remove_clothing(item)

        def restore_all_clothing(self):
            for cloth in [x for x in self.upper_body + self.lower_body + self.feet + self.accessories if x.half_off]:
                cloth.half_off = False

        def get_upper_ordered(self): #Returns a list of pieces from bottom to top, on the upper body. Other functions do similar things, but to lower and feet.
            return sorted(self.upper_body, key = lambda x: Outfit._cloth_sort_key(x))

        def get_lower_ordered(self):
            return sorted(self.lower_body, key = lambda x: Outfit._cloth_sort_key(x))

        def get_feet_ordered(self):
            return sorted(self.feet, key = lambda x: Outfit._cloth_sort_key(x))

        @property
        def get_upper_top_layer(self):
            if self.upper_body:
                return self.get_upper_ordered()[-1]
            return None

        @property
        def get_lower_top_layer(self):
            if self.lower_body:
                return self.get_lower_ordered()[-1]
            return None

        @property
        def get_feet_top_layer(self):
            if self.feet:
                return self.get_feet_ordered()[-1]
            return None

        def remove_random_any(self, top_layer_first = False, exclude_upper = False, exclude_lower = False, exclude_feet = False, do_not_remove = False):
            #Picks a random upper, lower, or feet object to remove. Is guaranteed to remove something if possible, or return None if nothing on the person is removable (They're probably naked).
            functs_to_try = []
            if not exclude_upper:
                functs_to_try.append(self.remove_random_upper)
            if not exclude_lower:
                functs_to_try.append(self.remove_random_lower)
            if not exclude_feet:
                functs_to_try.append(self.remove_random_feet)
            renpy.random.shuffle(functs_to_try) #Shuffle the functions so they appear in a random order.
            for remover in functs_to_try: #Try removing each of an upper, lower, and feet. If any succeed break there and return what we removed. Otherwise keep trying. If we run out of things to try we could not remove anything.
                success = remover(top_layer_first, do_not_remove)
                if success:
                    return success
            return None

        def remove_random_upper(self, top_layer_first = False, do_not_remove = False):
            #if top_layer_first only the upper most layer is removed, otherwise anything unanchored is a valid target.
            #if do_not_remove is set to True we only use this to find something valid to remove and return that clothing item. this lets us use this function to find thigns to remove with an animation.
            #Returns None if there is nothing to be removed.
            to_remove = None
            if top_layer_first:
                #Just remove the very top layer
                if self.__get_upper_unanchored():
                    to_remove = self.__get_upper_unanchored()[0]
                    if to_remove.is_extension:
                        return None #Extensions can't be removed directly.
                else:
                    return None
            else:
                to_remove = get_random_from_list(self.__get_upper_unanchored())
                if to_remove and to_remove.is_extension:
                    return None

            if to_remove and to_remove.layer == 0: # don not nipple covers or cinchers
                return None

            if to_remove and not do_not_remove:
                self.remove_clothing(to_remove)
            return to_remove

        def remove_random_lower(self, top_layer_first = False, do_not_remove = False):
            to_remove = None
            if top_layer_first:
                #Just remove the very top layer
                if self.__get_lower_unanchored():
                    to_remove = self.__get_lower_unanchored()[0]
                    if to_remove.is_extension:
                        return None #Extensions can't be removed directly.
                else:
                    return None
            else:
                to_remove = get_random_from_list(self.__get_lower_unanchored())
                if to_remove and to_remove.is_extension:
                    return None

            if to_remove and not do_not_remove:
                self.remove_clothing(to_remove)
            return to_remove

        def remove_random_feet(self, top_layer_first = False, do_not_remove = False):
            to_remove = None
            if top_layer_first:
                #Just remove the very top layer
                if self.__get_foot_unanchored():
                    to_remove = self.__get_foot_unanchored()[0]
                    if to_remove.is_extension:
                        return None #Extensions can't be removed directly.
                else:
                    return None
            else:
                to_remove = get_random_from_list(self.__get_foot_unanchored())
                if to_remove and to_remove.is_extension:
                    return None

            if to_remove and not do_not_remove:
                self.remove_clothing(to_remove)
            return to_remove

        def get_unanchored(self, half_off_instead = False): #Returns a list of the pieces of clothing that can be removed.
            #Question: should be be able to remove accessories like this? We would need a way to flag some things like makeup as unremovable.
            # Note: half_off_instead returns a list of clothing items that can be half-offed, which means eitehr they are completely unanchored, or they are anchored but all upper layers are half-off and half-off gives access
            return_list = []
            return_list.extend(self.__get_upper_unanchored(half_off_instead))
            return_list.extend(self.__get_lower_unanchored(half_off_instead))
            return_list.extend(self.__get_foot_unanchored(half_off_instead))

            return return_list

        def is_item_unanchored(self, the_clothing, half_off_instead = False): #Returns true if the clothing item passed is unanchored, ie. could be logically taken off.
            if the_clothing in self.upper_body:
                return the_clothing in self.__get_upper_unanchored(half_off_instead)
            elif the_clothing in self.lower_body:
                return the_clothing in self.__get_lower_unanchored(half_off_instead)
            elif the_clothing in self.feet:
                return the_clothing in self.__get_foot_unanchored(half_off_instead)
            return True

        @property
        def vagina_available(self): ## Doubles for asshole for anal.
            return not any(x for x in self.lower_body if x.anchor_below and not (x.half_off and x.half_off_gives_access))

        @property
        def vagina_visible(self):
            return not any(x for x in self.lower_body if x.hide_below and not (x.half_off and x.half_off_gives_access))

        @property
        def tits_available(self):
            return not any(x for x in self.upper_body if x.anchor_below and not x in [vest, suit_jacket] and not (x.half_off and x.half_off_gives_access))

        @property
        def tits_visible(self):
            return not any(x for x in self.upper_body if x.hide_below and not x in [vest, suit_jacket] and not (x.half_off and x.half_off_gives_access))

        @property
        def underwear_visible(self):
            return (self.wearing_bra and not self.bra_covered) or \
                    (self.wearing_panties and not self.panties_covered)

        @property
        def feet_available(self):
            return not any(x for x in self.feet if x.anchor_below)

        @property
        def feet_visible(self):
            return not any(x for x in self.feet if x.hide_below)

        @property
        def wearing_bra(self):
            return any(x for x in self.upper_body if (x.underwear and not x.layer == 0))

        @property
        def can_remove_bra(self):
            if not self.wearing_bra:
                return False
            bra = self.get_bra()
            unanchored = self.__get_upper_unanchored()
            return bra in unanchored

        def get_bra(self):
            return next((x for x in self.upper_body if x.underwear and not x.layer == 0), None)

        def remove_bra(self):
            if self.wearing_bra:
                self.remove_clothing(self.get_bra())
            return

        @property
        def wearing_panties(self):
            return any(x for x in self.lower_body if x.underwear and not x.layer == 0) \
                or any(x for x in self.upper_body if x in [leotard])

        @property
        def can_remove_panties(self):
            if not self.wearing_panties:
                return False
            panties = self.get_panties()
            unanchored = self.__get_lower_unanchored()
            return panties in unanchored

        def get_panties(self):
            return next((x for x in self.lower_body if x.underwear and not x.layer == 0), \
                    next((x for x in self.upper_body if x in [leotard]), None))

        def remove_panties(self):
            if self.wearing_panties:
                self.remove_clothing(self.get_panties())
            return

        def remove_bra_and_panties(self):
            self.remove_bra()
            self.remove_panties()
            return

        @property
        def bra_covered(self):
            if not self.wearing_bra:
                return False

            for cloth in self.get_upper_ordered()[::-1]: #Traverse list from outside in
                if cloth.underwear:
                    return False
                elif cloth.hide_below and not (cloth.half_off and cloth.half_off_reveals):
                    return True
            return False

        @property
        def is_bra_visible(self):
            return self.wearing_bra and not self.bra_covered

        @property
        def panties_covered(self):
            if not self.wearing_panties:
                return False

            for cloth in self.get_lower_ordered()[::-1]: #Traverse list from outside in
                if cloth.underwear:
                    return False
                elif cloth.hide_below and not (cloth.half_off and cloth.half_off_reveals):
                    return True
            return False

        @property
        def are_panties_visible(self):
            return self.wearing_panties and not self.panties_covered

        @property
        def has_overwear(self): #Returns true if the outfit has layer 2 clothing items for upper and lower body.
            if any(x in [nightgown_dress] for x in self.upper_body):
                return False
            if not any(x.layer >= 2 for x in self.upper_body):
                return False
            if not any(x.layer >= 2 for x in self.lower_body):
                return False
            return True

        @property
        def has_underwear(self):
            return self.wearing_bra and self.wearing_panties

        @property
        def is_wearing_underwear(self):
            return self.wearing_bra or self.wearing_panties

        @property
        def is_suitable_underwear_set(self): #Returns true if the outfit could qualify as an underwear set ie. Only layer 1 clothing.
            return not any(x for x in self if x.layer > 2)

        @property
        def is_suitable_overwear_set(self): #Returns true if the outfit could qualify as an overwear set ie. contains no layer 1 clothing.
            return not any(x for x in self if x.layer < 2)

        @property
        def shows_off_her_ass(self):
            if self.has_overwear:
                return any(x for x in self if x.layer >= 2 and x in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"])
            else:
                return any(x for x in self if x in WardrobeBuilder.preferences["showing her ass"]["lower_body"] + WardrobeBuilder.preferences["showing her ass"]["upper_body"])

        @property
        def shows_off_her_tits(self):
            if self.has_overwear:
                return any(x for x in self if x.layer >= 2 and x in WardrobeBuilder.preferences["showing her tits"])
            else:
                return any(x for x in self if x in WardrobeBuilder.preferences["showing her tits"])

        @property
        def underwear_slut_score(self): #Calculates the sluttiness of this outfit assuming it's an underwear set. We assume a modest overwear set is used (ie. one that covers visibility).
            # showing tits or ass has ony 50% impact on underwear slut score (fully naked == 30 slut)
            new_score = __builtin__.int(self.__get_body_parts_slut_score() * .5)
            new_score += self.__get_total_slut_modifiers()
            return new_score if new_score < 100 else 100

        @property
        def overwear_slut_score(self): #Calculates the sluttiness of this outfit assuming it's an overwear set. That means we assume a modest underwear set is used (ie. one that denies access).
            new_score = self.__get_body_parts_slut_score()
            new_score += self.__get_total_slut_modifiers()
            return new_score if new_score < 100 else 100

        @property
        def outfit_slut_score(self): #Calculates the sluttiness of this outfit assuming it's a full outfit. Full penalties and such apply.
            new_score = self.__get_body_parts_slut_score()
            new_score += self.__get_total_slut_modifiers()
            # penalty for not having an overwear item
            if not any(x.layer >= 3 for x in self.upper_body):
                new_score += 15
            if not any(x.layer >= 3 for x in self.lower_body):
                new_score += 15
            return new_score if new_score < 100 else 100

        def get_full_strip_list(self, strip_feet = True, strip_accessories = False): #TODO: This should support visible_enough at some point.
            items_to_strip = self.lower_body + [x for x in self.upper_body if x.layer > 0]
            if strip_feet:
                items_to_strip.extend(self.feet)
            if strip_accessories: # exclude make-up and earings
                items_to_strip.extend([x for x in self.accessories if not x in earings_list])
            items_to_strip.sort(key= lambda clothing: clothing.tucked, reverse = True) #Tucked upper body stuff draws after lower body.
            items_to_strip.sort(key= lambda clothing: clothing.layer) #Sort the clothing so it is removed top to bottom based on layer.

            extension_items = []
            for item in items_to_strip:
                if item.is_extension:
                    extension_items.append(item)

            for item in extension_items:
                items_to_strip.remove(item) #Don't try and strip extension directly.
            return items_to_strip[::-1] #Put it in reverse order so when stripped it will be done from outside in.

        def get_underwear_strip_list(self, visible_enough = True, avoid_nudity = False, strip_shoes = False): #Gets a list of things to strip until this outfit would have a girl in her underwear
            #If a girl isn't wearing underwear this ends up being a full strip. If she is wearing only a bra/panties she'll strip until they are visible, and the other slot is naked.
            test_outfit = self.get_copy() #We'll use a copy of the outfit. Slightly less efficient, but makes it easier to ensure we are generating valid strip orders.
            items_to_strip = []

            keep_stripping = not (self.is_bra_visible or self.tits_visible)
            while keep_stripping:
                keep_stripping = False
                item = test_outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
                if item is not None and not item.underwear:
                    test_outfit.remove_clothing(item)
                    if avoid_nudity and ((visible_enough and self.tits_visible) or self.tits_available):
                        test_outfit.add_upper(item) #Stripping this would result in nudity, which we need to avoid.
                        pass
                    elif visible_enough and (self.is_bra_visible or self.tits_visible):
                        items_to_strip.append(item)
                    else:
                        items_to_strip.append(item)
                        keep_stripping = True

            keep_stripping = not (self.are_panties_visible or self.vagina_visible)
            while keep_stripping:
                keep_stripping = False
                item = test_outfit.remove_random_lower(top_layer_first = True, do_not_remove = True)
                if item is not None and not item.underwear:
                    test_outfit.remove_clothing(item)
                    if avoid_nudity and ((visible_enough and self.vagina_visible) or self.vagina_available):
                        test_outfit.add_lower(item) #Stripping this would result in nudity, which we need to avoid.
                    elif visible_enough and (self.are_panties_visible or self.vagina_visible):
                        items_to_strip.append(item)
                    else:
                        items_to_strip.append(item)
                        keep_stripping = True

            if strip_shoes:
                for item in self.get_feet_ordered():
                    if item.layer == 2:
                        items_to_strip.insert(0, item) #Inserts shoes at the start of the list, since they're the first thing that should be removed.
            return items_to_strip

        def strip_to_underwear(self, visible_enough = True, avoid_nudity = False, strip_shoes = False): #Used to off screen strip a girl down to her underwear, or completely if she isn't wearing any.
            items_to_strip = self.get_underwear_strip_list(visible_enough, avoid_nudity, strip_shoes)
            for item in items_to_strip:
                self.remove_clothing(item)

        def get_tit_strip_list(self, visible_enough = True): #Generates a list of clothing that, when removed from this outfit, result in tits being visible. Useful for animated clothing removal.
            test_outfit = self.get_copy()
            items_to_strip = []
            while not ((test_outfit.tits_visible and visible_enough) or (test_outfit.tits_available and not visible_enough)):
                the_item = test_outfit.remove_random_upper(top_layer_first = True)
                if not the_item:
                    the_item = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True)
                if not the_item:
                    break
                items_to_strip.append(the_item)
            return [x for x in items_to_strip if x.layer != 0]

        def strip_to_tits(self, visible_enough = True): #Removes all clothing from this item until breasts are visible.
            if visible_enough:
                while not self.tits_visible:
                    the_item = self.remove_random_upper(top_layer_first = True)
                    if not the_item:
                        break
            else:
                while not (self.tits_visible and self.tits_available):
                    the_item = self.remove_random_upper(top_layer_first = True)
                    if not the_item:
                        break
            return

        def get_vagina_strip_list(self, visible_enough = False):
            test_outfit = self.get_copy()
            items_to_strip = []
            while not ((test_outfit.vagina_visible and visible_enough) or (test_outfit.vagina_available and not visible_enough)):
                the_item = test_outfit.remove_random_lower(top_layer_first = True) #Try and remove lower layer clothing first each loop
                if not the_item:
                    the_item = test_outfit.remove_random_any(top_layer_first = True, exclude_feet = True) #If that fails to make progress (ie. due to upper body items blocking things) remove upper body stuff until we can make progress again.
                if not the_item:
                    break
                items_to_strip.append(the_item)
            return items_to_strip

        def strip_to_vagina(self, visible_enough = False):
            self.remove_clothing_list(self.get_vagina_strip_list(visible_enough = visible_enough))
            return

        def can_half_off_to_tits(self, visible_enough = True):
            # Returns true if all of the clothing blocking her tits can be moved half-off to gain access, or if you already have access
            return (visible_enough and self.tits_visible) \
                or (not visible_enough and self.tits_available) \
                or __builtin__.len(self.get_half_off_to_tits_list(visible_enough = visible_enough)) > 0

        def get_half_off_to_tits_list(self, visible_enough = True):
            # If possible returns the list of clothing items, from outer to inner, that must be half-offed to gain view/access to her tits
            # If not possible returns an empty list.
            return_list = []
            possible = True
            anchored = None #Set to true when we hit something that stays anchored even if half-off. If that
            for item in self.get_upper_ordered()[::-1]: #Ordered top to bottom
                if visible_enough:
                    if item.hide_below and not (item.can_be_half_off and item.half_off_reveals): #If a piece of clothing hides what's be below and it's anchored or
                        possible = False
                        break
                    elif item.hide_below:
                        if anchored:
                            if item.can_be_half_off and item.half_off_gives_access:
                                if anchored not in return_list:
                                    return_list.append(anchored)
                                anchored = None #Something would anchor the clothing, but it can be removed easily enough.
                            else:
                                possible = False #Something is in the way and we can't get it off because of something else
                                break
                        if item not in return_list:
                            return_list.append(item) #Half-off the anchoring item, then the thing in the way.

                    if item.anchor_below:
                        anchored = item

                else:
                    if item.anchor_below and not (item.can_be_half_off and item.half_off_gives_access):
                        hidden = True
                        break

                    elif item.anchor_below:
                        if item not in return_list:
                            return_list.append(item)

            if not possible:
                return []

            else:
                return return_list

        def can_half_off_to_vagina(self, visible_enough = True):
            # Returns true if all of the clothing blocking her vagina can be moved half-off to gain access
            return ((visible_enough and self.vagina_visible) \
                or (not visible_enough and self.vagina_available)) \
                or __builtin__.len(self.get_half_off_to_vagina_list(visible_enough = visible_enough)) > 0

        def get_half_off_to_vagina_list(self, visible_enough = True):
            # If possible returns the list of clothing items, from outer to inner, that must be half-offed to gain view/access to her vagina
            # If not possible returns an empty list.
            return_list = []
            possible = True
            anchored = None #Set to true when we hit something that stays anchored even if half-off. If that
            for item in self.get_lower_ordered()[::-1]: #Ordered top to bottom
                if visible_enough:
                    if item.hide_below and not (item.can_be_half_off and item.half_off_reveals): #If a piece of clothing hides what's be below and it's anchored or
                        possible = False
                        break
                    elif item.hide_below or item.can_be_half_off:
                        if anchored:
                            if item.can_be_half_off and item.half_off_gives_access:
                                if anchored not in return_list:
                                    return_list.append(anchored)
                                anchored = None #Something would anchor the clothing, but it can be removed easily enough.
                            else:
                                possible = False #Something is in the way and we can't get it off because of something else
                                break

                        if item not in return_list:
                            return_list.append(item) #Half-off the anchoring item if we didn't already

                    if item.anchor_below:
                        anchored = item

                else:
                    if item.anchor_below and not (item.can_be_half_off and item.half_off_gives_access):
                        hidden = True
                        break

                    elif item.anchor_below or item.can_be_half_off:
                        if item not in return_list:
                            return_list.append(item)

            if not possible:
                return []

            else:
                return return_list

        @property
        def cum_covered(self): #Returns True if the person has some cum clothing item as part of their outfit. #TODO: Also have this check layer/visibility, so girls can be creampied but just put panties back on and have nobody notice.
            return any(x for x in self.accessories if x.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name])

        def remove_all_cum(self):
            for acc in [x for x in self.accessories if x.name in [mouth_cum.name, tits_cum.name, stomach_cum.name, face_cum.name, ass_cum.name, creampie_cum.name]]:
                self.accessories.remove(acc)
            return

        @property
        def has_mouth_cum(self):
            return any(x.name == mouth_cum.name for x in self.accessories)

        @property
        def has_tits_cum(self):
            return any(x.name == tits_cum.name for x in self.accessories)

        @property
        def has_stomach_cum(self):
            return any(x.name == stomach_cum.name for x in self.accessories)

        @property
        def has_face_cum(self):
            return any(x.name == face_cum.name for x in self.accessories)

        @property
        def has_ass_cum(self):
            return any(x.name == ass_cum.name for x in self.accessories)

        @property
        def has_creampie_cum(self):
            return any(x.name == creampie_cum.name for x in self.accessories)

        @property
        def has_dress(self):
            return any(self.has_clothing(item) for item in real_dress_list)

        @property
        def has_skirt(self):
            return any(self.has_clothing(item) for item in skirts_list)

        @property
        def has_pants(self):
            return any(self.has_clothing(item) for item in pants_list)

        @property
        def has_shirt(self):
            return any(self.has_clothing(item) for item in shirts_list)

        @property
        def has_socks(self):
            return any(self.has_clothing(item) for item in only_socks_list)

        @property
        def has_hose(self):
            return any(self.has_clothing(item) for item in real_pantyhose_list)

        @property
        def has_glasses(self):
            return any([x for x in self.accessories if x.name in [big_glasses.name, modern_glasses.name]])

        def remove_glasses(self):
            for acc in [x for x in self.accessories if x.name in [big_glasses.name, modern_glasses.name]]:
                self.accessories.remove(acc)
            return

        @property
        def has_full_access(self):
            return (self.tits_visible and self.tits_available and not self.wearing_bra
                and self.vagina_visible and self.vagina_available and not self.wearing_panties
                and not any(x.layer >= 2 for x in self.upper_body if not x.half_off)
                and not any(x.layer >= 2 for x in self.lower_body if not x.half_off))

        @property
        def is_easier_access(self):
            return not any(x for x in self.lower_body if x.layer >= 2 and x.anchor_below)

        def make_easier_access(self):
            changed = False
            if self.has_pants:
                swap_outfit_bottoms(self)
                changed = True

            for item in self.upper_body:
                if item.is_similar(pinafore):
                    new_item_top = vest.get_copy()
                    new_item_top.colour = item.colour
                    new_item_bottom = skirt.get_copy()
                    new_item_bottom.colour = item.colour
                    self.remove_clothing(item)
                    self.add_upper(new_item_top)
                    self.add_lower(new_item_bottom)
                    changed = True
            for item in self.lower_body:
                if item.is_similar(long_skirt) or item.is_similar(pencil_skirt):
                    new_item = skirt.get_copy()
                    new_item.colour = item.colour
                    self.remove_clothing(item)
                    self.add_lower(new_item)
                    changed = True
            return changed

        def remove_all_collars(self):
            for proper_name in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Spiked_Choker"]:
                found = find_in_list(lambda x: x.proper_name == proper_name, self.accessories)
                if found:
                    self.accessories.remove(found)
            return

        # Quickly make her show tits
        # ignores stripping logic where skirt / pants might be removed to show tits
        def remove_all_upper_clothing(self):
            for item in self.get_upper_ordered():
                self.remove_clothing(item)
            return

        def build_outfit_name(self):
            def get_clothing_items(outfit_part):
                return sorted([x for x in outfit_part if not x.is_extension and (x in [pinafore] or x.layer < 4)], key = lambda x: x.layer, reverse = True)

            outfitname = ""
            upper = get_clothing_items(self.upper_body)
            if upper:
                outfitname += upper[0].name

            lower = get_clothing_items(self.lower_body)
            if upper and lower:
                outfitname += " and "
            if lower:
                outfitname += lower[0].name

            feet = get_clothing_items(self.feet)
            if feet:
                if len(outfitname) == 0:
                    outfitname = " with ".join([x.name for x in feet])
                else:
                    if __builtin__.len(outfitname) != 0:
                        outfitname += " with "
                    outfitname += feet[0].name

            if __builtin__.len(outfitname) == 0:
                return "Naked"

            self.name = "{} {}".format(Outfit.classification(self.outfit_slut_score), outfitname)

            return self.name

        def update_name(self):
            self.name = self.build_outfit_name()
            return

        @property
        def is_legal_in_public(self):
            if mc.business.nudity_is_legal or (not self.tits_visible and not self.vagina_visible):
                return True
            if self.vagina_visible:
                return False
            if mc.business.topless_is_legal and not self.vagina_visible:
                return True
            return False

        def __get_upper_unanchored(self, half_off_instead = False):
            return_list = []
            for top in reversed(self.get_upper_ordered()):
                if top.has_extension is None or self.is_item_unanchored(top.has_extension, half_off_instead): #Clothing items that cover two slots (dresses) are unanchored if both halves are unanchored.
                    if not half_off_instead or (half_off_instead and top.can_be_half_off):
                        return_list.append(top) #Always add the first item because the top is, by definition, unanchored

                if top.anchor_below and not (half_off_instead and top.half_off and top.half_off_gives_access):
                    break #Search the list, starting at the outermost item, until you find something that anchors the stuff below it.
            return return_list

        def __get_lower_unanchored(self, half_off_instead = False):
            return_list = []
            for bottom in reversed(self.get_lower_ordered()):
                if bottom.has_extension is None or self.is_item_unanchored(bottom.has_extension, half_off_instead):
                    if not half_off_instead or (half_off_instead and bottom.can_be_half_off):
                        return_list.append(bottom)

                if bottom.anchor_below and not (half_off_instead and bottom.half_off and bottom.half_off_gives_access):
                    break
            return return_list

        def __get_foot_unanchored(self, half_off_instead = False):
            return_list = []
            for foot in reversed(self.get_feet_ordered()):
                if foot.has_extension is None or self.is_item_unanchored(foot.has_extension, half_off_instead):
                    if not half_off_instead or (half_off_instead and foot.can_be_half_off):
                        return_list.append(foot)

                if foot.anchor_below and not (half_off_instead and foot.half_off and foot.half_off_gives_access):
                    break
            return return_list

        def __generate_clothing_list(self):
            return sorted(self, key = lambda x: Outfit._cloth_sort_key(x))

        def __get_body_parts_slut_score(self):
            def _get_transparency_factor(cloth_list):
                alpha_values = [x.transparency for x in cloth_list]
                if not alpha_values:
                    alpha_values = [1.0]

                avg_transparency = reduce(lambda x, y: x + y, alpha_values) / float(len(alpha_values))

                return 1.0 - __builtin__.min(1.0, __builtin__.max(0.0, (avg_transparency - .33))/(.95 - .33))

            tits_score = 0
            if self.tits_visible:
                tits_score += 30
            elif self.tits_available:
                tits_score += 15
                tits_score += 15 * _get_transparency_factor([x for x in self.upper_body])
            else:
                tits_score += 30 * _get_transparency_factor([x for x in self.upper_body])

            if self.has_overwear and self.wearing_bra and self.is_bra_visible:
                tits_score += 5

            if self.has_overwear and not self.wearing_bra:
                tits_score += 10

            vagina_score = 0
            if self.vagina_visible:
                vagina_score += 30
            elif self.vagina_available:
                vagina_score += 15
                vagina_score += 15 * _get_transparency_factor([x for x in self.lower_body])
            else:
                vagina_score += 30 * _get_transparency_factor([x for x in self.lower_body])

            if self.has_overwear and self.wearing_panties and self.are_panties_visible:
                vagina_score += 10

            if self.has_overwear and not self.wearing_panties:
                vagina_score += 15

            return __builtin__.int(tits_score + vagina_score)

        def __get_total_slut_modifiers(self): #Calculates the sluttiness boost purely do to the different pieces of clothing and not what is hidden/revealed.
            return sum(x.slut_score for x in self)
