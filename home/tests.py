from django.test import TestCase
from django.urls import reverse

class CardDetailTests(TestCase):

    def test_valid_card_types_return_200(self):
        """Ruxsat berilgan karta turlari 200 OK qaytarishi kerak"""
        valid_cards = ['Visa', 'MasterCard', 'Humo', 'Uzcard']
        for card in valid_cards:
            # urls.py dagi name='card_detail' ga argument berib chaqiramiz
            url = reverse('home:card_detail', kwargs={'card_type': card})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_invalid_card_type_returns_404(self):
        """Tizimda yo'q karta turi (masalan, Azizbek) kiritilsa 404 qaytarishi kerak"""
        url = reverse('home:card_detail', kwargs={'card_type': 'Azizbek'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)