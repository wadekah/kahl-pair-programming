def convert(feet,inches): #takes in feet and inches values
    feet_to_inches = feet * 12 #convert to inches
    total = feet_to_inches + inches
    meters = total * 0.0254 #convert to meters
    return(meters)

import unittest

class TestConvert(unittest.TestCase):

    def test_convert_zero(self):
        result = convert(0, 0)
        self.assertEqual(result, 0)

    def test_convert_feet_only(self):
        result = convert(1, 0)
        self.assertAlmostEqual(result, 0.3048)

    def test_convert_inches_only(self):
        result = convert(0, 1)
        self.assertAlmostEqual(result, 0.0254)

    def test_convert_feet_and_inches(self):
        result = convert(1, 1)
        self.assertAlmostEqual(result, 0.3302)

if __name__ == '__main__':
    unittest.main()

# No defensive programming (assertations)
# Very light documentation