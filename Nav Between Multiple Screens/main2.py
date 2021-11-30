from kivy.app import App
from kivy.lang import  Builder
from kivy.uix.screenmanager import ScreenManager,Screen

class MainWindow(Screen):
    pass

class SreenWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my2.kv")


class MyMainApp(App):
    def build(self):
        return

if __name__ == "__main__":
    MyMainApp().run()