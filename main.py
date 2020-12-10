def on_forever():
    basic.show_number(sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS))
    basic.show_icon(IconNames.HEART)
    basic.clear_screen()
basic.forever(on_forever)
