init -100 python:
    global is64Bit
    is64Bit = sys.maxsize > 2**32

    @renpy.pure
    def parse_version_string(version):
        parts = version.split(".")
        return int(parts[0].strip("v")), int(parts[1]), int(parts[2])

    @renpy.pure
    def get_loaded_version():
        if "game_version" in globals():
            loaded_version = game_version
        else:
            loaded_version = "v0.33.3"
        return loaded_version

init -2:
    default persistent.zip_cache_size = 0 # default is small size
    default persistent.show_ntr = False     # default turn of NTR
    default persistent.keep_patreon_characters = True  # keep VREN original characters from hire process
    default persistent.mc_noncon_pref = 0   #Default to disabled. MC does not allow himself to be raped in any situation.

init python: # place first on the hijack stack
    add_label_hijack("after_load", "check_save_version")

init 5 python: # add to stack later then other mods
    add_label_hijack("normal_start", "activate_compatibility_fix")
    add_label_hijack("after_load", "update_compatibility_fix")
    add_label_hijack("start", "check_mod_installation")

init 100 python:
    add_label_hijack("normal_start", "store_game_version")

init -5 python:
    # override some of the default settings to improve performance
    config.image_cache_size = None  # when None the image_cache_size_mb value is used
    if is64Bit:
        config.image_cache_size_mb = 768 # fixed at 768 Mb * 4 bytes per pixel
    else:
        config.image_cache_size_mb = 384 # fixed at 384 Mb * 4 bytes per pixel

    # heart pasties and cincher (move to level 0)
    heart_pasties.layer = 0
    cincher.layer = 0

    # pencil skirt pussy usable to False
    pencil_skirt.anchor_below = True

    # change clothing layers (make layer 2 in between (available in under and overwear))
    for x in pants_list + skirts_list + [x for x in dress_list if x not in [lacy_one_piece_underwear, lingerie_one_piece, bodysuit_underwear]] + shirts_list:
        x.layer += 1
        if x.has_extension:
            x.has_extension.layer += 1

    # special case, it's part upper (layer 3) and part underwear (layer 1)
    leotard_bottom.layer = 1

    # special case, nightgown dress upper (layer 1) and bottom (layer 3 - like skirt)
    nightgown_dress.layer = 1

    # move makeup to layer 2 (in between layer)
    for x in [light_eye_shadow, heavy_eye_shadow, blush, lipstick]:
        x.layer += 1

    # disable gl2 extensions
    if renpy.android or renpy.mobile:
        config.gl2 = False
        persistent.vren_animation = False

    # allow for more idle objects
    config.automatic_images = None
    config.optimize_texture_bounds = True
    config.predict_statements = 64 if is64Bit else 32
    config.rollback_length = 64 if is64Bit else 32      # since refactor we can allow a longer rollback history
    config.cache_surfaces = False
    config.predict_screen_statements = False
    config.predict_screens = False
    config.list_compression_length = 200        # increase list compression length for rollback

    # disable auto save
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.autosave_on_input = False
    config.autosave_frequency = None
    config.has_autosave = True
    config.has_quicksave = True
    config.autosave_slots = 6
    # config.autosave_frequency = 200 # default: 200

    # for DEBUG only (uncomment when you get a cPickle error)
    # config.use_cpickle = False
    # config.debug_image_cache = True

    # disable sound settings
    config.has_sound = True
    config.has_music = False
    config.has_voice = False

    def update_pinned_cache():
        # cache all GUI images in memory
        for fn in [x for x in renpy.list_files() if x.endswith(".png")]:
            if re.search(r"(?:gui\/|map\/)", fn, re.IGNORECASE):
                renpy.cache_pin(fn)
        return

    # remove full outfits / overwear from default wardrobe that have no shoes or no layer 2 clothing items (nude outfits)
    # to prevent messed up outfits to be used by girls in daily life
    def cleanup_default_wardrobe():
        remove = []
        for outfit in default_wardrobe.outfit_sets + default_wardrobe.overwear_sets:
            if not any(x for x in outfit.feet if x.layer == 2):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 3 or x.layer == 4):
                remove.append(outfit)
            elif not any(x for x in outfit.upper_body if x.layer == 3 and x.has_extension) and \
                not any(x for x in outfit.lower_body if x.layer == 3):
                remove.append(outfit)

        if len(remove) > 10:
            write_log("WARNING: Something is wrong with the clothing layers, too many outfits ({}) are being removed.".format(len(remove)))
        # print("Removing {} outfits from default wardrobe.".format(len(remove)))
        for outfit in remove:
            # print("Removing: " + outfit.name)
            default_wardrobe.remove_outfit(outfit)
        return

label check_mod_installation(stack):
    $ execute_hijack_call(stack)
    return

label activate_compatibility_fix(stack):
    # make sure we store the crisis tracker in the save game
    $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ cleanup_default_wardrobe()

    $ execute_hijack_call(stack)
    return

label update_compatibility_fix(stack):
    if not "crisis_tracker_dict" in globals():
        $ crisis_tracker_dict = {}

    $ update_pinned_cache()

    $ cleanup_default_wardrobe()

    $ execute_hijack_call(stack)
    return

label store_game_version(stack):
    $ game_version = config.version
    $ execute_hijack_call(stack)
    return

label check_save_version(stack):
    $ loaded_version = get_loaded_version()

    if not "game_version" in globals():
        "Warning" "You are loading a save game from an un-modded game. This is not supported, start a new modded game."
        $ renpy.full_restart()
        return
    elif parse_version_string(loaded_version)[1] < parse_version_string(config.version)[1]:
        "Warning" "You are loading an incompatible game version ([loaded_version]). Please start a new game."
        $ renpy.full_restart()
        return
    elif parse_version_string(loaded_version)[2] < parse_version_string(config.version)[2]:
        "Warning" "You are loading a game created by a previous build ([loaded_version]), you might run into errors because of this. Before reporting errors, please start a new modded game and see if the problem persists."
    $ execute_hijack_call(stack)
    return
