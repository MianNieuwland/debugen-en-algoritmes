teller = 0

def on_forever():
    global teller
    led.plot(teller, 0)
    teller = teller + 1
    basic.pause(500)
    basic.clear_screen()
    if teller == 5:
        teller = 0
basic.forever(on_forever)
