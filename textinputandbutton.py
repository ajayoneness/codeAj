import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGradeLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGradeLayout,self).__init__(**kwargs)
        self.cols=2
        #name:
        self.add_widget(Label(text='name : '))
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)
        #movies:
        self.add_widget(Label(text='movies : '))
        self.movies = TextInput(multiline=False)
        self.add_widget(self.movies)
        #ratig:
        self.add_widget(Label(text='rating : '))
        self.rating = TextInput(multiline=False)
        self.add_widget(self.rating)
        
        #button :
        self.submit=Button(text="submit",font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name=self.name.text
        movies=self.movies.text
        rating=self.rating.txt
        print(f"hello {name}, you love {movies}, because the rating of this moves is {rating}")

        self.add_widget(Label(text=f"hello {name}, you love {movies}, because the rating of this moves is {rating}"))

class MyApp(App):
    def build(self):
        return MyGradeLayout()


if __name__=='__main__':
    MyApp().run()
