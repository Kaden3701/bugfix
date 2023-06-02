screen serum_sell_ui():
    add science_menu_background_image

    python:
        market_reach = "{market_reach:,}".format(market_reach = __builtin__.int(mc.business.market_reach))
        funds = "${funds:,}".format(funds = __builtin__.int(mc.business.funds))
        attention_info = get_attention_string(mc.business.attention, mc.business.max_attention) + " (-" + str(mc.business.attention_bleed) + "/Day)"
        attention_tooltip_info = get_attention_number_string(mc.business.attention, mc.business.max_attention)
        mental_price = "{value:.2f}".format(value = mc.business.get_aspect_price("Mental"))
        physical_price = "{value:.2f}".format(value = mc.business.get_aspect_price("Physical"))
        sexual_price = "{value:.2f}".format(value = mc.business.get_aspect_price("Sexual"))
        medical_price = "{value:.2f}".format(value = mc.business.get_aspect_price("Medical"))
        flaw_cost = "{value:.2f}".format(value = mc.business.get_aspect_price("Flaw"))
        mental_percentage = "{value:.0f}".format(value = 200*mc.business.get_aspect_percent("Mental"))
        physical_percentage = "{value:.0f}".format(value = 200*mc.business.get_aspect_percent("Physical"))
        sexual_percentage = "{value:.0f}".format(value = 200*mc.business.get_aspect_percent("Sexual"))
        medical_percentage = "{value:.0f}".format(value = 200*mc.business.get_aspect_percent("Medical"))
        flaw_percentage = "{value:.0f}".format(value = 200*mc.business.get_aspect_percent("Flaw"))
        active_contracts = "{number}".format(number = len(mc.business.active_contracts))
        max_active_contracts = "{number}".format(number = mc.business.max_active_contracts)
        number_of_contracts = "{number}".format(number = len(mc.business.offered_contracts))

    modal True
    hbox:
        spacing 40
        xanchor 0.5
        align (0.5, 0.1)
        frame:
            background "#1a45a1aa"
            align (0.05, 0.05)
            xysize (780, 820)
            vbox:
                hbox:
                    xsize 700
                    text "Serum In Stock" style "menu_text_title_style" size 20 xalign 0.0
                    text "Sell Serum" style "menu_text_title_style" size 20 xalign 0.9 xanchor 1.0
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    vbox:
                        for serum_stock in sorted(mc.business.inventory.serums_held, key = lambda x: x[0].name):
                            hbox:
                                $ serum_dose_value = mc.business.get_serum_base_value(serum_stock[0], round_value = True)
                                use serum_design_menu_item(serum_stock[0], name_addition = ": " + str(serum_stock[1]) + " Doses, $" + str(serum_dose_value) + "/Dose")
                                textbutton "1":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, serum_stock[0])
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive serum_stock[1] >= 1
                                textbutton "10":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, serum_stock[0], serum_count = 10)
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive serum_stock[1] >= 10
                                textbutton "All":
                                    ysize 64
                                    xsize 50
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_yanchor 0.5
                                    action Function(mc.business.sell_serum, serum_stock[0], serum_count = serum_stock[1])
                                    style "textbutton_style" text_style "textbutton_text_style"
                                    sensitive serum_stock[1] > 0


            #TODO: This holds the current serem selections


        fixed:
            align (0.05, 0.05)
            xysize (780, 800)
            vbox:
                spacing 40
                frame xfill True:
                    background "#1a45a1aa"
                    ysize 230
                    #TODO: Holds current information about aspect price, attention, market reach
                    vbox:
                        hbox:
                            textbutton "Market Reach:":
                                action VrenNullAction style "textbutton_style" text_style "textbutton_text_style"
                                tooltip "How many people have heard about your business. The larger your market reach the more each serum aspect point is worth."

                            text "[market_reach] People" style "textbutton_text_style" yalign 0.5

                            null width 50

                            text "Current Funds: {color=#98fb98}[funds]{/color}" style "textbutton_text_style" yalign 0.5

                        hbox:
                            textbutton "Attention:":
                                action VrenNullAction style "textbutton_style" text_style "textbutton_text_style"
                                tooltip "How much attention your business has drawn. If this gets too high the authorities will act, outlawing a serum design, leveling a fine, or seizing your inventory.\nCurrently: {}".format(attention_tooltip_info)

                            text "[attention_info]" style "textbutton_text_style" yalign 0.5

                        null height 8

                        text "Aspect Data" style "menu_text_title_style"
                        frame:
                            background "#00000088"
                            xsize 760
                            grid 6 3:
                                xfill True
                                null

                                text "Mental" style "menu_text_style" color "#387aff"
                                text "Physical" style "menu_text_style" color "#00AA00"
                                text "Sexual" style "menu_text_style" color "#FFC0CB"
                                text "Medical" style "menu_text_style" color "#FFFFFF"
                                text "Flaws" style "menu_text_style" color "#AAAAAA"

                                text ("Values") style "menu_text_style"
                                text "$ [mental_price]" style "menu_text_style"
                                text "$ [physical_price]" style "menu_text_style"
                                text "$ [sexual_price]" style "menu_text_style"
                                text "$ [medical_price]" style "menu_text_style"
                                text "$ [flaw_cost]" style "menu_text_style"

                                text ("Desire") style "menu_text_style"
                                text "[mental_percentage]%" style "menu_text_style"
                                text "[physical_percentage]%" style "menu_text_style"
                                text "[sexual_percentage]%" style "menu_text_style"
                                text "[medical_percentage]%" style "menu_text_style"
                                text "-[flaw_percentage]%" style "menu_text_style"

                frame xfill True:
                    background "#1a45a1aa"
                    ysize 550
                    vbox:
                        ysize 400
                        text "Active Contracts ([active_contracts]/[max_active_contracts] Max)" style "menu_text_title_style"
                        viewport:
                            mousewheel True
                            scrollbars "vertical"
                            vbox:
                                spacing 20
                                xsize 800
                                for contract in mc.business.active_contracts:
                                    use contract_select_button(contract):
                                        textbutton "Add Serum":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Show("serum_trade_ui", None, mc.business.inventory, contract.inventory, name_1 = "Stockpile", name_2 = contract.name, trade_requirement = contract.check_serum, hide_instead = True, inventory_2_max = contract.amount_desired)

                                        textbutton "Abandon": #TODO: This should probably require a double click or something.
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.abandon_contract, contract)

                                        textbutton "Complete":
                                            xanchor 1.0
                                            xalign 0.90
                                            style "textbutton_style"
                                            text_style "textbutton_text_style"
                                            action Function(mc.business.complete_contract, contract)
                                            sensitive contract.can_finish_contract


                    textbutton "New Contracts: [number_of_contracts] Available":
                        style "textbutton_style"
                        text_style "textbutton_text_style"
                        yanchor 1.0
                        yalign 1.0
                        xalign 0.5
                        ysize 40
                        action Show("contract_select")


                    #TODO: Holds information about current contracts and lets you transfer serum into and out of them


    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action Return()
        textbutton "Return" align [0.5,0.5] style "return_button_style" text_style "return_button_style"
