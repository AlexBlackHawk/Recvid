from kivy.lang import Builder
from kivy.uix.camera import Camera
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.hero import MDHeroFrom
from kivymd.uix.imagelist import MDSmartTile
from kivymd.uix.screen import MDScreen

from news import MovieNews

import imdb

from find import GreatestFilms, FindMovie

from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import AsyncImage
from kivy.clock import Clock

from kivy.properties import StringProperty, ObjectProperty


class MovieItem(MDHeroFrom):
    # film_title = StringProperty()
    # film_director = StringProperty()
    # film_year = StringProperty()
    # film_poster = StringProperty()
    manager = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.tile.ids.image.ripple_duration_in_fast = 0.05

    def on_transform_in(self, instance_hero_widget, duration):
        Animation(
            radius=[0, 0, 0, 0],
            box_radius=[0, 0, 0, 0],
            duration=duration,
        ).start(instance_hero_widget)

    def on_transform_out(self, instance_hero_widget, duration):
        Animation(
            radius=[24, 24, 24, 24],
            box_radius=[0, 0, 24, 24],
            duration=duration,
        ).start(instance_hero_widget)

    def on_release(self):
        def switch_screen(*args):
            self.manager.current_hero = self.film_title
            self.manager.current = "Movie info"

        Clock.schedule_once(switch_screen, 0.2)


class LoadMoreGreatestFilms(MDFillRoundFlatIconButton):
    pass


class LoadMoreFoundFilms(MDFillRoundFlatIconButton):
    pass


class ImageTitleScreen(MDScreen):
    pass


class MovieInfoBox(MDBoxLayout):
    pass


class ActorListItem(MDSmartTile):
    pass


class PosterImageListItem(MDSmartTile):
    pass


class RecvidApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.moviesDB = imdb.IMDb()
        self.gm = GreatestFilms()
        self.greatest_film_start = 0
        self.greatest_film_end = 10
        self.searched_film_start = 0
        self.searched_film_end = 10
        self.lmgf = LoadMoreGreatestFilms()
        self.lmff = LoadMoreFoundFilms()
        self.FM = FindMovie()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.root = Builder.load_file("interface.kv")
        return self.root

    def on_start(self):
        self.add_news()
        self.logic_for_adding_films()

    def add_news(self):
        news = MovieNews()
        for title, image, text in zip(news.titles(), news.images(), news.texts()):
            card = MDCard(orientation="vertical", size_hint=(.5, .95), pos_hint={"center_x": .5, "center_y": .5},
                          radius=20)

            img = AsyncImage(
                source=image,
                pos_hint={'center_x': 0.5, 'center_y': 0.6},
                size_hint=(.5, .5),
                allow_stretch=True,
                keep_ratio=True
            )
            labels_bl = MDBoxLayout(orientation="vertical", adaptive_height=True)

            ttl = MDLabel(text=title, font_style="H4", size_hint_y=.5, adaptive_height=True)
            txt = MDLabel(text=text, font_style="H6", size_hint_y=.5, adaptive_height=True)

            card.add_widget(img)
            card.add_widget(labels_bl)

            labels_bl.add_widget(ttl)
            labels_bl.add_widget(txt)

            self.root.ids.news_carousel.add_widget(card)

    def add_greatest_films(self):
        for i in range(self.greatest_film_start, self.greatest_film_end):
            movie = self.gm.get_result(i)
            mi = MovieItem(film_title=movie[0], film_poster=movie[3])
            self.root.ids.box.add_widget(mi)

        if self.greatest_film_start == 250:
            self.root.ids.screen_3.remove_widget(self.lmgf)
        else:
            self.greatest_film_start += 10
            self.greatest_film_end += 10

    def logic_for_adding_films(self, text="", search=False):
        if search:
            self.FM.movie_title = text
            self.FM.set_movie_info()
            self.add_searched_films()
        else:
            self.greatest_film_start = 0
            self.greatest_film_end = 10
            self.add_greatest_films()

    def add_searched_films(self):
        for i in range(self.searched_film_start, self.searched_film_end):
            movie = self.FM.get_searched_movie_result(i)
            mi = MovieItem(film_title=movie[0], film_poster=movie[3])
            self.root.ids.box.add_widget(mi)

        if self.searched_film_start == self.FM.amount_of_searched_movies():
            self.root.ids.screen_3.remove_widget(self.lmff)
        else:
            self.searched_film_start += 10
            self.searched_film_end += 10

    def open_camera(self):
        cam = Camera(play=True)
        camera_screen = MDScreen


if __name__ == "__main__":
    RecvidApp().run()
