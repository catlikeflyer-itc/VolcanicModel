import streamlit as st
from PIL import Image

def cargar():
    cuerpo = """
Podemos observar que considerando los valores para las variables más comunes, 
el trayecto del proyectil se ve fuertemente afectado por la resistencia del aire. 
Considerando que el cráter se encuentra a una altura de 5000 metros sobre el nivel 
del mar, un proyectil con las características citadas en la sección de definición 
de variables llegará a un alcance de casi 2100 m del epicentro en condiciones del 
vacío. Cuando realmente el alcance máximo con la resistencia del aire será menor 
a los 200 metros. Esto se debe a que, gracias a la fuerza de resistencia D, 
horizontalmente la magnitud de la velocidad irá decrementando comforme pase el 
tiempo, hasta tal punto que la velocidad en x tendrá una magnitud muy cercana a 0, 
significando que ya no viajará horizontalmente y solo actuará la aceleración 
gravitacional g desde este punto. 
"""
    cuerpo2 = """
A pesar de que el alcánce menor del proyectil con resistencia del aire, podemos 
observar en la gráfica de 'Altura contra tiempo' que el tiempo de vuelo es mayor 
con la resistencia del aire. Esto se debe a que el proyectil empieza a perder 
velocidad horizontal hacia abajo por la fuerza de resistencia que contrapone al 
de gravedad, causando a que esta llegue a un equilibro de fuerzas (fuerza neta 
vertical equivale a 0) y resultando en una velocidad terminal. Esto significa 
que comparado con el proyectil en el vacío este tendra una velocidad promedio 
menor durante el desplazamiento que haga hacia abajo, teniendo así un mayor 
tiempo de vuelo. Esto sucede ya que en un estado del vacío no se presenta una 
velocidad terminal por falta de fuerza que contraponga a la gravedad. La 
velocidad menor del fenómeno con resistencia se puede observar en la gráfica 
de 'Velocidad contra tiempo', en donde la velocidad en cualquier marca de tiempo 
del proyectil en el vacío es sustancialmente mayor. 

Matemáticamente, el fenómeno en el vacío asimila a un modelo polinomial de segundo 
grado fuertemente. Pero el fenómeno con la resistencia no asimila este modelo, de 
hecho, desvia significadamente con una caída abrupta. Dicho esto, la única 
similitud que se tienen entre los dos modelos realizados es el punto inicial en t=0.
"""
    eq = Image.open('images/eq.jpg')
    tiro = Image.open('images/tiro.jpg')

    st.header("Observaciones del simulador")
    st.text(cuerpo)
    st.image(eq, use_column_width=True)
    st.text(cuerpo2)
    st.image(tiro, caption='Imagen de Texas Gateway', use_column_width=True)