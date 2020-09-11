Pressure_Sensor = 0
Potentiometer = 0

def on_forever():
    global Pressure_Sensor, Potentiometer
    Pressure_Sensor = pins.digital_read_pin(DigitalPin.P0)
    Potentiometer = pins.analog_read_pin(AnalogPin.P1)
    if Pressure_Sensor == 1:
        images.create_big_image("""
            . # # # . . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            . # # # . . . . . .
            """).scroll_image(5, 200)
    elif Potentiometer < 300:
        images.create_big_image("""
            . # # # . . . . . .
            # # # # # . . . . .
            . . . # # . . . . .
            # # # # # . . . . .
            . # # # . . . . . .
            """).scroll_image(1, 200)
    elif Potentiometer > 900:
        images.create_big_image("""
            . # # # . . . . . .
            # . # . # . . . . .
            # # # # # . . . . .
            # # # # # . . . . .
            # . # . # . . . . .
            """).scroll_image(1, 200)
basic.forever(on_forever)
