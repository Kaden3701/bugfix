screen favourite_toggle_button(person):
    imagebutton:
        offset (10, 5)
        if person.is_favourite:
            idle "gui/extra_images/favourite_star_filled.png"
            hover "gui/extra_images/favourite_star_remove.png"
        else:
            idle "gui/extra_images/favourite_star_empty.png"
            hover "gui/extra_images/favourite_star_add.png"
        action [person.toggle_favourite, renpy.restart_interaction]
        tooltip "Toggle Favourite\nSets this person as one of your favourites, so you can find them on the map more easily."
