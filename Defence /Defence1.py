import re
def extract_numbers(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    # Convert the extracted numbers from strings to integers
    numbers = [int(number) for number in numbers]
    return numbers
# Example text containing numbers
text = "There are 10 apples and 20 oranges in the basket."
# Extract numbers from the text
numbers = extract_numbers(text)
# Print the extracted numbers
print("Numbers extracted from the text:", numbers)