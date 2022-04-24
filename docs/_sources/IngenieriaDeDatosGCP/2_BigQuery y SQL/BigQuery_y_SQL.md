![](img/BigQuery%20y%20SQL0.png)

# BigQuery y SQL

<span style="color:#CEA6FF">TABLE OF CONTENTS</span>

![](img/BigQuery%20y%20SQL1.png)

<span style="color:#FFFFFF">Modelo Relacional</span>

![](img/BigQuery%20y%20SQL2.png)

![](img/BigQuery%20y%20SQL3.png)

<span style="color:#FFFFFF">Modelo Relacional</span>

<span style="color:#CEA6FF">Modelo Relacional</span>

<span style="color:#252525">Es una estructura de tablas\, las cuales a su vez se relacionan con otras tablas\. Su principal característica es no poseer información repetida de forma innecesaria\, lo que permite adicionar más información sin llegar a afectar la otra almacenada\.</span>

![](img/BigQuery%20y%20SQL4.png)

<span style="color:#CEA6FF">Modelo Relacional</span>

![](img/BigQuery%20y%20SQL5.png)

<span style="color:#252525">También llamada entidad y en algunos textos relación\. Es una estructura compuesta por tuplas \(filas\, registros\) y atributos \(campos\, columnas\)\.</span>

![](img/BigQuery%20y%20SQL6.png)

<span style="color:#CEA6FF">Tipos de relaciones</span>

![](img/BigQuery%20y%20SQL7.png)

<span style="color:#252525"> __Uno a uno__ </span>  <span style="color:#252525">: Cada registro en cada tabla solo aparece una vez\.</span>

![](img/BigQuery%20y%20SQL8.png)

<span style="color:#252525"> __Uno a muchos__ </span>  <span style="color:#252525">: un registro en una tabla puede tener relación con varios elementos de otra tabla\.</span>

<span style="color:#CEA6FF">Tipos de relaciones</span>

<span style="color:#252525"> __Muchos a muchos__ </span>  <span style="color:#252525">: Cuando uno o más registros en una tabla puede tener una relación con uno o más elementos de otra tabla</span>

![](img/BigQuery%20y%20SQL9.png)

<span style="color:#252525"> __Clave primaria PK: __ </span>  <span style="color:#252525">también llamada llave primaria o primary key\, hace que el registro sea unívoco y obligatoriamente no nulo\.</span>

<span style="color:#252525"> __Clave foránea FK: __ </span>  <span style="color:#252525">también llamada foreign key\, clave secundaria o clave externa\, puede ser \-o no\- una clave primaria dentro de la tabla\. Su característica es que es el punto de enlace con otra tabla donde está\, es primary key\.</span>

<span style="color:#252525"> __Clave índice: __ </span>  <span style="color:#252525">es un campo que facilita la búsqueda dentro de una tabla\. Generalmente son campos primary key\.</span>

![](img/BigQuery%20y%20SQL10.png)

![](img/BigQuery%20y%20SQL11.png)

<span style="color:#CEA6FF">Sentencias y Estructuras</span>

* <span style="color:#000000">Existen múltiples sentencias en SQL que podemos utilizar para manipular nuestros datos\, las más importantes son:</span>
* <span style="color:#000000"> __Data Manipulation Language \(DML\)__ </span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __Select:__ </span>  <span style="color:#000000">  Consultar registros de una o varias tablas\.</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __Delete:__ </span>  <span style="color:#000000"> Eliminar registros de una tabla\. </span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __Insert:__ </span>  <span style="color:#000000"> Insertar registros en una tabla\.</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __Update:__ </span>  <span style="color:#000000"> Modificar registros de una tabla\.</span>
* <span style="color:#000000">Otra cláusula muy utilizada es: </span>  <span style="color:#000000"> __“Where”__ </span>  <span style="color:#000000">\. Con esta sentencia podemos seleccionar qué filtro aplicar a nuestros datos\. </span>

<span style="color:#CEA6FF">Sentencias y Estructuras</span>

<span style="color:#000000"> __Data Definition Language \(DDL\)__ </span>

* <span style="color:#000000">Las sentencias más importantes son:</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __CREATE DATABASE: __ </span>  <span style="color:#000000">Crea una nueva base de datos\.</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __ALTER DATABASE:__ </span>  <span style="color:#000000"> Modifica una base de datos\.</span>
        * <span style="color:#000000"> __ __ </span>  <span style="color:#000000"> __CREATE TABLE: __ </span>  <span style="color:#000000">Crea una nueva tabla\.</span>
        * <span style="color:#000000"> __ __ </span>  <span style="color:#000000"> __ALTER TABLE: __ </span>  <span style="color:#000000">Modifica una tabla\.</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __DROP TABLE: __ </span>  <span style="color:#000000">Eliimina una tabla\.</span>

<span style="color:#CEA6FF">Sentencias y Estructuras</span>

<span style="color:#000000"> __Data Control Language \(DCL\)__ </span>

* <span style="color:#000000">Las sentencias más importantes son:</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __GRANT: __ </span>  <span style="color:#000000">autoriza a uno o más usuarios a realizar una operación o conjunto de operaciones sobre un objeto\.</span>
        * <span style="color:#000000"> </span>  <span style="color:#000000"> __REVOKE: __ </span>  <span style="color:#000000">elimina una concesión\, que puede ser la concesión predeterminada\.</span>

<span style="color:#252525">Para consultar datos de una tabla\, deberemos usar la instrucción SELECT de SQL\. La declaración SELECT contiene la sintaxis para seleccionar columnas\, seleccionar filas\, agrupar datos\, unir tablas y realizar cálculos simples\.</span>

<span style="color:#252525">A continuación\, se ilustra la sintaxis básica de la declaración SELECT que recupera datos de una sola tabla:</span>

<span style="color:#252525">SELECT nombre\_de\_columna</span>

<span style="color:#252525">FROM nombre\_de\_tabla</span>

<span style="color:#252525">En caso de que deseemos consultar datos de todas las columnas de una tabla\, podemos usar el operador asterisco \(\*\)\, así:</span>

<span style="color:#252525">SELECT \*</span>

<span style="color:#252525">FROM nombre\_de\_tabla</span>

<span style="color:#252525">Importante: SQL no distingue entre mayúsculas y minúsculas\, esto significa que las palabras clave SELECT y select se interpretan de igual modo sin problemas</span>  <span style="color:#434343">\.</span>

<span style="color:#252525">Cuando utilizamos la instrucción SELECT para consultar datos de una tabla\, el orden en que aparecen las filas en el conjunto de resultados puede no ser el esperado</span>  <span style="color:#434343">\. </span>

<span style="color:#252525">Para especificar exactamente el orden de las filas en el conjunto de resultados\, deberemos agregar una cláusula ORDER BY en la declaración del SELECT de la siguiente manera:</span>

<span style="color:#252525">SELECT nombre\_de\_columna</span>

<span style="color:#252525">FROM nombre\_de\_tabla</span>

<span style="color:#252525">ORDER BY nombre\_de\_columna ASC</span>

<span style="color:#252525">La cláusula ORDER BY aparece después de la cláusula FROM\. En caso de que la declaración SELECT contenga una cláusula WHERE\, la cláusula ORDER BY debe aparecer después de la cláusula WHERE\. </span>

<span style="color:#252525">Para ordenar el conjunto de resultados\, tendremos que elegir el tipo de ordenación\, en base a las siguientes consideraciones:</span>

<span style="color:#252525">Ascendente \(ASC\)</span>

<span style="color:#252525">Descendente \(DESC\)</span>

<span style="color:#252525">Aclaración: Si no especifica el orden de clasificación\, por defecto es ascendente\.</span>

<span style="color:#252525">Cuando consultamos nuestros datos\, puede llegar a pasar que tengamos registros duplicados dentro de los resultados de la query\. Para eliminar los duplicados deberemos utilizar el operador DISTINCT en la cláusula SELECT de la siguiente manera:</span>

<span style="color:#252525">SELECT DISTINCT nombre\_de\_columna</span>

<span style="color:#252525">FROM nombre\_de\_tabla</span>

<span style="color:#252525">ORDER BY nombre\_de\_columna ASC</span>

<span style="color:#252525">Para seleccionar ciertas filas de una tabla\, se usa la cláusula WHERE en la declaración SELECT\. A continuación\, se ilustra la sintaxis de la cláusula WHERE en la declaración SELECT:</span>

<span style="color:#252525">SELECT nombre\_de\_columna</span>

<span style="color:#252525">FROM nombre\_de\_tabla</span>

<span style="color:#252525">WHERE condición</span>

<span style="color:#252525">Importante: </span>

<span style="color:#252525">La cláusula WHERE aparece inmediatamente después de la cláusula FROM y contiene una o más expresiones lógicas que evalúan cada fila de la tabla\.</span>

<span style="color:#CEA6FF">OPERADORES DE COMPARACIÓN</span>

<span style="color:#252525">La forma más básica de filtrar datos es utilizar operadores de comparación\. La siguiente tabla muestra los operadores de comparación SQL:</span>

![](img/BigQuery%20y%20SQL12.png)

<span style="color:#CEA6FF">OPERADORES LÓGICOS</span>

<span style="color:#252525">La siguiente tabla muestra los operadores lógicos de SQL:</span>

![](img/BigQuery%20y%20SQL13.png)

![](img/BigQuery%20y%20SQL14.png)

![](img/BigQuery%20y%20SQL15.png)

![](img/BigQuery%20y%20SQL16.png)

<span style="color:#CEA6FF">¿Qué otro servicios importantes existen en GCP?</span>

<span style="color:#252525"> __Cloud Storage__ </span>  <span style="color:#252525">: Servicio para almacenar y recuperar cualquier cantidad de datos en todo el mundo y en cualquier momento\. Cloud Storage se puede utilizar en varias situaciones\, como la entrega de contenido de un sitio web\, el almacenamiento de datos con fines de archivo y recuperación ante desastres\, o la distribución de grandes objetos de datos a los usuarios a través de una descarga directa\.</span>

![](img/BigQuery%20y%20SQL17.png)

<span style="color:#CEA6FF">¿Qué otro servicios importantes existen en GCP?</span>

<span style="color:#252525"> __Compute Engine: __ </span>  <span style="color:#252525">Servicio de computación seguro y personalizable con el que podemos crear y ejecutar máquinas virtuales en la infraestructura de Google\. Los nuevos clientes reciben 300 USD en crédito gratis para invertirlos en Google Cloud\. Todos los clientes tienen acceso a una máquina de uso general \(instancia f1\-micro\) cada mes de forma gratuita \(Cloud Shell\)\.</span>

![](img/BigQuery%20y%20SQL18.png)

<span style="color:#252525">OTROS\! </span>

<span style="color:#252525">Cloud Functions\.</span>

<span style="color:#252525">Cloud SQL\.</span>

<span style="color:#252525">Data Flow\.</span>

<span style="color:#CEA6FF">Buenas Prácticas y Recomendaciones</span>

<span style="color:#252525"> __Centrarse en el negocio: __ </span>  <span style="color:#252525">Hay que concentrarse en la identificación de los requerimientos del negocio y su valor asociado\, y usar estos esfuerzos para desarrollar relaciones sólidas con el negocio\.</span>

<span style="color:#252525"> __Construir una infraestructura de información adecuada: __ </span>  <span style="color:#252525">Diseñar una base de información única\, integrada\, fácil de usar\, de alto rendimiento donde se reflejará la amplia gama de requerimientos de negocio identificados en la empresa\. </span>

<span style="color:#252525"> __Capacitación del Personal: __ </span>  <span style="color:#252525">Aplicar conceptos vinculados al mundo del Data Literacy y la alfabetización de datos</span>  <span style="color:#28262B">\.</span>

<span style="color:#CEA6FF">Políticas de costos en GCP</span>

<span style="color:#252525"> __Trabajar con Cuotas:__ </span>

<span style="color:#252525">Google Cloud aplica cuotas sobre el uso de recursos para propietarios de proyectos\, lo que establece un límite estricto en relación con qué tanto puede usar tu proyecto un recurso particular de Google Cloud\. A continuación\, se muestran las cuotas que limitan dos tipos de uso de recursos:</span>

<span style="color:#252525"> </span>  <span style="color:#252525">Cuota de tarifa\, como la cantidad de solicitudes a la API por día\. Esta cuota se restablece luego de un tiempo especificado\, como un minuto o un día\.</span>

<span style="color:#252525"> </span>  <span style="color:#252525">Cuota de asignación\, como el número de máquinas virtuales o balanceadores de cargas que usa tu proyecto\. Esta cuota no se restablece con el tiempo y debe retirarse de manera explícita cuando ya no quieras usar el recurso\, por ejemplo\, mediante el borrado de un clúster de GKE</span>

![](img/BigQuery%20y%20SQL19.png)

