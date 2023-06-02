init 720 python:              #Because Vren Init personality functionns at 1300

    def sakari_titles(person):
        valid_titles = []
        valid_titles.append(person.name)

        return valid_titles

    def sakari_possessive_titles(person):
        valid_possessive_titles = [person.title]
        return valid_possessive_titles
    def sakari_player_titles(person):
        return mc.name

    sakari_personality = Personality("sakari", default_prefix = relaxed_personality.default_prefix,
    common_likes = ["skirts", "dresses", "the weekend", "the colour red", "makeup", "flirting", "high heels"],
    common_sexy_likes = ["doggy style sex", "giving blowjobs", "vaginal sex", "public sex", "lingerie", "skimpy outfits", "being submissive", "drinking cum", "cheating on men"],
    common_dislikes = ["polyamory", "pants", "working", "the colour yellow", "conservative outfits", "sports"],
    common_sexy_dislikes = ["taking control", "giving handjobs", "not wearing anything"],
    titles_function = sakari_titles, possessive_titles_function = sakari_possessive_titles, player_titles_function = sakari_player_titles)
