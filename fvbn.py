from kivy.clock import Clock
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivy.lang import Builder

class Separator(Widget):
    sep_color = ListProperty([1,0,0,1])

class Test(MDApp):

    def add_seps(self, dt):
        tab_bar = self.root.ids.mdbn.ids.tab_bar
        for i in range(len(tab_bar.children)-1, 0, -1):
            tab_bar.add_widget(Separator(size_hint=(None, 1), width=4, sep_color=[0,1,0,1]), index=i)

    def build(self):
        self.theme_cls.primary_palette = "Gray"
        Clock.schedule_once(self.add_seps)
        return Builder.load_string(
            '''

<Separator>:
    canvas:
        Color:
            rgba: self.sep_color
        Rectangle:
            pos: self.pos
            size: self.size
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Bottom navigation'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        id: mdbn
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Python'
            icon: 'language-python'

            MDLabel:
                text: 'Python'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'C++'
            icon: 'language-cpp'

            MDLabel:
                text: 'I programming of C++'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'JS'
            icon: 'language-javascript'

            MDLabel:
                text: 'JS'
                halign: 'center'
'''
        )


Test().run()
