import unittest
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_status_200(self):
        response = self.client.get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'ok': True, 'service': 'codex-workflow-test-lab'})

    def test_hello_status_200(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Hello from the test lab'})

    def test_unknown_route_404(self):
        response = self.client.get('/does-not-exist')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
