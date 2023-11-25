from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from grid_widget import grid_widget
from kivy.lang import Builder

# --------------------------------------------------------------------------------

class GameScreen(Screen):
    pass

# --------------------------------------------------------------------------------

Builder.load_file('game_screen.kv')

# Game Screen
game_screen = GameScreen(name = 'game')

float_layout = FloatLayout()

float_layout.add_widget(grid_widget)

game_screen.add_widget(float_layout)