init -1 python:
    def start_exhibition_fetish_quest(person):
        if not is_breeding_fetish_unlocked():
            return False
        if person.has_started_exhibition_fetish:
            return False
        if person.has_taboo(["sucking_cock", "vaginal_sex"]):
            return False

        if person.get_opinion_score("public sex") < 2 \
            or person.sex_skills["Oral"] < 4 \
            or person.sex_skills["Vaginal"] < 4 \
            or person.sex_skills["Anal"] < 4 \
            or person.sluttiness < 70:
            return False

        if renpy.random.randint(0,100) > fetish_serum_roll_fetish_chance(FETISH_EXHIBITION_OPINION_LIST, person):
            return False

        return False #None of them are written yet

init 1 python:
    #Requirement functions
    def exhibition_fetish_employee_intro_requirement():
        if time_of_day == 3:
            if mc.business.is_open_for_business:
                if mc.is_at_work:
                    return True
        return False


    def exhibition_fetish_family_intro_requirement():
        if the_person.is_home:
            if the_person.location.person_count == 1: #She is alone in her bedroom
                return True
        return False

    def exhibition_fetish_generic_intro_requirement(the_person):
        if the_person.location != the_person.home:
            return True
        return False

    def exhibition_fetish_mom_intro_requirement():
        return False

    def exhibition_fetish_lily_intro_requirement():
        return False

    def exhibition_fetish_rebecca_intro_requirement():
        return False

    def exhibition_fetish_gabrielle_intro_requirement():
        return False

    def exhibition_fetish_stephanie_intro_requirement():
        return False

    def exhibition_fetish_alex_intro_requirement():
        return False

    def exhibition_fetish_nora_intro_requirement():
        return False

    def exhibition_fetish_emily_intro_requirement():
        return False

    def exhibition_fetish_christina_intro_requirement():
        return False

    def exhibition_fetish_starbuck_intro_requirement():
        return False

    def exhibition_fetish_sarah_intro_requirement():

        return False

    def exhibition_fetish_ophelia_intro_requirement():
        return False

    def exhibition_fetish_candace_intro_requirement():
        return False

    def exhibition_fetish_dawn_intro_requirement():
        return False

    def exhibition_fetish_erica_intro_requirement():
        return False

    def exhibition_fetish_ashley_intro_requirement():
        return False

init 2 python: #Other exhibition fetish related python code

    pass

init 50 python:
    def get_exhibition_fetish_unique_dialogue_list():
        exhibition_list = [sarah]

        return exhibition_list

    def debug_set_stats_for_exhibition_fetish_mins(the_person):
        the_person.situational_sluttiness = {} #A dict that stores a "situation" string and the corresponding amount it is contributing to the girls sluttiness.
        the_person.situational_obedience = {}
        the_person.arousal = 0
        the_person.energy = the_person.max_energy
        the_person.max_opinion_score("anal sex")
        the_person.sluttiness = 70
        the_person.sluttiness = 70
        the_person.obedience = 0
        the_person.happiness = 100
        the_person.love = 0
        return

    def abort_exhibition_fetish_intro(the_person): #Use this function to exit a anal fetish scene for whatever reason (something fails, MC choice, etc.)
        the_person.event_triggers_dict["exhibition_fetish_start"] = False
        the_person.remove_role(exhibition_fetish_role)
### Function labels

# Fetish Labels
label exhibition_fetish_employee_intro_label(the_person):
    return False

label exhibition_fetish_family_intro_label(the_person):
    return False

label exhibition_fetish_generic_intro_label(the_person):
    return False

label exhibition_fetish_mom_intro_label():
    return False

label exhibition_fetish_lily_intro_label():
    return False

label exhibition_fetish_rebecca_intro_label():
    return False

label exhibition_fetish_gabrielle_intro_label():
    return False

label exhibition_fetish_stephanie_intro_label():
    return False

label exhibition_fetish_alex_intro_label():
    return False

label exhibition_fetish_nora_intro_label():
    return False

label exhibition_fetish_emily_intro_label():
    return False

label exhibition_fetish_christina_intro_label():
    return False

label exhibition_fetish_starbuck_intro_label():
    return False

label exhibition_fetish_sarah_intro_label():
    $ the_person = sarah
    "It's another Wednesday morning. The girls are starting to arrive for work and getting set up for the day."
    "You always enjoy when the girls get there in the morning. You check out some of their outfits, not so subtly, as they arrive."
    "You are just starting to think about calling one to the office for a quickie when someone interrupts your thoughts..."
    the_person "Ahem..."
    $ the_person.draw_person()
    mc.name "Ah, good morning [the_person.title]."
    the_person "Good morning. I umm, noticed you were checking out some of the employees..."
    mc.name "Ah, yes I was."
    the_person "I try to take care of your urges for you at the Monday meetings..."
    mc.name "Well, maybe..."
    the_person "Do you need me to take care of you again? I know it's hump day... I could do it right here?"
    "You look around. Several girls have already sat down at their desks and begun their work."
    "You look back at [the_person.possessive_title]. Is she blushing?"
    "You've been testing Social Sexual Proclivity Nanobots quite a bit on her lately. Is she doing this BECAUSE all the other girls are here?"
    "You reply to her in a voice that is louder than necessary, making sure all the girls around you hear it."
    mc.name "Yes [the_person.title]. Why don't you get on your knees and take care of it for me."
    $ the_person.change_happiness(3)
    the_person "Yes sir!"
    $ the_person.draw_person(position = "blowjob")
    "[the_person.possessive_title] gleefully gets down on her knees and pulls down your zipper. After pulling your cock out, she smiles up at you, then licks the tip."
    "You can hear murmurs from some of the girls around you, but it doesn't seem to phase her. If anything, she seems to be emboldened..."

    return

label exhibition_fetish_ophelia_intro_label():
    return False

label exhibition_fetish_candace_intro_label():
    return False

label exhibition_fetish_dawn_intro_label():
    return False

label exhibition_fetish_erica_intro_label():
    return False

label exhibition_fetish_ashley_intro_label():
    return False

label unit_test_exhibition_fetish_intro():

    "Generic intros"
    $ debug_set_stats_for_exhibition_fetish_mins(mom)
    "Method: exhibition_fetish_family_intro_label"
    call exhibition_fetish_family_intro_label(mom) from _unit_test_exhibition_fetish_intro_01
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(starbuck)
    "Method: exhibition_fetish_generic_intro_label"
    call exhibition_fetish_generic_intro_label(starbuck) from _unit_test_exhibition_fetish_intro_02
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(stephanie)
    "Method: exhibition_fetish_employee_intro_label"
    call  exhibition_fetish_employee_intro_label(stephanie) from _unit_test_exhibition_fetish_intro_03
    $ mc.energy = mc.max_energy

    $ stephanie.remove_role(exhibition_fetish_role)
    $ mom.remove_role(exhibition_fetish_role)
    $ starbuck.remove_role(exhibition_fetish_role)

    "Unique intros"
    $ debug_set_stats_for_exhibition_fetish_mins(mom)
    "Method: exhibition_fetish_mom_intro_label"
    call exhibition_fetish_mom_intro_label() from _unit_test_exhibition_fetish_intro_04
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(lily)
    "Method: exhibition_fetish_lily_intro_label"
    call exhibition_fetish_lily_intro_label() from _unit_test_exhibition_fetish_intro_05
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(aunt)
    "Method: exhibition_fetish_rebecca_intro_label"
    call exhibition_fetish_rebecca_intro_label() from _unit_test_exhibition_fetish_intro_06
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(cousin)
    "Method: exhibition_fetish_gabrielle_intro_label"
    call exhibition_fetish_gabrielle_intro_label() from _unit_test_exhibition_fetish_intro_07
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(stephanie)
    "Method: exhibition_fetish_stephanie_intro_label"
    call exhibition_fetish_stephanie_intro_label() from _unit_test_exhibition_fetish_intro_08
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(alexia)
    "Method: exhibition_fetish_alex_intro_label"
    call exhibition_fetish_alex_intro_label() from _unit_test_exhibition_fetish_intro_09
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(nora)
    "Method: exhibition_fetish_nora_intro_label"
    call exhibition_fetish_nora_intro_label() from _unit_test_exhibition_fetish_intro_10
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(emily)
    "Method: exhibition_fetish_emily_intro_label"
    call exhibition_fetish_emily_intro_label() from _unit_test_exhibition_fetish_intro_11
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(christina)
    "Method: exhibition_fetish_christina_intro_label"
    call exhibition_fetish_christina_intro_label() from _unit_test_exhibition_fetish_intro_12
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(starbuck)
    "Method: exhibition_fetish_starbuck_intro_label"
    call exhibition_fetish_starbuck_intro_label() from _unit_test_exhibition_fetish_intro_13
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(sarah)
    "Method: exhibition_fetish_sarah_intro_label"
    call exhibition_fetish_sarah_intro_label() from _unit_test_exhibition_fetish_intro_14
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(salon_manager)
    "Method: exhibition_fetish_ophelia_intro_label"
    call exhibition_fetish_ophelia_intro_label() from _unit_test_exhibition_fetish_intro_15
    $ mc.energy = mc.max_energy

    $ create_debug_candace()
    $ debug_set_stats_for_exhibition_fetish_mins(candace)
    "Method: exhibition_fetish_candace_intro_label"
    call exhibition_fetish_candace_intro_label() from _unit_test_exhibition_fetish_intro_16
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(dawn)
    "Method: exhibition_fetish_dawn_intro_label"
    call exhibition_fetish_dawn_intro_label() from _unit_test_exhibition_fetish_intro_17
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(erica)
    "Method: exhibition_fetish_erica_intro_label"
    call exhibition_fetish_erica_intro_label() from _unit_test_exhibition_fetish_intro_18
    $ mc.energy = mc.max_energy

    $ debug_set_stats_for_exhibition_fetish_mins(ashley)
    "Method: exhibition_fetish_ashley_intro_label"
    call exhibition_fetish_ashley_intro_label() from _unit_test_exhibition_fetish_intro_19
    $ mc.energy = mc.max_energy

    return
