from godot import exposed, signal
from godot.bindings import Node2D, Input
import sys
import time
import os
import threading


from chatbotNew import main
ctime = os.stat('daveOutput').st_ctime
@exposed
class newBot(Node2D):
    def _input(self, delta):
        if (Input.is_action_pressed("dave_enter") and self.get_node("LineEdit").get_text() != ''): 
            ctime = os.stat('daveOutput').st_ctime
            userIn = open('userInput', 'w')
            userIn.write(self.get_node("LineEdit").get_text())
            userIn.close()
            bufferResp = self.get_node("LineEdit").get_text()
            self.get_node("LineEdit").set_text('')
            print(self.get_node('RichTextLabel').get_text())
            print(os.stat('daveOutput').st_ctime > ctime)
            while True:
                if os.stat('daveOutput').st_ctime > ctime:
                    self.get_node("RichTextLabel").add_text('\n\nYou: ' + bufferResp)
                    daveOut = open('daveOutput','r')
                    buffer = daveOut.read()
                    daveOut.close()
                    self.get_node('RichTextLabel').add_text("\n\nDave:"+buffer)
                    break
            time.sleep(1.0)

thr = threading.Thread(target=main, args=(), kwargs={})
thr.start()