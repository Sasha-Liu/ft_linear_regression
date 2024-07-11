from .utils import get_coefs
from decimal import Decimal

def estimate_price(mileage, coef0 = None, coef1 = None):
    if coef0 is None or coef1 is None:
        coef0, coef1 = get_coefs()
    return Decimal(coef0 + coef1 * mileage)
