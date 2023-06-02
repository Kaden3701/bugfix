init -2:
    $ serum_transfer_amount = 1 # By default transfer 1 at a time, changed by player input. Right clicking by default transfers 10 at a time

init -1 python:
    def serum_transfer_amount_func(new_amount):
        if new_amount is "":
            new_amount = 1
        elif new_amount is "0": #Figure out exactly how this works and then make it work :)
            new_amount = 1
        elif __builtin__.int(new_amount) == 0:
            new_amount = 1
        store.serum_transfer_amount = __builtin__.int(new_amount)

screen serum_trade_ui(inventory_1,inventory_2,name_1="Player",name_2="Business", trade_requirement = None, hide_instead = False, inventory_2_max = -1): #Lets you trade serums back and forth between two different inventories. Inventory 1 is assumed to be the players.
    add science_menu_background_image
    modal True

    frame:
        background "#0a142688"
        xalign 0.2
        xanchor 0.5
        yalign 0.5

        vbox:
            xsize 590
            ysize 900
            yalign 0.0
            frame:
                background "#000080"
                xsize 590
                text "Trade Serums Between Inventories" style "menu_text_title_style" xalign 0.5

            frame:
                background "#0a142688"
                xalign 0.5

                viewport:
                    scrollbars "vertical"
                    xsize 650
                    mousewheel True
                    hbox:
                        xalign 0.5
                        vbox:
                            xalign 0.5

                            for serum in sorted(set(inventory_1.get_serum_types) | set(inventory_2.get_serum_types), key = lambda x: x.name): #Gets a unique entry for each serum design that shows up in either list. Doesn't duplicate if it's in both.
                                # has a few things. 1) name of serum design. 2) count of first inventory, 3) arrows for transfering, 4) count of second inventory.
                                $ trade_sensitive = True
                                if trade_requirement:
                                    $ trade_sensitive = trade_requirement(serum)

                                $ inventory1_count = inventory_1.get_serum_count(serum)
                                $ inventory2_count = inventory_2.get_serum_count(serum)

                                $ move_all_amount = inventory1_count
                                if inventory_2_max >= 0 and move_all_amount + inventory2_count > inventory_2_max:
                                    $ move_all_amount = inventory_2_max - inventory2_count

                                vbox:
                                    textbutton "[serum.name]":
                                        style "textbutton_style"
                                        text_style "serum_text_style"
                                        xsize 560
                                        if not trade_sensitive:
                                            background "#B14365"

                                        action NullAction()
                                        hovered Show("serum_tooltip", None, serum, given_align = (0.97,0.07), given_anchor = (1.0,0.0))
                                    hbox:
                                        frame:
                                            background "#000080"
                                            xsize 170
                                            # How many serums in inventory_1 (player's)
                                            text name_1 + ": " + str(inventory1_count) style "serum_text_style"

                                        null width 10

                                        textbutton "|<":
                                            action [Function(inventory_1.change_serum,serum,inventory_2.get_serum_count(serum)),Function(inventory_2.change_serum,serum,-inventory_2.get_serum_count(serum))]
                                            sensitive (inventory2_count > 0) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (inventory_2.get_serum_count(serum) > 0) and trade_sensitive:
                                                background "#143869"
                                                hover_background "#0a142688"
                                        textbutton "<<":
                                            action [Function(inventory_1.change_serum,serum,10),Function(inventory_2.change_serum,serum,-10)]
                                            sensitive (inventory2_count > 9) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (inventory_2.get_serum_count(serum) > 9) and trade_sensitive:
                                                background "#143869"
                                                hover_background "#0a142688"
                                        textbutton "<":
                                            action [Function(inventory_1.change_serum,serum, serum_transfer_amount),Function(inventory_2.change_serum,serum, -serum_transfer_amount)]
                                            sensitive (inventory2_count > serum_transfer_amount - 1) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (inventory2_count > serum_transfer_amount - 1) and trade_sensitive:
                                                hover_background "#0a142688"
                                                background "#143869"

                                        null width 10
                                        button:
                                            id "serum_transfer_amount"
                                            style "textbutton_style"

                                            action NullAction()
                                            unhovered Function(renpy.restart_interaction) #TODO: Tweak this so it is less annoying  and fix any associated errors

                                            add Input(
                                                size =  20,
                                                color = "#dddddd",
                                                default = serum_transfer_amount,
                                                changed = serum_transfer_amount_func,
                                                length = 4,
                                                button = renpy.get_widget("serum_trade_ui", "serum_transfer_amount"),
                                                allow = "0123456789"
                                            )

                                        null width 10

                                        textbutton ">":
                                            action [Function(inventory_2.change_serum,serum, serum_transfer_amount),Function(inventory_1.change_serum,serum,-serum_transfer_amount)]
                                            sensitive (inventory1_count > serum_transfer_amount - 1) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (inventory1_count > serum_transfer_amount - 1) and trade_sensitive:
                                                background "#143869"
                                                hover_background "#0a142688"
                                        textbutton ">>":
                                            action [Function(inventory_2.change_serum,serum,10),Function(inventory_1.change_serum,serum,-10)]
                                            sensitive (inventory1_count > 9) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (inventory1_count > 9) and trade_sensitive:
                                                background "#143869"
                                                hover_background "#0a142688"
                                        textbutton ">|":
                                            action [Function(inventory_2.change_serum,serum, move_all_amount),Function(inventory_1.change_serum,serum,-move_all_amount)]
                                            sensitive (move_all_amount > 0) and trade_sensitive
                                            style "textbutton_no_padding_highlight" text_style "serum_text_style"
                                            if (move_all_amount > 0) and trade_sensitive:
                                                background "#143869"
                                                hover_background "#0a142688"

                                        null width 10

                                        frame:
                                            background "#000080"
                                            xsize 170
                                            text name_2 + ": " + str(inventory2_count) style "serum_text_style"

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.88]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            if hide_instead:
                action [Hide("serum_trade_ui"), Hide("serum_tooltip")]
            else:
                action [Return(), Hide("serum_tooltip")]
        textbutton "Return" align [0.5,0.5] text_style "return_button_style"
