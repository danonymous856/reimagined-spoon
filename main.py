from kivy import *
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn=ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse Down",touch)
        self.btn.opacity = 0.5
        pass
    def on_touch_up(self, touch):
        print("Mouse Up",touch)
        pass
    def on_touch_move(self, touch):
        print("Mouse Move",touch)
        self.btn.opacity = 1
        pass

class MyApp(App):
    def build(self):
        return Touch()

if  __name__ == "__main__" :
    MyApp().run()