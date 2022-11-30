import unittest
import functions


class TestFormula(unittest.TestCase):

    def test_width_from_height(self):
        return


""" reference of unit testing

    delta_value = 0.001

    def test_add(self):
        self.assertEqual(formula.add(10, 5), 15)
        self.assertEqual(formula.add(-1, 1), 0)
        self.assertEqual(formula.add(-1, -1), -2)
        self.assertEqual(formula.add(1, -1), 0)

        self.assertRaises(ValueError, formula.add, 'abc', 1)
        self.assertRaises(ValueError, formula.add, 1, 'abc')
        self.assertRaises(ValueError, formula.add, 'abc', 'def')

        self.assertAlmostEqual(formula.add(1.1, 1.1), 2.2, delta=self.delta_value)
        self.assertAlmostEqual(formula.add(1.2, -1.1), 0.1, delta=self.delta_value)
"""
if __name__ == '__main__':
    unittest.main()