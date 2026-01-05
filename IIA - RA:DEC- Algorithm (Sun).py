import math
from datetime import datetime

def getsuncoordinates(date):

    # Days since J2000
    J2000 = datetime(2000, 1, 1, 12) # J2000 epoch
    deltadays = (date - J2000).total_seconds() / (24 * 3600)

    meanlongitude = (280.46646 + 0.985647 * deltadays) % 360
    meananomaly = (357.52911 + 0.98560028 * deltadays) % 360
    meananomalyrad = math.radians(meananomaly)

    ecliptical_longitude = (meanlongitude + 1.915 * math.sin(meananomalyrad) + 0.020 * math.sin(2 * meananomalyrad)) % 360

    ecliptical_longitude_rad = math.radians(ecliptical_longitude)

    obliquity = 23.439292 - 0.000013 * deltadays
    obliquityrad = math.radians(obliquity)

    # RA & DEC Calculations
    x = math.cos(ecliptical_longitude_rad)
    y = math.cos(obliquityrad) * math.sin(ecliptical_longitude_rad)
    z = math.sin(obliquityrad) * math.sin(ecliptical_longitude_rad)

    RA = math.atan2(y, x)
    DEC = math.asin(z)

    # RA & DEC Constants Conversion
    RAhours = (math.degrees(RA) / 15) % 24
    DECdegrees = math.degrees(DEC)

    return RAhours, DECdegrees

# Format Conversion of RA & DEC
def converttohms(decimalhours):
    hours = int(decimalhours)
    minutes = int((decimalhours - hours) * 60)
    seconds = (decimalhours - hours - minutes / 60) * 3600
    return f"{hours:02}h{minutes:02}m{seconds:02.1f}s"

def converttodms(decimaldegrees):
    sign = "+" if decimaldegrees >= 0 else "-"
    decimaldegrees = abs(decimaldegrees)
    degrees = int(decimaldegrees)
    minutes = int((decimaldegrees - degrees) * 60)
    seconds = (decimaldegrees - degrees - minutes / 60) * 3600
    return f"{sign}{degrees:02}°{minutes:02}'{seconds:02.1f}''"

# Date Input

date = datetime(2025, 1, 1, 00, 00, 00) #YY-MM-DD-HH-MM-SS Format
RA, DEC = getsuncoordinates(date)

RAhms = converttohms(RA)
DECdms = converttodms(DEC)

print(f"Date: {date}")
print(f"Right Ascension (RA): {RAhms}")
print(f"Declination (DEC): {DECdms}")