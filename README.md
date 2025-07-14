# Create virtual environment
python3 -m venv .

# Activate virtual environment
source ./bin/activate

# Desactivate virtual environment
deactivate

# Install packages
python -m pip install -r requirements.txt

# Predict price
python3 linear_regression/predict_price.py

# Train model
python3 linear_regression/train_model.py

# Draw graph
python3 linear_regression/draw_graph.py

