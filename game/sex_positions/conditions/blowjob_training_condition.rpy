#Use this for fucking an employee while working.


init -1 python:
    def condition_blowjob_training_reward_req(self, the_person, report_log):
        if report_log.get("guy orgasms", 0) > 0:   #She finished off MC
            return True
        return False


    def make_condition_blowjob_training():
        blowjob_training_whitelist = [blowjob, deepthroat, skull_fuck]
        blowjob_training_condition = Condition_Type("Blowjob Training", pre_label = "condition_blowjob_training_pre_label", post_label = "condition_blowjob_training_post_label", position_whitelist = blowjob_training_whitelist,
            reward_cond = condition_blowjob_training_reward_req, reward_label = "condition_blowjob_training_reward_label")
        return blowjob_training_condition

    blowjob_training_condition_blowjob_list = [
    "I know you've never done this much before. It's okay. You're doing great. The hottest part is just getting on your knees and trying. Now look up at me and open up.",
    "You're doing fine. Trying tilting your head up and looking at me while you lick the tip.",
    "If you need a break, like your way down and suck on my balls while you stroke it some.",
    "You are doing good, but there is room for improvement. Use your hand to help stroke as you suck on it.",
    "That feels great, but don't let yourself get into too much of a rhythm. Mix it up a bit, maybe just use your tongue for a couple strokes.",
    "Damn, you have a pretty good technique. Keep doing what you are doing, but look up at me. I want you to see how good it feels.",
    "That's it. Make love to my cock with your mouth. A good slut is always ready to do whatever it takes to please her man.",
    "Fuck, where'd you learn to suck dick like that? Keep going, it feels amazing.",
    "Fuck, that feels amazing. Just keep going, I love that hot little mouth of yours."]

    blowjob_training_condition_deepthroat_list = [
    "It's okay. I know it feels uncomfortable, but this takes practice. You'll be deepthroating like a pro in no time.",
    "Try to relax. I know it feels wrong, but you can ease the gag reflex with practice.",
    "Close your eyes, relax your throat. Take it nice and slow. You can take the whole thing, just keep practicing.",
    "Try leaning your head back and looking up at me. That lines up your throat and makes it easier to go deep.",
    "You're doing good. Next time it goes deep, try using your tongue at the base.",
    "Damn you are good at this. Do you practice this at home? I'd believe it if you said yes. Don't bother answering though, keep taking my cock deep.",
    "God, that's it. Pretend like your throat is your pussy and enjoy it, everytime it goes deep.",
    "Fuck, you take cock down your throat like a pro. Keep going, I want to see if you even can gag anymore.",
    "Your throat feels amazing. Keep at it, I want you to keep practicing."]

    blowjob_training_condition_skull_fuck_list = [
    "A good slut takes cock down her throat at will, and right now, I will it.",
    "All you need to do is open your mouth and I'll do the rest. Keep practicing, and eventually you'll be able to do it without gagging the whole time.",
    "You're a good slut, but a horrible cock sleeve. Open up, you need to keep practicing",
    "A good slut gags on her mans cock. Get ready, I'm going to ram it down your throat again until you gag on it the way you should.",
    "Damn, your throat feels great. Does it make you happy to gag and slobber all over my cock? It should.",
    "You are almost the perfect slut. You do great, taking my cock like this, we just need to train out the last of your gag reflex.",
    "Do you even have a gag reflex anymore? Don't answer that, I'm going to grab you by your head and find out.",
    "I'm not sure there is much I can teach you, but I'm going to keep using that throat of yours anyway.",
    "Fuck, that throat of yours feels amazing. Now take it like a good little cocksleeve."]


label condition_blowjob_training_pre_label(the_person, the_position, the_object, report_log, the_condition):
    $ dialogue_index = the_person.sex_skills["Oral"]
    $ dialogue_index = min(6, dialogue_index)   #Set bound conditions
    $ dialogue_index = max(0, dialogue_index)
    $ dialogue_index += renpy.random.randint(0,2)   #add up to 2 to index for varying dialogue per session.
    $ mc_dialogue = blowjob_training_condition_blowjob_list[dialogue_index]
    if the_position == deepthroat:
        $ mc_dialogue = blowjob_training_condition_deepthroat_list[dialogue_index]
    elif the_position == skull_fuck:
        $ mc_dialogue = blowjob_training_condition_skull_fuck_list[dialogue_index]
    mc.name "[mc_dialogue]"
    "[the_person.possessive_title] listens and tries what you suggest."
    return

label condition_blowjob_training_post_label(the_person, the_position, the_object, report_log, the_condition):
    $ the_person.change_obedience(1)
    return

label condition_blowjob_training_reward_label(the_person, report_log, the_condition):
    $ the_person.increase_sex_skill("Oral")
    $ the_person.change_obedience(10)
    "[the_person.possessive_title] seems pleased she managed to get you off during your training."
    return
