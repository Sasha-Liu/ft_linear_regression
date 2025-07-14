import matplotlib.pyplot as plt

from linear_regression.read_write import read_data, read_thetas
from linear_regression.calculation import (
    standard_deviation,
    average,
)


def calculate_linear_regression_line(theta0, theta1, avg, sd):
    """
    Math:
        The linear regression line on the standardized data is:

            y = ax` + b

        where x` is the standardized data.

        And we know:

            x` = (x - avg) / sd

        where
            x is the original data
            avg is the average of the data
            sd is the standard deviation of the data.

        If we replace x` with (x - avg) / sd, we have:

            y = a * ((x - avg) / sd) + b

        Then we just have to find where the line touch the axes.
    """
    return [
        (0, -theta1 * avg / sd + theta0),
        (-theta0 * sd / theta1 + avg, 0),
    ]


def draw_graph(data, theta0, theta1):
    mileages = [mileage for mileage, _ in data]
    prices = [price for _, price in data]
    avg = average(mileages)
    sd = standard_deviation(mileages)
    theta0, theta1 = read_thetas()
    dots = calculate_linear_regression_line(theta0, theta1, avg, sd)

    fig, ax = plt.subplots(figsize=(10, 5.5), layout="constrained")
    ax.scatter(mileages, prices)
    ax.plot(
        [dots[0][0], dots[1][0]],
        [dots[0][1], dots[1][1]],
    )

    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment="right")
    ax.set_xlabel("Mileage (km)")
    ax.set_ylabel("Price (euro)")
    ax.set_title("Linear Regression")
    plt.show()


if __name__ == "__main__":
    theta0, theta1 = read_thetas()
    data = read_data()
    draw_graph(data, theta0, theta1)
