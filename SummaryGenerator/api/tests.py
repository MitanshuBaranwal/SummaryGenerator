from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class APITests(APITestCase):
    def test_generate_summary(self):
        url = reverse('generate-summary')
        data = {'text': 'This is a Sample text for testing.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_generate_bullet_points(self):
        url = reverse('generate-bullet-points')
        data = {'text': 'This is a Sample text for testing.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)