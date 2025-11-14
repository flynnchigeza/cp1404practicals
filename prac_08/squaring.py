"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Lindsay Ward, IT@JCU
Started 13/10/2015
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Flynn Chigeza'


class SquaringApp(App):
    """Main app class for squaring numbers."""

    def build(self):
        """Build the app from the KV file."""
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        """Handle calculation when button is pressed."""
        try:
            value = float(self.root.ids.input_number.text)
            result = value ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input!"


if __name__ == '__main__':
    SquaringApp().run()
