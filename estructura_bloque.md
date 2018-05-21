# Estructura de un bloque de Bitcoin

### Número mágico (4 bytes)
 - No es algo específico de Bitcoin. Se utilizan en informática para ficheros y protocolos. Identifican el tipo de fichero o estructura de datos. Cuando el cliente de Bitcoin recibe un bloque comprueba este número para identificar la estructura de los datos. Bitcoin utiliza el valor 0xD9B4BEF9.

<p align="center">
  <img src="img_estruct_bloque/magic_number.png?raw=true" alt="Cabecera Bloque Bitcoin"/>
</p>

### Tamaño del bloque (4 bytes)
 - 

### Cabecera (80 bytes)
 - La cabecera del bloque se compone de los siguientes elementos:

|Tamaño (bytes)|Nombre|Tipo|Descripción|
|:---:|:---:|:---:|:---|
|4|version|int32_t|Indica las normas de validación de bloque a seguir.|
|32|hash de la cabecera del bloque anterior|char[32]|El hash SHA256(SHA256()) de la cabecera del bloque anterior.|
|32|hash del merkle root|char[32]|El hash SHA256(SHA256()) del árbol de merkle.|
|4|tiempo|uint32_t|El momento en el que el minero comenzó el hash del encabezado.|
|4|nBits|uint32_t|El hash de la cabecera del bloque debe ser igual o inferior a este valor.|
|4|nonce|uint32_t|Número que los mineros cambian para generar un hash igual o inferior al valor de nBits.|

### Contador de transacciones (1-9 bytes)




###### Fuentes:
 - [What is the magic number](https://bitcoin.stackexchange.com/questions/43189/what-is-the-magic-number-used-in-the-block-structure "What is the magic number")
 - [Bitcon Wiki - Block](https://en.bitcoin.it/wiki/Block "Bitcon Wiki - Block")
