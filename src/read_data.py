
def read_data():
    try:
        with open("./data/data.csv", "r") as file:
            file_str = file.read()
    except Exception as e:
        print("[ERROR] Cannot read from ./data/data.csv")
        raise e

    lines = file_str.split("\n")
    try:
        lines.remove("km,price")
    except Exception:
        pass

    data = []
    for line in lines:
        mileage, _, price = line.partition(",")
        try:
            data.append(float(mileage), float(price))
        except Exception:
            print(f"[WARNING] invalid line in data.csv : {line}")
    return data    
    