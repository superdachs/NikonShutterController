from machine import Pin

# set up pins for shutter and focus
shutter_pin = Pin(4, Pin.OUT)
focus_pin = Pin(5, Pin.OUT)
shutter_pin.value(0)
focus_pin.value(0)

# set up pin for serial hack
legacy_rts_pin = Pin(0, Pin.IN)
shutter_expose = False

# define interrup routine for serial shutter hack
def expose_irq(pin):
    print("expose irq")
    global shutter_expose
    shutter_expose = not pin.value()

legacy_rts_pin.irq(trigger=3, handler=expose_irq)

while True:
    # set the shutter
    shutter_pin.value(shutter_expose)
