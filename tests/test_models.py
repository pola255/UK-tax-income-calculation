import unittest
from models.tax import TaxCalculation

tax_bands = [
            {
                "rate": 0,
                "top": 1000,
                "bottom": 0
            },
            {
                "rate": 0.1,
                "top": 2000,
                "bottom": 1000
            },
            {
                "rate": 0.2,
                "top": 3000,
                "bottom": 2000
            },
            {
                "rate": 0.3,
                "bottom": 3000
            }
        ]

tax_calculation = TaxCalculation(tax_bands)


class ModelTest(unittest.TestCase):

    def test_tax_calculation_band_1(self):
        tax = tax_calculation.tax_calculation(800)
        self.assertEqual(tax, 0)
        tax = tax_calculation.tax_calculation(1000)
        self.assertEqual(tax, 0)

    def test_tax_calculation_band_2(self):
        tax = tax_calculation.tax_calculation(1500)
        self.assertEqual(tax, 50)
        tax = tax_calculation.tax_calculation(2000)
        self.assertEqual(tax, 100)

    def test_tax_calculation_band_3(self):
        tax = tax_calculation.tax_calculation(2500)
        self.assertEqual(tax, 200)
        tax = tax_calculation.tax_calculation(3000)
        self.assertEqual(tax, 300)

    def test_tax_calculation_more_than_last_band(self):
        tax = tax_calculation.tax_calculation(3500)
        self.assertEqual(tax, 450)


if __name__ == '__main__':
    unittest.main()
