# This is a hidden role designed to track changes in jealousy status in the sister pair Ashley and Stephanie
# In general, sexual actions performed with the non jealous girl increases jealousy score in the jealous sister
# when scores get high enough, jealous sister may approach MC looking for sex or force satisfaction.
# Possibly add an option to convince a girl to stop being so jealous

# Must be initialized after girlfriend_role_enhanced, which is init 2
init 3 python:
    def jealous_sister_on_turn(person):
        if len(person.jealous_witness_publix_sex_list()) > 0:
            the_score = 1
            for act in person.jealous_witness_publix_sex_list():
                if jealous_act_get_score(act) > the_score:
                    the_score = jealous_act_get_score(act)
            jealous_string = "You were fooling around in front of everybody at " + person.location.formal_name + " !"
            person.add_jealous_event(jealous_string, the_score)
            person.event_triggers_dict["jealous_public_act"] = []
        return

    def jealous_sister_on_day(person): #Use this function to determine if she is going to act on jealous score. also can check for date events here.
        return

    def jealous_act_get_score(the_act):
        if the_act == "foreplay":
            return 1
        elif the_act == "oral":
            return 2
        elif the_act == "anal":
            return 4
        else:
            return 3    #Use vaginal as the default. Jealous sister assumes you are fucking if she doesn't know the act


############ Jealous sister implementation ###############
# NOTE: Please read notes before modifying code.
# Jealous score is affected by and changed by witnessing or infering sexual encounters with the person she is jealous of.
# When jealous person sees or infers a sexual act, add a tuple to the list that contains a description of the act and the type of the act.
# Act description is called when jealous person tells you they know about doing XYZ with person.
# type of act is used so jealous person knows what they need in order to be given the same or similar treatment, EG: you fucked her, fuck me, she blew you, now eat me, etc.
# When a jealous person is made whole and is no longer jealous, reset the list
# Make sure all jealous acts can be run on people EVEN WITHOUT THE ROLE and exits appropriately because we may not always be able to test and see if someone should be jealous.

    def add_jealous_event(self, the_description, the_act):  #Add the tuple to the list and add to her jealousy score
        if is_jealous_sister(self):
            self.event_triggers_dict["jealous_list"].append([the_description, the_act])
            self.jealous_change_score(jealous_act_get_score(the_act))
        return

    Person.add_jealous_event = add_jealous_event

    def get_jealous_description(self):
        if is_jealous_sister(self):
            this_tuple = self.get_jealous_list()[-1]
            return this_tuple[0]
        return "I'm not jealous of anyone right now, I just want to fuck!"

    Person.get_jealous_description = get_jealous_description

    def get_jealous_act(self):
        if is_jealous_sister(self):
            return self.event_triggers_dict.get("jealous_list", [("", "vaginal")])[-1][1]
        return "vaginal"

    Person.get_jealous_act = get_jealous_act

    def reset_jealous_list(self):
        self.event_triggers_dict["jealous_list"] = []
        return

    Person.reset_jealous_list = reset_jealous_list

    def get_jealous_list(self):
        return self.event_triggers_dict.get("jealous_list", [("", "")])

    Person.get_jealous_list = get_jealous_list

    def jealous_score(self):
        return self.event_triggers_dict.get("jealous_score", 0)

    Person.jealous_score = jealous_score

    def jealous_score_reset(self):
        self.event_triggers_dict["jealous_score"] = 0
        return
    Person.jealous_score_reset = jealous_score_reset

    def jealous_change_score(self, the_score):
        self.event_triggers_dict["jealous_score"] = self.event_triggers_dict.get("jealous_score", 0) + the_score
        return

    Person.jealous_change_score = jealous_change_score

    def reset_all_jealousy(self):
        self.reset_jealous_list()
        self.jealous_score_reset()
        self.event_triggers_dict["jealous_public_act"] = []
        #TODO as we make mandatory events using jealousy, probably clear them out here
        return

    Person.reset_all_jealousy = reset_all_jealousy

    def jealous_witness_public_sex(self, the_act):
        self.event_triggers_dict["jealous_public_act"].append(the_act)
        return

    Person.jealous_witness_public_sex = jealous_witness_public_sex

    def jealous_witness_publix_sex_list(self):
        return self.event_triggers_dict.get("jealous_public_act", [])

    Person.jealous_witness_publix_sex_list = jealous_witness_publix_sex_list

    def jealous_sister_get_target_ident(self):
        return self.event_triggers_dict.get("jealous_target", None)

    Person.jealous_sister_get_target_ident = jealous_sister_get_target_ident

    def jealous_sister_get_revenge_tuple(self):   #Use a combination of her sluttiness and what acts she has witnessed to determine how she settles the score.
        target_score = 0
        #TODO use specific act scores so we can take opnions into account
        if self.sluttiness <= 20: #Look for foreplay events.
            target_score = 1
        elif self.sluttiness <= 40:
            target_score = 2
        elif self.sluttiness <= 60:
            target_score = 3
        else:
            target_score = 4

        for i in range(len(self.get_jealous_list()) - 1, -1, -1): #Iterate through the list backwards until we find a matching event for her to get revenge for.
            if self.get_jealous_list()[i][1] == target_score:
                return self.get_jealous_list()[i]
        # No matching event, so we just return the most recent event.
        return  self.get_jealous_list()[-1]

    Person.jealous_sister_get_revenge_tuple = jealous_sister_get_revenge_tuple

    jealous_sister_role = Role("Jealous sister", [], hidden = True,  on_turn = jealous_sister_on_turn, on_move = None, on_day = jealous_sister_on_day)

    def assign_jealous_sister_role(person, the_target):
        person.add_role(jealous_sister_role)
        person.reset_all_jealousy()
        person.event_triggers_dict["jealous_target"] = [the_target.identifier]
        return

    def is_jealous_sister(person):
        return person.has_role(jealous_sister_role)

    def get_jealous_sister(person, slut_requirement = 0):
        # May have multiple jealous sisters. Only grabs the first available one for consistency.
        for relation in town_relationships.get_relationship_list(person, types = "Sister"):
            sister = relation.get_other_person(person)
            if is_jealous_sister(sister) and sister.effective_sluttiness() >= slut_requirement:
                return sister
        return None

    def girlfriend_wakeup_jealous_sister_requirement(the_person):
        sister = get_jealous_sister(the_person, slut_requirement = 60)
        if sister is None:
            return False
        return (mc.location == the_person.home
            and the_person.location == the_person.home
            and sister.location == the_person.home
        )

    girlfriend_wakeup_jealous_sister = Action("Jealous wakeup", girlfriend_wakeup_jealous_sister_requirement, "girlfriend_wakeup_jealous_sister_label")
    girlfriend_morning_action_list.append(girlfriend_wakeup_jealous_sister)


label girlfriend_wakeup_jealous_sister_label(the_person):
    $ jealous_sister = get_jealous_sister(the_person, slut_requirement = 60)

    the_person "I'm gonna hop in the shower. Try not to miss me too much while I'm in there okay?"
    mc.name "Of course."
    $ the_person.draw_person(position = "back_peek")
    "[the_person.title] hops out of bed and heads to the shower. She stops at the door, then turns back and blows you a kiss."
    $ mc.change_locked_clarity(20)
    $ clear_scene()
    "[the_person.possessive_title] disappears behind the door as she closes it behind her. You can hear the shower turn on and you start to drift off to sleep again."
    "..."
    "You don't hear her come in, but the weight on the bed shifts. You open your eyes and see [jealous_sister.title], climbing on top of you."
    $ jealous_sister.outfit.strip_to_vagina()
    $ jealous_sister.draw_person(position = "cowgirl")
    "Her lower half is naked, and she straddles your hips with her cunt pressed against your rapidly hardening cock."
    "You start to say something, but [jealous_sister.fname] puts a finger on your lips."
    jealous_sister "Shhhh, if we're quiet, she'll never even know."
    $ mc.change_locked_clarity(30)
    "She leans forward and replaces her finger with her lips. She kisses you hungrily, making her need for you known."
    "Without breaking the kiss, she reaches down between you and grabs your dick, pointing it up. A quick movement of her hips, and your manhood slips inside of her."
    call get_fucked(jealous_sister, the_goal = "get off", start_position = cowgirl, skip_intro = True) from _call_get_fucked_jealous_sister_special_wakeup_01
    "As you are both recovering, you suddenly hear the water in the shower stop. [jealous_sister.possessive_title] quickly springs up, and quietly slips out the door, leaving you alone in [the_person.title]'s bed."
    $ clear_scene()
    "You take a few moments to make sure you are presentable. You don't want [the_person.title] to get suspicious... Soon the bathroom door opens."
    $ apply_towel_outfit(the_person)
    $ the_person.draw_person()
    "[the_person.title] walks in, wrapped in a towel."
    the_person "Mmm, that felt good. Do you want to shower now?"
    mc.name "No thanks, I'd probably better head out."
    the_person "Hmm, okay. Thanks for coming over last night... It was nice."
    $ clear_scene()
    "You get yourself dressed and say goodbye. You step out of [the_person.title]'s room and into the hall."
    $ jealous_sister.planned_outfit = jealous_sister.decide_on_outfit() # choose a new outfit for the day
    $ jealous_sister.apply_planned_outfit()
    $ jealous_sister.draw_person(position = "sitting")
    $ her_hallway.show_background()
    "As you walk to the door, you see [jealous_sister.title] at the table, having a cup of coffee and some toast."
    jealous_sister "Bye [jealous_sister.mc_title], hope you had a good time..."
    "She gives you a wink."
    mc.name "I definitely did. Take care [jealous_sister.title]."
    $ mc.change_locked_clarity(10)
    "You walk out the front door. Things in that place are crazy..."
    $ jealous_sister.reset_all_jealousy()
    $ the_person.planned_outfit = the_person.decide_on_outfit() # choose a new outfit for the day
    $ the_person.apply_planned_outfit()
    $ jealous_sister = None
    return
