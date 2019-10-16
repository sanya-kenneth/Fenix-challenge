import unittest
from main.main import compute_days_of_lighting


class ComputeDaysOfPowerTestCase(unittest.TestCase):
    """
    TestCase class for the compute days of power function
    """
    """
    get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000)
    get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000)
    get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000)
    get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000)

    """
    def test_function_returns_error_message_if_input_is_invalid(self):
        power_days = compute_days_of_lighting(200,2,"3",300,4,500,8)
        self.assertEqual(power_days, "Error.Invalid input!! All inputs must be valid numbers.")

    def test_function_returns_141_days_of_power(self):
        power_days = compute_days_of_lighting(3000, 3, 500, 10, 1500, 7,700000)
        self.assertEqual(power_days['days_of_power'], 141)
        self.assertEqual(power_days['customer_balance'], 4500)

    def test_function_returns_17_days_of_power(self):
        power_days = compute_days_of_lighting(500, 3, 500, 10, 500, 7, 21000)
        self.assertEqual(power_days['days_of_power'], 17)
        self.assertEqual(power_days['customer_balance'], 1000)

    def test_function_returns_5_days_of_power(self):
        power_days = compute_days_of_lighting(1300, 0, 500, 0, 1500, 7, 10000)
        self.assertEqual(power_days['days_of_power'], 5)
        self.assertEqual(power_days['customer_balance'], 1000)

    def test_function_returns_1_day_of_power(self):
        power_days = compute_days_of_lighting(10000, 3, 500, 10, 1500, 7, 11000)
        self.assertEqual(power_days['days_of_power'], 1)
        self.assertEqual(power_days['customer_balance'], 1000)
