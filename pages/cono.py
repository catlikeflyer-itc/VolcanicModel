import streamlit as st
from PIL import Image

def cargar():    
    st.header('Marco Teórico')
    cuerpo = """

En el mundo existen más de 1500 volcanes activos, que ciertamente son unas formaciones 
extraordinarias de la naturaleza, pero también representan un gran peligro para las poblaciones 
circundantes. Capaces de expulsar magma, cenizas y rocas en velocidades y temperaturas 
muy altas, el riesgo que presentan son inigualables.
"""
    cuerpo2 = """

Siendo el enfoque de esta investigación los distintos proyectiles que se arrojan dentro de 
una explosión volcánica, averiguaremos cuáles son de los más comunes que vamos a observar.
Primero que nada tenemos las cenizas, que son polvos minerales originados cuando ocurre una 
combustión de algún material. Estos llegan a tener una masa y diámetro mínimo, por lo que pueden
viajar cientos de kilómetros del epicentro. Dentro de los daños que estos pudieran causar esta 
a reducción de la visibilidad (efectos similares a la neblina), dificultades respiratorias, 
tapado de coladeras y descomposición de aeronaves ya que estas no se disuelven fácilmente con 
el agua.
"""
    cuerpo3 = """

Luego tenemos a los lapilli, que son fragmentos de roca con un diámetro de 2 mm a 64 mm, con una 
masa menor a los 500 gramos generalmente. Al ser más pesados y grandes que las cenizas, estas no 
causan reducción en la visibilidad o dificultades respiratorias, por su tamaño y masa mayor. Los 
fragmentos más grandes pueden llegar a causar daños materiales y heridas en caso de golpear a un 
objeto o persona, pero dado a su masa la energía con la impactarán no será lo suficientemente 
peligrosa.
"""
    cuerpo4 = """

Los que ya se pudieran clasificar como proyectiles balísticos tienen un diámetro mayor a los 
64 mm y una masa igual mayor a los 500 gramos. Su composición varía, por lo que dependiendo 
de la materia que predomina se pueden subclasificar. Comúnmente están formado por magma enfríada,
es decir, en el trayecto se vuelve una roca solida. De acuerdo a la CENAPRED, un balístico de 
300 mm puede viajar a 500 km/hr, e impactar con la energía de un auto de una tonelada viajando 
a 100 km/hr. Estos son los que poseén un factor de riesgo mayor, por lo quer identificar su 
trayectoria es fundamental para reducir los daños en una explosión.
"""
    fisica1 = """

Respecto a las interacciones físicas de los proyectiles, sabemos que se presentan vectores de 
velocidad, fuerza y aceleración interactuando con el proyectil de la siguiente manera:
"""
    
    volcan = Image.open('images/volcan.jpg')
    ceniza = Image.open('images/ceniza.jpg')
    lapilli = Image.open('images/lapilli.png')
    bomba = Image.open('images/bomba.jpg')
    vel = Image.open('images/vel.png')
    force = Image.open('images/force.png')

    st.text(cuerpo)
    st.image(volcan, use_column_width=True)
    st.text(cuerpo2)
    st.image(ceniza, caption='Las nubes visibles son ceniza expulsada', use_column_width=True)
    st.text(cuerpo3)
    st.image(lapilli, caption='Distintas formas del lapilli', use_column_width=True)
    st.text(cuerpo4)
    st.image(bomba, caption='Las bombas al caer, se solidifican como rocas', use_column_width=True)
    st.text(fisica1)
    st.image(vel, caption='Al momento de salir del cráter', use_column_width=True)
    st.image(force, caption='Fuerzas interactuando con el proyectil', use_column_width=True)


    

    