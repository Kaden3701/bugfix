### All the information and events related to the girlfriend role.

init -1 python:
    def ask_girlfriend_requirement(the_person):
        if the_person.has_role(girlfriend_role) or the_person.has_role(affair_role):
            return False
        elif the_person.has_role(sister_role) and the_person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False):
            return False
        elif the_person.has_role(mother_role) and the_person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False):
            return False
        elif the_person.love < 30:
            return False
        elif the_person.love < 60:
            return "Requires: 60 Love"
        return True #But note that there are still failure conditions in the actual event, but those lead to hints about what do to to stop it.

    def ask_break_up_requirement(the_person):
        return True

    def caught_cheating_requirement(the_person):
        return True

    def ask_get_boobjob_requirement(the_person):
        obedience_required = 130 - (the_person.get_opinion_score("showing her tits") * 5)
        if the_person.sluttiness < (40 - the_person.get_opinion_score("showing her tits") * 5):
            return False
        elif the_person.obedience < obedience_required:
            return "Requires: " + str(obedience_required) + " Obedience"
        elif the_person.event_triggers_dict.get("getting boobjob", False):
            return "Boobjob already scheduled"
        elif the_person.tits == Person.get_larger_tit(the_person.tits):
            return "At maximum size"
        return True

    def girlfriend_got_boobjob_requirement(start_day):
        if day < start_day:
            return False
        else:
            return True

    def girlfriend_ask_trim_pubes_requirement(the_person):
        obedience_required = 125 - (5*the_person.get_opinion_score("being submissive"))
        if the_person.sluttiness < 30:
            return False
        elif the_person.obedience < 110:
            return False
        elif the_person.obedience < obedience_required:
            return "Requires: " + str(obedience_required) + " Obedience"
        return True

    def girlfriend_do_trim_pubes_requirement(start_day):
        if day < start_day:
            return False
        return True

    def girlfriend_boob_brag_requirement(start_day):
        return True

    def add_girlfriend_got_boobjob_action(the_person):
        the_person.event_triggers_dict["getting boobjob"] = True #Reset the flag so you can ask her to get _another_ boobjob.
        got_boobjob_action = Action("Girlfriend Got Boobjob", girlfriend_got_boobjob_requirement, "girlfriend_got_boobjob_label", args = the_person, requirement_args = day + renpy.random.randint(3,6))
        mc.business.mandatory_crises_list.append(got_boobjob_action)
        return

    def add_girlfriend_brag_boobjob_action(the_person):
        girlfriend_boob_brag_action = Action("Girlfriend Boobjob Brag", girlfriend_boob_brag_requirement, "girlfriend_boob_brag_label")
        the_person.on_talk_event_list.append(girlfriend_boob_brag_action)
        return

    def girlfriend_build_pubes_choice_menu(the_person):
        valid_pubes_options = []
        for a_style in pube_styles:
            if a_style.name != the_person.pubes_style.name:
                valid_pubes_options.append([a_style.name, a_style])
        valid_pubes_options.append(["Never mind","Never mind"])
        return valid_pubes_options

    def add_girlfriend_do_trim_pubes_action(the_person, pubes_choice, time_needed):
        trim_pubes_action = Action("Girlfriend trim pubes", girlfriend_do_trim_pubes_requirement, "girlfriend_do_trim_pubes_label", args = [the_person, pubes_choice], requirement_args = [day + time_needed])
        mc.business.mandatory_crises_list.append(trim_pubes_action)
        the_person.event_triggers_dict["trimming_pubes"] = trim_pubes_action
        return

    def girlfriend_set_new_pubes(the_person, the_style):
        new_pubes = the_style.get_copy() #Copy the base style passed to us
        new_pubes.colour = the_person.pubes_style.colour #Modify the copy to match this person's details
        new_pubes.pattern = the_person.pubes_style.pattern #TODO: Make sure this makes sense for any future patterns we use.
        new_pubes.colour_pattern = the_person.pubes_style.colour_pattern
        the_person.pubes_style = new_pubes #And assign it to them.
        the_person.event_triggers_dict["trimming_pubes"] = None
        return

    def schedule_sleepover_available():
        return not mc.business.event_triggers_dict.get("girlfriend_sleepover_scheduled", False)

    def girlfriend_myplace_yourplace_requirement(the_person):
        if schedule_sleepover_available():
            if time_of_day < 4:
                return True
            else:
                return "Too Late"
        else:
            return "You already have a sleepover arranged"
        return False

    def girlfriend_sleepover_crisis_requirement():
        if time_of_day == 4:
            return True
        return False

    def girlfriend_wakeup_spooning_requirement(the_person):
        return True

    def girlfriend_underwear_shopping_requirement(the_person):
        if the_person.love < 80 and the_person.sluttiness < 40:
            return False
        if time_of_day == 0:
            return "Clothes store closed"
        elif time_of_day == 4: # Can be removed
            return "Clothes store closed"
        elif not mc.business.has_funds(500):
            return "Requires: $500"
        else:
            return True
        return False

    def girlfriend_quit_dikdok_requirement(the_person):
        if not the_person.has_role(dikdok_role):
            return False
        if the_person.love < 40: # hide option will love is very low
            return False
        if the_person.love < 60:
            return "Requires: 60 Love"
        return True


    def schedule_sleepover_in_story(person, your_place = True):
        mc.business.event_triggers_dict["girlfriend_person"] = person.identifier
        mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = True
        mc.business.event_triggers_dict["your_place"] = your_place

        girlfriend_sleepover_crisis = Action("Have a sleepover", girlfriend_sleepover_crisis_requirement, "girlfriend_sleepover_crisis_label")
        mc.business.add_mandatory_crisis(girlfriend_sleepover_crisis)
        return

    def get_random_girlfriend_morning_action(person):
        possible_action_list = []
        for wakeup_scene in girlfriend_morning_action_list:
            if wakeup_scene.is_action_enabled(person):
                wakeup_scene.args = [person]
                possible_action_list.append(wakeup_scene)
        return get_random_from_list(possible_action_list)

    # morning action
    girlfriend_wakeup_spooning = Action("Spooning wakeup", girlfriend_wakeup_spooning_requirement, "girlfriend_wakeup_spooning_label")

    # special list for girlfriend morning actions
    girlfriend_morning_action_list = []
    girlfriend_sleepover_interruption_list = []     #Ideas, daughter/mother walk in, phone call,
    girlfriend_roleplay_list = []                   #When a roleplay is created, add it here as an option. list of ACTIONS

    girlfriend_morning_action_list.append(girlfriend_wakeup_spooning)


label ask_break_up_label(the_person):
    # Stop being in a relationship.
    mc.name "[the_person.title], can we talk?"
    if the_person.happiness > 100:
        the_person "Sure, what's up?"
    else:
        the_person "Oh no, that's never good."

    mc.name "There's no easy way to say this, so I'll just say it: I think we should break up."
    $ the_person.draw_person(emotion = "sad")
    #TODO: Add a variant where you've passed below the girlfriend threshold and she feels the same way.

    $ the_person.change_happiness(-(the_person.love - 40)) #TODO: Double check this vs. the girlfriend love threshold.
    "She seems to be in shock for a long moment, before slowly nodding her head."
    the_person "Okay... I don't know what to say."
    $ the_person.change_love(-10)
    mc.name "I'm sorry, but it's just the way things are."
    $ the_person.remove_role(girlfriend_role)
    return

label ask_be_girlfriend_label(the_person):
    #Requires high love, if successful she becomes your girlfriend (which unlocks many other options). Requires high love and her not being in a relationship.
    #Hide this event at low love, show it when it at it's lowest love possibility and let it fail out for specific reasons (thus informing the player WHY it failed out).

    if the_person.has_role(sister_role): #She has specific dialogue
        call sister_girlfriend_intro(the_person) from _call_sister_girlfriend_intro

    elif the_person.has_role(mother_role):
        call mom_girlfriend_intro(the_person) from _call_mom_girlfriend_intro

    else: #General dialogue used for everyone.
        mc.name "[the_person.title], can I talk to you about something important?"
        the_person "Of course. What's on your mind."
        mc.name "I've been thinking about this for a while. I really like you and I hope you feel the same way about me."
        mc.name "I'd like to make our relationship official. What do you say?"


        if the_person.has_role(aunt_role):
            the_person "I... I don't know what to say [the_person.mc_title]. I love you like you were my own, but we could never have a real relationship together."
            the_person "Could you imagine what your mother would say about that, dating her sister? She would go crazy!"
            the_person "Come on, let's talk about something else."
            if the_person.event_triggers_dict.get("preg_your_kids_known",0) > 0 and persistent.pregnancy_pref > 0:
                "You turn to leave and she grabs you by the arm."
                the_person "Umm, wait a sec, you know what we have is not normal, but who cares right?"
                "She puts her arms around you and pulls you close."
                $ mc.change_locked_clarity(10)
                "She kisses you, and you kiss her back just as happily."
                $ the_person.add_role(girlfriend_role)
            else:
                the_person "Now if I was pregnant with your kiddo, I might have to reconsider this."

        elif the_person.has_role(cousin_role):
            the_person "You and me being, like, boyfriend and girlfriend? Ha, you must be crazy! Have you been huffing fumes at work?"
            the_person "I mean sure, I've come around on you and think you're not a total loser now, but we're cousins. Our parents would kill us."
            the_person "So yeah, that's going to be a no from me."
            if the_person.event_triggers_dict.get("preg_your_kids_known",0) > 0 and persistent.pregnancy_pref > 0:
                "You turn to leave and she grabs you by the arm."
                the_person "Umm, wait a sec, you know I'm a rebel."
                "She puts her arms around you and pulls you close."
                $ mc.change_locked_clarity(10)
                "She kisses you, and you kiss her back just as happily."
                $ the_person.add_role(girlfriend_role)
                the_person "Wonder if I can tempt you to give me a cream filling?"
                $ mc.change_locked_clarity(10)
            else:
                the_person "It is not like you knocked me up or anything, so its all fun and games from here."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)

            if the_person.get_opinion_score("cheating on men") > 0:
                # She likes cheating on men and offers to have an affair with you instead. Adds the affair role.
                "She takes a moment before responding."
                the_person "I mean, I already have a [so_title] and I can't just leave him like this."
                the_person "But... Maybe he doesn't need to know about any of this. Do you think you could be discreet."
                $ the_person.discover_opinion("cheating on men")
                menu:
                    "Have an affair with [the_person.title]":
                        mc.name "I can be if that's what you need."
                        $ the_person.draw_person(emotion = "happy")
                        $ the_person.add_role(affair_role)
                        $ the_person.change_slut(2, 60)
                        $ mc.change_locked_clarity(10)
                        "She leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
                        the_person "Well then, you know where to find me."

                    "Refuse":
                        mc.name "I can't do that. I need a relationship I can count on."
                        $ the_person.change_love(-3)
                        the_person "Right... Well, if you change your mind I'll be here."

            else:
                # She's just not into it, no matter how slutty she is. You'll have to seduce her to convince her first to have an affair.
                $ the_person.draw_person(emotion = "sad")
                "She takes a long moment before responding."
                the_person "Oh [the_person.mc_title], I'm so flattered, but you know that I have a [so_title]."
                if the_person.kids > 0:
                    if the_person.kids > 1:
                        the_person "I would never dream of leaving him, and it would devastate our children."
                    else:
                        the_person "I would never dream of leaving him, and it would devastate our child."
                else:
                    the_person "I would never dream of leaving him."


                if not the_person.has_taboo("vaginal_sex"):
                    mc.name "You didn't care about him when we were fucking."
                    if the_person.effective_sluttiness() > 50:
                        the_person "That didn't mean anything, we were just having fun. This is so much more serious than that."
                    else:
                        the_person "I don't know what I was thinking, that was a mistake."

                the_person "I care about you a lot, but it's just not something I could do."
                mc.name "I'm sorry to hear that. I hope we can still be friends."
                $ the_person.draw_person()
                the_person "As long as you understand where we stand, I think we can be."

        else:
            # She agrees, you're now in a relationship! Congratulations!
            $ the_person.draw_person(emotion = "happy")
            $ the_person.change_happiness(15)
            $ the_person.change_love(5)
            if the_person.age > 40:
                the_person "Oh I'm so happy to hear you say that! I was worried about our age difference, but I don't want that to stop us!"

            else:
                the_person "Oh my god, I'm so happy! Yes, I want you to be your girlfriend!"
            "She puts her arms around you and pulls you close."
            $ mc.change_locked_clarity(10)
            "She kisses you, and you kiss her back just as happily."
            $ the_person.add_role(girlfriend_role)

    return

label caught_cheating_label(the_other_girl, the_girlfriend): #Note: the_other_girl is stored as an argument in the event, while the_girlfriend is passed as an extra argument, so they are listed backwards.
    # This is an event added to the on_enter_room list for the girlfriend after she catches you cheating.

    if not the_girlfriend.has_role(girlfriend_role):
        return #She's lost the role somehow between now and when she caught you, so clear this out and move on.

    $ the_girlfriend.draw_person(emotion = "angry")
    "[the_girlfriend.title] storms up to you as soon as she sees you."
    the_girlfriend "What the fuck [the_girlfriend.mc_title]! How could you do that to me?"
    mc.name "Calm down, everything's okay."
    #TODO: Add some dialogue in case she's a particularly important person (ie. friend, mother)
    if town_relationships.is_family(the_girlfriend, the_other_girl):
        $ the_item = town_relationships.get_relationship_type(the_girlfriend, the_other_girl).lower()
        the_girlfriend "Really? Everything's okay while you're having sex with my [the_item]?"
        $ the_girlfriend.change_love(-25 + (5 * the_girlfriend.get_opinion_score("incest")))
    else:
        the_girlfriend "Really? Everything's okay while you're having sex with another woman?"
        $ the_girlfriend.change_love(-25)

    # Note: This only happens if she saw something happening that was too slutty for her, slutty girls think it's totally fine and normal.
    mc.name "Just let me explain..."
    if the_girlfriend.love < 60:
        the_girlfriend "I don't want to hear it. You're a lying scumbag who broke my heart..."
        $ the_girlfriend.change_happiness(-20)
        $ the_girlfriend.draw_person(emotion = "sad")
        $ the_girlfriend.remove_role(girlfriend_role)
        the_girlfriend "We're done! Through! Finished!"
        "She turns around and storms off."
        $ clear_scene()
    else:
        the_girlfriend "How could you possibly explain that?"
        mc.name "We were just fooling around, it didn't mean anything. Come on, you know I love you, right?"
        "She glares at you, but bit by bit her expression softens."
        "You sit down with her and calm her down, until finally she breaks and hugs you."
        the_girlfriend "Just never do that to me again, okay?"
        $ the_girlfriend.change_slut(2, 60)
        $ the_girlfriend.change_obedience(4)
        mc.name "Of course not, you'll never catch me doing that again."
        the_girlfriend "And I never want to see that bitch anywhere around you, okay?"
        mc.name "Of course."

    if not town_relationships.is_family(the_girlfriend, the_other_girl):
        $ town_relationships.worsen_relationship(the_girlfriend, the_other_girl)
        $ town_relationships.worsen_relationship(the_girlfriend, the_other_girl)
    return

label ask_get_boobjob_label(the_person):
    mc.name "I've been thinking about something lately."
    the_person "Mhmm? What about?"
    if the_person.has_large_tits:
        mc.name "Your breasts are great, but I think you could get some work done on them to make them even better."
        "She looks down at her tits and frowns."
        the_person "Do you think? Well, I suppose I could see someone about them."
    else:
        mc.name "Your breasts are nice, but I think they could stand to be a little bigger."
        "She looks down at her tits and frowns."
        the_person "Hmm, I guess you're right. If you want I could see someone about them."


    $ so_title = ""
    $ so_obedience_requirement = 150 - (5*the_person.get_opinion_score("cheating on men"))

    $ self_pay_requirement = 150 - (the_person.get_opinion_score("showing her tits") * 5)
    if the_person.relationship != "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
    menu:
        "Pay for her boobjob\n{color=#ff0000}{size=18}Costs: $7000{/size}{/color}" if mc.business.has_funds(7000):
            mc.name "If you arrange for it I don't mind paying for it."
            $ mc.business.change_funds(-7000)

        "Pay for her boobjob\n{color=#ff0000}{size=18}Requires: $7000{/size}{/color} (disabled)" if not mc.business.has_funds(7000):
            pass

        "Have her pay for it" if the_person.obedience >= self_pay_requirement and the_person.has_role(girlfriend_role):
            mc.name "Yeah, go see someone for me and get some implants. I want some nice big tits to play with"
            if the_person.get_opinion_score("being submissive") > 0:
                $ mc.change_locked_clarity(10)
                "She nods happily."
            else:
                "She hesitates, as if waiting for you to offer to pay, then nods dutifully."
                $ the_person.change_happiness(-5)

        "Have her pay for it\n{color=#ff0000}{size=18}Requires: [self_pay_requirement] Obedience{/size}{/color} (disabled)" if the_person.obedience < self_pay_requirement and the_person.has_role(girlfriend_role):
            pass

        "Have her [so_title] pay for it" if the_person.obedience >= so_obedience_requirement and the_person.has_role(affair_role):
            mc.name "Yeah, go see someone and get some implants put in. You can get your [so_title] to pay for them, right?"
            the_person "I don't know, what do I tell him?"
            $ mc.change_locked_clarity(10)
            mc.name "What every man wants to hear: \"Honey, I want to get some bigger tits!\"."
            mc.name "He'll be jumping at the opportunity to pay. Trust me."

        "Have her [so_title] pay for it\n{color=#ff0000}{size=18}Requires: [so_obedience_requirement] Obedience{/size}{/color} (disabled)"if the_person.obedience < so_obedience_requirement and the_person.has_role(affair_role):
            pass

        "Never mind":
            mc.name "On second thought, I don't think it's worth it. You look perfect just the way you are."
            the_person "Aww, thank you [the_person.mc_title]!"
            return

    $ the_person.discover_opinion("showing her tits")
    if the_person.get_opinion_score("showing her tits") > 0:
        $ the_person.change_happiness(10)
        $ the_person.change_obedience(1)
        $ mc.change_locked_clarity(10)
        the_person "Alright, I'll do it! Thank you [the_person.mc_title], I've always thought girls with bigger boobs looked hotter."


    elif the_person.get_opinion_score("showing her tits") < 0:
        $ the_person.change_happiness(-10)
        $ the_person.change_obedience(3)
        the_person "Fine, if that's what you'd like. I don't think I'll like all the attention being on my tits, but I want you to be happy."

    else:
        $ the_person.change_obedience(2)
        $ mc.change_locked_clarity(5)
        the_person "Okay [the_person.mc_title], if you want it I'll do it for you."

    the_person "I'll get it scheduled, if we're lucky I'll be able to have it done in a few days."
    if the_person.has_role(affair_role):
        the_person "I don't know if my [so_title] would want to kill you or thank you for this."

    $ add_girlfriend_got_boobjob_action(the_person)
    return

label girlfriend_got_boobjob_label(the_person):
    call got_boobjob(the_person) from _call_got_boobjob_girlfriend_got_boobjob
    $ add_girlfriend_brag_boobjob_action(the_person)
    return

label girlfriend_boob_brag_label(the_person): #TODO: Decide if we need a little alt-dialogue for the affair side of things.
    the_person "Hey [the_person.mc_title], what do you think?"
    if the_person.get_opinion_score("showing her tits") < 0:
        $ mc.change_locked_clarity(20)
        "She puts her arms behind her, revealing her newly enlarged chest."
        the_person "These feel so... excessive. It feels like everyone is staring at them all the time now."
        $ the_person.change_slut(-1 + the_person.get_opinion_score("showing her tits"))
    else:
        $ mc.change_locked_clarity(20)
        "She pushes her chest out towards you, shaking her tits just a little."
        the_person "I hope you like them, maybe we can have some fun with them later."
        $ the_person.change_slut(2, 60)

    call talk_person(the_person) from _call_talk_person_girlfriend_boob_brag_label
    return

label plan_date_night(the_person):
    #Special date for girlfriends only, you invite her over (or go over to her place?) and spend time watching a movie or something.

    return

label got_boobjob(the_person):
    $ min_cup_increase = 2
    # Event called a few days after someone has been asked to get a boob job. Results in larger brests. Duh.
    if Person.rank_tits(the_person.tits) <= (Person.rank_tits(Person.get_minimum_large_tit())-min_cup_increase): #Ie. B cup or smaller.
        $ the_person.tits = Person.get_minimum_large_tit() #Small tits all get upgraded to "large" D cup tits as a minimum, so they can be titfucked after.
        if the_person.personal_region_modifiers.get("breasts", 1) < 0.6:
            $ the_person.personal_region_modifiers["breasts"] = 0.3 #This is "normal" for C cups, so a little firmer than natural breasts but not by much.
    else: #Otherwise they get bigger by two steps.
        python:
            for x in range(0,min_cup_increase):
                    the_person.tits = the_person.get_larger_tit(the_person.tits) #Upgrade them twice, because we want boob jobs to be immediately noticeable.
        #Note that we DON'T change their breast region weight, to simulate natural vs. fake tits.

    if the_person.has_role(instapic_role):
        $ the_person.event_triggers_dict["insta_new_boobs_brag"] = True
        $ the_person.event_triggers_dict["insta_generate_pic"] = True #She'll make a post right away on Instapic about her new boobs.
    if the_person.has_role(dikdok_role):
        $ the_person.event_triggers_dict["dikdok_new_boobs_brag"] = True
        $ the_person.event_triggers_dict["dikdok_generate_video"] = True
    if the_person.has_role(onlyfans_role):
        $ the_person.event_triggers_dict["onlyfans_new_boobs_brag"] = True

    $ the_person.event_triggers_dict["getting boobjob"] = False #Reset the flag so you can ask her to get _another_ boobjob.
    if the_person.event_triggers_dict.get("boobjob_count",0) == 0:
        $ the_person.event_triggers_dict["boobjob_count"] = 1
    else:
        $ the_person.event_triggers_dict["boobjob_count"] += 1
    return

label girlfriend_ask_trim_pubes_label(the_person):
    mc.name "I want you to keep your pubes trimmed differently for me."
    "[the_person.possessive_title] nods obediently."
    the_person "How do you want me to trim them?"
    if the_person.event_triggers_dict.get("trimming_pubes", None) is not None:
        # She was already planning on a different style, so we can have some change your mind dialogue here
        $ mc.business.mandatory_crises_list.remove(the_person.event_triggers_dict.get("trimming_pubes",None)) #If she already had an event for this make sure to remove it.
        $ the_person.event_triggers_dict["trimming_pubes"] = None

    $ pubes_choice = renpy.display_menu(girlfriend_build_pubes_choice_menu(the_person),True,"Choice")

    if pubes_choice == "Never mind":
        mc.name "On second thought, I think they're fine the way they are."
    else:
        "You describe the style you want to her as she listens intently.."
        if pubes_choice.ordering_variable > the_person.pubes_style.ordering_variable:
            the_person "Okay, I'll have to let it grow out a bit but as soon as I can I'll trim them just the way you want [the_person.mc_title]."
            #It will take some time for them to grow out.
            $ add_girlfriend_do_trim_pubes_action(the_person, pubes_choice, renpy.random.randint(3,8))
        else:
            the_person "Okay, I'll trim them for you as soon as I can [the_person.mc_title]."
            $ add_girlfriend_do_trim_pubes_action(the_person, pubes_choice, 1)
    $ del pubes_choice
    return

label girlfriend_do_trim_pubes_label(the_person, the_style):
    #TODO: decide if we want to have a pubes comment where she tells you she's done it.
    $ girlfriend_set_new_pubes(the_person, the_style)
    return

label girlfriend_pubes_comment(the_person):
    #Next time you talk to her she comments that she trimmed her pubes
    return

label girlfriend_fuck_date_event(the_person):
    #Figure out her outfit for this

    if the_person.get_opinion_score("not wearing anything") > the_person.get_opinion_score("lingerie"):
        $ the_person.apply_outfit(Outfit("Nude"), update_taboo = True) #She's wearing nothing at all. nothing at all. nothing at all...

    elif the_person.get_opinion_score("lingerie") >= 0:
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.sluttiness + 20, the_person.sluttiness // 3, guarantee_output = True, preferences = WardrobePreference(the_person)), update_taboo = True) #She's just wearing lingerie for the evening.

    else:
        $ the_person.apply_outfit(the_person.decide_on_outfit(), update_taboo = True) #She picks a slutty outfit, but nothing truly "special".

    if the_person.obedience > 180 or the_person.get_opinion_score("being submissive") > 0 or the_person.get_opinion_score("giving blowjobs") > 0:
        #She's on her knees and ready to suck you off as soon as you come in.
        $ the_person.draw_person(position = "kneeling1")
        $ mc.change_locked_clarity(20)
        the_person "Hello, I'm ready for you [the_person.mc_title]..."
        "She licks her lips and watches you from her knees."
        the_person "Don't waste any time, I want you in my mouth."
        call fuck_person(the_person, private = True, start_position = blowjob, start_object = make_floor()) from _call_fuck_person_girlfriend_fuck_date_event_1

    else:
        #She's standing and ready to make out as soon as you come in."
        $ the_person.draw_person()
        $ mc.change_locked_clarity(10)
        the_person "Hello [the_person.mc_title]... I've been thinking about this all day."
        "You step inside. She reaches past you and closes the bedroom door." #Note that you never end up with submissive people down this branch
        "She wastes no time wrapping her arms around you and kissing you."
        call fuck_person(the_person, private = True, start_position = kissing, start_object = make_floor()) from _call_fuck_person_girlfriend_fuck_date_event_2

    $ the_report = _return

    $ done = False
    $ had_to_run = False
    $ girl_came = False
    $ so_called = False
    $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
    while not done:
        if the_report.get("girl orgasms", 0) > 0: #TODO: Have some variation to this based on how many times we've looped around.
            $ the_person.change_love(2 + the_person.get_opinion_score("cheating on men"))
            $ the_person.change_slut(1, 80)
            the_person "Oh god... That was amazing!"
            "[the_person.title] lies down on her bed and catches her breath."
            the_person "Ready to get back to it?"
            $ girl_came = True

        else:
            the_person "Whew, good job. Get some water and let's go for another!"
            "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
            "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."



        if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
            "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
            if girl_came:
                the_person "Well, I guess that's all I'm going to be drawing out of you for tonight. That was fun."
                "She kisses you and runs her hand over your back."
                the_person "Now you should get going. Unless you're planning to stay the night?"
            else:

                $ the_person.change_love(-1)
                $ the_person.change_slut(-1)
                the_person "Well I guess we're done then... Maybe next time you can get me off as well."

            $ done = True
            "You get dressed, triple check you haven't forgotten anything, and leave. [the_person.title] kisses you goodbye at the door."
        else:
            "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to get back to work."
            $ mc.change_energy(energy_gain_amount)
            $ the_person.change_energy(energy_gain_amount) #She gains some back too
            if energy_gain_amount >= 10:
                $ energy_gain_amount += -10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
            menu:
                "Fuck her again":
                    "Soon you're ready to go again and you wrap your arms around [the_person.title]."
                    mc.name "Come here you little slut."
                    # $ random_num = renpy.random.randint(0,100)
                    #TODO: Chance her adult daughter comes home and finds out what you're doing. (ie. same as the affair fuck date).
                    call fuck_person(the_person) from _call_fuck_person_girlfriend_fuck_date_event_3
                    $ the_report = _return

                "Call it a night":
                    mc.name "I have to get going. This was fun."
                    "You kiss [the_person.title], then get up and start collecting your clothes."
                    if girl_came:
                        the_person "Okay then. We need to do this again, you rocked my world [the_person.mc_title]."
                        "She sighs happily and lies down on her bed."

                    else:
                        the_person "Really? I didn't even get to cum yet..."
                        $ the_person.change_love(-1)
                        $ the_person.change_slut(-1)
                    $ done = True
                    "You shrug and pull up your pants."



    #As soon as done is True we finish looping. This means each path should narrate it's own end of encounter stuff.
    #Generic stuff to make sure we don't keep showing anyone.
    if not had_to_run:
        call check_date_trance(the_person) from _call_check_date_trance_girlfriend_fuck_date

    $ the_person.clear_situational_slut("Date")
    $ clear_scene()
    return "Advance Time"

label girlfriend_myplace_yourplace_label(the_person):
    mc.name "So, I'm kinda busy right now, but I thought that maybe later we could get together."
    the_person "Mmm, that sounds like fun. My place or yours?"
    menu:
        "My place":
            mc.name "Come over tonight, you can spend the night."
            $ the_person.call_dialogue("sleepover_yourplace_response")
            $ schedule_sleepover_in_story(the_person)
            $ mc.business.event_triggers_dict["your_place"] = True
        "Your place":
            mc.name "How about your place? I'll bring a bottle of wine."
            $ the_person.call_dialogue("sleepover_herplace_response")
            $ schedule_sleepover_in_story(the_person, your_place = False)
            $ mc.business.event_triggers_dict["your_place"] = False
    the_person "Anything else you need right now?"
    $ mc.change_locked_clarity(15)
    return

label girlfriend_sleepover_crisis_label():
    $ the_person = Person.get_person_by_identifier(mc.business.event_triggers_dict.get("girlfriend_person", None))
    if the_person is None:
        return
    #TODO give player the option to cancel the sleepover. she's probably sad.
    if mc.business.event_triggers_dict.get("your_place", True):
        "You go home for the night. Knowing that [the_person.title] is coming over, you quickly hop in the shower."
        $ mc.change_location(bedroom)
        "When you finish, you go to your room. You make sure everything is nice and tidy."
        $ mc.start_text_convo(the_person)
        the_person "Hey, I'm here, let me in?"
        $ mc.end_text_convo()
        $ the_person.draw_person()
        "You go to the front door. Your girlfriend is waiting for you."
        the_person "Hey!"
        #TODO mom or sister notice you, say hi, etc
        "You quickly lead her to your room. After you enter, you lock the door."
        the_person "I brought a few things with me. Mind if I use your bathroom?"
        mc.name "Go ahead."
        $ clear_scene()
        "[the_person.possessive_title] walks into your bathroom. You sit down on the bed and wait a couple minutes. Soon, you hear to door open."
        $ the_person.change_to_lingerie()
        $ the_person.draw_person()
        $ mc.change_locked_clarity(30)
        "[the_person.title] has changed into something much more comfortable..."
        mc.name "Damn, you look amazing..."
        $ the_person.call_dialogue("sleepover_yourplace_sex_start")
    else:
        "It's time for your date with [the_person.title]. You swing by the store on the way and pick up a decent bottle of wine."
        $ mc.business.change_funds(-15)
        $ the_person.learn_home()
        "You make your way to her place, then knock on the door. She quickly answers."
        $ the_person.draw_person()
        the_person "Ah! I'm so glad you're here. Come in!"
        $ mc.change_location(the_person.home)
        "You step inside. She leads you to the kitchen, where you set the wine."
        $ the_person.draw_person(position = "walking_away")
        the_person "That looks great! Let me get a couple wine glasses..."
        "She reaches up into the cabinet and pulls a couple down."
        $ the_person.draw_person(position = "stand2")
        the_person "You pour! I just got home a few minutes ago and I need to slip into something more comfortable."
        $ clear_scene()
        "You look through her drawers until you find a bottle opener. You pop the cork on the wine and pour a couple glasses."
        "She's busy... maybe you should put a serum in it?"
        menu:
            "Add a dose of serum to [the_person.title]'s wine" if mc.inventory.total_serum_count > 0:
                call give_serum(the_person) from _call_give_serum_girlfriend_sleepover_01
                "You mix the serum into [the_person.title]'s wine."
            "Add a dose of serum to [the_person.title]'s shake\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
                pass
            "Leave her drink alone":
                "You decide to leave her wine alone."
        "You wait for another minute, when you hear the bedroom door open."
        $ the_person.change_to_lingerie()
        $ the_person.draw_person()
        "[the_person.possessive_title] has changed into some sexy clothes."
        $ mc.change_locked_clarity(30)
        the_person "Hey... bring the glasses in here!"
        "She disappears into her bedroom. You quickly grab the glasses and follow her in. She is sitting on the edge of her bed."
        $ the_person.draw_person(position = "sitting")
        "You hand her the wine glass. She takes a long sip."
        $ the_person.call_dialogue("sleepover_herplace_sex_start")
    call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_01

    $ the_report = _return

    $ done = False
    $ girl_came = the_report.get("girl orgasms", 0)
    $ fuck_time_interrupted = False
    $ energy_gain_amount = 50 #Drops each round, representing your flagging endurance.
    if perk_system.has_ability_perk("Lustful Youth"):
        $ energy_gain_amount += 70
    while done == False:

        if girl_came > 5:
            $ the_person.change_stats(love = 3, slut = 1)
            $ the_person.call_dialogue("sleepover_impressed_response")
            if not perk_system.has_ability_perk("Lustful Youth"):
                "You feel like making [the_person.possessive_title] cum over and over has woken something inside you."
                "You feel like no matter what happens or how your day is going, you will always have the energy to make the ones you love cum."
                $ lustful_youth_perk_unlock()
                "You have gained the perk 'Lustful Youth'!"
        elif girl_came > 0:
            $ the_person.change_love(1)
            $ the_person.call_dialogue("sleepover_good_response")
        else:
            $ the_person.call_dialogue("sleepover_bored_response")

        if mc.energy < 40 and energy_gain_amount <= 20: #Forced to end the fuck date, so we set done to True.
            "The spirit is willing, but the flesh is spent. Try as she might [the_person.title] can't coax your erection back to life."
            if girl_came > 0:
                the_person "Mmm, I wore you out! That was fun."
                "She kisses you and runs her hand over your back."
            else:
                $ the_person.change_stats(slut = -1, love = -1)
                the_person "Well I guess we're done then... Maybe next time you can get me off as well."
            $ done = True

        else:
            "After a short rest you've recovered some of your energy and [the_person.possessive_title]'s eager to get back to work."
            $ mc.change_energy(energy_gain_amount)
            $ the_person.change_energy(energy_gain_amount) #She gains some back too
            if energy_gain_amount >= 10:
                $ energy_gain_amount += -10 #Gain less and less energy back each time until eventually you're exhausted and gain nothing back.
            menu:
                "Fuck her again":
                    "With your cock hard again, you pull [the_person.title] towards you."
                    $ mc.change_locked_clarity(30)
                    if renpy.random.randint(0,100) < 12 and not fuck_time_interrupted:
                        python:
                            fuck_time_interrupted = True    #Limit ourselves to one interruption per sleepover
                            possible_action_list = []
                            for interruption_scene in girlfriend_sleepover_interruption_list:
                                if interruption_scene.is_action_enabled(the_person): #Make sure requirement functions take the person as an arg
                                    possible_action_list.append(interruption_scene) #Build a list of valid crises from ones that pass their requirement.
                        $ interruption_action = get_random_from_list(possible_action_list)
                        if interruption_action:
                            call expression interruption_action.effect pass (*interruption_action.args) from _call_interruption_action_girlfriend_sleepover
                            $ del interruption_action
                        else: #default to fuck person if there isn't an interruption here.
                            call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_02
                            $ the_report = _return
                            $ girl_came += the_report.get("girl orgasms", 0)
                    elif renpy.random.randint(0,100) < ((the_person.get_opinion_score("taking control") + 1) * 15): #Baseline 15% chance, max 45% if she loves it
                        the_person "Mmm, lay back. I want to be on top this time..."
                        $ mc.change_locked_clarity(30)
                        "[the_person.possessive_title] pushes you on your back, you decide to take it easy for now and let her have her way with you."
                        call get_fucked(the_person, private = True)  from _call_get_fucked_sleepover_gf_03
                        $ the_report = _return
                        $ girl_came += the_report.get("girl orgasms", 0)
                    else:
                        call fuck_person(the_person, private = True) from _call_fuck_person_sleepover_gf_04
                        $ the_report = _return
                        $ girl_came += the_report.get("girl orgasms", 0)
                    if the_person.energy + energy_gain_amount < 30:
                        "[the_person.title] is panting. She is completely out of breath."
                        the_person "That's enough... oh my god, I can't move a muscle..."
                        the_person "I'm sorry honey, you wore me out! I need to be done for the night..."
                        $ done = True
                "Call it a night":
                    mc.name "Sorry, I need to get some sleep. I need to be done for tonight."
                    if girl_came:
                        the_person "Mmm, okay! That was nice."
                        "She kisses you and runs her hand over your back."
                    else:
                        $ the_person.change_stats(slut = -1, love = -1)
                        the_person "Well... Maybe next time you can get me off as well?"
                    $ done = True
    $ the_person.draw_person(position = "back_peek")
    "[the_person.possessive_title] turns her back to you. You cuddle up with her, wrapping your arm around her."
    mc.name "Goodnight..."
    the_person "Night..."

    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_sleepover_01

    $ picked_event = get_random_girlfriend_morning_action(the_person)
    if picked_event:
        call expression picked_event.effect pass (*picked_event.args) from _call_picked_event_girlfriend_sleepover
        $ del picked_event
    else:
        "You wakeup, but [the_person.possessive_title] isn't there. She must have gotten up early and left."
        $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
        $ the_person.apply_planned_outfit()
    $ mc.business.event_triggers_dict["girlfriend_person"] = None
    $ mc.business.event_triggers_dict["girlfriend_sleepover_scheduled"] = False  #Reset these so we can have another girlfriend sleepover.
    return

label girlfriend_wakeup_spooning_label(the_person):
    $ the_person.draw_person(position = "walking_away")
    "You slowly wake up, with your arms around [the_person.possessive_title], spooning with her."
    "She is still sleeping, but her skin is setting off electric sparks everywhere it is touching yours."
    $ mc.change_locked_clarity(50)
    if the_person.has_large_tits:
        "Your hands cup and squeeze one of her [the_person.tits_description]. It's so full and hot, it feels so good in your hands."
    else:
        "Your hand cups one of her [the_person.tits_description]. It's so soft and warm, it feels good in your hand."
    $ play_moan_sound()
    the_person "Mmmmmmmm......"
    "[the_person.title] moans but doesn't stir. Maybe you could surprise her with a little good morning dicking."
    menu:
        "Try to slide yourself in":
            pass
        "Get ready for the day":
            "Thinking about your tasks for the day, you feel yourself get a bit anxious about wasting the morning."
            "You get up and head for bathroom to take a leak."
            "When you come back, [the_person.title] is awake."
            $ the_person.draw_person(position = "missionary")
            the_person "Good morning! I slept great."
            $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
            $ the_person.apply_planned_outfit()
            $ the_person.draw_person(position = "stand3")
            "You both get ready for the day before heading out."
            $ clear_scene()
            return
    "Your cock is already hard, being up against [the_person.title], but she may not be fully wet yet."
    "You spit into your hand and rub it on your dick a few times, getting it lubed up."
    "When you feel good about it, you reach down and gently spread her cheeks apart. You position yourself at her entrance and give it a little push."
    "You are able to ease yourself about halfway in, but the angle makes it hard to get deep penetration."
    the_person "Oh [the_person.mc_title]. Mmmmmm..."
    "She's asleep, but is still responding to your touch. She must be a heavy sleeper! Or maybe she is just really worn out from last night..."
    "You give her a few gentle, smooth strokes. You can feel her pussy getting wetter with each stroke as her body begins to respond to the stimulation."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "With her legs closed and on her side like this, her pussy feels really tight. You can feel her gripping you every time you start to pull it out."
    $ mc.change_arousal(15)
    "Your reach around her with your hand and grab one of her tits. You start to get a little rough with her and pinch and pull at one of her nipples."
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(30)
    the_person "Mmm, that feels so... wait... [the_person.mc_title]?"
    $ the_person.draw_person( position = "back_peek", emotion = "happy")
    "[the_person.possessive_title] wakes up and looks back at you smiling."
    the_person "Oh my god that feels so good... Baby you know how to give a wakeup call, holy fuck!"
    "Encouraged by her words, you reach your hand down and lift her leg, giving you a better angle for deeper penetration."
    "You pick up the pace and begin to fuck her earnestly."
    $ the_person.change_arousal(30) #70
    $ mc.change_locked_clarity(30)
    the_person "Oh yes that feels so good, fuck me good!"
    "She reaches down and holds her leg for you, freeing up your hand. You reach down between her legs and start to play with her clit."
    "Her ass is making smacking noises now, every time your hips drive your cock deep inside of her."
    $ the_person.change_arousal(40) #110
    the_person "Oh fuck, yes! YES!"
    $ mc.change_locked_clarity(30)
    "She shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_person.have_orgasm()
    $ mc.change_arousal(20) #110
    mc.name "I'm gonna cum!"
    $ the_person.call_dialogue("cum_pullout")
    menu:
        "Cum inside":
            $ the_person.cum_in_vagina()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            "You grab her hip and shove your cock deep and hold it there, cumming deep inside her."
            $ play_moan_sound()
            "She moans and gasps with every spurt."
            $ the_person.call_dialogue("cum_vagina")
            "Satisfied, you slowly pull out of her."
            the_person "That's certainly one way to start the day... holy hell."
        "Pull out":
            $ the_person.cum_on_ass()
            $ the_person.draw_person( position = "back_peek")
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
            "You pull out at the last second. Large, thick ropes of cum rocket out of your cock, coating her ass."
            the_person "Oh my god... it's so warm!"
            "When you finish you lay back, admiring your painting skills."
            the_person "That's certainly one way to start the day..."
    $ the_person.reset_arousal()
    $ mc.reset_arousal()
    "You lay in bed together for a little longer, but soon it is time to start the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "stand4")
    "You both get ready for the day."
    the_person "Alright, I need to get some things done today. Thanks for the sleepover!"
    $ clear_scene()
    return

label girlfriend_roleplay_step_sister_label(the_person):
    #First, get the outfit, if we've picked one out for it.
    if (the_person.event_triggers_dict.get("stepsister_lingerie", None)):
        $ the_person.apply_outfit(the_person.event_triggers_dict.get("stepsister_lingerie", None))
    else:
        $ the_person.change_to_lingerie()
    #Now set nick names, etc
    $ the_person.roleplay_title_swap("Step Sis")
    $ the_person.roleplay_mc_title_swap("Step Brother")
    $ the_person.roleplay_possessive_title_swap("Your Step Sister")
    $ the_person.roleplay_personality_swap(lily_personality)

    if mc.business.event_triggers_dict.get("your_place", True):
        "Your girlfriend doesn't emerge from the bathroom right away, but eventually you hear her calling out."
        the_person "Help me! Someone help!"
        "You quickly get up and run into the bathroom."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "Oh! [the_person.mc_title]? Is that you?"
        "The roleplaying has begun..."
        mc.name "It's me, [the_person.title]. What's going on?"
        "She is bent over and has her head in the sink."
        if the_person.is_bald:
            the_person "Oh thank god it's you [the_person.mc_title]! I somehow got my hand stuck! In the... err... sink!"
            mc.name "You got your hand stuck in the sink, again!?! How does this keep happening [the_person.title]?"
        else:
            the_person "Oh thank god it's you [the_person.mc_title]! I somehow got my hair stuck! In the... err... sink!"
            mc.name "You got your hair stuck in the sink, again!?! How does this keep happening [the_person.title]?"
        "Her hips start to wiggle a bit as you approach her."
        $ mc.change_locked_clarity(30)
        the_person "I don't know! You've got to help me [the_person.mc_title]!"
        "She is laying it on pretty thick, but if it wasn't for her ass sticking up in the air, you might find this comical. Instead you are starting to get aroused."
        if the_person.vagina_available:
            "[the_person.possessive_title]'s ass, exposed and pointing at you, makes an enticing target. You run your hands along her hips and then grope it."
        else:
            "You walk over to [the_person.title]. You pull away the clothing between you and her ass."
            $ the_person.strip_outfit(top_layer_first = True, exclude_upper = True, exclude_lower = False, exclude_feet = True)
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(30)
        the_person "Oh my gooooooddd... [the_person.mc_title], what are you doing back there?"
        "You dip a finger into her cunt."
        mc.name "Just checking the plumbing, [the_person.title]. Nothing to worry about..."
    $ the_person.roleplay_title_revert()
    $ the_person.roleplay_mc_title_revert()
    $ the_person.roleplay_possessive_title_revert()
    $ the_person.roleplay_personality_revert()
    return

label girlfriend_underwear_shopping_label(the_person):
    mc.name "Hey, I got an idea. Why don't we go shopping for some new lingerie? Spice things up in the bedroom a bit?"
    if the_person.sluttiness < 40:
        the_person "Oh! Ummm... I guess..."
        the_person "I mean, if you want me to. I suppose I could get something new to wear for you once in a while..."
    else:
        the_person "Oh! That sounds fun!"
        the_person "This will be great! You can tell me what you like, and then I'll know what to wear whenever I want to get your engine revving."
    "You walk with your girlfriend to the mall. Soon you are in the clothes store, walking around the underwear section."
    $ mc.change_location(clothing_store)
    "Normally this would be a bit awkward by yourself, but with [the_person.title], it's not so bad..."
    the_person "Hmm, how should we do this? Want me to pick something out first? Or do you want to?"
    $ lingerie_outfit = None
    $ done = False
    while done == False:
        menu:
            "Have her pick something out":
                if lingerie_outfit is None:
                    the_person "Okay! I'll go with something I would normally wear, and you can let me know what you think, okay?"
                    mc.name "Sounds good. We can always make modifications to it or try something different if we need to."
                else:
                    mc.name "I think we should start over. Why don't you pick something out?"
                    the_person "Aww, I thought we were getting close. Ah well, I'll go pick something out."
                    $ the_person.draw_person(position = "kissing" )
                    "She gives you a quick kiss."
                    the_person "Thank you for being so patient!"
                    $ the_person.draw_person (position = "stand2")
                "You spend a few minutes with [the_person.possessive_title] as she looks through the different clothes racks. Eventually she picks something."
                "She takes your hand and you follow her to the dressing room."
                the_person "I'll be right back!"
                $ clear_scene()
                $ lingerie_outfit = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under")
                $ the_person.apply_outfit(lingerie_outfit)
                $ the_person.draw_person()
                "The door opens, and there stands your girlfriend."
                the_person "Aha! What do you think?"
                "You check her out for a bit. Should you change it? Or start over?"
            "Modify current outfit" if lingerie_outfit is not None:
                mc.name "I like it... but I'd like to make a few changes. Is that okay?"
                the_person "Okay! Grab what you think would look good, I'll be in the dressing room until you figure it out."
                $ clear_scene()
                "You pick out a few items to change her outfit a bit..."
                call screen outfit_creator(lingerie_outfit, outfit_type = "under")
                if _return != "Not_New":
                    $ lingerie_outfit = _return
                    "You pull out a few pieces of clothing to modify and take them to [the_person.possessive_title]. You set them on the top of the dressing room door."
                    mc.name "Here you go, try this."
                    if lingerie_outfit.outfit_slut_score <= the_person.sluttiness and lingerie_outfit.outfit_slut_score <= 40: #She likes it enough to try it on.
                        $ the_person.call_dialogue("lingerie_shopping_tame_response")
                    elif lingerie_outfit.outfit_slut_score >= 70 and lingerie_outfit.outfit_slut_score >= the_person.sluttiness:
                        $ the_person.call_dialogue("lingerie_shopping_wow_response")
                    else:
                        $ the_person.call_dialogue("lingerie_shopping_excited_response")
                    $ the_person.apply_outfit(lingerie_outfit, update_taboo = True)
                    $ the_person.draw_person()
                    the_person "What do you think?"
                    "You check her out for a bit. Should you change it? Or start over?"
                else:
                    mc.name "Sorry, I can't figure out a way to make it work. Why don't you get dressed really quick..."
                    the_person "Aww, okay..."
                    $ the_person.apply_outfit(the_person.planned_outfit)
                    $ the_person.draw_person()
                    $ lingerie_outfit = None
                    "She quickly gets dressed then emerges."
                    the_person "Okay... do you want to start over then?"

            "Pick something yourself":
                mc.name "Let me pick something out for you."
                if lingerie_outfit is not None:
                    the_person "Awww, okay. I kinda like this one, but I don't mind letting you dress me up a bit more."
                    the_person "I'll get changed, and while I do that, you pick something out for me, okay?"
                else:
                    the_person "Oh! Okay! I'll hop in the dressing room. You pick something out for me and just set it on top of the door, okay?"
                $ clear_scene()
                ""
                "You pick out a few items to change her outfit a bit..."
                call screen outfit_creator(Outfit("New Outfit"), outfit_type = "under")
                if _return != "Not_New":
                    $ lingerie_outfit = _return
                    "You pick out an outfit and take the clothes to [the_person.possessive_title]. You set them on the top of the dressing room door."
                    mc.name "Here you go, try this."
                    $ the_person.apply_outfit(lingerie_outfit, update_taboo = True)
                    if lingerie_outfit.outfit_slut_score <= the_person.sluttiness and lingerie_outfit.outfit_slut_score <= 40: #She likes it enough to try it on.
                        $ the_person.call_dialogue("lingerie_shopping_tame_response")
                    elif lingerie_outfit.outfit_slut_score >= 70 and lingerie_outfit.outfit_slut_score >= the_person.sluttiness:
                        $ the_person.call_dialogue("lingerie_shopping_wow_response")
                    else:
                        $ the_person.call_dialogue("lingerie_shopping_excited_response")

                    $ the_person.draw_person()
                    the_person "What do you think?"
                    "You check her out for a bit. Should you change it? Or start over?"
                else:
                    mc.name "Sorry, I can't figure out a way to make it work. Why don't you get dressed really quick..."
                    the_person "Aww, okay..."
                    $ the_person.apply_outfit(the_person.planned_outfit)
                    $ the_person.draw_person()
                    $ lingerie_outfit = None
                    "She quickly gets dressed then emerges."
                    the_person "Okay... do you want to start over then?"

            "Buy this" if lingerie_outfit is not None:
                $ done = True
                $ mc.change_locked_clarity(30)
                $ the_person.change_novelty(5)
            "Give up" if lingerie_outfit is None:
                $ done = True
    if lingerie_outfit is None:
        $ the_person.draw_person(emotion = "sad")
        the_person "Ah, okay. That's alright, maybe we could try again another time?"
        mc.name "Yeah, I think that might be for the better."
        $ the_person.change_stats(happiness = -3)
        "You head to the front of the store and walk out without buying anything."
    else:
        mc.name "That's it. That is exactly what I want."
        the_person "Ahh! Okay! Let me change out of it real quick and let's buy it."
        $ clear_scene()
        "[the_person.possessive_title] retreats into the dressing room for a minute."
        "Soon, she emerges, holding the items you've decided to purchase."
        $ the_person.apply_outfit(the_person.planned_outfit)
        $ the_person.draw_person()
        if the_person.has_taboo("roleplay"):
            pass
        else:
            "As you are walking up to the checkout counter, [the_person.title] asks you about the outfit."
            the_person "So... is this something you want me to wear when we like... do some roleplaying? Or just a sexy outfit?"
            "NOTE! Roleplay scenes are not yet implemented, but you can save outfits for them now..."
            menu:
                "Just a sexy outfit":
                    $ the_person.event_triggers_dict["favorite_lingerie"] = lingerie_outfit
                    the_person "Mmmm, okay! I'll wear this for you when I just want to be sexy!"
                "Roleplay: My baby girl":
                    $ the_person.event_triggers_dict["babygirl_lingerie"] = lingerie_outfit
                    if the_person.get_opinion_score("incest") > 0:
                        the_person "Oh! That sounds hot... You want to spank me while I call you daddy?"
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
                "Roleplay: My employee":
                    $ the_person.event_triggers_dict["employee_lingerie"] = lingerie_outfit
                    if the_person.is_employee:
                        the_person "Oh! But... I'm already your employee?"
                        mc.name "But what if you were a slutty employee who wasn't dating her boss and really needed a promotion."
                        the_person "Aaahhhh I see where you are going with this..."
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
                "Roleplay: My student":
                    $ the_person.event_triggers_dict["student_lingerie"] = lingerie_outfit
                    the_person "Ahhh, oh teacher? I'm sorry I forgot to study! What can I do to pass this class?"
                    mc.name "You've got exactly the right idea."
                "Roleplay: My ditzy stepsister" if not the_person.has_role(sister_girlfriend_role):
                    $ the_person.event_triggers_dict["stepsister_lingerie"] = lingerie_outfit
                    if the_person.get_opinion_score("incest") > 0:
                        the_person "Oh! That sounds hot... What are you going to do to me... step bro?"
                    else:
                        the_person "That's kinda weird... like those porn videos? I guess if you want to try it..."
        "You buy the outfit at the counter. It's a little pricey, but you're sure it'll be worth the investment."
        $ mc.business.change_funds(-150)
        $ the_person.add_outfit(lingerie_outfit, outfit_type = "under")
        the_person "Thanks, [the_person.mc_title]! This was fun!"
        if schedule_sleepover_available():
            the_person "So... want me to come over tonight? I'm not doing anything later..."
            menu:
                "Come over":
                    mc.name "I'd like to see this outfit in action. My place, say 9pm?"
                    the_person "Okay! See you then!"
                    $ the_person.event_triggers_dict["girlfriend_sleepover_lingerie"] = lingerie_outfit
                    $ schedule_sleepover_in_story(the_person)
                "Another time":
                    mc.name "Sorry, I'm running behind on work stuff. Another time, and soon."
                    the_person "Okay, I understand!"

    "You chat with your girlfriend for a bit, but soon it is time to go."
    $ the_person.draw_person(position = "kissing")
    "[the_person.possessive_title] embraces you and gives you a quick kiss before you part ways."
    $ mc.change_locked_clarity(10)
    $ clear_scene()
    $ del lingerie_outfit
    call advance_time from _call_advance_girlfriend_lingerie_shopping_01
    return

label girlfriend_quit_dikdok_label(the_person):
    mc.name "Hey [the_person.title], would you do something for me?"
    the_person "Sure, [the_person.mc_title], what do you need?"
    mc.name "I'm not very comfortable with you on DikDok, so I would prefer if you closed your account."
    the_person "Well, since I have you in my life, I don't see why not."
    $ the_person.remove_role(dikdok_role)
    $ the_person.event_triggers_dict["block_dikdok"] = True
    "She pulls out her phone and closes her account right there."
    return
