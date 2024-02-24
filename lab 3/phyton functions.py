def grams_to_ounces(n):
    n = n * 28.3495231
    print(n)
n = int(input())
grams_to_ounces(n)


def conversion(n):
    k = 5/9
    l = n -32
    n = k* l
    print(n)
n = int(input())
conversion(n)

def solve(numheads, numlegs):
    if numheads > numlegs or numlegs % 2 != 0:
        print("No solution exists.")
        return
    r = (numlegs - 2 * numheads) / 2
    c = numheads - r

    print("Number of rabbits:", int(r))
    print("Number of chickens:", int(c))

solve(35, 94)


def prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
    

def filtprime(numbers):
    return [num for num in numbers if prime(num)]


numbers = [int(x) for x in input("numbers: ").split()]
prime_numbers = filtprime(numbers)
print("Prime numbers:", prime_numbers)


