from tests.test_setup import BaseTest

class TestHotelForm(BaseTest):
    def test_hotel_form_endpoint(self):
        with self.app() as a:
            resp = a.get('/hotel_form')

            self.assertEqual(resp.status_code, 200, 'Sprawdź czy flask dzała - \'flask run\' w konsoli')

