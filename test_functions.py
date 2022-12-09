import unittest
import functions


class TestFormula(unittest.TestCase):
    delta_value = 0.001

    def test_width_from_height(self):
        
        self.assertEqual(functions.width_from_height(1080, 16, 9), 1920)
        self.assertEqual(functions.width_from_height(-900, 16, 9), -1600)
        self.assertEqual(functions.width_from_height(-480, 4, -3), 640)
        self.assertEqual(functions.width_from_height(720, -4, -3), 960)

        self.assertRaises(TypeError, functions.width_from_height, 'abc', 1, 1)
        self.assertRaises(TypeError, functions.width_from_height, 1, 'abc', 1)
        self.assertRaises(TypeError, functions.width_from_height, 'abc', 'def', 1)

        self.assertAlmostEqual(functions.width_from_height(100, 16, 9), 177.7777, delta=self.delta_value)
        self.assertAlmostEqual(functions.width_from_height(100, -4, 3), -133.3333, delta=self.delta_value)

    def test_height_from_width(self):

        self.assertEqual(functions.height_from_width(1920, 16, 9), 1080)
        self.assertEqual(functions.height_from_width(-1600, 16, 9), -900)
        self.assertEqual(functions.height_from_width(-640, 4, -3), 480)
        self.assertEqual(functions.height_from_width(960, -4, -3), 720)

        self.assertRaises(TypeError, functions.height_from_width, 'abc', 1, 1)
        self.assertRaises(TypeError, functions.height_from_width, 1, 'abc', 1)
        self.assertRaises(TypeError, functions.height_from_width, 'abc', 'def', 1)

        self.assertAlmostEqual(functions.height_from_width(100, 16, 9), 56.25, delta=self.delta_value)
        self.assertAlmostEqual(functions.height_from_width(100, -11, 9), -81.8181, delta=self.delta_value)


if __name__ == '__main__':
    unittest.main()
