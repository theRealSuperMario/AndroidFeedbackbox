__author__ = 'max'


import kivy
import os.path
import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Canvas, Color
from kivy.graphics import Color, Rectangle
from kivy.uix.textinput import TextInput
from time import gmtime, strftime
import os.path
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.properties import NumericProperty, ListProperty
from kivy.core.audio import SoundLoader

#import kivy.factory.Factory
kivy.require('1.0.8')
#from kivy.graphics.instructions.Instruction import *


class FeedbackApp(App):

    def on_pause(self):
        #False => stop
        #True  => nix
        return False

    def on_stop(self):
        #with open("text.txt", "w") as file:
        #    file.write(App.get_running_app().root.ids.surveyLabel.text)
        with open("save_data.txt", "w") as file:
            data = {
                "text":     App.get_running_app().root.ids.surveyText.text,
                "yellow":   App.get_running_app().root.ids.yellow.count,
                "green":    App.get_running_app().root.ids.green.count,
                "red":      App.get_running_app().root.ids.red.count,
                "surveyFontSize":  App.get_running_app().root.ids.surveyLabel.font_size
            }
            file.write(json.dumps(data))



    def on_resume(self):
        #if os.path.isfile('text.txt'):
        #    file = open('text.txt', 'r')
        #    App.get_running_app().root.ids.surveyText.text = file.readline()
        #else:
        #    pass
        if os.path.isfile("save_data.txt"):
            file = open("save_data.txt", "r")
            #   load mit object
            #   loads mit strings
            data = json.load(file)
            App.get_running_app().root.ids.surveyText.text  =   data["text"]
            App.get_running_app().root.ids.yellow.count     =   data["yellow"]
            App.get_running_app().root.ids.red.count        =   data["red"]
            App.get_running_app().root.ids.green.count      =   data["green"]
            App.get_running_app().root.ids.surveyLabel.font_size = data["surveyFontSize"]
        else:
            pass
        return True

    def on_start(self):
        App.get_running_app().root.ids.red.colour = [1, 0, 0, 1]
        App.get_running_app().root.ids.yellow.colour = [1, 1, 0, 1]
        App.get_running_app().root.ids.green.colour = [0, 1, 0, 1]
        self.on_resume()




class CounterLabel(Label):
    count = NumericProperty()
    colour = ListProperty()
    sound = SoundLoader.load("smw_coin.wav")

    def increment(self):
        self.count += 1
        self.sound.stop()
        self.sound.play()

    def reset(self):
        self.count = 0

    def on_count(self, *args):
        self.text = str(self.count)

    def colorcomp(self, liste):
        c = [1, 1, 1, 1]
        if len(liste) == 0:
            return [0,0,0,0]
        for x in [0, 1, 2]:
            c[x] -= liste[x]
        return c

if __name__=="__main__":
    FeedbackApp().run()