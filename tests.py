from unittest import TestCase, main

import calc

class CalcTestCase(TestCase):
    def test_calc(self):
        tests = [
            (1, 1, "CA", 1.04),
            (1, 1, "ca", 1.04),
            (1, 1, "cA", 1.04),
            (1, 1, "NV", 1.04),
            (1, 1, "UT", 1.02),
            (1, 1, "TX", .97),
        ]
        for test in tests:
            qty, unit_price, state, expected = test
            actual = calc.sales_discount(qty, unit_price, state)
            self.assertEquals(actual, expected, (test, actual))

if __name__ == '__main__':
    main()

