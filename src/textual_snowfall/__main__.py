from textual.app import App

from .widgets import Snowfall

class MyApp(App):
    def compose(self):
        yield Snowfall()

MyApp().run()

