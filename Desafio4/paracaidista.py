
# John Castillo Valencia
# MAT-156 Analisis Numérico
# UMSA - INFORMÁTICA

# Se importan las librerias para graficar
import matplotlib.pyplot as plt

# Variables
a = 9.8     # fuerza de gravedad en m/s
W = 68.1    # peso del objeto en Kgs
r = 12.5    # Resistencia del aire
e = 2.71828 # Constante de Napier
t = 0       # Tiempo inicial s
i = 2       # Intervalo de tiempo en s
v1 = 0      # Var solucion analítica
v2 = 1      # Var solucion analítica
vi = 0      # Vwlocidad instantanea
vct = 1     # Control del ciclo numerico

# Para el método numeirco
tc1 = []
vc1 = []
tc2 = []
vc2 = []

# calculo de velocidad usando metodo numerico
def vc(a, W, r, i, vi):
    return vi + (a - (r / W) * vi) * i

# calculo de velocidad usando metoo analitico
def vt(a, W, r, t, e):
    return ((a * W) / r) * (1 - e ** - ((r / W) * t))


def ca(a, W, r, t, e, i, v1, v2):
    while v1 != v2:
        v1 = vt(a, W, r, t, e)
        vc1.append(v1)
        tc1.append(t)

        t = t + i
        v2 = vt(a, W, r, t, e)


def cn(a, W, r, t, i, vi, vct):
    vc2.append(0)
    tc2.append(0)
    while vi != vct:
        vi = vc(a, W, r, i, vi)
        vc2.append(vi)
        t = t + i
        tc2.append(t)
        vct = vc(a, W, r, i, vi)

#  Grafica de todos los datos
def graficar(vc1, vc2, tc1, tc2):
    marcas = tc2[0::3]
    mapeado = range(len(marcas))
    plt.xticks(mapeado, marcas, rotation = 270)
    plt.title('Comparacion calculo de velocidad caida libre')
    plt.ylabel('Velocidad')
    plt.xlabel('Tiempo')
    plt.xlim(0, len(marcas))
    plt.ylim(vc1[0], vc1[-1] + 5)
    plt.plot(tc1, vc1, label="Analitico", marker="o", color="blue", ls="-", lw="1")
    plt.plot(tc2, vc2, label="Numerico", marker="x", color="red", ls="-.", lw="1")
    plt.legend()
    plt.show()

# Esta funcion presenta la tabla de valres calculados que se grafican
def tabla(vc1, tc1, vc2, tc2):
    nf = 0
    i = 0
    if (len(tc1) < len(tc2)):
        nf = len(tc1)
    else:
        nf = len(tc2)
    print('Calculos --> analiticos: {} numericos: {} '.format(len(tc1), len(tc2)))
    print('Tiempo analitico numerico')
    while i < nf:
        print('{0:6d} {1:2.4f} {2:2.4f}'.format(tc1[i], vc1[i], vc2[i]))
        i = i + 1

# Ejecucion del programa
ca(a, W, r, t, e, i, v1, v2)

cn(a, W, r, t, i, v1, vct)

tabla(vc1, tc1, vc2, tc2)

graficar(vc1, vc2, tc1, tc2)

# FIN