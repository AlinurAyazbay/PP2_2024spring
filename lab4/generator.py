#ex1 
def squares(N):
    for i in range(1, N+1):
        yield i**2
N = int(input())
for square in squares(N):
    print(square)

#ex2 
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)
n = int(input())
print(", ".join(even_numbers(n)))

#ex3
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input())
for num in divisible(n):
    print(num)

#ex4
def squares(a, b):
    for i in range(a, b + 1):
        yield i**2
a = int(input())
b = int(input())
for square in squares(a, b):
    print(square)

#ex5
def down(n):
    while n >= 0:
        yield n
        n = n-1
n = int(input())
for num in down(n):
    print(num)

