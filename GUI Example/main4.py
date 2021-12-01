from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from database import Database

class CreateAccountWindows(Screen):
    name = ObjectProperty(None)
    email =ObjectProperty(None)
    Password = ObjectProperty(None)
    test =ObjectProperty(None)

    def submit(self):
        if self.name.text != "" and self.email.text != "" and self.email.text.count("0") == 1 :
            if self.Password != "":
                db.add_user(self.email.text,self.password.text,self.name.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text=""
        self.password.text = ""
        self.name.text=""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text,self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            # am.current = "main"
        # else:
        #     invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text=""
        self.password.text=""

class MainWindow(Screen):
    n=ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current=""

    def logOut(self):
        sm.current ="login"

    def on_enter(self, *args):
        password,name,created = db.get_user(self.current)
        self.n.text = "Account Name :"+ name
        self.email.text="Email:"+self.current
        self.created.text = "Created On :" + created

class WindowManager(ScreenManager):
    pass

def invalid_login():
    pop = Popup(title = 'Invalid Login',
                content=Label(text='Invalid username or password'),
                size_hint=(None,None),size=(400,400))

    pop.open()

def invalidForm():
        pop = Popup(title='Invalid Form',
                    content=Label (text='please fill the inputs of with valid information'),
                    size_hint=(None,None),size=(400,400))
        pop.open()

# kv.Builder.load_file("my4.kv")

sm=WindowManager()
db=Database("users.txt")

# screens = [LoginWindow(name="Login"),CreateAccountWindows(name="create"),MainWindow(name='main')]
# for screens in screens:
#      sm=add_widget(screens)

sm.current = "login"

class MyMainApp(App):
    def build(self):
        return sm


if __name__=="__main__":
    MyMainApp().run()