#This class is designed to hold all the variables and labels required to create a corruption progression scene.
#Class contains labels for all parts of the scene in a list, which progresses automatically in corruption based on specified conditions
#Class should track what stage the progression is at so it can be referenced easily and should save the progress in save file
#Class should compile at startup the list of stages of the progression_scene so that it can be modified and added to as necessary
#Class may have to reference another class in the event of a branching storyline
#Use a character's init file to call their progression scene recompiles.


init -2 python:
    #Default function to run between cycles if we do a default unit test.
    def progression_scene_test_func_default(the_group = []):
        for person in the_group:
            person_one.change_slut(10, 100)
            person_one.change_energy(200)
        time_of_day = 1
        return

    list_of_progression_scenes = []

    class Progression_Scene():

        def __init__(self, compile_scenes, start_scene_list, req_list, trans_list, final_scene_list, intro_scene, exit_scene, progression_scene_action, choice_scene,
            stage = -1, advance_time = True, business_action = False, person_action = False, is_random = False, role_action = False, unit_test_func = None,
            is_multiple_choice = False, multiple_choice_scene = None, regress_scene_list = []):

            self.stage = stage  #The corruption level of the progression_scene event
            self.compile_scenes = compile_scenes #Use this function to recompile the lists. Should be run on game load and initial game start.
            self.intro_scene = intro_scene  #Scene to play the first time this progression_scene is called
            self.exit_scene = exit_scene    #If MC decides not to participate.
            self.choice_scene = choice_scene    #Use this to determine if MC wants to stay or leave the event.
            self.progression_scene_action = progression_scene_action  #Use this as a generic action that can be added to any girl to proc the event.
            self.name = self.progression_scene_action.name
            self.start_scene_list = start_scene_list    #Scene to play at the beginning of the progression_scene. Mostly to build lust and set the stage.
            self.req_list = req_list    #Requirements used to determine if we are advancing corruption levels
            self.trans_list = trans_list    #A transition between corruption levels.
            self.final_scene_list = final_scene_list    #The act of the progression_scene itself
            self.advance_time = advance_time    #IF the event should advance time. Probably yes?
            self.business_action = business_action  #If the action should be a business (mandatory) crisis
            self.person_action = person_action      #if the action should be a person (on room enter) crisis
            self.is_random = is_random              #If this action only pops up randomly.
            self.role_action = role_action          #if this a selectable action and is part of a role.
            if unit_test_func is None:              #Set a unit test function
                self.unit_test_func = progression_scene_test_func_default
            else:
                self.unit_test_func = unit_test_func
            self.is_multiple_choice = is_multiple_choice    #Set to true if we want MC to decide which final scene to play.
            self.multiple_choice_scene = multiple_choice_scene  #Use this scene to setup the choice. IE how do you fuck her, etc.
            self.regress_scene_list = regress_scene_list        #Fill this list if we want progress here to be capable of regressing.
            self.scene_unlock_list = []                         #Hold a list of scene refences. Should be numbers only, EG: [0,1,2,5]

        def get_stage(self):
            return self.stage

        def set_stage(self, stage):
            self.stage = stage

        def call_intro(self, the_group):
            renpy.call(self.intro_scene, the_group)
            return

        def call_start_scene(self, the_group):
            if len(self.start_scene_list) < self.stage + 1: #If the list is shorter than the index, assume the last on the list is the function we want to call.
                renpy.call(self.start_scene_list[-1], the_group)
            else:
                renpy.call(self.start_scene_list[self.stage], the_group)
            return

        def call_trans_scene(self, the_group):
            renpy.call(self.trans_list[self.stage], the_group)
            return

        def call_multi_trans_scene(self, the_group, the_stage):
            renpy.call(self.trans_list[the_stage], the_group)
            return

        def call_regress_scene(self, the_group):
            renpy.call(self.regress_scene_list[self.stage], the_group)

        def call_final_scene(self, the_group, scene_transition):
            renpy.call(self.final_scene_list[self.stage], the_group, scene_transition)
            return

        def call_multi_final_scene(self, the_group, scene_transition, the_stage):
            renpy.call(self.final_scene_list[the_stage], the_group, scene_transition)
            return

        def call_exit_scene(self, the_group):
            renpy.call(self.exit_scene, the_group)
            return

        def call_choice_scene(self, the_group):
            return renpy.call(self.choice_scene, the_group)

        def call_multiple_choice_scene(self, the_group):
            return renpy.call(self.multiple_choice_scene, the_group)

        def is_progress_only(self):
            if len(self.regress_scene_list) == 0:
                return True
            return False

        def recompile_scenes(self):
            self.compile_scenes(self)
            return

        def call_scene(self, the_group):
            renpy.call("progression_scene_label", self, the_group)
            return

        def run_unit_test(self, the_group, cycles = 10):
            scene_count = 0
            while scene_count < cycles:
                self.call_scene(the_group)
                self.unit_test_func(the_group)
            return

        def run_stage_test(self, the_group):
            renpy.call("progression_scene_stage_test_label", self, the_group)
            return

        def reset_scene(self):
            self.recompile_scenes()
            self.scene_unlock_list = []
            self.stage = -1
            return

        def progression_available(self):
            if self.is_multiple_choice:
                counter = 0
                while counter < len(self.trans_list):
                    if counter not in progression_scene.scene_unlock_list:
                        if progression_scene.req_list[counter]():
                            return True
                    counter += 1
                return False
                #Check all choices for possible progression.
            elif len(self.req_list) > self.stage + 1: #Only try if there is another scene
                if self.req_list[self.stage + 1]():
                    return True
            return False

        def update(self):
            if self.role_action:
                if self.progression_available():
                    self.progression_scene_action.name = self.name + " {image=gui/extra_images/Progress24.png}"
                else:
                    self.progression_scene_action.name = self.name



label progression_scene_label(progression_scene, the_group):
    #First, add the event back so that it recurs. For a role event, leave these two properties false.
    if progression_scene.business_action:
        $ mc.business.add_mandatory_crisis(progression_scene.progression_scene_action)
    if progression_scene.person_action:
        $ the_group[0].add_unique_on_room_enter_event(progression_scene.progression_scene_action)

    # If the stage is -1, it has not been run before. Call the intro.
    if progression_scene.stage == -1:
        $ progression_scene.stage = 0
        # "Progressions stage should now be 0"

        if progression_scene.intro_scene:
            $ progression_scene.call_intro(the_group)
            if progression_scene.is_multiple_choice:    #IF it is multiple choice, add the basic scene to the list of options.
                $ progression_scene.scene_unlock_list.append(0)
            if progression_scene.advance_time:
                python:
                    for x in the_group:
                        x.apply_serum_study()
                call advance_time from _call_advance_progression_scene_class_02
            return
        #If there isn't an intro scene, just play the [0] scene

    #First, play the start scene
    $ progression_scene.call_start_scene(the_group)
    #Allow players to opt out
    $ progression_scene.call_choice_scene(the_group)
    if not _return:
        $ progression_scene.call_exit_scene(the_group)
        return

    $ scene_transition = False    #pass in to the final scene if we played a transition or not. It may change the final scene.

    #If the scene is multiple choice, check and see if we unlocked any new "choices"
    if progression_scene.is_multiple_choice:
        $ counter = 0
        $ scene_choice = None
        python:
            while counter < len(progression_scene.trans_list):
                if counter not in progression_scene.scene_unlock_list:
                    if progression_scene.req_list[counter]():
                        progression_scene.scene_unlock_list.append(counter)
                        scene_transition = True
                        scene_choice = counter
                        progression_scene.call_multi_trans_scene(the_group, counter)
                        break
                counter += 1

        if not scene_transition:    #If we didn't unlock any new choices, let player choose what scene to play in multiple choice scene.
            $ progression_scene.call_multiple_choice_scene(the_group)
            $ scene_choice = _return

        #Now play the final scene
        $ progression_scene.call_multi_final_scene(the_group, scene_transition, scene_choice)



    else:
        #if it is linear progression, first check if we can progress this scene.
        if len(progression_scene.req_list) > progression_scene.stage + 1: #Only try if there is another scene
            if progression_scene.req_list[progression_scene.stage + 1]():
                $ progression_scene.stage = progression_scene.stage + 1
                $ progression_scene.call_trans_scene(the_group)
                $ scene_transition = True
        #If the scene can regress, check and see if we need to regress a step
        if not progression_scene.is_progress_only() and progression_scene.stage != 0:
            if not progression_scene.req_list[progression_scene.stage](the_group):
                $ progression_scene.stage = progression_scene.stage - 1
                $ progression_scene.call_regress_scene(the_group)
                $ scene_transition = True

        #Call the appropriate final scene.
        $ progression_scene.call_final_scene(the_group, scene_transition)
    if progression_scene.advance_time:
        python:
            for x in the_group:
                x.apply_serum_study()
        call advance_time from _call_advance_progression_scene_class_01
    return

label progression_scene_stage_test_label(progression_scene, the_group):
    "This is a unit test for [progression_scene.name] scene."
    "First, I'll load each person in the group for you to modify stats."
    $ count = 0
    $ the_stage
    while count < len(the_group):
        $ the_person = the_group[count]
        "[the_person.title] is now loaded as the person."
        "Please use the cheat menu to set to appropriate stats you want to test them at."
        "Done? Okay moving on to the next one."
        $ count += 1
    "Okay, now I'll attempt to let you set the event stage."
    "Note: this will reset progress on this scene in this save file."
    "Note: This menu does nothing for multiple choice scenes. If you are testing a multiple choice scene, I recommend setting their stats and just calling the scene over and over."
    "Note, if you have a large number of stages, you might have to go and edit this scene to make it possible to see them all here."
    "This label is at at the bottom of progression_scene.rpy found in mods/core/helper_functions !"
    "What stage should we set the event to?"
    menu:
        "-1":
            $ the_stage = -1
        "0":
            $ the_stage = 0
        "1" if len(progression_scene.req_list) > 1:
            $  the_stage = 1
        "2" if len(progression_scene.req_list) > 2:
            $  the_stage = 2
        "3" if len(progression_scene.req_list) > 3:
            $  the_stage = 3
        "4" if len(progression_scene.req_list) > 4:
            $  the_stage = 4
        "5" if len(progression_scene.req_list) > 5:
            $  the_stage = 5
        "6" if len(progression_scene.req_list) > 6:
            $  the_stage = 6
        "7" if len(progression_scene.req_list) > 7:
            $  the_stage = 7
        "8" if len(progression_scene.req_list) > 8:
            $  the_stage = 8
        "9" if len(progression_scene.req_list) > 9:
            $  the_stage = 9
        "10" if len(progression_scene.req_list) > 10:
            $  the_stage = 10
        "11" if len(progression_scene.req_list) > 11:
            $  the_stage = 11
    $ progression_scene.stage = the_stage
    "Okay, here we go!"
    $ progression_scene.call_scene(the_group)
    "Unit test complete?"
    return
