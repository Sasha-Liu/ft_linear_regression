import numpy as np

from linear_regression.read_write import read_data, read_thetas, write_thetas
from linear_regression.calculation import train
from linear_regression.calculation import (
    average, standard_deviation, standardize)


def standardize_mileages(data):
    mileages = [mileage for mileage, _ in data]
    avg = average(mileages)
    sd = standard_deviation(mileages)

    return np.array([
        (standardize(mileage, avg, sd), price)
        for mileage, price in data
    ])


def train_model():
    theta0, theta1 = read_thetas()
    data = read_data()
    data = standardize_mileages(data)
    print("Data normalized successfully.")

    theta0, theta1 = train(data, theta0, theta1)

    write_thetas(theta0, theta1)
    print("Thetas updated successfully.")


if __name__ == "__main__":
    train_model()
