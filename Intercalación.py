import tkinter as tk
from tkinter import messagebox

def intercalacion(lista_a, lista_b):
    resultado = []
    i, j = 0, 0
    while i < len(lista_a) and j < len(lista_b):
        if lista_a[i] <= lista_b[j]:
            resultado.append(lista_a[i])
            i += 1
        else:
            resultado.append(lista_b[j])
            j += 1
    resultado.extend(lista_a[i:])
    resultado.extend(lista_b[j:])
    return resultado

def ejecutar_intercalacion():
    try:
        texto_a = entrada_a.get().strip()
        texto_b = entrada_b.get().strip()

        if not texto_a or not texto_b:
            messagebox.showwarning("Advertencia", "Por favor ingresa datos en ambas listas.")
            return

        lista_a = [float(x) if '.' in x else int(x) for x in texto_a.split(',')]
        lista_b = [float(x) if '.' in x else int(x) for x in texto_b.split(',')]

        # Verificamos si las listas están ordenadas (requisito de la intercalación)
        if lista_a != sorted(lista_a) or lista_b != sorted(lista_b):
            messagebox.showinfo(
                "Aviso",
                "La intercalación requiere listas previamente ordenadas.\nSe ordenarán ambas listas antes de intercalar."
            )
            lista_a.sort()
            lista_b.sort()

        resultado = intercalacion(lista_a, lista_b)

        area_resultado.config(state="normal")
        area_resultado.delete(1.0, tk.END)
        area_resultado.insert(tk.END, f"Lista A ordenada: {lista_a}\n")
        area_resultado.insert(tk.END, f"Lista B ordenada: {lista_b}\n\n")
        area_resultado.insert(tk.END, f"Resultado Intercalado:\n{resultado}")
        area_resultado.config(state="disabled")

    except ValueError:
        messagebox.showerror("Error", "Ingresa solo números separados por comas (ej. 10, 20, 30).")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Método de Intercalación")
ventana.geometry("500x360")
ventana.resizable(False, False)

tk.Label(ventana, text="Método de Intercalación (2 Listas Ordenadas)", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(ventana, text="Sucursal Norte (números separados por coma):").pack()
entrada_a = tk.Entry(ventana, width=55)
entrada_a.insert(0, "120, 340, 560, 890")
entrada_a.pack(pady=5)

tk.Label(ventana, text="Sucursal Sur (números separados por coma):").pack()
entrada_b = tk.Entry(ventana, width=55)
entrada_b.insert(0, "150, 210, 560, 950")
entrada_b.pack(pady=5)

tk.Button(ventana, text="Intercalar Datos", command=ejecutar_intercalacion, bg="#2e7d32", fg="white", font=("Arial", 10, "bold")).pack(pady=10)

area_resultado = tk.Text(ventana, height=8, width=58, state="disabled", bg="#f4f4f4")
area_resultado.pack(pady=5)

ventana.mainloop()
