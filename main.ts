let current_temperature = 0
basic.forever(function on_forever() {
    
    current_temperature = input.temperature()
    basic.showNumber(current_temperature)
    basic.pause(1000)
    basic.clearScreen()
})
