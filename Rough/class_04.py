# Convert Number into Emoji 🥰
num_emoji_dict = {"1": "1️⃣ ", "2": "2️⃣ ", "3": "3️⃣ ", "4": "4️⃣ ",
                  "5": "5️⃣ ", "6": "6️⃣ ", "7": "7️⃣ ", "8": "8️⃣ ", "9": "9️⃣ ", "0": "0️⃣ "}


def is_vowels(value):
    # Make Dict of Tracing Each Vowels Quantity
    vowels_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    # For Loop for Provided Value
    for v in value.lower():
        # Check Each Word Include Vowels
        if v in vowels_count:
            # if Find Vowels increase Value by 1
            vowels_count[v] += 1

    # Get Sum of All Vowels
    total = sum(vowels_count.values())
    # Result
    result = f"Total Vowels are : {total} in \"{value}\"\n𝐀 = {vowels_count['a']} , 𝐄 = {vowels_count['e']} , 𝐈 = {vowels_count['i']} , 𝐎 = {vowels_count['o']} , 𝐔 = {vowels_count['u']}"
    # Replace Result Digits into Emoji
    for key, val in num_emoji_dict.items():
        result = result.replace(key, val)
    return result


# Get User Input
user_input = input("Please enter your value: ")
# Print & Call Function with Given User Input
print(is_vowels(user_input))
