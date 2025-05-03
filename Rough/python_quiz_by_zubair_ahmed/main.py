import streamlit as st

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - PAGE TITLE - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown(f"<p style='text-align: center; line-height: 1px; color: #666;font-weight: 100; font-size:14px;'>This quiz is for practice purposes only. Please do not consider it official.</p>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; line-height: 20px; margin-bottom: 20px;'>🚀 Test Your Python Knowledge!</h1>",
            unsafe_allow_html=True)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - QUIZ DATA - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
quiz_data = [
    {
        "concept": "Set Element Types and Hashability",
        "question": """
set_with_str_int = {"A", "B", 1, 2, 3}
set_with_tuple = {"A", "B", (1, 2, 3)}
set_with_dict = {"A", "B", {1: "C", 2: "D"}}
set_with_set = {"A", "B", {"C", "D"}}
set_with_list = {"A", "B", [1, 2, 3]}

print(set_with_str_int)
print(set_with_tuple)
print(set_with_dict)
print(set_with_set)
print(set_with_list)
""",
        "options": [
            "Only set_with_str_int and set_with_tuple work; others raise error",
            "All sets are valid and will print",
            "Only set_with_dict causes error",
            "Only set_with_list causes error"
        ],
        "answer": "Only set_with_str_int and set_with_tuple work; others raise error",
        "reason": "Only hashable (immutable) types can be elements in a set; dict, list, and set are unhashable"
    },
    {
        "concept": "Binary, Octal, and Hexadecimal Conversions",
        "question": """
bin_num = bin(25)
oct_num = oct(25)
hex_num = hex(25)

print(int(bin_num, 2))
print(int(oct_num, 8))
print(int(hex_num, 16))
""",
        "options": [
            "25 :gray[|] 25 :gray[|] 25",
            "Error: Invalid format for int conversion",
            "Binary, Octal, Hexadecimal numbers are printed in different formats",
            "2 :gray[|] 8 :gray[|] 16"
        ],
        "answer": "25 :gray[|] 25 :gray[|] 25",
        "reason": "`int()` correctly converts binary, octal, and hexadecimal string representations back to decimal"
    },
    {
        "concept": "Integer Caching and `id()` Function",
        "question": """
a = 123
b = 123

print(id(a))
print(id(b))
print(id(123))
""",
        "options": [
            "All three IDs are same",
            "All three IDs are different",
            "Only a and b have same ID, 123 is different",
            "Error: `id()` doesn't work on numbers"
        ],
        "answer": "All three IDs are same",
        "reason": "Small integers (typically -5 to 256) are cached and reused by Python"
    },
    {
        "concept": "Generators and Iteration",
        "question": """
def my_generator(my_lst):
    for char in my_lst:
        yield char

my_lst = ["A", "B", "C", "D", "E"]
x = my_generator(my_lst)

print(next(x))
print(next(x))
print(list(x))
print(list(x))
""",
        "options": [
            "A :gray[|] B :gray[|] ['C', 'D', 'E'] :gray[|] []",
            "next :gray[|] next :gray[|] ['A','B','C', 'D', 'E'] :gray[|] ['A','B','C', 'D', 'E']",
            "A :gray[|] B :gray[|] ['A','B','C', 'D', 'E'] :gray[|] []",
            "Error: Generator object cannot be iterated"
        ],
        "answer": "A :gray[|] B :gray[|] ['C', 'D', 'E'] :gray[|] []",
        "reason": "`next()` consumes values from the generator; once exhausted, repeated `list()` calls return empty list"
    },
    {
        "concept": "Merging Dictionaries with `update()` and Unpacking",
        "question": """
a = {1: "a", 2: "b"}
b = {3: "c", 4: "d"}
c = {5: "e", 6: "f"}

a.update(b)
print(a)
print({**a, **c})
""",
        "options": [
            "{1: 'a', 2: 'b', 3: 'c', 4: 'd'} :gray[|] {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}",
            "{1: 'a', 2: 'b', 3: 'c', 4: 'd'} :gray[|] {1: 'a', 2: 'b', 5: 'e', 6: 'f'}",
            "Error: Cannot merge dictionaries",
            "{1: 'a', 2: 'b', 3: 'c', 4: 'd'} :gray[|] Error"
        ],
        "answer": "{1: 'a', 2: 'b', 3: 'c', 4: 'd'} :gray[|] {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}",
        "reason": "`update()` merges the dictionaries, and `{**a, **c}` is used for unpacking and combining dictionaries."
    },
    {
        "concept": "Using `math.ceil()` for Rounding Up",
        "question": """
import math

print(math.ceil(-5.35))
print(math.ceil(5.35))
print(math.ceil(-96.99))
print(math.ceil(96.97))
""",
        "options": [
            "-5 :gray[|] 6 :gray[|] -96 :gray[|] 97",
            "-5 :gray[|] 5 :gray[|] -96 :gray[|] 96",
            "-6 :gray[|] 6 :gray[|] -97 :gray[|] 97",
            "Error: Invalid math operation"
        ],
        "answer": "-5 :gray[|] 6 :gray[|] -96 :gray[|] 97",
        "reason": "`math.ceil()` rounds numbers upwards, towards positive infinity, even for negative numbers"
    },
    {
        "concept": "Scope: `nonlocal` Keyword in Nested Functions",
        "question": """
city = "Karachi"

def outer_func():
    city = "Islamabad"
    print(city)

    def inner_func():
        nonlocal city
        city = "Lahore"
        print(city)

    inner_func()
    print(city)

outer_func()
print(city)
""",
        "options": [
            "Islamabad  :gray[|] Lahore  :gray[|] Lahore  :gray[|] Karachi",
            "Islamabad  :gray[|] Lahore  :gray[|] Islamabad  :gray[|] Karachi",
            "Islamabad  :gray[|] Lahore  :gray[|] Lahore  :gray[|] Lahore",
            "Error: `nonlocal` can't be used here"
        ],
        "answer": "Islamabad  :gray[|] Lahore  :gray[|] Lahore  :gray[|] Karachi",
        "reason": "`nonlocal` changes the variable in the nearest enclosing function, not global"
    },
    {
        "concept": "Dictionary with Duplicate Keys",
        "question": """
d = {'a':1, 'a':2, 'a':3}
print(len(d))
""",
        "options": [
            "1",
            "2",
            "3",
            "Error: Duplicate keys not allowed"
        ],
        "answer": "1",
        "reason": "Dictionaries cannot have duplicate keys; the last value overwrites the previous ones."
    },
    {
        "concept": "String to Number Conversion with `float()` and `int()`",
        "question": """
print(float("3.14"))
print(int("3.14"))
print(int("3"))
""",
        "options": [
            "3.14 :gray[|] Error: int() cannot convert string with decimal  :gray[|] 3",
            "3.14  :gray[|] Error: int() cannot convert string with decimal  :gray[|] Error: int() cannot convert string with decimal",
            "Error: float() cannot convert string with decimal  :gray[|] 3  :gray[|] 3",
            "3.14 :gray[|] 3.14 :gray[|] 3"
        ],
        "answer": "3.14 :gray[|] Error: int() cannot convert string with decimal  :gray[|] 3",
        "reason": "`float()` can handle decimals, but `int()` truncates the decimal part."
    },
    {
        "concept": "String Method: `partition()`",
        "question": """
two_nation = "Pakistan and India"

print(two_nation.partition("and")) # if word Exists
print(two_nation.partition("or")) # if word does't Exist
""",
        "options": [
            "('Pakistan ', 'and', ' India') :gray[|] ('Pakistan and India', '', '')",
            "('Pakistan ', 'and', ' India') :gray[|] ('Pakistan and India', 'or', 'or')",
            "('Pakistan ', 'and', ' India') :gray[|] ('Pakistan ', 'or', ' India')",
            "Error: partition() only splits existing words"
        ],
        "answer": "('Pakistan ', 'and', ' India') :gray[|] ('Pakistan and India', '', '')",
        "reason": "`partition()` splits at the first match; if not found, returns the string and two empty strings."
    },

    {
        "concept": "String Method: `find()` vs `rfind()`",
        "question": """
text = "Find in Left Right"

print(text.find("i")) # Find letter 'i'
print(text.find("ii")) # Find 'ii' in a row
print(text.find("i", 2)) # Find 'i' after index 2
print(text.rfind("i")) # Right-find letter 'i'
""",
        "options": [
            "1 :gray[|] Error :gray[|] 5 :gray[|] 14",
            "2 :gray[|] False :gray[|] 6 :gray[|] 15",
            "1 :gray[|] -1 :gray[|] 5 :gray[|] 14",
            "Error: `find` and `rfind` can't locate letters"
        ],
        "answer": "1 :gray[|] -1 :gray[|] 5 :gray[|] 14",
        "reason": "`find()` searches from left and `rfind()` from right — returns index if found, `-1` if not."
    },

    {
        "concept": "String Method: `split()` and `rsplit()` with `maxsplit`",
        "question": """
text = "1234123412341"
print(text.split("2"))
print(text.split("2", maxsplit=2))
print(text.rsplit("2", maxsplit=1))
""",
        "options": [
            "['1', '341', '341', '341'] :gray[|] ['1', '34', '12341'] :gray[|] ['123412341', '341']",
            "['1', '341', '341', '341'] :gray[|] ['1', '341', '3412341'] :gray[|] ['12341', '1341']",
            "['1', '341', '341', '341'] :gray[|] ['1', '341', '3412341'] :gray[|] ['123412341', '341']",
            "Error: maxsplit"
        ],
        "answer": "['1', '341', '341', '341'] :gray[|] ['1', '341', '3412341'] :gray[|] ['123412341', '341']",
        "reason": "`split()` cuts from left, `rsplit()` from right, `maxsplit` limits the number of splits."
    },
    {
        "concept": "String Method: `strip()` with Characters",
        "question": """
text = \"\"\"


    ###$$ Hallo $$###\"\"\"
text = text.strip()
print(text)
text = text.strip("$")
print(text)
text = text.strip("o $l#")
print(text)
""",
        "options": [
            "`###$$ Hallo $$###` :gray[|] `###$$ Hallo $$###` :gray[|] `Ha`",
            "`###$$ Hallo $$###`:gray[|] `### Hallo ###` :gray[|] `Ha`",
            "`###$$Hallo$$###` :gray[|] `###Hallo###` :gray[|] `Ha`",
            "Error: strip() does not work with multiple characters"
        ],
        "answer": "`###$$ Hallo $$###` :gray[|] `###$$ Hallo $$###` :gray[|] `Ha`",
        "reason": "`strip()` removes characters from both ends, not substrings, and is case-sensitive"
    },

    {
        "concept": "Tuple Syntax: Single Element Trap",
        "question": """
my_tuple: tuple = ("1")
print(type(my_tuple))
""",
        "options": [
            "<class 'tuple'>",
            "<class 'int'>",
            "Error: Invalid tuple definition",
            "<class 'str'>"
        ],
        "answer": "<class 'str'>",
        "reason": "Single-element tuples need a comma, without it Python treats it as an String/Integer/Float."
    },
    {
        "concept": "Using `exec()` to Execute Code from String",
        "question": """
text_str = \"\"\"
greeting = "Welcome"
print(greeting)

for x in range(1,5,2):
    print(x)

print(len(greeting))
\"\"\"

exec(text_str)

# WARNING:
# Never use exec() on untrusted files or user input unless you are completely sure of what the code contains. Always sanitize inputs to avoid security risks like code injection or remote code execution.
""",
        "options": [
            "Welcome :gray[|] 1 2 3 4 :gray[|] 7",
            "Welcome :gray[|] 1 2 3 4 5 :gray[|] 7",
            "Welcome :gray[|] 1 3 :gray[|] 7",
            "Error: exec() doesn't execute code"
        ],
        "answer": "Welcome :gray[|] 1 3 :gray[|] 7",
        "reason": "`exec()` executes the code, prints 'Welcome', loops with range(1, 5, 2), and prints the length of the greeting string."
    },


    {
        "concept": "Type Conversion: Boolean & Float to Integer",
        "question": """
print(int(True))
print(int(1))
print(int(1.0))
print(int(False))
print(int(0))
print(int(0.0))
""",
        "options": [
            "1 :gray[|] 1 :gray[|] 1 :gray[|] 0 :gray[|] 0 :gray[|] 0",
            "True :gray[|] 1 :gray[|] 1 :gray[|] False :gray[|] 0 :gray[|] 0",
            "True :gray[|] 1 :gray[|] 1.0 :gray[|] False :gray[|] 0 :gray[|] 0.0",
            "Error: Can't convert float or bool to int"
        ],
        "answer": "1 :gray[|] 1 :gray[|] 1 :gray[|] 0 :gray[|] 0 :gray[|] 0",
        "reason": "True == 1 and False == 0; float values without decimal converted to int directly."
    },

    {
        "concept": "Set with Mixed Data Types",
        "question": """
my_set = {True, 1, 1.0, False, 0, 0.0, "Babar", "babar"}
print(my_set)
""",
        "options": [
            "{True, 1, 1.0, False, 0, 0.0, 'Babar', 'babar'}",
            "{False, True, 'babar', 'Babar'}",
            "{True, 1, False, 0, 'Babar', 'babar'}",
            "Error: Duplicate values are not allowed in sets"
        ],
        "answer": "{False, True, 'babar', 'Babar'}",
        "reason": "True == 1 / 1.0 and False == 0 / 0.0 are equal, so duplicates removed."
    },
    {
        "concept": "String Method: `count()` and Case Sensitivity",
        "question": """
text = "National or International"
print(text.count("n"))
""",
        "options": [
            "3",
            "5",
            "Error: count() doesn't work on string",
            "4"
        ],
        "answer": "4",
        "reason": "`count()` method is case-sensitive and only counts lowercase 'n'."
    },
    {
        "concept": "F-String Debugging Feature (`= syntax`)",
        "question": """
person = "Zubair"
marks = 75
print(f"{person=}")
print(f"{marks=}")
print(f"{1+2=}")
""",
        "options": [
            "person='Zubair' :gray[|] marks=75 :gray[|] 1+2=3",
            "Zubair :gray[|] 75 :gray[|] 3",
            "Error: Invalid syntax for f-string with '='",
            "person=Zubair :gray[|] marks=75 :gray[|] 1+2=3"
        ],
        "answer": "person='Zubair' :gray[|] marks=75 :gray[|] 1+2=3",
        "reason": "`=` f-string debugging feature prints both the variable name and its value."
    },

    {
        "concept": "Extended Iterable Unpacking in Python",
        "question": """
players = ["Babar", "Naseem", "Rizwan", "Shaheen"]
first_player, *other_players, last_player = players
print(first_player)
print(other_players)
print(last_player)
""",
        "options": [
            "Babar :gray[|] ['Naseem', 'Rizwan'] :gray[|] Shaheen",
            "Babar :gray[|] Naseem :gray[|] Rizwan",
            "Error: Too many values to unpack",
            "' ' :gray[|] ['Babar', 'Naseem', 'Rizwan', 'Shaheen'] :gray[|] ' '"
        ],
        "answer": "Babar :gray[|] ['Naseem', 'Rizwan'] :gray[|] Shaheen",
        "reason": "`*other_players` absorbs middle values in unpacking"
    },
    {
        "concept": "Tuple vs Integer Assignment Confusion",
        "question": """
value:int = 1,125,256,199
print(type(value))
""",
        "options": [
            "<class 'tuple'>",
            "<class 'int'>",
            "Error: Invalid comma-separated integer",
            "<class 'list'>"
        ],
        "answer": "<class 'tuple'>",
        "reason": "Comma separates values, making it a tuple"
    },
    {
        "concept": "Rounding Numbers with `round()`",
        "question": """
round_figure: float = 12459.1234567
print(round(round_figure, 4))
print(round(round_figure, 2))
print(round(round_figure, -1))
print(round(round_figure, -3))
""",
        "options": [
            "12459.1235 :gray[|] 12459.12 :gray[|] 12460.0 :gray[|] 12000.0",
            "12459.1234 :gray[|] 12459.12 :gray[|] 12450.0 :gray[|] 12000.0",
            "Error: Negative precision not allowed",
            "12459.1235 :gray[|] 12459.12 :gray[|] 12459.0 :gray[|] 12459.0"
        ],
        "answer": "12459.1235 :gray[|] 12459.12 :gray[|] 12460.0 :gray[|] 12000.0",
        "reason": "`round()` handles decimal & negative precision correctly"
    },

    {
        "concept": "Number Formatting with Underscore & Comma",
        "question": """
large_number = 10000000000
print(f"{large_number:,}")
large_number2 = 10_000_000_000
print(large_number2)
""",
        "options": [
            "10,000,000,000 :gray[|] 10000000000",
            "10,000,000,000 :gray[|] 10_000_000_000",
            "Error: Underscore (_) not allowed in integers",
            "10000000000 :gray[|] 10_000_000_000"
        ],
        "answer": "10,000,000,000 :gray[|] 10000000000",
        "reason": "Comma formats number, underscore is ignored in value"
    },
    {
        "concept": "Dictionary `.setdefault()` Behavior",
        "question": """
countries = {"PAK": 92, "KSA": 966, "UAE": 971}
pakistan = countries.setdefault("PAK", 100)
print(pakistan)
""",
        "options": [
            "92",
            "100",
            "Error: Key already exists",
            "None"
        ],
        "answer": "92",
        "reason": "`setdefault()` returns existing value if key exists"
    },

    {
        "concept": "Dictionary `.get()` Method with Default Value",
        "question": """
countries = {"PAK": 92, "KSA": 966, "UAE": 971, "AFG": 93}
print(countries.get("USA"))
print(countries.get("USA", "Not-Found"))
""",
        "options": [
            "None :gray[|] Not-Found",
            "Error: 'USA' Key not found",
            "Not-Found :gray[|] Not-Found",
            "None :gray[|] None"
        ],
        "answer": "None :gray[|] Not-Found",
        "reason": "If key not found: `.get()` returns `None` or the provided default"
    },

    {
        "concept": "Sorting List with `key=len` and `reverse=True`",
        "question": """
countries = ["Pakistan", "Iran", "UAE", "Afghanistan", "China"]
print(sorted(countries, key=len, reverse=True))
""",
        "options": [
            "['Afghanistan', 'China', 'Iran', 'Pakistan', 'UAE']",
            "['UAE', 'Iran', 'China', 'Pakistan', 'Afghanistan']",
            "['Afghanistan', 'Pakistan', 'China', 'Iran', 'UAE']",
            "Error: `key=len` can't be used with `reverse`"
        ],
        "answer": "['Afghanistan', 'Pakistan', 'China', 'Iran', 'UAE']",
        "reason": "`sorted()` uses length for sorting, reverse=True reverses the order"
    },

    {
        "concept": "Zip with Dictionary and List in Loops",
        "question": """
countries = ["PAK", "KSA", "UAE", "USA"]
name_num = {"Zubair": 99, "Babar": 75}

for (key, value), country in zip(name_num.items(), countries):
    print(f"{key} - {value}%, {country}.")
""",
        "options": [
            "Zubair - 99%, PAK. :gray[|] Babar - 75%, KSA. :gray[|] Zubair - 99%, UAE. :gray[|] Babar - 75%, USA.",
            "Zubair - 99%, PAK. :gray[|] Babar - 75%, KSA.",
            "Error: Invalid pairing of country and name",
            "PAK - Zubair%. :gray[|] KSA - 99%. :gray[|] UAE - Babar%. :gray[|] USA - 75%."
        ],
        "answer": "Zubair - 99%, PAK. :gray[|] Babar - 75%, KSA.",
        "reason": "Zip pairs dictionary items with list elements"
    },


    {
        "concept": "Range with Negative Step",
        "question": """
my_list:range = list(range(10, 3, -2))
print(my_list)
""",
        "options": [
            "[10, 8, 6, 4]",
            "[10, 8, 6]",
            "[2, 4, 6, 8, 10]",
            "Error: Invalid Step"
        ],
        "answer": "[10, 8, 6, 4]",
        "reason": "Steps by -2, so it includes 4 but not 3"
    },
    {
        "concept": "Iterator Exhaustion in Python",
        "question": """
serial = [1,2,3]
my_iterator = iter(serial)

print(list(my_iterator))
print(list(my_iterator))
""",
        "options": [
            "[1, 2, 3] :gray[|] [1, 2, 3]",
            "[1, 2, 3] :gray[|] []",
            "Error: Iterator can't be reused",
            "[1, 2, 3] :gray[|] StopIteration Error"
        ],
        "answer": "[1, 2, 3] :gray[|] []",
        "reason": "Iterator exhausts after first_player complete loop"
    },
    {
        "concept": "String Multiplication & `capitalize()` Behavior",
        "question": """
lol = ("HA" * 4) + "..!"
print(lol.capitalize())
""",
        "options": [
            "Hahahaha..!",
            "HA4..!",
            "Error: Strings are immutable",
            "HaHaHaHa..!"
        ],
        "answer": "Hahahaha..!",
        "reason": "`capitalize()` makes first_player letter uppercase, rest lowercase"
    }, {
        "concept": "Multiple Variable Assignment & `print()` Parameters",
        "question": """
a, b, c = "Zubair", True, 15

print(b, a , c, sep=", ", end=".")
""",
        "options": [
            "True, Zubair, 15.",
            "True Zubair 15",
            "Error: ``sep`` and ``end`` can't be used together",
            "Zubair, True, 15"
        ],
        "answer": "True, Zubair, 15.",
        "reason": "`sep` defines separator, `end` defines output ending"
    },
    {
        "concept": "Boolean Logic with `any()` Function",
        "question": """
age = [0, 25, 18]
name = ["", "", "Naseem"]
numbers = [0, 0, 0]

print(any(age))
print(any(name))
print(any(numbers))
""",
        "options": [
            "True :gray[|] True :gray[|] False",
            "False :gray[|] False :gray[|] False",
            "Error: Empty strings not allowed",
            "True :gray[|] False :gray[|] True"
        ],
        "answer": "True :gray[|] True :gray[|] False",
        "reason": "`any()` returns True if at least one truthy value exists"
    },
    {
        "concept": "Boolean Logic with `all()` Function",
        "question": """
age = [0, 25, 18]
name = ["Zubair", "Babar", "Naseem"]
numbers = [0, 0, ""]

print(all(age))
print(all(name))
print(all(numbers))
""",
        "options": [
            "False :gray[|] True :gray[|] False",
            "True :gray[|] True :gray[|] True",
            "Error: Zero breaks all()",
            "False :gray[|] False :gray[|] False"
        ],
        "answer": "False :gray[|] True :gray[|] False",
        "reason": "`all()` returns False if any falsy value (like 0) exists"
    },
    {
        "concept": "Try-Except-Finally Execution Flow",
        "question": """
    def test():
        try:
            x = 1 / 0
        except ZeroDivisionError:
            return "Error Caught"
        finally:
            print("Finally Block Running")

    print(test())
    """,
        "options": [
            "Error Caught (Finally Block also runs)",
            "Error Caught",
            "Finally Block Running",
            "``Except`` return skips ``finally`` block"
        ],
        "answer": "Error Caught (Finally Block also runs)",
        "reason": "Finally always runs, even after return"
    },
    {
        "concept": "Boolean Logic with `or`, `and`, and `not`",
        "question": """
    name = "Babar Azam"
    age = 18
    position = None

    print(name or age or position)
    print(name and age and position)
    print(not age)
    """,
        "options": [
            "Babar Azam :gray[|] None :gray[|] False",
            "Babar Azam :gray[|] None :gray[|] True",
            "Error: None breaks `and` operation",
            "True :gray[|] False :gray[|] True"
        ],
        "answer": "Babar Azam :gray[|] None :gray[|] False",
        "reason": "`or` gives first_player truthy, `and` gives last_player falsy (None), `not` negates age"
    },
    {
        "concept": "String Immutability and Replacement",
        "question": """
    my_String = "Hallo World"
    print(my_String.replace("World", "Pakistan"))
    """,
        "options": [
            "Hallo Pakistan",
            "Hallo World",
            "Error: replace() doesn't work on immutable strings",
            "Error: Strings are immutable, can't modify in place"
        ],
        "answer": "Hallo Pakistan",
        "reason": "String replaced without modifying original"
    },
    {
        "concept": "Count Occurrences in List",
        "question": """
    my_list = ["A", "A", "a", "B", "C", "C", "D"]
    print(sum(1 for letter in my_list if letter == "A"))
    """,
        "options": [
            "3",
            "2",
            "1",
            "Error: LOOP should return letter not count"
        ],
        "answer": "2",
        "reason": "Count of 'A' is 2"
    },
    {
        "concept": "Absolute Value Function",
        "question": """
        num1 = 5
        num2 = abs(-5)
        print(num1 + num2)
        """,
        "options": ["5", "10", "0", "Error"],
        "answer": "10",
        "reason": "abs returns positive"
    }, {
        "concept": "Boolean Conversion Logic",
        "question": """
    print(bool(0))
    print(bool(""))
    print(bool(-1))
    """,
        "options": [
            "False :gray[|] False :gray[|] True",
            "True :gray[|] False :gray[|] False",
            "False :gray[|] False :gray[|] False",
            "True :gray[|] True :gray[|] Error"
        ],
        "answer": "False :gray[|] False :gray[|] True",
        "reason": "0/Empty False, -1 True"
    },
    {
        "concept": "List Reference Behavior",
        "question": """
        x = [1,2]
        y = x
        y.append(3)
        print(x)
        """,
        "options": ["[1, 2]", "[1, 2, 3]", "[3]", "Error"],
        "answer": "[1, 2, 3]",
        "reason": "Same list reference"
    },
    {
        "concept": "Negative Indexing",
        "question": """
        my_list = [1, 2, 3]
        print(my_list[-1])
        """,
        "options": ["1", "2", "3", "Error"],
        "answer": "3",
        "reason": "Negative index last_player"
    },
    {
        "concept": "String to List Conversion",
        "question": """
        print(list("abc"))
        """,
        "options": ["['abc']", "['a','b','c']", "Error", "None"],
        "answer": "['a','b','c']",
        "reason": "String to list"
    },
    {
        "concept": "Set Behavior - Unique Elements",
        "question": """
        print(len(set([1, 2, 2, 3])))
        """,
        "options": ["4", "3", "2", "Error"],
        "answer": "3",
        "reason": "Set removes duplicates"
    },
    {
        "concept": "String Indexing",
        "question": """
        print("hello"[1])
        """,
        "options": ["h", "e", "l", "o"],
        "answer": "e",
        "reason": "Index starts zero"
    },
    {
        "concept": "List Clear Method",
        "question": """
        x = [1, 2, 3]
        x.clear()
        print(len(x))
        """,
        "options": ["0", "3", "Error", "None"],
        "answer": "0",
        "reason": "clear makes empty"
    },
    {
        "concept": "Data Type Identification",
        "question": """
        print(type([]))
        """,
        "options": ["list", "dict", "tuple", "set"],
        "answer": "list",
        "reason": "[] defines list"
    },
    {
        "concept": "String Immutability",
        "question": """
    greeting = "hallo"
    greeting = greeting + "!"
    print(greeting.capitalize())
    """,
        "options": ["hallo!", "Hallo!", "error due to immutable", "None"],
        "answer": "Hallo!",
        "reason": "Strings create new object"
    }
]


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - QUIZ FORM - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
score = 0
if "submitted" not in st.session_state:
    st.session_state.submitted = False

for index, q in enumerate(quiz_data, start=1):
    correct = q["answer"]
    st.write("")
    st.write(
        f":gray[{index}. What will be the output?] Concept: :violet[{q['concept']}]")
    st.code(q["question"])
    options = q["options"]
    selected_answer = st.radio(
        ":gray[Select your answer:]", options, index=None, key=f"q{index}")

    # If the quiz is submitted, display the result
    if selected_answer == correct:
        st.success(f"✅ Correct! 📢 :green[\"{q["reason"]}\"]")
        score += 1
    elif selected_answer is None and st.session_state.submitted:
        st.warning(
            f"⚠️ You left this question! :gray[Correct Answer is:] :green[\"**{correct}**\"]")
    elif selected_answer is not None:
        st.error(
            f"❌ Wrong! :gray[Correct Answer is:] :green[\"**{correct}**\"]")

# Show Result
if st.button("🎯 Show My Total Score"):
    st.session_state.submitted = True
    st.subheader(f"✅ Your Total Score: {score} / {len(quiz_data)}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - FOOTER - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown("""<p style="color: #2f3038; text-align:center;">Made with ❤ by Zubair Ahmed</p>""",
            unsafe_allow_html=True)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# - - - - - - - - - - CSS STYLING AND LINKS - - - - - - - - - -
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
st.markdown("""
<style>.q_heading{
color: white !important;
font-weight:100 !important;
font-size: 18px !important;
line-height: 5px !important;
margin-top:20px !important;  
.concept{
font-weight:800 !important;
color: crimson !important;  
}</style>""", unsafe_allow_html=True)
