# Discount Microservice API
Microservicio de manejo de descuentos.

## Version: 1.0

**Contact information:**  
Developer: sedeverino  
severino@example.com  

---
## Endpoints

### /discounts/

#### POST
##### Summary

Crear descuento

##### Description

Crea un nuevo descuento en el sistema.

##### Parameters

| Name      | Located in | Description                                 | Required | Schema          |
|-----------|------------|---------------------------------------------|----------|-----------------|
| body      | body       | Datos del descuento a crear                 | Yes      | [DiscountBody](#discountbody) |

##### Responses

| Code | Description      | Schema             |
|------|------------------|--------------------|
| 200  | Descuento creado | [DiscountData](#discountdata) |
| 400  | Bad Request      | [ErrorData](#errordata)  |
| 500  | Internal Error   | [ErrorData](#errordata)  |

---

### /discounts/

#### GET
##### Summary

Listar descuentos

##### Description

Devuelve una lista de todos los descuentos registrados.

##### Parameters

| Name      | Located in | Description                 | Required | Schema |
|-----------|------------|-----------------------------|----------|--------|
| -         | -          | -                           | -        | -      |

##### Responses

| Code | Description         | Schema                        |
|------|---------------------|-------------------------------|
| 200  | Lista de descuentos | [ [DiscountData](#discountdata) ] |
| 500  | Internal Error      | [ErrorData](#errordata)       |

---

### /discounts/{discount_id}

#### GET
##### Summary

Obtener descuento

##### Description

Obtiene la información de un descuento por su ID.

##### Parameters

| Name        | Located in | Description                 | Required | Schema |
|-------------|------------|-----------------------------|----------|--------|
| discount_id | path       | ID del descuento a consultar| Yes      | int    |

##### Responses

| Code | Description       | Schema            |
|------|-------------------|-------------------|
| 200  | Datos del descuento | [DiscountData](#discountdata) |
| 404  | Not Found            | [ErrorData](#errordata)    |
| 500  | Internal Error       | [ErrorData](#errordata)    |

---

### /discounts/{discount_id}

#### PUT
##### Summary

Actualizar descuento

##### Description

Actualiza los datos de un descuento específico.

##### Parameters

| Name        | Located in | Description                  | Required | Schema              |
|-------------|------------|------------------------------|----------|---------------------|
| discount_id | path       | ID del descuento a actualizar| Yes      | int                 |
| body        | body       | Datos nuevos del descuento   | Yes      | [DiscountBody](#discountbody) |

##### Responses

| Code | Description           | Schema            |
|------|-----------------------|-------------------|
| 200  | Descuento actualizado | [DiscountData](#discountdata) |
| 404  | Not Found             | [ErrorData](#errordata)    |
| 400  | Bad Request           | [ErrorData](#errordata)    |
| 500  | Internal Error        | [ErrorData](#errordata)    |

---

### /discounts/{discount_id}

#### DELETE
##### Summary

Eliminar descuento

##### Description

Elimina un descuento del sistema por su ID.

##### Parameters

| Name        | Located in | Description                | Required | Schema |
|-------------|------------|----------------------------|----------|--------|
| discount_id | path       | ID del descuento a eliminar| Yes      | int    |

##### Responses

| Code | Description         | Schema            |
|------|---------------------|-------------------|
| 200  | Eliminado           | { "deleted": true }|
| 404  | Not Found           | [ErrorData](#errordata)    |
| 500  | Internal Error      | [ErrorData](#errordata)    |

---

## Models

#### DiscountBody

| Name        | Type         | Description             | Required |
|-------------|--------------|-------------------------|----------|
| name        | string       | Nombre del descuento    | Yes      |
| value       | number/float | Valor del descuento     | Yes      |
| description | string       | Descripción             | No       |
| [Otros]     | mixed        | Otros campos extra      | No       |

*Nota: El modelo debe especificarse según la implementación real del microservicio.*

#### DiscountData

| Name        | Type         | Description                | Required |
|-------------|--------------|----------------------------|----------|
| id          | int          | ID del descuento           | Yes      |
| name        | string       | Nombre del descuento       | Yes      |
| value       | float        | Valor                      | Yes      |
| description | string       | Descripción                | No       |
| [Otros]     | mixed        | Otros campos extra         | No       |

*Nota: El modelo debe especificarse según la implementación real del microservicio.*

#### ErrorData

| Name   | Type   | Description         | Required |
|--------|--------|---------------------|----------|
| error  | string | Descripción del error| No       |
