## Mom NTR Crisis Mod by Tristimdorion
# Based on the Pilotus13 Vanilla extension
# Overhaul edit by Longshot
# an idea that i want to implement later: if lily is slutty enough, she finds you spying and gets turned on, and then you and her have fun in the hall while jennifer does her thing in her room.
init 2 python:

    #cum_*_ntr def's added so pregnancy and sex counters will not be an issue in NTR.
    #otherwise she will blame you for her NTR babies
    #should be moved to methods under Person object later

    def cum_in_vagina_ntr(person):
        if person.outfit.can_add_accessory(creampie_cum):
            the_cumshot = creampie_cum.get_copy()
            the_cumshot.layer = 0
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("creampies"))
        person.change_happiness(3*person.get_opinion_score("creampies"))
        person.discover_opinion("creampies")
        person.did_she_become_pregnant(mc_father = False)

    def cum_in_mouth_ntr(person):
        if person.outfit.can_add_accessory(mouth_cum):
            the_cumshot = mouth_cum.get_copy()
            the_cumshot.layer = 0
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("drinking cum"))
        person.change_happiness(3*person.get_opinion_score("drinking cum"))
        person.discover_opinion("drinking cum")

    def cum_in_ass_ntr(person): #not used in mod? maybe it should be!
        #TODO: Add an anal specific cumshot once we have renders for it.
        if person.outfit.can_add_accessory(creampie_cum):
            the_cumshot = creampie_cum.get_copy()
            the_cumshot.layer = 0
            person.outfit.add_accessory(the_cumshot)
        person.change_slut(2*person.get_opinion_score("anal creampies"))
        person.change_happiness(3*person.get_opinion_score("anal creampies"))
        person.discover_opinion("anal creampies")

    def cum_on_face_ntr(person):
        if person.outfit.can_add_accessory(face_cum):
            the_cumshot = face_cum.get_copy()
            the_cumshot.layer = 0
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("cum facials"))
        person.change_happiness(3*person.get_opinion_score("cum facials"))
        person.discover_opinion("cum facials")

        person.change_slut(2*person.get_opinion_score("being covered in cum"))
        person.change_happiness(3*person.get_opinion_score("being covered in cum"))
        person.discover_opinion("being covered in cum")

    def cum_on_tits_ntr(person):
        if person.outfit.can_add_accessory(tits_cum):
            the_cumshot = tits_cum.get_copy()
            upper_item = person.outfit.get_upper_top_layer
            if upper_item:
                top_layer = upper_item.layer
            else:
                top_layer = -1
            the_cumshot.layer = top_layer + 1
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("being covered in cum"))
        person.change_happiness(3*person.get_opinion_score("being covered in cum"))
        person.discover_opinion("being covered in cum")

    def cum_on_stomach_ntr(person):
        if person.outfit.can_add_accessory(stomach_cum):
            the_cumshot = stomach_cum.get_copy()
            upper_item = person.outfit.get_upper_top_layer
            if upper_item:
                top_layer = upper_item.layer
            else:
                top_layer = -1
            the_cumshot.layer = top_layer + 1
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("being covered in cum"))
        person.change_happiness(3*person.get_opinion_score("being covered in cum"))
        person.discover_opinion("being covered in cum")

    def cum_on_ass_ntr(person):
        if person.outfit.can_add_accessory(ass_cum):
            the_cumshot = ass_cum.get_copy()
            lower_item = person.outfit.get_lower_top_layer
            if lower_item:
                top_layer = lower_item.layer
            else:
                top_layer = -1
            the_cumshot.layer = top_layer + 1
            person.outfit.add_accessory(the_cumshot)

        person.change_slut(2*person.get_opinion_score("being covered in cum"))
        person.change_happiness(3*person.get_opinion_score("being covered in cum"))
        person.discover_opinion("being covered in cum")

    def mom_ntr_mod_requirement():
        if mc.is_in_bed and mom.effective_sluttiness() >= 30:
            return mom.is_available and not mom.has_queued_event("sleeping_walk_in_label")
        return False

    def mom_ntr_select_finish(person):
        finishes = []
        if person.get_opinion_score("being covered in cum") > 0 or person.get_opinion_score("cum facials") > 0 or person.get_opinion_score("being submissive") < 0:
            finishes.append ("facial")
        if person.wants_creampie:
            finishes.append ("inside")
        if person.get_opinion_score("giving blowjobs") > 0 or person.get_opinion_score("drinking cum") > 0  or person.get_opinion_score("being submissive") < 0:
            finishes.append ("drink")
        finishes.append ("usual")
        return get_random_from_list(finishes)

    mom_ntr_mod_action = ActionMod("Mom NTR",mom_ntr_mod_requirement,"mom_ntr_mod_action_label",
        menu_tooltip = "At night, you hear strange sounds out of [mom.possessive_title]'s bedroom.", category = "NTR",
        initialization = init_action_mod_disabled, is_crisis = True)

label mom_ntr_mod_action_label():
    ## Mom having her private life
    $ the_person = mom
    "Some time late in the night, you're awoken by some noise down the hallway."
    "WARNING: This event (\"Mom NTR\") may contain non-consensual sexual acts. If you do not wish to see such content, choose \"Ignore it\" from the menu. The event can be disabled from the mod settings in your bedroom."
    menu:
        "Investigate":
            pass
        "Ignore it":
            return
    "As it seems to go on and on, you decide to investigate."
    "You drag yourself out of bed and enter the hallway. There is some rustling in [the_person.possessive_title]'s bedroom."
    "The door is ajar. You decide to take a peek."

    ## Determine what type of encounter it is
    if the_person.sluttiness >= 60:
        $ ran_num = renpy.random.randint (1,2)
    else:
        $ ran_num = 1

    $ mc.change_location(mom_bedroom)
    $ man_name = Person.get_random_male_name()
    $ wife_name = Person.get_random_name()
    while wife_name == the_person.name: ## Just to avoid stupid duplications
        $ wife_name = Person.get_random_name()

    ## Now determine how many clothes mom will take off
    if the_person.sluttiness < 40:
        $ clothes_number = renpy.random.randint (1,3) ## so it will be random from 1 to 3
    elif the_person.sluttiness < 80:
        $ clothes_number = renpy.random.randint (1,4) ## so it will be random from 1 to 4
    else:
        $ clothes_number = renpy.random.randint (2,4) ## so it will be random from 2 to 4

    ## Now determine how many clothes mom will take off
    if ran_num == 1: ## a scene with one man
        if the_person.get_opinion_score("giving blowjobs") > 0:
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "You take a look inside the room and your eyes widen. You see [the_person.possessive_title] sitting in front of an unknown man, sucking his cock."
            "By the look on man's face, you can tell that he is also quite surprised."
            "As they go on, you seem to recognize him. It's [man_name], one of [the_person.title]'s colleagues. You might have seen him at some corporate events."
            man_name "Wow, [the_person.fname]! We just got here and you already have my dick in your mouth. I didn't expect that, to say the least."
            $ the_person.draw_person(position = "blowjob", emotion = "happy")
            "[the_person.possessive_title] takes his dick out of her mouth and starts stroking it, looking up at [man_name]."
            the_person "Well, [man_name], you were so nice to me this evening that I felt you deserve a little present."
            $ the_person.discover_opinion("giving blowjobs")
            the_person "Besides, I just love to feel a strong, hard dick in my mouth."
            man_name "We have been working together for years now... I had no idea that you were such a cock-sucking slut, [the_person.fname]."
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "[the_person.possessive_title] smiles and gets up to embrace and kiss him passionately."
            "You are unsure what to do here."
        else:
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "You see [the_person.possessive_title] embracing some man, kissing him deeply."
            the_person "Oh [man_name], you are so nice. I had a wonderful evening!"
            "You recognize the man. It's [man_name], one of [the_person.possessive_title] colleagues."
            "You are unsure what to do here."
        menu:
            "Keep looking":
                "You decide to see what they are up to."
                "They go on kissing. After a while, [man_name] places his hands on [the_person.possessive_title]'s ass, caressing it."
                if the_person.sluttiness <= 30 or (the_person.is_dominant and the_person.sluttiness <= 45):
                    "[the_person.possessive_title] looks surprised by [man_name]'s actions."
                    the_person "No, [man_name]. We work together, there are some lines we should not cross."
                    the_person "It's late. Thanks for the wonderful evening. I'll see you in the office."
                    $ ran_num = renpy.random.randint(0,2) ##if man is aggressive
                    if ran_num < 1:
                        man_name "Sorry, [the_person.fname]. I lost control. I'll go now... good night."
                        "You go back to your room and through the half-closed door you see [man_name] leaving the house, head low in shameful disappointment."
                    else:
                        if the_person.get_opinion_score("giving blowjobs") > 0:
                            man_name "What the fuck, [the_person.fname]?! You've been flirting with me the whole evening, brought me to your room, sucked my cock, and now you want to stop?"
                        else:
                            man_name "Oh, no, [the_person.fname]. You've been flirting with me the whole evening, brought me to your room, and now you want to stop?"
                        man_name "No way. I can't go home with blue balls. You have to do something about it. You just need a little push."
                        $ mom_clothing = the_person.choose_strip_clothing_item()
                        if mom_clothing is None:
                            pass
                        else:
                            man_name "I don't think you need your [mom_clothing.name] anymore."
                            $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                            "He tears off [the_person.possessive_title]'s [mom_clothing.name] and throws it on the floor."
                            if the_person.get_opinion_score("being submissive") > 0:
                                "[the_person.possessive_title] just keeps standing there, shocked into submission, while [man_name] undresses her."
                            else:
                                the_person "Please, [man_name]. Don't do it. I'm so ashamed..."
                                man_name "Why don't you just shut up, [the_person.fname]? It will make life easier for both of us."
                        if clothes_number >1:
                            $ mom_clothing = the_person.choose_strip_clothing_item()
                            if not mom_clothing is None:
                                the_person "Please, not my [mom_clothing.name]..."
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "You watch as [the_person.possessive_title]'s [mom_clothing.name] is forcibly removed, despite her objections."
                                if the_person.get_opinion_score("being submissive") > 0:
                                    "[the_person.possessive_title] stands there in submission while [man_name] undresses her."
                                else:
                                    the_person "Please stop, [man_name]. You can't see me like this."
                                    man_name "I can and I will. Didn't I tell you to shut up? I suggest you do it."
                        if clothes_number >2:
                            $ mom_clothing = the_person.choose_strip_clothing_item()
                            if not mom_clothing is None:
                                man_name "You're not going to need this either, [the_person.fname]. Trust me."
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "[man_name] rips off her [mom_clothing.name]. His hands are all over [the_person.title]'s body."
                                if the_person.get_opinion_score("being submissive") > 0:
                                    "[the_person.possessive_title] keeps still, letting [man_name] undress her like a doll."
                                else:
                                    the_person "Please stop, [man_name]. I feel so naked..."
                                    man_name "Stop complaining, [the_person.fname], or I'll make it hurt."
                        if clothes_number >3:
                            $ mom_clothing = the_person.choose_strip_clothing_item()
                            if not mom_clothing is None:
                                $ the_person.draw_animated_removal (mom_clothing, position = "stand3", emotion = "sad")
                                "[man_name] continues stripping her. Now [the_person.title] is almost naked."
                                if the_person.get_opinion_score("being submissive") > 0:
                                    "Completely broken, [the_person.possessive_title] seems not to care what [man_name] sees or does."
                                else:
                                    "Afraid to anger him further, [the_person.possessive_title] just stands there, sobbing."
                        $ mom_clothing = None
                        if the_person.get_opinion_score("giving blowjobs") < 0:
                            man_name "Much better, [the_person.fname]! Now get on your knees and get back to it, you worthless whore."
                            "[the_person.title] can't refuse [man_name]'s force as she obeys him. She gets down on her knees."
                        else:
                            man_name "Much better, [the_person.fname]! Now get on your knees. I know want to suck my cock. I've seen the way you lick your lips when you look at it."
                            "[the_person.title] can't refuse [man_name]'s force as she obeys him. She gets down on her knees while he drops his pants."
                        $ the_person.draw_person(position = "blowjob", emotion = "sad")
                        man_name "That's better. Like the view of my friend? See how big he is because of you? Now get to work, [the_person.fname]!"
                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                        "[the_person.possessive_title] can't resist [man_name]'s urging and starts to suck him off."
                        if the_person.get_opinion_score("giving blowjobs") < 0:
                            man_name "That's it, bitch! You like to suck my cock, don't you? You're just too afraid to say it."
                            "[the_person.possessive_title] keeps sucking [man_name], making him groan with pleasure."
                        else:
                            man_name "Fuck, that's good. If I knew you were so good at sucking cock, I would've shoved mine in your throat a long time ago."
                            "[the_person.possessive_title] keeps sucking [man_name], making him groan with pleasure. She also seems to get a little aroused."
                        if the_person.vagina_available:
                            man_name "You're a great cocksucker, [the_person.fname]! Let's find out if you are any good at other stuff. Get on the bed and show me that fat ass."
                            $ the_person.draw_person(position = "doggy")
                            "[the_person.possessive_title] has lost all will to resist [man_name]'s orders. She gets on the bed, displaying her ass in front of him."
                            man_name "Good girl! You're already soaking wet, bitch. Did you know that?"
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "Oh, [man_name], just shut up and fuck me!"
                                the_person "I love it when a man is rough. You can see I'm already wet."
                                the_person "Please, [man_name], fuck me hard. Don't stop for anything. Make me scream like a bitch."
                                $ the_person.discover_opinion("being submissive")
                                man_name "No objections here, baby! I'll rail you so hard you'll have trouble walking in the morning."
                            else:
                                the_person "[man_name], please don't do it. We are colleagues... you can't do this."
                                man_name "I can and I will, [the_person.fname]. If you didn't want it, you wouldn't have flirted and let me along."
                                man_name "Now we are alone, you're on all fours, I'm rock hard, and you expect me to stop? I don't think so, cunt!"
                                "You think about stepping in and putting a stop to this, but it's like your body is frozen."
                            "You watch as [man_name] enters [the_person.possessive_title]'s pussy, bottoming out with one brutal thrust."
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "Fuck, yes! Please, [man_name], fuck me! Fuck me hard!"
                                man_name "You are really a slut, [the_person.fname]. Like being railed from behind?"
                                the_person "Yes. Yes. Do me! Fuck my slutty pussy, [man_name]!"
                                "For a while, there is silence in the room, aside from the wet sounds of [man_name]'s dick going in and out of [the_person.possessive_title]'s willing hole and the slapping of flesh on flesh."
                                if the_person.is_bald:
                                    "[man_name] grabs her by her neck and pulls her upwards."
                                else:
                                    "[man_name] grabs a fistful of her [the_person.hair_description] and pulls her upwards."
                                man_name "Do you like it, [the_person.fname]? Speak, whore!"
                                the_person "Oh yes! Don't stop, [man_name]. I'm going to cum!"
                                "[man_name] goes on pumping [the_person.possessive_title] and then slaps her ass, leaving a red handprint on her sweaty, quivering flesh."
                                the_person "Fuck! Yes, slap me! Hit me hard, it's so good while you're ravaging my pussy with your amazing cock!"
                                "They keep on fucking for some time, until both appear to be approaching orgasm."
                            else:
                                the_person "Oh... Please, [man_name], stop. You can't rape me like that!"
                                man_name "Shut your cockhole, [the_person.fname]. There's no way you can call this rape. You wanted it all along."
                                "The sounds of [man_name]'s dick forcing its way in and out of [the_person.possessive_title]'s resistant slit and the impacts of his hips on her ass fill the room. Each thrust is punctuated with a cry of pain and anguish from [the_person.possessive_title]."
                                if the_person.is_bald:
                                    "[man_name] grabs her by her neck and pulls her upwards."
                                else:
                                    "[man_name] grabs her [the_person.hair_description] and pulls her upwards."
                                man_name "You love this, don't you? Admit it, slut! You're squeezing my dick like a teenage virgin!"
                                the_person "Please, stop, [man_name]. Please, it hurts!"
                                "[man_name] answers [the_person.possessive_title]'s plea with even harder thrusts, beating his hips against her ass like a weapon."
                                man_name "Stop lying! This is what a cunt like you is made for. You'll beg me for more when I'm done!"
                                "He shoves her face down into the bed and keeps fucking her for some time, muffling her cries with her pillow. You can see her feet shaking in the air with each painful thrust."
                                "After another minute, [man_name] appears to be approaching orgasm."
                            $ finish = mom_ntr_select_finish(the_person)
                            if finish == "facial":
                                if the_person.get_opinion_score("being submissive") > 0:
                                    man_name "Fuck, I'm cumming! Get down on your knees!"
                                    "[man_name] steps back, sliding out of [the_person.possessive_title]. She hurries off the bed and drops to her knees before him."
                                    $ the_person.draw_person(position = "blowjob")
                                    the_person "Now shower me with your hot jizz. Cover my face with it!"
                                    man_name "Want me to paint your face, eh, [the_person.fname]? You're such a good little slut!"
                                    "[the_person.possessive_title] grins, reaching up toward him. You can hear the wet slapping as she desperately jerks his cock for her reward."
                                    "[man_name] can't hold for much longer and he starts cumming over [the_person.possessive_title]'s cock-drunk face."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    the_person "Mmm, [man_name], it feels so warm! I'm all covered in your love juices!"
                                    man_name "That was amazing, [the_person.fname]. We should do this more often."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] gets up and smiles."
                                else:
                                    man_name "Fuck, I'm cumming!"
                                    "[man_name] grabs [the_person.possessive_title] by the hips and yanks her back off the bed, manhandling her down onto her knees. You can see that she's a mess, tears and makeup smeared into a mask of misery."
                                    $ the_person.draw_person(position = "blowjob")
                                    man_name "Hold still while I mark you, bitch!"
                                    "[man_name] beats his cock furiously. He practically roars in triumph as he starts to cum, shooting cum all over [the_person.possessive_title]'s face and tits."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    man_name "Alright, [the_person.fname]. I expect you to behave better next time."
                            elif finish == "inside":
                                man_name "Fuck, I'm cumming!"
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "Please, [man_name], cum inside me. I don't care anymore, I just want to feel your warmth in me!"
                                    man_name "If you insist, baby. One cunt full of cum coming right up. Get your pussy ready."
                                    "[man_name] groans and shudders as he explodes inside of [the_person.possessive_title]."
                                else:
                                    "[the_person.possessive_title] struggles to lift her face from the bed."
                                    the_person "Please, [man_name], don't cum inside me. I won't tell anyone, but I can't get pregnant!"
                                    man_name "What did I tell you about complaining? I'll dump my load anywhere I want. Just shut up and take it!"
                                    "[man_name] shoves [the_person.possessive_title] down again, driving his cock into her. He growls possessively and his hips spasm as he blasts her womb full of his seed."
                                $ cum_in_vagina_ntr(the_person)
                                $ the_person.draw_person(position = "doggy")
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "Yes, yes! Fill me! Drench my pussy in your cum!"
                                    "[man_name] makes a few more thrusts and with a wet sound takes his cock out of [the_person.possessive_title]'s pussy."
                                    "You see some white drops falling to the blankets."
                                    man_name "Well, quite a nice view. One cum-filled bitch."
                                    "[the_person.possessive_title] turns over and smiles up at him."
                                    $ the_person.draw_person(position = "missionary")
                                    the_person "Mmm, it feels so good... you really know how to use a girl, [man_name]."
                                else:
                                    "You can hear [the_person.possessive_title] whimper miserably as her last vestige of dignity is stripped away."
                                    "[man_name] slaps her ass one final time as he pulls out. Some of his sperm drips from her, but most of it was deposited deep inside."
                                    man_name "Alright, [the_person.fname]. Your cunt is pretty good, but I expect you to behave better next time."
                            elif finish == "drink":
                                if the_person.get_opinion_score("being submissive") > 0:
                                    man_name "Fuck, I'm cumming! Get down on your knees!"
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] steps back, sliding out of [the_person.possessive_title]. She hurries off the bed and drops to her knees before him."
                                    the_person "Please Sir, fill my mouth with your hot jizz!"
                                    "[man_name] groans as [the_person.possessive_title] shoves her mouth down around his cock, bobbing her head and sucking hungrily."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    man_name "You're in no position to make requests, but I like the idea. Ngh, keep it up, I'm almost there!"
                                    "[the_person.possessive_title] purrs with lusty delight and sucks harder. Moments later, [man_name] moans in pleasure as he starts cumming into her mouth."
                                else:
                                    man_name "Fuck, I'm cumming!"
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "[man_name] grabs [the_person.possessive_title] by the hips and yanks her back off the bed, manhandling her down onto her knees. You can see that she's a mess, tears and makeup smeared into a mask of misery."
                                    man_name "Open wide, slut. Here comes your dessert."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] grabs [the_person.possessive_title]'s face in both hands and starts to fuck her mouth. She chokes loudly and pushes on his hips with her hands, but is powerless to resist him."
                                    man_name "Get used to being face fucked, [the_person.fname]. As of today, you're my own personal slut. Fuck, here it comes!"
                                    "[man_name] roars in triumph as he starts cumming into [the_person.possessive_title]'s throat."
                                "[the_person.possessive_title] gags and squirms as the cum overflows. She coughs loudly, shooting ropes of it across [man_name]'s merciless shaft."
                                $ cum_in_mouth_ntr(the_person) #$ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "It takes a while, but eventually he seems to reach his limit."
                                man_name "Wow, that was something. It's like that mouth of yours is meant for sucking cock."
                                "He takes his softening dick out of [the_person.possessive_title]'s mouth."
                                if the_person.get_opinion_score("being submissive") > 0:
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] gulps and drinks [man_name]'s cum in one shot. She licks her lips, cleaning a drop that had spilled out."
                                    "She looks up at him and smiles."
                                    the_person "Ah, you taste so good, [man_name]. I hope there will be more of it."
                                    man_name "You are just a perverted cum-loving slut, [the_person.fname]. You know that?"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] gets up and smiles."
                                    the_person "I know. And I'm glad you know too, now."
                                else:
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "[man_name] releases [the_person.possessive_title] from his grip. She gags and pulls away, pressing her shaking hands on the floor to keep from collapsing while she coughs up some of the load."
                                    "[man_name] laughs, reaching down for his pants."
                                    man_name "That's exactly where you belong, whore. I hope you understand that now."
                            elif finish == "usual":
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                    "[the_person.possessive_title] seems to be enjoying the rough treatment now. She screams in rapture, clearly not caring or understanding that you or [lily.fname] might come to investigate."
                                    the_person "Yes! Fuck! Tear me apart, [man_name]! I'm your bitch tonight and I need a proper fuck! Do it!"
                                    "The man keeps pumping her and slapping her already reddening ass. With each slap, [the_person.possessive_title] moans with pleasure."
                                    man_name "Didn't I say that you were just a slut, needing a push? I promised to give you a proper one, so you still owe me!"
                                    "[man_name] keeps reaming [the_person.possessive_title]'s pussy. After a few more thrusts, he pulls out and starts to cum on her ass."
                                    $ cum_on_ass_ntr(the_person) #$ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "His seed covers her butt, dripping down her legs and staining the bed."
                                    man_name "That's it, [the_person.fname]. You got what you deserved."
                                    $ the_person.draw_person(position = "kissing", emotion = "happy")
                                    "[the_person.possessive_title] gets up and kisses [man_name] with a passion."
                                    the_person "You were right, [man_name]. I lost count how many orgasms I had!"
                                    man_name "Good, it sounds like you understand what your purpose is now."
                                else:
                                    "[the_person.possessive_title] lies passively under [man_name] as he continues fucking her. She seems to have given up on resisting or reasoning with him."
                                    "[man_name] uses her like a cheap love doll. After a few more seconds, he pulls out and starts to cum on her ass."
                                    $ cum_on_ass_ntr(the_person) #$ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "His seed covers her butt, dripping down her legs and staining the bed."
                                    man_name "That's it, [the_person.fname]. You got what a teasing slut like you deserves."
                                    $ the_person.draw_person(position = "stand2", emotion = "sad")
                                    "[the_person.possessive_title] gets up. You see tears in her eyes."
                                    the_person "Damn you, [man_name]! I wish I never even met you. Now get out of my house. I never want to see you again!"
                                    $ the_person.draw_person(position = "sitting", emotion = "sad")
                                    "[the_person.possessive_title] sits on her bed, sobbing."
                                    man_name "Bah. You'll come crawling back soon enough. A cunt like you can't stand being empty for long."
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to bed."
                                "Some time later at night you are awoken again by screams coming from [the_person.possessive_title]'s room."
                                the_person "Take me with your hard dick, [man_name]. I want to feel it again. Please, use me again!"
                                man_name "Aren't you a cock-hungry whore, [the_person.fname]? Now lay on the table. I want to see your tits bouncing this time."
                                the_person "Of course, [man_name]. You can take me however you want. Just keep covering my slut body with your hot sperm."
                                "It seems that [the_person.possessive_title] does not wish for the encounter to end as her screams and [man_name]'s moans continue..."
                            else:
                                if the_person.sluttiness > 60:
                                    the_person "Yes, [man_name]. I'm sorry. You were right, it was scary... intense... but I feel good."
                                    man_name "Good girl. Let's get you cleaned up, then maybe I'll let you suck me off again."
                                    "They both go into the bathroom and you decide to get back to bed."
                                    "Some time later at night you are awoken again by the cries coming from the kitchen."
                                    the_person "Take me with your hard dick, [man_name]. I want to feel it again. Please, rape me again!"
                                    man_name "You're such a cock-hungry whore, [the_person.fname]. Now lay on the table. I want to see your tits this time, watch them bounce as I fuck you."
                                    the_person "Of course, [man_name]. You can take me however you want. Just keep filling me with your cum!"
                                    "It seems that [the_person.possessive_title] does not wish for the encounter to end as her screams and [man_name]'s moans continue..."
                                else:
                                    "You hurry back to your room, closing the door before [man_name] emerges. You hear his heavy footsteps move down the hall, followed by a slam and the sound of a car peeling out."
                                    "You go back to bed, ignoring the sounds of sobbing from [the_person.possessive_title]'s room. After a while, you hear her shuffle down the hall and run a shower, no doubt cleaning the evidence of her shameful encounter from her body."
                        else:
                            if the_person.get_opinion_score("giving blowjobs") > 0 :
                                "Letting her instincts take over, [the_person.possessive_title] keeps on sucking [man_name]'s cock. Soon he is moaning in pleasure and approaching climax."
                            else:
                                "[man_name] keeps fucking [the_person.possessive_title]'s face, holding her head so she can't pull away. It doesn't take long before he starts to approach climax."
                            $ finish = mom_ntr_select_finish(the_person)
                            if finish == "facial":
                                if the_person.get_opinion_score("being submissive") > 0:
                                    "Despite a rough start, [the_person.possessive_title] seems to have started enjoying herself. She takes his dick out of her mouth and looks up."
                                    $ the_person.draw_person(position = "blowjob")
                                    the_person "Wanna see this pretty face with your sperm on it, [man_name]? Now shower me with your hot jizz. Cover my whole body with it!"
                                    man_name "Want me to paint you white, huh [the_person.fname]? I knew you were a cum-slut the moment I laid eyes on you. Fuck, here it comes!"
                                    "[man_name] pulls back and starts beating himself to climax. You can see that [the_person.fname] is panting, but excited. Her eyes are unfocused and her tongue is lolling out of her open mouth."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "First he shoots [the_person.possessive_title]'s face and her [the_person.hair_description] with his semen."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "The load is big and he keeps going, covering [the_person.possessive_title]'s tits."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "It even drips down onto her stomach. There's almost none of [the_person.possessive_title]'s body that [man_name] doesn't claim."
                                    the_person "Now are you happy, [man_name]? See me covered in your love juices?"
                                    man_name "You're great, [the_person.fname]. We should do this more often."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] gets up and smiles."
                                else:
                                    man_name "Now you're getting it, slut. Are you ready for your facial?"
                                    $ the_person.draw_person(position = "blowjob")
                                    "[the_person.fname] coughs in protest, but the will to fight has been fucked out of her. [man_name] laughs and pulls her in harder, battering the back of her throat with his weapon."
                                    man_name "Yeah, you're ready. Here it comes, don't you fucking dare look away!"
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "First he shoots [the_person.possessive_title]'s face and her [the_person.hair_description] with his semen."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "The load is big and he keeps going, covering [the_person.possessive_title]'s tits."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "It even drips down onto her stomach. There's almost none of [the_person.possessive_title]'s body that [man_name] doesn't claim."
                                    "[man_name] shakes the last drops onto [the_person.possessive_title], then steps back to admire his handiwork."
                                    man_name "There, that's better. Now do you see what you're good for?"
                            elif finish == "drink":
                                if the_person.get_opinion_score("being submissive") > 0:
                                    "Despite a rough start, [the_person.possessive_title] seems to have started enjoying herself. Eventually, he pulls back to give her a chance to breathe."
                                    $ the_person.draw_person(position = "blowjob")
                                    the_person "Oh god... khh... that's so intense."
                                    man_name "I knew you could handle it, [the_person.fname]. I could see you were a born cocksleeve the first time I met you."
                                    the_person "I can't help it... your cock is just so beautiful. Please, let me finish it in my mouth."
                                    man_name "Ha! Now you're talking."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] resumes thrusting into [the_person.possessive_title]'s mouth, but no longer needs to hold her head to do it."
                                    "[the_person.possessive_title] sucks him hungrily, eager for the load he's about to deliver into her throat."
                                    "She starts sucking harder while playing with [man_name]'s balls. Soon he is on the edge."
                                    man_name "Oh fuck, here it comes! Take it, baby!"
                                    "[the_person.possessive_title] barely flinches as he drives into her, groaning and pumping blast after blast of thick cum directly into her stomach."
                                    $ play_swallow_sound()
                                    "Eventually, the tension drains from him, and he pulls back. [the_person.possessive_title] swallows loudly, then opens wide to show her empty mouth."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    the_person "That was amazing, there was so much I thought I was going to drown!"
                                    "She looks up at him and smiles."
                                    the_person "I hope there will be more next time."
                                    man_name "You're a perverted cum-slut, [the_person.fname]. You know that?"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] gets up and smiles."
                                else:
                                    man_name "No slacking off for you, whore!"
                                    "He grabs [the_person.possessive_title]'s head and impales it on his big cock."
                                    "It goes all the way inside with [man_name]'s balls hitting [the_person.title]'s jaw. She squirms, choking and struggling for air."
                                    man_name "I bet you love being face fucked, [the_person.fname]. Don't worry, I'll make sure you get exactly what you deserve."
                                    "[the_person.possessive_title]'s eyes lose focus and her struggles weaken. Ignoring her plight, [man_name] grips her head tighter and starts pulling her into him rapidly, using her throat as an onahole."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "Tears, spit, and slime drip from her mouth onto her tits as they swing back and forth from [man_name]'s violent use of her."
                                    "Finally, [man_name] roars in triumph and pulls her down, holding her at the base of his cock. His hips twitch as he starts dumping a massive load of cum directly into [the_person.possessive_title]'s stomach."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "You almost barge into the room, convinced you are about to watch [the_person.possessive_title] suffocate to death, but [man_name] finally pulls back, throwing her to the floor in a messy, broken heap."
                                    man_name "Wow, that was something. It's like that mouth of yours is meant for sucking cock."
                                    $ the_person.draw_person(position = "doggy")
                                    "[the_person.possessive_title] wheezes, coughing up some of the steaming load onto the carpet. Shaking and sobbing, she lifts herself back up again."
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    man_name "Oh good, you didn't pass out. Sometimes I'm too much for a girl, but I knew you were a natural cocksheath. Are you alright down there?"
                            elif finish == "usual":
                                "[man_name] pulls back, letting [the_person.possessive_title] breathe."
                                man_name "Fuck yeah. Now relax, I'm gonna fuck your tits and cover them in cum!"
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] leans back against the side of her bed, relieved to be able to breathe once more. Her chest is heaving with panting breaths."
                                    "[man_name] grabs her tits in both hands and lines his cock up between them, squeezing the hot flesh together and pumping his hips."
                                    man_name "These tits are great, [the_person.fname]. You were born to be a fucktoy, weren't you?"
                                    the_person "Y-yes sir. Please, u-use them however you wish."
                                    man_name "Ha! I knew I could fuck the defiance out of your whore mouth. Fuck, I'm close!"
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob")
                                    "[man_name] keeps pumping his hips, groaning as his cum shoots up between them. [the_person.possessive_title] flinches as it splashes off her chin and covers her tits."
                                    $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "blowjob")
                                    "There's so much it even drips down onto her stomach. With a final sated sigh, [man_name] steps back and releases her, enjoying the sight of his handiwork."
                                    man_name "There, now isn't it easier when you don't fight, [the_person.fname]?"
                                else:
                                    $ the_person.draw_person(position = "blowjob", emotion = "sad")
                                    "He pushes her back against the side of her bed and grabs her tits in both hands, thrusting his slimy cock in between them."
                                    "[the_person.possessive_title] whimpers as [man_name] starts pulling her breasts up and down, using them like an onahole to jack himself off."
                                    man_name "Fuck, that's so good. I bet you're loving this, finally being used like the fuckpuppet you've always known you were."
                                    "[the_person.possessive_title] looks away, tears staining her cheeks while [man_name] fucks her chest. After a few more thrusts, he starts to cum."
                                    man_name "Oh fuck, yeah! Ungh!!"
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion="sad")
                                    "[man_name] groans as he shoots his load up between [the_person.possessive_title]'s tits. It covers them in seconds, and some flies off to stain the floor as he keeps roughly pulling her mounds up and down until he finishes."
                                    man_name "Oh, fuck! [the_person.fname], you really dried me up! Now I gotta get going, my wife's waiting up for me. You better be ready for me next time."
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "How about a shower, [man_name]?"
                                "They both go into the bathroom and you decide to get back to bed."
                                "Some time later at night you are awoken again by the noise coming from [the_person.possessive_title]'s room."
                                the_person "Mrmh... Blgrhm..."
                                the_person "Fuck my throat with your hard dick, [man_name]. I need to feel it again. Please, use me until I pass out!"
                                man_name "Don't worry, [the_person.fname]. I plan to fuck your throat until you can't talk anymore!"
                                "It seems that [the_person.possessive_title] now does not wish for the encounter to end as her gagging and [man_name]'s moans continue."
                            else:
                                if the_person.sluttiness > 60:
                                    the_person "Yes, [man_name]. I'm sorry. You were right, it was scary... intense... but I feel good."
                                    man_name "Good girl. Let's get you cleaned up, then maybe I'll fuck your throat again."
                                    "They both go into the bathroom and you decide to get back to bed."
                                    "You have trouble getting back to sleep. [the_person.possessive_title] is making a lot of noise in the shower."
                                    the_person "Glkk... ghhh... ah, fuck! Take me with your hard dick, [man_name]. I want to feel it again. Please, rape my teasing whore face again!"
                                    man_name "You're such a cock-hungry slut, [the_person.fname]. Open wide, let's see if I can get my balls down to your chin."
                                    "It seems that [the_person.possessive_title] now does not wish for the encounter to end as her gagging and [man_name]'s moans continue."
                                else:
                                    "You hurry back to your room, closing the door before [man_name] emerges. You hear his heavy footsteps move down the hall, followed by a slam and the sound of a car peeling out."
                                    "You go back to bed, ignoring the sounds of sobbing from [the_person.possessive_title]'s room. After a while, you hear her shuffle down the hall and run a shower, no doubt cleaning the evidence of her shameful encounter from her body."
                else:
                    the_person "Oh, [man_name]. You clearly have some plans for tonight, don't you?"
                    if the_person.get_opinion_score("giving blowjobs") > 0:
                        "She strokes his penis a little."
                    else:
                        "She caresses the bulge in his pants."
                    the_person "I like those plans, and my little friend here seems to as well. Now let me help you get rid of those clothes."
                    "You see them help each other undress."
                    $ mom_clothing = the_person.choose_strip_clothing_item()
                    if not mom_clothing is None:
                        man_name "I don't think you need your [mom_clothing.name] anymore."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        "He takes off [the_person.possessive_title]'s [mom_clothing.name] and throws it on a nearby chair."
                    if clothes_number >1:
                        $ mom_clothing = the_person.choose_strip_clothing_item()
                        if not mom_clothing is None:
                            the_person "I like the touch of your soft hands, [man_name]."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "You watch as [the_person.possessive_title]'s [mom_clothing.name] is also removed. [man_name]'s hands are softly caressing her naked skin."
                    if clothes_number >2:
                        $ mom_clothing = the_person.choose_strip_clothing_item()
                        if not mom_clothing is None:
                            the_person "Ooooh, [man_name], I love the way you touch me. It makes me so excited..."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "[man_name] takes off [the_person.possessive_title]'s [mom_clothing.name]. His hands are all over her body."
                    if clothes_number >3:
                        $ mom_clothing = the_person.choose_strip_clothing_item()
                        if not mom_clothing is None:
                            the_person "I'm still overdressed, [man_name]. Please, take off my [mom_clothing.name] with those magical hands of yours."
                            $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                            "He grants her wish, caressing her body as he strips her down."
                    $ mom_clothing = None
                    $ the_person.change_slut(2, 40)
                    "They are both undressed, and you can clearly see where this is going."
                    the_person "Well, I think we are both ready for action. So, let's do it!"
                    menu:
                        "[the_person.possessive_title] lays on the bed..." if the_person.vagina_available:
                            $ the_person.draw_person(position = "missionary", emotion = "happy")
                            "You watch as [the_person.possessive_title] lays on her bed and spreads her legs, inviting [man_name] to enter her."
                            the_person "Oh, [man_name], how about you do me the old-fashioned way?"
                            man_name "Fuck, you look good like that... you don't have to ask me twice!"
                            "He quickly drops his shorts and climbs on top of [the_person.possessive_title], entering her pussy in one smooth thrust."
                            the_person "Oh yes, [man_name]! I really needed that. Do it!"
                            "[man_name] speeds up, pumping [the_person.possessive_title]'s wet vagina and kissing her hard."
                            man_name "God, [the_person.fname], you are really tight there!"
                            "[the_person.possessive_title] pulls [man_name]'s head down to hers, kissing him hungrily. Her hand caresses his back as he continues thrusting down into her."
                            "After a moment, she breaks the kiss to breathe, letting out a cry of pleasure."
                            the_person "Yes! Do me! I love how you do it! Fuck me harder!"
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "Harder, I beg you. I love being owned. Make me your little toy!"
                                $ the_person.discover_opinion("being submissive")
                                "[man_name] amplifies his movements. Now with each move he presses [the_person.possessive_title] against the bed, producing heavy squeaking sounds and the rhythmic slap of flesh on flesh."
                            $ the_person.change_arousal(renpy.random.randint(10,50))
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False

                            if not hidden or renpy.random.randint(0,2) == 1:
                                "[the_person.possessive_title] turns her head and sees that the door is slightly ajar and you are standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal_perc > 35:
                                    the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                    "[man_name] does not mind you joining the show as he keeps fucking [the_person.possessive_title]'s pussy."
                                    man_name "Go on, boy. You see she's ready for both of us. Aren't you, [the_person.fname]?"
                                    the_person "I don't mind [the_person.mc_title] seeing me like this. Now, come closer, dear."
                                    "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                    the_person "Good boy! Now let [the_person.possessive_title] take care of you."
                                    "She starts stroking your penis while [man_name] keeps driving his dick into her soaking vagina."
                                    the_person "Oh, [man_name], please go on. Keep fucking me!"
                                    man_name "Wow, [the_person.fname]. You really don't care about him seeing you being fucked liked that?"
                                    # NOTE: Does this sentence make sense with anything else than "mom" / "mother". Other characters would not use the titles, but for the sake of avoiding mentions of incest title should be used.
                                    #Longshot note: agreed, try not to hard-code family titles in case someone is playing a non-inc game and has changed her to "landlord" or something. Removing "your son seeing his [the_person.title]" in favor of "him seeing you".
                                    the_person "The only thing I care about right now is your cock inside of me. Keep going, [man_name]! Don't stop for anything!"
                                    while the_person.arousal_perc < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title]'s pussy. You can hear the wet sound of her sex taking his; clearly [the_person.possessive_title] is having great time."
                                        the_person "Please, [man_name], more. Do me! Do me!"
                                        if the_person.get_opinion_score("being submissive") > 0:
                                            the_person "Harder! Pin me down with that great shaft of yours! Use me as rough as you like!"
                                        "As she gets more and more turned on, the speed of her hand stroking your cock also increases."
                                        $ the_person.change_arousal(renpy.random.randint(10,50))
                                    "After being fucked by [man_name] for so long, [the_person.possessive_title] seems to be approaching orgasm."
                                    the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me as fast as you can, [man_name]!"
                                    "He starts to pump [the_person.possessive_title] with some ferocity, grunting with effort and fully burying his dick in her ove rand over again."
                                    $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                    $ the_person.have_orgasm()
                                    the_person "Yes! Yes! That's it! I love it, [man_name]!"
                                    man_name "Shit, [the_person.fname], your pussy is driving me crazy! I'm going to cum soon!"
                                    $ finish = mom_ntr_select_finish(the_person)
                                    if finish == "facial":
                                        the_person "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name]'s cock."
                                        the_person "Would you like to cover my face with your hot cum? I bet your wife never lets you to do this!"
                                        man_name "No, [wife_name] never wants anything exciting in bed. Sometimes I really hate it!"
                                        the_person "Well, that's your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking your cocks with both hands."
                                        man_name "I'm cumming [the_person.fname]!"
                                        "She leans closer so that [man_name]'s tip is just in front of her face."
                                        the_person "Do it, [man_name]! Cover me! Imagine I'm your frigid wife, and show me what you really want to do!"
                                        $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] groans and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Take it, you bitch! Feel my jizz all over your slutty face, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing this to his wife."
                                        the_person "You like that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "Fuck yeah, it really turns me on! I bet I'll be ready to go again soon."
                                        the_person "We'll discuss it later, [man_name]! Now I need to finish taking care of [the_person.mc_title]."
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick. The sensation of her skin on yours and the sight of her being such a slut is incredible, and in few seconds you are cumming on her tits."
                                        the_person "Mmm, much better! Now everyone is all taken care of."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to get cleaned up and talk."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person "Do me again, [man_name]. Fuck me harder! Shower your whore wife's face with your warm cum again!"
                                            man_name "Oh fuck! Get on your knees, slut! I'm cumming again!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and drift to sleep, listening to quiet moans and sounds of bedsprings from [the_person.possessive_title]'s room."
                                    elif finish == "inside":
                                        the_person "Yes! Do it, [man_name]! I want you to fill me."
                                        $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                        the_person "Yes, [man_name]! I want all inside me!"
                                        "After few seconds, [man_name] gets off of [the_person.possessive_title]. You see a trace of his cum dripping from [the_person.possessive_title]'s pussy."
                                        the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                        man_name "And you look gorgeous, [the_person.fname], lying there full of my cum. And with another man's cock in your hand, too!"
                                        the_person "I'm glad you like it, [man_name]! Now I need to finish with [the_person.mc_title]."
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a shower."
                                        $ the_person.draw_person(position = "walking_away")
                                        "As [the_person.possessive_title] starts walking toward the bathroom, you see several white drops falling on the floor."
                                        "While she walks past [man_name], he places his hand on her butt."
                                        the_person "First - the shower. Then we will see, dear."
                                        if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.title]'s room."
                                            the_person "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                            man_name "Take it all in, [the_person.fname]!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backward and his dick leaves her pussy with a wet sound . [the_person.possessive_title] gets on her knees in front of [man_name]'s cock."
                                        the_person "I want to taste your hot cum. I doubt your wife ever lets you do this!"
                                        man_name "[wife_name] never lets me do anything fun in bed, she's such a prude."
                                        the_person "Well, now's your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off. Meanwhile, one of her hands is still working on you."
                                        man_name "I'm gonna cum, [the_person.fname]!"
                                        "She keeps sucking him, bobbing her head at a steady pace and stroking you faster."
                                        the_person "Mmmmmm... Mmmm... Uhhh."
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shudders and starts filling her mouth with his load. There's so much it spills out onto her chin."
                                        man_name "Oh, yes! Suck it, [wife_name]!"
                                        "[man_name] clearly liked the idea of cumming in his wife's mouth."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        $ play_swallow_sound()
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it on her face."
                                        the_person "It seems you liked that, [man_name]! [wife_name] is just stupid. It's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I'll be ready to go again soon."
                                        the_person "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his cum too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that, she takes your cock between her hot lips."
                                        man_name "I never would have thought you were such cum-drinking fan, [the_person.fname]!"
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] slides her mouth down and up your dick, and in few seconds you cum inside. She leans back and gulps once more."
                                        the_person "There we go. Double the sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a shower."
                                        if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                            "You go back to your bedroom. Soon afterward, you hear screams from [the_person.possessive_title]'s room."
                                            the_person "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, please!"
                                            man_name "Suck it [wife_name], you bitch, or no sweets for you!"
                                            the_person "Mhhmhmh..."
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                                        "[the_person.possessive_title] closes the tip with her free hand so that no sperm is spilled."
                                        man_name "Oh fuck! That was great!"
                                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                                        the_person "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let me finish with my [the_person.mc_title]."
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum in her palm."
                                        the_person "There we go. All finished!"
                                        man_name "I don't believe it, [the_person.fname]. You just let your son watch us fuck, then jerked him off!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person "Didn't that turn you on, [the_person.mc_title]?"
                                        the_person "Now go to your room. [man_name] and I need to take a shower."
                                        if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                            "You go back to your bedroom and soon begin to hear screams from [the_person.possessive_title]'s room."
                                            the_person "Take me again, [man_name]. Bang me with your big, amazing dick!"
                                            man_name "Turn around, [the_person.fname]. I want you from behind."
                                            the_person "Oh, [man_name]! I'm cumming again! Slap my ass! Harder!"
                                            $ the_person.have_orgasm()
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "missionary", emotion = "angry")
                                    the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get back to your room now!"
                                    "You go back to your bedroom accompanied by the squeaking sounds from [the_person.possessive_title]'s room as [man_name] keeps pounding her."
                            else:
                                while the_person.arousal_perc < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title]'s pussy. It goes in and out with a wet sound. [the_person.title] moans loudly, and seems to be enjoying every thrust."
                                        the_person "Harder, [man_name], harder! Do me! Do me! Fuck me!"
                                        if the_person.get_opinion_score("being submissive") > 0:
                                            the_person "Please! Use me however you want, [man_name]. I love being your fuck toy! Fuck your slutty little [the_person.fname]!"
                                        else:
                                            pass
                                        "As she gets more and more turned on, her cries get louder and louder."
                                        $ the_person.change_arousal(renpy.random.randint(10,50))
                                "After being several minutes of fucked by [man_name], [the_person.possessive_title] draws close to orgasm."
                                the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! As fast as you can, [man_name]!"
                                "He starts to pump [the_person.possessive_title] with some ferocity, fully burying his dick in her."
                                $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                $ the_person.have_orgasm()
                                the_person "Yes! Yes! That's it! I love you, [man_name]!"
                                man_name "Shit, [the_person.fname], your pussy is driving me crazy! I'm gonna cum soon!"
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    the_person "Oh god, [man_name]! I want it on me!"
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards and his dick leaves her pussy with a wet sound. [the_person.possessive_title] gets on her knees in front of [man_name]'s cock."
                                    the_person "Please, cover my face with your hot cum! I bet your wife never lets you blast hers!"
                                    man_name "[wife_name] never wants anything wild like you do. Sometimes I really hate it!"
                                    the_person "Well, here's your chance to get back at her, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "Fuck! I'm cumming, [the_person.fname]!"
                                    "She leans closer so that [man_name]'s tip is just in front of her eyes."
                                    the_person "Do it, [man_name]! Cover me! Imagine it's your wife's bitch face, if you want."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shudders and starts spraying his semen over [the_person.possessive_title]'s face."
                                    man_name "Oh, yes! Get it, you bitch! Take that jizz all over your slutty face, [wife_name]!"
                                    "[man_name] clearly liked the idea of giving his wife a facial."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face onto her tits."
                                    the_person "You like that, [man_name]? Seeing a girl on her knees with your sperm all over her face?"
                                    man_name "Fuck yeah! Give me a minute and I'll do it again!"
                                    the_person "We will discuss it later, [man_name]. First - a shower. I need to wash this huge load off before it dries."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You hide in your room and watch them walking away to the bathroom. [the_person.possessive_title] leaves a sticky trail on the floor as the cum drips off her face and tits."
                                    "[man_name]'s hand is on [the_person.title]'s ass, but she does not object. As they close the door, you see [the_person.possessive_title] caresses his balls while his dick shows signs of already returning to life."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                        "You go back to your bedroom, but can still hear screams over the sound of running water in the bathroom."
                                        the_person "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                        man_name "On your knees, slut!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person "Yes! Do it, [man_name]! I want you to fill me."
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "Hammering down desperately into her, [man_name] starts spilling his semen into [the_person.possessive_title]'s pussy."
                                    the_person "Yes, [man_name]! I want it all inside me!"
                                    "After final thrust, [man_name] gets off [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s wet and gaping hole."
                                    the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.fname]. Lying there, full of my cum. I wish my wife would let me cum in her like this."
                                    the_person "I'm glad you like it, [man_name]! Want a better view?"
                                    "[the_person.possessive_title] spreads her legs even further, offering a full view of her cum-drenched pussy."
                                    the_person "Here you go. Remember this sight the next time you fuck your wife."
                                    $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                    the_person "Now I need to take a shower. Maybe we can do it all over again."
                                    $ the_person.draw_person(position = "walking_away")
                                    "You hide behind your bedroom door and watch [the_person.possessive_title] walk towards bathroom, leaving a trail of dripping goo on the floor."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to bed. Soon you again hear screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                        man_name "Take it all in, [the_person.fname]! You're such a perfect breeding whore!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to bed. While drifting to sleep, you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "Wait, [man_name]! I need to taste it!"
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards, and his dick leaves her pussy with a wet sound. [the_person.possessive_title] gets on her knees in front of [man_name]'s cock."
                                    the_person "I want to taste your hot cum. I bet your wife never even goes down on you!"
                                    man_name "[wife_name] never does anything more exciting than missionary. You're so much more exciting!"
                                    the_person "Well, now's your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks up into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.fname]!"
                                    "[the_person.possessive_title] keeps on sucking, bobbing her head at a steady pace."
                                    the_person "Mmmmmm... Mmmm... Uhhh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shudders and starts filling her mouth with his load."
                                    man_name "Oh, yes! Drink it, [wife_name]!"
                                    "[man_name] clearly liked the idea of cumming in his wife's mouth."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out of [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces where it overflowed onto her chin."
                                    the_person "That was great, [man_name]! [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "That was so hot! I'll be ready to do it again soon."
                                    the_person "We will discuss it later, [man_name]. First - a shower. I got sweaty with all of that fucking."
                                    $ the_person.draw_person(position = "walking_away")
                                    "You hide in your room and watch them walking away to bathroom."
                                    "[man_name]'s hand is on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see [the_person.title] caress his balls while his dick shows signs of returning to life." ###bookmark###
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                        man_name "Suck it, bitch, or no sweets for you!"
                                        the_person "Mhhmhmh..."
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[man_name] pulls out his cock, [the_person.possessive_title] grabs it and starts stroking. In a few moments the man begins to cum."
                                    "[the_person.possessive_title] closes the tip with her hand so that no sperm would be split around."
                                    man_name "Ow, fuck! That was great!"
                                    the_person "Indeed, [man_name]! It was great!"
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        the_person "I guess you like it when a girl allows you to be rough, don't you? I like feeling owned by a man while he fucks me."
                                        man_name "Yes, it is a wonderful feeling. I really turns me on. Wish I could do it with my wife..."
                                    man_name "Thanks, [the_person.fname]. I really needed that."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Didn't that event paid off, dear?"
                                    the_person "Now go to the bathroom, [man_name]. I will join you shortly."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Take me again, [man_name]. Bang me with your amazing big thing!"
                                        man_name "Turn around, [the_person.fname]. I want you from behind."
                                        the_person "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                        $ the_person.have_orgasm()
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                        "[the_person.possessive_title] poses next to bed..." if the_person.vagina_available:
                            $ the_person.draw_person(position = "standing_doggy")
                            "You see as [the_person.possessive_title] turns back and poses on her bed spreading her legs, inviting [man_name] to enter her from behind."
                            the_person "All the evening you seemed to be interested in my ass."
                            the_person "How about we do something while you can enjoy the view?"
                            "He quickly drops down his underwear and comes to [the_person.possessive_title], entering her pussy in one go."
                            the_person "Oh yes, [man_name]! Do it! I really needed that."
                            "[man_name] speeds up, pumping [the_person.possessive_title]'s wet vagina while playing with her tits."
                            "[the_person.title]'s hand is working on her clit while she is being railed from behind."
                            the_person "Yes! Do me! I like the way you do it!"
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "Harder! Smash your body up my ass! I want you to be rough with [the_person.fname]. You own me today!"
                                $ the_person.discover_opinion("being submissive")
                            else:
                                pass
                            $ the_person.change_arousal(renpy.random.randint(10,50))
                            "[man_name] caresses [the_person.title]'s ass."
                            man_name "You ass is so great, [the_person.fname]! I wish I could do this more often."
                            the_person "Who knows, [man_name]. If you do good now, then... So come on, nail me with your dick."
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False
                            if not hidden or renpy.random.randint(0,2) == 1:
                                "In a mirror next to the bed [the_person.possessive_title] sees that the door is slightly ajar and you are standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal_perc > 35:
                                    the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                    man_name "Holy cow, [the_person.fname]. You'll let your son watch you being fucked?"
                                    the_person "I don't mind [the_person.mc_title] seeing me like this. Now, come closer, [the_person.mc_title]."
                                    "You lay down on bed in front of [the_person.possessive_title] and take your dick out of your pants."
                                    the_person "Good boy! Now let [the_person.possessive_title] take care of you."
                                    "She starts sucking your penis while [man_name] keeps driving his dick into her soaking vagina."
                                    "[the_person.possessive_title] takes your cock out of her mouth and turns back to [man_name]."
                                    the_person "Oh, [man_name], please go on. Keep fucking me! Your hand feels so good on my ass."
                                    man_name "Sure, [the_person.fname]. You really look lovely from this position."
                                    the_person "Enjoy the view. But don't forget - you must try hard if you want to do this again. So keep going, [man_name]!"
                                    while the_person.arousal_perc < 100:
                                        "[man_name] thrusts his dick into [the_person.possessive_title] pussy. With each move [the_person.possessive_title] moans. Clearly she is having great time."
                                        the_person "Please, [man_name], more. Do me! Do me!"
                                        if the_person.get_opinion_score("being submissive") > 0:
                                            the_person "Slap my ass, [man_name]. Your [the_person.fname] has been a bad girl and needs spanking!"
                                            "[man_name] does as she requests and slaps her buttocks. [the_person.possessive_title] moans while sucking you."
                                        else:
                                            pass
                                        "As she gets more and more turned on, the speed of her lips on your cock also increases."
                                        $ the_person.change_arousal(renpy.random.randint(10,50))
                                    "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                    the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me as fast as you can, [man_name]!"
                                    "He starts to pump [the_person.possessive_title] with some ferocity, his balls slam into her clit. And there is a loud sound as he slaps into her ass."
                                    $ the_person.have_orgasm()
                                    the_person "Yes! Yes! That's it! I love it, [man_name]!"
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        the_person "You own me tonight, Master [man_name]!"
                                    else:
                                        pass
                                    man_name "Shit, [the_person.fname], your pussy is driving me crazy! I think I will come soon!"
                                    $ finish = mom_ntr_select_finish(the_person)
                                    if finish == "facial":
                                        the_person "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                        the_person "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. Sometimes I really hate it! Never had a blowjob from her.."
                                        the_person "Well, that's your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking your cocks with both hands."
                                        man_name "I'm cumming [the_person.fname]!"
                                        "She leans closer so that [man_name] tip is just in front of her eyes."
                                        the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                        $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "It really turns me on! I feel I can do another round shortly."
                                        the_person "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a bath."
                                        "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                            man_name "On your face, slut!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "inside":
                                        the_person "Yes! Do it, [man_name]! I want you to fill me."
                                        $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                        $ the_person.draw_person(position = "standing_doggy")
                                        "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title], while grabbing her ass with both hands."
                                        the_person "Yes, [man_name]! I want it in me!"
                                        "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy down her legs."
                                        the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                        man_name "And you look gorgeous, [the_person.fname], posing there, full of my cum. And with your son cock in hands."
                                        the_person "Glad you like it, [man_name]! Now let's finish with [the_person.mc_title]."
                                        "[the_person.possessive_title] lowers her head, taking your dick back into her mouth."
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        "[the_person.possessive_title] speeds up her lips around your dick and in few seconds you cum in her mouth."
                                        the_person "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a bath."
                                        $ the_person.draw_person(position = "walking_away")
                                        "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                        "While she walks past [man_name], he places his hand on her butt."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                            man_name "Take it all in, [the_person.fname]!"
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person "Hold it, [man_name]! I have a better idea."
                                        $ the_person.draw_person(position = "blowjob")
                                        "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] turns around and gets on her knees in front of [man_name] cock."
                                        the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. Even take her from behind, like I did you."
                                        the_person "Well, that's your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off."
                                        man_name "I'm gonna cum, [the_person.fname]!"
                                        "She just keep on going at steady pace."
                                        the_person "Mmmmmm... Mmmm... Uh."
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shrugs and starts filling her mouth with his load."
                                        man_name "Oh, yes! Get it, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        $ play_swallow_sound()
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                        the_person "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I feel I can do another round shortly."
                                        the_person "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his stuff too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that she takes your cock with her hot lips."
                                        man_name "Never thought you are such cum drinking fan, [the_person.fname]!"
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up mouth around your dick and in few seconds you cum inside. She moves her head back and gulps."
                                        the_person "Here we go. Double sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a bath."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                            man_name "Suck it, bitch, or no sweets for you!"
                                            the_person "Mhhmhmh..."
                                            "Screams go on long into the night..."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        $ the_person.draw_person(position = "standing_doggy")
                                        "[man_name] pulls out his cock and starts stroking it with [the_person.possessive_title]'s buttocks."
                                        "She reaches out and helps him with her hand. And when he starts to cum, she holds her hand over the tip so that he explodes into her hand."
                                        man_name "Ow, fuck! That was great!"
                                        the_person "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let's finish with [the_person.mc_title]."
                                        "[the_person.possessive_title] begin to jerk you off fast. You cannot hold for long an finish in her hand."
                                        the_person "Here we go. All finished!"
                                        man_name "I don't believe it, [the_person.fname]. You just let your son watch us fuck and then sucked him off!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the bed and smiles."
                                        the_person "Didn't that turn you on, [the_person.mc_title]?"
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a bath."
                                        if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                            the_person "Take me again, [man_name]. Bang me with your amazing big thing!"
                                            man_name "Turn around, [the_person.fname]. I want you from behind."
                                            the_person "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                            $ the_person.have_orgasm()
                                            "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "back_peek", emotion = "angry")
                                    the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                    "You go back to your bedroom accompanied by the squeaking sounds from [the_person.possessive_title]'s room as [man_name] keeps pounding her."
                            else:
                                while the_person.arousal_perc < 100:
                                    "[man_name] thrusts his dick into [the_person.possessive_title] pussy. As he slaps her ass, she moans."
                                    the_person "Please, [man_name], more. Do me!"
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        the_person "Fuck me like a dog! I wanna be your bitch tonight. Fuck your whore [the_person.fname]."
                                    else:
                                        pass
                                    "As she gets more and more turned on, her screams get louder and louder."
                                    $ the_person.change_arousal(renpy.random.randint(10,50))
                                "After being fucked by [man_name] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Fuck me as hard as you can, [man_name]!"
                                "He starts to pump [the_person.possessive_title] with some ferocity, fully burying his dick in her. His balls smash against [the_person.title]'s pussy."
                                $ the_person.have_orgasm()
                                the_person "Yes! Yes! That's it! I love this, [man_name]!"
                                man_name "Shit, [the_person.fname], your pussy is driving me crazy! I think I will come soon!"
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    the_person "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. You see [the_person.title]'s juices dripping on the floor. [the_person.possessive_title] gets on her knees in front of [man_name] cock."
                                    the_person "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed. I wish I could fuck her just like I did you."
                                    the_person "Well, that's your chance to try something new, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "I'm cumming [the_person.fname]!"
                                    "She leans closer so that [man_name] tip is just in front of her eyes."
                                    the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                    "[the_person.possessive_title] decides to back up his play."
                                    the_person "Yes, dear. Cover my bitchy face with your cum. I'm sorry that didn't allow that before."
                                    the_person "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                    the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name]. First - a shower. I need to wash off it before it dries."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You see them walking away to bathroom. Some white drops fall on the floor."
                                    "[man_name]'s hand is on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses his balls while his dick shows signs of returning to life."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. Fuck me harder! Shower your whore's face again!"
                                        man_name "On your face, slut!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person "Yes! Do it, [man_name]! I want you to fill me."
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title], grabbing her ass with both hands."
                                    the_person "Yes, [man_name]! I want it in me!"
                                    "After few seconds [man_name] gets off from [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.possessive_title]'s pussy over her legs."
                                    the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.fname] standing there, full of my cum. I wish my wife would allow this."
                                    the_person "Glad you like it, [man_name]! Want a better picture?"
                                    $ the_person.draw_person(position = "doggy")
                                    "[the_person.possessive_title] bends even further, offering a full view of her cum-drenched pussy."
                                    the_person "Here we go. Remember this view next time you fuck your wife."
                                    $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                    the_person "Now I need to take a shower, then you can give me another good pounding."
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] walks towards bathroom, you see several white drops falling on the floor."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. It feels so good to be filled with your semen!"
                                        man_name "Take it all in, [the_person.fname]!"
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] turns around and gets on her knees in front of [man_name] cock."
                                    the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name "No, [wife_name] never allows anything in bed. Even take her from behind, like I did you."
                                    the_person "Well, that's your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.fname]!"
                                    "She just keep on going at steady pace."
                                    the_person "Mmmmmm... Mmmm... Uh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shrugs and starts filling her mouth with his load."
                                    man_name "Oh, yes! Get it, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                    the_person "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "It really turned me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name]!"
                                    the_person "What a sweet load."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to shower. I will join you shortly."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Fuck me again, [man_name]. Take me however you wish. Just let me taste your sweet cum again, I beg you!"
                                        man_name "Suck it, bitch, or no sweets for you!"
                                        the_person "Mhhmhmh..."
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ the_person.draw_person(position = "standing_doggy")
                                    "[man_name] pulls out his cock and starts stroking it with [the_person.possessive_title]'s buttocks."
                                    "She reaches out and helps him with her hand. She quickly covers the tip with her hand when he starts to cum, so that he ejaculates into her hand."
                                    man_name "Ow, fuck! That was great! I really like having a woman from behind."
                                    the_person "Indeed, [man_name]! It was great! Best fuck I had in some time!"
                                    man_name "Thanks, [the_person.fname]. I really needed that."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Didn't that event pay off, dear?"
                                    the_person "Now go take a shower, [man_name]. I will join you shortly."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Take me again, [man_name]. Bang me with your amazing big thing!"
                                        man_name "Turn around, [the_person.fname]. I want you from behind."
                                        the_person "Oh, [man_name]! I'm cumming again. Slap my ass! Harder!"
                                        $ the_person.have_orgasm()
                                        "Screams go on long into the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                        "[the_person.possessive_title] gets on her knees...":
                            $ the_person.draw_person(position = "blowjob")
                            "You see as [the_person.possessive_title] gets on her knees, taking down [man_name]'s underwear."
                            "His erected dick is right in front of [the_person.possessive_title]'s face."
                            the_person "Hello there, sweetie. How about we have some fun together?"
                            $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                            "[the_person.possessive_title] takes his cock in her mouth and starts sucking."
                            "[man_name] paces his hands on her head slightly regulating the speed."
                            man_name "It feels great, [the_person.fname]. I like the way you do it!"
                            $ the_person.change_arousal(renpy.random.randint(10,50))
                            "[the_person.possessive_title] takes [man_name]'s dick out of her mouth, looks at his eyes."
                            the_person "I really like it, [man_name]. It feels great in my mouth."
                            "Then she gets back to suck it."
                            menu:
                                "Keep hiding...":
                                    $ hidden = True
                                "Don't hide...":
                                    $ hidden = False
                            if not hidden or renpy.random.randint(0,2) == 1:
                                "[the_person.possessive_title] turns her head a little and sees that the door is slightly ajar and you are standing there."
                                if the_person.sluttiness >=50 or the_person.get_opinion_score("public sex") > 0 or the_person.arousal_perc > 35:
                                    "[the_person.possessive_title] takes [man_name]'s dick out of her mouth."
                                    the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                    man_name "Shit, [the_person.fname]. Your son sees you sucking a guy off, and you don't mind?"
                                    "[the_person.possessive_title] doesn't bother to answer as she goes back to sucking him."
                                    "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                    "She starts stroking you while [man_name] keeps driving his dick into her mouth."
                                    while the_person.arousal_perc < 100:
                                        "[the_person.possessive_title] keeps sucking his dick. You notice that she is rubbing her clit with her free hand."
                                        man_name "Oh, that's great, [the_person.fname]! You are great at sucking cocks."
                                        if the_person.get_opinion_score("being submissive") > 0:
                                            "[the_person.possessive_title] grabs [man_name]'s ass and impales her mouth on his cock. His ball hit [the_person.possessive_title]'s jaw."
                                            man_name "Ow, that feels so good, [the_person.fname]!"
                                        else:
                                            pass
                                        "As she gets more and more turned on, her moans get louder and louder."
                                        $ arousal_plus = renpy.random.randint (10,50)
                                        $ the_person.change_arousal (arousal_plus)
                                    "[the_person.possessive_title] takes [man_name]'s cock out and looks up."
                                    the_person "Oh. I get so turned on with a cock im my mouth. I'm cumming!"
                                    "She gets back to his dick as her body shivers with orgasm."
                                    man_name "Oh, [the_person.fname], your tongue is driving me crazy! I think I will come soon!"
                                    $ finish = mom_ntr_select_finish(the_person)
                                    if finish == "facial":
                                        "She takes his dick out of her mouth."
                                        the_person "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                        man_name "No, [wife_name] never allows anything in bed. I wish I could make her blow me."
                                        the_person "Well, that's your chance to try something new, [man_name]!"
                                        "She looks into [man_name]'s eyes while jerking him with both hands."
                                        man_name "I'm cumming [the_person.fname]!"
                                        "She leans closer so that [man_name] tip is just in front of her eyes."
                                        the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                        $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                        man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                        "[the_person.possessive_title] decides to back up his play."
                                        the_person "Yes, dear. Cover my bitchy face with your cum. I'm sorry that didn't allow that before."
                                        the_person "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                        man_name "It really turns me on! I feel I can do another round shortly."
                                        the_person "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                        the_person "Here we go. All finished!"
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a shower."
                                        "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                            the_person "Mrmh... Blgrhm..."
                                            man_name "That's it, [wife_name]. My bitch want a shower?"
                                            the_person "Oh, yes, Master! Cover my face with your blessing!"
                                            "Seems [man_name] liked the idea of roleplaying with face-fucking [the_person.possessive_title]. She doesn't seem to object."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "drink":
                                        the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                        man_name "No, [wife_name] never blows me. It pisses me off, now that I know how good it is."
                                        the_person "Well, that's your chance to try something new, [man_name]!"
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "She looks into [man_name]'s eyes while sucking him off. Her hand keeps jerking you in meantime."
                                        man_name "I'm gonna cum, [the_person.fname]!"
                                        "She just keep on going at steady pace."
                                        the_person "Mmmmmm... Mmmm... Uh."
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "[man_name] shrugs and starts filling her mouth with his load."
                                        man_name "Oh, yes! Get it, [wife_name]!"
                                        "[man_name] clearly liked the idea of doing it with his wife."
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        $ play_swallow_sound()
                                        "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                        the_person "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                        man_name "It really turned me on! I feel I can do another round shortly."
                                        the_person "We will discuss it later, [man_name]! Now let's finish with [the_person.mc_title]. I want to drink his stuff too."
                                        $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                        "With that she takes your cock with her hot lips."
                                        man_name "Never thought you are such cum drinking fan, [the_person.fname]!"
                                        $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up mouth around your dick and in few seconds you cum inside. She moves her head back and gulps."
                                        the_person "Here we go. Double sweet load."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a bath."
                                        if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                            "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                            the_person "Mrmh... Blgrhm..."
                                            man_name "That's it, [wife_name]. Take it into your slutty mouth! Like the taste. whore?"
                                            "Seems [man_name] liked the idea of roleplaying with feeding [the_person.possessive_title]. She doesn't seem to object."
                                        else:
                                            "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                    elif finish == "usual":
                                        "[the_person.possessive_title] take his penis out of her mouth and looks up at him."
                                        the_person "Yes! Please cum on my breast. They are easier to clean than my furniture."
                                        man_name "As you wish!"
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[man_name] starts grinning as he ejaculates onto [the_person.possessive_title]'s large boobs."
                                        man_name "Ow, fuck! That was great!"
                                        "[the_person.possessive_title] looks up at him and smiles."
                                        the_person "Indeed, [man_name]! Now let's finish with [the_person.mc_title]."
                                        $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                        $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                        "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you also cum on [the_person.title]'s tits."
                                        $ the_person.draw_person(position = "stand2", emotion = "happy")
                                        "[the_person.possessive_title] stands up from the floor and smiles."
                                        the_person "Now go to your room, [the_person.mc_title]. [man_name] and I need to take a shower."
                                        "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                                else:
                                    $ the_person.happiness -= 5
                                    $ the_person.draw_person(position = "blowjob", emotion = "angry")
                                    the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get back to your room now!"
                                    "You go back to your bedroom accompanied by slobbering sounds from [the_person.possessive_title]'s room as she keeps sucking [man_name]'s dick."
                            else:
                                while the_person.arousal_perc < 100:
                                    "[the_person.possessive_title] keeps sucking his dick. You notice that she is rubbing her clit with a free hand."
                                    man_name "Oh, that's great, [the_person.fname]! Your mouth is so sweet and nice."
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        "[the_person.possessive_title] grabs [man_name]'s ass and impales her mouth on his cock. His ball hit [the_person.possessive_title]'s jaw."
                                        man_name "Ow, that feels so good, [the_person.fname]!"
                                    else:
                                        pass
                                    "As she gets more and more turned on, her moans get louder and louder."
                                    $ the_person.change_arousal(renpy.random.randint(10,50))
                                "[the_person.possessive_title] takes [man_name]'s cock out and looks up."
                                the_person "Oh. I get so turned on with a cock im my mouth. I'm cumming!"
                                "She gets back to his dick as her body shivers with orgasm."
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    "She takes his dick out of her mouth."
                                    the_person "Would you like to cover my face with your hot cum? I doubt that your wife allows you to do this!"
                                    man_name "No, [wife_name] never do anything like that. I wish I could make her blow me."
                                    the_person "Well, that's your chance to try something new, [man_name]!"
                                    "She looks into [man_name]'s eyes while jerking him with both hands."
                                    man_name "I'm cumming [the_person.fname]!"
                                    "She leans closer so that [man_name] tip is just in front of her eyes."
                                    the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name]!"
                                    "[the_person.possessive_title] decides to back up his play."
                                    the_person "Yes, dear. Cover my bitchy face with your cum. I'm sorry I didn't let you before."
                                    the_person "Cover your dearest [wife_name]'s face with semen. I really want it!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "His load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                    the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name]! Now I need a shower."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now we need to take a bath."
                                    "As you turn to leave, you see [man_name]'s balls being caressed by [the_person.possessive_title] and his thing starting to rise."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                        the_person "Mrmh... Blgrhm..."
                                        man_name "That's it, [wife_name]. You look great with this."
                                        "Seems [man_name] liked the idea of roleplaying with cumming on [the_person.possessive_title]. She doesn't seem to object."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name "No, [wife_name] never blows me. It pisses me off, now that I know how good it is."
                                    the_person "Well, that's your chance to try something new, [man_name]!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name]'s eyes while sucking him off."
                                    man_name "I'm gonna cum, [the_person.fname]!"
                                    "She just keep on going at steady pace."
                                    the_person "Mmmmmm... Mmmm... Uh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name] shrugs and starts filling her mouth with his load."
                                    man_name "Oh, yes! Get it, [wife_name]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                    the_person "Liked that, [man_name]? [wife_name] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name "It really turned me on! I feel I can do another round shortly."
                                    the_person "What a sweet load. As for another round, we will see..."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to shower. I will join you shortly."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 60:
                                        "You go back to your bedroom accompanied by incomprehensive loud blabbering from [the_person.possessive_title]'s room."
                                        the_person "Mrmh... Blgrhm..."
                                        man_name "That's it, [wife_name]. A proper wife should like her man taste!"
                                        "Seems [man_name] liked the idea of roleplaying with feeding [the_person.possessive_title]. She doesn't seem to object."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    "[the_person.possessive_title] take his penis out of her mouth and looks up at him."
                                    the_person "Yes! Please cum on my breasts. They are easier to clean than the furniture."
                                    man_name "As you wish!"
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name] starts grinning as he ejaculates to [the_person.possessive_title]'s large boobs."
                                    man_name "Ow, fuck! That was great!"
                                    "[the_person.possessive_title] looks up at him and smiles."
                                    the_person "Indeed, [man_name]! You did great!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "I really like the taste of big john, [man_name]."
                                    the_person "Now go to the bathroom, I will join shortly."
                                    "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
            "Get back to bed":
                "You decide that it is wrong to spy on [the_person.possessive_title]'s private life, so you go back to your room to sleep."
    elif ran_num == 2: ##For a scene with 2 men
        $ man_name2 = Person.get_random_male_name()
        while man_name == man_name2: ## Just to make sure that names don't match or it will look stupid
            $ man_name2 = Person.get_random_male_name()
        $ wife_name2 = Person.get_random_name()
        while wife_name2 == the_person.name or wife_name == wife_name2: ## Just to avoid stupid duplications
            $ wife_name2 = Person.get_random_name()
        ## let's create wives names here, just not to insert that in every scene it is required
        if the_person.get_opinion_score("giving blowjobs") > 0:
            $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
            "You take a look inside the room and your eyes widen. You see two men sitting on a bed with their cocks out of their pants."
            "[the_person.possessive_title] is on her knees in front of them, sucking one cock and jerking the other."
            "By the look on men's faces you can tell that them are also quite surprised. One of them is clearly not very comfortable with the situation."
            $ the_person.draw_person(position = "blowjob", emotion="happy")
            "[the_person.possessive_title] notices that. She stops sucking the other man and looks to the confused one with a broad smile."
            the_person "Oh, relax, [man_name]. The event was great, you men were so nice. Why not let the fun continue?"
            man_name "Well, you have a point there. [man_name2], did you expect that when we agreed to drive [the_person.fname] home, she will thank us this way?"
            man_name2 "I could only dream of [the_person.fname] sucking my boy. We worked together for so many years and now..."
            $ the_person.discover_opinion("giving blowjobs")
            the_person "And for all those years, [man_name2], you never knew how I dreamed of your cock in my mouth. I just like sucking men off so much..."
            man_name "Wow. I had no idea that you are cock-sucking slut, [the_person.fname]. Dreamed of my cock too?"
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "[the_person.possessive_title] just smiles then gets up, embraces and kisses [man_name] passionately."
            "It seems that [the_person.title] is having fun with her colleagues, [man_name] and [man_name2]."
            "You are unsure what to do here."
        else:
            $ the_person.draw_person(position = "kissing", emotion = "happy")
            "You see [the_person.possessive_title] embracing two men, kissing them deeply."
            the_person "Oh guys, you are so nice. I had a wonderful evening! Thanks for driving me home, [man_name]."
            man_name "Not a problem, [the_person.fname]. I'm glad that [man_name2] joined us."
            man_name2 "I live in this district too, so you actually did me a favor as well."
            "As you open the door a little more, you recognize them . It's [man_name] and [man_name2], [the_person.possessive_title] colleagues."
            "You are unsure what to do here."
        menu:
            "Keep looking":
                "You decide to see what they are up to."
                "They go on kissing. After a while [man_name] places his hands on [the_person.possessive_title]'s ass, slightly caressing it, while [man_name2] is fondling her tits."
                the_person "Oh, [man_name]. You clearly have some plans for tonight, don't you?"
                if the_person.get_opinion_score("giving blowjobs") > 0:
                    "She strokes their cocks a little."
                else:
                    "She caresses their crotches."
                the_person "I like that plan, as well as your little friends there. How about we get more comfortable by getting rid of those clothes?"
                $ mom_clothing = the_person.choose_strip_clothing_item()
                if not mom_clothing is None:
                    $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                    man_name "That's a nice [mom_clothing.name] you have, [the_person.fname]. I wonder how you will look without it."
                    "He takes off [the_person.possessive_title]'s [mom_clothing.name] and throws it on a nearby chair."
                if clothes_number >1:
                    $ mom_clothing = the_person.choose_strip_clothing_item()
                    if not mom_clothing is None:
                        the_person "I like the touch of your soft hands, [man_name]."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        man_name2 "Let me help you too. Your [mom_clothing.name] need to go off, don't you agree?"
                if clothes_number >2:
                    $ mom_clothing = the_person.choose_strip_clothing_item()
                    if not mom_clothing is None:
                        the_person "Ooooh, [man_name2], you are really turning me on with your touches."
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        if the_person.vagina_available:
                            "[man_name] takes off her [mom_clothing.name], while [man_name2] plays with her open pussy."
                        else:
                            "[man_name] takes off her [mom_clothing.name], while [man_name2] and [the_person.possessive_title] kiss passionately."
                if clothes_number >3:
                    $ mom_clothing = the_person.choose_strip_clothing_item()
                    if not mom_clothing is None:
                        the_person "I don't mind go even more naked, guys. Who would like to take my [mom_clothing.name] off?"
                        $ the_person.draw_animated_removal (mom_clothing, position = "kissing")
                        if the_person.vagina_available:
                            "[man_name2] grants her wish, while [man_name] fingers her open pussy."
                        else:
                            "[man_name2] grants her wish, while [the_person.possessive_title] caresses [man_name2]'s crotch."
                $ mom_clothing = None
                $ the_person.change_slut(2, 40)
                "Now with all of them pretty naked, you clearly see where it will go."
                the_person "Oh, guys, I feel so horny around you. Let's have some fun!"
                menu:
                    "[the_person.title] lays on the table..." if the_person.vagina_available:
                        $ the_person.draw_person(position = "missionary", emotion = "happy")
                        "You see as [the_person.possessive_title] lays on her table and spreads her legs, smiling broadly."
                        the_person "Alright, who's wanna be the first to bang your colleague?"
                        man_name "I've been in the company longer than any of you, so it would only be fair that I go first."
                        "He comes up to the table, kneels in front of it and starts licking [the_person.possessive_title]'s pussy."
                        $ the_person.change_arousal(renpy.random.randint(10,50))
                        the_person "Oh yes, [man_name]! It feels so great."
                        "[man_name] kisses her clit than stands up."
                        man_name "One big dick for [the_person.fname] coming right up!"
                        "In one powerful move he enters [the_person.possessive_title]. She rolls her eyes and moans."
                        the_person "Ahhh, fuck! That feels so good, [man_name]!"
                        "[man_name2] comes up to the table, stroking his dick."
                        man_name2 "How about you take care of me as well while I wait for my turn?"
                        the_person "Sure, [man_name2]. How about some helping hand?"
                        "She grabs his cock and starts stroking him while being pumped by [man_name]."
                        while the_person.arousal_perc < 60:
                            "[man_name] moves his dick in [the_person.possessive_title] pussy. It goes in and out with a wet sound. Clearly [the_person.title] is having great time."
                            the_person "Please, [man_name], more. Bang me like you always wanted!"
                            if the_person.get_opinion_score("being submissive") > 0:
                                the_person "Harder. I want a rough fuck! Nail me more!"
                            "As she gets more and more turned on, the speed of her hand on [man_name2]'s cock also increases."
                            $ the_person.change_arousal(renpy.random.randint(10,50))
                        the_person "Oh, [man_name], you are so great, but I want to feel [man_name2] inside too!"
                        man_name "Oh, [the_person.fname]... I hope you will take care of me in a meantime."
                        "[man_name] takes his cock out off her. You see [the_person.possessive_title]'s juices flowing out of her. She is clearly enjoying this."
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if not hidden or renpy.random.randint(0,2) == 1:
                            "While the men are changing positions, [the_person.possessive_title] turns her head and sees that the door is slightly ajar and you are standing there."
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                man_name "Wow, [the_person.fname]! Having two men at once, and now letting your son see it..."
                                the_person "My house, my rules. So, come on closer. I will help you let it go."
                                "You and [man_name] come to the table from both sides and [the_person.possessive_title] starts stroking your dicks."
                                "[man_name2] clearly has no objections of you joining the show as he puts his rock-hard cock into woman wet pussy."
                                the_person "Yes! It is so good!"
                                while the_person.arousal_perc < 100:
                                    "[man_name2] keeps doing [the_person.possessive_title]. His hip are smashing into [the_person.possessive_title]'s."
                                    the_person "Yes, [man_name2]! Fuck me more. I feel so good now."
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        the_person "Rougher! Do me harder! Fuck my brains out, I beg you!"
                                    else:
                                        pass
                                    "As she gets more and more turned on, she strokes your dicks faster and faster."
                                    $ the_person.change_arousal(renpy.random.randint(10,50))
                                "After being fucked by [man_name2] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Do me more, [man_name2]!"
                                "He starts to pump [the_person.possessive_title] real fast, his balls are smashing against [the_person.title]'s ass."
                                $ the_person.have_orgasm()
                                $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                                the_person "Yes! Yes! That's it! I love you guys!"
                                man_name2 "Shit, [the_person.fname], your pussy is driving me crazy! I think I will come soon!"
                                man_name "Same here, man."
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    the_person "Hold it, guys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes [man_name2] backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                    the_person "[man_name], [the_person.mc_title], come here!"
                                    "Both of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name "No, [wife_name] would never suggest anything like that..."
                                    man_name2 "I once proposed this to [wife_name2]. She called me a pervert who is watching too much porn."
                                    the_person "Well, now you can try the stuff from those movies yourselves!"
                                    "She looks into [man_name2]'s eyes while jerking your and [man_name]'s cocks with both hands. [man_name2] is jerking his member pointing into [the_person.title]'s face."
                                    man_name2 "I'm cumming [the_person.fname]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person "Do it, [man_name2]! Cover me! Imagine that's your wife, if you like."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    the_person "Liked that, [man_name2]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name2 "It really turns me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name]! Now let's finish with others."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around [man_name] dick and in few seconds he cums on her tits."
                                    the_person "Two out, one to go!"
                                    $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is show enough and you start to ejaculate. You finish on [the_person.title]'s tits and there is so much of jizz so it starts falling on her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the boys need to take a bath."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... More, please, do me more!"
                                        man_name2 "Now I want to take this bitch from behind. Get on all fours, [the_person.fname]."
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and men's laughter from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person "Yes! Do it, [man_name2]! I want you to fill me."
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "After a few hard thrusts, [man_name2] starts spilling his semen into [the_person.possessive_title]."
                                    the_person "Yes, [man_name2]! I want it in me!"
                                    "After few seconds [man_name2] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                    the_person "Wow, [man_name2]! You really needed to blow off some steam! That was a huge load."
                                    man_name2 "And you look gorgeous, [the_person.fname] lying there, full of my cum. And with two cocks in hands."
                                    the_person "Glad you like it, [man_name2]! Now [man_name], fill me up!"
                                    "[man_name] comes to [the_person.possessive_title]'s vagina and starts doing her again. As he is well aroused, after a few frictions he grins."
                                    the_person "Cum in me! Give it all to me!"
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "After a few final trusts, [man_name] pulls out. You see even more sperm flowing out."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                    the_person "Here we go. All finished!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the guys need to take a shower."
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                    "While she walks past [man_name], he places his hand on her butt."
                                    the_person "First - the shower. Then we will see, dear."
                                    man_name2 "Wait for me!"
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Fill me with cum!"
                                        man_name2 "Oh, [the_person.fname], I'm gonna fill you so much that it will come from your ears!"
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and the squeaking bed from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "Hold it, [man_name]! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                    the_person "[man_name], [the_person.mc_title], come here!"
                                    "Both of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                    man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                    the_person "Well, that's your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.fname]!"
                                    "She just keep on going at steady pace."
                                    the_person "Mmmmmm... Mmmm... Uh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you are such cum drinking fan, [the_person.fname]!"
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps."
                                    the_person "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] take you dick in her mouth and in a short time you also explode inside."
                                    "She retreats back and gulps."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the guys need to take a bath."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Let me drink your cum!"
                                        man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[man_name2] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                    man_name2 "Ow, fuck! That was great!"
                                    the_person "Indeed, [man_name2]! It was great! Best fuck I had in some time! Now let's finish with others."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "missionary", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around your dicks and in few seconds you both cum on her tits."
                                    the_person "Here we go. All finished!"
                                    man_name "I don't believe it, [the_person.fname]. You just let your son watch us fuck and then jerked him off!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Didn't that turn you on, [the_person.mc_title]?"
                                    the_person "Now go to your room, [the_person.mc_title]. Me and colleagues need to take a shower."
                                    "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                $ the_person.draw_person(position = "missionary", emotion = "angry")
                                the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by squeaking sound from [the_person.possessive_title]'s room as both men keep pounding her."
                        else:
                            while the_person.arousal_perc < 100:
                                "[man_name2] puts his dick into [the_person.possessive_title] pussy. By the look on [the_person.title]'s face she is clearly having great time."
                                "While being pumped by [man_name2], she grabs [man_name] cock and strokes him."
                                the_person "Please, [man_name2], more. Fuck me! Fuck your [the_person.fname]!"
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "Harder! Slam your dick in me, [man_name2]. I love being fucked roughly!"
                                "As she gets more and more turned on, her screams get louder and louder."
                                $ the_person.change_arousal(renpy.random.randint(10,50))
                            "After being fucked by [man_name2] for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                            the_person "Oh, God! I'm cumming! Fuck me! Keep doing this, [man_name2]!"
                            "He starts to pump [the_person.possessive_title] faster and faster, fully burying his dick in her."
                            $ the_person.draw_person(position = "missionary", emotion = "orgasm")
                            $ the_person.have_orgasm()
                            the_person "Yes! Yes! That's it! You made me cum, [man_name2]!"
                            man_name2 "Shit, [the_person.fname], your pussy is driving me crazy! I think I will come soon!"
                            man_name "Me too!"
                            $ finish = mom_ntr_select_finish(the_person)
                            if finish == "facial":
                                the_person "Hold it, guys! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes [man_name2] backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                the_person "Come here, [man_name]."
                                "He comes over. Now [the_person.possessive_title] is sitting on the floor with two dicks up to her face."
                                the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a pervert and didn't speak to me for a week!"
                                the_person "Well, that's your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.fname]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to bathroom. Some white drops fall on the floor."
                                "Both men hands are on [the_person.title]'s ass, but she does not object. As they close the door, you see that [the_person.possessive_title] caresses their balls while dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... More, please, do me more!"
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their fuck doll."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans and squeaking sounds from [the_person.possessive_title]'s room."
                            elif finish == "inside":
                                the_person "Yes! Do it, [man_name2]! I want you to fill me."
                                $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "After a few hard thrusts, [man_name2] starts spilling his semen into [the_person.possessive_title]."
                                the_person "Yes, [man_name2]! I want it in me!"
                                "After few seconds [man_name2] gets off [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                the_person "Wow, [man_name2]! You really needed to blow off steam! That was a huge load."
                                man_name "And you look gorgeous, [the_person.fname] lying there, full of my cum. I wish my wife would allow this."
                                the_person "Glad you like it, [man_name2]! Want a better picture?"
                                "[the_person.possessive_title] spreads her legs even further, offering a full view of her cum-drenched pussy."
                                the_person "Here we go. Remember this view next time you fuck your wife. Now [man_name], come here and fill me as well!"
                                "He comes over, enters [the_person.possessive_title] pussy and after a few moves starts to grin."
                                $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                the_person "Yes! Inside. Fill me!"
                                "After [man_name] finishes, he pulls out. [the_person.possessive_title] is laying on the table with white liquid flowing out of her."
                                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and heads towards bathroom. [man_name] slaps her ass."
                                the_person "Now I first need to take a shower, then we will see who can make me cum again."
                                $ the_person.draw_person(position = "walking_away")
                                "As [the_person.possessive_title] walks towards the bathroom, you see several white drops falling on the floor."
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Cum in me! I want to be filled."
                                    man_name2 "Spread wide and receive my load as well!"
                                    "It seems both men just found the perfect place to deposit their loads, as they seem to do [the_person.possessive_title] all night long."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person "Hold it, [man_name2]! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes him backwards. With a wet sound his dick leaves her pussy. [the_person.possessive_title] gets on her knees in front of [man_name2] cock."
                                the_person "Come here, [man_name]."
                                "He comes over. Now [the_person.possessive_title] is sitting on the floor with two dicks up to her face."
                                the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] hates oral sex. It is so frustrating."
                                man_name "I once asked [wife_name] for a blowjob. She said if I ever ask this again she will file a divorce!"
                                the_person "Well, that's your chance to experience the feeling, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off."
                                man_name2 "I'm gonna cum, [the_person.fname]!"
                                "She just keep on going at steady pace."
                                the_person "Mmmmmm... Mmmm... Uh."
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                $ play_swallow_sound()
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, [man_name2]. First - I need to taste [man_name]."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She puts another dick into her mouth and sucks it off."
                                man_name "This is so great. I can't hold much longer!"
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                $ play_swallow_sound()
                                "[man_name] comes into [the_person.possessive_title]'s mouth and pulls his cock away. She shows it to them, closes her mouth, smiles and swallows it."
                                $ the_person.draw_person(position = "walking_away")
                                "You see them walking away to the bathroom."
                                "[man_name]'s hand is on [the_person.title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter bathroom, the men's dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Do me again, [man_name]. Fuck me harder! Harder! Ahhh... Give it to me! I want to drink it all!"
                                    man_name2 "Like the taste, bitch? Aren't you a cum-gulping whore, [the_person.fname]?"
                                    "It seems [the_person.possessive_title]'s mouth gonna keep them awake for a while..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "[man_name2] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                man_name2 "Ow, fuck! That was great!"
                                the_person "Indeed, [man_name2]! It was great!"
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "I guess you like it when a girl allows you to be rough, don't you? I like feeling owned by a man while he fucks me."
                                    man_name2 "Yes, it is a wonderful feeling. It really turns me on. Wish I could do this with my wife..."
                                man_name2 "Thanks, [the_person.fname]. I really needed that."
                                man_name "I'm cumming too!"
                                $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "missionary", emotion = "happy")
                                "After being stroked for so long, he finally cums on [the_person.possessive_title]'s tits."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person "Didn't that event paid off, dear?"
                                the_person "Now go to the bathroom, guys. I will join you shortly."
                                "You go back to your bedroom accompanied by shower sounds from [the_person.possessive_title]'s room."
                    "[the_person.title] shows on the bed..." if the_person.vagina_available and (the_person.sluttiness > 70 or the_person.get_opinion_score("anal sex") > 0):
                        the_person "Alright, I have an idea of how we all can have fun. Please, [man_name], lie on the bed."
                        "The man does so. From where you stand you can see how hard he is."
                        $ the_person.draw_person(position = "doggy")
                        "[the_person.possessive_title] gets over him and puts his cock inside."
                        the_person "Oh, you have a wonderful thing here, [man_name]. Now, [man_name2], how about you stick your instrument in my ass? There is some lubricant in mddle drawer."
                        man_name2 "Shit, [the_person.fname]... I could only dream of anal. And you butt is so sweet."
                        "He comes up to the table, takes a tube of lubricant, pours some on his dick, then fingers [the_person.possessive_title]'s ass with it."
                        the_person "Thanks, [man_name2]. I'm ready. Put it in me."
                        $ the_person.change_arousal(renpy.random.randint(5,20))
                        "[man_name2] comes from behind and starts to slowly push against [the_person.possessive_title]'s ass."
                        the_person "Keep going, [man_name2]. It feels so pleasant."
                        "The man is now fully inside [the_person.possessive_title]'s ass."
                        the_person "Ahhh, fuck! That feels so good, guys!"
                        "Men start to slowly move. [the_person.possessive_title] kiss [man_name] with a passion, while [man_name2] is caressing her buttocks."
                        the_person "Ohh, guys! You make me feel so good!"
                        if the_person.get_opinion_score("being submissive") > 0:
                            the_person "Harder! Nail me with your cocks. I want you to be rough with your [the_person.fname]. I'm your fuck toy today!"
                            $ the_person.discover_opinion("being submissive")
                        else:
                            pass
                        "You just can't believe your eyes - [the_person.possessive_title] gets screwed by two men at once!"
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if not hidden or renpy.random.randint(0,2) == 1:
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                "[the_person.possessive_title] raises her head and looks into the mirror next to her bed, she sees you standing there, looking at her, through the slightly opened door."
                                the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                man_name2 "Wow, [the_person.fname]! Two of us not enough for you?"
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "I want two of you to fuck me real hard so that I would scream like mad. I don't want to wake [lily.fname] so I need something to shut my mouth."
                                    man_name "Wanna a rough fuck, [the_person.fname]? Can do!"
                                else:
                                    the_person "My house, my rules. So, come on [the_person.mc_title]. I will help you relax."
                                "You stand on the bed in front of [the_person.possessive_title] and she starts sucking your dick."
                                "The guys go on doing [the_person.possessive_title]'s two holes at once."
                                the_person "Mhhhh... Ohmmmm..."
                                while the_person.arousal_perc < 100:
                                    "[man_name2] and [man_name] keep fucking [the_person.possessive_title] two ways."
                                    the_person "Mhmhmmmmh..."
                                    "Your cock in [the_person.possessive_title]'s mouth prevents her from saying anything, she can only moan. On her face you see a mixture of pain and pleasure."
                                    if the_person.get_opinion_score("being submissive") > 0:
                                        "She pulls her head away from you."
                                        the_person "Oh God! Fuck me! Fuck! Fuck!"
                                        "Afraid that she would wake up [lily.fname], you grab her head and impale her wide open mouth on your dick."
                                        "It seems to turn her on even more."
                                    else:
                                        pass
                                    "As she gets more and more turned on, she sucks your dick faster and faster."
                                    $ the_person.change_arousal(renpy.random.randint(10,50))
                                "After being fucked by three of you for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                                the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Fill my holes!"
                                "Both men start to pump [the_person.possessive_title] real fast, their bodies slamming into her."
                                the_person "Aaaaaahhh...! Fuuuuuuck! Cumming!"
                                $ the_person.have_orgasm()
                                "Both men don't stop there, they keep on going. [the_person.possessive_title] seems to have reached multiple orgasms."
                                the_person "Yeah! More! Harder! Fuck me! Screw me! Rip me apart!"
                                man_name2 "Shit, [the_person.fname], your ass is so tight! I think I will come soon!"
                                man_name "Same here, man."
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    the_person "Hold it, giys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes away from man's crouches. With a wet sound their dicks leaves her holes. [the_person.possessive_title] gets on her knees on the bed."
                                    the_person "[man_name], [man_name2], [the_person.mc_title], come here!"
                                    "Three of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name "No, [wife_name] would never suggest anything like that..."
                                    man_name2 "I once proposed this to [wife_name2]. She called me a pervert who is watching too much porn."
                                    the_person "Well, now you can try the stuff from those movies yourselves!"
                                    "She looks into [man_name2]'s eyes while jerking your and [man_name]'s cocks with both hands. [man_name2] is jerking his member pointing into [the_person.title]'s face."
                                    man_name2 "I'm cumming [the_person.fname]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person "Do it, [man_name2]! Cover me! Imagine that's your wife, if you like."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    the_person "Liked that, [man_name2]? Seeing a girl on her knees with your sperm over her face?"
                                    man_name "It really turns me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name]! Now let's finish with others."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up her hand around [man_name] dick and in few seconds he cums on her tits."
                                    the_person "Two out, one to go!"
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is show enough and you start to ejaculate. You finish on [the_person.title]'s tits and there is so much of jizz so it starts falling on her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the boys need to take a bath."
                                    if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, [man_name]. Take my ass!"
                                        man_name "We are out of lubricant, so suck me for a while,[the_person.fname]."
                                        the_person "Sure, come here. Ahhh, [man_name2], keep doing me! I like it from behind."
                                        "It seems that men are planning to fuck [the_person.possessive_title] all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and men's laughter from [the_person.possessive_title]'s room."
                                elif finish == "inside":
                                    the_person "Yes! Do it, [man_name]! I want you to fill me."
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "doggy")
                                    "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                    the_person "Yes, [man_name]! I want it in me!"
                                    "After few seconds [man_name] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                    the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                    man_name "And you look gorgeous, [the_person.fname] lying there, full of my cum, being nailed in the ass."
                                    the_person "Glad you like it, [man_name]! Now [man_name2], fill me up!"
                                    "[man_name2] takes his cock from her ass and puts it into [the_person.possessive_title]'s vagina and starts doing her. As he is well aroused, after a few frictions he grins."
                                    the_person "Cum in me! Give it all to me!"
                                    $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                    $ the_person.draw_person(position = "doggy")
                                    "After a few final trusts, [man_name2] pulls out. You see even more sperm flowing out."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    "[the_person.possessive_title] speeds up her hand around your dick and in few seconds you cum on her tits."
                                    the_person "Here we go. All finished!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and guys need to take a shower."
                                    $ the_person.draw_person(position = "walking_away")
                                    "As [the_person.possessive_title] starts walking towards bathroom, you see several white drops falling on the floor."
                                    "While she walks past [man_name], he places his hand on her butt."
                                    the_person "First - the shower. Then we will see, dear."
                                    man_name2 "Wait for me!"
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Do me again, guys. Fuck me more! Ahhh... Fill me with cum!"
                                        man_name2 "Oh, [the_person.fname], now we will fill both your holes!"
                                        "It seems that men are planning to fuck [the_person.possessive_title]'s holes all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and squeaking sounds from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "Hold it, guys! I have a better idea."
                                    $ the_person.draw_person(position = "blowjob")
                                    "She pushes away from them. With a wet sound their dicks leaves her pussy and anus. [the_person.possessive_title] gets on her knees on the bed."
                                    the_person "[man_name], [man_name2], [the_person.mc_title], come here!"
                                    "Three of you come closer. Now [the_person.possessive_title] is on her knees with three erected dicks in front of her."
                                    the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                    man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                    the_person "Well, that's your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.fname]!"
                                    "She just keep on going at steady pace."
                                    the_person "Mmmmmm... Mmmm... Uh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you are such cum drinking fan, [the_person.fname]!"
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She quickly swallows the load."
                                    the_person "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something. I wish [wife_name] could do the same!"
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] takes your dick in her mouth and in a short time you also deposit your load."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the guys need to take a bath."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Take me again, guys. Fuck me however you want! My ass and pussy are all yours! Just let me drink your semen!"
                                        man_name2 "Open up your mouth, slut!  You gonna be fed with some hot stuff!"
                                        man_name "Can you take two loads at once, [the_person.fname]?"
                                        "It seems that men are planning to use [the_person.possessive_title] as cum dump all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                    "[man_name] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                    man_name "Ow, fuck! That was great!"
                                    the_person "Indeed, [man_name]! It was great! Best fuck I had in some time! Now let's finish with others."
                                    $ cum_on_ass_ntr(the_person) #$ the_person.cum_on_ass()
                                    $ the_person.draw_person(position = "doggy")
                                    "[man_name2] grabs her butt and speeds up. In few seconds he cums on her ass."
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    "Aroused by the view you cum on [the_person.possessive_title]'s tits."
                                    the_person "Here we go. All finished!"
                                    man_name "I don't believe it, [the_person.fname]. You just let your son watch us fuck you two ways and then sucked him off!"
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Didn't that turn you on, [the_person.mc_title]?"
                                    the_person "Now go to your room, [the_person.mc_title]. Me and my colleagues need to take a shower."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Please, take me again, boys. I really liked it when you stuffed me together!"
                                        man_name2 "You are sex hungry slut, [the_person.fname]."
                                        man_name "Let me take your ass this time."
                                        "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by squeaking sounds from [the_person.possessive_title]'s room as men keep doing her."
                        else:
                            "The guys go on doing [the_person.possessive_title]'s two holes at once."
                            the_person "Ow, it is so good! More!"
                            while the_person.arousal_perc < 100:
                                "[man_name2] and [man_name] keep fucking [the_person.possessive_title] two ways."
                                the_person "More, please. Fuck me more!"
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "Harder! Rip me apart! Take me roughly!"
                                else:
                                    pass
                                "As she gets more and more turned on, her screams get louder and louder."
                                $ the_person.change_arousal(renpy.random.randint(10,50))
                            "After being fucked by two men at once for quite some time, [the_person.possessive_title] seems to be closing to orgasm."
                            the_person "Oh, God! I'm cumming! Fuck me! Fuck me more! Fill my holes!"
                            "Men start to pump [the_person.possessive_title] real fast, their bodies slamming into her."
                            $ the_person.have_orgasm()
                            the_person "Aaaaaahhh...! Fuuuuuuck! Cumming!"
                            "Guys do not stop there, they keep on going. [the_person.possessive_title] seems to have reached multiple orgasms."
                            the_person "Yeah! More! More! Fuck me! Do me!"
                            man_name2 "Shit, [the_person.fname], your ass is so tight! I think I will come soon!"
                            man_name "Same here, man."
                            $ finish = mom_ntr_select_finish(the_person)
                            if finish == "facial":
                                the_person "Hold it, guys! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes them backwards. [the_person.possessive_title] gets on her knees on the bed. Men come up to her, stroking their cocks."
                                the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a pervert and didn't speak to me for a week!"
                                the_person "Well, that's your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.fname]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to the bathroom. Some white drops fall on the floor."
                                "Both men hands are on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Do me again, [man_name]. Fuck me any way you want! Harder! And spray it all over me!"
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their fuck doll."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans and squeaks from [the_person.possessive_title]'s room."
                            elif finish == "inside":
                                the_person "Yes! Do it, [man_name]! I want you to fill me."
                                $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "doggy")
                                "After a few hard thrusts, [man_name] starts spilling his semen into [the_person.possessive_title]."
                                the_person "Yes, [man_name]! I want it in me!"
                                "After few seconds [man_name] gets away [the_person.possessive_title]. You see a trace of his white liquid dripping from [the_person.title]'s pussy."
                                the_person "Wow, [man_name]! You really needed to blow off some steam! That was a huge load."
                                man_name "And you look gorgeous, [the_person.fname] lying there, full of my cum, being nailed in the ass."
                                the_person "Glad you like it, [man_name]! Now [man_name2], fill me up!"
                                "[man_name2] takes his cock from her ass and puts it into [the_person.possessive_title]'s vagina and starts doing her. As he is well aroused, after a few frictions he grins."
                                the_person "Cum in me! Give it all to me!"
                                $ cum_in_vagina_ntr(the_person) #$ the_person.cum_in_vagina()
                                $ the_person.draw_person(position = "doggy")
                                "After a few final trusts, [man_name2] pulls out. You see even more sperm flowing out."
                                $ the_person.draw_person(position = "back_peek", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and heads towards the bathroom. [man_name] slaps her ass."
                                the_person "Now I need to take a shower, then we will see who can fuck me harder."
                                $ the_person.draw_person(position = "walking_away")
                                "As [the_person.possessive_title] walks towards the bathroom, you see several white drops falling on the floor."
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Take me again, guys. Fuck me hard! Use my holes to your pleasure. Cum in me! I want to be filled."
                                    man_name2 "Spread wide and receive my load as well!"
                                    man_name "Oh, [the_person.fname], now we will fill both your holes!"
                                    "Seems that both men liked to fill [the_person.possessive_title] with sperm, as they seem to do [the_person.possessive_title] all night long."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person "Hold it, [man_name2]! I have a better idea."
                                $ the_person.draw_person(position = "blowjob")
                                "She pushes away from them. With a wet sound their dicks leaves her pussy and anus. [the_person.possessive_title] gets on her knees on the bed."
                                the_person "[man_name], [man_name2], come here!"
                                "Both of them come closer. Now [the_person.possessive_title] is on her knees with two hard dicks in front of her."
                                the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prudent and boring at times."
                                man_name "I asked [wife_name] once for a bj. She tried but it was awful and she called it disgusting..."
                                the_person "Well, that's your chance to try something new, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on [man_name]'s dick in meantime."
                                man_name2 "I'm gonna cum, [the_person.fname]!"
                                "She just keep on going at steady pace."
                                the_person "Mmmmmm... Mmmm... Uh."
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name2 "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                $ play_swallow_sound()
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "With that she takes his cock with her hot lips."
                                man_name2 "Never thought you are such cum drinking fan, [the_person.fname]!"
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps. With a happy smile she gets up."
                                $ the_person.draw_person(position = "walking_away")
                                the_person "Such a sweet taste. Now for a bath."
                                "You see them walking away to the bathroom."
                                "[man_name]'s hand is on [the_person.title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter the bathroom, the men's dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Take my ass again, [man_name2]. Fuck me more! Ahhh... Give it to me! I want to drink it all!"
                                    man_name2 "Like the taste, bitch? Aren't you a cum-gulping whore, [the_person.fname]?"
                                    "It seems [the_person.possessive_title]'s mouth gonna keep them awake for a while..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                "[man_name] pulls out his cock and finishes on [the_person.possessive_title] belly."
                                man_name "Ow, fuck! That was great!"
                                the_person "Indeed, [man_name]! It was great! I also liked having you two in me."
                                if the_person.get_opinion_score("being submissive") > 0:
                                    the_person "I guess I just like being used this way. I like feeling owned by men while they fuck me."
                                    man_name "Yes, it is a wonderful feeling. I really turns me on. Wish I could do it with my wife..."
                                man_name "Thanks, [the_person.fname]. I really needed that."
                                man_name2 "I'm cumming too!"
                                $ cum_on_ass_ntr(the_person) #$ the_person.cum_on_ass()
                                $ the_person.draw_person(position = "doggy")
                                "[man_name2] takes his dick out of [the_person.possessive_title]'s ass and covers it with his liquid."
                                $ the_person.draw_person(position = "stand2", emotion = "happy")
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person "Didn't that event went great?"
                                the_person "Now go take a shower, guys. I will join you shortly."
                                if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Take me again, guys, please. I really liked your hard things in me at once!"
                                    man_name2 "You are sex hungry slut, [the_person.fname]."
                                    man_name "Let me take your ass this time."
                                    "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                    "[the_person.title] gets on her knees":
                        $ the_person.draw_person(position = "blowjob")
                        "You see as [the_person.possessive_title] gets on her knees, taking down [man_name]'s underwear."
                        "His erected dick is right in front of [the_person.possessive_title]'s face."
                        the_person "Hello there, sweetie. How about we have some fun together?"
                        "[man_name2] also drops his pants and come to her."
                        $ the_person.draw_person(position="blowjob", special_modifier="blowjob")
                        "[the_person.possessive_title] takes the cock in her mouth and starts sucking."
                        "[man_name] places his hands on her head slightly regulating the speed."
                        man_name "It feels great, [the_person.fname]. I like the way you do it!"
                        man_name2 "How about giving me some pleasure too?"
                        "[the_person.possessive_title] begins to suck [man_name2]'s cock, while jerking [man_name]."
                        $ the_person.change_arousal(renpy.random.randint(10,50))
                        menu:
                            "Keep hiding...":
                                $ hidden = True
                            "Don't hide...":
                                $ hidden = False
                        if not hidden or renpy.random.randint(0,2) == 1:
                            "[the_person.possessive_title] turns her head and sees that the door is slightly ajar and you are standing there."
                            if the_person.sluttiness >=70 or the_person.get_opinion_score("public sex") > 0:
                                "[the_person.possessive_title] takes [man_name2]'s dick out of her mouth."
                                the_person "[the_person.mc_title], don't just stand there, come on in. [the_person.possessive_title] will help you relax as well."
                                "Both [man_name] and [man_name2] don't mind you joining the show as [the_person.possessive_title] goes back to sucking them."
                                "You come close to [the_person.possessive_title] and take your dick out of your pants."
                                "She starts stroking you along with [man_name] while [man_name2] keeps driving his dick into her mouth."
                                man_name2 "Oh, [the_person.fname], your tongue is driving me crazy! I think I will come soon!"
                                $ finish = mom_ntr_select_finish(the_person)
                                if finish == "facial":
                                    the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                    man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] covered in sperm, just like in the movies."
                                    man_name "I once came on [wife_name] belly. She called me a pervert and didn't speak to me for a week!"
                                    the_person "Well, this is your chance to try something new, guys! Just like the movies."
                                    "She looks into [man_name2]'s eyes while jerking him with both hands."
                                    man_name2 "I'm cumming [the_person.fname]!"
                                    "She leans closer so that [man_name2] tip is just in front of her eyes."
                                    the_person "Do it, [man_name]! Cover me! Imagine it is your wife, if you like."
                                    $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                    man_name2 "Oh, yes! Get it, you bitch! Get that jizz all over your slutty face, [wife_name2]!"
                                    "[man_name] clearly liked the idea of doing it with his wife."
                                    man_name "Shit, that's hot! I'm cumming too!"
                                    $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Second load is so huge that it spills from [the_person.possessive_title]'s face onto her breasts."
                                    the_person "Two out, one to go!"
                                    $ cum_on_stomach_ntr(the_person) #$ the_person.cum_on_stomach()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "Seeing [the_person.possessive_title] covered in cum is enough of a show and you too start to ejaculate. You finish on [the_person.possessive_title]'s tits and there's so much jizz it starts falling onto her belly."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and the boys need to take a shower."
                                    $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                    "You see them walking away to the bathroom followed by some white drops dripping towards the floor."
                                    "Both men have their hands on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while their dicks show signs of returning to life."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Oh, you are naughty guys! Want some more? Well, why not? As long as you promise to cum on me."
                                        man_name "On your face, [wife_name]! Looking good bitch!"
                                        man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                        "It seems the guys liked role-playing with [the_person.possessive_title] as their sperm dump."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and bed squeaks from [the_person.possessive_title]'s room."
                                elif finish == "drink":
                                    the_person "I want to taste your hot cum. I don't think your wife lets you do this!"
                                    man_name2 "No, [wife_name2] never allows anything other than missionary with a condom, she is so prude and boring at times."
                                    man_name "I asked [wife_name] once for a BJ. She tried but it was awful and she called it disgusting..."
                                    the_person "Well, this is your chance to try something new, guys!"
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "She looks into [man_name2]'s eyes while sucking him off. Her hands are working on two other dicks in meantime."
                                    man_name2 "I'm gonna cum, [the_person.fname]!"
                                    "She keeps on going at steady pace."
                                    the_person "Mmmmmm... Mmmm... Uh."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "[man_name2] shrugs and starts filling her mouth with his load."
                                    man_name2 "Oh, yes! Get it, [wife_name2]!"
                                    "[man_name2] clearly liked the idea of doing it with his wife."
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    $ play_swallow_sound()
                                    "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles. She swallows the sperm, but you still see traces of it."
                                    the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                    man_name2 "It really turned me on! I feel I can do another round shortly."
                                    the_person "We will discuss it later, [man_name2]! Now let's finish with [man_name]. I want to drink his stuff too."
                                    $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                    "With that she takes his cock with her hot lips."
                                    man_name2 "Never thought you were such a cum dump, [the_person.fname]!"
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] speeds up mouth around [man_name]'s dick and in few seconds he cums inside. She retreats back and gulps."
                                    the_person "Here we go. Double sweet load. Now for [the_person.mc_title]."
                                    man_name "Well, her mouth is really something."
                                    $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                    $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                    "[the_person.possessive_title] take you dick in her mouth and in a short time you also explode inside."
                                    "She moves back and gulps."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the floor and smiles."
                                    the_person "Now go to your room, [the_person.mc_title]. Me and guys need to take a bath."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        the_person "Want more of my mouth? Well, okay if you let me drink your cum!"
                                        man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                        "It seems that men are planning to cum in [the_person.possessive_title]'s mouth all the night..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans and gulping sounds from [the_person.possessive_title]'s room."
                                elif finish == "usual":
                                    "[the_person.possessive_title] takes [man_name2]'s cock out of her mouth and starts jerking him off, while you and [man_name] are helping yourselves."
                                    man_name2 "Ow, fuck! That feels great!"
                                    "As he starts to cum, [the_person.possessive_title] closes the tip with her hand so he finishes in it."
                                    man_name "Now help me too!"
                                    "[man_name2] places his instrument into [the_person.possessive_title]'s hand and she starts moving it. In few moments he cums in her hand."
                                    the_person "OK, now for you. [the_person.mc_title]."
                                    "You also explode into her hand."
                                    $ the_person.draw_person(position = "stand2", emotion = "happy")
                                    "[the_person.possessive_title] stands up from the bed and smiles."
                                    the_person "Didn't that event went great?"
                                    the_person "Now go to the bathroom, guys. I will join you shortly."
                                    if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                        "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                        man_name2 "How about another blowjob, [the_person.fname]?"
                                        man_name "I would not mind as well."
                                        "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                    else:
                                        "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            else:
                                $ the_person.happiness -= 5
                                $ the_person.draw_person(position = "blowjob", emotion = "angry")
                                the_person "[the_person.mc_title]! Don't spy on [the_person.possessive_title]! Get beck to your room now!"
                                "You go back to your bedroom accompanied by gulping sounds from [the_person.possessive_title]'s room as she keeps sucking [man_name]'s and [man_name2]'s dicks."
                        else:
                            man_name2 "Oh, [the_person.fname], your tongue is driving me crazy! I think I will come soon!"
                            $ finish = mom_ntr_select_finish(the_person)
                            if finish == "facial":
                                the_person "Would you like to cover my face with your hot cum? I doubt that your wives allows you to do this!"
                                man_name2 "No, [wife_name2] is not into lewd stuff. It's so boring. I wish to see [wife_name2] in sperm, just like in those movies."
                                man_name "I once came on [wife_name] belly. She called me a pervert and didn't speak to me for a week!"
                                the_person "Well, that's your chance to try something new, guys! Just like the movies."
                                "She looks into [man_name2]'s eyes while jerking him with both hands."
                                man_name2 "I'm cumming [the_person.fname]!"
                                "She leans closer so that [man_name2] tip is just in front of her eyes."
                                the_person "Do it, [man_name]! Cover me! Imagine that's your wife, if you like."
                                $ cum_on_face_ntr(the_person) #$ the_person.cum_on_face()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "[man_name2] shrugs and starts spraying his semen over [the_person.possessive_title] face."
                                man_name2 "Oh, yes! Get it, you bitch! Jizz all over your slutty face, [wife_name2]!"
                                "[man_name] clearly liked the idea of doing it with his wife."
                                man_name "Shit, that's hot! I'm cumming too!"
                                $ cum_on_tits_ntr(the_person) #$ the_person.cum_on_tits()
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                "Second load is so huge that it spills from [the_person.possessive_title]'s face on her breast."
                                the_person "Liked that, [man_name]? Seeing a girl on her knees with your sperm over her face?"
                                man_name "It really turns me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, guys. First - a shower. I need to wash off it before it dries."
                                $ the_person.draw_person(position = "walking_away", emotion = "happy")
                                "You see them walking away to the bathroom. Some white drops fall on the floor."
                                "Both men have their hands on [the_person.possessive_title]'s ass, but she does not object. As they close the door, you see that [the_person.title] caresses their balls while dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by talk from [the_person.possessive_title]'s room."
                                    the_person "Oh, you are naughty guys! Want some more? Well, why not? As long as you promise to cum on me."
                                    man_name "On your face, [wife_name]! Looking good bitch!"
                                    man_name2 "And this is for you, [wife_name2]! Aren't you a slut?"
                                    "It seems the guys liked role-playing with [the_person.possessive_title] as their sperm dump."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "drink":
                                the_person "I want to taste your hot cum. Don't think that your wife allows you to do this!"
                                man_name2 "No, [wife_name2] hates oral sex. It is so frustrating."
                                man_name "I once asked [wife_name] for a blowjob. She said if I ever ask this again she will file a divorce!"
                                the_person "Well, that's your chance to experience the feeling, guys!"
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She looks into [man_name2]'s eyes while sucking him off."
                                man_name2 "I'm gonna cum, [the_person.fname]!"
                                "She just keep on going at steady pace."
                                the_person "Mmmmmm... Mmmm... Uh."
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name2] shrugs and starts filling her mouth with his load."
                                man_name "Oh, yes! Get it, [wife_name2]!"
                                "[man_name2] clearly liked the idea of doing it with his wife."
                                $ the_person.draw_person(position = "blowjob", emotion = "happy")
                                $ play_swallow_sound()
                                "His weakened dick falls out from [the_person.possessive_title]'s mouth. She looks up and smiles, while swallowing the sperm, but you still see traces of it."
                                the_person "Liked that, [man_name2]? [wife_name2] is just stupid, it's a wonderful feeling when a man cums in your mouth."
                                man_name "It really turned me on! I feel I can do another round shortly."
                                the_person "We will discuss it later, [man_name2]. First - I need to taste [man_name]."
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "She puts another dick into her mouth and sucks it off."
                                man_name "This is so great. I can't hold much longer!"
                                $ cum_in_mouth_ntr(the_person) #$ the_person.cum_in_mouth()
                                $ the_person.draw_person(position = "blowjob", special_modifier="blowjob")
                                "[man_name] comes into [the_person.possessive_title]'s mouth and pulls his cock away. You see her mouth is full of cum, she gulps it down licking her lips."
                                $ the_person.draw_person(position = "walking_away")
                                "You see them walking away to the bathroom."
                                "[man_name]'s hand is on [the_person.possessive_title]'s ass, and [man_name2] caresses her between the legs, but she does not object. As they enter the bathroom, the men's dicks show signs of returning to life."
                                if the_person.get_opinion_score("being submissive") > 0 or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    the_person "Want more of my mouth? Well, okay if you let me drink your cum!"
                                    man_name2 "Open up your mouth, slut!  You gonna be feed with some hot stuff!"
                                    "It seems that men are planning to cum in [the_person.possessive_title]'s mouth all the night..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
                            elif finish == "usual":
                                "[the_person.possessive_title] takes [man_name2]'s cock out of her mouth and starts jerking him off, while [man_name] is caressing her boobs."
                                man_name2 "Ow, fuck! That feels great!"
                                "As he starts to cum, [the_person.possessive_title] closes the tip with her hand so he finishes in it."
                                man_name "Now help me too!"
                                "[man_name2] places his instrument into [the_person.possessive_title]'s hand and she starts moving it. In few moments he cums in her hand."
                                "[the_person.possessive_title] stands up from the bed and smiles."
                                the_person "Didn't that event went great?"
                                the_person "Now go take a shower, guys. I will join you shortly."
                                if the_person.get_opinion_score("being submissive") > 0  or the_person.sluttiness > 70:
                                    "You go back to your bedroom accompanied by screams from [the_person.possessive_title]'s room."
                                    man_name2 "How about another blowjob, [the_person.fname]?"
                                    man_name "I would not mind as well."
                                    "It seems that men are planning to have some more fun with [the_person.possessive_title]..."
                                else:
                                    "You go back to your bedroom and while drifting to sleep you hear quiet moans from [the_person.possessive_title]'s room."
            "Get back to bed":
                "You decide that it is wrong to interfere into [the_person.possessive_title]'s private life so you go back to your room to sleep."
        $ del man_name2
        $ del wife_name2

    $ del man_name
    $ del wife_name
    $ finish = None
    $ position = None
    $ the_person.change_stats(slut = 1, max_slut = 60)
    $ the_person.reset_arousal()
    $ the_person.apply_planned_outfit()
    $ mc.change_location(bedroom)
    $ clear_scene()
    return
