## Simulacion de Kojo's Kitchen Problem

### Instrucciones:

La cocina de Kojo es uno de los puestos de comida rapida en un centro comercial. El centro comercial esta abierto entre las 10:00 am y las 9:00 pm cada dia. En este lugar se sirven dos tipos de productos: sandwiches y sushi. Para los objetivos de este proyecto se asumira que existen solo dos tipos de consumidores: unos consumen solo sandwiches y los otros consumen solo productos de la gama del sushi. En Kojo hay dos periodos de hora pico durante un dıa de trabajo; uno entre las 11:30 am y la 1:30 pm, y el otro entre las 5:00 pm y las 7:00 pm. El intervalo de tiempo entre el arribo de un consumidor y el de otro no es homogeneo pero, por conveniencia, se asumira que es homogeneo. El intervalo de tiempo de los segmentos homogeneos, distribuye de forma exponencial. Actualmente dos empleados trabajan todo el dıa preparando sandwiches y sushi para los consumidores. El tiempo de preparacion depende del producto en cuestion. Estos distribuyen de forma uniforme, en un rango de 3 a 5 minutos para la preparacion de sandwiches y entre 5 y 8 minutos para la preparacion de sushi. El administrador de Kojo esta muy feliz con el negocio, pero ha estado recibiendo quejas de los consumidores por la demora de sus peticiones. El esta interesado en explorar algunas opciones de distribucion del personal para reducir el numero de quejas. Su interes esta centrado en comparar la situacion actual con una opcion alternativa donde se emplea un tercer empleado durante los periodos mas ocupados. La medida del desempeno de estas opciones estara dada por el porciento de consumidores que espera mas de 5 minutos por un servicio durante el curso de un dıa de trabajo. Se desea obtener el porciento de consumidores que esperan mas de 5 minutos cuando solo dos empleados estan trabajando y este mismo dato agregando un empleado en las horas pico.

### Solucion:

El metodo creado para la solucion del problema `Kojo's Kitchen` modela la llegada a la tienda con 2 y 3 empleados. A la hora de la apertura de la tienda comienzan a llegar los comensales y estos son atendidos por los empleados siempre que alguno este desocupado, sino esperaran en la cola. De aqui podemos deducir algunas de las variables principales:

- estado de cada empleado `attendand_status`
- cola para la llegada de un cliente a la tienda
- tiempo que se demora cada empleado en atender al cliente (esto es dependiente del tipo de pedido que realiza el cliente ya sea sandwich o sushi).
- listado de los tiempos que se demoro en la cola cada cliente (con esto se calculara el resultado final pedido)

### Proceso para obtener los resultados:

Se debe ejecutar el archivo `main.py`, este ejecutara dos simulaciones del problema, una con 2 empleados y otra con 3. El resultado de esta ejecucion arrojara el total de comensales atendidos y el porcentaje de comensales que estuvieron en la cola mas de 5 minutos.

### Modelacion

El estado inicial del problema sera el siguiente:

- t = 0 #tiempo
- worker_status(i) = NOT_BUSSY
- arrival_time = []
- waiting_time = []
- arrival_t = gen_exp()
- global_t = arrival_t

Si no podemos seguir trabajando(la tienda cerro y no hay mas clientes en cola):

- termina el proceso

Si llega un cliente:

- se generan los tiempos de llegada correspondiente a hora pico o hora regular, agregando al 3er empleado en caso que sea necesario
- global_t = arrival_t
- si algun trabajador esta libre se pasa al ultimo caso

Si un empleado termina una preparacion:

- global_t = min(arrival_t,waiting_t)
- t = arrival_time.dequeue
- se agrega global_t - t como tiempo de espera a la cola `waiting_time`
- se genera el tipo de pedido en dependencia de sushi o sandwish y de aqui se obtiene el tiempo de preparacion
