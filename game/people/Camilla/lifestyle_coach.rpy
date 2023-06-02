#This file is for the lifestyle coach. A new minor unique character who can help coach the MC to meet new life goals.
#Found at the mall. Initially can help MC setup new work and personal goals, after corruption can help setup new sex goals and help meet them.
init -1 python:

    def lifestyle_coach_review_goals_requirement(person):
        if mc.business.is_open_for_business and mc.location is mall:
            return True
        if person.location is not mall:
            return "Only at the mall"
        else:
            return "Only during business hours"
        return False

    def lifestyle_coach_choose_sexy_goal_requirement(the_person):
        if the_person.sluttiness > 40 and mc.energy > 80 and the_person.energy > 80:
            if the_person.location == mall:
                return True
        return False

    lifestyle_coach_review_goals = Action("Review Goals", lifestyle_coach_review_goals_requirement, "lifestyle_coach_review_goals_label")
    lifestyle_coach_role = Role(role_name ="Lifestyle Coach", actions =[lifestyle_coach_review_goals], hidden = True)


label lifestyle_coach_review_goals_label(the_person):
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    $ mc.business.change_funds(-20)
    mc.name "Hey [the_person.title]. Do you have time to talk about goals again?"
    the_person "Certainly! Tell me about how things are going and what you would like to change."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    mc.name "Thanks for the help!"
    $ scene_manager.clear_scene()
    return
