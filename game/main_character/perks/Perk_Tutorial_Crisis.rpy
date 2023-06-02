init -1 python:
    def Perk_Tutorial_Crisis_requirement():
        if mc.is_in_bed and day % 7 != 4: # not on Friday
            if mc.energy < mc.max_energy * .4:
                return True
        return False


label Perk_Tutorial_Crisis_label():
    $ mc.change_location(bedroom)
    $ the_person = mom
    $ scene_manager = Scene()
    $ mc.business.event_triggers_dict["perk_tutorial"] = 1
    "You are worn out after a long hard day. You collapse into your bed and are rapidly falling asleep when a knock on your door awakens you."
    mc.name "Wha? Come in?"
    $ scene_manager.add_actor(the_person)
    the_person "Hey honey... I'm sorry to bug you, but I was wondering if you could come help with something really quick!"
    mc.name "Seriously? Right now?"
    the_person "I'm sorry, I know you're tired, but it'll just be a moment I promise!"
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "You aren't sure you can get up. You try to dig deep so you can help [the_person.title] in her time of need."
    $ scene_manager.hide_actor(the_person)
    $ perk_system.add_ability_perk(Ability_Perk(description = "You dig deep and summon reserves of energy to meet the needs of others. Recovers 100 energy, usable once per week.", active = False, usable = True, usable_func = time_of_need_func, usable_cd = 7), "Time of Need")
    "You have gained the Perk: Time of Need!"
    while mc.energy < mc.max_energy * .4:
        "Open the 'Perk Sheet' screen (top left UI) and click on the 'Time of Need' perk to continue."
    $ mc.change_location(hall)
    $ scene_manager.show_actor(the_person, position = the_person.idle_pose)
    "You get up and follow your mom to the living room."
    the_person "Thank you! I just had this overwhelming urge to move some furniture around. You know how it is, once you get the urge it's hard to put it off..."
    "You help [the_person.possessive_title] move her furniture around. She seems extremely grateful."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    $ the_person.change_stats(happiness = 5, love = 3)
    the_person "Thank you! This means a lot to me!"
    $ mc.change_location(bedroom)
    $ scene_manager.clear_scene()
    "You say goodnight and then head back to bed."

    return
