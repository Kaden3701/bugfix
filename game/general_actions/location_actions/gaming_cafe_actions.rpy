init 3 python:
    GUILD_QUEST_MAX_LEVEL = 50
    def gaming_cafe_grind_character_requirement(): # Leave this in
        if day > mc.event_triggers_dict.get("gaming_cafe_grind_day", 9999):
            if gaming_cafe_is_open():
                return True
            else:
                return "Gaming Cafe is Closed!"
        else:
            return "Already played today"
        return False

    def gaming_cafe_buy_max_level_token_requirement():
        if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
            return True
        return False

    def gaming_cafe_adult_swim_requirement():
        if myra_lewd_cafe_open():
            if gaming_cafe_is_open():
                return True
            else:
                return "Gaming Cafe is Closed!"
        return False

    def gaming_cafe_small_grind():  #Baseline 20% chance to increase level, up to 100% chance below level 10.
        if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
            if renpy.random.randint(0,100) < 20 + ((GUILD_QUEST_MAX_LEVEL - gaming_cafe_character_level()) * 2):
                gaming_cafe_increase_character_level()
                return gaming_cafe_character_level()
        return False

    def gaming_cafe_med_grind():    #Baseline 40% chance to increase level, up to 100% chance below level 30.
        if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
            if renpy.random.randint(0,100) < 40 + ((GUILD_QUEST_MAX_LEVEL - gaming_cafe_character_level()) * 3):
                gaming_cafe_increase_character_level()
                return gaming_cafe_character_level()
        return False


    def gaming_cafe_large_grind():
        if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
            gaming_cafe_increase_character_level()
            return gaming_cafe_character_level()
        return False

    def gaming_cafe_increase_character_level():
        mc.event_triggers_dict["guild_quest_level"] = min((mc.event_triggers_dict.get("guild_quest_level", 8) + 1), GUILD_QUEST_MAX_LEVEL) #For not, max level 50
        return

    def gaming_cafe_character_level():
        return mc.event_triggers_dict.get("guild_quest_level", 8)

    # actions available from entry point action
    gaming_cafe_grind_character_action = Action("Play Guild Quest 2 {image=gui/heart/Time_Advance.png}", gaming_cafe_grind_character_requirement, "gaming_cafe_grind_character_label")
    gaming_cafe_buy_max_level_token_action = Action("Buy max level token for Guild Quest 2", gaming_cafe_buy_max_level_token_requirement, "gaming_cafe_buy_max_level_token_label")
    gaming_cafe_adult_swim = Action("Enter Adult Section", gaming_cafe_adult_swim_requirement, "gaming_cafe_adult_swim_label")

label gaming_cafe_grind_character_label():
    $ mc.event_triggers_dict["gaming_cafe_grind_day"] = day
    if alexia.location == gaming_cafe and myra.location == gaming_cafe and myra_will_grind_with_mc():
        call gaming_cafe_grind_with_both from _grind_with_both_girls_gaming_cafe_01
    elif alexia.location == gaming_cafe:
        call gaming_cafe_grind_with_alexia from _grind_with_alexia_01

    elif day%7 in [2,3,4] and myra.location == gaming_cafe:
        $ the_person = myra
        "You decide to play some Guild Quest 2. As you walk into the gaming cafe, you spot [the_person.title] at the counter."
        $ the_person.draw_person()
        mc.name "Hello [the_person.title]."
        the_person "Hey [the_person.mc_title]. Here to play some games?"
        mc.name "Of course. Want to play with me?"
        if myra_will_grind_with_mc():
            the_person "Definitely! I've been wanting to play again with you."
            mc.name "Want an energy drink? I can grab you one."
            the_person "Sure! That sounds great!"
            "You walk away from the counter."
            $ clear_scene()
            call gaming_cafe_grind_with_myra from _grind_with_myra_01
        else:
            the_person "What level are you up to?"
            "You tell her."
            if gaming_cafe_character_level() < 30:
                the_person "Ah. Honestly, I'm pretty busy, and at that level you are still learning the game. Get up to level 30 or so and we'll play!"
                mc.name "Okay. I'm gonna go find a PC. See ya!"
                $ clear_scene()
                "You find an open computer and pay the $5 for your time slot and load up the game. Time to decide what to do!"
                $ mc.business.change_funds(-5)
                call gaming_cafe_grind_solo from _gaming_cafe_grind_solo_01
            else:
                the_person "Oh wow! You've made a lot of progress! I'm down to play some, let me just finishing up a couple things real quick."
                the_person "Go find a PC, I'll be over in a minute."
                mc.name "Sounds good."
                $ clear_scene()
                call gaming_cafe_grind_with_myra_intro from _myra_gaming_intro_01
    else:
        "You decide to play some Guild Quest 2. As you walk into the gaming cafe though, you don't see [myra.possessive_title] at the counter like usual."
        "You find an open computer and pay the $5 for your time slot and load up the game. Time to decide what to do!"
        $ mc.business.change_funds(-5)
        call gaming_cafe_grind_solo from _gaming_cafe_grind_solo_02

    call advance_time from _call_advance_gaming_cafe_grind_advance_01
    return

label gaming_cafe_grind_with_myra():
    $ the_person = myra
    "Before you find a PC, you wander over to the vending machines. You buy [the_person.title] an energy drink."
    "You look around. Everyone around you is staring at a computer screen. If you are careful you can probably slip a serum into her drink..."
    call give_serum(the_person) from _call_give_myra_serum_cafe_01
    "You find a PC and sit down, setting the energy drink at the PC next to you. You log onto the computer, paying your $5 game time fee."
    $ mc.business.change_funds(-5)
    "As you finish loading up the game, [the_person.title] walks over and sits down next to you."
    $ the_person.draw_person(position = "sitting")
    the_person "Yum, thanks for the energy drink!"
    $ the_person.change_happiness(2)
    $ the_person.change_love(1, 50)
    "[the_person.title] logs on to the computer and sips her energy drink."
    the_person "Alright, what are we up to? I'm in the mood for a challenge!"
    menu:
        "Group Dungeon\n{size=18}Gain 60 Energy{/size}" if gaming_cafe_character_level() >= 10:
            mc.name "Let's run a dungeon. I could use the gear."
            the_person "Okay. Let's run with a pug, it will make it more challenging."
            mc.name "Okay."
            "You get a group together and dive into the dungeon. It is tough, but with [the_person.possessive_title] next to you it is easy to communicate."
            "She has a lot of experience on her tank. Each fight, she gathers up huge groups of enemies and balls them up so you can kill them fast with AoEs."
            "[the_person.possessive_title] makes it seem effortless. She chats with you about all kinds of things as you play."
            $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
            $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
            $ text_two = get_topic_text(overhear_topic)
            the_person "... but yeah, I guess you could say I [text_one] [text_two]"
            if the_person.discover_opinion(overhear_topic):
                mc.name "Oh! I didn't realize you felt that way, [the_person.title]."
            "You keep chatting. It is very relaxing to just play for a bit. With [the_person.possessive_title] playing with you, you tear thru a large chunk of content."

            $ mc.change_energy(60)
            $ progress = gaming_cafe_large_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun [the_person.title], but I need to be done."
            the_person "Yeah! Always good practice. Thanks for the runs!"
            "[the_person.possessive_title] seems to be genuine."
            $ the_person.change_happiness(5)
            $ the_person.change_love(2, 80)
        "Group Dungeon\n{color=#ff0000}{size=18}Requires: Level 10 Character{/size}{/color} (disabled)" if gaming_cafe_character_level() < 10:
            pass

        "Raid\n{size=18}Costs 20 Energy{/size}" if myra_will_grind_with_mc() and mc.energy >=20:
            mc.name "Down for a raid?"
            the_person "Fuck yeah I am. Let me put out a message in the guild chat."
            "You get a group together and dive into the raid. It is tough, but with [the_person.possessive_title] next to you it is easy to communicate."
            "She has a lot of experience on her tank, but the raid difficulty is rough. A couple of times someone in the group dies to mechanics"
            "With perseverance though, you soon manage to finish the raid, but it took a lot of effort."
            $ mc.change_energy(-20)
            $ progress = gaming_cafe_large_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
            the_person "Nice! You are really getting better at this game."
            "[the_person.title] looks over at you."
            $ the_person.change_happiness(10)
            $ the_person.change_love(2, 80)
            the_person "You know, it is really nice, to be able to play something with someone like this, you know? I appreciate it."
            mc.name "Don't worry, I'm really enjoying this also."
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun [the_person.title], but I need to be done."
            the_person "Yeah! That was awesome, let's play again soon!"
            "[the_person.possessive_title] seems to be eager to play with you again."

        "Raid\n{color=#ff0000}{size=18}Requires: 20 Energy{/size}{/color} (disabled)" if myra_will_grind_with_mc() and mc.energy <20:
            pass
    $ clear_scene()
    return

label gaming_cafe_grind_with_alexia():
    $ the_person = alexia
    "You decide to play some Guild Quest 2. As you walk into the gaming cafe, you spot [the_person.title] at a computer."
    $ the_person.draw_person(position = "sitting")
    "The seat next to her is open, so you sit down."
    mc.name "Fancy seeing you here, Cupcake."
    the_person "Oh! Hey [the_person.mc_title]. Want to play with me?"
    mc.name "Absolutely. Let me just log on here."
    "You pay the $5 for your time slot and load up the game."
    $ mc.business.change_funds(-5)
    the_person "What do you want to do? I was just doing some overland stuff."
    menu:
        "Overland content\n{size=18}Gain 100 Energy{/size}":
            mc.name "That sounds relaxing to me. I'll join you and we can just take it easy and chat for a bit."
            the_person "Okay!"
            "You load into the game and play some of the easier overland content with [the_person.possessive_title]. You chat about different stuff as you play."
            $ overhear_topic = the_person.get_random_opinion(include_sexy = False)
            $ text_one = person_opinion_to_string(the_person, overhear_topic)[1]
            $ text_two = get_topic_text(overhear_topic)
            the_person "... but yeah, I'm not sure he realizes I [text_one] [text_two]"
            if the_person.discover_opinion(overhear_topic):
                mc.name "Oh! I didn't realize you felt that way, [the_person.title]."
            "You keep chatting. It is very relaxing to just play for a bit. With [the_person.possessive_title] playing with you, you tear thru a large chunk of content."
            $ mc.change_energy(100)
            $ progress = gaming_cafe_med_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
                if progress == 30:
                    "You made it to level 30. Didn't [myra.possessive_title] say she would play with you when you got this far?"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun [the_person.title], but I need to be done."
            the_person "Yeah! I love playing this game, and playing with someone else is always more fun than solo!"
            $ the_person.change_happiness(5)
            $ the_person.change_love(1, 80)
        "Group Dungeon\n{size=18}Gain 60 Energy{/size}" if gaming_cafe_character_level() >= 10:
            mc.name "Let's run a dungeon. I could use the gear."
            the_person "Okay. I don't like to play with randoms, but if you are playing we should be good."
            "You get a group together and dive into the dungeon. It is tough, but with [the_person.possessive_title] next to you it is easy to communicate."
            "She has a lot of experience on her healer, so she manages to keep your group alive throughout the whole thing."
            "It took a lot of effort, but completing the difficult group content makes you feel good."
            $ mc.change_energy(60)
            $ progress = gaming_cafe_large_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
                if progress == 30:
                    "You made it to level 30. Didn't [myra.possessive_title] say she would play with you when you got this far?"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun [the_person.title], but I need to be done."
            the_person "Yeah! That was awesome, and I got a really good piece of gear!"
            "[the_person.possessive_title] seems to be thankful for your help."
            $ the_person.change_happiness(8)
            $ the_person.change_love(1, 80)
            $ the_person.change_obedience(3)
        "Group Dungeon\n{color=#ff0000}{size=18}Requires: Level 10 Character{/size}{/color} (disabled)" if gaming_cafe_character_level() < 10:
            pass

        "Raid\n{size=18}Costs 20 Energy{/size}" if myra_will_grind_with_mc() and mc.energy >=20:
            mc.name "I want to run a raid. They are really fun in this game."
            the_person "Oh... I don't normally like to run those... they are pretty tough..."
            mc.name "Ah, come on, we can do it! You're an awesome healer. There's this one I ran the other day that has really good healer gear."
            the_person "Well okay... we can try..."
            "You get a group together and dive into the raid. It is tough, but with [the_person.possessive_title] next to you it is easy to communicate."
            "She has a lot of experience on her healer, but the raid difficulty is rough. A couple of times the group dies."
            "With perseverance though, you soon manage to finish the raid, but it took a lot of effort."
            $ mc.change_energy(-20)
            $ progress = gaming_cafe_large_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
            the_person "Yes! That is like best in slot!"
            "[the_person.possessive_title] got a good piece of gear. She seems to be really thankful."
            $ the_person.change_happiness(10)
            $ the_person.change_love(1, 80)
            $ the_person.change_obedience(10)
            mc.name "See? Told you we could do it."
            the_person "You're right. Sorry I should have trusted you from the beginning."
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun [the_person.title], but I need to be done."
            the_person "Yeah! That was awesome, and I got a really good piece of gear!"
            "[the_person.possessive_title] seems to be thankful for your help."

        "Raid\n{color=#ff0000}{size=18}Requires: 20 Energy{/size}{/color} (disabled)" if myra_will_grind_with_mc() and mc.energy <20:
            pass
    $ clear_scene()
    return

label gaming_cafe_grind_with_both():
    $ scene_manager = Scene()
    "You decide to play some Guild Quest 2. As you walk into the gaming cafe, you spot [alexia.title] at a computer."
    "You look up, you also notice that [myra.possessive_title] is working at the moment."
    "Maybe they would be willing to play with you?"
    $ scene_manager.add_actor(myra)
    myra "Hey [myra.mc_title]. Here to play some games?"
    mc.name "Of course. I noticed that [alexia.title] is here. I thought maybe we could run something together?"
    myra "I'm down. Things are pretty slow right now."
    mc.name "Alright. Let me go check with her."
    myra "Ok. I'll be over in a minute."
    $ scene_manager.remove_actor(myra)
    "You walk over to [alexia.title]."
    $ scene_manager.add_actor(alexia, position = "sitting")
    mc.name "Hey [alexia.title]."
    alexia "[alexia.mc_title]! Good to see you. Want to play?"
    mc.name "Yeah, actually I think [myra.title] wants to play. Want to play together?"
    alexia "Sure! I need to take a break though, I need to pee and get a drink."
    mc.name "Hey, I'll grab the drink. What do you want?"
    alexia "Oh! A lemonade would be great. Thanks [alexia.mc_title]!"
    mc.name "Sure."
    $ scene_manager.remove_actor(alexia)
    "You head over to the refreshments. You get a lemonade and an energy drink for the girls, and get yourself a water."
    "You have time, you could probably add a serum to their drinks..."
    "You look at [myra.possessive_title]'s energy drink."
    call give_serum(myra) from _call_give_myra_serum_grinding_games_01
    "You look at [alexia.possessive_title]'s lemonade."
    call give_serum(alexia) from _call_give_alexeria_serum_grinding_games_02
    "You walk back over to the game computer that [alexia.possessive_title] was at earlier. You set her lemonade at it, set your water next to it, then [myra.title]'s next to that."
    $ scene_manager.add_actor(myra, display_transform = character_left_flipped)
    myra "Heyyyyy, this for me?"
    mc.name "You bet. [alexia.title] will be right back."
    myra "Great!"
    $ scene_manager.update_actor(myra, position = "sitting")
    "She sits down and starts to log on. You do the same at your computer, paying the usage fee."
    $ mc.business.change_funds(-5)
    $ scene_manager.add_actor(alexia)
    "Soon, [alexia.possessive_title] comes back."
    alexia "Hey! Ohhh yum, thanks [alexia.mc_title]!"
    $ scene_manager.update_actor(alexia, position = "sitting")

    "You decide what you want to do."
    menu:
        "Group Dungeon\n{size=18}Gain 60 Energy{/size}":
            mc.name "Let's run a dungeon. I could use the gear."
            myra "Okay. I've already got all the gear I need from those, but I'll help you guys with one."
            alexia "Thanks [myra.fname]! I actually need some stuff from Hollowfang Lair."
            mc.name "Yeah I think I need that one too."
            "You find a fourth for your dungeon. It is tough, but with [myra.possessive_title] as tank and [alexia.title] as healer, you get through it."
            "It took a lot of effort, but completing the difficult group content makes you feel good."
            $ mc.change_energy(60)
            $ progress = gaming_cafe_large_grind()
            if gaming_cafe_character_level() == GUILD_QUEST_MAX_LEVEL:
                "Your character is max level, but you manage to get some valuable gear."
            elif progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun you two, but I need to be done."
            alexia "Yeah! That was awesome, and I got a really good piece of gear!"
            myra "That is one of the better dungeons. Always good to practice tactics there!"
            "They both seem to have enjoyed the time playing."
            $ alexia.change_happiness(8)
            $ alexia.change_love(1, 80)
            $ alexia.change_obedience(3)
            $ myra.change_happiness(8)
            $ myra.change_love(1, 80)
            $ myra.change_obedience(3)


        "Raid\n{size=18}Costs 20 Energy{/size}" if mc.energy >=20:
            mc.name "I want to run a raid. They are really fun in this game."
            alexia "Oh... I don't normally like to run those... they are pretty tough..."
            myra "Don't worry [alexia.fname]! I'll tank, we'll do great!"
            mc.name "Yeah, you're an awesome healer. There's this one I ran the other day that has really good healer gear."
            alexia "Well okay... we can try..."
            $ alexia.change_obedience(5)
            "You get a group together and dive into the raid. It is tough, but with the girls next to you it is easy to communicate."
            "[myra.title] leads the team, and with [alexia.possessive_title] healing you are able to get through fairly easily."
            "You soon manage to finish the raid, but it took a lot of effort."
            $ mc.change_energy(-20)
            $ progress = gaming_cafe_large_grind()
            if gaming_cafe_character_level() == GUILD_QUEST_MAX_LEVEL:
                "Your character is max level, but you manage to get some valuable gear."
            elif progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
            alexia "Yes! That is like best in slot!"
            "[alexia.possessive_title] got a good piece of gear. She seems to be really thankful."
            $ alexia.change_happiness(10)
            $ alexia.change_love(1, 80)
            $ alexia.change_obedience(10)
            mc.name "See? Told you we could do it."
            myra "Damn right. Nice work too [myra.mc_title], I think you had one of the higher DPS stats in the group."
            $ myra.change_obedience(2)
            $ myra.change_love(1, 80)
            "You notice your ass is starting to get sore from sitting. You look at the clock and realize you have been playing for three hours."
            mc.name "Oh man. This has been fun, but I need to be done."
            "The girls had fun playing."

        "Raid\n{color=#ff0000}{size=18}Requires: 20 Energy{/size}{/color} (disabled)" if mc.energy <20:
            pass
    $ scene_manager.clear_scene()
    return

label gaming_cafe_grind_solo():
    $ progress = False
    menu:
        "Overland content\n{size=18}Gain 100 Energy{/size}":
            "You play some of the game's open world content. You run around with several people, fighting in events and questing."
            "The gameplay is relaxing, and you really enjoy your time playing."
            $ mc.change_energy(100)
            "You make some decent progress on your character after a while."
            $ progress = gaming_cafe_small_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
                if progress == 10:
                    "You get a notice from the game that you have now unlocked group dungeons. You might have to give those a shot next time you play!"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
        "Group Dungeon\n{size=18}Gain 20 Energy{/size}" if gaming_cafe_character_level() >= 10:
            "You decide to play some of the game's group dungeons. You get a group together and dive in."
            "It takes a while to get through it, but you manage to complete a full clear!"
            "It took a lot of effort, but completing the difficult group content makes you feel good."
            $ mc.change_energy(20)
            $ progress = gaming_cafe_med_grind()
            if progress:
                $ prog_string = "You have leveled your character up to level " + str(progress) + "!"
                "[prog_string]"
                if progress == 30:
                    "You made it to level 30. Didn't [myra.possessive_title] say she would play with you when you got this far?"
            else:
                "However, you didn't level up your character any. Guess you still need to grind some more."
        "Group Dungeon\n{color=#ff0000}{size=18}Requires: Level 10 Character{/size}{/color} (disabled)" if gaming_cafe_character_level() < 10:
            pass

    return

label gaming_cafe_grind_with_myra_intro():
    $ the_person = myra
    $ myra.event_triggers_dict["will_grind_with_mc"] = True
    "You find an area with open PC's and sit down. You log in and pay the $5 fee to play a game for a few hours."
    $ mc.business.change_funds(-5)
    "You start Guild Quest 2 and load your character. As you wander around for a bit, looking at your gear, [the_person.possessive_title] wanders over and sits next to you."
    $ the_person.draw_person(position = "sitting")
    "You notice she is carrying an energy drink."
    the_person "Hey! This should be fun!"
    mc.name "Yeah, I know you stay busy but I appreciate you playing with me for a bit."
    "[the_person.title] logs on to the computer and cracks open her energy drink."
    mc.name "I didn't know you liked those. You know I'd be glad to get you one as thanks for playing with me."
    the_person "Hmmm. I suppose it would be okay to charge you a noob tax. Next time I'll take you up on that!"
    "[the_person.possessive_title] logs on to the game, then looks through a couple menus."
    the_person "Hmm... I don't see you online... what was your IGN again?"
    mc.name "Bud Lightyear. And actually, you never did send me that guild invite..."
    the_person "Oh! I'm sorry. Let me do that right now..."
    "In a moment, a prompt comes up with your guild invite. You quickly accept."
    the_person "Alright. Have you ever run Trials of Komalie? It is one of the end game raids, but I think with my help you can handle it."
    mc.name "No, actually I've never done any raids in this game, just the small group dungeons."
    the_person "Oh! You're in for a treat! Let me start getting a group together..."
    "In the in game chat, you see [the_person.possessive_title] put out a call for a raid run to 'train the noob'."
    "You notice multiple people jump at the chance to play with her. She must be pretty good to have people sign up so fast!"
    "Soon, your group is full and you are entering the raid. As you start the first battle, [the_person.title] is giving you instructions."
    the_person "Alright, just run up the stairs. I'll pull all the guys up there for the group to spike down..."
    "You are focusing as best you can... This is actually pretty tough..."
    the_person "... no! Focus the dragon, the group will cleave the adds..."
    "Oh fuck, there are adds? You didn't even notice... You attack the dragon."
    "You die a couple times, but the group is quick to revive you."
    if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
        $ gaming_cafe_large_grind()
        "You get a level up notification in the middle of a fight, but ignore it and keep playing."
    "Soon, you are at the final boss. Three of your teammates accidentally turn the wrong way during a mechanic and die. A group wipe is all but assured."
    the_person "Fuck! Looks like this is a wipe..."
    mc.name "Hang on I still have reanimate..."
    "You cast reanimate, just barely getting the skill off before the boss kills you. You are dead, but the three teammates are back up."
    the_person "Nice! We're back in it. I'll rez you..."
    $ the_person.change_love(2, 80)
    "The battle is tough, but you finally manage to beat it. You look at the clock and realize you have been playing for three hours."
    if gaming_cafe_character_level() < GUILD_QUEST_MAX_LEVEL:
        $ gaming_cafe_large_grind()
        "As you are turning in the quest, you get another level up notification."
    the_person "Nice! Told you we could get you through it!"
    mc.name "That was fun, but definitely difficult."
    the_person "Yeah. Always fun run with a new guildmate. We should do this again sometime."
    mc.name "Sounds good to me, but I need to be done for today. I can only play so long."
    $ the_person.draw_person()
    "You both stand up."
    the_person "Take care!"
    mc.name "See ya"
    $ clear_scene()
    "You walk away from the PC. You had a great time raiding with [the_person.title], and your character made progress, but it took a lot of focus to get through it."
    "You also consider [the_person.possessive_title] and her energy drink. If you play with her again, maybe you could slip a serum into it?"
    "This might be the break you need to get closer with her..."
    return

label gaming_cafe_buy_max_level_token_label():
    "You are tired of the slow grind through Guild Quest 2, so you decide to buy one of the max level character tokens."
    $ mc.event_triggers_dict["guild_quest_level"] = 50
    $ mc.business.change_funds(-20)
    $ myra.event_triggers_dict["character_bought"] = True
    "It is $20. Not a huge sum of money, but it kind of feels like cheating..."
    "Next time you play though, you'll be able to tackle anything in the game!"
    return

label gaming_cafe_adult_swim_label():
    "In this label, MC explores the adult section of the gaming cafe and probably gets lucky."
    return
