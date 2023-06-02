#This file contains code for a generic bar date.
#For now, start moving bar date related functions here. No generic bar date has been written yet but it is TODO


init -1 python:
    def bar_date_requirement():
        return False







label bar_date_arcade_round_label(the_person, skill_modifier = 0):
    $ opponent_skill = the_person.focus + the_person.sex_skills["Foreplay"] + skill_modifier
    $ mc_skill = mc.focus + mc.sex_skills["Foreplay"]
    "In this scene, you square off against [the_person.title] playing the legendary arcade game Super Street Kombat 2 Turbo."
    "The only problem is, Starbuck hasn't written this stuff yet!"
    "You might have the opportunity to distract her with tickling, smacking her ass, or more."
    "It will be included in a future bar date update... until then..."
    if opponent_skill > mc_skill:
        "[the_person.possessive_title] wins the match easily!"
        return False
    else:
        "You beat [the_person.title] easily!"
        return True
    return False
