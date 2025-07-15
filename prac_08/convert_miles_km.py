from kivy.app import App
from kivy.lang import Builder

class MilesConverterApp(App):
    """Kivy app for converting miles to kilometers."""
    def build(self):
        """Build the kivy app from the kv file."""
        self.title = 'Convert Miles to Kilometers'
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

MilesConverterApp().run()