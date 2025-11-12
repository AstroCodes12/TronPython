# TronPython
A remake of Tron using Turtle Module for ERAU CS-118


GAME LOOP FUNCTIONALITY
    -The main game loop is a recursive function in GameFunctions.py called game_Loop()
            -game loop works by running all of the code sequentially, updating player position and direction, then updating the screen so that it looks like their moving at the same time. 

    -I used the pynput Keyboard module to take keyboard inputs because the turtle module version was too glitchy for me, and this allowed for more customization of what is run when the key is pressed

    -Player motion works by using the keys to change the direction of the player, then via a loop (recursive function in game_Loop()), it moves the player 25 pixels at a time in the set direction until it changes again

TRAIL AND KILLING FUNCTIONALITY
    -record_Trail takes a recording of the previous positions of the bike, storing each 2dVECT tuple in a list

    -trail_Kill() works by taking all of the stored 2DVECTs from record_Trail() and turning the list of tuples into a set of tuples and using the & (Intersect) set operator to find if there are any 'same' positions in the lists
        - if it finds a 'same' position, it kills the player
        -additionally, trail_Kill() compares the length of the 2DVECT list and the 2DVECT set, as if their lengths are different, then one of the bikes crossed their own path (because sets cannot have duplicates, and lists can)


NOTES:
    -Everything is called in Main

    -Listener from Pynput/keyboard is initialized in Main

    -screen.mainloop() is called at the end of Main.py ALWAYS | DO NOT CHANGE THIS OR IT WILL NOT RUN

    -screen is a variable in Map that contains the turtle.screen() object. This is so screen functionality is accessible
    
    -The main functions that initialize the map are create_Border(), create_Grid(), and create_Background() in Map.py

    -The main functions that initiaize the players are Tron_INIT() and Clu_INIT() in TronEntities.py
