# Harem Role - girl is accepted into the harem and accepts that she is not the only love interest
# - requires Threesome and love higher than 80
# Things to Consider:
# - can make a harem, lovable, or slavable? currently its lovable as per default and most easiest to implement
# - knows of the others in your harem
# - can have girlfriend and affair roles - when suggested, they may become sole harem, or need to be slowly integrated
# - girlfriend roles - suggestion to complete, may take time to accept.
# - if affair role - similar to gf role, if they leave SO = harem, continues affair as harem but for the children
# - Harem_Mansion - eventually a place where they all can live together?
# - Dialogs can be done way better than the way I did them XD
init 1 python:
    def ask_harem_requirement(the_person):
        if the_person.has_exact_role(harem_role): # already in harem
            return False
        if the_person.love < 60:    # hide option until love >= 60
            return False
        if the_person.love < 80:
            return "Requires: 80 Love"

        if the_person.has_role(affair_role):
            return True
        #kept special girlfriend roles for future
        if the_person.has_role(sister_role) and the_person.event_triggers_dict.get("sister_girlfriend_waiting_for_blessing", False):
            return "Requires: Mom's approval"
        elif the_person.has_role(mother_role) and the_person.event_triggers_dict.get("mom_girlfriend_waiting_for_blessing", False):
            return "Requires: Sister's approval"
        if not the_person.has_role(girlfriend_role):
            return "Requires: be your girlfriend"
        return True

    def harem_break_up_requirement(the_person):
        if the_person.home == harem_mansion:
            return False
        #Set to only show up if happiness is below 100 or love is below 80, to keep it from popping up all the time
        return the_person.happiness <= 100 or the_person.love <= 80

    def harem_ask_get_boobjob_requirement(the_person):
        if the_person.has_role(affair_role):
            return False
        return ask_get_boobjob_requirement(the_person)

    def harem_ask_trim_pubes_requirement(the_person):
        if the_person.has_role(affair_role):
            return False
        return girlfriend_ask_trim_pubes_requirement(the_person)

    def harem_fuck_date_requirement(the_person):
        if the_person.home == harem_mansion:    # already in mansion
            return False
        if the_person.has_role(affair_role):
            return False
        return fuck_date_requirement(the_person)

    def harem_move_to_mansion_requirement(the_person):
        if the_person.home == harem_mansion:    # already in mansion
            return False
        if not mc.business.event_triggers_dict.get("harem_mansion_build", False): # mansion not build
            return False
        if the_person.has_role(affair_role): # she needs to leave her SO
            return "Requires: Single"
        return True

    make_harem_action = Action("Ask her to join your harem", requirement = ask_harem_requirement, effect = "ask_to_join_harem_label",
        menu_tooltip = "Ask her to start an official, polyamorous relationship and be part of your Harem.", priority = 10)
    chat_actions.append(make_harem_action)

    #Setting Harem Roles = Polyamory, Polyamorous relationship for more ideas refer to
    #https://affirmativecouch.com/polyamorous-relationship-structures/
    # Hierarchial Polyamory would be what everyone is familiar with as a Harem
    # mc viewed as the Primary, then rest would fall under the following
    # Dependant Polyamory - chooses to live with mc
    # Solo Polyamory - chooses to live seperately
    # Polycules formed by individuals... so they might want only one on one with mc, but eventually threesome with another
    # - so you can make a relationship dependant on polycules = ie Emily will do threesome with mc and Sarah, but doesn't like others that way
    # - could use the relationship structure to define polycules between persons in the harem?
    # harem_role/cousin/aunt when they are girlfriend and added to the poly they get the generic girlfriend role, this is just to keep things tied up

label leave_harem_label(the_person):
    # Stop being in a relationship.
    mc.name "[the_person.title], can we talk?"
    if the_person.happiness > 100:
        the_person "Sure, what's up?"
    else:
        the_person "Oh no, that's never good."

    mc.name "There's no easy way to say this, so I'll just say it: It's not working out."
    $ the_person.draw_person(emotion = "sad")
    #TODO: Add a variant where you've passed below the girlfriend threshold and she feels the same way.
    $ the_person.change_happiness(-(the_person.love - 40)) #TODO: Double check this vs. the girlfriend love threshold.
    "She seems to be in shock for a long moment, before slowly nodding her head."
    the_person "Okay... I don't know what to say."
    $ the_person.change_love(-10)
    mc.name "I'm sorry, but it's just the way things are."

    python:
        # she is not happy and will reset her obedience to 100
        the_person.change_stats(love = -20, happiness = -20, obedience = 100 - the_person.obedience)
        # she loses her submissive trait
        the_person.update_opinion_with_score("being submissive", 0)
        the_person.remove_role(harem_role)
        the_person.remove_role(affair_role) # also ends affair if still present
        the_person.remove_role(girlfriend_role)
        the_person.set_schedule(downtown_hotel, the_times=[0, 4]) # she moves to a hotel
    return

label ask_to_join_harem_label(the_person):
    #Requires high love, if successful she becomes your girlfriend (which unlocks many other options). Requires high love and her not being in a relationship.
    #Hide this event at low love, show it when it at it's lowest love possibility and let it fail out for specific reasons (thus informing the player WHY it failed out).
    #requires you have to make her a girlfriend/paramour before you can suggest harem
    #General dialogue used for everyone.
    mc.name "[the_person.title], can I talk to you about something important?"
    the_person "Of course. What's on your mind."
    mc.name "I've been thinking about this for a while. I really hope you feel as strongly as I do about us."
    mc.name "I want you to be part of something bigger, we both have a lot of love to share."
    mc.name "I want us to be part of a strong and healthy polyamorous relationship, do you accept?"
    "[the_person.possessive_title] takes a moment before responding."
    #you are already in a relationship with them, but want to make them accept the harem
    $ convinced = False
    if the_person.relationship=="Single" and not the_person.has_role(girlfriend_role):
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "Of course! [the_person.mc_title], the more the merrier!"
            the_person "I look forward to seeing our family grow!"
            $ convinced  = True
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself...."

    elif the_person.has_exact_role(girlfriend_role):
        the_person "Well, we are together already...."
        the_person "And I really like having you all to myself..."
        the_person "Including more into the mix?"
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            the_person "I look forward to seeing our growing family!"
            $ convinced  = True
        else:
            the_person "I'm not ready yet [the_person.mc_title], I really like having you all to myself..."

    elif the_person.has_role(affair_role): #we keep the paramour til she is ready to leave the husband or told to by mc
        the_person "Well technically I'm already in a polyamorous relationship, but I am the link."
        the_person "So it does make sense you want something more than what I can offer you..."
        $ so_title = SO_relationship_to_title(the_person.relationship)
        the_person "I mean, I already have a [so_title] and I can't just leave him like this."
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] leans forward and kisses you, putting an arm around your waist and pulling you close. When she breaks the kiss she looks deep into your eyes."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "I look forward to seeing what I can add to our growing family!"
            $ convinced  = True
        else:
            the_person "I care about you a lot, but it's just not something I could do."
            the_person "Oh [the_person.mc_title], I'm so flattered, but you know that I have a [so_title]."
            if the_person.kids > 0:
                if the_person.kids > 1:
                    the_person "I would never dream of leaving him, and it would devastate our children."
                else:
                    the_person "I would never dream of leaving him, and it would devastate our child."
            else:
                the_person "I would never dream of leaving him."

    elif the_person in [lily, cousin]:
        the_person "[the_person.mc_title], you do make me happy..."
        if the_person.get_opinion_score("threesomes") > 0:
            "She stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
        else:
            the_person "I care about you a lot, but it's just not something I could do."

    elif the_person in [mom, aunt]:
        the_person "A bigger family?"
        the_person "As long as you understand where we stand, I think we can be."
        if the_person.get_opinion_score("threesomes") > 0:
            "[the_person.possessive_title] stares deep into your eyes as you take her hands and hold them in yours."
            mc.name "Just be with me [the_person.title]. It's that simple."
            "[the_person.possessive_title] hesitates for a long moment. At long last she nods."
            the_person "Okay, you're right. We've gone this far already..."
            $ convinced  = True
        else:
            the_person "I care about you a lot, we are family, that will never change."
            the_person "Adding more, I don't know? I need to think about it.."
    else:
        the_person "[the_person.possessive_title] taps her leg thinking about the pros and cons."

    if convinced:
        # She agrees, you're now in a relationship! Congratulations!
        $ the_person.draw_person(emotion = "happy")
        $ the_person.change_stats(happiness = 15, love = 5)
        if the_person.age > 40:
            the_person "Oh I'm so happy to hear you say that! I was worried about our age difference, but I don't want that to stop us!"
        else:
            the_person "Oh my god, I'm so happy! Yes, I want to be part of your flock!"
        "She puts her arms around you and pulls you close."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        $ mc.change_locked_clarity(10)
        "She kisses you, and you kiss her back just as happily."
        $ the_person.add_role(harem_role)
    else:
        mc.name "Remember [the_person.title], we will never be alone again."
        mc.name "If you change your mind, I'll be here for you."
        "Perhaps her willingness to share you with another is not high enough (threesomes opinion)."

    return


label harem_move_to_mansion_label(the_person):
    # TODO: Write more elaborate dialog for inviting to mansion
    mc.name "[the_person.title], would you like to live with me?"
    the_person "Oh [the_person.mc_title], I've been waiting for you to ask me this."
    the_person "Ever since you asked me to explore out relationship further. Of course I want to live with you!"
    mc.name "Perfect, I've already made arrangements, I will see you at my new mansion soon."

    # if successful
    $ the_person.change_home_location(harem_mansion)
    return
