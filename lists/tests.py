from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    # def home_page(request):
    #     pass

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Lista rzeczy do zrobienia</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
