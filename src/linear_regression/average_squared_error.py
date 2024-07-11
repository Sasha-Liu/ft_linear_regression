from .estimate_price import estimate_price
from decimal import Decimal

def get_average_squared_error(training_data, coef0, coef1):
    total_error = Decimal(0.0)
    for mileage, price in training_data:
        total_error += (Decimal(estimate_price(mileage, coef0, coef1)) - Decimal(price)) ** 2
    return total_error / len(training_data)