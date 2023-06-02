init -10 python:
    def init_list_of_hairs():
        hair_list = []
        hair_list.append(["blond", [0.89,0.75,0.47,1]])
        hair_list.append(["brown", [0.21,0.105,0.06,1]])
        hair_list.append(["black",[0.09,0.07,0.09,1]])
        hair_list.append(["chestnut", [0.59,0.31,0.18,1]])
        hair_list.append(["hot pink", [1,0.5,0.8,1]])
        hair_list.append(["sky blue", [0.4,0.5,0.9,1]])
        hair_list.append(["alt blond", [0.882, 0.733, 0.580,1]])
        hair_list.append(["light grey", [0.866, 0.835, 0.862,1]])
        hair_list.append(["ash brown", [0.590, 0.473, 0.379,1]])
        hair_list.append(["knight red", [0.745, 0.117, 0.235,1]])
        hair_list.append(["platinum blonde", [0.789, 0.746, 0.691,1]])
        hair_list.append(["golden blonde", [0.895, 0.781, 0.656,1]])
        hair_list.append(["turquoise" , [0.435, 0.807, 0.788,1]])
        hair_list.append(["lime green" , [0.647, 0.854, 0.564,1]])
        hair_list.append(["strawberry blonde", [0.644, 0.418, 0.273,1]])
        hair_list.append(["light auburn", [0.566, 0.332, 0.238,1]])
        hair_list.append(["pulp", [0.643, 0.439, 0.541,1]])
        hair_list.append(["saturated" , [0.905, 0.898, 0.513,1]])
        hair_list.append(["emerald" , [0.098, 0.721, 0.541,1]])
        hair_list.append(["light brown", [0.652, 0.520, 0.414,1]])
        hair_list.append(["bleached blonde", [0.859, 0.812, 0.733,1]])
        hair_list.append(["chestnut brown", [0.414, 0.305, 0.258,1]])
        hair_list.append(["barn red", [0.484, 0.039, 0.008,1]])
        hair_list.append(["dark auburn", [0.367, 0.031, 0.031,1]])
        hair_list.append(["toasted wheat", [0.848, 0.75, 0.469,1]])
        #TODO: Add more hair colours
        return hair_list

    def init_list_of_faces():
        faces = []
        faces.append("Face_1")
        faces.append("Face_2")
        faces.append("Face_3")
        faces.append("Face_4")
        faces.append("Face_5")

        faces.append("Face_6")
        faces.append("Face_7")
        faces.append("Face_8")
        faces.append("Face_9") #Used to be Mobile Exclusion
        #faces.append("Face_10") #Bad render
        faces.append("Face_11") #Used to be Mobile Exclusion
        faces.append("Face_12") #Used to be Mobile Exclusion
        faces.append("Face_13") #Used to be Mobile Exclusion
        faces.append("Face_14") #Used to be Mobile Exclusion
        return faces

    def init_list_of_eyes():
        eyes = []
        eyes.append(["dark blue",[0.32, 0.60, 0.82, 1.0]])
        eyes.append(["light blue",[0.60, 0.75, 0.98, 1.0]])
        eyes.append(["green",[0.35, 0.68, 0.40, 1.0]])
        eyes.append(["brown",[.62, .42, .29, 1.0]])
        eyes.append(["grey",[0.86, 0.90, 0.90, 1.0]])
        eyes.append(["emerald", [0.305, 0.643, 0.607, 1.0]])
        eyes.append(["steel blue", [0.2745, 0.5098, 0.7059, 1.0]])
        eyes.append(["dark brown", [0.4039, 0.2667, 0.2314, 1.0]])
        return eyes
