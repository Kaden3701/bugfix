#The very first Mc serum trait. Regenerates extra energy for the MC every turn.

init 2 python:
    mc_serum_feat_orgasm_control = MC_Serum_Trait("Serum: Feat of Orgasm Control",
    "Pleasure Center Stimulator",
    "physical",
    [perk_feat_orgasm_control_small, perk_feat_orgasm_control_med, perk_feat_orgasm_control_large],
    [perk_feat_orgasm_control_advance_req_01],
    "perk_feat_orgasm_control_upg_label",
    upg_string = "Master the Mind Control Agent trait to upgrade this serum formula.",
    on_apply = perk_feat_orgasm_control_on_apply,
    on_remove = perk_feat_orgasm_control_on_remove)

    list_of_mc_traits.append(mc_serum_feat_orgasm_control)

init 1 python:  #Associated Perks
    def perk_feat_orgasm_control_on_apply():
        mc.business.event_triggers_dict['orgasm_control_active'] = True
        return

    def perk_feat_orgasm_control_on_remove():
        mc.business.event_triggers_dict['orgasm_control_active'] = False
        return

    def perk_feat_orgasm_control_small():
        return Ability_Perk(description = "During sex, you can hold off orgasm indefinitely, but orgasms cost 20 energy.", usable = False)

    def perk_feat_orgasm_control_med():
        return Ability_Perk(description = "During sex, cum early or hold off indefinitely, but orgasms cost 20 energy.", usable = False)

    def perk_feat_orgasm_control_large():
        return Ability_Perk(description = "During sex, cum early or hold off indefinitely, and once per day you can quickly orgasm during a conversation before the other person can react. Orgasms cost 20 energy.", usable = False)

    def perk_feat_orgasm_control_advance_req_01():
        the_serum = find_serum_trait_by_name("Mind Control Agent")
        if the_serum.mastery_level >= 5:
            return True
        return False

label perk_feat_orgasm_control_upg_label(the_person):
    the_person "Research with the Mind Control Agent serum trait has yielded states in some test subjects that is borderline hypnosis."
    the_person "By adding some of those agents to the Orgasm Control serum, you should be able to tap into a borderline hypnotic state, gaining incredible control over your orgasms."
    mc.name "That sounds very useful. I'll give it a try when I have the chance."
    return

label climax_check_orgasm_control():
    "Your pleasure is growing. You could cum now, if you decide to."
    menu:
        "Cum now":
            "You focus on the pleasure and let yourself go."
            $ mc.change_energy(-20)
            $ mc.change_arousal(mc.max_arousal - mc.arousal + 10)
            return True
        "Delay orgasm":
            "You put off your orgasm for a bit longer."
            $ mc.change_arousal(mc.max_arousal - mc.arousal - 10)
            return False

label climax_check_double_orgasm_control_label():
    "It looks like she is getting ready to cum. Do you want cum with her?"
    menu:
        "Cum now":
            "You focus on the pleasure and let yourself go."
            $ mc.change_energy(-20)
            $ mc.change_arousal(mc.max_arousal - mc.arousal + 10)
            return True
        "Delay orgasm":
            "You put off your orgasm for a bit longer."
            $ mc.change_arousal(mc.max_arousal - mc.arousal - 10)
            return False

label climax_check_orgasm_control_in_convo_label(the_person):
    $ cum_location = None
    $ mc.business.set_event_day("mc_orgasm_in_convo_serum")
    "In the middle of your conversation with [the_person.possessive_title], you decide to take advantage of your superior orgasm control to unload on her."
    "You quickly whip out your dick and stroke yourelf to an orgasm."
    #First, determine if she cooperates or just stands there.
    if mc_serum_aura_obedience.is_active:
        "[the_person.title] quickly realizes what you are doing. However, due to your Aura of Compliance, she just looks at you, waiting for you to tell her what to do."
        "You can order her to take your cum how you want, but when you finish she might not appreciate it..."
        menu:
            "On her face":
                mc.name "On your knees, quick!"
                $ cum_location = "face"
                $ the_person.draw_person(position = "blowjob")
                "[the_person.title] drops to her knees and waits for you. A couple more strokes, and you start cumming."
                $ the_person.cum_on_face()
                $ the_person.draw_person(position = "blowjob")
                # clarity release
                "You pump out several strands of cum onto [the_person.possessive_title]'s face while she waits, obediently."
                "When you finish, she looks up at you."
            "On her tits":
                mc.name "On your knees, I want to finish on your tits!"
                $ cum_location = "tits"
                $ the_person.draw_person(position = "blowjob")
                if mc_serum_aura_obedience.trait_tier >= 2 and not the_person.tits_available:
                    mc.name "Get em out, quick!"
                    $ the_person.strip_to_tits(position = "blowjob", prefer_half_off = True)
                    "[the_person.title] quickly pulls her tits out."
                "A couple more strokes, and you start cumming."
                $ the_person.cum_on_tits()
                $ the_person.draw_person(position = "blowjob")
                "You pump out several strands of cum onto [the_person.possessive_title]'s tits while she waits, obediently."
                "When you finish, she looks up at you."
            "Bend her over" if mc_serum_aura_obedience.trait_tier >= 2:
                mc.name "Turn around and bend over."
                $ cum_location = "ass"
                $ the_person.draw_person(position = "standing_doggy")
                if mc_serum_aura_obedience.trait_tier >= 2 and not the_person.vagina_available:
                    "After she bends over, you quickly pull her clothes out of the way."
                    $ the_person.strip_to_vagina(prefer_half_off = True, visible_enough = True, position = "standing_doggy")
                    "You point your dick at her exposed ass and continue stroking yourself."
                "A couple more strokes, and you start cumming."
                $ the_person.cum_on_ass()
                $ the_person.draw_person(position = "standing_doggy")
                "You pump out several strands of cum onto [the_person.possessive_title]'s ass while she waits, obediently."
                "When you finish, she looks back at you."
            "Bend her over\n{color=#ff0000}{size=18}Requires Tier 2 Aura{/size}{/color} (disabled)" if mc_serum_aura_obedience.trait_tier < 2:
                pass
            "Have her swallow" if mc_serum_aura_obedience.trait_tier >= 3:
                mc.name "On your knees, I want you to swallow it all."
                $ cum_location = "mouth"
                $ the_person.draw_person(position = "blowjob")
                "[the_person.possessive_title] obediently drops to her knees and opens her mouth."
                "You give yourself a couple final strokes, then put the tip in her mouth as you start to cum."
                $ the_person.cum_in_mouth()
                $ the_person.draw_person(position = "blowjob")
                "[the_person.title]'s cheeks puff out a bit with the quantity of cum you unload."
                mc.name "That's it. Now swallow."
                $ play_swallow_sound()
                "[the_person.possessive_title] obediently gulps your cum down, then looks up at you."
            "Have her swallow\n{color=#ff0000}{size=18}Requires Tier 3 Aura{/size}{/color} (disabled)" if mc_serum_aura_obedience.trait_tier < 3:
                pass
    else:   #If no applicable auras occur use sluttiness to determine her immeidiate reaction.
        if the_person.sluttiness < 40:
            $ cum_location = "stomach"
            "[the_person.possessive_title] just stands there in shock as you quickly jack yourself off."
            "You give yourself a final couple of strokes and start to cum on her stomach."
            $ the_person.cum_on_stomach()
            $ the_person.draw_person()
            "[the_person.title] just watches in shock as you shoot strand after strand onto her stomach."
            "When you finish, she looks back at you and your eyes meet."
        elif the_person.has_cum_fetish:
            $ cum_location = "mouth"
            the_person "Oh fuck wait!"
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] quickly drops to her knees. She slaps your hand out of the way and opens her mouth."
            "She quickly pushes her face down on your cock, forcing it down her throat. With a couple quick strokes, you start to cum."
            $ the_person.cum_in_mouth()
            $ the_person.draw_person(position = "blowjob")
            "[the_person.title] takes your load straight down her throat, moaning all around your cock with every spurt."
            "[the_person.title]'s cum addiction takes over as she milks the last few drops of your cum."
            "Once finished, she pops off your cock and looks up at you."
        else:
            $ cum_location = "face"
            the_person "Whoa! Right now? Let me..."
            $ the_person.draw_person(position = "blowjob")
            "[the_person.possessive_title] gets on her knees, but before she can do anything you start to unload all over her face."
            $ the_person.cum_on_face()
            $ the_person.draw_person(position = "blowjob")
            # clarity release
            "You pump out several strands of cum onto [the_person.possessive_title]'s surprised face."
            "When you finish, she looks up at you."

    #How she reacts to the aftermath.
    #First, determine if we have a cum related serum that will dictate her response.
    if mc_serum_cum_obedience.is_active:  #Obedience cum, she may have even been put into a trance by it.
        if cum_location != "stomach":
            $ the_person.draw_person(position = "stand3")
            "[the_person.title] slowly stands up."
        else:
            "[the_person.title] is a little unsteady but stays standing."
        if the_person.is_in_trance:
            "Your serum effected cum and her trance has left her in a very pliable state."
            call do_training(the_person) from _call_do_training_orgasm_control_01
        "She doesn't say a word, but just waits for you to tell her what to do next."
    else:   #No associated serums, have her react naturally
        if the_person.sluttiness >= 40: #She's okay with it, but surprised
            the_person "Wow... that was so... sudden!"
            mc.name "Yeah... sorry I had some pent up stress."
            the_person "Right... stress... of course..."
            "[the_person.title] laughs to herself."
            $ the_person.change_obedience(1)
            $ the_person.change_love(-1)
        elif the_person.love >= 60 and not the_person.is_family:
            the_person "Wow... I... I could have taken care of that for you..."
            if len(mc.location.people) > 1:
                "[the_person.title] quickly looks around the room. She whispers to you in a hushed tone."
                the_person "Somewhere more private...!"
            else:
                the_person "Doing something we could have both enjoyed."
            mc.name "Sorry, I had some pent up stress that needed taken care of right away."
            the_person "Geesh, you are crazy..."
            $ the_person.change_obedience(1)
            $ the_person.change_slut(1, 50)
        elif the_person.obedience > 150:
            the_person "Is that all [the_person.mc_title]?"
            mc.name "Yes, that will be all for now."
            the_person "Okay..."
            $ the_person.change_obedience(1)
            $ the_person.change_slut(1, 50)
        else:
            the_person "What... the fuck!?!"
            the_person "Are you kidding me? You can't just... AHH"
            $ the_person.draw_person(position = "walking_away")
            "[the_person.title] quickly stands up and runs away. They did not seem to be happy about it what just happened..."
            $ the_person.change_love(-5)
            $ the_person.change_happiness(-5)
            $ clear_scene()
            $ the_person.apply_planned_outfit()
            jump game_loop
        "[the_person.possessive_title] quickly cleans herself up."
        $ the_person.apply_planned_outfit()
    $ the_person.draw_person(position = the_person.idle_pose)
    return

init 1 python:
    def climax_check_double_orgasm_control():
        renpy.call("climax_check_double_orgasm_control_label")
        return _return

init 2 python:
    def climax_check_orgasm_control_in_convo_requirement(person):
        if not mc_serum_feat_orgasm_control.is_active:
            return False
        if mc.business.days_since_event("mc_orgasm_in_convo_serum") < 1:
            return "Done too recently"
        if mc.energy < 20:
            return "Requires: 20{image=gui/extra_images/energy_token.png}"
        if mc_serum_feat_orgasm_control.is_active:
            if mc_serum_feat_orgasm_control.trait_tier < 3:
                return "Orgasm Control serum tier too low"
            return True
        return False

init 5 python:
    climax_check_orgasm_control_in_convo_action = Action("Cum on her   {color=#FFFF00}-20{/color} {image=gui/extra_images/energy_token.png}\n Serum: Orgasm Control", climax_check_orgasm_control_in_convo_requirement, "climax_check_orgasm_control_in_convo_label",
        menu_tooltip = "Use your superior orgasm control to whip out your cock and cum as fast as possible.")
    chat_actions.append(climax_check_orgasm_control_in_convo_action)
