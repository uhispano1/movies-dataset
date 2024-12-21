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
    return pd.read_csv("data/notas.csv")

df = load_data()

# Display the dataset for reference
st.write("### Dataset Preview")
st.dataframe(df, use_container_width=True)

# Input widget to search for a record by ID
st.write("### Search for a Record by ID")
search_id = st.text_input("Enter the ID to search for:")

if search_id:
    # Filter the dataset based on the input ID
    result = df[df["ID"].astype(str) == search_id]

    if not result.empty:
        st.success("Record found:")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No record found with the given ID.")
