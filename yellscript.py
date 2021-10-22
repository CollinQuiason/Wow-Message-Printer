from pynput.keyboard import Key, Controller, Listener, KeyCode, HotKey, GlobalHotKeys
import time
import subprocess
#Data
keyboard = Controller()
global MAC_ENVIRONMENT
global WINDOWS_ENVIRONMENT

#################
##CONFIGURATION##
#################
MAC_ENVIRONMENT = True
WINDOWS_ENVIRONMENT = False

ARGS_KEY_COMBINATION = '<cmd>+\\';
# The key combination to check
STOP_COMBINATION = {Key.shift, Key.esc}
STOP_KEY_COMBINATION = '<shift>+<esc>'
#WINDOWS_ENVIRONMENT
GUICOMBINATION = {Key.ctrl_r, Key.f4}
COMBINATION = {Key.shift_r}
DISCORDCOMBINATION = {Key.alt_r}
TP_RAIDO_COMBINATION = {KeyCode.from_char('#')}
#MAC_ENVIRONMENT
START_ADVANCED_COMBINATION = {KeyCode.from_char('#')}

# The currently active modifiers
current = set()
global messageString
global messageStringDiscord
global advancedCommandString
global args
messageString = ""
messageStringDiscord = ""
advancedCommandString = ""
enterinterval = 0.006
interval = 0.002

#Triggers
global recordMessage
global recordDiscordMessage
global recordAdvancedMessage
recordMessage = False
recordDiscordMessage = False
recordAdvancedMessage = False
global commit
global commitDiscordR
commit = False
commitDiscord = False




def main():

    def on_activate_args():
        global args
        args = ""
        def args_on_press(key):
            global args
            if (key == Key.enter):
                print("Sending Message: " + args)
                args_function_map[args]()
                argsListener.stop()
            args += str(key).replace('\'', '')
            print("Main on press pressed: " + str(key))
        def args_on_release(key):
            print("Main on press released: " + str(key))
        print("Main Entered!")
        with Listener(
                on_press=args_on_press,
                on_release=args_on_release) as argsListener:
            argsListener.join()

    def on_stop():
        hotKeyListener.stop()

    with GlobalHotKeys({
            STOP_KEY_COMBINATION: on_stop,
            ARGS_KEY_COMBINATION: on_activate_args}) as hotKeyListener:
        hotKeyListener.join()

#     with Listener(on_press=on_press, on_release=on_release) as listener:
#             listener.join()

def maintest():
    print("executed main test message function")
    subprocess.run(["echo", "\"yeet\""])
    subprocess.run(["echo", "pbpaste"])

def decrypt():
    subprocess.call(["/Users/collinquiasonrottinghaus/dev/cli-utils/build/install/cli-utils/bin/cli-utils", "-d", "$(pbpaste)"])

args_function_map = {
    "test": maintest,
    "de": decrypt
}


def on_press(key):
    global MAC_ENVIRONMENT
    global WINDOWS_ENVIRONMENT
    current.add(key)

    if (MAC_ENVIRONMENT):
        global recordAdvancedMessage
        global advancedCommandString
        if key in START_ADVANCED_COMBINATION:
            if all(k in current for k in START_ADVANCED_COMBINATION):
                print ("RECORD ADVANED MESSAGE ENABLED")
                recordAdvancedMessage = True
        elif recordAdvancedMessage == True and commitCommand == False and all(k in current for k in START_ADVANCED_COMBINATION) and (key not in START_ADVANCED_COMBINATION): #Add key to message record
            print ("Key added to advanced command: " + str(key))
            advancedCommandString += str(key)[1:-1]

    elif (WINDOWS_ENVIRONMENT):
        global recordMessage
        global messageString
        global recordDiscordMessage
        global messageStringDiscord
        if key in COMBINATION:
            if all(k in current for k in COMBINATION): #Record Message
                recordMessage = True
        if key in DISCORDCOMBINATION:
            if all(k in current for k in DISCORDCOMBINATION): #Record Message
                recordDiscordMessage = True
        if key in GUICOMBINATION:
            if all(k in current for k in GUICOMBINATION): #GUI Appear
                dosomething()
        if key in TP_RAIDO_COMBINATION:
            if all (k in current for k in TP_RAIDO_COMBINATION):
                tpRaido()
        elif recordMessage == True and commit == False and all(k in current for k in COMBINATION) and (key not in COMBINATION): #Add key to message record
            print ("Key added to wow message: " + str(key))
            messageString += str(key)[1:-1]
        elif recordDiscordMessage == True and commitDiscord == False and all(k in current for k in DISCORDCOMBINATION) and (key not in DISCORDCOMBINATION):
            print ("Key added to disord message: " + str(key))
            messageStringDiscord += str(key)[1:-1]

    if key in STOP_COMBINATION:
        if all (k in current for k in STOP_COMBINATION):
            listener.stop()
            raise StopIteration

def registerKeybind(combination, actionFunction):
    if key in combination:
        if all (k in current for k in combination):
            actionFunction()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass
    if key in COMBINATION and (not all(k in current for k in COMBINATION)):
        print("placeholder")
        # commitMessage()
    if key in DISCORDCOMBINATION and (not all(k in current for k in DISCORDCOMBINATION)):
        print("placeholder")
        # commitDiscordMessage()
    if key in START_ADVANCED_COMBINATION and (not all(k in current for k in START_ADVANCED_COMBINATION)):
        commitAdvancedCommand()

def commitAdvancedCommand():
    global advancedCommandString
    global commitCommand
    commitCommand = True
    if (advancedCommandString):
        print("advanced command string final: " + advancedCommandString)


    commitCommand = False


def commitMessage():
    global recordMessage
    recordMessage = False
    global commit
    commit = True
    global messageString
    print ("Wow Message Sending... \"" + messageString + "\"")
    for i in messageString.lower():
        message(letters[i])
    messageString = ""
    commit = False


def commitDiscordMessage():
    global recordDiscordMessage
    recordMessage = False
    global commitDiscord
    commit = True
    global messageStringDiscord
    print ("Discord Message Sending... \"" + messageStringDiscord + "\"")
    for i in messageStringDiscord.lower():
        messageDiscord(letters[i])
    messageStringDiscord = ""
    commitDiscord = False

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

def tpRaido():
    keyboard.release(Key.shift)
    print('tpRaido....')
    time.sleep(.01)
    enterKey()
    time.sleep(.01)
    pressKey(Key.backspace)
    time.sleep(.01)
    pressKey(Key.backspace)
    time.sleep(.01)
    pressKey(Key.backspace)
    time.sleep(.01)
    time.sleep(interval)
    typeMessageWithInterval("/tp Raido")
    time.sleep(.01)
    time.sleep(interval)
    enterKey()

def messageDiscord(letter):
    spaceDiscord()
    enterKey()
    for (index, pixel) in enumerate(letter):
        if index % 5 == 0:
            enterKey()
            enterKey()
        if pixel == '0':
            hunnet()
        else:
            cool()
    enterKey()

def typeMessage(message):
    keyboard.type(message)

def typeMessageWithInterval(message):
    time.sleep(interval)
    for char in message:
        pressKey(KeyCode.from_char(char))

def pressKey(key):
    keyboard.press(key)
    time.sleep(interval)
    keyboard.release(key)
    time.sleep(interval)

def enterKey():
    keyboard.press(Key.enter)
    time.sleep(enterinterval)
    keyboard.release(Key.enter)
    time.sleep(enterinterval)

def hunnet():
    typeMessage(":100:")

def cool():
    typeMessage(":cool:")

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
def spaceDiscord():
    typeMessage(":space_invader:")

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
        "11111",

    "0":"11111" +
        "10011" +
        "10101" +
        "11001" +
        "11111",

    "1":"01100" +
        "00100" +
        "00100" +
        "00100" +
        "01110",
}

main()







