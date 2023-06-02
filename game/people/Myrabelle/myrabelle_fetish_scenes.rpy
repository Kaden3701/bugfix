#Requirement Functions
init 1 python:
    def cum_fetish_myra_intro_requirement():
        pass
        return False

    def exhibition_fetish_myra_intro_requirement():
        pass
        return False

    def breeding_fetish_myra_intro_requirement():
        if time_of_day == 4:
            if mc.energy >80 and myra.energy > 80:
                return True
        return False

    def anal_fetish_myra_intro_requirement():
        pass
        return False


#Actions
init 2 python:
    cum_fetish_myra_intro = Fetish_Action("Myra Cum Fetish Intro", cum_fetish_myra_intro_requirement, "cum_fetish_myra_intro_label", fetish_type = "cum")
    exhibition_fetish_myra_intro = Fetish_Action("Myra Exhibitionism Fetish Intro", exhibition_fetish_myra_intro_requirement, "exhibition_fetish_myra_intro_label", fetish_type = "exhibition")
    breeding_fetish_myra_intro = Fetish_Action("Myra Breeding Fetish Intro", breeding_fetish_myra_intro_requirement, "breeding_fetish_myra_intro_label", fetish_type = "breeding")
    anal_fetish_myra_intro = Fetish_Action("Myra Anal Fetish Intro", anal_fetish_myra_intro_requirement, "anal_fetish_myra_intro_label", fetish_type = "anal")

label cum_fetish_myra_intro_label():
    $ the_person = myra

    $ add_cum_fetish(the_person)
    return

label exhibition_fetish_myra_intro_label():
    $ the_person = myra
    return


label breeding_fetish_myra_intro_label():
    $ the_person = myra
    $ the_person.arousal = 40
    "You feel your phone go off when you get a notification. It's a message from [the_person.possessive_title]"
    $ mc.start_text_convo(the_person)
    the_person "Hey, can you PLEASE come to the cafe tonight? It'll be worth it... I promise!"
    mc.name "Oh? What do you need?"
    the_person "It involves The Sims. It'll be worth it, just cum!"
    "You can't help but notice her spelling."
    mc.name "Alright, I'm on my way."
    $ mc.end_text_convo()
    $ mc.change_location(gaming_cafe)
    $ the_person.apply_outfit(special_fetish_nude_outfit)
    "When you get to the gaming cafe, you find it unlocked. You let yourself in, then lock the door."
    if myra_lewd_cafe_open():
        "You head to the back and into the adult's only section."
    else:
        "You head to the back where you've played a lewd version of The Sims with [the_person.title]"
    $ the_person.draw_person()
    the_person "Hey! You came!"
    mc.name "Of course. And I can see I am a bit overdressed. Are we playing The Sims tonight?"
    "You start to undress."
    the_person "Yeah! I don't know why, but I'm feeling pretty lucky about the way the game finishes tonight..."
    "[the_person.possessive_title] is definitely acting a bit odd. She is pretty forward about things, so you shouldn't be surprised she called you here this late."
    "However, you can't help shake the feeling that she has rigged this somehow."
    "You've been dosing her with reproduction proclivity serums recently. Maybe she is developing a breeding fetish?"
    "You step out of the last of your clothes and look up. [the_person.possessive_title] is looking at your hungrily."
    the_person "Fuck you look so... virile... let's get this going!"
    call myra_sex_roullette_session_label(the_person, breeding_fetish_intro = True) from _myra_breeding_fetish_intro_session_01
    "When you finish, she just stands there, running her hands over her belly."
    "She obviously intended for you to cum inside her from the moment she texted you."
    if the_person.knows_pregnant:
        the_person "No wonder I'm pregnant... there is nothing as amazing as taking a hot load of cum."
    else:
        the_person "Oh god, that was fucking amazing. Do you think... maybe it really knocked me up?"
    "It seems obvious now. After giving her multiple serums, [the_person.possessive_title] has developed a breeding fetish."
    "Even now you see her looking at your cock, trying to decide if she can milk another load from it."
    mc.name "You love it, don't you? You want to be by personal cum dumpster, to take my loads anytime and anywhere I want you to?"
    the_person "Oh god yes..."
    mc.name "You're going to love it, aren't you? When you show up for a tournament, your belly round, your big tits leaking milk. Everyone there is gonna know what a needy cunt you have."
    the_person "Yes!"
    mc.name "Everyone there is going to know you are a hopeless, thirsty slut. You long for your master's cum sloshing around in your fertile womb all day long."
    "[the_person.possessive_title]'s knees start to buckle for a second."
    the_person "Yes please! Breed me again PLEASE?"
    mc.name "I plan to. Keep your cunt ready for me, anytime I want to dump my load inside you."
    the_person "Yes! Don't worry, I'll be ready!"
    "You say goodbye to [the_person.title]."
    "[the_person.possessive_title] now has a fetish to get bred by you!"
    "If you re-enact a scene from The Sims in the future, she may also decide to force you to cum inside her too..."
    $ add_breeding_fetish(the_person)
    $ mc.change_location(bedroom)
    "You walk home and collapse into your bed. You can't wait to fill [the_person.possessive_title]'s needy cunt with your cum, over and over again."
    return


label anal_fetish_myra_intro_label():
    $ the_person = myra

    $ add_anal_fetish(the_person)
    return
