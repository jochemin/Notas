<p align="right">
  <img src="img_segwit/220px-Segwit.svg.png?raw=true" alt="Logo Segwit"/>
</p>

## Segwit (Historia)

Este documento cuenta la historia de segwit (testigo segregado), desde su concepción hasta su activación 

#### Comienzos
Segwit fue desarrollado en ["The Elements Project"](https://github.com/ElementsProject/elementsproject.org "The Elements Project") con Pieter Wuille ([@pwuille](https://twitter.com/pwuille "Pieter Wuille")) como investigador principal, su implementación en Bitcoin suponía un hard fork, posteriormente Luke Dashjr ([@LukeDashjr](https://twitter.com/LukeDashjr "Luke Darshjr")) propuso la forma de implementarlo como soft fork y tras esto se preparó el BIP para integrarlo en Bitcoin.

#### ¿Qué es segwit?
Segwit es una actualización del protocolo Bitcoin que modifica la estructura de las transacciones, guarda toda la información susceptible de ser maleable a un nuevo campo "witness data". El id de la transacción se calcula sin contar con este campo por lo que posteriormente no se puede modificar.

<p align="center">
  <img src="img_segwit/transaction.png?raw=true" alt="Transacción Segwit"/>
</p>


#### Propuesta Diciembre 2015 ([bip141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki "BIP141"))

Segwit fue propuesto mediante un BIP (Bitcoin Improvement Proposals) por Eric Lombrozo ([@eric_lombrozo](https://twitter.com/eric_lombrozo "Eric Lombrozo")), Johnson Lau ([@johnsonlau01](https://twitter.com/johnsonlau01 "Johnson Lau")) y Pieter Wuille ([@pwuille](https://twitter.com/pwuille "Pieter Wuille"))

Es un soft fork, es decir, los clientes no actualizados pueden coexistir con las versiones actualizadas.

La descripción de segwit se divide en 5 BIP:
 - [BIP141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki "BIP141") - Activado el 24 de Agosto de 2017
   - Descripción general
 - [BIP142](https://github.com/bitcoin/bips/blob/master/bip-0142.mediawiki "BIP142") - Reemplazado por el BIP143
   - Describe el formato nativo de las direcciones de pay-to-witness-public-key-hash (P2WPKH) y pay-to-witness-script-hash (P2WSH).
 - [BIP143](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki "BIP143") - Activado el 24 de Agosto de 2017
   - Entra en detalle en la verificación de transacciones en segwit y como resuelte el crecimiento cuadrático del hash de firmas.
 - [BIP144](https://github.com/bitcoin/bips/blob/master/bip-0144.mediawiki "BIP144") - Activado el 24 de Agosto de 2017
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

#### Críticas
  - Jeff Garzik ([@jgarzik](https://twitter.com/jgarzik "Jeff Garzik")) consideró insuficiente a SegWit como solución de escalado.
  - Mike Hearn, desarrollador principal del cliente [Bitcoin XT](https://bitcoinxt.software/ "Bitcoin XT") calificó a SegWit como "un truco contable", dejó el desarrollo de Bitcoin poco después.
  - Jonathan Toomim, desarrollado del cliente [Bitcoin Classic](https://bitcoinclassic.com/ "Bitcoin Classic") comentó que SegWit era "feo y raro", sugirió que sería mejor implementarlo como hard fork.
  - Peter Todd ([@peterktodd](https://twitter.com/peterktodd "Peter Todd")) tenía sus dudas en partícular en lo respectivo a minería. [[1](https://petertodd.org/2016/segwit-consensus-critical-code-review#peer-to-peer-networking)] [[2](https://www.mail-archive.com/bitcoin-dev@lists.linuxfoundation.org/msg03178.html)]

#### Entorno
Mientras SegWit se desarrollaba en la comunidad Bitcoin había tensiones en cuanto al tamaño del bloque (1MB), varios mineros y compañias Bitcoin encabezados por Bitcoin Classic preparaban un hard fork para aumentar el tamaño a 2 MB. [[1]](https://web.archive.org/web/20160129090054/https://bitcoinclassic.com/ "HF 2MB") 

El 21 de Febrero de 2016 en una reunión en Hong Kong entre varios desarrolladores de Bitcoin Core, operadores de agrupaciones mineras y miembros de la industria Bitcoin para discutir el problema de escalabilidad se llegó a un acuerdo conocido como ["El acuerdo de la mesa redonda de Bitcoin"](https://medium.com/@bitcoinroundtable/bitcoin-roundtable-consensus-266d475a61ff "El acuerdo de la mesa redonda de Bitcoin"), ese acuerdo consistió en estos puntos:
  - SegWit se está desarrollando como soft fork y se lanzará en los próximos 2 meses.
  - Se trabajará públicamente junto a toda la comunidad de desarrolladores del protocolo Bitcoin en un hard fork basado en las mejoras de SegWit. Los desarrolladores de Bitcoin Core tendrán una implementación de dicho hard fork para presentar 3 meses después del lanzamiento de SegWit.
  - Este hard fork incluirá características que se están tratando como aumentar el tamaño de los datos no testigos (non witness) a los 2 MB y sólo será adoptado si hay un acuerdo de la mayoría la comunidad Bitcoin.
  - Los mineros utilizarán SegWit cuando el hard fork se implemente en el cliente Bitcoin Core.
  - Solo se utilizarán sistemas compatibles con el consenso de Bitcoin Core que contendrán SegWit y el hard fork.
  - Se seguirán investigando tecnologías para usar el espacio en los bloques más eficientemente como las firmas [Schnorr.](https://bitcoinmagazine.com/articles/the-power-of-schnorr-the-signature-algorithm-to-increase-bitcoin-s-scale-and-privacy-1460642496/ "Firmas Schnorr")

Mese más tarde, en Julio de 2016 tuvo lugar una [reunión](https://bitcoinmagazine.com/articles/bitcoin-miners-and-developers-meet-in-california-to-improve-communications-1470158657/ "Reunión Julio") entre desarrolladores de Bitcoin Core y operadores de agrupaciones mineras en California. Los desarrolladores de Bitcoin Core salieron de la reunión convencidos de que SegWit sería activado por los mineros.

#### Lanzamiento
SegWit se incluyó en la versión 0.13.1 del cliente [Bitcoin Core](https://github.com/bitcoin/bitcoin "Bitcoin Core"), también se implementó en otros clientes como [Knots](https://github.com/bitcoinknots/bitcoin "Bitcoin Knots") o [Bcoin](https://github.com/bcoin-org/bcoin "Bcoin")

Para activar SegWit se utilizó un metodo llamado ["VersionBits"](https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki "BIP9") diseñado para minimizar interrupciones en la red. El 95% de los mineros tenían que señalizar su conformidad para que SegWit se activara en la red Bitcoin. Esta señalización iba a comenzar el 15 de Noviembre de 2016.

Se animó a los usuarios a que actualizaran el cliente lo que hicieron la mayoría. 

Todo apuntaba a que SegWit se activaría en breve, pero no fue así.

Varios de los participantes de la reunión de Hong Kong [cambiaron de opinión](https://bitcoinmagazine.com/articles/the-status-of-the-hong-kong-hard-fork-an-update-1479843521/ "Cambios de opinión").

Un hard fork significa que el protocolo que se es válido deja de serlo tras el momento del hard fork, los desarrolladores ven un peligro en este tipo de actualización y es que todos los clientes deben ir a la nueva versión si hay usuarios que no están de acuerdo pueden quedarse en la versión "vieja" del protocolo y provoca una bifurcación. Para evitar esto se propuso un ["soft-hardfork".](https://petertodd.org/2016/forced-soft-forks "soft-hardfork")

Lo malo del soft-hardfork era que se podía aplicar sin que los usuarios pudieran hacer nada, les obligaba a seguir las normas aunque no estuvieran de acuerdo o crear una nueva red. Para evitar esta situación los desarrolladores buscaban la manera de tener confirmación por parte de la comunidad de Bitcoin. Para ello se propusieron 2 soluciones basadas en los bitcoin que controlaban los usuarios, estas soluciones se llamaron "señalización con moneda" (coin-signaling). La primera de las soluciones permitía a los usuarios agregar un dato en las transacciones señalizando su conformidad con el fork, si todas las transacciones durante un periodo de tiempo señalizaban el fork se consideraba que la comunidad lo aprobaba. La segunda solución en la que estuvo trabajando [Peter Todd](https://twitter.com/peterktodd "Peter Todd") permitía a los usarios mostrar su posición sin necesidad de realizar transacciones, lo explicó [en su blog.](https://petertodd.org/2016/hardforks-after-the-segwit-blocksize-increase)

La falta de señalización de conformidad a SegWit por parte de los mineros y lo que varios desarrolladores [consideraron una ruptura de acuerdo](https://www.reddit.com/r/btc/comments/47dbeh/f2pool_why_not_take_a_cue_from_slush_and_offer/d0chqph/ "Ruptura de acuerdo") por parte del consorcio minero chino [F2Pool](https://www.f2pool.com/ "F2Pool") hicieron que los desarrolladores cambiaran su punto de vista. Peter Todd 

##### Presentación de SegWit de Pieter Wuille en "Scaling Bitcoin" en Hong Kong  ([@pwuille](https://twitter.com/pwuille "Pieter Wuille")) [-VIDEO-](https://www.youtube.com/watch?v=NOYNZB5BCHM)
