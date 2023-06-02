#Testing Comments


init 720 python:

    def Sarah_titles(the_person):
        return the_person.name
    def Sarah_possessive_titles(the_person):
        valid_possessive_titles = [Sarah_titles(the_person)]
        valid_possessive_titles.append("Your childhood friend")
        if the_person.event_triggers_dict.get("try_for_baby", 0) >= 1:
            valid_possessive_titles.append("Your breeding mare")
        return valid_possessive_titles
    def Sarah_player_titles(the_person):
        return mc.name
    Sarah_personality = Personality("Sarah", default_prefix = relaxed_personality.default_prefix,
    common_likes = ["skirts", "small talk", "Fridays", "the weekend", "the colour purple", "makeup", "flirting", "heavy metal music","punk music"],
    common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "showing her ass", "threesomes", "not wearing underwear", "creampies", "bareback sex"],
    common_dislikes = ["the colour pink", "supply work", "conservative outfits", "work uniforms"],
    common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex"],
    titles_function = Sarah_titles, possessive_titles_function = Sarah_possessive_titles, player_titles_function = Sarah_player_titles)





############################
##### Sarah Personality#####
############################
label Sarah_introduction(the_person):  #This shouldn't proc... ever?
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around and looks you up and down."

    $ the_person.set_title("???")
    the_person "Uh, sure? What do you want?"
    mc.name "I know this sounds crazy, but I saw you and just wanted to say hi and get your name."
    "She laughs and crosses her arms."
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Yeah? Well I like the confidence, I'll say that. My name's [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    the_person "And what about you, random stranger? What's your name?"
    return

label Sarah_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh, what do you want?"
    elif the_person.happiness < 90:
        the_person "Hey. Did you need something? I'm sorry I'm having a bit of a rough day."
    else:
        if the_person.sluttiness > 60:
            if the_person.is_highly_fertile:
                the_person "Hello. Need something? I hope so, I know I really need something soon..."
                "She lowers her voice and whispers in your ear."
                the_person "I'm fertile right now."
            elif the_person.event_triggers_dict.get("dating_path", False):
                the_person "Hello babe! I hope you aren't here just to talk."
            elif the_person.obedience > 180:
                the_person "Hello there [the_person.mc_title]. It's good to see you, is there anything I can help you with?"
            else:
                the_person "Hey there [the_person.mc_title]. I was just thinking about some fun things we could do together..."
        else:
            if the_person.obedience > 180:
                the_person "Hello, [the_person.mc_title]."
            else:
                the_person "Hey, how's it going?"
    return

label Sarah_sex_responses(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, I love that rush when you first get started."
        else:
            the_person "Oh... [the_person.mc_title] that feels really good..."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Mmm, keep going [the_person.mc_title]. You are getting me so hot."
        else:
            the_person "That... That feels great [the_person.mc_title]!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if the_person.event_triggers_dict.get("dating_path", False):
                the_person "Oh god, I'm your dirty little slut [the_person.mc_title]! It feels so good!"
            else:
                the_person "The things you do to me, it feel so good [the_person.mc_title]!"
        else:
            the_person "Does it feel as good for you as it does for me? Mmm, it feels so good!"
    else:
        if the_person.sluttiness > 50:
            if the_person.event_triggers_dict.get("dating_path", False):
                the_person "You fuck me so good, I can't imagine being with anyone else. Make me cum baby!"
            elif the_person.relationship == "Single":
                the_person "Fuck! I'm... You're going to make me cum! I want you to make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh god, why am I even with my [so_title]? He doesn't drive me crazy like you do [the_person.mc_title]!"
                the_person "Make me cum my brains out! Screw my [so_title], he's not half the man you are!"
        else:
            if the_person.event_triggers_dict.get("dating_path", False) and the_person.love > 80:
                the_person "Oh my god, [the_person.mc_title], I love you so much, you're gonna make me explode! Don't stop!"
            the_person "Don't stop! You're going to make me cum, don't you dare stop!"

    return
label Sarah_sex_responses_oral(the_person):
    call relaxed_sex_responses_oral(the_person) from _call_Sarah_sex_responses_oral
    return
label Sarah_sex_responses_vaginal(the_person):
    call relaxed_sex_responses_vaginal(the_person) from _call_Sarah_sex_responses_vaginal
    return
label Sarah_sex_responses_anal(the_person):
    call relaxed_sex_responses_anal(the_person) from _call_Sarah_sex_responses_anal
    return
label Sarah_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        if the_person.event_triggers_dict.get("dating_path", False):
            the_person "Oh god, even like this, you still make me cum! I'm cumming [the_person.mc_title]!"
        else:
            the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label Sarah_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label Sarah_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person "Ah! More! I'm going to... Ah! Cum! Fuck!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh god, I'm going to... Oh fuck me! Ah!"
    return

label Sarah_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        the_person "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is wracked with pleasure."
        the_person "Cum!"
    return

label Sarah_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "You picked this out for me? That's all I need to hear. Thanks!"
    else:
        the_person "Hey, thanks. That's a good look, I like it."
    return

label Sarah_clothing_reject(the_person):
    if the_person.obedience > 180:
        the_person "I don't... I'm sorry, but I really don't think I could get away with wearing something like this. I appreciate the thought though."
    else:
        if the_person.sluttiness > 60:
            the_person "Jesus, you didn't leave much to the imagination, did you? I don't think I can wear this."
        else:
            the_person "There's not much of an outfit to this outfit. Thanks for the thought, but there's no way I could wear this."
    return

label Sarah_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "Oh man, I'm a mess. I'll be back in a moment, I'm just going to get cleaned up for you."
    else:
        if the_person.sluttiness > 40:
            the_person "I don't think everyone else would appreciate me going around dressed like this as much as you would. I'll be back in a second, I just want to get cleaned up."
        else:
            the_person "Damn, everything's out of place after that. Wait here a moment, I'm just going to find a mirror and try and look presentable."
    return

label Sarah_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Could we leave my [the_clothing.display_name] on for now, please?"
    elif the_person.obedience < 70:
        the_person "No, no, no, I'll decide when my [the_clothing.display_name] come off, okay?"
    else:
        the_person "Not yet... get me a little warmed up first, okay?"
    return

label Sarah_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.is_highly_fertile:
            the_person "My body is yours to use, [the_person.mc_title]. Just try to cum inside me... it's a good time of the month for that!"
        elif the_person.event_triggers_dict.get("dating_path", False):
            the_person "Yes! Let's go! I'm glad I'm not the only one feeling needy."
        elif the_person.obedience < 70:
            the_person "Let's do it. Once you've had your fill I have a few ideas we could try out."
        else:
            the_person "I was hoping you would suggest that, just thinking about it gets me excited."
    else:
        the_person "You want to give it a try? Okay, let's try it."
    return

label Sarah_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        if the_person.event_triggers_dict.get("dating_path", False):
            the_person "I can't say no to you, can I? I want you to feel good, use me however you want, [the_person.mc_title]!"
        else:
            the_person "God, what have you done to me? I should say no, but... I just want you to use me however you want, [the_person.mc_title]."
    else:
        if the_person.obedience > 180:
            the_person "If that's what you want to do then I will do what you tell me to do."
        else:
            the_person "I shouldn't... but if you want to try it out I'm game. Try everything once, right?"
    return

label Sarah_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet [the_person.mc_title], get me warmed up first."
    else:
        the_person "Wait, I just... I don't think I'm ready for this. I want to fool around, but let's keep it casual."
    return

label Sarah_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "What? I have a [so_title], so you can forget about doing anything like that. Ever."
        "She glares at you, then walks away."
    elif the_person.sluttiness < 20:
        the_person "I'm sorry, what!? No, you've massively misread the situation, get the fuck away from me!"
        "[the_person.title] glares at you and steps back."
    else:
        the_person "What? That's fucking disgusting, I can't believe you'd even suggest that to me!"
        "[the_person.title] glares at you and steps back."
    return

label Sarah_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh, I think I know what you need right now. Let me take care of you."
        else:
            the_person "Right now? Okay, lead the way I guess."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, you're feeling as horny as me then? Come on, let's go."
            "[the_person.title] takes your hand and leads you off to find some place out of the way."
        elif the_person.sluttiness > 10:
            the_person "I know that look you're giving me, I think I know what you want."
        else:
            the_person "[mc.name], I know what you mean... Okay, I can spare a few minutes."
    return

label Sarah_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person "Alright, let's slip away for a few minutes and you can convince me a little more."
        elif the_person.sluttiness < 50:
            the_person "Come on, I know someplace nearby where we can get a few minutes of privacy."
        else:
            the_person "Oh my god. I hope you aren't planning on making me wait [the_person.mc_title], because I don't know if I can!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person "Fuck, let's get this party started!"
            the_person "I hope you don't mind that I've got a [so_title], because I sure as hell don't right now!"
        else:
            the_person "God damn it, you're bad for me [the_person.mc_title]... Come on, we need to go somewhere quiet so my [so_title] doesn't find out about this."
    return

label Sarah_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person "Well, I think you deserve a chance to impress me."
        elif the_person.sluttiness < 50:
            the_person "Mmm, well let's get this party started and see where it goes."
        else:
            the_person "Fuck, I'm glad you're as horny as I am right now. Come on, I can't wait any more!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person "Fuck, you know how to turn me on in ways my [so_title] never can. Come here!"
        else:
            the_person "You're such bad news [the_person.mc_title]... I have a [so_title], but all I can ever think of is you!"
    return

label Sarah_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        the_person "Sorry [the_person.mc_title], I'm not really in the mood to flirt or fool around."
        "[the_person.title] shrugs unapologetically."

    elif the_person.sluttiness < 50:
        the_person "I'll admit it, you're tempting me, but I'm not in the mood to fool around right now. Maybe some other time though, I think we could have a lot of fun together."

    else:
        the_person "Shit, that sounds like a lot of fun [the_person.mc_title], but I'm not feeling it right now. Hang onto that thought and we can fool around some other time."
    return

label Sarah_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "You know that all you have to do is ask and it's all yours."
        else:
            the_person "Thank you [the_person.mc_title], I'm glad you're enjoying the view."

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person "Then why don't you do something about it? Come on, we don't have to tell my [so_title] anything at all, right?"
            "[the_person.title] winks and spins around, giving you a full look at her body."
        else:
            the_person "You're playing with fire [the_person.mc_title]. I've got a [so_title], and I don't think he'd appreciate you flirting with me."
            mc.name "What about you, do you appreciate it?"
            "She gives a coy smiles and shrugs."
            the_person "Maybe I do."

    else:
        if the_person.sluttiness > 50:
            the_person "Then why don't you do something about it? Come on, all you have to do is ask."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Well thank you, play your cards right and maybe you'll get to see a little bit more."
            the_person "You'll have to really impress me though, I have high standards."
    return

label Sarah_flirt_response_low(the_person):
    if sarah_epic_tits_progress() >= 2:  #She has gone through bigger tits story
        the_person "Oh? You like how I look, now that I'm the total package?"
        $ the_person.draw_person(position = "walking_away")
        $ mc.change_locked_clarity(5)
        "[the_person.possessive_title] gives you a quick spin, showing off her body at the same time as her outfit."
        $ the_person.draw_person()
    else:
        the_person "Oh? Thank you [the_person.mc_title]! I'm glad to hear you like the way I look."
        the_person "I'm not sure why you feel that way though, I'm not wearing anything special."
        $ mc.change_locked_clarity(5)
    mc.name "Your body is fantastic, and the outfit is the icing on the cake."
    "She smiles and laughs."
    the_person "Ah, so you are resorting to flattery then? Your kind words are noted, [the_person.mc_title]!"
    return

label Sarah_flirt_response_mid(the_person):
    if  the_person.relationship != "Single": # She is taken
        the_person "Thank you [the_person.mc_title], but you know you shouldn't be saying that."
        mc.name "Why not? You're hot and I'm just trying to give you a compliment."
        the_person "Thank you, but I have a boyfriend. You know this."
        "She sighs and looks away from you for a moment."
        the_person "I... guess it's still nice to hear though. It's been a while since my boyfriend said I was hot."
        mc.name "Well I'm happy to tell you that you are very, very hot [the_person.title]."
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title] smiles and shrugs."
        the_person "Thanks. It means a lot to hear that from my childhood friend."
    elif the_person.effective_sluttiness("underwear_nudity") < 20:
        the_person "I know we are childhood friends, and obviously I want you to be honest with me, but I'm not sure it's right for you to say stuff like that."
        mc.name "Like what? That you're hot?"
        the_person "I guess I'm just not used to hearing the guy I used to play hide and seek with when I was little call me \"hot\"."
        mc.name "Well I suppose you'd better get used to it, since it's true and I'm not going to stop reminding you anytime soon."
        $ mc.change_locked_clarity(10)
        "[the_person.title] rolls her eyes at you, but you also notice the corner of her mouth turn up in a slight smile."
        the_person "Thanks Romeo, though I will admit it is nice to hear."

    else:
        the_person "Buttering me up again, are you?"
        the_person "You know, with the way you talk about me, a girl could get the wrong idea about what your intentions might be..."
        "[the_person.possessive_title] smiles and runs her hands down her hips. She hesitates for a moment, then turns around and pats her ass."
        $ the_person.draw_person(position = "back_peek")
        the_person "What exactly are your intentions, [the_person.mc_title]? You seem to have a hard time taking your eyes off of me..."
        $ mc.change_locked_clarity(10)
        "You zone out for a second, checking out [the_person.title]'s shapely hind end."
        $ the_person.draw_person()
        "She turns back and giggles."
        if sarah_epic_tits_progress() >= 2:
            the_person "Tongue tied? That's okay, I've been having that effect on a lot of guys lately."
        mc.name "What can I say? Your body is hypnotizing."
    return

label Sarah_flirt_response_high(the_person):
    if mc.location.person_count == 1: #If you are alone she'll flirt with you
        if the_person.effective_sluttiness("kissing") > (25 - (5*the_person.get_opinion_score("public_sex"))): # High sluttiness flirt
            if the_person.has_taboo("underwear_nudity"):
                the_person "Oh [the_person.mc_title], you're so bad! Do you really want to... see me naked?"
            else:
                the_person "Oh [the_person.mc_title]. You're always trying to get me naked."

            mc.name "You're so beautiful, I always want to see more."
            $ mc.change_locked_clarity(15)
            "She sighs and smiles."
            the_person "Don't worry, I want to get naked for you."

            menu:
                "Kiss her":
                    "You put an arm around [the_person.possessive_title]'s waist and pull her close."

                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You lean in and kiss her. She hesitates for a moment before gently pressing herself against your body."
                    else:
                        "Before you can take the initiative, she pushes herself on her toes and kisses you. You open your mouth and she devours your tongue eagerly."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_sarah_flirt_01
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "Believe me, I want to get naked for you too. Hopefully soon I'll have the time."
                    "[the_person.possessive_title] gives you a little pout."
                    the_person "We make time for what's important. But I understand, running a business is a lot of work."
                    the_person "Hopefully you have time soon!"

        else:
            the_person "Oh [the_person.mc_title]... I don't know if I could go that far."
            mc.name "Relax, we're just joking around. Unless you want to get naked for me?"
            "She laughs and shakes her head in disbelief. You see a glint of mischief in her eye when she asks you."
            the_person "Why don't you get naked first and we'll see what happens?"
            mc.name "You'll pull your phone out and start taking blackmail pictures. There's no way I'm doing that."
            the_person "Me? Blackmail you? [the_person.mc_title] why I would never!"
            if the_person.has_taboo("touching_penis"):
                mc.name "Do you know what would actually be really helpful? I've gotten all worked up, why don't you just touch me with your hand for a bit."
                the_person "You want me... to give you a handjob?"
                mc.name "You would be doing me a big favor..."
                $ the_person.call_dialogue("touching_penis_taboo_break")
                $ the_person.break_taboo("touching_penis")
            else:
                the_person "Ok fine, I've got a better idea. What if I put my hand in your pants and umm, you know, like we did the other day..."
                mc.name "Mmm, I suppose I would be up for that."

            $ mc.change_locked_clarity(15)
            "[the_person.possessive_title] places a hand on your chest and strokes it tenderly."
            "She looks into your eyes as her hand moves lower, running over your abs, down to your waist."
            "Her fingers slide into your pubic hair, then to the side of your cock and between your legs."
            "She runs a finger along the bottom of your shaft, ending at the sensitive spot under your tip."
            "Then she wraps her full hand around it and slides it back down to the base."
            "[the_person.possessive_title] begins to stroke you off with long, deliberate motions."
            call fuck_person(the_person, private = True, start_position = handjob, skip_intro = True) from _call_fuck_sarah_flirt_02
            $ the_person.call_dialogue("sex_review", the_report = _return)
            $ the_person.review_outfit()

    else: #She shushes you and rushes you off somewhere private.
        if the_person.effective_sluttiness() > 25: #She's slutty, but you need to find somewhere private so people don't find out.
            the_person "[the_person.mc_title]..."
            "[the_person.possessive_title] glances around nervously."
            the_person "Take me somewhere private and say something like that again and it might actually happen..."
            menu:
                "Find someplace quiet":
                    mc.name "Then let's find somewhere private. Come on."
                    "You take her hand and start to lead her away. She follows you eagerly."
                    the_person "Wow, I wasn't expecting you to actually do it! This is gonna be fun!"
                    "When you find a quiet spot you pull [the_person.possessive_title] close to you."
                    if the_person.has_taboo("kissing"):
                        $ the_person.call_dialogue("kissing_taboo_break")
                        $ the_person.break_taboo("kissing")
                        "You lean in and kiss her. She hesitates for a moment before gently pressing herself against your body."
                    else:
                        the_person "Oh god... come here [the_person.mc_title]..."
                        "She pushes herself up on her toes to meet your lips as you bring your head down to kiss her."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_sarah_flirt_03
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "I know, I just like to tease you."
                    the_person "Oh, is that so? Well two can play at that game."
                    if sarah_epic_tits_progress() >= 2:
                        $ the_person.draw_person(the_animation = tit_bob)
                        "She checks that nobody else is looking, then grabs her tits and jiggles them for you."
                        the_person "Teasing a lady like me. You should be ashamed of yourself, [the_person.mc_title]!"
                        $ the_person.draw_person()
                    else:
                        "She checks that nobody else is looking, then reaches down and grabs your package. You harden rapidly as she gives it a couple of strokes."
                        the_person "Teasing a lady like me. You should be ashamed of yourself, [the_person.mc_title]!"
                    $ mc.change_locked_clarity(15)
                    mc.name "Jesus woman, you win!"
                    the_person "I'm glad you understand."

        else: #She's not slutty, so she's embarrassed about what you're doing.
            "[the_person.possessive_title] gasps softly and glances around, checking to see if anyone else was listening."
            the_person "[the_person.mc_title], stop joking around! If other people overhear they might get the wrong idea!"
            mc.name "It's fine, nobody heard anything. Besides, who cares if other people know I want to see you naked?"
            $ mc.change_locked_clarity(15)
            "[the_person.possessive_title] gives you a very convincing frown, but she eventually breaks and cracks a smile."
            the_person "I guess, I just wish you would be a little more discrete."
            "She places a gentle hand on your shoulder and kisses you on the cheek."
    return
label Sarah_flirt_response_girlfriend(the_person):
    call relaxed_flirt_response_girlfriend(the_person) from _call_Sarah_flirt_response_girlfriend
    return
label Sarah_flirt_response_affair(the_person):
    call relaxed_flirt_response_affair(the_person) from _call_Sarah_flirt_response_affair
    return
label Sarah_cum_face(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "What do you think? Is this a good look [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person "I hope you had a good time [the_person.mc_title]. It certainly seems like you did."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person "Mmm, that's such a good feeling. Do you think I look cute like this?"
            "[the_person.title] runs her tongue along her lips, then smiles and laughs."
        else:
            the_person "Whew, glad you got that over with. Take a good look while it lasts."
    return

label Sarah_cum_mouth(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Mmm, thank you [the_person.mc_title]."
        else:
            "[the_person.title]'s face grimaces as she tastes your cum in her mouth."
            the_person "Ugh. There, all taken care of [the_person.mc_title]."
    else:
        if the_person.sluttiness > 80:
            the_person "Mmm, you taste great [the_person.mc_title]. Was it nice to watch me take your load in my mouth?"
        else:
            the_person "Ugh, that's such a... unique taste."
    return

label Sarah_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        the_person "Yes! Fill that condom for me [the_person.mc_title]!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Fill me up again and again [the_person.mc_title]! I'm already pregnant!"
            elif the_person.get_opinion_score("creampies") > 0:
                "[the_person.possessive_title] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Yes! Cum inside me [the_person.mc_title]! Mark me with your seed!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    the_person "Yes! Cum inside me and knock me up! Plant that seed as deep as you can!!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                the_person "I'm on the pill, cum wherever you want [the_person.mc_title]!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Ah! Do it!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                the_person "Please pull out! I'm not ready to get pregnant!"

            elif the_person.get_opinion_score("creampies") < 0:
                the_person "Make sure to pull out, you can cum anywhere, just not inside me!"

            else:
                the_person "Ah, really? You should pull out, just in case!"
    return

label Sarah_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
        the_person "Mmm, your cum feels so warm. I wish you weren't wearing a condom; I bet you would feel amazing raw."
    else:
        the_person "Whew... I can feel how warm your cum is through the condom. It feels nice."
    return

label Sarah_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Mmm, another load, right where it belongs..."
            "She sighs happily."

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Mmmm, it's so warm."
                "She sighs happily as you cum inside her."
                the_person "I feel bad for my [so_title], he never makes me feel this good."
            else:
                the_person "Oh fuck, it's so warm. I can feel it filling me up..."
                "She sighs happily as you cum inside her."

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Your cum is so nice and warm..."
                the_person "If you get me pregnant I guess I'll have to tell my [so_title] it's his."
            else:
                if the_person.sex_record.get("Vaginal Creampies", 0) > 10:
                    the_person "You keep cumming inside me over and over... it's only a matter of time until I get pregnant!"
                else:
                    the_person "Mmm, it's so warm... I wonder if it's going to get me pregnant."

        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ah... There it is..."
                the_person "Fuck, I hope you didn't knock me up though. I don't want to have to explain that to my [so_title]."
            else:
                the_person "Oh fuck, there it all is... It's so warm."

    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "No! I told you to pull out! I have a [so_title], what if I got pregnant?"
                the_person "Whatever, I guess it's already done."
            else:
                the_person "[the_person.mc_title]! I told you to pull out! What if I got pregnant."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "Hey, I told you to pull out! I've got an [so_title], you can't be finishing inside me!"

        elif the_person.get_opinion_score("creampies") < 0:
            the_person "Ugh, I told you to pull out! Fuck, you made such a mess..."

        else:
            the_person "Hey, didn't I tell you to pull out?"
            the_person "It's done now, I guess..."


    return

label Sarah_cum_anal(the_person):
    call relaxed_cum_anal(the_person) from _call_Sarah_cum_anal
    return

label Sarah_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!", "God fucking dammit!", "Son of a bitch!", "Mother fucker!", "Whoah!"])
    the_person "[rando]"
    return

label Sarah_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I've got a ton of things I need to get to, could we talk some other time [the_person.mc_title]?"
    else:
        the_person "Hey, I'd love to chat but I have a million things to get done right now. Maybe later?"
    return

label Sarah_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "One sec, I want to take something off."
        else:
            the_person "Ah, I'm wearing way too much right now. One sec!"

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "Why do I bother wearing all this?"
        else:
            the_person "Wait, I want to get a little more naked for you."

    else:
        if the_person.arousal_perc < 50:
            the_person "Give me a second, I'm going to strip something off just. For. You."
        else:
            the_person "Ugh, let me get this off. I want to feel you pressed against every inch of me!"
    return

label Sarah_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person "Ugh, for crying out loud, you two. Get a room or something, nobody wants to see this."
        $ the_person.change_stats(happiness = -2, obedience = -1)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person "Could you two at least keep it down? This is fucking ridiculous."
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze and ignore you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person "You're certainly feeling bold today [the_sex_person.fname]. At least it looks like you're having a good time..."
        $ the_person.change_slut(1)
        "[title] watches for a moment, then turns away while you and [the_sex_person.fname] keep [the_position.verbing]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person "Oh wow that's hot. You don't mind if I watch, do you?"
        $ the_person.change_slut(2)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person "Come on [the_person.mc_title], [the_sex_person.fname] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
    return

label Sarah_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Come on [the_person.mc_title], be rough with me. I can handle it!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "I bet she just wishes she was the one [the_position.verbing] you."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        the_person "Oh god, you need to get a little of this yourself, [the_watcher.fname]!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "[the_watcher.fname], I'm giving him all I can right now. Any more and he's going to break me!"
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Fuck, maybe we should go somewhere a little quieter..."
        $ the_person.change_stats(arousal = -1)
        "[the_person.title] seems uncomfortable with [the_watcher.fname] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.fname]!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 50)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.fname] around."

    return

label Sarah_work_enter_greeting(the_person):
    if the_person.happiness < 80:
        "[the_person.title] glances at you when you enter the room. She scoffs and turns back to her work."

    elif the_person.happiness > 130:
        if the_person.sluttiness > 40:
            the_person "Hey [the_person.mc_title], down here for business or pleasure?"
            "The smile she gives you tells you which one she's hoping for."
        else:
            "[the_person.title] looks up from her work and smiles at you when you enter the room."
            the_person "Hey [the_person.mc_title], it's nice to have you stop by. Let me know if you need anything!"

    else:
        if the_person.sluttiness > 60:
            $ the_person.draw_person(position = "stand4")
            "[the_person.title] walks over to you when you come into the room."
            the_person "Just the person I was hoping would stop by. I'm here if you need anything."
            "She winks and slides a hand down your chest, stomach, and finally your crotch."
            the_person "Anything at all."
        else:
            the_person "Hey [the_person.mc_title]. Need anything?"
    return

label Sarah_date_seduction(the_person):
    $ mc.change_locked_clarity(30)
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but there are a few more things I'd like to do with you. Want to come back to my place and find out what they are?"
            else:
                the_person "You've been a blast [the_person.mc_title]. Want to come back to my place, have a few drinks, and see where things lead?"
        else:
            if the_person.love > 40:
                the_person "Tonight's been amazing [the_person.mc_title], I just don't want to say goodbye. Do you want to come back to my place and have a few drinks?"
            else:
                the_person "This might be crazy, but I had a great time tonight and you make me a little crazy. Do you want to come back to my place and see where things go?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I've had a blast [the_person.mc_title], but I'm not done with you yet. Want to come back to my place?"
                the_person "My [so_title] won't be home until morning, so we would have plenty of time."
            else:
                the_person "This might be crazy, but do you want to come back to have another drink with me?"
                the_person "My [so_title] is stuck at work and I don't want to be left all alone."
        else:
            if the_person.love > 40:
                the_person "You're making me feel crazy [the_person.mc_title]. Do you want to come have a drink at my place?"
                the_person "My [so_title] won't be home until morning, and we have a big bed you could help me warm up."
            else:
                the_person "This is crazy, but would you want to have one last drink at my place? My [so_title] won't be home until morning..."
    return

label Sarah_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You're really done? Fuck [the_person.mc_title], I'm still so horny..."
            else:
                the_person "That's all you wanted? I was prepared to do so much more to you..."
        else:
            if the_person.arousal_perc > 60:
                the_person "Fuck, I'm so horny... you're sure you're finished?"
            else:
                the_person "That was a little bit of fun, I suppose."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "[the_person.mc_title], you got me so turned on..."
            else:
                the_person "I hope you had a good time."
        else:
            if the_person.arousal_perc > 60:
                the_person "Oh god, that was intense..."
            else:
                the_person "Done? Good, nice and quick."
    return


label Sarah_sex_take_control (the_person):
    if the_person.arousal_perc > 60:
        the_person "Ha! That's funny. Get back here, I'm almost done!"
    else:
        the_person "You wish! I'm not done with you yet."
    return

label Sarah_sex_beg_finish(the_person):
    the_person "Wait [the_person.mc_title], I'm going to cum soon and I just really need this... I'll do anything for you, just let me cum!"
    return

## Role Specific Section ##
label Sarah_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person "Well, I've got an idea in mind. It's risky, but I think it could really push our research to a new level."
    mc.name "Go on, I'm interested."
    the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

label Sarah_kissing_taboo_break(the_person):
    if the_person.love >= 20:
        the_person "A kiss? Of course! After all these years, this is like a dream come true..."
    else:
        the_person "Oh! Of course! Just for you [the_person.mc_title]!"
    return
label Sarah_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Are you as excited as I am? I've been imagining your hands on me for years..."
    elif the_person.love >= 20:
        the_person "Do you think we're ready for this? I like you, but it seems like a big step..."
        mc.name "Tell me what you think?"
        "You can see the answer in her eyes before she says anything."
        the_person "I'm ready if you are."
    else:
        the_person "I don't know if I'm ready for this [the_person.mc_title]."
        the_person "We've known each other for so long. You feel more like a brother..."
        mc.name "This doesn't have to mean anything unless we want it to. Just relax and let your body tell you what's right."
    return

label Sarah_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Are you ready? I've wondered what your cock would feel like for years."
        mc.name "I've wondered what your hand would feel like."
        the_person "Well, let's both satisfy the other person's curiosity then!"
    elif the_person.love >= 20:
        the_person "Your cock looks so big. I just want to make it feel good."
    else:
        the_person "Oh my god, look at how hard you've gotten. I didn't think it would be so big."
        mc.name "Go on, give it a touch."
        the_person "I... I don't know if I should."
        mc.name "Why not? It's right there, I certainly don't mind."
        the_person "Fine, but just for a second or two..."
    return

label Sarah_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Do it [the_person.mc_title]. I've been fantasizing about this moment since I hit puberty."
    elif the_person.love >= 20:
        the_person "I'm so nervous [the_person.mc_title]. After all these years... I never imagined this would happen!"
        mc.name "Just take a deep breath and relax. You trust me, right?"
        the_person "Of course. I trust you. I always have."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
    return

label Sarah_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Mhmm? What do you want me to do for you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Do you really want me to try?"
        "You nod and she bites her lip in anticipation."
        the_person "Mmm, okay. I can't wait to hear you moan!"
    elif the_person.love >= 30:
        the_person "I figured this was coming soon."
        mc.name "So..."
        "She gives you a warm smile."
        the_person "You mean a lot to me. I'll do it, just to make you feel good!"
    else:
        the_person "Oh my god, do you really want me to do that?"
        "She laughs nervously and shakes her head."
        the_person "You're crazy! I couldn't..."
        mc.name "Sure you could. Just kneel down and give it a taste."
        the_person "No, I mean what would people think?"
        mc.name "Who's going to know, and why do you care what people think?"
        mc.name "Just suck on it a little, and if you don't like doing it you can stop."
        "She shakes her head again, but you can see her resolve breaking the more she thinks about it."
        the_person "... Fine. I'll do it."
        mc.name "Do what?"
        "She smiles and laughs."
        the_person "You're the worst. I'll suck on your cock, [the_person.mc_title]. Happy?"
        mc.name "Not as happy as I'm about to be, that's for sure."
    return

label Sarah_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "My body is as ready as it's ever going to be."
    elif the_person.love >= 30:
        the_person "I'm not sure if \"ready\" is the right word, but you can keep going."
        the_person "I'm all yours. If you want to do something like that, I'm not going to say no!"
        mc.name "Just relax and enjoy, you'll have a great time."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "Whoa, really?"
            "She laughs nervously, but you see a wave of arousal sweep through her."
            the_person "Alright... You can eat me out if you really want to [the_person.mc_title]."

        else:
            the_person "I knew you wouldn't make me blow you without repaying the favor!"
            the_person "Alright then, you go for it."
        mc.name "Just relax and enjoy."
    return

label Sarah_vaginal_sex_taboo_break(the_person):
        if the_person.effective_sluttiness() >= 60:
            the_person "Oh my god... it's actually happening."
            "She looks at you a bit sheepishly."
            the_person "You don't know how long I've fantasized about finally doing this. Let's do it!"
        elif the_person.love >= 45:
            "[the_person.title] nods eagerly."
            the_person "I'm ready [the_person.mc_title], I'm ready to feel you inside me."
        else:
            if the_person.has_taboo("anal_sex"):
                the_person "So this is it, huh?"
                mc.name "Looks like it. Are you ready?"
                the_person "No... But I don't want you to stop either."
            else:
                "[the_person.title] giggles."
                the_person "This feels so backwards! You've already been in my ass, but now we're doing it properly."
                "She shrugs."
                the_person "At least this time it should be easier for you to fit inside."
        return

label Sarah_anal_sex_taboo_break(the_person):
        if the_person.effective_sluttiness() >= 75:
            "[the_person.title] takes a few deep breaths."
            the_person "Whew, I think I'm ready!"
            the_person "Fuck me in the ass [the_person.mc_title]! Stretch me out and ruin me!"

        elif the_person.love >= 60:
            the_person "I would do anything for you. If you want to put it in there, I'm willing to try!"

        else:
            the_person "Oh my god, you're actually going to do it! Fuck, I hope you fit!"
            mc.name "Don't worry, I'll make it fit."
        return

label Sarah_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "I don't mind, it's not like I could get more pregnant."

    elif the_person.get_opinion_score("bareback sex") > 0:
        the_person "You want to do me bare? That's so hot to hear you say something like that."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so it should be fine. Let's go!"
        elif the_person.get_opinion_score("creampies") > 0:
            the_person "You should probably know, before we start, that I'm not on birth control."
            if the_person.is_highly_fertile:
                the_person "Also... I'm pretty much at peak fertility right now. I'd almost definitely get pregnant."
            mc.name "Do you want me to pull out?"
            "She bites her lip and shakes her head."
            the_person "No, not particularly."
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You'll need to pull out though. The last thing in the world I want is to get knocked up."
        else:
            the_person "I'm not on the pill though. You'll need to pull out so you don't knock me up, got it?"

    elif the_person.love > 60:
        the_person "I want to feel close to you too [the_person.mc_title]."
        if the_person.on_birth_control:
            the_person "I'm on birth control, so you don't need to worry about getting me pregnant."
        elif the_person.get_opinion_score("creampies") > 0:
            the_person "If we're doing this, I don't want you to pull out when you finish either."
            mc.name "Are you on the pill?"
            "She shakes her head."
            the_person "No, but for you I'm okay with that risk."
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You'll need to pull out though. I'm not ready to get pregnant yet, okay?"
        else:
            if the_person.kids == 0:
                the_person "You'll need to pull out though. I don't think either of us want a kid yet, right?"
            else:
                the_person "You'll need to pull out though. I already have enough kids."

    else:
        if the_person.on_birth_control:
            the_person "You don't want to use protection? I'm on birth control, but isn't there still a chance?"
            the_person "As long as you pull out it should be fine, I think."
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You don't want to use protection? I'm not on birth control, what if you get me pregnant?"
            mc.name "I'll pull out. Don't you want our first time to be special?"
            the_person "I do... Fine, just please be careful where you cum."
        else:
            the_person "You don't want to use protection? I'm not on birth control, what if you get me pregnant?"
            mc.name "I'll pull out. Don't you want to know how much better it feels without a condom on?"
            the_person "I do... Okay, you can go in raw. Please be careful where you cum though."
    return

label Sarah_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.get_opinion_score("skimpy outfits") * 5):
        the_person "You want to get a look at my underwear, huh?"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I do. You've got good fashion sense, I bet you wear some cute underwear too."
            the_person "Well, let's get this off and you can check for yourself."
        else:
            mc.name "I do. I've already seen you naked, but I appreciate your fashion sense."
            the_person "Let's get this off then."

    elif the_person.love > 15:
        the_person "You want to see me in my underwear, huh? That's really cute."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Damn right I do. Come on, let's get you out of this..."

        else:
            mc.name "I've already seen you naked, so what's there to hide? Let's get this off..."

    else:
        the_person "But I'll only be in my underwear if I take off my [the_clothing.display_name]."

        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Yeah, that's kind of the point."
            the_person "I get that, but don't you think it's going a little far?"
            mc.name "What's so different between your underwear and your [the_clothing.display_name]? It's all just clothing."
            the_person "I guess... Okay, let's do this before I chicken out!"
        else:
            mc.name "Yeah, that's kind of the point. I've already seen you naked, what's special about your underwear?"
            the_person "I guess you're right. Okay, let's do it!"
    return

label Sarah_bare_tits_taboo_break(the_person, the_clothing):
    if Sarah_has_bigger_tits():
        the_person "Well... I guess you were the one who helped make my bigger tits happen."
        the_person "Okay! I bet you're going to love them!"
        "She shakes her chest for you, jiggling the large tits hidden underneath her [the_clothing.display_name]."
    else:
        the_person "Are you sure you want to see... my chest?"
        mc.name "Well, I want to see ALL of you, but for now I'll settle with your top half."
        the_person "Well... okay. Fuck it! Let's do it!"
    return

label Sarah_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.get_opinion_score("showing her ass") * 5):
        the_person "Ready to see my pussy? Well, what are you waiting for?"

    elif the_person.love > 35:
        the_person "If you take that off my pussy's going to be out, you know."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I know, that was the plan."
            the_person "Well... I guess we both knew where this was going. Okay, go for it."
        else:
            mc.name "You've let me touch it already, so what's the big deal about taking a look?"
            the_person "Nothing, it's just... It feels like a big step, but I trust you."

    else:
        the_person "Wait! If you take that off you'll be able to see my pussy."
        if the_person.has_taboo("touching_vagina"):
            mc.name "That's the point, yeah. What's wrong?"
        else:
            mc.name "You've already let me feel it, so what's the issue?"

        the_person "I... I don't know, I'm just nervous!"
        mc.name "Just take a deep breath and relax. I'm going to get these [the_clothing.display_name] off of you."
    return

label Sarah_facial_cum_taboo_break(the_person):
    return
label Sarah_mouth_cum_taboo_break(the_person):
    return
label Sarah_body_cum_taboo_break(the_person):
    return
label Sarah_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh yes, fill me up with your hot semen."
            the_person "It feels so good when you cum deep inside me, promise me you will do that again."

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I can't believe it... your cum is inside me! Oh god what am I gonna tell my [so_title]..."

            else:
                the_person "Oh my god, you finally filled me up! I can't believe this is finally happening!"

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh my god, fill me up! I don't even let my [so_title] do this to me!"

            else:
                if the_person.is_highly_fertile:
                    the_person "Oh my god, it's inside me! I'm ovulating right now! This is so risky..."
                    "She gets goosebumps and sighs."
                    the_person "... but so worth it. I feels so right inside me..."
                else:
                    the_person "Ah, finally! I've wanted you to put a load inside me for so long! I don't even care that I'm not on the pill!"

        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ah, I should have told you to pull out, but it just feels so good..."
                the_person "We shouldn't do that again though, if I get pregnant I'm going to have to explain it to my [so_title]."

            else:
                the_person "Ah, I really should have told you to pull out... I'm not on the pill..."
                the_person "It's just this once, right? It's probably fine..."

    else:
        if the_person.knows_pregnant:
            the_person "Oh my, well I can't get any more pregnant."
        elif not the_person.on_birth_control:
            the_person "Oh my god, [the_person.mc_title]! Did you really just cum inside me?"
            "She groans unhappily."
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ugh, now what if I get pregnant? I guess I'd have to tell my [so_title] it's his."
            else:
                the_person "Ugh, what if you get me knocked up? I just wanted to have some fun!"
                the_person "Whatever, it's probably fine."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "Hey, I told you to pull out. I don't want to cheat on my [so_title] like this..."
            the_person "I guess it's already done. Just be more careful next time, okay?"

        elif the_person.get_opinion_score("creampies") < 0:
            the_person "I said to pull out! Now look at what you've done, you've made such a mess in me."

        else:
            the_person "Hey, you should have pulled out! I guess just once isn't so bad, but don't make a habit of it."
    return

label Sarah_anal_creampie_taboo_break(the_person):
    return

label Sarah_get_drunk_dialogue(the_person, intoxication_level):
    if intoxication_level < 3: # mostly sober
        if the_person.sluttiness > 60:
            "[the_person.title] is carrying on, talking about a time that she was trying to hookup with a random guy on Tinder but it didn't go well."
            the_person "... So anyway, that's when I decided to start making sure to keep my pubic hair trimmed."
            mc.name "Yeah I bet. To be honest though, I probably would have eaten you out anyway."
            the_person "Yeah right, and risk getting hair in your mouth? Hey, that reminds me of a joke I heard. What do you call a Roman with a hair stuck in his teeth?"
            mc.name "I don't know, what?"
            the_person "A gladiator!"
            "You share a laugh together and continue having your drinks."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person "... So anyway, I still can't believe I didn't realize what was going on. That man can go fuck himself!"
            mc.name "Well, I for one am glad that they let you go, or it is likely we never would have reconnected."
            the_person "I mean... that's true! I guess everything happens for a reason?"

    elif intoxication_level < 5: # drunk
        if the_person.sluttiness > 60:
            "[the_person.title] is carrying on. She's had a few drinks and is starting to get pretty obvious, flirting with you."
            the_person "... So anyway, that's why I'm banned from the weekly wine tasting. They kept saying to spit it out, but I always swallow."
            mc.name "Always?"
            the_person "Don't believe me?"
            $ play_swallow_sound()
            "[the_person.possessive_title] takes a deep sip of her drink, then makes a show, tilting her head back and swallowing it all with a loud gulp."
            the_person "The defense declares this evidence to be called exhibit A... maybe later I can show you exhibit D."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person "... So anyway, I still can't believe I didn't realize what was going on. That man can go fuck himself!"
            mc.name "Well, I for one am glad that they let you go, or it is likely we never would have reconnected."
            the_person "I mean... that's true! I guess everything happens for a reason?"

    else:   #Absolutely wasted
        if the_person.sluttiness > 60:
            "[the_person.title] is wasted. She's trying to flirt with you, but can hardly get through her pick up lines."
            mc.name "You doing okay over there?"
            the_person "Me? Ummm... OF COURSE. Heyyyy, are you a candle?"
            mc.name "Not exactly..."
            the_person "BECAUSE I WOULD TOTALLY SUCK YOU OFF."
            mc.name "You mean... blow me?"
            the_person "That'sh what I said!"
            "You make a mental note that it's probably better to get her a water next instead of another drink."
        else:
            "[the_person.title] is carrying on, talking about her time at her internship, before you hired her."
            the_person "I mean, there were a couple cute dudesh there... and girlsh too if I'm honest..."
            the_person "But what ish going on now... I mean wow there issh sum incredible ass in your company!"
            mc.name "Yeah, I really enjoy the company and the employees."
            the_person "No kidding! Ugh my head hurtsss."
            "You make a mental note that it's probably better to get her a water next instead of another drink."

    return
