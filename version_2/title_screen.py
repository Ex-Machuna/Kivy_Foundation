from kivy.uix.screenmanager import Screen

from kivy.lang import Builder

# --------------------------------------------------------------------------------

class TitleScreen(Screen):
    pass

# --------------------------------------------------------------------------------

Builder.load_file('title_screen.kv')

# Title Screen
title_screen = TitleScreen(name = 'title')