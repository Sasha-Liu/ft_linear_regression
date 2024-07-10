

def get_coefs():
    """
    Read the coeffients from file.
    """
    try:
        with open("./data/regression_coefficients") as file:
            file_str = file.read()
        coef0, _, coef1 = file_str.partition("\n")
        return int(coef0), int(coef1)
    except Exception:
        print("Invalid ./regression_coeffients file, coeffients default to zero")
        return 0, 0


def estimate_price(mileage):
    coef0, coef1 = get_coefs()
    return coef0 + coef1 * mileage


def prompt_user():
    """
    Estimate car price based on mileage given by user.
    """
    try:
        mileage = input("Please enter car mileage (integer): ")
        mileage = int(mileage)
        price = estimate_price(mileage)
        print(f"The estimated price is {price}")
    except Exception:
        print("[ERROR] Invalid mileage.")
    except KeyboardInterrupt:
        print("[KeyboardInterrupt]")


if __name__ == "__main__":
    prompt_user()