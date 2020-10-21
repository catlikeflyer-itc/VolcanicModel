import matplotlib.pyplot as plt
import numpy as np

def plot_no_drag(r_x, r_y, x_max, ticks):
    
    fig = plt.figure(figsize=(20,20))

    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")

    plt.grid()
    plt.title("Trayectoria sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 20000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,20000+1,2000))

    return fig

def plot_drag(r_x, r_y, x_max, ticks):
    
    fig = plt.figure(figsize=(15,20))

    plt.plot(r_x,r_y, label="Con resistencia del aire")

    plt.grid()
    plt.title("Trayectoria sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 18000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,10000+1,2000))

    return fig


def plot_trayectories(r_x, r_y, x_list, y_list, x_max, ticks):
    
    fig1 = plt.figure(figsize=(20,20))

    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")
    plt.plot(x_list,y_list, label="Con Resistencia de Aire")

    plt.grid()


    plt.title("Trayectoria con y sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 18000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,20000+1,2000))

    _ = plt.legend()

    return fig1

def plot_compare(r_x, r_y, x_list, y_list, x_max, ticks, concept):
    
    fig1 = plt.figure(figsize=(20,20))

    plt.plot(r_x,r_y, label="Proyectil 1")
    plt.plot(x_list,y_list, label="Proyectil 2")

    plt.grid()


    plt.title("Comparación de dos proyectiles "+concept)

    plt.xlim([0,x_max])
    plt.ylim([0, 18000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,20000+1,2000))

    _ = plt.legend()

    return fig1

def plot_extra(t, r_y, t_list, y_list, v_x_list, v_y_list, v_list, a_x_list, a_y_list):
    fig = plt.figure(figsize = (15,8))

    plt.subplot(2,2,1)

    plt.plot(t,r_y,label="Vacio")
    plt.plot(t_list,y_list,label="Con Resistencia de Aire")
    plt.title("Altura contra tiempo")
    plt.xlim([0,100])
    _ = plt.ylim([0,10000])

    plt.subplot(2,2,2)

    plt.plot(t_list,v_x_list,label="v_x")
    plt.plot(t_list,v_y_list,label="v_y")
    plt.plot(t_list,v_list,label="v")
    plt.title("Velocidad contra tiempo")
    plt.xlim([0,100])

    plt.subplot(2,2,3)

    plt.plot(t_list,a_x_list,label="a_x")
    plt.plot(t_list,a_y_list,label="a_y")
    plt.title("Aceleracion contra tiempo")
    plt.xlim([0,100])

    plt.tight_layout()

    return fig

