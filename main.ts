let Pressure_Sensor = 0
let Potentiometer = 0
basic.forever(function on_forever() {
    
    Pressure_Sensor = pins.digitalReadPin(DigitalPin.P0)
    Potentiometer = pins.analogReadPin(AnalogPin.P1)
    if (Pressure_Sensor == 1) {
        images.createBigImage(`
            . # # # . . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            . # # # . . . . . .
            `).scrollImage(5, 200)
    } else if (Potentiometer < 300) {
        images.createBigImage(`
            . # # # . . . . . .
            # # # # # . . . . .
            . . . # # . . . . .
            # # # # # . . . . .
            . # # # . . . . . .
            `).scrollImage(1, 200)
    } else if (Potentiometer > 900) {
        images.createBigImage(`
            . # # # . . . . . .
            # . # . # . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            # . # . # . . . . .
            `).scrollImage(1, 200)
    }
    
})
