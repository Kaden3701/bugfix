init -15 python:
    class Facial_Accessory(Clothing): #This class inherits from Clothing and is used for special accessories that require extra information
        _position_sets = {}
        def get_position_sets(self):
            if not self.proper_name in self._position_sets:
                self._position_sets[self.proper_name] = {}
            return self._position_sets[self.proper_name]

        def set_position_sets(self, value):
            self._position_sets[self.proper_name] = value

        position_sets = property(get_position_sets, set_position_sets, None, "Facial Accessory position sets")

        def get_crop_offset_dict(self):
            return master_clothing_offset_dict.get(self.proper_name, {})

        crop_offset_dict = property(get_crop_offset_dict, None, None, "Offset dictionary")

        def __init__(self, name, layer, hide_below, anchor_below, proper_name, draws_breasts, underwear, slut_value, has_extension = None, is_extension = False, colour = None, tucked = False,
            opacity_adjustment = 1, whiteness_adjustment = 0.0, contrast_adjustment = 1.0, display_name = None, crop_offset_dict = None, modifier_lock = None):

            self.name = name
            if display_name is None:
                self.display_name = name
            else:
                self.display_name = display_name
            self.proper_name = proper_name
            self.hide_below = hide_below #If true, it hides the clothing beneath so you can't tell what's on.
            self.anchor_below = anchor_below #If true, you must take this off before you can take off anything of a lower layer.f
            self.layer = layer #A list of the slots above that this should take up or otherwise prevent from being filled. Slots are a list of the slot and the layer.

            self.half_off = False # Avoids any problems with the half-off system using facial accessories
            self.half_off_reveals = False
            self.half_off_clothing = False

            # self.half_off_regions = []
            # self.half_off_ignore_regions = []

            for set in supported_positions:
                self.position_sets[set] = Facial_Accessory_Images(proper_name,set)

            # self.crop_offset_dict = master_clothing_offset_dict.get(self.proper_name, {})

            self.draws_breasts = draws_breasts
            self.underwear = underwear #True if the item of clothing satisfies the desire for underwear for upper or lower (bra or panties), false if it can pass as outerwear. Underwear on outside of outfit gives higher slut requirement.
            self.slut_value = slut_value #The amount of sluttiness that this piece of clothing adds to an outfit.
            self.has_extension = has_extension
            self.is_extension = is_extension #If this is true the clothing item exists only as a placeholder. It will draw nothing and not be removed unless the main piece is removed.
            if not colour:
                self.colour = [1,1,1,1]
            else:
                self.colour = colour
            self.tucked = tucked #Items of clothing that are tucked are drawn a "half level", aka we cycle through all layer 2's and do untucked items, then do all tucked items.

            self.opacity_adjustment = opacity_adjustment
            self.whiteness_adjustment = whiteness_adjustment
            self.contrast_adjustment = contrast_adjustment

            self.modifier_lock = modifier_lock #If set to something other than None this facial accessory adds the modifier to all positions if possible.

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if (self.name == other.name
                    and self.hide_below == other.hide_below
                    and self.layer == other.layer
                    and self.is_extension == other.is_extension
                    and self.colour == other.colour):

                    return 0

            if self.__hash__() < other.__hash__():
                return -1
            else:
                return 1

        def is_similar(self, other):
            if type(self) is type(other):
                if (self.name == other.name
                    and self.hide_below == other.hide_below
                    and self.layer == other.layer
                    and self.is_extension == other.is_extension):

                    return True

            return False

        def __hash__(self):
            return hash((self.name, self.hide_below, self.layer, self.is_extension, self.draws_breasts, self.underwear, self.slut_value))

        def generate_item_displayable(self, position, face_type, emotion, special_modifiers = None, lighting = None):
            if self.is_extension:
                return

            if lighting is None:
                lighting = [1,1,1]

            image_set = self.position_sets.get(position)
            if image_set is None:
                image_set = self.position_sets.get("stand3") #Get a default image set if we are looking at a position we do not have.

            the_image = image_set.get_image(face_type, emotion, special_modifiers)
            if not the_image:
                the_image = image_set.get_image(face_type, emotion) # If we weren't able to get something with the special modifier just use a default to prevent a crash.

            brightness_matrix = im.matrix.brightness(self.whiteness_adjustment)
            contrast_matrix = im.matrix.contrast(self.contrast_adjustment)
            opacity_matrix = im.matrix.opacity(self.opacity_adjustment) #Sets the clothing to the correct colour and opacity.

            greyscale_image = im.MatrixColor(the_image, opacity_matrix * brightness_matrix * contrast_matrix) #Set the image, which will crush all modifiers to 1 (so that future modifiers are applied to a flat image correctly with no unusually large images

            colour_matrix = im.matrix.tint(self.colour[0], self.colour[1], self.colour[2]) * im.matrix.tint(*lighting)
            alpha_matrix = im.matrix.opacity(self.colour[3])
            shader_image = im.MatrixColor(greyscale_image, alpha_matrix * colour_matrix) #Now colour the final greyscale image

            return Composite(position_size_dict[position], self.crop_offset_dict.get(position,(0,0)), shader_image)

        def generate_raw_image(self, position, face_type, emotion, special_modifier):
            image_set = self.position_sets.get(position)
            if image_set is None:
                image_set = self.position_sets.get("stand3") #Get a default image set if we are looking at a position we do not have.

            the_image = image_set.get_image(face_type, emotion, special_modifiers)
            if not the_image:
                the_image = image_set.get_image(face_type, emotion) # If we weren't able to get something with the special modifier just use a default to prevent a crash.

            return the_image
