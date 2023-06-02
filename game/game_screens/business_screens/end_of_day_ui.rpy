screen end_of_day_update():
    add paper_background_image
    zorder 100
    modal True

    hbox:
        xalign 0.5
        yoffset 20
        spacing 200
        ysize 100

        text mc.business.name style "menu_text_title_style" size 40 xalign 0.5

    frame:
        background "#1a45a1aa"
        yoffset 100
        xalign 0.05
        xanchor 0.0
        yanchor 0.0
        xsize 1700
        ysize 230

        hbox:
            spacing 100
            vbox:
                xsize 800
                text "Daily Statistics:" style "textbutton_text_style" size 26
                text "     " + "Company Efficiency: " + str(mc.business.team_effectiveness) + "%" style "textbutton_text_style"
                text "     " + "Production Potential: " + str(__builtin__.int(mc.business.production_potential)) + " Units" style "textbutton_text_style"
                text "     " + "Supplies Procured: " + str(mc.business.supplies_purchased) + " Units" style "textbutton_text_style"
                text "     " + "Production Used: " + str(__builtin__.int(mc.business.production_used)) + " Units" style "textbutton_text_style"
                text "     " + "Research Produced: " + str(__builtin__.int(mc.business.research_produced)) style "textbutton_text_style"

            vbox:
                xsize 800
                $ profit = mc.business.funds - mc.business.funds_yesterday
                $ mc.business.listener_system.fire_event("daily_profit", profit = profit)
                text ("Profit" if profit > 0 else "Loss") + ": $ " + str(__builtin__.round(abs(profit), 2))  style "textbutton_text_style" size 26 color ("#00A000" if profit > 0 else "#A00000")
                text "     " + "Sales Made: $ " + str(__builtin__.round(mc.business.sales_made, 2)) style "textbutton_text_style"
                if mc.business.is_work_day:
                    text "     " + "Daily Salary Paid: $ " + str(__builtin__.round(mc.business.calculate_salary_cost(), 2)) style "textbutton_text_style"
                    text "     " + "Daily Operating Costs: $" + str(mc.business.operating_costs) style "textbutton_text_style"
                #text "     " + "Serums Sold Today: " + str(mc.business.serums_sold) + " Vials" style "textbutton_text_style"
                text "     " + "Serums Ready for Sale: " + str(mc.business.inventory.total_serum_count) + " Vials" style "textbutton_text_style"

    frame:
        background "#1a45a1aa"
        xalign 0.05
        yoffset 350
        xanchor 0.0
        yanchor 0.0

        viewport:
            mousewheel True
            scrollbars "vertical"
            xsize 1690
            ysize 500
            vbox:
                text "Highlights:" style "textbutton_text_style" size 26
                for item in mc.business.message_list:
                    text "     " + item style "textbutton_text_style" size 20

                for item in mc.business.counted_message_list:
                    text "     " + item + " x " + str(__builtin__.int(mc.business.counted_message_list[item])) style "textbutton_text_style" size 20

    frame:
        background None
        anchor [0.5,0.5]
        align [0.5,0.9]
        xysize [500,125]
        imagebutton:
            align [0.5,0.5]
            auto "gui/button/choice_%s_background.png"
            focus_mask "gui/button/choice_idle_background.png"
            action [
                Return()
            ]
        textbutton "End Day" id "end_day_button_text" align [0.5,0.5] style "button_text"
