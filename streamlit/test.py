import streamlit as st
from streamlit_folium import st_folium
import folium

# Titolo dell'app
st.title("Form con Mappa Leaflet")

# Creazione di un form Streamlit
with st.form("my_form"):
    st.write("Inserisci i tuoi dettagli:")
    
    # Campi del form
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    
    # Bottone di submit
    submitted = st.form_submit_button("Invia")
    if submitted:
        st.write("Grazie,", nome, "La tua email è stata registrata.")

# Configurazione iniziale della mappa Leaflet (usando Folium)
m = folium.Map(location=[45.4628328, 9.107692], zoom_start=12)

# Visualizzazione della mappa in Streamlit
st_folium(m, height=300)

# Ulteriori azioni dopo la sottomissione del form possono essere gestite qui
