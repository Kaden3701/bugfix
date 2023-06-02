#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_feat_hypnotist = MC_Serum_Trait("Serum: Feat of Hypnotism",
    "Medical Amphetamines",
    "physical",
    [perk_feat_hypnotist_small, perk_feat_hypnotist_med, perk_feat_hypnotist_large],
    [perk_feat_hypnotist_advance_req_01],
    "perk_feat_hypnotist_upg_label",
    upg_string = "Master the Permanent Bimbofication trait to upgrade this serum formula.")

    list_of_mc_traits.append(mc_serum_feat_hypnotist)

init 1 python:  #Associated Perks

    def perk_feat_hypnotist_small():
        return Ability_Perk(description = "You gain the ability to hypnotize a woman into a trance. Costs 30 energy.", usable = False)

    def perk_feat_hypnotist_med():
        return Ability_Perk(description = "You get a 20% discount on trance training and gain the ability to hypnotize a woman into a deep trance. Costs 30 energy.", usable = False)

    def perk_feat_hypnotist_large():
        return Ability_Perk(description = "You get a 40% discount on trance training and gain the ability to hypnotize a woman into a very deep trance. Costs 30 energy.", usable = False)

    def perk_feat_hypnotist_advance_req_01():
        the_serum = find_serum_trait_by_name("Permanent Bimbofication")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_feat_hypnotist_upg_label(the_person):
    the_person "Research with the Permanent Bimbofication serum trait has yielded some significant gains in inducing temporary trances."
    the_person "By stripping out some of the compounds making bimbofication permanent, it makes it easier to subdue a target using hypnosis."
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return

label hypnotize_in_sex_label(the_person, the_position):
    mc.name "Hey, look at me for a second."
    if the_position.position_tag == "doggy" or the_position.position_tag == "standing_doggy":
        "[the_person.title] looks back at you."
    elif the_position.position_tag == "blowjob":
        "[the_person.title] looks up at you."
    else:
        "[the_person.title] looks at you."
    "Using your hypnosis ability, you quickly hypnotize her into a trance."
    $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    if mc_serum_feat_hypnotist.trait_tier > 1:
        "[the_person.possessive_title]'s eyes quickly go blank as she start to go under."
        "With the power of your hypnosis serum, you push her into a deeper trance."
        $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
        if mc_serum_feat_hypnotist.trait_tier > 2:
            "You eyes focus on [the_person.title]'s, while her pupils dialate as she slips farther into your hypnosis."
            "Your ability has driven her even deeper."
            $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    "Now in trance, you can continue [the_position.verbing] her."
    $ mc.change_energy(-30)
    return

label hypnotize_in_convo_label(the_person):
    mc.name "Hey, can I have your attention for a moment?"
    the_person "Sure [the_person.mc_title], what is it?"
    "Using your hypnosis ability, you quickly hypnotize her into a trance."
    $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    if mc_serum_feat_hypnotist.trait_tier > 1:
        "[the_person.possessive_title]'s eyes quickly go blank as she start to go under."
        "With the power of your hypnosis serum, you push her into a deeper trance."
        $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
        if mc_serum_feat_hypnotist.trait_tier > 2:
            "You eyes focus on [the_person.title]'s, while her pupils dialate as she slips farther into your hypnosis."
            "Your ability has driven her even deeper."
            $ the_person.increase_trance(show_dialogue = False, reset_arousal = False, add_to_log = True)
    "Now in trance, you consider if there was anything else you needed from [the_person.title]."
    $ mc.change_energy(-30)
    return


init 2 python:
    def hypnotize_in_convo_requirement(person):
        if not mc_serum_feat_hypnotist.is_active:
            return False
        if mc.energy < 30:
            return "Requires: 30{image=gui/extra_images/energy_token.png}"
        if the_person.is_in_trance:
            return "Already in Trance"
        return True

init 5 python:
    hypnotize_in_convo_action = Action("Hypnotize her   {color=#FFFF00}-30{/color} {image=gui/extra_images/energy_token.png}\n Serum: Hypnotism", hypnotize_in_convo_requirement, "hypnotize_in_convo_label",
        menu_tooltip = "You can utilize your feat of hypnosis serum to put her into a trance.")
    chat_actions.append(hypnotize_in_convo_action)
