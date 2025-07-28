import datetime

ordenes_trabajo = []

def crear_orden():
    cliente = input("Nombre del cliente: ")
    equipo = input("Equipo a mantener: ")
    descripcion = input("Descripción del problema: ")
    fecha = datetime.date.today().isoformat()
    estado = "Pendiente"
    
    orden = {
        "id": len(ordenes_trabajo) + 1,
        "cliente": cliente,
        "equipo": equipo,
        "descripcion": descripcion,
        "fecha": fecha,
        "estado": estado
    }
    ordenes_trabajo.append(orden)
    print(" Orden creada exitosamente.\n")

def listar_ordenes():
    if not ordenes_trabajo:
        print(" No hay órdenes registradas.\n")
        return
    
    print("\n Lista de Órdenes:")
    for orden in ordenes_trabajo:
        print(f"ID: {orden['id']} | Cliente: {orden['cliente']} | Equipo: {orden['equipo']} | Estado: {orden['estado']}")
    print("")

def actualizar_orden():
    listar_ordenes()
    id_buscar = int(input("Ingrese el ID de la orden a actualizar: "))
    for orden in ordenes_trabajo:
        if orden['id'] == id_buscar:
            print(f"Estado actual: {orden['estado']}")
            nuevo_estado = input("Nuevo estado (Pendiente / En proceso / Finalizado): ")
            orden['estado'] = nuevo_estado
            print(" Orden actualizada.\n")
            return
    print(" Orden no encontrada.\n")

def eliminar_orden():
    listar_ordenes()
    id_borrar = int(input("Ingrese el ID de la orden a eliminar: "))
    global ordenes_trabajo
    ordenes_trabajo = [o for o in ordenes_trabajo if o['id'] != id_borrar]
    print(" Orden eliminada.\n")

def menu():
    while True:
        print("====== SISTEMA DE ÓRDENES DE MANTENIMIENTO - IMPOFER ======")
        print("1. Crear nueva orden")
        print("2. Listar órdenes")
        print("3. Actualizar estado de orden")
        print("4. Eliminar orden")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_orden()
        elif opcion == "2":
            listar_ordenes()
        elif opcion == "3":
            actualizar_orden()
        elif opcion == "4":
            eliminar_orden()
        elif opcion == "5":
            print(" Saliendo del sistema.")
            break
        else:
            print(" Opción inválida.\n")

if __name__ == "__main__":
    menu()
