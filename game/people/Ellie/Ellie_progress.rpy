init 10 python:
    def ellie_story_character_description():
        return "Fired from her previous job and desperate for work, you hired [ellie.name] to be your IT lead."

    def ellie_story_love_list():
        love_story_list = {}
        if not ellie_has_been_fingered():
            love_story_list[0] = "Advance her sluttiness story to continue this story."
            return love_story_list
        if not ellie_has_given_handjob():
            if ellie.love < 20:
                love_story_list[0] = "Increase [ellie.name]'s love to continue this story."
            else:
                love_story_list[0] = "[ellie.name] may surprise you at work soon."
            return love_story_list
        else:
            love_story_list[0] = "[ellie.name] returned the sexual favor with her first handjob!"

        if not ellie_has_brought_lunch_date():
            if ellie.love < 40:
                love_story_list[1] = "Increase [ellie.name]'s love to continue this story."
            else:
                love_story_list[1] = "Work in the morning and [ellie.name] maybe surprise you with a meal."
            return love_story_list
        else:
            love_story_list[1] = "[ellie.name] surprised you at work with a delicious home cooked meal."
            if ellie_has_given_blowjob():
                love_story_list[2] = "You made her cum while eating her out in your office."

        love_story_list[3] = "There is nothing more in this story line at this time."
        return love_story_list

    def ellie_story_lust_list():
        lust_story_list = {}
        if not ellie_has_been_fingered():
            if ellie.sluttiness < 20:
                lust_story_list[0] = "Trying increasing her sluttiness to continue this story."
            else:
                lust_story_list[0] = "Try working while she is working on a nanobot program to continue this story."
            return lust_story_list
        else:
            lust_story_list[0] = "Gave [ellie.name] her first orgasm with your fingers in her office!"

        if not ellie_has_given_handjob():   #Requires love story progress
            lust_story_list[1] = "Try progressing [ellie.name]'s love story to continue this story."
            return lust_story_list
        elif not ellie_has_given_blowjob(): #40 sluttiness event
            if ellie.sluttiness < 40:
                lust_story_list[1] = "Trying increasing her sluttiness to continue this story."
            elif not get_random_employees(1, exclude_list = [ellie], slut_required = 50):
                lust_story_list[1] = "[ellie.name] doesn't know anyone she can confide her desires in. Raise another employee's sluttiness to at least 50."
            else:
                lust_story_list[1] = "You may overhear a conversation [ellie.name] is having at work soon..."
            return lust_story_list
        else:
            lust_story_list[1] = "[ellie.name] gave you her first blowjob after you overheard her asking a coworker about oral sex!"

        lust_story_list[2] = "There is nothing more in this story line at this time."

        return lust_story_list

    def ellie_story_teamup_list():
        return {}

    def ellie_story_other_list():
        other_info_list = {}
        if ellie.days_employed > 0:
            other_info_list[0] = "[ellie.name] is thankful you hired her, despite blackmailing you."
        if ellie_is_a_squirter():
            other_info_list[1] = "[ellie.name] has extremely wet orgasms!"
        # other_info_list.append("[ellie.name] is not yet willing to go all the way with you. Try advancing her story.")
        return other_info_list
