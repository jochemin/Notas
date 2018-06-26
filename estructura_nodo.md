## Estructura directorio de datos de un nodo completo (Bitcoin Core)

### Localización (rutas por defecto)
- Windows 
  - C:\Users\YourUserName\Appdata\Roaming\Bitcoin
- GNU/Linux
  - ~/.bitcoin/
- MAC
  - ~/Library/Application Support/Bitcoin/

### Estructura

<p align="center">
  <img src="estructura_datos/Picture1.png?raw=true" alt="Estructura ficheros y directorios"/>
</p>

#### Directorio .bitcoin
        .bitcoin
    ├── blocks        # contiene los datos de la cadena de bloques.
    |   └── index     # una base de datos (LevelDB) que contiene metadatos de todos los bloques y su localización en el disco.
    ├── chainstate    # una base de datos (LevelDB) que guarda los UTXO (salidas no gastadas) y algunos metadatos de las transacciones de origen.
    ├── database      # guarda los ficheros "journaling" que utiliza Berkeley DB (BBDD usada por la cartera).
    ├── banlist.dat   # guarda las IPs/subred de los nodos baneados       
    ├── bitcoin.conf  # contiene la configuración del nodo Bitcoin
    ├── bitcoin.pid   # guarda el pid (identificador del proceso) de bitcoind mientras está en ejecución
    ├── debug.log     # el log de bitcoind o bitcoin-qt
    ├── mempool.dat   # las transacciones que se encuentran en la mempool del nodo
    ├── peers.dat     # base de datos con las direcciones IP de los nodos a los que nos hemos conectado
    └── wallet.dat    # la cartera personal (Berkely DB) con las claves y las transacciones.
