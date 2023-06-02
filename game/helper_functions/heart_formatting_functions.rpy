init -1 python:
    def build_hearts():
        # this function will create the actual hart images
        # for a total of 460 heart images in various configurations
        # based on gold_heart, red_heart, grey_heart and empty_heart
        for color in ["gold", "red", "grey"]:
            for i in range(0, 20):
                name = "{}_heart{}".format(color, i)
                heart_progress = HeartImage(name, "empty_heart.png", "{}_heart.png".format(color), i)
                renpy.image(name, heart_progress)

        for i in range(0, 20):
            for j in range(0, 21-i):
                name = "gold_heart{}_red_heart{}".format(i, j)
                heart_progress = HeartImage(name, "empty_heart.png", "gold_heart.png", i, "red_heart.png", j)
                renpy.image(name, heart_progress)

                name = "gold_heart{}_grey_heart{}".format(i, j)
                heart_progress = HeartImage(name, "empty_heart.png", "gold_heart.png", i, "grey_heart.png", j)
                renpy.image(name, heart_progress)
        return

    build_hearts()


    # override default function to limit call stack depth
    @renpy.pure
    def get_red_heart(sluttiness, depth = 0):
        return get_hearts(sluttiness, depth)

    # override default function to limit call stack depth
    @renpy.pure
    def get_gold_heart(sluttiness, depth = 0):
        return get_hearts(sluttiness, depth, color = "gold")

    @renpy.pure
    def get_hearts(sluttiness, depth = 0, color = "red"): #A recursive function, feet it a sluttiness and it will return a string of all red heart images for it. Heatrts taht are entirely empty are left out.
        sluttiness = __builtin__.int(sluttiness)
        if depth >= 5:
            return ""

        the_final_string = ""
        if sluttiness >= 20:
            the_final_string += "{{image=gui/heart/{}_heart.png}}".format(color)
            the_final_string += get_hearts(sluttiness - 20, depth + 1, color) #Call it recursively if we might have another heart after this.
        elif sluttiness > 0:
            the_final_string += "{{image={}_heart{}}}".format(color, sluttiness)

        return the_final_string

    @renpy.pure
    def get_love_hearts(value, max_hearts = 5):
        the_final_string = ""
        count = 0
        while count < max_hearts:
            if value >= 20:
                the_final_string += get_hearts(20)
                value -= 20
            elif value > 0:
                the_final_string += get_hearts(value)
                value -= value
            elif value <= -20:
                the_final_string += get_hearts(20, color="grey")
                value += 20
            elif value < 0:
                the_final_string += get_hearts(-value, color="grey")
                value -= value
            else:
                the_final_string += "{image=gui/heart/empty_heart.png}"
            count += 1
        return the_final_string

    @renpy.pure
    def get_heart_image_list(sluttiness, effective_sluttiness):
        heart_string = ""

        if sluttiness > effective_sluttiness:
            full_hearts = effective_sluttiness // 20
            gold_value = effective_sluttiness % 20
            heart_string += get_gold_heart(full_hearts * 20)
            grey_value = sluttiness - effective_sluttiness
            if full_hearts < 5:
                if gold_value == 0 and grey_value > 0:
                    heart_string += get_hearts(grey_value, full_hearts, color="grey")
                    full_hearts = heart_string.count("image=")
                elif gold_value > 0 and grey_value == 0:
                    heart_string += get_hearts(gold_value, full_hearts, color="gold")
                    full_hearts = heart_string.count("image=")
                elif gold_value + grey_value > 20:
                    used_grey = 20 - gold_value
                    heart_string += "{{image=gold_heart{}_grey_heart{}}}".format(gold_value, used_grey)
                    full_hearts += 1
                    if full_hearts < 5:
                        heart_string += get_hearts(grey_value - used_grey, full_hearts, color = "grey")
                        full_hearts = heart_string.count("image=")
                else:
                    heart_string += "{{image=gold_heart{}_grey_heart{}}}".format(gold_value, grey_value)
                    full_hearts += 1
        else:
            full_hearts = sluttiness // 20
            gold_value = sluttiness % 20
            heart_string += get_gold_heart(full_hearts * 20)
            red_value = effective_sluttiness - sluttiness
            if full_hearts < 5:
                if gold_value == 0 and red_value > 0:
                    heart_string += get_hearts(red_value, full_hearts, color="red")
                    full_hearts = heart_string.count("image=")
                elif gold_value > 0 and red_value == 0:
                    heart_string += get_hearts(gold_value, full_hearts, color="gold")
                    full_hearts = heart_string.count("image=")
                elif gold_value + red_value > 20:
                    used_red = 20 - gold_value
                    heart_string += "{{image=gold_heart{}_red_heart{}}}".format(gold_value, used_red)
                    full_hearts += 1
                    if full_hearts < 5:
                        heart_string += get_hearts(red_value - used_red, full_hearts, color="red")
                        full_hearts = heart_string.count("image=")
                else:
                    heart_string += "{{image=gold_heart{}_red_heart{}}}".format(gold_value, red_value)
                    full_hearts += 1

        while full_hearts < 5:
            heart_string += "{{image={}}}".format(get_file_handle("heart/empty_heart.png"))
            full_hearts += 1

        return heart_string
