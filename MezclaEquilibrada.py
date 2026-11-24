import tkinter as tk
from tkinter import messagebox

def obtener_corridas_naturales(datos):
    if not datos:
        return []
    corridas = []
    corrida_actual = [datos[0]]

    for i in range(1, len(datos)):
        if datos[i] >= datos[i - 1]:
            corrida_actual.append(datos[i])
        else:
            corridas.append(corrida_actual)
            corrida_actual = [datos[i]]
    corridas.append(corrida_actual)
    return corridas

def fusionar_dos_listas(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res

def mezcla_equilibrada_pasos(datos):
    historial = []
    iteracion = 1

    while True:
        corridas = obtener_corridas_naturales(datos)
        historial.append(f"Pasada {iteracion} - Corridas detectadas: {corridas}")

        if len(corridas) <= 1:
            return (corridas[0] if corridas else []), historial

        f1 = corridas[0::2]
        f2 = corridas[1::2]

        datos_fusionados = []
        for idx in range(len(f1)):
            if idx < len(f2):
                datos_fusionados.extend(fusionar_dos_listas(f1[idx], f2[idx]))
            else:
                datos_fusionados.extend(f1[idx])

        datos = datos_fusionados
        iteracion += 1

def ejecutar_mezcla_equilibrada():
    try:
        texto = entrada_datos.get().strip()
        if not texto:
            messagebox.showwarning("Advertencia", "Por favor ingresa una lista de números.")
            return

        datos = [float(x) if '.' in x else int(x) for x in texto.split(',')]
        ordenados, pasos = mezcla_equilibrada_pasos(datos)

        area_resultado.config(state="normal")
        area_resultado.delete(1.0, tk.END)
        area_resultado.insert(tk.END, f"Folios recibidos: {datos}\n\n")
        for paso in pasos:
            area_resultado.insert(tk.END, paso + "\n")
        area_resultado.insert(tk.END, f"\nResultado Final Ordenado:\n{ordenados}")
        area_resultado.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas (ej. 10, 25, 40, 5, 18).")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Método de Mezcla Equilibrada")
ventana.geometry("560x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Método de Mezcla Equilibrada (Natural Merge)", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(ventana, text="Ingresa folios parcialmente ordenados (separados por coma):").pack()
entrada_datos = tk.Entry(ventana, width=62)
entrada_datos.insert(0, "10, 25, 40, 5, 18, 30, 12, 50")
entrada_datos.pack(pady=5)

tk.Button(ventana, text="Ordenar por Mezcla Equilibrada", command=ejecutar_mezcla_equilibrada, bg="#6a1b9a", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

area_resultado = tk.Text(ventana, height=12, width=65, state="disabled", bg="#f4f4f4")
area_resultado.pack(pady=5)

ventana.mainloop()
