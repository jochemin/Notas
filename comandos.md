### Ver conexiones de Bitcoin Core

watch -t ./bitcoin-cli -netinfo 4

### Sacar los OP_RETURN de las tx de un bloque (necesita FQ https://github.com/wader/fq/releases)

bitcoin-cli getblock $(bitcoin-cli getblockhash 522222) 0 | xxd -r -p | fq -d bitcoin_block '.transactions[] | .outputs[] | select(.scriptpub[0].op == "return") | .scriptpub[1].arg'
