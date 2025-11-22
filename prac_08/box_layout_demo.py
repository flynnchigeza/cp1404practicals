from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):
    """Main app class for BoxLayout demo."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "BoxLayout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greeting button press."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Handle clear button press."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


# Run the app
if __name__ == '__main__':
    BoxLayoutDemoApp().run()

