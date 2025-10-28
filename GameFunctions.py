"""def Trail_Kill(trail_List, player_Pos):
    for pos in trail_List:
        if player_Pos == pos:
            print("Collision Detected!")
            return "Dead"
        else:
            print("No Collision")
            return "Alive"
"""

def Trail_Kill(trail_List, player_Pos):
    
    if player_Pos in trail_List:
        print("Collision Detected!")
        return "Dead"
    else:
        print(f"{trail_List} \n\n")
        print(f"{player_Pos} \n\n")
        print("No Collision")
        return "Alive"