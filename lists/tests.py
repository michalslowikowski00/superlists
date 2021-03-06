from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from django.urls import resolve

from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Lista rzeczy do zrobienia</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        self.assertEqual(response.content.decode(), expected_html)

        # TODO: handle csrf token in tests

    def test_home_page_can_save_POST_request(self):
        request = HttpRequest()
        request.method = "POST"
        request.POST["item_text"] = "Nowy element listy"

        response = home_page(request)

        self.assertIn("Nowy element list", response.content.decode())

        expected_html = render_to_string("home.html", {"new_item_text": "Nowy element listy"})
        self.assertEqual(response.content.decode(), expected_html)
