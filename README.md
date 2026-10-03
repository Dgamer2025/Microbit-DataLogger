# Microbit DataLogger
Un programa de BBC Micro:bit que registra datos sobre temperatura, nivel de sonido y nivel de luz.

### Cómo usar:
1. Descarga el programa .hex a tu BBC Microbit
2. Conecta la microbit a su batería, aún no la conectes por usb a tu PC. La placa debe estar en el ambiente donde quieras analizar datos, así que te interesa poder ponerla en zonas específicas con su batería, sin estar conectada a PC.
3. Una vez que la placa ya tenga corriente, pulsa el botón "A" y verás un símbolo de play (▶), lo que significa que la micro:bit ya está registrando Temperatura, Luz y Sonido cada segundo. También notarás que el símbolo de micrófono está parpadeando cada segundo.
4. Si quieres pausar el registro de datos, pero sin borrarlos, pulsa "B". Esto hará que el símbolo que aparezca en pantalla sea de pausa (⏸). A partir de ese momento, los datos se dejarán de registrar. Si quieres reanudar el registro de datos, vuelve a pulsar "A" y la placa seguirá.
5. Si deseas borrar los datos, pulsa "A+B". Aparecerá una cruz (X) que significa que se han borrado todos los datos registrados anteriormente.
6. Cuando quieras ver los datos, desconecta la Micro:bit de su batería y conéctala por USB a tu PC. Aparecerá un archivo llamado "MY_DATA.HTM". Simplemente ábrelo y podrás ver el historial dedaos registrados. También, si pulsas un botón que dice "Visual Preview", podrás ver esos datos en forma de gráfica.

### Qué incluye este repositorio:
Este repositorio incluye los archivos necesarios para ejecutar y/o editar el código de DataLogger. Está disponible en Python, JavaScript y también en la web.
- Enlace web:
https://makecode.microbit.org/S94616-40645-40271-58546
