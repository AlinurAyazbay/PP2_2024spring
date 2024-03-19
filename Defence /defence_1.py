lst = input()
lower = list(filter(lambda x: x.upper(), lst))
upper = list(filter(lambda x: x.lower(), lst))
print(f'{len(lower)} - lowercase letters\n{len(upper)} - uppercase letters')