import unittest

from index import temperature

class TestTemperatura(unittest.TestCase):

    def test_grados_centigrados(self):
        temp_k = 200

        temp_c = (temp_k - 27)

        self.assertEqual(temp_c, 173)
        
if __name__ == '__main__':
    unittest.main()