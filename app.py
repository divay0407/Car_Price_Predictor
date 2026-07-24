import streamlit as st
import pickle
import pandas as pd

# ---------------------------------------------------------
# Load model and (optional) supporting data
# ---------------------------------------------------------
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")

try:
    model = pickle.load(open("LinearRegressionModel.pkl", "rb"))
except Exception as e:
    st.error(f"Model failed to load: {e}")
    st.stop()

# If you saved a cleaned dataframe (e.g. car_data.pkl or Cleaned_Car_data.csv)
# to populate dropdowns with real values from training data, load it here.
# Otherwise, edit the lists below manually to match what your model was trained on.
try:
    car_data = pd.read_csv("cleaned_car_data.csv")
    companies = sorted(car_data["company"].unique())
    names = sorted(car_data["name"].unique())
    fuel_types = sorted(car_data["fuel_type"].unique())
    years = sorted(car_data["year"].unique(), reverse=True)
except FileNotFoundError:
    # Fallback manual lists — REPLACE with your actual training categories
    companies = ["Maruti", "Hyundai", "Honda", "Toyota", "Tata", "Ford"]
    names = ["Swift", "i20", "City", "Innova", "Nexon", "Figo"]
    fuel_types = ["Petrol", "Diesel", "CNG", "LPG"]
    years = list(range(2024, 2000, -1))

st.set_page_config(page_title="Car Price Predictor", page_icon="🚗")
st.title("🚗 Car Price Predictor")
st.write("Estimate a used car's resale price based on its details.")

# ---------------------------------------------------------
# Inputs
# ---------------------------------------------------------
company = st.selectbox("Company", companies)
name = st.selectbox("Car Model", names)
year = st.selectbox("Purchase Year", years)
kms_driven = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=30000, step=1000)
fuel_type = st.selectbox("Fuel Type", fuel_types)

# ---------------------------------------------------------
# Predict
# ---------------------------------------------------------
if st.button("Predict Price"):
    input_df = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=["name", "company", "year", "kms_driven", "fuel_type"]
    )

    try:
        prediction = model.predict(input_df)
        st.success(f"Estimated Price: ₹ {round(prediction[0]):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
        st.info(
            "This usually means the input format doesn't match what the model "
            "was trained on. Check column names/order and encoding (e.g. if you "
            "used OneHotEncoder/LabelEncoder inside a Pipeline vs. manually)."
        )

st.caption("Model: car_price_predictor.pkl")
