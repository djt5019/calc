from unittest import TestCase, main

import calc

class CalcTestCase(TestCase):
    def test_calc(self):
        self.assertEquals(calc.sales_discount(1, 1, "CA"), 1.08)

if __name__ == '__main__':
    main()

