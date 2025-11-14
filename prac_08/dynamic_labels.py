from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.lang import Builder

class DynamicLabelsApp(App):
    status_text = StringProperty("Ready")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # The list of names to create Labels for
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        # Load the kv file
        return Builder.load_file("dynamic_labels.kv")

    def create_widgets(self):
        # Add a Label for each name
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.entries_box.add_widget(temp_label)
        self.status_text = f"{len(self.names)} Labels Created"

    def clear_all(self):
        # Remove all Labels from entries_box
        self.root.ids.entries_box.clear_widgets()
        self.status_text = "Cleared"

if __name__ == "__main__":
    DynamicLabelsApp().run()
