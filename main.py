light_sensor = 0

def on_forever():
    global light_sensor
    light_sensor = pins.analog_read_pin(AnalogPin.P1)
    if light_sensor >= 700:
        pins.digital_write_pin(DigitalPin.P16, 1)
    else:
        pins.digital_write_pin(DigitalPin.P16, 0)
Math.random()
    
forever(on_forever)

def on_button_pressed_a():
    global light_sensor
    basic.show_number(light_sensor)
input.on_button_pressed(Button.A, on_button_pressed_a)