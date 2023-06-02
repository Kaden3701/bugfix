init -2 python:
    class Position():
        def __init__(self,name,slut_requirement,slut_cap,requires_hard, requires_large_tits,
            position_tag,requires_location,requires_clothing,skill_tag,
            girl_arousal,girl_energy,guy_arousal,guy_energy,connections,
            intro,scenes,outro,transition_default,
            strip_description, strip_ask_description,
            orgasm_description,
            taboo_break_description,
            verb = "fuck", verbing = None, opinion_tags = None, record_class = None,
            default_animation = None, modifier_animations = None,
            associated_taboo = None):


            self.name = name
            self.slut_requirement = slut_requirement #The required slut score of the girl. Obedience will help fill the gap if possible, at a happiness penalty. Value from 0 (almost always possible) to ~100
            self.slut_cap = slut_cap #The maximum sluttiness that this position will have an effect on.
            self.requires_hard = requires_hard
            self.requires_large_tits = requires_large_tits

            self.girl_arousal = girl_arousal # The base arousal the girl receives from this position.
            self.girl_energy = girl_energy # The amount of energy the girl spends on this position.

            self.guy_arousal = guy_arousal # The base arousal the guy receives from this position.
            self.guy_energy = guy_energy # The base energy the guy spends on this position.

            self.position_tag = position_tag # The tag used to get the correct position image set.
            self.requires_location = requires_location # A tag that must match an object to have sex on it (eg. "lean", which needs something like a wall to lean against)
            self.requires_clothing = requires_clothing # A tag that notes what (lack of) clothing requirements the position has. Vaginal requires access to her vagina, tits her tits.
            self.skill_tag = skill_tag #The skill that will provide a bonus to this position.
            self.opinion_tags = opinion_tags #The opinion that will be checked each round.
            self.connections = connections
            self.intro = intro
            self.taboo_break_description = taboo_break_description #Called instead of the intro/transition when you break a taboo with someone. Should include call to personality taboo specific dialogue.
            self.scenes = scenes
            self.outro = outro
            self._girl_outro = None # possible override for GIC
            self.transition_default = transition_default #TODO: add transitions that go between related positions but with different objects. Things like standing sex into fucking her against a window.
            self.transitions = []
            self.strip_description = strip_description
            self.strip_ask_description = strip_ask_description
            self.orgasm_description = orgasm_description
            self.verb = verb #A verb used to describe the position. "Fuck" is default, and mostly used for sex positions or blowjobs etc. Kiss, Fool around, etc. are also possibilities.
            if verbing is None: #The verb used as "Go back to [verbing] her.". Added specifically to support things like grope/groping, which have different spellings depending.
                self.verbing = verb + "ing"
            else:
                self.verbing = verbing
            self.record_class = record_class #A key to Person.sex_record[] that is updated once (and only once!) per sexual encounter if this position is picked.

            self.current_modifier = None #We will update this if the position has a special modifier that should be applied, like blowjob.

            if default_animation is None:
                self.default_animation = idle_wiggle_animation
            else:
                self.default_animation = default_animation #If not None this is used to animate the character if nothing else is specifically handed over.

            if modifier_animations is None: #If an animation exists for a special modifier it is used instead of the default one.
                self.modifier_animations = {}
            else:
                self.modifier_animations = modifier_animations

            self.associated_taboo = associated_taboo #What taboo tag, if any, is associated with this position. Until broken a taboo makes a position harder to select, but the taboo is broken once it is done once.
            self._last_scene = None # store last run scene, to prevent running same scene twice
            self._double_orgasm = None  # special scene when both MC and Girl come simultaneously

            # Current sex related taboo are:
            # kissing, touching_body, touching_penis, touching_vagina, sucking_cock, licking_pussy, vaginal_sex, anal_sex
            # And as a special case for vaginal sex: condomless_sex

        @property
        def last_scene(self):
            return self._last_scene

        @last_scene.setter
        def last_scene(self, value):
            self._last_scene = value

        @property
        def girl_outro(self):
            return self._girl_outro

        @girl_outro.setter
        def girl_outro(self, value):
            self._girl_outro = value

        @property
        def double_orgasm(self):
            return self._double_orgasm

        @double_orgasm.setter
        def double_orgasm(self, value):
            self._double_orgasm = value


        def link_positions(self, other, transition_label): #This is a one way link!
            self.connections.append(other)
            self.transitions.append([other,transition_label])

        def link_positions_two_way(self, other, transition_label_1, transition_label_2): #Link it both ways. Great for adding a modded position without modifying other positions.
            self.link_positions(other, transition_label_1)
            other.link_positions(self, transition_label_2)

        def call_intro(self, person, location, the_object):
            renpy.call(self.intro,person, location, the_object)

        def call_taboo_break(self, person, location, the_object):
            renpy.call(self.taboo_break_description, person, location, the_object)

        def call_scene(self, person, location, the_object):
            choice_list = [x for x in self.scenes if not x == self.last_scene]
            new_scene = get_random_from_list(choice_list) if choice_list else get_random_from_list(self.scenes)
            self.last_scene = new_scene
            renpy.call(new_scene, person, location, the_object)

        def call_outro(self, person, location, the_object):
            if self.girl_outro:  #Rely on girl outro tocall default outro if appropriate
                renpy.call(self.girl_outro, person, location, the_object)
            else:
                self.call_default_outro(person, location, the_object)

        def call_default_outro(self, person, location, the_object):
            renpy.call(self.outro,person, location, the_object)

        def call_transition(self, new_position, person, location, the_object):
            def get_position_name(position):
                return position.name.lower().replace(" ", "_")

            if not new_position is None:
                transition_scene = "transition_" + get_position_name(self) + "_" + get_position_name(new_position)
                #renpy.say(None, "Custom transition function is: " + transition_scene)
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling custom transition function: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)

                transition_scene = new_position.transition_default
                for position_tuple in self.transitions:
                    if position_tuple[0] == new_position: ##Does the position match the one we are looking for?
                        transition_scene = position_tuple[1] ##If so, set it's label as the one we are going to change to.

                #renpy.say(None, "Default transition scene is: " + transition_scene)
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling default transition scene: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)

            else: # we are calling from the new position (we don't have an old position to start from)
                transition_scene = self.transition_default
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling default transition: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)
            return

        # try different types of taboo break, the final choice is the break for the actual position broken
        # added an extra check to make sure the label exists, if not the taboo is broken without dialog
        def call_transition_taboo_break(self, new_position, person, location, the_object):
            def get_position_name(position):
                return position.name.lower().replace(" ", "_")

            if not new_position is None:
                transition_scene = "transition_" + get_position_name(self) + "_to_" + get_position_name(new_position) + "_taboo_break_label"
                #renpy.say(None, "Custom taboo break function is: " + transition_scene)
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling custom taboo break: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)

                #renpy.say(None, "Default taboo break function: " + new_position.taboo_break_description)
                if renpy.has_label(new_position.taboo_break_description):
                    #renpy.say(None, "Calling default taboo break: " + new_position.taboo_break_description)
                    renpy.call(new_position.taboo_break_description, person, location, the_object)

                transition_scene = new_position.transition_default
                for position_tuple in self.transitions:
                    if position_tuple[0] == new_position: ##Does the position match the one we are looking for?
                        transition_scene = position_tuple[1] ##If so, set it's label as the one we are going to change to.

                #renpy.say(None, "Default transition scene is: " + transition_scene)
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling default transition scene: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)

            else: # we are calling from the new position (we don't have an old position to start from)
                #renpy.say(None, "Default taboo break function: " + self.taboo_break_description)
                if renpy.has_label(self.taboo_break_description):
                    #renpy.say(None, "Calling default taboo break: " + self.taboo_break_description)
                    renpy.call(self.taboo_break_description, person, location, the_object)

                transition_scene = self.transition_default
                if renpy.has_label(transition_scene):
                    #renpy.say(None, "Calling default transition: " + transition_scene)
                    renpy.call(transition_scene, person, location, the_object)
            return

        def call_strip(self, person, clothing, location, the_object):
            renpy.call(self.strip_description, person, clothing, location, the_object)

        def call_strip_ask(self, person, clothing, location, the_object):
            renpy.call(self.strip_ask_description, person, clothing, location, the_object)

        def call_orgasm(self, person, location, the_object):
            renpy.call("call_orgasm_enhanced_label", self, person, location, the_object)

        def check_clothing(self, person):
            if self.requires_clothing == "Vagina":
                return person.vagina_available
            elif self.requires_clothing == "Tits":
                return person.tits_available
            else:
                return True ##If you don't have one of the requirements listed above just let it happen.

        def calculate_arousal_modified_speed(self, person):
            male_energy_fraction = (1.0*self.guy_energy) / ((self.guy_energy+self.girl_energy) or 1)  # Animation strength is divided based on who is spending more energy (ie. girls giving blowjobs speed up as they get horny, not you).
            male_animation_effect = male_energy_fraction * (mc.arousal/(mc.max_arousal or 1))  # Being closer to max arousal increases the speed of the animation.

            female_energy_fraction = (1.0*self.girl_energy) / ((self.guy_energy+self.girl_energy) or 1)
            female_animation_effect = female_energy_fraction * (person.arousal_perc / 100)

            the_animation_speed = 0.5 + (0.5 * (male_animation_effect + female_animation_effect)) #Scales the animation strength from 50% to 100%, increasing as each party gets more aroused.

            return the_animation_speed

        def calculate_position_requirements(self, person, ignore_taboo = False, only_known_opinions = False):
            position_taboo = self.associated_taboo
            if ignore_taboo:
                position_taboo = None

            final_slut_requirement = self.slut_requirement
            final_slut_cap = self.slut_cap
            if self.skill_tag == "Anal" and person.has_family_taboo:
                final_slut_requirement -= 5 #It's easier to convince a family member to have anal sex, since it's not "real" incest or something.
                final_slut_cap -= 5
            elif self.skill_tag == "Vaginal" and person.has_family_taboo:
                final_slut_requirement += 10 #It's harder to convince a family member to have vaginal sex
                final_slut_cap += 10

            if self.opinion_tags:
                for opinion_tag in self.opinion_tags:
                    final_slut_cap -= (person.get_known_opinion_score(opinion_tag) if only_known_opinions else person.get_opinion_score(opinion_tag)) * 5
                    final_slut_requirement -= (person.get_known_opinion_score(opinion_tag) if only_known_opinions else person.get_opinion_score(opinion_tag)) * 5
            if person.has_taboo(position_taboo):
                final_slut_requirement += 10    # when she has a taboo increase slut requirement
                final_slut_cap += 10

            return final_slut_requirement, final_slut_cap

        def redraw_scene(self, person, emotion = None): #redraws the scene, call this when something is modified.
            the_animation_speed = self.calculate_arousal_modified_speed(person)

            if self.current_modifier in self.modifier_animations:
                position_animation = self.modifier_animations[self.current_modifier]
            else:
                position_animation = self.default_animation

            person.draw_person(self.position_tag, emotion = emotion, special_modifier = self.current_modifier, the_animation = position_animation, animation_effect_strength = the_animation_speed)

        def her_position_willingness_check(self, person, ignore_taboo = False): #Checks if the given girl would/can pick this position. A mirror of the main character's options.
            possible = True

            position_taboo = self.associated_taboo
            if ignore_taboo:
                position_taboo = None

            final_slut_requirement = self.slut_requirement
            final_slut_cap = self.slut_cap
            if self.skill_tag == "Anal" and person.has_family_taboo:
                final_slut_requirement += -10 #It's easier to convince a family member to have anal sex, since it's not "real" incest or something.
                final_slut_cap += -10
            elif self.skill_tag == "Vaginal" and person.has_family_taboo:
                final_slut_requirement += 10 #It's harder to convince a family member to have vaginal sex
                final_slut_cap += 10


            if final_slut_requirement > person.effective_sluttiness(position_taboo):
                possible = False # Too slutty for her.
            elif not self.check_clothing(person):
                possible = False # Clothing is in the way.
            elif mc.energy < self.guy_energy or person.energy < self.girl_energy:
                possible = False # One of them is too tired.
            elif self.requires_hard and mc.recently_orgasmed:
                possible = False # The mc has cum recently and isn't hard.
            elif self.requires_large_tits and not person.has_large_tits:
                possible = False # You need large tits for this and she doesn't have it.

            return possible

        def build_position_willingness_string(self, person, ignore_taboo = False): #Generates a string for this position that includes a tooltip and coloured willingness for the person given.
            #Generates a list of strings for this position that includes a tooltip and coloured willingness for the person given.

            willingness_string = ""
            tooltip_string = ""

            girl_expected_arousal = str(__builtin__.int(self.girl_arousal * (1 + 0.1 * mc.sex_skills[self.skill_tag]))) #Estimate what they'll gain based on both of your skills to make the predictions as accurate as possible.
            guy_expected_arousal = str(__builtin__.int(self.guy_arousal * (1 + 0.1 * person.sex_skills[self.skill_tag])))

            energy_string = "   {color=#A3A3FF}" + str(self.calculate_energy_cost(mc)) + "{/color}/{color=#FF6EC7}" + str(self.calculate_energy_cost(person)) + "{/color} {image=energy_token_small}"
            arousal_string =  ", {color=#A3A3FF}" + guy_expected_arousal + "{/color}/{color=#FF6EC7}" + girl_expected_arousal + "{/color} {image=arousal_token_small}"

            disable = False
            position_taboo = self.associated_taboo

            if ignore_taboo:
                position_taboo = None

            final_slut_requirement, final_slut_cap = self.calculate_position_requirements(person, ignore_taboo, only_known_opinions = True)

            taboo_break_string = ""
            if person.has_taboo(position_taboo):
                taboo_break_string = " {image=taboo_break} "

            opinion_score = self.get_opinion_score(person)

            #NOTE: Removed the (tooltip) and (disabled) tags as they aren't needed in the screen which is their only use case at the moment, but consider adding those back in if being used in the renpy.display_menu
            if person.effective_sluttiness(position_taboo) > final_slut_cap:
                if opinion_score < 1 and person.arousal > final_slut_cap:
                    willingness_string = "{color=#6b6b6b}Boring{/color}" #No sluttiness gain AND half arousal gain
                    tooltip_string = " (tooltip) This position is too boring to interest her when she is this horny. No sluttiness increase and her arousal gain is halved."
                else:
                    willingness_string = "{color=#A3A3FF}Comfortable{/color}" #No sluttiness
                    tooltip_string = " (tooltip) This position is too tame for her tastes. No sluttiness increase, but it may still be a good way to get warmed up and ready for other positions."
            elif person.effective_sluttiness(position_taboo) >= final_slut_requirement:
                willingness_string = "{color=#3DFF3D}Exciting{/color}" #Normal sluttiness gain
                tooltip_string = " (tooltip) This position pushes the boundary of what she is comfortable with. Increases temporary sluttiness, which may become permanent over time or with serum application."
            elif person.effective_sluttiness(position_taboo) + person.obedience-100 >= final_slut_requirement:
                willingness_string = "{color=#FFFF3D}Likely Willing if Commanded{/color}"
                tooltip_string = " (tooltip) This position is beyond what she would normally consider. She is obedient enough to do it if she is commanded, at the cost of some happiness."
            else:
                willingness_string = "{color=#FF3D3D}Likely Too Slutty{/color}"
                tooltip_string = " (tooltip) This position is so far beyond what she considers appropriate that she would never dream of it."

            if person.has_taboo(position_taboo):
                tooltip_string +="\nSuccessfully selecting this position will break a taboo, making it easier to convince " + (person.title if person.title else "her") + " to do it and similar acts in the future."

            if not self.check_clothing(person):
                disable = True
                willingness_string += "\nObstructed by clothing"
            elif mc.recently_orgasmed and self.requires_hard:
                disable = True
                willingness_string += "\nRecently orgasmed"
            elif mc.energy < self.guy_energy and person.energy < self.girl_energy:
                disable = True
                willingness_string += "\nYou're both too tired"
            elif mc.energy < self.guy_energy:
                disable = True
                willingness_string += "\nYou're too tired"
            elif person.energy < self.girl_energy:
                disable = True
                willingness_string += "\nShe's too tired"

            change_amount = 0
            if self.opinion_tags:
                for opinion_tag in self.opinion_tags:
                    opinion_topic = person.get_opinion_topic(opinion_tag)
                    if opinion_topic:
                        # renpy.say(None, person.name + ": " + opinion_tag + " => " + str(person.get_opinion_score(opinion_tag)))
                        if opinion_topic[1]: # only show info when opinion is known
                            change_amount += person.get_opinion_score(opinion_tag) * 3 #Add a bonus or penalty if she likes or dislikes the position.

            position_opinion = ""
            if change_amount > 0:
                position_opinion = " {image=thumbs_up}"
            elif change_amount < 0:
                position_opinion = " {image=thumbs_down}"

            if disable:
                return taboo_break_string + self.name + position_opinion + "\n{size=12}" + willingness_string + "{/size}" + " (disabled)" #Don't show the arousal and energy string if it's disabled to prevent overrun
            else:
                return taboo_break_string + self.name + position_opinion + "\n{size=12}" + willingness_string + energy_string + arousal_string + "{/size}" + tooltip_string

        def calculate_energy_cost(self, person): # Calculates this positions's true energy cost based on the skill of the participants.
            base_energy = 0
            if isinstance(person, Person):
                base_energy = self.girl_energy
            else:
                base_energy = self.guy_energy
            return __builtin__.int(base_energy * (1 - (0.05*person.sex_skills[self.skill_tag])))

        def build_energy_string(self, person):
            return "{color=#A3A3FF}" + str(self.calculate_energy_cost(mc)) + "{/color}/{color=#FF6EC7}" + str(self.calculate_energy_cost(person)) + "{/color} {image=gui/extra_images/energy_token.png}"

        def build_arousal_string(self, person):
            girl_expected_arousal = str(int(self.girl_arousal * (1 + 0.1 * mc.sex_skills[self.skill_tag]))) #Estimate what they'll gain based on both of your skills to make the predictions as accurate as possible.
            guy_expected_arousal = str(int(self.guy_arousal * (1 + 0.1 * person.sex_skills[self.skill_tag])))
            return "{color=#A3A3FF}" + guy_expected_arousal + "{/color}/{color=#FF6EC7}" + girl_expected_arousal + "{/color} {image=gui/extra_images/arousal_token.png}"

        def build_energy_arousal_line(self, person):
            return "{size=18}" + self.build_energy_string(person) + " | " + self.build_arousal_string(person) + "{/size}"

        def get_opinion_score(self, person):   #An override of this function to avoid girls getting bored of positions.
            opinion_score = 0
            for opinion_tag in self.opinion_tags:
                opinion_score += person.get_opinion_score(opinion_tag) #Add a bonus or penalty if she likes or dislikes the position.
                person.discover_opinion(opinion_tag)
            if opinion_score <= 0 and perk_system.has_ability_perk("Serum: Aura of Arousal") and mc_serum_aura_arousal.trait_tier >= 2:
                if self.skill_tag == "Vaginal" or self.skill_tag == "Anal":
                    opinion_score = 1
                elif mc_serum_aura_arousal.trait_tier >= 3:
                    opinion_score = 1
            return opinion_score

        def get_trance_chance_modifier(self, person):
            trance_chance_modifier = 0
            for opinion_tag in self.opinion_tags:
                trance_chance_modifier += 2 * person.get_opinion_score(opinion_tag)
            return trance_chance_modifier


# this must be a label since renpy.call() always return to next label statement
# and not python code, so renpy.call must always be the last statement
label call_orgasm_enhanced_label(the_position, the_person, the_location, the_object):
    $ orgasm_choice = True
    if the_position.double_orgasm and perk_system.has_ability_perk("Serum: Feat of Orgasm Control"):
        if mc_serum_feat_orgasm_control.trait_tier >= 1 or mc.arousal >= mc.max_arousal:
            call climax_check_double_orgasm_control_label() from _double_orgasm_check_01
            $ orgasm_choice = _return

    if orgasm_choice and the_position.double_orgasm and mc.arousal >= mc.max_arousal:
        $ renpy.call(the_position.double_orgasm, the_person, the_location, the_object)
    else:
        $ renpy.call(the_position.orgasm_description, the_person, the_location, the_object)
    return
