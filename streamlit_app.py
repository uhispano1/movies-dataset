import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Student Record Finder", page_icon="🎓")
st.title("🎓 Student Record Finder")

st.write(
    """
    This app allows you to search for a student's record by entering their **ID**. 
    The data is loaded from a CSV file located at `data/notas.csv` with the following columns: `carnet`, `nombre`, `ID`, `nota`, `Resultado`.
    """
)


# Load the data from the CSV file
@st.cache_data
def load_data():
    df = pd.read_csv("data/notas.csv")
    return df
df = load_data()
