"""
CP1404
Program Dynamic Labels
Latrel Heron
12/11/2023
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """DynamicLabelsApp dynamically creates a label for each name"""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Latrel", "James", "Lebron", "Lonzo", "Goats", "Max"]

    def build(self):
        """Build the Kivy app from the kv file """
        self.title = "Dynamically create a label from names"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_label(temp_label)


DynamicLabelsApp().run()
