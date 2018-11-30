import winsound
import time0

# Morse codes sounds
def dot():
    winsound.Beep(428, 300)

def dash():
    winsound.Beep(428, 700)

sleep_after_words = 1
def play(str):
    a = str


    def p():
        dot()
        time0.sleep(0.2)
        dash()
        time0.sleep(0.2)
        dash()
        time0.sleep(0.2)
        dot()
        time0.sleep(sleep_after_words)

    def i():
        dot()
        time0.sleep(0.2)
        dot()
        time0.sleep(sleep_after_words)

    def h():
        dot()
        time0.sleep(0.2)
        dot()
        time0.sleep(0.2)
        dot()
        time0.sleep(0.2)
        dot()
        time0.sleep(sleep_after_words)

    def k():
        dash()
        time0.sleep(0.2)
        dot()
        time0.sleep(0.2)
        dash()
        time0.sleep(sleep_after_words)

    def a():
        dot()
        time0.sleep(0.2)
        dash()
        time0.sleep(sleep_after_words)

    p()
    h()
    i()
    k()
    a()


play('phika')