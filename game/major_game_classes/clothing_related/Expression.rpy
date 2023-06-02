init -2 python:
    class Expression():
        emotion_set = ["default","happy","sad","angry","orgasm"]
        ignore_position_set = ["doggy","walking_away","standing_doggy"] #The set of positions that we are not goign to draw emotions for. These look away from the camera TODO: This should reference the Position class somehow.

        def __init__(self,name,skin_colour,facial_style, colour = None):
            self.name = name
            self.skin_colour = skin_colour
            self.facial_style = facial_style #The style of face the person has, currently creatively named "Face_1", "Face_2", "Face_3", etc..
            self.special_modifiers = {"kissing":["kissing"]} #Special modifiers that are sometimes applied to expressions, but not always. ie. for blowjobs that may be either in normal crouching mode or blowjob mode.
            self.position_dict = {}
            for position in [x for x in supported_positions if x not in self.ignore_position_set]: #All positions support the blowjob special modifier now.
                if position in self.special_modifiers.keys():
                    self.special_modifiers[position].extend(["blowjob"])
                else:
                    self.special_modifiers[position] = ["blowjob"]

            for position in supported_positions:
                self.position_dict[position] = {}
                if position in self.ignore_position_set:
                    for emotion in self.emotion_set:
                        self.position_dict[position][emotion] = "default" + "_" + facial_style + "_" + position + "_" + skin_colour + ".png" ##An empty image to be drawn when we don't want to draw any emotion, because the character's face is turned away.
                else:
                    for emotion in self.emotion_set:
                        self.position_dict[position][emotion] = emotion + "_" + facial_style + "_" + position + "_" + skin_colour + ".png"

            for position, modifiers in self.special_modifiers.iteritems(): #Position is the key of our special modifers dict, get all the positions with a special modifier assigned.
                for modifier in modifiers: #If that position has multiple special modifers we want to add them all.
                    for emotion in self.emotion_set:
                        modified_emotion = emotion + "_" + modifier
                        self.position_dict[position][modified_emotion] = modified_emotion + "_" + facial_style + "_" + position + "_" + skin_colour + ".png"#Add a new emotion titled "<emotion>_<modifier>", for example "sad_blowjob".

            if not colour:
                self.colour = [1,1,1,1]
            else:
                self.colour = colour

        def generate_emotion_displayable(self,position,emotion, special_modifier = None, eye_colour = None, lighting = None):
            if not emotion in self.emotion_set:
                emotion = "default" #Get our default emotion to show if we get an incorrect one.
            elif special_modifier and special_modifier in self.special_modifiers:
                emotion = emotion + "_" + special_modifier

            if lighting is None:
                lighting = [1,1,1]

            if eye_colour is None:
                eye_colour = [.62, .42, .29, 1.0] #brown by default.

            if not emotion in self.position_dict[position]:
                return empty_image

            #renpy.notify("Lighting: {r}, {g}, {b}\nEye Color: {r1}, {g1}, {b1}".format(r=lighting[0], g=lighting[1], b=lighting[2], r1=eye_colour[0], g1=eye_colour[1], b1=eye_colour[2]))

            base_image = ZipContainer(position, self.position_dict[position][emotion])
            mask_image = ZipContainer(position, self.position_dict[position][emotion].replace("_" + self.skin_colour,"_Pattern_1"))

            # correctly lighted
            base_image = im.MatrixColor(base_image, im.matrix.tint(*lighting))

            # grey-scaled with slight brightness boost
            gray_scaled_image = im.MatrixColor(base_image, im.matrix.saturation(0) * im.matrix.brightness(.2))
            # colorized with eye colour
            colorized_image = im.MatrixColor(gray_scaled_image, im.matrix.tint(eye_colour[0], eye_colour[1], eye_colour[2]) * im.matrix.tint(*lighting))
            # only use eyes from colorized gray scale
            shader_image = AlphaMask(colorized_image, mask_image)

            # blend shader pattern into base image (mask location only)
            return Composite((0,0), (0,0), base_image, (0,0), shader_image)

        def generate_raw_image(self, position, emotion, special_modifier = None): #Returns the raw ZipFileImage or Image, instead of the displayable (used for generating region masks)
            if not emotion in self.emotion_set:
                emotion = "default" #Get our default emotion to show if we get an incorrect one.
            elif special_modifier and special_modifier in self.special_modifiers:
                emotion = emotion + "_" + special_modifier

            if not emotion in self.position_dict[position]:
                return empty_image

            return ZipContainer(position, self.position_dict[position][emotion])
