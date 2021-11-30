from kivy.app import App
from kivy.lang import  Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.widget import Widget
from  kivy.uix.popup import Popup

class Widgets(Widget):
    def btn(self):
        show_popup()
    pass

class P(FloatLayout):
    pass

class MyApp(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()

    popupWindow = Popup(title="Popup Window",content = show,size_hint=(None,None),size = (400,400))

    popupWindow.open()


if __name__ == "__main__":
    MyApp().run()