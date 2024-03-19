# Define the string
s = "Happy birthday"

# Specify the file path
file_path = "demofile.txt"

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    # Write the string to the file
    file.write(s)

print("String has been successfully written to the file:", file_path)
