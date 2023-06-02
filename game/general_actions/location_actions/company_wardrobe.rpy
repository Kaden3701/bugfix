## Company Uniforms Mod by Tristimdorion
# Adds outfits based on company name to the company uniforms
init 3 python:
    company_wardrobe_loaded = False

    def company_wardrobe_requirement():
        return not company_wardrobe_loaded

    def company_wardrobe_initialization(self):
        ceo_office.add_action(self)
        return

    def build_company_wardrobe(upper_color, under_color):
        lower_color = [.15, .15, .15, .95]
        upper_color_dim = [under_color[0] *.9, under_color[1] *.9, under_color[2] * .9, .9]

        normalu = Outfit(mc.business.name + " - Normal Underwear")
        normalu.add_upper(bralette.get_copy(), under_color)
        normalu.add_lower(cute_panties.get_copy(), under_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Relaxed Underwear")
        normalu.add_upper(strapless_bra.get_copy(), under_color)
        normalu.add_lower(lace_panties.get_copy(), under_color)
        normalu.add_feet(high_socks.get_copy(), under_color)
        normalu.add_accessory(blush.get_copy(), [0.76, 0.376, 0.368, 0.8])
        normalu.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Sexy Underwear")
        normalu.add_upper(lace_bra.get_copy(), under_color)
        normalu.add_lower(lace_panties.get_copy(), under_color)
        normalu.add_feet(thigh_highs.get_copy(), under_color)
        normalu.add_accessory(blush.get_copy(), [0.76, 0.376, 0.368, 0.8])
        normalu.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Provocative Underwear")
        normalu.add_upper(thin_bra.get_copy(), under_color)
        normalu.add_lower(thong.get_copy(), under_color)
        normalu.add_feet(fishnets.get_copy(), under_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Risque Underwear")
        normalu.add_upper(corset.get_copy(), under_color)
        normalu.add_lower(tiny_g_string.get_copy(), under_color)
        normalu.add_feet(fishnets.get_copy(), under_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Slutty Underwear")
        normalu.add_lower(tiny_g_string.get_copy(), under_color)
        normalu.add_feet(garter_with_fishnets.get_copy(), under_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalu.add_accessory(light_eye_shadow.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Commando Underwear")
        normalu.add_feet(fishnets.get_copy(), under_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalu.add_accessory(light_eye_shadow.get_copy(), upper_color)
        normalu.add_accessory(lipstick.get_copy(), [0.6,0.1,0.1,0.8])
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalu = Outfit(mc.business.name + " - Kinky Underwear")
        normalu.add_upper(cincher.get_copy(), under_color)
        normalu.add_lower(crotchless_panties.get_copy(), under_color)
        normalu.add_feet(thigh_highs.get_copy(), under_color)
        normalu.add_accessory(heavy_eye_shadow.get_copy(), [0,0,0,.8])
        normalu.add_accessory(light_eye_shadow.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalu, underwear_flag = True)

        normalo = Outfit(mc.business.name + " - Normal Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(dress_shirt.get_copy(), upper_color)
        normalo.add_feet(slips.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Pants Overwear")
        normalo.add_upper(dress_shirt.get_copy(), upper_color)
        normalo.add_upper(vest.get_copy(), lower_color)
        normalo.add_lower(suitpants.get_copy(), lower_color)
        normalo.add_feet(slips.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Relaxed Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(lace_crop_top.get_copy(), upper_color)
        normalo.add_feet(sandle_heels.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Sexy Overwear")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(business_vest.get_copy(), upper_color)
        normalo.add_feet(boot_heels.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Sexy Overwear Boots")
        normalo.add_lower(pencil_skirt.get_copy(), lower_color)
        normalo.add_upper(business_vest.get_copy(), upper_color)
        normalo.add_feet(tall_boots.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Fitness Overwear")
        normalo.add_upper(sweater.get_copy(), upper_color)
        normalo.add_lower(leggings.get_copy(), lower_color)
        normalo.add_feet(sneakers.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Provocative Overwear")
        normalo.add_lower(belted_skirt.get_copy(), lower_color)
        normalo.add_upper(belted_top.get_copy(), upper_color)
        normalo.add_feet(pumps.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Hotpants Overwear")
        normalo.add_upper(tanktop.get_copy(), upper_color)
        normalo.add_lower(jean_hotpants.get_copy(), lower_color)
        normalo.add_feet(heels.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Risque Overwear")
        normalo.add_lower(mini_skirt.get_copy(), lower_color)
        normalo.add_upper(business_vest.get_copy(), upper_color)
        normalo.add_feet(high_heels.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)

        normalo = Outfit(mc.business.name + " - Easy Access Overwear")
        normalo.add_lower(micro_skirt.get_copy(), lower_color)
        normalo.add_upper(vest.get_copy(), upper_color)
        normalo.add_feet(pumps.get_copy(), upper_color)
        mc.business.add_uniform_to_company(normalo, overwear_flag = True)


        normalf = Outfit(mc.business.name + " - Normal Uniform")
        normalf.add_upper(bralette.get_copy(), under_color)
        normalf.add_upper(dress_shirt.get_copy(), upper_color)
        normalf.add_lower(cute_panties.get_copy(), under_color)
        normalf.add_lower(pencil_skirt.get_copy(), lower_color)
        normalf.add_feet(slips.get_copy(), upper_color)
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Normal Pants Uniform")
        normalf.add_upper(bralette.get_copy(), under_color)
        normalf.add_upper(dress_shirt.get_copy(), upper_color)
        normalf.add_upper(vest.get_copy(), lower_color)
        normalf.add_lower(cute_panties.get_copy(), under_color)
        normalf.add_lower(suitpants.get_copy(), lower_color)
        normalf.add_feet(slips.get_copy(), upper_color)
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Sexy Uniform")
        normalf.add_upper(business_vest.get_copy(), upper_color)
        normalf.add_lower(lace_panties.get_copy(), under_color)
        normalf.add_lower(pencil_skirt.get_copy(), lower_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_feet(boot_heels.get_copy(), upper_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Sexy Uniform Boots")
        normalf.add_upper(business_vest.get_copy(), upper_color)
        normalf.add_lower(lace_panties.get_copy(), under_color)
        normalf.add_lower(pencil_skirt.get_copy(), lower_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_feet(tall_boots.get_copy(), upper_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Fitness Uniform")
        normalf.add_upper(sweater.get_copy(), upper_color)
        normalf.add_lower(lace_panties.get_copy(), under_color)
        normalf.add_lower(leggings.get_copy(), lower_color)
        normalf.add_feet(sneakers.get_copy(), upper_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Hotpants Uniform")
        normalf.add_upper(tanktop.get_copy(), upper_color)
        normalf.add_lower(tiny_lace_panties.get_copy(), under_color)
        normalf.add_lower(jean_hotpants.get_copy(), lower_color)
        normalf.add_feet(heels.get_copy(), upper_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Risque Uniform")
        normalf.add_lower(mini_skirt.get_copy(), lower_color)
        normalf.add_upper(business_vest.get_copy(), upper_color)
        normalf.add_feet(garter_with_fishnets.get_copy(), under_color)
        normalf.add_feet(pumps.get_copy(), upper_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Slutty Uniform")
        normalf.add_upper(two_part_dress.get_copy(), lower_color)
        normalf.add_upper(vest.get_copy(), upper_color)
        normalf.add_feet(fishnets.get_copy(), under_color)
        normalf.add_feet(high_heels.get_copy(), upper_color)
        normalf.add_accessory(wide_choker.get_copy(), upper_color_dim)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(blush.get_copy(), [0.76, 0.376, 0.368, 0.8])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)

        normalf = Outfit(mc.business.name + " - Easy Access Uniform")
        normalf.add_lower(micro_skirt.get_copy(), lower_color)
        normalf.add_upper(cincher.get_copy(), upper_color)
        normalf.add_upper(vest.get_copy(), upper_color)
        normalf.add_feet(thigh_highs.get_copy(), under_color)
        normalf.add_feet(pumps.get_copy(), upper_color)
        normalf.add_accessory(heavy_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(light_eye_shadow.get_copy(), [.1, .1, .12, .9])
        normalf.add_accessory(lipstick.get_copy(), [.745, .117, .235, .9])
        mc.business.add_uniform_to_company(normalf, full_outfit_flag = True)
        return

    company_wardrobe_action = ActionMod("Add Company Wardrobe", company_wardrobe_requirement, "append_company_wardrobe", initialization = company_wardrobe_initialization,
        menu_tooltip = "Adds a collection of over- and underwear for your company to your outfit manager.", category = "Wardrobe")

label append_company_wardrobe():
    "Choose you primary business color"
    menu:
        "Primary Color Red":
            $ build_company_wardrobe([.7, .1, .2, .95], [.97, .97, 1, .95])
        "Primary Color Yellow":
            $ build_company_wardrobe([.96, .77, .19, .95], [.15, .15, .15, .95])
        "Primary Color Blue":
            $ build_company_wardrobe([.17, .32, .75, .95], [.87, .69, .17, .95])
        "Primary Color Pink":
            $ build_company_wardrobe([1, .41, .71, .95], [.15, .15, .15, .95])
        "Primary Color White":
            $ build_company_wardrobe([.97, .97, 1, .95], [.97, .97, 1, .95])

    $ company_wardrobe_loaded = True
    "Company wardrobe complete.\nCheck your employee uniforms, some items might not be enabled due to missing clothing policies (not slutty enough)."
    return
