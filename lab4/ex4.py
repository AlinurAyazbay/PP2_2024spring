import re

# Sample text containing email addresses
text = """
Email addresses:
- john.doe@example.com
- jane.doe@example.com
- info@example.com
- invalid.email@com
"""

# Regular expression pattern to match email addresses
txt = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Find all email addresses in the text using the pattern
emails = re.findall(txt, text)

# Print the matched email addresses
print("Matched email addresses:")
for email in emails:
    print(email)
