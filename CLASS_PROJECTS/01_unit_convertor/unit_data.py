conversion_data: dict = {
    "Area": {
        "Square Kilometre": 1_000_000,  # 1 km² = 1,000,000 m²
        "Square Metre": 1,  # Base unit
        "Square Mile": 2_589_988.11,  # 1 mi² = 2,589,988.11 m²
        "Square Yard": 0.836127,  # 1 yd² = 0.836127 m²
        "Square Foot": 0.092903,  # 1 ft² = 0.092903 m²
        "Square Inch": 0.00064516,  # 1 in² = 0.00064516 m²
        "Hectare": 10_000,  # 1 ha = 10,000 m²
        "Acre": 4046.86  # 1 acre = 4,046.86 m²
    },
    "Data Transfer Rate": {
        "Bit per second": 1,  # Base unit (bps)
        "Kilobit per second": 1_000,  # 1 Kbps = 1,000 bps
        "Kilobyte per second": 8_000,  # 1 KBps = 8,000 bps
        "Kibibit per second": 1_024,  # 1 Kibps = 1,024 bps
        "Megabit per second": 1_000_000,  # 1 Mbps = 1,000,000 bps
        "Megabyte per second": 8_000_000,  # 1 MBps = 8,000,000 bps
        "Mebibit per second": 1_048_576,  # 1 Mibps = 1,048,576 bps
        "Gigabit per second": 1_000_000_000,  # 1 Gbps = 1,000,000,000 bps
        "Gigabyte per second": 8_000_000_000,  # 1 GBps = 8,000,000,000 bps
        "Gibibit per second": 1_073_741_824,  # 1 Gibps = 1,073,741,824 bps
        "Terabit per second": 1_000_000_000_000,  # 1 Tbps = 1,000,000,000,000 bps
        "Terabyte per second": 8_000_000_000_000,  # 1 TBps = 8,000,000,000,000 bps
        "Tebibit per second": 1_099_511_627_776  # 1 Tibps = 1,099,511,627,776 bps
    },
    "Digital Storage": {
        "Bit": 1,  # Base unit
        "Kilobit": 1_000,  # 1 Kb = 1,000 bits
        "Kibibit": 1_024,  # 1 Kib = 1,024 bits
        "Megabit": 1_000_000,  # 1 Mb = 1,000,000 bits
        "Mebibit": 1_048_576,  # 1 Mib = 1,048,576 bits
        "Gigabit": 1_000_000_000,  # 1 Gb = 1,000,000,000 bits
        "Gibibit": 1_073_741_824,  # 1 Gib = 1,073,741,824 bits
        "Terabit": 1_000_000_000_000,  # 1 Tb = 1,000,000,000,000 bits
        "Tebibit": 1_099_511_627_776,  # 1 Tib = 1,099,511,627,776 bits
        "Petabit": 1_000_000_000_000_000,  # 1 Pb = 1,000,000,000,000,000 bits
        "Pebibit": 1_125_899_906_842_624,  # 1 Pib = 1,125,899,906,842,624 bits

        "Byte": 8,  # 1 Byte = 8 bits
        "Kilobyte": 8_000,  # 1 KB = 8,000 bits
        "Kibibyte": 8_192,  # 1 KiB = 8,192 bits
        "Megabyte": 8_000_000,  # 1 MB = 8,000,000 bits
        "Mebibyte": 8_388_608,  # 1 MiB = 8,388,608 bits
        "Gigabyte": 8_000_000_000,  # 1 GB = 8,000,000,000 bits
        "Gibibyte": 8_589_934_592,  # 1 GiB = 8,589,934,592 bits
        "Terabyte": 8_000_000_000_000,  # 1 TB = 8,000,000,000,000 bits
        "Tebibyte": 8_796_093_022_208,  # 1 TiB = 8,796,093,022,208 bits
        "Petabyte": 8_000_000_000_000_000,  # 1 PB = 8,000,000,000,000,000 bits
        "Pebibyte": 9_007_199_254_740_992  # 1 PiB = 9,007,199,254,740,992 bits
    },
    "Energy": {
        "Joule": 1,  # Base unit
        "Kilojoule": 1_000,  # 1 kJ = 1,000 J
        "Gram calorie": 4.184,  # 1 cal = 4.184 J
        "Kilocalorie": 4_184,  # 1 kcal = 4,184 J
        "Watt hour": 3_600,  # 1 Wh = 3,600 J
        "Kilowatt-hour": 3_600_000,  # 1 kWh = 3,600,000 J
        "Electronvolt": 1.60218e-19,  # 1 eV = 1.60218 × 10⁻¹⁹ J
        "British thermal unit": 1_055.06,  # 1 BTU = 1,055.06 J
        "US therm": 105_505_600,  # 1 therm = 105,505,600 J
        "Foot-pound": 1.35582  # 1 ft⋅lb = 1.35582 J
    },
    "Frequency": {
        "Hertz": 1,  # Base unit
        "Kilohertz": 1_000,  # 1 kHz = 1,000 Hz
        "Megahertz": 1_000_000,  # 1 MHz = 1,000,000 Hz
        "Gigahertz": 1_000_000_000  # 1 GHz = 1,000,000,000 Hz
    },
    "Fuel Economy": {
        "Mile per US gallon": 1,  # Base unit
        "Mile per gallon": 1.20095,  # UK mile per gallon to US mile per gallon
        "Kilometer per liter": 2.35215,  # 1 km/L = 2.35215 mpg (US)
        "Litre per 100 kilometres": 235.215  # 1 L/100km = 235.215 mpg (US)
    },
    "Length": {
        "Kilometre": 1000,  # 1 km = 1000 m
        "Metre": 1,  # Base unit
        "Centimetre": 0.01,  # 1 cm = 0.01 m
        "Millimetre": 0.001,  # 1 mm = 0.001 m
        "Micrometre": 1e-6,  # 1 µm = 1e-6 m
        "Nanometre": 1e-9,  # 1 nm = 1e-9 m
        "Mile": 1609.34,  # 1 mile ≈ 1609.34 m
        "Yard": 0.9144,  # 1 yard = 0.9144 m
        "Foot": 0.3048,  # 1 foot = 0.3048 m
        "Inch": 0.0254,  # 1 inch = 0.0254 m
        "Nautical Mile": 1852  # 1 nautical mile = 1852 m
    },
    "Mass": {
        "Kilogram": 1,  # Base unit
        "Tonne": 0.001,  # 1 kg = 0.001 Tonne
        "Gram": 1000,  # 1 kg = 1000 g
        "Milligram": 1_000_000,  # 1 kg = 1,000,000 mg
        "Microgram": 1_000_000_000,  # 1 kg = 1,000,000,000 µg
        "Imperial ton": 0.000984207,  # 1 kg = 0.000984207 UK tons
        "US ton": 0.00110231,  # 1 kg = 0.00110231 US tons
        "Stone": 0.157473,  # 1 kg = 0.157473 stones
        "Pound": 2.20462,  # 1 kg = 2.20462 lbs
        "Ounce": 35.27396  # 1 kg = 35.27396 oz
    },
    "Plane Angle": {
        "Radian": 1,  # Base unit
        "Degree": 57.2958,  # 1 Radian = 57.2958 Degrees
        "Gradian": 63.662,  # 1 Radian = 63.662 Gradians
        "Milliradian": 1000,  # 1 Radian = 1000 Milliradians
        "Arcsecond": 206264.806,  # 1 Radian = 206264.806 Arcseconds
        "Minute of arc": 3437.75  # 1 Radian = 3437.75 Arcminutes
    },
    "Pressure": {
        "Pascal": 1,  # Base unit
        "Bar": 1e5,  # 1 Bar = 100000 Pascal
        "Pound per square inch": 6894.76,  # 1 PSI = 6894.76 Pascal
        "Standard atmosphere": 101325,  # 1 atm = 101325 Pascal
        "Torr": 133.322  # 1 Torr = 133.322 Pascal
    },
    "Speed": {
        "Mile per hour": 1.60934,  # 1 mph = 1.60934 km/h
        "Foot per second": 1.09728,  # 1 ft/s = 1.09728 km/h
        "Metre per second": 3.6,  # 1 m/s = 3.6 km/h
        "Kilometre per hour": 1,  # Base unit
        "Knot": 1.852  # 1 knot = 1.852 km/h
    },
    "Temperature": {
        "Degree Celsius": {
            "Fahrenheit": lambda c: (c * 9/5) + 32,
            "Kelvin": lambda c: c + 273.15
        },
        "Fahrenheit": {
            "Degree Celsius": lambda f: (f - 32) * 5/9,
            "Kelvin": lambda f: (f - 32) * 5/9 + 273.15
        },
        "Kelvin": {
            "Degree Celsius": lambda k: k - 273.15,
            "Fahrenheit": lambda k: (k - 273.15) * 9/5 + 32
        }
    },
    "Time": {
        "Nanosecond": {"Second": 1e-9},  # 1 nanosecond = 1e-9 seconds
        "Microsecond": {"Second": 1e-6},  # 1 microsecond = 1e-6 seconds
        "Millisecond": {"Second": 1e-3},  # 1 millisecond = 1e-3 seconds
        "Second": {
            "Millisecond": 1000,  # 1 second = 1000 milliseconds
            "Minute": 1/60,  # 1 second = 1/60 minutes
            "Hour": 1/3600  # 1 second = 1/3600 hours
        },
        "Minute": {
            "Second": 60,  # 1 minute = 60 seconds
            "Hour": 1/60,  # 1 minute = 1/60 hours
            "Day": 1/1440  # 1 minute = 1/1440 days
        },
        "Hour": {
            "Second": 3600,  # 1 hour = 3600 seconds
            "Minute": 60,  # 1 hour = 60 minutes
            "Day": 1/24,  # 1 hour = 1/24 days
            "Week": 1/168  # 1 hour = 1/168 weeks
        },
        "Day": {
            "Second": 86400,  # 1 day = 86400 seconds
            "Hour": 24,  # 1 day = 24 hours
            "Week": 1/7,  # 1 day = 1/7 weeks
            # 1 day ≈ 1/30.44 months (average)
            "Month": 1/30.44
        },
        "Week": {
            "Second": 604800,  # 1 week = 604800 seconds
            "Day": 7,  # 1 week = 7 days
            # 1 week ≈ 1/4.345 months (average)
            "Month": 1/4.345,
            # 1 week ≈ 1/52.143 years (average)
            "Year": 1/52.143
        },
        "Month": {
            # 1 month ≈ 2.628e+6 seconds (average)
            "Second": 2.628e+6,
            "Day": 30.44,  # 1 month ≈ 30.44 days (average)
            "Year": 1/12  # 1 month = 1/12 years
        },
        "Calendar year": {
            # 1 calendar year ≈ 3.154e+7 seconds (average)
            "Second": 3.154e+7,
            # 1 calendar year ≈ 365.25 days (average, accounting for leap years)
            "Day": 365.25,
            "Decade": 1/10,  # 1 calendar year = 1/10 decades
            "Century": 1/100  # 1 calendar year = 1/100 centuries
        },
        "Decade": {
            "Year": 10,  # 1 decade = 10 years
            "Century": 1/10  # 1 decade = 1/10 centuries
        },
        "Century": {
            "Year": 100,  # 1 century = 100 years
            "Decade": 10  # 1 century = 10 decades
        }
    },
    "Volume": {
        # 1 US liquid gallon ≈ 3.78541 liters
        "US liquid gallon": {"Liter": 3.78541},
        # 1 US liquid quart ≈ 0.946353 liters
        "US liquid quart": {"Liter": 0.946353},
        # 1 US liquid pint ≈ 0.473176 liters
        "US liquid pint": {"Liter": 0.473176},
        # 1 US legal cup = 0.24 liters
        "US legal cup": {"Liter": 0.24},
        # 1 US fluid ounce ≈ 0.0295735 liters
        "US fluid ounce": {"Liter": 0.0295735},
        # 1 US tablespoon ≈ 0.0147868 liters
        "US tablespoon": {"Liter": 0.0147868},
        # 1 US teaspoon ≈ 0.00492892 liters
        "US teaspoon": {"Liter": 0.00492892},
        # 1 cubic meter = 1000 liters
        "Cubic meter": {"Liter": 1000},
        "Liter": {
            "Cubic meter": 0.001,  # 1 liter = 0.001 cubic meters
            "Milliliter": 1000  # 1 liter = 1000 milliliters
        },
        # 1 milliliter = 0.001 liters
        "Milliliter": {"Liter": 0.001},  # 1 Imperial gallon ≈ 4.54609 liters
        # 1 Imperial quart ≈ 1.13652 liters
        "Imperial gallon": {"Liter": 4.54609},
        # 1 Imperial pint ≈ 0.568261 liters
        "Imperial quart": {"Liter": 1.13652},
        # 1 Imperial cup ≈ 0.284131 liters
        "Imperial pint": {"Liter": 0.568261},
        # 1 Imperial fluid ounce ≈ 0.0284131 liters
        "Imperial cup": {"Liter": 0.284131},
        # 1 Imperial tablespoon ≈ 0.0177582 liters
        "Imperial fluid ounce": {"Liter": 0.0284131},
        # 1 Imperial teaspoon ≈ 0.00591939 liters
        "Imperial tablespoon": {"Liter": 0.0177582},
        # 1 cubic foot ≈ 28.3168 liters
        "Imperial teaspoon": {"Liter": 0.00591939},
        "Cubic foot": {"Liter": 28.3168},  # 1 cubic inch ≈ 0.0163871 liters
        "Cubic inch": {"Liter": 0.0163871}
    },
}
