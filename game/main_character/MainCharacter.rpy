init -2 python:
    class MainCharacter():
        def __init__(self, location, name, last_name, business, stat_array, skill_array, sex_array):
            self.location = location
            self.name = name
            self.last_name = last_name
            self.energy = 50
            self.designed_wardrobe = Wardrobe("Designed Wardrobe")
            self.business = business
            self.inventory = SerumInventory()

            ##Mental stats##
            #Mental stats are generally fixed and cannot be changed permanently.
            self.charisma = stat_array[0]#How likeable the person is. Mainly influences marketing, also determines how well interactions with other characters go. Main stat for HR and sales
            self.int = stat_array[1] #How smart the person is. Mainly influences research, small bonuses to most tasks. #Main stat for research and production.
            self.focus = stat_array[2]#How on task the person stays. Influences most tasks slightly. #Main stat for supplies

            ##Work Skills##
            #Skills can be trained up over time, but are limited by your raw stats.
            self.hr_skill = skill_array[0]
            self.market_skill = skill_array[1]
            self.research_skill = skill_array[2]
            self.production_skill = skill_array[3]
            self.supply_skill = skill_array[4]

            ##Sex Stats##
            # These are physical stats about the character that impact how they behave in a sex scene. Future values might include penis size or sensitivity.
            self.arousal = 0 #How close to an orgasm you are. You cum when you reach your max_arousal, default 100.
            self.max_arousal = 100

            self.masturbation_novelty = 100 #How novel masturbation is. As something becomes less Novel you convert clarity less efficiently.
            self.locked_clarity = 50 #Clarity generated by events, but not yet released by cumming.
            self.free_clarity = 25 #Clarity unlocked by cumming, available for use unlocking serum traits.

            ##Sex Skills##
            # These skill represent your knowledge and experience with different types of intimacy. Useful for raising a girls arousal faster than your own.
            self.sex_skills = {}
            self.sex_skills["Foreplay"] = sex_array[0] # A catch all for everything that goes on before blowjobs, sex, etc. Includes things like kissing, massages, etc.
            self.sex_skills["Oral"] = sex_array[1] # Your skill at eating a girl out.
            self.sex_skills["Vaginal"] = sex_array[2] # Your skill at different positions that involve vaginal sex.
            self.sex_skills["Anal"] = sex_array[3] # Your skill skill at different positions that involve anal sex.
            #
            # self.max_stamina = 2 # How many times you can seduce someone each day
            # self.current_stamina = 2 # Current stamina.

            self.max_energy = 100 #Your physical energy. Mainly consumed by having sex, slowly comes back during the day (with some actions speeding this up), and a lot of it returns at the end of the day
            self.energy = self.max_energy

            self.main_character_actions = [] # A list of actions enabled for the main character when they talk to people. Kind of like a "role" for the MC.

            self.condom = False #True if you currently have a condom on. (maintained by sex scenes). TODO: Allow a third "broken" state and add dialgoue and descriptions for that.
            self.recently_orgasmed = False #If True you recently orgasmed and aren't hard until your arousal rises to 10 or the encounter ends.

            self.known_home_locations = MappedList(Room, all_locations_in_the_game) #When the MC learns a character's home location the room reference should be added here. They can then get to it from the map.

            self.having_text_conversation = None #Set to a Person when dialogue should be taking place on the phone. Logs dialogue (but not narration) as appropriate.
            self.text_conversation_paused = False #Shows the say window as normal for all dialogue with the phone display underneath if having_text_conversation is set to a Person

            self.phone = TextMessageManager()

            self.listener_system = ListenerManagementSystem() #A listener manager to let us enroll to events and update goals when they are triggered.

            #How many free points does the main character have to spend on their skills/abilities
            self.free_stat_points = 0
            self.free_work_points = 0
            self.free_sex_points = 0

            #The maximum score you can have in each of the major skill categories
            self.max_stats = 8
            self.max_work_skills = 8
            self.max_sex_skills = 8
            self.max_energy_cap = 200

            #The current goals set for the player to achieve. On completion they gain 1 point towards that class of skills
            self.stat_goal = None
            self.work_goal = None
            self.sex_goal = None

            #The difficulty of goals. Some goals will be removed once the difficulty is high enough, others will be added, and some will have completion requirements based on the difficulty.
            self.stat_goal_difficulty = 0
            self.work_goal_difficulty = 0
            self.sex_goal_difficulty = 0

            self.clarity_purchase_level = 0 #Increased by 1 every time you buy a stat with Clarity.
            # Each level costs 50*(2^level)

            self.log_items = [] #A list of items to display as a log. is a tuple of: [string_to_display, text_style, unix_time]
            self.log_max_size = 20

            self.scrap_goal_available = True

            self.can_skip_time = False #A flag used to determine when it is safe to skip time and when it is not. Left in as of v0.19.0 to ensure missed references do not cause a crash; has no function.

            self.stolen_underwear = {} #Person should be a key, and should hold a list of clothing that has been taken by the MC.
            self.event_triggers_dict = {} #General purpose dict for storing event flags related to the MC.

        @property
        def location(self):
            if not hasattr(self, "_location"):
                self._location = None
            return next((x for x in list_of_places if x.identifier == self._location), bedroom) # fallback location is MC bedroom

        @location.setter
        def location(self, value):
            if isinstance(value, Room):
                self._location = value.identifier

        def change_location(self,new_location, show_background = True):
            if isinstance(new_location, Room):
                self.location = new_location
                for person in [x for x in list_of_people if x.follow_mc]:
                    person.change_location(new_location)
                if show_background:
                    self.location.show_background()

        def change_stats(self, arousal = None, locked_clarity = None, energy = None, add_to_log = True):
            message = []
            if not arousal is None:
                self.change_arousal(arousal)
                message.append(("+" if arousal > 0 else "") + str(arousal) + " {image=arousal_token_small}")
            if not locked_clarity is None:
                self.change_locked_clarity(locked_clarity, add_to_log = False)
                message.append(("+" if locked_clarity > 0 else "") + str(locked_clarity) + " {image=lust_eye_token_small}")
            if not energy is None:
                amount = self.change_energy(energy, add_to_log = False)
                if amount and amount != 0:
                    message.append(("+" if amount > 0 else "") + str(amount) + " {image=energy_token_small}")
            if add_to_log and message:
                mc.log_event("You: " + " ".join(message), "float_text_yellow")
                if not locked_clarity is None and persistent.clarity_messages:
                    effect_strength = __builtin__.min((amount/80.0) + 0.4, 1.0)
                    renpy.show_screen("border_pulse", effect_strength, _transient = True)

        def change_arousal(self,amount):
            amount = __builtin__.int(__builtin__.round(amount))
            self.arousal += amount
            if self.arousal < 0:
                self.arousal = 0

        def reset_arousal(self):
            self.arousal = 0

        @property
        def arousal_perc(self):
            return ((self.arousal * 1.0) / (self.max_arousal or 1)) * 100

        @property
        def lust_tier(self):
            if self.locked_clarity > 1500:
                return 4
            if self.locked_clarity > 700:
                return 3
            if self.locked_clarity > 300:
                return 2
            if self.locked_clarity > 100:
                return 1
            return 0

        def change_energy(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.energy > self.max_energy:
                amount = self.max_energy - self.energy
            elif amount + self.energy < 0:
                amount = -self.energy

            self.energy += amount

            if add_to_log and amount != 0:
                log_string = "You: " + ("+" if amount > 0 else "") + str(amount)  + " Energy"
                mc.log_event(log_string, "float_text_yellow")
            return amount

        def change_max_energy(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            self.max_energy += amount
            if self.max_energy < 0:
                self.max_energy = 0

            if self.energy > self.max_energy: #No having more energy than max in case we lower max
                self.energy = self.max_energy

            if add_to_log and amount != 0:
                log_string = "You: " + ("+" if amount > 0 else "") + str(amount) + " Max Energy"
                mc.log_event(log_string, "float_text_yellow")
            return

        def change_masturbation_novelty(self, amount, add_to_log = True):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount + self.masturbation_novelty > 100:
                amount = 100 - self.masturbation_novelty

            elif amount + self.masturbation_novelty < 50:
                amount = -(self.masturbation_novelty - 50)

            self.masturbation_novelty += amount

            if add_to_log and amount != 0:
                log_string = "You: " + ("+" if amount > 0 else "") + str(amount) + " Masturbation Novelty"
                mc.log_event(log_string, "float_text_yellow")

        def change_locked_clarity(self, amount, add_to_log = True): #TODO: Decide if we need a max locked clarity thing to gate progress in some way.
            if "perk_system" in globals() and perk_system is not None:
                amount = amount * get_clarity_multiplier()
                if perk_system.get_ability_flag("Lustful Priorities"):
                    amount += 5

            amount = __builtin__.int(__builtin__.round(amount))
            self.locked_clarity += amount

            arousal = amount * .2
            if arousal > 5:
                arousal = 5
            self.change_arousal(arousal)

            if add_to_log and amount != 0:
                log_string = "You: " + ("+" if amount > 0 else "") + str(amount) + " {image=lust_eye_token_small} " + ("+" if arousal > 0 else "") + str(arousal)+ " {image=arousal_token_small}"
                mc.log_event(log_string, "float_text_blue")

                effect_strength = __builtin__.min((amount/80.0) + 0.4, 1.0)
                renpy.show_screen("border_pulse", effect_strength, _transient = True)
            return

        def convert_locked_clarity(self, conversion_multiplier = 1.0, with_novelty = None, add_to_log = True): #TODO: Decide if clarity should decay over time.
            amount = self.locked_clarity * conversion_multiplier
            if with_novelty:
                amount = amount * (with_novelty/100.0) #NOTE: Novelty is a score from 50 to 100, but is often treated as a percent.
            amount = __builtin__.int(__builtin__.round(amount))
            self.locked_clarity = 0
            self.free_clarity += amount

            if add_to_log and amount != 0:
                log_string = "You: " + str(amount) + " Clarity Released!"
                if with_novelty and with_novelty < 100:
                    log_string += "\n{}% lost due to low Novelty.".format(100-with_novelty)
                mc.log_event(log_string, "float_text_blue")
                renpy.show_screen("cum_screen", _transient = True)
            return

        def spend_clarity(self, amount, add_to_log = False):
            amount = __builtin__.int(__builtin__.round(amount))
            if amount < 0: #No spending negative clarity.
                return

            if amount > self.free_clarity:
                amount = self.free_clarity

            self.free_clarity += -amount

            if add_to_log and amount != 0:
                log_string = "You: Spent " + str(amount) + " Clarity"
                mc.log_event(log_string, "float_text_blue")
            return

        def add_clarity(self, amount, add_to_log = True): #Adds a flat amount of Clarity, without interacting with Locked Clarity. Used when an outside influence generates Clarity.
            amount = __builtin__.int(__builtin__.round(amount))
            if amount < 0:
                return

            self.free_clarity += amount

            if add_to_log and amount != 0:
                log_string = "You: received " + str(amount) + " Clarity"
                mc.log_event(log_string, "float_text_blue")
            return

        def save_design(self, the_outfit, new_name, outfit_type = "full"):
            the_outfit.name = new_name
            if outfit_type == "under":
                self.designed_wardrobe.add_underwear_set(the_outfit)
            elif outfit_type == "over":
                self.designed_wardrobe.add_overwear_set(the_outfit)
            else: #Generally outfit_type == full, or some other uncaught error.
                self.designed_wardrobe.add_outfit(the_outfit)

        @property
        def is_home(self):
            return self.location in home_hub

        @property
        def is_at_work(self): #Checks to see if the main character is at work, generally used in crisis checks.
            return self.location in office_hub

        @property
        def is_in_bed(self):
            return time_of_day == 4 and self.location == bedroom

        @property
        def has_dungeon(self):
            return mc.business.event_triggers_dict.get("dungeon_owned", False)


        def run_turn(self):
            self.listener_system.fire_event("time_advance")
            self.change_arousal(-20)
            self.change_energy(self.max_energy * .2, add_to_log = False)
            return

        def run_day(self):
            self.listener_system.fire_event("end_of_day")
            self.change_energy(self.max_energy * .6, add_to_log = False)
            self.change_masturbation_novelty(1, add_to_log = False)
            self.reset_arousal()
            self.scrap_goal_available = True

        def complete_goal(self, the_finished_goal):
            if the_finished_goal == self.stat_goal:
                self.free_stat_points += 1 #The player gets some new points to spend
                self.stat_goal_difficulty += 1 #Future goals become more difficult
                self.stat_goal = create_new_stat_goal(self.stat_goal_difficulty) #Generate a new goal

            elif the_finished_goal == self.work_goal:
                self.free_work_points += 1
                self.work_goal_difficulty += 1
                self.work_goal = create_new_work_goal(self.work_goal_difficulty)

            elif the_finished_goal == self.sex_goal:
                self.free_sex_points += 1
                self.sex_goal_difficulty += 1
                self.sex_goal = create_new_sex_goal(self.sex_goal_difficulty)

        def scrap_goal(self, the_finished_goal):
            if the_finished_goal == self.stat_goal:
                self.stat_goal = create_new_stat_goal(self.stat_goal_difficulty) #Generate a new goal

            elif the_finished_goal == self.work_goal:
                self.work_goal = create_new_work_goal(self.work_goal_difficulty)

            elif the_finished_goal == self.sex_goal:
                self.sex_goal = create_new_sex_goal(self.sex_goal_difficulty)

            self.scrap_goal_available = False

        def generate_goals(self):
            self.stat_goal = create_initial_stat_goal(self.stat_goal_difficulty)
            self.work_goal = create_initial_work_goal(self.work_goal_difficulty)
            self.sex_goal = create_initial_sex_goal(self.sex_goal_difficulty)

        def buy_point(self, stat_string, clarity_cost = 0):
            if stat_string == "stat":
                self.free_stat_points += 1

            elif stat_string == "work":
                self.free_work_points += 1

            elif stat_string == "sex":
                self.free_sex_points += 1

            self.clarity_purchase_level += 1
            self.spend_clarity(clarity_cost)

        def buy_point_cost(self):
            point_cost = __builtin__.int(50 * (2**(self.clarity_purchase_level/2.0)))
            return __builtin__.int(point_cost)

        def improve_stat(self, stat_string, amount = 1):
            if amount > self.free_stat_points:
                amount = self.free_stat_points
            if stat_string == "int":
                self.int += amount
            elif stat_string == "cha":
                self.charisma += amount
            elif stat_string == "foc":
                self.focus += amount

            self.free_stat_points += -amount

        def improve_work_skill(self, skill_string, amount = 1):
            if amount > self.free_work_points:
                amount = self.free_work_points

            if skill_string == "hr":
                self.hr_skill += amount
            elif skill_string == "market":
                self.market_skill += amount
            elif skill_string == "research":
                self.research_skill += amount
            elif skill_string == "production":
                self.production_skill += amount
            elif skill_string == "supply":
                self.supply_skill += amount

            self.free_work_points += -amount

        def improve_sex_skill(self, sex_string, amount = 1):
            if amount > self.free_sex_points:
                amount = self.free_sex_points

            if sex_string in self.sex_skills:
                self.sex_skills[sex_string] += amount
            elif sex_string == "stam":
                self.energy += amount * 20
                self.max_energy += amount * 20

            self.free_sex_points += -amount


        def log_event(self, the_text, the_text_style):
            if the_text is None: # Make sure we're not passing None items accidentally, which could cause crashes for the main hud.
                the_text = "???"
            if the_text_style is None:
                the_text_style = "float_text_grey"

            event_tuple = (the_text, the_text_style, time.time()) #Stores the unix time the event was added so we can run a little animation.
            self.log_items.insert(0,event_tuple)
            while len(self.log_items) > self.log_max_size:
                self.log_items.pop() #Pop off extra items until we are down to size.

        def start_text_convo(self, the_person): #Triggers all the appropriate variables so say entries will go into the phone text log.
            self.phone.register_number(the_person)
            self.having_text_conversation = the_person
            self.text_conversation_paused = False
            return

        def end_text_convo(self): #Resets all triggers from texting someone, so say messages are displayed properly again, ect.
            self.having_text_conversation = None
            self.text_conversation_paused = False
            return

        def pause_text_convo(self): #Keeps the phone UI and display up, but your dialogue and dialogue from any girl other than the one you're texting will display as normal and not be logged.
            self.text_conversation_paused = True #TODO: We no longer need to give characters a specific phone font, because it all goes right into the phone log itself. Otherwise this breaks the MC dialogue.
            return

        def resume_text_convo(self): #Start hiding the phone UI again. Use after you have paused a text convo
            self.text_conversation_paused = False
            return

        # def log_text_message(self, the_person, the_message):
        #     #TODO: Allow you to insert arbitrary messages by building history entries here! Use this for a narrator sytle "[Sent a picture]"!
        #     return

        def steal_underwear(self, the_person, the_item): #TODO: Add unit tests. TODO: Add ability to clear items out of the list. #TODO: Add ability to check if a similar item already exists in your collection.
            if not the_person.identifier in self.stolen_underwear:
                self.stolen_underwear[the_person.identifier] = []

            self.stolen_underwear[the_person.identifier].append(the_item)

        def get_underwear_list(self): #Returns a list of tuples. First item is the common display name "PERSON's ITEM", the second is the item reference itself #TODO: Add unit tests
            return_list = []
            for person_identifier in self.stolen_underwear:
                person = Person.get_person_by_identifier(person_identifier)
                for item in self.stolen_underwear[person_identifier]:
                    return_list.append([person.title + "'s " + item.display_name, item]) #TODO: Write the display code for this so it can show the little set of panties or bra with the correct colour/pattern. #TODO: might need an "empty" body type.

            return return_list
