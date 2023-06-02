init -1 python:
    class Perks():
        def __init__(self):
            self.stat_perks = {}
            self.item_perks = {}
            self.ability_perks = {}

        def update(self):  #By adding an update, we can add temporary perks that may expire.
            def expired_perks(perk_dict):
                perk_names = []
                for key, item in perk_dict.items():
                    if item.bonus_is_temp and day >= item.duration + item.start_day:
                        perk_names.append(key)
                return perk_names

            for perk_name in expired_perks(self.stat_perks):
                self.remove_perk(perk_name)

            for perk_name in expired_perks(self.item_perks):
                self.remove_perk(perk_name)

            for perk_name in expired_perks(self.ability_perks):
                self.remove_perk(perk_name)

            for perk_name in self.ability_perks:
                self.ability_perks[perk_name].update()
            return

        def remove_perk(self, perk_name):
            if perk_name in self.stat_perks:
                self.stat_perks[perk_name].remove()
                self.stat_perks.pop(perk_name)
            if perk_name in self.item_perks:
                self.item_perks[perk_name].remove()
                self.item_perks.pop(perk_name)
            if perk_name in self.ability_perks:
                self.ability_perks[perk_name].remove()
                self.ability_perks.pop(perk_name)
            return

        def save_load(self):
            for perk in self.stat_perks:
                if self.stat_perks[perk].save_load:
                    self.stat_perks[perk].save_load()
            for perk in self.item_perks:
                if self.item_perks[perk].save_load:
                    self.item_perks[perk].save_load()
            for perk in self.ability_perks:
                if self.ability_perks[perk].save_load:
                    self.ability_perks[perk].save_load()
            return

        def get_perk_desc(self, perk_name):
            if self.has_stat_perk(perk_name):
                return self.stat_perks[perk_name].description
            elif self.has_item_perk(perk_name):
                return self.item_perks[perk_name].description
            elif self.has_ability_perk(perk_name):
                return self.ability_perks[perk_name].description
            return "None"

        def add_stat_perk(self, perk, perk_name):
            if self.has_stat_perk(perk_name):
                #We already have this perk, check if we need to update temporary bonus.
                if not perk.bonus_is_temp:
                    return

                # Update duration for existing temporary perk.
                comp_perk = self.get_stat_perk(perk_name)
                if comp_perk.duration < perk.duration:
                    comp_perk.duration = perk.duration
                if comp_perk.start_day < perk.start_day:
                    comp_perk.start_day = perk.start_day
            else:
                perk.apply()
                self.stat_perks[perk_name] = perk
            return

        def has_stat_perk(self, perk_name):
            if perk_name in self.stat_perks:
                return True
            return False

        def get_stat_perk(self, perk_name):
            if self.has_stat_perk(perk_name):
                return self.stat_perks[perk_name]
            return None

        def add_item_perk(self, perk, perk_name):
            if not self.has_item_perk(perk_name):
                self.item_perks[perk_name] = perk
                if perk.on_unlock:
                    perk.on_unlock()

        def has_item_perk(self, perk_name):
            if perk_name in self.item_perks:
                return True
            return False

        def get_item_perk(self, perk_name):
            if self.has_item_perk(perk_name):
                return self.item_perks[perk_name]
            return None

        def add_ability_perk(self, perk, perk_name):
            if self.has_ability_perk(perk_name):
                if not perk.bonus_is_temp:
                    return

                comp_perk = self.get_ability_perk(perk_name)
                if comp_perk.duration < perk.duration:
                    comp_perk.duration = perk.duration
                if comp_perk.start_day < perk.start_day:
                    comp_perk.start_day = perk.start_day
            else:
                self.ability_perks[perk_name] = perk

        def has_ability_perk(self, perk_name):  #Only checks if the ability is available at all
            if perk_name in self.ability_perks:
                return True
            return False

        def get_ability_perk(self, perk_name):
            if self.has_ability_perk(perk_name):
                return self.ability_perks[perk_name]
            return False

        def get_ability_flag(self, perk_name):  #Returns if ability is unlocked, and if so, if it is toggled on
            if self.has_ability_perk(perk_name):
                if self.ability_perks[perk_name].togglable:
                    return self.ability_perks[perk_name].active
                return True
            return False

        def get_ability_clickable(self, perk_name):  #Returns true if perk should be available for clicking in screen
            if self.has_ability_perk(perk_name):
                if self.ability_perks[perk_name].togglable:
                    return True
                if self.ability_perks[perk_name].usable:
                    if self.ability_perks[perk_name].usable_day <= day:
                        return True
                return False
            return False

        def click_ability(self, perk_name):
            if self.has_ability_perk(perk_name):
                self.ability_perks[perk_name].click_perk()
            return

        def get_stat_perk_list(self):  #This function returns a list of all three perk lists.
            return self.stat_perks

        def get_item_perk_list(self):
            return self.item_perks

        def get_ability_perk_list(self):
            return self.ability_perks

        def get_ability_perk_text_desc(self, perk_name):
            ret_text = perk_name
            if self.has_ability_perk(perk_name):
                if self.ability_perks[perk_name].togglable:
                    if self.ability_perks[perk_name].active:
                        ret_text += " (active)"
                    else:
                        ret_text += " (inactive)"
                if self.ability_perks[perk_name].usable:
                    if self.ability_perks[perk_name].usable_day > day:
                        ret_text += " (On Cooldown)"
            return ret_text

        def perk_on_cum(self, the_person = None, the_place = None, add_to_log = True):
            for perk_name in self.ability_perks:
                self.ability_perks[perk_name].on_cum(the_person, the_place, add_to_log)

    class Stat_Perk():
        # owner can be MC or any other Person object (default is MC)
        # when owner is Person object we can add temporary stats without using a serum
        def __init__(self, description, owner = None, cha_bonus = 0, int_bonus = 0, foc_bonus = 0,
            hr_bonus = 0, market_bonus = 0, research_bonus = 0, production_bonus = 0, supply_bonus = 0,
            foreplay_bonus = 0, oral_bonus = 0, vaginal_bonus = 0, anal_bonus = 0, energy_bonus = 0,
            stat_cap = 0, skill_cap = 0, sex_cap = 0, energy_cap = 0,
            bonus_is_temp = False, duration = 0, save_load = None):

            self.owner = owner
            self.description = description
            self.cha_bonus = cha_bonus
            self.int_bonus = int_bonus
            self.foc_bonus = foc_bonus
            self.hr_bonus = hr_bonus
            self.market_bonus = market_bonus
            self.research_bonus = research_bonus
            self.production_bonus = production_bonus
            self.supply_bonus = supply_bonus
            self.foreplay_bonus = foreplay_bonus
            self.oral_bonus = oral_bonus
            self.vaginal_bonus = vaginal_bonus
            self.anal_bonus = anal_bonus
            self.energy_bonus = energy_bonus
            self.stat_cap = stat_cap
            self.skill_cap = skill_cap
            self.sex_cap = sex_cap
            self.energy_cap = energy_cap
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            self.start_day = day
            self.save_load = save_load

            if self.owner is None:
                self.owner = mc
            if description is None:
                self.description = ""


        def apply(self):
            self.owner.charisma += self.cha_bonus
            self.owner.int += self.int_bonus
            self.owner.focus += self.foc_bonus
            self.owner.hr_skill += self.hr_bonus
            self.owner.market_skill += self.market_bonus
            self.owner.research_skill += self.research_bonus
            self.owner.production_skill += self.production_bonus
            self.owner.supply_skill += self.supply_bonus
            self.owner.sex_skills["Foreplay"] += self.foreplay_bonus
            self.owner.sex_skills["Oral"] += self.oral_bonus
            self.owner.sex_skills["Vaginal"] += self.vaginal_bonus
            self.owner.sex_skills["Anal"] += self.anal_bonus
            self.owner.max_energy += self.energy_bonus
            if isinstance(self.owner, MainCharacter):
                self.owner.max_stats += self.stat_cap
                self.owner.max_work_skills += self.skill_cap
                self.owner.max_sex_skills += self.sex_cap
                self.owner.max_energy_cap += self.energy_cap
            return

        def remove(self):
            self.owner.charisma -= self.cha_bonus
            self.owner.int -= self.int_bonus
            self.owner.focus -= self.foc_bonus
            self.owner.hr_skill -= self.hr_bonus
            self.owner.market_skill -= self.market_bonus
            self.owner.research_skill -= self.research_bonus
            self.owner.production_skill -= self.production_bonus
            self.owner.supply_skill -= self.supply_bonus
            self.owner.sex_skills["Foreplay"] -= self.foreplay_bonus
            self.owner.sex_skills["Oral"] -= self.oral_bonus
            self.owner.sex_skills["Vaginal"] -= self.vaginal_bonus
            self.owner.sex_skills["Anal"] -= self.anal_bonus
            self.owner.max_energy -= self.energy_bonus
            # make sure energy is not > max energy
            if self.owner.energy > self.owner.max_energy:
                self.owner.energy = self.owner.max_energy

            if isinstance(self.owner, MainCharacter):
                self.owner.max_stats -= self.stat_cap
                self.owner.max_work_skills -= self.skill_cap
                self.owner.max_sex_skills -= self.sex_cap
                self.owner.max_energy_cap -= self.energy_cap
            return

    class Item_Perk():
        # owner can be MC or any other Person object (default is MC)
        def __init__(self, description, owner = None, usable = False, bonus_is_temp = False, duration = 0, on_unlock = None, save_load = None):
            self.owner = owner
            self.description = description
            self.usable = usable
            self.bonus_is_temp = bonus_is_temp
            self.duration = duration
            #self.start_day = day
            self.start_day = 0  #Consider getting rid of this. Is it necessary?
            self.on_unlock = on_unlock
            self.save_load = save_load

            if self.owner is None:
                self.owner = mc

    class Ability_Perk():
        def __init__(self, description, owner = None, active = True, togglable = False, usable = False, bonus_is_temp = False, duration = 0, usable_func = None, usable_cd = 0, update_func = None, save_load = None, cum_func = None):
            self.owner = owner
            self.description = description
            self.usable = usable            #Is this a usable ability
            self.usable_func = usable_func  #What to do if ability is used
            self.usable_cd = usable_cd      #How long to wait after this ability to use it again.
            self.togglable = togglable     #Can you toggle this ability
            self.active = active            #Is this ability currently active
            self.bonus_is_temp = bonus_is_temp   #Should we take away this ability
            self.duration = duration
            self.start_day = day
            self.usable_day = 0
            self.save_load = save_load
            self.update_func = update_func
            self.cum_func = cum_func

            if self.owner is None:
                self.owner = mc


        def click_perk(self):
            if self.usable:
                self.activate_perk()
            if self.togglable:
                self.toggle_perk()
            return

        def activate_perk(self):
            if self.usable and self.usable_day <= day:
                self.usable_func()
                self.usable_day = day + self.usable_cd
                return True
            return False

        def toggle_perk(self):
            if self.togglable:
                self.active = not self.active
            return

        def update(self):
            if hasattr(self, "update_func"):
                if self.update_func is not None and self.active:
                    self.update_func()
            return

        def remove(self):
            pass
            return

        def on_cum(self, the_person = None, the_place = None, add_to_log = True):
            if hasattr(self, "cum_func"):
                if self.cum_func is not None and self.active:
                    self.cum_func(the_person, the_place, add_to_log)
            return

    def second_wind_func():
        mc.change_energy(mc.max_energy / 2)
        #renpy.say(None,"You take a deep breath, getting your second wind. You recover some energy!") #TODO this doesn't work. probably just delete
        return

    def time_of_need_func():
        mc.change_energy(max(100, (mc.max_energy * .5)))

        return
