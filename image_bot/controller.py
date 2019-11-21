from playback import initializePyAutoGUI, countdownTimer, playActions
from time import sleep
import pyautogui
import os


def main():
    
    initializePyAutoGUI()
    countdownTimer()

    # This trade loop begins by docking at Loki Station
    LOOP_REPITITIONS = 3
    for i in range(0, LOOP_REPITITIONS):

        if i > 0:
            # Wait for station to load
            sleep(10.00)

        # Start docked at Loki Station, get to our universal starting position
        # get_starting_pos() should return an integer that corresponds with which
        # recorded action script should be played
        starting_pos = get_starting_pos("loki")
        try:
            action_filename = "lokistation_start_{}.json".format(starting_pos)
            playActions(action_filename)
        except FileNotFoundError as e:
            if not starting_pos:
                print("Starting position not recognized in Loki")
            else:
                print("No recorded actions for position {}".format(starting_pos))
            exit(0)
        else:
            print("Played starting actions {}".format(action_filename))
        sleep(2.00)

        # Confirm we're at the correct starting position
        confirmPosition("lokistation_starting_pos")

        # Playback those four steps to go to the trader, do the buying/selling,
        # go back to the ship, fly to Earth Station
        playActions("lokistation_goto_trader.json")
        sleep(2.00)
        playActions("lokistation_do_trading.json")
        sleep(2.00)
        confirmPosition("lokistation_done_trading")
        playActions("lokistation_goto_ship.json")
        sleep(10.00)  # allow time for loading screen when exiting station
        playActions("lokistation_goto_earthstation.json")

        # Wait for station to load
        sleep(10.00)

        # Now docked at Earth Station, get to that starting position
        # get_starting_pos() should return an integer that corresponds with which
        # recorded action script should be played
        starting_pos = get_starting_pos("earth")
        try:
            action_filename = "earthstation_start_{}.json".format(starting_pos)
            playActions(action_filename)
        except FileNotFoundError as e:
            if not starting_pos:
                print("Starting position not recognized in Earth")
            else:
                print("No recorded actions for position {}".format(starting_pos))
            exit(0)
        else:
            print("Played starting actions {}".format(action_filename))
        sleep(2.00)

        # Playback four steps to go to the trader, do the buying/selling,
        # go back to the ship, fly to Loki Station
        playActions("earthstation_goto_trader.json")
        sleep(2.00)
        playActions("earthstation_do_trading.json")
        sleep(2.00)
        playActions("earthstation_goto_ship.json")
        sleep(10.00)  # allow time for loading screen when exiting station
        playActions("earthstation_goto_lokistation.json")

        # Completed loop
        print("Completed loop")

    print("Done")


def get_starting_pos(station):
    # set the list of images we are trying to match
    if station == 'loki':
        images_to_check = [
            'lokistation_start_1.png',
            'lokistation_start_2.png',
            'lokistation_start_3.png',
            'lokistation_start_4.png',
            'lokistation_start_5.png',
            'lokistation_start_6.png',
            'lokistation_start_7.png',
            'lokistation_start_8.png',
            'lokistation_start_9.png',
            'lokistation_start_10.png',
            'lokistation_start_11.png',
            'lokistation_start_12.png',
            'lokistation_start_13.png',
            'lokistation_start_14.png',
            'lokistation_start_15.png',
            'lokistation_start_16.png',
            'lokistation_start_17.png',
            'lokistation_start_18.png',
            'lokistation_start_19.png',
        ]
    elif station == 'earth':
        images_to_check = [
            'earthstation_start_1.png',
            'earthstation_start_2.png',
            'earthstation_start_3.png',
            'earthstation_start_4.png',
            'earthstation_start_5.png',
            'earthstation_start_6.png',
            'earthstation_start_7.png',
            'earthstation_start_8.png',
            'earthstation_start_9.png',
            'earthstation_start_10.png',
            'earthstation_start_11.png',
            'earthstation_start_12.png',
            'earthstation_start_13.png',
            'earthstation_start_14.png',
            'earthstation_start_15.png',
        ]
    
    # loop over images until one is found, then return the index of the found
    # image
    for index, image_filename in enumerate(images_to_check):
        script_dir = os.path.dirname(__file__)
        needle_path = os.path.join(
            script_dir, 
            'needles', 
            image_filename
        )
        image_pos = pyautogui.locateOnScreen(needle_path)
        if image_pos:
            return index + 1

    return None


def confirmPosition(position_name):

    if position_name == "lokistation_starting_pos":
        x, y = (898, 153)
        rgb = (172, 178, 41)
    elif position_name == "lokistation_done_trading":
        x, y = (450, 296)
        rgb = (79, 78, 13)
    else:
        raise Exception("Position to confirm not recognized")

    pixel_matches = pyautogui.pixelMatchesColor(x, y, rgb, tolerance=10)
    if not pixel_matches:
        debug_str = "Pos: {} RGB expected: {} RGB found: {}".format(
            (x, y),
            rgb,
            pyautogui.pixel(x, y)
        )
        raise Exception("Detected off course for {}. Debug: {}".format(
            position_name, 
            debug_str
        ))

    print("On track for {}".format(position_name))


if __name__ == "__main__":
    main()
