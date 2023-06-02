# We pick up this story after the event where she is afraid of losing her job.
# First, we tie this thread up by making sure she has pleased her boss with sexual favors. She may have only gotten bigger tits at this point.
init -1 python:
    def mom_lust_story_bridge_requirement(person):
        if person.story_event_ready("slut") and person.location == kitchen:
            return mc.business.is_work_day  # only during workweek
        return False

    def mom_lust_boss_prostitutes_intro_requirement(person):
        return False

init 2 python:
    mom_lust_story_bridge = Action("Mom's work update", mom_lust_story_bridge_requirement, "mom_lust_story_bridge_label")
    mom_lust_boss_prostitutes_intro = Action("Mom's boss visits whores", mom_lust_boss_prostitutes_intro_requirement, "mom_lust_boss_prostitutes_intro_label")


label mom_lust_story_bridge_label(the_person):    #We can make this an on talk event.
    $ the_person.draw_person(emotion = "happy")
    $ the_person.lust_step = 6
    "When you walk into the room, you notice [the_person.possessive_title]. She is humming and seems to be in a great mood."
    mc.name "Hey [the_person.title]. You seem like you are having a good day! How was work?"
    if the_person.event_triggers_dict.get("mom_replacement_approach", "seduce") == "seduce":
        the_person "Oh! Hello honey! It was a great day indeed!"
        the_person "My boss has really been having it rough lately, but it has really given me the opportunity to shine!"
        the_person "There is something so satisfying about helping a man let go of all his stress for even just a few minutes when you get down on your knees and..."
        if the_person.love > 40 or the_person.is_girlfriend:
            the_person "I umm... sorry, this probably isn't something you are interested hearing about..."
        else:
            the_person "Well, let's just say that more and more of my time lately has been spent under his desk!"
        $ mc.change_locked_clarity(20)
    else:
        the_person "Ah, you could say that. I think I had a breakthrough with my boss."
        the_person "He has been so stressed out lately, and I could tell that just teasing him with my tits was really getting to him..."
        the_person "So I felt like it would be okay if I could help him relieve his stress some. Just a little!"
        the_person "So when he had his lunch break, I got down below his desk and... well..."
        menu:
            "Congratulate her":
                mc.name "Hey, that's great! Good job [the_person.title], I knew you could do it."
                the_person "Thank you [the_person.mc_title]. It's a huge weight off of my shoulders, that's for sure."

            "Ask how she did it":
                mc.name "That's great! So, how did you do it?"
                the_person "Well, I... Are you sure you want me to tell you this? Oh, I guess it's not a big deal."
                the_person "I asked to have a discussion with him in his office during lunch today."
                the_person "He wasn't happy about having his lunch interrupted, but he seemed much more interested when I took my top off."
                mc.name "Mmhm? Go on."
                the_person "Once I had his attention I told him I was really worried about stressed he was getting. He asked me what I was going to do about it."
                "She blushes a little and shrugs innocently."
                the_person "So I got onto my knees and used my mouth to... pleasure him."
                $ mc.change_locked_clarity(30)
                the_person "When he, um... {i}finished{/i}, he couldn't stop talking about how glad he was he hired me!"
                the_person "Thank you for your help [the_person.mc_title], I never would have gotten this promotion if it weren't for you!"
                mc.name "My pleasure [the_person.title], I'm just happy that you're doing what you enjoy."
                "She smiles and gives you a quick hug." #Copy the seduction menu choices
    "Things with [the_person.possessive_title] and her boss seem to be going well... but is this something you really want to continue?"
    "How much longer will it be until he is fucking her on the regular? Is that what you want? Would that make her happy?"
    "Maybe instead of encouraging things... you should try and hire her yourself? It is something to think about anyway."
    "For now, you are just happy that she is happy."
    $ the_person.add_unique_on_room_enter_event(mom_lust_boss_prostitutes_intro)
    return

label mom_lust_boss_prostitutes_intro_label(the_person):    #At 60 sluttiness, she finds out her boss is using prostitutes after finding his bank statements
    pass
    return


#The next set of labels allow us to pick up where she left off if we hire her.



label mom_new_employee_first_day_label():
    $ the_person = mom



    return
