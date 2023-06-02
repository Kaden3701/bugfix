# The default candace event series. Since she is already a bimbo, she starts at 40 sluttiness, which will compact this storyline considerably.
# In Candace's lust arc, we use her slutty aspects to enhance the supply division.
# She "accidentally" discovers new methods for getting cheap deals on supplies and for increasing supply rates, usually by captilizing on some sexual performance.
# Once unlocked, others in the supply division can be assigned the same duties to mimic her performance.
# Using her sexual prowess for business gains puts her in conflict with Sarah and Sarah's obedience path.
# Progression in Sarah's obedience path opens a teamup for Candace and Sarah as you try to train similar traits into Sarah.

init -1 python: #Requirement Functions
    def candace_overhear_supply_order_requirement(person):
        if person.sluttiness < 40:
            return False
        if not candace.story_event_ready("lust"):
            return False
        return time_of_day > 1 and person.is_at_work

    def candace_supply_order_discount_requirement():
        return time_of_day == 1 and mc.is_at_work and mc.business.is_open_for_business

    def candace_uniform_complaint_requirement():
        return False

    def candace_sex_shop_trip_requirement(person):
        return False

    def candace_supply_leader_team_huddle_requirement():
        return False

init 2 python:  #Actions and other functions
    candace_overhear_supply_order = Action("Candi's Supply Order", candace_overhear_supply_order_requirement, "candace_overhear_supply_order_label")
    candace_supply_order_discount = Action("Candi's Supply Discount", candace_supply_order_discount_requirement, "candace_supply_order_discount_label")
    candace_uniform_complaint = Action("Candi Hates the Uniforms", candace_uniform_complaint_requirement, "candace_uniform_complaint_label")
    candace_sex_shop_trip = Action("Candi in a Sex Store", candace_sex_shop_trip_requirement, "candace_sex_shop_trip_label")
    candace_supply_leader_team_huddle = Action("Candi Trains the Girls", candace_supply_leader_team_huddle_requirement, "candace_supply_leader_team_huddle_label")
    pass

#Labels
label candace_overhear_supply_order_label(the_person):  #45
    "You step into the office and look around. You see your employees hard at work. Close to you, you hear [the_person.title], on the phone with a supplier."
    "You can't help but overhear the conversation. As you look closer, you realize she is doing a video call."
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person, position = "sitting")
    the_person "Yes sir that's right. We need more of this stuff! Looks like it's called up... cal... calcium... phos... oh balls"
    "????" "I'm not sure I understand what you need. Do you have a label you can show me?"
    the_person "Oh! Certainly... I'd be glad to show you anything you want... let me see here."
    "She goes through a drawer in her desk and pulls out an empty vial. She tries holding it up to the camera."
    if the_person.tits_available:
        "????" "It's too close... can you back it up a little bit?... Yeah a bit farther..."
        "With her tits out, she pulls the vial back until it is resting in her cleavage."
        $ mc.change_locked_clarity(20)
        "????" "Now it's having a hard time focusing... can you move the camera closer?"
        "She takes the cam and brings up, point blank to her tits, with the little vial nestled between them."
    else:
        "????" "I can't make out the label, there's too many colors in the background..."
        the_person "Oh! I know how to fix that."
        "You are hardly surprised when you see [the_person.title] start to take her top off."
        $ scene_manager.strip_to_tits(person = the_person)
        the_person "How about now?"
        $ mc.change_locked_clarity(10)
        "????" "It's too close... can you back it up a little bit?... Yeah a bit farther..."
        "With her tits out, she pulls the vial back until it is resting in her cleavage."
        "????" "Now it's having a hard time focusing... can you move the camera closer?"
        $ mc.change_locked_clarity(20)
        "She takes the cam and brings up, point blank to her tits, with the little vial nestled between them."
    the_person "Are you getting a good look sir? Of the label, of course!"
    "????" "Yeah, I see it now. Calcium phosphide. You've been most helpful! I can get you a discount on those if you'd like, as thanks for your big... help."
    "[the_person.title] chuckles. You notice her nipples are getting a little stiffer... she seems to really be enjoying this..."
    the_person "No need! Maybe I could give you my number though... and you could show me your thanks later in... another way..."
    "She trades numbers with the supplier. Wait did she just turn down a discount? You watch as she says goodbye, making sure to lick her lips and wink before ending the call."
    "You decide to talk to her about it. You don't want to stifle her... creativity... but if she's getting discounts just for doing what she would already be doing, there's nothing wrong with that, right?"
    "You walk up to her desk. She smiles at you when she sees you approach."
    the_person "Hello [the_person.mc_title]! Anything I can do for you today?"
    "You get ready to speak... but you notice her posture subtly change as she finishes that sentence. Did she just push her chest out a bit? You shake it off."
    mc.name "Yes, sorry I couldn't help but overhear your conversation with that supplier."
    the_person "Yes... sorry I just couldn't help but have a little fun with the guy..."
    mc.name "That's perfectly fine, I didn't mind that at all."
    the_person "Oh? That's good!"
    mc.name "Yeah, I'm just curious. Why did you turn down the discount? If they are offering to discount the product..."
    the_person "Oh, that. Well, I've had several suppliers start to offer discounts the last few days. I would say yes but... I was concerned they might get the wrong idea about... why I am showing them my body..."
    the_person "I've gotten dick pics from three different suppliers in the last few days... it's been great! I want them to feel like they owe me!"
    mc.name "I'm sure that if you accepted their discount offer, they would still send you dick pics."
    "She thinks about what you said for a bit."
    the_person "I don't know... are you sure?"
    mc.name "I'll tell you what, try it on your next call and see what happens. If it doesn't go the way you want, you don't have to accept it anymore."
    the_person "Oh! That's a good idea! I mean yeah I miss out on one... but I suppose it's worth it to try!"
    "You are glad you get her to agree. You decide to let her get back to work."
    mc.name "Let me know how it goes."
    the_person "Yes sir!"
    $ scene_manager.clear_scene()
    $ mc.business.add_mandatory_crisis(candace_supply_order_discount)
    return  #40

label candace_supply_order_discount_label():
    $ the_person = candace
    $ scene_manager = Scene()  #Clean Scene
    $ scene_manager.add_actor(the_person)
    "As you arrive at work, [the_person.title] is wandering around, apparently looking for you."
    the_person "Ah! [the_person.mc_title]! I need to talk to you!"
    mc.name "Yes?"
    the_person "I tried what you said, and it worked! Our supplier for... for... fuck what was the chemical name..."
    "She stops talking for a second as she thinks."
    the_person "Ahh fuck it who cares. Whatever it was, they gave me a 10\% discount, and he even sent me a video later last night of him jacking off on a picture of my tits I sent him!"
    $ mc.change_locked_clarity(5)
    "That was... a lot of details."
    the_person "So... I kept going, and got almost all of our suppliers to give me some kind of discount! And it hasn't affected my umm... success rate... with sexting afterwards at all!"
    "You consider the implication. Maybe you could have her negotiate new standard rates with all your suppliers? Negotiating might be a bit tough for someone like her though..."
    "Fuck it, you decide to just let her get whatever discounts she happens to get and take the extra money without pushing your luck."
    mc.name "That's great. Thank you for your hard work."
    the_person "Yes sir!"
    $ candace.event_triggers_dict["supply_discount_active"] = True
    $ scene_manager.clear_scene()
    "[the_person.title] now receive a 10\% discount on all supply orders."
    $ cancace.event_triggers_dict["supply_discount"] = True
    $ mc.business.add_mandatory_crisis(candace_uniform_complaint)
    return

label candace_uniform_complaint_label():    #60
    pass
    return

label candace_sex_shop_trip_label(the_person):  #70
    pass
    return

label candace_supply_leader_team_huddle_label():    #80
    pass
    return
