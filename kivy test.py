
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Mywidget (Widget):
    pass

class MyApp(App):
    def buid(self):
        #return Label(text='hello world',font_size = 72,color = "red")
        return Mywidget()
if __name__=='__main__':
    MyApp().run()
