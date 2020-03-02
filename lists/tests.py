from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):

	def test_uses_home_teplate(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'home.html')

	def test_can_save_a_POST_request(self):
		response = self.client.post('/', data={'item_text': 'A new list item'})
		self.assertIn('A new list item', response.content.decode())
		self.assertTemplateUsed(response, 'home.html')

	def test_home_page_return_correct_html(self):
		response = self.client.get('/')

		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', html)
		self.assertTrue(html.strip().endswith('</html>'))

		self.assertTemplateUsed(response, 'home.html')


