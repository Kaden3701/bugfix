# Alpha Girl personality definition: Mod by Corrado
# Dominating personality applied to all girls with following traits:
# Older than 25, high charisma stat >=5, high intelligence >=4
# Likes or loves "taking control"

init 3 python:
    def alpha_personality_requirement():
        return True

    def change_alpha_personality_enabled(enabled):
        for person in list_of_people:
            update_alpha_personality(person)
        return

    alpha_personality_action = ActionMod("Alpha Personality", alpha_personality_requirement, "alpha_personality_dummy_label", priority = -10,
        menu_tooltip = "Enable or disable the Alpha personality.", category="Personality", on_enabled_changed = change_alpha_personality_enabled)

init 720 python:
    def alpha_titles(person):
        valid_titles = []
        valid_titles.append(person.formal_address + " " + person.last_name)
        if person.love > 20:
            valid_titles.append(person.name)
        if person.sluttiness > 90 and person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_titles.append("Anal Queen")
        return valid_titles

    def alpha_possessive_titles(person):
        valid_possessive_titles = []
        valid_possessive_titles.append(person.formal_address + " " + person.last_name)
        if person.sluttiness > 80 and (person.get_opinion_score("threesomes") > 0 or person.get_opinion_score("other girls") > 0):
            valid_possessive_titles.append("Your bi-sexual queen")
        if person.sluttiness > 90 and person.get_opinion_score("anal sex") > 0 and person.sex_skills["Anal"] > 4:
            valid_possessive_titles.append("Your anal queen")
        return valid_possessive_titles

    def alpha_player_titles(person):
        valid_player_titles = []
        valid_player_titles.append("Mr. " + mc.last_name)
        if person.happiness < 70:
            valid_player_titles.append("Small balls")
        if person.love > 40:
            valid_player_titles.append("Queen's King")
        if person.sluttiness > 60:
            valid_player_titles.append("Queen's Dick")
        return valid_player_titles

    alpha_personality = Personality("alpha", default_prefix = reserved_personality.default_prefix,
        common_likes = ["flirting", "work uniforms", "working", "sports", "small talk", "boots", "dresses", "high heels", "skirts", "the colour black", "the colour red"],
        common_sexy_likes = ["taking control", "threesomes", "getting head", "lingerie", "not wearing underwear", "showing her tits", "showing her ass", "skimpy uniforms"],
        common_dislikes = ["conservative outfits", "pants", "punk music", "the colour green", "the colour pink", "classical music", "jazz"],
        common_sexy_dislikes = ["being submissive", "bareback sex", "being fingered", "missionary style sex"],
        titles_function = alpha_titles, possessive_titles_function = alpha_possessive_titles, player_titles_function = alpha_player_titles)

    # don't add it to the default list of personalities, let the generic personality hook change it based on Charisma

label alpha_greetings(the_person):
    if the_person.love < 0:
        the_person "Yes, what do you want?"
    elif the_person.happiness < 90:
        the_person "Hello..."
    else:
        if the_person.obedience > 100:
            if the_person.sluttiness > 60:
                the_person "Hello [the_person.mc_title]... Is there anything I can manage for you?"
            else:
                the_person "Hello [the_person.mc_title]... Anything I can help you with?"
        else:
            if the_person.sluttiness > 60:
                the_person "Hello [the_person.mc_title], how has your day been? Maybe you can make mine better..."
            else:
                $ day_part = time_of_day_string(time_of_day)
                the_person "Good [day_part], [the_person.mc_title]!"
    return

label alpha_introduction(the_person):
    mc.name "Excuse me, could I bother you for a moment?"
    "She turns around."
    $ the_person.set_title("???")
    the_person "I guess? What can I do for you?"
    mc.name "I know this is strange, but I saw you and I just needed to know your name."
    "She laughs and rolls her eyes."
    the_person "Is that so? You're not the first one... Maybe for today!"
    mc.name "Really, I just wanted to talk to you."
    $ title_choice = the_person.get_random_title()
    $ formatted_title = the_person.create_formatted_title(title_choice)
    the_person "Well, if you insist, you can call me [formatted_title]."
    $ the_person.set_title(title_choice)
    $ the_person.set_possessive_title(the_person.get_random_possessive_title())
    "With a commanding gaze she waits for you to introduce yourself."
    return

label alpha_clothing_accept(the_person):
    if the_person.obedience < 140:
        the_person "Well, I will wear it when I feel like it."
        the_person "Thank you for the outfit, [the_person.mc_title]."
    else:
        the_person "Oh that's a nice combination! I'll try it at home later and see how it fits."
    return

label alpha_clothing_reject(the_person):
    if the_person.obedience > 140:
        the_person "I know it would make your day if I wore this for you [the_person.mc_title]!"
        the_person "I'm sorry, I know you are disappointed, you will need to convince me to wear something like this."
    else:
        if the_person.sluttiness > 60:
            the_person "I... [the_person.mc_title], do you think that's the best for a woman with my... 'assets'?"
            "[the_person.possessive_title] gives you a wink, smiles, but shakes her head."
            the_person "No, you should find something better to wear for me..."
        else:
            the_person "[the_person.mc_title], I'm a lady... I can't show my face in public with something like that!"
            "[the_person.possessive_title] shakes her head and gives you a scowl."
    return

label alpha_clothing_review(the_person):
    if the_person.obedience > 180:
        the_person "Turn around [the_person.mc_title], I'm really not looking ladylike right now. Just give me a moment to get dressed..."
    else:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], you shouldn't see me like this... Just give me a moment and I'll get dressed."
        elif not the_person.relationship == "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            the_person "Oh my, what would my [so_title] say if he saw me here, like this... with you? Turn around, I need to get dressed."
        else:
            the_person "Oh [the_person.mc_title], I'm not at my best! Turn around now, I need to get dressed."
    return

label alpha_strip_reject(the_person, the_clothing, strip_type = "Full"):
    if the_person.obedience > 180:
        the_person "I know it would make your day [the_person.mc_title], but I don't think I should take my [the_clothing.display_name] off. I'm a lady, after all."
    elif the_person.obedience < 70:
        the_person "Not yet [the_person.mc_title]. You just need to relax and let [the_person.title] take care of you."
    else:
        the_person "Don't touch that [the_person.mc_title]. Could you imagine if my [the_clothing.display_name] came off?"
    return

label alpha_sex_accept(the_person, the_position):
    if the_person.sluttiness > 70:
        if the_person.obedience < 100:
            the_person "Such a nice body you have, [the_person.mc_title], and I love sex... Let's give it a try and see how it feels!"
        else:
            the_person "I love sex, [the_person.mc_title], and I love it more when it's with you!"
    else:
        the_person "Okay, let's try this... I hope you know how to treat a real woman during sex!"
    return

label alpha_sex_obedience_accept(the_person):
    if the_person.sluttiness > 70:
        the_person "I know I shouldn't do this, I'm not some cheap slut..."
        the_person "But you look so strong and handsome... Let me feel your body!"
    else:
        if the_person.obedience > 180:
            the_person "I... We really shouldn't... But I know this will make me happy, let's do it [the_person.mc_title]..."
        else:
            the_person "How does this keep happening [the_person.mc_title]? I like you but we shouldn't be doing this..."
            "[the_person.possessive_title] looks straight in your eyes, conflicted."
            if not the_person.relationship == "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Ok... You just have to make sure my [so_title] never finds out about this..."
            elif person.has_role(girlfriend_role):
                the_person "Ok, since you have been so good to me, I will do this for you."
            else:
                the_person "Ok... But this doesn't mean we're more than just friends."
    return

label alpha_sex_gentle_reject(the_person):
    if the_person.sluttiness > 50:
        the_person "Not yet [the_person.mc_title], I need to get warmed up first. Let's start a little slower and enjoy ourselves."
    elif not the_person.relationship == "Single":
        the_person "I... we can't do that [the_person.mc_title]. I'm seeing someone else..."
    else:
        the_person "I can't... at least not yet."
    return

label alpha_sex_angry_reject(the_person):
    if not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "Wait, what? I have a [so_title], what did you think we were going to be doing?"
        "She glares at you and walks away."
    elif the_person.sluttiness < 20:
        the_person "Oh god, what did you just say [the_person.mc_title]?"
        the_person "I'm a lady, how could you even think I would do something like that!"
    else:
        the_person "What? Oh god, [the_person.mc_title], how could you suggest that! We can't do things like that, ever."
        "[the_person.possessive_title] turns away from you."
        the_person "You should go. This was a mistake. I should have known it was a mistake. I don't know what came over me."
    return


label alpha_climax_responses_foreplay(the_person):
    if the_person.sluttiness > 50:
        the_person "Oh, god! I'm almost... I'm going to..."
        the_person "{b}Cum!{/b} Ahhh!"
    else:
        the_person "Oh keep doing that [the_person.mc_title], I'm cumming!"
    return

label alpha_climax_responses_oral(the_person):
    if the_person.sluttiness > 70:
        the_person "Oh fuck! Oh fuck, you're making me cum so hard [the_person.mc_title]!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Oh my god, I'm going to cum. I'm going to cuuuum!"
        "She closes her eyes and squeals with pleasure."
    return

label alpha_climax_responses_vaginal(the_person):
    if the_person.sluttiness > 70:
        the_person "Ah! Yes [the_person.mc_title]! Right there, yes... pump me... I'm cumming!"
        "She closes her eyes and goes into a frenzy of multiple orgasms."
    else:
        the_person "Oh god, that's it... keep going... yes [the_person.mc_title]... yes! Yes! YES!"
    return

label alpha_climax_responses_anal(the_person):
    if the_person.sluttiness > 80:
        the_person "I'm going to cum! Pump my ass hard and make me cum!"
    else:
        the_person "Oh fuck, I think... I think I'm going to cum!"
    return

label alpha_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Do you need the touch of a skilled woman, [the_person.mc_title]? I know how stressed you can get you."
        else:
            the_person "Oh darling... What do you need my help with, [the_person.mc_title]?"
    else:
        if the_person.sluttiness > 50:
            the_person "Well, how about you let me take care of you for a change? I'm the best..."
        elif the_person.sluttiness > 20:
            the_person "What do you mean, [the_person.mc_title]? Do you want to spend some good time with me?"
        else:
            the_person "I'm not sure I understand, what do you need from me [the_person.mc_title]?"
    return

label alpha_seduction_accept_crowded(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            "[the_person.possessive_title] pinches your ass cheek, whispering..."
            the_person "You can't say things like that in public [the_person.mc_title]! Think of my reputation."
            "She looks around quickly to see if anyone heard you, then takes your hand in hers."
            the_person "Come on, I'm sure we can find a quiet place were you can take care of me."
        elif the_person.sluttiness < 70:
            "[the_person.possessive_title] smiles and devours your body with her eyes, making sure nobody around you notices."
            the_person "Okay, but we need to be discreet: I have a reputation to uphold. Let's find someplace quiet."
        else:
            the_person "Oh my, [the_person.mc_title]... why don't you take care of me right here!"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (5*the_person.get_opinion_score("cheating on men")) > 60:
            the_person "No point wasting any time, right? I hope my [so_title] won't be too jealous."
        else:
            the_person "Okay, but we need to be careful. I don't want my [so_title] to find out what we're doing."
    return

label alpha_seduction_accept_alone(the_person):
    if the_person.relationship == "Single":
        if the_person.sluttiness < 35:
            the_person "I can't believe I'm saying this... I'll play along for now, but you better not disappoint me."
            mc.name "Of course [the_person.title], I promise."
        elif the_person.sluttiness < 70:
            the_person "Oh [the_person.mc_title], what kind of goddess would I be if I said no? Come on, let's enjoy ourselves."
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

label alpha_sex_responses_foreplay(the_person):
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
            the_person "Oh gods, that feels amazing!"
        else:
            the_person "Oh lord... I could get used to you touching me like this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Touch me [the_person.mc_title], I want you to touch me!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "I should feel bad... but my selfish [so_title] never touches me this way!"
                the_person "I need this, so badly!"
        else:
            the_person "I want you to keep touching me, I'd never guessed you could make me feel this way, but I want more!"
    return

label alpha_sex_responses_oral(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title], you're so good to me."
        else:
            the_person "Oh my... that feels..."
            "She sighs happily."
            the_person "Yes, right there!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Yes, just like that! Mmmmmh!"
        else:
            the_person "Keep doing that [the_person.mc_title], it excites me so badly!"

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "Mmm, you really know how to put that tongue of yours to good use. That feels amazing!"
        else:
            the_person "Oh lord... your tongue is addictive, I just want more and more of it!"
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

label alpha_sex_responses_vaginal(the_person):
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
            the_person "Yes! Oh god yes, fill me!"
        else:
            the_person "Oh lord your... cock feels so big!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Keep... keep going [the_person.mc_title]! I'm going to climax soon!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Keep going! My [so_title]'s tiny cock never makes me climax and I want it so badly!"
                the_person "I should feel bad, but all I want is your cock in me right now!"
        else:
            "[the_person.title]'s face is flush as she pants and gasps."
    return

label alpha_sex_responses_anal(the_person):
    if the_person.arousal_perc < 40:
        if the_person.sluttiness > 50:
            the_person "Mmm, you feel so big when you're inside me like this."
        else:
            the_person "Be gentle, it feels like you're going to tear me in half!"

    elif the_person.arousal_perc < 65:
        if the_person.sluttiness > 50:
            the_person "Give it to me, [the_person.mc_title], give me every last inch!"
        else:
            the_person "Oh god! Owwww! Move a little slower..."

    elif the_person.arousal_perc < 90:
        if the_person.sluttiness > 50:
            the_person "I hope my ass isn't too tight for you, I don't want you to cum too early."
        else:
            the_person "I think I'll have some problems walking in public after this!"
    else:
        if the_person.sluttiness > 50:
            if the_person.relationship == "Single":
                the_person "Your cock feels like it was made to perfectly fill me! Keep going, I might actually climax!"
            else:
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "My [so_title] gave me some anal, but I never felt like this, you can take my ass anytime, [the_person.mc_title]!"
        else:
            the_person "Oh lord, this is actually starting to feel good, keep this up, Yes, I'm going to cum!"
    return

label alpha_seduction_refuse(the_person):
    if the_person.sluttiness < 30:
        the_person "Oh my god, what are you saying [the_person.mc_title]! Don't you think I'm a little too much for you? I'm sure you can't handle me."
    elif the_person.sluttiness < 60:
        the_person "I'm sorry [the_person.mc_title], but we really shouldn't do this anymore. It's just... not going to happen."
    else:
        the_person "I'm sorry [the_person.mc_title], I know how much you appreciate me, but now isn't a good time for me."
    return

label alpha_flirt_response_low(the_person):
    if the_person.outfit == the_person.planned_uniform:
        $ mc.change_locked_clarity(5)
        if the_person.judge_outfit(the_person.outfit):
            # She's in uniform and likes how it looks.
            the_person "Thank you [the_person.mc_title]. I think these are nice uniforms as well."
            mc.name "It helps having such an attractive employees to wear it."
            "[the_person.possessive_title] smiles."
            the_person "Well, thank you, I agree, I do look good."
        else:
            #She's in uniform, but she thinks it's a little too slutty.
            if the_person.vagina_visible:
                # Her pussy is on display.
                the_person "I would not call it much of an uniform, this is not how a lady like me should dress."
                the_person "I understand it's the company uniform, but not all women could wear it like me."
                mc.name "It will take some getting used to, but I think it would be a shame to cover up your wonderful figure."
                "[the_person.possessive_title] smiles and nods, she's so full of herself..."

            elif the_person.tits_visible:
                # Her tits are out
                if the_person.has_large_tits:
                    the_person "Thank you, but I can tell this uniform was designed by an overexcited, horny man."
                    the_person "Large chested women, like myself, appreciate a little more support in their outfits to show off their best feature."
                else:
                    the_person "Thank you, but I do think you should consider a more respectable uniform in the future."
                    the_person "It's not my first choice to show my goods in the workplace, like a cheap bimbo."
                mc.name "I understand it's a little uncomfortable, but I'm sure you'll get used to it."
                the_person "Perhaps, in time, but for now I really don't enjoy it at all."

            elif the_person.underwear_visible:
                # Her underwear is visible.
                the_person "Thank you. But this is not appropriate for a lady, it should be more decent and respectable, like me."
                mc.name "I know it can take some getting used to, but you look fantastic in it. You definitely have the body to pull this off."
                "[the_person.possessive_title] smiles and nods, she's so full of herself..."

            else:
                # It's just generally slutty.
                "[the_person.possessive_title] smiles warmly."
                the_person "Thank you, although I don't think I would ever wear this if it wasn't company policy."
                mc.name "Well you look fantastic in it either way. Maybe you should rethink your normal wardrobe."
                the_person "My wardrobe is damn perfect! Don't you suggest otherwise."

    else:
        #She's in her own outfit.
        "[the_person.possessive_title] seems caught off guard by the compliment."
        the_person "Oh, thank you! I'm not wearing anything special, it's just one of my normal outfits."
        mc.name "Well, you make it look good."
        $ mc.change_locked_clarity(5)
        "She smiles and laughs proud of herself."
        the_person "Men will always be men."
    return

label alpha_flirt_response_mid(the_person):
    if the_person.outfit == the_person.planned_uniform:
        if the_person.judge_outfit(the_person.outfit):
            if the_person.tits_visible:
                the_person "What it shows off most are my breasts. I'm not complaining though, between you and me, I kind of like it."
                $ mc.change_locked_clarity(10)
                "She winks and shakes her shoulders, jiggling her tits for you."
            else:
                the_person "With my body and your fashion taste, how could I look bad? This uniforms is very flattering."
                mc.name "It's easy to make a beautiful woman look wonderful."
                if the_person.effective_sluttiness() > 20:
                    $ the_person.draw_person(position = "back_peek")
                    the_person "It makes my butt look pretty good too. I don't think that was an accident."
                    "She gives her ass a little shake."
                    $ mc.change_locked_clarity(10)
                    mc.name "It would be a crime not to try and show your nice buttocks off."
                    $ the_person.draw_person()
                "She smiles wickedly."
                the_person "You know just what to say to make a woman feel special."

        else:
            # the_person "I think it shows off a little too much!"
            if the_person.vagina_visible:
                the_person "What doesn't this outfit show off!"

            elif the_person.tits_visible:
                the_person "It certainly shows off my breasts!"

            else:
                the_person "And it shows off a {i}lot{/i} of my body!"

            the_person "The workplace isn't my best choice to show so much skin, someone else would have much bigger problem than me."
            mc.name "It may take some time to adjust, but with enough time you'll feel perfectly comfortable in it."
            $ mc.change_locked_clarity(10)
            "She smiles and nods."
            the_person "I already feel perfectly comfortable in it, I just don't know if everybody else here would feel the same way!"
    else:
        if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
            "[the_person.possessive_title] smiles, then glances around."
            the_person "Keep your voice down [the_person.mc_title], there are other people around."
            mc.name "I'm sure they're all thinking the same thing."
            $ mc.change_locked_clarity(10)
            "She rolls her eyes and laughs softly."
            the_person "Maybe they are, but it's still embarrassing."
            the_person "You'll have better luck if you save your flattery for when we're alone."
            mc.name "I'll keep that in mind."

        else:
            "[the_person.possessive_title] gives a subtle smile and nods her head."
            the_person "Thank you [the_person.mc_title]. I'm glad you like it."
            the_person "What do you think of it from the back? Do I look good from this angle?"
            $ the_person.draw_person(position = "back_peek")
            "She turns and bends over a little bit, accentuating her butt."
            if not the_person.wearing_panties and not the_person.vagina_visible: #Not wearing underwear, but you can't see so she coments on it.
                the_person "My panties were always leaving unpleasant lines, so I had to stop wearing them."
            else:
                the_person "Well?"
            $ mc.change_locked_clarity(5)
            mc.name "You look just as fantastic from the back as you do from the front."
            $ the_person.draw_person()
            "She turns back and smiles, proud of herself."
    return

label alpha_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness() < (25 - (5*the_person.get_opinion_score("public_sex"))): # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "[the_person.mc_title], there are people around."
        "She bites her lip and leans close to you, whispering in your ear."
        $ mc.change_locked_clarity(15)
        the_person "But if we were alone, I might show you a little more, if you behave."
        menu:
            "Find someplace quiet":
                mc.name "Come with me."
                "[the_person.possessive_title] nods and follows a step behind you."
                "You walk down the corridor into an empty office space."
                "Once you're alone you put one hand around her waist, pulling her close against you. She looks into your eyes."
                the_person "And what are you planning now that you won the big prize?"

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")
                    "You lean in and kiss her. She closes her eyes and leans her body against yours."
                else:
                    "You answer with a kiss. She closes her eyes and leans her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_high_1
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'll just have to figure out how to get you alone then. Any thoughts?"
                the_person "You're smart enough, you'll figure something out."
                "She leans away from you again and smiles mischievously."

    else:
        if mc.location.person_count == 1: #She's shy but you're alone
            "[the_person.title] blushes and responds."
            the_person "I don't know what you mean [the_person.mc_title]."
            mc.name "It's just the two of us, you don't need to hide your feelings... I feel the same way."
            $ mc.change_locked_clarity(15)
            "She nods and takes a deep breath..."
            the_person "Okay, you might be right. What are your intentions now?"

        else:  #You're not alone, but she doesn't care.
            the_person "Well I wouldn't want you to go into a frenzy. You'll just have to find a way to get me out of this outfit..."
            if the_person.has_large_tits: #Bounces her tits for you
                $ the_person.draw_person(the_animation = tit_bob)
                "[the_person.possessive_title] bites her lip sensually and rubs her [the_person.tits_description], while pinching her nipples."

            else: #No big tits, so she can't bounce them
                "[the_person.possessive_title] bites her lip sensually and looks you up and down, as if she's mentally undressing you."

            $ mc.change_locked_clarity(15)
            the_person "Well, have you made up your mind, [the_person.mc_title]?"

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
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_person_alpha_flirt_response_high_2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                $ the_person.draw_person()
                mc.name "Nothing right now, but I've got a few ideas for later."
                "If [the_person.title] is disappointed she does a good job hiding it. She nods and smiles."
                the_person "Well maybe if you take me out for dinner we can talk about those ideas, I would like you to elaborate."
    return

label alpha_flirt_response_girlfriend(the_person):
    if mc.location.person_count > 1:
        # There are other people around, so she'll only start making out with you if she's slutty.
        if the_person.effective_sluttiness("kissing") < (25 - (5*the_person.get_opinion_score("public_sex"))):
            # Not very slutty, so she wants to find somewhere private
            "[the_person.title] smiles happily."
            the_person "Oh, well thank you [the_person.mc_title]. You're so sweet."
            "She leans in and squeezes you package while giving you a peck on the cheek."
            the_person "I wish we had a little more privacy, but that will have to wait."
            menu:
                "Find someplace quiet":
                    mc.name "Why wait until later? Come on."
                    "You take [the_person.possessive_title]'s hand. She hesitates for a moment, then follows as you lead her away."
                    "After a few minutes of searching you find a quiet spot. You put your arm around [the_person.title]'s waist and pull her close to you."
                    mc.name "So, what did you want that privacy for again?"
                    the_person "Oh, a few things. Let's start with this."
                    "She leans in and kisses you passionately while rubbing her body against you."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_girlfriend_1
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "Aw, you're going to make me wait? That's so cruel."
                    $ mc.change_locked_clarity(10)
                    "You reach around and place a hand on [the_person.possessive_title]'s ass, rubbing it gently."
                    "She sighs and bites her lip, then clears her throat and glances around to see if anyone else noticed."
                    the_person "I'm sure we can find a way for you to satisfy me, but let's take it easy while other people are around."
                    "You give her butt one last squeeze, then slide your hand off."

        else:
            "She smiles with a smirk."
            the_person "Ahh, you're so nice. Here..."
            "[the_person.possessive_title] leans in and kisses you. Her lips lingering against yours for a few long seconds."
            the_person "That was nice, you do know how to kiss."
            menu:
                "Make out":
                    "You respond by putting your arm around her waist and pulling her tight against you."
                    "You kiss her, and she eagerly grinds her body against you."
                    call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_girlfriend_2
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
                        the_person "We will see about that, [the_person.mc_title]! I might have some places you may kiss..."
    else:
        # You're alone, so she's open to fooling around.
        "She smiles happily."
        the_person "Oh, well thank you [the_person.mc_title]. You might pleasure me again soon."
        "[the_person.possessive_title] leans in and kisses you. Her lips linger against yours for a few seconds."
        menu:
            "Kiss her more":
                "You put your arm around her waist and pull her against you, returning her sensual kiss."
                "She presses her body against you and hugs you back. Her hands run down your hips and grab at your ass as you make out."
                call fuck_person(the_person, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_girlfriend_3
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                "You reach around [the_person.title] and place a hand on her ass, rubbing it gently. She sighs and leans her body against you."
                the_person "Mmm, that's nice, when we have some more time together you can show me what else you can do."
                mc.name "That sounds like fun. I'm looking forward to it."
                $ mc.change_locked_clarity(10)
                "You give her butt a light slap, then move your hand away."
    return

label alpha_flirt_response_affair(the_person):
    $ so_title = SO_relationship_to_title(the_person.relationship) # "husband", "boyfriend", etc.
    if mc.location.person_count > 1: #There are other people around, she's nervous about people finding out what you're doing.
        if (the_person.get_opinion_score("cheating on men") *15) + the_person.effective_sluttiness() > 50: #SHe's turned on by flirting in public or doesn't think anything is wrong with it
            the_person "Oh [the_person.mc_title], stop. If you keep talking like that you might get me excited."
            mc.name "And what would be so bad about that?"
            the_person "It would be so frustrating being in public and not being able to get my satisfaction."
            menu:
                "Find someplace quiet":
                    mc.name "Then let's go find someplace that isn't public. Come on, follow me."
                    "[the_person.possessive_title] glances around, then follows behind you as you search for a quiet spot."
                    "Soon enough you find a place where you and [the_person.title] can be alone."
                    "Neither of you say anything as you put your hands around her and pull her into a tight embrace."
                    "You kiss her, slowly and sensually. She moans and presses her body against you in return."
                    call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_person_alpha_flirt_response_affair_1
                    $ the_person.call_dialogue("sex_review", the_report = _return)
                    $ the_person.review_outfit()

                "Just flirt":
                    mc.name "Well that would just be cruel of me..."
                    $ mc.change_locked_clarity(10)
                    "You put your arm around [the_person.possessive_title] and rest your hand on her ass."
                    mc.name "... If I got you all excited thinking about the next time I'm going to fuck you."
                    "She leans her body against yours for a moment and squeezes your cock. You give her butt a final slap and let go of her."

        else: #She's shy or nervous about being discovered
            "[the_person.possessive_title] glances around, then glares at you sternly."
            the_person "[the_person.mc_title], you can't talk like that when there are other people around."
            the_person "You don't want my [so_title] to hear any rumours, do you? This thing would end so fast, you would regret it."
            "She runs a hand discretely along your arm."
            the_person "That would be a real shame, wouldn't it?"
            mc.name "Alright, I'll be more careful."
            the_person "Thank you. Just hold onto all those naughty thoughts and we can check them off one by one when we're alone."
    else:
        the_person "Oh is that so [the_person.mc_title]? Well, maybe you need to work out some of those naughty instincts..."
        "She stands close to you and runs her hand teasingly along your chest."
        menu:
            "Feel her up":
                mc.name "That sounds like a good idea. Come here."
                "You wrap your arms around [the_person.possessive_title]'s waist, resting your hands on her ass."
                "Then you pull her tight against you, squeezing her tight butt."
                "She quickly turns around and puts your hand between her thighs."
                call fuck_person(the_person, private = True, start_position = standing_grope, skip_intro = True) from _call_fuck_person_alpha_flirt_response_affair_2
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I want to, but I'm going to have to wait until we have more time together for that."
                $ mc.change_locked_clarity(10)
                "Her hand moves lower, until she reaches you crotch, giving your cock a squeeze, sending a brief shiver up your spine."
                the_person "I understand. When we have the chance you can take your time and give me some pleasure."
    return

label alpha_flirt_response(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 50:
            the_person "Oh [the_person.mc_title] stop that, you're making me horny again."
        else:
            the_person "Oh stop [the_person.mc_title], it's not nice to make fun of a lady like that."
            "[the_person.possessive_title] looks away."
    elif not the_person.relationship == "Single":
        $so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness + (the_person.get_opinion_score("cheating on men")*5) > 60:
            the_person "Well thank you [the_person.mc_title]. Don't let my [so_title] hear you say that, he might get jealous."
            "She smiles and winks mischievously."
        else:
            the_person "I have a [so_title], so you really shouldn't be talking to a lady like that..."
            "She looks around, but you can definitely see a slight smile on her face."
    else:
        if the_person.sluttiness > 50:
            the_person "Thank you, [the_person.mc_title]."
            "[the_person.possessive_title] smiles at you and turns around slowly, giving you a full look at her body."
            the_person "I know you cannot take those greedy eyes off me."
        else:
            the_person "Well, I do look good, don't I [the_person.mc_title]?"
    return

label alpha_flirt_response_text(the_person):
    mc.name "Hey [the_person.title]. Hope you're doing well."
    mc.name "I was thinking of you and wanted to talk."
    "There's a brief pause, then she texts back."
    if the_person.has_role(affair_role):
        the_person "Next time, come visit me, so we could do more than just talk."
        the_person "And don't make me wait too long, I might find someone else to please me."
        mc.name "I will, I promise."

    elif the_person.has_role(girlfriend_role):
        the_person "You should think of me. We should see each other soon."
        the_person "So we can spend more time in person. Texting isn't the same."
        mc.name "I will, I promise."

    if the_person.love < 20 and not the_person.relationship == "Single":
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "Make it quick [the_person.mc_title]. My [so_title] is watching me."

    elif the_person.love < 40:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Are you getting exited thinking about me? What did you want to talk about?"
        else:
            the_person "What do you want to talk about."

    else:
        if the_person.effective_sluttiness() > the_person.love:
            the_person "Mhmm, tell me about the ways you want to please me?"
        else:
            the_person "We can chat for a while, what would you like to talk about?"
    return

label alpha_condom_demand(the_person):
    if the_person.wants_creampie:
        the_person "Put some rubber on that that bad boy up, so we can get going."
        if the_person.relationship != "Single":
            $ so_title = SO_relationship_to_title(the_person.relationship)
            if the_person.on_birth_control:
                the_person "Although I have an IUD, My [so_title] doesn't need any surprises and unwanted consequences."
                $ the_person.update_birth_control_knowledge()
            else:
                the_person "And I don't want to tell my [so_title] that I'm pregnant."
        else:
            the_person "I don't want you to knock me up, this is just for fun!"
    else:
        the_person "You have a condom with you, if not, I have one for you."
        the_person "After you put it on, you can slip that monster right in."
    return

label alpha_condom_ask(the_person):
    if the_person.on_birth_control:
        the_person "I have an IUD, so we don't need a condom."
        $ the_person.update_birth_control_knowledge()
    elif the_person.wants_creampie:
        if the_person.get_opinion_score("creampies" > 0):
            the_person "You don't need a condom, so you can keep fucking me as you cum..."
        else:
            the_person "You don't need a condom, so you can cover me with that cum..."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You could wear a condom, but I prefer if you..."
        the_person "just do it without and be careful."
    return

label alpha_condom_bareback_ask(the_person):
    if the_person.get_opinion_score("bareback sex") > 0:
        if the_person.on_birth_control:
            the_person "Don't bother with a condom [the_person.mc_title]. I have long term protection."
            if the_person.wants_creampie:
                the_person "You can cum right inside of me, as often as I need."
            else:
                the_person "And I want you to cover me with your cum."
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "Don't bother with a condom [the_person.mc_title], we don't need it."
            if the_person.wants_creampie:
                the_person "I want you to fuck me unprotected and cum inside me, like nature intended."
            else:
                the_person "I want you to fuck me hard and cover me with that cum."
        $ the_person.discover_opinion("creampies")
    else:
        the_person "You don't need to bother with a condom [the_person.mc_title]."
        the_person "It feels so much better without one. Come on, get going."
    return

label alpha_condom_bareback_demand(the_person):
    if the_person.wants_creampie: #Just likes raw sex
        if the_person.on_birth_control:
            the_person "You don't need that, get that cock over here."
            the_person "Come on [the_person.mc_title], I want you to cum inside me!"
            $ the_person.update_birth_control_knowledge()
        else:
            the_person "You don't need to do that, I want to feel you and your cum all over me."
            if the_person.knows_pregnant:
                the_person "Come on [the_person.mc_title], just get over here and fuck me already!"
            else:
                the_person "I don't care if you get me pregnant [the_person.mc_title], just get over here and fuck me already!"
    else:
        if the_person.on_birth_control:
            the_person "You don't need that [the_person.mc_title], I am protected."
            the_person "So hurry up and fuck me!"
            $ the_person.update_birth_control_knowledge()
        else:
            if the_person.knows_pregnant:
                the_person "Don't waste my time with that. Stick your dick in me and fuck me!"
            else:
                the_person "Don't waste my time with that. I don't care about the risks, I just want you to fuck me!"
    return

label alpha_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("cum facials") > 0:
            $ pronoun = person_body_shame_string(the_person.body_type, "little cum slut")
            the_person "Do you like to see my face covered [the_person.mc_title]? Am I your good [pronoun]?"
        else:
            the_person "It's everywhere! Next time point that thing somewhere else, I'm only doing this for you as a favor."
    else:
        if the_person.effective_sluttiness() > 70  or the_person.get_opinion_score("cum facials") > 0:
            the_person "Oh, yes [the_person.mc_title], I'm covered with your load, this is soo good for my skin!"
        else:
            if the_person.sex_record.get("Cum Facials", 0) < 3:
                the_person "[the_person.mc_title], next time don't mess up my makeup like this."
            elif the_person.sex_record.get("Cum Facials", 0) < 6:
                the_person "Again? Are you not listening? Cum messes up my make up. Perhaps I should not do this anymore."
            else:
                $ the_person.change_happiness(-5)
                "[the_person.title] glares at you with an icy gaze."
            "She pulls out a tissue and wipes her face quickly."
    return

label alpha_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "It seems I did a good job, you do taste pretty good, [the_person.mc_title]."
        else:
            if the_person.sex_record.get("Cum in Mouth", 0) < 3:
                the_person "I'm really not into this, but I will make an exception for now, [the_person.mc_title]."
            else:
                "[the_person.title] looks at you with a cold stare. She clearly doesn't like you cumming in her mouth."
    else:
        if the_person.effective_sluttiness() > 70 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "You do taste better than others [the_person.mc_title], you may fill my mouth with your load when I feel like it..."
        else:
            "She spits your cum on the floor..."
            if the_person.sex_record.get("Cum in Mouth", 0) < 4:
                the_person "You need to give me a warning next time, [the_person.mc_title]."
    return

label alpha_cum_vagina(the_person):
    if mc.condom:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            the_person "Your seed is so close to me. Just a thin layer of latex separates it from me..."
        else:
            the_person "I can feel your seed through the condom. Well done, there's a lot of it."

    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("creampies") > 0:
            if the_person.relationship!= "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                the_person "Yes, give me your seed!"
                if the_person.on_birth_control:
                    the_person "Luckily I cannot get pregnant, but if I did, my [so_title] would believe it's his."
                else:
                    the_person "If I become pregnant I will tell my [so_title]'s it's his, I'm sure he will accept that."
            else:
                if the_person.on_birth_control:
                    the_person "Mmm, your semen feels warm and sticky, good thing I cannot get pregnant, because this might have done it."
                else:
                    the_person "Mmm, your semen is so nice and warm. I wonder how potent it is. You might have gotten me pregnant, you know."
        else:
            if the_person.relationship!= "Single":
                $ so_title = SO_relationship_to_title(the_person.relationship)
                if the_person.on_birth_control:
                    the_person "Oh yes, give me your hot cum right now."
                    the_person "My [so_title] hasn't satisfied me like this for months."
                else:
                    the_person "Oh shit, you needed to cum outside, [the_person.mc_title]."
                    the_person "What would I tell my [so_title] if I got pregnant, he might not believe it's his!"
            else:
                if the_person.on_birth_control:
                    the_person "Oh yes, shoot that hot cum right inside me."
                    the_person "Perhaps I should stop taking the pill and get pregnant, it would be nice to be a mother."
                else:
                    the_person "Oh FUCK, [the_person.mc_title], I told you not to cum inside me."
                    the_person "I'm in no position to be getting pregnant."
                    the_person "Well, I suppose you have me in the literal position to get pregnant, but you know what I mean."
    return

label alpha_cum_anal(the_person):
    if the_person.obedience > 180:
        if the_person.sluttiness > 90:
            $ pronoun = person_body_shame_string(the_person.body_type, "little anal queen")
            the_person "Ah... yes pump your seed into your [pronoun]?"
        else:
            the_person "Oh my, you filled up my bottom... Remember [the_person.mc_title], you're the only one I let do this."
    else:
        if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
            the_person "Cum inside me [the_person.mc_title], fill my beautiful ass with your cum!"
        else:
            the_person "Oh lord, I hope I'm ready for this!"
    return

label alpha_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "I hope you don't mind if I slip this off..."
        else:
            the_person "I'm just going to take this off for you [the_person.mc_title]..."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "How about I take this off for you."
        else:
            the_person "Oh [the_person.mc_title], you make me feel even more beautiful than I am!"
            the_person "I really need to take some more off and show my perfect body."
    else:
        if the_person.arousal_perc < 50:
            the_person "I'm really horny: I bet you want to see some more of me."
        else:
            the_person "I need to get this off, I want to feel your body against mine!"
    return

label alpha_surprised_exclaim(the_person):
    $rando = renpy.random.choice(["Oh my!","Oh, that's not good!", "Darn!", "Oh!", "My word!", "How about that!", "Shock and horror!", "I'll be jiggered!"])
    the_person "[rando]"
    return

label alpha_talk_busy(the_person):
    if the_person.obedience > 120:
        the_person "I'm sorry [the_person.mc_title], but I'm busy. We should talk later."
        the_person "You should take me somewhere nice, like a theater or a restaurant."
    else:
        the_person "I'm sorry [the_person.mc_title], we will have to chit-chat later."
    return

label alpha_sex_watch(the_person, the_sex_person, the_position):
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
        the_person "[the_person.mc_title], why are you doing this here..."
        $ the_person.change_slut(1)
        "[title] looks in another direction, but she keeps glancing at you and [the_sex_person.fname]."

    elif the_person.sluttiness > the_position.slut_requirement and the_person.sluttiness < the_position.slut_cap:
        $ the_person.draw_person(emotion = "happy")
        the_person "Well, [the_person.mc_title]! I might show you my personal skills someday..."
        $ the_person.change_slut(2)
        "[title] judges [the_sex_person.fname]'s performance while you [the_position.verb] her."

    else:
        $ the_person.draw_person(emotion = "happy")
        $ pronoun = person_body_shame_string(the_sex_person.body_type, "slut")
        the_person "You can do better [the_person.mc_title], give that little [pronoun] what she needs."
        "[title] watches you eagerly while you are [the_position.verbing] [the_sex_person.fname]."

    return

label alpha_being_watched(the_person, the_watcher, the_position):
    if the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #They agree you should give it to her harder
        the_person "Come on [the_person.mc_title], do me a little harder."
        $ the_person.change_arousal(1)
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's super slutty and doesn't care what people think.
        the_person "Don't listen to [the_watcher.fname]. I'm just taking care of you, [the_person.mc_title]!"

    elif the_person.sluttiness >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #She's super slutty and encourages the watcher to be slutty.
        $ the_person.change_arousal(1)
        the_person "[the_person.mc_title], I think [the_watcher.fname] sees that, you can satisfy me."
        "[the_person.possessive_title] seems turned on by [the_watcher.fname] watching you and her [the_position.verb]."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
        #She's into it and encouraged by the slut watching her.
        the_person "Oh [the_person.mc_title], I know it's wrong, but what you are doing just feels right."
        $ the_person.change_arousal(1)
        "The longer [the_watcher.fname] keeps watching, the more turned on [the_person.possessive_title] gets."

    elif the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
        #She's into it but shamed by the prude watching her.
        the_person "[the_person.mc_title], don't do that, not here. I have a reputation to keep."
        $ the_person.change_arousal(-1)
        $ the_person.change_slut(-1)
        "[the_person.possessive_title] is very uneasy with [the_watcher.fname] watching."

    else: #the_person.sluttiness < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
        #They're both into it but not fanatical about it.
        the_person "[the_watcher.fname], just have a good look, I may let you try him one day."
        $ the_person.change_arousal(1)
        $ the_person.change_slut(1)
        "[the_watcher.fname] seems more comfortable, watching you [the_position.verbing] [the_person.possessive_title]."

    return

label alpha_work_enter_greeting(the_person):
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
            "[the_person.possessive_title] gives you a warm smile."
            the_person "Hello [the_person.mc_title], good to see you here!"
    else:
        if the_person.obedience < 90:
            "[the_person.possessive_title] glances up from her work."
            the_person "Hey, how's it going, sexy?"
        else:
            "[the_person.possessive_title] looks at you when you enter the room."
            the_person "Hello [the_person.mc_title], let me know if you need any help."
    return

label alpha_date_seduction(the_person):
    $ mc.change_locked_clarity(30)
    if the_person.relationship == "Single":
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "You've been good enough tonight! Come with me, I think you can make me feel even better..."
            else:
                the_person "You were a perfect gentleman tonight [the_person.mc_title], you may escort me to my place."
        else:
            if the_person.love > 40:
                the_person "I had such a wonderful time tonight, you may take me home."
            else:
                the_person "You've been the wonderful date I deserve. Would you like to share a bottle of wine at my place?"
    else:
        $ so_title = SO_relationship_to_title(the_person.relationship)
        if the_person.sluttiness > the_person.love:
            if the_person.sluttiness > 40:
                the_person "You've been such a gentleman tonight. My [so_title] is having his poker night, so..."
                the_person "Join me at my place, I think you can do something else for me..."
            else:
                the_person "You were a perfect gentleman tonight [the_person.mc_title]. It's been years since I had this much fun with my [so_title]."
                the_person "He has his poker night with some friends. Would you like to join me at my place and have glass of wine?"
        else:
            if the_person.love > 40:
                the_person "I don't want this night to end. My [so_title] is on a business trip, so we will be alone..."
                the_person "Why don't you come over to my place so we can spend more time together."
            else:
                the_person "Tonight was fantastic. I think my [so_title] is out for the night."
                the_person "So come with me to my place and you can open a bottle of wine for us."
    return

label alpha_sex_end_early(the_person):
    if the_person.sluttiness > 50:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "Is that it? You think you can drive me crazy [the_person.mc_title], well I'm really horny..."
            else:
                the_person "All done? I was expecting a little more from you."
        else:
            if the_person.arousal_perc > 60:
                the_person "Already done? You can't stop now, I'm so excited at the moment..."
            else:
                the_person "Leaving already? Well, that's very disappointing."

    else:
        if the_person.love > 40:
            if the_person.arousal_perc > 60:
                the_person "That's it? Well, you could at least pleasure me too."
            else:
                the_person "All done? Fine, we will pick this up another time."
        else:
            if the_person.arousal_perc > 60:
                the_person "Already tired [the_person.mc_title]? Did I exhaust you? We definitely need to do something about that."
            else:
                the_person "That's all you wanted? This is far from over, but for now you can go."
    return

label alpha_sex_take_control(the_person):
    if the_person.arousal_perc > 60:
        the_person "I just can't let you go [the_person.mc_title], you're going to finish what you started!"
    else:
        the_person "Do you think you're going somewhere? You are not yet done with me [the_person.mc_title]."
    return

label alpha_sex_beg_finish(the_person):
    the_person "Wait, you can't stop now! C'mon [the_person.mc_title], I'm almost there, do your job!"
    return


## Taboo break dialogue ##
label alpha_kissing_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Oh, well hello there! Do you want to pleasure me?"
    elif the_person.love >= 20:
        the_person "So you feel it too?"
        "She sighs contentedly."
        the_person "Come here, I need you to give me a kiss..."
    else:
        the_person "I don't think we should be doing this [the_person.mc_title]."
        mc.name "Let's just see how it feels and decide then."
        "[the_person.title] eyes you warily, but you watch her resolve break down."
        the_person "Alright, one kiss, for starters."
    return

label alpha_touching_body_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 30:
        the_person "Do you want to know something?"
        mc.name "What?"
        the_person "I've had dreams just like this before, you giving my body the pleasure it deserves."
        mc.name "Well, I'm happy to oblige."

    elif the_person.love >= 20:
        the_person "I want you to know I take this very seriously, [the_person.mc_title]."
        mc.name "Of course. So do I [the_person.title]."
        the_person "I normally wouldn't even think about letting you touch me."
        mc.name "What do you mean?"
        the_person "I've always been the leader, the number one... but I get this feeling when you're around..."
        the_person "Somehow it's harder to deny you."
    else:
        the_person "You shouldn't be doing this [the_person.mc_title]. We barely know each other."
        mc.name "You don't want me to stop though, do you?"
        the_person "For now, hmm, you may continue."
        mc.name "Then let me show you."
    return

label alpha_touching_penis_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Look at how big your penis is. Darn, did I just find the right one for me?"
        the_person "Relax [the_person.mc_title], and let me enjoy it, okay?"
    elif the_person.love >= 20:
        the_person "Oh dear, if I'm honest I wasn't expecting it to be quite so substantial."
        mc.name "Don't worry, it doesn't bite. Go ahead and touch it, I want to feel your hand on me."
        "She bites her lip playfully."
    else:
        the_person "We will stop here, I don't want you to get the wrong idea about me."
        mc.name "Look at me [the_person.title], I'm rock hard. Nobody would ever know if you gave it a little feel."
        "You see her resolve falter."
        the_person "It is very large, I just need to feel it for a moment."
        mc.name "Just a moment. No longer than you want to."
        "She bites her lip as her resolve breaks completely."
    return

label alpha_touching_vagina_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 35:
        the_person "Do it [the_person.mc_title]. Touch my pussy."
    elif the_person.love >= 20:
        the_person "I'm as excited as a little girl. Does a woman like me make you feel that way too, [the_person.mc_title]?"
        mc.name "Just take a deep breath and relax. You trust me, right?"
        the_person "We will see if I can trust you."
    else:
        the_person "We shouldn't be doing this [the_person.mc_title]."
        mc.name "Just take a deep breath and relax. I'm just going to touch you a little, and if you don't like it I'll stop."
        the_person "Be very meticulous with your motions or this will end very fast."
        mc.name "I will, trust me, it's going to feel amazing."
    return

label alpha_sucking_cock_taboo_break(the_person):
    mc.name "I want you to do something for me."
    the_person "What would you like?"
    mc.name "I'd like you to suck on my cock."
    if the_person.effective_sluttiness() >= 45:
        the_person "I should say no."
        mc.name "But you aren't going to."
        "She shakes her head."
        the_person "I've told all my male partners that I don't do that, but with you, I can see me doing it."
    elif the_person.love >= 30:
        the_person "Oh [the_person.mc_title]! Really? I know most men are into that sort of thing, but I..."
        the_person "Well, I'm a little more sophisticated than that."
        mc.name "What's not classy about giving pleasure to your partner? Come on [the_person.title], aren't you a little curious?"
        the_person "I'm curious... and I've decided that I'll just give it a taste and see how it feels."
        mc.name "Alright, we can start slow and go from there."
    else:
        the_person "Did you just say something I don't want to hear?"
        mc.name "No you didn't. I want you to put my cock in your mouth and suck on it."
        the_person "I will not do something like that [the_person.mc_title], who do you think I am?"
        the_person "I'm not some kind of cheap floozy that you pick up on a street corner, I don't \"suck cocks\"."
        mc.name "Yeah you do, and you're going to do it for me."
        the_person "And why should I do that?"
        mc.name "Because deep down, you want to. You can be honest with me and with yourself, aren't you curious what it's going to be like?"
        "She looks away, but you both know the answer."
        mc.name "Just come here and put it in your mouth, and if you don't like how it feels you can stop."
        the_person "You shouldn't be able to do this to me, [the_person.mc_title], I'm better than this..."
    return

label alpha_licking_pussy_taboo_break(the_person):
    mc.name "I want to taste your pussy [the_person.title]. Are you ready?"
    if the_person.effective_sluttiness() >= 45:
        the_person "Oh what a gentleman I have! Why don't you get down to business, [the_person.mc_title]!"
    elif the_person.love >= 30:
        the_person "You're such a gentleman [the_person.mc_title], but I don't want to, thank you."
        mc.name "I don't think you understand. I {i}want{/i} to eat you out, I'm just waiting for you to say it."
        "[the_person.title] won't admit it..."
        the_person "Alright then, I've changed my mind, you can go to work now."
    else:
        the_person "You're a gentleman [the_person.mc_title], but I don't feel like it."
        if not the_person.has_taboo("sucking_cock"):
            the_person "It's flattering that you'd want to return the favor though, so thank you."

        mc.name "No, I don't think you understand what I'm saying. I {i}want{/i} to eat you out, I'm just waiting for you to say it."
        "[the_person.title] won't admit it..."
        the_person "Alright then, I've changed my mind, I usually just tell them they have to satisfy me."
        mc.name "Well you have now, just relax and enjoy yourself."
    return

label alpha_vaginal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 60:
        the_person "[the_person.mc_title], I'm not ashamed to say I'm very excited right now!"
        "She giggles gleefully."
        the_person "Come on and show me what you can do to a goddess with that monster!"
    elif the_person.love >= 45:
        the_person "Go ahead [the_person.mc_title]. I think we're both ready for this."
    else:
        if the_person.has_taboo("anal_sex"):
            the_person "Oh my god, what am I doing here with you [the_person.mc_title]?"
            the_person "I'm not the type of person to do this... Am I? Is this who I've always been, and I've just been lying to myself?"
            mc.name "Don't overthink it. Just listen to your body and you'll know what you want to do."
            "She closes her eyes and takes a deep breath."
            the_person "Alright, get over here and show me what you can do."
        else:
            the_person "I'm glad you're doing this properly this time."
            the_person "It might be the hot new thing to do, but I just don't enjoy anal. I think your cock will feel much better in my vagina."
    return

label alpha_anal_sex_taboo_break(the_person):
    if the_person.effective_sluttiness() >= 75:
        "She takes a few deep breaths."
        the_person "I'm ready if you are [the_person.mc_title]. Come and fuck my ass."

    elif the_person.love >= 60:
        the_person "This is really something I want you to do [the_person.mc_title]."
        mc.name "Yeah, I would love to."
        the_person "Okay then. It wouldn't be my first pick, but we can give it a try."
        the_person "I don't know if you'll even fit though. Your penis is quite large."
        mc.name "You'll stretch out more than you think."
    else:
        if the_person.has_taboo("vaginal_sex"):
            the_person "Oh lord, what happened to me?"
            the_person "I am a respectable lady, now I'm about to get fucked in the ass..."
            the_person "We've never even had sex before and now I'm letting you penetrate my ass!"
        else:
            the_person "I don't want to do this [the_person.mc_title]... I'm not even sure if you can fit inside me there."
            mc.name "You're the sexiest, I just can't resist to try your ass!"
            the_person "Oh lord, what happened to me..."
            the_person "I am a respectable lady, now I'm about to get fucked in the ass..."
        mc.name "Relax, you'll be fine and this isn't the end of the world. Who knows, you might even enjoy yourself."
        the_person "I doubt it. Come on then, there's no point stalling any longer."
    return

label alpha_condomless_sex_taboo_break(the_person):
    if the_person.get_opinion_score("bareback sex") > 0:
        the_person "You want to have sex without any protection? I'll admit, that would really turn me on."
        if the_person.on_birth_control:
            the_person "It would be very naughty if you came inside me though..."
            mc.name "Don't you think we're being naughty already?"
            "She bites her lip and nods."
            the_person "I think we are."
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You will pull out, I hate having it dripping out of me all day."
        else:
            the_person "You will pull out, I don't want to get pregnant."

    elif the_person.love > 60:
        the_person "If you think you're ready for this commitment, I am too. I want to feel close to you."
        if the_person.get_opinion_score("creampies") > 0:
            if the_person.on_birth_control:
                the_person "When you're going to finish, I want you to fill me up with your hot load."
            else:
                the_person "Although I would like to feel your cum filling me up, you can't cum inside me, understood!"
        elif the_person.get_opinion_score("creampies") < 0:
            if the_person.kids == 0:
                the_person "You will pull out, do you understand? I really don't plan to become a mother."
            else:
                the_person "You will pull out, do you understand? I've been pregnant before and it isn't nice."
        else:
            if the_person.kids == 0:
                the_person "You will pull out. I really don't plan to become a mother."
            else:
                the_person "You will pull out, understood! You are definitely not ready for little babies."

    else:
        the_person "You want to have sex without protection? That's very risky [the_person.mc_title]."
        if the_person.has_taboo("vaginal_sex"):
            mc.name "I want our first time to be special though, don't you?"
            "She takes a second to think, then nods."
            if the_person.on_birth_control:
                the_person "You really want to do it raw? Well, I'm on birth control, so let's make this special."
            else:
                the_person "I want you to be very careful where you finish, do you understand?"
        else:
            mc.name "It will feel so much better raw, for both of us."
            the_person "You might be right about that."
            "She takes a moment to think, then nods."
            if the_person.on_birth_control:
                the_person "Fine, you don't need a condom. I'm on birth control, so let's go wild."
            else:
                the_person "Fine, you don't need a condom, but be very careful where you finish, do you understand?"
    return

label alpha_underwear_nudity_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > 30 - (the_person.get_opinion_score("skimpy outfits") * 5):
        the_person "This is the first time you've gotten to see my underwear. I hope you like what you see."
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I will. You have good taste."
            the_person "Well then, what are you waiting for?"
        else:
            mc.name "I've already seen you out of your underwear, but I'm sure it complements your form."
            the_person "Time to find out. What are you waiting for?"

    elif the_person.love > 15:
        the_person "This is going to be the first time you've seen me in my underwear. You'll be amazed!"
        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "I'm sure I'll be: you look stunning in it."
            the_person "Well then, take off my [the_clothing.display_name] for me."

        else:
            mc.name "I already know you have a beautiful body, some nice underwear can only enhance the experience."
            the_person "You really know how to please me! Help me take off my [the_clothing.display_name]."

    else:
        the_person "If I take off my [the_clothing.display_name] you'll see me in my underwear."
        mc.name "That's the plan, yes."
        the_person "I shouldn't be going around half-naked for men I barely know. What would people think?"

        if the_person.has_taboo(["bare_tits","bare_pussy"]):
            mc.name "Why do you care what other people think? Forget about them and just focus on the moment."
            the_person "I have to keep some kind of decorum, but I am intrigued..."
        else:
            mc.name "You might have wanted to worry about that before I saw you naked. You have nothing left to hide."
            the_person "Yes, you are right, let's go."
    return

label alpha_bare_tits_taboo_break(the_person, the_clothing):
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
        the_person "[the_person.mc_title]! If you take off my [the_clothing.display_name] I won't be decent any more!"
        mc.name "I want to see your breasts and it's blocking my view."
        the_person "I'm aware it's \"blocking your view\", that's why I put it on this morning."
        if the_person.has_large_tits and the_clothing.underwear:
            the_person "Besides, a woman like me needs a little support. These aren't exactly light."
        mc.name "Come on [the_person.title]. You're gorgeous, I'm just dying to see more of you."
        the_person "Well I'm glad I have that effect on you. And you always know the right thing to say to me."
        "She takes a moment to think, then nods."
        the_person "You can take off my [the_clothing.display_name] and have a look."
    return

label alpha_bare_pussy_taboo_break(the_person, the_clothing):
    if the_person.effective_sluttiness() > (50 - the_person.get_opinion_score("showing her ass") * 5):
        the_person "You want to get me out of my [the_clothing.display_name]? Well, I'm glad you've finally asked."

    elif the_person.love > 35:
        the_person "Oh, slowly there [the_person.mc_title]. If you take off my [the_clothing.display_name] I'll be nude in front of you..."
        if the_person.has_taboo("touching_vagina"):
            mc.name "That's exactly what I want, to get a look at your magnificent body."
            the_person "Oh, continue... That's the best way to talk to a lady like me."
        else:
            mc.name "That's exactly what I want, to get a look at your magnificent body."
            the_person "Oh stop, you, I suppose you can take it off and have a look."

    else:
        the_person "Oh! Be careful, or you're going to have me showing you everything!"
        mc.name "That is what I was hoping for, yeah."
        the_person "Well! I'm not that kind of woman [the_person.mc_title]!"
        if the_person.has_taboo("touching_vagina"):
            mc.name "Don't you want to be though? Don't you want me to enjoy your body?"
            the_person "I might, but I shouldn't, it's not appropriate."
        else:
            mc.name "Of course you are! I've touched you before, I just want to feel what I was feeling before."
            the_person "This wasn't what I intended."

        "You can tell her protests are just to maintain her image, and she already knows what she wants."
        mc.name "Just relax and let it happen, you'll have a good time."
    return

# label alpha_facial_cum_taboo_break(the_person):
#     return

# label alpha_mouth_cum_taboo_break(the_person):
#     return

# label alpha_body_cum_taboo_break(the_person):
#     return

# label alpha_creampie_taboo_break(the_person):
#     return

# label alpha_anal_creampie_taboo_break(the_person):
#     return
