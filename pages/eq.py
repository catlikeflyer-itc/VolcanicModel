import streamlit as st
import sympy as sy

def cargar():
    st.subheader("Ecuaciones")
    st.text('Trayectoria sin resistencia del aire')
    st.latex(r'''
    \vec{r}(t) = \big(v_{ox}t\big) \vec{i} + \big(-\frac{1}{2}gt^2+v_{oy}t+s_{oy}\big)\vec{j}
    ''')
    st.latex(r'''
    v_{ox} = v_o\cos{\theta}
    v_{oy} = v_o\sin{\theta}
    ''')
    cuerpo = '''
Cuando empezamos a considerar la resistencia del aire, esta aplica una fuerza al 
sentido contrario del movimiento del proyectil. esta fuerza causa se que produzca 
una aceleración en la componente x del movimiento, significando que la velocidad 
en x ya no sera constante como en la situación sin resistencia aérea. Dicho esto, 
ahora sabemos que las componentes de desplazamiento, velocidad y aceleración cambian
conforme avance el tiempo, por lo que necesitamos calcular cada componente en los 
instantes del cambio del tiempo. 

En esta parte es en donde entra la modelación computacional, que se encarga de guardar
los valores que se obtuvieron en cada instante de tiempo, y al cabo del programa llegue 
a generar una visualización de la trayectoria del proyectil.
'''
    st.text(cuerpo)

    st.latex(r"a = F_{d} \cdot \vec{V}^2")
    st.latex(r"v = V(t-\Delta t) + a(t-\Delta t) \cdot \Delta t")
    st.latex(r"s = V(t) \cdot \Delta t + \frac{a(t)}{2} \cdot \Delta t^2")

    cuerpo1 = """
1. Definir las constantes, m, rho, C, A y Delta t dependiendo del problema
2. Definir los valores iniciales y_0, v_0, theta
3. Definir el número de iteraciones N del algoritmo, puedes decidir la estrateguia que prefieras.
4. Encontrar la aceleración inicial con 
"""
    st.text(cuerpo1)
    st.latex(r"a_x = -\frac{D}{m}vv_x y a_y = -g-\frac{D}{m}vv_y")
    st.text("5. Repetir los pasos 6-9 N veces\n6. Calcular lo siguiente")
    st.latex(r"\vec{v}(t+\Delta t) = \vec{v}+\vec{a}\Delta t")
    st.latex(r"\vec{s}(t+\Delta t) = \vec{s}+\vec{v}\Delta t+\frac{1}{2}\vec{a}\Delta t^2")
    st.latex(r"""
    a_x(t+\Delta t) = -\frac{D}{m}vv_x
    a_y(t+\Delta t)= -g-Dvv_y
    """)
    st.text('6. Definir D:')
    st.latex(r"D = \frac{\rho \cdot C\cdot A}{2}")

