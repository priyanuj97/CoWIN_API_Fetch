from pygame import mixer
import time

def play(address):
    mixer.init()
    mixer.music.load(address)
    mixer.music.set_volume(1)
    mixer.music.play()
    
    while True:      
        print("Press 'p' to pause, 'r' to resume")
        print("Press 'e' to exit the program")
        query = input("  ")
        
        if query == 'p':
            mixer.music.pause()     
        elif query == 'r':
            mixer.music.unpause()
        elif query == 'e':
            mixer.music.stop()
            break

if __name__ == '__main__':
    play('Levitating.mp3')