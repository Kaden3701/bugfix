init:   #Great for in showers, dressing rooms, etc.
    python:
        standing_cunnilingus = Position(name = "Standing Cunnilingus", slut_requirement = 40, slut_cap = 80, requires_hard = False, requires_large_tits = False,
            position_tag = "against_wall", requires_location = "Lean", requires_clothing = "Vagina", skill_tag = "Oral",
            girl_arousal = 15, girl_energy = 3,
            guy_arousal = 3, guy_energy = 12,
            connections = [],
            intro = "intro_standing_cunnilingus",
            scenes = ["scene_standing_cunnilingus_1","scene_standing_cunnilingus_2"],
            outro = "outro_standing_cunnilingus",
            transition_default = "transition_default_standing_cunnilingus",
            strip_description = "strip_standing_cunnilingus", strip_ask_description = "strip_ask_standing_cunnilingus",
            orgasm_description = "orgasm_standing_cunnilingus",
            taboo_break_description = "taboo_break_standing_cunnilingus",
            verb = "lick",
            opinion_tags = ["getting head", "taking control", "get off"], record_class = "Cunnilingus",
            default_animation = blowjob_bob,
            associated_taboo = "licking_pussy")

        list_of_girl_positions.append(standing_cunnilingus)

        standing_cunnilingus.girl_outro = "GIC_outro_standing_cunnilingus"

# init 1:
#     python:
#         cunnilingus.link_positions(other, "transition_label") #If there are transitions they go here

label intro_standing_cunnilingus(the_girl, the_location, the_object):
    "[the_girl.title] leans against the [the_object.name]. When you come close to her, she pushes down on your shoulders."
    $ standing_cunnilingus.redraw_scene(the_girl) #Draw her sitting down.
    the_person "I want you to kiss me for a little bit..."
    "You decide to go with it, for now. You slowly kiss your way down her body. She moans softly when you get close to her groin."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = standing_cunnilingus.position_tag, visible_enough = True, prefer_half_off = True)

    "You lean forward and run your tongue along her slit. She groans as soon as you make contact."
    the_girl "Oh [the_girl.mc_title]..."
    return

label taboo_break_standing_cunnilingus(the_girl, the_location, the_object):  #because this is a girl in charge position only it makes sense to bypass normal taboo break dialogue which usually assumes MC is in charge
    "[the_girl.title] leans against the [the_object.name]. When you come close to her, she pushes down on your shoulders."
    $ standing_cunnilingus.redraw_scene(the_girl)
    mc.name "What are you doing?"
    the_person "I know we've never done this but... I want you to kiss me down there."
    mc.name "Sorry, I don't eat out."
    "Startled, she suddenly she looks at you."
    the_person "Are you serious? I thought you..."
    "You get down on your knees in front of her."
    mc.name "Ha! Just kidding. Mmm, I can't wait to taste your pussy..."
    the_person "Ahh... you scared me there..."
    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = standing_cunnilingus.position_tag, visible_enough = True, prefer_half_off = True)
    "She runs her fingers through your hair as you get closer, her cunt inches from your face."
    "You slide forward and bring your head even closer. [the_girl.possessive_title] takes a sharp breath and turns her head to the side."
    "You bring one hand up to her [the_girl.pubes_description] pussy and spread it open to reveal the tender pink inside."
    the_girl "Come on, do it!"
    "You run your tongue along the length of her slit, tasting her sweet juices."
    the_girl "Oh my god!"
    return

label scene_standing_cunnilingus_1(the_girl, the_location, the_object):
    if the_girl.get_sex_goal() == "hate fuck":
        "[the_girl.title]'s hands are on the back of your head, pulling you against her as she rides you roughly."
        the_girl "That's it, lick my cunt [the_girl.mc_title]."
        $ play_spank_sound()
        "You swing your hand around hard and spank her ass. Her hips involuntarily thrust against you when you strike her."
        $ the_girl.call_dialogue("sex_responses_oral")
        $ the_girl.change_arousal(the_girl.get_opinion_score("getting head"))
    else:
        "[the_girl.title]'s hands are on the back of your head, running her fingers through your hair as you pleasure her."
        "You lick at [the_girl.possessive_title]'s delicate pussy, spreading her lips and sending your tongue inside."
        "She shivers with each touch, obviously enjoying the feeling."
        if the_girl.arousal_perc > 40:
            "Her pussy is dripping wet, filling your mouth with the taste of her juices."
        $ the_girl.call_dialogue("sex_responses_oral")
    return

label scene_standing_cunnilingus_2(the_girl, the_location, the_object):
    "You flick your tongue over [the_girl.possessive_title]'s clit. She gasps and grabs at your shoulders."
    $ the_girl.call_dialogue("sex_responses_oral")
    "You tease the sensitive nub with your tongue, then suck on it gently."
    if the_girl.arousal_perc > 80:
        $ play_moan_sound()
        "Her moans are getting desperate and her hips are bucking against you as you stimulate her."
    "She runs her fingers through your hair and sighs, leaning against the [the_object.name]."
    return

label outro_standing_cunnilingus(the_girl, the_location, the_object): #With low arousal gain this is unlikely to come up much
    $ play_moan_sound()
    "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
    "You touch yourself, stroking your hard cock between your legs while you pleasure her."
    "Finally you've gone too far, pushing yourself to climax."
    "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto the floor."
    $ ClimaxController.manual_clarity_release(climax_type = "masturbation", the_person = the_girl)
    the_girl "Wow, I didn't realize you loved eating pussy so much!"
    return


label transition_default_standing_cunnilingus(the_girl, the_location, the_object):
    "[the_girl.title] leans against the [the_object.name]. When you come close to her, she pushes down on your shoulders."
    $ standing_cunnilingus.redraw_scene(the_girl) #Draw her sitting down.
    the_person "I want you to kiss me for a little bit..."
    "You decide to go with it, for now. You slowly kiss your way down her body. She moans softly when you get close to her groin."
    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = standing_cunnilingus.position_tag, visible_enough = True, prefer_half_off = True)
    "You lean forward and run your tongue along her slit. She groans as soon as you make contact."
    the_girl "Oh [the_girl.mc_title]..."
    return

label strip_standing_cunnilingus(the_girl, the_clothing, the_location, the_object):
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = standing_cunnilingus.position_tag)
    "[the_girl.possessive_title] strips off her [the_clothing.name] while you're eating her out, throwing it to the side."
    return

label strip_ask_standing_cunnilingus(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'm like to take off my [the_clothing.name] if you don't mind."
    menu:
        "Let her strip":
            "You look up from between her legs and nod."
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = standing_cunnilingus.position_tag)
            "She strips out of her [the_clothing.name] and throws it to the side while you move back in and lick at her cunt."
            return True

        "Leave it on":
            "You look up from between her legs and shake your head."
            mc.name "No, I like how you look with it on."
            the_girl "Yeah? Do I look sexy in it? Mmmm..."
            return False

label orgasm_standing_cunnilingus(the_girl, the_location, the_object):
    $ play_moan_sound()
    "You notice [the_girl.possessive_title]'s moans becoming louder, and her legs twitching more noticeably on either side of your head."
    "You speed up your efforts, doing your best to drive her towards her orgasm. She moans and begins to writhe under your skilled tongue."
    $ the_girl.call_dialogue("climax_responses_oral")
    "All at once the tension in her body is unleashed in a series of violent tremors. Her hand grabs the back of your head, pulling you against her."
    "The moment passes and she relaxes. For a moment all she can do is look down at you and pant."
    return

label GIC_outro_standing_cunnilingus(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    #Perhaps an option where she hesitates and you grab her hips and pull her down while you cum.
    if the_goal == "hate fuck" or the_goal == "waste cum":
        $ play_moan_sound()
        "The taste of [the_girl.possessive_title]'s pussy, the sound of her moans, and the subtle twitches of her body drive you crazy."
        "You touch yourself, stroking your hard cock between your legs while you pleasure her."
        "Finally you've gone too far, pushing yourself to climax."
        "You pull your head back and grunt, jerking your cock and blasting out a load of cum onto the floor below [the_girl.title]."
        $ ClimaxController.manual_clarity_release(climax_type = "masturbation", the_person = the_girl)
        the_person "Wow. Just from licking me? What a pathetic waste of cum."
        "It makes a mess, but you finish cumming."
    else:
        $ standing_cunnilingus.call_default_outro(the_girl, the_location, the_object)
