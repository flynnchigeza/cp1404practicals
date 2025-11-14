"""
CP1404 Prac 8 - Convert Miles to Kilometres App
Do-from-scratch exercise
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesKmConverterApp(App):
    """Main App class for converting miles to kilometres."""

    output_text = StringProperty("0.0")

    def build(self):
        """Build the Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Handle conversion from miles to kilometres."""
        miles = self.get_valid_miles()
        result = miles * MILES_TO_KM
        self.output_text = str(result)

    def handle_increment(self, change):
        """Increase or decrease the miles value."""
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def handle_text(self):
        """Update the output whenever text changes."""
        self.handle_convert()

    def get_valid_miles(self):
        """Get a valid number from the input field, or return 0.0."""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


if __name__ == '__main__':
    MilesKmConverterApp().run()
