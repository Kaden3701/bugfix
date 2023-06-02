## Cougar personality Mod by Tristimdorion
# All girls in town older than 45 get this personality trait
# See generic_personality_hook.rpy for more information

init 3 python:
    def cougar_personality_requirement():
        return True

    def change_cougar_personality_enabled(enabled):
        for person in list_of_people:
            update_cougar_personality(person)
        return

    cougar_personality_action = ActionMod("Cougar Personality", cougar_personality_requirement, "cougar_personality_dummy_label", priority = -10,
        menu_tooltip = "Enable or disable the cougar personality.", category="Personality", on_enabled_changed = change_cougar_personality_enabled)

init 720 python:
    def cougar_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.love > 40:
            valid_titles.append("Cougar")
        if person.sluttiness > 70:
            valid_titles.append("Old Bitch")
        if person.sluttiness > 90 and person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_titles.append("Anal Harlot")
        return valid_titles
    def cougar_possessive_titles(person):
        valid_possessive_titles = []
        valid_possessive_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_possessive_titles.append(person.name)
        if person.sluttiness > 60:
            valid_possessive_titles.append("Your slutty cougar")
        if person.sluttiness > 90 and (person.get_opinion_score("drinking cum") > 0 or person.get_opinion_score("being covered in cum") > 0):
            valid_possessive_titles.append("Your cum-dump cougar")
        if person.sluttiness > 90 and person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_possessive_titles.append("Your anal minx")
        return valid_possessive_titles
    def cougar_player_titles(person):
        valid_player_titles = []
        valid_player_titles.append("Mr. " + mc.last_name)
        if person.happiness < 70:
            valid_player_titles.append("Little Boy")
        if person.love > 25:
            valid_player_titles.append("Darling")
        if person.sluttiness > 60:
            valid_player_titles.append("Young Stud")
        return valid_player_titles

    cougar_personality = Personality("cougar", default_prefix = reserved_personality.default_prefix, #Cougar style personality
        common_likes = ["skirts", "small talk", "Mondays", "the weekend", "the colour red", "makeup", "sports", "flirting", "high heels", "dresses"],
        common_sexy_likes = ["doggy style sex", "giving blowjobs", "getting head", "anal sex", "public sex", "skimpy outfits", "anal creampies", "showing her tits", "showing her ass", "taking control", "not wearing underwear", "creampies", "drinking cum", "cum facials"],
        common_dislikes = ["Mondays", "the colour pink", "conservative outfits", "work uniforms", "pants"],
        common_sexy_dislikes = ["being submissive", "being fingered", "missionary style sex", "bareback sex"],
        titles_function = cougar_titles, possessive_titles_function = cougar_possessive_titles, player_titles_function = cougar_player_titles)

    # don't add it to the default list of personalities, let the generic personality hook change it based on age

label cougar_greetings(the_person):
    if the_person.love < 0:
        the_person "Yes, what do you want?"
    elif the_person.happiness < 90:
        the_person "Hello..."
    else:
        if the_person.obedience > 180:
            if the_person.sluttiness > 60:
                the_person "Hello my boy. Is there anything I can take care of for you?"
            else:
                the_person "Hello young man. I hope everything is going well, if there's anything I can help with let me know."
        else:
            if the_person.sluttiness > 60:
                the_person "Hello [the_person.mc_title], how has your day been? I was... thinking about you, that's all."
            else:
                $ day_part = time_of_day_string(time_of_day)
                the_person "Good [day_part], [the_person.mc_title]!"
    return

label cougar_introduction(the_person): # Copy paste from relaxed to fix crash
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person "I guess? What can I do for you?"
    mc.name "I'm so sorry, I know this is silly but I just couldn't let you walk by without knowing your name."
    "She laughs with a twinkle in her eyes."
    the_person "Is that so? You're trying to impress me, aren't you."
    mc.name "Really, I really just wanted to talk to you."
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Well, if you insist, my name is [formatted_title]. It's nice to meet you..."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    "With a predatory smile, she waits for you to introduce yourself."
    return

label cougar_clothing_accept(the_person):
    if the_person.obedience > 140:
        the_person "Well, if you think I have got the body for it then I'm not going to argue."
        the_person "Thank you for the outfit, [the_person.mc_title]."
    else:
        the_person "Oh that's a nice combination! I'll show it to my friends later and see what they think."
    return

label cougar_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person "I know it would make your day if I wore this for you [the_person.mc_title], but what if my friends saw me in this?"
        the_person "I'm sorry, I know you are disappointed, but I will make it up to you."
    else:
        if the_person.sluttiness > 60:
            the_person "I... [the_person.mc_title], you don't think a woman of my... experience could get away with wearing this, do you?"
            "[the_person.possessive_title] laughs and shakes her head."
            the_person "No, these clothes are for young girls!"
        else:
            the_person "[the_person.mc_title]! I'm a lady, I can't show my face in public with something like that!"
            "[the_person.possessive_title] shakes her head and gives you a scowl."
    return

label cougar_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "Turn around [the_person.mc_title], I'm really not looking ladylike right now. Just give me a moment to get dressed..."
    else:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], I shouldn't be seen like this... Just give me a moment and I'll get dressed."
        elif not the_person.relationship == "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "Oh my, what would my [so_title] say if he saw me here, like this... with you. Turn around, I need to cover myself!"
        else:
            the_person "Oh [the_person.mc_title], I'm not decent! Turn around now, I need to cover myself!"
    return

label cougar_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I know it would make your day [the_person.mc_title], but I don't think I should take my [the_clothing.display_name] off. I'm a lady, after all."
    elif the_person.obedience < 70:
        the_person "Not yet sweety. You just need to relax and let me take care of you."
    else:
        the_person "Don't touch that [the_person.mc_title]. Could you imagine if my [the_clothing.display_name] came off? I could be your mother, we shouldn't do this."
    return

label cougar_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person "Such a nice body you have [the_person.mc_title] and I really want to do this... do you mind?"
        else:
            the_person "Whatever you want me to do [the_person.mc_title]. I just want to make sure you're happy."
    else:
        the_person "Okay, my young lover, let's do it!"
    return

label cougar_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "I know I shouldn't do this, I know I should say no..."
        the_person "But you look so strong and beautiful, please..."
    else:
        if the_person.obedience > 180:
            the_person "I... We really shouldn't... But I know this makes you happy. Let's do it [the_person.mc_title]..."
        else:
            the_person "How does this keep happening [the_person.mc_title]? You know I love you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks away, conflicted."
            if not the_person.relationship == "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I... You just have to make sure my [so_title] never finds out about this. Nobody can know..."
            else:
                the_person "I... You just have to make sure your mom and sister never find out about this. Nobody can know..."
    return

label cougar_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet [the_person.mc_title], I need to get warmed up first. Let's start a little slower and enjoy ourselves."
    else:
        the_person "I... we can't do that [the_person.mc_title]. I could be your mother, there are lines we just shouldn't cross."
    return

label cougar_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "Wait, what? I have a [so_title], what did you think we were going to be doing?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person "Oh god, what did you just say [the_person.mc_title]?"
        the_person "I could be your mother, how could you even think about that!"
    else:
        the_person "What? Oh god, I... I'm too old for you [the_person.mc_title]! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return


label cougar_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh my god! I'm going to... I'm going to..."
        the_person "{b}Cum!{/b} Ah!"
    else:
        the_person "Oh keep doing that [the_person.mc_title], I'm cumming!"
    return

label cougar_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh fuck! Oh fuck, make me cum [the_person.mc_title]!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh my god, I'm going to cum. I'm going to cum!"
        "She closes her eyes and squeals with pleasure."
    return

label cougar_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person "Ah! Yes [the_person.mc_title]! Right there on my... yesss... I'm cumming!"
        "She closes her eyes and goes into a frenzy of multiple orgasms."
    else:
        the_person "Oh god, that's it... keep going... yes [the_person.mc_title]... yes! Yes! YES!"
    return

label cougar_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person "I'm going to cum! Fuck my ass hard and make me cum!"
    else:
        the_person "Oh fuck, I think... I think I'm going to cum!"
    return

label cougar_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Do you need the touch of an experienced woman, [the_person.mc_title]? I know how stressed you can get you."
        else:
            the_person "Oh sweety... What do you need help with, [the_person.mc_title]?"
    else:
        if the_person.sluttiness > 50:
            the_person "Well, how about you let me take care of you for a change?"
        elif the_person.sluttiness > 20:
            the_person "What do you mean, [the_person.mc_title]? Do you want to spend some time with me?"
        else:
            the_person "I'm not sure I understand. What do you need [the_person.mc_title]?"
    return

label cougar_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            "[the_person.possessive_title] pinches your ass cheek, whispering.."
            the_person "You can't say things like that in public [the_person.mc_title]! Think of my reputation."
            "She looks around quickly to see if anyone heard you, then takes your hand in hers."
            the_person "Come on, I'm sure we can find a quiet place were you can take care of me."
        elif the_person.sluttiness < 70:
            "[the_person.possessive_title] smiles and devours your body with her eyes, making sure nobody around you notices."
            the_person "Okay, but we need to be careful. I don't think people would understand our relationship. Let's find someplace quiet."
        else:
            the_person "Oh my, [the_person.mc_title]... why don't you take care of me right here!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person "No point wasting any time, right? I hope my [so_title] won't be too jealous."
        else:
            the_person "Okay, but we need to be careful. I don't want my [so_title] to find out what we're doing."
    return

label cougar_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            the_person "I can't believe I'm saying this... I'll play along for now, but you better not disappoint me."
            mc.name "Of course [the_person.title], I promise."
        elif the_person.sluttiness < 70:
            the_person "Oh [the_person.mc_title], what kind woman would I be if I said no? Come on, let's enjoy ourselves."
        else:
            the_person "Oh [the_person.mc_title], I'm so glad I make you feel this way. Come on, let's get started!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person "Come on [the_person.mc_title], let's get going, screw my [so_title]!"
        else:
            the_person "I have a [so_title], I shouldn't be doing this..."
            "Her eyes tell quite a different story."
    return

label cougar_sex_responses_foreplay(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, you know just what I like, don't you?"
        else:
            the_person "Oh my... that feels very good, [the_person.mc_title]!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person "Keep doing that [the_person.mc_title]... Wow, you're good!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Oh gods above that feels amazing!"
        else:
            the_person "Oh lord... I could get used to you touching me like this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Touch me [the_person.mc_title], I want you to touch me!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I should feel bad... but my egoistic [so_title] never touches me this way!"
                the_person "I need this, so badly!"
        else:
            the_person "I want you to keep touching me, I never guessed a young man could make me feel this way, but I want more of it!"
    return

label cougar_sex_responses_oral(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person "Oh my... that feels..."
            "She sighs happily."
            the_person "Yes, right there!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Yes, just like that! Mmm!"
        else:
            the_person "Keep doing that [the_person.mc_title], it's making me feel... very aroused."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you really know how to put that tongue of yours to good use. That feels amazing!"
        else:
            the_person "Oh lord... your tongue is addictive, I just want more of it!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Oh I need this so badly [the_person.mc_title]! If you keep going you'll make me climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I should feel bad, but you make me feel so good, my worthless [so_title] never does this for me!"
        else:
            the_person "Oh sweet lord in heaven... This feeling is intoxicating!"
    return

label cougar_sex_responses_vaginal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, I love feeling you inside of me!"
        else:
            the_person "Oh lord, you're so big... Whew!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            "[the_person.title] closes her eyes and lets out a loud, sensual moan."
        else:
            the_person "Oh that feels very good, keep doing that!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Yes! Oh god yes, fuck me!"
        else:
            the_person "Oh lord your... cock feels so big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Keep... keep going [the_person.mc_title]! I'm going to climax soon!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Keep going! My [so_title]'s tiny cock never makes me climax and I want it so badly!"
                the_person "I should feel bad, but all I want is your young cock in me right now!"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label cougar_sex_responses_anal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, you feel so big when you're inside me like this."
        else:
            the_person "Be gentle, it feels like you're going to tear me in half!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Give it to me, [the_person.mc_title], give me every last inch!"
        else:
            the_person "Oh god! Oww! Move a little slower..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "I hope my ass isn't too tight for you, I don't want you to cum early."
        else:
            the_person "I don't think I will be able to walk straight after this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Your young cock feels so good stuffed inside me! Keep going, I might actually climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "My [so_title] always wanted to try anal, but I told him it would never happen. My rear entrance belongs to you, [the_person.mc_title]!"
        else:
            the_person "Oh lord, this is actually starting to feel good... If you keep this up, I'm going to cum!"
    return

label cougar_seduction_refuse(the_person):
    if the_person.sluttiness < 30:
        the_person "Oh my god, what are you saying [the_person.mc_title]! Don't you think I'm a little too old for you? I'm sure you can't handle me..."
    elif the_person.sluttiness < 60:
        the_person "I'm sorry [the_person.mc_title], but we really shouldn't do this anymore. It's just... not going to happen."
    else:
        the_person "I'm sorry [the_person.mc_title], I know how much you like to spend time with me, but now isn't a good time for me. I'll make it up to you though, I promise."
    return

label cougar_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            # She's in uniform and likes how it looks.
            the_person "Thank you [the_person.mc_title]. I think these are nice uniforms as well."
            mc.name "It helps having such an attractive employee to wear it."
            $ mc.change_locked_clarity(5)
            "[the_person.possessive_title] smiles."
            the_person "Well, thank you, young man, I appreciate the complement."
        else:
            #She's in uniform, but she thinks it's a little too slutty.
            $ mc.change_locked_clarity(5)
            if the_person.vagina_visible:
                # Her pussy is on display.
                the_person "I would not call it much of an uniform, if you know what I mean."
                the_person "I understand it's the company uniform, but a woman my age would like a little more coverage."
                mc.name "It will take some getting used to, but I think it would be a shame to cover up your wonderful figure."
                "[the_person.possessive_title] doesn't seem so sure, but she smiles and nods anyways."

            elif the_person.tits_visible:
                # Her tits are out
                if the_person.has_large_tits:
                    the_person "Thank you, but I can tell this uniform was designed by a horny boy."
                    the_person "Larger chested women, like myself, appreciate a little more support in their outfits."
                else:
                    the_person "Thank you, but I do hope you'll consider a more respectable uniform in the future."
                    the_person "It still doesn't feel natural showing my goods off like a young girl."
                mc.name "I understand it's a little uncomfortable, but I'm sure you'll get used to it."
                the_person "Perhaps, in time, but for now, I really don't enjoy it at all."

            elif the_person.underwear_visible:
                # Her underwear is visible.
                the_person "Thank you. But this is not appropriate for my age, it should be more descent and respectable, like me."
                mc.name "I know it can take some getting used to, but you look fantastic in it. You definitely have the body to pull this off."
                "[the_person.possessive_title] doesn't seem so sure, but she smiles and nods anyways."

            else:
                # It's just generally slutty.
                "[the_person.possessive_title] smiles warmly."
                the_person "Thank you, although I don't think I would ever wear this if it wasn't company policy."
                mc.name "Well you look fantastic in it either way. Maybe you should rethink your normal wardrobe."
                the_person "I'll think about it."

    else:
        #She's in her own outfit.
        "[the_person.possessive_title] seems caught off guard by the compliment."
        the_person "Oh, thank you! I'm not wearing anything special, it's just one of my normal outfits."
        mc.name "Well, you make it look good."
        $ mc.change_locked_clarity(5)
        "She smiles and laughs insecurely."
        the_person "Boys will be boys."
    return

label cougar_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.tits_visible:
                the_person "What it shows off most are my breasts. I'm not complaining though, between you and me, I kind of like it."
                $ mc.change_locked_clarity(10)
                "She winks and shakes her shoulders, jiggling her tits for you."
            else:
                the_person "With my body and your fashion taste, how could I look bad? These uniforms are very flattering."
                mc.name "It's easy to make a beautiful model look wonderful."
                if the_person.effective_sluttiness() > 20:
                    $ the_person.draw_person(position = "back_peek")
                    the_person "It makes my butt look pretty good too. I don't think that was an accident."
                    $ mc.change_locked_clarity(10)
                    "She gives her ass a little shake."
                    mc.name "It would be a crime to not try and show your nice buttocks off."
                    $ the_person.draw_person()
                "She smiles softly."
                the_person "You know just what to say to make a woman my age feel special."

        else:
            # the_person "I think it shows off a little too much!"
            if the_person.vagina_visible:
                the_person "What doesn't this outfit show off!"

            elif the_person.tits_visible:
                the_person "It certainly shows off my breasts!"

            else:
                the_person "And it shows off a {i}lot{/i} of my body!"

            the_person "I don't mind it so much if it's just me and you, but when there are other people around I wish it kept me a little more covered."
            mc.name "It may take some time to adjust, but with enough time you'll feel perfectly comfortable in it."
            $ mc.change_locked_clarity(10)
            "She smiles and nods."
            the_person "You're right, of course. If you think it's the best option for the company, I trust you."
    else:
        if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
            "[the_person.possessive_title] smiles, then glances around insecurely."
            the_person "Keep your voice down [the_person.mc_title], there are other people around."
            mc.name "I'm sure they're all thinking the same thing."
            $ mc.change_locked_clarity(10)
            "She rolls her eyes and laughs softly."
            the_person "Maybe they are, but it's still embarrassing."
            the_person "You'll have better luck if you save your flattery for when we're alone."
            mc.name "I'll keep that in mind."

        else:
            "[the_person.possessive_title] gives a subtle smile and nods her head."
            the_person "Thank you [the_person.mc_title]. I'm glad you like it... And me."
            the_person "What do you think of it from the back? It's hard for me to get a good look."
            $ the_person.draw_person(position = "back_peek")
            $ mc.change_locked_clarity(10)
            "She turns and bends over a little bit, accentuating her butt."
            if not the_person.wearing_panties and not the_person.vagina_visible: #Not wearing underwear, but you can't see so she coments on it.
                the_person "My panties were always leaving unpleasant lines, so I had to stop wearing them. I hope you can't tell."
            else:
                the_person "Well?"
            mc.name "You look just as fantastic from the back as you do from the front."
            $ the_person.draw_person()
            "She turns back and smiles warmly."
    return

label cougar_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "[the_person.mc_title], there are people around."
        "She bites her lip and leans close to you, whispering in your ear."
        $ mc.change_locked_clarity(15)
        the_person "But if we were alone, maybe we could figure something out..."
        menu:
            "Find someplace quiet":
                mc.name "Follow me."
                "[the_person.possessive_title] nods and follows a step behind you."
                "After searching for a couple of minutes you find a quiet, private space."
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person "And what are you planning now, my young stud?"

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She closes her eyes and leans her body against yours."
                else:
                    "You answer with a kiss. She closes her eyes and leans her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_cougar_flirt_response_high_1
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person "You're a smart boy, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.person_count == 1: #She's shy but you're alone
            "[the_person.title] blushes and stammers out a response."
            the_person "I... I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide how you feel. I feel the same way."
            "She nods and takes a deep breath, steadying herself."
            the_person "Okay, you're right. What are your intentions young man?"

        else:  #You're not alone, but she doesn't care.
            the_person "Well I wouldn't want you to go into a frenzy. You'll just have to find a way to get me out of this outfit..."
            if the_person.has_large_tits: #Bounces her tits for you
                $ the_person.draw_person(the_animation = tit_bob)
                "[the_person.possessive_title] bites her lip sensually and rubs her [the_person.tits_description], while pinching her nipples."

            else: #No big tits, so she can't bounce them (as much
                "[the_person.possessive_title] bites her lip sensually and looks you up and down, as if mentally undressing you."

            the_person "Well, have you made up your mind, my young stud?"

        $ mc.change_locked_clarity(15)

        menu:
            "Kiss her":
                $ the_person.draw_person()
                "You step close to [the_person.title] and put an arm around her waist."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She presses her body up against yours."
                else:
                    "When you lean in and kiss her she responds by pressing her body tight against you."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_person_cougar_flirt_response_high_2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Nothing right now, but I've got a few ideas for later."
                "If [the_person.title] is disappointed she does a good job hiding it. She nods and smiles."
                the_person "Well maybe if you take me out for dinner we can talk about those ideas, I'm interested to hear about them."
    return

label cougar_flirt_response_girlfriend(the_person):
    # Lead in: mc.name "You're so beautiful [the_person.title], I'm so lucky to have a woman like you in my life."
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.get_opinion_score("public_sex"))):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.title] smiles happily."
            the_person "Oh, well thank you [the_person.mc_title]. You're so sweet."
            "She leans in and gives you a quick peck on the cheek."
            the_person "I wish we had a little more privacy. Oh well, maybe later."
            menu:
                "Find someplace quiet":
                    mc.name "Why wait until later? Come on."
                    "You take [the_person.possessive_title]'s hand. She hesitates for a moment, then follows as you lead her away."
                    "After a few minutes of searching you find a quiet spot. You put your arm around [the_person.title]'s waist and pull her close to you."
                    mc.name "So, what did you want that privacy for again?"
                    the_person "Oh, a few things. Let's start with this..."
                    "She leans in and kisses you passionately while rubbing her body against you."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_cougar_flirt_response_girlfriend_1
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "Aw, you're going to make me wait? That's so cruel."
                    $ mc.change_locked_clarity(10)
                    "You reach around and place a hand on [the_person.possessive_title]'s ass, rubbing it gently."
                    "She sighs and bites her lip, then clears her throat and glances around to see if anyone else noticed."
                    the_person "I'll make sure to make it worth the wait, but let's take it easy while other people are around."
                    "You give her butt one last squeeze, then slide your hand off."

        else:
            # the_person "Oh [the_person, mc_title], you're so sweet. Come on, kiss me!"
            "She smiles and sighs happily."
            the_person "Ahh, you're such a sweet boy. Here..."
            "[the_person.possessive_title] leans in and kisses you. Her lips lingering against yours for a few long seconds."
            the_person "Was that nice? You do know how to kiss."
            menu:
                "Make out":
                    "You respond by putting your arm around her waist and pulling her tight against you."
                    "You kiss her, and she eagerly grinds her body against you."
                    call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_cougar_flirt_response_girlfriend_2
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "It was very nice. I've got some other nice things for you to kiss too, if you'd like."
                    if the_person.effective_sluttiness("sucking_cock") >= 60 or the_person.get_opinion_score("giving blowjobs") > 0:
                        "She bites her lip and runs her eyes up and down your body."
                        the_person "Mmmm, stop it [the_person.mc_title]. You're going to get me all wet in public."
                        $ mc.change_locked_clarity(10)
                        "You reach around and place your hand on her ass, rubbing it gently."
                        mc.name "Well we don't want that. I'll keep my thoughts to myself then."
                        "You give her butt one last squeeze, then slide your hand away."
                    else:
                        "She laughs and glances around."
                        the_person "Oh my god, [the_person.mc_title]! Save it for later though, I like what you're thinking..."
    else:
        # You're alone, so she's open to fooling around.
        "She smiles happily."
        the_person "Oh, well thank you [the_person.mc_title]. I'm lucky to have such a handsome boy."
        "[the_person.possessive_title] leans in and kisses you. Her lips linger against yours for a few seconds."
        menu:
            "Kiss her more":
                "You put your arm around her waist and pull her against you, returning her sensual kiss."
                "She presses her body against you and hugs you back. Her hands run down your hips and grab at your ass as you make out."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_cougar_flirt_response_girlfriend_3
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach around [the_person.title] and place a hand on her ass, rubbing it gently. She sighs and leans her body against you."
                $ mc.change_locked_clarity(10)
                the_person "Mmm, that's nice... Maybe when we have some more time together we can take this further."
                mc.name "That sounds like fun. I'm looking forward to it."
                "You give her butt a light slap, then move your hand away."

    return

label cougar_flirt_response_affair(the_person):
    # Lead in: mc.name "You look so good today [the_person.title], you're making me want to do some very naughty things to you."
    $ so_title = SO_relationship_to_title(the_person.relationship) # "husband", "boyfriend", etc.
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.get_opinion_score("cheating on men") *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            the_person "Oh [the_person.mc_title], stop. If you keep talking like that you're going to get me turned on."
            mc.name "And what would be so bad about that?"
            the_person "It would be so frustrating being in public and not being able to do anything to get my satisfaction."
            menu:
                "Find someplace quiet":
                    mc.name "Then let's go find someplace that isn't public. Come on, follow me."
                    "[the_person.possessive_title] glances around, then follows behind you as you search for a quiet spot."
                    "Soon enough you find a place where you and [the_person.title] can be alone."
                    "Neither of you say anything as you put your hands around her and pull her into a tight embrace."
                    "You kiss her, slowly and sensually. She moans and presses her body against you in return."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_cougar_flirt_response_affair_1
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "Well that would just be cruel of me..."
                    $ mc.change_locked_clarity(10)
                    "You put your arm around [the_person.possessive_title] and rest your hand on her ass."
                    mc.name "... If I got you all excited thinking about the next time I'm going to fuck you."
                    "She leans her body against yours for a moment and sighs happily. You give her butt a final slap and let go of her."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title] glances around, then glares at you sternly."
            the_person "[the_person.mc_title], you can't talk like that when there are other people around."
            the_person "You don't want my [so_title] to hear any rumours, do you? If he gets suspicious you might not get to see me so much..."
            "She runs a hand discretely along your arm."
            the_person "That would be such a shame, wouldn't it?"
            mc.name "Alright, I'll be more careful."
            the_person "Thank you. Just hold onto all those naughty thoughts and we can check them off one by one when we're alone."
    else:
        the_person "Oh is that so [the_person.mc_title]? Well, maybe you need to work out some of those naughty instincts..."
        "She stands close to you and runs her hand teasingly along your chest."
        menu:
            "Feel her up":
                mc.name "That sounds like a good idea. Come here."
                "You wrap your arms around [the_person.possessive_title]'s waist, resting your hands on her ass."
                "Then you pull her tight against you, squeezing her tight butt. She sighs happily and starts to kiss your neck."
                "You massage her ass for a moment, then spin her around and cup a tit with one hand. You move your other hand down to caress her inner thigh."
                call fuck_person(the_person, start_position = standing_grope, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_person_cougar_flirt_response_affair_2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I want to, but I'm going to have to wait until we have more time together for that."
                $ mc.change_locked_clarity(10)
                "Her hand moves lower down, brushing over your crotch and sending a brief shiver up your spine."
                the_person "I understand. When we have the chance we'll take our time and really enjoy each other."
    return

label cougar_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title] stop, you're making me horny again..."
        else:
            the_person "Oh stop [the_person.mc_title], it's not nice to make fun of me like that."
            "[the_person.possessive_title] blushes and looks away."
    elif not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 60:
            the_person "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that though, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person "I have a [so_title], you really shouldn't be talking to me like that..."
            "She seems more worried about being caught than flirting with you."
    else:
        if the_person.sluttiness > 50:
            the_person "Oh my... hmm... Thank you, [the_person.mc_title]."
            "[the_person.possessive_title] smiles at you and turns around slowly, giving you a full look at her body."
            the_person "Thank you for noticing me."
        else:
            the_person "Oh [the_person.mc_title], do you think I look good?"
    return

label cougar_flirt_response_text(the_person):
    mc.name "Hey [the_person.title]. Hope you're doing well."
    mc.name "I was thinking of you and wanted to talk."
    "There's a brief pause, then she texts back."
    if the_person.has_role(affair_role):
        the_person "If you were here we could do more than just talk."
        the_person "I hope you don't make me wait too long to see you again."
        mc.name "It won't be long. Promise."

    elif the_person.has_role(girlfriend_role):
        the_person "It's sweet of you to think of me. I hope we can see each other soon."
        the_person "I want to spend more time with you in person. Texting isn't the same."
        mc.name "It won't be long, I promise."

    if the_person.love < 20 and not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "Make it quick [the_person.mc_title]. My [so_title] is watching me."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Are you horny young man? What did you want to talk about?"
        else:
            the_person "Oh, that's nice of you to say."
            the_person "What did you want to talk to me about."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Mhmm, want to tell me about the dirty things you were thinking about me?"
            the_person "That would be something fun to talk about."
        else:
            the_person "It's sweet of you to be thinking of me."
            the_person "I'd love to chat, what would you like to talk about?"
    return

label cougar_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Why don't you wrap that bad boy up, so we can get going."
        if the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            if the_person.on_birth_control:
                the_person "Although I have an IUD, I don't want to surprise my [so_title] with some unexpected consequences."
                $ the_person.update_birth_control_knowledge()
            else:
                the_person "And I don't want to explain to my [so_title] how I got pregnant."
        else:
            the_person "I don't want you to feel bad about getting me pregnant, this is just for fun, right?"
    else:
        the_person "You have a condom with you, right? If not, I have one."
        the_person "And then you can slip that monster right in."
    return

label cougar_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "I have an IUD, so you don't need to put on a condom unless you want to be very safe."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        the_person "Maybe you don't need a condom. Then you can keep fucking me as you cum..."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You could wear a condom, but if you promise to be careful..."
        the_person "Maybe we don't need one, just this once."
    return

label cougar_condom_bareback_ask(the_person):
    if the_person.wants_creampie:
        if the_person.on_birth_control:
            the_person "Don't bother with a condom [the_person.mc_title]. I have an IUD, so it's perfectly safe."
            the_person "You can cum right inside of me, as often as you want."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Don't bother with a condom [the_person.mc_title], we don't need it."
            the_person "I want you to fuck me unprotected and cum inside me, like nature intended."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You don't need to bother with a condom [the_person.mc_title]."
        the_person "It feels so much better without one. You agree, right?"
    return

label cougar_condom_bareback_demand(the_person):
    if the_person.get_opinion_score("bareback sex") > 0 or the_person.get_opinion_score("creampies") > 0: #Just likes raw sex
        if the_person.on_birth_control:
            the_person "You don't need that, I have an IUD."
            the_person "Come on [the_person.mc_title], I want you to cum inside me!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "You don't need to do that, I want to feel you and your cum inside me."
            if the_person.knows_pregnant:
                the_person "I want you [the_person.mc_title], just get over here and fuck me already!"
            else:
                the_person "I don't care if you get me pregnant [the_person.mc_title], just get over here and fuck me already!"
    else:
        if the_person.on_birth_control:
            the_person "You don't need to do that [the_person.mc_title], I have an IUD."
            the_person "So hurry up and fuck me!"
            $ the_person.update_birth_control_knowledge()
        else:
            if the_person.knows_pregnant:
                the_person "Don't waste my time with that thing, just fuck me, stud!"
            else:
                the_person "Don't waste my time with that. I don't care about the risks, I just want you to fuck me!"
    return

label cougar_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("cum facials") > 0:
            $ pronoun = person_body_shame_string(the_person.body_type, "little cum slut")
            the_person "Ah... do you like to see my face covered [the_person.mc_title]? Am I your good [pronoun]?"
        else:
            the_person "Oh, it's everywhere! Next time be more careful, I'm only doing this for you."
    else:
        if the_person.effective_sluttiness() > 70  or the_person.get_opinion_score("cum facials") > 0:
            the_person "Oh, yes [the_person.mc_title], I'm covered with your load!"
        else:
            if the_person.sex_record.get("Cum Facials", 0) < 3:
                the_person "[the_person.mc_title], next time don't mess up my makeup like this."
            elif the_person.sex_record.get("Cum Facials", 0) < 6:
                the_person "Again? Are you not listening? Cum messes up my make up."
            else:
                "[the_person.title] just sighs."
            "She pulls out a tissue and wipes her face quickly."
    return

label cougar_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "It seems I did a good job, you have a wonderful taste [the_person.mc_title]."
        else:
            if the_person.sex_record.get("Cum in Mouth", 0) < 3:
                the_person "I'm not sure I'm really into this, I'll try to like it for you [the_person.mc_title]."
            else:
                "[the_person.title] smiles at you in an obviously fake manner. She clearly doesn't like you cumming in her mouth."
    else:
        if the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, you taste great [the_person.mc_title], you can fill my mouth with your load anytime..."
        else:
            "She spits your cum on the floor..."
            if the_person.sex_record.get("Cum in Mouth", 0) < 4:
                the_person "Give me a little heads up next time, [the_person.mc_title]."
    return

label cougar_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom:
        the_person "Come on [the_person.mc_title], shoot your fertile semen into that condom while you fuck me!"

    else:
        if the_person.wants_creampie:
            if the_person.knows_pregnant: #She's already knocked up, so who cares!
                the_person "Cum for me [the_person.mc_title], I want feel your fertile seed shooting right into me!"
            elif the_person.get_opinion_score("creampies") > 0:
                "[the_person.possessive_title] moans happily."
                if the_person.on_birth_control: #She just likes creampies.
                    the_person "Oh [the_person.mc_title], I want you to cum inside me! I want to feel every last drop of your cum!"
                else: #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    the_person "Oh [the_person.mc_title], I want your strong cum inside me! I want to become pregnant by my beautiful stud!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                the_person "Cum for me! You can let it out whenever you want!"
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Cum for me [the_person.mc_title], I want you to cum for me!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                the_person "Wait! You need to pull out, I don't want to become pregnant!"
            elif the_person.get_opinion_score("creampies") < 0:
                the_person "I want you to pull out, okay? You can finish anywhere but inside of me!"
            else:
                the_person "Just pull out and finish somewhere else [the_person.mc_title]!"
    return

label cougar_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
        the_person "Oh... your fertile seed is so close to me. Just a thin condom keeping your semen from my womb..."
    else:
        the_person "I can feel your young seed pulsing against the condom, it's so strong."
    return

label cougar_cum_vagina(the_person):
    $ so_title = SO_relationship_to_title(the_person.relationship)
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person "Oh... your seed is so close to me. Just a thin, thin condom in the way..."
        else:
            the_person "I can feel your seed through the condom. Well done, there's a lot of it."

    elif the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    elif the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh my... There's so much of it..."
            "She closes her eyes and sighs happily."
            the_person "It's no mystery how you got me pregnant."

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                the_person "You've making such a mess of my pussy. I never let my [so_title] do this to me."
                "She closes her eyes and sighs happily as you cum inside of her."
                the_person "Oh [the_person.mc_title], you turn in me into such a slutty woman."
            else:
                the_person "Oh [the_person.mc_title]... I can feel your cum inside me. It's so warm."
                "She closes her eyes and sighs happily as you cum."

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                the_person "Yes, give me your seed!"
                the_person "If I become pregnant I can say it's my [so_title]'s. I'm sure he would believe it."
            else:
                the_person "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know."
        else:
            if the_person.relationship != "Single":
                the_person "Oh my... That's a lot of cum. It feels so nice."
                the_person "I hope my [so_title] doesn't mind if I get pregnant."
            else:
                the_person "Oh my... That's a lot of cum. It feels so nice."
                the_person "I wonder if today was a risky day? I haven't been keeping track."

    else: #She's angry
        if not the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person "What would I tell my [so_title] if I got pregnant? He might not believe it's his!"
            else:
                the_person "Oh no... You need to cum outside of me [the_person.mc_title]."
                the_person "I'm in no position to be getting pregnant."
                the_person "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."

        elif the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "[the_person.mc_title], I told you to pull out!"
            the_person "I know you're having a good time, but I still have an [so_title], you need to respect my boundaries."

        elif the_person.get_opinion_score("creampies") < 0:
            the_person "[the_person.mc_title], I told you to pull out. Now look at the mess you've made... It's everywhere."

        else:
            the_person "[the_person.mc_title], I told you to pull out. I guess you just lost control."

    return

label cougar_cum_anal(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            $ pronoun = person_body_shame_string(the_person.body_type, "little anal slave")
            the_person "Ah... yes pump your seed into your [pronoun]?"
        else:
            the_person "Oh my, you filled up my bottom, remember [the_person.mc_title], I'm only doing this for you."
    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
            the_person "Cum inside me [the_person.mc_title], fill my ass with your cum!"
        else:
            the_person "Oh lord, I hope I'm ready for this!"
    return

label cougar_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "I hope you don't mind if I slip this off..."
        else:
            the_person "I'm just going to take this off for you [the_person.mc_title]..."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "How about I take this off for you."
        else:
            the_person "Oh [the_person.mc_title], you make me feel so young again!"
            the_person "I really need to take some more off."
    else:
        if the_person.arousal_perc < 50:
            the_person "I'm really horny, I bet you want to see some more of me."
        else:
            the_person "I need to get this off, I want to feel your young body against mine!"
    return

label cougar_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my!","Oh, that's not good!", "Darn!", "Oh!", "My word!", "How about that!", "Shock and horror!", "I'll be jiggered!"])
    the_person "[rando]"
    return

label cougar_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I'm sorry [the_person.mc_title], but I'm busy. Could we talk later?"
        the_person "Maybe you could take me somewhere nice."
    else:
        the_person "I'm sorry [the_person.mc_title], we will have to chit-chat later."
    return

label cougar_sex_watch(the_person, the_sex_person, the_position):
    $ title = the_person.title if the_person.title else "The stranger"
    if the_person.sluttiness < the_position.slut_requirement - 20:
        $ the_person.draw_person(emotion = "angry")
        the_person "[the_person.mc_title]! Why do you want me to watch that!"
        $ the_person.change_stats(happiness = -1, obedience = -2)
        "[title] looks away while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement - 10:
        $ the_person.draw_person(emotion = "sad")
        $ the_person.change_happiness(-1)
        the_person "[the_person.mc_title]! Could you at least try a more private place?"
        "[title] tries to avert her gaze while you and [the_sex_person.fname] [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_requirement:
        $ the_person.draw_person(emotion = "default")
        the_person "[the_person.mc_title], Why are you doing this here..."
        $ the_person.change_slut(1)
        "[title] looks in another direction, but she keeps glancing at you and [the_sex_person.fname]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(emotion = "happy")
        the_person "Oh my [the_person.mc_title]? You might want to teach me that someday..."
        $ the_person.change_slut(2)
        "[title] studies [the_sex_person.fname] while you [the_position.verb] her."

    else:
        $ the_person.draw_person(emotion = "happy")
        $ pronoun = person_body_shame_string(the_sex_person.body_type, "slut")
        the_person "You can do better [the_person.mc_title], give that little [pronoun] what she needs."
        "[title] watches you eagerly while you are [the_position.verbing] [the_sex_person.fname]."

    return

label cougar_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Come on [the_person.mc_title], do me a little harder."
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to [the_watcher.fname]. I'm just taking care of my young [the_person.mc_title]!"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person "[the_person.mc_title], I need you so much. I think [the_watcher.fname] sees that."
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh [the_person.mc_title], I know it's be wrong but being with you right here, just feels so right!"
        $ the_person.change_arousal(1)
        "The longer [the_watcher.fname] keeps watching, the more turned on [the_person.possessive_title] gets."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "[the_person.mc_title], we shouldn't do this. Not here. What would people think of you with an older woman?"
        $ the_person.change_arousal(-1)
        $ the_person.change_slut(-1)
        "[the_person.possessive_title] seems uneasy with [the_watcher.fname] nearby."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "[the_watcher.fname], I'm glad you don't criticize me."
        the_person "People say I shouldn't do this, but this young man makes me feel alive."
        $ the_person.change_arousal(1)
        $ the_person.change_slut(1)
        "[the_person.possessive_title] seems more comfortable [the_position.verbing] you with [the_watcher.fname] around."

    return

label cougar_work_enter_greeting(the_person):
    if the_person.happiness < 80 or the_person.love < 0:
        if the_person.obedience > 120:
            "[the_person.possessive_title] gives you a nod and then turns back to her work."
        else:
            "[the_person.possessive_title] does not acknowledge you when you enter."
    elif the_person.happiness > 120:
        if the_person.sluttiness > 50:
            "[the_person.possessive_title] looks up from her work when you enter the room."
            the_person "Hello [the_person.mc_title]. Let me know if you need my help..."
            "Smiling at you while looking at your crotch, slowly turning back to her work."
        else:
            "[the_person.possessive_title] gives you warm smile."
            the_person "Hello [the_person.mc_title], good to see you!"
    else:
        if the_person.obedience < 90:
            "[the_person.possessive_title] glances up from her work."
            the_person "Hey, how's it going?"
        else:
            "[the_person.possessive_title] looks at you when you enter the room."
            the_person "Hello [the_person.mc_title], let me know if you need any help."
    return

label cougar_date_seduction(the_person): #TODO: Change this to be different.
    $ mc.change_locked_clarity(30)
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "You've been such a good boy tonight. Come with me tonight and I think you can make me feel good too..."
            else:
                the_person "You were a perfect gentleman tonight [the_person.mc_title], would you like to join me at my place?"
        else:
            if the_person.love > 40:
                the_person "I had such a wonderful time tonight. You make me feel so young and alive, want to take a nightcap at my place?"
            else:
                the_person "You've been a wonderful date. Would you like to share a bottle of wine at my place?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "You've been such a good boy tonight. My [so_title] went night fishing with some buddies, so..."
                the_person "Join me tonight and I think you can make me feel good..."
            else:
                the_person "You were a perfect gentleman tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person "He has his poker night with some friends. Would you like to join me at my place and have glass of wine?"
        else:
            if the_person.love > 40:
                the_person "I don't want this night to end. My [so_title] is on a business trip."
                the_person "Do you want to come over to my place so we can spend more time together?"
            else:
                the_person "Tonight was fantastic. I think my [so_title] is out for the night."
                the_person "So do you want to come over to my place for a cup of coffee?"
    return

label cougar_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Is that it? You're going to drive me crazy [the_person.mc_title], I'm so horny..."
            else:
                the_person "All done? I hope you were having a good time."
        else:
            if the_person.arousal_perc > 60:
                the_person "Already done? I don't know how you can stop, I'm so excited at the moment!"
            else:
                the_person "Leaving already? Well, that's disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "That's it? Well, you could at least make me cum too."
            else:
                the_person "All done? Maybe we can pick this up the next time when we're alone."
        else:
            if the_person.arousal_perc > 60:
                the_person "I... I don't know what to say, did I exhaust you?"
            else:
                the_person "That's all you wanted? I guess we're finished then."
    return

label cougar_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "I just can't let you go [the_person.mc_title], You are going to finish what you started!"
    else:
        the_person "Do you think you're going somewhere? You are not yet done [the_person.mc_title]."
    return

label cougar_sex_beg_finish(the_person):
    the_person "Wait, you can't stop now? Come on [the_person.mc_title], I'm almost there, just keep going!"
    return


## Taboo break dialogue ##
label cougar_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, well hello there! Do you... Want to do anything with me?"
    elif the_person.love >= 20:
        the_person "So you feel it too?"
        "She sighs happily."
        the_person "I... I want to kiss you. Would you kiss me?"
    else:
        the_person "I don't know if this is a good idea [the_person.mc_title]..."
        mc.name "Let's just see how it feels. Trust me."
        "[the_person.title] eyes you warily, but you watch her resolve break down."
        the_person "Okay... Just one kiss, to start."
    return

label cougar_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Do you want to know something?"
        mc.name "What?"
        the_person "I've had dreams just like this before. They always stop just before you touch me."
        mc.name "Well, let's fix that right now."

    elif the_person.love >= 20:
        the_person "I want you to know I take this very seriously, [the_person.mc_title]."
        mc.name "Of course. So do I [the_person.title]."
        the_person "I normally wouldn't even think about letting someone like you touch me."
        mc.name "What do you mean, \"someone like me\"?"
        the_person "You're young and reckless. I always get the feeling you're bad news for me, but..."
        the_person "But somehow I just can't say no to you."
    else:
        the_person "You shouldn't be doing this [the_person.mc_title]. We... we barely know each other."
        mc.name "You don't want me to stop though, do you?"
        the_person "I don't... I don't know what I want."
        mc.name "Then let me show you."
    return

label cougar_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Look at how big your penis is. You poor boy, that must be very uncomfortable."
        the_person "Just relax and I'll see what I can do about it, okay?"
    elif the_person.love >= 20:
        the_person "Oh my... If I'm honest I wasn't expecting it to be quite so... Big."
        mc.name "Don't worry, it doesn't bite. Go ahead and touch it, I want to feel your hand on me."
        "She bites her lip playfully."
    else:
        the_person "We should stop here... I don't want you to get the wrong idea about me."
        mc.name "Look at me [the_person.title], I'm rock hard. Nobody would ever know if you gave it a little feel."
        "You see her resolve waver."
        the_person "It is very... Big. Just feel it for a moment?"
        mc.name "Just a moment. No longer than you want to."
        "She bites her lip as her resolve breaks completely."
    return

label cougar_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Do it [the_person.mc_title]. Touch my pussy."
    elif the_person.love >= 20:
        the_person "I'm as nervous as a little girl. Does a grown woman make you feel that way too [the_person.mc_title]?"
        mc.name "Just take a deep breath and relax. You trust me, right?"
        the_person "Of course. I trust you."
    else:
        the_person "I don't know if we should be doing this [the_person.mc_title]..."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Be very careful!"
        mc.name "Just a little. Trust me, it's going to feel amazing."
    return

label cougar_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "What would you like?"
    mc.name "I'd like you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "I... I really should say no."
        mc.name "But you aren't going to."
        "She shakes her head."
        the_person "I've told people all my life that I didn't do things like this, but now it's all I can think about."
    elif the_person.love >= 30:
        the_person "Oh [the_person.mc_title]! Really? I know most men are into that sort of thing, but I..."
        the_person "Well, I think I'm a little more sophisticated than that."
        mc.name "What's not classy about giving your partner pleasure? Come on [the_person.title], aren't you a little curious?"
        the_person "I'm curious, but I... Well... How about I just give it a taste and see how that feels?"
        mc.name "Alright, we can start slow and go from there."
    else:
        the_person "I'm sorry, I think I misheard you."
        mc.name "No you didn't. I want you to put my cock in your mouth and suck on it."
        the_person "I could never do something like that [the_person.mc_title], what would people think?"
        the_person "I'm not some kind of cheap hooker that you pick up on the street, I don't \"suck cocks\"."
        mc.name "Yeah you do, and you're going to do it for me."
        the_person "And why would I do that?"
        mc.name "Because deep down, you want to. You can be honest with me, aren't you a little bit curious what it's going to be like?"
        "She looks away, but you both know the answer."
        mc.name "Just get on your knees, put it in your mouth, and if you don't like how it feels you can stop."
        the_person "What are you doing to me [the_person.mc_title]? I used to think I was better than this..."
    return

label cougar_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Oh what a gentleman I have! Why don't you get down to business, [the_person.mc_title]!"
    elif the_person.love >= 30:
        the_person "You're such a gentleman [the_person.mc_title], but you don't have to do that."
        mc.name "I don't think you understand. I {i}want{/i} to eat you out, I'm not doing it as a favor."
        "[the_person.title] almost seems confused by the idea."
        the_person "Oh... Well then, I suppose you can get right to it."
    else:
        the_person "You're a gentleman [the_person.mc_title], but you don't need to do that."
        if not the_person.has_taboo("sucking_cock"):
            the_person "It's flattering that you'd want to return the favor though, so thank you."

        mc.name "No, I don't think you understand what I'm saying. I {i}want{/i} to eat you out, I'm not doing it as a favor."
        "[the_person.title] almost seems confused by the idea."
        the_person "Really? I mean... I just haven't met many men who {i}want{/i} to do that."
        mc.name "Well you have one now. Just relax and enjoy yourself."
    return

label cougar_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
        "She giggles gleefully."
        the_person "Come on and show me what you can do with that monster!"
    elif the_person.love >= 45:
        the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Oh my god, what am I doing here [the_person.mc_title]?"
            the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
            mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
            "She closes her eyes and takes a deep breath."
            the_person "I... I want to have sex with you. I'm ready."
        else:
            the_person "I'm glad you're doing this properly this time."
            "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return

label cougar_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."

    elif the_person.love >= 60:
        the_person "This is really something you want to do then [the_person.mc_title]?"
        mc.name "Yeah, it is."
        the_person "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person "I don't know if you'll even fit though. You're penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Oh lord, what happened to me?"
            the_person "I thought I was a respectable lady, now I'm about to get fucked in the ass..."
            the_person "We've never even had sex before and now I'm doing anal!"

            #TODO: "At least my vagina still belongs to my SO... At least I still have that one thing."

        else:
            the_person "I'm not sure about this [the_person.mc_title]... I'm not even sure if you can fit inside me there!"
            mc.name "I can stretch you out, don't worry about that."
            the_person "Oh lord, what happened to me..."
            the_person "I used to think I was a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person "I doubt it. Come on then, there's no point stalling any longer."
    return

label cougar_condomless_sex_taboo_break(the_person):
    if the_person.get_opinion_score("bareback sex") > 0:
        the_person "You want to have sex without any protection? I'll admit, that would really turn me on."
        if the_person.on_birth_control:
            the_person "It would be very naughty if you came inside me though..."
            mc.name "Don't you think we're being naughty already?"
            "She bites her lip and nods."
            the_person "I think we are."
        else:
            the_person "You will need to pull out though, I hate having it dripping out of me all day or worse getting pregnant."

    elif the_person.love > 60:
        the_person "If you think you're ready for this commitment, I am too. I want to feel close to you."
        if the_person.get_opinion_score("creampies") > 0:
            the_person "When you're going to finish you don't have to pull out unless you want to. Okay?"
            mc.name "Are you on the pill?"
            if the_person.on_birth_control:
                the_person "I'm taking birth control, so it's okay if you cum inside me."
            else:
                "She shakes her head."
                the_person "No, but I trust you to make the decision that is right for both of us."
        else:
            mc.name "Are you on the pill?"
            if the_person.on_birth_control:
                the_person "I'm taking birth control, but I would like you to cum on me instead of inside me."
            else:
                "She shakes her head."
                if the_person.kids == 0:
                    the_person "I don't want you to make me a mother."
                else:
                    the_person "I've been pregnant enough and you are definitely not ready for daddy duty."
    else:
        the_person "You want to have sex without protection? That's very risky [the_person.mc_title]."
        if the_person.has_taboo("vaginal_sex"):
            mc.name "I want our first time to be special though, don't you?"
            "She takes a second to think, then nods."
            if the_person.on_birth_control:
                the_person "You really want to do it raw? Well, I'm on birth control, so I guess that's okay..."
            else:
                the_person "I do. You need to be very careful where you finish, do you understand?"
        else:
            mc.name "It will feel so much better raw, for both of us."
            the_person "I have wondered what it would be like..."
            if the_person.on_birth_control:
                "She takes a moment to think, then nods."
            else:
                the_person "Fine, you don't need a condom, but be very careful where you finish, do you understand?"
    return

label cougar_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.get_opinion_score("skimpy outfits") * 5):
        the_person "This is the first time you've gotten to see my underwear. I hope you like what you see."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I will. You have good taste."
            the_person "Well then, what are you waiting for then?"
        else:
            mc.name "I've already seen you out of your underwear, but I'm sure it complements your form."
            the_person "Time to find out. What are you waiting for?"

    elif the_person.love > 15:
        the_person "This is going to be the first time you've seen me in my underwear. I have to admit, I'm feeling a little nervous."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Don't be, I'm sure you look stunning in it."
            the_person "Well then, take off my [the_clothing.display_name] for me."

        else:
            mc.name "I already know you have a beautiful body, some nice underwear can only enhance the experience."
            the_person "You're too kind. Help me take off my [the_clothing.display_name]."

    else:
        the_person "If I take off my [the_clothing.display_name] you'll see me in my underwear."
        mc.name "That's the plan, yes."
        the_person "I shouldn't be going around half-naked for men I barely know. What would people think?"

        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Why do you care what other people think? Forget about them and just focus on the moment."
            the_person "I have to keep some kind of decorum, but I am intrigued..."

        else:
            mc.name "You might have wanted to worry about that before I saw you naked. You don't have anything left to hide."
            the_person "I suppose you're right..."
    return

label cougar_bare_tits_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (40 - the_person.get_opinion_score("showing her tits") * 5):
        the_person "Oh, so you want to take a look at my breasts?"
        if the_person.has_large_tits:
            "She bounces her chest for you, jiggling the [the_person.tits_description] hidden underneath her [the_clothing.display_name]."
        else:
            "She bounces her chest and gives her [the_person.tits_description] a little jiggle."
        the_person "Well it would be a shame not to let you get a glimpse, right? I've been waiting for you to ask."
        mc.name "Let's get that [the_clothing.display_name] off so I can see them then."

    elif the_person.love > 25:
        the_person "Oh, you want to get my breasts out?"
        if the_person.has_large_tits:
            "She looks down at her own large rack, tits hidden and restrained by her [the_clothing.display_name]."
            the_person "I don't have to ask why, but I'm glad you're interested in them."
        else:
            the_person "I'm glad you're still interested in smaller breasts. It seems like every man is mad boob-crazy these days."
        mc.name "Of course I'm interested, let's get that [the_clothing.display_name] out of the way so I can get a good look at you."

    else:
        the_person "Young man! If you take off my [the_clothing.display_name] I won't be decent any more!"
        mc.name "I want to see your breasts and it's blocking my view."
        the_person "I'm aware it's \"blocking your view\", that's why I put it on this morning."
        if the_person.has_large_tits and the_clothing.underwear:
            the_person "Besides, a girl like me needs a little support. These aren't exactly light."
        mc.name "Come on [the_person.title]. You're gorgeous, I'm just dying to see more of you."
        the_person "Well I'm glad I have that effect on you. I suppose... I could make an exception..."
        "She takes a moment to think, then sighs and nods."
        the_person "You can take off my [the_clothing.display_name] and have a look. Just be kind to me, I'm feeling very vulnerable."
    return

label cougar_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.get_opinion_score("showing her ass") * 5):
        the_person "You want to get me out of my [the_clothing.display_name]? Well, I'm glad you've finally asked."

    elif the_person.love > 35:
        the_person "Oh, careful there [the_person.mc_title]. If you take off my [the_clothing.display_name] I won't be decent any more."
        if the_person.has_taboo("touching_vagina"):
            mc.name "I don't particularly want you to be decent at the moment, though. I want to get a look at your sweet pussy."
            the_person "Oh stop it, that's no way to talk to a lady."
            "She thinks for a moment, then nods timidly."
            the_person "Okay, you can take it off and have a look, but only this once."

        else:
            mc.name "I think you stopped being decent when you let me touch your pussy."
            the_person "Oh stop, you, I suppose you can take it off and have a look."

    else:
        the_person "Oh! Careful, or you're going to have me showing you everything!"
        mc.name "That is what I was hoping for, yeah."
        the_person "Well! I mean... I'm not that sort of woman [the_person.mc_title]!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Don't you want to be though? Don't you want me to enjoy your body?"
            the_person "I... I mean, I might, but I shouldn't... You shouldn't..."
        else:
            mc.name "Of course you are! I've had my hand on your pussy already, I just want to see what I was feeling before."
            the_person "I... I mean, that wasn't... I..."

        "You can tell her protests are just to maintain her image, and she already knows what she wants."
        mc.name "Just relax and let it happen, you'll have a good time."
    return

# label cougar_facial_cum_taboo_break(the_person):
#     return

# label cougar_mouth_cum_taboo_break(the_person):
#     return

# label cougar_body_cum_taboo_break(the_person):
#     return

label cougar_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Oh lord, I just love getting pumped full with cum!"

        elif the_person.on_birth_control:
            if the_person.relationship != "Single":
                $ so_title = girl_relationship_to_title(the_person.relationship)
                the_person "Oh... I feel like such a bad [so_title], but I think I needed this. I'm sure he would understand."

            else:
                the_person "Oh lord, I've wanted this so badly for so long!"

        elif the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Oh lord, I've needed this so badly!"
                the_person "I don't care about my [so_title], I just want you to treat me like a real woman and get me pregnant!"
            else:
                the_person "Oh lord, I've needed this so badly! I want you to treat me like a real woman and get me pregnant!"

            "She sighs happily."
            the_person "If you've got the energy we should do it again, to give me the best chance."

        else:
            if the_person.relationship != "Single":
                $ so_title = girl_relationship_to_title(the_person.relationship)
                the_person "I can't believe I let you do that... I'm such a terrible [so_title], but it felt so good!"
            else:
                the_person "I can't believe I let you do that, but it feels so good!"

            the_person "I'll just have to hope you haven't gotten me pregnant. We shouldn't do this again, it's too risky."

    else:
        if the_person.knows_pregnant:
            the_person "Well, it's not like I can get more pregnant, but perhaps next time you can cum somewhere else?"

        elif not the_person.on_birth_control:
            the_person "Oh no, did you just finish [the_person.mc_title]?"
            "She sighs unhappily."
            if the_person.relationship != "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "What if I get pregnant now? My [so_title] will start asking a lot of questions. Perhaps I should just fuck him tonight to avoid them."

            else:
                the_person "Have you thought about what you would do if you got this lady pregnant?"

            the_person "Maybe next time you should wear a condom, in case you get carried away again."

        elif the_person.relationship != "Single":
            $ so_title = girl_relationship_to_title(the_person.relationship)
            the_person "[the_person.mc_title], I told you to pull out."
            the_person "I'm already a terrible [so_title] for doing this and you just made me feel even worse."
            the_person "Maybe next time you should wear a condom in case you get too excited again."

        elif the_person.get_opinion_score("creampies") < 0:
            the_person "Oh [the_person.mc_title], I told you to pull out. I hope you're satisfied, you've made such a mess."

        else:
            the_person "[the_person.mc_title], did you just finish inside?"
            the_person "I guess boys will be boys, but try not to make a habit of it when I tell you to pull out."
    return

# label cougar_anal_creampie_taboo_break(the_person):
#     return
