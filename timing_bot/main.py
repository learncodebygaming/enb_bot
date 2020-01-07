import pyautogui
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00


def main():
    
    initializePyAutoGUI()
    countdownTimer()

    # Starting Point: Loki Station central landing platform. Wedge yourself between Louden MacEwen and the edge of the
    # wall. Then talk to him, and just close the interaction. It's important that you get the initial character 
    # alignment just right or the whole routine will be off.

    goToMerchant()
    tradeWithMerchant()
    returnToShip()
    flyToEarthStation()

    # Ending Point: Docked at Earth Station.
    print("Done")


def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)


def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)


def goToMerchant():
    # Back away from Louden MacEwen
    holdKey('s', 6.00)
    # Face the entrance
    holdKey('a', 0.10)
    # Go through the entrance into the main lobby
    holdKey('w', 7.00)
    # Turn to the bazaar lobby
    holdKey('d', 0.65)
    # Go through the entrance into the bazaar lobby
    holdKey('w', 5.60)
    # Turn to the trade merchant
    holdKey('d', 1.16)
    # Walk up to the trade merchant
    holdKey('w', 1.50)


def tradeWithMerchant():
    # Hover our mouse over the merchant
    pyautogui.moveTo(1200, 355, 0.25)
    sleep(DELAY_BETWEEN_COMMANDS)
    # Click the merchant to start our chat
    pyautogui.click()
    # Allow time for the chat to begin
    sleep(3.00)

    # Click the trade button
    pyautogui.click(378, 799, duration=0.25)
    # Allow time for the inventory to load
    sleep(1.00)

    # Move to the item. Was having trouble when I combined the movement with click() on this step
    pyautogui.moveTo(1159, 398, 0.25)
    sleep(1.0)
    # Now click on it to select it
    pyautogui.click()
    sleep(1.00)

    # Buy the item
    numToBuy = 28
    pyautogui.keyDown('shiftleft')
    for i in range(0, numToBuy):
        pyautogui.click()
        sleep(0.5)
    pyautogui.keyUp('shiftleft')

    # Click the close button
    pyautogui.click(1573, 320, duration=0.5)

    # Click the done button and wait for zoom out animation to finish
    pyautogui.click(486, 759, duration=0.5)
    sleep(2.00)


def returnToShip():
    # Change our body angle
    holdKey('a', 0.20)
    # Backup to center of the bazaar
    holdKey('s', 2.65)
    # Turn to the exit
    holdKey('d', 0.08)
    # Go through the exit back into the main lobby
    holdKey('w', 5.76)
    # Turn to the hangar
    holdKey('a', 0.68)
    # Go through the exit into the hangar
    holdKey('w', 6.20)
    # Turn towards our ship
    holdKey('a', 0.30)
    # Click our ship to exit the station
    pyautogui.click(438, 285, duration=0.25)
    # Allow time for the outside world to load
    sleep(10.00)


def flyToEarthStation():
    # Open the navigation map
    pyautogui.click(160, 840, duration=0.5)
    # Select the sector gate to Earth
    pyautogui.click(766, 469, duration=0.5)
    # Wait for warp path to be calculated
    sleep(1.5)
    # Initiate warp
    holdKey('z', 0.10)
    # Wait for warp to finish
    sleep(36)
    # Enter the gate
    pyautogui.click(1544, 627, duration=0.5)
    # Wait for the sector change to load
    sleep(15)
    # Open the navigation map
    pyautogui.click(160, 840, duration=0.5)
    # Select Earth Station
    pyautogui.click(428, 460, duration=0.5)
    # Wait for warp path to be calculated
    sleep(1.0)
    # Initiate warp
    holdKey('z', 0.10)
    # Wait for warp to finish
    sleep(17)
    # Dock at the station
    pyautogui.click(1544, 627, duration=0.5)


if __name__ == "__main__":
    main()
