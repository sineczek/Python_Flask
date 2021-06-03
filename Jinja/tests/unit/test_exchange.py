import app
from tests.test_setup import BaseTest
from app import CantorOffer, Currency
from flask import render_template


class TestExchange(BaseTest):

    def test_repr(self):
        c = Currency('USD', 'Dollar', 'united-states.png')
        c1 = Currency('EUR', 'Euro', 'european-union.png')

        self.assertEqual(c.__repr__(), '<Currency {}>'.format(c.code))
        self.assertEqual(c1.__repr__(), '<Currency {}>'.format(c1.code))

    def test_method_get(self):
        # sprawdzenie czy render_template exchange.html
        pass

    def test_method_post(self):
        # sprawdzenie czy render_template exchange_results.html z wartościami
        pass

    def test_currency_code(self):
        c = Currency('USD', 'Dollar', 'united-states.png')
        c1 = Currency('EUR', 'Euro', 'european-union.png')

        self.assertEqual(c.code, 'USD', "Zły kod waluty")
        self.assertEqual(c1.code, 'EUR', "Zły kod waluty")

    def test_currency_name(self):
        c = Currency('USD', 'Dollar', 'united-states.png')
        c1 = Currency('EUR', 'Euro', 'european-union.png')

        self.assertEqual(c.name, 'Dollar', 'Zła nazwa waluty')
        self.assertEqual(c1.name, 'Euro', 'Zła nazwa waluty')

    def test_currency_flag(self):
        c = Currency('USD', 'Dollar', 'united-states.png')
        c1 = Currency('EUR', 'Euro', 'european-union.png')

        self.assertEqual(c.flag, 'united-states.png', 'Zła flaga waluty')
        self.assertEqual(c1.flag, 'european-union.png', 'Zła flaga waluty')

    def test_offer_loads(self):
        c = CantorOffer()

        self.assertEqual(0, len(c.currencies), "Lista powinna być pusta")

        c.load_offer()
        self.assertEqual(5, len(c.currencies), 'Na liście powinno być 5 pozycji')

    def test_currencies(self):
        c = CantorOffer()
        c.load_offer()
        self.assertEqual(5, len(c.currencies), 'Na liście powinno być 5 pozycji')

    def test_currency_exchange(self):
        pass


    def test_ammount_exchange(self):
        pass
