# Inciso A y B

El cliente correspondiente es client.py y el servidor es sync_server.py.

El tiempo de ejecucion fue tomado solo para la transaccion. Sus tiempos de ejecucion en milisegundos fueron los siguientes:

| Nro              | Tiempo de ejecucion para el servidor | Tiempo de ejecucion para el cliente |
| ---------------- | ------------------------------------ | ----------------------------------- |
| 01               | 0.446                                | 0.670                               |
| 02               | 0.323                                | 0.462                               |
| 03               | 0.247                                | 0.554                               |
| 04               | 0.299                                | 0.469                               |
| 05               | 0.331                                | 0.513                               |
| 06               | 0.334                                | 0.512                               |
| 07               | 0.298                                | 0.552                               |
| 08               | 0.369                                | 0.520                               |
| 09               | 0.234                                | 0.350                               |
| 10               | 0.181                                | 0.278                               |
| Mediana          | 0.311                                | 0.513                               |
| Media Geometrica | 0.298                                | 0.475                               |

# Inciso C

El cliente correspondiente sigue siendo client.py y el servidor es async_server.py

La parte mas apropiada para volverse asincrona son las transacciones entre cliente servidor una vez establecida la conexion, las cuales estan encapsuladas en la corutina handle_client.

En esta parte se uso la version asincrona de accept(), debido a que el accept() sincrono bloquea el loop de eventos.

El tiempo de ejecucion fue tomado solo para la transaccion. Sus tiempos de ejecucion en milisegundos fueron los siguientes:

| Nro              | Tiempo de ejecucion para el servidor | Tiempo de ejecucion para el cliente |
| ---------------- | ------------------------------------ | ----------------------------------- |
| 01               | 0.353                                | 0.738                               |
| 02               | 0.375                                | 0.831                               |
| 03               | 0.358                                | 0.842                               |
| 04               | 0.371                                | 0.827                               |
| 05               | 0.364                                | 0.838                               |
| 06               | 0.373                                | 0.868                               |
| 07               | 0.393                                | 0.829                               |
| 08               | 0.350                                | 0.795                               |
| 09               | 0.447                                | 0.990                               |
| 10               | 0.478                                | 0.952                               |
| Mediana          | 0.372                                | 0.835                               |
| Media Geometrica | 0.384                                | 0.848                               |

# Inciso D

Las dos diferencias principales entre ambas versiones son el tiempo de ejecucion de la transaccion y la capacidad de la version asincrona de atender multiples requests al mismo tiempo.

| Version | Tiempo de transaccion para el servidor: Mediana | Tiempo de transaccion para el servidor: Media Geometrica |
| ------- | ----------------------------------------------- | -------------------------------------------------------- |
| Sync    | 0.311                                           | 0.372                                                    |
| Async   | 0.298                                           | 0.384                                                    |

La diferencia en tiempo de ejecucion puede ser facilmente explicado debido a que la version asincrona requiere un loop de eventos e ir alternando entre corutinas constantemente, lo que, naturalmente, aumenta su tiempo de ejecucion respecto a la version sincrona que ejecuta instrucciones secuencialmente

# Inciso E

La posibilidad de atender multiples requests a la vez viene de que, debido al loop de eventos, el proceso alterna entre escuchar nuevas requests y procesar la o las que tiene pendientes.

Se puede demostrar que la version asincrona puede atender multiples requests a la vez mediante las siguientes condiciones:

- Se agrega un asyncio.sleep(5) en medio de la transaccion en el servidor async
- Se agrega un time.sleep(5) en medio de la transaccion en el servidor sync

Estas condiciones garantizan que de tiempo a enviar dos solicitudes desde dos terminales diferentes.

Observacion: ambos servidores logean las conexiones, sendall y recv que realizan

Entonces, observamos los logs:

## Ejemplo de Log de la version sincrona

```
Listening at localhost:5000
========================================================
Connection accepted from 127.0.0.1:41714
========================================================
Received: 20230000
========================================================
Sent: 10.181818181818182
========================================================
Connection accepted from 127.0.0.1:41718
========================================================
Received: 20230000
========================================================
Sent: 10.181818181818182
```

Como podemos ver, a pesar de que las requests entre los clientes fueron enviadas a la vez (con 0.5 - 1 s de diferencia), fueron atendidas de forma secuencial:

```
Conn1 => Req1 => Res1 => Con2 => Req2 => Res2
```

## Ejemplo de Log de la version asincrona

```
Listening at localhost:5000
========================================================
Connection accepted from 127.0.0.1:40502
========================================================
Received: 20230000
========================================================
Connection accepted from 127.0.0.1:40518
========================================================
Received: 20230000
========================================================
Sent: 10.181818181818182
========================================================
Sent: 10.181818181818182
```

Como podemos ver, a diferencia de la version sincrona, ambas requests fueron atendidas en simultaneo:

```
Conn1 => Req1 => Conn2 => Req2 => Res1 => Res2
```

Finalmente, se demuestra que la version asincrona es capaz de recibir mas de una solicitud a la vez
