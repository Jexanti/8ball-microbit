let rn = 0
function doSomething () {
    rn = randint(0, 9)
    if (rn == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    } else if (rn == 1) {
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . # .
            # . # . .
            . # . . .
            `)
    } else if (rn == 2) {
        basic.showLeds(`
            . # # # .
            # . . . #
            . . # # .
            . . . . .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . # # .
            # . . . #
            # # . . #
            . . . . #
            . . # # .
            `)
        doSomething()
    }
}
input.onGesture(Gesture.Shake, function () {
    doSomething()
})
