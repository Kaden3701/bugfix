### PERSONALITY CHARACTERISTICS ###
init 700:
    python:
        def stephanie_titles(person):
            valid_titles = [person.name]
            if person.love > 10:
                valid_titles.append("Steph")
            return valid_titles

        def stephanie_possessive_titles(person):
            valid_titles = [person.name]
            if person.love > 10:
                valid_titles.append("Study Buddy")
            return valid_titles

        def stephanie_player_titles(person):
            valid_titles = [mc.name]
            if person.love > 20:
                valid_titles.append("Teacher's pet")
            return valid_titles


        stephanie_personality = Personality("stephanie", default_prefix = "wild",
        common_likes = ["pants", "Fridays", "makeup", "the colour red", "high heels"],
        common_sexy_likes = ["giving blowjobs", "drinking cum", "cheating on men", "doggy style sex", "public sex"],
        common_dislikes = ["Mondays", "conservative outfits"],
        common_sexy_dislikes = ["anal sex", "being submissive", "missionary style sex"],
        titles_function = stephanie_titles, possessive_titles_function = stephanie_possessive_titles, player_titles_function = stephanie_player_titles,
        insta_chance = 40, dikdok_chance = 20)

### DIALOGUE ###
label stephanie_greetings(the_person):
    if the_person.love < 0:
        the_person "Ugh... What do you need? Can we make this quick?"
    elif the_person.happiness < 90:
        the_person "Hey, hope you're having a better day than me. What's up?"
    else:
        if the_person.obedience > 180:
            if the_person.sluttiness > 60:
                the_person "Good to see you [the_person.mc_title], I hope you're here to see me about something fun."
            else:
                the_person "Good to see you [the_person.mc_title], how can I help?"
        else:
            if the_person.sluttiness > 60:
                the_person "Hey [the_person.mc_title], are you here for business or pleasure?"
                "[the_person.title] smiles playfully."
            else:
                the_person "Hey [the_person.mc_title], what's up?"
    return

label stephanie_cum_face(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish:
            the_person "Mmm, that feels nice."
        elif the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("cum facials") > 0 or the_person.get_opinion_score("drinking cum") > 1:
            the_person "Mmm, that feels nice. I bet it would feel even nicer in my mouth next time, [the_person.mc_title]."
        elif the_person.get_opinion_score("drinking cum") > 0:
            the_person "There we go, all taken care of. You can cum in my mouth next time if you want, it would make cleaning up a lot faster."
        else:
            the_person "There we go, all taken care of."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 1:
            if the_person.sex_record.get("Cum in Mouth", 0) > 0:
                the_person "Aww, you should shoot it into my mouth next time. I love how your hot cum tastes."
            else:
                the_person "Aww, you should shoot it into my mouth next time. I love the taste of hot cum."
            "[the_person.title] runs a finger through a puddle of your cum and then licks it clean, smiling at you while she does it."
        elif the_person.get_opinion_score("drinking cum") > 0:
            the_person "Oh man, you really got me covered, didn't you? I wish you would just cum in my mouth so I don't have to worry about getting cleaned up."
        else:
            the_person "Oh man, you really got me covered, didn't you?"
    return

label stephanie_cum_mouth(the_person):
    if the_person.has_cum_fetish or the_person.obedience > 180:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Oh god, you taste so good. Thank you for the treat [the_person.mc_title]."
        else:
            the_person "Mmm, thank you [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Mmm, your cum tastes so great [the_person.mc_title], are you sure there isn't any more of it for me?"
            "[the_person.title] licks her lips and sighs happily."
        elif the_person.get_opinion_score("drinking cum") > -1:
            "[the_person.title] licks her lips and smiles at you."
            the_person "Mmm, that was nice."
        else:
            "[the_person.title] licks her lips."
    return

# label stephanie_cum_vagina(the_person):
#     #TODO
#     return
#
# label stephanie_cum_anal(the_person):
#     #TODO
#     return

label stephanie_improved_serum_unlock(the_person):
    mc.name "[the_person.title], now that you've had some time to get use to the lab there is something I want to talk to you about."
    the_person "Sure, what can I help you with?"
    mc.name "Our R&D up to this point has been based on the notes you and I have from our days at the lab."
    mc.name "Remember how some of the effects we saw were enhanced by sexual arousal?"
    "[the_person.title] nods her understanding."
    the_person "Our data did indicate that, yes. [nora.fname]'s hypothesis was that an orgasm opened up chemical receptors that were normally unavailable."
    mc.name "What else can we do if we assume that is true? Does that open up any more research paths?"
    the_person "If it's true it might give us a way to induce greater effects in the recipients."
    "[the_person.possessive_title] thinks for a long moment, then smiles mischievously."
    the_person "But we'll need to do some experiments to be sure."
    mc.name "What sort of experiments?"
    the_person "I want to take a dose of serum myself, and you can record the effects."
    the_person "Then I'll make myself cu... induce a climax, and we can compare the effects after."
    mc.name "Do you think that's a good idea?"
    the_person "Self experimentation with prototype drugs? I don't see how it could go wrong!"
    the_person "Come on [the_person.mc_title], this is the stuff [nora.fname] would never let me do! It's a chance to be at the bleeding edge of science!"
    mc.name "Alright, what do we need?"
    the_person "A finished dose of serum that raises my Suggestibility. The higher it gets my Suggestibility the better, but any amount should do."
    the_person "Then we'll just need some time and some privacy for me to see what sort of effects my orgasms will have."
    return

label stephanie_sex_strip(the_person):
    if the_person.sluttiness < 20:
        if the_person.arousal_perc < 50:
            the_person "Ugh I've started to dress like [nora.title]. Let me take some of this off."
        else:
            the_person "Is it getting warm in here? I need to take something off."

    elif the_person.sluttiness < 60:
        if the_person.arousal_perc < 50:
            the_person "You saw more of me back at the lab, I think I can lose a little more clothing, don't you?"
        else:
            the_person "One second, let me take some of this off for you. Feel free to watch."

    else:
        if the_person.arousal_perc < 50:
            the_person "Ugh, fuck this stupid outfit. I hope you don't mind if I take it off."
        else:
            the_person "Wait, I need to take this off, I want to feel you against me."

    return

label stephanie_sex_toy_taboo_break(the_person):
    return

label stephanie_roleplay_taboo_break(the_person):
    return

label stephanie_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    the_person "Ohhh, a night with you all to myself? That sounds amazing..."
    "She runs her hand down your chest."
    return

label stephanie_sleepover_herplace_response(the_person): #Spending the night at her place
    if ashley_get_intro_complete(): #We have been introduced to Ashley
        the_person "Sounds good. I'll let Ash know you are coming over so she isn't surprised..."
    else:
        the_person "Wine sounds nice. I'll make sure I have something nice to wear."
        "[the_person.title] gives you a wink."
    return


label stephanie_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    the_person "I was hoping you would like it..."
    "[the_person.possessive_title] slowly walks over to you, her hips swaying enticingly."
    the_person "How do you want me? I'm yours for the night!"
    return


label stephanie_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm, that hits the spot. Nothing like a nice drink to get the night started."
    "[the_person.title] takes a few long sips, draining most of her glass before setting it on the nightstand."
    the_person "I'm ready to get this started. How do you want me?"
    return

label stephanie_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh my god, I've lost count of how many times you've made me cum tonight..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I think I can keep going... but you might need to be gentle!"
    return


label stephanie_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, you always make me feel so good..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I'm ready to go again if you are!"
    return

label stephanie_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Glad we got that out of your system. Take a minute, then get ready to fuck me for real!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."
    return
