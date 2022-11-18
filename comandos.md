### Generar el whitepaper de Bitcoin en PDF
seq 0 947 | (while read -r n; do bitcoin-cli gettxout 54e48e5f5c656b26c3bca14a8c95aa583d07ebe84dde3b7dd4a78f4e4186e713 $n | jq -r '.scriptPubKey.asm' | awk '{ print $2 $3 $4 }'; done) | tr -d '\n' | cut -c 17-368600 | xxd -r -p > bitcoin.pdf

### Ver conexiones de Bitcoin Core
watch -t ./bitcoin-cli -netinfo 4

### Sacar los OP_RETURN de las tx de un bloque (necesita FQ https://github.com/wader/fq/releases)
bitcoin-cli getblock $(bitcoin-cli getblockhash 522222) 0 | xxd -r -p | fq -d bitcoin_block '.transactions[] | .outputs[] | select(.scriptpub[0].op == "return") | .scriptpub[1].arg'

### Sacar mensaje bloque 0
bitcoin-cli getblock $(bitcoin-cli getblockhash 0) 2 | jq .tx[0].hex | xxd -r -p | strings | head -n 1

### Versión de nodo completo de nuestros peer
bitcoin-cli getpeerinfo | grep subver | sort | uniq -c | sort -n

### Versiones recibidas en el "version message"
tail -n5000000 ~/.bitcoin/debug.log | sed -n 's/.*receive version message: //p;' | sed 's/ version [0-9]*, blocks=.*//' | sort | uniq -c | sort -n

### Listado de cambios de dificultad 
d=1; for ((i=0; i < $(bitcoin-cli getblockchaininfo | jq .blocks); i += 2016)) do n=$(bitcoin-cli getblock $(bitcoin-cli getblockhash $i) | jq .difficulty); c=$(echo "($n/$d * 100) - 100" | bc -l); echo $i: $c; d=$n; done

### Sacar el mensaje de la tx coinbase de un bloque
echo $(bitcoin-cli decoderawtransaction $(bitcoin-cli getrawtransaction $(bitcoin-cli getblock $(bitcoin-cli getblockhash 668197) | jq -r '.tx[0]')) | jq -r '.vin[0].coinbase' | cut -c19-109 | xxd -r -p)