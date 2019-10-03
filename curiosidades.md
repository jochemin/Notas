- Comando curl http://rate.sx/btc
![alt text](https://i.imgur.com/QIKdA8k.png)

- Cálculo tasa de hash:
  tasa_hash = (bloques_encontrados/bloques_esperados*dificultad *2**32/600)

- bogosize (salida de gettxoutsetinfo)
  Unrelated to disk usage, but is a database-independent metric of UTXO set size: it counts every UTXO entry as 50 + the length of its  scriptPubKey. Source: https://git.devuan.org/devuan-packages/bitcoin/commit/8b22af3ee59f48298b5203b9a38549a0d1dfd326
