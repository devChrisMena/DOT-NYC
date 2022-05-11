from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #Label widget
        self.greeting = Label(text="Sentimental Analysis")
        self.window.add_widget(self.greeting)

        '''
        #text input widget, username
        self.userName = TextInput(multiline=False, padding_y = (20,20), size_hint = (1, 0.5))
        self.window.add_widget(self.userName)

        # text input widget, password
        self.passWord = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 0.5))
        self.window.add_widget(self.passWord)

        # text input widget, range
        self.range = TextInput(multiline=False, padding_y=(20, 20), size_hint=(1, 0.5))
        self.window.add_widget(self.range)
        '''
        # button widget
        self.button = Button(text="Twitter", background_color = '#F8CB2E')
        self.button.bind(on_press = self.callback_twitter)
        self.window.add_widget(self.button)

        self.button2 = Button(text="Instagram", background_color = '#EE5007')
        self.button2.bind(on_press = self.callback_instagram)
        self.window.add_widget(self.button2)

        self.button2 = Button(text="AI", background_color = '#B22727')
        self.button2.bind(on_press = self.callback_instagram)
        self.window.add_widget(self.button2)

        return self.window

    def callback_twitter(self, instance):

        return self.window

    def callback_instagram(self, instance):

        return self.window

if __name__ == "__main__":
    SayHello().run()