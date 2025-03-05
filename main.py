servo_k = 0

def on_button_pressed_a():
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    servos.P0.set_angle(0)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    servos.P0.set_angle(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(180)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(180)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(180)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # # #
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    servos.P0.set_angle(0)
    basic.show_leds("""
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        """)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        """)
    servos.P0.set_angle(90)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_released():
    global servo_k
    if servo_k:
        servo_k = 0
        servos.P1.run(0)
    else:
        servo_k = 1
        servos.P1.run(100)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)
