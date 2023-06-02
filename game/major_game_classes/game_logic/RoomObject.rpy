init -2 python:
    class RoomObject(): #Contains a list of traits for the object which decides how it can be used. #TODO: We need to rename this, this is just asking for a major namespace collision
        def __init__(self, name, traits, sluttiness_modifier = 0, obedience_modifier = 0):
            self.name = name
            if isinstance(traits, list):
                self.traits = traits
            elif traits is None:
                traits = []
            else:
                self.traits = [traits]
            self.sluttiness_modifier = sluttiness_modifier #Changes a girls sluttiness when this object is used in a sex scene
            self.obedience_modifier = obedience_modifier #Changes a girls obedience when this object is used in a sex scene.

        def __cmp__(self, other):
            if other is None:
                return -1
            if isinstance(self, other.__class__):
                if self.name == other.name:
                    return 0

            if self.__hash__() < other.__hash__(): #Use hash values to break ties.
                return -1
            else:
                return 1

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, other):
            if isinstance(self, other.__class__):
                return self.name == other.name
            return False

        def __ne__(self, other):
            if isinstance(self, other.__class__):
                return self.name != other.name
            return True

        def has_trait(self,the_trait):
            for trait in self.traits:
                if trait == the_trait:
                    return True
            return False

        @property
        def formatted_name(self):
            if self.sluttiness_modifier == 0 and self.obedience_modifier == 0:
                return self.name

            the_string = self.name + "\n{color=#ff0000}{size=18}"
            if self.sluttiness_modifier != 0 or self.obedience_modifier != 0:
                the_string += "Temporary Modifiers\n"

            if self.sluttiness_modifier < 0:
                the_string += str(self.sluttiness_modifier) + " Sluttiness"
                if not self.obedience_modifier == 0:
                    the_string += ", "
            if self.sluttiness_modifier > 0:
                the_string += "+" + str(self.sluttiness_modifier) + " Sluttiness"
                if not self.obedience_modifier == 0:
                    the_string += ", "

            if self.obedience_modifier < 0:
                the_string += str(self.obedience_modifier) + " Obedience"

            if self.obedience_modifier >0:
                the_string += "+" + str(self.obedience_modifier) + " Obedience"

            the_string += "{/size}{/color} (tooltip)The object you have sex on influences how enthusiastic and obedient a girl will be."
            return the_string
