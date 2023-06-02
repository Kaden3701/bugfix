# Camilla's Notes:
# A faithful wife, whose husband, the bartender, has requested she adopt the hotwife lifestyle.
# Camilla is also the lifestyle coach at the mall during the day, who helps MC set and prioritize goals.
# In her love story, she is introduced to Alexia as a means of taking lewd photos for company advertisements.
# In Nora's love story, Nora is introduced to Camilla to help her come up with life goals as she flounders with meaning and purpose in her job
#
# Camilla's current major flaws:
# There isn't a good way to increase her stats. Her only chance of getting serums is at the bar, with no useful time slot after.
# Come up with a new method for either being able to increase her stats during that scene, or give an alternate dosing method.




#Init  functions
init 2 python:
    list_of_instantiation_functions.append("create_camilla_character")

    camilla_wardrobe = wardrobe_from_xml("Camilla_Wardrobe")

    def create_camilla_character():
        camilla_wardrobe = wardrobe_from_xml("Camilla_Wardrobe")
        camilla_base_outfit = Outfit("camilla's base accessories")
        the_makeup = blush.get_copy()
        the_makeup.colour = [.65, .23, .17, 0.75]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [.26, .21, .14, 0.33]
        the_rings = copper_ring_set.get_copy()   #Change this
        copper_ring_set.colour = [.95,.95,.78,1.0]
        camilla_base_outfit.add_accessory(the_makeup)
        camilla_base_outfit.add_accessory(the_lipstick)
        camilla_base_outfit.add_accessory(the_rings)

        # init camilla role
        global camilla_role
        camilla_role = Role(role_name ="camilla", actions =[camilla_get_a_drink, camilla_go_dancing, camilla_take_pics, camilla_home_sex], hidden = True)
        camilla_job = Job("Lifestyle Coach", camilla_role, mall, work_times = [1,2])

        #global camilla_role
        global camilla
        camilla = make_person(name = "Camilla", last_name ="Rojas", body_type = "thin_body", age = 34, face_style = "Face_2",  tits="D", height = 0.98, hair_colour="golden blonde", hair_style = braided_bun, skin="tan" , \
            personality = introvert_personality, name_color = "#DAA520", starting_wardrobe = camilla_wardrobe, job = camilla_job, \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [4,2,2,2], sluttiness = 7, obedience_range = [70, 85], happiness = 119, love = 0, \
            relationship = "Married", kids = 0, force_random = True, base_outfit = camilla_base_outfit, type = 'story',
            forced_opinions = [["dancing", 2, True], ["fashion", 2, False], ["flirting", 1, False], ["working", 1, False], ["the colour purple", 2, False], ["dresses", 2, False], ["the colour blue", -2, False], ["skirts", 1, False]],
            forced_sexy_opinions = [["being submissive", 2, False], ["getting head", 2, False], ["drinking cum", 1, False], ["giving blowjobs", 2, False], ["public sex", 1, False], ["showing her ass", 2, False], ["anal sex", -2, False], ["bareback sex", 2, False], ["doggy style sex", 1, False]])

        camilla.add_role(lifestyle_coach_role)
        camilla.generate_home()
        camilla.home.add_person(camilla)
        camilla.set_schedule(downtown_bar, the_times = [3])


        # camilla_mod_initialization():
        # camilla.event_triggers_dict["intro_complete"] = False    # True after first talk
        # camilla.event_triggers_dict["get_drinks"] = False
        # camilla.event_triggers_dict["go_dancing"] = False
        # camilla.event_triggers_dict["take_pics"] = False
        # camilla.event_triggers_dict["will_fuck"] = False
        # camilla.event_triggers_dict["her_place"] = False
        # camilla.event_triggers_dict["outfit_help"] = False
        # camilla.event_triggers_dict["lingerie_help"] = False
        # camilla.event_triggers_dict["formal_date"] = False
        # camilla.event_triggers_dict["lost_anal_virginity"] = False
        # camilla.event_triggers_dict["boudoir_stage"] = 0
        camilla.fertility_percent = -1000.0 #She's infertile

        camilla_intro = Action("camilla_intro",camilla_intro_requirement,"camilla_intro_label")
        camilla.add_unique_on_room_enter_event(camilla_intro)
        return

init -1 python:
    #Requirement Functions

    def camilla_intro_requirement(person):
        if person.location == mall: # only trigger event when at the mall
            return True
        return False

    def camilla_spot_at_bar_requirement(the_person):
        if the_person.location == downtown_bar:
            return True
        return False

    def add_camilla_spot_at_bar_action():
        camilla_spot_at_bar = Action("Camilla at the bar", camilla_spot_at_bar_requirement, "camilla_spot_at_bar_label")
        camilla.add_unique_on_room_enter_event(camilla_spot_at_bar)
        return


#Additional Camilla Functions
init 2 python:
    def camilla_wear_salsa_dress():
        salsa_dress = camilla.wardrobe.get_outfit_with_name("Camilla Sexy Salsa Outfit")
        if salsa_dress:
            camilla.apply_outfit(salsa_dress)
        return

    def get_camilla_lingerie_set_white():
        outfit = Outfit("Lingerie Set Classic White")
        outfit.add_upper(teddy.get_copy(),colour_white)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_white)
        outfit.add_feet(high_heels.get_copy(), colour_white)
        return outfit

    def get_camilla_lingerie_set_pink():
        outfit = Outfit("Pink Lingerie")
        outfit.add_upper(teddy.get_copy(),colour_pink)
        outfit.add_feet(garter_with_fishnets.get_copy(), colour_pink)
        outfit.add_feet(high_heels.get_copy(), colour_pink)
        return outfit

label camilla_intro_label(the_person):
    $ scene_manager = Scene()
    "You decide to wander aimlessly around the mall for a bit. You do a bit of people watching and generally enjoy the time to yourself."
    "As you walk around, you spot a kiosk that catches your attention."
    "Lifestyle Coaches: We help you set and achieve long term and short term goals!"
    "You walk around the kiosk a bit, there are all kinds of testimonials and adverts up for the service."
    the_person "Hello there! I'm [the_person.fname]."
    $ scene_manager.add_actor(the_person)
    mc.name "I'm [mc.name]."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("Your lifestyle coach")
    $ the_person.set_mc_title(mc.name)
    the_person "Nice to meet you! I'm a lifestyle coach, here to help people achieve their dreams!"
    "The sales pitch is a little... optimistic? But to be honest, she is pretty good looking, so you decide to let her continue."
    the_person "I've personally helped all kinds of people achieve all kinds of things, from giving up drugs, to losing a few pounds!"
    the_person "Our first consultation is free. Would you be interested?"
    "What the hell. It couldn't hurt anything, right?"
    mc.name "I suppose."
    "You sit down with [the_person.title]. She asks you some generic questions about your personal and work life."
    "You explain that you are a small business owner, working with pharmaceuticals, leaving out some of the details."
    "You share some of your basic short term, and a few long term goals, both for your business and for yourself, personally."
    the_person "I see. Those sound like interesting goals! Might I offer a few alternatives also?"
    mc.name "Sure."
    $ hide_ui()
    call screen lifestyle_goal_sheet()
    $ show_ui()
    the_person "I hope that was helpful! Come back again and see me if you want to adjust your goals again in the future!"
    mc.name "I think it was. I'll be sure to check back with you again if I need to. Thanks!"
    $ the_person.event_triggers_dict["met"] = 1
    $ scene_manager.clear_scene()
    $ add_camilla_spot_at_bar_action()
    return

label camilla_spot_at_bar_label(the_person):
    "As you walk into the bar, you take a look around."
    $ the_person.draw_person(position = "sitting")
    "Sitting at the bar by herself, you notice [the_person.title], the lifestyle coach from the mall."
    "You are surprised a woman as pretty as her is sitting by herself at the bar, so you decide to go say hi."
    "She notices you as you walk up to her."
    mc.name "Hello [the_person.title]. Out for a drink this evening?"
    the_person "Hello... [the_person.mc_title] was it?"
    mc.name "Excellent memory. Yes I worked with you some at the mall the other day."
    the_person "Yes, I remember. The small business owner."
    mc.name "I noticed you at the bar by yourself. Mind if I sit with you for a while?"
    the_person "That's fine."
    "You sit down in a bar stool next to [the_person.possessive_title]."
    mc.name "So how long have you been working as a lifestyle coach?"
    the_person "Honestly, not too long. I mainly just do it as an extra source of income to supplement what my hubby brings in."
    "Ah, so she is married. You should probably keep things low key for now."
    mc.name "That's admirable. How long have you been married?"
    the_person "Almost 15 years now."
    mc.name "Wow, you don't look like someone who has been married 15 years!"
    the_person "Ah, we got married young."
    mc.name "Kids?"
    "[the_person.title] hesitates. You might have hit a sore subject with her..."
    the_person "No, no niños..."
    mc.name "I'm sorry... I'm probably getting a little personal."
    "You make a mental note that she doesn't have any kids"
    the_person "It's okay, that's a perfectly normal question to ask."
    "You feel bad. You notice that her glass is almost empty. You wave down the bartender. When he walks over, he smiles wide at [the_person.title]."
    "?????" "Something I can get for you?"
    mc.name "Can I get a beer and another for my friend?"
    "?????" "Sure. A beer and another paloma for the lovely miss [the_person.last_name]."
    "The bartender walks off. He seems to know [the_person.title]. She must be a regular here?"
    mc.name "Ah, you come here often then?"
    the_person "I do. I'm here most evenings. I like to have a drink before I head home each night. My husband works late."
    mc.name "I see. I'm here somewhat often as well. Maybe we could have a drink together once in a while?"
    the_person "I... I suppose that would be alright."
    "You sit back in the chair and chat with [the_person.possessive_title] for a while. You both enjoy the time together, getting to know one another as friends."
    $ the_person.change_love(3)
    $ mc.business.change_funds(-20)
    "Eventually you settle up with the bartender. You notice him gesture at [the_person.title] when she isn't looking, and gives you a little wink."
    "You aren't sure... is he trying to say she's... available? Maybe since her husband works late she picks up guys at the bar..."
    "You file it away in your brain. Maybe you could come back and have drinks with her again. A bar would be an ideal place to dose her with a few serums too..."
    "You get up and say goodbye to [the_person.possessive_title]."
    mc.name "Thank you for the conversation. I'll see you around [the_person.title]."
    the_person "Take care [the_person.mc_title]."
    "You can now have drinks with [the_person.title] at the bar in the evenings."
    $ camilla.add_unique_on_room_enter_event(camilla_outfit_help)
    $ camilla.add_unique_on_room_enter_event(camilla_obedience_new_goals)
    $ camilla.set_event_day("obedience_event")
    $ camilla.set_event_day("love_event")
    $ camilla.set_event_day("slut_event")
    $ camilla.set_event_day("story_event")
    $ camilla.event_triggers_dict["bar_met"] = True
    call advance_time from _call_advance_camilla_meet_at_bar_first_time_01
    return

init -1 python:
    def mc_dancing_skill(): #Wrapper for measuring MC's progress learning to salsa dance.
        return mc.charisma + __builtin__.round((mc.max_energy - 100) / 20)

    def camilla_is_fertile():   #Just make this a function name. Can come back and make the method once we decide triggers for making her fertile.
        return False
