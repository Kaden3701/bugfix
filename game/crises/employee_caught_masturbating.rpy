###Scene Idea: Caught Masturbating
#
#   In this scene, player is walking by some kind of private room when he hears moaning coming from inside
#   After investigating, player finds NPC masterbating
#   Player choices include walking away and watching
#   If watching, NPC has chance to notice PC watching. If slutty, NPC continues, if not, stops and gets angry
#   If watching, and NPC is slutty, have a chance if we went unnoticed for NPC to call out PC name
#   Give PC option to just continue watching, leave NPC a note saying thanks for the show, or to make self known
#   If make self known trigger sex scene
#
#
###
init 2 python:
    def SB_caught_masturbating_requirement():
        if mc.is_at_work:
            if mc.business.is_open_for_business:
                return any(x for x in mc.business.employee_list if x.energy > 30 and x.effective_sluttiness() > 30 - (5 * x.get_opinion_score("masturbating")))
            if mc.business.is_open_for_internship:
                return any(x for x in mc.business.intern_list if x.energy > 30 and x.effective_sluttiness() > 30 - (5 * x.get_opinion_score("masturbating")))
        return False

    def select_girl_masturbating(excluded = None):
        if mc.business.is_open_for_business:
            return get_random_from_list([x for x in mc.business.employee_list if not x == excluded and x.energy > 30 and x.effective_sluttiness() > 30 - (5 * x.get_opinion_score("masturbating"))])
        if mc.business.is_open_for_internship:
            return get_random_from_list([x for x in mc.business.intern_list if not x == excluded and x.energy > 30 and x.effective_sluttiness() > 30 - (5 * x.get_opinion_score("masturbating"))])
        return None

    SB_caught_masturbating_crisis = ActionMod("Office Masturbation",SB_caught_masturbating_requirement,"SB_caught_masturbating_crisis_label",
        menu_tooltip = "You find an employee masturbating in an empty storage room.", category = "Business", is_crisis = True)

label SB_caught_masturbating_crisis_label():
    $ the_person = select_girl_masturbating()
    if the_person is None:
        # "No one eligible for masturbating!"
        return

    $ the_clothing = the_person.outfit.get_lower_top_layer #Get the very top item of clothing.
    $ the_person_two = select_girl_masturbating(the_person)

    "You decide to take a quick break from what you are doing. You stand up and stretch your legs, and go for a quick walk."
    "While you are walking by an unused storage room, you hear some muffled sounds coming from inside."

    if the_person_two and willing_to_threesome(the_person, the_person_two):
        $ scene_manager = Scene()
        $ the_person.strip_outfit(delay = 0)
        $ the_person_two.strip_outfit(delay = 0)

        $ scene_manager.add_actor(the_person, position = "missionary", display_transform = character_69_bottom)
        $ scene_manager.add_actor(the_person_two, position = "cowgirl", display_transform = character_69_on_top)

        "Looking inside, you see [the_person.title] and [the_person_two.title] eating each other out."
        $ mc.change_locked_clarity(30)

        the_person "Oh yes [the_person_two.title], keep licking me right there, that feels wonderful."
        $ the_person.change_arousal(20)
        the_person_two "Mmm, [the_person.title], you taste great... oh yes, push some fingers in there... ah, yes, right there..."
        $ the_person_two.change_arousal(20)

        "While watching them going at it, you decide what to do next."
        menu:
            "Join them":
                the_person "Hi [the_person_two.mc_title], why don't you join us."
                mc.name "Wait a second [the_person.title], let me take care of that for you."
                "You quickly undress and..."
                call start_threesome(the_person, the_person_two, start_position = Threesome_sixty_nine, start_object = make_table(), position_locked = True, skip_intro = True) from _call_start_threesome_SB_caught_masturbating_crisis_label

                if the_person.energy > 20 and the_person_two.energy > 20:
                    "Once you're finished you quickly get dressed and say goodbye to the girls, who seem determined to continue for a while."
                else:
                    "Once you're finished you quickly get dressed and say goodbye to the girls."

            "Punish them for inappropriate behaviour" if office_punishment.is_active and mc.business.is_open_for_business:
                mc.name "[the_person.title], [the_person_two.title], this is totally inappropriate behaviour during office hours, even when you are on a break."
                mc.name "I don't have any choice but to record you both for disciplinary actions later."
                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                $ the_person_two.add_infraction(Infraction.inappropriate_behaviour_factory())
                $ scene_manager.update_actor(the_person, emotion = "sad")
                the_person "Really? I..."
                $ scene_manager.update_actor(the_person_two, emotion = "sad")
                the_person_two "But [the_person_two.mc_title], we..."
                mc.name "Stop, that's enough, you can finish what you are doing, but my decision stands."
                "You turn around and walk away."

            "Keep walking":
                pass

        $ scene_manager.clear_scene()
        $ mc.location.show_background()
    else:
        "Looking inside, you see [the_person.possessive_title] on all fours, with her back to you, quietly moaning."
        $ the_person.draw_person(position = "doggy")
        the_person "Mmmmmmmfff... oh..."
        $ the_person.change_arousal(50)
        $ the_person.discover_opinion("masturbating")
        if the_person.vagina_visible: #If she is naked below
            $ mc.change_locked_clarity(20)
            "With her pussy on full display, you can see she is masturbating vigorously. Her pink lips glisten with moisture."
        else:
            $ mc.change_locked_clarity(10)
            "While it is kind of hard to see, it appears that [the_person.possessive_title] has one hand in her [the_clothing.name] and is masturbating."

        menu:
            "Watch her masturbate":
                "You shift your weight slightly to get comfortable. The sight of [the_person.possessive_title] brazenly masturbating while at work has you mesmerized."
                the_person "Yes... fuck yes.."
                $ the_person.change_arousal(10)
                "[the_person.possessive_title] continues to moan to herself, lost in whatever fantasy she is masturbating to."
                #Get Caught?
                $ success_chance = 5 * (mc.focus + 1)
                if renpy.random.randint(0,100) < success_chance: #If player does not get caught
                    "[the_person.possessive_title] is breathing heavily. It is clear from how vigorously she is touching herself that she is going to orgasm soon." #TODO finish this
                    if the_person.effective_sluttiness() < 30:   #She's not interested in MC yet...
                        $ fantasy_guy = Person.get_random_male_name()
                        "[the_person.possessive_title] seems really into it. Her back is arched as her hand works its magic on her groin."
                        $ the_person.change_arousal(10)
                        the_person "Mmm, [fantasy_guy], that's it... I wanna be your slut..."
                        $ the_person.change_arousal(10)
                        "Hmm, she must be fantasizing about some other guy. Does she have a boyfriend or something maybe?"
                        the_person "Yes [fantasy_guy]... it feels so good when you do that..."
                        $ the_person.change_arousal(10)
                        "You aren't sure what she is fantasizing about, but she is getting really into it..."
                        "As [the_person.possessive_title] continues to masturbate, you can tell she is getting ready to finish."
                        $ the_person.change_arousal(10)
                        $ mc.change_locked_clarity(20)
                        $ the_person.have_orgasm()
                        "[the_person.possessive_title] whimpers as she cums. Her legs spasm and she gasps for air."
                        $ the_person.change_stats(happiness = 3, slut = 1, max_slut = 30)
                        "You decide to make a quick exit before she has a chance to recover. As quietly as you can, you close the door behind you and head back to your previous work."
                    else:
                        if mc.sex_skills["Oral"] > 4 or the_person.get_opinion_score("getting head") > 0 :    #Reward oral skill, OR if girl loves "getting head" ?
                            the_person "Oh God, [the_person.mc_title], that's it. Eat my pussy!"      #Get a chance to eat her
                            $ the_person.change_arousal(10)
                            $ mc.change_locked_clarity(20)
                            "It seems that [the_person.possessive_title] is fantasizing about you eating her out!"
                            "You decide that this is an opportunity too good to pass up."
                            mc.name "I'd be happy to [the_person.title]."
                            $ the_person.draw_person(position = "missionary")
                            "You startle [the_person.possessive_title] and she quickly turns over on her back."
                            the_person "[the_person.mc_title]? Oh God, how long have you been here?"
                            if the_person.vagina_visible:           #If its available no need to strip.
                                "You drop down on the floor in front of her. With her pussy exposed you waste no time diving right in."
                            else:                                              #Otherwise, strip her down.
                                "You don't bother to reply, instead you begin stripping away anything between you and her delicious pussy."
                                $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "missionary")
                                $ mc.change_locked_clarity(20)
                                "With her pussy finally exposed you waste no time diving right in."
                            $ the_person.break_taboo("bare_pussy")
                            $ the_person.break_taboo("licking_pussy")
                            "Cupping her ass with your hands, you circle your tongue all around her wet, inviting cunt."
                            $ the_person.change_arousal(10)
                            $ mc.change_locked_clarity(5)
                            the_person "Oh [the_person.mc_title], you have no idea how bad I need this."
                            "[the_person.possessive_title] runs her hands through your hair. You bury your nose in her mound and flick your tongue in and out of her slick hole."
                            "You circle her clit a few times with your tongue. You suck it into your mouth roughly a couple of times and then release it, your lips making wet, lewd smacking noises."
                            $ the_person.change_arousal(10)
                            the_person "I am so close... I'm sorry [the_person.mc_title], I'm not going to last much longer."
                            $ mc.change_locked_clarity(5)
                            $ the_person.draw_person(emotion="orgasm", position ="missionary")
                            "You double your efforts, licking, sucking, and teasing every corner of her pleasing slit."
                            $ the_person.change_arousal(10)
                            "[the_person.possessive_title] begins to orgasm convulsively, and she cries out."
                            the_person "Yes [the_person.mc_title]! Yes! Yes! Oh fuck, how do you do that!"
                            $ the_person.have_orgasm()
                            $ the_person.change_stats(obedience = 5, love = 3)
                            $ mc.change_locked_clarity(25)
                            #show screen float_up_screen(["+5 Happiness","+5 Obedience","+2 Core Sluttiness" ],["float_text_yellow","float_text_grey","float_text_pink"])
                            "[the_person.possessive_title] runs her hands through your hair one last time. You get up and give her a kiss, letting her taste herself on your tongue."
                            "You excuse yourself and then head to the bathroom and get cleaned up before returning to your work."
                        else:
                            "[the_person.possessive_title] seems really into it. Her back is arched as her hand works its magic on her groin."  ##TODO: this scene
                            the_person "Mmm, [the_person.mc_title], that's it... I wanna be your slut..."
                            $ the_person.change_arousal(10)
                            "You hear [the_person.possessive_title] mumble your name. She's fantasizing about you! You stay as quiet as possible and continue to watch in amazement."
                            if the_person.get_opinion_score("giving blowjobs") > 0:
                                the_person "Yeah [the_person.mc_title]... that's it... let me suck on that delicious cock... I'll take care of it for you..."
                                "She's fantasizing about sucking you off! Maybe you should pay her a visit later..."
                                $ the_person.discover_opinion("giving blowjobs")
                            elif the_person.get_opinion_score("anal sex") > 0:
                                the_person "Oh god [the_person.mc_title], be careful! It feels so full when you stick it in my ass like that..."
                                "She's fantasizing about you fucking her ass! Maybe you should pay her a visit later..."
                                $ the_person.discover_opinion("anal sex")
                            else:
                                the_person "Yes [the_person.mc_title]... you make me feel so good... I just wanna make you feel good too baby."
                                "Sounds like she is really into you. Maybe you should pay her a visit later..."
                            $ the_person.change_arousal(10)
                            $ mc.change_locked_clarity(20)
                            "[the_person.possessive_title]'s hand continues to work furiously on her pussy. You can tell from her proficiency that she probably does this often."
                            "As [the_person.possessive_title] continues to masturbate, you can tell she is getting ready to finish."
                            $ the_person.change_arousal(10)
                            $ the_person.have_orgasm()
                            "[the_person.possessive_title] whimpers as she cums. Her legs spasm and she gasps for air."
                            $ mc.change_locked_clarity(20)
                            "You back out of the room before she has a chance to recover. You can't believe your good luck, catching an employee masturbating... while thinking of you of all people!"
                            "On your way back to your work, you swing by [the_person.possessive_title]'s desk. You write her a quick note."
                            "Thanks for the show!"
                            "You finish it with your initials and leave it next to her computer monitor."
                            "Half an hour later while you are back at work..."
                            $ mc.start_text_convo(the_person)
                            if the_person.effective_sluttiness() > 60:
                                the_person "Next time join in!!!"
                            else:
                                the_person ";)"
                            $ mc.end_text_convo()

                else: #Player gets caught
                    "Straining to get a better view, for a brief moment you lose your focus. You accidentally drop a pen you were holding onto and it clatters loudly across the floor."
                    "[the_person.possessive_title] immediately stops and looks back at the source of the noise. She immediately locks eyes with you and the realization that she just got caught masturbating at work sinks in."
                    if the_person.effective_sluttiness() < 30: #She is not slutty. 50/50 she runs out of the room apologizing or gets pissed
                        $ the_person.draw_person()
                        "[the_person.possessive_title] quickly stands up."
                        if renpy.random.randint(0,100) < 50 : #She's pissed
                            $ the_person.draw_person(emotion="angry")
                            the_person "What the fuck?!? Were you just standing there watching me? Oh my god..."
                            mc.name "No, I was... I heard a noise... I was just trying to see what it was..."
                            if mc.charisma > 4:    #Charisma check to limit the damage
                                $ the_person.draw_person(emotion="happy")
                                "[the_person.possessive_title] hesitates for a moment, then turns to you."
                                the_person "Okay... I believe you... but still, maybe you could knock or something? You scared the shit out of me!"
                                "It looks like you've managed to convince her."
                                $ the_person.draw_person(position = "walking_away")
                                $ the_person.change_stats(happiness = -2, obedience = -2)
                                "After a quick apology, [the_person.possessive_title] excuses herself. You see her head into the women's restroom. You decide it would be a bad idea to try and follow her there."
                                "You finish up your walk and return back to your previous work."
                            else:
                                the_person "I know I shouldn't have been... but you shouldn't just... UGH!!!"
                                $ the_person.draw_person(position = "walking_away")
                                "[the_person.possessive_title] storms off. While the situation was awkward, it left a bit of tension in the air..."
                                $ the_person.change_stats(happiness = -5, obedience = -5, slut = 1, max_slut = 35)
                                "You finish up your walk and return back to your previous work."
                        else: #She's embarrassed
                            "Mortified, [the_person.possessive_title] makes a run for the door."
                            $ the_person.draw_person(position = "walking_away")
                            the_person "Oh my god... I'm so sorry [the_person.mc_title]. I just couldn't help myself. I won't let this happen again!"
                            "You try to reassure [the_person.possessive_title], but she quickly runs off before you can speak."
                            $ the_person.change_stats(happiness = -5, obedience = 5, slut = 1, max_slut = 35)
                            #show screen float_up_screen(["-5 Happiness","+5 Obedience"],["float_text_yellow","float_text_grey","float_text_pink"])    ###OLD code
                            "You finish up your walk and return back to your previous work."
                    elif the_person.effective_sluttiness() < 60 or not the_person.is_willing(doggy):#She is a bit slutty
                        "[the_person.possessive_title] is stunned. You can see the conflict in her eyes. She just got caught masturbating at work, by her boss of all people."
                        "Sensing her conflict, you decide to give her a bit of encouragement. You reach down and begin to stroke yourself through your slacks."
                        $ the_person.draw_person(position = "missionary")
                        "[the_person.possessive_title] rolls over on her back and continues masturbating."
                        $ the_person.change_arousal(20)
                        if the_person.vagina_visible:
                            "Her delicious pussy on full display, [the_person.possessive_title] increases her pace while closely watching you."
                            $ mc.change_locked_clarity(20)
                            $ the_person.break_taboo("bare_pussy")
                        else:
                            $ mc.change_locked_clarity(10)
                            "[the_person.possessive_title] has her hand in her [the_clothing.name]. Her movements get faster while closely watching you."
                        the_person "Oh my god. [the_person.mc_title], I can't believe this is happening..."
                        if the_person.get_opinion_score("public sex") > 0:
                            "[the_person.possessive_title]'s cheeks are flush with arousal. Her eyes stare straight into yours as she continues to touch herself."
                            the_person "Does it excite you, [the_person.mc_title]? To see me here, touching myself like this...?"
                            "You can tell she likes having an audience."
                            mc.name "Of course, [the_person.title]. And you like having someone here to watch you, don't you?"
                            $ play_moan_sound()
                            "[the_person.possessive_title] doesn't respond with words, but moans at your words. It is clear she enjoys when others watch her doing sexual things..."
                            $ the_person.discover_opinion("public sex")
                        else :
                            "[the_person.possessive_title]'s cheeks are flush with arousal. She closes her eyes and concentrates on whatever fantasy she is lost in."
                            "Her breathing gets ragged as she nears the finish line."
                        $ the_person.change_arousal(20)
                        the_person "Oh fuck... I'm gonna cum!"
                        $ the_person.draw_person(emotion="orgasm", position ="missionary")
                        $ mc.change_locked_clarity(20)
                        $ the_person.have_orgasm()
                        "[the_person.possessive_title] whimpers and her eyes glaze over as she cums. Her legs spasm and she gasps for air."
                        "Catching her breath, [the_person.possessive_title] looks up at you but doesn't say a word. It is clear that masturbating in front of her boss has left a lasting impression."
                        "You decide to give [the_person.possessive_title] a chance to recover. You nod at her and then back out of the room."
                        "You finish up your walk and return back to your previous work."
                    elif the_person.has_anal_fetish:
                        the_person "Oh [the_person.mc_title]! Thank god, I could really use your help here..."
                        if not the_person.vagina_visible:
                            $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "doggy")
                        $ mc.change_locked_clarity(50)
                        $ the_person.break_taboo("bare_pussy")
                        the_person "Could you just like... stick it in my ass for a bit? I'm trying to masturbate but not getting anywhere with it... you know how much I love it in my ass..."
                        menu:
                            "Fuck her ass":  # only show sex option if you had sex before
                                mc.name "Sure, I could spare a few minutes for your ass."
                                "You quickly pull your pants down. [the_person.possessive_title] is wiggling her ass back and forth, waiting for you."
                                "You rub the tip of your penis against [the_person.possessive_title]'s cunt. She is so wet, your cock is soon nicely lubed up."
                                "When you're ready you move your cock up to her back door. With some gentle pressure, you slip into her well exercised hole."
                                call fuck_person(the_person, start_position = doggy_anal, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_sex_sb_event_masturbation_30
                                $ the_report = _return
                                if the_report.get("girl orgasms", 0) > 1:
                                    $ the_person.event_triggers_dict["LastAnalFetish"] = day
                                    "[the_person.possessive_title] is exhausted. She came so hard, it is all she can do to pant and catch her breath."
                                    $ the_person.change_stats(happiness = 5, obedience = 5, slut = 1, max_slut = 60)
                                else:
                                    "[the_person.possessive_title] quickly recovers after you finish."
                                    $ the_person.change_stats(happiness = 3)
                                the_person "Mmm, you always know just what I need [the_person.mc_title]."
                                "You decide to give [the_person.possessive_title] a chance to recover. You make yourself decent, then leave the room, closing the door on the way out."
                                "You finish up your walk and return back to your previous work."

                            "Just watch":
                                mc.name "I'm afraid I can't right now, but that's okay, I'm definitely enjoying the view."
                                "She looks back at you. You can see the hunger in her eyes."
                                the_person "Ok [the_person.mc_title], but if you change your mind..."
                                "[the_person.possessive_title] continues rubbing her exposed pussy. Once in a while she peeks back at you to see if you are still watching."
                                $ the_person.change_arousal(20)
                                $ mc.change_locked_clarity(10)

                                if the_person.get_opinion_score("public sex") > 0:
                                    "[the_person.possessive_title]'s cheeks are flush with arousal. She peeks back and stares straight into your eyes as she continues to touch herself."
                                    the_person "Does it excite you, [the_person.mc_title]? To see me here, touching myself like this...?"
                                    "You can tell tell she likes having an audience."
                                    mc.name "Of course, [the_person.title]. And you like having someone here to watch you, don't you?"
                                    $ play_moan_sound()
                                    "[the_person.possessive_title] moans. It is clear she enjoys when others watch her doing sexual things..."
                                    $ the_person.discover_opinion("public sex")
                                else :
                                    "[the_person.possessive_title]'s cheeks are flush with arousal. She closes her eyes and concentrates on whatever fantasy she is lost in."
                                    "Her breathing gets ragged as she nears the finish line."
                                $ the_person.change_arousal(20)
                                the_person "Oh fuck... I'm gonna cum!"
                                $ mc.change_locked_clarity(20)
                                $ the_person.have_orgasm()
                                "[the_person.possessive_title] whimpers and her eyes glaze over as she cums. Her legs spasm and she gasps for air."
                                "Catching her breath, [the_person.possessive_title] leans forward, leaving her ass up in the air. It is clear that masturbating in front of her boss has left a lasting impression."
                                "You decide to give [the_person.possessive_title] a chance to recover. You nod to her and then back out of the room."
                                "You finish up your walk and return back to your previous work."

                    else: #She is very slutty
                        the_person "Oh [the_person.mc_title]! Thank god, I could really use your help here..."
                        if not the_person.vagina_visible:
                            "[the_person.possessive_title] moves her clothes out of the way."
                            $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "doggy")
                        $ mc.change_locked_clarity(20)
                        $ the_person.break_taboo("bare_pussy")
                        the_person "Could you just give me a little quickie? I'm all warmed up, you could just stick it in right now..."
                        menu:
                            "Fuck her" if the_person.is_willing(doggy): # only show sex option if you had sex before and not locked for any reason
                                mc.name "Sure, I could go for a quick fuck right now."
                                "You quickly pull your pants down. [the_person.possessive_title] is wiggling her ass back and forth, waiting for you."
                                "You rub the tip of your penis against [the_person.possessive_title]'s cunt. She is already soaking wet."
                                "When you're ready you push forward, slipping your shaft deep inside of [the_person.possessive_title]."
                                $ play_moan_sound()
                                "She moans and quivers as you start to pump in and out."
                                call fuck_person(the_person, start_position = doggy, start_object = make_floor(), skip_intro = True, skip_condom = True) from _call_sex_sb_event_masturbation_010
                                $ the_report = _return
                                if the_report.get("girl orgasms", 0) > 1:
                                    "[the_person.possessive_title] is exhausted. She came so hard, it is all she can do to pant and catch her breath."
                                    $ the_person.change_stats(happiness = 5, obedience = 5, slut = 1, max_slut = 80)
                                else:
                                    "[the_person.possessive_title] quickly recovers after you finish."
                                    $ the_person.change_stats(happiness = 3)
                                the_person "Mmmm, thanks, [the_person.mc_title]! That was just what I needed..."
                                "You decide to give [the_person.possessive_title] a chance to recover. You make yourself decent, then leave the room, closing the door on the way out."
                                "You finish up your walk and return back to your previous work."

                            "Just watch":
                                mc.name "I'm afraid I can't right now, but that's okay, I'm definitely enjoying the view."
                                "She looks back at you. You can see the hunger in her eyes."
                                the_person "Ok [the_person.mc_title], but if you change your mind..."
                                "[the_person.possessive_title] continues rubbing her exposed pussy. Once in a while she peeks back at you to see if you are still watching."
                                $ the_person.change_arousal(20)
                                $ mc.change_locked_clarity(10)

                                if the_person.get_opinion_score("public sex") > 0:
                                    "[the_person.possessive_title]'s cheeks are flush with arousal. She peeks back and stares straight into your eyes as she continues to touch herself."
                                    the_person "Does it excite you, [the_person.mc_title]? To see me here, touching myself like this...?"
                                    "You can tell she likes having an audience."
                                    mc.name "Of course, [the_person.title]. And you like having someone here to watch you, don't you?"
                                    $ play_moan_sound()
                                    "[the_person.possessive_title] moans. It is clear she enjoys when others watch her doing sexual things..."
                                    $ the_person.discover_opinion("public sex")
                                else :
                                    "[the_person.possessive_title]'s cheeks are flush with arousal. She closes her eyes and concentrates on whatever fantasy she is lost in."
                                    "Her breathing gets ragged as she nears the finish line."
                                $ the_person.change_arousal(20)
                                the_person "Oh fuck... I'm gonna cum!"
                                $ mc.change_locked_clarity(20)
                                $ the_person.have_orgasm()
                                "[the_person.possessive_title] whimpers and her eyes glaze over as she cums. Her legs spasm and she gasps for air."
                                "Catching her breath, [the_person.possessive_title] leans forward, leaving her ass up in the air. It is clear that masturbating in front of her boss has left a lasting impression."
                                "You decide to give [the_person.possessive_title] a chance to recover. You nod to her and then back out of the room."
                                "You finish up your walk and return back to your previous work."

            "Punish her for inappropriate behaviour" if office_punishment.is_active and mc.business.is_open_for_business:
                mc.name "[the_person.title], this isn't appropriate for the office. I'm going to have to write you up for this."
                the_person "Oh, I... I'm sorry [the_person.mc_title], I didn't think you would care..."
                $ the_person.add_infraction(Infraction.inappropriate_behaviour_factory())
                mc.name "I'm sure you'll have learned your lesson in the future."

            "Keep walking":
                "You decide to give [the_person.possessive_title] some privacy. As quietly as you can, you close the door behind you and continue walking."

        $ the_person.apply_planned_outfit()
        $ mc.location.show_background()
    $ the_clothing = None
    $ the_person_two = None
    $ clear_scene()
    return
