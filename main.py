light_sensor = 0

def on_forever():
    global light_sensor
    light_sensor = pins.analog_read_pin(AnalogPin.P1)
    if light_sensor >= 850:
        pins.digital_write_pin(DigitalPin.P16, 1)
        #back up
        motor.motor_run(motor.Motors.M1, motor.Dir.CCW, 75)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, 85)
        basic.pause(1500)
        #spin around at a random degree
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 75)
        motor.motor_run(motor.Motors.M2, motor.Dir.CCW, 75)
        basic.pause(randint(750,2000))

    else:
        #we're on white, drive forward
        pins.digital_write_pin(DigitalPin.P16, 0)
        motor.motor_run(motor.Motors.M1, motor.Dir.CW, 50)
        motor.motor_run(motor.Motors.M4, motor.Dir.CW, 50)
    
forever(on_forever)

def on_button_pressed_a():
    global light_sensor
    basic.show_number(light_sensor)
input.on_button_pressed(Button.A, on_button_pressed_a)