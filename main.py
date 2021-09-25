from kivy.app import App
from kivy.lang.builder import Builder
from random import randint

codeaj='''

BoxLayout:
    orientation : "vertical" 
    Button : 
        text : "Dice" 
        pos_hint : {"center_x":.5,"center_y" : .8}
        on_press : app.generate()
        font_size : 30
        
    Label : 
        id : random 
        text : "codeAj" 
        pos_hint : {"center_x":.5,"center_y" : .5}
        font_size : 30

'''

class kivyApp(App):
    def build(self):
        self.title = "Ludo dice"
        return Builder.load_string(codeaj)


    def generate(self):
        self.root.ids.random.text = str(randint(1,6))
        self.root.ids.random.font_size = 100

if __name__ == '__main__':
    kivyApp().run()