#ex1
l = [1, 2, 3, 5]
print(eval('*'.join(map(str, l))))

#ex2
def count(text):
    upcount = 0
    lowcount = 0
    for char in text:
        if char.isupper():
            upcount += 1
        elif char.islower():
            lowcount += 1
    return upcount, lowcount
input_string = "Hello Daryn"
upcount, lowcount = count(input_string)
print("uppercase", upcount)
print("lowercase", lowcount)
#ex3
def is_palindrome(string):
    clean_string = string.replace(" ", "").lower()
    return clean_string == clean_string[::-1]
input_string = "Daryn is umni guy"
result = is_palindrome(input_string)
if result:
    print("palindrome")
else:
    print("not a palindrome")

#ex4
import time 
num = int(input("Enter the number: "))
milsec = int(input("Enter the delay time: "))
sec = milsec/1000
time.sleep(sec)
sqrt = num ** 0.5
print(f"Square root of {num} after {milsec} miliseconds is {sqrt}")

#ex5
def all_true(tuple_values):
    return all(tuple_values)
my_tuple = (True, True, True)
result = all_true(my_tuple)
print(result)
