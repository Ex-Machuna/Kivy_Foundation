from kivy.uix.screenmanager import Screen

from kivy.lang import Builder

# --------------------------------------------------------------------------------

class HiScoresScreen(Screen):
    pass

# --------------------------------------------------------------------------------

Builder.load_file('hiscores_screen.kv')

# HiScores Screen
hiscores_screen = HiScoresScreen(name = 'hiscores')