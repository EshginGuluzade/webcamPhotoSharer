from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time
import webbrowser

from filesharer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.opacity = 1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.opacity = 0
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.file_path = "files/" + current_time + ".png"
        self.ids.camera.export_to_png(self.file_path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.file_path


class ImageScreen(Screen):
    link_message = "Please create a link first"
    def create_link(self):
        filePath = App.get_running_app().root.ids.camera_screen.file_path
        filesharer = FileSharer(file_path=filePath)
        self.url = filesharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
