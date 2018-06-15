"""Ile jest palindromicznych liczb trzycyfrowych które są jednoczesnie kwadratami liczb całkowitych i jakie to liczby"""
num_list = list(range(1000))

new_list = [str(i) for i in num_list]
result = []
for i in new_list:
    if i == i[::-1]:
        try:
            for v in range(-100, 100):
                if v * v == int(i):
                    result.append(i)
        except ZeroDivisionError:
            continue

print(result)