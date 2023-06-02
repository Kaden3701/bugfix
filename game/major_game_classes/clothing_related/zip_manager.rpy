############################################################
# MOD Implementation of ZIP file loading and image caching #
############################################################

init 2:
    default persistent.zip_cache_preload = True

init 5 python:
    # special class for managing thread locks and cache objects for zipfile loading
    class ZipManager():
        def __init__(self):
            self.Locks = {}
            self.Cache = {}
            self.load_delay = .05
            if is64Bit:
                self.max_items = 1200 if persistent.zip_cache_size == 0 else 2500
            else:
                self.max_items = 300 if persistent.zip_cache_size == 0 else 500

            for x in supported_positions + ["character_images"]:
                self.Locks[x] = threading.RLock()
                self.Cache[x] = LRUCacheDict(max_size = self.max_items, expiration = 0)    # most used character images per position

        def preload(self):  # load main character images into the zip file cache
            time.sleep(5)
            self.load_masking_areas()
            self.load_emotions()
            self.load_hair_styles()
            self.load_main_character_images()

        def load_main_character_images(self):
            for cloth in [white_skin, black_skin, tan_skin]:
                for position in supported_positions:
                    for body in ["standard_body","thin_body","curvy_body"] if cloth.body_dependant else ["standard_body"]:
                        for tits in Clothing_Images.breast_sizes if cloth.draws_breasts else ["AA"]:
                            file = cloth.position_sets[position].get_image(body, tits)
                            if file:
                                file.load()
                                time.sleep(self.load_delay)

        def load_hair_styles(self):
            for cloth in hair_styles:
                for position in supported_positions:
                    for body in ["standard_body","thin_body","curvy_body"] if cloth.body_dependant else ["standard_body"]:
                        for tits in Clothing_Images.breast_sizes if cloth.draws_breasts else ["AA"]:
                            file = cloth.position_sets[position].get_image(body, tits)
                            if file:
                                file.load()
                                time.sleep(self.load_delay)

        def load_masking_areas(self):
            for cloth in [breast_region, butt_region, all_regions, torso_region, stomach_region, pelvis_region, upper_arm_region, upper_leg_region, lower_arm_region, lower_leg_region, foot_region, hand_region, skirt_region, wet_nipple_region, vagina_region]:
                for position in supported_positions:
                    for body in ["standard_body","thin_body","curvy_body"] if cloth.body_dependant else ["standard_body"]:
                        for tits in Clothing_Images.breast_sizes if cloth.draws_breasts else ["AA"]:
                            file = cloth.position_sets[position].get_image(body, tits)
                            if file:
                                file.load()
                                time.sleep(self.load_delay)

        def load_emotions(self):
            for skin in ["white", "tan", "black"]:
                for face in Person._list_of_faces:
                    exp = emotion_images_dict[skin][face]
                    for position in supported_positions:
                        for emotion in Expression.emotion_set:
                            file = exp.generate_raw_image(position, emotion)
                            if file:
                                file.load()
                                time.sleep(self.load_delay)

        def size(self):
            return sum(x.size() for x in self.Cache.values())

        def byte_size(self):
            return sum(x.byte_size() for x in self.Cache.values())

        def utilization(self):
            # result = {}
            # for k, v in self.Cache.iteritems():
            #     result[k] = []
            #     result[k].append(v.size())
            #     result[k].append(v.size() * 100.0 / float(self.max_items))
            # return result
            return (self.size() * 100.0 / (self.max_items * float(len(self.Cache))))

    class ZipContainer(renpy.display.im.ImageBase): #TODO: Move this to a more obvious file. Probably something to do along with a bunch of other refactoring.
        def __init__(self, position, filename, mtime=0, **properties):
            super(ZipContainer, self).__init__(position, filename, mtime, **properties)
            self.position = position
            self.filename = filename

        def load(self):
            try:
                with zip_manager.Locks[self.position]:
                    if not self.filename in zip_manager.Cache[self.position]:
                        global mobile_zip_dict
                        zip_manager.Cache[self.position][self.filename] = mobile_zip_dict[self.position].read(self.filename)

                    sio = io.BytesIO(zip_manager.Cache[self.position][self.filename])
                    return renpy.display.pgrender.load_image(sio, self.filename)
            except:
                return renpy.display.pgrender.surface((2, 2), True)    # same object als the Renpy image zip returns https://github.com/renpy/renpy/blob/master/renpy/display/im.py

    zip_manager = ZipManager()

    if persistent.zip_cache_preload:
        # start background thread for pre-loading zip cache
        background_thread = threading.Thread(target=zip_manager.preload)
        background_thread.daemon = True
        background_thread.start()
