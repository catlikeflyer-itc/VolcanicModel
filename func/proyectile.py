import numpy as np

def proyectile_no_drag(v_0, theta_deg, y_0, t, g = 9.81):
    
    theta_rad = np.radians(theta_deg)
    v_0x = v_0*np.cos(theta_rad)
    v_0y = v_0*np.sin(theta_rad)

    r_x = v_0x*t
    r_y = (-1/2*g*(t**2)) + (v_0y*t) + (y_0)
    
    return r_x, r_y

def proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N, g = 9.81):
    
    # Ángulo en radianes
    theta_rad = np.radians(theta_deg)
    
    # Componentes de velocidad inicial
    v_0x = v_0*np.cos(theta_rad)
    v_0y = v_0*np.sin(theta_rad)
    
    # Tiempo
    this_t = 0
    t_list = [this_t]

    # Velocidad
    v = v_0
    v_x = v_0x
    v_y = v_0y
    

    v_list = [v]
    v_x_list = [v_0x]
    v_y_list = [v_0y]

    # Posición
    x = 0
    y = 3020

    x_list = [x]
    y_list = [y]

    # Calcula la aceleración inicial
    a_x = -(D/m)*v*v_x
    a_y = -g-(D/m)*v*v_y

    a_x_list = [a_x]
    a_y_list = [a_y]
    
    for i in range(N):
        
        # Calcular las velocidades para 'x' y 'y' del siguiente paso
        v_x_next = v_x + a_x*dt
        v_y_next = v_y + a_y*dt
        
        # Calcular la magnitud del vector de velocidad, en otras palabras, queremos encontrar
        # la magnitud del vector cuyas componentes son v_x_next y v_y_next
        v_next = np.sqrt((v_x_next**2) + (v_y_next**2))

        # Agrega los valores calculados a las listas v_list, v_x_list, v_y_list. Puedes hacer
        # esto con .append()
        v_list.append(v_next)
        v_x_list.append(v_x_next)
        v_y_list.append(v_y_next)

        # Calcula las posiciones 'x' y 'y' del siguiente paso
        x_next = x + (v_x*dt) + (1/2*a_x*(dt**2))
        y_next = y + (v_y*dt) + (1/2*a_y*(dt**2))

        # Agrega los valores calculados a las listas x_list y y_list
        x_list.append(x_next)
        y_list.append(y_next)

        # Calcula las aceleraciones para 'x' y 'y' del siguiente paso
        a_x_next = -(D/m)*v*v_x
        a_y_next = -g-(D/m)*v*v_y

        # Agrega los valores calculados a las listas a_x_list y a_y_list
        a_x_list.append(a_x_next)
        a_y_list.append(a_y_next)

        
        # Como ya terminamos esta iteración, hagamos que lo que calculamos como _next
        # sea el paso actual en la siguiente iteración. Por claridad, el primer
        # ejemplo se encuentra resuelto. Haz lo mismo con los demás.
        
        v_x = v_x_next
        v_y = v_y_next
        v = v_next

        x = x_next
        y = y_next

        a_x = a_x_next
        a_y = a_y_next

        # Calcula el tiempo y guárdalo en la lista t_list
        this_t += dt
        t_list.append(this_t)
        
    return x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list

