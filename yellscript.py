from pynput.keyboard import Key, Controller, Listener
import time
#Data
keyboard = Controller()

# The key combination to check
COMBINATION = {Key.ctrl_r, Key.f2}

# The currently active modifiers
current = set()
enterinterval = 0.006
interval = 0.002


def main():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()
def fullMessage(phrase):
	for i in phrase.upper():
		exec("message(%s)" % (i))
def message(letter):
	time.sleep(enterinterval)
	keyboard.press(Key.enter)
	time.sleep(enterinterval)
	keyboard.release(Key.enter)
	time.sleep(enterinterval)
	for (index, pixel) in enumerate(letter):
		if index % 5 == 0:
			time.sleep(enterinterval)
			keyboard.press(Key.enter)
			time.sleep(enterinterval)
			keyboard.release(Key.enter)
			time.sleep(enterinterval)
			keyboard.press(Key.enter)
			time.sleep(enterinterval)
			keyboard.release(Key.enter)
			time.sleep(enterinterval)
		if pixel == '0':
			cross()
		else:
			square()
	time.sleep(enterinterval)		
	keyboard.press(Key.enter)
	time.sleep(enterinterval)
	keyboard.release(Key.enter)
	time.sleep(enterinterval)
	space()

def on_press(key):
    if key in COMBINATION:
        current.add(key)
        if all(k in current for k in COMBINATION):
            fullMessage('run');

    if key == Key.esc or key == '`':
        listener.stop()
        raise StopIteration

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass	
def square():
	time.sleep(interval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press('[')
	time.sleep(interval)
	keyboard.release('[')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)
	keyboard.press('s')
	time.sleep(interval)
	keyboard.release('s')
	time.sleep(interval)
	keyboard.press('q')
	time.sleep(interval)
	keyboard.release('q')
	time.sleep(interval)
	keyboard.press('u')
	time.sleep(interval)
	keyboard.release('u')
	time.sleep(interval)
	keyboard.press('a')
	time.sleep(interval)
	keyboard.release('a')
	time.sleep(interval)
	keyboard.press('r')
	time.sleep(interval)
	keyboard.release('r')
	time.sleep(interval)
	keyboard.press('e')
	time.sleep(interval)
	keyboard.release('e')
	time.sleep(interval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press(']')
	time.sleep(interval)
	keyboard.release(']')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)
def space():
	time.sleep(enterinterval)		
	keyboard.press(Key.enter)
	time.sleep(enterinterval)
	keyboard.release(Key.enter)
	time.sleep(enterinterval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press('[')
	time.sleep(interval)
	keyboard.release('[')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)
	keyboard.press('m')
	time.sleep(interval)
	keyboard.release('m')
	time.sleep(interval)
	keyboard.press('o')
	time.sleep(interval)
	keyboard.release('o')
	time.sleep(interval)
	keyboard.press('o')
	time.sleep(interval)
	keyboard.release('o')
	time.sleep(interval)
	keyboard.press('n')
	time.sleep(interval)
	keyboard.release('n')
	time.sleep(interval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press(']')
	time.sleep(interval)
	keyboard.release(']')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)		
	keyboard.press(Key.enter)
	time.sleep(enterinterval)
	keyboard.release(Key.enter)
	time.sleep(enterinterval)
def cross():
	time.sleep(interval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press('[')
	time.sleep(interval)
	keyboard.release('[')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)
	keyboard.press('c')
	time.sleep(interval)
	keyboard.release('c')
	time.sleep(interval)
	keyboard.press('r')
	time.sleep(interval)
	keyboard.release('r')
	time.sleep(interval)
	keyboard.press('o')
	time.sleep(interval)
	keyboard.release('o')
	time.sleep(interval)
	keyboard.press('s')
	time.sleep(interval)
	keyboard.release('s')
	time.sleep(interval)
	keyboard.press('s')
	time.sleep(interval)
	keyboard.release('s')
	time.sleep(interval)
	keyboard.press(Key.shift)
	time.sleep(interval)
	keyboard.press(']')
	time.sleep(interval)
	keyboard.release(']')
	time.sleep(interval)
	keyboard.release(Key.shift)
	time.sleep(interval)

A =("11111" +
	"10001" +
	"11111" +
	"10001" +
	"10001")

B =("11110" +
	"10001" +
	"11110" +
	"10001" +
	"11110")

C =("11111" +
	"10000" +
	"10000" +
	"10000" +
	"11111")

D =("11110" +
	"10001" +
	"10001" +
	"10001" +
	"11110")

E =("11111" +
	"10000" +
	"11100" +
	"10000" +
	"11111")

F =("11111" +
	"10000" +
	"11100" +
	"10000" +
	"10000")

G =("11111" +
	"10000" +
	"10011" +
	"10001" +
	"11111")

H =("10001" +
	"10001" +
	"11111" +
	"10001" +
	"10001")

I =("01110" +
	"00100" +
	"00100" +
	"00100" +
	"01110")

J =("11111" +
	"00010" +
	"00010" +
	"10010" +
	"11110")

K =("10010" +
	"10100" +
	"11000" +
	"10100" +
	"10010")

L =("10000" +
	"10000" +
	"10000" +
	"10000" +
	"11111")

M =("10001" +
	"11011" +
	"10101" +
	"10001" +
	"10001")

N =("10001" +
	"11001" +
	"10101" +
	"10011" +
	"10001")

O =("11111" +
	"10001" +
	"10001" +
	"10001" +
	"11111")

P =("11110" +
	"10010" +
	"11110" +
	"10000" +
	"10000")

Q =("11111" +
	"10001" +
	"10001" +
	"10011" +
	"11111")

R =("11110" +
	"10010" +
	"11110" +
	"10100" +
	"10010")

S =("11111" +
	"10000" +
	"11111" +
	"00001" +
	"11111")

T =("11111" +
	"00100" +
	"00100" +
	"00100" +
	"00100")

U =("10001" +
	"10001" +
	"10001" +
	"10001" +
	"11111")

V =("10001" +
	"10001" +
	"01010" +
	"01010" +
	"00100")

W =("10001" +
	"10001" +
	"10101" +
	"11011" +
	"10001")

X =("10001" +
	"01010" +
	"00100" +
	"01010" +
	"10001")

Y =("10001" +
	"01010" +
	"00100" +
	"00100" +
	"00100")

Z =("11111" +
	"00010" +
	"00100" +
	"01000" +
	"11111")

main()




