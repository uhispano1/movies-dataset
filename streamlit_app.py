import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Notas de Arquitectura de Bases de Datos TAND05", page_icon="📝")
st.title("📝 Notas de Arquitectura de Bases de Datos TAND05")
st.write(
    """
    Esta aplicación permite buscar el registro de un estudiante ingresando su **numero de cédula**. 
    """
)
st.write(
    """
    ### Instrucciones:
    1. Ingrese su **numero de cédula** en el campo de texto para buscar su registro.
    2. Si el registro existe, se mostrará en la tabla debajo.
    """
)


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/notas.csv")
    return df


df = load_data()
df["cedula"] = df["cedula"].astype(str)

# Display the dataset for reference
 st.write("### Dataset Preview")
 st.dataframe(df, use_container_width=True)

st.write("### Buscar registro por número de cédula")
search_id = st.text_input("Introduce el número de cédula a consultar:")

if search_id:
    # Filter the dataset based on the input ID
    result = df[df["cedula"].astype(str) == search_id]

    if not result.empty:
        st.success("Registro encontrado:")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No hay registro encontrado.")
