import pages.simu as simu
import pages.cono as cono
import pages.refe as ref
import pages.eq as eq
import pages.intruc as ins
import pages.obs as obs
import streamlit as st

st.title('MOVIS')
st.subheader("Modelación Volcánica Interactiva y Simple")

pags = {
    "Bienvenido": ins,
    "Marco teórico": cono,
    "Simulación": simu,
    "Ecuaciones": eq,
    "Observaciones": obs,
    "Referencias": ref
}

st.sidebar.title('Ir a:')

selection = st.sidebar.radio("", list(pags.keys()))

page = pags[selection]
page.cargar()