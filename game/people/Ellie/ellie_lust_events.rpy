#Sluttiness EVents
#Converting Ellie's sluttiness events to taboo break style events.
#Each time an act is performed, she becomes more convinced that it is okay.
#

init 2 python:
    def ellie_grope_taboo_restore_requirement():
        if mc.is_at_work and ellie.is_at_work and ellie.has_broken_taboo(["touching_body"]):
            return True
        return False

    def ellie_work_grope_requirement(person):
        if mc.is_at_work and ellie.is_at_work and ellie.arousal_perc >= 20: #MC can tell that she is aroused from working on nanobots and sexual research.
            return True
        return False

    def ellie_text_message_apology_requirement():
        return day%7 == 6

    def ellie_never_been_kissed_requirement(the_person):
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        if ellie_is_working_on_nanobots() or ellie.sluttiness >= 20:
            return mc.business.days_since_event("hired_ellie_IT") >= TIER_2_TIME_DELAY
        return False

    def ellie_never_tasted_cock_requirement(the_person):
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        if the_person.sluttiness >= 40 and ellie.story_event_ready("slut"):
            if get_random_employees(1, exclude_list = [the_person], slut_required = 50):
                return True
        return False

    def ellie_oral_taboo_restore_requirement():
        if mc.is_at_work and ellie.is_at_work and ellie.has_broken_taboo(["sucking_cock"]):
            return True
        return False

    def ellie_work_blowjob_requirement(person):
        return False

    def ellie_never_been_fucked_requirement(the_person):
        if not (mc.business.is_open_for_business and mc.is_at_work):
            return False

        return the_person.sluttiness >= 60 and ellie.story_event_ready("slut")

    def ellie_vaginal_taboo_restore_requirement():
        if mc.is_at_work and ellie.is_at_work and ellie.has_broken_taboo(["vaginal_sex"]) and ellie.progress.lust_step == 1:
            return True
        return False

    def ellie_work_fuck_requirement(person):
        return False

    def ellie_never_tried_anal_requirement(the_person):
        return False

    def ellie_anal_taboo_restore_requirement():
        if mc.is_at_work and ellie.is_at_work and ellie.has_broken_taboo(["anal_sex"]):
            return True
        return False
    def ellie_work_anal_requirement(person):
        return False

    def ellie_turned_on_while_working_intro_requirement(the_person):
        return False

    def ellie_turned_on_while_working_requirement():
        return False

    ellie_oral_taboo_restore = Action("Ellie Oral Taboo", ellie_oral_taboo_restore_requirement, "ellie_oral_taboo_restore_label")
    ellie_never_been_fucked = Action("Ellie wants to fuck", ellie_never_been_fucked_requirement, "ellie_never_been_fucked_label")
    ellie_vaginal_taboo_restore = Action("Ellie vaginal taboo", ellie_vaginal_taboo_restore_requirement, "ellie_vaginal_taboo_restore_label")
    ellie_never_tried_anal = Action("Ellie tries anal", ellie_never_tried_anal_requirement, "ellie_never_tried_anal_label")
    ellie_anal_taboo_restore = Action("Ellie Anal Taboo", ellie_anal_taboo_restore_requirement, "ellie_anal_taboo_restore_label")

    ellie_turned_on_while_working_intro = Action("Ellie gets horny", ellie_turned_on_while_working_intro_requirement, "ellie_turned_on_while_working_intro_label")

    ellie_work_grope = Action("Sluttiness: Grope Her", ellie_work_grope_requirement, "ellie_work_grope_label")
    ellie_work_blowjob = Action("Sluttiness: Blowjob", ellie_work_blowjob_requirement, "ellie_work_blowjob_label")
    ellie_work_fuck = Action("Sluttiness: Fuck Her", ellie_work_fuck_requirement, "ellie_work_fuck_label")
    ellie_work_anal = Action("Sluttiness: Fuck Her Ass", ellie_work_anal_requirement, "ellie_work_anal_label")
    ellie_lust_role = Role(role_name ="Ellie Slut", actions =[ellie_work_grope, ellie_work_blowjob, ellie_work_fuck, ellie_work_anal], hidden = True)

    def add_ellie_grope_taboo_restore_action():
        ellie_grope_taboo_restore = Action("Ellie confronts you", ellie_grope_taboo_restore_requirement, "ellie_grope_taboo_restore_label")
        mc.business.add_mandatory_crisis(ellie_grope_taboo_restore)

        ellie.add_role(ellie_lust_role)
        return

    def add_ellie_text_message_apology_action():
        ellie_text_message_apology = Action("Ellie texts you", ellie_text_message_apology_requirement, "ellie_text_message_apology_label")
        mc.business.add_mandatory_morning_crisis(ellie_text_message_apology)
        ellie.remove_role(ellie_lust_role)
        ellie.progress.lust_step = 2
        return

    def add_ellie_never_been_kissed_action():
        ellie_never_been_kissed = Action("Ellie Gets Kissed", ellie_never_been_kissed_requirement, "ellie_never_been_kissed_label")
        ellie.add_unique_on_room_enter_event(ellie_never_been_kissed)
        return

    def add_ellie_never_tasted_cock_action():
        ellie_never_tasted_cock = Action("Ellie wants to taste", ellie_never_tasted_cock_requirement, "ellie_never_tasted_cock_label")
        ellie.add_unique_on_room_enter_event(ellie_never_tasted_cock)
        ellie.story_event_log("slut")
        return

label ellie_never_been_kissed_label(the_person):  #This is Ellies 20 sluttiness event. Also kick starts all other events
    "You step into your research division. It seems that progress is going well here. To one side you see [the_person.possessive_title], working on a nanobot project."
    $ the_person.draw_person(position = "sitting")
    $ the_person.arousal = 40
    $ mc.reset_arousal()
    $ ellie.story_event_log("slut")
    $ ellie.progress.lust_step = 1

    "As you approach her, you notice she seems to be breathing heavily and her cheeks are flushed."
    "One of the things that you have noticed about [the_person.possessive_title] is that she seems to get really hot and bothered, working in the research department."
    "Working on your nanobot programs and other sexual related serums must be really getting to her. You wonder if she could use some relief."
    mc.name "Hey [the_person.title], are you okay?"
    "You startle her and she jumps up."
    $ the_person.draw_person(position = the_person.idle_pose)
    the_person "[the_person.mc_title]! I was just... you know... working on the nanobot program..."
    mc.name "Great! How's it going?"
    the_person "How's what going?"
    mc.name "... The program..."
    the_person "ah... OH. Right. Well, it's going I guess."
    mc.name "Are you feeling okay? If you are sick and need to go home that would be quite alright."
    the_person "I'm fine, I'm just... y'know... trying to figure out the details of this darned thing."
    "She leans towards you and lowers her voice."
    the_person "I just don't understand why you all got to use them bots for making women do that, you know, fornicating."
    the_person "A woman should be keeping to herself, like she's supposed to."
    the_person "'sides, not like sex is such an amazing thing anyway."
    mc.name "Well, it isn't so much making women do something, as lowering inhibitions and giving women the chance to experience what they already want, but are afraid to experience."
    "[the_person.title] scoffs a bit at your rebuttal."
    mc.name "And as for sex not being amazing, I'd have say you probably just haven't had a competent partner yet."
    "[the_person.possessive_title] rolls her eyes."
    the_person "I don't need no partner ta know that."
    "You take a moment to evaluate your conversation with [the_person.title]."
    "From the way she is talking, the way she brushes it off, is it possible she is still a virgin?"
    "You know she grew up in religious territory..."
    mc.name "Well, I'd say you should keep an open mind. I'm pretty competent, if you ever want to put it to the test."
    $ the_person.change_arousal(10) #50
    the_person "Ha! That's something, bless your heart. I'm saving myself fer marriage, like I'd like you do something like that..."
    "Aha. You wonder if she's even done anything with someone before?"
    mc.name "There are numerous other things other than going all the way that could be done as an alternative."
    "As you look at her, you realize why she is acting funny. She's aroused! Probably from working on the nanobot code..."
    "You give her a wide, genuine smile."
    mc.name "Like I said, I'd be glad to show you. You wouldn't even have to take off any clothes."
    the_person "Hah, you're such a joker. Like I'd let you... run your hands all over me... or whatever..."
    $ the_person.change_arousal(10) #60
    $ the_person.draw_person(position = "sitting")
    "[the_person.possessive_title] sits back down at her desk, and you decide to let her keep working, but you can tell you've struck a nerve with her."
    $ clear_scene()
    "You decide to leave her alone for now. You finish inspecting the research department then head to your office."
    $ mc.change_location(ceo_office)
    "You sit down and start to work on some paperwork. You pull up some emails and get to work responding to some supply requests from logistics."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    "You look up. [the_person.title] is standing in your door."
    the_person "Hey uh, [the_person.mc_title]..."
    mc.name "Come in, close the door, and have a seat."
    the_person "Oh uh, sure..."
    "[the_person.title] does what you ask, then sits down across from you."
    $ the_person.draw_person(position = "sitting")
    mc.name "What can I do for you?"
    the_person "Well, I was working on that bot program, but I was kinda having trouble with parts of it..."
    mc.name "What kind of trouble?"
    the_person "It was a part about making some uh, things, a bit more sensitive, for ladies I mean..."
    the_person "And I kinda realized, you know that like... for the sake of being able to code it properly, I should probably have a better idea of... you know... what it feels like..."
    "Wow, she must be have been more ready for this than you realized. You thought it would be much more difficult to seduce her!"
    mc.name "Of course, and as your boss, it only makes sense that I would want to provide you with experiences that will make you better at your job."
    the_person "Exactly! Now... you said you could show me something that... that wouldn't involve me taking off clothes or something..."
    the_person "Just to make sure we are on the same page here, NOTHING goes inside of me... right?"
    mc.name "Not if you don't want something to."
    the_person "Well, I don't. I'm no whore! Working on this program just has me curious and distracted..."
    mc.name "It's okay. It's called getting aroused, and it is perfectly natural for this to happen in response to being exposed to sexual situations."
    the_person "I... I don't think I can talk about this stuff!"
    mc.name "It's okay. Tell you what, I'm going to talk to you through everything I'm doing, you don't have to say a word. If I start doing something you don't like, just stop me."
    the_person "Okay..."
    mc.name "Stand up."
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title] does so obediently. You need to be careful not to push things too far, but this could be the beginning of a very interesting relationship between you two."
    "You walk over to her. You open up your arms and pull her close to you."
    $ the_person.draw_person(position = "kissing")
    "You pull her body close to yours. You rub your hands along her back for a while, feeling her chest slowly rise and fall with deep breaths against yours."
    "You slowly start to lower your hands down her back. You feel her tense up a bit."
    mc.name "I'm going to move my hands lower. It's okay, it felt good when I rubbed your back, right?"
    "She relaxes a bit and nods quietly. She is still tense but doesn't move as you lower your hands down to her ass."
    "You slowly start to knead her curvy cheeks. They are supple and soft and feel amazing in your hands."
    $ play_moan_sound()
    the_person "Mmm..."
    $ the_person.change_arousal(5) #65
    $ mc.change_locked_clarity(20)
    "[the_person.title] lets out a little moan. She slowly relaxes further as you continue to rub and caress her rear."
    mc.name "See? Rubbing your back feels good, and rubbing down here feels a little bit better, doesn't it?"
    the_person "It does..."
    "She leans forward and relaxes more, just enjoying the touch of your hands on her body. You really need to take this slow, so you take your time rubbing for several minutes."
    "However, you won't be able to make her cum just from this. Eventually it is time to move on."
    mc.name "Alright, now I'm going to need you to turn around, so I can keep making you feel good."
    "[the_person.possessive_title] just nods. She doesn't say a word but turns around for you."
    $ the_person.draw_person(position = "walking_away")
    "You run your hands along her hips, to her front and along her belly. You get close to her so her body is right up against yours."
    mc.name "Okay, next, I'm going to touch your chest, okay?"
    the_person "You're not... gonna put our hand up my shirt... right?"
    mc.name "Not unless you want me to. It'll be just like I'm rubbing your back, but it'll feel even better, I promise."
    "[the_person.title] doesn't respond, but just waits. You know you are pushing boundaries here, so you proceed carefully."
    "You let both hands creep up her belly until they reach the bottom of her rib cage. You slide them up a bit more until you are cupping the bottom of her tits."
    $ play_moan_sound()
    the_person "Ahhhhh..."
    $ the_person.change_arousal(5) #70
    $ mc.change_locked_clarity(20)
    "You start to grope and massage her tits earnestly now, being careful to avoid her sensitive nipples. Her breathing is getting heavier and an occasional moan escapes her lips."
    mc.name "It's nice, isn't it? Doesn't it make you feel good?"
    the_person "Yeah... It's good... but weird too. It's making me all warm... down there..."
    mc.name "That is arousal building up. We want to build that up as much as we can, and it will make you feel amazing when it releases."
    the_person "I... I dunno about that, but keep doing what you're doing... it's nice..."
    "The weight of her heavy tits feels great in your hands. You really wish you could touch her flesh there, but for now you need to take things one step at a time."
    "When you feel her arousal start to plateau, you make your next move. With two fingers and a thumb, you start to knead her engorged nipples."
    $ the_person.change_arousal(10) #80
    $ play_moan_sound()
    the_person "Ah!"
    "[the_person.possessive_title] cries out and for a second her knees buckle. She catches herself, but when she straightens out, her body rubs up against yours."
    "You've been rock hard throughout this whole process, but when she straightens up her ass rubs up against you, causing you to moan."
    $ mc.change_locked_clarity(30)
    "Her body goes rigid."
    the_person "Ah! Was that... your... your thing!?!"
    mc.name "Yes, that is my penis."
    the_person "Don't you dare try and put that thing in me!"
    mc.name "Shhh, don't worry. I'm not even going to get it out of my pants. I'm just aroused too. It's okay."
    the_person "Ahh... okay..."
    "You go back to groping [the_person.possessive_title]'s big tits. You take turns kneading them and pinching her nipples."
    "[the_person.title] is starting to whimper. The poor girl is so pent up, the time to finish her off is now."
    mc.name "Okay... I'm going to touch you between your legs now. I'm not going to put my hand under any of your clothing. Is that okay?"
    "She whimpers a response, but before you touch her you want to make sure she really consents."
    mc.name "[the_person.title]? I don't want to do something you don't want me to. Do you want me to touch you the way I described?"
    the_person "Yes please... Please touch me... [the_person.mc_title]..."
    $ the_person.change_obedience(10)
    $ play_moan_sound()
    "Ahhh, she even said please! It seems she is so aroused, her resistance is breaking down."
    "Your left hand still on her tits, you move your right hand down her body and between her legs."
    "When you start to apply pressure on her cunt through her clothes, she starts to melt. Her hips move a bit on their own."
    $ the_person.change_arousal(10) #90
    $ mc.change_locked_clarity(50)
    the_person "Oh Lordie... forgive me..."
    "[the_person.title]'s hip movements have her ass rubbing up against you now. You can't help but moan a bit at the contact with the red-haired belle."
    the_person "Yer thing... it's poking me..."
    mc.name "Do you want me to stop?"
    the_person "NO! No... it's kinda nice."
    mc.name "You can move your hips a bit. It will help you control the pace to something that feels good to you, and it'll feel nice for me too."
    the_person "... okay..."
    "Instinctually, [the_person.possessive_title] starts to move her hips forward and backwards a bit, helping set a pace that feels best for her."
    $ mc.change_locked_clarity(50)
    $ the_person.break_taboo("touching_body")
    "You can't help pushing your hips a bit up against her as well. It feels nice to have her ass against your cock."
    "You wish you just rip off the clothes between you and her and bend her over your desk, but you know she isn't ready for that yet."
    $ play_moan_sound()
    "Her moaning is getting stronger and needy. She's going to cum soon."
    the_person "[the_person.mc_title]! Something is happening... I can't... I can't stop!"
    "You pinch her nipple forcefully with one hand and grab her by the pussy with the other. She cries out as she starts to cum."
    $ the_person.have_orgasm()
    the_person "AH! OH!"
    $ the_person.change_slut(3, 40)
    "Her body starts to collapse so you quickly grab her with your left hand, your right hand still rubbing her pussy through her orgasm."
    "Your hand quickly starts to get damp as she cums. She sure seems to be having a juicy orgasm."
    $ the_person.draw_person(position = the_person.idle_pose)
    "As soon as she regains control of her legs, [the_person.possessive_title] pulls away from you and turns."
    the_person "Oh heavens I just... no way... I couldn't have..."
    "She quickly puts a hand down her pants and then pulls it back out. It is shining wet. Did she just... squirt?"
    mc.name "That was just..."
    the_person "OH MY LORDIE I JUST PEED... oh my I'm so sorry, I have to go!!!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] quickly turns and flees your office, flinging your door open and running away."
    $ clear_scene()
    "You aren't certain... but you think you might have just brought her to her very first orgasm, ever."
    "It has left you extremely aroused, and you are sure she is probably very confused."
    "Is she a squirter? You can't say you have much experience with girls who tend to do that. If that was her first orgasm ever, maybe she was just really pent up."
    "A sexually repressed redhead that squirts. How do you feel about that?"
    "WARNING: The next menu will change future dialogue with [the_person.title]!"
    menu:
        "Squirting is hot!":
            $ ellie.event_triggers_dict["squirts"] = True
        "Squirting is gross!":
            $ ellie.event_triggers_dict["squirts"] = False

    "You'll want to speak with her soon though, about what just happened."
    $ add_ellie_grope_taboo_restore_action()
    $ the_person.event_triggers_dict["been_fingered"] = True

    "Your encounter has left you crazy horny."
    if mc.business.head_researcher.sluttiness > 60:
        $ the_person = mc.business.head_researcher
    elif mc.business.hr_director.sluttiness > 60:
        $ the_person = mc.business.hr_director
    else:
        "Unfortunately there isn't much you can do about it now. You spend a few minutes walking around your office until your boner finally goes down, then return to work."
        $ clear_scene()
        return
    "You decide to call [the_person.possessive_title] to your office to take care of it."
    "*KNOCK KNOCK*"
    $ the_person.draw_person()
    the_person "Hey [the_person.mc_title], you wanted to see me?"
    "When you turn to face them, they start to laugh."
    the_person "Jesus, you look like you just left a porn convention with your hands tied behind your back. Are you okay?"
    mc.name "I will be in a few minutes, hopefully."
    the_person "Ahhh, you need me to take care of that monster for you?"
    the_person "Okay!"

    if the_person.has_cum_fetish:
        "[the_person.title] closes your office door and locks it. Then she walks over to you and drops down to her knees."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(50)
        "In a flash she has your cock out."
        call fuck_person(the_person, private=True, start_position = cum_fetish_blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, self_strip = False) from _call_ellie_arousal_relief_01
    elif the_person.has_anal_fetish:
        "[the_person.title] closes your office door and locks it. Then she walks over to your desk, and bends over it."
        the_person "It's been a while since you had it in my ass... why don't you just take me for a quickie?"
        "You step behind her."
        $ mc.change_locked_clarity(50)
        call fuck_person(the_person, private=True, start_position = anal_standing, start_object = make_desk()) from _call_ellie_arousal_relief_02
    elif the_person.has_breeding_fetish:
        "[the_person.title] closes your office door and locks it. Then she walks over to your desk, and bends over it."
        the_person "My hungry cunt could really use a fresh load of seed... why don't we have a quickie?"
        "You step behind her."
        $ mc.change_locked_clarity(50)
        call fuck_person(the_person, private=True, start_position = bent_over_breeding, start_object = make_desk()) from _call_ellie_arousal_relief_03
    else:
        "[the_person.title] closes your office door and locks it. Then she walks over to you and drops down to her knees."
        $ the_person.draw_person(position = "blowjob")
        $ mc.change_locked_clarity(50)
        "She fumbles with your pants a bit, but eventually managed to pull your cock out."
        "She gives it a couple licks before she gets started."
        call fuck_person(the_person, private=True, start_position = blowjob, start_object = make_floor(), skip_intro = True, position_locked = True, self_strip = False) from _call_ellie_arousal_relief_04

    $ report_log = _return
    if report_log.get("guy orgasms", 0) > 0:
        "After you finish, you feel much better."
        mc.name "Thank you [the_person.title], I really needed that."
        the_person "Glad to help!"
        $ the_person.change_stats(happiness = 10, love = 5, obedience = 10)
    $ the_person.draw_person()
    $ the_person.review_outfit()
    "She smiles at you while putting her clothes back in order."
    mc.name "Alright, now get back to work."
    $ the_person.draw_person(position = "walking_away")
    the_person "Of course, [the_person.mc_title]."
    $ clear_scene()
    "After you get yourself cleaned up, you get back to work."
    return

label ellie_grope_taboo_restore_label():
    $ the_person = ellie
    $ first_time = the_person.event_triggers_dict.get("lust_grope_count", 0) == 0
    $ ellie.event_triggers_dict["lust_grope_count"] = ellie.event_triggers_dict.get("lust_grope_count", 0) + 1
    $ outcome_convince = False
    $ ellie.restore_taboo("touching_body", add_to_log = False)
    $ ellie.change_slut(-10)
    "You are going about your work, when [the_person.possessive_title] finds you."
    $ the_person.draw_person(emotion = "angry")
    if mc.location != ceo_office:
        the_person "Hey, can we talk somewhere private?"
        mc.name "Sure."
        $ mc.change_location(ceo_office)
        "You take her to your office and close the door. You offer to let her sit down but she declines."
        the_person "I'll keep this short, I just didn't want any other girls to hear this..."
    if first_time:
        the_person "You need to keep your hands to yourself! It isn't proper for a man to touch a woman like that before marriage!"
        mc.name "If I remember correctly, you came to my office?"
        the_person "Yeah well... I was in a moment of weakness. It ain't right for a man to take advantage like that!"
    else:
        the_person "You did it... again! Mister, you need to be keeping your hands to yourself now!"
        mc.name "But you enjoyed it... right?"
        the_person "That's... that's not the point!"
    the_person "So I need you to kindly keep your hands to yourself from now on, okay?"
    the_person "I'm not some harlot for you to feel up at any point you wish! Especially at work of all places!"

    $ attempts = 3 - the_person.event_triggers_dict.get("lust_grope_count", 0)

    menu:
        "I just want to make you feel good too" if ellie.progress.love_step >= 2:
            mc.name "Why do you get to touch me, but I can't touch you?"
            mc.name "It feels so good when you do that for me, isn't it only fair that you let me repay the favor?"
            the_person "I... but at... at work?"
            mc.name "Why not? We can be discrete."
            "She sighs, thinking. Eventually she relents."
            the_person "I... I guess so."
            $ outcome_convince = True

        "I just want to make you feel good too\n{color=#ff0000}{size=18}Requires: Love Story Progress{/size}{/color} (disabled)" if ellie.progress.love_step < 2:
            pass

        "But it keeps happening..." if ellie.event_triggers_dict.get("lust_grope_count", 0) >= 3:
            mc.name "If it needs to stop, why does it keep happening [the_person.title]?"
            mc.name "Feeling you squirm and melt while I touch you... I love doing it, and you love feeling it, don't you?"
            "[the_person.possessive_title] seems like she wants to argue, but she starts to relent."
            the_person "I... guess maybe... just once in a while!."
            "She thinks a moment more."
            the_person "But don't be getting any more silly ideas! I'm not some office whore!"
            $ outcome_convince = True

        "But it keeps happening...\n{color=#ff0000}{size=18}Requires: [attempts] more gropings{/size}{/color} (disabled)" if ellie.event_triggers_dict.get("lust_grope_count", 0) < 3:
            pass

        "Understood" if ellie.event_triggers_dict.get("lust_grope_count", 0) <= 3:
            mc.name "I understand. You have boundaries and I won't cross them again without approval."
            "She looks at you suspiciously, but ultimately accepts your proposal.."
            the_person "Alright. Let's just not have this talk again, okay?"

    if outcome_convince:
        the_person "You know... it is so confusing though... like... why do I gotta keep peeing my pants like that?"
        mc.name "[the_person.title]... I don't think you peed yourself, I think you just had an orgasm."
        the_person "I had a... a what now?"
        mc.name "[the_person.title], have you ever masturbated?"
        the_person "What the hecking kind of question is that? Of course not, that's for unsavory folk."
        $ the_person.draw_person(emotion = "sad")
        "You sigh. She is struggling in her brain to overcome her sexual desires, and being exposed to your serums is starting to overwhelm her."
        "She is making progress, but you can tell it is going to be a long road before you can fully corrupt her."
        mc.name "I tell you what. I'm going to email you some sexual health websites. I want you to do some research on things this weekend."
        mc.name "With the work we do here on serums, it is important that you have a good understanding what is actually going on with your body."
        the_person "You're saying... this is a work assignment?"
        mc.name "That's right. It will help you do your job better."
        mc.name "I'm not saying you have to masturbate, but getting to know your body better might help you better understand what we are trying to achieve here, in general."
        the_person "Okay, I'll take a look."
        $ clear_scene()
        "[the_person.possessive_title] leaves your office. You take a few minutes and email her some links to positive sex health websites and information."
        $ add_ellie_text_message_apology_action()
        $ ellie.progress.lust_step = 2
    else:
        $ the_person.draw_person(position = "walking_away")
        $ add_ellie_grope_taboo_restore_action()
        "You thought that [the_person.title] was ready for the next step, but it seems you still have more work to do."
        "You should keep an eye on her though. If you can get her aroused at work and increase her sluttiness, her mental walls might break down for you again."
        #$ ellie.lust_messages[0] = "Use obedience to convince [ashley.fname] to let you use her tits again."
    return

label ellie_work_grope_label(the_person):
    "As you chat with [the_person.title], you feel kind of bad for her. Her cheeks are flushed, and you notice her nipples are stiff."
    "She is getting aroused from working on serum and nanobot research again. Maybe it is time to make another pass at breaking down her sexual walls?"
    "You decide to take her to your office and see if she is ready for some exploration."
    "Due to her arousal distracting her from work, you are pretty sure that you can frame this is a performance evaluation."
    mc.name "[the_person.title], will you come with me to my office? I want to talk to you about your performance."
    the_person "Oh stars... okay."
    "You lead the way to your office. You step inside and lock the door."
    $ mc.change_location(ceo_office)
    mc.name "Go ahead and have a seat."
    $ the_person.draw_person(position = "sitting")
    the_person "I umm, I know my performance hasn't been great... I've just..."
    mc.name "You've been distracted. It is obvious, [the_person.title], that you are trying to work while distracted."
    the_person "I'm just not used to this environment."
    mc.name "You're so tense. You need to do something to help you blow off some steam, and let loose a little."
    "She looks at you a bit confused."
    the_person "...[the_person.mc_title]?"
    mc.name "Masturbating. I'm talking about masturbating. The research we are doing here brings a lot of sexual tension. You need to relieve it once in a while."
    $ the_person.change_love(-2)
    the_person "Wha! Why... I would never!"
    "You sigh, making a big show of it."
    mc.name "I know. And that is the problem. So we are just going to have to relieve the tension another way."
    mc.name "Stand up and close your eyes."
    $ the_person.change_arousal(5)
    "She lets an aroused sigh escape, but quietly stands up and closes her eyes."
    $ the_person.draw_person(position = the_person.idle_pose)
    "You stand up also, then quietly walk around behind her."
    $ the_person.draw_person(position = "walking_away")
    "You put your hands on her shoulders, and start to give her a gentle massage. You can feel the tension in her body."
    "You work her shoulders for a few minutes, feeling the tension drain from them as she starts to relax."
    the_person "That... that feels nice."
    mc.name "That's it. Just concentrate on how good it feels and relax."
    "You let your hands work down her back, focusing on the spine. When you reach the top of her ass, you stop and work your way back up."
    "This time, when you work your way back down, when you get close to her ass, you can feel her weight shift a bit, pushing back towards you a bit."
    "You let your hands run down her ass this time. She tightens up for a moment, but you quietly scold her."
    mc.name "Just relax. Focus on the feelings."
    the_person "Ah... that DOES feel good..."
    $ the_person.change_arousal(20)
    "You spend some time just groping her wonderful back side, then slowly slide your hands up and around her front, onto her stomach."
    "You step forward a bit now, pressing your body against hers."
    the_person "Oh stars... I don't know... I..."
    "You quietly shush her, sliding both hands up and onto her tits. Her protest stops and she lets out a loud moan."
    the_person "Oh! Oh my."
    "Her body immediately responds, pushing herself back against you as you start to grope her incredible tits."
    $ the_person.change_arousal(20)
    $ the_person.break_taboo("touching_body")
    $ mc.change_arousal(10)
    if the_person.has_large_tits:
        "[the_person.possessive_title]'s big tits feel soft and hot in your hands. It is a shame she isn't quite ready to put them to proper use yet."
        "You can't wait until you can convince her to wrap them around your cock."
    "Due to her previous arousal, [the_person.title]'s moaning builds quickly."
    if the_person.tits_visible:
        "[the_person.possessive_title] is melting in your hands as pinch and caress her nipples."
    else:
        "You move your hands down and start to push them up under her clothing."
        if ellie.event_triggers_dict.get("lust_grope_count", 0) >= 2:
            "[the_person.possessive_title] stops you, then surprises you as she pulls her clothing out of the way."
            $ the_person.strip_to_tits(prefer_half_off = True)
            "Finally getting your hands on her bare tits is amazing. She is melting as you pinch and caress her exposed nipples."
        else:
            "[the_person.possessive_title] stops you."
            the_person "On top of clothes... okay?"
            "You nod your acceptance, then continue to enjoy feeling her up."
    $ the_person.change_arousal(20)
    "[the_person.title] is really getting into it, so you slowly let one hand drop from her chest, down between her legs."
    "You are expecting resistance, but she is so turned on she just moans as you reach between her legs."
    if ellie.vagina_available:
        "You rub up and down her exposed slit, carefully stimulating her clit with pushing you fingers inside of her."
    else:
        "You grab her pussy and roughly put circling pressure around her clit."
    $ the_person.change_arousal(40)
    the_person "That's!.. Oh my... STARS! [the_person.mc_title] that is so good!"
    mc.name "That's it. Just let go of all that tension and let it drain out of you."
    "Suddenly, [the_person.possessive_title] siezes up as she starts to orgasm."
    $ the_person.have_orgasm()
    the_person "AH! OH! It's happening again!"
    $ the_person.change_slut(3, 40)
    "Her body starts to collapse so you quickly grab her with your left hand, your right hand still rubbing her pussy through her orgasm."
    if ellie_is_a_squirter():
        "Your hand starts to get damp as she cums, her forceful orgasm soaking through her clothes again."
    "It takes [the_person.title] several seconds to regain control of her legs."
    $ the_person.draw_person(position = the_person.idle_pose)
    " [the_person.possessive_title] suddenly pulls away from you and turns."
    the_person "Oh heavens I just... no way... not again!"
    the_person "oI'm so sorry, I have to go!!!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] quickly turns and flees your office, flinging your door open and running away."
    $ clear_scene()
    "You've brought the virgin to another orgasm in your office. It is so hot, watching her slowly learn to accept the sexual nature of her body."
    "You're sure that you are going to hear about this encounter from her again soon, but for now, you just enjoy the triumph of making her cum again."
    call advance_time from _call_advance_ellie_post_grope_01
    return

label ellie_text_message_apology_label():
    $ the_person = ellie
    "Sunday morning, you roll over and look at your phone. You have several missed text message."
    "Looking at your phone, you see they are all from [the_person.possessive_title], at about 3 am."
    $ mc.start_text_convo(the_person)
    the_person "Sorry, I know it's late, I was just up doing research on stuff you sent me..."
    the_person "I didn't know... all this stuff about my own body. No one ever told me this stuff."
    the_person "When I was in school, I just stayed busy with schoolwork and never had a boyfriend or anything."
    the_person "Anyway, thanks for sending me this, I appreciate yer helping me out with it."
    $ the_person.change_love(3)
    $ the_person.increase_sex_skill("Foreplay", 3, add_to_log = True)

    "You decide to send her a quick text back."
    mc.name "Happy to help. Let me know if you need any further demonstrations."
    $ the_person.change_slut(2)
    $ mc.end_text_convo()
    "You lay back down for a bit. You look at your phone and see the message was read, but she doesn't reply."
    $ add_ellie_never_given_handjob_action()
    return

label ellie_never_tasted_cock_label(the_person):  #This is Ellie's 40 sluttiness event.
    $ talk_person = get_random_employees(1, exclude_list = [the_person], slut_required = 50)
    $ scene_manager = Scene()
    $ ellie.story_event_log("slut")
    "As you walk towards the entrance of research and development, you begin to overhear a conversation."
    "You stop and listen in before walking in the door, not because of what is being talked about, but because of WHO is talking."
    if ellie_has_given_blowjob():
        the_person "So like, you've had one in your mouth before... right?"
        talk_person "Of course!"
        the_person "Do you ever like... yah know... in your mouth... when he finishes?"
        talk_person "Sure! Once in a while."
        the_person "But isn't it like... gross?"
        talk_person "Gross? No! I mean, it is a bit of acquired taste, but if you go into it with an open mind it is honestly not a bad taste."
        the_person "Sorry, I just... my mamma always said doing something like that was for whores..."
        talk_person "Nahh, as long as everyone is having a good time!"
        if the_person.get_opinion_score("cum facials") > the_person.get_opinion_score("drinking cum"):
            talk_person "Real talk here. Guy's love it when you just let them finish all over your face!"
            the_person "On... mah face?"
            talk_person "Yeah! They LOVE it. Plus it is actually kind of good for your skin."
            the_person "Ah... I see..."
        elif the_person.get_opinion_score("drinking cum") > 0:
            talk_person "Real talk here. I usually just swallow it all."
            the_person "Yeah?"
            talk_person "Yeah! Guys love it when you do that, and it makes cleanup stupid easy."
            the_person "Ah... I see..."
        else:
            talk_person "Real talk here. I usually just let guys finish however they want. On my face, my chest, in my mouth, whatever."
            the_person "Oh..."
        "You pick that moment to turn the corner into the room."
    else:
        the_person "So like, you've had one in your mouth before... right?"
        talk_person "Of course!"
        the_person "Isn't it, like, gross?"
        talk_person "Gross? No! I mean, it is a bit of acquired taste, but if you go into it with an open mind it is honestly not a bad taste."
        the_person "Sorry, I just... my mamma always said doing something like that was for whores..."
        talk_person "Nahh, as long as everyone is having a good time!"
        the_person "What do you do like, when he's finishing though?"
        if the_person.get_opinion_score("cum facials") > the_person.get_opinion_score("drinking cum"):
            talk_person "Real talk here. Guy's love it when you just let them finish all over your face!"
            the_person "On... mah face?"
            talk_person "Yeah! They LOVE it. Plus it is actually kind of good for your skin."
            the_person "Ah... I see..."
        elif the_person.get_opinion_score("drinking cum") > 0:
            talk_person "Real talk here. I usually just swallow it all."
            the_person "You... swallow?"
            talk_person "Yeah! Guys love it when you do that, and it makes cleanup stupid easy."
            the_person "Ah... I see..."
        else:
            talk_person "Real talk here. I usually just let guys finish however they want. On my face, my chest, in my mouth, whatever."
            the_person "Oh..."
        "You pick that moment to turn the corner into the room."
    $ scene_manager.add_actor(the_person, position = "sitting")
    $ scene_manager.add_actor(talk_person, position = "sitting", display_transform = character_center_flipped)
    "[the_person.possessive_title] is looking down when you enter and doesn't even notice you walk in. [talk_person.title] sees you, however, and smiles."
    talk_person "Oh hey [talk_person.mc_title]."
    "[the_person.title] startles and looks up at you."
    the_person "Ah! [the_person.mc_title]! I umm... I wasn't... we were just..."
    mc.name "Talking about some things highly inappropriate for work."
    the_person "Ohhh stars. I..."
    mc.name "Come with me. We'll talk about this in my office."
    the_person "Oh fudge... okay..."
    $ scene_manager.update_actor(the_person, position = "stand3")
    "[talk_person.possessive_title] looks at you a little concerned, but you give her quick wink. She gives a smile as you turn and walk back out of the room."
    $ scene_manager.clear_scene()
    $ del talk_person
    "Silently you lead [the_person.title] to your office."
    $ ceo_office.show_background()
    "You let her step inside, then close the door, locking it quietly, motioning for her to sit down."
    $ the_person.draw_person(position="sitting")
    "You sit down across from her."
    the_person "Look, it's not what you think!"
    mc.name "Oh, it's not, is it?"
    the_person "No, I was jus..."
    if ellie_has_given_blowjob():
        mc.name "You don't want to know what it is like to swallow cum?"
        the_person "I was curiou... wha???"
        mc.name "[the_person.title]. You don't have to go to other employees when you get curious about this stuff, okay? You can just come to me."
        "[the_person.possessive_title] is blushing hard."
        mc.name "Now... do you want to know what it's like to swallow my load?"
    else:
        mc.name "You don't want to know what it is like to suck dick?"
        the_person "I was curiou... wha???"
        mc.name "[the_person.title]. You don't have to go to other employees when you get curious about this stuff, okay? You can just come to me."
        "[the_person.possessive_title] is blushing hard."
        mc.name "Now... do you want to know what it's like to suck dick?"
    "[the_person.title] looks down for a few moments... but then gives a slow nod."
    mc.name "It's nothing to be ashamed about."
    the_person "I... I think I understand that sir... but I've spent so much of my life being told that kind of stuff is for... harlots..."
    "Her voice breaks a little with the last word."
    mc.name "It's okay. I understand that. If you don't want to try, that's fine. I don't want to pressure you into anything."
    mc.name "But I also want you to know that it is perfectly understandable to be curious."
    mc.name "Especially working here. We have a lot of work to be done here, researching chemicals and programs that change or enhance sexuality."
    mc.name "It's okay if the answer is no. Do you want to suck my dick?"
    "[the_person.possessive_title] nods her head."
    the_person "... Yes... I really do..."
    mc.name "There. Was that so hard? Come here. We'll go slow, okay?"
    $ the_person.draw_person()
    "[the_person.title] gets up and walks around your desk."
    mc.name "Go ahead and get down on your knees. There's a reason that's a classic."
    $ the_person.draw_person(position = "blowjob")
    "As she gets down, you pull your cock from your pants."
    mc.name "Alright, so there aren't really very many rules for this, but a basic one for while you are learning, no teeth!"
    the_person "No teeth?"
    mc.name "Right. Use your lips to cover up your teeth. Teeth hurt, okay?"
    the_person "Ah, okay, I'll try."
    mc.name "Alright, let's take this slow. Use your hand a little to get used to it."
    "[the_person.possessive_title] takes you in her hand and gives you a couple strokes. Not long ago, she had never done this either, but now she handles your meat with skill."
    $ mc.change_locked_clarity(20)
    mc.name "That's it. Now, just give it a little kiss."
    the_person "Okay... mmmm..."
    "[the_person.title] gives your cock a quick peck. Then another. Then three more."
    mc.name "See? It's not so bad, is it?"
    the_person "Nah, it's so hot. And it smells kind of... manly..."
    "[the_person.possessive_title] begins to kiss along the underside, down towards the base, then back up to the top."
    $ mc.change_locked_clarity(20)
    mc.name "Mmm, that feels nice."
    "When she gets to the tip, [the_person.title] looks up at you and makes eye contact. A bit of pre-cum is starting to leak from the tip."
    "She closes her eyes and sticks out her tongue. She slowly licks at the tip of the head, tasting your pre-cum for the first time."
    "It takes her a few moments to open her eyes."
    the_person "That... is certainly unique."
    if the_person.love > 40:
        the_person "It doesn't taste very good but like... because it's you, something about it makes it good anyways..."
    else:
        the_person "The taste isn't great... but the fact that it's coming from you makes it really hot anyways..."
    #Increase drinking cum score
    $ mc.change_locked_clarity(30)
    mc.name "Keep going, I'll be glad to get you some more."
    "[the_person.possessive_title] starts to run her tongue around the tip now. She goes up and down at first, then circles it a few times."
    "[the_person.title] gives you a couple more strokes with her hand while she licks the tip. She stops and looks up at you."
    the_person "Okay. Here goes!"
    "[the_person.possessive_title] opens her mouth and for the first time pushes your erection inside her lips."
    $ mc.change_locked_clarity(40)
    $ the_person.break_taboo("sucking_cock")
    "With the tip in her mouth, [the_person.title] swirls her tongue around it a few times. It feels so good."
    "After a few seconds, she bravely pushes down a little further. She is clearly testing her limits, unsure of how far she can take it."
    $ play_gag_sound()
    the_person "Mmmmmmm... UNGLCK"
    "[the_person.possessive_title] suddenly gags as she takes it a little too far. She quickly pulls off and catches her breath."
    the_person "Stars! Sorry I..."
    mc.name "It's okay. The tip is the most sensitive part, just do what you can, but don't force it."
    the_person "Mmm... okay..."
    $ mc.change_locked_clarity(40)
    $ the_person.increase_sex_skill("Oral", 4, add_to_log = True)
    "[the_person.title] looks up at you as she licks at the tip again. She maintains the eye contact as she opens her mouth and starts to suck on the tip again."
    $ the_person.change_arousal(10)
    the_person "Mmm... mmm..."
    "[the_person.possessive_title] gives a couple little moans as she keeps working you over. She seems to be be really getting into it."
    $ mc.change_locked_clarity(40)
    "[the_person.title] is getting braver. She pushes the tip past her lips now and starts bobbing her head gently."
    mc.name "That's it. You're doing great. If it starts to get uncomfortable, you can always back off and just use your hand for a bit."
    "[the_person.title] looks at you and nods for a second, but keeps going. Her silky tongue is working wonders traveling up and down your cock."
    $ mc.change_locked_clarity(40)
    "The sensations are getting more intense. She's going to make you cum."
    mc.name "[the_person.title], I'm gonna cum soon. What do you want me to do?"
    "She pulls off for a quick second."
    the_person "Whatever you want. I just want to make you feel good."
    "[the_person.possessive_title] opens up and starts sucking you off eagerly now. She is really working hard!"
    $ mc.change_locked_clarity(40)
    "The velvet soft tongue of [the_person.title] is driving you over the edge. What do you want to do?"
    menu:
        "Cum in her mouth":
            "You put your hand on the back of her head."
            mc.name "Get ready, I want to cum in your mouth... here it comes!"
            "With a moan you explode, your cock starts to dump its load in her eager mouth."
            $ the_person.cum_in_mouth()
            $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_person)
            $ the_person.draw_person(position = "blowjob")
            $ play_gag_sound()
            "[the_person.title] is startled by how forcefully you ejaculate. She gags almost immediately, but refuses to close her mouth."
            "Cumming in [the_person.possessive_title]'s hot, wet mouth feels incredible. When you finish, you look down and see that she still has the tip in her mouth."
            mc.name "[the_person.title], that was incredible. Now, I want you to look up at me and swallow."
            $ play_swallow_sound()
            "Dutifully, she looks up at you and does as you order. It takes a couple gulps, and she winces a bit, but she swallows it all."
            $ the_person.change_slut(2, 60)
            mc.name "So... how was it?"
            "She thinks about it for a moment."
            the_person "It was... I don't know! It was gross, but amazing at the same time..."
            $ the_person.increase_opinion_score("giving blowjobs", max_value = 1)
            $ the_person.increase_opinion_score("drinking cum", max_value = 2)
            $ the_person.increase_opinion_score("being submissive", max_value = 1)
        "Cum on her face" if not ellie_has_given_blowjob():
            "You put your hand on the back of her head and pull her off."
            mc.name "Use your hand, I want you to jack me off all over your face."
            "[the_person.possessive_title] starts stroking you rapidly with her hand, pointing you at her face."
            the_person "That's it. Cum on my face [the_person.mc_title]!"
            $ the_person.cum_on_face()
            $ ClimaxController.manual_clarity_release(climax_type = "face", the_person = the_person)
            $ the_person.draw_person(position = "kneeling1")
            "Hearing her words pushes you over the edge and your cock explodes. Spurt after spurt erupts all over her face."
            "She keeps jacking you off, and overall does a very good job of aiming your twitching manhood."
            "When the last wave finishes, you look down and survey [the_person.possessive_title]. Her face is plastered in your semen."
            $ the_person.change_slut(2, 60)
            mc.name "So... how was it?"
            the_person "It's... sticky? But hot, and watching you as you cum made me feel so incredible..."
            $ the_person.increase_opinion_score("giving blowjobs", max_value = 1)
            $ the_person.increase_opinion_score("cum facials", max_value = 2)
            $ the_person.increase_opinion_score("taking control", max_value = 1)

    "As you recover, you get yourself decent again."
    $ the_person.draw_person()
    $ the_person.event_triggers_dict["given_blowjob"] = True
    the_person "I... I think I'm gonna go to the lady's room..."
    if ellie_has_brought_lunch_date():  #You've already done a lunch date. Go straight to eating her out.
        menu:
            "Reciprocate by eating her out":
                mc.name "Already? But I want to return the favor."
                the_person "Ah, you want to... what now?"
                mc.name "I mean, it's only fair, right? You got to taste me... can't I taste you?"
                "[the_person.title] is shocked, she did not see this coming."
                the_person "I... I didn't like, shave or nothin'!"
                the_person "Aren't ladies supposed to do that?"
                mc.name "Nonsense. You can trim sometime if you would like, but I'm certain I can make my way through your red forest."
                $ the_person.change_slut(2, 60)
                "[the_person.title] thinks for several seconds. A drop of your cum slips off her face and onto the floor..."
                $ mc.change_locked_clarity(30)
                mc.name "Sit up on the desk. Don't worry, you won't regret it."
                the_person "Oh... stars! Okay..."
                call ellie_cunnilingus_office_label(the_person) from _ellie_post_bj_slam_dunk_01
                $ the_person.draw_person(position = "missionary")
                "You stand up. [the_person.possessive_title] is lying on your desk, recovering."
                the_person "Stars! [the_person.mc_title]... was that like how it was... when you...?"
                mc.name "It was."
                the_person "That felt so good... can we do this again sometime? I might need more practice."
                mc.name "Of course. I'm going to get back to work now. You can recover for a bit if you want before getting back to work."
                the_person "Yes sir..."
                $ clear_scene()
                "You step out of your office, leaving [the_person.possessive_title] to recover. You head to the restroom and clean up your face before returning to work."
            "Let her go":
                mc.name "That's a good idea."
                the_person "But umm... can we do this again sometime? I ummm... I might need more practice."
                mc.name "I think that can be arranged."
                $ the_person.draw_person(position = "walking_away")
                "[the_person.possessive_title] awkwardly turns and walks out of your office."
                $ clear_scene()
    else:
        mc.name "That's a good idea."
        the_person "But umm... can we do this again sometime? I ummm... I might need more practice."
        mc.name "I think that can be arranged."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] awkwardly turns and walks out of your office."
        $ clear_scene()
    "Your conservative, southern belle has now given you a blowjob! And it sounds like she wants to do it again soon!"
    "[the_person.title] now has oral positions unlocked."
    $ the_person.add_unique_on_room_enter_event(ellie_turned_on_while_working_intro)
    $ the_person.add_unique_on_room_enter_event(ellie_never_been_fucked)
    $ the_person.apply_planned_outfit()
    $ mc.location.show_background()
    #"Ellie may now approach MC once in a while when she is working on nanobot programs because working on sex related code is getting in her head and she needs some relief"
    return

label ellie_oral_taboo_restore_label():
    pass
    return

label ellie_work_blowjob_label(the_person):
    pass
    return

label ellie_never_been_fucked_label(the_person):  #This is Ellie's 60 sluttiness event. Also requires X number of oral encounters?
    $ ellie.story_event_log("slut")
    $ the_person.arousal = 70
    $ the_person.draw_person(position = "sitting")
    "You check up on [the_person.title] while she is working."
    "She appears to be getting herself really worked up again. She has one hand between her legs, touching herself, while she tries to type with the other."
    "You sigh. She has so many years of pent up sexual drive, she can barely control it now. Especially with all the serums you've been testing on her."
    mc.name "Trouble concentrating, [the_person.title]?"
    the_person "Ah!"
    "She startles, pulling her hand back from between her legs when she looks up from her work at you."
    the_person "No! No sir I was..."
    "She mumbles something you can't hear."
    mc.name "You were... what now?"
    "[the_person.possessive_title] sighs."
    the_person "I... I'm trying to work on this... but stars I just can't stop thinking about..."
    if ellie_has_given_virginity():
        the_person "You know... the thing we did the other day..."
        "Ever since you took her virginity, she has been looking for excuses to fuck you as often as possible."
    else:
        "She leaves off the end of her sentence. [the_person.title] has been working for you for a while now, but it is clear that she is finally ready."
        "You've fooled around with her a few times, but now it is time to take the final step and show her how good sex can be."
    mc.name "Come with me, I want to spend some time with you in my office."
    the_person "Oh! Okay!"
    $ the_person.draw_person(position = the_person.idle_pose)
    "She quickly jumps up and follows you out of R&D."
    $ ceo_office.show_background()
    "Once in your office, you close and lock the door."
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
        mc.name "It is clear to me that you need some relief... again..."
        the_person "I... I do appreciate it [the_person.mc_title]."
        mc.name "I think it is time for you to take the lead though."
        the_person "Sir?"
        "You step close to her, putting on hand on her shoulder."
        mc.name "Let's get naked. I'll sit down in my chair, and then you can come sit on my lap."
        the_person "Ah, you want me to... be on top? Are you sure?"
        "She bites her lip. You lift your hand up from her shoulder to her cheek. She looks up into your eyes... then melts."
        the_person "Okay... I can try that..."
        mc.name "Alright, let's get naked."
        $ the_person.strip_outfit(position = the_person.idle_pose)
        "You both quickly get undressed. You check out [the_person.possessive_title]."
        "Her nipples are stiff, and her labia are puffy and aroused. Clearly she is really turned on already."
        "You step over to your chair and sit down."
        mc.name "Alright, come here."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] walks over to you, then gets on your lap, her amazing tits are right in your face."
        mc.name "God your tits are fantastic."
        "You cup one in your hand, bringing your mouth up to the other one. You quickly suck and nip at her nipple, eliciting a loud moan from [the_person.possessive_title]."
        "You feel her hand on the back of your head, running her hand through your hair as you suckle her tit."
        the_person "Ahh. Okay, just gonna... do this... for a bit..."
        "[the_person.title] slowly adjusts her hips wider, until you can feel her humid groin get closer to yours, and then finally makes contact."
        the_person "Stars! It's so hard! Ahhh..."
        "She groans as she starts to rub herself up against you. Her soaking wet cunt is leaking fluid as she presses her hips eagerly against you and starts to grind."
        $ the_person.change_arousal(15) #85
        "You let go of her chest with your hand and put both your hands on her ass. You grab it to use for leverage as you start to thrust yourself up against her."
        the_person "[the_person.mc_title]! Be careful I'm... I'm already so... so close!"
        $ play_spank_sound()
        "Fuck it. You're sure you can make her cum more than once like this. You give her ass a smack but don't let up."
        $ the_person.change_arousal(20) #105
        the_person "Ah! I can't take it...!"
        $ the_person.have_orgasm(force_trance = True) #52
        "[the_person.possessive_title] suddenly starts to shake as she begins to orgasm. Her legs stop moving and she moans loudly."
        if ellie_is_a_squirter():
            "You feel an alarming amount of fluid in your lap as she orgasms, squirting as she cums."
        "She spends several seconds with her legs and arms rigid as you thrust up against her, your hands groping her ass."
        "When she finishes, she opens her eyes and looks at you."
        the_person "That was so good... your thing is so... hard..."
        "She pushes herself back a bit on your lap, then reaches down and takes your cock in her hand."
        $ the_person.draw_person(position = "kneeling1")
        "She gives you a few slow strokes with her hand, your cock is heavily lubricated from rubbing against her slit."
        the_person "Stars, it's throbbing!..."
        "[the_person.possessive_title] sits up a bit and leans forward. With your cock in hand, she rubs it up and down her slit again a few times."
        the_person "It's so hard... I can't wait to feel it inside..."
        $ the_person.change_arousal(10) #62
        "After several seconds, she looks at you."
        the_person "Okay... I think I'm ready."
        "After several seconds, she lifts her hips up and rotates them forward a bit. She takes the base of your cock in her hand."
        "Slowly, she lets her body weight down as you feel your tip push slightly up and into her vagina."
        the_person "Oh... [the_person.mc_title], it's so big... it feels amazing!"
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] leans forward and wraps her arms around you. Your face is buried in her cleavage."
        "[the_person.title] takes a deep breath."
        "You feel movement a she begins to let herself down, using her body weight to sink down onto you."
        $ the_person.change_arousal(20)    #82
        $ the_person.draw_person(position = "cowgirl")
        the_person "Ah! Oh stars OH!"
        "Her body goes rigid for several seconds... Did... she cum again?"
        the_person "Whew... that was close... Ha!"
        "You start to lick and suck on her nipple, and you feel her body shudder for a moment."
        "You spend several seconds on her tits before you feel her start to move."
        $ the_person.change_arousal(30) #112
        the_person "Ah! I'm not gonna last... I'm... OH!"
        $ mc.change_arousal(20)
        $ the_person.have_orgasm(force_trance = True) #56
        "[the_person.possessive_title] is cumming again! You grope her tits aggressively as her body twitches and spasms."
        if ellie_is_a_squirter():
            "Another orgasm, another flood as she squirters in your lap."
        the_person "Ah... I can't believe it..."
        "She leans back, her nipple leaves your mouth with a loud smack. You can feel her pussy quiver around you."
        mc.name "Damn. Twice already? Will I get a proper fuck?"
        the_person "Ah, of course... just give me a minute..."
        "[the_person.possessive_title]'s pussy is so warm and tight wrapped around you. It wasn't so long ago you took her virginity."
        "You reach with your hands behind her again and grab her ass. Her warm cheeks feel so good in your hands."
        the_person "Alright. I think I'm ready to get this thing going!"
        mc.name "What do you want me to do when I'm ready to finish?"
        if the_person.wants_creampie:
            the_person "You know how I want it. Right up inside me where it belongs..."
            mc.name "Alright. One cum stuffed cunt, coming right up."
        else:
            the_person "I should probably pull off... just in case..."
            mc.name "Alright. I'll warn you when I'm getting ready to cum, but that is up to you."
        "[the_person.title] starts to move her hips up and down."
        $ the_person.change_arousal(20) #76
        "[the_person.title]'s poor little cunt is quivering all around you. You have an almost overwhelming urge to grab her ass and slam it into her and fuck her silly, but you resist for now."
        mc.name "God damn your cunt is so good. Don't worry I probably won't last long either."
        "She leans forward to try a different angle now, her tits now back in range of your mouth. You eagerly sink your face into her tit flesh."
        $ the_person.change_arousal(20) #96
        the_person "[the_person.mc_title]! Your cock is so big, it's filling me up!"
        "You just murmur your agreement as you assault a nipple with your tongue. She is gasping with every thrust now."
        $ the_person.change_arousal(20) #92
        "The southern belle is moaning and gasping as you fuck her. She is getting close to cumming."
        "The heat of the situation is getting to you as well."
        "You grab her hips with your hands. Instead of allowing her to keeping move front to back, you pick up her body a few inches above you."
        the_person "[the_person.mc_title]? What are you..."
        "With room to work now, you thrust your hips forcefully up into hers. Her ass makes a loud smack as you begin to fuck her."
        $ the_person.change_arousal(20) #112
        the_person "Ah! Oh my stars it's too good! I'm... I'm cumming!"
        "[the_person.possessive_title]'s body goes rigid again as she starts to cum. Her tight, quivering little hole feels too good and pushes you over the edge too."
        mc.name "Oh fuck, me too!"
        $ the_person.have_orgasm(force_trance = True)
        if the_person.wants_creampie:
            the_person "Do it! I have to feel it!"
            $ the_person.cum_in_vagina()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
            $ the_person.draw_person(position = "cowgirl")
            "You slam her hips down onto yours, pushing yourself as deep as possible as you start to cum."
            "Her entire body is twitching and spasming as she cums with you. It feels like her cunt is milking you for every last drop."
            if ellie_is_a_squirter():
                "You can feel her copious juices running down between your legs and onto your chair."
            "Your cock twitches and pulses as you send out the last few spurts of your cum inside her. She clings to you helplessly."
        else:
            the_person "Ah! I should... I should get up..."
            "Her voice is shaky as she tries to gather the will to pull off. With a push or a pull on her hips, you could probably finish any way you want..."
            $ climax_controller = ClimaxController(["Pull her down and cum inside her", "pussy"],["Let her pull off and cum on her stomach", "body"])
            $ the_choice = climax_controller.show_climax_menu()
            if the_choice == "Pull her down and cum inside her":
                "You reach up and grab [the_person.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
                "The feeling of her warm, wet pussy sliding down and engulfing your cock again pushes you over the edge. You pull [the_person.title] tight against you and unload inside of her."
                the_person "Ah! Just... Just this once!"
                $ the_person.call_dialogue("cum_vagina")
                $ climax_controller.do_clarity_release(the_person)
                $ the_person.cum_in_vagina()
                $ the_person.change_obedience(5)
                $ the_person.draw_person(position = "cowgirl")

            elif the_choice == "Let her pull off and cum on her stomach":
                "You reach up and grab [the_person.possessive_title] by the hips. With one push your cock slips out from her warm cunt."
                "She grinds the lips of her pussy against your shaft as you climax. You fire your hot load over her stomach."
                $ the_person.cum_on_stomach()
                $ climax_controller.do_clarity_release(the_person)
                $ cowgirl.redraw_scene(the_person)
                the_person "Whew, that was close..."
        "For several seconds, [the_person.title] just sits on top of you."
        the_person "That was incredible. Three... three times!"
        mc.name "Maybe now you can concentrate on work."
        $ play_spank_sound()
        "She laughs for a moment. You give her ass a playful smack."
        "There are several moments of silence."
        the_person "I don't want to get up."
        mc.name "Take your time. Work can wait."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(2)
        the_person "Ah... yes sir."
        "Eventually, she slowly gets up."
        $ the_person.draw_person(position = "standing_doggy")
        the_person "Ah, we made such a mess..."
        "She turns around and starts looking in your desk drawers for something to clean herself with."
        "You just watch her ass sway back and forth in front of you in an orgasm addled bliss."
        "Eventually, she finds your wipes and stands up."
        $ the_person.draw_person(position = the_person.idle_pose)
    else:
        mc.name "It is clear to me that you need some relief... again..."
        the_person "I... I do appreciate it [the_person.mc_title]."
        mc.name "However, I'm a bit worried. Honestly, I don't think that yet another round of oral or fingerbanging is going to help much."
        the_person "Sir?"
        "You step close to her, putting on hand on her shoulder."
        mc.name "I think we both know it is time for you experience the real thing."
        "She shudders for a second... but there is still a bit of resistance."
        the_person "Stars, I don't know... I'm scared to..."
        "You see as she bites her lip, thinking."
        mc.name "Tell you what, I have an idea."
        the_person "Yeah?"
        mc.name "Let's just get naked. I'll sit down in my chair, and then you can come sit on my lap."
        the_person "But..."
        mc.name "You don't have to put it in if you don't want to, or you could even try just the tip, see how it feels."
        the_person "I don't know..."
        mc.name "Or just grind against me for a bit. I won't push you to take any steps you aren't ready for, it'll all be up to you."
        "She bites her lip again. You lift your hand up from her shoulder to her cheek. She looks up into your eyes... then melts."
        the_person "Okay... I'll just put it up against me for a bit... yeah that would feel good..."
        "Whew. You convinced her. Of course, for now, she thinks she is just going to grind against you for a bit..."
        "But with all the serums she's been taking, there is no way she just stops there."
        mc.name "Alright, let's get naked."
        $ the_person.strip_outfit(position = the_person.idle_pose)
        "You both quickly get undressed. You check out [the_person.possessive_title]."
        "Her nipples are stiff, and her labia are puffy and aroused. Clearly she is really turned on already."
        "You step over to your chair and sit down."
        mc.name "Alright, come here."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] walks over to you, then gets on your lap, her amazing tits are right in your face."
        mc.name "God your tits are fantastic."
        "You cup one in your hand, bringing your mouth up to the other one. You quickly suck and nip at her nipple, eliciting a loud moan from [the_person.possessive_title]."
        "You feel her hand on the back of your head, running her hand through your hair as you suckle her tit."
        the_person "Ahh. Okay, just gonna... do this... for a bit..."
        "[the_person.title] slowly adjusts her hips wider, until you can feel her humid groin get closer to yours, and then finally makes contact."
        the_person "Stars! It's so hard! Ahhh..."
        "She groans as she starts to rub herself up against you. Her soaking wet cunt is leaking fluid as she presses her hips eagerly against you and starts to grind."
        $ the_person.change_arousal(15) #85
        "You let go of her chest with your hand and put both your hands on her ass. You grab it to use for leverage as you start to thrust yourself up against her."
        the_person "[the_person.mc_title]! Be careful I'm... I'm already so... so close!"
        $ play_spank_sound()
        "Fuck it. You're sure you can make her cum more than once like this. You give her ass a smack but don't let up."
        $ the_person.change_arousal(20) #105
        the_person "Ah! I can't take it...!"
        $ the_person.have_orgasm() #52
        "[the_person.possessive_title] suddenly starts to shake as she begins to orgasm. Her legs stop moving and she moans loudly."
        if ellie_is_a_squirter():
            "You feel an alarming amount of fluid in your lap as she orgasms, squirting as she cums."
        "She spends several seconds with her legs and arms rigid as you thrust up against her, your hands groping her ass."
        "When she finishes, she opens her eyes and looks at you."
        the_person "That was so good... your thing is so... hard..."
        "She pushes herself back a bit on your lap, then reaches down and takes your cock in her hand."
        $ the_person.draw_person(position = "kneeling1")
        "She gives you a few slow strokes with her hand, your cock is heavily lubricated from rubbing against her slit."
        the_person "Stars, it's throbbing!..."
        "[the_person.possessive_title] sits up a bit and leans forward. With your cock in hand, she rubs it up and down her slit again a few times."
        the_person "It wants to go in... doesn't it?"
        mc.name "Of course. Our bodies are meant to come together this way."
        $ the_person.change_arousal(10) #62
        mc.name "The question is, do you want it to go in?"
        "[the_person.title] remains silent, but continues to rub your erection up and down her pussy."
        "After several seconds, she looks at you."
        the_person "Maybe... like you said earlier... you could put just the tip in? Just... to see how it feels..."
        mc.name "That's a great idea. You're on top. I'm ready whenever you are."
        "[the_person.possessive_title] sighs. She is nervous, but her desire is finally getting the better of her."
        "After several seconds, she lifts her hips up and rotates them forward a bit. She takes the base of your cock in her hand."
        "Slowly, she lets her body weight down as you feel your tip push slightly up and into her vagina."
        "It comes to an abrupt stop when you hit her virginity. She flinches for a second."
        the_person "Oh... [the_person.mc_title], it's so big..."
        mc.name "Shh, it's okay. Just enjoy it for a bit."
        $ the_person.draw_person(position = "cowgirl")
        "[the_person.title] leans forward and wraps her arms around you. Your face is buried in her cleavage."
        the_person "This... this is going to hurt... isn't it?"
        mc.name "Just for a bit. In just a few minutes, it'll turn into something incredible."
        the_person "You're right. I know you're right. Okay..."
        "[the_person.title] takes a deep breath."
        "You feel movement a she begins to let herself down, using her body weight to sink down onto you."
        "At first, nothing happens, but then suddenly her body gives way as her hymen tears."
        $ take_virginity(the_person)
        $ the_person.change_arousal(-50)    #12
        $ the_person.draw_person(position = "cowgirl")
        the_person "Ah! Oh stars oh snap!"
        "Her body goes rigid for several seconds. You glance down and see a bit of blood going down her thigh."
        the_person "[the_person.mc_title] this hurts! You are so big... it's tearing me apart!"
        mc.name "Shh, just relax. The worst of it is over. Here, let me help..."
        "You start to lick and suck on her nipple again, and you feel her body shudder for a moment."
        "You spend several seconds on her tits before you feel her start to move again."
        "She keeps letting her body sink down onto yours. It feels like ages, but soon you feel her push herself all the way down."
        "Fully impaled on you now, she gasps as you play with her tits."
        $ the_person.change_arousal(20) #32
        the_person "Ah... it's in... I can't believe it..."
        "She leans back, her nipple leaves your mouth with a loud smack. You can feel her pussy quiver around you."
        the_person "You better be right about this. It is starting to feel good now..."
        mc.name "Don't worry. This is the start of something amazing. You might be sore for a day or two, but you are going to love it everytime we fuck."
        "[the_person.possessive_title]'s pussy is so warm and tight wrapped around you. It isn't everyday you get to take a girl's virginity, so you just sit back and savor it."
        "You reach with your hands behind her again and grab her ass. Her warm cheeks feel so good in your hands."
        the_person "Alright... I think I'm ready to get this thing going..."
        mc.name "What do you want me to do... when I'm ready to finish?"
        the_person "Oh... I hadn't really thought about that."
        "She looks at you for a moment."
        the_person "I think... I want you to just finish... like this."
        mc.name "Inside you?"
        the_person "Yeah... this might be dumb but, this is my first time. I want to feel everything."
        mc.name "Okay. I'm ready when you are."
        the_person "Alright."
        "Slowly, gently, [the_person.possessive_title] rocks her hips forward a bit, and you slide partially out. Then she rocks her hips back, enveloping you fully again."
        the_person "Ahh!... oh wow..."
        "She does it again, going slowly. Her breath catches in her throat when she pushes it back again."
        the_person "[the_person.mc_title]...!"
        $ the_person.change_arousal(20) #52
        "[the_person.title]'s poor little cunt is quivering all around you. You have an almost overwhelming urge to grab her ass and slam it into her and fuck her silly, but you resist for now."
        mc.name "That's it. See? It is starting to feel good, isn't it?"
        "[the_person.possessive_title] is moving her hips back and forth now, her body quickly learning what feels good as she changes the angle a few times."
        the_person "It is... Oh stars it feels so good."
        "She leans forward to try a different angle now, her tits now back in range of your mouth. You eagerly sink your face into her tit flesh."
        $ the_person.change_arousal(20) #72
        the_person "[the_person.mc_title]! You're filling me up... it's so good!"
        "You just murmur your agreement as you assault a nipple with your tongue. She is gasping with every thrust now."
        $ the_person.change_arousal(20) #92
        "The southern belle is moaning and gasping as you fuck her for the first time. She is getting close to cumming."
        "The heat of the situation is getting to you as well. You decide it is time to fuck her proper and make her first time truly memorable."
        "You grab her hips with your hands. Instead of allowing her to keeping move front to back, you pick up her body a few inches above you."
        the_person "[the_person.mc_title]? What are you..."
        "With room to work now, you thrust your hips forcefully up into hers. Her ass makes a loud smack as you begin to fuck her."
        $ the_person.change_arousal(20) #112
        the_person "Ah! Oh my stars it's too good! I'm... I'm cumming!"
        "[the_person.possessive_title]'s body goes rigid again as she starts to cum. Her tight, quivering little hole feels too good and pushes you over the edge too."
        mc.name "Of fuck, me too!"
        $ the_person.have_orgasm(force_trance = True)
        the_person "Do it! I have to feel it!"
        $ the_person.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_person)
        $ the_person.draw_person(position = "cowgirl")
        "You slam her hips down onto yours, pushing yourself as deep as possible as you start to cum."
        "Her entire body is twitching and spasming as she cums with you. It feels like her cunt is milking you for every last drop."
        if ellie_is_a_squirter():
            "You can feel her copious juices running down between your legs and onto your chair."
        "Your cock twitches and pulses as you send out the last few spurts of your cum inside her. She clings to you helplessly."
        the_person "That was incredible."
        mc.name "I told you it would be."
        "She laughs for a moment."
        the_person "Yeah... you did."
        "There are several moments of silence."
        the_person "I don't want to get up."
        mc.name "Take your time. Work can wait."
        $ the_person.change_happiness(5)
        $ the_person.change_obedience(2)
        the_person "Ah... yes sir."
        "You sit for for a while just like that, your softening cock still inside of [the_person.possessive_title]."
        "Eventually, she slowly gets up, not anticipating how much would leak out of her."
        $ the_person.draw_person(position = "standing_doggy")
        "She panics, quickly turning around and puts her hand between her legs to keep too much from leaking out."
        "You can see her blood mixed with cum running down her legs. It makes your cock twitch at the incredible sight."
        the_person "[the_person.mc_title]! Get me a tissue or something, stars!"
        "You laugh and quickly grab some wipes from your desk."
        $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.title] is standing in front of you, starting to clean herself up. You can tell from the look in her eyes she is in a bit of a daze."
    "Or is that a trance? You decide to try and do some post orgasm training..."
    call do_training(the_person) from _call_do_training_ellie_after_fuck_01
    "[the_person.possessive_title] cleans herself up."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "I'm going to get back to work..."
    mc.name "Sounds good. I'll have to check your productivity at the end of the day. If it goes up, we might have to make this a regular thing."
    the_person "Oh... I'd better work hard then!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] turns and starts to walk out of your office. You can't believe how far she has come."
    "From a blackmailing virgin, she is getting to be one of your favorite office cumdumps."
    "You smile as you think about how far things are going to go with her."
    $ the_person.add_unique_on_room_enter_event(ellie_never_tried_anal)
    return

label ellie_vaginal_taboo_restore_label():
    pass
    return

label ellie_work_fuck_label(the_person):
    pass
    return

label ellie_never_tried_anal_label():   #This is Ellie's 80 sluttiness rating. Must have anal nanobots unlocked.
    pass
    $ ellie.story_event_log("slut")
    $ ellie.event_triggers_dict["given_anal_virginity"] = True
    return

label ellie_anal_taboo_restore_label():
    pass
    return

label ellie_work_anal_label(the_person):
    pass
    return

label ellie_turned_on_while_working_intro_label(the_person):
    $ ellie.event_triggers_dict["work_turnon"] = False
    return

label ellie_turned_on_while_working_label():    #Crisis event. Can be triggered after unlocking Ellie's oral sex options, and procs when she is working on nanobot programming.
    "During a break, you make the rounds to the different departments. When you swing by R&D, you decide to check up on [ellie.title]"
    "[ellie.title] is masturbating, trying to type with one hand and playing with herself with the other."
    "She is sorry. Working on this stuff gets her so horny."
    "Initially, you can chastise her (dislikes masturbation), encourage her (likes masturbation), or offer to help her."
    "If you offer to help her, you can do it right there in R&D (likes public sex), or find somewhere private."
    "Her reactions change based on her story and corruption progress. At extreme sluttiness, when she sees you walk up she may jump MC or if submissive, pull down bottoms and bend over her desk and beg."
    "Sex scene."
    return

label ellie_asks_to_join_harem_label(the_person):   #100 sluttiness event. Ellie asks to join MCs harem.
    pass
    return
