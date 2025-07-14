from linear_regression.read_write import read_data, read_thetas, write_thetas
from linear_regression.calculation import train


def train_model():
    theta0, theta1 = read_thetas()
    data = read_data()
    theta0, theta1 = train(data, theta0, theta1)
    write_thetas(theta0, theta1)


if __name__ == "__main__":
    train_model()
