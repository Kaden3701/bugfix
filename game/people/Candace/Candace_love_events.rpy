# In this arc we learn more about candace and her interests outside of being a bimbo.
# We take her out clothes shopping, to get her hair done, and a bar date
# She gets with Ophelia in her most obvious teamup after the salon event.

init -1 python: #Requirement Functions
    def candace_goes_clothes_shopping_requirement(person):
        if person.love < 20:
            return False
        if not candace.story_event_ready("love"):
            return False
        if not person.is_at_work:
            return False
        return True

    def candace_goes_to_salon_requirement():
        return False

    def candace_karaoke_date_invite_requirement(person):
        return False

    def candace_karaoke_date_requirement():
        return False

    def candace_booty_call_requirement():
        return False


init 2 python:  #Actions and other functions
    candace_goes_clothes_shopping = Action("Candi's Shopping", candace_goes_clothes_shopping_requirement, "candace_goes_clothes_shopping_label")
    candace_goes_to_salon = Action("Candi's Spa Day", candace_goes_to_salon_requirement, "candace_goes_to_salon_label")
    candace_karaoke_date_invite = Action("Candi's Date Request", candace_karaoke_date_invite_requirement, "candace_karaoke_date_invite_label")
    candace_karaoke_date = Action("Candi's Karaoke Date", candace_karaoke_date_requirement, "candace_karaoke_date_label")
    candace_booty_call = Action("Candi's Booty Call", candace_booty_call_requirement, "candace_booty_call_label")

#Labels

label candace_goes_clothes_shopping_label(the_person):
    $ the_person.draw_person(position = "sitting")
    $ the_person.story_event_log("love")
    "You step up to [the_person.possessive_title]'s desk. She's been working for you for a while now, so you decide to check up on her."
    mc.name "Hey there, [the_person.title]. How are you settling in?"
    the_person "Oh hey [the_person.mc_title]! It's going pretty good!"
    mc.name "Everything been working out okay?"
    the_person "Yes! It sure has! I have really been enjoying the work here, and the freedom I have now is great!"
    the_person "Guess what I did last night?"
    mc.name "What's that?"
    "[the_person.title] lowers her voice so as not to disturb others around her."
    the_person "I fucked my landlord!"
    mc.name "Oh! That's... great?!?"
    the_person "I know! And this time I did it just for fun! I didn't even need the rent discount! I just got my first paycheck. I've been trying to figure out what to do with it."
    mc.name "That's good to hear. And don't worry. It's not a race! You don't have to spend it as it comes in, you can always save some back."
    the_person "Yeah, I suppose. But it feels like, it's my first one, right? I should use it for something fun?"
    mc.name "That's true. Any ideas?"
    the_person "Well, I was thinking about going over to the mall. My boyf... I mean, my ex... he purged a lot of my favorite outfits. I was thinking about buying a couple new skirts or something!"
    mc.name "That's actually a really good idea."
    the_person "Yeah. I guess I'll just wait until this weekend. By the time I get off work here, I'm so tired."
    "You think about it for a moment."
    mc.name "You know... if you want to, you could always take a chunk of the day off and go. Honestly, I understand your situation, and I think it would be good for you to build your wardrobe back up."
    the_person "Oh! Are you sure? I mean, I only just started... playing hooky from work already?"
    "She thinks about it for a bit."
    the_person "That's really tempting... but, you know, back with my... ex... he used to help me pick out stuff to wear. I'm not sure I know what even looks good on me anymore!"
    mc.name "Umm, honestly, with a body like yours, just about anything looks good."
    $ the_person.change_stats(happiness = 2, love = 2)
    the_person "Aww, you charmer! I don't know, I just wish I had someone to go with me. A second set of eyes on everything, you know?"
    "Hmm... you COULD volunteer... you've never been clothes shopping with a woman like her before. All the tropes make it sound so boring. But, with a girl like [the_person.title], how boring could it be?"
    "You ponder it silently for a bit."
    the_person "Wait a minute... you're a guy!"
    mc.name "Yes... that is true?"
    the_person "Oh my god! Will you take me? PLEASE PLEASE PLEASE PLEEEEEAAASSSSEEEEE!"
    mc.name "You want me to go with you?"
    the_person "Of course! I mean, who else would be better to judge how sexy the outfits are? You, umm... you're into girls right?"
    if the_person.has_taboo("vaginal_sex"):
        mc.name "Ha! Yes, I'm definitely into girls."
    else:
        mc.name "Umm... we've had sex."
        the_person "Oh! Right... of course."
    the_person "Good, come on, just do it! I promise you won't regret it!"
    "A promise like that from [the_person.possessive_title] should not be taken lightly."
    mc.name "Ok. Let's go."
    if the_person.should_wear_uniform():
        the_person "Yay! I can't wait! Just let me get changed, real quick."
        $ the_person.apply_outfit(the_person.planned_outfit) # wear normal day clothes
        $ the_person.draw_person()
        "After a minute she comes back, ready to go."
    else:
        the_person "Yay! I can't wait!"

    $ the_person.change_location(clothing_store)
    $ mc.change_location(clothing_store)
    $ the_person.draw_person()

    "You leave the business and soon find yourself at the mall. You let [the_person.possessive_title] lead the way into the first store."
    "She browses through the racks of clothes but eventually finds a couple things she likes."
    the_person "Okay, you wait right here, I'll be right back to show you what I picked out!"
    $ clear_scene()
    call trying_on_clothes_label(the_person) from _clothes_shopping_candace_intro_01
    if _return > 0: # we bought some clothes
        "You walk with [the_person.title] up to the checkout line."
        the_person "God, that was fun! We should do that again sometime!"
        "You are surprised to admit it, but you actually had a lot of fun too."
        mc.name "Yeah I'd be up for doing that again sometime!"
        "At the checkout line, you pay for the new clothes for [the_person.possessive_title]."
        $ mc.business.change_funds(-100 * _return)
    else:
        "You walk with [the_person.title] to the exit."
        the_person "God, that was fun! Just a shame we didn't find anything we both like!"
        mc.name "I'm sure we will find something next time."
        the_person "Oh that's so nice, I can't wait for our next shopping trip!"

    mc.name "I'm not going back to work right away. Feel free to take the rest of the day off if you want."
    the_person "You're sweet. Thanks for the shopping trip!"
    $ the_person.draw_person(position = "walking_away")
    "This was really a fun way to watch [the_person.title] try on stuff in an intimate setting... maybe you should invite some other girls to go shopping sometime?"
    "You have now unlocked clothes shopping! Return to the clothing store anytime to invite a girl to go shopping with you."
    $ candace.event_triggers_dict["clothes_shopping"] = 1
    $ clothing_store.add_action(invite_to_clothes_shopping)
    $ mc.business.add_mandatory_crisis(candace_goes_to_salon)
    call advance_time from _call_advance_time_clothes_shopping_candace_1
    return  #20 Love

label candace_goes_to_salon_label():    #40 Love
    pass
    return

label candace_karaoke_date_invite_label(the_person):   #60 Love
    pass
    return

label candace_karaoke_date_label():
    pass
    return

label candace_booty_call_label():   #80 Love
    pass
    return
