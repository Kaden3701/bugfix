# Camilla's obedience events involve unlocking new and interesting goals for MC
# At first, they are normal goals, but eventually evolve into sexual goals.
# Nora gets introduced to Camilla through her love story if Camilla is far enough along in this storyline.



init -1 python: #Requirement functions
    def camilla_obedience_new_goals_requirement(person):
        if person.obedience < 120:
            return False
        if not person.story_event_ready("obedience"):
            return False
        if person.location != mall:
            return False
        return True

    def camilla_obedience_sexual_goals_intro_requirement(person):
        if person.obedience < 140:
            return False
        if not person.story_event_ready("obedience"):
            return False
        if person.location != mall:
            return False
        return True

    def camilla_obedience_tit_fuck_requirement(person):
        if person.obedience < 160:
            return False
        if not person.story_event_ready("obedience"):
            return False
        if person.location != mall:
            return False
        return True

    def camilla_obedience_ass_man_requirement(person):
        return False
        if person.obedience < 180:
            return False
        if not person.story_event_ready("obedience"):
            return False
        if person.location != mall:
            return False
        return True


init 2 python:  #Actions
    camilla_obedience_new_goals = Action("Making New Goals", camilla_obedience_new_goals_requirement, "camilla_obedience_new_goals_label")
    camilla_obedience_sexual_goals_intro = Action("Exploring Sexual Goals", camilla_obedience_sexual_goals_intro_requirement, "camilla_obedience_sexual_goals_intro_label")
    camilla_obedience_tit_fuck = Action("MC Loves Tits", camilla_obedience_tit_fuck_requirement, "camilla_obedience_tit_fuck_label")
    camilla_obedience_ass_man = Action("MC Loves Ass", camilla_obedience_ass_man_requirement, "camilla_obedience_ass_man_label")


#Obedience Labels.
label camilla_obedience_new_goals_label(the_person):    #120 obedience
    $ the_person.story_event_log("obedience")
    "In this label, we convince Camilla to help us come up with new goals."
    "She walks MC through the process, encourages him to learn what actions make him feel good, and to pursue those."
    $ camilla.event_triggers_dict["goal_coach"] = True
    $ camilla.add_unique_on_room_enter_event(camilla_obedience_sexual_goals_intro)
    return

label camilla_obedience_sexual_goals_intro_label(the_person):   #140 obedience
    $ the_person.story_event_log("obedience")
    "In this label, Camilla works with MC to come up with new sexual goals. This level of sexual goals a will be fairly tame."
    $ camilla.event_triggers_dict["sex_goal_coach"] = True
    $ camilla.add_unique_on_room_enter_event(camilla_obedience_tit_fuck)
    return

label camilla_obedience_tit_fuck_label(the_person): #160 obedience. Previously sluttiness trigger.
    $ the_person.draw_person()
    $ the_person.story_event_log("obedience")
    "You step up to [the_person.possessive_title]. She smiles as you approach her."
    the_person "Hey [the_person.mc_title] here to review your goals?"
    "You do want to... but you find yourself faltering for a second."
    "Setting goals, both long term and short term is important... but what really are your goals, anyway?"
    mc.name "I think so, but to be honest, I'm having trouble deciding what I even want."
    the_person "I see. Well, an exercise that might help. Let's pretend like money wasn't an obstacle. If you could do anything you wanted to right now, what would you do?"
    "You look at [the_person.possessive_title]. You think about the question for a moment... but soon your eyes drift down from her face..."
    "Her chest... her belly... her hips..."
    $ mc.change_locked_clarity(10)
    "You close your eyes."
    "Try as you might, you can't get images of her sexy body out of your head."
    the_person "That's it. Visualize what you want. What drives you? What gets you out of bed every morning? Your endgame?"
    "Try as you might, you can't get the women in your life out of your brain. Maybe... all the money... the company... is really all about?"
    "Having the women in your life serve your needs, physically, emotionally, sexually..."
    $ mc.change_locked_clarity(30)
    "Maybe it is time to just embrace it. There's nothing wrong with that, right? Any guy in your position would do the same thing."
    "You open your eyes and look at [the_person.possessive_title]. You eyes are immediately drawn to her tits."
    the_person "That's it. Can you envision your goal, [the_person.mc_title]?"
    "You look down at [the_person.title]'s ample chest. You can imagine your cock sliding between them, her smooth flesh caressing you."
    $ the_person.change_obedience(3)
    mc.name "I can envision it... and I can almost feel it."
    "She gasps when she realizes you are staring right at her chest."
    #TODO increase her sluttiness with new sluttiness score.
    mc.name "[the_person.title]... would you follow me to someplace more private?"
    the_person "Oh my... I suppose..."
    "You quickly duck into a side hall and find a family restroom, she joins you inside and you lock the door."
    mc.name "Take your top off."
    "You don't give her a choice in the matter, but she quickly complies."
    $ the_person.strip_outfit(exclude_lower = True)
    mc.name "I want to feel my cock between your tits, and I'm not taking no for an answer."
    the_person "Then I suppose it's a good thing I don't want to say no!"
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] gets on her knees and puts her tits between her hands. She looks up into your eyes as your cock slowly slides between them."
    "Yeah, this feels amazing. You know in your head, this is exactly what your goals are. To have women serve you, fuck you, make you cum."
    "You can't wait to cum all over her incredible tits."
    call get_fucked(the_person, the_goal = "body shot", private= True, start_position = tit_fuck, skip_intro = True, allow_continue = False) from _call_get_fucked_life_coach_tit_fuck_01
    the_person "Oh my god... that was so hot..."
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.title] stands up, her tits coated in your cum."
    "It felt amazing, but something also felt different."
    "You made the decision to just let yourself go, enjoy the moment, and cover her tits in cum."
    "Normally you feel like you would find yourself wishing you could have cum inside her somewhere, but this time... it doesn't matter."
    "What matters was that she did it willingly, happy to serve you and your needs, however you told her to."
    "You decide that in the future, you'll be open to cumming all over a girl's fun bags whenever the mood strikes you."
    $ tits_man_perk_unlock()
    "You have unlocked the perk 'Tits Man'! You now have the same clarity multiplier for cumming on tits as you do for creampies!"
    the_person "I'm going to get cleaned up... you should probably slip out when you can..."
    mc.name "I'll do that. Thanks for the help, [the_person.title]."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You quietly exit the bathroom and go about your day."
    $ camilla.event_triggers_dict["obedience_titfuck"] = True
    $ camilla.add_unique_on_room_enter_event(camilla_obedience_ass_man)
    return

label camilla_obedience_ass_man_label(the_person):  #180 obedience
    $ the_person.story_event_log("obedience")
    "In this label, MC cums all over Camilla's ass after sex. Gains the Ass Man perk."
    # $ camilla.add_unique_on_room_enter_event(camilla_obedience_tit_fuck)
    return
