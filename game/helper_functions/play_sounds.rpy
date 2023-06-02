init -2:
    default sound_folder = "sounds"

init 10 python:
    def play_moan_sound():
        rnd_num = renpy.random.randint(0, 14)
        filename = "{}/Moan{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")

    def play_female_orgasm():
        rnd_num = renpy.random.randint(0, 2)
        filename = "{}/Orgasm{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")

    def play_spank_sound():
        rnd_num = renpy.random.randint(0, 3)
        filename = "{}/Slap{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")

    def play_breathing_sound():
        rnd_num = renpy.random.randint(0, 1)
        filename = "{}/Breathing{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")

    def play_gag_sound():
        rnd_num = renpy.random.randint(0, 5)
        filename = "{}/Gag{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")

    def play_swallow_sound():
        rnd_num = renpy.random.randint(0, 5)
        filename = "{}/Swallow{}.wav".format(sound_folder, rnd_num)
        renpy.play(filename, "sex")
