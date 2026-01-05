import math
from datetime import datetime

def getmooncoordinates(date):
    
    J2000 = datetime(2000, 1, 1, 12)
    deltadays = (date - J2000).total_seconds() / (24 * 3600)
    
    longitude = (218.316 + 13.176396 * deltadays) % 360
    anomalymoon = (134.963 + 13.064993 * deltadays) % 360
    anomalysun = (357.529 + 0.98560028 * deltadays) % 360
    elongation = (297.850 + 12.190749 * deltadays) % 360
    latitude = (93.272 + 13.229350 * deltadays) % 360

    # Radian Conversion
    longitude_rad = math.radians(longitude)
    anomalymoon_rad = math.radians(anomalymoon)
    anomalysun_rad = math.radians(anomalysun)
    elongation_rad = math.radians(elongation)
    latitude_rad = math.radians(latitude)

    # Ecliptic longitude
    lon = longitude + 6.289 * math.sin(anomalymoon_rad) \
            + 1.274 * math.sin(2*elongation_rad - anomalymoon_rad) \
            + 0.658 * math.sin(2*elongation_rad) \
            + 0.214 * math.sin(2*anomalymoon_rad) \
            + 0.186 * math.sin(anomalysun_rad) \
            - 0.059 * math.sin(2*elongation_rad - 2*anomalymoon_rad) \
            - 0.057 * math.sin(2*elongation_rad - anomalysun_rad - anomalymoon_rad) \
            + 0.053 * math.sin(2*elongation_rad + anomalymoon_rad) \
            + 0.046 * math.sin(2*elongation_rad - anomalysun_rad) \
            + 0.041 * math.sin(anomalysun_rad - anomalymoon_rad)
    longitude_rad = math.radians(lon % 360)

    # Ecliptic latitude
    lat = 5.128 * math.sin(latitude_rad) \
            + 0.280 * math.sin(anomalymoon_rad + latitude_rad) \
            + 0.277 * math.sin(anomalymoon_rad - latitude_rad) \
            + 0.173 * math.sin(2*elongation_rad - latitude_rad) \
            + 0.055 * math.sin(2*elongation_rad + latitude_rad - anomalymoon_rad) \
            + 0.046 * math.sin(2*elongation_rad - latitude_rad - anomalymoon_rad)
    lat_rad = math.radians(lat)

    # Obliquity
    obliquity = 23.439292 - 0.000013 * deltadays
    eps_rad = math.radians(obliquity)

    # Equatorial Coordinates
    x = math.cos(longitude_rad) * math.cos(lat_rad)
    y = math.cos(eps_rad) * math.sin(longitude_rad) * math.cos(lat_rad) - math.sin(eps_rad) * math.sin(lat_rad)
    z = math.sin(eps_rad) * math.sin(longitude_rad) * math.cos(lat_rad) + math.cos(eps_rad) * math.sin(lat_rad)

    RA = math.atan2(y, x)
    DEC = math.asin(z)

    RAhours = (math.degrees(RA) / 15) % 24
    DECdegrees = math.degrees(DEC)

    return RAhours, DECdegrees

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

date = datetime(2025, 1, 1, 0, 0, 0)
RA, DEC = getmooncoordinates(date)

RAhms = converttohms(RA)
DECdms = converttodms(DEC)

print(f"Date: {date}")
print(f"Right Ascension (RA): {RAhms}")
print(f"Declination (DEC): {DECdms}")