# Resolucion de ejercicios 1 en Python
import matplotlib.pyplot as plt
import numpy as np

# Ejercicio 1: Calculo del precio de una vivienda
# Formula: P = m * A + b

def calcular_precio_vivienda(m, A, b):
    return m * A + b

def graficar_precio_vivienda(m, b, A_min, A_max):
    A = np.linspace(A_min, A_max, 100)
    P = calcular_precio_vivienda(m, A, b)
    plt.plot(A, P, label=f"m={m}, b={b}")
    plt.xlabel("Área construida (A)")
    plt.ylabel("Precio (P)")
    plt.title("Precio de Vivienda vs Área Construida")
    plt.legend()
    plt.grid()

# Ejercicio 2: Calculo de la ganancia mensual
# Formula: G = c * N + b

def calcular_ganancia_mensual(c, N, b):
    return c * N + b

def graficar_ganancia_mensual(c, b, N_min, N_max):
    N = np.linspace(N_min, N_max, 100)
    G = calcular_ganancia_mensual(c, N, b)
    plt.plot(N, G, label=f"c={c}, b={b}")
    plt.xlabel("Número de predicciones (N)")
    plt.ylabel("Ganancia (G)")
    plt.title("Ganancia Mensual vs Número de Predicciones")
    plt.legend()
    plt.grid()

# Ejercicio 3: Calculo del tiempo total de procesamiento
# Formula: T = k * D + c

def calcular_tiempo_procesamiento(k, D, c):
    return k * D + c

def graficar_tiempo_procesamiento(k, c, D_min, D_max):
    D = np.linspace(D_min, D_max, 100)
    T = calcular_tiempo_procesamiento(k, D, c)
    plt.plot(D, T, label=f"k={k}, c={c}")
    plt.xlabel("Tamaño de datos (D)")
    plt.ylabel("Tiempo (T)")
    plt.title("Tiempo de Procesamiento vs Tamaño de Datos")
    plt.legend()
    plt.grid()

# Ejercicio 4: Calculo del costo total
# Formula: C = p * D + f

def calcular_costo_total(p, D, f):
    return p * D + f

def graficar_costo_total(p, f, D_min, D_max):
    D = np.linspace(D_min, D_max, 100)
    C = calcular_costo_total(p, D, f)
    plt.plot(D, C, label=f"p={p}, f={f}")
    plt.xlabel("Cantidad de datos (D)")
    plt.ylabel("Costo Total (C)")
    plt.title("Costo Total vs Cantidad de Datos")
    plt.legend()
    plt.grid()

# Ejercicio 5: Medicion calibrada
# Formula: M = a * R + b

def calcular_medicion_calibrada(a, R, b):
    return a * R + b

def graficar_medicion_calibrada(a, b, R_min, R_max):
    R = np.linspace(R_min, R_max, 100)
    M = calcular_medicion_calibrada(a, R, b)
    plt.plot(R, M, label=f"a={a}, b={b}")
    plt.xlabel("Medición en crudo (R)")
    plt.ylabel("Medición Calibrada (M)")
    plt.title("Medición Calibrada vs Medición en Crudo")
    plt.legend()
    plt.grid()

# Ejercicio 6: Tiempo de respuesta promedio
# Formula: T = m * S + b

def calcular_tiempo_respuesta(m, S, b):
    return m * S + b

def graficar_tiempo_respuesta(m, b, S_min, S_max):
    S = np.linspace(S_min, S_max, 100)
    T = calcular_tiempo_respuesta(m, S, b)
    plt.plot(S, T, label=f"m={m}, b={b}")
    plt.xlabel("Solicitudes simultáneas (S)")
    plt.ylabel("Tiempo de Respuesta (T)")
    plt.title("Tiempo de Respuesta vs Solicitudes Simultáneas")
    plt.legend()
    plt.grid()

# Ejercicio 7: Ingresos de una plataforma
# Formula: I = p * S + b

def calcular_ingresos(p, S, b):
    return p * S + b

def graficar_ingresos(p, b, S_min, S_max):
    S = np.linspace(S_min, S_max, 100)
    I = calcular_ingresos(p, S, b)
    plt.plot(S, I, label=f"p={p}, b={b}")
    plt.xlabel("Número de suscriptores (S)")
    plt.ylabel("Ingresos (I)")
    plt.title("Ingresos vs Número de Suscriptores")
    plt.legend()
    plt.grid()

# Ejercicio 8: Energía consumida
# Formula: E = k * O + b

def calcular_energia_consumida(k, O, b):
    return k * O + b

def graficar_energia_consumida(k, b, O_min, O_max):
    O = np.linspace(O_min, O_max, 100)
    E = calcular_energia_consumida(k, O, b)
    plt.plot(O, E, label=f"k={k}, b={b}")
    plt.xlabel("Operaciones realizadas (O)")
    plt.ylabel("Energía Consumida (E)")
    plt.title("Energía Consumida vs Operaciones Realizadas")
    plt.legend()
    plt.grid()

# Ejercicio 9: Base de seguidores
# Formula: L = m * F + b

def calcular_base_seguidores(m, F, b):
    return m * F + b

def graficar_base_seguidores(m, b, F_min, F_max):
    F = np.linspace(F_min, F_max, 100)
    L = calcular_base_seguidores(m, F, b)
    plt.plot(F, L, label=f"m={m}, b={b}")
    plt.xlabel("Número de Seguidores (F)")
    plt.ylabel("Base de Likes (L)")
    plt.title("Base de Likes vs Número de Seguidores")
    plt.legend()
    plt.grid()

# Ejercicio 10: Costo total en ML
# Formula: C = p * t + c

def calcular_costo_ml(p, t, c):
    return p * t + c

def graficar_costo_ml(p, c, t_min, t_max):
    t = np.linspace(t_min, t_max, 100)
    C = calcular_costo_ml(p, t, c)
    plt.plot(t, C, label=f"p={p}, c={c}")
    plt.xlabel("Número de Iteraciones (t)")
    plt.ylabel("Costo Total (C)")
    plt.title("Costo Total vs Número de Iteraciones")
    plt.legend()
    plt.grid()

# Ejemplo de uso y graficas
if __name__ == "__main__":
    # Ejercicio 1
    plt.figure(figsize=(10, 6))
    graficar_precio_vivienda(m=1000, b=20000, A_min=50, A_max=200)
    plt.show()

    # Ejercicio 2
    plt.figure(figsize=(10, 6))
    graficar_ganancia_mensual(c=50, b=5000, N_min=0, N_max=300)
    plt.show()

    # Ejercicio 3
    plt.figure(figsize=(10, 6))
    graficar_tiempo_procesamiento(k=0.5, c=10, D_min=100, D_max=1000)
    plt.show()

    # Ejercicio 4
    plt.figure(figsize=(10, 6))
    graficar_costo_total(p=2, f=100, D_min=100, D_max=1000)
    plt.show()

    # Ejercicio 5
    plt.figure(figsize=(10, 6))
    graficar_medicion_calibrada(a=1.5, b=5, R_min=0, R_max=100)
    plt.show()

    # Ejercicio 6
    plt.figure(figsize=(10, 6))
    graficar_tiempo_respuesta(m=0.2, b=1, S_min=0, S_max=50)
    plt.show()

    # Ejercicio 7
    plt.figure(figsize=(10, 6))
    graficar_ingresos(p=10, b=500, S_min=0, S_max=1000)
    plt.show()

    # Ejercicio 8
    plt.figure(figsize=(10, 6))
    graficar_energia_consumida(k=5, b=20, O_min=0, O_max=500)
    plt.show()

    # Ejercicio 9
    plt.figure(figsize=(10, 6))
    graficar_base_seguidores(m=1.5, b=200, F_min=0, F_max=1000)
    plt.show()

    # Ejercicio 10
    plt.figure(figsize=(10, 6))
    graficar_costo_ml(p=0.5, c=50, t_min=0, t_max=100)
    plt.show()
