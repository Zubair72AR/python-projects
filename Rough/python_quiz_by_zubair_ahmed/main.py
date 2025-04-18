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
        "reason": "Negative index last"
    },
    {
        "concept": "String Multiplication",
        "question": """
        print("A" * 3)
        """,
        "options": ["AAA", "A3", "Error", "3A"],
        "answer": "AAA",
        "reason": "String repeated"
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
