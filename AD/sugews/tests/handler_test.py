import unittest
from handler.index import Handler
from mock import MagicMock


class HandlerTest(unittest.TestCase):

    def setUp(self):
        self.handler = Handler(None)
        self.handler.search = MagicMock(return_value=None)

    def test_save_routes(self):
        self.handler.routes = ['1', '2']
        self.handler.save_routes()
        self.assertEqual(len(self.handler.routes), 1)

    def test_set_category(self):
        self.handler.set_category('카테고리')
        self.assertEqual(self.handler.category, '카테고리')


if __name__ == '__main__':
    unittest.main()
