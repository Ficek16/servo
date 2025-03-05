input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        `)
    servos.P0.setAngle(90)
    servos.P1.setAngle(90)
    basic.pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . # . .
        . . # . .
        . . # . .
        `)
    servos.P0.setAngle(180)
    servos.P1.setAngle(0)
    basic.pause(1000)
    basic.clearScreen()
})
