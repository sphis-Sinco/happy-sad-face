input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.play(music.stringPlayable("C5 - - - - - - - ", 120), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . # . # .
        . . . . .
        . # . # .
        . # # # .
        . . . . .
        `)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    music.play(music.stringPlayable("E D G F B A C5 B ", 120), music.PlaybackMode.InBackground)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            `)
        basic.pause(100)
        basic.showLeds(`
            . # . # .
            . . . . .
            . # # # .
            # # # # #
            . . . . .
            `)
        basic.pause(100)
    }
    basic.showLeds(`
        . . . . .
        # . # . #
        # # # . #
        # . # . #
        . . . . .
        `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.play(music.stringPlayable("C - - - - - - - ", 120), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . # . # .
        . . . . .
        . # # # .
        . # . # .
        . . . . .
        `)
})
