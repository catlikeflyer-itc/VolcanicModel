import streamlit as st
import numpy as np
import pandas as pd
import func.plot as plot
import func.proyectile as pr

def volumen(r):
    return (4/3)*np.pi*r**3

ceniza = """
Las cenizas son los proyectiles con menor masa y tamaño, a punto de ser invisibles de manera 
unitaria al ojo del humano. De acuerdo a un análisis de los proyectiles del volcán Popocatépetl 
por la CENAPRED, nos dice que una ceniza tiene un radio de 1 mm (0.001 metros) con una masa 
mínima que llega a penas a los 0.5 g (0.0005 kg). Estas partículas son las responsables de causar 
distintos problemas en los humanos, como reducción de la visibilidad y problemas respiratorios. 
Con los aviones causa problemas serios como daños en los motores, por lo que se prohíbe volar por 
el espacio aéreo después de que el volcán expulse cenizas.
"""

lapilli = """
El lapilli se caracteriza por ser de mayor tamaño que la ceniza, pero el rango de tamaño varía 
desde los 2 mm de díametro hasta los 64 mm de diámetro. Su densidad promedio es de 2,800 kg/m^2, 
que es el valor que se tomó para esta simulación. Al momento de cambiar el radio, la masa 
automáticamente cambiará de manera proporcional. Estos proyectiles si bien son pequeños, 
dependiendo de la velocidad de expulsión, pueden generar daños materiales y atentar contra la vida 
humana dado a su densidad relativamente alta. Su forma es bastante irregular, pero geométricamente 
asemejan a una esfera, y considerando las irregularidades se asume que el coeficiente de arrastre 
es mayor al de la esfera con 0.65.
"""

bombas = """
Estos proyectiles llevan este nombre debido a su propiedad física única. En su salida del volcán, 
estos normalmente son expulsados en su estado magmático (literalmente es una bola de lava), por lo 
que el calor que poseén es alto. También, su tamaño es grande, teniendo un diámetro mayor a los 
64 mm (0.64 metros). Dado a su estado semilíqido inicial, durante el trayecto adquieren una forma 
achatada, como un balón de fútbol americano. Esto causa una reducción en arrastre, por lo que se 
consideró un coeficiente similar al balón del 0.47. La masa se obtiene considerando la densidad de 
la lava, de 3,100 2,800 kg/m^2.
"""

def cargar():
    st.header("Simulación de un proyectil")

    v_0 = st.slider("Velocidad Inicial", 100, 500 ,400)
    theta_deg = st.slider('Angulo: ', min_value=0, max_value=90, step=1, value=45)

    vx = v_0*(np.cos(theta_deg))
    vy = v_0*(np.sin(theta_deg))

    st.text(f"V. inicial x en m/s: {vx}")
    st.text(f"V. Inicial y en m/s: {vy}")

    y_0 = st.slider('Altitud del volcan: ', min_value=0, max_value=7000, step=500, value=5000)
    ticks = 1000

    proyectil = st.selectbox('Tipo de proyectil: ',['Ceniza','Lapilli', 'Bombas volcánicas'])

    if proyectil == 'Ceniza':
        st.text(ceniza)
        r = 0.0005
        m = 0.001
        C = 0.7
        x_max = 20000
        ticks = 2000


    elif proyectil == 'Lapilli':
        st.text(lapilli)
        r = st.slider('Radio en metros: ', min_value=0.02, max_value=0.032, step=0.002, value=0.032)
        rho = st.slider("Densidad en kg/m^3:", 2500, 2900, 2700, 50)
        m = rho*volumen(r)
        st.text(f"Masa en kg: {m}, Densidad en kg/m^3: {rho}")
        C = 0.65
        x_max = 20000

    elif proyectil == 'Bombas volcánicas':
        st.text(bombas)
        r = st.slider('Radio en metros: ', min_value=0.032, max_value=1.0, step=0.1, value=0.05)
        rho = st.slider("Densidad en kg/m^3:", 2900, 3400, 3100, 50)
        m = rho*volumen(r)
        st.text(f"Masa en kg: {m}, Densidad en kg/m^3: {rho}")
        C = 0.47
        x_max = 20000

    t = np.linspace(0,100,num=1000)
    rho = 1

    A = np.pi*r**2

    dt = 0.2
    N = 10000
    D = 0.5*(rho*C*A)

    r_x, r_y = pr.proyectile_no_drag(v_0, theta_deg, y_0, t)
    [x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list] = pr.proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N, g = 9.81)

    col1, col2 = st.beta_columns(2)

    fig_no_drag = plot.plot_no_drag(r_x, r_y, x_max, ticks)
    fig_drag = plot.plot_no_drag(x_list, y_list, x_max, ticks)
    fig1 = plot.plot_trayectories(r_x, r_y, x_list, y_list, x_max,ticks)
    fig_comp = plot.plot_extra(t, r_y, t_list, y_list, v_x_list, v_y_list, v_list, a_x_list, a_y_list)

    with col1:
        st.subheader("Trayectoria en el vacío")
        st.pyplot(fig_no_drag)
    with col2:
        st.subheader("Trayectoria con resistencia del aire")
        st.pyplot(fig_drag)
    
    
    st.subheader("Diferencias en las trayectorias")
    st.pyplot(fig1)

    st.subheader("Relación con el tiempo")
    st.pyplot(fig_comp)


