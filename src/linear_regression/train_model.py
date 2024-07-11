from .utils import read_data, write_coefs, get_coefs
from .estimate_price import estimate_price
from .average_squared_error import get_average_squared_error
from decimal import Decimal


# LEARNING_RATE = Decimal(0.0000000000776)
LEARNING_RATE = Decimal(0.00000000007765)


def update_coeffs(training_data, coef0, coef1):
    """
    Iterate once through the training data and update coefs.
    """
    gradient_coef0 = Decimal(0.0)
    gradient_coef1 = Decimal(0.0)
    n = Decimal(len(training_data))

    for mileage, price in training_data:
        gradient_coef0 += -2 * (price - estimate_price(mileage, coef0, coef1))
        gradient_coef1 += -2 * (price - estimate_price(mileage, coef0, coef1)) * mileage
        # print(f"price {price} estimate: {estimate_price(mileage, coef0, coef1)}")
        # print(f"gradient coefs : {gradient_coef0} {gradient_coef1}")
    gradient_coef0 = (gradient_coef0 / n) * LEARNING_RATE
    gradient_coef1 = (gradient_coef1 / n) * LEARNING_RATE

    coef0 = coef0 - gradient_coef0
    coef1 = coef1 - gradient_coef1

    return coef0, coef1


def train(epochs, log_interval):
    training_data = read_data()
    coef0, coef1 = get_coefs()
    
    for e in range(epochs):
        coef0, coef1 = update_coeffs(training_data, coef0, coef1)
        error = get_average_squared_error(training_data, coef0, coef1)
        if e % log_interval == 0:
            print(f"Epoch {e}. Coef0: {coef0}, coef1: {coef1}. Average squared error: {error}")
            write_coefs(coef0, coef1)

    
    write_coefs(coef0, coef1)
