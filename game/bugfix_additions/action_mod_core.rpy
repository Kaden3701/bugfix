# ACTION MOD CORE by Tristimdorion
# Create a ActionMod class, it has the same parameters as the VREN Action class.
# Attach the ActionMod object to any action list in the game.
# If you need some extra initialization after the game has started pass an initialization function (None is default)
# ActionMod is added to save games when not present, the matching is based on the name property, so make sure it's unique (and don't change it between releases)

# pre define variable for saving
define action_mod_list = None

init -1 python:
    # Initialize the randomizer
    renpy.random.seed()

    # use this as initalization method for the ActionMod to make it disabled by default
    def init_action_mod_disabled(self):
        self.enabled = False
        return

    class ActionMod(Action):
        _instances = set()

        # store instances of mod
        def __init__(self, name, requirement, effect, args = None, requirement_args = None, menu_tooltip = None, priority = 10, event_duration = 99999, is_fast = True,
            initialization = None, category="Misc", enabled = True, allow_disable = True, on_enabled_changed = None, options_menu = None,
            is_crisis = False, is_morning_crisis = False, is_mandatory_crisis = False):
            self.initialization = initialization
            self.category = category
            self.enabled = enabled
            self.allow_disable = allow_disable
            self.on_enabled_changed = on_enabled_changed
            self.options_menu = options_menu
            self.is_crisis = is_crisis                      # chance to trigger during day
            self.is_morning_crisis = is_morning_crisis      # chance to trigger early morning
            self.is_mandatory_crisis = is_mandatory_crisis  # only triggered once when requirements are met

            Action.__init__(self, name, requirement, effect, args, requirement_args, menu_tooltip, priority, event_duration, is_fast)

            ActionMod._instances.add(self)

        def initialize(self):
            if self.initialization:
                self.initialization(self)

        def show_options(self):
            if self.options_menu and renpy.has_label(self.options_menu):
                renpy.call(self.options_menu)

        def toggle_enabled(self):
            self.enabled = not self.enabled
            # trigger event
            if self.on_enabled_changed:
                self.on_enabled_changed(self.enabled)

            # update in game crisis lists ()
            if self.is_crisis:
                def _update_crisis(cl, action):
                    found = next((x for x in cl if x[0] == action), None)
                    if found and not action.enabled:
                        cl.remove(found)
                    if not found and action.enabled:
                        cl.append([action, 5])

                if not self.is_morning_crisis:
                    _update_crisis(crisis_list, self)

                if self.is_morning_crisis:
                    _update_crisis(morning_crisis_list, self)

            if self.is_mandatory_crisis:
                def _update_mandatory_crisis(cl, action, add_func, remove_func):
                    found = next((x for x in cl if x == action), None)
                    if found and not action.enabled:
                        remove_func(action)
                    if not found and action.enabled:
                        add_func(action)

                if "mc" in globals() and not self.is_morning_crisis:
                    _update_mandatory_crisis(mc.business.mandatory_crises_list, self, mc.business.add_mandatory_crisis, mc.business.remove_mandatory_crisis)

                if "mc" in globals() and self.is_morning_crisis:
                    _update_mandatory_crisis(mc.business.mandatory_morning_crises_list, self, mc.business.add_mandatory_morning_crisis, mc.business.remove_mandatory_crisis)

    def action_mod_settings_requirement():
        return True

    def action_mod_configuration_requirement():
        return any(x for x in ActionMod._instances if x.options_menu)

    # check all ActionMod classes in the game and make sure we have one instance of each and update the action_mod_list
    def append_and_initialize_action_mods():
        # add action_mod instances to list
        if not ActionMod._instances is None:
            # renpy.say(None, "There are " + str(__builtin__.len(action_mod_list)) + " mods in save game.")
            for action_mod in sorted(ActionMod._instances, key = lambda x: x.priority):
                if action_mod not in action_mod_list:
                    action_mod_list.append(action_mod)
                    action_mod.initialize()

        # cleanup removed actions
        for action_mod in action_mod_list:
            if action_mod not in ActionMod._instances:
                action_mod_list.remove(action_mod)

        # the crisis_list is not stored in save game
        for action_mod in action_mod_list:
            if action_mod.is_crisis:
                if action_mod.is_morning_crisis:
                    if not action_mod in [c[0] for c in morning_crisis_list]:
                        morning_crisis_list.append([action_mod, 5])
                else:
                    if not action_mod in [c[0] for c in crisis_list]:
                        crisis_list.append([action_mod, 5])
            elif action_mod.is_mandatory_crisis:
                if action_mod.is_morning_crisis:
                    mc.business.add_mandatory_morning_crisis(action_mod)
                else:
                    mc.business.add_mandatory_crisis(action_mod)

        # init crisis tracker events after mod core update
        global excluded_crisis_tracker_events
        excluded_crisis_tracker_events = [
            x[0] for x in crisis_list + morning_crisis_list
                if x[0].effect in
                    [
                        "work_relationship_change_label",
                        "sister_phone_crisis_action_label",
                        "mom_selfie_label",
                        "late_for_work_action_label",
                        "research_reminder_crisis_label"
                    ]
        ]
        return

    def build_action_mod_configuration_menu():
        tuple_list = []
        for action_mod in action_mod_list:
            if action_mod.enabled and hasattr(action_mod, "options_menu") and not action_mod.options_menu is None:
                tuple_string = action_mod.name + " (tooltip)" + action_mod.menu_tooltip
                tuple_list.append([tuple_string, action_mod])

        tuple_list = sorted(tuple_list, key=lambda x: x[0])
        tuple_list.append(["Back","Back"])
        return renpy.display_menu(tuple_list, True, "Choice")

    # mod settings action
    action_mod_options_action = Action("MOD Settings", action_mod_settings_requirement, "show_action_mod_settings", menu_tooltip = "Enable or disable mods")
    action_mod_configuration_action = Action("MOD Configuration", action_mod_configuration_requirement, "show_action_mod_configuration", menu_tooltip = "Change configuration for individual MODS")

init 4 python: # NOTE: Having it at 5 was causing errors after I moved things around. Haven't seen any side-effects of it.
    add_label_hijack("normal_start", "activate_action_mod_core")
    add_label_hijack("after_load", "update_action_mod_core")

# as long as VREN doesn't use this, we need to add a dummy label for hijacking purposes
# NOTE: this label gets called after the hijack labels have been triggered
label after_load():
    return

label activate_action_mod_core(stack):
    # initialize variable
    $ action_mod_list = []

    # define here using $ so it gets stored in save game
    python:
        append_and_initialize_action_mods()

        bedroom.add_action(action_mod_options_action)
        bedroom.add_action(action_mod_configuration_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

# called after loading a save game
label update_action_mod_core(stack):
    python:
        unmodded = False
        try:
            action_mod_list
        except NameError:
            unmodded = True

        # extra check to validate that action mod list exists correctly
        if not unmodded and not isinstance(action_mod_list, list):
            unmodded = True

    if unmodded:
        # initialize variable
        $ action_mod_list = []

    python:
        append_and_initialize_action_mods()
        bedroom.add_action(action_mod_options_action)
        bedroom.add_action(action_mod_configuration_action)

        # continue on the hijack stack if needed
        execute_hijack_call(stack)
    return

label show_action_mod_settings():
    $ hide_ui()
    call screen mod_configuration_ui
    $ show_ui()
    return

label show_action_mod_configuration():
    python:
        action_mod_choice =  build_action_mod_configuration_menu()

        if action_mod_choice == "Back":
            renpy.return_statement()
        else:
            action_mod_choice.show_options()
    jump show_action_mod_configuration
