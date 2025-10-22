def Trail_Kill(trail_List, player_Pos):
    for pos in trail_List:
        if player_Pos == pos:
            print("Collision Detected!")
            return "Dead"
        else:
            print("No Collision")
            return "Alive"
