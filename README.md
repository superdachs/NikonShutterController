# NikonShutterController

Some Nikon DSLR don't support bulb mode long exposure through USB PTP connection.
As a workaround several DIY cable instructions are made. All these cables use a serial-usb device as a hack using RTS line wired to a transistor.
This is not a suitable solution. Due to the fact that this setup is not stable and safe, I decided to build up a more stable version based on a NodeMCU ESP8266 microcontroller, a dedicated serial to usb adapter and mechanical relays.
This setup "translates" the weak RTS HIGH signal to a discrete signal on the microcontroller and power it up with npn transistors to switch relays safe and stable.

## parts list

### NodeMCU ESP8266 board
This board provides the logic, WLAN and debugging options. At the moment only the hacky way using a serial connection is provided. In future a nice web API will be a more sophisticated way to connect.
The USB-Connection of the NodeMCU will not be used for the serial hack so it is open for powering the circuit and connecting a pc to it. 

### FTDI USB to UART board
This is used only for the serial hack! The USB port do not provide any data connection. The board MUST be set to 3.3V to avoid damage of the NodeMCU! DONT EVER use 5V!

### NPN-Transistors
The Transistors are used to amplify the weak signal from the Microcontroller pins to switch the relays.

### Resistors
Two resistors are used to avoid shortening of base-emitter-circuit

### diodes
Two diodes are used to avoid high voltage on switching the relays off. They are NOT OPTIONAL!

### two 3V relays

### a 3.5mm headphone jack with 2.5mm adapter for the shutter cable


## wiring
We use the source voltage of the NodeMCU to provide enough amperes for the relays to switch!

NodeMCU PIN 4 - resistor (100Ohm) - Base 1
NodeMCU PIN 5 - resistor (100Ohm) - Base 2
NodeMCU PIN 0 - FTDI RTS
NodeMCU 3.3V - Sources of the Transistors
Diode Kathodes parallel to relays coil pin - Emmitters of the transistors

Ground connected to all devices and one coil pin of the relays and diode anodes.

Relays base pins both goes to the ground of the headphone jack. NO pins goes to the other pins of the jack. If it focusses and don't shoot, switch both.

## Software
First flash Micropython to the NodeMCU. It is described in Micropython documentation.
Setup a IDE like Pycharm with micropython plugin.
Upload sketch.

Shoot!

Yes this has TWO USB-Ports. The one from the FTDI is ONLY for triggering the exposure. The one of the NodeMCU is for programming, powering and further development.
You can't power this using only the FTDI Connection! A USB Power adaptor at the NodeMCU or a PC Connection on it is always neccessary!
