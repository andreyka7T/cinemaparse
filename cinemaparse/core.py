from bs4 import BeautifulSoup
import requests

class Aboutcinema:
    def __init__(self, city):
        elf.content = None
        self.city = city

    def extract_raw_content(self):
        main_page_url = "https://msk.subscity.ru"
        get_main_page_response = requests.get(main_page_url)
        self.content = BeautifulSoup(get_main_page_response.text, 'html.parser')

    def print_raw_content(self):
        return self.content.prettify()

    def get_films_list(self):
        list_films = list()
        all_films = self.content.find_all("div", class_="movie-plate")
        for one_film in all_films:
            list_films.append(film["attr-title"])
        return list_films[1:-1]
CINEMA_ABOUT_MOSCOW = Aboutcinema('msk')
CINEMA_ABOUT_MOSCOW.extract_raw_content()
CINEMA_ABOUT_MOSCOW.get_films_list()
