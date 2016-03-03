from unittest import TestCase, main

import calc

class CalcTestCase(TestCase):
    def test_calc(self):
        tests = [
            (1, 1, "CA", 1.04), # variations on california casing
            (1, 1, "ca", 1.04),
            (1, 1, "cA", 1.04),
            (1, 1, "NV", 1.04), # test a couple non-CA states
            (1, 1, "UT", 1.02),
            (1, 1, "TX", .97),  # test a state without sales tax
            (2, 500, "TX", 970.0),  # make sure we can do math
            (2, 1000, "TX", 1900.0),
            (3, 3000, "TX", 8370.0),
            (40000.0, 1, "TX", 36000.0),
            (50000, 2, "TX", 85000.0),
        ]
        for test in tests:
            qty, unit_price, state, expected = test
            actual = calc.sales_discount(qty, unit_price, state)
            self.assertEquals(actual, expected, (test, actual))

if __name__ == '__main__':
    main()

