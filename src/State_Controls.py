import TronEntities
import Map
from pynput import keyboard
import GameFunctions
import threading
import MainMenu


def runGame():
    """Decides where to send user, menu or game, based on gamestate"""

    if TronEntities.game_State == False:
        print("Running menu INIT")
        MainMenu.mMenu()  
        
    else:
        print("Running game INIT")

        """Pynput listener. Runs on separate thread to read inputs while turtle draws"""
        pynput_listener = keyboard.Listener(on_press=GameFunctions.on_press)
        pynput_listener_thread = threading.Thread(target=pynput_listener.start)
        pynput_listener_thread.daemon = True  # Allow program to exit even if this thread is running
        pynput_listener_thread.start()


        """Initializes maps and characters | runs main controls and game logic loop"""
        Map.init_MAP()
        TronEntities.Tron_INIT()
        TronEntities.Clu_INIT()
        GameFunctions.game_Loop()  # Start the game loop
