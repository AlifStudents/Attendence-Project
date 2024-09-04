from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from pages.landing_page import LandingPage
from pages.admin_dashboard import AdminDashboard
from pages.mark_attendance import MarkAttendance
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('kv/landing_page.kv')
Builder.load_file('kv/admin_dashboard.kv')
Builder.load_file('kv/mark_attendance.kv')


class MyScreenManager(ScreenManager):
    """
    Custom ScreenManager for handling different screens in the app.
    """
    pass
class ImageButton(ButtonBehavior, Image):
    pass

class AttendanceApp(MDApp):
     def build(self):
           sm = MyScreenManager()
        #    self.theme_cls.primary_palette = "Blue"  
        #    self.theme_cls.theme_style = "Light" 
           sm.add_widget(LandingPage(name='landing_page'))
           sm.add_widget(AdminDashboard(name='admin_dashboard'))
           sm.add_widget(MarkAttendance(name='mark_attendance'))


           sm.current = 'landing_page'
           return sm
     
if __name__ == '__main__':
    AttendanceApp().run()