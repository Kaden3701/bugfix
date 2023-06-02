#Camilla Teamups.

#planned teamups: Alexia is her main teamup. Starts with taking boudoir photos for her hubby, can end up taking them for MC
#If MC corrupts Camilla AND Alexia, have the option to have them both leave their SOs for MC at the same time.
#Alexia explores hotwifey lifestyle during team up. MC and encourage or discourage it.

#Boudoir photo stages:
# 1 - Sexy photos of both girls, Camilla talks a bit about hotwife lifestyle if alexia is dating
# 2 - Sexy photos. Ends with Camilla taking deepthroat, alexia disbelief she would "cheat". Give MC option to encourage hotwifing or encourage alexia to keep it secret.
# 3 - transition to 3 is decision time. Alexia gets turned on and blows MC. MC can start exerting pressure on her (you're mine while you're here) or encourage sharing
# 4 - Full on threesome. If MC exerting, girls talk about enjoying their MC time. If hotwifing, girls talk about getting reclaimed.
# 5 - Exerting - Convince girls to dump their SOs, commit to you. If hotwifing, option to have SOs watch the photo shoot.



init 1 python:
    def camilla_alexia_boudoir_intro_setup():   #Use this function to add the appropriate labels to the game for when boudoir photos can begin.
        if mc_business_has_expensive_camera() and alexia_is_model():
            alexia.add_unique_on_room_enter_event(camilla_alexia_boudoir_setup_intro)
        else:
            mc.business.add_mandatory_crisis(camilla_alexia_boudoir_setup_reminder)
        return

    camilla_alexia_boudoir_setup_reminder = Action("Boudoir Reminder", camilla_alexia_boudoir_setup_reminder_requirement, "camilla_alexia_boudoir_setup_reminder_label")
    camilla_alexia_boudoir_setup_intro = Action("Arrange photos with Alexia", camilla_alexia_boudoir_setup_intro_requirement, "camilla_alexia_boudoir_setup_intro_label")
    # camilla_alexia_boudoir_final_setup
    # camilla_alexia_boudoir_intro
    # camilla_alexia_boudoir_recur




#Requirement Functions
init -1 python:
    def camilla_alexia_boudoir_setup_reminder_requirement():
        if mc_business_has_expensive_camera() and alexia_is_model():
            if time_of_day == 2 and renpy.random.randint(0,100) < 30:
                return True
        return False

    def camilla_alexia_boudoir_setup_intro_requirement(the_person):
        return False



#Labels

label camilla_alexia_boudoir_setup_reminder_label():
    "While working in your office, you start daydreaming about some of your recent sexual adventures."
    "Suddenly, you remember [camilla.possessive_title], and your conversation about taking boudoir photos of her when you helped her pickup out some lingerie."
    "Recently, you purchased a camera and have started taking pictures with [alexia.title]. Maybe you could talk to her about doing them?"
    $ camilla_alexia_boudoir_intro_setup()
    return

label camilla_alexia_boudoir_setup_intro_label(the_person):
    mc.name "Hey [the_person.title]. Have a moment?"
    the_person "Uhh, sure [the_person.mc_title]."
    mc.name "You know how we take pictures of your for the ads to run, right?"
    the_person "Uhhh... yeah... hard to forget that..."
    mc.name "Well, I have a friend that I think would make a really good model. I was wondering if you would be willing to stay late one night and help me shoot some."
    the_person "Oh, like as the photographer?"
    mc.name "Exactly. I'd pay you overtime for it, of course."
    $ the_person.change_obedience(1)
    the_person "Oh man. I could really use the extra cash. What night were you thinking?"
    mc.name "I was thinking about Wednesday evenings, right after we close down."
    the_person "Okay. Are the pictures... are they going to be as risque as the ones I did?"
    mc.name "Definitely. Actually, they are kind of a favor to her, too. She wants to get some boudoir style pictures for her husband."
    the_person "Oh! She's married? And she's okay with... and he's okay with it too?"
    mc.name "He is actually very supportive."
    the_person "Okay. I'll do it. Just let me know what day you want to start, okay?"
    mc.name "Perfect. I'll talk to her and get back to you."
    $ clear_scene()
    "You let [the_person.title] go. You should talk to [camilla.title] and get the photoshoot finalized!"
    $ camilla.add_unique_on_talk_event(camilla_alexia_boudoir_final_setup)
    return

label camilla_alexia_boudoir_final_setup_label(the_person):
    mc.name "Hey [the_person.title]. Guess what!"
    the_person "What?"
    if (day % 7 != 2):
        mc.name "I have a photoshoot scheduled for you on Wednesday night."
    else:
        mc.name "I have a photoshoot schedule for you tonight!"
    $ the_person.change_happiness(5)
    the_person "Oh wow! That's incredible!"
    mc.name "Let me get you the address. It'll be at my business, and one of my marketing people will be doing the pictures with me."
    the_person "Sounds great!"
    "You give [the_person.possessive_title] the information on your business location and the timing."
    the_person "Okay, I'll be there! And I've got just the outfit for it!"
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] throws her arms around you and gives you a peck on the cheek."
    $ the_person.draw_person()
    the_person "See you there!"
    $ clear_scene()
    "Alright! You've got the time and place set for a sexy photoshoot!"
    $ mc.business.add_mandatory_crisis(camilla_alexia_boudoir_intro)
    return

label camilla_alexia_boudoir_intro_label():
    $ scene_manager = Scene()
    "It's Wednesday. The boudoir photoshoot with [camilla.possessive_title] and [alexia.title] is tonight!"
    if mc.is_at_work:
        "You finish up quickly with the last of your daily tasks before going to your office."
    else:
        "You head back to work and to your office to get ready."
    $ mc.change_location(ceo_office)
    "Shortly after, you hear a knock on your door."
    $ scene_manager.add_actor(alexia)
    alexia "Knock knock! Hey [alexia.mc_title]."
    "In her hands she has the company camera."
    mc.name "Come in! Come on in, I'm sure "


    return



#This label is seperated into three parts.
#In the intro portion, we basically talk about what we have done so far as a group.
#In the transition stage, we introduce what will be occuring during this session. If MC has unlocked the next tier of sluttiness stuff, we find out about it here.
#In the final stage, the sex act occurs.
label camilla_alexia_boudoir_recur_label(the_person):
    "It's Wednesday. The boudoir photoshoot with [camilla.possessive_title] and [alexia.title] is tonight!"
    if mc.is_at_work:
        "You finish up quickly with the last of your daily tasks before going to your office."
    else:
        "You head back to work and to your office to get ready."
    $ mc.change_location(ceo_office)


    return

# Teamup wrapper functions
init 2 python:
    def mc_business_has_expensive_camera():
        return mc.business.event_triggers_dict.get("has_expensive_camera",False)

    def alexia_is_model():
        return alexia == mc.business.company_model

    def alexia_has_flirty_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_flirt", False)
        return False

    def alexia_has_underwear_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_flash", False)
        return False

    def alexia_has_nude_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_naked", False)
        return False

    def alexia_has_blowjob_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_suck", False)
        return False

    def alexia_has_sex_ad():
        if alexia_is_model():
            return alexia.event_triggers_dict.get("camera_fuck", False)
        return False

    def camilla_boudoir_get_stage():
        return camilla.event_triggers_dict.get("boudoir_stage", 0)
