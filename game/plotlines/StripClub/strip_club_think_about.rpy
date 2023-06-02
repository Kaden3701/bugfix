## Stripclub storyline Mod by Corrado
# You think about buying the stripclub.

init 2 python:
    def think_about_buying_strip_club_requirement():
        if get_strip_club_foreclosed_stage() == 2:
            if day > get_strip_club_foreclosed_last_action_day() + 2 and time_of_day >= 3:
                return True
        return False

    def strip_club_bought_by_someone_else():
        strip_club_owner = Person.get_random_male_name()
        strip_club.background_image = Image(get_file_handle("Club_Background.png")) # Set up the original background
        strip_club.formal_name = strip_club_owner + "'s Gentlemen's Club"
        strip_club.add_action(strip_club_show_action) # Restore 'Watch a show' button
        for person in [x for x in stripclub_strippers if x not in unique_character_list]: # rehire strippers
            person.set_override_schedule(None, the_days=[0,1,2,3,4,5,6], the_times=[3,4])
        set_strip_club_foreclosed_stage(-1) # end story line
        starbuck.remove_on_talk_event("talk_again_buying_club_starbuck_label")
        return

    def strip_club_buy_days_left():
        return (19 + mc.business.event_triggers_dict.get("strip_club_decision_day", 0) - day)

    def discuss_buying_club_with_starbuck_requirement(person):
        if get_strip_club_foreclosed_stage() == 3 and mc.business.has_funds(60000):
            if day > get_strip_club_foreclosed_last_action_day() and time_of_day > 0:
                return True
        return False

    def strip_club_offer_expire_requirement():
        if strip_club_buy_days_left() % 5 == 0 and time_of_day == 1: # only show once per day
            return True
        if strip_club_buy_days_left() <= 0: # the event will be removed with this trigger
            return True
        return False

    def cousin_meet_at_strip_club_requirement(the_person, target_day):
        if time_of_day == 3 and day >= target_day:
            return True
        return False

    def add_strip_club_offer_expire_action():
        strip_club_offer_expire_action = Action("Strip club offer is expiring", strip_club_offer_expire_requirement, "strip_club_offer_expire_label")
        mc.business.add_mandatory_crisis(strip_club_offer_expire_action)

    def add_cousin_meet_at_strip_club():
        cousin_meet_at_strip_club_action = Action("Meet cousin at strip club", cousin_meet_at_strip_club_requirement, "strip_club_bought_strippers_selection_label", requirement_args = day + 1)
        cousin.set_override_schedule(strip_club, the_times = [3]) # set alternative schedule
        cousin.add_unique_on_room_enter_event(cousin_meet_at_strip_club_action)

    def add_think_about_buying_strip_club_action():
        think_about_buying_strip_club_action = Action("Think About Buying The Club", think_about_buying_strip_club_requirement, "think_about_buying_strip_club_label", args = starbuck)
        mc.business.add_mandatory_crisis(think_about_buying_strip_club_action)

    def add_discuss_buying_club_with_starbuck_action():
        discuss_buying_club_with_starbuck_action = Action("Buy the Stripclub", discuss_buying_club_with_starbuck_requirement, "discuss_buying_club_with_starbuck_label")
        starbuck.add_unique_on_talk_event(discuss_buying_club_with_starbuck_action)

    def add_talk_again_buying_club_starbuck_action():
        talk_again_buying_club_starbuck_action = Action("Buy the Stripclub", discuss_buying_club_with_starbuck_requirement, "talk_again_buying_club_starbuck_label")
        starbuck.add_unique_on_talk_event(talk_again_buying_club_starbuck_action)

label strip_club_offer_expire_label(): # Event trigger with timer
    if strip_club_buy_days_left() <= 0:
        $ strip_club_bought_by_someone_else()
        return

    "You're absorbed in your thoughts when suddenly you remember that you still need to decide if you want to buy the strip club or not..."
    if strip_club_buy_days_left() > 1:
        $ ran_num = strip_club_buy_days_left()
        "You still have [ran_num] days to make your final decision, you need to see [starbuck.title] if you change my mind."
    else:
        "This is the last day to make your decision. You need to see [starbuck.title] if you want to buy it."

    $ add_strip_club_offer_expire_action()
    return


label starbuck_talk_about_strip_club_label(the_person): # On_enter event
    $ the_person.draw_person(emotion = "happy")
    the_person "[the_person.mc_title], nice to see you! You have no idea what just happened five minutes ago!"
    the_person "I got a phone call from the bank. Looks like some strip club has been foreclosed for some unpaid taxes, and they asked me if I was interested in buying it!"
    the_person "They called ME because I had some kind of 'business affinity' they said!"
    mc.name "Funny! Yeah, those pencil pushers may know about money, but they know nothing about business."
    the_person "Anyway, they know my financial situation, so if I wanted to buy it, I just have to take out another mortgage on my house."
    mc.name "Right, the business here isn't bad and it could turn out to be a good investment, but you should consider it carefully."
    $ the_person.draw_person(emotion = "sad")
    the_person "[the_person.mc_title], you know I opened this shop because it was my husband's and my dream, to help people be more adventurous and have fun in the bedroom..."
    the_person "When he died I decided to chase our dream, but a strip club is something completely different."
    the_person "Look here [the_person.mc_title], they sent me all the required documents by email..."
    $ the_person.draw_person(emotion = "happy")
    the_person "YOU should be the one buying it! You're young and full of energy, and the place's environment could be very 'stimulating'!"
    mc.name "Actually [the_person.title], my company already gives me enough troubles and requires all my attention, I don't think..."
    the_person "Yeah, yeah, I get you. Anyway, I'll forward you the email with the papers I got from the bank. Promise me that you'll think about it, okay?"
    mc.name "I suppose it isn't worth arguing with you. I'll have my accountant take a look at them."
    "After a few second your phone notifies you that you got an email from [the_person.title]."
    $ set_strip_club_foreclosed_stage(2)
    $ add_think_about_buying_strip_club_action()
    return

label think_about_buying_strip_club_label(the_person):
    $ name_string = mc.business.event_triggers_dict.get("old_strip_club_name", "Strip Club")
    "As you are wandering downtown with your mind full of thoughts, you find yourself in front of the old [name_string]..."
    $ mc.change_location(strip_club)
    "It's so strange to see the club this way, no people around, no music..."
    "You've checked the documents [the_person.title] got from the bank and your accountant confirmed it is a solid investment."
    "When you decided to invest in [the_person.title]'s shop, you never imagined it could be so profitable."
    "Besides the economic returns, you built up a very nice relationship with [the_person.title]."
    "Buying this place could be a really good investment, not to mention the 'side bonuses' you could get as the club's owner."
    mc.name "$50,000 is a lot of money, but I guess it will be worth the effort... the benefits are really tempting..."
    mc.name "Okay, maybe I can invest my money in it, but running a place like this for sure will require a lot of time and effort..."
    mc.name "Perhaps I should find some kind of manager, but it needs to be someone I could trust..."
    mc.name "I need to think some more about buying this place, but I admit I'm very tempted... I need to talk again with [the_person.title]."
    "You're close to a decision about the Club, but now it's time to return back home and have a nice restoring sleep."
    $ mc.change_location(bedroom)
    $ set_strip_club_foreclosed_stage(3)
    $ add_discuss_buying_club_with_starbuck_action()
    return

label discuss_buying_club_with_starbuck_label(the_person): # The event trigger with an action button
    $ mc.business.event_triggers_dict["strip_club_decision_day"] = day
    $ the_person.draw_person(emotion = "happy", position = "stand4")
    mc.name "Hi [the_person.title]! I think I'm going to buy the strip club as you suggested, can you call your contact at the bank?"
    the_person "Really [the_person.mc_title]? Wow, I'm so exited and happy for you! Sure, let's call him immediately."
    "[the_person.title] takes out her phone, a minute later she is talking with a bank employee and after a few minutes the call ends."
    the_person "Everything's set up [the_person.mc_title]! They await your money transfer, after that they'll prepare all the documents for your signature."
    menu:
        "Buy the club\n{color=#ff0000}{size=18}Costs: $50,000{/size}{/color}" if mc.business.has_funds(50000):
            "You make a call and set up the money transfer from your company's account."
            $ mc.business.change_funds(-50000)
            the_person "Congratulations [the_person.mc_title]! You're now the proud owner of a Strip Club... and you already have one loyal customer, business partner."
            call starbuck_celebration_strip_event(the_person) from _call_starbuck_celebration_strip_event_1
            call starbuck_name_the_new_club_label(the_person) from _call_starbuck_name_the_new_club_label_1
        "Buy the club\n{color=#ff0000}{size=18}Requires: $50,000{/size}{/color} (disabled)" if not mc.business.has_funds(50000):
            pass
        "Change your mind":
            mc.name "Actually $50,000 is a lot of money, perhaps it's better to a few days so I can think it over..."
            $ the_person.draw_person(position = "stand4")
            the_person "I totally understand, [the_person.mc_title]... I think you should take your time."
            #TODO Add offer end
            $ ran_num = strip_club_buy_days_left()
            the_person "The bank said you have [ran_num] days left to decide, come see me again in a few days, if you've changed your mind."
            $ set_strip_club_foreclosed_stage(3) # stay at stage 3 with updated last action day
            $ add_talk_again_buying_club_starbuck_action()
            $ add_strip_club_offer_expire_action()

    $ clear_scene()
    return

label talk_again_buying_club_starbuck_label(the_person):
    $ the_person.draw_person(emotion = "happy", position = "stand3")
    the_person "Hey [the_person.mc_title], did you change your mind about buying the strip club?"
    mc.name "Hi [the_person.title], I've had some time to think about it."
    menu:
        "Buy the club\n{color=#ff0000}{size=18}Costs: $50,000{/size}{/color}" if mc.business.has_funds(50000):
            "You make a call and set up the money transfer from your company's account."
            $ set_strip_club_foreclosed_stage(4)
            $ mc.business.change_funds(-50000)
            the_person "Congratulations [the_person.mc_title]! You're now the proud owner of a Strip Club... and you already have one loyal customer, business partner."
            call starbuck_celebration_strip_event(the_person) from _call_starbuck_celebration_strip_event_2
            call starbuck_name_the_new_club_label(the_person) from _call_starbuck_name_the_new_club_label_2
        "Buy the club\n{color=#ff0000}{size=18}Requires: $50,000{/size}{/color} (disabled)" if not mc.business.has_funds(50000):
            pass
        "Need more time":
            mc.name "But I'm still not sure, I'm going to think about it a little while longer."
            the_person "Come see me again in a few days when you have made your decision."
            $ set_strip_club_foreclosed_stage(3) # stay at stage 3 with updated last action day
            $ add_talk_again_buying_club_starbuck_action()

    $ clear_scene()
    return

label starbuck_celebration_strip_event(the_person):
    "[the_person.title] comes closer to you..."
    $ the_person.draw_person(emotion = "happy", position = "stand2")
    the_person "Maybe I can show you my skills as 'exotic dancer' too... What do you think?"
    menu:
        "Accept":
            mc.name "You know I can't say no to such an offer."
            $ the_person.draw_person(emotion = "happy", position = "back_peek")
            the_person "Okay, [the_person.mc_title], follow me to the backroom..."
            $ the_person.draw_person(position = "walking_away")
            $ count = mc.location.person_count - 1
            "[the_person.title] starts to move towards the backroom..."
            menu:
                "Follow her\n{size=22}No interruptions{/size}":
                    "You follow [the_person.title] into the backroom, she sets up her phone to play some sexy music in the background."
                    $ the_person.draw_person(emotion = "happy", position = "back_peek")
                    the_person "Are you ready to fill my panties with cash?"
                    "You pull out some cash and wave it at her with a smile."
                "Stop her\n{size=22}[count] people watching{/size}":
                    mc.name "Generally, strippers perform onstage for a crowd... Don't tell me you're shy?"
                    $ the_person.draw_person(emotion = "happy", position = "back_peek")
                    "[the_person.possessive_title] gets what you mean and accepts your challenge."
                    if count > 0:
                        the_person "Okay, I don't care if my customers see me strip, let them enjoy the show."
                    else:
                        the_person "Okay, I don't care if someone enters the shop in the next few minutes, let them enjoy the show."
                    python:
                        the_person.change_arousal(4 * the_person.get_opinion_score(["showing her ass", "showing her tits", "being submissive"]))
                        the_person.change_love(the_person.get_opinion_score(["showing her ass", "showing her tits", "being submissive"]))
                        the_person.change_slut(2 *(the_person.get_opinion_score(["showing her ass", "showing her tits", "being submissive"])))
                        should_be_private = False
                    "[the_person.title] climbs up on the shop counter using it as a walkway to perform her sexy dance."
            $ the_person.draw_person(emotion = "happy", position = "back_peek")
            "[the_person.title] starts to dance to the music, swinging her hips and turning slowly to show herself off all around."
            $ the_person.draw_person(emotion = "happy", position = "stand5")
            "Slowly she starts to unbutton a bit and show some cleavage, you are amazed by her round [the_person.tits]-cup boobs."
            $ strip_list = the_person.outfit.get_tit_strip_list(visible_enough = True)
            $ ran_num = 0
            while ran_num < len(strip_list):
                $ the_item = strip_list[ran_num]
                menu:
                    "Throw some cash\n{color=#ff0000}{size=18}Costs: $20{/size}{/color}":
                        $ mc.business.change_funds(-20)
                        "You throw $20 on the counter, [the_person.title] is definitely intrigued by your game."
                        $ the_person.change_slut(2 * the_person.get_opinion_score("showing her tits"))
                    "Go on":
                        $ the_person.change_slut(1 * the_person.get_opinion_score("showing her tits"))

                $ the_person.draw_animated_removal(the_item)
                if the_person.tits_visible:
                    "[the_person.title] takes off her [the_item.display_name] slowly, teasing you as she frees her tits."
                    if the_person.has_taboo("bare_tits"):
                        the_person "God, it's the first time I'm doing this, but you know what? I like it."
                        $ the_person.break_taboo("bare_tits")
                else:
                    "[the_person.title] takes off her [the_item.display_name]."
                $ ran_num += 1

            $ the_person.draw_person(emotion = "happy", position = "stand4")
            $ strip_list = the_person.outfit.get_full_strip_list(strip_feet = False)
            $ ran_num = 0
            while ran_num < len(strip_list):
                $ the_item = strip_list[ran_num]
                menu:
                    "Throw some cash\n{color=#ff0000}{size=18}Costs: $20{/size}{/color}":
                        $ mc.business.change_funds(-20)
                        $ the_person.change_slut(2 * the_person.get_opinion_score("showing her ass"))
                    "Go ahead":
                        $ the_person.change_slut(1 * the_person.get_opinion_score("showing her ass"))

                $ the_person.draw_animated_removal(the_item)
                if the_person.vagina_visible:
                    "[the_person.possessive_title] peels off her [the_item.display_name], slowly revealing her cute pussy."
                    if the_person.has_taboo("bare_pussy"):
                        the_person "Am I really doing this? Am I, Yes, I am!"
                        "[the_person.title] takes a deep breath and continues to remove her clothes."
                        $ the_person.break_taboo("bare_pussy")
                else:
                    "[the_person.possessive_title] takes off her [the_item.display_name]."
                $ ran_num += 1

            $ the_person.draw_person(emotion = "happy", position = "stand3")
            "Now completely naked, [the_person.title] continues for a few minutes dancing seductively, knowing your eyes are glued to her body."
            $ the_person.draw_person(emotion = "happy", position = "back_peek")
            "Once she's done dancing, you get one last good look at her round, inviting ass."
            $ the_person.draw_person(emotion = "happy", position = "walking_away")
            "Without giving you another glance, she hops off the counter and puts her clothes back on."
            $ the_person.update_outfit_taboos()
            $ the_person.apply_outfit(the_person.planned_outfit)
            $ the_person.draw_person(emotion = "happy")
            $ the_item = None
        "Refuse":
            mc.name "Thank you [the_person.title], but right now I'm pretty busy. I'm sure you'll get your chance soon..."
            $ the_person.draw_person(emotion = "sad")
            "A bit disheartened, [the_person.title] nods."
    return

label starbuck_name_the_new_club_label(the_person):
    $ strip_club_owner = mc.name
    $ mc.business.remove_mandatory_crisis("strip_club_offer_expire_label") # remove expiry event
    the_person "Just a second, [the_person.mc_title]. What will you call your new strip club?"
    $ name_string = str(renpy.input("New Strip Club Name: ", strip_club_owner + "'s Gentlemen's Club"))
    $ strip_club.formal_name = name_string
    "The strip club name is now [name_string]. You pick up your phone and call [cousin.title]."
    mc.name "Hey [cousin.title], meet me tomorrow evening at the old Strip Club."
    cousin "What? Why?"
    mc.name "No questions now, just do it."
    cousin "Fine, I'll be there."
    $ add_cousin_meet_at_strip_club()
    $ set_strip_club_foreclosed_stage(4)
    return
