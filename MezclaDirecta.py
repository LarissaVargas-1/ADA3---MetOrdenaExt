import tkinter as tk
from tkinter import messagebox

def intercalar_bloques(izq, der):
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def mezcla_directa_pasos(datos):
    n = len(datos)
    longitud_bloque = 1
    historial = []

    while longitud_bloque < n:
        archivo_auxiliar = []
        for i in range(0, n, 2 * longitud_bloque):
            bloque_1 = datos[i : i + longitud_bloque]
            bloque_2 = datos[i + longitud_bloque : i + 2 * longitud_bloque]
            archivo_auxiliar.extend(intercalar_bloques(bloque_1, bloque_2))

        datos = archivo_auxiliar
        historial.append(f"Bloque tamaño {longitud_bloque}: {datos}")
        longitud_bloque *= 2

    return datos, historial

def ejecutar_mezcla_directa():
    try:
        texto = entrada_datos.get().strip()
        if not texto:
            messagebox.showwarning("Advertencia", "Por favor ingresa una lista de números.")
            return

        datos = [float(x) if '.' in x else int(x) for x in texto.split(',')]
        ordenados, pasos = mezcla_directa_pasos(datos)

        area_resultado.config(state="normal")
        area_resultado.delete(1.0, tk.END)
        area_resultado.insert(tk.END, f"Original: {datos}\n\n")
        for paso in pasos:
            area_resultado.insert(tk.END, paso + "\n")
        area_resultado.insert(tk.END, f"\nResultado Final Ordenado:\n{ordenados}")
        area_resultado.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas (ej. 28.5, 19.2, 33.0).")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Método de Mezcla Directa")
ventana.geometry("540x400")
ventana.resizable(False, False)

tk.Label(ventana, text="Método de Mezcla Directa (Straight Merge)", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(ventana, text="Ingresa registros desordenados (separados por coma):").pack()
entrada_datos = tk.Entry(ventana, width=60)
entrada_datos.insert(0, "28.5, 19.2, 33.0, 22.1, 18.4, 30.8, 25.0")
entrada_datos.pack(pady=5)

tk.Button(ventana, text="Ordenar por Mezcla Directa", command=ejecutar_mezcla_directa, bg="#1565c0", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

area_resultado = tk.Text(ventana, height=12, width=62, state="disabled", bg="#f4f4f4")
area_resultado.pack(pady=5)

ventana.mainloop()
