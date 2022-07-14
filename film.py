from kivy.core import window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField

Window.size = (480, 800)


class INSPECTOR(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        screen = Builder.load_file('layout.kv')
        # input = self.root.ids.get_barcode.string
        return screen

    def on_start(self):
        self.barcode = self.root.ids.barcode.text
        self.list = []

    def on_enter(self):
        self.list.append(self.barcode)
        for i in range(self.list):
            self.item = OneLineListItem(text=f"{self.list[i]}")
            self.root.ids.contaniner.add_widget(self.item)


if __name__ == "__main__":
    INSPECTOR().run()
