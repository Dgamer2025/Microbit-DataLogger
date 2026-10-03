#El código en versión Python (para MakeCode)
#

def on_button_pressed_a():
    global Registrando
    basic.show_leds("""
        . # . . .
        . # # . .
        . # # # .
        . # # . .
        . # . . .
        """)
    Registrando = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    datalogger.delete_log()
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Registrando
    Registrando = 0
    basic.show_leds("""
        . . . . .
        . # . # .
        . # . # .
        . # . # .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)

Registrando = 0
datalogger.set_column_titles("Temperatura", "Nivel de Sonido", "Nivel de Luz")
Registrando = 0

def on_every_interval():
    if Registrando == 1:
        datalogger.log(datalogger.create_cv("Temperatura", input.temperature()),
            datalogger.create_cv("Nivel de Sonido", input.sound_level()),
            datalogger.create_cv("Nivel de Luz", input.light_level()))
loops.every_interval(1000, on_every_interval)
