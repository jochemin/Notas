# Bug ajuste dificultad Bitcoin

### Ajuste de dificultad cada 2016 bloques
 - [Satoshi programó el ajuste de dificultad para que sucediera cada 2016 bloques, 2 semanas aproximadamente.](https://bitcointalk.org/index.php?topic=43.msg249#msg249) 14 días son 20160 minutos, los bloques de bitcoin se publican cada 10 minutos aproximadamente por lo que 20160/10 dan los 2016 bloques entre ajustes.

### Bug ajuste de dificultad
 - Aunque el ajuste, efectivamente, se produce cada 2016 bloques, el cálculo sólo tiene en cuenta los 2015 bloques anteriores. ¿Por que sucede esto?
 - En el código original de Satoshi tenemos estas 2 líneas:
   -  ```const unsigned int nInterval = nTargetTimespan / nTargetSpacing;``` [link](https://github.com/trottier/original-bitcoin/blob/92ee8d9a994391d148733da77e2bbc2f4acc43cd/src/main.cpp#L689C5-L689C69)
   -  ```for (int i = 0; pindexFirst && i < nInterval-1; i++)``` [link](https://github.com/trottier/original-bitcoin/blob/92ee8d9a994391d148733da77e2bbc2f4acc43cd/src/main.cpp#L701C5-L701C57)

<p align="center">
  <img src="img_varios/ajuste_bug.jpg?raw=true" alt="Difficulty Bug"/>
</p>