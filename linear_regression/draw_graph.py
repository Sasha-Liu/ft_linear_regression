import matplotlib.pyplot as plt

from linear_regression.read_write import read_data, read_thetas
from linear_regression.calculation import (
    standard_deviation,
    average,
)

SAVE_PATH = "./linear_regression/data/cars.png"


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


def draw_graph():
    #  Prepare data
    theta0, theta1 = read_thetas()
    data = read_data()
    mileages = [mileage for mileage, _ in data]
    prices = [price for _, price in data]
    avg = average(mileages)
    sd = standard_deviation(mileages)

    #  Plot dots and line
    fig, ax = plt.subplots(figsize=(10, 5.5), layout="constrained")
    ax.scatter(mileages, prices)
    dots = calculate_linear_regression_line(theta0, theta1, avg, sd)
    ax.plot(
        [dots[0][0], dots[1][0]],
        [dots[0][1], dots[1][1]],
    )

    #  Set labels and titles
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment="right")
    ax.set_xlabel("Mileage (km)")
    ax.set_ylabel("Price (euro)")
    ax.set_title("Linear Regression")

    #  Present graph and save it
    plt.show()
    fig.savefig(SAVE_PATH, transparent=False, dpi=80, bbox_inches="tight")


if __name__ == "__main__":
    try:
        draw_graph()
    except Exception as e:
        print(f"[ERROR] {e}")
