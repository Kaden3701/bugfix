init -1 python:
    def sarah_bar_date_requirement(the_day):
        if time_of_day == 3 and day%7 == the_day:  #Saturday
            return True
        return False

    def sarah_bar_date_ask_requirement(the_person):
        if not sarah_get_sex_unlocked():
            return False
        love_requirement = 30
        if sarah.love < love_requirement:
            return "Requires: " + str(love_requirement) + " Love"
        elif mc.business.event_triggers_dict.get("sat_date_scheduled", False):
            return "Already planned Saturday date!"
        return True

    sarah_bar_date_ask_action = Action("Ask her out to the bar", sarah_bar_date_ask_requirement, "sarah_bar_date_ask_label",
        menu_tooltip = "Plan a more serious date to the bar. Feed her a few drinks and see what happens!")

label sarah_bar_date_ask_label(the_person):
    mc.name "Hey, I was just thinking. Want to grab some drinks on Saturday night?"
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.get_opinion_score("cheating on men") > 0:
            the_person "Oh, that sounds like a lot of fun!"
            "She gives you a playful smile."
            the_person "Just don't tell my [so_title], okay? He might not like me going to a bar with a hot guy like you."
            mc.name "My lips are sealed."
            if the_person.effective_sluttiness() > 60:
                the_person "Treat me right and mine might not be. He's normally out late playing poker with the boys on Saturday. How does that sound?"
            else:
                the_person "He's normally out late playing poker with the boys on Saturday. How does that sound for you?"

        else:
            the_person "Oh, Drinks would be so much fun..."
            mc.name "Is there something wrong?"
            the_person "No, I just don't know what my [so_title] would think. He might be a little jealous of you, you know?"
            mc.name "You don't have to tell him that I'll be there, if you don't want to. There's no reason you couldn't go out by yourself or with the 'girls'"
            "She thinks about it for a moment, then nods and smiles."
            the_person "You're right, of course. He's normally out playing poker with the boys anyway."
    else:
        the_person "That sounds great! I'd love to go out for a few drinks with you [the_person.mc_title]!"
    mc.name "Sounds good. We'll get together on Saturday night."

    python:
        # it happens on a saturday
        mc.business.mandatory_crises_list.append(Action("Bar date", sarah_bar_date_requirement, "sarah_bar_date_label", args=the_person, requirement_args=5))
        mc.business.event_triggers_dict["sat_date_scheduled"] = True

    return "Advance Time"

label sarah_bar_date_label(the_person):
    $ mc.business.event_triggers_dict["sat_date_scheduled"] = False
    $ the_person.planned_outfit = get_sarah_date_outfit_two()
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ scene_manager = Scene()

    if mc.is_at_work:
        "Lost in thought as you get your work done in the silence of the weekend, a sudden voice startles you."
        the_person "[the_person.mc_title]! Working away your weekend again I see!"
        "You look up to see the now familiar face of [the_person.title] standing in the doorway."
        $ scene_manager.add_actor(the_person, emotion = "happy")
        "You had a date planned for tonight, but it looks like she knew you'd be here and decided to surprise you."
        the_person "You work too much! Let's go have some fun!"
        "You have been working quite a bit lately, it would be good to have a chance to blow off some steam."
        menu:
            "Let's Go":
                the_person "Yes! You won't regret this. Let's go!"
                "You finish up what you are working on and grab your stuff. You make sure to lock up the business on your way out with [the_person.possessive_title]."
                "As you exit the building, you consider where you should head for the night."
                menu:
                    "The Bar":
                        mc.name "What do you say we head to the bar and have a few drinks? Maybe play some darts?"
                        the_person "Oh! That sounds great!"
                        call Sarah_weekend_date_grab_drinks_label from _sarah_bar_date_01

                    # "Strip Club" if sarah.event_triggers_dict.get("stripclub_progress", 0) >= 1 and not strip_club_is_closed():
                    #     mc.name "In the mood for a titty bar?"
                    #     the_person "Oh! That sounds like a good evening!"
                    #     call Sarah_weekend_date_strip_club_label from sarah_weekend_date_crisis_02

                    "Your Place" if sarah_get_sex_unlocked():
                        the_person "Oh! A direct approach? Not even going to bother getting me boozed up?"
                        mc.name "Nah. The sex is better when you are sober anyway."
                        the_person "Ha! Okay, lead the way then stud!"
                        "A short walk later, and you are walking through your front door."
                        call Sarah_date_ends_at_your_place_label(the_person) from _sarah_date_happy_ending_03

            "Not Today":
                the_person "Seriously? You're going to turn me down?"
                mc.name "I'm sorry, there is a lot I want to get done around here."
                if sarah.sluttiness > 70:
                    the_person "You know, it is so sexy how much work you put into this place."
                    mc.name "Is that so?"
                    $ scene_manager.update_actor(the_person, position = "kneeling1")
                    "She slowly climbs up onto your desk and begins to touch herself."
                    the_person "I know you have a lot to do. Feel free to watch... or blow a little steam off with me!"
                    mc.name "Right! I'm sure a short diversion wouldn't delay me too much."
                    "She walks right up to you and starts to get down on her knees. You pull your cock out, which is now fully erect."
                    $ mc.change_locked_clarity(30)
                    $ scene_manager.update_actor(the_person, position = "blowjob")
                    the_person "That's it. Let me just take care of this for you..."
                    #call fuck_person(the_person, start_position = deepthroat, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_sex_description_sarah_weekend_deepthroat_1
                    call get_fucked(the_person, the_goal = "oral creampie", private= True, start_position = deepthroat, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_sarah_weekend_deepthroat_5
                    "[the_person.possessive_title] moans while licking the last drops from her lips."
                    the_person "You taste so good, just call me when you need to blow off some more steam..."
                    "You clear your throat and then respond."
                    mc.name "That was great, thank you!"
                    $ scene_manager.update_actor(the_person, position = "stand4")
                    the_person "Alright, I know you wanted to get other things done, so I'll let you get back to it. But don't work too hard!"
                    "She quickly cleans herself up then leaves, giving you a chance to continue your work, but now with your balls empty."
                elif sarah_epic_tits_progress() > 1:
                    the_person "I got an idea. Why don't you let me help you, you know, relieve a little tension?"
                    mc.name "I'm not honestly that tense right now..."
                    if the_person.tits_available:
                        "[the_person.title] begins to grope her own tits and play with her nipples."
                    else:
                        "Without prompting, [the_person.title] starts to remove her top..."
                        $ scene_manager.strip_to_tits(person = the_person)
                    the_person "Are you sure? My big tits don't make you tense... at all?"
                    "You have to admit it, seeing her epic tits gets you excited. You can feel an erection starting."
                    the_person "Hmmm. Earth to [the_person.mc_title]?"
                    mc.name "Right! I'm sure a short diversion wouldn't delay me too much."
                    the_person "Mmm, ever since I took those serums, I've been craving your cock between my tits..."
                    $ mc.change_locked_clarity(30)
                    the_person "Let me just take care of this for you..."
                    call mc_sex_request(the_person, the_request = "titfuck") from _call_mc_sex_request_sarah_weekend_titfuck_5
                    "[the_person.possessive_title] moans as she rubs your cum into her chest."
                    the_person "It feels so sticky on my skin... Mmmm, that was nice."
                    "You clear your throat and then respond."
                    mc.name "That felt great!"
                    $ scene_manager.update_actor(the_person, position = "stand4")
                    the_person "Alright, I know you wanted to get other things done, so I'll let you get back to it. But don't work too hard! Look me up if you need another break sometime!"
                    "She quickly cleans herself up then leaves, giving you a chance to continue your work, but now with your balls empty."
                else:
                    $ the_person.change_stats(happiness = -10, love = -5, obedience = 5)
                    the_person "Wow, okay. Sorry, I didn't realize you were so busy. Maybe next time I guess?"
                    "[the_person.title] quickly turns and walks out, leaving you to your work."
                    $ scene_manager.remove_actor(the_person)
    else:
        "You have a date planned with [the_person.title] right now."

        menu:
            "Get ready for the date {image=gui/heart/Time_Advance.png}":
                pass

            "Cancel the date (tooltip)She won't be happy with you canceling last minute":
                $ mc.start_text_convo(the_person)
                mc.name "I'm sorry, but something important came up at the last minute. We'll have to reschedule."
                $ the_person.change_stats(happiness = -5, love = -5)
                the_person "I hope everything is okay. Maybe we can do this some other time then."
                $ mc.end_text_convo()
                return

        if mom_date_intercept_requirement(mom, the_person) and renpy.random.randint(0,100) < (mom.love):
            call mom_date_intercept(mom, the_person) from _call_mom_date_intercept_sarah_01
            if _return:
                $ clear_scene()
                $ scene_manager.clear_scene()
                return "Advance Time"
        "You get ready and head towards the bar. When you are almost there, you see a familiar face."
        call Sarah_weekend_date_grab_drinks_label from sarah_weekend__bar_date_02

    $ scene_manager.clear_scene()
    return _return
