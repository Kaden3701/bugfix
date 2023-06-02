init 2 python:
    starbuck_candace_product_demo = Action("Candace helps with product demo", starbuck_candace_product_demo_requirement, "starbuck_candace_product_demo_label")
    starbuck_candace_recurring_event = Action("Candace and Starbuck hanging out", starbuck_candace_recurring_event_requirement, "starbuck_candace_recurring_event_label")

init -1 python:
    def starbuck_candace_product_demo_requirement(the_person):
        if starbuck.location == sex_store:
            if the_person.is_at_work:
                return True
        return False

    def starbuck_candace_recurring_event_requirement(the_person):
        if starbuck.location == sex_store and candace.location == sex_store:
            if day%7 == 5 and time_of_day == 3:  #Saturday evening
                return True
        return False

label starbuck_cargo_shipment_label(the_person):
    $ the_person.event_triggers_dict["Candi_event_start"] = True
    the_person "Hey partner. I was wondering if I might see you! I just got in some new stock. Want to check it out?"
    "Normally, going through freight at a mall store would be about the most boring thing you could imagine."
    "But this is not just any store! Going through boxes of sex store merchandise with [the_person.possessive_title] actually sounds pretty fun..."
    mc.name "Sure. Let's go take a look."
    "[the_person.title] puts a sign on the counter to ring the bell for service and motions for you to follow her. In the back storage area is a pallet of assorted toys, lingerie, videos, and other sex related items."
    "As you start to break down some of the boxes, you can't help but make jokes about some of the items."
    mc.name "Battery powered nipple clamps? Wow I didn't realize I was missing out on these!"
    "[the_person.title] laughs but also gets a little defensive."
    the_person "You might be surprised how popular they are! Especially with the cougars!"
    mc.name "Oh... Cougars eh? You mean like you?"
    the_person "Wow, okay, so we're gonna fight today? Is that what were gonna do?"
    "[the_person.title] sticks her tongue out at you, making it obvious she is just teasing."
    the_person "Oh. My. God... They're here!"
    "[the_person.title] is pulling a box out from the middle of the pallet. On the side of the box is a picture of dildos, with the questionable name of 'Double Girth Max 5000'."
    mc.name "Are those... Billy clubs?"
    the_person "No, but they might be the same size. It's the largest, suction cup mounted double dildo on the market!"
    "Hmmm... Suction cups?"
    mc.name "So you like... Mount that to the wall? Then back onto it?"
    the_person "Or on the floor, or rail, or a saddle, or... I mean whatever really. I've got to see this!"
    "She takes a box cutter and opens the box... She frowns a bit as she takes one out. It's enormous."
    the_person "Jesus... There's no way this fits in a person... This must be for stimulating cows or something!"
    mc.name "So are you going to make a demonstration video?"
    the_person "I had hoped to... But there's just no way..."
    "[the_person.possessive_title] seems a little disappointed. You can tell she had been looking forward to trying the toy, but the sheer size of it has her too afraid to even consider it."
    "Quietly, you continue working on the pallet of merchandise. You wonder if there is any way you could help her out."
    "As you think about it though, the amount of straight... Training... It would take to fuck that size is prohibitive. Maybe you could find someone else who could do it?"
    "You continue to think about it. Do you know anyone who might be capable of such a feat? Someone who never backs down from a sexual challenge?"
    "Someone who enjoys getting stretched to her limit? Who, let's face it, is probably also not that bright?"
    "Of course you know someone like that. [candace.title], the bimbo who you recently convinced to dump her boyfriend and work for you."
    "You aren't sure if she's ever ridden something that big, but you do know she would be up for trying. Now, you just consider how to bring it up with [the_person.title]..."
    mc.name "So... Let's say I knew someone... Who could do a demonstration video for us..."
    "[the_person.possessive_title] looks at you incredulously."
    the_person "I mean... I guess if there is a woman out there whose super power is taking enormous dildos, but I don't see how any normal person could manage this!"
    mc.name "Well... I have an employee who I sort of recruited from another company."
    mc.name "I don't know all the details of it, but I'm pretty sure she was drugged with something that has what seems to be permanent side effects. Some of which are an enormous sex drive, and the ability to take just about anything..."
    the_person "That's... Interesting? What other kind of side effects did it have?"
    mc.name "Well, unfortunately, it also destroyed most of her common sense. She is basically a dim witted bimbo."
    mc.name "I recruited her from her previous employer because he was taking advantage of her, paying her criminally low wages and forcing her to have sex for his own financial benefit."
    the_person "That's very kind of you... But won't asking her to let us do a demonstration video be basically the same thing?"
    mc.name "Honestly... I think if we showed it to her... I'm not sure we could stop her from trying it."
    mc.name "For sure though, we won't force her to do anything."
    mc.name "Maybe I could just bring her out here for a bit? We won't necessarily ask her to do it, but just get a feel for how she might respond. It would only be fair though, that we pay her some for her part in the demo."
    "[the_person.title] considers your proposal for a moment."
    the_person "I guess. Honestly, I kind of like doing the advertising, just me and you, ya know? But I guess once in a while bringing in a little extra talent couldn't hurt."
    mc.name "Don't worry, I won't let this impact our other endeavors."
    the_person "Okay... Bring her out sometime and we'll see what happens. What's the worst that could happen?"
    "You continue chatting with [the_person.title] as you finish breaking down her merchandise. Between the two of you, soon the job is done."
    the_person "Alright partner, I'll see you again soon? With your friend?"
    mc.name "Sounds good."
    "Alright, now just need to talk to [candace.possessive_title]. You aren't sure how to bring it up with her. Maybe just bring her out to the shop sometime, without telling her where you are going?"
    $ candace.add_unique_on_talk_event(starbuck_candace_product_demo)
    return

label starbuck_candace_product_demo_label(the_person):
    # the_person is candace (we always need a the_person for detailed UI)
    $ scene_manager = Scene()
    $ scene_manager.add_actor(the_person)
    mc.name "I have somewhere I want to take you. I think you'll enjoy it."
    "[the_person.title] cocks her head to the side and perks up a bit."
    the_person "Right now? In the middle of the work day?"
    mc.name "Yeah. I want you to meet a friend of mine."
    the_person "Oh! Okay! Does he have a nice dick too?"
    mc.name "My friend is a woman, but trust me, you won't regret this."
    the_person "Okay boss! You know I'm always up for whatever... Even other chicks!"
    $ mc.change_locked_clarity(10)
    "You exit the office and start walking over to the mall with [the_person.possessive_title] tagging along. She checks out a few people on the way over."
    # [Change to mall background]
    $ mall.show_background()
    "As you enter the mall, you've made up your mind. [the_person.title] is perfect for this. If anyone can take the Girth Max, it's her!"
    the_person "The mall? Did you bring me out here to try on some more clothes? We had so much fun last time... Remember?"
    mc.name "We aren't going to the clothes store today. I have somewhere else in mind."
    "You walk up to [starbuck.title]'s sex shop. As you walk inside, you look at [the_person.possessive_title]. Her eyes are wide with amazement."
    $ the_person.change_location(sex_store) # physically move candace to the sex store
    $ sex_store.show_background()
    the_person "Oh my God... Boss... That's... Oh my God what is this place??? Is this heaven?"
    "You are actually a little surprised. You had assumed that she had been into a place like this before, but it appears that you were mistaken."
    mc.name "No, this is a sex shop. And it's owned and operated by the friend I wanted to introduce you to."
    $ scene_manager.update_actor(the_person, position = "kissing")
    "[the_person.title] literally throws herself at you, wrapping her arms around you in a giant hug."
    the_person "Boss! I can't believe it! I must have been so good for you to bring me here! This is like, the best day ever!!!"
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    "Hearing the commotion, [starbuck.title] appears from an aisle and walks over. She looks at you a bit concerned."
    $ scene_manager.add_actor(starbuck, display_transform = character_center_flipped)
    starbuck "Hey partner... Everything okay?"
    "You start to answer but [the_person.possessive_title] immediately starts talking over you."
    the_person "Oh my God I'm more than okay! My boss just brought me here for the first time to this AMAZING PLACE. He said he even knows the owner? Can you believe it!?!"
    "Realization dawns on [starbuck.title]'s face."
    mc.name "Right. [the_person.fname], this is [starbuck.fname]. She's the one who owns this shop."
    the_person "Oh my god! It's so good to meet you!"
    $ scene_manager.update_actor(the_person, display_transform = character_center, position = "walking_away", z_order = 2)
    $ scene_manager.update_actor(starbuck, position = "kissing", z_order = 1)
    "[the_person.title] lets go of you. She immediately wraps her arms around [starbuck.title] and embraces her..."
    "Is she whispering in her ear? Well, so far it seems that [the_person.possessive_title] at least is enjoying her new acquaintance."
    "Hopefully [starbuck.possessive_title] has the patience for this too."
    starbuck "Hello there, it's nice to meet you too..."
    "[starbuck.title] gives her a hug back. Soon, [the_person.title] lets go and starts to look around the store."
    $ scene_manager.update_actor(the_person, display_transform = character_right, position = "walking_away")
    $ scene_manager.update_actor(starbuck, position = "stand4")
    the_person "Oh my! I didn't know this existed! Oh... Oh my..."
    "As [the_person.possessive_title] starts to wander off, you get a moment with [starbuck.title]."
    mc.name "Ah, well, as you can see, she's pretty enthusiastic."
    starbuck "Yeah! That was... Something else. I've never had a customer whisper in my ear that I'm doing gods work before."
    "She shakes her head and then chuckles."
    starbuck "I think I understand why you brought her out."
    mc.name "I tell you what. I'm going to walk with her around the store for a bit to get her acclimated, then we'll see about the toy in the back..."
    starbuck "Okay! I'll be up at the counter. Have fun!"
    "As [starbuck.possessive_title] heads up to the front of the store, you walk quickly and catch up with [the_person.title]. At the moment, she is going through a selection of crotchless panties."
    $ scene_manager.hide_actor(starbuck)
    $ scene_manager.update_actor(the_person, position = "stand3")
    the_person "Oh! Boss! Look at these! If I wore these to work with a skirt, you could just bend me over anywhere! You wouldn't even have to like, move my panties over or anything!"
    "A couple are browsing a couple bins away and hear her. The girl starts laughing and the guy gives you a grin and a thumbs up."
    mc.name "You're right. Let's take a few minutes and just walk around. There's all kinds of possibilities here."
    "You walk around with [the_person.possessive_title] for a bit, checking out the different items. Once in a while she'll ask you about something."
    the_person "But why do the nipple clamps need batteries?"
    mc.name "Well they can be programmed to give a small electrical shock..."
    $ the_person.change_arousal(15)
    the_person "Oh! That sounds... Amazing! Damn I should have brought a pen and paper, I need to start making a list..."
    "It really does have the same feeling as a kid in a candy shop. You're pretty sure she has decided to try and buy one of everything."
    the_person "I... Can't believe I had no idea this place existed... [the_person.mc_title]! Thank you for showing me this place!"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "[the_person.possessive_title] gets close to you. She reaches down and starts to rub your rapidly hardening cock through your pants. You quickly decide now is the time to bring up why your brought her here."
    mc.name "Actually, there's a reason I brought you out here. I was actually pretty certain you'd been here before now..."
    the_person "Oh? Does it involve that hard thing in your pants? Because looking at this sex stuff is really getting me, like, all worked up..."
    mc.name "I've got something different in mind. My friend? The one who runs the place? She's looking for help making an advertisement for a new product she just got in."
    mc.name "She's concerned about the size of it... I thought maybe you would be willing to give it a try and let us take a video."
    $ scene_manager.update_actor(the_person, position = "stand4")
    "[the_person.title] is looking at you confused. You can tell she is having trouble understanding what you are asking her to do."
    mc.name "I want you to fuck a giant double dildo while my friend and I take a video... If you want to I mean..."
    $ the_person.change_arousal(15)
    the_person "Oh! God boss, why didn't you just say so? That sounds like fun to me. Do you think... Do you think maybe your friend would be willing to mess around some? She is like, so fucking hot!"
    "Oh my. You hadn't considered trying to get both of them in the video some how. That would be a damn good video!"
    mc.name "That's a great idea... I'm not sure! Why don't we go talk to her!"
    the_person "Okay [the_person.mc_title]!"
    $ scene_manager.show_actor(starbuck, display_transform = character_center)
    "You walk with [the_person.title] up to the front of the store where [starbuck.possessive_title] is at. She looks at you two and hesitantly starts to ask."
    starbuck "Hey, so umm... Did [starbuck.mc_title] talk to you about..."
    the_person "I'll do it. Are you going to be in it too?"
    starbuck "Ah! I umm... I don't think I can, the toy is just a little too big for me..."
    the_person "You don't like, have to use the toy! Just like, maybe you could hold it and fuck me with it, or just let me eat you out or something!"
    "[starbuck.title] eyes widen a little in surprise. It seems, even as a sex shop owner, she was not expecting this level of excitement."
    starbuck "Well, I mean it does have suction cups... So I could probably mount it to some of the latex panties..."
    $ mc.change_locked_clarity(30)
    mc.name "It would probably be good, too, if we can work you into the video anyway, since you're the shop owner!"
    starbuck "Wow... Okay... Are you sure? The size of this thing is something else!"
    the_person "Damn right! Let's do it!"
    starbuck "Okay. [starbuck.mc_title], want to take her in the back room and maybe start getting her lubed up a bit? I'll see if I can rig something."
    $ scene_manager.hide_actor(starbuck)
    "You walk with [the_person.title] to the back. She starts to strip down as you grab some lube."
    $ scene_manager.strip_full_outfit(person = the_person)
    $ scene_manager.update_actor(the_person, position = "missionary")
    "When she finishes, she hops up on the counter, spreading her legs for you."
    the_person "Alright boss, lube me up! Don't be gentle with it either!"
    "You can see she is already pretty excited, so you decide to concentrate most of the lube on her anus. Soon you have two fingers buried in her ass and pumping them in and out."
    $ the_person.change_arousal(10)
    the_person "Mmm, that feels good..."
    "You stop for a second to squirt some more lube. You do your best to work it deep into her ass."
    # put a nude outfit on Starbuck
    $ starbuck.apply_outfit(Outfit("Nude"))
    # Template Holder for something like dark brown leather panties to Starbucks outfit? To make it look like she has something on#
    $ starbuck.outfit.add_lower(booty_shorts.get_copy(), [.15, .15, .15, .95])
    $ starbuck.outfit.add_feet(thigh_high_boots.get_copy(), [.15, .15, .15, .95])
    $ scene_manager.show_actor(starbuck, display_transform = character_center)
    $ mc.change_locked_clarity(30)
    "[the_person.title] is starting to moan when [starbuck.possessive_title] walks into the room. She's rigged the enormous double dick to some leather panties with some straps and velcro."
    starbuck "Glad to hear you are getting warmed up. Took me a bit to rig this. It's not perfect, but I think it will work!"
    the_person "Oh my God! That thing looks, like, amazing!"
    #"You watch intently as [starbuck.title] start to strip down..."
    "You never thought you would ever be in a position like this. You're about to film [starbuck.title], the sex shop owner, as she fucks [the_person.title], your bimbo office girl, with an enormous double headed dildo."
    "You pinch your arm. Yeah! You aren't dreaming this!"
    "[starbuck.possessive_title] puts on the strap-on. You hand her the lube so she can get it ready."
    mc.name "Okay... It would probably be best if [starbuck.title] can be facing the camera since she is the shop owner. [the_person.title] why don't you get down on your hands and knees and she can get behind you?"
    the_person "Mmm, that sounds good. And then you can come over, Boss, and I'll suck your..."
    mc.name "I have to run the camera. Maybe when we are done with the video we can have some fun though."
    if starbuck.is_jealous:
        starbuck "Hey now... I'm your girlfriend [starbuck.mc_title], don't be planning anything like that without me!"
    else:
        starbuck "I'll be surprised if you can walk after this hun, but if so I'm sure we can do something fun!"
    $ scene_manager.update_actor(the_person, display_transform = character_center, z_order = 2, position = "cowgirl")
    "Your [the_person.title] gets into position already wiggling her ass back and forth."
    the_person "I'm ready, stick it in!"
    $ scene_manager.update_actor(starbuck, display_transform = character_right_flipped, z_order = 1, position = "stand3")
    mc.name "Hang on, we have to start the video first. Usually [starbuck.title] does an intro too, then we'll get to the demo."
    the_person "Ugh, fine! What a tease!"
    "Everything appears to be all set up. You give a quick countdown, and then begin the video."
    starbuck "Hello folks! This is [starbuck.fname], from [starbuck.fname]'s Sex Shop, here with another demonstration video! This time we are demonstrating the brand new, Double Girth Maxx 5000!"
    "[starbuck.title] has an extra that she picks up and begins to go over the details to the camera."
    starbuck "Have a size queen in your life that won't shut up about big dicks? This double dildo has a full money-back guarantee that it will shut her up! Made with..."
    "You kind of zone out a bit as she goes over the construction and cleaning requirements. You notice [the_person.title] is starting to get a bit impatient also."
    the_person "Hey, are you gonna put that thing in me or not?"
    "[starbuck.title] just smiles and then introduces her assistant."
    starbuck "Today, to help me with the demonstration, is [the_person.fname]. One of my favorite features of this product is the suction cups, which have allowed me to attach it to these!"
    $ scene_manager.update_actor(starbuck, display_transform = character_center_flipped, z_order = 1, position = "kneeling1")
    "[starbuck.possessive_title] motions at the strap-on she's fashioned. While moving behind [the_person.possessive_title]."
    starbuck "Now, let's see if that guarantee holds up! Are you ready dear?"
    the_person "About time! I wasn't sure you were ever gonna... OHHHH!"
    "[the_person.possessive_title]'s eyes go wide as the enormous pair of phalli line up with her holes. [starbuck.title] holds her hips in place as she starts to push. [the_person.title] groans, only managing to sputter a couple of words out."
    the_person "So... full..."
    starbuck "Don't worry dear, it's about halfway in."
    "For a short moment, you think you notice a look of fear on [the_person.possessive_title]'s face, but it quickly changes to resolve."
    the_person "Ughhh... Keep... Going!"
    "With a firm grip on her hips, [starbuck.title] drives a bit deeper. [the_person.title] is gasping as she tries to take the final few inches. Despite her near constant sexual escapades, the toy is nearly too much."
    starbuck "Okay, here we go, one last push!"
    "With great effort, [starbuck.possessive_title] drives the last of the toy inside of her. [the_person.title]'s foot raises off the ground reflexively."
    starbuck "Wow! You did it! How does it feel girl?"
    the_person "It's... So... Full...!"
    "For once, [the_person.title] appears to be mostly speechless. You suppose there might be something to that 'shut her up' guarantee."
    starbuck "Let me know when you're ready for me to move."
    the_person "Just... Mmmmmmm! Give me a... a minute!"
    "[starbuck.title] takes the opportunity to talk about the product."
    starbuck "One thing I noticed, even though it's made from silicone, the product has a pleasant firmness to it as well. If you need to be pushy with it, it feels good and sturdy and should be able to handle it."
    "After a few more moments, [the_person.possessive_title] starts to slowly move her hips."
    the_person "Okay... Let's do this..."
    "[starbuck.possessive_title] gives her one slow, firm stroke. [the_person.title] just gasps as it starts to slide back in. It takes both hands on her rump for [starbuck.title] to push it all the way back in."
    starbuck "Wow, she is taking this thing like a champ! How are you holding up babe?"
    the_person "I'm... Good. It's good! Intense..."
    "[the_person.possessive_title] is having trouble making words. [starbuck.title] gives her another stroke. This time when she pushes back in she doesn't have to be quite as forceful."
    the_person "Ahh! Oh god sorry I'm not gonna last long!"
    starbuck "I can imagine why!"
    "[starbuck.possessive_title] gives another smooth stroke. [the_person.title] is starting to get into it now, willing herself to accept the enormous dildo."
    "This time she doesn't stop when it is all the way in, she pulls back right into another stroke."
    "Stroke...... Stroke...... Stroke......"
    "A slow, methodical pace is being set. [the_person.title] is panting and groaning with each stroke."
    the_person "Oh god... Oh god!"
    $ the_person.change_arousal(60)
    $ starbuck.change_arousal(15)
    $ mc.change_locked_clarity(50)
    $ the_person.have_orgasm()
    "[the_person.title]'s body begins to convulse as she begins to orgasm. [starbuck.possessive_title] keeps fucking her with the same methodical pace."
    "Her orgasm should be winding down now... But incredibly, it doesn't. [starbuck.title] speeds up just slightly and soon [the_person.possessive_title] is getting ready to orgasm again."
    the_person "Gah!!! Fuck oh fuck!"
    $ the_person.change_arousal(60)
    $ starbuck.change_arousal(15)
    $ mc.change_arousal(10)
    $ the_person.have_orgasm()
    "[the_person.title] orgasms again, her body getting weak as she succumbs to the incredible pleasure and pressure the toy is providing her. [starbuck.possessive_title] responds by speeding up again."
    "She still isn't going that fast, but the size of the toy makes the sensations overwhelming. She cries out as another orgasm begins to take her."
    the_person "Ahh! Holy fucking hell!"
    $ the_person.change_arousal(60)
    $ starbuck.change_arousal(15)
    $ mc.change_arousal(10)
    $ the_person.have_orgasm(half_arousal = False)
    "[starbuck.possessive_title] is forced to stop literally mid stroke as [the_person.title] orgasms forcefully, her holes squeezing so hard she momentarily can't push the dildo back in."
    "She grabs her hips and slowly but forcefully push the toy deep and then leaves it there, fully sheathed as [the_person.title] orgasms."
    "Completely spent, [the_person.possessive_title]'s arms give out and she collapses forward. The toy pulls out from her rump making a lewd squelch."
    "[the_person.title] is now in a heap on the floor. Once in a while an arm or a leg twitches as she tries to recover."
    $ scene_manager.update_actor(the_person, position = "missionary")
    $ scene_manager.update_actor(starbuck, display_transform = character_right, position = "stand4")
    "She manages to roll on her back, her breathing ragged. [starbuck.title] stands up, her enormous double dildo glistening in victory."
    starbuck "Well, I'd say the product works as advertised!"
    "[starbuck.title] gives a run down on the product price, and soon the video is complete. You stop recording."
    the_person "... ffuuuuuuuck... boss I don't think I can get up..."
    mc.name "It's okay. Take your time and recover."
    the_person "Yeah... you two... can I watch? Like... I can't do anything... now but... if you want to fuck... can I just watch?"
    $ mc.change_locked_clarity(20)
    "Even after getting the pounding of a lifetime, [the_person.possessive_title] still wants to be involved with sexy times."
    "[starbuck.title] looks at you hesitantly. Your cock aches after witnessing the previous spectacle, and you're sure she could get off too."
    mc.name "Sounds good. I think you deserve to be able to watch, after helping us make that video!"
    starbuck "That's true... okay, how do you want to... HEY!"
    $ scene_manager.update_actor(starbuck, position = "back_peek")
    "You grab [starbuck.title] and spin her around. You push her against the wall and quickly strip off her augmented panties."
    $ scene_manager.strip_full_outfit(person = starbuck)
    "Your cock is out in an instant, and soon you are behind her."
    "You rub your dick along her slit a few times, first up and down, and then side to side. You line yourself up and begin to push inside of her."
    $ mc.change_locked_clarity(30)
    "[starbuck.possessive_title] arches her back a bit. She steals a glance back at you while you enjoy the warm, slick grip of her pussy."
    "You both look over at [the_person.title]. She is watching intently and has one hand between her legs, lightly touching herself."
    "You put your hands on [starbuck.title]'s hips as you begin to fuck her. She moans and puts her hand on top of yours, encouraging you."
    starbuck "Give it to me [starbuck.mc_title]! I'm so hot from earlier..."
    $ starbuck.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "You immediately set the pace, giving it to her hard and rough. Her ass cheeks clap with each thrust."
    "[starbuck.title] pushes back against you, meeting every single thrust. Your balls swing forward and smack her clit with each thrust."
    starbuck "Oh fuck! Oh that's it, yes!"
    "[the_person.title] continues to watch, her fingers working circles around her clit as you go at it with [starbuck.possessive_title]."
    $ starbuck.change_arousal(20)
    $ mc.change_locked_clarity(30)
    "[starbuck.title]'s slit is so smooth, it's getting to be too much to bear. Instead of slowing down to try and last longer though, you speed up even more."
    starbuck "Oh my god I'm gonna cum... I'm gonna cum!"
    mc.name "Oh fuck me too."
    starbuck "Cum with me [starbuck.mc_title]! Shove it in deep and don't pull out until we're both finished!"
    mc.name "Like you could stop me if you tried!"
    $ starbuck.change_arousal(40)
    $ mc.change_locked_clarity(50)
    "You push yourself in as deep as you can. [starbuck.title]'s feet are actually off the ground as your forcefully pin her to the wall."
    "You feel her pussy start to quiver around you as she starts to cum and that's it, you can't take anymore."
    "You hear a gasp from across the room as you begin to fire your load deep inside of [starbuck.possessive_title]."
    the_person "Oh my god, I can see it pulsating..."
    starbuck "Yes! Fuck yes!"
    $ starbuck.have_orgasm(half_arousal = False)
    "Your control over [starbuck.possessive_title] is complete as she helplessly cums all over you. Your cock is planting your seed deep in her spasming cunt."
    "You keep her pinned there until the last of your aftershocks wash over both of you."
    $ starbuck.cum_in_vagina()
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
    $ mc.reset_arousal()
    "As you slowly pull out, your cum immediately starts pouring out of [starbuck.possessive_title] and down her leg."
    the_person "Oh god... I wish I had some..."
    "[the_person.possessive_title] starts crawling over to [starbuck.title]. When she finally turns around, [the_person.title] is on her hands and knees below her."
    $ scene_manager.update_actor(starbuck, position = "against_wall", z_order = 1)
    $ scene_manager.update_actor(the_person, position = "doggy", display_transform = character_right_flipped, z_order = 2)
    "When she turns around, without even asking, [the_person.title] lifts her leg and starts to lick your cum off of [starbuck.possessive_title]'s leg."
    starbuck "Oh! Oh my..."
    if the_person.is_bald:
        "[starbuck.title] runs her hands over [the_person.title]'s smooth head as her tongue goes higher between her legs. She moans as [the_person.possessive_title] licks around her pussy."
    else:
        "[starbuck.title] runs her hands through [the_person.title]'s hair as her tongue goes higher between her legs. She moans as [the_person.possessive_title] licks around her pussy."
    starbuck "Oh fuck... sorry I... I can't do that right now!"
    "[the_person.possessive_title] stops, understanding. Damn what a scene."
    mc.name "Well... I'd call today a complete success. I'm going to go ahead and edit that video while you two recover..."
    $ scene_manager.update_actor(starbuck, position = "stand4")
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped, position = "stand3")
    starbuck "Ah... yes that would be good. [the_person.fname]... how would you like to help me do more product demos sometime?"
    the_person "Oh. my. god. YES! Yes please!"
    starbuck "What do you think about Saturday? We could even make it a regular thing."
    "You go over to [starbuck.possessive_title]'s computer and start to work on the video. The two girls are talking about ideas for new videos."
    "By the time you finish a quick edit of the video, the two girls are talking like old friends. You feel like they have REALLY hit it off!"
    "Of course, sharing a love for sex and all things sex related has really helped."
    mc.name "Alright, the video is done. I'm going to head out now. Need anything before I go?"
    starbuck "Nope! [the_person.fname] and I are going to hang out for a bit. Thanks for bringing her out [starbuck.mc_title]!"
    the_person "Yeah! I like... can't believe how amazing today has been!"
    "You turn to leave the two girls as they chat... still naked..."
    "They have become almost instant best friends, and it sounds like they are planning to get together every Saturday here at the shop. Maybe you should swing by and join them sometime?"
    $ town_relationships.update_relationship(the_person, starbuck, "Best Friend")
    $ the_person.set_override_schedule(sex_store, the_days = [5], the_times = [3])
    $ starbuck.set_override_schedule(sex_store, the_days = [5], the_times = [3])
    $ starbuck.add_unique_on_room_enter_event(starbuck_candace_recurring_event)
    $ candace.event_triggers_dict["friends_with_starbuck"] = day
    $ starbuck.apply_planned_outfit()
    $ candace.apply_planned_outfit()
    $ mc.location.show_background()
    $ jump_game_loop()  # jump out of dialog and return to office
    return

label starbuck_candace_recurring_event_label(the_person):
    # the_person is starbuck (we always need a the_person for detailed UI)
    "Knowing that [the_person.title] and [candace.possessive_title] have started getting together on Saturdays, you decide to swing by the sex shop and see how it is going."
    "The shop is closed, as it usually is at this time. However, [the_person.possessive_title] gave you a key when you became partners."
    "You quietly unlock and door and slip inside, being careful to lock it behind you."
    "Once inside, the lights are dark in the shop itself. As you walk behind the counter, you notice the light in the back room is on."

    #TODO add links to appropriate random actions that could be occurring

    if the_person.event_triggers_dict.get("knows_candace_cured", False):
        "Sorry, this event is a work in progress!"
        # call starbuck_candace_orgasm_denial_contest_label(the_person, candace) from _candace_and_Starbuck_denial_Scene_01
    elif not the_person.event_triggers_dict.get("knows_candace_cured", False) and candace.personality == bimbo_personality:
        #TODO write an event here for candace and starbuck to do together
        "Sorry, this event is a work in progress!"
        pass
    else:
        $ scene_manager = Scene()
        "You hear some lively but friendly discussion coming from the back room. It sounds like [the_person.title] and [candace.possessive_title] are catching up."
        "You round the corner and see the two girls sitting at a table and chatting."
        $ scene_manager.add_actor(the_person, position = "sitting")
        $ scene_manager.add_actor(candace, position = "sitting", display_transform = character_center_flipped)
        the_person "Wow! That's amazing. This is so incredible [candace.fname]..."
        candace "It really is."
        "As you enter the room, the girls notice you."
        the_person "Ah!!! [the_person.mc_title]! The man of the hour!"
        $ scene_manager.update_actor(the_person, position = "kissing")
        "[the_person.title] jumps up and runs over to you, wrapping her arms around you in a huge hug."
        the_person "I can't believe it! You managed to restore [candace.fname]... you know..."
        "She lets go of you, then punches you in the arm."
        $ scene_manager.update_actor(the_person, position = "stand2", emotion = "angry")
        the_person "You didn't even tell me! God I feel like we've become almost best friends since you introduced us... and you don't even tell me what you were up to!?!"
        candace "There was no telling if it would even be effective or not. It was truly groundbreaking [the_person.fname]."
        the_person "I know! I know... I just... I mean that could have gone wrong too, right?"
        candace "I didn't realize it at the time, but in hindsight, I agree that it was worth the risk. I'm very fortunate [candace.mc_title] made the decisions he did!"
        "You see her expression soften."
        $ scene_manager.update_actor(the_person, position = "stand2", emotion = "happy")
        the_person "I'm sorry I didn't mean to downplay this. It really is incredible."
        the_person "Thank you partner. It's amazing what you have done for her. I'll never forget it!"
        $ the_person.change_stats(happiness = 10, obedience = 10, love = 10)
        $ scene_manager.add_actor(the_person, position = "sitting")

        "[the_person.possessive_title] sits back down and starts talking with [candace.title] again. You can tell they are going to be chatting for a while."
        mc.name "Well, I can see you two have some catching up to do."
        the_person "See you around partner!"
        candace "Take care [candace.mc_title]."
        "You head out from the store, giving the two girls time to catch up on things."
        $ the_person.event_triggers_dict["knows_candace_cured"] = True
        $ scene_manager.clear_scene()

    $ the_person.add_unique_on_room_enter_event(starbuck_candace_recurring_event)
    return

label starbuck_candace_orgasm_denial_contest_label(the_person_one, the_person_two):
    python:
        scene_manager = Scene()
        the_person_one.arousal = 0
        the_person_two.arousal = 0

    "You listen closely and hear... The girls are just chatting?"
    if not the_person_one.event_triggers_dict.get("orgasm_denial_discovered", False):
        "You peek around the corner and see [the_person_two.title] and [the_person_one.possessive_title], sitting at a table, each with a small cup in front of them. [the_person_one.title] is talking about her day."
        $ scene_manager.add_actor(the_person_one, position = "sitting")
        $ scene_manager.add_actor(the_person_two, position = "sitting", display_transform = character_center_flipped)
        the_person_one "Yeah business was a little slow, except one couple came in. They must have just gotten together or something, because they bought a full set up of stuff."
        "She takes a sip from her cup."
        the_person_one "You could see the looks in their eyes, they could barely keep their hands off each other!"
        "This is considerably more docile than you expected. You decide to make your presence known."
        mc.name "Good evening ladies. Having some coffee?"
        the_person_two "Tea, actually. I brought some oolong tea I got from an Asian market. Would you like some?"
        "You nod. [the_person_two.title] starts to pour you a cup as you come and sit with the two girls."
        the_person_one "Well [the_person_two.fname], so far so good!"
        mc.name "What is so good?"
        the_person_one "She bet that you would show up tonight. We decided to make another bet, one you can help us out with here in a bit..."
        mc.name "Oh? What would that be?"
        "[the_person_two.title] quickly cuts you off."
        the_person_two "You'll find out, but we weren't supposed to tell you about it yet, were we [the_person_one.fname]!?!"
        the_person_one "Right you are honey."
        "[the_person_one.title] shifts in her seat a bit awkwardly."
        $ the_person_one.change_arousal(15)
        $ the_person_two.change_arousal(15)
        the_person_one "So, how was your day [the_person_one.mc_title]."

        "You take a few moments to talk about how your day is going, before taking a sip of your tea. Wow that is really good. The flavor is light but crisp."
        mc.name "[the_person_two.title] this tea is excellent, where'd you get it from?"
        "She takes an odd pause before she answers."
        the_person_two "It's... Ahhh... I think I got it at the Asian market, you know over by the coffee shop downtown?"
        $ the_person_one.change_arousal(20)
        $ the_person_two.change_arousal(30)
        "Ever since you cured her bimboism, [the_person.possessive_title] has been razor sharp, especially with details and memory. Something seems a little weird with her..."
        "You look over at [the_person_one.possessive_title]. Are her cheeks a little flushed? Her nipples seem firm too. She definitely has some telltale signs of arousal... But why are they acting so funny? You decide to play it cool for now."

        mc.name "Any new product come in lately [the_person_one.title]?"
        "You think you hear... Is that buzzing?"
        $ the_person_one.change_arousal(20)
        $ the_person_two.change_arousal(30)
        the_person_one "Ohhhhh... mmm... wow, yeah funny you would ask. I'll show you when we get done here..."
        "You can hear it plainly now, an electric sounding buzz and whirring. Are they wearing some kind of vibrating panties?"
        $ mc.change_locked_clarity(10)
        "You can feel yourself getting hard. You wonder what exactly the bet is and what they are betting on."
        $ the_person_one.change_arousal(20)
        $ the_person_two.change_arousal(30)
        "[the_person_two.title] is starting to breath hard, once in a while a moan escapes. Suddenly, she breaks."
        the_person_two "Oh! Oh fuck I'm cumming!"
        "She leans forward a bit as her body starts to twitch."
        $ the_person_two.have_orgasm(half_arousal = False)

        "[the_person_one.title] jumps up."
        $ scene_manager.update_actor(the_person_one, position = "stand2")

        the_person_one "Yes! Ohhh, fuck. I win! Gotta get this thing off..."
        "[the_person_one.title] quickly strips her bottoms off."
        $ scene_manager.strip_to_vagina(person = the_person_one)
        "Once naked, she pulls a toy out from her cunt. It is vibrating and twisting in her hand."

        the_person_one "Ahh, so... This is the new product... It's a programmable phallus. I made a sample program that starts slow, but slowly gets faster and the vibrations get stronger over time."
        $ scene_manager.update_actor(the_person_two, position = "stand4")
        "You notice that [the_person_two.possessive_title] has recovered and is standing up now also. She it's starting to take her clothes off."
        $ scene_manager.strip_to_vagina(person = the_person_two)
        "You watch as she takes the same toy out of her snatch."
        the_person_two "Oh god that was great. Can I keep this one? How much do I owe you?"

        "[the_person_one.title] waves her off."
        the_person_one "Don't worry about it, this whole thing was totally worth it."

        mc.name "So... What was the bet, anyway?"
        the_person_one "Oh! That's the fun part. We bet that whoever could go the longest without cumming or tipping you off to what was going on would win. The winner gets to fuck you while the loser has to watch!"
        $ mc.change_locked_clarity(50)

        the_person_two "Oh man... I wanted to win so bad... But as soon as you sat down and the scent of your cologne hit me it was over. You smell so good and manly... Mmmm..."
        mc.name "I mean, I'm sure I could probably go a couple rounds..."

        the_person_one "Not a chance! She thought she could win but I totally called her bluff and now you are mine!"
        "[the_person_one.title] seems to be really getting into this. But she also looks really aroused... You can tell she was close to finishing too! Her labia are swollen and wet with moisture."

        the_person_two "Don't worry [the_person_two.mc_title]... I don't mind watching!"
        "[the_person_one.title] looks at you."
        the_person_one "Why don't you just sit back. I'll take good care of you!"

        call get_fucked(the_person_one, the_goal = "vaginal creampie") from _call_get_fucked_candace_starbuck_teamup_orgasm_denial_intro_01
        "Damn... [the_person_one.title] was right. She really did take care of you! You start to clean yourself up."

        $ scene_manager.update_actor(the_person_one, position = None)

        "[the_person_one.title] starts to clean herself up, but [the_person_two.possessive_title] quickly stops her."
        the_person_two "Hang on!"
        if the_person_one.has_creampie_cum:
            $ scene_manager.update_actor(the_person_one, position = "against_wall", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "doggy", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] lifts [the_person_one.possessive_title]'s leg. She begins to lick clean the cum that has begun to run down her legs."
        elif the_person_one.has_ass_cum:
            $ scene_manager.update_actor(the_person_one, position = "back_peek", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "doggy", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] gets behind [the_person_one.possessive_title]. She begins to lick clean the cum that has begun to run down her ass."
        elif the_person_one.has_tits_cum:
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "walking_away", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] embraces [the_person_one.possessive_title]. She leans forward and begins to lick clean the cum on [the_person_one.title]'s tits."
        elif the_person_one.has_stomach_cum:
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "doggy", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] gets down next to [the_person_one.possessive_title]. She begins to lick clean the cum that has begun to run down her stomach."
        elif the_person_one.has_face_cum:
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "walking_away", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] embraces [the_person_one.possessive_title]. She leans forward and begins to lick clean the cum on [the_person_one.title]'s face."
        elif the_person_one.has_mouth_cum:
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "walking_away", display_transform = character_right_flipped, z_order = 2)
            "[the_person_two.title] embraces [the_person_one.possessive_title]. The begin to make out, and you can see your cum getting swapped between them."
        else:
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "walking_away", display_transform = character_right_flipped, z_order = 2)
            "The girls embrace, making out out for a bit."
        "Even though she's been cured of her bimboism, it's good to see that [the_person_one.title] still loves the taste of cum."
        $ mc.change_locked_clarity(20)
        "As the girls do their thing, you decide to head out. You say goodbye and slip out from the sex shop."
        $ the_person_one.event_triggers_dict["orgasm_denial_discovered"] = True
    else:
        "You peek around the corner and see [the_person_two.title] and [the_person_one.possessive_title], sitting at a table, each with a small cup in front of them. [the_person_one.title] is talking about her day."
        python:
            for i in range(3): #This time we start without bottoms
                the_person_one.outfit.remove_random_lower(top_layer_first = True)
                the_person_two.outfit.remove_random_lower(top_layer_first = True)
            scene_manager.add_actor(the_person_one, position = "sitting")
            scene_manager.add_actor(the_person_two, position = "sitting", display_transform = character_center_flipped)
        "You quickly notice they are naked below the table. You assume they are sitting on the programmable dildos again."
        "You decide not waste any time."
        mc.name "Good evening ladies. Sharing some tea again?"
        the_person_two "That's right. Care for some?"
        "You walk over to them. Now that you know what you are listening for, you recognize the faint whir of the sex toys, during their work inside the two beautiful girls."
        mc.name "Not for me. Having another contest?"
        the_person_one "You know it! Same stakes as last time. Loser watches the winner get fucked."
        "You decide not to sit this one out."
        mc.name "I think that since I'm involved in this wager, I should be able to have a part in the contest."
        the_person_two "I suppose that would be okay... but don't try to swing the results too much!"
        mc.name "Or what?"
        "[the_person_two.title] raises her eyebrow."
        the_person_one "Hey, all's fair in love and war. If [the_person_one.mc_title] decides to make one of us cum first, I say it's fair game!"
        "[the_person_two.title] gives a short fake pout."
        the_person_two "Fine... let's do this!"
        $ the_round = 1
        $ cock_available = False
        while (the_person_one.arousal_perc < 100 and the_person_two.arousal_perc < 100): #Break the loop when someone orgasms.
            $ mc.change_locked_clarity(20)
            "What do you want to do?"
            menu:
                "Kiss [the_person_one.title]'s neck":
                    "You step over behind [the_person_one.possessive_title]. You rub her shoulders gently and lean down next to her ear. She gets goosebumps when you whisper."
                    mc.name "Be a good girl and cum for me..."
                    "You lick and nibble at her ear and slowly work your way down her neck."
                    the_person_one "Ahhh, fuck... I think it's [the_person_two.fname]'s turn next!"
                    $ the_person_one.change_arousal(the_person_one.get_opinion_score("kissing") + 5)
                "Kiss [the_person_two.title]'s neck":
                    "You step over behind [the_person_two.possessive_title]. You rub her shoulders gently and lean down next to her ear. She gets goosebumps when you whisper."
                    mc.name "Be a good girl and cum for me..."
                    "You lick and nibble at her ear and slowly work your way down her neck."
                    the_person_two "Isn't it [the_person_one.fname]'s turn now?"
                    $ the_person_two.change_arousal(the_person_two.get_opinion_score("kissing") + 5)
                "Grope [the_person_one.title]'s tits" if the_person_one.tits_available:
                    "You get behind [the_person_one.possessive_title]. You run your hands slowly around he neck, collar, and down until they rest on her chest."
                    if the_person_one.has_large_tits:
                        "You grope her [the_person_one.tits_description] in your hands. The heat and softness of them feel amazing. She cries out when you pinch her nipples."
                    else:
                        "You grope her [the_person_one.tits_description] in your hands. The heat and firmness of them feel amazing. She cries out when you pinch her nipples."
                    the_person_one "Ah! Oh god that feels nice..."
                    $ the_person_one.change_arousal(5)
                "Grope [the_person_two.title]'s tits" if the_person_two.tits_available:
                    "You get behind [the_person_two.possessive_title]. You run your hands slowly around he neck, collar, and down until they rest on her chest."
                    if the_person_two.has_large_tits:
                        "You grope her [the_person_two.tits_description] in your hands. The heat and softness of them feel amazing. She cries out when you pinch her nipples."
                    else:
                        "You grope her [the_person_two.tits_description] in your hands. The heat and firmness of them feel amazing. She cries out when you pinch her nipples."
                    the_person_two "Oh! God boss don't make me lose again please!"
                    $ the_person_two.change_arousal(5)
                "Just watch":
                    pass
                "Strip [the_person_one.title]'s top" if not the_person_one.tits_available:
                    "You step behind [the_person_one.possessive_title]. You reach down and grope her tits through her top."
                    mc.name "It's time to get these girls out in the open now..."
                    the_person_one "Whatever you say, partner..."
                    "You reach down and peel off her clothing. She doesn't resist at all."
                    $ scene_manager.strip_full_outfit(person = the_person_one)
                    "[the_person_one.title] gives a little shiver, now that she's naked, but she doesn't say a word."
                    $ the_person_one.change_arousal(the_person_one.get_opinion_score("showing her tits") + 5)
                "Strip [the_person_two.title]'s top" if not the_person_two.tits_available:
                    "You step behind [the_person_two.possessive_title]. You reach down and grope her tits through her top."
                    mc.name "It's time to get these girls out in the open now..."
                    "You reach down and peel off her clothing. She doesn't resist at all."
                    $ scene_manager.strip_full_outfit(person = the_person_two)
                    "[the_person_two.title] gives a little shiver, now that she's naked."
                    the_person_two "Mmm... is it cold in here?"
                    $ the_person_two.change_arousal(the_person_two.get_opinion_score("showing her tits") + 5)
                "Grope [the_person_one.title]'s tits (disabled)" if not the_person_one.tits_available:
                    pass

                "Grope [the_person_two.title]'s tits (disabled)" if not the_person_two.tits_available:
                    pass
                #TODO brief blowjob, handjob scenes
            if the_round < 3:
                "As the game continues, you can hear the faint buzz of the toys the girls are sitting on. You can tell this is going to be a tight game!"
                $ the_person_one.change_arousal(5)
                $ the_person_two.change_arousal(5)
            elif the_round < 6:
                "You can easily hear the vibrators now, as they work their magic inside of the two girls."
                $ the_person_one.change_arousal(8)
                $ the_person_two.change_arousal(8)
                "Thinking about the pleasure they are getting is starting to arouse you."
                $ mc.change_arousal(3)
                if renpy.random.randint(0,2) == 0 and not cock_available:
                    "The excitement is getting to be too much. You decide to get more comfortable. You quickly disrobe."
                    "[the_person_one.title] gasps when your cock springs free. [the_person_two.title] is staring at it, hungrily."
                    mc.name "It's time to take things up a notch."
            else:
                "The toys have shifted into their highest settings. The girls are beginning to moan and gasp, just trying to sit still is a challenge."
                $ the_person_one.change_arousal(10)
                $ the_person_two.change_arousal(10)
                "The distinct smell of feminine arousal in the air, mixed with punctuations of moans and gasps is really starting to turn you on."
                $ mc.change_arousal(3)
                if not cock_available:
                    "The excitement is getting to be too much. You decide to get more comfortable. You quickly disrobe."
                    "[the_person_one.title] gasps when your cock springs free. [the_person_two.title] is staring at it, hungrily."
                    mc.name "It's time to take things up a notch."
            if renpy.random.randint(0,1) == 0:
                if the_person_one.arousal_perc > 80:
                    "You look at [the_person_one.possessive_title]. Her whole body is jiggling as she continually adjusts herself in her seat, vainly trying to keep from cumming."
                    "She isn't going to last much longer!"
                elif the_person_one.arousal_perc > 40:
                    "You look at [the_person_one.possessive_title]. Her nipples are hard with arousal, and you notice her cheeks getting flush. She is getting excited!"
                else:
                    "You look at [the_person_one.possessive_title]. She sits easily for now, but you know the game has only just begun."
            else:
                if the_person_two.arousal_perc > 80:
                    "You look at [the_person_two.possessive_title]. She is panting non stop and is constantly shifting her weight in her seat, trying to manage the pleasure she is getting from the toy."
                    "She isn't going to last much longer!"
                elif the_person_two.arousal_perc > 40:
                    "You look at [the_person_two.possessive_title]. Once in a while she catches her breath when the toy hits a particularly sensitive spot, and she has a far away look in her eyes."
                else:
                    "You look at [the_person_two.possessive_title]. She sits easily for now, but you know the game has only just begun."
            $ the_round += 1

        if (the_person_one.arousal_perc >= 100 and the_person_two.arousal_perc >= 100): #They both orgasm together.
            $ the_person_one.have_orgasm(half_arousal = False)
            the_person_one "Oh... OH! OH FUCK!"
            $ the_person_two.have_orgasm(half_arousal = False)
            the_person_two "Oh fuck me! OH I'M CUMMING!"
            "The two girls both begin to moan as they cum together in unison. Geeze, this one seems too close to call?"
            "You give your shaft a couple strokes... two girls orgasming on either side of you is pretty fucking hot!"
            $ mc.change_locked_clarity(50)
            if willing_to_threesome(the_person_one, the_person_two):
                "As the girl slowly finish their orgasms, they both notice you, stroking yourself. [the_person_two.title] reaches out and grabs your arm, stopping you."
                the_person_one "Wow... was that a tie?"
                the_person_two "Yes it was."
                the_person_one "Does that mean... we have to share him?"
                the_person_two "That seems the most reasonable action."
                $ scene_manager.update_actor(the_person_one, position = None, display_transform = character_center_flipped)
                $ scene_manager.update_actor(the_person_two, position = None, display_transform = character_right)
                "The girls get up and start to walk over to you, predatorily. You decide to take charge before things get out of hand."
                mc.name "Alright, I know just what to do."
                "The girls stop and wait for your direction."
                call start_threesome(the_person_one, the_person_two) from _double_winners_means_threesome_time_01
                "When you are finished, you and the girls all get up together."
                $ scene_manager.update_actor(the_person_one, position = None, display_transform = character_center_flipped)
                $ scene_manager.update_actor(the_person_two, position = None, display_transform = character_right)
                the_person_one "Wow... we should tie again next time."
                the_person_two "That was certainly an acceptable outcome..."
                the_person_one "Next week?"
                "The girls agree to meet again next week."
            else:
                "Somehow though, you manage the will to stop. The girls are both exhausted from their contest. Slowly, they start to get up."
                $ scene_manager.update_actor(the_person_one, position = None)
                $ scene_manager.update_actor(the_person_two, position = None)
                the_person_one "Damn. A tie? What does that mean?"
                the_person_two "I guess that means we are both losers. I'm sorry boss... I... I don't think I can manager another round right now."
                the_person_one "Me neither. Next week though, I'm totally gonna win!"
                "The girls agree to meet again next week."
        elif the_person_one.arousal_perc >= 100 : #Starbuck cums first
            the_person_one "Oh... OH! OH FUCK!"
            "[the_person_one.possessive_title] squeals as her orgasm hits her. Her chest bounces as her body convulses."
            $ the_person_one.have_orgasm(half_arousal = False)
            the_person_two "Yes! Oh my god [the_person_two.mc_title] I need your cock so bad..."
            $ scene_manager.update_actor(the_person_two, position = None)
            "[the_person_two.title] stands up, she quickly pulls out the wildly moving dildo and tosses it aside. She pushes you back onto the table then climbs up on top of you."
            call get_fucked(the_person_two, the_goal = "vaginal creampie", private= False, start_position = cowgirl, start_object = make_table()) from _call_get_fucked_call_get_fucked_candace_won_orgasm_contest_01
            $ scene_manager.update_actor(the_person_one, position = None, display_transform = character_center_flipped)
            $ scene_manager.update_actor(the_person_two, position = None, display_transform = character_right)
            "After finishing, [the_person_two.title] gets up off of you. You notice [the_person_one.title] has recovered from her earlier orgasm and is standing to the side, watching."
            the_person_one "Mmm, that was fun. I swear, I'll win next time!"
            the_person_two "The odds are not in your favor girl. Next week?"
            "The girls agree to meet again next week."

        else: #Candace loses again
            the_person_two "Oh fuck me! OH I'M CUMMING!"
            "[the_person_two.possessive_title] arches her back and moans as her orgasm hits her. Her body quakes with each wave."
            $ the_person_two.have_orgasm(half_arousal = False)
            the_person_one "Once again the champion!"
            $ scene_manager.update_actor(the_person_one, position = None)
            "[the_person_one.title] stands up. She pull the dildo from her cunt with a squelch and sets it carefull on the table. She pushes you back onto the table."
            the_person_one "Mmm, don't worry partner, I'll be gentle!"
            call get_fucked(the_person_one, the_goal = "vaginal creampie", private= False, start_position = cowgirl, start_object = make_table()) from _call_get_fucked_starbuck_won_orgasm_contest_01
            $ scene_manager.update_actor(the_person_two, position = None, display_transform = character_center_flipped)
            $ scene_manager.update_actor(the_person_one, position = None, display_transform = character_right)
            "After finishing, [the_person_one.title] gets up off of you. You notice [the_person_two.title] has recovered from her earlier orgasm and is standing to the side, watching."
            the_person_two "God I cum so easily. Next time grope [the_person_two.fname] the whole time [the_person_one.mc_title]!"
            the_person_one "Resorting to cheating? I bet I could even handle that! Next week?"
            "The girls agree to meet again next week."
            the_person_two "Mmm... I see some cum on you..."
            "[the_person_two.title] starts to move toward [the_person_one.possessive_title]. They embrace and start to make out."
            $ scene_manager.update_actor(the_person_one, position = "kissing", z_order = 1, display_transform = character_right)
            $ scene_manager.update_actor(the_person_two, position = "walking_away", display_transform = character_right_flipped, z_order = 2)
        "As the girls do their thing, you decide to head out. You say goodbye and slip out from the sex shop."

    $ scene_manager.clear_scene()
    return
