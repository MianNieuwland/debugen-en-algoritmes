let teller = 0
basic.forever(function () {
    led.plot(teller, 0)
    teller = teller + 1
    basic.pause(500)
    basic.clearScreen()
    if (teller == 5) {
        teller = 0
    }
})
