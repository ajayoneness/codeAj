from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.material_resources import dp
from kivymd.uix.bottomnavigation import MDBottomNavigationItem, MDBottomNavigation
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.toolbar import MDToolbar
import pytube
from time import sleep
from utube import helper
from threading import *

Window.size = (350, 600)
helper = '''



BoxLayout:
    orientation:'vertical'

    MDToolbar:
        id : toptoolbar
        title: 'Utub'
        md_bg_color: .1, .1, .1, 1
        specific_text_color: 1, 1, 1, 1
        right_action_items : [["theme-light-dark",lambda x : app.lightdarkthem()]]

    MDBottomNavigation:
        id:buttontoolbar
        panel_color: .1, .1, .1, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            icon: 'youtube'
            text: 'Youtube'


            Image :
                id  : img
                source : "youtube.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint : .9,.9

            MDLabel:
                id : label
                text: 'Youtube'
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .6}
                theme_text_color : "Custom"
                color : 1,1,1,1

            MDTextField :
                id : textfild
                hint_text : "Enter youtube link "
                helper_text:'Hint : youtube.com/codeaj'
                helper_text_mode : "on_focus"
                icon_right : "youtube"
                icon_right_color : app.theme_cls.primary_color
                pos_hint : {'center_x': 0.5, 'center_y': 0.4}
                required: True
                size_hint_x: None
                width : 300


            MDRaisedButton:
                id : recbutton
                text : "convert"
                pos_hint: {"center_x": .5, "center_y": .3}
                on_press : app.okey()
                #on_release : app.release()
                #disabled : True
                theme_text_color : "Custom"
                color : 1,.5,1,1

            MDSpinner:
                id : aj 
                size_hint: None, None
                size: dp(46), dp(46)
                pos_hint: {'center_x': .5, 'center_y': .2}
                active: False

            #MDDropDownItem:
             #   id: drop_item
              #  pos_hint: {'center_x': .5, 'center_y': .1}
               # text: 'Item 0'
                #on_release: app.         


#------------------------------------------------------------------------------------------------------------->>>>>>>>

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Facebook'
            icon: 'facebook'


            Image :
                source : "fb.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint : .7,.7

            MDLabel:
                text: 'Facebook'

                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .6}
                

            MDTextField :
                hint_text : "Enter facebook link "
                helper_text:'Hint : fb.com/codeaj'
                #helper_text_mode : "on_focus"
                icon_right : "facebook"
                icon_right_color : app.theme_cls.primary_color
                pos_hint : {'center_x': 0.5, 'center_y': 0.4}
                size_hint_x: None
                width : 300


            MDRectangleFlatButton:
                text : "convert"
                pos_hint: {"center_x": .5, "center_y": .3}



        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Instagram'
            icon: 'instagram'


            Image :
                source : "insta.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint : .5,.5

            MDLabel:
                text: 'Instagram'

                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .6}

            MDTextField :
                hint_text : "Enter instagram link "
                helper_text:'Hint : instagram.com/code_ajay'
                helper_text_mode : "on_focus"
                icon_right : "instagram"
                icon_right_color : app.theme_cls.primary_color
                pos_hint : {'center_x': 0.5, 'center_y': 0.4}
                size_hint_x: None
                width : 300


            MDRectangleFlatButton:
                text : "convert"
                pos_hint: {"center_x": .5, "center_y": .3}

# About us

        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'AboutUs'
            icon: 'account'


            Image :
                source : "codeaj.png"
                pos_hint: {"center_x": .5, "center_y": .8}
                size_hint : .5,.5

            MDLabel:
                text: "codeAj"
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .6}







'''




class MainMenu(Screen):
    pass
class DownloadMenu(Screen):
    pass
sm=ScreenManager()
sm.add_widget(MainMenu(name='main_menu'))
sm.add_widget(DownloadMenu(name='download_menu'))


class Test(MDApp):

    def build(self):

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "LightBlue"
        self.link = Builder.load_string(helper)
        return self.link






    def close_dilog(self, obj):
        self.dilog.dismiss()
        self.root.ids.aj.active = False

    def youtube_download(self,obj):
        import plyer

        plyer.notification.notify(title=f'{self.vtitle[0:63]}',
                                  message="Downloading...")
        self.dilog.dismiss()
        self.ut.streams[0].download()


    def release(self):
        if "youtube.com" in self.root.ids.textfild.text :
            try:
                close = MDRectangleFlatButton(text="Close", on_release=self.close_dilog)
                more = MDRectangleFlatButton(text="Download", on_press=self.youtube_download)
                self.ut = pytube.YouTube(self.root.ids.textfild.text)
                self.vtitle = f"{self.ut.title}"
                self.dilog = MDDialog(title=f"{self.vtitle}",
                                  text=f"Author : {self.ut.author}\nRating : {self.ut.rating}\nViews : {self.ut.views}\nPublish Date : {self.ut.publish_date}\nLength : {int(self.ut.length/60)} minute",
                                  size_hint=(0.9, 1),
                                  buttons=[close, more],
                              )
                sleep(1)
                self.dilog.open()
                sleep(1)
            except :
                self.root.ids.label.text="No Network connecrion"
                self.root.ids.label.color = 0, 0, 1, 1
                self.root.ids.aj.active = False
        else :
            self.root.ids.label.text = "Invalid Link"
            self.root.ids.label.color=1,0,0,1
            self.root.ids.aj.active = False

    def press(self):
        self.root.ids.aj.active = True
        # self.root.ids.label.=
        sleep(1)

    def lightdarkthem(self):

        if self.theme_cls.theme_style =="Dark":
            self.theme_cls.theme_style="Light"
            self.root.ids.toptoolbar.md_bg_color=.5,.5,.5,1
            self.root.ids.buttontoolbar.panel_color = .5, .5, .5, 1
            self.root.ids.toptoolbar.specific_text_color=0,0,0,1
        else:
            self.theme_cls.theme_style="Dark"
            self.root.ids.toptoolbar.md_bg_color = .1, .1, .1, 1
            self.root.ids.buttontoolbar.panel_color = .1, .1, .1, 1
            self.root.ids.toptoolbar.specific_text_color = 1, 1, 1, 1


    def okey(self):
        t1 = Thread(target=self.press)
        t2 = Thread(target=self.release)
        t1.start()
        sleep(0.2)
        t2.start()

    #def set_item(self, text_item):
     #   self.root.ids.drop_item.set_item(text_item)
      #  self.menu.dismiss()


Test().run()
