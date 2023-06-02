init 2 python:
    def myra_bigger_tits_intro_requirement(the_person):
        if the_person.obedience >= 120 and myra_at_cafe():
            if myra.days_since_event("myra_bigger_tits_suggestion_day") > 7:
                return True
        return False

    def myra_bigger_tits_serum_requirement(the_person):
        if myra_wants_bigger_tits() and not myra.has_large_tits:
            if myra_at_cafe():
                if mc.inventory.has_serum_with_trait(breast_enhancement):
                    return True
                else:
                    return "Requires serum with Breast Enhancement Trait"
        return False

    def myra_bigger_tits_final_requirement(the_person):
        if myra.has_large_tits and myra_at_cafe():
            return True
        return False

    def myra_blowjob_training_intro_requirement(the_person):
        if the_person.obedience >= 140 and the_person.opinion_score_giving_blowjobs() > -2:
            if myra_at_cafe() and the_person.event_triggers_dict.get("can_train_focus", False):
                return True
        return False

    def myra_blowjob_training_progress_requirement(the_person):
        if myra_at_cafe() and myra.days_since_event("myra_bj_train") >= TIER_2_TIME_DELAY and the_person.obedience >= 160:
            return True
        return False

    def myra_blowjob_training_final_requirement(the_person):
        if myra_at_cafe() and myra.days_since_event("myra_bj_train")  >= TIER_2_TIME_DELAY and the_person.obedience >= 180:
            return True
        return False

    def add_myra_bigger_tits_intro_action():
        myra_bigger_tits_intro = Action("Myra Wants Bigger Tits", myra_bigger_tits_intro_requirement, "myra_bigger_tits_intro_label")
        myra.add_unique_on_room_enter_event(myra_bigger_tits_intro)
        myra.event_triggers_dict["suggested_bigger_tits"] = True
        myra.set_event_day("myra_bigger_tits_suggestion_day", override = False)
        return

    def add_myra_bigger_tits_serum_action():
        myra_bigger_tits_serum = Action("Give Serum for Bigger Tits", myra_bigger_tits_serum_requirement, "myra_bigger_tits_serum_label")
        myra.get_role_reference("myrabelle").add_action(myra_bigger_tits_serum)
        return

    def remove_myra_bigger_tits_serum_action():
        myra.get_role_reference("myrabelle").remove_action("myra_bigger_tits_serum_label")
        myra.increase_opinion_score("giving tit fucks")
        myra.event_triggers_dict["wants_bigger_tits"] = False
        return

    def add_myra_bigger_tits_final_action():
        myra_bigger_tits_final = Action("Myra Gets Large Tits", myra_bigger_tits_final_requirement, "myra_bigger_tits_final_label")
        myra.add_unique_on_talk_event(myra_bigger_tits_final)
        myra.event_triggers_dict["wants_bigger_tits"] = True  #This will open up the option on her role
        return

    def add_myra_blowjob_training_intro_action():
        myra_blowjob_training_intro = Action("Myra Needs Help", myra_blowjob_training_intro_requirement, "myra_blowjob_training_intro_label")
        myra.add_unique_on_room_enter_event(myra_blowjob_training_intro)
        myra.event_triggers_dict["lewd_game_oral"] = True
        return

    def add_myra_blowjob_training_progress_action():
        myra_blowjob_training_progress = Action("Develop Myra Orally", myra_blowjob_training_progress_requirement, "myra_blowjob_training_progress_label")
        myra.add_unique_on_room_enter_event(myra_blowjob_training_progress)
        myra.increase_opinion_score("giving blowjobs")
        myra.set_event_day("myra_bj_train")
        return

    def add_myra_blowjob_training_final_action():
        myra_blowjob_training_final = Action("Develop Myra Orally", myra_blowjob_training_final_requirement, "myra_blowjob_training_final_label")
        myra.set_event_day("myra_bj_train")
        myra.add_unique_on_room_enter_event(myra_blowjob_training_final)
        return

label myra_bigger_tits_intro_label(the_person):        #120 obedience event. If MC suggested bigger tits in love story, myra is interested now.
    $ the_person.draw_person()
    "You step into the gaming cafe. As you walk in, [the_person.possessive_title] notices you and walks over."
    the_person "Hey, do you have a second? I wanted to talk to you about something..."
    mc.name "Absolutely. What is on your mind [the_person.title]?"
    the_person "The other day, you said something that kind of got some gears turning in my head..."
    the_person "I've never been one to stress about looks, especially things that are outside of my control but..."
    the_person "Do you really think I should get bigger tits?"
    $ mc.change_locked_clarity(30)
    mc.name "That is a pretty loaded question."
    the_person "I know, and honestly the prospect of getting surgery terrifies me but, I don't know, you seem like a good guy, and I thought you could give me an honest opinion."
    mc.name "Well, I think you need to do what is right for you, first of all. But, I do have something that I think you might be interested in."
    the_person "Oh?"
    mc.name "As you know, I run a pharmaceutical company, and we are actually running tests on a drug that naturally increases breast size."
    the_person "What? Like, without surgery?"
    mc.name "That is correct."
    the_person "Do you need anyone to help test it?"
    mc.name "Actually yes. Would you be interested?"
    the_person "Yeah. I think I am. I want to know what it is like... you know?"
    mc.name "Well, I can't promise anything, but I'll make sure to keep you in mind if we do any trials soon."
    the_person "Ah, thank you [the_person.mc_title]! I'd better get back to the desk."
    $ the_person.change_obedience(2)
    $ the_person.change_happiness(2)
    $ clear_scene()
    "[the_person.title] will now accept breast enhancement serums."
    $ add_myra_bigger_tits_serum_action()
    $ add_myra_bigger_tits_final_action()
    return

label myra_bigger_tits_serum_label(the_person):       #This option becomes available if Myra wants bigger tits.
    mc.name "Hey, I have a breast enhancement serum for you to try. Still interested?"
    the_person "I am, yes!"
    call give_serum(the_person) from _call_give_myra_bigger_tits_serum_01
    if _return:
        "You hand her the serum, and she quickly drinks it down."
        mc.name "It might be a few days until you see the effects."
        the_person "Okay... I'll let you know how they work!"
    else:
        mc.name "Actually, I think I left them at the shop."
        "[the_person.title] looks disappointed, but understands."
    return

label myra_bigger_tits_final_label(the_person):       #If her tits are bigger, she thanks MC.
    "As you step into the gaming cafe, [the_person.possessive_title] spots you. She quickly walks up to you and grabs your hand."
    $ the_person.draw_person(position = "walking_away")
    the_person "Come on! I need to show you something!"
    "As you follow after her, you feel like you notice a little more... jiggle? In her step?"
    "She leads you to a stock room in the back. After practically shoving you in, she closes the door and locks it."
    $ the_person.draw_person()
    the_person "Sorry, I just had to do this. Check these out!"
    $ the_person.strip_to_tits(position = "stand3")
    $ mc.change_locked_clarity(30)
    if the_person.sluttiness >= 40 or the_person.love > 60:
        "[the_person.possessive_title] quickly strips off her top, revealing a generous set of tits."
        the_person "They're amazing! And they feel completely natural! Come, feel this..."
        "She grabs your hand and drags it to her chest, forcing you to feel her up."
        the_person "See? And..."
        $ the_person.change_arousal(20)
        the_person "And... they're so sensitive too..."
        $ the_person.increase_opinion_score("showing her tits")
        $ mc.change_locked_clarity(30)
        "You spend several seconds feeling up her new and improved rack. You admit, they are impressive."
        $ mc.change_arousal(20)
        "You can feel yourself getting excited as she starts to whimper from your touch."
        the_person "They are awesome, right?"
        "[the_person.possessive_title] looks down and notices your erection."
        the_person "Hey... you know... I've never had big enough tits to like..."
        "She looks at you for a moment."
        the_person "Want to fuck them?"
        mc.name "Yes. Yes I do."
        $ mc.change_locked_clarity(30)
        the_person "Hell yeah let's do it. I bet it feels amazing..."
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] gets down on her knees, you whip out your cock. She slides over to you."
        the_person "I've like, never done this so... you might have to help me a bit..."
        mc.name "I'm sure you'll do great."
        "With your cock in her hand, she slides the tip of your cock into her cleavage. Your erection quietly disappears into her ample bosom."
        "Her soft tit flesh feels great wrapped around you."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Wow, it feels so hot... God this is naughty... I love it!"
        "[the_person.title] starts to move her chest up and down, stroking your cock."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_myra_tits_reveal_1
        "When you finish, [the_person.possessive_title] stands up."
        $ the_person.draw_person()
        the_person "Wow... We'll have to do that again sometime."
        mc.name "Yes, anytime you need a cock between your tits, hit me up."
        the_person "Ha! Okay 'coach'. I'll keep that in mind! I'd better get cleaned up and get back to work."
    else:
        "[the_person.title] quickly pulls off her top, giving you an amazing view of her tits."
        mc.name "Damn. They look amazing."
        the_person "Yeah... they feel so sensitive too..."
        mc.name "Is that so?"
        "You step close to her, she takes a half step back."
        the_person "That's... what are you doing?"
        mc.name "I want to feel them for myself. You don't mind, right?"
        the_person "I suppose not... You did give me the drugs to do this I guess..."
        "You step forward again. You reach forward with both hands and take hold of her twin peaks."
        "They feel hot and soft to the touch. She whimpers a bit as you feel her up."
        $ the_person.change_arousal(20)
        the_person "They are amazing. You should be proud to show these girls off."
        $ the_person.increase_opinion_score("showing her tits")
        $ mc.change_locked_clarity(30)
        the_person "Mmm... yeah I think so..."
        "You pinch her nipples, then roll them between your thumb and fingers."
        $ the_person.change_arousal(20)
        the_person "Oh fuck they are so sensitive too..."
        $ mc.change_arousal(20)
        mc.name "Yeah you like it when I touch you like this don't you."
        the_person "Mmm... I do..."
        "You spend several seconds with [the_person.possessive_title], just enjoying the weight and softness of her improved rack."
        $ mc.change_arousal(20)
        mc.name "Damn. Now I'm all turned on. Why don't you get on your knees, let's see how they feel wrapped around my cock."
        "[the_person.title] looks at you, conflicted. This is a little outside her comfort zone."
        the_person "I... I don't know..."
        mc.name "Come on now. I made this possible, don't I deserve a little reward? I gave you the serums, free of charge."
        the_person "That's true."
        "She thinks about it for a few more moments."
        the_person "Fuck it. I was wondering what it would be like to do this anyway. Might as well be with you!"
        $ the_person.draw_person(position = "blowjob")
        "As [the_person.possessive_title] gets down on her knees, you whip out your cock. She slides over to you."
        the_person "I've like, never done this so... you might have to help me a bit..."
        mc.name "I'm sure you'll do great."
        "With your cock in her hand, she slides the tip of your cock into her cleavage. Your erection quietly disappears into her ample bosom."
        "Her soft tit flesh feels great wrapped around you."
        $ the_person.change_arousal(10)
        $ mc.change_locked_clarity(30)
        the_person "Wow, it feels so hot... God this is naughty... I love it!"
        "[the_person.title] starts to move her chest up and down, stroking your cock."
        call fuck_person(the_person, start_position = tit_fuck, start_object = make_floor(), skip_intro = True, girl_in_charge = False, position_locked = True) from _call_sex_description_myra_tits_reveal_2
        "When you finish, [the_person.possessive_title] stands up."
        $ the_person.draw_person()
        mc.name "Damn, that was amazing. We'll have to do this again sometime."
        the_person "That was surprisingly pleasant. I wouldn't mind doing it again!"

    $ remove_myra_bigger_tits_serum_action()
    $ the_person.apply_planned_outfit()
    $ clear_scene()
    "You quietly exit the stock room. "
    return

label myra_blowjob_training_intro_label(the_person):      #Myra ask for blowjob training after sessions with Alexia. Requires 140 obedience
    $ the_person.draw_person()
    if myra.event_triggers_dict.get("blowjob_train_start", False):  #This has already run once.
        return
    $ myra.event_triggers_dict["blowjob_train_start"] = True
    "When you step into the gaming cafe, you see [the_person.title], at her usual spot at the main desk."
    "She spots you when you walk in. She smiles so you decide to go say hello."
    mc.name "Good day [the_person.title]."
    the_person "Hey."
    "[the_person.possessive_title] looks around, then says to you in a hushed voice."
    if myra_alexia_teamup_scene.get_stage() >= 2:
        the_person "So... how'd you enjoy the other night with [alexia.fname]? That was pretty wild, huh?"
        mc.name "Yeah, but definitely in a good way."
        the_person "Yeah, you WOULD say that..."
        "[the_person.title] sticks her tongue into the side of her cheek, and briefly mimics a blowjob motion."
        $ mc.change_locked_clarity(10)
        mc.name "Oh come on, don't pretend like you didn't have a good time too."
        the_person "The gaming nights are fun. Hanging with [alexia.fname], hanging out with you..."
        the_person "That doesn't mean I like giving blowjobs though."
        mc.name "That's okay. I'll just throw the game for you next time. [alexia.title] gives way better head anyway."
        $ the_person.draw_person(emotion = "angry")
        $ the_person.change_happiness(-5)
        the_person "What? Are you fucking kidding me? You get head from [alexia.fname] often then?"
        mc.name "What? I mean, it's completely true. Your blowjobs need work."
        "It seems that comparing her to [alexia.possessive_title] has got her feeling competitive. You decide to push the issue."
        the_person "Yeah right. And let me guess, you just happen to be the man to teach me."
        mc.name "I mean, I am your coach. I guess it just depends. Is it a skill you WANT to be better at?"
        mc.name "You might be able to beat [alexia.title] at games, but in the oral skills department, she has you outclassed, hands down."

    else:
        the_person "So... recently we've been hanging out more, and I was just curious about your thoughts on something."
        the_person "I was reading on this message board about girls who refuse to, you know..."
        "[the_person.title] sticks her tongue into the side of her cheek, and briefly mimics a blowjob motion."
        $ mc.change_locked_clarity(10)
        mc.name "Giving blowjobs? It's okay, you can say it out loud, we are both adults."
        the_person "Ugh that's... crude."
        mc.name "What is so crude about it? Blowjobs are amazing."
        if the_person.has_taboo("sucking_cock"):
            mc.name "Why, do you need someone to help you practice your form?"
            $ the_person.draw_person(emotion = "angry")
            $ the_person.change_happiness(-5)
            the_person "Seriously? You want me to practice?"
            mc.name "Why not?"
        else:
            mc.name "Yours are okay though I guess"
            $ the_person.draw_person(emotion = "angry")
            $ the_person.change_happiness(-5)
            the_person "UGH. Of course you would say that."
            mc.name "What? I mean, it's completely true. Your blowjobs need work."
            "It seems that comparing her oral skill to other girls has got her feeling competitive. You decide to push the issue."
        the_person "Yeah right. And let me guess, you just happen to be the man to teach me."
        mc.name "I mean, I am your coach. I guess it just depends. Is it a skill you WANT to be better at?"

    the_person "Yeah right. Fuck off, I've got stuff to do."
    mc.name "Alright. I'm just gonna go play something for a bit."
    $ clear_scene()
    "You step away from the desk. You find a computer and sit down."
    "You aren't sure if that will work or not, but at least it left her thinking about it. Maybe she'll come around to it."
    "You hop on a computer and load up Guild Quest 2. You just play some overland stuff for a bit, your mind thinking about [the_person.title]."
    "After a couple hours, you are just getting ready to get up..."
    $ the_person.draw_person(emotion = "sad")
    the_person "Hey..."
    mc.name "Hey [the_person.title]."
    if myra_alexia_teamup_scene.get_stage() >= 2:
        the_person "Look, I'm sorry I got pissed earlier. Obviously I know that you fool around with [alexia.fname]."
        the_person "She talks about you way too much for things between you two to be just friendly."
        mc.name "Oh... she talks about me a lot?"
        the_person "I... look, I'm not here to talk about her, okay?"
    else:
        the_person "Look, I'm sorry I got pissed earlier. Obviously, we are hardly both young. I'm sure you've got an impressive body count."
        the_person "But I'm not here to talk about other girls... okay?"
    mc.name "Ok... what are you here to talk about?"
    the_person "I was thinking about it a lot. I DO want to get better, I had honestly just written off blowjobs as something OTHER girls do..."
    the_person "But the other night, the atmosphere was just... different? I WANTED to make you feel good. But I felt like I had no idea what I was doing..."
    mc.name "Ah, so you really DO need a coach! Don't worry [the_person.title]. I'm here to help."
    the_person "That's... why did I not see that reaction coming. You are so predictable."
    mc.name "Don't worry, you'll have an up close look at me coming soon."
    the_person "You are such a dumbass."
    mc.name "Alright, let's go find somewhere private."
    the_person "What, like... right now?"
    mc.name "Of course! There's no time like the present."
    the_person "Ummm, maybe we could start like some other..."
    mc.name "Nonsense! I'm your coach, I know what's best. Let's go."
    $ the_person.change_obedience(5)
    $ the_person.draw_person(position = "stand3")
    "You stand up."
    the_person "Umm, I guess there is a stock room where I keep spare computer parts."
    mc.name "Lead the way."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns away and you follow her. She goes into a doorway, down a small hall, and into a small parts room."
    $ the_person.draw_person()
    the_person "Fuck, I can't believe I'm doing this."
    mc.name "Don't worry. I'll help you develop skills that will be useful the rest of your life."
    "[the_person.title] rolls her eyes."
    the_person "So... what now coach?"
    mc.name "Well, first, you need to drop the smart-ass attitude."
    the_person "What? Fuck off, I'm just..."
    if myra_alexia_teamup_scene.get_stage() >= 2:
        mc.name "Let's be honest with each other. We both know WHY you are doing this. You are competitive by nature, and you can't stand the thought that [alexia.title] might be better than you."
    else:
        mc.name "Let's be honest with each other. WE both know WHY you are doing this. You are competitive by nature, and you can't stand the thought that a guy is thinking about some other girl when you're going down on him."
    mc.name "But the most important part about blowjobs has nothing to do with technique. It's all about attitude. Guys can tell when you're forcing it, and it's a big turn-off."
    "For a moment, [the_person.possessive_title] seems shocked at your forceful words. For a second, it seems she is about to tell you to fuck off again, but then she relaxes."
    the_person "I... I DO want to be better..."
    mc.name "That's great, but to get good at blowjobs, you have to WANT to give them. So far, all I can tell is that you are actively avoiding it."
    mc.name "Here's what you need to do. Get on your knees. Take out my cock. And lick it, like you WANT to. You WANT to make it good. You WANT to do anything you can to make me feel good."
    $ the_person.change_obedience(20)
    the_person "Okay..."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(30)
    "Finally, [the_person.possessive_title] gets on her knees in front of you. She undoes your pants and slowly pulls them down with your underwear."
    "She looks a little scared as she looks at your full size."
    the_person "I... I'll never be able to... it's too big!"
    mc.name "You let me worry about working up to handling the whole thing. For now, just lick it."
    the_person "Okay..."
    "You can feel [the_person.title]'s hot breath on your groin as she brings her face right up to it. She sticks out her tongue and runs it up the side a few times."
    mc.name "That's it. Now be honest. Before you met me, how many blowjobs have you given before?"
    the_person "I... don't see how that's relevant to my training..."
    mc.name "Just answer. I'll decide what's relevant."
    "[the_person.possessive_title] sighs."
    the_person "Two."
    mc.name "Really? Haven't had serious boyfriends before?"
    the_person "I have, I just... I was with a guy once who kept begging for blowjobs all the time. I finally gave in and did it once, but..."
    the_person "He... wasn't very gentle. He grabbed me by the hair and just kept..."
    the_person "Honestly, at one point, I thought I was doing to die. I was gagging so hard."
    mc.name "Ahh, I understand now. Don't worry [the_person.title]. We may work up to that point, but I won't do anything like that to you yet."
    the_person "Yeah?"
    "[the_person.possessive_title] takes another long couple of licks up and down your shaft."
    $ mc.change_locked_clarity(30)
    mc.name "Alright, we're gonna take this slow, okay? First, lick all around the tip, then put just the tip in your mouth."
    the_person "Hmm... okay..."
    "[the_person.title]'s hot tongue swirls around your tip a few times. "
    "Finally, her lips open and you feel your tip enter her mouth. She quietly sucks on the tip for several seconds."
    $ mc.change_arousal(10)
    mc.name "Mmm, that's it. That feels really good."
    $ the_person.change_happiness(5)
    "[the_person.possessive_title] looks up at you, and your eyes meet. You can see the beginning of something new. Something passionate. She is ready to learn to service you."
    "And more importantly, she WANTS to."
    $ the_person.break_taboo("sucking_cock")
    "[the_person.title] maintains her eye contact as she starts to bob her head a bit, servicing the tip of your cock."
    $ mc.change_arousal(10)
    $ mc.change_locked_clarity(50)
    mc.name "Why don't you touch yourself a little too."
    "[the_person.title] pops off your dick."
    the_person "What? You want me to masturbate?"
    mc.name "It'll help. Making yourself feel good will help get you in the mood. Plus little moans and gasps are fucking hot."
    $ the_person.draw_person(position = "kneeling1")
    the_person "I guess that makes sense..."
    "[the_person.possessive_title] reaches down and starts to touch herself. You let her go for several seconds."
    mc.name "See? Feels good, right?"
    the_person "Mmm... yeah..."
    mc.name "When you are feeling it, keep going. It'll make it easier."
    the_person "Fuck... mmm.... okay..."
    "[the_person.title] touches herself for several more seconds."
    $ the_person.draw_person(position = "blowjob")
    $ mc.change_locked_clarity(50)
    "When she turns back to your cock, she opens her mouth and starts to suck on it, more eagerly this time. This is shaping up to be a good blowjob session now."
    call fuck_person(the_person, start_position = blowjob, skip_intro = True, position_locked = True, condition = make_condition_blowjob_training()) from _call_sex_description_myra_bj_train_01
    mc.name "That's enough for now."
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "That went way better than you had expected. It seems that you may have flipped a switch in [the_person.possessive_title]'s brain."
    else:
        "Even though you didn't finish, her eagerness shows that she is ready and willing to learn."
        "It seems you may have flipped a switch in [the_person.possessive_title]'s brain."
    #$ myra.increase_sex_skill("Oral")  #Moved to training condition file
    $ add_myra_blowjob_training_progress_action()
    the_person "That actually was a lot more fun than I thought it would be."
    mc.name "Yes. Your enthusiasm helped a lot. I want you to practice your technique for a bit."
    the_person "My... technique?"
    mc.name "Yeah. Another good idea would be to watch some videos. And by that, I mean porn."
    the_person "Right... for science."
    mc.name "Exactly."
    $ the_person.draw_person()
    "[the_person.possessive_title] stands up."
    the_person "I'll umm... keep that in mind..."
    mc.name "Of course, you're always welcome to practice on me also."
    "[the_person.title] rolls her eyes."
    the_person "Ah yes, the white knight offers graciously to let me suck his dick whenever I want. How gallant."
    the_person "I'm going to get cleaned up, but I will keep your offer in mind..."
    mc.name "Alright, I'll see you later."
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    if myra_alexia_teamup_scene.get_stage() >= 2:
        "You step out of the stock room. The gaming nights you are having with [the_person.possessive_title] and [alexia.title] are paying off."
        "A week ago, [the_person.title] would never even consider sucking you off, but now she seems interested, if only to show up her friend."
    else:
        "You step out of the stock room. Getting [the_person.possessive_title] more obedient is starting to pay off."
        "A week ago, she never would have considered sucking you off, but now she seems interested."
    "You make a mental note to check back in with her in a week or so and see how her technique is progressing."
    "She might also be more willing to further her blowjob skills if you increase her obedience as well..."
    call advance_time from _call_advance_myra_bj_train_01_time
    return

label myra_blowjob_training_progress_label(the_person):
    $ the_person.draw_person()
    $ days_passed = myra.string_since_event("myra_bj_train")
    "You step into the gaming cafe. [the_person.possessive_title] notices you when you walk in, and waves you over to the front desk."
    the_person "Hey, quick question. Do you remember [days_passed] when you helped me practicing umm... you know... giving a blowjob?"
    mc.name "Yes, I just so happen to distinctly remember that."
    "[the_person.title] starts to a mumble a bit. You step a little closer to try and hear her better."
    the_person "Well I like... umm have been practicing a bit and was just like... wondering if you would mind letting me have another try."
    "Wow. It seems that [the_person.possessive_title] is eager to get on her knees and practice servicing you some more"
    mc.name "You... want to practice giving blowjobs on me again... am I hearing that correctly?"
    the_person "You fucker... yes. I'm just a little insecure about it and I don't trust anyone else to give me honest feedback, okay?"
    #### Work Zone
    mc.name "Lead the way."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns away and you follow her. She goes into a doorway, down a small hall, and into a small parts room."
    $ the_person.draw_person()
    the_person "Fuck, okay. I'm really nervous about this, but here goes."
    the_person "I swung by the sex shop here in the mall and bought a dildo that is about your size that I've been practicing on."
    if starbuck_is_business_partner():
        "Suddenly, [the_person.title] looks like she remembers something."
        the_person "Actually, while we were chatting, the nice lady running the place there told me to say hi to you?"
        the_person "And that she needs help running freight in the evenings more often..."
        "[the_person.title] shakes her head after she recalls that."
        the_person "Anyway..."
    the_person "I've just about got it so I can take the whole thing. But I know, from experience, practice is way different than the real thing."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets on her knees in front of you. She seems almost excited to get started."
    $ myra.increase_opinion_score("giving blowjobs")
    $ myra.event_triggers_dict["deepthroat_avail"] = True

    $ mc.change_locked_clarity(30)
    "She undoes your pants and slowly pulls them down with your underwear. She gasps when your hard cock springs free."
    $ the_person.change_arousal(10)
    "[the_person.possessive_title] takes it in her hand, and looks like she is just getting ready to get started."
    if not the_person.tits_available:
        mc.name "Hang on. Take your top off. I want something nice to look at while you service me."
        the_person "Ah, you want to check out my tits? I suppose I could be okay with that."
        "She gives you a wink as she takes her top off."
        $ the_person.strip_to_tits(position = "blowjob")
        "Once topless, [the_person.title] takes hold of your cock again."
    "She looks up at you and opens her mouth. Slowly, while making eye contact, her mouth descends around your cock."
    $ mc.change_arousal(10)
    "You feel her tense up a bit and feel your cock hit the back of her throat. She tries going a bit deeper but the suddenly pulls off, gagging slightly."
    the_person "Fuck! God it's so thick..."
    $ mc.change_locked_clarity(30)
    "She looks a little scared as she looks at your full size, but she makes another attempt."
    "At about three quarters in, she stops again, your cock hitting her throat barrier. She tries to push herself past it a couple times but just can't."
    "She pulls off again with a groan."
    the_person "Fuck... god I can't do it..."
    "She gives your cock a couple strokes with her hand while looking up at you..."
    the_person "Hey... could you like... help me?"
    mc.name "Help you how?"
    the_person "I'm so close... this time when I'm almost there can you like, put your hand on my head and just pull a little..."
    mc.name "Hmm, I suppose. Let's see how it goes. If you need to pull off, smack my leg with your right hand."
    the_person "Ahh, okay."
    $ the_person.change_obedience(5)
    "Determined, she opens her mouth and takes your cock again. At three quarters deep, you feel your cock hit the back of her throat again."
    "[the_person.title] looks up at you. Waiting."
    "You put your hand on the back of her head, then slowly add pressure and thrust your hips a bit. After a few seconds of pressure building up, her throat barrier gives way and she swallows your ful length."
    "Your balls on her chin, you let go of her head. Instead of pulling off, she shakes her a head a bit side to side, trying to adjust to having your cock in her throat."
    $ mc.change_arousal(15)
    $ mc.change_locked_clarity(50)
    "Suddenly, she gags and pulls off."
    the_person "Gah! Oh fuck..."
    "She only takes a couple seconds to catch her breath, then opens up and takes you again. She hits her throat barrier, but this time she shakes her head a bit and pushes through it."
    "Your cock is now fully enveloped by [the_person.possessive_title]'s hot mouth and throat. Her tongue starts to rub against the bottom side of it as she throats you."
    "This time, she stays on for several seconds before finally pulling off for air."
    the_person "Gah! Oh fuck. That was the first time I've had a real cock down my throat..."
    mc.name "Yeah? And was it all you hoped?"
    the_person "I was wrong about giving blowjobs... it is amazing. Your cock feels so hot and I can feel it twitching in my throat..."
    "[the_person.title] stops talking and goes down on you again. She stops for just a moment at about three quarters deep, then takes you all the way again."
    $ mc.change_arousal(15)
    $ mc.change_locked_clarity(50)
    "You put your hand on her head again. It's time for a proper deepthroat now."
    call fuck_person(the_person, start_position = deepthroat, skip_intro = True, position_locked = True, condition = make_condition_blowjob_training()) from _call_sex_description_myra_bj_train_02
    $ the_person.draw_person(position = "blowjob")
    $ the_report = _return
    if the_report.get("guy orgasms", 0) > 0:
        "[the_person.possessive_title] successfully drained your balls with her throat. Her training seems to be coming along nicely."
    else:
        "Even though you didn't finish, her eagerness shows that her training is coming along nicely."
        "You'll have to give it a go another time, when you both have more energy."
    mc.name "That was an impressive amount of progress, for such a short amount of time [the_person.title]."
    the_person "Yeah... am I the best you've had now?"
    mc.name "No, but you are definitely close."
    the_person "I... what!?! Are you shitting me?"
    mc.name "Just a bit more practice and you'll be there. When I can grab you by the hair and have my way with your mouth, you'll be there."
    the_person "Can't you just lie? God dammit..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] stands up and turns away from you."
    mc.name "Hey. You trusted me to be honest, and I am. Your skills are great, but your question was if you were the best."
    "She shakes her head."
    the_person "I know. I know. You're right."
    $ the_person.draw_person()
    the_person "Guess I still have some more work to do then."
    mc.name "I look forward to it."
    "[the_person.title] rolls her eyes."
    the_person "Right. I'm sure you do. Now fuck off, I gotta get decent."
    # $ myra.increase_sex_skill("Oral") Moved to condition training file
    $ add_myra_blowjob_training_final_action()
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You step out of the supply closet. Things are definitely moving in the right direction with [the_person.title]'s obedience training."
    "You make a mental note to check back in with her in a week or so and see if she has what it takes to be the best."
    "She might also be more willing to further her deepthroat skills if you increase her obedience as well..."
    call advance_time from _call_advance_myra_bj_train_02_time
    return  #160 Obedience

label myra_blowjob_training_final_label(the_person):
    "It has been a while since your last training session with [the_person.possessive_title]."
    "You step into the gaming cafe. You look to the counter and see her there."
    $ the_person.draw_person()
    "You think about how, just a short time ago, you met the independent gamer girl. Now, you've got her trained into being your personal cock sleeve."
    $ mc.change_locked_clarity(20)
    "Last time you trained her, you made sure she knew what the expectations were. It's time to see if she is ready."
    "You walk over to the counter."
    the_person "Hey [the_person.mc_title]. It's good to see you. Anything I can do for you today?"
    mc.name "You could say that."
    "[the_person.possessive_title] raises an eyebrow. She can tell you have something naughty in mind."
    mc.name "I'm here to check on your progress. I want to see if you can give me the, how did you put it? The best blowjob I've ever had?"
    the_person "Fuck yeah I'm ready. Let's head to the back..."
    $ myra.event_triggers_dict["blowjob_train_finish"] = True

    mc.name "Lead the way."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns away and you follow her. She goes into a doorway, down a small hall, and into a small parts room."
    $ the_person.draw_person()
    the_person "Last night, I managed to take 10 inches with my longest dildo."
    mc.name "That is pretty good, but I think you are underestimating the effect of thrusting on difficulty. Let's find out."
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] gets on her knees in front of you. She seems almost excited to get started."
    $ myra.increase_opinion_score("giving blowjobs")

    $ mc.change_locked_clarity(50)
    "She undoes your pants and slowly pulls them down with your underwear. She gasps when your hard cock springs free."
    $ the_person.change_arousal(10)
    if not the_person.tits_available:
        the_person "Hang on. let me do this really quick..."
        "She gives you a wink as she takes her top off."
        $ the_person.strip_to_tits(position = "blowjob")
    the_person "Alright, I'm ready. Have your way with me."
    "She looks up at you and opens her mouth. You put your hands on the back of her head. You slowly guide her mouth onto your cock and back towards her throat."
    $ mc.change_arousal(10)
    "You feel her tense up a bit and feel your cock hit the back of her throat. You don't bother to stop though, you push your cock through her throat barrier, all the way down."
    $ mc.change_locked_clarity(30)
    "You sigh when you feel your balls resting on her chin. She took your cock like a champ, but you aren't satisfied with just one thrust."
    "She looks up at you, you can see the determination in her eyes."
    $ the_person.change_obedience(5)
    "Holding her by the hair, you pull your hips back and then thrust down her throat. The only sound is some slurping as she throats you easily."
    "[the_person.title] looks up at you. A mischievous smile is on her face."
    "You pull her off for a second and let her get a breath. It is time to see what this slut can do."
    $ mc.change_arousal(15)
    $ mc.change_locked_clarity(50)
    call fuck_person(the_person, start_position = skull_fuck, skip_intro = True, position_locked = True, condition = make_condition_blowjob_training()) from _call_sex_description_myra_bj_train_03
    $ the_person.draw_person(position = "blowjob")

    "It takes [the_person.possessive_title] several seconds to catch her breath."
    mc.name "Damn, you really have gotten good at that.."
    the_person "Yeah... am I the best you've had now?"
    if ophelia_get_special_bj_unlocked():
        "She WAS good... but you can't help but think about a certain salon owner who lacks a gag reflex..."
        mc.name "I would say you are tied. Honestly I don't think blowjobs get any better than that."
    else:
        mc.name "I think so. You have gotten fucking good at that."
    $ the_person.draw_person()
    the_person "Good."
    mc.name "But don't stop now. It takes practice to stay at the top of your game."
    the_person "And I'm sure my wonderful coach will help keep my skills honed."
    mc.name "Of course."
    "[the_person.title] rolls her eyes, but you also see a little smirk. She has learned to enjoy servicing you."
    the_person "Right. I'm sure you do. Now fuck off, I gotta get decent."
    # $ myra.increase_sex_skill("Oral") Moved to condition training file
    $ myra.set_event_day("myra_bj_train")
    $ clear_scene()
    $ the_person.apply_planned_outfit()
    "You step out of the supply closet."
    "You make a mental note. You should try and give her an opportunity to show off her oral skills sometime..."
    call advance_time from _call_advance_myra_bj_train_03_time
    return  #160 Obedience
