#This crisis is a followup from a sexual encounter earlier in the day.
#A girl MC had sex with earlier in the day who had multiple orgasms texts MC to tell him how much she enjoyed it, can't stop thinking about it.

init -1 python:
    def crisis_nighttime_attaboy_requirement():      #Use this section to set up when this crisis or action can be fired.
        if day == attaboy_day and mc.is_in_bed:
            if attaboy_record.get("is_angry", False):   #Don't sext MC if the person ended sex angrily
                return False
            if Person.get_person_by_identifier(attaboy_target).location == mc.location:    #If she's sleeping with MC, don't have her text him.
                return False
            else:
                return True
        return False

init 2 python:
    crisis_nighttime_attaboy_action = ActionMod("Bedtime Sext", crisis_nighttime_attaboy_requirement, "crisis_nighttime_attaboy_label",  #Using ActionMod automatically adds this event to the crisis list
        menu_tooltip = "A sexy text from a satisfied lover.", category = "Home", is_crisis = True, is_morning_crisis = False)   #Categories include Home, Business, Fetish


init 1 python:
    # use these global vars to keep an up to date record of who MC has fucked good most recently.
    attaboy_target = None
    attaboy_record = None
    attaboy_day = -1
    #Precursor dialogue: "It was so hot, I can't stop thinking about it when, you know..."
    attaboy_position_descriptions = {
        "Against the Wall" : "You pinned me to the wall and had your way with me.",
        "Blowjob" : "I got to taste your wonderful, thick cock.",
        "Cowgirl" : "I got on top of you and slid down onto your amazing cock.",
        "Cunnilingus" : "Your tongue slipped into my pussy.",
        "Deepthroat" : "I finally got your cock to slide into my throat.",
        "Anal Doggy" : "You got me on all fours and slid into my ass.",
        "Doggy" : "You got me on all fours and pounded me doggystyle.",
        "Handjob" : "I could barely get my hand around your monster cock and started stroking it.",
        "Kissing" : "When our lips met. The electric jolt I got, I knew this was going to be an amazing session.",
        "Missionary" : "You put me on my back and slid inside of me.",
        "Piledriver" : "You lift my ankles up in the air and started pounding me.",
        "Skull Fuck" : "You grabbed my head and started fucking my face.",
        "Fingering" : "Your fingers slipped inside of me.",
        "Groping" : "Your hands started to roam all over my body, it felt so good.",
        "Tit Fuck" : "I slipped your cock between my big tits.",
        "Anal Cowgirl" : "I got on top of you and slid your cock into my ass.",
        "Sit on Lap" : "I sat on your lap with your cock in my ass.",
        "Standing Anal" : "You bent me over and slid your amazing cock into my ass.",
        "Swinging Anal" : "I got into the swing and your cock started sliding into my ass.",
        "Breeding Doggy" : "You bent me over and slid your raw cock inside my needy cunt.",
        "Breeding Missionary" : "You looked me in the eyes as your raw cock slipped inside my needy cunt.",
        "Cowgirl Blowjob" : "I laid you down and got to taste your amazing cock.",
        "Cowgirl Cunnilingus" : "I sat on your face.",
        "Doggy Anal DP" : "When I felt your cock and that strap-on penetrate my aching holes.",
        "Standing Doggy" : "You bent me over and had your way with me.",
        "Dry Cowgirl" : "I laid you down and started grinding my pussy against your big cock.",
        "Anal Piledriver" : "You lifted my ankles in the air and dominated my poor little asshole.",
        "Piledriver DP" : "You lifted my ankles in the air and fucked my holes with your cock and the strap-on.",
        "Prone" : "You pushed me down prone and fucked me silly when I was too tired to keep going.",
        "Reverse Cowgirl" : "I got on top and fucked you with my ass facing you.",
        "Sixty-Nine" : "I got on top and I got to suck your cock while you ate me out.",
        "Spanking" : "You bent me over and paddled me like the naughty little slut I am.",
        "Standing Cunnilingus" : "You got on your knees and started eating me out.",
        "Dildo Fuck" : "You pulled out that dildo and then slid it inside of me.",
        "Kneeling oral" :  "You got on your knees and started eating me out.",
        "Facing Wall" : "You turned my back to you and pinned me against the wall and pounded my needy pussy.",
        "Special Blowjob" : "Your yummy cock slid into my mouth and down my throat.",
        "Special Tit Fuck" : "Your cock slid between my tits. It gets me so hot just thinking about it!"
    }

#Precursor Dialogue "Yeah, you know what else was nice?"
    attaboy_cum_descriptions = {
        "creampies" : "When I felt your cock flooding my pussy with your cum.",
        "anal creampies" : "When I felt your cock explode in my ass, filling me with your cum.",
        "cum facials" : "When you finished and covered my face with your sticky cum.",
        "drinking cum" : "When I felt you explode in my mouth.",
        "cum on tits" : "When you coated my tits with your sticky cum.",
        "cum on stomach" : "When you pulled out and covered my tummy with your hot cum.",
        "cum on ass" : "When you pulled out and coated my ass with your hot cum!",

        "fetish creampies" : "I tried to keep it all in, but I could feel your cum leaking from my pussy all day. I'm so turned on just thinking about it!",
        "fetish anal creampies" : "I'm touching myself right now and I can still feel a little of your cum leaking out.",
        "fetish drinking cum" : "Your cum tastes so good, I wish I could swallow another load right now!",
        "fetish cum facials" : "Your cum feels so good, I wish I could take another load right now!",
        "fetish cum on tits" : "My tits are aching right now, I wish you could cover them with another load right now!",
        "fetish cum on stomach" : "Each spurt felt like lightning on my skin!",
        "fetish cum on ass" : "You can bend me over and cum on my ass anytime!",
        "fetish public sex" : "I just love it when you fuck me while other people are watching."
    }


    def get_attaboy_string_1(attaboy_record, the_person):
        text_list = []
        for x in attaboy_record.get("positions_used", []):
            text_list.append(attaboy_position_descriptions.get(x.name, None))
        if len(text_list) == 0: #Somehow we had sex without using any positions?
            text_list.append("I'm sure you know. It was amazing, and I'm getting wet just thinking about it!")
        return get_random_from_list(text_list)

    def get_attaboy_string_2(attaboy_record, the_person):
        text_list = []
        if attaboy_record.get("creampies", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("creampies", None))
        if attaboy_record.get("anal creampies", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("anal creampies", None))
        if attaboy_record.get("cum facials", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("cum facials", None))
        if attaboy_record.get("drinking cum", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("drinking cum", None))
        if attaboy_record.get("cum on tits", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("cum on tits", None))
        if attaboy_record.get("cum on stomach", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("cum on stomach", None))
        if attaboy_record.get("cum on ass", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("cum on ass", None))
        if len(text_list) == 0: #Didn't cum on her.
            text_list.append("Watching your face when you finished. Your O face is hot!")
        return get_random_from_list(text_list)


    def get_attaboy_fetish_string(attaboy_record, the_person):
        text_list = []
        if the_person.has_breeding_fetish:
            if attaboy_record.get("creampies", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish creampies", None))
        if the_person.has_anal_fetish:
            if attaboy_record.get("anal creampies", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish anal creampies", None))
        if the_person.has_cum_fetish:
            if attaboy_record.get("cum facials", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish cum facials", None))
            if attaboy_record.get("drinking cum", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish drinking cum", None))
            if attaboy_record.get("cum on tits", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish cum on tits", None))
            if attaboy_record.get("cum on stomach", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish cum on stomach", None))
            if attaboy_record.get("cum on ass", 0) > 0:
                text_list.append(attaboy_cum_descriptions.get("fetish cum on ass", None))
        if the_person.has_exhibition_fetish:
            if attaboy_record.get("was_public", False):
                text_list.append(attaboy_cum_descriptions.get("fetish public sex", None))
        if len(text_list) == 0: #No fetish text
            return None
        return get_random_from_list(text_list)

label crisis_nighttime_attaboy_label():
    $ the_person = Person.get_person_by_identifier(attaboy_target)
    if the_person is None:
        return

    if the_person.arousal < 60:
        $ the_person.arousal = 60

    $ text_1 = get_attaboy_string_1(attaboy_record, the_person)
    $ text_2 = get_attaboy_string_2(attaboy_record, the_person)
    $ text_3 = get_attaboy_fetish_string(attaboy_record, the_person)
    "After you get in bed, as you are drifting off to sleep, you hear your phone vibrate."
    "You roll over and look at it. It's a text from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey! Sorry, I'm not sure if you're still up or not, but just wanted to text you."
    the_person "I'm lying in bed, I can't stop thinking about earlier today when you made me cum my brains out."
    the_person "It was so hot, I can't stop thinking about it when, you know..."
    the_person "[text_1]"
    $ mc.change_locked_clarity(40)
    "You text her back."
    mc.name "Mmmm, yeah I liked that part too."
    if attaboy_record.get("guy orgasms", 0) > 0:
        the_person "Yeah, you know what else was nice?"
        mc.name "What?"
        the_person "[text_2]"
        $ mc.change_locked_clarity(50)
        if text_3:
            the_person "[text_3]"
            $ the_person.change_slut(1, 80)
            $ mc.change_locked_clarity(70)
            "Holy shit, [the_person.possessive_title] knows how to sext. You are getting really turned on."
        else:
            $ the_person.change_slut(1, 50)
            "Her dirty words are really turning you on."
    else:
        $ the_person.change_slut(1, 40)
        the_person "I'm sorry you didn't get to finish. I promise next time you'll get yours!"
    mc.name "What are you doing now?"
    the_person "Oh, not much. Wanna see?"
    mc.name "Hell yeah"
    if the_person.location != the_person.home and the_person.location.people > 1:
        the_person "Sorry! There's too many people around for me to snap any sexy pics..."
        $ the_person.draw_person(emotion = "happy")
        "She snaps you a quick selfie."
    elif the_person.is_at_mc_house:
        the_person "Then why don't you come see? Maybe we could have a repeat performance right now ;)"
        menu:
            "Go see [the_person.title]" if mc.energy > 80:
                $ mc.end_text_convo()
                "You get up and creep down the hall. When you open her door, you see [the_person.possessive_title] laying out on her bed."
                $ the_person.location.show_background()
                $ the_person.strip_outfit(delay = 0)
                $ mc.change_locked_clarity(50)
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                "[the_person.title] looks up when she hears her door open and smiles at you."
                if the_person.has_taboo(["bare_tits", "bare_pussy"]): #She doesn't want to strip in front of you, let's break those taboos!
                    mc.name "Oh my god... you're naked!"
                    the_person "I know you've never seen me before this... exposed..."
                    mc.name "You look amazing."
                    "She blushes and smiles wider."
                    the_person "Thanks... now close the door and get over here!"
                    $ the_person.break_taboo("bare_tits")
                    $ the_person.break_taboo("bare_pussy")
                else:
                    "Damn! She is so hot. You just stare at her for a few seconds."
                    the_person "You getting a good look?"
                    mc.name "Sorry, I..."
                    the_person "Just close the door and get over here!"
                "You quietly close the door and then walk over to the bed, joining [the_person.possessive_title]."
                call fuck_person(the_person, start_object = make_bed(), skip_intro = True) from _call_fuck_person_attaboy_encore_01
                "When you finish, [the_person.possessive_title] lays back in her bed."
                $ the_person.draw_person(position = "missionary", emotion = "happy")
                the_person "I think I'll be able to sleep well now!"
                "You say goodnight to [the_person.possessive_title], then quietly got back to your room for the night."

                $ mc.location.show_background()
                $ the_person.apply_planned_outfit()
                $ clear_scene()
                return
            "Go see [the_person.title]\n{color=#ff0000}{size=18}Requires more energy{/size}{/color} (disabled)" if mc.energy <= 80:
                pass
            "Too tired":
                mc.name "Sorry, I'm really worn out. Maybe tomorrow."
                the_person "Aww, okay."
    else:
        #Copy pasted a bunch of code from sister_phone crisis for her to send a few sexy selfies.
        $ lowest_stat = the_person.sluttiness
        # if the_person.love < lowest_stat: #Test using just sluttiness
        #     $ lowest_stat = the_person.love

        if lowest_stat >= 100:
            #Both love and sluttiness are very high. She is masturbating
            $ the_person.strip_outfit(delay = 0)
            $ mc.change_locked_clarity(50)
            $ the_person.draw_person(position = "missionary", emotion = "happy")
            "You get a selfie from [the_person.possessive_title] laying on her bed while she is masturbating."
            the_person "I want to feel you inside me soon!"

        elif lowest_stat >= 80:
            #Both are high. Sends you slutty selfies and talks about how she wants to fuck you. Sends them from work, etc.

            the_person "Wish you were here bending me over instead of just me taking pictures..."
            $ the_person.strip_outfit(delay = 0)
            $ the_person.draw_person(position = "standing_doggy")
            $ mc.change_locked_clarity(40)
            "[the_person.possessive_title] sends you a selfie from her bedroom naked and bent over her bed."
            $ the_person.change_slut(1, 100)

        elif lowest_stat >= 60:
            the_person "I was just about to get in the shower and I thought you might like a peek ;)"
            $ the_person.strip_to_underwear(delay = 0)
            $ the_person.draw_person(emotion = "happy")
            $ mc.change_locked_clarity(30)
            "[the_person.possessive_title] sends you a picture of herself stripped down in front of her bedroom mirror."
            $ the_person.change_slut(1, 80)

        else:

            $ the_person.outfit.remove_random_upper(top_layer_first = True)
            if the_person.wearing_bra and the_person.bra_covered: # when she is wearing a jacket, make sure to remove top
                $ the_person.outfit.remove_random_upper(top_layer_first = True)

            $ mc.change_locked_clarity(20)
            the_person "I don't feel comfortable sending nudes, but hopefully this brightens up your night."
            $ the_person.draw_person(emotion = "happy")
            "[the_person.possessive_title] sends you a selfie from her bedroom without her shirt on."
            $ the_person.change_slut(1, 60)

    the_person "Anyway, good night! Hopefully I'll see you tomorrow."
    mc.name "Good night."
    $ mc.end_text_convo()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    return
