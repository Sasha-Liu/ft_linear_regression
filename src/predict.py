from linear_regression.estimate_price import estimate_price


def predict():
    """
    Estimate car price based on mileage given by user.
    """
    try:
        mileage = input("Please enter car mileage (km): ")
        mileage = float(mileage)
        price = estimate_price(mileage)
        print(f"The estimated price is {price}")
    except Exception:
        print("[ERROR] Invalid mileage.")
    except KeyboardInterrupt:
        print("[KeyboardInterrupt]")


if __name__ == "__main__":
    predict()