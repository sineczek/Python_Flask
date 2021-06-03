from tests.test_setup import BaseTest

class TestExchange(BaseTest):

    def test_exchange_endpoint(self):
        with self.app() as a:
            resp = a.get('/exchange')

            self.assertEqual(resp.status_code, 200, 'Sprawdź czy flask dzała - \'flask run\' w konsoli')

