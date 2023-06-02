# Contains all of the events and related things to Christina's role (Emily's mother)
init 2 python:
    list_of_instantiation_functions.append("create_christina_character")

    def christina_foreplay_position_filter(foreplay_positions):
        # only allow groping until kissed
        if christina.event_triggers_dict.get("student_mom_door_kiss", 0) == 0:
            return foreplay_positions[1] in [standing_grope]
        return True

    def christina_oral_position_filter(oral_positions):
        # for now unlock after kiss
        return christina.event_triggers_dict.get("student_mom_door_kiss", 0) != 0

    def christina_vaginal_position_filter(vaginal_positions):
        # for now unlock after few blowjobs with swallow
        return christina.sex_record.get("Cum in Mouth", 0) > 3

    def christina_anal_position_filter(anal_positions):
        # for now unlock after few creampies
        return christina.sex_record.get("Vaginal Creampies", 0) > 3

    def create_christina_character():
        ### CHRISTINA (EMILY'S MOM) ###
        christina_wardrobe = wardrobe_from_xml("Christina_Wardrobe")
        #original height = 0.94
        global christina
        christina_base = Outfit("Christina's accessories")
        christina_base.add_accessory(diamond_ring.get_copy())

        christina = create_random_person(name = "Christina", last_name = "Vandenberg", age = 47, body_type = "standard_body", face_style = "Face_8", tits = "DD", height = 0.96, hair_colour = "chestnut", hair_style = braided_bun, pubes_style = diamond_pubes, skin = "white", \
            eyes = "light blue", personality = reserved_personality, starting_wardrobe = christina_wardrobe, stat_array = [4,2,3], skill_array = [2,1,1,1,1], sex_skill_array = [2,3,3,2], \
            sluttiness = 10, obedience = 105, happiness = 85, love = 0, start_home = emily.home, relationship = "Married", kids = 1, base_outfit = christina_base,
            work_experience = 2,type="story", job = Job("Trophy Wife", critical_job_role))

        christina.set_schedule(christina.home) #She's a stay-at-home Mom.
        christina.home.add_person(christina)
        christina.home.background = luxury_apartment_background
        christina.home.darken = False

        town_relationships.update_relationship(christina, emily, "Daughter", "Mother")
        #Note: She plays an important role to Emily's story, but she is just given the normal affair role during the game.

init -2 python:
    def student_mom_appologise_requirement(the_person):
        if time_of_day != 3:
            return False
        elif the_person not in the_person.home.people:
            return False
        else:
            return True

    def add_student_mom_apologize_action(person):
        student_mom_apologize_action = Action("Student_mom_appologise", student_mom_appologise_requirement, "student_mom_appologise_label")
        person.on_room_enter_event_list.append(student_mom_apologize_action)
        person.event_triggers_dict["student_mom_door_kiss"] = 1
        return

label study_check_up(the_student, the_mom):
    # TODO: Christina asks how things are going after a study session.
    # If her marks have improved enough, and if you haven't been already, Christina invites you to stay for dinner.
    if (the_student.tits_visible or the_student.vagina_visible) and not (the_student.planned_outfit.tits_visible or the_student.planned_outfit.vagina_visible):
        $ the_student.apply_planned_outfit() #Get dressed again
        $ the_student.draw_person()
        "[the_student.possessive_title] gets dressed so she can safely show you to the door."

    $ clear_scene()
    "[the_student.title] opens the door to her room and leads you downstairs. [the_mom.title] is waiting at the front door."
    $ her_hallway.show_background()
    $ the_group = GroupDisplayManager([the_student, the_mom], primary_speaker = the_mom)
    $ the_group.draw_group()


    if (the_student.tits_visible or the_student.vagina_visible) and not the_mom.judge_outfit(the_student.outfit, -10):
        "She is about to say something, when she notices her daughter's state of undress."
        the_mom "[the_student.fname], where are your clothes!"
        the_student "Hmm? Oh, I was just..."
        "Her mother cuts her off, clearly intending the question to be rhetorical."
        the_mom "Go put something on, right now! I'm sorry [the_mom.mc_title], she shouldn't have been undressed like that around you."
        mc.name "It's no problem, really. As long as she's learning I don't care what she wears."
        $ the_student.apply_outfit(the_student.get_random_appropriate_outfit(20, guarantee_output = True ))
        $ the_group.redraw_person(the_student)
        "[the_student.possessive_title] scampers off to her room and returns a short moment later, more reasonably dressed."
        the_student "Sorry..."
        the_mom "That's better. Now [the_mom.mc_title], tell me how my daughter is doing."

    elif not the_mom.judge_outfit(the_student.outfit, -10):
        if the_mom.judge_outfit(the_student.outfit, 10):
            # Just a little too slutty
            "She's about to say something, but pauses and looks over [the_student.title]'s outfit."
            the_mom "[the_student.fname], do you really think that's appropriate to wear when we have guests over?"
            the_student "[the_student.mc_title] isn't just a guest Mom, he's a friend!"
            "She scowls at her daughter."
            the_mom "We'll have a talk about this later."
            "[the_mom.possessive_title] turns her attention to you."
            the_mom "Tell me [the_mom.mc_title], how is my daughter doing? I hope her marks are better than her sense of decency."

        elif the_student.underwear_visible:
            "She's about to say something, but pauses when she notices her daughter's lack of clothing."
            the_mom "[the_student.fname], where are your clothes? You shouldn't be wandering around in your underwear when we have a guest."
            the_student "Oh, he doesn't care, right [the_student.mc_title]?"
            "You shrug and nod."
            mc.name "She'll see the best results if she's comfortable while studying, and I suppose she finds that comfortable."
            mc.name "As long as she's learning I don't care what she's wearing."
            "[the_mom.possessive_title] scowls at her daughter for a moment, but then turns her attention to you."
            the_mom "Well then tell me [the_mom.mc_title], how are her marks doing?"

        else:
            "She's about to say something, when she notices her daughter's outfit."
            the_mom "[the_student.fname], what are you wearing!"
            the_student "Hmm? Oh, I was just..."
            "Her mother cuts her off, clearly intending the question to be rhetorical."
            the_mom "Go put something on, right now! I'm sorry [the_mom.mc_title], she shouldn't have been undressed like that around you."
            mc.name "It's no problem, really. As long as she's learning I don't care what she wears."
            $ the_student.apply_outfit(the_student.get_random_appropriate_outfit(20, guarantee_output = True))
            $ the_group.redraw_person(the_student)
            "[the_student.possessive_title] scampers off to her room and returns a short moment later, more reasonably dressed."
            the_student "Sorry..."
            the_mom "That's better. Now [the_mom.mc_title], tell me how my daughter is doing."

    else:
        pass #Even if she's a little naked her mom is chill with it. Neat!
        the_mom "All done for tonight? Tell me [the_mom.mc_title], how is my daughter doing?"

    $ current_marks = the_student.event_triggers_dict.get("current_marks",0)
    if current_marks < 20:
        mc.name "I'll be honest, there's still a lot of work to do. It's going to take a lot of hard work if she wants to succeed."
        the_mom "Do you hear that [the_person.fname]? I expect you to keep working at this and to listen to everything [the_mom.mc_title] says."
        $ the_group.draw_person(the_student)
        $ the_student.change_happiness(-5)
        $ the_student.change_obedience(1)
        the_student "I promise I'm doing my best Mom."

    elif current_marks < 50:
        mc.name "I've watched her improve a little, but there's still a long way to go."
        mc.name "[the_student.fname] has been giving it her all though. I think with more time and focus she'll be able to do it."
        the_mom "At least she's improving. [the_student.fname], I expect you to listen to [the_mom.mc_title] and do everything he suggests."
        $ the_group.draw_person(the_student)
        $ the_student.change_happiness(-5)
        $ the_student.change_obedience(1)
        the_student "Okay Mom, I will."

    elif current_marks < 75:
        mc.name "[the_student.fname] is really starting to improve. As long as she can keep this up she will do fine."
        the_mom "That's good to hear. I'm glad to hear you are working so well with [the_mom.mc_title]."
        $ the_group.draw_person(the_student)
        $ the_student.change_obedience(1)
        the_student "Thank you Mom. He's been such a big help."

    elif current_marks < 95:
        mc.name "[the_student.fname] has turned things around. As long as she stays on top of her studies she shouldn't have any more problems."
        $ the_mom.change_love(1)
        the_mom "That's very good to hear. [the_student.fname], I'm proud of you."
        $ the_group.draw_person(the_student)
        $ the_student.change_obedience(1)
        $ the_student.change_love(1)
        the_student "Thanks Mom, It was really [the_student.mc_title], he's a very engaging teacher."


    else:
        mc.name "[the_student.fname] has been a model student. She's put in the hard work, and her marks reflect that. I'm expecting her to be the top of her class."
        $ the_mom.change_love(1)
        the_mom "Well that's surprising to hear. [the_student.fname] has never been very invested in her academics before."
        $ the_group.draw_person(the_student)
        $ the_student.change_obedience(1)
        $ the_student.change_love(2)
        the_student "I owe it all to [the_student.mc_title], he's the best teacher I've ever had. He really knows how to teach me a lesson."

    $ the_group.draw_person(the_mom)
    if the_student.event_triggers_dict.get("current_marks",0) >= 75:
        if the_mom.event_triggers_dict.get("offered_dinner", 0) == 0:
            $ the_mom.event_triggers_dict["stayed_for_dinner"] = 0
            $ the_mom.event_triggers_dict["offered_dinner"] = 1
            the_mom "Thank you for all your hard work [the_mom.mc_title]."
            the_mom "If you don't have any plans for the evening you're welcome to join us for dinner."#

        else:
            the_mom "Thank you for all of your hard work [the_mom.mc_title]. Would you like to join us for dinner tonight?"

        $ the_group.draw_person(the_student, emotion = "happy")
        "[the_student.possessive_title] holds onto your arm and smiles happily."
        the_student "You can stay a little longer, right [the_student.mc_title]?"

        menu:
            "Stay for dinner":
                mc.name "I'd love to stay for dinner. Thank you [the_mom.fname]."
                $ the_group.draw_person(the_mom)
                if the_mom.event_triggers_dict["stayed_for_dinner"] == 0:
                    the_mom "Excellent! Mr.[the_mom.last_name] will be home soon, he has wanted to meet you for a long time."
                    the_mom "I will have dinner ready in a few minutes. [the_student.fname], can you show [the_mom.mc_title] to the dining room and get the places set?"
                    call student_dinner(the_student, the_mom, first_time = True) from _call_student_dinner
                else:
                    the_mom "Excellent! I will have dinner ready in a few minutes."
                    the_mom "[the_student.fname], can you show [the_mom.mc_title] to the dining room and get the places set?"
                    $ the_group.draw_person(the_student)
                    the_student "Right away Mom. Come with me."
                    call student_dinner(the_student, the_mom, first_time = False) from _call_student_dinner_1
                $ the_mom.event_triggers_dict["stayed_for_dinner"] += 1

            "Leave politely":
                mc.name "I'm sorry, I made other plans for tonight."
                $ the_group.draw_person(the_mom)
                the_mom "That's a shame. Maybe next time you're over to tutor [the_student.fname] then."
                mc.name "I'll do my best."


    else:
        the_mom "Thank you for your hard work [the_mom.mc_title]. I hope we see you again soon."

    $ the_group = None
    $ mc.change_location(bedroom)
    return

label student_dinner(the_student, the_mom, first_time):
    python:
        clear_scene()
        scene_manager = Scene()
        christina.home.show_background()
        scene_manager.add_actor(the_student, emotion = "happy")
    if first_time:
        "[the_student.possessive_title] leads you into a finely decorated dining room. She pulls out a chair and motions for you to sit down at the table."
        $ add_christina_council_influence_intro_action()
        $ add_christina_daughter_training_action()
        $ add_christina_free_time_action()
        $ christina.set_event_day("obedience_event")
        $ christina.set_event_day("love_event")
        $ christina.set_event_day("slut_event")
        $ christina.set_event_day("story_event")
        $ christina.progress.love_step = 0
        $ christina.progress.obedience_step = 0
        $ christina.progress.lust_step = 0
    else:
        "[the_student.possessive_title] leads you into the dining room and pulls out a chair for you."
    the_student "You just have a seat, I'll get everything ready."
    $ scene_manager.update_actor(the_student, position = "sitting")
    "You sit down and wait while [the_student.possessive_title] sets out place mats and cutlery. When she's done she sits down in the seat next to you."
    $ scene_manager.add_actor(the_mom, display_transform = character_left_flipped)
    "After waiting for a few minutes [the_mom.possessive_title] steps out from the kitchen, carrying a tray of roasted chicken and a bottle of wine under her arm."
    "She places the tray down, places the bottle of wine down, and sits down across from you and her daughter."
    $ scene_manager.update_actor(the_mom, display_transform = character_center_flipped, position = "sitting")
    the_mom "Mr. [the_mom.last_name] should be home any minute now, he's probably just held up at the office."
    mc.name "No problem, we can wait a little..."
    $ scene_manager.update_actor(the_mom, position = "walking_away")
    "You're interrupted by the phone ringing. [the_mom.possessive_title] apologizes and moves into the kitchen."
    $ scene_manager.hide_actor(the_mom)
    the_mom "Yes... Okay... [the_student.fname]'s tutor is over for dinner... I'll tell him... We can talk when you get home..."
    $ scene_manager.show_actor(the_mom, position = "sitting", emotion = "sad")
    "[the_mom.possessive_title] comes back into the room and sits down. She has a tense smile as she reaches for the bottle of wine."
    $ mc.change_locked_clarity(5)
    if first_time:
        the_mom "My husband is going to be at the office for the rest of the night, so we should just get started."
        the_mom "He wanted me to tell you how happy he is with your work."
        "[the_student.possessive_title] sits, uncomfortably quiet, as her mother uncorks the bottle of wine and pours herself a generous amount."
    else:
        the_mom "My husband is going to be at the office late again. He told us to have dinner without him."
        "[the_student.possessive_title] sighs unhappily as her mother uncorks the bottle of wine. She pours herself a generous glass."

    the_mom "Let me pour you both a glass..."
    "You have dinner with [the_student.possessive_title] and [the_mom.possessive_title]."
    "[the_mom.possessive_title] seems tense at first, but after some food and two glasses of wine she is smiling and making pleasant conversation."
    $ scene_manager.update_actor(the_mom, emotion = "happy")
    the_mom "[the_student.fname], you made a very good choice when you asked [the_mom.mc_title] to tutor you. He's an absolute pleasure to have around."
    if the_student.love > 40 or the_student.effective_sluttiness() > 30:
        "[the_student.possessive_title] places her hand on your thigh and rubs it for emphasis."
        $ mc.change_locked_clarity(15)
        if the_student.effective_sluttiness() > 50:
            "She carries on the conversation with her mother, but her hand starts to drift higher up."
            $ mc.change_locked_clarity(20)
            "Soon [the_student.possessive_title] is rubbing your bulge under the table, massaging it through your pants."

    if the_mom.effective_sluttiness() > 20:
        $ mc.change_locked_clarity(10)
        "While you are talking you feel a gentle touch on your leg. You glance under the table and see it is [the_mom.possessive_title]'s foot caressing your calf."
        "She turns to you and smiles, keeping up her conversation with her daughter while her foot moves up your leg."
        $ mc.change_locked_clarity(10)
        "Soon enough she is rubbing her soft foot against your inner thigh. The movement brings her dangerously close to brushing your cock."
        "After a few moments of teasing she draws her leg back and slips her foot back in her shoe."

    the_mom "Now, how about I get dessert ready. [the_student.fname], please clean the table. Leave my wine, I'll have the rest with dessert."
    $ scene_manager.update_actor(the_student, position = "stand3")
    the_student "Okay Mom."
    $ scene_manager.update_scene(position = "walking_away")
    "Both women stand up. [the_mom.possessive_title] moves into the kitchen, while her daughter collects a stack of dirty dishes before following behind her."
    $ clear_scene()
    # You can already give Emily serum while she's studying, so this is just to corrupt her Mom.
    menu:
        "Add serum to [the_mom.possessive_title]'s wine" if mc.inventory.total_serum_count > 0:
            call give_serum(the_mom) from _call_give_serum_student_dinner_enhanced
            if _return:
                "You stand up and lean over the table, quickly emptying the contents of a small glass vial into [the_mom.possessive_title]'s half-finished wine glass."
                "You give the glass a quick swirl, then sit back down and wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."
            else:
                "You reconsider, and instead sit back in your chair and wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."

        "Add serum to [the_mom.possessive_title]'s wine\n{color=#ff0000}{size=18}Requires: Serum{/size}{/color} (disabled)" if mc.inventory.total_serum_count == 0:
            pass
        "Leave her drink alone":
            "You lean back in your chair and relax while you wait for [the_mom.possessive_title] and [the_student.possessive_title] to return."

    "After another minute or two both of them come back from the kitchen, now carrying small bowls of ice cream."
    $ scene_manager.update_actor(the_mom, position = "stand3")
    $ scene_manager.update_actor(the_student, position = "sitting")
    "[the_student.possessive_title] places one bowl down in front of you before sitting back in her chair beside you."
    $ scene_manager.update_actor(the_mom, position = "sitting")
    "[the_mom.possessive_title] sits down and takes a sip from her wine."
    the_mom "I'm glad you were able to join us for the evening [the_mom.mc_title]."
    the_mom "It seems like my husband is always at work, it's nice to have some company."
    menu:
        "Talk about [the_student.possessive_title]":
            mc.name "It's no trouble. It also gives us a perfect opportunity to talk about your daughter's education."
            if the_mom.event_triggers_dict.get("student_mom_extra_obedience", False):
                the_mom "Yes, give me an update on how things are going."
                "You give [the_mom.possessive_title] a recap of your work educating [the_student.possessive_title], leaving out anything too explicit."
                $ the_mom.change_happiness(5)
                the_mom "It sounds like you have everything under control. Good work."

            else:
                the_mom "That's a very good idea. Is she giving you any problems?"
                "You glance at [the_student.possessive_title] at your side, then shake your head."
                mc.name "No, she is doing very well. There are some new study techniques that I would like to try though."
                the_mom "Is that so? Well you have my full permission. [the_student.fname], I want you to do everything [the_mom.mc_title] tells you to do."
                the_mom "Please treat his instructions as if they were coming from me or your father."
                $ the_student.change_obedience(10)
                the_student "Yes Mom, I promise I will."
                $ the_mom.event_triggers_dict["student_mom_extra_obedience"] = True

        "Flirt with [the_mom.possessive_title]":
            mc.name "The pleasure is all mine. Your daughter is wonderful, I should have known she got it from her mother."
            "[the_mom.possessive_title] laughs and waves you off."
            the_mom "You're too kind."
            "You flirt with [the_mom.possessive_title] as much as you think you can get away with while her daughter is in the room."
            $ the_mom.change_stats(slut = 1, max_slut = 25, love = 2, max_love = 25)

        "Touch [the_student.possessive_title]" if the_student.effective_sluttiness("touching_body") > 35:
            mc.name "I'm glad to be here. I'm always happy to spend time with you and your daughter."
            "You move a hand to your side, and then onto [the_student.possessive_title]'s thigh, rubbing it gently."
            $ mc.change_locked_clarity(10)
            "You move your hand higher, up her thigh and to her crotch. You can feel her struggling to keep still in front of her mother."

            if the_student.effective_sluttiness() > 50:
                "In response [the_student.possessive_title] moves her hand onto your crotch, the movements hidden by the table."
                $ mc.change_locked_clarity(20)
                "She runs her hand along the bulge of your crotch, stroking you slowly through the fabric."
                the_student "He's been such a strong, firm presence in my life since I met him. I'm really learning a lot."
                $ the_student.change_slut(1, 65)
                $ mc.change_locked_clarity(20)
                "You and [the_student.possessive_title] fondle each other while you eat dessert, doing your best to keep [the_mom.possessive_title] from noticing everything."

            else:
                $ mc.change_locked_clarity(10)
                "You fondle [the_student.possessive_title] as you eat your dessert, doing your best to keep [the_mom.possessive_title] from noticing."

            $ the_student.change_slut(1 + the_student.get_opinion_score("public sex"))
            $ the_student.discover_opinion("public sex")
            "Eventually you finish your ice cream."
            the_mom "[the_student.fname], could you clean things up for us?"

    $ scene_manager.update_actor(the_student, position = "walking_away")
    "[the_student.possessive_title] collects the dishes again when you've finished dessert and carries them to the kitchen."
    $ scene_manager.hide_actor(the_student)
    the_mom "It's been wonderful having you over [the_mom.mc_title], but I'm sure you're looking forward to getting home."
    $ scene_manager.update_actor(the_mom, position = "stand3")
    mc.name "The dinner was fantastic. I'm lucky to have such a generous, beautiful host."
    "[the_mom.possessive_title] seems to blush, although it might just be the wine taking effect."
    $ her_hallway.show_background()
    $ scene_manager.show_actor(the_student, position = "stand4")
    "[the_mom.possessive_title] and [the_student.possessive_title] walk you to the door to say goodbye."
    the_student "Bye [the_student.mc_title], I hope you'll be by again soon!"
    if the_mom.effective_sluttiness("kissing") > 20 and not the_mom.event_triggers_dict.get("student_mom_door_kiss", 0) == 1: #TODO: Add a check that we haven't triggered the "I'm sorry" event.
        the_mom "[the_student.fname], I need to have a private word with [the_mom.mc_title] before he goes."
        $ scene_manager.remove_actor(the_student)
        "[the_student.possessive_title] nods and goes upstairs to her room. [the_mom.possessive_title] waits until she is gone before turning back to you."
        if the_mom.event_triggers_dict.get("student_mom_door_kiss", 0) == 2: #TODO: Add a check that you've also triggered the "I'm sorry event
            # She wants to kiss you, and you've already done it before
            the_mom "I just wanted to say thank you again for coming over..."
            $ scene_manager.update_actor(the_mom, position = "kissing", emotion = "happy", special_modifier = "kissing")
            "She takes a half step closer and leans in. You close the rest of the gap and kiss her."
            $ mc.change_locked_clarity(10)
            "[the_mom.possessive_title] kisses you passionately at the door, rubbing her body against you for a moment."
            "After a long moment she pulls back and breaks the kiss, panting softly."
            $ scene_manager.update_actor(the_mom, special_modifier = None)
            $ the_mom.break_taboo("kissing")
            the_mom "Come again soon, okay? I don't like being lonely..."
            mc.name "I won't be gone long."
            $ scene_manager.update_actor(the_mom, position = "stand3")
            "She watches you from the front door as you leave."

        else:
            # It's the first time
            mc.name "Is something wrong?"
            the_mom "No, nothing is wrong. I wanted to say thank you for tutoring my daughter."
            "She takes a half step closer, putting one of her legs between yours."
            the_mom "And for spending the evening with me, when I would have otherwise been all alone..."
            "She leans close, barely an inch separating you from her. You can smell the faint hint of wine on her breath."
            the_mom "With no one to comfort me..."
            $ scene_manager.update_actor(the_mom, position = "kissing", emotion = "happy", special_modifier = "kissing")
            "[the_mom.possessive_title] closes the gap and kisses you passionately, almost over-eagerly."
            $ mc.change_locked_clarity(10)
            "She presses her body against you and holds the back of your neck. After a long moment she pulls back, panting softly."
            $ scene_manager.update_actor(the_mom, special_modifier = None)
            $ the_mom.change_slut(1, 60)
            $ the_mom.break_taboo("kissing")
            the_mom "Thank you for staying for dinner [the_mom.mc_title]. I hope I see you again soon..."
            $ scene_manager.update_actor(the_mom, position = "stand3")
            "She steps back, trailing a hand along your chest."
            mc.name "I hope so too. Goodnight [the_mom.title]."
            "She watches you from the front door as you leave the house."
            $ add_student_mom_apologize_action(the_mom)

    else:
        the_mom "You're welcome to come again for dinner any time [the_mom.mc_title]. Have a good evening."
        "They watch you from the porch as you leave."





    #TODO: Something like "It's nice to have some company at home..."
    #TODO: Branching options? Let the player select what they want to do?
    #TODO: Something should lead directly into her having the affair role.
    #TODO: Options like "Talk about her daughter.", "Flirt with Christina.".
    #TODO: If she's slutty enough (should be achievable with some minor corruption or serum use, 25-ish) she finds a way to kiss you. The next time you're over she appologises.



    # TODO: This event. YOu stay for dinner. Emily's father is "delayed at the office", so the three of you have dinner together.
    # Christina praises your work and gives you permission to "do whatever you need to do to help her daughter."
    # Mention that she should "get more involved" in her daughters schooling.
    # She also gets a little tipsy and a little hands-y with you when you go to leave.

    $ the_mom.event_triggers_dict["stayed_for_dinner"] += 1
    $ scene_manager.clear_scene()
    return

label student_mom_appologise_label(the_person): #TODO Provide a way to not activate this event right away? Or even just to turn it down when it triggers.
    if the_person.has_role(affair_role) or the_person.effective_sluttiness() >= 60:
        $ the_person.event_triggers_dict["student_mom_door_kiss"] = 2
        return # There's nothing to worry about, she's either already fooling around with you or she's slutty enough she doesn't care.

    # first show apartment
    $ renpy.show("Apartment Entrance", what = apartment_background, layer = "master")
    $ the_person.draw_person()
    the_person "[the_person.mc_title], it's nice to see you."
    "She avoids making eye contact with you, looking off to the side."
    the_person "Could I speak with you for a moment, privately?"
    $ renpy.show(name = "living room", what = house_background, layer = "master")
    "You nod and follow her to the sitting room."
    the_person "I wanted to apologize for my moment of indiscretion."
    the_person "I was angry, and lonely, and drunk, and I lost control. I'm sorry."
    mc.name "You mean when you kissed me?"
    "She nods meekly."
    mc.name "You don't need to be sorry, I liked it. It sounds like you really needed it, too."
    the_person "I don't know what you mean..."
    mc.name "It's pretty obvious. When's the last time your husband was home on time?"
    the_person "It's been a few weeks..."
    mc.name "When was the last time you had sex together?"
    if the_person.effective_sluttiness() < 35:
        the_person "[the_person.mc_title], that's a little personal!"
        mc.name "It's been a while though, right?"
        the_person "It... has been a while. You're right."
    else:
        the_person "It... certainly has been a long time. Sometimes he asks to be pleasured when he gets home, but he never reciprocates."
        "She shakes her head in disbelief."
        the_person "I'm sorry, I shouldn't be telling you that."
    mc.name "You're a woman, and you have needs. [emily.title] is out of the house most of the day, your husband is working..."
    $ mc.change_locked_clarity(10)
    "You step close to [the_person.possessive_title] and put your arm around her waist."
    mc.name "It's natural for you to need some sort of physical contact. Isn't that what you want?"
    "She stutters out a few half answers."
    the_person "I don't... I mean, it would be nice, but I can't... I..."
    $ mc.change_locked_clarity(10)
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "You kiss her, and after a moment of hesitation she kisses you back."
    $ the_person.draw_person(position = "kissing")
    "When you break the kiss she looks deep into your eyes."
    the_person "Wow..."
    $ the_person.draw_person()
    mc.name "I'm going to be here to tutor your daughter. I could also give you the physical satisfaction you need."
    the_person "You mean, cheat on my..."
    "You nod. She sighs and closes her eyes, thinking it over. Your hand wanders down her back until you are cradling her ass."
    "Finally she opens her eyes and answers."
    the_person "I'm not going to throw myself at you, just because you happen to tutoring my daughter!"
    mc.name "Fine. Look, I'm not saying we start fucking. I can do other things for you to help you out, and maybe you can return the favor too."
    "She looks down, but seems to understand what you are saying."
    mc.name "I mean, it isn't really cheating just to have someone finally gety you some release with their fingers once in a while right?"
    the_person "I... I guess not."
    $ mc.change_locked_clarity(10)
    $ play_spank_sound()
    "You slap her ass hard, making her jump a little bit."
    mc.name "Good. I'll be seeing you soon."
    "She nods meekly, cheeks flush."
    return

label bad_mom_intro(the_person): #TODO: Set this up
    #When she hears that her daughter might actually pass her test she asks you to "stall her a little" so you can stay around
    # If you do that she tells you how horny the idea makes her. Asks you to do progressively meaner things to her daughter to get off.
    return
