# Body Monitor Nanobots (Submitted by Thaunatas)

init -2 python:
    def body_monitor_on_turn(the_person, the_serum, add_to_log = True):
        studied_something = False
        for serum in the_person.serum_effects:
            for trait in serum.traits:
                trait.add_mastery(0.1)
                studied_something = True

        if studied_something and add_to_log:
            display_name = the_person.create_formatted_title("???")
            if the_person.title:
                display_name = the_person.title
            mc.log_event("Remotely monitored " + display_name + ", mastery of all active serum traits increased by 0.1", "float_text_blue")
        return

    def body_monitor_on_day(the_person, the_serum, add_to_log):
        if the_person.max_energy < 180:
            the_person.change_max_energy(1, add_to_log = add_to_log)
        return

    def add_body_monitor_serum():
        body_monitor_serum_trait = SerumTraitMod(name = "Body Monitoring Nanobots",
            desc = "Monitoring body functions and vital parameters. Remotely transferring data for further analysis to your R&D Division.",
            positive_slug = "Remote Mastery Improvement",
            negative_slug = "+50 Production Cost",
            research_added = 1000,
            slots_added = 1,
            production_added = 50,
            base_side_effect_chance = 10,
            on_turn = body_monitor_on_turn,
            tier = 99,
            start_researched = False,
            research_needed = 1000,
            exclude_tags = ["Nanobots"],
            clarity_cost = 1000,
            mental_aspect = 0,
            physical_aspect = 3,
            sexual_aspect = 0,
            medical_aspect = 3,
            flaws_aspect = 0,
            attention = 0,
            allow_toggle = False)

    def get_body_monitor_serum():
        return find_in_list(lambda x: x.name == "Body Monitoring Nanobots", list_of_traits)

    def get_body_monitor_serum_mastery():
        serum = get_body_monitor_serum()
        if serum:
            return serum.mastery_level
        return 1.0

    def activate_body_monitory_serum():
        serum = get_body_monitor_serum()
        if serum:
            serum.tier = 2
            serum.researched = True
        return

    def enhance_body_monitor_serum():
        serum = get_body_monitor_serum()
        if serum:
            serum.on_day = body_monitor_on_day
            serum.desc = "Monitoring body functions and vital parameters and slowly improving body condition overnight. Remotely transferring data for further analysis to your R&D Division."
            serum._positive_slug = "Remote Mastery Improvement, +1 Max Energy/day (Max 180)"
        return

label serum_mod_body_monitor_serum_trait(stack):
    python:
        add_body_monitor_serum()
        execute_hijack_call(stack)
    return

init -1 python:
    def body_monitor_progress_count():
        return mc.business.event_triggers_dict.get("body_monitor_progress", 0)

    def body_monitor_phase_1_requirement():
        if mc.business.head_researcher and mc.business.it_director:
            return body_monitor_progress_count() == 0 and len(mc.business.IT_projects) > 0 and mc.business.is_open_for_business and mc.is_at_work
        return False

    def body_monitor_phase_2_requirement():
        if mc.business.head_researcher and mc.business.it_director:
            return day%7 == 0 and time_of_day == 0 and body_monitor_progress_count() == 1
        return False

    def body_monitor_phase_3_requirement():
        if get_body_monitor_serum_mastery() < 3.0:
            return False
        if mc.business.head_researcher and mc.business.it_director:
            return body_monitor_progress_count() == 2 and mc.business.is_open_for_business and mc.is_at_work
        return False

    def body_monitor_phase_4_requirement():
        if mc.business.it_director and day%7 == 6 and time_of_day ==4:
            return body_monitor_progress_count() == 3
        return False

    def bm_on_hold_1_requirement():
        if not mc.business.head_researcher or not mc.business.it_director:
            return body_monitor_progress_count() == 1
        return False

    def bm_continue_1_requirement():
        if mc.business.head_researcher and mc.business.it_director:
            return body_monitor_progress_count() == 1
        return False

    def bm_on_hold_2_requirement():
        return not mc.business.it_director and body_monitor_progress_count() == 3

    def bm_continue_2_requirement():
        return mc.business.it_director and body_monitor_progress_count() == 3

init 2 python:
    body_monitor_phase_1_action = ActionMod("Body Monitor Nano Trait", body_monitor_phase_1_requirement, "body_monitor_phase_1_label",
        menu_tooltip = "Enables the Body Monitoring Nanobot Trait.", category = "Business", is_mandatory_crisis = True) # chose Business as category since its the most fitting at the moment. Maybe add a nanobot section on the research side?
    body_monitor_phase_2_action = Action("Body Monitor Phase 2", body_monitor_phase_2_requirement, "body_monitor_phase_2_label")
    body_monitor_phase_3_action = Action("Body Monitor Phase 3", body_monitor_phase_3_requirement, "body_monitor_phase_3_label")
    body_monitor_phase_4_action = Action("Body Monitor Phase 4", body_monitor_phase_4_requirement, "body_monitor_phase_4_label")
    bm_on_hold_1_action = Action("Body Monitor on Hold 1", bm_on_hold_1_requirement, "bm_on_hold_1_label")
    bm_continue_1_action = Action("Body Monitor Continue 1", bm_continue_1_requirement, "bm_continue_1_label")
    bm_on_hold_2_action = Action("Body Monitor on Hold 2", bm_on_hold_2_requirement, "bm_on_hold_2_label")
    bm_continue_2_action = Action("Body Monitor Continue 2", bm_continue_2_requirement, "bm_continue_2_label")

label body_monitor_phase_1_label():
    $ person_1 = mc.business.head_researcher
    $ person_2 = mc.business.it_director
    $ workplace = mc.location
    if mc.location == mc.business.r_div:
        "As you look up from your work, you see [person_1.possessive_title] standing by her work station while [person_2.possessive_title] is sitting next to her studying some research documents."
        "When [person_1.possessive_title] notices you watching them, she gives you a sign to come over."
    else:
        $ mc.start_text_convo(person_1)
        person_1 "Do you have a moment to come over to the Lab? There is something we would like to discuss with you."
        "You wonder for a moment who could be meant by 'we'. Intrigued you decide to find out right away."
        mc.name "Sure. I am on my way."
        $ mc.end_text_convo()
        "You hurry down to the lab."
        $ mc.change_location(mc.business.r_div)
        "As you enter,  you see [person_1.possessive_title] standing by her work station while [person_2.possessive_title] is sitting next to her studying some research documents."
        "When [person_1.possessive_title] notices you, she waves at you and signals you to come over."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(person_1, position = "stand4", emotion = "happy")
    $ scene_manager.add_actor(person_2, display_transform = character_center_flipped, position = "sitting")
    "You approach your two employees."
    mc.name "Hey, what are you two working on?"
    person_1 "I was just in the middle of showing [person_2.fname] how we process the data from our field studies."
    "You nod and look at [person_2.possessive_title], who seems to be so deeply absorbed by her studies that she doesn't seem to be aware of your presence."
    mc.name "I see. Anything I can help you with?"
    "[person_1.possessive_title] shakes her head."
    person_1 "No, I can handle that. But there is something we wanted to talk to you about. As you can see, [person_2.fname] is really interested in the data we have acquired so far."
    person_1 "While she was reading over the data files, she mentioned that she might know of a way to improve the data we are collecting, and I thought that you might be interested in hearing about it as well. That's why I called you over."
    "Improving the data from your field studies is definitely something you are interested in."
    mc.name "Okay. You got my attention."
    mc.name "What did you come up with, [person_2.title]?"
    "You lay your hand on [person_2.possessive_title]'s shoulder."
    $ scene_manager.update_actor(person_2, position = "stand3")
    "[person_2.possessive_title] jumps up, surprised by your sudden touch. She blushes as she recognizes you."
    "You smile at her apologetically."
    mc.name "Sorry, I didn't mean to startle you."
    "[person_2.possessive_title] smiles sheepishly."
    person_2 "Hey [person_2.mc_title]. Do you need me for something?"
    mc.name "Maybe. [person_1.title] told me that you have an idea to improve our test data acquisition?"
    $ scene_manager.update_actor(person_2, emotion = "happy")
    "[person_2.possessive_title] nods eagerly."
    person_2 "While looking over the files, I noticed that some of the data includes vital parameters like heartbeat, blood-pressure and body temperature. And I think there is an easier method to gather data that doesn't require the test subjects to be present in the Lab."
    person_2 "We could use our nanobots to collect those vital parameters. They could be programmed to send us the data they gather directly into the lab mainframe, where it can be processed by our research team."
    mc.name "That would indeed be very handy. It would allow us to gather research data while our research team can focus on other tasks, right?"
    person_2 "In theory it should. The amount of data we can collect per test subject would be lower compared to a clinical study in the lab, but the nanobots would allow us to study multiple subjects at once, over a larger timescale."
    mc.name "That sounds very promising. How long would it take you to write the program for the bots?"
    person_2 "The program would be far less complex compared to our other nanobot programs. I could have it ready in a day or two, if I focus my time on it."
    "You think for a moment about it. More research data would be very handy. But you don't think it is important enough to let [person_2.possessive_title]'s current assignment suffer from it."
    mc.name "Okay, you got my permission to work on it. But I want you to focus on your current work assignment. I prefer to wait a few days longer rather than seeing your work suffer from it. Understood?"
    $ person_2.change_obedience(5)
    "[person_2.possessive_title] nods obediently."
    person_2 "Yes [person_2.mc_title]. I will work on it while I have some breathing room and focus on it over the weekend. I am sure it will be ready next week."
    "You nod in agreement."
    mc.name "Good. I think I have some work waiting for me. Let me know if there is something else I can help you with."
    "You take your leave and return to your workplace."
    $ mc.change_location(workplace)
    $ scene_manager.clear_scene()
    $ mc.business.event_triggers_dict["body_monitor_progress"] = body_monitor_progress_count() + 1
    $ mc.business.add_mandatory_crisis(body_monitor_phase_2_action)
    $ mc.business.add_mandatory_crisis(bm_on_hold_1_action)
    $ workplace = None
    return

label body_monitor_phase_2_label():
    $ the_person = mc.business.it_director
    $ ceo_office.show_background()
    $ the_person.draw_person()
    "As you approach your office to get ready for work, you notice [the_person.possessive_title] waiting for you in front of your office."
    "You wonder for a moment if you have forgotten about an appointment you set up with her, but then you remember the conversation you had with her last week about the new nanobot program."
    mc.name "Good morning [the_person.title]. I didn't expect you this early in the morning. Please come in and have a seat."
    $ the_person.draw_person(position = "sitting")
    "While you sit down behind your desk, [the_person.possessive_title] takes a seat in front of you. You notice that she is looking a bit exhausted."
    mc.name "You don't look so well. Is everything alright?"
    the_person "I just had a busy night. Don't worry, I am used to it."
    mc.name "Alright. What can I do for you? I assume you want to talk about the new nanobot program?"
    the_person "Yes, [the_person.mc_title]. The program is finished and ready to use. I already uploaded it into our database and set up the mainframe to receive the collected data."
    mc.name "That's great. So we can start adding the new program to our new designs?"
    "[the_person.possessive_title] nods, followed by a slight sigh."
    the_person "Unfortunately it didn't go as smoothly as I had hoped for. While running some simulations with the new program, I ran into a little problem."
    "You can't help but to start to feel a little bit worried."
    mc.name "A problem. Any unforeseen side-effects caused by the nanobots?"
    the_person "No no, nothing like that. The new nanobot program is totally safe to use. I tested it on myself and everything is working as expected."
    "You let out a sigh of relief."
    mc.name "Okay. Then what kind of problem did you run into?"
    the_person "Unfortunately it looks like we wont ba able to use the new program in combination with any of our other nanobot programs. The vital data the new program collects would get corrupted by the other programs."
    "You nod. Corrupted data would be problematic."
    mc.name "But using them as a stand alone program wouldn't cause any problems?"
    the_person "No, [the_person.mc_title]. No problems at all."
    mc.name "Great. Then tell [mc.business.head_researcher.name] that she has the green light to use the new program in our future designs. And please give her all the details she needs to know about."
    $ the_person.draw_person(position = "stand4")
    the_person "Yes [the_person.mc_title]! I will inform her right away."
    $ the_person.draw_person(position = "walking_away")
    "Not being able to use the new nanobot program in combination with your other nanobot programs is an unfortunate drawback, but you are sure that the new program will still prove to be very valuable for your business."
    "You have now unlocked the Body Monitor Nanobot Trait."
    "You wonder what kind of possibilities this will open up? You should get a batch of serums produced using it and research it."
    "You can learn more about it at mastery level 3.0."
    $ clear_scene()
    $ mc.location.show_background()
    $ activate_body_monitory_serum()
    $ mc.business.event_triggers_dict["body_monitor_progress"] = body_monitor_progress_count() + 1
    $ mc.business.add_mandatory_crisis(body_monitor_phase_3_action)
    $ mc.business.remove_mandatory_crisis("bm_on_hold_1_label") # not sure if necessary, but better safe than sorry
    return

label body_monitor_phase_3_label():
    $ person_1 = mc.business.head_researcher
    $ person_2 = mc.business.it_director
    "While taking a break from your work on your way to get a fresh cup of coffee, you see [person_1.possessive_title] approaching you."
    $ scene_manager = Scene()
    $ scene_manager.add_actor(person_1, position = "stand4")
    person_1 "Sorry to bother you [person_1.mc_title], but do you have a moment?"
    mc.name "Sure. What can I do for you?"
    person_1 "I wanted to talk to you about the Body Monitoring Nanobot Program."
    mc.name "The Program? Is there a problem with it?"
    person_1 "No, not really a problem. Just something I noticed while going over the last batch of data we received."
    mc.name "Have you talked to [person_2.fname] about it?"
    person_1 "Not yet. I wanted to talk to you about it before I take any further steps."
    mc.name "Okay. Then let's go to my office."
    $ scene_manager.update_actor(person_1, position = "walking_away")
    "You grab a cup of coffee for you and [person_1.possessive_title]."
    # add a dose of serum to her coffee? Don't want to mess around with that yet. Maybe later, once I figure out how to do it ^^
    "You think about adding a dose of serum to her coffee, but decide against it. You don't know what exactly she wants to talk about and dosing her could have unpredictable consequences."
    $ ceo_office.show_background()
    $ scene_manager.update_actor(person_1, position = "sitting")
    "After sitting down behind your desk, you look at [person_1.possessive_title]."
    mc.name "Alright. What is the matter?"
    person_1 "Like I mentioned before, there is no real problem with the program. The data the nanobots transmit is very valuable for our research. But something caught my attention. The amount of data we receive during daytimes is very high, while during the night, we hardly get any data."
    person_1 "This isn't a big surprise, since most test subjects are asleep during the night. But while the subject are sleeping, the nanobots are idle as well, which means there is a lot of wasted potential."
    "You nod in agreement."
    mc.name "I see. And I assume you would like to make use of that missed potential?"
    person_1 "Exactly."
    mc.name "Okay. Then we should call in [person_2.fname] as well. She is most capable of deciding if any idea you might come up with is feasible or not."
    "You send [person_2.possessive_title] a quick text and some minutes later, you hear a knock at your door."
    mc.name "Come in!"
    $ scene_manager.add_actor(person_2, display_transform = character_center_flipped, position = "stand3")
    person_2 "You wanted to see me, [person_2.mc_title]?"
    "Her eyes brush over [person_1.possessive_title]."
    person_2 "Is there something wrong?"
    mc.name "No need to worry. We were just discussing something, and we need your work expertise about the topic. Please take a seat."
    $scene_manager.update_actor(person_2, position = "sitting")
    "After [person_2.possessive_title] joins you at the desk, you give her a quick recap about the topic and then shift your attention towards [person_1.possessive_title]."
    mc.name "So, what do you have in mind?"
    person_1 "I was thinking about using the nanobots to do something that would be beneficial for the subjects on the one side, but would also benefit your non-work-related activities."
    "[person_1.possessive_title] winks at you with a smirk on her face."
    "You nod, taking the hint."
    person_1 "We could use the idle phase of the nanobots to stimulate the cell rejuvenation process. That would improve the general health of the subject and make them more energetic over the course of time. And a healthier body could also potentially increase the data we can collect."
    mc.name "That sounds interesting. Would that be doable, [person_2.title]?"
    "[person_2.possessive_title] takes a moment to think it over."
    person_2 "That should be within the realm of possibilities. Using the data the nanobots collected during the day, they should be able to track down damaged cells and stimulate the regeneration of those."
    person_2 "We won't be able to do miracles like curing severe diseases, but a general improvement of the body's health is a possibility."
    mc.name "How long would it take to reprogram the bots?"
    person_2 "If I focus on my general work duties, about as long as it took to write the base program. Until next week would be my estimation."
    mc.name "Good. [person_1.title], give her all the specifications she might need. I want this to be finished by Monday morning, if possible."
    $ scene_manager.update_actor(person_1, position = "stand3")
    person_1 "Understood, [person_1.mc_title]. I will give her everything she needs right away."
    $ scene_manager.update_actor(person_2, position = "stand3")
    person_2 "I will start working on it as soon as my schedule allows it, [person_2.mc_title]."
    $ scene_manager.update_actor(person_1, position ="walking_away")
    $ scene_manager.update_actor(person_2, position ="walking_away")
    "You watch your employees leave your office with a smile on your face."
    $ scene_manager.clear_scene()
    $ mc.location.show_background()
    $ mc.business.event_triggers_dict["body_monitor_progress"] = body_monitor_progress_count() + 1
    $ mc.business.add_mandatory_crisis(body_monitor_phase_4_action)
    $ mc.business.remove_mandatory_crisis("bm_on_hold_2_label")
    return

label body_monitor_phase_4_label():
    $ the_person = mc.business.it_director
    $ mc.start_text_convo(the_person)
    the_person "Just wanted to let you know that the improved nanobot program is uploaded to the database and ready to use."
    mc.name "That was quicker than I expected. Did you have any issues?"
    the_person "No, [the_person.mc_title]. Everything went smoothly. First tests showed a slight improvement of vital parameters. But its too early to notice any permanent improvements."
    $ the_person.change_max_energy(1)
    mc.name "Good work anyway. Have a good rest."
    the_person "Good night, [the_person.mc_title]."
    $ mc.end_text_convo()
    "The Body Monitoring Nanobot Trait got enhanced with an additional effect."
    $ enhance_body_monitor_serum()
    $ mc.business.event_triggers_dict["body_monitor_progress"] = body_monitor_progress_count() + 1
    $ mc.business.remove_mandatory_crisis("bm_on_hold_2_label") # Again, just to be safe
    return

label bm_on_hold_1_label():
    if mc.business.it_director is None:
        "Since your IT director position is vacant at the moment, you decide to put the new nanobot program project on hold, but keep the notes left behind by your former IT Director to be able to continue the project once the position is filled again."
    else:
        "Since your head researcher position is vacant now, you tell [mc.business.it_director.possessive_title] to put the new nanobot program project on hold until you assign a new Head Researcher."
    $ mc.business.remove_mandatory_crisis("body_monitor_phase_2_label")
    $ mc.business.add_mandatory_crisis(bm_continue_1_action)
    return

label bm_continue_1_label():
    "Now that both your IT director position and head researcher position are filled again, you give permission to continue the work on the new nanobot program."
    $ mc.business.add_mandatory_crisis(body_monitor_phase_2_action)
    $ mc.business.remove_mandatory_crisis("bm_on_hold_1_label")
    return

label bm_on_hold_2_label():
    "Since your IT director position is vacant at the moment, you decide to put the improvement of the nanobot program on hold, but keep the notes left behind by your former IT Director to be able to continue the project once the position is filled again."
    $ mc.business.remove_mandatory_crisis("body_monitor_phase_4_label")
    $ mc.business.add_mandatory_crisis(bm_continue_2_action)
    return

label bm_continue_2_label():
    "Now that your IT director position is filled again, you give permission to continue the work on the new nanobot program."
    $ mc.business.add_mandatory_crisis(body_monitor_phase_4_action)
    $ mc.business.add_mandatory_crisis(bm_on_hold_2_action)
    return
