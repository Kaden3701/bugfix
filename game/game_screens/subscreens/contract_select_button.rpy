init -2 python:
    def get_design_names_that_satisfy_contract(contract):
        usable_serums = []
        for sd in [x for x in mc.business.serum_designs if contract.check_serum(x)]:
            usable_serums.append(sd.name)

        if usable_serums:
            return ", ".join(usable_serums)
        return "None"

screen contract_select_button(contract):
    frame:
        background "#00000088"
        xsize 800
        hbox:
            ysize 140
            vbox:
                xsize 580
                text "[contract.name]":
                    style "textbutton_text_style"
                    size 20

                use contract_aspect_grid(contract)

                text "[contract.description]" style "textbutton_text_style" size 14 text_align 0.0
                text "Usable designs: " + get_design_names_that_satisfy_contract(contract) style "textbutton_text_style" size 16 text_align 0.0

            vbox:
                yfill False
                xanchor 1.00
                xalign 0.95
                xsize 195
                transclude #Place things on the right side of this entry for things like accessing the inventory.
