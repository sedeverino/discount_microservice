# Discount Microservice

Sistema de gestión de descuentos para la materia Arquitectura de Microservicios.

## Descripción

Este microservicio permite administrar descuentos, ofreciendo endpoints para crear, listar, obtener, actualizar y eliminar descuentos. Está desarrollado completamente en **Python** utilizando **FastAPI** y **SQLAlchemy**.

## Características

- Crear descuentos
- Listar todos los descuentos
- Obtener detalles de un descuento específico
- Actualizar descuentos existentes
- Eliminar descuentos

## Requisitos

- Python 3.10+
- FastAPI
- SQLAlchemy

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/sedeverino/discount_microservice.git

# Instalar dependencias
pip install -r requirements.txt
```

## Uso

```bash
# Ejecutar el microservicio
uvicorn app.main:app --reload
```

Abre tu navegador en [http://localhost:8000/docs](http://localhost:8000/docs) para ver la documentación interactiva.

## API

Consulta [README-API.md](./README-API.md) para la documentación completa de los endpoints y modelos.

## Autor

**sedeverino**
