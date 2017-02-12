# ademco

Just a script that connects to an Ademco alarm panel via serial port that happens to not support ECP. From testing it was clear that the panel sends out data at 2400 baud 8E1. By comparing the serial data to the indications on the fixed english keypad, it seems that each message is 4 bytes long and consists of two digits to be displayed on the keypad, and a bitfield so that the appropriate text can be displayed on the keypad LCD. 

The bus is similar to RS423 and it is inverted, so use a transistor in a common emitter configuration with a reasonably sized resistor so that the bus is not loaded. I have not tested sending data back to the panel.

So far the script just assumes that the first byte is 0x19 which does not display anything on the two digits on the LCD. This needs to be updated so that when the panel displays a zone on the keypad (e.g. 05), the script will find 0x05 as the first byte.

There does not seem to be any error correcting or checksum after the data is received, however it is technically possible to assume that some state transitions of the system are illegal.
