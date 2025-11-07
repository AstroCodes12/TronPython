import TronEntities
import Map
from pynput import keyboard
import GameFunctions
import threading

game_State = GameFunctions.game_State



if game_State:
    pynput_listener = keyboard.Listener(on_press=GameFunctions.on_press, on_release=GameFunctions.on_release)
    pynput_listener_thread = threading.Thread(target=pynput_listener.start)
    pynput_listener_thread.daemon = True # Allow program to exit even if this thread is running
    pynput_listener_thread.start()

    Map.init_MAP()
    TronEntities.Tron_INIT()
    TronEntities.Clu_INIT()
    GameFunctions.game_Loop() # Start the game loop
else:
    print("Game Over") 