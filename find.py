import requests
import json


class FindMovie:
    def __init__(self, movie_title=None):
        self.movie_title = movie_title
        self.url_with_title = "https://imdb-api.com/en/API/Search/k_k684ggde/"
        self.url_with_id = "https://imdb-api.com/en/API/Title/k_k684ggde/"
        self.movie_data = None
        self.payload = {}
        self.headers = {}

    def set_movie_info(self):
        self.movie_data = self.__get_movies()

    def __get_movies(self):
        self.url_with_title += self.movie_title
        response = requests.request("GET", self.url_with_title, headers=self.headers, data=self.payload)
        return json.loads(response.text)

    def amount_of_searched_movies(self):
        return len(self.movie_data["results"])

    def get_searched_movie_result(self, film_index):
        searched_movie_info = []
        film = self.movie_data["results"][film_index]
        searched_movie_info.append(film["title"])
        print(film["title"])
        print(film["id"])
        print("--------------------------------------------------------------------------")
        searched_movie_info.append(film["image"])
        return searched_movie_info


class GreatestFilms:
    def __init__(self):
        self.link = "https://imdb-api.com/en/API/Top250Movies/k_k684ggde"
        self.data = self.__get_data()

    def __get_data(self):
        payload = {}
        headers = {}
        response = requests.request("GET", self.link, headers=headers, data=payload)
        return json.loads(response.text)

    def get_result(self, film_index):
        greatest_film_info = []
        film = self.data["items"][film_index]
        greatest_film_info.append(film["fullTitle"])
        greatest_film_info.append(film["image"])
        return greatest_film_info


class FilmInfo:
    def __init__(self, film_id):
        self.film_id = film_id
        self.url_with_id = "https://imdb-api.com/en/API/Title/k_k684ggde/" + self.film_id
        self.film_parameters = ["releaseDate", "runtimeStr", "plot", "awards", "directorList",
                                "writerList", "actorList", "genreList", "companyList", "countryList", "languageList",
                                "contentRating", "imDbRating", "imDbRatingVotes", "metacriticRating", "ratings",
                                "wikipedia", "posters", "images", "trailer", "boxOffice"]
        self.data = self.__film_data()

    def __film_data(self):
        payload = {}
        headers = {}
        response = requests.request("GET", self.url_with_id, headers=headers, data=payload)
        return json.loads(response.text)

    def film_useful_info(self):
        movie_information = {}
        for parameter in self.film_parameters:
            if self.data[parameter] == "":
                movie_information[parameter] = "Unknown"
            else:
                movie_information[parameter] = self.data[parameter]
        return movie_information
