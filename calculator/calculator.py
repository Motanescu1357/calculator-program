from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

KV = '''
Screen:
    MDLabel:
        id: calculator_text
        text:  ""
        pos_hint: {"center_x":0.9, "center_y":0.9}
    Button:
        text: "0"
        size_hint: 0.2, 0.2
        pos_hint: {"center_x":0.1, "center_y":0.7}
        on_release: app.nr_0()
    Button:
        text: "1"
        size_hint: 0.2, 0.2
        pos_hint: {"center_x":0.3, "center_y":0.7}
        on_release: app.nr_1()
    Button:
        text: "2"
        pos_hint: {"center_x":0.5, "center_y":0.7}
        size_hint: 0.2, 0.2
        on_release: app.nr_2()
    Button:
        text: "3"
        pos_hint: {"center_x":0.1, "center_y":0.5}
        size_hint: 0.2, 0.2
        on_release: app.nr_3()
    Button:
        text: "4"
        pos_hint: {"center_x":0.3, "center_y":0.5}
        size_hint: 0.2, 0.2
        on_release: app.nr_4()
    Button:
        text: "5"
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size_hint: 0.2, 0.2
        on_release: app.nr_5()
    Button:
        text: "6"
        pos_hint: {"center_x":0.1, "center_y":0.3}
        size_hint: 0.2, 0.2
        on_release: app.nr_6()
    Button:
        text: "7"
        pos_hint: {"center_x":0.3, "center_y":0.3}
        size_hint: 0.2, 0.2
        on_release: app.nr_7()
    Button:
        text: "8"
        pos_hint: {"center_x":0.3, "center_y":0.3}
        size_hint: 0.2, 0.2
        on_release: app.nr_8()
    Button:
        text: "9"
        pos_hint: {"center_x":0.3, "center_y":0.3}
        size_hint: 0.2, 0.2
        on_release: app.nr_9()    
    Button:
        text: "/"
        pos_hint: {"center_x":0.7, "center_y":0.3}
        size_hint: 0.01, 0.01
        on_release: app.divide()
    Button:
        text: "*"
        pos_hint: {"center_x":0.73, "center_y":0.3}
        size_hint: 0.01, 0.01
        on_release: app.multiply()
    Button:
        text: "^"
        pos_hint: {"center_x":0.73, "center_y":0.26}
        size_hint: 0.01, 0.01
        on_release: app.pow()
    Button:
        text: "-"
        pos_hint: {"center_x":0.70, "center_y":0.26}
        size_hint: 0.01, 0.01
        on_release: app.minus()
    Button:
        text: "+"
        pos_hint: {"center_x":0.715, "center_y":0.23}
        size_hint: 0.01, 0.01
        on_release: app.plus()
    MDIconButton:
        icon: "backspace"
        pos_hint: {"center_x":0.9, "center_y":0.5}
        on_release: app.backspace()
    MDIconButton:
        icon: "equal"
        pos_hint: {"center_x":0.9, "center_y":0.3}
        on_release: app.equal()
    Button:
        text: "AC"
        pos_hint: {"center_x":0.1, "center_y":0.846}
        size_hint: 0.1, 0.1
        on_release: app.clear()
'''


class Calculator(MDApp, BoxLayout, Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.calculator_text = ""
        self.ui = Builder.load_string(KV)
        self.eui = BoxLayout()
        self.icon = "images/icon.png"

    def build(self):
        screen = Screen()
        screen.add_widget(self.ui)
        return screen

    def nr_0(self):
        self.calculator_text = self.calculator_text + "0"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_1(self):
        self.calculator_text = self.calculator_text + "1"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_2(self):
        self.calculator_text = self.calculator_text + "2"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_3(self):
        self.calculator_text = self.calculator_text + "3"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_4(self):
        self.calculator_text = self.calculator_text + "4"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_5(self):
        self.calculator_text = self.calculator_text + "5"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_6(self):
        self.calculator_text = self.calculator_text + "6"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_7(self):
        self.calculator_text = self.calculator_text + "7"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_8(self):
        self.calculator_text = self.calculator_text + "8"
        self.ui.ids.calculator_text.text = self.calculator_text

    def nr_9(self):
        self.calculator_text = self.calculator_text + "9"
        self.ui.ids.calculator_text.text = self.calculator_text

    def backspace(self):
        self.calculator_text = self.calculator_text[:-1]
        self.ui.ids.calculator_text.text = self.ui.ids.calculator_text.text[:-1]

    def equal(self):
        self.ui.ids.calculator_text.text = str(eval(self.calculator_text))
        self.calculator_text = str(eval(self.calculator_text))

    def divide(self):
        self.calculator_text = self.calculator_text + "/"
        self.ui.ids.calculator_text.text = self.calculator_text

    def multiply(self):
        self.calculator_text = self.calculator_text + "*"
        self.ui.ids.calculator_text.text = self.calculator_text

    def pow(self):
        self.calculator_text = self.calculator_text + "**"
        self.ui.ids.calculator_text.text = self.ui.ids.calculator_text.text + "**"

    def minus(self):
        self.calculator_text = self.calculator_text + "-"
        self.ui.ids.calculator_text.text = self.calculator_text

    def plus(self):
        self.calculator_text = self.calculator_text + "+"
        self.ui.ids.calculator_text.text = self.calculator_text

    def clear(self):
        self.calculator_text = ""
        self.ui.ids.calculator_text.text = self.calculator_text

Calculator().run()
