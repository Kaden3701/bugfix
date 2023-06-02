init 2 python:
    def sister_failed_test_requirement():
        if not lily.has_job(sister_student_job) and not lily.is_employee:
            return False
        if not lily.is_available or lily.has_queued_event("sleeping_walk_in_label"):
            return False
        if erica.event_triggers_dict.get("insta_pic_intro_complete", False) and day % 7 == 5:
            return False # Erica visits on saturday nights (no study time)
        if mc.is_in_bed and mc.business.event_triggers_dict.get("sister_serum_test", False) and lily.is_available:
            return True
        return False

    sister_failed_test_crisis = ActionMod("Lily Needs Help Studying",sister_failed_test_requirement,"sister_failed_test_label",
        menu_tooltip = "Lily needs help studying for school or work.", category = "Home", is_crisis = True)

#new night time crisis. Lily enters MC's bedroom and asks for help because she failed a test at school.
#Options change based on story progression with Lily. She can't pay you for tutoring, but offers other services.
#Basic option is to have her take a serum. If MC has unlocked it, you can have her strip before you start.
#If she strips before you start, based on sluttiness, things might go further.
label sister_failed_test_label():
    $ the_person = lily
    if the_person.has_job(sister_student_job):
        $ student = True
        $ word = "study"
        $ failed_subject = get_random_from_list( ["Calculus", "Biology", "Chemistry", "Physics", "Geology"])
    else:
        $ student = False
        $ word = "work"
    $ mc.change_location(bedroom) #Make sure we're in our bedroom.
    "Laying in your bed, you hear a knock on your door. You hear [the_person.possessive_title] from the other side of the door."
    the_person "Hey [the_person.mc_title], you still up? I was just wondering if I could come in for a bit?"
    mc.name "It's open."
    $ the_person.draw_person()
    "[the_person.title] is standing at your door. She is holding a backpack?"
    the_person "So... you're pretty smart, right?"
    "She walks over to your bed."
    mc.name "I mean, I did okay in school."
    "She rustles around in her backpack, before pulling out a piece of paper."
    if student:
        the_person "I'm having some troubles in my [failed_subject] class... I thought maybe you would be willing to [word] with me for a little bit?"
        "In her hand is a failed quiz."
    else:
        the_person "I'm having some troubles with my [the_person.job.job_title] tasks... I thought maybe you would be willing to [word] with me for a little bit?"
        if the_person.job == market_job:
            "In her hand are some phone scripts for cold calling."
        if the_person.job == rd_job or the_person.job == head_researcher_job:
            "In her hand are some readouts from the analyzers at work."
        if the_person.job == production_job:
            "In her hand is a manual for one of the machines you use on the assembly line."
        if the_person.job == supply_job:
            "In her hand is a spreadsheet of chemicals and their prices."
        if the_person.job == hr_job:
            "In her hand is an employee file for one of her coworkers."
    menu:
        "Help her":
            pass
        "Refuse":
            mc.name "I'm sorry, I'm way too tired to do that tonight."
            the_person "Okay... sorry to bug you [the_person.mc_title]."
            $ the_person.draw_person(position = "walking_away")
            "[the_person.possessive_title] walks out of your room, leaving you to sleep."
            $ the_person.change_stats(happiness = -3, obedience = 3, love = -1)
            return
    $ strip_path = False
    "You sit up and pat the bed. She sits down next to you."
    $ the_person.draw_person(position = "sitting")
    mc.name "Before we get started though, I want something in exchange."
    if student:
        the_person "I don't have any money to pay you for tutoring."
        mc.name "That's okay, I have something else in mind."
    else:
        the_person "Isn't working for you enough?"
        mc.name "It would be if you could get the job done yourself. Don't worry, it isn't anything extreme."
    menu:
        "Give her a serum" if mc.inventory.total_serum_count > 0:
            "You reach over to your backpack."
            if student:
                mc.name "Normally I pay you $50 to take one of these. Take one now, and that way I can also observe the effects while we [word]."
            else:
                if the_person.has_duty(daily_serum_dosage_duty):
                    mc.name "Since we are working more than expected I think you need to take another does of your daily serum."
                    the_person "Do you have them with you."
                    mc.name "I'll find something that will work."
                elif the_person.has_duty(unpaid_serum_testing_duty):
                    mc.name "Normally you take one of these for free as part of your job. Since we are working take one now, and that way I can also observe the effects while we [word]."
                else:
                    mc.name "Normally I pay you $50 to take one of these. Take one now, and that way I can also observe the effects while we [word]."
            the_person "Okay, that seems fair."
            call give_serum(the_person) from _call_give_serum_lily_study_time_01
            if _return:
                "You hand her the serum. She quickly drinks it, making a sour face from the taste."
                the_person "Alright, ready?"
                $ the_person.apply_serum_study()
            else:
                "After looking at your serums, you decide none of them would be useful."
                mc.name "Actually, I don't have the right ones with me. Come on let me just help you [word]."
        "Strip" if mc.business.event_triggers_dict.get("sister_strip",False) and not (the_person.tits_available or the_person.vagina_available):
            $ strip_path = True
            mc.name "Why don't you take off some of your clothes, that way I have something nice to look at while we [word]?"
            if the_person.sluttiness < 40 and not the_person.outfit.is_suitable_underwear_set: #Hesitant
                the_person "I know I do that sometimes, but usually I get dressed right after..."
                mc.name "It's just me. Having you wearing a little less would help me stay awake, too."
                "Her willpower crumbles."
                the_person "I don't know. How about if I just strip down to my underwear?"
                mc.name "That sounds good!"
                the_person "Okay..."
                $ the_person.draw_person(position = "stand3")
                "[the_person.title] stands up and starts to take some clothing off..."
                $ the_person.strip_to_underwear(position = "stand3")
                $ mc.change_locked_clarity(20)
                "When she finishes, she stands there for a moment, letting you check her out."
                $ the_person.change_slut(2)
                the_person "Okay... let's get started before this gets more awkward!"
            elif the_person.sluttiness > 60: #Eager
                the_person "Oh! That's a great idea! I know how much you like to look at me naked."
                $ the_person.draw_person(position = "stand3")
                "[the_person.title] stands up and starts to take some clothing off..."
                $ the_person.strip_outfit(position = "stand3")
                $ mc.change_locked_clarity(20)
                $ the_person.change_slut(2)
                "You check her out when she finishes. She even strikes a little pose for you."
                $ the_person.draw_person(position = "back_peek")
                the_person "There. Does this convince you to help me [word]?"
                $ mc.change_locked_clarity(20)
                mc.name "Yes, it does."
                the_person "Okay! Let's get started before we get too distracted!"
            else:   #Compliant
                the_person "Trying to get me out of my clothes again? I should have known."
                "[the_person.possessive_title] stands up. Is she leaving?"
                $ the_person.draw_person(position = "stand3")
                mc.name "Sorry, I thought since you had started doing that for me recently you might be open to it..."
                "[the_person.title] looks at you and laughs."
                the_person "What? I didn't say no. Since this is free, I get to decide what comes off though..."
                $ the_person.strip_outfit_to_max_sluttiness(position = "stand3")
                $ mc.change_locked_clarity(20)
                "When she finishes, [the_person.title] is wearing significantly less clothing."
                the_person "There. Does this convince you to help me [word]?"
                mc.name "Yes, it does."
                the_person "Okay! Let's get started!"
        "Go get your uniform" if the_person.is_employee and strict_uniform_policy.is_active and the_person.planned_uniform:
            $ the_person.apply_outfit(the_person.planned_uniform)
            if the_person.judge_outfit(the_person.planned_uniform):
                the_person "That's not too bad. It will help me get into the proper head space too."
            else:
                the_person "God, this is so embarrassing. At least at work I'm not the only one dressed like a slut."
            if office_punishment.is_active:
                mc.name "Now strip."
                if the_person.sluttiness > 60: #Eager
                    the_person "Oh! That's a great idea! I know how much you like to look at me naked."
                    $ the_person.draw_person(position = "stand3")
                    "[the_person.title] stands up and starts to take some clothing off..."
                    $ the_person.strip_outfit(position = "stand3")
                    $ mc.change_locked_clarity(20)
                    $ the_person.change_slut(2)
                    "You check her out when she finishes. She even strikes a little pose for you."
                    $ the_person.draw_person(position = "back_peek")
                    the_person "There. Does this convince you to help me [word]?"
                    $ mc.change_locked_clarity(20)
                    mc.name "Yes, it does."
                    the_person "Okay! Let's get started before we get too distracted!"
                else:   #Compliant
                    the_person "Trying to get me out of my clothes again? I should have known."
                    "[the_person.possessive_title] stands up. Is she leaving?"
                    $ the_person.draw_person(position = "stand3")
                    mc.name "Sorry, I thought since we were working and you are deserving of punishment for failing to get your tasks done..."
                    "[the_person.title] looks at you and laughs."
                    the_person "What? I didn't say no. Since this is free, I get to decide what comes off though..."
                    $ the_person.strip_outfit_to_max_sluttiness(position = "stand3")
                    $ mc.change_locked_clarity(20)
                    "When she finishes, [the_person.title] is wearing significantly less clothing."
                    the_person "There. Does this convince you to help me [word]?"
                    if strict_enforcement.is_active and not (the_person.vagina_available and the_person.tits_available):
                        mc.name "Keep going."
                        $ the_person.strip_outfit(position = "stand3")
                        $ mc.change_locked_clarity(20)
                        $ the_person.change_slut(2)
                        "You check her out when she finishes. She even strikes a little pose for you."
                        $ the_person.draw_person(position = "back_peek")
                        the_person "Okay... let's get started before this gets more awkward!"
                    else:
                        mc.name "Yes, it does."
                        the_person "Okay! Let's get started!"
        "Just Study":
            mc.name "Actually... I can't think of anything. Come on let me just help you study."

    # switch to strip path if she is teasing you (even without stripping)
    if not strip_path and (the_person.vagina_available or the_person.tits_available):
        $ strip_path = True
    mc.name "Here, why don't you sit next to me in the bed here while we [word]. You'll be more comfortable that way."
    the_person "Okay."
    $ the_person.draw_person(position = "sitting")
    "You pull the covers back. [the_person.title] sits down on the bed next to you, her back against the headboard."
    if strip_path:
        "Having [the_person.possessive_title] in your bed next to you, wearing so little, gets you excited, but you try to shake the thought and concentrate on [word]ing... for now anyway."
        $ mc.change_locked_clarity(20)
    if student:
        "You get into the books and take a look at [the_person.possessive_title]'s failed quiz. You recognize most of the material from your own time at the university."
        if mc.int > 5:
            "The text books themselves are a newer edition, but you remember where most of the information is located."
            "You quickly mark some places with sticky notes and help [the_person.title] make a quick study guide to avoid this quiz result again."
        elif mc.int >2:
            "The text books are a newer version, and it takes you quite a bit of time to figure out where all the information is located."
            $ mc.change_energy(-5)
            "Eventually, you are able to help [the_person.title] put together a study guide to avoid this quiz result again."
        else:
            "It's been too long since university. The books are new editions and you barely remember the material. It takes a team effort with [the_person.title] to find it all."
            $ mc.change_energy(-15)
            "After an extended period, you finally help her put together a study guide to avoid this quiz result again."
    else:
        if the_person.job == market_job:
            "You skim the phone scripts while thinking about how you chat with customers on the phone."
        if the_person.job == rd_job or the_person.job == head_researcher_job:
            "You skim the readouts, quickly identifying what they mean and thinking about what might need done to improve them."
        if the_person.job == production_job:
            "The machine giving [the_person.title] problems looks familiar from the cover of the manual so you have her explain the hang up."
        if the_person.job == supply_job:
            "You skim the list of suppliers and try to recall their various purchasing options."
        if the_person.job == hr_job:
            $ other_person = get_random_from_list(mc.business.employee_list)
            "You flip through the folder about [other_person.title] trying to figure out what is causing problems."
            $ other_person = None
        if mc.int > 5:
            "Even if you don't do her job every day you quickly recall the information you use working in the [the_person.job.job_location.name]."
            "You quickly mark some places with sticky notes and help [the_person.title] figure out how to get past the road blocks."
            if the_person.job == market_job:
                $ the_person.change_market_skill(1)
            if the_person.job == rd_job or the_person.job == head_researcher_job:
                $ the_person.change_research_skill(1)
            if the_person.job == production_job:
                $ the_person.change_production_skill(1)
            if the_person.job == supply_job:
                $ the_person.change_supply_skill(1)
            if the_person.job == hr_job:
                $ the_person.change_hr_skill(1)
        elif mc.int >2:
            "Working in the [the_person.job.job_location.name] is not your favorite thing, and it takes you quite a bit of time to figure out where all the information is located."
            $ mc.change_energy(-5)
            "Eventually, you are able to help [the_person.title] solve most of her problems."
        else:
            "It's been too long since worked in the [the_person.job.job_location.name] you barely remember the role. It takes a team effort with [the_person.title] to figure it all out."
            $ mc.change_energy(-15)
            "After an extended period, you finally help her plan out what she will do the next time she is at work.."
    the_person "Thank you [the_person.mc_title]... You're the best!"
    "She leans over and gives you a big hug, lingering with her body up against yours for several seconds."
    if strip_path:
        "Having [the_person.possessive_title] up against you quickly reminds you of her undressed state. You quickly get an erection from the close physical contact."
        $ mc.change_locked_clarity(10)
    else:
        "Eventually, [the_person.possessive_title] gets up and grabs her stuff."
        the_person "Thank you so much for the help. Good night!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] gets up and leaves your room, closing your door on the way out."
        $ the_person.change_stats(happiness = 3, obedience = 3, love = 3)
        return
    "She slowly sits up again. When you look down, you realize your erection is making an obvious tent in the blankets. There's no way she doesn't notice..."
    if the_person.sluttiness < 30: #Too chaste to do anything about it, but she still likes it.
        the_person "Ahhh, I'm sorry [the_person.mc_title], I didn't mean to get you excited."
        mc.name "It's okay, it happens when you are around sometimes."
        "[the_person.title] stays quiet, but you can see her blushing."
        $ the_person.change_slut(2)
        $ the_person.change_slut(3)
        $ the_person.draw_person(position = "stand2")
        if student:
            "She gets up and slowly collects her books."
        else:
            "She gets up and slowly collects her things."
        mc.name "Goodnight."
        the_person "Goodnight."
        $ the_person.draw_person(position = "walking_away")
        $ the_person.change_stats(happiness = 3, obedience = 3, love = 3)
        "[the_person.title] leaves your room, closing your door on the way out."
        return
    else:
        the_person "Ahh... I see you are a little excited there."
        mc.name "Sorry, it happens when you are around sometimes."
        "Slowly, she reaches her hand over to it. She runs her finger around the tip and plays with it a bit."
        the_person "Do you want me to take care of that for you? You were so helpful tonight, I'd be glad to..."
        $ mc.change_locked_clarity(20)
        menu:
            "Ask for handjob" if mc.energy > 50:
                the_person "Okay... I can do that."
                "Her hand goes under the covers and onto your chest. She slowly rubs your body with her hand as it works it's way south."
                "When she gets to your underwear, you lift your hips up a bit as [the_person.title] pulls them down, setting your erection free."
                if the_person.has_taboo("touching_penis"):
                    "[the_person.possessive_title] begins to falter a bit. You can sense her hesitation to touch you."
                    the_person "Are you sure... this is okay? I feel like we are really crossing a line here..."
                    mc.name "It's okay. It feels so good, don't you want to make me feel good?"
                    the_person "Yes... of course I want to... I just..."
                    "You take her hand in yours. She looks at you and bites her lip. You slowly move her hand down until your cock is resting in her palm."
                    the_person "Oh my god... it's so... warm..."
                    "Her hand starts to stroke you."
                    $ the_person.break_taboo("touching_penis")
                    $ mc.change_arousal(15)
                else:
                    "[the_person.possessive_title] reaches down and takes a light hold of your erection."
                    the_person "Oh god... I don't know why, but it always surprises me how warm it is..."
                    "Her hand starts to stroke you."
                    $ mc.change_arousal(15)
                call get_fucked(the_person, start_position = handjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _lily_study_time_handjob_01

            "Ask for blowjob" if the_person.sluttiness >= 50 and mc.energy > 50 and not the_person.has_taboo("touching_penis"):
                the_person "Mmm, okay. I'll do that for you [the_person.mc_title]."
                $ the_person.draw_person(position = "kneeling1")
                "[the_person.possessive_title] pulls the covers down and moves down to your legs. You lift her hips up when she pulls at your shorts, setting your erection free."
                if the_person.has_taboo("sucking_cock"):
                    "[the_person.title] takes your cock in her hand and gives it a couple strokes, but you can tell she is hesitating to go any further."
                    the_person "Are you sure... this is okay? I mean... I'm about to put my brother's cock in my mouth!"
                    mc.name "It's okay. It's going to feel so good, don't you want to make me feel good?"
                    the_person "Yeah... I mean... you were very helpful tonight..."
                    "She pauses for several seconds. You start to get worried she is going to back out."
                    the_person "Okay. Just this once, okay?"
                    "You nod your approval. [the_person.possessive_title] lowers her face until you can feel her breath on your aching cock."
                    the_person "Its just a blowjob. Here it goes!"
                    "[the_person.title] opens her mouth and runs her tongue along the tip, tasting your precum. The attention makes your penis twitch with need."
                    $ the_person.break_taboo("sucking_cock")
                    "The moment of truth arrives. [the_person.possessive_title] opens her mouth wide and slowly slides your cock past her lips. Their velvet warmth feels amazing."
                    "[the_person.title] begins to slowly bob her head up and down."
                else:
                    "[the_person.title] takes your cock in her hand and gives it a couple strokes."
                    the_person "Mmm, god it feels so hard. It feels like you really need to get off."
                    mc.name "I know. This is what you do to me [the_person.title]."
                    the_person "Ahh, so this is my fault? I suppose it's only fair that I help you with this problem then."
                    "[the_person.possessive_title] lowers her face until you can feel her breath on your aching cock."
                    "[the_person.title] opens her mouth and runs her tongue along the tip, tasting your precum. The attention makes your penis twitch with need."
                    mc.name "[the_person.title]... please..."
                    the_person "Mmm, I love to hear you beg."
                    "[the_person.possessive_title] opens her mouth wide and slowly slides your cock past her lips. Their velvet warmth feels amazing."
                    "[the_person.title] begins to slowly bob her head up and down."
                call get_fucked(the_person, start_position = cowgirl_blowjob, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_lily_study_time_blowjob_01
            "Ask for quickie" if the_person.sluttiness >= 60 and mc.energy > 50 and the_person.vagina_available and not the_person.has_taboo("touching_penis") and not the_person.has_taboo("sucking_cock"):
                if the_person.has_taboo("vaginal_sex"):
                    the_person "Wow... you want me to just... hop on and go for a ride? That's... a little crazy, don't you think?"
                    the_person "I mean, we've never even gone that far before..."
                    mc.name "Sorry, I umm, just said the first thing that popped into my head."
                    "[the_person.possessive_title] smiles at you."
                    the_person "I mean... I didn't say no... I just wasn't expecting you to just say it so nonchalantly. Let's have a quickie."
                    "Her hand is still stroking you through the covers. It feels like she is speeding up some..."
                    the_person "It's not like I've been totally just waiting for you to ask me something like this..."
                    "[the_person.title] pulls back the covers, you lift your hips when she pulls at your shorts, freeing your cock from its confines."
                    $ the_person.draw_person(position = "kneeling1")
                    the_person "God you always look so hard... I bet you really need to get off, don't you?"
                    mc.name "I know. This is what you do to me [the_person.title]."
                    "[the_person.possessive_title] lowers her face to your cock. She opens her mouth and starts to suck on the tip, tasting your precum."
                    "She gives your dick several strokes, but then stops."
                    $ the_person.draw_person(position = "cowgirl")
                    the_person "Okay... let's do it!"
                    "[the_person.title] climbs up on top of you, your cock in her hand."
                    $ the_person.break_taboo("vaginal_sex")
                    $ mc.change_locked_clarity(50)
                else:
                    the_person "Mmm, I was hoping you would say that!"
                    "[the_person.title] pulls down the covers. You lift your hips up when she pulls at your shorts, freeing your cock from its confines."
                    "She gives it a few strokes with her hand."
                    $ the_person.draw_person(position = "cowgirl")
                    the_person "Okay... let's do it!"
                    "[the_person.title] climbs up on top of you, your cock in her hand."
                    $ mc.change_locked_clarity(30)

                if requires_condom(the_person):
                    "[the_person.possessive_title] reaches over to her backpack, she pulls a condom out of her bag."
                    the_person "Better wrap you up, don't want to have any accidents..."
                    "She opens the package, then skillfully slides the condom down your penis."
                    the_person "Mmm, now we're ready!"
                    $ mc.condom = True
                elif the_person.has_breeding_fetish:
                    "She gives your cock a couple strokes."
                    the_person "Mmm... it's so hard. Do you have a good load saved up for me? I can't wait to feel it splash inside me..."
                elif the_person.has_taboo("condomless_sex"):
                    the_person "So... I know we've never really done this before but... do you think we could skip the condom?"
                    mc.name "If that is a risk you are willing to take, I'm okay with that [the_person.title]."
                    the_person "I know it's a little risky... I just... I want to feel you inside me, with no latex sleeve between us..."
                    $ mc.condom = False
                    $ the_person.change_arousal(15)
                    $ mc.change_locked_clarity(50)
                    $ the_person.break_taboo("condomless_sex")
                "[the_person.possessive_title] lifts her hips up slightly, lining you up with her pussy. She slowly lowers herself down, your cock pushing inside of her."
                "It takes a few seconds, but with steady pressure she manages to take you all the way. She takes a few moments to adjust to the feeling, then begins to rock her hips."
                call get_fucked(the_person, start_position = cowgirl, the_goal = "get mc off", private = True, skip_intro = True, allow_continue = False) from _call_get_fucked_lily_study_time_quickie_01
                $ the_report = _return
                if the_report.get("girl orgasms", 0) > 0:
                    the_person "Wow... that felt so good..."
                    "[the_person.title] takes it easy for a moment, enjoying the afterglow of her orgasm."
                    the_person "You made me cum so hard... I guess I still owe you a favor sometime?"
                elif the_report.get("guy orgasms", 0) > 0:
                    the_person "Mmm, that was hot..."
                    "[the_person.title] is a little slow to get up."
                    the_person "I think I need a little alone time in my room..."
                else:
                    "[the_person.title] seems a little disappointed that you didn't finish."
                    mc.name "I'm sorry, I think I'm just worn out."
                    the_person "That's okay. I'll just have to owe you one another time, okay?"
                "After a minute or so, [the_person.title] gets up."
            "Decline":
                mc.name "I appreciate that, but I'm just too tired tonight."
                "[the_person.title] stays quiet, but you can see her blushing."
                $ the_person.change_slut(2)
                $ the_person.change_slut(2)
        $ the_person.draw_person(position = "stand2")
        if student:
            "She gets up and slowly collects her books."
        else:
            "She gets up and slowly collects her things."
        mc.name "Goodnight."
        the_person "Goodnight."
        $ the_person.draw_person(position = "walking_away")
        "[the_person.title] leaves your room, closing your door on the way out."
        $ clear_scene()
    return

label sister_failed_test_unit_test():
    $ mc.business.event_triggers_dict["sister_serum_test"] = True
    python:
        the_person = lily
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 0
        the_person.sluttiness = 0
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 0"
    call sister_failed_test_label from _unit_test_lily_failed_test_01

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 10
        the_person.sluttiness = 10
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 10"
    call sister_failed_test_label from _unit_test_lily_failed_test_02

    $ mc.business.event_triggers_dict["sister_strip"] = True
    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 20
        the_person.sluttiness = 20
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 20"
    call sister_failed_test_label from _unit_test_lily_failed_test_03

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 30
        the_person.sluttiness = 30
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 30"
    call sister_failed_test_label from _unit_test_lily_failed_test_04

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 40
        the_person.sluttiness = 40
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 40"
    call sister_failed_test_label from _unit_test_lily_failed_test_05

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 60
        the_person.sluttiness = 60
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 60"
    call sister_failed_test_label from _unit_test_lily_failed_test_06

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 80
        the_person.sluttiness = 80
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 80"
    call sister_failed_test_label from _unit_test_lily_failed_test_07

    python:
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.sluttiness = 100
        the_person.sluttiness = 100
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0

    "Unit test Lily Test scenario, sluttiness = 100"
    call sister_failed_test_label from _unit_test_lily_failed_test_08
    return
