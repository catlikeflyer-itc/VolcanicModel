import streamlit as st

def cargar():
    st.header('Intrucciones de uso de la simulación')

    cuerpo ="""
Bienvenido a la simulación de proyectiles volcánicos, en esta simulación podrás simular
la trayectoria de los diferentes proyectiles que se expulsan en el momento de la una 
explosión volcanica. Al lado izquierdo podrás encontrar un menú que te ayudará a navegar 
por la aplicación.

1. En la pestaña de Marco teórico podrás encontrar más información sobre los proyectiles 
que expulsa un volcán.

2. En Ecuaciones y Metodología puedes consultar las ecuaciónes que se utilizaron para 
calcular las componentes.

3. En Simulación podrás encontrar el sistema en si, en donde puedes modificar las 
variables de velocidad inicial, ángulo de salida y altitud del volcán. Posteriormente 
puedes elegir el tipo de proyectil, que arrojará opciones para que ajustes su radio 
(con sus límites físicos dependiendo del proyectil) y te enseñará la masa y densidad de 
esta. En la parte de abajo puedes encontrar gráficas que visualizan las trayectorias.
Por último se visualizan graficas que relacionan cada componente respecto al tiempo. 

4. En Referencias puedes encontrar las fuentes que se emplearon para la investigación.

Por Do Hyun Nam
"""

    st.text(cuerpo)