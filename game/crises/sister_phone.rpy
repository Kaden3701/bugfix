## Sister Phone Crisis Mod by Tristimdorion
init 3 python:
    def sister_phone_crisis_requirement():
        if time_of_day > 0 and time_of_day < 3 and not mc.is_home: #She always sends you texts while you're not at home for the middle part of the day
            if not lily in mc.location.people and lily.is_available: #Obviously don't do it if she's right there with you.
                return lily.love >= 30
        return False

    sister_phone_crisis_action = ActionMod("Sister Phone Message",sister_phone_crisis_requirement,"sister_phone_crisis_action_label",
        menu_tooltip = "[the_person.possessive_title] sends you phone messages", category="Home", is_crisis = True)

label sister_phone_crisis_action_label():
    #TODO: have a way of saving and reviewing selfies in the future.
    #TODO: Have a proper weekday/weekend schedule for people and use that to determine when sister is at home, at work, or out on the town.
    $ the_person = lily
    $ lowest_stat = lily.sluttiness
    if the_person.love < lowest_stat:
        $ lowest_stat = lily.love

    $ mc.start_text_convo(the_person)
    if lowest_stat >= 95:
        #Both love and sluttiness are very high, she sends you super slutty selfies and says she can't wait till you come home, fuck her, and make her your girl.
        $ ran_num = renpy.random.randint(1,3) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            if mc.business.is_weekend:
                $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(lowest_stat, guarantee_output =  True))
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                $ mc.change_locked_clarity(10)
                "Her first message is a selfie of herself lying down on your bed in lingerie."
                the_person "I can't wait until you come home and give me what I need. I wish I could spend every minute of every day worshiping your cock like a [the_person.possessive_title] should."
            else:
                the_person "It's so hard not to talk about you at school. The other girls are gossiping and I just want to tell them how good it feels when you try and breed me..."
                the_person "My pussy full of your warm cum, knowing that I can take care of you the way only [the_person.possessive_title] could."
                the_person "I think I'm going to go touch myself in the bathroom. I hope you are having a great day too [the_person.mc_title]!"
        elif ran_num == 2:
            $ the_person.strip_outfit(delay = 0)
            the_person "Hi [the_person.mc_title], I hope I'm not interrupting your busy work day. This is just a quick reminder..."
            $ mc.change_locked_clarity(20)
            $ the_person.draw_person(emotion = "happy")
            "You get a selfie from [the_person.possessive_title] naked in front of her bedroom mirror."
            the_person "That [the_person.possessive_title] wants to feel you inside her tonight. Don't stay out too late!"
        else:
            $ the_person.apply_outfit(the_person.get_random_appropriate_underwear(lowest_stat, guarantee_output = True))
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] sends you a picture of herself sitting on her knees wearing some lingerie."
            $ mc.change_locked_clarity(20)
            the_person "I can't wait to see you. So I can suck your big dick, like the good little cocksucker that I am."

    elif lowest_stat >= 80:
        #Both are high. Sends you slutty selfies and talks about how she wants to fuck you. Sends them from work, etc.
        $ ran_num = renpy.random.randint(1,2) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            if mc.business.is_weekend:
                the_person "I'm here at home and wishing you could help me take these pictures..."
                $ the_person.strip_outfit(delay = 0)
                $ the_person.draw_person(position = "standing_doggy")
                $ mc.change_locked_clarity(20)
                "[the_person.possessive_title] sends you a selfie of her in her bedroom naked and bent over her bed."
            else:
                the_person "I'm stuck here at school and all I can think about is you. Wish you were here..."
                $ the_person.strip_outfit(delay = 0)
                $ the_person.draw_person(position = "standing_doggy")
                $ mc.change_locked_clarity(20)
                "[the_person.possessive_title] sends you a selfie of herself in the school bathroom, naked and bending over the sink."

        else:
            if mc.business.is_weekend:
                the_person "I know it shouldn't, but thinking about you gets me so wet. You've shaped me into a new girl."
            else:
                the_person "I'm stuck at school in a boring lecture, but I can't get you out of my head. I'm so wet, I wonder if anyone would notice if I touched myself..."

    elif lowest_stat >= 60:
        #Sends you nudes and talks about how she'll help you blow off steam later.
        $ ran_num = renpy.random.randint(1,4) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            if mc.business.is_weekend:
                the_person "I was just about to get in the shower and I thought you might like a peek. Love you [the_person.mc_title]!"
                $ the_person.strip_to_underwear(delay = 0)
                $ the_person.draw_person(emotion = "happy")
                $ mc.change_locked_clarity(10)
                "[the_person.possessive_title] sends you a picture of herself stripped down in front of her bedroom mirror."

            else:
                the_person "I thought you might be stressed so I snuck away from school to take this for you."
                $ the_person.strip_to_underwear(delay = 0)
                $ the_person.draw_person(emotion = "happy")
                $ mc.change_locked_clarity(10)
                "[the_person.possessive_title] sends you a picture of herself stripped down in the park."
                the_person "I've got to get back to class. I hope nobody noticed me gone!"

        elif ran_num == 2:
            the_person "I thought you might enjoy this ;)"
            $ the_person.strip_outfit(delay = 0)
            $ the_person.draw_person(emotion = "happy")
            $ mc.change_locked_clarity(20)
            "[the_person.possessive_title] sends you a picture of herself stripped naked in front of her bathroom mirror."
        elif ran_num == 3:
            the_person "I've been trying on underwear all day. Would you like a peek?"

            "[the_person.possessive_title] doesn't wait for a reply and starts sending selfies."
            python:
                for i in __builtin__.range(3):
                    the_person.apply_outfit(the_person.get_random_appropriate_underwear(lowest_stat, guarantee_output = True))
                    the_person.draw_person(emotion = "happy")
                    mc.change_locked_clarity(5)
                    renpy.pause(2)
            the_person "I hope you think [the_person.possessive_title] looks sexy in her underwear ;)"
        else:
            $ the_person.outfit.remove_all_upper_clothing()
            if mc.business.is_weekend:
                the_person "I'm so glad it's the weekend, I can finally let these girls out..."
                $ the_person.draw_person(emotion = "happy")
                $ mc.change_locked_clarity(10)
                "She sends you a selfie from the kitchen with her top off."
                the_person "I hope your day is going well, love you!"

            else:
                the_person "I think I'd be much more popular here at school if I was allowed to dress like this..."
                $ the_person.draw_person(emotion = "happy")
                $ mc.change_locked_clarity(10)
                "She sends you a selfie from her school bathroom with her top off."
                the_person "Oh well, at least I know you appreciate it. I need to get back to class, see you at dinner!"

    elif lowest_stat >= 40:
        #Sends you teasing pictures (ie. no shirt or something) and talks about how much she loves you.
        $ ran_num = renpy.random.randint(1,3) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            the_person "You're such a hard worker [the_person.mc_title]. Here's a little gift from the girl who loves you most in the world!"
            $ the_person.outfit.remove_random_upper(top_layer_first = True)
            if the_person.wearing_bra and the_person.bra_covered: # when she is wearing a jacket, make sure to remove top
                $ the_person.outfit.remove_random_upper(top_layer_first = True)

            $ the_person.draw_person(emotion = "happy")
            $ mc.change_locked_clarity(10)
            if mc.business.is_weekend:
                "[the_person.possessive_title] sends you a selfie without her shirt on. The background looks like her bedroom."
            else:
                "[the_person.possessive_title] sends you a selfie without her shirt on. It looks like it was taken in a bathroom of her school."

        elif ran_num == 2:
            $ the_person.outfit.remove_random_upper(top_layer_first = True)
            if the_person.wearing_bra and the_person.bra_covered: # when she is wearing a jacket, make sure to remove top
                $ the_person.outfit.remove_random_upper(top_layer_first = True)

            $ mc.change_locked_clarity(10)
            if mc.business.is_weekend:
                the_person "I wish you were here spending time with me. Maybe this will convince you [the_person.possessive_title] is a cool person to hang out with!"
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a selfie from her bedroom without her shirt on."
            else:
                the_person "I'm busy here at school but I really wish I could be spending time with you instead. Do you think I'm pretty enough to spend time with ;)"
                $ the_person.draw_person(emotion = "happy")
                "[the_person.possessive_title] sends you a selfie without her shirt on. It looks like it was taken in the bathroom of her school."

        else:
            $ the_clothing = the_person.outfit.remove_random_upper(top_layer_first = True, do_not_remove = True)
            if the_clothing:
                $ the_clothing.colour[3] = the_clothing.colour[3] * 0.7 #It's translucent.
                the_person "It looks like my [the_clothing.name] didn't like being in the wash, it's gone all see-through."
                $ the_person.draw_person(emotion = "happy")
                $ mc.change_locked_clarity(10)
                if the_clothing.underwear:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent bra."
                else:
                    "You get a selfie from [the_person.possessive_title] wearing a slightly transparent top."
                the_person "Oh well, I can still wear it when I'm doing chores around the house. Hope your day is going better, love you!"
            else:
                the_person "I've looked everywhere, but I just can't find my favorite bra!"
                $ the_person.draw_person(emotion = "default")
                "[the_person.possessive_title] sends you a short video of herself walking around your home. Her bare tits bounce with each step."
                the_person "You don't happen to know where it is, do you? I'm wandering around looking for it and it's getting chilly!"
            $ the_clothing = None

    elif lowest_stat >= 20:
        #Sends you normal texts but talks about wanting to get away to talk to you instead
        $ ran_num = renpy.random.randint(1,5) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            if mc.business.is_weekend:
                the_person "I hope I'm not interrupting, I just wanted to say hi and check in. I'm stuck here at home wishing I could spend more time with you."
            else:
                the_person "I hope I'm not interrupting, I just wanted to say hi and check in. I'm stuck here at school wishing I could spend more time with you."
            the_person "Have a great day, see you later tonight. Love, [the_person.possessive_title]."

        elif ran_num == 2:
            the_person "I hope you are having a great day [the_person.mc_title]! Imagining you out there working so hard makes me prouder than you can imagine!"
            the_person "I'm looking forward to seeing you at home tonight. Love, [the_person.possessive_title]."

        elif ran_num == 3:
            the_person "I hope you aren't busy, I was thinking about you and just wanted to say hi!"
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend:
                "[the_person.possessive_title] sends you a selfie she took in the living room of your house."
            else:
                "[the_person.possessive_title] sends you a selfie she took from the bathroom at school."
        elif ran_num == 4:
            the_person "I'm always sending selfies to my friends, so I hope you like me sending them to you too!"
            $ the_person.draw_person(emotion = "happy")
            if mc.business.is_weekend:
                "[the_person.possessive_title] sends you a selfie she took in her bedroom."
            else:
                "[the_person.possessive_title] sends you a selfie she took in an empty hallway at school."
        else:
            the_person "All your hard work has inspired me [the_person.mc_title], I'm going out for a walk to stay in shape!"
            $ the_person.draw_person(emotion = "happy")
            "[the_person.possessive_title] sends you a short video she took of herself outside. She's keeping up a brisk walk and seems slightly out of breath."
            if not the_person.wearing_bra:
                if the_person.has_large_tits:
                    "She doesn't seem to realize it but it's very obvious [the_person.possessive_title] isn't wearing a bra under her shirt. Her [the_person.tits_description] heave up and down with each step."
                else:
                    "She doesn't seem to realize it but it's very obvious [the_person.possessive_title] isn't wearing a bra under her shirt. Her [the_person.tits_description] slightly bounce with each step."

    else:
        #Sends you normal sisterly texts.
        $ ran_num = renpy.random.randint(1,3) #Used to determine which variant we use to avoid spamming the player with the exact same texts.
        if ran_num == 1:
            the_person "I hope I'm not interrupting your busy day [the_person.mc_title]. I just wanted to let you know that I'm proud of you and you're doing great work."
            the_person "Keep it up! See you at dinner ;)"

        elif ran_num == 2:
            the_person "Remember that [the_person.possessive_title] loves you! Have a great day!"

        else:
            the_person "Hi [the_person.mc_title], I'm just checking in to make sure you're doing okay."
            "It's so sweet of her to think of you."

    $ mc.end_text_convo()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return
