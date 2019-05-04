import re
import requests


def main():
    # ask user from which area in Brisbane
    # to get the weather observations.
    while True:
        try:
            print(f'1. Brisbane')
            print(f'2. Brisbane Airport')
            print(f'3. Amberley')
            location_number = int(input("Enter a number between 1 - 3, to know \n"
                                        "the current temperature in that area? "))

            if location_number == 1:
                location = 'brisbane'
                break
            elif location_number == 2:
                location = 'brisbane-airport'
                break
            elif location_number == 3:
                location = 'amberley'
                break
            elif location_number > 3:
                print("Invalid input. Try again!\n")
                continue
        except:
            print("Invalid input. Try again!\n")
            continue

    # script to connect to http://reg.bom.gov.au/qld/observations/brisbane.shtml
    extract_temperature = get_weather_info(location)

    display_temp_to_user(location, extract_temperature)


def get_weather_info(location):
    url = 'http://reg.bom.gov.au/qld/observations/brisbane.shtml'
    get_html = requests.get(url)
    temp_search_string_location = f'tBRISBANE-tmp tBRISBANE-station-{location}">([0-9.]+)</td>'
    extract_temperature = re.findall(temp_search_string_location, get_html.text)
    return extract_temperature


def display_temp_to_user(location, extract_temperature):
    # display result to user
    if extract_temperature == 1 or extract_temperature == -1:
        display = f'The temperature in {location.title()} is {extract_temperature[0]} degree Celsius.'
    else:
        display = f'The temperature in {location.title()} is {extract_temperature[0]} degrees Celsius.'
    return print(display)


if __name__ == '__main__':
    main()
