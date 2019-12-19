import unittest
from modules.db import save_routes, save_title, get_title, get_recomended_destinations
from mock import MagicMock


class DbTest(unittest.TestCase):

    def test_save_title(self):
        save_title('제목', '주소1')

    def test_get_title(self):
        save_title('제목', '주소2')
        self.assertEqual(get_title('주소2'), '제목')

    def test_save_routes(self):
        save_routes(['첫 번째 방문', '두 번째 방문'])

    def test_get_recomended_destinations(self):
        save_routes(['첫 번째 방문', '두 번째 방문', '세 번째 방문'])
        self.assertEqual(get_recomended_destinations(
            {'첫 번째 방문'}, ['첫 번째 방문']), ['두 번째 방문'])


if __name__ == '__main__':
    unittest.main()
