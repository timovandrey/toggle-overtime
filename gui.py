################################################################################
# File:         gui.py
# Author:       Timo Vandrey
# Date:         19.06.2022
# Version:      1
# Description:
# This is the GUI object and representation of the overtime calculator.
################################################################################
# IMPORTS                                                                      #
################################################################################
from kivy.app import App
from kivy.uix.button import Button
 
class TestApp(App):
    def build(self):
        return Button(text= " Hello Kivy World ")
 
TestApp().run()