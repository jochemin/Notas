## Segwit (Historia)<p align="right"><img src="img_segwit/220px-Segwit.svg.png?raw=true" alt="Logo Segwit"/></p>

Este documento cuenta la historia de segwit (testigo segregado), desde su concepción hasta su activación 

#### Comienzos
. Segwit fue desarrollado en ["The Elements Project"](https://github.com/ElementsProject/elementsproject.org "The Elements Project") con Pieter Wuille ([@pwuille](https://twitter.com/pwuille "Pieter Wuille")) como investigador principal, su implementación en Bitcoin suponía un hard fork, posteriormente Luke Dashjr ([@LukeDashjr](https://twitter.com/LukeDashjr "Luke Darshjr")) propuso la forma de implementarlo como soft fork y tras esto se preparó el BIP para integrarlo en Bitcoin.

#### Propuesta Diciembre 2015 ([bip141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki "BIP141"))

. Segwit fue propuesto mediante un BIP (Bitcoin Improvement Proposals) por Eric Lombrozo ([@eric_lombrozo](https://twitter.com/eric_lombrozo "Eric Lombrozo")), Johnson Lau ([@johnsonlau01](https://twitter.com/johnsonlau01 "Johnson Lau")) y Pieter Wuille ([@pwuille](https://twitter.com/pwuille "Pieter Wuille")

. Es un soft fork, es decir, los clientes no actualizados pueden coexistir con las versiones actualizadas.

. La descripción de segwit se divide en 5 BIP:
  - [BIP141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki "BIP141")
    - Descripción general
  - [BIP142](https://github.com/bitcoin/bips/blob/master/bip-0142.mediawiki "BIP142")
    - Describe el formato nativo de las direcciones de pay-to-witness-public-key-hash (P2WPKH) y pay-to-witness-script-hash (P2WSH).
  - [BIP143](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki "BIP143")
    - Entra en detalle en la verificación de transacciones en segwit y como resuelte el crecimiento cuadrático del hash de firmas.
  - [BIP144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki "BIP144")
    - Trata el cambio en los mensajes de red provocados por segwit.
  - [BIP145](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki "BIP145")
    - Cubre los cambios en la llamada JSON-RPC *getblocktemplate* al cliente bitcoin core.

#### [Mejoras](https://bitcoincore.org/en/2016/01/26/segwit-benefits/ "Mejoras Segwit (en)")
  - Soluciona la maleabilidad de las transacciones. ([¿En qué consiste la maleabilidad?](https://bitcointalk.org/index.php?topic=465427.msg5145366#msg5145366 "Maleabilidad de las transacciones"))
  - Aumenta el tamaño del bloque a 4MB en situación ideal, sobre los 2MB en condiciones normales.
  - Facilita la inclusión de nuevos opcodes o modificación de los existentes mendiante versionado de scripts. 
  - Facilita el desarrollo de soluciones de segunda capa.
  - Escalado lineal de las operaciones sighash. La cantidad de datos sobre los que se calcula el hash o comprueba la firma crece cuadráticamente el número de inputs no segwit de una transacción. ([The Megatransaction: Why Does It Take 25 Seconds?](http://rusty.ozlabs.org/?p=522 "La Megatransacción"))
  - Firma de los input. Anteriormente los input no se firmaban lo que suponía un problema para las carteras hardware que tenían que buscar las cantidades de los input en los output gastados con el tiempo que eso supone. 
  - Mayor seguridad en multifirma con P2SH
  - Reduce el crecimiento de los UTXO (Salidas de transacciones no gastadas)

# Documento en proceso
