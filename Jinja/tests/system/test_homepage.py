from tests.test_setup import BaseTest



class TestHome(BaseTest):
    def test_home_endpint(self):
        with self.app() as a:
            resp = a.get('/')

            self.assertEqual(resp.status_code, 200, 'Sprawdź czy flask dzała - \'flask run\' w konsoli')

    def test_home_contain(self):
        with self.app() as a:
            resp = a.get('/')
            self.assertEqual(resp.get_data(), b'This is index') # nie wiem skąd to "b"

    def test_sanity_check(self):
        with self.app() as a:
            resp = a.get('/gasvdsavdVvdsvasv')

            self.assertEqual(resp.status_code, 404, 'Sprawdź czy flask dzała - \'flask run\' w konsoli')
