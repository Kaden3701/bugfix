init -2 python:
    class SerumInventory(): #A bag class that lets businesses and people hold onto different types of serums, and move them around.
        def __init__(self,starting_list = None):
            if starting_list is None:
                self.serums_held = []
            else:
                self.serums_held = starting_list ##Starting list is a list of tuples, going [SerumDesign,count]. Count should be possitive.

        @property
        def total_serum_count(self):
            return sum(x[1] for x in self.serums_held)

        def get_serum_count(self, serum_design):
            return sum(x[1] for x in self.serums_held if x[0].is_same_design(serum_design))

        def get_matching_serum_count(self, check_function): #Hand a function to the inventory and get a count of the number of serums that match that requirement.
            return sum(self.get_serum_count(x) for x in self.get_serum_types if check_function(x))

        @property
        def get_serum_types(self): ## returns a list of all the serum types that are in the inventory, without their counts.
            return list(set(x[0] for x in self.serums_held))

        @property
        def get_max_serum_count(self): #Returns the count of the highest group of serums you have available.
            if not self.get_serum_types:
                return 0
            return max(self.get_serum_count(x) for x in self.get_serum_types)

        def change_serum(self, serum_design, change_amount): ##Serum count must be greater than 0. Adds to stockpile of serum_design if it is already there, creates it otherwise.
            found = False
            remove_list = []
            for design in self.serums_held:
                if design[0].is_same_design(serum_design) and not found:
                    design[1] += __builtin__.int(change_amount)
                    found = True
                    if design[1] <= 0:
                        remove_list.append(design)

            if remove_list: #Avoid removing items while we traverse the list
                for design in remove_list:
                    self.serums_held.remove(design)

            if not found:
                if change_amount > 0:
                    self.serums_held.append([serum_design, __builtin__.int(change_amount)])

        def has_serum_with_trait(self, trait):
            return any(x for x in self.get_serum_types if x.has_trait(trait))

        def get_serums_with_trait(self, trait):
            return [x for x in self.get_serum_types if x.has_trait(trait)]
