from kivy import *
from kivy.app import App
from kivy.uix import widget


class MyGrid(widget):
    pass

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__=="__main__":
    MyApp().run()