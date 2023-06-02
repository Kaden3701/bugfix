#This is a variant on the standing sex up against the wall. In this version, we have the girl's back to us instead of facing us.#

init python:
    facing_wall = Position(name = "Facing Wall", slut_requirement = 70, slut_cap = 90, requires_hard = True, requires_large_tits = False,
        position_tag = "back_peek", requires_location = "Lean", requires_clothing = "Vagina", skill_tag = "Vaginal",
        girl_arousal = 20, girl_energy = 16,
        guy_arousal = 18, guy_energy = 16,
        connections = [],
        intro = "intro_facing_wall",
        scenes = ["scene_facing_wall_1","scene_facing_wall_2"],
        outro = "outro_facing_wall",
        transition_default = "transition_default_facing_wall",
        strip_description = "strip_facing_wall", strip_ask_description = "strip_ask_facing_wall",
        orgasm_description = "orgasm_facing_wall",
        taboo_break_description = "taboo_break_facing_wall",
        verb = "fuck",
        opinion_tags = ["sex standing up", "vaginal sex"], record_class = "Vaginal Sex",
        default_animation = missionary_bob,
        associated_taboo = "vaginal_sex")

    #list_of_positions.append(facing_wall)     #Consider adding later, but for now, transition from the other standing scene

init 1:
    python:
        facing_wall.link_positions_two_way(against_wall, "transition_facing_wall_against_wall", "transition_against_wall_facing_wall")
        #facing_wall.link_positions(against_wall,"transition_facing_wall_against_wall")

label intro_facing_wall(the_girl, the_location, the_object):
    $ facing_wall.redraw_scene(the_girl)
    "You turn [the_girl.possessive_title] so she faces away from you and push her up against the [the_object.name]."

    if not the_girl.vagina_visible:
        "You quickly move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = facing_wall.position_tag, visible_enough = True, prefer_half_off = True)

    "You rub your dick along her slit a few times, first up and down, and then side to side. You line yourself up and begin to push inside of her."
    the_girl "Oh my god..."
    "[the_girl.possessive_title] sighs as you bottom out."
    if the_girl.effective_sluttiness() > 95:
        "She wiggles her ass back and forth a few times, enjoying the familiar feel of fullness you give her when you fuck her."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "[the_girl.mc_title], it feels so good..."
    else:
        "[the_girl.possessive_title] arches her back a bit. She steals a glance back at you while you enjoy the warm, slick grip of her pussy."
    "You put your hands on [the_girl.possessive_title]'s hips and give her a tentative thrust."
    if the_girl.arousal_perc > 60:
        "[the_girl.possessive_title]'s cunt is already slick and wet with arousal. She places on hand on top of yours, encouraging you fuck her."
    else:
        "[the_girl.possessive_title] gives a grunt as you begin to fuck her."
    if the_girl.get_opinion_score("sex standing up") > 0 :
        the_girl "Oh my god, it feels so good to get fucked like this."
        $ the_girl.change_arousal(the_girl.get_opinion_score("sex standing up"))
        $ the_girl.discover_opinion("sex standing up")
    return


    #####POSSIBLY USEFUL OPINIONS######
    #  "sex standing up"
    #  "vaginal sex"
    #  "kissing"
    #  "being fingered"
    #  "showing her ass"
    #  "creampies"
    #  "being covered in cum"
    #  "bareback sex"
    #  "being submissive"
    #  "taking control"

label scene_facing_wall_1(the_girl, the_location, the_object):
    "You grab [the_girl.possessive_title]'s hips and begin thrusting eagerly. Your hips slap against her ass in lewd smacking noises as you fuck her."
    $ the_girl.call_dialogue("sex_responses_vaginal")
    if the_girl.sex_skills["Vaginal"] < 2: #Inexperienced, option to dominate her a bit
        "[the_girl.possessive_title] is getting overwhelmed by the sensation. She is clearly enjoying your fucking but is having a hard time keeping up."
        the_girl "Sorry, I just... you are going so fast!"
        "You pull out then pull her hips back toward you slowly. You consider punishing her for her poor performance... or maybe you could slowly up the pace and talk dirty to her?"
        menu:
            "Punish Her":
                $ play_spank_sound()
                "SMACK"
                "You give [the_girl.possessive_title]'s ass a hard swat. It leaves a clear red handprint on her behind."
                the_girl "Yow!"
                mc.name "Sorry? That's not what I expect from you. Count how many times I spank you. How many times do you think you deserve?"
                if the_girl.get_opinion_score("being submissive") > 0:
                    "[the_girl.possessive_title] quivers at your touch and your words."
                    the_girl "O master, I don't know! Ten? Is ten enough?"
                    $ play_spank_sound()
                    "SMACK"
                    "You give her ass another swat. She arches her back in appreciation."
                    the_girl "Two!"
                    "You continue your punishment, alternating giving her a few thrusts and then another smack."
                    $ the_girl.discover_opinion("being submissive")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    $ play_spank_sound()
                    "SMACK"
                    the_girl "OH, god... SEVEN!"
                    mc.name "Does your pussy get wetter with every spank? I think it does!"
                    if the_girl.arousal_perc > 80:
                        mc.name "Are you going to cum when I spank you? Go ahead and cum. I'll punish you by spanking you another 10 times."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive") * 2)
                        $ play_moan_sound()
                        "[the_girl.possessive_title] moans loudly. She is breathing too heavy to make a coherent response."
                elif the_girl.sluttiness > 80 or the_girl.obedience > 180:
                    the_girl "I'm sorry [the_girl.mc_title]! I'll try to get better at this. Having you fuck me like this is so intense..."
                    $ play_spank_sound()
                    "SMACK"
                    mc.name "You didn't answer the question! Answer how many spankings you deserve for being such a tease"
                    the_girl "Oh god, five! I deserve five for being such a tease!"
                    $ play_spank_sound()
                    "You continue your punishment, alternating giving her a few thrusts and then another smack."
                elif the_girl.get_opinion_score("being submissive") < 0:
                    the_girl "What the fuck? How about zero?"
                    $ the_girl.discover_opinion("being submissive")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    "[the_girl.possessive_title] doesn't seem to appreciate the spanking, maybe you should refrain from doing so."
                else:
                    the_girl "Five! I think I need five... but could you not spank me so hard? It hurts..."
                    $ play_spank_sound()
                    "You give her plaint ass another swat, this time not quite as hard."
                    "Her ass quivers slightly as you spank her. It feels great around your cock."
                "After you finish her spanking, you grab her hips and resume your fucking."
            "Talk Dirty":
                mc.name "I love the way it sounds when I fuck you. Hear it?"
                "You thrust yourself back into her forcefully, her ass smacking against your hips with a loud smack."
                $ play_moan_sound()
                "[the_girl.possessive_title] moans and pushes herself back against you."
                mc.name "That's it, you’re my bitch. I love how naughty you are."
                "She seems to be into it. Maybe you should tell her how you want to finish."
                menu:
                    "I wanna creampie you":
                        if the_girl.wants_creampie:
                            "[the_girl.possessive_title]'s legs shake for a second. She peeks back at you with lust in her eyes."
                            the_girl "I'm already so full... I can't wait to feel you blow inside me."
                            "She seems to be into creampies!"
                            mc.name "Don't worry, I'm gonna put this cum where it belongs."
                            $ the_girl.discover_opinion("creampies")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("creampies"))
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans and her arousal is quickly building from your dirty talk."
                        elif the_girl.get_opinion_score("bareback sex") > 0:
                            "You see goosebumps form on the back of [the_girl.possessive_title]'s neck"
                            the_girl "Plant your seed inside me! I want to feel you fill me up!"
                            "Sounds like she likes the idea of getting bred!"
                            mc.name "When I get ready to cum, I'm gonna thrust so deep inside you and hold it there while I fill your fertile pussy."
                            $ the_girl.discover_opinion("bareback sex")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("bareback sex"))
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans and her arousal is quickly building from your dirty talk."
                        elif the_girl.get_opinion_score("creampies") < 0 or the_girl.effective_sluttiness() < 80:
                            "[the_girl.possessive_title] stiffens up slightly at the prospect of getting creampied"
                            the_girl "You could do that... or you could pullout and cum all over my ass... wouldn't that be sexy?"
                            "She doesn't seem to be into being cum inside. Maybe you should consider finishing somewhere else..."
                        else:
                            the_girl "Mmmmm, I love it when you fill me up... Or you could pull out and cum all over my ass... Whatever you want!"
                            "Sounds like she just wants to please you, without being partial to a creampie or finishing some other way."
                    "I wanna cover your ass":
                        if the_girl.get_opinion_score("being covered in cum") > 0:
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans and looks back at you."
                            the_girl "Oh god I love the feeling of your hot, sticky cum shooting all over me..."
                            mc.name "Oh, do you like that, slut? When I spray all over you skin and mark you as my little cumslut?"
                            $ play_moan_sound()
                            "She moans lewdly at your remarks. She seems to be getting into it."
                            $ the_girl.discover_opinion("being covered in cum")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being covered in cum"))
                        elif the_girl.get_opinion_score("showing her ass") > 0:
                            "[the_girl.possessive_title] looks back at you."
                            the_girl "Mmmm, do you think it's sexy? My ass, covered in your seed. I can't wait to bend over and shake it back and forth for you."
                            mc.name "I bet. That ass is so amazing, I bet you love showing it off every chance you get, don't you?"
                            "The next time you thrust into her, you pause for a second when you are fully embedded within her."
                            the_girl "I'm gonna shake my ass just like this for you, after you paint it with your cum"
                            "[the_girl.possessive_title] begins to move her hips side to side. It is a very alluring motion, and feels amazing being so deep inside her."
                            $ the_girl.discover_opinion("showing her ass")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
                            $ mc.change_arousal(5)
                        else:
                            "[the_girl.possessive_title] peeks back at you and smiles"
                            the_girl "That sounds hot... I can't wait to feel it..."
                "After you finish dirty talking, you grab her hips and resume your fucking."
    else:   #She is experienced. Give her a chance to please you
        "[the_girl.possessive_title] reaches back with one hand and grabs your hip, urging you to fuck her harder."
        "She is keeping pace with you, pushing back and meeting your thrusts exquisitely. Your hips make a loud slap against her ass with every thrust, and your balls swing forward and slap her pussy when you bottom out."
        the_girl "Oh god, [the_girl.mc_title], you fuck me so good..."
        "[the_girl.possessive_title]'s tight cunt feels so good, you can't help but slam into it over and over again. Maybe you should touch her a bit or talk dirty in her ear..."
        menu:
            "Touch her":
                "You thrust deep inside [the_girl.possessive_title]'s [the_girl.pubes_description] pussy and hold it there for a second. You reach one hand around her hip and trail it down between her legs..."
                "You reach her mound and being to work circles around her clit with your fingers"
                if the_girl.arousal_perc > 120:
                    the_girl "Oh my god you're gonna make me cum again! Holy fuck!"
                    $ the_girl.have_orgasm()
                    "With your fingers caressing her and your cock buried deep, you can feel her pussy pulse and spasm around you as another orgasmic wave hits her."
                    "The feeling of her juicy cunt convulsing all around your shaft is almost too much to bear"
                    $ mc.change_arousal(8)
                    $ the_girl.change_happiness(2)
                if the_girl.get_opinion_score("being fingered") > 0:
                    "[the_girl.possessive_title] reacts by pushing her hips forward to grind against your fingers."
                    "You use your other hand to hold her hip to keep your groin buried in her sex."
                    the_girl "OH... fuck, how do you do that... it feels so good!"
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
                else:   ####TODO add doesn't like it dialogue ###
                    $ play_moan_sound()
                    "[the_girl.possessive_title] moans at the added stimulation. She begins to move her hips side to side, alternating grinding against your fingers and your crotch"
                    the_girl "[the_girl.mc_title] that's it, keep going!"
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
                "You decide after a bit to get back to fucking. You bring you hand up to your face and see that is covered in her juices."
                menu:
                    "Make her suck it":
                        "You bring your fingers, glistening with her moisture, up to her face."
                        mc.name "Suck my fingers clean like a good girl."
                        if the_girl.has_cum_fetish:
                            "[the_girl.possessive_title] opens her mouth and sucks your fingers into her mouth. She sucks your fingers hungrily, deep into her mouth. Your fingertips are tickling the back of her throat."
                            "Her head bobs up and down as she suckles her juices off your fingers."
                            "You pull your fingers out with a pop. She looks back at you, her pouty lips almost enticing you to let her suck on your finger a bit longer."
                        elif the_girl.get_opinion_score("being submissive") > 0 or the_girl.effective_sluttiness() > 90:
                            the_girl "Yes [the_girl.mc_title]!"
                            "[the_girl.possessive_title] immediately opens her mouth and begins sucking on your fingers. She bobs her head up and down on them a few times as if it were a cock"
                            "Her mouth comes off your fingers with a pop."
                            the_girl "There you go [the_girl.mc_title], all clean!"
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                        else:
                            "[the_girl.possessive_title] tentatively opens her mouth and sucks on your fingers, one at a time, until none of her juices remain."
                    "Lick it clean":
                        "A tantalizing musk enters your nose, coming from your fingers. Without even thinking, you start to lick her juices off your fingers."
                        "You moan in appreciation of how good she tastes, and she peeks back at you."
                        if the_girl.has_cum_fetish:
                            the_girl "Oh [the_girl.mc_title], if you want to taste me, just ask! I love it when you lick my pussy..."
                        elif the_girl.get_opinion_score("getting head") > 0:
                            the_girl "You know, [the_girl.mc_title], if you ever want more, you could always go straight to the source..."
                            "For a second, you imagine [the_girl.possessive_title] laying on your bed, legs spread wide, while you eat her out..."
                            $ the_girl.discover_opinion("getting head")
                            $ mc.change_arousal( 2)
                            "It's a very enticing thought, and sounds like she would be into it..."
                        else:
                            "[the_girl.possessive_title]'s eyes go wide when she sees you licking your fingers."
                            "[the_girl.possessive_title] turns back to [the_object.name] and pushes back against you, prompting you to continue fucking her"
                    "Wipe it on your hip":
                        "You wipe your hand quickly on your hip."
                "Your fingers clean, you grab her hips with both hands and resume fucking her."

            "Dirty Talk":
                mc.name "I love the way it sounds when I fuck you. Hear it?"
                "You thrust yourself back into her forcefully, her ass smacking against your hips with a loud smack."
                $ play_moan_sound()
                "[the_girl.possessive_title] moans and pushes herself back against you."
                mc.name "That's it, you’re such a talented slut. I love how naughty you are."
                "She seems to be into it. Maybe you should tell her how you want to finish."
                menu:
                    "I wanna creampie you":
                        if the_girl.has_cum_fetish:
                            "[the_girl.possessive_title]'s legs shake for a second. She looks back at you with fire in her eyes."
                            the_girl "You better! Don't even thinking about robbing my poor pussy of your incredible cum. It belongs inside me!"
                            "You give her another rough thrust, pushing yourself deep inside her."
                            mc.name "Don't worry, when I cum, I'll push in so deep not a drop will leak out of you."
                            $ the_girl.change_arousal(10)
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans. She is truly addicted to your cum."
                            the_girl "Do it! Give me your cum! I want it so bad."
                        elif the_girl.wants_creampie:
                            "[the_girl.possessive_title]'s legs shake for a second. She peeks back at you with lust in her eyes."
                            the_girl "I'm already so full... I can't wait to feel you blow inside me."
                            "She seems to be into creampies!"
                            mc.name "Don't worry, I'm gonna put this cum where it belongs."
                            $ the_girl.discover_opinion("creampies")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("creampies"))
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans and her arousal is quickly building from your dirty talk."
                        elif the_girl.get_opinion_score("bareback sex") > 0:
                            "You see goosebumps form on the back of [the_girl.possessive_title]'s neck"
                            the_girl "Plant your seed inside me! I want to feel you fill me up!"
                            "Sounds like she likes the idea of getting bred!"
                            mc.name "When I get ready to cum, I'm gonna thrust so deep inside you and hold it there while I fill your fertile pussy."
                            $ the_girl.discover_opinion("bareback sex")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("bareback sex"))
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans and her arousal is quickly building from your dirty talk."
                        elif the_girl.get_opinion_score("creampies") < 0 or the_girl.effective_sluttiness() < 80:
                            "[the_girl.possessive_title] stiffens up slightly at the prospect of getting creampied"
                            the_girl "You could do that... or you could pullout and cum all over my ass... wouldn't that be sexy?"
                            "She doesn't seem to be into being cum inside. Maybe you should consider finishing somewhere else..."
                        else:
                            the_girl "Mmmmm, I love it when you fill me up... Or you could pull out and cum all over my ass... Whatever you want!"
                            "Sounds like she just wants to please you, without being partial to a creampie or finishing some other way."
                    "I wanna cover your ass":
                        if the_girl.has_cum_fetish:
                            "[the_girl.possessive_title]'s legs shake for a second. She looks back at you with fire in her eyes."
                            the_girl "You better! cover every single square inch of my ass. I want to feel it when I stand up and your cum runs down my legs"
                            "You fuck her roughly, each thrust making a loud slap."
                            mc.name "Don't worry, when I cum, you ass will be slick and sticky, coated in my seed.."
                            $ the_girl.change_arousal(10)
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans. She is truly addicted to your cum."
                            the_girl "Do it! Give me your cum! I want it so bad."
                        if the_girl.get_opinion_score("being covered in cum") > 0:
                            "[the_girl.possessive_title] moans and looks back at you."
                            the_girl "Oh god I love the feeling of your hot, sticky cum shooting all over me..."
                            mc.name "Oh, do you like that, slut? When I spray all over you skin and mark you as my little cumslut?"
                            $ play_moan_sound()
                            "She moans lewdly at your remarks. She seems to be getting into it."
                            $ the_girl.discover_opinion("being covered in cum")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("being covered in cum"))
                        elif the_girl.get_opinion_score("showing her ass") > 0:
                            "[the_girl.possessive_title] looks back at you."
                            the_girl "Mmmm, do you think it's sexy? My ass, covered in your seed. I can't wait to bend over and shake it back and forth for you."
                            mc.name "I bet. That ass is so amazing, I bet you love showing it off every chance you get, don't you?"
                            "The next time you thrust into her, you pause for a second when you are fully embedded within her."
                            the_girl "I'm gonna shake my ass just like this for you, after you paint it with your cum"
                            "[the_girl.possessive_title] begins to move her hips side to side. It is a very alluring motion, and feels amazing being so deep inside her."
                            $ the_girl.discover_opinion("showing her ass")
                            $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
                            $mc.change_arousal( 5)
                        else:
                            "[the_girl.possessive_title] peeks back at you and smiles"
                            the_girl "That sounds hot... I can't wait to feel it..."
                "After you finish dirty talking, you grab her hips and resume your fucking."

    return


label scene_facing_wall_2(the_girl, the_location, the_object):
    "You grab one of [the_girl.possessive_title]'s legs and lift it up to the side, giving you better access to thrust deep inside her"
    "The change of angle of your penetration is very stimulating for both of you."
    the_girl "Oh, that's it [the_girl.mc_title], don't stop, it feels so good!"
    "You didn't have any plans of stopping anyway."
    if mc.sex_skills["Vaginal"] > the_girl.sex_skills["Vaginal"]: #If MC is better at sex than girl
        "In fact, you decide it's time to take things to the next level and really pleasure her."
        "You shift your hips to the side, changing the angle of penetration to give increased friction against her G-spot."
        "You give [the_girl.possessive_title] a few short, shallow thrusts, the shove yourself deep and bottom out. You reach around her body and grope at her breast with your free hand."
        the_girl "[the_girl.mc_title] you fuck me so good... I don't know how you do it!"
        if the_girl.arousal_perc > 100: #Sex gets more intense the more she has orgasmed
            "After multiple orgasms, [the_girl.possessive_title]'s pussy is flooded with her juices. It feels so good to be buried in her soaked, convulsing slit."
            "It is a wonder that [the_girl.possessive_title] can even stand."
            $ mc.change_arousal( 5)
        elif the_girl.arousal_perc > 80:
            "The heat and moisture radiating from [the_girl.possessive_title]'s groin is intense, having already orgasmed at least once. You groan in appreciation of her eager cunt."
            $ mc.change_arousal( 3)
        else:
            "[the_girl.possessive_title]'s pussy is growing wetter with each thrust, the pleasure from your skillful fucking quickly bringing her to the brink of orgasm."
        "You decide to go for it and make another move in an attempt to please her even more."
        menu:
            "Lightly spank her pussy":
                "Still holding her leg up with one hand, you release her tit with your other and let it trail down her body to her slit."
                "Holding yourself deep inside her, you give her clit a few light, playful smacks with a couple of your fingers."
                if the_girl.get_opinion_score("being fingered") > 0:
                    $ play_moan_sound()
                    "[the_girl.possessive_title] moans enthusiastically at the stimulation of your light slaps on her clit."
                    the_girl "That's it, [the_girl.mc_title]! Spank my pussy! I've been so naughty!"
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered") + mc.sex_skills["Foreplay"])
                    "You continue giving [the_girl.possessive_title]'s mound a few more swats. You can feel her pelvic muscles clench you a few times as you tap her."
                    "[the_girl.possessive_title] clearly enjoys having your hands on her..."
                elif the_girl.get_opinion_score("being fingered") < 0:
                    the_girl "Ow! Hey! What was that for?"
                    "You pause for a second... maybe she isn't into have your hands on her down there?"
                    "You give he another light swat."
                    the_girl "Hey! You're supposed to be fucking me! Knock it off with that!"
                    $ the_girl.discover_opinion("being fingered")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being fingered"))
                    "Looks like she doesn't enjoy having your hands down there."
                else:
                    $ play_spank_sound()
                    "[the_girl.possessive_title] jumps when you first swat her, surprised by the mixture of pleasure and pain the smack gives her."
                    the_girl "Oh! [the_girl.mc_title]... that feels good... but could you be careful?"
                    "Using your index and middle finger, you give [the_girl.possessive_title]'s mound a few more taps, a bit lighter than before."
                    the_girl "Mmmmm, that's it!"
                    "Encouraged by her words, you give her a few more playful taps."
                    $ the_girl.change_arousal(mc.sex_skills["Foreplay"])

            "Play with her asshole":
                "You look down and admire [the_girl.possessive_title]'s amazing ass and get a naughty idea."
                "You release her soft titflesh with your hand and bring it up to [the_girl.possessive_title]'s mouth. She immediately takes them in her mouth and starts to suck on them, mimicking a blowjob on your fingers."
                "Satisfied there is enough lubrication, you pull yourself partway out of her cunt to give yourself a bit of room to work. You tentatively circle her ass a few times with your finger."
                if the_girl.get_opinion_score("anal sex") > 0:
                    $ play_moan_sound()
                    "At the sudden stimulation of her back door, [the_girl.possessive_title] moans and immediately thrusts her ass back at you."
                    the_girl "Mmm, that's it [the_girl.mc_title]! I can't wait to feel your fingers in one hole and your cock in the other..."
                    "Wow, she clearly enjoys having her ass played with!"
                    $ the_girl.discover_opinion("anal sex")
                    "You firmly press two fingers against [the_girl.possessive_title]'s puckered opening. Her bottom greedily takes your fingers and soon they are completely sheathed."
                    the_girl "[the_girl.mc_title]! I'm so full!"
                    "You move your hips in a few slow thrusts. You started to move your fingers in and out of her in time with your strokes."
                    "[the_girl.possessive_title] groans and her holes quiver in pleasure each time you penetrate her completely"
                    "You fuck her for a while like this, but eventually withdraw your fingers from her and let her leg go."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") + mc.sex_skills["Anal"])
                elif the_girl.get_opinion_score("anal sex") < 0:
                    "When you begin to stimulating her backdoor, [the_girl.possessive_title] immediately begins to protest."
                    the_girl "Hey! That hole's not for that... Keep your hands away from there, [the_girl.mc_title]!"        ####TODO FINISH THIS
                    $ the_girl.discover_opinion("anal sex")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex"))
                    "Seems like she isn't keen on having her ass played with."
                    "You let her leg down and resume your fucking."
                else:
                    "[the_girl.possessive_title] looks back at you, her eyes wide."
                    the_girl "[the_girl.mc_title]! Whoa! You take it easy there! I don't often get touched back there like that..."
                    "She seems open to having her backdoor caressed, but you decide it would be best to take it easy."
                    "With just your index finger, you trace a few circles around [the_girl.possessive_title]'s puckered opening."
                    "You gently probe her anus, pushing your finger in to the first knuckle before she starts to protest."
                    "You slowly withdraw your finger and then give her booty a light spank, her pliant flesh quivering from the impact."
                    "You spit on her ass and rub your finger in it, getting it lubricated again. This time you are able to delve you finger all the way inside."
                    the_girl "Holy fuck, [the_girl.mc_title]! That is so intense..."
                    "You slowly push your hips forward, embedding your shaft in between her legs. You move your finger along the pliant walls of [the_girl.possessive_title]'s rectum"
                    "You stroke yourself a few times through the thin wall of flesh that separates her vagina and her bowel. It feels good to be so deep in both her holes."
                    $ the_girl.change_arousal(mc.sex_skills["Anal"])
                    "Eventually, the stimulation starts to drop off a bit, so you decide to slowly withdraw your finger from her and resume your fucking."
            #"Neutral answer":
            #    "Neutral stuff"
    else:    #She is better at vaginal sex than MC
        "The soft, velvet flesh of [the_girl.possessive_title]'s cunt is bliss around your dick. It is almost overwhelming how tight she is."
        the_girl "[the_girl.mc_title], let me work it for a minute... I promise you won't be disappointed!"
        "You give her a couple quick thrusts while you consider it. You're sure with how skilled she is, that whatever she has in mind is probably very pleasurable..."
        menu:
            "Let her fuck you":
                mc.name "Okay, [the_girl.title], let's see what you can do."
                "Even with just one foot on the floor and the other in the air as you hold it, [the_girl.possessive_title] is able to begin gyrating her hips up against you."
                "Enjoying her skill, you stand and watch, entranced as [the_girl.possessive_title] stirs her creamy womb with your shaft."
                if the_girl.is_dominant:
                    "[the_girl.possessive_title] reaches back with one hand and grabs your hip and shoves you in deep inside her."
                    "She holds it there completely still, but you can still feel her stimulate you by clenching and releasing her pelvic muscles."
                    the_girl "[the_girl.mc_title]... You've always been so good to me... Let [the_girl.possessive_title] take care of you this time!"
                    $ the_girl.discover_opinion("taking charge")
                    "You can tell [the_girl.possessive_title] is enjoying taking charge for a minute in this normally submissive position."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("taking control"))

                $ mc.change_arousal( 5)
                "Having [the_girl.possessive_title] take charge for a bit is extremely pleasurable, but eventually you can see her start to grow tired."
                mc.name "Atta girl... it's time for me to set the pace now."
                "You release her leg and continue fucking her."
            "Continue normally":
                "You can tell that [the_girl.possessive_title] isn't getting as much pleasure from this position as you are, so you try to mix up your tactics a bit to keep her interested."
                "With your free hand you reach around her and start to fondle her tits."
                if the_girl.has_large_tits :
                    if the_girl.tits_available:
                        "You plant a hand on [the_girl.possessive_title]'s nice, soft tits and squeeze. Her pliant flesh melts in your hand, and the heat coming form her skin feels amazing."
                        the_girl "Mmm, [the_girl.mc_title]. Your hands feel so good."
                        "You enjoy teasing her supple [the_girl.tits_description] for a few moments. You hold one in place while you fuck her, feeling the weight of it sway with each motion."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("showing her tits"))
                    else:
                        "You plant a hand on [the_girl.possessive_title]'s big tits and fondle them through her [the_girl.outfit.get_upper_top_layer.display_name]."
                        the_girl "Mmm, you should just pull that out of the way. I want you to be able to grab them and squeeze them."
                        "For now, you decide to continue fondling her through her clothing."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("showing her tits"))
                    if the_girl.arousal_perc > 120:
                        $ play_moan_sound()
                        "[the_girl.possessive_title] moans loudly from your attention to her voluptuous chest. She thrusts herself back against you."
                        $ the_girl.have_orgasm()
                        "You feel yet another orgasm roll through her. Her drenched [the_girl.pubes_description] pussy is pulsating wildly and it's just too much. You are definitely about to cum!"
                        $ mc.change_arousal(10)
                        return
                else:
                    if the_girl.tits_available:
                        "You run a hand over [the_girl.possessive_title]'s [the_girl.tits_description]. You pinch and pull at one of her nipples."
                        the_girl "Oh! Easy there, it's sensitive."
                        "You move to her other nipple ad give it similar treatment. She gasps at the work of your strong hands on her chest."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("showing her tits"))
                        if the_girl.arousal_perc > 120:
                            $ play_moan_sound()
                            "[the_girl.possessive_title] moans loudly from your attention to her petite chest. She thrusts herself back against you."
                            "You feel yet another orgasm roll through her. Her drenched [the_girl.pubes_description] pussy is pulsating wildly and it's just too much. You are definitely about to cum!"
                            $ mc.change_arousal(10)
                            return
                    else:
                        "You try and feel up [the_girl.possessive_title]'s [the_girl.tits_description], but her [the_girl.outfit.get_upper_top_layer.display_name] stops you from getting much more than a handful of fabric."
                        "You give up and focus on fucking her instead."
                        $ the_girl.change_arousal(the_girl.get_opinion_score("showing her tits"))
                if the_girl.arousal_perc > 90:
                    "[the_girl.possessive_title]'s slit is drenched with her excitement."
                    the_girl "Oh god, [the_girl.mc_title], you are going to make me cum again!"
                elif the_girl.arousal_perc > 70:
                    "[the_girl.possessive_title]'s slit is saturated with her excitement. She is so close, you're about to make her cum!"
                "You release her leg and continue fucking her."
                return

            "Make her submit":
                if the_girl.is_bald:
                    "You reach up with your free hand and grab her by the throat."
                else:
                    "You reach up with your free hand and grab her hair next to the back of her head."
                mc.name "I don't think so. I'm the man here, I'll do what I please with you, when I please. If I want you to fuck me I'll tell you to."
                if the_girl.get_opinion_score("being submissive") > 0:
                    "[the_girl.possessive_title] melts back into you. Her urge to take the lead has been replaced with submission."
                    if the_girl.is_bald:
                        "You give a rough tug on neck to show her than you mean it."
                    else:
                        "You give a rough tug on her hair to show her than you mean it."
                    the_girl "Oh god... You've got me up against the [the_object.name]."
                    $ play_moan_sound()
                    "You fuck her hard and fast. [the_girl.possessive_title] gasps and moans, her rounded hips shaking with every thrust."
                    mc.name "That's right, I've got you right where I want you and there's nothing you can do about it."
                    "[the_girl.possessive_title] tries to move her head, but your strong grip on her [the_girl.hair_description] prevents her from shifting it much."
                    if the_girl.get_opinion_score("bareback sex") > 0:
                        the_girl "You could fuck me until you cum inside and there's nothing I could do. You could knock me up while I'm up against the [the_object.name] like I'm some kind of slut..."
                    elif the_girl.wants_creampie:
                        the_girl "You could cum right inside me and there's nothing I could do to stop you... Just blow your load inside of me like I'm just a little slut..."
                    else:
                        the_girl "Oh god you are just using me like a cock sleeve and there is nothing I can do. Like I'm just a little slut..."
                    "You push yourself deep inside her and then pause your fucking for a second."
                    mc.name "That's because you are a slut, [the_girl.title]. You are MY slut, to use as I please, no matter what I decide to do to you."
                    "[the_girl.possessive_title] gasps at your harsh words, but her quivering pussy betrays her excitement at being treated this way."
                    $ the_girl.change_arousal(the_girl.get_opinion_score("being submissive"))
                    $ the_girl.discover_opinion("being submissive")
                    return
                else:
                    the_girl "Yow! Hey what the fuck?"
                    if the_girl.obedience > 180:
                        "[the_girl.possessive_title]'s body stiffens at your rough treatment, but she knows better than to disobey you."
                        "You decide to release her [the_girl.hair_description], but continue to set the pace with your hips as you fuck her from behind."
                    else:
                        if the_girl.is_bald:
                            the_girl "Don't push your luck back there! It hurts when you squeeze my throat!"
                            "You release your grip and continue to fuck her. It seems she isn't turned on by your tough act."
                        else:
                            the_girl "Don't push your luck back there! It hurts when you pull my hair!"
                            "You release her hair and continue to fuck her. It seems she isn't turned on by your tough act."
                        $ the_girl.change_arousal(-5)

    return

label outro_facing_wall(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s sweet cunt draws you closer to your orgasm with each thrust. You finally pass the point of no return and speed up, fucking her as hard as you can manage."
    $the_girl.call_dialogue("sex_responses_vaginal")
    mc.name "Ah, I'm going to cum!"
    $ the_girl.call_dialogue("cum_pullout")
    $ climax_controller = ClimaxController(["Cum inside of her","pussy"], ["Cum on her ass", "body"], ["Cum on her face", "face"])
    $ the_choice = climax_controller.show_climax_menu()

    if the_choice == "Cum inside of her":
        if mc.condom:
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps when she feels you filling the condom deep inside of her."
            $ the_girl.call_dialogue("cum_condom")
            $ climax_controller.do_clarity_release(the_girl)
            "You wait until your orgasm has passed completely, then pull out and stand back. You condom is bulged on the end where it is filled with your seed."

            call post_orgasm_condom_routine(the_girl, facing_wall) from _call_post_orgasm_condom_routine_facing_wall

        else:
            "You push forward as you finally climax, thrusting your cock as deep inside of [the_girl.possessive_title] as you can manage. She gasps softly each time your dick pulses and shoots hot cum into her."
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ climax_controller.do_clarity_release(the_girl)
            $ facing_wall.redraw_scene(the_girl)
            "You pull back on [the_girl.possessive_title]'s hips and drive your cock deep inside of her as you cum. She gasps softly in time with each new shot of hot semen inside of her."

            if the_girl.wants_creampie:
                the_girl "Yes! Fill me up with your cum!"
            if the_girl.get_opinion_score("bareback sex") > 0:
                the_girl "I love it when you shoot your seed so deep!"
            $ the_girl.cum_in_vagina()
            $ facing_wall.redraw_scene(the_girl)
            if the_girl.sluttiness > 90:
                the_girl "Oh god it's so good. I'm going to fall asleep dreaming about this tonight..."
            elif the_girl.sluttiness > 70:
                the_girl "Oh fuck that's good. It feels so warm..."
            else:
                the_girl "Oh my god, why do I let you do this to me... but it feels so good..."

            "Once you finish, you slowly back up and pull yourself out of [the_girl.possessive_title]. A stream of semen trickles out of her and down her long legs for a few seconds."
            if the_girl.get_opinion_score("bareback sex") > 0:
                "[the_girl.possessive_title] reaches back and desperately tries to stop any more from leaking out with her hand."

    if the_choice == "Cum on her ass":
        $ the_girl.cum_on_ass()
        $ climax_controller.do_clarity_release(the_girl)
        $ facing_wall.redraw_scene(the_girl)
        if mc.condom:
            "You pull out of [the_girl.possessive_title] at the last moment, pulling your condom off as your blow your load all over her ass."
            "She holds still for you as you cover her with your sperm."
        else:
            "You pull out of [the_girl.possessive_title] at the last moment, stroking your shaft as you blow your load over her ass. She wiggles her ass for you as you cover her with your sperm."

        if the_girl.get_opinion_score("being covered in cum") > 0:
            the_girl "Yes! Paint me with your sticky cum!"

        if the_girl.get_opinion_score("showing her ass") > 0:
            "[the_girl.possessive_title] bends over and presents her cum covered ass to you."
            "She gives her hips a few enticing wiggles as your cum starts to drip down the back of her legs."
        elif the_girl.sluttiness > 90:
            the_girl "Oh god your seed is so hot! Does it look sexy, having it plastered all over my ass?"
            "She reaches back and runs a finger through the puddles of cum you've put on her, then licks her finger clean."
        else:
            the_girl "Oh! It's so warm..."
        "You stand back and sigh contentedly, enjoying the sight of [the_girl.possessive_title]'s ass covered in your semen."
    if the_choice == "Cum on her face":
        mc.name "Fuck, get ready [the_girl.title], I wanna cum on your face!"
        if mc.condom:
            "You pull your cock out of [the_girl.possessive_title] with a satisfying pop. You pull your condom off as she turns around on gets on her knees in front of you."
        else:
            "You pull your cock out of [the_girl.possessive_title] with a satisfying pop. She immediately turns around on gets on her knees in front of you."
        $ the_girl.draw_person(position = "kneeling1")
        if the_girl.get_opinion_score("cum facials") > 0:
            "[the_girl.possessive_title] begins stroking you while pointing your cock straight at her eager face."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. After your first spurt a big smile spreads across her face as you cover it with your cum."
            "[the_girl.possessive_title] keeps stroking you as you finish your orgasm. She grasps your penis at the base and slowly milks out the last couple of drops, letting fall down and on to her cheek."
            the_girl "Ohhhh... damn that is so hot..."
            "[the_girl.possessive_title] uses her hand to rub your cum into her skin, revealing in the sticky texture. A couple of times she licks her fingers clean."
        elif the_girl.sluttiness > 80:
            "[the_girl.possessive_title] sticks out her tongue for you and holds still, eager to take your hot load."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face and into her open mouth. She makes sure to wait until you're completely finished."
            the_girl "Oh god... it feels so good on my skin..."
        elif the_girl.sluttiness > 60:
            "[the_girl.possessive_title] closes her eyes and waits patiently for you to cum."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She waits until she's sure you're finished, then opens one eye and looks up at you."
        else:
            "[the_girl.possessive_title] closes her eyes and turns away, presenting her cheek to you as you finally climax."
            $ the_girl.cum_on_face()
            $ the_girl.draw_person(position = "kneeling1")
            "You let out a shuddering moan as you cum, pumping your sperm onto [the_girl.possessive_title]'s face. She flinches as the first splash of warm liquid lands on her cheek, but doesn't pull away entirely."
        if the_girl.get_opinion_score("being covered in cum") > 0:
            "[the_girl.possessive_title] runs her fingers through your cum on her face a few times. She quickly licks her fingers clean."
            the_girl "Mmm, your hot, sticky seed feels so good all over me..."
        $ climax_controller.do_clarity_release(the_girl)
        "You take a deep breath to steady yourself once you've finished orgasming. [the_girl.possessive_title] looks up at you from her knees, face covered in your semen."
        $ the_girl.call_dialogue("cum_face")
    return

label transition_facing_wall_against_wall(the_girl, the_location, the_object):
    "You decide to turn [the_girl.possessive_title] around to face you. You want to feel her chest against yours and kiss her deep while you fuck."
    "You pull out and back off for a second while you spin her hips."
    "[the_girl.possessive_title] plants her back against [the_object.name] and watches you as you line yourself back up."
    "You push forward, slipping your shaft deep inside of [the_girl.possessive_title]'s cunt. She gasps and quivers ever so slightly as you start to pump in and out."

    return

label transition_against_wall_facing_wall(the_girl, the_location, the_object):
    "You decide you want to turn her around so you can really give her a good pounding. You pull out and turn her around, facing [the_object.name]."
    $ facing_wall.redraw_scene(the_girl)
    "You rub your dick along her slit a few times, first up and down, and then side to side. You line yourself up and begin to push inside of her."
    the_girl "Oh my god..."
    "[the_girl.possessive_title] sighs as you bottom out."
    if the_girl.effective_sluttiness() > 95:
        "She wiggles her ass back and forth a few times, enjoying the familiar feel of fullness you give her when you fuck her."
    elif the_girl.effective_sluttiness() > 80:
        the_girl "[the_girl.mc_title], it feels so good..."
    else:
        "[the_girl.possessive_title] arches her back a bit. She steals a glance back at you while you enjoy the warm, slick grip of her [the_girl.pubes_description] pussy."
    "You put your hands on [the_girl.possessive_title]'s hips and give her a tentative thrust."
    if the_girl.arousal_perc > 60:
        "[the_girl.possessive_title]'s cunt is already slick and wet with arousal. She places on hand on top of yours, encouraging you fuck her."
    else:
        "[the_girl.possessive_title] gives a grunt as you begin to fuck her."
    if the_girl.get_opinion_score("sex standing up") > 0 :
        the_girl "Oh my god, it feels so good to get fucked like this."
        $ the_girl.change_arousal(the_girl.get_opinion_score("sex standing up"))
        $ the_girl.discover_opinion("sex standing up")
    return

label transition_default_facing_wall(the_girl, the_location, the_object):
    $ facing_wall.redraw_scene(the_girl)
    "You turn [the_girl.possessive_title] so she is is facing [the_object.name]."
    if not the_girl.vagina_available:
        "You move some clothing out of the way..."
        $ the_girl.strip_to_vagina(position = facing_wall.position_tag, visible_enough = True, prefer_half_off = True)
    "Once you're ready you push yourself forward, slipping your hard shaft deep inside of her. She lets out a gasp under her breath."
    return

label strip_facing_wall(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] leans forward a little further and pops off your cock."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = facing_wall.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
    "She groans happily when you push back inside of her."
    return

label strip_ask_facing_wall(the_girl, the_clothing, the_location, the_object):
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    "[the_girl.char] pants as you fuck her from behind."
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = facing_wall.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side. Then she gets herself lined up in front of you again."
            "She groans happily when you push back inside of her."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "You speed up, fucking her faster in response to her question."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips back into you and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label orgasm_facing_wall(the_girl, the_location, the_object):
    "[the_girl.possessive_title] gasps. Her hands grasp at the [the_object.name] as she starts to cum."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "You push her roughly up against [the_object.name] and keep fucking her through her orgasm."
    "After a couple of seconds [the_girl.possessive_title] takes a couple of deep breathes. You slow down your pace and give her a chance to recover."
    the_girl "Keep fucking me... Make me cum again!"
    return

label taboo_break_facing_wall(the_girl, the_location, the_object):
    # TODO: Add custom taboo break
    return
