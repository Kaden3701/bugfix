init 1 python:
    def generate_premade_list():
        global list_of_premade_characters
        list_of_premade_characters = []
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=1.035, skin="tan", tits="DD",hair_colour="chestnut",hair_style=messy_hair,type="premade")) #original height = 0.99
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=1.05, skin="white", tits="B",hair_colour="chestnut",hair_style=messy_hair,type="premade")) #original_height = 1
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=0.99, skin="white", tits="DD",hair_colour="brown",hair_style=twintail,type="premade")) #original height = 0.96
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.99, skin="white", tits="DD", hair_colour="chestnut",hair_style=messy_hair,type="premade")) #original height = 0.96
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=0.93, skin="tan", tits="B", hair_colour="black", hair_style=ponytail,type="premade")) #original height = 0.92
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.90, skin="white", tits="DD", hair_colour="blond", hair_style=messy_hair,type="premade")) #original height = 0.9
        list_of_premade_characters.append(create_random_person(body_type = "curvy_body", height=1.05, skin="white", tits="DD", hair_colour="chestnut", hair_style=messy_hair,type="premade")) #original height = 1.0
        list_of_premade_characters.append(create_random_person(body_type = "thin_body", height=0.96, skin="white", tits="FF", hair_colour="blond", hair_style=long_hair,type="premade")) #oriignal_height = 0.94
        list_of_premade_characters.append(create_random_person(body_type = "standard_body", height=0.975, skin="tan", tits="FF", hair_colour="brown", hair_style=ponytail,type="premade")) #original height = 0.95

    def generate_patreon_character_list():
        global list_of_patreon_characters
        # Patron reward characters! #
        list_of_patreon_characters = []

        #original height 0.99
        dinah_wardrobe = wardrobe_from_xml("Dinah_Wardrobe")
        person_dinah = create_random_person(name = "Dinah", last_name = "Midari", body_type = "standard_body", height=1.035, skin="black", tits="D", hair_colour="black", hair_style=short_hair, starting_wardrobe = dinah_wardrobe,type="unique")
        list_of_patreon_characters.append(person_dinah)

        #original height 0.96
        sylvia_wardrobe = wardrobe_from_xml("Sylvia_Wardrobe")
        person_sylvia = create_random_person(name = "Sylvia", last_name = "Weissfeldt", body_type = "curvy_body", height=0.99, skin="white", tits="C", hair_colour="blond", hair_style = long_hair, starting_wardrobe = sylvia_wardrobe,
            personality = reserved_personality,type="unique")
        list_of_patreon_characters.append(person_sylvia)

        #original height 0.98
        paige_wardrobe = wardrobe_from_xml("Paige_Wardrobe")
        # Well educated and raised in a very middle-class family.
        # Paige is a cool-headed young woman who has confidence without exuberance or extraversion.
        # her favourite activities are generally calm and solitary: reading, playing musical instruments, watching TV, etc.
        # She doesn't make friends quickly, but she is pleasant and easy to get along with, and the bonds she does cultivate are likely to last for life.
        # She has no passion for her work, but she is good at it and takes pride in that fact.
        person_paige = create_random_person(name = "Paige", last_name = "Sallow", body_type = "thin_body", height = 1.02, skin = "white", tits="A", hair_colour="brown", hair_style = messy_ponytail, starting_wardrobe = paige_wardrobe,
            personality = reserved_personality, job = electronics_support_job, stat_array = [1,4,3], skill_array = [5,1,2,3,2], sex_skill_array = [2,1,4,2],type="unique")
        list_of_patreon_characters.append(person_paige)

        #original height 0.94
        kendra_wardrobe = wardrobe_from_xml("Kendra_Wardrobe")
        # Kendra's family owns one of the largest pharmaceutical companies in the country. All of the Rivera children went to the finest prep schools.
        # Unlike her siblings, Kendra didn't inherit her parent's good looks or their general attitudes. She also disagreed with her families' viewpoint that being rich makes you better than everyone else.
        # This point of view put her at odds with everyone in her social class so she mostly hung out with the outcasts of her school.
        # By the time Kendra turned 16, she had grown into a stunningly beautiful woman and enjoyed the newfound attention she was receiving from boys. She was a free spirit, who just wanted to enjoy life.
        # When she graduated High School, she decided that college was not for her and pursued a career as glamor model. Kendra's parents were not pleased and cut her off financially but Kendra didn't care.
        # She was ready to be free and live her life.
        person_kendra = create_random_person(name = "Kendra", last_name = "Rivera", age = 18, body_type = "curvy_body", height = 0.96, skin = "tan", hair_colour = "chestnut", hair_style = shaved_side_hair, starting_wardrobe = kendra_wardrobe,
            personality = relaxed_personality, stat_array = [4,3,1], skill_array = [5,3,1,2,2], sex_skill_array = [2,2,4,1], face_style = "Face_4",type="unique")
        list_of_patreon_characters.append(person_kendra)

        #original height 1.00
        svetlanna_wardrobe = wardrobe_from_xml("Svetlanna_Wardrobe")
        # Svetlanna moved to the fictional city from a fictional Russian land at the age of 16. She was always fascinated with biochemistry and when her mother became ill, she dove even deeper into her studies.
        # After graduating from public education, she immediately moved to higher studies. She was hell-bent to learn all she could to help her mother.
        # Unfortunately, her mother died before Svetlanna could find a cure for her mysterious disease, which put her into a deep depression.
        # After some time, she met a woman that rekindled her love for biotechnology and put her on the path of a wild woman, never tied down with any one man or woman.
        person_svetlanna = create_random_person(name = "Svetlanna", last_name = "Ivanova", body_type= "thin_body", height = 1.05, skin = "white", tits="E", hair_colour = "blond", hair_style = long_hair, starting_wardrobe = svetlanna_wardrobe,
            personality = wild_personality, job = waitress_job, stat_array = [3,1,4], skill_array = [1,3,5,2,2], sex_skill_array = [2,1,2,4],type="unique")
        person_svetlanna.set_opinion("research work", 2, False) #Always loves research work # Patron reward
        list_of_patreon_characters.append(person_svetlanna)

        #original height 0.98
        kelly_wardrobe = wardrobe_from_xml("Kelly_Wardrobe")
        #
        person_kelly = create_random_person(name = "Kelly", last_name = "Uhls", body_type = "curvy_body", height = 1.02, skin = "white", eyes = "dark blue", tits = "E", hair_colour = "chestnut", hair_style = ponytail, starting_wardrobe = kelly_wardrobe,
            personality = reserved_personality, stat_array = [2,2,4], skill_array = [2,1,2,1,5], sex_skill_array = [3,4,2,1],type="unique")
        list_of_patreon_characters.append(person_kelly)

        #original height 0.90
        #sativa_wardrobe = wardrobe_from_xml("Sativa_Wardrobe") #TODO: Give her a wardrobe if the patron responds
        # Sativa's parents are very strict and traditional. They were determined to protect her from all the bad things in life, such as boys and booze.
        #When she turned 18,  Sativa moved out on her own.  Now she is determined to experience everything that she was previously denied.
        person_sativa = create_random_person(name = "Sativa", last_name = "Menendez", body_type = "curvy_body", face_style = "Face_7", height = 0.90, skin = "tan", eyes = "green", tits = "FF", hair_colour = "black", hair_style = bobbed_hair,
            personality = wild_personality, job = unemployed_job, stat_array = [3,1,4], skill_array = [2,2,1,1,5], sex_skill_array = [4,3,2,1],type="unique")
        list_of_patreon_characters.append(person_sativa)

        #original height 0.96
        #nuoyi_wardrobe = wardrobe_from_xml("Nuoyi_Wardrobe") #NOTE: Patron did not want a specific wardrobe, she'll draw her wardrobe randomly as normal.
        person_nuyoi = create_random_person(name = "Nuoyi", last_name = "Pan", body_type = "thin_body", height = 0.99, skin = "white", eyes = "dark blue", tits = "FF", hair_colour = "black", hair_style = long_hair,
            personality = wild_personality, job = bartender_job, stat_array = [4,3,1], skill_array = [5,2,2,1,1], sex_skill_array = [1,3,4,2],type="unique")
        list_of_patreon_characters.append(person_nuyoi)

        #original height 0.94
        lynn_wardrobe = wardrobe_from_xml("Lynn_Wardrobe")
        # An exchange student who is doing a year abroad at a Catholic school. Especially to get away from her helicopter parents.
        person_lynn = create_random_person(name = "Lynn", last_name = "Borch", body_type = "thin_body", height = 0.96, age = 19, skin = "white", eyes = "brown", tits = "C", hair_colour = "brown", hair_style = long_hair, starting_wardrobe = lynn_wardrobe,
            personality = introvert_personality, job = student_job, stat_array = [1,3,4], skill_array = [1,2,1,5,2], sex_skill_array = [2,1,5,1],type="unique")
        person_lynn.set_opinion("cheating on men", -2, False) #Always hates cheating on men, you don't know this
        list_of_patreon_characters.append(person_lynn)

        #original height 0.95
        # Olga is a young library employee who likes to dress colorfully and is childish by behavior.
        # As if she wants to overplay something.
        olga_wardrobe = wardrobe_from_xml("Olga_Wardrobe")
        person_olga = create_random_person(name = "Olga", last_name = "Schaad", body_type = "standard_body", height = 0.975, skin = "tan", eyes = "green", tits = "E", hair_colour = "blond", hair_style = messy_ponytail, starting_wardrobe = olga_wardrobe,
            personality = wild_personality, stat_array = [4,1,3], skill_array = [2,5,2,1,1], sex_skill_array = [2,4,1,1],type="unique")
        person_olga.set_opinion("working", 1, False) #Always likes working, you don't know this
        list_of_patreon_characters.append(person_olga)

        #original height 0.92
        # Svenja wants to become a fashion designer; she dropped out of college to do so and started working in a fashion boutique. She is 18 years old.
        # svenja_wardrobe = wardrobe_from_xml("Svenja_Wardrobe") #NOTE: Patron did not want a specific wardrobe, she'll draw her wardrobe randomly as normal.
        person_svenja = create_random_person(name = "Svenja", last_name = "Beitel",  body_type = "standard_body", height = 0.93, skin = "white", eyes = "dark blue", tits = "B", hair_colour = "blond", hair_style = ponytail,
            personality = wild_personality, job = salon_hairdresser_job, stat_array = [3,1,4], skill_array = [1,3,1,5,1], sex_skill_array = [3,4,1,1], type="unique")
        list_of_patreon_characters.append(person_svenja)

        # anna_wardrobe = wardrobe_from_xml("Anna_Wardrobe") #NOTE: Patron did not provide a specific wardrobe; she'll draw from the default pool.
        person_anna = create_random_person(name = "Anna", last_name = "Kostenko", body_type = "thin_body", height = 0.93, skin = "white", eyes = "light blue", tits = "A", hair_colour = "blond", hair_style = ponytail,
            personality = introvert_personality, job = yoga_teacher_job, age = 25, stat_array = [1,3,4], skill_array = [1,1,3,3,5], sex_skill_array = [1,3,4,1], type = "unique")
        list_of_patreon_characters.append(person_anna)

    def generate_random_characters(max_num_of_random):
        def create_a_new_character(job = None):
            person = make_person(job = job, force_random = True)
            person.generate_home().add_person(person)

        if not max_num_of_random == 0:
            # make sure we have at least one person for each specific jobs (including critical jobs)
            for job in [x[0] for x in list_of_jobs if len(people_with_job(x[0])) == 0]:
                create_a_new_character(job = job)

    def add_stripclub_strippers():
        for i in __builtin__.range(0, 4):
            create_stripper()

        # make one of the strippers an alpha-personality (simplifies stripclub story-line)
        alpha_stripper = get_random_from_list([x for x in stripclub_strippers if x.age >= 25 and not x.personality == alpha_personality])
        if alpha_stripper:
            change_personality(alpha_stripper, alpha_personality)
            alpha_stripper.charisma = 5
            alpha_stripper.int = 6
            alpha_stripper.update_opinion_with_score("taking control", 2, False)
            alpha_stripper.update_opinion_with_score("being submissive", -1, False)
        return
