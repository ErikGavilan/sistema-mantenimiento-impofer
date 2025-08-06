import datetime

ordenes_trabajo = []
contador_serial = 1

def crear_orden(cliente, equipo, descripcion):
    global contador_serial
    fecha_ingreso = datetime.date.today().isoformat()
    orden = {
        "id": len(ordenes_trabajo) + 1,
        "serial": f"{contador_serial:05}",
        "cliente": cliente,
        "equipo": equipo,
        "descripcion": descripcion,
        "fecha_ingreso": fecha_ingreso,
        "fecha_cotizacion": "",
        "fecha_inicio_mantenimiento": "",
        "fecha_entrega": "",
        "duracion_mantenimiento": "",
        "estado": "Por revisión"
    }
    ordenes_trabajo.append(orden)
    contador_serial += 1

def listar_ordenes():
    return ordenes_trabajo

def actualizar_orden(id_orden, nuevo_estado):
    for orden in ordenes_trabajo:
        if orden['id'] == id_orden:
            orden['estado'] = nuevo_estado
            fecha_actual = datetime.date.today().isoformat()

            if nuevo_estado == "Cotización enviada":
                orden['fecha_cotizacion'] = fecha_actual
            elif nuevo_estado == "Ejecutando mantenimiento":
                orden['fecha_inicio_mantenimiento'] = fecha_actual
            elif nuevo_estado == "Finalizado":
                orden['fecha_entrega'] = fecha_actual
                if orden['fecha_inicio_mantenimiento']:
                    fecha_inicio = datetime.datetime.strptime(orden['fecha_inicio_mantenimiento'], "%Y-%m-%d")
                    fecha_entrega = datetime.datetime.strptime(orden['fecha_entrega'], "%Y-%m-%d")
                    orden['duracion_mantenimiento'] = (fecha_entrega - fecha_inicio).days
            return True
    return False

def eliminar_orden(id_orden):
    global ordenes_trabajo
    ordenes_trabajo = [orden for orden in ordenes_trabajo if orden['id'] != id_orden]

def buscar_ordenes(filtro):
    return [orden for orden in ordenes_trabajo if filtro.lower() in orden['cliente'].lower() or filtro in orden['serial']]
