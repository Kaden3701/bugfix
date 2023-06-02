#This file contains the generic clothes shoping label as well as Candace specific version.
#Clothes shopping is unlocked after Candace takes you.
#Label starts out at a regular store, girl tries on three outfits. If players approves of less than 2, she prompts player to pick something out.
#After, based on sluttiness,  she picks out a set of new underwear. If not slutty, it's regular underwear. If moderately slutty, it's lingerie. If very slutty, pulls MC into room with her for sex scene.
#Anytime girl tries on outfit that she REALLY likes, if she works for MC, asks MC to wear to work. If yes, add outfit to her department uniform options.
#TODO, should we give option to add outfit to player's outfit selection?
init 2 python:
    def invite_to_clothes_shopping_requirement():
        if not candace_get_has_gone_clothes_shopping():
            return False
        if time_of_day == 0:
            return "Opens in the morning"
        elif time_of_day == 4: # Can be removed
            return "Closed for the night"
        elif not mc.business.has_funds(500):
            return "Requires $500"
        else:
            return True

    def build_outfit_selection(person):
        outfits = []
        for i in range(3):
            outfits.append(Wardrobe.generate_random_appropriate_outfit(person))
        outfits.append(Wardrobe.generate_random_appropriate_outfit(person, outfit_type = "under"))
        return outfits

    def clothes_shopping_get_work_wardrobe(person):
        if person in mc.business.research_team:
            return mc.business.r_uniform
        if person in mc.business.market_team:
            return mc.business.m_uniform
        if person in mc.business.supply_team:
            return mc.business.s_uniform
        if person in mc.business.production_team:
            return mc.business.p_uniform
        if person in mc.business.hr_team:
            return mc.business.h_uniform
        return None


init 3 python:
    invite_to_clothes_shopping = ActionMod("Invite someone to shop {image=gui/heart/Time_Advance.png}", invite_to_clothes_shopping_requirement, "invite_to_clothes_shopping_label",
        menu_tooltip = "Invite a person to go clothes shopping.", category="Mall")



label invite_to_clothes_shopping_label():
    "You decide to invite someone out for some clothes shopping."
    call screen main_choice_display(build_menu_items(
        [get_sorted_people_list(known_people_in_the_game(), "Clothes shopping", "Back")]
        ))

    if not isinstance(_return, Person):
        "You change your mind and decide to do something else instead."
        return

    $ the_person = _return
    # change her location to the clothing store and make sure she wears her 'personal outfit'
    $ the_person.change_location(mc.location)
    $ the_person.apply_planned_outfit()

    "You send a message to [the_person.fname] about going clothes shopping."
    "After some time you get a response..."
    if the_person.obedience > 100:
        the_person "Okay! I'll meet you there [the_person.mc_title]!"
    else:
        the_person "Oh! I suppose I could do that. You're buying though! I'll meet you there, [the_person.mc_title]."
    "You hang out for a few minutes. Soon you see [the_person.title]."
    $ the_person.draw_person()
    the_person "Hey there! Thanks for offering! Let's see what we can find."
    "She browses through the racks of clothes and eventually finds a couple things she likes."
    the_person "Okay, you wait right here, I'll be right back to show you what I picked out!"
    $ clear_scene()
    call trying_on_clothes_label(the_person) from _clothes_shopping_choice_01
    if _return > 0: # we bought some clothes
        "You walk with [the_person.title] up to the checkout line."
        the_person "God, that was fun! We should do that again sometime!"
        mc.name "Yeah I'll let you know if I have the chance."
        "At the checkout line, you pay for the new clothes for [the_person.possessive_title]."
        $ mc.business.change_funds(-100 * _return)
        the_person "You're sweet. Thanks for the shopping trip!"
    else: # we didn't find anything
        "You walk with [the_person.title] to the exit."
        the_person "God, that was fun! Just a shame we didn't find anything we both like!"
        mc.name "I'm sure we will find something next time."
        the_person "Oh that's so nice, I can't wait for our next shopping trip! See you next time."

    $ the_person.draw_person(position = "walking_away")
    "You watch [the_person.title] as she walks away..."
    call advance_time from _call_advance_time_clothes_shopping_choice_1
    return

label trying_on_clothes_label(the_person): #This label starts with trying on clothes, to finishing up with picking them out. The particulars of the setup and the transaction are for the calling label
    "You wait patiently while [the_person.title] changes." #lol make MC wait while we generate all the outfits.
    python:
        count = 0
        outfits = build_outfit_selection(the_person)
        preferences = WardrobePreference(the_person) #For determining if she loves the outfit or not
        the_person.apply_outfit(outfits[0])

    "It isn't long until [the_person.title] emerges from the dressing room."
    $ the_person.draw_person()
    the_person "Hey! What do you think?"
    "She gives you a little turn so you can see all sides."
    $ the_person.draw_person(position = "back_peek")
    if preferences.evaluate_outfit(outfits[0], the_person.effective_sluttiness() + 10, sluttiness_min = the_person.effective_sluttiness() - 10):
        the_person "I actually really like this one!"
    else:
        the_person "I'm not certain about this one to be honest!"
    $ the_person.draw_person(position = "stand4")
    the_person "Be honest!"
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "It looks really good on you."
            the_person "Aww, thank you! Okay!"
            $ count += 1
            $ the_person.wardrobe.add_outfit(outfits[0])
            $ the_person.change_novelty(3)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfits[0], preferences) from _clothes_shopping_uniform_addition_1
        "Try something else":
            mc.name "I'm not sure that is the best look for you. Maybe try something else?"
            the_person "Hmm, yeah, I think you might be right."
    the_person "Okay, stay right there, I'll be right back with the next one."
    $ clear_scene()
    "You hang out for a bit. Your mind wanders a bit, thinking about [the_person.title] getting naked in the dressing room..."
    $ the_person.apply_outfit(outfits[1])
    $ the_person.draw_person()
    the_person "Hey... you aren't dozing off on me are you?"
    "You look up and check out [the_person.title]'s next outfit."
    mc.name "Hmm... interesting. Let me see the back."
    $ the_person.draw_person(position = "back_peek")
    the_person "Does it look good?"
    $ the_person.draw_person(position = "stand3")
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "That one is definitely a keeper."
            the_person "Great!"
            $ count += 1
            $ the_person.wardrobe.add_outfit(outfits[1])
            $ the_person.change_novelty(3)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfits[1], preferences) from _clothes_shopping_uniform_addition_2
        "Try something else":
            mc.name "I'm not sure that outfit works. What else do you have?"
    the_person "Okay, I have one more, I'll be right back with the last one."
    $ clear_scene()
    "Hmm... [the_person.title] is back there right now, stripping down, slipping into something else... maybe you should try and sneak a peek..."
    $ the_person.apply_outfit(outfits[2])
    $ the_person.draw_person()
    "You are just starting to consider trying to sneak back there when she pops out of the dressing room."
    the_person "Alright! Third time is a charm. How about this?"
    $ the_person.draw_person(position = "back_peek")
    the_person "Make sure to check all the angles!"
    $ the_person.draw_person(position = "stand4")
    menu:
        "Keep that outfit":
            #TODO change responses based on sluttiness of outfit
            mc.name "Yep! That outfit was MADE for you."
            the_person "Aww. Okay!"
            $ count += 1
            $ the_person.wardrobe.add_outfit(outfits[2])
            $ the_person.change_novelty(3)
            call clothes_shopping_ask_to_add_to_uniform(the_person, outfits[2], preferences) from _clothes_shopping_uniform_addition_3
        "Try something else":
            mc.name "Honestly I think you would be better off with something else. It just isn't flattering."
    if count == 0:
        the_person "Seriously? Not a single outfit? You are impossible!"
        the_person "Tell you what. I'm gonna go change out of this. While I'm in there, pick out something for me to try on that YOU think is good and I'll try it on, okay?"
        mc.name "Okay."
        $ clear_scene()
        "[the_person.possessive_title] disappears to the back room to change. You look around at the different clothing racks, looking for something for her to try on."
        call screen outfit_creator(Outfit("New Outfit"))
        if _return != "Not_New":
            $ created_outfit = _return
            "You put together an outfit and take them to the back."
            if preferences.evaluate_outfit(created_outfit, the_person.effective_sluttiness() + 10, sluttiness_min = the_person.effective_sluttiness() - 10):
                the_person "Oh! This looks really nice! Ok give me just a minute and I'll be out, but I think I like it!"
            else:
                the_person "Hmm, normally I probably wouldn't pick out something like this, but I'll try it on for you..."
            $ the_person.apply_outfit(created_outfit)
            $ the_person.draw_person()
            "The dressing room door opens and you see [the_person.title] standing there."
            if created_outfit.outfit_slut_score > the_person.effective_sluttiness() + 20:
                the_person "I umm... I don't think I can come out of here in this."
                mc.name "What are you talking about? It looks fantastic!"
                the_person "No. Get your looks in, [the_person.mc_title], but I understand now why you want me to come clothes shopping with you!"
                $ clear_scene()
                "She closes the door. Damn, you must have gone a little overboard with that outfit..."
                the_person "I'm going to change back into, you know, DECENT clothes."
                $ the_person.change_stats(happiness = -5, slut = 1, max_slut = 60)
            else:
                the_person "Alright, what do you think?"
                $ the_person.draw_person(position = "back_peek")
                the_person "I'm trying it on just for you!"
                $ the_person.draw_person(position = "stand4")
                menu:
                    "Keep that outfit":
                        #TODO change responses based on sluttiness of outfit
                        mc.name "What can I say, I have good taste!"
                        the_person "Alright!"
                        $ count += 1
                        $ the_person.change_novelty(3)
                        $ the_person.wardrobe.add_outfit(created_outfit)
                    "Try something else":
                        mc.name "I'm sorry, I think maybe I'm not the one who should be doing this."
                        the_person "Geeze, you're awful! Whatever, I liked the last outfit, I'm gonna get it even if you didn't like it!"
                        $ the_person.wardrobe.add_outfit(outfits[2])
                the_person "Alright, I'm gonna change back into my other clothes now..."
                $ clear_scene()
            $ created_outfit = None
        else:
            mc.name "I'm sorry [the_person.title], but I can't find anything that would suit you."
            the_person "Oh, I was so looking forward to your pick, a well, just let me get dressed so we can get out of here."

        $ the_person.apply_planned_outfit()
        #TODO consider something sexy here
        "You give her a minute to change back into her regular outfit."
        $ the_person.draw_person()
    else:
        the_person "Alright! I feel like this was actually a productive trip! I'm gonna go get changed back into my normal clothes."
        $ clear_scene()
        $ the_person.apply_planned_outfit()
        "You give her a minute to change back into her regular outfit."
        $ the_person.draw_person()
        the_person "Alright, I'm gonna go check out now."
        mc.name "I'll follow you."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] begins walking toward the front of the department store."
        "As you are walking, you walk by the section of women's undergarments."
        the_person "Oh! That's a really a good sale!"
        "Suddenly, [the_person.title] takes a detour into the underwear section."
        the_person "This is great!"
        if the_person.effective_sluttiness() < 25:
            "You see [the_person.title] looking at normal women's undergarments. You see her pick out a pair."
            the_person "I'm gonna go try these on real quick..."
            mc.name "Go ahead, I'll wait outside the door."
            the_person "Okay!"
            $ clear_scene()
            $ the_person.apply_outfit(outfits[3])
            "Behind the closed door, you hear [the_person.title] shuffling around a bit."
            the_person "Okay... I can't decide if I like this set or not. I know this is kinda crazy but, would you tell me what you think?"
            mc.name "Absolutely."
            $ the_person.draw_person()
            the_person "What do you think?"
            menu:
                "Looks great!":
                    mc.name "The color and cut looks great on you!"
                    the_person "Aww, thank you! Okay that's enough peeking..."
                    $ the_person.change_stats(slut = 1, max_slut = 40, happiness = 2)
                    $ count += 1
                    $ the_person.change_novelty(3)
                    $ the_person.wardrobe.add_outfit(outfits[3])
                "Not your style":
                    mc.name "Your body looks great, but this particular cut isn't flattering."
                    the_person "Yeah I was afraid of that. Thank you for your honesty! Okay that's enough peeking..."
                    $ the_person.change_stats(slut = 1, max_slut = 40, obedience = 2)
            $ clear_scene()
            $ the_person.apply_planned_outfit()
            "In another few moments, [the_person.title] emerges from the dressing room."
            $ the_person.draw_person()
            the_person "Alright, let's go before I try on something else!"

        else:
            "You watch as [the_person.title] goes through the lingerie. There is some really sexy stuff here..."
            "You watch as she grabs a couple of things."
            the_person "I'm gonna go try these on really quick."
            "She lowers her voice to a hush."
            the_person "I'll be looking for your expert opinion, so stay by the door, okay [the_person.mc_title]?"
            mc.name "Hell yeah I'll be right there."
            "She giggles and heads off to the dressing room."
            $ clear_scene()
            $ the_person.apply_outfit(outfits[3])
            "Behind the closed door, you hear [the_person.title] shuffling around a bit."
            the_person "Okay, are you ready out there?"
            mc.name "Absolutely."
            $ the_person.draw_person()
            the_person "What do you think?"
            "She gives you a quick turn, then bends over the bench in the dressing room."
            $ the_person.draw_person(position = "standing_doggy")
            "She wiggles her hips a couple of times."
            the_person "Do you think I'll be able to get a man's attention with this?"
            menu:
                "Looks sexy!":
                    mc.name "It certainly has my attention. Is there room for two in that dressing room?"
                    $ count += 1
                    if the_person.effective_sluttiness() < 60:
                        the_person "Mmm, not today [the_person.mc_title]."
                        "You gawk for another moment, but eventually the door closes and [the_person.title] begins changing back into her normal outfit."
                    else:
                        $ the_person.draw_person()
                        "[the_person.title] looks to the left, then to right. There's no one around. She speaks in a whisper."
                        the_person "Get in here!"
                        $ mc.change_location(changing_room)
                        "You slip into the changing room. [the_person.possessive_title] closes it behind her."
                        if the_person.effective_sluttiness() < 80 and the_person.get_opinion_score("public sex") < 1: #She just wants to mess around a little
                            the_person "Mmm... want to have a little fun? Nothing too crazy though, I don't want to get caught..."
                            menu:
                                "Have some fun":
                                    "You grab her waist and pull her close."
                                    call fuck_person(the_person, private = True, prohibit_tags = ["Vaginal", "Anal"]) from _clothes_shopping_sex_in_a_changing_room_1 #Nothing too serious
                                    $ the_report = _return
                                    #TODO chance if there is anyone else at the clothing store to get noticed.
                                    if the_report.get("girl orgasms", 0) > 0:
                                        the_person "Oh my god, I can't believe how good that was. I hope no one heard me cumming..."
                                        $ the_person.change_stats(love = 3, happiness = 5)
                                    $ the_person.draw_person(position = "back_peek")
                                    "When you finish, you sneak back out of the changing room. You turn and check her out for a moment."
                                    the_person "I'll be out in a minute..."
                                    $ mc.change_location(clothing_store)
                                    $ clear_scene()
                                    "She closes the door slowly."
                                "Too risky":
                                    mc.name "I'm not sure I could keep it down... better play it safe."
                                    $ the_person.change_obedience(2)
                                    the_person "Hmmph, okay. Guess I'll change back into my regular clothes."
                                    $ the_person.strip_outfit(exclude_feet = False)
                                    "She strips out of her outfit and starts to reach for her regular clothes."
                                    $ the_person.draw_person(position = "standing_doggy")
                                    "You reach down and run your hands along her hips. She stops and just enjoys the feeling of your hands on her."
                                    $ the_person.change_arousal(5)
                                    the_person "Oh... so we're gonna do some teasing instead..."
                                    "You grope her ass. She wiggles her hips."
                                    $ the_person.change_arousal(5)
                                    the_person "Mm... two can play that game..."
                                    "She backs up a bit, pushing her ass up against you. She grinds her ass against your crotch."
                                    $ mc.change_arousal(5)
                                    $ the_person.change_arousal(5)
                                    the_person "Ugh... we should get together later and do this again somewhere more private."
                                    $ the_person.draw_person()
                                    "She stands up and starts to shoo you."
                                    the_person "That's enough, get out of here! I'm gonna change back now."
                                    "You sneak back out of the changing room. You turn and check her out for a moment."
                                    the_person "I'll be out in a minute..."
                                    $ clear_scene()
                                    $ mc.change_location(clothing_store)
                                    "She closes the door slowly."
                        else:  #She wants to get a little crazy
                            "She reaches down and begins to stroke you through your pants."
                            $ the_person.change_arousal(10)
                            the_person "Oh god, this is so crazy! I want you so bad."
                            "Her hand goes up, then slips into your underwear and then goes back down. Her hand wraps around your cock. She begins to stroke it."
                            the_person "Will you fuck me? Please? I promise I'll try to keep it down."
                            $ mc.change_arousal(10)
                            menu:
                                "Fuck Her":
                                    mc.name "Fuck yeah, let's do it."
                                    the_person "Yes! But go quick, I don't want anyone getting suspicious."
                                    $ the_person.strip_outfit()
                                    $ the_person.change_arousal(10)
                                    "You both quickly get naked. She looks like she really enjoys getting naked for you."
                                    the_person "Just stick it in! I'm ready, no need to warm me up..."
                                    call fuck_person(the_person, private = True, prohibit_tags = ["Foreplay", "Oral"], skip_intro = True, skip_condom = True) from _clothes_shopping_sex_in_a_changing_room_12#Nothing too serious
                                    $ the_report = _return
                                    if the_report.get("girl orgasms", 0) > 0:
                                        the_person "Oh my god, I can't believe how good that was. I hope no one heard me cumming..."
                                        $ the_person.change_stats(love = 3, happiness = 5)
                                    $ the_person.draw_person(position = "back_peek")
                                    "When you finish, you sneak back out of the changing room. You turn and check her out for a moment."
                                    #TODO chance if there is anyone else at the clothing store to get noticed.
                                    the_person "I'll be out in a minute..."
                                    $ clear_scene()
                                    $ mc.change_location(clothing_store)
                                    "She closes the door slowly."
                                "Too risky":
                                    mc.name "I'm not sure I could keep it down... better play it safe."
                                    $ the_person.change_obedience(2)
                                    the_person "Hmmph, okay. Guess I'll change back into my regular clothes."
                                    $ the_person.strip_outfit(exclude_feet = False)
                                    "She strips out of her outfit and starts to reach for her regular clothes."
                                    $ the_person.draw_person(position = "standing_doggy")
                                    "You reach down and run your hands along her hips. She stops and just enjoys the feeling of your hands on her."
                                    $ the_person.change_arousal(5)
                                    the_person "Oh... so we're gonna do some teasing instead..."
                                    "You grope her ass. She wiggles her hips."
                                    $ the_person.change_arousal(5)
                                    the_person "Mm... two can play that game..."
                                    "She backs up a bit, pushing her ass up against you. She grinds her ass against your crotch."
                                    $ mc.change_arousal(5)
                                    $ the_person.change_arousal(5)
                                    the_person "Ugh... we should get together later and do this again somewhere more private."
                                    $ the_person.draw_person()
                                    "She stands up and starts to shoo you."
                                    the_person "That's enough, get out of here! I'm gonna change back now."
                                    "You sneak back out of the changing room. You turn and check her out for a moment."
                                    the_person "I'll be out in a minute..."
                                    $ clear_scene()
                                    $ mc.change_location(clothing_store)
                                    "She closes the door slowly."
                                "Too risky\n{color=#ff0000}{size=18}Too aroused to say no{/size}{/color} (disabled)" if mc.arousal > 50:
                                    pass

                    $ the_person.change_stats(slut = 1, max_slut = 40, happiness = 2)
                    $ the_person.wardrobe.add_underwear_set(outfits[3])
                "Not your style":
                    mc.name "Your body looks great, but this particular cut isn't flattering."
                    the_person "Yeah I was afraid of that. Thank you for your honesty!"
                    $ the_person.change_stats(slut = 1, max_slut = 40, obedience = 2)
                    $ clear_scene()
                    "You gawk for another moment, but eventually the door closes and [the_person.title] begins changing back into her normal outfit."
            $ the_person.apply_planned_outfit()
            "In another few moments, [the_person.title] emerges from the dressing room."
            $ the_person.draw_person()
            the_person "Alright, let's go before I try on something else!"
    python:
        del outfits
        del preferences

    return count

label clothes_shopping_ask_to_add_to_uniform(the_person, the_outfit, preferences):
    if not the_person.is_employee:#Only run if person is employee
        return
    if preferences.evaluate_outfit(the_outfit, the_person.effective_sluttiness() + 10, sluttiness_min = the_person.effective_sluttiness() - 25): #Only run if she loves the outfit
        the_person "I really like this outfit. Do you think maybe, you could add it to the work uniform list?"
        the_person "I'd love to be able to wear it to work!"
        $ slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()
        if limited_to_top: #For now, we don't have clothes shopping for overwear only, so if it's limited to overwear then we certainly don't have the required policy
            "You take a look at the outfit, but quickly realize that it does not match the current uniform guidelines."
            mc.name "I'm sorry, but the current employee contract wouldn't allow for me to add that to the uniform guidelines."
            "She gives you a little pout, but seems to understand."
            return
        menu:
            "Add it to the uniforms"if the_outfit.outfit_slut_score <= slut_limit:
                mc.name "I think I'll do that when we get back to the office."
                the_person "Yay! Thank you [the_person.mc_title]!"
                $ mc.business.add_uniform_to_company(the_outfit, full_outfit_flag = True)
                #TODO figure out a way to make this count toward uniform goal count
            "Add it to the uniforms\n{color=#ff0000}{size=18}Too slutty!{/size}{/color} (disabled)" if the_outfit.outfit_slut_score > slut_limit:
                pass
            "Don't add to the uniforms":
                mc.name "It looks great, but I don't think the other girls would wear it as well as you."
                "She gives you a little pout, but seems to understand."
    return
