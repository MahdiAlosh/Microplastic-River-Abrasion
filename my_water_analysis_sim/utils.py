import math as m
import re

def extract_type_identifier(type_name):
    """
    Extract the type number (and optional suffix) from a type name string.
    Example: "Typ 10: Kiesgeprägte Ströme" -> 10
             "Typ: 15_g" -> 15_g
    """
    match = re.search(r"Typ\s*(\d+(\.\d+)?(_[A-Za-z]+)?)|\(Typ:\s*(\d+(\.\d+)?(_[A-Za-z]+)?)\)", type_name)
    if match:
        # Return the matched group (either from "Typ <number>" or "(Typ: <number>)") and normalize to lowercase
        return (match.group(1) or match.group(4)).lower()
    return None

def powerInput(slope, strickler):
    p = 980   # density in kg/m³
    g = 9.81  # acceleration in m/s²
    h = 1.53  # height of water column in m
    e = 0.1   # coefficient of efficiency
    r = h     # hydraulic radius ^2/3

    i = slope     # slope from Excel sheet converted to decimal number
    k = strickler # strickler coefficient from Excel sheet

    result = (p * g * h * i) * (k * m.pow(r, 2/3) * m.pow(i, 1/2)) * e 
    
    return result