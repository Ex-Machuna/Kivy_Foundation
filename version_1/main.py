from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# --------------------------------------------------------------------------------

class CustomScreenManager(ScreenManager):

    # OverRide On_Touch_Down to Inform User of Touch or Mouse Input
    def on_touch_down(self, touch):

        print(f'Touch_Down at: {touch.pos}')

        # Return the parent function as normal after performing your custom functions
        return super().on_touch_down(touch)
    
    # OverRide On_Touch_Move to Inform User of Touch or Mouse Input
    def on_touch_move(self, touch):

        print(f'Touch_Move at: {touch.pos}')

        # Return the parent function as normal after performing your custom functions
        return super().on_touch_move(touch)
    
    # OverRide On_Touch_Up to Inform User of Touch or Mouse Input
    def on_touch_up(self, touch):

        print(f'Touch_Up at: {touch.pos}')

        # Return the parent function as normal after performing your custom functions
        return super().on_touch_up(touch)

# --------------------------------------------------------------------------------

class TitleScreen(Screen):
    pass

class GameScreen(Screen):
    pass

# --------------------------------------------------------------------------------

# Application
class TestApp(App):

    # Build function creates the root widget of the application
    def build(self):

        Builder.load_file('titlescreen.kv')

        screen_manager = CustomScreenManager()
        screen_manager.add_widget(TitleScreen(name = 'title'))
        screen_manager.add_widget(GameScreen(name = 'game'))

        return screen_manager

# Run App
if __name__ == '__main__':
    TestApp().run()

# --------------------------------------------------------------------------------