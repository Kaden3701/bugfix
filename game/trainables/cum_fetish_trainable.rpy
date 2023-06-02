init 2 python:
    def train_cum_fetish_requirement(person):
        if not is_cum_fetish_unlocked():
            return False
        if person.has_role(cum_fetish_role):
            return False
        if person.has_started_cum_fetish:
            return "Not started"
        if person.sluttiness < 50:
            return ">50 sluttiness"
        return True

    def increase_cum_fetish(person):
        if renpy.random.randint(0,100) < 25: # only chance to increase skill
            person.increase_sex_skill("Oral", 5, add_to_log = True)
        person.change_slut(2, 90, add_to_log = True)
        if not fetish_serum_increase_opinion(FETISH_CUM_OPINION_LIST, 2, person):
            mc.log_event((person.title or person.name) + " cum fetish training is less effective, but she hasn't got a fetish yet.", "float_text_blue")
        return

    def get_attaboy_girl_response(the_person):
        text_list = []
        if the_person.sex_record.get("Vaginal Creampies", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("creampies", None))
        if the_person.sex_record.get("Anal Creampies", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("anal creampies", None))
        if the_person.sex_record.get("Cum Facials", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("cum facials", None))
        if the_person.sex_record.get("Cum in Mouth", 0) > 0:
            text_list.append(attaboy_cum_descriptions.get("drinking cum", None))
        if len(text_list) == 0: #Didn't inside her
            text_list.append("I get so exited when you cum all over me!")
        return get_random_from_list(text_list)

    cum_fetish_trainable = Trainable("cum_fetish_train", "train_cum_fetish_label", "Cum Fetish", base_cost = 2000, unlocked_function = train_cum_fetish_requirement)
    special_trainables.append(cum_fetish_trainable)


label train_cum_fetish_label(the_person):
    mc.name "I've got something to talk to you about [the_person.title]."
    "She nods and listens attentively."
    mc.name "I've noticed that you enjoy my cum a lot."
    $ text_1 = get_attaboy_girl_response(the_person)
    the_person "Uhm... yeah... [text_1]"
    mc.name "You would like it if I did that more often, right?"
    the_person "Oh... yes... I really would love that."
    mc.name "I want you to close your eyes and imagine me doing that right now."
    "She closes her eyes and you see her getting exited by the idea."
    $ increase_cum_fetish(the_person)
    the_person "Oh [the_person.mc_title], I can feel it..."
    if start_cum_fetish_quest(the_person):
        $ the_person.event_triggers_dict["cum_fetish_start"] = True
        "It seems you stirred something inside her, just wait and see what happens."
    else:
        if the_person.sluttiness < 70:
            "Although you have made some progress, you have the feeling she needs to be sluttier to embrace this fetish."
        else:
            "You have come one step closer to inducing her cum fetish. Perhaps another session or a serum with the Semen Nanobots will push her over the edge."
    mc.name "Alright, [the_person.title], that's enough for now. We will talk about this soon."
    the_person "Yes, I would love that."
    return True
