import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class MyApp(App):
    def build(self):
        return Camera()

if __name__ == '__main__':
    MyApp().run()
