from kivy.uix.screenmanager import Screen

from kivy.lang import Builder

# --------------------------------------------------------------------------------

class SettingsScreen(Screen):
    pass

# --------------------------------------------------------------------------------

Builder.load_file('settings_screen.kv')

# Settings Screen
settings_screen = SettingsScreen(name = 'settings')