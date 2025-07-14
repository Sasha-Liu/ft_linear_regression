from linear_regression.read_write import read_thetas
from linear_regression.calculation import predict
from linear_regression.read_write import read_data
from linear_regression.calculation import (
    average, standard_deviation, standardize)


def predict_price():
    data = read_data()
    mileages = [mileage for mileage, _ in data]
    avg = average(mileages)
    sd = standard_deviation(mileages)

    theta0, theta1 = read_thetas()
    mileage = float(input("Enter the mileage of the car: "))
    price = predict(theta0, theta1, standardize(mileage, avg, sd))
    print(f"Predicted price: {price:.2f}")


if __name__ == "__main__":
    predict_price()
