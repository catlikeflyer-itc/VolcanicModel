import streamlit as st
import numpy as np
import pandas as pd
import func.plot as plot
import func.proyectile as pr

def volumen(r):
    return (4/3)*np.pi*r**3

def columna():
    v_0 = st.slider("Velocidad Inicial", 100, 500 ,400)
    theta_deg = st.slider('Angulo: ', min_value=0, max_value=90, step=1, value=45)
    vx = v_0*(np.cos(theta_deg))
    vy = v_0*(np.sin(theta_deg))
    st.text(f"V. inicial x: {vx}, V. Inicial y: {vy}")
    y_0 = st.slider('Altitud del volcan: ', min_value=0, max_value=6000, step=500, value=3000)
    ticks = 1000

    proyectil = st.selectbox('Tipo de proyectil: ',['Ceniza','Lapilli', 'Bombas volcánicas'])
    if proyectil == 'Ceniza':
        r = 0.0005
        m = 0.001
        C = 0.7
        x_max = 20000
        ticks = 2000
        

    elif proyectil == 'Lapilli':
        r = st.slider('Radio en metros: ', min_value=0.02, max_value=0.032, step=0.002, value=0.032)
        rho = st.slider("Densidad en kg/m^3:", 2500, 2900, 50)
        m = rho*volumen(r)
        st.text(f"Masa en kg: {m}, Densidad en kg/m^3: {rho}")
        C = 0.65
        x_max = 20000

    elif proyectil == 'Bombas volcánicas':
        r = st.slider('Radio en metros: ', min_value=0.032, max_value=1.0, step=0.1, value=0.05)
        rho = st.slider("Densidad en kg/m^3:", 2900, 3400, 50)
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

    return r_x, r_y, x_list, y_list

def columna2():
    v_02 = st.slider("Velocidad Inicial", 100, 500 ,400)
    theta_deg2 = st.slider('Angulo: ', min_value=0, max_value=90, step=1, value=45)
    vx = v_02*(np.cos(theta_deg2))
    vy = v_02*(np.sin(theta_deg2))
    st.text(f"V. inicial x: {vx}, V. Inicial y: {vy}")
    y_02 = st.slider('Altitud del volcan: ', min_value=0, max_value=6000, step=500, value=3000)
    ticks = 1000

    proyectil2 = st.selectbox('Tipo de proyectil: ',['Ceniza','Lapilli', 'Bombas volcánicas'])
    if proyectil2 == 'Ceniza':
        r2 = 0.0005
        m2 = 0.001
        C2 = 0.7
        x_max = 20000
        ticks = 2000
        

    elif proyectil2 == 'Lapilli':
        r2 = st.slider('Radio en metros: ', min_value=0.02, max_value=0.032, step=0.002, value=0.032)
        rho2 = st.slider("Densidad en kg/m^3:", 2500, 2900, 50)
        m2 = rho2*volumen(r2)
        st.text(f"Masa en kg: {m2}, Densidad en kg/m^3: {rho2}")
        C2 = 0.65
        x_max = 20000

    elif proyectil2 == 'Bombas volcánicas':
        r2 = st.slider('Radio en metros: ', min_value=0.032, max_value=1.0, step=0.1, value=0.05)
        rho2 = st.slider("Densidad en kg/m^3:", 2900, 3400, 50)
        m2 = rho*volumen(r2)
        st.text(f"Masa en kg: {m2}, Densidad en kg/m^3: {rho2}")
        C2 = 0.47
        x_max = 20000

    t2 = np.linspace(0,100,num=1000)
    rho = 1

    A2 = np.pi*r2**2

    dt2 = 0.2
    N2 = 10000
    D2 = 0.5*(rho*C2*A2)

    r_x, r_y = pr.proyectile_no_drag(v_02, theta_deg2, y_02, t2)
    [x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list] = pr.proyectile_with_drag(v_02, theta_deg2, y_02, m2, D2, dt2, N2, g = 9.81)

    return r_x, r_y, x_list, y_list
    

def cargar():
    col1, col2 = st.beta_columns(2)
    with col1:
        x1, y1, xd1, yd1 = columna()
    with col2:
        x2, y2, xd2, yd2 = columna2()

    fig_no_drag = plot.plot_compare(x1, y1, x2, y2, 20000, 2000, "sin resistencia del aire")
    fig_drag = plot.plot_compare(xd1, yd1, xd2, yd2, 20000, 2000, "con resistencia del aire")  

    st.header("Comparación de las trayectorias")
    st.pyplot(fig_no_drag)
    st.pyplot(fig_drag)