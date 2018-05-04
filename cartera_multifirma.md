## Cartera multifirma con Electrum (https://electrum.org)

Este manual muestra la manera de crear una cartera multifirma. Las carteras multifirma como su nombre indica son aquellas en las que, para enviar fondos es necesario la autorización (mediante firma) de un número concreto de personas.

Obviamos la instalación de Electrum, para cualquier duda a este respecto consultar en su web.

El manual parte de que cada usuario utiliza una firma y tiene Electrum instalado, el idioma del software está en inglés.

1. Creamos una cartera nueva
<p align="center">
  <img src="img_multifirma/1.png?raw=true" alt="Nueva cartera"/>
</p>
2. Le damos un nombre
<p align="center">
  <img src="img_multifirma/2.png?raw=true" alt="Nueva cartera"/>
</p>
3. Seleccionamos la opción "Multi-signature wallet" (cartera multifirma)
<p align="center">
  <img src="img_multifirma/3.png?raw=true" alt="Nueva cartera"/>
</p>
4. En esta pantalla seleccionamos el número de usuarios que van a firmar y cuantas firmas hacen falta para mover fondos.
<p align="center">
  <img src="img_multifirma/4.png?raw=true" alt="Nueva cartera"/>
</p>
5. Podemos crear una nueva semilla, utilizar una ya creada, un hardware wallet... En este caso asumimos la creación de una nueva.
<p align="center">
  <img src="img_multifirma/5.png?raw=true" alt="Nueva cartera"/>
</p>
6. Por supuesto segwit
<p align="center">
  <img src="img_multifirma/6.png?raw=true" alt="Nueva cartera"/>
</p>
7. Guardamos los datos de nuestra nueva cartera
<p align="center">
  <img src="img_multifirma/7.png?raw=true" alt="Nueva cartera"/>
</p>

<p align="center">
  <img src="img_multifirma/8.png?raw=true" alt="Nueva cartera"/>
</p>
8. Ahora tendremos que añadir a todos los usuarios que van a firmar, para ello se utiliza la clave pública maestra, la semilla o una cartera hardware. Una vez añadidos se generarán las direcciones de la nueva cartera.
<p align="center">
  <img src="img_multifirma/9.png?raw=true" alt="Nueva cartera"/>
</p>

<p align="center">
  <img src="img_multifirma/10.png?raw=true" alt="Nueva cartera"/>
</p>

<p align="center">
  <img src="img_multifirma/11.png?raw=true" alt="Nueva cartera"/>
</p>
9. A la hora de realizar el envío de fondos desde nuestra cartera multifirma se realizará de la misma manera que una transacción normal. Comprobaremos que el estado de la transacción será "firmada parcialmente". La transacción no se podrá envíar a la red hasta que tenga el número de firmas suficiente que hemos configurado en el paso 4.
<p align="center">
  <img src="img_multifirma/14.png?raw=true" alt="Nueva cartera"/>
</p>
10. Enviaremos la transacción parcialmente firmada al resto de usuarios, se puede utilizar texto, código QR, fichero... Los usuarios importarán esta transacción en su cartera multifirma y, en caso de estar de acuerdo, la firmarán.
<p align="center">
  <img src="img_multifirma/16.png?raw=true" alt="Nueva cartera"/>
</p>
11. Una vez alcanzado el número de firmas necesario para mover fondos, el estado de la transacción pasará a "Firmado" y el botón de "Broadcast" se habilitará.
<p align="center">
  <img src="img_multifirma/17.png?raw=true" alt="Nueva cartera"/>
</p>
12. Una vez pulsado el botón de "Broadcast" la transacción se envíara a la red Bitcoin.
<p align="center">
  <img src="img_multifirma/18.png?raw=true" alt="Nueva cartera"/>
</p>
