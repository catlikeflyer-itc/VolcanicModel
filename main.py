import pages.simu as simu
import pages.cono as cono
import pages.refe as ref
import streamlit as st

st.title('Modelacion volcanica')

pags = {
    "Marco teórico": cono,
    "Simulación": simu,
    "Referencias": ref
}

st.sidebar.title('Ir a:')

selection = st.sidebar.radio("", list(pags.keys()))

page = pags[selection]
page.cargar()