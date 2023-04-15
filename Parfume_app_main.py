import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from ross_datagetter import ross_datagetter
from douglas_datagetter import douglas_datagetter
from empik_datagetter import empik_datagetter
from hebe_datagetter import hebe_datagetter
from testy_automatyzacja import notino_datagetter
from superph_datagetter import superpharm_datagetter
from smyk_datagetter import smyk_datagetter




class MainWindow(Screen):
    ross_url=ObjectProperty(None)
    notino_url=ObjectProperty(None)
    empik_url=ObjectProperty(None)
    hebe_url=ObjectProperty(None)
    douglas_url=ObjectProperty(None)
    smyk_url=ObjectProperty(None)
    superph_url=ObjectProperty(None)

    def on_press(self):
        ross_datagetter(self.ross_url.text,self)
        self.ross_url.text=''
        notino_datagetter(self.notino_url.text,self)
        self.notino_url.text=''
        smyk_datagetter(self.smyk_url.text,self)
        self.smyk_url.text=''
        superpharm_datagetter(self.superph_url.text,self)
        self.superph_url.text=''
        douglas_datagetter(self.douglas_url.text,self)
        self.douglas_url.text=''
        empik_datagetter(self.empik_url.text,self)
        self.empik_url.text=''
        hebe_datagetter(self.hebe_url.text,self)
        self.hebe_url.text=''



class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('parfume_app.kv')



class MyApp(App):
    def build(self):
        return kv





if __name__=='__main__':
    MyApp().run()

