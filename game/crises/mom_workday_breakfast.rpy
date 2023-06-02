## Morning crisis
#Have breakfast with Jennifer. Designed as an opportunity to raise her obedience, and to give some variation to morning events
#You wake up and have breakfast with Jennifer. At minimal sluttiness, gives MC the option to giver her a motivational speech.
#At mid sluttiness, MC can tell Jennifer she should try going to work without underwear on, try and get attention from men that way.
#At high sluttiness, Jennifer asks MC to cum on/in her so she can feel it throughout the day.
#Fetish options: for Anal, Jennifer asks for anal, for cum fetish, you cum on/in her as appropriate, and for vaginal, she asks for creampie.
init 2 python:
    def mom_breakfast_crisis_requirement():
        if mc.is_home and mc.business.is_work_day and not mom.is_employee:
            return mom.is_available and not mom.has_queued_event("sleeping_walk_in_label")
        return False

    def mom_commando_day_selfie_requirement():
        if time_of_day == 2: #It is the end of the day
            return True
        return False

    def mom_breakfast_mod_initialization(action_mod):
        # No Init code for this yet.
        return

    def add_mom_commando_day_selfie_action():
        mom_commando_day_selfie_action = Action("Mom Commando Selfie", mom_commando_day_selfie_requirement, "mom_commando_day_selfie_label")
        mc.business.add_mandatory_crisis(mom_commando_day_selfie_action)
        return

    mom_breakfast_crisis_action = ActionMod("Breakfast with Mom", mom_breakfast_crisis_requirement,"mom_breakfast_action_label", initialization = mom_breakfast_mod_initialization,
        menu_tooltip = "You have breakfast with Mom before she goes to work..", category="Home", is_crisis = True, is_morning_crisis = True)

label mom_breakfast_action_label():
    "You wake up, shower, and get ready for the day. As you finish getting ready you notice the smell of bacon and coffee coming from the kitchen."

    python:
        mc.change_location(kitchen)
        the_person = mom
        scene_manager = Scene()
    #"When you walk out to the kitchen, you see [the_person.title] just sitting down to some breakfast."
    # surprise scene, you walk into the kitchen and mom and lily are going at it
    if mc.business.event_triggers_dict.get("family_threesome", False) and renpy.random.randint(0, 3) == 1 and lily.is_available:
        call mom_breakfast_action_mom_and_lily_label() from _call_mom_breakfast_action_mom_and_lily_label
    else:
        $ scene_manager.add_actor(the_person, position = "sitting")
        mc.name "Good morning, [the_person.title]. That smells great!"
        "She sees you walk into the kitchen and greets you warmly."
        the_person "Good morning! I made extra, grab some breakfast! I want you well fed going to work today."
        "You grab some coffee and some bacon and sit down next to [the_person.possessive_title]. She is shaking her head while she looks at her phone."
        #$ the_person.draw_person(position = "sitting",emotion="angry")
        $ scene_manager.update_actor(the_person, position = "sitting", emotion="angry")
        mc.name "Everything okay?"
        if the_person.sluttiness < 20:  #Low Sluttiness path
            call mom_breakfast_action_label_low() from _call_mom_breakfast_action_label_low
        elif the_person.sluttiness < 70 or the_person.has_taboo("vaginal_sex"): #mid sluttiness path or no sex yet
            call mom_breakfast_action_label_medium() from _call_mom_breakfast_action_label_medium
        else:
            call mom_breakfast_action_label_high() from _call_mom_breakfast_action_label_high

    $ scene_manager.clear_scene()
    return _return

label mom_breakfast_action_label_low():
    "She wrinkles her nose for a second and then looks up at you."
    the_person "What? Oh... sorry, I was just looking at this work email. Sometimes I just feel so burnt out."
    "You look down at your coffee. You should probably say something."
    menu:
        "Emphasize Family": #This will increase love value.
            mc.name "You work so hard, [the_person.title]. You are pretty amazing, sacrificing so much for your family."
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person "Thank you, [the_person.mc_title], for your kind words. You and your sister mean so much to me, it's a good reminder why I do what I do sometimes."
            $ the_person.change_stats(happiness = 2, love = 5)

        "Emphasize Happiness": #This will increase happiness (duh)
            mc.name "I'm sorry work is such a pain. Just think about the weekend coming up, maybe you and [lily.fname] can go shopping or something?"
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person "Thank you, [the_person.mc_title], for your kind words. You and your sister mean so much to me, it's a good reminder why I do what I do sometimes."
            $ the_person.change_stats(happiness = 5, love = 2)

        "Emphasize Stability": #This will increase obedience
            mc.name "I'm sorry work is annoying. I know you do it just to keep us afloat, but I have a good feeling about this business I'm running now, I can start supporting the family more soon."
            "Your kind words bring a smile to her face."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person "Oh, thank you [the_person.mc_title], but you don't need to worry about supporting me. I'm just happy to see you making something of yourself."
            $ the_person.change_stats(happiness = 2, obedience = 5)
    "You and [the_person.title] chat for a while longer, until you finish with your breakfast."
    mc.name "Thanks for the great breakfast! I'll see you tonight after work!"
    "You say goodbye to her and head out for the day."
    return None

label mom_breakfast_action_label_medium():
    "She wrinkles her nose for a second and then looks up at you."
    the_person "What? Oh... sorry! I was supposed to meet with this guy after work today for a few drinks, but he cancelled on me!"
    "[the_person.title] mutters to herself for a moment."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion="sad")
    the_person "I mean, what does a woman my age have to do to get some male attention? It feels like no one even notices me at work anymore."
    "You look down at your coffee. You should probably say something."
    menu:
        "Go Commando": #Tell her to go without underwear. Has a chance of causing an event later in the day where she sends you a selfie with cum somewhere on her.
            mc.name "There are a few girls at my company that come in to work sometimes without any underwear on when they are looking for attention. Maybe you should try that?"
            "[the_person.title] thinks for a moment."
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
            the_person "You know what? Why not! I used to do that on dates when I was younger. If nothing else, it'll make me feel young!"
            "[the_person.title] gets up and gives you a quick peck on the cheek."
            $ scene_manager.update_actor(the_person, position = "stand4")
            the_person "You have a good day at work, I'm going to go umm, get changed!"
            python:
                the_person.draw_person(position = "walking_away")
                the_person.change_stats(obedience = 5, slut = 1, max_slut = 30)
                if the_person.planned_outfit.get_panties():
                    the_person.planned_outfit.remove_clothing(the_person.planned_outfit.get_panties())
                the_person.apply_planned_outfit()
                if the_person.sluttiness > 50:
                    add_mom_commando_day_selfie_action()
            return None
        "Give Her Some Attention":  #Sluttiness staircase event, take it farther the sluttier she is
            mc.name "I'm sorry [the_person.title], I didn't realize you were in need of some attention!"
            "You get up from your chair and walk around behind [the_person.possessive_title]."
            the_person "[the_person.mc_title]? What are you... oohhhh."
            "You put your hands on her shoulders and begin to massage them. She sighs as your hands begin to work on her tension."
            menu:
                "Grope her breasts" if the_person.sluttiness > 30 and not the_person.has_taboo("touching_body"):
                    "You work on her shoulders for a couple of minutes, then slowly run your hands down to her considerable chest."
                    the_person "Oh [the_person.mc_title]... I'm not sure..."
                    "You interrupt her and whisper in her ear."
                    mc.name "Sshhh, just relax. Close your eyes and relax."
                    $ the_person.change_arousal(15)
                    "You roll her nipples a couple of times between your fingers. She sighs at the sensations you are giving her."

                "Finish Massage":
                    "You work on her shoulders for a while. She sighs in relaxation. You finish up and go back to your breakfast."
                    return None
            if the_person.tits_available:
                "This skin of [the_person.possessive_title]'s creamy tits feels hot and soft in your hands."
            else:
                menu:
                    "Pull Her Top Up" if the_person.sluttiness > 40:
                        $ scene_manager.strip_to_tits(person = the_person, prefer_half_off = True)

                        "You reach down and slowly remove her top, exposing her creamy tits."
                        $ the_person.break_taboo("bare_tits")
                        "Your hands return to her chest, her boobs feel hot and soft in your hands."

                    "Finish Massage":
                        "[the_person.possessive_title] feels great, but eventually you decide it is too risky to keep going."
                        "[the_person.title] shakes her head a bit as you sit back down, as if trying to clear some thoughts from her head."
                        return None
            #Assume we are still going
            "She arches her back as the pleasurable feeling of having her tits played with begins to grow."
            $ the_person.change_arousal(20) #35
            the_person "Oh, that feels so good, but we should probably stop before your sister comes out..."
            menu:
                "Pet Her Pussy" if the_person.sluttiness > 30 and not the_person.vagina_available and not the_person.has_taboo("touching_vagina"):
                    "You whisper in her ear."
                    mc.name "I've got a better idea."
                    "You let one hand slowly descend from her breast down to the mound between her legs."
                    if the_person.outfit.can_half_off_to_vagina():
                        "Pushing some clothing out of the way as you go along."
                        $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
                    the_person "Oh! Mmmm, okay..."
                    "[the_person.title] lets out a little yelp when you first make contact with her groin."
                    "She arches her back again as you begin to nibble at her ear."
                    $ the_person.change_arousal(30) #65
                    menu:
                        "Finger Her" if the_person.sluttiness > 50:
                            "You bring your hand up a bit, then slowly down again, this time beneath her clothing."
                            "This time, she doesn't put up a fight, she is too close to cumming."
                            "Your fingers are now sliding across the flesh of her moistened cunt."
                        "Finish Massage":
                            "You decide for now just to tease her. You pet her through her clothes for a minute longer then stop, kissing her on her neck."
                            "[the_person.title] looks at you as you sit down, arousal clear in her eyes."
                            mc.name "Don't want to go too far, [lily.fname] could walk out at any moment..."
                            "She shakes her head for a moment, trying to clear her thoughts, but it is obvious her mind continues to dwell on how it could go if you had kept going..."
                            $ the_person.change_stats(obedience = 5)
                            return "Advance Time"
                "Finish Massage":
                    "You pinch and pull at her nipples for a few more minutes, but eventually you decide just to tease her for now."
                    "[the_person.title] looks at you as you sit down, arousal clear in her eyes."
                    mc.name "Don't want to go too far, [lily.fname] could walk out at any moment..."
                    $ the_person.change_stats(obedience = 5)
                    return "Advance Time"
                "Finger Her" if the_person.sluttiness > 50 and the_person.vagina_available and not the_person.has_taboo("touching_vagina"):
                    "You whisper in her ear."
                    mc.name "I've got a better idea."
                    "You let one hand slowly descend from her breast down to her exposed cunt."
                    $ the_person.break_taboo("touching_vagina")
                    $ the_person.change_arousal(30) #65
            #We assume here we are fingering her to completion.
            "You dip two fingers into her honeypot. She moans as your begin to stir your fingers for a bit."
            $ play_moan_sound()
            the_person "Oh honey, that feels so good..."
            $ the_person.change_arousal(20) #85
            "Her hips are beginning to move on their own now, needily grinding against your hand."
            "Her breathing is getting ragged. You begin to circle her clit with your fingers, trying to finish her off."
            the_person "Oh! That's it! Oh god I'm gonna..."
            "[the_person.title]'s body tenses, then convulses. She is able to muffle her noises to a whimper, trying not to alarm your sister."
            $ the_person.call_dialogue("climax_responses_foreplay")
            $ the_person.have_orgasm()
            $ the_person.change_stats(obedience = 3)
            "When she has finished climaxing, you slowly withdraw your finger and sit back down at the table. You take a quick sip of your coffee."
            "[the_person.title] is just putting her clothing back in place when your sister comes out of her room."
            $ the_person.apply_planned_outfit()
            $ scene_manager.draw_scene()
            "She grabs some cereal and sits at the table with you and [the_person.title]."
            $ scene_manager.add_actor(lily, position = "sitting", display_transform = character_left_flipped)
            lily "Good morning! Thanks for the coffee mom!"
            the_person "Good... Good morning dear..."
            "[lily.title] looks over at [the_person.title] with some concern."
            lily "Are you feeling okay mom? Your cheeks are all flushed and you look so... tired?"
            the_person "Of course dear, I was just getting ready to go get ready for work..."
            $ scene_manager.update_actor(mom, position = "stand2")
            "As [the_person.possessive_title] starts to get up, she looks at you. You make sure she notices as you lick some of her juices off your fingers."
            the_person "Oh my..."
            $ scene_manager.update_actor(mom, position = "walking_away")
            "[the_person.title] turns and leaves the kitchen in a hurry. You quickly finish breakfast and head out as well."
    return "Advance Time"

label mom_breakfast_action_label_high():
    "She wrinkles her nose for a second and then looks up at you."
    the_person "What? Oh... sorry! I was just sending some dirty text messages with this guy at work, but he has to go because of his wife or something..."
    "[the_person.title] mutters to herself for a moment. Then she looks over at you."
    $ scene_manager.update_actor(the_person, position = "sitting", emotion="happy")
    the_person "Say... you look awfully handsome this morning..."
    "She looks around, and notices the door to your sister's room is still closed. She must be sleeping in."
    the_person "I had some really crazy dreams last night, it would be nice if I could release a little tension before work. Are you up for a quickie?"
    menu:
        "Have a Quickie" if not the_person.has_taboo("condomless_sex"):
            mc.name "That sounds pretty nice actually, what did you have in mind?"

        "Feed Her" if the_person.has_cum_fetish:
            #fetish blowjob path
            the_person "Oh! I know! You just keep eating your breakfast, mommy will just help herself!"
            $ scene_manager.update_actor(the_person, position = "blowjob")
            $ the_person.break_taboo("touching_penis")
            "[the_person.possessive_title] quickly gets down on her knees and under the table. You feel her expert hands removing your belt and trousers. She sighs when your cock springs free."
            the_person "Mmm, that's what I was dreaming about... I had a dream that I was blowing you, and you started cumming, and you just kept cumming and cumming and it was everywhere..."
            "She opens her mouth and runs her tongue along your length, breathing in your masculine musk."
            the_person "It was amazing... I want some of the real thing!"
            $ the_person.break_taboo("sucking_cock")
            "She opens her mouth and slides your penis in. She dances circles all around it while she suckles the tip. You look down and notice that she is touching herself."
            $ the_person.change_arousal(20)
            # call fuck_person(the_person, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, girl_in_charge = True, position_locked = True) from _call_fuck_person_workday_breakfast_01
            call get_fucked(the_person, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, allow_continue = False) from _call_get_fucked_fuck_person_workday_breakfast_01
            "Finished with her breakfast, [the_person.title] gets up from the table and excuses herself."
            $ scene_manager.update_actor(the_person, position = "walking_away")
            the_person "Have a good day at work, I'm gonna go get ready for the day!"
            return "Advance Time"

        "Long Day Ahead":
            mc.name "I'm sorry [the_person.title], but I have a long day scheduled today. I think I had better save my energy!"
            $ scene_manager.update_actor(the_person, position = "sitting", emotion="sad")
            $ the_person.change_stats(happiness = -3, obedience = 2)
            the_person "That's okay, I understand. Well don't forget, dinner will be the usual time tonight. Maybe we can do something after that?"
            "You give her a non-committal shrug. The tension at the table is a little much, so you quickly finish your breakfast and head out."
            return None

    $ scene_manager.update_actor(the_person, position = "stand4")
    the_person "Oh! We'd better go quick, your sister could come out at any time..."

    if mc.business.event_triggers_dict.get("family_threesome", False):
        mc.name "Why does it matter if [lily.fname] comes out?"
        the_person "Well, I mean it's not that I mind, but your mommy has needs [the_person.mc_title]..."
        menu:
            "Insist [lily.title] join you" if willing_to_threesome(the_person, lily) and lily.is_available:
                mc.name "Don't worry [the_person.title]. I'll make sure you have your needs met."
                the_person "I suppose that would be okay, just make sure I get to finish!"
                mc.name "Of course!"
                "[the_person.possessive_title] quickly starts to strip down while you knock on [lily.possessive_title]'s door."

                $ scene_manager.strip_full_outfit(person = the_person)
                "After no response, you knock again."
                lily "What!?! I'm tired!"
                mc.name "Me and mom are gonna have some fun, you should join us."
                lily "Huh? Really!?! I'll be right there!"
                "You walk back to the kitchen and [lily.title] quickly joins you."
                $ scene_manager.add_actor(lily, display_transform = character_center)
                if lily.outfit.has_full_access:
                    "Already basically ready to go, [lily.title] looks to you for direction."
                else:
                    "Seeing [the_person.possessive_title] already naked, [lily.title] strips down also."
                    $ scene_manager.strip_full_outfit(person = lily)
                mc.name "Mom is feeling needy this morning sis, why don't we take care of her?"
                lily "Sounds great!"
                call start_threesome(the_person, lily, start_position = Threesome_doggy_deluxe, swapped = True) from _fuck_mom_for_breakfast_1
                $ the_report = _return
                if the_report.get("girl one orgasms", 0) > 0 and the_report.get("girl two orgasms", 0) > 0 and the_report.get("guy orgasms", 0) > 0: #Happy family
                    "The three of you remain together for a while, enjoying your orgasms."
                    $ the_person.change_stats(obedience = 3, happiness = 5)
                    the_person "You two... I get overwhelmed by all the love I feel for you two when we do things like this. I love you both so much!"
                elif the_report.get("girl one orgasms", 0) > 0:
                    "[the_person.possessive_title] recovers for a bit from her orgasm."
                    $ the_person.change_stats(obedience = 2, happiness = 3)
                    the_person "Thank you, [the_person.mc_title], for insisting on bringing your sister out. You were right, that felt so good."
                    lily "What? Mooooom! You were gonna fuck around without me?"
                "You get up and excuse yourself. Time to start the day!"
                return "Advance Time"

            "Relent":
                mc.name "Ok... but I'm not going to keep it down just because she is home."
                the_person "Okay dear."

    if the_person.outfit.can_half_off_to_vagina():
        "[the_person.possessive_title] quickly moves some clothing out of the way."
        $ scene_manager.strip_actor_strip_list(the_person, the_person.outfit.get_half_off_to_vagina_list(), half_off_instead = True)
    else: #We need to strip something off completely.
        "[the_person.possessive_title] quickly starts to strip down."
        $ scene_manager.strip_to_vagina(person = the_person)

    "You take a quick sip of coffee. [the_person.possessive_title] is ready to fuck you right here in the kitchen!"
    if the_person.has_anal_fetish:
        "She opens one of the drawers and pulls out a bottle of lube..."
        mc.name "You keep lube in the kitchen?"
        the_person "Hush, you never know when you might have need of something like that, especially with all the urges I've been having lately..."
        "You watch as she applies a generous amount to her hand, then she reaches back and starts applying it to her back end."
        the_person "Remember, this is a quickie! Sit back and enjoy, but don't hold back! I want your cum!"
        "[the_person.possessive_title] unzips your pants and pulls out your firm cock. She sits down on your lap, facing you."
        $ scene_manager.update_actor(the_person, position = "cowgirl")
        "With one hand on your cock, she guides you to her tight anal pucker. In one smooth motion, she relaxes herself and lowers her body down on to you, impaling herself on your manhood."
        the_person "OH fuck, that is just what I needed... I was dreaming about this last night... I dreamed that you had me tied up and bent over and you pounded my ass over and over..."
        "She is whispering in your ear. [the_person.title] is truly desperate to have her ass stuffed with your cock."
        the_person "I remember you saying you were gonna cum... and I was so ready for it, I was begging you for it... and then suddenly I woke up!"
        "[the_person.possessive_title]'s hips are moving in wide circles. Her bowel feels amazing, like a buttery vice."
        the_person "I just need to feel it. To feel you cum inside my ass, to blow so deep and fill me up."
        "Her voice and her movements are desperate. You suddenly realize that she is racing you to the finish, and you aren't sure who is going to finish first."
        the_person "I need it [the_person.mc_title]! I want to feel you slowly oozing out of me as I walk around at work today. Then when I get home I want you to spank me and fuck my ass over the counter while I cook dinner!"
        "Your balls are beginning to tense, you are seconds away from ejaculating!"
        the_person "Claim my asshole! Mark your territory with your cum! Then spank me and do it again and again!"
        $ play_moan_sound()
        "You climax in a frenzy. She arches her back and moans involuntarily when she feels your cum flood her rectum. Her orgasm hits immediately after yours."
        $ the_person.have_orgasm()
        "Finally speechless, [the_person.title]'s body stops rocking, but you feel the twitching of her sphincter as orgasmic waves hit her. You sigh happily, dumping the last of your cum inside her."

        $ the_person.cum_in_ass()
        $ scene_manager.update_actor(the_person) # redraw for cum
        $ ClimaxController.manual_clarity_release(climax_type = "anal", the_person = the_person)

        "As her orgasm subsides, [the_person.possessive_title] suddenly returns to her senses."
        the_person "Oh god... [lily.fname] could walk out any second!"
        $ scene_manager.update_actor(the_person, position = "walking_away")
        "[the_person.title] quickly gets up and hurries away. She calls back before she gets to her room."
        the_person "I love you, have a good day at work!"
        $ scene_manager.remove_actor(the_person)
        "You put your cock away and finish your breakfast before heading out for the day."
        return "Advance Time"

    the_person "Remember, this is a quickie! Sit back and enjoy, but don't hold back! I want your cum!"
    "[the_person.possessive_title] unzips your pants and pulls out your firm cock. She sits down on your lap, facing you."
    $ scene_manager.update_actor(the_person, position = "cowgirl")
    "With one hand on your cock, she guides you straight to her cunt. In one smooth motion, she relaxes herself and lowers her body down on to you, impaling herself on your manhood."
    the_person "OH fuck, that is just what I needed... I was dreaming about this last night..."
    "She is whispering in your ear. [the_person.title] is really turned on right now."
    the_person "I remember you saying you were gonna cum... and I was so ready for it, I was begging you for it... and then suddenly I woke up!"
    "[the_person.possessive_title]'s hips are moving in wide circles. Her sopping wet cunt feels amazing surrounding your penis."
    the_person "I want to feel it. Not just when you cum now... but when I'm at work, I want to feel you slowly leak out of me..."
    "Her voice and her movements are desperate. You suddenly realize that she is racing you to the finish, and you aren't sure who is going to finish first."
    the_person "I need it [the_person.mc_title]! I want every drip to be a reminder of how good you make me feel!"
    "Your balls are beginning to tense, you are seconds away from ejaculating! She begins to make a short, fast humping motion, grinding her clit against your stomach."
    the_person "Claim mommy! Mark your territory with your cum! Fill me up!"
    $ play_moan_sound()
    "You climax in a frenzy. She arches her back and moans involuntarily when she feels your cum flood her womb. Her orgasm hits immediately after yours."
    $ the_person.have_orgasm()
    "Finally speechless, [the_person.title]'s body stops rocking, but you feel the twitching of her pussy as orgasmic waves hit her. You sigh happily, dumping the last of your cum inside her."

    $ the_person.cum_in_vagina()
    $ scene_manager.update_actor(the_person) # redraw for cum
    $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)

    "As her orgasm subsides, [the_person.possessive_title] suddenly returns to her senses."
    the_person "Oh god... [lily.fname] could walk out any second!"
    $ the_person.apply_planned_outfit()
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "She quickly gets up and puts her clothes back on, leaning close to your ear."
    if the_person.wearing_panties:
        the_person "Hmmm, I'm going to feel your cum dripping into my panties all day."
    else:
        the_person "Hmmm, I'm going drip cum all day long, staining my clothes."

    $ scene_manager.update_actor(the_person, position = "walking_away")
    "[the_person.title] turns around and hurries away. She calls back before she gets to her room."
    $ scene_manager.update_actor(the_person, position = "back_peek")
    the_person "I love you, have a good day at work!"
    $ scene_manager.clear_scene()
    "You put your cock away and finish your breakfast before heading out for the day."
    return "Advance Time"

label mom_commando_day_selfie_label():
    $ the_person = mom
    $ mc.start_text_convo(the_person)
    if persistent.show_ntr:
        $ the_person.strip_outfit(delay = 0, exclude_upper = True)
        $ the_person.cum_on_ass()
        the_person "Hey, you were right! Going commando really paid off. I was making copies and when I bent over to pick them up from the tray, one of my colleagues noticed..."
        the_person "We snuck off to a janitor closet... he just barely pulled out in time!"
        $ the_person.draw_person(position = SB_get_random_ass_position())
        "She sends you a selfie of her ass covered in cum. You quickly text her back."
        mc.name "Nice! You should leave it right there and walk around the office like that!"
        the_person "You bad boy ;)"
    else:
        $ removed_something = the_person.strip_outfit_to_max_sluttiness(delay = 0, temp_sluttiness_boost = 20)
        the_person "Hey [the_person.mc_title], you were right. Going commando really paid off."
        the_person "At lunch I did a full Basic Instinct move on some colleagues sitting across from me at another table, they just couldn't stop ogling me. It turned me on so much..."
        $ the_person.draw_person(position = "sitting")
        "She sends you a selfie from a bathroom stall."
        the_person "As a thank you for your suggestion."
        if removed_something:
            mc.name "Nice! You should walk around the office like that!"
            "A moment later."
            the_person "Don't tempt me! See you at home tonight!"
        else:
            mc.name "Nice, I knew you would like it!"
            "A moment later."
            the_person "You know me too well! See you at home tonight!"

    $ mc.end_text_convo()
    "You smile and resume your day."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    return

label mom_breakfast_action_mom_and_lily_label():
    $ ran_num = renpy.random.randint(0, 1)
    if ran_num == 1:
        "As you walk into the kitchen, you see your sister and your mom eating each other out on the breakfast table."
        $ the_person.strip_outfit(delay = 0)
        $ lily.strip_outfit(delay = 0)
        $ scene_manager.add_actor(the_person, position = "missionary", display_transform = character_69_bottom)
        $ scene_manager.add_actor(lily, position = "cowgirl", display_transform = character_69_on_top)

        the_person "Oh yes baby, keep licking me right there, that feels wonderful."
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(20)
        lily "Mmm, mom, you taste great... oh yes, push some fingers in there... ah, yes, right there..."
        $ lily.change_arousal(20)

        "While watching them going at it, you decide what to do next."
        menu:
            "Join them":
                lily "Hi [lily.mc_title], why don't you join us."
                mc.name "Wait a second [the_person.title], let me take care of that for you."
                "You quickly undress and..."
                call start_threesome(the_person, lily, start_position = Threesome_sixty_nine, start_object = make_table(), position_locked = True, skip_intro = True) from _call_start_threesome_mom_breakfast_action_mom_and_lily_label_1
                "Once you're finished you pick up your clothes and say goodbye to the girls, who seem determined to continue for a while."
                $ mc.change_location(hall)
                return "Advance Time"
            "Walk away":
                return None
    else:
        "As you walk into the kitchen, you see your sister on her knees eating out your mom."
        $ the_person.strip_outfit(delay = 0)
        $ lily.strip_outfit(delay = 0)
        $ scene_manager.add_actor(the_person, position = "missionary", display_transform = Threesome_doggy_deluxe_girl_one_transform)
        $ scene_manager.add_actor(lily, position = "doggy", display_transform = Threesome_doggy_deluxe_girl_two_transform)

        $ mc.change_locked_clarity(20)
        the_person "Oh yes baby, keep licking me right there, that feels wonderful."
        $ the_person.change_arousal(20)
        "While licking your mom, your sister is furiously rubbing her pussy."
        $ lily.change_arousal(20)
        "While watching them going at it, you decide what to do next."
        menu:
            "Join them":
                the_person "Hello [the_person.mc_title], why don't you join us."
                mc.name "Wait a second [lily.title], let me take care of that for you."
                "You quickly undress and..."
                call start_threesome(the_person, lily, start_position = Threesome_doggy_deluxe, start_object = make_floor(), position_locked = True, skip_intro = True) from _call_start_threesome_mom_breakfast_action_mom_and_lily_label_2
                "Once you're finished you pick up your clothes and say goodbye to the girls, who seem determined to continue for a while."
                $ mc.change_location(hall)
                return "Advance Time"
            "Walk away":
                return None
    return
