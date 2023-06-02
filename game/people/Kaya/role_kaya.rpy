# Kaya is a new unique character. Kaya starts out working at the coffee shop after Alexia gets hired.
# Kaya is working at the coffee shop to get through college. Her mother was previously supporting her, but has fallen ill and can't afford to anymore.
# Kaya is the daughter of Sakari, who will be introduced later in the story. MC meets Kaya at the coffee shop after she starts working there.
# As MC gets to know Kaya, he learns about her money problems. Working with HR director, MC can start an intern project for college students to work at the company on the weekend.
# Weekend staffing is limited and is limited to Research and production departments (no suppliers open to buy supplies or sell serums, for now no HR? Maybe add HR in the future?)
# Eventually, MC meets Sakari and discovers his father had an affair with her and Kaya is a half sister.
# Kaya and her mother have native american heritage
# Use mod code to have her deny lunch dates due to being at work, require different date time.

style kaya_lang:
    outlines [ (absolute(4), "#080", absolute(0), absolute(0)) ]

init 2 python:
    list_of_instantiation_functions.append("create_kara_character")

    def create_kara_character():
        kaya_base_outfit = Outfit("kaya's base accessories")
        the_eye_shadow = heavy_eye_shadow.get_copy()
        the_eye_shadow.colour = [.26, .14, .21, 0.33]
        the_lipstick = lipstick.get_copy()
        the_lipstick.colour = [1.0, .21, .14, 0.33]
        the_bracelets = colourful_bracelets.get_copy()   #Change this
        the_bracelets.colour = [.71,.4,.85,1.0]
        kaya_base_outfit.add_accessory(the_eye_shadow)
        kaya_base_outfit.add_accessory(the_lipstick)
        kaya_base_outfit.add_accessory(the_bracelets)

        #global kaya_role
        global kaya
        kaya = make_person(name = "Kaya", last_name ="Greene", age = 22, body_type = "thin_body", face_style = "Face_3",  tits="B", height = 0.94, hair_colour="black", hair_style = messy_hair, skin="tan" , \
            eyes = "brown", personality = kaya_personality, name_color = "#f0defd",  \
            stat_array = [1,4,4], skill_array = [1,1,3,5,1], sex_skill_array = [4,2,2,2], sluttiness = 7, obedience_range = [70, 85], happiness = 88, love = 0, \
            relationship = "Single", kids = 0, force_random = True, base_outfit = kaya_base_outfit, type = 'story',
            forced_opinions = [["billiards", 2, False], ["work uniforms", -1, False], ["flirting", 1, False], ["working", 1, False], ["the colour green", 2, False], ["pants", 1, False], ["the colour yellow", 2, False], ["the colour red", 1, False]],
            forced_sexy_opinions = [["vaginal sex", 2, False], ["bareback sex", 2, False], ["drinking cum", -1, False], ["giving blowjobs", -1, False], ["missionary style sex", 2, False], ["creampies", 2, False]])

        kaya.generate_home()
        kaya.home.background_image = student_apartment_background
        kaya.set_schedule(kaya.home, the_times = [0,1,2,3,4])
        kaya.change_job(unemployed_job)
        kaya.home.add_person(kaya)

        # kaya_mod_initialization():
        # kaya.event_triggers_dict["intro_complete"] = False    # True after first talk
        # kaya.event_triggers_dict["drink_date_complete"] = False
        # kaya.event_triggers_dict["can_get_drinks"] = False
        # kaya.event_triggers_dict["can_get_barista_quickie"] = False
        # kaya.event_triggers_dict["has_moved"] = False
        # kaya.event_triggers_dict["has_started_internship"] = False
        # kaya.event_triggers_dict["barista_fuck_last_day"] = 9999
        # kaya.event_triggers_dict["studies_with_lily"] = False
        # kaya.event_triggers_dict["incest_warnings"] = 0
        # kaya.event_triggers_dict["no_condom_talk"] = False
        # kaya.event_triggers_dict["mc_knows_relation"] = False
        # kaya.event_triggers_dict["sakari_has_died"] = False

        mc.business.add_mandatory_crisis(kaya_setup_intro_event) #Add the event here so that it pops when the requirements are met.

        if persistent.pregnancy_pref != 0:
            kaya.on_birth_control = False
        return

init -2 python:
    def kaya_setup_intro_event_requirement():
        if alexia.is_employee and alexia.days_employed > 7:
            return True
        return False

    def kaya_intro_requirement(the_person):
        if the_person.location == coffee_shop and the_person.is_at_work:
            return True
        return False

    def kaya_ask_out_requirement(the_person):
        if the_person.event_triggers_dict.get("move_help_day", 0) != 0: # she stops going out with MC
            return False
        if the_person.location == coffee_shop and the_person.is_at_work and the_person.love > 20 and time_of_day == 3 and not kaya_can_get_drinks():
            return not mc.business.date_scheduled_today()
        return False

    def kaya_get_drinks_requirement(the_person):
        if the_person.event_triggers_dict.get("move_help_day", 0) != 0: # she stops going out with MC
            return False
        if the_person.location != the_person.job.job_location:
            return False
        if the_person.love < 20:
            return "Requires 20 love"
        if mc.business.date_scheduled_today():
            return "You already have plans tonight"
        if time_of_day != 3:
            return "Check in the evening"
        return True

    # def kaya_add_HR_program_event_requirement(): #Not attached to anything
    #     if mc.business.hr_director is not None and renpy.random.randint(0,5) == 1:
    #         return True
    #     return False

    def kaya_meet_lily_at_uni_requirement(the_person):
        if the_person.location == university and day%7 != 1 and the_person.sluttiness > 20 and kaya_has_had_drink_date():
            return True
        return False

    def kaya_meet_erica_at_uni_requirement(the_person):
        if the_person.location == university and day%7 != 1 and the_person.sluttiness > 20 and kaya_has_had_drink_date():
            return True
        return False

    def kaya_lily_study_night_intro_requirement():
        if not lily.has_job(sister_student_job):
            return False
        if day%7 == 1 and time_of_day == 4:
            return True
        return False

    def kaya_lily_study_night_apology_requirement(the_person):
        if not lily.has_job(sister_student_job):
            return False
        if the_person.location == coffee_shop:
            return True
        return False

    def kaya_lily_study_night_recurring_requirement(the_person):
        if not lily.has_job(sister_student_job):
            return False
        if the_person.event_triggers_dict.get("last_lily_study_night", 0) >= day:
            return False
        if day%7 == 1 and time_of_day == 4 and the_person.location == lily.home:    #TODO double check and make sure this actually works...
            return True
        return False

    def kaya_uni_scholarship_intro_requirement(the_person):
        # don't start internship before she moved out (changes her job and will lock out the move out / sakari intro)
        if not the_person.event_triggers_dict.get("has_moved", False):
            return False
        if the_person.love > 40 and mc.business.has_funds(10000) and the_person.location == university and day%7 < 4:
            return True
        return False

    def kaya_HR_start_internship_program_requirement():
        if mc.business.is_open_for_business and mc.is_at_work and mc.business.hr_director.is_at_work:
            return True
        return False

    def kaya_first_day_of_internship_requirement():
        if day%7 == 5 and time_of_day <= 1:
            return True
        return False

    def kaya_moving_in_with_mother_intro_requirement(the_person):
        if kaya.sluttiness > 40 and the_person.location == coffee_shop and kaya_studies_with_erica():
            return True
        return False

    def kaya_asks_for_help_moving_requirement():
        if day >= kaya.event_triggers_dict.get("move_help_day", 9999) and time_of_day == 4 and day%7 != 6:#MAke sure moving day does not conflict with monday meeting
            return True
        return False

    def kaya_moving_day_requirement():
        if time_of_day == 1: # move on morning transition / not early morning
            return True
        return False

    def kaya_share_the_news_requirement():
        if day >= kaya.event_triggers_dict.get("share_news_day", 9999) and time_of_day == 3 and kaya.location == coffee_shop:
            return True
        return False

    def kaya_jennifer_reveal_requirement(the_person):
        return False

    def kaya_lily_reveal_requirement(the_person):
        return False

    def kaya_barista_fuck_intro_requirement(the_person):
        if the_person.location == coffee_shop and time_of_day == 2 and the_person.sluttiness >= 60:
            return True
        return False

    def kaya_barista_fuck_requirement(the_person):
        if kaya_can_get_barista_quickie():
            if kaya.event_triggers_dict.get("barista_fuck_last_day", 9999) + 3 <= day:
                if time_of_day == 2:
                    if the_person.location == coffee_shop:
                        return True
                    else:
                        return "Only at the coffee shop"
                else:
                    return "Only in the afternoon"
            else:
                return "Wait a few days"
        return False

    def kaya_work_fuck_requirement(the_person):
        if kaya_can_get_work_quickie():
            if kaya.event_triggers_dict.get("work_fuck_last_day", 9999) + 3 <= day:
                if time_of_day == 2:
                    if the_person.location == mc.business.r_div:
                        return True
                    else:
                        return "Only at your business"
                else:
                    return "Only in the afternoon"
            else:
                return "Wait for next week"
        return False

    def kaya_jennifer_confrontation_requirement():
        if willing_to_threesome(kaya, mom):
            return True
        return False

init 3 python:
    kaya_setup_intro_event = Action("Kaya Setup", kaya_setup_intro_event_requirement, "kaya_setup_intro_event_label")
    kaya_intro = Action("Meet Kaya",kaya_intro_requirement,"kaya_intro_label")
    kaya_ask_out = Action("Ask to get drinks",kaya_ask_out_requirement,"kaya_ask_out_label")    #20 love
    kaya_moving_in_with_mother_intro = Action("Kaya can't drink",kaya_moving_in_with_mother_intro_requirement,"kaya_moving_in_with_mother_intro_label") #40 slut
    kaya_asks_for_help_moving = Action("Kaya Needs Help",kaya_asks_for_help_moving_requirement,"kaya_asks_for_help_moving_label")   #40 love + 40 slut
    kaya_moving_day = Action("Kaya Moves",kaya_moving_day_requirement,"kaya_moving_day_label")
    kaya_meet_lily_at_uni = Action("Kaya and Lily Meet",kaya_meet_lily_at_uni_requirement,"kaya_meet_lily_at_uni_label")    #20 slut
    kaya_meet_erica_at_uni = Action("Kaya and Erica Meet",kaya_meet_erica_at_uni_requirement,"kaya_meet_erica_at_uni_label")
    kaya_lily_study_night_intro = Action("Kaya and Lily Study",kaya_lily_study_night_intro_requirement,"kaya_lily_study_night_intro_label")
    kaya_lily_study_night_recurring = Action("Kaya and Lily Study",kaya_lily_study_night_recurring_requirement,"kaya_lily_study_night_recurring_label")
    kaya_lily_study_night_apology = Action("Apologize to Kaya",kaya_lily_study_night_apology_requirement,"kaya_lily_study_night_apology_label")
    kaya_uni_scholarship_intro = Action("Start scholarship program",kaya_uni_scholarship_intro_requirement,"kaya_uni_scholarship_intro_label")
    kaya_HR_start_internship_program = Action("Discuss scholarship with HR",kaya_HR_start_internship_program_requirement,"kaya_HR_start_internship_program_label")
    kaya_first_day_of_internship = Action("Kaya's first day as intern",kaya_first_day_of_internship_requirement,"kaya_first_day_of_internship_label")
    kaya_share_the_news = Action("Share the news with Kaya",kaya_share_the_news_requirement,"kaya_share_the_news_label")    #60 love
    kaya_jennifer_reveal = Action("Talk to Jennifer about Kaya",kaya_jennifer_reveal_requirement,"kaya_jennifer_reveal_label")
    kaya_lily_reveal = Action("Talk to Lily about Kaya", kaya_lily_reveal_requirement,"kaya_lily_reveal_label")
    kaya_barista_fuck_intro = Action("Kaya takes a break at work", kaya_barista_fuck_intro_requirement,"kaya_barista_fuck_intro_label")
    kaya_barista_fuck = Action("Fuck her on her break", kaya_barista_fuck_requirement,"kaya_barista_fuck_label")
    kaya_get_drinks = Action("Ask to get drinks",kaya_get_drinks_requirement,"kaya_get_drinks_label")
    kaya_work_fuck = Action("Fuck her on her break", kaya_work_fuck_requirement, "kaya_work_fuck_label")

label kaya_setup_intro_event_label():
    python:
        # init kaya role
        kaya_role = Role(role_name ="kaya", actions =[kaya_barista_fuck, kaya_get_drinks, kaya_work_fuck], hidden = True)
        kaya_barista_job = Job("Barista", [kaya_role, generic_student_role], coffee_shop, work_times = [2, 3])
        kaya.change_job(kaya_barista_job, job_known = True)
        # she also studies
        kaya.set_schedule(None, the_times = [1,2,3])    # Free roam
        kaya.set_schedule(university, the_days = [0, 1, 2, 3, 4], the_times = [1])
        kaya.add_unique_on_room_enter_event(kaya_intro)
    return

label kaya_intro_label(the_person):
    "Even though it is later in the day, you decide to swing by the coffee-shop for a pick me up."
    $ mc.change_location(coffee_shop)
    $ the_person.draw_person()
    "When you step inside, there's a new girl working there you haven't seen before."
    "You listen as the person ahead of you orders."
    "?????" "Yes I'd like a tall macchiato with whipped cream."
    the_person "Is that all?"
    "When she talks, there is a slight accent. It's subtle, and you have trouble placing it."
    "You quickly check behind you. No one in line behind you yet... maybe you can chat with her for a bit?"
    "The person in front of you moves to wait for their drink."
    the_person "Hi, what can I get you?"
    "That accent... where is it from? It's starting to bother you..."
    the_person "{=kaya_lang}Kia ora? {/=kaya_lang}(?????)... Do you want to order?"
    "Ah! You zoned out for a second. What was that word?"
    mc.name "Yes, sorry. I was trying to place your accent, but I can't. I'll just take a large coffee, leave room for cream."
    the_person "Okay. Is that all?"
    mc.name "Yeah..."
    "You pay for your coffee, but stand still."
    mc.name "You know, I've been coming here for a while but haven't seen you before. You just get hired?"
    the_person "Yeah, I'm going to school part time at the university, and I picked up this job to help pay tuition."
    mc.name "Ah, good for you. Well, best of luck with your studies. If you are as smart as you are beautiful, I'm sure you will do well."
    the_person "Ah, thank you..."
    mc.name "I'm [mc.name]."
    the_person "[the_person.fname]."
    $ the_person.set_title(the_person.name)
    $ the_person.set_possessive_title("Your favorite barista")
    $ the_person.set_mc_title(mc.name)
    mc.name "It's a pleasure to meet you."
    "Right then another employee puts your coffee on the counter and calls your name."
    the_person "Right... sorry, there's someone behind you..."
    "You hear a throat clear behind you. You grab your coffee and move out of the way."
    "Well, the new barista is cute! Maybe you should try to get to know her more..."
    $ the_person.add_unique_on_room_enter_event(kaya_ask_out)
    $ kaya.event_triggers_dict["intro_complete"] = True
    return

label kaya_ask_out_label(the_person): #Requires 20 love, substitute for first date.
    if not kaya_can_get_drinks():
        $ kaya.event_triggers_dict["can_get_drinks"] = True
        "You step into the coffee shop. You wonder if [the_person.title] is working. It is almost closing time."
        $ the_person.draw_person()
        "Sure enough, as you step inside, there she is. You've been getting to know her more lately, and you feel ready to ask her out."
        "When you step up to the counter, she smiles at you."
        $ the_person.draw_person( emotion = "happy")
        the_person "Good evening [the_person.mc_title]. What can I get you?"
        mc.name "I'll take a small coffee with room for cream... and I was hoping to ask you something."
        the_person "Okay, I can do that... and what is the question?"
    mc.name "I was ahhh, wondering if you were doing anything after you got off work today?"
    the_person "No, I don't have any plans. You umm... have any particular reason for asking?"
    mc.name "I know a good bar around the corner... I thought maybe we could get a drink?"
    the_person "Oh! I... you seem pretty nice... yeah I guess I could do that!"
    mc.name "Great! Tell you what, I'll take my coffee out to the patio... whenever you get off, I'll walk you over there?"
    the_person "Okay... don't worry I get off soon!"
    $ clear_scene()
    $ mc.change_location(downtown)
    "You step outside and sit down, sipping your coffee."
    "You spend some time on your phone, and follow up on a couple of work emails while you wait. It's a pretty pleasant evening."
    "Pretty soon you hear [the_person.possessive_title] clear her throat nearby. You look up from your phone."
    # change out of uniform
    $ the_person.apply_outfit(the_person.decide_on_outfit())
    $ the_person.draw_person()
    mc.name "Ah, you're right, that was quick!"
    the_person "Yes... hey... I need to be honest about something..."
    mc.name "Oh? Did you change your mind? It's quite alright..."
    the_person "No, I'd still like to go and hang out, but I won't be able to have any drinks."
    mc.name "Ah, you don't drink?"
    the_person "No, it's not that, I'm just... with school and some other stuff going on... money is just really tight right now..."
    mc.name "Oh! Why don't you let me pick up the tab tonight?"
    the_person "I couldn't let you..."
    mc.name "Just pretend like I left a 20 in your tip jar, and you wanted to treat yourself."
    the_person "I suppose... just a couple, okay?"
    mc.name "Great! Let's go."
    "You stand up, making sure to throw your coffee cup away and leave the table clean. You start to walk with [the_person.title] a couple blocks to the bar."
    the_person "So... sorry if I'm like... misreading this... but... is this like... a date?"
    "She seems to be in tune with your intentions."
    mc.name "Well [the_person.title], I'm certainly interested in getting to know you better! And I have to say I like what little I know about you so far..."
    mc.name "I can hardly think of a better way to learn more about you than a date!"
    $ the_person.change_love(2)
    the_person "Ahhh... I'm glad to know I wasn't mistaken."
    $ mc.change_location(downtown_bar)
    "Soon, you arrive at the bar. You point her to a high top you spot that looks open."
    mc.name "Hey, if you want to go grab that table, what is your drink of choice?"
    the_person "Oh, umm, let me walk up with you instead, I want to see if they have any specials."
    mc.name "Okay. With company as pretty as you we'll probably getting served faster anyway!"
    $ the_person.change_happiness(3)
    "She smiles and accepts your compliment. You walk up to the bar with her. Soon the bartender comes over."
    "?????" "Hey there. Never seen you around here before, what can I get you?"
    the_person "Hi! Are you running any specials tonight?"
    "?????" "Well, we got domestic beers for $2, some imports for $3, and rail drinks for $4."
    the_person "Ah, can I get a rum and coke please?"
    "You wonder if she's just trying to be considerate? You would hardly expected a girl like her to order that as a first choice..."
    "You must have given her a funny look."
    the_person "What? You seem like a nice guy, I just want to be a cheap date!"
    "Ah, so she must be very budget conscious. You suppose there are certainly worse personality traits to have!"
    "You order yourself an Old Fashioned, something to sip on while you chat."
    "Once you have your drinks, you look around. The table you were looking at is full... looks like everything is full..."
    the_person "Ah! Look! An open pool table! Let's play!"
    $ the_person.discover_opinion("billiards")
    "[the_person.possessive_title] gets really excited. She must really enjoy billiards?"
    "She takes a sip of her drink, then sets it down on the side of the pool table. You do the same."
    mc.name "So tell me, cheap date, what happens to be your actual favorite cocktail?"
    the_person "Why so interested? Trying to get me drunk?"
    mc.name "Honestly, I feel like a person's favorite drink says a lot about them."
    the_person "Is that so?"
    mc.name "Absolutely. I know I'm dealing with immature college girls when the answer I get is some ridiculous drink like 'sex on the beach'."
    the_person "Ha! Yeah I suppose."
    "[the_person.title] pulls some quarters out of her purse and puts them in the table. She pays the cost of a game and you hear the billiard balls fall into the gully."
    mc.name "But you... you seem much too practical for something like that. You seem like the type that would enjoy finer spirits."
    "[the_person.possessive_title] is pulling the balls from the gully and setting them on the table. She looks at you and smirks."
    the_person "Ah, is that so?"
    mc.name "Indeed. And the fact that you don't deny it tells me I'm right."
    the_person "You sure seem pretty confident in yourself there, mister! Tell you what. Let's play a round, and if you win, I'll tell you my favorite drink. Okay?"
    mc.name "Ah, who's confident now? Placing a wager on a billiards game!"
    "She chuckles and rolls her eyes mockingly."
    the_person "Disclosing my favorite drink hardly seems like a major wager. Maybe I intend to lose, so you can learn my secret? You're the one buying the drinks, remember?"
    the_person "Tell you what, if I win, I'll even allow you a guess, and I'll tell you if you're right or not."
    mc.name "That seems more than fair. If I can't get it right, I think I can get close."
    "She picks up her drink and takes a long sip. Then grabs her pole."
    the_person "Here, rack these up, will you?"
    "In here goes a brief billiards game Starbuck hasn't made yet. It uses MC's intelligence to determine if he wins or loses. Today you win!"
    $ _return = True
    # call play_billiards(the_person) from _kaya_first_billiards_01
    if _return: #You won
        the_person "Wow, I'm impressed! Do you play much?"
        mc.name "Not particularly. But It's a game of angles, and math has always been a strong subject for me."
        the_person "I see."
        mc.name "Now, about our wager?"
        the_person "Okay okay. If you really want to know..."
        the_person "My favorite cocktail is a Manhattan with an orange twist."
    else:
        mc.name "Wow, you are very good at pool! That was very impressive."
        the_person "Thank you. I love to play. It is a good exercise for your dexterity and your brain."
        mc.name "I agree. Now, about the wager..."
        the_person "Yes, this should be interesting. Go ahead, think about it and guess my favorite drink."
        "It is clear to you so far that [the_person.possessive_title] is intelligent and practical. However, even though she is strapped for money right now, you get the feeling things haven't always been this way for her."
        "Rum is too simple a spirit for her to favor. She probably favors gin or whiskey."
        "Something about her dark skin has you guessing it might be a darker spirit too, so you decide to guess a classic whiskey cocktail."
        menu:
            "Whiskey sour":
                pass
            "Highball":
                pass
            "John Collins":
                pass
        the_person "Wow. I admit, I was thinking that you were pretty full of shit, but that's actually really close! Close enough for me anyway!"
        mc.name "Oh?"
        the_person "My favorite cocktail is definitely a Manhattan with an orange twist."
    mc.name "Ah, a bold drink indeed. I was definitely thinking something whiskey inspired, but I would not have guessed that."
    the_person "Yeah. Sometimes I'll have one, but to make a good one it requires good whiskey. The ones you get with more affordable varieties just aren't as good."
    mc.name "Yes, a quality of many whiskey-heavy drinks, I think. Well, we seem to be ready for another round?"
    the_person "I umm... I'm kind of out of quarters..."
    mc.name "Here, let me go get us a couple more drinks and some quarters. I'm not quite ready to say goodbye for the evening yet."
    $ the_person.change_love(2)
    the_person "I suppose I could stay out for a bit longer."
    # $ mc.business.add_mandatory_crisis(kaya_get_drinks)
    $ kaya.event_triggers_dict["bar_date"] = True
    $ clear_scene()
    "You walk back up to the bartender. You order yourself another Old Fashioned and a top shelf Manhattan with an orange twist for [the_person.title]."
    "When he brings you the drinks, you ask for change for a dollar to play another round of pool. When he goes to make change for you, you look down at the drinks..."
    "You could probably slip a serum into her drink if you do it quickly..."
    call give_serum(the_person) from _call_give_kaya_serum_bar_01
    "You walk back to the pool table. She smirks when she sees your drink for her."
    $ the_person.draw_person()
    the_person "Ah, so you ARE trying to get me drunk then? Ahhh, {=kaya_lang}koretake {/=kaya_lang}(?????)."
    mc.name "As... what now?"
    the_person "Ah... sorry... as you might have guessed, English isn't my first language."
    "She takes a sip from her drink."
    the_person "My mom thought it was important for me to learn my native tongue first, even though no one really speaks it anymore."
    the_person "Sometimes I still find myself using words from it by accident."
    mc.name "Ah, I see. So what language is your first language?"
    the_person "Well, my family and I are natives... from before white colonization here."
    mc.name "That's very interesting! I'm not sure I've ever met a native."
    the_person "Well, to be honest, there aren't many of us left, and even fewer off of reservations."
    "You take a moment to think about it. You take the coins from the bartender and walk around the pool table, starting up another game."
    the_person "We playing for anything this time? It's kinda fun when there are stakes..."
    mc.name "Sounds good to me. I set the stakes last match, how about you set them for this one?"
    the_person "Hmmm... okay. How about, if I win, you have to walk me home?"
    mc.name "You know I was planning to offer to do that anyway, right?"
    the_person "Probably, but now you'll HAVE to!"
    mc.name "Ah. Well, in that case, if I win, you have to let me take you out for drinks again another time."
    the_person "Free drinks? Deal. I might have to lose on purpose!"
    "Another billiards game Starbuck hasn't made yet! What luck you get to skip it!"
    $ _return = True
    #call play_billiards(the_person) from _kaya_first_billiards_02
    if _return: #You won
        the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
        mc.name "The horror!"
        the_person "Guess I'll just have to walk myself home now, dreading the day the mysterious stranger shows up at the coffee-shop and demands my presence again!"

    else:
        the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
        mc.name "Too bad you didn't make that your wager then."
        "At first she looks at you, a bit startled, thinking you mean you don't want to, but then realizes you are teasing her"
        the_person "Guess you'll just have to walk me home and we'll go our separate ways then."
    "The teasing between you two has definitely become playful. You are really enjoying her company."
    the_person "But uh... we're doing both... right?"
    mc.name "Of course."
    "You both finish off what is left of your drinks, then leave the bar together."
    $ mc.change_location(downtown)
    "You step out on to the sidewalk and start to walk [the_person.possessive_title] home. Sensing a connection with her, you hold out your hand and she takes it."
    mc.name "So, you're going to class at the university, right?"
    the_person "That's right."
    mc.name "What are you studying?"
    the_person "I'm majoring in biology, but I'm hoping once I graduate to get into med school..."
    mc.name "Wow. So you want to be a doctor?"
    the_person "Yeah... something like that..."
    "She is quiet for a little bit, before she resumes."
    the_person "I know this might sound silly, but my mother is really the last family I have left. She's always had some recurring health issues, but lately they've been getting worse I think."
    the_person "It sucks... I know I'll never finish school in time to do anything for her... but I think I want to get into research. You know? Learn how to help other people. People like her."
    mc.name "She must be a great woman for you to look up to her like that."
    the_person "Yeah. She really is. She inspires me every day."
    mc.name "I can understand that. Did I tell you I run a pharmaceutical company? We do our own research and development, although not for any major medical illnesses."
    the_person "Really? That's pretty interesting. You're a very interesting man [the_person.mc_title]."
    "You walk in silence a bit longer with [the_person.title]."
    $ the_person.learn_home()
    "Soon you walk up to the steps of a run down apartment building. This must be where she is living."
    the_person "Hey, I just want to say, it's been a long time since I had a night like this to just relax and have fun. I had a great time... please come back and see me at the coffee shop, okay?"
    mc.name "Your charm is difficult to resist. And the coffee is good too."
    $ the_person.draw_person(position = "kissing")
    "[the_person.title] holds her arms out for a hug, and you draw her close. She is looking up at you, and feeling right, you kiss her."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
    "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
    $ the_person.change_arousal(15)
    $ the_person.break_taboo("kissing")
    "You keep making out for several more seconds until [the_person.title] breaks it off and then steps back."
    $ the_person.draw_person()
    the_person "God you are hot..."
    mc.name "Can I umm... come up?"
    the_person "Oh... I'm sorry... this was just a first date! I couldn't possibly after just once..."
    mc.name "That's okay. I'm sorry I didn't mean to make you uncomfortable."
    the_person "It didn't at all. We umm... we just need to get to know each other better. Okay?"
    mc.name "Sounds great. I'll see you around?"
    the_person "Bye!"
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] turns and starts to walk up the stairs of her apartment building."
    $ clear_scene()
    "Wow, what a busy night! You feel like you have a connection with [the_person.title]. She definitely seems eager too..."
    $ the_person.add_unique_on_room_enter_event(kaya_moving_in_with_mother_intro)   #Link this for now. Probably will change to a different place later on.
    $ the_person.add_unique_on_room_enter_event(kaya_meet_erica_at_uni)
    $ kaya.event_triggers_dict["drink_date_complete"] = True
    call advance_time() from _call_advance_time_kaya_ask_out
    return

label kaya_get_drinks_label(the_person):  #Repeatable date night with Kaya
    if the_person.event_triggers_dict.get("drink_date_count", 0) < 1:
        $ the_person.event_triggers_dict["drink_date_count"] = 1
    else:
        $ the_person.event_triggers_dict["drink_date_count"] = +1
    if not kaya_can_get_drinks():
        $ kaya.event_triggers_dict["can_get_drinks"] = True
        call kaya_ask_out_label(the_person) from _call_kaya_ask_out_label
    else:
        mc.name "How about a couple drinks tonight?"
        the_person "Sounds great! It's almost closing time, and I'm solo tonight. If you want to just grab a seat while I close up, we can walk over together."

        # "This will eventually be a full date that you can go on with [the_person.title], but it hasn't been written yet."
        # "You will have the chance to give her a serum though, so for now this is just a placeholder option to give her a serum."

        $ clear_scene()
        $ mc.change_location(downtown)
        "You step outside and sit down, sipping your coffee."
        "You spend some time on your phone, and follow up on a couple of work emails while you wait. It's a pretty pleasant evening."
        "Pretty soon you hear [the_person.possessive_title] clear her throat nearby. You look up from your phone."
        # change out of uniform
        $ the_person.apply_outfit(the_person.decide_on_outfit())
        $ the_person.draw_person()
        mc.name "Ah, you're right, that was quick!"
        "You stand up, making sure to throw your coffee cup away and leave the table clean. You start to walk with [the_person.title] a couple blocks to the bar."
        $ mc.change_location(downtown_bar)
        "Soon, you arrive at the bar. You point her towards an empty pool table."
        mc.name "Hey, if you want to go grab that table, I'll get us some drinks."
        "You order yourself an Old Fashioned and a Manhattan with an orange twist for [the_person.title]."
        "The bartender finishes them up quickly and you hand over some cash."
        "He thanks you and turn to walk down the bar to another customer. You are fairly alone at this corner of the bar, behind a support post."
        "You could probably slip a serum into her drink if you do it quickly..."
        call give_serum(the_person) from _call_give_kaya_serum_bar_02
        "By the time you get back [the_person.title] has the balls ready for you and trades you a stick for her drink."
        the_person "We playing for anything this time? It's kinda fun when there are stakes..."
        mc.name "Sounds good to me. Same stakes as last time?"
        the_person "What do you mean? Last time you won then you walked me home anyway and here we are having drinks again."
        mc.name "Seemed like a perfect outcome to me."
        $ the_person.change_stats(love = 2, happiness = 2)
        the_person "Yeah, I guess it's not too bad."
        "Another billiards game Starbuck hasn't made yet! What luck you get to skip it!"
        $ _return = True
        #call play_billiards(the_person) from _kaya_first_billiards_02
        if _return: #You won
            the_person "Oh no! Now I have to subject myself to another night of free drinks and billiards!"
            mc.name "The horror!"
        else:
            the_person "Well, I won! But... I still think you should have to take me out for drinks again some time."
            mc.name "I suppose that could be arranged."
        the_person "But uh... we're doing both... right?"
        mc.name "Of course."
        "You both finish off what is left of your drinks, then leave the bar together."
        $ mc.change_location(downtown)
        "You step out on to the sidewalk and start to walk [the_person.possessive_title] home. She reaches out for your hand before you have time to offer it."
        # put something here
        $ the_person.draw_person(position = "kissing")
        "[the_person.title] leans close and goes up on her toes, obviously hoping for something, and feeling right, you kiss her."
        $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
        "She responds immediately and starts kissing you back. Her mouth opens and your tongues intertwine in a passionate kiss."
        "Your hands start to roam around [the_person.possessive_title]'s back. She gives a little moan when your hand wanders down to her ass, but reaches back and moves your hand back up."
        $ the_person.change_arousal(15)
        $ the_person.change_slut(2, 30)
        "You keep making out for several more seconds until [the_person.title] breaks it off and then steps back."
        $ the_person.draw_person()
        the_person "God you are hot..."
        mc.name "Can I umm... come up?"
        the_person "Oh... I'm sorry... not yet..."
        mc.name "That's okay. I'm sorry I didn't mean to make you uncomfortable."
        the_person "It didn't at all. We umm... we just need to get to know each other better. Okay?"
        mc.name "Sounds great. I'll see you around?"
        the_person "Bye!"
        $ the_person.draw_person(position = "walking_away")
        "[the_person.possessive_title] turns and starts to walk up the stairs of her apartment building."
        $ clear_scene()
        "Wow, what a busy night! You feel like you have a connection with [the_person.title]."
        "Something is holding her back, you should probably see if you can make her more promiscuous before your next date."
        if kaya_studies_with_erica():
            "Maybe her Tuesday night study sessions with [erica.fname] could help you make progress."
    call advance_time() from _call_advance_time_kaya_drink
    return

label kaya_meet_lily_at_uni_label(the_person):    #This label starts Kaya and Lily friendship storyline. Requires mid Kaya love (>40?). REquires scholarship program.
    $ scene_manager = Scene()
    "You go for a stroll at the university. With no particular aim, you just walk around, checking out some of the girls, stretching your legs a bit."
    the_person "[the_person.mc_title]? Is that you?"
    $ scene_manager.add_actor(the_person)
    "You turn and see [the_person.possessive_title]. She goes to class here, but it is a big school, so you are surprised to see her."
    mc.name "Ah, hello there [the_person.title]."
    "She gives you a smile and chirps at you."
    the_person "We go out one night for drinks and you are stalking me at class, mister?"
    "[the_person.title] is very quick-witted. You can tell she is half-joking... but also seriously wanting to know what you are doing here."
    mc.name "Ah, sorry I wasn't looking for you, to be honest... I was... er..."
    "Just then, you are saved by another familiar voice."
    lily "Oh hey, [lily.mc_title]!"
    $ scene_manager.add_actor(lily, display_transform = character_center_flipped)
    "[lily.possessive_title] walks up."
    lily "You didn't tell me you were gonna be here! Want to grab some lunch?"
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "Ahhh... I see... you aren't here to see me..."
    "[lily.title] suddenly realizes you were talking with [the_person.possessive_title]. The edge of jealously is clear in [the_person.title]'s voice."
    lily "Oh! Sorry, I didn't realize you were talking to her..."
    mc.name "Ah, let me introduce you. [the_person.fname], this is my sister, [lily.fname]. She is taking classes here also."
    $ scene_manager.update_actor(the_person, emotion = "happy")
    "Relief is obvious on the face of [the_person.title]."
    the_person "Ah! Of course, you look so similar. Of course you are siblings! Nice to meet you."
    lily "Nice to meet you! Watch out for this guy though... he probably doesn't want you to know this but... he's a total nerd."
    the_person "Is that so?"
    "The two girls start to chat a bit, mostly at your expense. That's okay though, they seem to be hitting it off."
    if lily.has_taboo(["vaginal_sex", "sucking_cock", "anal_sex"]): #This is our check to see if anything serious has happened with Lily yet.
        "As you look at the two girls, you are suddenly struck by how similar they are. The way they talk and relate to each other."
        "[the_person.title] cracks a joke... they almost laugh the same? It's a little crazy how similar they are."
        "While you are really attracted to [the_person.possessive_title], it is kind of weird seeing her interact with your sister."
        $ kaya.event_triggers_dict["incest_warnings"] = 1
    else:   #You've started down the incest path with Lily
        "As you watch the two girls interact, you can't help but start to get turned on."
        "Two hot college coeds. One sleeps in your house and has already started opening up to you sexually, the other is right on the brink."
        "You can't help but imagine the two girls making out... getting on their knees in front of you, one of them taking the tip of your cock in her mouth while the other licks the shaft..."
        $ mc.change_locked_clarity(20)
        $ kaya.event_triggers_dict["incest_warnings"] = 0
    the_person "[the_person.mc_title]?"
    lily "Earth to [mc.name]?"
    mc.name "I'm sorry... I spaced out for a second."
    the_person "Your sister just invited me over to study Tuesday night... it turns out we have the same class, but at different times!"
    the_person "I said I wasn't sure you would feel comfortable with that..."
    mc.name "Oh! That's fine... why would I be uncomfortable with that?"
    lily "I don't know, sometimes you get weird about stuff..."
    mc.name "No, that sounds great! I'll make sure not to bug you gals too much."
    "[the_person.possessive_title] and [lily.title] trade phone numbers. Sounds like you have a study party to crash on Tuesday!"
    $ town_relationships.update_relationship(lily, kaya, "Friend")
    $ mc.business.add_mandatory_crisis(kaya_lily_study_night_intro)
    $ kaya.event_triggers_dict["has_started_internship"] = False
    return

label kaya_meet_erica_at_uni_label(the_person):     #This label is a replacement for kaya and lily event.
    $ scene_manager = Scene()
    "You go for a stroll at the university. With no particular aim, you just walk around, checking out some of the girls, stretching your legs a bit."
    the_person "[the_person.mc_title]? Is that you?"
    $ scene_manager.add_actor(the_person)
    "You turn and see [the_person.possessive_title]. She goes to class here, but it is a big school, so you are surprised to see her."
    mc.name "Ah, hello there [the_person.title]."
    "She gives you a smile and chirps at you."
    if the_person.event_triggers_dict.get("drink_date_count", 0) > 1:
        the_person "We go out for drinks and now you are stalking me at class, mister?"
    else:
        the_person "We go out one night for drinks and you are stalking me at class, mister?"
    "[the_person.title] is very quick-witted. You can tell she is half-joking... but also seriously wanting to know what you are doing here."
    mc.name "Ah, sorry I wasn't looking for you, to be honest... I was... er..."
    "Just then, you are saved by another familiar voice."
    erica "Oh hey, [erica.mc_title]!"
    $ scene_manager.add_actor(erica, display_transform = character_center_flipped)
    "[erica.possessive_title] walks up."
    erica "You didn't tell me you were gonna be here! I'm just headed to the gym, want to go workout?"
    $ scene_manager.update_actor(the_person, emotion = "angry")
    the_person "Ahhh... I see... you aren't here to see me..."
    "[erica.title] suddenly realizes you were talking with [the_person.possessive_title]. The edge of jealously is clear in [the_person.title]'s voice."
    erica "Oh! Sorry, I didn't realize you were talking to her..."
    mc.name "Ah, let me introduce you. [the_person.fname], this is [erica.fname]. She is taking classes here also, and we workout together once in a while."
    $ scene_manager.update_actor(the_person, emotion = "sad")
    "You can tell [the_person.title] is still skeptical."
    the_person "Ah... so you are... workout buddies?"
    mc.name "Yeah, something like that."
    erica "Nice to meet you! You look kind of familiar... have I seen you somewhere before?"
    the_person "Maybe, I work over at the coffee shop..."
    erica "Ah, probably not there, coffee makes me anxious."
    "The girls start to chat, trying to figure out if they know each other from somewhere."
    "Suddenly, they make a breakthrough."
    erica "Ah! Yes I have that class too! It is so hard!"
    the_person "Yeah it is definitely challenging."
    erica "Hey... do you want to get together to study sometime? They have study rooms here at the university."
    the_person "That would be really helpful."
    "As you watch the two girls interact, you can't help but start to get turned on."
    "Two hot college coeds. You've already started messing around with [erica.possessive_title], the other is right on the brink."
    "You can't help but imagine the two girls making out... getting on their knees in front of you, one of them taking the tip of your cock in her mouth while the other licks the shaft..."
    $ mc.change_locked_clarity(20)
    the_person "[the_person.mc_title]?"
    erica "Earth to [mc.name]?"
    mc.name "I'm sorry... I spaced out for a second."
    the_person "[erica.fname] just asked if you ever took molecular biology when you were here..."
    mc.name "Oh! Yes, actually that is one of my specialties. I use it every day at my pharmaceutical company."
    erica "Ah! You should join us sometime. I bet you could help us out if we get stuck."
    the_person "If it isn't too much of a bother."
    mc.name "No, I'll try to swing by sometime.."
    "[the_person.possessive_title] and [erica.title] trade phone numbers. Sounds like you have a study party to crash on Tuesday!"
    $ town_relationships.update_relationship(erica, kaya, "Friend")
    $ kaya.add_unique_on_room_enter_event(kaya_erica_teamup_action)
    $ kaya.event_triggers_dict["has_started_internship"] = False
    $ kaya.set_override_schedule(university, the_days = [1], the_times = [4])
    $ erica.set_override_schedule(university, the_days = [1], the_times = [4])
    return

label kaya_lily_study_night_intro_label():
    #This should no longer trigger
    $ the_person = kaya
    $ scene_manager = Scene()
    "As you are getting ready for bed, the sound of girls chattering and giggling can be heard from down the hall."
    "You remember that [the_person.possessive_title] was supposed to come over tonight to study with [lily.title]."
    "You decide to go say hi."
    $ mc.change_location(lily_bedroom)
    $ scene_manager.add_actor(lily)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_center_flipped)
    "You knock on the door and a second later [lily.possessive_title] swings the door open. [the_person.title] is sitting on her bed."
    lily "Oh hey, I didn't realize you were home."
    the_person "Hey [the_person.mc_title]!"
    mc.name "Hey, I thought I heard you two in here, so I decided to come say hello."
    lily "Yeah we've been studying pretty hard for the last hour, we were just about to take a break."
    mc.name "Sounds good. Can I get you anything? A soda or a glass of water maybe?"
    lily "Oh! I bought a bottle of white zinfandel and it's in the fridge. Can you get it open for me? I hate opening wine bottles."
    the_person "Wine? Now your sister is trying to get me drunk too?"
    lily "If you get drunk off of... wait what do you mean too?"
    "[lily.possessive_title] looks at you when she realizes what she means."
    lily "Damn, I didn't realize you were putting the moves on her!"
    mc.name "Don't worry, I'll go get it open."
    $ scene_manager.clear_scene()
    "You quickly bail out of that conversation and head for the kitchen."
    $ mc.change_location(kitchen)
    "Once in the kitchen you find the bottle of wine in the fridge and quickly get it open."
    "You grab two wine glasses and pour one. Hmm... maybe you could slip a serum into the girls drink really quick..."
    call give_serum(mom, add_to_log = False) from _call_give_kaya_serum_home_study_01
    if _return:
        "You have JUST finished mixing a serum into one glass and are getting ready to pour another when a voice from behind startles you."
    else:
        "You decide not to try and mix a serum in. Just as you are about to pour a second glass of wine, a voice from behind startles you."
    mom "Oh! A glass of wine! That looks perfect."
    $ scene_manager.add_actor(mom)
    "[mom.possessive_title] grabs the glass from you before you can react and starts to sip on it."
    mom "Thank you honey, you are so thoughtful."
    $ mom.change_stats(happiness = 5, love = 2)
    mc.name "Err, right."
    "You look at the second glass for a moment. This could get awkward when the other two get here."
    $ scene_manager.add_actor(lily, display_transform = character_center)
    $ scene_manager.add_actor(the_person, display_transform = character_left_flipped)
    "[the_person.title] and [lily.possessive_title] enter the kitchen right on queue."
    lily "Oh hey mom."
    mom "Hi dear. Who is your friend?"
    lily "Oh! You mean [mc.name]'s friend!"
    "[lily.possessive_title] winks at you in a painfully obvious way."
    the_person "Hi, I'm [the_person.fname]. I'm studying with [lily.fname]. We have the same class at the university..."
    "You get another wine glass out, and quickly pour two for the girls."
    mom "I see... [mc.name] do you know each other too?"
    "Before you can say anything, your annoyingly wonderful little sister speaks up."
    lily "Oh yeah, they've already been on one date. She just told me she thinks his butt is cute!"
    the_person "{=kaya_lang}Aue kahore{/=kaya_lang}..."
    "You aren't sure if your sister is actively cock blocking you or if she is just ineptly trying to help set you up, but the awkwardness in the room is hard to bear."
    mom "I see."
    "You hand the girls their glasses, [lily.title] goes over to the fridge to look for a snack."
    $ scene_manager.update_actor(lily, position = "walking_away")
    mom "Nice to meet you [the_person.fname]. You... look awfully familiar... what was your last name?"
    the_person "[the_person.last_name], ma'am."
    mom "I see..."
    lily "Hey, what do you think about having some of this?"
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(xoffset = -.1), position = "walking_away")
    $ scene_manager.update_actor(mom, emotion = "sad")
    "When [the_person.title] turns to the fridge, you notice [mom.possessive_title] struggle for a moment to keep her emotions in check."
    "She looks at you with clear sadness in her eyes. Realization dawns on her though that you notice, and she quickly puts on happy face..."
    $ scene_manager.update_actor(mom, emotion = "happy")
    the_person "That looks good, but what about this..."
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(xoffset = -.1), position = "standing_doggy")
    "[the_person.possessive_title] bends over to look at something on the bottom shelf of the fridge. You eyes immediately get drawn to her ass..."
    "God you hope you get a chance to play with her tight little booty soon..."
    $ mc.change_locked_clarity(20)
    "[mom.possessive_title] clears her throat."
    $ scene_manager.update_actor(mom, emotion = "angry")
    "When you look over, you realize she watched you checking out [the_person.title]. God, this whole evening has gotten so awkward!"
    $ scene_manager.update_actor(the_person, display_transform = character_center_flipped(xoffset = -.1), position = the_person.idle_pose)
    $ scene_manager.update_actor(lily, display_transform = character_center, position = the_person.idle_pose)
    "The two girls suddenly stand up and turn around. They've got a snack and their wine."
    lily "Alright, let's get back to studying. See ya!"
    $ scene_manager.remove_actor(lily)
    "[lily.possessive_title] walks out of the kitchen. As [the_person.title] walks by also, she gives you a big smile."
    the_person "Talk to you later, [the_person.mc_title]..."
    $ scene_manager.remove_actor(the_person)
    "The girls leave you alone with [mom.possessive_title] in the kitchen. This is sure to be a painful conversation. You brace yourself."
    "She takes a long drink of her glass of wine, then looks at you."
    if mom.has_taboo(["vaginal_sex", "sucking_cock", "anal_sex"]):  #You have not started incest content with her yet.
        mom "I don't expect you to understand this... but I want you to stay away from that girl."
        "Her strong stance startles you. She's never really meddled in your love life before... why now?"
        mc.name "What? Why?"
        mom "I... [mom.mc_title]... I can't explain it, okay? Sometimes you just need to trust your mother."
        $ scene_manager.update_actor(mom, emotion = "sad")
        mom "That girl is nothing but trouble. So stay away from her okay?"
        "She finishes the last of her drink, then leaves you in the kitchen, alone."
        $ kaya.event_triggers_dict["incest_warnings"] += 1
        $ mom.change_happiness(-5)
    else:
        mom "I know that you are going to date a lot of different girls... I shouldn't be surprised..."
        mc.name "Surprised by what?"
        $ scene_manager.update_actor(mom, emotion = "sad")
        mom "... just don't forget how much I love you, okay?"
        mc.name "Of course not, I love you too mom."
        $ mom.change_love(2)
        "She finishes the last of her drink, then leaves you in the kitchen, alone and confused."
        $ mom.change_happiness(-5)
    $ scene_manager.clear_scene()
    "Alone in the kitchen, you are left with more questions than answers. As you walk down the hall back to your bedroom, you hear the girls in [lily.title]'s room, but decide to leave them alone."
    $ the_person.set_override_schedule(lily_bedroom, the_days = [1], the_times = [4])
    $ lily.set_override_schedule(lily_bedroom, the_days = [1], the_times = [4])  #This should already be set, but just in case, make sure she is there.
    $ kaya.add_unique_on_room_enter_event(kaya_erica_teamup_action)
    $ kaya.add_unique_on_talk_event(kaya_uni_scholarship_intro)
    $ kaya.event_triggers_dict["studies_with_lily"] = True
    return

label kaya_lily_study_night_apology_label(the_person):
    #This should also no longer trigger
    "After the disaster that was Tuesday night, you decide you should probably talk to [the_person.possessive_title] and apologize about it."
    "Stepping up to the counter, [the_person.title] realizes it is you and smiles."
    $ the_person.draw_person(emotion = "happy")
    the_person "Ah, [the_person.mc_title]! I'm glad to see you. Can I get you something? The usual?"
    mc.name "That sounds good..."
    the_person "Okay. I'll make this one on the house, okay?"
    mc.name "Thanks... hey listen... about what happened on Tuesday..."
    the_person "Oh! It was great! Your sister and I had a great time studying and hanging out. She is so funny!"
    mc.name "I just wanted to... wait what?"
    the_person "I know she was trying to embarrass you, and me for that matter, but honestly I had to laugh."
    the_person "[lily.fname] is great. She's like the sister I never had! I hope it's okay, I'm going to come over again on Tuesday night to study again?"
    mc.name "That is fine of course."
    the_person "In fact, we might be making a thing of it. It was really handy being able to study for that class together."
    the_person "Of course... I still want to see you..."
    "Wow, this was easier than you expected."
    mc.name "Good. I honestly came to try and apologize about how awkward the other night was but... sounds like we're good."
    "?????""Ahem... excuse me sir are you almost done ordering?"
    "The guy behind you in line is apparently not amused with you holding up the line."
    "[the_person.possessive_title] gives you a wink, you grab your coffee and step out of line."
    "You sit down at a booth and sip your coffee for a bit. You look over at [the_person.title] and admire her as she works."
    "She glances over at you and notices you watching her and gives you a smile."
    $ jump_game_loop()
    return

label kaya_lily_study_night_recurring_label(the_person):
    #This should no longer trigger
    $ the_person = kaya
    $ scene_manager = Scene()
    "You remember that [the_person.possessive_title] was supposed to come over tonight to study with [lily.title], so you swing by her room."
    $ mc.change_location(lily_bedroom)
    $ scene_manager.add_actor(lily)
    $ scene_manager.add_actor(the_person, position = "sitting", display_transform = character_center_flipped)
    "[lily.possessive_title] opens the door. [the_person.title] is sitting behind her on the bed."
    lily "Oh hey."
    the_person "Hey [the_person.mc_title]!"
    mc.name "Hey, I know you are busy studying, but just wanted to come say hi. Can I get you girls a snack or something?"
    lily "Oh thanks, [lily.mc_title]. Yeah can you get us some pretzels, and I wouldn't mind a glass of soda from the fridge. Do you want anything [the_person.fname]?"
    the_person "Soda would be nice!"
    lily "Yeah two sodas and pretzels!"
    mc.name "Sure."
    $ scene_manager.clear_scene()
    "You head for the kitchen."
    $ mc.change_location(kitchen)
    "You pour a couple glasses of soda and grab some pretzels. You look around to make sure no one is there. Do you want to put some serum in the sodas?"
    menu:
        "Add serum to [lily.title]'s drink":
            call give_serum(lily) from _call_give_serum_lily_study_night_01
            if _return:
                "You mix the serum into [lily.possessive_title]'s soda."
            else:
                "You decide not to give her any for now."
        "Leave her drink alone":
            "You decide not to give her any for now."
    menu:
        "Add serum to [the_person.title]'s drink":
            call give_serum(the_person) from _call_give_serum_kaya_study_night_02
            if _return:
                "You mix the serum into [the_person.possessive_title]'s soda."
            else:
                "You decide not to give her any for now."
        "Leave her drink alone":
            "You decide not to give her any for now."
    "You bring the snacks and drink to the girls. They are busy studying, so you decide to leave them alone for tonight."
    $ kaya.event_triggers_dict["last_lily_study_night"] = day
    $ kaya.add_unique_on_room_enter_event(kaya_lily_study_night_recurring)
    return

label kaya_uni_scholarship_intro_label(the_person):
    "You go for a walk, eventually coming to the university grounds. You decide to walk about for a bit, admiring the architecture and the people."
    "After the four years you spent going here, you feel a connection to this place and to the students. It feels good to be on the grounds."
    "As you walk around, you spot [the_person.possessive_title]. She is stepping out of a building, and seems down."
    $ the_person.draw_person(emotion = "sad")
    mc.name "Hey [the_person.title]. Doing okay?"
    the_person "Wha? Oh hey [the_person.mc_title], I'm doing fine..."
    "She doesn't seem fine..."
    mc.name "Are you sure?"
    the_person "I... just got done withdrawing from my courses for next semester."
    mc.name "You did what? Isn't next semester your final one before graduating?"
    the_person "I had to drop out. I can't afford the tuition anymore."
    mc.name "[the_person.title]... I'm sorry... are you sure there isn't some other way? Where is the money from the coffee shop going?"
    the_person "Its my mom... the doctor is trying her on this new medication, but insurance won't cover it because it's experimental. They are giving her a good deal, but it is still really expensive."
    the_person "My paycheck can just barely cover it. Mom has been almost completely absent from her business lately, so she has been needing some help with bills too..."
    mc.name "[the_person.title], I didn't know you were so hard up... but your education is important! Isn't there some way of getting a student loan or?"
    the_person "They only look at last year's family income, and mom was making decent money then."
    mc.name "Well... what if I gave you the money? I run a business, I could manage."
    $ the_person.draw_person(emotion = "angry")
    the_person "What!?! I'm not asking for handouts!"
    mc.name "I didn't mean it like that! Everyone goes through hard times once in a while."
    $ the_person.draw_person(emotion = "sad")
    the_person "I... I know. I'm sorry, I didn't mean to blow up like that..."
    the_person "You're a sweet guy, but I don't think I could accept money like that from you as a gift."
    the_person "I'm sorry, I have to get going... take care!"
    mc.name "Goodbye."
    $ the_person.draw_person(position = "walking_away")
    "Your brain is working overtime as [the_person.possessive_title] walks away. There has to be some way that you can convince her to keep going to class?"
    "When things with her mother... resolve... sure she could go back then... but will she?"
    "Dropping out now, you get the sinking feeling she will probably never finish her degree."
    "Surely there is something you could do?"
    "You decide to talk to someone about it. Someone who knows a bit more about the University and its inner workings, financially and otherwise."
    "Someone who once helped you financially get through your time in university."
    "You walk to [nora.possessive_title]'s lab and knock on the door."
    $ nora.draw_person()
    nora "Ah, hello [nora.mc_title]."
    mc.name "Hello [nora.title]."
    nora "Is there something I can do for you?"
    mc.name "Advice, maybe."
    $ nora.draw_person(position = "sitting")
    nora "Sure, just give me a minute."
    "She steps back inside but returns a moment later."
    "[nora.title] invites you into her office and you sit down with her. You give her a brief history of what is going on with [the_person.title]."
    if kaya_mc_knows_relation():
        "Leaving out a few key details about her actual relationship with you."
    else:
        "Leaving out a few details about your interest in her."
    mc.name "So... is there anything I can do?"
    nora "Well, you could start a scholarship foundation. If you were to start one with the university, it would be up to you to determine who the recipients are."
    mc.name "Oh... a scholarship?"
    nora "Yes. However, it sounds like this student isn't interested in free money... maybe you could make some kind of scholarship - internship program?"
    mc.name "Ahh, internship?"
    nora "You are still running that research company right? Many degrees here have electives that involve an internship, especially STEM degrees."
    nora "You run an internship program where the students come help in your research facility and you pay their schooling costs for a semester."
    nora "The university would count it as credit accumulated to their degree."
    nora "Generally though, they want students to focus on their studies, so usually they ask that the hours be kept low, 10 hours a week or less."
    mc.name "Hmm, how much would it cost to set up something like that?"
    nora "Last time I checked, other similar programs paid about $15000 per intern. That covers the student's entire tuition, meal plan, and books for a semester."
    nora "The time for the interns to work is up to you, but most programs I've seen are set up for weekends. Either one full day, or two half-days."
    mc.name "I see... so this is something that I could start with just [the_person.title], but could bring on more people as things go along?"
    nora "Yes, if you want to I could work with you on identifying potential candidates. However, there are a few people who would be ineligible."
    nora "While not illegal, the university takes a strong stance against nepotism, so your family members would not be eligible."
    if kaya_mc_knows_relation():
        mc.name "I... ha, I would never... of course..."
    else:
        mc.name "Family?"
    nora "So [lily.fname], your sister, would not be eligible."
    mc.name "[lily.fname], right."
    mc.name "Are there any other limits to who I can hire? As interns?"
    nora "Not really, but you should be careful not to discriminate against protected classes with your awards."
    mc.name "What if I wanted to support a protected class?"
    nora "Such as?"
    mc.name "What if I made it... a STEM internship program for girls only?"
    nora "Oh! [nora.mc_title], that would be a great idea. No such program currently exists that I'm aware of. I think the university would jump at the chance to offer a STEM internship for women."
    nora "If you want to start this, I want to be your partner for it. To get some of these girls out into the world of research and getting some job experience before they graduate would be invaluable."
    nora "I'll talk to the university CFO right away if you want to get it set up. I'm sure I can convince him to approve it."
    if nora.sluttiness > 40:
        nora "I can be VERY persuasive."
    "You think about it for a moment. This seems like a great opportunity to get impressionable young co-eds in your business..."
    "However, you should probably run the details by your HR director before you go full steam ahead. For now, maybe you could just hire [the_person.possessive_title] until you talk to her."
    mc.name "Tell you what, let's start with the student that we've already been discussing. I'll talk to my HR supervisor and iron out the details, and then get this program going."
    nora "Excellent. What programs are you looking to intern from?"
    mc.name "Well, for a STEM program... we currently do medical research and pharmaceutical manufacturing, so I suppose Chemistry and Biology?"
    nora "I'll go corner the CFO right away. Can I give him your financial details? We could have this girl you are talking about official by this weekend."
    mc.name "Do it. I have the funds to start this ASAP."
    $ nora.change_stats(happiness = 10, love = 3, obedience = 5)
    nora "It's decided then. I'll go find him right now. You're doing a wonderful thing, supporting students, [nora.mc_title]."
    $ clear_scene()
    "You leave [nora.possessive_title]'s lab. You text [the_person.possessive_title]."
    $ mc.start_text_convo(the_person)
    mc.name "Hey, are you still at the university?"
    the_person "Yeah, I have an hour until my next class starts."
    mc.name "Meet me at the quad."
    the_person "Okay."
    $ mc.end_text_convo()
    "You walk quickly over to a courtyard between four of the main university buildings."
    $ the_person.draw_person(emotion = "sad")
    the_person "Hey [the_person.mc_title]..."
    mc.name "Hey. I want you to sign back up for your classes."
    the_person "I'm not taking your money."
    mc.name "I'm not giving you money, but I just got done talking to one of the professors here, and you've been offered an internship."
    the_person "A... what?"
    mc.name "The [mc.last_name] STEM Internship for Women program."
    the_person "I've never heard of such a program... or applied for it?"
    mc.name "That's because it just got created today. I really think you should accept it."
    the_person "I don't know..."
    mc.name "It is just for a few hours on the weekends. Half-days on Saturdays and Sundays. It will give you some good job experience."
    mc.name "And if you are ever just too tired from family stuff... just text me and stay home."
    $ the_person.draw_person(emotion = "happy")
    the_person "I... I don't know what to say."
    mc.name "Just say that you'll be there on Saturday. I'm still getting the details worked out."
    the_person "Okay. I'll do it! I'll see you Saturday... boss?"
    mc.name "See you then."
    $ clear_scene()
    $ mc.business.change_funds(-15000)
    "You have taken the first step toward beginning an internship program. You should talk with your HR supervisor as soon as possible to establish the details!"
    $ mc.business.add_mandatory_crisis(kaya_HR_start_internship_program)
    return

label kaya_HR_start_internship_program_label():
    $ the_person = mc.business.hr_director
    "You page your HR director to have her meet you in your office. You need to talk to her about starting up the internship program."
    $ mc.change_location(ceo_office)
    $ the_person.draw_person()
    the_person "You wanted to see me?"
    mc.name "I do. Have a seat."
    $ the_person.draw_person(position = "sitting")
    mc.name "I've partnered up with the local university. I'm starting a STEM internship program for women to help get them work experience and a scholarship toward their studies."
    the_person "That's... wow! Okay. How can I help?"
    mc.name "I've partnered with a former professor at the university who will help me decide who to award the internships to. The plan is to have them work here half-days on Saturday and Sunday."
    the_person "Okay..."
    mc.name "For now, I'm only hiring for Production and Research, since it is a STEM focused scholarship."
    the_person "So... you know I don't work on weekends, right?"
    mc.name "I wouldn't expect that of you..."
    the_person "So... the interns will be here unattended?"
    mc.name "I'll be here some of the time, I'm sure..."
    if the_person.sluttiness > 40:
        the_person "And you'll be able to keep it in your pants for the weekend, until I get here on Monday, right?"
    else:
        the_person "So you'll be here alone, as the only male, with a bunch of college age girls?"
    mc.name "Well..."
    "[the_person.possessive_title] sighs."
    the_person "They are also not technically employees, so employee policies and contracts won't technically apply to them."
    mc.name "Meaning?"
    the_person "Things like serum testing requirements, office duties, etc. None of those will apply to them."
    the_person "Although they need to comply with the company dress code, since this might include protective gear."
    mc.name "That's fine."
    the_person "They also generally won't quit, but their productivity will probably hinge on how much they enjoy working here."
    the_person "In addition, if things go badly, or if you can't behave yourself, I'm sure they'll make my life hell with HR paperwork and complaints..."
    mc.name "I'll be on my best behavior."
    the_person "Okay... can we start small at least?"
    mc.name "Well, for now I only have one person. How small do you think?"
    the_person "Let's keep it to three people per department. If things go good, we can expand it more."
    mc.name "That's a good idea."
    the_person "And [the_person.mc_title]... please don't let me come back to work on Mondays to a mountain of HR paperwork."
    mc.name "Yes ma'am."
    the_person "Alright. I'll make up a basic intern onboarding paperwork packet that you can give them."
    the_person "I hope I don't regret this..."
    $ the_person.draw_person(position = "walking_away")
    "[the_person.possessive_title] gets up and says goodbye, leaving your office."
    $ clear_scene()
    "You can now hire college interns! Talk to [nora.title] at the university to hire more. They cost $15000 and will work on weekends for their final semester."
    "If the intern is happy working here, they can be hired on full time after graduation."
    "Unhappy interns will hurt company efficiency while working. They will also refuse an employment offer after graduating."
    "Your first intern is [kaya.title]. For now you are limited to three interns per department. More interns per department, and more available departments may become available in the future."
    $ mc.business.add_mandatory_crisis(kaya_first_day_of_internship)
    return

label kaya_first_day_of_internship_label():
    $ the_person = kaya
    $ the_person.apply_university_outfit()
    if kaya_can_get_barista_quickie() and the_person.outfit.get_panties():
        $ the_person.outfit.remove_clothing(the_person.outfit.get_panties())
    call unlock_college_interns() from _unlock_intern_with_nora_and_business_01
    $ mc.business.hire_college_intern(the_person, "Research", add_to_location = False)
    "Today is the first day of your internship program. You make sure to head to work early to meet your first intern, [the_person.title]."
    $ mc.change_location(ceo_office)
    "You go to your office and make sure you are ready to start the day. On your desk is the paperwork packet your HR director made up."
    "The packet looks great, with very detailed instructions and guidelines. You should consider giving her a bonus..."
    "KNOCK KNOCK"
    $ the_person.draw_person()
    the_person "Hello?"
    mc.name "Ah! You found your way in. Welcome!"
    the_person "Thanks. I'm here! I still can't believe it... I enrolled in my classes again, and my university account shows zero balance!"
    the_person "So I'm ready to work. I'm not sure how much I'll be able to help, but I promise I'll try my best."
    mc.name "That is great to hear!"
    mc.name "You know you don't need to wear your school uniform for this right?"
    the_person "Oh, yeah. I just couldn't decide what to wear and this was an easy way to look professional."
    mc.name "I'm not complaining, just feel free to wear whatever you want."
    the_person "Ok, thanks!"
    $ mc.change_location(mc.business.p_div)
    "You give her a tour of the facility, showing her all the different departments."
    $ mc.change_location(mc.business.r_div)
    "Finally, you get to the research department."
    mc.name "And, this is where I'll have you working most of the time."
    the_person "Wow! A real lab. This is amazing!"
    "You show her around, how to use the computer systems, how to look at research progress, how to figure out what needs to be done, etc."
    the_person "Wow. This is great. I promise I'll work hard while I'm here. Is it just going to be me?"
    mc.name "For today, yes, but I'm going to look into providing scholarships to more students soon, so it won't always be that way."
    if kaya_can_get_barista_quickie():
        $ kaya.event_triggers_dict["can_get_work_quickie"] = True
        the_person "Oh, well that is too bad. I was hoping since we had some scheduled together time on the weekends you might be able to come visit me for a break."
        menu:
            "You promised to be good":
                mc.name "That is tempting, but I already made a promise to my HR director that I would behave."
                the_person "She's not here is she? I promise not to tell."
                mc.name "It's your first day, I should try and be a responsible adult."
                the_person "Where's the fun in that."
                the_person "Besides, I forgot to tell you, I forgot one of the parts of my uniform."
                $ the_person.strip_to_vagina(prefer_half_off = True)
                "As she finishes talking she hikes up her skirt showing you her pussy, is it already wet?"
                menu:
                    "Be good":
                        mc.name "Oh god, I must be crazy."
                        mc.name "I'm sorry, I want your first day to be at least somewhat like a normal job."
                        the_person "Alright, I'll be here if you change your mind."
                        return
                    "Give in":
                        pass
            "Since she's asking for it":
                mc.name "That sounds like an excellent idea."
                the_person "Great! I knew it was a good idea to leave my panties at home."
                $ the_person.strip_to_vagina(prefer_half_off = True)
                "As she finishes talking she hikes up her skirt showing you her pussy, is it already wet?"
                menu:
                    "Why wait":
                        pass
                    "Come back":
                        mc.name "Brilliant ideas like that will make you a fine addition to the team."
                        mc.name "Although it might impact my ability to focus knowing you are here waiting for me."
                        return
        mc.name "It seems like I am going to really enjoy having you work here, although I do wonder how much work we'll be getting done."
        call kaya_work_fuck_label(the_person) from _call_kaya_work_fuck_label
    return

label kaya_work_fuck_label(the_person):
    $ kaya.event_triggers_dict["can_get_work_quickie"] = True
    $ kaya.event_triggers_dict["work_fuck_last_day"] = day
    "You step closer to [the_person.title] and rub your hand on her ass."
    mc.name "The day is about half over, do you want to take a break?"
    if the_person.location.person_count > 1:
        mc.name "We can go somewhere private."
    "Alone with [the_person.title] you waste no time in bending her over a table."
    $ the_person.draw_person(position = bent_over_breeding.position_tag)
    $ the_person.strip_to_vagina(position = bent_over_breeding.position_tag, prefer_half_off = True)
    "You step to the side and get into position behind [the_person.title]. You run your cock up and down her slit a couple times, getting the tip nice and wet."
    "You slowly push into her. She reaches back and grabs your leg, urging you forward as her cunt stretches to receive you."
    "She keeps her voice hushed, as she urges you in between moans."
    the_person "That's it, now don't stop until you fill me up...!"
    call fuck_person(the_person, start_position = bent_over_breeding, start_object = make_table(), skip_intro = True, skip_condom = True, private = True) from _call_fuck_person_kaya_work
    $ report_log = _return
    $ the_person.draw_person(position = "standing_doggy")
    if report_log.get("creampies", 0) > 0 and report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
        "Your cum is dripping down the inside of her legs."
    elif report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
    else:
        "When you step back, [the_person.possessive_title] sighs happily."
    return

label kaya_moving_in_with_mother_intro_label(the_person): #This label is called if you ask her to get drinks with you after a few different points in the story. Req 40+ sluttiness
    $ the_person.draw_person()
    "You step into the coffee shop. [the_person.possessive_title] is looking as sexy as ever. You've GOT to get in her pants soon!"
    "You step up to the counter, she smiles when she sees you."
    mc.name "Hey, do you want to go out for a couple drinks tonight?"
    $ the_person.draw_person(emotion = "sad")
    the_person "I can't. My mother's health has been going downhill really fast the last couple of weeks."
    the_person "It seems that she probably will not survive much longer, so I need to spend as much time with her as I can."
    mc.name "I am so sorry. If there is anything I can do for you, please let me know."
    the_person "Thank you. It means a lot to hear that from you."
    the_person "If you want to swing by, I still make time to study with [erica.fname] on Tuesdays, but my schedule is pretty much maxed out now..."
    $ the_person.change_love(5)
    "Unfortunately, it seems that [the_person.possessive_title] may not be able to spend much time with you going forward."
    $ mc.business.add_mandatory_crisis(kaya_asks_for_help_moving)
    $ kaya.event_triggers_dict["move_help_day"] = day + 7
    $ kaya.event_triggers_dict["can_get_drinks"] = False
    #$ kaya.event_triggers_dict["studies_with_lily"] = False
    return

label kaya_asks_for_help_moving_label():    #Timed event after the drink refusal. Something like a week later? Maybe less?
    $ the_person = kaya
    $ mc.start_text_convo(the_person)
    the_person "Hey, sorry to bug you. Are you busy?"
    mc.name "Not particularly. Whatsup?"
    the_person "Just wondering if you could swing by the coffee shop."
    mc.name "Sure thing. I'll be right there."
    $ mc.end_text_convo()
    "You make your way over to the coffee shop. When you get there the door is locked, since it is closed for the night, but after knocking [the_person.possessive_title] quickly lets you in."
    $ mc.change_location(coffee_shop)
    $ the_person.draw_person()
    the_person "Hey! Thanks for coming... can I get you any coffee? It's on the house..."
    mc.name "No thanks. It's pretty late for that."
    the_person "Right..."
    "You walk with her over to a booth and you have a seat with her."
    $ the_person.draw_person(position = "sitting")
    the_person "So, I've been really busy here at the shop and school and with my mom... I haven't had the chance to make many friends. Especially guy friends."
    the_person "My mom has been having some trouble taking care of herself, so I was wondering if you would be able to do me a favor."
    mc.name "Probably. What is it?"
    the_person "I'm going to move back in with my mom tomorrow. I was wondering if you could help me move."
    mc.name "Ah, you need someone to help move boxes."
    the_person "Yeah, I suppose. I'm already pretty much packed up, but {=kaya_lang}makutu {/=kaya_lang}, it is such a big job."
    mc.name "I'm sorry... mak what?"
    the_person "Ah, sorry... that is like, a curse word in my native language."
    mc.name "Ah! Makutu. It was destiny that the first word I would learn from your native tongue is a curse!"
    $ the_person.change_happiness(3)
    the_person "Ha! I suppose it is."
    "She smiles as she looks down."
    the_person "So... tonight is the last night I get in my own place for a while. I was just thinking... you never even got to see it!"
    the_person "Do you want to come over and see it? It might be nice to not have to spend the night alone..."
    "There is some clear innuendo in her offer."
    mc.name "I'd love to come see it."
    $ the_person.change_happiness(2)
    the_person "{=kaya_lang}āue!{/=kaya_lang} I've got this place closed down already. Let's go!"
    $ the_person.draw_person()
    "You step out of the coffee shop into the night with [the_person.possessive_title]. You soon find yourself walking into her apartment."
    $ mc.change_location(the_person.home)
    "There are a few basic things still out, but most of her belongings have been put into boxes."
    $ the_person.add_situational_slut("Lonely", 20, "I don't want to spend the night alone!")
    "[the_person.possessive_title] turns to you."
    the_person "Well, this is it! Or at least it was. I liked having my own place... I'm sure I'll have my own place again soon..."
    $ the_person.draw_person(emotion = "sad")
    "Seeing that she is clearly distraught, you step forward and put your arms around [the_person.title]."
    "She pushes her face into your chest for a minute. She doesn't cry, but you can feel the emotions stirring inside her."
    the_person "I have a lot to be afraid of right now... but that doesn't mean I can't take time to do things that make me happy sometimes too."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "[the_person.possessive_title] looks up at you. She brings her arms around your neck and you lean in and begin to kiss."
    "It starts docile, but quickly heats up. Her tongue is hungry for yours and soon you are making out earnestly."
    $ the_person.change_arousal(10)
    $ mc.change_locked_clarity(20)
    "Your hands reach down and grope [the_person.possessive_title]'s ass. You've been waiting a while to get a piece of this!"
    "But still, something feels off. She seems desperate, and you wonder if her emotional state is okay."
    $ the_person.draw_person(position = "kissing")
    "You break off the kiss for a moment and look at her."
    mc.name "Are you sure you are okay with this? You've been through a lot lately, I feel like I'm kind of taking advantage of you."
    the_person "God... you are just perfect, aren't you?"
    the_person "It's okay. I know my mom is sick... but it's been this way for a while."
    the_person "I knew this day would come eventually. Besides, I'm a big girl. I can decide what I want for myself!"
    "She runs her hand down your chest and start to stroke you through your pants..."
    $ mc.change_locked_clarity(40)
    the_person "And right now, I want you!"
    menu:
        "Fuck Her (Keep going)":
            "You can't say no to her. You grab her and start to make out again. Tongues meet and the urgency returns immediately."
        "Call it a night":
            mc.name "I believe you, but my gut just keeps telling me this isn't the right time... let's put this on pause, okay?"
            mc.name "I'll come back in the morning, I'll still help you move. I don't want to stop seeing you, but I don't think I'm quite ready for this."
            the_person "Okay... I understand..."
            $ the_person.change_stats(happiness = -5, obedience = 3)
            $ mc.business.add_mandatory_crisis(kaya_moving_day)
            the_person "Tomorrow then?"
            mc.name "I'll be here."
            "You leave [the_person.possessive_title]'s place. It hurts to leave her like that, but something about it still just feels off."
            return
    "Primitive urges are overtaking you both. It isn't long until clothes start to come off."
    $ the_person.strip_to_tits(prefer_half_off = True, position = "kissing")
    "With her perky tits out, you quickly kiss down the side of her neck and to her chest. You lick and suckle on one nipple while you grope her other tit with your hands."
    the_person "{=kaya_lang}He pai te ahua{/=kaya_lang}"
    $ the_person.change_arousal(20)
    $ mc.change_locked_clarity(40)
    "You can't tell what she is saying, but you can tell from her moans she is enjoying your attention."
    "While you lick at her nipple, you use your hands to remove what is left of her clothing, with her help."
    $ the_person.strip_outfit(exclude_feet = False, position = "kissing")
    if persistent.pregnancy_pref != 0:
        $ the_person.on_birth_control = False
        "As you undress, you start to pull a condom out of your wallet."
        the_person "Oh my god... wait... we need to talk..."
        $ the_person.draw_person(position = the_person.idle_pose)
        "Fuck. She is so hot! You just want to pound her! Not talk!"
        the_person "I just... I'm sorry I meant to have this conversation before this happened but... you're just so fucking hot and I was scared how this might go."
        the_person "In my culture... we... well... we don't believe in using birth control."
        mc.name "Like... the pill?"
        the_person "Like... anything. Babies are sacred almost, no pills, no condoms..."
        mc.name "So... what... but..."
        the_person "I know that I sprung this on you at like, the worst possible time. If you still want to put on a condom this time, I totally understand."
        the_person "It's okay too, if you want to just pull out. In my culture, if a man has a will strong enough to pull out, he is allowed to..."
        mc.name "... ... ... You know that makes no sense whatsoever."
        the_person "I know! I'm so sorry, I know this is totally a mood killer but... if you don't want to... I would really prefer you didn't wear one..."
        the_person "But this one time it's okay if you decide to anyway."
        "You think about it for a moment. [the_person.possessive_title] is down to fuck, and wants it raw!"
        $ mc.change_locked_clarity(40)
        menu:
            "Put on a condom anyway":
                mc.name "I want to think about it more... but not while you are naked in front of me."
                mc.name "For now a condom goes on, and I'll think about it more."
                the_person "I understand. Thank you for not being upset."
                "You unwrap the condom and then roll it onto your erection."
                $ mc.condom = True
            "Keep it natural":
                mc.name "Thank you for telling me. I really appreciate it."
                "You take the condom and put it back in your wallet. You start to move back toward [the_person.possessive_title]."
                the_person "You just... so you..."
        $ mc.change_location(the_person.bedroom)
        "You pick up [the_person.title] move to the bedroom and throw her on the bed."
        the_person "{=kaya_lang}Hika!{/=kaya_lang}"
        $ the_person.draw_person(position = "missionary")
        "You quickly get on top of her. Her legs naturally wrap around your body as she urges you closer."
        the_person "Oh my god, oh fuck! I've been wanting this since the first night you took me out..."
        mc.name "I've been wanting this for a lot longer than that."
        $ the_person.change_stats(happiness = 5, love = 2)
        "When your cock finally hits her slit, she reaches down with her hand and guides it to her soaking wet hole."
        "You slide yourself in easily. [the_person.possessive_title] is wet and ready for you so you start to fuck her immediately."
        $ the_person.break_taboo("vaginal_sex")
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_intro = True, skip_condom = True) from _call_kaya_sex_at_Home_01
        $ report_log = _return
        if report_log.get("creampies", 0) > 0:
            the_person "Oh my god... I never knew how good it could be to get filled like that!"
            $ become_pregnant(the_person, mc_father = True) #For story reasons, knock her up for sure.
            "[the_person.possessive_title] rubs her belly. A bit of your cum is dribbling down her slit, the rest deposited deep inside of her."
            if report_log.get("creampies", 0) > 1:
                "Surely a few creampies can't be TOO risky... can it?"
            else:
                "Surely one creampie can't be TOO risky... can it?"
    else:
        "You pick up [the_person.title] and throw her on the bed."
        the_person "{=kaya_lang}Hika!{/=kaya_lang}"
        $ the_person.draw_person(position = "missionary")
        "You move on top of her on the bed, ready to fuck."
        call fuck_person(the_person, private=True, start_position = missionary, start_object = make_bed(), skip_condom = False) from _call_kaya_sex_at_Home_02
    $ kaya.event_triggers_dict["no_condom_talk"] = True   #We mark this is true here so it doesn't trigger later, since player pregnancy preferences override condom preference anyway
    $ the_person.draw_person(position = "missionary")
    "You lay in bed for a while with [the_person.possessive_title], but it is getting very late."
    mc.name "Hey... I'm sorry, but I didn't bring stuff to stay the night. I need to get going."
    the_person "Ahh. I know you can't stay. But that's okay. We're going to be doing this again... right?"
    mc.name "Yes, I would love to."
    the_person "Good. I have a pretty high sex drive... Are you sure you can keep up?"
    mc.name "No, but I'm willing to try."
    the_person "Ah, you're funny. Okay then. I'll see you tomorrow? You're still going to help me move, right?"
    mc.name "Definitely."
    "You get your clothes back on, and say goodnight to [the_person.title], who is still laying on her bed."
    "You walk home and fall into your bed, exhausted from your long day."
    $ mc.change_location(bedroom)
    $ mc.business.add_mandatory_crisis(kaya_moving_day)
    $ the_person.clear_situational_slut("Lonely")
    return

label kaya_moving_day_label():  #Today we meet Sakari, Kaya's mom, and learn Kaya is a half sister.
    $ the_person = kaya
    $ scene_manager = Scene()
    $ came_inside_kaya = False
    "It is moving day for [the_person.title]."
    if mc.business.is_open_for_business:
        "You make sure to let work know you will be out for the rest of the day."
    $ the_person.change_location(the_person.home)   # make sure she doesn't wear a location based outfit
    $ mc.change_location(the_person.home)
    "You walk over and soon you are knocking on [the_person.possessive_title]'s front door. She swings it open."
    $ scene_manager.add_actor(the_person)
    the_person "Hey! You're here!"
    $ scene_manager.update_actor(the_person, position = "kissing")
    "She pulls you close and gives you a big hug. She is glad to see you!"
    the_person "Thanks for coming. I'm no slouch, but this would take me forever to get done. You have no idea how much it means to me that you came to help..."
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    "[the_person.possessive_title] has rented a truck, you quickly get into the motions of loading up boxes."
    "You flirt with her a bit as you go, but the hard work holds most of your attention as you spend a couple hours moving things into the truck."
    "Soon, the single bedroom apartment is empty. [the_person.possessive_title] has switched from loading to cleanup as you load up the last few boxes."
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    $ the_person.add_situational_slut("Lonely", 20, "Last day at my own apartment")
    "When you come back in after loading the last box, [the_person.title] is wiping down her counter top, her ass swaying back and forth."
    if the_person.is_pregnant:    #We already knocked her up, go right into round 2.
        call kaya_fuck_in_apartment_label(the_person) from _kaya_sex_in_appt_01
        $ came_inside_kaya = _return
    elif kaya_had_condom_talk():
        "You can't help but admire the girls tight little ass as she wipes down her counters."
        "She told you last night she has a high sex drive. You feel like maybe you could put that to the test."
        if kaya_condom_check():
            "Although you know after her talk she isn't going to let you wrap it up first..."
        menu:
            "Fuck her":
                call kaya_fuck_in_apartment_label(the_person) from _kaya_sex_in_appt_02
                $ came_inside_kaya = _return
            "Leave her alone":
                pass
    else:
        mc.name "God you are hot. You know that?"
        $ scene_manager.update_actor(the_person, position = "stand3")
        the_person "You're pretty good looking yourself."
        the_person "You know... my offer from last night... it still stands."
        the_person "This might be the last time I have to myself for a while. It might be nice to finish it with a bang, so to speak."
        "God. You had the willpower to resist her last night because you were worried she wasn't thinking straight, but now it's a new day."
        "Who knows, this might be your last chance for a while too. Maybe you should just go for it?"
        menu:
            "Fuck her":
                "You can't take it anymore. You step forward and grab her by the waist. She immediately grabs on to you."
                "You start making out."
                $ scene_manager.update_actor(the_person, position = "kissing", special_modifier = "kissing")
                "The sexual tension is incredible. Her body responds to every touch and caress as your hands roam all over her."
                "Primitive urges are overtaking you both. It isn't long until clothes start to come off."
                $ scene_manager.update_actor(the_person, special_modifier = None)
                $ scene_manager.strip_to_tits(person = the_person, prefer_half_off = True)
                "With her perky tits out, you quickly kiss down the side of her neck and to her chest. You lick and suckle on one nipple while you grope her other tit with your hands."
                the_person "{=kaya_lang}He pai te ahua{/=kaya_lang}"
                $ the_person.change_arousal(20)
                $ mc.change_locked_clarity(40)
                "You can't tell what she is saying, but you can tell from her moans she is enjoying your attention."
                "While you lick at her nipple, you use your hands to remove what is left of her clothing, with her help."
                if persistent.pregnancy_pref != 0:
                    $ the_person.on_birth_control = False
                    "Suddenly, she starts to break it off."
                    the_person "Oh my god... wait... we need to talk..."
                    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
                    "Fuck. She is so hot! You just want to pound her! Not talk!"
                    the_person "I just... I'm sorry I meant to have this conversation before this happened but... you're just so fucking hot and I was scared how this might go."
                    the_person "In my culture... we... well... we don't believe in using birth control."
                    mc.name "Like... the pill?"
                    the_person "Like... anything. Babies are sacred almost, no pills, no condoms..."
                    mc.name "So... what... but..."
                    the_person "I know that I sprung this on you at like, the worst possible time. If you still want to put on a condom this time, I totally understand."
                    the_person "It's okay too, if you want to just pull out. In my culture, if a man has a will strong enough to pull out, he is allowed to..."
                    mc.name "... ... ... You know that makes no sense whatsoever."
                    the_person "I know! I'm so sorry, I know this is totally a mood killer but... if you don't want to... I would really prefer you didn't wear one..."
                    the_person "But this one time it's okay if you decide to anyway."
                    "You think about it for a moment. [the_person.possessive_title] is down to fuck, and wants it raw!"
                    $ kaya.event_triggers_dict["no_condom_talk"] = True
                    $ mc.change_locked_clarity(40)
                    menu:
                        "Put on a condom anyway":
                            mc.name "I want to think about it more... but not while you are naked in front of me."
                            mc.name "For now a condom goes on, and I'll think about it more."
                            the_person "I understand. Thank you for not being upset."
                            "You unwrap the condom and then roll it onto your erection."
                            $ mc.condom = True
                        "Keep it natural":
                            mc.name "Thank you for telling me. I really appreciate it."
                            the_person "I'm sorry..."
                            mc.name "I'm honored, honestly, that you would be willing to do this with me. It shows how much our relationship has grown so quickly."
                            the_person "That's true... do you mean...?"
                            mc.name "Let's do it."
                the_person "I umm... don't really have any furniture anywhere so we might have to get a bit creative..."
                "You grab her hips and spin her around, bending her over the kitchen counter."
                $ scene_manager.update_actor(the_person, position = "standing_doggy")
                the_person "Oh! Or maybe not. Oh god..."
                call kaya_fuck_in_apartment_label(the_person) from _kaya_sex_in_appt_03
                $ came_inside_kaya = _return
            "Leave her alone":
                pass

    $ the_person.clear_situational_slut("Lonely")
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    the_person "Alright, that should just about do it! Ready to... oh my god."
    mc.name "What?"
    the_person "I umm... just realized."
    the_person "My mom is going to be there when we get there... you're going to meet her today."
    mc.name "Geeze, you had me scared there for a second."
    the_person "I know but I didn't tell you that. Isn't that something girls are supposed to warn you about? Meeting their mother?"
    mc.name "You might be right, but I'll be fine. Besides, I'm just helping you move, right?"
    the_person "Right. But just so you know she's... a little different."
    mc.name "I already know she's sick."
    the_person "Yeah but... she's a native, like me. Sometimes we do things a little differently than you would expect."
    mc.name "I've come to appreciate that. Don't worry, I'll roll with it."
    the_person "Okay. Let's go!"
    $ scene_manager.update_actor(the_person, position = "sitting")
    $ mc.change_location(downtown)
    "[the_person.possessive_title] says goodbye to her apartment. You hop in the truck while she drives."
    "The truck ride is pretty quiet. You wonder what her mother is like. You guess you'll find out soon."
    #TODO have different backgrounds for Kaya and Sakari's homesteads. This will not feel right in the mean time.
    $ mc.change_location(sakari.home)
    $ scene_manager.update_actor(the_person, position = "walking_away")
    "Soon you arrive. [the_person.possessive_title] goes to the front door and lets herself in. You follow closely behind her."
    the_person "{=kaya_lang}Whaea! Kei konei ahau!{/=kaya_lang}(?????)"
    $ scene_manager.update_actor(the_person, position = the_person.idle_pose)
    $ scene_manager.add_actor(sakari, display_transform = character_center_flipped)
    sakari "{=kaya_lang}Tamahine!{/=kaya_lang}"
    "[the_person.title]'s mother steps out from the hallway. She is surprised when she sees you."
    sakari "Ah, [kaya.fname]! You did not tell me you were bringing a man back here the first day!"
    "She speaks in the same accent that [the_person.title] has, but much thicker."
    the_person "Ah, mom! This is [mc.name]. [mc.name], this is my mother, [sakari.fname]."
    mc.name "A pleasure to meet you."
    sakari "Of course dear."
    $ sakari.set_title(sakari.name)
    $ sakari.set_possessive_title(sakari.name)
    $ sakari.set_mc_title(mc.name)
    the_person "Alright. Let's get to work!"
    "You and [the_person.possessive_title] team up and start unloading her stuff."
    "After an hour or so the truck is starting to get pretty empty. [sakari.title] and [the_person.title] help direct you where to take things."
    "You come across a box that is labeled family pictures. When you take it inside, you ask [sakari.title] where to take it."
    sakari "Oh, that can probably just go in my closet for now. My room is the one on the right."
    $ scene_manager.clear_scene()
    $ mc.change_location(the_person.bedroom)
    "You walk into [sakari.possessive_title]'s room and place the box on an empty shelf in her closet. When you finish putting it up, you glance around her room."
    "Suddenly, you see a picture on her wall. It is a picture of a much younger [sakari.title], but she is standing suspiciously close to a man you feel like you almost recognize."
    "The picture of [sakari.possessive_title] and the man make it clear that they are close. He seems so familiar, but you can't quite put your finger on why."
    $ scene_manager.add_actor(sakari)
    sakari "Ah, thank you for all your help, young man."
    "Her eyes follow yours to the picture on the wall."
    mc.name "That's a nice picture. Who is the man?"
    sakari "That would be [the_person.fname]'s father. He and I had, I guess you would call it an office romance."
    sakari "We worked together for a while, but then things got complicated."
    mc.name "I'm sorry to hear that."
    sakari "Yes. He died a while ago, and I miss him. He was a good man."
    "Wow, you feel horrible. [kaya.title] already lost her dad... and now her mom is dying also."
    $ scene_manager.add_actor(the_person, display_transform = character_center_flipped)
    the_person "Hey, everything going okay in here?"
    sakari "Yes, I was just showing [sakari.mc_title] here some old pictures."
    "You look with new eyes at [the_person.possessive_title]."
    if came_inside_kaya:
        "Oh god... your cum is inside her right now!"
        "You wonder if she has any other family around... someone who could support her if she got knocked up?"
    elif the_person.is_pregnant:
        "Oh god... you came inside her last night!"
        "You wonder if she has any other family around... someone who could support her if she got knocked up?"
    the_person "Are you okay [the_person.mc_title]? You look like you've seen a ghost..."
    "You finally snap out of it and regain your composure."
    mc.name "Right. No I'm fine, just thinking about some things."
    the_person "Good! I just got the last of the boxes in. We are done! Now I get to start unpacking."
    mc.name "Ah, I'm glad I could help you [the_person.title]."
    the_person "UGH, but first I need to take the truck back to the rental place. Can I give you a ride home while I'm on my way?"
    mc.name "No, that's okay. I need to swing by work. I have some things I left there I need to take care of anyway."
    the_person "Alright... Mom I'll be back in a little bit, okay?"
    sakari "Okay. You take care too, young man."
    $ clear_scene()
    $ mc.change_location(downtown)
    "You say goodbye and leave. You can hear the moving truck start up as you walk away."
    # set kaya living with her mom
    $ kaya.change_home_location(sakari.home)
    $ sakari.learn_home()
    $ kaya.event_triggers_dict["mc_knows_relation"] = True
    "You leave the apartment and just walk for a while. You have a lot to think about."
    "You feel a tug in your heart. You want to be there for [kaya.possessive_title] over the next few weeks."
    "And her mom, [sakari.title]... you wonder what is going on with her? Poor [kaya.title]."
    "She's funny, great to be around..."
    if kaya_had_condom_talk():
        "And an awesome fuck."
    else:
        "And seems eager to fuck."
    "[the_person.title] is going to need some time to settle in anyway. You decide to give her some time to settle in before you bug her."
    $ mc.business.add_mandatory_crisis(kaya_share_the_news)
    $ kaya.event_triggers_dict["share_news_day"] = day + 7
    $ kaya.event_triggers_dict["has_moved"] = True
    return

label kaya_fuck_in_apartment_label(the_person): #We already have her bent over doggy in scene manager for this.
    $ came_inside_kaya = False  #This could change some dialogue later in the scene.
    "Bent over her counter, [the_person.possessive_title] wiggles her ass at you. You've been wanting to get her in this position for a long time."
    "Your hands go to her hips. Time to get her naked."
    $ the_person.change_arousal(20)
    $ the_person.strip_to_vagina(prefer_half_off = False, position = "standing_doggy")
    mc.name "Holy fuck your ass is amazing..."
    $ mc.change_locked_clarity(50)
    "You run your hands along her soft curves a few times, one time after running your hands down the sides, you bring them back up between her legs. Her cunt is soaked."
    the_person "Ah! You don't have to tease me... just stick it in!"
    call fuck_person(the_person, private=True, start_position = standing_doggy, skip_intro = True, skip_condom = kaya_condom_check()) from _call_kaya_doggy_at_home_04
    $ report_log = _return
    $ scene_manager.update_actor(the_person, position = "standing_doggy")
    if report_log.get("creampies", 0) > 0 and not the_person.is_pregnant and persistent.pregnancy_pref != 0: #Knock her up, first try
        the_person "Oh my god... I never knew how good it could be to get filled like that!"
        $ become_pregnant(the_person, mc_father = True) #For story reasons, knock her up for sure.
        "[the_person.possessive_title]'s legs are shaking. A bit of your cum is dribbling down her slit, the rest deposited deep inside of her."
        "Surely one creampie can't be TOO risky... can it?"
    else:
        the_person "Oh god... of course, I finally find a stud that will fuck me senseless and I move out of my apartment the same day..."
        "[the_person.possessive_title] is panting."
        the_person "Just... give me a second... I'll be good to go."
    if report_log.get("creampies", 0) > 0:
        $ came_inside_kaya = True
    the_person "I'm gonna clean up in the bathroom, give me a minute."
    $ scene_manager.clear_scene()
    "[the_person.possessive_title] disappears for a few minutes, then comes back after cleaning herself up."
    $ the_person.apply_outfit(the_person.planned_outfit)
    return came_inside_kaya

label kaya_share_the_news_label():  # Timed event after helping her move.
    $ the_person = kaya
    $ mc.start_text_convo(the_person)
    the_person "Hey! Sorry I've been really busy this week. Can you swing by the coffee shop? I'm just getting ready to close up!"
    mc.name "I'll be right there. It would be good to have a chat."
    if kaya.is_pregnant:
        the_person "And maybe a couple other things too ;)"
    else:
        the_person "Yeah, I miss you."
    the_person "See you soon!"
    $ mc.end_text_convo()
    $ mc.change_location(coffee_shop)
    "You head to your favorite coffee shop. After a knock on the door, [the_person.possessive_title] swings it open."
    $ the_person.draw_person()
    the_person "Hey! Have a seat, everyone else is gone."
    "You walk over to a booth and sit down. [the_person.title] locks the door and joins you."
    $ the_person.draw_person(position = "sitting")
    the_person "Thanks for coming."
    if kaya.is_pregnant:
        $ kaya.event_triggers_dict["preg_knows"] = True
        $ kaya.remove_on_room_enter_event("Pregnancy Announcement") #Attempt to remove the default pregnancy announcement event
        the_person "I have something I really need to talk to you about..."
        if the_person.love < 60:
            $ the_person.love = 60
        the_person "I think... I've really fallen for you. The other day, at my place... that was so hot!"
        the_person "I'm sorry... I'm really nervous about this!"
        the_person "I had a doctor appointment this morning just to make sure... I'm pregnant!"
        "Oh fuck. You've only been with her a bit... what are the odds?"
        "You get a knot in your stomach. Normally knocking up a hot piece of ass like [the_person.title] would be exciting..."
        "[the_person.possessive_title] is looking at you, nervous. You can tell she is excited, but is scared about how you are going to react."
        mc.name "That's incredible. I can hardly believe it."
        the_person "I know. I'm sorry, I know we haven't known each other very long but... I'm really excited."
    else:
        the_person "I'm sorry I haven't been able to talk with you much the last week. It has been stressful, moving back in with my mom."
        mc.name "I understand. That is a big life change."
        the_person "I just wanted to tell you I really appreciate everything you've done for me. It means more to me than you know."
        if the_person.love < 60:
            $ the_person.love = 60
        the_person "I know we haven't known each other for long but... I'm really falling for you."
        the_person "You don't have to say anything back, and I understand if you need time... but I feel like I need to be honest about my feelings and how I feel about you."
        "You get a knot in your stomach. Normally getting with a hot piece of ass like [the_person.title] would be exciting..."
        "[the_person.possessive_title] is looking at you, nervous. You can tell she is excited, but is scared about how you are going to react."
    mc.name "Yeah, well, there is something I need to talk to you about too."
    mc.name "I'm not sure how to say this, but, I feel like I am taking advantage of you."
    the_person "You think... what?"
    mc.name "Your mom told me about how your dad died... and with your mom sick too, I know you're in a vulnerable state..."
    if the_person.has_taboo("vaginal_sex"):
        mc.name "I shouldn't have pushed so hard... and I'm sorry."
    else:
        mc.name "I should have kept it in my pants... and I'm sorry."
    the_person "That's... I don't understand. Are you saying you don't want to..."
    menu:
        "You want to be with her":
            mc.name "That isn't what I'm saying. [kaya.title], you are funny, and great to be around, and I really want to make this work."
            mc.name "I'm just really feeling guilty about the way things went down."
            if kaya.knows_pregnant:
                mc.name "And now you're pregnant and..."
            the_person "Geeze, you scared me! I thought you were really going to say no!"
            mc.name "I want to make this work. Honestly."
            $ the_person.draw_person(position = "sitting", emotion = "happy")
            $ the_person.change_stats(happiness = 10, love = 5)
            mc.name "We can figure this whole thing out. Together."
            if not the_person.is_girlfriend:
                $ the_person.add_role(girlfriend_role)
                the_person "Does that mean... are we?"
                mc.name "[the_person.fname], will you be my girlfriend?"
                the_person "Oh! Yes of course!"
            else:
                the_person "I'm so glad to hear that you don't want to give up on things between us."
        "You don't feel that way (disabled)":
            pass
    $ the_person.draw_person(position = the_person.idle_pose)
    "[the_person.possessive_title] stands up."
    the_person "Come with me!"
    "You follow her to a backroom, away from the big windows facing the street."
    $ the_person.draw_person(position = "kissing", special_modifier = "kissing")
    "She pulls you close and you start to make out. She moans when your hand grabs her ass."
    $ the_person.change_arousal(15)
    $ mc.change_locked_clarity(30)
    $ the_person.draw_person(position = "kissing")
    the_person "You'd better take me now. I'm not sure how often we will be able to do this, so we'll need to take advantage of every opportunity."
    if kaya_had_condom_talk():#You've probably done this by now. If not, we definitely have the talk now.
        mc.name "You don't have to tell me twice."
        "Your hands are roaming everywhere over [the_person.possessive_title]'s body, and soon her clothes start to come off."
        $ the_person.strip_outfit(exclude_lower = True, position = "kissing")
        "When her tits spring free, you can't help but grope one while you lick and suck on the other."
        $ the_person.change_arousal(15)
        $ mc.change_locked_clarity(50)
        if the_person.is_pregnant:
            the_person "Oh god... is it possible that they are already starting to get more sensitive?"
        "Her moans drive you into a lust fueled frenzy. Soon you are both stepping out of your remaining clothes."
        $ the_person.strip_outfit(exclude_feet = False, position = "kissing")
        $ the_person.draw_person(position = "against_wall")
        "[the_person.possessive_title] lifts her leg up, allowing you easy access. You push her gently against the wall, lift her weight a bit to line yourself up with her cunt."
        "Once lined up, you let her body slide down the wall, her weight impaling her on your cock. You easily slide in to her eager pussy."
        the_person "Oh fuck... you better do this to me often, boyfriend!"
        call fuck_person(the_person, private=True, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = kaya_condom_check()) from _call_kaya_sex_at_shop_07
    else:
        $ kaya.event_triggers_dict["no_condom_talk"] = True
        "Primitive urges are overtaking you both. It isn't long until clothes start to come off."
        $ the_person.strip_to_tits(prefer_half_off = True, position = "kissing")
        "With her perky tits out, you quickly kiss down the side of her neck and to her chest. You lick and suckle on one nipple while you grope her other tit with your hands."
        the_person "{=kaya_lang}He pai te ahua{/=kaya_lang}"
        $ the_person.change_arousal(20)
        $ mc.change_locked_clarity(40)
        "You can't tell what she is saying, but you can tell from her moans she is enjoying your attention."
        "While you lick at her nipple, you use your hands to remove what is left of her clothing, with her help."
        $ the_person.strip_outfit(exclude_feet = False, position = "kissing")
        "You drop your pants and underwear to the floor and step out of them. You reach for her leg to pull up a little so you can get between them."
        if persistent.pregnancy_pref != 0:
            $ the_person.on_birth_control = False
            "Suddenly, she starts to break it off."
            the_person "Oh my god... wait... we need to talk..."
            $ the_person.draw_person(position = the_person.idle_pose)
            "Fuck. She is so hot! You just want to pound her! Not talk!"
            the_person "I just... I'm sorry I meant to have this conversation before this happened but... you're just so fucking hot and I was scared how this might go."
            the_person "In my culture... we... well... we don't believe in using birth control."
            mc.name "Like... the pill?"
            the_person "Like... anything. Babies are sacred almost, no pills, no condoms..."
            mc.name "So... what... but..."
            the_person "I know that I sprung this on you at like, the worst possible time. If you still want to put on a condom this time, I totally understand."
            the_person "It's okay too, if you want to just pull out. In my culture, if a man has a will strong enough to pull out, he is allowed to..."
            mc.name "... ... ... You know that makes no sense whatsoever."
            the_person "I know! I'm so sorry, I know this is totally a mood killer but... if you don't want to... I would really prefer you didn't wear one..."
            the_person "But this one time it's okay if you decide to anyway."
            "You think about it for a moment. [the_person.possessive_title] is down to fuck, and wants it raw!"
            $ kaya.event_triggers_dict["no_condom_talk"] = True
            $ mc.change_locked_clarity(40)
            menu:
                "Put on a condom anyway":
                    mc.name "I want to think about it more... but not while you are naked in front of me."
                    mc.name "For now a condom goes on, and I'll think about it more."
                    the_person "I understand. Thank you for not being upset."
                    "You unwrap the condom and then roll it onto your erection."
                    $ mc.condom = True
                "Keep it natural":
                    mc.name "Thank you for telling me. I really appreciate it."
                    the_person "I'm sorry..."
                    mc.name "I'm honored, honestly, that you would be willing to do this with me. It shows how much our relationship has grown so quickly."
                    the_person "That's true... do you mean...?"
                    mc.name "Let's do it."
        $ the_person.draw_person(position = "against_wall")
        "[the_person.possessive_title] lifts her leg up, allowing you easy access. You push her gently against the wall, lift her weight a bit to line yourself up with her cunt."
        "Once lined up, you let her body slide down the wall, her weight impaling her on your cock. You slide in easily to her eager pussy."
        the_person "Oh fuck... you better do this to me often, boyfriend!"
        call fuck_person(the_person, private=True, start_position = against_wall, start_object = make_wall(), skip_intro = True, skip_condom = True) from _call_kaya_sex_at_shop_08
    $ the_person.draw_person()
    "When you finish, [the_person.possessive_title] looks thoughtful."
    the_person "Living with my mother... we are going to have to get creative so we can get naughty..."
    mc.name "I mean, you are always welcome at my place."
    the_person "Yeah. I'll see if I can come up with something."
    "As you look at her, [the_person.title] looks happy, but tired."
    mc.name "It's been a long day. Can I help you close up?"
    the_person "No, I've got everything closed up already. You go on, I'll see you soon, babe?"
    "You smirk when she calls you that."
    the_person "Is that okay? To call you that?"
    mc.name "Sure."
    $ the_person.set_mc_title("Babe")
    mc.name "Take care."
    $ the_person.apply_outfit(the_person.planned_outfit)
    $ clear_scene()
    $ mc.change_location(downtown)
    "You leave the coffee shop and start to walk around downtown some, lost in your thoughts."
    "Last week, you found out the hot barista you've been hitting on's mom is dying and her dad is already gone."
    "And now... you are dating?"
    if the_person.knows_pregnant:
        "And you've knocked her up!"
    "[the_person.possessive_title] seems very eager to put out. Normally sexy time would be something you would plan, but you decide for now to let her see what she can come up with."
    #TODO find some way to drop a hint here that the best way to continue the storyline is to invite Kaya over for a sleepover date.
    #Adding on talk events to jennifer and lily that are currently blank, so that in the future when the mod updates we can write those scenes and include save game compatibility.
    # $ mom.add_unique_on_talk_event(kaya_jennifer_reveal)
    # $ lily.add_unique_on_talk_event(kaya_lily_reveal)
    $ kaya.add_unique_on_talk_event(kaya_barista_fuck_intro)
    $ sakari.add_unique_on_room_enter_event(sakari_intro)
    $ sakari.set_schedule(clothing_store, the_days = [0, 1, 2, 3, 4], the_times = [1])
    return

label kaya_jennifer_reveal_label(the_person):
    # Use this label to talk to Mom about your incest with Kaya
    pass
    return

label kaya_lily_reveal_label(the_person):
    # Use this label to talk to Lily about Kaya
    pass
    return

label kaya_barista_fuck_intro_label(the_person):    #60 sluttiness
    $ kaya.event_triggers_dict["can_get_barista_quickie"] = True
    $ the_person.arousal = 20
    $ kaya.event_triggers_dict["barista_fuck_last_day"] = day
    # Kaya works out a deal with a co-worker to fuck you on her break
    $ the_person.draw_person()
    "You swing by the coffee shop. You see that [the_person.title] is there, looking as hot as ever."
    "She sees you when you come in and waves you over to the counter. Thankfully there isn't a line."
    the_person "Hey! I'm glad you swung by!"
    mc.name "Oh?"
    the_person "Yeah, I'm just getting ready to take my break. Let me just tell my coworker to take over for me."
    $ the_person.draw_person(position = "walking_away")
    "She turns to her coworker, from the looks of it another college student. He just nods at her and gives you a quick wave."
    $ the_person.draw_person()
    the_person "Okay, follow me!"
    $ the_person.draw_person(position = "walking_away")
    "You follow [the_person.possessive_title] behind the counter and into a back storage area. You don't think you've ever been back here before?"
    "The door closes behind you, you follow her to the back corner, out of sight from the door."
    $ the_person.draw_person(position = "kissing")
    "When she turns around, she pulls you into an embrace and kisses your neck."
    the_person "Want to get busy?"
    mc.name "In the storage room? Isn't..."
    if the_person.is_girlfriend:
        the_person "I was complaining to my coworker about how I'd finally found a boyfriend but had to move in with my mom and it was impossible to get any alone time."
    else:
        the_person "I was complaining to my coworker about how I'd finally found an awesome hookup but had to move in with my mom and it was impossible to get any alone time."
    the_person "He said as long as we don't take forever or make a bunch of noise then we can hook up back here once in a while..."
    $ mc.change_locked_clarity(20)
    "[the_person.title] rakes her nails down your back as she finishes her sentence."
    "You look around the room. There's really nothing to set her on, but there is a small counter you can bend her over."
    the_person "What do you think?"
    mc.name "Are you sure you can be quiet?"
    $ the_person.change_arousal(15)
    $ the_person.change_happiness(3)
    the_person "No, but I'm willing to try."
    "You turn [the_person.possessive_title] around and bend her over the counter."
    $ the_person.draw_person(position = "standing_doggy")
    mc.name "Ah, maybe I should bring a gag with me next time I stop by for coffee."
    "You know you have to be quick, so you quickly pull away at the clothing between you and [the_person.title]'s fertile young cunt."
    $ the_person.strip_to_vagina(prefer_half_off = True, delay = 1)
    mc.name "You sure you are ready for this? This is kinda fast..."
    the_person "I was day dreaming about your cock when you walked in. Don't be gentle, I'm ready."
    "You run a finger along her slit with one hand while you undo your zipper with the other. She isn't lying, her pussy is wet and ready."
    mc.name "Wow you really are wet."
    if the_person.is_pregnant:
        the_person "I've always been kind of like this, but I think the hormone changes are making my urges even stronger."
    the_person "I've been waiting for a guy like you to come around for a while, now I feel like I just can't get enough..."
    "You step forward and get into position behind [the_person.title]. You run your cock up and down her slit a couple times, getting the tip nice and wet."
    "You slowly push into her. She reaches back and grabs your leg, urging you forward as her cunt stretches to receive you."
    "She keeps her voice hushed, as she urges you in between moans."
    the_person "That's it, now don't stop until you fill me up...!"
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_counter(), skip_intro = True, skip_condom = True, position_locked = True, private = True) from _call_sex_kaya_barista_quicky_01
    $ report_log = _return
    $ the_person.draw_person(position = "standing_doggy")
    if report_log.get("creampies", 0) > 0 and report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
        "Your cum is dripping down the inside of her legs."
    elif report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
    else:
        "When you step back, [the_person.possessive_title] sighs happily."
    kaya "Oh god... that was so good..."
    $ the_person.draw_person()
    "[the_person.title] stands up."
    kaya "Alright, I'd better straighten myself up and get back to work. There's a door back there that leads out into the alley... do you mind letting yourself out?"
    mc.name "Uhh sure, that would be no problem."
    kaya "Thanks! Now, we can't do this too often, maximum every few days, okay?"
    mc.name "Sounds good to me."
    $ kaya.apply_planned_outfit()
    $ clear_scene()
    "You step out of the back door and into the alley, leaving [the_person.possessive_title] to finish her shift."
    "This is an interesting development with [the_person.title]. Once in a while, you can swing by the coffee shop during the afternoon for a quickie."
    "While not as satisfying as full on sex, a quickie is better than nothing."
    if kaya_has_started_internship():
        $ kaya.event_triggers_dict["can_get_work_quickie"] = True
        "You should enjoy this phase of your relationship with her while it lasts. She is already your intern, and you doubt she is going to keep working here once she graduates!"
    else:
        "You should enjoy this phase of your relationship with her while it lasts. You doubt she is going to keep working here once she graduates!"
    return

label kaya_barista_fuck_label(the_person):
    $ start_energy = the_person.energy
    mc.name "Want to take a break..?"
    "You trail off the end of the sentence, making it clear you mean a break in the back of the shop."
    "[the_person.possessive_title] looks over and sees their coworker. She gives him a wave, then looks back."
    the_person "Yes. Follow me!"
    $ the_person.draw_person(position = "walking_away")
    "You follow [the_person.possessive_title] behind the counter and into a back storage area."
    "The door closes behind you, you follow her to the back corner, out of sight from the door."
    $ the_person.draw_person(position = "kissing")
    "When she turns around, she pulls you into an embrace and kisses your neck."
    the_person "Want to get busy?"
    "[the_person.title] rakes her nails down your back as she finishes her sentence."
    mc.name "Are you sure you can be quiet?"
    $ the_person.change_arousal(15)
    $ the_person.change_happiness(3)
    the_person "No, but I'm willing to try."
    "You turn [the_person.possessive_title] around and bend her over the counter."
    $ the_person.draw_person(position = "standing_doggy")
    # sex shop gag purchase for obedience gain
    # mc.name "Ah, maybe I sould bring a gag with me next time I stop by for coffee."
    "You know you have to be quick, so you quickly pull away at the clothing between you and [the_person.title]'s fertile young cunt."
    $ the_person.strip_to_vagina(prefer_half_off = True, delay = 1)
    mc.name "You sure you are ready for this? This is kinda fast..."
    the_person "I was day dreaming about your cock when you walked in. Don't be gentle, I'm ready."
    "You run a finger along her slit with one hand while you undo your zipper with the other. She isn't lying, her pussy is wet and ready."
    mc.name "Wow you really are wet."
    if the_person.is_pregnant:
        the_person "I've always been kind of like this, but I think the hormone changes are making my urges even stronger."
    the_person "I feel like I just can't get enough..."
    "You step forward and get into position behind [the_person.title]. You run your cock up and down her slit a couple times, getting the tip nice and wet."
    "You slowly push into her. She reaches back and grabs your leg, urging you forward as her cunt stretches to receive you."
    "She keeps her voice hushed, as she urges you in between moans."
    the_person "That's it, now don't stop until you fill me up...!"
    call fuck_person(the_person, start_position = standing_doggy, start_object = make_counter(), skip_intro = True, skip_condom = True, position_locked = True, private = True) from _call_sex_kaya_barista_quicky_02
    $ report_log = _return
    $ the_person.draw_person(position = "standing_doggy")
    if report_log.get("creampies", 0) > 0 and report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
        "Your cum is dripping down the inside of her legs."
    elif report_log.get("girl orgasms", 0) > 0:
        "When you step back, [the_person.possessive_title]'s legs are shaking, but she manages to stay standing."
    else:
        "When you step back, [the_person.possessive_title] sighs happily."
    kaya "Oh god... that was so good..."
    $ the_person.draw_person()
    "[the_person.title] stands up."
    kaya "Alright, I'd better straighten myself up and get back to work... do you mind letting yourself out?"
    mc.name "Uhh sure, that would be no problem."
    kaya "Thanks! Now, we can't do this too often, maximum every few days, okay?"
    mc.name "Sounds good to me."
    $ kaya.apply_planned_outfit()
    $ clear_scene()
    "You step out of the back door and into the alley, leaving [the_person.possessive_title] to finish her shift."
    if kaya_has_started_internship():
        $ kaya.event_triggers_dict["can_get_work_quickie"] = True
        "You should enjoy this phase of your relationship with her while it lasts. She is already your intern, and you doubt she is going to keep working here once she graduates!"
    else:
        "You should enjoy this phase of your relationship with her while it lasts. You doubt she is going to keep working here once she graduates!"
    $ kaya.event_triggers_dict["barista_fuck_last_day"] = day
    return

label kaya_jennifer_confrontation_label():  #Requires sexual actions taken with Jennifer
    "Make a date with Kaya. Plan it for MC's place."
    "Sneak toward's MC's room, but Jennifer notices."
    "She confronts MC and Kaya. Accuses Kaya of trying to steal her son from her."
    "MC steps in, stops things from getting crazy. Kaya is family, should treat her as such."
    "Ends with reconciliation. Threesome with Kaya and Jennifer."
    return

label play_billiards(the_person, skill_offset = 0): #MC can play billiards.
    $ the_person.draw_person()
    "[the_person.title] grabs a pool stick and starts to chalk the end while you rack the billiard balls."
    "Once you've got them nice and tight, you nod to her."
    mc.name "Go ahead, you can break."
    menu:
        "Play the game":
            pass
        "Simulate the game":
            pass
    return

init 2 python:
    def calc_pool_ball_sink_chance(skill = 0, difficulty = 0):
        if renpy.random.randint(0,100) < min((50 + (skill * 5) ) - (difficulty * 10), 90):
            return True
        return False

init 3 python:      #Use this section to make wrappers for determining where we are in relation to Kaya's major story events
    def kaya_has_finished_intro():
        return kaya.event_triggers_dict.get("intro_complete", False)   # True after first talk

    def kaya_can_get_drinks():
        return kaya.event_triggers_dict.get("can_get_drinks", False)

    def kaya_has_had_drink_date():
        return kaya.event_triggers_dict.get("drink_date_complete", False)

    def kaya_can_get_barista_quickie():
        return kaya.event_triggers_dict.get("can_get_barista_quickie", False)

    def kaya_has_started_internship():
        return kaya.event_triggers_dict.get("has_started_internship", False)

    def kaya_has_moved():
        return kaya.event_triggers_dict.get("has_moved", False)

    def kaya_had_condom_talk():
        return kaya.event_triggers_dict.get("no_condom_talk", False)

    def kaya_condom_check():    #Generally, events with Kaya should skip condom scene, UNLESS pregnancy pref is set to 0. Use this to determine if skip_condom should be true
        if persistent.pregnancy_pref == 0:
            return False
        return True

    def kaya_studies_with_lily():
        return kaya.event_triggers_dict.get("studies_with_lily", False)

    def kaya_studies_with_erica():
        return kaya.event_triggers_dict.get("studies_with_erica", False)

    def kaya_mc_knows_relation():
        return kaya.event_triggers_dict.get("mc_knows_relation", False)

    def kaya_can_get_work_quickie():
        return kaya.event_triggers_dict.get("can_get_work_quickie", False)


    def kaya_vaginal_position_filter(vaginal_positions):
        return kaya_had_condom_talk()

    def kaya_anal_position_filter(anal_positions):
        # for now unlock after a few creampies
        return kaya_had_condom_talk() and \
            kaya.sex_record.get("Vaginal Creampies", 0) > 3
