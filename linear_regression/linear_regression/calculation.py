LEARNING_RATE = 0.01
LOOP_COUNT = 1000


def mean_squared_error(data, theta0, theta1):
    """
    Data is a numpy array of (mileage, price)
    """
    error = 0.0

    for mileage, price in data:
        predicted_price = predict(theta0, theta1, mileage)
        error += (predicted_price - price) ** 2

    return error / len(data)



def predict(theta0, theta1, mileage):
    return  theta0 + (theta1 * mileage)


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
        return temp_theta0, temp_theta1

    for number in range(LOOP_COUNT):
        temp_theta0, temp_theta1 = loop(data, theta0, theta1)
        theta0 = temp_theta0
        theta1 = temp_theta1
        if number % 100 == 0:
            print(f"Loop {number}: theta0 = {theta0}, theta1 = {theta1}, MSE = {mean_squared_error(data, theta0, theta1)}")

    return theta0, theta1
