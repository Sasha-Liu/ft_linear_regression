from linear_regression.utils import read_thetas
from linear_regression.math import predict


def predict_price():
    theta0, theta1 = read_thetas()
    mileage = float(input("Enter the mileage of the car: "))
    price = predict(theta0, theta1, mileage)
    print(f"Predicted price: {price:.2f}")


if __name__ == "__main__":
    predict_price()