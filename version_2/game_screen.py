from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

from kivy.lang import Builder

# --------------------------------------------------------------------------------

class GameScreen(Screen):
    pass

# --------------------------------------------------------------------------------

Builder.load_file('game_screen.kv')

# Game Screen
game_screen = GameScreen(name = 'game')

layout = FloatLayout()
grid_layout = GridLayout(cols=5, 
                         rows=5, 
                         size_hint=(None, None), 
                         size=(300,300),
                         pos_hint={'center_x': 0.5, 'center_y': 0.5})
for i in range(25):
    grid_layout.add_widget(Button(text=str(i+1)))
layout.add_widget(grid_layout)
game_screen.add_widget(layout)