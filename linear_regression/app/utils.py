
def _read_data():
    try:
        with open("linear_regression/data/data.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()
        result = []
        lines = lines[1:]
        for line in lines:
            mileage, price = line.split(",")
            result.append((int(mileage), int(price)))
        return result
    except Exception as e:
        print(f"")
        raise e


def _get_params():
    try:
        with open("linear_regression/app/params.txt", "r", encoding="utf-8") as file:
            params = file.read()
        w, b = params.split("\n")
        w = int(w)
        b = int(b)
        return w, b
    except Exception as e:
        print(f"")
        raise e


def _update_params(new_w, new_b):
    pass
