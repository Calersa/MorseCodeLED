import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
ledpin=11
GPIO.setup(ledpin, GPIO.OUT)

MORSECODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

def blinkmorse(character):
    code=MORSECODE.get(character.upper(), '')
    for symbol in code:
        if symbol == '.':
            GPIO.output(ledpin, True)
            time.sleep(0.1)
            GPIO.output(ledpin, False)
        elif symbol == '-':
            GPIO.output(ledpin, True)
            time.sleep(0.3)
            GPIO.output(ledpin, False)
        time.sleep(0.1)
def blinkname(name):
    for letter in name:
        if letter != ' ':
            blinkmorse(letter)
        time.sleep(0.3)

try:
    name='JUAN'
    blinkname(name)

finally:
    GPIO.cleanup()