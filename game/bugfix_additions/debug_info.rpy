init -50 python:
    import threading
    from lru import LRUCacheDict
    import time

    class SystemInfo():
        def __init__(self):
            self.total_zip_size = 0
            self.total_zip_items = 0
            self.zip_utilization = 0
            self.texture_size = 0
            self.texture_count = 0
            self.cache_size = 0

        def update(self):
            if "zip_manager" in globals():
                global zip_manager
                self.total_zip_size = zip_manager.byte_size()
                self.total_zip_items = zip_manager.size()
                self.zip_utilization = zip_manager.utilization()
            self.texture_size, self.texture_count = renpy.exports.get_texture_size()
            self.cache_size = renpy.display.im.cache.get_total_size()


    system_info = SystemInfo()

    render_lock =  threading.RLock()

    # make sure we only call this on the main thread
    def validate_texture_memory():
        # keep texture memory at configured image_cache_size_in_mb; game slows down when this gets too high
        # check for 90% of available memory cache slows down dramatically when under pressure
        if renpy.display.draw.get_texture_size()[0] > (renpy.display.im.cache.cache_limit * 4 * .9):
            clean_memory()   # use main free memory function
        return

    def update_texture_info():
        while not hasattr(renpy.display.draw, "get_texture_size"):
            time.sleep(2)

        while 1:
            if debug_log_enabled:
                system_info.update()
            time.sleep(.5)
        return

    debug_log = LRUCacheDict(8, expiration = 0)

    # Background thread for updating debug info log information
    texture_info_thread = threading.Thread(target=update_texture_info, name="texture_monitor")
    texture_info_thread.daemon = True
    texture_info_thread.start()

    renpy.config.per_frame_screens.append("DebugInfo")

    def show_debug_log():
        global debug_log_enabled
        debug_log_enabled = True
        renpy.show_screen("DebugInfo")

    def hide_debug_log():
        global debug_log_enabled
        debug_log_enabled = False
        renpy.hide_screen("DebugInfo")

    # write to log.txt in root folder
    def write_log(s, *args):
        if debug_log_enabled:
            renpy.write_log(s, *args)
        print(s)
        return

    # add info to in-game debug window
    def add_to_debug_log(message, start_time = time.time()):
        if debug_log_enabled:
            debug_log["T" + str(time.time())] = message.format(total_time = time.time() - start_time)
        write_log(message.format(total_time = time.time() - start_time))

    def get_debug_log():
        return "\n".join(OrderedDict(sorted(debug_log._LRUCacheDict__values.items(), key=lambda t: t[0], reverse = True)).values())

    def get_persons_size():
        return sum(get_size(x) for x in list_of_people)

    def get_size(obj, seen=None):
        size = sys.getsizeof(obj)
        if not seen:
            seen = set()
        if id(obj) in seen:
            return 0
        # Important mark as seen *before* entering recursion to gracefully handle
        # self-referential objects
        seen.add(id(obj))
        try:
            if isinstance(obj, collections.Mapping):
                size += sum(get_size(v, seen) for v in obj.values())
                size += sum(get_size(k, seen) for k in obj.keys())
            elif hasattr(obj, '__dict__'):  # sum all object attributes
                size += sum(get_size(getattr(obj, name), seen) for name in obj.__dict__.keys())
            elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
                size += sum(get_size(i, seen) for i in obj)
            elif isinstance(obj, (str, bytes, bytearray)):
                size += len(obj)
            else: # check if passed object has a nested object property
                for attr in [x for x in dir(obj) if isinstance(x, (list, dict, tuple, object))]:
                    size += get_size(getattr(obj, attr), seen)
        except:
            pass
        return size

init 2:
    define debug_log_enabled = False

    style debug_label_text:
        size 14
        italic False
        bold False
        color "#ffffff"
        outlines [(2,"#222222",0,0)]

    screen DebugInfo():
        style_prefix "debug"
        zorder 100

        drag:
            drag_name "DebugInfo"
            xalign .9
            yalign 0
            drag_handle(0.0,0.0, 1.0,1.0)
            frame:
                background "#00000055"
                xmaximum 600
                padding (5,5)
                has vbox
                label "ZipCache memory: {total_size:.2f} MB".format(total_size = system_info.total_zip_size / 1024.0 / 1024.0) xminimum 400
                label "ZipCache items: {count} ({utilization:.1f}%)".format(count = system_info.total_zip_items, utilization = system_info.zip_utilization)
                label "Texture Memory: {total_size:.2f} MB ({num_of_items})".format(total_size = system_info.texture_size / 1024.0 / 1024.0, num_of_items = system_info.texture_count)
                label "Image Cache: {size:.1f} / {max_size:.1f} MB ({utilization:.1f}%)".format(size = 4.0 * system_info.cache_size / 1024.0 / 1024.0, max_size = 4.0 * renpy.display.im.cache.cache_limit / 1024.0 / 1024.0, utilization = system_info.cache_size * 100.0 / renpy.display.im.cache.cache_limit)
                label ""
                label get_debug_log()


    # renpy.profile_screen("main_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("business_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("person_info_ui", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
    # renpy.profile_screen("main_choice_display", predict=True, show=True, update=True, request=True, time=True, debug=False, const=True)
