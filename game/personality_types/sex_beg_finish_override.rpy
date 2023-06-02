# Will add a little of stripping to all the sex_beg_finish dialogs
# Original idea by BadRabbit

init 5 python:
    def inject_sex_beg_finish_labels():
        for lbl in renpy.get_all_labels():
            if lbl.endswith("sex_beg_finish"):
                # use AST label hook to execute python function while calling the original label
                hook_label(lbl, enhanced_sex_beg_finish)
        return

    def remove_clothing_based_on_preference(person):
        if person.get_opinion_score("showing her tits") > person.get_opinion_score("showing her ass"):
            # tits preference
            person.strip_outfit_to_max_sluttiness(exclude_lower = True, temp_sluttiness_boost = 20)
        elif person.get_opinion_score("showing her tits") < person.get_opinion_score("showing her ass"):
            # vagina/ass preference
            person.strip_outfit_to_max_sluttiness(exclude_upper = True, temp_sluttiness_boost = 20)

        # strip remaining if slutty enough
        person.strip_outfit_to_max_sluttiness()
        return

    def enhanced_sex_beg_finish(hook):
        remove_clothing_based_on_preference(the_person)
        return

    inject_sex_beg_finish_labels()
