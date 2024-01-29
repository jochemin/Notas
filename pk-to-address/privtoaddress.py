import hashlib
import base58
import codecs
import ecdsa

private_key = "18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725"

# Paso 1 - Generar una clave pública no comprimida

    # Pasamos la clave privada a bytes. El hex es porque le indicamos que el valor es hexadecimal
private_key_bytes = codecs.decode(private_key, 'hex')
    # Utilizamos las librerias SECP256k1 & ecdsa para generar la clave pública
public_key_raw = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
public_key_bytes = public_key_raw.to_string()
    # Pasamos la clave pública a hexadeciaml
public_key_hex = codecs.encode(public_key_bytes, 'hex')
    # Las claves públicas de Bitcoin comienzan con 0x04 así que lo añadimos al comienzo
public_key = (b'04' + public_key_hex).decode("utf-8")

# Paso 2 - Comprimir la clave pública

    # Comprobamos si el último byte es par o impar
if (ord(bytearray.fromhex(public_key[-2:])) % 2 == 0):
    public_key_compressed = '02'
else:
    public_key_compressed = '03'
    
    # Añadimos los bytes 0x02 to the X of the key if even or 0x03 if odd
public_key_compressed += public_key[2:66]

    # Convertimos la clave publica comprimida a bytes
hex_str = bytearray.fromhex(public_key_compressed)
    # Aplicamos hashing SHA-256  a la clave pública comprimida
sha = hashlib.sha256()
sha.update(hex_str)
sha.hexdigest() # .hexdigest() is hex ASCII

    # Aplicamos RIPMED-160 al resultado anterior
rip = hashlib.new('ripemd160')
rip.update(sha.digest())
key_hash = rip.hexdigest()

    # Añadimos el byte de version 0x00 para red principal
modified_key_hash = "00" + key_hash

    # Volvemos a aplicar has SHA-256 
sha = hashlib.sha256()
hex_str = bytearray.fromhex(modified_key_hash)
sha.update(hex_str)
sha.hexdigest()

    # Y lo volvemos a aplicar de nuevo
sha_2 = hashlib.sha256()
sha_2.update(sha.digest())
sha_2.hexdigest()

    # Cogemos los primeros 4 bytes de este resultado que será el checksum de la dirección
checksum = sha_2.hexdigest()[:8]

    # Añadimos este checksum al final del modified_key_hash
byte_25_address = modified_key_hash + checksum
byte_25_address

    # Convertimos este valor a base58
address = base58.b58encode(bytes(bytearray.fromhex(byte_25_address))).decode('utf-8')

print(address)