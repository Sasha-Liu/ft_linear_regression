DATA_FILE = "linear_regression/data/data.csv"
THETAS_FILE = "linear_regression/data/thetas.txt"


def read_data():
    data = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
        lines = lines[1:]
        for line in lines:
            mileage, price = line.split(",")
            data.append((float(mileage), float(price)))
    except Exception as e:
        print("[ERROR] Failed to read data file.")
        raise e

    return data


def read_thetas():
    try:
        with open(THETAS_FILE, "r", encoding="utf-8") as file:
            params = file.read()
        theta0, theta1 = params.split("\n")
        theta0 = float(theta0)
        theta1 = float(theta1)
        return theta0, theta1
    except Exception as e:
        print(f"[ERROR] Failed to read thetas file: {e}")
        raise e


def write_thetas(new_thata0, new_theta1):
    try:
        with open(THETAS_FILE, "w", encoding="utf-8") as file:
            file.write(f"{new_thata0}\n{new_theta1}")
        print("[INFO] Thetas updated successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to update thetas file: {e}")
        raise e
