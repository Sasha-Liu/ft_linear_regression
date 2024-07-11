from decimal import Decimal


COEF_FILE = "./data/regression_coefficients"
DATA_FILE = "./data/data.csv"


def get_coefs():
    """
    Read the coeffients from file.
    """
    try:
        with open(COEF_FILE, "r") as file:
            file_str = file.read()
        coef0, _, coef1 = file_str.partition("\n")
        return Decimal(coef0), Decimal(coef1)
    except Exception:
        print(f"Invalid {COEF_FILE}, coeffients default to zero")
        return 0, 0
    

def write_coefs(coef0, coef1):
    """
    Write the coeffients to file.
    """
    try:
        with open(COEF_FILE, "w") as file:
            file.write(f"{coef0}\n{coef1}")
    except Exception:
        print(f"[ERROR] cannot write to {COEF_FILE}")


def read_data():
    try:
        with open(DATA_FILE, "r") as file:
            file_str = file.read()
    except Exception as e:
        print(f"[ERROR] Cannot read from {DATA_FILE}")
        raise e

    lines = file_str.split("\n")
    try:
        lines.remove("km,price")
    except Exception:
        pass

    data = []
    for line in lines:
        if line.isspace() or line == "":
            continue
        mileage, _, price = line.partition(",")
        try:
            data.append((Decimal(mileage), Decimal(price)))
        except (Exception, ValueError) as e:
            print(f"[WARNING] invalid line : {line}")
            raise e
    return data 
