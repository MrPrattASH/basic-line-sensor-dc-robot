let light_sensor = 0
forever(function on_forever() {
    
    light_sensor = pins.analogReadPin(AnalogPin.P1)
    if (light_sensor >= 850) {
        pins.digitalWritePin(DigitalPin.P16, 1)
        // back up
        motor.MotorRun(motor.Motors.M1, motor.Dir.CCW, 75)
        motor.MotorRun(motor.Motors.M2, motor.Dir.CCW, 85)
        basic.pause(1500)
        // spin around at a random degree
        motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 75)
        motor.MotorRun(motor.Motors.M2, motor.Dir.CCW, 75)
        basic.pause(randint(750, 2000))
    } else {
        // we're on white, drive forward
        pins.digitalWritePin(DigitalPin.P16, 0)
        motor.MotorRun(motor.Motors.M1, motor.Dir.CW, 50)
        motor.MotorRun(motor.Motors.M4, motor.Dir.CW, 50)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showNumber(light_sensor)
})
