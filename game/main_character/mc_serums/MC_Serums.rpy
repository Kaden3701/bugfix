# #This file organizes the serums for MC usage.
#
# init -1 python:
#     class MC_Serum():
#         def __init__(self):
#             self.stat_serums = []
#             self.other_serums = []     #Just in case?
#             self.ability_serums = []
#             self.max_serum_count = 0
#
#         def get_MC_serum_count(self):
#             return (__builtin__.len(self.stat_serums) + __builtin__.len(self.ability_serums) + __builtin__.len(self.other_serums))
#
#         def get_MC_serum_count_remaining(self):
#             return (self.max_serum_count - self.get_MC_serum_count())
#
#         def add_stat_serum(self, stat_serum):
#             if stat_serum not in self.stat_serums:
#                 self.stat_serums.append(stat_serum)
#
#         def add_ability_serum(self, ability_serum):
#             if ability_serum not in self.ability_serums:
#                 self.ability_serums.append(ability_serum)
#
#         def apply_serum(self):
#             return
#
#
#
#     class MC_serum_effect():
#         def __init__(self, perk, name, perk_type, linked_serum_trait, perk_cat):
#             self.perk = perk
#             self.name = name
#             self.perk_type = perk_type
#             self.linked_serum_trait = linked_serum_trait
#             self.perk_cat = perk_cat  #This determines which category to put the perk in.
#
#         def apply_serum(self):
#             if perk_type == "Stat":
#                 perk_system.add_stat_perk(self.perk, self.name)
#             elif perk_type == "Ability":
#                 perk_system.add_ability_perk(self.perk, self.name)
#
#         def check_serum_avail(self): #Determine if trait SHOULD be available
#             if self.linked_serum_trait.side_effect_chance < 5:
#                 return True
#             return False
#
#         def check_link_serum_avail(self):  #Determine if trait shows as more research required.
#             if self.linked_serum_trait.researched:
#                 if not self.check_serum_avail():
#                     return True
#             return False
#
#
#     MC_Serum_effect_list = []  #TODO move this to an init possibly?
#
#     def get_avail_MC_serum_by_cat(perk_cat):
#         return_list = []
#         for perk in MC_Serum_effect_list:
#             if perk.perk_cat == perk_cat:
#                 if perk.check_serum_avail():
#                     return_list.append(perk_cat)
#         return return_list
#
#     def get_avail_MC_serum_link_unlock_by_cat(perk_cat):
#         return_list = []
#         for perk in MC_Serum_effect_list:
#             if perk.perk_cat == perk_cat:
#                 if perk.check_link_serum_avail():
#                     return_list.append(perk_cat)
#         return return_list
#
#     def get_avail_MC_serums():
#         return_list = []
#         for perk in MC_Serum_effect_list:
#             if perk.check_serum_avail():
#                 return_list.append(perk_cat)
#         return return_list
