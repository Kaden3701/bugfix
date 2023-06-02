init -8 python:
    def get_wardrobe_file(xml_filename):
        file_name = xml_filename + ".xml"
        wardrobe_file = None

        for file in renpy.list_files():
            if file_name in file:
                wardrobe_file = renpy.file(file)
                break

        return wardrobe_file

    def get_xml_files_from_path():
        result = []
        for file in renpy.list_files():
            if file.endswith(".xml"):
                base = os.path.basename(file)
                result.append(os.path.splitext(base)[0])
        result.sort()
        return result

    def wardrobe_from_xml(xml_filename, in_import = False):
        file_name = get_wardrobe_file(xml_filename)
        if file_name is None:
            return Wardrobe("[xml_filename]") #If there is no wardrobe present we return an empty wardrobe with the name of our file.

        tree_root = ET.parse(file_name).getroot()

        wardrobe = Wardrobe(tree_root.attrib["name"])

        return parse_wardrobe_tree(wardrobe, tree_root)

    def outfit_from_xml(outfit_element):
        def proper_name_to_clothing_copy(proper_name):
            for match in panties_list + bra_list + pants_list + skirts_list + dress_list + shirts_list + socks_list + shoes_list + earings_list + bracelet_list + rings_list + neckwear_list:
                if match.proper_name == proper_name:
                    return match.get_copy()

        return_outfit = Outfit(outfit_element.attrib["name"])
        clothing_mapping = {"UpperBody":Outfit.add_upper, "LowerBody":Outfit.add_lower, "Feet":Outfit.add_feet, "Accessories":Outfit.add_accessory}

        for location in clothing_mapping:
            for item_element in outfit_element.find(location):
                clothing_copy = proper_name_to_clothing_copy(item_element.attrib["name"])
                if clothing_copy:
                    clothing_colour = [float(item_element.attrib["red"]), float(item_element.attrib["green"]), float(item_element.attrib["blue"]), float(item_element.attrib["alpha"])]
                    pattern = item_element.get("pattern",None)
                    if pattern is not None:
                        colour_pattern = [float(item_element.attrib["pred"]), float(item_element.attrib["pgreen"]), float(item_element.attrib["pblue"]), float(item_element.attrib["palpha"])]
                    else:
                        colour_pattern = None
                    clothing_mapping[location](return_outfit, clothing_copy, clothing_colour, pattern, colour_pattern)
        return return_outfit


    def import_wardrobe(wardrobe, xml_filename): # This is a rewrite of the wardrobe_from_xml function written by Vren.
        # Wardrobe should be who's / what wardrobe you want to import into. e.g for main character it is mc.designed_wardrobe
        wardrobe = wardrobe

        file_name = get_wardrobe_file(xml_filename)
        if file_name is None:
            return wardrobe # return the original wardrobe since we didn't find an xml to import into it.

        return parse_wardrobe_tree(wardrobe, ET.parse(file_name).getroot())

    def import_uniform(xml_filename):
        file_name = get_wardrobe_file(xml_filename)
        if file_name is None:
            return

        xml_root = ET.parse(file_name).getroot()
        for outfit_element in xml_root.find("FullSets"):
            mc.business.business_uniforms.append(UniformOutfit(outfit_from_xml(outfit_element)))
        for outfit_element in xml_root.find("UnderwearSets"):
            mc.business.business_uniforms.append(UniformOutfit(outfit_from_xml(outfit_element)))
        for outfit_element in xml_root.find("OverwearSets"):
            mc.business.business_uniforms.append(UniformOutfit(outfit_from_xml(outfit_element)))
        return

    def parse_wardrobe_tree(wardrobe, xml_root):
        for outfit_element in xml_root.find("FullSets"):
            wardrobe.add_outfit(outfit_from_xml(outfit_element))
        for outfit_element in xml_root.find("UnderwearSets"):
            wardrobe.add_underwear_set(outfit_from_xml(outfit_element))
        for outfit_element in xml_root.find("OverwearSets"):
            wardrobe.add_overwear_set(outfit_from_xml(outfit_element))
        return wardrobe
