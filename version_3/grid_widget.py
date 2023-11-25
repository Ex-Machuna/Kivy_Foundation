from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

# --------------------------------------------------------------------------------

class GridWidget(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.generate_grid()

    # Generate Grid
    def generate_grid(self):

        for i in range(25):
            self.add_widget(Button(text=str(i+1)))

# --------------------------------------------------------------------------------

grid_widget = GridWidget(   cols=5, 
                            rows=5, 
                            size_hint=(None, None), 
                            size=(300,300),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5}     )