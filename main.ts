let light_sensor = 0
Math.random()
forever(function on_forever() {
    
    light_sensor = pins.analogReadPin(AnalogPin.P1)
    if (light_sensor >= 700) {
        pins.digitalWritePin(DigitalPin.P16, 1)
    } else {
        pins.digitalWritePin(DigitalPin.P16, 0)
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showNumber(light_sensor)
})
