from test_answers.unittest_8 import return_altos
import unittest

class TestNameAltos(unittest.TestCase):

    def test_name_is_altos(self):
        self.assertEqual(return_altos() ,'Altos')


if __name__ == '__main__':
    unittest.main()
