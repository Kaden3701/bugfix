init -2 python:
    color_clothing_map = {
        "Jean_Hotpants": ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Daisy_Dukes" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Jeans" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Suit_Pants" : ["the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"],
        "Capris" : ["the colour black", "the colour blue", "the colour brown", "the colour white"],
        "Pencil_Skirt": ["the colour black", "the colour blue", "the colour brown", "the colour white", "the colour red", "the colour yellow", "the colour green"],
        "Short_Socks" : ["the colour black", "the colour white", "the colour red"],
        "Long_Socks" : ["the colour black", "the colour white", "the colour red"],
        "High_Socks" : ["the colour black", "the colour white", "the colour red", "the colour pink", "the colour yellow"],
        "Slips": ["the colour black", "the colour white", "the colour brown"],
        "Shoes" : ["the colour black", "the colour white", "the colour brown"],
        "Sneakers" : ["the colour black", "the colour white", "the colour red"],
        "Sandal_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "High_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Boot_Heels": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "High_Boots": ["the colour black", "the colour white", "the colour red", "the colour brown"],
        "Gold_Earings": ["the colour yellow"],
        "Copper_Bracelet": ["the colour yellow"],
        "Diamond_Ring": ["the colour yellow"],
        "Copper_Ring_Set": ["the colour yellow"],
        "Spiked_Bracelet": ["the colour white"],
        "Spiked_Choker": ["the colour white"],
    }

    #Use this to define a set of neutral colors, useful for colors that match most anything else.
    neutral_colors = {
        "khaki": [.765, .69, .569, .95],
        "swiss coffee": [.859, .331, .321, .95], #wut? this is salmon colored lol
        "light grey": [.827, .827, .827, .95],
        "cotton white": [.992, .953, .918, .95],
        "dark grey": [.365, .365, .365, .95],
        "midnight black": [.15, .15, .15, .95]
    }

    neutral_palette = {
        "dark denim": [0, .278, .671, .95],
        "denim": [.082, .376, .741, .95],
        "light denim": [.365, .678, .925, .95],
        "midnight black": [.15, .15, .15, .95],
        "khaki": [.765, .69, .569, .95],
        "dark grey": [.365, .365, .365, .95],
        "indian yellow": [.89, .659, .341, .95],
        "grey": [.502, .502, .502, .95],
        "light grey": [.827, .827, .827, .95],
        "sky blue": [.529, .808, .922, 0.95],
        "antique white": [.98, .922, .843, .95],
        "white smoke": [.95, .95, .95, .95],
        "light beige": [.94, .94, .78, .95],
        "leather": [.384, .29, .18, .95],
        "mocha": [.514, .373, .345, .95],
        "charcoal": [.212, .271, .31, .95],
        "scarlet": [1, .141, .0, .95],    #Looks decent for some patterns, might have to delete
        "pale pink": [.98, .885, .867, .95],
        "berry": [.478, .09, .071, .95],
    }

    neutral_color_map = {
        "Jeans": ["dark denim", "denim", "light denim", "midnight black", "dark grey"],
        "Suit_Pants": ["midnight black", "leather", "khaki", "grey", "berry"],
        "Capris": ["dark denim", "denim", "dark grey"],
        "Leggings": ["midnight black", "dark grey", "leather", "berry", "indian yellow"],
        "Leggings_Pattern": ["pale pink", "light grey", "white smoke"],
        "Jean_Hotpants": ["dark denim", "denim", "light denim", "midnight black", "dark grey"],
        "Booty_Shorts": ["midnight black", "dark grey", "leather", "berry"],
        "Daisy_Dukes": ["light denim", "sky blue", "dark grey"],

        "Long_Skirt": ["midnight black", "leather"],
        "Pencil_Skirt": ["midnight black", "dark grey", "leather", "grey", "khaki", "white smoke", "berry", "indian yellow"],
        "Lace_Skirt": ["midnight black", "leather", "white smoke", "light grey"],
        "Skirt": ["khaki", "light grey", "leather", "light beige", "white smoke"],
        "Belted_Skirt": ["khaki", "grey", "leather", "light grey", "berry"],
        "Belted_Skirt_Pattern": ["leather", "dark grey"],
        "Mini_Skirt": ["khaki", "dark grey", "leather", "white smoke", "berry"],
        "Micro_Skirt": ["midnight black", "leather", "light grey", "white smoke"],

        "Lab_Coat": ["midnight black", "white smoke", "light grey"],
        "Suit_Jacket": ["midnight black", "white smoke", "dark denim", "dark grey"],
        "Vest": ["midnight black", "white smoke", "light grey", "leather"],

        "Short_Socks": ["white smoke", "light grey", "midnight black", "berry"],
        "Long_Socks": ["midnight black", "white smoke", "berry"],
        "High_Socks": ["midnight black", "white smoke", "light grey", "berry"],
        "Thigh_Highs": ["midnight black", "white smoke", "light grey", "mocha", "berry"],
        "Fishnets": ["midnight black", "white smoke", "dark grey", "berry"],
        "Garter_and_Fishnets": ["charcoal", "dark grey", "grey", "white smoke", "berry"],
        "Garter_and_Fishnets_Pattern": ["charcoal", "white smoke"],

        "Sandles": ["white smoke", "midnight black", "leather", "grey"],
        "Shoes": ["leather", "light grey"],
        "Slips": ["leather", "white smoke", "midnight black", "mocha", "dark grey"],
        "Sneakers": ["grey", "white smoke", "light beige"],
        "Sneakers_Pattern": ["white smoke"],
        "Sandal_Heels": ["midnight black", "grey", "white smoke", "light beige"],
        "Pumps": ["white smoke", "charcoal"],
        "Heels": ["midnight black", "charcoal", "white smoke"],
        "High_Heels": ["midnight black", "white smoke", "grey"],
        "Boot_Heels": ["leather", "grey"],
        "High_Boots": ["charcoal", "leather"],
        "Thigh_Boots": ["charcoal", "leather", "light grey"],

        "Tshirt": ["midnight black", "dark grey", "white smoke", "berry", "indian yellow"],
        "Tshirt_Pattern": ["grey", "light grey", "berry"],
        "Lace_Sweater": ["white smoke", "light grey", "midnight black", "berry", "indian yellow"],
        "Long_Sweater": ["midnight black", "light grey", "white smoke", "berry", "indian yellow"],
        "Sleveless_Top": ["midnight black", "dark grey", "white smoke", "berry", "indian yellow"],
        "Long_Tshirt": ["midnight black", "white smoke", "dark grey", "berry", "indian yellow"],
        "Long_Tshirt_Pattern": ["white smoke", "light grey", "light beige", "berry"],
        "Frilly_Longsleeve_Shirt": ["white smoke", "dark grey", "charcoal", "berry", "indian yellow"],
        "Sweater": ["leather", "white smoke", "charcoal", "khaki", "berry", "indian yellow"],
        "Belted_Top": ["leather", "khaki", "grey", "white smoke", "charcoal", "berry", "indian yellow"],
        "Lace_Crop_Top": ["charcoal", "light beige", "light grey", "white smoke", "berry", "indian yellow"],
        "Tanktop": ["leather", "white smoke", "grey", "midnight black", "berry", "indian yellow"],
        "Camisole": ["midnight black", "dark grey", "white smoke", "berry", "indian yellow"],
        "Long_Sleeve_Blouse": ["white smoke", "midnight black", "sky blue", "berry", "indian yellow"],
        "Short_Sleeve_Blouse": ["charcoal", "white smoke", "light beige", "light grey", "berry", "indian yellow"],
        "Wrapped_Blouse": ["charcoal", "light beige", "white smoke", "berry", "indian yellow"],
        "Tube_Top": ["white smoke", "midnight black", "dark grey", "charcoal", "berry", "indian yellow"],
        "Tie_Sweater": ["midnight black", "dark grey", "white smoke", "berry", "indian yellow"],
        "Tie_Sweater_Pattern": ["scarlet", "pale pink", "light grey", "light beige"],
        "Dress_Shirt": ["charcoal", "grey", "white smoke", "berry", "indian yellow"],
        "Tight_Vest": ["white smoke", "light beige", "dark grey", "charcoal", "berry", "indian yellow"],

        "Wool_Scarf": ["khaki", "charcoal", "grey", "white smoke", "berry", "indian yellow"],
        "Lace_Choker": ["charcoal", "white smoke", "dark grey", "berry", "pale pink", "indian yellow"],
        "Wide_Choker": ["charcoal", "white smoke", "dark grey", "berry", "pale pink", "indian yellow"],
        "Spiked_Choker": ["charcoal", "white smoke", "dark grey", "pale pink"],
        # "Necklace_Set"
        # "Gold_Chain_Necklace"
        # "Collar_Breed"    # probably just leave these collars alone...
        # "Collar_Cum_Slut"
        # "Collar_Fuck_Doll"

        "Forearm_Gloves": ["charcoal", "light beige", "light grey", "white smoke", "berry"],
        "Forearm_Gloves_Pattern": ["charcoal", "pale pink", "white smoke"],
        # "Copper_Bracelet"
        # "Gold_Bracelet"
        # "Spiked_Bracelet"
        # "Bead_Bracelet"
        # "Colourful_Bracelets"
        #
        # "Diamond_Ring"
        # "Garnet_Ring"
        # "Copper_Ring_Set"

        # "Chandelier_Earings" #TODO
        # "Gold_Earings"
        "Modern_Glasses": ["charcoal", "midnight black"],
        "Big_Glasses": ["charcoal", "midnight black"],
        "Sunglasses": ["charcoal", "midnight black"],
        "Head_Towel": ["white smoke"],
        # "Ball_Gag"
        # "Upper_Eye_Shadow"
        # "Full_Shimmer"
        # "Blush"
        # "Lipstick"


        "Underwear": ["charcoal", "white smoke", "dark grey", "pale pink"]
    }

    swap_bottoms_map = {
        "Jeans": [long_skirt],
        "Suit_Pants": [pencil_skirt, long_skirt],
        "Capris": [pencil_skirt, skirt],
        "Leggings": [skirt, lace_skirt],
        "Jean_Hotpants": [lace_skirt, belted_skirt],
        "Booty_Shorts": [mini_skirt, belted_skirt],
        "Daisy_Dukes": [mini_skirt, micro_skirt],

        "Long_Skirt": [jeans, suitpants],
        "Pencil_Skirt": [suitpants, capris],
        "Lace_Skirt": [leggings, capris],
        "Skirt": [capris, leggings],
        "Belted_Skirt": [leggings, jean_hotpants],
        "Mini_Skirt": [booty_shorts, daisy_dukes],
        "Micro_Skirt": [daisy_dukes]
    }

    coverup_upper_list = [lab_coat, suit_jacket, vest]
    coverup_lower_list = []

    # exclude list is a list of girl color preference (red, blue, green etc.) she hates
    def neutralize_item_colour(item, exclude_list = []):
        def build_preference_colors(color_list, exclude_list):
            neutral_colors = [neutral_palette[x] for x in color_list]
            if not exclude_list:
                return neutral_colors
            neutral_list = [x for x in neutral_colors if not WardrobeBuilder.get_color_opinion(x) in exclude_list]
            if not neutral_list:
                return neutral_colors
            return neutral_list

        if item is None:
            return None

        current_alpha = item.colour[3]
        if item in real_bra_list or item in panties_list:
            item.colour = renpy.random.choice(build_preference_colors(neutral_color_map["Underwear"], exclude_list))
            item.pattern = None
            item.colour[3] = current_alpha
            return item

        if item in dress_list and item not in real_dress_list:
            item.colour = renpy.random.choice(build_preference_colors(neutral_color_map["Underwear"], exclude_list))
            item.pattern = None
            item.colour[3] = current_alpha
            return item

        if item.proper_name in neutral_color_map.keys():
            item.colour = renpy.random.choice(build_preference_colors(neutral_color_map[item.proper_name], exclude_list))
            item.colour[3] = current_alpha
            if item.proper_name == "Sneakers": #For sneakers we always set the pattern color to white (laces)
                item.pattern = item.supported_patterns[renpy.random.choice(item.supported_patterns.keys())]
                color_key = item.proper_name + "_Pattern"
                pattern_alpha = item.colour_pattern[3]
                item.colour_pattern = renpy.random.choice(build_preference_colors(neutral_color_map[color_key], exclude_list))
                item.colour_pattern[3] = pattern_alpha
            elif isinstance(item, Facial_Accessory):    #facial accessories don't have patterns
                pass
            elif item.pattern:
                color_key = item.proper_name + "_Pattern"
                if color_key in neutral_color_map.keys():
                    pattern_alpha = item.colour_pattern[3]
                    item.colour_pattern = renpy.random.choice(build_preference_colors(neutral_color_map[color_key], exclude_list))
                    item.colour_pattern[3] = pattern_alpha
                else:
                    item.colour_pattern = item.colour   #Preserve the pattern to possibly colorize later
        return item

    def swap_outfit_bottoms(outfit):
        for item in outfit.lower_body:
            if (item in real_pants_list or item in skirts_list) and item.proper_name in swap_bottoms_map.keys():
                swap_item = get_random_from_list(swap_bottoms_map[item.proper_name]).get_copy()
                swap_item.colour = item.colour
                outfit.lower_body.remove(item)
                outfit.add_lower(swap_item)
                return outfit
        return outfit

    def enhance_existing_wardrobe(person, max_outfits):
        outfit_builder = WardrobeBuilder(person)

        while __builtin__.len(person.wardrobe.outfit_sets) < max_outfits:    # add some generated outfits
            outfit = outfit_builder.build_outfit("full", renpy.random.randint(2, 6) * 2)
            if outfit.has_overwear and outfit_builder.approves_outfit_color(outfit):
                person.wardrobe.add_outfit(outfit)

        while __builtin__.len(person.wardrobe.overwear_sets) < max_outfits:    # add some generated outfits
            overwear = outfit_builder.build_outfit("over", renpy.random.randint(2, 6) * 2)
            if overwear.is_suitable_overwear_set and outfit_builder.approves_outfit_color(overwear):
                person.wardrobe.add_overwear_set(overwear)

        while __builtin__.len(person.wardrobe.underwear_sets) < max_outfits:    # add some generated outfits
            underwear = outfit_builder.build_outfit("under", renpy.random.randint(2, 6) * 2)
            if underwear.is_suitable_underwear_set and outfit_builder.approves_outfit_color(underwear):
                person.wardrobe.add_underwear_set(underwear)

        return

    def add_make_up_to_outfit(person, outfit, make_up_score_boost = 0):
        # determine make-up colors based on skin-tone
        if person.body_images == black_skin:
            eye_shadow_colours = [[.569, .349, .263, .9], [0, .2, .4, .9], [.47, .318, .663, .9]]
            lipstick_colours = [[.569, .318, .212, .8], [.451, .416, .526, .8], [.492, .419, .384, .8]]
            blush_colours = [[.435, .306, .216, .6], [.588, .251, 0, .6], [.451, .412, .576, .6]]
        else:
            eye_shadow_colours = [[.1, .1, .12, .9], [.4, .5, .9, .9], [.644, .418, .273, .9]]
            lipstick_colours = [[.745, .117, .235, .8], [1, .5, .8, .8], [ .8, .26, .04, .8]]
            blush_colours = [[.34, .34, .32, .6], [1, .898, .706, .6], [.867, .627, .867, .6]]

        make_up_score = person.get_opinion_score("makeup") + make_up_score_boost
        if make_up_score > 0 or (make_up_score <= 0 and renpy.random.randint(0, 4) == 0):
            make_up_score += renpy.random.randint(1, 2)
            if make_up_score > 0:
                outfit.add_accessory(light_eye_shadow.get_copy(), renpy.random.choice(eye_shadow_colours))
            if make_up_score > 1:
                outfit.add_accessory(heavy_eye_shadow.get_copy(), renpy.random.choice(eye_shadow_colours))
            if make_up_score > 2:
                outfit.add_accessory(lipstick.get_copy(), renpy.random.choice(lipstick_colours))
            if make_up_score > 3:
                outfit.add_accessory(blush.get_copy(), renpy.random.choice(blush_colours))
        return

    real_bra_list = [x for x in bra_list if x not in [cincher, heart_pasties]]
    real_pants_list = [x for x in pants_list if not x in [cop_pants]]
    real_shirt_list = [x for x in shirts_list if not x in [cop_blouse, lab_coat]]
    real_dress_list = [x for x in dress_list if x not in [bath_robe, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, apron, nightgown_dress, sweater_dress]]
    only_socks_list = [x for x in socks_list if x not in [thigh_highs, fishnets, garter_with_fishnets]]
    real_pantyhose_list = [x for x in socks_list if x not in only_socks_list]
    earings_only_list = [chandelier_earings, gold_earings, modern_glasses]
    neckwear_without_collars = [x for x in neckwear_list if x.proper_name not in ["Collar_Breed", "Collar_Cum_Slut", "Collar_Fuck_Doll", "Wool_Scarf", "Spiked Choker"]]
    makeup_list = [lipstick, light_eye_shadow, heavy_eye_shadow, blush]

    class WardrobeBuilder():
        default_person = None

        preferences = {}
        preferences["skimpy outfits"] = {}
        preferences["skimpy outfits"]["upper_body"] = [two_part_dress, thin_dress, leotard, lace_sweater, belted_top, lace_crop_top, frilly_longsleeve_shirt, tanktop, tube_top, business_vest, kitty_babydoll]
        preferences["skimpy outfits"]["lower_body"] = [booty_shorts, jean_hotpants, daisy_dukes, belted_skirt, mini_skirt, micro_skirt]
        preferences['skimpy outfits']["feet"] = [thigh_highs, fishnets, garter_with_fishnets, pumps, heels, high_heels, thigh_high_boots]
        preferences["skimpy outfits"]["accessories"] = [lace_choker, wide_choker, spiked_choker]
        preferences["conservative outfits"] = {}
        preferences["conservative outfits"]["upper_body"] = [long_sweater, sleeveless_top, long_tshirt, camisole, long_sleeve_blouse, short_sleeve_blouse, tie_sweater, dress_shirt, sweater_dress, bra, bralette, sports_bra, lab_coat, vest, suit_jacket]
        preferences["conservative outfits"]["lower_body"] = [pencil_skirt, skirt, long_skirt, jeans, suitpants, panties, plain_panties, cotton_panties, boy_shorts, kitty_panties]
        preferences["conservative outfits"]["feet"] = [sandles, shoes, slips, sneakers, short_socks]
        preferences["conservative outfits"]["accessories"] = [wool_scarf]
        preferences["dresses"] = {}
        preferences["dresses"]["upper_body"] = real_dress_list
        preferences["skirts"] = {}
        preferences["skirts"]["lower_body"] = skirts_list
        preferences["pants"] = {}
        preferences["pants"]["lower_body"] = real_pants_list
        preferences["showing her tits"] = {}
        preferences["showing her tits"]["upper_body"] = [strapless_bra, lace_bra, strappy_bra, quarter_cup_bustier, cincher, heart_pasties, thin_dress, two_part_dress, pinafore, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, lace_sweater, sweater, belted_top, tube_top, business_vest, suit_jacket, vest]
        preferences["showing her ass"] = {}
        preferences["showing her ass"]["upper_body"] = [two_part_dress, thin_dress, summer_dress, virgin_killer, frilly_dress, leotard, lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear]
        preferences["showing her ass"]["lower_body"] = [cute_panties, lace_panties, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string, string_panties, strappy_panties, crotchless_panties, leggings, booty_shorts, jean_hotpants, daisy_dukes, micro_skirt]
        preferences["high heels"] = {}
        preferences["high heels"]["feet"] = [sandle_heels, pumps, heels, high_heels, boot_heels, thigh_high_boots]
        preferences["boots"] = {}
        preferences["boots"]["feet"] = [boot_heels, tall_boots, thigh_high_boots]
        preferences["makeup"] = {}
        preferences["makeup"]["accessories"] = [light_eye_shadow, heavy_eye_shadow, blush, lipstick]
        preferences['lingerie'] = {}
        preferences['lingerie']["upper_body"] = [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear, strapless_bra, lace_bra, thin_bra, strappy_bra, cincher, corset, heart_pasties]
        preferences['lingerie']["lower_body"] = [lace_panties, cute_lace_panties, tiny_lace_panties, thin_panties, thong, tiny_g_string, string_panties, strappy_panties]
        preferences['lingerie']["feet"] = [thigh_highs, fishnets, garter_with_fishnets]
        preferences['lingerie']['accessories'] = [lace_choker, wide_choker]

        matching_underwear = {}
        matching_underwear["Bralette"] = [boy_shorts, cute_lace_panties, tiny_lace_panties, thong, tiny_g_string]
        matching_underwear["Sports_Bra"] = [cotton_panties, panties, lace_panties]
        matching_underwear["Lace_Bra"] = [cute_lace_panties, lace_panties, tiny_lace_panties, thong, tiny_g_string, crotchless_panties]
        matching_underwear["Strappy_Bra"] = [strappy_panties]
        matching_underwear["Corset"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]
        matching_underwear["Kitty_Babydoll"] = [kitty_panties, thong, kitty_panties, strappy_panties, kitty_panties]
        matching_underwear["Cincher"] = [panties, thin_panties, thong, tiny_lace_panties, tiny_g_string, string_panties, crotchless_panties]

        color_prefs = {}
        color_prefs["the colour blue"] = OrderedDict([
            ("dark slate blue", [.282, .239, .545, .95]),
            ("dark denim", [0, .278, .671, .95]),
            ("denim", [.082, .376, .741, .95]),
            ("steel blue", [.0275, .51, .706, .95]),
            ("light denim", [.365, .678, .925, .95]),
            ("cornflower blue", [.392, .584, .929, .95]),
            ("sky blue", [.529, .808, .922, 0.95]),
        ])
        color_prefs["the colour yellow"] = OrderedDict([
            ("khaki", [.765, .69, .569, .95]),
            ("indian yellow", [.89, .659, .341, .95]),
            ("saffron", [.96, .77, .19, .95]),
            ("corn", [.98, .92, .36, .95]),
        ])
        color_prefs["the colour red"] = OrderedDict([
            ("bordeaux red", [.38, .118, .149, .95]),
            ("berry", [.478, .09, .071, .95]),
            ("sinopia", [.80, .26, .04, .95]),
            ("vermillion", [.890, .258, .203, .95]),
            ("debian red", [.843, .039, .325, .95]),
        ])
        color_prefs["the colour pink"] = OrderedDict([
            ("dark pink", [.906, .329, .502, .95]),
            ("hot pink", [1, .412, .706, .95]),
            ("cotton candy", [1, .733, .851, .95]),
            ("pale pink", [.98, .885, .867, .95]),
        ])
        color_prefs["the colour black"] = OrderedDict([
            ("midnight black", [.15, .15, .15, .95]),
            ("charcoal", [.212, .271, .31, .95]),
            ("dark grey", [.365, .365, .365, .95]),
            ("warm black", [0, .26, .36, .95]),
        ])
        color_prefs["the colour green"] = OrderedDict([
            ("army green", [.294, .325, .125, .95]),
            ("sea green", [.18, .545, .341, .95]),
            ("jade", [.0, .659, .43 , .95]),
            ("caribbean green", [.0, .8, .6, .95]),
            ("pistachio", [.576, .772, .447, .95]),
        ])
        color_prefs["the colour purple"] = OrderedDict([
            ("palatinate purple", [.41, .16, .38, .95]),
            ("dark lavender", [.45, .31, .59, .95]),
            ("mauve", [.878, .690, 1, .95]),
            ("rich lilac", [.714, .4, .824, .95]),
        ])
        color_prefs["the colour orange"] = OrderedDict([
            ("burnt orange", [.8, .33, 0, .95]),
            ("tigers eye", [.878, .552, .235, .95]),
            ("honey orange", [.89, .6, .16, .95]),
            ("swiss coffee", [.859, .331, .321, .95]),
        ])
        color_prefs["the colour white"] = OrderedDict([
            ("antique white", [.98, .922, .843, .95]),
            ("cotton white", [.992, .953, .918, .95]),
            ("white smoke", [.95, .95, .95, .95]),
            ("ghost white", [.97, .97, 1, .95]),
        ])
        color_prefs["the colour brown"] = OrderedDict([
            ("leather", [.384, .29, .18, .95]),
            ("coffee", [.435, .305, .215, .95]),
            ("saddle brown", [.451, .313, .235, .95]),
            ("mocha", [.514, .373, .345, .95]),
            ("khaki", [.765, .69, .569, .95]),
            ("chocolate noir", [.352, 0.239, .239, .95]),
            ("light beige", [.94, .94, .78, .95]),
        ])
        #color_prefs[""][""] = [, , , ]

        @staticmethod
        def clothing_in_preferences(topic, clothing):
            return any(clothing in WardrobeBuilder.preferences[topic][x] for x in WardrobeBuilder.preferences[topic].keys())

        @staticmethod
        def get_color_from_opinion_color(opinion_color):
            return get_random_from_list([WardrobeBuilder.color_prefs[opinion_color][x][:] for x in WardrobeBuilder.color_prefs[opinion_color]])

        @staticmethod
        def get_item_color(item, color, exclude_list = [], multiplier = 1.0):
            if item.proper_name in color_clothing_map:
                # exclude hate list
                available_list = list(set(color_clothing_map[item.proper_name]) - set(exclude_list))
                if not available_list:
                    # no color left revert to original list
                    available_list = color_clothing_map[item.proper_name]

                # color not match list
                if not WardrobeBuilder.get_color_opinion(color) in available_list:
                    color_set = WardrobeBuilder.color_prefs[renpy.random.choice(available_list)]
                    color_name = renpy.random.choice(color_set.keys())
                    color = color_set[color_name][:]
                    return [color[0] * multiplier, color[1] * multiplier, color[2] * multiplier, color[3]]
            return [color[0] * multiplier, color[1] * multiplier, color[2] * multiplier, color[3]]

        @staticmethod
        def get_color_opinion(colour):
            if isinstance(colour, list) and len(colour) >= 3:
                color_name = closest_preference_color(Color(rgb=(colour[0], colour[1], colour[2])))

                for opinion in WardrobeBuilder.color_prefs:
                    if color_name in WardrobeBuilder.color_prefs[opinion]:
                        return opinion

            return "the colour black" # default fallback

        @staticmethod
        def get_color(person, base_color = None):
            def get_excluded(base_color):
                if base_color:
                    # prevents clashing colours
                    opinion_color = WardrobeBuilder.get_color_opinion(base_color)
                    if opinion_color == "the colour red":
                        return ["the colour pink", "the colour purple", "the colour brown"]
                    if opinion_color == "the colour pink":
                        return ["the colour red", "the colour purple", "the colour brown"]
                    if opinion_color == "the colour purple":
                        return ["the colour red", "the colour pink", "the colour blue"]
                    if opinion_color == "the colour blue":
                        return ["the colour purple"]
                    if opinion_color == "the colour orange":
                        return ["the colour yellow"]
                    if opinion_color == "the colour yellow":
                        return ["the colour orange"]
                    if opinion_color == "the colour brown":
                        return ["the colour black", "the colour pink", "the colour red"]
                    if opinion_color == "the colour black":
                        return ["the colour brown"]
                return []

            color_list = []
            for cp in [x for x in WardrobeBuilder.color_prefs if x not in get_excluded(base_color)]:
                score = person.get_opinion_score(cp)
                if score > -2: # don't append colors she hates
                    color_list.extend([[WardrobeBuilder.color_prefs[cp][x][:], (score + 2) ** 2] for x in WardrobeBuilder.color_prefs[cp]])

            if not color_list:  # if she hates all colours
                for cp in WardrobeBuilder.color_prefs:
                    color_list.extend([[WardrobeBuilder.color_prefs[cp][x][:], 5] for x in WardrobeBuilder.color_prefs[cp]])

            return get_random_from_weighted_list(color_list)

        @staticmethod
        def get_main_color_scheme(person, match_percent = 60):
            primary_color = WardrobeBuilder.get_color(person)
            alternate_color = WardrobeBuilder.get_color(person, primary_color)

            col_choice = renpy.random.randint(0, 100)
            lower_percent = (100 - match_percent) // 2
            if col_choice < lower_percent:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = primary_color
            elif col_choice >= lower_percent and col_choice < match_percent:
                color_upper = primary_color
                color_lower = primary_color
                color_feet = alternate_color
            else:
                color_upper = primary_color
                color_lower = alternate_color
                color_feet = alternate_color

            # print("Upper: {}, Lower: {}, Feet: {}".format(
            #     closest_preference_color(Color(rgb=(color_upper[0], color_upper[1], color_upper[2]))),
            #     closest_preference_color(Color(rgb=(color_lower[0], color_lower[1], color_lower[2]))),
            #     closest_preference_color(Color(rgb=(color_feet[0], color_feet[1], color_feet[2])))))

            return (color_upper, color_lower, color_feet)

        @staticmethod
        def build_filter_list(item_list, points, min_points = 0, filter_list = [], layers = [1, 2, 3, 4]):
            # extend range until we have items
            while not any(x for x in item_list if x.slut_value >= min_points and x.slut_value <= points and x.layer in layers and x not in filter_list):
                if min_points == 0 and points < 15: # only extend up if we reach bottom
                    points +=1
                if min_points > 0:
                    min_points -= 1
            return [x for x in item_list if x.slut_value >= min_points and x.slut_value <= points and x.layer in layers and x not in filter_list]

        @staticmethod
        def build_weighted_list(person, item_group, filtered_list):
            item_list = [[x, 1, True] for x in filtered_list]
            for pref in WardrobeBuilder.preferences:
                score = person.get_opinion_score(pref)
                for name in [x for x in WardrobeBuilder.preferences[pref] if x == item_group]:
                    for item in [x for x in WardrobeBuilder.preferences[pref][name] if x in filtered_list]:
                        found = next((x for x in item_list if x[0]==item), None)
                        if score == -2:
                            found[2] = False
                        found[1] += (score + 2) ** 2

            # first return pref without hated, then without pref and hate, then with pref, then any item
            return [x for x in item_list if x[1] > 1 and x[2]] \
                or [x for x in item_list if x[1] > 0 and x[2]] \
                or [x for x in item_list if x[1] > 1] \
                or [x for x in item_list if x[1] > 0]

        @staticmethod
        def add_accessory_from_list(outfit, filtered_list, chance, item_color = [.8, .1, .1, .95]):
            if renpy.random.randint(0, chance) == 0:
                item = get_random_from_list(filtered_list)
                if item:
                    outfit.add_accessory(item.get_copy(), WardrobeBuilder.get_item_color(item, item_color))
            return

        @staticmethod
        def get_item_from_list(person, item_group, filtered_list, points = 0, empty_item_opinions = [], no_pattern = False):
            weighted_list = WardrobeBuilder.build_weighted_list(person, item_group, filtered_list)

            item = get_random_from_weighted_list(weighted_list)
            if not item:    # make sure we have an item from the list
                item = get_random_from_list(filtered_list)

            if no_pattern:
                return item

            # force pattern for certain items, others random 50/50
            if item and hasattr(item, "supported_patterns") and item.supported_patterns and \
                (renpy.random.randint(0, 1) == 1 or item in [apron, breed_collar, cum_slut_collar, fuck_doll_collar]):
                item = item.get_copy() # get copy before applying pattern
                item.pattern = item.supported_patterns[renpy.random.choice(item.supported_patterns.keys())]
                item.colour_pattern = WardrobeBuilder.get_color(person, item.colour)
                item.colour_pattern[3] = .80 + (renpy.random.randint(0, 15) / 100.0)    # random pattern transparency
            return item

        @staticmethod
        def get_clothing_min_max_slut_value(sluttiness):
            base_sluttiness = __builtin__.max(sluttiness - 15, 0) # first 15 points of sluttiness don't impact outfit builder
            min_sluttiness = __builtin__.min(base_sluttiness / 18, 5) if sluttiness > 50 else 0 # prevent override of person preferences until she's slutty enough not to care
            return (min_sluttiness, __builtin__.min(base_sluttiness / 7, 12))

        @staticmethod
        def apply_bottom_preference(person, outfit):
            swapped = False
            if outfit.has_pants and person.get_opinion_score("skirts") > person.get_opinion_score("pants"): #Outfit has pants and girl prefers skirts
                outfit = swap_outfit_bottoms(outfit)
                swapped = True
            elif outfit.has_skirt and person.get_opinion_score("skirts") < person.get_opinion_score("pants"):
                outfit = swap_outfit_bottoms(outfit)
                swapped = True
            return outfit, swapped

        @staticmethod
        def set_sexier_panties(person, outfit, the_color = None):
            panties = outfit.get_panties()
            if not panties is None and panties.is_extension: # one-piece
                return False
            (min_slut, max_slut) = WardrobeBuilder.get_clothing_min_max_slut_value(person.sluttiness)

            if panties and panties.slut_value >= min_slut:
                return False

            new_panties = get_random_from_list([x for x in panties_list if x.slut_value >= min_slut and x.slut_value <= max_slut])
            if new_panties:
                if the_color is None and panties:
                    new_panties.colour = panties.colour
                else:
                    bra = outfit.get_bra()
                    if the_color is None and bra:
                        the_color = bra.colour

                    new_panties.colour = the_color or WardrobeBuilder.get_color_from_opinion_color(person.favourite_colour)
                    if panties:
                        new_panties.colour[3] = panties.colour[3]   # preseve original alpha

                if panties:
                    outfit.remove_clothing(panties)
                outfit.add_lower(new_panties)
                return True
            return False

        @staticmethod
        def set_sexier_bra(person, outfit, the_color = None, allow_remove_bra = True):
            bra = outfit.get_bra()
            if not bra is None and bra.has_extension: # one-piece
                return False
            (min_slut, max_slut) = WardrobeBuilder.get_clothing_min_max_slut_value(person.sluttiness)

            if bra and bra.slut_value >= min_slut:
                return False

            if allow_remove_bra and outfit.get_panties() is None:   # also remove bra if not wearing panties
                outfit.remove_clothing(bra)
                return True

            new_bra = get_random_from_list([x for x in real_bra_list if x.slut_value >= min_slut and x.slut_value <= max_slut])
            if new_bra:
                if the_color is None and bra:
                    new_bra.colour = bra.colour
                else:
                    panties = outfit.get_panties()
                    if the_color is None and panties:
                        the_color = panties.colour

                    new_bra.colour = the_color or WardrobeBuilder.get_color_from_opinion_color(person.favourite_colour)
                    if bra:
                        new_bra.colour[3] = bra.colour[3]   # preserve alpha

                if bra:
                    outfit.remove_clothing(bra)
                outfit.add_upper(new_bra)
                return True
            return False

        def __init__(self, person):
            if person and isinstance(person, Person):
                self.person = person
            else:
                if self.default_person is None:
                    self.default_person = create_random_person(name ="Ema", last_name = "Hesire", age = 23, body_type = "thin_body", tits = "B")
                    self.default_person.opinions.clear() # reset opinions so every item has an equal chance
                    self.default_person.sexy_opinions.clear()

                self.person = self.default_person

            skirts_score = self.person.get_opinion_score("skirts")
            pants_score = self.person.get_opinion_score("pants")
            dress_score = self.person.get_opinion_score("dresses")

            # person hates all main clothing items, make her like skirts.
            if skirts_score + pants_score + dress_score == -6:
                self.person.opinions["skirts"] = [1, True]

        def build_outfit(self, outfit_type, points, min_points = 0):
            if (outfit_type == "over"):
                return self.build_overwear(points, min_points)
            if (outfit_type == "under"):
                return self.build_underwear(points, min_points)

            underwear = self.build_underwear(points, min_points)
            overwear = self.build_overwear(points, min_points)

            outfit = Wardrobe.build_assembled_outfit(underwear, overwear)
            if outfit.is_legal_in_public:
                return outfit

            if outfit.vagina_visible:   # make sure vagina is covered so it's a legal outfit
                self.set_sexier_panties(self.person, outfit)

            if outfit.is_legal_in_public:
                return outfit

            if outfit.tits_visible:     # make sure tits are covered so it's a legal outfit
                self.set_sexier_bra(self.person, outfit, allow_remove_bra = False)

            return outfit # should be legal now

        def get_hate_list(self):
            return [x for x in self.preferences.keys() + self.color_prefs.keys() if self.person.get_opinion_score(x) == -2]

        def get_love_list(self):
            return [x for x in self.preferences.keys() + self.color_prefs.keys() if self.person.get_opinion_score(x) == 2]

        def get_color_hate_list(self):
            return [x for x in self.color_prefs.keys() if self.person.get_opinion_score(x) == -2]

        def approves_outfit_color(self, outfit):
            for clothing in outfit.feet + outfit.lower_body + outfit.upper_body:
                opinion_color = self.get_color_opinion(clothing.colour)
                if opinion_color in self.get_color_hate_list():
                    return False
            return True

        def build_overwear(self, points = 0, min_points = 0):
            def make_upper_item_transparent(item, points, colour):
                colour[3] = .85 + (renpy.random.randint(0, 10) / 100.0)
                if item.layer == 3 and item.slut_value > 0 and points > 6 and item in real_shirt_list + real_dress_list:
                    colour[3] = .75 + (renpy.random.randint(0, 15) / 100.0)
                return item.get_copy(), colour

            def make_lower_item_transparent(item, points, colour):
                colour[3] = .85 + (renpy.random.randint(0, 10) / 100.0)
                if item.layer == 3 and item.slut_value > 0 and points > 6 and item in skirts_list + [suitpants, leggings, booty_shorts]:
                    colour[3] = .75 + (renpy.random.randint(0, 15) / 100.0)
                return item.get_copy(), colour

            outfit = Outfit("Overwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme(self.person)

            # decide if person will wear overwear
            if not (points >= 10 and self.person.get_opinion_score("not wearing anything") > 0 and renpy.random.randint(0, 4 - self.person.get_opinion_score("not wearing anything")) == 0):
                upper_item_list = real_dress_list + real_shirt_list

                # find upper body item
                item = self.get_item_from_list(self.person, "upper_body", self.build_filter_list(upper_item_list, points, min_points), points, ["not wearing anything"])
                if item:
                    outfit.add_upper(*make_upper_item_transparent(item, points, self.get_item_color(item, color_upper, self.get_color_hate_list())))

                # we added a overlay item, so find a real upper item this time
                if item and item.layer == 4 and not item.has_extension:
                    item = self.get_item_from_list(self.person, "upper_body", self.build_filter_list(upper_item_list, points, min_points, layers = [3]), points, ["not wearing anything"])
                    if item:
                        outfit.add_upper(*make_upper_item_transparent(item, points, self.get_item_color(item, color_lower, self.get_color_hate_list())))

                # find lowerbody item
                if item is None or (not item.has_extension or item.has_extension.layer == 2):
                    item = self.get_item_from_list(self.person, "lower_body", self.build_filter_list(real_pants_list + skirts_list, points, min_points), points, ["not wearing anything"])
                    if item:
                        outfit.add_lower(*make_lower_item_transparent(item, points, self.get_item_color(item, color_lower, self.get_color_hate_list(), 0.9)))

            # find feet item
            item = self.get_item_from_list(self.person, "feet", self.build_filter_list(shoes_list, points, 0))
            if item:
                outfit.add_feet(item, self.get_item_color(item, color_feet, self.get_color_hate_list(), 0.8))

            # random chance of adding outfit custom makeup (base on pref for make-up)
            if self.person.get_opinion_score("makeup") > -2 and renpy.random.randint(0, 4 - self.person.get_opinion_score("makeup")) == 0:
                # add makeup to outfit (overrides makeup in base_outfit)
                add_make_up_to_outfit(self.person, outfit)

            self.add_accessory_from_list(outfit, self.build_filter_list(earings_only_list, points, min_points, self.person.base_outfit.accessories), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(rings_list, points, min_points, self.person.base_outfit.accessories), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(bracelet_list, points, min_points, self.person.base_outfit.accessories), 3, color_upper)
            self.add_accessory_from_list(outfit, self.build_filter_list(neckwear_without_collars, points, min_points, self.person.base_outfit.accessories), 3, color_upper)

            outfit.update_name()
            return outfit

        def build_underwear(self, points = 0, min_points = 0):
            def make_upper_item_transparent(item, points, colour):
                colour[3] = .90 + (renpy.random.randint(0, 5) / 100.0)
                if points >= 8 and item.slut_value > 0 and item in [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear] + real_bra_list:
                    colour[3] = .7 + (renpy.random.randint(0, 20) / 100.0)
                return item.get_copy(), colour

            def make_lower_item_transparent(item, points, colour):
                colour[3] = .90 + (renpy.random.randint(0, 5) / 100.0)
                if points >= 8 and item.slut_value > 0 and item in panties_list:
                    colour[3] = .7 + (renpy.random.randint(0, 20) / 100.0)
                return item.get_copy(), colour

            outfit = Outfit("Underwear")

            color_upper, color_lower, color_feet = self.get_main_color_scheme(self.person, match_percent = 80) # underwear mismatch is less likely

            # decide if person will wear underwear
            if self.person.get_opinion_score("not wearing underwear") <= -2 \
                or not (points > 6 and renpy.random.randint(0, 3 - self.person.get_opinion_score("not wearing underwear")) == 0):

                # find upper body item
                item = self.get_item_from_list(self.person, "upper_body", self.build_filter_list(real_bra_list + [lingerie_one_piece, lacy_one_piece_underwear, bodysuit_underwear, leotard], points, min_points), points, ["showing her tits", "not wearing underwear"])
                if item:
                    outfit.add_upper(*make_upper_item_transparent(item, points, color_upper))

                # random chance of adding sexy underwear part (heart pasties / cincher)
                if points >= 7 and renpy.random.randint(0, 3 - self.person.get_opinion_score("lingerie")) == 0:
                    outfit.add_upper(*make_upper_item_transparent(renpy.random.choice([cincher, heart_pasties]), points, color_upper))

                # find lower body item
                if not item or not item.has_extension:
                    if item and item.proper_name in self.matching_underwear:
                        item = self.get_item_from_list(self.person, "lower_body", self.build_filter_list(self.matching_underwear[item.proper_name], points, min_points), points, ["showing her ass", "not wearing underwear"])
                    else:
                        item = self.get_item_from_list(self.person, "lower_body", self.build_filter_list(panties_list, points, min_points), points, ["showing her ass", "not wearing underwear"])
                    if item:
                        outfit.add_lower(*make_lower_item_transparent(item, points, color_lower if item in [cincher, heart_pasties] else color_upper))
            else:
                # random chance of adding sexy underwear part (heart pasties / cincher)
                if points >= 7 and renpy.random.randint(0, 3 - self.person.get_opinion_score("lingerie")) == 0:
                    outfit.add_upper(*make_upper_item_transparent(renpy.random.choice([cincher, heart_pasties]), points, color_upper))

            # random socks (with high points we definitely wear socks)
            if min_points > 2 or points >= 8 or renpy.random.randint(0, 1) == 0:
                if points >= 5:
                    item = self.get_item_from_list(self.person, "feet", self.build_filter_list([x for x in socks_list if x not in [short_socks, medium_socks]], points, min_points))
                else:
                    item = self.get_item_from_list(self.person, "feet", self.build_filter_list(socks_list, points, min_points))
                if item:
                    outfit.add_feet(item.get_copy(), color_feet)

            # random shoes (with high points we definitely wear shoes)
            if min_points > 2 or points >= 8 or renpy.random.randint(0, 1) == 0:
                item = self.get_item_from_list(self.person, "feet", self.build_filter_list(shoes_list, points, 0))
                if item:
                    outfit.add_feet(item, self.get_item_color(item, color_feet, self.get_color_hate_list(), 0.8))

            # random chance of adding outfit custom makeup (base on pref for make-up)
            if self.person.get_opinion_score("makeup") > -2 and renpy.random.randint(0, 4 - self.person.get_opinion_score("makeup")) == 0:
                # add makeup to outfit (overrides makeup in base_outfit)
                add_make_up_to_outfit(self.person, outfit)

            self.add_accessory_from_list(outfit, self.build_filter_list(rings_list, points, min_points, self.person.base_outfit.accessories), 3, color_lower)
            self.add_accessory_from_list(outfit, self.build_filter_list(bracelet_list, points, min_points, self.person.base_outfit.accessories), 3, color_upper)
            self.add_accessory_from_list(outfit, self.build_filter_list(neckwear_without_collars, points, min_points, self.person.base_outfit.accessories), 3, color_upper)

            outfit.update_name()
            return outfit

        def personalize_outfit(self, outfit, opinion_color = None, coloured_underwear = False, main_colour = None, swap_bottoms = False, allow_skimpy = True):
            def preserve_colour_alpha(new_colour, old_colour):
                alpha_blended = new_colour[:]
                alpha_blended[3] = old_colour[3]
                return alpha_blended

            outfit.remove_all_collars()
            outfit.remove_all_cum()

            underwear_colour = None

            #First, get a theme color
            if opinion_color is None:
                if main_colour:
                    opinion_color = self.get_color_opinion(main_colour)
                elif renpy.random.randint(0,100) < 50:  #50% chance we go straight to a favorite color.
                    main_colour = self.get_color(self.person)
                    opinion_color = self.get_color_opinion(main_colour)
                else:
                    opinion_color = self.person.favourite_colour

            color_list = [self.color_prefs[opinion_color][x][:] for x in self.color_prefs[opinion_color]]
            if main_colour is None:
                main_colour = renpy.random.choice(color_list)

            color_hate_list = self.get_color_hate_list()

            if coloured_underwear:
                if renpy.random.randint(0,100) < 70: #70% chance to use similar color as outfit theme
                    underwear_colour = renpy.random.choice(color_list)
                else:
                    color_list = []
                    underwear_colour = self.get_color(self.person, main_colour)

            if swap_bottoms:
                (outfit, swapped) = self.apply_bottom_preference(self.person, outfit)

            if allow_skimpy:
                self.set_sexier_panties(self.person, outfit, underwear_colour)
                self.set_sexier_bra(self.person, outfit, underwear_colour)

            #Next, determine what kind of outfit this is.
            if outfit.has_dress: #If it is a dress, let the dress be the focal point of the outfit.
                # renpy.say ("", "Suitable dress set")
                for item in outfit.upper_body:
                    if item in real_bra_list and coloured_underwear:
                        item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                    elif item in real_dress_list:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                        if item in real_bra_list:
                            underwear_colour = item.colour  #If we neutralized the bra, makes sure we save the colour the give matching panties
                for item in outfit.lower_body:
                    if item in panties_list and (coloured_underwear or underwear_colour):
                        item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                    elif item in real_dress_list:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = preserve_colour_alpha(main_colour, item.colour_pattern)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)


            elif outfit.has_pants: #This outfit has lower body pants covering.
                # renpy.say ("", "Suitable pants set")
                #Fist determine if we want to switch to a skirt. #TODO figure out how to do this
                #Next, figure out what kind of top we have. Regular, bra, or topless.
                if outfit.tits_visible:   #Tits are on display, but she may have a top still. Colour her top (if there) and pants
                    for item in outfit.upper_body:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            item.colour = preserve_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item, color_hate_list)

                elif not outfit.bra_covered: #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize pants
                    for item in outfit.upper_body:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            neutralize_item_colour(item, color_hate_list)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                else: #Assume a decent top is being worn. Top is the focal point of the outfit
                    for item in outfit.upper_body:
                        if item in real_bra_list and coloured_underwear:
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in shirts_list:
                            item.colour = preserve_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                            if item in real_bra_list:
                                underwear_colour = item.colour
                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in real_pants_list:
                            neutralize_item_colour(item, color_hate_list)
                        else:
                            neutralize_item_colour(item, color_hate_list)

                for item in outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)

            elif outfit.has_skirt: #This outfit has a skirt.
                # renpy.say ("", "Suitable skirt set")
                #Similar logic to pants. First determine if we should switch to pants
                #Next, determine what kind of top is being worn.
                if outfit.tits_visible:   #Tits are on display, but she may have a top still. Colour her top (if there) and skirt
                    for item in outfit.upper_body:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            item.colour = preserve_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                elif not outfit.bra_covered: #Bra is on display, use that for our colour theme. Bra is focal point of outfit, so neutralize skirt
                    for item in outfit.upper_body:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            neutralize_item_colour(item, color_hate_list)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                else:   #She's wearing a full outfit. Probably top is focal point, but there is a CHANCE that she may decide to make the skirt the outfit focal point.
                    skirt_focus = renpy.random.randint(0,100) < 30  #30% chance for skirt focus
                    for item in outfit.upper_body:
                        if item in real_bra_list and coloured_underwear:
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in shirts_list and not skirt_focus:
                            item.colour = preserve_colour_alpha(main_colour, item.colour)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                            if item in real_bra_list:
                                underwear_colour = item.colour
                            elif item.pattern: #Item has pattern that we can use to colorize
                                item.colour_pattern = main_colour

                    for item in outfit.lower_body:
                        if item in panties_list and (coloured_underwear or underwear_colour):
                            item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                        elif item in skirts_list:
                            if skirt_focus:
                                item.colour = preserve_colour_alpha(main_colour, item.colour)
                            else:
                                neutralize_item_colour(item, color_hate_list)
                        else:
                            neutralize_item_colour(item, color_hate_list)
                for item in outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)

            #Next type of outfite: housewear. Girl comfy clothes general in game are some top with just panties or no panties. EG mom's apron, pajamas, etc.
            #With this outfit, tits will be covered. Make top the focal point.
            elif outfit.has_shirt:
                # renpy.say ("", "Suitable comfy set")
                for item in outfit.upper_body:
                    if item in real_bra_list and coloured_underwear:
                        item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                    elif item in shirts_list:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                        if item in real_bra_list:
                            underwear_colour = item.colour

                for item in outfit.lower_body:
                    if item in panties_list and (coloured_underwear or underwear_colour):
                        item.colour = preserve_colour_alpha(underwear_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.feet:
                    if item.proper_name == "Sneakers":
                        neutralize_item_colour(item)
                        item.colour_pattern = main_colour
                    elif renpy.random.randint(0,100) < 30 and item in shoes_list: #Nomrally we neutralize feet, but have a chance at having a matching set of shooes
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)

            #This outfit does not have lower or upper body covering. Could be just underwear or lingerie.
            #First, check and see if this is just an underwear set. In that case, colour all underwear as main color.
            #To differentiate between underwear and lingerie, check and see if it is classic underwear set via layers.
            #If bottom layer only, check sluttiness rating and access and for pantyhose vs socks and determine if we treat as just underwear or as lingerie
            elif outfit.is_suitable_underwear_set and not (outfit.has_hose and outfit.underwear_slut_score > 15):
                #Make underwear main color, neutralize everything else.
                # renpy.say ("", "Suitable underwear set")
                for item in outfit.upper_body:
                    if item in real_bra_list:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)

                for item in outfit.lower_body:
                    if item in panties_list:
                        item.colour = preserve_colour_alpha(main_colour,item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.feet:
                    neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)
            else: #This is for exciting, lingerie style outfits. Lingerie is generally completely color matching, maybe with only one or two neutral pieces.
                # renpy.say ("", "Suitable lingerie set")
                for item in outfit.upper_body:
                    item.colour = preserve_colour_alpha(main_colour, item.colour)
                for item in outfit.lower_body:
                    item.colour = preserve_colour_alpha(main_colour, item.colour)
                for item in outfit.feet:
                    if item in socks_list and renpy.random.randint(0,100) < 70:
                        item.colour = preserve_colour_alpha(main_colour, item.colour)
                    else:
                        neutralize_item_colour(item, color_hate_list)
                for item in outfit.accessories:
                    neutralize_item_colour(item, color_hate_list)
            return outfit
