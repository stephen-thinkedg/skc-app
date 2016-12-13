import unittest
from adder import Adder


class TestBob(unittest.TestCase):

    def test_create_adder(self):
        adder = Adder()

    def test_increment(self):
        adder = Adder()
        self.assertEqual(adder.increment(3), 4)

         
if __name__=='__main__':
    unittest.main(verbosity=3)
