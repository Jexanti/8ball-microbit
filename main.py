rn = 0
def doSomething():
    global rn
    rn = randint(0, 9)
    if rn == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
    elif rn == 1:
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            """)
    elif rn == 2:
        basic.show_leds("""
            . # # # .
            # . . . #
            . . # # .
            . . . . .
            . . # . .
            """)
    else:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
        doSomething()

def on_gesture_shake():
    doSomething()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
