# Use this file to hold information relating to Sakari's story progress and hint system.

init 10 python:
    def sakari_story_character_description():
        return "A native woman who had an affair with your dad and whose daughter, [kaya.name], is your half sister."

    def sakari_story_love_list():
        love_story_list = {
            0 : "There is nothing more in this story line at this time."
        }
        return love_story_list

    def sakari_story_lust_list():
        lust_story_list = {
            0: "There is nothing more in this story line at this time."
        }
        return lust_story_list

    def sakari_story_teamup_list():
        return {
            0: [kaya, "Hmm, [kaya.name] is [sakari.name]'s daughter... surely nothing could happen there... right?'"]
        }

    def sakari_story_other_list():
        return {
            0: "[sakari.title] has started working at the clothing store again. Look for her there in the morning."
        }
