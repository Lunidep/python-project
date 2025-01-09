from django.test import TestCase
from django.urls import reverse


class PingPongTests(TestCase):
    def test_ping(self):
        response = self.client.get(reverse('ping'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'message': 'pong'})

    def test_pong(self):
        response = self.client.get(reverse('pong'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'message': 'ping'})
