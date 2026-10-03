//El código en versión JavaScript (para Makecode)

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showLeds(`
        . # . . .
        . # # . .
        . # # # .
        . # # . .
        . # . . .
        `)
    Registrando = 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
    datalogger.deleteLog()
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Registrando = 0
    basic.showLeds(`
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        `)
})
let Registrando = 0
datalogger.setColumnTitles("Temperatura", "Nivel de Sonido", "Nivel de Luz")
Registrando = 0
loops.everyInterval(1000, function on_every_interval() {
    if (Registrando == 1) {
        datalogger.log(datalogger.createCV("Temperatura", input.temperature()), datalogger.createCV("Nivel de Sonido", input.soundLevel()), datalogger.createCV("Nivel de Luz", input.lightLevel()))
    }
    
})
