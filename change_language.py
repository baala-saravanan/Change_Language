import gpio as GPIO
import sys
import os
from pydub import AudioSegment
sys.path.insert(0, '/home/rock/Desktop/Hearsight/')
from play_audio import GTTSA
from config import *


class CHLANG:
    def __init__(self):
        self.languages = ["Hindi","English","Tamil","Malayalam","Telugu","Kannada"]
        
        GPIO.setup([450, 421, 447, 448], GPIO.IN)
        self.play_audio = GTTSA()

    def handle_lang(self):
        self.play_audio.play_machine_audio("press_feature_button.mp3")
        counts = -1
        while True:
            input_state1 = GPIO.input(450)
            input_state2 = GPIO.input(421)
            input_state3 = GPIO.input(447)
            input_state4 = GPIO.input(448)
            
            if input_state1:
                direction = 1
                counts = (counts + direction) % len(self.languages)
                print(counts)
                self.play_audio.play_machine_audio("{}.mp3".format(self.languages[counts]))

            if input_state2:
                direction = -1
                counts = (counts + direction) % len(self.languages)
                print(counts)
                self.play_audio.play_machine_audio("{}.mp3".format(self.languages[counts]))

            if input_state3:
                self.play_audio.play_machine_audio("feature_confirmed.mp3")
                os.remove(LANG_FILE)
                with open(LANG_FILE,'w') as file:
                    file.write(self.languages[counts])
#                self.play_audio.play_machine_audio("Thank You.mp3")
                break
                    
            if input_state4:
                self.play_audio.play_machine_audio(f"feature_exited.mp3")
#                self.play_audio.play_machine_audio("Thank You.mp3")
                break