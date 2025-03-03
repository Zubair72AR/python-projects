from decimal import Decimal

conversion_data: dict = {
    "Area": {
        "Square Kilometre": Decimal("1000000"),
        "Square Metre": Decimal("1"),
        "Square Mile": Decimal("2589988.11"),
        "Square Yard": Decimal("0.836127"),
        "Square Foot": Decimal("0.092903"),
        "Square Inch": Decimal("0.00064516"),
        "Hectare": Decimal("10000"),
        "Acre": Decimal("4046.86")
    },
    "Data Transfer Rate": {
        "Bit per second": Decimal("1"),
        "Kilobit per second": Decimal("1000"),
        "Kilobyte per second": Decimal("8000"),
        "Kibibit per second": Decimal("1024"),
        "Megabit per second": Decimal("1000000"),
        "Megabyte per second": Decimal("8000000"),
        "Mebibit per second": Decimal("1048576"),
        "Gigabit per second": Decimal("1000000000"),
        "Gigabyte per second": Decimal("8000000000"),
        "Gibibit per second": Decimal("1073741824"),
        "Terabit per second": Decimal("1000000000000"),
        "Terabyte per second": Decimal("8000000000000"),
        "Tebibit per second": Decimal("1099511627776")
    },
    "Digital Storage": {
        "Bit": Decimal("1"),
        "Kilobit": Decimal("1000"),
        "Kibibit": Decimal("1024"),
        "Megabit": Decimal("1000000"),
        "Mebibit": Decimal("1048576"),
        "Gigabit": Decimal("1000000000"),
        "Gibibit": Decimal("1073741824"),
        "Terabit": Decimal("1000000000000"),
        "Tebibit": Decimal("1099511627776"),
        "Petabit": Decimal("1000000000000000"),
        "Pebibit": Decimal("1125899906842624"),
        "Byte": Decimal("8"),
        "Kilobyte": Decimal("8000"),
        "Kibibyte": Decimal("8192"),
        "Megabyte": Decimal("8000000"),
        "Mebibyte": Decimal("8388608"),
        "Gigabyte": Decimal("8000000000"),
        "Gibibyte": Decimal("8589934592"),
        "Terabyte": Decimal("8000000000000"),
        "Tebibyte": Decimal("8796093022208"),
        "Petabyte": Decimal("8000000000000000"),
        "Pebibyte": Decimal("9007199254740992")
    },
    "Energy": {
        "Joule": Decimal("1"),
        "Kilojoule": Decimal("1000"),
        "Gram calorie": Decimal("4.184"),
        "Kilocalorie": Decimal("4184"),
        "Watt hour": Decimal("3600"),
        "Kilowatt-hour": Decimal("3600000"),
        "Electronvolt": Decimal("1.60218e-19"),
        "British thermal unit": Decimal("1055.06"),
        "US therm": Decimal("105505600"),
        "Foot-pound": Decimal("1.35582")
    },
    "Frequency": {
        "Hertz": Decimal("1"),
        "Kilohertz": Decimal("1000"),
        "Megahertz": Decimal("1000000"),
        "Gigahertz": Decimal("1000000000")
    },
    "Fuel Economy": {
        "Mile per US gallon": Decimal("1"),
        "Mile per gallon": Decimal("1.20095"),
        "Kilometer per liter": Decimal("2.35215"),
        "Litre per 100 kilometres": Decimal("235.215")
    },
    "Length": {
        "Kilometre": Decimal("1000"),
        "Metre": Decimal("1"),
        "Centimetre": Decimal("0.01"),
        "Millimetre": Decimal("0.001"),
        "Micrometre": Decimal("1e-6"),
        "Nanometre": Decimal("1e-9"),
        "Mile": Decimal("1609.34"),
        "Yard": Decimal("0.9144"),
        "Foot": Decimal("0.3048"),
        "Inch": Decimal("0.0254"),
        "Nautical Mile": Decimal("1852")
    },
    "Mass": {
        "Kilogram": Decimal("1"),
        "Tonne": Decimal("0.001"),
        "Gram": Decimal("1000"),
        "Milligram": Decimal("1000000"),
        "Microgram": Decimal("1000000000"),
        "Imperial ton": Decimal("0.000984207"),
        "US ton": Decimal("0.00110231"),
        "Stone": Decimal("0.157473"),
        "Pound": Decimal("2.20462"),
        "Ounce": Decimal("35.27396")
    },
    "Plane Angle": {
        "Radian": Decimal("1"),
        "Degree": Decimal("57.2958"),
        "Gradian": Decimal("63.662"),
        "Milliradian": Decimal("1000"),
        "Arcsecond": Decimal("206264.806"),
        "Minute of arc": Decimal("3437.75")
    },
    "Pressure": {
        "Pascal": Decimal("1"),
        "Bar": Decimal("100000"),
        "Pound per square inch": Decimal("6894.76"),
        "Standard atmosphere": Decimal("101325"),
        "Torr": Decimal("133.322")
    },
    "Speed": {
        "Kilometre per hour": Decimal("1"),
        "Mile per hour": Decimal("1.60934"),
        "Foot per second": Decimal("1.09728"),
        "Metre per second": Decimal("3.6"),
        "Knot": Decimal("1.852")
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
        "Second": 1,  # Base unit
        "Nanosecond": 1e-9,  # 1 ns = 1e-9 seconds
        "Microsecond": 1e-6,  # 1 µs = 1e-6 seconds
        "Millisecond": 1e-3,  # 1 ms = 1e-3 seconds
        "Minute": 60,  # 1 min = 60 seconds
        "Hour": 3600,  # 1 hr = 3600 seconds
        "Day": 86400,  # 1 day = 86400 seconds
        "Week": 604800,  # 1 week = 604800 seconds
        "Month": 2.628e+6,  # 1 month ≈ 2.628e+6 seconds (average)
        "Year": 3.154e+7,  # 1 year ≈ 3.154e+7 seconds (average)
        "Decade": 3.154e+8,  # 1 decade = 10 years
        "Century": 3.154e+9  # 1 century = 100 years
    },
    "Volume": {
        "Liter": 1,  # Base unit
        "US liquid gallon": 3.78541,  # 1 US gallon = 3.78541 liters
        "US liquid quart": 0.946353,  # 1 US quart = 0.946353 liters
        "US liquid pint": 0.473176,  # 1 US pint = 0.473176 liters
        "US legal cup": 0.24,  # 1 US cup = 0.24 liters
        "US fluid ounce": 0.0295735,  # 1 US fl oz = 0.0295735 liters
        "US tablespoon": 0.0147868,  # 1 US tbsp = 0.0147868 liters
        "US teaspoon": 0.00492892,  # 1 US tsp = 0.00492892 liters
        "Cubic meter": 1000,  # 1 m³ = 1000 liters
        "Milliliter": 0.001,  # 1 mL = 0.001 liters
        "Imperial gallon": 4.54609,  # 1 Imperial gallon = 4.54609 liters
        "Imperial quart": 1.13652,  # 1 Imperial quart = 1.13652 liters
        "Imperial pint": 0.568261,  # 1 Imperial pint = 0.568261 liters
        "Imperial cup": 0.284131,  # 1 Imperial cup = 0.284131 liters
        "Imperial fluid ounce": 0.0284131,  # 1 Imperial fl oz = 0.0284131 liters
        "Imperial tablespoon": 0.0177582,  # 1 Imperial tbsp = 0.0177582 liters
        "Imperial teaspoon": 0.00591939,  # 1 Imperial tsp = 0.00591939 liters
        "Cubic foot": 28.3168,  # 1 ft³ = 28.3168 liters
        "Cubic inch": 0.0163871  # 1 in³ = 0.0163871 liters
    }
}
