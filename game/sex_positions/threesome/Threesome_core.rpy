init python:
  def set_pos_align(trans, xchange, ychange):
    trans.xalign = xchange
    trans.yalign = ychange
    return None


transform threesome_test_1():
    yalign 0.5
    yanchor 0.5
    function set_pos_align
    zoom 1.0

transform threesome_test_2():
    yalign 0.5
    yanchor 0.5
    function set_pos_align
    zoom 1.0

init -1 python:
    list_of_threesomes = []
    girl_swap_pos = False  #Nasty hack to tell threesome code to swap girl 1 and girl 2. #TODO find a better way to do this
    THREESOME_BASE_SLUT_REQ = 80  #A constant to hold the usual base sluttiness requirements for threesomes.
    class Threesome_Position():
        def __init__(self,name,slut_requirement,position_one_tag, position_two_tag,girl_one_final_description,girl_two_final_description,requires_location,requirements,
        p1_transform, p2_transform, p1_z_order = 0, p2_z_order = 1, can_swap = False, verb = "fuck", verbing = None):
            self.name = name
            self.slut_requirement = slut_requirement #The required slut score of the girl. Obedience will help fill the gap if possible, at a happiness penalty. Value from 0 (almost always possible) to ~100
            self.position_one_tag = position_one_tag # The tag used to get the correct position image set
            self.position_two_tag = position_two_tag # The tag used to get the correct position image set
            self.girl_one_final_description = girl_one_final_description   #Textual position description if girl one is the final one in position
            self.girl_two_final_description = girl_two_final_description      #textual position description if girl two is the final one in position
            self.requires_location = requires_location #
            self.requirements = requirements        #The requirements to run this position. Should be a function
            self.mc_position = []                   #Holds the positions that MC can take during this position
            self.verb = verb #A verb used to describe the position. "Fuck" is default, and mostly used for sex positions or blowjobs etc. Kiss, Fool around, etc. are also possibilities.
            self.verbing = verbing
            self.current_modifier = None #We will update this if the position has a special modifier that should be applied, like blowjob.
            self.p1_transform = p1_transform
            self.p2_transform = p2_transform
            self.p1_z_order = p1_z_order
            self.p2_z_order = p2_z_order
            self.can_swap = can_swap

            if verbing is None:
                self.verbing = verb + "ing"

        # requires the existence of a scene_manager with both actors
        def update_scene(self, person_one, person_two):
            #print("Render: " + self.name + (" (Swapped)" if girl_swap_pos else ""))
            if girl_swap_pos:
                #print(person_two.name + " at: " + self.position_one_tag + ", z-order: " + str(self.p1_z_order))
                #print(person_one.name + " at: " + self.position_two_tag + ", z-order: " + str(self.p2_z_order))
                scene_manager.update_actor(person_two, position = self.position_one_tag, display_transform = self.p1_transform, z_order = self.p1_z_order)
                scene_manager.update_actor(person_one, position = self.position_two_tag, display_transform = self.p2_transform, z_order = self.p2_z_order)
            else:
                #print(person_one.name + " at: " + self.position_one_tag + ", z-order: " + str(self.p1_z_order))
                #print(person_two.name + " at: " + self.position_two_tag + ", z-order: " + str(self.p2_z_order))
                scene_manager.update_actor(person_one, position = self.position_one_tag, display_transform = self.p1_transform, z_order = self.p1_z_order)
                scene_manager.update_actor(person_two, position = self.position_two_tag, display_transform = self.p2_transform, z_order = self.p2_z_order)
            scene_manager.draw_scene()
            return

        def align_position(self, person_one, person_two):
            scene_manager.draw_scene()
            return

        def redraw_scene(self, person_one, person_two):
            scene_manager.draw_scene()
            return




    class Threesome_MC_position():
        def __init__(self,name,skill_tag_p1,skill_tag_p2,girl_one_arousal,girl_two_arousal,girl_one_source,girl_two_source,girl_one_energy,girl_two_energy,
            guy_arousal,skill_tag_guy,guy_source,guy_energy,intro,scenes,outro,strip_description,strip_ask_description,orgasm_description,swap_description,requirement,
            description = None, action_description = None, default_action_person = None):
            self.name = name
            self.description = description #Describes the position the MC is in
            self.action_description = action_description # Template for action {0} will be replaced with the action person number (one/two -> used for swap girls - description update)
            self.default_action_person = default_action_person
            self.skill_tag_p1 = skill_tag_p1 #The skill that will provide a bonus to this for girl 1
            self.skill_tag_p2 = skill_tag_p2 #The skill that will provide a bonus to this for girl 2
            self.girl_one_arousal = girl_one_arousal # The base arousal the girl receives from this position.
            self.girl_two_arousal = girl_two_arousal # The base arousal the girl receives from this position.
            self.girl_one_source = girl_one_source  #Who is giving girl 1 pleasure. 0 = MC, 1 = herself, 2 = girl 2
            self.girl_two_source = girl_two_source  #Who is giving girl 2 pleasure. 0 = MC, 1 = girl 1, 2 = herself
            self.girl_one_energy = girl_one_energy  #energy cost for girl 1
            self.girl_two_energy = girl_two_energy  #energy cost for girl 2
            self.guy_arousal = guy_arousal # The base arousal the guy receives from this position.
            self.skill_tag_guy = skill_tag_guy #The skill that will decide how much arousal MC receives.
            self.guy_source = guy_source # Who is giving MC pleasure. 0 = MC, 1 = girl 1, 2 = girl 2
            self.guy_energy = guy_energy #Energy burn for guy
            self.intro = intro
            self.scenes = scenes
            self.outro = outro
            self.strip_description = strip_description
            self.strip_ask_description = strip_ask_description
            self.orgasm_description = orgasm_description
            self.swap_description = swap_description
            self.requirement = requirement

        def call_intro(self, person_one, person_two, the_location, the_object):
            if girl_swap_pos:
                renpy.call(self.intro,person_two, person_one, the_location, the_object)
            else:
                renpy.call(self.intro,person_one, person_two, the_location, the_object)

        def call_scene(self, person_one, person_two, the_location, the_object):
            random_scene = renpy.random.randint(0,__builtin__.len(self.scenes)-1)
            if girl_swap_pos:
                renpy.call(self.scenes[random_scene],person_two, person_one, the_location, the_object)
            else:
                renpy.call(self.scenes[random_scene],person_one, person_two, the_location, the_object)

        def call_orgasm(self, person_one, person_two, the_location, the_object):
            if girl_swap_pos:
                renpy.call(self.orgasm_description,person_two, person_one, the_location, the_object)
            else:
                renpy.call(self.orgasm_description,person_one, person_two, the_location, the_object)

        def call_outro(self, person_one, person_two, the_location, the_object):
            if girl_swap_pos:
                renpy.call(self.outro,person_two, person_one, the_location, the_object)
            else:
                renpy.call(self.outro,person_one, person_two, the_location, the_object)

        def call_transition(self, person_one, person_two, the_location, the_object):
            if girl_swap_pos:
                renpy.call(self.swap_description,person_two, person_one, the_location, the_object)
            else:
                renpy.call(self.swap_description,person_one, person_two, the_location, the_object)

        def check_girl_one_energy(self, person_one):
            if girl_swap_pos:
                if self.girl_two_energy > person_one.energy:
                    return False
            else:
                if self.girl_one_energy > person_one.energy:
                    return False
            return True

        def check_girl_two_energy(self, person_two):
            if girl_swap_pos:
                if self.girl_one_energy > person_two.energy:
                    return False
            else:
                if self.girl_two_energy > person_two.energy:
                    return False
            return True

        def calc_arousal_changes(self, person_one, person_two):
            #Calculate arousal gains
            if girl_swap_pos:
                girl_one_arousal_change = self.girl_two_arousal + ((person_one.get_opinion_score("threesomes") / 5) * self.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
                if self.girl_two_source == 0:  #MC is source#
                    girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
                elif self.girl_two_source == 1:
                    girl_one_arousal_change += girl_one_arousal_change * person_one.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
                else:  #Assume girl 2 is source
                    girl_one_arousal_change += girl_one_arousal_change * person_two.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
            else:
                girl_one_arousal_change = self.girl_one_arousal + ((person_one.get_opinion_score("threesomes") / 5) * self.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
                if self.girl_one_source == 0:  #MC is source#
                    girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
                elif self.girl_one_source == 1: #Girl one is her own source? Maybe masturbating?
                    girl_one_arousal_change += girl_one_arousal_change * person_one.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
                else:  #Assume girl 2 is source
                    girl_one_arousal_change += girl_one_arousal_change * person_two.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level

            person_one.change_arousal(girl_one_arousal_change)  #Make the change

            #Repeat for girl two
            if girl_swap_pos:
                girl_two_arousal_change = self.girl_one_arousal + ((person_two.get_opinion_score("threesomes") / 5) * self.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
                if self.girl_one_source == 0:  #MC is source#
                    girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
                elif self.girl_one_source == 1: #Girl 1 is source
                    girl_two_arousal_change += girl_two_arousal_change * person_one.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
                else:  #Assume girl 2 is source
                    girl_two_arousal_change += girl_two_arousal_change * person_two.sex_skills[self.skill_tag_p1] * 0.1  #Add 10% per skill level
            else:
                girl_two_arousal_change = self.girl_two_arousal + ((person_two.get_opinion_score("threesomes") / 5) * self.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
                if self.girl_two_source == 0:  #MC is source#
                    girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
                elif self.girl_two_source == 1: #Girl 1 is source
                    girl_two_arousal_change += girl_two_arousal_change * person_one.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level
                else:  #Assume girl 2 is source
                    girl_two_arousal_change += girl_two_arousal_change * person_two.sex_skills[self.skill_tag_p2] * 0.1  #Add 10% per skill level

            person_two.change_arousal(girl_two_arousal_change)  #Make the change

            #MC arousal change
            his_arousal_change = self.guy_arousal
            if self.guy_source == 0:
                his_arousal_change += 0.1 * mc.sex_skills[self.skill_tag_guy]
            elif girl_swap_pos:
                if self.guy_source == 1:
                    his_arousal_change += 0.1 * person_two.sex_skills[self.skill_tag_guy]
                else:
                    his_arousal_change += 0.1 * person_one.sex_skills[self.skill_tag_guy]
            else:
                if self.guy_source == 1:
                    his_arousal_change += 0.1 * person_one.sex_skills[self.skill_tag_guy]
                else:
                    his_arousal_change += 0.1 * person_two.sex_skills[self.skill_tag_guy]


            mc.change_arousal(his_arousal_change)

        def get_mc_pleasure_source(self, person_one, person_two):
            if self.guy_source == 0:
                return None #Masturbating
            if girl_swap_pos:
                if self.guy_source == 1:
                    return person_two
                else:
                    return person_one
            if self.guy_source == 1:
                return person_one
            return person_two



label threesome_test():
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom)
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    $ scene_manager.strip_full_outfit()
    call start_threesome(mom, lily) from threesome_test_call_1
    $ scene_manager.clear_scene()
    return "Test Complete"

label threesome_join_test():
    $ scene_manager = Scene()
    $ scene_manager.add_actor(mom, position = "standing_doggy")
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    lily "Let me take off some clothes."
    $ scene_manager.strip_full_outfit()
    call join_threesome(mom, lily, "standing_doggy", private = True) from _call_threesome_join_test
    $ scene_manager.clear_scene()
    return "Test Complete"

label threesome_alignment():
    $ position_choice = threesome_double_blowjob
    $ position_choice.update_scene(mom, lily)
    $ finished = False
    while not finished:
        menu:
            "mom + x":
                $ position_choice.p1_transform.xpos += .01
                pass
            "mom - x":
                $ position_choice.p1_transform.xpos -= .01
                pass
            "mom + y":
                $ position_choice.p1_transform.yalign += .01
                pass
            "mom - y":
                $ position_choice.p1_transform.yalign -= .01
                pass
            "mom + zoom":
                $ position_choice.p1_transform.zoom += .01
                pass
            "mom - zoom":
                $ position_choice.p1_transform.zoom -= .01
                pass
            "lily + x":
                pass
            "lily - x":
                pass
            "lily + y":
                pass
            "lily - y":
                pass
            "lily + zoom":
                pass
            "lily - zoom":
                pass
        $ position_choice.align_position(the_person_one, the_person_two)  #This doesn't work lol. Delete? I hate transforms

init 5 python:
    def build_threesome_round_start_menu(position_choice, person_one, person_two):
        option_list = []
        option_list.append("Start Choice")
        for options in position_choice.mc_position:
            if options.requirement(person_one, person_two):
                option_list.append([options.description,options.name])
        option_list.append(["Change your mind and leave", "Leave"])
        return option_list

    def build_threesome_round_choice_menu(position_choice, person_one, person_two, position_locked, hide_leave):
        option_list = []
        option_list.append("Round Choice")
        if position_choice is not None:
            option_list.append(["Keep going","Continue"]) #Note: you're prevented from continuing if the energy cost would be too high by the pre-round checks.
            if not (person_one.outfit.has_full_access or person_two.outfit.has_full_access):
                option_list.append(["Pause and strip them down","Strip"])

            #Give option for MC to change position without changing the girls positions
            for options in position_choice.mc_position:
                if options != active_mc_position:
                    if options.requirement(person_one, person_two):
                        option_list.append([options.description,options.name])

            if not position_locked:
                option_list.append(["Pause and change position\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
                #### For now, no implementation of connections
                # for position in position_choice.connections:
                #     if object_choice.has_trait(position.requires_location):
                #         appended_name = "Transition to " + position.build_position_willingness_string(the_person) #Note: clothing and energy checks are done inside of build_position_willingness, invalid positiosn marked (disabled)
                #         option_list.append([appended_name,position])

            if not hide_leave: #TODO: Double check that we can always get out
                option_list.append(["Stop fucking and leave", "Leave"]) #TODO: Have this appear differently depending on if you've cum yet, she's cum yet, or you've both cum.

        else:
            if not position_locked:
                option_list.append(["Pick a new position\n-5 {image=gui/extra_images/arousal_token.png}","Change"])
            if not (person_one.outfit.has_full_access or person_two.outfit.has_full_access):
                option_list.append(["Strip them down","Strip"])
            if not hide_leave:
                option_list.append(["Stop and leave", "Leave"])
        return option_list

    def build_threesome_person_one_position_choice_menu(person_one, person_two):
        option_list = []
        option_list.append(person_one.name + " position:")
        for threeway in list_of_threesomes:
            if threeway.requirements(person_one, person_two):
                if (get_initial_threesome_pairing(threeway.position_one_tag)) not in option_list: #This doesn't work for stand2-5 TODO
                    option_list.append(get_initial_threesome_pairing(threeway.position_one_tag))
                if (get_initial_threesome_pairing(threeway.position_two_tag)) not in option_list:
                    option_list.append(get_initial_threesome_pairing(threeway.position_two_tag))
        return option_list

    def build_threesome_person_two_position_choice_menu(person_one, person_two):
        option_list = []
        option_list.append(person_two.name + " position:")
        for threeway in list_of_threesomes:
            if threeway.requirements(person_one, person_two):
                if threeway.position_one_tag == girl_one_choice:            #Look for positions that match with any position taken by girl 1
                    option_list.append([threeway.girl_two_final_description, threeway.position_two_tag])
                elif threeway.position_two_tag == girl_one_choice:
                    option_list.append([threeway.girl_one_final_description, threeway.position_one_tag])
        if __builtin__.len(option_list) == 0:
            renpy.say(None, "Something has gone wrong, no available positions")  #Return something default?
        return option_list

    def build_threesome_strip_menu(person_one, person_two):
        option_list = []
        option_list.append("Stripping Choice")
        if not person_one.outfit.has_full_access:
            option_list.append (["Strip " + person_one.title, "strip_one"])
        if not person_two.outfit.has_full_access:
            option_list.append (["Strip " + person_two.title, "strip_two"])
        option_list.append (["Finished", "Leave"])
        return option_list

    def update_threesome_action_description(position, swapped):
        for mc_pos in position.mc_position:
            if mc_pos.action_description:
                if swapped:
                    mc_pos.description = mc_pos.action_description.replace("{0}", "one" if mc_pos.default_action_person == "two" else "two")
                else:
                    mc_pos.description = mc_pos.action_description.replace("{0}", "two" if mc_pos.default_action_person == "two" else "one")
        return

    def choose_threesome_position(girl_one_choice, girl_two_choice):
        for threeway in list_of_threesomes:
            if girl_one_choice == threeway.position_one_tag and girl_two_choice == threeway.position_two_tag:
                position_choice = threeway
                swapped = False
            if girl_one_choice == threeway.position_two_tag and girl_two_choice == threeway.position_one_tag:
                position_choice = threeway
                swapped = True

        #print ("Chosen Position: " + threeway.name + (" (Swapped)" if girl_swap_pos else ""))

        update_threesome_action_description(position_choice, swapped)
        return (position_choice, swapped)

    def valid_threesome_position(position):
        return any([x for x in list_of_threesomes if position in [x.position_one_tag, x.position_two_tag]])

    def get_mc_round_choice(position_choice, person_one, person_two):
        option_list = []
        for options in position_choice.mc_position:
            if options.requirement(person_one, person_two):
                option_list.append([options.description,options.name])
        option_list.append(["Change your mind and leave", "Leave"])
        return renpy.display_menu(option_list,True,"Choice")

    def get_mc_active_position(position_choice, round_choice):
        for options in position_choice.mc_position:
            if round_choice == options.name:
                return options
        return None

label start_threesome(the_person_one, the_person_two, start_position = None, start_object = None, skip_intro = False, private = True, girl_in_charge = False, position_locked = False, report_log = None, affair_ask_after = True, hide_leave = False, swapped = False):
    # When called
    if report_log is None:
        $ report_log = create_report_log()

    $ finished = False #When True we exit the main loop (or never enter it, if we can't find anything to do)
    $ position_choice = None
    $ object_choice = None
    $ girl_swap_pos = swapped

    #Family situational modifiers
    #Omitting these for now

    #Cheating modifiers
    #Also leaving these out

    #Privacy modifiers

    #Love modifiers. Always applies if negative, but only adds a bonus if you are in private.

    #If no initial position set, get one now
    if start_position is None:
        call pick_threesome(the_person_one, the_person_two) from threesome_initial_position_set
        $ position_choice = _return
    else:
        $ position_choice = start_position
        $ update_threesome_action_description(position_choice, girl_swap_pos)
    #pick_threesome can give use the option to swap the girls opening spots
    # if girl_swap_pos:
    #     $ the_person = the_person_one
    #     $ the_person_one = the_person_two
    #     $ the_person_two = the_person
    #     $ int_swap = report_log["girl one orgasms"]
    #     $ report_log["girl one orgasms"] = report_log["girl two orgasms"]
    #     $ report_log["girl two orgasms"] = int_swap

    $ position_choice.update_scene(the_person_one, the_person_two)
    if not skip_intro:
        "As the girls get into position, you consider how to begin your threesome."

    # We start any encounter by letting them pick what position they want (unless something is forced or the girl is in charge)
    $ active_mc_position = None
    call screen main_choice_display(build_menu_items([build_threesome_round_start_menu(position_choice, the_person_one, the_person_two)]))
    $ round_choice = _return

    if round_choice == "Leave":
        "Really? You changed your mind? You leave the poor girls after you got them all ready for some action."
    else:
        $ mc.listener_system.fire_event("threesome", the_person_one = the_person_one, the_person_two = the_person_two)
        $ active_mc_position = get_mc_active_position(position_choice, round_choice)
        if active_mc_position is None:
            "Something broke..."
            $ round_choice = "Leave"
        elif not skip_intro:
            $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice)
            $ scene_manager.draw_scene()    # intro can cause stripping and wrong layer drawing
            $ round_choice = None
        else:
            $ round_choice = None
    while not finished:
        # if girl_in_charge:
        #     # For now, default to guys only in charge
        if round_choice is None: #If there is no set round_choice
            #TODO: Add a variant of this list when the girl is in control to ask if you want to resist or ask/beg for something.

            call screen main_choice_display(build_menu_items([build_threesome_round_choice_menu(position_choice, the_person_one, the_person_two, position_locked, hide_leave)]))
            $ round_choice = _return

        # Now that a round_choice has been picked we can do something.
        if round_choice == "Change" or round_choice == "Continue":
            if round_choice == "Change": # If we are changing we first select and transition/intro the position, then run a round of sex. If we are continuing we ignore all of that
                "You decide to change it up."
                call pick_threesome(the_person_one, the_person_two) from threesome_mid_position_set
                $ position_choice = _return
                # if girl_swap_pos:
                #     $ the_person = the_person_one
                #     $ the_person_one = the_person_two
                #     $ the_person_two = the_person
                #     $ int_swap = report_log["girl one orgasms"]
                #     $ report_log["girl one orgasms"] = report_log["girl two orgasms"]
                #     $ report_log["girl two orgasms"] = int_swap
                $ position_choice.update_scene(the_person_one, the_person_two)
                "As the girls get into position, you consider how to resume your threesome."
                $ round_choice = get_mc_round_choice(position_choice, the_person_one, the_person_two)
                $ active_mc_position = get_mc_active_position(position_choice, round_choice)
                if round_choice == "Leave":
                    $ finished = True
                    "You decide to finish the threesome instead."

                if not active_mc_position:
                    "Something broke..."
                    $ finished = True
                else:
                    $ active_mc_position.call_intro(the_person_one, the_person_two, mc.location, object_choice)
                    $ scene_manager.draw_scene() # call intro can cause stripping and wrong z-order draw

            $ start_position = None #Clear start positions/objects so they aren't noticed next round.
            $ start_object = None
            if active_mc_position and position_choice: #If we have both an object and a position we're good to go, otherwise we loop and they have a chance to choose again.
                call threesome_round(the_person_one, the_person_two, position_choice = active_mc_position, object_choice = None, private = private, report_log = report_log) from _call_threesome_round_1
                $ first_round = False
                if not active_mc_position.requirement(the_person_one, the_person_two):
                    "Your post-orgasm cock softens, stopping you from continuing for now."
                    $ position_choice = None
                    $ active_mc_position = None
                elif active_mc_position.guy_energy > mc.energy:
                    "You're too exhausted to continue [position_choice.verbing] [the_person.possessive_title]."
                    $ position_choice = None
                    $ active_mc_position = None
                elif not active_mc_position.check_girl_one_energy(the_person_one):
                    the_person_one "I'm exhausted [the_person_one.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_two.energy > 30:
                        #TODO give option to continue fucking the second girl
                        the_person_two "Don't worry, I'm still good to go!"
                        "Do you want to continue?"
                        menu:
                            "Fuck [the_person_two.title]":
                                "[the_person_one.title] moves to the side and recovers while you resume activities with [the_person_two.title]."
                                $ scene_manager.hide_actor(the_person_one)
                                $ report_log["girl orgasms"] = report_log["girl two orgasms"]
                                call fuck_person(the_person_two, private = private, report_log = report_log) from threesome_to_twosome_transition_1
                                $ scene_manager.show_actor(the_person_one, display_transform = character_center_flipped)
                                $ report_log["girl two orgasms"] = _return["girl orgasms"]

                            "Done for now":
                                mc.name "I think we should just be done for now." #TODO girl takes over if she needs to cum and hasn't yet
                        $ finished = True
                    else:
                        the_person_two "Yeah me too. I think I need a break!"
                        $ finished = True
                elif not active_mc_position.check_girl_two_energy(the_person_two):
                    the_person_two "I'm exhausted [the_person_two.mc_title], I can't keep this up..."
                    $ position_choice = None
                    $ active_mc_position = None
                    if the_person_one.energy > 30:
                        the_person_one "Don't worry, I'm still good to go!"
                        "Do you want to continue?"
                        menu:
                            "Fuck [the_person_one.title]":
                                "[the_person_two.title] moves to the side and recovers while you resume activities with [the_person_one.title]."
                                $ scene_manager.hide_actor(the_person_two)
                                $ report_log["girl orgasms"] = report_log["girl one orgasms"]
                                call fuck_person(the_person_one, private = private, report_log = report_log) from threesome_to_twosome_transition_2
                                $ scene_manager.show_actor(the_person_two, display_transform = character_center_flipped)
                                $ report_log["girl one orgasms"] = _return["girl orgasms"]
                            "Done for now":
                                mc.name "I think we should just be done for now." #TODO girl takes over if she needs to cum and hasn't yet
                        $ finished = True

                        pass
                    else:
                        the_person_one "Yeah me too. I think I need a break!"
                        $ finished = True
                #else: #Nothing major has happened that requires us to change positions, we can have girls take over, strip
                #for now disable stripping
                    #pass
                    #call girl_strip_event(the_person, position_choice, object_choice) from _call_girl_strip_event

        elif round_choice == "Strip":
            #currently not implemented
            call threesome_strip_menu(the_person_one, the_person_two) from _call_strip_menu_threesome_1

        elif round_choice == "Leave":
            $ finished = True # Unless something stops us the encounter is over and we can end


        elif round_choice == "Girl Leave":
            $ finished = True
        #Need to catch position changes here.
        else:
            $ active_mc_position = get_mc_active_position(position_choice, round_choice)
            $ active_mc_position.call_transition(the_person_one, the_person_two, mc.location, object_choice)

        $ round_choice = None #Get rid of our round choice at the end of the round to prepare for the next one. By doing this at the end instead of the beginning of the loop we can set a mandatory choice for the first one.


    # Teardown the sex modifiers

    if report_log["girl one orgasms"] > 0:
        $ the_person_one.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_one.arousal = (the_person_one.arousal / 2)
    if report_log["girl two orgasms"] > 0:
        $ the_person_two.arousal = 0 # If she came she's satisfied.
    else:
        $ the_person_two.arousal = (the_person_two.arousal / 2)

    #Easy marker to add to log if EVERYONE orgasmed
    if report_log["girl one orgasms"] > 0 and report_log["girl two orgasms"] > 0 and report_log["guy orgasms"] > 0:
        $ report_log["trifecta"] = True



    #Disabling affair check for now. Doesn't really make sense in a threesome.
    # if affair_ask_after and private and ask_girlfriend_requirement(the_person_one) is True and not the_person_one.relationship == "Single":
    #     if the_person_one.love >= 60 and the_person_one.sluttiness >= 30 - (the_person_one.get_opinion_score("cheating on men") * 5) and report_log.get("girl orgasms",0) >= 1: #If she loves you enoguh, is moderately slutty, and you made her cum
    #         call affair_check(the_person_one, report_log) from _call_affair_check_threesome_one


    python: #Log all of the different classes of sex, but only once per class.
        if the_person_one.sex_record.get("Threesomes", 0) == 0:
            the_person_one.sex_record["Threesomes"] = 1
        else:
            the_person_one.sex_record["Threesomes"] += 1
        if the_person_two.sex_record.get("Threesomes", 0) == 0:
            the_person_two.sex_record["Threesomes"] = 1
        else:
            the_person_two.sex_record["Threesomes"] += 1

        # record the last time we had sex
        the_person_one.sex_record["Last Sex Day"] = day
        the_person_two.sex_record["Last Sex Day"] = day

        mc.condom = False
        mc.recently_orgasmed = False
        active_mc_position = None
        object_choice = None
        position_choice = None
        round_choice = None
        options = None
        the_person_one = None
        the_person_two = None

    # We return the report_log so that events can use the results of the encounter to figure out what to do.
    return report_log

label threesome_round(the_person_one, the_person_two, position_choice, object_choice = None, private = True, report_log = None):
    #Draw event before calling this scene

    #Normal round events
    $ position_choice.call_scene(the_person_one, the_person_two, mc.location, object_choice)
    # TODO listener event, to log events for challenge
    if report_log is not None:
        $ report_log["total rounds"] += 1

    #Calculate arousal gains
    $ position_choice.calc_arousal_changes(the_person_one, the_person_two)
    #
    # $ girl_one_arousal_change = position_choice.girl_one_arousal + ((the_person_one.get_opinion_score("threesomes") / 5) * position_choice.girl_one_arousal)   #20% arousal bonus for each level of threesome like/dislike
    # if position_choice.girl_one_source == 0:  #MC is source#
    #     $ girl_one_arousal_change += girl_one_arousal_change * mc.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level
    # elif position_choice.girl_one_source == 1: #Girl one is her own source? Maybe masturbating?
    #     $ girl_one_arousal_change += girl_one_arousal_change * the_person_one.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level
    # else:  #Assume girl 2 is source
    #     $ girl_one_arousal_change += girl_one_arousal_change * the_person_two.sex_skills[position_choice.skill_tag_p1] * 0.1  #Add 10% per skill level
    #
    # $ the_person_one.change_arousal(girl_one_arousal_change)  #Make the change
    # #Repeat for girl two
    # $ girl_two_arousal_change = position_choice.girl_two_arousal + ((the_person_two.get_opinion_score("threesomes") / 5) * position_choice.girl_two_arousal)   #20% arousal bonus for each level of threesome like/dislike
    # if position_choice.girl_two_source == 0:  #MC is source#
    #     $ girl_two_arousal_change += girl_two_arousal_change * mc.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level
    # elif position_choice.girl_one_source == 1: #Girl 1 is source
    #     $ girl_two_arousal_change += girl_two_arousal_change * the_person_one.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level
    # else:  #Assume girl 2 is source
    #     $ girl_two_arousal_change += girl_two_arousal_change * the_person_two.sex_skills[position_choice.skill_tag_p2] * 0.1  #Add 10% per skill level
    #
    # $ the_person_two.change_arousal(girl_two_arousal_change)  #Make the change
    #
    # #MC arousal change
    # $ his_arousal_change = position_choice.guy_arousal
    # if position_choice.guy_source == 0:
    #     $ his_arousal_change += 0.1 * mc.sex_skills[position_choice.skill_tag_guy]
    # elif position_choice.guy_source == 1:
    #     $ his_arousal_change += 0.1 * the_person_one.sex_skills[position_choice.skill_tag_guy]
    # else:
    #     $ his_arousal_change += 0.1 * the_person_two.sex_skills[position_choice.skill_tag_guy]
    #
    #
    # $ mc.change_arousal(his_arousal_change)
    #Erection changes
    if mc.recently_orgasmed and mc.arousal_perc >= 10:
        $ mc.recently_orgasmed = False
        "Your cock stiffens again, coaxed back to life by the girls."

    #Energy Changes
    $ mc.change_energy(-position_choice.guy_energy)
    $ the_person_one.change_energy(-position_choice.girl_one_energy)
    $ the_person_two.change_energy(-position_choice.girl_two_energy)

    #Add clarity
    $ mc.locked_clarity += (position_choice.guy_arousal * 10)

    #If girl(s) orgasms, call orgasm scene
    if the_person_one.arousal_perc >= 100 or the_person_two.arousal_perc >= 100:
        $ position_choice.call_orgasm(the_person_one, the_person_two, mc.location, object_choice)

        if the_person_one.arousal_perc >= 100:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_one)
            $ the_person_one.change_stats(arousal = -the_person_one.arousal/2, happiness = 5)
            $ report_log["girl one orgasms"] += 1
            $ report_log["total orgasms"] += 1
        if the_person_two.arousal_perc >= 100:
            $ mc.listener_system.fire_event("girl_climax", the_person = the_person_two)
            $ the_person_two.change_stats(arousal = -the_person_two.arousal/2, happiness = 5)
            $ report_log["girl two orgasms"] += 1
            $ report_log["total orgasms"] += 1

    #If MC orgasms, call outro
    if mc.arousal_perc >= 100:
        $ position_choice.call_outro(the_person_one, the_person_two, mc.location, object_choice)
        $ the_person_one.change_obedience(3)
        $ the_person_two.change_obedience(3)
        $ mc.reset_arousal()
        if perk_system.has_ability_perk("Serum: Energy Regeneration") and mc_serum_energy_regen.trait_tier >= 2 and mc.energy > 30:
            $ mc.recently_orgasmed = False
            "Despite your orgasm, because of your Energy Regeneration Serum, your cock quickly gets hard again, allowing you to continue."
        else:
            $ mc.recently_orgasmed = True
        $ report_log["guy orgasms"] += 1
        $ report_log["total orgasms"] += 1
        if position_choice.get_mc_pleasure_source(the_person_one, the_person_two):   #returns none if MC is pleasuring himself
            $ ClimaxController.manual_clarity_release(climax_type = "threesome", the_person = (position_choice.get_mc_pleasure_source(the_person_one, the_person_two)))
        else:
            $ ClimaxController.manual_clarity_release()

    #TODO set public sex responses

    return

label pick_threesome(the_person_one, the_person_two, girl_one_position = None, object_choice = None):  #We can pass in a position for girl one if the second girl "walks in" on the sex event
    if not (girl_one_position and valid_threesome_position(girl_one_position)):
        call screen main_choice_display(build_menu_items([build_threesome_person_one_position_choice_menu(the_person_one, the_person_two)]))
        $ girl_one_choice = _return
    else:
        $ girl_one_choice = girl_one_position

    call screen main_choice_display(build_menu_items([build_threesome_person_two_position_choice_menu(the_person_one, the_person_two)]))
    $ girl_two_choice = _return

    $ (position_choice, girl_swap_pos) = choose_threesome_position(girl_one_choice, girl_two_choice)

    #TODO figure out if position requires an object, if so select the object#
    return position_choice

label threesome_strip_menu(the_person_one, the_person_two):
    call screen main_choice_display(build_menu_items([build_threesome_strip_menu(the_person_one, the_person_two)]))
    $ strip_choice = _return

    if strip_choice == "strip_one":
        mc.name "[the_person_one.title], I want you to give me full access."
        the_person_one "Of course!"
        $ scene_manager.strip_full_outfit(person = the_person_one)
        $ scene_manager.draw_scene()
    elif strip_choice == "strip_two":
        mc.name "[the_person_two.title], I want you to give me full access."
        the_person_two "Sounds good!"
        $ scene_manager.strip_full_outfit(person = the_person_two)
        $ scene_manager.draw_scene()
    else:
        return
    call threesome_strip_menu(the_person_one, the_person_two) from _threesome_recurrent_strip_call_1
    return

label join_threesome(the_person_one, the_person_two, initial_position, private = True, report_log = None):  #We can use this function to add a second girl to an existing sex scene.
    #Works by selecting a position then calling threesome with the first position pre-set
    $ girl_swap_pos = False # reset swapped
    call pick_threesome(the_person_one, the_person_two, girl_one_position = initial_position) from _join_threesome_position_selection_1
    $ position_choice = _return
    call start_threesome(the_person_one, the_person_two, start_position = position_choice, skip_intro = True, private = private, report_log = report_log) from _join_threesome_in_progress_1

    return _return

init python:
    def get_initial_threesome_pairing(position_tag):
        if position_tag == "stand2" or position_tag == "stand3" or position_tag == "stand4" or position_tag == "stand5":
            return (["Stand Right There", "stand"])  #TODO this probably isn't going to work right. Figure out another way to do this. Or don't write positions using standX?
        elif position_tag == "walking_away":
            return (["Turn Away From Me", "walking_away"])
        elif position_tag == "kissing":
            return (["Put Your Arms Up", "kissing"])
        elif position_tag == "missionary":
            return (["Lay on Your Back", "missionary"])
        elif position_tag == "blowjob":
            return (["Get on Your Knees", "blowjob"])
        elif position_tag == "against_wall":
            return (["Put Your Back to the Wall", "against_wall"])
        elif position_tag == "back_peek":
            return (["Turn Away But Look At Me", "back_peek"])
        elif position_tag == "sitting":
            return (["Sit Down", "sitting"])
        elif position_tag == "kneeling1":
            return (["Lay Forward", "kneeling1"])
        elif position_tag == "standing_doggy":
            return (["Bend Over", "standing_doggy"])
        elif position_tag == "doggy":
            return (["Get on Your Hands and Knees", "doggy"])
        elif position_tag == "cowgirl":
            return (["Sit on Top", "cowgirl"])
        else:
            return (["Broken Position", "stand4"])

    def can_join_threesome(person_one, person_two, initial_position_tag): #Can use this function to check if there is a threesome position available that a second girl can join.
        if person_one.energy < 50 or person_two.energy < 50:
            return False

        for threeway in list_of_threesomes:
            if threeway.requirements(person_one, person_two):
                if threeway.position_one_tag == initial_position_tag:            #Look for positions that match with any position taken by girl 1
                    return True
                elif threeway.position_two_tag == initial_position_tag:
                    return True
        return False

    def willing_to_threesome(person_one, person_two):    #Use this function to check and see if two people are willing to engage in a threesome
        # only allow threesomes when we had sex before (without condom)
        if person_one.has_taboo(["sucking_cock", "condomless_sex"]):
            return False
        if person_two.has_taboo(["sucking_cock", "condomless_sex"]):
            return False
        if person_one.get_opinion_score("threesomes") <= -2 or person_two.get_opinion_score("threesomes") <= -2:
            return False

        person_one_slut_req = THREESOME_BASE_SLUT_REQ
        person_two_slut_req = THREESOME_BASE_SLUT_REQ
        if town_relationships.is_family(person_one, person_two):
            person_one_slut_req += (-5 * (person_one.get_opinion_score("incest") - 2)) #Incest modifier
            person_two_slut_req += (-5 * (person_two.get_opinion_score("incest") - 2)) #Incest modifier

        # threesome opinion modifier
        person_one_slut_req += (person_one.get_opinion_score("threesomes") * -5)
        person_two_slut_req += (person_two.get_opinion_score("threesomes") * -5)

        if person_one.effective_sluttiness() < person_one_slut_req:
            return False
        if person_two.effective_sluttiness() < person_two_slut_req:
            return False
        return True
