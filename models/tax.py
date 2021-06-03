

class TaxCalculation:

    def __init__(self, tax_bands):
        self.tax_bands = tax_bands

    def tax_calculation(self, income):
        """
        The function receives the income
        return the income tax
        """
        tax = 0
        for band in self.tax_bands:
            if income - band['bottom'] <= 0:
                break
            if income > band['top']:
                tax += band['rate'] * (band['top'] - band['bottom'])

            else:
                tax += band['rate'] * (income - band['bottom'])

        return tax
