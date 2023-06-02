## Girlfriend Service crisis. If dating an employee, she approaches you and offers to hookup.
init 2 python:
    def girlfriend_service_requirement():
        if mc.business.is_open_for_business and mc.is_at_work:
            return any(x for x in mc.business.employee_list if x.has_role(girlfriend_role))
        return False

    def girlfriend_service_get_person():
        return get_random_from_list([x for x in mc.business.employee_list if x.has_role(girlfriend_role)])

    girlfriend_service = ActionMod("Girlfriend Service", girlfriend_service_requirement, "girlfriend_service_label",
        menu_tooltip = "WIP: Your girlfriend offers sex at work.", category = "Business",
        # initialization = init_action_mod_disabled,
        is_crisis = True)

label girlfriend_service_label():
    $ the_person = girlfriend_service_get_person()
    if the_person is None:
        return

    python:
        public_session = mc.location.person_count > 1
        # actually visit the MC
        old_location = None
        if not the_person.location == mc.location:
            old_location = the_person.location
            the_person.change_location(mc.location)

    "As you are getting your work done, your girlfriend, [the_person.title], comes up to you."
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title]. Have a sec?"
    mc.name "For you? Of course."
    #TODO harem content here eventually
    if the_person.get_opinion_score("public sex") > 0:
        the_person "There are so many girls here. Just wanted to make sure you aren't getting too tempted."
        "She starts to rub your crotch through your pants."
        $ mc.change_locked_clarity(10)
        the_person "I was thinking, I could take care of you... right here..."
        if public_session:
            "You glance around. Some of your employees are already starting to notice what is going on."
        else:
            "You glance around. You are the only two people around..."
        menu:
            "Service me" if mc.energy >= 50:
                the_person "Mmm, I knew you would say that. Anything sound good in particular?"
                menu:
                    "Anything":
                        the_person "Mmm, okay! Let's get started..."
                        call get_fucked(the_person, private = not public_session) from _girlfriend_service_initiate_07
                    "I want to cum on your face":
                        the_person "Mmm, sounds hot..."
                        call get_fucked(the_person, the_goal = "facial", start_position = blowjob, private = not public_session) from _girlfriend_service_initiate_08
                    "I want to cum in your mouth" if the_person.effective_sluttiness() > 40:
                        the_person "Mmm, sounds yummy..."
                        call get_fucked(the_person, the_goal = "oral creampie", start_position = deepthroat, private = not public_session) from _girlfriend_service_initiate_04
                    "I want to cum inside you" if the_person.effective_sluttiness() > 60:
                        the_person "Ohhh... that sounds so good..."
                        call get_fucked(the_person, the_goal = "vaginal creampie", start_position = standing_doggy, private = not public_session) from _girlfriend_service_initiate_05
                    "I want to cum in your ass" if the_person.effective_sluttiness() > 80:
                        the_person "Mmm, you are such a naughty boy..."
                        call get_fucked(the_person, the_goal = "anal creampie", start_position = anal_standing, private = not public_session) from _girlfriend_service_initiate_06
                mc.name "That was nice."
                "[the_person.possessive_title] slowly starts to clean herself up."
                the_person "Yeah... I'll have to do that again soon..."
            "Go somewhere private" if public_session and mc.energy > 50:
                $ public_session = False
                mc.name "Sounds good to me, but we should find somewhere private."
                the_person "Why?"
                mc.name "I don't want other employees to think I'm favoring you... just because you're my girlfriend."
                "She gives you some pouty lips for a moment, but soon relents."
                "You grab [the_person.title]'s hand and lead her to an empty storage room and lock the door behind you."
                mc.name "Now... what exactly did you have in mind?"
                "[the_person.possessive_title] smiles and moves toward you."
                call get_fucked(the_person, private = not public_session) from _girlfriend_service_initiate_079
                $ the_person.change_stats(happiness = 5)
            "Too tired" if mc.energy < 50:
                mc.name "I'm sorry. It's been a long day and I'm just too tired right now. But I think I would like to do this another time..."
                "She seems a little disappointed, but understanding."
                the_person "Okay... another time then..."
                "Rejected, she turns around and walks away, going back to her work."
            "Too busy" if mc.energy >= 50:
                mc.name "I'm sorry, I have too much work to get done right now."
                "She gets flustered."
                $ the_person.draw_person(emotion = "angry")
                the_person "Wow, no time for me? Really? Your girlfriend?"
                $ the_person.change_stats(love = -5, happiness = -5)
                if the_person.is_dominant: #She takes over anyway.
                    "You argue for a bit. Suddenly, she snaps."
                    the_person "You know what? I don't care if you're busy. I have needs and you need to meet them."
                    "She steps towards you aggressively."
                    call get_fucked(the_person, the_goal = "hate fuck", private = not public_session) from _girlfriend_service_initiate_hate_fuck_01
                    "Finished, she seems to have cooled off some."
                    the_person "We'll talk about this more another time..."
                    "She cleans up a bit, and then gets back to work."
                else:
                    "Rejected, she turns around and walks away, going back to her work."
    else:
        "She lowers her voice a bit."
        the_person "I was trying to get some work done, but I couldn't stop thinking about your cock."
        if public_session:
            the_person "I was wondering if you wanted to find somewhere private and let me play with it..."
        else:
            the_person "I was wondering if you would let me play with it..."

        menu:
            "Get her alone" if public_session and mc.energy >= 50:
                $ public_session = False
                mc.name "I like the way you are thinking, follow me."
                "You grab [the_person.title]'s hand and lead her to an empty storage room and lock the door behind you."
                mc.name "Now... what exactly did you have in mind?"
                "[the_person.possessive_title] smiles and moves toward you."
                call get_fucked(the_person, private = not public_session) from _girlfriend_service_initiate_03
                $ the_person.change_stats (happiness = 5)
            "Service me here" if mc.energy >= 50:
                if not public_session:
                    if mc.location != ceo_office:
                        "Looking around, [the_person.title] realizes you two are the only two people around."
                    the_person "Okay, let's do it right here!"
                    "[the_person.possessive_title] moves toward you."
                    call get_fucked(the_person, private = not public_session) from _girlfriend_service_initiate_01
                    $ the_person.change_stats (happiness = 5)
                else:
                    "She looks around at the other girls in the room."
                    if the_person.get_opinion_score("public sex") == -2:
                        the_person "But... there's people around?"
                        mc.name "So?"
                        the_person "I couldn't... you can't possibly think that I'd..."
                        mc.name "Why not? It isn't like our relationship is secret. Besides, who are they going to complain to? I'm the boss, remember?"
                        "You put your hand on her chin, she looks up at you."
                        mc.name "A fact that you would be wise to remember."
                        $ the_person.change_stats (obedience = 5, happiness = -5, love = -3)
                        "She clearly isn't happy, but appears to accept your request."
                    elif the_person.effective_sluttiness() > 80 or (the_person.get_opinion_score("public sex") == 0 and the_person.effective_sluttiness() > 40):
                        the_person "Oh my god... right here in front of everyone? That is so hot... Let's do it!"
                    else:
                        the_person "I don't know... I think the other employees are gonna notice..."
                        mc.name "So? It's not like our relationship is a secret. Besides, who are they going to complain to? I'm the boss remember?"
                        the_person "Okay, If you're sure about it."
                    "[the_person.possessive_title] moves toward you."
                    call get_fucked(the_person, private = not public_session) from _girlfriend_service_initiate_02
                    $ the_person.change_stats (obedience = 5)
            "Too tired" if mc.energy < 50:
                mc.name "I'm sorry. It's been a long day and I'm just too tired right now. But I think I would like to do this another time..."
                "She seems a little disappointed, but understanding."
                the_person "Okay... another time then..."
                "Rejected, she turns around and walks away, going back to her work."
            "Not right now":
                mc.name "I'm sorry, but I'm very busy with work. I'll try and find you later though."
                $ the_person.change_stats (happiness = -5, obedience = 2)
                the_person "Ah, right, of course..."
                "You can tell she is a little saddened, but she backs off and goes back to her work."

    if public_session:
        "As you put your cock back in your pants, the activity in the room returns to normal."
        "Your girlfriend has a smile on her face as she finishes cleaning up."
        $ the_person.change_happiness(5)

    python:
        clear_scene()
        the_person.apply_planned_outfit()
        public_session = None
        if old_location:
            the_person.change_location(old_location)
            old_location = None
        mc.location.show_background()
    return
