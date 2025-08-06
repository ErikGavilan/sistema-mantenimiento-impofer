# Sistema de Órdenes de Mantenimiento - IMPOFER

Este es un sistema de gestión de órdenes de mantenimiento desarrollado en Python, utilizando **CustomTkinter** para la interfaz gráfica. Permite la creación, actualización, búsqueda y seguimiento de órdenes de trabajo de manera organizada y profesional.

## Características principales
- Registro de órdenes de mantenimiento con datos del cliente y descripción del equipo.
- Asignación automática de serial (5 dígitos, secuencial).
- Estados de seguimiento: Por revisión, En revisión, Cotización enviada, Ejecutando mantenimiento, Finalizada.
- Registro de fechas clave: ingreso, cotización enviada, inicio de mantenimiento, entrega.
- Cálculo automático de duración del mantenimiento.
- Búsqueda de órdenes por nombre del cliente o número de serial.
- Interfaz moderna y profesional con **CustomTkinter**.

## Requisitos
- Python 3.10 o superior
- customtkinter
- git (para clonar el repositorio)

### Instalación de dependencias:
```bash
pip install customtkinter
