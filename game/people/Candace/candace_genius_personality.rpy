### PERSONALITY CHARACTERISTICS ###
init 720:
    python:
        def genius_titles(the_person):
            if the_person.love < 20:
                return "Dr." + the_person.last_name #If she doesn't like you she's much more formal.
            else:
                return the_person.name
        def genius_possessive_titles(the_person):
            return genius_titles(the_person) #If we don't have a special possessive just use their normal title.
        def genius_player_titles(the_person):
            return mc.name

        genius_personality = Personality("genius", default_prefix = relaxed_personality.default_prefix,
        common_likes = ["pants", "the weekend", "small talk", "the colour pink", "flirting","punk music","pop music"],
        common_sexy_likes = ["missionary style sex", "kissing", "masturbating", "being submissive", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour yellow", "work uniforms"],
        common_sexy_dislikes = ["taking control", "doggy style sex", "showing her tits", "showing her ass", "bareback sex", "creampies"],
        titles_function = genius_titles, possessive_titles_function = genius_possessive_titles, player_titles_function = genius_player_titles)



### DIALOGUE ###
label genius_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person "I guess? What do you need?"
    mc.name "I know this is strange, but I saw you and I just needed to know your name."
    "She laughs and blushes."
    the_person "Really? You're just saying that to impress me, aren't you."
    mc.name "Really, I really just wanted to talk to you."
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Well fine, my name is [formatted_title]. It's nice to meet you..."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    "She waits expectantly for you to introduce yourself."
    return

label genius_greetings(the_person):
    if the_person.love < 0:
        the_person "Are you bugging me for a reason?"
    elif the_person.happiness < 90:
        the_person "I'm pretty busy. Did you need something?"
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title], it's always good to see you."
            else:
                the_person "Hey there, you're looking good today!"
        else:
            if the_person.obedience > 180:
                the_person "Hello [the_person.mc_title]. What can I do for you?"
            else:
                the_person "Hello!"
    return

label genius_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm... This is a great warmup."
        else:
            the_person "Mmmm... That feels nice."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Oh wow you are hitting all the right places."
            "She purrs warmly."
        else:
            the_person "Oh my god..."
            "It seems like she's trying not to moan too loudly."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if the_person.wearing_panties:
                the_person "I think it's about time we get naked and get down to business."
            elif the_person.vagina_available:
                the_person "I'm sure you've already observed this, but I think it's time to get down to business."
            else:
                the_person "Oh god, I'm getting so hot. You'd better get me out of these clothes soon."
        else:
            the_person "Mmm, this feels amazing [the_person.mc_title]."

    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Oh god, I'm gonna cum soon if you keep going!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I wish my [so_title] knew how to touch me like this. You're going to make me cum!"
        else:
            the_person "Oh god... I think I might cum soon!"

    return

label genius_sex_responses_oral(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "It's time to put that tongue of yours to work [the_person.mc_title]... Ah..."
        else:
            the_person "Oh wow... that's... Mph!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Mmm, I expected it to be good, but I didn't think it would be THIS good..."
        else:
            the_person "That... that feels so good [the_person.mc_title]... So fucking good."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "God, your tongue feels so good!"

        else:
            "You're so good at that... Fuck, it's starting to drive me crazy!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Keep going [the_person.mc_title], you're going to get me to cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "My [so_title] never does this for me any more... I feel horrible, but I need this so badly!"
        else:
            the_person "Oh no... Oh god, you're going to make me..."
            the_person "Cum!"

    return

label genius_sex_responses_vaginal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, your cock feels so good when it first goes in."
        else:
            the_person "Oh my god... Ah..."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Keep fucking me [the_person.mc_title]! My body is just getting warmed up!"
        else:
            the_person "Oh my god, that feeling..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Ah, fuck me [the_person.mc_title]! Give me that big cock!"

        else:
            "[the_person.possessive_title] mumbles softly to herself."
            the_person "Fuck... Oh fuck... My pussy..."
    else:
        the_person "Oh god, I'm gonna cum all over that amazing cock of yours!"

    return

label genius_sex_responses_anal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Oh fuck, you feel even bigger in my ass!"
        else:
            the_person "Fuck, it feels so big... That's all of it, right? I can't take any more!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Fuck my ass [the_person.mc_title], I can take it!"
        else:
            the_person "Oh fuck, my poor ass..."
            "Her groan is a mixture of pain and pleasure."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "That's it! Fuck that nasty hole!"
            else:
                the_person "That's it! Fuck my poor little hole raw!"
        else:
            "[the_person.title] bites down on her lip and growls defiantly."
            the_person "Oh fuck... Fuck you're big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Oh god, keep going! Stuff my ass and make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I never let my [so_title] do this, you know? My tight ass is only for you!"
        else:
            the_person "I can't..."
            "She struggles to catch her breath."
            the_person "... I can't believe you might make me cum!"
    return


label genius_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh fuck [the_person.mc_title] I'm cumming!!!"
    else:
        the_person "Mmmmhm!"
    return

label genius_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh fuck! Oh fuck, make me cum [the_person.mc_title]!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh my god, I'm going to cum. I'm going to cum!"
        "She closes her eyes and squeals with pleasure."
    return

label genius_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person "Fuck your cock is so good [the_person.mc_title], I'm cumming!!!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Ah! I'm cumming! Oh fuck! Ah!"
    return

label genius_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person "[the_person.mc_title] I'm cumming! Oh fuck it's so good!"
    else:
        the_person "Oh fuck, I think... I think I'm going to cum!"
    return

label genius_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person "Oh, it's cute! Thanks, [the_person.mc_title]!"
    return

label genius_clothing_reject(the_person):
    if the_person.obedience > 180:
        the_person "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
    else:
        if the_person.sluttiness > 60:
            the_person "Wow. I'm usually up for anything but I think that's going too far."
        else:
            the_person "Sorry, I need clothes that will cover a little bit more."
    return

label genius_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "I'm sorry [the_person.mc_title], I'm feeling a little self-conscious. I'll go and get cleaned up so I'm presentable again."
    else:
        if the_person.sluttiness > 40:
            the_person "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
        else:
            the_person "What a wonderful mess we made! I'll be back in a moment, I'm going to go get cleaned up."
    return

label genius_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I'm sorry, but we need to leave my [the_clothing.display_name] on for now. Okay?"
    elif the_person.obedience < 70:
        the_person "Slow down there, I'll decide when to take off my [the_clothing.display_name]."
    else:
        the_person "I think that my [the_clothing.display_name] should stay where it is for now."
    return

label genius_strip_obedience_accept(the_person, the_clothing, strip_type = "Full"):
    "[the_person.title] speaks up meekly as you start to move her [the_clothing.display_name]."
    if the_person.obedience > 180:
        the_person "Maybe I should... Sorry, never mind."
    else:
        the_person "Wait, I don't know about this..."
    return

label genius_grope_body_reject(the_person):
    if the_person.effective_sluttiness("touching_body") < 5: #Fail point for touching shoulder
        "[the_person.possessive_title] steps back, then laughs awkwardly."
        the_person "Hey, sorry. We don't need to be that friendly, okay?"
        mc.name "Oh yeah, of course."
        "She gives you another awkward smile and stays a little further away."
    else: #Fail point for touching waist
        "[the_person.possessive_title] shifts awkwardly, trying to pull away from your hand."
        the_person "Hey, can you move your hand? It's no big deal, I'm just not super comfortable with it."
        "You pull your hands back and nod apologetically."
        mc.name "Of course, sorry."
        the_person "Don't worry about it, it's no big deal..."
        "She doesn't say anything more, but she still seems uncomfortable with the situation."
    return

label genius_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "That is an excellent suggestion!"
        else:
            the_person "Mmm, you have a dirty mind [the_person.mc_title]. I can't wait to see how you use it!"
    else:
        the_person "I like that plan, [the_person.mc_title]."
    return

label genius_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh god [the_person.mc_title], I should really say no... But I just can't say no to you."
    else:
        if the_person.obedience > 180:
            the_person "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person "I... Okay, if you really want to, let's give it a try."
    return

label genius_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
    else:
        the_person "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
    return

label genius_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "Wait, what? I have a [so_title], what did you think we were going to be doing?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person "What the fuck do you think you're doing, that's disgusting!"
        the_person "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label genius_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Yes [the_person.mc_title]? Do you need help relieving some stress?"
        else:
            the_person "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.sluttiness > 10:
            the_person "Oh, do you see something you like?"
        else:
            the_person "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label genius_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
        elif the_person.sluttiness < 50:
            the_person "Come on, let's go find someplace quiet where we won't be interrupted."
        else:
            the_person "If you want to sneak off that's fine, or if you want to we can just go at it right here!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person "No point wasting any time, right? I hope my [so_title] won't be too jealous."
        else:
            the_person "I guess we could sneak away for a few minutes, but we have to make sure my [so_title] doesn't find out what we're doing."
    return

label genius_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 20:
            the_person "Well, there's nobody around to stop us..."
        elif the_person.sluttiness < 50:
            the_person "Mmm, I love it when you get ideas like this. Let's get to it!"
        else:
            the_person "Oh [the_person.mc_title], you know I was thinking the same thing!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 50:
            the_person "Don't make me wait then [the_person.mc_title]!"
        else:
            the_person "This is so dumb, I have a [so_title], I shouldn't be doing this..."
            "It's clear she wants to do it anyways."
    return

label genius_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.title] blushes and looks away from you awkwardly."
        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."

    elif the_person.sluttiness < 50:
        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
        "[the_person.title] smiles and gives you a wink."

    else:
        the_person "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
    return

label genius_flirt_response(the_person):

    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person "Thank you for the compliment, [the_person.mc_title]."
    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that though, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person "I have a [so_title], you really shouldn't be talking to me like that..."
            "She seems more worried about being caught than flirting with you."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peek."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label genius_flirt_response_low(the_person):
    if the_person.is_wearing_uniform and the_person.is_employee:
        if the_person.judge_outfit(the_person.outfit):
            #She's in uniform and likes how it looks.
            the_person "Thanks, [the_person.mc_title]. I like these uniforms too. Did you design them yourself?"
            mc.name "I did."
            the_person "Amazing! I think you have a good eye for fashion."
            mc.name "It's easy when I have such good models for it all."
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title] smiles and laughs self-consciously."
        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.vagina_visible:
                # Her pussy is on display.
                the_person "Thanks, but I really wish this uniform covered, well, anything."
                the_person "I know it's company policy, but it's a little... breezy."
                mc.name "It would be a shame to cover up such a beautiful body though."
                $ mc.change_locked_clarity(5)
                "[the_person.possessive_title] blushes and looks away."

            elif the_person.tits_visible:
                # Her tits are out
                if the_person.has_large_tits:
                    the_person "Thanks, but I really wish my uniform included a bra."
                    the_person "I know most men don't think about it, but I could use some support for my [the_person.tits_description]."
                else:
                    the_person "Thanks, but I really wish my uniform included an actual top."
                    the_person "When the AC is running my nipples could probably cut glass!"
                mc.name "It might be a little uncomfortable, but you look incredible in it."
                $ mc.change_locked_clarity(5)
                the_person "I better, I certainly wouldn't be wearing this if it wasn't required!"

            elif the_person.underwear_visible:
                # Her underwear is visible.
                the_person "Thanks, I just wish this uniform kept me a little more covered. It feels like I'm barely wearing anything."
                mc.name "I know it's a little unconventional, but you look fantastic in it. It's a perfect fit for you."
                $ mc.change_locked_clarity(5)
                "[the_person.possessive_title] smiles and blushes."
                the_person "That's good. I guess it's company policy for a reason."
            else:
                # It's just generally slutty.
                the_person "Thanks. It's not the kind of thing I would normally wear, but I guess it's company policy for a reason."
                mc.name "Well you wear it like a natural. I can't think of anyone it would look better on."
                $ mc.change_locked_clarity(5)
                "[the_person.possessive_title] smiles and blushes."

    else:
        #She's in her own outfit.
        the_person "Thank you, I thought it looked cute too."
        $ mc.change_locked_clarity(5)
        "[the_person.possessive_title] turns to give you a side on look of her and smiles at you."
    return

label genius_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            the_person "Wow [the_person.mc_title], complimenting your own choice in uniform?"
            if the_person.tits_visible:
                the_person "I'm sure my boobs aren't out by accident. Not that I mind..."
                "She jiggles and wiggles her shoulders, jiggling her breasts for you."
            else:
                $ the_person.draw_person(position = "back_peek")
                the_person "Not that I mind..."
                "She gives you a full spin, letting you look at her from every angle."
                $ the_person.draw_person()
            $ mc.change_locked_clarity(10)
            mc.name "I might have picked it out, but you're the one making it look so good."
            "[the_person.possessive_title] smiles, blushing a little from the compliment."
            the_person "Maybe sometime we could go shopping again and I could help you pick something new out for the uniforms..."

        else:
            the_person "I think it shows off a little too much!"
            if the_person.vagina_visible:
                the_person "Look at me, you can practically see everything!"
                the_person "No offence, but this uniform makes me look like a whore."
            elif the_person.tits_visible:
                the_person "My boobs are just hanging out, for goodness sakes!"
                the_person "No offence, but your uniform makes me look like a slut."
            else:
                the_person "No offence, but this uniform feels a little inappropriate."
            mc.name "I understand, but it's important for the business."
            the_person "You and I both know that's bullshit, but I'll go along with it for now."
            $ mc.change_locked_clarity(10)
            "[the_person.possessive_title] gives you an uncomfortable smile."

    else:
        if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
            "[the_person.possessive_title] smiles."
            the_person "[the_person.mc_title], you're so bad! What if someone heard you?"
            mc.name "They'd probably agree. You're a sexy looking lady."
            "[the_person.possessive_title] blushes."
            $ mc.change_locked_clarity(10)
            the_person "Well I'm glad you like it. And I'm glad you like me."

        else:
            the_person "Well thank you. I thought it looked pretty cute when I picked it out."
            the_person "Do you want a better look?"
            mc.name "Of course I do."
            $ the_person.draw_person(position = "back_peek")
            the_person "Do you think my ass looks good in it?"
            "She wiggles her hips for you, just a little."
            $ mc.change_locked_clarity(10)
            mc.name "I think it looks great, I wish I could see some more of it."
            $ the_person.draw_person()
            the_person "I'm sure you do. Maybe if you take me to dinner first."
    return

label genius_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.get_opinion_score("public_sex"))):
        # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Not very high, unless we can find someplace quiet."
        menu:
            "Find someplace quiet":
                mc.name "Alright, let's find somewhere quiet then."
                the_person "Oh! I was teasing, but if you're up for it..."
                "You take [the_person.possessive_title]'s hand and lead her away. She follows you happily."
                "After searching for a couple of minutes you find a quiet space with just the two of you."
                the_person "Well... What did you want me all alone for?"
                $ the_person.draw_person(position = "kissing")
                "She steps close to you and puts her arms around your waist. She brings her face close to yours."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_genius_47
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm a patient man, I can wait until we have some privacy. It's probably for the best; you might get a little loud."
                "[the_person.possessive_title] blushes and places her hand on your shoulder, massaging your muscles."
                the_person "Confident, huh? Maybe if you take me out to dinner you'll get your chance at some privacy."

    else:
        # She wants to kiss you, leading to other things.
        if mc.location.person_count == 1:
            #She's shy about the whole thing.
            "She looks around."
            the_person "[the_person.mc_title], it's just us here."
            mc.name "So you're saying my chances are good?"
            $ the_person.draw_person(position = "kissing")
            $ mc.change_locked_clarity(15)
            "She takes a step closer to you and puts her arms around your waist, bringing her face close to yours."
            the_person "They could certainly be worse. Let's just... see where things go."

        else:
            #She's into turning you on.
            if the_person.has_large_tits:
                $ the_person.draw_person(the_animation = tit_bob)
                "[the_person.possessive_title] smiles mischievously at you and bounces her [the_person.tits_description] up and down."
                the_person "Interested in getting a closer look at these girls?"
            else:
                "[the_person.possessive_title] smiles mischievously and wiggles her hips."
            $ mc.change_locked_clarity(15)
            the_person "Maybe we can... fool around a little? Does that sound fun?"
            $ the_person.draw_person()

        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_genius_48
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I wish we could, but I'll need to take a rain check."
                "[the_person.title] pouts and steps back, disappointed."
                $ the_person.draw_person()
                mc.name "Don't worry, we'll get there soon enough. I just want to wait for the right time."
                #TODO: There should be boyfriend/family specific variants here like "Right, what was I even thinking? I don't know what came over me."
                the_person "Right. Sure."
                "She tries to hide it, but you can tell she's a little disappointed."
    return

label genius_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.get_opinion_score("public_sex"))):
            # Not very slutty, so she wants to find somewhere private
            the_person "Oh [the_person.mc_title], you're so sweet!"
            "She leans in and kisses you on the cheek a few times. When she leans back she glances around the room and blushes."
            the_person "Do you want to find someplace more private so I can kiss you somewhere else?"
            menu:
                "Find someplace quiet":
                    mc.name "That sounds fun, come on, let's go."
                    "[the_person.title] follows you eagerly as you lead her away."
                    "After a few minutes of searching you find a quiet spot and put an arm around [the_person.possessive_title]."
                    "She sighs happily as you pull her close and kiss her. She puts her arms around you and hugs you tight, opening her lips for you."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_genius_71
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "That's depends on what you're going to kiss. I've got a few suggestions..."
                    "She laughs and shakes her head."
                    the_person "I think I know what you're going to suggest. That's going to have to wait until later."

        else:
            the_person "Oh [the_person.mc_title], you're so sweet. Come on, kiss me!"
            "She leans in and kisses you on the lips, then leans back and smiles."
            menu:
                "Make out":
                    "You put your hand on the back of her neck and pull her close again, kissing her slowly and sensually."
                    "She sighs happily and leans her body against you, clearly unworried about anyone else around."
                    call fuck_person(the_person, start_position = kissing, private = False, skip_intro = True) from _call_fuck_genius_72
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "So, is there anything else you want to kiss? I've got some suggestions..."
                    if the_person.effective_sluttiness("sucking_cock") >= 60 or the_person.get_opinion_score("giving blowjobs") > 0:
                        the_person "Uh huh? I think I know what you're thinking about."
                        $ mc.change_locked_clarity(10)
                        "She reaches down and cups your crotch, rubbing it gently while looking into your eyes."
                        the_person "I think I could make that happen, if we have some time alone."
                        mc.name "Next time we're alone I'll hold you to that promise."
                        "[the_person.possessive_title] massages your cock, then smiles and lets go."
                        the_person "I'm looking forward to it."

                    else:
                        "She blushes and shakes her head bashfully."
                        the_person "Oh my god, you're so predictable! Well..."
                        "She leans close and whispers into your ear."
                        $ mc.change_locked_clarity(10)
                        the_person "Maybe if you can get us alone I can take a few requests..."
                        "[the_person.possessive_title] nibbles at your ear, then steps back and smiles happily."
    else:
        # You're alone, so she's open to fooling around.
        the_person "Oh, you! Come here, I want to kiss you!"
        $ the_person.draw_person(position = "kissing")
        "She puts her arms around you and leans in, quickly kissing you a few times on the lips."
        "When she's finished kissing you she rests her head on your shoulder and sighs happily."
        the_person "This is so nice..."
        menu:
            "Kiss her":
                "You place a gentle hand on her chin and raise her lips back to yours."
                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "This time when you kiss her it's slow and sensual. You hear her sigh happily, and she presses her body against yours."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_genius_73
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You place your hands around her and hold her close. You run one hand down her back and rest it on her ass, massaging it gently."
                the_person "Mmm... Can we just stay like this for a moment?"
                mc.name "Of course."
                $ mc.change_locked_clarity(10)
                "You hold [the_person.possessive_title] for a few minutes in silence."
                $ the_person.draw_person()
                "She finally breaks the hug steps back."
                the_person "Maybe next time we can... do some more kissing? I think I'd like that."
                mc.name "I'd like that too."
                "She smiles and blushes."
    return

label genius_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    $ so_title = SO_relationship_to_title(the_person.relationship) # "husband", "boyfriend", etc.
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.get_opinion_score("cheating on men") *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            the_person "Am I really? Haha, well..."
            "She takes your hand and looks around before leaning close and whispering in your ear."
            the_person "Do you want to take me somewhere private and show me all those naughty things you want to do?"
            menu:
                "Find someplace quiet":
                    mc.name "I do, follow me."
                    "You lead [the_person.possessive_title] away. After a few minutes of searching you manage to find a quiet spot."
                    the_person "So, where do we start?"
                    "You put your arm around her waist and rest your hand on her ass as you lean in and kiss her."
                    "She presses her body enthusiastically against you and returns your kiss with just as much excitement."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_genius_74
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "You're that easy, huh? I drop one complement and you're ready to get on your knees."
                    $ mc.change_locked_clarity(10)
                    "She laughs quietly and shrugs."
                    the_person "I'm only this easy for you [the_person.mc_title]. You've turned me into such a little slut."
                    mc.name "Well you're going to have to wait a little while until I have the time to give you the attention you deserve."
                    the_person "Okay, just don't make me wait too long."

        else: #She's shy or nervous about being discovered
            the_person "[the_person.mc_title]! Don't say things like that when there are people around!"
            "She glances around nervously. She gives a relieved sigh when it's clear nobody else is close enough to overhear you."
            the_person "Sorry, I just don't want my [so_title] to hear any rumours about us. I don't know what I'd do if he found out."
            mc.name "Relax, I wouldn't do anything that would get you in trouble."
            $ mc.change_locked_clarity(10)
            "She laughs and shakes her head."
            the_person "Obviously that's not true. Just being together might get me in trouble. It's still worth it though..."
            "[the_person.title] runs her hand along your arm, feeling your muscles through your shirt."
            the_person "When we've got some time alone we can have some fun, okay? Just hold on until then."
            mc.name "Okay, I think I can manage that."
    else:
        # the_person "Yeah? Well there's nobody around, and I'm not going to stop you."
        "[the_person.title] smiles and laughs, running a hand along your chest."
        the_person "You're pretty good looking too. I hope I'm not getting you too excited..."
        "Her hand runs lower, over your abs and down to your crotch. She teases your cock through your pants."
        menu:
            "Make out":
                mc.name "You are, and you're going to have to take responsibility for that."
                "You put your arm around her waist, resting your hand on her ass, and pull her into an intense kiss."
                "She leans into you eagerly, returning the kiss with just as much enthusiasm."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_genius_75
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "You're always exciting, but I think I'll be able to hold out for a little while longer."
                $ mc.change_locked_clarity(10)
                "You put your arm around her waist and grab her ass, massaging it as you talk."
                mc.name "But you should know, the next time I get you alone I'm going to pay you back for all this teasing."
                the_person "Yeah? Well now you've got me excited!"
                $ play_spank_sound()
                "You give her butt a hard slap and let her go."
    return

label genius_cum_face(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Mmm, did you know that cum doesn't just taste good, it's good for the skin too?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person "Mmm, it feels so hot on my face, and it's good for the skin too!"
        else:
            the_person "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label genius_cum_mouth(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Wow, that was an above average size load [the_person.mc_title]. Thank you!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            the_person "And it's so full of proteins and vitamins too..."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person "Bleh, I don't know if I'll ever get used to that."
    return

label genius_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom: #TODO: All of the cum-drunk stuff
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "I'm already pregnant, why are we even bothering with a condom?"
                the_person "Take it off and cum inside my pussy, just like you did when you knocked me up!"
            elif the_person.on_birth_control:
                the_person "You are? Do..."
                "She moans, almost desperately."
                the_person "... Do you want to cum inside me? Just take the condom off, I don't care any more!"
                the_person "I just want your cum!"
            else:
                the_person "Oh god... I can't resist it!"
                the_person "I want you to cum in my pussy [the_person.mc_title]!"
                "She seems almost desperate as she moans."
                the_person "I don't care if you knock me up! I'm just your... breeding slut!"

            menu: #TODO: Add a variant of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
                "Take off the condom":
                    "You don't have much time to spare. You pull out, barely clearing her pussy, and pull the condom off as quickly as you can manage."
                    $ mc.condom = False
                "Leave it on":
                    "You ignore [the_person.possessive_title]'s cum-drunk offer and keep the condom in place."

        else:
            the_person "Oh yeah, cum for me [the_person.mc_title]!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Cum wherever you want [the_person.mc_title]!"
            elif the_person.get_opinion_score("creampies") > 0:
                "[the_person.possessive_title] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Yes! Cum inside me [the_person.mc_title]! Fill me up with your hot load!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    the_person "Yes! Cum inside me and knock me up! Let's pass our genes on to the next generation!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                the_person "I'm on the pill, cum wherever you want [the_person.mc_title]!"
                $ the_person.update_birth_control_knowledge()
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Ah! Do it!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                the_person "Please pull out! I don't want to get pregnant!"

            elif the_person.get_opinion_score("creampies") < 0:
                the_person "Make sure to pull out, you can cum anywhere else you want!"

            else:
                the_person "Ah, really? You should pull out, just in case!"
    return

label genius_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
        the_person "Mmm, your cum feels so warm. I wish you weren't wearing a condom; I bet you would feel amazing raw."
    else:
        the_person "Whew... I can feel how warm your cum is through the condom. It feels nice."
    return

label genius_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Mmm, your cum is so nice and warm. I love it when you fill me up [the_person.mc_title]."
            "She sighs happily."

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Mmmm, it's so warm."
                "She sighs happily as you cum inside her."
                the_person "I feel bad for my [so_title], he never makes me feel this good."
            else:
                the_person "Oh fuck, it's so warm. I can feel it inside me..."
                "She sighs happily as you cum inside her."

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Your cum is so nice and warm..."
                the_person "If you get me pregnant I guess I'll have to tell my [so_title] it's his."
            else:
                the_person "Mmm, it's so warm. I kinda hope it gets me pregnant..."

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
                the_person "Fuck, I told you to pull out! I have a [so_title], what if I got pregnant?"
                the_person "Whatever, I guess it's already done."
            else:
                the_person "Fuck, I told you to pull out! What if I got pregnant."
                the_person "Whatever, I guess it's already done."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "Hey, I told you to pull out! I've got an [so_title], you can't be finishing inside me!"

        elif the_person.get_opinion_score("creampies") < 0:
            the_person "Ugh, I told you to pull out! Fuck, you made such a mess..."

        else:
            the_person "Hey, didn't I tell you to pull out?"
            the_person "Well, whatever. It's done now, I guess."


    return

label genius_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person "Oh god yes, cum inside my ass!"
    else:
        the_person "Oh god, ah!"
    return

label genius_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person "[rando]"
    return

label genius_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Hey, I'm really sorry, but I've got some stuff I need to take care of. Could we catch up some other time?"
    else:
        the_person "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
    return

label genius_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Let me get this out of the way..."
        else:
            the_person "Let me get this out of the way for you..."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "This is just getting in the way..."
        else:
            the_person "Ah... I need to get this off."

    else:
        if the_person.arousal_perc < 50:
            the_person "Let me get this worthless thing off..."
        else:
            the_person "Oh god, I need all of this off so badly!"

    return

label genius_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person "Holy shit, are you really doing this in front of everyone?"
        $ the_person.change_stats(happiness = -1, obedience = -2)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person "Oh my god, you two are just... Wow..."
        $ change_report = the_person.change_slut(1)
        "[title] averts her gaze, but keeps glancing over while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person "Oh my god that's... Wow that looks... Hot."
        $ change_report = the_person.change_slut(2)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
        "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."

    return

label genius_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "I can handle it [the_person.mc_title], you can be rough with me."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to [the_watcher.fname], I'm having a great time. Look, she can't stop peeking over."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh god, having you watch us like this..."
        $ the_person.change_arousal(1)
        "[the_person.title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut(-1)
        "[the_person.title] seems uncomfortable with [the_watcher.fname] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
        $ the_person.change_arousal(1)
        $ the_person.change_slut(1)
        "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.fname] around."

    return

label genius_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        if the_person.obedience > 120:
            "[the_person.title] gives you a curt nod and then turns back to what she was doing."
        else:
            "[the_person.title] glances at you when you enter the room then looks away quickly to avoid starting a conversation."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.title] looks up from her work when you enter the room."
            the_person "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
            "She smiles and winks, then turns back to what she was doing."
        else:
            "[the_person.title] turns to you when you enter the room and shoots you a smile."
            the_person "Hey, good to see you!"

    else:
        if the_person.obedience < 90:
            "[the_person.title] glances up from her work."
            the_person "Hey, how's it going?"
        else:
            "[the_person.title] waves at you as you enter the room."
            the_person "Hey, let me know if you need anything [the_person.mc_title]."
    return

label genius_date_seduction(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I had a great time [the_person.mc_title], but I'm not ready to say goodbye yet. Want to come back to my place?"
            else:
                the_person "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
        else:
            if the_person.love > 40:
                the_person "You're such great company [the_person.mc_title]. Would you please come back to my place and spend some more time with me?"
            else:
                the_person "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "I had a great time [the_person.mc_title]. My [so_title] is supposed to be out for the rest of the night with his friends so..."
                the_person "Would you like to swing by my place tonight?"
            else:
                the_person "I had such a good time tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person "He's out with some friends tonight. Would you like to come to my place and have a drink?"
        else:
            if the_person.love > 40:
                the_person "I don't want this night to end. My [so_title] is out with friends, do you want to come home with me so we can spend more time together?"
            else:
                the_person "Tonight was fantastic. I think my [so_title] is out for the night, so we could go back to my place for a quick drink. What do you say?"
    return

label genius_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Oh damn it [the_person.mc_title], don't go all limp dick on me now!"
            else:
                the_person "Is that all you wanted to do? I was happy just being close to you."
        else:
            if the_person.arousal_perc > 60:
                the_person "Is that really all? [the_person.mc_title], I was just getting started!"
            else:
                the_person "Aww, we were just getting started and you're already finished?"

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You don't want to keep going? I didn't realize you were such a tease [the_person.mc_title]."
            else:
                the_person "That's all? Well, maybe we can try again some other time."
        else:
            if the_person.arousal_perc > 60:
                the_person "Oh my god... you've got me all out of breath..."
            else:
                the_person "That's all? Alright."
    return

label genius_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "Nope! You can't just get worked up and then leave. Lay back [the_person.mc_title], I'm not done yet."
    else:
        the_person "Wait, we're just getting started! You just relax and leave this to me."
    return

label genius_sex_beg_finish(the_person):
    the_person "No no no, please [the_person.mc_title] you can't stop now. I'll do whatever you want, please just let me cum!"
    return

## Role Specific Section ##
label genius_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] smiles mischievously."
    the_person "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
    mc.name "Go on, I'm interested."
    the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
    the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
    return

## Taboo break dialogue ##
label genius_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Don't be shy [the_person.mc_title], come on and kiss me."
    elif the_person.love >= 20:
        the_person "So... Do you want to kiss me?"
        mc.name "I do."
        the_person "Good, because I've really wanted to kiss you too."
    else:
        the_person "Hey there..."
        mc.name "Hey."
        the_person "Are you sure we should be doing this? I mean, I barely know you, when you think about it."
        mc.name "I'm sure. Just close your eyes and relax."
    return

label genius_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Are you as excited as I am? I... I've always wanted to feel your hands on me."
    elif the_person.love >= 20:
        the_person "Do you think we're ready for this? I like you, but it seems like a big step..."
        mc.name "Tell me what you think?"
        "You can see the answer in her eyes before she says anything."
        the_person "I'm ready if you are."
    else:
        the_person "I don't know if I'm ready for this [the_person.mc_title]."
        the_person "It feel like we barely know each other, you know?"
        mc.name "This doesn't have to mean anything unless we want it to. Just relax and let your body tell you what's right."
    return

label genius_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Are you ready? I've wondered what your cock would feel like for a while."
        mc.name "Don't let me stop you then. Go for it."
    elif the_person.love >= 20:
        the_person "Your cock looks so big. I guess I shouldn't keep you waiting any longer then."
    else:
        the_person "Oh my god, look at how hard you've gotten. I didn't think it would be so big."
        mc.name "Go on, give it a touch."
        the_person "I... I don't know if I should."
        mc.name "Why not? It's right there, I certainly don't mind."
        the_person "Fine, but just for a second or two..."
    return

label genius_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Do it [the_person.mc_title]. Touch my pussy."
    elif the_person.love >= 20:
        the_person "I'm so nervous [the_person.mc_title], do you feel that way too?"
        mc.name "Just take a deep breath and relax. You trust me, right?"
        the_person "Of course. I trust you."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Just a little?"
        mc.name "Just a little. Trust me, it's going to feel amazing."
    return

label genius_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Mhmm? What do you want me to do for you?"
    mc.name "I want you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "Do you really want me to try? I'm up for it if you are."
        "You nod and she bites her lip in anticipation."
    elif the_person.love >= 30:
        the_person "I guess knew this was coming."
        mc.name "So..."
        "She rolls her eyes and sighs dramatically."
        the_person "Alright, I'll do it."
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

label genius_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Oh, well that sounds like some fun. I'd be crazy to say no, right?"
        mc.name "Yeah, you would be."
        the_person "Well then, go to town!"
    elif the_person.love >= 30:
        the_person "I'm not sure if \"ready\" is the right word, but you can keep going."
        mc.name "Just relax and enjoy, you'll have a great time."
    else:
        if the_person.has_taboo("sucking_cock"):
            the_person "Whoa, really?"
            "She laughs nervously, but watch a wave of arousal sweep through her."
            the_person "Alright... You can eat me out if you really want to [the_person.mc_title]."

        else:
            the_person "I was wondering if you were going to repay the favor."
            the_person "Alright then, you go for it."
        mc.name "Just relax and enjoy."
    return

label genius_vaginal_sex_taboo_break(the_person): #TODO: add a "I dont do anal""you do for me" stle taboo break
    if the_person.effective_sluttiness() >= 60:
        the_person "Whew, here we go! I'm so excited!"
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
            the_person "At lest this time it should be easier for you to fit inside."
    return

label genius_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "[the_person.title] takes a few deep breaths."
        the_person "Whew, I think I'm ready!"
        the_person "Fuck me in the ass [the_person.mc_title]! Stretch me out and ruin me!"

    elif the_person.love >= 60:
        the_person "I can't believe we're doing this... Do you think you'll even fit?"
        mc.name "I'll fit, but you might not be walking right for a few days."
        the_person "Haha, sure thing..."
        the_person "... You're kidding, right?"
        mc.name "Let's find out."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Fuck, you must really like it tight. We've never even fucked and you're going right for my asshole!"
            the_person "Are you even sure it's going to fit?"
            mc.name "I'll make it fit, but you might not be walking right for a few days."
            the_person "Oh fuck..."
        else:
            the_person "Oh my god, you're actually going to do it! Fuck, I hope you even fit!"
            mc.name "Don't worry, I'll stretch out your ass like I've stretched out all your other holes."
    return

label genius_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "I don't mind, it's not like I could get more pregnant."
    elif the_person.get_opinion_score("bareback sex") > 0:
        the_person "You want to do me raw? That's so hot."
        if the_person.on_birth_control:
            the_person "I'm on the pill, so it should be fine, right? Maybe you should pull out, just in case."
            $ the_person.update_birth_control_knowledge()
        elif the_person.get_opinion_score("creampies") > 0:
            the_person "It's probably smart for you to pull out when you cum though. I'm not on birth control."
            $ the_person.update_birth_control_knowledge()
            mc.name "Do you feel smart today?"
            "She bites her lip and shakes her head."
            the_person "No, not particularly."
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You'll need to pull out though. The last thing in the world I want is to get knocked up."
        else:
            the_person "I'm not on the pill though. You'll need to pull out so you don't knock me up, got it?"
            $ the_person.update_birth_control_knowledge()

    elif the_person.love > 60:
        the_person "I want to feel close to you too [the_person.mc_title]."
        if the_person.on_birth_control:
            the_person "I'm on birth control, so you don't need to worry about getting me pregnant."
            $ the_person.update_birth_control_knowledge()
        elif the_person.get_opinion_score("creampies") > 0:
            the_person "If we're doing this, I don't want you to pull out when you finish either."
            mc.name "Are you on the pill?"
            "She shakes her head."
            the_person "No, but for you I'm okay with that risk."
            $ the_person.update_birth_control_knowledge()
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You'll need to pull out though. I don't want you to get me pregnant, okay?"
        else:
            if the_person.kids == 0:
                the_person "You'll need to pull out though. I don't think either of us want a kid yet, right?"
            else:
                the_person "You'll need to pull out though. I've spent enough time being a mother."

    else:
        if the_person.on_birth_control:
            the_person "You don't want to use protection? I'm on birth control, but it isn't 100 percent effective."
            $ the_person.update_birth_control_knowledge()
            "You shrug, and she thinks for a moment before nodding."
            the_person "As long as you pull out it should be fine, I think."
        elif the_person.has_taboo("vaginal_sex"):
            the_person "You don't want to use protection? I'm not on birth control, you know."
            $ the_person.update_birth_control_knowledge()
            mc.name "I'll pull out. Don't you want our first time to be special?"
            the_person "I do... Fine, just please be careful where you cum."
        else:
            the_person "You don't want to use protection? I'm not on birth control, what if you get me pregnant?"
            $ the_person.update_birth_control_knowledge()
            mc.name "I'll pull out. Don't you want to know how much better it feels without a condom on?"
            the_person "I do... Okay, you can go in raw. Please be careful where you cum though."
    return

label genius_underwear_nudity_taboo_break(the_person, the_clothing):
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

label genius_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.get_opinion_score("showing her tits") * 5):
        the_person "So you want to see my tits, huh? I bet you're going to love them."
        if the_person.has_large_tits:
            "She shakes her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She shakes her chest and gives her [the_person.tits_description] a little jiggle."
        mc.name "I bet I will, I just have to get your [the_clothing.display_name] out of the way."
        the_person "Go for it then, I'm not going to stop you."

    elif the_person.love > 25:
        the_person "So you want to see my boobs?"
        mc.name "Yeah, I do. Are you ready for that?"
        "She takes a long moment to respond, then nods."
        the_person "Yeah, I think I am. I didn't realize how nervous I was going to be though!"
        mc.name "Don't be nervous. Just relax and let me get rid of this [the_clothing.display_name] for you."

    else:
        the_person "Wait, wait, wait! I..."
        mc.name "What's wrong?"
        the_person "I'm... Not sure I'm ready to show you my boobs. I'm just feeling really nervous."
        if the_person.has_large_tits:
            mc.name "You don't have anything to be nervous about. Most girls would kill to have tits as big as yours, you should be proud to show them off."
        else:
            mc.name "You don't have anything to be nervous about. Most girls would kill to have tits as cute as yours."
        "She takes a deep breath and shakes out her shoulders, inadvertently jiggling her [the_person.tits_description] while she's at it."
        the_person "Okay, fuck it! Let's do it!"
    return

label genius_bare_pussy_taboo_break(the_person, the_clothing):
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

label genius_facial_cum_taboo_break(the_person):

    return

label genius_mouth_cum_taboo_break(the_person):

    return

label genius_body_cum_taboo_break(the_person):

    return

label genius_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Hmm, I love your cum deep inside me."
            "She sighs happily."

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Mmm, I finally have your cum in me... I'll have to tell my [so_title] I'm sorry, but this feels so good!"

            else:
                the_person "Oh my god, I finally have your cum in me... It feels so good!"

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ah, finally! I've wanted a load inside me for so long, I don't even care that it's not my [so_title] giving it to me!"

            else:
                the_person "Ah, finally! I've wanted you to put a load inside me for so long! I don't even care I'm not on the pill!"
                $ the_person.update_birth_control_knowledge()

            "She pants happily for a moment."
            the_person "Now I just have to wait and see if you got me pregnant... We should go for round two, just to make sure you did."

        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ah, I should have told you to pull out, but it just feels so good..."
                the_person "We shouldn't do that again though, if I get pregnant I'm going to have to explain it to my [so_title]."

            else:
                the_person "Ah, I really should have told you to pull out... I'm not on the pill..."
                $ the_person.update_birth_control_knowledge()
                the_person "It's just this once, right? It's probably fine..."

    else:
        if the_person.knows_pregnant:
            the_person "Oh, you came deep inside me."

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

label genius_anal_creampie_taboo_break(the_person):

    return
