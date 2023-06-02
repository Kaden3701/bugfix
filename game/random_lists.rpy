init -2:
    python:

        def VrenNullAction(): #For some reason the NullAction still returns None, so it still transitions screens.
            pass

        def get_random_from_weighted_list(list, return_everything = False): #Passed a list of parameters which are ["Thing", weighted value, anything_else,...]
            #If return_everything is True, returns the entire tuple instead of just an action
            if len(list) == 0:
                return None

            total_value = 0
            for item in list:
                total_value += item[1] #Get the total weighting value that we use to determine what thing we've picked.

            random_value = renpy.random.randint(0,total_value) #Gets us a value somewhere inside of our probability space.
            running_total = 0
            for item in list:
                if random_value <= (item[1]+running_total):
                    if return_everything:
                        return item
                    else:
                        return item[0]
                else:
                    running_total += item[1]

        def is_in_weighted_list(test_item,list):
            for item in list:
                if test_item == item[0]:
                    return True
            return False

        def index_in_weighted_list(test_item,list):
            for item in list:
                if test_item == item[0]:
                    return list.index(item)
            raise ValueError("{!r} is not in weighted list".format(test_item))


        def get_random_job(): #TODO: Replace this with a more directed function that distributes jobs based on stats.
            return get_random_from_weighted_list([x for x in list_of_jobs if x[1] > 2])


        technobabble_list = []
        technobabble_list.append("optimize the electromagnetic pathways")
        technobabble_list.append("correct for the nanowave signature")
        technobabble_list.append("de-scramble the thermal injector")
        technobabble_list.append("crosslink the long chain polycarbons")
        technobabble_list.append("carbonate the ethyl groups")
        technobabble_list.append("oxidize the functional group")
        technobabble_list.append("resynchronize the autosequencers")
        technobabble_list.append("invert the final power spike")
        technobabble_list.append("kickstart the process a half second early")
        technobabble_list.append("stall the process by a half second")
        technobabble_list.append("apply a small machine learning algorithm")
        technobabble_list.append("hit the thing in just the right spot")
        technobabble_list.append("wait patiently for it to finish")

        font_list = []
        font_list.append("fonts/Avara.ttf")
        font_list.append("fonts/GlacialIndifference-Regular.otf")
        font_list.append("fonts/FantasqueSansMono-Regular.ttf")
        font_list.append("fonts/TruenoRg.otf")
        font_list.append("fonts/TruenoBd.otf")
        font_list.append("fonts/Crimson-Roman.ttf")
        font_list.append("fonts/Crimson-Bold.ttf")
        font_list.append("fonts/HKVenetian-Regular.otf")
        font_list.append("fonts/HKVenetian-Italic.otf")
        font_list.append("fonts/AAntiCorona-L3Ax3.ttf")

        def get_random_font():
            return gui.default_font
            # use one generic font
            #return get_random_from_list(font_list)

        #https://snook.ca/technical/colour_contrast/colour.html A good site to generate colour contrast examples to make sure thigns are readable. Our text background is roughly #3459d2
        readable_color_list = [] #Colors that are easily readable on our blue background.
        readable_color_list.append("#ffffff") #White
        readable_color_list.append("#dddddd") #Grey
        readable_color_list.append("#ffff6e") #Yellow
        readable_color_list.append("#8fff66") #Green
        readable_color_list.append("#cf6347") #Tomato Red
        readable_color_list.append("#ffd4d4") #Pink
        readable_color_list.append("#FFB1F8") #Hotpink
        readable_color_list.append("#73ffdf") #Teal
        readable_color_list.append("#dda0dd") #Plum
        readable_color_list.append("#87cefa") #Light Blue (Replaces pure blue)
        readable_color_list.append("#fcf7de") # Corn Silk
        readable_color_list.append("#f0defd") # Lavender
        readable_color_list.append("#f2d7b4") # Wheat
        readable_color_list.append("#DAA520") # Golden Rod
        readable_color_list.append("#FFA07A") # Light Salmon
        readable_color_list.append("#FFA500") # Orange
        readable_color_list.append("#D2691E") # Chocolate
        readable_color_list.append("#20B2AA") # Light Sea Green
        readable_color_list.append("#C0C0C0") # Silver


        def get_random_readable_color():
            return get_random_from_list(readable_color_list)

        def format_group_of_people(list_of_people): # Returns a string made up of people titles like "PersonA, PersonB, and PersonC." or just "PersonA and PersonB" if there are two people. (or PersonA if it's just one person)
            #Note: the list is formatted in the order it is handed over. renpy.random.scramble() it beforehand if you want it in a random order.
            return_string = ""
            if len(list_of_people) == 1:
                return_string += list_of_people[0].title
            elif len(list_of_people) == 2:
                return_string += list_of_people[0].title + " and " + list_of_people[1].title
            else:
                for a_person in list_of_people:
                    if a_person is not list_of_people[-1]: #If they're not the last person:
                        return_string += a_person.title + ", "
                    else:
                        return_string += "and " + a_person.title

            #TODO: Add a variant of this that lets you set a max number of people. A kind of "blah, blah, blah, and 7 more people..." response.
            return return_string

        def format_list_of_clothing(the_list): # Takes a list of strings and formats them to the form "ThingA, thingB, and ThingC"
            return_string = ""
            if len(the_list) == 1:
                return_string = the_list[0].display_name
            elif len(the_list) ==2:
                return_string = the_list[0].display_name + " and " + the_list[1].display_name
            else:
                for item in the_list:
                    if item is the_list[-1]:
                        return_string += "and " + item.display_name
                    else:
                        return_string += item.display_name + ", "
            return return_string
