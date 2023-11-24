from kivy.uix.screenmanager import ScreenManager
from screens import *
from kivy.lang import Builder

# --------------------------------------------------------------------------------

class CustomScreenManager(ScreenManager):

    # OverRide On_Touch_Down
    def on_touch_down(self, touch):
        print(f'Touch_Down at: {touch.pos}')
        return super().on_touch_down(touch)
    
    # OverRide On_Touch_Move
    def on_touch_move(self, touch):
        print(f'Touch_Move at: {touch.pos}')
        return super().on_touch_move(touch)
    
    # OverRide On_Touch_Up
    def on_touch_up(self, touch):
        print(f'Touch_Up at: {touch.pos}')
        return super().on_touch_up(touch)

# --------------------------------------------------------------------------------

# Load the Necessary Kivy Files to Build the Root Screen Widget
Builder.load_file('screen_manager.kv')
Builder.load_file('screens.kv')

# Screen Manager
screen_manager = CustomScreenManager()

# Add Screens with the add_widget() function, which passes 
# a name parameter that it can be recognized by
screen_manager.add_widget(TitleScreen(name = 'title'))
screen_manager.add_widget(GameScreen(name = 'game'))
screen_manager.add_widget(HiScoresScreen(name = 'hiscores'))
screen_manager.add_widget(SettingsScreen(name = 'settings'))