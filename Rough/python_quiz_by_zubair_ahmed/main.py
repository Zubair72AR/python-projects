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
            "person='Zubair' marks=75 1+2=3",
            "Zubair 75 3",
            "Error: Invalid syntax for f-string with '='",
            "person=Zubair marks=75 1+2=3"
        ],
        "answer": "person='Zubair' marks=75 1+2=3",
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
            "Babar ['Naseem', 'Rizwan'] Shaheen",
            "'Babar' 'Naseem' 'Rizwan'",
            "Error: Too many values to unpack",
            "['Babar', 'Naseem', 'Rizwan', 'Shaheen']"
        ],
        "answer": "Babar ['Naseem', 'Rizwan'] Shaheen",
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
            "12459.1235\n12459.12\n12460.0\n12000.0",
            "12459.1234\n12459.12\n12450.0\n12000.0",
            "Error: Negative precision not allowed",
            "12459.1235\n12459.12\n12459.0\n12459.0"
        ],
        "answer": "12459.1235\n12459.12\n12460.0\n12000.0",
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
            "10,000,000,000\n10000000000",
            "10,000,000,000\n10_000_000_000",
            "Error: Underscore (_) not allowed in integers",
            "10000000000\n10_000_000_000"
        ],
        "answer": "10,000,000,000\n10000000000",
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
            "None Not-Found",
            "Error: 'USA' Key not found",
            "Not-Found Not-Found",
            "None None"
        ],
        "answer": "None Not-Found",
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
            "Zubair - 99%, PAK. Babar - 75%, KSA. Zubair - 99%, UAE. Babar - 75%, USA.",
            "Zubair - 99%, PAK. Babar - 75%, KSA.",
            "Error: Invalid pairing of country and name",
            "PAK - Zubair%. KSA - 99%. UAE - Babar%. USA - 75%."
        ],
        "answer": "Zubair - 99%, PAK. Babar - 75%, KSA.",
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
            "[1, 2, 3] [1, 2, 3]",
            "[1, 2, 3] []",
            "Error: Iterator can't be reused",
            "[1, 2, 3] StopIteration Error"
        ],
        "answer": "[1, 2, 3] []",
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
            "True True False",
            "False False False",
            "Error: Empty strings not allowed",
            "True False True"
        ],
        "answer": "True True False",
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
            "False True False",
            "True True True",
            "Error: Zero breaks all()",
            "False False False"
        ],
        "answer": "False True False",
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
            "Babar Azam None False",
            "Babar Azam None True",
            "Error: None breaks `and` operation",
            "Babar Azam None True"
        ],
        "answer": "Babar Azam None False",
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
            "False False True",
            "True False False",
            "False False False",
            "True True Error"
        ],
        "answer": "False False True",
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
