from kivy.app import App

from screen_manager import screen_manager

# --------------------------------------------------------------------------------

# Application
class FoundationApp(App):

    # The build() function creates the root widget of the application
    def build(self):
        return screen_manager

# Run App
if __name__ == '__main__':
    FoundationApp().run()

# --------------------------------------------------------------------------------