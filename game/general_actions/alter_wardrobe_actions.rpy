# Alter wardrobe functions original by Kaden

init 4 python:
    def modify_wardrobe_requirement(person):
        if person.obedience < 130:
            return "Requires: 130 Obedience"
        if person.effective_sluttiness() < 30 and person.love < 30:
            return "Requires: 30 Sluttiness or 30 Love"
        return True

    modify_wardrobe_action = ActionMod("Modify entire wardrobe", requirement = modify_wardrobe_requirement, effect = "modify_wardrobe_label",
        menu_tooltip = "Ask girl to change her wardrobe.", priority = -5, category = "Wardrobe", initialization = init_action_mod_disabled)

    def build_specific_action_list_alter_outfit_extended(org_func):
        def build_specific_action_list_wrapper(person, keep_talking = True):
            # run original function
            result = org_func(person, keep_talking)
            # run extension code (append new action to base game menu)
            found = next((x for x in action_mod_list if x.effect == "modify_wardrobe_label"), None)
            if isinstance(found, ActionMod) and found.enabled:   # use enabled from action mod settings
                # use not stored action to append to action menu
                result.append([modify_wardrobe_action, person])
            return result

        return build_specific_action_list_wrapper

    # wrap up the build_specific_action_list function
    if "build_specific_action_list" in dir():
        build_specific_action_list = build_specific_action_list_alter_outfit_extended(build_specific_action_list)

    def bra_removal(person): # replace extensions with something
        alterations = 0
        for outfit in [x for x in person.wardrobe.outfit_sets + person.wardrobe.underwear_sets if x.wearing_bra]:
            old_bra = outfit.get_bra()
            new_panties = None
            if old_bra.has_extension and person.get_opinion_score("not wearing underwear") < 0:
                new_panties = cute_panties.get_copy()
                new_panties.colour = old_bra.colour
            outfit.remove_clothing(old_bra)
            if new_panties:
                outfit.add_lower(new_panties)
            alterations += 1
        return alterations

    def panty_removal(person):
        alterations = 0
        for outfit in [x for x in person.wardrobe.underwear_sets + person.wardrobe.outfit_sets if x.wearing_panties]:
            old_panties = outfit.get_panties()
            if old_panties.is_extension:
                new_bra = None
                if person.get_opinion_score("not wearing underwear") < 0:
                    new_bra = bralette.get_copy()
                    new_bra.colour = old_panties.colour
                if outfit.get_bra():
                    outfit.remove_clothing(outfit.get_bra())
                    alterations += 1
                if new_bra:
                    outfit.add_upper(new_bra)
                    new_bra = None

            outfit.remove_clothing(old_panties)
            alterations += 1

        return alterations

    def lingerie_removal(person):
        alterations = 0
        for outfit in [x for x in person.wardrobe.underwear_sets + person.wardrobe.outfit_sets if x.wearing_bra]:
            old_bra = outfit.get_bra()
            if old_bra.has_extension:
                if old_bra in [lacy_one_piece_underwear]:
                    new_bra = lace_bra.get_copy()
                    new_panties = lace_panties.get_copy()
                elif old_bra in [bodysuit_underwear]:
                    new_bra = kitty_babydoll.get_copy()
                    new_panties = kitty_panties.get_copy()
                elif old_bra in [lingerie_one_piece]:
                    new_bra = teddy.get_copy()
                    new_panties = tiny_g_string.get_copy()
                else:
                    new_bra = strappy_bra.get_copy()
                    new_panties = strappy_panties.get_copy()

                outfit.remove_clothing(old_bra)

                if new_bra:
                    new_bra.colour = old_bra.colour
                    outfit.add_upper(new_bra)
                if new_panties:
                    new_panties.colour = old_bra.colour
                    outfit.add_lower(new_panties)
                outfit.update_name()
                alterations += 1
        return alterations

    def no_pants(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_lower_ordered() if x in pants_list]:
                if clothing.slut_value <= 0:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = long_skirt.get_copy()
                    else:
                        new_clothing = pencil_skirt.get_copy()
                elif clothing.slut_value <= 1:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = skirt.get_copy()
                    else:
                        new_clothing = lace_skirt.get_copy()
                elif clothing.slut_value <= 4:
                    new_clothing = belted_skirt.get_copy()
                elif clothing.slut_value <= 6:
                    new_clothing = mini_skirt.get_copy()
                elif clothing.slut_value <= 8:
                    new_clothing = micro_skirt.get_copy()

                outfit.remove_clothing(clothing)
                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.add_lower(new_clothing)
                    outfit.update_name()

                alterations += 1
        return alterations

    def no_dresses(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_upper_ordered() if x in real_dress_list]:
                if clothing.slut_value == 0:
                    if renpy.random.randint(0,1) == 1:
                        new_top = camisole.get_copy()
                    elif renpy.random.randint(0,1) == 1:
                        new_top = tshirt.get_copy()
                    else:
                        new_top = sweater.get_copy()
                    if renpy.random.randint(0,1) == 1:
                        new_bottom = long_skirt.get_copy()
                    else:
                        new_bottom = pencil_skirt.get_copy()
                elif clothing.slut_value <= 2:
                    if renpy.random.randint(0,1) == 1:
                        new_top = lace_sweater.get_copy()
                    elif renpy.random.randint(0,1) == 1:
                        new_top = business_vest.get_copy()
                    else:
                        new_top = frilly_longsleeve_shirt.get_copy()
                    if renpy.random.randint(0,1) == 1:
                        new_bottom = skirt.get_copy()
                    else:
                        new_bottom = lace_skirt.get_copy()
                elif clothing.slut_value <= 4:
                    new_top = lace_crop_top.get_copy()
                    new_bottom = belted_skirt.get_copy()
                elif clothing.slut_value <= 5:
                    if renpy.random.randint(0,1) == 1:
                        new_top = tanktop.get_copy()
                    else:
                        new_top = tube_top.get_copy()
                    new_bottom = mini_skirt.get_copy()
                elif clothing.slut_value <= 6:
                    new_top = belted_top.get_copy()
                    new_bottom = micro_skirt.get_copy()
                else:
                    new_bottom = None
                    new_top = None

                outfit.remove_clothing(clothing)
                if new_top:
                    new_top.colour = clothing.colour
                    outfit.add_upper(new_top)
                if new_bottom:
                    new_bottom.colour = clothing.colour
                    outfit.add_lower(new_bottom)
                outfit.update_name()
                alterations += 1
        return alterations

    def shorter_pants(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_lower_ordered() if x in pants_list]:
                if clothing.slut_value <= 0:
                    new_clothing = capris.get_copy()
                elif clothing.slut_value <= 1 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    new_clothing = leggings.get_copy()
                elif clothing.slut_value <= 3 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    new_clothing = jean_hotpants.get_copy()
                elif clothing.slut_value <= 4 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    new_clothing = booty_shorts.get_copy()
                elif clothing.slut_value <= 6 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    new_clothing = daisy_dukes.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_lower(new_clothing)
                    outfit.update_name()
                    alterations += 1
        return alterations

    def shorter_skirts(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_lower_ordered() if x in skirts_list]:
                if clothing.slut_value <= 0 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = skirt.get_copy()
                    else:
                        new_clothing = lace_skirt.get_copy()
                elif clothing.slut_value <= 1 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    new_clothing = belted_skirt.get_copy()
                elif clothing.slut_value <= 3 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    new_clothing = mini_skirt.get_copy()
                elif clothing.slut_value <= 5 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    new_clothing = micro_skirt.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_lower(new_clothing)
                    outfit.update_name()
                    alterations += 1
        return alterations

    def smaller_dresses(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_upper_ordered() if x in real_dress_list]:
                if clothing.slut_value <= 0 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = evening_dress.get_copy()
                    else:
                        new_clothing = frilly_dress.get_copy()
                elif clothing.slut_value <= 2 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    new_clothing = thin_dress.get_copy()
                elif clothing.slut_value <= 4 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    new_clothing = virgin_killer.get_copy()
                elif clothing.slut_value <= 5 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = nightgown_dress.get_copy()
                    else:
                        new_clothing = two_part_dress.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    if clothing == pinafore:    # when pinafore also remove shirt
                        top = next((x for x in outfit.get_upper_ordered() if x.layer == 2), None)
                        if top:
                            outfit.remove_clothing(top)
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_upper(new_clothing)
                    outfit.update_name()
                    alterations += 1
        return alterations

    def smaller_shirts(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_upper_ordered() if x in real_shirt_list and x.layer == 2]:
                if clothing.slut_value <= 0:
                    new_clothing = wrapped_blouse.get_copy()
                if clothing.slut_value <= 0 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = camisole.get_copy()
                    elif renpy.random.randint(0,1) == 1:
                        new_clothing = tshirt.get_copy()
                    else:
                        new_clothing = sweater.get_copy()
                elif clothing.slut_value <= 1 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = lace_sweater.get_copy()
                    elif renpy.random.randint(0,1) == 1:
                        new_clothing = business_vest.get_copy()
                    else:
                        new_clothing = frilly_longsleeve_shirt.get_copy()
                elif clothing.slut_value <= 2 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    new_clothing = lace_crop_top.get_copy()
                elif clothing.slut_value <= 3 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = tanktop.get_copy()
                    else:
                        new_clothing = tube_top.get_copy()
                elif clothing.slut_value <= 4 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    new_clothing = belted_top.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_upper(new_clothing)
                    outfit.update_name()
                    alterations += 1
        return alterations

    def sexier_panties(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.underwear_sets:
            for clothing in [x for x in outfit.get_lower_ordered() if x in panties_list]:
                if clothing.slut_value <= 0:
                    new_clothing = panties.get_copy()
                if clothing.slut_value <= 0 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = thin_panties.get_copy()
                    elif renpy.random.randint(0,1) == 1:
                        new_clothing = kitty_panties.get_copy()
                    else:
                        new_clothing = cute_panties.get_copy()
                elif clothing.slut_value <= 1 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = cute_lace_panties.get_copy()
                    else:
                        new_clothing = lace_panties.get_copy()
                elif clothing.slut_value <= 2 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = thong.get_copy()
                    else:
                        new_clothing = tiny_lace_panties.get_copy()
                elif clothing.slut_value <= 3 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = string_panties.get_copy()
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = tiny_g_string.get_copy()
                    else:
                        new_clothing = strappy_panties.get_copy()
                elif clothing.slut_value <= 4 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    new_clothing = crotchless_panties.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_lower(new_clothing)
                    if outfit in person.wardrobe.underwear_sets:
                        outfit.update_name()
                    alterations += 1
        return alterations

    def sexier_bras(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.underwear_sets:
            for clothing in [x for x in outfit.get_upper_ordered() if x in real_bra_list]:
                if clothing.slut_value <= 0:
                    new_clothing = bralette.get_copy()
                if clothing.slut_value <= 0 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 20:
                    new_clothing = strapless_bra.get_copy()
                elif clothing.slut_value <= 1 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 40:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = lace_bra.get_copy()
                    else:
                        new_clothing = thin_bra.get_copy()
                elif clothing.slut_value <= 2 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 60:
                    new_clothing = strappy_bra.get_copy()
                elif clothing.slut_value <= 7 and (person.get_opinion_score("skimpy outfits")*5 + person.sluttiness) > 80:
                    if renpy.random.randint(0,1) == 1:
                        new_clothing = heart_pasties.get_copy()
                    else:
                        new_clothing = quarter_cup_bustier.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_upper(new_clothing)
                    if outfit in person.wardrobe.underwear_sets:
                        outfit.update_name()
                    alterations += 1
        return alterations

    def sexier_socks(person):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.underwear_sets:
            for clothing in [x for x in outfit.get_feet_ordered() if x in socks_list]:
                if clothing.slut_value <= 0 and (person.get_opinion_score("lingerie")*5 + person.sluttiness) > 20:
                    new_clothing = high_socks.get_copy()
                elif clothing.slut_value <= 2 and (person.get_opinion_score("lingerie")*5 + person.sluttiness) > 40:
                    new_clothing = thigh_highs.get_copy()
                elif clothing.slut_value <= 5 and (person.get_opinion_score("lingerie")*5 + person.sluttiness) > 60:
                    new_clothing = fishnets.get_copy()
                elif clothing.slut_value <= 10 and (person.get_opinion_score("lingerie")*5 + person.sluttiness) > 100:
                    new_clothing = garter_with_fishnets.get_copy()
                else:
                    new_clothing = None

                if new_clothing:
                    new_clothing.colour = clothing.colour
                    outfit.remove_clothing(clothing)
                    outfit.add_feet(new_clothing)
                    alterations += 1
        return alterations

    def translucent(person, fade_number = .98, fade_over = False, fade_under = False):
        alterations = 0
        for outfit in person.wardrobe.outfit_sets + person.wardrobe.overwear_sets:
            for clothing in [x for x in outfit.get_upper_ordered() + outfit.get_lower_ordered()]:
                if not clothing.colour[3] == fade_number \
                    and ((fade_over and not clothing in real_bra_list + panties_list) \
                        or (fade_under and clothing in real_bra_list + panties_list)):

                    clothing.colour[3] = fade_number
                    alterations += 1
        return alterations

    def build_modify_wardrobe_menu():
        modify_outfit = ["Outfit", ["Change Base Outfit", "base"], ["More Translucency", "translucent"],
            ["Sexier Clothes (all options)", "sexier_clothes"], ["Back", "back"]
        ]
        modify_overwear = ["Overwear", ["Stop wearing pants", "no_pants"], ["Stop wearing dresses", "no_dresses"],
            ["Shorter Skirts", "shorter_skirts"], ["Shorter Pants", "shorter_pants"],
            ["Sexier Shirts", "sexier_shirts"], ["Sexier Dresses", "sexier_dresses"],
            ["Sexier Socks", "sexier_socks"]
        ]
        modify_underwear = ["Underwear", ["Stop wearing lingerie", "lingerie_removal"],
            ["Stop wearing bras", "no_bras"], ["Stop wearing panties", "no_panties"],
            ["Sexier Bras", "sexier_bras"], ["Sexier Panties", "sexier_panties"]
        ]

        return [modify_outfit, modify_overwear, modify_underwear]


label modify_wardrobe_label(the_person):
    call screen main_choice_display(build_menu_items(build_modify_wardrobe_menu()))
    $ strip_choice = _return
    $ alterations = 0
    if strip_choice == 'base':
        mc.name "Let's take a look at the accessories you are always wearing."
        the_person "Alright, it shouldn't be too hard to update my jewelry collection."
        call screen outfit_creator(the_person.base_outfit, outfit_type = "full", slut_limit = None)
        if _return != "Not_New" and isinstance(_return, Outfit):
            $ the_person.change_obedience(1)
            $ the_person.base_outfit = _return
        $ clear_scene()
    elif strip_choice == "no_pants":
        mc.name "I want you to stop wearing pants."
        if the_person.get_opinion_score("skirts") < the_person.get_opinion_score("pants"):
            the_person "I'm not really a fan of skirts."
            if the_person.sluttiness > 40 or the_person.obedience > 140 or the_person.love > 40:
                mc.name "Don't worry [the_person.title] I am, and isn't that what really matters?"
                the_person "I guess you're right. I'll make the switch as soon as I can."
                $ alterations += no_pants(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.get_opinion_score("skirts") > the_person.get_opinion_score("pants"):
            the_person "Ok."
            $ alterations += no_pants(the_person)
        else:
            the_person "Oh, that sounds exciting. Free and open access for people like you to take advantage of me."
            $ alterations += no_pants(the_person)
        $ the_person.discover_opinion("pants")
        $ the_person.discover_opinion("skirts")
    elif strip_choice == "no_dresses":
        mc.name "I want you to stop wearing dresses."
        if the_person.get_opinion_score("skirts") < the_person.get_opinion_score("dresses"):
            the_person "I really prefer them to skirts."
            if the_person.sluttiness > 40 or the_person.obedience > 140 or the_person.love > 40:
                mc.name "Don't worry [the_person.title] I prefer skirts, and isn't that what really matters?"
                the_person "I guess you're right. I'll make the switch as soon as I can."
                $ alterations += no_dresses(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.get_opinion_score("skirts") > the_person.get_opinion_score("dresses"):
            the_person "Ok."
            $ alterations += no_dresses(the_person)
        else:
            the_person "Oh, that sounds exciting. It will give me a chance to show off more of my body from time to time."
            $ alterations += no_dresses(the_person)
        $ the_person.discover_opinion("dresses")
        $ the_person.discover_opinion("skirts")
    elif strip_choice == "lingerie_removal":
        mc.name "I want you to stop wearing lingerie."
        if the_person.get_opinion_score("not wearing underwear") < 0:
            the_person "I'm not sure I'm comfortable with not wearing underwear."
            mc.name "Sorry, that isn't what I meant, just don't wear the full body lingerie. You can still wear bras and panties."
            the_person "Ok, I'll see if there is anything I need to change."
        elif the_person.get_opinion_score("not wearing underwear") >= 1:
            the_person "Oh, that sounds exciting. I'll stop wearing underwear altogether."
            mc.name "Oh, actually..."
            menu:
                "Just no full body lingerie":
                    mc.name "Sorry, that isn't what I meant, just don't wear the full body lingerie. You can still wear bras and panties."
                "No bras":
                    mc.name "Actually, just get rid of bras, you can keep wearing panties."
                    $ alterations += bra_removal(the_person)
                "No panties":
                    mc.name "Actually, just get rid of panties, you can keep wearing bras."
                    $ alterations += panty_removal(the_person)
                "No underwear":
                    mc.name "That sounds even better, thanks, [the_person.title]."
                    $ alterations += bra_removal(the_person)
                    $ alterations += panty_removal(the_person)
        else:
            the_person "Ok."
        $ alterations += lingerie_removal(the_person)
        $ the_person.discover_opinion("lingerie")
    elif strip_choice == "no_bras":
        mc.name "I want you to stop wearing bras."
        if the_person.get_opinion_score("not wearing underwear") < 0:
            the_person "I'm not sure I'm comfortable with that."
            if the_person.sluttiness > 50 or the_person.obedience > 150 or the_person.love > 50:
                mc.name "Don't worry [the_person.title] I'm comfortable with it, and isn't that what really matters?"
                the_person "I guess you're right. I'll remove them from my wardrobe as soon as I can."
                $ alterations += bra_removal(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.get_opinion_score("not wearing underwear") == 0:
            the_person "Ok."
            $ alterations += bra_removal(the_person)
        else:
            if the_person.has_large_tits:
                the_person "Oh, that sounds exciting, but my tits are so big."
                mc.name "That's exactly why you should do it. Just imagine them swinging around all day for everyone to see."
                the_person "That does sound pretty hot. I'll do it as soon as I can."
            elif the_person.tits in ["A", "AA"]:
                the_person "That shouldn't be a problem. I've never had much to hold in them anyway."
                mc.name "Exactly, and this way I'll be able to grab a little handful whenever I want."
                the_person "I like the thought of that. I'll do it as soon as I can."
            else:
                the_person "Ok."
            $ alterations += bra_removal(the_person)
        $ the_person.discover_opinion("not wearing underwear")
    elif strip_choice == "no_panties":
        mc.name "I want you to stop wearing panties."
        if the_person.get_opinion_score("not wearing underwear") < 0:
            the_person "I'm not sure I'm comfortable with that."
            if the_person.sluttiness > 60 or the_person.obedience > 160 or the_person.love > 60:
                mc.name "Don't worry [the_person.title] I'm comfortable with it, and isn't that what really matters?"
                the_person "I guess you're right. I'll remove them from my wardrobe as soon as I can."
                $ alterations += panty_removal(the_person)
            else:
                mc.name "I understand, you're not really ready for that yet."
        elif the_person.get_opinion_score("not wearing underwear") == 0:
            the_person "Ok."
            $ alterations += panty_removal(the_person)
        else:
            the_person "Oh, that sounds exciting."
            $ alterations += panty_removal(the_person)
        $ the_person.discover_opinion("not wearing underwear")
    elif strip_choice == "shorter_skirts":
        mc.name "I want you to wear shorter skirts."
        if the_person.get_opinion_score("skimpy outfits") > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.get_opinion_score("skimpy outfits") == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += shorter_skirts(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "shorter_pants":
        mc.name "I want you to wear shorter pants."
        if the_person.get_opinion_score("skimpy outfits") > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.get_opinion_score("skimpy outfits") == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += shorter_pants(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_dresses":
        mc.name "I want you to wear sexier dresses."
        if the_person.get_opinion_score("skimpy outfits") > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.get_opinion_score("skimpy outfits") == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += smaller_dresses(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_shirts":
        mc.name "I want you to wear sexier shirts."
        if the_person.get_opinion_score("skimpy outfits") > 0:
            the_person "Oh, that sounds exciting. You know how much I love showing skin."
        elif the_person.get_opinion_score("skimpy outfits") == 0:
            the_person "Ok."
        else:
            the_person "I'm not sure about showing any more skin that I already do."
            mc.name "You're so beautiful, [the_person.title]. I'm sure I'm not the only one who would enjoy seeing more of you."
            the_person "I'll think about it."
        $ alterations += smaller_shirts(the_person)
        $ the_person.discover_opinion("skimpy outfits")
    elif strip_choice == "sexier_bras":
        mc.name "I want you to wear sexier bras."
        if the_person.get_opinion_score("not wearing underwear") == 2:
            the_person "That is something I could probably do, but why don't I just stop wearing them altogether?"
            $ the_person.discover_opinion("not wearing underwear")
            menu:
                "Yes":
                    mc.name "That would be even better. Go ahead and remove them from your wardrobe entirely."
                    the_person "Yes, [the_person.mc_title]."
                    $ alterations += sexier_bras(the_person)
                "No":
                    mc.name "No, I like you wearing them, I just want them to be skimpy and sexy."
                    the_person "I'll take a look and see what I can do for you."
        else:
            if the_person.get_opinion_score("lingerie") > 0:
                the_person "Well I do like having something sexy to show off when I take off my clothes."
            elif the_person.get_opinion_score("lingerie") == 0:
                the_person "Ok."
            else:
                the_person "Underwear is underwear, does it really matter what it looks like?"
                mc.name "It does for me, I love seeing your body highlighted by sexy clothes."
                the_person "Alright, I'll take a look through my wardrobe."
        $ the_person.discover_opinion("lingerie")
        $ alterations += sexier_bras(the_person)
    elif strip_choice == "sexier_panties":
        mc.name "I want you to wear sexier panties."
        if the_person.get_opinion_score("not wearing underwear") >= 2:
            the_person "That is something I could probably do, but why don't I just stop wearing them altogether?"
            $ the_person.discover_opinion("not wearing underwear")
            menu:
                "Yes":
                    mc.name "That would be even better. Go ahead and remove them from your wardrobe entirely."
                    the_person "Yes, [the_person.mc_title]."
                    $ alterations += sexier_panties(the_person)
                "No":
                    mc.name "No, I like you wearing them, I just want them to be skimpy and sexy."
                    the_person "I'll take a look and see what I can do for you."
        else:
            if the_person.get_opinion_score("lingerie") > 0:
                the_person "Well I do like having something sexy to show off when I take off my clothes."
            elif the_person.get_opinion_score("lingerie") == 0:
                the_person "Ok."
            else:
                the_person "Underwear is underwear, does it really matter what it looks like?"
                mc.name "It does for me, I love seeing your body highlighted by sexy clothes."
                the_person "Alright, I'll take a look through my wardrobe."
        $ the_person.discover_opinion("lingerie")
        $ alterations += sexier_panties(the_person)
    elif strip_choice == "sexier_socks":
        mc.name "I want you to wear sexier socks."
        if the_person.get_opinion_score("lingerie") > 0:
            the_person "Oh, that sounds fun. I'm always looking for more ways to attract attention."
            mc.name "Exactly, and if you do you'll get more attention from me."
            the_person "I'll take a look and see what I can change for you."
        elif the_person.get_opinion_score("lingerie") == 0:
            the_person "What do you mean sexier socks? How are socks sexy?"
            mc.name "You know, things like thigh highs. Socks that you wear for people to see."
            the_person "Oh, I've never really gotten the appeal, but I guess I can give it a try."
        else:
            the_person "I'm not really a fan of advertising my sexuality."
            mc.name "Don't think of it as that, it is about highlighting your best features. Don't you think you are beautiful enough to show off?"
            the_person "I suppose I can take a look at my wardrobe for you."
        $ alterations += sexier_socks(the_person)
        $ the_person.discover_opinion("lingerie")
    elif strip_choice == "translucent":
        mc.name "I like the clothes you are wearing, I just wish they didn't obstruct so much of my view of you."
        the_person "That's sweet, but it isn't like I can just make my clothes more see through for you."
        mc.name "Sure you can, I have this compound that does just that." #whole quest chain in development: chemical spill > research > work laundry policies > serum trait > home laundry tampering
        the_person "Well in that case..."
        the_person "What parts of my clothes do you want me to change?"
        $ fade_over = False
        $ fade_under = False
        $ fade_number = .98
        menu:
            "Just overwear":
                $ fade_over = True
                mc.name "I think just the top layers of your clothes. I like being able to see your underwear showing through."
                if the_person.get_opinion_score("skimpy outfits") > 0:
                    the_person "I do like showing off."
            "Just underwear" if not the_person.has_taboo("underwear_nudity"):
                $ fade_under = True
                mc.name "I think just your underwear. I really like the look of sheer lingerie once I get your clothes off."
                if the_person.get_opinion_score("showing her tits") > 0 or the_person.get_opinion_score("showing her ass") > 0:
                    the_person "Fortunately I like showing off my assets."
            "Everything" if not the_person.has_taboo("underwear_nudity"):
                $ fade_over = True
                $ fade_under = True
                mc.name "I think everything you wear should be see through."
                if the_person.get_opinion_score("showing her tits") > 0 or the_person.get_opinion_score("showing her ass") > 0:
                    the_person "I like the way you think, no wonder we get along so well."
        the_person "Now I just need to know how far I should take this."
        menu:
            "95":
                $ fade_number = 0.95
                mc.name "Let's start small."
            "90" if the_person.sluttiness > 20:
                $ fade_number = 0.90
                mc.name "Fade them a bit, but not too much."
            "80" if the_person.sluttiness > 40:
                $ fade_number = 0.80
                mc.name "I want to be able to see through them."
            "75" if the_person.sluttiness > 60:
                $ fade_number = 0.75
                mc.name "Take it down a quarter."
            "66" if the_person.sluttiness > 70:
                $ fade_number = 0.66
                mc.name "Go pretty far, I want to know what is under everything."
            "50" if the_person.sluttiness > 80:
                $ fade_number = 0.50
                mc.name "Go extreme, let me see everything under them."
            "33" if the_person.sluttiness > 90:
                $ fade_number = 0.33
                mc.name "I should barely be able to tell you are wearing anything."
        the_person "Alright, I should be able to do that."
        $ alterations += translucent(the_person, fade_number, fade_over, fade_under)
    elif strip_choice == "sexier_clothes":
        mc.name "I want you to wear sexier clothes."
        the_person "What do you mean?"
        mc.name "Show some skin, shorter skirts and pants, smaller shirts and dresses, sexier underwear. Just go crazy."
        the_person "I guess I can take a look at what I would be comfortable changing about my wardrobe."
        $ alterations += lingerie_removal(the_person)
        $ alterations += shorter_skirts(the_person)
        $ alterations += shorter_pants(the_person)
        $ alterations += smaller_shirts(the_person)
        $ alterations += smaller_dresses(the_person)
        $ alterations += sexier_panties(the_person)
        $ alterations += sexier_bras(the_person)
        $ alterations += sexier_socks(the_person)
        $ the_person.discover_opinion("skimpy outfits")
        $ the_person.discover_opinion("lingerie")

    $ test_outfit = the_person.planned_outfit
    if the_person.wardrobe.has_outfit_with_name(test_outfit.name):
        $ the_person.apply_outfit(the_person.wardrobe.get_outfit_with_name(test_outfit.name))
    $ test_outfit = None

    if alterations > 10:
        the_person "Wow, I had to make [alterations] changes to my wardrobe for you."
        mc.name "That is a lot. I really appreciate it, [the_person.title]."
        if the_person.get_opinion_score("not wearing anything") == 2:
            the_person "At this rate I'll be not wearing anything at all before too long. Won't that be exciting?"
            mc.name "You know, we could see about trying that out now if you want."
            the_person "What did you have in mind?"
            call demand_strip_label(the_person) from call_demand_strip_label_wardrobe
    elif alterations > 5:
        the_person "That wasn't too bad, I only had to make [alterations] changes to my wardrobe."
        mc.name "Thank you [the_person.title]."
    elif alterations > 1:
        the_person "That was easy, I only had to change [alterations] parts of my wardrobe."
        mc.name "Thanks."
    elif alterations == 1:
        the_person "That was easy, I only had to change [alterations] part of my wardrobe."
        mc.name "Thanks."
    else:
        the_person "I'm sorry [the_person.mc_title], I couldn't find any parts of my wardrobe I was comfortable changing."
        if the_person.sluttiness > 90:
            mc.name "I guess we have probably taken things as far as they can go."
        else:
            mc.name "I guess I have some more work to do before you're ready for this."
    return
