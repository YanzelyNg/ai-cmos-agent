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

# --- CONECTANDO CON GEMINI ---
model = genai.GenerativeModel("gemini-2.5-flash")

question = st.text_input(
    "Pregunta"
)

if question:
      try:
          # --- 5. CONECTANDO CON GEMINI ---
          # Usamos gemini-1.5-flash porque es el más rápido para visión artificial.
          #model = genai.GenerativeModel("gemini-2.5-flash")
          
          # Este es el 'PROMPT': la instrucción específica para la IA.
          prompt = """
          Dame un resumen de lo que te indico.
          """
          
          # --- 6. ENVIANDO DATOS A LA API ---
          # Enviamos una lista que contiene el texto (prompt) y la imagen.
          response = model.generate_content(prompt)
          
          # --- 7. MOSTRAR EL RESULTADO ---
          st.subheader("Resultado:")
          st.write(response.text)
          
      except Exception as e:
          st.error(f"Error: {e}")

st.write("Hola")
