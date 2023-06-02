# SAKARI OUTLINE
# Sakari is Kaya's mother, who is in failing health due to a bloodborn disease. She doesn't actually meet MC until later in the game (EG pacing with Candace)
# Sakari's intro event is paced based on having Ellie doing IT projects, since that means the business is somewhere in tier 2. Sakari's story is the first that is TIME SENSITIVE
# Sakari starts at 100 max energy, and it drops by 5 every week. Upon reaching <50, MC gets a notification that Sakari has gone to the hospital, then hospice, then passes away.
# Sakari's love events will give MC the opportunity to research a cure for her, but it will be very expensive. Alternatively, MC can try and make her remaining days "as pleasurable as possible"
# We introduce Sakari at the clothes store, which we discover she owns. Her 20 love event involves MC discovering the nature of her affliction, at 40 she offers to sell MC her business
# At 60 love she wants to be with MC for what is left of her time if she hasn't been cured yet. If MC cures sakari before she gets to 60 love, she bypasses the 60 love event and goes to 80 love event
# 80 love event only activates if Sakari has been cured, and she basically offers to be MC's personal MILF, even if MC is also dating Kaya.
# At 100 love if Kaya is also at 100 love they offer to move in with MC. Kaya's love quests involve MC talking with Lily and Jennifer about their relationship, so it is not a surprise to them.
# Sakari's sluttiness events basically revolve around doing slutty things she never got to do during her life.
# At 20 she skinny dips with MC at night
# at 40 she blows MC at the movie theatre
# at 60 she fucks MC in a dressing room at her clothing store
# at 80 she asks MC if she can dance at his strip club for one night (must own strip club)
# at 100 she offers to join MC's harem if he has one, if not and 100 sluttiness with Kaya she has a threesome with her and MC.



#Init
init 2 python:
    list_of_instantiation_functions.append("create_sakari_character")

    def create_sakari_character():
        sakari_base_outfit = Outfit("sakari's base accessories")
        the_glasses = modern_glasses.get_copy()
        the_glasses.colour = [.15, .15, .15, 1.0]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.15, .15, .15, 0.5]
        the_rings = garnet_ring.get_copy()   #Change this
        the_rings.colour = [.82,.15,.15,1.0]
        sakari_base_outfit.add_accessory(the_lipstick)
        sakari_base_outfit.add_accessory(the_rings)
        sakari_base_outfit.add_accessory(the_glasses)

        # init sakari role
        global sakari_role
        sakari_role = Role(role_name ="sakari", actions =[], hidden = True)

        #global sakari_role
        global sakari
        sakari = make_person(name = "Sakari", last_name ="Greene", age = 42, body_type = "thin_body", face_style = "Face_14",  tits="C", height = 0.92, hair_colour="black", hair_style = bald_hair, skin="tan" , \
            eyes = "brown", personality = sakari_personality, name_color = "#FFA500", job = unemployed_job, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [4,2,2,2], sluttiness = 7, obedience_range = [100, 120], happiness = 88, love = 0, \
            relationship = "Single", kids = 1, force_random = True, base_outfit = sakari_base_outfit, type = 'story',
            forced_opinions = [["production work", 2, True], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour blue", -2, False], ["classical music", 1, False]],
            forced_sexy_opinions = [["being submissive", 2, False], ["getting head", 1, False], ["drinking cum", -2, False], ["giving blowjobs", -1, False], ["creampies", 2, False]])

        sakari.generate_home()
        sakari.add_role(sakari_role)
        sakari.set_schedule(sakari.home, the_times = [0,1,2,3,4])   #Hide Sakari at home until we are ready to use her
        sakari.home.add_person(sakari)

        # sakari_mod_initialization():
        # sakari.event_triggers_dict["intro_complete"] = False    # True after first talk
        # sakari.event_triggers_dict["is_sick"] = False           # True after intro. This triggers her energy degeneration
        # sakari.event_triggers_dict["mc_knows_sick"] = False
        # sakari.event_triggers_dict["mc_offered_partner"] = False
        # sakari.event_triggers_dict["mc_is_partner"] = False
        # sakari.event_triggers_dict["mc_is_booty_call"] = False
        # sakari.event_triggers_dict["is_mc_personal_milf"] = False
        # sakari.event_triggers_dict["is_jealous"] = True
        # sakari.event_triggers_dict["has_skinny_dipped"] = False
        # sakari.event_triggers_dict["has_given_movie_bj"] = False
        # sakari.event_triggers_dict["has_fucked_at_store"] = False
        # sakari.event_triggers_dict["has_stripped_at_club"] = False
        # sakari.event_triggers_dict["had_kaya_threesome"] = False
        # sakari.event_triggers_dict["ophelia_teamup_started"] = False
        # sakari.event_triggers_dict["opehlia_teamup"] = False
        # sakari.event_triggers_dict["rebecca_teamup_started"] = False
        # sakari.event_triggers_dict["rebecca_teamup"] = False

        # In Kaya's event, we keep the variable for whether or not Sakari has died, since

        # sakari_intro = Action("sakari_intro",sakari_intro_requirement,"sakari_intro_label") #Set the trigger day for the next monday. Monday is day%7 == 0
        # mc.business.add_mandatory_crisis(sakari_intro) #Add the event here so that it pops when the requirements are met.

        # set relationships
        town_relationships.update_relationship(sakari, kaya, "Daughter", "Mother")
        # town_relationships.update_relationship(nora, sakari, "Friend")
        # town_relationships.update_relationship(lily, sakari, "Rival")

        sakari.text_modifiers.append(maori_accent)

        return

#Requirement Functions
init 3 python:
    def sakari_intro_requirement(the_person):
        return False

    sakari_intro = Action("See Sakari at Clothing Store", sakari_intro_requirement, "sakari_intro_label")

#Story Labels
label sakari_intro_label(the_person):
    "You wander into the clothes store at the mall. You walk in without any specific purpose and decide to do some people watching."
    "As you walk around, you notice a familiar face, talking to a couple employees."
    $ the_person.draw_person()
    the_person "Set the new line up front, with the displays, and see if we can get some interest in that."
    "It's [the_person.title], [kaya.possessive_title]'s mom. She seems to be giving instructions?"
    "?????" "Okay, what do you want done with the product up there?"
    the_person "We need to clearance it out. It's been up for far too long."
    "One of the other workers speaks up."
    "It's good to have you around running things again, [the_person.fname]"
    the_person "Ah, believe me it is good to be back."
    "The employees grab a couple boxes of merchandise and set off with it."
    "Alone now, [the_person.possessive_title] looks up and notices you. She seems a little out of breath."
    the_person "Ah, is that [the_person.title]?"
    mc.name "It is. I am surprised to see you."
    the_person "Ah, well I was feeling a bit better, and I hadn't been into the store in such a long time."
    the_person "Business has not been going well while I've been out sick."
    "You suddenly make the connection with the name of the clothing store."
    mc.name "Wait, you own [clothing_store.name]?"
    the_person "Indeed. For now, anyway..."
    "Something about the way she said that is unsettling. Didn't [kaya.title] say she was getting sicker?"
    mc.name "So, you are feeling better this week?"
    the_person "Yes, feeling better is a good way to say that."
    "It's obvious from the way she is saying it that she is hiding something, but you decide for now to let it go."
    mc.name "I'm sure [kaya.fname] will be glad to hear that you are at the store. She is very worried about you."
    $ the_person.draw_person(emotion = "sad")
    the_person "Yes, my dear [kaya.fname]..."
    if kaya.is_girlfriend:
        the_person "You are taking good care of her, right? She talks about you... a LOT."
        mc.name "Of course."
    else:
        the_person "You know... she sure talks about you... a LOT."
    "[the_person.possessive_title] mumbles something under her breath for a moment."
    the_person "Daughter... she doesn't know I'm here, working."
    "You glance at the time. This is when she would normally be in class."
    mc.name "I'm guessing you would like to keep it that way?"
    the_person "Never, EVER lie to my girl... but if she doesn't ask you, there's no need to tell her."
    the_person "She is certain to discover eventually, but on days I have the energy, I will be here in the morning to work."
    "An employee walks over, clearly looking for [the_person.title]."
    the_person "Ah, I need to get back to work. if you'll excuse me."
    mc.name "Certainly."
    $ the_person.change_job(clothing_cashier_job, job_known = True)
    $ the_person.set_schedule(None, the_times = [1,2,3]) # Free roam
    $ the_person.add_unique_on_room_enter_event(sakari_coffee_break)
    $ clear_scene()
    return


label sakari_coffee_break_label(the_person):
    "You swing by the clothing store and see that [the_person.possessive_title] is working this morning."
    $ the_person.draw_person()
    "Looks like she is changing out some price tags on some items. She looks tired."
    mc.name "Good day, [the_person.title]."
    the_person "To you as well, [the_person.mc_title]."
    mc.name "Care to take a break? I could go get us a couple coffees."
    the_person "That is very kind of you. Would you mind though, I would prefer hot tea?"
    "This is the first chance you've gotten to actually sit down with [the_person.title], so you jump at the chance."
    mc.name "I think I can manage that. How do you take it?"
    the_person "Plain, thank you."
    "You excuse yourself and walk into the mall, getting you and [the_person.possessive_title] drinks."
    $clear_scene()
    "You head to the generic branded coffee shop and order your drinks."
    "Before you walk back to the clothes store, you consider using the opportunity to give [the_person.title] a serum in her drink..."
    call give_serum(the_person) from _call_give_sakari_serum_coffee_01

    "You walk back to the clothing store, drinks in hand."
    $ the_person.draw_person()
    the_person "Ah, good timing. I just finished with this task."
    the_person "I have a small office, let's sit in there for a bit."
    mc.name "Sounds good. Lead the way!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.title] leads you to the back of the store and into a small office."
    "She sits down at a small desk and motions for you to sit across from her. You step in the office and sit down, leaving the door open."
    $ the_person.draw_person(position = "sitting")

    the_person "Lately, we've been getting to know each other better, so I wanted to make sure you understand what is going on with me."
    if kaya.is_girlfriend:
        the_person "Especially since you are so close with [kaya.fname]... my dear daughter..."
    the_person "I have an illness called myeloma. It is a type of recurring blood cancer."
    the_person "The prognosis is terminal, and unfortunately I have entered the final stage of the illness."
    mc.name "Ah [the_person.title]. I'm so sorry..."
    the_person "There are many experimental treatments... and unfortunately they have all failed."
    the_person "I recently decided to go off all treatments. I'm feeling much better, but it will only be a short term thing."
    mc.name "Ah, so that's why you have been back at the store a bit."
    the_person "Yes. I want to leave things ready... for [kaya.fname]."
    the_person "The last estimate I heard, was one to three months..."

    "There is a long silence as you soak in the information you just learned."

    the_person "I don't want you to misunderstand. I've enjoy getting to know you, but I understand if you don't want to spend time with someone who is not going to be around much longer."
    mc.name "What do you mean?"
    the_person "I just mean... don't feel like you HAVE to come here to the store and spend with an old lady like me."
    the_person "Your time is better spent with someone closer to your age..."
    mc.name "I see what you are saying [the_person.title], but I don't see it the same way."
    the_person "Oh?"
    mc.name "Spending my time with someone who doesn't have much time left could provide very interesting perspective."
    mc.name "Sometimes, when faced with mortality, it makes it easier to focus on what is truly important and what isn't."
    the_person "A wise man are you?"
    mc.name "Maybe so. Or, maybe it's an ego thing."
    mc.name "I have to say, I've never been in this position before... especially since I lost my dad so suddenly..."
    $ the_person.draw_person(position = "sitting", emotion = "sad")
    the_person "Ahh, yes. It should not surprise me that your father's son turned out to be a good man also..."
    mc.name "I don't know if I'll be able to do a perfect job of it... but if I can make your final days more pleasant, I am happy to do so."
    $ the_person.change_love(3)
    $ the_person.draw_person(position = "sitting", emotion = "happy")
    the_person "That is very kind of you, [the_person.mc_title]."

    "After a few more moments of silence, you decide to change topics."

    call small_talk_person(the_person, apply_energy_cost = False) from _call_small_talk_person_sakari_coffee_break

    the_person "Well, thank you for the tea. I feel refreshed! I think I'll try to get a little more work done today."
    $ the_person.draw_person()
    "You stand up with [the_person.possessive_title] and leave her small office."
    $ clear_scene()

    "The weight of your conversation sits heavy on your chest for a while."
    "You should decide, and fairly quickly. Do you want to spend more time with [the_person.possessive_title]?"
    "If you wait too long to decide, you might miss the opportunity completely."
    "Starbuck" "NOTE TO PLAYERS: [sakari.fname]'s max energy will decrease over time due to her sickness."
    "Starbuck" "Once it hits a low enough threshold, she will get removed from the game!"
    # $ ellie.add_unique_on_room_enter_event(nanobot_cure_ellie_inspiration)    #NOTE this is probably going to just be a new conversation option that opens up.
    $ mc.business.add_mandatory_crisis(sakari_business_proposition)
    $ mc.business.add_mandatory_crisis(sakari_goes_skinny_dipping)
    return

label sakari_business_proposition_label():    #mandatory event
    pass
    return

label sakari_business_partner_start_label():
    pass

    # $ mc.business.add_mandatory_crisis(sakari_goes_skinny_dipping)
    $ mc.business.add_mandatory_crisis(sakari_mc_booty_call_intro)
    return

label sakari_mc_booty_call_intro_label():     #Mandatory event
    pass
    return

label sakari_mc_booty_call_crisis_label():      #After the mandatory event, we add it to possible nighttime crisis events.
    pass
    return

label sakari_invites_mc_for_sleepover_label():  #mandatory event
    pass
    return

label sakari_kaya_move_in_label():          #Live in girlfriends still a WIP. come back to this later.
    pass
    return


#Sluttiness Labels

label sakari_goes_skinny_dipping_label():   #mandatory event
    $ the_person = sakari
    "As you are getting ready for bed, your phone vibrates. You are surpised by who it appears to be from."
    $ mc.start_text_convo(the_person)
    the_person "Hello [the_person.mc_title]. This is [sakari.fname], [kaya.fname]'s mother."
    "You didn't know she even had your number. Maybe she got it from [kaya.title]?"
    mc.name "Hello, how are you doing?"
    the_person "Good. I've been thinking a lot about what you said. You know, about mortality giving you a fresh perspective on things."
    the_person "There's something I've always wanted to do, but never had the chance. Can you meet me downtown in a bit?"
    "Wow. It's pretty late, but you are intrigued about what she has in mind."
    mc.name "Sure. Should I bring anything?"
    the_person "No. Meet me here."
    "The last message is followed up with an address. It is downtown close to the river."
    $ mc.end_text_convo()
    "You change back into your regular clothes, then head out."
    $ mc.change_location(downtown)
    "15 minutes later, you are downtown. Eventually, you spot [the_person.title] and walk up to her."
    $ the_person.draw_person()
    mc.name "Good evening [the_person.title]."
    the_person "Ah, good evening [the_person.mc_title]."
    mc.name "Mind telling me what we are up to tonight?"
    the_person "Like I told you earlier, there is something I have always wanted to do... and there is no time like the present."
    the_person "But I need help, "


    return

label sakari_goes_to_the_movies_label():
    pass
    return

label sakari_fuck_at_clothing_store_label(the_person):  #room enter event
    pass
    return

label sakari_dances_at_strip_club_intro_label(the_person):  #room_enter_event
    pass
    return

label sakari_dances_at_strip_club_label():      #mandatory event.
    pass
    return

label sakari_share_mc_during_sleepover_label(): #Mandatory event
    pass
    return


#Sakari cure storyline  - Eventually pull these labels out of this file and into a new one, but adding a new file named "sakari cure" would be spoiler, so for now leave it buried here
#Starts with MC talking to Ellie about Nanobots. during a nighttime mandatory crisis MC realizes nanobots could be used to target Sakari's sickness.
#First prototype kills lab rats because bots are either too effective and flood the system with dead cells, or not effective enough and the illness comes back
#Second phase create a new serum type to combat the effects of the necrosis of the nanobot tech
#Put both together into a serum and it will cure sakari if she is given sufficient doses.

#Start race for the cure storyline###
label nanobot_cure_ellie_inspiration_label(the_person):  #On room enter event.
    pass
    return

label nanobot_cure_mc_nighttime_plans_label():  #Mandatory night crisis
    pass
    return

label nanobot_cure_plan_stage_one_label(the_person):    #ellie on talk event
    pass
    return

label nanobot_cure_ask_sakari_for_blood_label(the_person):  #Sakari on talk event
    pass
    return

label nanobot_cure_start_IT_project_label(the_person):  #Ellie on room enter event.
    pass
    return

label nanobot_cure_setup_stage_one_test_label():    #Mandatory event
    pass
    return

label nanobot_cure_plan_stage_two_label():     #Mandatory event
    pass
    return

label nanobot_cure_start_serum_research_label(the_person): #room enter event with head researcher.
    pass
    return

label nanobot_cure_kaya_stays_late_label(the_person):   #Room enter. if Kaya is in research she stays late to keep researching cure for her mother.
    pass
    return

label nanobot_cure_serum_complete_label(): #mandatory event
    pass
    return

label nanobot_cure_setup_stage_two_test_label():    #mandatory event
    pass
    return

label nanobot_cure_give_serum_to_sakari_label():
    pass
    return

label nanobot_cure_sakari_recurring_treatment_label():
    pass
    return

label nanobot_cure_complete_label():
    pass
    return

#End race for the cure storyline###

#Race for the cure failure labels

label sakari_is_in_hospital_label():
    pass
    return

label sakari_is_in_hospice_label():
    pass
    return

label sakari_has_passed_label():
    pass
    return

#Story wrappers
init 3 python:
    def sakari_is_sick():
        return sakari.event_triggers_dict.get("is_sick", False)

    def sakari_intro_complete():
        return sakari.event_triggers_dict.get("intro_complete", False)

    def sakari_mc_knows_sick():
        return sakari.event_triggers_dict.get("mc_knows_sick", False)

    def sakari_offered_mc_partner():
        return sakari.event_triggers_dict.get("mc_offered_partner", False)

    def sakari_mc_are_partners():
        return sakari.event_triggers_dict.get("mc_is_partner", False)

    def sakari_mc_is_booty_call():
        return sakari.event_triggers_dict.get("mc_is_booty_call", False)

    def sakari_is_mc_personal_milf():
        return sakari.event_triggers_dict.get("is_mc_personal_milf", False)

    def sakari_is_jealous():
        return sakari.event_triggers_dict.get("is_jealous", True)

    def sakari_has_skinny_dipped():
        return sakari.event_triggers_dict.get("has_skinny_dipped", False)

    def sakari_has_given_movie_bj():
        return sakari.event_triggers_dict.get("has_given_movie_bj", False)

    def sakari_has_fucked_at_store():
        return sakari.event_triggers_dict.get("has_fucked_at_store", False)

    def sakari_has_stripped_at_club():
        return sakari.event_triggers_dict.get("has_stripped_at_club", False)

    def sakari_has_had_kaya_threesome():
        return sakari.event_triggers_dict.get("had_kaya_threesome", False)

    def sakari_has_died():
        return kaya.event_triggers_dict.get("sakari_has_died", False)

#Sakari other functions
