init -1 python:
    #Helper functions for creating instances of commonly used room objects.
    def make_wall():
        return RoomObject("wall",["Lean"])

    def make_door():
        the_door = RoomObject("door", ["Lean"])
        return the_door

    def make_window():
        return RoomObject("window",["Lean"])

    def make_chair():
        return RoomObject("chair",["Sit","Low"])

    def make_desk():
        return RoomObject("desk",["Sit","Lay","Low"])

    def make_table():
        return RoomObject("table",["Sit","Lay","Low"])

    def make_bed():
        return RoomObject("bed",["Sit","Lay","Low"])

    def make_couch():
        return RoomObject("couch",["Sit","Lay","Low"])

    def make_floor():
        return RoomObject("floor",["Lay","Kneel"])

    def make_grass():
        return RoomObject("grass",["Lay","Kneel"])

    def make_stage():
        return RoomObject("stripclub stage",["Lay","Sit"])

    def make_front_door():
        return RoomObject("front door", ["Lean"])

    def make_hall_carpet():
        return RoomObject("hall carpet", ["Kneel", "Lay"])

    def make_stairs():
        return RoomObject("stairs", ["Sit", "Low"])

    def make_swing():
        return RoomObject("sex swing",["Sit","Low","Lay", "Swing"])

    def make_counter():
        return RoomObject("counter",["Sit","Lay","Low"])

    def make_reception():
        return RoomObject("reception desk",["Sit","Lay","Low"])

    def make_dryer():
        return RoomObject("dryer", ["Sit","Lay"])

    def make_mirror():
        return RoomObject("mirror", ["Lean"])

    def make_medical_table():
        return RoomObject("medical table", ["Lay", "Sit", "Low"])

    def make_washing_machine():
        return RoomObject("washing machine", ["Sit", "Lay"])

    def make_bdsmbed():
        return RoomObject("Bed Cuffs", ["Lay", "Kneel"])

    def make_pillory():
        return RoomObject("Pillory", ["Stand", "Lean", "Low"])

    def make_woodhorse():
        return RoomObject("Wood Horse", ["Sit", "Lean", "Lay"])

    def make_cage():
        return RoomObject("Cage", ["Lay", "Kneel"])

    def make_toilet():
        return RoomObject("Toilet", ["Sit", "Low"])

    def make_sink():
        return RoomObject("Bathroom Sinks", ["Sit", "Lean", "Low"])

    def make_love_rug():
        return RoomObject("Love Rug", ["Kneel", "Lay"])

    # For parks and gym
    def make_bench():
        return RoomObject("Bench", ["Lay", "Sit", "Low", "Kneel"])

    def make_alley():
        return RoomObject("Alley", ["Lean", "Kneel"])

    # For R&D:
    def make_examtable():
        return RoomObject("Exam Table", ["Lay", "Sit", "Low"])

    # For strip_club:
    # strip club stage is make_stage()
    def make_pole():
        return RoomObject("Stripper Pole", ["Lean", "Low"])

    # Classic porn audition couch
    def make_white_leather_couch():
        return RoomObject("White Leather Couch",["Sit","Lay","Low"])


# room object collections
init 5 python:
    dungeon_objects = [
        make_bed(),
        make_couch(),
        make_bdsmbed(),
        make_pillory(),
        make_wall(),
        make_floor(),
    ]
    harem_objects =[
        make_bed(),
        make_couch(),
        make_chair(),
        make_wall(),
        make_floor(),
    ]
    downtown_bar_objects = [
        make_desk(),
        make_chair(),
        make_wall(),
        make_floor()
    ]
    downtown_hotel_lobby_objects = [
        make_desk(),
        make_chair(),
        make_wall(),
        make_floor(),
    ]
    downtown_hotel_room_objects = [
        make_desk(),
        make_chair(),
        make_floor(),
        make_window(),
        make_wall(),
        make_bed()
    ]
    purgatory_objects = [
        make_floor()
    ]
    laundry_room_objects = [
        make_washing_machine(),
        make_dryer(),
        make_wall(),
        make_floor()
    ]
    hair_salon_objects = [
        make_floor(),
        make_wall(),
        make_chair(),
        make_mirror(),
        make_window(),
        make_counter()
    ]
    generic_store_objects = [
        make_floor(),
        make_wall(),
        make_window(),
        make_counter()
    ]
    clothing_store_objects =[
        make_floor(),
        make_window(),
        make_counter(),
        RoomObject("Mannequin", ["Lean"])
    ]
    bdsm_room_objects = [
        make_pillory(),
        make_woodhorse(),
        make_cage(),
        make_chair(),
        make_wall(),
        make_floor(),
        make_bed(),
        make_couch(),
        make_pole(),
        make_stage()
    ]
    ceo_office_objects = [
        make_chair(),
        make_desk(),
        make_wall(),
        make_window(),
        make_floor(),
        make_white_leather_couch(),
    ]
    police_jail_objects = [
        RoomObject("cell bars", ["Lean"]),
        make_wall(),
        make_bed(),
        make_floor(),
    ]
    home_shower_objects = [
        make_floor(),
        make_wall(),
        RoomObject("shower door", ["Lean"]),
    ]
    gym_shower_objects = [
        make_floor(),
        make_wall(),
        RoomObject("shower door", ["Lean"]),
        make_bench(),
    ]
    coffee_shop_objects = [
        make_floor(),
        make_wall(),
        make_window(),
        make_counter(),
        RoomObject("booth", ["Sit", "Lay", "Low"]),
        make_bench()
    ]
    changing_room_objects = [
        make_wall(),
        make_floor(),
        make_chair()
    ]
    gaming_cafe_objects = [
        make_floor(),
        make_wall(),
        make_desk(),
        make_chair()
    ]
