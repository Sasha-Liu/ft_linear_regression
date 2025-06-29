from linear_regression.utils import read_data, read_thetas, write_thetas
from linear_regression.math import train, mean_squared_error


def train_model():
    theta0, theta1 = read_thetas()
    data = read_data()
    print(f"Initial thetas: theta0 = {theta0}, theta1 = {theta1}")
    print(f"Initial MSE: {mean_squared_error(data, theta0, theta1)}")

    theta0, theta1 = train(data, theta0, theta1)

    print(f"Final thetas: theta0 = {theta0}, theta1 = {theta1}")
    print(f"Final MSE: {mean_squared_error(data, theta0, theta1)}")

    write_thetas(theta0, theta1)
    print("Thetas updated successfully.")



if __name__ == "__main__":
    train_model()