from .read_data import read_data
from .estimate_price import estimate_price


def get_average_squared_error():
    data = read_data()
    squared_error = [
        (estimate_price(mileage) - price) ** 2
        for mileage, price in data
    ]
    return sum(squared_error) / len(squared_error)


if __name__ == "__main__":
    loss = get_average_squared_error()
    print(f"The average loss is {loss}")