#Love Events

init -1 python:
    def ellie_never_given_handjob_requirement():
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        return ellie.love >= 20

    def ellie_brings_lunch_requirement():
        if time_of_day != 1:
            return False
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        return ellie.love >= 40 and ellie.story_event_ready("love")

    def ellie_dinner_date_intro_requirement(the_person):
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        return the_person.love >= 60 and ellie.story_event_ready("love")

    def ellie_dinner_date_requirement():
        return day%7 == 6 and time_of_day == 3

    def ellie_lingerie_shopping_requirement(the_person):
        return the_person.love >= 80 and ellie.story_event_ready("love")

init 1 python:
    ellie_dinner_date_intro = Action("Ellie asks for a dinner date", ellie_dinner_date_intro_requirement, "ellie_dinner_date_intro_label")
    ellie_dinner_date = Action("Ellie cooks for you", ellie_dinner_date_requirement, "ellie_dinner_date_label")
    ellie_lingerie_shopping = Action("Ellie dresses up for you", ellie_lingerie_shopping_requirement, "ellie_lingerie_shopping_label")

    def add_ellie_never_given_handjob_action():
        ellie_never_given_handjob = Action("Ellie wants to touch", ellie_never_given_handjob_requirement, "ellie_never_given_handjob_label")
        mc.business.add_mandatory_crisis(ellie_never_given_handjob)
        return

    def add_ellie_brings_lunch_action():
        ellie_brings_lunch = Action("Ellie likes cooking", ellie_brings_lunch_requirement, "ellie_brings_lunch_label")
        mc.business.add_mandatory_crisis(ellie_brings_lunch)
        ellie.story_event_log("love")
        return

label ellie_never_given_handjob_label():    #20 Love event. Requires 20 slut event.
    $ the_person = ellie
    $ the_person.arousal = 0
    $ mc.reset_arousal()
    "You are going about your work, when [the_person.possessive_title] finds you."
    $ the_person.draw_person()
    if mc.location != ceo_office:
        the_person "Hey, can we talk somewhere private?"
        mc.name "Sure."
        $ mc.change_location(ceo_office)
        "You bring her to your office. After stepping inside, she closes the door and locks it."
    mc.name "Have a seat?"
    the_person "Yes sir."
    $ the_person.draw_person(position = "sitting")
    mc.name "What can I do for you?"
    the_person "Are blue balls real?"
    "Wow she is getting right to the point. You have to smile at the way she pronounced blue though."
    mc.name "Wow, umm... yeah, yeah they are."
    the_person "And... and they hurt?"
    mc.name "Yeah, they can, I guess it depends on the situation..."
    the_person "The... other day... when you touched me? Did you get turned on too?"
    mc.name "Yes, it was very hot getting you off with my fingers..."
    the_person "When... when I ran oft... did you get..."
    "She lowers her voice to a whisper."
    the_person "Blue balls?"
    "You stifle your laughter."
    mc.name "Umm, maybe a little bit, but I wouldn't worry about..."
    the_person "So you got me off, for nothing in return? And it actually hurt you?"
    if the_person.has_taboo("touching_penis"):
        the_person "Can... can I try? I want to try something I read about."
        mc.name "Well, I might be up for that, but it depends on what exactly you have in mind."
        the_person "I mean, since then, I've seen all kinds of methods... but I think I can just use my hand... right?"
        mc.name "[the_person.title], are you saying you want to give me a handjob?"
        the_person "Eh!? I mean, you make it sound so dirty, I just..."
        "She is kind of cute when she gets disgruntled."
        the_person "I just want us to be even, okay? I hate the thought of leaving your poor thing all pent up..."
        "You keep quiet about the fact that you've had multiple releases since the incident."
        mc.name "Well I think that's great. I would love to have a nice handjob right now."

    else:
        the_person "Do... do you want me to do that thing, with my hand again?"
        mc.name "I would love a nice handjob right now."
    $ the_person.change_slut(2, 40)
    the_person "Geesh, you don't have to keep saying that..."
    mc.name "Why? I mean, it's what you call it. It's okay, say it. Tell me what you want me to do."
    "[the_person.possessive_title] takes a deep breath."
    the_person "[the_person.mc_title], can I give you a handjob?"
    mc.name "... and?"
    the_person "Wha? and?"
    mc.name "What do you say when you are asking your boss for something?"
    $ the_person.change_obedience(5)
    the_person "Ah... geesh. [the_person.mc_title], can I give you a handjob, please?"
    mc.name "Great! Yes that would be perfect right now."
    "You stand up and walk over to [the_person.title]. She looks up at you from her chair."
    the_person "I... can you get it out?"
    mc.name "Oh, I think it would be a good idea to make this more... educational. Why don't you give it a try?"
    $ the_person.change_arousal(5)
    the_person "Okay [the_person.mc_title]..."
    "Her hands have a little bit of a shake, but she slowly brings them up to your pants."
    mc.name "There you go, now just rub your hands along my pants until you find it."
    "She does as you order, and is soon rubbing her hand up and down your cock through your pants."
    $ mc.change_arousal(5)
    mc.name "Mmm, that's it... now pull down the zipper carefully..."
    "[the_person.possessive_title] pulls the zipper down, then pushes her fingers into your pants."
    "She keeps rubbing your dick with her hand now, but gets confused when she tries to figure how to get it out of your underwear."
    the_person "Isn't... isn't it just supposed to... pop out or something?"
    mc.name "Nope! Thank goodness! There's another hole in the fabric, usually on the side..."
    "She fishes around for several more seconds, but finally finds it."
    mc.name "Now back the other way..."
    "Finally, she gets her hand through. And for the first time in her life, she is holding a dick."
    $ mc.change_locked_clarity(20)
    $ the_person.change_arousal(10) #15
    $ the_person.break_taboo("touching_penis")
    the_person "Oh my stars... it's so warm! And hard!"
    "She starts to stroke you a bit, but having her hand through your pants and underwear makes it hard for her to move."
    "She struggles a bit more but finally manages to pull it out."
    the_person "Oh! It's so big! I... I thought people were exaggerating on the internet..."
    the_person "This thing is supposed to..."
    "She suddenly closes her legs."
    mc.name "Not yet. For now, just give it a couple strokes with your hand."
    $ the_person.change_obedience(2)
    "[the_person.possessive_title] grabs you with her hand and gives you a few slow strokes. Her grip is way too hard."
    mc.name "Gentle now. Think about how soft your vagina is. Try and replicate that with your hand."
    the_person "Ah! Sorry..."
    "[the_person.title] gives you a few softer strokes now. They are much more pleasant."
    $ the_person.increase_sex_skill("Foreplay", 4, add_to_log = True)
    $ mc.change_locked_clarity(20)
    $ the_person.draw_person(position = "blowjob")
    "[the_person.title] gets down on her knees next to you, watching you very closely as she starts her first ever handjob."
    "Thankfully, her hand is very soft as she strokes you off, and the taboo of defiling this southern belle makes it even hotter."
    the_person "One of the things I read about... boys like it when they have something to look at, right?"
    mc.name "That's true."
    the_person "Would you like to... see my boobies?"
    mc.name "I would love to see your titties. Get them out for me [the_person.title]."
    the_person "Ah, okay [the_person.mc_title]."
    $ the_person.strip_to_tits(position = "blowjob")
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(5)
    "Her tits now out for your viewing pleasure, this little session is going great. When she looks back at your dick there is a little pre-cum leaking from it."
    the_person "Ah! It's got stuff coming out!"
    mc.name "Yeah, that is pre-cum. It starts to come out a little bit when I get really turned on."
    mc.name "Don't worry, it doesn't hurt you. Keep going, this feels great."
    "Slowly, [the_person.possessive_title] reaches out and starts to stroke you again. The pre-cum helps, but you wish there was more moisture."
    mc.name "How are you doing, are you getting turned on?"
    the_person "Yeah."
    mc.name "Are you getting wet?"
    the_person "I errm..."
    mc.name "Are you?"
    the_person "Yeah [the_person.mc_title]."
    mc.name "Feel how dry my dick is?"
    the_person "Errr... yeah... it is dry."
    mc.name "I would feel even better if there was more moisture, like what your body is making now."
    the_person "[the_person.mc_title], you can't stick it in there! I'm... that's not..."
    mc.name "That's not what I mean. Let me see your hand."
    the_person "Okay?"
    "You take her hand and bring it up to your mouth. You get a big bit of saliva and spit it into her hand."
    mc.name "Now keep going."
    the_person "Ohhh... okay..."
    $ mc.change_locked_clarity(30)
    $ the_person.change_arousal(5)
    "She resumes stroking you now, and the sensations are much more pleasant. When her hand gets a little dry, she gets the idea and spits into her own hand before resuming."
    "This is turning into an almost acceptable handjob. She might actually be able to get you off."
    mc.name "That's it. Just keep it wet."
    the_person "Got it..."
    "[the_person.title] is watching you closely as she strokes your cock. When she notices it getting dry again, she leans forward for a moment..."
    "You almost think she might actually put it in her mouth... but unfortunately she lets a large glob of saliva drip from her mouth to your erection."
    "She starts stroking again, and with her spit it actually feels really good..."
    "You look down at the busty red head as she strokes you off..."
    "You feel her breath on your skin as she keeps going. You stand and just enjoy the sensations."
    "She re-wets your cock a couple more times, and soon the sensations are really ramping up."
    mc.name "[the_person.title]... I'm going to cum soon..."
    the_person "Oh god, I read about this... okay..."
    "[the_person.possessive_title] keeps stroking you, clearly with no idea what is really about to happen, her face just inches from your cock."
    mc.name "Oh fuck don't stop... don't stop!"
    $ the_person.cum_on_face()
    $ the_person.draw_person(position = "blowjob")
    $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
    "You start to blow your load right onto [the_person.title]'s face. She flinches with each shot, but dutifully keeps stroking you."
    "Spurt after spurt erupts onto her. When you finish, you look down and admire her handywork."
    the_person "Wow... I... that..."
    "She struggles to get a sentence out. Now might be a good time to encourage her..."
    menu:
        "Encourage Her\n{color=#ff0000}{size=18}Increases love{/size}{/color}":
            mc.name "That felt amazing. Thank you so much [the_person.title]."
            the_person "I... yeah... felt good then?"
            mc.name "Very much so."
            $ the_person.change_love(3)
        "She looks hot\n{color=#ff0000}{size=18}Increases sluttiness{/size}{/color}":
            mc.name "Fuck, you look so hot like that, covered in my cum."
            the_person "You like it... yeah?"
            mc.name "Definitely. Maybe next time I'll cover your tits too."
            the_person "Oh my... next time?"
            $ the_person.change_slut(3, 60)
        "Make her taste it\n{color=#ff0000}{size=18}Increases obedience{/size}{/color}":
            mc.name "That's a good girl. Now why don't you lick your fingers clean and give it a taste."
            the_person "Do girls really... do that?"
            mc.name "All the time. Go on."
            "[the_person.title] slowly brings her fingers to her mouth, then licks your cum off them."
            "She grimaces for a second."
            the_person "Oi, that is pretty salty..."
            mc.name "It's an acquired taste. Don't worry, you'll get used to it."
            $ the_person.change_obedience(3)
    $ the_person.draw_person()
    "[the_person.title] stands up."
    the_person "Do you think we should do that again sometime?"
    mc.name "I would certainly like to."
    the_person "Yeah... me too. But I think I'm gonna go find the lady's room..."
    mc.name "Of course. I won't hold you up any longer."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and starts walking out of your office. You watch her hips as she moves away."
    $ clear_scene()
    "You are a bit surprised how quickly she has opened up to you like this. Maybe she is more ready to move past her repressed childhood than you realized?"
    "Either way, you are certain there is more fun to be had with the busty redhead soon."
    #Load up the three story branches
    $ add_ellie_never_tasted_cock_action()
    $ add_ellie_brings_lunch_action()
    $ add_ellie_tit_fuck_action()
    # Link to her team up scenes here also?
    return

label ellie_brings_lunch_label():   #40 love scene. Brings MC lunch to have a date in his office.
    if ellie_has_brought_lunch_date():  #I left a scenario in game where this could occur twice. IF this event has already occurred, just exit immediately.
        return
    $ the_person = ellie
    $ ellie.event_triggers_dict["brought_lunch"] = True
    $ ellie.story_event_log("love")
    "It's the end of the morning shift. You finish up with your work and are just getting ready to head to the breakroom for lunch."
    $ the_person.draw_person()
    the_person "Hey. Doing anything for lunch?"
    mc.name "Ah, hello [the_person.title]. Not in particular, I think I brought some instant noodles I was going to warm up."
    $ the_person.draw_person (emotion = "happy")
    the_person "Good! I got up early this morning and made a few things to bring in... I was wondering if you wanted t'eat with me?"
    mc.name "Oh, that is very kind of you. You enjoy cooking?"
    the_person "Oh, I do! It's hard, I can't find my favorites from growing up around here, so I have to make them myself."
    $ the_person.discover_opinion("cooking")
    the_person "But thankfully I've always loved cooking."
    "It was very kind of her to bring you some food. She has started to get affectionate with you, so you decide to ask if she wants to eat in private."
    mc.name "Want to eat in my office? We could chat a bit and wouldn't be disturbed."
    the_person "Oh! That sounds nice. Like a... errr..."
    mc.name "Like a lunch date?"
    the_person "Oh, yeah... I guess that is kind of silly..."
    mc.name "Oh? I quite like the sound of it. A lunch date sounds great."
    $ the_person.change_love (2, 60)
    the_person "Ah! Let me go get my stuff from the breakroom, I'll meet your at your office [the_person.mc_title]."
    $ clear_scene()
    $ ceo_office.show_background()
    "You head to your office. You wait a few minutes and soon [the_person.possessive_title] arrives."
    $ the_person.draw_person()
    the_person "Knock knock!"
    "[the_person.title] steps into your office and closes the door behind her. She brings over a container filled with food. It smells amazing."
    $ the_person.draw_person(position = "sitting")
    the_person "If there's anything you don't like, don't worry, just pick it out, I won't be offended."
    "You look down. A healthy portion of macaroni and cheese, ham slices, something fried?... and some fresh green beans."
    mc.name "Wow, [the_person.title], this looks delicious. These are?"
    the_person "Fried tomatoes! It's hard to get good tomatoes around here, but these'll do."
    "You take a few bites. The food is all homemade and tastes delicious."
    $ the_person.change_happiness(2)
    "You dig in and start eating. You look up and notice [the_person.title] smile a bit when she sees you enjoying her cooking."
    "She picks up a fork and starts eating with you."
    "When you are about halfway through your food, you realize you haven't said a word since you started eating."
    "You slow down and start to chat with her."
    call date_conversation(the_person) from _call_date_conversation_ellie_01
    "As you finish up with your meal, you look across the desk at [the_person.possessive_title]."
    "It was very kind of her to make this food for you, you want to make sure she knows that you appreciate it."
    mc.name "[the_person.title], that was amazing. Thank you so much for the meal."
    the_person "Oh, of course. I enjoyed making it, and being able to spend some time here with you."
    if ellie_has_given_blowjob():   #WE've already done the blowjob scene. Go straight to eating her out as thanks.
        "There is significant sexual tension in the air. You consider if you should take things with [the_person.title] further..."
        menu:
            "Eat her out":
                mc.name "I think it's time for dessert."
                the_person "Dessert? Oh, I didn't bring any... I could go get a candy bar from the machine..."
                mc.name "That won't be necessary. I have something else in mind."
                the_person "Oh?"
                "You notice some blush in her cheeks as she begins to realize you have something sexual in mind."
                mc.name "Last time you were in my office, you got to have dessert. I think it is my turn this time."
                mc.name "I want you to sit on my desk."
                "You get up and walk over to your office door and lock it. When you turn back, [the_person.title] has gotten up on your desk."
                call ellie_cunnilingus_office_label(the_person) from _ellie_lunch_date_dessert_ending_01
                $ the_person.draw_person (position = "missionary")
                "You stand up, leaving [the_person.possessive_title] on your desk, panting."
                the_person "That... was that like, how it made you feel? You know, when I sucked on yours?"
                mc.name "Probably not exactly the same, but similar, yes."
                the_person "Stars... [the_person.mc_title] I owe you... maybe if I practice I can do that as good to you as you did it to me..."
                mc.name "Of course. I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
            "Finger her":
                mc.name "I think it's time for dessert."
                the_person "Dessert? Oh, I didn't bring any... I could go get a candy bar from the machine..."
                mc.name "Don't bother. I have something else in mind. Would you stand up please?"
                "As [the_person.possessive_title] stands up, you walk around behind her..."
                $ the_person.draw_person(position = "back_peek")
                "You let your hands start to roam all over the busty redheads body."
                "She flinches at first, still not used to your touch, but quickly leans back and begins to enjoy it."
                mc.name "Let me show you how thankful I am for that delicious meal."
                the_person "Ahh, okay... do you want you want then..."
                call fuck_person(the_person, private=True, start_position = standing_finger, skip_intro = False) from _call_ellie_post_lunch_finger_01
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    "[the_person.possessive_title] is breathing heavy, recovering from her orgasm."
                    the_person "Mmm, that was good. I think I need a minute..."
                mc.name "I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
    else:
        "There is some tension in the air... but you decide for now it would be better not to act on it."
        mc.name "Yes, it was great. Thank you again."
        "You stand up and [the_person.title] does the same."
        $ the_person.draw_person()
        "You leave your office together and go back to the work day."
    $ ellie.story_event_log("love")
    $ ellie.apply_planned_outfit()
    $ ellie.add_unique_on_talk_event(ellie_dinner_date_intro)
    $ clear_scene()
    $ mc.location.show_background()
    return

label ellie_cunnilingus_office_label(the_person):
    $ the_person.draw_person (position = "sitting")
    $ the_person.arousal = 0
    "You walk over to [the_person.title]. You can see her trembling slightly as you get close."
    mc.name "[the_person.title], I am going to eat you out now. Are you okay with that?"
    the_person "[the_person.mc_title], isn't that kind of gross?"
    mc.name "Nonsense. You already got to taste me. It's only fair I get to return the favor!"
    if the_person.vagina_available:
        mc.name "Now, go ahead and scoot to the end of the desk and open your legs. I want to see your beautiful cunt."
        "[the_person.possessive_title] obeys, but blushes in embarrassment at your words."
        $ the_person.change_slut(2, 60)
    else:
        "You slowly remove her bottoms. She doesn't resist and lets you strip her down."
        $ the_person.strip_to_vagina(position = "sitting")
        "Once exposed, you pull her to the edge of your desk and urge her legs apart."
    $ the_person.draw_person(position = "missionary")
    $ mc.change_locked_clarity(50)
    "You kneel down and look closely. [the_person.possessive_title]'s fresh, virgin cunt is inches away."
    "You are certain that you are the first person to do this with her, and it is really turning you on."
    the_person "You... you just gonna look mister?"
    "The nervous edge in her voice is so cute. You decide not to respond, instead you lean forward the last couple of inches."
    "You stick out your tongue and run it up and down her slit, just barely touching it."
    $ the_person.break_taboo("licking_pussy")
    $ play_moan_sound()
    the_person "Ah! Oh my..."
    $ the_person.change_arousal(10)
    "You slither you tongue inside of [the_person.title]'s pristine pussy. You take your time and explore her crevice."
    "Her smell and taste is musky but with a hint of vanilla. Your tongue travels all up and down her slit, although you purposefully detour around her clit."
    $ the_person.change_arousal(10)
    "Curious about her taste at the source, you snake your tongue down to her entrance proper. You tongue smoothly pushes slightly into her virgin hole."
    "The opening is so tight you can barely fit your tongue, but she moans at the intrusion."
    $ play_moan_sound()
    the_person "Ohhhh... that's so good..."
    $ the_person.change_arousal(20)
    "You feel her soft hand settle gently on your head as she gives in to the pleasure you are giving her."
    "You slide your tongue inside of [the_person.possessive_title]'s cunt as far as you can reach."
    "You swirl it around, enjoying all the soft sensations and tastes of her pussy."
    $ the_person.change_arousal(20)
    "So far, you've stayed away from her clit, but it is time to push her into the final stretch. You pull your tongue from her hole and then lick your way up her slit."
    the_person "Mmm, that was so... OH!"
    "You circle [the_person.title]'s clit once, the slide your tongue across it. Her back arches and the hand on the back of your head suddenly grabs your hair."
    "You slide it across again and again, each time with slightly increasing pressure. Then her hips begin to move with you."
    $ the_person.change_arousal(25)
    the_person "Stars, I can't... [the_person.mc_title]!"
    $ play_moan_sound()
    "Lapping eagerly at her clit, you run your hands along her stomach, down her legs and the insides of her thighs."
    "Her back arches and she moans loudly as she gets ready to cum."
    $ the_person.change_arousal(25)
    the_person "!!!!!!!"
    "The hand on the back of your head grabs your hair and pulls you closer. You can feel her legs wrap around your back as she starts to cum."
    $ the_person.have_orgasm()
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("getting head", max_value = 1)
    if ellie_is_a_squirter():
        "Suddenly, your whole face is soaked in [the_person.possessive_title]'s juices. As her body writhes in pleasure, she squirts a bit with every wave."
        "You keep your attention on her clit, enjoying getting her off with such a strong orgasm."
    else:
        "[the_person.possessive_title] writhes in pleasure as she cums."
        "You keep your attention on her clit, enjoying getting her off with a strong orgasm."
    the_person "That... that was amazing..."
    menu:
        "Keep going" if mc.sex_skills["Oral"] >= 3:
            pass
        "Keep going \n{color=#ff0000}{size=18}Requires better oral skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 3:
            pass
        "Get up":
            "You look up from between [the_person.possessive_title]'s shapely legs and smile."
            mc.name "I suppose that is enough for now."
            return
    "{i}You haven't seen anything yet,{/i} you think to yourself. You give her a few moments to catch her breath, then begin licking at her slit again."
    the_person "Mmm... that's nice... I... you can stop..."
    "You bring your face away from her body for a second to say a single word."
    mc.name "No."
    "Her legs tremble slightly when you return to your work, licking at her sopping cunt."
    the_person "No? Wha... but dun... OH..."
    "You flick your tongue across her clit again, and suddenly she feels the spark of more arousal."
    $ the_person.change_arousal(10) #65
    $ the_person.change_obedience(5)
    "The hand on the back of your head is trying to pull you away now, but you easily fight it. Now instead of pressure, you flick your tongue across her clit in various rhythms and directions."
    "After experimenting some, you find a good rhythm and can feel her hips start to respond to your continuing licking."
    $ the_person.change_arousal(15) #80
    the_person "Buh... I read about... but I didn't think... more than once..."
    "You put both hands under her ass and grope her pliant cheeks. The hand on your head relaxes now, and [the_person.title] is having trouble forming sentences."
    the_person "Ah, stars! [the_person.mc_title]... keep... ah! I'm... YES!"
    $ the_person.change_arousal(15) #95
    "Legs start to wrap around your back again, and the hand on your head is pulling you closer. This seems to be a pattern for her as she gets ready to cum again."
    "As your finishing move, you latch onto her clit with your lips and start to lightly suckle on it. Her back arches and her cries grow urgent."
    the_person "[the_person.mc_title]! I'm... yer gonna!!! AH!"
    $ the_person.change_arousal(25) #120
    "Her body seizes as another orgasm hits her. Loud panting and moaning, and then suddenly release."
    $ the_person.have_orgasm()
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("being submissive", max_value = 2)
    if ellie_is_a_squirter():
        "Another round of fluid erupts from her depths as she cums. She is making an absolute mess of your desk and your face, but you don't care."
        "Your mouth stays latched to her clit you push her through her second orgasm."
    else:
        "[the_person.title] is trying in vain to move her hips with you, but she has lost the ability to do any more than twitch now and then."
        "Your mouth stays latched to her clit you push her through her second orgasm."

    the_person "That... STARS... I never thought that... was possible..."
    the_person "You umm... yer done... right?"

    menu:
        "Not a chance" if mc.sex_skills["Oral"] >= 6:
            pass
        "Not a chance \n{color=#ff0000}{size=18}Requires better oral skill{/size}{/color} (disabled)" if mc.sex_skills["Oral"] < 6:
            pass
        "Done":
            "You look up from between [the_person.possessive_title]'s shapely legs and smile."
            mc.name "I suppose that is enough for now."
            return
    the_person "'Not a chance'? Seriously??? I can't... AH!"
    "Your mouth latches on to her clit again. Now you are alternating between hard and soft suckling as her body begins to respond again."
    $ the_person.change_arousal(10) #70
    "[the_person.possessive_title]'s body is responding to your tongue, but you know that this time you'll need to use more than just that."
    "You take a break from suckling her clit for a moment and lick her slit up and down. Then you bring your index up and push it up against her virgin hole."
    the_person "That feels good, but I'm not sure that I can do this again [the_person.mc_title]..."
    "Well, you'll be damned if you're not going to try anyway. With slow, gentle pressure, you push your finger into her incredible tight hole."
    the_person "Ah... Ohhh my..."
    "You manage to get it all the way in, but there isn't much room to work with. You turn your hand so your palm is facing up, and start to move it with a slow come-hither motion."
    $ the_person.change_arousal(10) #80
    "As you stroke her, you soon find the little g-spot in the front of her vagina and start to massage it with your finger. Her moans are starting to turn into growls."
    the_person "Agghghh... what is... ahhhhh. Maybe if you... aggghhhh..."
    "You continue to stroke and can feel her hips moving again. You lick her clit a few times now, and then start to suckle it again."
    $ the_person.change_arousal(15) #95
    "Your skillful assault on [the_person.possessive_title]'s body is paying off. She is writhing from your touch and her legs wrap around your back even more urgently now."
    the_person "I'M!... HOW IS THIS!?! [the_person.mc_title]??? I'M GONNA GO AGAIN!"
    "That's your cue. Thankfully [the_person.title] is very vocal, so it is easy to gauge when it is time to focus."
    "You suckle her clit urgently now, and your finger strokes her silky insides as her entire body begins to tremble."
    $ the_person.have_orgasm(half_arousal = False)
    $ mc.change_locked_clarity(50)
    $ the_person.increase_opinion_score("getting head", max_value = 2)
    if ellie_is_a_squirter():
        "A third round of fluid is ejaculated forcefully as she cums. Her juices are now running down the side of your desk."
        "Your hand and face are soaked, but you focus your efforts and coax her through a third orgasm."
    else:
        "[the_person.title] lets out a moan as her body has a third powerful orgasm."
        "Your skillful mouth and finger guide her through it."
    "When she finishes, her body goes limp."
    the_person "Stop! You have to stop! I can't... I might die!"
    "You release her body and chuckle from between [the_person.possessive_title]'s shapely legs."
    the_person "Wha? I'm not joking! I'll have like... a heart attack or something!"
    "You can't help but laugh. She smacks your shoulder but doesn't have the strength to put any real force into it."
    return

label ellie_dinner_date_intro_label(the_person): #Ellie invites MC over for dinner
    $ the_person.draw_person(position = "sitting")
    "You walk into the research lab. You notice [the_person.possessive_title], sitting at her station and getting some work done."
    "Recently, you have grown a bit fond of the southern redhead. Something about her innocence has made your playtime fun."
    "You decide to go see how she is doing. You walk over to her desk."
    mc.name "Hey [the_person.title]. How's it going over here?"
    "She looks up from her work and smiles."
    the_person "Oh hey [the_person.mc_title]. I was hoping I would see you today."
    mc.name "Oh? And why is that?"
    the_person "I know you know this, but, I love to cook. I was thinking about making up something and thought maybe you'd like to come over and have dinner with me?"
    mc.name "Dinner? At your place?"
    the_person "Yeah, pretty much. I was thinking maybe Sunday night if it isn't any trouble for you."
    "Apparently [the_person.possessive_title] has been enjoying your time together, also. The chance to be alone with her, at her place, could make for some interesting opportunities."
    if ellie_has_given_virginity():
        "You can hardly forget how hot it was, when you took her virginity. It appears she is enjoying her new found sexuality also."
    else:
        "You wonder if this might be the opportunity you finally need to deflower the busty redhead..."
    mc.name "That sounds great. Sunday night. I'll bring a bottle of wine?"
    the_person "Oh, you don't have to bring anything, but if you really want to that would be sweet of you."
    mc.name "Sunday night then."
    $ clear_scene()
    "You step away from [the_person.title]'s desk. Sounds like you have a dinner date Sunday!"
    $ mc.business.add_mandatory_crisis(ellie_dinner_date)
    return

label ellie_dinner_date_label():
    $ the_person = ellie
    $ ellie.event_triggers_dict["dinner_date"] = False
    $ ellie.story_event_log("love")
    "It is Sunday night. You have a dinner date with [the_person.title] tonight. You shoot her a text and she sends you her address."
    $ mc.change_location(downtown)
    "You swing by a store on the way there and pick up a bottle of mid range red wine. The make your way to her place."
    $ mc.change_location(her_hallway)
    "Soon, you are at the front door to her apartment, knocking on her door."
    $ the_person.learn_home()
    $ the_person.draw_person()
    the_person "Ah! You're here! Come in!"
    $ mc.change_location(the_person.home)
    "When you step inside, you are immediately assaulted by number of heavenly smells."
    mc.name "Oh my god. It smells amazing in here."
    the_person "Ah, thank you! I made up some jambalaya and cornbread. Dessert is still in the oven but I hope you like peach cobbler..."
    "Your mouth is watering. This girl can cook!"
    mc.name "That sounds incredible. Here, I brought this."
    "You hand her the bottle of wine. She takes it and sets it on the counter."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] starts working on portioning out some food. You walk up behind her and wrap your arms around her stomach. She sighs."
    the_person "Ah it's almost... almost ready..."
    "You kiss her on the neck a bit, running one hand up her stomach and up to her generous chest..."
    $ the_person.change_arousal(10)
    $ the_person.draw_person(position = "back_peek")
    the_person "Ahh... sit yourself down... I didn't make this soup for nothing!"
    "Reluctantly, you let her go, then sit down at her table."
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] finishes putting out food, then sits down beside you."
    "You dig in to the jambalaya. It has considerable heat, but tastes amazing."
    "As you eat, you make some small talk with [the_person.title]. However, you can feel sexual tension building throughout the meal."
    "At one point, you feel [the_person.possessive_title]'s foot next to yours, and she slides it up and down the side of your legs a couple times."
    "A buzzer goes off in the kitchen."
    the_person "Ah! The cobbler should be done! Let me go pull it out..."
    $ the_person.draw_person(position = "walking_away")
    "Last time anyone says that tonight..."
    "She jumps up and heads back to the kitchen. You watch her as she walks away from the table."
    $ the_person.draw_person(position = the_person.idle_pose)
    "In a few minutes, she re-emerges with two bowls of peach cobbler with a scoop of vanilla ice cream."
    "She sets one down next to you, then sits down."
    $ the_person.draw_person(position = "sitting")
    the_person "This is one of my favorites. My momma made this for me when I was growing up."
    "You take a bite. The peaches and ice cream meld together into a savory dessert."
    mc.name "Wow... this is really good..."
    "You dig in, barely saying a word as you down it."
    "You finish the last bite of your peach cobbler. You look up at [the_person.possessive_title]. There is an obvious tension in the air."
    if ellie_has_given_virginity():
        "Note from the author. You have already had sex with [the_person.title]."
        "However, you can reset her virginity status now to experience this part of the story as if it were her first time."
        "Would you like to experience this event as if she is still a virgin?"
        menu:
            "Yes. Take her virginity (again)":
                $ restore_virginity(the_person)
            "No.":
                pass
    if ellie_has_given_virginity():
        "You decide it is time to make your move. You get up from your chair and walk around to [the_person.title]."
        the_person "Ah, what are you coming over here for AH."
        "You pick her up roughly and she clings to you."
        $ the_person.draw_person(position = "against_wall")
        mc.name "Which way to the bedroom."
        the_person "Back there!"
        $ mc.change_location(the_person.bedroom)
        "She points to her bedroom door. You quickly open up and maneuver her through it, then throw her down on the bed."
        $ the_person.draw_person(position = "missionary")
        the_person "I know you aren't the typical romance type... but once in a while it is nice to do things the old fashioned way!"
        mc.name "Don't worry. What we are about to do is VERY old fashioned."
        "You decide to get her naked before you go any further."
        mc.name "Let's get these pesky clothes off you now, [the_person.title]."
        $ the_person.strip_outfit(position = "missionary")
        "You look down at [the_person.possessive_title]. Time to get some."
        call fuck_person(the_person, start_position = missionary, start_object = make_bed(), private = True, skip_condom = True, skip_intro = True) from _call_sex_description_ellie_after_dinner_encore_01
        $ had_sex = True
    else:
        mc.name "Thank you [the_person.title]. That was delicious."
        the_person "Aww, it was nothing..."
        "She scoops the last of her dessert from her bowl, finishing it off."
        the_person "You ummm... want some coffee or something?"
        mc.name "Not particularly, but I'm also not ready to leave yet."
        the_person "Well umm, I just realized, I hadn't give you a tour of the place yet..."
        "She looks around."
        the_person "I mean... it's just an apartment but ummm..."
        mc.name "Well I wouldn't mind seeing the inside of the bedroom."
        $ the_person.change_arousal(5)
        the_person "Oh! That's a great idea..."
        $ the_person.draw_person(position = "walking_away")
        "You get up and follow [the_person.possessive_title] into her bedroom."
        $ mc.change_location(the_person.bedroom)
        $ the_person.draw_person(position = the_person.idle_pose)
        the_person "This is it... this is where I..."
        "Her voice drifts off as you close in on her."
        $ the_person.draw_person(position = "kissing")
        "You both wrap your arms around each other. Your tongues meet and you eagerly make out."
        $ the_person.change_arousal(5)
        $ mc.change_arousal(5)
        "You reach behind her and grab her ass. She gives a little moan as you start to knead it."
        "You grab her ass with both hands now and roughly lift her up."
        $ the_person.draw_person(position = "against_wall")
        the_person "Mmm... oh [the_person.mc_title]..."
        "[the_person.possessive_title] wraps her legs around you. Your cock is now nestled between her legs as she rubs herself against you."
        "You walk forward to her bed and then fall forward onto it."
        $ the_person.draw_person(position = "missionary")
        $ the_person.change_arousal(15)
        $ mc.change_arousal(15)
        the_person "Oh stars, you make me feel so good [the_person.mc_title]..."
        "You stop making out for a second, and she looks into your eyes."
        the_person "Will you... you know..."
        "She leaves her question unasked."
        mc.name "No... I don't know. What do you want?"
        the_person "I... I want you, [the_person.mc_title]..."
        the_person "I know it sounds crazy, but I can't stop thinking about you. I know you may not feel the same way but... I want my first time to be with you."
        "Yes! It is finally time to take [the_person.title]'s cherry."
        mc.name "[the_person.title]. If you are certain, I would be proud to be your first."
        the_person "I am. I know the first time is gonna hurt... but it's okay. I want you to take me, and don't stop until you finish, okay?"
        mc.name "Alright. If you're sure. But first, you're wearing way too many clothes..."
        "You quickly start to peel off all of [the_person.possessive_title]'s clothing."
        $ the_person.strip_outfit(position = "missionary")
        "Once she is naked, you quickly strip down yourself, then take a moment to admire the busty redhead beneath you."
        "It isn't every day you get to take a woman's virginity, so you want to savor this."
        mc.name "Do you... want me to wear a condom?"
        "[the_person.title] shakes her head."
        the_person "I know I should... but for my first time... I want to experience everything..."
        mc.name "Are you on birth control?"
        the_person "No... I... I never thought I would need to..."
        mc.name "Do you understand... it is possible that you could get pregnant?"
        the_person "Yes... I understand."
        "Fuck! Looks like it is up to you. Are you going to go into this raw?"
        menu:
            "Put on a condom":
                $ mc.condom = True
                mc.name "I'm sorry, but I don't trust myself to pull out, and I'm not quite ready to take that chance."
                the_person "I understand. Take me how you want."
                "You reach over to your pants, grab your wallet and quickly pull out a condom. You quickly slide it on."
            "Go bareback":
                mc.name "The odds are pretty slim... but it is possible that I won't be able to pull out in time."
                the_person "I know. I kind of want to know what it is like... to feel it... I mean..."
                "[the_person.possessive_title] blushes with the last of her words."
                $ the_person.increase_opinion_score("bareback sex")
                $ the_person.increase_opinion_score("creampies")
        "You get into position on top of her. She spreads her legs wide and puts her hands on your back."
        $ the_person.change_arousal(15)
        mc.name "Alright, last chance to back out. After this, there is no going back."
        the_person "Do it... I'm ready!"
        mc.name "Okay..."
        "With her legs spread wide, your cock easily finds her slick entrance. She is wet and about as ready as she can be."
        "You slowly push yourself inside her. Barely inside, you hit her hyman. She winces a bit."
        mc.name "Alright. Here we go. 1...2...3..."
        "At three, you push inside forcefully. Her body resists for just a moment, then gives way, giving you access to her depths."
        the_person "Fuck! Oh stars..."
        $ take_virginity(the_person)
        $ the_person.draw_person(position = "missionary")
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True, condition = make_condition_taking_virginity()) from _call_fuck_person_ellie_love_60_01

    $ the_person.draw_person(position = "missionary")
    "When you are finish, you collapse onto [the_person.title]'s bed next to her."
    the_person "That was amazing."
    mc.name "Yeah."
    if the_person.is_girlfriend:
        pass
    else:
        the_person "So umm... I don't know if this is something you had considered or not but..."
        the_person "Don't people usually like... say they are boyfriend and girlfriend when they do stuff like that?"
        mc.name "Some people do."
        the_person "Ah... umm... do you?"
        "[the_person.possessive_title] is curious if you want to make your relationship a bit more official. What do you want to do?"
        menu:
            "Ask her to be your girlfriend":
                mc.name "I do. [the_person.title], will you make it official? Will you be my girlfriend?"
                the_person "Oh thank the stars, yes!"
                $ the_person.add_role(girlfriend_role)
                $ the_person.change_love(5, 80)
                $ the_person.change_happiness(10)
                "[the_person.possessive_title] rolls over and gives you a lingering kiss on the lips."
                the_person "You... you wanna stay the night?"
                mc.name "I'm sorry, I didn't arrange for that. But I definitely will soon."
                the_person "Okay."
            "Say you aren't sure yet":
                mc.name "I really enjoy spending time with you [the_person.title], but things are moving really fast. I'm not sure I'm ready to commit to that yet."
                the_person "Ah... yeah... they have moved really fast, ain't they."
                $ the_person.change_love(-2, 80)
                $ the_person.change_happiness(-2)
                "You can tell she is a little disappointed, but she tries to hide it."
    "You get up and get your clothes back on. [the_person.possessive_title] stays in bed."
    mc.name "I can see myself out. Have a good night."
    the_person "Goodnight [the_person.mc_title]! I'll see you at work tomorrow..."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You step out of [the_person.possessive_title]'s apartment."
    $ the_person.add_unique_on_room_enter_event(ellie_lingerie_shopping)
    return

label ellie_lingerie_shopping_label(the_person):    #Ellie's 80 love event. She asks MC to take her shopping for exciting underwear to wear for him.
    $ ellie.story_event_log("love")
    return
