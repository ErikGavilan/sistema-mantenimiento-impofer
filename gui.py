import customtkinter as ctk
from tkinter import messagebox
import backend

def crear_orden_gui():
    cliente = entry_cliente.get()
    equipo = entry_equipo.get()
    descripcion = entry_descripcion.get()

    if not cliente or not equipo or not descripcion:
        messagebox.showerror("Error", "Debe completar todos los campos.")
        return

    backend.crear_orden(cliente, equipo, descripcion)

    entry_cliente.delete(0, ctk.END)
    entry_equipo.delete(0, ctk.END)
    entry_descripcion.delete(0, ctk.END)

    actualizar_lista_gui()
    messagebox.showinfo("Éxito", "Orden creada exitosamente.")

def actualizar_lista_gui(ordenes=None):
    lista_ordenes.delete("1.0", ctk.END)
    if ordenes is None:
        ordenes = backend.listar_ordenes()
    for orden in ordenes:
        texto = (f"ID: {orden['id']} | Serial: {orden['serial']} | Cliente: {orden['cliente']} | Equipo: {orden['equipo']} | "
                 f"Estado: {orden['estado']} | Ingreso: {orden['fecha_ingreso']} | Cotización: {orden['fecha_cotizacion']} | "
                 f"Inicio Mto: {orden['fecha_inicio_mantenimiento']} | Entrega: {orden['fecha_entrega']} | "
                 f"Duración: {orden['duracion_mantenimiento']} días")
        lista_ordenes.insert(ctk.END, texto + "\n")

def actualizar_estado_gui():
    seleccion = lista_ordenes.get("insert", "insert lineend")
    if not seleccion.strip():
        messagebox.showerror("Error", "Seleccione una orden para actualizar.")
        return

    id_text = seleccion.split('|')[0].strip()
    id_orden = int(id_text.split(':')[1])

    nuevo_estado = estado_var.get()
    backend.actualizar_orden(id_orden, nuevo_estado)
    actualizar_lista_gui()
    messagebox.showinfo("Éxito", "Estado actualizado correctamente.")

def eliminar_orden_gui():
    seleccion = lista_ordenes.get("insert", "insert lineend")
    if not seleccion.strip():
        messagebox.showerror("Error", "Seleccione una orden para eliminar.")
        return

    id_text = seleccion.split('|')[0].strip()
    id_orden = int(id_text.split(':')[1])

    backend.eliminar_orden(id_orden)
    actualizar_lista_gui()
    messagebox.showinfo("Éxito", "Orden eliminada correctamente.")

def buscar_orden_gui():
    filtro = entry_busqueda.get()
    resultados = backend.buscar_ordenes(filtro)
    if resultados:
        actualizar_lista_gui(resultados)
    else:
        messagebox.showinfo("Sin resultados", "No se encontraron órdenes con ese filtro.")

def iniciar_gui():
    global entry_cliente, entry_equipo, entry_descripcion, lista_ordenes, estado_var, entry_busqueda

    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("blue")

    ventana = ctk.CTk()
    ventana.title("Sistema de Órdenes de Trabajo - IMPOFER")
    ventana.geometry("1200x700")

    frame_registro = ctk.CTkFrame(master=ventana)
    frame_registro.pack(padx=20, pady=10, fill="x")

    label_titulo = ctk.CTkLabel(frame_registro, text="Registrar Nueva Orden", font=("Arial", 20))
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    entry_cliente = ctk.CTkEntry(frame_registro, placeholder_text="Nombre del Cliente", width=400)
    entry_cliente.grid(row=1, column=0, padx=10, pady=5)

    entry_equipo = ctk.CTkEntry(frame_registro, placeholder_text="Equipo", width=400)
    entry_equipo.grid(row=2, column=0, padx=10, pady=5)

    entry_descripcion = ctk.CTkEntry(frame_registro, placeholder_text="Descripción del Problema", width=400)
    entry_descripcion.grid(row=3, column=0, padx=10, pady=5)

    btn_crear = ctk.CTkButton(frame_registro, text="Crear Orden", command=crear_orden_gui, width=200)
    btn_crear.grid(row=4, column=0, padx=10, pady=10)

    frame_lista = ctk.CTkFrame(master=ventana)
    frame_lista.pack(padx=20, pady=10, fill="both", expand=True)

    lista_ordenes = ctk.CTkTextbox(frame_lista, width=1100, height=300)
    lista_ordenes.pack(padx=10, pady=10, fill="both", expand=True)

    frame_estado = ctk.CTkFrame(master=ventana)
    frame_estado.pack(padx=20, pady=10, fill="x")

    estado_var = ctk.StringVar(value="Por revisión")
    opciones_estado = ["Por revisión", "En revisión", "Cotización enviada", "Ejecutando mantenimiento", "Finalizado"]

    dropdown_estado = ctk.CTkOptionMenu(frame_estado, values=opciones_estado, variable=estado_var)
    dropdown_estado.grid(row=0, column=0, padx=10, pady=10)

    btn_actualizar_estado = ctk.CTkButton(frame_estado, text="Actualizar Estado", command=actualizar_estado_gui)
    btn_actualizar_estado.grid(row=0, column=1, padx=10, pady=10)

    frame_busqueda = ctk.CTkFrame(master=ventana)
    frame_busqueda.pack(padx=20, pady=10, fill="x")

    entry_busqueda = ctk.CTkEntry(frame_busqueda, placeholder_text="Buscar por nombre o serial", width=400)
    entry_busqueda.grid(row=0, column=0, padx=10, pady=10)

    btn_buscar = ctk.CTkButton(frame_busqueda, text="Buscar", command=buscar_orden_gui)
    btn_buscar.grid(row=0, column=1, padx=10, pady=10)

    btn_eliminar = ctk.CTkButton(frame_busqueda, text="Eliminar Orden Seleccionada", command=eliminar_orden_gui, fg_color="red")
    btn_eliminar.grid(row=0, column=2, padx=10, pady=10)

    actualizar_lista_gui()

    ventana.mainloop()
