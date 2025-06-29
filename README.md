# Create virtual environment
python -m venv .

# Activate virtual environment
source ./bin/activate

# Desactivate virtual environment
deactivate

# Install packages
python -m pip install -r requirements.txt

# Predict price
python3 linear_regression/predict_price.py

