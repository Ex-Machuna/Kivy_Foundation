import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

# --------------------------------------------------------------------------------

class TestLayout(FloatLayout):
    pass

class TestApp(App):

    # Build function creates the root widget of the application
    def build(self):

        # Build Widget Tree from .kv File
        Builder.load_file('testlayout.kv')

        # Return TestLayout Instance which will use the previously loaded Widget Tree
        return TestLayout()

# Run App
if __name__ == '__main__':
    TestApp().run()

# --------------------------------------------------------------------------------