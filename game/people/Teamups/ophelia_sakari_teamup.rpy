#Notes: I want to use a seperate file from now on for contain all teamup code and dialogue.
#Erica and other files are getting TOO LONG and need to be paired down accordingly
#Sakari's planned teamups are with Ophelia and eventually someone in MC's family.
#Jennifer would be ideal, with Sakari offering her a job at the clothes store. However, unsure of how things will progress with vanilla Jennifer
# Rebecca makes sense and also already has a teamup planned for rebecca and ophelia, making the three of them a prime harem start possibility.

#Sakari's ophelia teamup should start right after her skinny dipping scene and before her blowjob scene, and somewhere around her 40 love scene. Implications are that ophelia gives her some blowjob tips.
#Ophelia needs to have progress her salon to the point of offering massage services. Sakari teaming up with her slows her weekly energy loss by going to the spa.
# Rebecca's teamup should only occur if Sakari is cured. Rebecca is shopping at the store and MC sees her, introduces her to the shop owner, they become friends.

#Requirement functions
init -2 python:
    pass

# Actions
init 3 python:
    pass

#Story Labels










#Story wrappers
init 3 python:
    def sakari_ophelia_teamup_started():
        return sakari.event_triggers_dict.get("ophelia_teamup_started", False)

    def sakari_ophelia_teamup_active():
        return sakari.event_triggers_dict.get("opehlia_teamup", False)

    def sakari_rebecca_teamup_started():
        return sakari.event_triggers_dict.get("rebecca_teamup_started", False)

    def sakari_rebecca_teamup_active():
        return sakari.event_triggers_dict.get("rebecca_teamup", False)
