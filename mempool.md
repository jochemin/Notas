#### ¿Qué ocurre cuando se llena el espacio reservado para la mempool en un nodo?
Los nodos pueden configurar un tamaño máximo para la mempool mediante el fichero de configuración ``` -maxmempool=<n> ``` si no se configura este parámetro se aplica el valor por defecto que con el cliente Bitcoin Core 0.18.0 (02/05/2019) es de 300MB<sup>1</sup>.

Si el tamaño máximo de la mempool se alcanza, se aplica una comisión mínima para aceptar transacciones nuevas en la mempool y se eliminan de esta todas aquellas con una comisión inferior<sup>1</sup>.




<sup>1</sup> https://github.com/bitcoin/bitcoin/blob/c536dfbcb00fb15963bf5d507b7017c241718bf6/src/policy/policy.h#L32
<sup>2</sup> https://github.com/bitcoin/bitcoin/blob/master/src/validation.cpp#L741
