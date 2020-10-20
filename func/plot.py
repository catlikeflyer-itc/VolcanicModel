import matplotlib.pyplot as plt
import numpy as np

def plot_no_drag(r_x, r_y, x_max, ticks):
    
    fig = plt.figure(figsize=(20,10))

    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")

    plt.grid()
    plt.title("Trayectoria sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 10000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,10000+1,1000))

    return fig

def plot_drag(r_x, r_y, x_max, ticks):
    
    fig = plt.figure(figsize=(20,10))

    plt.plot(r_x,r_y, label="Con resistencia del aire")

    plt.grid()
    plt.title("Trayectoria sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 10000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,10000+1,1000))

    return fig


def plot_trayectories(r_x, r_y, x_list, y_list, x_max, ticks):
    
    fig1 = plt.figure(figsize=(20,10))

    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")
    plt.plot(x_list,y_list, label="Con Resistencia de Aire")

    plt.grid()


    plt.title("Trayectoria con y sin resistencia de aire")

    plt.xlim([0,x_max])
    plt.ylim([0, 10000])

    _ = plt.xticks(np.arange(0,x_max+1,ticks))
    _ = plt.yticks(np.arange(0,10000+1,1000))

    _ = plt.legend()

    return fig1

