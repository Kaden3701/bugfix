# This is Camilla's resistant story line. Early on in her love series, she asks for MCs help with her husband, but regrets it when getting into things that are too personal.
# Later, Camilla has the revelation that her husband is actually a cheater. Gives MC the option to adjust to this new lifestyle, or to leave her husband for him.
# While considering it, Camilla gives MC her anal virginity, and cuckolds her husband until events resolve.
# Camilla meets Alexia as part of this storyline, and can be used to take photos at your business.

init -1 python: #Requirement Functions
    def camilla_outfit_help_requirement(person):
        if person.love < 20:
            return False
        if not person.story_event_ready("love"):
            return False
        if person.location != mall:
            return False
        return True

    def camilla_lingerie_help_requirement(person):
        if person.love < 40:
            return False
        if not person.story_event_ready("love"):
            return False
        if person.location != mall:
            return False
        return True

    def camilla_formal_date_requirement():
        if camilla.love < 60:
            return False
        if time_of_day == 3 and day%7 < 4 and camilla.story_event_ready("love"):
            return True
        return False

    def camilla_gives_anal_virginity_requirement(the_person):
        return False

init 2 python:  #Camilla Actions
    camilla_outfit_help = Action("Shopping Trip", camilla_outfit_help_requirement, "camilla_outfit_help_label")
    camilla_lingerie_help = Action("Lingerie Shopping", camilla_lingerie_help_requirement, "camilla_lingerie_help_label")
    camilla_formal_date = Action("Camilla Comes Over", camilla_formal_date_requirement, "camilla_formal_date_label")
    camilla_gives_anal_virginity = Action("Camilla Tries Anal", camilla_gives_anal_virginity_requirement, "camilla_gives_anal_virginity_label")

    camilla_love_role = Role(role_name ="Camilla Love", actions =[ashley_work_titfuck, ashley_work_blowjob, ashley_work_fuck, ashley_work_anal], hidden = True)

# Camilla's love story scenes

label camilla_outfit_help_label(the_person):    #20
    python:
        camilla_outfit_1 = Wardrobe.generate_random_appropriate_outfit(the_person)
        camilla_outfit_2 = Wardrobe.generate_random_appropriate_outfit(the_person)
        camilla_outfit_3 = None
    "You go for a walk around the mall. As you pass by the stall where [the_person.title] is working it, she notices you."
    $ the_person.draw_person()
    the_person "Hola [the_person.mc_title]."
    mc.name "Hey [the_person.title]. How are you doing today?"
    the_person "I'm doing well. Just having a little bit of a dilemma."
    mc.name "Oh? What is going on?"
    the_person "Ah, well, my husband is taking me out tomorrow for a date, and I can't decide what to wear!"
    the_person "I bought two new outfits over at Sak's, but I just can't decide."
    "Hmmm, maybe this is something you could help out with?"
    mc.name "I have an idea. Why don't you try them on for me and I'll help you decide?"
    the_person "Oh... well... I don't know... that seems kind of personal."
    the_person "I'm not sure I feel comfortable with that."
    mc.name "Why not? I don't mean any harm by it. What time is your break?"
    the_person "Well... I'm about due for a break. Let me just put up a be right back sign and we can head over to the clothing store and I'll use the changing room there."
    mc.name "Great!"
    $ mc.change_location(clothing_store)
    "You walk with her to the clothing store and back towards the dressing rooms."
    mc.name "So, a hot date huh? Any idea what you are gonna do?"
    the_person "I have no idea! I just want to make sure I look nice for it!"
    the_person "Alright, give me just one moment and I'll be out!"
    $ clear_scene()
    "[the_person.possessive_title] steps into the dressing room. You wish you could have a look and see what is going on in there, but think better of it in this public setting."
    $ the_person.apply_outfit(camilla_outfit_1, update_taboo = True)
    $ the_person.draw_person(position = "stand2")
    "[the_person.title] steps out of the dressing room."
    the_person "Here! This is the front..."
    $ the_person.draw_person(position = "back_peek")
    the_person "And this is what it looks like from the back..."
    $ mc.change_locked_clarity(10)
    "She pauses for a few seconds to let you look her up and down."
    $ the_person.draw_person(position = "stand2")
    the_person "Alright. So this is the first one! Hang on before you say anything, let me show you the other one I am thinking of..."
    $ clear_scene()
    "[the_person.possessive_title] disappears back into the dressing room... damn you wish you could see her getting undressed..."
    $ the_person.apply_outfit(camilla_outfit_2, update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] steps out of the dressing room in her second outfit."
    the_person "Here we go! And of course..."
    $ the_person.draw_person(position = "back_peek")
    "She turns around again, giving you a good look at her back side."
    $ mc.change_locked_clarity(10)
    the_person "The back of this one..."
    $ the_person.draw_person(position = "stand4")
    the_person "What do you think?"
    menu:
        "Suggest the first outfit":
            mc.name "I think your husband would appreciate the first outfit the most."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = camilla_outfit_1
            $ the_person.add_outfit(camilla_outfit_1,"full")
            the_person "Thanks! It helps to have a man's opinion on this."

        "Suggest the second outfit":
            mc.name "I think your husband would appreciate the second outfit the most."
            "She smiles and nods."
            $ the_person.change_happiness(5)
            $ the_person.next_day_outfit = camilla_outfit_2
            $ the_person.add_outfit(camilla_outfit_2,"full")
            the_person "Thanks! It helps to have a man's opinion on this."

        "Suggest your own outfit":
            mc.name "They both look good, but I think I have another idea for something you could wear..."
            "[the_person.title] seems surprised, but goes along with it for now."
            the_person "Oh? I suppose I have time I could try on one more outfit... why don't you go pick something out for me while I change?"
            mc.name "Okay."
            $ clear_scene()
            call outfit_master_manager(slut_limit = the_person.sluttiness + 5, show_overwear = False, show_underwear = False) from _call_outfit_master_manager_camilla_hubby_impression_01
            $ camilla_outfit_3 = _return
            #$ the_person.draw_person()

            if camilla_outfit_3 is None:
                "You try a few different combinations, but you can't come up with anything. You head back to the changing room."
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()
                mc.name "Sorry, I thought I had an idea but I guess I was wrong."
                the_person "That's fine [the_person.mc_title]. I think I'm going to go with the first one."
                $ the_person.change_happiness(5)
                $ the_person.next_day_outfit = camilla_outfit_1
                $ the_person.add_outfit(camilla_outfit_1,"full")
            else:
                "You take the outfit for [the_person.possessive_title] back to the changing room and set it on top of the door."
                the_person "Okay, give me a minute to try it on!"

                $ the_person.apply_outfit(camilla_outfit_3, update_taboo = True)
                $ the_person.draw_person()
                $ the_person.change_stats(happiness = 5, obedience = 5, love = 1)
                the_person "This is... surprisingly fashionable!"
                $ the_person.draw_person(position = "back_peek")
                "[the_person.title] gives you a quick turn to show it off."
                $ mc.change_locked_clarity(10)
                $ the_person.add_outfit(camilla_outfit_3,"full")
                $ the_person.next_day_outfit = camilla_outfit_3
                the_person "What the hell. I'm going to get it. Give me a minute, I'm going to change back..."
                $ clear_scene()
                $ the_person.apply_planned_outfit()
                $ the_person.draw_person()

    the_person "Thank you for the help [the_person.mc_title]."
    mc.name "Of course. Always glad to help."
    the_person "This still feels weird though..."
    "She mutters something under her breath."
    # $ the_person.change_love(1, 40)
    the_person "I'd better get back to my stall. Take care!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] walks away, leaving you in the clothing store. You hope that her husband can appreciate her beauty as much as you do!"
    $ the_person.add_unique_on_room_enter_event(camilla_lingerie_help)
    $ camilla.event_triggers_dict["help_with_outfit"] = True
    python: #Cleanup time
        camilla_outfit_1 = None
        camilla_outfit_2 = None
        camilla_outfit_3 = None
    return

label camilla_outfit_love_restore_label(the_person):
    pass

    $ the_person.story_event_log("love")
    return

label camilla_outfit_love_label(the_person):
    pass
    return

label camilla_lingerie_help_label(the_person):  #40
    python:
        camilla_lingerie_1 = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under")
        camilla_lingerie_2 = Wardrobe.generate_random_appropriate_outfit(the_person, outfit_type = "under")

    "Walking around the mall, you happen to walk by [the_person.possessive_title]'s stall. You decide to stop in and see how she is doing."
    $ the_person.draw_person()
    mc.name "Hello [the_person.title]. How are you doing?"
    the_person "Oh hey [the_person.mc_title]. I'm doing good. Here to work on your goals again?"
    mc.name "Nah, I just stopped in to say hello and see how you are doing."
    the_person "Ah, thanks. It's always good to see you."
    "You chat with her for a few minutes about general small talk."
    the_person "Say... are you busy right now?"
    mc.name "Not really."
    the_person "I'm due for a lunch break... want to snap a few more umm... you know... pics for me?"
    "Damn. You can't forget taking pics with her in the bar restroom with your dick in her mouth. Surely this opportunity is worth taking too!"
    mc.name "Definitely. Have something in mind?"
    the_person "Well, I have a couple more outfits I kind of wanted to get your opinion on, but they are for a more intimate encounter than last time..."
    mc.name "Wow, sounds great! Lead the way!"
    $ mc.change_location(clothing_store)
    "You walk with her to the clothing store and back towards the dressing rooms."
    the_person "So, I have a special night planned with the hubby... I was hoping you could give me your opinion on some lingerie sets..."
    the_person "And then snap a couple quick pictures that I can send to him as a tease!"
    mc.name "Alright, I think I'm down for that."
    $ mc.change_location(changing_room)
    "When you get to the dressing rooms, [the_person.possessive_title] takes a quick look around to make sure the coast is clear, then quickly drags you into the changing room with her."
    the_person "Shh, just be quiet. It'll be easier if you're in here with me while I try these on."
    $ the_person.strip_outfit(exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Quietly, [the_person.possessive_title] strips down in front of you. She gives you a sheepish smile when she is naked, before donning her underwear set."
    $ the_person.apply_outfit(camilla_lingerie_1, update_taboo = True)
    $ the_person.draw_person(position = "stand2")
    "[the_person.title] whispers to you."
    the_person "Okay. This is the first set..."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns around and bends over, give you the opportunity to check out how the set hugs her curves."
    "You enjoy a good long look."
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "stand2")
    the_person "Alright, one second..."
    $ the_person.strip_outfit(exclude_feet = False)
    $ mc.change_locked_clarity(20)
    "Quietly, [the_person.possessive_title] strips down in front of you again."
    $ the_person.apply_outfit(camilla_lingerie_2, update_taboo = True)
    $ the_person.draw_person(position = "stand4")
    "[the_person.title] whispers to you."
    the_person "Okay. This is the second set."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns around and bends over again. The way she is showing off her body is really starting to turn you on."
    $ mc.change_locked_clarity(20)
    "You swear you see a little wiggle in her hips as you check her out."
    $ the_person.draw_person(position = "stand4")
    the_person "What do you think? Which set did you like better?"
    menu:
        "The first set":
            the_person "Ah, okay. One second..."
            $ the_person.strip_outfit(exclude_feet = False)
            $ mc.change_locked_clarity(20)
            "Quietly, [the_person.possessive_title] strips down and then changes back into the first outfit."

            $ the_person.apply_outfit(camilla_lingerie_1, update_taboo = True)
            $ the_person.draw_person(position = "stand2")
            $ the_person.add_outfit(camilla_lingerie_1,"under")
        "This set":
            the_person "Ah, I see..."
            $ the_person.add_outfit(camilla_lingerie_2,"under")

    the_person "Okay, can you snap some pics for me?"
    mc.name "Sure."
    "[the_person.title] hands you her phone with her camera app pulled up. She strikes a few poses for you."
    $ the_person.draw_person(position = "stand4")
    "[the_person.possessive_title] strikes a few poses for you. You make sure to snap pics showing off her incredible body as best you can."
    $ the_person.draw_person(position = "standing_doggy")
    if camilla.event_triggers_dict.get("anal_sex", False):
        "Bending over, you get an awesome view of [the_person.title]'s ass."
        "For a second you get goosebumps thinking about the first time you bent her over the bathrooms sink at the bar and fucked her proper."
        $ mc.change_locked_clarity(50)
    else:
        "Bending over, you get a great view of [the_person.title]'s undefiled ass."
        "The way things are going, you think it is only a matter of time until you can bend her over and fuck her properly."
        $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "sitting")
    "You snap a few more pictures of [the_person.possessive_title] as she sits on the bench, showcasing her long, sexy legs."
    "Suddenly, you are struck by just how picture perfect she really is. Long legs, nice tits, and her tanned skin gives her an exotic appearance."
    mc.name "[the_person.fname]... have you ever thought about shooting some professional pictures?"
    the_person "Umm... you mean like... modeling?"
    mc.name "Not necessarily modeling... but like, boudoir photos? You really do have the body for it."
    $ the_person.change_stats(slut = 1, max_slut = 60, love = 2, max_love = 80)
    the_person "Oh! You mean like... sexy photos?"
    mc.name "Yeah."
    the_person "Wow... I mean, I guess I've always kind of thought about it but... I don't think I really have the body for it?"
    "What the fuck, is she serious?"
    mc.name "I would argue aggressively against that statement. Your body would be perfect for boudoir."
    the_person "I don't know... what would I even do with them?"
    mc.name "You could sell them for advertisement purposes, or even keep them for you and your husband."
    mc.name "You should try it. Worst case scenario, you don't care for it, so you get rid of them and don't try it again."
    the_person "I guess... I could maybe try it sometime? Is that something you could do for me?"
    if mc_business_has_expensive_camera():
        "You think about it. You do have the expensive camera that you got for making ads at your business."
        if alexia == mc.business.company_model: #Alexia is the company model
            "Actually, the photo sessions you have been doing with [alexia.possessive_title] have been going well."
            "Maybe you could have her help you with it? That would probably make it an easier sell to [the_person.title] if a woman was helping."
            mc.name "Actually, at my business I have a nice camera and photographer we use for company ads. She would probably be willing to help if I asked her to."
            "[the_person.possessive_title] thinks about it for a bit, but finally agrees."
            the_person "Okay... I'll do it. Can you set it up for me and let me know when and where?"
            mc.name "Certainly, I'll get back to you about it."
        else:
            "Right now though, you don't really have anyone who you could count on to take the pictures."
            "Maybe in the future you will have something better in line to facilitate this sort of photo shoot."
            mc.name "I don't have the ability right now to do that, but I'll let you know in the future if that is something I can pull off."
            "She looks disappointed, but also relieved."
            the_person "Okay. I appreciate the thought."
    else:
        "Unfortunately, you have no idea how you could facilitate this. After thinking about it for a bit, you decide it isn't in your capabilities right now."
        mc.name "I don't have the ability right now to do that, but I'll let you know in the future if that is something I can pull off."
        "She looks disappointed, but also relieved."
        the_person "Okay. I appreciate the thought."
    $ camilla_alexia_boudoir_intro_setup()
    "You snap a couple more photos. Just when you think you are finishing up, [the_person.title] gets down on her knees and slides over to you."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] grabs your zipper and starts to pull it down. A couple quick motions later, and your cock is out and inches from her face."
    the_person "Hey, keep taking pictures!"
    mc.name "Right!"
    "You snap more pictures as [the_person.title] opens up and slides her warm wet mouth down over the tip of your erection."
    $ mc.change_locked_clarity(50)
    "All the sexy wardrobe changes have you aching for release. You sigh as [the_person.possessive_title]'s mouth starts bobbing up and down."
    call get_fucked(the_person, start_position = blowjob, private = True, skip_intro = True, ignore_taboo = True, allow_continue = False) from _call_get_fucked_camilla_lingerie_blowjob_01
    if the_person.has_mouth_cum:
        "[the_person.possessive_title] looks up at you. You frame the cum dribbling down the sides of her mouth in a final set of pictures."
        the_person "Mmm, another tasty snack. Glad I got a high protein lunch today!"
    elif the_person.has_face_cum:
        "[the_person.possessive_title] looks up at you. You frame her cum drenched face in a final set of pictures."
        the_person "God, it doesn't get old, does it? Sucking off another man?"
    $ the_person.draw_person (position = "stand2")
    "[the_person.title] stands up. You hand her back her phone."
    the_person "Go ahead and sneak out, I'm going to buy this and send a few messages..."
    mc.name "Sounds good... I'll see you next time."
    $ clear_scene()
    $ the_person.apply_planned_outfit() # restore clothes
    $ mc.change_location(clothing_store)
    "With a quick wink, you excuse yourself from the changing room and go out into the clothing store."
    "[the_person.title] was so hot in that lingerie. You really hope you get the chance to take more photos of her like that."
    $ mc.business.add_mandatory_crisis(camilla_formal_date)
    $ camilla.event_triggers_dict["help_with_lingerie"] = True
    python: #Cleanup time
        del camilla_lingerie_1
        del camilla_lingerie_2
    return

label camilla_lingerie_love_restore_label(the_person):
    pass

    $ the_person.story_event_log("love")
    return

label camilla_lingerie_love_label(the_person):
    pass
    return

label camilla_formal_date_label():    #60
    $ the_person = camilla
    "As you are finishing up your day, your phone vibrates, and you see you have a message from [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    the_person "Hey Señor! Sorry, I know this is last minute... are you busy tonight?"
    mc.name "I'm not now. Want to meet at the bar?"
    the_person "I was actually wondering if you wanted to grab dinner somewhere else tonight."
    "Dinner? That sounds a LOT like a date! You wonder why she suddenly wants to change things up. Could be interesting!"
    mc.name "Sounds great. I know a good place. I'll text you the address, my treat, okay?"
    the_person "Wow, you don't have to do that... but I'm not going to say no! See you there!"
    "You send her the address and set a time. It's a fairly upscale place that you think she will be fairly impressed by."
    $ mc.end_text_convo()
    "You double check and make sure you look okay for the occasion, then head over to the restaurant."
    $ mc.change_location(fancy_restaurant)
    "When you arrive, you check in at the front counter. You wait a few minutes, but your date soon arrives."

    $ the_person.planned_outfit = the_person.wardrobe.get_outfit_with_name("Camilla Summer Dress") or the_person.get_random_appropriate_outfit(guarantee_output = True)
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ the_person.draw_person()
    the_person "Buenas noches señor!"
    mc.name "Ah. [the_person.title], good to see you. You look great!"
    the_person "Gracias! I can't wait to try this place. I knew it was here, but despite living in this town for a decade, I've never been inside."
    mc.name "Yes, and I think the change of scenery will do us some good. The bar is nice and all but this is certainly a pleasant alternative."
    the_person "Yeah I suppose so."
    "You make some small talk with [the_person.possessive_title] until you are shown to your table."
    $ the_person.draw_person(position = "sitting")
    "The waiter seats you both and turns to you."
    "WAITER" "Can I get your started with anything? Our house red wine is delightful for a beautiful young couple such as yourselves."
    the_person "Ha!... ahhh..."
    "[the_person.title] lets out a snort. For a second, the waiter looks at you in distress, thinking he's embarrassed you by assuming you were a couple, but you just smile."
    mc.name "That sounds great. Start with two glasses?"
    "WAITER" "Yes sir. I'll have those right out."
    "As the waiter walks away, [the_person.possessive_title] looks at you and laughs."
    the_person "A young couple. That's the funniest thing I've heard in a while!"
    if camilla.event_triggers_dict.get("anal_sex", False):
        mc.name "Is it funny though? We do other things that couples often do..."
    elif camilla.event_triggers_dict.get("home_sex", False):
        mc.name "I mean, we've been intimate. Is it really that far off?"
    else:
        mc.name "I mean, I helped you shop for lingerie. Is it REALLY that far off?"
    the_person "I suppose that is a fair point."
    mc.name "I know it was for the benefit if your husband... but still."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    the_person "Ugh, can we PLEASE not bring him up tonight?"
    "Yikes... has something happened between them? Usually the time you spend with [the_person.title] is for mostly his benefit..."
    "The look on her face tells you that you should probably leave it alone though."
    mc.name "I'm fine with that. Let's talk more about *us* then."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    mc.name "I suppose I'll go first... What are you ordering?"
    the_person "I have no idea... the menu all looks so good. I was thinking maybe the salmon."
    mc.name "That does sound good..."
    the_person "Yeah. I had a friend tell me once it's a good aphrodisiac. Might be good for when it's time to get out of here."
    "The sultry tone in [the_person.possessive_title]'s voice makes it clear that she is hoping for there to be a part two to this date."
    "The waiter brings out the wine and takes your orders. Before long you've drank two glasses each. The waiter returns and sees your empty glasses."
    "WAITER" "Sir, you and your friend here seem to be enjoying the wine tonight. Might I bring a full bottle for you?"
    mc.name "That sounds great."
    "Soon the food and the wine arrive. You dig in to a plate of pesto shrimp linguini and [the_person.title] eats her salmon."
    "When you finish eating, you've both had several glasses of wine. [the_person.possessive_title] looks at you seriously."
    the_person "So, you are probably wondering why I suddenly want to go out for dinner with you."
    mc.name "Yeah I'm definitely wondering..."
    "[the_person.title] takes a long draught of wine and then continues."
    the_person "Well, at the bar a few nights ago, I got approached by a woman. She said hello, knew my name. Knew a lot about me actually."
    the_person "She explained that she was so happy that I was FINALLY coming around to the hotwife lifestyle."
    the_person "I... I asked how she knew about it? And she said... she said that her and her husband and... and my husband... had been fucking around too."
    the_person "Of course I just... you know... played it off cool. But I was so blindsided by it! I asked her... you know... how long had they been at it."
    the_person "And, well, they've been fucking around for a LOT longer than we have..."
    the_person "But that hey! It's okay right? We're all in the lifestyle together now right?"
    the_person "She pointed out her husband. Asked if I was interested. I said maybe, but honestly I just got sick to my stomach."
    mc.name "[the_person.fname]... I'm sorry..."
    $ the_person.change_stats(happiness = -5, love = 2, max_love = 80)
    the_person "It's ok. You didn't have anything to do with it. I just... I just don't understand, why he kept it all a secret from me... you know?"
    "[the_person.title] turns away for a second and wipes her eyes."
    mc.name "What... what are you going to do?"
    the_person "I have no idea, honestly. These last few weeks have been so crazy! I don't know if I even want this lifestyle."
    the_person "I honestly was just thinking that... maybe tonight we could go back to your place?"
    the_person "I don't want to go home tonight. Just let me come over, and tomorrow, or the next day, or sometime soon, I can really just think about it and figure it out."
    mc.name "Okay. Let's get out of here."
    $ mc.business.change_funds(-200)
    "You quickly grab the check, putting the dinner on the company card. A short walk later, you are walking into your house with [the_person.possessive_title]."
    $ mc.change_location(bedroom)
    #TODO if MC has fixed up bedroom camilla is impressed, if not she says something of colour.
    $ the_person.draw_person()
    the_person "Wow... I've not been in a man's bedroom in... a long time."
    mc.name "You want to just... get some sleep? I'm sure it's been a long day."
    $ the_person.change_love(2, 90)
    the_person "That is very kind of you... but that isn't why I'm here."
    "You step close to [the_person.title] and pull her close to you."
    $ the_person.draw_person(position = "kissing")
    $ the_person.change_arousal(10)
    "You lips meet with an immediate spark. There is something different about her this time."
    "Before when you would kiss, she was a bit reserved, holding back a piece of herself."
    "This time though, she isn't kissing you out of a duty to her husband. She's doing it because she WANTS to."
    "Your hands drop to her ass. She moans into your mouth as you make out."
    $ the_person.change_arousal(15)
    the_person "Señor! I'm ready... let's do this!"
    $ the_person.draw_person()
    "With a shove, she pushes you onto your back on your bed. She stands in front of you as she strips down."
    $ the_person.strip_outfit()
    $ mc.change_locked_clarity(50)
    "[the_person.possessive_title] stands in front of you, completely naked, ready for a full night of fun. She slowly climbs on top of you."
    $ the_person.draw_person(position = "cowgirl")
    the_person "Like what you see, señor?"
    mc.name "Fuck yes. You are so sexy..."
    the_person "Mmm... I believe you... but I want to see proof..."
    "[the_person.title] grabs your pants and you lift your ass up a bit as she slides them off you."
    "She grabs your mostly erect cock and gives it a couple strokes."
    the_person "Ahh... not bad... but I think we can get it a little harder first..."
    "[the_person.possessive_title] opens her mouth and runs her tongue along the length of your cock."

    python: #Creation of custom sex path for this scene.
        first_node = dom_sex_path_node(cowgirl_blowjob, completion_requirement = dom_requirement_mc_aroused)    #Blowjob to arousal
        final_node = dom_sex_path_node(reverse_cowgirl, completion_requirement = dom_requirement_creampie)   #Finish inside her
        sex_path = [first_node, final_node]
    call get_fucked(the_person, the_goal = "vaginal creampie", sex_path = sex_path, skip_intro = True, allow_continue = False, start_object = make_bed()) from _call_get_fucked_camilla_sleepover_fuck_01
    $ the_report = _return
    if the_report.get("girl orgasms", 0) > 0:
        the_person "Oh my god... that was amazing. You ALWAYS get me off... its incredible..."
    if the_report.get("guy orgasms", 0) > 0:
        if the_person.has_ass_cum:
            "[the_person.possessive_title] looks back at you. Her ass is plastered with your sticky seed."
            "For once, you can just lie back and enjoy it, without worrying about snapping pictures for her husband."
            "You have to admit, having her all to yourself feels great."
        elif the_person.has_creampie_cum:       #We assume we finished inside her#
            "[the_person.possessive_title]'s pussy is dripping cum from your creampie."
            "It's so hot, dumping your load inside a married woman."
            if camilla_is_fertile():
                "Especially since you cured her infertility."
                if the_person.knows_pregnant():
                    "You've already knocked her up, and now every load is another claim you are staking on her body."
                else:
                    "Every load you dump inside her could be the one that knocks her up."
            else:
                "But it is a little worrying to be doing so... is she even on birth control?"
                mc.name "Is it okay? To be having risky sex like this?"
                the_person "Oh yeah. I don't know if I've ever talked to you about this but... I'm actually infertile..."
                the_person "A hormonal issue going back since before puberty."
                mc.name "Ah, I see."
    python:
        del sex_path
        del first_node
        del final_node

    "[the_person.title] lays down in your bed next to you, on her side. You cuddle up behind her."
    $ the_person.draw_person(position = "walking_away")
    "Her body is flushed and hot, but her beautiful skin feels amazing against yours."
    "You put your arm around her. She takes your hand and puts it on her breast. You give it a good squeeze."
    the_person "Goodnight [the_person.mc_title]..."
    mc.name "Night..."

    python: # she stays the night so she will have to wear the same outfit again the next day
        the_person.next_day_outfit = the_person.planned_outfit

    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_camilla_spend_the_night
    python: # init morning
        the_person.apply_outfit(special_fetish_nude_outfit)
        the_person.change_energy(200)
        mc.location.lighting_conditions = dark_lighting

    $ the_person.draw_person(position = "walking_away")
    "In the middle of the night, you stir a bit. The warm body next to you continues sleeping."
    "It takes you a few moments to remember... [the_person.possessive_title] invited herself over last night, and she's naked, right next to you!"
    "Your hand is cupping her chest. You give her hefty tits a squeeze, enjoying their heat and weight."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(10)
    the_person "Mmm..."
    "God, thinking about the latina goddess next to you in bed is getting you hard. She's still sleeping... but surely she wouldn't mind if you slipped inside her for a bit?"
    "You are both already naked... maybe you could just slide it between her legs for a bit, up against her pussy... that could be nice..."
    "You carefully move your hips back and down, then slowly push forward, your cock sliding in between her thighs..."
    the_person "Ahhh... [the_person.SO_name]..."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(15)
    "[the_person.title] is so out of it, she thinks you are her husband!"
    "As you slide up against her, you can feel a bit of heat and humidity escaping her crotch. She's definitely getting turned on too."
    "You let go of her tits and reach down between her legs. You use your hand to push your cock against her slit as much as possible and then start to thrust a bit."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #60
    the_person "[the_person.SO_name], que me cojan..."
    "You have no idea what she is saying, but she is definitely getting into it. You decide to go for it."
    "You take a couple more strokes, then use your hand to put your cock up. You slide into her wet cunt quite easily."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #85
    the_person "Que me jodan más fuerte..."
    "God, fucking married women is amazing. She is pushing her ass back against you now. You aren't sure if she's woken up or not but you don't really care."
    "You grope her tits roughly and start to really pound her. She is moaning loudly."
    $ mc.change_locked_clarity(50)
    $ the_person.change_arousal(25) #110
    the_person "Papi! punto de correrse!"
    "Did she just call you daddy? Either way, the urgency in her voice makes it clear she is finishing."
    "[the_person.possessive_title] shoves her ass back against you as she cums. Her helpless body quivers in delight. Her moans drive you even harder."
    $ the_person.have_orgasm()
    "The quivering pussy enveloping your cock is too much. You are going to cum!"
    "You decide to keep playing the part. You shove your erection in deep and let yourself go."
    the_person "Dame esa leche!"
    $ the_person.cum_in_vagina()
    $ the_person.draw_person(position = "walking_away")
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
    "You explode inside of [the_person.title]. You flood her cunt with wave after wave of cum. She moans and gasps."
    "When you finish, you collapse back in bed beside her. You put your arm around her, and feel her take your hand and move it to her breast again."
    "So... she definitely woke up at some point of that..."
    "You drift off to sleep again."
    $ mc.location.lighting_conditions = standard_outdoor_lighting
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = "back_peek")
    "You slowly wake up. When you stir, you see [the_person.possessive_title] looking at herself in your mirror on the wall, doing some makeup."
    "She hears you stir and turns her head to look at you."
    the_person "Good morning, señor..."
    mc.name "Good morning."
    the_person "I need to run some errands... Sorry, but I need to go."
    "You stand up and walk over to her. She turns as your approach her and you embrace."
    $ the_person.draw_person(position = "kissing")
    the_person "Thank you for last night... it was magical."
    mc.name "It was. Can we do it again soon?"
    "[the_person.title] falters for a moment."
    the_person "I'm not sure... Things are really confusing right now."
    $ the_person.draw_person()
    "[the_person.possessive_title] slowly pulls away from you."
    the_person "I need to go. Goodbye."
    mc.name "Bye."
    $ clear_scene()
    "[the_person.title] leaves your room. It was so hot, sleeping with such a sexy married woman."
    "It is nagging at you a little bit though. She's married to someone else. Are you really okay with this?"
    "You feel some pangs of jealousy. Maybe you could make her yours? Convincing her to leave her husband seems like a tall task."
    "Is that really what you want? To wreck someone's marriage? The guy doesn't seem that great though. Maybe you would be doing her a favor."
    "Either way, you can't help but feel like the time is coming soon that you are going to have to decide what you really want from your relationship with [the_person.title]."
    $ the_person.add_unique_on_room_enter_event(camilla_gives_anal_virginity)
    $ camilla.event_triggers_dict["formal_date"] = True
    return

label camilla_date_love_restore_label(the_person):
    pass


    $ the_person.story_event_log("love")
    return

label camilla_date_love_label(the_person):
    pass
    return

label camilla_gives_anal_virginity_label(the_person): #80
    "In this scene, camilla gives MC her anal virginity."
    $ the_person.add_unique_on_room_enter_event(camilla_decision_time)
    return

label camilla_anal_love_restore_label(the_person):
    pass


    $ the_person.story_event_log("love")
    return

label camilla_anal_love_label(the_person):
    pass
    return

label camilla_decision_time_label(the_person):
    "In this label, you help Camilla reach a decision. Will she leave her husband, or continue hotwifing?"
    $ the_person.story_event_log("love")
    return
