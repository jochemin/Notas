# Criptografía en Bitcoin

1. Algoritmo de firma digital de curva elíptica (Elliptic Curve Digital Signature Algorithm (ECDSA))
 - Bitcoin utiliza la curva secp256k1 definida en [este documento (PDF).](http://www.secg.org/collateral/sec2_final.pdf)
 - Bitcoin utiliza el algoritmo para asegurar que los fondos sólo pueden ser gastados por sus dueños legítimos.
 - Conceptos relacionados con ECDSA:
   - Clave privada: número de 256 bit, cualquier número entre 0x1 y 0xFFFF FFFF FFFF FFFF FFFF FFFF FFFF FFFE BAAE DCE6 AF48 A03B BFD2 5E8C D036 4140 es una clave privada válida. Este rango viene definido en el estandar [secp256k1.](https://es.bitcoin.it/wiki/Secp256k1 "secp256k1") 
   - Clave pública: número que se calcula a partir de la clave privada. Este d


###### Fuentes:
 - [¿Por qué se utiliza Criptografía de Curva Elíptica en Bitcoin? ECDSA](https://www.oroyfinanzas.com/2014/01/criptografia-curva-eliptica-bitcoin-por-que-utiliza-ecdsa/) por [Alex Preukschat](https://twitter.com/AlexPreukschat "Alex Preukschat")
 - [SafeCurves: choosing safe curves for elliptic-curve cryptography.](http://safecurves.cr.yp.to/) ][¿Por qué dice que secp256k1 no es segura?](https://bitcointalk.org/index.php?topic=380482.0)
 - [Bitcoin Wiki: Secp256k1](https://es.bitcoin.it/wiki/Secp256k1)

