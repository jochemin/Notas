#### Log de servicio
```
journalctl -u service-name.service
``` 
#### Log de servicio (último arranque)
```
journalctl -u service-name.service -b
``` 
#### Comprobar que TOR esta OK
```
curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
``` 
#### Mostrar la API Key de Whirlpool
```
docker exec -it whirlpool cat /home/whirlpool/.whirlpool-cli/whirlpool-cli-config.properties | grep cli.apiKey= | cut -c 12-
```
#### Mostrar intentos fallidos autenticación ssh
```
grep sshd.\*Failed /var/log/auth.log
```