init 10 python:
    #Prototypes for an easier way of managing story progress screens. Add an init function to attempt to retain global functionaliy

    def candace_story_love_list():
        love_story_list = {}

        if candace.event_triggers_dict.get("quit_job", 0) != 0:
            love_story_list[0] = "Keep working on [candace.fname] to quit her current job."
            return love_story_list

        love_story_list[0] = "You managed to hire [candace.fname] and convinced her to dump her boyfriend"

        if candace.love < 20:
            love_story_list[1] = "Increase [candace.fname]'s love to 20"
        if not candace.story_event_ready("love"):
            love_story_list[1] = "[candace.fname] needs time before she is ready to progress this story"
        if not candace.is_at_work:
            love_story_list[1] = "Talk to [candace.fname] at when she is working."

        if not candace.event_triggers_dict.get("clothes_shopping", 0) != 0:
            return love_story_list

        love_story_list[1] = "You went clothes shopping with [candace.fname]. You can invite other girls to go with you from the store anytime."
        love_story_list[2] = "This event is not yet written."
        return love_story_list

    def candace_story_lust_list():
        lust_story_list = {}

        if candace.sluttiness < 40:
            lust_story_list[0] = "Increase [candace.fname]'s sluttiness to 40"
        if not candace.story_event_ready("lust"):
            lust_story_list[0] = "[candace.fname] needs time before she is ready to progress this story"
        else:
            lust_story_list[0] = "Check up on [candace.fname] at work in the afternoon or evening"

        if not candace.event_triggers_dict.get("supply_discount", False):
            lust_story_list[0] = "Check up with [candace.fname] and see how it went with the supplier."
            return lust_story_list

        lust_story_list[0] = "You convinced [candace.fname] to accept discounts from supply venders!"
        lust_story_list[1] = "The next step has not yet been written"

        return lust_story_list

    def candace_story_obedience_list():
        obedience_story_list = {
            0: "This event is not yet written."

        }
        return obedience_story_list

    def candace_story_teamup_list():
        return {
            0 : [salon_manager, "This teamup is not yet written"],
            1 : [sarah, "This teamup is not yet written"],
            2 : [starbuck, "This teamup is not yet written"]
        }

    def candace_story_other_list():
        #candace's other story indices:
        # 0 - Her relationship with her boyfriend
        # 1 - Your karaoke skill level
        # 2 - Her bimbo status

        other_story_list = {}
        other_story_list[0] = "She is currently in a relationship"

        if candace.event_triggers_dict.get("quit_job", 0) != 0:
            other_story_list[0] = "You managed to break up [candace.fname]'s relationship with her abusive ex"

        # candace.other_messages[1] = "Your skill level at karaoke is "+ karaoke_skill + " / 20"
        return other_story_list
