init python:
    reverse_cowgirl = Position(name = "Reverse Cowgirl", slut_requirement = 60, slut_cap = 80, requires_hard = True, requires_large_tits = False,
        position_tag = "doggy", requires_location = "Lay", requires_clothing = "Vagina", skill_tag = "Vaginal",
        girl_arousal = 18, girl_energy = 14,
        guy_arousal = 14, guy_energy = 10,
        connections = [],
        intro = "intro_reverse_cowgirl",
        scenes = ["scene_reverse_cowgirl_1","scene_reverse_cowgirl_2"],
        outro = "outro_reverse_cowgirl",
        transition_default = "transition_default_reverse_cowgirl",
        strip_description = "strip_reverse_cowgirl", strip_ask_description = "strip_ask_reverse_cowgirl",
        orgasm_description = "orgasm_reverse_cowgirl",
        taboo_break_description = "taboo_break_reverse_cowgirl",
        verb = "be ridden by", verbing = "being ridden by",
        opinion_tags = ["taking control","vaginal sex", "vaginal creampie", "get off"], record_class = "Vaginal Sex",
        default_animation = blowjob_bob,
        associated_taboo = "vaginal_sex")

    list_of_girl_positions.append(reverse_cowgirl)
    reverse_cowgirl.girl_outro = "GIC_outro_reverse_cowgirl"

init 1:
    python:
        missionary.link_positions(reverse_cowgirl,"transition_missionary_reverse_cowgirl")
        reverse_cowgirl.link_positions(doggy,"transition_reverse_cowgirl_doggy")

#init 1:
#    python:
#        #Here is where you would put connections if they existed.

label intro_reverse_cowgirl(the_girl, the_location, the_object):
    mc.name "[the_girl.title], why don't you ride me for a bit?"
    "You lie down on the [the_object.name], and [the_girl.possessive_title] gets on top, facing away from you."
    "She reaches between her legs and wraps her hand around your cock. She slowly guides it into her slit and then slides the length of it inside her."
    return

label scene_reverse_cowgirl_1(the_girl, the_location, the_object):
    # CHOICE CONCEPT: She fucks you, skill based lists#
    "You lie back on the [the_object.name] while [the_girl.possessive_title] works your cock in and out of her."
    if the_girl.arousal_perc > 80:
        "You can clearly see her arousal every time she bounces up and down on top of you; her juices are beginning to run down the inside of her thighs."
    else:
        "You watch in rapture as her tight pussy lips grip your shaft with every bounce."
    if the_girl.has_breeding_fetish:   #Fetish serum, highly skilled and loves sex
        the_girl "Oh [the_girl.mc_title], I love how full I feel when you fuck me... god, I wish we could do this every day!"
        "[the_girl.possessive_title] gives you a few quick, shallow dips, then pulls off you almost completely, leaving just your tip inside her."
        "She swirls her hips a couple times, then impales herself on you again. [the_girl.possessive_title] works her hips relentlessly on top of you as she pleases herself on your erection."
        "After constant exposure to the serums you've designed, it is clear by the way she fucks you with wild abandon that you've turned her into your slut."
        "She give you a few more vigorous thrusts, then sheathes you entirely as deep as she can get you."
        "[the_girl.possessive_title] stops moving her hips for a few seconds, but you can feel her contracting and relaxing the muscles around her pelvis, her cunt milking you without even having to move her hips."
        mc.name "Oh my god [the_girl.title], that feels amazing..."
        if the_girl.arousal_perc > 100:
            "[the_girl.possessive_title] looks back at you with passion in her eyes while the contractions of her pussy around you suddenly strengthen. Her eyes start to glaze as she orgasms again."
            the_girl "[the_girl.mc_title]! I'm cumming again! Cum for me... I need you to cum for me now!!!"
            "Her pleading and the intense pleasure her cunt is giving you is pushing you to orgasm soon."
            $ mc.change_arousal(50)
            return
        "Her sexual expertise is incredibly pleasing for both of you."
        $ the_girl.change_arousal(10)
        $ mc.change_arousal(7)
    elif the_girl.sex_skills["Vaginal"] > 2: #She has some skill
        "[the_girl.possessive_title] slows her pace for a bit, working your erection purposefully with her body."
        "She makes a couple shallow dips, then sheathes you entirely."
        "[the_girl.possessive_title] stops moving her hips for a few seconds, but you can feel her contracting and relaxing the muscles around her pelvis, her cunt milking you without even having to move her hips."
        mc.name "Oh my god [the_girl.title], that feels amazing..."
        if the_girl.arousal_perc > 100:
            the_girl "[the_girl.mc_title]! I'm cumming again! Cum for me... I need you to cum for me now!"
            "Her pleading, and the intense pleasure her cunt is giving you, is pushing you to orgasm soon."
            $ mc.change_arousal(50)
            return
        $ play_moan_sound()
        "[the_girl.title] moans as she continues to ride you."

    else:
        "[the_girl.possessive_title] works her hips up and down on you as best she can."
        "She makes a couple shallow dips, then then sheathes you entirely. She makes a few awkward gyrations with her hips."
        the_girl "Mmm, it feels good. I wish I could fuck you as good as you fuck me."
        mc.name "Don't worry, it feels great, keep going."
        $ play_moan_sound()
        "[the_girl.title] moans as she continues to ride you."

    return

label scene_reverse_cowgirl_2(the_girl, the_location, the_object):
    # CHOICE CONCEPT: She bottoms out and grinds on you for a bit. Spank or finger her
    "[the_girl.possessive_title] bounces up and down a few times on your cock, then holds you deep inside her."
    "Instead of bouncing up and down, she starts to grind herself back and forth."
    the_girl "Mmmm, [the_girl.mc_title], it's so big... I feel so full!"
    "[the_girl.possessive_title]'s shapely ass looks amazing on display in front of you. You grasp one of her pliant cheeks in your hand as she grinds."
    menu:
        "Spank it":
            "You bring your hand off [the_girl.possessive_title]'s ass and give it a firm slap."
            $ play_spank_sound()
            the_girl "Oh!"
            $ play_spank_sound()
            "You enjoy the way her tight ass jiggles and spank it again."
            if the_girl.get_opinion_score("showing her ass") > 0:
                $ the_girl.discover_opinion("showing her ass")
                the_girl "You're gonna leave a mark, [the_girl.mc_title]! Then everyone who sees it will know what a slut I am!"
                "She wiggles her hips back and forth, giving you an enticing moving target. You give her irresistible ass another spank."
                $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass") * 2)
                $ play_moan_sound()
                "[the_girl.possessive_title] moans as you give her a few more swats. A bright red handprint is beginning to form on her cheeks."
            elif the_girl.has_breeding_fetish:
                $ play_spank_sound()
                "You give her irresistible ass another spank. [the_girl.possessive_title] times her thrusts with your hand smacking her booty, swallowing your dick whole with her greedy cunt when you spank her."
                the_girl "Mmmm. I've been bad [the_girl.mc_title], I can't get your dick off my mind!"
                $ play_spank_sound()
                "You spank her again. She bottoms out on top of you in time with your smack again. She greatly enjoys the sensation of getting filled up and spanked at the same time."
                $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
            else:
                the_girl "Do you like that, [the_girl.mc_title]? Ah!"
                $ play_spank_sound()
                "[the_girl.possessive_title] is enjoying herself. You give her accommodating ass another squeeze and then spank it again."
                "You can feel [the_girl.possessive_title]'s pussy quivering as she grinds herself back into you."
                $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
            "You leave a hand planted on [the_girl.possessive_title]'s butt while she fucks you, squeezing it and giving it the occasional slap."

        "Admire her":
            mc.name "Damn [the_girl.title], your ass is amazing!"
            "[the_girl.possessive_title] wiggles back and forth a few more times, then looks back at you and smiles."
            if the_girl.is_dominant:
                the_girl "Do you like that, [the_girl.mc_title]? Just lay back and let me take care of you..."
                "You run your hands along your hips while she grinds back against you. Her cunt feels amazing wrapped around you."
                if the_girl.arousal_perc > 100:
                    the_girl "Oh god, I'm gonna cum again! Fuck, you should cum too... are you gonna cum soon?"
                    "[the_girl.possessive_title]'s pussy spasms again in orgasm. The combination of her orgasm and the view of her ass is incredibly arousing."
                    $ mc.change_arousal(10)
                    $ the_girl.change_happiness(2)
                else:
                    $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
                    the_girl "Ohh, you make me so wet. I want to make you feel good too... Do you wanna cum soon?"
                if the_girl.wants_creampie:
                    "[the_girl.possessive_title] reaches back between her legs and cups your balls."
                    the_girl "Mmm, you feel so full... I want you to fill me up! I can't wait to milk all that cum out of you!"
                else:
                    "[the_girl.possessive_title] grabs your ankles to steady herself."
                    the_girl "You should... I love it when you cum. I want to make you cum!"
            else:
                the_girl "I'm glad you like it, [the_girl.mc_title]. I love it when you fuck me, but sometimes it feels good to be on top too..."
                if the_girl.get_opinion_score("masturbating") > 0:
                    "[the_girl.possessive_title] reaches down with one hand and begins to rub her clit as she grinds back against you."
                    $ the_girl.discover_opinion("masturbating")
                    $ the_girl.change_arousal(the_girl.get_opinion_score("masturbating"))
                "You grab [the_girl.possessive_title]'s ass cheeks with both hands. Her smooth skin feels supple in your hands." ###TODO
            "After some time spent grinding, [the_girl.possessive_title] resumes her bouncing motion on top of you."
        "Finger Her Ass" if (the_girl.get_opinion_score("anal sex") > 0 and the_girl.get_known_opinion_score("anal sex")):   #Can only be done if the girl is known buttslut#
            "You decide to help her feel even more full! You bring your index finger up to your mouth. You stick it in your mouth, getting it good and lubed up."
            "[the_girl.possessive_title] stops grinding for a second when she feels your finger at her asshole."
            if the_girl.sex_skills["Anal"] > 1: #She can easily take a finger
                "You push your finger easily up inside her. Her rectum relaxes and she sighs when you finger is fully engulfed by her back passage."
                the_girl "OH! I love that feeling... keep it right there..."
            else:
                "You meet some resistance as you slowly push your finger against her rectum. She gasps as she fights the instinct to resist it."
                the_girl "Oh! I love this feeling, but give me a second, I'm not very good at taking things back there..."
                "She takes a deep breath, but is able to slowly force herself to relax. You are able to slowly slide your finger inside her."
                "It takes several seconds, but her rectum finally relaxes enough you are able to fully engulf your finger in her back passage."
                the_girl "Mmm... keep it right there, I'm gonna take it slow."
            "[the_girl.title] begins to slowly grind her hips again. With each movement forward your cock and finger slowly pull out of her, and with each movement back she takes them both deep."
            the_girl "Yes! Oh fuck [the_girl.mc_title], the pressure feels so good!"
            $ the_girl.change_arousal(the_girl.get_opinion_score("anal sex") * 2)
            if the_girl.arousal_perc > 100:
                $ play_moan_sound()
                "You can feel [the_girl.title]'s pussy and ass quaking as she aftershocks from her orgasms. She moans ecstatically."
                $ the_girl.have_orgasm()
                "Her [the_girl.pubes_description] pussy clenching your cock as she grinds you feels amazing, and it turns you on seeing her rolling into multiple orgasms."
                $ mc.change_arousal(10)
                $ the_girl.change_happiness(2)
            else:
                "[the_girl.title] is taking her time, just enjoying the feeling of having you fill both her holes."
                "She stops for a second when you hit just the right spot and works her hips side to side for a few moments instead of forward and back."
            "Eventually, she stops grinding and begins to work her body up and down again. You try to keep your finger inside her ass, but it soon slips out."
            $ play_spank_sound()
            "Instead of stopping to let you push your finger back inside her, she keeps riding you, so you give her ass a firm spank."
        "Finger Her Ass\n{color=#ff0000}{size=18}Must like anal sex{/size}{/color} (disabled)" if (the_girl.get_opinion_score("anal sex") <= 0 or not the_girl.get_known_opinion_score("anal sex")):
            pass
    return

label outro_reverse_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s sweet cunt milks your cock, the wet friction pushing you past the point of no return."
    mc.name "Ah, I'm going to cum!"
    "[the_girl.possessive_title] looks back at you and smiles."
    if mc.condom:
        "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
        $ play_moan_sound()
        "She moans as she feels your erection twitching inside of her. You dump your load into the condom, hoping it can contain it."
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        "When you finish, [the_girl.possessive_title] slowly pulls up off you."
        "You gaze at her shapely ass. She reaches back and carefully removes your condom."
        the_girl "Wow that was good. Look at all that cum you made for me..."
        return
    elif the_girl.knows_pregnant:
        the_girl "That's it, shoot your seed deep inside me! Shower my baby with your cum!"
        "She stops her up and down movements and pushes herself down onto you, forcing you up inside her as deep as she can."
        $ play_moan_sound()
        "[the_girl.possessive_title] moans as the first wave of your cum floods her pussy. She slowly moves as you dump your load deep inside her."
        $ the_girl.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        the_girl "Oh Yes! Cum for me! It feels so good when you shoot your cum into my pussy!"
        "[the_girl.possessive_title] slowly pulls herself up, rubbing her drenched pussy, while she smiles at you."
        if the_girl.event_triggers_dict.get("preg_accident", False): # she got pregnant by accident
            the_girl "This is how I got pregnant in the first place, too much potent cum in my fertile pussy."
    elif the_girl.has_cum_fetish:
        if renpy.random.randint(0, 1) == 1: # random choice of cum fetish dialog
            the_girl "Oh god, I can't wait to feel you shoot it up inside me... Cum for me [the_girl.mc_title]!"
            "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
            $ play_moan_sound()
            "She moans as the first wave of your cum floods her [the_girl.pubes_description] pussy. She rocks her hips back and forth on top of you as you dump your load inside her."
            "[the_girl.possessive_title]'s body goes rigid as your cum pours into her pussy. Goosebumps erupt all over her body as her brain registers her creampie."
            the_girl "Oh... OH! Yes [the_girl.mc_title]! Pump it deep! I want it all inside me!"
            "[the_girl.possessive_title] revels in having her cum fetish fulfilled."
            $ the_girl.cum_in_vagina()
            $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
            $ reverse_cowgirl.redraw_scene(the_girl)
            "When you finish, [the_girl.possessive_title] slowly pulls up off you."
            "You gaze at her shapely ass as a few drips of your seed drip out her pussy and onto [the_object.name]."
        else:
            "[the_girl.possessive_title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
            "She reaches down moving your member between her ass cheeks and her hand."
            the_girl "Oh, it's so good when you spray me with your seed... Do it! Cum all over me!"
            "You don't have time to respond before the first wave of cum erupts from your penis."
            $ the_girl.cum_on_ass()
            $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
            $ reverse_cowgirl.redraw_scene(the_girl)
            "[the_girl.possessive_title]'s body goes rigid as your cum coats her ass. Goosebumps erupt all over her body as her brain registers your cum on her skin."
            "[the_girl.possessive_title] revels in bliss as your dick sprays jet after jet of seed across her ass. She moans lewdly."
            the_girl "Thank you [the_girl.mc_title]. Oh my god, it's so good..."
            "You lay back and take a few moments to enjoy the view. [the_girl.possessive_title] is massaging your cum into her ass cheeks with both hands."
    elif the_girl.wants_creampie:
        the_girl "Oh god, I can't wait to feel you shoot it up inside me... Cum for me [the_girl.mc_title]!"
        "[the_girl.possessive_title]'s quivering hole feels too good, you can't hold it back anymore."
        $ play_moan_sound()
        "She moans as the first wave of your cum floods her [the_girl.pubes_description] pussy. She rocks her hips back and forth on top of you as you dump your load inside her."
        $ the_girl.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        "When you finish, [the_girl.possessive_title] slowly pulls up off you."
        "You gaze at her shapely ass as a few drips of your seed drip out her pussy and onto [the_object.name]."
    elif the_girl.get_opinion_score("bareback sex") > 0:
        the_girl "That's it, shoot your seed in deep! I want to feel you flood my womb!"
        "She stops her up and down movements and pushes herself down onto you, forcing you up inside her as deep as she can."
        $ play_moan_sound()
        "[the_girl.possessive_title] moans as the first wave of your cum floods her [the_girl.pubes_description] pussy. She holds herself still as you dump your load deep inside her."
        "You reach your hands forward and grab her hips, and push yourself up slightly, holding her hips in place."
        $ the_girl.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        the_girl "Yes! Cum deep! I don't want a single drop to go to waste!"
        "When you finish, [the_girl.possessive_title] stays still for a few minutes, keeping you deep inside her."
        "She reaches down between her legs, and then slowly pulls off of you, trying to use her hand to keep any of your seed from spilling out."
    elif the_girl.get_opinion_score("being covered in cum") > 0:
        "[the_girl.possessive_title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down moving your member between her ass cheeks and her hand."
        the_girl "Oh my god, it's so warm. I want to feel you shoot your load all over my ass!"
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_girl.cum_on_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        the_girl "Thank you [the_girl.mc_title], I love the feeling of your cum on my skin..."
        "You lay back and take a few moments to enjoy the view."
    elif the_girl.get_opinion_score("showing her ass") > 0:
        "[the_girl.possessive_title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down moving your member between her ass cheeks and her hand."
        the_girl "I want to feel you shoot your load all over my ass! It's going to feel so hot, knowing I've got your load all over my ass..."
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_girl.cum_on_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        the_girl "Thank you [the_girl.mc_title]. Do I look good? With your sticky seed painted all over my backside?"
        "[the_girl.possessive_title] shakes her hips side to side for you, showing off her prize. In a couple places your cum starts drip down from her shapely ass."
        "You lay back and take a few moments to enjoy the view."
    elif the_girl.sex_skills["Vaginal"] >= 5:
        the_girl "Oh god, it feels too good to pull off now... just shoot it up inside me!"
        if the_girl.arousal_perc > 100:
            "[the_girl.possessive_title] is riding you with wild abandon, as yet another orgasm wracks her body. Too late to stop, you begin cumming at the same time."
        elif the_girl.arousal_perc > 80:
            "[the_girl.possessive_title] is riding you with wild abandon, and an orgasm wracks her body. Too late to stop, you begin cumming at the same time."
        $ the_girl.cum_in_vagina()
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        "[the_girl.possessive_title]'s expert cunt draws wave after wave of cum from you. For a second you lose the ability to process anything outside the feeling of her velvet pussy wrapped perfectly around your shaft."
        the_girl "Oh [the_girl.mc_title]... I needed that so bad... Let's do that again soon okay?"
    elif the_girl.effective_sluttiness("creampie") < 60:
        the_girl "Oh shit, you can't cum inside me!"
        "[the_girl.possessive_title] lifts her hips up off of you, your twitching cock suddenly cold and aching to be back inside her."
        "She reaches down moving your member between her ass cheeks and her hand."
        "You don't have time to respond before the first wave of cum erupts from your penis."
        $ the_girl.cum_on_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ reverse_cowgirl.redraw_scene(the_girl)
        "When the last of your cum splashes onto her ass, she stops stroking you."
        "You lay back and take a few moments to enjoy the view."
    else:
        "[the_girl.title] starts to pull up and off of you. She hesitates with the tip of your cock just inside of her pussy."
        the_girl "I... I really shouldn't let you..."
        "She bites her lip and moans, unsure of what to do."
        menu:
            "Pull her down and cum inside her":
                "You reach up and grab [the_girl.possessive_title] by the hips. With one confident pull she plunges back onto your cock, gasping with pleasure."
                "The feeling of her warm, wet pussy sliding down and engulfing your cock again pushes you over the edge. You pull [the_girl.title] tight against you and unload inside of her."
                the_girl "Ah! Just... Just this once!"
                $ the_girl.call_dialogue("cum_vagina")
                $ the_girl.cum_in_vagina()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                $ the_girl.change_obedience(3)
                "You give a few half-hearted pumps when you're done, then tap [the_girl.title] on the ass. She slides off of your dick and collapses beside you."

            "Let her pull off and cum on her ass":
                "You stay silent. [the_girl.possessive_title] waits another second, as if waiting to be convinced, then pulls off of your cock."
                "She moves your cock between her ass cheeks until you fire your hot semen all over her."
                $ the_girl.cum_on_ass()
                $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
                $ reverse_cowgirl.redraw_scene(the_girl)
                the_girl "Whew, that was close..."
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    return

label transition_default_reverse_cowgirl(the_girl, the_location, the_object):
    $ reverse_cowgirl.redraw_scene(the_girl)
    "You lie down on the [the_object.name], and [the_girl.possessive_title] gets on top, facing away from you."
    "She reaches between her legs and wraps her hand around your cock. She slowly guides it into her slit and then slides the length of it inside her."
    return

label strip_reverse_cowgirl(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] straightens up a bit and peeks back at you."
    $ the_girl.call_dialogue("sex_strip")
    $ the_girl.draw_animated_removal(the_clothing, position = reverse_cowgirl.position_tag)
    "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
    "She resumes working her hips up and down on top of you with a sigh."
    return

label strip_ask_reverse_cowgirl(the_girl, the_clothing, the_location, the_object):
    "[the_girl.possessive_title] straightens up a bit and peeks back at you."
    the_girl "[the_girl.mc_title], I'd like to take off my [the_clothing.name], would you mind?"
    menu:
        "Let her strip":
            mc.name "Take it off for me."
            $ the_girl.draw_animated_removal(the_clothing, position = reverse_cowgirl.position_tag)
            "[the_girl.possessive_title] struggles out of her [the_clothing.name] and throws it to the side."
            "She resumes working her hips up and down on top of you with a sigh."
            return True

        "Leave it on":
            mc.name "No, I like how you look with it on."
            if the_girl.sluttiness < 60:
                the_girl "Do you think I look sexy in it?"
                "She bottoms herself out on top of you and starts to grind her hips into yours."
            elif the_girl.sluttiness < 80:
                the_girl "Does it make me look like a good little slut? All I want to be is your good little slut [the_girl.mc_title]."
                $ play_moan_sound()
                "She pushes her hips back into you and moans happily."
            else:
                the_girl "Does it make me look like the cum hungry slut that I am? That's all I want to be for you [the_girl.mc_title], your dirty little cum dumpster!"
                $ play_moan_sound()
                "She grinds her hips back into you and moans ecstatically."
            return False

label transition_missionary_reverse_cowgirl(the_girl, the_location, the_object):
    $ the_girl.draw_person(position = "missionary")
    "Looking down at [the_girl.possessive_title], you decide it's time to change things up a little bit."
    mc.name "Hey, why don't we change it up a bit, do you wanna be on top for a bit?"
    if the_girl.is_dominant:
        the_girl "Oh! I love being on top. Let's do it!"
        $ the_girl.change_arousal(5)
    else:
        the_girl "Sure, if that's what you want, [the_girl.mc_title]."
    "You pull off of her and let her up, then lay down on your back."
    mc.name "Why don't you ride me reverse cowgirl? Let me watch that amazing ass of yours."
    if the_girl.get_opinion_score("showing her ass") > 0:
        the_girl "Mmm, you wanna watch my booty bounce up and down on you? That sounds hot!"
        $ the_girl.change_arousal(the_girl.get_opinion_score("showing her ass"))
        "[the_girl.possessive_title] winks at you, then climbs on top you, giving her ass a bit of a shake as she climbs on."
    else:
        "[the_girl.possessive_title] blushes, but soon swings her legs over you with her back facing you."
    $ the_girl.draw_person(position = "doggy")
    "[the_girl.possessive_title] reaches down between her legs and takes hold of your penis. She gives it a couple strokes, then lines it up with her slit."
    "She pushes her hips back onto you slowly, until you are fully embedded inside her."
    return

label transition_reverse_cowgirl_doggy(the_girl, the_location, the_object):
    "While the view of her ass is amazing, you decide it is time that you took control of the situation."
    "You grab [the_girl.possessive_title]'s hips and slowly push her up off you. She looks back at you for a moment in confusion."
    mc.name "Don't worry [the_girl.title], I'm just gonna change things up. I'll be back inside you in a second."
    "You slide yourself out then get on your knees behind her."
    $ play_moan_sound()
    if the_girl.arousal_perc > 60:
        "You rub the tip of your penis against [the_girl.possessive_title]'s cunt, feeling how nice and wet she is already. She moans softly when you slide the head of your dick over her clit."
    else:
        "You rub the tip of your penis against [the_girl.possessive_title]'s cunt, getting ready to slide yourself inside."
    "When you're ready you push forward, slipping your shaft deep inside of [the_girl.possessive_title]. She gasps and quivers ever so slightly as you start to pump in and out."
    return

label orgasm_reverse_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title]'s cunt quivers and spasms around you, and then suddenly tenses up."
    $ the_girl.call_dialogue("climax_responses_vaginal")
    "[the_girl.possessive_title] stirs her womb aggressively with your erection throughout her climax."
    "After a couple of seconds [the_girl.possessive_title] sighs and the tension drains from her body."
    the_girl "God it feels so good, I wonder if you can last long enough to let me cum again..."
    return

label taboo_break_reverse_cowgirl(the_girl, the_location, the_object):
    "[the_girl.possessive_title] leads you to the [the_object.name]."
    the_girl "Lie down for me, [the_girl.mc_title]..."
    $ reverse_cowgirl.redraw_scene(the_girl)
    "You nod and follow her instructions. She steps over you and kneels down, giving you a perfect view of her ass."
    if the_girl.effective_sluttiness(reverse_cowgirl.associated_taboo) > reverse_cowgirl.slut_cap:
        "She reaches between her legs and grabs your cock, bringing it towards her and running the tip against her clit."
        "You feel her thighs tremble with pleasure."
    else:
        "She reaches behind her and grabs your cock, rubbing it between her butt cheeks."
    $ the_girl.call_dialogue(cowgirl.associated_taboo+"_taboo_break")
    "[the_girl.title] lifts herself up, puts your hard cock in line with her [the_girl.pubes_description] pussy, and starts to lower herself down."
    "You feel a moment of resistance as your cock spreads her open, then her body weight carries her all the way down your shaft."
    $ play_moan_sound()
    "She closes her eyes and moans, holding your entire length inside of her for a few seconds."
    "When she's ready she leans forward, grabs your legs and starts to move her hips up and down, giving you a perfect view of her ass bouncing up and down on your cock."
    return

label GIC_outro_reverse_cowgirl(the_girl, the_location, the_object, the_goal = None):
    $ the_goal = the_girl.get_sex_goal()

    if the_goal == "get off" or the_goal == "anal creampie" or the_goal == "facial" or the_goal == "oral creampie" or the_goal is None or the_goal == "get mc off":
        $ reverse_cowgirl.call_default_outro(the_girl, the_location, the_object)
    elif the_goal == "waste cum":
        "[the_girl.possessive_title]'s sweet cunt milks your cock, the wet friction pushes you past the point of no return."
        mc.name "Ah, I'm going to cum!"
        "[the_girl.possessive_title] looks back at you and gives you a naughty smile."
        if mc.condom:
            "At the last second, she pulls off you and pulls your condom off."
        else:
            "Her hips lift up off you. Your cock is suddenly cold and aching to be back inside of her as you get ready to cum."
        the_girl "I'm not letting you cum in me!"
        "You groan but you don't have time to take over, so you just lay back and let your orgasm overtake you."
        $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
        "She reaches down between her legs and strokes your cock, pointing it at you."
        "Thick strands of cum erupt as you orgasm. It ropes up and out over your belly."
        "When you finish you lay back and [the_girl.title] stops stroking you. She wipes her hand on your leg."
        $ the_girl.change_stats(happiness = 2, obedience = -3)
    elif the_goal == "hate fuck":
        if the_girl.on_birth_control or mc.condom:
            the_girl "Already? I guess the view of my ass was just too much for you to handle."
            if mc.condom:
                the_girl "Whatever, I'm sure the condom can handle your pathetic load."
                "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."
            else:
                the_girl "I don't feel like getting off. Go ahead and cum inside me [the_girl.mc_title], I'm on birth control anyway."
                "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                $ the_girl.cum_in_vagina()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                $ reverse_cowgirl.redraw_scene(the_girl)
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
        else:
            the_girl "Already? Is my cunt to just too much for you to handle?"
            if the_girl.wants_creampie:
                the_girl "Whatever. I want to feel you cum inside me. Not like your swimmers are strong enough to knock me up anyway."
                "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
                $ the_girl.cum_in_vagina()
                $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
                $ reverse_cowgirl.redraw_scene(the_girl)
                "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
                "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
            else:
                the_girl "Whatever. Hurry up and cum."
                "She starts to speed up. You moan as you get ready to fire your load up inside her."
                "At the last second, she pulls off. You groan as you start to cum, spraying all over your stomach."
                $ ClimaxController.manual_clarity_release(climax_type = "air", the_person = the_girl)
                "She watches as your cock twitches and finishes."
                the_girl "Look at all that wasted cum... Too bad, [the_girl.mc_title]!"
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    elif the_goal == "vaginal creampie":
        the_girl "Yes! Ah!"
        "[the_girl.title] drops herself down, grinding her hips against yours and pushing your cock as deep into her as possible."
        "Her breath catches in her throat when you pulse out your hot load of cum deep inside of her."
        $ ClimaxController.manual_clarity_release(climax_type = "pussy", the_person = the_girl)
        #the_girl "Oh my god... Give it all to me [the_girl.mc_title]... Fill me up..."
        if mc.condom:
            "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
            "The tip of your condom is ballooned out and hanging to the side, filled with your warm seed."

            call post_orgasm_condom_routine(the_girl, reverse_cowgirl) from _call_post_orgasm_condom_routine_reverse_cowgirl

        elif the_girl.has_role(breeding_fetish_role):
            the_girl "That's it! Inside me! I need that seed deep!"
            $ the_girl.cum_in_vagina()
            $ reverse_cowgirl.redraw_scene(the_girl)
            "As you finish, you can feel her working her vaginal muscles, milking the cum from your cock as best she can."
            "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
            "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
        else:
            $ the_girl.call_dialogue("cum_vagina")
            $ the_girl.cum_in_vagina()
            $ reverse_cowgirl.redraw_scene(the_girl)
            "She rocks herself back and forth on you until you're completely spent, then she pulls up and lets your dick fall out of her."
            "[the_girl.possessive_title] straddles you for a few more seconds as she catches her breath. Your cum drips out of her and onto your stomach."
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    elif the_goal == "body shot":
        the_girl "Ohhh, cum all over my ass!"
        if mc.condom:
            "[the_girl.possessive_title] pulls off you, reaches down and pulls your condom off, and begins stroking you."
        else:
            "[the_girl.possessive_title] pulls off you, reaches down, and begins to stroke you."
        "She strokes you and simultaneously points your cock at her ass."
        $ the_girl.cum_on_ass()
        $ ClimaxController.manual_clarity_release(climax_type = "body", the_person = the_girl)
        $ the_girl.draw_person(position = "missionary")
        "She rolls off and lies next to you on the [the_object.name]."
    elif the_goal == "oral creampie":
        the_girl "Wait! I want it in my mouth!"
        if mc.condom:
            "[the_girl.possessive_title] pulls off you, but quickly moves down your body. She pulls off the condom and takes you into her mouth."
        else:
            "[the_girl.possessive_title] pulls off you, but quickly moves down your body and takes you into her mouth."
        $ the_girl.draw_person(position = "kneeling1")
        $ play_moan_sound()
        "She moans as your cum begins to spill into her mouth"
        $ the_girl.cum_in_mouth()
        $ ClimaxController.manual_clarity_release(climax_type = "mouth", the_person = the_girl)
        $ the_girl.draw_person(position = "kneeling1")
        "You let out a shuddering moan as you cum, pumping your sperm into [the_girl.possessive_title]'s eager mouth. She makes sure to wait until you're completely finished."
        $ play_swallow_sound()
        "[the_girl.title] closes her mouth and swallows loudly."
        "It takes a few big gulps to get every last drop of your cum down, but when she opens up again it's all gone."
    else:
        $ reverse_cowgirl.call_default_outro(the_girl, the_location, the_object)
