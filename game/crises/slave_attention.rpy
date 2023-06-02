## Slave Attention Crisis Mod by Tristimdorion
# One of your slaves feels you are ignoring her and demands some attention
init 3 python:
    def slave_attention_crisis_requirement():
        if time_of_day > 0 and mc.is_home: #She always sends you texts while you're not at home for the middle part of the day
            return any(x for x in known_people_in_the_game() if x.has_role(slave_role) and x.sex_record.get("Last Sex Day", 0) + 10 < day)
        return False

    def get_unhappy_slave():
        return get_random_from_list([x for x in known_people_in_the_game() if x.has_role(slave_role) and x.is_available and x.sex_record.get("Last Sex Day", 0) + 10 < day])

    slave_attention_crisis_action = ActionMod("Slave Needs Attention",slave_attention_crisis_requirement,"slave_attention_crisis_action_label",
        menu_tooltip = "One of your slaves feels you are ignoring her and demands your attention", category="Home", is_crisis = True)


label slave_attention_crisis_action_label():
    $ the_person = get_unhappy_slave()

    # set person for debug purposes
    # $ the_person = lily
    if the_person is None:
        return

    if the_person.sex_record.get("Last Sex Day", 0) > day + 21: # she is very upset
        $ the_person.draw_person(emotion = "angry")
        the_person "[the_person.mc_title]! You have been neglecting your slave, don't you want me to be your slave anymore?"
    else:
        $ the_person.draw_person(emotion = "sad")
        the_person "[the_person.mc_title], you haven't used me for a long time, did I displease you in any way?"

    $ old_location = mc.location
    if not mc.location is dungeon:
        mc.name "Follow me, we need a more appropriate surrounding for this conversation."
        $ mc.change_location(dungeon)

    $ mc.location.show_background()
    $ the_person.draw_person(position = "stand3", emotion = "sad")
    mc.name "Why are you still on your feet, slave?"
    $ the_person.draw_person(position = "kneeling1", emotion = "sad")
    "She quickly realizes her mistake and drops to her knees."

    menu:
        "Comfort her":
            mc.name "I've indeed been very busy, I think you deserve some attention."
            $ the_person.draw_person(position = "kneeling1", emotion = "happy")
            the_person "Thank you [the_person.mc_title], do whatever you please, my body and mind are yours."
            if not (the_person.vagina_visible and the_person.tits_visible):
                mc.name "Take off your clothes."
                "[the_person.possessive_title] stands up and starts to strip down."
                $ the_person.strip_outfit(position = "stand3", emotion = "happy")

            $ mc.change_locked_clarity(20)
            "You decide to put her up against the pillory and..."
            $ the_person.draw_person(position = "against_wall", emotion = "happy")

            menu slave_attention_comfort_menu:
                "Whip her" if mc.energy >= 20:
                    "You take a leather flogger from the wall and start to give [the_person.possessive_title] a good whipping."

                    python:
                        for count in __builtin__.range(1, 11):
                            play_spank_sound()
                            renpy.say(the_person.char, "(Smack " + str(count) + "!!)..."  + (renpy.random.choice(["Ouch!", "Yes!", "Fuck!", "Oh!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal(5)
                            renpy.pause(.8)

                    $ mc.change_stats(arousal = 20, energy = -20)

                    if the_person.arousal_perc >= 100:
                        $ play_spank_sound()
                        the_person "Oh my god, I'm cumming... Aaargh... YES... please [the_person.mc_title], continue abusing my body..."
                        $ the_person.have_orgasm()

                    "Looking at her welted body, you decide what to do next."
                    jump slave_attention_comfort_menu
                "Whip her\n{color=#ff0000}{size=18}Requires at least 20 {image=gui/extra_images/energy_token.png}{/size}{/color} (disabled)" if mc.energy < 20:
                    pass
                "Fuck her" if not the_person.has_taboo("vaginal_sex") and mc.energy >= 40:
                    "You quickly undress and start fucking her right there."

                    # TODO instead of default FUCK_PERSON make custom dialog that fits better.
                    call fuck_person(the_person, start_position = against_wall, start_object = make_pillory(), skip_intro = True, skip_condom = True, position_locked = True) from _call_slave_attention_crisis_2
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        the_person "Thank you [the_person.mc_title], for giving your slave so much pleasure."
                    else:
                        the_person "Please [the_person.mc_title], keep fucking me, I need you inside me so bad."

                    jump slave_attention_comfort_menu

                "Fuck her\n{color=#ff0000}{size=18}Requires at least 40 {image=gui/extra_images/energy_token.png} and had sex{/size}{/color} (disabled)" if mc.energy < 40 or the_person.has_taboo("vaginal_sex"):
                    pass
                "Dildo her" if mc.energy >= 40 and perk_system.has_item_perk("Dildo"):
                    "You pick up one of the bigger dildos from your cabinet."

                    # TODO instead of default FUCK_PERSON make custom dialog that fits better.
                    call fuck_person(the_person, start_position = standing_dildo, start_object = make_pillory(), skip_intro = True, position_locked = True) from _call_slave_attention_crisis_3
                    $ the_report = _return
                    if the_report.get("girl orgasms", 0) > 0:
                        the_person "Oh Master, you can put that thing inside me whenever you want, it made me cum so hard."
                    else:
                        the_person "Please [the_person.mc_title], stick that thing into me, I need to cum so badly."

                    jump slave_attention_comfort_menu
                "Dildo her\n{color=#ff0000}{size=18}Requires at least 40 {image=gui/extra_images/energy_token.png} and dildo{/size}{/color} (disabled)" if mc.energy < 40 or not perk_system.has_item_perk("Dildo"):
                    pass
                "Let her go":
                    mc.name "That's enough for now, you can get dressed."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(position = "stand3")
                    the_person "Thank you Master, for granting your slave this much pleasure."
                    "You just nod, as she quickly scurries out of the room."

        "Release her":
            mc.name "Well, [the_person.title], I don't think this is working out, although I'm not unsatisfied with your performance, this is not working out."
            the_person "Please Master, give me another chance... you can punish me hard if you need to."
            if not the_person.vagina_visible:
                "Pleading she turns around stripping her bottom bare, waiting for your decision."
                $ the_person.strip_outfit(position = "doggy", exclude_upper = True)
            else:
                "She quickly turns around, presenting you her naked bottom, waiting for your decision."
                $ the_person.draw_person(position = "doggy")
            $ mc.change_locked_clarity(10)

            menu:
                "Punish her (keep)":
                    mc.name "Very well, your eagerness to serve me has convinced me, but your insolence has to be punished."
                    mc.name "I'm going to spank your cute ass until it has a nice shade and you will count along."

                    python:
                        for count in __builtin__.range(1, 11):
                            renpy.say(the_person.char, str(count) + "..."  + (renpy.random.choice(["Ouch!", "Fuck!", "Damn!"]) if count%3 == 0 else ""), interact = False)
                            the_person.change_arousal(5)
                            renpy.pause(.8)

                        mc.change_stats(arousal = 20, energy = -20)

                    menu:
                        "Fuck her" if not the_person.has_taboo("vaginal_sex") and mc.energy >= 40:
                            mc.name "And now for the main course."
                            "Without any mercy you decide to fuck her ass hard."
                            call fuck_person(the_person, start_position = doggy_anal, start_object = make_floor(), skip_intro = True, skip_condom = True, position_locked = True) from _call_slave_attention_crisis_1
                            mc.name "That's enough, now get dressed and get out of here, I will call you when I have need for you."
                            $ the_person.apply_planned_outfit()
                            $ the_person.draw_person(position = "stand3")
                            "She quickly puts on her clothes and bows her head."
                            the_person "As you wish, [the_person.mc_title]."
                            $ the_person.change_stats(happiness = 5, obedience = 5)

                        "Fuck her\n{color=#ff0000}{size=18}Requires at least 40{image=gui/extra_images/energy_token.png} and had sex{/size}{/color} (disabled)" if mc.energy < 40 or the_person.has_taboo("vaginal_sex"):
                            pass

                        "Send her away":
                            mc.name "That's enough, now get dressed and get out of here, I will call you when I have need for you."
                            $ the_person.apply_planned_outfit()
                            $ the_person.draw_person(position = "stand3")
                            "She quickly puts on her clothes and bows her head."
                            the_person "As you wish, [the_person.mc_title]."
                            $ the_person.change_stats(happiness = -3, obedience = 3)

                "Release her":
                    mc.name "No, my decision is final, you are hereby released from your slave duties."
                    $ the_person.apply_planned_outfit()
                    $ the_person.draw_person(position = "stand3")
                    "She quickly puts on her clothes and bows her head."
                    the_person "As you wish..."
                    $ slave_release_slave(the_person)
                    "[the_person.title] is no longer your slave and you will need to retrain her if you want to enslave her again."

        "Ignore her":
            mc.name "So you think you can make any demands from me now?"
            the_person "Oh no, [the_person.mc_title], I would never do that... I was just hoping you would use your slave."
            mc.name "Well you thought wrong, get up and get out of here."
            $ the_person.draw_person(position = "walking_away")
            "She quickly jumps to her feet and rushes out of your dungeon."
            $ the_person.change_stats(happiness = -3, obedience = 1)
            the_person "Yes Master, please forgive me..."

    $ clear_scene()
    $ the_person.apply_planned_outfit()
    if old_location != dungeon:
        "You move back to [old_location.formal_name]."
    $ mc.change_location(old_location)
    $ old_location = None
    return
