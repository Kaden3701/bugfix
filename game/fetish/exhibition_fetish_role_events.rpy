# Use this file for role related events and actions.
init 2 python:
    sb_free_strip_pose_list = [["Turn around","walking_away"],["Turn around and look back","back_peek"],["Hands down, ass up","standing_doggy"],["Be flirty","stand2"],["Be casual","stand3"],["Strike a pose","stand4"],["Move your hands out of the way","stand5"]]

    def sb_free_strip_build_strip_menu(person, must_be_naked):
        option_list = []
        option_list.append("Choose Strip Action")
        for item in person.outfit.get_unanchored():
            if not item.is_extension:
                test_outfit = person.outfit.get_copy()
                test_outfit.remove_clothing(item)

                display_string = "Strip " + item.name
                option_list.append([display_string, [item, 0]])

        option_list.append(["Just watch","Watch"])
        option_list.append(["Tell her to pose","Pose"])
        if not must_be_naked or person.outfit.has_full_access:
            option_list.append(["Finish the show","Finish"])
        return option_list

    def sb_free_strip_build_pose_menu(current_pose):
        option_list = []
        option_list.append("Choose Pose")
        for pose in sb_free_strip_pose_list:
            if not pose[1] == current_pose:
                option_list.append(pose)
        option_list.append(["Never mind",None])
        return option_list

init 3 python:
    exhibition_fetish_role = Role(role_name = "Exhibitionist", actions = [])

    def add_exhibition_fetish(person):
        person.add_role(exhibition_fetish_role)
        #person.update_sex_skill("Vaginal", 6)
        person.event_triggers_dict["LastExhibitionFetish"] = day
        # fetish_add_collar(person, breed_collar)
        return


#Strip scene for exhibitionists
# label free_strip_scene(the_person, must_be_naked = True):
#     $ picked_pose = the_person.idle_pose #She starts in her idle pose (which is a string)
#     $ keep_stripping = True #When set to false the loop ends and the strip show stops.

#     while keep_stripping:
#         $ ran_num = renpy.random.randint(0,3) #Produce 4 different descriptions at each level to help keep this interesting.
#         $ the_person.draw_person(position = picked_pose)
#         $ the_clothing = the_person.choose_strip_clothing_item()
#         if ran_num == 0:
#             if the_clothing is not None:
#                 "[the_person.possessive_title] pulls at her [the_clothing.name] seductively."
#                 the_person "Mmm, I bet you want me to take this off, right?"
#                 "[the_person.possessive_title] wiggles her hips side to side and bites her bottom lip, as if imagining some greater pleasure yet to come."
#             else:
#                 "[the_person.possessive_title] runs her hands down her body seductively."
#                 the_person "Mmm, I bet you want to get your hands on me now, right?"
#                 "[the_person.possessive_title] wiggles her hips side to side and bites her bottom lip, as if imagining some greater pleasure yet to come."

#         elif ran_num == 1:
#             if the_person.has_large_tits:
#                 "[the_person.possessive_title] moves her body side to side for you, letting her large tits bounce and jiggle while you watch."
#                 "[the_person.possessive_title] takes a wider stances and slides her hands down her own thighs, all while maintaining eye contact with you."
#                 the_person "You're looking so good today [the_person.mc_title], did you know that?"
#             else:
#                 "[the_person.possessive_title] moves her body side to side for you while you watch."
#                 "[the_person.possessive_title] takes a wider stances and slides her hands down her own thighs, all while maintaining eye contact with you."
#                 the_person "You're looking so good today [the_person.mc_title], did you know that?"

#         elif ran_num == 2:
#             if the_clothing is not None:
#                 "[the_person.possessive_title] slips a hand under her [the_clothing.name] and starts to pull it off."
#                 the_person "Maybe I should just... slip this off. What do you think?"
#             else:
#                 if the_person.has_large_tits:
#                     "[the_person.possessive_title]'s hands slide up and down her body. She cups one of her sizeable breast and squeezes it, pinching her own nipple while she does."
#                     the_person "Oh [the_person.mc_title], I think I'm going to need more than your eyes on me soon..."
#                 else:
#                     "[the_person.possessive_title]'s hands slide up and down her body. She rubs her small breasts, paying special attention to their firm nipples."
#                     the_person "Oh [the_person.mc_title], I think I'm going to need more than your eyes on me soon..."
#         else:
#             the_person "I hope you're enjoying the show [the_person.mc_title]."
#             "She wiggles her hips for you and winks."

#         call screen main_choice_display(build_menu_items([sb_free_strip_build_strip_menu(the_person, must_be_naked)]))
#         $ strip_choice = _return

#         if strip_choice == "Watch":
#             if renpy.random.randint(0,1) == 0:
#                 $ the_clothing = the_person.choose_strip_clothing_item()
#                 if renpy.random.randint(0,100) < 67: #She's independent enough to strip, change pose, etc. on her own.
#                     if the_clothing is not None : #A more obedient person is less willing to strip without being told to. A less obedient person will strip further on their own.
#                         $ the_person.draw_animated_removal(the_clothing, position = picked_pose)
#                         "You watch as [the_person.possessive_title] grabs their [the_clothing.name] and pulls it off."
#                     else:
#                         #She has nothing to strip off or she's as slutty as she's willing to get
#                         "[the_person.possessive_title] seems comfortable just the way she is."
#                 else: #She doesn't quite know what to do without you telling her.
#                     "Without any direction [the_person.possessive_title] just keeps doing what she was doing."
#             else:
#                 #She decides to change pose half the time.
#                 $ new_pose = get_random_from_list(sb_free_strip_pose_list)
#                 if not new_pose[1] == picked_pose:
#                     $ picked_pose = new_pose[1]
#                     "While you're watching [the_person.possessive_title] changes pose so you can see her from a different angle."
#                 else:
#                     "[the_person.possessive_title] seems comfortable just the way she is."
#         elif strip_choice == "Pose":
#             #You ask her to change into a different pose
#             mc.name "I want to see you from a different angle."

#             call screen main_choice_display(build_menu_items([sb_free_strip_build_pose_menu(picked_pose)]))

#             if _return in [x[1] for x in sb_free_strip_pose_list]:
#                 $ picked_pose = _return
#                 "[the_person.possessive_title] nods and moves for you."
#             else:
#                 mc.name "Never mind, you look perfect like this."
#         elif strip_choice == "Finish":
#             $ keep_stripping = False
#             mc.name "Wow [the_person.title], that was amazing."
#             call break_strip_outfit_taboos(the_person) from _call_break_strip_outfit_taboos_free_strip_scene
#             if _return:
#                 the_person "Oh my, I didn't think I could go that far, I'm glad you enjoyed it."
#             else:
#                 the_person "Oh, are we done already? It feels like something is just getting started!"
#         else:
#             $ the_clothing = strip_choice[0]
#             the_person "This you mean? You want me to take this off?"
#             $ the_person.draw_animated_removal(strip_choice[0], position = picked_pose)
#             "[the_person.possessive_title] strips off her [the_clothing.name]. She throws it playfully, hitting you in the face." #Hopefully this wasn't shoes, lol

#     $ the_clothing = None
#     $ picked_pose = None
#     return
