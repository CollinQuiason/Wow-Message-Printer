from pynput.keyboard import Key, Controller, Listener
import time
#Data
keyboard = Controller()

# The key combination to check
GUICOMBINATION = {Key.ctrl_r, Key.f4}
COMBINATION = {Key.f4}

# The currently active modifiers
current = set()
global messageString
messageString = ""
enterinterval = 0.006
interval = 0.002

#Triggers
global recordMessage
recordMessage = False
global commit
commit = False


def main():
	with Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

def commitMessage():
	global recordMessage
	recordMessage = False
	global commit
	commit = True
	global messageString
	print str("Message Sending... + \"" messageString + "\"")
	for i in messageString.lower():
		message(letters[i])
	messageString = ""
	commit = False

def message(letter):
	enterKey()
	for (index, pixel) in enumerate(letter):
		if index % 5 == 0:
			enterKey()
			enterKey()
		if pixel == '0':
			cross()
		else:
			square()
	enterKey()
	space()

def on_press(key):
    global recordMessage
    global messageString
    current.add(key)
    if key in COMBINATION:
        if all(k in current for k in COMBINATION): #Record Message
            recordMessage = True
    if key in GUICOMBINATION:
    	if all(k in current for k in GUICOMBINATION): #GUI Appear

    elif key == Key.esc or key == '`': #Stop
        listener.stop()
        raise StopIteration
    elif recordMessage == True and commit == False: #Add key to message record
		print str("Key added to message: " + key)
		messageString += str(key)[2:3]

def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass
    if key in COMBINATION and (not all(k in current for k in COMBINATION)):
    	commitMessage()

def enterKey():
	keyboard.press(Key.enter)
	time.sleep(enterinterval)
	keyboard.release(Key.enter)
	time.sleep(enterinterval)

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

letters = {
	"a":"11111" +
		"10001" +
		"11111" +
		"10001" +
		"10001",


	"b":"11110" +
		"10001" +
		"11110" +
		"10001" +
		"11110",

	"c":"11111" +
		"10000" +
		"10000" +
		"10000" +
		"11111",

	"d":"11110" +
		"10001" +
		"10001" +
		"10001" +
		"11110",

	"e":"11111" +
		"10000" +
		"11100" +
		"10000" +
		"11111",

	"f":"11111" +
		"10000" +
		"11100" +
		"10000" +
		"10000",

	"g":"11111" +
		"10000" +
		"10011" +
		"10001" +
		"11111",

	"h":"10001" +
		"10001" +
		"11111" +
		"10001" +
		"10001",

	"i":"01110" +
		"00100" +
		"00100" +
		"00100" +
		"01110",

	"j":"11111" +
		"00010" +
		"00010" +
		"10010" +
		"11110",

	"k":"10010" +
		"10100" +
		"11000" +
		"10100" +
		"10010",

	"l":"10000" +
		"10000" +
		"10000" +
		"10000" +
		"11111",

	"m":"10001" +
		"11011" +
		"10101" +
		"10001" +
		"10001",

	"n":"10001" +
		"11001" +
		"10101" +
		"10011" +
		"10001",

	"o":"11111" +
		"10001" +
		"10001" +
		"10001" +
		"11111",

	"p":"11110" +
		"10010" +
		"11110" +
		"10000" +
		"10000",

	"q":"11111" +
		"10001" +
		"10001" +
		"10011" +
		"11111",

	"r":"11110" +
		"10010" +
		"11110" +
		"10100" +
		"10010",

	"s":"11111" +
		"10000" +
		"11111" +
		"00001" +
		"11111",

	"t":"11111" +
		"00100" +
		"00100" +
		"00100" +
		"00100",

	"u":"10001" +
		"10001" +
		"10001" +
		"10001" +
		"11111",

	"v":"10001" +
		"10001" +
		"01010" +
		"01010" +
		"00100",

	"w":"10001" +
		"10001" +
		"10101" +
		"11011" +
		"10001",

	"x":"10001" +
		"01010" +
		"00100" +
		"01010" +
		"10001",

	"y":"10001" +
		"01010" +
		"00100" +
		"00100" +
		"00100",

	"z":"11111" +
		"00010" +
		"00100" +
		"01000" +
		"11111"
}


main()







