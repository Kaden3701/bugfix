label starbuck_greetings(the_person):
    call starbuck_intro from SB_starbuck_intro_1
    return

label starbuck_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person "Oh wow, I bet this will look great on me!"
    else:
        the_person "You think this would look good on me? I'll keep that in mind!"
    return

label starbuck_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person "Oh, I wish I could wear this [the_person.mc_title], but even at a sex shop you can go too far..."
    else:
        if the_person.sluttiness > 60:
            the_person "Oh my god [the_person.mc_title]... It's hot, but I can't wear this here!"
        else:
            the_person "Oh my god [the_person.mc_title], an outfit like that should only be worn in private!"
    return

label starbuck_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "Sorry [the_person.mc_title], I should really get myself dressed properly again! Just a second!"
    else:
        if the_person.sluttiness > 50:
            the_person "I love the way you're looking at me, but I should wear something else before another customer comes in."
        else:
            the_person "Oh my god, I shouldn't be dressed like this at the shop! Just give me a moment."
    return

label starbuck_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I wish I could let you, but I don't think I should be taking my [the_clothing.display_name] off yet."
    elif the_person.obedience < 70:
        the_person "Sorry [the_person.mc_title], but I love being a tease. I'm going to leave my [the_clothing.display_name] on for a bit."
    else:
        the_person "I can't take my [the_clothing.display_name] off right now [the_person.mc_title]!"
    return

label starbuck_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            "[the_person.possessive_title] gives you a wink."
            the_person "I was thinking the same thing!"
        else:
            the_person "You want to do that with me, [the_person.mc_title]? You're lucky I'm just as perverted."
    else:
        the_person "Hmmm, sounds good! Let's do it!"
    return

label starbuck_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh god [the_person.mc_title], I don't think I could do this for anyone else..."
        the_person "But I just can't say no to you."
    else:
        if the_person.obedience > 180:
            the_person "If that's what my best customer needs me to do..."
        else:
            the_person "I'm not sure I should be letting a customer... sample the goods this way..."
            "She seems conflicted for a second."
            the_person "Okay, just promise you won't tell anyone!"
    return

label starbuck_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet, I need to get warmed up first. Let's start out with something a little more tame."
    else:
        the_person "I... we can't do that [the_person.mc_title]. You're one of my customers, after all!"
    return

label starbuck_sex_angry_reject(the_person):
    if the_person.sluttiness < 20:
        the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person "Ugh! Get away from me, I don't even want to talk to you after that."
    else:
        the_person "What the fuck do you think you're doing, even I won't do that!"
        the_person "Get the fuck away from me, I don't even want to talk to you after that!"
    return

label starbuck_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "What's up [the_person.mc_title]? Do you need any help testing the merchandise?"
        else:
            the_person "What're you thinking about? You look like you're up to something."
    else:
        if the_person.sluttiness > 50:
            the_person "Do you have something in mind? I wouldn't mind fooling around some..."
        elif the_person.sluttiness > 10:
            the_person "Oh, do you see something you like?"
        else:
            the_person "I... what do you mean, [the_person.mc_title]?"
    return

label starbuck_seduction_accept_crowded(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title] grabs your arm and smiles."
        the_person "That sounds great. Let's head to the backroom and get started... let's at least find someplace quiet."

    elif the_person.sluttiness < 50:
        the_person "I... I mean, we shouldn't do anything like that without at least going to the back room... right?"

    else:
        the_person "Oh god, that sounds so hot. Let's get to it!"
    return

label starbuck_seduction_accept_alone(the_person):
    if the_person.sluttiness < 20:
        the_person "Well, there's nobody around to stop us..."
    elif the_person.sluttiness < 50:
        the_person "Mmm, that's a fun idea. Come on, let's get to it!"
    else:
        the_person "Oh [the_person.mc_title], I can't wait!"
    return

label starbuck_seduction_refuse(the_person):
    if the_person.sluttiness < 20:
        "[the_person.possessive_title] blushes and looks away from you awkwardly."
        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."

    elif the_person.sluttiness < 50:
        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
        "[the_person.possessive_title] smiles and gives you a wink."

    else:
        "[the_person.possessive_title] looks at you and frowns"
        the_person "It's so, so tempting, but I've had a rough day and just don't feel up to it right now [the_person.mc_title]. Hold onto that thought though."
    return

label starbuck_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "I hope you are ready to back that flirting up with some action!"
        else:
            the_person "Thank you for the compliment, sir."
    else:
        if the_person.sluttiness > 50:
            the_person "Mmm, I like what I'm seeing too."
            "[the_person.possessive_title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Hey, maybe if you buy something first."
            "[the_person.possessive_title] gives you a wink and smiles."
    return

label starbuck_cum_face(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Mmm, that feels great. I love it when you blow a big load all over my face."
            "[the_person.possessive_title] licks her lips, cleaning up a few drops of your semen that had run down her face."
        else:
            the_person "Mmm, thanks! I hope you enjoyed it as much as I did!"
            "[the_person.possessive_title] runs a finger along her cheek, wiping away some of your semen."
    else:
        if the_person.sluttiness > 80:
            the_person "Ah... I love a nice, hot load on my face. Don't you think I look hot like this?"
            "[the_person.char] runs a finger through a puddle of your cum and then licks it clean, winking at you while she does."
        else:
            the_person "Fuck me, you really pumped it out, didn't you?"
            "[the_person.possessive_title] runs a finger along her cheek, wiping away some of your semen."
    return

label starbuck_cum_mouth(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 60:
            the_person "Oh god, you taste so good. Thank you for the treat [the_person.mc_title]."
        else:
            the_person "Mmm, thank you sir. Feel free to browse while I clean myself up!"
    else:
        if the_person.sluttiness > 80:
            the_person "Mmm, your cum tastes so great [the_person.mc_title], are you sure there isn't any more of it for me?"
            "[the_person.possessive_title] licks her lips and sighs happily."
        else:
            "[the_person.possessive_title] licks her lips and smiles at you."
            the_person "Mmm, that was nice."
    return


label starbuck_cum_pullout(the_person):
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

label starbuck_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
        the_person "Mmm, your cum feels so warm. I wish you weren't wearing a condom; I bet you would feel amazing raw."
    else:
        the_person "Whew... I can feel how warm your cum is through the condom. It feels nice."
    return

label starbuck_cum_vagina(the_person):
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

label starbuck_sex_strip(the_person):
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
            the_person "Ugh let me get this off. I want to feel your skin pressed up against me!"
    return

label starbuck_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I wish I could talk more, but I have other customers. Can we talk later [the_person.mc_title]?"
    else:
        the_person "Hey, I'd love to chat but I have a million things to get done around the store right now. Maybe later?"
    return

label starbuck_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person "Ugh, for crying out loud, you two. Get a room or something, nobody wants to see this."
        $ the_person.change_stats(happiness = -1, obedience = -2)
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
        "[title] watches for a moment, then turns away  while you and [the_sex_person.fname] keep [the_position.verb]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person()
        the_person "Oh wow that's hot. I should sell tickets to this!"
        $ the_person.change_slut(2)
        "[title] watches you and [the_sex_person.fname] [the_position.verb]."

    else:
        $ the_person.draw_person(emotion = "happy")
        the_person "Come on [the_person.mc_title], [the_sex_person.fname] is going to fall asleep at this rate! You're going to have to give her a little more than that."
        "[title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
    return

label starbuck_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "I can handle it [the_person.mc_title]. Let's show [the_watcher.fname] how it's done!"
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to [the_watcher.fname]. This is a sex shop, surely they expect to see something like this when they walk in?"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person "I don't usually demonstrate the goods like this, [the_watcher.fname]. You understand, right?"
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh [the_person.mc_title], [the_watcher.fname] is watching you fuck my brains out!"
        $ the_person.change_arousal(2)
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "Fuck [the_person.mc_title], maybe we should have gone to the back room?"
        $ the_person.change_stats(arousal= -1)
        "[the_person.possessive_title] seems uncomfortable with [the_watcher.fname] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "Ah, now this is a party! Maybe when he's done you can tap in and take a turn [the_watcher.fname]!"
        the_person "Orgy day at Starbuck's Sex Shop... that's actually a pretty good idea!"
        $ the_person.change_stats(arousal = 1, slut = 1, max_slut = 30)
        "[the_person.possessive_title] seems more comfortable [the_position.verbing] you with [the_watcher.fname] around."

    return


label starbuck_flirt_response_low(the_person):
    the_person "Thank you! I thought it looked cute too. Hopefully it helps me sell more product!"
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "[the_person.possessive_title] turns to give you a good look of her and smiles at you."
    $ the_person.draw_person()
    return

label starbuck_flirt_response_mid(the_person):
    if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
        "[the_person.possessive_title] smiles, then glances around nervously."
        the_person "[the_person.mc_title], you're so bad! Hopefully none of my customers heard that..."
        mc.name "They'd probably agree. You're a sexy lady."
        $ mc.change_locked_clarity(10)
        "[the_person.possessive_title] blushes."
        the_person "Well I'm glad you like it. And I'm glad you like me."

    else:
        the_person "Thanks! Same as movies, sex sells! I've seen increased sales since I started dressing like this."
        the_person "Do you want a better look?"
        mc.name "Of course I do."
        $ the_person.draw_person(position = "back_peek")
        the_person "Do you think my ass looks good in it?"
        $ mc.change_locked_clarity(10)
        "She wiggles her hips for you, just a little."
        mc.name "I think it looks great, I wish I could see some more of it."
        $ the_person.draw_person()
        the_person "I'm sure you do. Maybe if you take me to dinner first."
    return

label starbuck_flirt_response_high(the_person):
    if mc.location.person_count > 1 and (the_person.effective_sluttiness("kissing") < 25 and mc.location == sex_store):
        # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "I'd say your chances are actually pretty good, if you don't mind sneaking to the back room with me."
        menu:
            "Find someplace quiet":
                mc.name "Alright, let's do it."
                the_person "Mmm, okay! Let's go!"
                "[the_person.possessive_title] takes your hand and leads you between a few shelves to a door for employees only."
                "You step through and she follows you, locking the door behind her."
                $ the_person.draw_person(position = "kissing")
                "She steps close to you and puts her arms around your waist. She brings her face close to yours."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _starbuck_flirt_response_high_1
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm a patient man, I can wait until you close up tonight."
                $ mc.change_locked_clarity(15)
                "[the_person.possessive_title] blushes and places her hand on your shoulder, massaging your muscles."
                the_person "You sure? Don't be a tease, okay? I want to see you later!"

    else:
        # She wants to kiss you, leading to other things.
        if mc.location.person_count == 1:
            #She's shy about the whole thing.
            "She looks around for a moment, the turns her head back to you."
            the_person "[the_person.mc_title], I... I mean, it's just us here."
            mc.name "So you're saying my chances are good?"
            $ the_person.draw_person(position = "kissing")
            $ mc.change_locked_clarity(15)
            "She takes a step closer to you and puts her arms around your waist, bringing her face close to yours."
            the_person "They could certainly be worse. Let's just... see where things go."

        elif mc.location == sex_store:
            the_person "Maybe we can have some fun. I could call it a product demo?"
            the_person "I bet it would help me move some extra merchandise..."
            mc.name "Oh, so that's why you want to? For the increased revenue?"
            the_person "Well, that, and you are so much fun to play with!"

        else:
            the_person "I don't know, it's kind of busy around here."
            mc.name "Don't worry, I'll make sure every girl here is jealous of how you're getting it."
            the_person "Oh? Those better not be empty words!"

        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                else:
                    pass

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _starbuck_flirt_response_high_2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I wish we could, but I'll need to take a rain check."
                $ the_person.draw_person()
                "[the_person.title] pouts and steps back, disappointed."
                mc.name "Don't worry, we'll get there soon enough. I just want to wait for the right time."
                the_person "Right. Sure."
                "She tries to hide it, but you can tell she's a little disappointed."
    return

init python:
    def starbuck_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        valid_titles.append("Cara")
        return valid_titles

    def starbuck_possessive_titles(person):
        valid_possessive_titles = []
        valid_possessive_titles.append(person.formal_address + " " + person.last_name)
        valid_possessive_titles.append("The sex shop owner")
        if sex_shop_stage() > 1:
            valid_possessive_titles.append("Your business partner")
        if person.sluttiness > 60 and sex_shop_stage() > 1:
            valid_possessive_titles.append("Your slutty business partner")
        if person.sluttiness > 100 and person.sex_skills["Anal"] >= 4:
            valid_possessive_titles.append("Your buttslut")
        if person.has_cum_fetish or person.has_cum_fetish:
            valid_possessive_titles.append("Your cum guzzler")
            valid_possessive_titles.append("Your cum catcher")
        return valid_possessive_titles

    def starbuck_player_titles(person):
        valid_player_titles = []
        valid_player_titles.append("Mr. " + mc.last_name)
        if sex_shop_stage() > 1:
            valid_player_titles.append("Business Partner")
        return valid_player_titles
