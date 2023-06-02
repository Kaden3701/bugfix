init -2 python:
    class Person(): #Everything that needs to be known about a person.
        #Define "private" range limits, use static/class methods to retrieve from the Person class
        _final_stat_floor = 0
        _initial_stat_floor = 1
        _initial_stat_ceiling = 5

        _final_skill_floor = 0
        _initial_skill_floor = 1
        _initial_skill_ceiling = 5

        _final_sex_skill_floor = 0
        _initial_sex_skill_floor = 1
        _initial_sex_skill_ceiling = 5

        _final_happiness_floor = 0
        _initial_happiness_floor = 90
        _initial_happiness_ceiling = 110

        _initial_suggestibility_floor = 0
        _initial_suggestibility_ceiling = 15

        _initial_sluttiness_floor = 0
        _initial_sluttiness_ceiling = 10

        _final_love_floor = -100
        _initial_love_floor = 0
        _initial_love_ceiling = 0
        _final_love_ceiling = 100

        _final_obedience_floor = 0
        _initial_obedience_floor = 90
        _initial_obedience_ceiling = 110

        _final_work_experience_floor = 1
        _initial_work_experience_floor = 1
        _initial_work_experience_ceiling = 3
        _final_work_experience_ceiling = 5

        _initial_age_floor = 18
        _initial_age_ceiling = 50
        _final_age_floor = 18
        _final_age_ceiling = 60
        _teen_age_ceiling = 19
        _old_age_floor = 40

        _height_step = 0.015 #1 inch
        _initial_height_floor =   ((5 * 12) +  0) * _height_step #5'  0"
        _initial_height_ceiling = ((5 * 12) + 10) * _height_step #5' 10"
        _final_height_floor =     ((4 * 12) +  0) * _height_step #4'  0"
        _final_height_ceiling =   ((7 * 12) +  0) * _height_step #7'  0"
        _short_height_ceiling =   ((5 * 12) +  3) * _height_step #5'  3"
        _tall_height_floor =      ((5 * 12) +  9) * _height_step #5'  9"

        _base_list_of_relationships = [["Single",120],["Girlfriend",50],["Fiancée",20],["Married",10]]

        _large_tit_minimum = "D"
        _huge_tit_minimum = "E"
        _small_tit_maximum = "C"
        _tiny_tit_maximum = "AA"

        _list_of_names = init_list_of_names()
        _list_of_last_names = init_list_of_last_names()
        _list_of_male_names = init_list_of_male_names()

        _coffee_list = [
            "just black",
            "just a little sugar",
            "one sugar",
            "two sugar",
            "lots of sugar",
            "just a splash of cream",
            "just some cream",
            "lots of cream",
            "cream and sugar"
        ]

        #These are "ideal" hair colours. Individuals will have minor variations applied to them so that different "blonds" have slightly different hair.
        _list_of_hairs = init_list_of_hairs()

        _list_of_skins = []
        _list_of_skins.append(["white",5])
        _list_of_skins.append(["black",1])
        _list_of_skins.append(["tan",2])

        _list_of_faces = init_list_of_faces() # Only character critical faces are included in all versions.

        _list_of_eyes = init_list_of_eyes()

        _list_of_tits = []
        _list_of_tits.append(["AA",5])
        _list_of_tits.append(["A",15])
        _list_of_tits.append(["B",30])
        _list_of_tits.append(["C",30])
        _list_of_tits.append(["D",15])
        _list_of_tits.append(["DD",10])
        _list_of_tits.append(["DDD",5])
        _list_of_tits.append(["E",2])
        _list_of_tits.append(["F",1])
        _list_of_tits.append(["FF",1])

        _list_of_clothing_colours = []
        _list_of_clothing_colours.append([0.15,0.15,0.15,1]) #Black
        _list_of_clothing_colours.append([1.0,1.0,1.0,1]) #White
        _list_of_clothing_colours.append([0.7,0.4,0.4,1]) #Light Pink
        _list_of_clothing_colours.append([0.4,0.7,0.4,1]) #Light blue
        _list_of_clothing_colours.append([0.4,0.4,0.7,1]) #Light green
        _list_of_clothing_colours.append([0.31,0.23,0.33,1]) #Purple
        _list_of_clothing_colours.append([0.9,0.5,0.1,1]) #Orange

        _list_of_body_types = []
        _list_of_body_types.append("thin_body")
        _list_of_body_types.append("standard_body")
        _list_of_body_types.append("curvy_body")

        # A master list of things a character might like or dislike.
        # Should always be named so it fits the framework "Likes X" or "Dislikes X".
        # Personalities have a unique list that they always draw from as well
        _opinions_list = init_list_of_opinions()

        #Another list of opinions, but these ones are sex/kink related and
        # probably shouldn't be brought up in polite conversation.
        _sexy_opinions_list = init_list_of_sexy_opinions()

        @classmethod
        def get_random_tit(cls,min=None,max=None):
            if not min:
                start = 0
            else:
                start = cls.get_tit_index(min)
            if not max:
                end = len(cls._list_of_tits)
            else:
                end =  cls.get_tit_index(max)+1
            return get_random_from_weighted_list(cls._list_of_tits[start:end])


        @classmethod
        def get_tit_weighted_list(cls,min=None,max=None):
            if not min:
                start = 0
            else:
                start = cls.get_tit_index(min)
            if not max:
                end = len(cls._list_of_tits)
            else:
                end =  cls.get_tit_index(max)+1
            return cls._list_of_tits[start:end]

        @classmethod
        def get_maximum_tit(cls):
            return get_random_from_weighted_list(cls._list_of_tits[-1:])

        @classmethod
        def get_tit_index(cls,current_tits):
            return index_in_weighted_list(current_tits,cls._list_of_tits)

        @classmethod
        def rank_tits(cls,the_tits): #Useful if you need to know exactly who has larger tits and want to compare ints. Also see Person.has_large_tits, for a flat definition of large tits as D or larger
            #Mostly an alias for get_tit_index but defaults to 0 (which is undesirable for a function that may be as like setting a maximum as a minimum)
            try:
                return cls.get_tit_index(the_tits)
            except UnboundLocalError as err:
                return 0

        @classmethod
        def get_smaller_tit(cls,current_tit):
            current_index = cls.get_tit_index(current_tit)
            return cls._list_of_tits[__builtin__.max(0,current_index-1)][0]


        @classmethod
        def get_larger_tit(cls,current_tit):
            current_index = cls.get_tit_index(current_tit)
            return cls._list_of_tits[__builtin__.min(current_index+1,len(cls._list_of_tits)-1)][0]


        @classmethod
        def get_random_tiny_tit(cls):
            return cls.get_random_tit(max=cls._tiny_tit_maximum)


        @classmethod
        def get_random_small_tit(cls):
            return cls.get_random_tit(max=cls._small_tit_maximum)


        @classmethod
        def get_random_large_tit(cls):
            return cls.get_random_tit(min=cls._large_tit_minimum)

        @classmethod
        def get_random_huge_tit(cls):
            return cls.get_random_tit(min=cls._huge_tit_minimum)

        @classmethod
        def get_maximum_tiny_tit(cls):
            return cls._tiny_tit_maximum

        @classmethod
        def get_maximum_small_tit(cls):
            return cls._small_tit_maximum

        @classmethod
        def get_minimum_large_tit(cls):
            return cls._large_tit_minimum

        @classmethod
        def get_minimum_huge_tit(cls):
            return cls._huge_tit_minimum


        @classmethod
        def get_tiny_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(max=cls._tiny_tit_maximum)

        @classmethod
        def get_small_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(max=cls._small_tit_maximum)

        @classmethod
        def get_large_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(min=cls._large_tit_minimum)

        @classmethod
        def get_huge_tits_weighted_list(cls):
            return cls.get_tit_weighted_list(min=cls._huge_tit_minimum)

        @staticmethod
        def tit_is_in_weighted_tits_list(tit,weighted_tit_list):
            return is_in_weighted_list(tit,weighted_tit_list)

        @classmethod
        def tit_is_tiny(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_tiny_tits_weighted_list())

        @classmethod
        def tit_is_small(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_small_tits_weighted_list())

        @classmethod
        def tit_is_large(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_large_tits_weighted_list())

        @classmethod
        def tit_is_huge(cls,tit):
            return cls.tit_is_in_weighted_tits_list(tit,cls.get_huge_tits_weighted_list())

        @classmethod
        def get_random_skin(cls):
            return get_random_from_weighted_list(cls._list_of_skins)

        @classmethod
        def get_random_hair_colour(cls):
            return get_random_from_list(cls._list_of_hairs)

        @staticmethod
        def get_darkened_colour(the_colour, variation_constant = 0.07):
            return_list = the_colour[:]
            for component_index in __builtin__.range(3): #In case there's an alpha component, we don't want to change that.
                return_list[component_index] = return_list[component_index] * (1-variation_constant)

            return return_list

        @classmethod
        def generate_hair_colour(cls, base_colour = None, create_variation = True):
            return_hair = None

            if base_colour:
                hair = next((x for x in cls.get_list_of_hairs() if x[0] == base_colour), None)
                if hair:
                    return_hair = copy.deepcopy(hair)

            if not return_hair:
                return_hair = copy.deepcopy(cls.get_random_hair_colour()) #Deep copy the hair colours because lists are passed by reference and it is two lists deep.

            if create_variation: #The colour is modified slightly to give different characters slightly different hair colours even if they have the same base.
                hair_colour = return_hair[1]
                for component_index in __builtin__.range(3): #The RGB components can be 10% lighter or darker each.
                    component_variation_constant = 0.07
                    if renpy.random.randint(0,1) == 0:
                        # Shade it, it's a little darker.
                        shade_factor = renpy.random.random() * component_variation_constant
                        hair_colour[component_index] = hair_colour[component_index] * (1-shade_factor)

                    else:
                        # Tint it, it's a little lighter.
                        tint_factor = renpy.random.random() * component_variation_constant
                        hair_colour[component_index] = hair_colour[component_index] + ((1-hair_colour[component_index])*tint_factor)

            # add light opacity to better blend with character
            return_hair[1][3] = .95

            return return_hair

        @classmethod
        def get_random_eye(cls):
            return get_random_from_list(cls._list_of_eyes)


        @classmethod
        def generate_eye_colour(cls,base_colour = None, create_variation = True):
            if base_colour:
                for eyes in cls.get_list_of_eyes():
                    if eyes[0] == base_colour: #If we ask for a specific base...
                        return_eyes = copy.deepcopy(eyes)
            else: #Otherwise just get a random one
                return_eyes = copy.deepcopy(cls.get_random_eye()) #Deep copy the hair colours because lists are passed by reference and it is two lists deep.

            if create_variation: #The colour is modified slightly to give different characters slightly different hair colours even if they have the same base.
                eye_colour = return_eyes[1]
                for component_index in __builtin__.range(3): #The RGB components can be 10% lighter or darker each.
                    component_variation_constant = 0.02 #TODO: Test how much this should vary for eye colour.
                    if renpy.random.randint(0,1) == 0:
                        # Shade it, it's a little darker.
                        shade_factor = renpy.random.random() * component_variation_constant
                        eye_colour[component_index] = eye_colour[component_index] * (1-shade_factor)

                    else:
                        # Tint it, it's a little lighter.
                        tint_factor = renpy.random.random() * component_variation_constant
                        eye_colour[component_index] = eye_colour[component_index] + ((1-eye_colour[component_index])*tint_factor)

            return return_eyes


        @classmethod
        def get_random_face(cls):
            return get_random_from_list(cls._list_of_faces)

        @classmethod
        def get_random_name(cls):
            names = [person.name for person in list_of_people]
            return renpy.random.choice(list(set(cls._list_of_names)-set(names)))

        @classmethod
        def get_random_last_name(cls):
            names = [person.last_name for person in list_of_people]
            return renpy.random.choice(list(set(cls._list_of_last_names)-set(names)))

        @classmethod
        def get_random_male_name(cls):
            return get_random_from_list(cls._list_of_male_names)

        @classmethod
        def get_random_glasses_frame_colour(cls):
            # Picks one of several mostly-neutral colours that should go well with most items
            return get_random_from_list(cls._list_of_clothing_colours)

        @classmethod
        def get_random_body_type(cls):
            return get_random_from_list(cls._list_of_body_types)

        @classmethod
        def get_normal_opinions_list(cls):
            return cls._opinions_list[:]

        @classmethod
        def get_sexy_opinions_list(cls):
            return cls._sexy_opinions_list[:]


        @classmethod
        def get_random_normal_opinion(cls):
            return get_random_from_list(cls._opinions_list)

        @classmethod
        def get_random_sexy_opinion(cls):
            return get_random_from_list(cls._sexy_opinions_list)

        @classmethod
        def get_random_coffee_style(cls):
            return get_random_from_list(cls._coffee_list)

        @classmethod
        def get_list_of_hairs(cls):
            return copy.deepcopy(cls._list_of_hairs) #Return a deepcopy so that original list and it's content is immutable

        @classmethod
        def get_list_of_eyes(cls):
            return copy.deepcopy(cls._list_of_eyes) #Return a deepcopy so that original list and it's content is immutable

        @classmethod
        def get_stat_floor(cls,initial=True):
            if initial:
                return cls._initial_stat_floor
            else:
                return cls._final_stat_floor

        @classmethod
        def get_skill_floor(cls,initial=True):
            if initial:
                return cls._initial_skill_floor
            else:
                return cls._final_skill_floor

        @classmethod
        def get_sex_skill_floor(cls,initial=True):
            if initial:
                return cls._initial_sex_skill_floor
            else:
                return cls._final_sex_skill_floor

        @classmethod
        def get_stat_ceiling(cls):
            return cls._initial_stat_ceiling

        @classmethod
        def get_skill_ceiling(cls):
            return cls._initial_skill_ceiling

        @classmethod
        def get_sex_skill_ceiling(cls):
            return cls._initial_sex_skill_ceiling

        @classmethod
        def get_happiness_floor(cls,initial=True):
            if initial:
                return cls._initial_happiness_floor
            else:
                return cls._final_happiness_floor

        @classmethod
        def get_happiness_ceiling(cls):
            return cls._initial_happiness_ceiling


        @classmethod
        def get_suggestibility_floor(cls):
            return cls._initial_suggestibility_floor

        @classmethod
        def get_suggestibility_ceiling(cls):
            return cls._initial_suggestibility_ceiling

        @classmethod
        def get_sluttiness_floor(cls):
            return cls._initial_sluttiness_floor

        @classmethod
        def get_sluttiness_ceiling(cls):
            return cls._initial_sluttiness_ceiling

        @classmethod
        def get_love_floor(cls,initial=True):
            if initial:
                return cls._initial_love_floor
            else:
                return cls._final_love_floor

        @classmethod
        def get_love_ceiling(cls,initial=True):
            if initial:
                return cls._initial_love_ceiling
            else:
                return cls._final_love_ceiling

        @classmethod
        def get_obedience_floor(cls,initial=True):
            if initial:
                return cls._initial_obedience_floor
            else:
                return cls._final_obedience_floor

        @classmethod
        def get_obedience_ceiling(cls):
            return cls._initial_obedience_ceiling


        @classmethod
        def get_work_experience_floor(cls,initial=True):
            if initial:
                return cls._initial_work_experience_floor
            else:
                return cls._final_work_experience_floor

        @classmethod
        def get_work_experience_ceiling(cls,initial=True):
            if initial:
                return cls._initial_work_experience_ceiling
            else:
                return cls._final_work_experience_ceiling

        @classmethod
        def get_age_floor(cls,initial=True):
            if initial:
                return cls._initial_age_floor
            else:
                return cls._final_age_floor

        @classmethod
        def get_age_ceiling(cls,initial=True):
            if initial:
                return cls._initial_age_ceiling
            else:
                return cls._final_age_ceiling

        @classmethod
        def get_height_floor(cls,initial=True):
            if initial:
                return cls._initial_height_floor
            else:
                return cls._final_height_floor

        @classmethod
        def get_height_ceiling(cls,initial=True):
            if initial:
                return cls._initial_height_ceiling
            else:
                return cls._final_height_ceiling

        @classmethod
        def get_old_age_floor(cls):
            return cls._old_age_floor

        @classmethod
        def get_teen_age_ceiling(cls):
            return cls._teen_age_ceiling

        @classmethod
        def get_tall_height_floor(cls):
            return cls._tall_height_floor

        @classmethod
        def get_short_height_ceiling(cls):
            return cls._short_height_ceiling

        @classmethod
        def get_height_step(cls):
            return cls._height_step


        @staticmethod
        def get_person_by_identifier(identifier):
            return next((x for x in list_of_people if x.identifier == identifier), None)

        @staticmethod
        def get_initial_kids_range(age_range,relationships_array):
            kids_range = [-1, 4]
            if age_range < 20:
                kids_range[1] -= 2 #Reduce chance of teen pregnancy

            if age_range[0] > 22 :
                kids_range[0] += 1 #Young people have less time to have kids in general, so modify their number down a bit.
                kids_range[1] += 1

            if age_range[1] < 28:
                kids_range[1] -= 1 #Young characters don't have as many kids

            if age_range[1] < 38:
                kids_range[1] -= 1 #As you get older you're more likely to have one

            if not (is_in_weighted_list("Fiancée",relationships_array) or is_in_weighted_list("Married",relationships_array)):
                kids_range[1] -= 1 #People who are in a stable relationship have more kids

            if not is_in_weighted_list("Married",relationships_array):
                kids_range[1] -= 2 #And married people have more kids still

            return kids_range

        @classmethod
        def get_potential_relationships_list(cls):
            return copy.deepcopy(cls._base_list_of_relationships)

        #Tighten kid range now that true age is known ?
        @classmethod
        def finalize_kids_range(cls,kids_range,age_range,relationships_list,age,relationship):
            if age_range is None or age_range[0] <= 22:
                if age > 22:
                    kids_range[0] += 1 #Young people have less time to have kids in general, so modify their number down a bit.
                    kids_range[1] += 1
            if age_range is None or age_range[1] >= 28:
                if age < 28:
                    kids_range[1] -= 1 #Young characters don't have as many kids
            if age_range is None or age_range[1] >= 38:
                if age < 38:
                    kids_range[1] -= 1 #Young characters don't have as many kids
            if relationships_list is None or (is_in_weighted_list("Fiancée",relationships_list) or is_in_weighted_list("Married",relationships_list)):
                if relationship not in ["Fiancée","Married"]:
                    kids_range[1] -= 1 #People who are in a stable relationship have kids more often than single people
            if relationships_list is None or (is_in_weighted_list("Fiancée",relationships_list) or is_in_weighted_list("Married",relationships_list)):
                if relationship not in ["Married"]:
                    kids_range[1] -= 2 #People who married have kids more often than single people
            return kids_range

        @classmethod
        def finalize_relationships_weight(cls,relationships_list,age):
            for relationship in relationships_list:
                if relationship[0] == "Single":
                    relationship[1] -= age
                if relationship[0] == "Girlfriend":
                    relationship[1] += age
                if relationship[0] == "Fiancée":
                    relationship[1] += 2*age
                if relationship[0] == "Married":
                    relationship[1] += 3*age
            return relationships_list


        def __init__(self,name,last_name,age,body_type,tits,height,body_images,hair_colour,hair_style,pubes_colour,pubes_style,skin,eyes,job,wardrobe,personality,stat_list,skill_list,
            sluttiness=0,obedience=100,suggest=0,sex_skill_list=[0,0,0,0], love = 0, happiness = 100, home = None,
            font = "fonts/Avara.tff", name_color = "#ffffff", dialogue_color = "#ffffff",
            face_style = "Face_1", tan_style = None,
            special_role = None,
            title = None, possessive_title = None, mc_title = None,
            relationship = None, SO_name = None, kids = None, base_outfit = None,
            generate_insta = False, generate_dikdok = False, generate_onlyfans = False, coffee_style=None,
            work_experience = 1, type="random"):

            self.type = type

            #Using char instead of a string lets us customize the font and colour we are using for the character.
            self.char = Character("???", #The name to be displayed above the dialogue.
                what_font = font, #The font to be used for the character.
                who_font = font,
                color = name_color, #The colour of the character's NAME section
                what_color = dialogue_color, #The colour of the character's dialogue.
                what_style = "general_dialogue_style") #Used to describe everything that isn't character specific.

            ## Personality stuff, name, ect. Non-physical stuff.
            self.name = name
            self.last_name = last_name
            ## Physical things.
            self.age = age
            self.body_type = body_type
            self.tits = tits
            self.height = height
            self.body_images = body_images.get_copy() #instance of Clothing class, which uses full body shots.
            self.face_style = face_style

            self.event_triggers_dict = {} #A dict used to store extra parameters used by events, like how many days has it been since a performance review.

            self.title = title #Note: We format these down below!
            self.possessive_title = "The unknown woman" #The way the girl is referred to in relation to you. For example "your sister", "your head researcher", or just their title again.
            if not possessive_title is None:
                self.set_possessive_title(possessive_title)

            if mc_title:
                self.mc_title = mc_title #What they call the main character. Ie. "first name", "mr.last name", "master", "sir".
            else:
                self.mc_title = "Stranger"

            self.identifier = hash((name, last_name, age))
            self.available = True

            self._stripper_salary = 0
            self._location = None
            self._home = None   # private home identifier
            self._follow_mc = False
            self._baby_desire = (-200 if persistent.pregnancy_pref == 3 else 0)

            if home:
                self.home = home #The room the character goes to at night. If none a random public location is picked.

            self.schedule = Schedule()

            self.override_schedule = Schedule() #The mandatory place a person will go EVEN if they have work (useful for giving days off or requiring weekend work)

            # Relationship and family stuff
            if relationship:
                self.relationship = relationship
            else:
                self.relationship = "Single" #Should be Single, Girlfriend, Fiancée, or Married.

            if SO_name:
                self.SO_name = SO_name
            else:
                self.SO_name = None #If not single, name of their SO (for guilt purposes or future events).

            if kids:
                self.kids = kids
            else:
                self.kids = 0


            self.personality = personality


            # Loves, likes, dislikes, and hates determine some reactions in conversations, options, etc. Some are just fluff.
            self.opinions = {} #Key is the name of the opinion (see random list), value is a list holding [value, known]. Value ranges from -2 to 2 going from hate to love (things not on the list are assumed 0). Known is a bool saying if the player knows about their opinion.

            self.sexy_opinions = {}

            #TODO: Relationship with other people (List of known people plus relationship with them.)

            self.what_font = font
            self.who_font = font
            self.what_color = dialogue_color

            if title: #Format the given titles, if any, so they appear correctly the first time you meet at person.
                self.set_title(title) #The way the girl is referred to by the MC. For example: "Mrs. Whatever", "Lily", or "Mom". Will reset "???" if appropriate
            else:
                self.char.name = self.create_formatted_title("???")
            if possessive_title:
                self.set_possessive_title(possessive_title)

            self.text_modifiers = [] #A list of functions, each of which take Person, String and return a modified String. Used to modify text to dynamically highlight words, or reflect a speech difference.

            self.pubes_colour = None

            self.hair_style = hair_style
            if pubes_style is None:
                self.pubes_style = shaved_pubes #An empty image place holder so we can always call on them to draw.
            else:
                self.pubes_style = pubes_style

            self.set_hair_colour(Color(rgb=(hair_colour[1][0],hair_colour[1][1],hair_colour[1][2])))

            self.skin = skin
            self.tan_style = tan_style

            self.set_eye_colour(Color(rgb=(eyes[1][0], eyes[1][1], eyes[1][2])))
            #TODO: Tattoos eventually

            self.serum_tolerance = 2 #How many active serums this person can tolerate before they start to suffer negative effects.
            self.serum_effects = [] #A list of all of the serums we are under the effect of.

            if not special_role:  #Characters may have a special role that unlocks additional actions. By default this is an empty list.
                self.special_role = []
            elif isinstance(special_role, Role):
                self.special_role = [special_role] #Support handing a non-list special role, in case we forget to wrap it in a list one day.
            elif isinstance(special_role, list):
                self.special_role = special_role #Otherwise we've handed it a list
            else:
                self.special_role = []

            self.on_room_enter_event_list = ActionList() #Checked when you enter a room with this character. If an event is in this list and enabled it is run (and no other event is until the room is reentered)
            self.on_talk_event_list = ActionList() #Checked when you start to interact with a character. If an event is in this list and enabled it is run (and no other event is until you talk to the character again.)\

            ##Mental stats##
            #Mental stats are generally fixed and cannot be changed permanently. Ranges from 1 to 5 at start, can go up or down (min 0)
            self.charisma = stat_list[0] #How likeable the person is. Mainly influences marketing, also determines how well interactions with other characters go. Main stat for HR and sales
            self.int = stat_list[1] #How smart the person is. Mainly influences research, small bonuses to most tasks. #Main stat for research and production.
            self.focus = stat_list[2] #How on task the person stays. Influences most tasks slightly. #Main stat for supplies

            self.charisma_debt = 0 #Tracks how far into the negative a characters stats are, for the purposes of serum effects. Effective stats are never lower than 0.
            self.int_debt = 0
            self.focus_debt = 0

            ##Work Skills##
            #Skills can be trained up over time, but are limited by your raw stats. Ranges from 1 to 5 at start, can go up or down (min 0)
            self.hr_skill = skill_list[0]
            self.market_skill = skill_list[1]
            self.research_skill = skill_list[2]
            self.production_skill = skill_list[3]
            self.supply_skill = skill_list[4]

            self.max_energy = 100
            self.energy = self.max_energy

            self.salary_modifier = 1.0 # Set by events for what this character considers "fair" for their skill, and/or reflects what they were promised.
            self.productivity_adjustment = 1.0 # Set by events for what this character is actually able to produce. Generally a "hidden" stat that you can't change.

            self.work_experience = work_experience # How experienced with work in general this girl is. The higher it is the more money a girl will want, but the more duties she can handle.
            self.job = None
            self.duties = []
            self.change_job(job)


            self.salary = self.calculate_base_salary()


            self.idle_pose = get_random_from_list(["stand2","stand3","stand4","stand5"]) #Get a random idle pose that you will use while people are talking to you.
            self.idle_animation = idle_wiggle_animation #If we support animation we use this to jiggle their tits and ass just a little to give the screen some movement.
            #self.idle_animation.innate_animation_strength += 0.05 * rank_tits(self.tits) # Larger tits swing more #TODO: Implement region specific weighting.

            self.personal_region_modifiers = {"breasts":0.1+0.1 * Person.rank_tits(self.tits)} #A dict that stores information about modifiers that should be used for specific regions of animations. Default is 1.

            ##Personality Stats##
            #Things like suggestibility, that change over the course of the game when the player interacts with the girl
            self.suggestibility = 0 + suggest #How likely a girl is to enter or deepen a trance when orgasming
            self.suggest_bag = [] #This will store a list of integers which are the different suggestion values fighting for control. Only the highest is used, maintained when serums are added and removed.

            self.happiness = happiness #Higher happiness makes a girl less likely to quit and more willing to put up with you pushing her using obedience.
            self.love = love
            self.sluttiness = 0 + sluttiness #How slutty the girl is by default. Higher will have her doing more things just because she wants to or you asked.
            self.core_sluttiness = self.sluttiness #Core sluttiness is the base level of what a girl considers normal. normal "sluttiness" is the more variable version, technically refered to as "temporary slutiness".
            self.obedience = obedience #How likely the girl is to listen to commands. Default is 100 (normal person), lower actively resists commands, higher follows them.

            if coffee_style is None:
                self.coffee_style = self.get_random_coffee_style()
            else:
                self.coffee_style = coffee_style

            #Situational modifiers are handled by events. These dicts and related functions provide a convenient way to avoid double contributions. Remember to clear your situational modifiers when you're done with them!!
            self.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
            self.situational_obedience = {} #A dict that stores a "situation" string and a corresponding amount that it has affected their obedience by.

            ##Sex Stats##
            #These are physical stats about the girl that impact how she behaves in a sex scene. Future values might include things like breast sensitivity, pussy tighness, etc.
            self.arousal = 0 #How actively horny a girl is, and how close she is to orgasm.
            self.max_arousal = 100 #Her maximum arousal. TODO: Keep this hidden until you make her cum the first time?

            self.novelty = 100 #How novel this girl making you cum is. Breaking taboos and time increases it, the girl making you cum decreases it.

            ##Sex Skills##
            #These represent how skilled a girl is at different kinds of intimacy, ranging from kissing to anal. The higher the skill the closer she'll be able to bring you to orgasm (whether you like it or not!)
            self.sex_skills = {}
            self.sex_skills["Foreplay"] = sex_skill_list[0] #A catch all for everything that goes on before blowjobs, sex, etc. Includes things like kissing and strip teases.
            self.sex_skills["Oral"] = sex_skill_list[1] #The girls skill at giving head.
            self.sex_skills["Vaginal"] = sex_skill_list[2] #The girls skill at different positions that involve vaginal sex.
            self.sex_skills["Anal"] = sex_skill_list[3] #The girls skill at different positions that involve anal sex.

            self.sex_record = {}
            self.broken_taboos = [] #Taboos apply a penalty to the _first_ time you are trying to push some boundry (first time touching her pussy, first time seeing her tits, etc.), and trigger special dialogue when broken.

            bc_chance = 100 - (self.age + (self.get_opinion_score("bareback sex")*15))
            if persistent.pregnancy_pref == 2 and renpy.random.randint(0,100) > bc_chance:
                self.on_birth_control = False #If this character is on birth control or not. Note that this may be overridden by a game wide setting preventing pregnancy. (and on other settings may not be 100% effective)
            else:
                self.on_birth_control = True
            self.bc_penalty = 0 #Lowers the chance of birth control preventing a pregnancy. (Default is 100% if predictable or 90% if realistic). #TODO: Add serum traits that affect this.
            self.fertility_percent = 20.0 - ((self.age-18.0)/3.0) #The chance, per creampie, that a girl gets pregnant.
            self.ideal_fertile_day = renpy.random.randint(0,29) #Influences a girls fertility chance. It is double on the exact day of the month, dropping down to half 15 days before/after. Only applies on realistic setting.

            self.lactation_sources = 0 #How many things are causing this girl to lactate. Mainly serum traits, side effects, or pregnancy.

            ## Clothing things.
            self.wardrobe = None
            if not wardrobe is None:
                self.wardrobe = copy.copy(wardrobe) #Note: we overwrote default copy behaviour for wardrobes so they do not have any interference issues with eachother.

            if base_outfit is None:
                self.base_outfit = Outfit(name + "'s Base Outfit")
            elif isinstance(base_outfit, Outfit):
                self.base_outfit = base_outfit

            self.infractions = [] #List of infractions this character has committed.

            self.outfit = None  # what outfit is she currently wearing
            self.planned_outfit = None #planned_outfit is the outfit the girl plans to wear today while not at work. She will change back into it after work or if she gets stripped. Cop0y it in case the outfit is changed during the day.
            self.planned_uniform = None #The uniform the person was planning on wearing for today, so they can return to it if they need to while at work.
            self.next_day_outfit = None
            self.maid_outfit = None
            self.location_outfit = None
            self.dress_code_outfit = None

            ## Internet things ##
            if generate_insta: #NOTE: By default all of these are not visible to the player.
                self.add_role(instapic_role)
            if generate_dikdok:
                self.add_role(dikdok_role)
            if generate_onlyfans:
                self.add_role(onlyfans_role)

            ## Conversation things##
            self.sexed_count = 0
            self.is_favourite = False

            self.training_log = defaultdict(int) #Contains a list of Trainable.training_tag's that this person has had trained already, which is used to increase the cost of future training in similar things.

        def __call__(self, what, *args, **kwargs): #Required to play nicely with statement equivalent say() when passing only Peron object.
            new_what = self.personalise_text(what) #keep the old what as a reference in case we need it.

            global portrait_say
            portrait_say = self.build_person_portrait()
            if not persistent.text_effects:
                self.char(new_what, *args, **kwargs)
                portrait_say = None
                return

            new_colour = Color(self.what_color) #Multiple sections may modify the colour of the entire string, so we apply it once at the end.

            #Tags that are applied are generally applied to the inner most parts up here, more general as we go down.
            if self.has_role(trance_role): #Desaturate her dialogue as she falls deeper into a trance.
                if self.has_exact_role(trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.7)
                elif self.has_exact_role(heavy_trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.4)
                elif self.has_exact_role(very_heavy_trance_role):
                    new_colour = new_colour.multiply_hsv_saturation(0.1)

            flattened_phrase = remove_punctuation(what).lower() #Strip the entire phrase so we can check for individual words.
            if "knocked up" in new_what.lower():
                if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                    start_index = new_what.lower().find("knocked up")
                    start_substring = new_what[start_index:start_index + len("knocked up")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "knock me up" in new_what.lower():
                if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                    start_index = new_what.lower().find("knock me up")
                    start_substring = new_what[start_index:start_index + len("knock me up")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "preg me" in new_what.lower():
                if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                    start_index = new_what.lower().find("preg me")
                    start_substring = new_what[start_index:start_index + len("preg me")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "oh god" in new_what.lower():
                if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                    start_index = new_what.lower().find("oh god")
                    start_substring = new_what[start_index:start_index + len("oh god")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)

            if "oh my god" in new_what.lower():
                if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                    start_index = new_what.lower().find("oh my god")
                    start_substring = new_what[start_index:start_index + len("oh my god")]
                    replace_substring = "{sc=1}"+self.wrap_string(start_substring, the_colour = new_colour)+"{/sc}"
                    new_what = new_what.replace(start_substring, replace_substring)


            temp_what = ""
            for word in new_what.split(): #Per word modifications
                flattened_word = remove_punctuation(word).lower() #Stripped and lower case for easy comparison, we use the full raw word (including punctaiton) for replacement.
                modified_word = False
                effect_strength = str(int(6*(self.arousal_perc/100)) + 2) #If an effect triggers this scales the effect with arousal.
                if word[0] == "{" and word [-1] == "}":
                    pass #Don't do anything to tags.

                elif flattened_word == "cum" or flattened_word == "cumming": #Strip punctuation, avoids us catching phrases like "cumming" and only shaking the front.
                    if self.arousal_perc > (40 - 10*(self.get_opinion_score("drinking cum")+self.get_opinion_score("being covered in cum")+self.get_opinion_score("cum facials")+self.get_opinion_score("creampies"))):
                        modified_word = True
                        cum_color = Color("#e5e5d6")

                        word_replace = self.wrap_string(word, the_colour = cum_color, the_font = "fonts/plasdrip.ttf")
                        word_replace = "{atl=0.3,drop_text~#~ 2.0, bounce_text~" + effect_strength + "}" + word_replace + "{/atl}"
                        temp_what += word_replace + " "

                elif flattened_word == "cock" or flattened_word == "dick":
                    if self.arousal_perc > (40 - 10*(self.get_opinion_score("big dicks"))):
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        word_replace = "{sc=1}{bt=" + effect_strength + "}" + word_replace + "{/bt}{/sc}"
                        temp_what += word_replace + " "

                elif flattened_word == "pussy" or flattened_word == "vagina" or flattened_word == "cunt":
                    if self.arousal_perc > (50):
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour)
                        word_replace = "{bt=" + effect_strength + "}" + word_replace + "{/bt}"
                        temp_what += word_replace + " "

                elif any(flattened_word == target_word for target_word in ["tit","tits","boob","boobs","breast","breasts","mommy milkers"]):
                    if self.arousal_perc > 40 - 10*self.get_opinion_score("showing her tits"):
                        modified_word = True
                        tit_effect_strength = str(int(6*(self.arousal_perc/100)) + Person.rank_tits(self.tits))
                        word_replace = self.wrap_string(word, the_colour = new_colour)
                        word_replace = "{atl=bounce_text~" + tit_effect_strength + "}" + word_replace + "{/atl}"
                        temp_what += word_replace + " "

                elif flattened_word == "fuck":
                    if self.arousal_perc > 60:
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        temp_what += word_replace + " "

                elif flattened_word == "pregnant" or flattened_word == "bred" or flattened_word == "breed": #TODO: Add a word effect that swells through the middle?
                    if self.arousal_perc > 40 - (10*self.get_opinion_score("bareback sex") + self.get_opinion_score("creampies")) or self.has_breeding_fetish:
                        modified_word = True
                        word_replace = self.wrap_string(word, the_colour = new_colour, size_mod = effect_strength)
                        word_replace = "{sc=1}" + word_replace + "{/sc}"
                        temp_what += word_replace + " "

                if not modified_word:
                    temp_what += word + " "

            new_what = temp_what #[:-1] #STrip the last character, which is an unused space.
            new_what = self.wrap_string(new_what, the_colour = new_colour)

            self.char(new_what, *args, **kwargs)
            portrait_say = None

        def __hash__(self):
            return self.identifier

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.name == other.name and self.last_name == other.last_name and self.age == other.age
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.name != other.name or self.last_name != other.last_name and self.age != other.age
            return True

        def wrap_string(self, string, the_colour = None, the_font = None, size_mod = None): #Useful for wrapping a piece of advanced tag dialogue with the proper font, colour, style.
            return_string = string
            if the_colour is None:
                the_colour = self.what_color.hexcode
            else:
                the_colour = the_colour.hexcode

            if the_font is None:
                the_font = self.who_font
            return_string = "{color=" + the_colour + "}" + return_string + "{/color}"
            return_string = "{font=" + the_font + "}" + return_string + "{/font}" #Then set the font
            if size_mod is not None:
                size_string = str(size_mod)
                if size_mod > 0:
                    size_string = "+" + size_string
                return_string = "{size=" + size_string + "}" + return_string + "{/size}"
            #return_string = "{=general_dialogue_style}" + return_string + "{/=general_dialogue_style}"
            return return_string

        @property
        def idle_pose(self):
            if not "downtown_bar" in globals(): # skip this when running tutorial
                return self._idle_pose

            if not hasattr(self, "_idle_pose"):
                self._idle_pose = renpy.random.choice(["stand2","stand3","stand4","stand5"])

            if renpy.call_stack_depth() < 2:
                # we are in the main menu (alternative idle_pose)
                if (self.is_employee and self.is_at_work) or self.location == downtown_bar:
                    return "sitting"
                if self.location == gym:
                    pose = self.event_triggers_dict.get("gym_pose", None)
                    if not pose: # store preferred position in bdsm room (prevent switching on hover)
                        pose = renpy.random.choice(["missionary", "stand2", "back_peek", "stand4", "sitting"])
                        self.event_triggers_dict["gym_pose"] = pose
                    return pose

            if self.has_role(caged_role):
                pose = self.event_triggers_dict.get("bdsm_room_pose", None)
                if not pose: # store preferred position in bdsm room (prevent switching on hover)
                    pose = renpy.random.choice(["cowgirl", "kneeling1", "blowjob"])
                    self.event_triggers_dict["bdsm_room_pose"] = pose
                return pose
            return self._idle_pose

        @idle_pose.setter
        def idle_pose(self, value):
            self._idle_pose = value

        @property
        def location(self):
            return next((x for x in list_of_places if x.identifier == self._location), self.home) # fallback location is her home

        @location.setter
        def location(self, value):
            if isinstance(value, Room):
                self._location = value.identifier

        @property
        def home(self):
            return next((x for x in list_of_places if x.identifier == self._home), None)

        @home.setter
        def home(self, value):
            if isinstance(value, Room):
                self._home = value.identifier
            else:
                self._home = None

        def learn_home(self): # Adds the_person.home to mc.known_home_locations allowing it to be visited without having to go through date label
            if not self.home in mc.known_home_locations + [lily_bedroom, mom_bedroom, aunt_bedroom, cousin_bedroom]:
                mc.known_home_locations.append(self.home)
                return True # Returns true if it succeeds
            return False # Returns false otherwise, so it can be used for checks.

        def change_home_location(self, new_home):
            if not isinstance(new_home, Room):
                print("change_home_location(): Error new home parameter is not a room.")
                return

            # remove current location, if house will be empty
            if not any(x for x in all_people_in_the_game(excluded_people = [self]) if x.home == self.home) \
                and self.home in mc.known_home_locations:
                mc.known_home_locations.remove(self.home)

            # if at old home location, move to new home
            if self.location == self.home:
                self.change_location(new_home)

            # set home and default schedule to new home location
            self.set_schedule(new_home, the_times = [0,4])
            self.home = new_home
            return

        def toggle_favourite(self):
            self.is_favourite = not self.is_favourite

        @property
        def is_home(self):
            return self.location == self.home

        @property
        def is_at_work(self):
            # special handling for college interns
            if self.is_intern and self.is_at_office:
                return True

            # special handling for girls working at stripclub (use roles instead of job)
            if self.is_strip_club_employee:
                if not strip_club_is_closed():
                    return self.location in [strip_club, bdsm_room]
                return False

            if not self.job:
                return False

            if self.has_role(maid_role):
                return not self.job.schedule.get_destination() is None

            # she works around town, so when the job has a scheduled location, she's at work
            if self == police_chief:
                return not self.job.schedule.get_destination() is None

            return self.location == self.job.job_location

        @property
        def is_at_office(self):
            return self.location in office_hub

        @property
        def is_at_mc_house(self):
            return self.location in home_hub

        @property
        def bedroom(self):
            if not hasattr(self, "_bedroom"):
                if self.has_role(prostitute_role):
                    self._bedroom = prostitute_bedroom.identifier
                else:
                    self._bedroom = renpy.random.choice([generic_bedroom_1, generic_bedroom_2, generic_bedroom_3, generic_bedroom_4]).identifier
            return next((x for x in list_of_places if x.identifier == self._bedroom), self.home) # fallback location is her home

        @bedroom.setter
        def bedroom(self, location):
            if not isinstance(location, Room):
                return
            self._bedroom = location.identifier

        def change_location(self, destination):
            if not isinstance(destination, Room):
                return

            if self.location == destination:
                return

            self.location = destination

            # only change outfit when not following mc
            if self.follow_mc:
                return

            if destination == gym:
                self.apply_gym_outfit()
            elif destination == university and self.has_role(generic_student_role):
                self.apply_university_outfit()
            else:
                self.apply_planned_outfit()

        def change_to_bedroom(self):
            mc.change_location(self.bedroom)
            return

        def change_to_hallway(self):
            mc.change_location(her_hallway) # use generic hallway

        @property
        def can_clone(self):
            if not genetic_manipulation_policy.is_owned:
                return False
            if self.has_role(clone_role):
                return False
            if self in unique_character_list:
                return False
            return True

        @property
        def follow_mc(self):
            return self._follow_mc

        @follow_mc.setter
        def follow_mc(self, value):
            self._follow_mc = value

        @property
        def expression_images(self):
            global emotion_images_dict
            return emotion_images_dict[self.skin][self.face_style]

        @property
        def fname(self):
            return self.create_formatted_title(self.name)

        @property
        def display_name(self):
            display_name = self.create_formatted_title("???")
            if self.title:
                display_name = self.title
            return display_name

        @property
        def arousal_perc(self):
            return ((self.arousal * 1.0) / (self.max_arousal or 1)) * 100

        @property
        def work(self):
            if not hasattr(self, "_work"):
                self._work = None
            return next((x for x in list_of_places if x.identifier == self._work), None)

        @work.setter
        def work(self, value):
            if isinstance(value, Room):
                self._work = value.identifier
            else:
                self._work = None

        @property
        def is_family(self):
            return any(relationship in [sister_role,mother_role,aunt_role,cousin_role] for relationship in self.special_role)

        @property
        def is_employee(self):
            return self.has_role(employee_role)

        @property
        def is_strip_club_employee(self):
            return self.has_role([stripper_role, stripclub_stripper_role, stripclub_waitress_role, stripclub_bdsm_performer_role, stripclub_manager_role, stripclub_mistress_role])

        @property
        def employed_since(self):
            return self.event_triggers_dict.get("employed_since", -1)

        @employed_since.setter
        def employed_since(self, value):
            self.event_triggers_dict["employed_since"] = value

        @property
        def days_employed(self):
            if self.is_employee:
                return day - self.employed_since
            return 0

        @property
        def suggest_tier(self):   #Returns a value of 0-3 depending on the person's suggestibility.
            if self.suggestibility < 15:
                return 0
            elif self.suggestibility < 35:
                return 1
            elif self.suggestibility < 55:
                return 2
            elif self.suggestibility < 75:
                return 3
            return 4 #Edge case, has suggestibility not yet in game

        @property
        def obedience_tier(self):
            if self.obedience < 100:
                return 0
            elif self.obedience < 120:
                return 1
            elif self.obedience < 140:
                return 2
            elif self.obedience < 160:
                return 3
            elif self.obedience < 180:
                return 4
            return 5

        @property
        def is_available(self):
            return self.location != purgatory and self.available

        @property
        def is_bald(self):
            return self.hair_style == bald_hair

        @property
        def is_dominant(self):
            if self.personality == alpha_personality and self.obedience < 250:
                return True
            return self.get_opinion_score("taking control") > 0 and \
                self.get_opinion_score("taking control") >= self.get_opinion_score("being submissive")

        @property
        def is_submissive(self):
            if self.has_role(slave_role):
                return True
            if self.personality == alpha_personality and self.obedience < 250:
                return False
            return self.get_opinion_score("being submissive") > 0 and \
                self.get_opinion_score("taking control") <= self.get_opinion_score("being submissive")

        @property
        def is_stranger(self):
            return not self.title or self.mc_title == "Stranger"

        @property
        def is_single(self):
            return self.relationship == "Single" and not self.is_girlfriend

        @property
        def is_girlfriend(self):
            return self.has_role([girlfriend_role, harem_role])

        @property
        def is_affair(self):
            return self.has_role(affair_role)

        @property
        def tan_style(self):
            return self._tan_style

        @tan_style.setter
        def tan_style(self, value):
            if value == no_tan:
                self._tan_style = None
            else:
                self._tan_style = value

        @property
        def formal_address(self):
            if self.job == nora_professor_job:
                return "Professor"
            if self.job in [doctor_job]:
                return "Doctor"
            if self.relationship == "Married":
                return "Mrs."
            elif self.age > 30:
                return "Ms."
            return "Miss"

        def change_height(self, amount, chance):
            lower_limit = Person.get_height_floor(initial=False)
            upper_limit = Person.get_height_ceiling(initial=False)

            if amount == 0 or (self.height <= lower_limit and amount < 0) or (self.height >= upper_limit and amount > 0):
                return False

            if renpy.random.randint(0, 100) <= chance:
                self.height += amount
            else:
                return False

            if self.height > upper_limit:
                self.height = upper_limit

            if self.height < lower_limit:
                self.height = lower_limit
            return True

        @property
        def weight(self):
            if not hasattr(self, "_weight"):
                if self.body_type == "thin_body":
                    self._weight = 60 * self.height
                elif self.body_type == "standard_body":
                    self._weight = 75 * self.height
                else:
                    self._weight = 90 * self.height
            return self._weight

        @weight.setter
        def weight(self, value):
            self._weight = value

        def change_weight(self, amount, chance):
            if (amount == 0):
                return False

            if renpy.random.randint(0, 100) <= chance:
                self.weight += amount

            # maximum and minimum weight are dependant on height
            max_weight = (self.height) * 100
            min_weight = (self.height) * 50
            switch_point_low = (self.height) * 68
            switch_point_high = (self.height) * 83

            if (amount > 0):
                if self.weight > switch_point_low + 3 and self.body_type == "thin_body":
                    self.body_type = "standard_body"
                    return True
                if self.weight > switch_point_high + 3 and self.body_type == "standard_body":
                    self.body_type = "curvy_body"
                    return True
                if self.weight > max_weight: #Maximum weight
                    self.weight = max_weight
                return False

            if (amount < 0):
                if self.weight < min_weight:  #Minimum weight
                    self.weight = min_weight
                    return False
                if self.weight < switch_point_low - 3 and self.body_type == "standard_body":
                    self.body_type = "thin_body"
                    return True
                if self.weight < switch_point_high - 3 and self.body_type == "curvy_body":
                    self.body_type = "standard_body"
                    return True
                return False

        @property
        def hair_description(self):
            if self.is_bald:
                return "bald head"
            elif self.hair_style in [braided_bun]:
                return "braided hair"
            elif self.hair_style in [messy_short_hair, shaved_side_hair, short_hair, windswept_hair]:
                return "short hair"
            elif self.hair_style in [messy_ponytail, twintail, ponytail]:
                return "pony tail"
            return "long hair"

        @property
        def pubes_description(self):
            if self.pubes_style == shaved_pubes:
                return "bald"
            if self.pubes_style == landing_strip_pubes:
                return "brazilian waxed"
            if self.pubes_style == default_pubes:
                return "hairy"
            return "neatly trimmed"

        @property
        def tits_description(self):
            rank = self.rank_tits(self.tits)
            adjective = "perky"
            descriptor = "tits"

            if rank == 0:
                adjective = renpy.random.choice(["flat", "minute", "tiny"])
                descriptor = renpy.random.choice(["titties", "tits", "nipples"])
            elif rank >= 1 and rank <= 3:
                adjective = renpy.random.choice(["firm", "perky", "small"])
                descriptor = renpy.random.choice(["breasts", "tits", "boobs"])
            elif rank >= 4 and rank <= 6:
                adjective = renpy.random.choice(["shapely", "large", "big", "generous"])
                descriptor = renpy.random.choice(["breasts", "tits", "bosoms"])
            elif rank >= 7 and rank <= 9:
                adjective = renpy.random.choice(["large", "voluptuous", "colossal", "huge"])
                descriptor = renpy.random.choice(["breasts", "tits", "jugs", "melons"])

            return "{adj} {desc}".format(adj = adjective, desc = descriptor)

        @property
        def sluttiness_tier(self):
            if self.sluttiness < 20:
                return 0
            if self.sluttiness < 40:
                return 1
            if self.sluttiness < 60:
                return 2
            if self.sluttiness < 80:
                return 3
            if self.sluttiness < 100:
                return 4
            return 5

        def reset_event_parameters(self):
            base_value = 0 if not "GAME_SPEED" in globals() else GAME_SPEED
            self.event_triggers_dict["chatted"] = 4 - base_value
            self.event_triggers_dict["flirted"] = 4 - base_value
            self.event_triggers_dict["complimented"] = 4 - base_value
            return

        def init_person_variables(self):
            #Set personality based opinions.
            for x in __builtin__.range(2,5):
                the_opinion_key, opinion_list = self.personality.generate_default_opinion()
                if the_opinion_key:
                    self.opinions[the_opinion_key] = opinion_list

            for x in __builtin__.range(2,4):
                the_opinion_key, opinion_list = self.personality.generate_default_sexy_opinion()
                if the_opinion_key:
                    self.sexy_opinions[the_opinion_key] = opinion_list

            self.sex_record["Handjobs"] = 0
            self.sex_record["Blowjobs"] = 0
            self.sex_record["Cunnilingus"] = 0
            self.sex_record["Tit Fucks"] = 0
            self.sex_record["Vaginal Sex"] = 0
            self.sex_record["Anal Sex"] = 0
            self.sex_record["Cum Facials"] = 0
            self.sex_record["Cum in Mouth"] = 0
            self.sex_record["Cum Covered"] = 0
            self.sex_record["Vaginal Creampies"] = 0
            self.sex_record["Anal Creampies"] = 0
            self.sex_record["Fingered"] = 0
            self.sex_record["Kissing"] = 0

            return

        def generate_home(self, set_home_time = True): #Creates a home location for this person and adds it to the master list of locations so their turns are processed.
            # generate new home location if we don't have one
            start_home = self.home
            if not start_home:
                start_home = Room(self.name + " " + self.last_name + " home", self.name + " " + self.last_name + " home", house_background, [make_wall(), make_floor(), make_couch(), make_window()],[],False,[0.5,0.5], visible = False, hide_in_known_house_map = False, lighting_conditions = standard_indoor_lighting)

            # add home location to list of places, before assignment
            if not start_home in list_of_places:
                list_of_places.append(start_home)

            self.home = start_home

            if set_home_time:
                self.set_schedule(self.home, the_times = [0,4])
            return self.home

        def generate_daughter(self, force_live_at_home = False): #Generates a random person who shares a number of similarities to the mother
            age = renpy.random.randint(18, self.age-16)

            if renpy.random.randint(0,100) < 60:
                if self.is_pregnant:
                    body_type = self.event_triggers_dict.get("pre_preg_body", None)
                else:
                    body_type = self.body_type
            else:
                body_type = None

            if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
                face_style = self.face_style
            else:
                face_style = None

            if renpy.random.randint(0,100) < 30: #30% of the time they share hair colour (girls dye their hair a lot)
                hair_colour = self.hair_colour
            else:
                hair_colour = None

            if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
                if self.is_pregnant:
                    tits = self.event_triggers_dict.get("pre_preg_tits", None)
                else:
                    tits = self.tits
            else:
                tits = None

            if renpy.random.randint(0,100) < 60: #Share the same eye colour
                eyes = self.eyes
            else:
                eyes = None

            if renpy.random.randint(0,100) < 80: #Have heights that roughly match (mostly)
                height = self.height * (renpy.random.randint(95,105)/100.0)
                if height > 1.0:
                    height = 1.0
                elif height < 0.8:
                    height = 0.8
            else:
                height = None

            if force_live_at_home or renpy.random.randint(0,100) < 85 - age: #It is less likely she lives at home the older she is.
                start_home  = self.home
            else:
                start_home  = None


            the_daughter = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
                hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

            if start_home is None:
                the_daughter.generate_home()
            else:
                the_daughter.set_schedule(the_location = start_home, the_times = [0,4])

            the_daughter.home.add_person(the_daughter)

            for sister in town_relationships.get_existing_children(self): #First find all of the other kids this person has
                town_relationships.update_relationship(the_daughter, sister, "Sister") #Set them as sisters

            town_relationships.update_relationship(self, the_daughter, "Daughter", "Mother") #Now set the mother/daughter relationship (not before, otherwise she's a sister to herself!)

            return the_daughter

        def generate_mother(self, lives_with_daughter = False): #Generates a random person who shares a number of similarities to the mother
            age = renpy.random.randint(self.age + 16, 55)

            if renpy.random.randint(0,100) < 60:
                if self.is_pregnant:
                    body_type = self.event_triggers_dict.get("pre_preg_body", None)
                else:
                    body_type = self.body_type
            else:
                body_type = None

            if renpy.random.randint(0,100) < 40: #Slightly lower for facial similarities to keep characters looking distinct
                face_style = self.face_style
            else:
                face_style = None

            if renpy.random.randint(0,100) < 30: #30% of the time they share hair colour (girls dye their hair a lot)
                hair_colour = self.hair_colour
            else:
                hair_colour = None

            if renpy.random.randint(0,100) < 60: # 60% they share the same breast size
                if self.is_pregnant:
                    tits = self.event_triggers_dict.get("pre_preg_tits", None)
                else:
                    tits = self.tits
            else:
                tits = None

            if renpy.random.randint(0,100) < 60: #Share the same eye colour
                eyes = self.eyes
            else:
                eyes = None

            if renpy.random.randint(0,100) < 80: #Have heights that roughly match (mostly)
                height = self.height * (renpy.random.randint(95,105)/100.0)
                if height > 1.0:
                    height = 1.0
                elif height < 0.8:
                    height = 0.8
            else:
                height = None

            if lives_with_daughter:
                start_home  = self.home
            else:
                start_home  = None

            the_mother = make_person(last_name = self.last_name, age = age, body_type = body_type, face_style = face_style, tits = tits, height = height,
                hair_colour = hair_colour, skin = self.skin, eyes = eyes, start_home = start_home, force_random = True)

            # set children fixed to one, to prevent circular relative creations (like create mom, has 3 children, so we can start hiring her other daughters)
            the_mother.kids = 1

            if start_home is None:
                the_mother.generate_home()
            else:
                the_mother.set_schedule(the_location = start_home, the_times = [0,4])

            the_mother.home.add_person(the_mother)

            for sister in town_relationships.get_existing_sisters(self): #First find all of the sisters this person has
                town_relationships.update_relationship(the_mother, sister, "Daughter", "Mother") #Set the mother/daughter relationship for the sisters
                the_mother.kids += 1 # increase child count per sister

            town_relationships.update_relationship(self, the_mother, "Mother", "Daughter") #Now set the mother/daughter relationship with person

            return the_mother

        def run_turn(self):
            self.change_energy(20, add_to_log = False)

            remove_list = []
            for serum in self.serum_effects: #Compute the effects of all of the serum that the girl is under.
                serum.run_on_turn(self) #Run the serum's on_turn funcion if it has one.
                if serum.is_expired: #Returns true if the serum effect is suppose to expire in this time, otherwise returns false. Always updates duration counter when called.
                    remove_list.append(serum) #Use a holder "remove" list to avoid modifying list while iterating.

            for serum in remove_list:
                serum.run_on_remove(self)
                self.serum_effects.remove(serum)

            # Check for serum overdoses after expired effects have been removed.
            over_tolerance_count = len(self.serum_effects) - self.serum_tolerance
            if over_tolerance_count > 0:
                self.change_happiness(over_tolerance_count*-5, add_to_log = False)
                self.add_situational_slut("over serum tolerance", over_tolerance_count*-5, "My body feels strange...")
                self.add_situational_obedience("over serum tolerance", over_tolerance_count*-5, "My body feels strange...")
            else:
                self.clear_situational_slut("over serum tolerance")
                self.clear_situational_obedience("over serum tolerance")

            if self.lactation_sources > 0: #She'll have milky tits, which can be milked in some cases
                self.event_triggers_dict["max_milk_in_breasts"] = Person.rank_tits(self.tits) * 2 #Max milk is determind by tit size
                self.event_triggers_dict["milk_in_breasts"] = self.event_triggers_dict.get("milk_in_breasts", 0) + Person.rank_tits(self.tits) * self.lactation_sources * 0.2
                if self.event_triggers_dict.get("milk_in_breasts",0) > self.event_triggers_dict.get("max_milk_in_breasts",0):
                    self.event_triggers_dict["milk_in_breasts"] = self.event_triggers_dict.get("max_milk_in_breasts",0)

            else:
                self.event_triggers_dict["max_milk_in_breasts"] = 0

            for role in self.special_role:
                role.run_turn(self)

        def run_move(self):
            for serum in self.serum_effects: #Compute the effects of all of the serum that the girl is under.
                serum.run_on_move(self) #Run the serum's on_move function if one exists

            # reset talk actions
            self.reset_event_parameters()

            self.sexed_count = 0 #Reset the counter for how many times you've been seduced, you might be seduced multiple times in one day!

            if time_of_day == 0: #Change outfit here, because crisis events might be triggered after run day function
                if self.next_day_outfit:
                    self.planned_outfit = self.next_day_outfit
                    self.next_day_outfit = None
                else:
                    self.planned_outfit = self.decide_on_outfit()
                self.planned_uniform = None
                self.maid_outfit = None
                self.apply_planned_outfit()

            # off duty clear planned uniform / dress code outfit
            if self.is_employee and time_of_day == 4:
                self.planned_uniform = None
                self.dress_code_outfit = None

            destination = self.get_destination() #None destination means they have free time
            if not destination:
                destination = get_random_from_list([x for x in list_of_places if (x.public and x.is_accessible) or x == self.home])

            if not self.location == destination: # only call move_person when location changed
                self.location_outfit = None # Clear the current location outfit
                # changing outfits is handled by change_location
                self.change_location(destination)

            if self.should_wear_uniform: #She's wearing a uniform
                if creative_colored_uniform_policy.is_active:
                    self.change_happiness(max(-1,self.get_opinion_score("work uniforms")), add_to_log = False)
                else:
                    self.change_happiness(self.get_opinion_score("work uniforms"), add_to_log = False)
                if self.planned_uniform and self.planned_uniform.outfit_slut_score > self.sluttiness*0.8: #A skimpy outfit/uniform is defined as the top 20% of a girls natural sluttiness.
                    self.change_slut(self.get_opinion_score("skimpy uniforms"), 30, add_to_log = False)
            else:
                #A skimpy outfit is defined as the top 20% of a girls natural sluttiness.
                if self.planned_outfit and self.planned_outfit.outfit_slut_score > self.sluttiness * 0.80 and self.get_opinion_score("skimpy outfits") > -2:
                    self.change_slut(1, max_modified_to = ((self.get_opinion_score("skimpy outfits") +1) * 10), add_to_log = False)

            #A conservative outfit is defined as the bottom 20% of a girls natural sluttiness.
            if self.sluttiness < 30 and self.outfit and self.outfit.outfit_slut_score < self.sluttiness * 0.20:
                # happiness won't go below 80 or over 120 by this trait and only affects in low sluttiness range, after that she won't care
                if self.happiness > 80 and self.happiness < 120:
                    self.change_happiness(self.get_opinion_score("conservative outfits"), add_to_log = False)

            # lingerie only impacts to sluttiness level 30
            if self.outfit and (self.outfit.get_bra() or self.outfit.get_panties()):
                lingerie_bonus = 0
                if self.outfit.get_bra() and self.outfit.get_bra().slut_value > 1: #We consider underwear with an innate sluttiness of 2 or higher "lingerie" rather than just underwear.
                    lingerie_bonus += self.get_opinion_score("lingerie")
                if self.outfit.get_panties() and self.outfit.get_panties().slut_value > 1:
                    lingerie_bonus += self.get_opinion_score("lingerie")
                lingerie_bonus = __builtin__.int(lingerie_bonus/2.0)
                self.change_slut(lingerie_bonus, max_modified_to = 30, add_to_log = False)

            # not wearing underwear only impacts sluttiness to level 40
            if self.outfit and not self.is_wearing_underwear: #We need to determine how much underwear they are not wearing. Each piece counts as half, so a +2 "love" is +1 slut per chunk.
                underwear_bonus = 0
                if not self.wearing_bra:
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                if not self.wearing_panties:
                    underwear_bonus += self.get_opinion_score("not wearing underwear")
                underwear_bonus = __builtin__.int(underwear_bonus/2.0) #I believe this rounds towards 0. No big deal if it doesn't, very minor detail.
                self.change_slut(underwear_bonus, max_modified_to = 40, add_to_log = False)

            # showing the goods only impacts sluttiness to level 50
            if self.outfit and self.tits_visible:
                self.change_slut(self.get_opinion_score("showing her tits"), max_modified_to = 50, add_to_log = False)
            if self.outfit and self.vagina_visible:
                self.change_slut(self.get_opinion_score("showing her ass"), max_modified_to = 50, add_to_log = False)

            # showing everything only impacts sluttiness to level 60
            if self.outfit and self.outfit.has_full_access:
                self.change_slut(self.get_opinion_score("not wearing anything"), max_modified_to = 60, add_to_log = False)

            for lta_store in [self.on_room_enter_event_list, self.on_talk_event_list]:
                for an_action in [x for x in lta_store if isinstance(x, Limited_Time_Action)]:
                    an_action.turns_valid -= 1
                    if an_action.turns_valid <= 0:
                        lta_store.remove(an_action)

            for role in self.special_role:
                role.run_move(self)

        def run_day(self):
            self.change_energy(.6 * self.max_energy, add_to_log = False)
            self.change_novelty(1, add_to_log = False)

            #Now we will normalize happiness towards 100 over time. Every 5 points of happiness above or below 100 results in a -+1 per turn, rounded towards 0.
            hap_diff = self.happiness - 100
            hap_diff = __builtin__.int(hap_diff/5.0) #python defaults to truncation towards 0, so this gives us the number we should be changing our happinss by
            self.change_happiness(-hap_diff, add_to_log = False) #Apply the change

            if self.arousal > (self.max_arousal / 2.0): #If her arousal is high she masturbates at night, generating a small amount of sluttiness #TODO: Have this trigger an LTE where girls might be getting off when you walk in.
                self.arousal = 0
                if self.get_opinion_score("masturbating") > 0: # Masturbating turns her on, so just getting off turns her back on!
                    self.arousal = 15*self.get_opinion_score("masturbating")
                self.change_happiness(5+5*self.get_opinion_score("masturbating"), add_to_log = False)
                self.run_orgasm(show_dialogue = False, trance_chance_modifier = self.get_opinion_score("masturbating"), add_to_log = False, fire_event = False)

            remove_list = []
            for serum in self.serum_effects:
                serum.run_on_turn(self) #If a run_on_turn is called and the serum has expired no effects are calculated, so we can safely call this as many times as we want.
                serum.run_on_turn(self) #Night is 3 turn chunks, but one is already called when time progresses. Run serums twice more, and if we've gotten here we also run the on day function.
                serum.run_on_day(self) #Serums that effect people at night must effect two of the three turns.
                if serum.is_expired: #Night is 3 segments, but 1 is allready called when run_turn is called.
                    remove_list.append(serum)

            for serum in remove_list:
                serum.run_on_remove(self)
                self.serum_effects.remove(serum)

            for infraction in self.infractions:
                infraction.days_existed += 1
                if infraction.days_existed > infraction.days_valid:
                    self.remove_infraction(infraction)

            self.situational_sluttiness.clear()
            self.situational_obedience.clear()

            # dominant person slowly bleeds obedience on run_day (lowest point offset by love)
            if self.is_dominant:
                if self.obedience - self.love > 100 - (self.get_opinion_score("taking control") * 5):
                    self.change_obedience(-1, add_to_log = False)

            if day%7 == 0: #If the new day is Monday
                self.change_happiness(self.get_opinion_score("Mondays")*10, add_to_log = False)

            elif day%7 == 4: #If the new day is Friday
                self.change_happiness(self.get_opinion_score("Fridays")*10, add_to_log = False)

            elif day%7 == 5 or day%7 == 6: #If the new day is a weekend day
                self.change_happiness(self.get_opinion_score("the weekend")*10, add_to_log = False)

            for role in self.special_role:
                role.run_day(self)

        def get_display_colour_code(self, saturation = 1.0, given_alpha = 1.0):
            the_colour = Color(self.char.what_args["color"])
            the_colour = the_colour.multiply_hsv_saturation(saturation)
            the_colour = the_colour.multiply_value(saturation)
            the_colour = the_colour.replace_opacity(given_alpha)

            return the_colour.hexcode

        def build_person_portrait(self, special_modifier = None):
            position = "stand5"
            emotion = "happy"
            special_modifier = None
            lighting = [.98,.98,.98]

            disp_key = "P:{}_F:{}_H:{}_HC:{}_EC:{}".format(self.identifier,
                self.face_style, self.hair_style.name,
                hash(tuple(x for x in map(hash, self.hair_style.colour))),
                hash(tuple(x for x in map(hash, self.eyes[1]))))

            if disp_key in portrait_cache:
                return portrait_cache[disp_key]

            displayable_list = []
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair

            x_size, y_size = position_size_dict.get(position)
            composite_list = [(x_size,y_size)]

            for display in displayable_list:
                if isinstance(display, __builtin__.tuple):
                    composite_list.extend(display)
                else:
                    composite_list.append((0,0))
                    composite_list.append(display)

            portrait_cache[disp_key] = AlphaMask(Flatten(Composite(*composite_list)), portrait_mask_image)
            return portrait_cache[disp_key]

        def build_person_displayable(self, position = None, emotion = None, special_modifier = None, lighting = None, hide_list = [], outfit = None, cache_item = True): #Encapsulates what is done when drawing a person and produces a single displayable.
            if position is None:
                position = self.idle_pose
            if emotion is None:
                emotion = self.get_emotion()
            if outfit is None:
                outfit = self.outfit

            forced_special_modifier = self.outfit.get_forced_modifier()
            if forced_special_modifier is not None:
                special_modifier = forced_special_modifier

            disp_key = "ID:{}_P:{}_E:{}_SM:{}_L:{}_O:{}".format(self.identifier, position, emotion, special_modifier, hash(tuple(x for x in map(hash, lighting))), outfit.__hash__())
            if disp_key in character_cache:
                return character_cache[disp_key]

            displayable_list = []
            displayable_list.append(self.body_images.generate_item_displayable(self.body_type,self.tits,position,lighting)) #Add the body displayable
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
            if self.tan_style:
                displayable_list.append(self.tan_style.generate_item_displayable(self.body_type,self.tits, position, lighting = lighting)) # Add the tan
                if self.tan_style.has_extension:
                    displayable_list.append(self.tan_style.has_extension.generate_item_displayable(self.body_type, self.tits, position, lighting = lighting)) # Add the tan
            displayable_list.append(self.pubes_style.generate_item_displayable(self.body_type, self.tits, position, lighting = lighting)) #Add in her pubes

            displayable_list.extend(outfit.generate_draw_list(self,position,emotion,special_modifier, lighting = lighting, hide_layers = hide_list))
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair

            x_size, y_size = position_size_dict.get(position)
            composite_list = [(x_size,y_size)]

            for display in displayable_list:
                if isinstance(display, __builtin__.tuple):
                    composite_list.extend(display)
                else:
                    composite_list.append((0,0))
                    composite_list.append(display)

            character_composite = Composite(*composite_list)

            if persistent.vren_display_pref == "Float" or persistent.vren_display_pref == "Frame":
                character_raw_body = im.Composite((x_size, y_size),
                    (0,0), self.body_images.generate_raw_image(self.body_type,self.tits,position),
                    #(0,0), self.expression_images.generate_raw_image(position, emotion, special_modifier = special_modifier),
                    self.hair_style.crop_offset_dict.get(position,(0,0)), self.hair_style.generate_raw_image("standard_body", self.tits, position))

                blurred_image = im.Blur(character_raw_body, 6)
                aura_colour = self.get_display_colour_code()
                recoloured_blur = im.MatrixColor(blurred_image, im.matrix.colorize(aura_colour, aura_colour))

                final_composite = Composite((x_size, y_size), (0,0), recoloured_blur, (0,0), character_composite)
            else:
                final_composite = character_composite

            # Create a composite image using all of the displayables
            if cache_item:
                character_cache[disp_key] = Flatten(final_composite)
                return character_cache[disp_key]
            return Flatten(final_composite)

        def build_weight_mask(self, the_animation, position, animation_effect_strength): #Builds a weight mask displayable that highlights the sections of a character that should be animated.
            x_size, y_size = position_size_dict.get(position)

            composite_components = []
            region_weight_items_dict = the_animation.get_weight_items()
            for region_weight_name in region_weight_items_dict: #Goes through each region ie. "breasts", "butt", and others to come, and applies the animation strength, the personal region strength, and animation region strength
                the_weight_item = region_weight_items_dict[region_weight_name]
                composite_components.append(the_weight_item.crop_offset_dict.get(position, (0,0)))
                region_weight_modifier = animation_effect_strength * self.personal_region_modifiers.get(region_weight_name, 1) * the_animation.innate_animation_strength * the_animation.region_specific_weights.get(region_weight_name, 1)
                if region_weight_modifier > 1:
                    region_weight_modifier = 1

                region_brightness_matrix = im.matrix.brightness(-1 + region_weight_modifier)
                region_mask = the_weight_item.generate_raw_image(self.body_type, self.tits, position)
                region_mask = im.MatrixColor(region_mask, region_brightness_matrix)
                composite_components.append(region_mask)

            the_mask_composite = im.Composite((x_size, y_size), *composite_components)

            weight_mask = im.Blur(the_mask_composite, 2)

            return weight_mask

        def draw_person(self,position = None, emotion = None, special_modifier = None, show_person_info = True, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0,
            draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True): #Draw the person, standing as default if they aren't standing in any other position
            validate_texture_memory()
            if position is None:
                position = self.idle_pose

            if emotion is None:
                emotion = self.get_emotion()

            if not can_use_animation():
                the_animation = None
            elif the_animation is None: # assign default animation when not passed and enabled
                if position in ["blowjob", "kneeling1"]:
                    the_animation = blowjob_bob
                elif position in ["doggy", "standing_doggy", "back_peek"]:
                    the_animation = ass_bob
                elif position in ["missionary"]:
                    the_animation = missionary_bob
                else:
                    the_animation = self.idle_animation

            if display_transform is None:
                display_transform = character_right

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_zorder is None:
                display_zorder = 0

            at_arguments = [display_transform, scale_person(self.height)]
            if not the_animation is None:
                at_arguments.append(basic_bounce(the_animation))

            if extra_at_arguments:
                if isinstance(extra_at_arguments, list):
                    at_arguments.extend(extra_at_arguments)
                else:
                    at_arguments.append(extra_at_arguments)

            self.hide_person(draw_layer = draw_layer)
            if wipe_scene:
                clear_scene() #Make sure no other characters are drawn either.
                if show_person_info:
                    renpy.show_screen("person_info_ui",self)

            if the_animation:
                weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)
                renpy.show(str(self.identifier), at_list=at_arguments, layer = draw_layer, what = ShaderPerson(self.build_person_displayable(position, emotion, special_modifier, lighting), weight_mask), tag = str(self.identifier))
            else:
                renpy.show(str(self.identifier), at_list=at_arguments, layer = draw_layer, what = self.build_person_displayable(position, emotion, special_modifier, lighting), tag = str(self.identifier))

        def hide_person(self, draw_layer = "solo"): #Hides the person. Makes sure to hide all posible known tags for the character.
            # We keep track of tags used to display a character so that they can always be unique, but still tied to them so they can be hidden
            renpy.hide(str(self.identifier), draw_layer)
            renpy.hide(str(self.identifier) + "_old", draw_layer)

        def draw_animated_removal(self, the_clothing, position = None, emotion = None, show_person_info = True, special_modifier = None, lighting = None, background_fill = "auto", the_animation = None, animation_effect_strength = 1.0, half_off_instead = False,
            draw_layer = "solo", display_transform = None, extra_at_arguments = None, display_zorder = None, wipe_scene = True, scene_manager = None):
            if the_clothing is None:  #we need something to take off
                renpy.say("WARNING", "Draw animated removal called without passing a clothing item.")
                return

            if self.outfit is None:
                renpy.say("WARNING", self.name + " is not wearing any outfit to remove an item from, aborting draw animated removal.")
                return

            if position is None:
                position = self.idle_pose

            if emotion is None:
                emotion = self.get_emotion()

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_transform is None: # make sure we don't need to pass the position with each draw
                display_transform = character_right

            if not can_use_animation():
                the_animation = None
            elif the_animation is None:
                the_animation = self.idle_animation

            at_arguments = [display_transform, scale_person(self.height)]
            if not the_animation is None:
                at_arguments.append(basic_bounce(the_animation))
            if extra_at_arguments:
                if isinstance(extra_at_arguments, list):
                    at_arguments.extend(extra_at_arguments)
                else:
                    at_arguments.append(extra_at_arguments)

            if not isinstance(the_clothing, list):  # convert clothing to list, if not already
                the_clothing = [the_clothing]

            if display_zorder is None:
                display_zorder = 0

            if wipe_scene:
                clear_scene()

            if scene_manager is None and show_person_info:
                renpy.show_screen("person_info_ui",self)
            else:   # when we are called from the scene manager we have to draw the other characters
                scene_manager.draw_scene(exclude_list = [self])

            bottom_displayable = self.build_person_displayable(position, emotion, special_modifier, lighting, cache_item = False) # needs to be flattened for fade to work correctly
            for cloth in the_clothing:
                if half_off_instead:
                    self.outfit.half_off_clothing(cloth) #Half-off the clothing
                else:
                    self.outfit.remove_clothing(cloth) #Remove the clothing
            top_displayable = self.build_person_displayable(position, emotion, special_modifier, lighting, cache_item = False)

            self.hide_person()

            if the_animation:
                weight_mask = self.build_weight_mask(the_animation, position, animation_effect_strength)
                renpy.show(str(self.identifier), at_list=at_arguments, layer = draw_layer, what = ShaderPerson(top_displayable, weight_mask), zorder = display_zorder, tag = str(self.identifier))
                renpy.show(str(self.identifier) + "_old", at_list= at_arguments + [clothing_fade], layer = draw_layer, what = ShaderPerson(bottom_displayable, weight_mask), zorder = display_zorder + 1, tag = str(self.identifier) + "_old") #Overlay old and blend out
            else:
                renpy.show(str(self.identifier), at_list=at_arguments, layer = draw_layer, what = top_displayable, zorder = display_zorder, tag = str(self.identifier))
                renpy.show(str(self.identifier) + "_old", at_list= at_arguments + [clothing_fade], layer = draw_layer, what = bottom_displayable, zorder = display_zorder + 1, tag = str(self.identifier) + "_old") #Overlay old and blend out

            renpy.pause(1.0) # slight pause between animations
            return

        def get_emotion(self): # Get the emotion state of a character, used when the persons sprite is drawn and no fixed emotion is required.
            if self.arousal>= self.max_arousal:
                return "orgasm"

            elif self.happiness > 100:
                return "happy"

            elif self.happiness < 80:
                if self.love > 0:
                    return "sad"
                else:
                    return "angry"

            else:
                return "default"

        def call_dialogue(self, type, *args, **kwargs): #Passes the parameter along to the persons personality and gets the correct dialogue for the event if it exists in the dict.
            if type == "sex_review" and kwargs.get("the_report", {}).get("is_angry", False):
                renpy.say(self, "Now leave me alone, I'm done.")
            else:
                self.personality.get_dialogue(self, type, *args, **kwargs)

        def get_known_opinion_score(self, topic):
            the_topic = self.get_opinion_topic(topic)
            if the_topic is None:
                return 0
            else:
                if the_topic[1]:
                    return the_topic[0]
                return 0

        def get_known_opinion_list(self, include_sexy = False, include_normal = True, only_positive = False, only_negative = False): #Gets the topic string of a random opinion this character holds. Includes options to include known opinions and sexy opinions. Returns None if no valid opinion can be found.
            the_dict = {} #Start our list of valid opinions to be listed as empty

            if include_normal: #if we include normal opinions build a dict out of the two
                the_dict = dict(the_dict, **self.opinions)

            if include_sexy: #If we want sexy opinions add them in too.
                the_dict = dict(the_dict, **self.sexy_opinions)

            known = [x for x in the_dict if the_dict[x][1]]
            if only_positive:
                return [x for x in the_dict if self.get_opinion_score(x) > 0]

            if only_negative:
                return [x for x in the_dict if self.get_opinion_score(x) < 0]

            return the_dict.keys()

        def has_unknown_opinions(self, normal_opinions = True, sexy_opinions = True):
            if normal_opinions:
                return any(x for x in self.opinions if not self.opinions[x][1])

            if sexy_opinions:
                return any(x for x in self.sexy_opinions if not self.sexy_opinions[x][1])

            return False

        def get_opinion_score(self, topic): #Like get_opinion_topic, but only returns the score and not a tuple. Use this when determining a persons reaction to a relevant event.
            if isinstance(topic, basestring):
                if topic in self.opinions:
                    return self.opinions[topic][0]
                if topic in self.sexy_opinions:
                    return self.sexy_opinions[topic][0]

            return_value = 0
            if isinstance(topic, list):
                for a_topic in topic:
                    return_value += self.get_opinion_score(a_topic)
            return return_value

        def get_opinion_topics_list(self, include_unknown = True, include_normal = True, include_sexy = True, include_hate = True, include_dislike = True, include_like = True, include_love = True):
            #TODO: Needs unit testing
            opinion_return_list = []
            lists_to_check = []
            if include_normal:
                for topic in self.opinions:
                    if self.opinions[topic][1] or include_unknown:
                        if self.opinions[topic][0] == -2 and include_hate:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == -1 and include_dislike:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == 1 and include_like:
                            opinion_return_list.append(topic)
                        elif self.opinions[topic][0] == 2 and include_love:
                            opinion_return_list.append(topic)
            if include_sexy:
                for topic in self.sexy_opinions:
                    if self.sexy_opinions[topic][1] or include_unknown:
                        if self.sexy_opinions[topic][0] == -2 and include_hate:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == -1 and include_dislike:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == 1 and include_like:
                            opinion_return_list.append(topic)
                        elif self.sexy_opinions[topic][0] == 2 and include_love:
                            opinion_return_list.append(topic)
            return opinion_return_list

        def get_opinion_topic(self, topic): #topic is a string matching the topics given in our random list (ie. "the colour blue", "sports"). Returns a tuple containing the score: -2 for hates, -1 for dislikes, 0 for no opinion, 1 for likes, and 2 for loves, and a bool to say if the opinion is known or not.
            if topic in self.opinions:
                return self.opinions[topic]

            if topic in self.sexy_opinions:
                return self.sexy_opinions[topic]

            return None

        def get_random_opinion(self, include_known = True, include_sexy = False, include_normal = True, only_positive = False, only_negative = False): #Gets the topic string of a random opinion this character holds. Includes options to include known opinions and sexy opinions. Returns None if no valid opinion can be found.
            the_dict = {} #Start our list of valid opinions to be listed as empty

            if include_normal: #if we include normal opinions build a dict out of the two
                the_dict = dict(the_dict, **self.opinions)

            if include_sexy: #If we want sexy opinions add them in too.
                the_dict = dict(the_dict, **self.sexy_opinions)


            known_keys = []
            if not include_known: #If we do not want to talk about known values
                for k in the_dict: #Go through each value in our combined normal and sexy opinion dict
                    if the_dict[k][1]: #Check if we know about it...
                        known_keys.append(k) #We build a temporary list of keys to remove because otehrwise we are modifying the dict while we traverse it.
                for del_key in known_keys:
                    del the_dict[del_key]

            remove_keys = []
            if only_positive or only_negative: # Let's us filter opinions so they only include possitive or negative ones.
                if only_positive:
                    for k in the_dict:
                        if self.get_opinion_score(k) < 0:
                            remove_keys.append(k)

                if only_negative:
                    for k in the_dict:
                        if self.get_opinion_score(k) > 0:
                            remove_keys.append(k)

                for del_key in remove_keys:
                    del the_dict[del_key]

            if the_dict:
                return get_random_from_list(the_dict.keys()) #If we have something in the list we can return the topic string we used as a key for it. This can then be used with get_opinion_score to get the actual opinion
            else:
                return None #If we have nothing return None, make sure to deal with this when we use this function.

        def discover_opinion(self, topic, add_to_log = True): #topic is a string matching the topics given in our random list (ie. "the colour blue"). If the opinion is in either of our opinion dicts we will set it to known, otherwise we do nothing. Returns True if the opinion was updated, false if nothing was changed.
            updated = False
            if topic in self.opinions:
                if not self.opinions[topic][1]:
                    updated = True
                self.opinions[topic][1] = True

            if topic in self.sexy_opinions:
                if not self.sexy_opinions[topic][1]:
                    updated = True
                self.sexy_opinions[topic][1] = True

            if updated and add_to_log and self.title is not None:
                mc.log_event("Discovered: {} {} {}".format(self.display_name, opinion_score_to_string(self.get_opinion_score(topic)), topic),"float_text_grey")

            return updated

        def set_opinion(self, topic, strength, known = False): #override function to set an opinion to a known value, mainly used to set up characters before they are introduced
            if not strength == 0:
                if topic in self.get_sexy_opinions_list():
                    self.sexy_opinions[topic] = [strength, known]
                else:
                    self.opinions[topic] = [strength, known]
            else:
                if topic in self.opinions:
                    self.opinions.pop(topic)
                if topic in self.sexy_opinions:
                    self.sexy_opinions.pop(topic)

        def update_opinion_with_score(self, topic, score, add_to_log = True):
            if topic in Person._sexy_opinions_list:
                if topic in self.sexy_opinions:
                    self.sexy_opinions[topic][0] = score
                else:
                    self.sexy_opinions[topic] = [score, add_to_log]

            if topic in Person._opinions_list:
                if topic in self.opinions:
                    self.opinions[topic][0] = score
                else:
                    self.opinions[topic] = [score, add_to_log]

            if add_to_log:
                mc.log_event((self.title or self.name) + " " + opinion_score_to_string(score) + " " + str(topic), "float_text_green")
            return

        def strengthen_opinion(self, topic, add_to_log = True):
            old_opinion = self.get_opinion_topic(topic)
            if old_opinion is None: #You cannot strengthen an opinion of 0, for that make a new one entirely.
                return False

            updated = False
            if old_opinion[0] == 1 or old_opinion[0] == -1:
                updated = True
                new_opinion_value = 2*old_opinion[0]
                if topic in self.opinions:
                    self.opinions[topic] = [new_opinion_value, old_opinion[1]]
                else:
                    self.sexy_opinions[topic] = [new_opinion_value, old_opinion[1]]

            if add_to_log and updated:
                mc.log_event("Opinion Strengthened: {} now {} {}".format(self.display_name, opinion_score_to_string(self.get_opinion_score(topic)), topic), "float_text_grey")
            return updated

        def increase_opinion_score(self, topic, max_value = 2, add_to_log = True, weighted = False):
            score = self.get_opinion_score(topic)

            if score < 2 and score < max_value:
                if weighted:
                    if renpy.random.randint(0,100) < self.suggestibility:
                        self.update_opinion_with_score(topic, score + 1, add_to_log)
                else:
                    self.update_opinion_with_score(topic, score + 1, add_to_log)
            return

        def weaken_opinion(self, topic, add_to_log = True):
            old_opinion = self.get_opinion_topic(topic)
            if old_opinion is None: #You cannot weaken an opinion of 0, for that make a new one entirely.
                return False

            updated = False
            if old_opinion[0] == 2 or old_opinion[0] == -2:
                updated = True
                new_opinion_value = old_opinion[0]//2
                if topic in self.opinions:
                    self.opinions[topic] = [new_opinion_value, old_opinion[1]]
                else:
                    self.sexy_opinions[topic] = [new_opinion_value, old_opinion[1]]

            else: #ie it was -1 or 1, because 0 already returned
                updated = True
                if topic in self.opinions:
                    self.opinions.pop(topic)
                elif topic in self.sexy_opinions:
                    self.sexy_opinions.pop(topic)

            if add_to_log and updated:
                mc.log_event("Opinion Weakened: {} now {} {}".format(self.display_name, opinion_score_to_string(self.get_opinion_score(topic)), topic), "float_text_grey")

            return updated

        def decrease_opinion_score(self, topic, add_to_log = True):
            score = self.get_opinion_score(topic)

            if score > -2:
                self.update_opinion_with_score(topic, score - 1, add_to_log)
            return

        def max_opinion_score(self, topic, add_to_log = True):
            score = self.get_opinion_score(topic)
            if score != 2:
                self.update_opinion_with_score(topic, 2, add_to_log)
            return

        def create_opinion(self, topic, start_positive = True, start_known = True, add_to_log = True):
            start_value = 1
            if not start_positive:
                start_value = -1 #Determines if the opinion starts as like or dislike.
            if not self.get_opinion_score(topic) == 0: #She already has an opinion
                return False

            opinion_tuple = [start_value, start_known]
            if topic in self.get_sexy_opinions_list():
                self.sexy_opinions[topic] = opinion_tuple
            else:
                self.opinions[topic] = opinion_tuple

            if add_to_log:
                mc.log_event("Opinion Inspired: {} now {} {}".format(self.display_name, opinion_score_to_string(self.get_opinion_score(topic)), topic), "float_text_grey")
            return True

        def add_opinion(self, topic, score, known = None, sexy_opinion = None, add_to_global = False, add_to_log = True):
            if known is None and topic in self.opinions:
                sexy_opinion = False # override passed value
                known = self.opinions[topic][1]

            if known is None and topic in self.sexy_opinions:
                sexy_opinion = True # override passed value
                known = self.sexy_opinions[topic][1]

            if known is None:
                known = False

            if sexy_opinion is None: # check global list
                sexy_opinion = False
                if topic in Person._sexy_opinions_list:
                    sexy_opinion = True

            if sexy_opinion:
                self.sexy_opinions[topic] = [score, known]

                if add_to_global and topic not in Person._sexy_opinions_list:
                    Person._sexy_opinions_list.append(topic)
            else:
                self.opinions[topic] = [score, known]
                if add_to_global and topic not in Person._opinions_list:
                    Person._opinions_list.append(topic)

            if add_to_log:
                mc.log_event("{} {} {}".format(self.display_name, opinion_score_to_string(score), topic), "float_text_green")

        def reset_opinions(self):
            self.opinions.clear()

        def reset_sexy_opinions(self):
            self.sexy_opinions.clear()

        def has_taboo(self, taboos):
            if taboos is None:
                return False

            if isinstance(taboos, basestring):
                taboos = [taboos]

            return any(x for x in taboos if x not in self.broken_taboos)

        def has_broken_taboo(self, taboos):
            if taboos is None:
                return False

            if isinstance(taboos, basestring):
                taboos = [taboos]

            return any(x for x in taboos if x in self.broken_taboos)

        def break_taboo(self, the_taboo, add_to_log = True, fire_event = True):
            if the_taboo in self.broken_taboos:
                return False

            self.broken_taboos.append(the_taboo)
            self.change_novelty(5, add_to_log = add_to_log)

            if add_to_log:
                mc.log_event("Taboo broken with {}!".format(self.display_name), "float_text_red")

            if fire_event:
                mc.listener_system.fire_event("girl_taboo_break", the_taboo = the_taboo)
            return True

        def restore_taboo(self, the_taboo, add_to_log = True):
            if not the_taboo in self.broken_taboos:
                return False

            while the_taboo in self.broken_taboos:
                self.broken_taboos.remove(the_taboo)

            if add_to_log:
                mc.log_event("Taboo reasserted with {}!".format(self.display_name), "float_text_red")
            return True

        def pick_position_comment(self, the_report): #Takes a report and has the person pick the most notable thing out of it. Generally used to then have them comment on it.
            highest_slut_position = None
            highest_slut_opinion = 0
            for position in the_report.get("positions_used", []):
                slut_opinion = position.slut_requirement
                if position.opinion_tags is not None:
                    for opinion_tag in position.opinion_tags:
                        slut_opinion += 5*self.get_opinion_score(opinion_tag)
                if highest_slut_position is None or slut_opinion > highest_slut_opinion:
                    highest_slut_position = position
                    highest_slut_opinion = slut_opinion

            return highest_slut_position

        @property
        def is_wearing_dress_code(self):
            return self.outfit == self.dress_code_outfit and self.dress_code_outfit != self.planned_outfit

        @property
        def should_wear_dress_code(self):
            if not self.is_at_work:  # quick exit
                return False

            if self.is_employee and not self.is_intern and not self.is_strip_club_employee:
                # Casual fridays for employees only
                if not (day%7 == 4 and casual_friday_uniform_policy.is_active):
                    # Check for dress code and whether planned outfit applies
                    return dress_code_policy.is_active
            return False

        def wear_dress_code(self): #Puts the girl into her uniform, if it exists.
            if self.dress_code_outfit is None:
                self.dress_code_outfit = self.wardrobe.decide_on_uniform(self)

            if self.dress_code_outfit is not None:
                # print("{} - wear dresscode {}".format(self.name, self.dress_code_outfit.name))
                self.apply_outfit(self.dress_code_outfit)
            else:
                # print("{} - no dresscode, wear planned outfit {}".format(self.name, self.planned_outfit.name))
                self.apply_outfit(self.planned_outfit)
            return

        @property
        def current_planned_outfit(self):
            if self.should_wear_uniform and self.planned_uniform:
                return self.planned_uniform
            elif self.should_wear_dress_code and self.dress_code_outfit:
                return self.dress_code_outfit
            elif self.location in [gym, university] and self.location_outfit:
                return self.location_outfit
            return self.planned_outfit

        def set_planned_outfit(self, new_outfit):
            if isinstance(new_outfit, Outfit):
                self.planned_outfit = new_outfit.get_copy() #Get a copy to return to when we are done.
                self.apply_outfit(self.planned_outfit)

        def add_outfit(self,the_outfit, outfit_type = "full"):
            if outfit_type == "under":
                self.wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                self.wardrobe.add_overwear_set(the_outfit)
            else: #outfit_type = full
                self.wardrobe.add_outfit(the_outfit)

        def decide_on_outfit(self, sluttiness_modifier = 0.0):
            return self.wardrobe.decide_on_outfit(self, sluttiness_modifier)

        def get_random_appropriate_outfit(self, sluttiness_limit = None, sluttiness_min = 0, guarantee_output = False):
            outfit = self.wardrobe.get_random_appropriate_outfit(sluttiness_limit = sluttiness_limit or self.effective_sluttiness(), sluttiness_min = sluttiness_min, guarantee_output = guarantee_output, preferences = WardrobePreference(self))
            if guarantee_output and (not outfit or outfit.name == "Nothing"): # when no outfit and we need one, generate one
                outfit = Wardrobe.generate_random_appropriate_outfit(self, sluttiness_limit = sluttiness_limit or self.effective_sluttiness())
            return outfit

        def get_random_appropriate_underwear(self, sluttiness_limit = None, sluttiness_min = 0, guarantee_output = False):
            outfit = self.wardrobe.get_random_appropriate_underwear(sluttiness_limit = sluttiness_limit or self.effective_sluttiness(), sluttiness_min = sluttiness_min, guarantee_output = guarantee_output, preferences = WardrobePreference(self))
            if guarantee_output and (not outfit or outfit.name == "Nothing"): # when no outfit and we need one, generate one
                outfit = Wardrobe.generate_random_appropriate_outfit(self, outfit_type = "under", sluttiness_limit = sluttiness_limit or self.effective_sluttiness())
            return outfit

        def get_random_appropriate_overwear(self, sluttiness_limit = None, sluttiness_min = 0, guarantee_output = False):
            outfit = self.wardrobe.get_random_appropriate_overwear(sluttiness_limit = sluttiness_limit or self.effective_sluttiness(), sluttiness_min = sluttiness_min, guarantee_output = guarantee_output, preferences = WardrobePreference(self))
            if guarantee_output and (not outfit or outfit.name == "Nothing"): # when no outfit and we need one, generate one
                outfit = Wardrobe.generate_random_appropriate_outfit(self, outfit_type = "over", sluttiness_limit = sluttiness_limit or self.effective_sluttiness())
            return outfit

        def personalize_outfit(self, outfit, opinion_color = None, coloured_underwear = False, main_colour = None, swap_bottoms = False, allow_skimpy = True):
            return WardrobeBuilder(self).personalize_outfit(outfit, opinion_color = opinion_color, coloured_underwear = coloured_underwear, main_colour = main_colour, swap_bottoms = swap_bottoms, allow_skimpy = allow_skimpy)

        @property
        def is_wearing_uniform(self): # Returns True if the clothing the girl is wearing contains all of the uniform clothing items. #TODO: may want to support more flexibility for over/underwear sets that had optional bits chosen by the girl.
            #May want to make this a Business side check. Make "is_valid_uniform" check like this against all uniforms available for the character. Would provide the flexiblity I mentioned above.
            if self.planned_uniform is None:
                return False #If no uniform is set you aren't wearing one at all.

            # run extension code
            if casual_friday_uniform_policy.is_active and day % 7 == 4:
                return False

            uniform_wardrobe = mc.business.get_uniform_wardrobe_for_person(self)
            slut_limit, underwear_limit, limited_to_top = mc.business.get_uniform_limits()

            matching_overwear = False
            overwear_set = False #Tracks if we had at least one overwear we _could_ have been wearing

            for potential_uniform in [x for x in uniform_wardrobe.overwear_sets if x.overwear_slut_score <= slut_limit]: #Check if we match the overwear and underwear sets.
                overwear_set = True
                if not matching_overwear:
                    matching_overwear = True
                    for cloth in potential_uniform:
                        if not self.outfit.has_clothing(cloth):
                            matching_overwear = False
                            break

            if limited_to_top:  # quick exit if we only match overwear
                return matching_overwear

            matching_full = False
            full_set = False #Boolean used to track if we have at least one full set we _could_ have been wearing

            matching_underwear = False
            underwear_set = False #Tracks if we had an underwear set we could have been wearing

            for potential_uniform in [x for x in uniform_wardrobe.outfit_sets if x.outfit_slut_score <= slut_limit]: #Check if we match any of the full uniforms
                full_set = True
                if not matching_full:
                    matching_full = True #Assume they match, then find a counter example. When we do, break and try the next one.
                    for cloth in potential_uniform:
                        if not self.outfit.has_clothing(cloth):
                            matching_full = False
                            break

            for potential_uniform in [x for x in uniform_wardrobe.underwear_sets if x.underwear_slut_score <= underwear_limit]:
                underwear_set = True
                if not matching_underwear:
                    matching_underwear = True
                    for cloth in potential_uniform:
                        if not self.outfit.has_clothing(cloth):
                            matching_underwear = False
                            break

            if matching_full:
                return True

            elif matching_overwear and matching_underwear:
                return True

            elif matching_overwear or matching_underwear: #Sometimes this is okay
                if matching_overwear and not underwear_set:
                    return True
                elif matching_underwear and not overwear_set:
                    return True

            return False

        @property
        def should_wear_uniform(self):
            if not self.is_at_work:  # quick exit
                return False

            if self.job in [nurse_job, night_nurse_job, doctor_job]:
                return True

            if self.event_triggers_dict.get("forced_uniform", False):
                return True

            wardrobe = mc.business.get_uniform_wardrobe_for_person(self)
            if not wardrobe or wardrobe.outfit_count == 0:
                return False

            if self.is_strip_club_employee: # no casual friday for strippers (employee moonlighting)
                return True

            if self.is_employee or self.is_intern:
                # Casual fridays for employees only
                if not (day%7 == 4 and casual_friday_uniform_policy.is_active):
                    # Check for uniform
                    return wardrobe.outfit_count != 0
            # Non-employees
            else:
                return True # Everybody else wears a uniform while at work

            return False

        def wear_uniform(self): #Puts the girl into her uniform, if it exists.
            if self.planned_uniform is None:
                if self.event_triggers_dict.get("forced_uniform", False):
                    the_uniform = self.event_triggers_dict.get("forced_uniform")
                else:
                    the_uniform = mc.business.get_uniform_wardrobe_for_person(self).decide_on_uniform(self)
                self.set_uniform(the_uniform, wear_now = False) #If we don't have a uniform planned for today get one.

            if self.planned_uniform is not None: #If our planned uniform is STILL None it means we are unable to construct a valid uniform. Only assign it as our outfit if we have managed to construct a uniform.
                # print("{} - wear uniform {}".format(self.name, self.planned_uniform.name))
                self.apply_outfit(self.planned_uniform) #We apply clothing taboos to uniforms because the character is assumed to have seen them in them.

        def set_uniform(self,uniform, wear_now = True):
            if isinstance(uniform, Outfit):
                self.planned_uniform = uniform.get_copy()
                if wear_now:
                    self.wear_uniform()

        def apply_outfit(self, the_outfit = None, ignore_base = False, update_taboo = False): #Hand over an outfit, we'll take a copy and apply it to the person, along with their base accessories unless told otherwise.
            if the_outfit is None:
                # put on uniform if required
                if self.should_wear_uniform:
                    self.wear_uniform()
                    return

                the_outfit = self.planned_outfit
                if the_outfit is None:
                    return #We don't have a planned outfit, so trying to return to it makes no sense.
            if ignore_base:
                self.outfit = the_outfit.get_copy()
            else:
                self.outfit = the_outfit.get_copy().merge_outfit(self.base_outfit)

            if update_taboo: #If True, we assume this outfit is being put on or shown to the MC. It can break taboos about showing underwear, tits, pussy.
                self.update_outfit_taboos()

        def apply_planned_outfit(self, ignore_base = False, update_taboo = False):
            if time_of_day != 0:    # in timeslot 0 we pick new outfits
                self.restore_all_clothing() # restore half-off clothing items of current outfit.

            if self.should_wear_uniform:
                self.wear_uniform()
            elif self.should_wear_dress_code:
                self.wear_dress_code()
            elif self.location in [gym, university] and self.location_outfit:
                self.apply_outfit(self.location_outfit, ignore_base = ignore_base, update_taboo = update_taboo)
            else:
                if not self.planned_outfit: # extra validation to make sure we have a planned outfit
                    self.planned_outfit = self.decide_on_outfit()

                self.apply_outfit(self.planned_outfit, ignore_base = ignore_base, update_taboo = update_taboo)
            return

        def apply_gym_outfit(self):
            self.location_outfit = self.personalize_outfit(workout_wardrobe.decide_on_outfit(self), allow_skimpy = False)
            self.apply_outfit(self.location_outfit)
            return

        def apply_university_outfit(self):
            if university_wardrobe:
                self.location_outfit = university_wardrobe.decide_on_outfit(self)
                self.apply_outfit(self.location_outfit)
            return

        def apply_yoga_outfit(self):
            # strip to underwear or else pick workout outfit
            if self.effective_sluttiness("underwear_nudity") >= 60:
                if not self.planned_outfit: # make sure we have a planned outfit
                    self.planned_outfit = self.decide_on_outfit()

                yoga_outfit = Outfit("Yoga Outfit")
                yoga_outfit.add_feet(slips.get_copy(), colour_black)    # she always wears slips for yoga
                yoga_outfit.merge_outfit(self.planned_outfit, underwear_only = True)

                # make sure she's not nude (erica nude yoga goes into other function)
                if not yoga_outfit.wearing_bra:
                    item = renpy.random.choice([bralette, lace_bra, strappy_bra])
                    yoga_outfit.add_upper(item.get_copy(), colour_black)
                if not yoga_outfit.wearing_panties:
                    item = renpy.random.choice([cute_lace_panties, thong, strappy_panties])
                    yoga_outfit.add_lower(item.get_copy(), colour_black)

                self.location_outfit = self.personalize_outfit(yoga_outfit, allow_skimpy = False)
            else:
                self.location_outfit = self.personalize_outfit(workout_wardrobe.decide_on_outfit(self), allow_skimpy = False)

            self.apply_outfit(self.location_outfit)
            return

        def apply_yoga_shoes_only(self):
            # for now, just apply a nude outfit with black slips
            outfit = Outfit("Nude")
            outfit.add_feet(slips.get_copy(), colour_black)
            self.apply_outfit(outfit)
            return

        def approves_outfit_color(self, outfit):
            return WardrobeBuilder(self).approves_outfit_color(outfit)

        def review_outfit(self, dialogue = True, draw_person = True):
            if not self.has_cum_fetish:
                self.outfit.remove_all_cum()

            if not self.outfit.matches(self.current_planned_outfit) \
                and (__builtin__.len(self.location.people) > 1 \
                or (self.should_wear_uniform and not self.is_wearing_uniform) \
                or (self.should_wear_dress_code and not self.is_wearing_dress_code) \
                or (self.outfit.outfit_slut_score > self.sluttiness)):
                self.apply_planned_outfit()
                if draw_person:
                    self.draw_person()
                if dialogue:
                    self.call_dialogue("clothing_review") # must be last call in function
            return

        def judge_outfit(self, outfit, temp_sluttiness_boost = 0, use_taboos = True, as_underwear = False, as_overwear = False): #Judge an outfit and determine if it's too slutty or not. Can be used to judge other people's outfits to determine if she thinks they look like a slut.
            # temp_sluttiness can be used in situations (mainly crises) where an outfit is allowed to be temporarily more slutty than a girl is comfortable wearing all the time.
            #Returns true if the outfit is wearable, false otherwise
            if not outfit:
                return False

            if as_underwear or as_overwear:
                use_taboos = False

            taboo_modifier = []
            if use_taboos and not (outfit.bra_covered or outfit.panties_covered) and self.has_taboo("underwear_nudity"):
                taboo_modifier.append("underwear_nudity")
            elif use_taboos and outfit.tits_visible and self.has_taboo("bare_tits"):
                taboo_modifier.append("bare_tits")
            elif use_taboos and outfit.vagina_visible and self.has_taboo("bare_pussy"):
                taboo_modifier.append("bare_pussy")

            slut_required = outfit.outfit_slut_score
            if as_underwear:
                slut_required = outfit.underwear_slut_score

            elif as_overwear:
                slut_required = outfit.overwear_slut_score

            if (outfit.get_bra() or outfit.get_panties()) and not as_overwear: #Girls who like lingerie judge outfits with lingerie as less slutty than normal
                lingerie_bonus = 0
                if outfit.get_bra() and outfit.get_bra().slut_value > 2: #We consider underwear with an innate sluttiness of 3 or higher "lingerie" rather than just underwear.
                    lingerie_bonus += self.get_opinion_score("lingerie")
                if outfit.get_panties() and outfit.get_panties().slut_value > 2:
                    lingerie_bonus += self.get_opinion_score("lingerie")
                lingerie_bonus = __builtin__.int(lingerie_bonus*2) # Up to an 8 point swing in either direction
                slut_required += -lingerie_bonus #Treated as less slutty if she likes it, more slutty if she dislikes lingerie

            # Considers the outfit less slutty if she likes showing her tits and ass and that's what it would do.
            if outfit.vagina_visible or outfit.are_panties_visible:
                slut_required += -2*self.get_opinion_score("showing her ass")

            if outfit.tits_visible or outfit.is_bra_visible:
                slut_required += -2*self.get_opinion_score("showing her tits")

            if slut_required > (self.effective_sluttiness(taboo_modifier) + temp_sluttiness_boost): #Arousal is important for judging potential changes to her outfit while being stripped down during sex.
                return False
            return True

        def update_outfit_taboos(self):
            return_value = False
            if self.tits_visible:
                if self.break_taboo("bare_tits"):
                    return_value = True
            if self.vagina_visible:
                if self.break_taboo("bare_pussy"):
                    return_value = True
            if self.outfit.are_panties_visible or self.outfit.is_bra_visible:
                if self.break_taboo("underwear_nudity"):
                    return_value = True
            return return_value

        def give_serum(self,the_serum_design, add_to_log = True):
            if the_serum_design is None:
                return #We might have handed over no serum because we aren't producing any and a crisis was looking for one, or something similar.
            else:
                the_serum_design = copy.copy(the_serum_design) #Take a copy so we aren't touchinn the reference we are handed.
            self.serum_effects.append(the_serum_design)
            the_serum_design.run_on_apply(self, add_to_log)
            mc.listener_system.fire_event("give_random_serum", the_person = self)

        def apply_serum_study(self, add_to_log = True): #Called when the person is studied by the MC. Raises mastery level of all traits used in active serums by 0.2
            studied_something = False
            for serum in self.serum_effects:
                for trait in serum.traits:
                    trait.add_mastery(0.2)
                    studied_something = True

            if studied_something and add_to_log:
                mc.log_event("Observed {}, mastery of active serum traits increased by 0.2".format(self.display_name), "float_text_blue")

        def change_suggest(self,amount, add_to_log = True): #This changes the base, usually permanent suggest. Use add_suggest_effect to add temporary, only-highest-is-used, suggestion values
            self.suggestibility += amount
            if add_to_log and amount != 0 and self.title:
                mc.log_event("{}: Suggestibility increased permanently by {}{}%".format((self.title or self.name), ("+" if amount > 0 else ""), amount), "float_text_blue")

        # monitor that mc serum suggest change amount does not exceed max_amt
        def change_modded_suggestibility(self, amount, max_amt = 30, add_to_log = True):
            if self.event_triggers_dict.get("mod_suggest_amt", 0) >= max_amt:
                return
            change_amount = amount
            if self.event_triggers_dict.get("mod_suggest_amt", 0) + amount > max_amt:
                change_amount = max_amt - self.event_triggers_dict.get("mod_suggest_amt", 0)
            self.change_suggest(change_amount, add_to_log = add_to_log)
            self.event_triggers_dict["mod_suggest_amt"] = self.event_triggers_dict.get("mod_suggest_amt", 0) + change_amount
            return

        def add_suggest_effect(self,amount, add_to_log = True):
            if amount > __builtin__.max(self.suggest_bag or [0]):
                self.change_suggest(-__builtin__.max(self.suggest_bag or [0]), add_to_log = False) #Subtract the old max and...
                self.change_suggest(amount, add_to_log = False) #add our new suggest.
                if add_to_log and amount != 0 and self.title:
                    mc.log_event("{}: Suggestibility increased, by {}".format((self.title or self.name), amount), "float_text_blue")
            else:
                if add_to_log and amount != 0 and self.title:
                    mc.log_event("{}: Suggestibility {} lower than current {} amount. Suggestibility unchanged.".format((self.title or self.name), amount, self.suggestibility), "float_text_blue")
            self.suggest_bag.append(amount) #Add it to the bag, so we can check to see if it is max later.

        def remove_suggest_effect(self,amount):
            if amount in self.suggest_bag: # Avoid removing the "amount" if we don't actually have it in the bag.
                self.change_suggest(- __builtin__.max(self.suggest_bag or [0]), add_to_log = False) #Subtract the max
                self.suggest_bag.remove(amount)
                self.change_suggest(__builtin__.max(self.suggest_bag or [0]), add_to_log = False) # Add the new max. If we were max, it is now lower, otherwie it cancels out.

        def change_happiness(self,amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount*self.get_trance_multiplier()))
            if self.happiness + amount < 0:
                amount = 0 - self.happiness
            if self.happiness + amount > 300:
                amount = 300 - self.happiness

            self.happiness += amount

            if add_to_log and amount != 0:
                log_string = ("+" if amount > 0 else "") + str(amount) + " {image=happy_token_small}"
                if self.get_trance_multiplier() != 1:
                    log_string += "\nChange amplified by " + str(int((self.get_trance_multiplier()*100)-100)) + "% due to trance"
                mc.log_event(self.display_name + ": " + log_string, "float_text_yellow")
            return amount

        def change_love(self, amount, max_modified_to = None, add_to_log = True):
            if max_modified_to:
                suggestibility_modifier = 0
                if self.suggestibility == 0:
                    pass
                elif self.suggestibility < 20:
                    suggestibility_modifier = __builtin__.int(self.suggestibility / 5.0)
                elif self.suggestibility < 60:
                    suggestibility_modifier = 2 + __builtin__.int(self.suggestibility / 10.0)
                elif self.suggestibility < 120:
                    suggestibility_modifier = 8 + __builtin__.int(self.suggestibility / 20.0)
                else:
                    suggestibility_modifier = 14
                max_modified_to += suggestibility_modifier

            amount = __builtin__.int(__builtin__.round(amount))

            if max_modified_to is not None and self.love + amount > max_modified_to:
                amount = max_modified_to - self.love
                if amount < 0: #Never subtract love because of a cap, only limit how much they gain.
                    amount = 0

            if self.love + amount < -100:
                amount = -100 - self.love
            elif self.love + amount > 100:
                amount = 100 - self.love

            self.love += amount

            if add_to_log:
                if amount == 0:
                    log_string = "Love limit reached for interaction"
                else:
                    log_string = ("+" if amount > 0 else "") + str(amount) + " {image=red_heart_token_small}"
                mc.log_event(self.display_name + ": " + log_string, "float_text_pink")
            return amount

        def change_slut(self, amount, max_modified_to = None, add_to_log = True):
            if max_modified_to:  # change max_modified_to based on suggestibility
                suggestibility_modifier = 0
                if self.suggestibility == 0:
                    pass
                elif self.suggestibility < 20:
                    suggestibility_modifier = __builtin__.int(self.suggestibility / 2.0)
                elif self.suggestibility < 60:
                    suggestibility_modifier = 10 + __builtin__.int((self.suggestibility - 20) / 4.0)
                elif self.suggestibility < 80:
                    suggestibility_modifier = 20 + __builtin__.int((self.suggestibility - 60) / 8.0)
                else:
                    suggestibility_modifier = 30
                max_modified_to += suggestibility_modifier

            # limit sluttiness to 100 -> read as 100%
            # there is no content for higher sluttiness values,
            # but it will impact the game negatively if it is over 100 (bored sex pos etc.)
            if not max_modified_to or max_modified_to > 100:
                max_modified_to = 100

            amount = __builtin__.int(__builtin__.round(amount))

            if max_modified_to and self.sluttiness + amount > max_modified_to:
                amount = max_modified_to - self.sluttiness
                if amount < 0:
                    amount = 0

            if self.sluttiness + amount < 0:
                amount = -self.sluttiness
            elif self.sluttiness + amount > 100:
                amount = 100 - self.sluttiness

            self.sluttiness += amount

            if add_to_log:
                if amount == 0:
                    log_string = "No Effect on Sluttiness"
                else:
                    log_string = ("+" if amount > 0 else "") + str(amount) + " {image=gold_heart_token_small}"
                mc.log_event(self.display_name + ": " + log_string, "float_text_pink")
            return amount

        def add_situational_slut(self, source, amount, description = ""):
            self.situational_sluttiness[source] = (amount,description)

        def clear_situational_slut(self, source):
            self.add_situational_slut(source, 0) #We don't actually ever care if we remove the key, we just want to set the amount to 0.

        def add_situational_obedience(self, source, amount, description = ""):
            if source in self.situational_obedience:
                difference = amount - self.situational_obedience[source][0]
                self.change_obedience(difference, add_to_log = False)
            else:
                self.change_obedience(amount, add_to_log = False)
            self.situational_obedience[source] = (amount,description)

        def clear_situational_obedience(self, source):
            self.add_situational_obedience(source, 0)

        def change_obedience(self,amount, add_to_log = True):
            if self.obedience + amount < 0:
                amount = -self.obedience
            elif self.obedience + amount > 300:
                amount = 300 - self.obedience

            self.obedience += amount

            if add_to_log and amount != 0: #If we don't know the title don't add it to the log, because we know nothing about the person
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) +" {image=triskelion_token_small}"
                mc.log_event(log_string,"float_text_grey")
            return amount

        def change_cha(self, amount, add_to_log = True):
            self.charisma += self.charisma_debt #Set our charisma to be our net score
            self.charisma_debt = 0 #We are currently holding no stat debt.

            self.charisma += amount #Adjust our stat now, may be positive or negative.
            if self.charisma < 0:
                self.charisma_debt = self.charisma #If we are less than 0 store it as a debt.
                self.charisma = 0

            if amount != 0 and add_to_log:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Charisma"
                mc.log_event(log_string, "float_text_grey")

        def change_int(self, amount, add_to_log = True):
            self.int += self.int_debt
            self.int_debt = 0

            self.int += amount
            if self.int < 0:
                self.int_debt = self.int
                self.int = 0

            if amount != 0 and add_to_log:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Intelligence"
                mc.log_event(log_string, "float_text_grey")

        def change_focus(self, amount, add_to_log = True): #See charisma for full comments
            self.focus += self.focus_debt
            self.focus_debt = 0

            self.focus += amount
            if self.focus < 0:
                self.focus_debt = self.focus
                self.focus = 0

            if amount != 0 and add_to_log:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Focus"
                mc.log_event(log_string, "float_text_grey")

        def change_hr_skill(self, amount, add_to_log = True):
            if amount + self.hr_skill < 0:
                amount = -self.hr_skill #Min 0
            self.hr_skill += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " HR Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_market_skill(self, amount, add_to_log = True):
            if amount + self.market_skill < 0:
                amount = -self.market_skill #Min 0
            self.market_skill += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Market Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_research_skill(self, amount, add_to_log = True):
            if amount + self.research_skill < 0:
                amount = -self.research_skill #Min 0
            self.research_skill += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Research Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_production_skill(self, amount, add_to_log = True):
            if amount + self.production_skill < 0:
                amount = -self.production_skill #Min 0
            self.production_skill += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Production Skill"
                mc.log_event(log_string, "float_text_yellow")

        def change_supply_skill(self, amount, add_to_log = True):
            if amount + self.supply_skill < 0:
                amount = -self.supply_skill #Min 0
            self.supply_skill += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Supply Skill"
                mc.log_event(log_string, "float_text_yellow")

        def increase_work_skill(self, skill, max_value = 6, add_to_log = True):
            if skill == 0 or skill == "hr_skill":
                self.update_work_skill("hr_skill", min(max_value, self.hr_skill + 1), add_to_log = add_to_log)
            elif skill == 1 or skill == "market_skill":
                self.update_work_skill("market_skill", min(max_value, self.market_skill + 1), add_to_log = add_to_log)
            elif skill == 2 or skill == "research_skill":
                self.update_work_skill("research_skill", min(max_value, self.research_skill + 1), add_to_log = add_to_log)
            elif skill == 3 or skill == "production_skill":
                self.update_work_skill("production_skill", min(max_value, self.production_skill + 1), add_to_log = add_to_log)
            elif skill == 4 or skill == "supply_skill":
                self.update_work_skill("supply_skill", min(max_value, self.supply_skill + 1), add_to_log = add_to_log)
            return

        def decrease_work_skill(self, skill, add_to_log = True):
            if skill == 0 or skill == "hr_skill":
                self.update_work_skill("hr_skill", max(0, self.hr_skill - 1), add_to_log = add_to_log)
            elif skill == 1 or skill == "market_skill":
                self.update_work_skill("market_skill", max(0, self.market_skill - 1), add_to_log = add_to_log)
            elif skill == 2 or skill == "research_skill":
                self.update_work_skill("research_skill", max(max_value, self.research_skill - 1), add_to_log = add_to_log)
            elif skill == 3 or skill == "production_skill":
                self.update_work_skill("production_skill", max(max_value, self.production_skill - 1), add_to_log = add_to_log)
            elif skill == 4 or skill == "supply_skill":
                self.update_work_skill("supply_skill", max(max_value, self.supply_skill - 1), add_to_log = add_to_log)
            return

        def update_work_skill(self, skill, score, add_to_log = True):
            skill_name = None
            if skill == 0 or skill == "hr_skill":
                skill_name = "HR Skill"
                current = self.hr_skill
            elif skill == 1 or skill == "market_skill":
                skill_name = "Market Skill"
                current = self.market_skill
            elif skill == 2 or skill == "research_skill":
                skill_name = "Research Skill"
                current = self.research_skill
            elif skill == 3 or skill == "production_skill":
                skill_name = "Production Skill"
                current = self.production_skill
            elif skill == 4 or skill == "supply_skill":
                skill_name = "Supply Skill"
                current = self.supply_skill

            if skill_name is None:
                return

            if current == score:
                return
            if skill_name == "HR Skill":
                self.hr_skill = score
            elif skill_name == "Market Skill":
                self.market_skill = score
            elif skill_name == "Research Skill":
                self.research_skill = score
            elif skill_name == "Production Skill":
                self.production_skill = score
            elif skill_name == "Supply Skill":
                self.supply_skill = score

            self.sex_skills[skill] = score
            if add_to_log:
                mc.log_event((self.title or self.name) + " " + skill_name + " is now at level " + str(score), "float_text_green")
            return

        def change_sex_skill(self, skill_name, amount, add_to_log = True): #NOTE: We assume we pass a proper skill name here, otherwise we crash out.
            # ["Foreplay","Oral","Vaginal","Anal"]
            if amount + self.sex_skills[skill_name] < 0:
                amount = -self.sex_skills[skill_name] #At most we make it 0. No negative values.
            self.sex_skills[skill_name] += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " " + skill_name + " Skill"
                mc.log_event(log_string, "float_text_yellow")

        def increase_sex_skill(self, skill, max_value = 5, add_to_log = True):
            if skill not in self.sex_skills:
                return

            score = self.sex_skills[skill]
            if score < max_value:
                self.update_sex_skill(skill, score + 1, add_to_log)
            return

        def decrease_sex_skill(self, skill, add_to_log = True):
            if skill not in self.sex_skills:
                return

            score = self.sex_skills[skill]
            if score > 0:
                self.update_sex_skill(skill, score - 1, add_to_log)
            return

        def update_sex_skill(self, skill, score, add_to_log = True):
            if skill not in self.sex_skills:
                return

            current = self.sex_skills[skill]
            if current == score:
                return

            self.sex_skills[skill] = score
            if add_to_log:
                mc.log_event((self.title or self.name) + " " + skill.lower() + " skill is now at level " + str(score), "float_text_green")
            return

        def change_stats(self, obedience = None, happiness = None, arousal = None, love = None, slut = None, max_slut = None, max_love = None, energy = None, novelty = None, add_to_log = True):
            message = []
            if not happiness is None:
                self.change_happiness(happiness, add_to_log = False)
                if happiness != 0:
                    message.append(("+" if happiness > 0 else "") + str(happiness) + " {image=happy_token_small}")
            if not obedience is None:
                amount = self.change_obedience(obedience, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) +" {image=triskelion_token_small}")
            if not arousal is None:
                amount = self.change_arousal(arousal, add_to_log = False)
                if arousal != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " {image=arousal_token_small}")
            if not love is None:
                amount = self.change_love(love, max_love, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " {image=red_heart_token_small}")
            if not slut is None:
                amount = self.change_slut(slut, max_slut, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " {image=gold_heart_token_small}")
            if not energy is None:
                amount = self.change_energy(energy, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " {image=energy_token_small}")
            if not novelty is None:
                amount = self.change_novelty(novelty, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " Novelty")
            if add_to_log and message:
                mc.log_event(self.display_name + ": " + " ".join(message), "float_text_yellow")
            return

        def change_arousal(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if self.arousal + amount < 0:
                amount = 0 - self.arousal

            self.arousal += amount
            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " {image=arousal_token_small}"
                mc.log_event(log_string, "float_text_red")
            return amount

        def reset_arousal(self):
            base_arousal = self.sluttiness / 10.0
            base_arousal += self.get_opinion_score("masturbating")
            base_arousal += self.get_opinion_score("showing her tits")
            base_arousal += self.get_opinion_score("showing her ass")
            base_arousal += self.get_opinion_score("not wearing underwear")

            if base_arousal < 0:
                base_arousal = 0

            self.arousal = __builtin__.round(base_arousal)

        def change_max_arousal(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.max_arousal < 20:
                amount = -(self.max_arousal - 20)

            self.max_arousal += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Max Arousal"
                mc.log_event(log_string, "float_text_red")
            return amount

        def change_novelty(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.novelty > 100:
                amount = 100 - self.novelty
            elif amount + self.novelty < 0:
                amount = self.novelty
            self.novelty += amount

            if add_to_log and amount != 0:
                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + str(amount) + " Novelty"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def change_energy(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.energy > self.max_energy:
                amount = self.max_energy - self.energy
            elif amount + self.energy < 0:
                amount = -self.energy

            self.energy += amount

            if add_to_log and amount != 0:
                log_string = self.display_name+ ": " + ("+" if amount > 0 else "") + str(amount) + " {image=energy_token_small}"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def change_max_energy(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.max_energy < 0:
                amount = -self.max_energy

            self.max_energy += amount

            if self.energy > self.max_energy: #No having more energy than max
                self.energy = self.max_energy

            if add_to_log and amount != 0:
                log_string = self.display_name+ ": " + ("+" if amount > 0 else "") + str(amount) + " Max Energy"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        ## STRIP OUTFIT TO MAX SLUTTINESS EXTENSION
        # Strips down the person to a clothing their are comfortable with (starting with top, before bottom)
        # narrator_messages: narrator voice after each item of clothing stripped, use '[person.<title>]' for titles and '[strip_choice.name]' for clothing item.
            # Can be an array of messages for variation in message per clothing item or just a single string or None for silent stripping
        # scene manager parameter is filled from that class so that all people present in scene are drawn
        def strip_outfit_to_max_sluttiness(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, narrator_messages = None, display_transform = None, lighting = None, temp_sluttiness_boost = 0, position = None, emotion = None, scene_manager = None, wipe_scene = False):
            # internal function to strip top clothing first.
            def get_strip_choice_max(outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
                strip_choice = None
                if not exclude_upper:
                    strip_choice = outfit.remove_random_upper(top_layer_first)
                if strip_choice is None:
                    strip_choice = outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet)
                return strip_choice

            def get_messages(narrator_messages):
                messages = []
                if not narrator_messages:
                    pass
                elif not isinstance(narrator_messages, list):
                    messages = [narrator_messages]
                else:
                    messages = narrator_messages
                return messages

            messages = get_messages(narrator_messages)
            msg_count = __builtin__.len(messages)

            test_outfit = self.outfit.get_copy()
            removed_something = False

            strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)
            # renpy.say(None, strip_choice.name + "  (required: " + str(test_outfit.outfit_slut_score) +  ", sluttiness: " +  str(self.effective_sluttiness() + temp_sluttiness_boost) + ")")
            while strip_choice and self.judge_outfit(test_outfit, temp_sluttiness_boost):
                if delay > 0:
                    self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                    if msg_count == 0:
                        renpy.pause(delay) # if no message to show, wait a short while before automatically continue stripping
                else:
                    test_outfit.remove_clothing(strip_choice)
                self.apply_outfit(test_outfit, ignore_base = True) #Swap our current outfit out for the test outfit.
                removed_something = True
                if msg_count > 0:   # do we need to show a random message and replace titles and outfit name
                    msg_idx = renpy.random.randint(1, msg_count)
                    msg = messages[msg_idx - 1]
                    msg = msg.replace("[the_person.possessive_title]", self.possessive_title or "the unknown woman").replace("[the_person.title]", self.title or self.name).replace("[the_person.mc_title]", self.mc_title).replace("[strip_choice.name]", strip_choice.name).replace("[strip_choice.display_name]", strip_choice.display_name)
                    renpy.say(None, msg)

                strip_choice = get_strip_choice_max(test_outfit, top_layer_first, exclude_upper, exclude_lower, exclude_feet)

            return removed_something

        def strip_to_underwear(self, visible_enough = True, avoid_nudity = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
            strip_list = self.outfit.get_underwear_strip_list(visible_enough = visible_enough, avoid_nudity = avoid_nudity)
            self.__strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
            return

        def strip_to_tits(self, visible_enough = True, prefer_half_off = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
            half_off_instead = False
            if prefer_half_off and self.outfit.can_half_off_to_tits(visible_enough = visible_enough):
                strip_list = self.outfit.get_half_off_to_tits_list(visible_enough = visible_enough)
                half_off_instead = True
            else:
                strip_list = self.outfit.get_tit_strip_list(visible_enough = visible_enough)
            self.__strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
            return

        def strip_to_vagina(self, visible_enough = False, prefer_half_off = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
            half_off_instead = False
            if prefer_half_off and self.outfit.can_half_off_to_vagina(visible_enough = visible_enough):
                strip_list = self.outfit.get_half_off_to_vagina_list(visible_enough = visible_enough)
                half_off_instead = True
            else:
                strip_list = self.outfit.get_vagina_strip_list(visible_enough = visible_enough)
            self.__strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
            return

        def strip_full_outfit(self, strip_feet = False, strip_accessories = False, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, delay = 1):
            strip_list = self.outfit.get_full_strip_list(strip_feet = strip_feet, strip_accessories = strip_accessories)
            self.__strip_outfit_strip_list(strip_list, position = position, emotion = emotion, display_transform = display_transform, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene, delay = delay)
            return

        def strip_outfit(self, top_layer_first = True, exclude_upper = False, exclude_lower = False, exclude_feet = True, delay = 1, display_transform = None, position = None, emotion = None, lighting = None, scene_manager = None, wipe_scene = False):
            def extra_strip_check(person, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
                done = exclude_upper or person.tits_available
                if done and (exclude_lower or person.vagina_available):
                    if done and (exclude_feet or person.outfit.feet_available):
                        return False

                return True # not done continue stripping

            if position is None:
                self.position = self.idle_pose

            if emotion is None:
                self.emotion = self.get_emotion()

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_transform is None:
                display_transform = character_right

            strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)
            while not strip_choice is None and extra_strip_check(self, top_layer_first, exclude_upper, exclude_lower, exclude_feet):
                if delay > 0:
                    self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                    renpy.pause(delay)
                else:
                    self.outfit.remove_clothing(strip_choice)
                strip_choice = self.outfit.remove_random_any(top_layer_first, exclude_upper, exclude_lower, exclude_feet, do_not_remove = True)

            # special case where she is wearing a two-part item that blocks her vagina, but we need it be available
            if not exclude_lower and not self.vagina_available:
                strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)
                while not strip_choice is None:
                    if delay > 0:
                        self.draw_animated_removal(strip_choice, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                        renpy.pause(delay)
                    else:
                        self.outfit.remove_clothing(strip_choice)
                    strip_choice = self.outfit.remove_random_any(top_layer_first, False, exclude_lower, exclude_feet, do_not_remove = True)

        def choose_strip_clothing_item(self):
            clothing = None
            # If she has a preference (even a least-bad preference) she'll strip that down first.
            if self.get_opinion_score("showing her tits") > self.get_opinion_score("showing her ass"):
                clothing = self.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, exclude_lower = True, do_not_remove = True)
            elif self.get_opinion_score("showing her tits") < self.get_opinion_score("showing her ass"):
                clothing = self.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, exclude_upper = True, do_not_remove = True)
            if clothing is None: #Either our previous checks failed to produce anything OR they were equal
                clothing = self.outfit.remove_random_any(top_layer_first = True, exclude_feet = True, do_not_remove = True)
            return clothing

        @property
        def job_happiness_score(self):
            happy_points = self.happiness - 100 #Happiness over 100 gives a bonus to staying, happiness less than 100 gives a penalty
            happy_points += max(-20, self.obedience - 90) #A more obedient character is more likely to stay, even if they're unhappy. Even highly independant girls will stay if they are happy and/or paid well
            happy_points += self.salary - self.calculate_base_salary() #A real salary greater than her base is a bonus, less is a penalty. TODO: Make this dependent on salary fraction, not abosolute pay.
            happy_points += self.get_opinion_score("working") * 5 # Does she like working? It affects her happiness score.

            if self.days_employed < 14:
                happy_points += 14 - self.days_employed #Employees are much less likely to quit over the first two weeks.
            return happy_points

        def get_no_condom_threshold(self, situational_modifier = 0):
            if self.knows_pregnant:
                return 0 #You can't get more pregnant, so who cares?

            if self.has_breeding_fetish:
                return 0 #She _wants_ to get knocked up. This will probably trigger other dialogue as well.

            no_condom_threshold = 50 + (self.get_opinion_score("bareback sex") * -10) + situational_modifier
            if any(relationship in [sister_role,mother_role,aunt_role,cousin_role] for relationship in self.special_role):
                no_condom_threshold += 10

            if persistent.pregnancy_pref == 0:
                no_condom_threshold += 10 #If pregnancy content is being ignored we return to the baseline of 60
            elif self.on_birth_control: #If there is pregnancy content then a girl is less likely to want a condom when using BC, much more likely to want it when not using BC.
                no_condom_threshold -= 20

            return no_condom_threshold

        def wants_condom(self, situational_modifier = 0, use_taboos = True):
            taboo_modifier = 0
            if use_taboos and self.effective_sluttiness("condomless_sex") < self.get_no_condom_threshold(situational_modifier = situational_modifier):
                return True
            elif self.effective_sluttiness() < self.get_no_condom_threshold(situational_modifier = situational_modifier):
                return True
            return False

        @property
        def has_family_taboo(self): #A check to see if we should use an incest taboo modifier.
            if self.get_opinion_score("incest") > 0: #If she thinks incest is hot she doesn't have an incest taboo modifier. Maybe she should, but it should just be reduced? For now this is fine.
                return False

            elif self.is_family:
                return True

            return False

        @property
        def has_large_tits(self): #Returns true if the girl has large breasts. "D" cups and up are considered large enough for titfucking, swinging, etc.
            return Person.rank_tits(self.tits) > 5

        def increase_tit_size(self):
            new_tits = Person.get_larger_tit(self.tits)
            if new_tits != self.tits:
                self.tits = new_tits
                self.personal_region_modifiers["breasts"] += 0.1

        def decrease_tit_size(self):
            new_tits = Person.get_smaller_tit(self.tits)
            if new_tits != self.tits:
                self.tits = new_tits
                self.personal_region_modifiers["breasts"] -= 0.1

        @property
        def wants_creampie(self): #Returns True if the girl is going to use dialogue where she wants you to creampie her, False if she's going to be angry about it. Used to help keep dialogue similar throughout events
            # when breeding fetish, she always wants a creampie
            if self.has_breeding_fetish:
                return True
            if persistent.pregnancy_pref == 3 and self.is_highly_fertile and self.baby_desire > 200:
                return True

            creampie_threshold = 75
            if self.on_birth_control:
                creampie_threshold -= 20 #Much more willing to let you creampie her if she's on BC

            if girlfriend_role in self.special_role:
                creampie_threshold -= 10 + (5 * self.get_opinion_score("being submissive")) #Desire to be a "good wife"

            if self.is_family: # If she hates incest, it increases the treshhold
                creampie_threshold += 10 - (10 * self.get_opinion_score("incest"))

            # if she hates bareback sex, it increases the threshold
            creampie_threshold += (-10 * self.get_opinion_score("bareback sex"))

            effective_slut = self.effective_sluttiness("creampie") + (10 * self.get_opinion_score("creampies")) + (10 * self.get_opinion_score("anal creampies"))
            if effective_slut >= creampie_threshold or self.knows_pregnant:
                return True

            return False

        def days_from_ideal_fertility(self):
            day_difference = abs((day % 30) - self.ideal_fertile_day)
            if day_difference > 15:
                day_difference = 30 - day_difference #Wrap around to get correct distance between months.
            return day_difference

        def update_birth_control_knowledge(self, force_known_state = None, force_known_day = None): #Called any time a girl gives you information about her BC. Allows for an up to date detailed info screen that doesn't give more than you know
            if force_known_state is None: #Useful when you an event changes a girls BC and you can expect that she's not going to be on birth control the next day.
                known_state = self.on_birth_control
            else:
                known_state = force_known_day

            if force_known_day is None:
                known_day = day
            else:
                known_day = force_known_day

            self.event_triggers_dict["birth_control_status"] = known_state
            self.event_triggers_dict["birth_control_known_day"] = known_day

        @property
        def is_mc_father(self):
            return self.event_triggers_dict.get("preg_mc_father", True)

        @property
        def has_child_with_mc(self):
            return self.sex_record.get("Children with MC", 0) > 0

        @property
        def number_of_children_with_mc(self):
            return self.sex_record.get("Children with MC", 0)

        @property
        def is_pregnant(self):
            if self.has_role(pregnant_role):
                return True
            return False

        @property
        def is_lactating(self):
            return self.lactation_sources > 0

        @property
        def knows_pregnant(self):
            if self.is_pregnant:
                return self.event_triggers_dict.get("preg_knows", False)
            return False

        @property
        def pregnancy_due_day(self):
            if self.is_pregnant:
                return self.event_triggers_dict.get("preg_finish_announce_day", 0)
            return -1

        @property
        def pregnancy_is_visible(self):
            if self.is_pregnant:
                return day > self.pregnancy_show_day
            return False

        @property
        def pregnancy_show_day(self):
            if self.is_pregnant:
                return self.event_triggers_dict.get("preg_transform_day", 0)
            return -1

        @property
        def baby_desire(self):
            return self._baby_desire

        @baby_desire.setter
        def baby_desire(self, value):
            self._baby_desire = value

        def change_baby_desire(self, value):
            if self.baby_desire + value < -500:
                self.baby_desire = -500
            elif self.baby_desire + value > 500:
                self.baby_desire = 500
            else:
                self.baby_desire += value

        @property
        def is_highly_fertile(self):
            if self.is_pregnant:
                return False
            if persistent.pregnancy_pref < 2:
                return False
            day_difference = __builtin__.abs((day % 30) - self.ideal_fertile_day) # Gets the distance between the current day and the ideal fertile day.
            if day_difference > 15:
                day_difference = 30 - day_difference #Wrap around to get correct distance between months.
            if day_difference < 4:
                return True
            return False

        def effective_sluttiness(self, taboos = None): #Used in sex scenes where the girl will be more aroused, making it easier for her to be seduced.
            if taboos is None:
                taboos = []
            elif not isinstance(taboos, list): #Handles handing over a single item without pre-wrapping it for "iteration".
                taboos = [taboos]

            return_amount = __builtin__.int(self.sluttiness + (self.arousal/4))

            for taboo in taboos:
                if taboo not in self.broken_taboos: #If any of the taboo handed over are not already broken this person has a -15 effective sluttiness.
                    return_amount += -10
                    break #Only appies once, so break once the mallus is applied.


            for source in self.situational_sluttiness:
                return_amount += self.situational_sluttiness[source][0]

            return return_amount

        # runner method for triggering orgasm in serums or day loops (from dialogs use .have_orgasm())
        def run_orgasm(self, show_dialogue = True, force_trance = False, trance_chance_modifier = 0, add_to_log = True, sluttiness_increase_limit = 30, reset_arousal = True, fire_event = True):
            self.change_slut(1, sluttiness_increase_limit, add_to_log = add_to_log)
            if fire_event:
                mc.listener_system.fire_event("girl_climax", the_person = self)
            if renpy.random.randint(0,100) < self.suggestibility + trance_chance_modifier or force_trance:
                self.increase_trance(show_dialogue = show_dialogue, reset_arousal = reset_arousal, add_to_log = add_to_log)

        @property
        def is_in_trance(self):
            return self.has_role([trance_role, heavy_trance_role, very_heavy_trance_role])

        @property
        def is_in_very_heavy_trance(self):
            return self.has_role([very_heavy_trance_role])

        @property
        def trance_training_availabe(self):
            return self.is_in_trance and self.event_triggers_dict.get("trance_training_available", True)

        def increase_trance(self, show_dialogue = True, reset_arousal = True, add_to_log = True):
            if not self.has_role(trance_role):
                self.add_role(trance_role)
                mc.listener_system.fire_event("girl_trance", the_person = self)
                if add_to_log:
                    mc.log_event(self.display_name + " sinks into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + "'s eyes lose focus slightly as she slips into a climax induced trance.")

            elif self.has_exact_role(trance_role):
                self.remove_role(trance_role)
                self.add_role(heavy_trance_role)
                if add_to_log:
                    mc.log_event(self.display_name + " sinks deeper into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + " seems to lose all focus as her brain slips deeper into a post-orgasm trance.")

            elif self.has_exact_role(heavy_trance_role):
                self.remove_role(heavy_trance_role)
                self.add_role(very_heavy_trance_role)
                if add_to_log:
                    mc.log_event(self.display_name + " sinks deeper into a trance!", "float_text_red")
                if show_dialogue:
                    renpy.say(None, self.possessive_title + "'s eyes glaze over, and she sinks completely into a cum addled trance.")

            if reset_arousal:
                self.reset_arousal() #TODO: Decide if resetting should only halve it, like making a girl cum yoruself.

        def get_trance_multiplier(self):
            if self.has_exact_role(trance_role):
                return 1.5
            elif self.has_exact_role(heavy_trance_role):
                return 2.0
            elif self.has_exact_role(very_heavy_trance_role):
                return 3.0
            return 1.0

        def allow_position(self, position):
            if position.opinion_tags:
                for opinion in position.opinion_tags:
                    if self.get_known_opinion_score(opinion) == -2:
                        if self.has_role(slave_role) and self.obedience > 200: #A slave does what she is told.
                            return True
                        if perk_system.has_ability_perk("Serum: Aura of Compliance") and mc_serum_aura_obedience.trait_tier >= 3:
                            return True
                        return False
            return True

        def is_position_filtered(self, position):
            # return the function for that characters position filter (or None)
            def character_position_filter(person, position = "foreplay"):
                func_name = "{}_{}_position_filter".format(person.name.lower(), position.lower())
                if func_name in globals():
                    return globals()[func_name]
                return None

            pos_filter = character_position_filter(self, position.skill_tag)
            if callable(pos_filter):
                return not pos_filter([1, position])
            return False

        def is_willing(self, the_position, private = True):
            final_slut_requirement, final_slut_cap = the_position.calculate_position_requirements(self, False)
            # DON'T USE EFFECTIVE SLUTTINESS IN THIS FUNCTION
            # IT CAN HAVE THE MODIFIERS THAT THIS FUNCTION EMULATES
            # TO VALIDATE PRIOR TO ACTUALLY STARTING THE SEX LOOP
            # IT VALIDATES IF SHE IS WILLING BY HERSELF (NOT USING OBEDIENCE)

            # quick exit for hate
            if not self.allow_position(the_position):
                # print("Position not allowed for " + self.name)
                return False

            # quick exit for custom blocking of position (story line)
            if self.is_position_filtered(the_position):
                # print("Position is filtered for " + self.name)
                return False

            # she hates one of the associated opinions
            for opinion in the_position.opinion_tags:
                if self.get_opinion_score(opinion) <= -2:
                    return False

            # print("Initial requirement: {}".format(final_slut_requirement))
            if self.has_role(prostitute_role):
                final_slut_requirement -= 20        # prostitutes are more willing by nature
            elif self.relationship == "Girlfriend":
                final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 2  # love negates requirement penalty
            elif self.relationship == "Fiancée":
                final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 3  # love negates requirement penalty
            elif self.relationship == "Married":
                final_slut_requirement -= (self.get_opinion_score("cheating on men") - 2) * 5 # love negates requirement penalty
            # print("After relation modifier: {}".format(final_slut_requirement))

            if not private:
                multiplier = 5 if self.sluttiness < 50 else 2
                final_slut_requirement -= (self.get_opinion_score("public sex") - 2) * multiplier # love negates requirement penalty
                # print("After private modifier: {}".format(final_slut_requirement))

            if self.love < 0:   # the more they hate you the higher the requirement
                final_slut_requirement += __builtin__.int(self.love * .2)
            else:
                if self.has_role([girlfriend_role, affair_role]):               # girlfriend lowers requirement by love
                    final_slut_requirement -= __builtin__.int(self.love * .2)
                elif self.is_family:
                    final_slut_requirement -= __builtin__.int((self.love - 50) * .2)  # family only lowers if they love you enough
                else:
                    final_slut_requirement -= __builtin__.int((self.love - 50) * .1)  # default only lowers if they love you enough
            # print("After love modifier: {}".format(final_slut_requirement))

            final_slut_requirement -= __builtin__.int((self.happiness - 120) * .2) # happiness only lowers requirement if they have a good mood
            # print("After happiness modifier: {}".format(final_slut_requirement))

            # obedience can lower / increase requirement by up to 30 points
            # at default obedience of 100 increases requirement by 10 points
            final_slut_requirement -= __builtin__.int((self.obedience - 150) * .2)
            # print("After obedience modifier: {}".format(final_slut_requirement))

            # print("Position: " + the_position.name + "[Sluttiness: " + str(self.sluttiness) + ", Required: " + str(final_slut_requirement) + "]")
            if self.sluttiness >= final_slut_requirement:
                return True
            return False

        def unlock_spanking(self, add_to_log = True):
            if self.can_be_spanked:
                return False
            self.event_triggers_dict["unlock_spanking"] = True
            if add_to_log:
                mc.log_event((self.title or self.name) + " can now be spanked during sex.",  "float_text_green")
            return True

        @property
        def can_be_spanked(self):
            return self.event_triggers_dict.get("unlock_spanking", False)

        @property
        def generic_orgasm_arousal_modifier(self):
            total_amount = 0
            if not mc.condom:
                total_amount += 2 * self.get_opinion_score("bareback sex")
            else:
                total_amount -= 2 * self.get_opinion_score("bareback sex")
            if self.relationship != "Single":
                total_amount += 2 * self.get_opinion_score("cheating on men")
            return total_amount

        @property
        def birthcontrol_efficiency(self):
            if not self.on_birth_control:
                return 0

            PERCENTAGES = [100, 100, 90, 99]
            return PERCENTAGES[persistent.pregnancy_pref] - self.bc_penalty

        @property
        def effective_fertility(self):
            if persistent.pregnancy_pref == 0 or self.fertility_percent < 0:
                return 0

            fertility = self.fertility_percent
            if persistent.pregnancy_pref > 1:
                day_difference = self.days_from_ideal_fertility() # Gets the distance between the current day and the ideal fertile day.
                multiplier = 2 - (float(day_difference)/10.0) # The multiplier is 2 when the day difference is 0, 0.5 when the day difference is 15.
                fertility = self.fertility_percent * multiplier

            if persistent.pregnancy_pref == 3:
                if self.baby_desire < -400:
                    fertility = fertility / 4
                elif self.baby_desire < 400:
                    fertility = fertility / 2
            return fertility

        @property
        def pregnancy_chance(self):
            if self.effective_fertility <= 0:
                return 0
            return (self.effective_fertility / 100) * (100-self.birthcontrol_efficiency)

        def did_she_become_pregnant(self, mc_father = True):
            if persistent.pregnancy_pref == 0 or self.has_role(pregnant_role):
                return False

            # Pregnancy Check #
            if renpy.random.randint(0,100) < self.effective_fertility: #There's a chance she's pregnant
                if renpy.random.randint(0,100) >= self.birthcontrol_efficiency: # Birth control failed to prevent the pregnancy
                    become_pregnant(self, mc_father = mc_father) #Function in role_pregnant establishes all of the pregnancy related variables and events.
                    return True

            return False

        def cum_in_mouth(self, add_to_record = True): #Add the appropriate stuff to their current outfit, and peform any personal checks if rquired.
            mc.listener_system.fire_event("sex_cum_mouth", the_person = self)
            if self.outfit.can_add_accessory(mouth_cum):
                the_cumshot = mouth_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("drinking cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("drinking cum"), add_to_log = add_to_record)
            self.discover_opinion("drinking cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum in Mouth"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["mouth_cum"] = report_log.get("mouth_cum", 0) + 1

            perk_system.perk_on_cum(the_person = self, the_place = "drinking cum", add_to_log = add_to_record)
            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["drinking cum"] = report_log.get("drinking cum", 0) + 1
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("drinking cum"), add_to_log = add_to_record)

        def cum_in_vagina(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_vagina", the_person = self)
            if self.outfit.can_add_accessory(creampie_cum):
                the_cumshot = creampie_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            slut_change_amount =  self.get_opinion_score("creampies")

            if self.wants_creampie:
                self.change_happiness(5*self.get_opinion_score("creampies"), add_to_log = add_to_record)
            else:
                self.change_happiness(-5 + (5*self.get_opinion_score("creampies")), add_to_log = add_to_record)
                self.change_love(-2 + self.get_opinion_score("creampies"), add_to_log = add_to_record)
                slut_change_amount += self.get_opinion_score("being_submissive")

            self.change_slut(slut_change_amount, add_to_log = add_to_record)
            self.discover_opinion("creampies", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Vaginal Creampies"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["creampies"] = report_log.get("creampies", 0) + 1

            self.did_she_become_pregnant()

            perk_system.perk_on_cum(the_person = self, the_place = "creampies", add_to_log = add_to_record)
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("creampies"), add_to_log = add_to_record)


        def cum_in_ass(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_ass", the_person = self)
            #TODO: Add an anal specific cumshot once we have renders for it.
            if self.outfit.can_add_accessory(creampie_cum):
                the_cumshot = creampie_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            if not self.wants_creampie:
                self.change_love(-2 + self.get_opinion_score("anal creampies"), add_to_log = add_to_record)

            self.change_happiness(5 * self.get_opinion_score("anal creampies"), add_to_log = add_to_record)
            self.change_slut(self.get_opinion_score("anal creampies"), add_to_log = add_to_record)
            self.discover_opinion("anal creampies", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Anal Creampies"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["anal creampies"] = report_log.get("anal creampies", 0) + 1

            perk_system.perk_on_cum(the_person = self, the_place = "anal creampies", add_to_log = add_to_record)
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("anal creampies"), add_to_log = add_to_record)

        def cum_on_face(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_on_face", the_person = self)
            if self.outfit.can_add_accessory(face_cum):
                the_cumshot = face_cum.get_copy()
                the_cumshot.layer = 0
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("cum facials"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("cum facials"), add_to_log = add_to_record)
            self.discover_opinion("cum facials", add_to_log = add_to_record)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Facials"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["facials"] = report_log.get("facials", 0) + 1

            perk_system.perk_on_cum(the_person = self, the_place = "cum facials", add_to_log = add_to_record)
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("cum facials"), add_to_log = add_to_record)

        def cum_on_tits(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_on_tits", the_person = self)
            if self.outfit.can_add_accessory(tits_cum):
                the_cumshot = tits_cum.get_copy()
                upper_item = self.outfit.get_upper_top_layer
                if upper_item:
                    top_layer = upper_item.layer
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer + 1
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1

            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on tits"] = report_log.get("cum on tits", 0) + 1
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)

        def cum_on_stomach(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_on_stomach", the_person = self)
            if self.outfit.can_add_accessory(stomach_cum):
                the_cumshot = stomach_cum.get_copy()
                upper_item = self.outfit.get_upper_top_layer
                if upper_item:
                    top_layer = upper_item.layer
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer + 1
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1

            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on stomach"] = report_log.get("cum on stomach", 0) + 1
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)

        def cum_on_ass(self, add_to_record = True):
            mc.listener_system.fire_event("sex_cum_on_ass", the_person = self)
            if self.outfit.can_add_accessory(ass_cum):
                the_cumshot = ass_cum.get_copy()
                lower_item = self.outfit.get_lower_top_layer
                if lower_item:
                    top_layer = lower_item.layer
                else:
                    top_layer = -1
                the_cumshot.layer = top_layer + 1
                self.outfit.add_accessory(the_cumshot)

            self.change_slut(self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.change_happiness(5*self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)
            self.discover_opinion("being covered in cum", add_to_log = add_to_record)

            if add_to_record:
                self.sex_record["Cum Covered"] += 1

            if "report_log" in globals():   # add to report log if exists
                report_log["body_cum"] = report_log.get("body_cum", 0) + 1

            if "report_log" in globals() and add_to_record:   # add to report log if exists
                report_log["cum on ass"] = report_log.get("cum on ass", 0) + 1
            self.change_arousal(self.generic_orgasm_arousal_modifier + 5 * self.get_opinion_score("being covered in cum"), add_to_log = add_to_record)

        @property
        def stripper_salary(self):
            return self._stripper_salary

        @stripper_salary.setter
        def stripper_salary(self, value):
            self._stripper_salary = value

        def change_salary(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if self.salary + amount < 0:
                amount = -self.salary

            self.salary += amount
            if add_to_log and amount != 0:
                self.set_event_day("last_raise")

                log_string = self.display_name + ": " + ("+" if amount > 0 else "") + "$" + str(amount) + "/Day"
                mc.log_event(log_string, "float_text_green")
            return amount

        #TODO: We should add an "expected salary modifier" field, so people who are interns don't get angry about it.
        def calculate_base_salary(self): #returns the default value this person should be worth on a per day basis.
            return __builtin__.int(((self.int + self.focus + self.charisma)*2 + (self.hr_skill + self.market_skill + self.research_skill + self.production_skill + self.supply_skill)) * self.salary_modifier * (0.5+0.25*self.work_experience))

        def calculate_job_salary(self, salary_modifier = None): #NOTE: base_salary includes self.salary_modifier.
            if salary_modifier is None:
                salary_modifier = 1.0
            return __builtin__.int(self.calculate_base_salary() * salary_modifier * self.job.wage_adjustment);

        def calculate_job_efficiency(self):
            return self.job.productivity_adjustment * self.productivity_adjustment;

        def set_schedule(self, the_location, the_days = None, the_times = None):
            self.schedule.set_schedule(the_location, the_days, the_times)

        def set_override_schedule(self, the_location, the_days = None, the_times = None):
            self.override_schedule.set_schedule(the_location, the_days, the_times)

        def copy_schedule(self): #Returns a properly formatted dict without references to the current schedule.
            return self.schedule.get_copy()
            #TODO: Should this return some sort of overlapped work/life schedule?

        def get_destination(self, specified_day = None, specified_time = None): #TODO: Needs to check against personal and work schedule
            if not self.available:  # special case to make people disappear (used in pregnancy)
                return purgatory

            override_return = self.override_schedule.get_destination(specified_day, specified_time)
            if override_return is not None:
                return override_return

            work_return = self.job.schedule.get_destination(specified_day, specified_time)
            if work_return is not None:
                return work_return #our job is telling us to be somewhere, so go there

            return self.schedule.get_destination(specified_day, specified_time) #Otherwise, go where we want.

        def get_next_destination(self):
            override_return = self.override_schedule.get_next_destination()
            if override_return is not None:
                return override_return

            work_return = self.job.schedule.get_next_destination()
            if work_return is not None:
                return work_return

            return self.schedule.get_next_destination()

        def person_meets_requirements(self, slut_required = 0, slut_max = 2000, obedience_required = 0, obedience_max = 2000, love_required = -200, love_max = 2000):
            if self.sluttiness >= slut_required and self.sluttiness <= slut_max and self.obedience >= obedience_required and self.obedience <= obedience_max and self.love >= love_required and self.love <= love_max:
                return True
            return False

        def create_formatted_title(self, the_title):
            formatted_title = "{color=" + self.char.who_args["color"] + "}" + "{font=" + self.char.what_args["font"] + "}" + the_title + "{/font}{/color}"
            return formatted_title

        def set_title(self, new_title): #Takes the given title and formats it so that it will use the characters font colours when the_person.title is used.
            self.char.name = new_title #This ensures the dialogue name is correct for the new title.
            self.title = self.create_formatted_title(new_title)

        def set_possessive_title(self, new_title):
            self.possessive_title = self.create_formatted_title(new_title)

        def set_mc_title(self, new_title):
            self.mc_title = new_title

        def personalise_text(self, what):
            for text_modifier in self.text_modifiers:
                what = text_modifier(self, what)

            return what

        def has_job(self, job):
            if not self.job:
                return False

            if isinstance(job, basestring):
                return self.job.job_title == job
            elif isinstance(job, list):
                return self.job in job

            return self.job == job

        def has_job_role(self, job_role):
            if not self.job:
                return False

            if job_role in self.job.job_roles:
                return True
            return False

        def change_job(self, new_job, job_known = True): #Start a new job, quitting your old one if nessesary
            if self.job and new_job == self.job: #Don't do anything if we already have this job.
                return

            if self.job: # If we had a job before we should quit it. Should only come up on init (after that we're always Unemployed, which is still a Job)
                if self.job.quit_function:
                    self.job.quit_function(self)

                for role in self.job.job_roles: #Remove any job roles that aren't shared with the new job (we do this to maintain linkd roles which are still valid)
                    if not role in new_job.job_roles:
                        self.remove_role(role)

                for old_duty in self.duties:
                    if not old_duty in new_job.mandatory_duties + new_job.available_duties: #
                        self.remove_duty(old_duty) #Remove duties that aren't available in the new job

            if callable(new_job.hire_function):
                new_job.hire_function(self)

            for role in new_job.job_roles:
                if not self.has_exact_role(role):
                    self.add_role(role)

            for new_duty in new_job.mandatory_duties:
                if new_duty not in self.duties:
                    self.add_duty(new_duty)

            self.limit_duties() # Make sure we don't have too many duties after changing our job.

            self.job = new_job

            self.salary = self.calculate_job_salary()
            self.event_triggers_dict["job_known"] = job_known

        def quit_job(self): #Quit and become unemployed
            self.change_job(unemployed_job)

        def add_duty(self, the_duty):
            if the_duty not in self.duties: #Isn't possible to have the same duty twice.
                if the_duty.on_apply is not None:
                    the_duty.on_apply(self)
                self.duties.append(the_duty)

        def remove_duty(self, the_duty):
            if the_duty in self.duties:
                if the_duty.on_remove is not None:
                    the_duty.on_remove(self)
                self.duties.remove(the_duty)

        def has_duty(self, the_duty):
            for a_duty in self.duties:
                if a_duty == the_duty:
                    return True
            return False

        def limit_duties(self): #Checks if we are over our duty limit and removes non-mandatory duties until we are under
            if len(self.duties) > self.work_experience:
                over_count = len(self.duties) - self.work_experience
                for a_duty in self.duties[::-1]: #Traverse the list backwards, so the most recently added duty is first trimmed.
                    if a_duty not in self.job.mandatory_duties:
                        self.remove_duty(a_duty)
                        over_count += -1
                        if over_count == 0:
                            break
            return

        def get_duty_actions(self):
            return_list = []
            for duty in self.duties:
                if self.is_at_work or not duty.only_at_work:
                    for act in duty.actions:
                        if act not in return_list: #Trim duplicates out of our duty list (NOTE: maybe we want to trim them out at the UI level?)
                            return_list.append(act)
            return return_list

        def get_duty_internet_actions(self):
            return_list = []
            for duty in self.duties:
                if self.is_at_work or not duty.only_at_work:
                    for act in duty.internet_actions:
                        if act not in return_list:
                            return_list.append(act)
            return return_list

        def add_role(self, role):
            if not isinstance(role, Role):
                return False

            added = False
            if not role in self.special_role:
                self.special_role.append(role)
                added = True

            if not added:
                return False

            # special condition if she hates kissing, but becomes your girlfriend or paramour she would allow kissing
            if self.get_opinion_score("kissing") <= -2 and role in [girlfriend_role, affair_role, harem_role]:
                self.increase_opinion_score("kissing")

            # special situation if she gets girlfriend role, she loses affair role and SO
            if role == girlfriend_role:
                self.remove_role(affair_role)
                self.relationship = "Single" #Technically they aren't "single", but the MC has special roles for their girlfriend.
                self.SO_name = None

            if role == harem_role:
                self.remove_role(girlfriend_role)
                mc.business.event_triggers_dict["harem_mansion_unlocked"] = True

            return added

        def remove_role(self, role, remove_all = False, remove_linked = True):
            if role in self.special_role:
                self.special_role.remove(role)
                if remove_linked:
                    for linked_role in role.linked_roles:
                        self.remove_role(role, remove_all, remove_linked)
                return True
            return False

        def has_role(self, role):
            if isinstance(role, basestring):
                return any(x for x in self.special_role if x.role_name == role) \
                    or any(x for x in self.special_role if x.check_parent_role(role))
            elif isinstance(role, list):
                return any(x in self.special_role for x in role) \
                    or any(y.check_parent_role(x) for y in self.special_role for x in role)

            return role in self.special_role \
                or any(x for x in self.special_role if x.check_parent_role(role))

        def has_exact_role(self, role): #As has_role, but checks against all roles and all of their looks_like roles.
            if role in self.special_role:
                return True
            return False

        def get_role_reference(self, role_or_rolename):
            for role in self.special_role:
                if isinstance(role_or_rolename, Role) and role == role_or_rolename:
                    return role
                if isinstance(role_or_rolename, basestring) and role.role_name == role_or_rolename:
                    return role
            return None

        def has_queued_event(self, action_or_name):
            return self.on_room_enter_event_list.has_action(action_or_name) \
                or self.on_talk_event_list.has_action(action_or_name)

        def add_infraction(self, the_infraction, add_to_log = True, require_policy = True):
            if office_punishment.is_active or not require_policy:
                self.infractions.append(the_infraction)
                if add_to_log:
                    mc.log_event(self.display_name + " committed infraction: " + the_infraction.name + ", Severity " + str(the_infraction.severity), "float_text_grey")

        def remove_infraction(self, the_infraction):
            if the_infraction in self.infractions:
                self.infractions.remove(the_infraction)

        def set_eye_colour(self, new_colour):
            new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
            eye_colour_name = closest_eye_color(new_colour).capitalize()
            eye_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

            self.eyes = [eye_colour_name, eye_colour_list]
            return

        def set_hair_colour(self, new_colour, change_pubes = True, darken_pubes_amount = 0.07):
            #NOTE: new_colour should be a Ren'py colour.
            new_colour = Color(rgb=(new_colour.rgb)) #Make sure we don't have any alpha problems.
            hair_colour_name = closest_hair_colour(new_colour).capitalize()
            hair_colour_list = [new_colour.rgb[0], new_colour.rgb[1], new_colour.rgb[2], 1.0]

            self.hair_colour = [hair_colour_name, hair_colour_list]

            if change_pubes:
                pubes_colour = new_colour.shade(1.0-darken_pubes_amount)
                self.pubes_style.colour = [pubes_colour.rgb[0], pubes_colour.rgb[1], pubes_colour.rgb[2], 1.0]
                self.pubes_colour = self.pubes_style.colour
            self.hair_style.colour = hair_colour_list

        def get_milk_trait(self): # Generates a milk trait that can be used any time you harvest lactating milk. #TODO: Add ways to give this trait augments, like +duration or it suppresses side effects.
            milk_trait = SerumTrait(self.title + "'s Breast Milk",
                "Fresh breast milk produced by " +  self.possessive_title + ". Valuable to the right sort of person.",
                sexual_aspect = 2, medical_aspect = 2)
            return milk_trait

        def get_titles(self): #Returns a list of character titles this person can have. A title is what you call a person, often but not always their name or based on their name.
            list_of_titles = []

            personality_titles = self.personality.get_personality_titles(self)
            if isinstance(personality_titles, list):
                list_of_titles.extend(personality_titles)
            else:
                list_of_titles.append(personality_titles)

            if self.sluttiness > 20:
                if self.obedience > 150:
                    list_of_titles.append("Slave")


            if self.sluttiness > 60:
                list_of_titles.append("Slut")
                if self.obedience > 140:
                    list_of_titles.append("Cocksleeve")
                    list_of_titles.append("Cock Slave")

                if Person.rank_tits(self.tits) >= 9:
                    list_of_titles.append("Melony")
                elif Person.rank_tits(self.tits) == 0:
                    list_of_titles.append("Sweet Pea")
                elif Person.rank_tits(self.tits) >= 4:
                    list_of_titles.append("Big Tits")
                else:
                    list_of_titles.append("Little Tits")

                if self.sex_record.get("Vaginal Creampies", 0) >= 20:
                    list_of_titles.append("Breeding Material")

            if self.sluttiness > (70 - (self.get_opinion_score("drinking cum")*5 + self.get_opinion_score("creampies")*5 + self.get_opinion_score("cum facials")*5 + self.get_opinion_score("being covered in cum")*5)):
                if self.sex_record.get("Cum Facials", 0) > 5 or self.sex_record.get("Cum in Mouth", 0) > 5 or self.sex_record.get("Cum Covered", 0) > 5:
                    list_of_titles.append("Cumslut")

            if self.sluttiness > (70 - (self.get_opinion_score("bareback sex")*5 + self.get_opinion_score("creampies")*5)):
                if self.sex_record.get("Vaginal Creampies", 0) > 5 or self.sex_record.get("Anal Creampies", 0) > 5:
                    list_of_titles.append("Cumdump")

            if self.love >= 60 and self.has_role(girlfriend_role):
                list_of_titles.append("Love")

            if self.love < 0:
                list_of_titles.append("Cunt")
                list_of_titles.append("Bitch")

            if self.love >= 95:
                list_of_titles.append("Honey")
                list_of_titles.append("Darling")

            if self not in unique_character_list:
                if self.love > 30 and self.height > 1.1:
                    list_of_titles.append("Sexy Legs")
                    list_of_titles.append("Sky High")

                if self.love > 30 and self.height < 0.8:
                    list_of_titles.append("Tinkerbell")
                    list_of_titles.append("Little Lady")

                if self.love > 30 and self.sluttiness > 20 and self.get_opinion_score("high heels") >= 2:
                    list_of_titles.append("Killer Heels")

                if self.sluttiness > 80:
                    list_of_titles.append("Whore")

                if self.sluttiness > 50 and self.has_job(stripper_job):
                    list_of_titles.append("Pole-Slut")
                if self.love > 50 and self.has_job(stripclub_mistress_job):
                    list_of_titles.append("Milady")
                if self.sluttiness > 60 and self.has_job(stripclub_mistress_job):
                    list_of_titles.append("Mistress")

            if self.has_child_with_mc or (self.knows_pregnant and self.is_mc_father):
                list_of_titles.append("Wife")
                list_of_titles.append("Waifu")

            return list(set(list_of_titles))


            return list(set(list_of_titles)) #We return the list so that it can be presented to the player. In general the girl will always want to pick the first one on the list.

        def get_random_title(self):
            return get_random_from_list(self.get_titles())

        def get_possessive_titles(self):
            list_of_titles = []
            #Your mother and sister both have specific personality types, so they get their family titles there.

            personality_possessive_titles = self.personality.get_personality_possessive_titles(self)
            if isinstance(personality_possessive_titles, list):
                list_of_titles.extend(personality_possessive_titles)
            else:
                list_of_titles.append(personality_possessive_titles)

            if self.has_role(employee_role):
                list_of_titles.append("Your employee")
                if self.sluttiness > 60:
                    list_of_titles.append("Your office slut")

            if self.love > 10:
                list_of_titles.append("Your friend")

            if self.obedience > 150:
                list_of_titles.append("Your slave")
                if self.sluttiness > 60:
                    list_of_titles.append("Your dedicated cocksleeve")


            if self.sluttiness > 60:
                if self.int <= 1 and self.has_large_tits:
                    list_of_titles.append("Your airhead bimbo")


                if self.love > 50:
                    list_of_titles.append("Your personal slut")
                elif self.love < 0:
                    list_of_titles.append("Your hatefuck slut")
                else:
                    list_of_titles.append("Your slut")

                if self.kids > 0:
                    list_of_titles.append("Your slutty MILF")

                if not self.is_single:
                    list_of_titles.append("Your cheating slut")

                if self.sex_record.get("Vaginal Creampies", 0) >= 20:
                    list_of_titles.append("Your breeder")

            if self.sluttiness > (70 - (self.get_opinion_score("drinking cum")*5 + self.get_opinion_score("creampies")*5 + self.get_opinion_score("cum facials")*5 + self.get_opinion_score("being covered in cum")*5)):
                if self.sex_record.get("Cum Facials", 0) > 5 or self.sex_record.get("Cum in Mouth", 0) > 5 or self.sex_record.get("Cum Covered", 0) > 5:
                    list_of_titles.append("Your cumslut")

                if self.sex_record.get("Vaginal Creampies", 0) > 5 or self.sex_record.get("Anal Creampies", 0) > 5:
                    list_of_titles.append("Your cumdump")



            if self.love >= 60 and self.has_role(girlfriend_role):
                list_of_titles.append("Your love")
                list_of_titles.append("Your girlfriend")

            if self.love >= 60 and self.has_role(affair_role):
                list_of_titles.append("Your lover")

            if self.has_role([generic_student_role]):
                list_of_titles.append("Your student")

            if self not in unique_character_list:
                if self.sluttiness > 80:
                    list_of_titles.append("Your whore")

                if self.has_job(stripper_job):
                    list_of_titles.append("Your exotic dancer")
                if self.love > 50 and self.has_job(stripclub_mistress_job):
                    list_of_titles.append("Your burlesque queen")
                if self.sluttiness > 50 and self.has_job(stripclub_mistress_job):
                    list_of_titles.append("Your kinky Mistress")
                if self.has_job(stripclub_waitress_job):
                    list_of_titles.append("Your waitress")
                if self.sluttiness > 50 and self.has_job(stripclub_manager_job):
                    list_of_titles.append("Your naughty Manager")

            if self.has_child_with_mc or (self.knows_pregnant and self.is_mc_father):
                list_of_titles.append("Your wife")
                list_of_titles.append("Your partner")
                list_of_titles.append("Your waifu")

            return list(set(list_of_titles))

        def get_random_possessive_title(self):
            return get_random_from_list(self.get_possessive_titles())

        def get_player_titles(self):
            list_of_titles = ["Mr. " + mc.last_name, mc.name]
            personality_player_titles = self.personality.get_personality_player_titles(self)
            if isinstance(personality_player_titles, list):
                list_of_titles.extend(personality_player_titles)
            else:
                list_of_titles.append(personality_player_titles)

            if self.love >= 95:
                list_of_titles.append("Honey")
                list_of_titles.append("Darling")

            if self.is_employee:
                if self.obedience > 120:
                    list_of_titles.append("Sir")
                elif self.obedience < 80 and self.is_employee:
                    list_of_titles.append("Boss")

            if self.obedience > 140 and self.sluttiness > 50:
                list_of_titles.append("Master")

            if self.sluttiness > 50:
                if self.love > 50:
                    list_of_titles.append("Daddy")
                elif self.love < 0:
                    list_of_titles.append("Fuck Meat")
                    list_of_titles.append("Cunt Slave")
                else:
                    list_of_titles.append("Boy Toy")

            if self.has_role([generic_student_role]):
                list_of_titles.append("Teacher")

            if self.has_child_with_mc or (self.knows_pregnant and self.is_mc_father):
                list_of_titles.append("Husband")
                list_of_titles.append("Hubby")

            return list(set(list_of_titles))

        def get_random_player_title(self):
            return get_random_from_list(self.get_player_titles())


        def remove_person_from_game(self):
            if self in list_of_people:  # remove from global people list
                list_of_people.remove(self)

            if self.home in list_of_places:
                # only remove home when not 'dungeon' or any other character has same home location
                if not self.home == dungeon and not any(x.home == self.home for x in known_people_in_the_game(excluded_people = [self])):
                    list_of_places.remove(self.home) # remove home location from list_of_places
            if self.home in mc.known_home_locations:
                mc.known_home_locations.remove(self.home) # remove home location from known_home_locations

            # cleanup crisis events where person is in argument list
            for crisis_store in [mc.business.mandatory_crises_list, mc.business.mandatory_morning_crises_list]:
                for crisis in crisis_store[:]:
                    args = crisis.args
                    if not isinstance(args, list):
                        args = [args]

                    if any(x for x in args if x == self):
                        crisis_store.remove(crisis)

            # remove from business teams
            for team in [mc.business.research_team, mc.business.market_team, mc.business.supply_team, mc.business.production_team, mc.business.hr_team]:
                if self in team:
                    team.remove(self)

            # remove from business rooms
            for room in [mc.business.s_div, mc.business.r_div, mc.business.p_div, mc.business.m_div, mc.business.h_div]:
                if self in room.people:
                    room.remove_person(self)

            # remove from stripclub
            for team in [stripclub_strippers, stripclub_bdsm_performers, stripclub_waitresses]:
                if self in team:
                    team.remove(self)

            # remove from relationships array
            town_relationships.remove_all_relationships(self)

            self.base_outfit = None
            self.planned_outfit = None
            self.planned_uniform = None

            if self.wardrobe:
                self.wardrobe.clear_wardrobe()
                self.wardrobe = None

            if self.special_role:
                self.special_role.clear()
            if self.on_room_enter_event_list:
                self.on_room_enter_event_list.clear()
            if self.on_talk_event_list:
                self.on_talk_event_list.clear()
            if self.event_triggers_dict:
                self.event_triggers_dict.clear()
            if self.suggest_bag:
                self.suggest_bag.clear()
            if self.broken_taboos:
                self.broken_taboos.clear()
            if self.sex_record:
                self.sex_record.clear()
            if self.opinions:
                self.opinions.clear()
            if self.sexy_opinions:
                self.sexy_opinions.clear()

            # clear all references held by person object.
            self.schedule = None
            self.override_schedule = None
            self.home = None
            self.job = None
            self.relationship = None
            self.personality = None
            self.char = None
            self.body_images = None
            self.face_style = None
            self.hair_colour = None
            self.hair_style = None
            self.pubes_style = None
            self.skin = None
            self.eyes = None
            self.serum_effects = None
            self.personal_region_modifiers = None
            self.situational_sluttiness = None
            self.situational_obedience = None
            # now let the Garbage Collector do the rest (we are no longer referenced in any objects).
            return


        def __strip_outfit_strip_list(self, strip_list, position = None, emotion = None, display_transform = None, lighting = None, scene_manager = None, wipe_scene = False, half_off_instead = False, delay = 1):
            if position is None:
                self.position = self.idle_pose

            if emotion is None:
                self.emotion = self.get_emotion()

            if lighting is None:
                lighting = mc.location.get_lighting_conditions()

            if display_transform is None:
                display_transform = character_right

            for item in strip_list:
                if delay > 0:
                    self.draw_animated_removal(item, display_transform = display_transform, position = position, emotion = emotion, lighting = lighting, half_off_instead = half_off_instead, scene_manager = scene_manager, wipe_scene = wipe_scene) #Draw the strip choice being removed from our current outfit
                    renpy.pause(delay)
                else:
                    self.outfit.remove_clothing(item)
            return

##########################################
# Expose outfit methods on Person object #
##########################################

        @property
        def tits_available(self):
            return self.outfit.tits_available

        @property
        def tits_visible(self):
            return self.outfit.tits_visible

        @property
        def vagina_available(self):
            return self.outfit.vagina_available

        @property
        def vagina_visible(self):
            return self.outfit.vagina_visible

        @property
        def underwear_visible(self):
            return self.outfit.underwear_visible

        @property
        def wearing_bra(self):
            return self.outfit.wearing_bra

        @property
        def wearing_panties(self):
            return self.outfit.wearing_panties

        @property
        def bra_covered(self):
            return self.outfit.bra_covered

        @property
        def panties_covered(self):
            return self.outfit.panties_covered

        @property
        def has_underwear(self):
            return self.outfit.has_underwear

        @property
        def is_wearing_underwear(self):
            return self.outfit.is_wearing_underwear

        @property
        def is_bra_visible(self):
            return self.outfit.is_bra_visible

        @property
        def are_panties_visible(self):
            return self.outfit.are_panties_visible

        @property
        def get_bra(self):
            return self.outfit.get_bra()

        @property
        def get_panties(self):
            return self.outfit.get_panties()

        @property
        def can_remove_bra(self):
            return self.outfit.can_remove_bra

        @property
        def can_remove_panties(self):
            return self.outfit.can_remove_panties

        @property
        def has_mouth_cum(self):
            return self.outfit.has_mouth_cum

        @property
        def has_tits_cum(self):
            return self.outfit.has_tits_cum

        @property
        def has_stomach_cum(self):
            return self.outfit.has_stomach_cum

        @property
        def has_face_cum(self):
            return self.outfit.has_face_cum

        @property
        def has_ass_cum(self):
            return self.outfit.has_ass_cum

        @property
        def has_creampie_cum(self):
            return self.outfit.has_creampie_cum

        def restore_all_clothing(self):
            return self.outfit.restore_all_clothing()

        def get_full_strip_list(self, strip_feet = True, strip_accessories = False):
            return self.outfit.get_full_strip_list(strip_feet, strip_accessories)

        def get_underwear_strip_list(self, visible_enough = True, avoid_nudity = False):
            return self.outfit.get_underwear_strip_list(visible_enough, avoid_nudity)

        def can_half_off_to_tits(self, visible_enough = True):
            return self.outfit.can_half_off_to_tits(visible_enough)

        def get_half_off_to_tits_list(self, visible_enough = True):
            return self.outfit.get_half_off_to_tits_list(visible_enough)

        def get_tit_strip_list(self, visible_enough = True):
            return self.outfit.get_tit_strip_list(visible_enough)

        def can_half_off_to_vagina(self, visible_enough = True):
            return self.outfit.can_half_off_to_vagina(visible_enough)

        def get_half_off_to_vagina_list(self, visible_enough = True):
            return self.outfit.get_half_off_to_vagina_list(visible_enough)

        def get_vagina_strip_list(self, visible_enough = True):
            return self.outfit.get_vagina_strip_list(visible_enough)

        # wrapper for girl in charge
        def get_sex_goal(self):
            return self.event_triggers_dict.get("sex_goal", None)

        # determine girl cum preference
        def facial_or_swallow(self):    #Use this function to determine if girl wants a facial or to swallow cum. If neither is preferred, return one at random.
            if self.has_cum_fetish or self.get_opinion_score("cum facials") == self.get_opinion_score("drinking cum"):
                return renpy.random.choice(["swallow", "facial"])
            if self.get_opinion_score("cum facials") > self.get_opinion_score("drinking cum"):
                return "facial"
            return "swallow"


##################################################
#    Body descriptor python wrappers             #
##################################################

        @property
        def body_is_thin(self):
            return self.body_type == "thin_body"

        @property
        def body_is_average(self):
            return self.body_type == "standard_body"

        @property
        def body_is_thick(self):
            return self.body_type == "curvy_body"

        @property
        def body_is_pregnant(self):
            return self.body_type == "standard_preg_body"

##################################################
#     Fetish related wrappers                    #
##################################################

        @property
        def fetish_count(self):
            return __builtin__.len([x for x in self.special_role if x in [anal_fetish_role, cum_fetish_role, breeding_fetish_role, exhibition_fetish_role]])

        @property
        def has_anal_fetish(self):
            return self.has_role(anal_fetish_role)

        @property
        def has_cum_fetish(self):
            return self.has_role(cum_fetish_role)

        @property
        def has_breeding_fetish(self):
            return self.has_role(breeding_fetish_role)

        @property
        def has_exhibition_fetish(self):
            return self.has_role(exhibition_fetish_role)

        @property
        def has_started_anal_fetish(self):
            return self.event_triggers_dict.get("anal_fetish_start", False)

        @property
        def has_started_breeding_fetish(self):
            return self.event_triggers_dict.get("breeding_fetish_start", False)

        @property
        def has_started_cum_fetish(self):
            return self.event_triggers_dict.get("cum_fetish_start", False)

        @property
        def has_started_exhibition_fetish(self):
            return self.event_triggers_dict.get("exhibition_fetish_start", False)


##########################################
# Roleplay functions                     #
##########################################

        def change_to_lingerie(self):
            if self.event_triggers_dict.get("girlfriend_sleepover_lingerie", None):
                self.apply_outfit(self.event_triggers_dict.pop("girlfriend_sleepover_lingerie"))
            elif self.event_triggers_dict.get("favorite_lingerie", None):
                self.apply_outfit(self.event_triggers_dict.get("favorite_lingerie", None))
            elif len(self.wardrobe.underwear_sets) > 0:
                self.apply_outfit(get_random_from_list(self.wardrobe.underwear_sets))
            else:
                self.apply_outfit(lingerie_wardrobe.pick_random_outfit())
            return

        def roleplay_mc_title_swap(self, new_title):
            self.event_triggers_dict["backup_mc_title"] = self.mc_title
            self.set_mc_title(new_title)
            return

        def roleplay_mc_title_revert(self):
            self.mc_title = self.event_triggers_dict.get("backup_mc_title", mc.name)
            return

        def roleplay_title_swap(self, new_title):
            self.event_triggers_dict["backup_title"] = self.title
            self.set_title(new_title)
            return

        def roleplay_title_revert(self):
            self.title = self.event_triggers_dict.get("backup_title", self.name)
            return

        def roleplay_possessive_title_swap(self, new_title):
            self.event_triggers_dict["backup_possessive_title"] = self.possessive_title
            self.set_possessive_title(new_title)
            return

        def roleplay_possessive_title_revert(self):
            self.possessive_title = self.event_triggers_dict.get("backup_possessive_title", self.name)
            return

        def roleplay_personality_swap(self, personality):
            self.event_triggers_dict["backup_personality"] = self.personality
            self.personality = personality
            return

        def roleplay_personality_revert(self):
            self.personality = self.event_triggers_dict.get("backup_personality", relaxed_personality)
            return


##########################################
# Misc                                   #
##########################################

        @property
        def is_intern(self):
            return self.has_role(college_intern_role)

        @property
        def is_jealous(self):
            if self.love > 90 or self.obedience > 200:
                return False
            if not (self.is_girlfriend or self.is_affair):
                return False
            if self == sarah and sarah_threesomes_unlocked():
                return False
            return self.event_triggers_dict.get("is_jealous", True)

        @property
        def is_free_use(self):  #Use this function to determine if the girl is very slutty and basically down for anything.
            if self.sluttiness < 80:
                return False
            # Doesn't hate any sexual actions
            if any(x for x in self.sexy_opinions if self.get_opinion_score(x) < -1):
                return False
            return not self.has_taboo(["vaginal_sex", "anal_sex"])

        def have_orgasm(self, half_arousal = True, force_trance = False, trance_chance_modifier = 0, sluttiness_increase_limit = 30, reset_arousal = False, add_to_log = True):
            play_female_orgasm()
            mc.listener_system.fire_event("girl_climax", the_person = self)

            self.run_orgasm(show_dialogue = add_to_log, force_trance = force_trance, trance_chance_modifier = trance_chance_modifier, add_to_log = add_to_log, sluttiness_increase_limit = sluttiness_increase_limit, reset_arousal = reset_arousal, fire_event = False)
            self.change_happiness(3, add_to_log = add_to_log)

            if half_arousal:
                self.change_arousal(-self.arousal/2, add_to_log = add_to_log)
            elif "report_log" in globals():
                self.change_arousal(-__builtin__.max((self.arousal/(report_log.get("girl orgasms", 0)+2))+20, self.arousal - self.max_arousal - 1), add_to_log = add_to_log)
            else:
                self.change_arousal(-self.arousal, add_to_log = add_to_log)

            if "report_log" in globals():
                report_log["girl orgasms"] = report_log.get("girl orgasms", 0) + 1
            return

        @property
        def favourite_colour(self):
            favourite_colour = self.event_triggers_dict.get("favourite_colour", None)

            #check if current favourite is still in list_of favourites
            list_of_favourites = [x for x in WardrobeBuilder.color_prefs.keys() if self.get_opinion_score(x) == 2]
            if favourite_colour in list_of_favourites:
                return favourite_colour

            # we need to find a new favorite colour going forward
            if len(list_of_favourites) > 0:
                new_favourite = renpy.random.choice(list_of_favourites)
            else:
                new_favourite = renpy.random.choice(WardrobeBuilder.color_prefs.keys())
                self.set_opinion(new_favourite, 2)

            self.event_triggers_dict["favourite_colour"] = new_favourite
            return new_favourite

        @property
        def has_story(self):
            return any(x for x in progress_list if x.person == self)

        @property
        def progress(self):
            return next((x for x in progress_list if x.person_identifier == self.identifier), None)

        def tag_sex_record(self, record_class = None):    #Tag a sex record for later comparison
            if not isinstance(record_class, basestring):
                return False
            tag_string = "tag_sex_record_" + record_class
            self.event_triggers_dict[tag_string] = self.sex_record.get(record_class, 0)
            return True

        def comp_sex_record(self, record_class = None):   #Compare the current sex record with a previous tagged value.
            if not isinstance(record_class, basestring):
                return -1
            tag_string = "tag_sex_record_" + record_class
            return (self.sex_record.get(record_class, 0) - self.event_triggers_dict.get(tag_string, 0))

        @property
        def cum_exposure_count(self):
            total = 0
            total += self.sex_record.get("Vaginal Creampies", 0)
            total += self.sex_record.get("Anal Creampies", 0)
            total += self.sex_record.get("Cum Facials", 0)
            total += self.sex_record.get("Cum in Mouth", 0)
            total += self.sex_record.get("Cum Covered", 0)
            return total

##########################################
# event functions                        #
##########################################

        def set_event_day(self, dict_key, override = True, set_day = None):
            if dict_key in self.event_triggers_dict and not override:
                return False
            self.event_triggers_dict[dict_key] = day if set_day is None else set_day
            return True

        def get_event_day(self, dict_key, set_if_none = True):
            if not dict_key in self.event_triggers_dict and set_if_none:
                self.set_event_day(dict_key)

            return self.event_triggers_dict.get(dict_key, 0)

        def days_since_event(self, dict_key, set_if_none = False):
            if not dict_key in self.event_triggers_dict and set_if_none:
                self.set_event_day(dict_key)

            return day - self.event_triggers_dict.get(dict_key, day)

        def story_event_ready(self, dict_key):
            if self.days_since_event("story_event") < TIER_1_TIME_DELAY:        #In general, we want to keep tier 1 between all events with a certain person
                return False
            if self.days_since_event(dict_key + "_event") >= TIER_2_TIME_DELAY:           #Events of the same type should be spaced out a little further
                return self.is_available
            return False

        def story_event_log(self, dict_key):
            self.set_event_day(dict_key + "_event")
            self.set_event_day("story_event")
            return

        def string_since_event(self, dict_key): #Returns a string describing how long it has been since an event
            since = self.days_since_event(dict_key)

            if since < 1:
                return "earlier"
            elif since == 1:
                return "yesterday"
            elif since <= 4:
                return "a few days ago"
            elif since <= 10:
                return "a week ago"
            elif since <= 19:
                return "a couple weeks ago"
            elif since <= 28:
                return "a few weeks ago"
            elif since <= 45:
                return "a month ago"
            elif since <= 75:
                return "a couple months ago"
            elif since <= 145:
                return "a few months ago"
            return "quite some time ago"



##########################################
# Unique crisis addition functions       #
##########################################
        # Use these extensions to add only unique crisis. Checks to see if the event has already been added, so it won't duplicate.
        def add_unique_on_talk_event(self, the_crisis):
            if the_crisis not in self.on_talk_event_list:
                self.on_talk_event_list.append(the_crisis)

        def add_unique_on_room_enter_event(self, the_crisis):
            if the_crisis not in self.on_room_enter_event_list:
                self.on_room_enter_event_list.append(the_crisis)

        def remove_on_talk_event(self, the_crisis):
            if isinstance(the_crisis, basestring):
                found = next((x for x in self.on_talk_event_list if x.effect == the_crisis or x.name == the_crisis), None)
                if found:
                    self.on_talk_event_list.remove(found)

            if the_crisis in self.on_talk_event_list:
                self.on_talk_event_list.remove(the_crisis)

        def remove_on_room_enter_event(self, the_crisis):
            if isinstance(the_crisis, basestring):
                found = next((x for x in self.on_room_enter_event_list if x.effect == the_crisis or x.name == the_crisis), None)
                if found:
                    self.on_room_enter_event_list.remove(found)

            if the_crisis in self.on_room_enter_event_list:
                self.on_room_enter_event_list.remove(the_crisis)


###################################
# Person object caching functions #
###################################

        # cache the last 512 generated displayables
        global character_cache
        character_cache = LRUCacheDict(512, expiration = 0)

        def clean_cache(self):
            partial = "ID:{}".format(self.identifier)
            obsolete = [x for x in character_cache.keys() if partial in x]
            for x in obsolete:
                del character_cache[x]

        global portrait_cache
        portrait_cache = LRUCacheDict(100, expiration = 0)

        def person_portrait(self, special_modifier = None):
            position = "stand5"
            emotion = "happy"
            special_modifier = None
            lighting = [.98,.98,.98]

            disp_key = "P:{}_F:{}_H:{}_HC:{}_EC:{}".format(self.identifier,
                self.face_style, self.hair_style.name,
                hash(tuple(x for x in map(hash, self.hair_style.colour))),
                hash(tuple(x for x in map(hash, self.eyes[1]))))

            if disp_key in portrait_cache:
                return portrait_cache[disp_key]

            displayable_list = []
            displayable_list.append(self.expression_images.generate_emotion_displayable(position,emotion, special_modifier = special_modifier, eye_colour = self.eyes[1], lighting = lighting)) #Get the face displayable
            displayable_list.append(self.hair_style.generate_item_displayable("standard_body",self.tits,position, lighting = lighting)) #Get hair

            x_size, y_size = position_size_dict.get(position)
            composite_list = [(x_size,y_size)]

            for display in displayable_list:
                if isinstance(display, __builtin__.tuple):
                    composite_list.extend(display)
                else:
                    composite_list.append((0,0))
                    composite_list.append(display)

            portrait_cache[disp_key] = AlphaMask(Flatten(Composite(*composite_list)), portrait_mask_image)
            return portrait_cache[disp_key]
