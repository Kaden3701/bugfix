init 1 python:
    def set_IT_director_tag(key, value):
        if mc.business.it_director:
            mc.business.it_director.IT_tags[key] = value

    def get_IT_director_tag(key, default = None):
        if mc.business.it_director:
            return mc.business.it_director.IT_tags.get(key, default)

    def update_IT_projects_requirement(the_person):
        return mc.business.it_director and mc.business.is_open_for_business

    def IT_project_complete_requirement():
        return mc.business.it_director and mc.business.is_open_for_business and mc.is_at_work

    def IT_director_on_turn(the_person):
        if the_person.location == mc.business.r_div:
            mc.business.IT_increase_project_progress(amount = (the_person.int * 2) + (the_person.focus))
        return

    def IT_director_nanobot_intro_requirement(the_person):
        if mc.is_at_work:
            return True
        return False

    def IT_director_teamup_start_requirement():
        if mc.is_at_work and mc.business.it_director and mc.business.is_open_for_business:
            if mc.business.days_since_event("IT_dir_nanobot_takeover_day") >= TIER_2_TIME_DELAY:
                return True
        return False

    # def IT_director_on_move(the_person):
    #     if mc.business.is_open_for_business and mc.business.current_IT_project:


    update_IT_projects_action = Action("Review IT Projects", update_IT_projects_requirement, "update_IT_projects_label",
        menu_tooltip = "Start, change, activate, or deactivate IT projects.", priority = 5)
    IT_project_complete_action = Action("IT Project Complete", IT_project_complete_requirement, "IT_project_complete_label")
    IT_director_nanobot_intro = Action("Nanobot Programs", IT_director_nanobot_intro_requirement, "IT_director_nanobot_intro_label")
    IT_director_teamup_start = Action("IT and RnD Teamup Intro", IT_director_teamup_start_requirement, "IT_director_teamup_start_label")

    IT_director_role = Role("IT Director", [update_IT_projects_action], on_turn = IT_director_on_turn)



label update_IT_projects_label(the_person):
    mc.name "I'd like to review the IT projects."
    the_person "Ok. Here's what we have going on right now, [the_person.mc_title]."
    call screen it_project_screen()
    the_person "Got it. Is there anything else I can do for you, [the_person.mc_title]?"
    return

label IT_project_complete_label():
    $ the_person = mc.business.it_director
    if the_person is None:
        return
    $ the_person.draw_person()
    "[the_person.possessive_title] tracks you down while you are working."
    the_person "Hey [the_person.mc_title], just wanted to let you know I finished up with that project you had me working on."
    "You take a moment to review your completed projects and decide if you want her to start something different."
    call screen it_project_screen()
    "When you finish reviewing her projects, [the_person.title] gets back to work."

    return

label IT_director_nanobot_intro_label(the_person):
    "You approach [the_person.possessive_title] to talk to her about your nanobot program."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]."
    the_person "Hey [the_person.mc_title]. Need something?"
    mc.name "I do. Our research department has hit a bit of a dead end with the nanobot development project, and I was wondering if you could lend your expertise."
    the_person "I suppose. Didn't we already discuss the projects I could work on to improve your nanobots?"
    mc.name "Yes, but I have ideas for completely new programs I would like to have designed."
    the_person "Ah, I see."
    mc.name "Can we go to my office?"
    the_person "Sure."
    $ ceo_office.show_background()
    $ the_person.draw_person(position = "sitting")
    "You walk with [the_person.possessive_title] to your office. She sits down across from you."
    if fetish_serum_unlock_count() == 1:
        mc.name "Right, well as you know, we have a basic nanobot program, designed to increase a female's propensity for sexual activities."
        the_person "errmm... right..."
        mc.name "I have some ideas for programs that are a bit more... specific..."
        "You explain to [the_person.possessive_title] your ideas for four new nanobot programs."
        $ the_person.change_slut(1, 40)
    elif fetish_serum_unlock_count() < 4:
        mc.name "Right. As you know, we have a few basic programs for our nanobots, but I have ideas for more."
        "You explain to [the_person.possessive_title] your ideas for new nanobot programs."
        $ the_person.change_slut(1, 40)
    elif fetish_serum_unlock_count() == 4:
        mc.name "Right. As you know, we have a few programs for our nanobots, but I have an idea for one more."
        "You explain to [the_person.possessive_title] your idea for a new nanobot program."
        $ the_person.change_slut(1, 40)
    else:
        mc.name "Right. As you know, we have several programs for our nanobots, but we still know so little about how they actually affect people."
    if fetish_serum_unlock_count() < 5:
        "When you finish, her cheeks are flushed from embarrassment."
        the_person "I... I don't know... you're talking about..."
        mc.name "I know. This is a little outside of your comfort zone, but as my only IT employee, I need you to step up and help out with it."
        "She seems unconvinced for now, but relents."
        the_person "I suppose I could do that."
        $ the_person.change_obedience(3)
        mc.name "Thank you. In addition, we know so little about how they actually affect people."
    mc.name "I was hoping you would be willing to work with Research so we can learn more about them."
    mc.name "Nothing crazy, just help monitor their effects as we run tests with them."
    the_person "I'm not sure this is a good idea..."
    "It seems like [the_person.title] might need some convincing..."
    menu:
        "Do it for me\n{color=#ff0000}{size=18}Increases love{/size}{/color}":
            mc.name "I know this seems odd, but I need you to trust me, okay?"
            mc.name "Don't worry, I have a plan, and I need someone like you to get this done."
            $ the_person.change_love(3)
        "It'll be fun\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color}":
            mc.name "Don't worry. We'll be able to use it to have all kinds of fun."
            $ the_person.change_slut(3, 60)
        "I'm the boss\n{color=#ff0000}{size=18}Increases obedience{/size}{/color}":
            mc.name "I know it seems odd, but remember who makes out your paychecks, okay?"
            $ the_person.change_obedience(3)
    the_person "I suppose..."
    mc.name "Great!"
    $ the_person.draw_person()
    "You both stand up."
    the_person "I'll add those programs to the list of projects I can work on then... just let me know when you want me to work on them."
    mc.name "Certainly."
    $ the_person.draw_person(position = "walking_away")
    $ mc.business.event_triggers_dict["fetish_to_IT"] = True
    "[the_person.possessive_title] turns and walks out of your office."
    "From now on, you can work with her towards perfecting your nanobot programs."
    "In addition, you can talk to her about the programs as you begin to master them."
    $ mc.business.set_event_day("IT_dir_nanobot_takeover_day")
    $ mc.business.add_mandatory_crisis(IT_director_teamup_start)
    $ mc.location.show_background()
    $ clear_scene()
    return

label IT_director_teamup_start_label():
    call ellie_stephanie_teamup_progression_scene_action_label(ellie) from _it_director_teamup_intro_prog_scene_intro_01
    return
