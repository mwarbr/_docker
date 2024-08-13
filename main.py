from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDToolbar:
        title: "KivyMD Application"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10

    Widget:
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
