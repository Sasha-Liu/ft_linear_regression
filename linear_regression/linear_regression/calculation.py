import math
import numpy as np

LEARNING_RATE = 0.001
LOOP_COUNT = 10000


def mean_squared_error(data, theta0, theta1):
    """
    Data is a numpy array of (mileage, price)
    """
    error = 0.0

    for price, mileage in data:
        predicted_price = predict(theta0, theta1, mileage)
        error += (predicted_price - price) ** 2

    return error / len(data)


def average(data):
    """
    Data is a list
    """
    return sum(data) / len(data)


def standard_deviation(data):
    """
    Data is a list
    """
    avg = average(data)
    variance = sum([(x - avg) ** 2 for x in data]) / len(data)
    return math.sqrt(variance)


def standardize(input_data, avg, sd):
    return (input_data - avg) / sd


def predict(theta0, theta1, mileage):
    return theta0 + (theta1 * mileage)


def standardize_mileages(data):
    print("[INFO] Standardizing mileages...")
    mileages = [mileage for mileage, _ in data]
    avg = average(mileages)
    sd = standard_deviation(mileages)

    stardardized_data = np.array([
        (standardize(mileage, avg, sd), price)
        for mileage, price in data
    ])
    print("[INFO] Standardization complete.")
    return stardardized_data


def train(data, theta0, theta1):

    def loop(data, theta0, theta1):
        temp_theta0 = 0.0
        temp_theta1 = 0.0

        for mileage, price in data:
            predicted_price = predict(theta0, theta1, mileage)
            temp_theta0 += predicted_price - price
            temp_theta1 += (predicted_price - price) * mileage

        temp_theta0 = LEARNING_RATE * (temp_theta0 / len(data))
        temp_theta1 = LEARNING_RATE * (temp_theta1 / len(data))
        return theta0 - temp_theta0, theta1 - temp_theta1
    
    logging_message = "[INFO] Loop {number:6} | theta0: {theta0:9.3f} | theta1: {theta1:9.3f} | MSE: {mse:15.3f}"
    
    data = standardize_mileages(data)

    print(logging_message.format(number="BEFORE", theta0=theta0, theta1=theta1, mse=mean_squared_error(data, theta0, theta1)))
    for number in range(1, LOOP_COUNT + 1):
        theta0, theta1 = loop(data, theta0, theta1)
        if number % 100 == 0:
            print(logging_message.format(number=number, theta0=theta0, theta1=theta1, mse=mean_squared_error(data, theta0, theta1)))
            
    print(logging_message.format(number="AFTER", theta0=theta0, theta1=theta1, mse=mean_squared_error(data, theta0, theta1)))

    return theta0, theta1
