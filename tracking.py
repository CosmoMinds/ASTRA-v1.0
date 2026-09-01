import json
import requests

from skyfield.api import EarthSatellite, load, wgs84

from datetime import datetime, timezone, timedelta


AMSAT_URL = "https://www.amsat.org/tle/current/dailytle.txt"

OBSERVER_LATITUDE = 18.52
OBSERVER_LONGITUDE = 73.86


def load_tracking_satellites():

    with open("tracking_satellites.json", "r") as file:
        satellites = json.load(file)

    return satellites


def download_tle_data():

    response = requests.get(
        AMSAT_URL,
        timeout=10
    )

    response.raise_for_status()

    return response.text


def find_satellite_tle(tle_text, satellite_name):

    lines = tle_text.splitlines()

    for index in range(len(lines) - 2):

        name = lines[index].strip()

        line1 = lines[index + 1].strip()

        line2 = lines[index + 2].strip()

        if not line1.startswith("1 "):
            continue

        if not line2.startswith("2 "):
            continue

        if name.upper() == satellite_name.upper():

            return line1, line2

    return None


def calculate_position(line1, line2, satellite_name):

    ts = load.timescale()

    satellite = EarthSatellite(
        line1,
        line2,
        satellite_name,
        ts
    )

    now = datetime.now(timezone.utc)

    t = ts.from_datetime(now)

    geocentric = satellite.at(t)

    subpoint = wgs84.subpoint(geocentric)

    latitude = subpoint.latitude.degrees

    longitude = subpoint.longitude.degrees

    altitude = subpoint.elevation.km

    return latitude, longitude, altitude


def utc_to_ist(utc_time):

    ist_offset = timedelta(
        hours=5,
        minutes=30
    )

    ist_time = utc_time + ist_offset

    return ist_time


def track_satellites():

    satellites = load_tracking_satellites()

    utc_time = datetime.now(timezone.utc)

    ist_time = utc_to_ist(utc_time)

    print()

    print("====================================================")
    print("             Astra Real-Time Tracking")
    print("====================================================")

    print(
        "UTC Time :",
        utc_time.strftime("%Y-%m-%d %H:%M:%S")
    )

    print(
        "IST Time :",
        ist_time.strftime("%Y-%m-%d %H:%M:%S")
    )

    print("Observer Latitude  :", OBSERVER_LATITUDE)

    print("Observer Longitude :", OBSERVER_LONGITUDE)

    print("====================================================")

    active_satellites = []

    for satellite in satellites:

        if satellite["status"].lower() == "active":

            active_satellites.append(satellite)

    if not active_satellites:

        print()
        print("No active satellites available for tracking.")

        input("Press Enter to return to Dashboard...")

        return

    print()

    print("Downloading orbital data from AMSAT...")

    try:

        tle_text = download_tle_data()

    except requests.RequestException as error:

        print()
        print("Unable to download orbital data from AMSAT.")

        print("Error :", error)

        input("Press Enter to return to Dashboard...")

        return

    print()

    print("Orbital data downloaded successfully.")

    print("====================================================")

    for satellite in active_satellites:

        print()

        print("Satellite :", satellite["name"])

        print("NORAD ID  :", satellite["norad_id"])

        print("Status    :", satellite["status"])

        tle = find_satellite_tle(
            tle_text,
            satellite["name"]
        )

        if tle:

            line1, line2 = tle

            latitude, longitude, altitude = calculate_position(
                line1,
                line2,
                satellite["name"]
            )

            print(
                "Latitude  :",
                round(latitude, 4)
            )

            print(
                "Longitude :",
                round(longitude, 4)
            )

            print(
                "Altitude  :",
                round(altitude, 2),
                "km"
            )

        else:

            print("TLE data unavailable from AMSAT.")

        print("----------------------------------------------------")

    input("Press Enter to return to Dashboard...")