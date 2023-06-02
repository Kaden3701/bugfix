init -2 python: # Some functions used only within screens for modifying variables
    def show_candidate(the_candidate):
        clear_scene()
        the_candidate.draw_person(show_person_info = False, background_fill = "444444", the_animation = no_animation)

    def interview_reveal_age():
        reveal_age = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_age = reveal_age or recruitment_policy.extra_data.get("reveal_age",False)
        return reveal_age

    def interview_reveal_tits():
        reveal_tits = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_tits = reveal_tits or recruitment_policy.extra_data.get("reveal_tits",False)
        return reveal_tits

    def interview_reveal_sex_skills():
        reveal_sex_skills = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_sex_skills = reveal_sex_skills or recruitment_policy.extra_data.get("reveal_sex_skills",False)
        return reveal_sex_skills

    def interview_reveal_kids():
        reveal_kids = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_kids = reveal_kids or recruitment_policy.extra_data.get("reveal_kids",False)
        return reveal_kids

    def interview_reveal_relationship():
        reveal_relationship = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_relationship = reveal_relationship or recruitment_policy.extra_data.get("reveal_relationship",False)
        return reveal_relationship

    def interview_reveal_suggestibility():
        reveal_suggestibility = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_suggestibility = reveal_suggestibility or recruitment_policy.extra_data.get("reveal_suggestibility",False)
        return reveal_suggestibility

    def interview_reveal_obedience():
        reveal_obedience = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_obedience = reveal_obedience or recruitment_policy.extra_data.get("reveal_obedience",False)
        return reveal_obedience

    def interview_reveal_sluttiness():
        reveal_sluttiness = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_sluttiness = reveal_sluttiness or recruitment_policy.extra_data.get("reveal_sluttiness",False)
        return reveal_sluttiness

    def interview_reveal_happiness():
        reveal_happiness = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_happiness = reveal_happiness or recruitment_policy.extra_data.get("reveal_happiness",False)
        return reveal_happiness

    def interview_reveal_love():
        reveal_love = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_love = reveal_love or recruitment_policy.extra_data.get("reveal_love",False)
        return reveal_love

    def interview_reveal_height():
        reveal_height = False
        for recruitment_policy in recruitment_policies_list:
            if recruitment_policy.is_active:
                reveal_height = reveal_height or recruitment_policy.extra_data.get("reveal_height",False)
        return reveal_height

    def show_candidate(person):
        clear_scene()
        person.draw_person(show_person_info = False)
        return

    def build_recruitment_traits_slug():
        traits = []
        if recruitment_stat_improvement_policy.is_active:
            if recruitment_stat_minimums_policy.is_active:
                traits.append("Highly Skilled Worker")
            else:
                traits.append("Skilled Worker")
        if recruitment_suggest_improvement_policy.is_active:
            traits.append("Suggestible")
        if recruitment_obedience_improvement_policy.is_active:
            traits.append("Obedient")
        if recruitment_slut_improvement_policy.is_active:
            traits.append("Slutty")
        if recruitment_sex_improvement_policy.is_active:
            if recruitment_sex_minimums_policy.is_active:
                traits.append("Sexual Expert")
            else:
                traits.append("Sexual Skills")

        return ', '.join(traits)

screen interview_ui(the_candidates, count):
    default requirements = mc.business.generate_candidate_requirements()
    default current_selection = 0
    default the_candidate = the_candidates[current_selection]
    vbox:
        yalign 0.2
        xalign 0.4
        xanchor 0.5
        spacing 30
        frame:
            background "#1a45a1aa"
            ysize 80
            xsize 1320
            xalign 0.5
            xanchor 0.5
            text "[the_candidate.name] [the_candidate.last_name]" style "menu_text_style" size 50 xanchor 0.5 xalign 0.5 color the_candidate.char.who_args["color"] font the_candidate.char.what_args["font"]
        hbox:
            xsize 1320
            spacing 30
            frame:
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Personal Information" style "menu_text_title_style" size 20 #Info about the person: age, height, happiness, obedience, etc.
                    if interview_reveal_age():
                        text "Age: [the_candidate.age]" style "menu_text_style" size 16
                    if interview_reveal_height():
                        text "Height: " + height_to_string(the_candidate.height) style "menu_text_style" size 16
                        text "Weight: " + get_person_weight_string(the_candidate) style "menu_text_style" size 16
                    if interview_reveal_happiness():
                        text "Happiness: [the_candidate.happiness]" style "menu_text_style" size 16
                    if interview_reveal_suggestibility():
                        text "Suggestibility: [the_candidate.suggestibility]" style "menu_text_style" size 16
                    if interview_reveal_sluttiness():
                        text "Sluttiness: [the_candidate.sluttiness]" style "menu_text_style" size 16
                    if interview_reveal_love():
                        text "Love: [the_candidate.love]" style "menu_text_style" size 16
                    if interview_reveal_obedience():
                        text "Obedience: [the_candidate.obedience] - " + get_obedience_string(the_candidate.obedience) style "menu_text_style" size 16
                    if interview_reveal_tits():
                        text "Cup Size: [the_candidate.tits]" style "menu_text_style" size 16
                        text "Eye Colour: " + the_candidate.eyes[0].title() style "menu_text_style" size 16
                    if interview_reveal_relationship():
                        if the_candidate.has_role(girlfriend_role):
                            text "Relationship: Girlfriend" style "menu_text_style" size 16
                        else:
                            text "Relationship: [the_candidate.relationship]" style "menu_text_style" size 16

                        if the_candidate.relationship != "Single":
                            text "Significant Other: [the_candidate.SO_name]" style "menu_text_style" size 16
                        elif the_candidate.has_role(girlfriend_role):
                            text "Significant Other: [mc.name]" style "menu_text_style" size 16

                    if interview_reveal_kids():
                        text "Kids: [the_candidate.kids]" style "menu_text_style" size 16

                    text "Required Salary: $[the_candidate.salary]/day" style "menu_text_style" size 16

            frame:
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Stats and Skills" style "menu_text_title_style" size 20 #Info about the persons raw stats, work skills, and sex skills
                    text "Work Experience Level: [the_candidate.work_experience]" style "menu_text_style" size 16
                    text "Stats" style "menu_text_style" size 20
                    text "    Charisma: [the_candidate.charisma]" style "menu_text_style" size 16
                    text "    Intelligence: [the_candidate.int]" style "menu_text_style" size 16
                    text "    Focus: [the_candidate.focus]" style "menu_text_style" size 16
                    text "Work Skills" style "menu_text_style" size 20
                    text "    HR: [the_candidate.hr_skill]" style "menu_text_style" size 16
                    text "    Marketing: [the_candidate.market_skill]" style "menu_text_style" size 16
                    text "    Research: [the_candidate.research_skill]" style "menu_text_style" size 16
                    text "    Production: [the_candidate.production_skill]" style "menu_text_style" size 16
                    text "    Supply: [the_candidate.supply_skill]" style "menu_text_style" size 16
                    if interview_reveal_sex_skills():
                        text "Sex Skills" style "menu_text_style" size 20
                        text "    Foreplay: " + str(the_candidate.sex_skills["Foreplay"]) style "menu_text_style" size 16
                        text "    Oral: " + str(the_candidate.sex_skills["Oral"]) style "menu_text_style" size 16
                        text "    Vaginal: " + str(the_candidate.sex_skills["Vaginal"]) style "menu_text_style" size 16
                        text "    Anal: " + str(the_candidate.sex_skills["Anal"]) style "menu_text_style" size 16

            frame:
                $ master_opinion_dict = dict(the_candidate.opinions, **the_candidate.sexy_opinions)
                background "#1a45a1aa"
                xsize 420
                ysize 550
                vbox:
                    text "Opinions" style "menu_text_title_style" size 20 #Info about the persons loves, likes, dislikes, and hates
                    hbox:
                        spacing 5
                        vbox:
                            xsize 210
                            text "Loves" style "menu_text_style" size 22
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == 2:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "????" style "menu_text_style" size 16
                        vbox:
                            text "Likes" style "menu_text_style" size 22
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == 1:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "????" style "menu_text_style" size 16
                    hbox:
                        ysize 14
                    hbox:
                        spacing 5
                        vbox:
                            xsize 210
                            text "Dislikes" style "menu_text_style" size 20
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == -1:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "????" style "menu_text_style" size 16

                        vbox:
                            text "Hates" style "menu_text_style" size 20
                            for opinion in master_opinion_dict:
                                if master_opinion_dict[opinion][0] == -2:
                                    if master_opinion_dict[opinion][1]:
                                        text opinion.title() style "menu_text_style" size 16
                                    else:
                                        text "????" style "menu_text_style" size 16

        frame:
            background "#1a45a1aa"
            xsize 1320
            ysize 200
            hbox:
                vbox:
                    xsize 650
                    text "Expected Production" style "menu_text_title_style"
                    text "    Human Resources: +" + str(human_resource_potential_stat(the_candidate)) + "% Company efficiency per turn" style "menu_text_style" size 16
                    text "    Marketing: +" + str(marketing_potential_stat(the_candidate)) + " Market reach increased per turn" style "menu_text_style" size 16
                    text "    Research and Development: " + str(research_potential_stat(the_candidate)) + " Research points per turn" style "menu_text_style" size 16
                    text "    Production: " + str(production_potential_stat(the_candidate)) + " Production points per turn" style "menu_text_style" size 16
                    text "    Supply Procurement: " + str(supply_potential_stat(the_candidate)) + " Units of supply per turn" style "menu_text_style" size 16

                if count > 1:
                    vbox:
                        text "Recruitment Settings" style "menu_text_title_style"
                        text "    Age Range: " + str(requirements.get("age_floor", 18)) + " - "+ str(requirements.get("age_ceiling", 55)) style "menu_text_style" size 16
                        if recruitment_single_policy.is_active or recruitment_married_policy.is_active:
                            text "    Relation: " + ("Single" if recruitment_single_policy.is_active else "Married") style "menu_text_style" size 16
                        if "tits" in requirements.keys():
                            text "    Cup-size: " + requirements.get("tits", "AA") style "menu_text_style" size 16
                        if recruitment_mothers_policy.is_active or recruitment_childless_policy.is_active:
                            text "    Children: " + ("Yes" if recruitment_mothers_policy.is_active else "No") style "menu_text_style" size 16
                        if recruitment_short_policy.is_active or recruitment_tall_policy.is_active:
                            text "    Height: " + ("Short" if recruitment_short_policy.is_active else "Tall") style "menu_text_style" size 16
                        if recruitment_suggest_improvement_policy.is_active or recruitment_obedience_improvement_policy.is_active or recruitment_slut_improvement_policy.is_active:
                            text "    Traits: " + build_recruitment_traits_slug() style "menu_text_style" size 16

        frame:
            background "#1a45a1aa"
            xsize 1320
            ysize 100
            hbox:
                align (.5, .5)
                textbutton "Previous Candidate":
                    sensitive current_selection > 0
                    selected False
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        SetScreenVariable("current_selection",current_selection-1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection-1]),
                        Function(show_candidate,the_candidates[current_selection-1])
                    ]

                null width 320
                textbutton " Hire Nobody  ":
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        Function(the_candidate.hide_person),
                        Return("None")
                    ]

                null width 20

                textbutton " Hire  ":
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        Function(the_candidate.hide_person),
                        Return(the_candidate)
                    ]

                null width 320
                textbutton "Next Candidate":
                    sensitive current_selection < count-1
                    selected False
                    style "textbutton_style"
                    text_style "textbutton_text_style"
                    action [
                        SetScreenVariable("current_selection",current_selection+1),
                        SetScreenVariable("the_candidate",the_candidates[current_selection+1]),
                        Function(show_candidate,the_candidates[current_selection+1])
                    ]


    imagebutton:
        auto "/tutorial_images/restart_tutorial_%s.png"
        xysize (54, 54)
        anchor (1.0, 1.0)
        align (1.0, 1.0)
        action Function(mc.business.reset_tutorial,"hiring_tutorial")

    if mc.business.event_triggers_dict.get("hiring_tutorial", 0) > 0 and mc.business.event_triggers_dict.get("hiring_tutorial", 1) <= 5: #We use negative numbers to symbolize the tutorial not being enabled
        imagebutton:
            sensitive True
            xsize 1920
            ysize 1080
            idle "/tutorial_images/hiring_tutorial_{}.png".format(mc.business.event_triggers_dict.get("hiring_tutorial", 1))
            hover "/tutorial_images/hiring_tutorial_{}.png".format(mc.business.event_triggers_dict.get("hiring_tutorial", 1))
            action Function(mc.business.advance_tutorial,"hiring_tutorial")
