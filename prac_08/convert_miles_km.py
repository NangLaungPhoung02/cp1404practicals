"""
convert_miles_km.py
Estimate time 40 minutes
Actual total three files time: 1 hour
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    output_km = StringProperty()

    def build(self):
        Window.size = (400, 150)
        self.title = "Miles to Kilometers"
        self.output_km = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        """Convert miles to kilometers and update label."""
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.output_km = str(km)

    def handle_increment(self, change):
        """Increase or decrease the miles value and update TextInput and result """
        miles = self.get_miles()
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_miles(self):
        """Return the number of miles as a float, or 0.0 if invalid."""
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
