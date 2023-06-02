init 3 python:
    list_of_instantiation_functions.append("create_iris_character")

    def create_iris_character():
        ### IRIS ###
        #iris_wardrobe = wardrobe_from_xml("Iris_Wardrobe")
        iris_base = Outfit("Iris's accessories") #TODO: Decide what accessories we want her to haven

        influencer_job = Job("Influencer", critical_job_role, work_days = [], work_times = [])

        global iris
        iris = create_random_person(name = "Iris", last_name = "Vandenberg", age = 21, body_type = "thin_body", face_style = "Face_7", tits = "DD", height = 0.9, hair_colour = "blond", hair_style = twintail, pubes_style = shaved_pubes, skin = "white", \
            eyes = "green", personality = relaxed_personality, stat_array = [6,2,1], skill_array = [1,4,0,0,1], sex_skill_array = [4,4,0,0], job = influencer_job, \
            sluttiness = 5, obedience = 80, happiness = 120, love = 0, relationship = "Single", kids = 0, suggestibility_range = [6, 12],
            work_experience = 1)

        iris.add_role(instapic_role)
        iris.add_role(dikdok_role)
        iris.generate_home()
        iris.home.add_person(iris)
        iris.set_override_schedule(iris.home) #Hides her at home so she doesn't wander the city by accident.

        town_relationships.update_relationship(iris, emily, "Sister")
        town_relationships.update_relationship(iris, christina, "Mother", "Daughter")
        return
