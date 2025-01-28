def on_button_pressed_a():
    music.play(music.string_playable("C5 - - - - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . # . # .
        . . . . .
        . # . # .
        . # # # .
        . . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play(music.string_playable("E D G F B A C5 B ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    for index in range(4):
        basic.show_leds("""
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . . . . .
            """)
        basic.pause(100)
        basic.show_leds("""
            . # . # .
            . . . . .
            . # # # .
            # # # # #
            . . . . .
            """)
        basic.pause(100)
    basic.show_leds("""
        . . . . .
        # . # . #
        # # # . #
        # . # . #
        . . . . .
        """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play(music.string_playable("C - - - - - - - ", 120),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . # . # .
        . . . . .
        . # # # .
        . # . # .
        . . . . .
        """)
input.on_button_pressed(Button.B, on_button_pressed_b)
