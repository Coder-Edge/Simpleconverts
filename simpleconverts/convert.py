# simpleconverts/convert.py

class ConversionError(Exception):
    pass


# -------------------------------
# DISTANCES
# -------------------------------
_distance_factors = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.34,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254,
}

# MASSE
_mass_factors = {
    "g": 1.0,
    "kg": 1000.0,
    "t": 1_000_000.0,
    "lb": 453.592,
    "oz": 28.3495,
}

# VOLUME
_volume_factors = {
    "l": 1.0,
    "ml": 0.001,
    "cl": 0.01,
    "gal": 3.78541,
    "qt": 0.946353,
    "pt": 0.473176,
    "cup": 0.24,
    "floz": 0.0295735,
}

# TEMPS
_time_factors = {
    "s": 1.0,
    "min": 60.0,
    "h": 3600.0,
    "d": 86400.0,
    "week": 604800.0,
    "month": 2_629_746.0,
    "year": 31_556_952.0,
}

# ENERGIE
_energy_factors = {
    "j": 1.0,
    "kj": 1000.0,
    "kwh": 3.6e6,
    "cal": 4.184,
    "kcal": 4184.0,
}

# TEMPERATURES
def _convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convertir vers Celsius
    if from_unit == "c":
        c = value
    elif from_unit == "f":
        c = (value - 32) * 5 / 9
    elif from_unit == "k":
        c = value - 273.15
    else:
        raise ConversionError(f"Unité de température non reconnue : {from_unit}")

    # Convertir de Celsius vers cible
    if to_unit == "c":
        return c
    elif to_unit == "f":
        return c * 9 / 5 + 32
    elif to_unit == "k":
        return c + 273.15
    else:
        raise ConversionError(f"Unité de température non reconnue : {to_unit}")


# API PRINCIPALE
def convert(value, from_unit, to_unit):
    """Convertit une valeur entre deux unités courantes"""
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    # Températures
    if from_unit in ["c", "f", "k"] and to_unit in ["c", "f", "k"]:
        return _convert_temperature(value, from_unit, to_unit)

    # Distances
    if from_unit in _distance_factors and to_unit in _distance_factors:
        return value * _distance_factors[from_unit] / _distance_factors[to_unit]

    # Masse
    if from_unit in _mass_factors and to_unit in _mass_factors:
        return value * _mass_factors[from_unit] / _mass_factors[to_unit]

    # Volume
    if from_unit in _volume_factors and to_unit in _volume_factors:
        return value * _volume_factors[from_unit] / _volume_factors[to_unit]

    # Temps
    if from_unit in _time_factors and to_unit in _time_factors:
        return value * _time_factors[from_unit] / _time_factors[to_unit]

    # Energie
    if from_unit in _energy_factors and to_unit in _energy_factors:
        return value * _energy_factors[from_unit] / _energy_factors[to_unit]

    raise ConversionError(f"Conversion impossible entre {from_unit} et {to_unit}")
