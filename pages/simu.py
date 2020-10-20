import streamlit as st
import numpy as np
import func.plot as plot
import func.proyectile as pr

def cargar():

    v_0 = st.slider("Velocidad Inicial", 100, 500 ,350)
    theta_deg = st.slider('Angulo: ', min_value=0, max_value=90, step=5, value=45)
    y_0 = st.slider('Altitud del volcan: ', min_value=0, max_value=6000, step=500, value=3000)
    ticks = 1000

    proyectil = st.selectbox('Tipo de proyectil: ',['Ceniza','Lapilli', 'Bombas volcánicas'])
    if proyectil == 'Ceniza':
        r = 0.0005
        m = 0.001
        C = 0.7
        x_max = 5000
        ticks = 100

    elif proyectil == 'Lapilli':
        r = st.slider('Radio en metros: ', min_value=0.001, max_value=0.032, step=0.002, value=0.032)
        m = st.slider('Masa en kg: ', min_value=0.010, max_value=0.5, step=0.02, value=0.5)
        C = 0.65
        x_max = 5000

    elif proyectil == 'Bombas volcánicas':
        r = st.slider('Radio en metros: ', min_value=0.032, max_value=1, step=0.1, value=0.05)
        m = st.slider('Masa en kg: ', min_value=0.010, max_value=10, step=0.2, value=1)
        C = 0.47
        x_max = 10000

    t = np.linspace(0,60,num=1000)
    rho = 1

    A = np.pi*r**2

    dt = 0.2
    N = 10000
    D = 0.5*(rho*C*A)

    r_x, r_y = pr.proyectile_no_drag(v_0, theta_deg, y_0, t)
    [x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list] = pr.proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N, g = 9.81)


    fig_no_drag = plot.plot_no_drag(r_x, r_y, x_max, ticks)
    fig_drag = plot.plot_no_drag(x_list, y_list, x_max, ticks)
    fig1 = plot.plot_trayectories(r_x, r_y, x_list, y_list, x_max,ticks)


    st.pyplot(fig_no_drag)
    st.pyplot(fig_drag)
    st.pyplot(fig1)

