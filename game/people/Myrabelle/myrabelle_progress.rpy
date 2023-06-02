init 10 python:
    def myrabelle_story_character_description():
        return "An aspiring professional gamer and owner of the Gaming Cafe at the mall."

    def myrabelle_story_love_list():
        love_story_list = {}
        love_story_list[0] = "[myra.name] has opened a gaming cafe at the mall. Play games there to restore energy."
        if not myra_will_grind_with_mc():
            love_story_list[1] = "Get your character to at least level 30 to play Guild Quest 2 with [myra.name]."
        else:
            love_story_list[1] = "[myra.name] enjoys playing Guild Quest 2 with you."

        if myra_plays_esports():
            love_story_list[2] = "You learned she is a part of an esports team."
        elif myra.love < 20:
            love_story_list[2] = "Increase [myra.name]'s love to learn more about her."
            return love_story_list
        else:
            love_story_list[2] = "Swing by the gaming cafe to learn more about [myra.name]."
            return love_story_list

        if myra_has_failed_tournament():
            love_story_list[3] = "However, [myra.name] lost her first esports tournament, badly."
        elif myra.love < 40:
            love_story_list[3] = "Increase [myra.name]'s love to learn more about her."
            return love_story_list
        else:
            love_story_list[3] = "[myra.name]'s first tournament is on a Sunday."
            return love_story_list

        if myra_can_sponsor():
            love_story_list[4] = "She lost a major sponsor as a result."
        elif myra.love < 60:
            love_story_list[4] = "Increase [myra.name]'s love to progress her story."
            return love_story_list
        else:
            love_story_list[4] = "Stop by the cafe in the evening to learn the repercussions of her loss."
            return love_story_list

        if myra_has_been_sponsored():
            love_story_list[5] = "You stepped up and sponsored her esports team yourself."
        if not mc.business.has_funds(25000):
            love_story_list[5] = "You need more money to step up and sponsor her yourself."
            return love_story_list
        else:
            love_story_list[5] = "Talk to [myra.name] about sponsoring her team yourself."
            return love_story_list

        love_story_list[6] = "This is the end of content in this version. Everything after this in her love story is just outlining."
        if myra.love < 80:
            love_story_list[7] = "Increase [myra.name]'s love to progress her story."
            return love_story_list
        elif myra_focus_progression_scene.get_stage() < 2:
            love_story_list[7] = "Help [myra.name] train her focus to advance her story."
            return love_story_list
        elif not myra_has_won_tournament():
            love_story_list[7] = "Talk to [myra.name] about setting up a new tournament. She is ready!"
            return love_story_list

        if myra_has_won_tournament():
            love_story_list[8] = "[myra.name] hosted her own tournament and placed third! A huge improvement!"
        if myra_is_expanding_business():
            love_story_list[8] = "She has used her winnings to begin expanding her business!"
        elif myra.love < 95:
            love_story_list[8] = "Increase [myra.name]'s love to progress her story."
            return love_story_list
        else:
            love_story_list[8] = "Talk to [myra.name] about her winnings."
            return love_story_list


        love_story_list[9] = "There is nothing more in this story line at this time."
        return love_story_list

    def myrabelle_story_lust_list():
        lust_story_list = {}
        if myra_distracts_gamers():
            lust_story_list[0] = "[myra.name] likes to use dirty language and double entendres to distract gaming opponents."
        elif myra.sluttiness < 20:
            lust_story_list[0] = "Raise [myra.name]'s sluttiness to advance this story."
            return lust_story_list
        else:
            lust_story_list[0] = "Swing by the gaming cafe during business hours to advance this story."
            return lust_story_list

        if myra_caught_masturbating():
            lust_story_list[1] = "[myra.name] enjoys sexual video games. You caught her masturbating to one."
        elif myra.sluttiness < 40:
            lust_story_list[1] = "Raise [myra.name]'s sluttiness to advance this story."
            return lust_story_list
        else:
            lust_story_list[1] = "Swing by the gaming cafe during the evening to advance this story."
            return lust_story_list

        if myra_lewd_game_fuck_avail():
            lust_story_list[2] = "[myra.name] enjoys fucking you while acting out positions from a sexual PC game. She is willing every evening at the gaming cafe."
        elif myra.sluttiness < 60:
            lust_story_list[2] = "Raise [myra.name]'s sluttiness to advance this story."
            return lust_story_list
        elif myra.has_taboo("vaginal_sex"):
            lust_story_list[2] = "Fuck [myra.name] to advance this story."
            return lust_story_list
        else:
            lust_story_list[2] = "Swing by the gaming cafe during the evening to advance this story."
            return lust_story_list

        if myra_lewd_cafe_open():
            lust_story_list[3] = "She has opened an adults only VIP section at the gaming cafe for sexual PC games."
        elif myra.sluttiness < 80:
            lust_story_list[3] = "Raise [myra.name]'s sluttiness to advance this story."
            return lust_story_list
        elif not myra_is_expanding_business():
            lust_story_list[3] = "Advance [myra.name]'s love story before advancing this story."
            return lust_story_list


        lust_story_list[4] = "There is nothing more in this story line at this time."

        return lust_story_list

    def myrabelle_story_teamup_list():
        teamup_story_list = {}

        #Alexia
        if myra_alexia_teamup_scene.get_stage() == -1:
            teamup_story_list[0] = [alexia, "[alexia.name] is her good friend. Maybe there will be an opportunity here someday"]
        elif myra_alexia_teamup_scene.get_stage() == 0:
            teamup_story_list[0] = [alexia, "[alexia.name] meets with her every Friday night. You can rub their backs if you join them."]
        elif myra_alexia_teamup_scene.get_stage() == 1:
            teamup_story_list[0] = [alexia, "[alexia.name] and [myra.name] compete for you to finger them on Friday nights."]
        elif myra_alexia_teamup_scene.get_stage() == 2:
            teamup_story_list[0] = [alexia, "[alexia.name] and [myra.name] compete for you to eat them out on Friday nights."]
        elif myra_alexia_teamup_scene.get_stage() == 3:
            teamup_story_list[0] = [alexia, "[alexia.name] and [myra.name] compete for you to fuck them on Friday nights."]
        elif myra_alexia_teamup_scene.get_stage() == 3:
            teamup_story_list[0] = [alexia, "[alexia.name] and [myra.name] have a friendly gaming night that always ends in a threesome on Friday nights."]
        return teamup_story_list

    def myrabelle_story_other_list():
        other_info_list = {}
        if myra_focus_progression_scene.get_stage() >= 0:
            other_info_list[0] = "You can help [myra.name] train her focus to get better at gaming in distracting situations."
            if myra_focus_progression_scene.get_stage() == 0:
                other_info_list[1] = "You distract her with back rubs during training. Raise her sluttiness to take distractions further."
            elif myra_focus_progression_scene.get_stage() == 1:
                other_info_list[1] = "You distract her by groping her tits during training. Raise her sluttiness to take distractions further."
            elif myra_focus_progression_scene.get_stage() == 2:
                other_info_list[1] = "You distract her by fingering her during training. Raise her sluttiness to take distractions further."
            elif myra_focus_progression_scene.get_stage() == 3:
                other_info_list[1] = "You distract her by getting a lap dance during training. Raise her sluttiness to take distractions further."
            elif myra_focus_progression_scene.get_stage() == 4:
                other_info_list[1] = "You distract her by fucking her ass during training."
        if myra_can_distribute_serum():
            other_info_list[2] = "Every Wednesday, you can send company energy drinks to [myra.name] for distribution."
        if myra_wants_bigger_tits() and not myra.has_large_tits:
            other_info_list[3] = "[myra.name] has asked for help growing bigger tits."
        elif myra.has_large_tits and myra_wants_bigger_tits():
            other_info_list[3] = "[myra.name] is thankful you helped her grow her tits."
        if myra_finish_blowjob_training():
            other_info_list[4] = "You helped train [myra.name] how to give amazing head."
        elif myra_started_blowjob_training():
            other_info_list[4] = "You are training [myra.name] how to give better head. Check back with her weekly."
        else:
            other_info_list[4] = "[myra.name] hates giving head. You should look for some way to show her oral skills are important."
        if myra_lewd_cafe_open():
            other_info_list[5] = "[myra.name] has opened an adults only section to the gaming cafe!"

        return other_info_list
