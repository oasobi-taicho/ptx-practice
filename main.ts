basic.forever(function on_forever() {
    basic.showNumber(sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.Centimeters))
    basic.showIcon(IconNames.Heart)
    basic.clearScreen()
})
