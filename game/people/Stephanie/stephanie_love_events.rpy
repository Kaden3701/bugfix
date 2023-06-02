



init 2 python:
    def stephanie_tennis_intro_requirement():
        if day%7 == 5 and time_of_day == 0 and mc.is_at_work:
            if stephanie.love >= 20 and stephanie.story_event_ready("love"):
                return True
        return False

# Event addition declarations.
    def add_stephanie_tennis_intro_action():
        stephanie_tennis_intro_action = Action("Stephanie Still Plays Tennis", stephanie_tennis_intro_requirement, "stephanie_tennis_intro_label")
        mc.business.add_mandatory_crisis(stephanie_tennis_intro_action)
        return

init 5 python:
    def stephanie_get_tennis_outfit(full_outfit = True):
        outfit = Outfit("Stephanie Tennis Outfit")
        outfit.add_upper(sports_bra.get_copy(), [.56, .1, .06, 1.00])
        outfit.add_upper(tanktop.get_copy(), [1.0, 1.0, 1.0, .85])
        outfit.add_lower(cotton_panties.get_copy(), [.56, .1, .06, 1.00])
        outfit.add_lower(skirt.get_copy(), [.94, .94, 1.0, .95])
        outfit.add_feet(sneakers.get_copy(), [1.0, .81, 1.0, 1.0], "Pattern_1", [1.0, 1.0, 1.0, 1.0])
        outfit.add_feet(short_socks.get_copy(), [1.0, 1.0, 1.0, 1.0])
        return outfit

    def stephanie_gym_outfit():
        stephanie.apply_outfit(stephanie_get_tennis_outfit())
        return


label stephanie_tennis_intro_label():
    $ the_person = stephanie
    $ steph_tennis_outfit = stephanie_get_tennis_outfit(full_outfit = True)
    $ steph_tennis_outfit.remove_random_lower(top_layer_first = True)   #She is missing the skirt.
    $ the_person.apply_outfit(steph_tennis_outfit)
    "It is an early Saturday morning at your new business. You set yourself to working on some administrative tasks."
    "However, as you begin your work, you hear a few doors open and close. You get up and investigate."
    $ the_person.draw_person(position = "standing_doggy")
    "As you round a corner, you are greeted by a wonderful sight. [the_person.possessive_title]'s ass, covered only by panties."
    $ mc.change_locked_clarity(20)
    "You are so surprised, you don't get the chance to get a good look before blurting something out."
    mc.name "Ah... [the_person.title]?"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly stands up and turns to you, surprised. She blushes a bit, but doesn't bother trying to cover up anything."
    the_person "[the_person.mc_title]! I didn't realize you were working weekends."
    mc.name "I guess I could say the same thing?"
    the_person "Ah, I'm not working. I leave a set of spare clothes here during the week, just in case I make a mess doing research and need to change."
    the_person "I couldn't find my tennis skirt at home, I thought maybe I left it here..."
    $ the_person.draw_person(position = "standing_doggy")
    $ mc.change_locked_clarity(20)
    "She turns around and resumes rummaging through the desk..."
    $ mc.change_arousal(20)
    "Damn... maybe you should give that ass of hers a little swat..."
    $ the_person.draw_person(position = "standing_doggy", display_transform = character_right(zoom = 1.2))
    "You quietly start to move up behind her, when suddenly she stands up and turns around."
    $ the_person.draw_person(position = the_person.idle_pose, display_transform = character_right(zoom = 1.2))
    the_person "Ah! Found them!"
    $ steph_tennis_outfit = stephanie_get_tennis_outfit(full_outfit = True)
    $ the_person.apply_outfit(steph_tennis_outfit)
    $ the_person.draw_person(position = the_person.idle_pose, display_transform = character_right(zoom = 1.2))
    "She slides her skirt up and over her hips. Damn, maybe you can cop a feel of that backside another time."
    $ received_handjob = False
    if the_person.is_willing(handjob):  #She notices MC is turned on, offers to help out.
        "[the_person.possessive_title] notices the bulge in your pants when she turns to you."
        "She rolls her eyes, but also gives you a slight smile."
        the_person "Sorry, I didn't mean to get you all worked up. I didn't even know you were here, to be honest."
        mc.name "It's okay."
        "She bites her lip, clearly thinking something over."
        the_person "You know... I'm pretty sure it is just us here. I could give you a hand with that, if you want."
        mc.name "Oh?"
        "You quickly decide."
        menu:
            "Accept Handjob":
                $ received_handjob = True
                mc.name "What can I say, that ass of yours really gets me going. I would appreciate it."
                the_person "Ah, that isn't the first time I've heard that!"
                "[the_person.possessive_title] moves closer to you."
            "Decline Handjob":
                mc.name "I really appreciate it, but I need to be working on other things right now."
                the_person "Really? Alright..."
                $ the_person.change_stats(happiness = -2, obedience = 2)
    else:
        "Your erection is almost painful, though [the_person.possessive_title] seems almost oblivious."
        "You think about it... maybe you should ask her for a little relief?"
        menu:
            "Ask for Handjob":

                mc.name "Damn, I have to say, that ass of yours really gets me going."
                the_person "Ah, that isn't the first time I've heard that!"
                mc.name "I'm not going to get pushy about it, but umm, would you be willing to give me a quick hand with it?"
                mc.name "You don't have to do anything crazy, but it would be helpful for me to be able to get back to work and concentrate."
                $ the_person.add_situational_slut("embarrassed", 20, "Embarassed from being caught in her panties.")
                the_person "Oh! I... wow..."
                "She looks up at you and bites her lip, thinking about it."
                if the_person.allow_position(handjob):
                    the_person "You know what? Why not. It is just the two of us here... not like anyone is going to walk in on us!"
                    $ the_person.change_stats(happiness = 2, obedience = 2)
                    "[the_person.possessive_title] moves closer to you."
                    $ received_handjob = True
                else:
                    the_person "Sorry... I don't think I can do that..."
                    "There is a moment of awkward silence."
                    $ the_person.change_stats(happiness = -2, obedience = -2)
            "Let the Moment Pass":
                "It takes a moment, but you manage to will your hormones down, atleast long enough to finish the conversation."
    if received_handjob:
        call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = False, allow_continue = False) from _steph_tennis_handjob_01
        $ the_report = _return
        if the_report.get("guy orgasms",0) > 0:
            "You take a few moments to recover from your orgasm."
        "[the_person.title] takes a few moments to clean herself up and straighten her outfit."
        $ steph_tennis_outfit = stephanie_get_tennis_outfit(full_outfit = True)
        $ the_person.apply_outfit(steph_tennis_outfit)
        $ the_person.draw_person(position = the_person.idle_pose)
    $ the_person.clear_situational_slut("embarrassed")
    mc.name "So... you said you need the skirt for tennis?"
    the_person "Yeah, I'm trying to get back into it. It has been a while, but I found a place that I can practice over by the fitness center."
    mc.name "I remember when we used to play once in a while."
    the_person "Yeah... hey if you ever want to come out, I'm sure I could use the practice!"
    the_person "It is out by the gym. It is kind of run down, not nearly as nice as the one we used to play at in university, but it is servicable."
    mc.name "I'll keep that in mind."
    the_person "Great! See ya!"
    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.possessive_title] as she walks away."
    "You used to play with her once in a while on weekends... Maybe you should start doing that again?"
    "It might be a good chance to get in shape, and spending time with [the_person.title] always tends to be pleasant."
    "You can now find her at the gym on Saturday mornings."
    $ the_person.set_schedule(gym, the_days = [5], the_times = [1])
    $ stephanie.love_step = 1
    $ stephanie.apply_gym_outfit = stephanie_gym_outfit
    return
