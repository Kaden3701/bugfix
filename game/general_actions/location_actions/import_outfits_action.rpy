# Import outfits by Trollden
# Use it as you see fit

init 3 python:
    def import_wardrobe_requirement():
        return True

    def give_uniform_requirement():
        if strict_uniform_policy.is_owned:
            return True
        else:
            return "Requires: [strict_uniform_policy.name] or higher"

    def import_wardrobe_mod_initialization(self):
        bedroom.add_action(self)
        self.enabled = False
        return
    def give_wardrobe_mod_initialization(self):
        clothing_store.add_action(self)
        self.enabled = False
        return
    def give_uniform_mod_initialization(self):
        ceo_office.add_action(self)
        self.enabled = False
        return

    def check_import_xml_file(xml_filename):
        for file in renpy.list_files():
            if xml_filename in file:
                return True
        return False

    import_wardrobe_action = ActionMod("Import Wardrobe from XML", import_wardrobe_requirement, "import_wardrobe_label",
        initialization = import_wardrobe_mod_initialization, menu_tooltip = "Import wardrobe into player wardrobe from xml (Bedroom)", category = "Wardrobe")

    give_wardrobe_action = ActionMod("Add Wardrobe from XML", import_wardrobe_requirement, "give_wardrobe_label",
        initialization = give_wardrobe_mod_initialization, menu_tooltip = "Import wardrobe into person wardrobe from xml (Clothing Store)", category = "Wardrobe")

    give_uniform_action = ActionMod("Add Uniforms from XML", give_uniform_requirement, "give_uniform_label",
        initialization = give_uniform_mod_initialization, menu_tooltip = "Import wardrobe into company division wardrobe from xml (CEO Office)", category = "Wardrobe")

label import_wardrobe_label():
    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import to your wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    if check_import_xml_file(xml_filename):
        $ import_wardrobe(mc.designed_wardrobe, xml_filename)
    else:
        "Speaker" "File not found."
    return

label give_wardrobe_label():
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_in_the_game(), "Clothes for", "Back")]
        ))

    if isinstance(_return, Person):
        $ the_person = _return
        call give_wardrobe_input(the_person) from _call_give_wardrobe_input# What to do if "Back" was not the choice taken.
    return

label give_wardrobe_input(person = the_person): # when called from action default to the person
    $ the_person = person
    $ the_person.draw_person()

    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import to [the_person.name]'s wardrobe"
    $ xml_filename = str(renpy.input("Wardrobe to import:"))

    if check_import_xml_file(xml_filename):
        $ import_wardrobe(the_person.wardrobe, xml_filename)
        "Speaker" "You send a shipment of clothes to [the_person.name]."
        "Speaker" "Delivery complete."
    else:
        "Speaker" "File not found."

    $ clear_scene()
    return

label give_uniform_label():
    "Speaker" "Enter the file name e.g Lily_Wardrobe (case sensitive) then hit enter to import uniforms."

    $ xml_filename = str(renpy.input("Wardrobe to import:"))
    if check_import_xml_file(xml_filename):
        $ import_uniform(xml_filename)
        "Speaker" "Uniforms added to business."
    else:
        "Speaker" "File not found."
    return
