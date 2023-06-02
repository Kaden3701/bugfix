init -1 python:

    def candace_midnight_wakeup_requirement():
        return False

    def candace_begin_cure_research_requirement(person):
        return False

    def candace_anti_bimbo_serum_requirement():
        return False

    def candace_cure_bimbo_requirement():
        return False

    def candace_meet_doctor_candace_requirement():
        return False

init 2 python:
    candace_midnight_wakeup = Action("Candi Gets Arrested", candace_midnight_wakeup_requirement, "candace_midnight_wakeup_label")
    # candace_love_path_intro = Action("Candi Browses Tinder", candace_browsing_tinder_at_work_requirement, "candace_browsing_tinder_at_work_label")
    candace_begin_cure_research = Action("Cure for Candi", candace_begin_cure_research_requirement, "candace_begin_cure_research_label")
    candace_anti_bimbo_serum = Action("Bimbo Cure Progress", candace_anti_bimbo_serum_requirement, "candace_anti_bimbo_serum_label")
    candace_cure_bimbo = Action("Bimbo Cure Serum", candace_cure_bimbo_requirement, "candace_cure_bimbo_label")
    candace_meet_doctor_candace = Action("Meet Doctor Candace", candace_meet_doctor_candace_requirement, "candace_meet_doctor_candace_label")


#Candace's bimbo cure event series requires completion of her Love and Obedience series. Assume love of atleast 80 and obedience 180 for this line.
label candace_midnight_wakeup_label():
    python:
        candace_check_police_chief_met()
        # make sure she is in the police station wearing her uniform
        police_chief.change_location(police_station)
        police_chief.wear_uniform()

        the_person = candace

    "Your phone goes off in the middle of the night, waking you up. You look over at it."
    "You have no idea who it is, so you silence it and roll over. Seconds later, it's going off again. You groggily sit up and answer your phone."
    mc.name "Hello?"
    "?????" "Hi. Is this [mc.name]?"
    mc.name "Yes..."
    "?????" "This is [police_chief.title] with the police department. We have a [the_person.fname] [the_person.last_name] here who asked us to call you."
    "[candace.fname]? Who do you know named [candace.fname]?"
    mc.name "I'm sorry I'm not sure who that is..."
    police_chief "She also goes by Candi."
    "Oh shit! What is [the_person.fname] doing at the police department?"
    mc.name "Oh! Is she okay?"
    police_chief "She's fine. She got swept up last night in a prostitution sting. Apparently she was going around a strip club last night offering services..."
    $ mc.change_locked_clarity(10)
    police_chief "But it turns out she was doing it for free. We got multiple witnesses so we are gonna let her go."
    police_chief "We were just gonna send her off, but I didn't feel good about her walking home alone this time of night so I asked if she could call anyone and she gave me your name and number."
    "That sounds exactly like something [the_person.fname] would do."
    mc.name "Okay... I'll be there in 20 minutes."
    "You hang up the phone and take a minute. [the_person.fname], you REALLY need to be more careful. Who knows what kind of guy you could have wound up with? You wonder if it isn't time to do something more drastic with her."
    "You get up and quickly get yourself dressed. You leave a quick note on the counter in case anyone notices you are gone in the middle of the night and head out. It's a fairly short walk to the police station."
    #Change to police station
    $ police_station.show_background()
    "As you walk in, you walk up to the front desk. There's a good looking girl behind the desk. She smiles when she greets you."
    "?????" "Hello. Can I help you?"
    mc.name "Yeah. I'm here to pick up [candace.fname]."
    "?????" "Ahh. Sure thing. First though, the chief wants to talk to you in her office, privately..."
    mc.name "Okay..."
    "?????" "Her office is right down the hall there."
    "The kind officer points you the way to go. You head down the hall, take a breath and knock."
    police_chief "It's open."
    "You let yourself in."
    police_chief "Close the door, please."
    "You close the door behind you. Behind the desk is an official looking officer. She greets you with a scowl."
    $ police_chief.draw_person(position = "sitting", emotion = "angry")
    police_chief "So you must be here to pick up that crazy bitch, [candace.fname]."
    mc.name "Yeah, something like that..."
    police_chief "We need to chat. I got a call from my deputy a few hours ago at home, saying I needed to get here right away. They said they had arrested someone they didn't know what to do with."
    "Oh boy, this is going to be interesting..."
    police_chief "So I come in, and they got her in solitary lockup. I asked why, and apparently she was in a cell with a few other women and when a deputy walked by she would beg to suck his dick."
    police_chief "When he said no and walked away, he could hear her making passes at the other girls in the cell."
    police_chief "So I get here, bring her to my office and wouldn't you know it, it's the woman that was walking around topless at the mall the other day!"
    police_chief "I start asking her questions, you know. Where are you from, where's your family, that sort of thing."
    police_chief "She says she doesn't know, so I ask about friends and she says she just has a couple..."
    police_chief "We talk for a bit longer... And it's pretty clear from her conversation... This lady has no business being out in public. She is so far gone. Do you have any idea what is going on with her?"
    "You take a moment to consider how to answer this. You are going to need to proceed carefully."
    mc.name "Well, when I met [candace.fname], she was in a bad relationship. The guy she was with was taking advantage of her."
    mc.name "I did some work on her background, and although I'm not sure where, I think she may have been involved in some sort of pharmaceutical experiment that made her like that."
    mc.name "I helped her get out of the relationship and set her up with a job at my business, trying to help her get independent again."
    police_chief "Hmm. I see. That's unfortunate, but she doesn't seem to understand that she can't just wander around downtown hitting on everything with a pulse. She's gonna wind up getting kidnapped... Or worse."
    mc.name "I agree. To be honest, I didn't realize she had been doing that."
    "The chief ponders for a few moments."
    police_chief "Look... I can't force you to do this... But it is something you might consider. It's clear to me that [candace.fname] can't really take care of herself."
    police_chief "We can't find any records pertaining to family in the area either."
    police_chief "If you put in a motion with the local courts filing for her power of conservatorship on the grounds that she is unable to function independently, I'd be willing to sign that in support."
    police_chief "With that, you could have her sent somewhere better designed to take care of folks like her. It'd be for her own good."
    mc.name "That seems... extreme? Maybe she would be willing to move in with a friend or something?"
    police_chief "Yeah... Maybe... Look, you don't HAVE to do anything. But for her sake, you should consider doing SOMETHING."
    police_chief "Otherwise, if she winds up back in here, I won't be able to just let her go, I'll have to get her committed somewhere."
    mc.name "I understand ma'am."
    police_chief "Alright. Well, good luck. I'll call down to lockup and have them bring her up."
    $ clear_scene()
    "You excuse yourself from the police chief's office. As you are walking back to the entrance, you start thinking about what you could do for [the_person.fname]. Maybe she could move in with someone?"
    "She has been pretty close with [starbuck.fname] recently. Maybe she would be willing to have a roommate?"
    "Maybe you could even have her move in with you? It might be a little cramped, but you think if you explain things to Mom and [lily.fname] they would understand."
    "You think a little more. What about the bimboism itself? Maybe there is some way it could be reversed? You've made some incredible strides recently with the serums at your business, but you've never considered trying to undo their effects."
    "Is such a thing possible? Maybe you could talk to [mc.business.head_researcher.name] about it?"
    $ the_person.draw_person()
    "As you stand at the entrance, lost in thought, an officer brings [the_person.fname] out."
    if the_person.love > 20:
        the_person "Hey boss! Sorry to have them call you. They kept asking me who would come and get me and you were the only one I could think of!"
    elif the_person.love < 20:
        the_person "Oh, hey boss... I'm sorry to drag you out here in the middle of the night like this..."
    else:
        the_person "Hey [the_person.mc_title]. Sorry about this..."
    mc.name "It's okay. Let's just get you home. We can talk about this when we get there."
    "The officer says you are free to go, so you step out into the night with her."

    $ downtown.show_background()
    "As you walk towards her house, you sigh when she tries to lead you into a back alley."
    the_person "It's been a frustrating night... I just thought, like, maybe we could..."
    $ mc.change_locked_clarity(10)
    mc.name "Let's get back to your place first, okay?"
    the_person "Aww, okay."
    "It's pretty clear to you that if you don't do anything, [the_person.fname] is going to get herself into real trouble. Is this really something you want to get yourself involved in though?"
    "You get to her apartment, and soon she is walking through the front door... Which was completely unlocked..."
    #candi home background
    $ mc.change_location(the_person.home)
    the_person "Finally! Let's have some fun!"
    mc.name "Wait... We need to talk first."
    the_person "God damnit why does everyone just want to talk? Just like... Let's get naked and then like... Let our bodies do the talking?"
    $ mc.change_locked_clarity(15)
    mc.name "This is important."
    "It's time to make a decision. What are you going to do?"
    menu:
        "Move in with you \n{color=#ff0000}{size=18}Corruption path \n Not yet written{/size}{/color} (disabled) ":
            pass
        "Move in with \n{color=#ff0000}{size=18}FWB path \n Not yet written{/size}{/color} (disabled)":
            pass
        "Research a cure":
            call candace_love_path_intro_label from _set_candace_to_love_path
        "Do nothing \n{color=#ff0000}{size=18}Abandon path \n Not yet written{/size}{/color} (disabled)":
            pass

    python:
        clear_scene()
    return

label candace_love_path_intro_label():
    $ the_person = candace
    $ the_person.draw_person()
    "You've made up your mind. While the current [the_person.title] certainly has her charms, the drug she was given is ruining her life."
    "You care about her too much to let that happen. You have to do what you can to research it and see if you can reverse the effects."
    mc.name "[the_person.title]... Tomorrow we are going to talk to [mc.business.head_researcher.name]. I want to see if we can try and reverse the experiment that made you like this."
    the_person "Made me... Like this? I don't understand... Don't you like me?"
    mc.name "Of course I do. But the changes that it caused, you're a danger to yourself. How long have you been going out and wandering around, looking for a fuck?"
    the_person"I... err... I mean... Sometimes I just get the urge..."
    mc.name "And you can't control it?"
    the_person "I mean... Why should I? It's just for fun!"
    mc.name "I get that, but you can't just wander the streets. I got you out of your previous relationship because I care about you and couldn't stand to see you getting taken advantage of like that."
    mc.name "If you keep doing this, someone even worse is going to come along and who knows what will happen."
    $ the_person.draw_person(emotion = "sad")
    the_person "I... I..."
    "A small tear is coming down her eye."
    the_person "I don't want to be... Like... A burden..."
    "You step closer to her, pulling her into a hug."
    the_person "If that is what you think... I trust you boss."
    "You feel relieved. You could have gone through court to file to be her conservator, but it sounds like it won't come to that. You hold her close for a while. Soon, you feel a little movement."
    "[the_person.title]'s hand makes it way from your back to your front, as she begins stroking your crotch."
    the_person "Is it... Is it time now?"
    $ mc.change_locked_clarity(20)
    "She truly is insatiable."
    if mc.energy < 50:
        "You are exhausted from a long day, but you dig deep, knowing there's no way you could leave her without giving [the_person.title] a decent dicking."
        $ mc.change_energy(50)
    "[the_person.title] gives a little yelp as you pick her up."
    mc.name "Yes, it's time now."
    $ the_person.draw_person(position = "against_wall", emotion = "happy")
    the_person "Yay! I've been waiting for this all night!"
    $ mc.change_location(kitchen)
    "[the_person.title] wraps her legs around you, grinding against you, as you carry her over to her kitchen counter."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(15)
    if not the_person.vagina_available():
        "You pull off everything between you and her cunt."
        $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "missionary")
    "[the_person.title] reaches down and starts to play with herself as you start to get undressed. She starts to moan as you pull your cock out."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    the_person "Just put it in me, I'm ready for it... Whoa!"
    $ the_person.draw_person(position = "missionary")
    "You grab legs and push them up over her head. You waste no time, lining yourself up with her slit, you push yourself into her."
    the_person "Oh! Fucking... Finally!"
    "[the_person.title] grabs her own legs, holding them back for you as best she can. It's time to give her pounding she's been looking for!"
    call fuck_person(the_person, start_position = piledriver, start_object = make_counter(), private = True, skip_intro = True, skip_condom = True) from _call_candace_love_fuck_01
    "You look at the clock on [the_person.possessive_title]'s microwave. It's almost 2am. You are exhausted."
    mc.name "Hey... It's really late... Can I crash here tonight?"
    "[the_person.title]'s face gets disturbingly excited."
    the_person "Oh. My. God. A slumber party! Let's do it!"
    $ the_person.draw_person(position = "walking_away")
    "She starts to lead you into her bedroom."
    mc.name "[the_person.title] I just need to get some sleep..."
    the_person "Don't worry, you'll wake up and be all like, {i}'I've never slept better!'{/i}"
    "She modulates her voice lower when she imitates you. Oh god what are you getting yourself in to..."
    $ the_person.change_to_bedroom()
    "In her bedroom, you lay down on her bed, pulling blankets up over yourself. Her bed smells flowery."
    the_person "Okay, let me just get into some jammies..."
    $ the_person.draw_person(position = "walking_away")
    "You try to stay awake for her, but your eyes are getting so heavy."
    "You are starting to feel yourself drift off when you hear the bedroom door close as [the_person.title] comes back."
    python:
        the_outfit = Outfit("Candi's Pink Nightgown")
        the_outfit.add_upper(nightgown_dress.get_copy(), [1.0, .71, .75, .65])
        the_person.apply_outfit(the_outfit)
        the_outfit = None
    $ the_person.draw_person(position = "stand4")
    "She is wearing a sheer pink nightgown, and absolutely nothing else. Normally a sight like that would be enough to get your blood boiling, but right now you are just too tired."
    $ mc.change_locked_clarity(5)
    "Silently, [the_person.title] climbs into bed next to you. You turn on your side and cuddle up with her, spooning her from behind."
    $ the_person.draw_person(position = "walking_away")
    "Still naked, your cock is now up against [the_person.possessive_title]'s rear. She wiggles back and forth a couple times until it nestles in between her cheeks."
    "She grabs your hand and brings it around her front, placing it on her chest. She sighs, then turns her head."
    the_person "Goodnight boss. Thanks for spending the night... I've... Like... always wanted to try sleeping like this..."
    mc.name "Goodnight..."
    the_person "Hopefully in the morning my nightgown will be covered in cum..."
    "You know you should probably be alarmed by that statement... But you are too tired to care at this point."
    $ mc.change_locked_clarity(5)
    mc.name "Yeah... Me too..."
    "You drift off to sleep."
    "You are exhausted, but begin to dream sexy dreams about [the_person.title], the bomb shell bimbo you are cuddled up with. At one point, you are dreaming that she has climbed on top of you and is riding your cock aggressively."
    "However, the feelings are so intense, you aren't sure... Could this be real?"
    $ the_person.draw_person(position = "cowgirl")
    the_person "That's it boss... It's okay I'm like, just letting you work that boner off..."
    $ mc.change_locked_clarity(50)
    "You reach up and grab her tits. This definitely feels real. And you are really close to finishing."
    mc.name "I'm... I'm!"
    "You try to warn her. She quickly pops off and starts to jack you off. You cum, blowing your load all over her nightgown covered belly."
    $ the_person.cum_on_stomach()
    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
    $ the_person.draw_person(position = "cowgirl") # paint cum
    "When you finish, [the_person.title] starts to lick her fingers. She seems happy as she lays back in bed next to you. Sleep rapidly overtakes you."
    $ mc.change_locked_clarity(20)
    "You sleep for a while longer. You aren't surprised though when you feel warm, wet sensations enveloping your cock again."
    "The delicious suction and the sound of [the_person.possessive_title]'s lips smacking give you all the information you need. [the_person.title] is sucking you off."
    $ the_person.draw_person(position = "blowjob")
    "You crack your eyes open and see Candi, working diligently to get you off with her mouth. You aren't sure how long she has been doing this, but it's definitely working."
    $ mc.change_locked_clarity(50)
    if the_person.is_bald():
        "You reach down and run your hand over her scalp. She looks up at you an makes eye contact... And then maintains it as she starts to give you long, slow strokes with her mouth."
    else:
        "You reach down and run your hand through her [the_person.hair_description], helping keep it out of her way. She looks up at you an makes eye contact... And then maintains it as she starts to give you long, slow strokes with her mouth."
    mc.name "God... I thought I was empty last time... Get ready here it cums again!"
    $ mc.change_locked_clarity(50)
    "She takes you out of her mouth and strokes you with her hands. She points you down at her chest as you begin to fire off your load."
    $ the_person.cum_on_tits()
    $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_person)
    $ the_person.draw_person(position = "blowjob")
    "She keeps eye contact and doesn't say a word as you drop your load all over her chest. It immediately starts soaking into her nightgown. You can see the stains from earlier still on her belly."
    "You aren't sure what happens after that, because you pass out again. Your last thought as you fall back asleep, is that [the_person.title] must think a slumber party means getting as much cum as possible on her nightgown."
    $ the_person.next_day_outfit = the_person.outfit # stay in current outfit next day
    call advance_time_move_to_next_day() from _call_advance_time_move_to_next_day_candace_love_path_intro # move time forward without morning events
    "You open your eyes. Sunlight? Next to you, the bed is empty. Crap, what time is it? You get up and reach for your phone."
    "The battery is dead. Is that coffee you smell? [the_person.title] must hear you stirring, she soon appears in the door to her bedroom."
    $ the_person.draw_person(position = "stand4")
    "She is still wearing the same nightgown. Evidence of your long, sex filled night apparent."
    $ mc.change_locked_clarity(20)
    the_person "Good morning sleepyhead!"
    mc.name "Hey... Is that coffee?"
    the_person "Yup! I have some eggs and toast ready too!"
    mc.name "Wow, you didn't have to do that."
    "She looks at you, a bit puzzled."
    the_person "I don't? My last boyfriend always told me to, like, always have breakfast ready whenever he gets up!"
    "That's right, her last boyfriend was a controlling asshole. You forget that sometimes."
    "You shake your head."
    mc.name "That sounds great, but you don't HAVE to do that. I appreciate it though!"
    "You start to get up. As you push the blankets down, you remember that you are completely naked."
    mc.name "Are my clothes still out there?"
    the_person "Oh... Well... Maybe I shouldn't have done this but... Like... I threw your stuff in the washer..."
    "You grimace. You doubt she has anything extra you can wear."
    the_person "It's okay though! They'll be clean before it's time to go to work."
    mc.name "Ah, okay. What time is it?"
    the_person "It's about 7."
    "That should work out okay. Eat some breakfast, and you can head in to work with [the_person.title] and go straight to [mc.business.head_researcher.title]."
    "A timer goes off in the other room."
    the_person "Oh! I gotta get back to the kitchen!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and leaves the room. As she turns, you notice her nightgown has cum stains on the ass too... When did that happen? Did she make you cum while you were completely asleep too?"
    $ mc.change_locked_clarity(30)
    "You slowly get up, your feet a little unsteady. You work your way out of the bedroom."
    $ kitchen.show_background()
    "In the kitchen, there is a small table with two chairs. You walk over and sit down at one."
    $ the_person.draw_person(position = "back_peek")
    the_person "It's almost ready. Sorry I, like, only know how to make scrambled eggs..."
    mc.name "It's quite alright. Listen... I just want to make sure you know this... You didn't have to make me cum so much last night either..."
    the_person "Oh, I know. I just... Wanted to. I haven't had someone stay over since... Well, as far as I can remember anyway! I thought that like, if you had a good time, maybe you'd stay over again sometime..."
    "She turns and sets down two plates of eggs and toast, then turns back and starts pouring a couple cups of coffee."
    mc.name "Your old boyfriend, he never stayed over here?"
    "She turns around with two cups, then sits down across from you."
    $ the_person.draw_person(position = "sitting")
    the_person "No, he used to make me come to his place, he never really came here... He didn't let me umm... Do stuff... In the night either. Said he needed his sleep."
    mc.name "I umm... It might be good to ask next time... I didn't mind it, but I'm definitely pretty tired today."
    the_person "I'm sorry! I just... I could feel it, you know, get hard? And I couldn't help myself!"
    mc.name "It's okay, really. I could have said no, and it... Well it's pretty amazing, to wake up to a woman like you pleasuring me."
    the_person "Yay! That's why you should stay over again!"
    $ mc.change_locked_clarity(50)
    "You take a bite of the eggs. It's actually pretty good. The coffee is hot and helps wake you up."
    mc.name "Listen... Today we are going to go talk with [mc.business.head_researcher.title]. I promise we'll definitely do this again sometime, but for now, I want you to work with her, okay? I want to find out if we can reverse the effects of the lab experiment."
    "She picks at her breakfast."
    the_person "There are times... You know? Like where I feel like I almost... Remember. Like, I remember being so excited. Like I was on the verge of something! But there was a deadline... Our funding was gonna get cut..."
    $ the_person.draw_person(position = "sitting", emotion = "angry")
    "She furrows her brow."
    the_person "I just... Ugh! I can't remember! I can't remember anything..."
    mc.name "It's okay. Thank you for breakfast. It's very good."
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    the_person "Like, totally!"
    "It's amazing how quickly her personality changes back to her normal, bubbly self."
    "You finish your breakfast and sit sipping your coffee. Candi finishes up as well. She stands up and grabs your plates."
    $ the_person.draw_person(position = "stand2")
    "She takes them over to the her sink and begins to wash them. As you watch, she bends over, scrubbing them clean..."
    $ the_person.draw_person(position = "standing_doggy")
    "God, her ass is great. Even after cumming over and over last night, you feel blood flowing to your dick as you watch her bent over."
    $ mc.change_locked_clarity(30)
    "Still completely naked, you know there is no way you can hide it from her. Maybe you should take charge, and give her a good fuck before you both head in to work."

    "You get up from the table and start to walk over to [the_person.possessive_title]. She doesn't seem to react... Surely she heard you get up?"
    "Then you notice. She is starting to wiggle her ass back and forth. God she really is a sex hungry minx."
    $ mc.change_locked_clarity(50)
    "You grip her hips with your hands, and then push your fully erect cock against her ass."
    the_person "Oh, thank God, I was, like, REALLY hoping to get one more before work..."
    # pull up nightgown
    $ the_person.draw_animated_removal(the_person.outfit.get_lower_top_layer, position = "standing_doggy", half_off_instead = True)

    "You slowly lift up her nightgown, exposing her rear. You position the head of your cock against her entrance and then start to rub it up and down her slit. When you pull back for a second, your tip is slick with her arousal."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    the_person "Stop teasing... I'm ready. I'm always ready!"
    mc.name "I know, but someone has to teach you patience."
    the_person "I'm patient! I can totally be patient, I'm the most... Ohhh!!!"
    "You cut her off mid sentence as you thrust yourself all the way into her. You don't give her time to recover, as you start to roughly fuck her."
    call fuck_person(the_person, start_position = standing_doggy, private = True, skip_intro = True, skip_condom = True) from _call_candace_love_fuck_02

    # You decide to just wait and see what happens. You continue to enjoy the view of Candi's ass as she scrubs your plates clean, then sets them on a drying rack. She turns around and immediately notices your erection.
    # "Oh, thank God, I was, like, REALLY hoping to get one more in before work..."
    # She starts to walk over to you. You give her a simple ultimatum.
    # "We can do it one more time... But this time I finish inside you. Your choice of what hole."
    # She gives you a smile. "Mmm... Decisions... Decisions..."
    "As you are both recovering, you hear a buzzer go off."
    the_person "Oh! The dryer is done! I guess it's about time to head into the office..."
    "[the_person.title] disappears for a moment then comes back, holding your clothes."
    $ the_person.draw_person(position = "stand4")
    "You spend a few minutes getting dressed and freshening up a bit in the restroom. When you emerge, you see [the_person.possessive_title] also getting ready for the day."
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    mc.name "I'm going to head in a little early. I'll page you down to my office when I've had a chance to talk to [mc.business.head_researcher.title]."
    the_person "Okay! See you later!"
    "You step out of [the_person.title]'s apartment. You should make it a priority to talk to your head researcher."
    $ mc.business.head_researcher.add_unique_on_talk_event(candace_begin_cure_research)
    if not perk_system.has_ability_perk("Lustful Youth"):
        "You feel like making [the_person.possessive_title] cum over and over has woken something inside you."
        "You feel like no matter what happens or how your day is going, you will always have the energy to make the ones you love cum."
        $ lustful_youth_perk_unlock()
        "You have gained the perk 'Lustful Youth'!"
    return

label candace_begin_cure_research_label(the_person):
    $ scene_manager = Scene()
    mc.name "I need to talk to you about something. Can come with me to my office?"
    "Your head researcher looks up from her work and nods."
    the_person "Sure, I'll be right there."
    "She follows you to your office. You close the door in the way in, and you both have a seat."
    $ ceo_office.show_background()
    $ scene_manager.add_actor(the_person, position = "sitting")
    mc.name "I need to talk to you about [candace.fname]. Before she came here, she worked at another pharmaceutical company similar to this one."
    #[If you have already researched the bimbo serum]
    if mc.business.is_trait_researched(permanent_bimbo):
        mc.name "I think she may have been involved in a trial in something similar to our bimbo serum."
    else:
        mc.name "I think she may have been involved in some sort of trial on a drug that affected her mental capacities."
    the_person "I actually thought something similar. I didn't know that she came from a competitor, but her personality exhibits all of the traits that we've seen from the serum, both physical and mental."
    mc.name "Unfortunately, it has inhibited her ability to function independently. Do you think there is any way of reversing the serum effects? Or even just partially?"
    the_person "Wow... That's a difficult question. Up until now, just about all of our work has been on making the serums MORE effective, not nullifying them."
    mc.name "I understand that this is a difficult question... But unfortunately [candace.fname] is no longer able to manage. I can't sit idly by and watch her life get ruined, if there is something we can do to help her."
    "Your head researcher ponders the issue for a bit."
    the_person "Can you give me some time to study her? With a few tests... Maybe I could figure something out."
    mc.name "That is fine. I actually need to find her a place to stay for a bit..."
    "You explain to [the_person.fname] what happened with [candace.fname] getting arrested and your conversation with the police chief."
    if the_person == stephanie:
        the_person "Wow... Tell you what. Why don't you have her move in with me for a bit? I can work on it on the side, and between me and [ashley.fname] we should be able to keep an eye on her..."
    else:
        the_person "Wow. Well, I live alone, why don't you have her move in with me for a bit? I could put her in my guest room."
    mc.name "[the_person.fname], you're amazing. Let me call her in and we'll talk to her."
    "You call [candace.fname] and ask her to come to your office. In a minute there's a knock on your door."
    mc.name "Come in."
    $ scene_manager.add_actor(candace, display_transform = character_left_flipped)
    candace "You need something?"
    mc.name "Have a seat."
    "[candace.fname] walks in and sits down next to [the_person.fname]."
    $ scene_manager.update_actor(candace, display_transform = character_center_flipped, position = "sitting")
    mc.name "Remember how we talked about having [the_person.fname] examining you and doing some research?"
    "She looks at you with a puzzled look."
    candace "I... I remember we had a slumber party..."
    "You can tell that she is struggling to remember."
    mc.name "You got arrested, remember?"
    candace "Right! And I told the nice police officer I was hiding drugs 'somewhere special' and so he had to do a strip search and..."
    $ mc.change_locked_clarity(10)
    mc.name "[candace.fname], we said we would talk with [the_person.fname] about helping you control some of your... urges... Among other things."
    candace "If you say so boss!"
    mc.name "Okay. Well, in order to keep things from impacting the business too much, [the_person.fname] would like you to stay with her for a while. It will make it easier for her to run tests on you as necessary."
    candace "You mean... You want me to move in? With [the_person.fname]?"
    mc.name "Don't worry, it would only be temporary. A couple weeks at most."
    mc.name "Think of it, like a slumber party."
    candace "Oh! A slumber party! That will be like, so much fun!"
    "[the_person.fname] gives you a wink, seeing that [candace.fname] is going along with the plan."
    the_person "I'll come over after work today and help you pack a few things."
    mc.name "Good. Let me know if either of you need anything."
    "With that, you dismiss the meeting. Hopefully [the_person.fname] will be able to find some way to reverse the effects of the serum that made [candace.fname] this way."
    $ candace.event_triggers_dict["living_with_stephanie"] = day
    $ candace.set_schedule(the_location = the_person.home, the_times = [0,4])
    $ mc.business.add_mandatory_crisis(candace_anti_bimbo_serum)
    $ scene_manager.clear_scene()
    $ mc.location.show_background()
    $ jump_game_loop() # jump out of dialog and return to office
    return

label candace_anti_bimbo_serum_label():
    $ the_person = mc.business.head_researcher
    $ mc.start_text_convo(the_person)
    the_person "Hey! Meet me in your office ASAP!"
    mc.name "On my way!"
    $ mc.end_text_convo()
    $ the_person.draw_person(position = "sitting")
    $ ceo_office.show_background()
    "You quickly head to your office and find [the_person.possessive_title] sitting behind your desk with her feet up."
    the_person "Guess what? I'm a fucking genius."
    mc.name "Oh? Do you have something to report from your research with Candi?"
    the_person "Something like that. You see, at first, I was racking my brain, trying to come up with some crazy chemical compound that could go back and undo a complex drug with multiple binding points and effects."
    the_person "But then I realized, I was doing it all wrong."
    mc.name "Oh?"
    the_person "Yeah! You don't need to UN-do all the previous serums effects, I just needed to create new compounds that counter the undesirable side effects."
    the_person "Specifically for [candace.fname], the effect that makes her a total dumbass, the loss of her intelligence."
    mc.name "And you were successful in creating something to do that?"
    the_person "Well... Kind of. I have a pretty good idea of how to do that, but I'm going to need help researching it. I added my idea to the serum trait database."
    if not mc.business.is_trait_researched(permanent_bimbo):
        the_person "Also, we really should research the bimbo serum that we have the preliminary results for first. It would give us a better understanding before we attempt this path."
    the_person "If you want us to look into it more, the research team will get to work on it. It is something that could be very useful, in general."
    the_person "If someone were to accidentally ingest the bimbo serum or something, this could at least counteract the effect on their mental state and personality."
    mc.name "That sounds very useful. Let me think about it and I'll swing by research later if I decide to have the research department focus on it."
    if the_person.sluttiness > 60:
        the_person "Okay... In the mean time, [candace.fname] can feel free to keep staying with me. We've, umm, had a lot of fun, living together the last few weeks!"
        "You remember the night you spent with her. You are certain they've been having lots of fun together."
        $ mc.change_locked_clarity(5)
        mc.name "Sounds good, I appreciate it."
        $ town_relationships.update_relationship(the_person, candace, "Best Friend")
    else:
        the_person "Okay... Well, don't delay it, okay? Living with her has been... Stressful."
        the_person "She keeps 'accidentally' walking in on me when I'm showering and sometimes when I wake up in the morning she's in my bed next to me!"
        mc.name "It won't be too much longer. I appreciate it."
        the_person "Okay... She's driving me crazy, okay!"
        $ town_relationships.update_relationship(the_person, candace, "Rival")
    "[the_person.title] leaves your office."
    $ clear_scene()
    if mc.business.is_trait_researched(permanent_bimbo):
        "You now have a new serum trait available to research."
    else:
        "As soon as you research permanent bimbofication, you will have a new serum trait available for research."
    "It has the powerful effect of reversing the bimbo serum's personality change and intelligence penalty!"

    $ unlock_anti_bimbo_serum()
    $ mc.business.add_mandatory_crisis(candace_cure_bimbo)
    return

label candace_cure_bimbo_label():
    $ scene_manager = Scene()
    $ the_person = mc.business.head_researcher
    "You have now finished researching the anti bimbo serum trait. You text your lead researcher."
    mc.name "Hey, can you make me a single dose anti bimbo serum for [candace.fname]?"
    the_person "Already done. I figured you would want that."
    mc.name "Thanks, bring it to my office. I'll have her meet us there."
    $ ceo_office.show_background()
    "You walk to your office and sit down. You call [candace.fname] and have her come. You admit that you are very nervous about what is about to happen."
    "Will [candace.fname] suddenly remember everything that's happened?"
    "Will she hold you responsible for all the times you fucked her in her current state?"
    "There are so many possibilities, it's impossible to know what is about to happen."
    $ scene_manager.add_actor(the_person)
    $ scene_manager.add_actor(candace, display_transform = character_center_flipped)
    "Both girls walk into your office at about the same time."
    candace "Yeah boss?"
    mc.name "Why don't you both sit down."
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ scene_manager.update_actor(candace, position = "sitting")
    mc.name "I have some good news [candace.fname]. [the_person.fname] has designed a serum to help you get back to your old self. It won't be a complete reversal, but it should help a lot with some of the issues you've been having with your memory and impulse control."
    candace "Okay boss. If that's what you want, I'd be happy to try it."
    mc.name "Thank you for trusting me. It means a lot. [the_person.fname]?"
    the_person "Okay... Do you mind if I take notes? This will be our first human trial..."
    candace "Sure."
    "[the_person.fname] hands [candace.fname] the vial."
    the_person "Here you go. I made it a little salty, the way you said you like it. I couldn't recreate the other properties you asked for reliably..."
    candace "Oh! Well thanks for trying."
    "Without further ado, she pops the cap and downs it. She hands the vial back to [the_person.title] and you wait."
    "[candace.fname] closes her eyes and begins to breath deeply. So far she doesn't seem to be having any major negative reactions, but you are starting to get concerned."
    "It's only been a minute or two, but it feels like an eternity. Finally she opens her eyes and looks at you."
    "Her pupils narrow and you can see her focus on you with a startling level of concentration."
    $ candace.personality = genius_personality
    $ candace.event_triggers_dict["cure_day"] = day
    $ candace.int = 9       #Scary smart
    candace "[candace.mc_title]... This is incredible!"
    mc.name "Candi, are you okay?"
    candace "Candi? Yes that's what I went by... But you can call me [candace.fname]."
    $ candace.set_title("Candace")
    "You feel a sense of relief, but also a bit of fear. Is this the same person still? Or is she someone completely different now?"
    mc.name "How are you feeling [candace.title]? Do you know where you are? What has been happening recently?"
    "She turns to [the_person.fname]."
    candace "Yes. Yes I remember... Everything."
    the_person "Anything you can tell us? About what originally happened to you? Or how you got here?"
    $ scene_manager.update_actor(candace, emotion = "sad")
    "Her brow furrows as she starts to recall."
    candace "I was the lead researcher, at another company, and we had just received word that our government funding was going to get cut if we couldn't get results."
    "She clears her throat and continues."
    candace "I was desperate, but also overconfident. I wanted to rush human trials, but my boss said no. So I decided to take it myself."
    the_person "What were you trying to make?"
    candace "It seems so silly now. It was a drug designed for espionage. To reduce someone to their basest desires and to be completely open to suggestion and to be truthful."
    candace "The implications of the drug in the hands of the intelligence agency were immense."
    candace "But it was supposed to be temporary. In animal testing, the drug worked its way out of the body within 24 hours."
    candace "Something went wrong with mine... The effects... Appear to have been permanent?"
    $ scene_manager.update_actor(candace, emotion = "angry")
    "She shakes her head. Her fists clench as she remembers the next events."
    $ renpy.say(candace.char, "The lab shut down... I had nowhere to work, no money... And my libido had skyrocketed... I didn't know what to do. Then I met " + ophelia_get_ex_name() + "...")
    candace "I was out in front of this strip club... Trying to find someone to take me home that night, when I ran into him. He could tell I was in a bad spot... And totally took advantage of it."
    candace "Soon I was his 'personal secretary', but he wasn't even paying me anything. I was doing all sorts of errands for him, trading sexual favors for discounts, among other things."
    $ scene_manager.update_actor(candace, emotion = "happy")
    "[candace.title] turns to you, her expression softening."
    candace "But then, I met you... At that restaurant. You convinced me to quit, and to leave that controlling asshole... And gave me a job..."
    mc.name "I'm glad I was able to help..."
    candace "You did more than just help. You brought stability back to my life, gave me hope... You even bailed me out of jail! I owe you a great debt Mr. [mc.last_name]."
    $ candace.set_mc_title(mc.name)
    mc.name "Please, just [candace.mc_title]. I'm sorry about the times I also took advantage of your mental state."
    candace "What? I don't remember you doing anything like that."
    mc.name "We've been intimate. A lot actually."
    candace "Yes. And I'd like for that to continue. You weren't taking advantage, you were giving me exactly what I wanted."
    $ mc.change_locked_clarity(10)
    "She says that now... but a lot has happened to her. You still feel a bit uneasy about how much you fucked her while she was in her previous mental state."
    mc.name "I see. What about your work? Would you like to move over to the research department? We are doing amazing things here."
    candace "No, no. Not right now anyway. I need some time away from all that. I think for now I'd like to continue where I am now. It is actually quite enjoyable."
    candace "Actually, I think I know of a few suppliers I might be able to secure better contracts with, if I use a little persuasion anyway."
    mc.name "You don't need to keep using your body to secure discounts from suppliers if you don't want to."
    "She looks at you a bit puzzled."
    candace "Why wouldn't I want to? [candace.mc_title], a woman's body is an incredible tool to wield as they choose. If I want to be the best I can be, why would I deny myself the use of that tool?"
    "[candace.title] gives you a wink."
    candace "Plus, it's really really fun to be a tease."
    $ mc.change_locked_clarity(10)
    "Oh god, what have you done? You realize any man who tries to negotiate unfavorable contract terms with this woman is absolutely fucked."
    "It is clear that even though she has her intelligence back, [candace.title] still has her previous opinions and her sexuality."
    "You look over and see [the_person.title] scribbling down notes at an incredible pace."
    the_person "Wow... This is just absolutely amazing. Candi... Err... [candace.title]... Tonight after work, I suppose I'll help you pack up so you can move back to your place then?"
    candace "Yes I would like that. You've been very nice, letting me stay with you, but I think I would like my personal space back."
    candace "Really, the work that has been done to help me... I don't think I will ever be able to repay you."
    the_person "Well, when [the_person.mc_title] came to me and asked me to do it... I knew I couldn't say no. I'm so relieved that it has all worked out."
    candace "Ah, so you were the architect of the whole thing [candace.mc_title]? I suppose I shouldn't be surprised."
    mc.name "Well... That night at the police station. The chief talked to me before I bailed you out. She wanted me to apply to be your conservator."
    mc.name "I knew I needed to do everything I could to get the effects reversed..."
    candace "Wow... I didn't realize things had gone that far. I'm going to have to think about that for a bit."
    candace "Now, unless there's more to discuss, I think I have some new supply contracts to negotiate."
    $ scene_manager.update_actor(the_person, position = "walking_away")
    $ scene_manager.update_actor(candace, position = "walking_away")
    "The girls turn and leave you in your office. The progress made with [candace.title] has been incredible, for sure."
    $ scene_manager.clear_scene()
    "It feels like a happy ending for her, but at the same time you feel certain that this is really just the beginning of the story of you and your genius office girl."
    $ candace.event_triggers_dict["sex_record_snapshot"] = candace.sex_record.copy() #This should take a snapshot of our sex record with candace so we can compare it later
    $ candace.set_schedule(the_location = candace.home, the_times = [0,4])
    $ mc.business.add_mandatory_crisis(candace_meet_doctor_candace)
    return

label candace_meet_doctor_candace_label():
    python:
        the_person = candace

    "It's been about a week since you cured [the_person.title] of her bimboism..."
    "Well, mostly anyway. Since that time, talking with her is like talking to an entirely different person... But also the same."
    if the_person.is_bald():
        "She still smells the same, she still has the same naughty look in her eyes, she still smiles at you the same way."
    else:
        "She still smells the same, she still twirls her hair around her finger the same way, she still smiles at you the same way."
    "Yet, every time she opens her mouth and speaks, she is completely different."
    "A few days ago you walked by the break room while a trivia show was on, and [the_person.title] was spitting answers out before the host even finished with the question."
    "When she looks you in the eye and speaks, her words carry weight. You don't blow off her suggestions as if they are nonsense anymore."
    if candace_get_sex_record_difference_tier() == 0:
        "The changes have made you wary, especially of having sex with her. She still seems willing, but it just feels wrong."
        "You can't bring yourself to lay your hands on her. And in a business like yours that could be a problem in the long term. You decide to address it."
    elif candace_get_sex_record_difference_tier() == 1:
        "The changes have made you wary about how you relate with her, especially sexually. You've gotten touchy feely with her... But so far you haven't gone further."
        "The tension is starting to get to you. You decide to address it."
    elif candace_get_sex_record_difference_tier() == 2:
        "You've tested the waters with her since then. She seems to be just as receptive to your sexual advances as before."
        "Something about her resurgent intelligence has you wary though. You decide to talk to her about it."
    elif candace_get_sex_record_difference_tier() >= 3:
        "Since the change, somehow she has gotten even sexier. Whenever an opportunity arises, you can't seem to keep your hands off of her. And she seems to enjoy it too."
        if candace_get_sex_record_difference_tier() >= 4:
            "Even now, you can't help but day dream a bit about dumping your seed inside her yet again."
            "Something about her resurgent intelligence leaves you wary though. You decide to talk to her about it."
    $ mc.change_location(ceo_office)
    "You head to your office. You sit down at your desk and call down to [the_person.title] and ask her to come to your office. Soon she is at your door, stepping inside."
    $ the_person.draw_person()
    the_person "Good day [the_person.mc_title]."
    mc.name "Thank you for coming, [the_person.title]. Would you please close the door?"
    the_person "Certainly."
    "[the_person.title] closes the door and walks over to your desk, taking a seat."
    $ the_person.draw_person(position = "sitting")
    mc.name "I'm sorry for interrupting your day, but I wanted to talk to you about something."
    the_person "Ah yes, I calculated you would want to have this talk today."
    mc.name "Right. So obviously it would be good if we can get some things... Out in the open."
    the_person "Certainly sir. Do you mind if I go first?"
    "Oh boy. You aren't sure you are ready for this, but you are hopeful this will be a positive conversation."
    mc.name "Honestly, I'm not sure how to put this in to words. If you know how, by all means."
    the_person "Yes sir. So I've spent a lot of the last week, recounting the events I went through in the last few months, replaying them in my head, considering the outcomes and variables."
    the_person "The outcome that occurred... Where my intelligence was restored... The odds of something like that happening are less than .01 percent."
    mc.name "I mean, I'm sure it is rare that you chance upon a guy in the same industry..."
    the_person "Yes, that is certainly rare, sir. But it goes beyond that."
    the_person "To find someone that would take the time that you did, to recognize that I was in an abusive relationship, to do what it took to get me out, to get me a job, to help me make friends."
    the_person "When that same person COULD have taken a different route... Taken advantage, taken control."
    mc.name "I... I could never have done something like that..."
    the_person "I know. For you to have the morals to do that."
    the_person "But beyond that, to be in this industry, to be in a position to actually help, and to make the pushes necessary to formulate the cure, and to give it to me."
    "[the_person.title] looks you right in the eye and delivers her judgement."
    the_person "It could have only been you. You saved me. And for that, I owe you everything."
    $ the_person.change_love(100, 100)
    mc.name "Don't be ridiculous, you don't owe me anything..."
    the_person "I know you feel that way. But it goes beyond that too. You have your flaws, sure. Every man has a vice. But you mean everything to me."
    if the_person.is_girlfriend():
        the_person "I know I've changed a lot, and you may not love me anymore, but I love you. I'm completely yours if you still want me."
    else:
        the_person "I know I've changed a lot, and I'm willing to be patient if you want me to. But I love you. I'm completely yours if you want me."
    "Wow, you hadn't anticipated this."
    mc.name "You mean... You aren't angry? For the times I was weak... Even though I should have known better... and took advantage of you?"
    "[the_person.title] begins to laugh."
    the_person "Took advantage... Of me? I... Did not estimate that you might be fearing reprisal. You really are too good to be true, aren't you?"
    "[the_person.title] stands up. You worry she is about turn and leave... But instead... She starts getting naked?"
    $ the_person.outfit.remove_random_upper()
    $ the_person.outfit.remove_random_lower()
    $ the_person.draw_person(position = "stand2")
    mc.name "That's... You don't have to do that..."
    $ mc.change_locked_clarity(20)
    the_person "I know. But I want to. Sir, I threw myself at you so many times, you never took advantage of me. Your restraint in everything has been incredible."
    the_person "No straight man could have resisted being exposed to the amount of sex appeal I was displaying without succumbing."
    "She continues to disrobe. You are mesmerized by the beautiful woman in front of you."
    $ the_person.outfit.remove_random_upper()
    $ the_person.outfit.remove_random_lower()
    $ the_person.draw_person(position = "stand2")
    the_person "Besides, even if my brains were scrambled, I still wanted it. And I enjoyed it. A LOT. But I know some part of you still doesn't believe me."
    $ mc.change_locked_clarity(50)
    the_person "So now, I'm going to show you. Actions speak louder than words."
    "She motions to you."
    the_person "Would you please get naked for me? I want to show you how much I loved it, and how much I STILL love your cock."
    the_person "I want you to just sit back, let me get on top of you, and fuck you."
    the_person "I want to have intercourse, and then I want to feel you orgasm, and deposit your semen inside me."
    "Wow... A scientific way of putting it, but also very effective. You pull your cock out while [the_person.title] finishes stripping."
    $ the_person.strip_outfit()
    "Her eyes are on you as she walks around the desk. You glance at your unlocked office door..."
    the_person "Don't worry, we won't get interrupted during this..."
    mc.name "Have you been monitoring my office traffic?"
    the_person "No. But I did put up your out to lunch sign and locked the door on my way in without you noticing..."
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "cowgirl")
    "[the_person.title] gets up on top of you. Her eyes are making direct contact with yours as she takes your cock in one hand and starts to run you up and down her slit."
    "Her natural lubrication soon has you wet and ready for penetration."
    "She leans forward and closes her eyes. Your lips make contact and you begin to kiss. At the same time, she lifts her hips slightly, lines you up with her cunt, and slowly sinks down onto you."
    $ mc.change_locked_clarity(50)
    "Her tongue dances with yours as the first fledgling thrusts are made of her hips onto yours. Her kisses punctuated with moans."
    the_person "Mmm... You feel so good. I swear, every time we fuck is better than the last..."
    $ the_person.change_arousal(30)
    call get_fucked(the_person, the_goal = "vaginal creampie", start_position = cowgirl, private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_meet_dr_candace_fuck_01
    "When you finish, she just stays on top of you for a bit. You can feel your seed dribble out of her for a bit, but she doesn't seem to care about the mess. She just holds on to you."
    the_person "Thank you. I needed that."
    mc.name "Yes. I admit I was being apprehensive, but that certainly, ermmm, eased my mind."
    the_person "It certainly is a very relaxing activity. When I was working on my thesis, I was calling up the poor guy I was seeing at the time all the time trying to de-stress."
    mc.name "Thesis? You mean... You have a doctorate?"
    the_person "Yes."
    mc.name "So... I should be calling you Doctor [the_person.last_name]?"
    the_person "Ahh, let me just stop you right there. I would prefer things between us, and the girls here at the office, to remain more... Informal."
    "She sits back a bit and smiles."
    the_person "I'd prefer other titles. [candace.fname] is good, but what would be even better would be if you just called me... Your girlfriend..."
    mc.name "I might take issue with you getting busy with your landlord if we're gonna do this."
    "She chuckles before responding."
    the_person "You goof. With a cock as good as yours, I won't need anything else..."
    "After a moment she adds on to that."
    the_person "I would like to keep helping [starbuck.fname] at the shop though... She's become a good friend."
    if the_person.is_girlfriend():
        "Well, it seems that [the_person.title] still has feelings for you and wants to continue being your girlfriend."
    else:
        "Well, in quite the reversal of roles, [candace.fname] has asked you out officially. Do you want to accept?"
        menu:
            "Accept":
                if not the_person.is_girlfriend():
                    $ the_person.add_role(girlfriend_role)
                mc.name "So, what is your degree in, anyway?"
                the_person "I received my doctorate for molecular biology and genetics... Though I'm not sure why that is relevant."
                mc.name "Oh, I just wanted to know for when I have to introduce you to people as \"my girlfriend, Dr. [the_person.last_name]\"."
                $ the_person.change_stats(happiness = 15, love = 5)
                the_person "Ahh! I suppose that would be okay... The first part anyway."
                "She leans back a bit and gets kinda dreamy eyed."
                the_person "You know, I truly had no idea if you were going to accept or not."
                mc.name "Yeah. I was on the fence myself, but then you rode me cowgirl while I was in my office chair."
                mc.name "I realized if we were dating I could call you in here anytime during the work day and do it again..."
                the_person "... You know I would do that even if we weren't dating, right?"
                "You give her a wink. You decide to get busy one more time before you move on for the day..."
                mc.name "Yeah but now I don't have to use the company punishment manual to do this either."
                $ mc.change_locked_clarity(20)
                "She gives a little yelp as you suddenly scoot your chair from your desk. You stand up, picking her up as you go, then turn her over and bend her over you desk."
                $ the_person.draw_person(position = "standing_doggy")
                mc.name "You've been one naughty doctor."
                the_person "Oh lord I like where this is going."
                mc.name "Getting yourself arrested? The cops thought you were a prostitute!"
                "With your harsh, but playful words you bring your hand down and smack her ass. It wobbles enticingly."
                $ the_person.change_arousal(10)
                $ mc.change_locked_clarity(20)
                the_person "Oh! I'm sorry boss!"
                mc.name "Going out and looking for some stranger to meet your needs... When I was here all along!"
                "You give her ass another spank."
                $ the_person.change_arousal(15)
                $ mc.change_locked_clarity(20)
                the_person "Ahh! I'm sorry, I won't do it again!"
                "A red handprint starts to appear on her rear, where you spanked her. You lighten you touch a bit and gently rub her ass, soothing it."
                mc.name "I know. Because you don't need to anymore. When you get those cravings, and it's just too much to bear, come and find me. I'll meet your needs, anytime, anywhere."
                the_person "Oh... That's amazing..."
                "She starts to wiggle her hips and giggle a little."
                the_person "Excuse me, boss? I think I'm feeling those 'needs' again!"
                $ mc.change_locked_clarity(50)
                "Her playful tone makes it obvious she is playing dumb a little, whereas just a few weeks ago, she would have said something similar to that, but being completely serious."
                "You let your fingers run their way down the inside of her cheeks, dipping them gently in her pussy. She's still soaking wet from when you fucked earlier."
                $ the_person.change_arousal(10)
                "[the_person.title] turns her head back to look at you. Are those puppy dog eyes?"
                the_person "Please, I need you again sir. Please!"
                "God damn no wonder she is so good at negotiating supply contracts, she knows just how to ask."
                "Your cock is rock hard and ready to seal the deal. It's time to fuck [the_person.title] properly now that you have everything out in the open."
                $ mc.change_locked_clarity(50)
                "Your grab her hips and move in close. She reaches between her legs and holds the tip of your erection, guiding you inside of her."
                "You easily bottom out inside of her in one smooth stroke. She groans at the sensations of being filled again."
                the_person "Okay... I'm done being cute. You can rough me up now!"
                if the_person.is_bald():
                    "You reach up and grab her neck."
                else:
                    "You reach up and grab her hair."
                mc.name "I think I'll do that."
                "Pulling her head back, you start to thrust yourself inside of her at a rapid pace. It's time to give it to her good!"
                call fuck_person(the_person,start_position = standing_doggy, skip_intro = True, girl_in_charge = False, position_locked = True, skip_condom = True) from _fuck_doctor_candace_again_02
                "When you finish with her, [the_person.title] is sprawled out across your desk. Your light colored cum on her dark skin is a beautiful contrast."
                "You get yourself cleaned up a bit and looking presentable while she is still recovering."
                the_person "Oh fuck [the_person.mc_title]... Your dick is amazing..."
                "Her breathing is finally starting to slow down a bit."
                the_person "Are we, umm... We doing my place or yours tonight?"
                mc.name "Honestly, I'm not sure if I'll be able to tonight, but I'll let you know."
                the_person "Mmm... Okay... You go ahead... I think I would just like to bask a little..."
                "You consider for a moment getting a nice couch for your office..."
                "But then whenever you call a girl in they'd probably assume you were getting ready to make a cheap porno movie. Better not."
                mc.name "Rest up, I'm going to get back to work."
                "You feel great about how things have progressed with [the_person.possessive_title]."
            "Reject (disabled)":
                pass
    $ clear_scene()
    return
