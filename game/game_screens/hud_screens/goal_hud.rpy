default persistent.show_goal_ui = True

screen goal_hud_ui():
    if persistent.show_goal_ui:
        frame:
            background Transform(goal_frame_image, alpha=persistent.hud_alpha)
            yalign 0.5
            xysize (260, 250)
            vbox:
                textbutton "Goal Information" action Show("mc_character_sheet") style "textbutton_style" text_style "menu_text_title_style" text_size 14 xsize 245 tooltip "Complete goals to earn experience, and spend experience to improve your stats and skills."
                for goal in [mc.stat_goal,mc.work_goal,mc.sex_goal]:
                    frame:
                        ysize 60
                        background None
                        bar value goal.progress_fraction range 1.0 xalign 0.5 ysize 50 xfill True
                        textbutton "[goal.name]\n{color=#aaaaaa}[goal.progress_string]{/color}":
                            style "transparent_style"
                            text_style "serum_text_style_traits"
                            xfill True
                            text_size 16
                            yalign 0.5
                            action Show("mc_character_sheet")
                            sensitive True
                            tooltip goal.description
