init 2 python:
    def train_anal_fetish_requirement(person):
        if not is_anal_fetish_unlocked():
            return False
        if person.has_role(anal_fetish_role):
            return False
        if person.has_started_anal_fetish:
            return "Not started"
        if person.sluttiness < 50:
            return ">50 sluttiness"
        if person.get_opinion_score("anal sex") < 1 or person.get_opinion_score("anal creampies") < 1:
            return "Likes Anal Sex and Creampies"
        return True

    def increase_anal_fetish(person):
        if renpy.random.randint(0,100) < 25: # only chance to increase skill
            person.increase_sex_skill("Anal", 5, add_to_log = True)
        person.change_slut(2, 90, add_to_log = True)
        if not fetish_serum_increase_opinion(FETISH_ANAL_OPINION_LIST, 2, person):
            mc.log_event((person.title or person.name) + " anal fetish training is less effective, but she hasn't got a fetish yet.", "float_text_blue")
        return

    anal_fetish_trainable = Trainable("anal_fetish_train", "train_anal_fetish_label", "Anal Fetish", base_cost = 2000, unlocked_function = train_anal_fetish_requirement)
    special_trainables.append(anal_fetish_trainable)

label train_anal_fetish_label(the_person):
    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you really enjoy when I play with your ass."
    the_person "Yeah... I do..."
    mc.name "I was thinking that we should explore this a little further, what do you think?"
    the_person "Well, I wouldn't mind, if you did."
    mc.name "Good, stand up and show me your butt."
    $ the_person.draw_person(position = "standing_doggy")
    "[the_person.possessive_title] turns around to show you her bottom."
    if not the_person.vagina_available:
        mc.name "Let's get these clothes out of the way."
        $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "standing_doggy")
    "Now since you got her sweet ass on display, what do you plan to do with it?"
    menu:
        "Rub her ass":
            "You reach out and start to rub her ass."
            the_person "Hmmm, that feels nice..."
            "As you slowly move your thumbs closer to her rectum, she starts pushing her butt in your direction."
            mc.name "You like this, don't you?"
            the_person "Oh yes, please, just push them a little inside."
            "You place your thumbs on either side and slide the tips inside, provoking a little sigh from [the_person.possessive_title]."
            mc.name "Do you want me to stretch it a bit for you?"
            the_person "Mmm... get that dirty hole ready for your big cock."
            "You continue stretching her asshole for a while, until you notice that her [the_person.pubes_description] pussy starts glistening."

        # TODO: Write the ass spanking part
        #"Spank her ass" if the_person.get_opinion_score("being submissive") > 0:
        #    pass

        "Finger her ass" if the_person.sex_skills["Anal"] > 1:
            "You reach out and start to rub her bottom."
            the_person "Hmmm, that feels nice..."
            "After awhile, you slowly start tracing her orifice with your fingers. Causing a slight tremble from [the_person.possessive_title]."
            the_person "Oh, yes, right there [the_person.mc_title]."
            "That's all the encouragement you need to slide your finger inside."
            the_person "Mmmm... yes... that's it. Every time I play with myself I have to push a finger inside."
            menu:
                "Continue":
                    "Using some spit as lube, you shove your entire finger inside of her."
                    the_person "Oh god, YES, just like that..."
                    "You continue to finger fuck her ass for a while, until her [the_person.pubes_description] pussy gets really wet."
                "Slide in a second finger":
                    "You lube up a second finger with your saliva and push both fingers inside."
                    the_person "Ahhh... YES... stretch my dirty hole [the_person.mc_title]."
                    mc.name "You are going to be my slutty anal bitch, aren't you [the_person.fname]?"
                    the_person "Yes... I will... hmmm... right there..."
                    "You continue to shove your fingers up her bum, until her [the_person.pubes_description] pussy gets really wet."

        "Shove a dildo inside" if the_person.sex_skills["Anal"] > 2 and perk_system.has_item_perk("Dildo"):
            if the_person.event_triggers_dict.get("has_used_dildo", False):
                mc.name "I have brought your favorite toy."
                the_person "Ok, slide that bad boy right in there!"
            else:
                mc.name "I have something I think you might enjoy."
                the_person "Oh? What might that be?"
                "You pull the dildo out of your backpack. Her eyes fix on it and she realizes what you want to do."
                if the_person.sluttiness > 40: #She is excited.
                    the_person "Oh! That looks like fun..."
                else:
                    the_person "Oh my god, it's so big! I don't know about this..."
                    mc.name "Don't worry, I'll go slow."

            "You lube up the dildo and slide it all the way into her bowels, leaving just enough room to hold it."
            the_person "Oh god, that's it [the_person.mc_title]."
            mc.name "You enjoy this, don't you?"
            the_person "Oh yes, please, can you push it a little further."
            mc.name "Do you want to swallow it with your ass?"
            the_person "I wouldn't mind giving it a try..."
            "You smile, and press the last part of the toy into her ass until her sphincter closes over the end caressing your fingers."
            the_person "Ahhh....Yes...sooo deep...keep moving..."
            mc.name "You are going to be my little anal whore, aren't you [the_person.fname]?"
            the_person "I am...YES...deeper...your greedy little anal whore!!"
            "You continue to push the toy back when it slowly starts moving out again, until you finally let it pop out completely."

    mc.name "Alright, [the_person.title], that's enough for now. We will continue this another time."
    $ increase_anal_fetish(the_person)
    the_person "Oh [the_person.mc_title], that felt... just... amazing."
    if start_anal_fetish_quest(the_person):
        $ the_person.event_triggers_dict["anal_fetish_start"] = True
        "It seems you have awoken something inside her, just wait and see what happens."
    else:
        if the_person.sluttiness < 70:
            "Although you have made some progress, you have the feeling she needs to be sluttier to fully develop this fetish."
        else:
            "You have come one step closer to awakening her anal desires. Perhaps another session or a serum with the Anal Nanobots will push her over the edge."
    $ the_person.apply_planned_outfit()
    $ the_person.draw_person()
    the_person "Please, don't make me wait too long."
    return True
