#####################################  Scene Idea  ##############################################
# Scene: One one One Training
#        Pick a random (obedient? intelligent? Probably not bimbo) employee during business hours. Verify they have at least one work skill lower than MC
#        Give MC the option to train the NPC in the skill for a random (small) increase
#        ***Optional:
#        If NPC is slutty (>60?), check and see if MC has sex skill greater than NPC
#        If yes, have NPC ask if MC will train her in sex skill
#        Check if MC has energy. If yes give MC option to train in sex skill
#        If yes, trigger sex skill training scene.
#
#        Future options: Other benefits for NPCs having high sex skills
#
################################################################################################
init 2 python:
    # increases affection for trained job (if not maxed)
    def increase_job_affection(person, job_description):
        score = person.get_opinion_score(job_description)
        if score < 2:
            score += 1
            person.opinions[job_description] = [score, True]
            mc.log_event((person.title or person.name) + " now " + opinion_score_to_string(score) + " " + job_description + ".", "float_text_grey")
        return

    def one_on_one_training_requirement():
        if mc.is_at_work:
            if mc.business.is_open_for_business:
                return any(x for x in mc.business.employee_list if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill))
            if mc.business.is_open_for_internship:
                return any(x for x in mc.business.intern_list if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill))
        return False

    def get_training_employee():
        return get_random_from_list([x for x in mc.business.employee_list if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill)])

    def get_training_intern():
        return get_random_from_list([x for x in mc.business.intern_list if x.obedience > 110 and x.int > 1 and (mc.hr_skill > x.hr_skill or mc.supply_skill > x.supply_skill or mc.market_skill > x.market_skill or mc.research_skill > x.research_skill or mc.production_skill > x.production_skill)])

    def one_on_one_update_HR_skill(person):
        increase = renpy.random.randint(1,(mc.hr_skill - person.hr_skill))
        person.hr_skill += increase
        mc.log_event((person.title or person.name) + ": +" + str(increase) + " HR Skill", "float_text_grey")
        increase_job_affection(person, "HR work")
        if perk_system.has_ability_perk("Those Who Can't, Teach"):
            if mc.hr_skill < mc.max_work_skills:
                mc.hr_skill += 1
                mc.log_event("+1 HR skill from Perk", None)
        return True

    def one_on_one_update_supply_skill(person):
        increase = renpy.random.randint(1,(mc.supply_skill - person.supply_skill))
        person.supply_skill += increase
        mc.log_event((person.title or person.name) + ": +" + str(increase) + " Supply skill", "float_text_grey")
        increase_job_affection(person, "supply work")
        if perk_system.has_ability_perk("Those Who Can't, Teach"):
            if mc.supply_skill < mc.max_work_skills:
                mc.supply_skill += 1
                mc.log_event("+1 Supply skill from Perk", None)
        return True

    def one_on_one_update_marketing_skill(person):
        increase = renpy.random.randint(1,(mc.market_skill - person.market_skill))
        person.market_skill += increase
        mc.log_event((person.title or person.name) + ": +" + str(increase) + " Marketing skill", "float_text_grey")
        increase_job_affection(person, "marketing work")
        if perk_system.has_ability_perk("Those Who Can't, Teach"):
            if mc.market_skill < mc.max_work_skills:
                mc.market_skill += 1
                mc.log_event("+1 Market skill from Perk", None)
        return True

    def one_on_one_update_research_skill(person):
        increase = renpy.random.randint(1,(mc.research_skill - person.research_skill))
        person.research_skill += increase
        mc.log_event((person.title or person.name) + ": +" + str(increase) + " Researching skill", "float_text_grey")
        increase_job_affection(person, "research work")
        if perk_system.has_ability_perk("Those Who Can't, Teach"):
            if mc.research_skill < mc.max_work_skills:
                mc.research_skill += 1
                mc.log_event("+1 Research skill from Perk", None)
        return True

    def one_on_one_update_production_skill(person):
        increase = renpy.random.randint(1,(mc.production_skill - person.production_skill))
        person.production_skill += increase
        mc.log_event((person.title or person.name) + ": +" + str(increase) + " Production skill", "float_text_grey")
        increase_job_affection(person, "production work")
        if perk_system.has_ability_perk("Those Who Can't, Teach"):
            if mc.production_skill < mc.max_work_skills:
                mc.production_skill += 1
                mc.log_event("+1 Production skill from Perk", None)
        return True

    one_on_one_action = ActionMod("One on One Training", one_on_one_training_requirement, "SB_one_on_one_label",
        menu_tooltip = "You give an employee on the job training.", category = "Business", is_crisis = True)

label SB_one_on_one_label():
    if mc.business.is_open_for_business:
        $ the_person = get_training_employee()
    else:
        $ the_person = get_training_intern()
    if the_person is None: # "No one eligible for training!"
        return

    $ old_location = mc.location
    $ mc.change_location(lobby)

    "You take a quick break from work to go get a quick snack from the vending machine. While you are trying do decide what snack to buy, [the_person.possessive_title] enters the break room."
    $ the_person.draw_person()
    the_person "Oh, hey [the_person.mc_title]!"
    "You keep chatting with [the_person.possessive_title] for a while. Eventually, the subject of your role in the company and the various jobs you fulfill around the lab comes up."
    the_person "Yeah, I've heard that you are pretty skilled at some of the different jobs in the lab here. I was wondering if maybe you could give me some pointers?"
    "You consider [the_person.possessive_title]'s request for a moment, taking into account her personal ambitions and skill level."
    $ done = False
    $ dislike = False
    $ topic = None
    menu:
        "Train HR" if the_person.hr_skill < mc.hr_skill and the_person.get_opinion_score("HR work") > -2:
            "You explain to [the_person.possessive_title] the ins and outs of HR work. You do it in pretty broad terms, but touch on all the important parts."
            if the_person.get_opinion_score("HR work") < 0:
                $ dislike = True
                $ topic = "HR work"
            else:
                $ done = one_on_one_update_HR_skill(the_person)

        "Train Supply" if the_person.supply_skill < mc.supply_skill and the_person.get_opinion_score("supply work") > -2:
            "You do some hands on training with [the_person.possessive_title], showing her various methods for securing the different chemicals required for serum production."
            if the_person.get_opinion_score("supply work") < 0:
                $ dislike = True
                $ topic = "supply work"
            else:
                $ done = one_on_one_update_supply_skill(the_person)

        "Train Marketing" if the_person.market_skill < mc.market_skill and the_person.get_opinion_score("marketing work") > -2:
            "You spend some time with [the_person.possessive_title], giving all kinds of advice on the art of the sale. It's not just about good deals, but making people understand they need the product you offer."
            if the_person.get_opinion_score("marketing work") < 0:
                $ dislike = True
                $ topic = "marketing work"
            else:
                $ done = one_on_one_update_marketing_skill(the_person)

        "Train Research" if the_person.research_skill < mc.research_skill and the_person.get_opinion_score("research work") > -2:
            "You talk with [the_person.possessive_title] about various chemicals and scientific methods, and how they apply to different portions of the brain."
            if the_person.get_opinion_score("research work") < 0:
                $ dislike = True
                $ topic = "research work"
            else:
                $ done = one_on_one_update_research_skill(the_person)

        "Train Production" if the_person.production_skill < mc.production_skill and the_person.get_opinion_score("production work") > -2:
            "You share some insights with [the_person.possessive_title] about the chemical processes and reactions between common serum elements."
            if the_person.get_opinion_score("production work") < 0:
                $ dislike = True
                $ topic = "production work"
            else:
                $ done = one_on_one_update_production_skill(the_person)

        "Too Busy":
            "You apologize. You are just too busy to offer one on one training right now."
    if done:
        the_person "Thanks for the help, [the_person.mc_title]. I'm sure that will come in handy during work around here!"
        if not perk_system.has_ability_perk("Those Who Can't, Teach"):
            "Teaching someone else has given you new insights into your own skills. You realize by teaching others, you increase you own mastery in a given skill set."
            $ perk_system.add_ability_perk(Ability_Perk(description = "When you teach someone else a skill, you also gain a skill point in that area.", active = False, usable = False), "Those Who Can't, Teach")
        elif not perk_system.has_stat_perk("Those Who Can, Do"):
            if mc.production_skill == mc.max_work_skills:
                "Sharing with someone a skill you thought you had wholly mastered reveals a few final deficient areas. You feel like you can take your skills even further now."
                $ perk_system.add_stat_perk(Stat_Perk(description = "Teaching others has raised your skill ceiling to new levels. +1 work skills cap", skill_cap = 1), "Those Who Can, Do")
    elif dislike:
        if the_person.discover_opinion(topic):
            "As you talk you catch glimmers of what could be disgust cross her face. It seems like [topic] might have been the thing to discuss with [the_person.title]."
        else:
            "As you get further into the details you recall that [the_person.title] doesn't really like [topic]."
        "Since it is too late to start over you shift focus, talking up the positive and enjoyable parts of the job."
        if renpy.random.randint(0, 100) < mc.charisma * 5: # about 50% max success rate
            "Surprisingly it seems to work and [the_person.title] starts to nod along as you finish talking."
            $ the_person.increase_opinion_score(topic)
            the_person "You know, when you say it that way, maybe it wouldn't be so bad to do that everyday."
        else:
            "Unfortunately she doesn't seem to be moved by your words."
            the_person "Sorry, I just don't think I would ever be happy doing [topic]."
    else:
        the_person "That's okay, [the_person.mc_title], I understand. Maybe another time then!"

    $ mc.change_location(old_location)
    $ old_location = None
    $ clear_scene()
    return
