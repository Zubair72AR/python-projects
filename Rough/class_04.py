import re

emails = [
    "zubair@gmail.com",
    "ali@yahoo.com",
    "fatima@hotmail.com",
    "ahmed@gmail.com",
    "sara@outlook.com",
    "bilal@gmail.com",
    "myname@gmail.com.xyz"
]

# Your code here
gmail_com = [e for e in emails if re.search(r"@gmail.com$", e)]
print(gmail_com)
