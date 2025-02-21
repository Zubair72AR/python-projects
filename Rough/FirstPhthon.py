# print("This is my first Python Message")

# num1 = float(input("number 01 -- "))
# num2 = int(input("number 02 -- "))
# print((num1 * num2) /2)

# dict = {
# "firstName" : "Zubair",
# "lastName" : "Ahmed",
# "age" : 18,
# "city" : "Karachi",
# "hobbies" : {
#     "1" : "Reading",
#     "2" : "Swimming",
#     "3" : "Cricket",
#     "4" : "History Videos"
# },
# "languages" : ("English", "Urdu", "Arabic")
# }

# dict["height_cm"] = 175

# print(dict.keys()) # for Printing only Keys
# print(dict.values()) # for Printing only Values
# print(dict.items())
# print(dict.pop("age"))
# print(dict.get("firstName")) # for Printing without Error if Didn't Exist then will not show any  Error


# Sets

# set1 = {"apple", "banana", "cherry"}
# set2 = {"apple", "banana", "mango", "orange"}
# union = (set1.union(set2))
# print(sorted(union))
# print("total number of fruits >>>", len(union))


# while loop

# value = 9
# number = 1
# while number <= 10:
#     print(f"{value} x {number} = {value * number}")
#     number += 1

# squireNUmbers = [0, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(squireNUmbers):
#     print(squireNUmbers[i])
#     i += 1

# names = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# index = 0
# while index < len(names):
#     print(names[index])
#     index += 1


# name = ["Zubair", "Babar", "Zohaib", "Shoaib", "Basit"]

# findName = "Shoaib"
# idx = 0

# while idx < len(name):
#     if name[idx] == findName:
#         print(f"Found {findName} at index {idx}")
#         break
#     idx += 1
# else:
#     print(f"{findName} not found")


# name = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in name:
#     print(i)

# for i in range(10): # VALUE in the RANGE is "STOP"
#     print("Print each number", i)
# for i in range(2, 10): # VALUE in the RANGE is "START - STOP"
#     print("Print 2 to 9 number", i)
# for i in range(4, 10, 2): # VALUE in the RANGE is "START - STOP - STEP"
#     print("Print 4 to 9 Even number", i)


# def oddEvenNumber(val):
#     if val % 2 == 0:
#         print(f"{val} is Even")
#     else:
#         print(f"{val} is Odd")


# oddEvenNumber(8888)


# def find(a):
#     if a == 0:
#         return
#     print(a)
#     find(a-1)


# find(10)


# text = "Hello WORLD"

# print("Original:", text)
# print("capitalize():", text.capitalize())
# print("upper():", text.upper())
# print("lower():", text.lower())
# print("title():", text.title())
# print("swapcase():", text.swapcase())
# print("casefold():", text.casefold())


# text1 = "HELLO WORLD"
# text2 = "Straße"  # جرمن زبان میں "Street" کا مطلب

# print(text1.lower())    # "hello world"
# print(text1.casefold())  # "hello world"

# print(text2.lower())    # "straße"
# print(text2.casefold())  # "strasse"  ✅ (مزید normalization)
# word1 = "straße"
# word2 = "STRASSE"

# print(word1.lower() == word2.lower())    # False ❌
# print(word1.casefold() == word2.casefold())  # True ✅

while True:
    try:
        x = int(input("Enter: "))
        break
    except:
        print("Error: Please enter number only.")
        continue
