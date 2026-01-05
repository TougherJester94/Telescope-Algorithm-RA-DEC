import math
from datetime import datetime

def getsaturncoordinates(date):
    J2000 = datetime(2000, 1, 1, 12)
    deltadays = (date - J2000).total_seconds()/(24 * 3600)

# Contination in a later sequence
