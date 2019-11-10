'''Cinema module'''
from bs4 import BeautifulSoup
import requests

class CinemaParser:
    """Class about cinema"""
    def __init__(self, city):
        """init"""
        self.content = None
        self.city = city

    def extract_raw_content(self):
        """Cinema content"""
        main_page_url = "https://"+self.city+".subscity.ru"
        get_main_page_response = requests.get(main_page_url)
        self.content = BeautifulSoup(get_main_page_response.text, 'html.parser')

    def print_raw_content(self):
        """content printer"""
        print(self.content.prettify())
CINEMA_ABOUT_MOSCOW = CinemaParser('msk')
CINEMA_ABOUT_MOSCOW.extract_raw_content()
