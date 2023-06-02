
init 720 python:              #Because Vren Init personality functionns at 1300

    def camilla_titles(person):
        valid_titles = []
        valid_titles.append(person.name)
        if person.effective_sluttiness() > 40:
            valid_titles.append("Slutwife")
            valid_titles.append("Cuckold Wife")
        return valid_titles

    def camilla_possessive_titles(person):
        valid_possessive_titles = [person.title]

        if person.effective_sluttiness() > 60:
            valid_possessive_titles.append("The Slutwife")
            valid_possessive_titles.append("Your Swinging Slut")

        if person.effective_sluttiness() > 90:
            valid_possessive_titles.append("The Bar Cumdump")
        return valid_possessive_titles
    def camilla_player_titles(person):
        valid_titles = "Mr. " + mc.last_name
        if person.love > 20:
            valid_titles.append(mc.name)
        if person.has_breeding_fetish:
            valid_titles.append("Bull")
        return valid_titles

    camilla_personality = Personality("camilla", default_prefix = wild_personality.default_prefix,
    common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
    common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
    common_dislikes = ["polyamory", "pants", "working", "the colour yellow", "conservative outfits", "sports"],
    common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything"],
    titles_function = camilla_titles, possessive_titles_function = camilla_possessive_titles, player_titles_function = camilla_player_titles)


#************* Personality labels***************#


label camilla_greetings(the_person):
    if mc.location == downtown_bar:
        if the_person.event_triggers_dict.get("camilla_progress", 0) >= 2:
            the_person "Hey there [the_person.mc_title]."
            the_person "You want to umm, you know, meet me in the back? I'm sure that's why you're here..."
        else:
            the_person "Hey there!"

    elif the_person.effective_sluttiness() > 60:
        if the_person.obedience > 180:
            the_person "Hello, [the_person.mc_title], it's good to see you."
        else:
            the_person "Hey there handsome, feeling good?"
    else:
        if the_person.obedience > 180:
            the_person "Hello, [the_person.mc_title]."
        else:
            the_person "Hey there!"
    return

label camilla_sex_responses(the_person):
    if the_person.effective_sluttiness() > 50:
        if the_person.obedience > 180:
            the_person "Oh my, keep doing that please!"
        else:
            the_person "Fuck it feels good when you do that. Keep going!"
    else:
        "[the_person.title] closes her eyes and moans quietly to herself."
    return

label camilla_climax_responses_foreplay(the_person):
    if the_person.effective_sluttiness() > 50:
        the_person "Oh fuck yes, I'm going to cum! I'm cumming!"
    else:
        the_person "Oh fuck, you're going to make me cum! Fuck!"
        "She goes silent, then lets out a shuddering moan."
    return

label camilla_climax_responses_oral(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Fuck yes, I'm going to cum! Make me cum!"
    else:
        the_person "Oh my god, you're good at that! I'm going to... I'm going to cum!"
    return

label camilla_climax_responses_vaginal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "I'm going to cum! Ah! Make me cum [the_person.mc_title], I want to cum so badly! Ah!"
        "She closes her eyes and squeals with pleasure."
    else:
        the_person "Ah! I'm cumming! Oh fuck! Ah!"
    the_person "Fuck I hope daddy does this to me again later!"
    return

label camilla_climax_responses_anal(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh fuck, your cock feels so huge in my ass! It's going to make me cum!"
        the_person "Ah! Mmhmmm!"
    else:
        the_person "Oh fucking shit, I think you're going to make me..."
        "She barely finishes her sentence before her body is wracked with pleasure."
        the_person "Cum!"
    return

label camilla_clothing_accept(the_person):
    if the_person.obedience > 180:
        the_person "It's for me? Thank you [the_person.mc_title], I'll add it to my wardrobe."
    else:
        the_person "Thanks, [the_person.mc_title]! I wonder if daddy would like to see me in this too."
    return

#label camilla_clothing_reject(the_person):
#    if the_person.obedience > 180:
#        the_person "Is that really for me [the_person.mc_title]? I want to... but I don't think I could wear that without getting in some sort of trouble."
#    else:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Wow. I'm usually up for anything but I think that's going too far."
#        else:
#            the_person "Wow. It's a little... skimpy. I don't think I could wear that."
#    return

# label camilla_clothing_review(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I love when you look at me like that, but I don't think the downtown_bar staff would appreciate it as much. I'd better clean up a bit."
#         else:
#             the_person "I'd better clean up some before I go to leave the downtown_bar..."
#     elif the_person.obedience > 180:
#         the_person "I'm sorry [the_person.mc_title], you shouldn't have to see me like this. I'll go and get cleaned up so I'm presentable again."
#     else:
#         if the_person.effective_sluttiness() > 40:
#             the_person "Whew, I think we messed up my clothes a bit. Just give me a quick second to get dressed into something more decent."
#         else:
#             the_person "My clothes are a mess! I'll be back in a moment, I'm going to go get cleaned up."
#     return

#label camilla_strip_reject(the_person, the_clothing, strip_type = "Full"):
#    if the_person.obedience > 180:
#        the_person "I'm sorry, but can we leave that where it is for now?"
#    elif the_person.obedience < 70:
#        the_person "Slow down there, I'll decide when that comes off."
#    else:
#        the_person "I think that should stay where it is for now."
#    return

# label camilla_sex_accept(the_person, the_position):
#     if the_person.effective_sluttiness() > 70:
#         if the_person.obedience < 70:
#             the_person "I was just about to suggest the same thing."
#         else:
#             the_person "Mmm, you have a dirty mind [the_person.mc_title], I like it."
#     else:
#         the_person "Okay, we can give that a try."
#     return

label camilla_sex_obedience_accept(the_person):
    if the_person.effective_sluttiness() > 70:
        the_person "Oh god [the_person.mc_title], I should really say no... but thinking about daddy doing this to me too gets me so hot!"
    else:
        if the_person.obedience > 180:
            the_person "Yes [the_person.mc_title], if that's what you want to do I'll give it a try."
        else:
            the_person "I... Okay, if you really want to, let's give it a try."
    return

# label camilla_sex_gentle_reject(the_person):
#     if the_person.effective_sluttiness() > 50:
#         the_person "Wait, I don't think I'm warmed up enough for this [the_person.mc_title]. How about we do something else first?"
#     else:
#         the_person "Wait. I don't think I'm comfortable with this. Could we just do something else instead?"
#     return

label camilla_sex_angry_reject(the_person):
    if the_person.effective_sluttiness() < 20:
        the_person "What the fuck! Do you think I'm just some whore who puts out for anyone who asks?"
        the_person "Not even daddy asks me to do that! Get the fuck away from me."
    else:
        the_person "What the fuck do you think you're doing, that's disgusting!"
        the_person "Not even daddy asks me to do that! Get the fuck away from me."
    return

label camilla_seduction_response(the_person):
    if the_person.obedience > 180:
        if the_person.effective_sluttiness() > 50:
            the_person "Yes [the_person.mc_title]? Want to take some pics together?"
        else:
            the_person "Yes [the_person.mc_title]? Is there something I can help you with?"
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, I know that look. Do you want to fool around a little?"
        elif the_person.effective_sluttiness() > 10:
            the_person "Oh, do you see something you like?"
        else:
            the_person "Oh, I don't really know what to say [the_person.mc_title]..."
    return

# label camilla_seduction_accept_crowded(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() < 20:
#             the_person "I suppose we could sneak away into the locker room... There's nothing wrong with that, right?"
#         elif the_person.effective_sluttiness() < 70:
#             the_person "Come on, let's sneak into the locker room and do it!"
#         else:
#             the_person "Oh fuck that sounds nice. I'm not sure I can wait until we sneak into the locker room, maybe we should just do it right here!"
#         return
#
#     if the_person.effective_sluttiness() < 20:
#         the_person "I suppose we could sneak away for a few minutes. There's nothing wrong with that, right?"
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Come on, let's go find someplace quiet where we won't be interrupted."
#     else:
#         the_person "No point wasting any time then, right? Let's get to it!"
#     return

# label camilla_seduction_accept_alone(the_person):
#     if mc.location == downtown_bar:
#         if the_person.effective_sluttiness() < 20:
#             the_person "Well, there's nobody around to see us..."
#         elif the_person.effective_sluttiness() < 50:
#             the_person "I can't believe how empty the gym is right now. Let's do it right here!"
#         else:
#             the_person "Oh [the_person.mc_title], the gym is empty, fuck me now!"
#         return
#     if the_person.effective_sluttiness() < 20:
#         the_person "Well, there's nobody around to stop us..."
#     elif the_person.effective_sluttiness() < 50:
#         the_person "Mmm, that's a fun idea. Come on, let's get to it!"
#     else:
#         the_person "Oh [the_person.mc_title], don't make me wait!"
#     return

#label camilla_seduction_refuse(the_person):
#    if the_person.effective_sluttiness() < 20:
#        "[the_person.title] blushes and looks away from you awkwardly."
#        the_person "I, uh... Sorry [the_person.mc_title], I just don't feel that way about you."
#
#    elif the_person.effective_sluttiness() < 50:
#        the_person "Oh, it's tempting, but I'm just not feeling like it right now. Maybe some other time?"
#        "[the_person.title] smiles and gives you a wink."
#
#    else:
#        the_person "It's so, so tempting, but I don't really feel up to it right now [the_person.mc_title]. Hold onto that thought though."
#    return

label camilla_flirt_response(the_person):
    if mc.location == downtown_bar:
        if the_person.love > 50:  #She loves you too much and is going to or already has called things off
            the_person "señor, didn't your mother ever tell you it's rude to hit on a married woman?"
            "[the_person.title] gives you a wink."
            return
        if the_person.event_triggers_dict.get("camilla_progress", 0) >= 2:
            the_person "Well why don't you meet me in the back in a bit and we'll see what happens?"
        else:
            the_person "Hey, maybe if you buy me a drink first."
            "[the_person.title] gives you a wink and smiles."
        return

    if the_person.obedience > 180:
        if the_person.effective_sluttiness() > 50:
            the_person "If that's what you want I'm sure I could help with that [the_person.mc_title]."
        else:
            the_person "Thank you for the compliment, [the_person.mc_title]."
    else:
        if the_person.effective_sluttiness() > 50:
            the_person "Mmm, if that's what you want I'm sure I could find a chance to give you a quick peek."
            "[the_person.title] smiles at you and spins around, giving you a full look at her body."
        else:
            the_person "Hey, maybe if you buy me dinner first."
            "[the_person.title] gives you a wink and smiles."
    return

label camilla_flirt_response_low(the_person):
    #She's in her own outfit.
    the_person "Thanks! It's really cute, right? My husband helped me pick it out!"
    $ the_person.draw_person(position = "walking_away")
    $ mc.change_locked_clarity(5)
    "She smiles and gives you a quick spin, showing off her outfit from every angle."
    $ the_person.draw_person()
    return

label camilla_flirt_response_mid(the_person):
    if the_person.effective_sluttiness() < 20 and mc.location.person_count > 1:
        if the_person.tits_visible:
            the_person "Are you sure you don't mean my tits look good in this outfit?"
            "She winks and wiggles her shoulders, setting her boobs jiggling for you."
            mc.name "All of you looks good, tits included."
            the_person "Good answer. I knew you would like this look when I was picking it out this morning."
        else:
            the_person "Aw, thanks! I thought this was a pretty hot look when I was getting dressed this morning."

        $ mc.change_locked_clarity(10)
        if camilla_lingerie_help_complete():
            the_person "Maybe sometime we could shopping together again and you could pick out something for me to wear again."
        else:
            the_person "Maybe hubby will let you come shopping with me one day, so you can tell me what else you want to see me in."
        mc.name "I think I would like that."

    else:
        the_person "Thanks, hubby thought I looked pretty hot in it too this morning when I picked it out."
        the_person "You want a better look, right? Here, how does it make my ass look?"
        $ the_person.draw_person(position = "back_peek")
        the_person "Good?"
        $ mc.change_locked_clarity(10)
        mc.name "Fantastic. I wish I could get an even better look at it."
        "[the_person.possessive_title] smiles and turns back to face you."
        $ the_person.draw_person()
        the_person "I'm sure you do. Buy me a drink and we'll see what happens."
    return

label camilla_flirt_response_high(the_person):
    if mc.location.person_count > 1 and the_person.effective_sluttiness("kissing") < (25 - (5*the_person.get_opinion_score("public_sex"))):
        # There are other people here, if she's not slutty she asks if you want to find somewhere quiet
        the_person "Not very high, unless we can find someplace quiet."
        menu:
            "Find someplace quiet":
                mc.name "Alright, let's find somewhere quiet then."
                the_person "Wait, I don't know if we should..."
                mc.name "Relax, it's just going to be a little bit of fun."
                "You take [the_person.possessive_title]'s hand and lead her away. After a moment of hesitation she follows you happily."
                "After searching for a couple of minutes you find a quiet space with just the two of you."
                the_person "Well... What did you want me all alone for?"
                $ the_person.draw_person(position = "kissing")
                "She steps close to you and puts her arms around your waist. She brings her face close to yours."

                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, private = True, start_position = kissing, skip_intro = True) from _call_fuck_camilla_47
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I'm a patient man, I can wait until we have some privacy. It's probably for the best; you might get a little loud."
                "[the_person.possessive_title] blushes and places her hand on your shoulder, massaging your muscles."
                the_person "Confident, senior? Maybe if you take me out to dinner you'll get your chance at some privacy."

    else:
        # She wants to kiss you, leading to other things.
        if mc.location.person_count == 1:
            #She's shy about the whole thing.
            "She looks around nervously."
            the_person "[the_person.mc_title], I... I mean, it's just us here."
            mc.name "So you're saying my chances are good?"
            $ the_person.draw_person(position = "kissing")
            "She takes a step closer to you and puts her arms around your waist, bringing her face close to yours."
            the_person "They could certainly be worse. Let's just... see where things go."

        else:
            #She's into turning you on.
            $ mc.change_locked_clarity(15)
            "[the_person.possessive_title] smiles mischievously and wiggles her hips."
            the_person "Maybe we can... fool around a little? Does that sound fun?"
            $ the_person.draw_person()

        menu:
            "Kiss her":
                if the_person.has_taboo("kissing"):
                    $ the_person.call_dialogue("kissing_taboo_break")
                    $ the_person.break_taboo("kissing")

                $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
                "You close the final gap and kiss her. She returns the kiss immediately, leaning her body against yours."
                call fuck_person(the_person, start_position = kissing, private = mc.location.person_count < 2, skip_intro = True) from _call_fuck_camilla_48
                $ the_person.call_dialogue("sex_review", the_report = _return)
                $ the_person.review_outfit()

            "Just flirt":
                mc.name "I wish we could, but I'll need to take a rain check."
                "[the_person.title] pouts and steps back, disappointed."
                mc.name "Don't worry, we'll get there soon enough. I just want to wait for the right time."
                #TODO: There should be boyfriend/family specific variants here like "Right, what was I even thinking? I don't know what came over me."
                the_person "Right. Sure."
                "She tries to hide it, but you can tell she's a little disappointed."
    return


label camilla_hookup_rejection(the_person):
    the_person "Your loss! Just thinking about you makes me want to get on my knees, and you could have had some of this..."
    return

label camilla_hookup_accept(the_person):
    $ mc.change_location(downtown_bar)

    "A few minutes later, you walk into the bar. You start walking back toward the women's restroom. The bartender nods to you as you pass the bar."
    $ work_bathroom.show_background()
    $ the_person.draw_person(position = "stand4")
    $ the_person.arousal = 20
    "You discover [the_person.possessive_title] standing at one of the sinks, touching herself while waiting for you. Her pussy glistens with arousal."
    "You quickly lock the door behind you. She notices you walk in but doesn't say a word."
    $ the_person.draw_person(position = "kissing")
    "You walk over to her silently. She looks into your eyes as she wraps her arms around your shoulders. You bring your face to hers and begin to make out."
    "You waste no time and grab her hips with your hands. You pull her close and she begins to grind her hips against yours."
    the_person "Mmmm, my favorite bull is here to take care of me."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #35 + 2
    "You run your hands along her stomach and back up a little bit, giving yourself some room to work."
    "You run your hand down [the_person.title]'s belly, across her mound and between her legs. She moans as your fingers run across her labia."
    the_person "I'm glad I called you, that feels good..."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #50 + 4
    "[the_person.title] runs a hand through your hair, while you run your fingers along her slit."
    "You move two fingers across her clitoris gently in long strokes."
    "She grinds herself happily against your hand. She moans appreciatively at your skilled fingering."
    "You bring two fingers to her dripping hole and push them up inside of her. You find her G-spot and begin to stroke it firmly."
    the_person "Mmm, that's the spot..."
    "[the_person.title] gasps as you stroke her. Her body is reacting quickly to your fingers."
    $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #65 + 6
    if the_person.arousal_perc > 100: #She is surprised how fast you make her cum
        "Suddenly, you feel her body go stiff and her moans ramp up quickly."
        the_person "Fuck! I'm gonna... you're gonna make me...!"
        $ the_person.have_orgasm()
        "[the_person.title] convulses as she orgasms. She is caught completely off guard by how fast you made her cum."
        "The hand on the back of your head lets go but you continue to stroke her G-spot for several more seconds."
    else:
        the_person "Mmm, that's it. Your fingers feel so good."
        "[the_person.title]'s hand on the back of your head guides your face down to one of her breasts. You like and suck at her nipples as you continue to finger her."
        "Her body is responding. Her hips are starting to twitch back and forth on their own as she approaches an orgasm."
        $ the_person.change_arousal( 15 + (mc.sex_skills["Foreplay"] * 2)) #80 + 8
        if the_person.arousal_perc > 100: #She orgasms
            the_person "Yes! That's it! I'm gonna cum!"
            $ the_person.have_orgasm()
            "[the_person.title] convulses as she orgasms. She moans and runs her hands through your hair."
            "You continue to stroke her G-spot for several more seconds."
        else:   #Not skilled enough to make her orgasm.
            "You are feverishly working at her pussy, but for some reason you can't seem to find the right spot."
            "Soon, your wrist starts to cramp up from the bad angle forcing you to slow. She is a little frustrated but still very aroused."
    $ the_person.change_arousal(-30) #50 + 8
    the_person "Mmm, that was a great warmup. Let me return the favor."
    "[the_person.possessive_title] quickly helps you undress, then gets down on her knees in front of you."

    $ the_person.draw_person(position = "blowjob")
    the_person "Here, don't forget this!"
    "She hands you her phone. You snap a couple picture of this bombshell on her knees with your cock in the foreground."
    "She gives your cock a few slow strokes before she begins to lick the tip. Her tongue feels like wet velvet as it circles around your glans."
    "[the_person.title] opens her mouth and then envelopes the end of your dick with her warm, wet mouth."
    "[the_person.title] keeps her mouth open wide and bobs her head back and forth to slide your cock in and out. The feeling of her soft, warm mouth sends shivers up your spine."
    "As she slides her tongue along your length you snap a few more pictures."
    "It feels amazing, you can tell if you let her keep going you will cum quickly."
    #TODO write blowjob finish scene#
    mc.name "That feels great, but I don't want to finish in your mouth. Why don't you stand up and turn around..."
    $ the_person.draw_person(position = "standing_doggy")
    if the_person.effective_sluttiness() > 40: #She asks if you want to use a condom
        the_person "Do you want to put on a condom first?"
        menu:
            "Put on a condom":
                mc.name "Yeah, I'd probably better. I may not be able to resist not pulling out."
                if the_person.effective_sluttiness() > 60:
                    the_person "I mean... it's okay with me if you wanted to stick it in for a little bit without one on, you know, just to get started..."
                    if the_person.effective_sluttiness() > 90:
                        the_person "... or even just finish inside me. I promise I wouldn't mind at all!"
                    mc.name "Maybe next time!"
                "You get a condom and put it on quickly."
                $ mc.condom = True
            "Fuck her raw":
                $ mc.condom = False
                mc.name "No way, I want to feel everything."
                if the_person.effective_sluttiness() > 60:
                    the_person "Mmmm, sounds good. I was hoping you would say that!"
                    if the_person.effective_sluttiness() > 80:
                        "She wiggles her ass back and forth a little bit."
                        the_person "You don't need to worry about pulling out. My husband goes crazy when another man cums inside me!"
                else:
                    the_person "Okay, just make sure to pull out before you finish, okay?"
    else:
        the_person "You have a condom right? Make sure you put one on..."
        mc.name "Right! I'd probably better. I may not be able to resist not pulling out."
        "You get a condom and put it on quickly."
        $ mc.condom = True
    "You put your hands on her hips and put your dick at her entrance. She is still soaked from your fingering earlier, so you easily slide into her."
    "Her pussy feels amazing wrapped around your erection. Her legs shake a bit as she gets used to the depth of your penetration."
    $ the_person.change_arousal(20) #70 + 8
    the_person "Ohhh, [the_person.mc_title]... That is exactly what I was hoping for when I sent you that text earlier. That feels so good..."
    "You give her a few tentative thrusts, then quickly pick up the pace and begin fucking her in earnest."
    "You set her phone to video mode, and take a clip of her backside rippling as you thrust in and out of her."
    "Your hips slap against [the_person.possessive_title]'s ass as you fuck her vigorously."
    $ the_person.call_dialogue("sex_responses_vaginal")
    if mc.condom == True:
        "You grasp her ass with both hands and begin to grope her. You knead her cheeks as your hips slowly work your erection in and out of her."
        $ the_person.change_arousal(20) #90 + 8
        if the_person.arousal_perc > 100:
            $ the_person.have_orgasm()
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. You can see in the mirror that her mouth is hanging open and her eyes are closed."
        "After the stimulation from her blowjob earlier, you know you aren't going to last long. You give her ass a loud spank."
        mc.name "That's it, bitch. I'm about to cum!"
        if the_person.effective_sluttiness() > 90: #She is so slutty, she begs for your cum.
            the_person "The condom! Take it off! Please!?! Your cock is so good, I want to feel you dump your load inside me!"
            "Your brain is getting a little hazy with lust. Surely there's nothing wrong with that, right?"
            menu:
                "Take It Off":
                    "In one swift motion you pull out of [the_person.title], pull the condom off, then shove yourself deep back inside her."
                    "You wad up the condom then throw it on the counter. It lands with splat."
                    the_person "Yes! Cum for me! I want to feel it!"
                    $ the_person.change_arousal(20) #110 + 8
                    "Her excitement is too much. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
                    the_person "Yes! Fill me with your cum!"
                    "You feel her pussy convulsing around your dick as she also starts to orgasm."
                    $ the_person.change_stats(slut = 1, happiness = 2)
                    $ the_person.cum_in_vagina()
                    $ the_person.draw_person( position = "standing_doggy") # redraw with cum
                    "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well used pussy."
                    "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
                    "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the restroom."
                    return
                "Leave It On":
                    mc.name "I can't pull out, even for a second!"
        "You bottom out and cum, dumping your load into the condom."
        "You wait until your orgasm has passed completely, then pull out and stand back. Your condom is bulged on the end where it is filled with your seed."
        if the_person.arousal_perc < 100:
            the_person "Wow, okay, I guess we are done?"
            $ the_person.change_stats(happiness = -5, obedience = -5)
            "She is a bit disappointed she didn't finish."
        else:
            the_person "That was nice. I'll make sure next time I'm in the mood to hit you up again..."
        "You take your condom off and throw it in the trash can. You both get dressed before sneaking out of the bathroom."
        return
    else: #You went in raw
        "You push yourself in as deep as you can go. [the_person.possessive_title] moans as you fill her completely."
        "With every thrust, her ass ripples pleasantly. You give her cheek an open handed spank and watch as shockwaves expand from the epicenter."
        "[the_person.title] moans at your rough treatment."
        $ the_person.change_arousal(20) #70 + 8
        if the_person.arousal_perc > 100:
            $ the_person.have_orgasm()
            "You can feel [the_person.title]'s pussy begin to spasm as she cums. Her silky wetness contracting around you feels amazing."

    if the_person.effective_sluttiness() > 70:
        the_person "You should stick a finger in my other hole while you fuck me and take a picture. Then hubby will have to reclaim both holes!"
        "Wow, it's not every day you have a beautiful married woman ask you to finger her ass while you bend her over and fuck her!"
        "You reach a hand forward and put your index finger in front of her face. She quickly gets the idea and opens her mouth with her tongue out, and begins slathering your finger with saliva."
        "When satisfied, you bring you fingers back to her tight back passage. You pull your cock almost completely out and stop you hip motion as you begin to press your finger against [the_person.title]'s puckered hole."
        "She forces her sphincter to relax and your finger begins to slip inside her."
        the_person "Ohh, yes. You can move your hips, that feels good..."
        "You give [the_person.possessive_title]'s cunt a few slow thrusts, while simultaneously fingering her other hole."
        $ the_person.change_arousal(20)#90 + 8
        if the_person.arousal_perc > 120:
            the_person "OH! It's so good... fuck I'm gonna cum again!!!"
            "You get the now familiar feeling of [the_person.title] cumming around your cock, but this time you can also feel the waves around your finger."
            $ the_person.have_orgasm()
            "You almost forgot to take some pictures! You grab her phone with your free hand and snap a few pics of her getting double penetration."
            "You wonder what it would feel like to make her cum again, but with your cock in her ass instead..."
            menu:
                "Stay Vaginal":
                    "As [the_person.title]'s pussy quivers around you, you decide to just keep doing what you are doing."
                "Fuck Her Ass" if the_person.effective_sluttiness() >= 70:
                    "You pull out of her pussy. Her juices leave a strand attached to you, connecting you to her cunt."
                    the_person "Mmm, [the_person.mc_title]? Why did you pull out... OH!"
                    "Her question is swiftly answered when she feels your manhood poking her puckered hole."
                    if the_person.effective_sluttiness() > 90:
                        the_person "Yes! Fuck my ass good!"
                    else:
                        the_person "Oh my... be careful!"
                    "With your hands firmly on her hips, you slowly push forward. It takes several seconds of steady pressure until you finally bottom out."
                    the_person "Oh god you make me feel so dirty... I love it!"
                    "You fuck her hard but at a steady, even pace."
                    "[the_person.possessive_title] moans, matching each hip movement of yours with a movement of her own."
                    the_person "It feels so deep... I can't... my legs!"
                    "Her knees give out, but you are too close to stop fucking her. You grab her hips roughly and pick up the pace."
                    $ the_person.change_arousal(20)#110 + 8
                    "Her ass begins to spasm. Her buttery smooth back passage squeezes you over and over as her body is racked with yet another orgasm. It feels incredible."
                    $ the_person.have_orgasm()
                    mc.name "Get ready, I'm gonna cum!"
                    "[the_person.title] is incoherent, and doesn't process your words."
                    "You plunge deep into her ass and hold it there while you cum. She gasps in time with each new shot of hot semen inside of her."
                    $ the_person.cum_in_ass()
                    $ the_person.draw_person(position = "standing_doggy") # redraw for cum
                    "You stand there for a minute, holding her hips in the air, you dick buried in her bowel as it softens. Eventually she speaks up."
                    the_person "Wow... okay... I think I can stand now..."
                    "You slowly let her down. Her legs buckle for a second, but she catches herself."
                    "You see a faint trace of your semen running down the back of her leg."
                    "You take several pics now. Her hole is gaping slightly and you can see the faint tint of your creamy deposit inside it."
                    the_person "That was SO good. You'll be hearing from me again, I'm sure. I can't wait to send hubby those pictures..."
                    "You and [the_person.title] get cleaned up and dressed, then sneak out of the restroom."
                    return
                "Fuck Her Ass\n{color=#ff0000}{size=18}Requires 80 sluttiness{/size}{/color} (disabled)" if the_person.effective_sluttiness() < 80:
                    pass
    "[the_person.possessive_title]'s creamy cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    mc.name "Get ready, I'm gonna cum!"
    $ the_person.change_arousal(35)
    if the_person.effective_sluttiness() > 90:
        "To your surprise [the_person.title] reaches back with both hands and grabs your hips, pulling you deep inside of her."
        "Her grip is startlingly strong. You don't think you could pull out even if you wanted to!"
        the_person "That's it, cum with me!"
        "Your cum erupts in a torrent. Your seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
        $ the_person.have_orgasm()
        $ the_person.cum_in_vagina()
        $ the_person.draw_person(position = "standing_doggy") # redraw for cum
        "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well used pussy."
        "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
        "You take a moment to recover. Then you and [the_person.title] get cleaned up and dress. You quietly sneak out of the restroom."
        return
    elif the_person.effective_sluttiness() > 60:
        the_person "Oh god... you should probably pull out but... it feels so good..."
        "You briefly consider pulling out."
        menu:
            "Pull Out":
                "You pull out of [the_person.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
                the_person "Oh! It's so hot on my skin!"
                $ the_person.cum_on_ass()
                $ the_person.draw_person(position = "standing_doggy")
                "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
                "You use her phone and get several close up pictures of her luscious ass with your load covering it."
                "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
                return
            "Creampie":
                "Her pussy feels too good. You bottom out and cum, dumping wave after wave of your semen deep inside of her."
                "Your seed spills deep inside [the_person.title]. Her entire body begins to spasm as she joins you in orgasm."
                $ the_person.have_orgasm()
                $ the_person.cum_in_vagina()
                $ the_person.draw_person(position = "standing_doggy") # redraw for cum
                "You wait until your orgasm has passed completely, then pull out and stand back. Your cum leaks from her well used pussy."
                "You use her phone and get several close up pictures of her well used snatch with your load dripping out of it."
                "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
                return
    else:
        "[the_person.title] suddenly moves her hips forward, your cock slides out of her."
        the_person "Cum on my ass!"
        "You stroke your shaft as you blow your load over her ass. She holds still for you as you cover her with your sperm."
        $ the_person.cum_on_ass()
        $ the_person.draw_person(position = "standing_doggy")
        "You stand back and sigh contentedly, enjoying the sight of [the_person.possessive_title]'s ass covered in your semen."
        "You use her phone and get several close up pictures of her luscious ass with your load covering it."
        "You take a moment to recover. Then you and [the_person.title] get cleaned up and dressed. You quietly sneak out of the restroom."
    return

#label camilla_cum_face(the_person):
#    if the_person.obedience > 180:
#        if the_person.effective_sluttiness() > 60:
#            the_person "Do I look cute covered in your cum, [the_person.mc_title]?"
#            "[the_person.title] licks her lips, cleaning up a few drops of your semen that had run down her face."
#        else:
#            the_person "I hope this means I did a good job."
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    else:
#        if the_person.effective_sluttiness() > 80:
#            the_person "Ah... I love a nice, hot load on my face. Don't you think I look cute like this?"
#        else:
#            the_person "Fuck me, you really pumped it out, didn't you?"
#            "[the_person.title] runs a finger along her cheek, wiping away some of your semen."
#    return

label camilla_cum_mouth(the_person):
    if mc.location == downtown_bar or the_person.has_cum_fetish:
        if the_person.has_cum_fetish or the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 1:
            the_person "Your cum tastes great [the_person.mc_title]! I bet I get another tasty load later..."
            $ play_swallow_sound()
            "[the_person.possessive_title] winks at you as she swallows your cum."
        elif the_person.effective_sluttiness() > 50 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Thanks, [the_person.mc_title]. I hope daddy cums in my mouth later too!"
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title]. It doesn't taste the best, but I'm always a good little slut."
    elif the_person.obedience > 180:
        if the_person.effective_sluttiness() > 60 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "That was very nice [the_person.mc_title], thank you."
        else:
            "[the_person.title]'s face grimaces as she tastes your sperm in her mouth."
            the_person "Thank you [the_person.mc_title], I hope you had a good time."
    else:
        if the_person.effective_sluttiness() > 80 or the_person.get_opinion_score("drinking cum") > 0:
            the_person "Your cum tastes great [the_person.mc_title], thanks for giving me so much of it."
            "[the_person.title] licks her lips and sighs happily."
        else:
            the_person "Bleh, I don't know if I'll ever get used to that."
    return

label camilla_cum_pullout(the_person):
    # Lead in: "I'm going to cum!"
    if mc.condom: #TODO: All of the cum-drunk stuff
        if the_person.wants_creampie and not the_person.has_taboo("condomless_sex"): #TODO: FIgure out we want any more requirements for this to fire.
            if the_person.knows_pregnant:
                the_person "I'm already pregnant, why are we even bothering with a condom?"
                the_person "Take it off and cum inside my pussy, just like you did when you knocked me up!"
            elif the_person.on_birth_control:
                the_person "You are? Do..."
                "She moans, almost desperately."
                the_person "... Do you want to cum inside me? Just take the condom off!"
                the_person "I just want your cum!"
            elif camilla_is_fertile():
                the_person "Oh god... I can't resist it!"
                the_person "I want you to cum in my pussy [the_person.mc_title]!"
                "She seems almost desperate as she moans."
                the_person "I don't care if you knock me up! I'm just your... breeding slut!"
            else:
                the_person "You should take the condom off!"
                the_person "It's okay, I'm infertile... nothing will happen!"
                "She seems almost desperate as she moans."

            menu: #TODO: Add a varient of this normally so you can stealth a girl (don't do that in real life, it's super fucked up).
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
                elif camilla_is_fertile(): #Yeah, she's not on BC and asking for you to creampie her. She's looking to get pregnant.
                    the_person "Yes! Cum inside me and knock me up! Breed me like the slut I am!"
                else:
                    the_person "Yes! Cum inside me! I love it!"
            elif the_person.on_birth_control: #She's on the pill, so she's probably fine
                the_person "I'm on the pill, cum wherever you want [the_person.mc_title]!"
                $ the_person.update_birth_control_knowledge()
            else: #Too distracted to care about getting pregnant or not. Oh well, what could go wrong?
                the_person "Ah! Do it!"
        else:
            if not the_person.on_birth_control: #You need to pull out, I'm not on the pill!
                the_person "Please pull out! I want you to cum all over me instead!"

            elif the_person.get_opinion_score("creampies") < 0:
                the_person "Make sure to pull out, you can cum anywhere else you want, I just don't like it inside me!"

            elif camilla_is_fertile():
                the_person "Can you pull out? I'm not ready to get pregnant yet!"

            else:
                the_person "Ah, really? Can you pull out? I just like it better that way..."
    return

label camilla_cum_condom(the_person):
    if the_person.effective_sluttiness() > 75 or the_person.get_opinion_score("creampies") > 0:
        the_person "Mmm, your cum feels so warm. I wish you weren't wearing a condom; I bet you would feel amazing raw."
    else:
        the_person "Whew... I can feel how warm your cum is through the condom. It feels nice."
    return

label camilla_cum_vagina(the_person):
    if the_person.has_taboo("creampie"):
        $ the_person.call_dialogue("creampie_taboo_break")
        $ the_person.break_taboo("creampie")
        return

    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "Mmm, your cum is so nice and warm..."
            "She sighs happily."

        elif the_person.on_birth_control or not camilla_is_fertile():
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
                the_person "If you get me pregnant I'm not sure what to tell [so_title]..."
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
                the_person "Fuck, I told you to pull out! I have a [so_title]!"
                the_person "Whatever, I guess it's already done."
            else:
                the_person "Fuck, I told you to pull out!"
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

label camilla_cum_anal(the_person):
    if the_person.sluttiness > 75 or the_person.get_opinion_score("anal creampies") > 0:
        the_person "Oh god yes, cum inside me!"
    else:
        the_person "Oh god, ah!"
    return

#label camilla_surprised_exclaim(the_person):
#    $rando = renpy.random.choice(["Fuck!","Shit!","Oh fuck!","Fuck me!","Ah! Oh fuck!", "Ah!", "Fucking tits!", "Holy shit!", "Fucking shit!"])
#    the_person "[rando]"
#    return

# label camilla_talk_busy(the_person):
#     if mc.location == downtown_bar:
#         the_person "Hey, I'm really sorry, but I need to keep on the lookout. Maybe another time?"
#     if the_person.obedience > 120:
#         the_person "Hey, I'm really sorry, but I've got some stuff I need to take care of. Could we catch up some other time?"
#     else:
#         the_person "Hey, sorry [the_person.mc_title] but I've got some stuff to take care of. It was great talking though!"
#     return

#label camilla_sex_strip(the_person):
#    if the_person.effective_sluttiness() < 20:
#        if the_person.arousal < 50:
#            the_person "Let me get this out of the way..."
#        else:
#            the_person "Let me get this out of the way for you..."
#
#    elif the_person.effective_sluttiness() < 60:
#        if the_person.arousal < 50:
#            the_person "This is just getting in the way..."
#        else:
#            the_person "Ah... I need to get this off."
#
#    else:
#        if the_person.arousal < 50:
#            the_person "Let me get this worthless thing off..."
#        else:
#            the_person "Oh god, I need all of this off so badly!"

#    return

# label camilla_sex_watch(the_person, the_sex_person, the_position):
#     if the_person.effective_sluttiness() < the_position.slut_requirement - 20:
#         $ the_person.draw_person(emotion = "angry")
#         the_person "Holy shit, are you really doing this in front of everyone?"
#         $ the_person.change_obedience(-2)
#         $ the_person.change_happiness(-1)
#         "[the_person.title] looks away while you and [the_sex_person.fname] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement - 10:
#         $ the_person.draw_person()
#         $ the_person.change_happiness(-1)
#         "[the_person.title] tries to avert her gaze while you and [the_sex_person.fname] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_requirement:
#         $ the_person.draw_person()
#         the_person "Oh my god, you two are just... Wow..."
#         $ change_report = the_person.change_slut(1)
#         "[the_person.title] averts her gaze, but keeps glancing over while you and [the_sex_person.fname] [the_position.verb]."
#
#     elif the_person.effective_sluttiness() > the_position.slut_requirement and the_person.effective_sluttiness() < the_position.slut_cap:
#         $ the_person.draw_person()
#         the_person "Oh my god that's... Wow that looks...Hot."
#         $ change_report = the_person.change_slut(2)
#         "[the_person.title] watches you and [the_sex_person.fname] [the_position.verb]."
#
#     else:
#         $ the_person.draw_person(emotion = "happy")
#         the_person "Come on [the_person.mc_title], you can give her a little more than that. I'm sure she can handle it."
#         "[the_person.title] watches eagerly while you and [the_sex_person.fname] [the_position.verb]."
#
#     return

# label camilla_being_watched(the_person, the_watcher, the_position):
#     if the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #They agree you should give it to her harder
#         the_person "I can handle it [the_person.mc_title], you can be rough with me."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's super slutty and doesn't care what people think.
#         the_person "Don't listen to [the_watcher.title], I'm having a great time. Look, she can't stop peeking over."
#
#     elif the_person.effective_sluttiness() >= the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #She's super slutty and encourages the watcher to be slutty.
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness >= the_position.slut_cap:
#         #She's into it and encouraged by the slut watching her.
#         the_person "Oh god, having you watch us like this..."
#         $ the_person.change_arousal(1)
#         "[the_person.title] seems turned on by [the_watcher.title] watching you and her [the_position.verb]."
#
#     elif the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_requirement:
#         #She's into it but shamed by the prude watching her.
#         the_person "[the_person.mc_title], maybe we shouldn't be doing this here..."
#         $ the_person.change_arousal(-1)
#         $ the_person.change_slut(-1)
#         "[the_person.title] seems uncomfortable with [the_watcher.title] nearby."
#
#     else: #the_person.effective_sluttiness() < the_position.slut_cap and the_watcher.sluttiness < the_position.slut_cap:
#         #They're both into it but not fanatical about it.
#         the_person "Oh my god, having you watch us do this feels so dirty. I think I like it!"
#         $ the_person.change_arousal(1)
#         $ the_person.change_slut(1)
#         "[the_person.title] seems more comfortable [the_position.verbing] you with [the_watcher.title] around."
#
#     return

# label camilla_work_enter_greeting(the_person):
#     if the_person.happiness < 80:
#         if the_person.obedience > 120:
#             "[the_person.title] gives you a curt nod and then turns back to what she was doing."
#         else:
#             "[the_person.title] glances at you when you enter the room then looks away quickly to avoid starting a conversation."
#
#     elif the_person.happiness > 120:
#         if the_person.effective_sluttiness() > 50:
#             "[the_person.title] looks up from her work when you enter the room."
#             the_person "Hey [the_person.mc_title]. Let me know if you need any help with anything. Anything at all."
#             "She smiles and winks, then turns back to what she was doing."
#         else:
#             "[the_person.title] turns to you when you enter the room and shoots you a smile."
#             the_person "Hey, good to see you!"
#
#     else:
#         if the_person.obedience < 90:
#             "[the_person.title] glances up from her work."
#             the_person "Hey, how's it going?"
#         else:
#             "[the_person.title] waves at you as you enter the room."
#             the_person "Hey, let me know if you need anything [the_person.mc_title]."
#     return

# label camilla_date_seduction(the_person):
#     if the_person.effective_sluttiness() > the_person.love:
#         if the_person.effective_sluttiness() > 40:
#             the_person "I had a great time [the_person.mc_title], but I can think of a few more things we could do together. Want to come back to my place?"
#             # the_person "I had a great night [the_person.mc_title], would you like to come back to my place and let me repay the favour?"
#         else:
#             the_person "I had a really good time tonight [the_person.mc_title]. I don't normally do this but... would you like to come back to my place?"
#             #the_person "I had a great night [the_person.mc_title], but I don't see why it should end here. If you want to come back to my place I can think of a few things we could do."
#     else:
#         if the_person.love > 40:
#             the_person "You're such great company [the_person.mc_title]. Would you like to come back to my place and spend some more time together?"
#         else:
#             the_person "I had a great night [the_person.mc_title]. Would you like to come back to my place for a quick drink?"
#     return

## Role Specific Section ##
# label camilla_improved_serum_unlock(the_person):
#     mc.name "[the_person.title], now that you've had some time in the lab there's something I wanted to talk to you about."
#     the_person "Okay, how can I help?"
#     mc.name "All of our research and development up until this point has been based on the limited notes I have from my university days. I'm sure there's more we could learn, and I want you to look into it for me."
#     "[the_person.title] smiles mischievously."
#     the_person "I've got an idea that you might want to hear then. It's not the most... orthodox testing procedure but I think it is necessary if we want to see rapid results."
#     mc.name "Go on, I'm interested."
#     the_person "Our testing procedures focus on human safety, which I'll admit is important, but it doesn't leave us with much information about the subjective effects of our creations."
#     the_person "What I want to do is take a dose of our serum myself, then have you record me while you run me through some questions."
#     return

label camilla_sex_toy_taboo_break(the_person):
    pass
    return

label camilla_roleplay_taboo_break(the_person):
    pass
    return

label camilla_condomless_sex_taboo_break(the_person):
    if the_person.knows_pregnant:
        the_person "I don't mind, it's not like I could get more pregnant."

    elif the_person.get_opinion_score("bareback sex") > 0:
        the_person "You want to do me raw? That's so hot."
        if the_person.on_birth_control or not camilla_is_fertile():
            the_person "I'm infertile, so you shouldn't have anything to worry about."
            $ the_person.update_birth_control_knowledge()
            if the_person.get_opinion_score("creampies") > 0:
                the_person "If you want to you can still pull out. It might be smart to do that."
                $ the_person.update_birth_control_knowledge()
                mc.name "Do you feel smart today?"
                "She bites her lip and shakes her head."
                the_person "No, not particularly."
            elif the_person.get_opinion_score("creampies") < 0:
                the_person "You'll need to pull out though. I just don't like the cleanup and the way it oozes out of you all day long."
        else:
            the_person "I'm not on the pill though. You'll need to pull out so you don't knock me up, got it?"
            $ the_person.update_birth_control_knowledge()

    elif the_person.love > 60:
        the_person "I want to feel close to you too [the_person.mc_title]."
        if the_person.on_birth_control:
            the_person "I'm on birth control, so you don't need to worry about getting me pregnant."
            $ the_person.update_birth_control_knowledge()
        elif not camilla_is_fertile():
            the_person "It's okay. I'm actually infertile, so you don't need to worry about getting me pregnant."
            if the_person.get_opinion_score("creampies") > 0:
                the_person "If we're doing this, I don't want you to pull out when you finish either."
                the_person "I want the full experience of having another man fuck me and cum deep inside."
            elif the_person.get_opinion_score("creampies") < 0:
                the_person "You'll need to pull out though. This is already kind of weird, and I don't want you oozing out of me all day long."
        else:
            if the_person.get_opinion_score("creampies") > 0:
                the_person "If we're doing this, I don't want you to pull out when you finish either."
                the_person "I've never experienced risky sex... it sounds so hot!"
            elif the_person.get_opinion_score("creampies") < 0:
                the_person "You'll need to pull out, I'm not ready to be a mother!"

    else:
        if the_person.get_opinion_score("creampies") > 0:
            the_person "If we're doing this, I don't want you to pull out when you finish either."
            the_person "I've never experienced risky sex... it sounds so hot!"
        elif the_person.get_opinion_score("creampies") < 0:
            the_person "You'll need to pull out, I'm not ready to be a mother!"
    return

label camilla_creampie_taboo_break(the_person):
    if the_person.wants_creampie:
        if the_person.knows_pregnant:
            the_person "OH señor! I love your cum deep inside me."
            "She sighs happily."

        elif the_person.on_birth_control or not camilla_is_fertile():
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

        elif not the_person.on_birth_control and camilla_is_fertile():
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

label camilla_sleepover_yourplace_response(the_person): #Invited her over to spend the night
    if the_person.sluttiness < 80:
        the_person "Sounds great! Save some energy, we can make it a fun night."
    else:
        the_person "Are you having the same dirty urges as me? Save some energy for me. We can make it a great night!"
    return

label camilla_sleepover_herplace_response(the_person): #Spending the night at her place
    if the_person.sluttiness < 80:
        the_person "Mmm, that sounds great! Bring a toothbrush, you can spend the night."
    else:
        the_person "You don't need the wine to seduce me."
    return


label camilla_sleepover_yourplace_sex_start(the_person): #Right before sexy times at your place
    "[the_person.title] slowly walks over to you, purposefully exaggerating her hip movements with each step."
    the_person "Thanks... you ready for some fun?"
    return


label camilla_sleepover_herplace_sex_start(the_person): #Right before sexy times at her place
    the_person "Mmm... what do you say we stay in and just cuddle tonight?"
    "She gives you a smirk. You can't help but frown at the thought of just cuddling..."
    the_person "Hah! Oh my god, you should have seen your face..."
    "She sets her wine down on her nightstand."
    the_person "Get over here! I'm ready for some fun!"
    return

label camilla_sleepover_impressed_response(the_person):  #If you've made her cum a lot
    the_person "Oh my god, you're making me cum my brains out... this is amazing..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I think I can keep going... I'm gonna be sore in the morning though!"
    return


label camilla_sleepover_good_response(the_person):  #If you've made her cum
    the_person "Ahhh, that was nice..."
    "[the_person.title] lies down in bed and catches her breath."
    the_person "I'm ready to go again if you are!"
    return

label camilla_sleepover_bored_response(the_person):  #If she hasn't cum yet
    the_person "Whew, good job. Get some water and let's go for another!"
    "You take some time to catch your breath, drink some water, and wait for your refractory period to pass."
    "You hold [the_person.title] in bed while she caresses you and touches herself, keeping herself ready for you."
    return

label camilla_lingerie_shopping_tame_response(the_person):
    the_person "Are you sure? This seems kinda tame..."
    mc.name "I know. I just want to see what it looks like on you."
    return

label camilla_lingerie_shopping_excited_response(the_person):
    the_person "Ah, this look great! I bet you will like this!"
    return

label camilla_lingerie_shopping_wow_response(the_person):
    the_person "Wow! I can honestly say I was not expecting you to go all in like this!"
    mc.name "If you don't feel comfortable with it, that's okay."
    "She is quiet, but you can hear here rustling around inside as she starts getting changed."
    the_person "It's okay... This is just to wear in private with you anyway... right?"
    return
