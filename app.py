import re

text = "My Phone number is 1234567890"
pattern = r"\w\w\w\w\w\w\w\w\w\w"  # Matches any ten consecutive digits

match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")