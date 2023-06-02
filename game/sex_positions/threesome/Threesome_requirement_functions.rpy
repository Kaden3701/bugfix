#This is a dedicated rpy file for frequently used threesome requirement functions.
#list here for easy lookup later and so I don't have to write a new requirement function for every single positiona and variant


init -1 python:
    def requirement_both_vagina_available(the_person_one, the_person_two):
        if the_person_one.vagina_available:
            if the_person_two.vagina_available:
                return True
        return False

    def requirement_test(the_person_one, the_person_two):
        return True

    def requirement_hard_both_vagina_available(the_person_one, the_person_two):
        if mc.recently_orgasmed:
            return False
        if the_person_one.vagina_available:
            if the_person_two.vagina_available:
                return True
        return False
    def requirement_always_true(the_person_one, the_person_two):
        return True

    def requirement_disable_position(the_person_one, the_person_two):
        return False

    def requirement_hard(the_person_one, the_person_two):
        if mc.recently_orgasmed:
            return False
        else:
            return True

    def requirement_hard_both_vagina_both_like_anal(the_person_one, the_person_two):
        if mc.recently_orgasmed:
            return False
        if the_person_one.get_opinion_score("anal sex") < 0:
            return False
        if the_person_two.get_opinion_score("anal sex") < 0:
            return False
        if the_person_one.vagina_available:
            if the_person_two.vagina_available:
                return True
        return False

    def requirement_hard_both_vagina_male_strapon(the_person_one, the_person_two):
        if mc.recently_orgasmed:
            return False
        if the_person_one.vagina_available:
            if the_person_two.vagina_available:
                if perk_system.has_item_perk("Male Strapon"):
                    return True
        return False
