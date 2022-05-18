from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from Scripts import Twitter, Instagram, Stats

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        self.window.size_hint = (0.7, 0.9)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Image
        self.window.add_widget(Image(source="Img/NYCDOT.png"))

        #Label widget
        self.greeting = Label(text="Sentimental Analysis", font_size=30, color='#0c9b67')
        self.window.add_widget(self.greeting)
        # text input widget, range
        self.range = TextInput(multiline=False, padding_y=(10, 10), size_hint=(1, 0.5), hint_text='Days')
        self.window.add_widget(self.range)
   
        # button widget
        self.button = Button(text="Twitter", background_color = '#F8CB2E')
        self.button.bind(on_press = self.callback_twitter)
        self.window.add_widget(self.button)

        self.button2 = Button(text="Instagram", background_color = '#EE5007')
        self.button2.bind(on_press = self.callback_instagram)
        self.window.add_widget(self.button2)

        self.button2 = Button(text="Analyze Twitter", background_color = '#B22727')
        self.button2.bind(on_press = self.callback_ai_tw)
        self.window.add_widget(self.button2)

        self.button2 = Button(text="Analyze Instagram", background_color = '#B22727')
        self.button2.bind(on_press = self.callback_ai_ig)
        self.window.add_widget(self.button2)

        return self.window

    def callback_twitter(self, instance):
        Twitter.start(self.range.text)
        return self.window

    def callback_instagram(self, instance):
        Instagram.start(self.range.text)
        return self.window
    
    def callback_ai_tw(self, instnace):
        Stats.twitterStats()
        return self.window

    def callback_ai_ig(self, instnace):
        Stats.instagramStats()
        return self.window

if __name__ == "__main__":
    SayHello().run()