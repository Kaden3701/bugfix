### PERSONALITY CHARACTERISTICS ###
init 720:
    python:
        def candace_titles(person):
            return "Candi"
        def candace_possessive_titles(person):
            return "Your Office Bimbo"
        def candace_player_titles(person):
            valid_mc_titles = []
            valid_mc_titles.append(mc.name)
            valid_mc_titles.append("Cutie")
            valid_mc_titles.append("Boss")
            return valid_mc_titles
        candace_personality = Personality("candace", default_prefix = bimbo_personality.default_prefix,
        common_likes = ["skirts", "small talk", "the colour pink", "makeup", "pop music"],
        common_sexy_likes = ["giving blowjobs", "missionary style sex", "being submissive", "skimpy outfits", "showing her tits", "showing her ass", "not wearing anything", "not wearing underwear", "lingerie", "cum facials"],
        common_dislikes = ["working", "work uniforms", "conservative outfits", "Mondays", "pants"],
        common_sexy_dislikes = ["taking control", "masturbating"],
        titles_function = candace_titles, possessive_titles_function = candace_possessive_titles, player_titles_function = candace_player_titles)

### DIALOGUE ###
label candace_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around at you. She doesn't hide the way she looks your body up and down."
    $ the_person.set_title("???")
    the_person "Oh you're cute! Okay, cutie, what do you need?"
    mc.name "I just wanted to get your name. I saw you walking past and..."
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    if the_person.has_large_tits:
        the_person "And you liked my tits? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    else:
        the_person "And you liked my ass? Yeah, I get that a lot. I'm [formatted_title], it's nice to meet you!"
    $ mc.change_locked_clarity(5)
    #the_person "Well then, I suppose I shouldn't disappoint you. You can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    the_person "So what's your name?"
    return

label candace_greetings(the_person):
    if the_person.love < 0:
        the_person "Oh, my, god... What do you want? Do I look like I want to be talking to you?"
    elif the_person.happiness < 90:
        the_person "Hi [the_person.mc_title]..."
    elif renpy.random.randint(0,4) == 1:
        the_person "Hi [the_person.mc_title]..."
        mc.name "You doing okay today?"
        the_person "Yeah... I guess. I just had a disappointing night last night."
        mc.name "Oh?"
        call candace_random_dumb_dialogue(the_person) from _candace_flavor_text_1
    else:
        if the_person.sluttiness > 60:
            if the_person.obedience > 180:
                the_person "Hey there [the_person.mc_title]. I mean sir! Hey there, sir!"
            else:
                the_person "Hey [the_person.mc_title], what are you doing here? Can I help with anything? Anything at all?"
        else:
            if the_person.obedience > 180:
                the_person "Hi there [the_person.mc_title], what can I do for you?"
            else:
                the_person "Hi there [the_person.mc_title]!"
    return

label candace_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know just how to touch me [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly while you touch her."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Do you like touching me [the_person.mc_title]? I know I like it when you do!"
        else:
            the_person "Do you like touching me [the_person.mc_title]? You seem to know exactly what to do."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yes! That feels really nice!"
            "She giggles happily, clearly having a good time."
        else:
            the_person " Mmm, you're driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh fuck! My [so_title] would be so pissed if he knew how much better you feel when you touch me!"
                the_person "Make me cum! Make me cum my brains out!"

        else:
            the_person "Oh my god, I might cum if you keep touching me like that!"
    return

label candace_sex_responses_oral(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Aww, you always know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Does my pussy taste good [the_person.mc_title]? I'll repay the favor and suck your cock later!"
        else:
            the_person "That, like, feels so good [the_person.mc_title]!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Ah! Hehe, that feels so good!"
            "She giggles happily, clearly having a good time."
        else:
            the_person "Oh wow! Mmmm, you're tongue is, like, driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "I can, like, feel it happening! You're going to make me cum with your mouth! Make me cum, please!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh fuck! My [so_title] would be so pissed if he knew how much better you make me feel!"
                the_person "He never licks my pussy though, so make me cum! Make me cum my brains out!"

        else:
            the_person "Oh my god, you're... You might make me cum if you keep licking my pussy like that!"
    return

label candace_sex_responses_vaginal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know what I like [the_person.mc_title]!"
        else:
            "[the_person.title] giggles softly."

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Is your cock always this big, or are you just happy to see me? Hehe!"
        else:
            the_person "Am I your dirty girl [the_person.mc_title]? Because I'm having so much fun right now!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yes! Keep fucking me!"
            "She giggles happily, clearly having a good time."
        else:
            the_person "Oh wow! Mmmm, your cock is driving me crazy [the_person.mc_title]!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "I can, like, feel it happening! You're going to make me cum my fucking brains out [the_person.mc_title]! Please, make me cum!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh fuck! My [so_title] would be so pissed if he knew how much better your cock feels!"
                the_person "Oh well, I just want to cum! Make me cum! Make me cum my brains out!"

        else:
            the_person "Oh my god, you're... You might make me cum if you keep going!"
    return

label candace_sex_responses_anal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "I can, like, feel every single inch of you in me! You're so big!"
        else:
            the_person "You're, like, {i}huge{/i} inside of me! I don't know if I can do this for very long!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            if mc.condom:
                the_person "Fuck my ass [the_person.mc_title], fuck it good until you're done with me!"
            else:
                the_person "Fuck my ass [the_person.mc_title], fuck it good and raw and you're done with me!"
        else:
            the_person "Oh, it feels like you're stirring up my insides with your dick! Ah!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "I'm so stretched out, I think I'm starting to get the hang of this!"
            "She giggles happily, clearly proud of her accomplishment."
        else:
            the_person "My mind is going blank, all I can think about is your cock inside of me!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "I can, like, feel it happening! Fuck my ass and make me cum [the_person.mc_title]! Do it!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh fuck! My [so_title] would be so pissed if he knew I was letting you anal me."
                the_person "He's been begging for it for {i}months{/i}, but I just know he wouldn't feel nearly as good inside me as you do!"

        else:
            the_person "Oh my god, you're... You might make me cum if you keep fucking my ass! Please make me cum!"
    return

label candace_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh god, I'm going to cum! All I want to do is cum [the_person.mc_title], ah!"
        "She squeals with pleasure and excitement."
    else:
        the_person "Oh my god, this feeling. I'm... I'm... cumming!"

    return

label candace_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh god, make me cum [the_person.mc_title]! My mind is going blank, I just need to cum!"
    else:
        the_person "That feels, like, {i}so good{/i}!"
        "She closes her eyes and squeals with pleasure."
    return

label candace_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh god, I'm going to cum! Ahh, make me cum [the_person.mc_title], it's all I want right now!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Yes, yes, yes! Make me cum! Make me cum hard!"
    return

label candace_climax_responses_anal(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh my god! I'm going to cum with your cock up my ass!"
        "She squeals loudly."
    else:
        the_person "Oh my god! I'm such a slut, I'm about to cum! Oh fuck!"

    return

label candace_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "Oh that's cute! You have such a good sense of style [the_person.mc_title], this is just what I like to wear!"
    else:
        the_person "It's so cute! I love getting new clothes - you should see my closet at home, there's no such thing as too many shoes, right?"
    return

label candace_clothing_reject(the_person):
    if the_person.obedience > 180:
        the_person "Uh... I don't think I'm allowed to wear that. I really wish I could though, just for you!"
    else:
        if the_person.sluttiness > 60:
            the_person "That's not really an outfit, is it? I like something a little cuter - some heels, add a dash of pink, and a top to show off my tits!"
            "[the_person.title] looks the outfit over again for a moment and shakes her head."
            the_person "Yeah, this just isn't going to do it. Thanks for the thought though!"
        else:
            the_person "Aww, I don't think I could ever wear something like that! I wish I could though, could you imagine the looks I would get? It would be. So. Hot."
    return

label candace_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "Hehe, you really made a mess of me. I should go get tidied up, I'm supposed to be a proper lady here!"
    else:
        if the_person.sluttiness > 40:
            "[the_person.title] looks down at herself and giggles."
            the_person "Hehe, I'm all messed up after that! I need to go sort this out, this outfit just doesn't work right now!"
        else:
            the_person "Oh darn, my outfit's all confuzzled! I'm going to go fix this up, I'll be back before you know it!"
    return

label candace_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "Don't you think I look cuter with my [the_clothing.display_name] on? Leave it alone for now, okay?"
    elif the_person.obedience < 70:
        the_person "Oh no-no-no, I'm going to decide when my [the_clothing.display_name] come off. I want to see you work for it!"
    else:
        "[the_person.title] giggles and bats your hand away playfully."
        the_person "Not yet, there's so much fun stuff we have to do first!"
    return

label candace_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 70:
            the_person "Oh yeah, that's one of my favorite things to do! Come on, let's do it!"
        else:
            the_person "Yeah, let's do it! You're so cute when you're horny, did you know that?"
    else:
        the_person "Oh? Oh! Yeah, let's do that!"
    return

label candace_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Wow that's a... does that even work? I thought... well I guess I should try it before I knock it!"
    else:
        if the_person.obedience > 180:
            the_person "If that's what you want, boss man, that's what you'll get!"
        else:
            the_person "You bring out the worst in me, you know that [the_person.mc_title]? I was a nice, respectable girl before you showed up!"
    return

label candace_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "No, no, no, not yet. I want you to make me wait for it a little bit, get me really begging for it."
    else:
        the_person "Uh, I don't think that sounds fun. Let's do something else. Come on, you pick!"
    return

label candace_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "What? I have a [so_title], and he treats me so much better than you could EVER hope to. Understood?"
        "She rolls her eyes dramatically and walks away."
        the_person "Perv."
    elif the_person.sluttiness < 20:
        the_person "Uh, what the ACTUAL FUCK?! What do you think you're doing? Just saying that must be... illegal, or something!"
        "[the_person.title] glares at you and walks away."
    else:
        the_person "Eew! No, no, no! I will NEVER do that with ANYONE! Eew!"
        "[the_person.title] shakes her head and walks away."
    return

label candace_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh yay, I know how to deal with this! You just relax and I'll make you feel very, very good!"
        else:
            the_person "All I can think about is that cute little dress I saw this morning. Oh, that's not you meant, was it..."
            "[the_person.title] giggles."
            the_person "Never mind, lead the way!"
    else:
        if the_person.sluttiness > 50:
            the_person "Yay! I was getting so horny that I was ready to jump you in the hall!"
        elif the_person.sluttiness > 10:
            the_person "Hehe, I thought you had the that look in your eye. I have a sixth sense, but it's for horny guys instead of ghosts!"
        else:
            the_person "Oh, I don't really know what to say [the_person.mc_title]..."
    return

label candace_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Just make it an official order and it's all yours, boss man."
            $ mc.change_locked_clarity(5)
        else:
            the_person "Hehe, thank you, you're way too nice to me!"

    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 50:
            the_person "That's like, super hot to hear you say. We just can't let my [so_title] or he would flip out."
            $ mc.change_locked_clarity(5)
        else:
            the_person "Oh my god, you're so cute! My [so_title] never says things like that to me."
            "She pouts for a moment before returning to her bubbly self."

    else:
        if the_person.sluttiness > 50:
            the_person "You should try your luck sometimes. Maybe take me out for a drink, I get wild after I've had a few. Wild-er, I guess."
            $ mc.change_locked_clarity(5)
        else:
            the_person "Oh you, stop it! You're going to make me blush!"
    return

label candace_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            #She's in uniform and likes how it looks.
            the_person "Hehe, thanks! I love these outfits you make us wear, they're, like, so cute!"
            the_person "Maybe you should pick out other things for me to wear. I bet you have some good ideas!"
            mc.name "For you I certainly do. Maybe I'll talk to you later about it."
            $ mc.change_locked_clarity(5)
            "She smiles happily."
            the_person "Alright!"

        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.vagina_visible:
                # Her pussy is on display.
                the_person "Thanks! I keep worrying I'm going to get in trouble, but then I remember I'm allowed to be dressed like this!"
                mc.name "Not just allowed: required."
                the_person "Yeah! This is such a crazy place to work!"
                $ mc.change_locked_clarity(5)
                "[the_person.possessive_title] bounces happily, unintentionally jiggling her tits."

            elif the_person.tits_visible:
                #Her tits are out
                if the_person.has_large_tits:
                    the_person "Hehe, thanks! I really like how it shows off my [the_person.tits_description]!"
                    "[the_person.possessive_title] bounces happily, jiggling her breasts."
                    the_person "People are always telling me I need to hide them, but at work I don't have to worry about that!"
                else:
                    the_person "Hehe, thanks! I really like how I it shows off my [the_person.tits_description]!"
                    "[the_person.possessive_title] looks down at her own chests and pouts."
                    the_person "I wish they were bigger though. Oh well!"
                    $ mc.change_locked_clarity(5)

            elif the_person.underwear_visible:
                # Her underwear is visible.
                the_person "Hehe, thank you! I know it's a little slutty, but I like how little these outfits you make us wear cover!"
                mc.name "I certainly do too."
                $ mc.change_locked_clarity(5)
                "She laughs and sticks her tongue out."
                the_person "You're silly, you know that? But like, in a fun way."
            else:
                # It's just generally slutty.
                the_person "Hehe, thank you! I don't think I'm brave enough to wear something like this outside, but at work it's okay! Right?"
                mc.name "More than okay, it's required."
                the_person "Oh yeah, right! I'm sorry, there are so many rules here, I'm always forgetting them!"
                mc.name "Well don't worry, you're doing a great job so far."
                $ mc.change_locked_clarity(5)
                "[the_person.possessive_title] smiles and bounces happily."
                the_person "Yay!"

    else:
        #She's in her own outfit.
        the_person "Aw, thanks! It took me sooooo long to decide what to wear today. I picked this because it made my ass look good. What do you think?"
        $ the_person.draw_person(position = "back_peek")
        "[the_person.possessive_title] spins around and leans forward a little, wiggling her butt at you."
        mc.name "Oh yeah, I think it looks really good."
        $ the_person.draw_person()
        $ mc.change_locked_clarity(5)
        the_person "Yay!"
    return

label candace_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.tits_visible:
                the_person "Hehe, thanks! Do you like my boobs?"
                "She puts her hands behind her back and thrusts her chest out at you, waiting for your response."
                $ mc.change_locked_clarity(10)
                mc.name "They look fantastic."
                "[the_person.possessive_title] smiles and giggles."
                the_person "Yay! I like having my boobs out at work. It feels naughty, but I'm, like, allowed to do it!"
            else:
                the_person "Hehe, thanks! I think you're, like, pretty hot too!"
                the_person "Oh my god! We should go partying together! That would be, like, so much fun!"
                $ mc.change_locked_clarity(10)
                mc.name "That does sound like fun. Maybe we will."
                "She nods and smiles happily."
        else:
            "[the_person.possessive_title] smiles and giggles."
            the_person "Hehe, thanks! I think you're pretty hot too!"
            the_person "Oh, we should totally go partying together! That would be, like, so much fun!"
            mc.name "That does sound like fun. Maybe we will."
            "She nods and smiles happily."
            $ mc.change_locked_clarity(10)
            the_person "I can even wear something nice for you, instead of this silly uniform you make..."
            "She stops suddenly and covers her mouth with her hand."
            the_person "Oops. I'm sorry, I didn't mean that. I just kind of talk without thinking sometimes." #TODO: On with the spanking! And then, the oral sex!
            mc.name "It's fine. You don't have to like your uniform as long as you're wearing it."
            "[the_person.title] puts on a stern face and nods severely."
            the_person "Of course, [the_person.mc_title]!"

    else:
        if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
            the_person "Hehe, thanks! I uh..."
            "[the_person.possessive_title] bites her lip and leans closer to you to whisper in your ear."
            the_person "I think you're, like, pretty hot too."
            $ mc.change_locked_clarity(10)
            "She pulls back and smiles playfully."

        else:
            the_person "Hehe, thank you! I think you're looking, like, pretty hot too."
            the_person "Oh, we should totally go partying some time! I can wear something even cuter for you..."
            $ the_person.draw_person(position = "back_peek")
            the_person "Maybe something that shows off my butt a little more... Doesn't that sound fun?"
            "[the_person.possessive_title] wiggles her hips, shaking her butt for your enjoyment."
            $ mc.change_locked_clarity(10)
            mc.name "That does sound like fun. Maybe we should go out one day."
            $ the_person.draw_person()
            "She turns back to you and smiles."
            the_person "Yay!"
    return

label candace_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))):
        "[the_person.possessive_title] giggles and looks around nervously."
        the_person "Oh my god, [the_person.mc_title]! That's so naughty!"
        menu:
            "Find someplace quiet":
                mc.name "Come with me and we can do some more naughty things."
                "[the_person.title] giggles again and nods eagerly. You take her hand and lead her away."
                "When you're finally alone you put your arm around her waist and pull her close."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass
                "You kiss her, and she responds by leaning her body against you eagerly."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_55123
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "Wait until I get you alone and you'll see how naughty I can get."
                the_person "Hehe, I'm excited to find out!"

    else: # She wants to kiss you, leading to other things.
        if mc.location.person_count == 1:
            the_person "Oh my god, [the_person.mc_title]! you're so naughty!"
            "She giggles playfully and looks you up and down."
            $ mc.change_locked_clarity(15)
            the_person "But maybe... We could fool around, if you really want to. I think you're pretty cute."

        else:  #She's into turning you on.
            if the_person.has_large_tits: #Bounces her tits for you
                "She giggles and grabs her own tits, jiggling them for you."
                $ the_person.draw_person(the_animation = tit_bob)

            else:
                "She giggles and wiggles her hips for you."
            $ mc.change_locked_clarity(15)
            the_person "Do you want to have some fun?"

        menu:
            "Kiss her":
                mc.name "Yeah, I do. Come here."
                $ the_person.draw_person()
                if the_person.has_taboo("kissing"):
                    "You put your arm around [the_person.title]'s waist and pull her close. She giggles as she falls against your body."
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You kiss her, and she rubs her body against you eagerly."
                else:
                    "You put your arm around [the_person.title]'s waist and pull her close. She leans her body against you eagerly as you kiss her."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_person_56123
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I do, but it'll have to be some other time."
                $ the_person.draw_person(emotion = "sad")
                "She pouts and crosses her arms dramatically."
                the_person "Aww, why? Can't you, like, just do something with me right now?"
                mc.name "I'll make it up to you, I promise."
                "[the_person.title] sighs and nods."
                the_person "Okay..."
    return

label candace_cum_face(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person "I hope this means I did a good job."
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
        else:
            the_person "Fuck me, you really pumped it out, didn't you?"
            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
    return

label candace_cum_mouth(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.sluttiness > 80:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person "Bleh, I don't know if I'll ever get used to that."
    return

label candace_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person "That condom is so stretchy! I can feel how much cum you put into it and it's, like, a lot!"
        else:
            the_person "Mmm, your cum is so nice and hot!"

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                if the_person.on_birth_control:
                    the_person "Mmm, I love having all your cum inside me. I did take my pill, right?"
                else:
                    the_person "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person "Oh well, my [so_title] will just take care of it, so that doesn't matter!"
            else:
                if the_person.on_birth_control:
                    the_person "Mmm, I love having all your cum inside me. I did take my pill, right?"
                else:
                    the_person "Mmm, I love having all your cum inside me. That might make me pregnant, right?"
                "She thinks about this for a second, then shrugs."
                the_person "Oh well, it's worth it to feel like this!"
        else:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                if the_person.on_birth_control:
                    the_person "Oh, that's so hot... But wait, I did take my pill, right?"
                else:
                    the_person "Oh, that's so hot... But wait, if I get pregnant what do I tell my [so_title]?"
                "She bites her lip and looks worried."
                the_person "We shouldn't do this too often. Next time you can cum somewhere else, okay?"
            else:
                if the_person.on_birth_control:
                    the_person "Oh, that's so hot... But wait, I did take my pill, right?"
                else:
                    the_person "Oh, that's so hot... But what do I do if I get pregnant?"
                "She bites her lip and looks worried."
                the_person "We shouldn't do this too often, okay? Next time you can cum, like, somewhere else, right?"
    return

label candace_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person "Give me your cum! I want you to cum in my ass! Ah!"
    else:
        the_person "Oh! Fuck, I hope there's room for all your cum!"
    return

label candace_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
    the_person "[rando]"
    return

label candace_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "Hi, I'm like, really sorry, but I have way more stuff than you can imagine that I have to get done right now. Could we catch up later?"
    else:
        the_person "Hey, I'm sorry, but I'm just suuuper busy right now! Hit me up later though, I'd love to chat once I get all this stupid work done!"
    return

label candace_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Oh wait, I know what you want to see more of..."
        else:
            the_person "Ugh, all this clothing is getting in the way!"

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "I spent so much time this morning picking out this outfit, but I think you'd enjoy it more if I took it off, right?"
        else:
            the_person "Ah... I need to get all of this silly stuff off of me!"

    else:
        if the_person.arousal_perc < 50:
            the_person "Teehee, just wait a moment and I'll strip this off for you..."
        else:
            the_person "Oh my god, let me strip for you [the_person.mc_title], let me be your slutty stripper!"

    return

label candace_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person "Is that, like, allowed? I thought that was illegal or something. Ugh."
        $ the_person.change_stats(happiness = -1, obedience = -2)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person()
        the_person "Could you two get a room or something? There are some of us here who are trying to focus and you're being very distracting."
        $ the_person.change_happiness(-1)
        "[title] tries to avert her gaze while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person()
        the_person "Wow [the_sex_person.fname] you're so adventurous, I don't think I could ever do that. But it looks, like, super fun!"
        $ change_report = the_person.change_slut(1)
        "[title] averts her gaze, but keeps glancing over while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person "Oh. My. God. That is so fucking hot... Keep it up girl, you're doing great!"
        $ change_report = the_person.change_slut(2)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person "Mmm, come on [the_person.mc_title], you should do something more to her. I bet she wants it real bad. I know I do..."
        "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
    return

label candace_being_watched(the_person, the_watcher, the_position):
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

label candace_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        "[the_person.title] looks at you, pouts, then looks back at her work."

    elif the_person.happiness > 120:
        if the_person.sluttiness > 40:
            "[the_person.title] looks at you when you enter the room and smiles."
            the_person "[the_person.mc_title]! I'm so glad you're stopping by, I've been so bored without you."
            "She pouts at you, eyes running up and down your body shamelessly."
            the_person "I hope you're here for something fun!"
        else:
            "[the_person.title] looks up from her work when you come into the room and smiles."
            the_person "[the_person.mc_title]! It's so good to see you! I've been having, like, the best day!"

    else:
        if the_person.obedience < 100:
            the_person "Hi [the_person.mc_title]! Do you need anything, any way I can help you?"
        else:
            the_person "Hi [the_person.mc_title]! Duh, I mean sir! Hi sir!"
            "[the_person.title] sticks out her tongue, then smiles and turns back to her work."

    return

label candace_date_seduction(the_person):
    if the_person.sluttiness > the_person.love:
        $ mc.change_locked_clarity(30)
        if the_person.sluttiness > 40:
            the_person "So [the_person.mc_title], don't you think it's time you came back home with me and we had some real fun?"
            "[the_person.title] bites her lip and puffs out her chest just a little bit."
        else:
            the_person "[the_person.mc_title], I swear you're driving me crazy. Do you, like, want to come home with me and just get wild?"

    else:
        if the_person.love > 40:
            the_person "[the_person.mc_title], I don't know how you do it but I swear you've been driving me, like, totally crazy all night."
            $ mc.change_locked_clarity(40)
            "[the_person.title] runs her hand along your arm and giggles."
            the_person "I want you to come back to my place so I can have you all to myself."
            "She looks around and thinks for a second."
            the_person "I guess if I HAVE to stay and share you, I could do that too though!"
        else:
            $ mc.change_locked_clarity(40)
            the_person "Oh my god [the_person.mc_title], tonight has been so much fun. Do you want to, like, come back home with me and drink some more?"
    return

label candace_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Aww sweety, I was just getting close to cumming and you're done?!"
            else:
                the_person "That's all? Aww, I hope you had a good time with me..."
        else:
            if the_person.arousal_perc > 60:
                "Wait, you're stopping? Aren't you crazy horny right now too?"
            else:
                the_person "Don't you want to play with me any more? Oh well, your loss."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "You're actually done? But weren't you, like, having fun? I'm so fucking horny now..."
            else:
                the_person "Is that all you wanted to do? I thought guys had to, like, cum or it hurt."
        else:
            if the_person.arousal_perc > 60:
                the_person "Aww, I was just getting getting warmed up!"

            else:
                the_person "That's it? Well, I guess that was a fun time well it lasted."
    return

label candace_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "You're funny! I haven't even cum yet! There's not way I'm letting you leave yet!"
    else:
        the_person "Oh honey, we're just getting started! You just relax and leave this to me."
    return


## Role Specific Section ##
label candace_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
    the_person "Okay, how can I help?"
    mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
    "[the_person.title] nods happily."
    "There's a long pause."
    mc.name "Do you know what to do?"
    the_person "Uh, duh! Look into the serum-stuff we make and make it better-er!"
    mc.name "Right, and do you have any idea how to actually do that?"
    "[the_person.title]'s eyebrows knit together as she tries to think."
    the_person "Uhm... not yet but... what if..."
    "You imagine you can see the little hamster in her head running as fast as it can."
    the_person "I've got it! What if you test it on me!"
    mc.name "Do you think that's a good idea!"
    the_person "Duh, that's why I thought of it! Come on, how bad could it be? Just let me try it! Record it or something and I'll tell you what it feels like!"
    return

## Taboo break dialogue ##
label candace_kissing_taboo_break(the_person):
    the_person "Mmm, let's start with making out! But you don't plan on stopping there, do you?"
    return

label candace_touching_body_taboo_break(the_person):
    the_person "Mmm, your hands feel so good on me! Make sure to play with my nipples, it feels so good!"
    return

label candace_touching_penis_taboo_break(the_person):
    the_person "Your cock looks so hard... can I stroke it a little?"
    mc.name "A little or a lot, your choice."
    the_person "Oh good. Probably not too much, I need your cock to stroke me back a bit!"
    return

label candace_touching_vagina_taboo_break(the_person):
    the_person "Yay! I was hoping we would get around to doing this soon!"
    return

label candace_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "Oh yeah? What do you want me to do to you?"
    mc.name "I want you to suck on my cock."
    the_person "Yum! I was planning on doing that soon anyway!"
    return

label candace_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    the_person "Oh thank god, last guy I was with never returned the favor when I sucked his dick."
    "She spreads her legs and waits for you to get to work."
    return

label candace_vaginal_sex_taboo_break(the_person):
    the_person "Fucking. Finally. I was getting ready to ask you!"
    if candace_get_has_quit_job():
        the_person "It isn't right for a boss not to fuck his employee!"
    return

label candace_anal_sex_taboo_break(the_person):
    the_person "Oh god, you're going to put that thing in my ass?"
    "She grabs your cock and strokes it a few times. At first you think she might be a little scared."
    the_person "This is like... a dream come true! Fuck my ass good [the_person.mc_title]!"
    return

label candace_condomless_sex_taboo_break(the_person):
    the_person "Mmm, I love it bare. Skin on skin is the best!"
    "She stops and thinks for a second."
    if the_person.on_birth_control:
        the_person "I remembered to take my pill this morning, so cum ANYWHERE."
    else:
        the_person "I'm not taking birth control right now. I'm not gonna tell you where to cum, but thought that, like, you might want to know that!"
    return

label candace_underwear_nudity_taboo_break(the_person, the_clothing):
    the_person "You want to see my underwear? Sure! I'm actually surprised I remembered to put normal clothes on today!"
    return

label candace_bare_tits_taboo_break(the_person, the_clothing):
    the_person "You want to see my tits? Of course! I'm actually surprised I don't already have them out!"
    return

label candace_bare_pussy_taboo_break(the_person, the_clothing):
    the_person "You want to see my pussy?"
    "[the_person.title] looks down."
    the_person "Oh! I guess I did remember to wear clothes today! Just give me one second and I'll get this off for you."
    return

label candace_facial_cum_taboo_break(the_person):

    return

label candace_mouth_cum_taboo_break(the_person):

    return

label candace_body_cum_taboo_break(the_person):

    return

label candace_creampie_taboo_break(the_person):

    return

label candace_anal_creampie_taboo_break(the_person):

    return

label candace_random_dumb_dialogue(the_person):
    $rando = renpy.random.choice(["Did you know for cock fights... they use chickens? Like, what the fuck? What a waste of $50!",
    "I asked the guy at the grocery store the other day if he had time for a little stuffing... he brought me some kind of herb?",
    "I went to this place that was advertising foot longs. Turns out they are some kind of sandwich?"])
    the_person "[rando]"
    return

label candace_sex_toy_taboo_break(the_person):
    pass
    return

label candace_roleplay_taboo_break(the_person):
    pass
    return

label candace_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    the_person "Oh. my. god. YES! I can't wait to get fucked senseless in your bed!"
    "She pauses for a second."
    the_person "We... umm... you ARE asking me over to fuck all night long, right?"
    mc.name "Yes, that's exactly what I was thinking."
    the_person "Yay!"
    return

label candace_sleepover_herplace_response(the_person): #Spending the night at her place
    the_person "Oh. my. god. YES! There's so many places in my apartment I haven't had sex yet!"
    return


label candace_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    the_person "I almost walked out naked, but I thought you might like this."
    the_person "Let's fuck!"
    return


label candace_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    "[the_person.possessive_title] takes the wine glass. She gulps it down, draining the glass all at once."
    the_person "Mmm, that was nice! But enough with the booze, let's fuck!"
    return

label candace_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    "[the_person.possessive_title] holds up one hand, showing you her fingers."
    the_person "I came like... this many times... then I lost count..."
    mc.name "What about your other hand?"
    the_person "I need to keep that one free... well... mostly free anyway..."
    "She reaches over and starts to stroke you with her mostly free hand."
    the_person "My pussy is raw... but I bet I could cum again!"
    return


label candace_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Oh god, I love it when you fuck me like that."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "Let's go again! Fuck me like this all night!"
    return

label candace_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Get the easy one over with. From here on out, fuck me good!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "[the_person.title] awaits you eagerly as she caresses you and touches herself."
    return

label candace_lingerie_shopping_tame_response(the_person):
    the_person "Umm... did you accidentally give me too much stuff? I'm wearing like, way too many clothes!"
    mc.name "I know. I just want to see what it looks like on you."
    the_person "I'd rather show you what it looks like OFF of me!"
    return

label candace_lingerie_shopping_excited_response(the_person):
    the_person "Oh! Hot damn I can't wait to show this to my boyfriend!"
    $ the_person.draw_person()
    the_person "Oh my god! I forgot you were here! Doesn't this, like, make you want to fuck me?"
    return

label candace_lingerie_shopping_wow_response(the_person):
    the_person "Wow! I'm so glad you brought me here!"
    the_person "I'd probably get arrested for wearing this in public, but I can't wait to wear it just for you!"
    return
