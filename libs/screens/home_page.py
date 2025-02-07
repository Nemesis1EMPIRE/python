from kivymd.uix.screen import MDScreen

import json

from libs.components.circular_avatar_image import CircularAvatarImage


class HomePage(MDScreen):
    profile_picture = "images/900.png" 
    other = "images/900 (2).png"

    def on_enter(self):
        self.list_stories()

    def list_stories(self):
        with open('data/stories.json') as f_obj:
            data = json.load(f_obj)
            for name in data:
                self.ids.stories.add_widget(CircularAvatarImage(
                    avatar = data[name]['avatar'],
                    name = name
                ))