init 2 python:
    def intern_water_spill_crisis_requirement():
        return mc.is_at_work and any(x for x in mc.business.intern_list if x.is_at_work)

    intern_water_spill_crisis = ActionMod("Intern Water Spill Crisis",intern_water_spill_crisis_requirement,"intern_water_spill_crisis_label",
        menu_tooltip = "An intern spills her water", category = "Intern", is_crisis = True)

label intern_water_spill_crisis_label():
    $ the_person = get_random_from_list(mc.business.intern_list)
    if len(the_person.outfit.get_upper_ordered()) == 0:
        return #She's not wearing a top, we can't exactly spill water on nothing!

    $ the_clothing = the_person.outfit.get_upper_top_layer #Get the very top item of clothing.
    "You're hard at work when [the_person.title] comes up to you. She has a textbook in one hand, a water bottle in the other."
    $ the_person.draw_person()
    mc.name "Hey [the_person.title], how can I help you?"
    the_person "I was working on some homework during my break and I hit some snags. I heard you are pretty good with academics?"
    "You listen as [the_person.possessive_title] dives into her homework problem."
    "You aren't paying a terrible amount of attention until she goes to take a drink from her water bottle and dumps it down her front!"
    $ the_clothing.colour[3] *= .8
    $ the_person.draw_person(emotion="angry")
    $ the_person.call_dialogue("surprised_exclaim")
    "She tries to wipe the water off, but not before it's soaked through the front of her [the_clothing.display_name]."
    $ mc.change_locked_clarity(10)
    $ test_outfit = the_person.outfit.get_copy() #Make a copy, we'll try removing the wet item and reevaluating.
    $ test_outfit.remove_clothing(the_clothing)
    $ thinks_appropriate = the_person.judge_outfit(test_outfit,10) #Does she think it's appropriate to strip off her top when it's wet?
    if not thinks_appropriate:
        the_person "I'm so sorry about this [the_person.mc_title], I just... I just need to go and dry this off!"
        if the_person.has_large_tits:
            "[the_person.title] runs off towards the bathroom. You get a nice glimpse at the way her tits jiggle under her wet shirt."
        else:
            "[the_person.title] runs off towards the bathroom."
        $ clear_scene()
        $ the_clothing.colour[3] *= 1.25
        "After a few minutes she's back, with her [the_clothing.display_name] dried off and no longer transparent."
        $ the_person.draw_person()
        $ the_person.change_slut(1)
        the_person "Ugh, that was so embarrassing. Let's just forget about that, okay?"
        mc.name "Of course, back to your homework then, right?"
        "You help [the_person.possessive_title] sort out her homework issues, then get back to work."
        $ the_person.change_int(1)
    else:
        $ thinks_appropriate = the_person.judge_outfit(test_outfit) #Does she think it's appropriate to just strip it off all of the time?
        if thinks_appropriate:
            the_person "I'm so sorry about this [the_person.mc_title]. Let me just take this off, you keep talking."
            $ the_person.draw_animated_removal(the_clothing)
            $ the_person.update_outfit_taboos()
            if the_person.tits_visible:
                "[the_person.title] strips off her [the_clothing.display_name], letting you get a nice good look at her [the_person.tits] sized tits."
                $ mc.change_locked_clarity(30)
            else:
                "[the_person.title] strips off her [the_clothing.display_name] and puts it to the side, then turns her attention back to you."
                $ mc.change_locked_clarity(10)
            menu:
                "Right, your homework...":
                    the_person "I hope I'm not distracting you. I can dry my shirt off if you'd prefer."
                    mc.name "No, that's fine. Just remind me again what we were talking about."
                    $ the_person.change_slut(1)
                    "You help [the_person.possessive_title] with her homework questions while she stands topless beside your desk."
                    $ the_person.change_int(1)

                "Keep going...":
                    mc.name "You might as well keep going. All this homework talk is boring and I'd appreciate something pleasant to look at while I help you."
                    if the_person.tits_visible and the_person.vagina_visible:
                        mc.name "Not that there's much I can't see already..."
                    elif the_person.tits_visible:
                        mc.name "You already have your tits out for me, what's a little more skin?"
                    elif the_person.vagina_visible:
                        mc.name "I mean, I can already see your cunt. What's a little more skin at this point?"

                    if the_person.judge_outfit(the_person.outfit, -25): #How comfortable are they with their current outfit? If they have an extra 20 sluttiness start stripping!
                        "[the_person.title] smiles mischievously and starts to strip down some more."
                        the_person "You have been very helpful to me. It's the least I could do."

                    elif the_person.obedience > 140:
                        "[the_person.title] nods and starts to strip down some more."
                        the_person "I'll do whatever you would like me to do, sir."

                    else:
                        the_person "I mean... that doesn't seem appropriate... but I do need help with my homework..."
                        "[the_person.possessive_title] starts to strip down some more, but you can tell she isn't happy about it."
                        "You're sure she'll make a complaint to HR."
                        $ mc.business.change_team_effectiveness(-10)

                    python:
                        next_piece = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        while (next_piece and the_person.judge_outfit(the_person.outfit, the_person.obedience-100+10)):
                            the_person.draw_animated_removal(next_piece)
                            renpy.say(None,the_person.title + " takes off her " + next_piece.name + " and drops it on the floor.")
                            next_piece = the_person.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
                        next_piece = None
                    $ the_person.update_outfit_taboos()
                    the_person "There, I hope that's good enough."
                    mc.name "Much better. Now, back to your homework."
                    python:
                        the_person.change_slut(3)
                        the_person.change_obedience(5)
                        if the_person.int < 6:
                            the_person.change_int(1)
                    if the_person.tits_visible and the_person.vagina_visible:
                        "You help [the_person.possessive_title] with her homework while she stands next to your desk, her body completely on display."
                        $ mc.change_locked_clarity(50)
                    else:
                        "You help [the_person.possessive_title] with her homework while she stands next to your desk, still partially undressed."
                        $ mc.change_locked_clarity(30)


            $ the_clothing.colour[3] *= 1.25
            $ the_person.review_outfit()

        else:
            the_person "I'm so sorry about this [the_person.mc_title], should I go dry this off first?"
            menu:
                "Dry it off now":
                    mc.name "You go dry it off, I'll wait here for you."
                    the_person "I'll be back as soon as I can."
                    $ clear_scene()
                    "[the_person.title] runs off towards the bathroom."
                    $ the_clothing.colour[3] *= 1.25
                    "After a few minutes she's back, with her [the_clothing.display_name] dried off and no longer transparent."
                    $ the_person.draw_person()
                    $ the_person.change_slut(1)
                    the_person "Ugh, that was so embarrassing. Let's just forget about that, okay?"
                    mc.name "Of course, back to your homework then, right?"
                    "You help [the_person.possessive_title] with her homework, then get back to work."
                    if the_person.int < 6:
                        $ the_person.change_int(1)

                "Leave it alone":
                    mc.name "I'd like to get back to work as quickly as possible, just leave it for now and you can dry it off later."
                    if test_outfit.tits_visible:
                        "[the_person.title] looks down at her transparent top, then nods and continues on about her homework. Getting a good look at her tits makes the boring topic much more interesting."
                    else:
                        "[the_person.title] looks down at her top, then nods and continues. At least the transparent clothing helps make the boring topic more interesting."
                    $ mc.change_locked_clarity(5)
                    $ the_person.change_obedience(1)
                    $ the_person.change_slut(1)
                    "After a few minutes you've answered all of [the_person.possessive_title]'s questions, and she heads off to dry her [the_clothing.display_name]."
                    $ the_clothing.colour[3] *= 1.25
                    if the_person.int < 6:
                        $ the_person.change_int(1)

                "Take it off":
                    mc.name "I'm really quite busy right now, just take it off now and you can dry it off later."
                    the_person "I... Okay, fine. I really need your help on this."
                    $ the_person.draw_animated_removal(the_clothing)
                    $ the_person.change_stats(happiness = -5, slut = 2, obedience =2)
                    $ mc.business.change_team_effectiveness(-10)
                    "[the_person.title] clearly isn't happy, but she takes off her [the_clothing.display_name] and resumes talking about her homework."
                    $ the_person.update_outfit_taboos()
                    "You're sure she'll probably make a complaint with HR..."
                    if test_outfit.tits_visible:
                        "Getting a good look at her tits makes the boring topic much more interesting. After a few minutes you've sorted out her problems. She goes to dry her top while you get back to work."
                    else:
                        "You spend a few minutes and sort out all of her problems. When you're done she goes off to dry her top while you get back to work."
                    $ mc.change_locked_clarity(20)
                    $ the_clothing.colour[3] *= 1.25
                    $ the_person.outfit.add_upper(the_clothing)
                    if the_person.int < 6:
                        $ the_person.change_int(1)

    $ the_clothing = None
    $ del test_outfit
    $ clear_scene()
    return
