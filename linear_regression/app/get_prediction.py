
def get_prediction():
    """
    Prompt user for mileage and predict the price of the car.
    """
    try:
        with open("linear_regression/app/params.txt", "r", encoding="utf-8") as file:
            params = file.read()
        w, b = params.split("\n")
        w = float(w)
        b = float(b)
    except Exception as e:
        print(f"Please check that linear_regression/app/params.txt exist with valid contents.\nError: {str(e)}")
        return
    
    while True:
        mileage = input("Enter a mileage: ")
        if mileage == "quit":
            return
        try:
            mileage = float(mileage)
        except Exception as e:
            print(f"Invalid input : {str(e)}")
        else:
            print(f"Predicted price: {mileage * w + b}")


if __name__ == "__main__":
    get_prediction()