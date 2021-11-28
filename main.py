from kivy import *
from kivy.app import App
from kivy.uix import widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout


class MyGrid(widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    pass

    def btn(self,instance):
        print("Nmae:",self.name.text,"email:",self.email.text)
        self.name.text = ""
        self.email.text = ""

def btn(instance):
    print("Run!")

class MyApp(App):
    def build(self):
        return MyGrid()

    def btn(self):y

if __name__=="__main__":
    MyApp().run()