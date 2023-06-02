init 5 python:
    ####################################################
    # Activate text modifier for person:			   #
    # the_person.text_modifiers.append( maori_belle) #
    ####################################################


    # word replacer (no special chars like - or ')
    maori_dict = {
        "daughter": "tamāhine",
        "sacred": "tapu",
        "woman": "wahine"
    }

    # letter replace (in word)
    maori_replace_dict = {
        "wh": "f",
    }

    # word group replacer
    maori_word_group_dict = {
        "thank you ": "tēnā koe"
    }

    def maori_accent(person, what):
        return word_replace(letter_replacer(word_group_replacer(what,  maori_word_group_dict),  maori_replace_dict),  maori_dict)
