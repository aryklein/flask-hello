#/usr/bin/python

import unittest
from hello import app

class BasicTestCase(unittest.TestCase):
    def test_root_path(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!')

    def test_other_path(self):
        tester = app.test_client(self)
        response = tester.get('/other', content_type='html/text')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
