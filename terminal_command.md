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
