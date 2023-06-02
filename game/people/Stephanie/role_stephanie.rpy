init 1 python:
    list_of_instantiation_functions.append("create_stephanie_character")

    def create_stephanie_character():
        ### STEPHANIE ###
        stephanie_wardrobe = wardrobe_from_xml("Stephanie_Wardrobe")

        steph_lab_assistant_job = Job("Lab Assistant", critical_job_role, job_location = university) #Job for Steph to technically have at the start of the game so her job title is set correctly.

        global stephanie
        stephanie = create_random_person(name = "Stephanie", age = 29, body_type = "standard_body", face_style = "Face_3",  tits="C", height = 0.96, hair_colour="brown", hair_style = messy_short_hair, skin="white" , \
            eyes = "brown", personality = stephanie_personality, name_color = "#cf3232", dial_color = "#cf3232" , starting_wardrobe = stephanie_wardrobe, \
            stat_array = [3,6,5], skill_array = [1,1,6,2,1], sex_skill_array = [3,4,2,1], sluttiness = 14, obedience = 112, happiness = 119, love = 7, \
            title = "Stephanie", possessive_title = "Your friend", mc_title = mc.name, relationship = "Single", kids = 0,
            work_experience = 3,type="story")
        stephanie.generate_home().add_person(stephanie)

        global steph_role
        steph_role = Role("Stephanie", [], hidden = True) #Used to hold any Stephanie specific actions not tied to another role, and to guarantee this is Steph even if she undergoes a personality change.
        stephanie.add_role(steph_role)
        stephanie.change_job(steph_lab_assistant_job)

        # make sure she has no opinion on conservative outfits (affects happiness)
        if "conservative outfits" in stephanie.opinions:
            del stephanie.opinions["conservative outfits"]

        stephanie.set_opinion("kissing", 1, False)  # she likes kissing
        stephanie.set_opinion("vaginal sex", 2, False) # she likes having sex
        stephanie.set_opinion("research work", 2, True) #Steph always loves research work, which you know
        stephanie.set_opinion("small talk", 1, False)  # she likes small talk
        stephanie.set_opinion("flirting", 1, False)  # she likes flirting
        stephanie.set_opinion("threesomes", 1, False) # she likes threesomes

        #Setup Stephanie's storylines from the beginning, since she is a starting character.
        stephanie.set_event_day("obedience_event")
        stephanie.set_event_day("love_event")
        stephanie.set_event_day("slut_event")
        stephanie.set_event_day("story_event")
        add_stephanie_tennis_intro_action()
        add_stephanie_at_the_bar_intro_action()
        stephanie.set_schedule(downtown_bar, the_days = [2,4], the_times = [4])
