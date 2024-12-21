import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("🎬 Movies dataset")
st.write(
    """
    This app visualizes data from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    It shows which movie genre performed best at the box office over the years. Just 
    click on the widgets below to explore!
    """
)


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/notas.csv")
    return df


df = load_data()

# Display the dataset for reference
st.write("### Dataset Preview")
st.dataframe(df, use_container_width=True)

st.write("### Search for a Record by ID")
search_id = st.text_input("Enter the ID to search for:")

if search_id:
    # Filter the dataset based on the input ID
    result = df[df["cedula"].astype(str) == search_id]

    if not result.empty:
        st.success("Record found:")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No record found with the given ID.")
