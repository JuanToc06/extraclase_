import matplotlib.pyplot as plt

# Datos de la tabla
trimestres = ["1er trimestre", "2do trimestre", "3er trimestre"]
gastos = [
    ["Agua", 120, 85, 180],
    ["Luz", 420, 105, 225],
    ["Gas", 360, 90, 160],
]

# Obtener las categorías y los valores de gastos
categorias = [item[0] for item in gastos]
valores_agua = [item[1] for item in gastos]
valores_luz = [item[2] for item in gastos]
valores_gas = [item[3] for item in gastos]

# Crear gráfica de barras
fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
x = range(len(categorias))
ancho_barras = 0.2

# Crear barras para cada trimestre
ax.bar(x, valores_agua, width=ancho_barras, label="Agua")
ax.bar([pos + ancho_barras for pos in x], valores_luz, width=ancho_barras, label="Luz")
ax.bar([pos + 2*ancho_barras for pos in x], valores_gas, width=ancho_barras, label="Gas")

ax.set_xlabel('Categorías')
ax.set_ylabel('Gastos')
ax.set_xticks([pos + ancho_barras for pos in x])
ax.set_xticklabels(categorias)
ax.legend()

plt.title("Gastos Trimestrales")
plt.show()
