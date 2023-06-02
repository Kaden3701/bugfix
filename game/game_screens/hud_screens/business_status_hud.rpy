label check_business_inventory_loop:
    call screen show_serum_inventory(mc.business.inventory,[],["Business Inventory"])
    return

screen business_ui(): #Shows some information about your business.
    python:
        count = number_of_hints()
        employee_count = str(mc.business.employee_count) + "/" + str(mc.business.max_employee_count)
        funds = "${funds:,}".format(funds = __builtin__.int(mc.business.funds))
        daily_salary = "$"+ str(__builtin__.int(mc.business.calculate_salary_cost())) + " | $" + str(__builtin__.int(mc.business.operating_costs))
        efficiency = str(__builtin__.int(mc.business.team_effectiveness)) + "%"
        supplies = str(__builtin__.int(mc.business.supply_count)) +"/" + str(__builtin__.int(mc.business.supply_goal))
        if mc.business.active_research_design:
            current_research = "(" + str(__builtin__.int(mc.business.active_research_design.current_research)) + "/" + str(__builtin__.int(mc.business.active_research_design.research_needed)) + ")"

    frame:
        background Transform(im.Flip(info_frame_image, vertical=True), alpha=persistent.hud_alpha)
        xsize 600
        ysize 400
        yalign 1.0
        vbox:
            yanchor 1.0
            yalign 1.0
            yoffset -30
            spacing 5
            text "[mc.business.name]" style "menu_text_title_style" xalign 0.03 yoffset -10
            textbutton "Employee Count: [employee_count]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Your current and maximum number of employees. Purchase new business policies from your CEO office to increase the number of employees you can have."
                action NullAction()

            textbutton "Company Funds: [funds]":
                style "transparent_style"
                text_style "menu_text_style"
                if mc.business.funds < 0:
                    text_color "#DD0000"
                tooltip "The amount of money in your business account. If you are in the negatives for more than three days your loan defaults and the game is over!"
                action NullAction()

            textbutton "Daily Salary Cost: [daily_salary]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "The amount of money spent daily to pay your employees along with daily operating costs. Neither apply during the weekend."
                action NullAction()

            textbutton "Company Efficiency: [efficiency]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "The more employees you have the faster your company will become inefficient. Perform HR work at your office or hire someone to do it for you to raise your company Efficiency. All productivity is modified by company Efficiency."
                action NullAction()

            textbutton "Current Raw Supplies: [supplies]":
                style "transparent_style"
                text_style "menu_text_style"
                tooltip "Your current and goal amounts of serum supply. Manufacturing serum requires supplies, spend time ordering supplies from your office or hire someone to do it for you. Raise your supply goal from your office if you want to keep more supply stockpiled."
                action NullAction()

            if not mc.business.active_research_design is None:
                textbutton "Current Research:":
                    style "transparent_style"
                    text_style "menu_text_style"
                textbutton "[mc.business.active_research_design.name] [current_research]":
                    style "transparent_style"
                    text_style "menu_text_style"
                    text_color "#43B197"
                    tooltip "The current research task of your R&D division. Visit them to set a new goal or to assemble a new serum design."
                    action NullAction()

            else:
                textbutton ("Current Research: None!" if not theoretical_research.is_active else "Current Research: Theoretical Research"):
                    style "transparent_style"
                    text_style "menu_text_style"
                    text_color "#B14365"
                    tooltip "The current research task of your R&D division. Visit them to set a new goal or to assemble a new serum design."
                    action NullAction()

            hbox:
                vbox:
                    xsize 230
                    textbutton "Review Staff" action Show("employee_overview") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Review all of your current employees."
                    textbutton "Check Stock" action ui.callsinnewcontext("check_business_inventory_loop") style "textbutton_style" text_style "textbutton_text_style" xsize 220 tooltip "Check the doses of serum currently waiting to be sold or sitting in your production area."
                vbox:
                    xsize 80
                    if count > 0:
                        hbox:
                            xpos 85
                            ypos 35
                            textbutton "{image=question_mark}":
                                background None
                                text_style "textbutton_text_style"
                                action NullAction()
                                hovered [
                                    Show("game_hints_tooltip")
                                ]
                                unhovered [
                                    Hide("game_hints_tooltip")
                                ]
                            text "[count]" style "serum_text_style_header" yoffset 10
