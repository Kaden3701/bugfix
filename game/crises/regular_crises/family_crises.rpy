# holds all of the crises involving your family.

init 1 python:
    def mom_outfit_help_requirement():
        if time_of_day == 4 and (day%7 <= 3 or day%7==7) and mc.is_home: #It has to be a day before a weekday, so she has work in the morning.
            return mom.is_available and mom.job != unemployed_job and not mom.has_queued_event("sleeping_walk_in_label")
        return False

    def sister_helps_mom_with_next_day_outfit(mom, sister):
        mom.change_stats(slut = 1, max_slut = __builtin__.min(sister.effective_sluttiness(), 30))

        thinks_appropriate = False
        count = 0
        while not thinks_appropriate or count < 3:
            outfit = Wardrobe.generate_random_appropriate_outfit(sister, outfit_type = "full", opinion_color = sister.favourite_colour, allow_skimpy = sister.effective_sluttiness() > 30)
            thinks_appropriate = mom.judge_outfit(outfit)
            count += 1
        if thinks_appropriate and outfit:
            return outfit
        return None

    crisis_list.append([
        Action("Mom Outfit Help Crisis ",mom_outfit_help_requirement,"mom_outfit_help_crisis_label"),
        5])

label mom_outfit_help_crisis_label():
    $ the_person = mom
    # Your mom asks for help planning an outfit for the next day. As a bonus you get to watch her strip down between outfits (peek/don't peek decision given, she doesn't care at high sluttiness)
    if not mom in mc.location.people:
        #She's in a different room, shh calls you in.
        the_person "[the_person.mc_title], can you help me with something for a moment?"
        "You hear [the_person.possessive_title] call for you from her bedroom."
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, I'll be right there."
                $ mom_bedroom.show_background()
                $ the_person.draw_person()
                "You step into [the_person.possessive_title]. She's standing at the foot of her bed and laying out a few sets of clothing."
                mc.name "Hey [the_person.title], what's up?"

            "Say you're busy":
                mc.name "Sorry [the_person.title], I'm a little busy at the moment."
                the_person "Okay, I'll ask your sister."
                $ the_person.next_day_outfit = sister_helps_mom_with_next_day_outfit(the_person, lily)
                $ clear_scene()
                return
    else:
        #She's in the room with you right now (how? no clue, but maybe it'll happen one day!)
        $ the_person.draw_person()
        the_person "[the_person.mc_title], could you help me with something for a moment?"
        menu:
            "Help [the_person.possessive_title]":
                mc.name "Sure thing, what's up?"
                "[the_person.possessive_title] goes over to her closet and pulls out a few sets of clothing. She starts to lay them out."

            "Say you're busy":
                mc.name "Sorry [the_person.title], I should really be getting to bed."
                the_person "That's okay [the_person.mc_title], I'll ask your sister then."
                $ the_person.next_day_outfit = sister_helps_mom_with_next_day_outfit(the_person, lily)
                $ clear_scene()
                return

    if mom.job in [mom_secretary_job, mom_associate_job]:
        the_person "I've got a meeting with an important client tomorrow and I don't know what I should wear."
    else:
        the_person "I don't know what to wear to work tomorrow and I want to make an impression on the girls."

    the_person "Could you give me your opinion?"
    mc.name "Of course, let's take a look!"
    $ first_outfit = Wardrobe.generate_random_appropriate_outfit(the_person)
    $ second_outfit = None # Changes her goals based on how you respond to the first one (ie. she tones it down, makes it sluttier, or keeps it the way it is)
    $ third_outfit = None # She asks you to put something together from her wardrobe. If it's reasonable for her she'll add it to her wardrobe.
    $ caught = False #Did you get caught watching her strip

    if the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 30: #She really doesn't want you to see anything
        the_person "Okay, I'll need a moment to get changed."
        mc.name "I can just turn around, if that would be faster."
        the_person "I'll just be a second. Go on, out."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of her bedroom. You lean against her door and wait."
        the_person "Okay, all done. Come on in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person "Okay, I'll need a moment to get changed. Could you just turn around for a second?"
        $ clear_scene()
        "You nod and turn your back to [the_person.possessive_title]. You hear her moving behind you as she starts to get undressed."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."

                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take's off her [strip_choice.display_name]."
                    $ mc.change_locked_clarity(2)
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                        the_person "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ clear_scene()
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person "Just give me one second to get dressed [the_person.mc_title]."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ the_person.strip_outfit(exclude_feet = False)
        $ mc.change_locked_clarity(10)
        "Once she's stripped naked she grabs her new outfit and starts to put it on."
        if the_person.update_outfit_taboos(): #Some taboo was broken.
            the_person "I should probably have told you to look away, but you don't mind, right?"
            the_person "It's nothing you haven't seen when you were younger."
            mc.name "I don't mind at all [the_person.title]."
            "She smiles at you and finishes getting dressed again."

    $ the_person.apply_outfit(first_outfit, update_taboo = True)
    $ the_person.draw_person()
    the_person "Well, what do you think?"
    "You take a moment to think before responding."
    menu:
        "Say it's too revealing":
            mc.name "I don't think it's very appropriate for work [the_person.title]. Maybe you should try something a little less... revealing."
            $ the_person.change_slut(-2)
            the_person "Maybe you're right. Okay, I'll try something a little more conservative for this next outfit."
            $ second_outfit = Wardrobe.generate_random_appropriate_outfit(the_person, sluttiness_limit = the_person.effective_sluttiness() - 10)

        "Say she looks beautiful in it":
            mc.name "You look beautiful [the_person.title], I think it would be perfect."
            $ the_person.change_stats(happiness = 5, love = 1)
            "She smiles and blushes."
            the_person "You aren't just saying that, are you? I want your real opinion"
            mc.name "It's a great look for you."
            the_person "Great! I want to try another outfit before I settle on this one though, if you don't mind."
            $ second_outfit = Wardrobe.generate_random_appropriate_outfit(the_person)

        "Say it's not revealing enough":
            mc.name "I don't know [the_person.title], it's a little stuffy, isn't it? Maybe you should pick something that's a little more modern and fun."
            $ the_person.change_slut(1+the_person.get_opinion_score("skimpy uniforms"))
            $ the_person.discover_opinion("skimpy uniforms")
            if the_person.get_opinion_score("skimpy uniforms") >= 0:
                the_person "Do you think so? Maybe it is a little too conservative."
                "She nods and turns towards her closet."
                the_person "Okay, I'll give something else a try then."
            else:
                the_person "Oh no, I hate having to dress in those skimpy little outfits everyone wants their secretaries in these days."
                "She sighs and shrugs."
                the_person "Well, if that's what you think I'll give something else a try."
            $ second_outfit = Wardrobe.generate_random_appropriate_outfit(the_person, sluttiness_limit = the_person.effective_sluttiness() + 10)

    #Strip choices for the second peek section
    if the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 35 or caught: #She really doesn't want you to see anything
        the_person "Okay, I just need to get changed again."
        $ clear_scene()
        "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
        the_person "Okay, come in!"

    elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
        the_person "I'm going to need to get changed again."
        $ clear_scene()
        "You turn around to give her some privacy."
        menu:
            "Try and peek":
                # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                $ the_person.draw_person()
                "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                $ caught = False
                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                while strip_choice and not caught:
                    $ the_person.draw_animated_removal(strip_choice)
                    "You watch as [the_person.possessive_title] take's off her [strip_choice.display_name]."
                    $ mc.change_locked_clarity(2)
                    if renpy.random.randint(0,100) < 10: #you got caught
                        the_person "I'll be done in just a second [the_person.mc_title]..."
                        "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                        $ the_person.draw_person(emotion = "angry")
                        $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                        the_person "[the_person.mc_title], are you watching me change!"
                        mc.name "No, I... The mirror was just sort of there."
                        "She covers herself with her hands and motions for the door."
                        the_person "Could you wait outside, please?"
                        $ clear_scene()
                        "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                        the_person "Okay, you can come back in."
                        $ caught = True
                    else:
                        menu:
                            "Keep watching":
                                $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                            "Stop peeking":
                                "You pull your eyes away from the mirror and do your best not to peek."
                                $ clear_scene()
                                $ strip_choice = None

                if not caught:
                    "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                    the_person "Okay [the_person.mc_title], you can turn around now."

            "Wait until she's done":
                "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                the_person "Okay, all done. You can turn around now."

    else: #She's slutty enough that she doesn't care if you watch or not.
        the_person "It'll just take me a second to get changed."
        "[the_person.possessive_title] starts to strip down in front of you."
        $ the_person.strip_outfit(exclude_feet = False)
        $ mc.change_locked_clarity(10)
        "Once she's stripped naked she grabs another outfit and starts to put it on."

    $ the_person.apply_outfit(second_outfit, update_taboo = True)
    #$ the_person.outfit = second_outfit changed v0.24.1
    $ the_person.draw_person()

    the_person "Alright, there we go! Now, do you think this is better or worse than what I was just wearing?"
    $ the_person.draw_person(position = "back_peek")
    "She gives you a few turns, letting you get a look at the full outfit."
    $ the_person.draw_person()
    menu:
        "Suggest the first outfit":
            mc.name "I think you looked best in the first outfit, you should wear that."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = first_outfit
            the_person "I think you're right, I'll put it away for tomorrow."

        "Suggest the second outfit":
            mc.name "I think this one suits you better, you should wear it tomorrow."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = second_outfit
            the_person "I think you're right, it does look good on me."

        "Suggest your own outfit":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "You go to [the_person.possessive_title]'s closet and start to put together an outfit of your own for her."
            $ clear_scene()
            call outfit_master_manager(slut_limit = the_person.sluttiness + 10, show_overwear = False, show_underwear = False) from _call_outfit_master_manager_mom_outfit_help_enhanced
            $ third_outfit = _return
            $ the_person.draw_person()

            if third_outfit is None:
                "You try a few different combinations, but you can't come up with anything you think [the_person.title] will like."
                mc.name "Sorry [the_person.title], I thought I had an idea but I guess I was wrong."
                the_person "That's fine [the_person.mc_title]. Do you want to pick one of my outfits instead?"
                menu:
                    "Suggest the first outfit":
                        mc.name "I think you looked best in the first outfit, you should wear that."
                        "She smiles and nods."
                        $ the_person.change_happiness(2)
                        $ the_person.next_day_outfit = first_outfit
                        the_person "I think you're right, I'll put it away for tomorrow."

                    "Suggest the second outfit":
                        mc.name "I think this one suits you better, you should wear it tomorrow."
                        "She smiles and nods."
                        $ the_person.change_happiness(2)
                        $ the_person.next_day_outfit = second_outfit
                        the_person "I think you're right, it does look good on me."

            else:
                "You lay the outfit out for [the_person.possessive_title]. She looks it over and nods."
                the_person "I'll try it on, but I think I like it!"

                if the_person.effective_sluttiness() + the_person.love < 35 or caught: #She really doesn't want you to see anything
                    $ clear_scene()
                    "[the_person.possessive_title] shoos you out of the room while she changes into her new outfit."
                    the_person "Okay, come back!"

                elif the_person.effective_sluttiness(["underwear_nudity","bare_pussy","bare_tits"]) + the_person.love < 50: #She just asks you to turn your back, so you can peek if you want.
                    the_person "I'm just going to get changed one last time, if you could turn around for a second."
                    $ clear_scene()
                    "You turn around to give her some privacy."
                    menu:
                        "Try and peek":
                            # Chance to get spotted. Otherwise you get to watch as she strips clothing off one item at a time until she is naked.
                            $ the_person.draw_person()
                            "You shuffle to the side and manage to get a view of [the_person.possessive_title] using a mirror in the room."
                            $ caught = False
                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)
                            while strip_choice and not caught:
                                $ the_person.draw_animated_removal(strip_choice)
                                "You watch as [the_person.possessive_title] takes off her [strip_choice.display_name]."
                                $ mc.change_locked_clarity(2)
                                if renpy.random.randint(0,100) < 10: #you got caught
                                    the_person "I'll be done in just a second [the_person.mc_title]..."
                                    "Her eyes glance at the mirror you're using to watch her. You try to look away, but your eyes meet."
                                    $ the_person.draw_person(emotion = "angry")
                                    $ the_person.change_stats(happiness = -5, slut = 1 + the_person.get_opinion_score("not wearing anything"), max_slut = 20)
                                    the_person "[the_person.mc_title], are you watching me change!"
                                    mc.name "No, I... The mirror was just sort of there."
                                    "She covers herself with her hands and motions for the door."
                                    the_person "Could you wait outside, please?"
                                    $ clear_scene()
                                    "You hurry outside and close the door to [the_person.possessive_title]'s bedroom behind you."
                                    the_person "Okay, you can come back in."
                                    $ caught = True
                                else:
                                    menu:
                                        "Keep watching":
                                            $ strip_choice = the_person.outfit.remove_random_any(top_layer_first = True, do_not_remove = True)

                                        "Stop peeking":
                                            "You pull your eyes away from the mirror and do your best not to peek."
                                            $ clear_scene()
                                            $ strip_choice = None

                            if not caught:
                                "[the_person.possessive_title] finishes stripping down and starts to get dressed in her new outfit. After a few moments she's all put together again."
                                the_person "Okay [the_person.mc_title], you can look."

                        "Wait until she's done":
                            "You twiddle your thumbs until [the_person.possessive_title] is finished changing."
                            the_person "Okay, all done. You can look."

                else: #She's slutty enough that she doesn't care if you watch or not.
                    the_person "It'll just take a moment for me to slip into this."
                    "[the_person.possessive_title] starts to strip down in front of you."
                    $ the_person.strip_outfit(exclude_feet = False)
                    $ mc.change_locked_clarity(10)
                    "Once she's stripped naked she grabs another outfit and starts to put it on."

                $ the_person.apply_outfit(third_outfit, update_taboo = True)
                $ the_person.draw_person()
                $ the_person.change_stats(happiness = 5, obedience = 5, love = 1)
                the_person "I think you have great fashion sense [the_person.mc_title]! It's settled, I'll wear this tomorrow!"
                $ the_person.add_outfit(third_outfit,"full")
                $ the_person.next_day_outfit = third_outfit

    the_person "Thank you so much for the help [the_person.mc_title]. I don't know why but I've been feeling much more unsure about the way I dress lately."
    mc.name "Any time, I'm just glad to help."
    if the_person.effective_sluttiness(["touching_penis", "sucking_cock"]) > 50:
        the_person "Is there anything I could do to show you how thankful I am? You are such a helpful son..."
        if mc.energy < 50:
            mc.name "I'm sure you could think of something, but honestly I'm exhausted. I think I'll just head for bed."
            the_person "Of course honey. Have a good night!"
        else:
            mc.name "I don't know [the_person.title]. Did you have anything in mind?"
            the_person "Oh, I wouldn't say I have something specific..."
            "[the_person.possessive_title] starts to take off her outfit. Saving her clothes for tomorrow you guess?"
            $ the_person.strip_outfit(exclude_lower = True)
            $ mc.change_locked_clarity(10)
            if the_person.has_taboo("condomless_sex") and the_person.is_willing(tit_fuck): #Mid sluttiness path.
                "With her tits out, she starts to walk over to you."
                the_person "I'm sure it was hard for you... to watch your mother undress like that... right in front of you..."
                $ the_person.draw_person(position = "kissing")
                "She wraps her arms around you. The heat coming from her chest radiates against you. It feels great."
                "You pull her close as you embrace. Your erection is now rubbing up against her belly..."
                the_person "Oh my... you feel so hard. Why don't you let your mother take care of that for you?"
                "Slowly, [the_person.possessive_title] slides down to her knees. She pulls your zipper down and takes your cock out."
                $ the_person.draw_person(position = "blowjob")
                the_person "You have become such a virile young man..."
                $ mc.change_locked_clarity(20)
                if the_person.is_willing(blowjob) and the_person.get_opinion_score("giving blowjobs") >= the_person.get_opinion_score("giving tit fucks"):
                    "[the_person.possessive_title]'s lips part and she runs the tip of your cock back and forth across her tongue."
                    if the_person.has_taboo("sucking_cock"):
                        the_person "Oh my god... I just can't stop myself. I'm sorry honey, I know I shouldn't be doing this..."
                        the_person "I'll stop if you want me too. You probably think I'm crazy!"
                        mc.name "I don't think you're crazy. This is a great way to say thank you. I can't believe I'm so lucky."
                        the_person "I'm glad to hear that... I just... need to taste it!!!"
                        $ the_person.break_taboo("sucking_cock")
                    if the_person.is_bald:
                        "Suddenly, she opens a bit wider and takes your cock into her mouth. Your rest your hand on the top of her bald head as she starts to bob up and down."
                    else:
                        "Suddenly, she opens a bit wider and takes your cock into her mouth. Your hands run through her [the_person.hair_description] as her head starts to bob up and down."
                    call fuck_person(the_person, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_01

                else:
                    "You watch in amazement as she wraps your cock between her tits, you erection now enveloped in her creamy cleavage."
                    if the_person.has_taboo("touching_body"):
                        the_person "Oh my god... it's so hot... I just want to make it feel good!"
                        the_person "I'll stop if you want me too. You probably think I'm crazy!"
                        mc.name "I don't think you're crazy. This is a great way to say thank you. I can't believe I'm so lucky."
                        the_person "I'm glad to hear that... I just... want to feel it blow all over me!"
                        $ the_person.break_taboo("touching_body")
                    "[the_person.possessive_title] slowly starts to rock her body up and down, stroking your cock with her tits."
                    call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_02
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"
            elif the_person.is_willing(standing_doggy):
                the_person "I mean... you are such a virile young man... maybe you could think of some way I could thank you..."
                "[the_person.possessive_title] turns around and bends over as she starts to take off what is left of her outfit. She takes her time..."
                $ the_person.strip_outfit(position = "standing_doggy")
                "When she finishes, she stays bent over her bed. Her hips wiggle back and forth a bit, making it obvious what she has in mind..."
                $ mc.change_locked_clarity(20)
                "It's been a long day, but you still got some energy left, so you decide to have your way with her. You pull your dick out and step behind [the_person.possessive_title]."
                call fuck_person(the_person, start_position = standing_doggy, start_object = make_bed(), skip_intro = True, position_locked = True) from _call_fuck_person_mom_outfit_help_crisis_03
                "When you finish up, you put your dick away."
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"
            else:
                the_person "How about a nice handjob? I know that you like it when I take care of you."
                $ mc.change_locked_clarity(10)
                "[the_person.possessive_title] gets your cock out of your pants and starts jerking you off."
                call get_fucked(the_person, the_goal = "get mc off", start_position = handjob, start_object = make_floor(), skip_intro = True, prohibit_tags = ["Vaginal", "Anal"]) from _call_get_fucked_person_mom_outfit_help_crisis_01
                "When you are done, you put your cock in your pants."
                mc.name "That was nice... if you ever need any more outfit advice, let me know!"

    $ the_person.draw_person()
    "You leave [the_person.possessive_title] in her room as she starts to pack her clothes away."

    python:
        first_outfit = None
        second_outfit = None
        third_outfit = None
        clear_scene()
    return

init 1 python:
    def mom_lingerie_surprise_requirement():
        if time_of_day == 4 and mc.location == bedroom:
            if mom.arousal_perc > 50 and mom.energy > 50 and mom.love > 40:
                return mom.effective_sluttiness("underwear_nudity") > 40
        return False

    crisis_list.append([
        Action("Mom Lingerie Surprise Crisis", mom_lingerie_surprise_requirement, "mom_lingerie_surprise_label"),
        3])

label mom_lingerie_surprise_label():
    #In which your Mom comes to your room at night in some sexy lingerie and fools around with you. Triggers at high sluttiness and love.
    $ the_person = mom
    $ mc.change_location(bedroom)
    "You are woken up in the middle of the night by the sound of your bedroom door closing."
    "You sit up and turn on the lamp beside your bed."
    $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit(), update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    the_person "I'm sorry to wake you up [the_person.mc_title], but I wanted to ask you something."
    "[the_person.possessive_title] is standing by the door, wearing some very revealing lingerie. She walks over to your bed and sits down beside you."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "sitting")
    mc.name "What did you want to ask?"
    the_person "I know you've been busy with work, and I'm very proud, but sometimes I worry you're not having your needs met."
    "She places a hand on your arm and slides it up to your chest, caressing you with her soft fingers."
    the_person "Your physical needs, I mean. I know I'm your mother, but I thought I could dress up and you could pretend I was someone else. Someone not related to you."
    menu:
        "Ask for her help (tooltip)Ask your mother to help satisfy your physical desires.":
            mc.name "That would be amazing Mom, I could really use your help."
            $ the_person.change_slut(2, 50)
            "[the_person.possessive_title] smiles and bounces slightly on your bed."
            if the_person.effective_sluttiness() < 50:
                the_person "Excellent! Now you just pretend that I'm... your highschool sweetheart, and that we aren't related. Okay?"
                $ mc.change_locked_clarity(10)

            elif the_person.effective_sluttiness() < 80:
                the_person "Excellent! Don't think of me as your mother, just think of me as a sexy mom from down the street. I'm a real milf, okay?"
                $ mc.change_locked_clarity(20)

            else:
                the_person "Excellent! Now don't think of me as your mom, just think of me as your private, slutty milf. I'll do whatever your cock wants me to do, okay?"
                $ mc.change_locked_clarity(40)
            "You nod and she slides closer to you on the bed."

            $ the_person.add_situational_obedience("crisis_stuff", 25, "I'm doing it for my family.")
            call fuck_person(the_person) from _call_fuck_person_14
            $ the_report = _return
            if the_report.get("girl orgasms", 0):
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "[the_person.possessive_title] needs a few minutes to lie down when you're finished. Bit by bit her breathing returns to normal."
                $ the_person.change_love(5)
                the_person "Oh [the_person.mc_title], that was magical. I've never felt so close to you before..."

            else:
                $ the_person.draw_person(emotion = "happy")
                "When you're finished [the_person.possessive_title] gives you a kiss on your forehead and stands up to leave."
                $ the_person.change_love(3)
                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                the_person "Sweet dreams."

            $ the_person.clear_situational_obedience("crisis_stuff")

        "Not tonight":
            mc.name "That's very sweet of you Mom, and you look very nice, but I really just need a good night's sleep."
            "You see a split second of disappointment on [the_person.possessive_title]'s face, then it's gone and she blushes and turns away."
            the_person "Of course, I'm so sorry to have bothered you. I mean, it would be strange if we did anything like that, right?"
            $ the_person.draw_person(position = "walking_away")
            "She stands up and leaves your room. You're asleep within minutes."

    $ clear_scene()
    return

init 1 python:
    def mom_selfie_requirement():
        if time_of_day == 0 or time_of_day == 4:
            return False
        if mom.love < 15:
            return False
        if mc.is_home or mc.location == mom.location:
            return False
        return True

    crisis_list.append([
        Action("Mom Selfie Crisis", mom_selfie_requirement, "mom_selfie_label"),
        7])

label mom_selfie_label():
    #TODO: have a way of saving and reviewing selfies in the future.
    $ the_person = mom
    $ mc.start_text_convo(the_person)
    $ lowest_stat = mom.sluttiness
    if the_person.love < lowest_stat:
        $ lowest_stat = mom.love

    "While you're going about your day you get a text from your mother."
    if lowest_stat >= 100:
        #Both love and sluttiness are very high, she sends you super slutty selfies and says she can't wait till you come home, fuck her, and make her your woman.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if the_person.is_at_work:
                the_person "It's so hard not to talk about you at work. The other women are gossiping and I just want to tell them how good it feels when you try and breed me..."
                the_person "My pussy full of your warm cum, knowing that I can take care of you the way only a mother could."
                the_person "I think I'm going to go touch myself in the bathroom. I hope you are having a great day too [the_person.mc_title]!"
            else:
                $ the_person.apply_outfit(lingerie_wardrobe.pick_random_outfit(), update_taboo = True)
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "Her first message is a selfie of herself lying down on your bed in lingerie."
                the_person "I can't wait until you come home and make love to me. I wish I could spend every minute of every day worshiping your cock like a good mother should."

        elif ran_num == 1:
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)

            the_person "Hi [the_person.mc_title], I hope I'm not interrupting your busy work day. This is just a quick reminder..."
            $ the_person.draw_person(emotion = "happy")
            $ the_person.update_outfit_taboos()
            "You get a selfie from [the_person.possessive_title] naked in front of her bedroom mirror."
            the_person "... that your Mom wants to feel you inside her tonight. Don't stay out too late!"

        elif ran_num == 2:
            #Blowjob pose, she tells you to face fuck her, as is her duty
            $ the_person.draw_person(position = "blowjob", emotion = "happy", special_modifier = "blowjob")
            "You get a selfie from [the_person.possessive_title]. She's on her knees, mouth open wide."
            the_person "My mouth is yours to use however you want [the_person.mc_title]."
            the_person "It's my duty to take care of you, so grab and use it whenever you want."
        $ mc.change_locked_clarity(30)

    elif lowest_stat >= 80:
        #Both are high. Sends you slutty selfies and talks about how she wants to fuck you. Sends them from work, etc.
        $ ran_num = renpy.random.randint(0,1) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if the_person.is_at_work:
                the_person "I'm stuck here at work and all I can think about is you. Wish you were here..."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] sends you a selfie of herself in the office bathroom, naked and bending over the sink."


            else:
                the_person "I'm here at home and wishing it was you could help me take these pictures..."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(position = "standing_doggy")
                "[the_person.possessive_title] sends you a selfie her bedroom naked and bent over her bed."

            $ the_person.update_outfit_taboos()

        elif ran_num == 1:
            if the_person.is_at_work:
                the_person "I'm at work and stuck at my desk but I can't get you out of my head. I'm so wet, I wonder if anyone would notice if I touched myself..."
            else:
                the_person "I know it shouldn't, but thinking about you gets me so wet. You've made me a new woman [the_person.mc_title]."

        $ mc.change_locked_clarity(20)

    elif lowest_stat >= 60:
        #Sends you nudes and talks about how she'll help you blow off steam later.
        $ ran_num = renpy.random.randint(0,3) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            if the_person.is_at_work:
                the_person "I thought you might be stressed so I snuck away from work to take this for you."
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        if the_person.outfit.panties_covered:
                            the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a picture of herself stripped down in the office bathroom."
                the_person "I've got to get back to work. I hope nobody noticed me gone!"

            else:
                the_person "I was just about to get in the shower and I thought you might like a peek. Love you [the_person.mc_title]!"
                python:
                    for i in range(3):
                        the_person.outfit.remove_random_upper(top_layer_first = True)
                        if the_person.outfit.panties_covered: #If we get down to her panties keep them on, because that's sexier.
                            the_person.outfit.remove_random_lower(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a picture of herself stripped down in front of her bedroom mirror."

            $ the_person.update_outfit_taboos()

        elif ran_num == 1:
            the_person "I thought you might enjoy this ;)"
            python:
                for i in range(3):
                    the_person.outfit.remove_random_upper(top_layer_first = True)
                    the_person.outfit.remove_random_lower(top_layer_first = True)
            $ the_person.draw_person(emotion = "happy")
            "Mom sends you a picture of herself stripped naked in front of her bathroom mirror."
            $ the_person.update_outfit_taboos()
        elif ran_num == 2:
            the_person "I've been trying on underwear all day. Would you like a peek?"
            "[the_person.possessive_title] doesn't wait for a reply and starts sending selfies."
            python:
                for i in range(3):
                    the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True), update_taboo = True)
                    the_person.draw_person(emotion = "happy")
                    renpy.say(None,"")
            the_person "I hope you think your mommy looks sexy in her underwear ;)"

        elif ran_num == 3:
            python:
                while not the_person.tits_visible:
                    the_person.outfit.remove_random_upper(top_layer_first = True)

            if the_person.is_at_work:
                the_person "I think I'd be much more popular here at work if I was allowed to dress like this..."
                $ the_person.draw_person(emotion = "happy")
                "She sends you a selfie from her office bathroom with her top off."
                the_person "Oh well, at least I know you appreciate it. I need to get back to work, see you at dinner!"

            else:
                the_person "I'm so glad I'm not stuck at work, I can finally let these girls out..."
                $ the_person.draw_person(emotion = "happy")
                "She sends you a selfie from the kitchen with her top off."
                the_person "I hope your day is going well, love you!"
            $ the_person.update_outfit_taboos()

        $ mc.change_locked_clarity(20)

    elif lowest_stat >= 40:
        #Sends you teasing pictures (ie. no shirt or something) and talks about how much she loves you.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person "You're such a hard worker [the_person.mc_title]. Here's a little gift from the woman who loves you most in the world!"
            $ the_person.outfit.remove_random_upper(top_layer_first = True)
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend:
                "[the_person.possessive_title] sends you a selfie without her shirt on. The background looks like her bedroom."
            else:
                "[the_person.possessive_title] sends you a selfie without her shirt on. It looks like it was taken in the bathroom of her office."
            $ the_person.update_outfit_taboos()

        elif ran_num == 1:
            if the_person.is_at_work:
                the_person "I'm busy here at work but I really wish I could be spending time with you instead. Do you think I'm pretty enough to spend time with ;)"
                $ the_person.outfit.remove_random_upper(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "Mom sends you a selfie without her shirt on. It looks like she's taken in the bathroom of her office."
            else:
                the_person "I wish you were here spending time with me. Maybe this will convince you your mom is a cool person to hang out with!"
                $ the_person.outfit.remove_random_upper(top_layer_first = True)
                $ the_person.draw_person(emotion = "happy")
                "Mom sends you a selfie from her bedroom without her shirt on."
            $ the_person.update_outfit_taboos()

        elif ran_num == 2:
            $ the_clothing = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
            if the_clothing:
                $ the_clothing.colour[3] = the_clothing.colour[3]*0.9 #It's translucent.
                the_person "It looks like my [the_clothing.name] didn't like being in the wash, it's gone all see-through."
                $ the_person.draw_person(emotion = "happy")
                if the_clothing.underwear:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent bra."
                    if the_person.has_taboo("underwear_nudity"):
                        the_person "Oops, I probably shouldn't be sending pictures like this to my son!"
                        the_person "Oh well, it's not like I'm naked. You better not show it to your friends!"
                        $ the_person.break_taboo("underwear_nudity")
                else:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent top."
                the_person "Oh well, I can still wear it when I'm doing chores around the house. Hope your day is going better, love you!"
            else:
                the_person "I've looked everywhere, but I just can't find my favorite bra!"
                $ the_person.draw_person(emotion = "default", the_animation = blowjob_bob, animation_effect_strength = 0.8)
                "[the_person.possessive_title] sends you a short video of herself walking around your home. Her bare tits bounce with each step."
                the_person "You don't happen to know where it is, do you? I'm wandering around looking for it and it's getting chilly!"
                if the_person.has_taboo("bare_tits"):
                    the_person "Oops! I hope nobody saw you looking at that, I wasn't thinking about my breasts being out."
                    the_person "I don't mind you seeing them though, just don't go sharing that video with your friends!"
                    $ the_person.break_taboo("bare_tits")

        $ mc.change_locked_clarity(15)

    elif lowest_stat >= 20:
        #Sends you normal texts but talks about wanting to get away to talk to you instead
        $ ran_num = renpy.random.randint(0,4) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person "I hope I'm not interrupting, I just wanted to say hi and check in. I'm stuck here at work but wish I could spend more time with you."
            the_person "Have a great day, see you later tonight. Love, Mom."

        elif ran_num == 1:
            the_person "I hope you are having a great day [the_person.mc_title]! Imagining you out there working so hard makes me prouder than you can imagine!"
            the_person "I'm looking forward to seeing you at home tonight. Love, Mom."

        elif ran_num == 2:
            the_person "I hope you aren't busy, I was thinking about you and just wanted to say hi!"
            $ the_person.draw_person(emotion = "happy")
            if the_person.is_at_work:
                "[the_person.possessive_title] sends you a selfie she took from her office at work."
            else:
                "[the_person.possessive_title] sends you a selfie she took in the living room of your house."

        elif ran_num == 3:
            the_person "Kids these days are always sending selfies to each other, right? I hope I'm doing this right!"
            $ the_person.draw_person(emotion = "happy")
            if the_person.is_at_work:
                "[the_person.possessive_title] sends you a selfie she took from her office at work."
            else:
                "[the_person.possessive_title] sends you a selfie she took in the living room of your house."

        elif ran_num == 4:
            the_person "All your hard work has inspired me [the_person.mc_title], I'm going out for a walk to stay in shape!"
            $ the_person.draw_person(emotion = "happy", the_animation = blowjob_bob, animation_effect_strength = 0.8)
            "[the_person.possessive_title] sends you a short video she took of herself outside. She's keeping up a brisk walk and seems slightly out of breath."
            if not the_person.outfit.wearing_bra:
                "She doesn't seem to realise, but it's very obvious [the_person.possessive_title] isn't wearing a bra under her top."
                if the_person.has_large_tits:
                    "Her sizeable breasts heave up and down with each step."
                $ mc.change_locked_clarity(10)

    else:
        #Sends you normal motherly texts.
        $ ran_num = renpy.random.randint(0,2) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 0:
            the_person "I hope I'm not interrupting your busy day [the_person.mc_title]. I just wanted to let you know that I'm proud of you and you're doing great work."
            the_person "Keep it up! Dinner will be at the normal time."

        elif ran_num == 1:
            the_person "Remember that your mother loves you no matter what! Have a great day!"

        elif ran_num == 2:
            the_person "Hi [the_person.mc_title], I'm just checking in to make sure you're doing okay. I hope you don't mind your mother being concerned about you."

    "It's so sweet of her to think of you."
    $ mc.end_text_convo()
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    return

init 1 python:
    def mom_morning_surprise_requirement():
        if time_of_day != 0 or mom.love < 45:
            return False
        if not mc.business.is_work_day or mc.location != bedroom:
            return False
        return mom.is_available and not mom.has_queued_event("sleeping_walk_in_label")

    morning_crisis_list.append([
        Action("Mom Morning Surprise", mom_morning_surprise_requirement, "mom_morning_surprise_label"),
        5])

label mom_morning_surprise_label():
    $ the_person = mom
    if not the_person.is_willing(handjob):
        the_person "[the_person.mc_title], it's time to wake up."
        "You're woken up by the gentle voice of your mother. You struggle to open your eyes and find her sitting on the edge of your bed."
        $ the_person.draw_person(position="sitting")
        mc.name "Uh... Huh?"
        the_person "You're normally up by now, but I didn't hear an alarm and I was worried you were going to be late."
        "You roll over and check your phone. It looks like you forgot to set an alarm and you've overslept."
        mc.name "Thanks Mom, you really saved me here."
        $ the_person.change_happiness(3)
        "She smiles and stands up."
        $ the_person.draw_person()
        the_person "There's some breakfast in the kitchen, make sure to grab some before you go flying out the door."
        "You sit up on the side of the bed and stretch, letting out a long yawn."
        if the_person.effective_sluttiness() < 20:
            the_person "Oh... I should... Uh..."
            "[the_person.possessive_title] blushes and turns around suddenly. It takes you a moment to realise why: your morning wood pitching an impressive tent with your underwear."
            mc.name "Sorry Mom, I didn't..."
            the_person "No, it's perfectly natural. I'll give you some privacy."
            $ the_person.change_slut(2, 15)
            "She takes one last glance at you then hurries from the room."
            $ mc.change_locked_clarity(5)
            $ clear_scene()
            "You get up and ready, hurrying a little to make up for lost time."
        else:
            the_person "Oh, and you might want to take care of that before you go out [the_person.mc_title]."
            "She nods towards your crotch and you realise you're pitching an impressive tent."
            mc.name "Oh, sorry about that."
            the_person "No, it's perfectly natural and nothing to be embarrassed about."
            $ the_person.change_slut(2, 25)
            $ mc.change_locked_clarity(5)
            "She stares at it for a short moment before pulling her eyes back up to meet yours."
            the_person "Certainly nothing to be embarrassed about, but I think you should take care of it before you leave."
            "[the_person.possessive_title] turns around and starts rifling through your closet."
            $ the_person.draw_person(position = "walking_away")
            the_person "I'll find you a nice outfit to wear to save you some time. Go ahead [the_person.mc_title], pretend I'm not even here. It's nothing I haven't seen before."
            menu:
                "Masturbate":
                    "You pull your underwear down, grab your hard cock, and start to stroke it."
                    mc.name "Thanks Mom, you're really helping me out this morning."
                    the_person "Anything to help you succeed."
                    $ the_person.draw_person(position = "back_peek")
                    "She wiggles her butt, then turns her attention back to putting together an outfit for you."
                    $ mc.change_locked_clarity(5)
                    "You keep jerking yourself off, pulling yourself closer and closer to orgasm."
                    "You're getting close when [the_person.possessive_title] turns around and walks back towards your bed with a handful of clothes."
                    the_person "I think you'll look really cute in this. Are you almost done [the_person.mc_title]?"
                    menu:
                        "Order her to get on her knees" if the_person.obedience >= 130:
                            mc.name "I'm so close. Get on your knees Mom."
                            the_person "If... if that's what you need to finish."
                            $ the_person.draw_person(position = "blowjob")
                            $ climax_options = []
                            if the_person.obedience >= 140:
                                $ climax_options.append(["Order her to open her mouth","mouth"])
                            else:
                                $ climax_options.append(["Order her to open her mouth\n{color=#ff0000}{size=18}Requires: 140 Obedience{/size}{/color} (disabled)", "mouth"])

                            if the_person.has_large_tits:
                                $ climax_options.append(["Order her to hold up her tits","tits"])

                            $ climax_options.append(["Cum all over her", "body"])
                            $ climax_controller = ClimaxController(*climax_options)
                            $ the_choice = climax_controller.show_climax_menu()
                            if the_choice == "Order her to open her mouth":
                                mc.name "Open your mouth Mom."
                                the_person "[the_person.mc_title], I don't think..."
                                mc.name "I'm so close Mom, open your mouth!"
                                "She hesitates for a split second, then closes her eyes and opens her mouth."
                                $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                "Seeing [the_person.possessive_title] presenting herself for you pushes you past the point of no return."
                                $ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
                                "You slide forward a little, place the tip of your cock on her bottom lip, and start to fire your load into her mouth."
                                $ climax_controller.do_clarity_release(the_person)
                                "[the_person.possessive_title] stays perfectly still while you cum. When you're done you sit back and sigh."
                                if the_person.get_opinion_score("drinking cum") > 0:
                                    $ play_swallow_sound()
                                    "[the_person.title] turns her head away from you, avoiding your eyes as she quietly swallows your cum."
                                    $ mc.change_locked_clarity(10)
                                else:
                                    "[the_person.title] turns away and spits your cum out into her hand. She takes a long while to say anything."
                                the_person "I don't... That wasn't what we should do [the_person.mc_title]."
                                mc.name "You were just being a loving mother and doing what I asked. That was amazing."
                                $ the_person.change_obedience(5)
                                "I... I don't know. Just don't tell anyone, okay?"
                                mc.name "Of course, I promise [the_person.title]."
                                $ the_person.draw_person()
                                "She stands up and heads for the door."
                                the_person "Well hurry up at least and get dressed, I don't want you to be late after all that!"

                            elif the_choice == "Order her to hold up her tits":
                                if the_person.tits_visible:
                                    mc.name "Hold up your tits, I'm going to cum!"
                                    "[the_person.possessive_title] mumbles something but does as she's told. She cups her large breasts in her hands and presents them in front of you."
                                else:
                                    mc.name "Quick, get your tits out [the_person.title]!"
                                    "She seems uncomfortable but is swept along with the urgency of the moment."
                                    if the_person.outfit.can_half_off_to_tits():
                                        $ generalised_strip_description(the_person, the_person.outfit.get_half_off_to_tits_list(), half_off_instead = True, position = "blowjob")
                                    else:
                                        $ generalised_strip_description(the_person, the_person.outfit.get_tit_strip_list(), position = "blowjob")
                                    $ mc.change_locked_clarity(10)
                                    "[the_person.possessive_title] scoops up her large breasts and holds them up, presenting them to you just in time."

                                "You grunt and climax, firing your load out and right onto [the_person.possessive_title]'s chest."
                                $ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "kneeling1")
                                $ climax_controller.do_clarity_release(the_person)
                                the_person "I... Oh [the_person.mc_title], I don't think I should have let you do that."
                                mc.name "It's okay Mom, you were just being a loving mother and doing what I asked."
                                $ the_person.change_obedience(3)
                                "She smiles, seemingly proud of the compliment."
                                the_person "Maybe you're right... Now hurry up and get dressed before you're late!"

                            elif the_choice == "Cum all over her":
                                mc.name "Fuck, here I cum! Stay right there!"
                                "[the_person.title] mumbles something, perhaps a half hearted objection, but turns her head and stays still in front of you."
                                "You grunt and climax, firing your load in an arc over [the_person.possessive_title]'s body."
                                $ climax_controller.do_clarity_release(the_person)
                                "She flinches as the first few drops of cum land on her."
                                $ the_person.change_obedience(2)
                                $ the_person.change_slut(2 + the_person.get_opinion_score("being covered in cum"), 50)
                                $ the_person.discover_opinion("being covered in cum")
                                the_person "Oh! Oh..."
                                "You take a few seconds to catch your breath. [the_person.title] starts to hunt down and wipe at the drops of sperm you've sprinkled all over her."
                                the_person "Maybe that was... going too far."
                                mc.name "I needed it so badly though [the_person.title]. Thank you."
                                $ the_person.draw_person()
                                "She stands up and heads for the door."
                                the_person "You're welcome. Now hurry up and get dressed. I don't want you to be late after all of that!"


                        "Order her to get on her knees\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_person.obedience < 130:
                            pass

                        "Climax":
                            "Knowing that [the_person.possessive_title] is just a step away watching you stroke your cock and waiting for you to cum pushes you over the edge."
                            $ climax_controller = ClimaxController(["Cum!","air"])
                            $ climax_controller.show_climax_menu()
                            "You grunt and climax, firing your load out in an arc. [the_person.title] gasps softly and watches it fly, looks away."
                            $ climax_controller.do_clarity_release(the_person)
                            the_person "Well done. I'll make sure to clean that up while you're out today."
                            $ mc.change_locked_clarity(5)
                            "She leans over and kisses you on the forehead while you're still catching your breath."
                            the_person "Now get dressed or you'll be late for work."
                            $ clear_scene()
                            "[the_person.possessive_title] leaves and you get dressed as quickly as you can manage."

                "Ask her to leave":
                    mc.name "I think it will take care of itself Mom. Thanks for the offer but I can pick out my own outfit."
                    the_person "Oh, okay [the_person.mc_title]. Just make sure don't give any of those nice girls you work with a shock when you walk in."
                    $ the_person.draw_person()
                    $ mc.change_locked_clarity(5)
                    "She turns back to you and gives you a hug and a kiss. Her eyes continue to linger on your crotch."
                    $ clear_scene()
                    "When she leaves you get dressed as quickly as you can, rushing to make up for lost time."


    elif not the_person.is_willing(blowjob) or the_person.has_taboo("sucking_cock"):
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realise you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob") #TODO: We need a handjob pose.
        "[the_person.possessive_title] is sitting on the side of your bed. The covers have been pulled down and she has your morning wood in her hand. She strokes it slowly as she speaks."
        if the_person.has_taboo("touching_penis"):
            the_person "Good morning, don't be embarrassed. I saw your... morning wood, and wanted to help you take care of it."
            "She looks away, blushing intensely."
            the_person "If you want me to stop, just tell me. We never need to talk about this again, okay!"
            the_person "Actually, I should just go. This is a mistake. What am I doing?"
            "[the_person.possessive_title] starts to stand up, but you grab her wrist and pull her back. You guide her hand back to your cock."
            mc.name "It's okay [the_person.title], I was liking it. This is a really nice surprise."
            "She nods happily and speeds up her strokes, settling back down on the bed beside you."
            $ the_person.break_taboo("touching_penis")
        else:
            the_person "Good morning [the_person.mc_title]. You forgot to set an alarm and overslept. I came in to wake you up and saw this..."
            "She speeds up her strokes."
        the_person "I thought that this would be a much nicer way to wake up, and I can't let you leave the house in this condition."
        mc.name "Right, of course. Thanks Mom."
        "You lie back, relax, and enjoy the feeling of your mother's hand caressing your hard shaft."
        the_person "Anything for you [the_person.mc_title], I just want to make sure you're happy and successful."
        "After a few minutes you can feel your orgasm starting to build. [the_person.title] rubs your precum over your shaft and keeps stroking."
        $ climax_options = []
        if the_person.obedience >= 130:
            $ climax_options.append(["Order her to take your cum in her mouth","mouth"])
        else:
            $ climax_options.append(["Order her to take your cum in her mouth\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)","mouth"])

        $ climax_options.append(["Cum!","air"])
        $ climax_controller = ClimaxController(*climax_options)
        $ the_choice = climax_controller.show_climax_menu()
        if the_choice == "Order her to take your cum in her mouth":
            mc.name "I'm almost there Mom, I need to cum in your mouth."
            $ the_person.change_obedience(5)
            "She nods and leans over, stroking your cock faster and faster as she places the tip just inside her mouth."
            $ climax_controller.do_clarity_release(the_person)
            "The soft touch of her lips pushes you over the edge. You gasp and climax, shooting your hot load into [the_person.possessive_title]'s waiting mouth."
            $ the_person.cum_in_mouth()
            if the_person.get_opinion_score("drinking cum") > 0:
                $ play_swallow_sound()
                "[the_person.title] pulls back off of your cock slowly. She turns her head away and discretely swallows your cum."
            else:
                "[the_person.title] pulls back off your cock slowly. She spits your cum out into her hand and straightens up."

        elif the_choice == "Cum!":
            mc.name "I'm almost there Mom, keep going!"
            "She nods and strokes your dick as fast as she can manage, pushing you over the edge."
            $ climax_controller.do_clarity_release(the_person)
            "You grunt and fire your hot load into up into the air. It falls back down onto your stomach and [the_person.possessive_title]'s hand."
            "Mom strokes you slowly for a few seconds, then lets go and places her hand on her lap while you take a second to recover."

        the_person "Whew, that was a lot. I hope that leaves you feeling relaxed for the rest of the day."
        "She leans forward and kisses you on the forehead."
        mc.name "Thanks Mom, you're the best."
        $ the_person.change_love(2)
        $ the_person.change_slut(2, 50)
        $ the_person.change_happiness(5)
        $ the_person.draw_person(position = "back_peek")
        "She smiles and gets up. She pauses before she leaves your room."
        the_person "You better get ready now or you're going to be late!"


    elif not the_person.is_willing(cowgirl) or the_person.has_taboo("vaginal_sex"):
        #TODO: image a lying down blowjob pose
        "You're slowly awoken by a strange, pleasant sensation. When you open your eyes it takes a moment to realise you aren't still dreaming."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(20)
        "[the_person.possessive_title] is lying face down between your legs, gently sucking off your morning wood."
        "She notices you waking up and pulls off of your cock to speak."
        if the_person.has_taboo("sucking_cock"):
            the_person "Don't panic [the_person.mc_title]! I came in because your alarm hadn't gone off and saw this..."
            "She wiggles your dick with her hand."
            the_person "I couldn't stop myself... I mean, I couldn't imagine you having to rush out of the door with this!"
            the_person "I'll stop if you want me too. You probably think I'm crazy!"
            mc.name "I don't think your crazy, I think you are incredibly thoughtful. This feels amazing."
            $ the_person.break_taboo("sucking_cock")
        else:
            the_person "Good morning [the_person.mc_title]. I noticed your alarm hadn't gone off and came in to wake you up..."
            "She licks your shaft absentmindedly."
            the_person "And saw this. I thought this would be a much nicer way of waking you up."
            mc.name "That feels great [the_person.title]."
            $ the_person.change_happiness(5)
        "She smiles up at you, then lifts her head and slides your hard dick back into her mouth."
        "You lie back and enjoy the feeling of [the_person.possessive_title] sucking you off."
        $ the_person.draw_person(position = "blowjob", special_modifier = "blowjob")
        $ mc.change_locked_clarity(20)
        "For several minutes the room is quiet save for a soft slurping sound each time [the_person.title] slides herself down your shaft."
        "You rest a hand on the back of her head as you feel your orgasm start to build, encouraging her to go faster and deeper."
        mc.name "I'm almost there Mom, keep going!"
        "She mumbles out an unintelligible response and keeps sucking your cock."
        $ climax_controller = ClimaxController(["Cum in her mouth!","mouth"])
        $ climax_controller.show_climax_menu()
        "You arch your back and grunt as you climax, firing a shot of cum into [the_person.possessive_title]'s mouth."
        $ the_person.cum_in_mouth()
        $ the_person.draw_person(position = "blowjob")
        $ climax_controller.do_clarity_release(the_person)
        "She pulls back until the tip of your cock is just inside her lips and holds there, collecting each new spurt of semen until you're completely spent."
        "When you're done she pulls up and off, keeping her lips tight to avoid spilling any onto you."
        menu:
            "Order her to swallow" if the_person.obedience >= 130:
                mc.name "That was great [the_person.title], now I want you to swallow."
                $ play_swallow_sound()
                "She looks at you and hesitates for a split second, then you see her throat bob as she sucks down your cum."
                $ the_person.change_obedience(5)
                $ play_swallow_sound()
                "[the_person.possessive_title] takes a second gulp to make sure it's all gone, then opens her mouth and takes a deep breath."


            "Order her to swallow\n{color=#ff0000}{size=18}Requires: 130 Obedience{/size}{/color} (disabled)" if the_person.obedience < 130:
                pass

            "Let her spit it out":
                $ the_person.draw_person(position = "sitting")
                "You watch as she slides her legs off the side of your bed, holds out a hand, and spits your cum out into it."

        the_person "Whew, I'm glad I was able to help with that [the_person.mc_title]. That was a lot more than I was expecting."
        mc.name "Thanks [the_person.title], you're the best."
        $ the_person.change_love(2)
        $ the_person.change_slut(3, 60)
        $ the_person.draw_person()
        "She smiles and leans over to give you a kiss on the forehead."
        the_person "My pleasure, now you should be getting up or you'll be late for work!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] gets up and leaves you alone to get dressed and ready for the day. You rush a little to make up for lost time."
        $ clear_scene()

    else:
        # First we need to take her and remove enough clothing that we can get to her vagina, otherwise none of this stuff makes sense.
        # We do that by getting her lowest level pieces of bottom clothing and removing it, then working our way up until we can use her vagina.
        # This makes sure skirts are kept on (because this is supposed to be a quickly).
        $ removed_something = the_person.outfit.strip_to_vagina()
        "You're woken up by your bed shifting under you and a sudden weight around your waist."
        $ the_person.draw_person(position = "cowgirl", emotion = "happy")
        $ mc.change_locked_clarity(25)
        $ mc.change_arousal(10)
        "[the_person.possessive_title] has pulled down your sheets and underwear and is straddling you. The tip of your morning wood is brushing against her pussy."
        the_person "Good morning [the_person.mc_title]. I didn't hear your alarm go off and when I came to check on you I noticed this..."
        $ mc.change_locked_clarity(5)
        $ mc.change_arousal(10)
        "She grinds her hips back and forth, rubbing your shaft along the lips of her cunt."
        the_person "Would you like me to take care of this for you?"
        menu:
            "Let [the_person.title] fuck you":
                mc.name "That would be great [the_person.title]."
                $ the_person.change_happiness(5)
                $ the_person.change_love(2)
                $ the_person.change_slut(2, 80)
                if the_person.has_taboo("vaginal_sex"):
                    "She teases your tip against her pussy, getting it wet with her juices."
                    the_person "Just this once... Mommy is going to take care of you in a very special way."
                    $ the_person.break_taboo("vaginal_sex")

                $ mc.change_arousal(10)
                "You lie back relax as [the_person.possessive_title] lowers herself down onto your hard cock."
                call fuck_person(the_person, start_position = cowgirl, start_object = bedroom.get_object_with_name("bed"), skip_intro = True, girl_in_charge = True,position_locked=True,self_strip=False) from _call_fuck_person_15
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    $ the_person.change_love(5)
                    the_person "That was amazing [the_person.mc_title], you know how to make me feel like a woman again!"
                    $ the_person.draw_person(position = "missionary")
                    "She rolls over and kisses you, then rests her head on your chest."
                    "After a minute she sighs and starts to get up."
                    $ the_person.draw_person()
                    the_person "I shouldn't be keeping you from your work, I don't want to make you any more late!"
                    "She reaches down to help you up. She smiles at you longingly, eyes lingering on your crotch, and leaves you alone in your room."
                else:
                    the_person "I'm glad I could help [the_person.mc_title]. Now you should hurry up before you're late!"
                    "[the_person.possessive_title] kisses you on the forehead and stands up to leave."
                    $ the_person.draw_person(position = "walking_away")
                    "You get yourself put together and rush to make up for lost time."
                $ the_person.review_outfit()

            "Ask her to get off":
                mc.name "Sorry [the_person.title], but I need to save my energy for later today."
                $ the_person.change_happiness(-3)
                $ the_person.change_obedience(5)
                "She frowns but nods. She swings her leg back over you and stands up."
                $ the_person.draw_person()
                the_person "Of course [the_person.mc_title], if you need me for anything just let me know. I hope you aren't running too late!"
                $ the_person.draw_person(position = "walking_away")
                if removed_something:
                    "[the_person.title] collects some of her discarded clothes from your floor and heads for the door."
                else:
                    "[the_person.title] gives you a kiss on the forehead and heads for the door."
                $ clear_scene()
                "You get up and rush to get ready to make up for lost time."

    $ clear_scene()
    return

init 1 python:
    def lily_new_underwear_requirement():
        if not mc.is_in_bed or lily.love < 30:
            return False
        if lily.has_taboo("underwear_nudity") or lily.effective_sluttiness("underwear_nudity") < 20:
            return False
        if erica.event_triggers_dict.get("insta_pic_intro_complete", False) and day % 7 == 5:
            return False # Erica visits on saturday nights (no new underwear event)
        return True

    def lily_new_underwear_get_underwear(person):
        return Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under")

    crisis_list.append([
        Action("Lily New Underwear Crisis", lily_new_underwear_requirement, "lily_new_underwear_crisis_label"),
        5])

label lily_new_underwear_crisis_label():
    # Lily has some new underwear she wants to demo for you.
    # We base the underwear sluttiness on Lily's sluttiness and use Love+Sluttiness to see if she'll show you as a "full outfit".
    $ the_person = lily #Just so we can keep
    $ the_underwear = lily_new_underwear_get_underwear(the_person)
    if the_underwear is None:
        return #Lily doesn't have any skimpy underwear to show us :(

    $ mc.change_location(bedroom) #Make sure we're in our bedroom.
    if the_person.obedience >= 95:
        "There's a knock at your door."
        the_person "[the_person.mc_title], can I talk to you for a sec?"
        mc.name "Uh, sure. Come in."
        "Your bedroom door opens and [the_person.possessive_title] steps in. She's carrying a shopping bag in one hand."
    else:
        "There's a single knock at your bedroom door before it's opened up. [the_person.possessive_title] steps in, carrying a shopping bag in one hand."

    $ the_person.draw_person(emotion = "happy")
    if the_underwear.underwear_slut_score < 10:
        the_person "This is a little awkward, but I picked up some new underwear at the mall today but I don't know if I like the way it looks."
        the_person "Would you take a look and let me know what you think?"
    elif the_underwear.underwear_slut_score < 20:
        the_person "I was at the mall today and picked up some new underwear. I know Mom would say it's too skimpy, but I wanted a guys opinion."
        $ mc.change_locked_clarity(5)
        the_person "Would you let me try it on and tell me what you think?"
    else:
        the_person "I was at the mall today and picked up some lingerie. I was hoping you'd let me model it for you and tell me what you think."
        $ mc.change_locked_clarity(10)

    menu:
        "Take a look at [the_person.title]'s new underwear":
            "You sit up from your bed and give [the_person.possessive_title] your full attention."
            mc.name "Sure thing, is it in there?"
            "You nod your head towards the bag she is holding."
            the_person "Yeah, I'll go put it on and be back in a second. Don't move!"
            $ clear_scene()
            "[the_person.title] skips out of your room, closing the door behind her."
            $ the_person.apply_outfit(the_underwear)
            "You're left waiting for a few minutes. Finally, your door cracks open and [the_person.title] slips inside."
            $ the_person.draw_person(emotion="happy")
            if the_person.update_outfit_taboos():
                the_person "Oh my god, this is so much more embarrassing than I thought it would be."
                mc.name "Come on [the_person.title], I'm your brother. You can trust me."
                "She takes a deep breath and nods."
                the_person "Yeah, sure. Just don't stare too much, okay?"
                the_person "So, what do you think?"
                mc.name "Turn around, I want to see the other side."
            else:
                the_person "Here we go. What do you think?"
            $ the_person.draw_person(emotion="happy", position = "back_peek")
            "She turns around to give you a good look from behind."
            $ mc.change_locked_clarity(10)
            menu:
                "She looks beautiful": #Raises love
                    mc.name "You look beautiful [the_person.title]. You're a heart stopper."
                    $ the_person.change_love(2)
                    the_person "Aww, you really think so?"

                "She looks sexy": #Raises sluttiness
                    mc.name "You look damn sexy in it [the_person.title]. Like you're just waiting to pounce someone."
                    $ the_person.change_slut(2, 30)
                    the_person "Ooh, I like being sexy. Rawr!"

                "She looks elegant": #Raises obedience
                    mc.name "It makes you look very elegant, [the_person.title]. Like a proper lady."
                    $ the_person.change_obedience(2)
                    the_person "It's not too uptight, is it? Do you think Mom would wear something like this?"

                "You don't like it": #Raises nothing.
                    mc.name "I'm not sure it's a good look on you [the_person.title]."
                    $ the_person.change_happiness(-2)
                    the_person "No? Darn, it was starting to grow on me..."

            "[the_person.title] stands in front of your mirror and poses."
            $ the_person.draw_person(emotion = "happy")
            the_person "Do you think I should keep it? I'm on the fence."
            menu:
                "Keep it":
                    $ the_person.wardrobe.add_underwear_set(the_underwear)
                    mc.name "You should absolutely keep it. It looks fantastic on you."
                    $ the_person.change_happiness(3)
                    "[the_person.title] grins and nods."
                    the_person "You're right, of course you're right. Thank you [the_person.mc_title], you're the best!"


                "Return it":
                    mc.name "I think you have other stuff that looks better."
                    $ the_person.change_obedience(2)
                    the_person "I think you're right, I should save my money and get something better. Thank you [the_person.mc_title], you're the best!"

            $ the_person.change_love(3)
            "[the_person.possessive_title] walks over to you and gives you a hug."
            the_person "Okay, it's getting cold. I'm going to go put some clothes on!"
            $ clear_scene()
            $ the_person.apply_planned_outfit() # make her change back to her normal outfit (for morning crisis events)
            "[the_person.title] slips out into the hall, leaving you alone in your room."


        "Send her away":
            mc.name "Sorry [the_person.title], but I'm busy right now. You'll have to figure out if you like it by yourself."
            the_person "Right, no problem. Have a good night!"
            $ clear_scene()
            "She leaves and closes your door behind her."

    $ clear_scene()
    $ the_underwear = None
    return

init 1 python:
    def lily_morning_encounter_requirement():
        if time_of_day == 0 and day%7 != 5 and mc.is_home: # not on saturday morning
            return lily.is_available and not lily.has_queued_event("sleeping_walk_in_label")
        return False

    morning_crisis_list.append([
        Action("Lily Morning Encounter", lily_morning_encounter_requirement, "lily_morning_encounter_label"),
        5])

label lily_morning_encounter_label():
    python:
        the_person = lily
        comfortable = False
        if the_person.effective_sluttiness() >= 60:
            the_person.apply_outfit(Outfit("Nude"))
        else:
            the_person.apply_outfit(the_person.get_random_appropriate_underwear(guarantee_output = True))

        if the_person.wearing_panties and the_person.wearing_bra:
            comfortable = True
        elif the_person.wearing_bra or the_person.effective_sluttiness("bare_tits") > 40:
            comfortable = True
        elif the_person.wearing_panties or the_person.effective_sluttiness("bare_pussy") > 40:
            comfortable = True
        elif the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) > 40:
            comfortable = True

        mc.change_location(hall)

    "You wake up in the morning to your alarm. You get dressed and leave your room to get some breakfast."
    $ the_person.draw_person()
    if the_person.wearing_panties and the_person.wearing_bra:
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing nothing but her underwear."
        $ mc.change_locked_clarity(5)
    elif the_person.wearing_panties:
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing just a tiny pair of panties."
        $ mc.change_locked_clarity(10)
    elif the_person.wearing_bra:
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, wearing a bra, but surprisingly no panties."
        $ mc.change_locked_clarity(10)
    else:
        $ mc.change_locked_clarity(15)
        "The door to [the_person.possessive_title]'s room opens as you're walking past. She steps out, completely naked."

    if the_person.effective_sluttiness("underwear_nudity") < 10:
        #She's startled and embarrassed.
        "[the_person.title] closes her door behind her, then notices you. She gives a startled yell."
        the_person "Ah! [the_person.mc_title], what are you doing here?"
        "She tries to cover herself with her hands and fumbles with her door handle."
        mc.name "I'm just going to get some breakfast. What are you doing?"
        "[the_person.title] gets her door open and hurries back inside. She leans out so all you can see is her head."
        the_person "I was going to get some laundry and thought you were still asleep. Could you, uh, move along?"
        $ the_person.change_slut(2)
        "You shrug and continue on your way."

    elif comfortable == False:
        "[the_person.title] closes her door behind her, then notices you. She turns and jumps slightly in shock, pressing herself against the door."
        the_person "Sorry [the_person.mc_title], you startled me a bit."
        if the_person.wearing_panties:
            if not the_person.wearing_bra:
                if the_person.has_large_tits:
                    "She moves her hands up to her [the_person.tits_description], covering them, but also creating some impressive cleavage in the process."
                else:
                    "She covers her [the_person.tits_description] with her hands, but leaves the rest of her body exposed to you."
        else:
            if not the_person.wearing_bra:
                "She cups one hand on her pussy while stretching the other arm across her breasts."
                if the_person.has_large_tits:
                    "It doesn't quite get the job done leaving them bulging out above and below her arm."
                else:
                    "This mostly takes care of her front, but her ass is still bare."
            else:
                "She cups one hand on her pussy while she splays the other out over her ass."
        "She is pretty well covered, but the idea of being basically naked leaves her looking a bit uneasy."
        $ mc.change_locked_clarity(5)
        mc.name "Yep, early start today. Are you okay?"
        the_person "I just wasn't expecting to run into anyone in the hall at this time of day."
        mc.name "What are you doing anyway?"
        the_person "I'm just up to get some laundry. I put some in last night."
        "She shifts on her feet and nods down the hall."
        the_person "Go ahead, I don't want to distract you."
        menu:
            "Head to the kitchen":
                mc.name "Well, alright I'm going to go get breakfast if you want to join me when you are more presentable."
                "You start to move down the hall again, but not before seeing her start to blush a bit."
                $ the_person.change_stats(love = 1, happiness = 2)
                the_person "Thanks, I'll see you in a bit."
                "You reach the kitchen and head in to prepare breakfast, hearing her make her way to the laundry room a moment later."
            "Ladies first":
                mc.name "No, I insist, ladies first."
                "You take a step back, making an exaggerated gesture down the hall."
                "She looks at your eye imploringly, but you just smile at her until she sighs in resignation."
                the_person "Fine, have it your way."
                "You let [the_person.title] get a step ahead of you so you can look at her ass, but once she is past she swings her hands back to cover herself."
                $ the_person.draw_person(position = "back_peek")
                "She eyes you warily and her gait is a bit stiff, but you keep up the smile and try to avoid staring too much."
                "The view is pleasant, and as you walk together she seems to relax a bit with the idea of being mostly undressed around you."
                $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)
                $ the_person.draw_person(position = "walking_away")
                "You reach the door to the kitchen and split up. You linger a second and enjoy the view as [the_person.possessive_title] walks away."
                # Make a bad decision?

    elif the_person.effective_sluttiness("underwear_nudity") < 40:
        #She doesn't mind but doesn't think to tease you further
        "[the_person.title] closes her door behind her, then notices you. She turns and smiles."
        the_person "Morning [the_person.mc_title], I didn't think you'd be up yet."
        mc.name "Yep, early start today. What are you up to?"
        if the_person.wearing_panties:
            if not the_person.wearing_bra:
                "She starts to walk alongside you and doesn't seem to mind being topless."
            else:
                "She starts to walk alongside you and doesn't seem to mind being in her underwear."
        else:
            if not the_person.wearing_bra:
                "She starts to walk alongside you and doesn't seem to mind being naked."
            else:
                "She starts to walk alongside you and doesn't seem to mind that she is only wearing a bra."
        $ mc.change_locked_clarity(5)
        $ the_person.update_outfit_taboos()
        the_person "I'm just up to get some laundry. I put some in last night."
        "You let [the_person.title] get a step ahead of you so you can look at her ass."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Compliment her":
                #Bonus love and happiness
                mc.name "Well, I'm glad I ran into you. Seeing you is a pretty good way to start my day."
                $ the_person.change_stats(love = 2, happiness = 5)
                the_person "You're just saying that because you get to see me naked, you perv."
                $ the_person.draw_person(position = "back_peek")
                "She peeks back at you and winks."

            "Slap her ass":
                #Bonus sluttiness and obedience
                mc.name "Did you know you look really cute without any clothes on?"
                $ play_spank_sound()
                "You give her a quick slap on the ass from behind. She yelps and jumps forward a step."
                the_person "Ah! Hey, I'm not dressed like this for you, this is my house too you know."
                "She reaches back and rubs her butt where you spanked it."
                the_person "And ew. I'm your sister, you shouldn't be gawking at me."
                mc.name "I'll stop gawking when you stop shaking that ass."
                $ the_person.draw_person(position = "back_peek")
                the_person "You wish this ass was for you."
                $ mc.change_locked_clarity(5)
                "She spanks herself lightly and winks at you."
                $ the_person.change_stats(obedience = 2, slut = 1, max_slut = 30)

        $ the_person.draw_person(position = "walking_away")
        "You reach the door to the kitchen and split up. You wait a second and enjoy the view as [the_person.possessive_title] walks away."

    else: #sluttiness >= 40-55
        #She likes being watched and teases you a little while you walk together.
        "[the_person.title] closes her door behind her, then notices you."
        the_person "Morning [the_person.mc_title], I was wondering if you were going to be up now."
        mc.name "Yep, early start today. What are you up to?"
        the_person "I was just going to get some laundry out of the machine."
        if the_person.wearing_panties:
            if the_person.wearing_bra:
                "[the_person.possessive_title] thumbs her underwear playfully."
                $ mc.change_locked_clarity(5)
            else:
                "[the_person.possessive_title] cups her breasts playfully."
                $ mc.change_locked_clarity(10)
        else:
            "[the_person.possessive_title] absentmindedly runs her hands over her hips."
            $ mc.change_locked_clarity(10)

        $ the_person.update_outfit_taboos()
        if mom.effective_sluttiness() > 40:
            the_person "I know you like it when I walk around naked and when I'm doing laundry I have an excuse."
        else:
            the_person "I know you like it when I walk around naked but Mom doesn't. At least when I'm doing laundry I have an excuse."
        "You join her as she starts to walk down the hall."
        $ the_person.draw_person(position = "walking_away")
        menu:
            "Grope her as you walk":
                $ play_moan_sound()
                "You reach behind [the_person.title] and grab her ass while she's walking. She moans softly and leans against you."
                if the_person.has_taboo("touching_body"):
                    $ the_person.call_dialogue("touching_body_taboo_break")
                    $ the_person.break_taboo("touching_body")
                else:
                    the_person "[the_person.mc_title], what are you doing? We can't doing anything here..."
                    mc.name "I know, I'm just having a feel. You've got a great ass."
                    $ play_spank_sound()
                    "You spank her butt and she moans again. You work your hand down between her legs from behind and run a finger along her slit."
                    the_person "Fuck, please don't get me too wet. I don't want to have to explain that to Mom if she finds us."
                    "You flick your finger over [the_person.possessive_title]'s clit, then slide your hand back and knead her ass some more."
                    $ mc.change_locked_clarity(20)
                $ the_person.change_stats(love = 2)
                "When you reach the kitchen [the_person.title] reluctantly pulls away from you."

            "Put her hand on your cock as you walk":
                "You take [the_person.title]'s left hand and push it against your crotch."
                if the_person.has_taboo("touching_penis"):
                    the_person "Oh my god, what are you doing!"
                    mc.name "I saw you looking at it, I thought you might be curious. Just give it a feel."
                    the_person "I can't believe you... You just made me touch it like that!"
                    mc.name "You liked it though, didn't you? Come on, let's keep walking."
                    "You hold her hand against your crotch as you walk. She looks away awkwardly, but doesn't try and pull away."
                    mc.name "You can touch it for real, if you want."
                    the_person "You're such a pervert, you know that? Tricking me into this..."
                    "Her hand slides up to your waist, then down under your underwear. She wraps her hand around your shaft and rubs it gently."
                    mc.name "Sure thing [the_person.title], I've really tricked you."
                    $ the_person.break_taboo("touching_penis")
                else:
                    the_person "What are you doing?"
                    mc.name "Look at what you do to me when you walk around like this. You're driving me crazy [the_person.title]."
                    "You let go of her hand but it stays planted on your bulge as you walk."
                    the_person "You're such a pervert, you know that? I can't believe you'd even think about me like that..."
                    "Her hand slides up to your waist, then down under your underwear. She wraps her hand around your shaft and rubs it gently."
                    mc.name "Don't pretend like you don't like it. You're just as horny as I am."
                    the_person "Hey, I'm just doing this for you, okay?"
                    mc.name "Sure thing sis. Keep going."

                $ mc.change_locked_clarity(20)
                $ the_person.change_stats(obedience = 3, slut = 1, max_slut = 30)

                "The two of you walk slowly towards the kitchen as [the_person.possessive_title] fondles your dick."
                "When you reach the door to the kitchen she reluctantly pulls her hand out of your pants."
        if the_person.effective_sluttiness() > 40:
            menu:
                "Follow her" if the_person.effective_sluttiness("bare_pussy") > 40:
                    call lily_morning_encounter_follow_up_one_label(the_person) from _call_from_lily_morning_encounter_label_1
                "Grab her wrist" if mc.business.event_triggers_dict.get("family_threesome", False):
                    call lily_morning_encounter_follow_up_two_label(the_person) from _call_from_lily_morning_encounter_label_2
                "Let her go":
                    $ _return = False

        if _return:
            "Very happy with how your morning has gone so far you head back to your room to start getting ready for the day."
            $ mc.change_location(bedroom)
        else:
            mc.name "Maybe we'll follow up on this later."
            "[the_person.possessive_title]'s face is flush. She nods and heads towards the laundry room. You get to watch her ass shake as she goes."

    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    return

label lily_morning_encounter_follow_up_one_label(the_person):
    $ mc.change_location(laundry_room)
    "Not satisfied to let things go there, you follow her into the laundry room."
    the_person "Oh, [the_person.mc_title] I thought you were going to the kitchen."
    mc.name "I was, but I don't think I can leave you like this in good conscience."
    the_person "That is so sweet, I was worried I would have to take care of myself before I could think about school for the day."
    $ the_person.change_stats(happiness = 5, love = 3)
    if the_person.wearing_panties:
        $ the_person.outfit.strip_to_vagina()
        "As you step towards her she drops her panties off her hips to the floor."
        $ the_person.update_outfit_taboos()
    menu:
        "Continue with your fingers":
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = standing_finger, skip_intro = False) from _call_lily_morning_encounter_laundryfinger

        "Get a taste of her pussy" if not the_person.has_taboo("licking_pussy"):
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = cunnilingus, skip_intro = False) from _call_lily_morning_encounter_laundrylick

        "Fuck her" if not the_person.has_taboo("vaginal_sex"): # only show sex option if you had sex before
            call fuck_person(the_person, private = True, start_object = make_floor(), start_position = missionary, skip_intro = False) from _call_lily_morning_encounter_laundryfuck

    the_person "Thanks bro, now get out of here, so I can do my laundry."
    $ clear_scene()
    $ mc.change_location(kitchen)
    "You walk back to the kitchen to get some breakfast."
    return True

label lily_morning_encounter_follow_up_two_label(the_person):
    python:
        jealous_person = False
        if the_person.sex_record.get("Last Sex Day", 0) < day - 7:
            jealous_person = True
        the_other_person = None
        scene_manager = Scene()
        if renpy.random.randint(0, 1) == 1: # 50% we have a second person (if someone is in the house)
            the_other_person = get_random_from_list(people_in_mc_home(excluded_people = [the_person]))
        jealous_watcher = False
        if the_other_person:
            if the_other_person.effective_sluttiness() < 40:
                the_other_person = None
            elif the_other_person.sex_record.get("Last Sex Day", 0) < day - 7:
                jealous_watcher = True

    "Not satisfied by a little groping you grab [the_person.title] by the wrist and pull her along with you towards the kitchen."
    the_person "Hey, [the_person.mc_title], what do you think you are doing?"
    $ scene_manager.add_actor(the_person, emotion = "angry")
    mc.name "I think we need to continue this before I can go about my day."
    the_person "What, in the kitchen? What about mom?"
    mc.name "She'll have to wait her turn."
    $ mc.change_location(kitchen)
    if the_other_person and renpy.random.randint(0, 1) == 1: #someone is already there 25%
        the_person "I'm serious, what if sh..."
        $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "sitting", emotion = "happy")
        the_other_person "Good morning [the_other_person.mc_title]..."
        if the_other_person.sluttiness < 60:
            the_other_person "... and, [the_person.title], what do you think you are doing walking around naked?"
            the_person "Sorry, [the_other_person.name] I was on my way to get my laundry and [the_person.mc_title] pulled me in here."
        else:
            the_other_person "... and, [the_person.title], walking around naked again I see."
            the_person "Well, since [the_person.mc_title] likes it so much I didn't want to disappoint him."
        the_other_person "Well I can understand that, now [the_other_person.mc_title] what are you doing dragging [the_person.possessive_title] around?"
        mc.name "She got me so excited that I figured she could help me take care of this."
        if jealous_person == True:
            the_other_person "Well, you can hardly blame her for wanting to get your attention."
            if jealous_watcher == True:
                the_other_person "You've been so busy and hardly paid any attention to either of us this week."
                mc.name "Sorry, [the_other_person.title] I don't want you to feel neglected."
                $ scene_manager.update_actor(the_person, emotion = "sad")
                the_person "Hey, I don't want to miss out on quality time with you either."
                mc.name "We could all do something together, that way everyone wins."
            else:
                the_other_person "She mentioned the other day that you've been ignoring her, loneliness can lead to desperation."
                mc.name "I know, I've just been so busy, but I'm ready to remedy that right now."
        else:
            the_other_person "Ah, the insatiability of youth. I sort of miss that."
            if jealous_watcher == True:
                the_other_person "I wouldn't mind some attention myself you know."
                mc.name "Sorry, [the_other_person.title] I can give you my attention now, and let [the_person.title] get on with her day."
                the_person "Yeah, if you want to take care of [the_other_person.name] we can always do something later."
                mc.name "That is very generous of you [the_person.title], but you don't need to leave for me to take care of [the_other_person.title]."
            else:
                the_person "He is just so good, I can't get enough."
                the_other_person "I'll let you two have your fun."
                mc.name "Thanks, [the_other_person.title], but you don't need to be left out."
        the_other_person "What ever will make you happiest [the_other_person.mc_title]."
        the_person "Yeah [the_person.mc_title], tell us what you want to do."
        "It seems like you have full control over what happens next. Who do you want to spend more time with?"
        menu:
            "Just [the_person.title]":
                mc.name "[the_other_person.title] I think I'm just going to focus on [the_person.title], she is the one who started this after all."
                if jealous_watcher == True:
                    the_other_person "If that is what you want to do, just try to make time for me soon too."
                    $ the_other_person.change_stats(happiness = -5, love = -1)
                else:
                    the_other_person "Don't let me get in your way. I'll see you tonight."
                $ scene_manager.remove_actor(the_other_person)
                $ the_other_person = None
            "Just [the_other_person.title]":
                mc.name "Go on, [the_person.title] I'm going to spend some quality time with [the_other_person.title]"
                if jealous_person == True:
                    the_person "Ok, just remember that I'd like to spend time with you soon too."
                    $ the_person.change_stats(happiness = -5, love = -1)
                else:
                    the_person "Ok, you two have fun. I'll see you tonight."
                $ scene_manager.remove_actor(the_person)
                $ the_person = the_other_person
                $ the_other_person = None
            "Both" if willing_to_threesome(the_person, the_other_person):
                mc.name "We're all here, and time as a family is important. [the_person.title] why don't you help me take care of [the_other_person.title]."
                mc.name "First I think there are far too many clothes being worn in this room."
                $ scene_manager.update_actor(the_other_person, position = "stand3")
                $ scene_manager.strip_full_outfit()     # they both undress
                call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen1
                $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                $ scene_manager.update_actor(the_other_person, position = the_person.idle_pose)
                the_person "That's a nice way to start the day, but I have to get my laundry, see you later [the_person.mc_title]."
                $ scene_manager.update_actor(the_person, position = "walking_away")
                the_other_person "Hmm, I also enjoyed that, perhaps we can continue this tonight..."
                $ scene_manager.remove_actor(the_person)
                the_other_person "Anyway, this was fun, but I have to get going too, son."
                mc.name "No problem, see you later, mom."
            "No one":
                mc.name "This is really tempting, but I just remembered something I have to do today."
                mc.name "If I linger I'm going to be late so we'll have to try again another time."
                if jealous_person == True:
                    the_person "Ok, just remember that I'd like to spend time with you soon."
                    $ the_person.change_stats(happiness = -5, love = -1)
                if jealous_watcher == True:
                    the_other_person "If that is what you want to do, just try to make time for me soon."
                    $ the_other_person.change_stats(happiness = -5, love = -1)
                "It isn't easy abandoning the two of them, so you quickly make your way back to your room to get ready for the day."
                $ mc.change_location(bedroom)
        if not the_other_person:
            mc.name "Now get over here [the_person.title]."
            menu:
                "Get a handjob":
                    call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_lily_morning_encounter_handjob_02

                "Force her to her knees" if the_person.is_willing(blowjob):
                    "You open up your pants and take out your hardening member."
                    mc.name "Now show me how good you are at sucking cock."
                    $ the_person.draw_person(position = "kneeling1")
                    "You force her down to her knees, pulling her head closer to your crotch."
                    call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_lily_morning_encounter_kitchenblow

                "Lay her on the table" if the_person.is_willing(missionary):
                    call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = False) from _call_fuck_person_lily_morning_encounter_kitchenfuck

                "Bend her over the table" if the_person.is_willing(spanking):
                    call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = False) from _call_fuck_person_lily_morning_encounter_kitchenspank4

            the_person "Thanks bro, I'm going to do my laundry now."
            $ the_person.draw_person(position = "walking_away")
            "You watch as your sister walks to the laundry room."
    else:
        the_person "Very funny, I'm serious."
        mc.name "So am I, we've certainly done more than let her watch us. I'm sure we can do whatever we want wherever we want."
        the_person "I suppose that is true."
        $ scene_manager.update_actor(the_person, position = "stand2")
        the_person "So, [the_person.mc_title] what do you want to do to [the_person.possessive_title]?"
        menu:
            "Ask for a handjob":
                the_person "Okay... I can do that."
                "[the_person.title] quickly pulls down your shorts, setting your erection free."
                if the_person.has_taboo("touching_penis"):
                    "[the_person.possessive_title] begins to falter a bit. You can sense her hesitation to touch you."
                    the_person "Are you sure... this is okay? I feel like we are really crossing a line here..."
                    mc.name "It's okay. It feels so good, don't you want to make me feel good?"
                    the_person "Yes... of course I want to... I just..."
                    "You take her hand in yours. She looks at you and bites her lip. You slowly move her hand down until your cock is resting in her palm."
                    the_person "Oh my god... it's so... warm..."
                    "Her hand starts to stroke you."
                    $ the_person.break_taboo("touching_penis")
                    $ mc.change_arousal(15)
                else:
                    "[the_person.possessive_title] reaches down and takes a light hold of your erection."
                    the_person "Oh god... I don't know why, but it always surprises me how warm it is..."
                    "Her hand starts to stroke you."
                    $ mc.change_arousal(15)
                call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False, ) from _call_get_fucked_lily_morning_encounter_handjob_01
                mc.name "Thanks sis, I needed that."
                $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                the_person "Anytime bro, I'm off to get my laundry done."
                $ scene_manager.update_actor(the_person, position = "walking_away")
                "You watch your sister as she walks out of the kitchen."

            "Force her to her knees" if the_person.is_willing(blowjob):
                $ scene_manager.update_actor(the_person, position = "kneeling1")
                "You run your hand up her arm to her shoulder and firmly push her down to her knees."
                mc.name "I think you need to get a closer look at the problem, maybe see if you can find a solution."
                "She pulls down your pants allowing your erection to spring free."
                the_person "Wow, [the_person.mc_title], that is certainly a big problem but I think I can handle it."
                $ scene_manager.update_actor(the_person, position = "blowjob")
                "She gently takes you in her hand as she leans in and begins to lick your shaft"
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Suddenly you hear a gasp from the door behind you."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what do you think you are doing?"
                    mc.name "Oh, hey [the_other_person.title] I was just teaching [the_person.title] a lesson for walking around the house naked."
                    if the_other_person.sluttiness < 80:
                        the_other_person "Again? What a little slut, although I have to admit the view is not bad."
                    else:
                        the_other_person "You can hardly blame her, with a body like that I would walk around naked as much as I could."
                    menu:
                        "Invite [the_other_person.title]" if willing_to_threesome(the_person, the_other_person):
                            mc.name "Your body is nothing to be ashamed of [the_other_person.possessive_title], in fact you could join us if you want."
                            the_other_person "That is such a generous offer. I guess I can change my breakfast plans."
                            mc.name "Well then, you are wearing far too many clothes."
                            $ scene_manager.update_actor(the_other_person, position = "stand3")
                            $ scene_manager.strip_full_outfit()
                            call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen2
                            the_person "Wow, that is definitely a good start for day, but I'm off to get my laundry, see you later [the_person.mc_title]."
                            $ scene_manager.update_actor(the_person, position = "walking_away")
                            the_other_person "Indeed, I wouldn't mind doing this on a regular basis."
                            $ scene_manager.remove_actor(the_person)
                            the_other_person "Thank you [the_other_person.mc_title], see you next time."
                            mc.name "No problem, see you later mom."

                        "Continue with [the_person.title]":
                            mc.name "I can't argue with that, do you want to stay and watch?"
                            the_other_person "Well I was going to make breakfast, but I guess a little show with my meal wouldn't hurt."
                            $ scene_manager.update_actor(the_other_person, position = "sitting", emotion = "happy")
                            call mc_sex_request(the_person, the_request = "blowjob") from _call_mc_sex_request_lily_morning_encounter_kitchenblow2
                            $ scene_manager.update_actor(the_person, position = "kneeling1")
                            the_other_person "Thanks for the show, honey."
                            $ scene_manager.update_actor(the_other_person, position = "walking_away")
                            $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                            the_person "Thanks, I'm going to collect my laundry, see you later, bro."
                            $ scene_manager.update_actor(the_person, position = "walking_away")
                            "You watch as your sister scoots off to the laundry room."

                else:
                    mc.name "Don't be shy [the_person.title], I know how much you want this."
                    call fuck_person(the_person, private = True, start_position = blowjob, skip_intro = True, position_locked = True) from _call_lily_morning_encounter_kitchenblow3
                    mc.name "That was great [the_person.title]."
                    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                    the_person "I know, you weren't so bad yourself, bro."
                    the_person "I'm going to get my laundry, see you later."
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    "You watch as your sister walks to the laundry room."

            "Lay her on the table" if the_person.is_willing(missionary): # only show sex option if you had sex before
                $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True)
                $ scene_manager.update_actor(the_person, position = "missionary")
                "Putting your other hand on [the_person.title]'s shoulder you gently guide her to the table and push her back to sit on the top."
                the_person "Oh, [the_person.mc_title] what did you have in mind for me?"
                mc.name "I think you need a good fucking, it is obvious you are horny all the time, walking around naked and teasing me."
                the_person "I can hardly disagree with that, I was hoping something like this would happen."
                "You pull down your pants and step between her legs, slowly running your hard shaft along her wet folds."
                the_person "Mmm, now who is the one teasing."
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Before you can respond you hear a gasp behind you at the kitchen door."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what are you are doing?"
                    mc.name "Oh, hey [the_other_person.title] I was just about to give [the_person.title] a bit of my attention."
                    if the_other_person.sluttiness < 80:
                        the_other_person "Right here in the middle of the kitchen?"
                    else:
                        the_other_person "Getting an early start today aren't you?"
                    mc.name "Sure, no time like the present."
                    if jealous_person == True:
                        the_other_person "Well, you can hardly blame her for wanting to get your attention."
                        if jealous_watcher == True:
                            the_other_person "You've been too busy to make time for either of us this week."
                        else:
                            the_other_person "She mentioned the other day that you've been ignoring her, loneliness can lead to desperation."
                    else:
                        the_other_person "Ah, the insatiability of youth. I sort of miss that."
                        if jealous_watcher == True:
                            the_other_person "I wouldn't mind some attention myself you know."
                        else:
                            $ scene_manager.update_actor(the_other_person, position = "stand2")
                            the_other_person "I'll let you two have your fun."
                            $ scene_manager.remove_actor(the_other_person)

                    $ kitchen_threesome = False # init variable
                    if jealous_watcher == True:
                        mc.name "Sorry, [the_other_person.title] I can give you my attention now, and let [the_person.title] get on with her day."
                        if jealous_person == True:
                            $ scene_manager.update_actor(the_person, emotion = "sad")
                            the_person "Hey, now I don't what to miss out on time with you again."
                            $ kitchen_threesome = True
                        else:
                            the_person "Are you sure?"
                            menu:
                                "Yes":
                                    mc.name "Go on, [the_person.title] I'm going to spend some quality time with [the_other_person.title]."
                                    the_person "Ok, you two have fun. I'll see you tonight."
                                    $ scene_manager.remove_actor(the_person)
                                    $ the_person = the_other_person

                                "No" if willing_to_threesome(the_person, the_other_person):
                                    mc.name "Actually, I think you could help me take care of [the_other_person.title]."
                                    $ kitchen_threesome = True
                    if kitchen_threesome == True:
                        mc.name "Well then, I guess we need to decide who goes first."
                        $ scene_manager.update_actor(the_other_person, position = "stand3", emotion = "happy")
                        $ scene_manager.strip_full_outfit()
                        call start_threesome(the_person, the_other_person, start_position = Threesome_double_down) from _call_lily_morning_encounter_threesome_event_kitchen3
                        $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                        $ scene_manager.update_actor(the_other_person, position = the_person.idle_pose)
                        the_person "Wow, that was just amazing, but I have to get my laundry, see you later [the_person.mc_title]."
                        $ scene_manager.update_actor(the_person, position = "walking_away")
                        the_other_person "Ah, always in a rush that one."
                        $ scene_manager.remove_actor(the_person)
                        the_other_person "Thank you [the_other_person.mc_title], this was fun, but I have to get going too."
                        mc.name "No problem, see you later, mom."
                    else:
                        call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = False) from _call_lily_morning_encounter_kitchenfuck2
                        the_person "Wow, that was fun [the_person.mc_title], but I need to get my laundry."
                        $ scene_manager.update_actor(the_person, position = "walking_away")
                        mc.name "No problem, see you later, sis."
                else:
                    call fuck_person(the_person, private = False, start_position = missionary, start_object = make_table(), skip_intro = True) from _call_lily_morning_encounter_kitchenfuck3
                    the_person "Ah, that was fun [the_person.mc_title], but I need to get some clothes out of the washing machine."
                    $ scene_manager.update_actor(the_person, position = "walking_away")
                    mc.name "No problem, see you later, sis."

            "Bend her over the table" if the_person.is_willing(spanking):
                "Already hard from the teasing in the hallway you waste no time forcing [the_person.title] over to the table."
                $ scene_manager.strip_to_vagina(the_person, visible_enough = True, prefer_half_off = True)
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                "You push her roughly against it and bend her over getting an even better look at her tight ass."
                the_person "Oh, [the_person.mc_title] what are you going to do to me?"
                mc.name "I think it is time to teach you a lesson. If you are going to keep teasing me there will be consequences."
                if the_person.get_opinion_score("being submissive") > 0:
                    the_person "I'm not sure this is the deterrent you think it is, but I'm not complaining."
                else:
                    the_person "I'm not a big fan of punishments [the_person.mc_title]."
                if the_other_person:
                    $ scene_manager.add_actor(the_other_person, display_transform = character_left_flipped, position = "stand4", emotion = "angry")
                    "Just before you bring your hand down on [the_person.title]'s ass you hear a gasp from behind you."
                    the_other_person "[the_other_person.mc_title], [the_person.title] what is going on?"
                    mc.name "Good morning [the_other_person.title], I found this slut walking down the hallway naked and was about to teach her a lesson."
                    the_other_person "She really has been acting out recently, I guess it is time for someone to discipline her."
                    menu:
                        "Send [the_other_person.title] away":
                            mc.name "Exactly, and since you don't seem capable I guess I'll take care of it."
                            mc.name "You can go."
                            the_other_person "Yes, [the_other_person.mc_title]."
                            $ scene_manager.remove_actor(the_other_person)
                            call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = True, position_locked = True) from _call_lily_morning_counter_kitchenspank1

                        "Make [the_other_person.title] stay":
                            mc.name "I know you've been struggling with her discipline, take a seat and I'll show you how it is done."
                            $ scene_manager.update_actor(the_other_person, position = "sitting")
                            the_other_person "Yes, [the_other_person.mc_title]."
                            $ the_other_person.change_obedience(5)
                            call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = True, private = False, position_locked = True) from _call_lily_morning_encounter_kitchenspank2
                            $ scene_manager.update_actor(the_other_person, position = "sitting")
                            $ scene_manager.update_actor(the_person, position = "stand2")
                            mc.name "You see, it isn't that hard, to make her behave."
                            the_other_person "Indeed, I see your point. I will do better from now on."

                        "Punish [the_other_person.title] instead":
                            mc.name "And you've barely done anything about it."
                            mc.name "I think maybe you need to be punished in her place."
                            $ scene_manager.update_actor(the_other_person, position = "stand2", display_transform = character_right)
                            $ scene_manager.update_actor(the_person, position = "sitting", display_transform = character_left_flipped)
                            the_other_person "If you think that is best [the_other_person.mc_title]."
                            $ the_other_person.change_obedience(10)
                            $ scene_manager.strip_to_vagina(the_other_person, visible_enough = True, prefer_half_off = True)
                            call fuck_person(the_other_person, start_position = spanking, start_object = make_table(), skip_intro = False, private = False, position_locked = True) from _call_lily_morning_encounter_kitchenspank3
                            $ scene_manager.draw_scene()
                            mc.name "I hope this has taught you a lesson and that you will take your responsibilities more seriously now."
                            the_person "Yes [the_person.mc_title]."
                            the_other_person "Yes [the_other_person.mc_title], I will try harder."

                else:
                    call fuck_person(the_person, start_position = spanking, start_object = make_table(), skip_intro = True, private = True, position_locked = True) from _call_lily_morning_encounter_kitchenspank

                    the_person "See you next time bro, I'm going to do my laundry now."
                    $ the_person.draw_person(position = "walking_away")
                    "You watch as your sister walks to the laundry room."

    $ the_other_person = None
    $ scene_manager.clear_scene()
    $ scene_manager = None
    return True

init 1 python:
    def family_weekend_breakfast_requirement():
        if time_of_day != 0 or day%7 != 6:
            return False
        return mom.love > 20 and mc.is_home

    morning_crisis_list.append([
        Action("Family Morning Breakfast", family_weekend_breakfast_requirement, "family_morning_breakfast_label"),
        15])

label family_morning_breakfast_label():
    python:
        if mom.effective_sluttiness() > 40:
            mom.apply_outfit(mom.get_random_appropriate_underwear(guarantee_output = True))

        if lily.effective_sluttiness() > 40:
            lily.apply_outfit(lily.get_random_appropriate_underwear(guarantee_output = True))

        #Make sure we're in our bedroom when the event starts.
        mc.change_location(bedroom)
        # initialize scene manager for multi person scene
        scene_manager = Scene()

    "You're woken up in the morning by a knock at your door."
    mc.name "Uh, come in."
    "You groan to yourself and sit up in bed."
    if mom.love > lily.love:
        $ scene_manager.add_actor(mom)
        "[mom.possessive_title] cracks open the door and leans in."
        mom "I'm making some breakfast for you and [lily.fname]. Come on down if you'd like some."
        mc.name "Thanks, [mom.title], I'll be down in a minute."
        $ scene_manager.update_actor(mom, emotion = "happy")
        "She flashes you a smile and closes the door."
        $ scene_manager.hide_actor(mom)
    else:
        $ scene_manager.add_actor(lily)
        "[lily.possessive_title] cracks your door open and leans in. She seems just as tired as you are."
        lily "Hey, I think Mom's making a family breakfast for us."
        mc.name "Thanks for letting me know [lily.title], I'll be down in a minute."
        "She nods and closes your door as she leaves."
        $ scene_manager.hide_actor(lily)

    "You get up, get dressed, and head for the kitchen."
    $ mc.change_location(kitchen)
    $ scene_manager.show_actor(mom, position = "walking_away", display_transform = character_left_flipped)

    if mom.effective_sluttiness() > 40:
        if mom.vagina_visible:
            "[mom.possessive_title] is in front of the stove naked, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(20)
        elif mom.tits_visible:
            "[mom.possessive_title] is standing in front of the stove topless, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(10)
        else:
            "[mom.possessive_title] is just in her underwear in front of the stove, humming as she scrambles a pan full of eggs."
            $ mc.change_locked_clarity(5)
    else:
        "[mom.possessive_title] is at the stove and humming to herself as she scrambles a pan full of eggs."

    $ mom.update_outfit_taboos()
    $ scene_manager.update_actor(mom, position = "back_peek")

    mom "Good morning [mom.mc_title]. I'm almost ready to serve, hopefully [lily.fname] will be here soon."
    lily "I'm coming!"

    $ scene_manager.show_actor(lily)

    if lily.effective_sluttiness() > 40:
        if lily.vagina_visible:
            "[lily.possessive_title] comes into the room naked. She gives a dramatic yawn before sitting down at the kitchen table."
            $ mc.change_locked_clarity(20)
        elif lily.tits_visible:
            "[lily.possessive_title] walks topless into the kitchen, yawning dramatically before sitting down at the table."
            $ mc.change_locked_clarity(10)
        else:
            "[lily.possessive_title] walks into the room only wearing her underwear. She gives a dramatic yawn before sitting down at the kitchen table."
            $ mc.change_locked_clarity(5)
    else:
        "[lily.possessive_title] comes into the room and gives a dramatic yawn before sitting down at the kitchen table."

    $ lily.update_outfit_taboos()
    $ scene_manager.update_actor(lily, position = "sitting")

    if mom.effective_sluttiness() > 40 and lily.effective_sluttiness() > 40:
        #You have breakfast with both of them stripped down like it's no big thing.
        lily "Hope I'm not too late."
        $ scene_manager.update_actor(mom, position = "walking_away")
        "Your mother takes the pan off the stove and begins to slide the contents off onto three plates."
        mom "No, just on time."
        $ scene_manager.update_actor(mom, position = "stand3")
        "She turns around and hands one plate to you and one plate to [lily.title]."
        if mom.lactation_sources > 0 and mom.tits_available:
            mom "Want a little milk for your coffee, honey?"
            "[mom.title] gives you a quick wink."
            mc.name "Sure mom."
            "[mom.possessive_title] bends slightly over your coffee. She takes one of her breasts in her hand and starts to squeeze."
            "It takes a second, but soon a stream of her milk is pouring out into you coffee."
            mom "Just say when!"
            "You let her continue for a few more moments, until you can see the cream start to circulate around your hot coffee."
            $ mom.change_stats(slut = 1, max_slut = 40, happiness = 5)
            mc.name "That's good!"
            lily "Thanks Mom, you're the best!"
        elif lily.lactation_sources > 0 and lily.tits_available:
            mom "Want some coffee, honey?"
            mc.name "Sure mom, [lily.coffee_style], please."
            mom "Here you go, maybe [lily.fname] could help you out with some milk."
            "[mom.title] gives you a quick wink."
            lily "Really, Mom?"
            mc.name "I mean... if you don't mind it would be nice."
            "[lily.possessive_title] gives an exasperated sigh, but then bends slightly over your coffee. She takes one of her breasts in her hand and starts to squeeze."
            "It takes a second, but soon a stream of her milk is pouring out into you coffee."
            lily "Let me know when you have enough."
            "You let her continue for a few more moments, until you can see the cream start to circulate around your hot coffee."
            $ lily.change_stats(slut = 1, max_slut = 40, happiness = 5)
            mc.name "That's good!"
        else:
            lily "Thanks Mom, you're the best!"
        $ scene_manager.update_actor(mom, position = "sitting")
        mom "No problem, I'm just happy to spend my morning relaxing with my two favorite people!"
        "You enjoy a relaxing breakfast bonding with your mother and lily. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "Neither [lily.title] or [mom.possessive_title] seem to think it's strange to relax in their underwear."
        $ mc.change_locked_clarity(10)
        $ lily.change_stats(love = 3)
        $ mom.change_stats(love = 3, happiness = 5)
        if mc.business.event_triggers_dict.get("family_threesome", False):
            "While no one else seems to be bothered by all the skin in the room, it is starting to take a toll on you."
            "You try to focus on something work related, but instead all you can focus on are [mom.possessive_title]'s heaving tits, across the table from you."
            mom "Honey? Are you feeling okay? You seem a little zoned out..."
            "Next to you, [lily.title] notices your erection and speaks up."
            lily "I'm sure he's fine mom, but us walking around like this has him all worked up. He's hard as a rock!"
            "[lily.possessive_title] reaches down and starts to stroke you."
            mom "Oh! I'm so sorry [mom.mc_title], I didn't even think about that. [lily.fname] honey, let's take care of him before the day gets going."
            lily "Good idea mom!"
            menu:
                "Accept their help":
                    mc.name "Oh wow, that would be great!"
                    $ scene_manager.update_actor(mom, position = "stand2")
                    $ scene_manager.update_actor(lily, position = "blowjob")
                    "[mom.possessive_title] gets up and starts walking around the table, while [lily.title] gets on her knees and starts pulling off your pants and underwear."
                    "Your cock springs out of your clothes, nearly smacking [lily.possessive_title] in the face. [mom.title] gets on her knees next to [lily.title]."
                    call start_threesome(lily, mom, start_position = threesome_double_blowjob, position_locked = True) from _threesome_for_breakfast_yum_1
                    $ the_report = _return
                    if the_report.get("guy orgasms", 0) > 0:
                        "You enjoy your post-orgasm bliss for a few moments while [mom.possessive_title] and [lily.possessive_title] get up."
                    else:
                        "Finished for now, you decide to put your cock away while [mom.possessive_title] and [lily.possessive_title] get up."
                    $ scene_manager.update_actor(mom, position="stand3", display_transform = character_center_flipped)
                    $ scene_manager.update_actor(lily, position = "stand4", display_transform = character_right)
                    mc.name "Mmm, thanks for breakfast mom!"
                    if the_report.get("guy orgasms", 0) > 0:
                        "[lily.title] laughs and jokes back."
                        lily "Thanks for breakfast, bro!"
                "Refuse":
                    mc.name "That's okay, I have a ton of stuff to get done today. Maybe tonight after dinner?"
                    mom "Okay, if that's what you want [mom.mc_title]."
                    $ scene_manager.update_actor(mom, position="walking_away", display_transform = character_left_flipped)
                    "[mom.possessive_title] gets up and starts to do the dishes."
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    elif mom.effective_sluttiness() > 40 and not lily.effective_sluttiness() > 40:
        #Lily thinks her mom is embarrassing and weird but Mom pulls rank.
        lily "Oh my god Mom, what are you wearing?"
        $ scene_manager.update_actor(mom, position = "back_peek")
        mom "What? It's the weekend and it's just the three of us. I didn't think anyone would mind if I was a little more casual."
        $ scene_manager.update_actor(lily, position = "sitting")

        if mom.vagina_visible:
            lily "Mom, I don't think you know what casual means. Could you at least put on some panties or something?"
        elif mom.tits_visible:
            lily "Mom, I don't think you know what casual means. I mean, couldn't you at least put on a bra?"
        else:
            lily "Mom, you're prancing around the kitchen in your underwear. In front of your son and daughter. That's weird."
            "[lily.title] looks at you."
            lily "Right [lily.mc_title], that's weird?"

        if mom.obedience > 115:
            $ scene_manager.update_actor(mom, position = "stand3")
            mom "What do you think [mom.mc_title], do you think it's \"weird\" for your mother to want to be comfortable in her own house?"
            $ mc.change_locked_clarity(5)
            menu:
                "Side with Mom":
                    mc.name "I think Mom's right, [lily.title]. It's nothing we haven't seen before, she's just trying to relax on her days off."
                    $ mom.change_obedience(-3)
                    $ lily.change_obedience(3)
                    "[lily.title] looks at the two of you like you're crazy, then sighs dramatically."
                    lily "Fine, but this is really weird, okay?"
                    $ scene_manager.update_actor(mom, position = "sitting")
                    "[mom.possessive_title] dishes out three portions and sits down at the table with you. [lily.title] eventually gets used to her mother's outfit and joins in on your conversation."
                    $ lily.change_slut(2)
                    $ mom.change_happiness(5)


                "Side with [lily.title]":
                    mc.name "I actually think [lily.title] is right, this is a little weird. Could you go put something on, for our sakes?"
                    $ lily.change_stats(obedience = -2, slut = 1, max_slut = 30)
                    $ mom.change_stats(happiness = -10, obedience = 2)
                    mom "Oh you two, you're so silly. Fine, I'll be back in a moment. [lily.fname], could you watch the eggs?"
                    $ scene_manager.hide_actor(mom)
                    $ scene_manager.update_actor(lily, position = "walking_away", display_transform = character_left_flipped)
                    "Your mother leaves to get dressed. [lily.possessive_title] ends up serving out breakfast for all three of you."
                    $ scene_manager.update_actor(lily, position = "sitting")
                    $ mom.apply_outfit(mom.planned_outfit)
                    lily "She's been so weird lately. I don't know what's going on with her..."
                    $ scene_manager.show_actor(mom, position = "sitting", display_transform = character_right)
                    $ lily.change_happiness(5)
                    $ mom.change_happiness(5)
                    "When [mom.possessive_title] gets back she sits down at the table and the three of you enjoy your breakfast together."

        else:
            #She likes what she likes
            mom "Well luckily I'm your mother and it doesn't matter what you think. I'm going to wear what makes me comfortable."
            "She takes the pan off the stove and slides the scrambled eggs out equally onto three plates."
            $ scene_manager.update_actor(mom, position = "stand3")
            mom "Now, would you like some breakfast or not?"
            "[lily.title] sighs dramatically."
            lily "Fine, but this is really weird, okay?"
            $ lily.change_slut(2)
            $ mom.change_happiness(5)
            $ scene_manager.update_actor(mom, position = "sitting")
            "[mom.possessive_title] gives everyone a plate and sits down. [lily.title] eventually gets used to her mother's outfit and joins in on your conversation."
            "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."


    elif lily.effective_sluttiness() > 40 and not mom.effective_sluttiness() > 40:
        # Mom thinks lily is way too underdressed and sends her back to get dressed.
        "Your mother turns around and gasps."
        $ scene_manager.update_actor(mom, position = "stand3", emotion="angry")
        mom "[lily.fname]! What are you wearing?"
        lily "What do you mean? I just got up, I haven't had time to pick out an outfit yet."
        mom "You shouldn't be running around the house naked. Go put some clothes on young lady."
        $ scene_manager.update_actor(lily, emotion = "angry")
        "[lily.possessive_title] scoffs and rolls her eyes."
        lily "Come on Mom, you're being ridiculous. This is my house too, I should be able to wear whatever I want!"
        "[mom.possessive_title] and [lily.fname] lock eyes, engaged in a subtle battle of wills."
        if lily.obedience > mom.obedience:
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = None)
            "[mom.possessive_title] sighs loudly and turns back to the stove."
            mom "Fine! You're so stubborn [lily.fname], I don't know how I survive around here!"
            $ lily.change_stats(obedience = -2, happiness = 5)
            $ mom.change_obedience(10)
            $ scene_manager.update_actor(lily, emotion = "happy")
            "[lily.possessive_title] looks at you, obviously pleased with herself, and winks."

        else:
            "[lily.title] finally sighs loudly and looks away. She pushes her chair back and stands up in defeat."
            $ scene_manager.update_actor(lily, position = "stand4")
            lily "Fine! I'll go put on some stupid clothes so my stupid mother doesn't keep worrying."
            $ scene_manager.update_actor(lily, position = "walking_away")
            "[lily.title] sulks out of the kitchen."
            $ scene_manager.hide_actor(lily)
            $ scene_manager.update_actor(mom, position = "walking_away", emotion = "sad")
            mom "I don't know how I manage to survive with you two around!"
            $ lily.apply_outfit(lily.planned_outfit)
            $ lily.change_stats(obedience = 5, happiness = -5)
            $ mom.change_obedience(-2)
            $ scene_manager.show_actor(lily, position = "sitting")
            "[lily.possessive_title] is back by the time [mom.title] starts to plate breakfast. She sits down and starts to eat without saying anything."
            $ scene_manager.update_actor(mom, position = "sitting")

        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    else:
        # Neither of them are particularly slutty, so it's just a normal breakfast.
        lily "So what's the occasion Mom?"
        $ scene_manager.update_actor(mom, position = "stand3")
        "[mom.possessive_title] takes the pan off the stove and scoops the scrambled eggs out equally onto three waiting plates."
        mom "Nothing special, I just thought we could have a nice quiet weekend breakfast together."
        "She slides one plate in front of you and one plate in front of [lily.possessive_title], then turns around to get her own before sitting down to join you."
        $ scene_manager.update_actor(mom, position = "sitting")
        mom "Go ahead, eat up!"
        $ lily.change_love(3)
        $ mom.change_stats(love = 3, happiness = 5)
        "You enjoy a relaxing breakfast bonding with [mom.title] and [lily.title]. [mom.possessive_title] seems particularly happy she gets to spend time with you."
        "When you're done you help [mom.possessive_title] put the dirty dishes away and get on with your day."

    $ scene_manager.clear_scene()
    return "Advance Time"

init 1 python:
    def morning_shower_requirement():
        return time_of_day == 0 and day%7 != 5 and mc.is_home

    def apply_towel_outfit(person):
        towel_outfit = Outfit("Towel")
        towel_outfit.add_dress(towel.get_copy()) #TODO: Decide if we want a head towel here, maybe just for mom or just for Lily
        person.apply_outfit(towel_outfit)
        return

    morning_crisis_list.append([
        Action("Morning Shower", morning_shower_requirement, "morning_shower_label"),
        5])

label morning_shower_label(): #TODO: make a similar event for your Aunt's place.
    # You wake up and go to take a shower, lily or your mom are already in there.
    "You wake up in the morning uncharacteristically early feeling refreshed and energized. You decide to take an early shower to kickstart the day."
    $ the_person = get_random_from_list(people_in_mc_home() + [None]) #Checks all the rooms in player's home
    if the_person is None or the_person.has_queued_event("sleeping_walk_in_label"):
        #You run into nobody, gain some extra energy. TODO: One of the girls comes to join you.
        "You head to the bathroom and start the shower. You step in and let the water just flow over you, carrying away your worries for the day."
        "After a few long, relaxing minutes it's time to get out. You start the day feeling energized."
        $ mc.change_energy(20)
        return

    "You head to the bathroom, but hear the shower already running inside when you arrive."

    menu:
        "Skip your shower":
            "With the bathroom occupied you decide to get some extra sleep instead."

        "Knock on the door":
            # She says she'll be "out in a minute", or invites you in. Give her a shower outfit.
            "You knock on the door a couple of times and wait for a response."
            if the_person.effective_sluttiness(["bare_tits","bare_pussy"]) > 30:
                the_person "It's open, come on in!"
                $ home_shower.show_background()
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.draw_person(position = "back_peek")
                "You open the door and see [the_person.possessive_title] in the shower."
                call girl_shower_enter(the_person) from _call_girl_shower_enter_1
            else:
                the_person "Just a second!"
                call girl_shower_leave(the_person) from _call_girl_shower_leave_1

        "Peek Inside":
            $ home_shower.show_background()
            $ apply_towel_outfit(the_person)
            $ the_person.draw_person(position = "walking_away")
            "You see [the_person.possessive_title] is standing in front of a mirror, getting ready for a shower, undressing herself."

            $ the_person.strip_outfit(position = "walking_away", exclude_feet = False)

            "Now completely nude, she gets into the shower."
            "You see the water running down her chest."
            $ the_person.draw_person(position = "stand3", emotion = "happy")
            "[the_person.possessive_title] turns around, with the water now going on her back and firm ass."
            if the_person.has_large_tits:
                "You can't help but admire [the_person.possessive_title]'s great body and [the_person.tits_description]."
                "Just as this thought flashes through your mind, she starts rubbing her boobs."
            else:
                "You can't help but admire [the_person.possessive_title]'s slim body and [the_person.tits_description]."
                "Just as this thought flashes through your mind, she starts rubbing her breasts, pinching her small nipples."
            $ mc.change_locked_clarity(10)
            $ the_person.change_arousal(renpy.random.randint(10,50))
            if the_person.effective_sluttiness() >=50 or the_person.get_opinion_score("masturbating") > 0 or the_person.arousal_perc > 35:
                call morning_shower_masturbation() from _call_morning_shower_masturbation_enhanced

            menu:
                "Go Inside":
                    if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) <= 20:
                        $ the_person.draw_person(emotion = "angry")
                        the_person "What the fuck [the_person.mc_title]! Can't you see it's occupied?"
                        mc.name "The door was unlocked, I thought you might have already been finished."
                        the_person "Knock next time, okay? I'll be done in a minute."
                        "She shoos you out of the room, seeming more upset about being interrupted than being seen naked."
                        $ hall.show_background()
                        $ clear_scene()
                        $ the_person.change_stats(love = -2, happiness = -2)
                        call girl_shower_leave(the_person) from _call_girl_shower_leave_4
                    else:
                        "She looks up at you, slightly startled, and turns her body away from you."
                        the_person "Oh, [the_person.mc_title]!"
                        mc.name "I'm just here to have a shower."
                        the_person "I should be finished soon, if you don't mind waiting."
                        $ the_person.update_outfit_taboos()
                        call girl_shower_enter(the_person) from _call_girl_shower_enter_2

                "Walk away":
                    pass

        "Barge in":
            # Locked, unless the girl is slutty enough that you wouldn't mind (TODO: add a "make changes to the house" option where you can't lock the door so you can barge in on lily.)
            if the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) < 10:
                "You try and open the door, but find it locked."
                the_person "One second!"
                call girl_shower_leave(the_person) from _call_girl_shower_leave_2
            elif the_person.effective_sluttiness(["bare_tits", "bare_pussy"]) <= 20:
                $ home_shower.show_background()
                #She's angry that you've barged in on her (but she doesn't mind enough to have locked the door).
                $ the_person.apply_outfit(Outfit("Nude"))
                #$ the_person.outfit = Outfit("Nude") #changed v0.24.1
                $ the_person.draw_person(emotion = "angry")
                $ mc.change_locked_clarity(10)
                "You open the door. [the_person.possessive_title] is standing naked in the shower. She spins around and yells in surprise."
                the_person "[the_person.mc_title]! I'm already in here, what are you doing?"
                mc.name "The door was unlocked, I thought you might have already been finished."
                the_person "Knock next time, okay? I'll be done in a minute."
                "She shoos you out of the room, seeming more upset about being interrupted than being seen naked."
                $ hall.show_background()
                $ clear_scene()
                $ the_person.change_stats(love = -1, slut = 2)
                call girl_shower_leave(the_person) from _call_girl_shower_leave_3
            else:
                $ home_shower.show_background()
                $ the_person.apply_outfit(Outfit("Nude"))
                $ the_person.draw_person(position = "back_peek")
                "You open the door and see [the_person.possessive_title] in the shower."
                "She looks up at you, slightly startled, and turns her body away from you."
                the_person "Oh, [the_person.mc_title]!"
                mc.name "I'm just here to have a shower."
                the_person "I should be finished soon, if you don't mind waiting."
                $ the_person.update_outfit_taboos()
                call girl_shower_enter(the_person) from _call_girl_shower_enter_3

    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    $ clear_scene()
    return

label morning_shower_masturbation():
    "The warmth of the water and her caresses seem to turn [the_person.possessive_title] on."
    $ the_person.draw_person(position = "missionary")
    "She sits on the shower floor, spreads her legs and begins to masturbate with her hand."
    while the_person.arousal_perc < 100:
        $ ran_num = renpy.random.randint(0,4)
        if ran_num == 0:
            $ play_moan_sound()
            "[the_person.possessive_title] rubs her clit and her moans grow louder."
        elif ran_num == 1:
            "As she gets more and more turned on, her hand is moving faster and faster."
        elif ran_num == 2:
            "She pushes three fingers inside, making a deep guttural noise."
            the_person "Ahh, yes. Fuck me hard and deep."
        elif ran_num == 3:
            if the_person.get_opinion_score("anal sex") > 0:
                "She slowly pushes a finger in her rectum..."
                the_person "Mmmm, yes, make me your little anal slut."
            else:
                "[the_person.possessive_title] moves two fingers along her labia, quietly moaning with pleasure."
        else:
            if the_person.get_opinion_score("being submissive") > 0:
                "[the_person.possessive_title] pinches her nipples hard, wincing from excitement and pain."
            else:
                if the_person.has_large_tits:
                    "With one hand she softly squeezes her [the_person.tits_description]."
                else:
                    "With one hand she squeezes her [the_person.tits_description]."
        $ the_person.change_arousal(renpy.random.randint(20,35))
        $ mc.change_locked_clarity(10)
    the_person "Shit, I'm cumming!"
    $ the_person.have_orgasm()
    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
    "You see [the_person.possessive_title]'s body shiver as she reaches orgasm."
    the_person "Wow, that was intense. Need to be quieter or someone might just hear me."
    $ the_person.draw_person(position = "walking_away")
    "She gets up and returns to washing her body."
    "You see her love juices mixing with the water dripping on the floor."
    $ the_person.reset_arousal()
    return

label girl_shower_leave(the_person):
    "After a short pause the shower stops and you hear movement on the other side of the door."
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "The bathroom door opens and [the_person.possessive_title] steps out from the steamy room in a towel."
    $ mc.change_locked_clarity(5)
    if the_person is mom:
        the_person "There you go [the_person.mc_title], go right ahead."
        "She gives you a quick kiss and steps past you."
    else:
        the_person "There, it's all yours. I might have used up all of the hot water."
        "She steps past you and heads to her room."
    return

label girl_shower_enter(the_person):
    menu:
        "Wait and watch her shower":
            "You nod and head to the sink to brush your teeth. You lean on the sink and watch [the_person.title] while you brush."
            if the_person.effective_sluttiness() > 40 - (5 * (the_person.get_opinion_score("showing her tits")+the_person.get_opinion_score("showing her ass"))):
                $ the_person.discover_opinion("showing her tits")
                $ the_person.discover_opinion("showing her ass")
                "She notices you watching, but doesn't seem to mind the attention."
                $ the_person.change_slut(1+(the_person.get_opinion_score("showing her tits")+the_person.get_opinion_score("showing her ass")))
            else:
                the_person "It's strange to shower with someone else in the room."
                mc.name "Nothing to worry about, we're all family here, right?"
                "She shrugs and nods, but you notice she's always trying to shield her body from your view."
                $ the_person.change_slut(1)
                $ the_person.change_obedience(1)
            $ the_person.update_outfit_taboos()
            $ mc.change_locked_clarity(10)
            "Soon enough she's finished. She steps out and grabs a towel, but leaves the shower running for you."

            $ apply_towel_outfit(the_person)
            $ the_person.draw_person()
            the_person "There you go. Enjoy!"
            $ clear_scene()
            "She steps past you and leaves. You get into the shower and enjoy the relaxing water yourself."
            $ mc.change_energy(20)

        "Join her in the shower" if the_person.obedience >= 120:
            mc.name "How about I just jump in, I can get your back and we'll both save some time."
            if the_person.effective_sluttiness() > 40:
                the_person "Sure, if you're okay with that. I will put you to work though."
                "She gives you a warm smile and invites you in with her."
            else:
                the_person "I'm not sure..."
                mc.name "I've got work to get to today, so I'm getting in that shower."
                "[the_person.possessive_title] nods meekly."
                the_person "Okay."

            "You strip down and get in the shower with [the_person.title]. The space isn't very big, so she puts her back to you."
            "You're left with her ass inches from your crotch, and when she leans over to pick up the shampoo she grinds up against you."
            $ mc.change_locked_clarity(20)
            the_person "Oops, sorry about that."
            "Your cock, already swollen, hardens in response, and now even stood up the tip brushes against [the_person.possessive_title]'s ass."
            if the_person.effective_sluttiness("touching_body") <= 40:
                the_person "I think I'm just about done, so you can take care of this..."
                "She wiggles her butt and strokes your tip against her cheeks."
                $ mc.change_locked_clarity(10)
                $ the_person.change_slut(1 + the_person.get_opinion_score("showing her ass"))
                "She steps out of the shower and grabs a towel."
                $ apply_towel_outfit(the_person)
                $ the_person.draw_person()
                the_person "See you next time."
                $ clear_scene()
                "She leaves the room and you finish your shower alone, feeling refreshed by the water."
                $ mc.change_location(bedroom)

            # elif the_person.effective_sluttiness() <= 60: #TODO: Add a "hot dog" position and make it a starting position for this.
            #     "She wiggles her butt and strokes your tip against her cheeks."
            #     the_person "Do you need some help with this? How about you just... use my butt?"
            #     $ the_person.draw_person("walking_away")
            #     "She rubs up against you while you talk, stroking your shaft with her wet, slippery ass."
            #     menu:
            #         "Jerk off with her ass":
            #
            #         "Just have a shower":


            else:
                the_person "What is this?"
                "She wiggles her butt and strokes your tip against her cheeks."
                $ mc.change_locked_clarity(10)
                the_person "Well we need to take care of this, don't we..."
                "She turns around and faces you. It might be the hot water, but her face is flush."
                $ the_person.change_slut(2)
                menu:
                    "Fuck her" if not the_person.has_taboo("vaginal_sex"): # only show sex option if you had sex before
                        $ mc.change_location(home_shower)
                        call fuck_person(the_person, skip_intro = True) from _call_fuck_person_shower_enhanced_1
                        $ the_report = _return

                        $ apply_towel_outfit(the_person)
                        $ the_person.draw_person()
                        "When you're finished [the_person.title] steps out of the shower and grabs a towel. She dries herself off, then wraps herself in it and turns to you."
                        if the_report.get("girl orgasms",0)>0:
                            the_person "Well that's a good way to start the day. See you later."
                        elif the_report.get("guy orgasms",0)>0:
                            the_person "Well I hope you enjoyed your start to the day. See you later."
                        else:
                            the_person "Well maybe we can pick this up some other time. See you later."

                        $ clear_scene()
                        "She leaves the room and you finish your shower alone, feeling refreshed by the water."
                        $ mc.change_location(bedroom)

                    "Just have a shower":
                        mc.name "Maybe some other time, I've got to hurry up though."
                        "She pouts and nods."
                        $ the_person.change_obedience(1)
                        the_person "Alright, up to you."

            $ mc.change_energy(20)


        "Join her in the shower\n{color=#ff0000}{size=18}Requires: 120 Obedience{/size}{/color} (disabled)" if the_person.obedience < 120:
            pass

    return

init 1 python:
    def cousin_tease_crisis_requirement():
        if not mc.phone.has_number(cousin): # she is not yet in the game
            return False
        if cousin.obedience > 150 or cousin.love > 30:
            return False
        if cousin.days_since_event("cousin_text_tease", True) < TIER_2_TIME_DELAY:
            return False

        return cousin.effective_sluttiness() >= 20 and cousin not in mc.location.people

    crisis_list.append([
        Action("Cousin text tease", cousin_tease_crisis_requirement, "cousin_tease_crisis_label"),
        3])

label cousin_tease_crisis_label():
    $ the_person = cousin
    $ mc.start_text_convo(the_person)
    if the_person.effective_sluttiness("underwear_nudity") < 35: #She'll want money

        the_person "I need some cash. Do you have a hundred bucks?"
        menu:
            "Send [the_person.title] some money\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}" if mc.business.has_funds(100):
                $ mc.business.change_funds(-100)
                "You pull up your banking app and send [the_person.possessive_title] some money, then text back."
                mc.name "There you go, sent."
                the_person "Just like that? Well, thanks I guess."
                mc.name "It's just money, I'd rather you were happy."
                $ the_person.change_obedience(-4)
                $ the_person.change_happiness(5)
                $ the_person.change_love(1)
                the_person "Sure thing, nerd."


            "Send [the_person.title] some money\n{color=#ff0000}{size=18}Costs: $100{/size}{/color} (disabled)" if not mc.business.has_funds(100):
                pass

            "Ask why she needs it":
                mc.name "What do you need it for?"
                the_person "Why do you care? Come on, I need some cash quick."
                the_person "Come on you horny perv, I'll give you a picture of my tits if you send me the cash."
                $ the_person.draw_person()
                if the_person.tits_visible:
                    "She sends you a picture, but her tits are already out and on display."
                    $ mc.change_locked_clarity(15)
                    the_person "Fuck, delete that. That wasn't one wasn't for you..."
                    mc.name "No, I think I've gotten everything I want already."
                    $ the_person.change_slut(1, 30)
                    $ the_person.change_obedience(1)
                    "She types, then deletes several messages, but never sends anything else to you."
                else:
                    "She sends you a picture from her phone, obviously trying to tease you a little."
                    $ mc.change_locked_clarity(5)
                    menu:
                        "Send [the_person.title] some money\n{color=#ff0000}{size=18}Costs: $100{/size}{/color}" if mc.business.has_funds(100):
                            $ mc.business.change_funds(-100)
                            "You send her the money from your phone."
                            mc.name "Alright, there's your cash. Whip those girls out for me."
                            the_person "Ugh, I didn't think you'd actually do it."
                            $ the_person.outfit.strip_to_tits(visible_enough = False)
                            $ the_person.draw_person(position = "back_peek")
                            "She sends you a picture, with her back turned to the camera."
                            $ mc.change_locked_clarity(5)
                            the_person "There."
                            mc.name "What the fuck is that, I want to see those tits."
                            the_person "I've already got my cash, so whatever nerd."
                            mc.name "You know I can reverse it within ten minutes, right?"
                            the_person "Fuck. Fine!"
                            $ the_person.draw_person()
                            $ mc.change_locked_clarity(15)
                            the_person "There. Now go jerk off in the bathroom or whatever it is you want to do with that."
                            $ the_person.change_obedience(-2)
                            $ the_person.change_slut(2, 30)

                            menu:
                                "Reverse the payment anyways":
                                    $ mc.business.change_funds(100)
                                    "You don't respond to her, but you do open up your banking app again."
                                    "You flag the recent transfer as \"accidental\" and in a few minutes the money is back in your account."
                                    "It doesn't take long before you get a string of angry texts from [the_person.possessive_title]."
                                    $ the_person.change_love(-5)
                                    $ the_person.change_obedience(-3)
                                    the_person "What the FUCK!"
                                    the_person "Give me my money! We had a deal!"
                                    mc.name "Sorry, but I've already got my pics. Later nerd."
                                    "You have to block her for a few minutes as more angry texts stream in."

                                "Let her keep the money":
                                    "You think about reversing the charges anyways, but decide it's not the best idea if you want to keep this sort of relationship going."
                                    $ the_person.break_taboo("bare_tits")


                        "Send [the_person.title] some money\n{color=#ff0000}{size=18}Costs: $100{/size}{/color} (disabled)" if not mc.business.has_funds(100):
                            pass

                        "Blackmail her for some nudes" if the_person.event_triggers_dict.get("blackmail_level",-1) > 0 and the_person.event_triggers_dict.get("last_blackmailed", -5) + 5 <= day:
                            $ the_person.event_triggers_dict["last_blackmailed"] = day
                            if the_person.event_triggers_dict.get("blackmail_level",1) == 1:
                                mc.name "How about this, you send them over and I don't say anything to your mom about you stealing from my sister."

                            else: #Level 2
                                mc.name "How about this, you send them over and I don't say anything to your mom about your new job."

                            the_person "Oh my god, you little rat. You wouldn't."
                            mc.name "You know I would. Come on, whip those girls out and take some shots for me."
                            $ the_person.outfit.strip_to_tits(visible_enough = False)
                            $ the_person.draw_person()
                            "There's a pause, then [the_person.title] sends you some shots of herself topless."
                            $ mc.change_locked_clarity(15)
                            the_person "There. Satisfied?"
                            if the_person.event_triggers_dict.get("blackmail_level",1) == 2:
                                menu:
                                    "Not yet":
                                        mc.name "Not yet, I want to see those tits shaking. Send me a video."
                                        mc.name "Just imagine I slid a twenty down your g-string and you're giving me a private dance. You're good at those, right?"
                                        "There's another pause, then [the_person.title] sends you a video."
                                        $ the_person.draw_person(position = "kneeling1", emotion = "angry", the_animation = blowjob_bob, animation_effect_strength = 0.8)
                                        "She's kneeling on her bed. She sighs dramatically, then starts to bounce her body, jiggling her tits up and down."
                                        $ mc.change_locked_clarity(15)
                                        "You watch it through, but feel like she could put some more effort into it."
                                        mc.name "Come on, that was a little pathetic. Smile for me and really give it your all this time."
                                        the_person "You want another video? You're being ridiculous."
                                        mc.name "You know the deal. Get to work."
                                        "There's yet another pause, then another video."
                                        $ the_person.draw_person(position = "kneeling1", emotion = "happy", the_animation = blowjob_bob, animation_effect_strength = 1.0)
                                        if the_person.has_large_tits:
                                            "This time [the_person.title] has a nice, fake smile for you. She bounces herself a little more vigorously and really gets her big tits moving."
                                        else:
                                            "This time [the_person.title] has a nice, fake smile for you."
                                            "She bounces herself a little more vigorously, but there's not much chest for her to shake to shake."
                                        $ mc.change_locked_clarity(15)
                                        the_person "Are you satisfied now, you little perv?"

                                        mc.name "For now. See you around."

                                    "For now":
                                        mc.name "For now, but we'll see how I'm feeling next time I see you."
                                        the_person "Ugh. Please don't remind me."

                            $ the_person.update_outfit_taboos()
                            $ the_person.change_obedience(3)
                            $ the_person.change_slut(2, 30)

                        "Blackmail her for some nudes\nBlackmailed too recently. (disabled)" if the_person.event_triggers_dict.get("blackmail_level",-1) > 0 and the_person.event_triggers_dict.get("last_blackmailed", -5) + 5 > day:
                            pass


                        "Tell her no":
                            mc.name "You think I'd want to pay to see your tits? You should be paying me."
                            $ the_person.change_love(-1)
                            the_person "Whatever, I can make the cash somewhere else."
                            "You don't receive any more messages from her."



            "Tell her no":
                mc.name "For you? Of course not."
                $ the_person.change_obedience(1)
                the_person "Oh my god, you're the worst. Whatever."

    else:
        "Out of the blue, [the_person.possessive_title] sends you a text."
        the_person "Are you at work right now?"
        if mc.is_at_work:
            mc.name "Yeah, why do you care?"
        else:
            mc.name "No. Why do you care?"

        "She sends you a picture."
        $ the_person.apply_outfit(lingerie_wardrobe.get_random_appropriate_outfit(the_person.effective_sluttiness() * 2, the_person.effective_sluttiness() // 2, guarantee_output = True, preferences = WardrobePreference(the_person)))
        $ the_person.draw_person(position = "kneeling1")
        "She's in her bedroom, kneeling on her bed in nothing but some lingerie."
        $ mc.change_locked_clarity(15)
        if the_person.update_outfit_taboos():
            the_person "I can't believe I'm showing this to a pervert like you, but I got a new outfit."
            the_person "Do you like it?"

        else:
            the_person "I got a new outfit. Do you like it?"
        menu:
            "I love it":
                mc.name "Absolutely. Your tits look amazing in it."
                $ the_person.change_love(1)
                $ the_person.change_obedience(-2)
                the_person "You're such a pervert looking at me like that."

            "No":
                mc.name "On you, not really."
                $ the_person.change_love(-1)
                $ the_person.change_obedience(1)
                the_person "You lying little shit. I know you love seeing me like this. You're such a pervert."
        the_person "I bet you're about to blow your load just looking at me, right?"

        if the_person.has_large_tits:
            the_person "Do you want me to take this off and show you my big, soft tits?"
        else:
            the_person "Do you want me to take this off and play with my tits for you?"
        $ mc.change_locked_clarity(10)

        menu:
            "Yes":
                mc.name "Of course I do. Send me some pics."
                $ the_person.change_obedience(-1)
                the_person "I knew you would. I want you to beg me for them."
                mc.name "What?"
                the_person "I want you to beg to see my tits. Come on, you want them, right?"
                menu:
                    "Beg to see her tits":
                        "You think about it for a moment, then give in."
                        mc.name "Fine, I'm begging you to show me your tits."
                        the_person "A little more, please."
                        if the_person.has_large_tits:
                            mc.name "All I want in life is to get a look at those huge tits. I need it so badly."
                        else:
                            mc.name "All I want in life is to get a look at your tits. I need it so badly."
                        $ mc.change_locked_clarity(10)
                        the_person "Close..."
                        mc.name "I'm so turned on, just thinking about your tits. Please [the_person.title], I'm begging you!"
                        $ the_person.change_obedience(-2)
                        $ the_person.change_happiness(5)
                        "You wait eagerly for her response."
                        the_person "Oh my god, I can't believe you're this easy to screw with."
                        mc.name "Whatever, just send me some pics."
                        the_person "You really thought I was going to send those? Ha!"
                        the_person "Talk to you later, nerd."

                    "Refuse":
                        mc.name "Why would I beg just to see those udders? If I wanted to see some attention starved bimbo's tits I can go online."
                        $ the_person.change_slut(1, 50)
                        the_person "Whatever nerd. You probably already blew your load in your pants."
                        "You ignore her and she doesn't message you again."

            "No":
                mc.name "Not right now. I've got other stuff to do."
                the_person "Really? You've got to be kidding me."
                the_person "You don't want to see me spread over this bed, naked and waiting for you?"
                the_person "My poor little pussy just dripping wet, waiting for a big hard cock?"
                the_person "Just beg for it and it's yours. My tight little cunt is all yours."
                $ mc.change_locked_clarity(10)
                menu:
                    "Beg to see her naked":
                        "You think about it for a moment, then give in."
                        mc.name "Fine, I'm begging you [the_person.title], let me see you naked."
                        the_person "I'm not sure I'm convinced. A little more please."
                        mc.name "All I want in life right now is to see you stripped out."
                        the_person "Close..."
                        mc.name "I'm so turned on just thinking about you. Please, I'm begging you!"
                        $ mc.change_locked_clarity(10)
                        $ the_person.change_obedience(-4)
                        $ the_person.change_happiness(8)
                        "You wait eagerly for her response."
                        the_person "Oh my god, I'm taking a picture of this chat. I can't believe how desperate you get."
                        mc.name "What? I don't care, just send me some pics."
                        the_person "You really thought I was going to send anything? Hahahaha!"
                        the_person "Talk to you later, nerd."


                    "Refuse":
                        mc.name "Jesus, you're looking a little desperate there [the_person.title]. I can find attention starved bimbos all over the internet if I wanted one."
                        $ the_person.change_slut(2, 50)
                        the_person "You pathetic little nerd, I bet you've just already blown your load. You should be paying me for this."
                        "You ignore her and she doesn't message you again."


    $ mc.end_text_convo()
    $ the_person.apply_planned_outfit() #Return to her planned outfit.
    $ clear_scene()
    $ the_person.set_event_day("cousin_text_tease")
    return
