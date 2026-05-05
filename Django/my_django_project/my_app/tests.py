from django.test import TestCase
from django.urls import reverse

class NewsCategoryTests(TestCase):

    def test_technology_page(self):
        response = self.client.get(reverse('technology'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/technology.html')

    def test_politics_page(self):
        response = self.client.get(reverse('politics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/politics.html')

    def test_sports_page(self):
        response = self.client.get(reverse('sports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/sports.html')

    def test_entertainment_page(self):
        response = self.client.get(reverse('entertainment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/entertainment.html')