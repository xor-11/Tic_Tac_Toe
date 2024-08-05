from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp




class Game(GridLayout):

    a = BooleanProperty(True)
    check = StringProperty("")
    player = StringProperty("X starts")

    def torf(self):
        if self.a == True:
            self.player = "O"
        elif self.a == False:
            self.player = "X"
        elif self.a == "" :
            self.player = ""



    k = ["0","0","0","0","0","0","0","0","0","0"]


    def playername(self,widget):
        if self.a == True:
            self.player == widget.text


    def restart(self):
        self.check = ""
        self.player = "X starts"
        self.k = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        self.a = True
        self.ids.b1.disabled = False
        self.ids.b2.disabled = False
        self.ids.b3.disabled = False
        self.ids.b4.disabled = False
        self.ids.b5.disabled = False
        self.ids.b6.disabled = False
        self.ids.b7.disabled = False
        self.ids.b8.disabled = False
        self.ids.b9.disabled = False
        self.ids.b1.text = ""
        self.ids.b2.text = ""
        self.ids.b3.text = ""
        self.ids.b4.text = ""
        self.ids.b5.text = ""
        self.ids.b6.text = ""
        self.ids.b7.text = ""
        self.ids.b8.text = ""
        self.ids.b9.text = ""



    def disableall(self):
        self.ids.b1.disabled = True
        self.ids.b2.disabled = True
        self.ids.b3.disabled = True
        self.ids.b4.disabled = True
        self.ids.b5.disabled = True
        self.ids.b6.disabled = True
        self.ids.b7.disabled = True
        self.ids.b8.disabled = True
        self.ids.b9.disabled = True


    def checkwin(self):
        if (self.k[1] + self.k[2] + self.k[3]) == "OOO" or  (self.k[4] + self.k[5] + self.k[6]) == "OOO"  or (self.k[7] + self.k[8] + self.k[9]) == "OOO"  or (self.k[1] + self.k[4] + self.k[7]) == "OOO"  or (self.k[2] + self.k[5] + self.k[8]) == "OOO" or  (self.k[3] + self.k[6] + self.k[9]) == "OOO"  or (self.k[1] + self.k[5] + self.k[9]) == "OOO"  or (self.k[3] + self.k[5] + self.k[7]) == "OOO" :
            self.disableall()
            self.a == False
            self.torf()
            self.popup3()
            self.check = " Won"
        elif  (self.k[1] +self.k[2] + self.k[3]) == "XXX" or (self.k[4] + self.k[5] + self.k[6]) == "XXX" or (self.k[7] + self.k[8] + self.k[9]) == "XXX" or (self.k[1] + self.k[4] + self.k[7]) == "XXX" or (self.k[2] + self.k[5] + self.k[8]) == "XXX" or (self.k[3] + self.k[6] + self.k[9]) == "XXX" or (self.k[1] + self.k[5] + self.k[9]) == "XXX" or (self.k[3] + self.k[5] + self.k[7]) == "XXX" :
            self.disableall()
            self.a == False
            self.torf()
            self.popup2()
            self.check = " Won"
            #print(True)
        elif self.k.count("X") == 5:
            self.a = ""
            self.check = "Draw"
            self.popup1()
            self.torf()
           # print(False)
        else :
            self.check = "'s turn"

    def turn1(self,b):
        if self.a == True:
            self.k[int(1)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1,0,0,1)
            b.text = "x"
            self.torf()
            b.disabled = True

            self.a = False

        else:
            self.k[int(1)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
        #print(self.k)
    def turn2(self,b):
        if self.a == True:
            self.k[int(2)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(2)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn3(self,b):
        if self.a == True:
            self.k[int(3)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(3)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn4(self,b):
        if self.a == True:
            self.k[int(4)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(4)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn5(self,b):
        if self.a == True:
            self.k[int(5)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(5)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn6(self,b):
        if self.a == True:
            self.k[int(6)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(6)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn7(self,b):
        if self.a == True:
            self.k[int(7)] = "X"
            b.font_size = "50dp"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(7)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn8(self,b):
        if self.a == True:
            self.k[int(8)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(8)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def turn9(self,b):
        if self.a == True:
            self.k[int(9)] = "X"
            b.font_name = "fonts/Queensides-3z7Ey.ttf"
            b.font_size = "50dp"
            b.disabled_color = (1, 0, 0, 1)
            b.text = "x"
            self.torf()
            b.disabled = True
            self.a = False

        else:
            self.k[int(9)] = "O"
            b.font_name = "fonts/Montserrat-Light.ttf"
            b.font_size = "40dp"
            b.disabled_color = (0,1,0,1)
            b.text = "O"
            self.torf()

            b.disabled = True
            self.a = True
        self.checkwin()
    def popup1(self):
        popup = Popup(title = "",separator_height =  0, content=Label(text='Draw', font_size = "20dp",font_name = "fonts/Montserrat-Bold.ttf"),size_hint = (0.5,0.5))
        popup.open()
    def popup2(self):
        popup = Popup(title='',separator_height =  0, content=Label(text='X  won', font_size = "20dp",font_name = "fonts/Montserrat-Bold.ttf"),size_hint = (0.5,0.5))
        popup.open()
    def popup3(self):
        popup = Popup(title='',separator_height =  0, content=Label(text='O won', font_size = "20dp",font_name = "fonts/Montserrat-Bold.ttf"),size_hint = (0.5,0.5))
        popup.open()







class agameApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Game()





agameApp().run()