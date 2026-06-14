import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN INICIAL ---
# st.secrets['GOOGLE_API_KEY'] busca la llave que guardamos en el Setting de Streamlit Cloud.
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ Falta configurar la GOOGLE_API_KEY en los Secrets de Streamlit.")
    st.stop() # Detiene la ejecución si no hay llave
  
st.title("Analog Agent")

question = st.text_input(
    "Pregunta"
)

if question:
    st.write(question)
    response = model.generate_content(
      question
    )
  
  st.write(response.text)
